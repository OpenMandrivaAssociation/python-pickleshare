%global pypi_name pickleshare

Name:           python-%{pypi_name}
Version:	0.7.5
Release:	8
Summary:        Tiny 'shelve'-like database with concurrency support

License:        MIT
URL:            https://github.com/ipython/pickleshare
Source0:	https://files.pythonhosted.org/packages/source/p/pickleshare/pickleshare-%{version}.tar.gz
BuildArch:      noarch
 
BuildSystem:	python
BuildRequires:  python%{pyver}dist(setuptools)

%description
PickleShare - a small 'shelve' like data store with concurrency support.

Like shelve, a PickleShareDB object acts like a normal dictionary. 
Unlike shelve, many processes can access the database simultaneously. 
Changing a value in database is immediately visible to other processes 
accessing the same database.

Concurrency is possible because the values are stored in separate files. 
Hence the "database" is a directory where all files are governed 
by PickleShare.

%files
%{py_puresitedir}/%{pypi_name}.py
%{py_puresitedir}/%{pypi_name}-%{version}-py*.*.egg-info
