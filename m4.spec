Summary:	GNU Macro Processor
Summary(de):	GNU-Makro-Prozessor
Summary(fr):	Processeur de macros de GNU
Summary(pl):	GNU procesor jêzyka makrodefinicji
Summary(tr):	GNU MakroÝþlemcisi
Name:		m4
Version:	1.4o
Release:	1
Copyright:	GPL
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
Source:		ftp://ftp.seindal.dk/gnu/%{name}-%{version}.tar.gz
Patch0:		m4-info.patch
Patch1:		m4-system-libltdl.patch
URL:		http://www.seindal.dk/rene/gnu/
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
Prereq:		/usr/sbin/fix-info-dir
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}

%description
A GNU implementation of the traditional UNIX macro processor. M4 is useful
for writing text files which can be logically parsed, and is used by many
programs as part of their build process. M4 has built-in functions for
including files, running shell commands, doing arithmetic, etc. The
autoconf program needs m4 for generating configure scripts, but not for
running configure scripts.

%description -l de
Dies ist die GNU-Makroverarbeitungssprache. Es ist zum Schreiben von
Textdateien geeignet, die logisch geparst werden können. Viele Programme
nutzen dies als Teil des Build-Vorgangs.

%description -l fr
Le langage de macro commande GNU. Il est utile pour constituer des fichiers
textes devant etre parcourues logiquement. De nombreux programmes
l'utilisent lors de leur processus de construction.

%description -l pl 
W pakiecie znajduje siê m4 - GNU procesor jêzyka makrodefinicji. U¿ywany
jest do tworzenia plików tekstowych, które mog± byæ logicznie parsowane.
Wiele programów korzysta z m4 podczas procesu kompilacji kodu ¼ród³owego.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
cp aclocal.m4 acinclude.m4
gettextize --copy --force
aclocal
automake
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	--without-included-gettext \
	--with-modules \
	--with-gmp
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9fn $RPM_BUILD_ROOT{%{_infodir}/*,%{_mandir}/man1/*} \
	NEWS README

%find_lang %{name}

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {NEWS,README}.gz

%attr(755,root,root) %{_bindir}/m4

%{_datadir}/m4
%{_infodir}/m4*
%{_mandir}/man1/*

%attr(755,root,root) %{_libexecdir}/m4/*.so
