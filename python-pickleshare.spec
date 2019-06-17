%global pypi_name pickleshare

Name:           python-%{pypi_name}
Version:        0.7.4
Release:        1
Summary:        Tiny 'shelve'-like database with concurrency support

License:        MIT
URL:            https://github.com/pickleshare/pickleshare
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-setuptools
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
%py_build
pushd %py2dir
python2 setup.py build

%install
%py_install
pushd %py2dir
python2 setup.py install --root=%{buildroot}

%files -n python2-%{pypi_name} 
%{py_puresitedir}/%{pypi_name}.py*
%{py_puresitedir}/%{pypi_name}-%{version}-py?.?.egg-info

%files
%{py3_puresitedir}/%{pypi_name}.py
%{py3_puresitedir}/%{pypi_name}-%{version}-py?.?.egg-info
%{py3_puresitedir}/__pycache__/*

