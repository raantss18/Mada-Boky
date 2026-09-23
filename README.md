# Manuel de mathématiques — Seconde (T10), Madagascar

Cette branche est consacrée exclusivement au manuel de mathématiques de
Seconde (T10). Le projet LaTeX et les PDF prêts à l'emploi se trouvent dans
[`Livres/T10`](Livres/T10).

## Éditions produites

- `main.tex` : édition élève ;
- `main-prof.tex` : édition professeur, avec guide pédagogique et corrigés.

Depuis le dossier `Livres/T10` :

```bash
make all       # les deux éditions
make student   # édition élève
make teacher   # édition professeur
make qa        # contrôles structurels
```

Les PDF suivis par Git sont disponibles dans `Livres/T10/build/`. La licence
du projet est [CC BY 4.0](LICENSE.md).
