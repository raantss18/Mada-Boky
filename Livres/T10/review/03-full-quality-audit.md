# T10 — full quality audit against the official programme (2 October 2026)

**Authority:** GitHub `raantss18/Mada-Boky`, branch `main` (see `README-DRIVE-SNAPSHOT.md`, updated today).
**Scope:** `Livres/T10` as committed (`814ac40` plus the one-line authority change). Not a re-proofreading of every exercise: Pass 1 and Pass 2 (`01-sol-audit.md`, `02-astra-audit.md`) already did that. This pass asks a different question: **does the book teach what the official programme requires, in a usable order, and do its own documents tell the truth about it?**

## 1. Official curriculum — found

| Document | Location in repo | What it is |
|---|---|---|
| **PE T10** (Programme d'Études, MEN, "GITA", PDF created 4 Sept 2026) | `PSE/PE-2026/PE_T10.pdf` (byte-identical copy in `PSE/RAPE 2026/PE_T10.pdf`) | Whole T10 programme, all subjects. **Mathematics = printed pp. 118–129**: general aims, 4 components, specific learning outcomes, contents, suggested activities, evaluation criteria. |
| **RAPE 2nde 2025-2026** (Répartition annuelle, MEN, Aug 2025) | `PSE/Répartitions 2025 2026/RAPE_T10_2025_2026.pdf`, maths on printed pp. 26–29 | Contents per period (5 periods). Stated as *mandatory* for experimental public schools and the basis of official exam papers. |
| Older: Programme 2nde (2019), RAPE 2021-22 | `PSE/Programmes/`, `PSE/Répartitions 2021 2022/` | Historical. |
| **RAPE T10 GENERALISATION, août 2026** | **not in the repository** | Cited by `docs/audit-programme-evaluations.md` and by Pass 2 from a Drive link. Could not be read here. **[VERIFY]** If it differs from the 2025-26 RAPE, add it to `PSE/` and re-run section 3. |

Programme content (PE), with hours: **Analyse 62 h** (ℝ, intervals/absolute value, encadrements, trinôme/cubic/rational equations, reference functions), **Algèbre 16 h** (logic, algorithmics), **Géométrie 40 h** (lines, circles, line–circle intersection, trigonometric circle, vectors incl. scalar product), **Traitement de données 10 h** (discrete/continuous, median, mean, variance, standard deviation, bar/histogram/pie charts). Total 128 h = 32 weeks × 4 h.
Neither document lists probability, sequences, derivatives or limits.

[VERIFY] The PE contradicts itself on weekly hours: the general table (p. 9) gives Mathématiques T10 = 5 h, the mathematics page says "VOLUME HORAIRE : 4 heures", and the RAPE says 4 h. The book uses 4 h; that matches the subject page and the RAPE.

## 2. What was verified, and how

| Check | Result |
|---|---|
| `make qa` | Passes (42 modules). The script checks numbering, 66 automatism series, ≥42 exercises, ≥8 problems. **It does not check programme coverage.** |
| Fresh build, both editions (pdfLaTeX, TeX Live 2023) | Succeeds. **299 student / 479 teacher pages**, identical to the committed PDFs. 0 overfull hbox; 2 overfull vbox (teacher); font-shape warnings only; 0 undefined references. |
| GitHub Actions `build-t10.yml` | Last 5 runs, including `814ac40` on `main`: success. |
| Published PDFs vs sources | Same page counts and date (24 Sept) as Pass 2. |
| Visual check of Ch. 7 pages 174–178 | Confirms finding C07 below. |
| Spot-check of mathematics (Ch. 4, "Niveau 1" corrections: discriminant, canonical forms, quadratic inequalities, Viète, cubic factorisations, rational domains, 2×2 systems, sign tables; all ~40 items re-derived by hand) | **No error found.** Worked examples in Ch. 3–4 (rationalisation, sign tables, polynomial division) re-derived: correct. |
| Assessment bank scanned for out-of-programme keywords | Clean, as the guide claims. |
| Anecdotes (dates) | Consistent, except the two flagged in D05. |

Not done: line-by-line re-verification of all ~1 100 exercises and 139 problems; independent classroom trial.

## 3. Programme conformity findings (course text vs PE/RAPE)

Severity: **Major** = a required item is missing from the course or wrongly labelled optional; **Moderate** = partial/misplaced; **Minor** = editorial. "Course" means the theory part of a chapter, not its exercises.

| ID | Location | Sev. | Finding | Programme source |
|---|---|---|---|---|
| C01 | Ch. 3 §3.1 | Major | The chain taught is ℕ⊂ℤ⊂ℚ⊂ℝ. **𝔻 (décimaux) is never defined.** The macro `\D` exists, the entry activity (`activities/03`) and the teacher guide (week 5) use 𝔻, the course omits it. | PE: "établir que ℕ⊂ℤ⊂𝔻⊂ℚ⊂ℝ" |
| C02 | Ch. 3 | Major | No course on the different writings of a real: écriture décimale d'ordre n, valeur arrondie, valeur approchée, notation scientifique. Scientific notation appears only in exercises; "arrondi" appears nowhere in the book. | PE (écriture décimale/fractionnaire/scientifique); RAPE P1 |
| C03 | Ch. 3 §3.4 | Major | "Encadrer un réel" teaches only √n between consecutive integers. **No rules for encadrer a sum, difference, product, quotient** (the PE's whole learning outcome "Mettre en œuvre les techniques des encadrements"). Guide week 8 ("Encadrements et propagation") has no matching course text. | PE; RAPE P1 |
| C04 | Ch. 4 §4.6 | Major | Linear systems are tagged `\horsprogramme` ("Consolidation facultative") and the guide calls them an extension. The RAPE 2025-26 (P2) lists **systems of two equations in two unknowns (graphical and algebraic) and systems of two inequalities (graphical)**. The label contradicts the RAPE; the graphical resolution is not taught anywhere. | RAPE P2 |
| C05 | Ch. 4 | Major | Missing from the course: (a) **solving rational equations** (valeurs interdites, A/B = C/D, rational inequalities — only simplification and sign tables are taught); (b) **solving cubic equations/inequalities** as a method (only factorisation + sign table); (c) tricks for an **évidente root**; (d) a stated method for **second-degree inequalities**; (e) the sign theorem covers only *a* > 0 (the *a* < 0 and Δ = 0, Δ < 0 strict cases are absent from the statement). | PE learning outcome 3; RAPE P2 |
| C06 | Ch. 4 | Moderate | Order is discriminant → sign → **canonical form** last, although the discriminant formulas are derived from the canonical form. The theorem is stated without proof. | RAPE P2 (canonical form first) |
| C07 | Ch. 7 | Major (editorial) | **Duplicated and scrambled sections.** 7.2 "Fonctions de référence" holds only a figure and is followed by the red "Hors programme" box; 7.3 "Transformations" (marked optional) repeats, with the same *Proposition*, in 7.6 "Transformations de courbes" (not marked). The actual reference-function table is in 7.5, after definitions, whereas 7.2 comes before them. A student sees the same content twice, and optional content twice with different status. | — |
| C08 | Ch. 7 | Major | RAPE lists six reference functions: **ax+b, x², 1/x, √x, \|x\|, x³**. The PE lists four. The book makes ax+b an exercise only and 1/x a table row; the guide treats both as "consolidation". Since the RAPE is the document that drives exams, ax+b and 1/x should be core. **[VERIFY against RAPE août 2026.]** | RAPE P3 vs PE |
| C09 | Ch. 6 | Major | **Parametric equations of a circle are absent** (PE: "Equations paramétriques d'un cercle", "modéliser un mouvement circulaire"). The circle of diameter [AB] (RAPE) is only an exercise. | PE; RAPE P4 |
| C10 | Ch. 6 | Major | Line–circle intersection: the course gives only the distance criterion. The programme requires analytic resolution (substitute and solve the system); this appears only in exercises. Also absent from the course: converting between cartesian/reduced/parametric forms, the direction vector read from an equation, equations of altitude and median (only the médiatrice is worked). | PE; RAPE P3–4 |
| C11 | Ch. 8 | Major | **Parity and periodicity of trigonometric functions** are not stated as results (only inside a symmetry table); no period of tan; the guide has a week for it (week 21). | PE "Fonctions trigonométriques: parité, périodicité" |
| C12 | Ch. 8 §8.4 | Moderate | The whole section "Résolution d'équations trigonométriques" is labelled hors programme. The PE's activity "préciser les mesures des angles connaissant son cosinus et/ou son sinus" corresponds to the basic cos x = a, sin x = a on [0, 2π]. The label is too broad. | PE |
| C13 | Ch. 8 §8.2–8.3 | Moderate | The values table and the theorem cos²+sin²=1 come *before* cos/sin are defined on the circle (§8.3); the theorem has no one-line proof (M lies on the unit circle). | — |
| C14 | Ch. 9 | Major | The course never **defines discrete vs continuous variable**, classes, or class centre (only a remark); **no construction rules** for bar chart, histogram, pie chart (angle = 360°×f) — they appear only in exercises. Yet the objectives list them and the guide has weeks 28 and 30 on them. Quartiles are marked optional in §9.1 but listed unmarked in the grouped-series definition ("Q₁ (25%), Q₃ (75%)"), with a different rank convention. | PE; RAPE P4–5 |
| C15 | Ch. 1 | Major | The course states **neither De Morgan's laws, nor ¬(P⇒Q), nor the converse as a definition, nor exclusive OR**, nor how to translate sentences into formulas. The objectives promise "Former la négation et la réciproque d'une implication"; De Morgan appears only as a question inside Exercise 3. The RAPE names "OU (inclusif/exclusif)". The truth table appears twice (definition and figure). | PE; RAPE P1 |
| C16 | Ch. 2 | Moderate | The course has **no worked loop** (`Pour`, `Tant que`): the only worked algorithm is a conditional. "Boucles" is a programme item. "Complexité, efficacité, validité" (RAPE) get one remark. | PE; RAPE P1 |
| C17 | Ch. 5 | Moderate | Sequencing: "Produit scalaire" (§5.2) uses coordinates before §5.4 defines the frame; geometric operations (‖λu‖ = \|λ\|‖u‖, sense) and u = kv are missing; the programme item "Vecteurs et parallélisme de droites" has no statement. The barycentre/centre-of-gravity proposition is not in the programme and unmarked. | RAPE P1–2 |

## 4. Scope and structure findings

| ID | Finding | Sev. |
|---|---|---|
| S01 | **Order differs from the RAPE.** RAPE: logic, algorithmics, ℝ, vectors (P1) → equations, collinearity/scalar product (P2) → functions, lines (P3) → statistics, circles (P4) → statistics charts, trigonometry (P5). Book: vectors, lines+circles, functions, trigonometry, then all statistics last. The RAPE is mandatory in experimental schools; a teacher following it cannot use the chapters in order. | Moderate |
| S02 | **The teacher guide's progression is not the chapter order, and has a prerequisite error.** Week 7 teaches the *parametric equation of a line* (direction vector) 17 weeks before vectors (weeks 24–27). Statistics get 4 weeks (16 h) against 10 h in the programme. | Moderate |
| S03 | **Unmarked out-of-programme items.** Chapters 3 and 5 contain zero optional markers outside the "Défi" boxes, yet include homothety, barycentre, regression (Ch. 5), Thalès in coordinates, Simpson's paradox, axe radical, Horner, Collatz, tri fusion, RLE, Fibonacci. A keyword scan of exercise and problem titles and bodies (ad-hoc script, not committed) finds ~25 candidates carrying no `\ExtensionTTen` mark (examples: Ch. 6 "Axe radical de deux cercles", Ch. 5 "Barycentre et partage d'un segment", Ch. 2 "Algorithme de Horner", Ch. 9 "Paradoxe de Simpson"). The book's own audit says these must not be evaluated; the student cannot tell. This is Pass 2's open item **P2-U02**, still open. | Major |
| S04 | The automatism series (week 1B: contrapositive; two series: "quartile correspondant à la médiane") use items the book itself classes as optional. | Minor |
| S05 | Sections added to Ch. 3–9 as "Logique & Algorithmes" (≈ 150–250 lines each) are large relative to the course (≈ 100–300 lines per chapter). Course : exercises ratio is roughly 1 : 4. For a textbook, the *course* is the thinnest part. | Moderate |

## 5. Documentation and hygiene

| ID | Finding | Sev. |
|---|---|---|
| D01 | **`docs/audit-programme-evaluations.md` declares every domain "Conforme"** (matrix). Section 3 above shows it is not: items C01–C03, C05, C09–C11, C14 are missing from the course. It also lists "systèmes linéaires" and "fonction inverse" as outside T10, contradicting the RAPE (C04, C08), and says "le dossier courant ne contient pas de sous-dossier `PSE/`", which was a Drive statement and is false in this repository. **Should be rewritten, not just amended.** | Major |
| D02 | Stale figures: `README.md` says 289 / 459 pages; `docs/validation.md` says 303 / 475 (and "20 September"); actual 299 / 479. | Minor |
| D03 | `README.md` documents `sources/manuel_seconde_predecesseur.tex` and a `sources/` folder; **it does not exist** in `Livres/T10`. | Minor |
| D04 | `chapters/08-trigonometrie.tex` lines 34–~135: an `\iffalse … \fi` block of dead figure code (~100 lines). | Minor |
| D05 | Content to **[VERIFY]**: (a) Ch. 9 anecdote attributes to Nicolas Bernoulli the remark "Cela n'était déjà pas inconnu aux sots"; the "even the stupidest man knows…" remark is, as far as I know, from Jakob Bernoulli's own *Ars conjectandi*; the anecdote is also about probability, which is outside T10. (b) Ch. 4: al-Khwārizmī's *Kitāb al-mukhtaṣar* is dated "830"; sources usually give c. 820. (c) Guide: EEF review "plus de 3 000 études" — not checked. | Minor |
| D06 | Spelling: "Irrationnalité" (×8) should be "Irrationalité". Terminology: "Antipose" (Ch. 8) is not a standard French term. | Minor |
| D07 | `README-DRIVE-SNAPSHOT.md` filename still says Drive/snapshot. Kept to avoid breaking references. Other files (`review/02-astra-audit.md` "Authority: the current Drive project"; `02-numbering-handoff.md`; README mention of Google Drive; `docs/audit-programme-evaluations.md`) still carry Drive-era authority statements; they are historical records except the last, see D01. | Minor |

## 6. What is good

- Builds cleanly and reproducibly (local and CI); numbering and cross-links are generated, not typed; 600 statement/solution pairs linked in both directions.
- Programme-faithful *exercise* coverage is broad: every programme domain has graded exercises, problems and corrections, and the assessment bank is in-programme with calculator status per block.
- Sampled corrections are correct; previous audits fixed a large number of real errors (A01–A26) and the sample here found none new.
- The hors-programme mechanism (red rule + label) is clear when applied; the gap is its coverage (S03).

## 7. Recommended order of work

1. **Write the missing course sections** (C01–C05, C09–C11, C14, C15, C16): these are programme items a student cannot learn from the course.
2. Repair Ch. 7 structure (C07) and decide C08 (ax+b, 1/x core) after reading the RAPE août 2026.
3. Re-label C04 and C12 so required content is not marked optional.
4. Finish P2-U02 (S03) by marking the ~25 unmarked items.
5. Rewrite `docs/audit-programme-evaluations.md` honestly (D01); refresh numbers (D02, D03); delete dead code (D04); fix D05–D06.
6. Reconsider chapter order or add an explicit "RAPE order" reading plan (S01–S02).
7. Add the RAPE août 2026 to `PSE/` if available.

Nothing in this audit was changed in the book sources; only `README-DRIVE-SNAPSHOT.md` and this report.

## 8. Resolution (2 October 2026, follow-up commit)

| ID | Status | What was done |
|---|---|---|
| C01 | Fixed | 𝔻 defined, chain ℕ⊂ℤ⊂𝔻⊂ℚ⊂ℝ, figure redrawn, worked classification with proof that 1/3 ∉ 𝔻. |
| C02 | Fixed | New Ch. 3 section: decimal/fraction/scientific writings; values by default/excess, rounding of order n (table with √2, π, −2/3); order of magnitude. Also a⁰, a⁻ⁿ and √(x²)=\|x\|. |
| C03 | Fixed | Definition of encadrement and amplitude; property for sum, difference, product, quotient with sign hypotheses; warning; worked example (√2, √3). |
| C04 | Fixed | Systems no longer marked optional; determinant/graphical interpretation; graphical method for two inequalities (half-planes) with figure. |
| C05 | Fixed | Evident roots (incl. divisor test), cubic equation/inequality method with full worked example, polynomial equality, rational equations (forbidden-value trap) and rational inequalities, full sign theorem for any *a*, second-degree inequality method with two examples. |
| C06 | Fixed | Canonical form now precedes the discriminant; proofs of discriminant and sign theorems. |
| C07 | Fixed | Ch. 7 rebuilt: Généralités → variations/parity → six reference functions → graphical interpretation → transformations (once, marked optional). Duplicate figure and sections removed. |
| C08 | Fixed | ax+b and 1/x are core (table, figure panel, proofs of variations for all six functions). Guide updated. [VERIFY against RAPE août 2026.] |
| C09 | Fixed | Parametric circle (with justification and circular-motion example); circle of diameter [AB] with vector proof. |
| C10 | Fixed | Direction vector from equation, conversions between the three forms (worked example), vector criteria for parallel/perpendicular lines, altitude/median/perpendicular bisector method and example, analytic + graphical line–circle intersection with figure. Distance point–line and two-circle positions marked optional. |
| C11 | Fixed | New section: cos/sin as functions, period, parity, tan odd and π-periodic, with justification. |
| C12 | Fixed | Section renamed "Angles de cosinus ou de sinus donné" and treated as core; only resolution over ℝ is marked optional. sin x = a method wording fixed. |
| C13 | Fixed | Ch. 8 reordered: right-triangle reminder, radian (+ arc length), unit circle, fundamental property with proof and a cos-from-sin example, then remarkable values. |
| C14 | Fixed | New Ch. 9 section on population/variable (qualitative, discrete, continuous), counts, frequencies, classes; complete worked series (mean 1.6, median 1, mode 1, variance 1.44, σ = 1.2); construction method and figures for bar chart, pie chart, histogram. Quartile bullet and second box plot marked optional; the optional marker wrongly placed on mode/cumulative frequencies removed. |
| C15 | Fixed | Exclusive or (table), converse, De Morgan and negation of an implication (table proof), translation method and order of quantifiers; duplicate truth table removed. |
| C16 | Fixed | New "Boucles" section with a bounded loop (2ⁿ, traced) and an unbounded loop (paper-folding threshold); "qualités d'un algorithme" (validity, complexity, efficiency). Trace and pseudo-code conventions are no longer under the optional marker; only the loop invariant is. |
| C17 | Fixed | Ch. 5 reordered (operations → frame → collinearity/alignment/parallelism → scalar product); geometric definitions of sum and k·u; collinearity as u = kv with determinant criterion; parallel-lines property; scalar-product rules and worked angle (45°) and orthogonality examples. |
| S01–S02 | Fixed | Guide progression and the 66 automatism series (regenerated from `scripts/generate_automatismes.py`) now follow the five RAPE periods; vectors precede parametric lines. |
| S03 | Mostly fixed | 20 further exercises/problems tagged `[HORS PROGRAMME T10]` (Ch. 2, 5, 6, 7, 9). Item-by-item review of all ~1 100 exercises still open (P2-U02). |
| S04 | Fixed | Contrapositive and quartile questions replaced in the automatism bank. |
| S05 | Partly | Course text substantially extended; exercise volume unchanged. |
| D01 | Fixed | `docs/audit-programme-evaluations.md` rewritten from the repository's PE/RAPE, with section-level matrix and open points. |
| D02–D03 | Fixed | README and `docs/validation.md` page counts refreshed (313 / 493); défis count corrected (67, not 68); non-existent `sources/` reference removed. |
| D04 | Fixed | Dead `\iffalse` block removed. |
| D05 | Fixed | Bernoulli anecdote replaced by a William Playfair one (bar chart 1786, pie chart 1801); al-Khwārizmī date now "vers 820–830". EEF "plus de 3 000 études" removed (see §9); title corrected. |
| D06 | Fixed | "Irrationalité" spelling; "Antipose" replaced by explicit symmetries. |
| QA | Added | `make qa` now checks that each chapter's course text contains the programme notions (fails on the pre-fix sources with 31 errors, passes now). |

New mathematics written in this commit was checked by hand (all numerical examples recomputed; sign tables re-derived). The exercises and their corrections were not modified, except for optional tags in titles.

## 9. Follow-up (2 October 2026): Viète, EEF reference, ministry website

- **Viète's relations** appear in neither the PE nor the RAPE, so they are now flagged
  `[HORS PROGRAMME T10]`: the Ch. 4 proposition, the exercises "Relations de Viète" and
  "Viète appliqué", the question "les deux racines sont positives" (exercise "Paramètre
  dans le discriminant", item 4), item 3 of the problem "Logique et équations
  paramétriques", and the summary line in the chapter review. Three in-programme
  corrections that invoked Viète now use factorisation instead:
  $(x-1)(x-m)$, $(x-2)(x-m)$, and $(x-x_1)(x-x_2)$ for "Construire une équation".
- **EEF reference.** The claim "plus de 3 000 études" could not be checked against
  the source. The EEF site, ERIC, UCL Discovery, the Brighton repository and the
  CloudFront copy of the PDF are all blocked by this environment's network proxy.
  A web-search summary attributes "66 meta-analyses ... more than 3000 original
  studies" to the review, but no verbatim source text could be read, so the number
  was removed. The title now reads *Improving Mathematics in Key Stages Two and
  Three: Evidence Review* (March 2018), the title under which ERIC indexes it
  (record ED612295). The other four references in the guide were not re-checked.
- **Ministry website.** `www.education.gov.mg`, `plateforme.education.mg`,
  `hay.education.mg` and `lexpress.mg` are all blocked here, so no newer RAPE or PE
  could be obtained. Web search shows the ministry hosts RAPE/RAPS PDFs under
  `www.education.gov.mg/wp-content/uploads/...` and a page "Répartition annuelle du
  programme d'études". A 2026-2027 T10 document did not appear in the search results.
  The comparison therefore still rests on `PSE/`.
