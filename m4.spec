Summary:	GNU Macro Processor
Summary(de):	GNU-Makro-Prozessor
Summary(fr):	Processeur de macros de GNU
Summary(pl):	GNU procesor jêzyka makrodefinicji
Summary(tr):	GNU MakroÝþlemcisi
Name:		m4
Version:	1.4n
Release:	5
Copyright:	GPL
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
Source:		ftp://ftp.seindal.dk/gnu/%{name}-%{version}.tar.gz
Patch0:		m4-info.patch
URL:		http://www.seindal.dk/rene/gnu/
Prereq:		/sbin/install-info
Buildroot:	/tmp/%{name}-%{version}-root

%description
This is the GNU Macro processing language. It is useful for writing text
files that can be parsed logically. Many programs use it as part of their
build process.

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
%setup -q
%patch -p1

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
    ./configure \
	--prefix=%{_prefix} \
	--without-included-gettext \
	%{_target_platform}
make

%install
rm -rf $RPM_BUILD_ROOT

make \
    install \
    prefix=$RPM_BUILD_ROOT%{_prefix}

gzip -9fn $RPM_BUILD_ROOT/usr/share/{info/*,man/man1/*} NEWS README

%post
/sbin/install-info %{_infodir}/m4.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/m4.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,README}.gz

%attr(755,root,root) %{_bindir}/m4

%{_datadir}/m4
%{_infodir}/m4*
%{_mandir}/man1/*

%lang(de) %{_datadir}/locale/de/LC_MESSAGES/m4.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/m4.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/m4.mo
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/m4.mo
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/m4.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/m4.mo
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/m4.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/m4.mo

%changelog
* Sun May 23 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.4n-5]
- more macros in use,
- calling autoconf,
- compressed %doc.

* Wed Mar 10 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4n-3]
- added Group(pl),
- removed man group from man pages.

* Sun Jan 03 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4n-2]
- standarized {un}registering info pages (added m4-info.patch),
- added --without-included-gettext to configure parameters,
- added gzipping man pages.

* Sat Nov 21 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4m-1]
- added URL,
- fixed: removed %{_infodir}/dir from %files.
- added m4 man page to %files,
- cosmetic changes in %post, %preun in {un}installing m4 info page,
- added %{_datadir}/m4 to %files.

* Thu Nov 12 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4k-1]
- changed base Source URL,
- siplification in %install,
- changed way passing $RPM_OPT_FLAGS and LDFLAGS,
- cosmetic canges in %prep
- added .mo files with %lang macros in %files.

* Mon Sep 28 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.4-11d]
- build against PLD Tornado,
- macro %%{name}-%%{version} in Patch,
- CFLAGS=$RPM_OPT_FLAGS & LDFLAGS=-s before ./configure,
- transaltion modified for pl,

  translation fixed by Adam Kozubowicz <tapir@interdata.com.pl>

- fixed files permissions.

* Mon Aug 31 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4-11]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added %attr and %defattr macros in %files (allows build package from
  non-root account),
- start at RH spec file.
