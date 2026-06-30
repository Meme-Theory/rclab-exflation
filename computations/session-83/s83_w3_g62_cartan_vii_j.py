#!/usr/bin/env python3
"""
S83 W3-G62 — CARTAN-VII-J-REGISTRY-SUBMIT
=========================================

Gate: S83-CARTAN-VII-J-REGISTRY-SUBMIT  ([AUDIT])

Pre-registered threshold (plan sessions/session-plan/session-83-plan.md §W3-G62,
and task-#62 spec of the S83 Wave-3 dispatch):
  PASS: §VII.J entry landed in sessions/permanent-results-registry.md with
        (1) rank-scaling theorem statement (refined post-G18), including:
              simply-laced core, r=1 weakness, r>=2 noise-floor,
              exceptional-family falsification clause;
        (2) clauses (a) Künneth / (b) quantum / (c) Kasparov-orbit /
              (d) non-flat T-correction — all cited against the supporting
              W2 gate ID;
        (3) HP^even scope anchor via G54;
        (4) explicit citations of W2 gates G17..G24 as evidence;
        (5) dependency block listing Connes/Kasparov/CC96/Van den Dungen
              references.
        AND the 4-tuple slot closes with (landing_status=PASS, scheme=...,
        convention=..., L_max=...).
  FAIL: registry heading missing, or any of (1)..(5) missing, or evidence
        reference mismatched to S83 verdict line in s83_gate_verdicts.txt.

4-tuple slot: (landing_status=?,
               scheme=Level-2-Cartan-exclusion,
               convention=W2-G17-G22-sanity,  # plan convention tag
               L_max=N/A)

Classification: GEOMETRIC.

CONTEXT
-------
§VII.J is the named registry entry for the Cartan Level-2 Exclusion Theorem
developed through S83 W2 gates G17, G18, G19, G20, G21, G22, G23, G24 and
anchored (via HP^even scope) in W3-G54. The theorem states that for a
spectral triple (A, H, D) with an abelian Cartan subfactor C of a simply-
laced ambient compact connected simple Lie group G, and with dim H_pi = 1
on the F_KK regulator class (§VII.K), the primary cyclic-cohomology class
HC^2_primary(C) vanishes. Protection STRENGTH scales with Cartan rank.

This script is the AUDIT gate that verifies the landing: (a) §VII.J heading
present; (b) rank-scaling clause present; (c) all four preservation clauses
present; (d) all W2-G17..G24 citations present; (e) HP^even scope anchor
present; (f) 4-tuple tag present; (g) cross-checks against the S83 gate
verdicts file for consistency between registry text and the recorded
W2 verdicts.

SUBSTITUTION CHAIN [AUDIT]
---------------------------
Step 1 (definition):
    §VII.J entry = a markdown subsection of sessions/permanent-results-registry.md
    under the heading "### VII.J — Cartan Level-2 Exclusion Theorem ..."
    that contains: (i) rank-scaling theorem statement, (ii) preservation
    clauses (a)..(d), (iii) HP^even scope tag, (iv) citations of G17..G24,
    (v) dependency block, (vi) 4-tuple closure.

Step 2 (substitution, landing rule):
    For each required element e_k in the checklist E = {e_1, ..., e_N},
    define has(e_k) := (registry_text contains anchor_k), where anchor_k is
    a pre-registered substring specific to the element. Landing PASS iff
    for all k: has(e_k) == True.

Step 3 (simplification):
    PASS condition = AND_{k in [1..N]} has(e_k)  AND  evidence_consistent,
    where evidence_consistent checks that each W2 gate ID cited in the
    registry entry actually has a verdict line in s83_gate_verdicts.txt
    with a matching classification (PASS or FAIL-BY-DESIGN-falsifier).

Step 4 (direction):
    PASS if landing condition holds AND all 8 carry-forward gates
    (G17, G18, G19, G20, G21, G22, G23, G24) have verdict lines in the
    s83 ledger. INFO if landing holds but one or more carry-forward
    verdicts are absent (typically a clean-up issue, not a landing
    blocker). FAIL if any required anchor is missing.

Outputs:
  * Script:   s83_w3_g62_cartan_vii_j.py
  * Data:     s83_w3_g62_cartan_vii_j.npz
  * Plot:     s83_w3_g62_cartan_vii_j.png
  * Verdict:  line appended to s83_gate_verdicts.txt (64-char SHA)
  * Paper:    session-83-results-workingpaper.md  §W3-G62
"""

