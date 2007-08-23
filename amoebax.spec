Summary:	Cute and addictive puzzle game
Summary(pl.UTF-8):	Ładna i uzależniająca gra logiczna
Name:		amoebax
Version:	0.2.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.emma-soft.com/games/amoebax/download/%{name}-%{version}.tar.bz2
# Source0-md5:	1fecc5e4c8c4151b39f84baa5a18897b
Patch0:		%{name}-desktop.patch
URL:		http://www.emma-soft.com/games/amoebax/
BuildRequires:	SDL-devel >= 1.2.11
BuildRequires:	SDL_image-devel >= 1.2.5
BuildRequires:	SDL_mixer-devel >= 1.2.7
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Amoebax is a cute and addictive puzzle game. Due an awful mutation,
some amoeba's species have started to multiply until they take the
world if you can't stop them. Fortunately the mutation made then too
unstable and lining up four or more will make them disappear.

%description -l pl.UTF-8
Amoebax jest ładną i uzależniającą grą loginczą. W wyniku straszliwej
mutacji pewien gatunek ameby zaczął się rozmnażać i może opanować
świat jeśli go nie powstrzymasz. Naszczęsćie mutacja jest bardzo
niestabilna i połączenie czterech lub więcej osobników tego samego
typu powoduje ich znikanie.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install data/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS doc/manual.pdf
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/*.6*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
