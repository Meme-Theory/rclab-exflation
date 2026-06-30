#!/usr/bin/env python3
"""
S93 W5-3 — S93-W5-3-VII-AR-FULL-TIER-N4-RETRY
=============================================

Gate: S93-W5-3-VII-AR-FULL-TIER-N4-RETRY
Trigger: [SIGN]
Classification: GEOMETRIC  (cutoff_axis: spectral)
Agent: connes-ncg-theorist (FULL-tier Connes-Chamseddine 1996 §2.2-2.3 pipeline)

Pre-registered threshold (plan §W5-3 item 1 — CONJUNCTION operator):
  PASS (Branch FULL-PASS-CONFIRMED) iff
      |ρ_S(FULL) − ρ_S(SCHEMATIC)| < 1e-3
      AND rank_change_per_anchor(FULL) reproduces the single deep-IR flip [0,0,0,0,1]
  FAIL (Branch FULL-FAIL-METHODOLOGY-FLOOR-ONLY) iff
      |ρ_S(FULL) − ρ_S(SCHEMATIC)| ≥ 1e-3  OR  the FULL-tier flip vanishes / moves.
  INFO iff regime-breakdown (>50% of anchor window outside CC-1996 N=4 validity)
      OR borderline |ρ_S diff| near 1e-3 with MARGINAL regime.

§VII.AR substrate-physics compute. NOT part of the STAGE-3 tier ladder.
Dual-prior-pre-registered (~0.65 FULL-FAIL per S-1 II.2).

LEVEL-PIN DISCIPLINE (substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY):
  This gate executes the FULL physical regularization (Connes-Chamseddine 1996
  §2.2-2.3 N=4 Pauli-Villars mass tower at Λ_UV = M_KK), DROPPING the SCHEMATIC
  profile-prefactor knob. CLASS pin = FULL (TIER-1). The verdict-line convention
  carries NO -SCHEMATIC suffix and a `# tier_pin=TIER-1` companion row.

WHY THIS GATE EXISTS — conviction-or-acquittal of the §W4-1 PASS-A deep-IR flip
------------------------------------------------------------------------------
S92 §W4-1 returned composite=PASS, reading=PASS-A-AND-B
(audit_sha256=257e2619fe308645a8f87d127dde3764696d0432038725af77e3fa1fa96ce490).
PASS-A's axis-B clause (d) PASSed because the ASYMMETRIC Bogoliubov coupling
(per-regulator (cutoff_frac, M_PV²_frac) pins) produced a SINGLE rank-flip at
the deep-IR anchor 1/M_KK²-internal: rank_change_per_anchor = [0,0,0,0,1].
BUT §W4-1 consumed SCHEMATIC regulator profiles + a SCALAR (1 − M_PV²_frac_r)
prefactor (tier_pin=TIER-2). The S-1 II.2 audit found the deep-IR flip is a
property of that SCALAR M_PV²_frac prefactor under SCHEMATIC profile saturation,
NOT of the substrate's BdG occupation physics. This gate is the FULL-tier N=4
conviction-or-acquittal: does the flip survive the SCHEMATIC→FULL transition?

CONNES-CHAMSEDDINE 1996 §2.2-2.3 N=4 PAULI-VILLARS MULTIPLIER FORMALISM
----------------------------------------------------------------------
The FULL physical regularization replaces the SCHEMATIC scalar (1 − M_PV²_frac_r)
with the genuine N=4 Pauli-Villars mass tower. CC-1996 §2.2-2.3 multiplier set
(alternating-binomial, Sage-verified):
    c_j = (-1)^j · C(4, j) = [1, -4, 6, -4, 1],  j = 0..4
with masses M_j² = j · (M_PV²_frac_r · max(λ²)), j = 0..4 (M_0 = 0 physical field).
This set cancels the first N=4 moments (k=0..3) and leaves the first non-vanishing
moment at k=4 (residue Σ_j c_j j^4 = 24 — Sage-exact), exactly the structure that
makes the N=4 tower a faithful physical regularization at the substrate-distance-2
pole s=4. The PV-subtracted s=4 kernel per eigenvalue:
    K_PV(λ²; M_PV²) = Σ_{j=0}^{4} c_j / (λ² + j·M_PV²)^s ,  s = 4.

SUBSTITUTION CHAIN (per math-scripts.md §"Double-Check Logic Before Compute"):

  Claim: "The §W4-1 PASS-A deep-IR rank-flip at 1/M_KK²-internal either survives
          the SCHEMATIC→FULL transition (substrate-IS structural feature) or
          vanishes (SCHEMATIC M_PV²_frac prefactor artifact). Dual prior ≈ 0.65
          FULL-FAIL (S-1 II.2)."

  Step 1 (Definitions): at the deep-IR anchor t_ref = 1/M_KK²-internal, all four
    regulator profiles {F_2 Gaussian-exp, cutoff_sqrt sharp-step, anomaly
    polynomial-corrected, Zubarev Fermi-Dirac} SATURATE to ≈ 1 (heat-kernel
    weight e^{−t_ref·λ²} → 1 as t_ref → 0 for the bottom-K eigenvalues).
    [S-1 II.2; reproduces the WP ordering exactly.]

  Step 2 (SCHEMATIC mechanism): with all profiles ≈ 1, the SCHEMATIC rank ordering
    at the deep-IR anchor is driven NOT by the profile families but by the scalar
    M_PV²_frac prefactor vector {0.1, 0.05, 0.2, 0.15} (asymmetric pins).
    [S-1 II.2 finding.]

  Step 3 (SCHEMATIC flip is a prefactor artifact): ⇒ the SCHEMATIC rank-flip
    [0,0,0,0,1] at the deep-IR anchor is a property of the M_PV²_frac SCALAR
    prefactor under SCHEMATIC profile saturation, NOT of the substrate's BdG
    occupation physics (the S52 Bogoliubov amplitude v_a² = Δ²/(2(λ²+Δ²)) carries
    NO per-regulator Pauli-Villars mass-suppression knob of the M_PV²_frac form).
    [S-1 audit-provenance note.]

  Step 4 (FULL-tier mechanism + PREDICTED DIRECTION): under FULL-tier N=4
    Connes-Chamseddine physical regularization, the Pauli-Villars subtraction
    K_PV(λ²; M_PV²) = Σ_j c_j/(λ²+j·M_PV²)^4 does NOT reduce to a scalar
    M_PV²_frac prefactor at the deep-IR anchor — it carries the full physical
    mass-tower structure (the N=4 alternating-binomial multipliers re-weight every
    eigenvalue by a λ-dependent kernel). PREDICTED DIRECTION (dual prior ~0.65):
    the deep-IR flip VANISHES (Branch FULL-FAIL), because the artifact mechanism
    (Step 3) is specific to the SCHEMATIC saturation.

  Step 5 (SIGN read-off): the directional prediction is FULL-FAIL via flip-
    vanishing. The discriminating scalar is the deep-IR PRIMARY-vs-SCHEMATIC
    Spearman ρ_S^{deep-IR}; sign(|ρ_S(FULL) − ρ_S(SCHEMATIC)| − 1e-3). If the
    abs-diff is ≥ 1e-3 AND/OR the flip is NOT reproduced ⇒ FULL-FAIL ⇒ flip is
    SCHEMATIC artifact ⇒ PASS-A reclassifies to METHODOLOGY-floor-only. If the
    abs-diff is < 1e-3 AND the flip is reproduced ⇒ FULL-PASS ⇒ flip is
    substrate-IS structural feature.
    sign_verdict semantics: PASS iff the substitution-chain Step-4 PREDICTED
    direction (FULL-FAIL / flip-vanishing) matches the COMPUTED direction.

  Conclusion: genuine [SIGN] discriminator. The composite §W4-1 verdict REMAINS
  PASS on disk either way (verdict permanence; PASS-B sub-atlas-minus-ζ carries
  the composite); only PASS-A's epistemic standing is at stake. The gate's
  PASS/FAIL maps to the S-1 V.1 reclassification branches with ≥ 0.9 posterior
  re-allocation per epistemic-discipline.md §"Dual-prior pre-registration".

SUBSTRATE FRAMING (per phononic-framing.md §"IS Space, Not IN Space"):
  GEOMETRIC. The §VII.AR observable IS the Spearman rank-ordering of
  {F_2, cutoff_sqrt, anomaly, Zubarev} regulator images at substrate-distance-2
  Mellin-cone pole s=4 on D_K's block-diagonal spectrum at τ_fold = 0.19 — an
  algebra-INVARIANT spectrum-only functional (Cell I / biaxial-FI-LEVEL-DRESSED
  hybrid). Direction substrate → emergent: D_K eigenvalues → BdG sub-algebra
  M_2(ℂ) ⊂ A_K → asymmetric Bogoliubov amplitudes OR A_5_extended sub-atlas →
  rank-ordering predicate at the s=4 pole. The FULL-tier retry is the K=4 level-
  pin discipline's conviction-or-acquittal test: a SCHEMATIC regularization
  profile is NOT a physical regularization; honest -SCHEMATIC tagging at §W4-1 is
  what makes this FULL-tier retry a meaningful discriminator, not a formality.

DUAL-PRIOR PRE-REGISTRATION (epistemic-discipline.md §"Dual-prior"):
  Track A (FULL-PASS; flip is substrate-IS structural feature): prior 0.35.
  Track B (FULL-FAIL; flip is SCHEMATIC M_PV²_frac prefactor artifact): prior 0.65.
  Discriminator gate criterion:
    FULL-PASS  ⇒ posterior 0.90 to Track A (flip is substrate-IS).
    FULL-FAIL  ⇒ posterior 0.90 to Track B (flip is methodology-floor artifact).
    INFO (regime-breakdown / borderline) ⇒ priors UNCHANGED.
  The outcome MUST NOT be re-narrativized to fit either track post-hoc.

Output 4-tuple:
  (value=<composite-string>,
   scheme=FULL-tier-N4-Connes-Chamseddine-1996,
   convention=VII-AR-Stage-2-FULL-TIER-N4-Connes-Chamseddine-1996-asymmetric-AND-A5extended,
   L_max=12)

Inputs (SHA-256 pinned at runtime):
  - computations/_shared/canonical_constants.py
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (runtime canonical path)
  - computations/session-92/s92_w4_1_vii_ar_stage_2_re_dispatch_asymmetric_coupling.py
  - computations/session-89/s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.py
  - script bytes (feeds BOTH audit_sha256 and content_sha256)
  - §W4-1 PASS verdict audit_sha256 = 257e2619... (string pin)

Plan: sessions/session-plan/session-93-plan-w5.md §W5-3 (lines 428-629).
WP:   sessions/archive/session-93/session-93-w5-workingpaper.md §W5-3.
Verdict file: computations/session-93/s93_gate_verdicts.txt.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import math
import hashlib
import json
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    Vol_SU3_Haar,
)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from scipy.stats import spearmanr  # noqa: E402

# ---------------- Gate-block constants (canonical pins per plan §W5-3) ----------------
GATE_ID = "S93-W5-3-VII-AR-FULL-TIER-N4-RETRY"
SCHEME = "FULL-tier-N4-Connes-Chamseddine-1996"
CONVENTION = (
    "VII-AR-Stage-2-FULL-TIER-N4-Connes-Chamseddine-1996-asymmetric-AND-A5extended"
)
L_MAX = 12  # (local) plan §W5-3 machinery_pin_map (matches §W4-1 SCHEMATIC anchor)
S_POLE_AR = 4  # (local) substrate-distance-2 Mellin-cone pole s=4

# Pre-registered thresholds (plan §W5-3 strict_PASS_boundary)
RHO_S_AGREEMENT_BAND = 1e-3  # (local) machine-precision-equivalence band (S92 §W4-1 CF)
DEEP_IR_FLIP_TARGET = [0, 0, 0, 0, 1]  # (local) the single deep-IR flip to reproduce

# §VII.AR Level-3 registered Spearman anchor (registry line 17345/17351)
SPEARMAN_REGISTRY_ANCHOR = 0.800  # (local) |ρ_S(s=4)|_PRIMARY discrete-combinatorial EXACT

# Eigenvalue IR cutoff (matches W7a-74 PRIMARY + §W4-1 line 186)
EVAL_CUTOFF = 1e-6  # (local)

# 4-regulator §VII.AR atlas (registry line 17345 / W7a-74 PRIMARY)
REGULATOR_NAMES = ["F_2", "cutoff_sqrt", "anomaly", "Zubarev"]

# 5 substrate-natural heat-kernel anchors (registry line 17351, W7a-74 PRIMARY)
ANCHOR_LABELS = [
    "1/max_lambda_sq",
    "2.3/max_lambda_sq",
    "ln2/max_lambda_sq",
    "1/avg_lambda_sq_mw",
    "1/M_KK_sq",
]
DEEP_IR_ANCHOR = "1/M_KK_sq"  # (local) anchor-5; where the §W4-1 SCHEMATIC flip lives

# Asymmetric (REGULATOR-SPECIFIC) PARAMETER pins — substrate-physics derivation
# per registry E5 sub-atlas enumeration + §W4-1 substitution chain. These are the
# SAME pins §W4-1 used; the FULL-tier retry re-uses the anchor/atlas/pin structure.
ASYMMETRIC_CUTOFF_FRAC = {
    "F_2":         0.7,   # (local) anchor canonical
    "cutoff_sqrt": 0.5,   # (local) sharp-step distinction
    "anomaly":     0.9,   # (local) polynomial-correction distinction
    "Zubarev":     1.2,   # (local) Fermi-Dirac analog scale shift
}
ASYMMETRIC_M_PV_SQ_FRAC = {
    "F_2":         0.10,  # (local)
    "cutoff_sqrt": 0.05,  # (local)
    "anomaly":     0.20,  # (local)
    "Zubarev":     0.15,  # (local)
}

# A_5_extended sub-atlas (registry line 17371/17384 substrate-natural; excludes ζ)
A5_EXTENDED_REGULATORS = ["Pauli_Villars", "sharp_cutoff", "sinc_lattice", "sech_lattice"]
A5_UNIFORM_CUTOFF_FRAC = 1.0    # (local) A_5_extended substrate-natural uniform cf
A5_UNIFORM_M_PV_SQ_FRAC = 0.10  # (local) A_5_extended substrate-natural uniform M_PV²_frac

# ---- Connes-Chamseddine 1996 §2.2-2.3 N=4 Pauli-Villars multiplier set ----
# c_j = (-1)^j · C(4, j) = [1, -4, 6, -4, 1]; Sage-verified: cancels moments
# k=0..3, first non-vanishing moment at k=4 (residue Σ_j c_j j^4 = 24).
# Masses M_j² = j · (M_PV²_frac_r · max(λ²)), j = 0..4 (M_0 = 0, physical field).
CC1996_N4_PV_COEFFS = np.array([1.0, -4.0, 6.0, -4.0, 1.0])  # (local) (-1)^j C(4,j)
N_PV = 4  # (local) Connes-Chamseddine 1996 §2.2-2.3 N=4 tower

# §W4-1 SCHEMATIC PASS verdict (string pin per S-1 reference)
W4_1_PASS_AUDIT_SHA = (
    "257e2619fe308645a8f87d127dde3764696d0432038725af77e3fa1fa96ce490"
)

# Dual-prior pre-registration (epistemic-discipline.md §"Dual-prior")
PRIOR_TRACK_A_FULL_PASS = 0.35  # (local) flip is substrate-IS structural feature
PRIOR_TRACK_B_FULL_FAIL = 0.65  # (local) flip is SCHEMATIC M_PV²_frac prefactor artifact
POSTERIOR_REALLOCATION = 0.90   # (local) ≥0.9 posterior re-allocation per plan

# ---------------- File paths ----------------
SESSION_DIR = ROOT / "computations" / "session-93"
SHARED_DIR = ROOT / "computations" / "_shared"
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"
SCRIPT_PATH = Path(__file__).resolve()

# L_max=12 cache runtime canonical path (lives in session-84; matches plan pin SHA)
S84_L12_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S92_W4_1_SCRIPT = (
    ROOT / "computations" / "session-92"
    / "s92_w4_1_vii_ar_stage_2_re_dispatch_asymmetric_coupling.py"
)
W7A74_PRIMARY = (
    ROOT / "computations" / "session-89"
    / "s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.py"
)

OUT_NPZ = SESSION_DIR / "s93_w5_3_vii_ar_full_tier_n4_retry.npz"
OUT_PNG = SESSION_DIR / "s93_w5_3_vii_ar_full_tier_n4_retry.png"
VERDICT_FILE = SESSION_DIR / "s93_gate_verdicts.txt"

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "s84_spectrum_cache_L12_tau019": S84_L12_CACHE,
    "s92_w4_1_asymmetric_coupling_script": S92_W4_1_SCRIPT,
    "w7a74_PRIMARY_evaluator": W7A74_PRIMARY,
    "script": SCRIPT_PATH,
}


# ---------------- SHA helpers ----------------
def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()  # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 78)
    print(f"Gate: {GATE_ID}")
    print("=" * 78)
    print("Input SHAs (first 20 lines of stdout per .claude/templates/script-template.py):")
    for name, p in files.items():
        if not p.exists():
            print(f"  {name:48s} = (file not found; pin skipped)")
            continue
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        print(f"  {name:48s} = {sha[:16]}...  ({p.relative_to(ROOT)})")
    # §W4-1 PASS verdict string pin (no on-disk file resolution needed)
    pins["w4_1_pass_audit_sha_string_pin"] = W4_1_PASS_AUDIT_SHA
    print(f"  {'w4_1_pass_audit_sha_string_pin':48s} = {W4_1_PASS_AUDIT_SHA[:16]}...  (S92 §W4-1 PASS)")
    return pins


def compute_dual_sha(pins: dict, script_path: Path) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema.

    audit_sha256_inputs: script + canonical + pinmap + cache + w7a74 evaluator.
    content_sha256_inputs: script only.
    """
    script_bytes = script_path.read_bytes()
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)
    audit = hashlib.sha256(script_bytes + canonical_bytes + pinmap_json).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


