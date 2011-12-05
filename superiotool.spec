%define name superiotool
%define svnversion 20111206
%define version 0.%{svnversion} 

Summary:	Detect which Super I/O you have on your mainboard
Name:		%{name}
Version:	%{version}
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

