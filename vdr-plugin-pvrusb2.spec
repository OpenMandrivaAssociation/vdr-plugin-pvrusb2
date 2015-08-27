%define plugin	pvrusb2

Summary:	VDR plugin: PVR USB2 analog TV support
Name:		vdr-plugin-%plugin
Version:	0.1.1
Release:	19
Group:		Video
License:	GPL+
URL:		http://vdr.unetz.com/download/pvrusb2/
Source:		http://vdr.unetz.com/download/pvrusb2/vdr-%plugin-%{version}.tgz
Patch0:		pvrusb2-0.1.1-i18n-1.6.patch
Patch1:		pvrusb2-0.1.1-vdr-1.6.patch
Patch2:		pvrusb2-duplicate-parameter.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This is a driver plugin for the Hauppauge PVR USB2 box using the
kernel driver provided by Mike Isely
(http://www.isely.net/pvrusb2.html).

%prep
%setup -q -n %plugin-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# increase verbosity
var=VERBOSE
param=-v
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README HISTORY
