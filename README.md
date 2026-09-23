# Mada-Boky

Collection de manuels et de ressources pédagogiques de mathématiques
pour le lycée à Madagascar, rédigés en LaTeX.

## Version courante : 1.1

Trois manuels de Terminale publiés, auxquels s'ajoute un manuel T10
complet, avec ses deux éditions — élève et professeur.

| Manuel | Élève | Professeur | Exercices | Devoirs surveillés |
|---|---|---|---|---|
| Terminale S | 224 p. | 286 p. | 248 + 177 d'annales | 18 |
| Terminale L | 136 p. | 170 p. | 281 + 64 d'annales | 4 |
| Terminale OSE | 178 p. | 210 p. | 159 + 85 d'annales | — |
| T10 (Seconde) | 295 p. | 469 p. | 42 exercices et 8 problèmes dans la banque | Banque modulable |

Ce que la version 1.1 apporte, en trois lignes : la série S tient désormais
sans exception la règle « pas de question avant la notion », gagne un devoir
surveillé par chapitre, un glossaire en annexe, et le corrigé des 166
exercices qui n'en avaient pas ; la série OSE voit les mathématiques
financières passer en annexe, conformément au Programme d'Études ; la série L
a sa partie « Traitement des données » restructurée.

Le détail, manuel par manuel, est dans le **[journal des versions](CHANGELOG.md)**.

## Contenu du dépôt

| Dossier | Description |
|---|---|
| `Livres/` | Sources LaTeX des manuels : `T10`, `T11-S`, `T12-S`, `T12-L`, `T12-OSE` |
| `Sujets/` | Sujets de BAC (officiels et blancs) et de concours ENI |
| `PSE/` | Programmes scolaires, répartitions annuelles et documents d'accompagnement |
| `Captures/`, `captureTsymety/` | Captures d'écran de travail |
| `Claude outputs/` | PDF compilés des versions élève et professeur |

## Compilation

Chaque livre se compile depuis son propre dossier avec le script fourni, qui
produit les deux éditions depuis la même source :

```bash
cd Livres/T12-S
./compiler.sh les-deux      # ou : eleve | prof | propre
```

Moteur : XeLaTeX via `latexmk`. Les polices Libertinus et Jost sont utilisées
si elles sont installées ; sinon la compilation bascule automatiquement sur
TeX Gyre Pagella et TeX Gyre Heros.

## Télécharger les livres (PDF)

Les versions élève et professeur des manuels sont publiées comme fichiers
téléchargeables sur la page **[Releases](https://github.com/raantss18/Mada-Boky/releases/latest)**
du dépôt — pas besoin de cloner le dépôt ni de compiler le LaTeX.

## Licence

Contenu publié sous licence **[CC BY 4.0](LICENSE.md)** : libre de copie,
d'adaptation et d'usage commercial, à condition de créditer **Mada-Boky**
avec un lien vers ce dépôt.
