%global kf_version 6.6.0

Name: kf6-kdbusaddons
Version: 6.6.0
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 1 addon with various classes on top of QtDBus

License: LGPLv2+
URL:     https://invent.kde.org/frameworks/kdbusaddons

Source0: %{name}-%{version}.tar.bz2

BuildRequires: kf6-extra-cmake-modules >= %{kf_version}
BuildRequires: kf6-rpm-macros >= %{kf_version}
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qttools-devel

%description
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Development Documentation files for %{name}
BuildArch:      noarch
%description    doc


%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build

%cmake_kf6 \
    -DWITH_X11=OFF
%cmake_build

%install
%cmake_install

%find_lang_kf6 kdbusaddons6_qt

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kdbusaddons6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/kdbusaddons*
%{_kf6_bindir}/kquitapp6
%{_kf6_libdir}/libKF6DBusAddons.so.*

%files devel
%{_kf6_includedir}/KDBusAddons/
%{_kf6_libdir}/libKF6DBusAddons.so
%{_kf6_libdir}/cmake/KF6DBusAddons/
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch
