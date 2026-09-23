#!/usr/bin/env python3
"""Generate one short automatism set for each planned teaching session."""

from pathlib import Path


BANKS = {
    "logic": [
        (r"Dire si « $7$ est pair » est une proposition et donner sa valeur de vérité.", r"Proposition fausse."),
        (r"Nier : « $x\geq 3$ ».", r"$x<3$."),
        (r"Nier : « $P$ et $Q$ ».", r"« non $P$ ou non $Q$ »."),
        (r"Nier : « $P$ ou $Q$ ».", r"« non $P$ et non $Q$ »."),
        (r"Donner la réciproque de $P\Rightarrow Q$.", r"$Q\Rightarrow P$."),
        (r"Donner la contraposée de $P\Rightarrow Q$.", r"$\neg Q\Rightarrow\neg P$."),
        (r"Traduire « tout réel a un carré positif ou nul ».", r"$\forall x\in\R,\ x^2\geq0$."),
        (r"Nier : $\forall x\in\R,\ x^2\geq1$.", r"$\exists x\in\R,\ x^2<1$."),
        (r"La phrase « $x+2=5$ » est-elle une proposition lorsque $x$ n'est pas fixé ?", r"Non : c'est un prédicat."),
        (r"Compléter : $P\Leftrightarrow Q$ signifie $P\Rightarrow Q$ et \ldots", r"$Q\Rightarrow P$."),
        (r"Donner un contre-exemple à « tout nombre premier est impair ».", r"$2$."),
        (r"Si $P$ est vraie et $Q$ fausse, donner la valeur de $P\land Q$.", r"Fausse."),
        (r"Si $P$ est vraie et $Q$ fausse, donner la valeur de $P\lor Q$.", r"Vraie."),
        (r"Nier : « il existe un entier pair supérieur à $10$ ».", r"Tout entier supérieur à $10$ est impair."),
        (r"Écrire « $2$ est l'unique solution » avec le symbole $\exists!$.", r"$\exists!x,\ x=2$."),
        (r"La négation de $x\neq0$ est-elle $x=0$ ?", r"Oui."),
    ],
    "algo": [
        (r"Après $x\leftarrow4$ puis $x\leftarrow2x-1$, que vaut $x$ ?", r"$7$."),
        (r"Après $a\leftarrow3$, $b\leftarrow5$, $a\leftarrow b$, que vaut $a$ ?", r"$5$."),
        (r"Que teste la condition $n\bmod2=0$ ?", r"Si $n$ est pair."),
        (r"Combien de fois s'exécute une boucle « Pour $i$ de $1$ à $6$ » ?", r"$6$ fois."),
        (r"Avec $S\leftarrow0$, puis $S\leftarrow S+3$ répété quatre fois, donner $S$.", r"$12$."),
        (r"Dans un organigramme, quelle forme représente un test ?", r"Un losange."),
        (r"Dans un organigramme, quelle forme représente un traitement ?", r"Un rectangle."),
        (r"Après $x\leftarrow-2$, afficher $x^2+1$.", r"$5$."),
        (r"Si $x=7$, le test $x<5$ est-il vrai ?", r"Non."),
        (r"Avec $i\leftarrow1$, puis tant que $i<5$, $i\leftarrow i+1$, donner la valeur finale.", r"$5$."),
        (r"Différencier en un mot « Lire $x$ » et « Afficher $x$ ».", r"Entrée; sortie."),
        (r"Après $a\leftarrow2$, $b\leftarrow a+3$, $a\leftarrow b^2$, donner $(a,b)$.", r"$(25,5)$."),
        (r"Une boucle Tant que peut-elle ne jamais s'arrêter ?", r"Oui, si sa condition reste vraie."),
        (r"Donner l'instruction qui augmente $k$ de $1$.", r"$k\leftarrow k+1$."),
        (r"Que vaut $17\bmod5$ ?", r"$2$."),
        (r"Que vaut le quotient entier de $17$ par $5$ ?", r"$3$."),
    ],
    "numbers": [
        (r"Simplifier $\dfrac{42}{56}$.", r"$\dfrac34$."),
        (r"Calculer $2^{-3}$.", r"$\dfrac18$."),
        (r"Écrire $0{,}00072$ en notation scientifique.", r"$7{,}2\times10^{-4}$."),
        (r"Encadrer $\sqrt{20}$ entre deux entiers consécutifs.", r"$4<\sqrt{20}<5$."),
        (r"Traduire $|x-3|\leq2$ par un intervalle.", r"$x\in[1;5]$."),
        (r"Calculer $\dfrac34-\dfrac16$.", r"$\dfrac7{12}$."),
        (r"Simplifier $\sqrt{75}$.", r"$5\sqrt3$."),
        (r"Calculer $3^2\times3^{-4}$.", r"$\dfrac19$."),
        (r"Donner $[-2;5[\cap[1;8]$.", r"$[1;5[$."),
        (r"Donner $]-\infty;3]\cup[1;6[$.", r"$]-\infty;6[$."),
        (r"Classer $-\dfrac58$ dans le plus petit ensemble usuel.", r"$\D$."),
        (r"Comparer $\sqrt{11}$ et $\dfrac72$.", r"$\sqrt{11}<\dfrac72$."),
        (r"Calculer $|{-4}-3|$.", r"$7$."),
        (r"Résoudre $|x|=6$.", r"$x=-6$ ou $x=6$."),
        (r"Écrire $\dfrac13$ avec une précision de $10^{-2}$.", r"$0{,}33$ au centième."),
        (r"Calculer $(2^3)^2$.", r"$64$."),
        (r"Rationaliser $\dfrac1{\sqrt5}$.", r"$\dfrac{\sqrt5}{5}$."),
        (r"Résoudre $|x+1|<3$.", r"$x\in]-4;2[$."),
        (r"Donner un encadrement décimal de $\sqrt2$ au dixième.", r"$1{,}4<\sqrt2<1{,}5$."),
        (r"Calculer $\dfrac{5}{12}+\dfrac14$.", r"$\dfrac23$."),
    ],
    "lines": [
        (r"Donner un vecteur directeur de $2x-3y+5=0$.", r"$(3;2)$."),
        (r"Donner un vecteur normal à $4x+y-2=0$.", r"$(4;1)$."),
        (r"La droite $x=3$ a-t-elle un coefficient directeur ?", r"Non."),
        (r"Vérifier si $A(1;2)$ appartient à $x+y-3=0$.", r"Oui."),
        (r"Donner la pente de la droite passant par $(1;2)$ et $(3;6)$.", r"$2$."),
        (r"Écrire la droite de pente $3$ passant par $(0;-2)$.", r"$y=3x-2$."),
        (r"Donner une droite parallèle à $y=-2x+1$.", r"Par exemple $y=-2x+4$."),
        (r"Donner la pente d'une droite perpendiculaire à $y=\dfrac12x+3$.", r"$-2$."),
        (r"Transformer $y=3x-5$ en forme cartésienne.", r"$3x-y-5=0$."),
        (r"Déterminer l'ordonnée à l'origine de $2x+y-7=0$.", r"$7$."),
        (r"Les droites $y=4x+1$ et $y=4x-6$ sont-elles parallèles ?", r"Oui."),
        (r"Donner une équation de la droite passant par $(2;1)$ et verticale.", r"$x=2$."),
        (r"Calculer le milieu de $(1;3)$ et $(5;-1)$.", r"$(3;1)$."),
        (r"Calculer la distance entre $(0;0)$ et $(3;4)$.", r"$5$."),
    ],
    "quadratic": [
        (r"Calculer le discriminant de $x^2-5x+6$.", r"$\Delta=1$."),
        (r"Résoudre $x^2-5x+6=0$.", r"$x=2$ ou $x=3$."),
        (r"Factoriser $2x^2+4x+2$.", r"$2(x+1)^2$."),
        (r"Donner la forme canonique de $x^2-6x+5$.", r"$(x-3)^2-4$."),
        (r"Résoudre $(x-3)(x+4)\leq0$.", r"$x\in[-4;3]$."),
        (r"Donner le signe de $(x-2)(x+1)$ pour $x>2$.", r"Positif."),
        (r"Résoudre $x^2-9=0$.", r"$x=-3$ ou $x=3$."),
        (r"Factoriser $x^2+x-6$.", r"$(x+3)(x-2)$."),
        (r"Donner le sommet de $x^2-4x+1$.", r"$S(2;-3)$."),
        (r"Combien de racines réelles si $\Delta<0$ ?", r"Aucune."),
        (r"Combien de racines réelles si $\Delta=0$ ?", r"Une racine double."),
        (r"Vérifier si $2$ est racine de $x^3-3x^2-4x+12$.", r"Oui."),
        (r"Factoriser $x^3-4x$.", r"$x(x-2)(x+2)$."),
        (r"Donner les valeurs interdites de $\dfrac{x+1}{x^2-4}$.", r"$-2$ et $2$."),
        (r"Résoudre $\dfrac{x-1}{x+2}=0$.", r"$x=1$."),
        (r"Donner le signe de $-2(x-1)^2$.", r"Négatif ou nul."),
        (r"Résoudre $x^2+4x+4>0$.", r"$\R\setminus\{-2\}$."),
        (r"Développer $(x-4)^2$.", r"$x^2-8x+16$."),
    ],
    "circle": [
        (r"Écrire le cercle de centre $(2;-1)$ et de rayon $3$.", r"$(x-2)^2+(y+1)^2=9$."),
        (r"Donner le centre de $x^2+y^2-4x+6y=0$.", r"$(2;-3)$."),
        (r"Le point $(3;4)$ appartient-il à $x^2+y^2=25$ ?", r"Oui."),
        (r"Donner le rayon de $(x-1)^2+(y+2)^2=16$.", r"$4$."),
        (r"Combien de points communs ont une droite tangente et un cercle ?", r"Un."),
        (r"Si $d(\Omega,\Delta)>r$, quelle est la position de la droite ?", r"Extérieure."),
        (r"Si $d(\Omega,\Delta)<r$, quelle est la position de la droite ?", r"Sécante."),
        (r"La tangente en $A$ est perpendiculaire à quel segment ?", r"Au rayon $[\Omega A]$."),
        (r"Calculer $d((0;0),(6;8))$.", r"$10$."),
        (r"Donner l'équation du cercle de diamètre $[AB]$, avec $A(-2;0)$ et $B(2;0)$.", r"$x^2+y^2=4$."),
        (r"Deux cercles ont $r_1=3$, $r_2=2$, $d=5$. Leur position ?", r"Tangents extérieurement."),
        (r"Deux cercles ont $r_1=5$, $r_2=2$, $d=1$. Leur position ?", r"L'un est intérieur à l'autre."),
        (r"Compléter le carré : $x^2-6x=(x-3)^2-\ldots$", r"$9$."),
        (r"Donner une équation de la tangente à $x^2+y^2=25$ en $(5;0)$.", r"$x=5$."),
    ],
    "functions": [
        (r"Si $f(x)=x^2-2x$, calculer $f(-1)$.", r"$3$."),
        (r"Donner le domaine de $x\mapsto\sqrt{x-3}$.", r"$[3;+\infty[$."),
        (r"La fonction carré est-elle paire ?", r"Oui."),
        (r"Donner le minimum de $(x-2)^2+1$.", r"$1$, atteint en $2$."),
        (r"Résoudre $|x|=5$.", r"$x=-5$ ou $x=5$."),
        (r"La fonction cube est-elle croissante sur $\R$ ?", r"Oui."),
        (r"Calculer l'image de $-2$ par $x\mapsto x^3$.", r"$-8$."),
        (r"Donner le domaine de $x\mapsto\dfrac1{x-4}$.", r"$\R\setminus\{4\}$."),
        (r"Résoudre $\sqrt{x}=3$.", r"$x=9$."),
        (r"Comparer $(-3)^2$ et $(-2)^2$.", r"$9>4$."),
        (r"Si $a<b$ et $f$ est croissante, comparer $f(a)$ et $f(b)$.", r"$f(a)\leq f(b)$."),
        (r"Donner le sommet de $x\mapsto-(x+1)^2+4$.", r"$(-1;4)$."),
        (r"Résoudre $|x-2|\leq3$.", r"$x\in[-1;5]$."),
        (r"Calculer $f(0)$ pour $f(x)=\sqrt{x+4}$.", r"$2$."),
        (r"La fonction racine carrée est-elle définie en $-1$ ?", r"Non."),
        (r"Donner les zéros de $(x-1)^2-9$.", r"$-2$ et $4$."),
        (r"Une fonction impaire vérifie quelle relation ?", r"$f(-x)=-f(x)$."),
        (r"Donner l'image de $3$ par $x\mapsto|x-5|$.", r"$2$."),
    ],
    "trig": [
        (r"Convertir $180^\circ$ en radians.", r"$\pi$."),
        (r"Convertir $\dfrac{\pi}{3}$ en degrés.", r"$60^\circ$."),
        (r"Donner $\cos0$ et $\sin0$.", r"$1$ et $0$."),
        (r"Donner $\cos\dfrac{\pi}{2}$ et $\sin\dfrac{\pi}{2}$.", r"$0$ et $1$."),
        (r"Compléter : $\cos^2x+\sin^2x=\ldots$", r"$1$."),
        (r"Donner $\cos\dfrac{\pi}{3}$.", r"$\dfrac12$."),
        (r"Donner $\sin\dfrac{\pi}{6}$.", r"$\dfrac12$."),
        (r"Réduire $\dfrac{13\pi}{6}$ modulo $2\pi$.", r"$\dfrac{\pi}{6}$."),
        (r"Quelle est la parité du cosinus ?", r"Paire."),
        (r"Quelle est la parité du sinus ?", r"Impaire."),
        (r"Convertir $150^\circ$ en radians.", r"$\dfrac{5\pi}{6}$."),
        (r"Donner $\cos\pi$ et $\sin\pi$.", r"$-1$ et $0$."),
        (r"Si $\sin x=\dfrac35$ et $x$ est dans le premier quadrant, donner $\cos x$.", r"$\dfrac45$."),
        (r"Donner une mesure positive de l'angle $-\dfrac{\pi}{2}$ modulo $2\pi$.", r"$\dfrac{3\pi}{2}$."),
        (r"Dans quel quadrant se trouve $\dfrac{3\pi}{4}$ ?", r"Deuxième quadrant."),
        (r"Donner la période du sinus.", r"$2\pi$."),
    ],
    "vectors": [
        (r"Pour $A(1;2)$ et $B(4;-2)$, donner $\vv{AB}$.", r"$(3;-4)$."),
        (r"Donner le milieu de $A(1;2)$ et $B(4;-2)$.", r"$\left(\dfrac52;0\right)$."),
        (r"Les vecteurs $(2;3)$ et $(4;6)$ sont-ils colinéaires ?", r"Oui."),
        (r"Calculer $(2;-1)\cdot(3;4)$.", r"$2$."),
        (r"Les vecteurs $(1;2)$ et $(-4;2)$ sont-ils orthogonaux ?", r"Oui."),
        (r"Calculer la norme de $(3;4)$.", r"$5$."),
        (r"Compléter : $\vv{AB}+\vv{BC}=\ldots$", r"$\vv{AC}$."),
        (r"Donner un vecteur colinéaire à $(3;-2)$.", r"Par exemple $(6;-4)$."),
        (r"Calculer le déterminant de $(2;1)$ et $(3;4)$.", r"$5$."),
        (r"Si $\vec u\cdot\vec v=0$ et les vecteurs sont non nuls, que conclure ?", r"Ils sont orthogonaux."),
        (r"Si $\vv{AB}=\vv{DC}$, quelle figure est $ABCD$ ?", r"Un parallélogramme."),
        (r"Donner les coordonnées du centre de gravité de $(0;0)$, $(3;0)$, $(0;6)$.", r"$(1;2)$."),
        (r"Calculer $(1;3)\cdot(-3;1)$.", r"$0$."),
        (r"Les points $(0;0)$, $(2;3)$, $(4;6)$ sont-ils alignés ?", r"Oui."),
        (r"Donner $\vv{BA}$ si $\vv{AB}=(5;-2)$.", r"$(-5;2)$."),
        (r"Calculer $\|(1;-2)\|^2$.", r"$5$."),
        (r"Que vaut $\vec u\cdot\vec u$ ?", r"$\|\vec u\|^2$."),
        (r"Donner le point $D$ tel que $ABCD$ soit un parallélogramme, avec $A(0;0)$, $B(2;0)$, $C(3;1)$.", r"$D(1;1)$."),
    ],
    "stats": [
        (r"Calculer la moyenne de $2,4,6,8$.", r"$5$."),
        (r"Donner la médiane de $1,3,3,7,9$.", r"$3$."),
        (r"Donner la médiane de $1,3,7,9$.", r"$5$."),
        (r"Calculer la fréquence de $12$ élèves parmi $30$.", r"$0{,}4=40\%$."),
        (r"Quelle est la variance de $5,5,5,5$ ?", r"$0$."),
        (r"L'écart-type peut-il être négatif ?", r"Non."),
        (r"Quel graphique convient à des données continues regroupées en classes ?", r"Un histogramme."),
        (r"Si on ajoute $3$ à toutes les valeurs, comment change la moyenne ?", r"Elle augmente de $3$."),
        (r"Donner l'étendue de $4,7,9,12$.", r"$8$."),
        (r"Donner le mode de $2,3,3,3,5,6$.", r"$3$."),
        (r"Calculer la moyenne pondérée de $10$ (coef. $2$) et $16$ (coef. $1$).", r"$12$."),
        (r"Si toutes les valeurs sont multipliées par $2$, comment change l'étendue ?", r"Elle est multipliée par $2$."),
        (r"Quel quartile correspond à la médiane ?", r"$Q_2$."),
        (r"La somme des fréquences d'une série vaut combien ?", r"$1$ ou $100\%$."),
        (r"Donner l'effectif total des effectifs $4,7,5,4$.", r"$20$."),
        (r"Une fréquence de $0{,}35$ correspond à quel pourcentage ?", r"$35\%$."),
        (r"Quel indicateur est le plus sensible à une valeur extrême : moyenne ou médiane ?", r"La moyenne."),
        (r"Une série a variance $9$. Donner son écart-type.", r"$3$."),
    ],
}


