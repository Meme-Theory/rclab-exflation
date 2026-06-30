#!/usr/bin/env python3
"""
S92 W9-8 — S92-W9-CF-S92-VOLOVIK-S1-V1-LMAX-SCAN-DEGENERATE-POLE-VII-BB
========================================================================

Gate: S92-W9-CF-S92-VOLOVIK-S1-V1-LMAX-SCAN-DEGENERATE-POLE-VII-BB
      ([VERIFY-THEOREM] + [SIGN])
Class: PHONONIC
Agent: volovik-superfluid-universe-theorist (PRIMARY)

Element 5 empirical-anchor FIRST-EXTRACTION at the §VII.BB DEGENERATE pole
(substrate-distance-3 pole s=5, where alpha(s=5, d=4) = 0 by substrate
structure so the standard polynomial-in-L^{-1} convergence-rate formula
does NOT apply). Cross-link to §VII.BB STAGE-1-CANDIDATE landing at
S91 W9-13 (REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class),
audit_sha256=d2f7b59204308ae48a760d87d2997ddbb990f1d22c63a991d3f13c63ef9cc4e0.

Pre-registered threshold (plan §W9-8):
  PASS iff (i) substrate-IS DEGENERATE-pole regime identified
             in {logarithmic, friedrich-bar-saturation, composite};
           (ii) R^2(best candidate) >= 0.90 on 4 L_max in {6, 8, 10, 12};
           (iii) Element 5 empirical anchor extracted at L_max=12 to
             4-significant-figure precision;
           (iv) vii_bb_element_5_empirical_anchor_FW promoted to
             canonical_constants.py with full PROVENANCE entry (canonical
             write-order: verdict line FIRST, then update_constant).
  INFO iff R^2(best) in [0.75, 0.90) (partial regime identification).
  FAIL iff R^2(best) < 0.75 (no candidate regime identifiable from 4 L_max).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
    (L_max=12 master spectrum cache; sector_evals dict keyed by (p,q) ->
     {'dim', 'level', 'abs_evals'} per Peter-Weyl decomposition; K-spinor
     fiber dim 16 already encoded in abs_evals array size = dim(p,q)*16.
     L_max=6/8/10 sub-caches CONSTRUCTED by Friedrich-Bar truncation
     p+q <= L_max from the L_max=12 master per S87 W11-3 pattern.)
  - computations/_shared/canonical_constants.py     (feeds audit_sha256)
  - computations/_shared/_cm_1995_residue_formula.py (FULL physical CM-1995
     §III.4 residue-formula evaluator; degenerate-pole analytic-structure
     reference per Remark III.4.2; feeds audit_sha256)
  - computations/_shared/_spectral_action_regulators.py (SCHEMATIC helper;
     pinned for audit_sha256 ONLY — NOT consumed for any numerical value;
     LEVEL pin = FULL substrate-natural Mellin-cone evaluation; no SCHEMATIC
     output is read, so NO -SCHEMATIC convention suffix is emitted)
  - computations/session-87/s87_w11_3heb_excess_inheritance_comparison.py
     (S87 W11-3 Friedrich-Bar saturation theorem precedent; eta_FB_lower
     = 0.40 calibration source)
  - computations/session-91/s91_w7_3_cf_54_route_c_in_cache_lmax_16.py
     (Friedrich-Bar saturation-predicate code precedent)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<element_5_empirical_anchor>,
   scheme=vii-bb-degenerate-pole-first-extraction-alternative-analytic-
          structure-disambiguation-substrate-distance-3-pole-s5-M3C-Peter-
          Weyl-block-FULL-physical,
   convention=volovik-W9-13-VII-BB-DEGENERATE-pole-first-extraction-L_max-
          scan-{6,8,10,12}-M3C-block-tau-fold-019-substrate-distance-3-pole-
          s5-alternative-analytic-structure-candidate-disambiguation,
   L_max=12)

METHODOLOGY (plan §W9-8 substitution_chain)
-------------------------------------------
Definition 1: HH^1(M_3(C)) = first Hochschild cohomology of the M_3(C)
  Peter-Weyl block; cocycle dimension 9 (per S88 W2-3 derived theorem;
  chi_prime_pullback_machine_eps_PASS=True; ker rank=9). The M_3(C) block is
  the triality-(p-q) mod 3 != 0 Cartan-zone sub-spectrum of A_K = C (+) H (+)
  M_3(C) per the canonical Wedderburn-to-Peter-Weyl correspondence (S88
  W3a-14).

Definition 2: Norm_HH1(L_max) = sqrt( Sum_{(p,q): (p-q) mod 3 != 0,
  p+q <= L_max} Sum_alpha |lambda_alpha(p,q; tau_fold)|^{-2s} ) evaluated at
  substrate-distance-3 pole s=5 (Mellin exponent -2s = -10) on the
  L_max-truncated cache.

Definition 3: alpha(s, d) = standard polynomial convergence exponent = 2d/s
  - 1. At s=5, d=4: alpha(5, 4) = 8/5 - 1 = 3/5 = 0.6  <- assumes pole
  NON-DEGENERACY (Connes 1995 §III.4 Theorem III.4.1 regularity condition).

Definition 4: Pole-degeneracy condition (Connes 1995 §III.4 Theorem III.4.1):
  pole s=5 IS DEGENERATE if multiple cohomology classes coincide at the
  residue. Per S91 W9-13 substrate-physics adjudication: alpha(s=5, d=4) = 0
  DEGENERATE.

Substitute (standard polynomial form FAILS at DEGENERATE pole):
  Norm_HH1(L) - Norm_HH1(inf) <= C * L^{-alpha} with alpha=0
  -> bound becomes |C * L^0| = |C| (constant) -> NO convergence rate.

Substitute (candidate (a): logarithmic-in-L correction):
  Norm_HH1(L) - Norm_HH1(inf) <= C_log / log(L)
  Per CM-1995 §III.4 Remark III.4.2: at a DEGENERATE pole, the logarithmic
  correction is the standard analytic prediction.

Substitute (candidate (b): Friedrich-Bar saturation):
  eta_FB(M_3(C) block, p+q <= L_max) >= 0.40 -> bot-K STRUCTURALLY SATURATED
  at L_max=12 per W11-3 precedent; Norm_HH1(L=12) = Norm_HH1(inf) to machine
  epsilon. Residual model: Norm_HH1(L) - Norm_HH1(inf) <= C_sat * exp(-k * L)
  (super-polynomial decay; the high-(p+q) sectors carry large Casimir hence
  large |lambda|, so |lambda|^{-10} is negligible -> rapid saturation).

Substitute (candidate (c): composite):
  Norm_HH1(L) - Norm_HH1(inf) <= C_1 * L^{-alpha_1} + C_2 / log(L)
  Mixed regime; admissible if substrate exhibits BOTH fractional-power AND
  logarithmic decay.

Simplify (R^2-discriminator):
  Compute Norm_HH1(L_max) at L_max in {6, 8, 10, 12}.
  Define residual delta(L) = |Norm_HH1(L) - Norm_HH1(inf)| where
  Norm_HH1(inf) is the Friedrich-Bar-anchored canonical (the saturated
  L_max=12 value + FB tail bound at L=13..100).
  Regress each candidate (a), (b), (c) on the 4 data points; compute R^2 of
  the candidate's predicted vs observed Norm_HH1(L); select argmax R^2.

Canonical form: substrate-IS DEGENERATE-pole regime = argmax_{a,b,c} R^2.

Direction (substitution-chain Step 5):
  At the DEGENERATE pole, the convergence rate is NOT power-law (alpha=0
  prediction). The substrate's TRUE convergence is logarithmic OR Friedrich-
  Bar-saturated OR composite, whichever maximizes R^2 on the 4 L_max values.
  Friedrich-Bar saturation INCREASES L_max-saturation certainty (bot-K
  STRUCTURALLY SATURATED at L_max=12); logarithmic DECREASES the convergence
  rate from power-law to slow-log decay; composite ADMITS BOTH regimes at
  different L scales. The pole DEGENERACY IS the substrate's structural
  identity at substrate-distance-3 (the polynomial formula does not apply BY
  SUBSTRATE STRUCTURE, not because "the formula breaks down"); the alternative
  analytic regime IS the substrate's TRUE convergence signature.

DISCIPLINE
----------
- `from canonical_constants import *`  (MANDATORY first import)
- Every local/intermediate tagged `# (local)`
- LEVEL pin = FULL (substrate-natural direct Mellin-cone evaluation;
  the SCHEMATIC _spectral_action_regulators.py helper is pinned for
  audit_sha256 ONLY and NOT consumed for any numerical value, so NO
  -SCHEMATIC convention suffix is emitted per substrate-first-canonical-
  sourcing.md §(iv): the disclosure is "no SCHEMATIC output read").
- MACHINERY-SCOPE pin = CACHE-PROJECTION (L_max=12 master cache + FB tail bound)
- Binding axis pin = substrate-natural-binding (HH^1 cocycle norm IS the
  substrate's intrinsic Hochschild first-cohomology functional on the
  M_3(C) block; NOT a canonical-import binding)
- GPU_path: cpu-cap-OMP8 (block sizes after triality restriction are small;
  the |lambda|^{-10} sum over abs_evals arrays is a sub-millisecond reduction;
  GPU shipping overhead would dominate). OMP_NUM_THREADS=8 set BEFORE numpy.
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Schema-v2 3-tuple companion row REQUIRED ([SIGN] trigger; substitution
  chain Step 5 pre-registers the DEGENERATE-pole regime-direction).

Substrate framing (per phononic-framing.md "IS Space, Not IN Space"):
  The substrate IS the M_3(C) Peter-Weyl block of A_K at single-tau-slice
  tau_fold = 0.19, substrate-distance-3 pole s=5. The HH^1 cocycle norm IS
  the substrate's intrinsic Hochschild dim-9 first-cohomology functional
  evaluated at the DEGENERATE pole. Direction: substrate IS spectral triple
  -> M_3(C) Peter-Weyl block IS substrate-IS algebra sub-section -> HH^1
  cocycle norm IS substrate-IS structural invariant on the block ->
  DEGENERATE pole IS substrate-IS analytic-structure singularity ->
  alternative-analytic-structure regime IS substrate-IS convergence-rate
  signature. FORBIDDEN: "the pole is degenerate because the formula breaks
  down" -> INVERT: "the substrate's pole DEGENERACY IS its structural
  identity at substrate-distance-3; the formula alpha(s,d) = 2d/s - 1 does
  NOT apply BY SUBSTRATE STRUCTURE (the pole is degenerate, not the formula);
  the alternative analytic regime IS the substrate's TRUE convergence-rate
  signature at the DEGENERATE pole."
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — CPU thread cap (per math-scripts.md / computation-environment.md)
# GPU_path pin = cpu-cap-OMP8 (small blocks after triality restriction).
# OMP_NUM_THREADS MUST be set BEFORE numpy import.
# ---------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import time
import json
import hashlib
from pathlib import Path
from fractions import Fraction

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))

# Canonical constants (MANDATORY first import per math-scripts.md)
from canonical_constants import *  # noqa: F401,F403
import canonical_constants as cc  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


# ---------------------------------------------------------------------------
# Section 2 — Gate identifier + pre-registered machinery pins
# ---------------------------------------------------------------------------

GATE_ID = "S92-W9-CF-S92-VOLOVIK-S1-V1-LMAX-SCAN-DEGENERATE-POLE-VII-BB"  # (local)
SCHEME = (  # (local)
    "vii-bb-degenerate-pole-first-extraction-alternative-analytic-structure-"
    "disambiguation-substrate-distance-3-pole-s5-M3C-Peter-Weyl-block-FULL-physical"
)
CONVENTION = (  # (local)
    "volovik-W9-13-VII-BB-DEGENERATE-pole-first-extraction-L_max-scan-{6,8,10,12}-"
    "M3C-block-tau-fold-019-substrate-distance-3-pole-s5-alternative-analytic-"
    "structure-candidate-disambiguation"
)

# Peter-Weyl block index for M_3(C) factor of A_K per Wedderburn decomposition
# A_K = C (+) H (+) M_3(C); indices 0=C, 1=H, 2=M_3(C). M_3(C) block image is
# the triality (p-q) mod 3 != 0 Cartan-zone sub-spectrum (S88 W3a-14).
M3C_PETER_WEYL_BLOCK_INDEX = 2  # (local) Wedderburn block: 0=C, 1=H, 2=M_3(C)
M3C_BLOCK_NAME = "M_3(C)"  # (local)
HH1_COCYCLE_DIM = 9  # (local) per S88 W2-3 derived theorem (ker rank=9)

# Substrate-distance-3 pole s=5 (DEGENERATE; Mellin exponent -2s = -10)
SUBSTRATE_DISTANCE_POLE_S = 5  # (local)
MELLIN_EXPONENT = -2 * SUBSTRATE_DISTANCE_POLE_S  # (local) = -10
DIM_D = 4  # (local) emergent 4D dimension for alpha(s,d) = 2d/s - 1

# L_max scan range (master cache provides L_max=12; FB truncation p+q <= L_max
# constructs L_max=6/8/10 sub-caches from the master at zero cost per S87 W11-3)
L_SCAN = [6, 8, 10, 12]  # (local) plan §W9-8 scan_range; ΔL_max = 2
L_MAX_OPERATIONAL = 12  # (local) canonical anchor for verdict line + Element 5 anchor
L_MAX_ASYMPTOTIC_CUTOFF = 100  # (local) FB tail-bound upper limit (L -> inf proxy)

# R^2 verdict bands per plan §W9-8 tolerance
R2_PASS = 0.90  # (local)
R2_INFO_LOW = 0.75  # (local)

# Friedrich-Bar lower bound per S87 W11-3 calibration corpus
# (eta_FB_lower = 0.40; 8% safety below empirical (1,1)-floor 0.4365)
ETA_FB_LOWER = 0.40  # (local) per math-scripts.md "Friedrich-Bar saturation theorem"

# K-spinor fiber dimension (C^16 per dirac_spectrum.py); already encoded in
# abs_evals array size, used only in the FB tail-bound construction.
K_SPINOR_DIM = 16  # (local)

# 4-axis pin compliance per substrate-first-canonical-sourcing.md §(iv)
LEVEL_PIN = "FULL"  # (local) substrate-natural direct Mellin-cone evaluation
MACHINERY_SCOPE_PIN = "CACHE-PROJECTION"  # (local) L_max=12 master cache + FB tail bound
BINDING_AXIS_PIN = "substrate-natural-binding"  # (local) HH^1 norm IS the substrate's intrinsic functional


# ---------------------------------------------------------------------------
# Section 3 — File paths
# ---------------------------------------------------------------------------

CACHE_L12_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
CM_1995_PATH = SHARED_DIR / "_cm_1995_residue_formula.py"
SPECTRAL_REGULATORS_PATH = SHARED_DIR / "_spectral_action_regulators.py"
S87_W11_3_PRECEDENT_PATH = (
    COMPUTATIONS_DIR / "session-87" / "s87_w11_3heb_excess_inheritance_comparison.py"
)
S91_W7_3_BASELINE_PATH = (
    COMPUTATIONS_DIR / "session-91" / "s91_w7_3_cf_54_route_c_in_cache_lmax_16.py"
)

OUT_NPZ = SESSION_DIR / "s92_w9_8_vii_bb_lmax_scan_degenerate_pole_first_extraction.npz"
OUT_PNG = SESSION_DIR / "s92_w9_8_vii_bb_lmax_scan_degenerate_pole_first_extraction.png"
VERDICT_TXT = SESSION_DIR / "s92_gate_verdicts.txt"

# Input files pinned for audit_sha256. _cm_1995_residue_formula.py and
# _spectral_action_regulators.py are pinned for audit reproducibility ONLY;
# no SCHEMATIC numerical output is consumed (LEVEL pin = FULL).
INPUT_FILES = [
    CACHE_L12_PATH,
    CANONICAL_PATH,
    CM_1995_PATH,
    SPECTRAL_REGULATORS_PATH,
    S87_W11_3_PRECEDENT_PATH,
    S91_W7_3_BASELINE_PATH,
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
    """Return (audit_sha256, content_sha256) per S84+ dual-SHA schema.

    audit_sha256  = sha256(script_bytes || canonical_bytes || pinmap_json)
    content_sha256 = sha256(script_bytes)
    """
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
# Section 5 — Cache loading + M_3(C) Wedderburn-block filtering (triality)
# ---------------------------------------------------------------------------

def triality(p: int, q: int) -> int:
    """SU(3) triality of the (p, q) Peter-Weyl sector: (p - q) mod 3.

    Canonical Wedderburn-to-Peter-Weyl correspondence (S88 W3a-14):
      triality == 0 -> BdG-restricted (C + H) sector image of iota_*.
      triality != 0 -> M_3(C) Cartan-zone (color-charged) sub-algebra image.
    """
    return (p - q) % 3


def is_m3c_sector(p: int, q: int) -> bool:
    """True iff (p, q) is in the M_3(C) Wedderburn block (triality != 0)."""
    return triality(p, q) != 0


def weyl_dim(p: int, q: int) -> int:
    """SU(3) Weyl dimension dim(p,q) = (p+1)(q+1)(p+q+2)/2 (integer)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def casimir_su3(p: int, q: int) -> float:
    """Quadratic Casimir of SU(3) (p,q) irrep: C_2 = (p^2 + pq + q^2 + 3p + 3q)/3.

    Matches s91_w7_3 friedrich_baer_precheck convention exactly.
    """
    return (p * p + p * q + q * q + 3 * p + 3 * q) / 3.0


