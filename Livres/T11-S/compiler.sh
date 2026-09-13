#!/usr/bin/env bash
# ---------------------------------------------------------------------------
#  compiler.sh — pilote de compilation du livre Première S
#
#    ./compiler.sh eleve      édition de l'élève       -> livre-t11s-eleve.pdf
#    ./compiler.sh prof       édition du professeur    -> livre-t11s-prof.pdf
#    ./compiler.sh les-deux   les deux éditions
#    ./compiler.sh propre     efface le dossier build
# ---------------------------------------------------------------------------
set -euo pipefail
cd "$(dirname "$0")"

RACINE=livre-t11s
SOUS_DOSSIERS=(
  front
  chapitres/p1-analyse chapitres/p2-algebre
  chapitres/p3-geometrie chapitres/p4-donnees
  annexes
)

prepare_build () {
  mkdir -p build
  for d in "${SOUS_DOSSIERS[@]}"; do mkdir -p "build/$d"; done
}

compile_eleve () {
  prepare_build
  latexmk -xelatex -interaction=nonstopmode "$RACINE.tex"
  cp "build/$RACINE.pdf" "$RACINE-eleve.pdf"
  echo "→ $RACINE-eleve.pdf"
}

compile_prof () {
  prepare_build
  latexmk -xelatex -interaction=nonstopmode \
    -jobname="$RACINE-prof" \
    "\def\editionprof{}\input{$RACINE.tex}"
  cp "build/$RACINE-prof.pdf" "$RACINE-prof.pdf"
  echo "→ $RACINE-prof.pdf"
}

case "${1:-eleve}" in
  eleve)    compile_eleve ;;
  prof)     compile_prof ;;
  les-deux) compile_eleve; compile_prof ;;
  propre)   rm -rf build; echo "build/ effacé" ;;
  *) echo "Usage : $0 {eleve|prof|les-deux|propre}" >&2; exit 1 ;;
esac
