Summary:     GNU Macro Processor
Summary(de): GNU-Makro-Prozessor
Summary(fr): Processeur de macros de GNU
Summary(pl): GNU makro procesor
Summary(tr): GNU Makro Ýþlemcisi
Name:        m4
Version:     1.4n
Release:     2
Copyright:   GPL
Group:       Utilities/Text
Source:      ftp://ftp.seindal.dk/gnu/%{name}-%{version}.tar.gz
Patch0:      m4-info.patch
URL:         http://www.seindal.dk/rene/gnu/
Prereq:      /sbin/install-info
Buildroot:   /tmp/%{name}-%{version}-root

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
Pakiet ten zawiera GNU makro porocesor. jest on u¿ytesczny w ró¿nego rodzaju
generatorach róznych tekstów. Wiele programów u¿ywa m4 w trakcie swojej
pracy lub do generowania róznych plików (np. w sendamilu do generowania
sendmail.cf).

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--without-included-gettext
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr

gzip -9fn $RPM_BUILD_ROOT/usr/{info/*,man/man1/*}

%post
/sbin/install-info /usr/info/m4.info.gz /etc/info-dir

%preun
if [ $1 = 0 ]; then
	/sbin/install-info --delete /usr/info/m4.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc NEWS README
%attr(755, root, root) /usr/bin/m4
/usr/info/m4*
/usr/share/m4
%attr(644, root,  man) /usr/man/man1/*
%lang(de) /usr/share/locale/de/LC_MESSAGES/m4.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/m4.mo
%lang(it) /usr/share/locale/it/LC_MESSAGES/m4.mo
%lang(ja) /usr/share/locale/ja/LC_MESSAGES/m4.mo
%lang(nl) /usr/share/locale/nl/LC_MESSAGES/m4.mo
%lang(pl) /usr/share/locale/pl/LC_MESSAGES/m4.mo
%lang(ru) /usr/share/locale/ru/LC_MESSAGES/m4.mo
%lang(sv) /usr/share/locale/sv/LC_MESSAGES/m4.mo

%changelog
* Sun Jan 03 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4n-2]
- standarized {un}registering info pages (added m4-info.patch),
- added --without-included-gettext to configure parameters,
- added gzipping man pages.

* Sat Nov 21 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4m-1]
- added URL,
- added pl transaltion,
- fixed: removed /usr/info/dir from %files.
- added m4 man page to %files,
- cosmetic changes in %post, %preun in {un}installing m4 info page,
- added /usr/share/m4 to %files.

* Thu Nov 12 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4k-1]
- changed base Source URL,
- siplification in %install,
- changed way passing $RPM_OPT_FLAGS and LDFLAGS,
- cosmetic canges in %prep
- added .mo files with %lang macros in %files.

* Mon Aug 31 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4-11]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- Manhattan build

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- added info file handling and BuildRoot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
