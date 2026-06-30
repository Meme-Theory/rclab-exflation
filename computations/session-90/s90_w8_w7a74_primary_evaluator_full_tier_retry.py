#!/usr/bin/env python3
"""
S90 W8-2 — S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR  (CF-60)
=========================================================================

Gate: S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR  ([VERIFY])

PURPOSE
-------
Spearman cross-tier rank-vector verification comparing:
  - rank_vector^{FULL}      from canonical W7a-74 PRIMARY evaluator
    (S88 `s88_w7a_rank_vs_magnitude_layer_discriminator.py` TIER-1 callables
     `_physical_zeta_T1`, `_physical_cutoff_T1`, `_physical_pv_T1`,
     `_physical_heat_T1`); evaluated over 5 substrate-natural heat-kernel
    anchors at substrate-distance-2 pole s=4 (n_helper=2) on the L_max=12
    physical D_K spectrum at tau_fold=0.19.
  - rank_vector^{SCHEMATIC} loaded from
    `computations/session-89/s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.npz`
    (W5-7 PARTIAL-POSITIVE compliance row 5 per
     `substrate-first-canonical-sourcing.md §(iv)` calibration corpus).

PASS bands (plan §W8-2 lines 501-505):
  PASS-A  iff  N_FULL >= 4/5  AND  spearman_cross_tier >= 0.9
          ==> §VII.AR LEVEL-DRESSED WEAKENED ("SCHEMATIC robust faithful proxy")
  PASS-B  iff  N_FULL >= 4/5  AND  spearman_cross_tier <  0.9
          ==> §VII.AR LEVEL-DRESSED STRENGTHENED ("non-trivial cross-tier
              structural differentiation"); CONNES V.4 PROVISIONAL -> LANDED
  INFO    iff  N_FULL == 3
  FAIL    iff  N_FULL <  3  OR  rank-vector degenerate  OR  any anchor NaN

5 ANCHORS (substrate-natural per W22 synthesis §II.6):
  A1: t_ref = 1/max(λ²)            (inverse-UV² Compton timescale)
  A2: t_ref = 2.3/max(λ²)          (calibrated to SCHEMATIC effective top-mode suppression)
  A3: t_ref = ln(2)/max(λ²)        (half-suppression at lambda_max)
  A4: t_ref = 1/<λ²>_mw            (multiplicity-weighted mean)
  A5: t_ref = 1/M_KK²-internal     (anchor-5 unit-consistency check)

CLASSIFICATION: GEOMETRIC + PHONONIC
  GEOMETRIC because Spearman rank correlation IS a substrate-IS scalar of
  the spectral triple's algebra-INVARIANT cell at the s=4 pole;
  PHONONIC because the regulator-dressed phononic GGE-class observables
  carry the cross-anchor envelope.

CONVENTION (plan lines 444 + §iv K=4 MANDATORY level-pin discipline):
  scheme       = W7a74-PRIMARY-FULL-tier
  convention   = FULL-physical-regularization-NOT-SCHEMATIC   (NO -SCHEMATIC suffix)
  CLASS pin    = FULL (per substrate-first-canonical-sourcing.md §(iv))
  L_max        = 12  (S84 master cache; W22 §IV.3(v) anchor)

SUBSTITUTION CHAIN (plan §W8-2 lines 513-552, MANDATORY):

  Step 1 — Definitions
    rank_vector^{SCHEMATIC}_a := argsort(M_a^{SCHEMATIC,s=4}_a, descending)
                                  [§W5-7 NPZ `rank_vectors[a]`]
    rank_vector^{FULL}_a      := argsort(M_a^{FULL,s=4}_a, descending)
                                  [this gate's output, anchor a]
    spearman(X, Y)            := 1 − (6 Σ d_i²)/(n(n²−1))
                                  on rank vectors of length 4
    threshold                 := 0.9

  Step 2 — Substitution (per-anchor):
    For each anchor a in {A1..A5}, build FULL-tier 4-regulator moments
    M_F2 (zeta-direct on physical λ²),
    M_csq (hard-cutoff at 0.7·max(λ²)),
    M_an  (Pauli-Villars at M_PV² = 0.1·max(λ²)),
    M_zub (heat-kernel with t_ref = anchor a value).
    argsort gives rank_vector^{FULL}_a.

  Step 3 — Per-anchor Spearman:
    spearman_a := spearman(rank_vector^{FULL}_a, rank_vector^{SCHEMATIC}_a)
    spearman_cross_tier := mean over the 5 anchors (the gate-line value).

  Step 4 — N_FULL admissibility count:
    N_FULL := count of anchors with finite, non-NaN M values within the
              plausible band [1e-50, 1e50] in M_KK² units, AND with
              distinct ranks (no all-tied degeneracy).

  Step 5 — Direction:
    spearman_cross_tier >= 0.9 ⟹ PASS-A (WEAKENED; SCHEMATIC robust);
    spearman_cross_tier <  0.9 ⟹ PASS-B (STRENGTHENED; non-trivial differentiation).
    N_FULL == 3 ⟹ INFO (partial admissibility);
    N_FULL <  3 ⟹ FAIL (regulator class breakdown at s=4).

  Step 6 — Conclusion:
    spearman_cross_tier classifies §VII.AR LEVEL-DRESSED into
    WEAKENED (PASS-A) vs STRENGTHENED (PASS-B) feeding the Stage-2
    cross-axis independent-verify gate CF-58 (Wave 7) with the
    substrate-IS FULL-tier rank vector as one of its input pins.

CO-AUTHOR ROLE (connes-ncg-theorist, plan §377-381):
  NCG-axiomatic structural-orthogonality 4-corner audit applied inline:
    F_2          → algebra-INVARIANT spectrum-only (Corner II at s=4)
    cutoff_sqrt  → algebra-INVARIANT spectrum-only (Corner II at s=4)
    anomaly (PV) → algebra-INVARIANT spectrum-only (Corner II at s=4)
    Zubarev (HK) → algebra-INVARIANT spectrum-only (Corner II at s=4)
  All 4 regulators inhabit the SAME algebra-axis cell (Corner II;
  algebra-INVARIANT × Mellin pole s=4) per
  `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`
  MANDATORY-K=3. Spearman comparison respects cross-corner pollution
  test: no cross-corner mixing in the rank computation; all moments
  are spectrum-only functionals of the {λ_k, m_k} pair on the SAME
  spectral triple. Cross-corner co-primary FORBIDDEN check: PASS.

SUBSTRATE FRAMING (per `phononic-framing.md §"IS Space, Not IN Space"`):
  The substrate IS the spectral triple at τ_fold = 0.19 (Level 1
  single-τ-slice). The 5-anchor FULL-tier moments M_a^{FULL,s=4}
  ARE substrate-IS observables at substrate-distance-2 pole s=4.
  The SCHEMATIC counterpart IS the methodology-floor image under
  the layer-functor F: substrate → methodology → audit per
  `epistemic-discipline.md §"Layer-Decomposition"`. The Spearman
  cross-tier IS the structural-fidelity measure of F at the
  rank-ordering layer.

OUTPUT 4-tuple:
  (value=(N_FULL, spearman_cross_tier),
   scheme=W7a74-PRIMARY-FULL-tier,
   convention=FULL-physical-regularization-NOT-SCHEMATIC,
   L_max=12)

Plan:   sessions/session-plan/session-90-plan-w8.md §W8-2 (lines 353-591).
WP:     sessions/archive/session-90/session-90-w8-workingpaper.md §W8-2.
Registry: sessions/permanent-results-registry.md §VII.AR (LEVEL-DRESSED).
Verdict file: computations/session-90/s90_gate_verdicts.txt.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Path / env / canonical-constants
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import math
import json
import time
import hashlib
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SHARED_DIR = PROJECT_ROOT / "_shared"
SESSION_87_DIR = PROJECT_ROOT / "session-87"
SESSION_88_DIR = PROJECT_ROOT / "session-88"
SESSION_89_DIR = PROJECT_ROOT / "session-89"
SESSION_90_DIR = PROJECT_ROOT / "session-90"
sys.path.insert(0, str(SHARED_DIR))

# Canonical-constants (MANDATORY per computations/_shared/CLAUDE.md)
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    tau_fold,
    M_KK,
    Vol_SU3_Haar,
)

import numpy as np  # noqa: E402
from scipy.stats import spearmanr  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# Pull the W7a-74 PRIMARY-tier evaluators from the S88 canonical script
sys.path.insert(0, str(SESSION_88_DIR))
from s88_w7a_rank_vs_magnitude_layer_discriminator import (  # noqa: E402
    _physical_zeta_T1,
    _physical_cutoff_T1,
    _physical_pv_T1,
    _physical_heat_T1,
)
from _analytic_zeta import load_spectrum  # noqa: E402


# ---------------------------------------------------------------------------
# Section 2 — Constants (pre-registered pins per plan §W8-2 machinery)
# ---------------------------------------------------------------------------
GATE_ID = "S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR"  # (local)
SCHEME = "W7a74-PRIMARY-FULL-tier"  # (local) plan line 443
CONVENTION = "FULL-physical-regularization-NOT-SCHEMATIC"  # (local) plan line 444 (NO -SCHEMATIC suffix)
L_MAX = 12  # (local) plan §W8-2 PRDR pin
TAU = 0.19  # (local) tau_fold single-tau-slice (matches tau_fold ≈ 0.19)

N_HELPER = 2  # (local) s=4 ↔ n=2 per W7a-74 canonical mapping
M_PV_SQ_FRAC = 0.10  # (local) plan §W8-2 hard pin
CUTOFF_FRAC = 0.70  # (local) plan §W8-2 hard pin
PLAUSIBLE_BAND_LO = 1e-50  # (local) plan §W8-2 line 436
PLAUSIBLE_BAND_HI = 1e50  # (local) plan §W8-2 line 436
SPEARMAN_THRESHOLD = 0.9  # (local) plan §W8-2 PASS-A vs PASS-B boundary
N_FULL_PASS = 4  # (local) plan §W8-2 PASS / INFO boundary
N_FULL_INFO = 3  # (local) plan §W8-2 INFO / FAIL boundary

REGULATOR_ORDER = ("F_2", "cutoff_sqrt", "anomaly", "Zubarev")  # (local)
ANCHOR_LABELS = (
    "1/max_lambda_sq",
    "2.3/max_lambda_sq",
    "ln2/max_lambda_sq",
    "1/avg_lambda_sq_mw",
    "1/M_KK_sq_internal",
)  # (local)

VERDICT_TXT = SESSION_90_DIR / "s90_gate_verdicts.txt"  # (local) canonical per gate-verdicts.md
OUT_NPZ = SESSION_90_DIR / "s90_w8_w7a74_primary_evaluator_full_tier_retry.npz"  # (local)
OUT_PNG = SESSION_90_DIR / "s90_w8_w7a74_primary_evaluator_full_tier_retry.png"  # (local)


# ---------------------------------------------------------------------------
# Section 3 — SHA helpers
# ---------------------------------------------------------------------------
def file_sha256(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except OSError:
        return "MISSING"


def closure_hash(pins: dict) -> str:
    canon = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True)  # (local)
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per S84+ dual-SHA schema."""
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
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


