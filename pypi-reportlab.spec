#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-reportlab
Version  : 3.6.8
Release  : 88
URL      : https://files.pythonhosted.org/packages/50/c7/f80ab0ff9c7f7dc0b537fad0ee929ea5e56091b3f72de8e04ab3e02086b6/reportlab-3.6.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/50/c7/f80ab0ff9c7f7dc0b537fad0ee929ea5e56091b3f72de8e04ab3e02086b6/reportlab-3.6.8.tar.gz
Summary  : The Reportlab Toolkit
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.0 OFL-1.0
Requires: pypi-reportlab-license = %{version}-%{release}
Requires: pypi-reportlab-python = %{version}-%{release}
Requires: pypi-reportlab-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pillow)
BuildRequires : python3-dev

%description
This directory is the home of various ReportLab tools.
They are packaged such that they can be used more easily.

%package license
Summary: license components for the pypi-reportlab package.
Group: Default

%description license
license components for the pypi-reportlab package.


%package python
Summary: python components for the pypi-reportlab package.
Group: Default
Requires: pypi-reportlab-python3 = %{version}-%{release}

%description python
python components for the pypi-reportlab package.


%package python3
Summary: python3 components for the pypi-reportlab package.
Group: Default
Requires: python3-core
Provides: pypi(reportlab)
Requires: pypi(pillow)

%description python3
python3 components for the pypi-reportlab package.


%prep
%setup -q -n reportlab-3.6.8
cd %{_builddir}/reportlab-3.6.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1646240761
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-reportlab
cp %{_builddir}/reportlab-3.6.8/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-reportlab/638e7067709f6721a407b256bd4ed84cb1737106
cp %{_builddir}/reportlab-3.6.8/src/reportlab/fonts/bitstream-vera-license.txt %{buildroot}/usr/share/package-licenses/pypi-reportlab/b3245f6ac784e19a10843831b45b5944c62e3ccc
cp %{_builddir}/reportlab-3.6.8/src/reportlab/license.txt %{buildroot}/usr/share/package-licenses/pypi-reportlab/638e7067709f6721a407b256bd4ed84cb1737106
cp %{_builddir}/reportlab-3.6.8/src/rl_addons/renderPM/libart_lgpl/COPYING %{buildroot}/usr/share/package-licenses/pypi-reportlab/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-reportlab/638e7067709f6721a407b256bd4ed84cb1737106
/usr/share/package-licenses/pypi-reportlab/b3245f6ac784e19a10843831b45b5944c62e3ccc
/usr/share/package-licenses/pypi-reportlab/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
