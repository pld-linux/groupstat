Summary:	GroupStat
Summary(pl):	GroupStat
Name:		groupstat
Version:	0.12.1
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	http://www.locl.net/homes/alexdw/comp/groupstat/download/%{name}_%{version}.tar.gz
Url:		http://www.locl.net/homes/alexdw/
Requires:	perl-News-Scan
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GroupStat is an advenced statistic program for news groups

%description -l pl
GroupStat jest zaawansowanym programem do prowadzenia statystyk news.

%prep
%setup -q -n %{name}_%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install getnews groupstat $RPM_BUILD_ROOT%{_bindir}
install groupstat.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf copyright* TODO README BUGS CHANGELOG

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