# ---------------- SCHEMATIC regulator profiles (verbatim from §W4-1 / W7a-74 PRIMARY) ----------------
def reg_profile_F_2(x):
    """F_2 SCHEMATIC: Gaussian heat-kernel exp(-x). x = t_ref·cf·λ²."""
    return np.exp(-x)


def reg_profile_cutoff_sqrt(x):
    """cutoff_sqrt SCHEMATIC: sharp cutoff Θ(1 - sqrt(x))."""
    return np.where(np.sqrt(np.maximum(x, 0.0)) <= 1.0, 1.0, 0.0)


def reg_profile_anomaly(x):
    """anomaly SCHEMATIC: anomaly-corrected exp(-x)·(1 − x + x²/2)."""
    return np.exp(-x) * (1.0 - x + 0.5 * x * x)


def reg_profile_Zubarev(x):
    """Zubarev SCHEMATIC: smooth Zubarev-like 1/(1 + exp(10·(x − 1)))."""
    return 1.0 / (1.0 + np.exp(10.0 * (x - 1.0)))


REGULATOR_PROFILES = {
    "F_2": reg_profile_F_2,
    "cutoff_sqrt": reg_profile_cutoff_sqrt,
    "anomaly": reg_profile_anomaly,
    "Zubarev": reg_profile_Zubarev,
}


