
%define plugin	pvrusb2
%define name	vdr-plugin-%plugin
%define version	0.1.1
%define rel	12

Summary:	VDR plugin: PVR USB2 analog TV support
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://vdr.unetz.com/download/pvrusb2/
Source:		http://vdr.unetz.com/download/pvrusb2/vdr-%plugin-%version.tar.bz2
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
This is a driver plugin for the Hauppauge PVR USB2 box using the
kernel driver provided by Mike Isely
(http://www.isely.net/pvrusb2.html).

%prep
%setup -q -n %plugin-%version

%vdr_plugin_params_begin %plugin
# increase verbosity
var=VERBOSE
param=-v
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


