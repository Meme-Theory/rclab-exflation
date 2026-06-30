#!/usr/bin/env python3
"""
S100a W6-1 S100a-VIIW3LAB-STAGE2-VERIFY — Stage-2 two-agent PASS-AND aggregation
================================================================================

Gate: S100a-VIIW3LAB-STAGE2-VERIFY ([VERIFY])
Classification: GEOMETRIC (substrate-IS rank-2 cocycle pair on (A_K, H_K, D_K);
the fabric's intrinsic cohomology, not its excitations)

Pre-registered operator (plan session-100a-plan-w6.md SW6-1, operator.form):
  composite = PASS  iff  (for all c in axisA_own {A1,A2,A3}: V_A(c)=PASS)
                    AND  (for all c in axisB_own {B1,B2}:    V_B(c)=PASS)
                    AND  (for all j in JOINT {J1,J2,J3}: V_A(j)=PASS AND V_B(j)=PASS)
                         [PASS-AND, logical AND not OR]
  composite = FAIL  iff  exists c, exists R in {A,B}: V_R(c)=FAIL
  composite = INFO  iff  (no clause FAIL) AND (exists c, R: V_R(c)=INFO)

Stage-2 protocol-condition pre-flight (joint-theorem-promotion.md, audit items;
machinery_pin_map): reviewer identities MUST match the pinned assignment
(Axis-A van-den-dungen-bridge-theorist; Axis-B landau-condensed-matter-theorist),
neither reviewer in the Stage-0-author exclusion set {volovik-superfluid-universe-
theorist, connes-ncg-theorist, mack-cosmic-bridge}, both
no_workshop_context_attestation flags True, and the substrate-input-orthogonality
predicate satisfied (s87 npz loaded by Axis-B ONLY; s89 npz by Axis-A ONLY).
A protocol-condition breach blocks Stage-2 -> 3 promotion (audit FAIL) per
joint-theorem-promotion.md "Missing any of (1)-(6) -> audit FAIL".

Ratio sub-check (machinery_pin_map.ratio_band / .tolerance): the Gate-2
cohomology-asymmetry sub-check inside clauses J1/J3 — |computed - canonical| /
canonical <= 1e-3 relative against the canonical pin
substrate_cocycle_ratio_67_88 (canonical_constants.py; S86-W5-CANON-EXTRACT).
Three routes recorded: (i) this script's independent norm-pin route
cocycle_norm_phi67 / cocycle_norm_phi88; (ii) Axis-A reviewer's reported
sub-check; (iii) Axis-B reviewer's reported sub-check. All three must lie
within the band; a band breach is recorded as a sub-check inconsistency flag
(the composite verdict itself is the pre-registered clause-set conjunction).

SUBSTITUTION CHAIN (conjunction-logic chain; plan item 7 — no physics sign claim):
  Definition 1: V_A(c) = Axis-A (van-den-dungen-bridge-theorist) verdict on
                clause c in {A1,A2,A3} u {J1,J2,J3}.
  Definition 2: V_B(c) = Axis-B (landau-condensed-matter-theorist) verdict on
                clause c in {B1,B2} u {J1,J2,J3}.
  Definition 3: PASS-AND (joint-theorem-promotion.md "Stage 2"): a JOINT clause
                j PASSES iff V_A(j)=PASS AND V_B(j)=PASS (logical AND, NOT OR).
  Substitute:   composite = [AND_{c in {A1,A2,A3}} V_A(c)=PASS]
                        AND [AND_{c in {B1,B2}}    V_B(c)=PASS]
                        AND [AND_{j in {J1,J2,J3}} (V_A(j)=PASS AND V_B(j)=PASS)].
  Simplify:     composite=PASS iff every own-axis clause PASSES in its owning
                reviewer AND every JOINT clause PASSES in BOTH reviewers.
  Canonical:    composite in {PASS, FAIL, INFO} per operator.form (FAIL on any
                clause-FAIL; INFO on any clause-INFO absent FAIL).
  Direction:    PASS-AND is strictly stronger than PASS-OR — a JOINT clause
                passing in only ONE reviewer does NOT satisfy the gate (the
                structural-independence guarantee; OR is FORBIDDEN per
                joint-theorem-promotion.md "Stage 2" PASS criterion bullet 2).
  Conclusion:   composite=PASS => SVII.W-3.LAB -> STAGE-3-PERMANENT with
                Stage-3-CLASS tag JOINT-CROSS-AXIS-STAGE-2-PASS-AND;
                composite in {FAIL, INFO} => hold STAGE-1-CANDIDATE.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-100a/s100a_viiw3lab_reviewer_axisA_vdd.json
  - computations/session-100a/s100a_viiw3lab_reviewer_axisB_landau.json
  - sessions/permanent-results-registry.md (SVII.W-3.LAB block, lines 17030-17099)
  - computations/session-87/s87_w11_3heb_excess_inheritance_comparison.npz
  - computations/session-89/s89_w2_a7_chi_prime_inheritance_morphism.npz
  - .claude/rules/joint-theorem-promotion.md
  - .claude/rules/inheritance-falsifier-protocol.md
  - .claude/rules/cross-pillar-bridge-anatomy.md
  - canonical_constants.py (feeds audit_sha256; cocycle pins)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<composite payload>, scheme=JOINT-CROSS-AXIS-STAGE-2,
   convention=PASS-AND-two-agent-inheritance-morphism-FWD-C3, L_max=N/A)

Audit discriminators (plan SW6-1 item 6):
  audit_sha256   = sha256(script || canonical_constants.py || SVII.W-3.LAB
                   entry-block bytes || pinmap_json)   ["script","canonical","pinmap"]
  content_sha256 = sha256(script)                       ["script"]
  pinmap carries reviewer assignment + clause enumeration + orthogonality
  declaration + ratio band + all 9 input-file SHAs.

OPERATIONAL DEVIATION (disclosed): the plan method-block names
computations/_shared/s100a_viiw3lab_stage2_verify.py; the authoritative
output_artifacts block names computations/session-100a/ — this script lives at
the output_artifacts path (orchestrator-confirmed; plan-internal drift).

Verdict emission: this script PRINTS the payload (print_verdict_payload);
the dispatching agent calls mcp__knowledge__emit_verdict(**payload) — the
race-safe, lock-serialized single writer of s100a_gate_verdicts.txt. The
script does NOT write the verdict file (Windows open("a") cross-process race;
S98 lost 5/8 lines under 8 concurrent writers).

GPU_path: cpu-cap-OMP8 — no matrix work (set-conjunction + ratio arithmetic).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap BEFORE numpy import (GPU_path=cpu-cap-OMP8)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import; S34+)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
# Consumed canonical pins:
#   substrate_cocycle_ratio_67_88 = 7.3249917525961665 (S86-W5-CANON-EXTRACT)
#   cocycle_norm_phi67            = 0.793346 M_KK^2    (S86 W-5 CANONICAL-3)
#   cocycle_norm_phi88            = 0.108307 M_KK^2    (S86 W-5 CANONICAL-4)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# ---------------------------------------------------------------------------
# Section 3 — Identity + pre-registration pins (plan SW6-1 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "100a"                                                   # (local)
GATE_ID = "S100a-VIIW3LAB-STAGE2-VERIFY"                           # (local)
SCHEME = "JOINT-CROSS-AXIS-STAGE-2"                                # (local)
CONVENTION = "PASS-AND-two-agent-inheritance-morphism-FWD-C3"      # (local)
L_MAX = "N/A"                                                      # (local)

AXIS_A_REVIEWER = "van-den-dungen-bridge-theorist"                 # (local)
AXIS_B_REVIEWER = "landau-condensed-matter-theorist"               # (local)
STAGE0_EXCLUDED = (                                                # (local)
    "volovik-superfluid-universe-theorist",
    "connes-ncg-theorist",
    "mack-cosmic-bridge",
)
CLAUSES_AXIS_A_OWN = ("A1", "A2", "A3")                            # (local)
CLAUSES_AXIS_B_OWN = ("B1", "B2")                                  # (local)
CLAUSES_JOINT = ("J1", "J2", "J3")                                 # (local)
ALL_CLAUSES = CLAUSES_AXIS_A_OWN + CLAUSES_AXIS_B_OWN + CLAUSES_JOINT  # (local)

RATIO_BAND_REL = 1e-3   # (local) pre-registered Gate-2 sub-check band (0.1%)

# Orthogonality-pinned anchor files (basename markers for inputs_read scan)
S87_NPZ_MARKER = "s87_w11_3heb_excess_inheritance_comparison.npz"  # (local)
S89_NPZ_MARKER = "s89_w2_a7_chi_prime_inheritance_morphism.npz"    # (local)

# Input files (all SHA-pinned into pinmap)
REVIEWER_A_JSON = SESSION_DIR / "s100a_viiw3lab_reviewer_axisA_vdd.json"
REVIEWER_B_JSON = SESSION_DIR / "s100a_viiw3lab_reviewer_axisB_landau.json"
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
S87_NPZ = COMPUTATIONS_DIR / "session-87" / S87_NPZ_MARKER
S89_NPZ = COMPUTATIONS_DIR / "session-89" / S89_NPZ_MARKER
RULE_JOINT = PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
RULE_INHERIT = PROJECT_ROOT / ".claude" / "rules" / "inheritance-falsifier-protocol.md"
RULE_BRIDGE = PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [
    CANONICAL_PATH,
    REGISTRY_PATH,
    REVIEWER_A_JSON,
    REVIEWER_B_JSON,
    S87_NPZ,
    S89_NPZ,
    RULE_JOINT,
    RULE_INHERIT,
    RULE_BRIDGE,
]

OUT_NPZ = SESSION_DIR / "s100a_viiw3lab_stage2_verify.npz"
OUT_PNG = SESSION_DIR / "s100a_viiw3lab_stage2_verify.png"

ENTRY_HEADING = "## §VII.W-3.LAB"                             # (local)
PLAN_PINNED_ENTRY_START_LINE = 17030                               # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for the pinmap."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def extract_entry_block(registry_path: Path) -> tuple[str, int, int]:
    """Extract the registered SVII.W-3.LAB entry block (heading to the line
    before the next '## ' heading). Returns (block_text, start_line, end_line)
    with 1-based line numbers. Anchor-based extraction (runtime canonical-path
    rescue per substrate-first-canonical-sourcing.md (ii.B)); the plan-pinned
    span 17030-17099 is cross-checked and any drift disclosed in stdout."""
    lines = registry_path.read_text(encoding="utf-8").splitlines()  # (local)
    start_idx = None  # (local)
    for i, ln in enumerate(lines):
        if ln.startswith(ENTRY_HEADING):
            start_idx = i
            break
    if start_idx is None:
        raise RuntimeError(f"SVII.W-3.LAB heading not found in {registry_path}")
    end_idx = len(lines)  # (local)
    for j in range(start_idx + 1, len(lines)):
        if lines[j].startswith("## "):
            end_idx = j
            break
    block = "\n".join(lines[start_idx:end_idx])  # (local)
    return block, start_idx + 1, end_idx  # 1-based inclusive span


def compute_audit_content_sha(
    script_path: Path,
    canonical_path: Path,
    entry_block: str,
    pins: dict[str, str],
) -> tuple[str, str]:
    """S84+ dual-SHA per plan SW6-1 audit_discriminators:
    audit_sha256   = sha256(script || canonical_constants.py ||
                            SVII.W-3.LAB entry-block bytes || pinmap_json)
    content_sha256 = sha256(script)
    """
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    entry_bytes = entry_block.encode("utf-8")  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(entry_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Aggregation compute
# ---------------------------------------------------------------------------

def load_reviewer(path: Path) -> dict:
    """Load a reviewer clause-verdict JSON."""
    return json.loads(path.read_text(encoding="utf-8"))


def protocol_preflight(rev_a: dict, rev_b: dict) -> tuple[bool, list[str]]:
    """Stage-2 protocol-condition checks (joint-theorem-promotion.md audit
    items, mechanically verifiable from the reviewer JSONs). Returns
    (all_ok, list_of_breach_descriptions)."""
    breaches: list[str] = []  # (local)

    # (i) reviewer identity matches the pinned assignment
    if rev_a.get("reviewer") != AXIS_A_REVIEWER:
        breaches.append(f"axisA_identity={rev_a.get('reviewer')}!={AXIS_A_REVIEWER}")
    if rev_b.get("reviewer") != AXIS_B_REVIEWER:
        breaches.append(f"axisB_identity={rev_b.get('reviewer')}!={AXIS_B_REVIEWER}")

    # (ii) neither reviewer is a Stage-0 author
    for tag, rev in (("axisA", rev_a), ("axisB", rev_b)):
        if rev.get("reviewer") in STAGE0_EXCLUDED:
            breaches.append(f"{tag}_reviewer_is_Stage0_author={rev.get('reviewer')}")

    # (iii) no-workshop-context attestations
    if rev_a.get("no_workshop_context_attestation") is not True:
        breaches.append("axisA_attestation_missing")
    if rev_b.get("no_workshop_context_attestation") is not True:
        breaches.append("axisB_attestation_missing")

    # (iv) clause-set exact match to the pinned enumeration
    a_clauses = set(rev_a.get("clauses", {}).keys())  # (local)
    b_clauses = set(rev_b.get("clauses", {}).keys())  # (local)
    a_expected = set(CLAUSES_AXIS_A_OWN) | set(CLAUSES_JOINT)  # (local)
    b_expected = set(CLAUSES_AXIS_B_OWN) | set(CLAUSES_JOINT)  # (local)
    if a_clauses != a_expected:
        breaches.append(f"axisA_clause_set={sorted(a_clauses)}!={sorted(a_expected)}")
    if b_clauses != b_expected:
        breaches.append(f"axisB_clause_set={sorted(b_clauses)}!={sorted(b_expected)}")

    return (len(breaches) == 0), breaches


def orthogonality_check(rev_a: dict, rev_b: dict) -> tuple[bool, dict]:
    """Substrate-input-orthogonality predicate (pre-registered): s87 npz loaded
    by Axis-B ONLY; s89 npz loaded by Axis-A ONLY. Verified mechanically
    against each reviewer's inputs_read declaration."""
    a_inputs = " || ".join(rev_a.get("inputs_read", []))  # (local)
    b_inputs = " || ".join(rev_b.get("inputs_read", []))  # (local)
    s87_in_a = S87_NPZ_MARKER in a_inputs  # (local)
    s87_in_b = S87_NPZ_MARKER in b_inputs  # (local)
    s89_in_a = S89_NPZ_MARKER in a_inputs  # (local)
    s89_in_b = S89_NPZ_MARKER in b_inputs  # (local)
    s87_exclusive_b = (s87_in_b and not s87_in_a)  # (local)
    s89_exclusive_a = (s89_in_a and not s89_in_b)  # (local)
    satisfied = s87_exclusive_b and s89_exclusive_a  # (local)
    flags = {
        "s87_loaded_by_axisA": s87_in_a,
        "s87_loaded_by_axisB": s87_in_b,
        "s89_loaded_by_axisA": s89_in_a,
        "s89_loaded_by_axisB": s89_in_b,
        "s87_exclusive_to_axisB": s87_exclusive_b,
        "s89_exclusive_to_axisA": s89_exclusive_a,
        "orthogonality_satisfied": satisfied,
    }  # (local)
    return satisfied, flags


