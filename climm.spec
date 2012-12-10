Name:		climm
Version:	0.7.1
Release:	%mkrel 1
Epoch:		0
Summary:	Text-mode ICQ clone
Group:		Networking/Instant messaging
License:	GPLv2+
URL:		http://www.climm.org/
Source0:	http://www.climm.org/source/%{name}-%{version}.tgz
Patch0:		climm-0.6.4-linktcl.patch
Patch1:		climm-0.7.1-gnutls-2.8.patch
Obsoletes:	micq < %{version}-%{release}
Provides:	micq = %{version}-%{release}
BuildRequires:	enca
BuildRequires:	gettext-devel
BuildRequires:	gloox-devel
BuildRequires:	gnutls-devel
BuildRequires:	libotr-devel
BuildRequires:	tcl-devel
BuildRequires:	libiksemel-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
climm is a very portable text-mode ICQ clone - it is known to compile
under Linux, BSD, AIX, HPUX, Windows, AmigaOS and with restrictions
BeOS. Originally written by Matthew D. Smith, a great part of climm
has been rewritten by Rudiger Kuhlmann, in particular the support for
the new version 8 of the OSCAR protocol that became necessary, the
internationalization, the file transfer and some restructuring of
the code.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
autoreconf -fi
%{configure2_5x} --disable-dependency-tracking \
                 --enable-otr \
                 --enable-ssl=gnutls \
                 --enable-tcl \
                 --enable-xmpp \
                 --disable-rpath
