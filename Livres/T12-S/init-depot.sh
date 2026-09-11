#!/usr/bin/env bash
# ---------------------------------------------------------------------------
#  Initialise le dossier du livre comme dépôt Git.
#  À lancer une seule fois, depuis le dossier T12-S :
#      chmod +x init-depot.sh && ./init-depot.sh
#  Le fichier .gitignore, déjà présent, écarte le dossier build et tous les PDF.
# ---------------------------------------------------------------------------
set -e

if [ -d .git ]; then
  echo "Le dépôt existe déjà. Rien à faire."
  exit 0
fi

git init -b main
git add .
git commit -m "Boky Matematika — Terminale S : première version des sources

Éditions Mada-Boky. Livre conforme au Programme d'Études 2026,
série Scientifique option S."

echo
echo "Dépôt créé. Les PDF et le dossier build ne sont pas suivis."
echo
echo "Pour l'envoyer sur GitHub, créez le dépôt distant puis :"
echo "    git remote add origin git@github.com:VOTRE-COMPTE/boky-t12s.git"
echo "    git push -u origin main"
