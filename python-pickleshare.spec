%global pypi_name pickleshare

Name:           python-%{pypi_name}
Version:        0.7.4
Release:        1
Summary:        Tiny 'shelve'-like database with concurrency support

License:        MIT
URL:            https://github.com/pickleshare/pickleshare
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
 
BuildRequires:  python-setuptools
BuildRequires:  python3-devel

%description
PickleShare - a small ‘shelve’ like data store with concurrency support.

Like shelve, a PickleShareDB object acts like a normal dictionary. 
Unlike shelve, many processes can access the database simultaneously. 
Changing a value in database is immediately visible to other processes 
accessing the same database.

Concurrency is possible because the values are stored in separate files. 
Hence the “database” is a directory where all files are governed 
by PickleShare.

%package -n     python2-%{pypi_name}
Summary:        Tiny 'shelve'-like database with concurrency support
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}

PickleShare - a small ‘shelve’ like data store with concurrency support.

Like shelve, a PickleShareDB object acts like a normal dictionary. 
Unlike shelve, many processes can access the database simultaneously. 
Changing a value in database is immediately visible to other processes 
accessing the same database.

Concurrency is possible because the values are stored in separate files. 
Hence the “database” is a directory where all files are governed 
by PickleShare.

%prep
%setup -qn %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# fix interpreter
sed -i 's/\/usr\/bin\/env python/\/usr\/bin\/python/' pickleshare.py

cp -a . %py2dir

%build
python setup.py build
pushd %py2dir
python2 setup.py build

%install
python setup.py install --root=%buildroot
pushd %py2dir
python2 setup.py install --root=%buildroot

%files -n python2-%{pypi_name} 
%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-4
- Rebuild for Python 3.6

* Wed Nov 16 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.4-3
- Do not own __pycache__ dir

* Sat Oct 01 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.4-2
- Fix typos and interpreter strings

* Sat Sep 24 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.4-1
- Update to 0.7.4

* Fri Aug 12 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.7.3-1
- Initial package.
