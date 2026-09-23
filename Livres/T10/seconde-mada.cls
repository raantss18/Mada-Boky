\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{seconde-mada}[2026/09/19 v1.0 Manuel T10 Madagascar]

\LoadClass[12pt,a4paper,openright]{book}

\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
% A minimal TeX distribution may not ship
% french.ldf. Typography therefore remains self-contained and does not depend
% on Babel; explicit French spacing is handled in the source.
\RequirePackage{mathpazo}
\RequirePackage{microtype}
\RequirePackage[a4paper,top=2.4cm,bottom=2.7cm,inner=2.7cm,outer=2.1cm,
  marginparwidth=1.45cm,marginparsep=0.35cm,headheight=15pt]{geometry}
\RequirePackage{amsmath,amssymb,mathtools}
\RequirePackage{tikz,pgfplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows.meta,calc,patterns,shapes.geometric,
  decorations.pathmorphing,decorations.pathreplacing,positioning,
  intersections,backgrounds}
\RequirePackage{xcolor}
\definecolor{BN}{RGB}{18,42,86}
\definecolor{OR}{RGB}{195,155,52}
\definecolor{TQ}{RGB}{0,122,140}
\definecolor{VE}{RGB}{50,112,65}
\definecolor{BO}{RGB}{136,22,42}
\definecolor{OD}{RGB}{212,115,36}
\definecolor{VI}{RGB}{96,54,136}
\definecolor{GC}{RGB}{248,248,244}
\definecolor{GM}{RGB}{165,165,160}

\RequirePackage{tcolorbox}
\tcbuselibrary{skins,breakable,theorems}
\RequirePackage{fancyhdr}
\RequirePackage[nobottomtitles*]{titlesec}
\renewcommand{\bottomtitlespace}{.12\textheight}
\RequirePackage{enumitem,multicol}
\RequirePackage{booktabs,array,tabularx,multirow,longtable}
\RequirePackage{eurosym}
\RequirePackage{wrapfig,graphicx,float}
\RequirePackage{setspace,emptypage,comment,needspace,xspace}
\RequirePackage{listings}
\RequirePackage{eso-pic}
\RequirePackage{makeidx}
\RequirePackage{colortbl}
\RequirePackage{etoolbox}
\RequirePackage[colorlinks,linkcolor=BN,urlcolor=OR,citecolor=TQ]{hyperref}
\hypersetup{
  pdftitle={Mathématiques - Classe de Seconde (T10)},
  pdfsubject={Manuel conforme au PE et au RAPE T10 Madagascar 2026},
  pdfkeywords={mathématiques, Seconde, T10, Madagascar}
}
\makeindex

\newcommand{\og}{\guillemotleft\,}
\newcommand{\fg}{\,\guillemotright}
\newcommand{\pgcd}{\operatorname{pgcd}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\D}{\mathbb{D}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\vv}[1]{\overrightarrow{#1}}
\newcommand{\abs}[1]{\left|#1\right|}
\newcommand{\norme}[1]{\left\|#1\right\|}
\newcommand{\vrai}{\textbf{V}}
\newcommand{\faux}{\textbf{F}}
\newcommand{\Vrai}{\textbf{Vrai}}
\newcommand{\Faux}{\textbf{Faux}}

\newif\ifmdgteacher
\providecommand{\MdgVersion}{student}
\ifdefstring{\MdgVersion}{teacher}{\mdgteachertrue}{\mdgteacherfalse}
\ifmdgteacher
  \newcommand{\MdgEditionLabel}{Version professeur}
\else
  \newcommand{\MdgEditionLabel}{Version élève}
\fi

\setlist[itemize,1]{label={\color{OR!70}$\triangleright$},leftmargin=*}
\setlist[enumerate,1]{leftmargin=*,font=\color{BN}\bfseries}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.3em plus 0.1em minus 0.05em}
% Give prose and inline mathematics a little controlled flexibility before
% TeX resorts to protruding into the margin.
\setlength{\emergencystretch}{2em}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE]{\small\textcolor{BN}{\nouppercase{\leftmark}}}
\fancyhead[RO]{\small\textcolor{BN}{\nouppercase{\rightmark}}}
\fancyfoot[LE,RO]{\textcolor{GM}{\small\thepage}}
\fancyfoot[LO,RE]{\textcolor{GM}{\small T10 -- \MdgEditionLabel}}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\headrule}{\color{OR!60}\hrule width\textwidth}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\textcolor{GM}{\small\thepage}}%
  \renewcommand{\headrulewidth}{0pt}}

\titleformat{\part}[display]{\normalfont\centering}
  {\vspace*{2cm}{\color{OR!60}\rule{3cm}{0.5pt}}\enspace
   {\color{OR}\small\scshape\bfseries Partie \thepart}\enspace
   {\color{OR!60}\rule{3cm}{0.5pt}}}
  {10pt}{\color{BN}\centering\Huge\bfseries}
  [\vspace{8pt}{\color{BN!20}\rule{6cm}{0.4pt}}\vspace{10pt}]
\titleformat{\chapter}[display]{\normalfont\raggedright}
  {\hfill{\color{BN!12}\fontsize{88}{88}\selectfont\bfseries\thechapter}}
  {-24pt}{\color{BN}\huge\bfseries}
  [\vspace{2pt}{\color{OR}\rule{\textwidth}{1.2pt}}\vspace{4pt}]
\titlespacing{\chapter}{0pt}{20pt}{28pt}
\titleformat{\section}{\color{BN}\large\bfseries}
  {\textcolor{OR}{\thesection}}{0.7em}{}
  [{\vspace{-6pt}\color{BN!15}\rule{\textwidth}{0.4pt}}]
\titleformat{\subsection}{\color{BN!75}\normalsize\bfseries}
  {\thesubsection}{0.5em}{}

\endinput
