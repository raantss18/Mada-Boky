# Résolution séparée — géométrie

Tentative du même modèle à partir d'une extraction sans corrections, avant comparaison. Coordonnées métriques en repère orthonormé; orientation directe pour rotations et produits vectoriels. Préfixe `t11s-` omis dans les IDs.

## Calcul vectoriel (c13)

- auto :AB=(3,4),norme5.
- e01 :2a+b=5,a−b=1 ⇒a=2,b=1;déterminant−3≠0,base valide.
- e02 :produit6−4=2,normes√5 et5,cos=2/(5√5),dans[−1,1].
- e03 :AB=(4,0),AC=(1,√3),normes4 et2,produit4 ⇒cosA=1/2,A=π/3;BC²=(−3)²+3=12,BC=2√3. Triangle rectangle en C, titre cohérent.
- e04 :25+49=2AI²+64/2 ⇒AI²=21,AI=√21.
- e05 :u,v orthogonaux mais norme√2,donc produit=2(aa'+bb'),pas aa'+bb';u·u=2 contre-exemple à1. Pour une base réellement oblique, termes croisés aussi.
- e06 :aire=(30×40/2)sin60°=300√3 m²;troisième côté²=900+1600−2400×1/2=1300,soit10√13 m.

## Barycentres (c14)

- auto :milieu(3,2);x²−4x+4.
- e01 :G=((2+7)/3,(4−1)/3)=(3,1),somme3≠0.
- e02 :grouper B,C en(I,2);poids2,2 avec A donnent milieuAI.
- e03 :moyenne(2,1),centre du rectangle,également milieu des diagonales.
- e04 :MI²−9=k;pour0 :cercle(I,3);pour−9 :{I};pour−10 :vide.
- e05 :MA²+MB²=2MI²+8=18 ⇒MI²=5,cercle(I,√5).
- e06 :4(x²+y²)=(x−3)²+y² ⇒3x²+3y²+6x−9=0 ⇒(x+1)²+y²=4;centre(−1,0),rayon2. Barycentre(A,1),(B,−1/4) :abscisse(−3/4)/(3/4)=−1.
- e07 :somme0,division interdite;si A≠B,GA−GB=BA≠0,aucun point solution;si A=B,tous les G satisfont,aucune unicité,donc pas de barycentre au sens défini.

## Transformations (c15)

- auto :(−2,3) et(2,3).
- e01 :(5,−1);(0,1);(−1,2).
- e02 :OA=(2,0),multiplier−2 :OA'=(−4,0),A'=(−3,2);longueurs2 et4,rapport distances2.
- e03 :vecteur2AB=(4,4),translation,image(4,5).
- e04 :r∘t(0)=(0,1),t∘r(0)=(1,0);ordre non commutatif.
- e05 :α=2,β=1,ρ=√5;cosθ=2/√5,sinθ=1/√5,θ∈]0,π/2[ (tanθ=1/2). Point fixe :−x+y=1,−x−y=−2 ⇒x=1/2,y=3/2;det2≠0,unique.
- e06 :M'=3(−y,x);A'=(0,0),B'=(0,6),C'=(−3,0);aire initiale1,image9. Rotation quart de tour puis multiplication radiale3 décrit la construction.

## Trigonométrie (c16)

- auto :0,−1,1/2;π/2.
- e01 :150°=5π/6=500/3 grades;−17π/6+2π=−5π/6∈]−π,π].
- e02 :cos(π/4−π/6)=√2√3/4+√2/4=(√6+√2)/4.
- e03 :sinx=1/2 ⇒x=π/6+2kπ ou5π/6+2kπ;cos2x=0 ⇒2x=π/2+kπ ⇒x=π/4+kπ/2.
- e04 :arc d'ordonnée>√2/2 : ]π/4,3π/4[,aucune solution négative dans[−π,π].
- e05 :somme→2sin2x cosx;sin2x=0 ⇒x=kπ/2,cosx=0 donne sous-famille;sur[0,2π[ :0,π/2,π,3π/2.
- e06 :tangente strictement croissante sur l'intervalle sans pôle,ou cosx>0 transforme l'inégalité : ]−π/2,π/4];extrémités cos=0 exclues.
- e07 :sinx(cosx−1)=0 ⇒x=kπ OU x=2kπ;union x=kπ. Division perd les multiples impairs deπ,les multiples pairs subsistent via cosx=1.

## Espace (c17)

- auto :9;x=2,y=1.
- e01 :milieu(1/2,1/2,1/2),distance√3/2.
- e02 :produit1;u∧v=(−2,−1,2),norme3,aire3/2;produits avec u,v nuls.
- e03 :AB=(−1,1,0),AC=(−1,0,1),produit=(1,1,1)≠0;plan x+y+z=1. Paramétrage(1−s−t,s,t),s,t réels;normale orthogonale aux deux directions.
- e04 :t+(1+t)+(2−t)=3+t=4 ⇒t=1,point(1,2,1),unique.
- e05 :poserx=t ⇒(t,1−t,2t);point(0,1,0),direction(1,−1,2) non nulle. Normales(1,1,0),(−2,0,1) non colinéaires.
- e06 :somme3 pour toutt;premier plan contient la droite,deuxième intersection vide,droite strictement parallèle.
- e07 :|1+4+6−2|/√(1+4+4)=9/3=3.

## DS3

- e01 :AB·AC=12,aire12;G=((6+4)/4,8/4)=(5/2,2). I=(3,0);2MI²+18=26 ⇒MI=2,cercle(I,2).
- e02 :19π/6−4π=−5π/6;cos²x=1/2 ⇒π/4,3π/4,5π/4,7π/4;sinx≥1/2 ⇒[π/6,5π/6].
- e03 :ρ=2,θ=π/2;point fixe x=−2y+1,y=2x+2 ⇒x=−3/5,y=4/5;image(1,4),facteur aires4.
- e04 :AB∧AC=(1,1,1);plan somme1;droite somme6t=1 ⇒(1/6,1/3,1/2). Distance origine1/√3,aire√3/2.
