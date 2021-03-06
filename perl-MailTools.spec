#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Mail
%define		pnam	Tools
Summary:	MailTools - a set of Perl modules related to mail applications
Summary(pl.UTF-8):	MailTools - zestaw modułów perlowych do pracy z pocztą i aplikacjami pocztowymi
Name:		perl-MailTools
Version:	2.21
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mail/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	69ee516d40011e7e92b77c6f06c0dc01
URL:		http://search.cpan.org/dist/MailTools/
BuildRequires:	perl-devel >= 1:5.8.1
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

%description -l pl.UTF-8
MailTools - zestaw narzędzi do pracy z pocztą i aplikacjami
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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Mail/*.pod

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a README.* examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
gzip -9nf $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/README.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/MailTools.pm
%{perl_vendorlib}/Mail/Address.pm
%{perl_vendorlib}/Mail/Cap.pm
%{perl_vendorlib}/Mail/Field.pm
%{perl_vendorlib}/Mail/Filter.pm
%{perl_vendorlib}/Mail/Header.pm
%{perl_vendorlib}/Mail/Internet.pm
%{perl_vendorlib}/Mail/Mailer.pm
%{perl_vendorlib}/Mail/Send.pm
%{perl_vendorlib}/Mail/Util.pm
%{perl_vendorlib}/Mail/Field
%{perl_vendorlib}/Mail/Mailer
%{_mandir}/man3/MailTools.3pm*
%{_mandir}/man3/Mail*::*.3pm*
%{_examplesdir}/%{name}-%{version}
