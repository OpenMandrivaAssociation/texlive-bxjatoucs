Name:		texlive-bxjatoucs
Version:	52509
Release:	1
Summary:	Convert Japanese character code to Unicode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bxjatoucs
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjatoucs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjatoucs.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is meant for macro/package developers: It provides
function-like (fully-expandable) macros that convert a
character code value in one of several Japanese encodings to a
Unicode value. Supported source encodings are: ISO-2022-JP
(jis), EUC-JP (euc), Shift_JIS (sjis), and the Adobe-Japan1
glyph set.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bxjatoucs
%{_texmfdistdir}/fonts/tfm/public/bxjatoucs
%doc %{_texmfdistdir}/doc/latex/bxjatoucs

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
