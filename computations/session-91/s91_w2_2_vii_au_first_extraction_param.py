#!/usr/bin/env python3
"""
S91 W2-2 — S91-VII-AU-FIRST-EXTRACTION-PARAMETERIZATION (T1.5)
==============================================================================

Gate: S91-VII-AU-FIRST-EXTRACTION-PARAMETERIZATION-W8-CF-72 ([VERIFY] + [CHAIN])

Pre-registered threshold (plan §W2-2 (9) 6-row table):
  PASS-a:    sub-option (a) matches predicted formula within 1e-9 rel AND
             (b)/(c) don't (or are inadmissible).
  PASS-b:    sub-option (b) canonical (PV substrate-natural at Λ_UV = M_KK;
             FULL physical).
  PASS-c:    sub-option (c) canonical (L_k=1 atlas-row pre-normalization
             required for Level-1 cohomology-class binding).
  PASS-multi: two or three sub-options indistinguishable within 1e-9 ⇒
             multi-pin atlas.
  INFO:      cross-sub-option spread ∈ (1e-9, 1e-6); defers canonicalization.
  FAIL:      spread > 1e-6 OR any M_3 non-finite OR truncation-inconsistent.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-90/s90_w8_spectrum_cache_L12_tau038.npz
    (L_max=12 master spectrum cache; sector-by-sector Peter-Weyl
     decomposition with (p,q) keys)
  - computations/_shared/_cm_1995_residue_formula.py
    (PRIMARY full physical evaluator; LEVEL pin = FULL per
     substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY)
  - computations/_shared/canonical_constants.py (feeds audit_sha256)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<'a'|'b'|'c'|'multi'>,
   scheme=Mellin-cone-residue-at-substrate-distance-1-pole-s3,
   convention=op-proj-first-extraction-three-param-sub-option-discriminator,
   L_max=12)

Classification: GEOMETRIC.

METHODOLOGY
-----------
The §VII.AU first-extraction Mellin-cone residue at substrate-distance-1
pole s=3 is computed under three structurally distinct EVALUATION
CONVENTIONS of the same substrate-IS canonical:

  (a) ζ-regularization (substrate-natural direct evaluation):
        M_3^(a) = slope_A_canonical · K_a2(τ_fold) / (2π²)
        where K_a2(τ_fold) = Σ_{(p,q)≠(0,0)} dim(p,q) · |λ(p,q,τ_fold)|^{-6}
        is the substrate a_2 Seeley-DeWitt trace at pole s=3 (closed-form
        algebraic identity on the finite spectral triple per CM-1995 §III.4).

  (b) Pauli-Villars subtraction at Λ_UV = M_KK:
        M_3^(b) = M_3^(a) − (1/(2π²)) · K_a2_PV(τ_fold; Λ_UV = M_KK)
        where K_a2_PV is the high-|λ| tail with cutoff |λ| > Λ_UV / M_KK
        in dimensionless cache units. At finite L_max=12 the substrate
        spectrum is bounded by |λ|_max ≪ Λ_UV/M_KK ≈ 1 ⇒ K_a2_PV = 0
        (substrate-natural PV subtraction is structurally vacuous at
        finite L_max; the substrate-IS PV regulator binds at the
        infinite-L_max continuum limit, NOT at the finite-cache
        truncation).

  (c) Locked-norm L_k=1 atlas-row pre-normalization:
        M_3^(c) = M_3^(a) / L_k1_atlas_norm
        where L_k1_atlas_norm = K_a2_partial(p+q=1) / 6 is the L_k=1
        atlas-row layer normalization per
        substrate-first-canonical-sourcing.md §(ii.A) intra-algebra-INVARIANT
        layer orthogonality (atlas-row vs cache-moment evaluation
        convention of the same substrate-IS canonical).

The three sub-options are NOT three different external regulators applied
to the substrate — they are three evaluation conventions of the SAME
substrate-IS Mellin-cone residue at pole s=3 on the operator-projection
algebra image of A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- LEVEL pin = FULL (consumes `_cm_1995_residue_formula.py` PRIMARY)
- MACHINERY-SCOPE pin = CACHE-PROJECTION (consumes L_max=12 cache)
- Binding axis pin = substrate-natural-binding (substrate-IS direct
  evaluation; not canonical-import binding)
- Runtime canonical resolution for slope_A_canonical per
  substrate-first-canonical-sourcing.md §(ii.B) plan-text-drift correction
  orchestrator-convention (fallback: slope_A_FW_Conv_A_AT_TAU_FOLD).
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Schema-v2 3-tuple companion row (substitution chain Step 4
  pre-registers M_3^(a) > 0 directional prediction).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
import canonical_constants as cc  # noqa: E402

# FULL physical evaluator — LEVEL pin = FULL per substrate-first-canonical-sourcing.md §(iv)
from _cm_1995_residue_formula import jensen_irrep_table  # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")  # non-interactive backend
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S91"  # (local)
GATE_ID = "S91-VII-AU-FIRST-EXTRACTION-PARAMETERIZATION"  # (local)
SCHEME = "Mellin-cone-residue-at-substrate-distance-1-pole-s3"  # (local)
CONVENTION = "op-proj-first-extraction-three-param-sub-option-discriminator"  # (local)
L_MAX_OPERATIONAL = 12  # (local)
L_MAX_CROSS_CHECK = 10  # (local)

# Pre-registered tolerances (per plan §W2-2 (7) machinery pin table)
PASS_BAND = 1e-9  # (local) within-sub-option canonical-formula match
INFO_BAND = 1e-6  # (local) cross-sub-option spread upper bound for INFO
REL_TOL_TRUNCATION = 5e-2  # (local) L_max=10 vs 12 drift threshold for VALID regime

# LEVEL pin (substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY)
LEVEL_PIN = "FULL"  # (local)  consumes _cm_1995_residue_formula.py PRIMARY
MACHINERY_SCOPE_PIN = "CACHE-PROJECTION"  # (local)  consumes L_max=12 cache
BINDING_AXIS_PIN = "substrate-natural-binding"  # (local)

# Output destinations
OUT_NPZ = SESSION_DIR / "s91_w2_2_vii_au_first_extraction_param.npz"
OUT_PNG = SESSION_DIR / "s91_w2_2_vii_au_first_extraction_param.png"
VERDICT_TXT = SESSION_DIR / "s91_gate_verdicts.txt"

CACHE_PATH = COMPUTATIONS_DIR / "session-90" / "s90_w8_spectrum_cache_L12_tau038.npz"
RESIDUE_HELPER_PATH = SHARED_DIR / "_cm_1995_residue_formula.py"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [
    CACHE_PATH,
    RESIDUE_HELPER_PATH,
    CANONICAL_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    """Return (audit_sha256, content_sha256) per S84+ dual-SHA schema."""
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Substrate canonical resolution (slope_A_canonical runtime)
# ---------------------------------------------------------------------------

def resolve_slope_A_canonical():
    """Runtime canonical resolution for slope_A_canonical per
    substrate-first-canonical-sourcing.md §(ii.B) plan-text-drift correction.

    Priority order:
      1. canonical_constants.slope_A_canonical (TBD at S91 W2 dispatch;
         will be present after T0.7 PASS promotes the pin)
      2. canonical_constants.slope_A_FW_Conv_A_AT_TAU_FOLD (Sage-CM-1995
         §III.4 evaluation at τ_fold = 0.190; GEOMETRIC reading
         per Reading A canonical at S89 CF V.3)
      3. plan-pinned fallback value

    Returns (slope_A_value, source_tag).
    """
    if hasattr(cc, "slope_A_canonical"):
        # T0.7 has promoted the canonical pin
        return float(cc.slope_A_canonical), "canonical_constants.slope_A_canonical"
    if hasattr(cc, "slope_A_FW_Conv_A_AT_TAU_FOLD"):
        # Substrate-natural fallback: Conv-A geometric reading at τ_fold = 0.190
        return (
            float(cc.slope_A_FW_Conv_A_AT_TAU_FOLD),
            "canonical_constants.slope_A_FW_Conv_A_AT_TAU_FOLD",
        )
    # Plan-pinned fallback per §W2-2 substitution chain
    return 10.0, "plan-pinned-fallback-substrate-distance-1-base"


# ---------------------------------------------------------------------------
# Section 6 — K_a2(τ_fold) via Mellin-cone residue at pole s=3
# ---------------------------------------------------------------------------

def compute_K_a2(L_max: int, tau: float) -> tuple[float, dict]:
    """K_a2(τ) substrate a_2 Seeley-DeWitt trace at Mellin-cone pole s=3
    on the spectral triple (A_K, H_K, D_K).

    Per CM-1995 §III.4 dimension-spectrum analysis at finite L_max,
    ζ_a2_φ(z) = Σ_{(p,q)≠(0,0)} dim(p,q) · |λ(p,q,τ)|^{-6-2z}
    is holomorphic in z; "residue at simple pole z=0" of the dimension-
    spectrum reduces algebraically to the value at z=0:

      K_a2(τ) = ζ_a2_φ(0) = Σ_{(p,q)≠(0,0)} dim(p,q) · |λ(p,q,τ)|^{-6}    (s=3 weight)

    This is bit-precision identical to the s=4 pole evaluator pattern
    in `_cm_1995_residue_formula.py` (with ρ^{0} weight at pole s=3 vs
    ρ^{3} weight at pole s=4 for the a_4 GV-Heitsch cocycle).

    Returns (K_a2_value, per_level_breakdown).
    """
    dims, rhos, lams = jensen_irrep_table(L_max, tau)
    # Pole s=3 ⇒ |D|^{-2s} weight is |λ|^{-6} on the finite spectrum
    inv6 = 1.0 / (lams ** 6)  # (local) Mellin pole-s=3 weight
    K_a2 = float(np.sum(dims * inv6))  # (local)

    # Per-level breakdown for L_k=1 atlas-row pre-normalization
    breakdown = {}  # (local)
    for level in range(int(rhos.max()) + 1):
        mask = (rhos == level)  # (local)
        if not mask.any():
            continue
        partial = float(np.sum(dims[mask] * inv6[mask]))  # (local)
        breakdown[int(level)] = partial

    return K_a2, breakdown


def compute_K_a2_PV(L_max: int, tau: float, lambda_UV_cache_units: float) -> float:
    """Pauli-Villars high-|λ| tail subtraction (substrate-natural at Λ_UV = M_KK).

    K_a2_PV(τ; Λ_UV) = Σ_{(p,q)≠(0,0), |λ|>Λ_UV} dim(p,q) · |λ(p,q,τ)|^{-6}

    At finite L_max=12, the substrate spectrum is bounded:
      max |λ(p,q,τ_fold)| = √C_2(12,0) · exp(-0.19 · 12) ≈ √60 · 0.103 ≈ 0.80
    in dimensionless cache units (the substrate's intrinsic eigenvalue
    scale, where M_KK is the underlying GeV-scale). The Pauli-Villars
    cutoff at Λ_UV = M_KK corresponds to lambda_UV_cache_units ≈ 1 in
    this dimensionless reduction (Mellin-cone evaluation IS scale-
    invariant; the substrate IS the dimensionless spectral triple).

    For |λ|_max < lambda_UV_cache_units, the PV tail is empty ⇒
    K_a2_PV = 0 structurally. This is the substrate-natural PV reading:
    the substrate spectrum at finite L_max does NOT reach the UV cutoff,
    so the PV subtraction is vacuous at the finite-cache truncation.
    """
    dims, rhos, lams = jensen_irrep_table(L_max, tau)
    inv6 = 1.0 / (lams ** 6)  # (local)
    pv_mask = (lams > lambda_UV_cache_units)  # (local) high-|λ| tail
    K_a2_PV = float(np.sum(dims[pv_mask] * inv6[pv_mask]))  # (local)
    return K_a2_PV


def compute_L_k1_atlas_norm(K_a2_breakdown: dict) -> tuple[float, dict]:
    """Locked-norm L_k=1 atlas-row pre-normalization
    per substrate-first-canonical-sourcing.md §(ii.A) intra-algebra-INVARIANT
    layer orthogonality (atlas-row vs cache-moment).

    The L_k=1 atlas-row corresponds to the k=1 Peter-Weyl level
    (p+q=1), comprising sectors (1,0) and (0,1) with total dim 3+3=6.
    The locked-norm convention fixes the L_k=1 contribution to the
    sector-aggregated Mellin trace at unit reference: dividing K_a2
    by the k=1 partial sum normalizes the atlas-row layer to 1.

    Returns (L_k1_atlas_norm, atlas_diagnostics).
    """
    K_a2_k1 = K_a2_breakdown.get(1, 0.0)  # (local) k=1 partial sum
    # L_k=1 atlas-row pre-norm: per-dim normalization at k=1
    # (locked norm references the unit-dim contribution at the
    # substrate's atlas-row layer first Peter-Weyl level)
    k1_dim_total = 6  # (local) dim(1,0) + dim(0,1) = 3 + 3
    L_k1_atlas_norm = K_a2_k1 / k1_dim_total  # (local) per-dim atlas reference
    diagnostics = {
        "k1_partial_sum": K_a2_k1,
        "k1_dim_total": k1_dim_total,
        "L_k1_atlas_norm": L_k1_atlas_norm,
    }
    return L_k1_atlas_norm, diagnostics


# ---------------------------------------------------------------------------
# Section 7 — Compute three sub-options
# ---------------------------------------------------------------------------

def compute_three_sub_options(L_max: int, tau: float):
    """Evaluate M_3^(a), M_3^(b), M_3^(c) per the substitution chain Step 2.

    Returns dict with M_3_a, M_3_b, M_3_c, K_a2, K_a2_PV, L_k1_atlas_norm,
    slope_A_canonical_pin, slope_A_source.
    """
    # K_a2 substrate a_2 trace at Mellin pole s=3
    K_a2, K_a2_breakdown = compute_K_a2(L_max, tau)

    # Pauli-Villars subtraction with Λ_UV = M_KK substrate-natural cutoff
    # (dimensionless ratio in cache units; M_KK is the underlying GeV scale).
    # For the dimensionless substrate spectrum at finite L_max, |λ|_max < 1
    # in cache units; the substrate-natural PV cutoff is the substrate-IS
    # spectral ceiling. Pin lambda_UV_cache_units = 1.0 per the substrate's
    # intrinsic dimensionless normalization (M_KK pin is at the continuum
    # limit, not the finite-cache truncation).
    LAMBDA_UV_CACHE_UNITS = 1.0  # (local)
    K_a2_PV = compute_K_a2_PV(L_max, tau, LAMBDA_UV_CACHE_UNITS)

    # L_k=1 atlas-row pre-normalization
    L_k1_atlas_norm, L_k1_diagnostics = compute_L_k1_atlas_norm(K_a2_breakdown)

    # slope_A_canonical runtime resolution
    slope_A_canonical, slope_A_source = resolve_slope_A_canonical()

    # Substitution chain Step 2 — Mellin pole s=3 residue weight
    INV_TWO_PI_SQ = 1.0 / (2.0 * np.pi * np.pi)  # (local) Mellin pole s=3 weight

    # Sub-option (a): direct ζ-regularization
    M_3_a = slope_A_canonical * INV_TWO_PI_SQ * K_a2  # (local)

    # Sub-option (b): Pauli-Villars subtraction at Λ_UV = M_KK
    M_3_b = M_3_a - INV_TWO_PI_SQ * K_a2_PV  # (local)

    # Sub-option (c): L_k=1 atlas-row pre-normalization
    if L_k1_atlas_norm == 0.0:
        M_3_c = float("nan")  # (local) atlas-norm singular
    else:
        M_3_c = M_3_a / L_k1_atlas_norm  # (local)

    return {
        "M_3_a": M_3_a,
        "M_3_b": M_3_b,
        "M_3_c": M_3_c,
        "K_a2": K_a2,
        "K_a2_PV": K_a2_PV,
        "K_a2_breakdown": K_a2_breakdown,
        "L_k1_atlas_norm": L_k1_atlas_norm,
        "L_k1_diagnostics": L_k1_diagnostics,
        "slope_A_canonical_pin": slope_A_canonical,
        "slope_A_source": slope_A_source,
        "lambda_UV_cache_units": LAMBDA_UV_CACHE_UNITS,
        "inv_two_pi_sq": INV_TWO_PI_SQ,
    }


# ---------------------------------------------------------------------------
# Section 8 — Gate evaluation
# ---------------------------------------------------------------------------

def evaluate_gate(L12_results: dict, L10_results: dict):
    """Apply plan §W2-2 (9) 6-row threshold table.

    Returns (composite_verdict, value, sign_verdict, magnitude_verdict,
              regime_verdict, diagnostics).
    """
    M_3_a = L12_results["M_3_a"]  # (local)
    M_3_b = L12_results["M_3_b"]  # (local)
    M_3_c = L12_results["M_3_c"]  # (local)

    diagnostics = {}  # (local)

    # FAIL condition 1: any M_3 non-finite
    finite_a = np.isfinite(M_3_a)  # (local)
    finite_b = np.isfinite(M_3_b)  # (local)
    finite_c = np.isfinite(M_3_c)  # (local)
    diagnostics["finite_a"] = bool(finite_a)
    diagnostics["finite_b"] = bool(finite_b)
    diagnostics["finite_c"] = bool(finite_c)

    if not (finite_a and finite_b and finite_c):
        return ("FAIL", "non-finite", "FAIL", "FAIL", "BREAKDOWN", diagnostics)

    # Cross-sub-option spread
    M_3_values = np.array([M_3_a, M_3_b, M_3_c])  # (local)
    spread = float(M_3_values.max() - M_3_values.min())  # (local)
    rel_spread = spread / max(abs(M_3_values).max(), 1e-30)  # (local)
    diagnostics["spread"] = spread
    diagnostics["rel_spread"] = rel_spread

    # Pairwise cross-sub-option residuals (always populated for diagnostics)
    pairwise_a_b = abs(M_3_a - M_3_b) / max(abs(M_3_a), 1e-30)  # (local)
    pairwise_a_c = abs(M_3_a - M_3_c) / max(abs(M_3_a), 1e-30)  # (local)
    pairwise_b_c = abs(M_3_b - M_3_c) / max(abs(M_3_b), 1e-30)  # (local)
    diagnostics["pairwise_a_b"] = pairwise_a_b
    diagnostics["pairwise_a_c"] = pairwise_a_c
    diagnostics["pairwise_b_c"] = pairwise_b_c

    a_b_indistinguishable = (pairwise_a_b < PASS_BAND)  # (local)
    a_c_indistinguishable = (pairwise_a_c < PASS_BAND)  # (local)
    b_c_indistinguishable = (pairwise_b_c < PASS_BAND)  # (local)
    diagnostics["a_b_indistinguishable"] = bool(a_b_indistinguishable)
    diagnostics["a_c_indistinguishable"] = bool(a_c_indistinguishable)
    diagnostics["b_c_indistinguishable"] = bool(b_c_indistinguishable)
    n_indistinguishable = sum([
        a_b_indistinguishable,
        a_c_indistinguishable,
        b_c_indistinguishable,
    ])  # (local)
    diagnostics["n_indistinguishable_pairs"] = n_indistinguishable

    # Sign verdict — substitution chain Step 4: M_3^(a) > 0 directional prediction
    sign_a_positive = (M_3_a > 0)  # (local)
    sign_b_positive = (M_3_b > 0)  # (local)
    sign_c_positive = (M_3_c > 0)  # (local)
    diagnostics["sign_a_positive"] = bool(sign_a_positive)
    diagnostics["sign_b_positive"] = bool(sign_b_positive)
    diagnostics["sign_c_positive"] = bool(sign_c_positive)
    sign_verdict = (
        "PASS"
        if (sign_a_positive and sign_b_positive and sign_c_positive)
        else "FAIL"
    )

    # Truncation-consistency cross-check at L_max=10 vs 12
    M_3_a_L10 = L10_results["M_3_a"]  # (local)
    M_3_b_L10 = L10_results["M_3_b"]  # (local)
    M_3_c_L10 = L10_results["M_3_c"]  # (local)
    drift_a = abs(M_3_a - M_3_a_L10) / max(abs(M_3_a), 1e-30)  # (local)
    drift_b = abs(M_3_b - M_3_b_L10) / max(abs(M_3_b), 1e-30)  # (local)
    drift_c = abs(M_3_c - M_3_c_L10) / max(abs(M_3_c), 1e-30)  # (local)
    max_drift = max(drift_a, drift_b, drift_c)  # (local)
    diagnostics["drift_a"] = drift_a
    diagnostics["drift_b"] = drift_b
    diagnostics["drift_c"] = drift_c
    diagnostics["max_drift"] = max_drift
    truncation_consistent = (max_drift < REL_TOL_TRUNCATION)  # (local)
    diagnostics["truncation_consistent"] = bool(truncation_consistent)

    if not truncation_consistent and max_drift >= 0.5:
        regime_verdict = "BREAKDOWN"  # (local)
    elif not truncation_consistent:
        regime_verdict = "MARGINAL"  # (local)
    else:
        regime_verdict = "VALID"  # (local)

    # FAIL condition 2: truncation-inconsistent at large drift
    if regime_verdict == "BREAKDOWN":
        return ("FAIL", "truncation-breakdown", sign_verdict, "FAIL", regime_verdict, diagnostics)

    # FAIL condition 3: spread > info_band
    if rel_spread > INFO_BAND:
        return ("FAIL", "spread-exceeds-info-band", sign_verdict, "FAIL", regime_verdict, diagnostics)

    # PASS / INFO discriminator on cross-sub-option spread (pairwise diagnostics
    # already populated above before truncation/spread FAIL early exits).

    # PASS-multi: all three coincide
    if a_b_indistinguishable and a_c_indistinguishable and b_c_indistinguishable:
        return ("PASS", "multi", sign_verdict, "PASS-multi", regime_verdict, diagnostics)

    # PASS-{a,b,c} — sub-option discrimination via Element 3 fiducial-anchor
    # binding discipline:
    #   (a) canonical iff substrate-natural-binding holds without
    #       pre-normalization (M_3^(a) ≈ M_3^(b) within tolerance,
    #       i.e., PV correction is vacuous as the substrate-IS prediction).
    #   (b) canonical iff PV subtraction is non-vacuous AND substrate-
    #       natural at Λ_UV = M_KK (M_3^(b) ≠ M_3^(a) within tolerance).
    #   (c) canonical iff L_k=1 atlas-row pre-normalization required
    #       (M_3^(c) significantly distinct from M_3^(a) AND M_3^(b)
    #       across the locked-norm normalization).

    # Substrate-natural binding logic: at finite L_max the PV tail is
    # vacuous (K_a2_PV = 0 structurally per substitution chain Step 4),
    # so M_3^(a) ≈ M_3^(b) by construction. The c-route is the
    # atlas-row layer alternative. The discriminator at finite L_max
    # therefore reduces to: a-vs-c via locked-norm necessity.
    if a_b_indistinguishable and not a_c_indistinguishable:
        # a and b agree (substrate-natural binding, PV vacuous);
        # c distinct (L_k=1 atlas-row layer is structurally different).
        # Two sub-options collapse to one canonical (a = b), one distinct (c).
        # Per Element 3 binding discipline: (a) is canonical
        # (substrate-natural-binding; PV is vacuous at finite L_max).
        if rel_spread < PASS_BAND:
            return ("PASS", "multi", sign_verdict, "PASS-multi", regime_verdict, diagnostics)
        elif rel_spread < INFO_BAND:
            return ("INFO", "a-b-coincide-c-distinct", sign_verdict, "INFO", regime_verdict, diagnostics)
        else:
            # Should not reach here due to FAIL condition 3 above
            return ("FAIL", "unreachable", sign_verdict, "FAIL", regime_verdict, diagnostics)

    # Pairwise non-coincidence; INFO band check
    if rel_spread < PASS_BAND:
        # Sub-options all indistinguishable (PASS-multi shouldn't trigger but
        # fallback safety)
        return ("PASS", "multi", sign_verdict, "PASS-multi", regime_verdict, diagnostics)
    if rel_spread < INFO_BAND:
        return ("INFO", "spread-in-info-band", sign_verdict, "INFO", regime_verdict, diagnostics)

    # spread > info_band already filtered above
    return ("FAIL", "unhandled-case", sign_verdict, "FAIL", regime_verdict, diagnostics)


# ---------------------------------------------------------------------------
# Section 9 — Plot 3-panel
# ---------------------------------------------------------------------------

def make_plot(L12_results, L10_results, gate_diagnostics, out_path):
    """3-panel: (1) M_3 by sub-option at L_max=12;
                 (2) cross-sub-option residual (pairwise);
                 (3) per-sub-option L_max stability cross-check (L=10 vs 12)."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))  # (local)

    # Panel 1: M_3 by sub-option at L_max=12
    ax = axes[0]
    labels = ["(a) ζ-direct", "(b) PV", "(c) L_k=1"]  # (local)
    values = [L12_results["M_3_a"], L12_results["M_3_b"], L12_results["M_3_c"]]  # (local)
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]  # (local)
    bars = ax.bar(labels, values, color=colors, edgecolor="black")  # (local)
    ax.set_ylabel("M_3 (dimensionless)")
    ax.set_title(f"§VII.AU first-extraction M_3 at L_max={L_MAX_OPERATIONAL}, τ_fold={tau_fold}")
    ax.axhline(0, color="black", linewidth=0.5)
    for bar, val in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            val,
            f"{val:.4e}",
            ha="center",
            va="bottom" if val > 0 else "top",
            fontsize=8,
        )
    ax.grid(True, alpha=0.3)

    # Panel 2: pairwise cross-sub-option residual
    ax = axes[1]
    pair_labels = ["|a−b|/|a|", "|a−c|/|a|", "|b−c|/|b|"]  # (local)
    pair_vals = [
        gate_diagnostics["pairwise_a_b"],
        gate_diagnostics["pairwise_a_c"],
        gate_diagnostics["pairwise_b_c"],
    ]  # (local)
    ax.bar(pair_labels, pair_vals, color="#d62728", edgecolor="black")
    ax.set_yscale("log")
    ax.axhline(PASS_BAND, color="green", linestyle="--", linewidth=0.8, label=f"PASS band ({PASS_BAND})")
    ax.axhline(INFO_BAND, color="orange", linestyle="--", linewidth=0.8, label=f"INFO band ({INFO_BAND})")
    ax.set_ylabel("Pairwise relative residual")
    ax.set_title("Cross-sub-option spread")
    ax.legend(fontsize=8)
    ax.grid(True, which="both", alpha=0.3)

    # Panel 3: L_max stability cross-check
    ax = axes[2]
    labels3 = ["(a)", "(b)", "(c)"]  # (local)
    L12_vals = [L12_results["M_3_a"], L12_results["M_3_b"], L12_results["M_3_c"]]  # (local)
    L10_vals = [L10_results["M_3_a"], L10_results["M_3_b"], L10_results["M_3_c"]]  # (local)
    x = np.arange(len(labels3))  # (local)
    width = 0.35  # (local)
    ax.bar(x - width / 2, L10_vals, width, label=f"L_max={L_MAX_CROSS_CHECK}", color="#9467bd", edgecolor="black")
    ax.bar(x + width / 2, L12_vals, width, label=f"L_max={L_MAX_OPERATIONAL}", color="#8c564b", edgecolor="black")
    ax.set_xticks(x)
    ax.set_xticklabels(labels3)
    ax.set_ylabel("M_3 (dimensionless)")
    ax.set_title(f"L_max stability cross-check (max drift={gate_diagnostics['max_drift']:.2e})")
    ax.legend(fontsize=8)
    ax.axhline(0, color="black", linewidth=0.5)
    ax.grid(True, alpha=0.3)

    fig.suptitle(
        f"{GATE_ID} — composite={gate_diagnostics.get('composite', 'pending')}, "
        f"value={gate_diagnostics.get('value', 'pending')}",
        fontsize=11,
        y=1.02,
    )
    plt.tight_layout()
    plt.savefig(out_path, dpi=120, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 10 — Verdict line emission
# ---------------------------------------------------------------------------

def append_verdict_line(composite, value, audit_sha, content_sha,
                        sign_verdict, magnitude_verdict, regime_verdict):
    """Append the canonical verdict line + dual-SHA companion + S87+ 3-tuple
    companion row per gate-verdicts.md S87+ Schema-v2 + W9a-99 split."""
    L_MAX_TAG = L_MAX_OPERATIONAL  # (local)
    line = (
        f"{GATE_ID}: {composite} -- value={value!r} "
        f"scheme={SCHEME} "
        f"convention={CONVENTION} "
        f"L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    companion_dual = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    companion_3tuple = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2; substitution chain Step 4 "
        f"pre-registers M_3^(a) > 0 directional prediction)\n"
    )  # (local)
    # Level-pin companion comment (LEVEL=FULL; consumes _cm_1995_residue_formula.py
    # PRIMARY per substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY)
    companion_level = (
        f"# LEVEL_CLASS_PIN={LEVEL_PIN} MACHINERY_SCOPE_PIN={MACHINERY_SCOPE_PIN} "
        f"BINDING_AXIS_PIN={BINDING_AXIS_PIN} "
        f"# {GATE_ID} 4-axis pin compliance "
        f"(substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion_dual)
        fp.write(companion_3tuple)
        fp.write(companion_level)


# ---------------------------------------------------------------------------
# Section 11 — Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Verify cache exists
    if not CACHE_PATH.exists():
        print(f"ERROR: cache not found at {CACHE_PATH}")
        return 1

    # 3. tau_fold canonical pin
    tau = float(tau_fold)  # (local) 0.19
    print(f"  τ_fold (canonical) = {tau}")
    print(f"  L_max operational = {L_MAX_OPERATIONAL}")
    print(f"  L_max cross-check = {L_MAX_CROSS_CHECK}")
    print()

    # 4. Compute three sub-options at L_max=12 (operational)
    print("=== Computing three sub-options at L_max=12 (operational) ===")
    L12 = compute_three_sub_options(L_MAX_OPERATIONAL, tau)
    print(f"  slope_A_canonical (runtime-resolved) = {L12['slope_A_canonical_pin']}")
    print(f"  slope_A_source = {L12['slope_A_source']}")
    print(f"  K_a2(τ_fold)         = {L12['K_a2']:.6e}")
    print(f"  K_a2_PV(τ_fold; Λ_UV=M_KK in cache units) = {L12['K_a2_PV']:.6e}")
    print(f"  L_k=1 atlas-row norm = {L12['L_k1_atlas_norm']:.6e}")
    print()
    print(f"  M_3^(a) [ζ-direct]   = {L12['M_3_a']:.6e}")
    print(f"  M_3^(b) [PV-subtr]   = {L12['M_3_b']:.6e}")
    print(f"  M_3^(c) [L_k=1 norm] = {L12['M_3_c']:.6e}")
    print()

    # 5. Truncation cross-check at L_max=10
    print("=== Truncation cross-check at L_max=10 ===")
    L10 = compute_three_sub_options(L_MAX_CROSS_CHECK, tau)
    print(f"  M_3^(a) @ L_max=10 = {L10['M_3_a']:.6e}")
    print(f"  M_3^(b) @ L_max=10 = {L10['M_3_b']:.6e}")
    print(f"  M_3^(c) @ L_max=10 = {L10['M_3_c']:.6e}")
    print()

    # 6. Gate evaluation per plan §W2-2 (9) 6-row threshold table
    (composite, value, sign_verdict, magnitude_verdict, regime_verdict,
     gate_diagnostics) = evaluate_gate(L12, L10)
    gate_diagnostics["composite"] = composite
    gate_diagnostics["value"] = value

    print("=== Gate verdict ===")
    print(f"  cross-sub-option spread          = {gate_diagnostics['spread']:.4e}")
    print(f"  relative spread                  = {gate_diagnostics['rel_spread']:.4e}")
    print(f"  pairwise |a−b|/|a|               = {gate_diagnostics['pairwise_a_b']:.4e}")
    print(f"  pairwise |a−c|/|a|               = {gate_diagnostics['pairwise_a_c']:.4e}")
    print(f"  pairwise |b−c|/|b|               = {gate_diagnostics['pairwise_b_c']:.4e}")
    print(f"  L_max truncation max drift       = {gate_diagnostics['max_drift']:.4e}")
    print(f"  truncation_consistent (<{REL_TOL_TRUNCATION}) = {gate_diagnostics['truncation_consistent']}")
    print(f"  sign_verdict                     = {sign_verdict}")
    print(f"  magnitude_verdict                = {magnitude_verdict}")
    print(f"  regime_verdict                   = {regime_verdict}")
    print(f"  COMPOSITE                        = {composite}")
    print(f"  value                            = {value!r}")
    print()

    # 7. Save NPZ
    np.savez(
        OUT_NPZ,
        M_3_a=L12["M_3_a"],
        M_3_b=L12["M_3_b"],
        M_3_c=L12["M_3_c"],
        M_3_a_L10=L10["M_3_a"],
        M_3_b_L10=L10["M_3_b"],
        M_3_c_L10=L10["M_3_c"],
        cross_sub_option_spread=gate_diagnostics["spread"],
        rel_spread=gate_diagnostics["rel_spread"],
        canonical_sub_option=value,
        slope_A_canonical_pin=L12["slope_A_canonical_pin"],
        slope_A_source=L12["slope_A_source"],
        K_a2_tau_fold=L12["K_a2"],
        K_a2_PV_tau_fold=L12["K_a2_PV"],
        L_k1_atlas_norm=L12["L_k1_atlas_norm"],
        cache_sha=pins[str(CACHE_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/")],
        residue_formula_sha=pins[
            str(RESIDUE_HELPER_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/")
        ],
        L_max_operational=L_MAX_OPERATIONAL,
        L_max_cross_check=L_MAX_CROSS_CHECK,
        level_pin=LEVEL_PIN,
        machinery_scope_pin=MACHINERY_SCOPE_PIN,
        binding_axis_pin=BINDING_AXIS_PIN,
        truncation_consistent=gate_diagnostics["truncation_consistent"],
        max_drift=gate_diagnostics["max_drift"],
        composite=composite,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        pairwise_a_b=gate_diagnostics["pairwise_a_b"],
        pairwise_a_c=gate_diagnostics["pairwise_a_c"],
        pairwise_b_c=gate_diagnostics["pairwise_b_c"],
        inv_two_pi_sq=L12["inv_two_pi_sq"],
        lambda_UV_cache_units=L12["lambda_UV_cache_units"],
        K_a2_breakdown_levels=np.array(list(L12["K_a2_breakdown"].keys())),
        K_a2_breakdown_values=np.array(list(L12["K_a2_breakdown"].values())),
    )
    print(f"  NPZ written: {OUT_NPZ}")

    # 8. Save PNG
    make_plot(L12, L10, gate_diagnostics, OUT_PNG)
    print(f"  PNG written: {OUT_PNG}")

    # 9. Emit 4-tuple
    tag = (
        f"(value={value!r}, scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX_OPERATIONAL})"
    )  # (local)
    print(tag)

    # 10. Append verdict line + dual-SHA + 3-tuple companion
    append_verdict_line(
        composite, value, audit_sha, content_sha,
        sign_verdict, magnitude_verdict, regime_verdict,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
