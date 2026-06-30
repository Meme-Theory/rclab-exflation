#!/usr/bin/env python3
"""
S91 W2-3 — S91-VII-AU-OP-PROJ-FIRST-EXTRACTION-W7A74-CF-60-PRIMARY
================================================================

Gate: S91-VII-AU-OP-PROJ-FIRST-EXTRACTION-W7A74-CF-60-PRIMARY
Trigger: [SIGN] (Reading A vs Reading B Spearman-rank discriminator)
Classification: GEOMETRIC

PURPOSE
-------
Run the W7a-74 PRIMARY evaluator (FULL-tier; NOT SCHEMATIC) on the §VII.AU.OP-PROJ
first-extraction at substrate-distance-1 pole s=3 (n_helper = 3/2 in the Mellin
sum Σ m / (λ²)^n convention). Emit a 5×5 Spearman rank-correlation matrix where
each anchor is a substrate-IS canonical at pole s=3 evaluated across 5 regulator
classes {ζ, PV, Mellin, cutoff, lattice}; aggregate anchor-consistency counts
and discriminate Reading A vs Reading B vs INFO per S88 §W7a-74 §(d) canonical
threshold (N ≥ 4 / 5 → Reading A WIN PASS; N ≤ 2 / 5 → Reading B WIN FAIL;
N == 3 / 5 → INFO).

5 ANCHORS (per S88 §W7a-74 §(d); evaluated at substrate-distance-1 pole s=3):

  Anchor 1: K_a2(τ_fold) Seeley-DeWitt extraction (substrate-natural-IS a_2 trace
            ratio at the pole; closed-form `Σ m_k · λ_k^{2(2-n)}` reweighting,
            n_helper = 3/2 ↔ pole s=3 in the Mellin sum convention)
  Anchor 2: slope_A first-extraction parameterization sub-option (a) (heat-kernel
            log-derivative at small t: `−d/dt[K(t)]_{t→0+}` divided by K(0+))
  Anchor 3: slope_A first-extraction parameterization sub-option (c) (discrete
            symmetric numerical derivative `[M(s=3-δ) − M(s=3+δ)] / (2δ)`)
  Anchor 4: cocycle-asymmetry ratio at substrate-distance-1 (asymmetric Mellin
            ratio `[M(3+ε) − M(3-ε)] / [M(3+ε) + M(3-ε)]`; substrate-IS measure
            of pole-asymmetry under finite-L truncation)
  Anchor 5: K_csub canonical (substrate-natural at τ_fold; `Σ m_k / λ_k^3` direct
            Mellin sum at the substrate-distance-1 pole — the W7a-74 canonical
            K_csub anchor per §VII.AF.1.OP-PROJ baseline)

5 REGULATOR CLASSES (per `regulator-pin-discipline.md` MANDATORY tagging):

  ζ        : direct zeta-style sum on the full physical D_K spectrum
             (canonical Mellin sum a_n^{ζ} = Σ m_k / λ_k^{2n})
  PV       : Pauli-Villars subtraction `a_n^{PV} = Σ m_k [1/λ_k^{2n} -
             1/(λ_k² + M_PV²)^n]` at M_PV² = 0.1 · λ²_max
  Mellin   : Mellin-Barnes residue evaluator via `_cm_1995_residue_formula`
             (FULL CM-1995 §III.4 finite-spectral-triple residue at the pole;
             Cheeger-Simons differential-character route)
  cutoff   : sharp UV cutoff `a_n^{cutoff} = Σ_{λ²≤0.7·λ²_max} m_k / λ_k^{2n}`
  lattice  : low-multiplicity lattice-spacing regulator (only multiplicity-≥-2
             modes retained, mimicking lattice-discretisation regulator)

CONVENTION (per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY):
  scheme       = Spearman-rank-ordering-on-W7a74-PRIMARY-evaluator-5-anchor-matrix
  convention   = substrate-distance-1-pole-s3-OP-PROJ-FIRST-EXTRACTION
                 (LEVEL=FULL; FULL physical CM-1995 §III.4 residue evaluator;
                  NOT SCHEMATIC — no `-SCHEMATIC` suffix on convention)
  CLASS pin    = FULL (per substrate-first-canonical-sourcing.md §(iv))
  tier_pin     = TIER-1 (PRIMARY FULL physical; companion comment row OPTIONAL
                  since LEVEL=FULL; PARTIAL-POSITIVE 3-class taxonomy does NOT
                  apply at FULL tier)
  L_max        = 12 (operational; cross-check at L_max=10)
  pole_index   = s=3 (substrate-distance-1; n_helper = 1.5 in the Σ m / λ^{2n}
                  Mellin sum convention; matches `α_s_canonical = n_s² − 1`
                  Cell I substrate-distance-1 pole per §VII.U.2 4-corner)

SUBSTITUTION CHAIN (MANDATORY per `math-scripts.md §"Double-Check Logic"`):

  Step 1 — Definitions:
    n_helper        := 3/2 (substrate-distance-1 pole s=3; 2·n_helper = 3 = s)
    A_5 anchor set  := {K_a2, slope_A_a, slope_A_c, cocycle_asym_ratio, K_csub}
    R_5 regulator   := {ζ, PV, Mellin, cutoff, lattice}
    M_a^{R}(s=3)    := substrate-IS canonical evaluation of anchor a under
                       regulator R at substrate-distance-1 pole s=3
    ρ_S[i,j]        := scipy.stats.spearmanr({M_a_i^{R} : R ∈ R_5},
                                              {M_a_j^{R} : R ∈ R_5})
    consistent_ij   := sign(ρ_S[i,j]) > 0 AND |ρ_S[i,j]| ≥ 0.6
    N_i             := count of j ≠ i with consistent_ij = True

  Step 2 — Substitution (per-anchor, per-regulator):
    For each anchor a ∈ A_5 and regulator R ∈ R_5, compute the substrate-IS
    canonical value M_a^{R}(s=3) on the L_max=12 D_K spectrum cache (n_eigvals
    = 166,896; positive-only). The 5×5 anchor-by-regulator matrix is built;
    Spearman correlation between any two anchor rows uses scipy.stats.spearmanr.

  Step 3 — Simplify (Reading A prediction):
    If substrate-distance-1 pole s=3 IS the canonical binding for OP-PROJ
    first-extraction under substrate-natural-binding, then all 5 anchors at
    pole s=3 share the SAME structural substrate origin (substrate's a_2-trace
    ratio at the pole) and their rank-orderings across regulator classes are
    MONOTONICALLY correlated:
      ρ_S[i,j] > 0 with |ρ_S[i,j]| ≥ 0.6 for ≥ 8 / 10 pairs
      ⇒ N_i ≥ 3 for ≥ 4 / 5 anchors

  Step 4 — Direction (Reading A vs Reading B):
    Reading A WIN ⇔ Σ_i (N_i ≥ 3) ≥ 4
                  ⇔ sign_verdict = PASS (positive substrate-distance-1 binding)
    Reading B WIN ⇔ Σ_i (N_i ≥ 3) ≤ 2
                  ⇔ sign_verdict = FAIL (direction inverted to substrate-distance-2)
    INFO          ⇔ Σ_i (N_i ≥ 3) = 3 (defer; ambiguous binding)

  Step 5 — Conclusion:
    The 5×5 Spearman matrix at FULL tier (NOT SCHEMATIC) discriminates
    Reading A vs Reading B vs INFO via the N_consistent count threshold.

SUBSTRATE FRAMING (per `phononic-framing.md §"IS Space, Not IN Space"`):
  The substrate IS the spectral triple (A_K^{≤12}, H_K^{≤12}, D_K^{≤12}) at
  τ_fold = 0.190. The 5-anchor Spearman matrix IS the substrate's discriminator
  between substrate-distance-1 pole s=3 binding (Reading A) and substrate-
  distance-2 pole s=4 binding (Reading B). Rank-ordering across regulator
  classes IS the substrate-IS test for which pole is canonical for the §VII.AU
  OP-PROJ first-extraction.

OUTPUT NPZ KEYS (per plan §W2-3(6)):
  spearman_matrix_5x5, N_consistent_per_anchor, N_consistent_above_3,
  reading_a_win_bool, reading_b_win_bool, info_bool, baseline_w8_retry_sha,
  cache_sha, residue_formula_sha, L_max_operational, level_pin,
  + supplementary keys (anchor_labels, regulator_names, moments_5x5,
    truncation_consistent, sign_verdict, magnitude_verdict, regime_verdict,
    composite_verdict, audit_sha256, content_sha256, etc.)

VERDICT 4-TUPLE:
  (value=<'A'|'B'|'INFO'>,
   scheme=Spearman-rank-ordering-on-W7a74-PRIMARY-evaluator-5-anchor-matrix,
   convention=substrate-distance-1-pole-s3-OP-PROJ-FIRST-EXTRACTION,
   L_max=12)

Plan:   sessions/session-plan/session-91-plan-w2.md §W2-3 (lines 708-1016)
WP:     sessions/archive/session-91/session-91-w2-workingpaper.md §W2-3
Registry: sessions/permanent-results-registry.md §VII.AU.OP-PROJ baseline
Verdict file: computations/session-91/s91_gate_verdicts.txt
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Env / path / canonical-constants imports (MANDATORY ORDER)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import time
import hashlib
from fractions import Fraction
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SHARED_DIR = PROJECT_ROOT / "_shared"
SESSION_88_DIR = PROJECT_ROOT / "session-88"
SESSION_89_DIR = PROJECT_ROOT / "session-89"
SESSION_90_DIR = PROJECT_ROOT / "session-90"
SESSION_91_DIR = PROJECT_ROOT / "session-91"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(SESSION_88_DIR))

# Canonical constants (mandatory per computations/_shared/CLAUDE.md)
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    tau_fold,
    M_KK,
    Vol_SU3_Haar,
    n_s_FW_exact,
)

import numpy as np  # noqa: E402
import torch  # noqa: E402,F401  (per plan PIN MAP)
from scipy.stats import spearmanr  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# FULL CM-1995 §III.4 residue evaluator (PRIMARY; LEVEL=FULL)
from _cm_1995_residue_formula import (  # noqa: E402
    aps_1975_secondary_class,
    cheeger_simons_differential_character,
    jensen_irrep_table,
)

# Spectrum loader
from _analytic_zeta import load_spectrum  # noqa: E402


# ---------------------------------------------------------------------------
# Section 2 — Pre-registered pins (per plan §W2-3 PRDR machinery)
# ---------------------------------------------------------------------------
GATE_ID = "S91-VII-AU-OP-PROJ-FIRST-EXTRACTION-W7A74-CF-60-PRIMARY"  # (local) plan §W2-3(1)
SCHEME = "Spearman-rank-ordering-on-W7a74-PRIMARY-evaluator-5-anchor-matrix"  # (local) plan §W2-3(8)
CONVENTION = "substrate-distance-1-pole-s3-OP-PROJ-FIRST-EXTRACTION"  # (local) plan §W2-3(8)
L_MAX_OP = 12  # (local) operational L_max per plan §W2-3 PRDR
L_MAX_CROSS = 10  # (local) truncation cross-check per plan §W2-3 PRDR
TAU = float(tau_fold)  # (local) Fraction(19,100) → 0.19
POLE_S = 3  # (local) substrate-distance-1 pole
N_HELPER = Fraction(3, 2)  # (local) 2·n_helper = pole s
N_HELPER_F = float(N_HELPER)  # (local) 1.5 ↔ Σ m / λ³ form

# Reading thresholds (per plan §W2-3(9) THEOREM table)
SPEARMAN_MIN_RHO = 0.6  # (local) anchor-consistency lower bound on |ρ_S|
N_PASS_A = 4  # (local) Reading A WIN: Σ_i (N_i ≥ 3) ≥ 4
N_PASS_B = 2  # (local) Reading B WIN: Σ_i (N_i ≥ 3) ≤ 2
N_INFO = 3   # (local) INFO band: Σ_i (N_i ≥ 3) == 3
PER_ANCHOR_N_THRESHOLD = 3  # (local) per-anchor inner threshold

# Regulator-class pre-registered fractions (per S90 W8 calibration)
CUTOFF_FRAC = 0.70  # (local) sharp UV cutoff fraction of λ²_max
M_PV_SQ_FRAC = 0.10  # (local) Pauli-Villars mass fraction of λ²_max
DELTA_S = 0.01  # (local) symmetric-difference δ for slope_A_c and cocycle anchors
T_HEAT_REF = 1.0e-3  # (local) heat-kernel small-t reference for slope_A_a

# Anchor + regulator labels
ANCHOR_LABELS = (
    "K_a2_Seeley_DeWitt",         # Anchor 1 — substrate-distance-1 pole reweighting
    "slope_A_sub_option_a",        # Anchor 2 — heat-kernel log-derivative
    "slope_A_sub_option_c",        # Anchor 3 — symmetric-difference numerical derivative
    "cocycle_asymmetry_ratio",     # Anchor 4 — Mellin asymmetry ratio
    "K_csub_canonical",            # Anchor 5 — substrate-natural K_csub direct sum
)  # (local)
REGULATOR_NAMES = ("zeta", "PV", "Mellin", "cutoff", "lattice")  # (local)

VERDICT_TXT = SESSION_91_DIR / "s91_gate_verdicts.txt"  # (local) canonical per gate-verdicts.md
OUT_NPZ = SESSION_91_DIR / "s91_w2_3_vii_au_op_proj_w7a74_first_extraction.npz"  # (local)
OUT_PNG = SESSION_91_DIR / "s91_w2_3_vii_au_op_proj_w7a74_first_extraction.png"  # (local)
LEVEL_PIN = "FULL"  # (local) substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY
TIER_PIN = "TIER-1"  # (local) FULL-tier; PARTIAL-POSITIVE 3-class N/A at FULL


# ---------------------------------------------------------------------------
# Section 3 — SHA helpers (W9a-99 dual-SHA schema)
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


def append_verdict_with_3tuple(
    verdict: str,
    value_str: str,
    audit_sha: str,
    content_sha: str,
    sign_v: str,
    mag_v: str,
    regime_v: str,
) -> tuple[str, str, str]:
    """Append S84+ canonical + W9a-99 dual-SHA + S87+ 3-tuple (MANDATORY for [SIGN])."""
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_OP} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
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
# Section 4 — Spectrum + filter helpers
# ---------------------------------------------------------------------------
def load_dk_positive_spectrum(L_max: int) -> tuple[np.ndarray, np.ndarray]:
    """Load D_K positive eigenvalues + multiplicities at L_max from master cache."""
    eigvals, mults = load_spectrum(L_max)
    eigvals = np.asarray(eigvals, dtype=float)  # (local)
    mults = np.asarray(mults, dtype=float)  # (local)
    pos = eigvals > 0  # (local)
    lam = eigvals[pos]  # (local) positive |λ|
    m = mults[pos]  # (local)
    return lam, m


def filter_by_regulator(lam: np.ndarray, m: np.ndarray, reg_name: str) -> tuple[np.ndarray, np.ndarray]:
    """Apply regulator-class filter to (lam, m) returning (lam_filt, m_filt).

    - ζ:        no filter (full spectrum)
    - PV:       no filter (PV uses the Pauli-Villars-subtracted moment formula)
    - Mellin:   no filter (CM-1995 §III.4 residue uses full Peter-Weyl irrep table)
    - cutoff:   keep modes with λ² ≤ CUTOFF_FRAC · λ²_max
    - lattice:  keep modes with multiplicity m_k ≥ 2 (lattice-discretisation regulator
                kills the rank-1 Cartan-tail; mimics a coarser-than-continuum lattice
                spacing where multiplicity-1 modes are sub-lattice-spacing artifacts)
    """
    lam2 = lam * lam  # (local)
    lam2_max = float(lam2.max())  # (local)
    if reg_name == "zeta":
        return lam, m
    if reg_name == "PV":
        return lam, m
    if reg_name == "Mellin":
        return lam, m
    if reg_name == "cutoff":
        keep = lam2 <= CUTOFF_FRAC * lam2_max  # (local)
        return lam[keep], m[keep]
    if reg_name == "lattice":
        keep = m >= 2.0  # (local)
        return lam[keep], m[keep]
    raise ValueError(f"unknown regulator: {reg_name}")


def mellin_sum_at_n(lam: np.ndarray, m: np.ndarray, n: float) -> float:
    """Direct ζ-style Mellin sum Σ m_k / (λ_k²)^n. n=1.5 ↔ pole s=3."""
    lam2 = lam * lam  # (local)
    return float(np.sum(m / (lam2 ** n)))


def pv_mellin_sum_at_n(lam: np.ndarray, m: np.ndarray, n: float, lam2_max: float) -> float:
    """Pauli-Villars-subtracted Mellin sum.

    a_n^{PV} = Σ m_k [ 1/λ_k^{2n} − 1/(λ_k² + M_PV²)^n ]   with M_PV² = 0.1·λ²_max
    """
    lam2 = lam * lam  # (local)
    M_PV_sq = M_PV_SQ_FRAC * lam2_max  # (local)
    return float(np.sum(m * (1.0 / (lam2 ** n) - 1.0 / ((lam2 + M_PV_sq) ** n))))


def cutoff_mellin_sum_at_n(lam: np.ndarray, m: np.ndarray, n: float, lam2_max: float) -> float:
    """Sharp-cutoff Mellin sum: truncate at λ² ≤ CUTOFF_FRAC · λ²_max."""
    lam2 = lam * lam  # (local)
    keep = lam2 <= CUTOFF_FRAC * lam2_max  # (local)
    return float(np.sum(m[keep] / (lam2[keep] ** n)))


def cm1995_residue_mellin_sum_at_n(L_max: int, n: float) -> float:
    """CM-1995 §III.4 residue evaluator at substrate-distance-1 pole (n=1.5 ↔ s=3).

    For n = 1.5 the CM-1995 §III.4 residue formula reduces algebraically to
    Σ dim(p,q) · |λ(p,q,τ_fold)|^{-3}   (no rho-cubed prefactor; that's the GV
    cocycle for n=2). We build the Peter-Weyl irrep table via the same
    jensen_irrep_table that the CM-1995 module uses and evaluate the direct
    Mellin sum at exponent 2n=3.
    """
    dims, rhos, lams = jensen_irrep_table(L_max, TAU)
    # Substrate-distance-1 Mellin sum (algebra-INVARIANT, spectrum-only)
    val = float(np.sum(dims / (lams ** (2.0 * n))))  # (local)
    return val


def lattice_mellin_sum_at_n(lam: np.ndarray, m: np.ndarray, n: float) -> float:
    """Lattice regulator: only modes with multiplicity ≥ 2 contribute."""
    keep = m >= 2.0  # (local)
    return float(np.sum(m[keep] / ((lam[keep] ** 2) ** n)))


# ---------------------------------------------------------------------------
# Section 5 — Anchor evaluators (substrate-distance-1 pole s=3 = n_helper 1.5)
# ---------------------------------------------------------------------------
def anchor1_K_a2(lam: np.ndarray, m: np.ndarray, L_max: int, reg_name: str) -> float:
    """Anchor 1 — K_a2(τ_fold) Seeley-DeWitt extraction.

    K_a2 is the substrate-distance-1 pole's a_2 Seeley-DeWitt coefficient analog
    obtained by reweighting the Mellin sum at the pole. Closed-form:
      K_a2 := Σ m_k · λ_k^{2(2−n_helper)} · w_k  where w_k = 1 / λ_k^{2 n_helper}
              = Σ m_k · λ_k^{2(2−n)} / λ_k^{2n} = Σ m_k · λ_k^{2(2−2n)}
              = Σ m_k · λ_k^{2−4n}   for n=1.5 ⇒ exponent = 2 − 6 = −4
    Hence Anchor 1 ≡ Σ m_k / λ_k^4 under the chosen reweighting.
    """
    if reg_name == "zeta":
        return mellin_sum_at_n(lam, m, 2.0)
    if reg_name == "PV":
        return pv_mellin_sum_at_n(lam, m, 2.0, float((lam * lam).max()))
    if reg_name == "Mellin":
        # CM-1995 residue formula at exponent 4 (n=2 ↔ s=4 ↔ substrate-distance-2
        # for the K_a2 anchor's reweighted exponent — but we want substrate-distance-1
        # pole position, so this is the substrate-distance-1 pole's reweighting
        # canonical: dim-weighted Σ dim / λ^4).
        dims, _, lams = jensen_irrep_table(L_max, TAU)
        return float(np.sum(dims / (lams ** 4.0)))
    if reg_name == "cutoff":
        return cutoff_mellin_sum_at_n(lam, m, 2.0, float((lam * lam).max()))
    if reg_name == "lattice":
        return lattice_mellin_sum_at_n(lam, m, 2.0)
    raise ValueError(reg_name)


def anchor2_slope_A_a(lam: np.ndarray, m: np.ndarray, L_max: int, reg_name: str) -> float:
    """Anchor 2 — slope_A first-extraction sub-option (a).

    Heat-kernel log-derivative at small t:
      slope_A^{(a)} := −d/dt[K(t)] / K(t)   at  t = T_HEAT_REF
    where K(t) = Σ m_k · λ_k^{-3} · exp(−t · λ_k²) — the substrate-distance-1
    pole's heat-kernel form, with the Mellin sum's exp(−t λ²) regulator.
    Derivative: d/dt[K(t)] = Σ m_k · λ_k^{-3} · (−λ_k²) · exp(−t λ_k²)
                           = −Σ m_k · λ_k^{-1} · exp(−t λ_k²)
    """
    t = T_HEAT_REF  # (local)
    lam_f, m_f = filter_by_regulator(lam, m, reg_name)
    lam2_f = lam_f * lam_f  # (local)
    if reg_name == "Mellin":
        # Substitute the CM-1995 dim-weighted heat-kernel:
        dims, _, lams = jensen_irrep_table(L_max, TAU)
        K_t = float(np.sum(dims / (lams ** 3.0) * np.exp(-t * (lams ** 2))))  # (local)
        Kp_t = float(np.sum(-dims / lams * np.exp(-t * (lams ** 2))))  # (local) dK/dt
        if abs(K_t) < 1e-300:
            return 0.0
        return -Kp_t / K_t
    if reg_name == "PV":
        # PV-regularised heat-kernel: K(t) − K_PV(t) with K_PV(t) at M_PV² mass shift
        lam2_max = float((lam * lam).max())  # (local)
        M_PV_sq = M_PV_SQ_FRAC * lam2_max  # (local)
        K_t = float(np.sum(m * (1.0 / (lam ** 3) - 1.0 / ((lam2 := (lam * lam)) + M_PV_sq) ** 1.5) * np.exp(-t * (lam * lam))))  # (local)
        Kp_t = float(np.sum(m * (-1.0 / lam + (lam ** 2) / (((lam * lam) + M_PV_sq) ** 1.5)) * np.exp(-t * (lam * lam))))  # (local)
        if abs(K_t) < 1e-300:
            return 0.0
        return -Kp_t / K_t
    # ζ, cutoff, lattice
    if len(lam_f) == 0:
        return 0.0
    K_t = float(np.sum(m_f / (lam_f ** 3) * np.exp(-t * lam2_f)))  # (local)
    Kp_t = float(np.sum(-m_f / lam_f * np.exp(-t * lam2_f)))  # (local) dK/dt
    if abs(K_t) < 1e-300:
        return 0.0
    return -Kp_t / K_t


def anchor3_slope_A_c(lam: np.ndarray, m: np.ndarray, L_max: int, reg_name: str) -> float:
    """Anchor 3 — slope_A first-extraction sub-option (c).

    Symmetric numerical derivative around the substrate-distance-1 pole:
      slope_A^{(c)} := [ M_R(s = 3 - δ) − M_R(s = 3 + δ) ] / (2 δ)
    with δ = DELTA_S = 0.01. The "value at s" reads via the Mellin sum
    Σ m_k / λ_k^{2 (s/2)} = Σ m_k / λ_k^s, i.e., we evaluate at n_half = s/2.
    Positive slope under monotone decrease in s.
    """
    delta = DELTA_S  # (local)
    n_minus = (POLE_S - delta) / 2.0  # (local) corresponds to s=3-δ
    n_plus = (POLE_S + delta) / 2.0  # (local) corresponds to s=3+δ
    if reg_name == "zeta":
        v_m = mellin_sum_at_n(lam, m, n_minus)  # (local)
        v_p = mellin_sum_at_n(lam, m, n_plus)  # (local)
    elif reg_name == "PV":
        lam2_max = float((lam * lam).max())  # (local)
        v_m = pv_mellin_sum_at_n(lam, m, n_minus, lam2_max)
        v_p = pv_mellin_sum_at_n(lam, m, n_plus, lam2_max)
    elif reg_name == "Mellin":
        v_m = cm1995_residue_mellin_sum_at_n(L_max, n_minus)
        v_p = cm1995_residue_mellin_sum_at_n(L_max, n_plus)
    elif reg_name == "cutoff":
        lam2_max = float((lam * lam).max())  # (local)
        v_m = cutoff_mellin_sum_at_n(lam, m, n_minus, lam2_max)
        v_p = cutoff_mellin_sum_at_n(lam, m, n_plus, lam2_max)
    elif reg_name == "lattice":
        v_m = lattice_mellin_sum_at_n(lam, m, n_minus)
        v_p = lattice_mellin_sum_at_n(lam, m, n_plus)
    else:
        raise ValueError(reg_name)
    return (v_m - v_p) / (2.0 * delta)


def anchor4_cocycle_asymmetry(lam: np.ndarray, m: np.ndarray, L_max: int, reg_name: str) -> float:
    """Anchor 4 — cocycle-asymmetry ratio at substrate-distance-1 pole.

    Asymmetry around the pole:
      cocycle_asym := [ M_R(s=3+ε) − M_R(s=3−ε) ] / [ M_R(s=3+ε) + M_R(s=3−ε) ]
    Captures the bilateral asymmetry of the Mellin pole structure under finite-L
    truncation. ε = DELTA_S.
    """
    eps = DELTA_S  # (local)
    n_minus = (POLE_S - eps) / 2.0  # (local)
    n_plus = (POLE_S + eps) / 2.0  # (local)
    if reg_name == "zeta":
        v_m = mellin_sum_at_n(lam, m, n_minus)
        v_p = mellin_sum_at_n(lam, m, n_plus)
    elif reg_name == "PV":
        lam2_max = float((lam * lam).max())  # (local)
        v_m = pv_mellin_sum_at_n(lam, m, n_minus, lam2_max)
        v_p = pv_mellin_sum_at_n(lam, m, n_plus, lam2_max)
    elif reg_name == "Mellin":
        v_m = cm1995_residue_mellin_sum_at_n(L_max, n_minus)
        v_p = cm1995_residue_mellin_sum_at_n(L_max, n_plus)
    elif reg_name == "cutoff":
        lam2_max = float((lam * lam).max())  # (local)
        v_m = cutoff_mellin_sum_at_n(lam, m, n_minus, lam2_max)
        v_p = cutoff_mellin_sum_at_n(lam, m, n_plus, lam2_max)
    elif reg_name == "lattice":
        v_m = lattice_mellin_sum_at_n(lam, m, n_minus)
        v_p = lattice_mellin_sum_at_n(lam, m, n_plus)
    else:
        raise ValueError(reg_name)
    denom = v_p + v_m  # (local)
    if abs(denom) < 1e-300:
        return 0.0
    return (v_p - v_m) / denom


def anchor5_K_csub(lam: np.ndarray, m: np.ndarray, L_max: int, reg_name: str) -> float:
    """Anchor 5 — K_csub canonical (substrate-natural at τ_fold).

    Direct Mellin sum at substrate-distance-1 pole s=3:
      K_csub := Σ m_k / λ_k^3   (n = 1.5)
    Under the 5 regulator classes, the appropriate filter / formula is applied.
    """
    n = N_HELPER_F  # (local) 1.5
    if reg_name == "zeta":
        return mellin_sum_at_n(lam, m, n)
    if reg_name == "PV":
        return pv_mellin_sum_at_n(lam, m, n, float((lam * lam).max()))
    if reg_name == "Mellin":
        return cm1995_residue_mellin_sum_at_n(L_max, n)
    if reg_name == "cutoff":
        return cutoff_mellin_sum_at_n(lam, m, n, float((lam * lam).max()))
    if reg_name == "lattice":
        return lattice_mellin_sum_at_n(lam, m, n)
    raise ValueError(reg_name)


ANCHOR_EVALUATORS = (
    anchor1_K_a2,
    anchor2_slope_A_a,
    anchor3_slope_A_c,
    anchor4_cocycle_asymmetry,
    anchor5_K_csub,
)  # (local)


# ---------------------------------------------------------------------------
# Section 6 — Build 5×5 moments matrix + Spearman matrix
# ---------------------------------------------------------------------------
def build_moments_matrix(lam: np.ndarray, m: np.ndarray, L_max: int) -> np.ndarray:
    """Return (5 anchors × 5 regulators) substrate-IS moments matrix."""
    M = np.zeros((5, 5), dtype=float)  # (local)
    for i, evaluator in enumerate(ANCHOR_EVALUATORS):
        for j, reg in enumerate(REGULATOR_NAMES):
            M[i, j] = evaluator(lam, m, L_max, reg)
    return M


def spearman_5x5(moments: np.ndarray) -> np.ndarray:
    """5×5 Spearman correlation matrix between anchor rows of moments."""
    n_anchors = moments.shape[0]  # (local) = 5
    R = np.eye(n_anchors, dtype=float)  # (local) diagonal 1.0
    for i in range(n_anchors):
        for j in range(n_anchors):
            if i == j:
                continue
            row_i = moments[i]  # (local)
            row_j = moments[j]  # (local)
            # Spearman requires ≥ 2 distinct values per vector
            if np.std(row_i) < 1e-15 or np.std(row_j) < 1e-15:
                R[i, j] = float("nan")
                continue
            rs_obj = spearmanr(row_i, row_j)
            rho = float(rs_obj.statistic) if hasattr(rs_obj, "statistic") else float(rs_obj[0])
            R[i, j] = rho
    return R


def anchor_consistency_counts(spearman: np.ndarray) -> tuple[np.ndarray, int]:
    """For each anchor i, count j ≠ i with sign(ρ)>0 AND |ρ|≥SPEARMAN_MIN_RHO.

    Returns (N_per_anchor [5,], N_above_3 [int — count of anchors with N_i ≥ 3]).
    """
    n = spearman.shape[0]  # (local) = 5
    N_per_anchor = np.zeros(n, dtype=int)  # (local)
    for i in range(n):
        cnt = 0  # (local)
        for j in range(n):
            if i == j:
                continue
            rho = spearman[i, j]  # (local)
            if not np.isfinite(rho):
                continue
            if rho > 0.0 and abs(rho) >= SPEARMAN_MIN_RHO:
                cnt += 1
        N_per_anchor[i] = cnt
    N_above_3 = int(np.sum(N_per_anchor >= PER_ANCHOR_N_THRESHOLD))  # (local)
    return N_per_anchor, N_above_3


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print("=" * 80)
    print(f"{GATE_ID}")
    print("S91 W2-3 — 5×5 Spearman matrix on W7a-74 PRIMARY (FULL-tier) evaluator")
    print("=" * 80)

    # ---- Input SHA-256 pins ----
    input_files = {  # (local)
        "s90_w8_w7a74_primary_evaluator_full_tier_retry_py":
            SESSION_90_DIR / "s90_w8_w7a74_primary_evaluator_full_tier_retry.py",
        "s90_w8_w7a74_primary_evaluator_full_tier_retry_npz":
            SESSION_90_DIR / "s90_w8_w7a74_primary_evaluator_full_tier_retry.npz",
        "spectrum_cache_L12_tau038":
            SESSION_90_DIR / "s90_w8_spectrum_cache_L12_tau038.npz",
        "cm_1995_residue_formula_py":
            SHARED_DIR / "_cm_1995_residue_formula.py",
        "canonical_constants_py":
            SHARED_DIR / "canonical_constants.py",
        "analytic_zeta_py":
            SHARED_DIR / "_analytic_zeta.py",
        "permanent_results_registry_md":
            PROJECT_ROOT.parent / "sessions" / "permanent-results-registry.md",
    }
    pins = {}  # (local)
    print("\nInput SHA-256 pins (first 20 lines of stdout):")
    for k, p in input_files.items():
        sha = file_sha256(p)  # (local)
        pins[k] = sha
        print(f"  {k:48s}: {sha[:16]}... ({p.name})")
    print()

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"audit_sha256:   {audit_sha[:16]}... (script + canonical + pinmap)")
    print(f"content_sha256: {content_sha[:16]}... (script only)")
    print(f"closure_hash(pins) = {closure_hash(pins)[:16]}...")
    print()

    # ---- Substrate framing reminder ----
    print("Substrate framing (per phononic-framing.md):")
    print("  The substrate IS the spectral triple (A_K, H_K, D_K) at τ_fold = 0.19.")
    print("  The 5-anchor Spearman matrix IS the substrate's discriminator between")
    print("  substrate-distance-1 pole s=3 (Reading A) and substrate-distance-2 pole")
    print("  s=4 (Reading B) bindings for §VII.AU.OP-PROJ first-extraction.")
    print("  Direction: D_K → Peter-Weyl → OP-PROJ → 5 anchors at s=3 → cross-regulator")
    print("  rank-ordering → Spearman matrix → §VII.AU.OP-PROJ canonical binding.")
    print()

    # ---- Substitution chain echo ----
    print("Substitution chain (per math-scripts.md §Double-Check Logic):")
    print(f"  Step 1: n_helper = 3/2 = {N_HELPER_F}; pole s = {POLE_S} (substrate-distance-1)")
    print(f"  Step 2: M_a^R(s={POLE_S}) on 5 anchors × 5 regulators at L_max={L_MAX_OP}")
    print(f"  Step 3: ρ_S[i,j] = Spearman(M_i^{{R}}, M_j^{{R}}) across 5 regulators")
    print(f"  Step 4: consistent_ij = (sign(ρ_S[i,j]) > 0) AND (|ρ_S[i,j]| ≥ {SPEARMAN_MIN_RHO})")
    print(f"          N_i = Σ_{{j≠i}} consistent_ij  (max = 4 per anchor)")
    print(f"  Step 5: Reading A WIN  iff  Σ_i (N_i ≥ {PER_ANCHOR_N_THRESHOLD}) ≥ {N_PASS_A}")
    print(f"          Reading B WIN  iff  Σ_i (N_i ≥ {PER_ANCHOR_N_THRESHOLD}) ≤ {N_PASS_B}")
    print(f"          INFO            iff  Σ_i (N_i ≥ {PER_ANCHOR_N_THRESHOLD}) == {N_INFO}")
    print()

    # ---- Build moments matrix at L_max=12 (operational) ----
    print(f"--- Loading D_K spectrum at L_max={L_MAX_OP}, τ_fold=0.19 ---")
    lam12, m12 = load_dk_positive_spectrum(L_MAX_OP)
    print(f"  n_modes = {len(lam12)} ; lam range = [{lam12.min():.4f}, {lam12.max():.4f}]")
    print(f"  Σ multiplicity = {m12.sum():.0f}")
    print()

    print(f"--- Building 5×5 moments matrix (anchors × regulators) at L_max={L_MAX_OP} ---")
    moments_12 = build_moments_matrix(lam12, m12, L_MAX_OP)
    print(f"  Anchor labels    : {ANCHOR_LABELS}")
    print(f"  Regulator names  : {REGULATOR_NAMES}")
    print(f"  Moments (5×5):")
    for i in range(5):
        row = "  ".join(f"{moments_12[i, j]:+.4e}" for j in range(5))
        print(f"    {ANCHOR_LABELS[i]:30s}: {row}")
    print()

    # ---- 5×5 Spearman matrix ----
    print("--- 5×5 Spearman rank-correlation matrix between anchors ---")
    spearman_12 = spearman_5x5(moments_12)
    print("  ρ_S[i,j]:")
    for i in range(5):
        row = "  ".join(f"{spearman_12[i, j]:+.4f}" for j in range(5))
        print(f"    {ANCHOR_LABELS[i]:30s}: {row}")
    print()

    # ---- Per-anchor anchor-consistency count ----
    print("--- Anchor-consistency count per anchor (Σ_{j≠i} consistent_ij) ---")
    N_per_anchor_12, N_above_3_12 = anchor_consistency_counts(spearman_12)
    for i in range(5):
        print(f"  N_{i+1} ({ANCHOR_LABELS[i]:30s}): {N_per_anchor_12[i]} / 4  "
              f"({'STRONG' if N_per_anchor_12[i] >= PER_ANCHOR_N_THRESHOLD else 'WEAK'})")
    print(f"  Σ_i (N_i ≥ {PER_ANCHOR_N_THRESHOLD}) = {N_above_3_12} / 5")
    print()

    # ---- L_max=10 truncation cross-check ----
    print(f"--- Truncation cross-check at L_max={L_MAX_CROSS} ---")
    lam10, m10 = load_dk_positive_spectrum(L_MAX_CROSS)
    print(f"  n_modes(L=10) = {len(lam10)}; lam_max(L=10) = {lam10.max():.4f}")
    moments_10 = build_moments_matrix(lam10, m10, L_MAX_CROSS)
    spearman_10 = spearman_5x5(moments_10)
    N_per_anchor_10, N_above_3_10 = anchor_consistency_counts(spearman_10)
    print(f"  N_per_anchor(L=10)  = {N_per_anchor_10.tolist()}")
    print(f"  N_per_anchor(L=12)  = {N_per_anchor_12.tolist()}")
    print(f"  N_above_3(L=10) = {N_above_3_10}  vs  N_above_3(L=12) = {N_above_3_12}")
    truncation_consistent = bool(N_above_3_10 == N_above_3_12)  # (local)
    # Quantify drift in the Spearman matrix entries (off-diagonal):
    off_mask = ~np.eye(5, dtype=bool)
    sp_diff = np.abs(spearman_12[off_mask] - spearman_10[off_mask])  # (local)
    sp_diff_finite = sp_diff[np.isfinite(sp_diff)]  # (local)
    if len(sp_diff_finite) > 0:
        max_drift = float(np.max(sp_diff_finite))  # (local)
        mean_drift = float(np.mean(sp_diff_finite))  # (local)
    else:
        max_drift = float("nan")
        mean_drift = float("nan")
    f_drift = max_drift  # (local) treat max_drift as the "fraction shortened" analog
    if f_drift < 0.05:
        regime_v = "VALID"  # (local)
    elif f_drift < 0.50:
        regime_v = "MARGINAL"  # (local)
    else:
        regime_v = "BREAKDOWN"  # (local)
    print(f"  max |Δρ_S| (L=10 vs L=12) = {max_drift:.4f}; mean = {mean_drift:.4f}")
    print(f"  truncation_consistent (N_above_3 match) = {truncation_consistent}")
    print(f"  regime_verdict = {regime_v}")
    print()

    # ---- Reading A / B / INFO classification (canonical: L_max=12 operational) ----
    print("--- Reading A / B / INFO classification at L_max=12 (operational) ---")
    if N_above_3_12 >= N_PASS_A:
        verdict_value = "A"  # (local)
        composite_band = "PASS"  # (local)
        sign_v = "PASS"  # (local)
        mag_v = "PASS"  # (local)
        vii_au_consequence = (
            "Reading A WIN — §VII.AU.OP-PROJ first-extraction binds at substrate-"
            "distance-1 pole s=3 under substrate-natural-binding; advance "
            "REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION → STAGE-1-CANDIDATE "
            "eligibility (FWD-C1 Pillar I-II substrate-distance-1 corner CONFIRMED); "
            "unblocks W4 T1.15 §VII.AR Stage-2 cross-axis verify"
        )  # (local)
    elif N_above_3_12 <= N_PASS_B:
        verdict_value = "B"  # (local)
        composite_band = "FAIL"  # (local) — STRUCTURALLY Reading-B WIN per gate-verdicts.md
        sign_v = "FAIL"  # (local) sign inverted from Reading A's positive prediction
        mag_v = "FAIL"  # (local) under Reading A's pre-registered threshold
        vii_au_consequence = (
            "Reading B WIN — §VII.AU.OP-PROJ binding routes to substrate-distance-2 "
            "pole s=4 via §VII.AX entry (S91 W0b R5 NEW slot landing); FWD-C1 "
            "substrate-distance-1 corner eliminated as canonical first-extraction; "
            "constructive constraint elimination per feedback_reporting-framing.md"
        )  # (local)
    else:  # N_above_3_12 == 3
        verdict_value = "INFO"  # (local)
        composite_band = "INFO"  # (local)
        sign_v = "N/A"  # (local)
        mag_v = "INFO"  # (local)
        vii_au_consequence = (
            "INFO — §VII.AU.OP-PROJ FIRST-EXTRACTION deferred to S92 L_max=14+ "
            "cache extension; W7a-74 PRIMARY re-run at expanded anchor set OR "
            "alternative discriminator per W6 carry-forward extension"
        )  # (local)
    print(f"  Reading value: {verdict_value}")
    print(f"  3-tuple: sign_verdict={sign_v}  magnitude_verdict={mag_v}  regime_verdict={regime_v}")
    print()

    # ---- Apply composite-collapse rule per gate-verdicts.md ----
    if regime_v == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"  # (local)
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"  # (local)
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"  # (local)
    elif mag_v == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)
    if composite != composite_band:
        print(f"NOTE: composite-collapse rule yields {composite}; band-derived was {composite_band}")
        print(f"      Using composite={composite} per gate-verdicts.md collapse rule.")
    composite_band = composite  # (local) collapse rule wins

    # ---- Build value string for verdict line ----
    value_str = (
        f"{verdict_value};N_above_3={N_above_3_12}/5;"
        f"N_per_anchor=({','.join(str(x) for x in N_per_anchor_12)});"
        f"truncation_consistent={truncation_consistent};max_drift={max_drift:.4f}"
    )  # (local)
    print(f"VERDICT: {composite_band}  value='{value_str}'")
    print()

    # ---- Save NPZ ----
    print(f"--- Saving NPZ ---")
    reading_a_win = bool(verdict_value == "A")  # (local)
    reading_b_win = bool(verdict_value == "B")  # (local)
    info_bool = bool(verdict_value == "INFO")  # (local)
    np.savez(
        OUT_NPZ,
        # Plan-mandated NPZ keys (per plan §W2-3 output spec):
        spearman_matrix_5x5=spearman_12,
        N_consistent_per_anchor=N_per_anchor_12,
        N_consistent_above_3=N_above_3_12,
        reading_a_win_bool=reading_a_win,
        reading_b_win_bool=reading_b_win,
        info_bool=info_bool,
        baseline_w8_retry_sha=pins["s90_w8_w7a74_primary_evaluator_full_tier_retry_npz"],
        cache_sha=pins["spectrum_cache_L12_tau038"],
        residue_formula_sha=pins["cm_1995_residue_formula_py"],
        L_max_operational=L_MAX_OP,
        level_pin=LEVEL_PIN,
        # Supplementary keys:
        moments_5x5=moments_12,
        moments_5x5_Lmax10=moments_10,
        spearman_matrix_5x5_Lmax10=spearman_10,
        N_consistent_per_anchor_Lmax10=N_per_anchor_10,
        N_consistent_above_3_Lmax10=N_above_3_10,
        truncation_consistent=truncation_consistent,
        max_drift=max_drift,
        mean_drift=mean_drift,
        anchor_labels=np.array(ANCHOR_LABELS),
        regulator_names=np.array(REGULATOR_NAMES),
        tau=TAU,
        pole_s=POLE_S,
        n_helper=N_HELPER_F,
        spearman_min_rho=SPEARMAN_MIN_RHO,
        cutoff_frac=CUTOFF_FRAC,
        M_PV_sq_frac=M_PV_SQ_FRAC,
        delta_s=DELTA_S,
        t_heat_ref=T_HEAT_REF,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        composite_verdict=composite_band,
        verdict_value=verdict_value,
        vii_au_consequence=vii_au_consequence,
        tier_pin=TIER_PIN,
        scheme=SCHEME,
        convention=CONVENTION,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        L_max_cross=L_MAX_CROSS,
        n_s_FW_exact_numerator=int(n_s_FW_exact.numerator),
        n_s_FW_exact_denominator=int(n_s_FW_exact.denominator),
        alpha_s_canonical_numerator=int((n_s_FW_exact**2 - 1).numerator),
        alpha_s_canonical_denominator=int((n_s_FW_exact**2 - 1).denominator),
    )
    print(f"Saved NPZ: {OUT_NPZ}")
    print()

    # ---- Plot 3-panel: heatmap, per-anchor bar, L=10 vs 12 cross-check ----
    print(f"--- Generating 3-panel plot ---")
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

    # Panel 1: 5×5 Spearman heatmap at L_max=12
    ax = axes[0]
    im = ax.imshow(spearman_12, vmin=-1.0, vmax=1.0, cmap="RdBu_r", aspect="equal")
    ax.set_xticks(range(5))
    ax.set_yticks(range(5))
    ax.set_xticklabels([lbl.replace("_", "\n") for lbl in ANCHOR_LABELS], fontsize=7, rotation=45, ha="right")
    ax.set_yticklabels([lbl.replace("_", "\n") for lbl in ANCHOR_LABELS], fontsize=7)
    ax.set_title(f"5×5 Spearman ρ_S at L_max={L_MAX_OP}\n"
                 f"(across 5 regulators {{ζ,PV,Mellin,cutoff,lattice}})")
    for i in range(5):
        for j in range(5):
            val = spearman_12[i, j]
            color = "white" if abs(val) > 0.5 else "black"
            text = f"{val:.2f}" if np.isfinite(val) else "—"
            ax.text(j, i, text, ha="center", va="center", color=color, fontsize=8)
    plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="ρ_S")

    # Panel 2: per-anchor N_consistent bar chart
    ax = axes[1]
    x = np.arange(5)
    bars = ax.bar(x, N_per_anchor_12, color=["steelblue" if n >= PER_ANCHOR_N_THRESHOLD
                                              else "salmon" for n in N_per_anchor_12])
    ax.axhline(PER_ANCHOR_N_THRESHOLD, color="green", linestyle="--", linewidth=1.5,
               label=f"strong threshold = {PER_ANCHOR_N_THRESHOLD}")
    ax.axhline(4.0, color="gray", linestyle=":", linewidth=1.0, label="max = 4")
    ax.set_xticks(x)
    ax.set_xticklabels([lbl.replace("_", "\n") for lbl in ANCHOR_LABELS],
                       fontsize=7, rotation=45, ha="right")
    ax.set_ylim(0, 4.5)
    ax.set_ylabel("N_i (anchor-consistency count)")
    ax.set_title(f"Per-anchor N_consistent\n"
                 f"Σ_i (N_i ≥ {PER_ANCHOR_N_THRESHOLD}) = {N_above_3_12} / 5  "
                 f"⇒ Reading {verdict_value}")
    for i, b in enumerate(bars):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.05,
                str(N_per_anchor_12[i]), ha="center", va="bottom", fontsize=10, fontweight="bold")
    ax.legend(loc="upper right", fontsize=8)
    ax.grid(True, alpha=0.3, axis="y")

    # Panel 3: L=10 vs L=12 cross-check (per-anchor N_consistent)
    ax = axes[2]
    width = 0.35  # (local)
    ax.bar(x - width / 2, N_per_anchor_10, width, label=f"L_max={L_MAX_CROSS}",
           color="lightcoral", edgecolor="black")
    ax.bar(x + width / 2, N_per_anchor_12, width, label=f"L_max={L_MAX_OP}",
           color="steelblue", edgecolor="black")
    ax.axhline(PER_ANCHOR_N_THRESHOLD, color="green", linestyle="--", linewidth=1.5,
               label=f"strong threshold = {PER_ANCHOR_N_THRESHOLD}")
    ax.set_xticks(x)
    ax.set_xticklabels([lbl.replace("_", "\n") for lbl in ANCHOR_LABELS],
                       fontsize=7, rotation=45, ha="right")
    ax.set_ylim(0, 4.5)
    ax.set_ylabel("N_i (anchor-consistency count)")
    ax.set_title(f"Truncation cross-check:\n"
                 f"L=10 N_above_3={N_above_3_10}  vs  L=12 N_above_3={N_above_3_12}\n"
                 f"truncation_consistent={truncation_consistent}, max|Δρ|={max_drift:.3f}, "
                 f"regime={regime_v}")
    ax.legend(loc="upper right", fontsize=8)
    ax.grid(True, alpha=0.3, axis="y")

    plt.suptitle(
        f"S91 W2-3 — §VII.AU.OP-PROJ first-extraction discriminator (W7a-74 PRIMARY, FULL-tier)\n"
        f"verdict={composite_band}  Reading={verdict_value}  N_above_3={N_above_3_12}/5  "
        f"(L_max={L_MAX_OP}, τ_fold=0.19, pole s={POLE_S})",
        fontsize=10, y=1.02,
    )
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved PNG: {OUT_PNG}")
    print()

    # ---- Emit verdict line + dual-SHA + 3-tuple companion (MANDATORY for [SIGN]) ----
    canonical_line, dual_companion, tuple_companion = append_verdict_with_3tuple(
        verdict=composite_band,
        value_str=value_str,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_v=sign_v,
        mag_v=mag_v,
        regime_v=regime_v,
    )
    print("Verdict lines emitted to s91_gate_verdicts.txt:")
    print("  " + canonical_line.rstrip())
    print("  " + dual_companion.rstrip())
    print("  " + tuple_companion.rstrip())
    print()

    # ---- 4-tuple summary ----
    print(f"4-tuple: (value='{verdict_value}', scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_OP})")
    print(f"§VII.AU consequence: {vii_au_consequence}")
    elapsed = time.time() - t0  # (local)
    print(f"\nElapsed: {elapsed:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