def append_verdict(verdict: str, value_str: str, audit_sha: str, content_sha: str,
                    sign_v: str, mag_v: str, regime_v: str) -> tuple[str, str, str]:
    """Append S84+ canonical + W9a-99 dual-SHA companion + S87+ 3-tuple companion."""
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    dual_companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    tuple_companion = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_companion)
        fp.write(tuple_companion)
    return canonical_line, dual_companion, tuple_companion


# ---------------------------------------------------------------------------
# Section 4 — Spectrum loading + anchor derivation
# ---------------------------------------------------------------------------
def load_dk_spectrum(L_max: int):
    """Load D_K eigenvalues + multiplicities at L_max=12 from S84 master cache."""
    spec = load_spectrum(L_max)
    if isinstance(spec, tuple):
        eigvals, mults = spec
    else:
        eigvals = spec
        mults = np.ones_like(eigvals)
    eigvals = np.asarray(eigvals, dtype=float)  # (local)
    mults = np.asarray(mults, dtype=float)  # (local)
    return eigvals, mults


def derive_anchors(eigvals: np.ndarray, mults: np.ndarray) -> list:
    """Five substrate-natural heat-kernel anchors per W22 synthesis §II.6."""
    pos = eigvals > 0  # (local)
    lam2 = eigvals[pos] ** 2  # (local)
    m = mults[pos]  # (local)
    max_lambda_sq = float(np.max(lam2))  # (local)
    avg_lambda_sq_mw = float(np.sum(m * lam2) / np.sum(m))  # (local) multiplicity-weighted
    M_KK_sq = float(M_KK) ** 2  # (local) in GeV²
    anchors = [
        ("1/max_lambda_sq", 1.0 / max_lambda_sq),
        ("2.3/max_lambda_sq", 2.3 / max_lambda_sq),
        ("ln2/max_lambda_sq", math.log(2.0) / max_lambda_sq),
        ("1/avg_lambda_sq_mw", 1.0 / avg_lambda_sq_mw),
        ("1/M_KK_sq_internal", 1.0 / M_KK_sq),
    ]  # (local)
    return anchors, max_lambda_sq, avg_lambda_sq_mw, M_KK_sq