SESSIONS = [
    ("Énoncés, propositions et vérité", "logic"), ("Connecteurs et négation", "logic"),
    ("Implication et équivalence", "logic"), ("Quantificateurs et négations", "logic"),
    ("Variables et affectation", "algo"), ("Lire un pseudo-code", "algo"),
    ("Conditions", "algo"), ("Boucles et organigrammes", "algo"),
    ("Ensembles de nombres", "numbers"), ("Fractions et puissances", "numbers"),
    ("Racines carrées et ordre", "numbers"), ("Intervalles et valeur absolue", "numbers"),
    ("Équations de droites", "lines"), ("Forme paramétrique d'une droite", "lines"),
    ("Écritures approchées", "numbers"), ("Encadrements et propagation", "numbers"),
    ("Forme canonique", "quadratic"), ("Discriminant", "quadratic"),
    ("Résolution du second degré", "quadratic"), ("Factorisation du trinôme", "quadratic"),
    ("Signe du trinôme", "quadratic"), ("Inéquations du second degré", "quadratic"),
    ("Polynôme avec une racine connue", "quadratic"), ("Division et identification", "quadratic"),
    ("Signe d'un produit", "quadratic"), ("Équations rationnelles", "quadratic"),
    ("Équations de cercles", "circle"), ("Intersection droite-cercle", "circle"),
    ("Domaine et image d'une fonction", "functions"), ("Lecture graphique", "functions"),
    ("Variations et extremum", "functions"), ("Parité", "functions"),
    ("Fonction carré", "functions"), ("Fonction cube", "functions"),
    ("Valeur absolue", "functions"), ("Racine carrée", "functions"),
    ("Degrés et radians", "trig"), ("Cercle trigonométrique", "trig"),
    ("Angles remarquables", "trig"), ("Relation fondamentale", "trig"),
    ("Parité et périodicité", "trig"), ("Fonctions et trigonométrie", "trig"),
    ("Courbes de référence", "functions"), ("Tableaux de variation", "functions"),
    ("Problèmes sur les fonctions", "functions"), ("Pratique mixte", "mixed"),
    ("Vecteurs : direction et norme", "vectors"), ("Égalité et opérations", "vectors"),
    ("Coordonnées et milieu", "vectors"), ("Colinéarité", "vectors"),
    ("Alignement et parallélisme", "vectors"), ("Produit scalaire", "vectors"),
    ("Orthogonalité", "vectors"), ("Problèmes vectoriels", "vectors"),
    ("Population et variable", "stats"), ("Effectifs et fréquences", "stats"),
    ("Moyenne et médiane", "stats"), ("Variance et écart-type", "stats"),
    ("Diagrammes en bâtons et circulaires", "stats"), ("Histogramme", "stats"),
    ("Interpréter une représentation", "stats"), ("Problème statistique", "stats"),
    ("Révisions mixtes I", "mixed"), ("Révisions mixtes II", "mixed"),
    ("Remédiation ciblée", "mixed"), ("Approfondissement et recherche", "mixed"),
]


