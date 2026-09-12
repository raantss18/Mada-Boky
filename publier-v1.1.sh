#!/usr/bin/env bash
# ---------------------------------------------------------------------------
#  Mada-Boky — publication de la version 1.1
#
#  À lancer depuis la racine du dépôt :
#      chmod +x publier-v1.1.sh && ./publier-v1.1.sh
#
#  Le script fait trois choses, dans cet ordre :
#    1. retire du dépôt les fichiers devenus orphelins (ils restent dans
#       l'historique Git, rien n'est perdu) ;
#    2. enregistre et pousse le commit de la version 1.1, avec son tag ;
#    3. crée la release GitHub et y joint les six PDF.
#
#  Il s'arrête à la première erreur et demande confirmation avant de pousser.
# ---------------------------------------------------------------------------
set -euo pipefail
cd "$(dirname "$0")"

TAG="v1.1"
TITRE="Mada-Boky v1.1 — Terminale S revue, OSE corrigée, L restructurée"

# --- 1. Ménage -------------------------------------------------------------
# Fichiers que plus aucun livre n'inclut : anciens noms de chapitres de la
# série S avant la renumérotation de la partie Algèbre, chapitres de suites
# et de données retirés de la série L, chapitres financiers passés en annexe
# dans la série OSE.
ORPHELINS=(
  "Livres/T12-S/chapitres/p2-algebre/ch08-arithmetique.tex"
  "Livres/T12-S/chapitres/p2-algebre/ch09-numeration.tex"
  "Livres/T12-S/chapitres/p2-algebre/ch10-calcul-matriciel.tex"
  "Livres/T12-S/chapitres/p2-algebre/ch11-suites.tex"
  "Livres/T12-S/front/progression.tex"
  "Livres/T12-S/annexes/lexique.tex"
  "Livres/T12-L/chapitres/p3-suites"
  "Livres/T12-L/chapitres/p4-donnees"
  "Livres/T12-OSE/chapitres/p5-financier"
)

echo "→ Retrait des fichiers orphelins"
for f in "${ORPHELINS[@]}"; do
  if git ls-files --error-unmatch "$f" >/dev/null 2>&1 || [ -e "$f" ]; then
    git rm -r --quiet --ignore-unmatch "$f" && echo "   retiré : $f"
  fi
done

# Anciens dépôts Git locaux et dossiers de compilation, hors du dépôt
rm -rf Livres/T12-S/.git-historique-solo
git rm -r --quiet --cached --ignore-unmatch Livres/*/build >/dev/null 2>&1 || true

# --- 2. Commit et tag ------------------------------------------------------
echo
echo "→ État du dépôt"
git status --short

echo
read -r -p "Enregistrer, taguer $TAG et pousser ? [o/N] " REPONSE
[[ "$REPONSE" =~ ^[oOyY]$ ]] || { echo "Abandon — rien n'a été poussé."; exit 0; }

git add -A
git commit -m "Version 1.1 des trois manuels

Terminale S : règle « pas de question avant la notion » tenue sans exception,
partie Algèbre réordonnée (suites, arithmétique, numération, matrices),
un devoir surveillé par chapitre, glossaire en annexe, corrigé de tous les
exercices d'entraînement. 224 pages élève, 286 professeur.

Terminale OSE : mathématiques financières passées en annexe, avant-propos
réécrit. Les PDF de la v1.0 étaient en retard de quatre pages sur leurs
sources. 178 pages élève, 210 professeur.

Terminale L : partie « Traitement des données » restructurée, annexes et
pages liminaires mises à jour. 136 pages élève, 170 professeur."

git tag -a "$TAG" -m "$TITRE"
git push origin main
git push origin "$TAG"

# --- 3. Release GitHub -----------------------------------------------------
echo
if command -v gh >/dev/null 2>&1; then
  gh release create "$TAG" \
    "Claude outputs/livre-t12s-eleve.pdf" \
    "Claude outputs/livre-t12s-prof.pdf" \
    "Claude outputs/livre-t12l-eleve.pdf" \
    "Claude outputs/livre-t12l-prof.pdf" \
    "Claude outputs/livre-t12ose-eleve.pdf" \
    "Claude outputs/livre-t12ose-prof.pdf" \
    --title "$TITRE" \
    --notes-file CHANGELOG.md
  echo "→ Release $TAG publiée."
else
  echo "La commande gh n'est pas installée : la release doit être créée à la main."
  echo "Ouvrez https://github.com/raantss18/Mada-Boky/releases/new?tag=$TAG"
  echo "et joignez les six PDF du dossier « Claude outputs »."
fi