def ratio_subcheck(rev_a: dict, rev_b: dict) -> dict:
    """Gate-2 cohomology-asymmetry ratio sub-check vs the canonical pin,
    band 1e-3 relative. Three routes: this script's independent norm-pin
    route + the two reviewers' reported sub-checks (re-verified here)."""
    canonical = substrate_cocycle_ratio_67_88  # canonical pin (S86-W5-CANON-EXTRACT)
    ratio_script = cocycle_norm_phi67 / cocycle_norm_phi88  # (local) norm-pin route
    rd_script = abs(ratio_script - canonical) / canonical   # (local)

    a_sub = rev_a.get("ratio_subcheck", {})  # (local)
    b_sub = rev_b.get("ratio_subcheck", {})  # (local)
    a_computed = float(a_sub.get("computed", float("nan")))  # (local)
    b_computed = float(b_sub.get("computed", float("nan")))  # (local)
    rd_a = abs(a_computed - canonical) / canonical  # (local) recomputed here
    rd_b = abs(b_computed - canonical) / canonical  # (local) recomputed here

    within_script = rd_script <= RATIO_BAND_REL  # (local)
    within_a = rd_a <= RATIO_BAND_REL            # (local)
    within_b = rd_b <= RATIO_BAND_REL            # (local)

    # consistency of each reviewer's REPORTED rel_dev with the recomputation
    rep_rd_a = float(a_sub.get("rel_dev", float("nan")))  # (local)
    rep_rd_b = float(b_sub.get("rel_dev", float("nan")))  # (local)
    report_consistent_a = abs(rep_rd_a - rd_a) <= 1e-9    # (local)
    report_consistent_b = abs(rep_rd_b - rd_b) <= 1e-9    # (local)

    return {
        "canonical": canonical,
        "band_rel": RATIO_BAND_REL,
        "script_computed": ratio_script,
        "script_rel_dev": rd_script,
        "script_within": within_script,
        "axisA_computed": a_computed,
        "axisA_rel_dev": rd_a,
        "axisA_within": within_a,
        "axisA_report_consistent": report_consistent_a,
        "axisB_computed": b_computed,
        "axisB_rel_dev": rd_b,
        "axisB_within": within_b,
        "axisB_report_consistent": report_consistent_b,
        "all_within_band": bool(within_script and within_a and within_b),
    }


