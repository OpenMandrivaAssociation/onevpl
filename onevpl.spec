%define major 2
%define libpackage %mklibname onevpl %{major}
%define devpackage %mklibname -d onevpl

Name:           onevpl
Version:        2021.6.0
Release:        1
Summary:        oneAPI Video Processing Library (oneVPL) dispatcher, tools, and examples
License:        MIT
Group:          Development
URL:            https://github.com/oneapi-src/oneVPL
Source0:        https://github.com/oneapi-src/oneVPL/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wayland-client)

%description
The oneAPI Video Processing Library (oneVPL) provides a single video processing
API for encode, decode, and video processing that works across a wide range of
accelerators.

%package -n %{libpackage}
Summary:        oneAPI Video Processing Library (oneVPL) dispatcher
Group:          System/Libraries

%description -n %{libpackage}
The oneAPI Video Processing Library (oneVPL) provides a single video processing
API for encode, decode, and video processing that works across a wide range of
accelerators.

%package -n %{devpackage}
Summary:        Development files for oneAPI Video Processing Library (oneVPL) dispatcher
Group:          Development/Languages/C and C++
Requires:	%{libpackage} = %{EVRD}

%description -n %{devpackage}
This package contains the development headers and pkgconfig files for
the oneAPI Video Processing Library (oneVPL) dispatcher

%package samples
Summary:        Examples for the oneAPI Video Processing Library (oneVPL) dispatcher
Group:          Development/Languages/C and C++

%description samples
This package contains example applications for the oneAPI Video Processing Library (oneVPL) dispatcher.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake
%make_buil

%install
%make_install -C build

%files -n %{libpackage}
%license LICENSE 
%{_libdir}/libvpl.so.%{major}*

%files -n %{devpackage}
%doc 
%{_includedir}/vpl/
%{_libdir}/libvpl.so
%{_libdir}/pkgconfig/vpl.pc
%{_libdir}/cmake/vpl/
%{_datadir}/oneVPL/

%files samples
%{_bindir}/*
