# Résolution séparée — analyse

Méthode : tentative du même modèle sur une extraction sans blocs `corrige`, puis comparaison à effectuer séparément. Ce n'est pas une revue humaine indépendante. Les chapitres 2 et 3 avaient été lus avec leurs corrections à la reprise; les calculs ci-dessous sont refaits sans consultation de celles-ci pendant la tentative. Tous les calculs portent sur les réels, angles en radians.

## Chapitre 1

- c01-auto : x≥3; ±2; 7,7; 7,5; x≠−1/2; strictement négatif; 1,1,−1; x²,−x³; ±3; aucune racine réelle de −4.
- c01-e01 : substitution donne 1,8,−1.
- c01-e02 : substitutions avec dénominateurs non nuls : −1/2,10,2/3.
- c01-e03 : f(x)=1 ⇔ x(2x−5)=0 : 0,5/2. f(x)=−3 ⇔ 2x²−5x+4=0, Δ=−7 : aucun.
- c01-e04 : 3x+1=3(x−2) donnerait 1=−6 : aucun; g=3+7/(x−2).
- c01-e05 : √(x+4)=0 donne −4; =3 donne 5; =−1 impossible par positivité.
- c01-e06 : 7 est l'image de −2; −2 est un antécédent de 7.
- c01-e07 : R; R\{−5}; R\{−3,3}; [3,+∞[; ]−∞,5]; ]1,+∞[.
- c01-e08 : x²+1>0 donne R; x²−1=0 exclut ±1. Même si le facteur x−1 se simplifie, 1 reste exclu.
- c01-e09 : (x−1)(x−4)≥0 donne ]−∞,1]∪[4,+∞[.
- c01-e10 : x≤3 et x≠±2, soit ]−∞,−2[∪]−2,2[∪]2,3].
- c01-e11 : |x|≠2, soit R\{−2,2}.
- c01-e12 : quotient positif sur ]−∞,−2], négatif sur ]−2,3[, positif sur ]3,+∞[; −2 inclus, 3 exclu.
- c01-e13 : décroissance stricte de la fonction affine (pente −3); croissance stricte de 5x² sur [0,+∞[.
- c01-e14 : x² décroît jusqu'à 0 puis croît; multiplier par −4 renverse les deux sens, maximum 0 en 0. Limites de x² : +∞; celles de −4x² : −∞.
- c01-e15 : si √a>√b, la différence des carrés est positive, donc a>b, contradiction. Racine carrée strictement croissante également lorsque a<b.
- c01-e16 : pour 0<a<b, 1/b−1/a=(a−b)/(ab)<0; décroissance stricte.
- c01-e17 : −2≤f(0)≤8; aucune valeur précise, aucune égalité forcée ni continuité garantie. Des fonctions croissantes en escalier réalisent diverses valeurs.
- c01-e18 : a,c,e paires; b,d impaires (d sur R\{±2}); f ni paire ni impaire, domaine [0,+∞[ non symétrique.
- c01-e19 : R\{2} n'est pas symétrique : −2 y est, 2 n'y est pas.
- c01-e20 : f(3+h)=h²−4=f(3−h); domaine R invariant.
- c01-e21 : g(1+h)=2+1/h et g(1−h)=2−1/h pour h≠0; somme 4; domaine invariant autour de 1.
- c01-e22 : fg est impaire par changement x→−x. f+g paire seulement si g=0, impaire seulement si f=0; en général ni l'une ni l'autre (1+x). Si les deux sont nulles, les deux parités s'appliquent.
- c01-e23 : f(x)=f(−x)=−f(x), donc 2f(x)=0 partout.
- c01-e24 : T=π/2 donne sin(4x+2π)=sin4x. Pour une période T, prendre x=0 donne sin4T=0 et x=π/8 donne cos4T=1; donc 4T∈2πZ. Plus petite période positive π/2.
- c01-e25 : T=4π. x=0 implique cos(T/2)=1, donc T∈4πZ; minimalité.
- c01-e26 : addition de deux fonctions 2π-périodiques. f(0)=1 interdit l'imparité; f(π/2)=1 et f(−π/2)=−1 interdisent la parité.
- c01-e27 : cos²(x+π)=cos²x; paire. Une période T satisfait cos²T=1, donc T∈πZ; plus petite π. Symétrie/périodicité ramènent à [0,π/2]. « Le plus court » sera à préciser comme réduction obtenue par ces deux outils.
- c01-e28 : 4,7,−2 diffèrent de 1 de multiples de 3 : trois valeurs 5.
- c01-e29 : f(T/2+h)=f(−T/2−h)=f(T/2−h), par parité puis période T.
- c01-problem : f(0)=0,f(1)=1,f(2)=0. f(−1)=−1, f(3)=f(−1)=−1, f(5)=f(1)=1. Sur [−2,0], f(x)=x(2+x); recopier le motif [−2,2] par multiples de 4. x=1 n'est pas axe global : f(−1)=−1≠f(3)=−1 ne réfute pas, mais f(−1/2)=−3/4 et f(5/2)=−3/4 non plus; chercher le bon point : f(0)=f(2)=0, f(−1)=f(3)=−1. En fait x=1 EST axe : sur [0,2], x(2−x) est symétrique autour de 1; la portion négative est symétrique autour de −1 et la répétition de période 4 étend la symétrie. Pour tout x, réduire à [0,4], vérifier f(2−x)=f(x) par les deux morceaux, puis périodicité. Attention : parité impaire n'interdit pas un axe décalé.
- c01-test : domaine [−3,4[∪]4,+∞[ (−4 hors domaine); g=1 ⇔ 2x(x−4)=0 : 0,4; h=x²+x⁻² paire sur R*; g(2±h)=2h²−7; sin3x impaire, période 2π/3, réduction [0,π/3] par imparité/périodicité. La locution « plus petit » nécessite la même précision.

## Chapitre 2

- auto : (x−3)(x+3),2,0,001,4,x>2. act : quotient x+1 sauf 1 : 1,9;1,99;2,01;2,1, limite 2, indéfini en 1.
- e01 : substitution autorisée : 2 et 1.
- e02 : (x²−9)/(x−3)=x+3 sauf 3 : 6; (x−1)(x−2)/(x−1)=x−2 sauf 1 : −1.
- e03 : domaine x≥−4,x≠0; conjugué 1/(√(x+4)+2) : 1/4.
- e04 : −2x³ domine : −∞ à droite,+∞ à gauche; division par x² du quotient donne 4 aux deux infinis (x=0,3 exclus).
- e05 : valeur/limite droite m, limite gauche 3; m=3, nécessaire et suffisant.
- e06 : polynôme continu, valeurs −1,1 : zéro intérieur. Pour a<b, b³−a³>0 et b−a>0, donc croissance stricte et unicité sur R.
- e07 : x+1 a limite 2; ajouter 100(x−0,9)(x−1,1) conserve les deux mesures mais limite 1. Données finies ne prouvent pas une limite.

## Chapitre 3

- auto : x+1 sauf 1; 1/(x−2) négatif à gauche, positif à droite.
- e01 : 3+8/(x−2); verticale 2, horizontale 3; écart signe x−2.
- e02 : division 2x−1+3/(x−1); oblique 2x−1, verticale 1.
- e03 : limite 2 en 1, aucune branche infinie, trou en (1,2).
- e04 : différence √(x²+1)−x=1/(√(x²+1)+x)→0 à droite; à gauche la somme √(x²+1)+x→0, oblique −x. La différence demandée à gauche tend à +∞.
- e05 : x/(x²+1)→0, oblique 2x−3; seul zéro de l'écart x=0 : (0,−3).
- e06 : rapports x,1/√x,1+1/√x : directions verticale,horizontale,oblique pente 1; écarts divergents, pas d'asymptote droite.

## Chapitre 4

- auto : 2ah+h²; pente (6−2)/(3−1)=2. act : ((2+h)²−4)/h=4+h→4.
- e01 : différence divisée par h =6a+3h−2→6a−2.
- e02 : 3x²−4;8(2x−1)³;−3/(x−2)² sur R\{2};3cos3x. Les autres domaines de dérivation sont R.
- e03 : f(2)=−2,f'(2)=1 : y=x−4. Écart (x−2)²≥0, égalité seulement en 2.
- e04 : f'=3(x−1)(x+1); +,−,+ aux seuils −1,1; valeurs 2,−2; limites −∞,+∞.
- e05 : continue en 2, taux −1 à gauche,1 à droite, non dérivable; pentes −1 et 1.
- e06 : autres côté 20−x,0<x<20; aire 20x−x²=100−(x−10)²; maximum 100 m² pour carré 10 m.
- e07 : continuité a+b=1; taux droit a, gauche 2; a=2,b=−1, conditions suffisantes aussi.

## Chapitre 5

- auto : (x−3)(x+1); f(0)=−1.
- e01 : (x−2)²−1, domaine R; +∞ aux deux bornes; décroît jusqu'à 2 puis croît; minimum −1; axe 2; intersections (1,0),(3,0),(0,3). Tracé parabole avec ces points.
- e02 : différence x²−5x+4=(x−1)(x−4); au-dessus hors [1,4], en dessous sur ]1,4[, intersections (1,0),(4,3).
- e03 : h=2+3/(x−1), dérivée −3/(x−1)²; décroît sur chaque composante; limites 2 à ±∞,−∞ en 1−,+∞ en 1+; asymptotes x=1,y=2; axes (−1/2,0),(0,−1); centre (1,2).
- e04 : résultats c04-e04, fonction impaire; f''=6x change signe en 0; inflexion (0,0), tangente y=−3x.
- e05 : x² : dérivée nulle et minimum; x³ : dérivée nulle et aucun extremum.
- e06 : −2sinx<0 sur ]0,π[, décroissance de 2 à −2; parité puis périodicité 2π permettent le tracé complet.

## DS1

- e01 : simplification x+2 donne 4. Raccord : b=1 pour continuité, a=0 pour taux gauche/droit 0.
- e02 : g=(x−1)+1/(x−1), domaine R\{1}; verticale 1 et oblique y=x−1; écart signe x−1; limites −∞/+∞ en 1−/1+, −∞/+∞ aux infinis. g'=1−1/(x−1)²=x(x−2)/(x−1)². Croît ]−∞,0], décroît [0,1[ puis ]1,2], croît [2,+∞[. Max local (0,−2), min local (2,2); centre (1,0) car g(1±h)=±(h+1/h). Esquisse à deux branches respectant ces données.
- e03 : A=x(12−x),0<x<12; max 36 m² en 6. A(4)=32,A'(4)=4 : tangente y=4x+16; A−tangente=−(x−4)²≤0.

Les identifiants abrégés ci-dessus sont préfixés `t11s-` dans les sources. Une correction complète doit aussi fournir les limites explicitement demandées et une méthode de tracé, pas seulement une valeur finale.
