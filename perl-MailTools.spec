#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	Tools
Summary:	MailTools - a set of perl modules related to mail applications
Summary(pl):	MailTools - zestaw narzêdzi do pracy z poczt± i aplikacjami pocztowymi
Name:		perl-MailTools
Version:	1.62
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	cc1f222e7a53518fb214ecdea05e5b4d
BuildRequires:	perl-devel >= 5.6
%if %{with tests}
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

%{?_with_tests:%{__make} test}

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
