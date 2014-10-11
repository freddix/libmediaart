Summary:	Media art extraction and cache management library
Name:		libmediaart
Version:	0.6.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libmediaart/0.6/%{name}-%{version}.tar.xz
# Source0-md5:	8bd508886c47397925771e2717c80d52
URL:		https://github.com/curlybeast/libmediaart
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	vala
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Media art extraction and cache management library.

%package devel
Summary:	Header files for libmediaart library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libmediaart library.

%package apidocs
Summary:	libmediaart API documentation
Group:		Documentation

%description apidocs
API documentation for libmediaart library.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %ghost %{_libdir}/libmediaart-1.0.so.0
%attr(755,root,root) %{_libdir}/libmediaart-1.0.so.*.*.*
%{_libdir}/girepository-1.0/MediaArt-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmediaart-1.0.so
%{_datadir}/gir-1.0/MediaArt-1.0.gir
%{_datadir}/vala/vapi/libmediaart-1.0.vapi
%{_includedir}/libmediaart-1.0
%{_pkgconfigdir}/libmediaart-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libmediaart

