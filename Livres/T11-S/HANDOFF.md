# T11 S — reprise et remise du travail

Ce fichier est un guide de reprise pour une autre instance, pas une fiche distribuée aux élèves et pas une approbation de publication. Les sources canoniques restent dans `raantss18/Mada-Boky`, branche `main`, dossier `Livres/T11-S`.

1. Récupérer le `main` courant; préserver les changements extérieurs à ce dossier et réconcilier les nouveaux commits.
2. Lire `AGENTS.md`, `project/index.md`, `project/tasks.md`, `review/issues.json` et `review/checkpoint-verification.json`. Leurs dates, hashes et états priment sur une ancienne conversation.
3. Utiliser build-maths-textbook. Référence de contenu : `PSE/PE-2026/PE_T11.pdf`, pages imprimées 352–363, couverture « VERSION EXPÉRIMENTALE ». Aucune approbation ministérielle définitive ni calendrier actuel n'est affirmé.
4. Après toute modification, invalider les contrôles dépendants. Recalculer l'inventaire (`python3 scripts/build_inventory.py`), vérifier sémantiquement ses groupes et mettre à jour la correspondance curriculaire.
5. Résoudre séparément les nouveaux énoncés avant comparaison aux corrections; conserver les calculs et leurs limites dans `review/evidence/`.
6. Compiler les deux éditions par `bash compiler.sh les-deux`. Inspecter chaque page de chaque PDF final à résolution lisible; une miniature ou une compilation ne suffit pas.
7. Exécuter `python3 scripts/check_gates.py .` sans modifier sa politique; conserver sortie et code. Ne déclarer « passed » qu'un contrôle effectivement fait sur les sources et PDF courants.
8. Sauver les sources, PDF et preuves ensemble; lire le commit/arbre distant et comparer les hashes. Sauver ensuite le rapport de persistance et le pointeur de reprise, puis vérifier aussi ce dernier commit.

État détaillé et prochaine action : `project/index.md` et `project/tasks.md`. Tant qu'une revue requise manque ou qu'un défaut demeure, les PDF restent des brouillons. Une candidature vérifiée par modèle, si elle est atteinte, reste distincte d'une approbation humaine de publication.

État au 2026-10-03T06:30:11.959261+00:00 : 947 objets / 206 groupes / 87 exigences; deux builds propres réussis et 248 pages finales inspectées. Checker inchangé : code 0. Snapshot `d8e0177459644755457cd0d406d5ed2dcaab4977b68aadc707c8fa862851d91e`. Source/PDF/preuves relus à `5318824ff0b4a9a8545159ff1b7d7aabcee71313`; la sauvegarde suivante porte les gates et le pointeur. Statut conservé : brouillon relu par modèle, publication humaine non approuvée.
