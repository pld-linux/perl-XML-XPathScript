#
# Conditional build:
%bcond_without	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	XML-XPathScript
Summary:	XML::XPathScript - XML templating language
Summary(pl.UTF-8):	XML::XPathScript - język szablonów XML
Name:		perl-XML-XPathScript
Version:	0.14
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	69910ecc1f07d4943f5a42c0d96abf21
URL:		http://axkit.org/
BuildRequires:	perl-XML-XPath
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XPathScript is an XML templating language that has some concepts from
ASP and some from XSLT. This makes for a very flexible option for
transforming XML to HTML or text or just about any other format.

%description -l pl.UTF-8
XPathScript to język szablonów XML zawierający trochę pomysłów z ASP i
trochę z XSLT. Składa się to na bardzo elastyczny sposób
przekształcania XML-a do HTML-a, tekstu lub dowolnego innego formatu.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/XML/*.pm
%{perl_vendorlib}/XML/XPathScript
%{_mandir}/man3/*

#%{perl_vendorlib}/Apache/AxKit/Language/YPathScript.pm
