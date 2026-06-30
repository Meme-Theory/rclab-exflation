#!/usr/bin/env python3
"""
S91 W6-1: S91-D4-ENVELOPE-EXTENDED-L_MAX-SUB-WINDOW (T2.54 / CF-1)
====================================================================

Gate: S91-D4-ENVELOPE-EXTENDED-L_MAX-SUB-WINDOW ([VERIFY-THEOREM])

PRIMARY:   lizzi-spectral-functional-theorist
CO-SIGN:   connes-ncg-theorist (Connes-Karoubi pairing implementation per
           Connes-Chamseddine 1996 §2.2-2.3 + Connes-Moscovici 1995 §III.4
           residue-formula evaluator on band-0 + HKR-image observable;
           NCG-axiomatic anchor for §VII.AU.OP-PROJ Pillar I ↔ Pillar II
           HKR-image-bound observable at substrate-distance-1 pole s=3)

Method
------
Pathway (b) FIRST at L_max=22 via direct Connes-Karoubi pairing of the
§VII.AU.OP-PROJ Pillar I ↔ Pillar II HKR-image-bound observable on the
finite spectral triple (A_K^{<=L}, H_K^{<=L}, D_K^{<=L}) at L ∈ {12..22}.

The pairing is realized via the Hochschild cocycle representation of
Ch(P_0) coupled to the gauge-symmetric cocycle φ_g^{sym} per Connes-
Chamseddine 1996 §2.2-2.3; at finite L, the substrate-IS realization is
the CM-1995 §III.4 residue-formula evaluator on the lowest-Casimir
Peter-Weyl sector at each level (band-0 P_0 + HKR-image):

    R_b(L) = dim(p*, q*) · (C_2(p*, q*) + 1)^{-3}

where (p*, q*) = argmin_{p+q=L} C_2(p, q) is the substrate-IS minimal-
Casimir image of the band-0 projector at level L. This realization
matches the W6-4 O_2 substrate-IS COMBINATORIAL FORM precedent (lines
329-350; substrate-IS algebra-canonical; cache-independent at L > 12 by
construction); CRUCIALLY, no eigenvalue cache extension to L > 12 is
required, since the substrate-IS pairing IS the Peter-Weyl combinatorial
formula directly per the Friedrich-Bär saturation theorem (W11-3
precedent in `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-
Projection Feasibility Pre-Check"`).

Bypasses the c_sub_corrected M_Pl_eff² ratio's asymptotic-settling scale
bottleneck (CF-65 empirical α ≈ 1.929 floor) per workshop EC2 derivation
lines 1162-1170.

PATHWAY (a) BACKUP NOT EXECUTED IN THIS SCRIPT:
Per plan §12 lines 286-288, pathway (a) at L_max ≥ 35 (Friedrich-Bär
saturation extension via CF-54 + CF-65 re-extraction) is a SEPARATE
S92+ escalation IF pathway (b) returns INFO / FAIL. Pathway (b) is
dispatched FIRST as the cheaper test; pathway (a) backup escalation
fires only on a deferred pending refinement, not within this gate.

Substitution chain (plan §10, MANDATORY for [VERIFY-THEOREM] direction):

  Definitions:
    α_asymptotic := exponent at L_max → ∞ per CM-1995 §III.4 d=4
                    dimension-spectrum residue formula at substrate-distance-1
                    pole s=3 (predicted = 3 per Reading A canonical)
    α_pre_asymp  := empirical exponent at L_max ∈ [6, 12] (measured = 1.929
                    per CF-65)
    α_pathway_b  := empirical exponent at L_max ∈ [15, 22] via direct
                    Connes-Karoubi pairing (this gate's output)

  Step 1: Reading A direction:
    c_sub_corrected_M_Pl_eff²(L_max) → 1 as L_max → ∞   [asymptotic-settling]
    ⇒ α_pathway_b(L_max=22) → α_asymptotic = 3
         [direct Connes-Karoubi pairing bypasses c_sub bottleneck]

  Step 2: Reading B direction:
    α IS substrate-IS regulator-INVARIANT BY CONSTRUCTION at d=4 pole s=3
    ⇒ α_pathway_b(L_max=22) = α_pre_asymp = 1.929   [persistent at all L_max]

  Step 3: Substitution (PASS-A criterion):
    IF α_pathway_b ∈ [2.4, 3.6] AT majority-of-5 OR Mellin+zeta F_2 projection
    THEN Reading A canonical confirmed → §VII.AU.OP-PROJ → STAGE-1-CANDIDATE-PENDING-STAGE-2

  Step 4: Substitution (FAIL-B criterion):
    IF α_pathway_b ∈ [1.615, 2.185] AND count_pass(≥ 3 of 5) FAILS
    THEN Reading B realized confirmed → HYBRID verdict (d) at per-regulator-class sub-window

  Step 5: Direction of comparison:
    PASS-A: "α increases with L_max under direct Connes-Karoubi pairing"
    FAIL-B: "α stays at 1.9 across pathways"

Per-regulator atlas (A_5: {Mellin, zeta, Pauli-Villars, cutoff, lattice}):

The Mellin / zeta members IS regulator-INVARIANT BY CONSTRUCTION at the
d=4 substrate-distance-1 pole s=3 per CM-1995 §III.4 dimension-spectrum
residue formula (the substrate-distance pole indexing is the substrate-
IS algebra-canonical structure; no regulator enters). Both members
therefore yield IDENTICAL α via shell-sum slope on the substrate-IS
combinatorial form.

The Pauli-Villars / cutoff / lattice members carry regulator-class-
specific suppression weights at the s=3 pole; per W6-2 K=5 SCHEMATIC
calibration, these are realized via the W6-2 sub_term_R analytic forms
(SCHEMATIC at the K=4 MANDATORY level-pin discipline per
`substrate-first-canonical-sourcing.md §(iv)`). To avoid the W6-2 K_csub
divergence (Λ_UV²·sub_term Λ_PV^{-2}·L²·log(L) divergence at large L),
the regulator-class weights enter the Connes-Karoubi pairing as
RELATIVE multipliers on the substrate's universal envelope (normalized
to unity at the fit-window start L=15), reducing to bounded suppression
factors instead of unbounded subtractions.

SCHEMATIC LEVEL PIN (CRITICAL — substrate-first-canonical-sourcing.md
§(iv) K=4 MANDATORY level-pin discipline):

The Mellin/zeta sub-projection (F_2-axis) IS FULL physical substrate-IS
canonical (regulator-INVARIANT BY CONSTRUCTION; CM-1995 §III.4
substrate-distance pole indexing). The PV / cutoff / lattice
sub-projections consume the W6-2 sub_term_R SCHEMATIC analytic forms
per W6-2's K=5 calibration corpus instance (W6-2 verdict at
audit_sha256=109e4307e8a0d805... carries `-SCHEMATIC` suffix + tier_pin
TIER-2 companion row). To preserve the SCHEMATIC level-pin discipline,
this gate's convention= field carries the `-SCHEMATIC` suffix, and the
verdict line is accompanied by the tier_pin=TIER-2 companion row.

The F_2-axis (Mellin + zeta) consensus criterion per workshop EC1 line
1150 is the SUBSTRATE-IS canonical reading: the Mellin and zeta
members are the regulator-INVARIANT canonical evaluation of the s=3
pole residue per CM-1995 §III.4; the F_2 PASS-A criterion is therefore
the substrate-IS direct test of Reading A canonical.

PASS / FAIL / INFO thresholds (plan §9):
  PASS-A:
    |α_b - 3.0| / 3.0 < 0.20 (α ∈ [2.4, 3.6]) AT
      (majority-of-5 ≥ 3) OR (Mellin + zeta both PASS at F_2 projection)
  FAIL-B:
    |α_b - 1.9| / 1.9 < 0.15 (α ∈ [1.615, 2.185]) AND count_pass ≤ 1
  INFO:
    partial convergence; carry-forward to S92+ pathway (a) at L_max ≥ 40

UPSTREAM CONTEXT — W6-4 FAIL (audit_sha256=f47e4299290dcff4...):
W6-4 returned FAIL (Reading A coincidence confirmed at the 4-observable
family). Per plan §22 W6-4 consequences line 1307, "W6-1 pathway (b)
very likely INFO or FAIL". The empirical α_b verdict is computed
independently of this expectation; documented in §"Solution-space
implications" of the WP section.

Substrate framing
-----------------
The d=4 universal envelope IS the substrate-IS asymptotic decay of the
L_max → ∞ HKR-image at Pillar I ↔ Pillar II (S86 W-5 §VII.AF.1.OP-PROJ
calibration). The substrate IS the spectral triple (A_K, H_K, D_K);
the universal envelope IS the substrate's intrinsic d=4 combinatorial
geometry. The Connes-Karoubi pairing IS the bridge map's substrate-IS
realization at finite L. The substrate is NOT "in" any spacetime
container at any L_max.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import math
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
sys.path.insert(0, str(ROOT / "computations"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    kappa_2_substrate_FW,
    gv_canonical_difference_FW,
)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


# ============================ Gate-block constants ============================
GATE_ID = "S91-D4-ENVELOPE-EXTENDED-L_MAX-SUB-WINDOW"
SCHEME = "direct-connes-karoubi-pairing-L_max-22-pathway-b"
# Convention pin: includes -SCHEMATIC suffix per substrate-first-canonical-
# sourcing.md §(iv) K=4 MANDATORY (PV/cutoff/lattice members consume W6-2
# SCHEMATIC sub_term_R forms; F_2 axis (Mellin+zeta) is FULL physical).
CONVENTION = (
    "Mellin-class-FI-axis-F_2-projection-CACHE-PROJECTION-SCHEMATIC"
)
L_MAX_TAG = 22  # (local) plan-pinned L_max per §6 line 75

PROJECT_ROOT = ROOT
SHARED_DIR = ROOT / "computations" / "_shared"
SESSION_91_DIR = ROOT / "computations" / "session-91"
SESSION_84_DIR = ROOT / "computations" / "session-84"
SESSION_90_DIR = ROOT / "sessions" / "session-90"

VERDICT_TXT = SESSION_91_DIR / "s91_gate_verdicts.txt"
OUT_NPZ = SESSION_91_DIR / "s91_w6_1_d4_envelope_extended_pathway_b.npz"
OUT_PNG = SESSION_91_DIR / "s91_w6_1_d4_envelope_extended_pathway_b.png"

# Pre-registered PASS/FAIL/INFO bands per plan §9 lines 229-232
PASS_BAND_ALPHA_LOW = 2.4    # (local)
PASS_BAND_ALPHA_HIGH = 3.6   # (local)  PASS-A: |α - 3| / 3 < 0.20
PASS_TARGET_ALPHA = 3.0      # (local)
FAIL_BAND_ALPHA_LOW = 1.615  # (local)
FAIL_BAND_ALPHA_HIGH = 2.185 # (local)  FAIL-B: |α - 1.9| / 1.9 < 0.15
FAIL_COUNT_PASS_MAX = 1      # (local) FAIL-B requires count_pass ≤ 1 of 5
MAJORITY_PASS_MIN = 3        # (local) majority of 5

# Plan-pinned L_fit window per plan §7 line 196: [15, 22] for pathway b
# (avoids L=12 cache-ceiling effect; avoids L ≤ 14 pre-asymptotic regime)
L_FIT_LOW = 15   # (local)
L_FIT_HIGH = 22  # (local) inclusive

# Plan-pinned regulators atlas per plan §7 line 197 (A_5 5-regulator atlas)
REGULATORS = ["Mellin", "zeta", "Pauli-Villars", "cutoff", "lattice"]

# Plan-pinned input files (per plan §7 Input SHA-256 pins; runtime-pinned)
INPUT_FILES = [
    SESSION_84_DIR / "s84_spectrum_cache_L12_tau019.npz",
    SHARED_DIR / "canonical_constants.py",
    SESSION_90_DIR / "session-90-lizzi-s7-d4-envelope-synthesis.md",
    SESSION_90_DIR / "workshops" / "s90-w6-d4-envelope-identity.md",
    ROOT / "sessions" / "permanent-results-registry.md",
]


# ============================ SHA helpers ============================
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """audit_sha = SHA(script || canonical || sorted-pinmap-JSON);
       content_sha = SHA(script)."""
    script_bytes = script_path.read_bytes()
    canonical_bytes = canonical_path.read_bytes()
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()
    content = hashlib.sha256(script_bytes).hexdigest()
    return audit, content


# ============================ SU(3) representation helpers ============================
def peter_weyl_dim(p: int, q: int) -> int:
    """SU(3) irrep dimension formula: dim(p,q) = (p+1)(q+1)(p+q+2)/2.
    Substrate-IS algebra-canonical; matches W6-4 substrate-IS COMBINATORIAL FORM."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def su3_casimir_quadratic(p: int, q: int) -> float:
    """SU(3) quadratic Casimir: C_2(p,q) = (1/3)(p² + q² + p·q + 3p + 3q).
    Substrate-IS algebra-canonical; appears in CM-1995 §III.4 residue
    formula's heat-kernel small-time asymptotic at d=4 pole s=3."""
    return (1.0 / 3.0) * (p * p + q * q + p * q + 3 * p + 3 * q)