make

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std} INSTALL="%{__install} -p"
# convert documentation to UTF-8, when possible
# es, fr are 7bit, sr is already UTF8
%{_bindir}/enconv -L russian -x UTF-8 doc/ru/*
%{_bindir}/enconv -L slovak -x UTF-8 doc/sk/*
%{_bindir}/enconv -L ukrainian -x UTF-8 doc/uk/* || :
for i in doc/de/* doc/pt_BR/* doc/it/*; do
  %{_bindir}/iconv -f iso8859-1 -t UTF-8 $i > $i.tmp
  %{__mv} -f $i.tmp $i
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc NEWS AUTHORS FAQ README TODO
%doc doc/README.i18n doc/README.logformat doc/README.ssl doc/example-climm-event-script
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%defattr(0644,root,root,0755)
%lang(de) %{_mandir}/de/man?/*
%lang(es) %{_mandir}/es/man?/*
%lang(fr) %{_mandir}/fr/man?/*
%lang(it) %{_mandir}/it/man?/*
%{_mandir}/man?/*
%lang(pt_BR) %{_mandir}/pt_BR/man?/*
%lang(ru) %{_mandir}/ru/man?/*
%lang(se) %{_mandir}/se/man?/*
%lang(sk) %{_mandir}/sk/man?/*
%lang(sr) %{_mandir}/sr/man?/*
%lang(uk) %{_mandir}/uk/man?/*


%changelog
* Wed Sep 22 2010 Funda Wang <fwang@mandriva.org> 0:0.7.1-1mdv2011.0
+ Revision: 580568
- New version 0.7.1

* Fri Oct 02 2009 Funda Wang <fwang@mandriva.org> 0:0.7-1mdv2010.1
+ Revision: 452490
- BR iksemel
- New version 0.7

* Wed Jun 03 2009 Funda Wang <fwang@mandriva.org> 0:0.6.4-2mdv2010.0
+ Revision: 382359
- rebuild for gnutls 2.8

* Sat Mar 14 2009 Funda Wang <fwang@mandriva.org> 0:0.6.4-1mdv2009.1
+ Revision: 354999
- new version 0.6.4
- build with newer tcl

* Sat Dec 06 2008 Adam Williamson <awilliamson@mandriva.org> 0:0.6.3-2mdv2009.1
+ Revision: 311072
- rebuild for new tcl
- spec clean

* Sun Oct 12 2008 Funda Wang <fwang@mandriva.org> 0:0.6.3-1mdv2009.1
+ Revision: 292808
- New version 0.6.3

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0:0.6.2-3mdv2009.0
+ Revision: 243528
- rebuild

* Sun Mar 02 2008 Funda Wang <fwang@mandriva.org> 0:0.6.2-1mdv2008.1
+ Revision: 177610
- disable parallel build
- New version 0.6.2
- Reenable xmpp protocol

* Sat Jan 19 2008 Funda Wang <fwang@mandriva.org> 0:0.6.1-4mdv2008.1
+ Revision: 155051
- rebuild against latest gnutls

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 23 2007 David Walluck <walluck@mandriva.org> 0:0.6.1-2mdv2008.1
+ Revision: 111687
- remove unused patches
- provide micq
- include documentation conversion from Fedora

* Sun Nov 18 2007 Funda Wang <fwang@mandriva.org> 0:0.6.1-1mdv2008.1
+ Revision: 109818
- fix description
- disable xmpp build
- New version 0.6.1
- micq renamed to climm
- rebuild

  + Anssi Hannula <anssi@mandriva.org>
    - rebuild for new soname of tcl

* Mon Jun 11 2007 David Walluck <walluck@mandriva.org> 0:0.5.4.1-1mdv2008.0
+ Revision: 38003
- 0.5.4.1

* Thu Jun 07 2007 David Walluck <walluck@mandriva.org> 0:0.5.4-2mdv2008.0
+ Revision: 36127
- BuildRequires: gettext-devel
- update summary
- patch for tcl8.5 support
- build with otr support
- be more explicit with configure options
- more explicit file permissions in file list
- 0.5.4
- enable XMPP support
- Import micq



* Tue Feb 28 2006 Jerome Soyer <saispo@mandriva.org> 0.5.1-1mdk
- New release 0.5.1

* Mon Jan 02 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.0.4-2mdk
- rebuilt against soname aware deps (tcl/tk)
- fix deps

* Sat Oct  1 2005 Couriousous <couriousous@mandriva.org> 0.5.0.4-1mdk
- 0.5.0.4
- Mandrakelinux -> Mandriva

* Thu Feb 17 2005 Couriousous <couriousous@mandrake.org> 0.5-1mdk
- 0.5

* Sun Dec 26 2004 Couriousous <couriousous@mandrake.org> 0.4.99.9-1mdk
- Update MICQ_EXTRAVERSION
- Fix BuildRequires
- Fix Summary
- From: Marc Koschewski
	- 0.4.99.9

* Mon Jan 19 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.4.11-1mdk
- 0.4.11

* Tue Oct 07 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.4.10.5-1mdk
- 0.4.10.5

* Tue Sep 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.4.10.4-1mdk
- 0.4.10.4

* Wed Jun 04 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.4.10.3-2mdk
- fix license
- add patch0 from author

* Thu May 15 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.4.10.3-1mdk
- 0.4.10.3

* Mon Mar 17 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.4.10.2-1mdk
- 0.4.10.2

* Mon Jan 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.4.10.1-1mdk
- 0.4.10.1

* Wed Jan 08 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.4.10-1mdk
- 0.4.10

* Mon Oct 14 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.4.9.4-3mdk
- change desc.

* Fri Oct 11 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.4.9.4-2mdk
- export MICQ_EXTRAVERSION=Mandrake

* Mon Oct 07 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.4.9.4-1mdk
- 0.4.9.4

* Tue Aug 27 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.4.9.3-1mdk
- 0.4.9.3

* Thu Aug 22 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.4.9.2b-1mdk
- 0.4.9.2b

* Mon Aug 27 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.4.7-1mdk
- 0.4.7

* Tue Aug 21 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.4.6-4mdk
- rebuild

* Mon Jan 22 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.4.6-3mdk
- rebuild

* Mon Sep 11 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.4.6-2mdk
- clean spec
- BM

* Mon Jun 12 2000 John Johnson <jjohnson@linux-mandrake.com> 0.4.6-1mdk
- updated rpm to version 0.4.6 version of micq

* Fri May 12 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.4.4-1mdk
- fix group
- add url
- bzip2 sources
- fix files section 

* Sun Apr 30 2000 John Johnson <jjohnson@linux-mandrake.com>
- built package for mandrake i586