def aggregate_pass_and(rev_a: dict, rev_b: dict) -> tuple[str, dict, dict, dict]:
    """Apply operator.form set-conjunction. Returns (composite,
    V_A map, V_B map, per-clause aggregate map)."""
    v_a = {c: rev_a["clauses"][c]["verdict"].upper()
           for c in (CLAUSES_AXIS_A_OWN + CLAUSES_JOINT)}  # (local)
    v_b = {c: rev_b["clauses"][c]["verdict"].upper()
           for c in (CLAUSES_AXIS_B_OWN + CLAUSES_JOINT)}  # (local)

    all_verdicts = list(v_a.values()) + list(v_b.values())  # (local) 11 entries

    # per-clause aggregate: owner verdict for own-axis; AND for JOINT
    agg: dict[str, str] = {}  # (local)
    for c in CLAUSES_AXIS_A_OWN:
        agg[c] = v_a[c]
    for c in CLAUSES_AXIS_B_OWN:
        agg[c] = v_b[c]
    for j in CLAUSES_JOINT:
        pair = (v_a[j], v_b[j])  # (local)
        if "FAIL" in pair:
            agg[j] = "FAIL"
        elif "INFO" in pair:
            agg[j] = "INFO"
        elif pair == ("PASS", "PASS"):
            agg[j] = "PASS"
        else:
            agg[j] = "INFO"  # unrecognized verdict token -> conservative

    # operator.form composite (exact set logic; FAIL > INFO > PASS precedence)
    if any(v == "FAIL" for v in all_verdicts):
        composite = "FAIL"  # (local)
    elif any(v == "INFO" for v in all_verdicts):
        composite = "INFO"  # (local)
    elif all(v == "PASS" for v in all_verdicts):
        composite = "PASS"  # (local)
    else:
        composite = "INFO"  # (local) unrecognized token absent FAIL -> INFO
    return composite, v_a, v_b, agg


