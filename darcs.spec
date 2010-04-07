#
# TODO:
# Setup.lhs: At least the following dependencies are missing:
# hashed-storage >=0.3.8 && <0.4 && >=0.3.8 && <0.4,
# haskeline >=0.6.1 && <0.7 && >=0.6.1 && <0.7
#
Summary:	David's Advanced Revision Control System - yet another replacement for CVS
Summary(pl.UTF-8):	David's Advanced Revision Control System - jeszcze jeden zamiennik CVS-a
Name:		darcs
Version:	2.4
Release:	0.1
License:	GPL v2
Group:		Development/Version Control
Source0:	http://darcs.net/releases/%{name}-%{version}.tar.gz
# Source0-md5:	169a6d245a33da97b2daa0eda60b28e5
URL:		http://darcs.net/
BuildRequires:	ghc >= 6.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
David's Advanced Revision Control System is yet another replacement
for CVS. It is written in Haskell, and has been used on Linux, MacOS
X, FreeBSD, OpenBSD and Microsoft Windows. Darcs includes a CGI
script, which can be used to view the contents of your repository.

%description -l pl.UTF-8
David's Advanced Revision Control System (zaawansowany system kontroli
wersji Davida) to jeszcze jeden zamiennik CVS-a. Jest napisany w
Haskellu, dotychczas był używany na Linuksie, MacOS-ie X, FreeBSD,
OpenBSD i Microsoft Windows. Darcs zawiera skrypt CGI, który może być
używany do oglądania zawartości repozytorium.

%prep
%setup -q

%build
runhaskell Setup.lhs configure --prefix=%{_prefix}
runhaskell Setup.lhs build

%install
rm -rf $RPM_BUILD_ROOT
runhaskell Setup.lhs copy --destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc manual AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/bash_completion.d/%{name}
%{_mandir}/man?/*
