Summary:	A GNU collection of diff utilities
Summary(de):	GNU-Sammlung von diff-Utilities
Summary(fr):	Utilitaires diff de GNU
Summary(pl):	Narzêdzia diff GNU
Summary(tr):	GNU dosya karþýlaþtýrma araçlarý
Name:		diffutils
Version:	2.8.7
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://alpha.gnu.org/gnu/diffutils/%{name}-%{version}.tar.gz
# Source0-md5:	18d6587cb915e7aa110a5d463d6ed156
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	34a7ab56f975ff7e439ea13923ec8ae4
Patch0:		%{name}-info.patch
Patch1:		%{name}-pl.po-update.patch
URL:		http://www.gnu.org/software/diffutils/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.14.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Diffutils includes four utilities: diff, cmp, diff3 and sdiff. Diff
compares two files and shows the differences, line by line. The cmp
command shows the offset and line numbers where two files differ, or
cmp can show the characters that differ between the two files. The
diff3 command shows the differences between three files. Diff3 can be
used when two people have made independent changes to a common
original; diff3 can produce a merged file that contains both persons
changes and warnings about conflicts. The sdiff command can be used to
merge two files interactively.

%description -l de
Diffutils enthält 4 Utilities: diff, cmp, diff3 und sdiff. Diff
vergleicht zwei Dateien und zeigt die Unterschiede, Zeile für Zeile.
cmp zeigt Offset und Zeilennummern, in denen sich zwei Dateien
unterscheiden, cmp kann auch die Zeichen zeigen, die sich
unterscheiden. diff3 zeigt die Unterschiede zwischen 3 Dateien. Diff3
kann benutzt werden, wenn zwei Leute unabhängige Änderungen zu einem
gemeinsamen Ursprung gemacht haben; diff3 kann eine Datei erzeugen,
die die Änderungen beider Personen und Warnungen zu Konflikten
enthält. Der sdiff-Befehl kann benutzt werden, um zwei Dateien
interaktiv zusammenzufügen.

%description -l pl
Diffutils zawiera nastêpuj±ce programy: diff, cmp, diff3 i sdiff. diff
s³u¿y do porównywania dwóch plików wy¶wietlaj±c ró¿nice miêdzy nimi
linia po linii. Polecenie cmp podaje numery bajtów na których
wystêpuj± ró¿nice miêdzy porównywanymi plikami. diff3 pokazuje ró¿nice
miedzy trzema plikami. diff3 mo¿e byæ u¿yty np. w sytuacji kiedy dwie
osoby wykona³y zmianê niezale¿nie od siebie na jednym pliku,
pozwalaj±c uzyskaæ po³±czon± listê zmian zawieraj±c± informacje o tym,
kto co zmieni³, a tak¿e informacje o konfliktach miedzy tymi dwoma
modyfikacjami. Polecenie sdiff s³u¿y do interakcyjnego ³±czenia dwóch
plików.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	PR_PROGRAM=/usr/bin/pr

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xvf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%{_infodir}/diff.info*
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(pt) %{_mandir}/pt/man1/*
%lang(ru) %{_mandir}/ru/man1/*
