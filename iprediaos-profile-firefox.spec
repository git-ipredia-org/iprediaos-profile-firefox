Name:		iprediaos-profile-firefox		
Version:	1
Release:	2%{?dist}
Summary:	Firefox profile for IprediaOS

Group:		System Environment/Base
License:	GPL
URL:		http://www.ipredia.org		
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:	noarch

#BuildRequires:	
Requires:	firefox

%description
Skeleton template for Firefox.

%prep
%setup -q


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Add dist to startpage URL (add it to ?os=)
# Remove the dot from dist
os=$(echo %{?dist} | sed "s:\.::g")
sed -i "s:?os=:?os=$os:g" $RPM_BUILD_ROOT%{_sysconfdir}/skel/.mozilla/firefox/a.default/user.js


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%{_sysconfdir}/skel/.mozilla/firefox/a.default/user.js
%{_sysconfdir}/skel/.mozilla/firefox/profiles.ini


%changelog
* Tue Apr 10 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 1-2
- Add os to startpage URL

* Tue Mar 27 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 1-1
- Initial package
