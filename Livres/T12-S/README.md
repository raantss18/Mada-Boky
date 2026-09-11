# Boky Matematika — Terminale S

Livre prof-élève de mathématiques pour la classe de Terminale, série S,
conforme au **Programme d'Études 2026** de l'Enseignement Secondaire Général
(Madagascar). Éditions Mada-Boky.

Dix-huit chapitres, trois annexes, deux éditions issues d'une source unique.
Chaque chapitre se termine par un devoir surveillé de deux heures, noté sur
vingt, cumulatif, assemblé d'énoncés authentiques.

## Compiler

```bash
./compiler.sh eleve      # édition de l'élève
./compiler.sh prof       # édition du professeur (corrigés + notes de classe)
./compiler.sh les-deux   # les deux
```

Moteur : XeLaTeX. Les polices Libertinus et Jost sont utilisées si elles sont
installées ; sinon le livre bascule automatiquement sur TeX Gyre Pagella et
TeX Gyre Heros, et compile à l'identique.

Pour ne recompiler qu'un chapitre, décommenter la ligne `\includeonly` en tête
de `livre-t12s.tex`.

## Mettre le dossier sous Git

```bash
chmod +x init-depot.sh && ./init-depot.sh
```

Le fichier `.gitignore` écarte le dossier `build/`, tous les PDF et les
fichiers auxiliaires LaTeX : seules les sources sont versionnées.

## Organisation

| Dossier | Contenu |
|---|---|
| `preambule/` | `bmt-style` (mise en page, couleurs), `bmt-blocks` (blocs pédagogiques), `bmt-macros` (notations) |
| `front/` | couverture, page de titre, avant-propos, mode d'emploi |
| `chapitres/p1-analyse` | chapitres 1 à 7 — 60 h |
| `chapitres/p2-algebre` | chapitres 8 à 11 — 45 h : suites, arithmétique, numération, matrices |
| `chapitres/p3-geometrie` | chapitres 12 à 16 — 45 h |
| `chapitres/p4-donnees` | chapitres 17 et 18 — 45 h |
| `annexes/` | progression annuelle non datée (édition professeur), formulaire, glossaire des notions, recueil de sujets |
| `figures/` | scripts de génération des figures |

## Anatomie d'un chapitre

Chaque chapitre suit le même parcours : révision des acquis antérieurs
uniquement, automatismes chronométrés, cours (définitions, propriétés,
théorèmes et démonstrations), blocs « je visualise » et « je comprends sur un
exemple », exercices placés juste après chaque notion, banque « je m'entraîne
sur annales », recherche, auto-évaluation, exercice type baccalauréat et
exercice de concours. L'édition professeur ajoute les corrigés et une note de
conduite de classe.

Règle absolue : **aucune question ne porte sur une notion avant qu'elle ait
été enseignée.** Les blocs d'entrée ne mobilisent que des acquis antérieurs.

## Les exercices d'annales

Aucun exercice n'est inventé. Chaque énoncé de la section « je m'entraîne sur
annales » porte sa provenance complète — pays, série, session, numéro. Les
sources sont les sujets Malagasy (sessions 2011 à 2026, baccalauréats blancs,
concours ENI), les baccalauréats africains de série C et D (Cameroun, Bénin,
Côte d'Ivoire, Congo-Brazzaville, Mauritanie, Burkina Faso) et les annales de
la médiathèque EDUCMAD d'AccèsMad. Lorsqu'un énoncé fait appel à une notion
étudiée plus loin dans l'année, la propriété nécessaire est admise juste avant
l'exercice, en italique et isolée.

Aucun indice ne figure du côté de l'élève, y compris dans les exercices de
concours ; les corrigés complets sont réservés à l'édition professeur.

## État

Dix-huit chapitres rédigés, trois annexes composées, compilation sans erreur
et sans débordement de ligne. Édition élève : 224 pages. Édition professeur :
286 pages. Le livre compte 248 exercices d'entraînement — tous corrigés dans
l'édition professeur —, 177 énoncés d'annales sourcés, 18 devoirs surveillés
de trois exercices, 21 exercices au format du baccalauréat et 18 exercices de
concours.
