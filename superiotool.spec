%define name superiotool
%define svnversion 20111206
%define version 0.%{svnversion} 

Summary:	Detect which Super I/O you have on your mainboard
Name:		%{name}
Version:	20121019
Release:	1
Source0:	%{name}-%{svnversion}.tar.bz2
License:	GPL
Group:		System/Kernel and hardware
Url:		http://www.coreboot.org/Superiotool
BuildRequires:	pciutils-devel
Patch0:		makefiles_normal_dir.patch

%description
Superiotool is a GPL'd user-space helper tool for LinuxBIOS development 
purposes (but may also be useful for other things).
It allows you to detect which Super I/O you have on your mainboard,
and it can provide detailed information about the register contents
of the Super I/O.

%prep
%setup -q -n %name
%patch0 -p1

%build
%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%{_sbindir}/superiotool
%{_mandir}/man8/superiotool*



%changelog
* Mon Dec 05 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.20111206-1
+ Revision: 737954
- version update to upstream git checkout

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 0.20071017-5mdv2010.0
+ Revision: 434187
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.20071017-4mdv2009.0
+ Revision: 261236
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.20071017-3mdv2009.0
+ Revision: 253734
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Oct 17 2007 Erwan Velu <erwan@mandriva.org> 0.20071017-1mdv2008.1
+ Revision: 99651
- import superiotool

