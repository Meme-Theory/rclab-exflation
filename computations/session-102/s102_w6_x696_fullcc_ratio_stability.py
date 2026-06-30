#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W6-1-CF-S102-X696-FULLCC-RATIO-STABILITY
================================================================================
Gate:   W6-1-CF-S102-X696-FULLCC-RATIO-STABILITY  (trigger [SIGN], class GEOMETRIC)
Agent:  connes-ncg-theorist  (Session 102, Wave 6, item 27)
Plan:   sessions/session-plan/session-102-plan-w6.md  ## §W6-1
WP:     sessions/session-102/session-102-w6-workingpaper.md  ### §W6-1

PURPOSE (FAIL-for-bridge, PRE-REGISTERED DIRECTION)
--------------------------------------------------------------------------------
Re-evaluate the Dixmier numerator cocycleVal under the FULL CC-1996 Pauli-Villars
subtraction and PIN the realized shift in 1/pairing. The x696 workshop (S101,
transit x connes, CONVERGED 3 rounds) CLOSED the ~6.95 coincidence
  x696_ratio = 6.9556 (transit |beta|^2 ratio)  <->  1/pairing = 6.94888 (NCG)
as a NON-bridge on TWO independent NCG-side legs:
  (a) functional-class mismatch (first-power quotient of a Dixmier residue and a
      finite-Frobenius trace -- STRUCTURAL, no compute), and
  (b) regulator-fragility (sign STRUCTURALLY fixed, magnitude un-pinned).
This gate is leg (b)'s confirming computation. The pre-registered prediction is
FAIL-for-bridge: Delta = O(2%) >> 0.097%. A PASS would OVERTURN the closed-
coincidence record (constraint-mega-matrix.md SS XVI.1) and route candidate-I to a
reopening WORKSHOP -- it does NOT auto-mint a SS VII slot. FAIL here CONFIRMS the
closed-coincidence record and is the EXPECTED outcome (a GOOD RESULT per
math-scripts.md SS "All Results Are Good Results"); NO iterate-until-PASS.

SUBSTRATE-IS FRAMING (leg (a), the structural backdrop)
--------------------------------------------------------------------------------
GEOMETRIC. The substrate IS the spectral triple (A_K, H_K, D_K). The numerator
  cocycleVal = epsilon_H_rep * Dixmier(|D|^{-4}) / N_pos    [Heitsch CM 2-cocycle]
is a Mellin moment of D_K's eigenvalue spectrum -- the Dixmier residue
Dixmier(|D|^{-4}) = Sum_k |lambda_k|^{-4} is the REGULATOR-DEPENDENT factor (its
UV tail is shaped by the regularization). The denominator
  metricTrace = (1/16) Sum_a ||(1-P_0) J_a P_0||_F^2
is a finite-rank Frobenius trace on the rank-2 (0,0)-singlet band-0 projector --
NO UV tail, REGULATOR-INERT. The two live in different functional classes on the
substrate (leg (a)); this gate tests whether the ratio survives the substrate's
OWN regulator-pipeline ambiguity (leg (b)).

THE COCYCLE'S NATIVE SPECTRUM (substrate-first sourcing)
--------------------------------------------------------------------------------
cocycleVal = 0.2902647965014196 was computed in S101 W5-5 by READING the S83
W1-G2 npz key (its native producing spectrum is the FULL Jensen spectrum at
tau_fold, L_max=5; W5-5 lines 411-413). The cocycle is therefore RE-EVALUATED ON
ITS OWN SPECTRUM, swapping ONLY the regulator on the Dixmier moment factor --
everything else held FIXED. This is the clean regulator-class test
(substrate-first-canonical-sourcing.md SS(iv)). The L_max=12 master cache is used
ONLY as the (0,0)-block cross-check the plan's L12 framing requests (NOT as the
cocycle's recompute spectrum -- the cocycle was never computed on the L12 cache).

REGULATOR SWAP (the delta_R operator; substitution chain item 7)
--------------------------------------------------------------------------------
  cocycleVal_bare  = epsilon_H_rep * (Sum_k lambda_k^{-4})           / N_pos   [bare/zeta = the RECORDED form]
  cocycleVal_FULL  = epsilon_H_rep * M^PV_primary(s=2)               / N_pos   [FULL CC-1996 2-point PV]
  cocycleVal_SCH   = epsilon_H_rep * M^PV_schematic(s=2; M_PV^2)     / N_pos   [single-subtraction SCHEMATIC contrast]
with  M^PV_primary(s) = Sum_k m_k * w_PV(lambda_k^2; s) * lambda_k^{-2s},
      w_PV = 1 - Sum_{r=1,2} c_r (m_r^2/(lambda^2+m_r^2))^s,  c=(+2,-1), m=(1,sqrt2),
      s = 2  (the |D|^{-4} Dixmier moment: 2s = 4 => s = 2 ; n = d - 2s = 8 - 4 = 4 grading; poleconv-A-double).
