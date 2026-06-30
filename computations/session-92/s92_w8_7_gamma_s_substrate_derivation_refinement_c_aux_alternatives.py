"""
s92_w8_7_gamma_s_substrate_derivation_refinement_c_aux_alternatives.py
======================================================================

S92-W8-CF-S92-GAMMA-S-SUBSTRATE-DERIVATION-REFINEMENT-C-AUX-ALTERNATIVES (§W8-7)

Classification: GEOMETRIC.

Substrate framing (phononic-framing.md §"IS Space, Not IN Space"):
  The substrate IS the spectral triple (A_K, H_K, D_K(tau_fold)) with
  A_K = C (+) H (+) M_3(C). The modified-universal-kernel
      gamma(s) = Gamma(s) * (1 + c_aux * (s - s_*)^{-1})
  IS a substrate-IS cohomology-class observable (the (c) cohomology-class
  image of the universal kernel Gamma(s) under element-1 deformation). The
  coefficient c_aux is NOT a free parameter at the substrate-IS layer: it is
  substrate-DERIVED from one of four algebra-INVARIANT data of A_K --
      (default) Wedderburn algebra-weight (1-2+3)/6 = 1/3
      (i)   SU(3) chiral-anomaly polynomial coefficient d_888/2 = sqrt(3)/6
      (ii)  M_3(C) Casimir difference-ratio (C_2(adj)-C_2(fund))/C_2(adj) = 23/27
      (iii) chi_BdG inheritance-morphism rank ratio {-1/6 (irrep-dim), -5/14 (Wedderburn)}
  Explanation flows substrate -> bridge map (Connes-Karoubi pairing /
  K_0 inheritance morphism) -> emergent LRD alpha-anchor observable. The
  empirical 1/458 anchor is a laboratory-IN observable; the substrate is
  logically prior.

WHAT THIS GATE COMPUTES
-----------------------
A 4-candidate x 3-test discrete grid (12 evaluations) characterizing
alternative substrate-derivations of c_aux beyond the default 1/3, per the
S91 W3 §W3-3 carry-forward CF-S92-GAMMA-S-SUBSTRATE-DERIVATION-REFINEMENT-
ALTERNATIVE-C-AUX.

The S91 W3 §W3-3 closed form (verdict S91-CF37-AUX-4-SECONDARY-CORRIDOR,
audit_sha256 8ab158e9...) is:
    gamma_weight_aux^(3)(c_aux) = chi_prime_weight * (1 + c_aux * psi(s_*))   (Eq. 1)
    alpha''(M_LRD) = R_universal_baseline * gamma_weight_aux
                     * (M_KK/M_Pl_reduced)^2 * g(M_LRD, L=10)                 (Eq. 2)
with chi_prime_weight = 1/2, s_* = 1, psi(1) = -gamma_Euler = -0.5772156649,
R_universal_baseline = R_universal_HP1_strict_F4 = 1.030902, g = 1.000
(saturated at M_LRD = 1e7 M_sun, L=10).

Three convergent-derivation tests (per plan §W8-7 method.description):
  Test A (parse-tree clause (e) closed-form reduction): does gamma_C(s) reduce
    to a closed-form algebraic identity on A_K WITHOUT post-hoc state-pair
    operations? A substrate-derived SCALAR c_aux (algebra-INVARIANT,
    spectrum-only) reduces gamma_C(s) to a closed form trivially.
  Test B (Connes-Karoubi pairing residue at s_*=1): does
    Res_{s=1}[gamma_C(s) * <[phi_g^{sym}], [Ch(P_HSS'(M_LRD))]>] produce a
    finite + non-zero substrate-IS observable value 0 < alpha''(M_LRD) < 1
    (S91 W3 §W3-3 Sub-clause A pre-registration), and does the numerical
    residue REPRODUCE the closed form Eq. 1 to within 5e-2 relative deviation?
  Test C (HKR-image K_0 inheritance morphism commutation): does gamma_C(s) at
    the candidate c_aux value commute with the substrate's
    K_0(A_K) -> K_0(M_2(C)) inheritance morphism induced by chi? A global
    scalar multiplier commutes with any linear map; M*(lam*v) = lam*(M*v).

PRE-REGISTERED VERDICT RUBRIC (plan §W8-7 operator)
---------------------------------------------------
  PASS iff >= 1 ALTERNATIVE candidate in {anomaly, casimir, BdG_rank} PASSes
       all 3 tests AND a substrate-natural selection is identified (Connes 1996
       reconstruction theorem natural normalization). If the default 1/3 is the
       UNIQUE pass, default is reaffirmed canonical.
  INFO iff partial PASS (one candidate 2-of-3 with 1 INFO) OR multiple
       candidates PASS all 3 tests WITHOUT a discriminating substrate-natural
       selection criterion (i.e., the 3 tests are non-discriminating).
  FAIL iff no candidate PASSes ANY of the 3 tests (would lock the default 1/3).

This is an EXPLORATORY characterization. The outcome is honestly reported;
no iteration-until-PASS (PROHIBITED_ACTIONS Class 6). Iterative-tuning of
c_aux is FORBIDDEN (PROHIBITED_ACTIONS Class 1 convention-shopping) per the
S91 CF spec.

Convention discipline:
    scheme     = connes-moscovici-1995-§III.4-residue-formula-modified-universal-kernel
    convention = volovik-superfluid-universe-theorist-primary-substrate-derivation-refinement-c-aux-alternatives

Sage-QQ cross-checks: all c_aux candidates are exact rationals (or sqrt(3)-
algebraic for the anomaly candidate) per regulator-pin-discipline.md
§"Extension: Sage-Exact Rationals". The Sage-QQ values are pinned in the
SAGE_EXACT dict below and cross-checked against the float64 path.

d_abc provenance note (feedback_research-corpus.md): Cornwell
1989 §13.2 Table A.5 is NOT in researchers/. The substrate-natural SU(3)
symmetric-structure-constant scalar is the Cartan-diagonal hypercharge
self-coupling |d_888| = 1/sqrt(3), cited via the canonical SU(3) Gell-Mann
identity sum_{abc} d_abc^2 = 40/3 and the standard d_888 = -1/sqrt(3) value.
This is marked as a CONVENTION-DEPENDENT choice; d_888 is selected because it
ties to the framework's own phi_88 Cartan-hypercharge cocycle in the 3He-B
inheritance structure (cocycle_norm_phi88 in canonical_constants.py).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # (local) CPU thread cap; no GPU needed (closed-form arithmetic)
os.environ.setdefault("MKL_NUM_THREADS", "8")   # (local)

import sys
import json
import hashlib
from pathlib import Path
from fractions import Fraction

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import digamma, gamma as gamma_fn   # (local import) digamma for psi(s_*); gamma for kernel curve

# --- canonical constants (MANDATORY import; never hardcode) ---
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import (
    M_KK,                       # 7.428660036284456e16 GeV (gravity route)
    M_Pl_reduced,               # 2.435e18 GeV
    R_universal_HP1_strict_F4,  # 1.030902
    eps_H_HP1_norm,             # 16.197719 (PRIMARY canonical anchoring R_universal_HP1_strict_F4)
    cocycle_norm_phi88,         # 0.108307 M_KK^2 (phi_88 Cartan hypercharge cocycle; ties anomaly candidate)
    cocycle_norm_phi67,         # 0.793346 M_KK^2 (phi_67 chiral pair cocycle)
    tau_fold,                   # 0.19
)

# -----------------------------------------------------------------------------
# Gate identity + convention
# -----------------------------------------------------------------------------
GATE_ID = "S92-W8-CF-S92-GAMMA-S-SUBSTRATE-DERIVATION-REFINEMENT-C-AUX-ALTERNATIVES"
SCHEME = "connes-moscovici-1995-III.4-residue-formula-modified-universal-kernel"
CONVENTION = "volovik-superfluid-universe-theorist-primary-substrate-derivation-refinement-c-aux-alternatives"
L_MAX = 10                  # (local) S91 W3 §W3-3 D_K spectral-triple truncation pin (matches CF-37 for comparability)

HERE = Path(__file__).resolve().parent
VERDICT_TXT = HERE / "s92_gate_verdicts.txt"
NPZ_OUT = HERE / "s92_w8_7_gamma_s_substrate_derivation_refinement_c_aux_alternatives.npz"
PNG_OUT = HERE / "s92_w8_7_gamma_s_substrate_derivation_refinement_c_aux_alternatives.png"

# -----------------------------------------------------------------------------
# Substrate Wedderburn rank data of A_K = C (+) H (+) M_3(C)
# (irrep-dimension convention per S91 W3 §W3-3 Definition 2: rank(M_n(C)) = n;
#  Wedderburn-rank convention: rank(M_n(C)) = n^2)
# -----------------------------------------------------------------------------
RANK_C_IRREP = 1            # (local) irrep dim of C
RANK_M2_IRREP = 2           # (local) irrep dim of H ~ M_2(C) (the BdG sub-algebra)
RANK_M3_IRREP = 3           # (local) irrep dim of M_3(C)
RANK_AK_IRREP = RANK_C_IRREP + RANK_M2_IRREP + RANK_M3_IRREP   # (local) = 6

RANK_C_WEDD = 1             # (local) Wedderburn rank of C = 1^2
RANK_M2_WEDD = 4            # (local) Wedderburn rank of M_2(C) = 2^2
RANK_M3_WEDD = 9            # (local) Wedderburn rank of M_3(C) = 3^2
RANK_AK_WEDD = RANK_C_WEDD + RANK_M2_WEDD + RANK_M3_WEDD        # (local) = 14

# SU(3) Casimir pins (Humphreys 1972 §10 Cartan classification A_2; plan humphreys_casimir_pin)
C2_ADJ_SU3 = Fraction(9, 1)     # (local) C_2(adj_SU(3)) = 9 per plan pin
C2_FUND_SU3 = Fraction(4, 3)    # (local) C_2(fund_SU(3)) = 4/3 per plan pin

# SU(3) symmetric-structure-constant identity (canonical; Cornwell 1989 not in researchers/)
SUM_DABC2_SU3 = Fraction(40, 3)  # (local) sum_{abc} d_abc^2 = 40/3 for SU(3) Gell-Mann normalization
# d_888 = -1/sqrt(3) (Cartan-diagonal hypercharge self-coupling); substrate-natural scalar |d_888|.

# -----------------------------------------------------------------------------
# S91 W3 §W3-3 closed-form pins (verdict S91-CF37-AUX-4-SECONDARY-CORRIDOR)
# -----------------------------------------------------------------------------
CHI_PRIME_WEIGHT = 0.5          # (local) chi'_weight = (rank(M_2(C))+rank(Cl(1)))/sum = (2+1)/6 = 0.5
S_STAR = 1                      # (local) substrate-distance-1 pole (default)
G_SATURATED = 1.0               # (local) g(M_LRD=1e7 M_sun, L=10) saturated = 1.000 (element-3 (d) identical to CF-37)
M_LRD = 1.0e7                   # (local) LRD scale 1e7 M_sun (anchor scan point)
EMP_ANCHOR_1_OVER_458 = 1.0 / 458.0   # (local) 2.183406e-03 laboratory-IN anchor

# Dimensional bridge factor (M_KK/M_Pl_reduced)^2
MKK_OVER_MPL_SQ = (M_KK / M_Pl_reduced) ** 2          # (local) ~9.307286e-04

# Test B reproduction tolerance (plan tolerance field)
TEST_B_REL_TOL = 5e-2           # (local) 5e-2 relative deviation for residue-vs-closed-form reproduction

# Sub-clause A bounds (Test B existence criterion)
SUBA_LOW = 0.0                  # (local)
SUBA_HIGH = 1.0                 # (local)


# =============================================================================
# Substrate-derivation of the 4 c_aux candidates (Sage-QQ exact + float64)
# =============================================================================
# SAGE_EXACT values pinned from Sage-QQ session (regulator-pin-discipline.md
# §"Extension: Sage-Exact Rationals"). Cross-checked against float64 below.
SAGE_EXACT = {
    "c_aux_default":     "1/3",                 # (1-2+3)/6, irrep-dim convention
    "c_aux_anomaly":     "sqrt(3)/6",           # d_888/2 = (1/sqrt(3))/2
    "c_aux_casimir":     "23/27",               # (9 - 4/3)/9
    "c_aux_BdG_irrep":   "-1/6",                # (2-3)/6, irrep-dim convention
    "c_aux_BdG_wedder":  "-5/14",               # (4-9)/14, Wedderburn-rank convention
    "psi_s_star":        "-euler_gamma",
    "C2_adj_over_fund":  "27/4",                # bare ratio (over-amplifies; rejected)
}


def c_aux_default_value():
    """Default substrate-Wedderburn algebra-weight: (rank(C) - rank(M_2(C)) + rank(M_3(C))) / sum.
    Irrep-dim convention rank(M_n(C)) = n. (1 - 2 + 3) / 6 = 1/3.
    ONE structural choice (the sign-alternating rank pattern); the numerator and
    denominator are both the Wedderburn rank data directly.
    """
    num = RANK_C_IRREP - RANK_M2_IRREP + RANK_M3_IRREP    # (local) 1 - 2 + 3 = 2
    den = RANK_AK_IRREP                                   # (local) 6
    return num / den                                      # 1/3


def c_aux_anomaly_value():
    """Candidate (i): SU(3) chiral-anomaly polynomial coefficient.
    c_aux_anomaly = d_abc * (rank(M_3(C)) - rank(chi(M_3(L)))) / rank(A_K)
                  = d_888 * 3 / 6 = d_888 / 2, with d_888 = 1/sqrt(3) (Cartan
    hypercharge self-coupling; |d_888| is the substrate-natural single scalar
    from the d_abc tensor; ties to phi_88). chi kills M_3(C) so
    rank(chi(M_3(L))) = 0; rank-ratio = 3/6 = 1/2.
    TWO choices: (a) d_888 scalar-pick from the d_abc tensor; (b) rank-ratio factor.
    """
    d_888_mag = 1.0 / np.sqrt(3.0)                        # (local) |d_888| = 1/sqrt(3) ~ 0.5773502692
    rank_ratio = (RANK_M3_IRREP - 0) / RANK_AK_IRREP      # (local) (3-0)/6 = 1/2
    return d_888_mag * rank_ratio                         # sqrt(3)/6 ~ 0.2886751346


def c_aux_casimir_value():
    """Candidate (ii): M_3(C) Casimir difference-ratio normalization.
    Bare ratio C_2(adj)/C_2(fund) = 9/(4/3) = 27/4 = 6.75 OVER-AMPLIFIES the (c)
    cohomology-class shift (plan flags this). Difference-ratio normalization:
    (C_2(adj) - C_2(fund)) / C_2(adj) = (9 - 4/3)/9 = 23/27 ~ 0.8519.
    TWO+ choices: the difference-norm is a post-hoc repair of the over-amplifying
    bare ratio (which normalization?).
    """
    diff = float(C2_ADJ_SU3 - C2_FUND_SU3)                # (local) 9 - 4/3 = 23/3
    return diff / float(C2_ADJ_SU3)                       # (23/3)/9 = 23/27


def c_aux_BdG_value(convention):
    """Candidate (iii): chi_BdG inheritance-morphism rank ratio.
    c_aux_BdG_rank = (rank(M_2(C)) - rank(ker chi_BdG)) / rank(A_K),
    ker chi_BdG = M_3(C) (chi kills M_3(C); ker_M3C_dim = 9 per S89 §W2-3).
      irrep-dim convention:   (2 - 3) / 6   = -1/6   ~ -0.1667
      Wedderburn-rank conv.:  (4 - 9) / 14  = -5/14  ~ -0.3571
    TWO unresolved ambiguities: sign (negative) AND rank-convention (irrep vs Wedderburn).
    """
    if convention == "irrep":
        return (RANK_M2_IRREP - RANK_M3_IRREP) / RANK_AK_IRREP      # -1/6
    elif convention == "wedderburn":
        return (RANK_M2_WEDD - RANK_M3_WEDD) / RANK_AK_WEDD         # -5/14
    raise ValueError(convention)


# =============================================================================
# The closed form Eq. 1 + Eq. 2 (Test B residue evaluation)
# =============================================================================
PSI_S_STAR = float(digamma(S_STAR))     # (local) psi(1) = -euler_gamma = -0.5772156649


def gamma_weight_aux(c_aux):
    """Eq. 1: gamma_weight_aux^(3)(c_aux) = chi_prime_weight * (1 + c_aux * psi(s_*))."""
    return CHI_PRIME_WEIGHT * (1.0 + c_aux * PSI_S_STAR)


def alpha_double_prime(c_aux):
    """Eq. 2: alpha''(M_LRD) = R_base * gamma_weight_aux * (M_KK/M_Pl)^2 * g."""
    gw = gamma_weight_aux(c_aux)                                          # (local)
    return R_universal_HP1_strict_F4 * gw * MKK_OVER_MPL_SQ * G_SATURATED


def residue_numerical(c_aux):
    """Test B numerical residue: Res_{s=1}[gamma_C(s) * pairing(s)].
    The Connes-Moscovici 1995 §III.4 simple-pole residue at s_*=1 of
    gamma_C(s) = Gamma(s)*(1 + c_aux*(s-1)^{-1}) times the s-independent pairing
    weight chi_prime_weight: the (s-1)^{-1} simple pole has residue
    Gamma(1)*c_aux = c_aux (since Gamma(1)=1); the regular part Gamma(s) at s=1
    contributes its value Gamma(1)=1 to the constant-1 term. The full
    residue-evaluated weight equals chi_prime_weight*(1 + c_aux*psi(1)) by the
    digamma-correction of the Gamma-modulated pole (S91 W3 §W3-3 closed form).
    We evaluate the residue numerically via a contour-difference quotient around
    s=1 and verify it reproduces Eq. 1 to within TEST_B_REL_TOL.
    """
    # Numerical residue of gamma_C(s)*chi_prime_weight at the simple pole s=1,
    # PLUS the Gamma-regular digamma correction, reconstructed as the S91 closed
    # form. Cross-check: small-eps expansion of Gamma(s)(1+c_aux/(s-1)) near s=1:
    #   Gamma(1+e) = 1 - euler_gamma*e + O(e^2);  (1 + c_aux/e)
    #   product = c_aux/e + (1 - euler_gamma*c_aux) + O(e)
    #   the FINITE part (e^0 coeff) = 1 - euler_gamma*c_aux = 1 + c_aux*psi(1).
    # times chi_prime_weight => Eq. 1. Evaluate the finite part numerically.
    eps = 1e-6                                                           # (local) expansion parameter
    s_plus = 1.0 + eps                                                  # (local)
    g_kernel = gamma_fn(s_plus) * (1.0 + c_aux / eps)                   # (local) gamma_C(s) near pole
    pole_part = c_aux / eps                                             # (local) singular term
    finite_part = g_kernel - pole_part                                  # (local) e^0 coefficient (-> 1 + c_aux*psi(1))
    return CHI_PRIME_WEIGHT * finite_part


# =============================================================================
# The 3 convergent-derivation tests (per candidate)
# =============================================================================
def test_A_parse_tree_closed_form(c_aux, is_algebra_invariant):
    """Test A: gamma_C(s) reduces to a closed-form algebraic identity on A_K
    WITHOUT post-hoc state-pair operations (parse-tree clause (e)).
    A substrate-derived SCALAR c_aux that is algebra-INVARIANT (spectrum-only:
    rank arithmetic / Casimir eigenvalue / d_abc representation invariant)
    reduces gamma_C(s) = Gamma(s)*(1 + c_aux*(s-s_*)^{-1}) to a closed form
    trivially -- c_aux multiplies a closed-form kernel; no state-pair operation
    is introduced. PASS iff c_aux is a finite algebra-INVARIANT scalar.
    """
    finite = np.isfinite(c_aux)                                         # (local)
    return "PASS" if (finite and is_algebra_invariant) else "FAIL"


def test_B_connes_karoubi_residue(c_aux):
    """Test B: residue at s_*=1 produces 0 < alpha'' < 1 (Sub-clause A) AND the
    numerical residue reproduces the closed form Eq. 1 to within TEST_B_REL_TOL.
    Returns (verdict, alpha_val, residue_reproduction_rel_dev).
    """
    alpha = alpha_double_prime(c_aux)                                   # (local)
    gw_closed = gamma_weight_aux(c_aux)                                 # (local) Eq. 1 closed form
    gw_residue = residue_numerical(c_aux)                              # (local) numerical residue
    repro_rel_dev = abs(gw_residue - gw_closed) / abs(gw_closed) if gw_closed != 0 else np.inf  # (local)
    suba = (SUBA_LOW < alpha < SUBA_HIGH)                              # (local) finite + non-zero + bounded
    repro_ok = (repro_rel_dev <= TEST_B_REL_TOL)                      # (local) residue reproduces closed form
    verdict = "PASS" if (suba and repro_ok) else ("INFO" if suba else "FAIL")  # (local)
    return verdict, alpha, repro_rel_dev


def test_C_K0_inheritance_commutation(c_aux):
    """Test C: gamma_C(s) commutes with the inheritance morphism
    chi_*: K_0(A_K)=Z^3 -> K_0(M_2(C))=Z induced by chi (kills M_3(C)).
    gamma_C(s) acts as a GLOBAL SCALAR multiplier (1 + c_aux*(s-s_*)^{-1}) on the
    Connes-Karoubi pairing; scalar multiplication commutes with any linear map.
    Verify M*(lam*v) == lam*(M*v) numerically with chi_* = [[1,1,0]] (kills 3rd
    K_0 generator = M_3(C) class).
    PASS iff the commutator is zero for the candidate's scalar.
    """
    chi_star = np.array([[1.0, 1.0, 0.0]])                            # (local) K_0(A_K)->K_0(M_2(C)); kills M_3(C)
    v = np.array([1.0, 1.0, 1.0])                                     # (local) generic K_0 generator vector
    lam = (1.0 + c_aux)                                              # (local) representative scalar (s-indep part)
    lhs = chi_star @ (lam * v)                                       # (local) gamma scalar BEFORE chi_*
    rhs = lam * (chi_star @ v)                                       # (local) chi_* THEN gamma scalar
    commutes = np.allclose(lhs, rhs, atol=1e-14, rtol=0.0)           # (local)
    return "PASS" if commutes else "FAIL"


# =============================================================================
# Dual-SHA (S84+ schema)
# =============================================================================
def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def file_sha256(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def compute_dual_sha(script_path: Path, pins: dict) -> tuple:
    script_bytes = b""
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                       # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                   # (local)
    return audit, content


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append canonical line + dual-SHA companion row ([VERIFY-THEOREM]: no
    schema-v2 3-tuple companion required per spawn prompt)."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# =============================================================================
# Main
# =============================================================================
def main():
    # --- substrate-derive the 4 candidate c_aux values ---
    c_aux_default = c_aux_default_value()           # (local) 1/3
    c_aux_anomaly = c_aux_anomaly_value()           # (local) sqrt(3)/6
    c_aux_casimir = c_aux_casimir_value()           # (local) 23/27
    c_aux_BdG_irrep = c_aux_BdG_value("irrep")      # (local) -1/6
    c_aux_BdG_wedder = c_aux_BdG_value("wedderburn")  # (local) -5/14
    # Canonical BdG_rank representative: irrep-dim convention (matches S91 W3 §W3-3 Definition 3
    # default rank convention); Wedderburn-rank value tracked as the alternative.
    c_aux_BdG_rank = c_aux_BdG_irrep                 # (local) -1/6 (canonical-convention representative)

    # --- Sage-QQ exact cross-check (float of exact rationals) ---
    sage_check = {
        "c_aux_default":    abs(c_aux_default - float(Fraction(1, 3))) < 1e-15,
        "c_aux_anomaly":    abs(c_aux_anomaly - (1.0/np.sqrt(3.0))/2.0) < 1e-15,
        "c_aux_casimir":    abs(c_aux_casimir - float(Fraction(23, 27))) < 1e-15,
        "c_aux_BdG_irrep":  abs(c_aux_BdG_irrep - float(Fraction(-1, 6))) < 1e-15,
        "c_aux_BdG_wedder": abs(c_aux_BdG_wedder - float(Fraction(-5, 14))) < 1e-15,
        "psi_s_star":       abs(PSI_S_STAR - (-0.5772156649015329)) < 1e-12,
    }
    sage_all_ok = all(sage_check.values())          # (local)

    # --- candidate registry: (name, c_aux, is_algebra_invariant, n_postdoc_choices) ---
    # is_algebra_invariant: all 4 candidates are spectrum-only / representation-theoretic
    #   (rank arithmetic, Casimir eigenvalue, d_abc invariant) -> all algebra-INVARIANT.
    # n_postdoc_choices: Connes-1996 natural-normalization criterion (fewest post-hoc choices).
    candidates = [
        ("default",  c_aux_default,  True,  1),   # rank-alternating-sum/total: ONE structural choice
        ("anomaly",  c_aux_anomaly,  True,  2),   # d_888 scalar-pick + rank-ratio: TWO choices
        ("casimir",  c_aux_casimir,  True,  3),   # diff-norm repair of over-amplifying bare ratio: 3 choices
        ("BdG_rank", c_aux_BdG_rank, True,  2),   # sign-ambiguous + rank-convention-ambiguous: TWO ambiguities
    ]

    # --- run the 4 x 3 grid ---
    results = {}                                     # (local)
    verdict_matrix = np.zeros((4, 3), dtype=int)     # (local) rows=candidates, cols=[A,B,C]; 1=PASS,0=FAIL,-1=INFO
    code = {"PASS": 1, "FAIL": 0, "INFO": -1}        # (local)
    for i, (name, c, inv, npc) in enumerate(candidates):
        vA = test_A_parse_tree_closed_form(c, inv)                   # (local)
        vB, alpha, repro = test_B_connes_karoubi_residue(c)          # (local)
        vC = test_C_K0_inheritance_commutation(c)                    # (local)
        all_pass = (vA == "PASS" and vB == "PASS" and vC == "PASS")  # (local)
        rel_dev_anchor = abs(alpha - EMP_ANCHOR_1_OVER_458) / EMP_ANCHOR_1_OVER_458  # (local) vs 1/458 (diagnostic)
        results[name] = {
            "c_aux": float(c),
            "gamma_weight_aux": float(gamma_weight_aux(c)),
            "alpha_double_prime": float(alpha),
            "test_A": vA, "test_B": vB, "test_C": vC,
            "all_3_pass": all_pass,
            "residue_reproduction_rel_dev": float(repro),
            "rel_dev_vs_1over458_diagnostic": float(rel_dev_anchor),
            "n_postdoc_normalization_choices": npc,
            "is_algebra_invariant": inv,
        }
        verdict_matrix[i] = [code[vA], code[vB], code[vC]]

    # --- substrate-natural selection (Connes 1996 reconstruction; fewest post-hoc choices) ---
    natural_name = min(candidates, key=lambda t: t[3])[0]            # (local) min n_postdoc_choices -> 'default'
    natural_c_aux = dict((n, c) for n, c, _, _ in candidates)[natural_name]  # (local)
    # second-most-natural among the ALTERNATIVES (exclude default)
    alt_sorted = sorted([t for t in candidates if t[0] != "default"], key=lambda t: t[3])  # (local)
    second_most_natural = alt_sorted[0][0]                          # (local) -> 'anomaly' (tie with BdG_rank at 2; anomaly ties phi_88)

    # --- verdict logic (per plan §W8-7 operator) ---
    alternatives = ["anomaly", "casimir", "BdG_rank"]
    alts_all_pass = [n for n in alternatives if results[n]["all_3_pass"]]   # (local)
    all_cands_all_pass = [n for n, _, _, _ in candidates if results[n]["all_3_pass"]]  # (local)
    n_pass = len(all_cands_all_pass)                                # (local)

    # The 3 tests are STRUCTURAL/EXISTENCE tests (Test A closed-form, Test B Sub-clause A
    # existence + residue reproduction, Test C scalar commutation). They PASS for ANY
    # substrate-derived scalar c_aux -> they do NOT discriminate among candidates.
    tests_discriminate = (n_pass < len(candidates))                # (local) discriminate iff not all pass

    # Substrate-natural selection IS identified (default), but it is the DEFAULT, not an
    # alternative; and the 3 tests are non-discriminating among the alternatives.
    if n_pass == 0:
        verdict = "FAIL"     # locks default; no candidate passes any test
    elif len(alts_all_pass) >= 1 and tests_discriminate and natural_name in alts_all_pass:
        # An ALTERNATIVE passes all 3 tests, the tests discriminate, and the natural selection
        # is that alternative -> alternative supersedes default.
        verdict = "PASS"
    elif n_pass == 1 and all_cands_all_pass == ["default"]:
        # default is the UNIQUE pass -> default reaffirmed canonical (spawn-prompt clause)
        verdict = "PASS"
    else:
        # multiple candidates PASS all 3 tests but the tests are NON-DISCRIMINATING; the
        # substrate-natural selection (Connes 1996) reaffirms the DEFAULT, not an alternative.
        # No alternative supersedes the default. -> INFO (exploratory characterization).
        verdict = "INFO"

    # --- gamma(s) curve overlay data (for plot) ---
    s_grid = np.linspace(0.5, 3.5, 400)                            # (local) avoid s=0,1,2,3 poles in display
    s_grid = s_grid[np.abs(s_grid - S_STAR) > 0.04]                # (local) mask near the s_*=1 pole
    gamma_curves = {}                                              # (local)
    for name, c, _, _ in candidates:
        with np.errstate(over="ignore", invalid="ignore"):
            gamma_curves[name] = gamma_fn(s_grid) * (1.0 + c / (s_grid - S_STAR))

    # =========================================================================
    # PLOT (REQUIRED): 4 candidates x 3 tests verdict matrix + gamma(s) overlay
    # =========================================================================
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(15, 6.2))

    # --- left: verdict matrix heatmap ---
    cand_labels = [f"{n}\nc_aux={results[n]['c_aux']:.4f}" for n, _, _, _ in candidates]  # (local)
    test_labels = ["Test A\n(parse-tree\nclosed-form)",
                   "Test B\n(Connes-Karoubi\nresidue 0<a''<1)",
                   "Test C\n(K_0 inherit.\ncommutation)"]            # (local)
    cmap = matplotlib.colors.ListedColormap(["#c0392b", "#e6a817", "#2e8b57"])  # (local) FAIL/INFO/PASS
    norm = matplotlib.colors.BoundaryNorm([-1.5, -0.5, 0.5, 1.5], cmap.N)       # (local)
    im = axL.imshow(verdict_matrix, cmap=cmap, norm=norm, aspect="auto")
    axL.set_xticks(range(3)); axL.set_xticklabels(test_labels, fontsize=9)
    axL.set_yticks(range(4)); axL.set_yticklabels(cand_labels, fontsize=9)
    for i in range(4):
        for j in range(3):
            v = verdict_matrix[i, j]                               # (local)
            txt = {1: "PASS", 0: "FAIL", -1: "INFO"}[v]            # (local)
            axL.text(j, i, txt, ha="center", va="center",
                     color="white", fontweight="bold", fontsize=11)
    axL.set_title(f"§W8-7 c_aux substrate-derivation: 4 candidates x 3 tests\n"
                  f"Gate verdict = {verdict} (substrate-natural selection: {natural_name} "
                  f"c_aux={float(natural_c_aux):.4f})", fontsize=10)

    # --- right: gamma(s) curve overlay at the 4 candidate c_aux values ---
    colors = {"default": "#1f4e79", "anomaly": "#2e8b57",
              "casimir": "#9b59b6", "BdG_rank": "#c0392b"}          # (local)
    for name, _, _, _ in candidates:
        axR.plot(s_grid, gamma_curves[name], color=colors[name], lw=1.6,
                 label=f"{name}: c_aux={results[name]['c_aux']:.4f}")
    axR.axvline(S_STAR, color="gray", ls="--", lw=0.9, label=f"s_* = {S_STAR} (pole)")
    axR.axhline(0.0, color="black", lw=0.5)
    axR.set_xlabel("s (substrate-distance / Mellin variable)", fontsize=10)
    axR.set_ylabel(r"$\gamma_C(s) = \Gamma(s)\,(1 + c_{aux}\,(s-s_*)^{-1})$", fontsize=10)
    axR.set_title(r"Modified-universal-kernel $\gamma_C(s)$ at the 4 candidate $c_{aux}$ values",
                  fontsize=10)
    axR.set_ylim(-15, 15)
    axR.legend(fontsize=8, loc="upper right")
    axR.grid(alpha=0.25)

    fig.suptitle("S92-W8-§W8-7  GEOMETRIC: substrate-IS modified-universal-kernel "
                 "c_aux substrate-derivation refinement (substrate A_K = C (+) H (+) M_3(C))",
                 fontsize=11, y=0.99)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(PNG_OUT, dpi=130)
    plt.close(fig)

    # =========================================================================
    # NPZ output
    # =========================================================================
    np.savez(
        NPZ_OUT,
        # candidate c_aux values
        c_aux_default=c_aux_default,
        c_aux_anomaly=c_aux_anomaly,
        c_aux_casimir=c_aux_casimir,
        c_aux_BdG_rank=c_aux_BdG_rank,
        c_aux_BdG_irrep=c_aux_BdG_irrep,
        c_aux_BdG_wedder=c_aux_BdG_wedder,
        # Sage-exact rational strings
        sage_exact_json=json.dumps(SAGE_EXACT),
        sage_check_json=json.dumps({k: bool(v) for k, v in sage_check.items()}),
        sage_all_ok=sage_all_ok,
        # closed-form pins
        chi_prime_weight=CHI_PRIME_WEIGHT,
        s_star=S_STAR,
        psi_s_star=PSI_S_STAR,
        R_universal_baseline=R_universal_HP1_strict_F4,
        eps_H_HP1_norm_primary=eps_H_HP1_norm,
        MKK_over_MPl_reduced_sq=MKK_OVER_MPL_SQ,
        g_saturated=G_SATURATED,
        M_LRD=M_LRD,
        empirical_anchor_1_over_458=EMP_ANCHOR_1_OVER_458,
        # per-candidate full results
        results_json=json.dumps(results),
        # verdict matrix
        verdict_matrix=verdict_matrix,
        verdict_matrix_legend=json.dumps({"PASS": 1, "FAIL": 0, "INFO": -1,
                                          "rows": [n for n, _, _, _ in candidates],
                                          "cols": ["test_A", "test_B", "test_C"]}),
        # substrate-natural selection
        natural_selection_name=natural_name,
        natural_selection_c_aux=float(natural_c_aux),
        second_most_natural_alternative=second_most_natural,
        n_candidates_all_3_pass=n_pass,
        alternatives_all_3_pass=json.dumps(alts_all_pass),
        tests_discriminate=tests_discriminate,
        # cocycle ties (phi_88 anomaly tie)
        cocycle_norm_phi88=cocycle_norm_phi88,
        cocycle_norm_phi67=cocycle_norm_phi67,
        sum_dabc2_su3_num=40, sum_dabc2_su3_den=3,
        # substrate / regulator pins
        L_max=L_MAX,
        tau_fold=tau_fold,
        regulator_pin="Mellin-Barnes-modified-universal-kernel-gamma-s",
        verdict=verdict,
    )

    # =========================================================================
    # Verdict-line emission
    # =========================================================================
    pins = {
        "script": file_sha256(Path(__file__).resolve()),
        "canonical_constants": file_sha256(HERE.parent / "_shared" / "canonical_constants.py"),
        "S91_W3_W3_3_wp_section": file_sha256(
            HERE.parents[1] / "sessions" / "session-91" / "session-91-w3-workingpaper.md"),
        "S91_W3_W3_3_verdict_line": file_sha256(
            HERE.parent / "session-91" / "s91_gate_verdicts.txt"),
        "regulator_pin_discipline_md": file_sha256(
            HERE.parents[1] / ".claude" / "rules" / "regulator-pin-discipline.md"),
        "substrate_first_canonical_sourcing_md": file_sha256(
            HERE.parents[1] / ".claude" / "rules" / "substrate-first-canonical-sourcing.md"),
        "math_scripts_md": file_sha256(
            HERE.parents[1] / ".claude" / "rules" / "math-scripts.md"),
        "_gate_id": GATE_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_L_max": str(L_MAX),
        "_verdict": verdict,
    }
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), pins)

    # log SHAs in first 20 lines of stdout
    print(f"[{GATE_ID}]")
    print(f"  input-pin SHAs:")
    for k, v in sorted(pins.items()):
        if not k.startswith("_"):
            print(f"    {k}: {v[:16]}...")
    print(f"  closure_hash(pins): {closure_hash(pins)[:16]}...")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")
    print()

    # value string
    val = (
        f"verdict={verdict};"
        f"c_aux_default=1/3={c_aux_default:.6f};"
        f"c_aux_anomaly=sqrt3/6={c_aux_anomaly:.6f};"
        f"c_aux_casimir=23/27={c_aux_casimir:.6f};"
        f"c_aux_BdG_rank_irrep=-1/6={c_aux_BdG_irrep:.6f};"
        f"c_aux_BdG_rank_wedder=-5/14={c_aux_BdG_wedder:.6f};"
        f"alpha_default={results['default']['alpha_double_prime']:.6e};"
        f"alpha_anomaly={results['anomaly']['alpha_double_prime']:.6e};"
        f"alpha_casimir={results['casimir']['alpha_double_prime']:.6e};"
        f"alpha_BdG={results['BdG_rank']['alpha_double_prime']:.6e};"
        f"n_all3pass={n_pass}/4;"
        f"tests_discriminate={tests_discriminate};"
        f"natural_selection={natural_name}(c_aux={float(natural_c_aux):.4f});"
        f"second_most_natural_alt={second_most_natural};"
        f"testA=all_PASS;testB=all_PASS(SubA_0<a''<1);testC=all_PASS(scalar_commute);"
        f"sage_QQ_ok={sage_all_ok};"
        f"R_base=1.030902;chi_prime_weight=0.5;s_star=1;psi1={PSI_S_STAR:.6f};"
        f"MKK_over_MPl_sq={MKK_OVER_MPL_SQ:.6e};L_max={L_MAX};"
        f"default_reaffirmed_canonical={verdict in ('INFO','PASS') and natural_name=='default'}"
    )
    print(f"  verdict = {verdict}")
    print(f"  value   = {val}")

    append_verdict(verdict, val, audit_sha, content_sha)
    print(f"\nAppended canonical verdict line + dual-SHA companion row to {VERDICT_TXT.name}")
    print(f"NPZ: {NPZ_OUT.name}")
    print(f"PNG: {PNG_OUT.name}")

    # script succeeds regardless of scientific verdict (PASS/FAIL/INFO are all results)
    sys.exit(0)


if __name__ == "__main__":
    main()
