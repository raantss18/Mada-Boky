#!/usr/bin/env bash
# ---------------------------------------------------------------------------
#  Fusionne T12-S et T12-OSE dans un seul dépôt Git commun à la collection
#  Mada-Boky, au lieu d'un dépôt par livre.
#
#  À lancer UNE SEULE FOIS, depuis le dossier Livres/ (celui qui contient
#  T12-S/ et T12-OSE/) :
#
#      chmod +x fusionner-depot-git.sh && ./fusionner-depot-git.sh
#
#  Ce que fait le script :
#    1. Vérifie qu'il n'y a pas déjà un dépôt à la racine de Livres/.
#    2. Met de côté l'historique Git actuel de T12-S (T12-S/.git-historique-solo),
#       au lieu de le supprimer : rien n'est perdu, mais le nouveau dépôt
#       commun repart avec un historique propre à lui.
#    3. Initialise un nouveau dépôt à la racine de Livres/, y ajoute T12-S et
#       T12-OSE, et fait un premier commit commun.
#
#  Il ne touche à aucun fichier source, seulement à la structure Git.
# ---------------------------------------------------------------------------
set -e
cd "$(dirname "$0")"

if [ -d .git ]; then
  echo "Un dépôt existe déjà ici (Livres/.git). Rien à faire."
  exit 0
fi

if [ ! -d T12-S ] || [ ! -d T12-OSE ]; then
  echo "Ce script doit être lancé depuis le dossier Livres/, qui doit"
  echo "contenir T12-S/ et T12-OSE/."
  exit 1
fi

if [ -d T12-S/.git ]; then
  mv T12-S/.git T12-S/.git-historique-solo
  echo "Ancien historique de T12-S conservé dans T12-S/.git-historique-solo"
  echo "(dossier cache, hors suivi Git — à supprimer plus tard si inutile)."
fi

git init -b main
cat > .gitignore <<'EOF'
# Chaque livre a deja son propre .gitignore (build/, PDF, fichiers auxiliaires
# LaTeX). Celui-ci ne fait qu'ecarter les traces laissees par la fusion.
*/.git-historique-solo/
EOF

git add T12-S T12-OSE .gitignore
git commit -m "Fusion des livres T12-S et T12-OSE dans un dépôt commun

Éditions Mada-Boky, collection Boky Matematika."

echo
echo "Dépôt commun créé à la racine de Livres/."
echo "Pour le connecter au dépôt GitHub existant (raantss18/Mada-Boky) :"
echo "    git remote add origin git@github.com:raantss18/Mada-Boky.git"
echo "    git push -u origin main --force-with-lease"
echo
echo "ATTENTION : --force-with-lease écrase l'historique distant actuel,"
echo "qui ne contenait que T12-S. Vérifiez d'abord que rien d'autre n'a été"
echo "poussé sur ce dépôt distant depuis un autre poste."
