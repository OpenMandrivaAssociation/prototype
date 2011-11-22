%define	Summary	Award-winning RType clone

Summary:	%{Summary}
Name:		prototype
Version:	1.0
Release:	%mkrel 1
License:	Freeware
Group:		Games/Arcade
URL:		http://xout.blackened-interactive.com/ProtoType/Prototype.html
Source0:	http://xout.blackened-interactive.com/dump/new/ProtoType_src.zip
Source1:	http://xout.blackened-interactive.com/ProtoType/ProtoType.zip
# some patches (0-6) depend on each other, we must fix it it future
# these patches are from Gentoo with few modifications
Patch0:		prototype-1.0-makefile.patch
Patch1:		prototype-1.0-includes.patch
Patch2:		prototype-1.0-sdlrendertarget.patch
Patch3:		prototype-1.0-setstate.patch
Patch4:		prototype-1.0-linuxfixes.patch
Patch5:		prototype-1.0-hacks.patch
Patch6:		prototype-1.0-homedir.patch
BuildRequires:	MesaGLU-devel
BuildRequires:	SDL-devel
BuildRequires:	devil-devel
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRequires:	fmod3-devel
BuildRequires:	dos2unix
# fmod3 is 32 bit only so this one is too
ExclusiveArch:	%{ix86}
BuildRoot:	%{_tmppath}/%{oname}-%{version}-%{release}-buildroot

%description
Inspired by an old favourite of mine, Prototype pits you against a horde
of enemies in this short but fun RType clone. Prototype has been featured
in numerous magazines and even was awarded "Freeware Game of the month" in
PC Zone It was also awarded first place in the first shmup-dev competition.

%prep
%setup -q -c -a 1
dos2unix *.cpp *.h
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
for i in *.cpp; do sed -i "$i" -e "s:Data/:"%{_gamesdatadir}"/"%{name}"/:g"; done
%__mv ProtoType/Data/Gfx/forcecharge.png ProtoType/Data/Gfx/ForceCharge.png
%__mv ProtoType/Data/Gfx/chainParticle.png ProtoType/Data/Gfx/ChainParticle.png
%__mv ProtoType/Data/Gfx/Ladybird.png ProtoType/Data/Gfx/LadyBird.png
%__mv ProtoType/Data/Gfx/Turret1.png ProtoType/Data/Gfx/turret1.png
%__mv ProtoType/Data/Gfx/StarBurst.png ProtoType/Data/Gfx/Starburst.png
%__mv ProtoType/Data/Gfx/forceblast.png ProtoType/Data/Gfx/Forceblast.png
%__mv ProtoType/Data/Gfx/Fireball.png ProtoType/Data/Gfx/FireBall.png
%__mv ProtoType/Data/Gfx/anim_back1.png ProtoType/Data/Gfx/Anim_back1.png
%__mv ProtoType/Data/Gfx/anim_back2.png ProtoType/Data/Gfx/Anim_back2.png
%__mv ProtoType/Data/Gfx/anim_Fore1.png ProtoType/Data/Gfx/Anim_Fore1.png
%__mv ProtoType/Data/Gfx/anim_Fore2.png ProtoType/Data/Gfx/Anim_Fore2.png
%__mv ProtoType/Data/Gfx/anim_Fore3.png ProtoType/Data/Gfx/Anim_Fore3.png
%__mv ProtoType/Data/Gfx/WaterSplash.png ProtoType/Data/Gfx/watersplash.png
%__mv ProtoType/Data/Gfx/PrototypeMk1.png ProtoType/Data/Gfx/Prototypemk1.png
%__mv ProtoType/Data/Sound/deflection.wav ProtoType/Data/Sound/Deflection.wav
%__mv ProtoType/Data/Sound/smallExplosion.wav ProtoType/Data/Sound/SmallExplosion.wav
%__mv ProtoType/Data/Sound/PickUp.wav ProtoType/Data/Sound/Pickup.wav
%__mv ProtoType/Data/Sound/UI_Select.wav ProtoType/Data/Sound/UI_select.wav

%build
%make

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Prototype
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

%__install -d %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
%__install -d %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48,64x64,128x128}/apps
convert ProtoType/Data/Gfx/FireBug.png -resize 32x32 %{buildroot}%{_iconsdir}/%{name}.png
convert ProtoType/Data/Gfx/FireBug.png -resize 48x48 %{buildroot}%{_liconsdir}/%{name}.png
convert ProtoType/Data/Gfx/FireBug.png -resize 16x16 %{buildroot}%{_miconsdir}/%{name}.png
convert ProtoType/Data/Gfx/FireBug.png -resize 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
convert ProtoType/Data/Gfx/FireBug.png -resize 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert ProtoType/Data/Gfx/FireBug.png -resize 48x48 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert ProtoType/Data/Gfx/FireBug.png -resize 64x64 %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
convert ProtoType/Data/Gfx/FireBug.png -resize 128x128 %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

%__install -d %{buildroot}%{_gamesdatadir}/%{name}
%__install -d %{buildroot}%{_gamesbindir}
%__mv %{name} %{buildroot}%{_gamesbindir}/%{name}

mv ProtoType/Data/* %{buildroot}%{_gamesdatadir}/%{name}/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ProtoType/README.txt
%{_gamesbindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png

