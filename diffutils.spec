Summary:	GNU diff Utilities
Summary(de):	GNU-Diff-Utilities 
Summary(fr):	Utilitaires diff de GNU
Summary(pl):	narz�dzia diff GNU
Summary(tr):	GNU dosya kar��la�t�rma ara�lar�
Name:		diffutils
Version:	2.7
Release:	16
Group:		Utilities/Text
Group(pl):	Narz�dzia/Tekst
Copyright:	GPL
Source:		ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		diffutils-man.patch
Patch1:		diffutils-info.patch
Prereq:		/sbin/install-info
Buildroot:	/tmp/%{name}-%{version}-root

%description
Diffutils includes four utilities:  diff, cmp, diff3 and sdiff. Diff
compares two files and shows the differences, line by line. The cmp command
shows the offset and line numbers where two files differ, or cmp can show
the characters that differ between the two files. The diff3 command shows
the differences between three files. Diff3 can be used when two people have
made independent changes to a common original; diff3 can produce a merged
file that contains both persons changes and warnings about conflicts. The
sdiff command can be used to merge two files interactively.

Install diffutils if you need to compare text files.

%description -l pl
Narz�dzia diff s� u�ywane do por�wnywania zawarto�ci plik�w i tworzenia 
zbioru z r�nicami. Mo�na go potem u�y� (za pomoc� programu patch) do
uaktualnienia starszego pliku. Wszystkie narz�dzia (za wyj�tkiem cmp)
pracuj� tylko na plikach tekstowych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=%{_prefix}

make PR_PROGRAM=%{_bindir}/pr

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/{man1,pl/man1}

make install prefix=$RPM_BUILD_ROOT/usr \
	bindir=$RPM_BUILD_ROOT/%{_bindir} \
	mandir=$RPM_BUILD_ROOT/%{_mandir} \
	infodir=$RPM_BUILD_ROOT/%{_infodir}

strip $RPM_BUILD_ROOT%{_bindir}/*

install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install man/pl/*.1 $RPM_BUILD_ROOT%{_mandir}/pl/man1

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/diff* \
	$RPM_BUILD_ROOT%{_mandir}/{man1/*,pl/man1/*}

%post
/sbin/install-info %{_infodir}/diff.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/diff.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%{_infodir}/diff.info*gz
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%changelog
* Mon Jun 07 1999 Jan R�korajski <baggins@pld.org.pl>
  [2.7-16]
- spec cleanup

* Thu Apr  1 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.7-15]
- added cmp(1), diff(1), diff3(1), sdiff(1) man pages and pl man page
  diff(1),
- standarized {un}registration info pages (added diffutils-info.patch).

* Thu Sep 24 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [2.7-12]
- added pl translation,
- adde -q %setup parameter,
- moved CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" from make 
  to configure (as a much safer solution).

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun May 03 1998 Cristian Gafton <gafton@redhat.com>
- fixed spec file to reference/use the $RPM_BUILD_ROOT always

* Wed Dec 31 1997 Otto Hammersmith <otto@redhat.com>
- fixed where it looks for 'pr' (%{_bindir}, rather than /bin)

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- added BuildRoot

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- uses install-info

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
