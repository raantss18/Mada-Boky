# Terminale S graphics review — 2026-09-13

Branch: `codex/t12s-graphics-and-layout`.

## Source and scope

The author supplied `TCD-professional-source.zip` through Google Drive
(`1A_Y_u3nZqNyR2lT76Tg5eqd3qWBwvbFv`) and explicitly authorized reuse.
The exponential/logarithm drawing in `TCD/ExpoLog/Lesona.tex` is preserved in
`Livres/T12-S/figures/source-exp-ln-tcd.tex`; its adapted version is included
from `figures/exp-ln.tex` by chapter 6. The adaptation retains the source's
TikZ axes and graduation structure, uses the book palette, and pairs the
two curves in a square window with identical coordinate units.

All 33 instructional TikZ drawings included by the active 18 chapters were
rendered and visually inspected, both separately and on their student and
teacher PDF pages. The inventory records the source and PDF page locations.
Inactive duplicate chapter files are outside this build's scope.

Final deliverables: student edition, 230 pages; teacher edition, 290 pages.
Both final compilation logs contain no overfull boxes, missing-character
warnings, or undefined control sequences. The matrix-power definition was
also checked on the complete PDF page in both editions.

## Corrections

- Load `mathtools` before `unicode-math` so extensible mathematical braces
  render correctly. Check matrix powers, grouped digits, and underset notation.
- Turn the barycentre and point-to-plane distance braces toward their segments.
- Use equal coordinate units for exponential/logarithm reflection and the
  sequence construction against the diagonal.
- Expand the differential-equation viewport and red curve domain; label the
  explicit solutions for the same parameter value, `m = 1`.
- Keep the cubic and its tangents inside the intended drawing area; move
  derivative and inflection labels away from curves and axes.
- Correct the complex-product modulus and exact similarity triangle coordinates.
- Separate geometric labels from edges, correct the line/plane intersection,
  and distinguish the hidden portion of the secant.
- Mark included and excluded endpoints in the cumulative distribution graph.
- Wrap overflowing teacher-edition calculations and widen the progression
  table's first column.
- Stop compilation on LaTeX errors before copying a deliverable PDF.

## Reproduction

Requirements: XeLaTeX, latexmk, French hyphenation, TeX Gyre Pagella/Heros
(or the alternative fonts supported by the existing style), PGF/TikZ and
PGFPlots. From `Livres/T12-S`, run `./compiler.sh eleve` and then
`./compiler.sh prof` sequentially.

For a compact visual proof, run `python audit/make-proof.py` from the repository
root, then from `Livres/T12-S` run:

```sh
xelatex -halt-on-error -interaction=nonstopmode -output-directory=build build/graphics-proof.tex
```

This produces one page per instructional drawing plus a mathematical-brace
and underset proof page. Recheck the complete editions after changes that
affect figure sizes or page layout.
