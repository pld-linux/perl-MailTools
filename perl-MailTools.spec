#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	Tools
Summary:	MailTools - a set of Perl modules related to mail applications
Summary(pl):	MailTools - zestaw modu³ów perlowych do pracy z poczt± i aplikacjami pocztowymi
Name:		perl-MailTools
Version:	1.74
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mail/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	aba82a7eb87906278d98174e10d838be
URL:		http://search.cpan.org/dist/MailTools/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl(Net::Domain) >= 1.05
BuildRequires:	perl(Net::SMTP) >= 1.03
BuildRequires:	perl-TimeDate
BuildRequires:	perl-libnet
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

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
