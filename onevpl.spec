%define major 2
%define oldlibpackage %mklibname onevpl 2
%define libpackage %mklibname onevpl
%define devpackage %mklibname -d onevpl

%define oname oneVPL

Name:           onevpl
Version:        2.10.1
Release:        1
Summary:        oneAPI Video Processing Library (oneVPL) dispatcher, tools, and examples
License:        MIT
Group:          Development
URL:            https://github.com/oneapi-src/oneVPL
Source0:        https://github.com/intel/libvpl/archive/refs/tags/v%{version}/libvpl-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)

BuildRequires:  python%{pyver}dist(pybind11)

Requires:	%{libpackage} = %{EVRD}

%description
The oneAPI Video Processing Library (oneVPL) provides a single video processing
API for encode, decode, and video processing that works across a wide range of
accelerators.

%package -n %{libpackage}
Summary:        oneAPI Video Processing Library (oneVPL) dispatcher
Group:          System/Libraries
%rename %{oldlibpackage}

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

#package -n python-%{name}
#Summary:    Python interface to %{name}

#description -n python-%{name}
#This package contains python interfaces to %{name}.

%prep
%autosetup -p1 -n libvpl-%{version}

%build
%cmake  \
        -DBUILD_PYTHON_BINDING:BOOL=ON \
        -DPYTHON_INSTALL_DIR:STRING=%{python_sitearch}
%make_build

%install
%make_install -C build

%files
%license LICENSE 
%doc %{_datadir}/vpl/licensing/
%{_bindir}/*
%{_prefix}/etc/modulefiles/vpl
%{_prefix}/etc/vpl/vars.sh
%{_datadir}/vpl/examples/

%files -n %{libpackage}
%{_libdir}/libvpl.so.%{major}*

%files -n %{devpackage}
%{_includedir}/vpl/
%{_libdir}/libvpl.so
%{_libdir}/vpl/libvpl_wayland.so
%{_libdir}/pkgconfig/vpl.pc
%{_libdir}/cmake/vpl/

#files -n python-%{name}
#{python_sitearch}/pyvpl.cpython-*
