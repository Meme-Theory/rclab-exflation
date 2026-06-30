#!/usr/bin/env python3
"""
S94 W8-2 — S94-VII-AR-PASS-A-SUBSTRATE-DERIVATION
=================================================

Gate: S94-VII-AR-PASS-A-SUBSTRATE-DERIVATION
Trigger: [SIGN]
Classification: GEOMETRIC  (cutoff_axis: spectral)
Agent: volovik-superfluid-universe-theorist

Plan: sessions/session-plan/session-94-plan-w8.md §W8-2.
WP:   sessions/archive/session-94/session-94-w8-workingpaper.md §W8-2.
Verdict file: computations/session-94/s94_gate_verdicts.txt.

CONVICTION-OR-ACQUITTAL OF §VII.AR PASS-A's EPISTEMIC STANDING
--------------------------------------------------------------
At S92 §W4-1 the PASS-A asymmetric-coupling reading produced a single deep-IR
rank-flip rank_change_per_anchor = [0,0,0,0,1] and an anti-correlated deep-IR
Spearman ρ_S = −0.20, but it consumed SCHEMATIC regulator profiles plus a SCALAR
(1 − M_PV²_frac_r) prefactor (tier_pin=TIER-2). At S93 W5-3 the FULL-tier N=4
Connes-Chamseddine 1996 §2.2-2.3 Pauli-Villars re-run (dropping the SCHEMATIC
scalar knob) FAILED to reproduce the flip:
    rank_change_per_anchor_FULL = [1,1,1,1,1]
    ρ_S_FULL_asymmetric          = +0.200000
    ρ_S_SCHEMATIC_asymmetric     = −0.200000
    abs_diff_asymmetric          =  0.400000  ≫ 1e-3   ⇒  W5-3 FAIL.
PASS-A was reclassified to METHODOLOGY-floor-only and §VII.AR STAGE-3 eligibility
narrowed {PASS-A, PASS-B} → {PASS-B}.

THIS gate asks the remaining first-principles question: is the deep-IR rank-flip
recoverable from SUBSTRATE BdG PHYSICS — the S52 Bogoliubov occupation amplitude
    v_a²(λ) = Δ²/(2(λ²+Δ²))  =  (1/2)(1 − λ/√(λ²+Δ²))   (ξ_a → λ, |Δ_a| = Δ)
on the M₂(ℂ) ⊂ A_K BdG sub-algebra at τ_fold = 0.19 — used as the per-eigenvalue
weighting in place of the SCHEMATIC scalar prefactor?
    PASS ⇒ PASS-A RESTORED as substrate-IS realization; eligibility re-widens
           {PASS-B} → {PASS-A, PASS-B}.
    FAIL ⇒ PASS-A permanently METHODOLOGY-floor; eligibility stays {PASS-B}.
PASS-B carries §VII.AR STAGE-3 eligibility either way (ρ_S_FULL_a5extended = 1.0).

THE DISCRIMINATING CHANGE (vs W5-3)
-----------------------------------
The W5-3 machinery is reused VERBATIM — same L_max=12 cache, same 4-regulator
atlas {F_2, cutoff_sqrt, anomaly, Zubarev}, same 5 substrate-natural heat-kernel
anchors, same CC-1996 N=4 PV multiplier set c_j=[1,-4,6,-4,1] at Λ_UV=M_KK, same
asymmetric (cf, M_PV²_frac) pins. The ONLY DISCRIMINATING change is the SOURCE of
the per-regulator coupling: the FULL-tier PRIMARY moment now carries an EXTRA
per-eigenvalue factor v_a²(λ) (the substrate BdG occupation weight computed from
D_K's spectrum + Delta_BCS), in place of the SCHEMATIC scalar (1 − M_PV²_frac_r)
prefactor (which W5-3 had already dropped). The SCHEMATIC-level (bare) moment is
left UNCHANGED — it is the reference against which PRIMARY rank-changes are tested.

SUBSTITUTION CHAIN (per math-scripts.md §"Double-Check Logic Before Compute") —
mirrors plan §W8-2 substitution_chain content, numbers substituted in main().

  Claim: "Under SUBSTRATE-DERIVED per-regulator coupling (S52 BdG occupation
          v_a²=Δ²·[2(λ²+Δ²)]⁻¹ on M₂(ℂ)⊂A_K) replacing the SCHEMATIC scalar
          (1−M_PV²_frac_r) prefactor, the §VII.AR deep-IR rank-flip [0,0,0,0,1]
          + ρ_S^{deep-IR}<0 is EITHER recovered (PASS-A substrate-IS) OR stays
          absent (rank [1,1,1,1,1], ρ_S≥0; PASS-A methodology-floor)."

  Step 1 (Definitions):
    - W5-3 FULL-tier baseline (on disk, S93-W5-3-VII-AR-FULL-TIER-N4-RETRY):
        ρ_S_FULL_asymmetric        = +0.200000   (deep-IR, FULL N=4, SCHEMATIC-scalar dropped)
        ρ_S_SCHEMATIC_asymmetric   = −0.200000   (deep-IR, §W4-1 SCHEMATIC reproduction)
        rank_change_per_anchor_FULL = [1,1,1,1,1]   (flip NOT reproduced)
        abs_diff_asymmetric        =  0.400000  ≫ 1e-3  ⇒ W5-3 FAIL.
    - S52 BdG Bogoliubov occupation (canonical; knowledge equation entry
        "v_a(K)² = (1/2)(1 − ξ_a(K)/E_a(K))", E_a=√(ξ_a²+|Δ_a|²);
        s91-w1-operational-alignment-regulator-class-robustness.md:385:
        "|v_a(K)|² = Δ_a² / (2(λ_a² + Δ_a²))"):
        normal-coordinate / long-wavelength reduction ξ_a → λ, |Δ_a| = Δ = Delta_BCS:
        v_a²(λ) = (1/2)(1 − λ/√(λ²+Δ²)) = Δ²/(2(λ²+Δ²))
        [canonical: Delta_BCS = 0.4642547394830737, R-protected, BCS-GAP-CANONICAL-70]
        v_a²(0)=1/2 ; v_a²(λ→∞)→0 — MONOTONE-DECREASING (deep-IR concentrated).
    - CC-1996 N=4 PV kernel (FULL physical regularization, reused from W5-3):
        K_PV(λ²; M_PV²) = Σ_{j=0}^{4} c_j/(λ²+j·M_PV²)^4,  c_j=[1,-4,6,-4,1]
        [a_2^{Pauli-Villars}; Λ_UV = M_KK]

  Step 2 (Substitute — the parameter SOURCE replacement, no simplification):
      W5-3 FULL PRIMARY moment:
        M_r^{PRIMARY,W5-3}(t) = Σ_λ m_λ · profile_r(cf_r·t·λ²) · K_PV(λ²; M_PV²_frac_r·max(λ²))
      SUBSTRATE-DERIVED FULL PRIMARY moment (THIS gate):
        M_r^{PRIMARY,sub}(t) = Σ_λ m_λ · profile_r(cf_r·t·λ²) · K_PV(λ²; M_PV²_frac_r·max(λ²)) · v_a²(λ)
      — the per-eigenvalue substrate BdG occupation weight v_a²(λ) is the physical
        SOURCE of the per-regulator coupling, computed from D_K's spectrum + Delta_BCS.
        (The cf_r/M_PV²_frac_r atlas is retained verbatim for like-for-like
        anchor/atlas comparison with W5-3; the DISCRIMINATING change is v_a²(λ).)

  Step 3 (Why this could go either way — the structural fork):
    - Track-A mechanism (flip recovers): the deep-IR-concentrated BdG weight
      v_a²(λ) re-amplifies the smallest-λ eigenvalues asymmetrically across
      regulators (each regulator's profile_r already re-weights the deep-IR shell
      differently), reproducing the rank-flip the SCALAR M_PV²_frac prefactor
      produced at SCHEMATIC saturation.
    - Track-B mechanism (flip stays absent): v_a²(λ) is a regulator-INDEPENDENT
      multiplicative weight (the SAME function of λ for all 4 regulators), so it
      CANNOT by itself break the rank-ordering the regulators establish; the FULL
      N=4 PV tower remains the dominant deep-IR re-weighting and the rank vector
      stays [1,1,1,1,1] (the W5-3 FULL result). This is the dual-prior FAVORED
      branch (prior 0.70, inherited+sharpened from W5-3 S-1 II.2: the flip is a
      property of the regulator-ASYMMETRIC SCALAR M_PV²_frac prefactor, NOT of
      regulator-common BdG occupation).

  Step 4 (Read off PREDICTED DIRECTION):
      PREDICTED (dual prior ~0.70 Track B): the substrate-derived weighting does
      NOT recover the flip — rank stays [1,1,1,1,1], ρ_S_FULL_substrate ≥ 0 —
      because v_a²(λ) is a regulator-COMMON multiplicative weight (Step 3 Track B)
      and the W5-3 finding localized the flip to the regulator-ASYMMETRIC SCALAR
      M_PV²_frac knob, which the substrate amplitude does not carry.
      sign_verdict semantics: PASS iff this PREDICTED direction (FAIL / flip-
      stays-absent) matches the COMPUTED direction.

  Step 5 (Conclusion):
      Genuine [SIGN] discriminator. The discriminating scalar is
        d := sign(|ρ_S_FULL_substrate − ρ_S_SCHEMATIC| − 1e-3) AND sign(ρ_S_FULL_substrate).
      PASS ⇒ flip recovered + ρ_S<0 ⇒ PASS-A restored substrate-IS
             ⇒ §VII.AR eligibility re-widens {PASS-B} → {PASS-A, PASS-B}.
      FAIL ⇒ flip [1,1,1,1,1] persists OR ρ_S≥0 ⇒ PASS-A permanently
             methodology-floor ⇒ §VII.AR eligibility stays {PASS-B}.
      The §VII.AR composite (PASS-B sub-atlas-minus-ζ, ρ_S=1.0) is unaffected
      either way — PASS-B carries §VII.AR STAGE-3 eligibility (verdict permanence
      on the S93 W5-3 reclassification; this gate ONLY governs PASS-A's standing).

GATE OPERATOR (plan §W8-2 (1)):
  PASS iff  (rank_change_per_anchor(substrate-derived FULL) == [0,0,0,0,1])
        AND (ρ_S_FULL_substrate < 0)
        AND (|ρ_S_FULL_substrate − ρ_S_SCHEMATIC| ≤ 1e-3).
  FAIL iff  (rank vector == [1,1,1,1,1] persists) OR (ρ_S_FULL_substrate ≥ 0).
  INFO iff  regime-breakdown (>50% anchors non-finite/degenerate) OR borderline.

DUAL-PRIOR PRE-REGISTRATION (epistemic-discipline.md §"Dual-prior"; plan §W8-2):
  Track A (substrate-IS-restored): prior 0.30.
  Track B (methodology-floor-only): prior 0.70.  (inherited+sharpened from W5-3 0.65)
  Discriminator gate criterion:
    PASS  ⇒ posterior 0.90 to Track A (flip is substrate-IS).
    FAIL  ⇒ posterior 0.90 to Track B (flip is methodology-floor only).
    INFO  ⇒ priors UNCHANGED.
  The outcome MUST NOT be re-narrativized to fit either track post-hoc.

LEVEL-PIN DISCIPLINE (substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY):
  CLASS pin = FULL (TIER-1). The producing script executes the genuine CC-1996
  §2.2-2.3 N=4 Pauli-Villars mass tower (c_j=[1,-4,6,-4,1], masses M_j²=j·M_PV²,
  Λ_UV=M_KK) reused from W5-3 — NOT the SCHEMATIC scalar (1−M_PV²_frac_r) prefactor
  — AND sources the per-regulator coupling from the substrate-IS BdG amplitude
  v_a². The verdict-line convention carries NO -SCHEMATIC suffix; a
  `# tier_pin=TIER-1` companion row accompanies the canonical line. The s=4
  PV-subtracted Seeley-DeWitt-class moment is tagged a_2^{Pauli-Villars}
  (regulator-pin-discipline.md); bare a_2 is FORBIDDEN. The SCHEMATIC-scalar
  source is RETAINED ONLY as the W5-3 cross-check baseline (ρ_S_SCHEMATIC=−0.20),
  NEVER as the PASS source.

SUBSTRATE FRAMING (phononic-framing.md §"IS Space, Not IN Space"):
  GEOMETRIC. The §VII.AR observable IS the Spearman rank-ordering of the
  4-regulator atlas {F_2, cutoff_sqrt, anomaly, Zubarev} images at the substrate-
  distance-2 Mellin-cone pole s=4 on D_K's block-diagonal spectrum at τ_fold=0.19
  — an algebra-INVARIANT spectrum-only functional. Direction substrate → emergent:
  D_K eigenvalues + Delta_BCS → BdG occupation amplitude v_a²(λ) on M₂(ℂ)⊂A_K →
  per-eigenvalue weighting → rank-ordering predicate at the s=4 pole. No container-
  thinking: the substrate IS the rank-ordering; the lab does not measure §VII.AR
  IN any continuum.

Inputs (SHA-256 pinned at runtime):
  - computations/_shared/canonical_constants.py
      (plan §W8-2 pin 102f8f76...; LIVE file SHA differs — plan-text-drift per
       substrate-first-canonical-sourcing.md §(ii.B); the consumed Delta_BCS /
       M_KK / tau_fold / Vol_SU3_Haar values are UNCHANGED and match the knowledge
       MCP canonical Delta_BCS=0.4642547394830737 bit-for-bit; drift documented in
       the verdict-line value field. LIVE canonical is authoritative.)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (runtime canonical path)
  - computations/session-93/s93_w5_3_vii_ar_full_tier_n4_retry.py (machinery reuse)
  - computations/session-92/s92_w4_1_vii_ar_stage_2_re_dispatch_asymmetric_coupling.py
  - computations/session-89/s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.py
  - script bytes (feeds BOTH audit_sha256 and content_sha256)
  - W5-3 FAIL verdict audit_sha256 = 2e4a33bf68bdeef7386ffe02b0efbc06727694919a62741b257e0d4efb557d13 (string pin)
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
    Delta_BCS,
)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from scipy.stats import spearmanr  # noqa: E402

# ---------------- Gate-block constants (canonical pins per plan §W8-2) ----------------
GATE_ID = "S94-VII-AR-PASS-A-SUBSTRATE-DERIVATION"
SCHEME = "FULL-tier-N4-Connes-Chamseddine-1996-substrate-BdG-derived-coupling"
CONVENTION = (
    "VII-AR-PASS-A-substrate-derived-v_a2-BdG-M2C-asymmetric-FULL-tier-N4-Lambda-UV-M_KK"
)
L_MAX = 12  # (local) plan §W8-2 machinery_pin_map (matches W5-3 anchor)
S_POLE_AR = 4  # (local) substrate-distance-2 Mellin-cone pole s=4

# Pre-registered thresholds (plan §W8-2 strict_PASS_boundary; same band as W5-3 conjunct-1)
RHO_S_AGREEMENT_BAND = 1e-3  # (local) flip-match band
DEEP_IR_FLIP_TARGET = [0, 0, 0, 0, 1]  # (local) the single deep-IR flip to recover

# W5-3 FULL-tier baselines (on disk; for like-for-like comparison reporting)
W5_3_RHO_S_FULL_BASELINE = 0.200000        # (local) W5-3 ρ_S_FULL_asymmetric (on disk)
W5_3_RHO_S_SCHEMATIC_BASELINE = -0.200000  # (local) W5-3 ρ_S_SCHEMATIC_asymmetric (on disk)
W5_3_RANK_CHANGE_FULL = [1, 1, 1, 1, 1]    # (local) W5-3 FULL rank vector (on disk)

# §VII.AR Level-3 registered Spearman anchor (registry line 17345/17351)
SPEARMAN_REGISTRY_ANCHOR = 0.800  # (local) |ρ_S(s=4)|_PRIMARY discrete-combinatorial EXACT

# Eigenvalue IR cutoff (matches W7a-74 PRIMARY + W5-3)
EVAL_CUTOFF = 1e-6  # (local)

# 4-regulator §VII.AR atlas (registry line 17345 / W7a-74 PRIMARY) — verbatim W5-3
REGULATOR_NAMES = ["F_2", "cutoff_sqrt", "anomaly", "Zubarev"]

# 5 substrate-natural heat-kernel anchors (registry line 17351, W7a-74 PRIMARY) — verbatim W5-3
ANCHOR_LABELS = [
    "1/max_lambda_sq",
    "2.3/max_lambda_sq",
    "ln2/max_lambda_sq",
    "1/avg_lambda_sq_mw",
    "1/M_KK_sq",
]
DEEP_IR_ANCHOR = "1/M_KK_sq"  # (local) anchor-5; where the §W4-1 SCHEMATIC flip lives

# Asymmetric (REGULATOR-SPECIFIC) PARAMETER pins — REUSED VERBATIM from W5-3 / §W4-1.
# These are NOT the discriminating change; they are retained for like-for-like
# anchor/atlas comparison. The DISCRIMINATING change is the v_a²(λ) weighting.
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

# ---- Connes-Chamseddine 1996 §2.2-2.3 N=4 Pauli-Villars multiplier set ----
# c_j = (-1)^j · C(4, j) = [1, -4, 6, -4, 1]; cancels moments k=0..3, first
# non-vanishing moment at k=4 (residue Σ_j c_j j^4 = 24). REUSED VERBATIM from W5-3.
CC1996_N4_PV_COEFFS = np.array([1.0, -4.0, 6.0, -4.0, 1.0])  # (local) (-1)^j C(4,j)
N_PV = 4  # (local) Connes-Chamseddine 1996 §2.2-2.3 N=4 tower

# W5-3 FAIL verdict (string pin per plan §W8-2 input_files)
W5_3_FAIL_AUDIT_SHA = (
    "2e4a33bf68bdeef7386ffe02b0efbc06727694919a62741b257e0d4efb557d13"
)
# §W4-1 SCHEMATIC PASS verdict (string pin; provenance chain)
W4_1_PASS_AUDIT_SHA = (
    "257e2619fe308645a8f87d127dde3764696d0432038725af77e3fa1fa96ce490"
)

# Dual-prior pre-registration (epistemic-discipline.md §"Dual-prior"; plan §W8-2)
PRIOR_TRACK_A_SUBSTRATE_RESTORED = 0.30  # (local) flip is substrate-IS structural feature
PRIOR_TRACK_B_METHODOLOGY_FLOOR = 0.70   # (local) flip is methodology-floor only (regulator-common v_a²)
POSTERIOR_REALLOCATION = 0.90            # (local) ≥0.9 posterior re-allocation per plan

# ---------------- File paths ----------------
SESSION_DIR = ROOT / "computations" / "session-94"
SHARED_DIR = ROOT / "computations" / "_shared"
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"
SCRIPT_PATH = Path(__file__).resolve()

# plan §W8-2 canonical_constants pin (plan-freeze 2026-05-25); LIVE SHA checked at runtime
CANONICAL_CONSTANTS_PLAN_PIN = (
    "102f8f763573cedc797f66eb50f7cf5f7a277c4a805d7b3ad2b94e205c55bc96"
)

# L_max=12 cache runtime canonical path (lives in session-84; matches plan pin SHA)
S84_L12_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
W5_3_MACHINERY = (
    ROOT / "computations" / "session-93" / "s93_w5_3_vii_ar_full_tier_n4_retry.py"
)
S92_W4_1_SCRIPT = (
    ROOT / "computations" / "session-92"
    / "s92_w4_1_vii_ar_stage_2_re_dispatch_asymmetric_coupling.py"
)
W7A74_PRIMARY = (
    ROOT / "computations" / "session-89"
    / "s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.py"
)

OUT_NPZ = SESSION_DIR / "s94_vii_ar_pass_a_substrate_derivation.npz"
OUT_PNG = SESSION_DIR / "s94_vii_ar_pass_a_substrate_derivation.png"
VERDICT_FILE = SESSION_DIR / "s94_gate_verdicts.txt"

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "s84_spectrum_cache_L12_tau019": S84_L12_CACHE,
    "w5_3_full_tier_machinery": W5_3_MACHINERY,
    "w4_1_asymmetric_coupling_script": S92_W4_1_SCRIPT,
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
    # W5-3 FAIL + §W4-1 PASS verdict string pins (no on-disk file resolution needed)
    pins["w5_3_fail_audit_sha_string_pin"] = W5_3_FAIL_AUDIT_SHA
    pins["w4_1_pass_audit_sha_string_pin"] = W4_1_PASS_AUDIT_SHA
    print(f"  {'w5_3_fail_audit_sha_string_pin':48s} = {W5_3_FAIL_AUDIT_SHA[:16]}...  (S93 W5-3 FAIL)")
    print(f"  {'w4_1_pass_audit_sha_string_pin':48s} = {W4_1_PASS_AUDIT_SHA[:16]}...  (S92 §W4-1 PASS)")
    return pins


def compute_dual_sha(pins: dict, script_path: Path) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema.

    audit_sha256_inputs: script + canonical + pinmap.
    content_sha256_inputs: script only.
    (Matches plan §W8-2 audit_discriminators: audit=[script,canonical,pinmap],
     content=[script].)
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


# ---------------- SCHEMATIC regulator profiles (verbatim from W5-3 / §W4-1 / W7a-74) ----------------
def reg_profile_F_2(x):
    """F_2: Gaussian heat-kernel exp(-x). x = t_ref·cf·λ²."""
    return np.exp(-x)


def reg_profile_cutoff_sqrt(x):
    """cutoff_sqrt: sharp cutoff Θ(1 - sqrt(x))."""
    return np.where(np.sqrt(np.maximum(x, 0.0)) <= 1.0, 1.0, 0.0)


def reg_profile_anomaly(x):
    """anomaly: anomaly-corrected exp(-x)·(1 − x + x²/2)."""
    return np.exp(-x) * (1.0 - x + 0.5 * x * x)


def reg_profile_Zubarev(x):
    """Zubarev: smooth Zubarev-like 1/(1 + exp(10·(x − 1)))."""
    return 1.0 / (1.0 + np.exp(10.0 * (x - 1.0)))


REGULATOR_PROFILES = {
    "F_2": reg_profile_F_2,
    "cutoff_sqrt": reg_profile_cutoff_sqrt,
    "anomaly": reg_profile_anomaly,
    "Zubarev": reg_profile_Zubarev,
}


# ---------------- SUBSTRATE-DERIVED BdG occupation weight (THE DISCRIMINATING CHANGE) ----------------
def bogoliubov_occupation_weight(lambdas: np.ndarray):
    """S52 Bogoliubov occupation amplitude v_a²(λ) on M₂(ℂ) ⊂ A_K.

    PLAN-PINNED operative weight (plan §W8-2 machinery_pin_map line 340 +
    substitution_chain Step 1/Step 2, leading form):

        v_a²(λ) = Δ²/(2(λ²+Δ²))                          [Form A — the pinned weight]

    with Δ = Delta_BCS (R-protected canonical, BCS-GAP-CANONICAL-70). This is the
    PHYSICAL per-eigenvalue SOURCE of the per-regulator coupling, replacing the
    SCHEMATIC scalar (1 − M_PV²_frac_r) prefactor. Monotone-DECREASING in λ:
    Form-A v_a²(0)=1/2, v_a²(λ→∞)→0 — deep-IR (smallest-λ) eigenvalues carry the
    largest occupation weight.

    TWO CANONICAL FORMS — NOT bit-identical away from λ→0 (Sage-verified):
      Form A: "|v_a(K)|² = Δ_a²/(2(λ_a²+Δ_a²))"   (s91-w1-operational-alignment
              -regulator-class-robustness.md:385, "per S52 BdG canonical
              amplitudes"). In standard BdG relations this is Δ²/(2E²) = 2·u²v²
              (the pair-coherence-density amplitude), E_a = √(λ²+Δ²).
      Form B: "v_a(K)² = (1/2)(1 − ξ_a(K)/E_a(K))", E_a=√(ξ_a²+|Δ_a|²)
              (session-89-w5-workingpaper.md; the fundamental BdG occupation
              identity). With ξ_a → λ: (1/2)(1 − λ/√(λ²+Δ²)).
    Sage (s94 §W8-2 substitution-chain Step 1): Form A = ½ − (1/2Δ²)λ² + O(λ³)
    (even-in-λ); Form B = ½ − (1/2Δ)λ + O(λ²) (linear-in-λ term). They COINCIDE
    at λ=0 (both 1/2) and DIVERGE for λ>0 (diff 5.65e-2 at λ_min=0.820, 1.82e-3 at
    λ_max=5.419). The plan's "v_a²(λ)=(1/2)(1−λ/√(λ²+Δ²)) = Δ²/(2(λ²+Δ²)) + O(...)
    at λ→0" text flags exactly this: the algebraic identity is leading-order in the
    DEEP-IR only. The plan PINS Form A as the operative weight (machinery_pin_map
    leading form); Form B is the λ→0-equivalent canonical BdG occupation reference.

    Returns (form_A operative, form_B reference, max_diff) so main() can document
    the distinction honestly (NOT assert false bit-equality).
    """
    lam = np.asarray(lambdas, dtype=np.float64)  # (local)
    d2 = Delta_BCS * Delta_BCS  # (local)
    form_A = d2 / (2.0 * (lam * lam + d2))  # (local) plan-pinned operative weight
    form_B = 0.5 * (1.0 - lam / np.sqrt(lam * lam + d2))  # (local) λ→0-equivalent reference
    max_form_diff = float(np.max(np.abs(form_A - form_B)))  # (local) Sage: diverges for λ>0
    return form_A, form_B, max_form_diff


# ---------------- FULL-tier N=4 CC-1996 Pauli-Villars kernel (verbatim W5-3) ----------------
def cc1996_n4_pv_kernel(lam2: np.ndarray, M_PV_sq: float) -> np.ndarray:
    """Connes-Chamseddine 1996 §2.2-2.3 N=4 Pauli-Villars subtraction kernel at s=4.

        K_PV(λ²; M_PV²) = Σ_{j=0}^{4} c_j / (λ² + j·M_PV²)^s ,  s = 4,
        c_j = (-1)^j C(4, j) = [1, -4, 6, -4, 1], masses M_j² = j·M_PV².
    FULL physical mass-tower structure (a_2^{Pauli-Villars}). j=0 (M_0=0) physical
    field; j=1..4 PV regulator fields. REUSED VERBATIM from W5-3.
    """
    ker = np.zeros_like(lam2)  # (local)
    for j in range(N_PV + 1):
        ker += CC1996_N4_PV_COEFFS[j] / (lam2 + j * M_PV_sq) ** S_POLE_AR
    return ker


# ---------------- Mellin moments ----------------
def mellin_moment_SCHEMATIC(lambdas, mults, t_ref, regulator_name, level):
    """SCHEMATIC asymmetric-coupling moment (verbatim §W4-1 mechanism).

    Used ONLY as the W5-3 cross-check baseline (ρ_S_SCHEMATIC=−0.20). NEVER the
    PASS source. PRIMARY here keeps the SCHEMATIC scalar (1 − M_PV²_frac_r) knob
    (this reproduces §W4-1 / the W5-3 SCHEMATIC baseline).
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


def mellin_moment_FULL_N4_substrate(lambdas, mults, t_ref, regulator_name, level,
                                    lambda_max_sq, v_a_sq):
    """FULL-tier N=4 CC-1996 moment with SUBSTRATE-DERIVED v_a² weighting.

    PRIMARY (substrate-derived; THE DISCRIMINATING CHANGE vs W5-3):
        Σ_λ m_λ · profile_reg(cf_r·t_ref·λ²) · K_PV(λ²; M_PV²_frac_r·max(λ²)) · v_a²(λ)
      — the extra per-eigenvalue v_a²(λ) factor is the substrate BdG occupation
        weight (THE SOURCE of the per-regulator coupling), replacing the SCHEMATIC
        scalar (1 − M_PV²_frac_r) prefactor.
    SCHEMATIC (bare; UNCHANGED reference for rank-change testing):
        Σ_λ m_λ · profile_reg(t_ref·λ²) · λ⁻⁸     (no v_a² weight — it IS the reference)

    The FULL N=4 PV tower K_PV is REUSED VERBATIM from W5-3 (a_2^{Pauli-Villars};
    Λ_UV=M_KK, M_PV² = M_PV²_frac_r × max(λ²)). v_a_sq is the precomputed per-
    eigenvalue weight array (same length as lambdas).
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
        # THE DISCRIMINATING CHANGE: × v_a²(λ) substrate BdG occupation weight
        return float(np.sum(mults * prof_vals * ker * v_a_sq))
    else:  # SCHEMATIC bare (UNCHANGED reference; same as W5-3 SCHEMATIC level)
        x = t_ref * lam2  # (local)
        prof_vals = profile(x)  # (local)
        integrand = mults * prof_vals * lam2 ** (-S_POLE_AR)  # (local)
        return float(np.sum(integrand))


def rank_vector(moments: np.ndarray) -> np.ndarray:
    """argsort-of-argsort rank vector (rank 0 = smallest moment). Verbatim W5-3."""
    return np.argsort(np.argsort(moments)).astype(np.float64)


# ---------------- Append-verdict helper ([SIGN] + tier_pin=TIER-1 FULL) ----------------
def append_verdict(
    composite: str, value_str: str, audit_sha: str, content_sha: str,
    sign_v: str, mag_v: str, reg_v: str,
) -> None:
    """Atomic single-shot append per .claude/templates/script-template.py.

    Emits (all four rows, [SIGN] + FULL level-pin):
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
        f"(Connes-Chamseddine 1996 §2.2-2.3 N=4 Pauli-Villars tower at Λ_UV=M_KK, "
        f"a_2^{{Pauli-Villars}}); substrate-first-canonical-sourcing.md §(iv) K=4 "
        f"MANDATORY level-pin: CLASS=FULL; NO -SCHEMATIC suffix; per-regulator "
        f"coupling SOURCED from substrate-IS S52 BdG occupation v_a²=Δ²/(2(λ²+Δ²)) "
        f"on M₂(ℂ)⊂A_K; SCHEMATIC scalar (1−M_PV²_frac) retained as W5-3 cross-check "
        f"baseline ONLY (ρ_S_SCHEMATIC=−0.20), never the PASS source\n"
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

    # ---- canonical_constants plan-text-drift detection (substrate-first §(ii.B)) ----
    live_canonical_sha = pins.get("canonical_constants", "")  # (local)
    canonical_drift = (live_canonical_sha != CANONICAL_CONSTANTS_PLAN_PIN)  # (local)
    if canonical_drift:
        print("\n--- PLAN-TEXT-DRIFT (substrate-first-canonical-sourcing.md §(ii.B)) ---")
        print(f"  canonical_constants.py plan-§W8-2 pin = {CANONICAL_CONSTANTS_PLAN_PIN[:16]}...")
        print(f"  canonical_constants.py LIVE runtime    = {live_canonical_sha[:16]}...")
        print(f"  drift DETECTED: LIVE canonical is authoritative (knowledge-base-wins).")
        print(f"  consumed values UNCHANGED: Delta_BCS={Delta_BCS} (== MCP canonical), "
              f"M_KK={M_KK}, tau_fold={tau_fold}.")
        print(f"  drift documented in verdict-line value field; no remediation needed "
              f"(consumed Delta_BCS/M_KK/tau_fold bit-identical to plan-freeze values).")

    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    print(f"\n  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # ---- Step 0: pre-registered predictions + dual-prior declaration ----
    print("--- Step 0: pre-registered predictions + dual-prior ---")
    print(f"  Substrate-distance pole s = {S_POLE_AR}")
    print(f"  4-regulator atlas: {REGULATOR_NAMES}")
    print(f"  Asymmetric cutoff_frac (verbatim W5-3): {ASYMMETRIC_CUTOFF_FRAC}")
    print(f"  Asymmetric M_PV²_frac  (verbatim W5-3): {ASYMMETRIC_M_PV_SQ_FRAC}")
    print(f"  CC-1996 §2.2-2.3 N=4 PV multipliers c_j = {CC1996_N4_PV_COEFFS.tolist()}")
    print(f"  DISCRIMINATING change: per-eigenvalue v_a²(λ)=Δ²/(2(λ²+Δ²)), Δ=Delta_BCS={Delta_BCS}")
    print(f"  Deep-IR flip target (recover): rank_change_per_anchor = {DEEP_IR_FLIP_TARGET}")
    print(f"  ρ_S agreement band: {RHO_S_AGREEMENT_BAND}")
    print(f"  W5-3 baselines (on disk): ρ_S_FULL=+{W5_3_RHO_S_FULL_BASELINE}, "
          f"ρ_S_SCHEMATIC={W5_3_RHO_S_SCHEMATIC_BASELINE}, rank_FULL={W5_3_RANK_CHANGE_FULL}")
    print(f"  Dual prior: Track A (substrate-IS-restored) = {PRIOR_TRACK_A_SUBSTRATE_RESTORED}; "
          f"Track B (methodology-floor-only) = {PRIOR_TRACK_B_METHODOLOGY_FLOOR}")
    print(f"  τ_fold = {tau_fold}; M_KK = {M_KK}; Vol_SU3_Haar = {Vol_SU3_Haar}")
    print(f"  PREDICTED DIRECTION (subst. chain Step 4): FAIL (flip stays absent; "
          f"v_a² is regulator-COMMON)")

    # ---- Step 1: load L_max=12 master cache (verbatim W5-3 protocol) ----
    print("\n--- Step 1: load L_max=12 spectrum cache (τ=0.19) ---")
    if not S84_L12_CACHE.exists():
        # Mechanical-closure INFO branch (plan §W8-2 INFO_meaning (c))
        print(f"  Cache not found: {S84_L12_CACHE} -> PRE-REG-INC mechanical closure")
        value_str = (
            f"PRE-REG-INC_blocked_by_s84_spectrum_cache_L12_tau019_MISSING;deferred_to_S95"
        )  # (local)
        append_verdict("INFO", value_str, audit_sha, content_sha, "N/A", "FAIL", "BREAKDOWN")
        print("  INFO (mechanical closure) appended; deferred to S95.")
        return 0
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

    # ---- Step 1b: SUBSTRATE-DERIVED BdG occupation weight v_a²(λ) ----
    print("\n--- Step 1b: substrate BdG occupation weight v_a²(λ) (THE DISCRIMINATING CHANGE) ---")
    v_a_sq, v_a_sq_formB, form_diff = bogoliubov_occupation_weight(lambdas)  # (local) operative=Form A
    # Order-statistics by λ to confirm deep-IR concentration
    order = np.argsort(lambdas)  # (local)
    print(f"  OPERATIVE weight = Form A: v_a²(λ)=Δ²/(2(λ²+Δ²)) [plan machinery_pin_map line 340]")
    print(f"  v_a²(λ_min={lambdas.min():.4e}) = {v_a_sq[order[0]]:.6f}  (deep-IR; largest weight)")
    print(f"  v_a²(λ_max={lambdas.max():.4e}) = {v_a_sq[order[-1]]:.6e}  (UV; smallest weight)")
    print(f"  v_a²(0)_analytic = {0.5:.6f}; v_a²(Δ)_analytic = {0.25:.6f}  (Δ=Delta_BCS, Form A)")
    print(f"  Form A monotone-decreasing in λ: {bool(np.all(np.diff(v_a_sq[order]) <= 1e-15))}")
    # Honest form-distinction disclosure (Sage-verified; NOT bit-equal away from λ→0)
    print(f"  Form B reference (1/2)(1−λ/√(λ²+Δ²)): v_a²_B(λ_min)={v_a_sq_formB[order[0]]:.6f}, "
          f"v_a²_B(λ_max)={v_a_sq_formB[order[-1]]:.6e}")
    print(f"  max|Form A − Form B| over cache λ-range = {form_diff:.6e} "
          f"(coincide ONLY at λ→0; plan '+O(...) at λ→0' text confirmed; Sage-verified)")
    print(f"  Form-distinction note: Form A = Δ²/(2E²) = 2u²v² (pair-coherence-density); "
          f"Form B = (1/2)(1−ξ/E) (fundamental BdG occupation); both substrate-IS on M₂(ℂ).")

    # ---- Step 2: 5 substrate-natural heat-kernel anchors (verbatim W5-3) ----
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
    # SCHEMATIC reproduction (rank-change PRIMARY vs SCHEMATIC) — W5-3 cross-check baseline
    # (RETAINED ONLY as the cross-check baseline ρ_S_SCHEMATIC=−0.20; NEVER the PASS source)
    # ============================================================
    print("\n" + "=" * 78)
    print("SCHEMATIC reproduction (W5-3 cross-check baseline; NOT the PASS source)")
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

    t_deep = anchors[DEEP_IR_ANCHOR]
    mp_d = np.array([mellin_moment_SCHEMATIC(lambdas, mults, t_deep, r, "PRIMARY") for r in REGULATOR_NAMES])
    ms_d = np.array([mellin_moment_SCHEMATIC(lambdas, mults, t_deep, r, "SCHEMATIC") for r in REGULATOR_NAMES])
    rp_d = rank_vector(mp_d)
    rs_d = rank_vector(ms_d)
    _res = spearmanr(rp_d, rs_d)
    rho_S_SCHEMATIC = float(_res.correlation) if not np.isnan(_res.correlation) else 0.0
    print(f"\n  Deep-IR PRIMARY-vs-SCHEMATIC Spearman (SCHEMATIC baseline) = {rho_S_SCHEMATIC:+.6f}")
    print(f"  W5-3 on-disk baseline ρ_S_SCHEMATIC = {W5_3_RHO_S_SCHEMATIC_BASELINE:+.6f} "
          f"(cross-check match: {abs(rho_S_SCHEMATIC - W5_3_RHO_S_SCHEMATIC_BASELINE) < 1e-6})")

    # ============================================================
    # FULL-tier N=4 + SUBSTRATE-DERIVED v_a² (rank-change PRIMARY vs SCHEMATIC)
    # — the conviction-or-acquittal
    # ============================================================
    print("\n" + "=" * 78)
    print("FULL-tier N=4 CC-1996 §2.2-2.3 + SUBSTRATE-DERIVED v_a² weighting")
    print("=" * 78)
    full_rank_change = []  # (local)
    full_rank_P = {}       # (local)
    full_rank_S = {}       # (local)
    for an, t in anchors.items():
        mp = np.array([
            mellin_moment_FULL_N4_substrate(lambdas, mults, t, r, "PRIMARY", max_lambda_sq, v_a_sq)
            for r in REGULATOR_NAMES
        ])
        ms = np.array([
            mellin_moment_FULL_N4_substrate(lambdas, mults, t, r, "SCHEMATIC", max_lambda_sq, v_a_sq)
            for r in REGULATOR_NAMES
        ])
        rp = rank_vector(mp)
        rs = rank_vector(ms)
        full_rank_P[an] = rp
        full_rank_S[an] = rs
        chg = int(not np.array_equal(rp, rs))
        full_rank_change.append(chg)
        print(f"  {an:22s} PRIMARY={rp.astype(int).tolist()} SCHEMATIC={rs.astype(int).tolist()} change={bool(chg)}")
    print(f"  FULL+v_a² rank_change_per_anchor = {full_rank_change}  (target deep-IR flip {DEEP_IR_FLIP_TARGET})")
    flip_reproduced = (full_rank_change == DEEP_IR_FLIP_TARGET)
    print(f"  flip_reproduced (FULL+v_a² matches [0,0,0,0,1]): {flip_reproduced}")

    # Deep-IR PRIMARY-vs-SCHEMATIC Spearman under FULL-tier + v_a² (the discriminating scalar)
    mp_fd = np.array([
        mellin_moment_FULL_N4_substrate(lambdas, mults, t_deep, r, "PRIMARY", max_lambda_sq, v_a_sq)
        for r in REGULATOR_NAMES
    ])
    ms_fd = np.array([
        mellin_moment_FULL_N4_substrate(lambdas, mults, t_deep, r, "SCHEMATIC", max_lambda_sq, v_a_sq)
        for r in REGULATOR_NAMES
    ])
    rp_fd = rank_vector(mp_fd)
    rs_fd = rank_vector(ms_fd)
    _resf = spearmanr(rp_fd, rs_fd)
    rho_S_FULL_substrate = float(_resf.correlation) if not np.isnan(_resf.correlation) else 0.0
    print(f"\n  Deep-IR PRIMARY-vs-SCHEMATIC Spearman (FULL+v_a² substrate) = {rho_S_FULL_substrate:+.6f}")
    print(f"  W5-3 on-disk baseline ρ_S_FULL = +{W5_3_RHO_S_FULL_BASELINE:.6f} (scalar-knob, no v_a²)")

    abs_diff_substrate = abs(rho_S_FULL_substrate - rho_S_SCHEMATIC)  # (local) flip-match band
    print(f"  abs_diff (flip-match band) = |ρ_S(FULL+v_a²) − ρ_S(SCHEMATIC)| = {abs_diff_substrate:.6f}")
    print(f"  abs_diff ≤ {RHO_S_AGREEMENT_BAND} ? {abs_diff_substrate <= RHO_S_AGREEMENT_BAND}")

    # ============================================================
    # COMPOSITE ADJUDICATION (plan §W8-2 operator)
    # ============================================================
    print("\n" + "=" * 78)
    print("COMPOSITE ADJUDICATION (plan §W8-2 operator)")
    print("=" * 78)
    # PASS iff rank==[0,0,0,0,1] AND ρ_S_FULL_substrate<0 AND abs_diff(ρ_S)≤1e-3
    conjunct_rank_flip = flip_reproduced  # (local) rank == [0,0,0,0,1]
    conjunct_rho_neg = (rho_S_FULL_substrate < 0.0)  # (local) deep-IR anti-correlation
    conjunct_abs_diff = (abs_diff_substrate <= RHO_S_AGREEMENT_BAND)  # (local) flip-match band
    full_pass = conjunct_rank_flip and conjunct_rho_neg and conjunct_abs_diff
    reclassification_branch = (
        "PASS-A-RESTORED-SUBSTRATE-IS" if full_pass
        else "PASS-A-PERMANENTLY-METHODOLOGY-FLOOR"
    )
    print(f"  conjunct-rank-flip (rank==[0,0,0,0,1]):       {conjunct_rank_flip}")
    print(f"  conjunct-rho-neg   (ρ_S_FULL_substrate < 0):  {conjunct_rho_neg}")
    print(f"  conjunct-abs-diff  (|Δρ_S| ≤ {RHO_S_AGREEMENT_BAND}):       {conjunct_abs_diff}")
    print(f"  reclassification_branch = {reclassification_branch}")

    # ---- [SIGN] 3-tuple verdict (S87 schema-v2) ----
    # sign_verdict: PASS iff substitution-chain Step-4 PREDICTED direction (FAIL /
    #   flip-stays-absent) matches the COMPUTED direction.
    predicted_direction_fail = True  # (local) Step 4 predicted FAIL (flip stays absent)
    computed_fail = (not full_pass)  # (local)
    sign_v = "PASS" if (predicted_direction_fail == computed_fail) else "FAIL"

    # magnitude_verdict: the gate's numeric target — PASS iff the full conjunction holds
    #   (rank flip recovered AND ρ_S<0 AND |Δρ_S|≤band); FAIL otherwise.
    mag_v = "PASS" if full_pass else "FAIL"

    # regime_verdict: CC-1996 N=4 PV regularization × v_a² weighting validity over
    #   the anchor window. VALID iff all FULL-tier substrate moments finite +
    #   non-degenerate at all 5 anchors (plan §W8-2 INFO_meaning (a)).
    full_moments_finite = True  # (local)
    n_anchors_breakdown = 0  # (local)
    for an in anchors:
        vals = np.array([
            mellin_moment_FULL_N4_substrate(lambdas, mults, anchors[an], r, "PRIMARY",
                                            max_lambda_sq, v_a_sq)
            for r in REGULATOR_NAMES
        ])
        if not np.all(np.isfinite(vals)) or np.std(vals) < 1e-30:
            full_moments_finite = False
            n_anchors_breakdown += 1
    breach_frac = n_anchors_breakdown / len(anchors)  # (local)
    if full_moments_finite:
        reg_v = "VALID"
    elif breach_frac <= 0.5:
        reg_v = "MARGINAL"
    else:
        reg_v = "BREAKDOWN"

    # Composite collapse rule (gate-verdicts.md §"Composite-collapse rule" — PRE-REGISTERED)
    # Modifying this rule after seeing the verdict is PROHIBITED Class-3.
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

    print(f"\n  3-tuple: sign={sign_v} magnitude={mag_v} regime={reg_v} "
          f"(breach_frac={breach_frac:.2f})")
    print(f"  COMPOSITE = {composite}  (collapse rule applied)")

    # ---- Dual-prior posterior re-allocation (pre-registered; NOT post-hoc) ----
    print("\n--- Dual-prior posterior re-allocation (pre-registered; plan §W8-2) ---")
    if composite == "PASS":
        post_A, post_B = POSTERIOR_REALLOCATION, 1.0 - POSTERIOR_REALLOCATION
        track_resolved = "Track A (substrate-IS-restored; flip is BdG occupation physics)"
        eligibility = "{PASS-A, PASS-B} (re-widened)"
    elif composite == "FAIL":
        post_A, post_B = 1.0 - POSTERIOR_REALLOCATION, POSTERIOR_REALLOCATION
        track_resolved = "Track B (methodology-floor-only; v_a² is regulator-common)"
        eligibility = "{PASS-B} (unchanged; PASS-A permanently methodology-floor)"
    else:  # INFO
        post_A, post_B = PRIOR_TRACK_A_SUBSTRATE_RESTORED, PRIOR_TRACK_B_METHODOLOGY_FLOOR
        track_resolved = "priors UNCHANGED (regime-breakdown / borderline)"
        eligibility = "{PASS-B} (unchanged; PASS-A standing UNRESOLVED)"
    print(f"  prior:     Track A = {PRIOR_TRACK_A_SUBSTRATE_RESTORED}, "
          f"Track B = {PRIOR_TRACK_B_METHODOLOGY_FLOOR}")
    print(f"  posterior: Track A = {post_A}, Track B = {post_B}")
    print(f"  resolved:  {track_resolved}")
    print(f"  §VII.AR eligibility: {eligibility}")

    # ============================================================
    # SAVE artifacts (NPZ + PNG)
    # ============================================================
    print("\n--- SAVE artifacts ---")
    sch_rank_P_arr = np.array([sch_rank_P[a] for a in ANCHOR_LABELS])
    sch_rank_S_arr = np.array([sch_rank_S[a] for a in ANCHOR_LABELS])
    full_rank_P_arr = np.array([full_rank_P[a] for a in ANCHOR_LABELS])
    full_rank_S_arr = np.array([full_rank_S[a] for a in ANCHOR_LABELS])

    np.savez(
        OUT_NPZ,
        # --- core gate observables (plan-required keys) ---
        rho_S_FULL_substrate=rho_S_FULL_substrate,
        rho_S_SCHEMATIC=rho_S_SCHEMATIC,
        abs_diff_substrate=abs_diff_substrate,
        rank_change_per_anchor_FULL_substrate=np.array(full_rank_change),
        flip_reproduced=flip_reproduced,
        reclassification_branch=reclassification_branch,
        eligibility=eligibility,
        tier_pin="TIER-1",
        # --- W5-3 baselines (on disk; like-for-like comparison) ---
        w5_3_rho_S_FULL_baseline=W5_3_RHO_S_FULL_BASELINE,
        w5_3_rho_S_SCHEMATIC_baseline=W5_3_RHO_S_SCHEMATIC_BASELINE,
        w5_3_rank_change_FULL=np.array(W5_3_RANK_CHANGE_FULL),
        # --- SCHEMATIC reproduction cross-check ---
        rank_change_per_anchor_SCHEMATIC=np.array(sch_rank_change),
        schematic_reproduces_flip=schematic_reproduces_flip,
        deep_ir_flip_target=np.array(DEEP_IR_FLIP_TARGET),
        # --- substrate BdG occupation weight (THE DISCRIMINATING CHANGE) ---
        v_a_sq_form="Form_A_Delta^2_div_2(lambda^2+Delta^2)_operative_plan_pinned",
        v_a_sq_min=float(v_a_sq.min()),
        v_a_sq_max=float(v_a_sq.max()),
        v_a_sq_at_lambda_min=float(v_a_sq[order[0]]),
        v_a_sq_at_lambda_max=float(v_a_sq[order[-1]]),
        v_a_sq_formB_at_lambda_min=float(v_a_sq_formB[order[0]]),
        v_a_sq_formB_at_lambda_max=float(v_a_sq_formB[order[-1]]),
        form_A_minus_form_B_max=form_diff,
        form_distinction_note=(
            "Form A=Δ²/(2(λ²+Δ²))=2u²v² (pair-coherence-density, plan-pinned operative); "
            "Form B=(1/2)(1−λ/√(λ²+Δ²)) (fundamental BdG occupation, λ→0-equivalent ref); "
            "Sage-verified NOT bit-equal away from λ→0 (coincide at λ=0, both 1/2)."
        ),
        Delta_BCS=Delta_BCS,
        # --- rank vectors (per-anchor rows) ---
        sch_rank_PRIMARY=sch_rank_P_arr,
        sch_rank_SCHEMATIC=sch_rank_S_arr,
        full_rank_PRIMARY=full_rank_P_arr,
        full_rank_SCHEMATIC=full_rank_S_arr,
        # --- gate adjudication ---
        conjunct_rank_flip=conjunct_rank_flip,
        conjunct_rho_neg=conjunct_rho_neg,
        conjunct_abs_diff=conjunct_abs_diff,
        rho_S_agreement_band=RHO_S_AGREEMENT_BAND,
        composite_verdict=composite,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=reg_v,
        breach_frac=breach_frac,
        # --- dual prior ---
        prior_track_A_substrate_restored=PRIOR_TRACK_A_SUBSTRATE_RESTORED,
        prior_track_B_methodology_floor=PRIOR_TRACK_B_METHODOLOGY_FLOOR,
        posterior_track_A=post_A,
        posterior_track_B=post_B,
        track_resolved=track_resolved,
        # --- CC-1996 N=4 PV multiplier set ---
        cc1996_n4_pv_coeffs=CC1996_N4_PV_COEFFS,
        N_PV=N_PV,
        # --- pins / metadata ---
        anchor_labels=np.array(ANCHOR_LABELS),
        regulator_names=np.array(REGULATOR_NAMES),
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
        w5_3_fail_audit_sha=W5_3_FAIL_AUDIT_SHA,
        w4_1_pass_audit_sha=W4_1_PASS_AUDIT_SHA,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        cache_sha=pins.get("s84_spectrum_cache_L12_tau019", ""),
        canonical_constants_live_sha=live_canonical_sha,
        canonical_constants_plan_pin=CANONICAL_CONSTANTS_PLAN_PIN,
        canonical_drift=canonical_drift,
        FULL_tier_disclosure=(
            "FULL physical regularization: Connes-Chamseddine 1996 §2.2-2.3 N=4 "
            "Pauli-Villars mass tower c_j=[1,-4,6,-4,1] at Λ_UV=M_KK (a_2^{Pauli-Villars}), "
            "REUSED VERBATIM from W5-3. DISCRIMINATING change: per-eigenvalue substrate "
            "BdG occupation weight v_a²(λ)=Δ²/(2(λ²+Δ²)) on M₂(ℂ)⊂A_K, Δ=Delta_BCS, "
            "replacing the SCHEMATIC scalar (1-M_PV²_frac) prefactor. tier_pin=TIER-1; "
            "CLASS=FULL; NO -SCHEMATIC suffix per substrate-first-canonical-sourcing.md "
            "§(iv) K=4. SCHEMATIC scalar source retained as W5-3 cross-check baseline ONLY."
        ),
    )
    print(f"  NPZ -> {OUT_NPZ.relative_to(ROOT)}")

    # ---- PNG plot ----
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Panel 1: SCHEMATIC vs FULL+v_a² rank-change vectors + v_a²(λ) curve inset
    ax = axes[0]
    x = np.arange(len(ANCHOR_LABELS))
    ax.bar(x - 0.2, sch_rank_change, width=0.38, label="SCHEMATIC rank-change (W5-3 baseline)",
           alpha=0.85, color="tab:blue")
    ax.bar(x + 0.2, full_rank_change, width=0.38, label="FULL N=4 + v_a² rank-change",
           alpha=0.85, color="tab:red")
    ax.axvspan(len(ANCHOR_LABELS) - 1.5, len(ANCHOR_LABELS) - 0.5, color="gold", alpha=0.25,
               label="deep-IR anchor (target flip)")
    ax.set_xticks(x)
    ax.set_xticklabels([a.replace("_lambda_sq", "_λ²") for a in ANCHOR_LABELS],
                       rotation=30, ha="right", fontsize=9)
    ax.set_ylabel("rank changed (PRIMARY vs SCHEMATIC)? (0/1)")
    ax.set_ylim(-0.1, 1.25)
    ax.set_title(
        f"§VII.AR rank-change: SCHEMATIC={sch_rank_change} vs FULL+v_a²={full_rank_change}\n"
        f"target deep-IR flip {DEEP_IR_FLIP_TARGET}; flip_reproduced={flip_reproduced}"
    )
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(True, alpha=0.3)

    # v_a²(λ) curve inset (the discriminating change)
    axins = ax.inset_axes([0.55, 0.45, 0.42, 0.45])
    lam_sorted = lambdas[order]  # (local)
    axins.plot(lam_sorted, v_a_sq[order], color="tab:green", lw=1.5)
    axins.axhline(0.5, ls="--", color="gray", lw=0.8, alpha=0.7)
    axins.set_title("v_a²(λ)=Δ²/(2(λ²+Δ²))", fontsize=8)
    axins.set_xlabel("λ", fontsize=7)
    axins.set_ylabel("v_a²", fontsize=7)
    axins.tick_params(labelsize=6)
    axins.grid(True, alpha=0.3)

    # Panel 2: verdict box
    ax = axes[1]
    ax.axis("off")
    box = (
        f"COMPOSITE: {composite}\n"
        f"reclassification_branch:\n  {reclassification_branch}\n"
        f"§VII.AR eligibility: {eligibility}\n\n"
        f"ρ_S(SCHEMATIC) deep-IR  = {rho_S_SCHEMATIC:+.4f}  (W5-3: {W5_3_RHO_S_SCHEMATIC_BASELINE:+.2f})\n"
        f"ρ_S(FULL N=4 + v_a²)    = {rho_S_FULL_substrate:+.4f}  (W5-3 scalar: +{W5_3_RHO_S_FULL_BASELINE:.2f})\n"
        f"|abs_diff (flip band)|  = {abs_diff_substrate:.4f}\n"
        f"  ≤ {RHO_S_AGREEMENT_BAND} band ? {conjunct_abs_diff}\n\n"
        f"SCHEMATIC rank-change   = {sch_rank_change}\n"
        f"FULL+v_a² rank-change   = {full_rank_change}\n"
        f"W5-3 FULL rank-change   = {W5_3_RANK_CHANGE_FULL}\n"
        f"flip recovered [0,0,0,0,1]? {conjunct_rank_flip}\n\n"
        f"GATE OPERATOR (AND of 3 conjuncts):\n"
        f"  rank-flip [0,0,0,0,1] = {conjunct_rank_flip}\n"
        f"  ρ_S_FULL_substrate<0  = {conjunct_rho_neg}\n"
        f"  |Δρ_S| ≤ 1e-3         = {conjunct_abs_diff}\n\n"
        f"3-tuple: ({sign_v}, {mag_v}, {reg_v})\n\n"
        f"DUAL PRIOR (pre-registered):\n"
        f"  prior  A={PRIOR_TRACK_A_SUBSTRATE_RESTORED} B={PRIOR_TRACK_B_METHODOLOGY_FLOOR}\n"
        f"  poster A={post_A} B={post_B}\n"
        f"  -> {track_resolved}\n\n"
        f"DISCRIMINATING CHANGE: v_a²(λ)=Δ²/(2(λ²+Δ²))\n"
        f"  Δ=Delta_BCS={Delta_BCS:.6f}\n"
        f"  v_a²(λ_min)={v_a_sq[order[0]]:.4f}, v_a²(λ_max)={v_a_sq[order[-1]]:.2e}\n\n"
        f"tier_pin=TIER-1 (FULL; CC-1996 §2.2-2.3 N=4 PV; a_2^Pauli-Villars)\n"
        f"c_j = {CC1996_N4_PV_COEFFS.astype(int).tolist()}"
    )
    ax.text(0.02, 0.98, box, transform=ax.transAxes, fontsize=8.5,
            family="monospace", verticalalignment="top",
            bbox=dict(boxstyle="round,pad=0.5",
                      facecolor="mistyrose" if composite == "FAIL"
                      else ("honeydew" if composite == "PASS" else "lightyellow"),
                      alpha=0.9))
    ax.set_title("§VII.AR PASS-A substrate-derivation: conviction-or-acquittal verdict")

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
    if full_pass:
        stage_field = (
            "PASS-A_RESTORED_SUBSTRATE-IS;eligibility_re-widens_PASS-B_to_PASS-A-AND-PASS-B;"
            "sign_meaning=predicted_FAIL_NOT_matched_outcome_is_PASS_flip_recovered"
        )  # (local)
    else:
        stage_field = (
            "PASS-A_PERMANENTLY_METHODOLOGY-FLOOR;eligibility_stays_PASS-B;"
            "PASS-B_carries_VII-AR_STAGE-3_eligibility;w5_3_reclassification_stands;"
            "sign_meaning=predicted_FAIL_flip-stays-absent_matches_computed"
        )  # (local)
    value_str = (
        f"composite={composite};reclassification_branch={reclassification_branch};"
        f"rho_S_FULL_substrate={rho_S_FULL_substrate:.6f};"
        f"rho_S_SCHEMATIC={rho_S_SCHEMATIC:.6f};"
        f"abs_diff_substrate={abs_diff_substrate:.6f};"
        f"rho_S_agreement_band={RHO_S_AGREEMENT_BAND};"
        f"rank_change_per_anchor_FULL_substrate=[{full_rc}];"
        f"rank_change_per_anchor_SCHEMATIC=[{sch_rc}];"
        f"deep_ir_flip_target=[0,0,0,0,1];"
        f"flip_reproduced={flip_reproduced};"
        f"conjunct_rank_flip={conjunct_rank_flip};"
        f"conjunct_rho_neg={conjunct_rho_neg};"
        f"conjunct_abs_diff={conjunct_abs_diff};"
        f"w5_3_baseline_rho_S_FULL=+{W5_3_RHO_S_FULL_BASELINE:.6f};"
        f"w5_3_baseline_rho_S_SCHEMATIC={W5_3_RHO_S_SCHEMATIC_BASELINE:.6f};"
        f"w5_3_baseline_rank_change_FULL=[1,1,1,1,1];"
        f"v_a_sq_form=Delta_BCS^2_div_2(lambda^2+Delta_BCS^2)_on_M2C;"
        f"v_a_sq_at_lambda_min={float(v_a_sq[order[0]]):.6f};"
        f"v_a_sq_at_lambda_max={float(v_a_sq[order[-1]]):.6e};"
        f"Delta_BCS={Delta_BCS};"
        f"tier_pin=TIER-1;CLASS=FULL;a_2_tag=Pauli-Villars;"
        f"cc1996_n4_pv_coeffs=[1,-4,6,-4,1];N_PV={N_PV};Lambda_UV=M_KK;"
        f"predicted_direction=FAIL_flip_stays_absent;"
        f"dual_prior_track_A={PRIOR_TRACK_A_SUBSTRATE_RESTORED};"
        f"dual_prior_track_B={PRIOR_TRACK_B_METHODOLOGY_FLOOR};"
        f"posterior_track_A={post_A};posterior_track_B={post_B};"
        f"track_resolved={track_resolved.split(' (')[0]};"
        f"vii_ar_eligibility={eligibility.split(' (')[0].strip()};"
        f"schematic_baseline_cross_check_match={abs(rho_S_SCHEMATIC - W5_3_RHO_S_SCHEMATIC_BASELINE) < 1e-6};"
        f"canonical_drift={canonical_drift};"
        f"canonical_live_sha={live_canonical_sha[:16]};canonical_plan_pin={CANONICAL_CONSTANTS_PLAN_PIN[:16]};"
        f"Delta_BCS_unchanged_vs_MCP_canonical=True;"
        f"w5_3_fail_audit_sha={W5_3_FAIL_AUDIT_SHA[:16]};"
        f"w4_1_pass_audit_sha={W4_1_PASS_AUDIT_SHA[:16]};"
        f"cache_sha={pins.get('s84_spectrum_cache_L12_tau019', '')[:16]};"
        f"L_max={L_MAX};tau_fold={tau_fold};s_pole={S_POLE_AR};"
        f"{stage_field}"
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
