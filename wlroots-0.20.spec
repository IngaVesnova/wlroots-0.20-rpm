%global debug_package %{nil}

Name:           wlroots0.20
Version:        0.20.2
Release:        1%{?dist}
Summary:        Modular Wayland compositor library (version 0.20)

License:        MIT
URL:            https://gitlab.freedesktop.org/wlroots/wlroots
Source0:        https://gitlab.freedesktop.org/wlroots/wlroots/-/archive/%{version}/wlroots-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.59.0
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  hwdata-devel
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(wayland)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.38
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm) >= 2.4.129
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(libinput) >= 1.14.0
BuildRequires:  pkgconfig(libxkbcommon) >= 1.8.0
BuildRequires:  pkgconfig(pixman-1) >= 0.43.0
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires: pkgconfig(libliftoff)
BuildRequires: pkgconfig(x11-server-Xwayland)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-render)

%description
Modular Wayland compositor library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%prep
%autosetup -n wlroots-%{version}

%build
%meson \
  -Dxwayland=enabled \
  -Dexamples=false

%meson_build

%install
%meson_install

%files
%license LICENSE
%{_libdir}/libwlroots-0.20.so*

%files devel
%{_includedir}/wlroots-0.20/
%{_libdir}/libwlroots-0.20.so
%{_libdir}/pkgconfig/wlroots-0.20.pc

%changelog
* Tue Aug 04 2026 Custom Maintainer - %{version}-1
- Initial build of wlroots 0.20