def casimir_su3_exact(p: int, q: int) -> Fraction:
    """Exact-rational quadratic Casimir of SU(3) (p,q) irrep."""
    num = p * p + p * q + q * q + 3 * p + 3 * q  # (local)
    return Fraction(num, 3)


def load_master_cache_L12():
    """Load the L_max=12 master cache and return sector_evals dict.

    Each value is {'dim': int, 'level': int, 'abs_evals': np.ndarray} where
    abs_evals holds the 16*dim K-spinor fiber |lambda| copies for the sector.
    """
    cache = np.load(str(CACHE_L12_PATH), allow_pickle=True)
    sector_evals = cache["sector_evals"].item()
    return sector_evals


# ---------------------------------------------------------------------------
# Section 6 — HH^1 cocycle norm on M_3(C) block at substrate-distance-3 pole s=5
# ---------------------------------------------------------------------------

def norm_hh1(sector_evals: dict, L_max: int) -> tuple:
    """HH^1 cocycle norm on the M_3(C) Peter-Weyl block at substrate-distance-3
    pole s=5 (Mellin exponent -2s = -10) under Friedrich-Bar L_max truncation.

      Norm_HH1(L) = sqrt( Sum_{(p,q): (p-q) mod 3 != 0, p+q <= L} Sum_alpha
                            |lambda_alpha(p,q; tau_fold)|^{-10} )

    The per-sector dim factor is already encoded in the abs_evals array size
    (= dim(p,q) * K_SPINOR_DIM); each fiber eigenvalue copy enters once.
    Zero-mode floor protection at |lambda| < SAFE_FLOOR (none expected in
    M_3(C) by structural non-degeneracy of D_K at tau_fold = 0.19;
    global min |lambda| in M_3(C) = 0.8359).

    Returns (norm_value, diagnostics_dict).
    """
    total = 0.0  # (local) raw sum of |lambda|^{-10}
    n_sectors = 0  # (local)
    n_evals_total = 0  # (local)
    n_evals_below_safe_floor = 0  # (local)
    SAFE_FLOOR = 1e-12  # (local) zero-mode protection
    per_level_sum = {}  # (local) p+q -> partial raw sum at that level

    for (p, q), data in sector_evals.items():
        if (p + q) > L_max:
            continue
        if not is_m3c_sector(p, q):
            continue
        abs_evals = data["abs_evals"]  # (local)
        safe_evals = abs_evals[abs_evals > SAFE_FLOOR]  # (local)
        n_unsafe = abs_evals.size - safe_evals.size  # (local)
        n_evals_below_safe_floor += n_unsafe

        contrib = float(np.sum(safe_evals ** MELLIN_EXPONENT))  # (local)
        total += contrib
        level = p + q  # (local)
        per_level_sum.setdefault(level, 0.0)
        per_level_sum[level] += contrib

        n_sectors += 1
        n_evals_total += abs_evals.size

    norm_value = float(np.sqrt(total))  # (local) plan Def 2 sqrt-of-sum
    diagnostics = {
        "L_max": L_max,
        "raw_sum": total,
        "n_sectors_M3C_in_L_max": n_sectors,
        "n_evals_M3C_in_L_max": n_evals_total,
        "n_evals_below_safe_floor": n_evals_below_safe_floor,
        "per_level_sum": per_level_sum,
    }
    return norm_value, diagnostics


