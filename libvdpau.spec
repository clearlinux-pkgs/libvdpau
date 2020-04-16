#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libvdpau
Version  : 1.4
Release  : 9
URL      : https://gitlab.freedesktop.org/vdpau/libvdpau/-/archive/1.4/libvdpau-1.4.tar.gz
Source0  : https://gitlab.freedesktop.org/vdpau/libvdpau/-/archive/1.4/libvdpau-1.4.tar.gz
Summary  : Nvidia VDPAU library
Group    : Development/Tools
License  : MIT
Requires: libvdpau-lib = %{version}-%{release}
Requires: libvdpau-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : doxygen
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : graphviz
BuildRequires : pkgconfig(32dri2proto)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(dri2proto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
Patch1: 0001-Set-default-configuration-in-absence-of-config-file.patch

%description
No detailed description available

%package dev
Summary: dev components for the libvdpau package.
Group: Development
Requires: libvdpau-lib = %{version}-%{release}
Provides: libvdpau-devel = %{version}-%{release}
Requires: libvdpau = %{version}-%{release}
Requires: libvdpau = %{version}-%{release}

%description dev
dev components for the libvdpau package.


%package dev32
Summary: dev32 components for the libvdpau package.
Group: Default
Requires: libvdpau-lib32 = %{version}-%{release}
Requires: libvdpau-dev = %{version}-%{release}

%description dev32
dev32 components for the libvdpau package.


%package doc
Summary: doc components for the libvdpau package.
Group: Documentation

%description doc
doc components for the libvdpau package.


%package lib
Summary: lib components for the libvdpau package.
Group: Libraries
Requires: libvdpau-license = %{version}-%{release}

%description lib
lib components for the libvdpau package.


%package lib32
Summary: lib32 components for the libvdpau package.
Group: Default
Requires: libvdpau-license = %{version}-%{release}

%description lib32
lib32 components for the libvdpau package.


%package license
Summary: license components for the libvdpau package.
Group: Default

%description license
license components for the libvdpau package.


%prep
%setup -q -n libvdpau-1.4
cd %{_builddir}/libvdpau-1.4
%patch1 -p1
pushd ..
cp -a libvdpau-1.4 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587057394
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir
cd ../build32;
meson test -C builddir || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libvdpau
cp %{_builddir}/libvdpau-1.4/COPYING %{buildroot}/usr/share/package-licenses/libvdpau/aedf533f647d97c8bb8f7374844d959e18cf8fe6
pushd ../build32/
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/vdpau/vdpau.h
/usr/include/vdpau/vdpau_x11.h
/usr/lib64/libvdpau.so
/usr/lib64/pkgconfig/vdpau.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libvdpau.so
/usr/lib32/pkgconfig/32vdpau.pc
/usr/lib32/pkgconfig/vdpau.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libvdpau/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvdpau.so.1
/usr/lib64/libvdpau.so.1.0.0
/usr/lib64/vdpau/libvdpau_trace.so
/usr/lib64/vdpau/libvdpau_trace.so.1
/usr/lib64/vdpau/libvdpau_trace.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libvdpau.so.1
/usr/lib32/libvdpau.so.1.0.0
/usr/lib32/vdpau/libvdpau_trace.so
/usr/lib32/vdpau/libvdpau_trace.so.1
/usr/lib32/vdpau/libvdpau_trace.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libvdpau/aedf533f647d97c8bb8f7374844d959e18cf8fe6
