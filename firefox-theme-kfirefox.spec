%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define ver 16

%define _mozillaextpath %{firefox_mozillapath}/extensions

Summary: KDEFF theme for Mozilla Firefox
Name: firefox-theme-kfirefox
Version: 0.%{ver}
Release: %mkrel 18
License: GPLv3
Group: Networking/WWW
URL: http://ramonantonio.net/kde-firefox/
Source: http://kfirefox.googlecode.com/files/kfirefox0%{ver}.jar
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox = %{firefox_epoch}:%{firefox_version}
Obsoletes: mozilla-firefox-theme-kdeff <= 0.4
Provides: mozilla-firefox-theme-kdeff = %{version}-%{release}
Obsoletes: firefox-theme-kde4ff <= 0.16
Provides: firefox-theme-kde4ff = %{version}-%{release}
%if %mdkversion >= 201000
Obsoletes: firefox-theme-kdeff < 0.4-19mdv
%endif
BuildRequires: firefox-devel

%description
KFirefox is a KDE4-like theme using Oxygen icons for Mozilla Firefox 3.

%prep
# Unfortunately, we have to fix the packaging for this one. :(
%setup -T -q -c -n %{name}-%{version}
unzip -q %{SOURCE0}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mozillaextpath}

# this rdf contains 3 em:id sections.
hash="$(sed -n '/.*em:id="\(kde.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{_mozillaextpath}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%dir %firefox_mozillapath
%{_mozillaextpath}


%changelog
* Thu Jan 06 2011 Thierry Vignaud <tv@mandriva.org> 0.16-18mdv2011.0
+ Revision: 628972
- rebuild for new firefox

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 0.16-17mdv2011.0
+ Revision: 561842
- rebulid for ff 3.6.8

* Mon Jun 28 2010 Frederic Crozat <fcrozat@mandriva.com> 0.16-16mdv2010.1
+ Revision: 549362
- rebuild with FF 3.6.6

* Sun Apr 04 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.16-15mdv2010.1
+ Revision: 531265
- Rebuild

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 0.16-14mdv2010.1
+ Revision: 531122
- rebuild

* Wed Mar 24 2010 Funda Wang <fwang@mandriva.org> 0.16-13mdv2010.1
+ Revision: 526993
- rebuild

* Fri Jan 22 2010 Funda Wang <fwang@mandriva.org> 0.16-12mdv2010.1
+ Revision: 494806
- rebuild

* Thu Jan 21 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.16-11mdv2010.1
+ Revision: 494729
- Rebuild for new FF

* Sun Jan 10 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.16-10mdv2010.1
+ Revision: 488334
- Rebuild for new FF

* Wed Dec 30 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.16-9mdv2010.1
+ Revision: 484148
- Rebuild for FF 3.6

* Tue Nov 10 2009 Funda Wang <fwang@mandriva.org> 0.16-8mdv2010.1
+ Revision: 463987
- rebuild for new ff

* Fri Sep 18 2009 Funda Wang <fwang@mandriva.org> 0.16-7mdv2010.0
+ Revision: 444462
- real obsoletes old kde3 package

* Wed Sep 16 2009 Funda Wang <fwang@mandriva.org> 0.16-6mdv2010.0
+ Revision: 443396
- rebuild for new ff
- obsoletes old kde3 theme as kde3 -> kde4 migration

* Tue Aug 18 2009 Gustavo De Nardin <gustavodn@mandriva.com> 0.16-5mdv2010.0
+ Revision: 417678
- buildrequire firefox-devel, which provides the new macros for building extensions
- make use of the firefox package macros
- rebuild for firefox 3.5.2

* Tue Aug 11 2009 Raphaël Gertz <rapsys@mandriva.org> 0.16-4mdv2010.0
+ Revision: 415200
- Fix obsolete

* Sun Aug 09 2009 Raphaël Gertz <rapsys@mandriva.org> 0.16-3mdv2010.0
+ Revision: 412928
- Update to 3.5.2

* Thu Jul 30 2009 Raphaël Gertz <rapsys@mandriva.org> 0.16-2mdv2010.0
+ Revision: 404564
- Fix obsolete and provides
- New package for firefox-3.5.1
- Move to new package
- Fix for firefox-3.5.1
- New version for firefox 3.5.1
- Duplicate for 3.5 branch
- Allow firefox 3.0.11 and greater

  + Funda Wang <fwang@mandriva.org>
    - rebuild for new ff
    - rebuild for new ff
    - rebuild for new ff
    - rebuild for new ff
    - rebuild for new ff
    - rebuild for new ff
    - rebuild for new FF
    - New version 0.14

  + Gustavo De Nardin <gustavodn@mandriva.com>
    - rebuild for firefox 3.0.8

  + Tiago Salem <salem@mandriva.com.br>
    - version 3.0.2
    - fix sed in rdf file to get the right id.
    - bump release
    - obsoleting kde theme for firefox 2
    - import firefox-theme-kde4ff

  + Frederic Crozat <fcrozat@mandriva.com>
    - handle upgrade from 2008.1 better

