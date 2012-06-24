Summary:	A small accounting package
Summary(pl):	Prosty pakiet do rozliczania
Name:		tinyaccounting
Version:	1.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://tinyaccounting.org/download/sources/%{name}-%{version}.tgz
# Source0-md5:	9b03ed3cb71be00a9a8020a1e3ffea81
URL:		http://tinyaccounting.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tiny Accounting allows you to follow the performance of responsibility
centers and to allocate expenses, generates reports of all accounting
data in the general ledger, takes care of journal book-keeping and
allows financial reporting, deals with cash-flow. Analytical and
reporting tools are also included and address company or group
accounts.

%description -l pl
Tiny Accounting pozwala na �ledzenie wydajno�ci o�rodk�w
odpowiedzialno�ci, przydzielanie wydatk�w, generowanie raport�w z
wszystkich danych rozliczeniowych w ksi�dze g��wnej, opiekuje si�
dzienn� ksi�gowo�ci� i pozwala na tworzenie raport�w finansowych,
zajmuje si� przep�ywem got�wki. Do��czone s� tak�e narz�dzia
analityczne i raportuj�ce przeznaczone dla rachunk�w firmowych i
grupowych.

%prep
%setup -q -n tinyaccount-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