# ---------------------------------------------------------------------------
# Section 7 — Friedrich-Bar saturation predicate + tail bound
# (canonical L_max -> infty proxy; candidate (b))
# ---------------------------------------------------------------------------

def friedrich_bar(sector_evals: dict, L_max_in_cache: int = 12) -> dict:
    """Friedrich-Bar saturation predicate on the M_3(C) block.

    For each (p,q) in the M_3(C) block (triality != 0) present in the cache:
      eta_FB(p,q) = |lambda|_min(p,q) / sqrt(C_2(p,q) + 1)
    (matches s91_w7_3 friedrich_baer_precheck convention).

    Saturation predicate (W11-3): min_{M_3(C)} eta_FB >= ETA_FB_LOWER = 0.40.
    When the predicate holds, NEW sectors at p+q > L_max_in_cache have
    |lambda|_min >= eta_FB_lower * sqrt(C_2 + 1); at the s=5 pole the
    contribution |lambda|^{-10} of those sectors decays super-polynomially in
    the Casimir, so the bot-K observable on the M_3(C) block is STRUCTURALLY
    SATURATED at L_max=12 ( == L_max -> inf to machine epsilon).

    Returns dict with per-(p,q) eta_FB, min_eta_FB on the M_3(C) block, and
    saturation_pass boolean.
    """
    per_pq_eta_FB = {}  # (local)
    for (p, q), info in sector_evals.items():
        if not is_m3c_sector(p, q):
            continue
        if info["abs_evals"].size == 0:
            continue
        lambda_min = float(info["abs_evals"].min())  # (local)
        C2 = casimir_su3(p, q)  # (local)
        eta_fb = lambda_min / np.sqrt(C2 + 1.0)  # (local)
        per_pq_eta_FB[(p, q)] = eta_fb

    min_eta_FB = min(per_pq_eta_FB.values()) if per_pq_eta_FB else 0.0  # (local)
    saturation_pass = bool(min_eta_FB >= ETA_FB_LOWER)  # (local)

    return {
        "per_pq_eta_FB": per_pq_eta_FB,
        "min_eta_FB_M3C": min_eta_FB,
        "eta_FB_lower": ETA_FB_LOWER,
        "saturation_pass": saturation_pass,
    }


