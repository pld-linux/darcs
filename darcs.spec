Summary:	David's Advanced Revision Control System is yet another replacement for CVS
Name:		darcs
Version:	0.9.20
Release:	1
License:	GPL v2
Group:		Development/Version Control
Source0:	http://abridgegame.org/darcs/%{name}-%{version}.tar.gz
# Source0-md5:	4d7bd4d35ee5eadb5913fb19cbfea5ab
URL:		http://abridgegame.org/darcs/
BuildRequires:	ghc >= 5.04
BuildRequires:	curl-devel
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
David's Advanced Revision Control System is yet another replacement
for CVS. It is written in Haskell, and has been used on Linux, MacOS
X, FreeBSD, OpenBSD and Microsoft Windows. Darcs includes a cgi
script, which can be used to view the contents of your repository.

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
%doc manual AUTHORS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