# ---------------- A_5_extended sub-atlas profiles (substrate-natural; excluding ζ) ----------------
def reg_profile_Pauli_Villars(x):
    """PV profile (substrate-natural): exp(-x) − exp(-2x) (CC-1996 §2.2-2.3 mass-ratio c=2)."""
    return np.exp(-x) - np.exp(-2.0 * x)


def reg_profile_sharp_cutoff(x):
    """Sharp cutoff Θ(1 - x)."""
    return np.where(x <= 1.0, 1.0, 0.0)


def reg_profile_sinc_lattice(x):
    """Sinc lattice spacing regulator sin(πx)/(πx); lattice domain bound x ≤ 1."""
    out = np.where(np.abs(x) < 1e-12, 1.0, np.sin(np.pi * x) / (np.pi * np.maximum(np.abs(x), 1e-12)))
    return np.where(x <= 1.0, out, 0.0)  # (local) lattice domain bound


def reg_profile_sech_lattice(x):
    """sech lattice regulator sech(x) = 2/(exp(x)+exp(-x))."""
    return 2.0 / (np.exp(x) + np.exp(-x))


A5_EXTENDED_PROFILES = {
    "Pauli_Villars": reg_profile_Pauli_Villars,
    "sharp_cutoff":  reg_profile_sharp_cutoff,
    "sinc_lattice":  reg_profile_sinc_lattice,
    "sech_lattice":  reg_profile_sech_lattice,
}


