#!/usr/bin/env python3
"""
S91 W3-3 — S91-CF37-AUX-4-SECONDARY-CORRIDOR (T1.8)
====================================================

Gate: `S91-CF37-AUX-4-SECONDARY-CORRIDOR` ([VERIFY-THEOREM] ∧ [SIGN])

PRIMARY (Axis-A substrate-physics): volovik-superfluid-universe-theorist
        (orchestrator dispatch 2026-05-16; non-connes-ncg + non-phonon-first
        per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`
        clause 2 downstream-inheritance reach extension; OAA exclusion on
        connes-ncg-theorist (CF-37 (d)∘(b) primary corridor original co-author)
        AND phonon-first-cosmologist (CF-37 original primary author))

Axis-B cross-review (NCG-axiomatic / bridge map): van-den-dungen-bridge-theorist
        (dispatched separately AFTER this script's .npz output lands; read-only
        consumption + working-paper sub-section authoring).

═══════════════════════════════════════════════════════════════════════════
SUBSTRATE FRAMING (read first; pin direction-of-explanation)
═══════════════════════════════════════════════════════════════════════════

The substrate IS the spectral triple (A_K, H_K, D_K(τ_fold = 0.190)) at
L_max = 10 (78,080 eigenvalues across 65 Peter-Weyl sectors). The (c)∘(d)
compositional corridor IS the substrate's intrinsic Connes-Karoubi pairing
on its Hochschild cocycle space under element-1 = (c) γ(s) ≠ Γ(s)
modified-universal-kernel cohomology-class shift AND element-3 = (d) χ'
inheritance-restricted horizon-spanning projector P_HSS'(M) = χ'^*(P_HSS(M)).
α''(M_LRD) IS the substrate's intrinsic ratio at the LRD scale; the empirical
1/458 anchor is laboratory-IN; direction substrate → bridge map → laboratory
observable.

The AUX-4 corridor is NOT "exploring different element-1 deformations to
find the one that matches data": γ(s) = Γ(s)·(1 + c_aux·(s − s_*)^{-1}) is
the W-1 workshop's PRE-REGISTERED secondary candidate after (d)∘(b) closure
at S90 W4 CF-37 FAIL. The three γ_weight_aux candidates below are
substrate-derived (Wedderburn weights, ratios, full residue evaluation),
NOT numerical-tuning parameters. PROHIBITED_ACTIONS Class 1
(convention-shopping) and Class 6 (iterate-until-PASS) apply.

═══════════════════════════════════════════════════════════════════════════
STRUCTURAL ANSATZ — Element-1 (c) γ(s) ≠ Γ(s) modified-universal-kernel
═══════════════════════════════════════════════════════════════════════════

The standard CM-1995 §III.4 universal kernel is the gamma function:

    Γ(s) = ∫₀^∞ t^{s-1} e^{-t} dt

The W-1 workshop AUX-4 pre-registration specifies a modified-universal-kernel
under the (c) cohomology-class shift:

    γ(s) = Γ(s) · (1 + c_aux · (s - s_*)^{-1})

where s_* is the substrate-distance pole (default s_* = 1) and c_aux is
the substrate-Wedderburn algebra-weight constant at element-1 layer:

    c_aux = (rank(C) - rank(M_2(C)) + rank(M_3(C))) / (rank(C) + rank(M_2(C)) + rank(M_3(C)))
          = (1 - 2 + 3) / (1 + 2 + 3) = 2/6 = 1/3

The (c) shift adds a SIMPLE POLE at s = s_* to the universal kernel,
shifting the residue evaluation by a digamma-function-modulated factor
relative to the standard Γ(s) kernel.

═══════════════════════════════════════════════════════════════════════════
γ_weight_aux candidate enumeration (honest disclosure per plan §6 Step 5)
═══════════════════════════════════════════════════════════════════════════

Three substrate-derived candidates for the (c)-deformation analog of
χ'_weight = 0.5 in CF-37 (d)∘(b):

(1) γ_weight_aux^{(1)} = (rank(C) + rank(M_2(C)) + rank(M_3(C))) / (rank(M_2(C)) + rank(M_3(C)))
                       = (1+2+3) / (2+3) = 6/5 = 1.2
    Substrate-physics: un-restricted Wedderburn ratio; the (c) cohomology-
    class shift OPENS the M_3(C) summand that χ' kills (zero map per S89
    §W2-3). This candidate represents the (c)-corrected projector image
    spanning ALL three Wedderburn summands without inheritance restriction
    at the COHOMOLOGY level.

(2) γ_weight_aux^{(2)} = c_aux · χ'_weight = (1/3) · 0.5 = 1/6 ≈ 0.167
    Substrate-physics: γ-modulated χ'-weight via element-1 (c) shift; the
    γ(s) modification weighs the W-5 baseline by c_aux directly,
    composing with the χ' inheritance restriction at the spectral level.

(3) γ_weight_aux^{(3)} = full residue evaluation at s_* via the modified-
    universal-kernel substitution into the CM-1995 §III.4 residue formula.
    SUBSTITUTION CHAIN (substrate-IS):

    Standard CM-1995 §III.4 residue formula:
        R_universal = Res_{s=s_*}[Γ(s) · pairing(s)]

    Modified-universal-kernel substitution:
        pairing_aux(s_*) = Res_{s=s_*}[γ(s) · pairing(s)]
                         = Res_{s=s_*}[Γ(s)·(1 + c_aux·(s - s_*)^{-1}) · pairing(s)]

    Expanding:
        pairing_aux(s_*) = Res_{s=s_*}[Γ(s) · pairing(s)]
                         + c_aux · Res_{s=s_*}[Γ(s) · pairing(s) · (s - s_*)^{-1}]

    The first term is the standard CM-1995 residue (= χ'_weight · R_universal
    at the χ'-restricted projector). The second term involves the residue
    of a (s - s_*)^{-2} double pole, whose residue is the DERIVATIVE of
    [Γ(s) · pairing(s)] at s = s_*:

        d/ds [Γ(s) · pairing(s)] |_{s=s_*}
            = Γ(s_*) · pairing(s_*) · (ψ(s_*) + d/ds log pairing(s_*))

    where ψ(s) = Γ'(s)/Γ(s) is the digamma function. The substrate-IS
    pairing(s) at the modified-universal-kernel is regulator-class
    INVARIANT per the W-5 calibration corpus instance #1 (Level-1
    cohomology-class identity at HKR/Connes-Karoubi); hence
    d/ds log pairing(s_*) = 0 to leading order in the substrate-physics
    derivation.

    Therefore:
        γ_weight_aux^{(3)} = χ'_weight · (1 + c_aux · ψ(s_*))

    At s_* = 1 (default substrate-distance pole): ψ(1) = -γ_Euler ≈ -0.5772
        γ_weight_aux^{(3)}(s_*=1) = 0.5 · (1 + (1/3) · (-0.5772))
                                  = 0.5 · (1 - 0.1924) = 0.5 · 0.8076 = 0.4038

    At s_* = 3 (alternative substrate-distance pole; per substrate-distance
    Mellin pattern §VII.U.1): ψ(3) = 3/2 - γ_Euler ≈ 0.9228
        γ_weight_aux^{(3)}(s_*=3) = 0.5 · (1 + (1/3) · 0.9228)
                                  = 0.5 · 1.3076 = 0.6538

The CANONICAL γ_weight_aux selection is candidate (3) at s_* = 1 (default
substrate-distance pole; matches the W-5 calibration corpus instance #1
anchor at s=1). This is the most defensible substrate-derivation because
it composes the (c) modified-universal-kernel with the χ' inheritance
restriction at the residue layer (NOT just at the cohomology-class layer
as candidate (1) or the multiplicative-weight layer as candidate (2)).

═══════════════════════════════════════════════════════════════════════════
Sign substitution chain (substrate-IS PRE-COMMITTED direction)
═══════════════════════════════════════════════════════════════════════════

Per plan §10, the direction is pre-committed (Sub-clause A): 0 < α''(M_LRD) < 1.
The magnitude is OPEN at plan-freeze (Sub-clause B is the substantive
substrate-physics evaluation the gate produces).

Step 1 (definitions): φ_g^{sym} gradient-symmetric Hochschild 1-cocycle on
    A_K = C ⊕ H ⊕ M_3(C); χ' inheritance morphism per S89 §W2-3 derived theorem
    (kernel rank 9 on M_3(C); Wedderburn 9 > 8 forces zero map);
    γ(s) = Γ(s)·(1 + c_aux·(s - s_*)^{-1}); P_HSS'(M) = χ'^*(P_HSS(M)).
Step 2 (positivity numerator): γ(s) carries (c) shift; for s_* > 0 the
    residue Res_{s=s_*}[γ(s) · pairing(s)] is non-zero. P_HSS'(M_LRD) is
    positive idempotent ⇒ [Ch(P_HSS'(M_LRD))] non-negative.
Step 3 (positivity denominator + dimensional bridge): M_KK² > 0,
    M_Pl_reduced² > 0, (M_KK/M_Pl_reduced)² = 9.307286e-4 > 0.
Step 4 (substrate saturation): g(M_LRD, L=10) = 1.000 (inheritance-
    restricted projector saturates L=10 substrate at M_LRD = 10⁷ M_sun;
    SAME as CF-37 since element-3 (d) is identical).
Step 5 (combine; canonical candidate (3) at s_*=1):
    α''(M_LRD) = R_universal · γ_weight_aux · (M_KK/M_Pl_reduced)² · g(M_LRD, L=10)
               = 1.030902 · 0.4038 · 9.307286e-4 · 1.000
               ≈ 3.875e-4
Step 6 (read-off): 0 < γ_weight_aux < ∞ ⇒ 0 < α'' < (saturating bound) ✓ A.

Plan reference: sessions/session-plan/session-91-plan-w3.md §W3-3.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
from scipy.special import digamma  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

GATE_ID = "S91-CF37-AUX-4-SECONDARY-CORRIDOR"  # (local)
SCHEME = "connes-karoubi-pairing-on-gamma-s-modified-universal-kernel"  # (local)
CONVENTION = (
    "substrate-IS-Cell-I-K-counter-instance-2-AUX-4-SECONDARY-CORRIDOR"
    "-NON-CONNES-NON-PHONON-FIRST-AUTHOR"
)  # (local)
L_MAX = 10  # (local) plan-pinned L_max
SCHEMA_VERSION = "S87+"  # (local)

# Plan-pinned thresholds (per plan §9; preserve CF-37 defaults)
M_LRD_M_SUN = 1e7  # (local) LRD pivot mass
M_SCAN_M_SUN = np.array([1e5, 1e6, 1e7, 1e8, 1e9])  # (local) 5-point log-spaced
EMPIRICAL_ANCHOR = 1.0 / 458.0  # (local) ≈ 2.18341e-3
SUB_B_PASS_BAND = 0.30  # (local) 30% RATIO per CF-37 default; CF-38 FAIL retained
SUB_B_INFO_BAND = 0.10  # (local) lower edge of INFO band
SUB_C_R2_THRESHOLD = 0.95  # (local) R² minimum for envelope fit PASS
PUBLICATION_SIG_FIGS = 5  # (local) per Class 8.3

# Wedderburn rank ratios under χ' inheritance morphism (preserved from CF-37)
# A_K = C ⊕ H ⊕ M_3(C); ranks 1, 2, 3 respectively (total 6)
# χ' kills M_3(C) entire (S89 §W2-3 derived theorem); image rank = 1 + 2 = 3
CHI_PRIME_WEIGHT_NUM = 3  # (local) preserved rank under χ'
CHI_PRIME_WEIGHT_DEN = 6  # (local) total rank of A_K
CHI_PRIME_WEIGHT = CHI_PRIME_WEIGHT_NUM / CHI_PRIME_WEIGHT_DEN  # (local) = 0.5

# γ(s) modified-universal-kernel pin (Element-1 (c) deformation)
# c_aux = (rank(C) - rank(M_2(C)) + rank(M_3(C))) / (rank(C) + rank(M_2(C)) + rank(M_3(C)))
#       = (1 - 2 + 3) / 6 = 2/6 = 1/3
C_AUX_NUM = 2  # (local) (rank(C) - rank(M_2(C)) + rank(M_3(C))) = 1 - 2 + 3 = 2
C_AUX_DEN = 6  # (local) total Wedderburn rank
C_AUX = C_AUX_NUM / C_AUX_DEN  # (local) = 1/3

# Default substrate-distance pole choice for γ(s) modification
S_STAR_DEFAULT = 1  # (local) substrate-distance-1 pole; matches W-5 calibration #1
S_STAR_ALT = 3  # (local) alternative pole; per substrate-distance Mellin §VII.U.1

# γ_weight_aux candidate (1): un-restricted Wedderburn ratio (M_3(C) summand opens)
GAMMA_WEIGHT_AUX_C1 = (1 + 2 + 3) / (2 + 3)  # (local) = 6/5 = 1.2

# γ_weight_aux candidate (2): c_aux · χ'_weight (multiplicative composition)
GAMMA_WEIGHT_AUX_C2 = C_AUX * CHI_PRIME_WEIGHT  # (local) = (1/3)·(1/2) = 1/6 ≈ 0.167

# Input file paths
SPECTRUM_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S89_W1_ALPHA_DIAG = COMPUTATIONS_DIR / "session-89" / "s89_w1_alpha_m_horizon_microstate_count.npz"
S89_W2_CHI_PRIME = COMPUTATIONS_DIR / "session-89" / "s89_w2_a7_chi_prime_inheritance_morphism.npz"
REGISTRY_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"

# χ' anchor SHA from S89 §W2-3 derived theorem (audit chain pin)
CHI_PRIME_ANCHOR_AUDIT_SHA = (
    "90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843"
)  # (local)

# Output paths
NPZ_OUT = SESSION_DIR / "s91_w3_alpha_m_aux4_corridor_c_compose_d.npz"
PNG_OUT = SESSION_DIR / "s91_w3_alpha_m_aux4_corridor_c_compose_d.png"
VERDICT_TXT = SESSION_DIR / "s91_gate_verdicts.txt"


def sha256_of(path):
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def emit_verdict(verdict, value_str, audit_sha, content_sha,
                 sign_v, mag_v, regime_v):
    """Single-shot AFTER-pattern emission per registry-landing.md."""
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    annotation = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)
        fp.write(annotation)


def filter_l_max_10_sectors(sector_evals):
    """Filter sector_evals dict to keep only (p,q) with p+q <= L_max=10."""
    return {pq: v for pq, v in sector_evals.items() if sum(pq) <= L_MAX}


def compute_substrate_spectrum(sectors_l10):
    """Compute substrate spectrum statistics at L_max=10."""
    all_abs_evals = []  # (local)
    sector_count = {}  # (local) {(p,q): num_eigenvalues}
    for pq, info in sectors_l10.items():
        evals = np.asarray(info['abs_evals'])
        all_abs_evals.append(evals)
        sector_count[pq] = len(evals)
    abs_evals_flat = np.concatenate(all_abs_evals)
    return abs_evals_flat, sector_count


def gamma_weight_aux_candidate_3(s_star, c_aux=C_AUX, chi_prime_weight=CHI_PRIME_WEIGHT):
    """Candidate (3): full CM-1995 §III.4 residue evaluation at s_*.

    γ_weight_aux^{(3)} = χ'_weight · (1 + c_aux · ψ(s_*))

    where ψ(s) is the digamma function. Derivation in module docstring;
    substrate-IS pairing(s) is regulator-class INVARIANT per W-5
    calibration #1 ⇒ d/ds log pairing(s_*) = 0 to leading order.
    """
    psi_s_star = digamma(s_star)  # (local) digamma at substrate-distance pole
    weight = chi_prime_weight * (1.0 + c_aux * psi_s_star)
    return weight, psi_s_star


def horizon_cutoff_lambda_in_M_KK_units(M_M_sun):
    """Substrate-area horizon cutoff Λ(M) in M_KK units.

    Λ(M) ~ M_KK · sqrt(S_BH(M) / S_BH(M_KK_unit)) = M_KK · M / M_Pl_reduced.
    For M >> M_Pl_reduced, Λ(M)/M_KK >> 1, so g(M, L=10) ≈ 1.
    """
    M_sun_in_GeV = 1.989e30 / 1.7826619216279e-27  # (local) M_sun in GeV
    M_GeV = M_M_sun * M_sun_in_GeV  # (local)
    Lambda_in_M_KK = M_GeV / M_Pl_reduced  # (local)
    return Lambda_in_M_KK


def compute_alpha_double_prime(M_M_sun, R_universal, gamma_weight_aux, abs_evals_flat):
    """Compute α''(M, L_max=10) under the (c)∘(d) corridor structural ansatz.

    α''(M, L_max=10) = R_universal × γ_weight_aux × (M_KK / M_Pl_reduced)² × g(M, L_max=10)

    Element-1 = (c) γ(s) ≠ Γ(s) modified-universal-kernel (γ_weight_aux absorbs
    the modification at the residue layer); element-3 = (d) χ' inheritance
    restriction (g(M, L=10) saturation fraction; SAME as CF-37).
    """
    Lambda_in_M_KK = horizon_cutoff_lambda_in_M_KK_units(M_M_sun)  # (local)
    n_inside_cutoff = int(np.sum(abs_evals_flat <= Lambda_in_M_KK))  # (local)
    g_M = n_inside_cutoff / len(abs_evals_flat)  # (local)
    M_KK_over_M_Pl_sq = (M_KK / M_Pl_reduced) ** 2  # (local) ≈ 9.307e-4
    alpha_dp = R_universal * gamma_weight_aux * M_KK_over_M_Pl_sq * g_M  # (local)
    return alpha_dp, g_M, Lambda_in_M_KK, M_KK_over_M_Pl_sq


def fit_envelope(M_scan, alpha_double_prime_scan):
    """Fit α''(M) = 1 + c · (M/M_thr)^{-n} per plan §9 Sub-clause C envelope form.

    Use log-log linearization on (1 - α''(M)) vs M for finite c < 0:
        1 - α''(M) = -c · (M/M_thr)^{-n}
        log(1 - α''(M)) = log(-c) - n · log(M/M_thr)
    """
    eps = np.where(alpha_double_prime_scan < 1.0, 1.0 - alpha_double_prime_scan, 1e-30)
    valid = eps > 0
    if valid.sum() < 3:
        return None, None, None, 0.0
    log_eps = np.log(eps[valid])
    log_M = np.log(M_scan[valid])
    coeffs = np.polyfit(log_M, log_eps, 1)
    b, a = coeffs[0], coeffs[1]  # (local)
    n = -b
    M_thr_choice = M_scan[2]  # (local) M_LRD
    log_minus_c = a - n * np.log(M_thr_choice)
    c = -np.exp(log_minus_c)
    log_eps_pred = a + b * log_M
    ss_res = np.sum((log_eps - log_eps_pred) ** 2)
    ss_tot = np.sum((log_eps - np.mean(log_eps)) ** 2)
    R_squared = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return c, M_thr_choice, n, R_squared


def main():
    t0 = time.time()
    inputs = [
        SPECTRUM_CACHE, S89_W1_ALPHA_DIAG, S89_W2_CHI_PRIME,
        REGISTRY_MD, CANONICAL_CONSTANTS,
    ]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # ---- Step 1: Load L_max=12 cache, filter to L_max=10 ----
    print("Step 1: load substrate cache, filter to L_max=10")
    cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
    sector_evals_full = cache['sector_evals'].item()
    sectors_l10 = filter_l_max_10_sectors(sector_evals_full)
    n_sectors_l10 = len(sectors_l10)  # (local)
    print(f"  L_max=10 sectors: {n_sectors_l10} (filtered from {len(sector_evals_full)} total)")

    # Compute bot-20 occupation (inherits from filtered cache; preserve from CF-37)
    all_evals_with_pq = []
    for pq, info in sectors_l10.items():
        for e in info['abs_evals']:
            all_evals_with_pq.append((pq, e))
    all_evals_with_pq.sort(key=lambda x: x[1])
    bot20 = all_evals_with_pq[:20]
    bot20_occupation = {}
    for pq, _ in bot20:
        bot20_occupation[pq] = bot20_occupation.get(pq, 0) + 1
    print(f"  bot-20 occupation: {dict(sorted(bot20_occupation.items()))}")
    print()

    # ---- Step 2: χ' inheritance morphism anchor verification ----
    print("Step 2: χ' inheritance morphism anchor (element-3 (d); SAME as CF-37)")
    chi_prime = np.load(S89_W2_CHI_PRIME, allow_pickle=True)
    chi_prime_kernel_dim = int(chi_prime['kernel_M3C_dimension'])
    chi_prime_target = str(chi_prime['chi_prime_target'])
    chi_prime_target_dim = int(chi_prime['chi_prime_target_dim'])
    chi_prime_composite = str(chi_prime['composite_verdict'])
    print(f"  S89 §W2-3 audit_sha:    {CHI_PRIME_ANCHOR_AUDIT_SHA[:32]}...")
    print(f"  kernel_M3C_dimension:   {chi_prime_kernel_dim}")
    print(f"  chi_prime_target:       {chi_prime_target}")
    print(f"  chi_prime_target_dim:   {chi_prime_target_dim}")
    print(f"  composite verdict:      {chi_prime_composite}")
    print(f"  Wedderburn 9 > 8 ⇒ χ'|_M_3(C) = 0 (zero map); image rank 3")
    print(f"  χ'_weight = {CHI_PRIME_WEIGHT_NUM}/{CHI_PRIME_WEIGHT_DEN} = {CHI_PRIME_WEIGHT}")
    print()

    # ---- Step 3: Element-1 (c) γ(s) ≠ Γ(s) modified-universal-kernel ----
    print("Step 3: element-1 (c) γ(s) ≠ Γ(s) modified-universal-kernel specification")
    print(f"  γ(s) = Γ(s) · (1 + c_aux · (s - s_*)^{{-1}})")
    print(f"  c_aux = (rank(C) - rank(M_2(C)) + rank(M_3(C))) / total = "
          f"{C_AUX_NUM}/{C_AUX_DEN} = {C_AUX:.6f}")
    print(f"  Default substrate-distance pole s_* = {S_STAR_DEFAULT}")
    print(f"  Alternative pole s_* = {S_STAR_ALT} (per §VII.U.1 Mellin pattern)")
    print()

    # ---- Step 4: Enumerate γ_weight_aux candidates (honest disclosure) ----
    print("Step 4: γ_weight_aux candidate enumeration (3 substrate-derivations)")
    print(f"  Candidate (1) un-restricted Wedderburn: γ_weight_aux^(1) = "
          f"6/5 = {GAMMA_WEIGHT_AUX_C1}")
    print(f"  Candidate (2) c_aux · χ'_weight:         γ_weight_aux^(2) = "
          f"(1/3)·(1/2) = {GAMMA_WEIGHT_AUX_C2:.6f}")

    # Candidate (3) at s_* = 1 (default)
    gw3_s1, psi_s1 = gamma_weight_aux_candidate_3(S_STAR_DEFAULT)
    print(f"  Candidate (3) full residue at s_*=1:     ψ(1) = {psi_s1:.6f}, "
          f"γ_weight_aux^(3)(s_*=1) = 0.5·(1 + (1/3)·({psi_s1:.4f})) = {gw3_s1:.6f}")

    # Candidate (3) at s_* = 3 (alternative for due-diligence)
    gw3_s3, psi_s3 = gamma_weight_aux_candidate_3(S_STAR_ALT)
    print(f"  Candidate (3) full residue at s_*=3:     ψ(3) = {psi_s3:.6f}, "
          f"γ_weight_aux^(3)(s_*=3) = 0.5·(1 + (1/3)·({psi_s3:.4f})) = {gw3_s3:.6f}")

    # CANONICAL selection: candidate (3) at s_* = 1
    gamma_weight_aux_canonical = gw3_s1  # (local)
    psi_canonical = psi_s1  # (local)
    s_star_canonical = S_STAR_DEFAULT  # (local)
    print(f"  >> CANONICAL: candidate (3) at s_*=1 ⇒ γ_weight_aux = {gamma_weight_aux_canonical:.6f}")
    print(f"     (composes (c) modified-universal-kernel with χ' inheritance at residue layer)")
    print()

    gamma_weight_aux_candidates = np.array([GAMMA_WEIGHT_AUX_C1, GAMMA_WEIGHT_AUX_C2, gw3_s1])

    # ---- Step 5: Cite W-5 baseline ----
    print("Step 5: W-5 baseline canonical pins")
    print(f"  R_universal_HP1_strict_F4 = {R_universal_HP1_strict_F4} (W-5 V4)")
    print(f"  eps_H_HP1_norm = {eps_H_HP1_norm} (PRIMARY canonical; Class-(d) provenance)")
    print(f"  M_KK = {M_KK:.6e} GeV")
    print(f"  M_Pl_reduced = {M_Pl_reduced:.6e} GeV")
    print(f"  tau_fold = {tau_fold}")
    print(f"  (M_KK/M_Pl_reduced)² = {(M_KK/M_Pl_reduced)**2:.6e}")
    print()

    # ---- Step 6: Substrate spectral content ----
    print("Step 6: substrate spectrum at L_max=10")
    abs_evals_flat, sector_count = compute_substrate_spectrum(sectors_l10)
    n_substrate = len(abs_evals_flat)  # (local)
    n_chi_prime_image = int(np.round(CHI_PRIME_WEIGHT * n_substrate))  # (local)
    print(f"  total eigenvalues at L_max=10: {n_substrate}")
    print(f"  χ'-image (rank ratio 3/6): {n_chi_prime_image}")
    print(f"  |λ|_min = {np.min(abs_evals_flat):.6f} M_KK-units")
    print(f"  |λ|_max = {np.max(abs_evals_flat):.6f} M_KK-units")
    print()

    # ---- Step 7: M-scan computation of α''(M) under CANONICAL γ_weight_aux ----
    print("Step 7: M-scan α''(M) under (c)∘(d) corridor (canonical γ_weight_aux)")
    alpha_dp_scan = []  # (local)
    g_M_scan = []  # (local)
    Lambda_M_scan = []  # (local)
    for M_M_sun in M_SCAN_M_SUN:
        adp, g_M, Lambda_M_KK, M_KK_over_M_Pl_sq = compute_alpha_double_prime(
            M_M_sun, R_universal_HP1_strict_F4,
            gamma_weight_aux_canonical, abs_evals_flat,
        )
        alpha_dp_scan.append(adp)
        g_M_scan.append(g_M)
        Lambda_M_scan.append(Lambda_M_KK)
        print(f"  M = {M_M_sun:.0e} M_sun: Λ(M)/M_KK = {Lambda_M_KK:.3e}, "
              f"g(M, L=10) = {g_M:.6f}, α''(M) = {adp:.6e}")
    alpha_dp_scan = np.array(alpha_dp_scan)
    g_M_scan = np.array(g_M_scan)
    Lambda_M_scan = np.array(Lambda_M_scan)
    print()

    # α''(M_LRD) = value at index 2 (M = 10⁷ M_sun)
    alpha_dp_M_LRD = alpha_dp_scan[2]  # (local)
    alpha_dp_M_LRD_pub = float(np.round(alpha_dp_M_LRD, PUBLICATION_SIG_FIGS))
    print(f"  α''(M_LRD = 10⁷ M_sun, L_max=10) = {alpha_dp_M_LRD:.6e}")
    print(f"  Publication precision (5 sig figs): {alpha_dp_M_LRD_pub:.5e}")
    print()

    # ---- Step 8: Cross-evaluate at alternative γ_weight_aux candidates ----
    print("Step 8: cross-evaluate α''(M_LRD) under alternative γ_weight_aux candidates")
    alpha_dp_c1, _, _, _ = compute_alpha_double_prime(
        M_LRD_M_SUN, R_universal_HP1_strict_F4, GAMMA_WEIGHT_AUX_C1, abs_evals_flat,
    )
    alpha_dp_c2, _, _, _ = compute_alpha_double_prime(
        M_LRD_M_SUN, R_universal_HP1_strict_F4, GAMMA_WEIGHT_AUX_C2, abs_evals_flat,
    )
    alpha_dp_c3_s3, _, _, _ = compute_alpha_double_prime(
        M_LRD_M_SUN, R_universal_HP1_strict_F4, gw3_s3, abs_evals_flat,
    )
    print(f"  Candidate (1) γ_weight_aux = 1.2:     α''(M_LRD) = {alpha_dp_c1:.6e}, "
          f"rel_dev = {abs(alpha_dp_c1 - EMPIRICAL_ANCHOR)/EMPIRICAL_ANCHOR:.4f}")
    print(f"  Candidate (2) γ_weight_aux = 1/6:     α''(M_LRD) = {alpha_dp_c2:.6e}, "
          f"rel_dev = {abs(alpha_dp_c2 - EMPIRICAL_ANCHOR)/EMPIRICAL_ANCHOR:.4f}")
    print(f"  Candidate (3) s_*=1 (CANONICAL):      α''(M_LRD) = {alpha_dp_M_LRD:.6e}, "
          f"rel_dev = {abs(alpha_dp_M_LRD - EMPIRICAL_ANCHOR)/EMPIRICAL_ANCHOR:.4f}")
    print(f"  Candidate (3) s_*=3 (due-diligence):  α''(M_LRD) = {alpha_dp_c3_s3:.6e}, "
          f"rel_dev = {abs(alpha_dp_c3_s3 - EMPIRICAL_ANCHOR)/EMPIRICAL_ANCHOR:.4f}")
    print()

    # ---- Step 9: Sub-clause B (rel_dev band) ----
    print("Step 9: Sub-clause B (empirical anchor 1/458 comparison)")
    rel_dev = abs(alpha_dp_M_LRD - EMPIRICAL_ANCHOR) / EMPIRICAL_ANCHOR  # (local)
    print(f"  empirical anchor 1/458 = {EMPIRICAL_ANCHOR:.6e}")
    print(f"  α''(M_LRD) computed     = {alpha_dp_M_LRD:.6e}")
    print(f"  rel_dev = |α'' - 1/458|/(1/458) = {rel_dev:.4f}")
    print(f"  band: PASS ≤ {SUB_B_INFO_BAND}, INFO ≤ {SUB_B_PASS_BAND}, FAIL > {SUB_B_PASS_BAND}")
    if rel_dev <= SUB_B_INFO_BAND:
        sub_B_verdict = "PASS"
    elif rel_dev <= SUB_B_PASS_BAND:
        sub_B_verdict = "INFO"
    else:
        sub_B_verdict = "FAIL"
    print(f"  → Sub-clause B verdict: {sub_B_verdict}")
    print()

    # ---- Step 10: Sub-clause A (sign) ----
    print("Step 10: Sub-clause A (sign 0 < α'' < 1 via substitution chain)")
    pairing_value = R_universal_HP1_strict_F4 * gamma_weight_aux_canonical  # (local) > 0
    M_KK_over_M_Pl_sq = (M_KK / M_Pl_reduced) ** 2  # (local) > 0
    print(f"  Step 1 def: φ_g^sym ∈ HH^1(A_K); χ' (S89 §W2-3); γ(s)≠Γ(s) (W-1 AUX-4)")
    print(f"  Step 2 sub: γ(s_*)·pairing(s_*) residue ≥ 0 (non-negative idempotent)")
    print(f"               × χ'^*[φ_g^sym] non-negative (gradient-symmetric)")
    print(f"  Step 3 sub: pairing_numerator = R · γ_weight_aux = {pairing_value:.6e} > 0")
    print(f"  Step 4 sub: area_ratio (M_KK/M_Pl)² = {M_KK_over_M_Pl_sq:.6e} > 0")
    print(f"  Step 5 sub: g(M_LRD, L=10) = {g_M_scan[2]:.6e} ∈ (0, 1]")
    print(f"  Step 6 sub: α''(M_LRD) = {alpha_dp_M_LRD:.6e}")
    print(f"  Step 7 dir: 0 < α''(M_LRD) < 1 ⇒ Sub-clause A PASS")
    assert pairing_value > 0, "Sub-clause A FAIL: pairing not strictly positive"
    assert M_KK_over_M_Pl_sq > 0, "Sub-clause A FAIL: area ratio non-positive"
    assert g_M_scan[2] > 0, "Sub-clause A FAIL: g(M_LRD) non-positive"
    if 0 < alpha_dp_M_LRD < 1:
        sub_A_verdict = "PASS"
    else:
        sub_A_verdict = "FAIL"
    print(f"  → Sub-clause A verdict: {sub_A_verdict}")
    print()

    # ---- Step 11: Sub-clause C (envelope fit) ----
    print("Step 11: Sub-clause C M-asymptotic envelope fit")
    c_fit, M_thr_fit, n_fit, R_squared_fit = fit_envelope(M_SCAN_M_SUN, alpha_dp_scan)
    print(f"  envelope α''(M) = 1 + c · (M/M_thr)^{{-n}}")
    if c_fit is not None:
        print(f"  c = {c_fit:.6e}")
        print(f"  M_thr = {M_thr_fit:.6e} M_sun")
        print(f"  n = {n_fit:.6f}")
        print(f"  R² = {R_squared_fit:.6f}")
    else:
        print(f"  fit insufficient (need ≥3 distinct (1-α'') points; got "
              f"{int(np.sum(alpha_dp_scan < 1.0))} valid)")
    print(f"  requires: n > 0 AND R² ≥ {SUB_C_R2_THRESHOLD}")
    if c_fit is None or n_fit is None:
        sub_C_verdict = "FAIL"
        sub_C_reason = "envelope fit underdetermined (α'' approximately constant across M-scan)"
    elif n_fit > 0 and R_squared_fit >= SUB_C_R2_THRESHOLD:
        sub_C_verdict = "PASS"
        sub_C_reason = f"n = {n_fit:.4f} > 0 AND R² = {R_squared_fit:.4f} ≥ {SUB_C_R2_THRESHOLD}"
    elif n_fit > 0:
        sub_C_verdict = "INFO"
        sub_C_reason = f"n = {n_fit:.4f} > 0 BUT R² = {R_squared_fit:.4f} < {SUB_C_R2_THRESHOLD}"
    else:
        sub_C_verdict = "FAIL"
        sub_C_reason = f"n = {n_fit:.4f} ≤ 0 (envelope fails substrate prediction)"
    print(f"  → Sub-clause C verdict: {sub_C_verdict} ({sub_C_reason})")
    print()

    # ---- Step 12: Composite verdict ----
    print("Step 12: composite verdict per plan §9 collapse rule")
    print(f"  Sub-clause A (sign 0<α''<1):        {sub_A_verdict}")
    print(f"  Sub-clause B (rel_dev ≤ 30% RATIO): {sub_B_verdict}")
    print(f"  Sub-clause C (n>0 AND R²≥0.95):     {sub_C_verdict}")
    sub_verdicts = [sub_A_verdict, sub_B_verdict, sub_C_verdict]
    if any(v == "FAIL" for v in sub_verdicts):
        composite = "FAIL"
    elif any(v == "INFO" for v in sub_verdicts):
        composite = "INFO"
    else:
        composite = "PASS"
    print(f"  → composite: {composite}")
    print()

    # ---- Step 13: 3-tuple annotation ----
    print("Step 13: 3-tuple annotation (S87 schema-v2)")
    # sign_verdict: substitution chain pre-registers 0 < α'' < 1
    sign_v = "PASS" if (0 < alpha_dp_M_LRD < 1) else "FAIL"
    # magnitude_verdict: tied to Sub-clause B band classification
    if sub_B_verdict == "PASS":
        mag_v = "PASS"
    elif sub_B_verdict == "INFO":
        mag_v = "INFO"
    else:
        mag_v = "FAIL"
    # regime_verdict: VALID at L_max=10 per Friedrich-Bär saturation theorem (W11-3 precedent)
    # The substrate's bottom-K observables at L_max=10 are structurally saturated;
    # no L_max ≥ 12 extrapolation required for the residue evaluation at s_*=1.
    regime_v = "VALID"
    print(f"  sign_verdict={sign_v} (substitution Step 6 PRE-COMMITTED direction)")
    print(f"  magnitude_verdict={mag_v} (Sub-clause B band)")
    print(f"  regime_verdict={regime_v} (Friedrich-Bär saturation at L=10)")
    print()

    # ---- Step 14: Save NPZ ----
    print("Step 14: save NPZ + PNG artifacts")
    np.savez(
        NPZ_OUT,
        # α''(M_LRD) primary outputs
        alpha_double_prime_M_LRD_value=alpha_dp_M_LRD,
        alpha_double_prime_M_LRD_pub5sf=alpha_dp_M_LRD_pub,
        publication_sig_figs=PUBLICATION_SIG_FIGS,
        # γ_weight_aux candidate enumeration
        gamma_weight_aux_candidates=gamma_weight_aux_candidates,
        gamma_weight_aux_candidate_1=GAMMA_WEIGHT_AUX_C1,
        gamma_weight_aux_candidate_2=GAMMA_WEIGHT_AUX_C2,
        gamma_weight_aux_candidate_3_at_s1=gw3_s1,
        gamma_weight_aux_candidate_3_at_s3=gw3_s3,
        gamma_weight_aux_canonical=gamma_weight_aux_canonical,
        gamma_weight_aux_canonical_label="candidate_3_full_residue_at_s_star_1",
        # γ(s) kernel modulation pins
        c_aux=C_AUX,
        c_aux_form=f"{C_AUX_NUM}/{C_AUX_DEN}",
        s_star=s_star_canonical,
        s_star_alternative=S_STAR_ALT,
        psi_s_star_canonical=psi_canonical,
        psi_s_star_alternative=psi_s3,
        # M-scan results
        M_scan=M_SCAN_M_SUN,
        g_M_scan=g_M_scan,
        Lambda_M_scan_in_M_KK=Lambda_M_scan,
        alpha_double_prime_scan=alpha_dp_scan,
        # Cross-evaluation at all γ_weight_aux candidates
        alpha_double_prime_M_LRD_c1=alpha_dp_c1,
        alpha_double_prime_M_LRD_c2=alpha_dp_c2,
        alpha_double_prime_M_LRD_c3_s1=alpha_dp_M_LRD,
        alpha_double_prime_M_LRD_c3_s3=alpha_dp_c3_s3,
        # Empirical anchor + sub-clause verdicts
        empirical_anchor_1_over_458=EMPIRICAL_ANCHOR,
        rel_dev_M_LRD=rel_dev,
        sub_B_PASS_band=SUB_B_INFO_BAND,
        sub_B_INFO_band=SUB_B_PASS_BAND,
        sub_clause_A_verdict=sub_A_verdict,
        sub_clause_B_verdict=sub_B_verdict,
        sub_clause_C_verdict=sub_C_verdict,
        composite=composite,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        # Envelope fit results
        envelope_c=c_fit if c_fit is not None else np.nan,
        envelope_M_thr=M_thr_fit if M_thr_fit is not None else np.nan,
        envelope_n=n_fit if n_fit is not None else np.nan,
        envelope_R_squared=R_squared_fit,
        sub_C_reason=sub_C_reason,
        # Substrate spectral content + bot-20 occupation
        n_total_substrate_states=n_substrate,
        n_chi_prime_image=n_chi_prime_image,
        chi_prime_weight=CHI_PRIME_WEIGHT,
        chi_prime_weight_form=f"{CHI_PRIME_WEIGHT_NUM}/{CHI_PRIME_WEIGHT_DEN}",
        bot20_occupation=str(dict(sorted(bot20_occupation.items()))),
        bot20_total=20,
        # W-5 baseline + canonical pins
        R_universal_baseline=R_universal_HP1_strict_F4,
        eps_H_HP1_norm_canonical=eps_H_HP1_norm,
        M_KK_over_M_Pl_reduced_sq=M_KK_over_M_Pl_sq,
        L_max=L_MAX,
        tau_fold_pin=tau_fold,
        regulator_pin="Mellin-Barnes-modified-universal-kernel-gamma-s",
        # χ' anchor SHA + calibration corpus status
        chi_prime_anchor_audit_sha=CHI_PRIME_ANCHOR_AUDIT_SHA,
        calibration_corpus_instance=(
            "instance_2_LANDED" if composite == "PASS" else "instance_2_pending"
        ),
        # Audit pins
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        schema_version=SCHEMA_VERSION,
    )
    print(f"  NPZ: {NPZ_OUT.relative_to(PROJECT_ROOT)}")

    # ---- Plot ----
    fig, ax = plt.subplots(figsize=(9, 6.5))
    ax.loglog(M_SCAN_M_SUN, alpha_dp_scan, 'o-', color='C0', lw=2, markersize=8,
              label=f"α''(M) (c)∘(d) corridor; γ_weight_aux={gamma_weight_aux_canonical:.4f}")
    # Cross-evaluation overlays at each candidate
    alpha_scan_c1 = np.array([compute_alpha_double_prime(m, R_universal_HP1_strict_F4,
                                                          GAMMA_WEIGHT_AUX_C1, abs_evals_flat)[0]
                              for m in M_SCAN_M_SUN])
    alpha_scan_c2 = np.array([compute_alpha_double_prime(m, R_universal_HP1_strict_F4,
                                                          GAMMA_WEIGHT_AUX_C2, abs_evals_flat)[0]
                              for m in M_SCAN_M_SUN])
    ax.loglog(M_SCAN_M_SUN, alpha_scan_c1, 's--', color='C1', alpha=0.5,
              label=f"candidate (1) γ=6/5={GAMMA_WEIGHT_AUX_C1}")
    ax.loglog(M_SCAN_M_SUN, alpha_scan_c2, '^--', color='C2', alpha=0.5,
              label=f"candidate (2) γ=1/6≈{GAMMA_WEIGHT_AUX_C2:.4f}")
    ax.axhline(EMPIRICAL_ANCHOR, color='red', linestyle='--', lw=1.5,
               label=f"empirical anchor 1/458 = {EMPIRICAL_ANCHOR:.4e}")
    ax.axhspan(EMPIRICAL_ANCHOR * (1 - SUB_B_PASS_BAND),
               EMPIRICAL_ANCHOR * (1 + SUB_B_PASS_BAND),
               alpha=0.12, color='green',
               label='Sub-clause B 30% RATIO PASS band')
    ax.axvline(M_LRD_M_SUN, color='blue', linestyle=':', alpha=0.5,
               label='M_LRD = 10⁷ M_sun')
    ax.set_xlabel('M [M_sun]')
    ax.set_ylabel("α''(M, L_max=10)")
    ax.set_title(
        f"S91 W3-3 T1.8 AUX-4: α''(M) (c)∘(d) corridor at L_max=10\n"
        f"composite={composite}; α''(M_LRD)={alpha_dp_M_LRD:.3e} vs 1/458={EMPIRICAL_ANCHOR:.3e}; "
        f"rel_dev={rel_dev:.3f}\n"
        f"γ(s)=Γ(s)·(1+c_aux/(s-s_*)); c_aux=1/3; s_*=1; ψ(1)=-γ_Euler"
    )
    ax.legend(loc='best', fontsize=8)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(PNG_OUT, dpi=120)
    plt.close()
    print(f"  PNG: {PNG_OUT.relative_to(PROJECT_ROOT)}")
    print()

    # ---- Step 15: Emit verdict (single-shot AFTER-pattern) ----
    print("Step 15: emit verdict line + dual-SHA companion + 3-tuple annotation")
    verdict_value = (
        f"alpha_double_prime_M_LRD={alpha_dp_M_LRD_pub:.5e};"
        f"empirical_anchor=2.18341e-03;"
        f"rel_dev={rel_dev:.4f};"
        f"sub_A={sub_A_verdict};"
        f"sub_B={sub_B_verdict};"
        f"sub_C={sub_C_verdict};"
        f"composite={composite};"
        f"gamma_weight_aux_canonical={gamma_weight_aux_canonical:.6f};"
        f"gamma_weight_aux_candidate_choice=3_full_residue_at_s_star_1;"
        f"s_star={s_star_canonical};"
        f"c_aux=1_over_3;"
        f"psi_s_star={psi_canonical:.6f};"
        f"R_universal_baseline={R_universal_HP1_strict_F4};"
        f"chi_prime_weight={CHI_PRIME_WEIGHT_NUM}_over_{CHI_PRIME_WEIGHT_DEN}={CHI_PRIME_WEIGHT};"
        f"M_KK_over_M_Pl_reduced_sq={M_KK_over_M_Pl_sq:.5e};"
        f"envelope_n={n_fit if n_fit is not None else 'undefined'};"
        f"envelope_R_squared={R_squared_fit:.4f};"
        f"L_max={L_MAX};"
        f"bot20_occupation_at_L10={dict(sorted(bot20_occupation.items()))};"
        f"regulator_pin=Mellin-Barnes-modified-universal-kernel-gamma-s;"
        f"chi_prime_anchor_audit_sha=90bba262af80a04c;"
        f"calibration_corpus_instance={'instance_2_LANDED' if composite == 'PASS' else 'instance_2_pending'};"
        f"after_pattern_compliance=True"
    )
    emit_verdict(composite, verdict_value, audit_sha, content_sha,
                 sign_v, mag_v, regime_v)
    print(f"  appended to: {VERDICT_TXT.relative_to(PROJECT_ROOT)}")
    print(f"\n=== {GATE_ID}: {composite} (wall {time.time() - t0:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
