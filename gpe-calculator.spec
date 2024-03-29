Summary:	GPE calculator
Summary(pl.UTF-8):	Kalkulator GPE
Name:		gpe-calculator
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.gz
# Source0-md5:	6dc5eed9b200a45cf007f7a7ed4c2d23
URL:		http://gpe.linuxtogo.org/
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	pkgconfig
Requires:	gpe-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPE calculator, for embedded devices.

%description -l pl.UTF-8
Kalkulator GPE dla urządzeń wbudowanych.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall \$(GTKCFLAGS)" \
	LDFLAGS="%{rpmldflags} \$(GTKLDFLAGS)" \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
