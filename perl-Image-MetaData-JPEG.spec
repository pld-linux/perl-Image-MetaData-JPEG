#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Image
%define	pnam	MetaData-JPEG
Summary:	Image::MetaData::JPEG - Perl extension for showing/modifying JPEG (meta)data
Name:		perl-Image-MetaData-JPEG
Version:	0.15
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Image/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a6d6a38bf07343aa1749d7fb6a5442ca
URL:		http://search.cpan.org/dist/Image-MetaData-JPEG/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The purpose of this module is to read/modify/rewrite meta-data
segments in JPEG (Joint Photographic Experts Group format) files,
which can contain comments, thumbnails, Exif information (photographic
parameters), IPTC information (editorial parameters) and similar data.

Each JPEG file is made of consecutive segments (tagged data blocks),
and the actual row picture data. Most of these segments specify
parameters for decoding the picture data into a bitmap; some of them,
namely the COMment and APPlication segments, contain instead
meta-data, i.e., information about how the photo was shot (usually
added by a digital camera) and additional notes from the photograph.
These additional pieces of information are especially valuable for
picture databases, since the meta-data can be saved together with the
picture without resorting to additional database structures. See the
appendix about the structure of JPEG files for technical details.

This module works by breaking a JPEG file into individual segments.
Each file is associated to an Image::MetaData::JPEG structure object,
which contains one Image::MetaData::JPEG::Segment object for each
segment. Segments with a known format are then parsed, and their
content can be accessed in a structured way for display. Some of them
can even be modified and then rewritten to disk.

# %description -l pl.UTF-8 # TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Image/MetaData/*.pm
%{perl_vendorlib}/Image/MetaData/JPEG
%{_mandir}/man3/*