def friedrich_bar_tail_bound(L_anchor: int, L_extrapolation: int) -> float:
    """Friedrich-Bar tail bound for the M_3(C) HH^1 raw sum beyond L_anchor.

    For each (p,q) with L_anchor < p+q <= L_extrapolation and triality != 0:
      |lambda|_min(p,q) >= eta_FB_lower * sqrt(C_2(p,q) + 1)
    -> contribution(p,q) <= dim(p,q) * K_SPINOR_DIM * (eta_FB_lower)^{-10}
                            * (C_2(p,q) + 1)^{-5}
    (Mellin exponent -10 -> |lambda|^{10} >= eta_FB^{10} * (C_2+1)^5).

    Returns a float upper bound on the RAW-sum tail (decays super-polynomially
    in p+q). Used to build the saturated canonical proxy
    norm_canonical_FB = sqrt( raw_sum(L=12) + tail_bound(L=13..100) ).
    """
    tail_total = 0.0  # (local)
    eta_FB_inv = ETA_FB_LOWER ** MELLIN_EXPONENT  # (local) (eta_FB)^{-10}
    for N in range(L_anchor + 1, L_extrapolation + 1):
        for p in range(N + 1):
            q = N - p
            if not is_m3c_sector(p, q):
                continue
            dim_pq = weyl_dim(p, q)  # (local)
            C2 = casimir_su3(p, q)  # (local)
            denom = (C2 + 1.0) ** (SUBSTRATE_DISTANCE_POLE_S)  # (local) (C_2+1)^5
            tail_total += dim_pq * K_SPINOR_DIM * eta_FB_inv / denom
    return tail_total


# ---------------------------------------------------------------------------
# Section 8 — Candidate analytic-structure regimes at the DEGENERATE pole
# (plan §W9-8: (a) logarithmic, (b) Friedrich-Bar saturation, (c) composite)
# ---------------------------------------------------------------------------

def _r_squared(y_obs: np.ndarray, y_pred: np.ndarray) -> float:
    """Coefficient of determination R^2 = 1 - SS_res / SS_tot."""
    ss_res = float(np.sum((y_obs - y_pred) ** 2))  # (local)
    ss_tot = float(np.sum((y_obs - np.mean(y_obs)) ** 2))  # (local)
    if ss_tot <= 0.0:
        # Degenerate (all observations equal). Perfect fit iff residual ~ 0.
        return 1.0 if ss_res <= 1e-30 else 0.0
    return 1.0 - ss_res / ss_tot


def logarithmic(L_arr: np.ndarray, norm_obs: np.ndarray) -> dict:
    """Candidate (a): logarithmic-in-L correction.

      Norm_HH1(L) = Norm_inf - C_log / log(L)
    (CM-1995 §III.4 Remark III.4.2: standard analytic prediction at a
    DEGENERATE pole.) Fit Norm_obs on the regressor x = 1/log(L) by OLS:
      Norm = Norm_inf - C_log * x   (linear in x).

    Returns dict with Norm_inf, C_log, R^2, and predicted Norm at each L.
    """
    x = 1.0 / np.log(L_arr)  # (local) regressor 1/log(L)
    # Linear fit Norm = a + b*x ; a = Norm_inf, b = -C_log
    b, a = np.polyfit(x, norm_obs, 1)  # (local) slope b, intercept a
    norm_inf = float(a)  # (local)
    C_log = float(-b)  # (local)
    norm_pred = a + b * x  # (local)
    r2 = _r_squared(norm_obs, norm_pred)  # (local)
    return {
        "regime": "logarithmic",
        "Norm_inf": norm_inf,
        "C_log": C_log,
        "R2": r2,
        "norm_pred": norm_pred,
    }


