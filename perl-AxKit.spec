#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires server)
#
%define		pdir	Apache
%define		pnam	AxKit
%define		_axver	1.62
Summary:	AxKit - the Apache XML delivery toolkit
Summary(pl.UTF-8):	AxKit - narzędzia dostarczające XML dla Apache'a
Name:		perl-AxKit
Version:	1.6.2
Release:	1
License:	GPL v2 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	1634ad62ac941c7d2ee3b1a2d129c14a
URL:		http://axkit.org/
BuildRequires:	apache-mod_perl >= 1.17
BuildRequires:	libxml2-devel
%if %{with tests}
BuildRequires:	perl-Apache-Filter
%endif
BuildRequires:	perl-Apache-Test >= 1.00
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-DBI
BuildRequires:	perl-Digest-MD5 >= 2.09
BuildRequires:	perl-Error >= 0.14
BuildRequires:	perl-IPC-Run
BuildRequires:	perl-XML-DOM
BuildRequires:	perl-XML-Handler-AxPoint
BuildRequires:	perl-XML-LibXML-SAX >= 1.51
BuildRequires:	perl-XML-LibXSLT >= 1.49
BuildRequires:	perl-XML-Parser >= 2.27
BuildRequires:	perl-XML-SAX-Writer
BuildRequires:	perl-XML-Sablotron >= 0.40
BuildRequires:	perl-XML-XPath >= 1.00
BuildRequires:	perl-XMLNews-HTMLTemplate
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libapreq >= 0.32
BuildRequires:	perltidy
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildConflicts:	perl-XML-LibXML = 1.53
Requires:	apache-mod_perl >= 1.17
Requires:	perl-Digest-MD5 >= 2.09
Requires:	perl-libapreq >= 0.32
Conflicts:	perl-HTTP-GHTTP < 1.00
Conflicts:	perl-XML-LibXML = 1.53
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	'perl(UNIVERSAL)'

%description
The Apache XML Delivery Toolkit (AxKit) is a suite of tools for the
Apache httpd server running mod_perl, that give developers extremely
flexible options for delivering XML to all kinds of browsers, from
handheld systems, Braille readers, and ordinary browsers. All this can
be achieved using nothing but W3C standards, although the plugin
architecture provides the hooks for developers to write their own
stylesheet systems, should they so desire.

%description -l pl.UTF-8
AxKit (Apache XML Delivery Toolkit) to zestaw narzędzi dla serwera
Apache z działającym modułem mod_perl, dający programistom bardzo
elastyczne możliwości dostarczania XML-a do wszystkich rodzajów
przeglądarek: z palmtopów, czytników Braille'a, zwykłych przeglądarek.
Wszystko to można osiągnąć przy pomocy samych standardów W3C, ale
architektura wtycznek udostępnia programistom punkty zaczepienia
pozwalające na pisanie własnych systemów stylów.

%package Language-AxPoint
Summary:	AxPoint - an AxKit PDF Slideshow generator
Summary(pl.UTF-8):	AxPoint - generator slajdów PDF do AxKitu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description Language-AxPoint
AxPoint allows you to create PDF slideshows or presentations using an
XML definition of the slideshow.

%description Language-AxPoint -l pl.UTF-8
AxPoint pozwala na tworzenie slajdów lub prezentacji PDF przy użyciu
definicji XML.

%package Language-HtmlDoc
Summary:	HtmlDoc module for AxKit - deliver XHTML as PDF
Summary(pl.UTF-8):	Moduł HtmlDoc do AxKitu - dostarczajacy XHTML jako PDF
Group:		Development/Languages/Perl
Requires:	%{name}-Language-LibXSLT = %{version}-%{release}
Requires:	htmldoc

%description Language-HtmlDoc
HtmlDoc module allows to convert any XHTML page into a quite nice
looking PDF document. Be prepared to do some tweaking of your XHTML
input, though, because HTMLDOC is HTML 3.2 only, it does not yet
understand CSS and only some HTML 4.0 (as of version 1.8.18). Using an
extra XSLT stylesheet, it isn't all that hard to create HTMLDOC
friendly input and you get nice results.

