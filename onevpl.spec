%define major 2
%define libpackage %mklibname onevpl %{major}
%define devpackage %mklibname -d onevpl

%define oname oneVPL

Name:           onevpl
Version:        2022.1.5
Release:        1
Summary:        oneAPI Video Processing Library (oneVPL) dispatcher, tools, and examples
License:        MIT
Group:          Development
URL:            https://github.com/oneapi-src/oneVPL
Source0:        https://github.com/oneapi-src/oneVPL/archive/v%{version}/%{oname}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(wayland-client)

Requires:	%{libpackage} = %{EVRD}

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

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%cmake -DBUILD_PYTHON_BINDING=TRUE
%make_build

%install
%make_install -C build

%files
%license LICENSE 
%doc %{_datadir}/doc/oneVPL/
%{_bindir}/*

%files -n %{libpackage}
%{_libdir}/libvpl.so.%{major}*

%files -n %{devpackage}
%{_includedir}/vpl/
%{_libdir}/libvpl.so
%{_libdir}/oneVPL/libvpl_wayland.so
%{_libdir}/pkgconfig/vpl.pc
%{_libdir}/cmake/vpl/
%{_datadir}/oneVPL/
