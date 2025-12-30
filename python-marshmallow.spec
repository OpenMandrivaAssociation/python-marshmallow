Name:		python-marshmallow
Version:	4.1.0
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/m/marshmallow/marshmallow-%{version}.tar.gz
Summary:	A lightweight library for converting complex datatypes to and from native Python datatypes.
URL:		https://pypi.org/project/marshmallow/
License:	None
Group:		Development/Python

Requires:   python%{pyver}dist(packaging) >= 17

BuildSystem:	python

BuildArch:	noarch

%description
A lightweight library for converting complex datatypes to and from native Python datatypes.

%files
%{py_sitedir}/marshmallow
%{py_sitedir}/marshmallow-*.*-info