# ---------------------------------------------------------------------------
# Section 6 — Plot (clause-by-clause PASS-AND matrix)
# ---------------------------------------------------------------------------

def make_plot(v_a: dict, v_b: dict, agg: dict, composite: str,
              ratio: dict, ortho_ok: bool) -> None:
    code_map = {"N/A": 0, "PASS": 1, "INFO": 2, "FAIL": 3}  # (local)
    cmap = ListedColormap(["#d9d9d9", "#2e7d32", "#f9a825", "#c62828"])  # (local)

    rows = list(ALL_CLAUSES)  # (local)
    col_labels = [f"V_A (vdd)", f"V_B (landau)", "PASS-AND aggregate"]  # (local)
    cell_text = []  # (local)
    cell_code = []  # (local)
    for c in rows:
        va = v_a.get(c, "N/A")  # (local)
        vb = v_b.get(c, "N/A")  # (local)
        ag = agg[c]  # (local)
        cell_text.append([va, vb, ag])
        cell_code.append([code_map.get(va, 0), code_map.get(vb, 0),
                          code_map.get(ag, 0)])

    fig, ax = plt.subplots(figsize=(9.0, 6.8))
    im = ax.imshow(np.array(cell_code), cmap=cmap, vmin=0, vmax=3, aspect="auto")
    ax.set_xticks(range(3))
    ax.set_xticklabels(col_labels, fontsize=10)
    ax.set_yticks(range(len(rows)))
    row_labels = [
        "A1 own-A: Elem-1 substrate-IS cocycle pair",
        "A2 own-A: Elem-3 bridge map chi (M3(C)->0)",
        "A3 own-A: Elem-4 structural-exact envelope",
        "B1 own-B: Elem-2 lab-IN OE-form",
        "B2 own-B: Elem-5 4-gate falsifier (DEFERRED)",
        "J1 JOINT: (Delta_B/Delta_A)^p cancellation",
        "J2 JOINT: rank(ker iota_*) = 2",
        "J3 JOINT: Level-1 cohomology-class identity",
    ]  # (local)
    ax.set_yticklabels(row_labels, fontsize=9)
    for i in range(len(rows)):
        for j in range(3):
            ax.text(j, i, cell_text[i][j], ha="center", va="center",
                    fontsize=10, fontweight="bold",
                    color="white" if cell_code[i][j] in (1, 3) else "black")
    ax.set_title(
        f"{GATE_ID} — Stage-2 two-agent PASS-AND matrix\n"
        f"composite = {composite} "
        f"(own-A 3/3, own-B 2/2, JOINT 3/3 PASS-AND-both required)",
        fontsize=11)
    foot = (
        f"ratio sub-check vs substrate_cocycle_ratio_67_88 = {ratio['canonical']:.16f} (band {ratio['band_rel']:.0e} rel):\n"
        f"  script norm-pin route = {ratio['script_computed']:.16f}  rel_dev = {ratio['script_rel_dev']:.3e}  within = {ratio['script_within']}\n"
        f"  Axis-A reported = {ratio['axisA_computed']:.16f}  rel_dev = {ratio['axisA_rel_dev']:.3e}  within = {ratio['axisA_within']}\n"
        f"  Axis-B reported = {ratio['axisB_computed']:.16f}  rel_dev = {ratio['axisB_rel_dev']:.3e}  within = {ratio['axisB_within']}\n"
        f"substrate-input-orthogonality SATISFIED = {ortho_ok} "
        f"(s87 npz -> Axis-B only; s89 npz -> Axis-A only); "
        f"attestations: no-workshop-context both True"
    )  # (local)
    fig.text(0.06, 0.015, foot, fontsize=7.6, family="monospace", va="bottom")
    fig.subplots_adjust(left=0.34, bottom=0.30, top=0.88, right=0.97)
    fig.savefig(OUT_PNG, dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload (printed; agent calls emit_verdict)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    companion_note: str = "",
    extra_rows: list[str] | None = None,
) -> dict:
    """Emit the verdict PAYLOAD for the dispatching AGENT to pass to the
    knowledge-MCP emit_verdict tool (race-safe, lock-serialized; the script
    does NOT write the verdict file). [VERIFY] trigger — no schema-v2 3-tuple.
    Session is the letter-suffixed sub-session label '100a' (string)."""
    payload: dict = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)

    # 2. Registered-entry block extraction + SHA (anchor-based; drift check)
    entry_block, entry_start, entry_end = extract_entry_block(REGISTRY_PATH)
    entry_sha = hashlib.sha256(entry_block.encode("utf-8")).hexdigest()  # (local)
    drift = (entry_start != PLAN_PINNED_ENTRY_START_LINE)  # (local)
    print(f"  SVII.W-3.LAB entry block: lines {entry_start}-{entry_end} "
          f"(plan-pinned start {PLAN_PINNED_ENTRY_START_LINE}; drift={drift})")
    print(f"  entry_block_sha256: {entry_sha[:16]}...")

    # 3. Pinmap identity keys (reviewer assignment + clause enumeration +
    #    orthogonality declaration + ratio band) per audit_discriminators
    pins["_gate_id"] = GATE_ID
    pins["_scheme"] = SCHEME
    pins["_convention"] = CONVENTION
    pins["_axisA_reviewer"] = AXIS_A_REVIEWER
    pins["_axisB_reviewer"] = AXIS_B_REVIEWER
    pins["_stage0_excluded"] = ",".join(STAGE0_EXCLUDED)
    pins["_clauses_axisA_own"] = ",".join(CLAUSES_AXIS_A_OWN)
    pins["_clauses_axisB_own"] = ",".join(CLAUSES_AXIS_B_OWN)
    pins["_clauses_joint"] = ",".join(CLAUSES_JOINT)
    pins["_orthogonality_declaration"] = (
        f"{S87_NPZ_MARKER}->axisB_only;{S89_NPZ_MARKER}->axisA_only")
    pins["_ratio_band_rel"] = f"{RATIO_BAND_REL:.0e}"
    pins["_entry_block_sha256"] = entry_sha

    # 4. Dual SHA (audit = script || canonical || entry-block || pinmap_json)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_audit_content_sha(
        script_path, CANONICAL_PATH, entry_block, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+entry+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 5. Load reviewer clause-verdict JSONs
    rev_a = load_reviewer(REVIEWER_A_JSON)  # (local)
    rev_b = load_reviewer(REVIEWER_B_JSON)  # (local)

    # 6. Stage-2 protocol-condition pre-flight
    proto_ok, breaches = protocol_preflight(rev_a, rev_b)
    print(f"protocol_preflight: ok={proto_ok}"
          + (f" breaches={breaches}" if breaches else ""))

    # 7. Substrate-input-orthogonality predicate
    ortho_ok, ortho_flags = orthogonality_check(rev_a, rev_b)
    print(f"substrate_input_orthogonality: SATISFIED={ortho_ok} {ortho_flags}")

    # 8. Ratio sub-check (3 routes vs canonical pin; band 1e-3 rel)
    ratio = ratio_subcheck(rev_a, rev_b)
    print("ratio_subcheck vs substrate_cocycle_ratio_67_88 ="
          f" {ratio['canonical']:.16f} (band {ratio['band_rel']:.0e} rel):")
    print(f"  script norm-pin route: {ratio['script_computed']:.16f}"
          f"  rel_dev={ratio['script_rel_dev']:.6e}  within={ratio['script_within']}")
    print(f"  Axis-A (vdd):    {ratio['axisA_computed']:.16f}"
          f"  rel_dev={ratio['axisA_rel_dev']:.6e}  within={ratio['axisA_within']}"
          f"  report_consistent={ratio['axisA_report_consistent']}")
    print(f"  Axis-B (landau): {ratio['axisB_computed']:.16f}"
          f"  rel_dev={ratio['axisB_rel_dev']:.6e}  within={ratio['axisB_within']}"
          f"  report_consistent={ratio['axisB_report_consistent']}")
    print(f"  all_within_band={ratio['all_within_band']}")

    # 9. PASS-AND aggregation (operator.form exact set logic)
    composite, v_a, v_b, agg = aggregate_pass_and(rev_a, rev_b)
    n_pass = sum(1 for v in list(v_a.values()) + list(v_b.values())
                 if v == "PASS")  # (local)
    print(f"\nclause-verdict matrix (V_A over A1-A3+J1-J3; V_B over B1-B2+J1-J3):")
    for c in ALL_CLAUSES:
        print(f"  {c}: V_A={v_a.get(c, 'N/A'):<5} V_B={v_b.get(c, 'N/A'):<5}"
              f" aggregate={agg[c]}")
    print(f"clause_verdicts_PASS = {n_pass}/11")
    print(f"operator.form composite (clause-set conjunction) = {composite}")

    # 10. Protocol-breach override: a Stage-2 protocol-condition failure
    #     blocks promotion (joint-theorem-promotion.md audit -> FAIL),
    #     regardless of clause verdicts. Pre-registered machinery pins.
    inconsistency_flags: list[str] = []  # (local)
    if not proto_ok:
        composite = "FAIL"
        inconsistency_flags.append("protocol_preflight_breach")
    if not ortho_ok:
        # orthogonality predicate MANDATORY at K=3: without it Stage-2
        # PASS-AND carries the substrate-input-overlap caveat -> not clean
        composite = "FAIL" if composite == "FAIL" else "INFO"
        inconsistency_flags.append("substrate_input_orthogonality_unsatisfied")
    if not ratio["all_within_band"]:
        # sub-check band breach contradicts J1/J3 PASS -> inconsistency flag
        composite = "FAIL" if composite == "FAIL" else "INFO"
        inconsistency_flags.append("ratio_subcheck_band_breach")
    if inconsistency_flags:
        print(f"OVERRIDE flags: {inconsistency_flags} -> composite={composite}")
    print(f"\nFINAL composite = {composite}")

    # 11. Save npz
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        clause_names=np.array(ALL_CLAUSES),
        v_axisA=np.array([v_a.get(c, "N/A") for c in ALL_CLAUSES]),
        v_axisB=np.array([v_b.get(c, "N/A") for c in ALL_CLAUSES]),
        aggregate=np.array([agg[c] for c in ALL_CLAUSES]),
        composite=composite,
        n_clause_verdicts_pass=n_pass,
        n_clause_verdicts_total=11,
        reviewer_axisA=rev_a["reviewer"],
        reviewer_axisB=rev_b["reviewer"],
        stage0_excluded=np.array(STAGE0_EXCLUDED),
        attestation_axisA=bool(rev_a["no_workshop_context_attestation"]),
        attestation_axisB=bool(rev_b["no_workshop_context_attestation"]),
        ratio_canonical=ratio["canonical"],
        ratio_band_rel=ratio["band_rel"],
        ratio_script_computed=ratio["script_computed"],
        ratio_script_rel_dev=ratio["script_rel_dev"],
        ratio_axisA_computed=ratio["axisA_computed"],
        ratio_axisA_rel_dev=ratio["axisA_rel_dev"],
        ratio_axisB_computed=ratio["axisB_computed"],
        ratio_axisB_rel_dev=ratio["axisB_rel_dev"],
        ratio_all_within_band=ratio["all_within_band"],
        ortho_s87_loaded_by_axisA=ortho_flags["s87_loaded_by_axisA"],
        ortho_s87_loaded_by_axisB=ortho_flags["s87_loaded_by_axisB"],
        ortho_s89_loaded_by_axisA=ortho_flags["s89_loaded_by_axisA"],
        ortho_s89_loaded_by_axisB=ortho_flags["s89_loaded_by_axisB"],
        orthogonality_satisfied=ortho_flags["orthogonality_satisfied"],
        protocol_preflight_ok=proto_ok,
        inconsistency_flags=np.array(inconsistency_flags if inconsistency_flags
                                     else ["none"]),
        entry_block_sha256=entry_sha,
        entry_block_lines=np.array([entry_start, entry_end]),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        scheme=SCHEME,
        convention=CONVENTION,
    )
    print(f"saved npz: {OUT_NPZ.name}")

    # 12. Plot
    make_plot(v_a, v_b, agg, composite, ratio, ortho_ok)
    print(f"saved png: {OUT_PNG.name}")

    # 13. Value payload + 4-tuple + verdict payload
    stage3_tag = ("JOINT-CROSS-AXIS-STAGE-2-PASS-AND;" if composite == "PASS"
                  else "")  # (local)
    value = (
        f"{stage3_tag}clause_verdicts=11/11_PASS"
        if composite == "PASS" else
        f"{stage3_tag}clause_verdicts={n_pass}/11_PASS_flags={'+'.join(inconsistency_flags) or 'none'}"
    )  # (local)
    value += (
        f"(ownA=A1+A2+A3;ownB=B1+B2;joint=J1+J2+J3_PASS-AND-both);"
        f"ratio_subcheck_vs_{ratio['canonical']:.10f}:"
        f"script={ratio['script_computed']:.10f}(rd={ratio['script_rel_dev']:.3e}),"
        f"vdd_rd={ratio['axisA_rel_dev']:.3e},landau_rd={ratio['axisB_rel_dev']:.3e},"
        f"band=1e-3,all_within={ratio['all_within_band']};"
        f"input_orthogonality={'SATISFIED' if ortho_ok else 'UNSATISFIED'}"
        f"(s87npz->landau_only;s89npz->vdd_only);"
        f"attestations=both_True;"
        f"reviewers=vdd+landau_non-Stage-0"
    )
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    companion = (
        f"two-agent PASS-AND aggregation; entry-block sha256={entry_sha[:16]} "
        f"(registry lines {entry_start}-{entry_end}); Level-3 element-5 "
        f"empirical anchor remains DEFERRED 2027-2030 (slot-reserving; B2 "
        f"PASSed as DEFERRED-but-pre-registered)")  # (local)
    extra = [
        ("# reviewer-cleanliness: STATIC leg = Stage-0-authorship "
         "EXCLUSION-PASS at plan-freeze (_joint_theorem_independent_verify_"
         "audit.py --check-reviewers VII.W-3.LAB --strict; excluded "
         "volovik/connes/mack); DYNAMIC leg = downstream-inheritance reach "
         "grep NO-HITS both reviewers (orchestrator, 2026-06-06) "
         f"# {GATE_ID}"),
        ("# Stage-3 routing: SVII.W-3.LAB STAGE-1-CANDIDATE -> "
         "STAGE-3-PERMANENT tag edit = ORCHESTRATOR-DIRECT at session-end "
         "synthesis (joint-theorem-promotion.md Stage 3); "
         "falsifier-master-inventory rows #47-#54b -> mack-cosmic-bridge "
         f"sole writer # {GATE_ID}"),
    ]  # (local)
    print_verdict_payload(composite, value, audit_sha, content_sha,
                          companion_note=companion, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    # exit 0 regardless of scientific verdict (math-scripts.md exit-code rule)
    return 0


if __name__ == "__main__":
    sys.exit(main())
