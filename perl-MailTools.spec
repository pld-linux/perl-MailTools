%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	Tools
Summary:	MailTools Perl module
Summary(cs):	Modul MailTools pro Perl
Summary(da):	Perlmodul MailTools
Summary(de):	MailTools Perl Modul
Summary(es):	Módulo de Perl MailTools
Summary(fr):	Module Perl MailTools
Summary(it):	Modulo di Perl MailTools
Summary(ja):	MailTools Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	MailTools ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul MailTools
Summary(pl):	Modu³ Perla MailTools
Summary(pt):	Módulo de Perl MailTools
Summary(pt_BR):	Módulo Perl MailTools
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl MailTools
Summary(sv):	MailTools Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl MailTools
Summary(zh_CN):	MailTools Perl Ä£¿é
Name:		perl-MailTools
Version:	1.41
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-libnet
BuildRequires:	perl(Net::Domain) >= 1.05
BuildRequires:	perl(Net::SMTP) >= 1.03
BuildRequires:	perl-TimeDate
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MailTools - a set of perl modules related to mail applications.

%description -l pl
MailTools - zestaw narzêdzi do pracy z poczt± i aplikacjami
pocztowymi.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install {README.*,bin/*} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/README.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitelib}/Mail/*.pm
%{perl_sitelib}/Mail/Field
%{perl_sitelib}/Mail/Mailer
%{perl_sitelib}/auto/Mail
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