def choose(category: str, seed: int):
    if category == "mixed":
        cats = ["numbers", "quadratic", "functions", "vectors", "stats"]
        return [BANKS[cat][(seed * 3 + i) % len(BANKS[cat])] for i, cat in enumerate(cats)]
    bank = BANKS[category]
    questions = [bank[(seed * 4 + i) % len(bank)] for i in range(4)]
    if category == "numbers":
        questions.append(BANKS["logic"][(seed + 5) % len(BANKS["logic"])])
    else:
        questions.append(BANKS["numbers"][(seed * 2 + 3) % len(BANKS["numbers"])])
    return questions


def render() -> str:
    lines = [
        r"\part{Automatismes et évaluations}",
        r"\chapter{Automatismes de chaque séance}",
        "",
        r"Chaque série est prévue pour 8 à 10 minutes, sans calculatrice sauf indication.",
        r"Elle associe la notion du jour à une question de rappel. Dans l'édition",
        r"professeur, les réponses apparaissent immédiatement sous la série.",
        "",
    ]
    for index, (title, category) in enumerate(SESSIONS):
        week = index // 2 + 1
        letter = "A" if index % 2 == 0 else "B"
        qa = choose(category, index)
        lines.extend([
            rf"\section{{Semaine {week}, séance {letter} -- {title}}}",
            r"\begin{enumerate}",
        ])
        lines.extend(rf"  \item {question}" for question, _ in qa)
        lines.append(r"\end{enumerate}")
        answers = r" \quad ".join(rf"\textbf{{{i}.}} {answer}" for i, (_, answer) in enumerate(qa, 1))
        lines.extend([
            r"\TeacherOnly{%",
            r"\begin{tcolorbox}[colback=VE!3,colframe=VE!35,boxrule=.4pt,arc=1mm]",
            r"\small\textit{Réponses.}\quad " + answers,
            r"\end{tcolorbox}}",
            "",
        ])
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    target = root / "assessments" / "automatismes.tex"
    target.write_text(render(), encoding="utf-8")
    print(f"Generated {len(SESSIONS)} session sets in {target}")
