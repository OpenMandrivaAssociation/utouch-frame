%define major 1
%define libname %mklibname  %{name} %{major}
%define develname   %mklibname  %{name} -d

Name:           utouch-frame
Version:        1.1.4
Release:        1
License:        GPL-3.0
Summary:        Touch frame library
Url:            http://launchpad.net/utouch-frame
Group:          Graphical desktop/Other 
Source:         %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(utouch-evemu)

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
%setup -q
 
%build
%configure \
  --disable-static
%make
 
%install
%makeinstall_std
# Remove unwanted files
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print
 
 
%files
%defattr(-,root,root)
%doc ChangeLog README COPYING
%{_bindir}/utouch-frame-test-mtdev
 
%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*
 
%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/utouch/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
 
