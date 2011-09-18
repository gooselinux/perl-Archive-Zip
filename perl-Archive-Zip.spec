Name:           perl-Archive-Zip
Version:        1.30
Release:        2%{?dist}
Summary:        Perl library for accessing Zip archives

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Archive-Zip/
Source0:        http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Archive-Zip-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  perl(Compress::Zlib) >= 1.14
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Which) >= 0.05
BuildRequires:  perl(Test::More)
BuildRequires:  unzip
BuildRequires:  zip

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The Archive::Zip module allows a Perl program to create, manipulate,
read, and write Zip archive files.
Zip archives can be created, or you can read from existing zip files.
Once created, they can be written to files, streams, or strings.
Members can be added, removed, extracted, replaced, rearranged, and
enumerated.  They can also be renamed or have their dates, comments,
or other attributes queried or modified.  Their data can be compressed
or uncompressed as needed.  Members can be created from members in
existing Zip files, or from existing directories, files, or strings.


%prep
%setup -q -n Archive-Zip-%{version}
%{__perl} -pi -e 's|^#!/bin/perl|#!%{__perl}|' examples/*.pl
%{__perl} -pi -e 's|^#!/usr/local/bin/perl|#!%{__perl}|' examples/selfex.pl


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README examples/
%{_bindir}/crc32
%{perl_vendorlib}/Archive/
%{_mandir}/man3/Archive*.3*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.30-2
- rebuild against perl 5.10.1

* Mon Jul 27 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.30-1
- update to 1.30

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May 16 2008 Steven Pritchard <steve@kspei.com> 1.23-1
- Update to 1.23.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.20-5
- Rebuild for perl 5.10 (again)

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.20-4
- rebuild for new perl

* Mon Aug 23 2007 Robin Norwood <rnorwood@redhat.com> - 1.20-3
- Fix license tag

* Wed Jun 27 2007 Robin Norwood <rnorwood@redhat.com> - 1.20-2
- Resolves: rhbz#226240
- Incorporate changes from Steven Pritchard's package review
- Fix find option order.
- Use fixperms macro instead of our own chmod incantation.
- Remove check macro cruft.
- Update build dependencies.
- Package LICENSE.
- BR unzip, zip for better test coverage.

* Tue Jun 05 2007 Robin Norwood <rnorwood@redhat.com> - 1.20-1
- Update to latest CPAN version: 1.20
- Fix broken changelog

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.16-1.2.1
- rebuild

* Fri Feb 03 2006 Jason Vas Dias<jvdias@redhat.com> - 1.16-1.2
- rebuilt for new perl-5.8.8

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Mon Jul 11 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.16-1
- Update to 1.16.

* Thu Apr 14 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.14-1
- Update to 1.14.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Aug 15 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.12-0.fdr.1
- Update to 1.12.

* Tue Jul  6 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.11-0.fdr.1
- Update to 1.11.
- Bring up to date with current fedora.us Perl spec template.

* Sun Apr 18 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.10-0.fdr.1
- Update to 1.10.
- Reduce directory ownership bloat.
- Require perl(:MODULE_COMPAT_*).

* Fri Nov 28 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.09-0.fdr.1
- Update to 1.09.

* Wed Oct 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.08-0.fdr.1
- Update to 1.08.

* Tue Oct 21 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.07-0.fdr.1
- Update to 1.07.

* Sun Sep 14 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.06-0.fdr.1
- Update to 1.06.
- Specfile cleanups.

* Sun Jun  8 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.05-0.fdr.1
- First build.
