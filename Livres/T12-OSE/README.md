# Boky Matematika — Terminale OSE

Livre prof-élève de mathématiques pour la classe de Terminale, série OSE
(Organisation Société Économie), conforme au **Programme d'Études 2026** de
l'Enseignement Secondaire Général (Madagascar). Éditions Mada-Boky.

Dix-sept chapitres en cinq parties, trois annexes, deux éditions issues d'une
source unique — même principe éditorial que le livre de Terminale S.

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
de `livre-t12ose.tex`.

## Dépôt Git

Ce livre partage le dépôt Git de la collection avec T12-S plutôt que d'avoir
le sien. Voir `init-depot.sh` et `../fusionner-depot-git.sh`.

## Organisation

| Dossier | Contenu |
|---|---|
| `preambule/` | `bmt-style` (mise en page, couleurs), `bmt-blocks` (blocs pédagogiques), `bmt-macros` (notations) — identiques à ceux de T12-S, plus une cinquième couleur (`bmtGrenat`) pour les mathématiques financières |
| `front/` | couverture, page de titre, avant-propos, mode d'emploi |
| `chapitres/p1-analyse` | chapitres 1 à 6 — 80 h |
| `chapitres/p2-algebre` | chapitres 7 et 8 — 25 h |
| `chapitres/p3-geometrie` | chapitres 9 à 12 — 45 h |
| `chapitres/p4-donnees` | chapitres 13 à 15 — 30 h |
| `chapitres/p5-financieres` | chapitres 16 et 17 — hors chiffrage du PE, période 4 de la RAPE |
| `annexes/` | progression annuelle non datée (édition professeur), formulaire, glossaire des notions, recueil de sujets |
| `figures/` | scripts de génération des figures |

## Ce qui diffère du livre de série S

- **Analyse** plus large (80 h contre 60 h) mais sans équations différentielles.
- **Algèbre** resserrée : ni arithmétique, ni calcul matriciel général — un
  seul système linéaire, à trois inconnues.
- **Géométrie** aussi riche que celle de série S (complexes, barycentre,
  isométries, similitudes directes et indirectes), alors qu'aucun sujet de
  baccalauréat OSE examiné à ce jour ne l'a testée : le livre reste fidèle au
  Programme d'Études 2026 malgré cet écart, choix confirmé avec l'auteur.
  Voir `claude/reforme-2026-ose.md` dans le projet pour le détail de cet écart.
- Pas de géométrie dans l'espace.
- Une **cinquième partie**, Mathématiques financières, absente des quatre
  composantes du PE mais bien réelle : présente dans le programme 2019, dans
  la RAPE (période 4) et dans chaque sujet de baccalauréat OSE examiné.
- Pas de bloc « je vise le concours » : ENI et ESPA ne correspondent pas au
  profil de la série OSE.

## Anatomie d'un chapitre

Chaque chapitre suit le même parcours que dans le livre de série S : révision
des acquis antérieurs uniquement, automatismes chronométrés, cours
(définitions, propriétés, théorèmes et démonstrations), blocs « je visualise »
et « je comprends sur un exemple », exercices placés juste après chaque
notion, banque « je m'entraîne sur annales », recherche, auto-évaluation, et
exercice type baccalauréat. L'édition professeur ajoute les corrigés et une
note de conduite de classe.

Règle absolue : **aucune question ne porte sur une notion avant qu'elle ait
été enseignée.** Les blocs d'entrée ne mobilisent que des acquis antérieurs.

## Les exercices d'annales

Aucun exercice n'est inventé. Chaque énoncé de la section « je m'entraîne sur
annales » porte sa provenance complète — pays, série, session, numéro. Les
sources principales sont les sujets malgaches de série OSE (sessions 2021,
2022 et 2026, EDUCMAD/AccèsMad et archives locales) ; en renfort ponctuel,
des séries économiques francophones (Côte d'Ivoire G1/G2, Sénégal G) pour les
chapitres où la banque malgache seule ne suffit pas, et — pour les chapitres
d'analyse antérieurs au logarithme, où le contenu ne dépend pas de la série —
le même fonds générique (Côte d'Ivoire, Cameroun) déjà vérifié pour T12-S.
Lorsqu'aucune source conforme n'existe, l'exercice « comme au baccalauréat »
est un exercice original calibré sur l'épreuve, signalé comme tel.

Aucun indice ne figure du côté de l'élève ; les corrigés complets sont
réservés à l'édition professeur.

## État

Structure des cinq parties et dix-sept chapitres fixée. Rédaction en cours —
voir la liste des tâches du projet pour l'avancement chapitre par chapitre.
