#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	XML-XPathScript
Summary:	XML templating language
Name:		perl-XML-XPathScript
Version:	0.03
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
URL:		http://axkit.org/
BuildRequires:	perl-XML-XPath
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XPathScript is an XML templating language that has some concepts from ASP
and some from XSLT. This makes for a very flexible option for transforming
XML to HTML or text or just about any other format.

%prep
%setup -q -n %{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

# some problem with XML constants - broken test ?
%{?_with_tests:%{__make} test}

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
%{perl_sitelib}/XML/*.pm
%{_mandir}/man3/*
	       
