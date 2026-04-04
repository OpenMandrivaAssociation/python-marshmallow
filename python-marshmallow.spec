%define module marshmallow

Name:		python-marshmallow
Version:	4.3.0
Release:	1
Summary:	A library for converting to and from native Python datatypes
License:	None
Group:		Development/Python
URL:		https://pypi.org/project/marshmallow/
Source0:	https://files.pythonhosted.org/packages/source/m/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
A lightweight library for converting complex datatypes to and from native
Python datatypes.

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
