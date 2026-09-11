# Boky Matematika — Terminale L

Troisième volume de la collection, après **T12-S** et **T12-OSE**.
Éditions Mada-Boky. Aucun nom d'auteur ne figure sur l'ouvrage.

Conforme au **Programme d'Études 2026** (Enseignement Secondaire Général,
Madagascar), série littéraire — épreuve de mathématiques générales,
options A1 et A2, 2 h 15, coefficients 1 et 3.

## Compiler

```bash
./compiler.sh eleve      # -> build/livre-t12l-eleve.pdf
./compiler.sh prof       # -> build/livre-t12l-prof.pdf
./compiler.sh les-deux
./compiler.sh propre
```

Moteur : XeLaTeX via `latexmk`. Le nom `Makefile` est refusé en écriture par
les outils distants : le pilote est `compiler.sh`.

État de la dernière compilation : **162 pages** (édition élève),
**202 pages** (édition professeur), sans erreur ni débordement.

## Arborescence

```
T12-L/
├── livre-t12l.tex            maître, avec \includeonly
├── compiler.sh               pilote de compilation
├── latexmkrc                 XeLaTeX, sortie dans build/
├── init-depot.sh             renvoie vers Livres/fusionner-depot-git.sh
├── .gitignore                écarte build/, les PDF, les auxiliaires
├── preambule/                bmt-style.sty · bmt-blocks.sty · bmt-macros.sty
├── front/                    couverture · page-titre · avant-propos · mode-emploi
├── chapitres/p1-algebre      ch01 · ch02 · devoir-1
├── chapitres/p2-analyse      ch03 à ch09 · devoir-2
├── chapitres/p3-suites       ch10 · ch11 · devoir-3
├── chapitres/p4-donnees      ch12 à ch14 · devoir-4
└── annexes/                  progression-prof (prof) · formulaire · glossaire · sujets
```

## Structure : quatre parties, quatorze chapitres

| Partie | Couleur | Heures | Chapitres |
|---|---|---|---|
| I — Algèbre | latérite | 12 h | 1 Équations et inéquations du second degré · 2 Systèmes d'équations linéaires |
| II — Analyse | indigo | 30 h | 3 Lire et interpréter une courbe · 4 Limites et branches infinies · 5 Dérivation et sens de variation · 6 Étude complète d'une fonction · 7 La fonction logarithme népérien · 8 La fonction exponentielle · 9 Primitives et calcul intégral |
| III — Suites numériques | palissandre | hors PE (RAPE, période 4) | 10 Généralités sur les suites · 11 Suites arithmétiques et suites géométriques |
| IV — Traitement des données et probabilités | raphia | 22 h | 12 Dénombrement · 13 Probabilité · 14 Statistique à deux variables |

Les couleurs indigo, latérite et raphia sont celles de toute la collection.
Le **palissandre** est propre à ce volume : il signale la partie qui ne
figure pas au tableau des contenus du PE 2026 (les suites), exactement comme
le grenat signalait les mathématiques financières dans T12-OSE.

## Décisions arrêtées

- **Référentiel** : PE 2026, section « Série littéraire », extraite du
  fichier `PSE/RAPE 2026/PE_T12.pdf` (pages 121 à 128 : Analyse 30 h,
  Algèbre 12 h, Traitement des données et probabilités 22 h ; aucun contenu
  de géométrie).
- **Les suites forment une partie à part** : absentes du tableau des
  contenus du PE, elles figurent dans la RAPE 2025-2026 (période 4), dans le
  programme 2019 (six semaines) et dans l'exercice 1 de **chaque** session
  dépouillée, de 1999 à 2026.
- **Ordre du livre** : les suites viennent après l'analyse, parce que les
  sujets écrivent `V_n = e^{2-n}` ou `W_n = ln(U_n)` — la règle d'antériorité
  l'impose. L'annexe de progression propose la conversion en cinq périodes.
- **Pas de bloc « je vise le concours »** : ni l'ENI ni l'ESPA ne
  correspondent au profil de la série.
- **Hors programme, et absents du livre** : nombres complexes, géométrie
  dans l'espace, calcul matriciel, probabilités conditionnelles,
  indépendance, variables aléatoires.
- **Options A1 / A2** : mêmes sujets, barème double `(A1 ; A2)`, questions
  supplémentaires de A2 signalées par `\pourAdeux` à leur place logique.
- **Devoirs surveillés** : un par partie (quatre au total), calibrés sur
  l'épreuve réelle — 2 h 15, deux exercices de 5 points, un problème de 10.
- **Livre intemporel** : aucune date ; la progression annuelle est en annexe
  professeur, avec une colonne « vos dates ».

## Formats d'exercices

Outre les blocs de la collection (révision, automatismes, je m'entraîne, je
cherche, je me teste, comme au baccalauréat, annales), ce volume ajoute :
`qcm`, `vraifaux`, `lecturegraphique`, `situation` et `devoirsurveille`,
avec `\bareme{}` pour les barèmes et `\pourAdeux` pour les questions
réservées à l'option A2.

## Banque d'annales

Sessions malgaches série A exploitées : **1999, 2000, 2001, 2002, 2003,
2004, 2005, 2009, 2010, 2012, 2013, 2014, 2015, 2016, 2017, 2020, 2021,
2022, 2026**, plus le baccalauréat blanc du Lycée Philibert Tsiranana
(2022-2023). Source : le sujet local 2026 (`Sujets/BAC-officiel/2026-A-litteraire/`)
et la médiathèque EDUCMAD/AccèsMad (cours « Série A — Mathématiques »).

Pour les chapitres 4, 5 et 6, où le problème malgache repose toujours sur un
logarithme ou une exponentielle, la banque est complétée par le fonds
générique déjà vérifié pour T12-S : baccalauréats probatoires du Cameroun
(séries D, TI, IH) et Côte d'Ivoire série C.

Un seul énoncé est signalé « **d'après** » : l'exercice 1 de la session
2022, dont la copie disponible est partiellement illisible ; l'énoncé y est
rétabli et chaque résultat redémontré.
