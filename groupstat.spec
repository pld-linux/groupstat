%include	/usr/lib/rpm/macros.perl
Summary:	GroupStat
Summary(pl.UTF-8):   GroupStat
Name:		groupstat
Version:	0.12.1
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.mgzi.net/comp/groupstat/download/%{name}_%{version}.tar.gz
# Source0-md5:	40f4a2f4bfa2b3f7ea0806ef4fa172c7
URL:		http://www.mgzi.net/comp/groupstat/
Requires:	perl-News-Scan
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GroupStat is an advanced statistic program for news groups.

%description -l pl.UTF-8
GroupStat jest zaawansowanym programem do prowadzenia statystyk news.

%prep
%setup -q -n %{name}_%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install getnews groupstat $RPM_BUILD_ROOT%{_bindir}
install groupstat.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc copyright* TODO README BUGS CHANGELOG
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
