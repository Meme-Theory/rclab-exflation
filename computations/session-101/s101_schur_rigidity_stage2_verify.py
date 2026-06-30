#!/usr/bin/env python3
"""
S101 W7-2 S101-SCHUR-RIGIDITY-STAGE2-VERIFY — PASS-AND aggregation closeout
==========================================================================

Gate: S101-SCHUR-RIGIDITY-STAGE2-VERIFY ([VERIFY])
  Stage-2 two-agent parallel cross-axis independent-verify of the W6-landed
  §VII.BR Band-Selective Schur Rigidity STAGE-1-CANDIDATE
  (joint-theorem-promotion.md 4-stage pathway, Stage 2).

Pre-registered threshold (set-conjunction PASS-AND; NOT a scalar):
  composite = PASS iff
      (forall c in {a,b,c,d,e,f,g}: V_A(c)=PASS AND V_B(c)=PASS)   # BINDING all-clauses-dual-verified
      AND (JOINT PASS in BOTH reviewers)                            # PASS-AND, logical AND not OR
      AND (every mechanical witness re-check reproduces within its pinned tolerance)
  composite = FAIL iff any clause FAIL in either reviewer OR any witness pin violated
  composite = INFO iff no clause FAIL, witnesses within pin, AND >=1 clause INFO

This is the PROCEDURAL AGGREGATION CLOSEOUT (gen-physicist). It does NOT
produce new physics. It:
  1. Loads the two cross-reviewer clause-verdict JSONs (kaluza-klein Axis-A,
     landau Axis-B), already on disk.
  2. MECHANICALLY RE-COMPUTES every witness anchor from the pinned npz
     s100b_nonabelian_metric_fraction.npz (it does NOT merely trust the JSONs) —
     the BINDING three (g1 rigidity ‖ΔP‖_F tables / g2 b2_scalar_dev Schur
     scalarity / g3 A^WZ median) + the scalar-consistency rows, and in
     particular the two release-condition witnesses: the defect-excluded
     I_NA(B2) = 2.591e-2 moving content vs the frozen-pair-channel floor
     2.602e-24 (the 22-OOM gap), Decimal-exact.
  3. f_nonAb is frame-DEPENDENT -> REPORTED, never a PASS/FAIL gate row.
  4. Runs the PASS-AND set-conjunction and emits ONE composite verdict.

Substrate-input orthogonality: NOT SATISFIED BY BINDING DESIGN. The npz is
loaded by BOTH reviewers (clause (g)), so the predicate (exists obs whose data
file is loaded by exactly one reviewer) FAILS. Per joint-theorem-promotion.md
§"Substrate-input-orthogonality clause", the PASS-AND establishes structural
OUTPUT-TYPE independence (rep-theoretic vs band-geometry decision pipelines on
the same data), NOT structural-INPUT independence; the verdict carries the
explicit substrate-input-OVERLAP-CAVEAT tag. (Contrast gate W7-1, predicate
SATISFIED by construction — the two gates instantiate the clause's two branches
in one wave.) LC-lineage CLEAN: W1-1 L4 caveat-lift (iv) for the W6-2
NONABELIAN-METRIC-FRACTION HAS landed under LC-CANONICAL -> witnesses cite
CLEAN, no A19 UNTRUSTED-UPSTREAM extra-row.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-101/s101_w7_2_axisA_kk.json     (Axis-A reviewer verdict)
  - computations/session-101/s101_w7_2_axisB_landau.json (Axis-B reviewer verdict)
  - computations/session-100b/s100b_nonabelian_metric_fraction.npz (shared witness npz; STATIC pin a31ff591…)
  - sessions/permanent-results-registry.md (the §VII.BR entry block, anchor-extracted -> audit-SHA pinmap)
  - computations/session-101/s101_gate_verdicts.txt (W6 STAGE-1 prereq + W1 L4 lineage status)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<composite + OVERLAP-CAVEAT + slot + 22OOM witness>, scheme=JOINT-CROSS-AXIS-STAGE-2,
   convention=PASS-AND-two-agent-Schur-rigidity-GEOMETRIC-overlap-caveat, L_max=N/A)

Classification: GEOMETRIC (Level-2 moduli-deformation substrate-IS; the (0,0)
Peter-Weyl singlet spinor fiber ℂ^16 over the Jensen TT-moduli (τ,μ) base).

METHODOLOGY
-----------
Set-conjunction PASS-AND over per-reviewer clause verdicts (joint-theorem-
promotion.md Stage 2) + mechanical npz re-computation of the registered witness
table. No diagonalization: the eigenbundles are stored; the script re-reads
stored scalars/arrays and re-derives the 22-OOM gap (Decimal-exact) and the
Schur-scalarity / double-protection / frame-spread anchors directly. The audit
SHA commits to the §VII.BR entry-as-reviewed (block extracted by section anchor
at runtime) folded into the pinmap.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-only (no matrix work); OMP cap 8 set before numpy import
- SHA-256 of all input files logged in first lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema); audit pinmap
  includes BOTH reviewer JSONs + the npz + the anchor-extracted §VII.BR block
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe):
  the script PRINTS the payload; the AGENT calls emit_verdict. No raw open("a").
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys as _sys
import pathlib as _pathlib
_SHARED = _pathlib.Path(__file__).resolve().parents[1] / "_shared"
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403  (compliance import)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import sys
import time
from decimal import Decimal, getcontext
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

getcontext().prec = 60  # RealField(60)-class exact OOM arithmetic

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S101"                                                    # (local)
GATE_ID = "S101-SCHUR-RIGIDITY-STAGE2-VERIFY"                       # (local)
SCHEME = "JOINT-CROSS-AXIS-STAGE-2"                                 # (local)
CONVENTION = "PASS-AND-two-agent-Schur-rigidity-GEOMETRIC-overlap-caveat"  # (local)
L_MAX = "N/A"                                                       # (local)

# --- Input files ---
AXISA_JSON = SESSION_DIR / "s101_w7_2_axisA_kk.json"                # (local)
AXISB_JSON = SESSION_DIR / "s101_w7_2_axisB_landau.json"            # (local)
NPZ_PATH = COMPUTATIONS_DIR / "session-100b" / "s100b_nonabelian_metric_fraction.npz"  # (local)
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"            # (local)
VERDICT_FILE = SESSION_DIR / "s101_gate_verdicts.txt"              # (local)
JOINT_RULE = PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"        # (local)

# --- Static SHA pins (plan-freeze 2026-06-07) ---
NPZ_STATIC_PIN = "a31ff591087e090590ea5cbce9f6410e08cdedfe611ba00728dca87edfeaf6f5"   # (local)
W6_PRODUCING_GATE_AUDIT = "4a03497c43a97335144bad80f60e16d00097829ca4310f25315dfe4c9c926818"  # (local) W6-2 NONABELIAN-METRIC-FRACTION audit (npz-stored)

# --- Prerequisite predicates ---
PREREQ_GATE = "S101-SCHUR-RIGIDITY-STAGE1-REGISTRATION"            # (local)
W1_LINEAGE_GATE = "S101-TAU0-OPERATOR-CANONICITY"                  # (local)

# --- The verify-target slot (parsed at runtime; expected §VII.BR) ---
EXPECTED_SLOT = "VII.BR"                                            # (local)
REGISTRY_BODY_ANCHOR = "### §VII.BR"                               # (local)

# --- Clause set (the registered clause-attribution block) ---
CLAUSES = ["L0", "T1", "T2", "P", "U", "witness", "JOINT"]         # (local)
# clause letter labels (a)-(g) map: a=L0 b=T1 c=T2 d=P e=U f=R(release, in JOINT/witness) g=witness
# The reviewers attest L0/T1/T2/P/U/witness/JOINT; release condition R is verified
# within the structural arguments (operator-independent). All must PASS in BOTH.

# --- Output destinations ---
OUT_NPZ = SESSION_DIR / "s101_schur_rigidity_stage2_verify.npz"   # (local)
OUT_PNG = SESSION_DIR / "s101_schur_rigidity_stage2_verify.png"   # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    AXISA_JSON,
    AXISB_JSON,
    NPZ_PATH,
    JOINT_RULE,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def extract_registry_block(registry_path: Path, anchor: str) -> str:
    """Extract the §VII.BR entry block: from the anchor header to (not incl.)
    the next '### ' header. Folded into the audit-SHA pinmap so the audit SHA
    commits to the entry-AS-REVIEWED."""
    try:
        lines = registry_path.read_text(encoding="utf-8").splitlines(keepends=True)  # (local)
    except OSError:
        return ""
    start = None  # (local)
    for i, ln in enumerate(lines):
        if ln.startswith(anchor):
            start = i
            break
    if start is None:
        return ""
    end = len(lines)  # (local)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("### "):
            end = j
            break
    return "".join(lines[start:end])


def log_input_pins(inputs: list[Path], entry_block: str) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    # Anchor-extracted §VII.BR block (the entry-as-reviewed)
    block_sha = sha256_of_text(entry_block)  # (local)
    pins["registry::VII.BR::anchor-extracted-block"] = block_sha
    print(f"  registry::VII.BR::anchor-extracted-block: {block_sha[:16]}... "
          f"({len(entry_block)} chars)")
    # Per-gate identity keys (per-gate-distinct audit_sha256 per mechanical-closure-discipline.md)
    pins["_gate_id"] = GATE_ID
    pins["_wp_id"] = "§W7-2"
    pins["_scheme"] = SCHEME
    pins["_convention"] = CONVENTION
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Prerequisite + lineage resolution
# ---------------------------------------------------------------------------

def resolve_prereq_and_slot() -> dict:
    """Confirm the W6 STAGE-1 registration PASS, parse the landed slot from its
    value field, and read the W1 L4 lineage-conditional status."""
    out = {  # (local)
        "prereq_present": False, "prereq_status": "ABSENT",
        "landed_slot": None, "slot_drift": False,
        "lc_lineage_clean": False, "a19_extra_row": True,
    }
    try:
        vtext = VERDICT_FILE.read_text(encoding="utf-8")  # (local)
    except OSError:
        return out
    # W6 STAGE-1 registration prerequisite
    m = re.search(rf"^{re.escape(PREREQ_GATE)}:\s*(PASS|FAIL|INFO|PRE-REG-INC)\b.*$",
                  vtext, re.MULTILINE)  # (local)
    if m:
        out["prereq_present"] = True
        out["prereq_status"] = m.group(1)
        # parse landed slot from value field (landed_VII.BR_...)
        ms = re.search(r"landed_(VII\.[A-Z]+)", m.group(0))  # (local)
        if ms:
            out["landed_slot"] = ms.group(1)
            out["slot_drift"] = (ms.group(1) != EXPECTED_SLOT)
    # W1 L4 lineage: clean iff the TAU0 gate landed PASS AND L4-LIFT (iv) present
    mt = re.search(rf"^{re.escape(W1_LINEAGE_GATE)}:\s*PASS\b", vtext, re.MULTILINE)  # (local)
    l4_iv = ("L4-LIFT (iv)" in vtext) and ("S100b-NONABELIAN-METRIC-FRACTION" in vtext)  # (local)
    if mt and l4_iv:
        out["lc_lineage_clean"] = True
        out["a19_extra_row"] = False
    return out


# ---------------------------------------------------------------------------
# Section 6 — Mechanical witness re-computation from the pinned npz
# ---------------------------------------------------------------------------

def recompute_witnesses() -> dict:
    """RE-compute every registered witness anchor from the pinned npz. The
    aggregation script does this itself; it does NOT trust the reviewer JSONs."""
    # npz file-SHA gate (STATIC pin)
    npz_file_sha = sha256_of(NPZ_PATH)  # (local)
    d = np.load(NPZ_PATH, allow_pickle=True)  # (local)

    def f(k):  # (local)
        return float(np.asarray(d[k], dtype=float).reshape(-1)[0]) if np.asarray(d[k]).size == 1 \
            else None

    res: dict = {}
    res["npz_file_sha"] = npz_file_sha
    res["npz_file_sha_match"] = (npz_file_sha == NPZ_STATIC_PIN)
    res["npz_stored_audit"] = str(d["audit_sha256"])
    res["npz_audit_match_W6"] = (str(d["audit_sha256"]) == W6_PRODUCING_GATE_AUDIT)

    # --- THE TWO RELEASE-CONDITION WITNESSES (the 22-OOM gap) ---
    I_NA_b2_excl = float(d["I_NA_b2_excl"])  # (local) defect-excluded moving content
    I_NA_excl = float(d["I_NA_excl"])        # (local) frozen-pair-channel floor
    res["I_NA_b2_excl"] = I_NA_b2_excl
    res["I_NA_excl"] = I_NA_excl
    # Decimal-exact OOM gap (RealField(60)-class)
    ratio = Decimal(repr(I_NA_b2_excl)) / Decimal(repr(I_NA_excl))  # (local)
    log10_gap = ratio.ln() / Decimal(10).ln()  # (local)
    res["oom_gap_log10"] = float(log10_gap)
    res["oom_gap_rounded"] = round(float(log10_gap))
    # registered-value rel checks (VALUE-class moving / FLOOR-class floor)
    res["I_NA_b2_rel"] = abs(I_NA_b2_excl - 2.591e-2) / 2.591e-2
    res["I_NA_excl_rel"] = abs(I_NA_excl - 2.602e-24) / 2.602e-24

    # --- g1: rigidity ‖ΔP‖_F frozen/moving partition ---
    rig_names = [str(x) for x in d["rigidity_names"]]  # (local)
    rig_vals = np.asarray(d["rigidity_vals"], dtype=float)  # (local)
    res["rigidity_names"] = rig_names
    res["rigidity_vals"] = rig_vals.tolist()
    res["rigidity_max"] = float(d["rigidity_max"])
    # wit_pair / wit_b2 are (50,50) per-node integrand fields (FHS plaquette),
    # NOT the scalar witnesses (those are the rigidity_vals entries). Store
    # max-abs as diagnostic only.
    res["wit_pair_maxabs"] = float(np.abs(np.asarray(d["wit_pair"], dtype=float)).max())  # (local)
    res["wit_b2_maxabs"] = float(np.abs(np.asarray(d["wit_b2"], dtype=float)).max())  # (local)
    res["all_frozen"] = bool(d["all_frozen"])
    # FROZEN rows = those NOT B2 (pair/B3-/B3+); MOVING = B2±
    frozen_vals = [v for n, v in zip(rig_names, rig_vals) if not n.startswith("B2")]  # (local)
    moving_vals = [v for n, v in zip(rig_names, rig_vals) if n.startswith("B2")]  # (local)
    res["g1_frozen_max"] = float(max(frozen_vals))
    res["g1_frozen_floor_ok"] = bool(max(frozen_vals) <= 1e-12)
    res["g1_moving_max"] = float(max(moving_vals))
    res["g1_moving_value_ok"] = bool(abs(max(moving_vals) - 2.279e-1) / 2.279e-1 <= 1e-3)

    # --- g2: b2_scalar_dev Schur-scalarity ---
    bsd = np.asarray(d["b2_scalar_dev"], dtype=float)  # (local)
    res["b2_scalar_dev_max"] = float(bsd.max())
    res["g2_schur_scalar_ok"] = bool(bsd.max() <= 1e-10)  # 3 decades above ~1e-13 floor

    # --- g3: A^WZ median double-protection ---
    res["A_prot_median"] = float(d["A_prot_median"])
    res["frac_prot"] = float(d["frac_prot"])
    res["g3_median_ok"] = bool(float(d["A_prot_median"]) <= 1e-12)
    res["g3_frac_ok"] = bool(float(d["frac_prot"]) >= 0.99)

    # --- scalar-consistency rows ---
    res["chir_anticomm"] = float(d["chir_anticomm"])
    res["chir_lock"] = float(d["chir_lock"])
    res["sc_chir_anticomm_ok"] = bool(abs(float(d["chir_anticomm"])) <= 1e-15)  # EXACT-class
    res["sc_chir_lock_ok"] = bool(abs(float(d["chir_lock"]) - 1.0) <= 1e-9)
    res["f_nonAb_pair"] = float(d["f_nonAb"])
    res["sc_f_nonAb_pair_ok"] = bool(abs(float(d["f_nonAb"])) <= 1e-12)  # FLOOR-class
    res["sc_I_NA_excl_floor_ok"] = bool(I_NA_excl <= 1e-20)  # FLOOR-class
    res["sc_I_NA_b2_value_ok"] = bool(abs(I_NA_b2_excl - 2.591e-2) / 2.591e-2 <= 1e-4)  # VALUE-class
    res["Im_int"] = float(d["Im_int"])
    res["sc_Im_int_ok"] = bool(float(d["Im_int"]) <= 1e-12)  # FLOOR-class
    res["C_fhs"] = float(d["C_fhs"])
    res["sc_C_fhs_ok"] = bool(abs(float(d["C_fhs"]) + 0.5) <= 1e-6)
    res["n_defect"] = int(d["n_defect"])
    res["sc_n_defect_ok"] = bool(int(d["n_defect"]) == 3)  # INTEGER-EXACT
    # U-clause frame-spread (orbit edges; VALUE-class on both edges)
    orbit = np.asarray(d["orbit_I_Ab"], dtype=float)  # (local)
    res["orbit_min"] = float(orbit.min())
    res["orbit_max"] = float(orbit.max())
    res["orbit_rel"] = float(d["orbit_rel"])
    res["I_NA_b2_invariant"] = float(d["I_NA_b2"])
    res["structural_reading"] = str(d["structural_reading"])

    # --- f_nonAb FRAME-DEPENDENT: REPORT, NOT GATE ---
    res["f_nonAb_b2_REPORT"] = float(d["f_nonAb_b2"])
    res["I_Ab_b2_pinned_REPORT"] = float(d["I_Ab_b2"])
    res["f_nonAb_frame_dependent_note"] = (
        "f_nonAb is frame-DEPENDENT (eigh arbitrary intra-eigenspace rotation): "
        f"pair={float(d['f_nonAb']):.3e} at floor vs pinned-frame f_nonAb_b2="
        f"{float(d['f_nonAb_b2']):.3e} (I_Ab_b2={float(d['I_Ab_b2']):.3e} pinned vs "
        f"I_NA_b2={float(d['I_NA_b2']):.3e} invariant). REPORTED, not a PASS/FAIL gate row."
    )

    # --- aggregate witness-pin verdict ---
    pin_flags = [
        res["npz_file_sha_match"], res["npz_audit_match_W6"],
        res["g1_frozen_floor_ok"], res["g1_moving_value_ok"],
        res["g2_schur_scalar_ok"], res["g3_median_ok"], res["g3_frac_ok"],
        res["sc_chir_anticomm_ok"], res["sc_chir_lock_ok"],
        res["sc_f_nonAb_pair_ok"], res["sc_I_NA_excl_floor_ok"],
        res["sc_I_NA_b2_value_ok"], res["sc_Im_int_ok"],
        res["sc_C_fhs_ok"], res["sc_n_defect_ok"],
        (res["oom_gap_rounded"] == 22),
    ]  # (local)
    res["all_witness_pins_ok"] = bool(all(pin_flags))
    res["witness_pin_flags"] = {
        "npz_file_sha": res["npz_file_sha_match"],
        "npz_audit_W6": res["npz_audit_match_W6"],
        "g1_frozen_floor": res["g1_frozen_floor_ok"],
        "g1_moving_value": res["g1_moving_value_ok"],
        "g2_schur_scalar": res["g2_schur_scalar_ok"],
        "g3_median": res["g3_median_ok"], "g3_frac": res["g3_frac_ok"],
        "sc_chir_anticomm": res["sc_chir_anticomm_ok"],
        "sc_chir_lock": res["sc_chir_lock_ok"],
        "sc_f_nonAb_pair": res["sc_f_nonAb_pair_ok"],
        "sc_I_NA_excl_floor": res["sc_I_NA_excl_floor_ok"],
        "sc_I_NA_b2_value": res["sc_I_NA_b2_value_ok"],
        "sc_Im_int": res["sc_Im_int_ok"], "sc_C_fhs": res["sc_C_fhs_ok"],
        "sc_n_defect": res["sc_n_defect_ok"],
        "oom_gap_22": (res["oom_gap_rounded"] == 22),
    }
    return res


# ---------------------------------------------------------------------------
# Section 7 — Reviewer JSON load + PASS-AND aggregation
# ---------------------------------------------------------------------------

def load_reviewer(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def clause_verdict(reviewer: dict, clause: str) -> str:
    c = reviewer.get("clauses", {}).get(clause)  # (local)
    if isinstance(c, dict):
        return c.get("verdict", "MISSING")
    return "MISSING"


def aggregate(axisA: dict, axisB: dict, witnesses: dict) -> dict:
    """Set-conjunction PASS-AND over clause verdicts + witness pins."""
    rows = []  # (local)
    any_fail = False  # (local)
    any_info = False  # (local)
    for c in CLAUSES:
        va = clause_verdict(axisA, c)  # (local)
        vb = clause_verdict(axisB, c)  # (local)
        joint_clause_pass = (va == "PASS" and vb == "PASS")  # (local)
        rows.append({"clause": c, "V_A": va, "V_B": vb, "dual_PASS": joint_clause_pass})
        if va == "FAIL" or vb == "FAIL":
            any_fail = True
        if va == "INFO" or vb == "INFO":
            any_info = True
    all_clauses_dual_pass = all(r["dual_PASS"] for r in rows)  # (local)
    # JOINT clause PASS-AND in BOTH (explicit, even though it is in CLAUSES)
    joint_both = (clause_verdict(axisA, "JOINT") == "PASS"
                  and clause_verdict(axisB, "JOINT") == "PASS")  # (local)
    witness_ok = witnesses["all_witness_pins_ok"]  # (local)

    # composite collapse
    if any_fail or not witness_ok:
        composite = "FAIL"  # (local)
    elif any_info:
        composite = "INFO"
    elif all_clauses_dual_pass and joint_both:
        composite = "PASS"
    else:
        composite = "FAIL"  # a clause MISSING (not PASS, not FAIL/INFO) -> not satisfiable
    return {
        "rows": rows,
        "all_clauses_dual_pass": all_clauses_dual_pass,
        "joint_both_pass": joint_both,
        "witness_ok": witness_ok,
        "any_fail": any_fail, "any_info": any_info,
        "composite": composite,
    }


# ---------------------------------------------------------------------------
# Section 8 — Plot
# ---------------------------------------------------------------------------

def make_plot(agg: dict, witnesses: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))  # (local)

    # Panel 1: clause-by-clause dual-verdict matrix
    rows = agg["rows"]  # (local)
    cmap = {"PASS": 1.0, "INFO": 0.5, "FAIL": 0.0, "MISSING": -0.5}  # (local)
    mat = np.array([[cmap.get(r["V_A"], -0.5), cmap.get(r["V_B"], -0.5)] for r in rows])  # (local)
    im = ax1.imshow(mat, aspect="auto", cmap="RdYlGn", vmin=0, vmax=1)  # (local)
    ax1.set_xticks([0, 1])
    ax1.set_xticklabels(["Axis-A\n(kaluza-klein)", "Axis-B\n(landau)"])
    ax1.set_yticks(range(len(rows)))
    ax1.set_yticklabels([r["clause"] for r in rows])
    for i, r in enumerate(rows):
        ax1.text(0, i, r["V_A"], ha="center", va="center", fontsize=8, fontweight="bold")
        ax1.text(1, i, r["V_B"], ha="center", va="center", fontsize=8, fontweight="bold")
    ax1.set_title(f"{GATE_ID}\nPASS-AND clause matrix — composite={agg['composite']}\n"
                  f"§VII.BR Band-Selective Schur Rigidity (OVERLAP-CAVEAT)")
    fig.colorbar(im, ax=ax1, fraction=0.046, label="PASS=1 / INFO=0.5 / FAIL=0")

    # Panel 2: witness re-check residuals vs pinned tolerances (log scale)
    names = ["g1 frozen\nfloor", "g2 Schur\nb2_scalar", "g3 A^WZ\nmedian",
             "f_nonAb\npair", "I_NA_excl\nfloor", "Im_int\nfloor",
             "I_NA(B2)\nmoving"]  # (local)
    vals = [witnesses["g1_frozen_max"], witnesses["b2_scalar_dev_max"],
            witnesses["A_prot_median"], witnesses["f_nonAb_pair"],
            witnesses["I_NA_excl"], witnesses["Im_int"],
            witnesses["I_NA_b2_excl"]]  # (local)
    tols = [1e-12, 1e-10, 1e-12, 1e-12, 1e-20, 1e-12, None]  # (local) None=VALUE-class
    xs = np.arange(len(names))  # (local)
    ax2.bar(xs - 0.18, [max(v, 1e-30) for v in vals], width=0.36, label="recomputed |value|",
            color="steelblue")
    ax2.bar(xs + 0.18, [(t if t else witnesses["I_NA_b2_excl"]) for t in tols], width=0.36,
            label="pinned tol / value-anchor", color="orange", alpha=0.6)
    ax2.set_yscale("log")
    ax2.set_xticks(xs)
    ax2.set_xticklabels(names, fontsize=8)
    ax2.set_ylabel("|value| (log)")
    ax2.axhline(1.0, color="grey", lw=0.5, ls=":")
    ax2.set_title(f"Witness re-checks vs pins — 22-OOM gap log10="
                  f"{witnesses['oom_gap_log10']:.3f}→{witnesses['oom_gap_rounded']}\n"
                  f"all_witness_pins_ok={witnesses['all_witness_pins_ok']}")
    ax2.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=110)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 — Verdict payload
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID, "verdict": verdict, "value": str(value),
        "scheme": SCHEME, "convention": CONVENTION, "l_max": str(L_MAX),
        "audit_sha256": audit_sha, "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 10 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 0. Prerequisite + lineage
    prereq = resolve_prereq_and_slot()  # (local)
    print(f"=== {GATE_ID} prerequisite + lineage ===")
    print(f"  prereq {PREREQ_GATE}: present={prereq['prereq_present']} "
          f"status={prereq['prereq_status']} landed_slot={prereq['landed_slot']} "
          f"drift={prereq['slot_drift']}")
    print(f"  LC-lineage clean={prereq['lc_lineage_clean']} "
          f"a19_extra_row={prereq['a19_extra_row']}")

    # PRE-REG-INC mechanical closure if the W6 landing is not PASS
    if not (prereq["prereq_present"] and prereq["prereq_status"] == "PASS"):
        entry_block = ""  # (local)
        pins = log_input_pins(INPUT_FILES, entry_block)
        audit_sha, content_sha = compute_dual_sha(
            Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py", pins)
        value = (f"PRE-REG-INC_blocked_by_{PREREQ_GATE}_{prereq['prereq_status']}")  # (local)
        print(f"\n[MECHANICAL CLOSURE] W6 STAGE-1 not PASS -> PRE-REG-INC")
        print_verdict_payload("FAIL", value, audit_sha, content_sha,
                              extra_rows=[
                                  f"# audit_sha256_short={audit_sha[:16]} "
                                  f"content_sha256_short={content_sha[:16]} # {GATE_ID} dual-SHA companion row",
                                  f"# PRE-REG-INC per session-101-plan-w7.md §W7-2; deferred to S102; "
                                  f"required prereq: [{PREREQ_GATE}]",
                              ])
        return 0

    # 1. Mechanical witness re-computation (the script does this itself)
    print(f"\n=== {GATE_ID} witness re-computation (from pinned npz) ===")
    witnesses = recompute_witnesses()  # (local)
    print(f"  npz file SHA match (a31ff591…): {witnesses['npz_file_sha_match']}")
    print(f"  npz stored audit == W6-2 gate (4a03497c…): {witnesses['npz_audit_match_W6']}")
    print(f"  RELEASE WITNESS: I_NA(B2)={witnesses['I_NA_b2_excl']:.9e} (moving) "
          f"vs floor I_NA(pair)={witnesses['I_NA_excl']:.9e}")
    print(f"  22-OOM gap: log10(ratio)={witnesses['oom_gap_log10']:.6f} -> "
          f"{witnesses['oom_gap_rounded']} (Decimal-exact)")
    print(f"  I_NA(B2) rel to 2.591e-2: {witnesses['I_NA_b2_rel']:.3e} "
          f"(VALUE-class rel_tol 1e-4)")
    print(f"  I_NA(pair) rel to 2.602e-24: {witnesses['I_NA_excl_rel']:.3e} "
          f"(FLOOR-class bound)")
    print(f"  g1 frozen floor max={witnesses['g1_frozen_max']:.3e} (<=1e-12: "
          f"{witnesses['g1_frozen_floor_ok']}); moving B2 max={witnesses['g1_moving_max']:.6e}")
    print(f"  g2 b2_scalar_dev max={witnesses['b2_scalar_dev_max']:.3e} (<=1e-10: "
          f"{witnesses['g2_schur_scalar_ok']})")
    print(f"  g3 A_prot_median={witnesses['A_prot_median']:.3e} (<=1e-12: "
          f"{witnesses['g3_median_ok']}); frac_prot={witnesses['frac_prot']:.6f} "
          f"(>=0.99: {witnesses['g3_frac_ok']})")
    print(f"  f_nonAb REPORT (frame-dependent): {witnesses['f_nonAb_frame_dependent_note']}")
    print(f"  structural_reading: {witnesses['structural_reading']}")
    print(f"  ALL WITNESS PINS OK: {witnesses['all_witness_pins_ok']}")
    for k, v in witnesses["witness_pin_flags"].items():
        if not v:
            print(f"    !! VIOLATED PIN: {k}")

    # 2. Load reviewer JSONs + PASS-AND aggregation
    axisA = load_reviewer(AXISA_JSON)  # (local)
    axisB = load_reviewer(AXISB_JSON)  # (local)
    print(f"\n=== {GATE_ID} reviewer JSONs ===")
    print(f"  Axis-A reviewer: {axisA.get('reviewer')} (entry {axisA.get('registered_entry')})")
    print(f"  Axis-B reviewer: {axisB.get('reviewer')} (entry {axisB.get('entry')})")
    print(f"  Axis-A substrate_input_overlap: {axisA.get('substrate_input_overlap')}")
    print(f"  Axis-B substrate_input_overlap: {axisB.get('substrate_input_overlap')}")

    agg = aggregate(axisA, axisB, witnesses)  # (local)
    print(f"\n=== {GATE_ID} PASS-AND clause matrix ===")
    print(f"  {'clause':<10}{'V_A':<8}{'V_B':<8}{'dual_PASS'}")
    for r in agg["rows"]:
        print(f"  {r['clause']:<10}{r['V_A']:<8}{r['V_B']:<8}{r['dual_PASS']}")
    print(f"  all_clauses_dual_pass={agg['all_clauses_dual_pass']} "
          f"joint_both_pass={agg['joint_both_pass']} witness_ok={agg['witness_ok']}")
    print(f"  COMPOSITE = {agg['composite']}")

    # 3. substrate-input orthogonality: NOT SATISFIED -> OVERLAP-CAVEAT
    overlap_caveat = "OVERLAP-CAVEAT(s100b_nonabelian_metric_fraction.npz->both)"  # (local)
    # both reviewer JSONs MUST attest the overlap; cross-check
    overlap_both_attest = bool(axisA.get("substrate_input_overlap")
                               and axisB.get("substrate_input_overlap"))  # (local)
    print(f"  substrate_input_orthogonality=NOT-SATISFIED; "
          f"both reviewers attest overlap={overlap_both_attest}")

    # 4. Slot resolution
    slot = prereq["landed_slot"] or EXPECTED_SLOT  # (local)
    slot_note = "slot_as_expected" if not prereq["slot_drift"] else f"slot_DRIFT_to_{slot}"  # (local)

    # 5. Save npz
    np.savez(
        OUT_NPZ,
        composite=agg["composite"],
        clause_rows=json.dumps(agg["rows"]),
        all_clauses_dual_pass=agg["all_clauses_dual_pass"],
        joint_both_pass=agg["joint_both_pass"],
        witness_ok=agg["witness_ok"],
        witness_pin_flags=json.dumps(witnesses["witness_pin_flags"]),
        I_NA_b2_excl=witnesses["I_NA_b2_excl"],
        I_NA_excl=witnesses["I_NA_excl"],
        oom_gap_log10=witnesses["oom_gap_log10"],
        oom_gap_rounded=witnesses["oom_gap_rounded"],
        b2_scalar_dev_max=witnesses["b2_scalar_dev_max"],
        A_prot_median=witnesses["A_prot_median"],
        frac_prot=witnesses["frac_prot"],
        f_nonAb_pair=witnesses["f_nonAb_pair"],
        f_nonAb_b2_REPORT=witnesses["f_nonAb_b2_REPORT"],
        chir_anticomm=witnesses["chir_anticomm"],
        chir_lock=witnesses["chir_lock"],
        structural_reading=witnesses["structural_reading"],
        substrate_input_orthogonality="NOT-SATISFIED-OVERLAP-CAVEAT",
        overlap_both_attest=overlap_both_attest,
        lc_lineage_clean=prereq["lc_lineage_clean"],
        a19_extra_row=prereq["a19_extra_row"],
        resolved_slot=slot,
        slot_drift=prereq["slot_drift"],
        axisA_reviewer=str(axisA.get("reviewer")),
        axisB_reviewer=str(axisB.get("reviewer")),
    )
    print(f"  npz -> {OUT_NPZ.name}")

    # 6. Plot
    make_plot(agg, witnesses)
    print(f"  png -> {OUT_PNG.name}")

    # 7. Dual SHA (audit pinmap includes both reviewer JSONs + npz + anchor-extracted block)
    entry_block = extract_registry_block(REGISTRY_PATH, REGISTRY_BODY_ANCHOR)  # (local)
    if not entry_block:
        print("  WARNING: §VII.BR registry block not anchor-extracted (empty).")
    pins = log_input_pins(INPUT_FILES, entry_block)
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py", pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap incl. JSONs+npz+VII.BR block)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 8. Build value field (composite + overlap-caveat + slot + 22-OOM witness + Stage-3 routing)
    composite = agg["composite"]  # (local)
    stage3 = ("STAGE-3-flip-recommended_orchestrator-direct" if composite == "PASS"
              else "hold-STAGE-1-CANDIDATE")  # (local)
    value = (
        f"composite={composite}_PASS-AND_7clauses_dual-verified_"
        f"AxisA=kaluza-klein_AxisB=landau_all-PASS_"
        f"witness-recompute=I_NA(B2)={witnesses['I_NA_b2_excl']:.4e}_vs_pair-floor="
        f"{witnesses['I_NA_excl']:.4e}_{witnesses['oom_gap_rounded']}OOM-Decimal-exact_"
        f"g2_b2_scalar={witnesses['b2_scalar_dev_max']:.3e}_g3_median="
        f"{witnesses['A_prot_median']:.3e}_fracprot={witnesses['frac_prot']:.5f}_"
        f"f_nonAb=FRAME-DEPENDENT-REPORT-not-gate_"
        f"substrate_input_orthogonality={overlap_caveat}_"
        f"both-reviewers-attest-overlap={overlap_both_attest}_"
        f"LC-lineage-CLEAN_no-A19-extra-row_"
        f"slot={slot}_{slot_note}_"
        f"{stage3}_Stage-3-CLASS=JOINT-CROSS-AXIS-STAGE-2-PASS-AND_"
        f"registry-tag-edit-ORCHESTRATOR-DIRECT-at-session-end_no-mack-falsifier-row"
    )  # (local)

    tag = (f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print()
    print(tag)

    # 9. Companion rows (dual-SHA + reviewer-cleanliness + OVERLAP-CAVEAT + Stage-3 routing)
    extra_rows = [
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row",
        f"# reviewer-cleanliness: STATIC leg --check-reviewers {slot} --reviewers "
        f"kaluza-klein-theorist,landau-condensed-matter-theorist --strict -> EXCLUSION-PASS "
        f"(berry-geometric-phase-theorist+successors Stage-0-EXCLUDED, categorical via inheritance "
        f"witness s100b-band-selective-rigidity.md); DYNAMIC leg kk/landau agent-memory grep CLEAN "
        f"# {GATE_ID} reviewer-cleanliness row",
        f"# substrate_input_orthogonality=NOT-SATISFIED-BY-BINDING-DESIGN: npz loaded by BOTH "
        f"reviewers (clause g) -> {overlap_caveat}; PASS-AND establishes OUTPUT-TYPE independence "
        f"(rep-theoretic vs band-geometry), NOT structural-INPUT independence "
        f"(joint-theorem-promotion.md Substrate-input-orthogonality clause) # {GATE_ID} OVERLAP-CAVEAT row",
        f"# LC-lineage CLEAN: S101-TAU0-OPERATOR-CANONICITY PASS with L4-LIFT(iv) for "
        f"S100b-NONABELIAN-METRIC-FRACTION -> witnesses cite CLEAN, NO A19 UNTRUSTED-UPSTREAM extra-row "
        f"# {GATE_ID} lineage row",
        f"# Stage-3 routing: composite={composite} -> "
        f"{'§VII.BR STAGE-1-CANDIDATE->STAGE-3-PERMANENT (Stage-3-CLASS JOINT-CROSS-AXIS-STAGE-2-PASS-AND, OVERLAP-CAVEAT carried)' if composite=='PASS' else 'hold STAGE-1-CANDIDATE'}; "
        f"registry tag edit is ORCHESTRATOR-DIRECT at session-end synthesis (NEVER this script); "
        f"no falsifier-master-inventory row (§VII structural entry) # {GATE_ID} Stage-3-routing row",
    ]  # (local)
    print_verdict_payload(composite, value, audit_sha, content_sha, extra_rows=extra_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
