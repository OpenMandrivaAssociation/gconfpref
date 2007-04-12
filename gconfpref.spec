%define name gconfpref
%define version 0.0.1
%define release %mkrel 3

Name: %name
Summary: Another configuration tools for gconf
Version: %{version}
Release: %{release}
License: GPL
Url: http://www.angelfire.com/linux/dbrody/gconfpref.html
Group: Graphical desktop/GNOME
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}

BuildRequires: automake >= 1.4
Buildrequires: libgnome2-devel >= 2.0
Buildrequires: libgnomeui2-devel >= 2.0
Buildrequires: libatk-devel >= 1.0
Buildrequires: libpango-devel >= 1.0
Buildrequires: libgnomecanvas2-devel >= 2.0
Buildrequires: libGConf-devel >= 2.0
Buildrequires: libgnome-vfs-devel >= 2.0

%description
Gconfpref is a user friendly gconf editor.

%prep
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
%setup -q

%build
%configure

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std

mkdir -p %{buildroot}/%{_menudir}
cat << EOF > %{buildroot}/%{_menudir}/%{name}
?package(%name):command="%{_bindir}/gconfpref" icon="configuration_section.png" \
                needs="X11" section="Configuration/GNOME" \
 title="Gconfpref" longtitle="Edit your gnome preferences" needs="gnome" \
 xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gconfpref
Comment=Edit your gnome preferences
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;GTK;X-MandrivaLinux-System-Configuration-GNOME
EOF

%find_lang %name --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files -f %name.lang
%defattr(-,root,root,0755)
%{_bindir}/*
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

