Summary: Image loading library for SDL
Name: SDL_image
Version: 1.2.4
Release: 2%{?dist}
Source: http://www.libsdl.org/projects/SDL_image/release/%{name}-%{version}.tar.gz
URL: http://www.libsdl.org/projects/SDL_image/
License: LGPL
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: SDL-devel >= 1.2.4-1, libjpeg-devel, libpng-devel, libtiff-devel

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, PPM, PCX, GIF, JPEG, PNG) as SDL surfaces.

%package devel
Summary: Development files for the SDL image loading library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: SDL-devel >= 1.2.4-1

%description devel
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains the files needed for development using
the SDL image loading library contained in the SDL_image package.

%prep

%setup -q

%build
# XCF support is crashy in 1.2.4
%configure --disable-dependency-tracking --enable-tif
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall
mkdir -p $RPM_BUILD_ROOT%{_bindir}
./libtool --mode=install /usr/bin/install showimage $RPM_BUILD_ROOT%{_bindir}

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README CHANGES COPYING
%{_bindir}/showimage
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/lib*.so
%{_includedir}/SDL/*

%changelog
* Sat Jun 25 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.2.4-2
- Rebuild.

* Sun Jun 19 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.2.4-1
- 1.2.4, patches obsolete.
- Bring back TIFF support (BuildRequire libtiff-devel).
- Build with dependency tracking disabled.
- Require exact EVR of main package in -devel.

* Thu May 26 2005 Bill Nottingham <notting@redhat.com> 1.2.3-9
- rebuild

* Wed Feb  9 2005 Thomas Woerner <twoerner@redhat.com> 1.2.3-7
- rebuild

* Thu Sep 30 2004 Thomas Woerner <twoerner@redhat.com> 1.2.3-6
- moved to new autofoo utils

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 18 2003 Thomas Woerner <twoerner@redhat.com> 1.2.3-3
- fixed build with automake-1.7

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May  6 2003 Thomas Woerner <twoerner@redhat.com> 1.2.3-1
- new version 1.2.3

* Mon Feb 17 2003 Elliot Lee <sopwith@redhat.com>
- ppc64 fix

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Sun Dec 01 2002 Elliot Lee <sopwith@redhat.com>
- Remove unpackaged files

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.2-1
- 1.2.2

* Fri Mar  1 2002 Than Ngo <than@redhat.com> 1.2.1-4
- rebuild in new env

* Thu Jan 24 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.1-3
- Rebuild to get rid of superfluous dependencies
- Clean up spec file

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jan  7 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.1-1
- 1.2.1
- Require arts-devel rather than the obsolete kdelibs-sound-devel

* Fri Oct 26 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.0-4
- Rebuild with new libpng

* Tue Jul 24 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add build requirements (#49827)

* Tue Jul 10 2001 Elliot Lee <sopwith@redhat.com>
- Rebuild

* Sun Apr 15 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.2.0

* Sun Jan  7 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.1.0
- Use %%post -p, %%postun -p
- devel requires %%{name} = %%{version} rather than just %%{name}
- enable tiff support

* Tue Dec 19 2000 Than Ngo <than@redhat.com>
- added missing %post and %%postun

* Wed Nov 29 2000 Than Ngo <than@redhat.com>
- first build for 7.1
