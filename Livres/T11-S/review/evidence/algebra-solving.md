# Résolution séparée — algèbre

Tentative du même modèle sur les sources privées des blocs `corrige`, avant comparaison. Domaines réels sauf entiers explicitement annoncés. Les identifiants ci-dessous portent le préfixe `t11s-`.

## Logique (c06)

- auto : 0,2,4; 9≠6 donc faux; x=±2.
- e01 : x≤2 OU x≥5; il existe un entier non pair; pour tout réel x,x²≠−1.
- e02 : réciproque x²>4⇒x>2 fausse (−3); contraposée x²≤4⇒x≤2 vraie, puisque −2≤x≤2; implication initiale vraie.
- e03 : au moins un facteur nul, autorisant les deux; a=b=0 réfute « exactement un ».
- e04 : premier vrai en prenant m=n+1; second faux (n=0 forcerait m=1 et n=1 forcerait m=2). Négations : ∃n∈N,∀m∈N,m≠n+1; ∀m∈N,∃n∈N,m≠n+1.
- e05 : x≥0 donne |x|=x par définition; |x|=x donne x≥0 car |x|≥0.
- e06 : 0 rend l'énoncé indéfini; sur R*, x=−1 le réfute.
- e07 : (2k+1)+(2l+1)=2(k+l+1), pair; réciproque fausse pour 2+4.

## Algorithmique (c07)

- auto : reste 2; a=5; somme 10.
- e01 : u=2 puis 5,14,41; sortie 41.
- e02 : lire n∈N; S=0; pour k=1,…,n ajouter k²; afficher S. Invariant S=Σ(j²,j=1,…,k), terminaison après n tours; n=0 : 0; n=3 :14.
- e03 : résultat erroné (7,7). Temp=a;a=b;b=Temp donne (7,4).
- e04 : u=3,6,12,24,48,96,192; test ≤100 : n=6. Test <96 : sortie 96,n=5; l'égalité change le dernier tour.
- e05 : u reste 1 car (1+1)/2=1; test toujours vrai, aucune terminaison en calcul exact.
- e06 : Lire n,S=0,k=1 → losange k≤n? → oui : S=S+k²,k=k+1 puis retour au test; non : afficher S. Tester n=0 fait directement sortir, n=3 donne14.

## Équations (c08)

