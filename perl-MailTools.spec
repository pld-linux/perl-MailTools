%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	MailTools perl module
Summary(pl):	Modu³ perla MailTools
Name:		perl-MailTools
Version:	1.13
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Mail/MailTools-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
MailTools - a set of perl modules related to mail applications.

%description -l pl
MailTools - zestaw modu³ów 

%prep
%setup -q -n MailTools-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

make install DESTDIR=$RPM_BUILD_ROOT

install {README.*,bin/*} $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Mail
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	$RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}/README.* \
        ChangeLog README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/Mail/*.pm
%{perl_sitelib}/Mail/Field
%{perl_sitelib}/Mail/Mailer
%{perl_sitelib}/auto/Mail/Internet
%{perl_sitelib}/auto/Mail/Util
%{perl_sitearch}/auto/Mail

%{_mandir}/man3/*

/usr/src/examples/%{name}-%{version}
