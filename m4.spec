Summary:	GNU Macro Processor
Summary(de):	GNU-Makro-Prozessor
Summary(fr):	Processeur de macros de GNU
Summary(pl):	GNU procesor jêzyka makrodefinicji
Summary(tr):	GNU MakroÝþlemcisi
Name:		m4
Version:	1.4n
Release:	6
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
./configure %{_target} \
	--prefix=%{_prefix} \
	--without-included-gettext
make

%install
rm -rf $RPM_BUILD_ROOT

make install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

gzip -9fn $RPM_BUILD_ROOT{%{_infodir}/*,%{_mandir}/man1/*} \
	NEWS README

%find_lang m4

%post
/sbin/install-info %{_infodir}/m4.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/m4.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f m4.lang
%defattr(644,root,root,755)
%doc {NEWS,README}.gz

%attr(755,root,root) %{_bindir}/m4

%{_datadir}/m4
%{_infodir}/m4*
%{_mandir}/man1/*

%changelog
* Sat May 29 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4n-6]
- based on RH spec,
- spec rewrited by PLD team,
- pl translation Wojtek ¦lusarczyk <wojtek@shadow.eu.org>.
