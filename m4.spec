Summary:	GNU Macro Processor
Summary(de):	GNU-Makro-Prozessor
Summary(fr):	Processeur de macros de GNU
Summary(pl):	GNU procesor jêzyka makrodefinicji
Summary(tr):	GNU MakroÝþlemcisi
Name:		m4
Version:	1.4p
%define		_pre	pre2
Release:	0.%{_pre}.6
Epoch:		2
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.seindal.dk/gnu/%{name}-%{version}%{_pre}.tar.gz
Patch0:		%{name}-ac_am_cleanups.patch
Patch1:		%{name}-format_string_fix.patch
Patch2:		%{name}-info.patch
Patch3:		%{name}-pl.po-update.patch
Patch4:		%{name}-po-fix.patch
URL:		http://www.seindal.dk/rene/gnu/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.11.5
BuildRequires:	gmp-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
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
Requires:	%{name} = %{version}

%description devel
Files to develop application with embedded m4 interpreter.

%description devel -l pl
Pliki do tworzenia aplikacji z wbudowanym interpreterem m4.

%package static
Summary:	Static m4 library
Summary(pl):	Statyczna biblioteka m4
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static m4 library.

%description static -l pl
Statyczna biblioteka m4.

%prep
%setup  -q -n %{name}-%{version}%{_pre}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f acm4/ltdl.m4
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I acm4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--without-included-gettext \
	--with-modules \
	--with-gmp \
	--disable-ltdl-install \
	--enable-changeword \
	%{!?debug:--without-dmalloc} \
	--disable-rpath \
	--enable-static
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{_libdir}/m4/*.a

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/sbin/ldconfig

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README THANKS AUTHORS ChangeLog TODO

%attr(755,root,root) %{_bindir}/m4
%attr(755,root,root) %{_libdir}/libm4.so.*.*
%dir %{_libdir}/m4
%attr(755,root,root) %{_libdir}/m4/*.so
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
