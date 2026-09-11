# Mada-Boky

Collection de manuels et de ressources pédagogiques de mathématiques
pour le lycée à Madagascar, rédigés en LaTeX.

## Contenu du dépôt

| Dossier | Description |
|---|---|
| `Livres/` | Sources LaTeX des manuels : `T12-S`, `T12-L`, `T12-OSE` |
| `Sujets/` | Sujets de BAC (officiels et blancs) et de concours ENI |
| `PSE/` | Programmes scolaires, répartitions annuelles et documents d'accompagnement |
| `Captures/`, `captureTsymety/` | Captures d'écran de travail |
| `Claude outputs/` | PDF compilés des versions élève et professeur |

## Compilation

Chaque livre se compile depuis son propre dossier (`Livres/T12-S`, etc.)
avec `latexmk` ou le script de build fourni :

```bash
cd Livres/T12-S
latexmk -xelatex livre-t12s.tex
```

## Télécharger les livres (PDF)

Les versions élève et professeur des manuels sont publiées comme fichiers
téléchargeables sur la page **[Releases](https://github.com/raantss18/Mada-Boky/releases/latest)**
du dépôt — pas besoin de cloner le dépôt ni de compiler le LaTeX.

## Licence

Contenu publié sous licence **[CC BY 4.0](LICENSE.md)** : libre de copie,
d'adaptation et d'usage commercial, à condition de créditer **Mada-Boky**
avec un lien vers ce dépôt.