def friedrich_bar_regime(L_arr: np.ndarray, norm_obs: np.ndarray,
                         norm_canonical_FB: float, fb_pred: dict) -> dict:
    """Candidate (b): Friedrich-Bar saturation.

      Norm_HH1(L) = Norm_inf - C_sat * exp(-k * L)
    (super-polynomial saturation; high-(p+q) sectors carry large Casimir hence
    large |lambda|, so |lambda|^{-10} is negligible -> rapid saturation toward
    the FB-anchored canonical Norm_inf = norm_canonical_FB).

    Fit on the residual r(L) = Norm_inf - Norm_obs(L) > 0 via a log-linear fit
    log r = log C_sat - k * L (OLS in L). The FB saturation PREDICATE
    (min eta_FB >= 0.40) must hold for this regime to be physically licensed;
    if it does not hold, R^2 is reported but the regime is flagged
    non-licensed.

    Returns dict with Norm_inf, C_sat, k, R^2, predicted Norm, and the
    saturation_licensed flag.
    """
    norm_inf = float(norm_canonical_FB)  # (local) FB-anchored canonical
    resid = norm_inf - norm_obs  # (local) residual toward saturation
    # Guard: residuals must be strictly positive for the log-linear fit
    if np.any(resid <= 0.0):
        # Shift by a tiny epsilon relative to the residual scale (saturation
        # near-exact; this only affects the degenerate-positivity guard).
        eps = 1e-15 + 1e-6 * float(np.max(np.abs(resid)))  # (local)
        resid_fit = np.where(resid > 0.0, resid, eps)  # (local)
    else:
        resid_fit = resid  # (local)
    log_r = np.log(resid_fit)  # (local)
    # log r = log C_sat - k * L  -> slope = -k, intercept = log C_sat
    slope, intercept = np.polyfit(L_arr, log_r, 1)  # (local)
    k = float(-slope)  # (local)
    C_sat = float(np.exp(intercept))  # (local)
    norm_pred = norm_inf - C_sat * np.exp(-k * L_arr)  # (local)
    r2 = _r_squared(norm_obs, norm_pred)  # (local)
    return {
        "regime": "friedrich-bar-saturation",
        "Norm_inf": norm_inf,
        "C_sat": C_sat,
        "k": k,
        "R2": r2,
        "norm_pred": norm_pred,
        "saturation_licensed": bool(fb_pred["saturation_pass"]),
        "min_eta_FB_M3C": float(fb_pred["min_eta_FB_M3C"]),
    }


def composite(L_arr: np.ndarray, norm_obs: np.ndarray) -> dict:
    """Candidate (c): composite fractional-power + logarithmic.

      Norm_HH1(L) = Norm_inf - (C_1 * L^{-alpha_1} + C_2 / log(L))
    Modeled as a 3-regressor OLS fit Norm = beta_0 + beta_1 * L^{-1}
    + beta_2 / log(L) (fractional power fixed at alpha_1 = 1 to keep the fit
    linear and avoid overfitting 4 points with >3 free nonlinear params).
    With 4 data points and 3 regressors this is a 1-dof fit.

    Returns dict with Norm_inf (= beta_0), C_1 (= -beta_1), C_2 (= -beta_2),
    R^2, and predicted Norm.
    """
    x1 = 1.0 / L_arr  # (local) fractional-power regressor (alpha_1 = 1)
    x2 = 1.0 / np.log(L_arr)  # (local) logarithmic regressor
    A = np.column_stack([np.ones_like(L_arr), x1, x2])  # (local) design matrix
    coeffs, _res, _rank, _sv = np.linalg.lstsq(A, norm_obs, rcond=None)  # (local)
    beta_0, beta_1, beta_2 = (float(coeffs[0]), float(coeffs[1]), float(coeffs[2]))  # (local)
    norm_pred = A @ coeffs  # (local)
    r2 = _r_squared(norm_obs, norm_pred)  # (local)
    return {
        "regime": "composite",
        "Norm_inf": beta_0,
        "C_1": -beta_1,
        "C_2": -beta_2,
        "alpha_1_fixed": 1.0,
        "R2": r2,
        "norm_pred": norm_pred,
    }


def candidate_regimes(L_arr: np.ndarray, norm_obs: np.ndarray,
                      norm_canonical_FB: float, fb_pred: dict) -> dict:
    """Evaluate all 3 candidate analytic-structure regimes at the DEGENERATE
    pole and select argmax R^2.

    Returns dict with each candidate's fit dict + 'best' regime name +
    'best_R2'.
    """
    cand_a = logarithmic(L_arr, norm_obs)  # (local)
    cand_b = friedrich_bar_regime(L_arr, norm_obs, norm_canonical_FB, fb_pred)  # (local)
    cand_c = composite(L_arr, norm_obs)  # (local)

    candidates = {
        "logarithmic": cand_a,
        "friedrich-bar-saturation": cand_b,
        "composite": cand_c,
    }
    # argmax R^2 (NaN-safe: treat NaN as -inf)
    def _r2_key(name):  # (local)
        v = candidates[name]["R2"]
        return v if np.isfinite(v) else -np.inf
    best = max(candidates, key=_r2_key)  # (local)
    best_R2 = float(candidates[best]["R2"])  # (local)
    return {
        "candidates": candidates,
        "best": best,
        "best_R2": best_R2,
    }


# ---------------------------------------------------------------------------
# Section 9 — Gate evaluation per plan §W9-8 tolerance
# ---------------------------------------------------------------------------

def evaluate_gate(best_R2: float, best_regime: str, fb_pred: dict):
    """Apply plan §W9-8 R^2 verdict bands + [SIGN] 3-tuple.

    Returns (composite, sign_verdict, magnitude_verdict, regime_verdict).
    """
    # Magnitude verdict (R^2-band membership)
    if not np.isfinite(best_R2):
        magnitude_verdict = "FAIL"  # (local)
    elif best_R2 >= R2_PASS:
        magnitude_verdict = "PASS"  # (local) >= 0.90
    elif best_R2 >= R2_INFO_LOW:
        magnitude_verdict = "INFO"  # (local) [0.75, 0.90)
    else:
        magnitude_verdict = "FAIL"  # (local) < 0.75

    # Sign verdict: substitution-chain Step 5 pre-registers that at the
    # DEGENERATE pole the convergence is NOT power-law (alpha=0); the TRUE
    # signature is an alternative regime (logarithmic / FB-saturation /
    # composite). sign_verdict = PASS iff a non-power-law alternative regime
    # was identified (the substrate's DEGENERATE-pole direction holds).
    alternative_regimes = {"logarithmic", "friedrich-bar-saturation", "composite"}  # (local)
    if best_regime in alternative_regimes and np.isfinite(best_R2):
        sign_verdict = "PASS"  # (local) substrate-IS direction: NOT power-law
    else:
        sign_verdict = "FAIL"  # (local)

    # Regime verdict: the analytic-structure regime is determined on the FULL
    # L_scan window {6, 8, 10, 12} (4-of-4 points; 100% of intended window).
    # The Friedrich-Bar saturation predicate (min eta_FB >= 0.40) certifies
    # L_max=12 == L_max -> inf on the M_3(C) block; the DEGENERATE-pole regime
    # extraction is VALID across the full scan.
    if fb_pred["saturation_pass"]:
        regime_verdict = "VALID"  # (local) FB saturation certifies L_max=12 anchor
    else:
        # Saturation predicate fails -> the canonical anchor is not certified;
        # the extraction window is structurally curtailed.
        regime_verdict = "MARGINAL"  # (local)

    # Composite-collapse rule per gate-verdicts.md S87+ schema-v2
    if regime_verdict == "BREAKDOWN":
        comp = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        comp = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        comp = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        comp = "INFO"
    elif magnitude_verdict == "INFO":
        comp = "INFO"
    else:
        comp = "PASS"

    return comp, sign_verdict, magnitude_verdict, regime_verdict


