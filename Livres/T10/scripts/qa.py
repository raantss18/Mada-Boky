#!/usr/bin/env python3
"""Fast static checks for the T10 textbook source tree."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {ROOT / "sources" / "manuel_seconde_predecesseur.tex"}
tex_files = [p for p in ROOT.rglob("*.tex") if p not in EXCLUDED and "build" not in p.parts]
errors: list[str] = []

all_text = "\n".join(p.read_text(encoding="utf-8") for p in tex_files)

# Inputs must resolve relative to project root.
for source in tex_files:
    text = source.read_text(encoding="utf-8")
    for item in re.findall(r"\\input\{([^}]+)\}", text):
        target = ROOT / (item if item.endswith(".tex") else item + ".tex")
        if not target.exists():
            errors.append(f"missing input: {item} (from {source.relative_to(ROOT)})")

# Every named environment must have balanced begin/end counts project-wide.
begins = Counter(re.findall(r"\\begin\{([^}]+)\}", all_text))
ends = Counter(re.findall(r"\\end\{([^}]+)\}", all_text))
for env in sorted(set(begins) | set(ends)):
    if begins[env] != ends[env]:
        errors.append(f"environment {env}: {begins[env]} begin / {ends[env]} end")

# Duplicate labels break navigation in the teacher edition.
labels = re.findall(r"\\label\{([^}]+)\}", all_text)
for label, count in Counter(labels).items():
    if count > 1 and not label.startswith(("exo:", "prob:", "sol:")):
        errors.append(f"duplicate label {label!r}: {count}")

# Correction numbers are generated in the order of their chapter's statements.
# Check the count and chapter heading so insertions cannot silently drift.
for chapter_file in sorted((ROOT / "chapters").glob("[0-9][0-9]-*.tex")):
    chapter_number = int(chapter_file.name[:2])
    solution_file = next((ROOT / "solutions").glob(f"{chapter_number:02d}-*.tex"), None)
    if solution_file is None:
        errors.append(f"missing solution module for chapter {chapter_number}")
        continue
    chapter_text = chapter_file.read_text(encoding="utf-8")
    solution_text = solution_file.read_text(encoding="utf-8")
    exercise_count = len(re.findall(r"\\begin\{exo\}", chapter_text))
    problem_count = len(re.findall(r"\\begin\{probleme\}", chapter_text))
    for line_no, line in enumerate(chapter_text.splitlines(), 1):
        if line.startswith(r"\begin{exo}") and r"\corrige" not in line:
            errors.append(f"chapter {chapter_number}:{line_no}: exercise has no correction link")
        if line.startswith(r"\begin{probleme}") and r"\corrigeP" not in line:
            errors.append(f"chapter {chapter_number}:{line_no}: problem has no correction link")
    if len(re.findall(r"^\\solutionchapter\{", solution_text, re.M)) != 1:
        errors.append(f"chapter {chapter_number}: expected one generated solution heading")
    exercise_solutions = len(re.findall(r"^\\solutiontitle\{", solution_text, re.M))
    problem_solutions = len(re.findall(r"^\\psolutiontitle\{", solution_text, re.M))
    if exercise_solutions != exercise_count:
        errors.append(f"chapter {chapter_number}: {exercise_solutions} exercise solutions for {exercise_count} exercises")
    if problem_solutions != problem_count:
        errors.append(f"chapter {chapter_number}: {problem_solutions} problem solutions for {problem_count} problems")
    if re.search(r"\\(?:p)?solutiontitle\{\d+\}\{\d+\}", solution_text):
        errors.append(f"chapter {chapter_number}: manually numbered correction title remains")

if "°" in all_text:
    errors.append("raw Unicode degree sign found; use $^{\\circ}$ for portable builds")

# Recurring typography regressions found during the 2026 visual audit.
for pattern, message in [
    (r"\$\\og|\\fg\$", "French quotation mark command used inside math mode"),
    (r"\\vec\{[ij]\}", "dotted i/j used under a vector arrow; use \\imath/\\jmath"),
    (r"u_k/2", "stacked fraction expected in the Syracuse recurrence"),
    (r"-b/\(2a\)", "stacked fraction expected for -b/(2a)"),
    (r"\\text\{aire\}/", "ambiguous slash notation in an area formula"),
    (r"clip\s*=\s*false", "PGFPlots clipping disabled; keep graphs within their axes"),
    (r"\\input\{backmatter/competences\}", "obsolete transversal-skills page is still included"),
]:
    if re.search(pattern, all_text):
        errors.append(message)

# Edition-level promises: two teaching sessions per week and a usable modular
# assessment bank. These checks prevent accidental content loss.
automatismes = (ROOT / "assessments" / "automatismes.tex").read_text(encoding="utf-8")
evaluations = (ROOT / "assessments" / "evaluations.tex").read_text(encoding="utf-8")
if len(re.findall(r"^\\section\{Semaine \d+, séance [AB]", automatismes, re.M)) != 66:
    errors.append("expected 66 session-by-session automatism series")
if "\\chapter{Banque d'exercices et de problèmes}" not in evaluations:
    errors.append("assessment module must be an exercise and problem bank")
if len(re.findall(r"^\\begin\{exo\}", evaluations, re.M)) < 42:
    errors.append("expected at least 42 selectable exercises")
if len(re.findall(r"^\\begin\{probleme\}", evaluations, re.M)) < 8:
    errors.append("expected at least eight selectable problems")
if evaluations.count(r"\calcoui") + evaluations.count(r"\calcnon") < 50:
    errors.append("each bank item must state calculator policy")
bank_corrections = (ROOT / "assessments" / "corrections.tex").read_text(encoding="utf-8")
if len(re.findall(r"^\\bankexerciseanswer\{", bank_corrections, re.M)) != evaluations.count(r"\begin{exo}"):
    errors.append("assessment-bank exercise correction count differs from the statement count")
if len(re.findall(r"^\\bankproblemanswer\{", bank_corrections, re.M)) != evaluations.count(r"\begin{probleme}"):
    errors.append("assessment-bank problem correction count differs from the statement count")
if r"\hyperref[sol:B\thenexo]" not in evaluations or r"\hyperref[sol:BP\thenprob]" not in evaluations:
    errors.append("assessment items must link to their corrections")
if r"\hyperref[exo:\thenbankexocorr]" not in bank_corrections or r"\hyperref[prob:\thenbankprobcorr]" not in bank_corrections:
    errors.append("assessment corrections must link back to their statements")
if any(marker in evaluations for marker in (
    "10 à 25 minutes", "25 à 45 minutes", "35 à 70 minutes",
    "40--50 min", "1 h à 1 h 30"
)):
    errors.append("assessment bank must not contain suggested completion times")

# User-facing sources must remain a plain textbook: no institutional claims,
# curriculum acronyms or algorithmic-complexity material.
active_user_text = "\n".join(
    p.read_text(encoding="utf-8")
    for p in tex_files
    if not any(part in {"solutions", "teacher"} for part in p.parts)
)
for pattern, message in [
    (r"\b(?:PE/RAPE|RAPE|Minist[eè]re)\b", "institutional or curriculum reference remains"),
    (
        r"Complexit[eé]\s*:|(?:\\mathcal|\\mathrm)\s*\{?O\}?\s*\(\s*(?:1|n|n\^2|\\log)",
        "algorithmic complexity remains in the student text",
    ),
]:
    if re.search(pattern, active_user_text, re.I):
        errors.append(message)

required = [
    "Énoncés", "Algorithmique", "Ensemble", "Trinôme", "Droites",
    "Cercle trigonométrique", "Vecteurs", "variance", "écart-type",
]
plain = all_text.replace("\\'", "").replace("\\`", "")
for term in required:
    if term.lower() not in plain.lower():
        errors.append(f"core textbook keyword not found: {term}")

if errors:
    print("QA FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(
    f"QA OK: {len(tex_files)} TeX modules; "
    "exercise/problem numbering and source structure checked"
)
