#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	A case-insensitive list for Python
Summary(pl.UTF-8):	Lista dla Pythona ignorująca wielkość liter
Name:		python-nocaselist
# keep 1.x here for python2 support
Version:	1.1.1
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/nocaselist/
Source0:	https://files.pythonhosted.org/packages/source/n/nocaselist/nocaselist-%{version}.tar.gz
# Source0-md5:	5683b96dc116bf0efb318dc3b763a28f
URL:		https://pypi.org/project/nocaselist/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest >= 4.3.1
BuildRequires:	python-six >= 1.14.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 6.2.5
BuildRequires:	python3-six >= 1.14.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class NocaseList is a case-insensitive list that preserves the
original lexical case of its items.

%description -l pl.UTF-8
Klasa NocaseList to ignorująca wielkość liter lista, zachowująca
oryginalną wielkość liter elementów.

%package -n python3-nocaselist
Summary:	A case-insensitive list for Python
Summary(pl.UTF-8):	Lista dla Pythona ignorująca wielkość liter
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-nocaselist
Class NocaseList is a case-insensitive list that preserves the
original lexical case of its items.

%description -n python3-nocaselist -l pl.UTF-8
Klasa NocaseList to ignorująca wielkość liter lista, zachowująca
oryginalną wielkość liter elementów.

%prep
%setup -q -n nocaselist-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/nocaselist
%{py_sitescriptdir}/nocaselist-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-nocaselist
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/nocaselist
%{py3_sitescriptdir}/nocaselist-%{version}-py*.egg-info
%endif