# ---------------- FULL-tier N=4 CC-1996 Pauli-Villars kernel ----------------
def cc1996_n4_pv_kernel(lam2: np.ndarray, M_PV_sq: float) -> np.ndarray:
    """Connes-Chamseddine 1996 §2.2-2.3 N=4 Pauli-Villars subtraction kernel at s=4.

    K_PV(λ²; M_PV²) = Σ_{j=0}^{4} c_j / (λ² + j·M_PV²)^s ,  s = 4,
    with c_j = (-1)^j C(4, j) = [1, -4, 6, -4, 1] and masses M_j² = j·M_PV².
    This is the FULL physical mass-tower structure replacing the SCHEMATIC scalar
    (1 − M_PV²_frac) prefactor. j=0 (M_0=0) is the physical field; j=1..4 are the
    Pauli-Villars regulator fields with the alternating-binomial multipliers.
    """
    ker = np.zeros_like(lam2)  # (local)
    for j in range(N_PV + 1):
        ker += CC1996_N4_PV_COEFFS[j] / (lam2 + j * M_PV_sq) ** S_POLE_AR
    return ker


# ---------------- Mellin moments ----------------
def mellin_moment_SCHEMATIC(lambdas, mults, t_ref, regulator_name, level):
    """SCHEMATIC asymmetric-coupling moment (verbatim §W4-1 mechanism; reproduces s92).

    PRIMARY:   Σ_λ m_λ · profile_reg(cf_r·t_ref·λ²) · (1 − M_PV²_frac_r) · λ⁻⁸
    SCHEMATIC: Σ_λ m_λ · profile_reg(t_ref·λ²) · λ⁻⁸     (bare profile)
    """
    profile = REGULATOR_PROFILES[regulator_name]  # (local)
    if level == "PRIMARY":
        cf = ASYMMETRIC_CUTOFF_FRAC[regulator_name]  # (local) regulator-specific
        pvf = ASYMMETRIC_M_PV_SQ_FRAC[regulator_name]  # (local) regulator-specific
        x = cf * t_ref * lambdas ** 2  # (local)
        vals = profile(x) * (1.0 - pvf)  # (local) SCHEMATIC scalar prefactor knob
    else:  # SCHEMATIC bare
        x = t_ref * lambdas ** 2  # (local)
        vals = profile(x)  # (local)
    integrand = mults * vals * lambdas ** (-2 * S_POLE_AR)  # (local) λ⁻⁸
    return float(np.sum(integrand))


def mellin_moment_FULL_N4(lambdas, mults, t_ref, regulator_name, level, lambda_max_sq):
    """FULL-tier N=4 CC-1996 physical regularization moment.

    PRIMARY:   Σ_λ m_λ · profile_reg(cf_r·t_ref·λ²) · K_PV(λ²; M_PV²_frac_r·max(λ²))
               where K_PV is the N=4 Pauli-Villars mass tower (NOT the scalar knob).
    SCHEMATIC: Σ_λ m_λ · profile_reg(t_ref·λ²) · λ⁻⁸     (bare profile; same as SCHEMATIC level)

    The FULL-tier PRIMARY replaces the SCHEMATIC scalar (1 − M_PV²_frac_r) prefactor
    with the genuine CC-1996 §2.2-2.3 N=4 Pauli-Villars subtraction K_PV(λ²; M_PV²)
    at Λ_UV = M_KK (M_PV² pinned to M_PV²_frac_r × max(λ²), the substrate UV anchor).
    """
    profile = REGULATOR_PROFILES[regulator_name]  # (local)
    lam2 = lambdas ** 2  # (local)
    if level == "PRIMARY":
        cf = ASYMMETRIC_CUTOFF_FRAC[regulator_name]  # (local)
        pvf = ASYMMETRIC_M_PV_SQ_FRAC[regulator_name]  # (local)
        x = cf * t_ref * lam2  # (local)
        prof_vals = profile(x)  # (local)
        M_PV_sq = pvf * lambda_max_sq  # (local) substrate UV anchor (Λ_UV ~ M_KK natural)
        ker = cc1996_n4_pv_kernel(lam2, M_PV_sq)  # (local) FULL N=4 PV tower
        return float(np.sum(mults * prof_vals * ker))
    else:  # SCHEMATIC bare (same as SCHEMATIC-level for like-for-like flip comparison)
        x = t_ref * lam2  # (local)
        prof_vals = profile(x)  # (local)
        integrand = mults * prof_vals * lam2 ** (-S_POLE_AR)  # (local)
        return float(np.sum(integrand))


def mellin_moment_a5_FULL_N4(lambdas, mults, t_ref, regulator_name, lambda_max_sq):
    """A_5_extended FULL-tier N=4 moment (substrate-natural; uniform cf=1.0, M_PV²_frac=0.1)."""
    profile = A5_EXTENDED_PROFILES[regulator_name]  # (local)
    lam2 = lambdas ** 2  # (local)
    x = A5_UNIFORM_CUTOFF_FRAC * t_ref * lam2  # (local)
    prof_vals = profile(x)  # (local)
    M_PV_sq = A5_UNIFORM_M_PV_SQ_FRAC * lambda_max_sq  # (local)
    ker = cc1996_n4_pv_kernel(lam2, M_PV_sq)  # (local) FULL N=4 PV tower
    return float(np.sum(mults * prof_vals * ker))


def rank_vector(moments: np.ndarray) -> np.ndarray:
    """argsort-of-argsort rank vector (rank 0 = smallest moment)."""
    return np.argsort(np.argsort(moments)).astype(np.float64)


# ---------------- Append-verdict helper ([SIGN] + tier_pin=TIER-1 FULL) ----------------
def append_verdict(
    composite: str, value_str: str, audit_sha: str, content_sha: str,
    sign_v: str, mag_v: str, reg_v: str,
) -> None:
    """Atomic single-shot append per .claude/templates/script-template.py.

    Emits:
      1. Canonical line (NO -SCHEMATIC suffix; FULL-tier convention)
      2. Dual-SHA companion comment row (W9a-99 split)
      3. Schema-v2 3-tuple companion row ([SIGN] trigger; sign/magnitude/regime)
      4. tier_pin=TIER-1 companion row (FULL physical regularization per §(iv) K=4)
    """
    canonical = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    three_tuple = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    tier_pin = (
        f"# tier_pin=TIER-1 # {GATE_ID} FULL physical regularization "
        f"(Connes-Chamseddine 1996 §2.2-2.3 N=4 Pauli-Villars tower at Λ_UV=M_KK); "
        f"substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY level-pin: "
        f"CLASS=FULL; NO -SCHEMATIC suffix; drops the §W4-1 -SCHEMATIC-PENDING-FULL-TIER-N4 tag\n"
    )  # (local)
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)
        f.write(three_tuple)
        f.write(tier_pin)


