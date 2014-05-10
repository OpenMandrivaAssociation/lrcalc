Name:		lrcalc
Group:		Sciences/Mathematics
Version:	1.1.6
Release:	3.beta
License:	GPLv2+
Summary:	Littlewood-Richardson Calculator
URL:		http://math.rutgers.edu/~asbuch/lrcalc
Source0:	http://math.rutgers.edu/~asbuch/lrcalc/%{name}-sage-%{version}.tar.gz
Source1:	lrcalc.module.in
Source2:	%{name}.rpmlintrc

%description
The "Littlewood-Richardson Calculator" is a package of C and Maple programs
for computing Littlewood-Richardson coefficients. The C programs form the
engine of the package, providing fast calculation of single LR coefficients,
products of Schur functions, and skew Schur functions. The Maple code mainly
gives an interface which makes it possible to use the C programs from Maple.
This interface uses the same notation as the SF package of John Stembridge,
to make it easier to use both packages at the same time.

%package	devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-sage-%{version}

%build
%configure --bindir=%{_libdir}/%{name} --enable-shared --disable-static
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm %{buildroot}%{_libdir}/*.la

mkdir -p %{buildroot}%{_datadir}/Modules/modulefiles
sed 's#@BINDIR@#'%{_libdir}/%{name}'#g;' < %{SOURCE1} > \
    %{buildroot}%{_datadir}/Modules/modulefiles/%{name}-%{_arch} 

%check
make check

%files
%doc AUTHORS
%doc ChangeLog
%doc COPYING
%doc LICENSE
%doc README
%{_libdir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_datadir}/Modules/modulefiles/%{name}-%{_arch}

%files		devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
