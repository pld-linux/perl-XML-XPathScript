#
# Conditional build:
%bcond_without	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	XML-XPathScript
Summary:	XML::XPathScript - XML templating language
Summary(pl):	XML::XPathScript - jêzyk szablonów XML
Name:		perl-XML-XPathScript
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	958b448047923e989c8d1f6e38fc2d2c
URL:		http://axkit.org/
BuildRequires:	perl-XML-XPath
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XPathScript is an XML templating language that has some concepts from
ASP and some from XSLT. This makes for a very flexible option for
transforming XML to HTML or text or just about any other format.

%description -l pl
XPathScript to jêzyk szablonów XML zawieraj±cy trochê pomys³ów z ASP i
trochê z XSLT. Sk³ada siê to na bardzo elastyczny sposób
przekszta³cania XML-a do HTML-a, tekstu lub dowolnego innego formatu.

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
%{_mandir}/man3/*