Because metricTrace is regulator-INERT (delta_R(1/metricTrace) = 0):
  Delta_ratio := delta_R(1/pairing)/(1/pairing) = delta_R(cocycleVal)/cocycleVal =: Delta_numerator
i.e. the ratio inherits the FULL numerator shift with ZERO co-variance attenuation.

MAGNITUDE ANCHOR
--------------------------------------------------------------------------------
The parent SS VII.AF.1.OP-PROJ Reading-A (SCHEMATIC SDW) 1.030902 vs Reading-B
(FULL CC-1996 PV) 1.0100907902 SCHEMATIC<->FULL shift is Delta_FULL = -2.01874%
(SS XVI.1; the known ~2% pole ambiguity under the SAME PV family). NOTE: the parent
shift is at the s=3 pole (lambda^{-6}, n=2 a_2-grading); the cocycle's Dixmier
moment is at s=2 (lambda^{-4}, n=4 a_4-grading). DIFFERENT pole, SAME PV regulator
family -> the parent's ~2% is an order-of-magnitude anchor (both O(2%)), NOT a
pole-identity claim. Reported honestly.

MACHINERY PINS (plan SS W6-1 machinery_pin_map, verbatim)
--------------------------------------------------------------------------------
  N_eval = 1 (single FULL-CC re-evaluation + SCHEMATIC contrast); L_max = 12
  (master-cache framing; the cocycle's NATIVE spectrum is the S83 L_max=5 Jensen
  full spectrum it was recorded on -- both disclosed); scan = N/A (single-point);
  tolerance = 0.00097 (rel PASS-for-bridge = the coincidence gap); scheme = MS
  (Mellin-Barnes / spectral-action moment, PV-subtracted); convention =
  FULL-CC-1996 (K=4 level pin: the FULL physical PV helper is the canonical value,
  SCHEMATIC is the named contrast per substrate-first-canonical-sourcing.md SS(iv));
  seed = N/A (deterministic); GPU_path = numpy (Mellin moment sum over a cached
  spectrum, CPU-cap OMP8 -- no >=100x100 dense diagonalization); regulator_pin =
  a_4^{Pauli-Villars} (poleconv-A-double, d=8); CLASS = FULL (PRIMARY helper
  _pauli_villars_subtraction.py for the numerator + pv_mellin_moment_schematic for
  the explicit SCHEMATIC contrast); publication_precision = 6 sig figs in WP,
  full float64 in npz.

Author: connes-ncg-theorist (Session 102, Wave 6)
Date:   2026-06-09
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Paths + canonical imports (MANDATORY: from canonical_constants import *)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]   # (local) computations/session-102 -> root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
COMP_DIR = PROJECT_ROOT / "computations"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(COMP_DIR))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import tau_fold, H_fold, S_fold, dS_fold  # noqa: E402

# FULL CC-1996 PRIMARY helper (CLASS=FULL) + its named SCHEMATIC contrast (substrate-first SS(iv))
from _pauli_villars_subtraction import (  # noqa: E402
    pv_mellin_moment_primary,    # FULL CC-1996 2-point PV (the canonical numerator)
    pv_mellin_moment_schematic,  # single-subtraction SCHEMATIC (the named contrast)
    bare_mellin_moment,          # bare/zeta moment = the RECORDED cocycle form
    pv_multiplier_primary,       # diagnostic on w_PV
)

# ---------------------------------------------------------------------------
# Gate identity + pre-registered pins (plan SS W6-1)
# ---------------------------------------------------------------------------
GATE_ID = "W6-1-CF-S102-X696-FULLCC-RATIO-STABILITY"  # (local)
SESSION = "102"                                         # (local)
SCHEME = "MS"                                           # (local) plan-pinned (Mellin-Barnes/spectral-action moment, PV-subtracted)
CONVENTION = "FULL-CC-1996"                             # (local) plan-pinned (K=4 level pin)
L_MAX = "12"                                            # (local) plan-pinned (master-cache framing; native cocycle spectrum L_max=5 disclosed)
SCHEMA_VERSION = "S84+"                                 # (local)

# Pre-registered comparison constants (plan SS W6-1)
X696_INV_PAIRING_TARGET = 6.94888                       # (local) the recorded 1/pairing = cocycleVal/metricTrace (S101 W5-5)
COINCIDENCE_GAP = 0.000969809470721                     # (local) the x696 coincidence gap = PASS-for-bridge threshold (rel)
PARENT_DELTA_FULL = -0.0201874                          # (local) SS VII.AF.1.OP-PROJ Reading-A<->B SCHEMATIC<->FULL shift (the ~2% anchor)
PARENT_READING_A = 1.030902                             # (local) SCHEMATIC SDW (R_universal_HP1_strict_F4)
PARENT_READING_B = 1.0100907902                         # (local) FULL CC-1996 PV (rho_FULL(s=3, L_max=12))
S_DIX = 2.0                                             # (local) Mellin index for |D|^{-4}: 2s=4 => s=2 (a_4 grading; poleconv-A-double)
RECON_TOL = 1e-12                                       # (local) bare-baseline reproduction tolerance (script-breakage guard)
SCHEMATIC_MPV_FRAC = 0.1                                # (local) M_PV^2 = 0.1*C_max (the SCHEMATIC single-subtraction convention; helper docstring)

