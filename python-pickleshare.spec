%global pypi_name pickleshare

Name:           python-%{pypi_name}
Version:	0.7.5
Release:	2
Summary:        Tiny 'shelve'-like database with concurrency support

License:        MIT
URL:            https://github.com/pickleshare/pickleshare
Source0:	https://files.pythonhosted.org/packages/d8/b6/df3c1c9b616e9c0edbc4fbab6ddd09df9535849c64ba51fcb6531c32d4d8/pickleshare-0.7.5.tar.gz
BuildArch:      noarch
 
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

%prep
%setup -qn %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# fix interpreter
sed -i 's/\/usr\/bin\/env python/\/usr\/bin\/python/' pickleshare.py

%build
%py_build

%install
%py_install

%files
%{py3_puresitedir}/%{pypi_name}.py
%{py3_puresitedir}/%{pypi_name}-%{version}-py?.?.egg-info
%{py3_puresitedir}/__pycache__/*
