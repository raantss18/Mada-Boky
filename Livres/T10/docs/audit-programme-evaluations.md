# Audit du programme T10 et des évaluations

Mise à jour : 2 octobre 2026. Ce document remplace la version du 20 septembre 2026,
dont la matrice déclarait « Conforme » des domaines dont le cours ne traitait pas
certaines notions (voir `review/03-full-quality-audit.md`).

## Référentiels

| Document | Emplacement dans le dépôt | Rôle |
|---|---|---|
| Programme d'études T10 (PE), MEN | `PSE/PE-2026/PE_T10.pdf`, mathématiques pp. 118-129 | Contenus, résultats d'apprentissage, critères d'évaluation |
| Répartition annuelle 2nde 2025-2026 (RAPE), MEN | `PSE/Répartitions 2025 2026/RAPE_T10_2025_2026.pdf`, mathématiques pp. 26-29 | Contenus par période; obligatoire dans les établissements concernés; base des sujets officiels |
| RAPE T10 « généralisation », édition août 2026 | **absent du dépôt** | Cité lors du passage 2 (lien Drive). À ajouter dans `PSE/` pour vérification |

Volume horaire : la page mathématiques du PE et le RAPE indiquent **4 heures** par
semaine; le tableau général du PE (p. 9) indique 5 heures. Le manuel retient
4 heures (128 h = 32 semaines; progression sur 33 semaines). Si l'établissement
dispose de 5 heures, la cinquième sert à la remédiation et à la pratique.

Répartition horaire du PE : analyse 62 h, algèbre 16 h, géométrie 40 h,
traitement des données 10 h.

## Matrice de conformité du cours

« Cours » désigne la partie de chaque chapitre qui précède la section Exercices.
Depuis le 2 octobre 2026, `make qa` vérifie automatiquement la présence de ces
notions dans le cours (`course_requirements` dans `scripts/qa.py`).

| Notion prescrite (PE / RAPE) | Où dans le cours | Statut |
|---|---|---|
| Énoncé, proposition; « et », « ou » inclusif et exclusif; implication, réciproque, équivalence; négations (De Morgan, implication); quantificateurs et traduction | Ch. 1, §1–3 | Conforme |
| Vocabulaire, variables, affectation, séquence, conditions, boucles bornées et non bornées, pseudo-code, organigramme; validité, complexité, efficacité | Ch. 2, §1–5 | Conforme |
| ℕ ⊂ ℤ ⊂ 𝔻 ⊂ ℚ ⊂ ℝ; fractions, puissances, racines | Ch. 3, §1, §2 et §6 | Conforme |
| Écritures décimale, fractionnaire, scientifique; valeurs approchées par défaut, par excès, arrondi d'ordre n | Ch. 3, §3 | Conforme |
| Encadrements d'ordre quelconque; somme, différence, produit, quotient | Ch. 3, §4 | Conforme |
| Intervalles, valeur absolue, distance; lien intervalle–distance–valeur absolue | Ch. 3, §4–5 | Conforme |
| Forme canonique, discriminant, racines, factorisation, signe du trinôme, inéquations du second degré | Ch. 4, §1–2 | Conforme |
| Degré 3 : égalité de polynômes, racine évidente, factorisation (identification, division), équations, signe, inéquations | Ch. 4, §3 | Conforme |
| Fractions rationnelles : valeurs interdites, équations, signe, inéquations | Ch. 4, §4 | Conforme |
| Systèmes de deux équations (algébrique et graphique), de deux inéquations (graphique) | Ch. 4, §5 | Conforme (RAPE) |
| Vecteurs : caractéristiques, égalité, opérations géométriques et analytiques, milieu | Ch. 5, §1–3 | Conforme |
| Colinéarité, alignement, parallélisme | Ch. 5, §4 | Conforme |
| Produit scalaire (définition géométrique et analytique), orthogonalité | Ch. 5, §5 | Conforme |
| Droites : équations cartésienne, réduite, paramétrique; vecteur directeur; passages entre formes; parallélisme, orthogonalité; hauteur, médiane, médiatrice | Ch. 6, §1 et §3 | Conforme |
| Cercles : équation cartésienne, cercle de diamètre [AB], équations paramétriques | Ch. 6, §2 et §4 | Conforme |
| Intersection droite–cercle : résolution analytique et graphique | Ch. 6, §4 | Conforme |
| Fonctions : ensemble de définition, image, antécédent, variations, extremums, parité | Ch. 7, §1–2 | Conforme |
| Fonctions de référence ax+b, x², 1/x, √x, \|x\|, x³ : variations démontrées, tableaux, courbes | Ch. 7, §3 | Conforme |
| Interprétation d'une courbe, résolution graphique | Ch. 7, §4 | Conforme |
| Triangle rectangle (rappel), radian, cercle trigonométrique, lignes des angles remarquables, propriété fondamentale | Ch. 8, §1–3 | Conforme |
| Fonctions trigonométriques : parité, périodicité; angles de cosinus ou sinus donné | Ch. 8, §4–5 | Conforme |
| Variable discrète/continue, effectifs, fréquences, classes | Ch. 9, §1 | Conforme |
| Mode, moyenne, médiane; étendue, variance, écart-type (exemple complet résolu) | Ch. 9, §2–4 | Conforme |
| Diagrammes en bâtons, circulaire, histogramme | Ch. 9, §5 | Conforme |

## Ordre d'enseignement

Les chapitres sont thématiques. La progression du guide du professeur (et les
66 séries d'automatismes, générées par `scripts/generate_automatismes.py`)
suivent l'ordre des cinq périodes du RAPE.

## Frontière : contenus non exigibles

Ces thèmes figurent dans des défis, des blocs « Hors programme T10 » ou des
exercices portant le repère `[HORS PROGRAMME T10]` :

- suites, récurrence, convergence et limites;
- probabilités et simulations probabilistes;
- récursivité, tris, codage binaire, compression RLE, Collatz, Horner et autres
  algorithmes spécialisés; invariant de boucle;
- barycentres, homothéties, rotations, droite d'Euler, puissance d'un point et axe
  radical; distance d'un point à une droite; position relative de deux cercles;
- asymptotes, point fixe, théorème des valeurs intermédiaires; transformations de
  courbes;
- résolution d'équations trigonométriques sur ℝ et identités avancées;
- quartiles, boîte à moustaches, régression, statistique bidimensionnelle et
  paradoxe de Simpson;
- contraposée et raisonnement par l'absurde; méthodes de Cardano, règle de
  Descartes.

Règle d'usage : proposés à un élève volontaire ou en approfondissement, jamais
prérequis ni évalués dans une épreuve commune.

Ne sont **plus** classés hors programme, car le RAPE les prescrit : systèmes
linéaires (chapitre 4) et fonction inverse (chapitre 7).

## Banque d'exercices et de problèmes

Chaque exercice ou problème est indépendant, porte une indication de calculatrice
et ne mobilise que des notions du parcours prescrit (contrôle par mots-clés du
2 octobre 2026). Usages : diagnostic, formatif, sommatif (voir le guide).

## Points restant à vérifier

1. Lire le RAPE « août 2026 » et vérifier qu'il ne modifie pas la liste ci-dessus.
2. Le classement des énoncés d'exercices hors programme a été fait sur leurs
   titres et leurs thèmes; une relecture item par item des quelque 1 100
   exercices reste souhaitable avant d'en utiliser de nouveaux en évaluation commune.
3. Les relations de Viète (chapitre 4) ne figurent ni au PE ni au RAPE; elles
   sont conservées sans repère, car elles servent d'outil de contrôle. Décision
   éditoriale à confirmer.