%description Language-HtmlDoc -l pl.UTF-8
Moduł HtmlDoc pozwala na konwertowanie stron XHTML na dosyć ładnie
wyglądające dokumenty PDF. Trzeba jednak uważać na wejściowy XHTML,
ponieważ HTMLDOC rozumie tylko HTML 3.2, nie obsługuje CSS i części
HTML 4.0 (stan z wersji 1.8.18). Ale przy użyciu dodatkowego arkusza
XSLT nie jest trudne przygotowanie odpowiedniego wejścia dla HTMLDOC,
aby osiągnąć ładne wyniki.

%package Language-LibXSLT
Summary:	LibXSLT module for AxKit
Summary(pl.UTF-8):	Moduł LibXSLT do AxKitu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	perl-XML-LibXSLT >= 1.49

%description Language-LibXSLT
LibXSLT module for AxKit.

%description Language-LibXSLT -l pl.UTF-8
Moduł LibXSLT do AxKitu.

%package Language-PassiveTeX
Summary:	PassiveTeX module for AxKit
Summary(pl.UTF-8):	Moduł PassiveTeX do AxKitu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	passivetex

%description Language-PassiveTeX
PassiveTeX module for AxKit.

%description Language-PassiveTeX -l pl.UTF-8
Moduł PassiveTeX do AxKitu.

%package Language-Query
Summary:	Query module for AxKit
Summary(pl.UTF-8):	Moduł Query do AxKitu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description Language-Query
Query module for AxKit.

%description Language-Query -l pl.UTF-8
Moduł Query do AxKitu.

%package Language-SAXMachines
Summary:	SAXMachines module for AxKit - transform content with SAX Filters
Summary(pl.UTF-8):	Moduł SAXMachines do AxKitu - przepuszczający zawartość przez filtry SAX
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	perl-XML-LibXML-SAX >= 1.50
Requires:	perl-XML-LibXSLT >= 1.49
# not found by perl.req???
Requires:	perl-XML-SAX-Machines

%description Language-SAXMachines
Language::SAXMachines provides an easy way (via Barrie Slaymaker's
XML::SAX::Machines) to use SAX filter chains to transform XML content.
It is not technically a "language" in the same sense that XSP,
XPathScript, or XSLT are since there is no stylesheet to write or
process. Instead, the SAX filters are added via config directives in
your .htaccess or *.conf file.

%description Language-SAXMachines -l pl.UTF-8

Moduł Language::SAXMachines udostępnia łatwy sposób (poprzez moduł
XML::SAX::Machines Barrie Slaymakera) na użyawnie łańcuchów filtrów
SAX do przekształcania XML-a. Technicznie nie jest to "język" w takim
sensie jak XSP, XPathScript czy XSLT, ponieważ nie ma arkuszy styli do
zapisywania ani przetwarzania. Zamiast tego filtry SAX są dodawane
poprzez dyrektywy konfiguracyjne w plikach .htaccess lub *.conf.

%package Language-Sablot
Summary:	Sablot module for AxKit
Summary(pl.UTF-8):	Moduł Sablot do AxKitu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description Language-Sablot
Sablot module for AxKit.

%description Language-Sablot -l pl.UTF-8
Moduł Sablot do AxKitu.

%package Language-XMLNews
Summary:	XMLNews modules for AxKit
Summary(pl.UTF-8):	Moduły XMLNews do AxKitu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description Language-XMLNews
XMLNews modules (XMLNewsNITF and XMLNewsRDF) for AxKit.

%description Language-XMLNews -l pl.UTF-8
Moduły XMLNews (XMLNewsNITF i XMLNewsRDF) do AxKitu.

%package Language-XPathScript
Summary:	XPathScript language module for AxKit
Summary(pl.UTF-8):	Moduł języka XPathScript do AxKitu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	perl-XML-Parser >= 2.27
Requires:	perl-XML-XPath >= 1.00

%description Language-XPathScript
XPathScript language module for AxKit.

%description Language-XPathScript -l pl.UTF-8
Moduł języka XPathScript do AxKitu.

