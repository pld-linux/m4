Summary:     GNU Macro Processor
Summary(de): GNU-Makro-Prozessor
Summary(fr): Processeur de macros de GNU
Summary(tr): GNU Makro Ýþlemcisi
Name:        m4
Version:     1.4
Release:     11
Copyright:   GPL
Group:       Utilities/Text
Source:      ftp://prep.ai.mit.edu:/pub/gnu/%{name}-%{version}.tar.gz
Patch:       m4-1.4-glibc.patch
Buildroot:   /tmp/%{name}-%{version}-root
Prereq:      /sbin/install-info

%description
This is the GNU Macro processing language.  It is useful for writing text
files that can be parsed logically.  Many programs use it as part of their
build process.

%description -l de
Dies ist die GNU-Makroverarbeitungssprache. Es ist zum Schreiben von
Textdateien geeignet, die logisch geparst werden können. Viele Programme
nutzen dies als Teil des Build-Vorgangs.

%description -l fr
Le langage de macro commande GNU. Il est utile pour constituer des fichiers
textes devant etre parcourues logiquement. De nombreux programmes
l'utilisent lors de leur processus de construction.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch -p1

%build
./configure --prefix=/usr
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s

%install
./configure --prefix=$RPM_BUILD_ROOT/usr
make install
strip $RPM_BUILD_ROOT/usr/bin/m4
gzip -9fn $RPM_BUILD_ROOT/usr/info/*

%post
/sbin/install-info /usr/info/m4.info.gz /usr/info/dir

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete /usr/info/m4.info.gz /usr/info/dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc NEWS README
%attr(755, root, root) /usr/bin/m4
/usr/info/*

%changelog
* Mon Aug 31 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4-11]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- Manhattan build

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- added info file handling and BuildRoot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
