Name:    pcb
Version: 4.3.0
Release: 1
Summary: An interactive printed circuit board editor
License: GPLv2
Group:   Office
URL:     http://pcb.sourceforge.net
Source0:	https://sourceforge.net/projects/pcb/files/pcb/%{name}-%{version}/%{name}-%{version}.tar.gz


BuildRequires: intltool
BuildRequires: flex
BuildRequires: bison
BuildRequires: tk
BuildRequires: pkgconfig(gdlib)
BuildRequires: imagemagick
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gdlib)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkglext-1.0)
Requires: m4


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
%configure \
	--disable-dependency-tracking \
	--with-gui=gtk \
	--enable-dbus \
	--enable-toporouter \
	--disable-update-mime-database \
	--disable-update-desktop-database \
	--docdir=%{_docdir}/%{name}-%{version}

%make_build

%install
%make_install

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