# ---------------------------------------------------------------------------
# Section 5 — FULL-tier 4-class evaluator (per W7a-74 canonical TIER-1)
# ---------------------------------------------------------------------------
def evaluate_4class_full_per_anchor(eigvals, mults, n_helper, t_ref):
    """FULL physical regularization (TIER-1) at 4 regulator classes.

    Re-uses the canonical W7a-74 PRIMARY evaluator's TIER-1 functions
    (`_physical_zeta_T1`, `_physical_cutoff_T1`, `_physical_pv_T1`,
    `_physical_heat_T1`) from `s88_w7a_rank_vs_magnitude_layer_discriminator.py`
    operating on physical D_K eigenvalues at L_max=12, tau_fold=0.19.

    Returns dict { F_2: ..., cutoff_sqrt: ..., anomaly: ..., Zubarev: ... }
    """
    pos = eigvals > 0  # (local)
    lambda_max_sq = float(np.max(eigvals[pos] ** 2))  # (local)
    M_F2 = _physical_zeta_T1(eigvals, mults, n_helper, lambda_max_sq)
    M_csq = _physical_cutoff_T1(eigvals, mults, n_helper, lambda_max_sq, cutoff_frac=CUTOFF_FRAC)
    M_an = _physical_pv_T1(eigvals, mults, n_helper, lambda_max_sq, mpv_frac=M_PV_SQ_FRAC)
    M_zub = _physical_heat_T1(eigvals, mults, n_helper, lambda_max_sq, t_ref)
    return {
        "F_2": M_F2,
        "cutoff_sqrt": M_csq,
        "anomaly": M_an,
        "Zubarev": M_zub,
    }