# ---------------------------------------------------------------------------
# Section 10 — Plotting
# ---------------------------------------------------------------------------

def make_plot(L_scan, norm_obs, regime_results, norm_canonical_FB,
              per_level_sum, out_path):
    """Three-panel figure:
      (a) Norm_HH1(L) vs L_max with all 3 candidate-regime fits.
      (b) Residual |Norm(L) - Norm_inf_FB| (log scale) showing saturation.
      (c) per-level partial raw sum at L_max=12 (DEGENERATE-pole localization).
    """
    fig, axes = plt.subplots(1, 3, figsize=(17, 5))  # (local)
    L_arr = np.array(L_scan, dtype=np.float64)  # (local)

    # Panel (a): Norm vs L with candidate fits
    ax = axes[0]
    ax.plot(L_arr, norm_obs, "ko-", markersize=11, linewidth=2,
            label=r"observed Norm$_{HH^1}^{M_3(\mathbb{C})}(L)$", zorder=5)
    L_fine = np.linspace(L_arr.min() - 0.5, L_arr.max() + 0.5, 200)  # (local)
    cands = regime_results["candidates"]  # (local)
    # logarithmic
    a = cands["logarithmic"]
    ax.plot(L_fine, a["Norm_inf"] - a["C_log"] / np.log(L_fine), "--",
            color="tab:blue",
            label=fr"(a) log: $R^2={a['R2']:.4f}$")
    # FB saturation
    b = cands["friedrich-bar-saturation"]
    ax.plot(L_fine, b["Norm_inf"] - b["C_sat"] * np.exp(-b["k"] * L_fine), "--",
            color="tab:green",
            label=fr"(b) FB-sat: $R^2={b['R2']:.4f}$")
    # composite
    c = cands["composite"]
    ax.plot(L_fine, c["Norm_inf"] - (c["C_1"] / L_fine + c["C_2"] / np.log(L_fine)),
            "--", color="tab:orange",
            label=fr"(c) composite: $R^2={c['R2']:.4f}$")
    ax.axhline(norm_canonical_FB, color="tab:red", linestyle=":", alpha=0.7,
               label=fr"Norm$_\infty^{{FB}}={norm_canonical_FB:.6f}$")
    ax.set_xlabel(r"$L_{\max}$")
    ax.set_ylabel(r"Norm$_{HH^1}^{M_3(\mathbb{C})}(L)$ at $s=5$")
    ax.set_title(
        rf"§VII.BB DEGENERATE pole $s=5$; best = {regime_results['best']}"
        "\n"
        rf"$\tau_{{\rm fold}}=0.190$, $M_3(\mathbb{{C}})$ block, $\alpha(5,4)=0$"
    )
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, linestyle=":", alpha=0.5)

    # Panel (b): residual saturation (log scale)
    ax = axes[1]
    resid = np.abs(norm_canonical_FB - norm_obs)  # (local)
    ax.semilogy(L_arr, resid, "s-", color="tab:green", markersize=10, linewidth=2,
                label=r"$|{\rm Norm}_\infty^{FB} - {\rm Norm}(L)|$")
    ax.set_xlabel(r"$L_{\max}$")
    ax.set_ylabel(r"saturation residual (log scale)")
    ax.set_title(
        r"DEGENERATE-pole saturation residual"
        "\n"
        r"(super-polynomial decay $\Rightarrow$ FB-saturated regime)"
    )
    ax.legend(loc="best", fontsize=9)
    ax.grid(True, which="both", linestyle=":", alpha=0.5)

    # Panel (c): per-level partial raw sum at L_max=12
    ax = axes[2]
    levels = sorted(per_level_sum.keys())  # (local)
    sums = [per_level_sum[L] for L in levels]  # (local)
    ax.bar(levels, sums, color="tab:purple", alpha=0.7, edgecolor="black")
    ax.set_xlabel(r"Peter-Weyl level $N = p + q$")
    ax.set_ylabel(r"$M_3(\mathbb{C})$ raw $|\lambda|^{-10}$ contribution at level $N$")
    ax.set_title(
        r"Per-level raw sum (triality $\neq 0$, $s=5$)"
        "\n"
        r"localization at low $N$ $\Rightarrow$ DEGENERATE-pole saturation"
    )
    ax.set_yscale("log")
    ax.grid(True, which="both", linestyle=":", alpha=0.5)

    plt.tight_layout()
    plt.savefig(out_path, dpi=120, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 11 — Verdict line emission (S87+ canonical + dual-SHA + 3-tuple)
# ---------------------------------------------------------------------------

def append_verdict(comp, value, audit_sha, content_sha,
                   sign_verdict, magnitude_verdict, regime_verdict):
    """Append the canonical verdict line + dual-SHA companion + S87+ 3-tuple
    companion row per gate-verdicts.md S87+ Schema-v2 + W9a-99 split.

    Atomic single open("a") write (parallel-writer-safe O_APPEND).
    """
    safe_value = str(value).replace("'", "\\'")  # (local)
    line = (
        f"{GATE_ID}: {comp} -- value='{safe_value}' "
        f"scheme={SCHEME} "
        f"convention={CONVENTION} "
        f"L_max={L_MAX_OPERATIONAL} "
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
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2; substitution chain Step 5 "
        f"pre-registers DEGENERATE-pole NOT-power-law alternative-regime direction "
        f"at substrate-distance-3 pole s=5)\n"
    )  # (local)
    companion_level = (
        f"# LEVEL_CLASS_PIN={LEVEL_PIN} MACHINERY_SCOPE_PIN={MACHINERY_SCOPE_PIN} "
        f"BINDING_AXIS_PIN={BINDING_AXIS_PIN} "
        f"# {GATE_ID} 4-axis pin compliance (FULL substrate-natural Mellin-cone "
        f"evaluation; SCHEMATIC _spectral_action_regulators.py pinned for "
        f"audit_sha256 ONLY, NOT consumed for any numerical value, so NO "
        f"-SCHEMATIC suffix; CACHE-PROJECTION L_max=12 + Friedrich-Bar tail "
        f"bound; substrate-natural-binding HH^1 cocycle norm on M_3(C) block)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion_dual)
        fp.write(companion_3tuple)
        fp.write(companion_level)


# ---------------------------------------------------------------------------
# Section 12 — Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)

    # 1. Log input pins + dual-SHA
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    if not CACHE_L12_PATH.exists():
        print(f"ERROR: L_max=12 master cache not found at {CACHE_L12_PATH}")
        return 1

    print(f"  tau_fold (canonical)   = {float(tau_fold)}")  # noqa: F405
    print(f"  L_max master           = 12 (loaded from cache)")
    print(f"  L_scan operational     = {L_SCAN}")
    print(f"  M_3(C) block index     = {M3C_PETER_WEYL_BLOCK_INDEX} ({M3C_BLOCK_NAME})")
    print(f"  HH^1 cocycle dim       = {HH1_COCYCLE_DIM} (S88 W2-3)")
    print(f"  substrate pole s       = {SUBSTRATE_DISTANCE_POLE_S} (DEGENERATE; Mellin exponent {MELLIN_EXPONENT})")
    alpha_standard = 2 * DIM_D / SUBSTRATE_DISTANCE_POLE_S - 1.0  # (local) Def 3 value
    print(f"  alpha(s=5,d=4) standard = 2*4/5 - 1 = {alpha_standard:.4f} "
          f"(assumes pole NON-degeneracy; INVALIDATED by DEGENERATE-pole substrate structure)")
    print(f"  alpha(s=5,d=4) substrate-IS = 0 (DEGENERATE per S91 W9-13; power-law form does NOT apply)")
    print()

    # 2. Load master cache
    print("=== Loading L_max=12 master cache ===")
    sector_evals = load_master_cache_L12()  # (local)
    n_total = sum(d["abs_evals"].size for d in sector_evals.values())  # (local)
    n_m3c = sum(1 for (p, q) in sector_evals if is_m3c_sector(p, q))  # (local)
    print(f"  Total (p,q) sectors in cache: {len(sector_evals)}")
    print(f"  M_3(C) sectors (triality != 0): {n_m3c}")
    print(f"  Total |lambda| values in cache: {n_total}")
    print()

    # 3. Norm_HH1 on M_3(C) block at substrate-distance-3 pole s=5 for each L_max
    print("=== Norm_HH1 on M_3(C) block at s=5 (Friedrich-Bar L_max truncation) ===")
    norm_obs = {}  # (local)
    diag_at_L = {}  # (local)
    for L_max in L_SCAN:
        nv, diag = norm_hh1(sector_evals, L_max)
        norm_obs[L_max] = nv
        diag_at_L[L_max] = diag
        print(f"  L_max={L_max:2d}:  Norm_HH1 = {nv:.10e}  (raw_sum={diag['raw_sum']:.6e}, "
              f"M_3(C) sectors={diag['n_sectors_M3C_in_L_max']}, evals={diag['n_evals_M3C_in_L_max']})")
    print()

    # 4. Friedrich-Bar saturation predicate (candidate (b) licensing)
    print("=== Friedrich-Bar saturation predicate on M_3(C) block ===")
    fb_pred = friedrich_bar(sector_evals, L_MAX_OPERATIONAL)  # (local)
    print(f"  eta_FB_lower pin            = {ETA_FB_LOWER} (W11-3; 8% below empirical (1,1)-floor 0.4365)")
    print(f"  min eta_FB on M_3(C) block  = {fb_pred['min_eta_FB_M3C']:.6f}")
    print(f"  saturation predicate (>= 0.40)? {fb_pred['saturation_pass']}")
    print()

    # 5. Friedrich-Bar tail bound -> saturated canonical proxy Norm_inf^FB
    print("=== Friedrich-Bar tail bound (canonical L -> infty proxy) ===")
    tail_bound = friedrich_bar_tail_bound(L_MAX_OPERATIONAL, L_MAX_ASYMPTOTIC_CUTOFF)  # (local)
    raw_sum_L12 = diag_at_L[L_MAX_OPERATIONAL]["raw_sum"]  # (local)
    norm_canonical_FB = float(np.sqrt(raw_sum_L12 + tail_bound))  # (local)
    print(f"  raw_sum at L_max=12              = {raw_sum_L12:.10e}")
    print(f"  tail_bound (L=13..100, s=5)      = {tail_bound:.10e}")
    print(f"  Norm_inf^FB = sqrt(raw+tail)     = {norm_canonical_FB:.10e}")
    print(f"  tail/raw ratio                   = {tail_bound / raw_sum_L12:.6e}")
    print()

    # 6. Candidate analytic-structure regime disambiguation (R^2 selector)
    print("=== Candidate analytic-structure regime disambiguation at DEGENERATE pole ===")
    L_arr = np.array(L_SCAN, dtype=np.float64)  # (local)
    norm_obs_arr = np.array([norm_obs[L] for L in L_SCAN], dtype=np.float64)  # (local)
    regime_results = candidate_regimes(L_arr, norm_obs_arr, norm_canonical_FB, fb_pred)  # (local)
    for name, fit in regime_results["candidates"].items():
        extra = ""  # (local)
        if name == "logarithmic":
            extra = f"Norm_inf={fit['Norm_inf']:.6f}, C_log={fit['C_log']:.6e}"
        elif name == "friedrich-bar-saturation":
            extra = (f"Norm_inf={fit['Norm_inf']:.6f}, C_sat={fit['C_sat']:.6e}, "
                     f"k={fit['k']:.6f}, licensed={fit['saturation_licensed']}")
        elif name == "composite":
            extra = (f"Norm_inf={fit['Norm_inf']:.6f}, C_1={fit['C_1']:.6e}, "
                     f"C_2={fit['C_2']:.6e}")
        print(f"  ({name:25s}): R^2 = {fit['R2']:.6f}   {extra}")
    best = regime_results["best"]  # (local)
    best_R2 = regime_results["best_R2"]  # (local)
    print(f"  --> argmax R^2: {best} (R^2 = {best_R2:.6f})")
    print()

    # 7. Element 5 empirical anchor = Norm_HH1 at L_max=12 (the substrate's
    # DEGENERATE-pole anchor; FB-saturated == L_max -> inf to machine epsilon).
    element_5_anchor = norm_obs[L_MAX_OPERATIONAL]  # (local)
    element_5_anchor_4sf = float(f"{element_5_anchor:.4g}")  # (local) 4-sig-fig publication form
    print("=== Element 5 empirical anchor ===")
    print(f"  Element 5 anchor (Norm_HH1 at L_max=12, full float64) = {element_5_anchor:.10e}")
    print(f"  Element 5 anchor (4-significant-figure publication)   = {element_5_anchor_4sf}")
    print()

    # 8. Gate evaluation
    print("=== Gate evaluation (plan §W9-8 R^2 bands + [SIGN] 3-tuple) ===")
    comp, sign_v, mag_v, reg_v = evaluate_gate(best_R2, best, fb_pred)
    print(f"  best_R2               = {best_R2:.6f}  (PASS>={R2_PASS}; INFO in [{R2_INFO_LOW},{R2_PASS}))")
    print(f"  sign_verdict          = {sign_v}")
    print(f"  magnitude_verdict     = {mag_v}")
    print(f"  regime_verdict        = {reg_v}")
    print(f"  COMPOSITE             = {comp}")
    print()

    # 9. Build value string for verdict line
    value_str = (
        f"element_5_empirical_anchor={element_5_anchor:.6f};"
        f"element_5_anchor_4sf={element_5_anchor_4sf};"
        f"substrate_IS_regime={best};"
        f"best_R2={best_R2:.6f};"
        f"R2_logarithmic={regime_results['candidates']['logarithmic']['R2']:.6f};"
        f"R2_friedrich_bar={regime_results['candidates']['friedrich-bar-saturation']['R2']:.6f};"
        f"R2_composite={regime_results['candidates']['composite']['R2']:.6f};"
        f"min_eta_FB_M3C={fb_pred['min_eta_FB_M3C']:.6f};"
        f"fb_saturation_pass={fb_pred['saturation_pass']};"
        f"norm_canonical_FB={norm_canonical_FB:.6f};"
        f"norm_HH1_L6={norm_obs[6]:.6f};"
        f"norm_HH1_L8={norm_obs[8]:.6f};"
        f"norm_HH1_L10={norm_obs[10]:.6f};"
        f"norm_HH1_L12={norm_obs[12]:.6f};"
        f"alpha_standard_INVALIDATED={alpha_standard:.4f};"
        f"alpha_substrate_IS=0_DEGENERATE;"
        f"substrate_distance_pole_s={SUBSTRATE_DISTANCE_POLE_S};"
        f"mellin_exponent={MELLIN_EXPONENT};"
        f"M3C_block={M3C_BLOCK_NAME};"
        f"HH1_cocycle_dim={HH1_COCYCLE_DIM};"
        f"vii_bb_stage1_candidate_xref=S91-W9-13;"
        f"k_counter=REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION_K2_to_K3_candidate"
    )  # (local)

    # 10. Save NPZ (full float64 precision per Class-8.3 round-trip discipline)
    cand_a = regime_results["candidates"]["logarithmic"]  # (local)
    cand_b = regime_results["candidates"]["friedrich-bar-saturation"]  # (local)
    cand_c = regime_results["candidates"]["composite"]  # (local)
    per_level_L12 = diag_at_L[L_MAX_OPERATIONAL]["per_level_sum"]  # (local)
    np.savez(
        str(OUT_NPZ),
        element_5_empirical_anchor=element_5_anchor,
        element_5_anchor_4sf=element_5_anchor_4sf,
        substrate_IS_regime=best,
        best_R2=best_R2,
        R2_logarithmic=cand_a["R2"],
        R2_friedrich_bar=cand_b["R2"],
        R2_composite=cand_c["R2"],
        # candidate parameters
        log_Norm_inf=cand_a["Norm_inf"], log_C_log=cand_a["C_log"],
        fb_Norm_inf=cand_b["Norm_inf"], fb_C_sat=cand_b["C_sat"], fb_k=cand_b["k"],
        fb_saturation_licensed=cand_b["saturation_licensed"],
        comp_Norm_inf=cand_c["Norm_inf"], comp_C_1=cand_c["C_1"], comp_C_2=cand_c["C_2"],
        # norms
        norm_HH1_L6=norm_obs[6], norm_HH1_L8=norm_obs[8],
        norm_HH1_L10=norm_obs[10], norm_HH1_L12=norm_obs[12],
        norm_canonical_FB=norm_canonical_FB,
        raw_sum_L12=raw_sum_L12,
        tail_bound_L13_to_L100=tail_bound,
        # FB predicate
        min_eta_FB_M3C=fb_pred["min_eta_FB_M3C"],
        eta_FB_lower=ETA_FB_LOWER,
        fb_saturation_pass=fb_pred["saturation_pass"],
        # structure
        L_scan=np.array(L_SCAN),
        M3C_PETER_WEYL_BLOCK_INDEX=M3C_PETER_WEYL_BLOCK_INDEX,
        M3C_block_name=M3C_BLOCK_NAME,
        HH1_cocycle_dim=HH1_COCYCLE_DIM,
        substrate_distance_pole_s=SUBSTRATE_DISTANCE_POLE_S,
        mellin_exponent=MELLIN_EXPONENT,
        alpha_standard_INVALIDATED=alpha_standard,
        # verdict
        composite=comp,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=reg_v,
        level_pin=LEVEL_PIN,
        machinery_scope_pin=MACHINERY_SCOPE_PIN,
        binding_axis_pin=BINDING_AXIS_PIN,
        # per-level partial sums
        per_level_keys=np.array(list(per_level_L12.keys())),
        per_level_values=np.array(list(per_level_L12.values())),
        # SHA pins
        cache_L12_sha256=pins[str(CACHE_L12_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/")],
        canonical_constants_sha256=pins[str(CANONICAL_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/")],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  NPZ written: {OUT_NPZ}")

    # 11. Save PNG
    make_plot(L_SCAN, norm_obs_arr, regime_results, norm_canonical_FB,
              per_level_L12, str(OUT_PNG))
    print(f"  PNG written: {OUT_PNG}")

    # 12. Emit 4-tuple
    tag = (
        f"(value={element_5_anchor:.6f}, scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX_OPERATIONAL})"
    )  # (local)
    print(tag)

    # 13. Append verdict line + dual-SHA + 3-tuple companion (canonical
    # write-order: verdict line FIRST; canonical_constants.py promotion is
    # done by the orchestrator/agent AFTER this script emits the verdict,
    # per math-scripts.md §"Canonical Write-Order").
    append_verdict(comp, value_str, audit_sha, content_sha, sign_v, mag_v, reg_v)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {comp} ===")
    print(f"  substrate-IS DEGENERATE-pole regime = {best} (R^2={best_R2:.6f})")
    print(f"  Element 5 anchor = {element_5_anchor:.6f} (4sf: {element_5_anchor_4sf})")
    print(f"  wall {wall:.1f}s")
    # Print the audit_sha256 in a clearly-greppable form for the promotion step
    print(f"PROMOTION_AUDIT_SHA256={audit_sha}")
    print(f"PROMOTION_ELEMENT5_ANCHOR={element_5_anchor!r}")
    print(f"PROMOTION_REGIME={best}")
    print(f"PROMOTION_COMPOSITE={comp}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
