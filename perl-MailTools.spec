%include	/usr/lib/rpm/macros.perl
Summary:	MailTools perl module
Summary(pl):	Modu³ perla MailTools
Name:		perl-MailTools
Version:	1.13
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Mail/MailTools-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-libnet
BuildRequires:	perl-TimeDate
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MailTools - a set of perl modules related to mail applications.

%description -l pl
MailTools - zestaw narzêdzi do pracy z poczt± i aplikacjami
pocztowymi.

%prep
%setup -q -n MailTools-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install {README.*,bin/*} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/README.* \
        ChangeLog README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Mail/*.pm
%{perl_sitelib}/Mail/Field
%{perl_sitelib}/Mail/Mailer
%{perl_sitelib}/auto/Mail/Internet
%{perl_sitelib}/auto/Mail/Util
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
