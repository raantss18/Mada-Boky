#!/usr/bin/env bash
# ---------------------------------------------------------------------------
#  Boky Matematika — Terminale OSE
#
#    ./compiler.sh eleve    édition de l'élève      -> build/livre-t12ose-eleve.pdf
#    ./compiler.sh prof     édition du professeur   -> build/livre-t12ose-prof.pdf
#    ./compiler.sh les-deux les deux éditions
#    ./compiler.sh propre   efface les fichiers intermédiaires
# ---------------------------------------------------------------------------
set -euo pipefail
cd "$(dirname "$0")"
MAIN=livre-t12ose
BUILD=build

# L'arborescence de build doit refléter celle des sources (fichiers .aux)
mkdir -p "$BUILD"/{front,annexes,chapitres/{p1-analyse,p2-algebre,p3-geometrie,p4-donnees}}

LMK=(latexmk -xelatex -shell-escape -interaction=nonstopmode -outdir="$BUILD")

eleve() {
  "${LMK[@]}" "$MAIN.tex"
  cp "$BUILD/$MAIN.pdf" "$BUILD/$MAIN-eleve.pdf"
  echo "→ $BUILD/$MAIN-eleve.pdf"
}

prof() {
  "${LMK[@]}" -pretex='\def\editionprof{}' -usepretex \
              -jobname="$MAIN-prof" "$MAIN.tex"
  echo "→ $BUILD/$MAIN-prof.pdf"
}

case "${1:-eleve}" in
  eleve)     eleve ;;
  prof)      prof ;;
  les-deux)  eleve; prof ;;
  propre)    latexmk -c -outdir="$BUILD" ;;
  *)         echo "usage : $0 {eleve|prof|les-deux|propre}" ; exit 1 ;;
esac