- auto : (x−2)(x−3); ±3; x≥1.
- e01 : (x−1)((m−1)x−2)=0. Si m=1 : x=1. Sinon 1,2/(m−1), racines confondues seulement pour m=3. Aucun cas sans racine.
- e02 : côtés a+b=13,ab=40; X²−13X+40=(X−5)(X−8), dimensions5 m et8 m (toutes deux positives).
- e03 : P(1)=4, affirmation fausse; P(−1)=0 et P(2)=0; division par x+1 donne x²−5x+6=(x−2)(x−3), solutions−1,2,3, exhaustives.
- e04 : X=x²≥0, (X−1)(X−4)=0; x=−2,−1,1,2.
- e05 : domaine x≥−2. Pour √(x+2)≤x, imposer x≥0 puis x²−x−2≥0 : [2,+∞[. Pour >, tous les −2≤x<0 puis 0≤x<2 : [−2,2[. Les deux ensembles partitionnent le domaine.
- e06 : x<−2 donne −2x−1=5 ⇒−3; −2≤x≤1 donne3≠5; x>1 donne2x+1=5 ⇒2.
- e07 : x≠−1; quotient positif sur ]−∞,−1[ et [2,+∞[, négatif entre −1 et2; 2 inclus.
- e08 : domaine x≥−3/2 et membre droit≥0 donc x≥1; carré donne x=2±√6; seule2+√6≥1, substitution confirme.

## Systèmes (c09)

- auto : x=3,y=2; 0=1 impossible.
- e01 : deuxième moins première : x−2y=−3; troisième moins première : y−2z=−4. Résoudre donne z=3,y=2,x=1; substitution (6,3,2).
- e02 : y=s,x=3−s,z=5−s,t=2+s; quatrième équation vaut toujours10. Toute valeur s∈R convient, pas d'unicité.
- e03 : deuxième moins2×première donne0=−1; aucune solution.
- e04 : b=s,a=9−s,c=11−s,d=2+s; dernière 13+s=20 ⇒s=7. (a,b,c,d)=(2,7,4,9), milliers d'ariary; vérifier9,11,13,20.
- e05 : addition des deux dernières moins première donne2x=6 ⇒x=3,y=1,z=2. Première ligne sans x, échanger avec une ligne à coefficient non nul.
- e06 : soustraction (m−1)y=1. m=1 : impossible; m≠1 : y=1/(m−1),x=(2m−3)/(m−1), unique.

## Arithmétique (c10)

- auto :47=6×7+5;1,2,3,4,6,12.
- e01 :91=7×13 composé; pour101 tester2,3,5,7 (√101<11); aucun ne divise101, premier.
- e02 :180=2²3²5,252=2²3²7;PGCD36,PPCM1260, produit36×1260=180×252.
- e03 :1071=2×462+147;462=3×147+21;147=7×21;PGCD21,fraction51/22, copremiers.
- e04 :PGCD(84,126)=42 lots,2 cahiers3 stylos par lot; tout nombre admissible de lots divise les deux effectifs, d'où maximalité.
- e05 :PPCM(12,18)=36 jours; premier multiple commun positif.
- e06 :8 et9 sont composés et copremiers; deux premiers distincts ont seul diviseur commun1.
- e07 :24=2³3,36=2²3²,54=2×3³;PGCD6,PPCM216. Leur produit1296≠24×36×54=46656 : la formule à deux facteurs ne s'étend pas directement.

## Numération (c11)

- auto :32,27;23=2×11+1.
- e01 :16+8+1=25;2×27+1×9+0×3+2=65;2×16+10=42.
- e02 :53=32+16+4+1=(110101)₂;53=2×25+0×5+3=(203)₅.
- e03 :2 interdit en base2; chiffre maximal7 implique base minimale8.
- e04 :2b+3=17 ⇒b=7≥4, valide.
- e05 :1011₂+110₂=10001₂;11+6=17. Retenues aux colonnes2 et4 produisent les chiffres successifs1,0,0,0,1.
- e06 :premier chiffre≥1 donne borne b^(k−1); valeur maximale Σ((b−1)b^i,i=0,…,k−1)=b^k−1, bornes atteintes par100…0 et(b−1)…(b−1).

## Suites (c12)

- auto :16,1/8,18.
- e01 :u0=−2,u5=13,u10=28,différence3>0;v_n=2+3n par récurrence.
- e02 :5r=22−7=15 ⇒r=3;6 termes, somme6(7+22)/2=87.
- e03 :u_n=81/3^n,limite0;termes81,27,9,3,1;somme121.
- e04 :u_n=1−1/(n+2);différence1/((n+2)(n+3))>0;limite1.
- e05 :u alterne±1, deux sous-suites distinctes donc aucune limite;|v_n|=1/(n+1)→0 donc v→0 malgré l'alternance. Ni u ni v monotones.
- e06 :v_n=u_n−50, v_(n+1)=0,8v_n,v0=50;u_n=50+50×0,8^n,strictement décroissante et limite50.
- e07 :1,3,7 :différences2,4 et ratios3,7/3, ni arithmétique ni géométrique. Avec u0=−1, suite constante−1 (arithmétique r=0,géométrique q=1).
- e08 :Lire N≥0;u=100,S=100;pour k=1,…,N :u=0,8u+10,S=S+u;afficher u,S. N=2 :u1=90,u2=82,S=272;invariant S=u0+…+uk. N=0 conserve100,100.

## DS2

- e01 :négation ∃x∈R,∀y∈R,y≤x;paramètre cf.c08-e01;√(x+6)=x impose x≥0, (x−3)(x+2)=0 ⇒x=3 seulement.
- e02 :soustraire première :y=2,z=3,t=4,x=1.840=2×360+120;360=3×120 :PGCD120,PPCM2520.45=32+8+4+1=101101₂.
- e03 :u1=8,u2=7,différences−2,−1 donc non arithmétique;v0=4,v_(n+1)=v_n/2 ⇒u_n=6+4/2^n,strictement décroissante,limite6. u_n<6,1⇔2^n>40 :n=6 (u5=6,125,u6=6,0625). Boucle u=10,n=0;tant que u≥6,1 :u=u/2+3,n=n+1;sortie6,terminaison par convergence et limite strictement sous le seuil.
