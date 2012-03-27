Name:		iprediaos-profile-firefox		
Version:	1
Release:	1%{?dist}
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


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc



%changelog

