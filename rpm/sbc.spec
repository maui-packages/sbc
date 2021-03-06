# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       sbc

# >> macros
# << macros

Summary:    SBC library
Version:    1.2
Release:    1
Group:      System/Libraries
License:    GPLv2+
URL:        http://www.kernel.org/pub/linux/bluetooth/
Source0:    %{name}-%{version}.tar.xz
Source100:  sbc.yaml
Requires:   fdupes
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(sndfile) >= 1.0.20
BuildRequires:  fdupes

%description
Bluetooth low-complexity, subband codec (SBC) library.


%package tools
Summary:    SBC tools
Group:      System/Base
Requires:   %{name} = %{version}-%{release}

%description tools
%{summary}.

%package devel
Summary:    SBC development headers and libraries
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Description: %{summary}

%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%reconfigure --disable-static
make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%fdupes  %{buildroot}/%{_datadir}
%fdupes  %{buildroot}/%{_includedir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libsbc.so.*
# >> files
# << files

%files tools
%defattr(-,root,root,-)
%{_bindir}/sbcdec
%{_bindir}/sbcenc
%{_bindir}/sbcinfo
# >> files tools
# << files tools

%files devel
%defattr(-,root,root,-)
%{_libdir}/libsbc.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/sbc/*.h
# >> files devel
# << files devel