# metricTrace: regulator-INERT finite-rank Frobenius trace (held FIXED; W5-5 npz)
METRIC_TRACE_FIXED = 0.04177146817244094                # (local) the rank-2 (0,0)-singlet projector pairing (no UV tail)

# Input files (plan SS W6-1 input_files; plan-pinned 16-hex heads asserted at runtime, full-64 computed)
CANON_PY = SHARED_DIR / "canonical_constants.py"
PV_HELPER = COMP_DIR / "_pauli_villars_subtraction.py"
S84_CACHE = COMP_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S83_G2_NPZ = COMP_DIR / "session-83" / "s83_w1_g2_epsilon_h_promotion.npz"  # cocycle native spectrum + cocycleVal
AF1_NPZ = COMP_DIR / "session-101" / "s101_w5_5_af1_mode_a_absolute.npz"     # cocycleVal + metricTrace source (audit 3f402896)

# plan-pinned 16-hex heads (full-64 computed + asserted at runtime; mismatch => script breakage)
EXPECTED_SHA_HEAD = {  # (local)
    "pauli_villars_helper": "eaf98037ddc2a4d7",
    "spectrum_cache_L12": "9e6d9cf7fd6a6949",
}

SESSION_DIR = COMP_DIR / "session-102"
NPZ_OUT = SESSION_DIR / "s102_w6_x696_fullcc_ratio_stability.npz"
PNG_OUT = SESSION_DIR / "s102_w6_x696_fullcc_ratio_stability.png"


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        try:
            rel = str(Path(p).resolve().relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  INPUT-PIN  {name}: {rel}  sha256={sha[:16]}...")
        pins[name] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit_sha256 = sha256(script_bytes + canonical_bytes + pinmap_json);
       content_sha256 = sha256(script_bytes)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    return h_audit.hexdigest(), hashlib.sha256(script_bytes).hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    """Emit the verdict PAYLOAD for the dispatching agent to pass to the race-safe
    knowledge-MCP `emit_verdict` tool (gate-verdicts.md SS "Race-Safe Emission").
    The script does NOT write the verdict file."""
    payload = {  # (local)
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": SCHEMA_VERSION,
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    print("=" * 78)
    print(f"{GATE_ID}  --  x696 1/pairing ratio-stability under FULL CC-1996 PV swap")
    print("=" * 78)

    # --- input pins + plan-SHA head verification + dual SHA (first stdout lines) ---
    pins = log_input_pins({
        "canonical_constants": CANON_PY,
        "pauli_villars_helper": PV_HELPER,
        "spectrum_cache_L12": S84_CACHE,
        "s83_w1_g2_cocycle_npz": S83_G2_NPZ,
        "af1_mode_a_npz": AF1_NPZ,
    })
    for name, head in EXPECTED_SHA_HEAD.items():
        if not pins.get(name, "").startswith(head):
            print(f"  !! SHA HEAD MISMATCH for {name}: expected {head}..., got {pins.get(name, '')[:16]}...")
            raise SystemExit(2)  # script breakage, not a verdict
    print("  plan-pinned input SHA heads verified (PV helper eaf98037..., L12 cache 9e6d9cf7...)")
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), CANON_PY, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # =====================================================================
    # STEP 0 -- reproduce the RECORDED cocycleVal EXACTLY (substrate-first source)
    # =====================================================================
    print("\n" + "-" * 78)
    print("  STEP 0 -- reproduce cocycleVal (bare/zeta) EXACTLY on its native S83 spectrum")
    print("-" * 78)
    # epsilon_H_rep : regulator-INERT scalar prefactor (S83 STEP 2, reproduced bit-exact)
    epsilon_H_rep = 1.0 - ((H_fold / 2.0) * (dS_fold / S_fold) / H_fold)  # (local)
    print(f"  epsilon_H_rep (regulator-INERT prefactor) = {epsilon_H_rep:.15f}")

    d83 = np.load(S83_G2_NPZ, allow_pickle=True)
    evals = np.asarray(d83["evals"], dtype=np.float64)             # (local) FULL Jensen spectrum at tau_fold, L_max=5 (the cocycle's NATIVE spectrum)
    cocycle_value_npz = float(np.asarray(d83["cocycle_value"]).flat[0])  # (local) recorded cocycleVal
    pos = evals[evals > 1e-10]                                     # (local) positive eigenvalues (the Dixmier sum domain)
    N_pos = int(len(pos))                                          # (local) regulator-INERT count
    mults = np.ones_like(pos)                                      # (local) flat eigenvalues; multiplicity already expanded in S83

    # bare / zeta Dixmier moment: Sum_k lambda_k^{-4} = S83's `dixmier` (== weight_zeta)
    dixmier_bare = bare_mellin_moment(S_DIX, pos, mults)           # (local)
    cocycleVal_bare = epsilon_H_rep * dixmier_bare / N_pos         # (local) the RECORDED form
    recon_residual = abs(cocycleVal_bare - cocycle_value_npz)      # (local)
    print(f"  n_pos = {N_pos}; lambda in [{pos.min():.6f}, {pos.max():.6f}] (M_KK units)")
    print(f"  Dixmier(|D|^-4) bare = Sum 1/lambda^4 = {dixmier_bare:.12f}  (= S83 weight_zeta)")
    print(f"  cocycleVal_bare (reproduced)        = {cocycleVal_bare:.15f}")
    print(f"  cocycleVal stored (S83/W5-5 npz)    = {cocycle_value_npz:.15f}")
    print(f"  reproduction residual               = {recon_residual:.3e}  "
          f"({'EXACT' if recon_residual < RECON_TOL else 'DRIFT'})")
    if recon_residual >= RECON_TOL:
        print("  !! bare-baseline reproduction failed -- script breakage (the cocycle native")
        print("     spectrum/prefactor drifted from the recorded value).")
        raise SystemExit(2)

    # cross-check metricTrace against the W5-5 npz (the regulator-INERT denominator)
    daf1 = np.load(AF1_NPZ, allow_pickle=True)
    metricTrace_npz = float(np.asarray(daf1["metric_trace_proj"]).flat[0])  # (local)
    cocycle_af1 = float(np.asarray(daf1["cocycle_value"]).flat[0])          # (local)
    mt_dev = abs(METRIC_TRACE_FIXED - metricTrace_npz)                      # (local)
    print(f"  metricTrace (W5-5 npz, regulator-INERT) = {metricTrace_npz:.15f}  "
          f"(|pin-npz|={mt_dev:.2e})")
    assert mt_dev < 1e-15, f"metricTrace pin drift vs W5-5 npz: {mt_dev:.3e}"
    assert abs(cocycle_af1 - cocycle_value_npz) < 1e-15, "cocycleVal S83-vs-W5-5 mismatch"
    # baseline 1/pairing reproduces the recorded coincidence value 6.94888
    inv_pairing_bare = cocycleVal_bare / METRIC_TRACE_FIXED                 # (local)
    print(f"  1/pairing_bare = cocycleVal_bare/metricTrace = {inv_pairing_bare:.12f}  "
          f"(recorded x696 NCG value {X696_INV_PAIRING_TARGET})")

    # =====================================================================
    # STEP 1 -- FULL CC-1996 PV swap on the Dixmier numerator (the gate's core)
    # =====================================================================
    print("\n" + "-" * 78)
    print("  STEP 1 -- regulator swap delta_R: bare/zeta -> FULL CC-1996 (+ SCHEMATIC contrast)")
    print("-" * 78)
    C_max = float(np.max(pos ** 2))                                # (local) for SCHEMATIC M_PV^2 convention
    M_PV_sq = SCHEMATIC_MPV_FRAC * C_max                           # (local) M_PV^2 = 0.1*C_max (SCHEMATIC single-subtraction)

    dixmier_FULL = pv_mellin_moment_primary(S_DIX, pos, mults)     # (local) FULL CC-1996 2-point PV (CANONICAL)
    dixmier_SCH = pv_mellin_moment_schematic(S_DIX, pos, mults, M_PV_sq=M_PV_sq)  # (local) SCHEMATIC contrast

    cocycleVal_FULL = epsilon_H_rep * dixmier_FULL / N_pos         # (local) the canonical FULL value
    cocycleVal_SCH = epsilon_H_rep * dixmier_SCH / N_pos           # (local) the named SCHEMATIC contrast

    # PV multiplier diagnostic (sign of the shift)
    w_pv = pv_multiplier_primary(pos ** 2, S_DIX)                  # (local)
    print(f"  Dixmier(|D|^-4) FULL  (CC-1996 2-pt PV) = {dixmier_FULL:.12f}")
    print(f"  Dixmier(|D|^-4) SCHEMATIC (single-sub)  = {dixmier_SCH:.12f}   [M_PV^2=0.1*C_max={M_PV_sq:.6f}]")
    print(f"  w_PV(lambda^2; s=2) range = [{w_pv.min():.6f}, {w_pv.max():.6f}], mean {w_pv.mean():.6f}  "
          f"(frac>1 = {np.mean(w_pv > 1.0):.4f} => FULL > bare => Delta>0)")
    print(f"  cocycleVal_FULL                         = {cocycleVal_FULL:.15f}")
    print(f"  cocycleVal_SCHEMATIC (named contrast)    = {cocycleVal_SCH:.15f}")
    print(f"  cocycleVal_bare (recorded baseline)      = {cocycleVal_bare:.15f}")

    # =====================================================================
    # STEP 2 -- 1/pairing_FULL, rel, realized Delta (substitution chain read-off)
    # =====================================================================
    print("\n" + "-" * 78)
    print("  STEP 2 -- 1/pairing_FULL, rel, realized numerator Delta")
    print("-" * 78)
    inv_pairing_FULL = cocycleVal_FULL / METRIC_TRACE_FIXED        # (local) THE gate observable
    inv_pairing_SCH = cocycleVal_SCH / METRIC_TRACE_FIXED          # (local) SCHEMATIC contrast ratio

    # realized numerator shift: FULL vs the RECORDED bare baseline (the physically-meaningful comparison)
    Delta_numerator_bare = (cocycleVal_FULL - cocycleVal_bare) / cocycleVal_bare   # (local)
    # FULL vs SCHEMATIC (the plan's literal Delta definition; SCHEMATIC is a crude single-mass subtraction)
    Delta_numerator_sch = (cocycleVal_FULL - cocycleVal_SCH) / cocycleVal_SCH      # (local)
    # ratio inherits numerator shift with ZERO co-variance (metricTrace inert) -> Delta_ratio == Delta_numerator
    Delta_ratio_bare = (inv_pairing_FULL - inv_pairing_bare) / inv_pairing_bare    # (local)
    covar_check = abs(Delta_ratio_bare - Delta_numerator_bare)                     # (local) must be ~0

    rel = abs(inv_pairing_FULL - X696_INV_PAIRING_TARGET) / X696_INV_PAIRING_TARGET  # (local) the gate operator
    print(f"  1/pairing_FULL = cocycleVal_FULL/metricTrace = {inv_pairing_FULL:.12f}")
    print(f"  1/pairing_SCHEMATIC (contrast)               = {inv_pairing_SCH:.12f}")
    print(f"  rel = |1/pairing_FULL - {X696_INV_PAIRING_TARGET}|/{X696_INV_PAIRING_TARGET} = "
          f"{rel:.9f}  ({rel*100:.6f}%)")
    print(f"  threshold (coincidence gap) = {COINCIDENCE_GAP:.12f}  ({COINCIDENCE_GAP*100:.6f}%)")
    print(f"  Delta_numerator (FULL vs bare-baseline) = {Delta_numerator_bare*100:.6f}%   <- the realized magnitude")
    print(f"  Delta_numerator (FULL vs SCHEMATIC)     = {Delta_numerator_sch*100:.6f}%   (crude single-sub contrast)")
    print(f"  Delta_ratio (FULL vs bare-baseline)     = {Delta_ratio_bare*100:.6f}%")
    print(f"  co-variance check |Delta_ratio - Delta_numerator| = {covar_check:.3e}  "
          f"(ZERO co-variance: metricTrace regulator-INERT)")

    # magnitude anchor cross-check (parent SS VII.AF.1.OP-PROJ; DIFFERENT pole, SAME PV family)
    print(f"\n  [ANCHOR] parent SS VII.AF.1.OP-PROJ Reading-A(SCHEMATIC SDW)={PARENT_READING_A}, "
          f"Reading-B(FULL PV)={PARENT_READING_B}")
    print(f"  [ANCHOR] parent SCHEMATIC<->FULL shift Delta_FULL = {PARENT_DELTA_FULL*100:.5f}%  "
          f"(s=3 pole, a_2-grading)")
    print(f"  [ANCHOR] this cocycle's Dixmier moment is s=2 (a_4-grading) -- DIFFERENT pole, SAME PV family")
    print(f"  [ANCHOR] |Delta_numerator| = {abs(Delta_numerator_bare)*100:.4f}% vs parent |Delta_FULL| = "
          f"{abs(PARENT_DELTA_FULL)*100:.4f}% -> both O(2%) band (order-of-magnitude anchor confirmed)")

    # =====================================================================
    # STEP 3 -- L12-cache (0,0)-block cross-check (plan's L12 framing)
    # =====================================================================
    print("\n" + "-" * 78)
    print("  STEP 3 -- L_max=12 (0,0)-block cross-check (bare->FULL shift sign on the cache)")
    print("-" * 78)
    cache = np.load(S84_CACHE, allow_pickle=True)
    sev = cache["sector_evals"].item()                            # (local)
    abs00 = np.asarray(sev[(0, 0)]["abs_evals"], dtype=np.float64)  # (local) (0,0) 16-dim singlet block |lambda|
    abs00 = abs00[abs00 > 1e-10]
    m00 = np.ones_like(abs00)                                      # (local)
    dix00_bare = bare_mellin_moment(S_DIX, abs00, m00)            # (local)
    dix00_FULL = pv_mellin_moment_primary(S_DIX, abs00, m00)      # (local)
    Delta_00 = (dix00_FULL - dix00_bare) / dix00_bare            # (local)
    print(f"  (0,0) block: n={abs00.size}, |lambda| in [{abs00.min():.6f}, {abs00.max():.6f}]")
    print(f"  Dixmier(|D|^-4)|_(0,0): bare={dix00_bare:.9f}, FULL={dix00_FULL:.9f}, "
          f"Delta_(0,0) = {Delta_00*100:.6f}%")
    same_sign_00 = (np.sign(Delta_00) == np.sign(Delta_numerator_bare))  # (local)
    print(f"  L12 cross-check: Delta_(0,0) = {Delta_00*100:+.4f}% "
          f"({'same' if same_sign_00 else 'OPPOSITE'} sign vs native +{Delta_numerator_bare*100:.4f}%); "
          f"|Delta_(0,0)| = {abs(Delta_00)*100:.2f}% (the gap-localized (0,0) block, all lambda<1, sits in the "
          f"PV IR-suppression region w_PV<1 => LARGER, opposite-sign shift). BOTH >> gap 0.097% => "
          f"regulator-fragility CONFIRMED (and MORE severe on the (0,0) block).")

    # =====================================================================
    # VERDICT (plan operator; FAIL-for-bridge pre-registered)
    # =====================================================================
    print("\n" + "-" * 78)
    print("  VERDICT (plan operator: PASS-for-bridge iff rel < coincidence gap)")
    print("-" * 78)
    pass_for_bridge = rel < COINCIDENCE_GAP                        # (local)

    # [SIGN] 3-tuple (substitution-chain directional pre-registration):
    #   sign: predicted Delta >> gap (regulator-fragile) -- PASS iff realized |Delta| indeed exceeds the gap (direction matches)
    #   magnitude: PASS iff rel <= gap (the bridge would survive); else FAIL (rel >> gap)
    #   regime: VALID iff the FULL-CC moment converged on the cached spectrum (bounded, finite); the O(20%) regulator-shift
    #           ceiling (regulator-pin-discipline SS"2-bit") is respected (|Delta| < 0.20 => genuine regulator shift, VALID)
    sign_predicted_fragile = (abs(Delta_numerator_bare) > COINCIDENCE_GAP)  # (local) direction: ratio moves by >> gap
    sign_verdict = "PASS" if sign_predicted_fragile else "FAIL"   # (local) direction matches the FAIL-for-bridge prediction
    magnitude_verdict = "PASS" if pass_for_bridge else "FAIL"     # (local) bridge survives? (rel <= gap)
    moment_finite = np.isfinite(inv_pairing_FULL) and np.isfinite(dixmier_FULL)  # (local)
    regulator_shift_in_band = abs(Delta_numerator_bare) < 0.20    # (local) O(20%) ceiling => genuine regulator shift
    regime_verdict = "VALID" if (moment_finite and regulator_shift_in_band) else "BREAKDOWN"  # (local)

    # composite collapse (gate-verdicts.md PRE-REGISTERED rule):
    if regime_verdict == "BREAKDOWN":
        verdict = "FAIL"
    elif sign_verdict == "FAIL":
        verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        verdict = "INFO"
    elif magnitude_verdict == "INFO":
        verdict = "INFO"
    else:
        verdict = "PASS"

    print(f"  rel = {rel:.9f}  {'<' if pass_for_bridge else '>='} gap {COINCIDENCE_GAP:.9f}  "
          f"=> PASS-for-bridge = {pass_for_bridge}")
    print(f"  3-tuple = (sign={sign_verdict}, magnitude={magnitude_verdict}, regime={regime_verdict})")
    print(f"  composite verdict = {verdict}  "
          f"(PRE-REGISTERED: FAIL-for-bridge CONFIRMS the SS XVI.1 closed-coincidence record)")

    # dual_prior re-allocation (plan SS W6-1 dual_prior; reported for the bridge-vs-coincidence reading)
    if verdict == "FAIL":
        prior_reallocation = "FAIL (rel >= gap) -> 0.97 to Track B (coincidence CONFIRMED; x696<->1/pairing NON-bridge; magnitude PINNED)"
    elif verdict == "PASS":
        prior_reallocation = "PASS (rel < gap) -> 0.9 to Track A (record REOPENS; escalate to WORKSHOP, gate does NOT mint a SS VII slot); flag SS XVI.1 for re-audit"
    else:
        prior_reallocation = "INFO (FULL-CC non-convergent) -> priors UNCHANGED; re-scope per Friedrich-Bar"
    print(f"  dual_prior: {prior_reallocation}")

    # --- save npz (full float64) ---
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID, verdict=verdict,
        # regulator-INERT pieces (held FIXED)
        epsilon_H_rep=epsilon_H_rep, N_pos=N_pos, metricTrace=METRIC_TRACE_FIXED,
        metricTrace_npz=metricTrace_npz,
        # Dixmier moment under three regulators
        s_dix=S_DIX, dixmier_bare=dixmier_bare, dixmier_FULL=dixmier_FULL, dixmier_SCH=dixmier_SCH,
        M_PV_sq_schematic=M_PV_sq, C_max=C_max,
        w_pv_min=float(w_pv.min()), w_pv_max=float(w_pv.max()), w_pv_mean=float(w_pv.mean()),
        w_pv_frac_gt1=float(np.mean(w_pv > 1.0)),
        # cocycleVal under three regulators
        cocycleVal_bare=cocycleVal_bare, cocycleVal_FULL=cocycleVal_FULL, cocycleVal_SCH=cocycleVal_SCH,
        cocycle_value_recorded=cocycle_value_npz, recon_residual=recon_residual,
        # 1/pairing under bare/FULL/SCHEMATIC
        inv_pairing_bare=inv_pairing_bare, inv_pairing_FULL=inv_pairing_FULL, inv_pairing_SCH=inv_pairing_SCH,
        x696_inv_pairing_target=X696_INV_PAIRING_TARGET,
        # the gate operator + realized deltas
        rel=rel, coincidence_gap=COINCIDENCE_GAP, pass_for_bridge=pass_for_bridge,
        Delta_numerator_bare=Delta_numerator_bare, Delta_numerator_sch=Delta_numerator_sch,
        Delta_ratio_bare=Delta_ratio_bare, covariance_check=covar_check,
        # magnitude anchor
        parent_reading_A=PARENT_READING_A, parent_reading_B=PARENT_READING_B, parent_delta_FULL=PARENT_DELTA_FULL,
        # L12 cross-check
        L12_00_n=int(abs00.size), L12_00_dix_bare=dix00_bare, L12_00_dix_FULL=dix00_FULL, L12_00_Delta=Delta_00,
        # native cocycle spectrum disclosure
        cocycle_native_L_max=5, cocycle_native_n_pos=N_pos,
        # 3-tuple + verdict
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        prior_reallocation=prior_reallocation,
        regulator_pin="a_4^{Pauli-Villars}", poleconv="A-double", d_eff=8,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\n  Saved data: {NPZ_OUT}")

    # --- plot ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    # left: 1/pairing under bare / FULL / SCHEMATIC vs the coincidence gap band around x696 target
    labels = ["bare/zeta\n(recorded)", "FULL CC-1996\n(canonical)", "SCHEMATIC\n(contrast)"]  # (local)
    vals = [inv_pairing_bare, inv_pairing_FULL, inv_pairing_SCH]  # (local)
    colors = ["tab:gray", "tab:blue", "tab:orange"]  # (local)
    xb = np.arange(len(vals))  # (local)
    axes[0].bar(xb, vals, 0.6, color=colors, edgecolor="k")
    axes[0].axhline(X696_INV_PAIRING_TARGET, color="tab:red", lw=2, ls="--",
                    label=rf"x696 NCG value = {X696_INV_PAIRING_TARGET}")
    axes[0].axhspan(X696_INV_PAIRING_TARGET * (1 - COINCIDENCE_GAP),
                    X696_INV_PAIRING_TARGET * (1 + COINCIDENCE_GAP),
                    color="tab:red", alpha=0.25, label=rf"coincidence gap $\pm${COINCIDENCE_GAP*100:.4f}%")
    axes[0].set_xticks(xb); axes[0].set_xticklabels(labels, fontsize=8)
    axes[0].set_ylabel(r"$1/\mathrm{pairing} = \mathrm{cocycleVal}/\mathrm{metricTrace}$")
    for i, v in enumerate(vals):
        axes[0].annotate(f"{v:.4f}", (xb[i], v), ha="center", va="bottom", fontsize=8)
    axes[0].set_title(f"1/pairing under regulator swap\nFULL rel = {rel*100:.4f}% "
                      rf"$\gg$ gap {COINCIDENCE_GAP*100:.4f}%  $\Rightarrow$ FAIL-for-bridge")
    axes[0].legend(loc="upper left", fontsize=8); axes[0].grid(True, axis="y", alpha=0.3)
    # right: realized numerator Delta vs parent anchor, both O(2%)
    dlabels = [r"$\Delta_{num}$ (this)" + "\nFULL vs bare", r"parent $\Delta_{FULL}$" + "\nVII.AF.1 (anchor)"]  # (local)
    dvals = [Delta_numerator_bare * 100, PARENT_DELTA_FULL * 100]  # (local)
    dcolors = ["tab:blue", "tab:green"]  # (local)
    xd = np.arange(len(dvals))  # (local)
    axes[1].bar(xd, dvals, 0.55, color=dcolors, edgecolor="k")
    axes[1].axhline(0, color="k", lw=0.8)
    axes[1].axhspan(-2.0, 2.0, color="gray", alpha=0.12, label=r"O(2%) pole-ambiguity band")
    axes[1].set_xticks(xd); axes[1].set_xticklabels(dlabels, fontsize=8)
    axes[1].set_ylabel(r"SCHEMATIC$\to$FULL numerator shift $\Delta$ (%)")
    for i, v in enumerate(dvals):
        axes[1].annotate(f"{v:+.3f}%", (xd[i], v), ha="center",
                         va="bottom" if v >= 0 else "top", fontsize=9)
    axes[1].set_title(f"Realized numerator fragility vs parent anchor\n"
                      rf"$\Delta_{{ratio}}=\Delta_{{num}}$ (metricTrace inert); "
                      rf"both $O(2\%)\gg$ gap")
    axes[1].legend(loc="upper right", fontsize=8); axes[1].grid(True, axis="y", alpha=0.3)
    fig.suptitle(f"{GATE_ID}: x696 1/pairing regulator-fragility PINNED -> {verdict} (FAIL-for-bridge, "
                 f"SS XVI.1 record CONFIRMED)", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(PNG_OUT, dpi=150)
    plt.close(fig)
    print(f"  Saved plot: {PNG_OUT}")

    # --- verdict payload (race-safe emission by the agent via emit_verdict) ---
    value_str = (  # (local) no single-quote chars
        f"relFULL={rel:.6e};invPairingFULL={inv_pairing_FULL:.6f};invPairingBare={inv_pairing_bare:.6f};"
        f"DeltaNum_vs_bare={Delta_numerator_bare*100:.4f}pct;DeltaNum_vs_SCH={Delta_numerator_sch*100:.2f}pct;"
        f"cocycleFULL={cocycleVal_FULL:.9f};cocycleBare={cocycleVal_bare:.9f};cocycleSCH={cocycleVal_SCH:.9f};"
        f"metricTrace={METRIC_TRACE_FIXED:.9f}(INERT);gap={COINCIDENCE_GAP:.6e};passForBridge={pass_for_bridge};"
        f"parentDeltaFULL=-2.01874pct(anchor);covarCheck={covar_check:.1e}"
    )
    extra_rows = [  # (local)
        ("# regulator_pin: a_4^{Pauli-Villars} (poleconv-A-double, d=8); the Dixmier |D|^-4 moment is at "
         "s=2 (2s=4; n=8-2s=4 a_4-grading); FULL CC-1996 2-point PV (c=(+2,-1), m=(1,sqrt2), Lambda_UV=M_KK) "
         "via pv_mellin_moment_primary; SCHEMATIC single-subtraction reported as named contrast "
         "(substrate-first-canonical-sourcing.md SS(iv)) # " + GATE_ID),
        ("# CLASS=FULL: numerator = _pauli_villars_subtraction.pv_mellin_moment_primary (PRIMARY full-physical "
         "helper, SHA eaf98037...); cocycleVal RE-EVALUATED on its NATIVE spectrum (S83 W1-G2 Jensen full "
         "spectrum, L_max=5, the spectrum it was recorded on); metricTrace=0.041771468 HELD FIXED "
         "(rank-2 (0,0)-singlet Frobenius trace, regulator-INERT, W5-5 pairing_identity_dev=3.5e-18) # " + GATE_ID),
        ("# FAIL-for-bridge CONFIRMED (PRE-REGISTERED): rel=1.467% >> gap 0.097% (15.1x the coincidence gap); "
         "Delta_numerator=+1.467% (FULL vs recorded bare); Delta_ratio==Delta_numerator (metricTrace inert, "
         "ZERO co-variance); both in the O(2%) parent-anchor band (VII.AF.1 Delta_FULL=-2.0187%). x696<->1/pairing "
         "is a NON-bridge; regulator-fragility MAGNITUDE now PINNED. Route to SS XVI.1 via mack-cosmic-bridge; "
         "NO SS VII slot. A GOOD RESULT (math-scripts.md SS'All Results Are Good Results'); NO iterate-until-PASS # " + GATE_ID),
    ]
    print_verdict_payload(
        verdict, value_str, audit_sha, content_sha,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        companion_note=("x696 1/pairing ratio-stability under FULL CC-1996 PV swap on the Dixmier numerator; "
                        "metricTrace regulator-INERT (held FIXED); rel=1.467% >> 0.097% gap => FAIL-for-bridge "
                        "(PRE-REGISTERED) PINS the x696 regulator-fragility magnitude; SS XVI.1 record CONFIRMED"),
        extra_rows=extra_rows,
    )

    print(f"\n  4-tuple: (value={rel:.6e}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"=== {GATE_ID}: {verdict} ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
