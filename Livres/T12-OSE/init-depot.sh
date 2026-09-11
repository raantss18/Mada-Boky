#!/usr/bin/env bash
# ---------------------------------------------------------------------------
#  Ce livre partage le dépôt Git de la collection Mada-Boky avec T12-S,
#  au lieu d'avoir son propre dépôt séparé.
#
#  Comme T12-S possède aujourd'hui son propre dépôt Git local (initialisé
#  dans Livres/T12-S/.git), la fusion en un seul dépôt commun aux deux livres
#  se fait avec le script Livres/fusionner-depot-git.sh, à lancer une seule
#  fois depuis le dossier Livres/ :
#
#      chmod +x fusionner-depot-git.sh && ./fusionner-depot-git.sh
#
#  Ce script est fourni à part (pas dans ce dossier T12-OSE) car il touche
#  aussi au dossier T12-S. Ce fichier init-depot.sh ne fait rien par
#  lui-même : il documente seulement la marche à suivre.
# ---------------------------------------------------------------------------
echo "Voir Livres/fusionner-depot-git.sh, à lancer depuis le dossier Livres/."
