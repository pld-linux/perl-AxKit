#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	AxKit
Summary:	AxKit - The Apache XML Delivery Toolkit
Summary(pl):	AxKit - narzêdzia dostarczaj±ce XML dla Apache'a
Name:		perl-AxKit
%define		_axver	1.61
Version:	1.6.1
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
URL:		http://axkit.org/
%if %{!?_with_tests:0}%{?_with_tests:1}
BuildRequires:	perl-Apache-Filter
%endif
BuildRequires:	apache-mod_perl >= 1.17
BuildRequires:	libxml2-devel
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-DBI
BuildRequires:	perl-Digest-MD5 >= 2.09
BuildRequires:	perl-Error >= 0.14
BuildRequires:	perl-IPC-Run
BuildRequires:	perl-XML-Handler-AxPoint
BuildRequires:	perl-XML-LibXML-SAX >= 1.50
BuildRequires:	perl-XML-LibXSLT >= 1.49
BuildRequires:	perl-XML-Parser >= 2.27
BuildRequires:	perl-XML-SAX-Writer
BuildRequires:	perl-XML-Sablotron >= 0.40
BuildRequires:	perl-XML-XPath >= 1.00
BuildRequires:	perl-XMLNews-HTMLTemplate
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-libapreq >= 0.32
BuildRequires:	perl-libxml-enno
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	apache-mod_perl >= 1.17
Requires:	perl-Digest-MD5 >= 2.09
Requires:	perl-libapreq >= 0.32
BuildConflicts:	perl-XML-LibXML = 1.53
Conflicts:	perl-HTTP-GHTTP < 1.00
Conflicts:	perl-XML-LibXML = 1.53
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Apache XML Delivery Toolkit (AxKit) is a suite of tools for the
Apache httpd server running mod_perl, that give developers extremely
flexible options for delivering XML to all kinds of browsers, from
handheld systems, Braille readers, and ordinary browsers. All this can
be achieved using nothing but W3C standards, although the plugin
architecture provides the hooks for developers to write their own
stylesheet systems, should they so desire.

%description -l pl
AxKit (Apache XML Delivery Toolkit) to zestaw narzêdzi dla serwera
Apache z dzia³aj±cym modu³em mod_perl, daj±cy programistom bardzo
elastyczne mo¿liwo¶ci dostarczania XML do wszystkich rodzajów
przegl±darek: z palmtopów, czytników Braille'a, zwyk³ych przegl±darek.
Wszystko to mo¿na osi±gn±æ przy pomocy samych standardów W3C, ale
architektura wtycznek udostêpnia programistom punkty zaczepienia
pozwalaj±ce na pisanie w³asnych systemów stylów.

%package Language-AxPoint
Summary:	AxPoint - an AxKit PDF Slideshow generator
Summary(pl):	AxPoint - generator slajdów PDF do AxKitu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Language-AxPoint
AxPoint allows you to create PDF slideshows or presentations using an
XML definition of the slideshow.

%description Language-AxPoint -l pl
AxPoint pozwala na tworzenie slajdów lub prezentacji PDF przy u¿yciu
definicji XML.

%package Language-HtmlDoc
Summary:	HtmlDoc module for AxKit - deliver XHTML as PDF
Summary(pl):	Modu³ HtmlDoc do AxKitu - dostarczajacy XHTML jako PDF
Group:		Development/Languages/Perl
Requires:	%{name}-Language-LibXSLT = %{version}
Requires:	htmldoc

%description Language-HtmlDoc
HtmlDoc module allows to convert any XHTML page into a quite nice
looking PDF document. Be prepared to do some tweaking of your XHTML
input, though, because HTMLDOC is HTML 3.2 only, it does not yet
understand CSS and only some HTML 4.0 (as of version 1.8.18). Using an
extra XSLT stylesheet, it isn't all that hard to create HTMLDOC
friendly input and you get nice results.

%description Language-HtmlDoc -l pl
Modu³ HtmlDoc pozwala na konwertowanie stron XHTML na dosyæ ³adnie
wygl±daj±ce dokumenty PDF. Trzeba jednak uwa¿aæ na wej¶ciowy XHTML,
poniewa¿ HTMLDOC rozumie tylko HTML 3.2, nie obs³uguje CSS i czê¶ci
HTML 4.0 (stan z wersji 1.8.18). Ale przy u¿yciu dodatkowego arkusza
XSLT nie jest trudne przygotowanie odpowiedniego wej¶cia dla HTMLDOC,
aby osi±gn±æ ³adne wyniki.

%package Language-LibXSLT
Summary:	LibXSLT module for AxKit
Summary(pl):	Modu³ LibXSLT do AxKitu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}
Requires:	perl-XML-LibXSLT >= 1.49

%description Language-LibXSLT
LibXSLT module for AxKit.

%description Language-LibXSLT -l pl
Modu³ LibXSLT do AxKitu.

%package Language-PassiveTeX
Summary:	PassiveTeX module for AxKit
Summary(pl):	Modu³ PassiveTeX do AxKitu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}
Requires:	passivetex

%description Language-PassiveTeX
PassiveTeX module for AxKit.

%description Language-PassiveTeX -l pl
Modu³ PassiveTeX do AxKitu.

%package Language-Query
Summary:	Query module for AxKit
Summary(pl):	Modu³ Query do AxKitu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Language-Query
Query module for AxKit.

%description Language-Query -l pl
Modu³ Query do AxKitu.

%package Language-SAXMachines
Summary:	SAXMachines module for AxKit - transform content with SAX Filters
Summary(pl):	Modu³ SAXMachines do AxKitu - przepuszczaj±cy zawarto¶æ przez filtry SAX
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}
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

