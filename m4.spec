Summary:	GNU Macro Processor
Summary(de):	GNU-Makro-Prozessor
Summary(fr):	Processeur de macros de GNU
Summary(pl):	GNU procesor jêzyka makrodefinicji
Summary(tr):	GNU MakroÝþlemcisi
Name:		m4
Version:	1.4q
Release:	2
Epoch:		2
License:	GPL
Group:		Applications/Text
#Source0:	ftp://ftp.seindal.dk/gnu/%{name}-%{version}%{_pre}.tar.gz
Source0:	http://www.lrde.epita.fr/~akim/download/%{name}-%{version}.tar.bz2
# Source0-md5:	de5ffda17f317b12272286ea93c9f2c0
Patch0:		%{name}-info.patch
Patch1:		%{name}-pl.po-update.patch
Patch2:		%{name}-po-fix.patch
Patch3:		%{name}-fixes-1.4.1.patch
URL:		http://www.seindal.dk/rene/gnu/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7.1
BuildRequires:	gettext-devel >= 0.11.5
BuildRequires:	gmp-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	perl-devel
BuildRequires:	texinfo
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}

%description
A GNU implementation of the traditional UNIX macro processor. M4 is
useful for writing text files which can be logically parsed, and is
used by many programs as part of their build process. M4 has built-in
functions for including files, running shell commands, doing
arithmetic, etc. The autoconf program needs m4 for generating
configure scripts, but not for running configure scripts.

%description -l de
Dies ist die GNU-Makroverarbeitungssprache. Es ist zum Schreiben von
Textdateien geeignet, die logisch geparst werden können. Viele
Programme nutzen dies als Teil des Build-Vorgangs.

%description -l fr
Le langage de macro commande GNU. Il est utile pour constituer des
fichiers textes devant etre parcourues logiquement. De nombreux
programmes l'utilisent lors de leur processus de construction.

%description -l pl
W pakiecie znajduje siê m4 - GNU procesor jêzyka makrodefinicji.
U¿ywany jest do tworzenia plików tekstowych, które mog± byæ logicznie
parsowane. Wiele programów korzysta z m4 podczas procesu kompilacji
kodu ¼ród³owego.

%package devel
Summary:	Files to develop application with embedded m4 interpreter
Summary(pl):	Pliki do tworzenia aplikacji z wbudowanym interpreterem m4
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Files to develop application with embedded m4 interpreter.

%description devel -l pl
Pliki do tworzenia aplikacji z wbudowanym interpreterem m4.

%package static
Summary:	Static m4 library
Summary(pl):	Statyczna biblioteka m4
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static m4 library.

%description static -l pl
Statyczna biblioteka m4.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

rm -f config/{libtool,ltdl}.m4

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I config
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	PACKAGE=m4 \
	--disable-ltdl-install \
	--disable-rpath \
	--enable-static \
	--with-gmp \
	--with-modules \
	%{!?debug:--without-dmalloc}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/m4/*.a

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README THANKS AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/m4
%attr(755,root,root) %{_libdir}/libm4.so.*.*
%dir %{_libdir}/m4
%attr(755,root,root) %{_libdir}/m4/*.so*
%{_libdir}/m4/*.la
%{_datadir}/m4
%{_infodir}/m4*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libm4.so
%{_libdir}/libm4.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libm4.a
