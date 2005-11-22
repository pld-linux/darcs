Summary:	David's Advanced Revision Control System - yet another replacement for CVS
Summary(pl):	David's Advanced Revision Control System - jeszcze jeden zamiennik CVS-a
Name:		darcs
Version:	1.0.4
Release:	1
License:	GPL v2
Group:		Development/Version Control
Source0:	http://abridgegame.org/darcs/%{name}-%{version}.tar.gz
# Source0-md5:	0be693b00e4b1bd24906d4f479e78923
URL:		http://abridgegame.org/darcs/
BuildRequires:	curl-devel
BuildRequires:	ghc >= 6.2
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
David's Advanced Revision Control System is yet another replacement
for CVS. It is written in Haskell, and has been used on Linux, MacOS
X, FreeBSD, OpenBSD and Microsoft Windows. Darcs includes a CGI
script, which can be used to view the contents of your repository.

%description -l pl
David's Advanced Revision Control System (zaawansowany system kontroli
wersji Davida) to jeszcze jeden zamiennik CVS-a. Jest napisany w
Haskellu, dotychczas by³ u¿ywany na Linuksie, MacOS-ie X, FreeBSD,
OpenBSD i Microsoft Windows. Darcs zawiera skrypt CGI, który mo¿e byæ
u¿ywany do ogl±dania zawarto¶ci repozytorium.

%prep
%setup -q

%build
CPPFLAGS="-I%{_includedir}/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc manual AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/bash_completion.d/%{name}
%{_mandir}/man?/*
