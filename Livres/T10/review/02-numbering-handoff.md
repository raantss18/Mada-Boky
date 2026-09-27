# T10 — automatic numbering follow-up (23 September 2026)

This folder is a temporary Drive copy. GitHub `raantss18/Mada-Boky`, branch `main`, remains the authoritative source. The copy starts from GitHub commit `4b03ba2705352ca22d2cd6af86a2426e7b859bf2`, includes the locally committed assessment-link fix `c593653d18e52d0de4c36f65aa47b1d5b6909c36`, and adds the numbering changes listed below. These latter changes have **not** been pushed to GitHub.

| ID | Location | Severity | Problem | Action | Status | Confidence |
|---|---|---|---|---|---|---|
| N01 | `solutions/01`–`09`, `styles/mdg-pedagogy.sty` | Major | Correction headings repeated chapter and item numbers manually. | Generate numbers from independent solution counters; print the corresponding statement's `\ref*`; keep clickable statement links. | FIXED | High |
| N02 | `solutions/01`–`09`, `teacher/guide-professeur.tex` | Minor | Chapter numbers in correction section headings and section numbers in the teacher guide were typed literally. | Derive both from counters without changing the visible sequence. | FIXED | High |
| N03 | `assessments/corrections.tex` | Major | The correction bank encoded `42` and `8` as offsets and switched type at item 43. | Save the statement counters at bank start; use separate automatically numbered exercise/problem answer commands. | FIXED | High |
| N04 | Cross-references in chapters 1–3 and solutions 1, 3, 5 | Minor | A few references displayed fixed exercise or chapter numbers. | Use labelled `\ref` references; make exercise and problem counters referenceable. | FIXED | High |
| N05 | Chapter 8 exercises and `styles/mdg-pedagogy.sty` | Major | Three trigonometry statements had corrections but omitted their link; two exercise backlink anchors landed on the preceding page at a page break. | Added the three links, attached exercise anchors to their visible heading lines, and added a QA check for missing correction markers. | FIXED | High |

The difficulty labels “Niveau 1–3”, numbered exercise subquestions, week/session labels and numerical mathematical content are intentionally retained: they are categories, lists or values rather than manually duplicated document numbering.

The unresolved mathematical and programme questions remain in `01-sol-audit.md` (U01–U04). That historical report also shows U05–U06 as unresolved **at the time of the first pass**; N01–N02 above resolve them in this Drive snapshot.

**Verification:** `python3 scripts/qa.py` passed (42 TeX modules), and `make all` compiled 295 student and 471 teacher pages. The final logs contain no undefined references, duplicate labels or fatal errors. A PDF-level check found exactly 600 labelled statement–solution pairs; all 600 have a forward link and backlink on the matching pages, and all reference numbers agree with their labels. Rendered exercise pages at the two former page breaks and the bank-correction page were inspected.
