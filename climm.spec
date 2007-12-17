Name:          climm
Version:       0.6.1
Release:       %mkrel 2
Epoch:         0
Summary:       Text-mode ICQ clone
Group:         Networking/Instant messaging
License:       GPL
URL:           http://www.climm.org/
Source0:       http://www.climm.org/source/%{name}-%{version}.tgz
Obsoletes:      micq < %{version}-%{release}
Provides:       micq = %{version}-%{release}
BuildRequires:  enca
BuildRequires:  gettext-devel
#BuildRequires: gloox-devel
BuildRequires:  gnutls-devel
BuildRequires:  libotr-devel
BuildRequires:  tcl-devel

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

%build
%{configure2_5x} --disable-dependency-tracking \
                 --enable-otr \
                 --enable-ssl=gnutls \
                 --enable-tcl \
                 --disable-xmpp \
                 --disable-binreloc \
                 --disable-rpath
%{make}

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
%doc NEWS AUTHORS FAQ README TODO COPYING COPYING-GPLv2
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
%lang(sk) %{_mandir}/sk/man?/*
%lang(sr) %{_mandir}/sr/man?/*
%lang(uk) %{_mandir}/uk/man?/*
