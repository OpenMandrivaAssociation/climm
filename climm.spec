Name:          climm
Version:       0.6.1
Release:       %mkrel 1
Epoch:         0
Summary:       Text-mode ICQ clone
Group:         Networking/Instant messaging
License:       GPL
URL:           http://www.climm.org/
Source0:       http://www.climm.org/source/%{name}-%{version}.tgz
Patch0:        micq-0.5.4.1-tcl-8.5.patch
Patch1:        micq-0.5.4-am_prog_cc_c_o.patch
BuildRequires: gettext-devel
#BuildRequires: gloox-devel
BuildRequires: gnutls-devel
BuildRequires: libotr-devel
BuildRequires: tcl-devel
Obsoletes:     micq
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root

%description
mICQ is a text-mode clone of the Mirabilis ICQ online
messaging/conferencing program.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1

%build
%{_bindir}/autoreconf -v -i
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
%{makeinstall_std}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc AUTHORS COPYING COPYING-GPLv2 ChangeLog FAQ INSTALL NEWS README TODO contrib/
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
