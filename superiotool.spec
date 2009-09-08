%define name superiotool
%define svnversion 20071017
%define version 0.%{svnversion} 
%define release %mkrel 5

Summary: Detect which Super I/O you have on your mainboard
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{svnversion}.tar.gz
License: GPL
Group: System/Kernel and hardware
Url: http://linuxbios.org/index.php/Superiotool
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Superiotool is a GPL'd user-space helper tool for LinuxBIOS development 
purposes (but may also be useful for other things).
It allows you to detect which Super I/O you have on your mainboard,
and it can provide detailed information about the register contents
of the Super I/O.

%prep
%setup -q -n %name

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
%makeinstall PREFIX=$RPM_BUILD_ROOT/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/superiotool
%{_mandir}/man8/superiotool*

