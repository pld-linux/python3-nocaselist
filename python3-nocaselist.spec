#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	A case-insensitive list for Python
Summary(pl.UTF-8):	Lista dla Pythona ignorująca wielkość liter
Name:		python3-nocaselist
Version:	2.1.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/nocaselist/
Source0:	https://files.pythonhosted.org/packages/source/n/nocaselist/nocaselist-%{version}.tar.gz
# Source0-md5:	30a83f342cdb5a5a6ae20785daa7de94
URL:		https://pypi.org/project/nocaselist/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.4
%if %{with tests}
BuildRequires:	python3-pytest >= 6.2.5
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class NocaseList is a case-insensitive list that preserves the
original lexical case of its items.

%description -l pl.UTF-8
Klasa NocaseList to ignorująca wielkość liter lista, zachowująca
oryginalną wielkość liter elementów.

%prep
%setup -q -n nocaselist-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m zipfile -e build-3/*.whl build-3-test
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest -o pythonpath="$PWD/build-3-test" tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.md README.md SECURITY.md
%{py3_sitescriptdir}/nocaselist
%{py3_sitescriptdir}/nocaselist-%{version}.dist-info
