#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	Tools
Summary:	MailTools - a set of perl modules related to mail applications
Summary(pl):	MailTools - zestaw narzêdzi do pracy z poczt± i aplikacjami pocztowymi
Name:		perl-MailTools
Version:	1.58
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	9c03ab8274cf053e8e58db953fe8432b
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-libnet
BuildRequires:	perl(Net::Domain) >= 1.05
BuildRequires:	perl(Net::SMTP) >= 1.03
BuildRequires:	perl-TimeDate
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MailTools - a set of perl modules related to mail applications.

%description -l pl
MailTools - zestaw narzêdzi do pracy z poczt± i aplikacjami pocztowymi.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a README.* examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
gzip -9nf $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/README.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorlib}/Mail/*.pm
%{perl_vendorlib}/Mail/Field
%{perl_vendorlib}/Mail/Mailer
%{perl_vendorlib}/auto/Mail/*
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
