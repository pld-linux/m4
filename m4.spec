#
# Conditional build
%bcond_with	tests	# perform "make check"
#
Summary:	GNU Macro Processor
Summary(de.UTF-8):	GNU-Makro-Prozessor
Summary(fr.UTF-8):	Processeur de macros de GNU
Summary(pl.UTF-8):	GNU procesor języka makrodefinicji
Summary(tr.UTF-8):	GNU Makroİşlemcisi
Name:		m4
Version:	1.4.14
Release:	1
Epoch:		3
License:	GPL v3+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/m4/%{name}-%{version}.tar.bz2
# Source0-md5:	e6fb7d08d50d87e796069cff12a52a93
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/m4/
BuildRequires:	texinfo
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GNU implementation of the traditional UNIX macro processor. M4 is
useful for writing text files which can be logically parsed, and is
used by many programs as part of their build process. M4 has built-in
functions for including files, running shell commands, doing
arithmetic, etc. The autoconf program needs m4 for generating
configure scripts, but not for running configure scripts.

%description -l de.UTF-8
Dies ist die GNU-Makroverarbeitungssprache. Es ist zum Schreiben von
Textdateien geeignet, die logisch geparst werden können. Viele
Programme nutzen dies als Teil des Build-Vorgangs.

%description -l fr.UTF-8
Le langage de macro commande GNU. Il est utile pour constituer des
fichiers textes devant etre parcourues logiquement. De nombreux
programmes l'utilisent lors de leur processus de construction.

%description -l pl.UTF-8
W pakiecie znajduje się m4 - GNU procesor języka makrodefinicji.
Używany jest do tworzenia plików tekstowych, które mogą być logicznie
parsowane. Wiele programów korzysta z m4 podczas procesu kompilacji
kodu źródłowego.

%package devel
Summary:	Files to develop application with embedded m4 interpreter
Summary(pl.UTF-8):	Pliki do tworzenia aplikacji z wbudowanym interpreterem m4
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Files to develop application with embedded m4 interpreter.

%description devel -l pl.UTF-8
Pliki do tworzenia aplikacji z wbudowanym interpreterem m4.

%package static
Summary:	Static m4 library
Summary(pl.UTF-8):	Statyczna biblioteka m4
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static m4 library.

%description static -l pl.UTF-8
Statyczna biblioteka m4.

%prep
%setup -q
%patch0 -p1

rm -f config/{libtool,ltdl}.m4

%build
%configure \
	PACKAGE=m4 \
	%{!?debug:--without-dmalloc}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{?with_tests:%{__make} check}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc NEWS README THANKS AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/m4
%{_infodir}/m4.info*
%{_mandir}/man1/m4.1*
