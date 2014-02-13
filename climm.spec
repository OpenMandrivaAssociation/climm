Summary:	Text-mode ICQ clone
Name:		climm
Version:	0.7.1
Release:	2
License:	GPLv2+
Group:		Networking/Instant messaging
Url:		http://www.climm.org/
Source0:	http://www.climm.org/source/%{name}-%{version}.tgz
Patch0:		climm-0.6.4-linktcl.patch
Patch1:		climm-0.7.1-gnutls-2.8.patch
BuildRequires:	enca
BuildRequires:	gettext-devel
BuildRequires:	tcl-devel
BuildRequires:	pkgconfig(gloox)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(iksemel)
BuildRequires:	pkgconfig(libotr)

%description
climm is a very portable text-mode ICQ clone - it is known to compile
under Linux, BSD, AIX, HPUX, Windows, AmigaOS and with restrictions
BeOS. Originally written by Matthew D. Smith, a great part of climm
has been rewritten by Rudiger Kuhlmann, in particular the support for
the new version 8 of the OSCAR protocol that became necessary, the
internationalization, the file transfer and some restructuring of
the code.

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

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
autoreconf -fi
%configure2_5x \
	--disable-dependency-tracking \
	--enable-ssl=gnutls \
	--enable-tcl \
	--enable-xmpp \
	--disable-rpath
make

%install
%makeinstall_std INSTALL="install -p"
# convert documentation to UTF-8, when possible
# es, fr are 7bit, sr is already UTF8
enconv -L russian -x UTF-8 doc/ru/*
enconv -L slovak -x UTF-8 doc/sk/*
enconv -L ukrainian -x UTF-8 doc/uk/* || :
for i in doc/de/* doc/pt_BR/* doc/it/*; do
  iconv -f iso8859-1 -t UTF-8 $i > $i.tmp
  mv -f $i.tmp $i
done