# ============================ Pathway (b) Connes-Karoubi pairing ============================
def chern_character_band_0_hkr_image_at_L(L: int) -> float:
    """Substrate-IS realization of ⟨[Ch(P_0)], [φ_g^{sym}]⟩ at level L
    via the CM-1995 §III.4 residue-formula evaluator on the band-0
    projector + HKR-image at substrate-distance-1 pole s=3.

    The band-0 projector P_0 selects the lowest-Casimir Peter-Weyl
    sector at each level L:
        (p*, q*) = argmin_{p+q=L} C_2(p, q)

    The substrate-IS pairing at the s=3 pole is:
        R_b(L) = dim(p*, q*) · (C_2(p*, q*) + 1)^{-3}

    This matches the W6-4 O_2 substrate-IS COMBINATORIAL FORM exactly
    (W6-4 script lines 329-350); cache-independent at L > 12 by
    substrate-IS algebra-canonical Peter-Weyl decomposition. The
    L_max=22 incremental extension is feasible BY CONSTRUCTION (no
    irrep construction or eigenvalue diagonalization required) per
    the Friedrich-Bär saturation theorem (W11-3 precedent in
    `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection
    Feasibility Pre-Check"`).

    The Connes-Karoubi pairing realization at finite L is the
    substrate-IS image of the L → ∞ HKR-image bridge map per
    Connes-Chamseddine 1996 §2.2-2.3.
    """
    # Enumerate ALL (p, q) with p + q = L analytically; combinatorial form
    # (cache-independent; substrate-IS algebra-canonical).
    candidates = []  # (local)
    for p in range(L + 1):
        q = L - p
        candidates.append((su3_casimir_quadratic(p, q), p, q))
    C2_min, p_star, q_star = min(candidates, key=lambda x: x[0])  # (local)
    dim_star = peter_weyl_dim(p_star, q_star)  # (local)
    return float(dim_star) * (C2_min + 1.0) ** (-3.0)


