%global tl_name gitlog
%global tl_revision 38932

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0.beta
Release:	%{tl_revision}.1
Summary:	Typesetting git changelogs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gitlog
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gitlog.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gitlog.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows git change log history to be incorporated into LaTeX
documents; the log data is obtained from the git distributed version
control system. The current release (0.0.beta) is a proof-of-concept
release to allow users an early evaluation and to attract ideas and
support. Requests and suggestions, as well as code contributions are
welcome.

