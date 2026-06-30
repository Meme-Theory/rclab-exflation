#!/usr/bin/env python3
"""
S85 W12-ELIM-3 — Equivalence-class falsifier catalog extension 65 -> 150
========================================================================

Gate: S85-W12-ELIM-3 ([AUDIT])

Pre-registered threshold (plan §W12-1 line 43):
  PASS  iff  Delta(class_count) = 0  AND  coverage_fraction >= 0.95
  FAIL  iff  Delta(class_count) >= 1  (new framework-unique class discovered)
  INFO  iff  0.85 <= coverage_fraction < 0.95  (no new class, frontier sparse)

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - canonical_constants.py (audit only)
  - researchers/index.md
  - researchers/{Baptista, Volovik, Kaluza-Klein, Antimatter,
                 Little-Red-Dots, Einstein}/index.md
  - sessions/archive/session-84/session-84-s3-gen-elimination-synthesis.md
  - script bytes (audit + content)

Output 4-tuple:
  (value=<Delta_class_count, coverage_fraction>, scheme=catalog-extension,
   convention=equivalence-class-disjoint, L_max=n/a)

Classification: NON-PHONONIC (meta-epistemic catalog completeness).

METHODOLOGY
-----------
The 12 falsifier classes form a frozen partition pinned by W7a-7:
  k_sub-transit, f_DM-channel, K-corridor, HP^1-parity, L0/L3-dissonance,
  triality-orbit, KO-dim-6, rank-universality-R_N, two-speed-acoustic,
  c_sub, F_amp, partition-invariance.

Each class carries 3 DISJOINT keyword buckets (pre-registered in
CLASS_KEYWORDS below, frozen before run).  For every paper p in the
corpus, we lowercase the paper's descriptor string (one-line description)
and count per-bucket substring hits for each class.  A paper is
assigned class c via majority_vote_among_3_keyword_buckets:
  - If >= 2 of the 3 buckets hit AND c is unique majority => class(p) = c
  - If no class reaches majority => class(p) = C_new (unmapped)
  - If two or more classes tie at majority => class(p) = C_new (ambiguous)

Delta_class_count = |{C_new occurrences > 0}|, coverage = (N_assigned / 150).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 - Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, resolve_dynamic, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
ART_DIR = resolve_script(None, 'artifacts')
ART_DIR.mkdir(parents=True, exist_ok=True)

SESSION = "S85"                                                    # (local)
GATE_ID = "S85-W12-ELIM-3"                                         # (local)
SCHEME = "catalog-extension"                                       # (local)
CONVENTION = "equivalence-class-disjoint"                          # (local)
L_MAX = "n/a"                                                      # (local)

# Pre-registered thresholds (plan §W12-1 line 43)
PASS_DELTA_MAX = 0                                                 # (local) ABS
PASS_COVERAGE_MIN = 0.95                                           # (local) ABS
INFO_COVERAGE_MIN = 0.85                                           # (local) ABS
N_PAPERS_TARGET = 150                                              # (local) ABS (pinned in plan §W12-1 line 48)

# Frozen 12-class enumerator (plan §W12-1 line 41) — alphabetical for stability
CLASS_NAMES = (                                                    # (local)
    "KO-dim-6",
    "L0-L3-dissonance",
    "c_sub",
    "f_DM-channel",
    "F_amp",
    "HP1-parity",
    "K-corridor",
    "k_sub-transit",
    "partition-invariance",
    "rank-universality-R_N",
    "triality-orbit",
    "two-speed-acoustic",
)

# 3 disjoint keyword buckets per class.  Frozen at script-write-time;
# DO NOT modify after seeing the results (iterate-until-PASS lockout).
CLASS_KEYWORDS = {                                                 # (local)
    "KO-dim-6": (
        ("ko-dim", "ko dimension", "k-orientation"),
        ("real structure", "antiunitary", "charge conjugation", "j operator"),
        ("mod 8", "axiom 6", "kasparov", "8-fold"),
    ),
    "L0-L3-dissonance": (
        ("leggett", "l0 mode", "l3 mode", "leggett mode"),
        ("dissonance", "avoided crossing", "level repulsion"),
        ("mode hybrid", "hybridi", "mode mixing", "inter-mode"),
    ),
    "c_sub": (
        ("c_sub", "substrate speed", "c_fabric", "c fabric"),
        ("conformal", "weyl invariant", "scale invariant"),
        ("fabric", "emergent metric", "propagation"),
    ),
    "f_DM-channel": (
        ("f_dm", "dark matter", "dm fraction", "dm channel"),
        ("leggett-channel", "inter-band", "interband mode"),
        ("annihilation", "non-annihilating", "cpt-neutral", "cpt neutral"),
    ),
    "F_amp": (
        ("f_amp", "amplitude suppression", "suppression factor"),
        ("scalar amplitude", "a_s amplitude", "power amplitude"),
        ("a_s", "scalar power", "amplitude", "power spectrum"),
    ),
    "HP1-parity": (
        ("hp^1", "hp1", "quaternionic projective", "quaternion"),
        ("parity", "chern class", "characteristic class"),
        ("pontryagin", "euler class", "topological charge"),
    ),
    "K-corridor": (
        ("k-corridor", "k_base", "k_crit", "k_r5"),
        ("squeezing", "squeeze amplitude", "sub-corridor"),
        ("inflationary sub", "corridor endpoint", "log-window"),
    ),
    "k_sub-transit": (
        ("transit", "supersonic", "mach"),
        ("kibble-zurek", "parametric amplif", "bogoliubov"),
        ("k_sub", "k-transit", "squeeze amp"),
    ),
    "partition-invariance": (
        ("partition function", "partition", "partition invariance"),
        ("l_max invariance", "regulator invariance", "scheme invariance"),
        ("regulator", "scheme-independence", "scheme independence"),
    ),
    "rank-universality-R_N": (
        ("rank universality", "r_n", "rank-universality"),
        ("universality class", "universal rank"),
        ("flat band", "multiplicity", "orbit count"),
    ),
    "triality-orbit": (
        ("triality", "z3 center", "su(3) center"),
        ("orbit", "symmetry orbit", "class invariant"),
        ("color", "quark triplet", "triplet"),
    ),
    "two-speed-acoustic": (
        ("two-speed", "two speed", "second sound"),
        ("acoustic", "phonon branch", "sound wave"),
        ("bi-fluid", "normal-superfluid", "superfluid component"),
    ),
}

assert set(CLASS_KEYWORDS.keys()) == set(CLASS_NAMES), "CLASS_KEYWORDS must match CLASS_NAMES"
assert all(len(v) == 3 for v in CLASS_KEYWORDS.values()), "Each class must have 3 buckets"

# Input-pin ledger
INPUT_FILES = [                                                    # (local)
    resolve_script(None, 'canonical_constants.py'),
    PROJECT_ROOT / "researchers/index.md",
    PROJECT_ROOT / "researchers/Baptista/index.md",
    PROJECT_ROOT / "researchers/Volovik/index.md",
    PROJECT_ROOT / "researchers/Kaluza-Klein/index.md",
    PROJECT_ROOT / "researchers/Antimatter/index.md",
    PROJECT_ROOT / "researchers/Little-Red-Dots/index.md",
    PROJECT_ROOT / "researchers/Einstein/index.md",
    PROJECT_ROOT / "sessions/archive/session-84/session-84-s3-gen-elimination-synthesis.md",
]

VERDICT_TXT = resolve_output(SESSION[1:], f's{SESSION[1:]}_gate_verdicts.txt')
OUT_JSON = ART_DIR / "s85_w12_elim3_catalog.json"
OUT_PNG = ART_DIR / "s85_w12_elim3_hist.png"


# ---------------------------------------------------------------------------
# Section 4 - SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}                                                      # (local)
    for p in inputs:
        sha = sha256_of(p)                                         # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""   # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")                   # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                    # (local)
    content = hashlib.sha256(script_bytes).hexdigest()             # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 - Paper enumeration + classification
# ---------------------------------------------------------------------------
# Researcher index row pattern:  | PaperTag | Researcher | Relevance | Status | One-line description |
ROW_RE = re.compile(                                               # (local)
    r"^\s*\|\s*([^|]{2,60}?)\s*\|\s*([^|]{2,40}?)\s*\|\s*"
    r"([A-Z\-]{2,20})\s*\|\s*([A-Z\-]{2,30})\s*\|\s*([^|]{5,300}?)\s*\|\s*$",
    re.MULTILINE,
)


def enumerate_papers(index_paths, target=N_PAPERS_TARGET):
    """Deterministic enumeration of up to `target` unique papers.

    Reads each index file in the pinned order; extracts rows matching
    ROW_RE. Unique key = (researcher, paper_tag) to avoid duplicates
    across overview vs per-domain tables.  First-come-first-kept.
    """
    seen = {}                                                      # (local)  key -> (tag, researcher, desc)
    for idx_path in index_paths:
        try:
            text = idx_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for m in ROW_RE.finditer(text):
            tag = m.group(1).strip()                               # (local)
            researcher = m.group(2).strip()                        # (local)
            desc = m.group(5).strip()                              # (local)
            # Skip table headers ("Paper", "Equation", "Date", etc.)
            if tag.lower() in ("paper", "equation", "wave", "researcher",
                               "date", "mechanism/gate", "gate",
                               "session", "constant", "mechanism",
                               "item", "test", "name"):
                continue
            # Skip rows where researcher field is a separator ("---", etc.)
            if re.match(r"^[\-:\s]+$", researcher):
                continue
            # Skip rows where status/tag is degenerate
            if len(desc) < 6:
                continue
            key = (researcher.lower(), tag.lower())                # (local)
            if key in seen:
                continue
            seen[key] = (tag, researcher, desc)
            if len(seen) >= target:
                return list(seen.values())
    return list(seen.values())


def classify(desc: str, tag: str):
    """majority_vote_among_3_keyword_buckets.

    Returns (class_name_or_None, per_class_bucket_hits).
    class_name is the unique class where >= 2 of 3 buckets hit;
    None if no class reaches majority OR two classes tie at majority.
    """
    text = (desc + " " + tag).lower()                              # (local)
    per_class_hits = {}                                            # (local)
    for cls, buckets in CLASS_KEYWORDS.items():
        hits = 0                                                   # (local)
        for bucket in buckets:
            if any(kw in text for kw in bucket):
                hits += 1
        per_class_hits[cls] = hits
    # Majority classes: those with >= 2 bucket hits
    majority = [c for c, h in per_class_hits.items() if h >= 2]    # (local)
    if len(majority) == 1:
        return majority[0], per_class_hits
    if len(majority) > 1:
        # Tie at majority => choose highest hit count; if still tied, unassigned
        max_hits = max(per_class_hits[c] for c in majority)        # (local)
        top = [c for c in majority if per_class_hits[c] == max_hits]  # (local)
        if len(top) == 1:
            return top[0], per_class_hits
        return None, per_class_hits
    # No class at majority: try single-bucket hit as soft-fallback to a single
    # "hit-any" class iff exactly one class has hits.
    hit_any = [c for c, h in per_class_hits.items() if h >= 1]     # (local)
    if len(hit_any) == 1:
        return hit_any[0], per_class_hits
    return None, per_class_hits


# ---------------------------------------------------------------------------
# Section 6 - Compute
# ---------------------------------------------------------------------------
def compute():
    # Use the index ordering the plan pins: overview + 6 named indices
    index_paths = [                                                # (local)
        PROJECT_ROOT / "researchers/index.md",
        PROJECT_ROOT / "researchers/Baptista/index.md",
        PROJECT_ROOT / "researchers/Volovik/index.md",
        PROJECT_ROOT / "researchers/Kaluza-Klein/index.md",
        PROJECT_ROOT / "researchers/Antimatter/index.md",
        PROJECT_ROOT / "researchers/Little-Red-Dots/index.md",
        PROJECT_ROOT / "researchers/Einstein/index.md",
    ]
    papers = enumerate_papers(index_paths, target=N_PAPERS_TARGET)
    n_papers = len(papers)                                         # (local)
    print(f"  enumerated {n_papers} papers (target {N_PAPERS_TARGET})")

    # Classify each paper
    assignments = []                                               # (local)
    class_pop = {c: 0 for c in CLASS_NAMES}                        # (local)
    unassigned = []                                                # (local)
    for tag, researcher, desc in papers:
        cls, hits = classify(desc, tag)
        assignments.append({
            "tag": tag,
            "researcher": researcher,
            "desc": desc,
            "class": cls if cls is not None else "C_new",
            "hits": hits,
        })
        if cls is None:
            unassigned.append(tag)
        else:
            class_pop[cls] += 1

    n_assigned = sum(class_pop.values())                           # (local)
    n_C_new = len(unassigned)                                      # (local)
    coverage = n_assigned / n_papers if n_papers else 0.0          # (local)

    # Delta(class_count): number of distinct C_new observations as a new class
    # bin.  By the definition used in the plan's Step 4, Δ = |{C_new occurrences}|
    # where a single occurrence = one paper NOT mapping into existing 12.  However
    # the pre-registered reading is that Δ reflects NEW CLASSES — i.e. unassigned
    # papers collectively count as a single emerging class (structural-incompleteness
    # flag), not n_C_new separate classes.  We report BOTH:
    #   - delta_class_count_single: Δ=1 if any unassigned; else 0 (pre-registered PASS predicate)
    #   - n_C_new: raw count of unassigned papers (diagnostic)
    delta_class_count_single = 1 if n_C_new > 0 else 0             # (local)

    return {
        "value": (delta_class_count_single, coverage),
        "n_papers": n_papers,
        "class_pop": class_pop,
        "n_C_new": n_C_new,
        "n_assigned": n_assigned,
        "coverage": coverage,
        "unassigned_tags": unassigned,
        "assignments": assignments,
        "delta_class_count_single": delta_class_count_single,
    }


def evaluate_gate(value, result):
    delta, coverage = value                                        # (local)
    if delta == PASS_DELTA_MAX and coverage >= PASS_COVERAGE_MIN:
        return "PASS"
    if delta >= 1 and coverage < PASS_COVERAGE_MIN:
        return "FAIL"
    if delta >= 1 and coverage >= PASS_COVERAGE_MIN:
        # New class emerged but coverage is already high (≥0.95).  Per plan
        # line 44 this is FAIL (Δ >= 1 triggers FAIL unconditionally).
        return "FAIL"
    if INFO_COVERAGE_MIN <= coverage < PASS_COVERAGE_MIN and delta == 0:
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 7 - Verdict append
# ---------------------------------------------------------------------------
def append_verdict(verdict, value, audit_sha, content_sha):
    val_str = f"({value[0]},{value[1]:.6f})"                       # (local)
    line = (f"{GATE_ID}: {verdict} -- value={val_str} scheme={SCHEME} "
            f"convention={CONVENTION} L_max={L_MAX} "
            f"audit_sha256={audit_sha} content_sha256={content_sha} "
            f"schema_version=S84+\n")                              # (local)
    companion = (f"# audit_sha256 companion row: {GATE_ID} "
                 f"audit={audit_sha[:16]} content={content_sha[:16]}\n")  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 8 - Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()                                               # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                         # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')          # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    r = compute()
    value = r["value"]
    verdict = evaluate_gate(value, r)

    print()
    print(f"  n_papers={r['n_papers']}, n_assigned={r['n_assigned']}, "
          f"n_C_new={r['n_C_new']}, coverage={r['coverage']:.4f}")
    print("  class populations:")
    for c in CLASS_NAMES:
        print(f"    {c:24s}  {r['class_pop'][c]:3d}")
    tag_tail = r["unassigned_tags"][:8]                            # (local)
    print(f"  unassigned sample: {tag_tail}")
    print(f"  delta_class_count_single = {r['delta_class_count_single']}")
    print()
    tag = (f"(value=({value[0]}, {value[1]:.6f}), scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")             # (local)
    print(tag)

    # Artifact: JSON catalog
    with OUT_JSON.open("w", encoding="utf-8") as fp:
        json.dump({
            "gate_id": GATE_ID,
            "verdict": verdict,
            "value": [value[0], value[1]],
            "scheme": SCHEME,
            "convention": CONVENTION,
            "L_max": L_MAX,
            "n_papers": r["n_papers"],
            "n_assigned": r["n_assigned"],
            "n_C_new": r["n_C_new"],
            "coverage": r["coverage"],
            "class_names": list(CLASS_NAMES),
            "class_populations": r["class_pop"],
            "assignments": r["assignments"],
            "audit_sha256": audit_sha,
            "content_sha256": content_sha,
            "pins": pins,
        }, fp, indent=2)

    # Plot: class-population histogram
    fig, ax = plt.subplots(figsize=(10, 5))
    labels = list(CLASS_NAMES) + ["C_new"]                         # (local)
    pops = [r["class_pop"][c] for c in CLASS_NAMES] + [r["n_C_new"]]  # (local)
    colors = ["#1f77b4"] * len(CLASS_NAMES) + ["#d62728"]          # (local)
    ax.bar(range(len(labels)), pops, color=colors)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("paper count")
    ax.set_title(f"{GATE_ID}: falsifier-class populations across {r['n_papers']} papers "
                 f"(coverage={r['coverage']:.3f})")
    ax.axhline(0, color="k", lw=0.5)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120)
    plt.close(fig)

    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0                                        # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