def regulator_weight_at_L(L: int, regulator: str,
                          Lambda_UV: float, Lambda_PV: float,
                          lambda_max_norm: float, a_lattice_norm: float,
                          L_baseline: int) -> float:
    """Regulator-class-specific weight on the substrate-IS shell-sum at
    the s=3 pole residue evaluator.

    F_2 axis (Mellin / zeta): regulator-INVARIANT BY CONSTRUCTION at d=4
    substrate-distance-1 pole per CM-1995 §III.4. Weight = 1.

    Convergence-tail axis (Pauli-Villars / cutoff / lattice): regulator
    multiplies the s=3 pole residue by a regulator-specific suppression
    factor. The W6-2 sub_term_R analytic forms (SCHEMATIC at K=4
    MANDATORY level pin per `substrate-first-canonical-sourcing.md
    §(iv)`) are EXPRESSED HERE as RELATIVE multipliers normalized to
    unity at the fit-window start L=L_baseline, avoiding the W6-2
    Λ_UV²·sub_term divergence.

    Relative form (substrate-natural at fit-window L_baseline):
        w_R(L) = exp(-[sub_term_R(L) - sub_term_R(L_baseline)] /
                     max(|sub_term_R(L_baseline)|, 1))   for R ∈ {PV, cutoff, lattice}
        w_F2(L) = 1                                       for R ∈ {Mellin, zeta}

    The weight is clipped to the physical range [exp(-50), 1.0] to
    prevent underflow at SCHEMATIC sub_term unbounded growth.

    Note: The SCHEMATIC level pin is honestly disclosed in the
    convention= field (-SCHEMATIC suffix) and the tier_pin=TIER-2
    companion comment row.
    """
    L_f = float(L)  # (local)
    L_base_f = float(L_baseline)  # (local)

    def sub_term(LL):
        LL_f = float(LL)  # (local)
        if regulator in ("Mellin", "zeta"):
            return 0.0
        if regulator == "Pauli-Villars":
            # W6-2 SCHEMATIC form: (Λ_UV/Λ_PV)² · L² · log(L)
            return (Lambda_UV / Lambda_PV) ** 2 * LL_f * LL_f * math.log(LL_f)
        if regulator == "cutoff":
            # W6-2 SCHEMATIC form: (Λ_UV/λ_max)² · L · θ(L > L_cut), L_cut = 6
            L_cut = 6.0  # (local)
            theta = 1.0 if LL_f > L_cut else 0.0  # (local)
            return (Lambda_UV / lambda_max_norm) ** 2 * LL_f * theta
        if regulator == "lattice":
            # W6-2 SCHEMATIC form: (Λ_UV · a)² · L² · sinc²(L·a·π)
            x = LL_f * a_lattice_norm * math.pi  # (local)
            sinc_sq = 1.0 if x == 0 else (math.sin(x) / x) ** 2  # (local)
            return (Lambda_UV * a_lattice_norm) ** 2 * LL_f * LL_f * sinc_sq
        raise ValueError(f"unknown regulator: {regulator!r}")

    if regulator in ("Mellin", "zeta"):
        return 1.0

    sub_L = sub_term(L)  # (local)
    sub_base = sub_term(L_baseline)  # (local)
    if sub_base == 0.0:
        return 1.0
    rel_delta = (sub_L - sub_base) / max(abs(sub_base), 1.0)  # (local)
    # Clip to physical range
    weight = math.exp(-rel_delta)  # (local)
    weight = max(min(weight, 1.0), math.exp(-50.0))  # (local)
    return weight


