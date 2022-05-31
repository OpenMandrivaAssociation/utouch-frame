%define major 1
%define libname %mklibname  %{name} %{major}
%define develname   %mklibname  %{name} -d
%define oname frame

Name:           utouch-frame
Version:        2.5.0
Release:        1
License:        GPL-3.0
Summary:        Touch frame library
Url:            http://launchpad.net/frame
Group:          Graphical desktop/Other 
Source:         https://launchpad.net/frame/trunk/v%{version}/+download/frame-%{version}.tar.xz
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(evemu)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xorg-server)

Requires:	evemu

Requires:   %{libname} = %{version}-%{release}
 
%description
This package provides the tree that handles the buildup and 
synchronization
of a set of simultaneous touches.
 
%package -n %{libname}
Summary:        Touch frame library
Group:          System/Libraries
 
%description -n %{libname}
This package provides the tree that handles the buildup and 
synchronization
of a set of simultaneous touches.
 
%package -n %{develname}
Summary:        Touch frame library development files
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
 
%description -n %{develname}
This package provides the tree that handles the buildup and 
synchronization
of a set of simultaneous touches.
 
This package includes the development files for utouch-evemu.
 
%prep
%autosetup -n %{oname}-%{version}
 
%build
autoreconf -fi
%configure \
  --disable-static
%make_build
 
%install
%make_install
 
%files
%doc ChangeLog README COPYING
%{_bindir}/utouch-frame-test-mtdev
 
%files -n %{libname}
%{_libdir}/*.so.%{major}*
 
%files -n %{develname}
%{_includedir}/utouch/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
 