%package Language-XSP
Summary:	XSP language module for AxKit - eXtensible Server Pages
Summary(pl.UTF-8):	Moduł językowy XSP do AxKitu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	perl-XML-LibXML >= 1.50

%description Language-XSP
XSP language module for AxKit - eXtensible Server Pages.

%description Language-XSP -l pl.UTF-8
Moduł językowy XSP do AxKitu - "Rozszerzalne Strony Serwera".

%prep
%setup -q -n %{pnam}-%{_axver}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

# some problem with XML constants - broken test ?
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf demo examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIB Changes README SUPPORT TODO axkit.org
%{perl_vendorarch}/AxKit.pm
%dir %{perl_vendorarch}/Apache/AxKit
%{perl_vendorarch}/Apache/AxKit/*.pm
%dir %{perl_vendorarch}/Apache/AxKit/Language
%{perl_vendorarch}/Apache/AxKit/MediaChooser
%dir %{perl_vendorarch}/Apache/AxKit/Plugin
%{perl_vendorarch}/Apache/AxKit/Plugin/[!F]*.pm
%{perl_vendorarch}/Apache/AxKit/Provider
%{perl_vendorarch}/Apache/AxKit/StyleChooser
%dir %{perl_vendorarch}/auto/AxKit
%attr(755,root,root) %{perl_vendorarch}/auto/AxKit/*.so
%dir %{perl_vendorarch}/auto/Apache/AxKit/CharsetConv
%attr(755,root,root) %{perl_vendorarch}/auto/Apache/AxKit/CharsetConv/*.so
%{_mandir}/man3/AxKit.3pm*
%{_mandir}/man3/Apache::AxKit::[!LP]*
%{_mandir}/man3/Apache::AxKit::Language.3pm*
%{_mandir}/man3/Apache::AxKit::LibXMLSupport.3pm*
%{_mandir}/man3/Apache::AxKit::Provider*
%{_mandir}/man3/Apache::AxKit::Plugin::[!F]*
%{_examplesdir}/%{name}-%{version}

%files Language-AxPoint
%defattr(644,root,root,755)
%{perl_vendorarch}/Apache/AxKit/Language/AxPoint.pm
%{_mandir}/man3/Apache::AxKit::Language::AxPoint.3pm*

%files Language-HtmlDoc
%defattr(644,root,root,755)
%{perl_vendorarch}/Apache/AxKit/Language/HtmlDoc.pm
%{_mandir}/man3/Apache::AxKit::Language::HtmlDoc.3pm*

%files Language-LibXSLT
%defattr(644,root,root,755)
%{perl_vendorarch}/Apache/AxKit/Language/LibXSLT.pm

%files Language-PassiveTeX
%defattr(644,root,root,755)
%{perl_vendorarch}/Apache/AxKit/Language/PassiveTeX.pm

%files Language-Query
%defattr(644,root,root,755)
%{perl_vendorarch}/Apache/AxKit/Language/Query.pm

%files Language-SAXMachines
%defattr(644,root,root,755)
%{perl_vendorarch}/Apache/AxKit/Language/SAXMachines.pm
%{_mandir}/man3/Apache::AxKit::Language::SAXMachines.3pm*

%files Language-Sablot
%defattr(644,root,root,755)
%{perl_vendorarch}/Apache/AxKit/Language/Sablot.pm

%files Language-XMLNews
%defattr(644,root,root,755)
%{perl_vendorarch}/Apache/AxKit/Language/XMLNews*.pm

%files Language-XPathScript
%defattr(644,root,root,755)
%{perl_vendorarch}/Apache/AxKit/Language/XPathScript.pm
%{perl_vendorarch}/Apache/AxKit/Plugin/Fragment.pm
%{_mandir}/man3/Apache::AxKit::Language::XPathScript.3pm*
%{_mandir}/man3/Apache::AxKit::Plugin::Fragment.3pm*

%files Language-XSP
%defattr(644,root,root,755)
%{perl_vendorarch}/Apache/AxKit/Language/XSP.pm
%{perl_vendorarch}/Apache/AxKit/Language/XSP
%{_mandir}/man3/Apache::AxKit::Language::XSP*