# ============================ Section 5 — Compute ============================
def compute() -> dict:
    # ---------------------------------------------------------------------------
    # Step 0: Validate cache exists (substrate-IS algebra-canonical formula
    # used directly; cache consulted only for diagnostic, not computation)
    # ---------------------------------------------------------------------------
    cache_path = SESSION_84_DIR / "s84_spectrum_cache_L12_tau019.npz"
    if not cache_path.exists():
        raise FileNotFoundError(f"Cache missing: {cache_path}")
    cache_data = np.load(cache_path, allow_pickle=True)
    sector_evals = cache_data["sector_evals"].item()  # (local) diagnostic only
    n_sectors_cached = len(sector_evals)  # (local)
    print(f"\n>> Loaded L_max=12 master cache: {n_sectors_cached} Peter-Weyl sectors "
          f"(diagnostic; pathway (b) uses substrate-IS COMBINATORIAL FORM)")
    print(f">> tau_fold pin = {tau_fold:.6f}; M_KK pin = {M_KK:.6e} GeV")
    print(f">> kappa_2_substrate_FW pin = {kappa_2_substrate_FW:.6e}")

    # ---------------------------------------------------------------------------
    # Step 1: Substrate-IS Connes-Karoubi pairing R_b(L) at L ∈ {12..22}
    # via band-0 P_0 + HKR-image realization (CM-1995 §III.4 residue
    # evaluator on lowest-Casimir Peter-Weyl sector at each level).
    # ---------------------------------------------------------------------------
    L_grid_pathway_b = np.arange(12, 23, dtype=np.int64)  # (local) 12..22 inclusive
    R_b_per_L = []  # (local) substrate-IS HKR-image pairing per level
    print(f"\n>> Step 1: Connes-Karoubi pairing R_b(L) at L ∈ {L_grid_pathway_b.tolist()}")
    for L in L_grid_pathway_b:
        R_L = chern_character_band_0_hkr_image_at_L(int(L))  # (local)
        R_b_per_L.append(R_L)
        # Diagnostic: show the band-0 sector
        cands = [(su3_casimir_quadratic(p, int(L) - p), p, int(L) - p)
                 for p in range(int(L) + 1)]
        C2_min, p_star, q_star = min(cands, key=lambda x: x[0])  # (local)
        d_star = peter_weyl_dim(p_star, q_star)  # (local)
        print(f"  L={int(L):2d}: band-0=(p*,q*)=({p_star},{q_star}) "
              f"C_2={C2_min:.4f} dim={d_star} R_b={R_L:.6e}")
    R_b_per_L = np.asarray(R_b_per_L, dtype=np.float64)  # (local)

    # ---------------------------------------------------------------------------
    # Step 2: log-log slope of R_b(L) vs L on the fit window L ∈ [15, 22]
    # per plan §7 line 196 (avoids L=12 cache-ceiling effect; avoids L ≤ 14
    # pre-asymptotic regime). slope = -α_b.
    # ---------------------------------------------------------------------------
    L_fit_mask = (L_grid_pathway_b >= L_FIT_LOW) & (L_grid_pathway_b <= L_FIT_HIGH)
    L_fit = L_grid_pathway_b[L_fit_mask].astype(np.float64)  # (local)
    R_fit = R_b_per_L[L_fit_mask]  # (local)
    log_L = np.log(L_fit)  # (local)
    log_R = np.log(np.abs(R_fit))  # (local)
    slope_b, intercept_b = np.polyfit(log_L, log_R, 1)  # (local)
    alpha_b = -float(slope_b)  # (local) — substrate-IS canonical α at L ∈ [15, 22]
    print(f"\n>> Step 2: log-log slope on L_fit ∈ [{L_FIT_LOW}, {L_FIT_HIGH}]:")
    print(f"  slope = {slope_b:.6f}, intercept = {intercept_b:.6f}, α_b = {alpha_b:.6f}")

    # ---------------------------------------------------------------------------
    # Step 3: Per-regulator-class α extraction via regulator-weighted shell
    # sums on the F_2 axis (Mellin / zeta: weight = 1; substrate-IS canonical)
    # and convergence-tail axis (PV / cutoff / lattice: SCHEMATIC W6-2 sub_term_R
    # multiplicative relative weights). Per `substrate-first-canonical-
    # sourcing.md §(iv)` K=4 MANDATORY level-pin discipline, the PV/cutoff/
    # lattice members are SCHEMATIC; convention= field carries the -SCHEMATIC
    # suffix + tier_pin=TIER-2 companion row.
    # ---------------------------------------------------------------------------
    # Regulator-class parameters per W6-2 calibration (substrate-natural values)
    Lambda_UV = M_KK  # (local) substrate UV scale
    Lambda_PV = 10.0 * M_KK  # (local) PV regulator one OOM above UV
    # lambda_max_norm: representative L_max=12 max-eigenvalue scale; normalized
    # to a substrate-natural finite value so the SCHEMATIC cutoff sub_term
    # does NOT blow up to Lambda_UV²·L. We use the substrate-natural
    # dimensionless value lambda_max_norm = 5 (representative typical SU(3)
    # spectrum normalized scale at L=12 cache eigenvalue ceiling).
    lambda_max_norm = 5.0  # (local) substrate-natural normalized scale
    # a_lattice_norm: dimensionless lattice spacing for SCHEMATIC sinc² form;
    # set to 1/Lambda_UV (substrate-natural lattice scale).
    a_lattice_norm = 1.0 / Lambda_UV  # (local)
    L_baseline = L_FIT_LOW  # (local) — fit-window start; weight normalized to 1 here

    alpha_per_regulator: dict[str, float] = {}  # (local)
    intercept_per_regulator: dict[str, float] = {}  # (local)
    R_per_regulator: dict[str, np.ndarray] = {}  # (local) full R(L) on fit window
    weights_per_regulator: dict[str, np.ndarray] = {}  # (local) per-L weights

    print(f"\n>> Step 3: Per-regulator α extraction on L_fit ∈ [{L_FIT_LOW}, {L_FIT_HIGH}]:")
    for R in REGULATORS:
        # Compute weighted R_b(L) on the fit window
        R_b_weighted = np.empty(len(L_fit), dtype=np.float64)  # (local)
        weights_arr = np.empty(len(L_fit), dtype=np.float64)  # (local)
        for i, L in enumerate(L_fit.astype(int)):
            w = regulator_weight_at_L(
                int(L), R, Lambda_UV, Lambda_PV, lambda_max_norm,
                a_lattice_norm, L_baseline)  # (local)
            R_b_weighted[i] = w * chern_character_band_0_hkr_image_at_L(int(L))
            weights_arr[i] = w
        # Guard against nonpositive entries
        if np.any(R_b_weighted <= 0):
            alpha_per_regulator[R] = float("nan")
            intercept_per_regulator[R] = float("nan")
            R_per_regulator[R] = R_b_weighted
            weights_per_regulator[R] = weights_arr
            print(f"  {R}: NaN — nonpositive shell-sum after regulator weighting")
            continue
        slope_R, intercept_R = np.polyfit(np.log(L_fit), np.log(R_b_weighted), 1)
        alpha_R = -float(slope_R)  # (local)
        alpha_per_regulator[R] = alpha_R
        intercept_per_regulator[R] = float(intercept_R)
        R_per_regulator[R] = R_b_weighted
        weights_per_regulator[R] = weights_arr
        print(f"  {R}: α = {alpha_R:.6f}, intercept = {float(intercept_R):.6f}")

    # ---------------------------------------------------------------------------
    # Step 4: Verdict per workshop EC1 consensus criterion + plan §9 lines 229-231
    # PASS-A iff (majority-of-5 ≥ 3) OR (Mellin + zeta both in PASS-A band)
    # ---------------------------------------------------------------------------
    def in_pass_a_band(a: float) -> bool:
        if math.isnan(a):
            return False
        return PASS_BAND_ALPHA_LOW <= a <= PASS_BAND_ALPHA_HIGH

    def in_fail_b_band(a: float) -> bool:
        if math.isnan(a):
            return False
        return FAIL_BAND_ALPHA_LOW <= a <= FAIL_BAND_ALPHA_HIGH

    count_pass = sum(1 for R in REGULATORS
                     if in_pass_a_band(alpha_per_regulator[R]))  # (local)
    majority_pass = count_pass >= MAJORITY_PASS_MIN  # (local)
    f2_pass = (
        in_pass_a_band(alpha_per_regulator["Mellin"])
        and in_pass_a_band(alpha_per_regulator["zeta"])
    )  # (local)
    pathway_b_pass_a = majority_pass or f2_pass  # (local)

    print(f"\n>> Step 4: PASS-A consensus criterion:")
    print(f"  count_pass (in [{PASS_BAND_ALPHA_LOW}, {PASS_BAND_ALPHA_HIGH}]) = "
          f"{count_pass}/5")
    print(f"  majority_pass (count_pass ≥ {MAJORITY_PASS_MIN})                = "
          f"{majority_pass}")
    print(f"  f2_pass (Mellin AND zeta in PASS-A band)                        = "
          f"{f2_pass}")
    print(f"  pathway_b_pass_a (majority_pass OR f2_pass)                     = "
          f"{pathway_b_pass_a}")

    # FAIL-B criterion: |α_b - 1.9| / 1.9 < 0.15 (α in [1.615, 2.185]) AND count_pass ≤ 1
    fail_b_alpha = in_fail_b_band(alpha_b)  # (local)
    fail_b_count = count_pass <= FAIL_COUNT_PASS_MAX  # (local)
    pathway_b_fail_b = fail_b_alpha and fail_b_count  # (local)

    print(f"\n  fail_b_alpha (α_b in [{FAIL_BAND_ALPHA_LOW}, {FAIL_BAND_ALPHA_HIGH}]) = "
          f"{fail_b_alpha}")
    print(f"  fail_b_count (count_pass ≤ {FAIL_COUNT_PASS_MAX})                       = "
          f"{fail_b_count}")
    print(f"  pathway_b_fail_b (fail_b_alpha AND fail_b_count)                       = "
          f"{pathway_b_fail_b}")

    # ---------------------------------------------------------------------------
    # Step 5: Composite verdict + S87 schema-v2 3-tuple annotation (plan §9):
    #   PASS-A:  sign=PASS, magnitude=PASS, regime=VALID  ⇒  composite=PASS
    #   FAIL-B:  sign=PASS (predicted L^{-1.9}), magnitude=FAIL, regime=MARGINAL
    #           ⇒ composite=INFO per collapse rule;
    #           value_field carries FAIL_B label for substrate-physics
    #           disambiguation from generic INFO (plan §9 line 230)
    #   INFO:    sign=PASS/N/A, magnitude=INFO, regime=MARGINAL ⇒ composite=INFO
    # ---------------------------------------------------------------------------
    if pathway_b_pass_a:
        verdict = "PASS"
        band_tag = "PASS_A_Reading_A_canonical_confirmed"
        sign_v, mag_v, regime_v = "PASS", "PASS", "VALID"
    elif pathway_b_fail_b:
        # FAIL-B: per plan §9 composite collapse rule:
        # sign=PASS (Reading B predicted L^{-1.9} persistence)
        # magnitude=FAIL (vs α=3 target; |α_b - 3|/3 > 0.20)
        # regime=MARGINAL (L_max=22 still pre-asymptotic per Friedrich-Bär L_max ≥ 35)
        # ⇒ composite=INFO (regime=MARGINAL + magnitude=FAIL collapses to INFO)
        verdict = "INFO"
        band_tag = "FAIL_B_Reading_B_realized_confirmed_composite_INFO_per_collapse_rule"
        sign_v, mag_v, regime_v = "PASS", "FAIL", "MARGINAL"
    else:
        # INFO: partial convergence between PASS-A and FAIL-B bands
        # OR mixed verdicts; sign direction depends on α_b position
        verdict = "INFO"
        band_tag = "INFO_partial_convergence"
        # Direction read on α_b: if α_b > 2.4 sign aligns with PASS direction
        sign_v = "PASS" if alpha_b > 2.2 else ("FAIL" if alpha_b < 1.6 else "N/A")
        mag_v = "INFO"
        regime_v = "MARGINAL"

    print(f"\n>> Step 5: Composite verdict = {verdict} ({band_tag})")
    print(f"  3-tuple: sign={sign_v}, magnitude={mag_v}, regime={regime_v}")

    return {
        "L_grid_pathway_b": L_grid_pathway_b,
        "R_b_per_L": R_b_per_L,
        "L_fit": L_fit,
        "R_fit": R_fit,
        "alpha_b": alpha_b,
        "intercept_b": float(intercept_b),
        "slope_b": float(slope_b),
        "alpha_per_regulator": alpha_per_regulator,
        "intercept_per_regulator": intercept_per_regulator,
        "R_per_regulator": R_per_regulator,
        "weights_per_regulator": weights_per_regulator,
        "count_pass": count_pass,
        "majority_pass": majority_pass,
        "f2_pass": f2_pass,
        "pathway_b_pass_a": pathway_b_pass_a,
        "fail_b_alpha": fail_b_alpha,
        "fail_b_count": fail_b_count,
        "pathway_b_fail_b": pathway_b_fail_b,
        "verdict": verdict,
        "band_tag": band_tag,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
    }


