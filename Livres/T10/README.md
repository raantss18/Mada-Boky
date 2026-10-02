# Manuel de mathématiques -- Seconde (T10), Madagascar

Projet LaTeX modulaire produisant deux éditions à partir d'une source commune :

- `main.tex` : édition élève;
- `main-prof.tex` : édition professeur, avec guide pédagogique, liens vers les
  corrigés et solutions complètes.

## Compilation

Prérequis : TeX Live 2023 ou plus récent avec `latexmk`, `makeindex`, TikZ,
PGFPlots, `tcolorbox`, `listings`, `titlesec`, `fancyhdr` et `mathpazo`.
Le projet ne dépend pas d'`algorithm2e` : le sous-ensemble de pseudo-code utilisé
est fourni dans `styles/mdg-algorithms.sty`.

Le cercle trigonométrique de `figures/cercle-trigonometrique.tex` est adapté
du fichier `Appendix/Trigonometrie.tex` communiqué dans le dossier Google Drive
de référence (consulté le 19 septembre 2026). La palette, le dédoublonnage des
angles et le placement des étiquettes ont été refaits pour cette maquette.

```bash
make all       # PDF élève et professeur
make student   # édition élève seulement
make teacher   # édition professeur seulement
make qa        # contrôles statiques du projet
```

Les PDF finaux sont créés dans `build/`.

Les deux PDF validés sont également conservés dans ce dépôt afin que les
enseignants puissent les consulter sans disposer d'une installation LaTeX.
À chaque modification, l'intégration continue exécute `make qa`, recompile les
deux éditions et publie les PDF comme artefacts du traitement.

## Organisation

```text
activities/    activités d'entrée, prérequis et automatismes par chapitre
assessments/   banque d'exercices et de problèmes, repère diagnostique et corrigés
backmatter/    glossaire, notations et colophon
chapters/      neuf chapitres élèves
docs/          validation technique et décisions éditoriales
frontmatter/   couverture, préface et mode d'emploi
scripts/       contrôles qualité reproductibles
solutions/     corrigés détaillés de l'édition professeur
review/        rapports de relecture et d'audit successifs
styles/        environnements, typographie et pseudo-code
teacher/       guide du professeur et progression annuelle
```

## Livrables validés

- `build/manuel-mathematiques-t10-eleve.pdf` : édition élève, 313 pages A4;
- `build/manuel-mathematiques-t10-professeur.pdf` : édition professeur,
  493 pages A4.

Les archives ZIP et les fichiers auxiliaires de compilation ne sont pas suivis
par Git : ils peuvent être recréés à partir des sources.

## Principes éditoriaux

1. Le parcours principal reste directement exploitable en classe.
2. Les approfondissements sont disponibles mais clairement signalés.
3. Les contextes ne supposent ni Internet ni ordinateur.
4. Les exercices externes ne sont pas reproduits; les références pédagogiques
   sont créditées dans le guide du professeur.
5. Toute correction d'une coquille de contenu doit être faite dans le module
   concerné, jamais uniquement dans un PDF généré.
6. Une série courte d'automatismes est prévue pour chacune des 66 séances. La
   banque contient des exercices autonomes et des problèmes de synthèse,
   structurés en sous-questions.
7. Chaque bloc indique la règle applicable à la calculatrice. Les structures
   BEPC, Bac et internationales inspirent l'organisation des assemblages, sans
   étendre les contenus au-delà de T10.
8. Les défis et contenus explicitement signalés comme extensions portent une
   ligne rouge, sont facultatifs, non exigibles en T10 et exclus des
   évaluations communes.

L'audit détaillé se trouve dans `docs/audit-programme-evaluations.md`.

## Référentiels officiels

Programme d'études T10 : `PSE/PE-2026/PE_T10.pdf` (mathématiques pp. 118-129);
répartition annuelle : `PSE/Répartitions 2025 2026/RAPE_T10_2025_2026.pdf`.
La conformité du cours est décrite dans `docs/audit-programme-evaluations.md` et
contrôlée par `make qa`. Le dépôt GitHub est la source faisant autorité
(voir `README-DRIVE-SNAPSHOT.md`).

## Provenance du corpus hérité

Le manuscrit hérité d'origine a servi de base à une séparation mécanique en
modules, ensuite relus et corrigés; il n'est pas conservé dans ce dépôt. Les
fichiers modulaires sont les seules sources faisant autorité.