%description Language-SAXMachines -l pl
Modu³ Language::SAXMachines udostêpnia ³atwy sposób (poprzez modu³
XML::SAX::Machines Barrie Slaymakera) na u¿yawnie ³añcuchów filtrów
SAX do przekszta³cania zawarto¶ci XML. Technicznie nie jest to "jêzyk"
w takim sensie jak XSP, XPathScript czy XSLT, poniewa¿ nie ma arkuszy
styli do zapisywania ani przetwarzania. Zamiast tego filtry SAX s±
dodawane poprzez dyrektywy konfiguracyjne w plikach .htaccess lub
*.conf.

%package Language-Sablot
Summary:	Sablot module for AxKit
Summary(pl):	Modu³ Sablot do AxKitu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Language-Sablot
Sablot module for AxKit.

%description Language-Sablot -l pl
Modu³ Sablot do AxKitu.

%package Language-XMLNews
Summary:	XMLNews modules for AxKit
Summary(pl):	Modu³y XMLNews do AxKitu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Language-XMLNews
XMLNews modules (XMLNewsNITF and XMLNewsRDF) for AxKit.

%description Language-XMLNews -l pl
Modu³y XMLNews (XMLNewsNITF i XMLNewsRDF) do AxKitu.

%package Language-XPathScript
Summary:	XPathScript language module for AxKit
Summary(pl):	Modu³ jêzyka XPathScript do AxKitu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}
Requires:	perl-XML-Parser >= 2.27
Requires:	perl-XML-XPath >= 1.00

%description Language-XPathScript
XPathScript language module for AxKit.

%description Language-XPathScript -l pl
Modu³ jêzyka XPathScript do AxKitu.

%package Language-XSP
Summary:	XSP language module for AxKit - eXtensible Server Pages
Summary(pl):	Modu³ jêzykowy XSP do AxKitu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}
Requires:	perl-XML-LibXML >= 1.50

%description Language-XSP
XSP language module for AxKit - eXtensible Server Pages.

%description Language-XSP -l pl
Modu³ jêzykowy XSP do AxKitu - "Rozszerzalne Strony Serwera".

%prep
%setup -q -n %{pnam}-%{_axver}

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

cp -rf demo examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIB Changes README SUPPORT TODO axkit.org
%{perl_sitearch}/AxKit.pm
%dir %{perl_sitearch}/Apache/AxKit
%{perl_sitearch}/Apache/AxKit/*.pm
%dir %{perl_sitearch}/Apache/AxKit/Language
%{perl_sitearch}/Apache/AxKit/MediaChooser
%dir %{perl_sitearch}/Apache/AxKit/Plugin
%{perl_sitearch}/Apache/AxKit/Plugin/[^F]*.pm
%{perl_sitearch}/Apache/AxKit/Provider
%{perl_sitearch}/Apache/AxKit/StyleChooser
%dir %{perl_sitearch}/auto/AxKit
%{perl_sitearch}/auto/AxKit/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/AxKit/*.so
%dir %{perl_sitearch}/auto/Apache/AxKit/CharsetConv
%{perl_sitearch}/auto/Apache/AxKit/CharsetConv/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Apache/AxKit/CharsetConv/*.so
%{_mandir}/man3/AxKit.3pm*
%{_mandir}/man3/Apache::AxKit::[^LP]*
%{_mandir}/man3/Apache::AxKit::Language.3pm*
%{_mandir}/man3/Apache::AxKit::Provider*
%{_mandir}/man3/Apache::AxKit::Plugin::[^F]*
%{_examplesdir}/%{name}-%{version}

%files Language-AxPoint
%defattr(644,root,root,755)
%{perl_sitearch}/Apache/AxKit/Language/AxPoint.pm
%{_mandir}/man3/Apache::AxKit::Language::AxPoint.3pm*

%files Language-HtmlDoc
%defattr(644,root,root,755)
%{perl_sitearch}/Apache/AxKit/Language/HtmlDoc.pm
%{_mandir}/man3/Apache::AxKit::Language::HtmlDoc.3pm*

%files Language-LibXSLT
%defattr(644,root,root,755)
%{perl_sitearch}/Apache/AxKit/Language/LibXSLT.pm

%files Language-PassiveTeX
%defattr(644,root,root,755)
%{perl_sitearch}/Apache/AxKit/Language/PassiveTeX.pm

%files Language-Query
%defattr(644,root,root,755)
%{perl_sitearch}/Apache/AxKit/Language/Query.pm

%files Language-SAXMachines
%defattr(644,root,root,755)
%{perl_sitearch}/Apache/AxKit/Language/SAXMachines.pm
%{_mandir}/man3/Apache::AxKit::Language::SAXMachines.3pm*

%files Language-Sablot
%defattr(644,root,root,755)
%{perl_sitearch}/Apache/AxKit/Language/Sablot.pm

%files Language-XMLNews
%defattr(644,root,root,755)
%{perl_sitearch}/Apache/AxKit/Language/XMLNews*.pm

%files Language-XPathScript
%defattr(644,root,root,755)
%{perl_sitearch}/Apache/AxKit/Language/XPathScript.pm
%{perl_sitearch}/Apache/AxKit/Plugin/Fragment.pm
%{_mandir}/man3/Apache::AxKit::Language::XPathScript.3pm*
%{_mandir}/man3/Apache::AxKit::Plugin::Fragment.3pm*

%files Language-XSP
%defattr(644,root,root,755)
%{perl_sitearch}/Apache/AxKit/Language/XSP.pm
%{perl_sitearch}/Apache/AxKit/Language/XSP
%{_mandir}/man3/Apache::AxKit::Language::XSP*
