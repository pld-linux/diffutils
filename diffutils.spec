Summary:     GNU diff Utilities
Summary(de): GNU-Diff-Utilities 
Summary(fr): Utilitaires diff de GNU
Summary(pl): narzêdzia diff GNU
Summary(tr): GNU dosya karþýlaþtýrma araçlarý
Name:        diffutils
Version:     2.7
Release:     12
Group:       Utilities/Text
Source:      ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Copyright:   GPL
Prereq:      /sbin/install-info
Buildroot:   /tmp/%{name}-%{version}-root

%description
The diff utilities can be used to compare files, and generate a record
of the "differences" between files.  This record can be used by the
patch program to bring one file up to date with the other.  All these
utilities (except cmp) only work on text files.

%description -l pl
Narzêdzia diff s± u¿ywane do porównywania zawarto¶ci plików i tworzenia 
zbioru z ró¿nicami. Mo¿na go potem u¿yæ (za pomoc± programu patch) do
uaktualnienia starszego pliku. Wszystkie narzêdzia (za wyj±tkiem cmp)
pracuj± tylko na plikach tekstowych.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s ./configure --prefix=/usr 
make PR_PROGRAM=/usr/bin/pr

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install
gzip -9nf $RPM_BUILD_ROOT/usr/info/diff*

strip $RPM_BUILD_ROOT/usr/bin/*

%post
/sbin/install-info /usr/info/diff.info.gz /usr/info/dir --entry="* diff: (diff).                 The GNU diff."

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete /usr/info/diff.info.gz /usr/info/dir --entry="* diff: (diff).                 The GNU diff."
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc NEWS README
%attr(755, root, root) /usr/bin/*
%attr(644, root, root) /usr/info/diff.info*gz

%changelog
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
- fixed where it looks for 'pr' (/usr/bin, rather than /bin)

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- added BuildRoot

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- uses install-info

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
