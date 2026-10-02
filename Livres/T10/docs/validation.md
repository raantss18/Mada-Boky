# Validation de l'édition 2026

Date du contrôle : 20 septembre 2026; mise à jour le 2 octobre 2026 (compléments de cours, voir `review/03-full-quality-audit.md`).

## Périmètre livré

- 9 chapitres et 9 activités d'entrée;
- 411 exercices, 139 problèmes et 67 défis;
- 66 séries d'automatismes, soit une par séance sur 33 semaines;
- 1 repère diagnostique, 42 exercices structurés et 8 problèmes de synthèse;
  chaque bloc précise son usage de la calculatrice;
- édition élève : 313 pages A4;
- édition professeur : 493 pages A4, guide, progression, liens et corrigés.

## Contrôles réalisés

- compilation reproductible des deux éditions avec pdfLaTeX et `latexmk`;
- résolution de toutes les références internes;
- correspondance complète entre numéros d'exercices/problèmes et corrigés;
- contrôle statique des entrées, environnements, contenus attendus et
  caractères non portables (`make qa`);
- vérification visuelle des couvertures, sommaires, chapitres, graphiques,
  pseudo-codes, évaluations, corrigés et annexes, plus une planche-contact de
  toutes les pages;
- polices incorporées dans les PDF.
- aucun débordement horizontal; dans l'édition professeur, deux débordements
  verticaux de 1,34 pt (sans effet visible);
- présence dans le cours de chaque notion du PE/RAPE T10 (`make qa`).
- conformité de chaque question d'évaluation au PE/RAPE T10 et présence d'un
  audit séparant le parcours prescrit des enrichissements non exigibles.
- signalisation visuelle continue en rouge des défis et blocs explicitement
  identifiés hors programme T10.

## Relectures encore recommandées

Avant une diffusion large, il reste souhaitable d'organiser une double lecture
mathématique indépendante, une relecture linguistique et un essai dans plusieurs
classes aux profils variés. Cette étape est distincte du contrôle éditorial et
technique du présent projet.
