Name:		texlive-gitlog
Version:	38932
Release:	2
Summary:	Typesetting git changelogs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gitlog
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gitlog.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gitlog.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows git change log history to be incorporated
into LaTeX documents; the log data is obtained from the git
distributed version control system. The current release
(0.0.beta) is a proof-of-concept release to allow users an
early evaluation and to attract ideas and support. Requests and
suggestions, as well as code contributions are welcome.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/gitlog
%doc %{_texmfdistdir}/doc/latex/gitlog

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