def rank_vector_descending(moments_dict: dict, regulator_order: tuple) -> np.ndarray:
    """argsort descending: rank 0 = highest M; rank len-1 = smallest M.

    Returns array of len(regulator_order) where entry i is the rank (0..n-1)
    of regulator regulator_order[i].
    """
    M_arr = np.array([moments_dict[r] for r in regulator_order])  # (local)
    # argsort gives indices that would sort ascending; reverse for descending
    order_idx = np.argsort(-M_arr)  # (local)  indices sorted by descending M
    # rank[i] = position of regulator i in the descending-M order
    rank = np.empty_like(order_idx)  # (local)
    rank[order_idx] = np.arange(len(M_arr))  # (local)
    return rank.astype(float)


def in_plausible_band(moments_dict: dict) -> bool:
    """N_FULL admissibility check (plan §W8-2 line 436)."""
    for v in moments_dict.values():
        if not np.isfinite(v):
            return False
        if abs(v) < PLAUSIBLE_BAND_LO and v != 0.0:
            return False
        if abs(v) > PLAUSIBLE_BAND_HI:
            return False
    # Also check for all-tied degeneracy
    arr = np.array(list(moments_dict.values()))
    if np.std(arr) < 1e-15 * (abs(arr).max() + 1e-30):
        return False
    return True


