#
# Conditional build
%bcond_without	tests	# perform "make check"
#
Summary:	GNU Macro Processor
Summary(de.UTF-8):	GNU-Makro-Prozessor
Summary(fr.UTF-8):	Processeur de macros de GNU
Summary(pl.UTF-8):	GNU procesor języka makrodefinicji
Summary(tr.UTF-8):	GNU Makroİşlemcisi
Name:		m4
Version:	1.4.19
Release:	1
Epoch:		3
License:	GPL v3+
Group:		Applications/Text
Source0:	https://ftp.gnu.org/gnu/m4/%{name}-%{version}.tar.xz
# Source0-md5:	0d90823e1426f1da2fd872df0311298d
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/m4/
BuildRequires:	gettext-tools >= 0.19.2
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRequires:	xz
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

%{__sed} -i '1 i @documentencoding ISO-8859-1' doc/m4.texi

# fails because of "Killed" printed (expected stderr is empty)
%{__rm} checks/198.sysval
touch checks/stamp-checks

# PLD builders stub resolv.conf file, use another one for tests
%{__sed} -i -e 's,/etc/resolv\.conf,/etc/nsswitch.conf,' tests/test-read-file.c
# SIGPIPE tests fail on builders due to unknown reason (detached terminal???)
# raise(SIGPIPE) does nothing, child process exits with return code 71
%{__sed} -i -e 's/ 3 4 //' tests/test-execute.sh

%build
%configure \
	PACKAGE=m4 \
	--disable-silent-rules \
	%{!?debug:--without-dmalloc}

%{__make}

%if %{with tests}
st=0
%{__make} check || st=1
if [ "$st" -ne 0 ]; then
	cat tests/test-suite.log
	exit 1
fi
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/m4
%{_infodir}/m4.info*
%{_mandir}/man1/m4.1*
