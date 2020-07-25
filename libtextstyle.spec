#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	GNU libtextstyle - Text styling library
Summary(pl.UTF-8):	GNU libtextstyle - biblioteka do obsługi stylu tekstu
Name:		libtextstyle
Version:	0.20.5
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://alpha.gnu.org/gnu/gettext/%{name}-%{version}.tar.gz
# Source0-md5:	30be56f2428ff2add624caf3a1700d3e
Patch0:		%{name}-libdir.patch
URL:		https://www.gnu.org/software/gettext/libtextstyle/manual/
BuildRequires:	make >= 3.79.1
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides an easy way to add styling to programs that
produce output to a console or terminal emulator window.

libtextstyle is for you if your application produces text that is more
readable when it is accompanied with styling information, such as
color, font attributes (weight, posture), or underlining.

%description -l pl.UTF-8
Ta biblioteka zapewnia łatwy sposób dodawania styli do programów
produkujących wyjście na konsoli lub w oknie emulatora terminala.

libtextstyle ma zastosowanie tam, gdzie aplikacja produkuje tekst,
który jest bardziej czytelny, jeśli jest wzbogacony o informacje o
stylu, takie jak kolor, atrybuty czcionek (grubość, nachylenie) lub
podkreślenie.

%package devel
Summary:	Header files for libtextstyle library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libtextstyle
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ncurses-devel

%description devel
Header files for libtextstyle library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libtextstyle.

%package static
Summary:	Static libtextstyle library
Summary(pl.UTF-8):	Statyczna biblioteka libtextstyle
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libtextstyle library.

%description static -l pl.UTF-8
Statyczna biblioteka libtextstyle.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-rpath \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# duplicates info
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libtextstyle

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libtextstyle.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtextstyle.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtextstyle.so
%{_libdir}/libtextstyle.la
%{_includedir}/textstyle.h
%{_includedir}/textstyle
%{_infodir}/libtextstyle.info*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libtextstyle.a
%endif