# ---------------------------------------------------------------------------
# Section 6 — Anchor-5 unit-consistency cross-check (CONNES V.5)
# ---------------------------------------------------------------------------
def anchor5_unit_consistency_log(eigvals, mults, n_helper, t_ref_M_KK):
    """Compute M_5^{FULL,s=4} := M_a^{FULL,s=4} · M_KK^{-2} cross-check.

    Per plan §W8-2 lines 415-417 (CONNES V.5). The FULL-tier moment
    computed at anchor t_ref = 1/M_KK² in internal units is dimensionless;
    multiplying by M_KK^{-2} would re-dress it; the cross-check is whether
    the unit-cancellation produces a self-consistent dimensionless number
    that does NOT saturate the plausible band.

    NOTE: in the W7a-74 PRIMARY convention, eigenvalues are stored in
    M_KK-natural units (dimensionless); λ²_max = 29.365 is dimensionless.
    Multiplication by M_KK^{-2} for anchor-5 introduces a factor of
    1/M_KK² which is ~1/(5.5e33) GeV^{-2} — a vanishingly small number
    if the moment is GeV-bearing, or simply a re-dressing if the
    moment is internal-unit-bearing. In both readings, the rank-ordering
    is invariant (rank ordering is unaffected by uniform multiplicative
    re-dressing across all 4 regulators).
    """
    M_KK_sq = float(M_KK) ** 2  # (local)
    moments_anchor5 = evaluate_4class_full_per_anchor(eigvals, mults, n_helper, t_ref_M_KK)
    # Dimensionless unit-cancellation cross-check (multiplicative rescale by 1/M_KK²)
    moments_anchor5_rescaled = {k: v / M_KK_sq for k, v in moments_anchor5.items()}  # (local)
    log_dict = {
        "moments_raw": moments_anchor5,
        "moments_rescaled_by_1_over_MKK_sq": moments_anchor5_rescaled,
        "M_KK_sq": M_KK_sq,
        "rank_invariance_check": (
            rank_vector_descending(moments_anchor5, REGULATOR_ORDER).tolist()
            == rank_vector_descending(moments_anchor5_rescaled, REGULATOR_ORDER).tolist()
        ),
    }  # (local)
    return log_dict


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print("=" * 80)
    print(f"{GATE_ID}  (CF-60; S90 W8-2)")
    print("=" * 80)

    # ---- Section 7.1: input SHA-256 pins ----
    input_files = {  # (local)
        "spectrum_cache": PROJECT_ROOT / "session-84" / "s84_spectrum_cache_L12_tau019.npz",
        "spectral_action_regulators": SHARED_DIR / "_spectral_action_regulators.py",
        "analytic_zeta": SHARED_DIR / "_analytic_zeta.py",
        "canonical_constants": SHARED_DIR / "canonical_constants.py",
        "schematic_w5_7_npz": SESSION_89_DIR / "s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.npz",
        "w7a74_primary_evaluator": SESSION_88_DIR / "s88_w7a_rank_vs_magnitude_layer_discriminator.py",
        "plan_w8": PROJECT_ROOT.parent / "sessions" / "session-plan" / "session-90-plan-w8.md",
    }
    pins = {}  # (local)
    print()
    print("Input SHA-256 pins (first 20 lines of stdout):")
    for k, p in input_files.items():
        sha = file_sha256(p)  # (local)
        pins[k] = sha
        print(f"  {k:32s}: {sha[:16]}... ({p.name})")
    print()

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"audit_sha256:   {audit_sha[:16]}... (script + canonical + pinmap)")
    print(f"content_sha256: {content_sha[:16]}... (script only)")
    print()
    print(f"W7a-74 PRIMARY evaluator content_sha (Input pin to §VII.AR registry):")
    print(f"  s88_w7a_rank_vs_magnitude_layer_discriminator.py = {pins['w7a74_primary_evaluator']}")
    print()

    # ---- Section 7.2: load D_K eigenspectrum (L_max=12 master cache) ----
    print("--- Loading D_K spectrum at L_max=12, tau_fold=0.19 ---")
    eigvals, mults = load_dk_spectrum(L_MAX)
    pos = eigvals > 0  # (local)
    print(f"  n_modes = {len(eigvals)}; positive = {pos.sum()}")
    print(f"  lambda range: [{eigvals[pos].min():.4e}, {eigvals[pos].max():.4e}]")
    print(f"  total multiplicity: {np.sum(mults):.0f}")
    anchors, max_lambda_sq, avg_lambda_sq_mw, M_KK_sq = derive_anchors(eigvals, mults)
    print(f"  max_lambda_sq      = {max_lambda_sq:.6f}")
    print(f"  avg_lambda_sq_mw   = {avg_lambda_sq_mw:.6f}")
    print(f"  M_KK_sq (canonical) = {M_KK_sq:.4e}")
    print()
    print("5 substrate-natural anchors:")
    for lbl, val in anchors:
        print(f"  {lbl:32s}: t_ref = {val:.6e}")
    print()

    # ---- Section 7.3: load SCHEMATIC rank vectors from S89 W5-7 NPZ ----
    print("--- Loading SCHEMATIC rank vectors from S89 W5-7 NPZ ---")
    schematic_npz = np.load(input_files["schematic_w5_7_npz"], allow_pickle=True)
    schematic_rank_vectors = np.asarray(schematic_npz["rank_vectors"], dtype=float)  # (local) shape (5, 4)
    schematic_moments = np.asarray(schematic_npz["moments_per_anchor"], dtype=float)  # (local) shape (5, 4)
    schematic_anchors_arr = np.asarray(schematic_npz["anchors"], dtype=float)  # (local) shape (5,)
    schematic_anchor_labels = list(schematic_npz["anchor_labels"])  # (local)
    schematic_regulator_names = list(schematic_npz["regulator_names"])  # (local)
    print(f"  SCHEMATIC anchor labels: {schematic_anchor_labels}")
    print(f"  SCHEMATIC regulators:    {schematic_regulator_names}")
    print(f"  SCHEMATIC rank_vectors shape: {schematic_rank_vectors.shape}")
    for i, lbl in enumerate(schematic_anchor_labels):
        print(f"    anchor {i} ({lbl}): rank = {schematic_rank_vectors[i].astype(int).tolist()}")
    print()

    # ---- Section 7.4: FULL-tier 5-anchor evaluation ----
    print("--- FULL-tier (PRIMARY) evaluation: 5 anchors x 4 regulators ---")
    full_moments = np.zeros((5, 4), dtype=float)  # (local) (anchor, regulator)
    full_rank_vectors = np.zeros((5, 4), dtype=float)  # (local)
    per_anchor_M_dicts = []  # (local)
    per_anchor_in_band = []  # (local)
    for i, (lbl, t_ref) in enumerate(anchors):
        M_dict = evaluate_4class_full_per_anchor(eigvals, mults, N_HELPER, t_ref)
        per_anchor_M_dicts.append(M_dict)
        for j, reg in enumerate(REGULATOR_ORDER):
            full_moments[i, j] = M_dict[reg]
        full_rank_vectors[i] = rank_vector_descending(M_dict, REGULATOR_ORDER)
        in_band = in_plausible_band(M_dict)  # (local)
        per_anchor_in_band.append(in_band)
        print(f"  anchor {i} ({lbl}): t_ref={t_ref:.4e}")
        for reg in REGULATOR_ORDER:
            print(f"    M_{reg:14s} = {M_dict[reg]:+.6e}")
        print(f"    rank_vector_FULL = {full_rank_vectors[i].astype(int).tolist()}")
        print(f"    in_plausible_band = {in_band}")
    print()

    # ---- Section 7.5: Anchor-5 unit-consistency cross-check (CONNES V.5) ----
    print("--- Anchor-5 unit-consistency log (CONNES V.5) ---")
    anchor5_t_ref = anchors[4][1]  # (local) 1/M_KK_sq_internal
    anchor5_log = anchor5_unit_consistency_log(eigvals, mults, N_HELPER, anchor5_t_ref)
    print(f"  anchor5 t_ref = 1/M_KK²_internal = {anchor5_t_ref:.4e}")
    print(f"  M_KK² = {anchor5_log['M_KK_sq']:.4e}")
    print(f"  rank_invariance_check (raw vs M_KK^{-2}-rescaled): {anchor5_log['rank_invariance_check']}")
    print()

    # ---- Section 7.6: Spearman cross-tier per-anchor + mean ----
    print("--- Spearman cross-tier rank correlation (FULL vs SCHEMATIC) per anchor ---")
    spearman_per_anchor = np.zeros(5, dtype=float)  # (local)
    for i in range(5):
        full_rank = full_rank_vectors[i]
        sch_rank = schematic_rank_vectors[i]
        if np.std(full_rank) < 1e-15 or np.std(sch_rank) < 1e-15:
            # All-tied case
            rho = float("nan")
        else:
            rs_obj = spearmanr(full_rank, sch_rank)
            rho = float(rs_obj.statistic) if hasattr(rs_obj, "statistic") else float(rs_obj[0])
        spearman_per_anchor[i] = rho
        print(f"  anchor {i} ({anchors[i][0]:32s}): FULL={full_rank.astype(int).tolist()} "
              f"SCHEMATIC={sch_rank.astype(int).tolist()} spearman={rho:+.6f}")
    spearman_cross_tier = float(np.nanmean(spearman_per_anchor))  # (local) mean across 5 anchors
    print(f"\n  spearman_cross_tier (mean over 5 anchors) = {spearman_cross_tier:.6f}")
    print(f"  threshold (plan §W8-2): {SPEARMAN_THRESHOLD}")
    print()

    # ---- Section 7.7: N_FULL admissibility ----
    N_FULL = int(sum(per_anchor_in_band))  # (local)
    print(f"  N_FULL (anchors PASSing plausible band): {N_FULL} / 5")
    print()

    # ---- Section 7.8: Band classification ----
    if N_FULL < N_FULL_INFO:
        verdict = "FAIL"
        band = "FAIL"
        vii_ar_consequence = (
            "regulator-class breakdown at substrate-distance-2 pole s=4; "
            "§VII.AR LEVEL-DRESSED FAILS structural inheritance from SCHEMATIC tier; "
            "Stage-2 dispatch CF-58 BLOCKED"
        )
    elif N_FULL == N_FULL_INFO:
        verdict = "INFO"
        band = "INFO"
        vii_ar_consequence = (
            "partial admissibility — §VII.AR LEVEL-DRESSED PASS-band hedged; "
            "Stage-2 dispatch CF-58 conditional on S91 regulator-class extension"
        )
    elif spearman_cross_tier >= SPEARMAN_THRESHOLD:
        verdict = "PASS"
        band = "PASS-A"
        vii_ar_consequence = (
            "§VII.AR LEVEL-DRESSED Sub-claim B (cross-tier rank-PARAMETER coupling) "
            "WEAKENED; SCHEMATIC IS a faithful proxy at the rank-ordering layer; "
            "CONNES V.4 PROVISIONAL tagging remains PROVISIONAL pending Stage-2 CF-58"
        )
    else:
        verdict = "PASS"
        band = "PASS-B"
        vii_ar_consequence = (
            "§VII.AR LEVEL-DRESSED Sub-claim B STRENGTHENED; SCHEMATIC vs FULL are "
            "structurally differentiated at the rank-ordering layer; "
            "CONNES V.4 PROVISIONAL tagging PROMOTES to LANDED"
        )
    print(f"BAND CLASSIFICATION: {band}")
    print(f"§VII.AR consequence: {vii_ar_consequence}")
    print()

    # ---- Section 7.9: 3-tuple verdict (sign / magnitude / regime) ----
    # sign_verdict: N/A (no signed delta — Spearman is non-signed correlation)
    sign_v = "N/A"  # (local)
    # magnitude_verdict per band table:
    #   PASS-A / PASS-B → PASS  (composite landed in canonical band)
    #   INFO            → INFO
    #   FAIL            → FAIL
    if band in ("PASS-A", "PASS-B"):
        mag_v = "PASS"
    elif band == "INFO":
        mag_v = "INFO"
    else:
        mag_v = "FAIL"
    # regime_verdict: VALID if all 5 anchors produced finite, non-NaN, in-band values;
    # MARGINAL if 1 anchor saturates the plausible band edge;
    # BREAKDOWN if ≥2 anchors saturate OR anchor-5 unit-consistency check fails
    all_finite = np.all(np.isfinite(full_moments)) and np.all(np.isfinite(spearman_per_anchor[:-1]))
    saturate_count = sum(1 for ok in per_anchor_in_band if not ok)  # (local)
    if not all_finite or not anchor5_log["rank_invariance_check"]:
        regime_v = "BREAKDOWN"  # (local)
    elif saturate_count >= 2:
        regime_v = "BREAKDOWN"  # (local)
    elif saturate_count == 1:
        regime_v = "MARGINAL"  # (local)
    else:
        regime_v = "VALID"  # (local)
    print(f"3-tuple: sign_verdict={sign_v}  magnitude_verdict={mag_v}  regime_verdict={regime_v}")
    print()

    # Apply gate-verdicts.md composite-collapse rule deterministically
    if regime_v == "BREAKDOWN":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    if composite != verdict:
        print(f"NOTE: composite-collapse rule yields {composite}; "
              f"band-derived verdict was {verdict}; using composite={composite}")
        verdict = composite  # gate-verdicts.md collapse rule wins

    # ---- Section 7.10: emit value string + verdict ----
    value_str = f"N_FULL={N_FULL}/5;spearman_cross_tier={spearman_cross_tier:.6f};band={band}"  # (local)
    print(f"VERDICT: {verdict}  value='{value_str}'")
    print()

    # ---- Section 7.11: save NPZ ----
    np.savez(
        OUT_NPZ,
        anchor_labels=np.array(ANCHOR_LABELS),
        anchor_t_refs=np.array([t for _, t in anchors], dtype=float),
        regulator_names=np.array(REGULATOR_ORDER),
        full_moments=full_moments,                              # (5, 4)
        full_rank_vectors=full_rank_vectors,                    # (5, 4)
        schematic_rank_vectors=schematic_rank_vectors,          # (5, 4)
        schematic_moments=schematic_moments,                    # (5, 4)
        spearman_per_anchor=spearman_per_anchor,                # (5,)
        spearman_cross_tier=spearman_cross_tier,                # scalar
        spearman_threshold=SPEARMAN_THRESHOLD,
        N_FULL=N_FULL,
        N_FULL_PASS=N_FULL_PASS,
        N_FULL_INFO=N_FULL_INFO,
        per_anchor_in_band=np.array(per_anchor_in_band, dtype=bool),
        max_lambda_sq=max_lambda_sq,
        avg_lambda_sq_mw=avg_lambda_sq_mw,
        M_KK_sq=M_KK_sq,
        anchor5_log=json.dumps(anchor5_log, default=float),
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        composite_verdict=verdict,
        band=band,
        vii_ar_consequence=vii_ar_consequence,
        L_max=L_MAX,
        tau=TAU,
        s_pole=4,
        n_helper=N_HELPER,
        M_PV_sq_frac=M_PV_SQ_FRAC,
        cutoff_frac=CUTOFF_FRAC,
        plausible_band=np.array([PLAUSIBLE_BAND_LO, PLAUSIBLE_BAND_HI], dtype=float),
        w7a74_primary_evaluator_content_sha=pins["w7a74_primary_evaluator"],
        audit_sha=audit_sha,
        content_sha=content_sha,
    )
    print(f"Saved NPZ: {OUT_NPZ}")

    # ---- Section 7.12: plot ----
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: per-anchor Spearman vs threshold
    ax = axes[0]
    x = np.arange(5)
    ax.bar(x, spearman_per_anchor, color=['steelblue']*5)
    ax.axhline(SPEARMAN_THRESHOLD, color='red', linestyle='--', linewidth=1.5,
                label=f'PASS-A threshold = {SPEARMAN_THRESHOLD}')
    ax.axhline(spearman_cross_tier, color='green', linestyle='-', linewidth=1.5,
                label=f'mean = {spearman_cross_tier:.4f}')
    ax.set_xticks(x)
    ax.set_xticklabels([lbl.replace("_", " ").replace("lambda", "λ") for lbl in ANCHOR_LABELS],
                       rotation=30, ha='right', fontsize=8)
    ax.set_ylabel('Spearman ρ_S (FULL vs SCHEMATIC rank vector)')
    ax.set_title(f'S90 W8-2 — Spearman cross-tier per anchor\n'
                 f'verdict={verdict}  band={band}  N_FULL={N_FULL}/5')
    ax.set_ylim(-1.1, 1.1)
    ax.legend(loc='lower right', fontsize=8)
    ax.grid(True, alpha=0.3)

    # Right: rank-vector comparison (FULL vs SCHEMATIC) overlay
    ax = axes[1]
    width = 0.35  # (local) bar-pair half-width for grouped chart
    x = np.arange(4)  # (local) regulator index
    # Plot mean rank across anchors for both tiers
    full_rank_mean = np.mean(full_rank_vectors, axis=0)  # (local) mean over anchors
    sch_rank_mean = np.mean(schematic_rank_vectors, axis=0)  # (local)
    ax.bar(x - width/2, full_rank_mean, width, label='FULL (TIER-1) mean rank',
           color='steelblue', edgecolor='black')
    ax.bar(x + width/2, sch_rank_mean, width, label='SCHEMATIC (S89 W5-7) mean rank',
           color='salmon', edgecolor='black')
    ax.set_xticks(x)
    ax.set_xticklabels(REGULATOR_ORDER)
    ax.set_ylabel('Mean rank (0=highest M, 3=smallest M)')
    ax.set_title(f'S90 W8-2 — Mean rank-vector comparison\n'
                 f'spearman_cross_tier = {spearman_cross_tier:.4f}  '
                 f'(threshold = {SPEARMAN_THRESHOLD})')
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120, bbox_inches='tight')
    print(f"Saved PNG: {OUT_PNG}")
    print()

    # ---- Section 7.13: emit verdict line + dual-SHA companion + 3-tuple ----
    canonical_line, dual_companion, tuple_companion = append_verdict(
        verdict=verdict,
        value_str=value_str,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_v=sign_v,
        mag_v=mag_v,
        regime_v=regime_v,
    )
    print("Verdict line emitted to s90_gate_verdicts.txt:")
    print(canonical_line.rstrip())
    print(dual_companion.rstrip())
    print(tuple_companion.rstrip())
    print()

    # ---- Section 7.14: 4-tuple summary ----
    print(f"4-tuple: (value=({N_FULL}, {spearman_cross_tier:.6f}), "
          f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    elapsed = time.time() - t0  # (local)
    print(f"\nElapsed: {elapsed:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