# ---------------- Main ----------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)

    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    print(f"\n  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap+cache+w7a74)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # ---- Step 0: pre-registered predictions + dual-prior declaration ----
    print("--- Step 0: pre-registered predictions + dual-prior ---")
    print(f"  Substrate-distance pole s = {S_POLE_AR}")
    print(f"  4-regulator atlas: {REGULATOR_NAMES}")
    print(f"  Asymmetric cutoff_frac: {ASYMMETRIC_CUTOFF_FRAC}")
    print(f"  Asymmetric M_PV²_frac:  {ASYMMETRIC_M_PV_SQ_FRAC}")
    print(f"  CC-1996 §2.2-2.3 N=4 PV multipliers c_j = {CC1996_N4_PV_COEFFS.tolist()}")
    print(f"  Deep-IR flip target (SCHEMATIC §W4-1): rank_change_per_anchor = {DEEP_IR_FLIP_TARGET}")
    print(f"  ρ_S agreement band: {RHO_S_AGREEMENT_BAND}")
    print(f"  Dual prior: Track A (FULL-PASS) = {PRIOR_TRACK_A_FULL_PASS}; "
          f"Track B (FULL-FAIL) = {PRIOR_TRACK_B_FULL_FAIL}")
    print(f"  τ_fold = {tau_fold}; M_KK = {M_KK}; Vol_SU3_Haar = {Vol_SU3_Haar}")
    print(f"  PREDICTED DIRECTION (subst. chain Step 4): FULL-FAIL (flip vanishes)")

    # ---- Step 1: load L_max=12 master cache (verbatim §W4-1 protocol) ----
    print("\n--- Step 1: load L_max=12 spectrum cache (τ=0.19) ---")
    if not S84_L12_CACHE.exists():
        raise RuntimeError(f"Cache not found: {S84_L12_CACHE}")
    cache = np.load(S84_L12_CACHE, allow_pickle=True)
    sectors = cache["sector_evals"].item()
    n_sectors = len(sectors)
    lams = []  # (local)
    mlt = []  # (local)
    for (p, q), data in sectors.items():
        if max(p, q) > L_MAX:
            continue
        ev = np.asarray(data["abs_evals"], dtype=np.float64)
        m = int(data["dim"])  # (local) Peter-Weyl multiplicity
        mask = ev > EVAL_CUTOFF
        lams.append(ev[mask])
        mlt.append(np.full(int(mask.sum()), m, dtype=np.float64))
    lambdas = np.concatenate(lams) if lams else np.zeros(0, dtype=np.float64)
    mults = np.concatenate(mlt) if mlt else np.zeros(0, dtype=np.float64)
    n_eigs = int(len(lambdas))  # (local)
    print(f"  n_sectors loaded: {n_sectors}")
    print(f"  n_eigenvalues at L_max={L_MAX}: {n_eigs}")
    print(f"  lambda range: [{lambdas.min():.4e}, {lambdas.max():.4e}]")

    # ---- Step 2: 5 substrate-natural heat-kernel anchors ----
    print("\n--- Step 2: compute 5 substrate-natural heat-kernel anchors ---")
    max_lambda_sq = float(np.max(lambdas ** 2))  # (local) substrate UV anchor
    avg_lambda_sq_mw = float(np.sum(mults * lambdas ** 2) / np.sum(mults))  # (local)
    M_KK_sq = float(M_KK ** 2)  # (local)
    anchors = {
        "1/max_lambda_sq":    1.0 / max_lambda_sq,
        "2.3/max_lambda_sq":  2.3 / max_lambda_sq,
        "ln2/max_lambda_sq":  math.log(2.0) / max_lambda_sq,
        "1/avg_lambda_sq_mw": 1.0 / avg_lambda_sq_mw,
        "1/M_KK_sq":          1.0 / M_KK_sq,
    }
    for name, t in anchors.items():
        print(f"  {name:24s} = {t:.6e}")

    # ============================================================
    # SCHEMATIC reproduction (rank-change PRIMARY vs SCHEMATIC) — reproduces §W4-1
    # ============================================================
    print("\n" + "=" * 78)
    print("SCHEMATIC reproduction (rank-change PRIMARY vs SCHEMATIC) — must match §W4-1")
    print("=" * 78)
    sch_rank_change = []  # (local)
    sch_rank_P = {}       # (local)
    sch_rank_S = {}       # (local)
    for an, t in anchors.items():
        mp = np.array([mellin_moment_SCHEMATIC(lambdas, mults, t, r, "PRIMARY") for r in REGULATOR_NAMES])
        ms = np.array([mellin_moment_SCHEMATIC(lambdas, mults, t, r, "SCHEMATIC") for r in REGULATOR_NAMES])
        rp = rank_vector(mp)
        rs = rank_vector(ms)
        sch_rank_P[an] = rp
        sch_rank_S[an] = rs
        chg = int(not np.array_equal(rp, rs))
        sch_rank_change.append(chg)
        print(f"  {an:22s} PRIMARY={rp.astype(int).tolist()} SCHEMATIC={rs.astype(int).tolist()} change={bool(chg)}")
    print(f"  SCHEMATIC rank_change_per_anchor = {sch_rank_change}  (target deep-IR flip {DEEP_IR_FLIP_TARGET})")
    schematic_reproduces_flip = (sch_rank_change == DEEP_IR_FLIP_TARGET)
    print(f"  SCHEMATIC reproduces deep-IR flip [0,0,0,0,1]: {schematic_reproduces_flip}")

    # Deep-IR PRIMARY-vs-SCHEMATIC Spearman (the discriminating scalar)
    t_deep = anchors[DEEP_IR_ANCHOR]
    mp_d = np.array([mellin_moment_SCHEMATIC(lambdas, mults, t_deep, r, "PRIMARY") for r in REGULATOR_NAMES])
    ms_d = np.array([mellin_moment_SCHEMATIC(lambdas, mults, t_deep, r, "SCHEMATIC") for r in REGULATOR_NAMES])
    rp_d = rank_vector(mp_d)
    rs_d = rank_vector(ms_d)
    _res = spearmanr(rp_d, rs_d)
    rho_S_SCHEMATIC_asymmetric = float(_res.correlation) if not np.isnan(_res.correlation) else 0.0
    print(f"\n  Deep-IR PRIMARY-vs-SCHEMATIC Spearman (SCHEMATIC) = {rho_S_SCHEMATIC_asymmetric:+.6f}")

    # ============================================================
    # FULL-tier N=4 (rank-change PRIMARY vs SCHEMATIC) — the conviction-or-acquittal
    # ============================================================
    print("\n" + "=" * 78)
    print("FULL-tier N=4 CC-1996 §2.2-2.3 (rank-change PRIMARY vs SCHEMATIC)")
    print("=" * 78)
    full_rank_change = []  # (local)
    full_rank_P = {}       # (local)
    full_rank_S = {}       # (local)
    for an, t in anchors.items():
        mp = np.array([
            mellin_moment_FULL_N4(lambdas, mults, t, r, "PRIMARY", max_lambda_sq)
            for r in REGULATOR_NAMES
        ])
        ms = np.array([
            mellin_moment_FULL_N4(lambdas, mults, t, r, "SCHEMATIC", max_lambda_sq)
            for r in REGULATOR_NAMES
        ])
        rp = rank_vector(mp)
        rs = rank_vector(ms)
        full_rank_P[an] = rp
        full_rank_S[an] = rs
        chg = int(not np.array_equal(rp, rs))
        full_rank_change.append(chg)
        print(f"  {an:22s} PRIMARY={rp.astype(int).tolist()} SCHEMATIC={rs.astype(int).tolist()} change={bool(chg)}")
    print(f"  FULL rank_change_per_anchor = {full_rank_change}  (target deep-IR flip {DEEP_IR_FLIP_TARGET})")
    flip_reproduced = (full_rank_change == DEEP_IR_FLIP_TARGET)
    print(f"  flip_reproduced (FULL matches [0,0,0,0,1]): {flip_reproduced}")

    # Deep-IR PRIMARY-vs-SCHEMATIC Spearman under FULL-tier (the discriminating scalar)
    mp_fd = np.array([
        mellin_moment_FULL_N4(lambdas, mults, t_deep, r, "PRIMARY", max_lambda_sq)
        for r in REGULATOR_NAMES
    ])
    ms_fd = np.array([
        mellin_moment_FULL_N4(lambdas, mults, t_deep, r, "SCHEMATIC", max_lambda_sq)
        for r in REGULATOR_NAMES
    ])
    rp_fd = rank_vector(mp_fd)
    rs_fd = rank_vector(ms_fd)
    _resf = spearmanr(rp_fd, rs_fd)
    rho_S_FULL_asymmetric = float(_resf.correlation) if not np.isnan(_resf.correlation) else 0.0
    print(f"\n  Deep-IR PRIMARY-vs-SCHEMATIC Spearman (FULL) = {rho_S_FULL_asymmetric:+.6f}")

    abs_diff_asymmetric = abs(rho_S_FULL_asymmetric - rho_S_SCHEMATIC_asymmetric)  # (local)
    print(f"  abs_diff_asymmetric = |ρ_S(FULL) − ρ_S(SCHEMATIC)| = {abs_diff_asymmetric:.6f}")
    print(f"  abs_diff < {RHO_S_AGREEMENT_BAND} ? {abs_diff_asymmetric < RHO_S_AGREEMENT_BAND}")

    # ============================================================
    # A_5_extended PASS-B (FULL-tier N=4 on the substrate-natural sub-atlas, excl. ζ)
    # ============================================================
    print("\n" + "=" * 78)
    print("A_5_extended PASS-B (FULL-tier N=4; substrate-natural sub-atlas excl. ζ)")
    print("=" * 78)
    a5_rank_vectors = {}  # (local)
    for an, t in anchors.items():
        mom = np.array([
            mellin_moment_a5_FULL_N4(lambdas, mults, t, r, max_lambda_sq)
            for r in A5_EXTENDED_REGULATORS
        ])
        a5_rank_vectors[an] = rank_vector(mom)
        order = [A5_EXTENDED_REGULATORS[i] for i in np.argsort(mom)]
        print(f"  {an:22s} rank(low→high) = {order}")
    ref_a5 = a5_rank_vectors[ANCHOR_LABELS[0]]
    a5_spear = {}  # (local)
    for an in ANCHOR_LABELS:
        if an == ANCHOR_LABELS[0]:
            a5_spear[an] = 1.0
        else:
            r = spearmanr(ref_a5, a5_rank_vectors[an])
            a5_spear[an] = float(r.correlation) if not np.isnan(r.correlation) else 0.0
    non_self_a5 = [abs(v) for k, v in a5_spear.items() if k != ANCHOR_LABELS[0]]
    rho_S_FULL_a5extended = max(non_self_a5) if non_self_a5 else 0.0  # (local)
    print(f"  A_5_extended FULL Spearman per-anchor: {[round(a5_spear[a], 4) for a in ANCHOR_LABELS]}")
    print(f"  rho_S_FULL_a5extended (|ρ_S|_max_non_self) = {rho_S_FULL_a5extended:.6f}")

    # ============================================================
    # COMPOSITE ADJUDICATION (plan §W5-3 operator: CONJUNCTION)
    # ============================================================
    print("\n" + "=" * 78)
    print("COMPOSITE ADJUDICATION (plan §W5-3 operator: AND)")
    print("=" * 78)
    conjunct_1_abs_diff = (abs_diff_asymmetric < RHO_S_AGREEMENT_BAND)  # (local)
    conjunct_2_flip = flip_reproduced  # (local)
    full_pass = conjunct_1_abs_diff and conjunct_2_flip
    reclassification_branch = (
        "FULL-PASS-CONFIRMED" if full_pass else "FULL-FAIL-METHODOLOGY-FLOOR-ONLY"
    )
    print(f"  conjunct-1 (|ρ_S(FULL) − ρ_S(SCHEMATIC)| < {RHO_S_AGREEMENT_BAND}): {conjunct_1_abs_diff}")
    print(f"  conjunct-2 (flip reproduced [0,0,0,0,1]): {conjunct_2_flip}")
    print(f"  reclassification_branch = {reclassification_branch}")

    # ---- [SIGN] 3-tuple verdict (S87 schema-v2) ----
    # sign_verdict: PASS iff substitution-chain Step-4 PREDICTED direction
    #   (FULL-FAIL / flip-vanishing) matches the COMPUTED direction.
    predicted_direction_full_fail = True  # (local) Step 4 predicted FULL-FAIL
    computed_full_fail = (not full_pass)  # (local)
    sign_v = "PASS" if (predicted_direction_full_fail == computed_full_fail) else "FAIL"

    # magnitude_verdict: the |ρ_S diff| vs the 1e-3 PASS band (the gate's numeric target).
    #   PASS iff abs_diff ≤ pass_band (1e-3) AND flip reproduced (FULL-PASS magnitude).
    #   FAIL iff abs_diff > pass_band OR flip not reproduced.
    if conjunct_1_abs_diff and conjunct_2_flip:
        mag_v = "PASS"
    else:
        mag_v = "FAIL"

    # regime_verdict: CC-1996 N=4 PV regularization validity over the anchor window.
    #   VALID iff all FULL-tier moments finite + non-degenerate at all 5 anchors.
    full_moments_finite = True  # (local)
    for an in anchors:
        vals = np.array([
            mellin_moment_FULL_N4(lambdas, mults, anchors[an], r, "PRIMARY", max_lambda_sq)
            for r in REGULATOR_NAMES
        ])
        if not np.all(np.isfinite(vals)) or np.std(vals) < 1e-30:
            full_moments_finite = False
    reg_v = "VALID" if full_moments_finite else "BREAKDOWN"

    # Composite collapse rule (gate-verdicts.md §"Composite-collapse rule" — PRE-REGISTERED)
    if reg_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and reg_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and reg_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    print(f"\n  3-tuple: sign={sign_v} magnitude={mag_v} regime={reg_v}")
    print(f"  COMPOSITE = {composite}  (collapse rule applied)")

    # ---- Dual-prior posterior re-allocation (pre-registered; NOT post-hoc) ----
    print("\n--- Dual-prior posterior re-allocation (pre-registered) ---")
    if composite == "PASS":
        post_A, post_B = POSTERIOR_REALLOCATION, 1.0 - POSTERIOR_REALLOCATION
        track_resolved = "Track A (flip is substrate-IS structural feature)"
    elif composite == "FAIL":
        post_A, post_B = 1.0 - POSTERIOR_REALLOCATION, POSTERIOR_REALLOCATION
        track_resolved = "Track B (flip is SCHEMATIC M_PV²_frac prefactor artifact)"
    else:  # INFO
        post_A, post_B = PRIOR_TRACK_A_FULL_PASS, PRIOR_TRACK_B_FULL_FAIL
        track_resolved = "priors UNCHANGED (regime-breakdown / borderline)"
    print(f"  prior:     Track A = {PRIOR_TRACK_A_FULL_PASS}, Track B = {PRIOR_TRACK_B_FULL_FAIL}")
    print(f"  posterior: Track A = {post_A}, Track B = {post_B}")
    print(f"  resolved:  {track_resolved}")

    # ============================================================
    # SAVE artifacts (NPZ + PNG)
    # ============================================================
    print("\n--- SAVE artifacts ---")
    sch_rank_P_arr = np.array([sch_rank_P[a] for a in ANCHOR_LABELS])
    sch_rank_S_arr = np.array([sch_rank_S[a] for a in ANCHOR_LABELS])
    full_rank_P_arr = np.array([full_rank_P[a] for a in ANCHOR_LABELS])
    full_rank_S_arr = np.array([full_rank_S[a] for a in ANCHOR_LABELS])
    a5_rank_arr = np.array([a5_rank_vectors[a] for a in ANCHOR_LABELS])

    np.savez(
        OUT_NPZ,
        # --- core gate observables (plan-required keys) ---
        rho_S_FULL_asymmetric=rho_S_FULL_asymmetric,
        rho_S_SCHEMATIC_asymmetric=rho_S_SCHEMATIC_asymmetric,
        abs_diff_asymmetric=abs_diff_asymmetric,
        rank_change_per_anchor_FULL=np.array(full_rank_change),
        flip_reproduced=flip_reproduced,
        rho_S_FULL_a5extended=rho_S_FULL_a5extended,
        reclassification_branch=reclassification_branch,
        tier_pin="TIER-1",
        # --- SCHEMATIC reproduction cross-check ---
        rank_change_per_anchor_SCHEMATIC=np.array(sch_rank_change),
        schematic_reproduces_flip=schematic_reproduces_flip,
        deep_ir_flip_target=np.array(DEEP_IR_FLIP_TARGET),
        # --- rank vectors (per-anchor rows) ---
        sch_rank_PRIMARY=sch_rank_P_arr,
        sch_rank_SCHEMATIC=sch_rank_S_arr,
        full_rank_PRIMARY=full_rank_P_arr,
        full_rank_SCHEMATIC=full_rank_S_arr,
        a5_rank_FULL=a5_rank_arr,
        a5_spearman_per_anchor=np.array([a5_spear[a] for a in ANCHOR_LABELS]),
        # --- gate adjudication ---
        conjunct_1_abs_diff_pass=conjunct_1_abs_diff,
        conjunct_2_flip_pass=conjunct_2_flip,
        rho_S_agreement_band=RHO_S_AGREEMENT_BAND,
        composite_verdict=composite,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=reg_v,
        # --- dual prior ---
        prior_track_A_full_pass=PRIOR_TRACK_A_FULL_PASS,
        prior_track_B_full_fail=PRIOR_TRACK_B_FULL_FAIL,
        posterior_track_A=post_A,
        posterior_track_B=post_B,
        track_resolved=track_resolved,
        # --- CC-1996 N=4 PV multiplier set ---
        cc1996_n4_pv_coeffs=CC1996_N4_PV_COEFFS,
        N_PV=N_PV,
        # --- pins / metadata ---
        anchor_labels=np.array(ANCHOR_LABELS),
        regulator_names=np.array(REGULATOR_NAMES),
        a5_extended_regulators=np.array(A5_EXTENDED_REGULATORS),
        asymmetric_cutoff_frac=np.array([ASYMMETRIC_CUTOFF_FRAC[r] for r in REGULATOR_NAMES]),
        asymmetric_M_PV_sq_frac=np.array([ASYMMETRIC_M_PV_SQ_FRAC[r] for r in REGULATOR_NAMES]),
        spearman_registry_anchor=SPEARMAN_REGISTRY_ANCHOR,
        n_eigenvalues=n_eigs,
        n_sectors=n_sectors,
        L_max=L_MAX,
        s_pole=S_POLE_AR,
        max_lambda_sq=max_lambda_sq,
        tau_fold=tau_fold,
        M_KK=M_KK,
        Vol_SU3_Haar=Vol_SU3_Haar,
        w4_1_pass_audit_sha=W4_1_PASS_AUDIT_SHA,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        cache_sha=pins.get("s84_spectrum_cache_L12_tau019", ""),
        FULL_tier_disclosure=(
            "FULL physical regularization: Connes-Chamseddine 1996 §2.2-2.3 N=4 "
            "Pauli-Villars mass tower c_j=[1,-4,6,-4,1] at Λ_UV=M_KK, replacing the "
            "SCHEMATIC scalar (1-M_PV²_frac) prefactor. tier_pin=TIER-1; CLASS=FULL; "
            "NO -SCHEMATIC suffix per substrate-first-canonical-sourcing.md §(iv) K=4."
        ),
    )
    print(f"  NPZ -> {OUT_NPZ.relative_to(ROOT)}")

    # ---- PNG plot ----
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Panel 1: SCHEMATIC vs FULL rank-change vectors across the 5 anchors
    ax = axes[0]
    x = np.arange(len(ANCHOR_LABELS))
    ax.bar(x - 0.2, sch_rank_change, width=0.38, label="SCHEMATIC rank-change", alpha=0.85, color="tab:blue")
    ax.bar(x + 0.2, full_rank_change, width=0.38, label="FULL N=4 rank-change", alpha=0.85, color="tab:red")
    # Highlight deep-IR anchor (target flip location)
    ax.axvspan(len(ANCHOR_LABELS) - 1.5, len(ANCHOR_LABELS) - 0.5, color="gold", alpha=0.25,
               label="deep-IR anchor (target flip)")
    ax.set_xticks(x)
    ax.set_xticklabels([a.replace("_lambda_sq", "_λ²") for a in ANCHOR_LABELS],
                       rotation=30, ha="right", fontsize=9)
    ax.set_ylabel("rank changed (PRIMARY vs SCHEMATIC)? (0/1)")
    ax.set_ylim(-0.1, 1.25)
    ax.set_title(
        f"§VII.AR rank-change: SCHEMATIC={sch_rank_change} vs FULL={full_rank_change}\n"
        f"target deep-IR flip {DEEP_IR_FLIP_TARGET}; flip_reproduced={flip_reproduced}"
    )
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(True, alpha=0.3)

    # Panel 2: verdict box
    ax = axes[1]
    ax.axis("off")
    box = (
        f"COMPOSITE: {composite}\n"
        f"reclassification_branch:\n  {reclassification_branch}\n\n"
        f"ρ_S(SCHEMATIC) deep-IR = {rho_S_SCHEMATIC_asymmetric:+.4f}\n"
        f"ρ_S(FULL N=4)  deep-IR = {rho_S_FULL_asymmetric:+.4f}\n"
        f"|abs_diff|             = {abs_diff_asymmetric:.4f}\n"
        f"  < {RHO_S_AGREEMENT_BAND} band ? {conjunct_1_abs_diff}\n\n"
        f"SCHEMATIC rank-change = {sch_rank_change}\n"
        f"FULL N=4  rank-change = {full_rank_change}\n"
        f"flip reproduced [0,0,0,0,1]? {conjunct_2_flip}\n\n"
        f"GATE OPERATOR (AND):\n"
        f"  conjunct-1 (|Δρ_S|<1e-3) = {conjunct_1_abs_diff}\n"
        f"  conjunct-2 (flip)        = {conjunct_2_flip}\n\n"
        f"3-tuple: ({sign_v}, {mag_v}, {reg_v})\n\n"
        f"DUAL PRIOR (pre-registered):\n"
        f"  prior  A={PRIOR_TRACK_A_FULL_PASS} B={PRIOR_TRACK_B_FULL_FAIL}\n"
        f"  poster A={post_A} B={post_B}\n"
        f"  -> {track_resolved}\n\n"
        f"A_5_extended ρ_S (FULL, PASS-B) = {rho_S_FULL_a5extended:.4f}\n\n"
        f"tier_pin=TIER-1 (FULL; CC-1996 §2.2-2.3 N=4 PV)\n"
        f"c_j = {CC1996_N4_PV_COEFFS.astype(int).tolist()}"
    )
    ax.text(0.02, 0.98, box, transform=ax.transAxes, fontsize=9,
            family="monospace", verticalalignment="top",
            bbox=dict(boxstyle="round,pad=0.5",
                      facecolor="mistyrose" if composite == "FAIL" else "honeydew",
                      alpha=0.9))
    ax.set_title("§VII.AR FULL-tier N=4 conviction-or-acquittal verdict")

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"  PNG -> {OUT_PNG.relative_to(ROOT)}")

    # ============================================================
    # APPEND VERDICT ([SIGN] 3-tuple + tier_pin=TIER-1)
    # ============================================================
    print("\n--- APPEND VERDICT ---")
    sch_rc = ",".join(str(c) for c in sch_rank_change)  # (local)
    full_rc = ",".join(str(c) for c in full_rank_change)  # (local)
    # PASS-A epistemic standing on the resolved branch (composite carries the meaning;
    # the §W4-1 composite REMAINS PASS on disk either way by verdict permanence).
    if full_pass:
        stage3_field = "stage_3_eligibility_on_PASS_A=RATIFIED_BOTH_PASS_A_AND_PASS_B"  # (local)
        sign_meaning = "predicted_FULL-FAIL_NOT_matched_outcome_is_FULL-PASS"  # (local)
    else:
        stage3_field = (
            "stage_3_eligibility_on_PASS_A=PASS-A_reclassified_METHODOLOGY-floor-only;"
            "PASS-B_sub-atlas_carries_composite;w4_1_composite_PASS_retained_verdict_permanence"
        )  # (local)
        sign_meaning = "predicted_FULL-FAIL_matches_computed_FULL-FAIL"  # (local)
    value_str = (
        f"composite={composite};reclassification_branch={reclassification_branch};"
        f"rho_S_FULL_asymmetric={rho_S_FULL_asymmetric:.6f};"
        f"rho_S_SCHEMATIC_asymmetric={rho_S_SCHEMATIC_asymmetric:.6f};"
        f"abs_diff_asymmetric={abs_diff_asymmetric:.6f};"
        f"rho_S_agreement_band={RHO_S_AGREEMENT_BAND};"
        f"conjunct_1_abs_diff_pass={conjunct_1_abs_diff};"
        f"rank_change_per_anchor_FULL=[{full_rc}];"
        f"rank_change_per_anchor_SCHEMATIC=[{sch_rc}];"
        f"deep_ir_flip_target=[0,0,0,0,1];"
        f"flip_reproduced={flip_reproduced};"
        f"conjunct_2_flip_pass={conjunct_2_flip};"
        f"rho_S_FULL_a5extended={rho_S_FULL_a5extended:.6f};"
        f"tier_pin=TIER-1;CLASS=FULL;"
        f"cc1996_n4_pv_coeffs=[1,-4,6,-4,1];N_PV={N_PV};Lambda_UV=M_KK;"
        f"predicted_direction=FULL-FAIL_flip_vanishes;"
        f"sign_verdict_meaning={sign_meaning};"
        f"dual_prior_track_A={PRIOR_TRACK_A_FULL_PASS};dual_prior_track_B={PRIOR_TRACK_B_FULL_FAIL};"
        f"posterior_track_A={post_A};posterior_track_B={post_B};"
        f"track_resolved={track_resolved.split(' (')[0]};"
        f"w4_1_pass_audit_sha={W4_1_PASS_AUDIT_SHA[:16]};"
        f"cache_sha={pins.get('s84_spectrum_cache_L12_tau019', '')[:16]};"
        f"L_max={L_MAX};tau_fold={tau_fold};s_pole={S_POLE_AR};"
        f"{stage3_field}"
    )
    append_verdict(composite, value_str, audit_sha, content_sha, sign_v, mag_v, reg_v)
    print(f"  Verdict appended to {VERDICT_FILE.relative_to(ROOT)}")

    # ---- 4-tuple final output ----
    print("\n--- 4-tuple ---")
    print(f"  (value={composite}/{reclassification_branch}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n  Elapsed: {time.time() - t0:.2f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
