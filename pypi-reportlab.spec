#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-reportlab
Version  : 4.0.5
Release  : 101
URL      : https://files.pythonhosted.org/packages/10/ec/4a423a97e53399c05889cd12f789ab9175f2498c77b47cc006b6482b71c1/reportlab-4.0.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/10/ec/4a423a97e53399c05889cd12f789ab9175f2498c77b47cc006b6482b71c1/reportlab-4.0.5.tar.gz
Summary  : The Reportlab Toolkit
Group    : Development/Tools
License  : BSD-3-Clause OFL-1.0
Requires: pypi-reportlab-license = %{version}-%{release}
Requires: pypi-reportlab-python = %{version}-%{release}
Requires: pypi-reportlab-python3 = %{version}-%{release}
Requires: pypi(freetype_py)
Requires: pypi(rlpycairo)
BuildRequires : buildreq-distutils3
BuildRequires : freetype-dev
BuildRequires : pypi(freetype_py)
BuildRequires : pypi(rlpycairo)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
Requires: pypi(freetype_py)
Requires: pypi(pillow)
Requires: pypi(rlpycairo)

%description python3
python3 components for the pypi-reportlab package.


%prep
%setup -q -n reportlab-4.0.5
cd %{_builddir}/reportlab-4.0.5
pushd ..
cp -a reportlab-4.0.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695743160
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . freetype-py
pypi-dep-fix.py . rlPyCairo
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . freetype-py
pypi-dep-fix.py . rlPyCairo
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-reportlab
cp %{_builddir}/reportlab-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-reportlab/638e7067709f6721a407b256bd4ed84cb1737106 || :
cp %{_builddir}/reportlab-%{version}/src/reportlab/fonts/bitstream-vera-license.txt %{buildroot}/usr/share/package-licenses/pypi-reportlab/b3245f6ac784e19a10843831b45b5944c62e3ccc || :
cp %{_builddir}/reportlab-%{version}/src/reportlab/license.txt %{buildroot}/usr/share/package-licenses/pypi-reportlab/638e7067709f6721a407b256bd4ed84cb1737106 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} freetype-py
pypi-dep-fix.py %{buildroot} rlPyCairo
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-reportlab/638e7067709f6721a407b256bd4ed84cb1737106
/usr/share/package-licenses/pypi-reportlab/b3245f6ac784e19a10843831b45b5944c62e3ccc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
