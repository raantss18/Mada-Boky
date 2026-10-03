# Résolution séparée — données et synthèse

Tentative du même modèle sans consulter les corrections pendant la résolution; comparaison ultérieure. Variance descriptive divisée par N. Les quantiles utilisent les rangs par excès indiqués dans le cours.

## Statistique (c18)

- auto :30;3,3,5,8;moyenne19/4=4,75.
- e01 :50000×1,10×0,95=52250 ariary;coefficient1,045,hausse4,5%.
- e02 :inverse1/1,25=0,8,baisse20%.
- e03 :N=10,ordre5,5,10,10,10,10,10,15,15,15. Somme105,moyenne10,5;médiane10;Q1 rang3=10,Q3 rang8=15,D1 rang1=5,D9 rang9=15. Somme carrés1225,moyenne carrés122,5;variance122,5−110,25=12,25;écart type3,5.
- e04 :moyennes et médianes10;étendues4 et20;variances(4+0+4)/3=8/3 et(100+0+100)/3=200/3. Même centre n'implique pas même dispersion.
- e05 :moyenne et médiane augmentent3;écarts à la moyenne inchangés,variance et écart type inchangés.
- e06 :min2,max12;Q1 rang3=4,Q3 rang8=9;médiane(5+7)/2=6;boîte[4,9],trait6,moustaches2 et12 sur même axe linéaire.
- e07 :centres5 et15,moyenne(10×5+20×15)/30=35/3 min≈11,67;approximative,positions à l'intérieur des classes inconnues. Classes à préciser sans double appartenance au temps10.
- Exemple de cours :4,6,6,8,10,10,12,14. Somme70,moyenne35/4;SOMME DES CARRÉS692 (16+36+36+64+100+100+144+196),pas792. Variance692/8−(35/4)²=159/16=9,9375;écart type√159/4≈3,15238 min. Boîte min4,Q1=6,médiane9,Q3=10,max14 reste correcte. Erreur numérique à réparer dans cours ET DS4.

## Dénombrement (c19)

- auto :(a,1),(a,2),(b,1),(b,2);24.
- e01 :union25+18−10=33;aucun7.
- e02 :zéro initial accepté,10⁴=10000,10×9×8×7=5040 sans répétition;zéro initial exclu,9×10³=9000,9×9×8×7=4536 sans répétition.
- e03 :12×11=132 rôles ordonnés;C(12,3)=220 comités.
- e04 :2³=8 applications;0 injections par principe des tiroirs;surjections8−2 constantes=6,exhaustif car F a deux éléments.
- e05 :un sous-ensemble vide,un ensemble complet;complément bijecte les p-sous-ensembles et les(n−p)-sous-ensembles.
- e06 :exactement2 filles :C(5,2)×4=40;au moins1 :C(9,3)−C(4,3)=84−4=80.
- e07 :chaque comité compté3!=6 fois;336/6=56.

## Probabilités (c20)

- auto :3/5,2/5,36 couples.
- e01 :couples(1,6),(2,5),(3,4),(4,3),(5,2),(6,1) :6/36=1/6;pour2,seul(1,1) :1/36. Équilibre ET indépendance justifient les36 couples uniformes.
- e02 :intersection{6},prob1/6;union{2,4,5,6},prob2/3;contraire{1,3},prob1/3.
- e03 :C(7,3)=35;3 rouges :C(4,3)=4,prob4/35;exactement2 :C(4,2)×3=18,prob18/35;au moins1 bleue :1−4/35=31/35.
- e04 :deux tirages indépendants avec remise,49 couples d'objets équiprobables;2 rouges16/49;couleurs différentes2×4×3/49=24/49.
- e05 :union0,6+0,5−0,2=0,9;contraire0,1;pas incompatibles car intersection0,2>0. Atomiques0,2;0,4;0,3;0,1 sont positives,somme1 :données réalisables.
- e06 :non;uniformité angulaire donne1/4,1/4,1/2.
- e07 :1−C(4,3)/C(9,3)=1−4/84=20/21.

## DS4

- e01 :80000×0,85×1,10=74800;coefficient0,935,taux−6,5%;taux retour80000/74800−1=13/187≈6,95187%.
- e02 :moyenne8,75,médiane9,Q1=6,Q3=10,étendue10;variance159/16=9,9375,écart type√159/4≈3,15238. IQR4 min sépare les deux quartiles;la présence d'ex aequo oblige à éviter l'affirmation « exactement50% des observations » dans cet intervalle. Boîte4,6,9,10,14.
- e03 :totalC(10,3)=120;exactement2filles C(6,2)×4=60;au moins1 :1−C(4,3)/120=29/30;président/secrétaire10×9=90 versus C(10,2)=45,différence due à l'ordre.
- e04 :P(A)=1/2,P(B)=1/2,P(A∩B)=2/6=1/3,P(A∪B)=4/6=2/3;formule1/2+1/2−1/3.

## Synthèse A

- e01 :f=x+2+4/x,domaineR*;limites−∞/+∞ en0−/0+,−∞/+∞ aux infinis;asymptotesx=0,y=x+2. f'=1−4/x² :croît jusqu'à−2,puis décroît sur[−2,0[ et]0,2],puis croît;maxlocalf(−2)=−2,minlocalf(2)=6. f=7⇔x²−5x+4=0 avec x≠0 :1,4. f(h)+f(−h)=4,centre(0,2). f1=7,f'1=−3 :tangente−3x+10.
- e02 :v_(n+1)=3v_n. u0=2 donnev0=0,u constant2,limite2. u0=3 donnev0=1,u_n=2+3^n,strictement croissante,limite+∞;somme cinq termes=10+(1+3+9+27+81)=131.
- e03 :I=(2,0),MI²−4=5 ⇒cercle(I,3). HomothétiecentreArapport2 :centre(4,0),rayon6. Deux sommets choisisuniformément :6paires dont2diagonales,prob1/3.

## Synthèse B

- e01 :P1=0,(x−1)(x−2)(x+1),racines−1,1,2;PGCD36,PPCM1260;110101₂=53=203₅.
- e02 :cosx=√2/2 sur[−π,π] :±π/4;u∧v=(−2,−1,2),norme3,aire3/2. PlanparO :−2x−y+2z=0,directionsindépendantes;droite(1,0,t) donne−2+2t=0 ⇒(1,0,1),unique.
- e03 :moyenne10,5,écart type3,5;deuxhausses coefficient1,1²=1,21,taux21%;exactement2rouges18/35;au moins1rouge1−C(3,3)/35=34/35.
