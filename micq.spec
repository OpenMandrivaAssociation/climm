Name:          micq
Version:       0.5.4.1
Release:       %mkrel 3
Epoch:         0
Summary:       Text-mode ICQ clone
Group:         Networking/Instant messaging
License:       GPL
URL:           http://www.micq.org/
Source0:       http://www.micq.org/source/micq-0.5.4.1.tgz
Patch0:        micq-0.5.4.1-tcl-8.5.patch
Patch1:        micq-0.5.4-am_prog_cc_c_o.patch
BuildRequires: gettext-devel
BuildRequires: gloox-devel
BuildRequires: gnutls-devel
BuildRequires: libotr-devel
BuildRequires: tcl-devel
BuildRoot:    %{_tmppath}/%{name}-%{version}-%{release}-root


%description
mICQ is a text-mode clone of the Mirabilis ICQ online
messaging/conferencing program.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{_bindir}/autoreconf -v -i

%build
export MICQ_EXTRAVERSION=Mandriva
%{configure2_5x} --disable-dependency-tracking \
                 --enable-otr \
                 --enable-ssl=gnutls \
                 --enable-tcl \
                 --enable-xmpp \
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
%attr(0755,root,root) %{_bindir}/micq
%{_datadir}/%{name}
%defattr(0644,root,root,0755)
%{_mandir}/de/man1/micq.1*
%{_mandir}/de/man5/micqrc.5*
%{_mandir}/de/man7/micq.7*
%{_mandir}/es/man1/micq.1*
%{_mandir}/es/man5/micqrc.5*
%{_mandir}/es/man7/micq.7*
%{_mandir}/fr/man1/micq.1*
%{_mandir}/fr/man5/micqrc.5*
%{_mandir}/fr/man7/micq.7*
%{_mandir}/it/man1/micq.1*
%{_mandir}/man1/micq.1*
%{_mandir}/man5/micqrc.5*
%{_mandir}/man7/micq.7*
%{_mandir}/pt_BR/man1/micq.1*
%{_mandir}/pt_BR/man5/micqrc.5*
%{_mandir}/pt_BR/man7/micq.7*
%{_mandir}/ru/man1/micq.1*
%{_mandir}/ru/man5/micqrc.5*
%{_mandir}/ru/man7/micq.7*
%{_mandir}/sk/man1/micq.1*
%{_mandir}/sk/man5/micqrc.5*
%{_mandir}/sk/man7/micq.7*
%{_mandir}/sr/man1/micq.1*
%{_mandir}/sr/man5/micqrc.5*
%{_mandir}/sr/man7/micq.7*
%{_mandir}/uk/man1/micq.1*
%{_mandir}/uk/man7/micq.7*