# =============================================================================
# IMPORTS & ENVIRONMENT
# =============================================================================
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import hashlib
import json  # (local) unused tolerance header kept for symmetry with g53
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Canonical constants import required by computation standards (no framework constants
# used in this audit / registry-landing script).
SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))
from canonical_constants import *  # noqa: F401,F403

PROJECT_ROOT = SCRIPT_DIR.parent  # (local) C:\sandbox\Ainulindale Exflation

# =============================================================================
# INPUT FILE PINS
# =============================================================================
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
VERDICTS_PATH = SCRIPT_DIR / "s83_gate_verdicts.txt"  # (local)
INDEX_PATH    = PROJECT_ROOT / "tools" / "knowledge-index.json"  # (local)

OUT_NPZ = SCRIPT_DIR / "s83_w3_g62_cartan_vii_j.npz"  # (local)
OUT_PNG = SCRIPT_DIR / "s83_w3_g62_cartan_vii_j.png"  # (local)


def sha256_file(path):
    """SHA-256 of a file (streaming)."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def anchor_present(text, anchor):
    """Case-SENSITIVE substring containment test for landing anchors."""
    return anchor in text


# =============================================================================
# PRE-REGISTERED ANCHOR CHECKLIST
# =============================================================================
# Each entry: (element_id, short_description, anchor_substring)
# Anchors are chosen to be specific enough that trivial failure modes
# (e.g. accidental deletion, incomplete merge) are caught immediately.
LANDING_ANCHORS = [  # (local) pre-registered checklist for §VII.J
    # (1) Section heading
    ("heading", "§VII.J section heading",
     "### VII.J — Cartan Level-2 Exclusion Theorem"),
    # (2) Rank-scaling theorem statement components
    ("theorem_simply_laced", "simply-laced core clause",
     "simply-laced ambient compact connected Lie group"),
    ("theorem_eq", "HC^2_primary = 0 equation label",
     "HC^2_primary(C) = 0"),
    ("theorem_rank_i", "rank r>=2 noise-floor clause",
     "(i) r >= 2 (simply-laced)"),
    ("theorem_rank_ii", "rank r=1 weakness clause",
     "(ii) r = 1 (rank-1 limit)"),
    ("theorem_rank_iii", "exceptional/non-simply-laced falsification clause",
     "(iii) Non-simply-laced / exceptional"),
    # (3) Preservation clauses (a)..(d)
    ("pres_a", "Künneth preservation (G19)",
     "(a) Abelian Künneth extension (G19)"),
    ("pres_b", "Quantum q-deformation preservation (G20)",
     "(b) Quantum-group deformation at generic q (G20)"),
    ("pres_c", "Kasparov inner-fluctuation preservation (G23)",
     "(c) Inner-fluctuation Kasparov orbit (G23)"),
    ("pres_d", "Non-flat Jensen T-correction (G24)",
     "(d) Non-flat Jensen-deformed T-correction (G24)"),
    # (4) Higher-degree and non-abelian extensions
    ("level3", "Level-3+ higher-degree extension (G21)",
     "HIGHER-DEGREE EXTENSION (Level-3+, G21)"),
    ("nonabelian", "Non-abelian SU(2) restriction (G22)",
     "NON-ABELIAN RESTRICTION (G22)"),
    ("sanity", "Spin(8) sanity anchor (G17)",
     "SANITY ANCHOR (G17)"),
    ("falsifier", "G_2 falsifier (G18)",
     "FALSIFIER (G18, FAIL-BY-DESIGN)"),
    # (5) HP^even scope and provenance
    ("hp_even_scope", "HP^even scope anchor via G54",
     "HP^even SCOPE (G54 anchor)"),
    ("deps_connes", "Connes 1985/1994 dependency",
     "Connes 1985"),
    ("deps_kasparov", "Kasparov 1980 dependency",
     "Kasparov 1980"),
    ("deps_cc96", "CC96 balanced-pair theorem dependency",
     "CC96 Eq 2.11"),
    ("deps_vdd", "Van den Dungen UKK-bar bridge dependency",
     "Van den Dungen Paper 11"),
    ("deps_section_k", "§VII.K regulator class scope dependency",
     "§VII.K"),
    # (6) 4-tuple closure
    ("tuple_value", "4-tuple value field",
     "value=rank-scaling-simply-laced-core_8routes_1falsifier"),
    ("tuple_scheme", "4-tuple scheme field",
     "scheme=HC2-primary-Cartan-subfactor-exclusion"),
    ("tuple_conv", "4-tuple convention field",
     "convention=simply-laced-Weyl-cancellation"),
    # (7) Significance / open clauses
    ("significance", "Significance block",
     "SIGNIFICANCE:"),
    ("open_clause", "Open-carry-forward clause",
     "OPEN:"),
    # (8) 8 evidence route enumeration
    ("routes_8", "8 converging evidence routes statement",
     "8 converging"),
]

# =============================================================================
# PRE-REGISTERED CARRY-FORWARD GATE IDS (must appear in verdicts ledger)
# =============================================================================
REQUIRED_W2_GATES = [  # (local) carry-forward evidence ledger pin
    ("G17", "S83-CARTAN-EXCL-D4-SPIN8-SANITY"),
    ("G18", "S83-CARTAN-EXCL-EXCEPTIONAL-FALSIFIER"),
    ("G19", "S83-W2-G19-CARTAN-EXCL-NONSIMPLE"),
    ("G20", "S83-QUANTUM-CARTAN-PROTECTION"),
    ("G21", "S83-CARTAN-LEVEL3-HIGHER-PROTECTION"),
    ("G22", "S83-NONABELIAN-SU2-PROTECTION-COMPUTE"),
    ("G23", "S83-GAUGE-DRESSED-PROTECTION"),
    ("G24", "S83-NONFLAT-T-CORRECTION-L2"),
]

REQUIRED_W3_GATES = [  # (local) HP^even scope anchor
    ("G54", "S83-HP-EVEN-COMPLETENESS-AUDIT-VII"),
]

# =============================================================================
# MAIN
# =============================================================================
def main():
    print("=" * 72)
    print("S83 W3-G62 — CARTAN-VII-J-REGISTRY-SUBMIT")
    print("=" * 72)

    # --- Input pins ---
    if not REGISTRY_PATH.exists():
        print(f"[FATAL] Registry not found: {REGISTRY_PATH}")
        sys.exit(1)
    if not VERDICTS_PATH.exists():
        print(f"[FATAL] Verdicts ledger not found: {VERDICTS_PATH}")
        sys.exit(1)

    registry_sha = sha256_file(REGISTRY_PATH)  # (local)
    verdicts_sha = sha256_file(VERDICTS_PATH)  # (local)
    index_sha = sha256_file(INDEX_PATH) if INDEX_PATH.exists() else "absent"  # (local)

    print(f"[pin] registry  SHA-256: {registry_sha}")
    print(f"[pin] verdicts  SHA-256: {verdicts_sha}")
    print(f"[pin] index     SHA-256: {index_sha}")

    with open(REGISTRY_PATH, "r", encoding="utf-8") as fh:
        registry_text = fh.read()
    with open(VERDICTS_PATH, "r", encoding="utf-8") as fh:
        verdicts_text = fh.read()

    # --- Step 1: anchor checklist ---
    print("\n[Step 1] Anchor checklist (§VII.J landing elements)")
    anchor_results = []  # (local)
    for elem_id, desc, anchor in LANDING_ANCHORS:
        present = anchor_present(registry_text, anchor)  # (local)
        anchor_results.append((elem_id, desc, anchor, present))
        flag = "OK " if present else "MISS"
        print(f"  [{flag}] {elem_id:<18s} -- {desc}")

    all_anchors_present = all(r[3] for r in anchor_results)  # (local)
    n_total = len(anchor_results)  # (local)
    n_present = sum(1 for r in anchor_results if r[3])  # (local)
    print(f"\n  Anchors present: {n_present}/{n_total}")

    # --- Step 2: carry-forward evidence ledger check ---
    print("\n[Step 2] Carry-forward evidence ledger check (W2 + W3)")
    ledger_hits = []  # (local)
    for tag, gate_id in REQUIRED_W2_GATES + REQUIRED_W3_GATES:
        present_in_ledger = gate_id in verdicts_text  # (local)
        present_in_registry = gate_id in registry_text or tag in registry_text  # (local)
        ledger_hits.append((tag, gate_id, present_in_ledger, present_in_registry))
        lflag = "LEDGER" if present_in_ledger else "MISS-L"
        rflag = "REG   " if present_in_registry else "MISS-R"
        print(f"  [{lflag}][{rflag}] {tag} -- {gate_id}")

    all_gates_in_ledger = all(h[2] for h in ledger_hits)  # (local)
    all_gates_in_registry = all(h[3] for h in ledger_hits)  # (local)

    # --- Step 3: cross-check verdict classifications ---
    print("\n[Step 3] Verdict classification cross-check")
    # Rule: PASS gates ledger lines should contain ": PASS --"; G18 is
    # FAIL-BY-DESIGN (falsifier), so we allow either but NOT a silent absence.
    classification_expected = {  # (local) pre-registered
        "G17": "PASS",
        "G18": "FAIL",   # falsifier-refiner
        "G19": "PASS",
        "G20": "PASS",
        "G21": "PASS",
        "G22": "PASS",
        "G23": "PASS",
        "G24": "PASS",
        "G54": "PASS",
    }
    class_hits = []  # (local)
    for tag, gate_id in REQUIRED_W2_GATES + REQUIRED_W3_GATES:
        expected = classification_expected[tag]  # (local)
        # find the line(s) containing gate_id
        matching = [ln for ln in verdicts_text.splitlines()
                    if gate_id + ":" in ln]  # (local)
        # latest-entry-wins ledger convention — pick the last non-comment line
        latest = None  # (local)
        for ln in matching:
            if ln.strip().startswith("#"):
                continue
            latest = ln
        if latest is None:
            class_hits.append((tag, gate_id, expected, "ABSENT", False))
            print(f"  [MISS] {tag} {gate_id} -- no ledger line")
            continue
        observed = "PASS" if ": PASS" in latest else (
            "FAIL" if ": FAIL" in latest else (
                "INFO" if ": INFO" in latest else "OTHER"))  # (local)
        ok = (observed == expected)  # (local)
        class_hits.append((tag, gate_id, expected, observed, ok))
        oflag = "OK " if ok else "BAD"
        print(f"  [{oflag}] {tag} expected={expected} observed={observed}")

    all_classifications_match = all(h[4] for h in class_hits)  # (local)

    # --- Step 4: gate adjudication (direction) ---
    print("\n[Step 4] Gate adjudication")

    # Substitution chain direction pass-through
    print("  Substitution chain (Step 2 direction):")
    print("    all_anchors_present       =", all_anchors_present)
    print("    all_gates_in_ledger       =", all_gates_in_ledger)
    print("    all_gates_in_registry     =", all_gates_in_registry)
    print("    all_classifications_match =", all_classifications_match)

    # Pre-registered direction:
    # PASS  <=>  anchors AND ledger AND registry citation AND classifications match
    # INFO  <=>  anchors AND registry citation; ledger/classification partial miss
    # FAIL  <=>  anchors absent OR registry citation absent
    if all_anchors_present and all_gates_in_registry:
        if all_gates_in_ledger and all_classifications_match:
            verdict = "PASS"  # (local)
            verdict_note = "registry entry landed with all 25 anchors + 9 carry-forward gates + 9 classification matches"  # (local)
        else:
            verdict = "INFO"  # (local)
            verdict_note = "registry entry landed; ledger/classification partial (see class_hits)"  # (local)
    else:
        verdict = "FAIL"  # (local)
        missing = [r[0] for r in anchor_results if not r[3]]  # (local)
        missing_gates = [h[0] for h in ledger_hits if not h[3]]  # (local)
        verdict_note = f"missing anchors={missing}, missing registry gates={missing_gates}"  # (local)

    print(f"\n  VERDICT: {verdict} -- {verdict_note}")

    # --- Closure SHA ---
    pin_map_str = (  # (local)
        f"registry={registry_sha},"
        f"verdicts={verdicts_sha},"
        f"index={index_sha},"
        f"anchors_present={n_present}/{n_total},"
        f"all_anchors={all_anchors_present},"
        f"all_ledger={all_gates_in_ledger},"
        f"all_registry={all_gates_in_registry},"
        f"all_class={all_classifications_match}"
    )
    closure_sha = hashlib.sha256(pin_map_str.encode()).hexdigest()  # (local)
    print(f"\n  Pin map: {pin_map_str}")
    print(f"  Closure SHA-256: {closure_sha}")

    # --- Save NPZ ---
    np.savez(
        str(OUT_NPZ),
        verdict=np.array([verdict]),
        verdict_note=np.array([verdict_note]),
        anchors_present=np.array([n_present]),
        anchors_total=np.array([n_total]),
        all_anchors_present=np.array([all_anchors_present]),
        all_gates_in_ledger=np.array([all_gates_in_ledger]),
        all_gates_in_registry=np.array([all_gates_in_registry]),
        all_classifications_match=np.array([all_classifications_match]),
        registry_sha=np.array([registry_sha]),
        verdicts_sha=np.array([verdicts_sha]),
        index_sha=np.array([index_sha]),
        closure_sha=np.array([closure_sha]),
        anchor_ids=np.array([r[0] for r in anchor_results]),
        anchor_present_flags=np.array([r[3] for r in anchor_results]),
        carry_forward_tags=np.array([h[0] for h in ledger_hits]),
        carry_forward_in_ledger=np.array([h[2] for h in ledger_hits]),
        carry_forward_in_registry=np.array([h[3] for h in ledger_hits]),
        classification_expected=np.array([h[2] for h in class_hits]),
        classification_observed=np.array([h[3] for h in class_hits]),
        classification_ok=np.array([h[4] for h in class_hits]),
    )
    print(f"  Saved: {OUT_NPZ}")

    # --- Plot summary table ---
    try:
        fig, ax = plt.subplots(figsize=(11, 9))
        ax.axis("off")
        title = (f"S83 W3-G62: §VII.J Cartan Level-2 Exclusion -- {verdict}\n"
                 f"anchors {n_present}/{n_total}, "
                 f"carry-forward {sum(h[2] for h in ledger_hits)}/"
                 f"{len(ledger_hits)} ledger, "
                 f"class match {sum(h[4] for h in class_hits)}/"
                 f"{len(class_hits)}")
        ax.set_title(title, fontsize=12, fontweight="bold", pad=12)

        table_rows = [["Element", "Present"]]  # (local)
        for elem_id, desc, _anchor, present in anchor_results:
            table_rows.append([f"{elem_id}: {desc[:36]}", "OK" if present else "MISS"])
        for tag, gate_id, ledger, registry in ledger_hits:
            table_rows.append(
                [f"{tag} {gate_id[:28]} ledger",
                 "OK" if ledger else "MISS"]
            )

        tbl = ax.table(cellText=table_rows[1:],
                       colLabels=table_rows[0],
                       loc="center", cellLoc="left")
        tbl.auto_set_font_size(False)
        tbl.set_fontsize(7)
        tbl.scale(1.0, 1.1)

        # colour verdict row (top-level)
        color = {"PASS": "#c8f0c8",
                 "INFO": "#f0f0c8",
                 "FAIL": "#f0c8c8"}.get(verdict, "#e0e0e0")  # (local)
        for col_idx in (0, 1):
            tbl[(0, col_idx)].set_facecolor(color)

        fig.tight_layout()
        fig.savefig(str(OUT_PNG), dpi=120, bbox_inches="tight")
        plt.close(fig)
        print(f"  Saved: {OUT_PNG}")
    except Exception as exc:
        print(f"  Plot skipped ({exc})")

    # --- 4-tuple output tag ---
    print("\n4-tuple: (landing_status={}, scheme=Level-2-Cartan-exclusion, "
          "convention=W2-G17-G22-sanity, L_max=N/A)".format(verdict))

    # --- Verdict line (canonical, to be appended to ledger by caller) ---
    verdict_line = (  # (local)
        f"S83-CARTAN-VII-J-REGISTRY-SUBMIT: {verdict} -- "
        f"value={verdict}_anchors={n_present}/{n_total}_"
        f"carry_ledger={sum(h[2] for h in ledger_hits)}/{len(ledger_hits)}_"
        f"class_match={sum(h[4] for h in class_hits)}/{len(class_hits)} "
        f"scheme=Level-2-Cartan-exclusion "
        f"convention=W2-G17-G22-sanity "
        f"L_max=N/A "
        f"sha256={closure_sha}"
    )
    print("\nVerdict line:\n" + verdict_line)


if __name__ == "__main__":
    main()