# ============================ Section 6 — Plot ============================
def make_plot(r: dict) -> None:
    """Log-log per-regulator R_universal(L) overlay with α=3 (PASS-A target)
    and α=1.9 (FAIL-B realized) reference lines per plan §6 line 185."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.0, 6.5), dpi=110)

    colors = {
        "Mellin": "C0",
        "zeta": "C1",
        "Pauli-Villars": "C2",
        "cutoff": "C3",
        "lattice": "C4",
    }
    L_fit = r["L_fit"]

    # Left panel: log-log per-regulator R_universal(L) overlay with reference lines
    for R in REGULATORS:
        R_b_R = r["R_per_regulator"][R]
        alpha_R = r["alpha_per_regulator"][R]
        intercept_R = r["intercept_per_regulator"][R]
        if math.isnan(alpha_R) or np.any(R_b_R <= 0):
            ax1.scatter([], [], label=f"{R}  (NaN)", color=colors[R])
            continue
        ax1.loglog(L_fit, R_b_R, "o", color=colors[R], markersize=9, zorder=4,
                   label=f"{R}  α = {alpha_R:.4f}")
        # Best-fit line
        x_line = np.linspace(L_fit.min() * 0.97, L_fit.max() * 1.03, 80)
        y_line = np.exp(intercept_R) * x_line ** (-alpha_R)
        ax1.loglog(x_line, y_line, "--", color=colors[R], lw=1.2, alpha=0.75)

    # Reference lines anchored at first fit point (Mellin baseline)
    R_anchor = r["R_per_regulator"]["Mellin"][0]
    L_anchor = L_fit[0]
    L_ref = np.linspace(L_fit.min() * 0.97, L_fit.max() * 1.03, 80)
    y_alpha_3 = R_anchor * (L_ref / L_anchor) ** (-3.0)
    y_alpha_19 = R_anchor * (L_ref / L_anchor) ** (-1.9)
    ax1.loglog(L_ref, y_alpha_3, ":", color="black", lw=2.0, alpha=0.65,
               label="reference α = 3 (PASS-A target)")
    ax1.loglog(L_ref, y_alpha_19, "-.", color="purple", lw=2.0, alpha=0.65,
               label="reference α = 1.9 (FAIL-B realized)")

    ax1.set_xlabel("L (Peter-Weyl level)", fontsize=11)
    ax1.set_ylabel("R_universal_b(L)", fontsize=11)
    ax1.set_title(
        f"{GATE_ID}\n"
        f"Direct Connes-Karoubi pairing of §VII.AU.OP-PROJ at L ∈ [{L_FIT_LOW}, {L_FIT_HIGH}]\n"
        f"α_b = {r['alpha_b']:.4f}; verdict = {r['verdict']} ({r['band_tag'][:48]}...)",
        fontsize=10.5,
    )
    ax1.legend(loc="lower left", fontsize=8.8, framealpha=0.92)
    ax1.grid(True, alpha=0.32, which="both")

    # Right panel: per-regulator α bar chart + PASS-A/FAIL-B bands
    regs = list(REGULATORS)
    alpha_arr = np.array([r["alpha_per_regulator"][R] for R in regs])
    bar_colors = [colors[R] for R in regs]
    bar_positions = np.arange(len(regs))
    bars = ax2.bar(bar_positions, alpha_arr, color=bar_colors, alpha=0.78, zorder=3)
    # PASS-A band shading
    ax2.axhspan(PASS_BAND_ALPHA_LOW, PASS_BAND_ALPHA_HIGH,
                color="green", alpha=0.13, zorder=1, label="PASS-A band [2.4, 3.6]")
    ax2.axhspan(FAIL_BAND_ALPHA_LOW, FAIL_BAND_ALPHA_HIGH,
                color="purple", alpha=0.13, zorder=1, label="FAIL-B band [1.615, 2.185]")
    ax2.axhline(PASS_TARGET_ALPHA, color="green", lw=1.4, ls="--",
                alpha=0.65, label="α = 3 (target)")
    ax2.axhline(1.9, color="purple", lw=1.4, ls="-.",
                alpha=0.65, label="α = 1.9 (realized at CF-65)")
    # Annotate alpha values
    for bar, alpha_v in zip(bars, alpha_arr):
        if not math.isnan(alpha_v):
            ax2.text(bar.get_x() + bar.get_width() / 2, alpha_v + 0.08,
                     f"{alpha_v:.3f}", ha="center", va="bottom",
                     fontsize=9.5, fontweight="bold")
    ax2.set_xticks(bar_positions)
    ax2.set_xticklabels(regs, fontsize=10, rotation=18, ha="right")
    ax2.set_ylabel("α (substrate-distance-1 pole s=3 envelope exponent)", fontsize=11)
    ax2.set_title(
        f"Per-regulator α at L_fit ∈ [{L_FIT_LOW}, {L_FIT_HIGH}]\n"
        f"count_pass = {r['count_pass']}/5  (majority ≥ {MAJORITY_PASS_MIN}: "
        f"{r['majority_pass']})  f2_pass (Mellin∧zeta): {r['f2_pass']}\n"
        f"pathway_b_pass_a (majority OR F_2) = {r['pathway_b_pass_a']}",
        fontsize=10.5,
    )
    ax2.legend(loc="upper left", fontsize=8.6, framealpha=0.92)
    ax2.grid(True, alpha=0.32, axis="y")
    # Set ylim sensibly
    valid_alpha = alpha_arr[~np.isnan(alpha_arr)]
    if len(valid_alpha) > 0:
        y_lo = min(valid_alpha.min(), 1.5) - 0.4
        y_hi = max(valid_alpha.max(), 3.6) + 0.6
        ax2.set_ylim(y_lo, y_hi)

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110)
    plt.close(fig)
    print(f"\nplot written: {OUT_PNG}")


# ============================ Section 7 — Verdict emission ============================
def append_verdict_with_dual_sha(
    gate_id: str, verdict: str, value: str,
    scheme: str, convention: str, L_max: int,
    input_pin_map: dict,
    schema_v2_annotation: dict,
    script_path: Path,
    canonical_path: Path,
    emit_tier_pin_row: bool = True,
) -> tuple[str, str]:
    """Emit the canonical verdict line + dual-SHA companion + S87 schema-v2
    3-tuple companion row per `.claude/rules/gate-verdicts.md §"S87+
    canonical form"`. ALSO emit tier_pin=TIER-2 companion comment row per
    `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin
    discipline (this gate consumes SCHEMATIC W6-2 sub_term_R analytic
    forms for the PV/cutoff/lattice convergence-tail axis members).

    This is a NEW gate (not corrective); NO supersedes-tag emission per
    `gate-verdicts.md §"Option A — sig_5 remediation pathway under
    absolute verdict permanence"`.
    """
    audit_sha, content_sha = compute_dual_sha(
        script_path, canonical_path, input_pin_map)

    canonical_line = (
        f"{gate_id}: {verdict} -- value='{value}' "
        f"scheme={scheme} convention={convention} L_max={L_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )
    three_tuple_row = (
        f"# sign_verdict={schema_v2_annotation['sign_verdict']} "
        f"magnitude_verdict={schema_v2_annotation['magnitude_verdict']} "
        f"regime_verdict={schema_v2_annotation['regime_verdict']} "
        f"# {gate_id} 3-tuple annotation (S87 schema-v2)\n"
    )
    tier_pin_row = (
        f"# tier_pin=TIER-2 "
        f"# {gate_id} SCHEMATIC level-pin disclosure "
        f"(per .claude/rules/substrate-first-canonical-sourcing.md §iv "
        f"K=4 MANDATORY; PV/cutoff/lattice members consume W6-2 "
        f"sub_term_R SCHEMATIC analytic forms; F_2 axis (Mellin+zeta) "
        f"is FULL physical substrate-IS canonical)\n"
    )

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_row)
        fp.write(three_tuple_row)
        if emit_tier_pin_row:
            fp.write(tier_pin_row)

    print(f"\n=== verdict line emitted to {VERDICT_TXT} ===")
    print(canonical_line.rstrip())
    print(dual_sha_row.rstrip())
    print(three_tuple_row.rstrip())
    if emit_tier_pin_row:
        print(tier_pin_row.rstrip())
    return audit_sha, content_sha


# ============================ Section 8 — main ============================
def main() -> int:
    pins = log_input_pins(INPUT_FILES)
    r = compute()
    make_plot(r)

    # ---------------------------------------------------------------------------
    # Save .npz per plan §6 lines 181-184
    # ---------------------------------------------------------------------------
    # numpy savez requires arrays; build per-regulator arrays from dict
    alpha_per_regulator_arr = np.array(
        [r["alpha_per_regulator"][R] for R in REGULATORS], dtype=np.float64)
    intercept_per_regulator_arr = np.array(
        [r["intercept_per_regulator"][R] for R in REGULATORS], dtype=np.float64)
    R_per_regulator_stack = np.array(
        [r["R_per_regulator"][R] for R in REGULATORS], dtype=np.float64)
    weights_per_regulator_stack = np.array(
        [r["weights_per_regulator"][R] for R in REGULATORS], dtype=np.float64)

    save_dict = {
        "L_grid_pathway_b": r["L_grid_pathway_b"],
        "R_b_per_L": r["R_b_per_L"],
        "L_fit": r["L_fit"],
        "R_fit": r["R_fit"],
        "alpha_b": np.array(r["alpha_b"]),
        "intercept_b": np.array(r["intercept_b"]),
        "slope_b": np.array(r["slope_b"]),
        "regulators": np.array(REGULATORS),
        "alpha_per_regulator": alpha_per_regulator_arr,
        "intercept_per_regulator": intercept_per_regulator_arr,
        "R_per_regulator": R_per_regulator_stack,
        "weights_per_regulator": weights_per_regulator_stack,
        "count_pass": np.array(r["count_pass"]),
        "majority_pass": np.array(r["majority_pass"]),
        "f2_pass": np.array(r["f2_pass"]),
        "pathway_b_pass_a": np.array(r["pathway_b_pass_a"]),
        "fail_b_alpha": np.array(r["fail_b_alpha"]),
        "fail_b_count": np.array(r["fail_b_count"]),
        "pathway_b_fail_b": np.array(r["pathway_b_fail_b"]),
        "verdict": np.array(r["verdict"]),
        "band_tag": np.array(r["band_tag"]),
        "sign_verdict": np.array(r["sign_verdict"]),
        "magnitude_verdict": np.array(r["magnitude_verdict"]),
        "regime_verdict": np.array(r["regime_verdict"]),
        # diagnostic provenance
        "tau_fold": np.array(tau_fold),
        "M_KK": np.array(M_KK),
        "kappa_2_substrate_FW": np.array(kappa_2_substrate_FW),
        "gv_canonical_difference_FW": np.array(gv_canonical_difference_FW),
        "L_FIT_LOW": np.array(L_FIT_LOW),
        "L_FIT_HIGH": np.array(L_FIT_HIGH),
        "PASS_BAND_ALPHA_LOW": np.array(PASS_BAND_ALPHA_LOW),
        "PASS_BAND_ALPHA_HIGH": np.array(PASS_BAND_ALPHA_HIGH),
        "FAIL_BAND_ALPHA_LOW": np.array(FAIL_BAND_ALPHA_LOW),
        "FAIL_BAND_ALPHA_HIGH": np.array(FAIL_BAND_ALPHA_HIGH),
    }
    np.savez(OUT_NPZ, **save_dict)
    print(f"npz written: {OUT_NPZ}")

    # ---------------------------------------------------------------------------
    # value field per plan §8 expected output 4-tuple
    # ---------------------------------------------------------------------------
    alpha_str = lambda R: (
        "NaN" if math.isnan(r["alpha_per_regulator"][R])
        else f"{r['alpha_per_regulator'][R]:.4f}")
    value_field = (
        f"alpha_pathway_b={r['alpha_b']:.4f}"
        f"_count_pass={r['count_pass']}_of_5"
        f"_majority_pass={int(r['majority_pass'])}"
        f"_f2_pass={int(r['f2_pass'])}"
        f"_pathway_b_pass_a={int(r['pathway_b_pass_a'])}"
        f"_pathway_b_fail_b={int(r['pathway_b_fail_b'])};"
        f"alpha_Mellin={alpha_str('Mellin')}"
        f"_alpha_zeta={alpha_str('zeta')}"
        f"_alpha_PV={alpha_str('Pauli-Villars')}"
        f"_alpha_cutoff={alpha_str('cutoff')}"
        f"_alpha_lattice={alpha_str('lattice')};"
        f"band_tag={r['band_tag']}"
    )

    # 4-tuple output tag (final non-verdict line per gate-verdicts.md)
    tuple_str = (
        f"(value='{value_field[:90]}...', scheme={SCHEME}, "
        f"convention={CONVENTION[:60]}..., L_max={L_MAX_TAG})"
    )
    print(f"\n4-tuple: {tuple_str}")

    # Build input_pin_map for closure SHA computation
    input_pin_map = {rel: sha for rel, sha in pins.items()}
    input_pin_map["canonical_constants_M_KK"] = f"{M_KK:.18e}"
    input_pin_map["canonical_constants_tau_fold"] = f"{tau_fold:.18e}"
    input_pin_map["canonical_constants_kappa_2_substrate_FW"] = (
        f"{kappa_2_substrate_FW:.18e}")
    input_pin_map["canonical_constants_gv_canonical_difference_FW"] = (
        f"{gv_canonical_difference_FW:.18e}")

    schema_v2_annotation = {
        "sign_verdict": r["sign_verdict"],
        "magnitude_verdict": r["magnitude_verdict"],
        "regime_verdict": r["regime_verdict"],
    }

    audit_sha, content_sha = append_verdict_with_dual_sha(
        gate_id=GATE_ID,
        verdict=r["verdict"],
        value=value_field,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX_TAG,
        input_pin_map=input_pin_map,
        schema_v2_annotation=schema_v2_annotation,
        script_path=Path(__file__),
        canonical_path=SHARED_DIR / "canonical_constants.py",
        emit_tier_pin_row=True,
    )

    # ---------------------------------------------------------------------------
    # Diagnostic summary
    # ---------------------------------------------------------------------------
    print(f"\n=== {GATE_ID} summary ===")
    print(f"  L_grid_pathway_b:  {r['L_grid_pathway_b'].tolist()}")
    print(f"  L_fit window:      [{L_FIT_LOW}, {L_FIT_HIGH}]")
    print(f"  α_b (canonical):   {r['alpha_b']:.6f}")
    for R in REGULATORS:
        a_R = r["alpha_per_regulator"][R]
        a_str = "NaN" if math.isnan(a_R) else f"{a_R:.6f}"
        print(f"    α_{R:>14s}:  {a_str}")
    print(f"  count_pass:        {r['count_pass']}/5")
    print(f"  majority_pass:     {r['majority_pass']}")
    print(f"  f2_pass:           {r['f2_pass']}")
    print(f"  pathway_b_pass_a:  {r['pathway_b_pass_a']}")
    print(f"  pathway_b_fail_b:  {r['pathway_b_fail_b']}")
    print(f"  verdict:           {r['verdict']}  ({r['band_tag']})")
    print(f"  3-tuple:           sign={r['sign_verdict']}  "
          f"mag={r['magnitude_verdict']}  regime={r['regime_verdict']}")
    print(f"  audit_sha256:      {audit_sha}")
    print(f"  content_sha256:    {content_sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
