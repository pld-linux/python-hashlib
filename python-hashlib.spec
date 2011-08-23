%define		module	hashlib
Summary:	Python secure hash and message digest module
Name:		python-%{module}
Version:	20081119
Release:	1
License:	PSF
Group:		Libraries/Python
Source0:	http://code.krypto.org/python/hashlib/hashlib-%{version}.tar.gz
# Source0-md5:	09dea11f5b826718d2032db210183d3c
URL:		http://code.krypto.org/python/hashlib/
BuildRequires:	python-devel < 1:2.5
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python secure hash and message digest module MD5, SHA1, SHA224,
SHA256, SHA384 and SHA512 (backported from Python 2.5).

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitedir} \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*hashlib.py[oc]
