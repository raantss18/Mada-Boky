#!/usr/bin/env python3
"""Check textbook review records and hashes; never certify mathematical truth."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ITEM_GATES = {
    "definition": {"mathematics", "hypotheses"},
    "property": {"mathematics", "hypotheses"},
    "proof": {"mathematics", "hypotheses"},
    "claim": {"mathematics", "hypotheses"},
    "example": {"mathematics", "pedagogy"},
    "exercise": {"mathematics", "solution_match", "pedagogy"},
    "correction": {"mathematics", "solution_match"},
    "figure": {"mathematics", "visual"},
    "section": {"pedagogy"},
}
PROJECT_GATES = {"coverage", "notation", "pedagogy", "build", "visual", "persistence"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", type=Path)
    parser.add_argument("--manifest", default="review/gates.json")
    parser.add_argument("--snapshot", action="store_true", help="Print current source snapshot only")
    args = parser.parse_args()
    root = args.project_root.resolve()
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    def local_path(raw):
        if not isinstance(raw, str) or not raw or Path(raw).is_absolute():
            raise ValueError("Paths must be nonempty and relative to the project")
        path = (root / raw).resolve()
        if not path.is_relative_to(root):
            raise ValueError("Path escapes project root: " + raw)
        return path

    def read_json(raw):
        return json.loads(local_path(raw).read_text(encoding="utf-8"))

    def verify_file(record, label):
        path = local_path(record["path"])
        require(path.is_file(), label + ": missing " + record["path"])
        if path.is_file():
            require(digest(path) == record.get("sha256"), label + ": stale hash " + record["path"])
            require(path.stat().st_size > 0, label + ": empty evidence/output " + record["path"])

    data = read_json(args.manifest)
    require(data.get("schema_version") == 1, "Unsupported schema_version")
    require(data.get("scope") in {"chapter", "book"}, "scope must be chapter or book")
    sources = data["source_files"]
    require(isinstance(sources, list) and bool(sources), "source_files must be nonempty")
    actual = {}
    for record in sources:
        raw = record["path"]
        require(raw not in actual, "Duplicate source: " + raw)
        path = local_path(raw)
        if not path.is_file():
            raise ValueError("Missing source: " + raw)
        actual[raw] = digest(path)
        if not args.snapshot:
            verify_file(record, "Source")
    snapshot = hashlib.sha256(json.dumps(actual, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if args.snapshot:
        print(snapshot)
        return 0
    require(data.get("snapshot_sha256") == snapshot, "Source snapshot changed")
    inventory_path = data["inventory_file"]
    require(inventory_path in actual, "Inventory must be in source snapshot")
    items = read_json(inventory_path)
    require(isinstance(items, list) and bool(items), "Inventory must be a nonempty list")
    expected = {("@project", gate) for gate in PROJECT_GATES}
    ids = set()
    for item in items:
        identity = item["id"]
        require(isinstance(identity, str) and bool(identity), "Invalid item ID")
        require(identity != "@project" and identity not in ids, "Reserved/duplicate ID: " + str(identity))
        ids.add(identity)
        require(bool(item.get("location")), "Missing location: " + identity)
        kind = item["kind"]
        require(kind in ITEM_GATES, "Unknown kind: " + str(kind))
        expected.update((identity, gate) for gate in ITEM_GATES.get(kind, set()))
    found = set()
    for review in data["reviews"]:
        key = (review["item_id"], review["gate"])
        label = key[0] + "/" + key[1]
        require(key in expected, "Unexpected review: " + label)
        require(key not in found, "Duplicate review: " + label)
        found.add(key)
        require(review.get("status") == "passed", "Unpassed review: " + label)
        require(review.get("snapshot_sha256") == snapshot, "Stale review: " + label)
        require(isinstance(review.get("method"), str) and bool(review["method"].strip()), "Missing method: " + label)
        require(isinstance(review.get("reviewed_at"), str) and bool(review["reviewed_at"].strip()), "Missing review date: " + label)
        evidence = review.get("evidence", [])
        require(isinstance(evidence, list) and bool(evidence), "Missing evidence: " + label)
        for record in evidence:
            verify_file(record, label)
    for identity, gate in sorted(expected - found):
        errors.append("Missing review: " + identity + "/" + gate)
    variants = data["expected_variants"]
    require(isinstance(variants, list) and bool(variants), "expected_variants must be nonempty")
    require(len(variants) == len(set(variants)), "Duplicate expected variant")
    output_variants = []
    for record in data["outputs"]:
        output_variants.append(record["variant"])
        verify_file(record, "Output")
    require(sorted(output_variants) == sorted(variants), "Outputs do not match requested variants")
    issues = read_json(data["issues_file"])
    require(isinstance(issues, list), "Issues must be a list")
    for issue in issues:
        status = issue.get("status")
        if status != "resolved" and not (status == "deferred" and issue.get("out_of_scope") is True):
            errors.append("Unresolved in-scope issue: " + str(issue.get("id", "unnamed")))
    if errors:
        print("GATES FAILED\n" + "\n".join("- " + e for e in errors))
        return 1
    print("Recorded gates complete for " + data["scope"] + " snapshot " + snapshot)
    print("Bookkeeping only: not mathematical certification or proof of complete inventory/honest review.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        print("GATES FAILED: invalid/missing input: " + str(exc), file=sys.stderr)
        sys.exit(1)
