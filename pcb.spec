Name:    pcb
Version: 20110918
Release: 3
Summary: An interactive printed circuit board editor
License: GPLv2
Group:   Office
URL:     https://pcb.sourceforge.net
BuildRequires: gtk2-devel
BuildRequires: intltool
BuildRequires: dbus-devel
BuildRequires: flex
BuildRequires: bison
BuildRequires: tk
BuildRequires: gd-devel
BuildRequires: imagemagick
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: gtkglext-devel
Requires: m4
Source0: http://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz

%description
PCB is an interactive printed circuit board editor.
PCB includes a rats nest feature, design rule checking, and can provide
industry standard RS-274-X (Gerber), NC drill, and centroid data (X-Y data)
output for use in the board fabrication and assembly process. PCB offers
high end features such as an autorouter and trace optimizer which can
tremendously reduce layout time.

%prep
%setup -q -n %{name}-%{version}

%build
export CFLAGS=`echo %optflags | sed "s/-D_FORTIFY_SOURCE=2 // g" -`
%configure2_5x --disable-static \
 --enable-dbus \
 --disable-update-mime-database \
 --disable-update-desktop-database

%make

%install
%makeinstall_std

rm -fr %{buildroot}%{_datadir}/mimelnk %{buildroot}%{_includedir} %{buildroot}%{_libdir}/*.a

%find_lang %{name}


%files -f %{name}.lang
%doc %{_datadir}/doc/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/gEDA/scheme/*
%{_mandir}/man1/%{name}*
%{_infodir}/*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-*
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/mime/packages/pcb.xml
