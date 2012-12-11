
%define plugin	pvrusb2
%define name	vdr-plugin-%plugin
%define version	0.1.1
%define rel	17

Summary:	VDR plugin: PVR USB2 analog TV support
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL+
URL:		http://vdr.unetz.com/download/pvrusb2/
Source:		http://vdr.unetz.com/download/pvrusb2/vdr-%plugin-%version.tar.bz2
Patch0:		pvrusb2-0.1.1-i18n-1.6.patch
Patch1:		pvrusb2-0.1.1-vdr-1.6.patch
Patch2:		pvrusb2-duplicate-parameter.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This is a driver plugin for the Hauppauge PVR USB2 box using the
kernel driver provided by Mike Isely
(http://www.isely.net/pvrusb2.html).

%prep
%setup -q -n %plugin-%version
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




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.1-17mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.1.1-16mdv2009.1
+ Revision: 359751
- fix duplicate parameter names in function declaration
  (duplicate-parameter.patch)
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.1.1-15mdv2009.0
+ Revision: 197968
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.1.1-14mdv2009.0
+ Revision: 197713
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- adapt for api changes of VDR 1.6 (P1)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1.1-13mdv2008.1
+ Revision: 145192
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.1.1-12mdv2008.1
+ Revision: 103187
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.1.1-11mdv2008.0
+ Revision: 50036
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.1.1-10mdv2008.0
+ Revision: 42123
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.1.1-9mdv2008.0
+ Revision: 22778
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1.1-8mdv2007.0
+ Revision: 90965
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.1.1-7mdv2007.1
+ Revision: 74075
- rebuild for new vdr
- Import vdr-plugin-pvrusb2

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.1-6mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.1.1-5mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.1-4mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.1.1-3mdv2007.0
- rebuild for new vdr

* Thu Jul 20 2006 Anssi Hannula <anssi@mandriva.org> 0.1.1-2mdv2007.0
- fix url

* Thu Jul 20 2006 Anssi Hannula <anssi@mandriva.org> 0.1.1-1mdv2007.0
- initial Mandriva release

