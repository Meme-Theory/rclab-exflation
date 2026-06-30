"""Throwaway: characterize NOISE/VALID structural-equation shapes in audit corpus."""
import json
import re
import random
from pathlib import Path
from collections import Counter

audit = json.loads(Path("tools/_anchor_validation_results.json").read_text())
idx = json.loads(Path("tools/knowledge-index.json").read_text(encoding="utf-8"))
eq_index = {e["id"]: e for e in idx["equations"]}

structural_noise = []
structural_valid = []
for aid, av in audit["equations"].items():
    e = eq_index[aid]
    if e["type"] != "structural":
        continue
    if av["verdict"] == "NOISE":
        structural_noise.append((aid, av, e))
    elif av["verdict"] == "VALID":
        structural_valid.append((aid, av, e))


def lhs_of(raw):
    m = re.match(r"^([^=\n]*?)(\s*[=≡≈]\s*)(.*)$", raw)
    return m.group(1).strip() if m else None


def category_of(path):
    p = path.lower().replace("\\", "/")
    if p.startswith("computations/") and (p.endswith(".txt") or p.endswith(".json")):
        return "computation_output"
    if p.startswith("computations/") and p.endswith(".py"):
        return "computation_script"
    if p.startswith("sessions/session-plan/"):
        return "plan_file"
    if "/workshops/" in p:
        return "workshop_md"
    if p.startswith("sessions/session-") and p.endswith(".md"):
        return "session_md"
    if p.startswith("sessions/framework/"):
        return "framework_md"
    return "other"


cat_noise = Counter()
cat_valid = Counter()
for (_, _, e) in structural_noise:
    cat_noise[category_of(e["source_file"])] += 1
for (_, _, e) in structural_valid:
    cat_valid[category_of(e["source_file"])] += 1

print("Source-file CATEGORY breakdown:")
print(f"{'category':25s} {'NOISE':>8s} {'VALID':>8s} {'NOISE %':>10s}")
all_cats = sorted(set(cat_noise) | set(cat_valid))
for c in all_cats:
    n, v = cat_noise[c], cat_valid[c]
    pct = (100.0 * n / (n + v)) if (n + v) > 0 else 0
    print(f"{c:25s} {n:>8d} {v:>8d} {pct:>9.1f}%")

print()
print("Signature patterns in 133 NOISE structural:")

PATTERNS = {
    "audit_sha256=": r"^audit_sha256\s*=",
    "convention=": r"^convention\s*=",
    "scheme=": r"^scheme\s*=",
    "value=quoted": r"^value\s*=\s*['\"]",
    "tier_pin=": r"^tier_pin\s*=",
    "schema_version=": r"^schema_version\s*=",
    "OMP/MKL env": r"^(OMP|MKL)_NUM_THREADS",
    "section_header_colon": r":\s*$",
    "output_var=num+unit": r"^[a-zA-Z_][a-zA-Z_0-9]*\s*(\([^)]*\))?\s*=\s*[-+]?[\d.]+(?:[eE][-+]?\d+)?\s*[a-zA-Z\^]*\s*$",
    "tuple_listing_with_commas_and_eq": r"^[a-zA-Z_]+\s*=\s*[^,]+,\s*[a-zA-Z_]+\s*=",
    "var=val:another=val": r"^[a-zA-Z_]+\s*=\s*[^:]+:\s*[a-zA-Z_]+\s*=",
    "has_status_word": r"\b(CONVERGED|PASS|FAIL|VALID|UNKNOWN|NULL|ERROR|RETRACTED)\b",
    "starts_with_uppercase_word": r"^[A-Z][a-z]+\s+[a-z]",
    "ends_with_colon": r":$",
}

sig_hits = Counter()
none_examples = []
for (aid, _, e) in structural_noise:
    raw = e["raw"]
    hits = []
    for name, pat in PATTERNS.items():
        flags = re.IGNORECASE if "has_status" in name else 0
        if re.search(pat, raw, flags):
            hits.append(name)
    if not hits:
        sig_hits["NONE"] += 1
        none_examples.append((aid, raw[:120]))
    else:
        for h in hits:
            sig_hits[h] += 1

print(f"  total NOISE: {len(structural_noise)}")
for sig, n in sig_hits.most_common():
    print(f"  {sig:35s} : {n}")

print()
print("First 10 NOISE entries NOT matching any signature (residual):")
for aid, raw in none_examples[:10]:
    print(f"  [{aid}] {raw}")

valid_multi = [
    (aid, av, e)
    for (aid, av, e) in structural_valid
    if lhs_of(e["raw"]) and len(lhs_of(e["raw"]).split()) > 1
]
print()
print(f"VALID structural with multi-word LHS: {len(valid_multi)} of {len(structural_valid)}")
print("(false-positive risk if we drop \\s from the LHS character class)")
print()
print("Sample of 20:")
random.seed(42)
for aid, av, e in random.sample(valid_multi, min(20, len(valid_multi))):
    lhs = lhs_of(e["raw"])
    raw = e["raw"].replace("\n", " | ")[:120]
    print(f"  [{aid}] LHS={lhs!r}")
    print(f"       raw: {raw}")
    print()
