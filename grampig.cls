\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{grampig}

\LoadClass[10pt,utf8,varwidth=10cm,border=0.5cm]{standalone}

\RequirePackage{zxjatype}
\RequirePackage{enumitem}
\RequirePackage{fontspec}
\RequirePackage[x11names]{xcolor}
\RequirePackage{ruby}
\RequirePackage{microtype}
\RequirePackage{array}
\RequirePackage{booktabs}
\RequirePackage{makecell}
\RequirePackage{tabularx}
\RequirePackage{pbox}
\RequirePackage{xargs}

\definecolor{navy}{HTML}{001F3F}
\definecolor{blue}{HTML}{0074D9}
\definecolor{aqua}{HTML}{7FDBFF}
\definecolor{teal}{HTML}{39CCCC}
\definecolor{olive}{HTML}{3D9970}
\definecolor{green}{HTML}{2ECC40}
\definecolor{lime}{HTML}{01FF70}
\definecolor{yellow}{HTML}{FFDC00}
\definecolor{orange}{HTML}{FF851B}
\definecolor{red}{HTML}{FF4136}
\definecolor{fuchsia}{HTML}{F012BE}
\definecolor{purple}{HTML}{B10DC9}
\definecolor{maroon}{HTML}{85144B}
\definecolor{white}{HTML}{FFFFFF}
\definecolor{silver}{HTML}{DDDDDD}
\definecolor{gray}{HTML}{AAAAAA}
\definecolor{black}{HTML}{111111}

\newcommand{\backgroundcolor}{SeaGreen4}
\newcommand{\foregroundcolor}{black}
\newcommand{\accentcolor}{gray}

\newcommand{\watermark}{\textsc{cursed}}


\DeclareOption{basic}{
	\renewcommand{\backgroundcolor}{yellow}
	\renewcommand{\foregroundcolor}{black}
	\renewcommand{\accentcolor}{maroon}
}
\DeclareOption{intermediate}{
	\renewcommand{\backgroundcolor}{navy}
	\renewcommand{\foregroundcolor}{aqua}
	\renewcommand{\accentcolor}{yellow}
}
\DeclareOption{advanced}{
	\renewcommand{\backgroundcolor}{maroon}
	\renewcommand{\foregroundcolor}{yellow}
	\renewcommand{\accentcolor}{orange}
}
\DeclareOption{pig}{
	\renewcommand{\backgroundcolor}{maroon}
	\renewcommand{\foregroundcolor}{pink}
	\renewcommand{\accentcolor}{lime}
}
\DeclareOption{ocha}{
	\renewcommand{\backgroundcolor}{silver}
	\renewcommand{\foregroundcolor}{maroon}
	\renewcommand{\accentcolor}{orange}
}
\DeclareOption{ocha-dark}{
	\renewcommand{\backgroundcolor}{black}
	\renewcommand{\foregroundcolor}{pink}
	\renewcommand{\accentcolor}{red}
}
\DeclareOption{bless}{
	\renewcommand{\watermark}{}
}
\ProcessOptions\relax

\def\@title{ぶんぽう}
\renewcommand*{\title}[1]{
	\def\@title{#1}
}

\def\@pos{pos}
\newcommand*{\pos}[1]{
	\def\@pos{#1}
}

\newcommand*{\e}[1]{{\color{\accentcolor}#1}}
\newcommand*{\br}{\\[0.4em]}
\newcommand*{\bh}{\\[-0.2em]}
\newcommand*{\p}[1]{\mbox{#1}\CJKglue}
\newcommand{\f}[2]{\ruby{#1}{\sffamily\protect\smash{#2}}\CJKglue}

\usepackage{xstring}
\newcommand{\squeeze}{\kern -0.25em}
\newcommand{\furiganafix}[1]{{%
		\StrSubstitute{#1}{・}{@・@}[\x]%
		\StrSubstitute{\x}{ゃ}{@ゃ@}[\x]%
		\StrSubstitute{\x}{ゅ}{@ゅ@}[\x]%
		\StrSubstitute{\x}{ょ}{@ょ@}[\x]%
		\StrSubstitute{\x}{ぁ}{@ぁ@}[\x]%
		\StrSubstitute{\x}{ぃ}{@ぃ@}[\x]%
		\StrSubstitute{\x}{ぅ}{@ぅ@}[\x]%
		\StrSubstitute{\x}{ぇ}{@ぇ@}[\x]%
		\StrSubstitute{\x}{ぉ}{@ぉ@}[\x]%
		\StrSubstitute{\x}{っ}{@っ@}[\x]%
		\StrSubstitute{\x}{ャ}{@ャ@}[\x]%
		\StrSubstitute{\x}{ュ}{@ュ@}[\x]%
		\StrSubstitute{\x}{ョ}{@ョ@}[\x]%
		\StrSubstitute{\x}{ァ}{@ァ@}[\x]%
		\StrSubstitute{\x}{ィ}{@ィ@}[\x]%
		\StrSubstitute{\x}{ゥ}{@ゥ@}[\x]%
		\StrSubstitute{\x}{ェ}{@ェ@}[\x]%
		\StrSubstitute{\x}{ォ}{@ォ@}[\x]%
		\StrSubstitute{\x}{ッ}{@ッ@}[\x]%
		\StrSubstitute{\x}{@@}{@}[\x]%
		\StrSubstitute{\x}{@}{\squeeze}[\x]%
		\x}}

\newcommand{\g}{\furiganafix}

\renewcommand{\rubysep}{-0.1em}
\renewcommand{\rubysize}{0.56}

\pagecolor{\backgroundcolor}
\color{\foregroundcolor}

\setlength{\tabcolsep}{0.5ex}

\setCJKmainfont[Scale=MatchUppercase, BoldFont={*-SemiBold}, ItalicFont=*]{./_fonts/SourceHanSerifJP.otf}
\setCJKsansfont[Scale=MatchUppercase, BoldFont={*-Bold}, ItalicFont=*]{./_fonts/SourceHanSansJP.otf}
\setmainfont[BoldFont={*-Semibold}, Numbers={OldStyle}]{./_fonts/SourceSerifPro.otf}

\setlist{leftmargin=0em,itemsep=0.5em,parsep=0em,partopsep=0em,topsep=0em}
\setlength{\parindent}{0pt}
\newlength{\width}
\setlength{\width}{10cm}
\setlength{\fboxsep}{1em}
\setlength{\parskip}{0em}

\renewcommand{\maketitle}{
	\begin{tabular}{@{}p{0.333\width}@{}p{0.333\width}@{}p{0.333\width}@{}}
		\makecell[lt]{\e{\large\@title}} & \makecell[ct]{\textsc{\e\watermark}} & \makecell[rt]{\@pos}
	\end{tabular}\br
}
