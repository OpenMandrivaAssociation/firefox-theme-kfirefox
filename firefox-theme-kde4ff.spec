%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define ff_epoch 0
%define ff_ver 3.5.1
%define ver 16

%define _mozillapath %{_libdir}/firefox-%{ff_ver}
%define _mozillaextpath %{_mozillapath}/extensions

Summary: KDEFF theme for Mozilla Firefox
Name: firefox-theme-kfirefox
Version: 0.%{ver}
Release: %mkrel 1
License: GPLv3
Group: Networking/WWW
URL: http://ramonantonio.net/kde-firefox/
Source: http://kfirefox.googlecode.com/files/kfirefox0%{ver}.jar
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox = %{ff_epoch}:%{ff_ver}
Obsoletes: mozilla-firefox-theme-kdeff <= 0.14
Provides: mozilla-firefox-theme-kdeff = %{version}-%{release}

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
%dir %_mozillapath
%{_mozillaextpath}
