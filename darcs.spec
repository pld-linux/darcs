#
# Conditional build:
%bcond_without	tests		# build without tests

Summary:	David's Advanced Revision Control System - yet another replacement for CVS
Summary(pl.UTF-8):	David's Advanced Revision Control System - jeszcze jeden zamiennik CVS-a
Name:		darcs
Version:	2.10.3
Release:	0.1
License:	GPL v2
Group:		Development/Version Control
Source0:	http://darcs.net/releases/%{name}-%{version}.tar.gz
# Source0-md5:	0caaeb63253e28fdafecd50413c731d6
Patch0:		%{name}-ghc72.patch
Patch1:		%{name}-relax-regex-libs-deps.patch
Patch2:		%{name}-tests-ghc72.patch
URL:		http://darcs.net/
BuildRequires:	curl-devel >= 7.19.1
BuildRequires:	ghc >= 6.12.3
BuildRequires:	ghc-base16-bytestring < 0.2
BuildRequires:	ghc-base16-bytestring >= 0.1
BuildRequires:	ghc-cryptohash <0.12
BuildRequires:	ghc-cryptohash > =0.4
BuildRequires:	ghc-data-ordlist < 0.5
BuildRequires:	ghc-data-ordlist >= 0.4
BuildRequires:	ghc-hashed-storage >= 0.5
BuildRequires:	ghc-haskeline >= 0.6.1
BuildRequires:	ghc-mmap >= 1:0.5
BuildRequires:	ghc-regex-applicative < 0.4
BuildRequires:	ghc-regex-applicative >= 0.2
BuildRequires:	ghc-regex-compat-tdfa < 0.96
BuildRequires:	ghc-regex-compat-tdfa >= 0.95.1
BuildRequires:	ghc-sandi < 0.4
BuildRequires:	ghc-sandi >= 0.2
BuildRequires:	ghc-tar >= 0.3
BuildRequires:	ghc-terminfo >= 0.3
BuildRequires:	ghc-transformers-compat < 0.6
BuildRequires:	ghc-transformers-compat >= 0.4
BuildRequires:	ghc-unix-compat < 0.5
BuildRequires:	ghc-unix-compat >= 0.1.2
BuildRequires:	ghc-utf8-string >= 0.3
BuildRequires:	ghc-zip-archive < 0.3
BuildRequires:	ghc-zip-archive >= 0.2.3
BuildRequires:	ghc-zlib >= 0.5.1.0
BuildRequires:	gmp-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ghcdir		ghc-%(/usr/bin/ghc --numeric-version)

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

%package -n bash-completion-darcs
Summary:	bash-completion for darcs
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla darcsa
Group:		Applications/Shells
Requires:	bash-completion
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n bash-completion-darcs
This package provides bash-completion for darcs.

%description -n bash-completion-darcs -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla darcsa.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1

%build
runhaskell Setup.lhs configure -v2 \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--docdir=%{_docdir}/%{name}-%{version} \
	--flags="curl curl-pipelining terminfo color mmap"

runhaskell Setup.lhs build
%{?with_tests:runhaskell Setup.lhs test}

runhaskell Setup.lhs haddock --executables \
	--css=doc/darcs.css

%install
rm -rf $RPM_BUILD_ROOT

runhaskell Setup.lhs copy --destdir=$RPM_BUILD_ROOT

# work around automatic haddock docs installation
rm -rf %{name}-%{version}-doc
cp -a $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} %{name}-%{version}-doc

# bash completion
install -d $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
install -p contrib/darcs_completion $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/%{name}

# we only want the binary
rm -r $RPM_BUILD_ROOT/%{_libdir}/%{ghcdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%doc %{name}-%{version}-doc/html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files -n bash-completion-darcs
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/%{name}
