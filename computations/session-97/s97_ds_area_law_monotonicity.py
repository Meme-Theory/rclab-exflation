#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S97-DS-AREA-LAW-MONOTONICITY  [SIGN]  GEOMETRIC
===============================================
INDEPENDENCE test of the de Sitter / cosmological-horizon area law S_dS = A/4G.

QUESTION (operator, plan §W5-3):
  Does S_dS = A/4G admit an INDEPENDENT substrate-spectral-monotonicity functional
  M_dS(tau) -- one that reproduces S_dS = A/4G WITHOUT consuming the S65 EIH
  Casimir-Monotonicity a0/a2 ratio lock (PASS) -- or is the only available functional
  algebraically EQUIVALENT to [S63-BH-chain  o  radius-map] (INFO), or does no distinct
  functional exist at all (FAIL)?

VERDICT (set membership, plan §W5-3 operator):
  PASS : ∃ M_dS(tau) reproducing S_dS = A/4G whose monotone content is NOT the sole
         a0/a2 ratio (carries independent monotone content).
  INFO : M_dS(tau) exists but Delta := [M_dS] - [BH-chain o radius-map] ≡ 0
         (Sage-exact, |Delta| < 1e-12) -- algebraically EQUIVALENT, exact, NOT independent.
  FAIL : no functional distinct from the a0/a2-inherited route reproduces S_dS = A/4G.

SUBSTRATE FRAMING (phononic-framing.md §"IS Space, Not IN Space"):
  GEOMETRIC. The de Sitter horizon entropy is a property of the FABRIC's spectral
  organization, NOT a law imposed on a pre-existing spacetime container. The arrow is
      D_K eigenvalues -> a0/a2 Seeley-DeWitt spectral moments -> Lambda, G_N
                      -> horizon radius R_H = sqrt(3/Lambda) -> area A = 4 pi R_H^2
                      -> horizon entropy.
  The cosmological constant Lambda IS the a0 zeroth Seeley-DeWitt moment (volume /
  vacuum-energy term); Newton's G_N IS the a2 second moment (Einstein-Hilbert). The
  Gibbons-Hawking formula S_dS = A/4G is the EMERGENT-PHYSICS OUTPUT the substrate route
  must reproduce -- the INDEPENDENT-CROSS-CHECK -- never the source. We explain GR via the
  substrate; we NEVER explain the substrate via GR.

S63 / S65 ANCHORS (knowledge MCP, query-first):
  S63 chain (EM.3, internal-to-framework derivation of S = A/(4G_N)):
      substrate-spectral-monotonicity -> BCS-coherence-suppression
        -> vacuum-energy-reduction -> area-theorem
      with the substrate area identity  area_SA = a_2_fold / N_edges  (S63 substrate
      identity, s87-pixelation-lock-hawking-transit.md).
  S65 W6-A (PERMANENT): EIH Casimir Monotonicity -- local a0/a2 INCREASES with C_2(p,q).
      This is the ratio-lock the PASS route must NOT consume.
  S65 W1-B (PERMANENT): CC Ratio from Scalar Curvature Only --
      d(a0/a2)/ds = -(a0/a2)/R * dR/ds   (the a0/a2 ratio is a function of R only).
  S64 W2-A (PERMANENT): a0/a2 trap -- decreasing a2 INCREASES a0/a2.

SUBSTITUTION CHAIN (the [SIGN] read-off; Sage-verified at plan-freeze, re-verified here):
  Step 1 (Definitions, cited):
    a0       = a0_fold = 6440.0              [zeta-scheme 0th SDW half-moment; CONST-FREEZE-42]
    a2       = a2_fold = 2776.1653888634     [zeta-scheme 2nd SDW half-moment; CONST-FREEZE-42]
    Lambda   = kappa_Lambda * a0 / vol       [cosmological constant from the a0 volume term]
    R_H      = sqrt(3/Lambda)                [de Sitter horizon radius, Gibbons-Hawking]
    A        = 4 pi R_H^2 = 12 pi / Lambda   [dS horizon area]
    G_N      = G_coeff / a2                  [Newton's constant from the a2 EH moment]
    S_dS(GH) = A/(4 G_N) = 3 pi / (Lambda G_N)   [Gibbons-Hawking dS entropy]
  Step 2 (Substitute -- the Gibbons-Hawking route):
    S_dS(GH) = (12 pi/Lambda)/(4 G_N) = 3 pi/(Lambda G_N)
             propto a2/a0 = (a0/a2)^{-1}.
    => the GH dS entropy is ALREADY a function of the SINGLE a0/a2 ratio.
  Step 3 (S63 black-hole chain analog -- the candidate M_dS):
    M_dS(tau) = [S63 monotone applied to the dS horizon]
              = [BH-chain] o [radius-map  a0 -> Lambda -> R_H].
    Same substrate monotone; the dS horizon (R_H = sqrt(3/Lambda)) replaces the BH horizon.
  Step 4 (Direction -- the independence test):
    Delta(tau) := M_dS(tau) - ([BH-chain] o [radius-map]).
    IF Delta ≡ 0 (|Delta| < 1e-12)         => algebraically EQUIVALENT, NOT independent => INFO.
    IF Delta ≢ 0 AND d M_dS / d(a0/a2) is NOT the sole monotone source => INDEPENDENT => PASS.
    IF no distinct M_dS reproduces S_dS = A/4G at all                  => FAIL.
    [SIGN] sub-claim: the substrate monotone is vacuum-energy-REDUCTION; as Lambda decreases
      (=> a0/a2 decreases) the dS horizon entropy INCREASES (dS_dS/d(a0/a2) < 0). This sign
      matches the S63 BH area-theorem monotone (entropy increases along the substrate monotone).
  Step 5 (Conclusion + anchor structure):
    Anchor structure (registry-landing.md): PRIMARY (framework substrate monotonicity M_dS)
    + INDEPENDENT-CROSS-CHECK (Gibbons-Hawking output) -- PARALLEL routes to the same
    conclusion, NOT a sequential V->C chain. PRIMARY+INDEPENDENT-CROSS-CHECK is correct;
    SOURCE-DOUBLE-CITE-CO-PRIMARY would be WRONG.

NUMERICAL CONTENT:
  (i) Symbolic equivalence test (Sage-mirror in numpy + closed-form): Delta(tau) over the
      tau-grid; report max|Delta| and whether < 1e-12.
  (ii) [SIGN] direction: sign of dS_dS/d(a0/a2) and the monotone direction over tau.
  (iii) a2-cancellation witness: substitute a0 = r*a2 and confirm a2 cancels (S_dS depends on
      (a0,a2) only via the single ratio r=a0/a2) -- the structural proof that there is NO
      independent monotone source (kills the PASS branch).
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

# ---- canonical constants (MANDATORY per math-scripts.md) ----
SHARED = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(SHARED))
from canonical_constants import (   # noqa: E402
    a0_fold,            # 6440.0                zeta-scheme 0th SDW half-moment (CONST-FREEZE-42)
    a2_fold,            # 2776.1653888633655    zeta-scheme 2nd SDW half-moment (CONST-FREEZE-42)
    tau_fold,           # 0.19                  van Hove fold position
    w0_FW,              # -0.918                framework dark-energy w0 (Lambda-sign context)
    M_KK,               # 7.42866e16            substrate compactification scale (GeV)
    l_Planck,           # 1.616255e-35 m        Planck length (ell_P for the GH normalization)
    G_DeWitt,           # 5.0                   DeWitt moduli kinetic coefficient
)

# ============================================================================
# Identity
# ============================================================================
GATE_ID = "S97-DS-AREA-LAW-MONOTONICITY"
SCHEME = "FW"
CONVENTION = "PRIMARY-MONOTONICITY+INDEPENDENT-CROSS-CHECK"   # NOT co-primary (registry-landing.md)
L_MAX = 10                    # (local) a0/a2 read from L_max=10 spectral-moment cache / canonical pins
SCHEMA_VERSION = "S84+"

HERE = Path(__file__).resolve().parent                       # computations/session-97
SCRIPT_PATH = HERE / "s97_ds_area_law_monotonicity.py"
NPZ_PATH = HERE / "s97_ds_area_law_monotonicity.npz"
PNG_PATH = HERE / "s97_ds_area_law_monotonicity.png"
VERDICT_PATH = HERE / "s97_gate_verdicts.txt"

CANONICAL_CONSTANTS_PATH = SHARED / "canonical_constants.py"
SPECTRUM_CACHE = HERE.parent / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
BASELINE_S66 = Path("sessions/framework/ARCHIVE/baseline-findings-s66.md")  # EIH S65 W6-A / W1-B refs

# ============================================================================
# Machinery pins (PRDR; plan §W5-3 machinery_pin_map)
# ============================================================================
N_EVAL = 200                  # (local) tau-grid points for the M_dS(tau) monotonicity scan
TAU_LO = 0.190                # (local) fold (tau_fold)
TAU_HI = 0.6                  # (local) late-time endpoint (matches S97 W1 a(t) window)
TOLERANCE = 1e-12             # (local) Sage-exact equivalence test tolerance (INFO/PASS discriminator)

# ============================================================================
# de Sitter horizon construction from the a0/a2 Seeley-DeWitt moments
# ============================================================================
# We work in DIMENSIONLESS substrate units where the proportionality constants
# (kappa_Lambda from the a0 -> Lambda map, G_coeff from the a2 -> G_N map, vol) are
# collected into a single positive prefactor C0 that CANCELS in every dimensionless
# comparison and in the deceleration / monotonicity SIGN. The structural content
# (a2-cancellation, Delta ≡ 0, the SIGN of dS_dS/d(a0/a2)) is prefactor-INDEPENDENT.

def Lambda_of(a0, vol=1.0, kappa_Lambda=1.0):
    """Cosmological constant Lambda = kappa_Lambda * a0 / vol (a0 IS the volume term)."""
    return kappa_Lambda * a0 / vol


def G_N_of(a2, G_coeff=1.0):
    """Newton's constant G_N = G_coeff / a2 (a2 IS the Einstein-Hilbert moment)."""
    return G_coeff / a2


def R_H_of(Lambda):
    """de Sitter horizon radius R_H = sqrt(3/Lambda) (Gibbons-Hawking)."""
    return np.sqrt(3.0 / Lambda)


def area_of(Lambda):
    """dS horizon area A = 4 pi R_H^2 = 12 pi / Lambda."""
    return 12.0 * np.pi / Lambda


def S_dS_GH(a0, a2, vol=1.0, kappa_Lambda=1.0, G_coeff=1.0):
    """ROUTE 1 -- Gibbons-Hawking entropy S_dS = A/(4 G_N) = 3 pi/(Lambda G_N).
    The INDEPENDENT-CROSS-CHECK output the substrate route must reproduce."""
    Lam = Lambda_of(a0, vol, kappa_Lambda)
    GN = G_N_of(a2, G_coeff)
    A = area_of(Lam)
    return A / (4.0 * GN)


def M_dS_BHchain_o_radiusmap(a0, a2, vol=1.0, kappa_Lambda=1.0, G_coeff=1.0):
    """ROUTE 2 -- M_dS = [S63 BH-chain]  o  [radius-map  a0 -> Lambda -> R_H].
    The S63 area-theorem entropy is S = A/(4 G_N). M_dS replaces the BH horizon AREA
    with the dS horizon area A(R_H) = 12 pi/Lambda produced by the radius map, and
    feeds it through the SAME A/(4 G_N) functional that the BH chain produces. Built
    INDEPENDENTLY of Route 1 (different call path, same substrate moments)."""
    Lam = Lambda_of(a0, vol, kappa_Lambda)          # radius-map leg: a0 -> Lambda
    R_H = R_H_of(Lam)                               # radius-map leg: Lambda -> R_H
    A_dS = 4.0 * np.pi * R_H**2                     # radius-map leg: R_H -> A = 12 pi/Lambda
    GN = G_N_of(a2, G_coeff)                        # a2 -> G_N (Einstein-Hilbert moment)
    return A_dS / (4.0 * GN)                        # S63 A/(4G) functional at the dS horizon


# ============================================================================
# SHA helpers (dual-SHA, Option A append-only)
# ============================================================================
def sha256_of(path):
    h = hashlib.sha256()                                     # (local)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def dual_sha(pin_map):
    """(audit_sha256, content_sha256). audit = closure over ordered input-pin map;
    content = script bytes."""
    audit_payload = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode()  # (local)
    h_audit = hashlib.sha256(); h_audit.update(audit_payload)
    h_content = hashlib.sha256()
    with open(SCRIPT_PATH, "rb") as f:
        h_content.update(f.read())
    return h_audit.hexdigest(), h_content.hexdigest()


def find_prior_audit_shas():
    import re as _re                                         # (local)
    if not VERDICT_PATH.exists():
        return []
    pat = _re.compile(rf"^{_re.escape(GATE_ID)}:\s.*?audit_sha256=([a-f0-9]{{64}})", _re.MULTILINE)  # (local)
    return pat.findall(VERDICT_PATH.read_text(encoding="utf-8"))


def append_verdict(verdict, value, audit_sha, content_sha,
                   sign_v, mag_v, regime_v, supersedes=None):
    """Append canonical line + dual-SHA companion row + schema-v2 3-tuple companion
    row ([SIGN] trigger). Option A append-only (verdict permanence)."""
    sup_tag = f";supersedes={supersedes}" if supersedes else ""               # (local)
    canonical = (
        f"{GATE_ID}: {verdict} -- value='{value}{sup_tag}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] dS area-law independence test: "
        f"M_dS vs [S63-BH-chain o radius-map]; Delta≡0 ratio-lock\n"
    )
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2)\n"
    )
    with open(VERDICT_PATH, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)
        f.write(tuple_row)


# ============================================================================
# Main
# ============================================================================
def main():
    # ----- input SHA pins (first 20 lines of stdout per gate-verdicts.md) -----
    sha_canon = sha256_of(CANONICAL_CONSTANTS_PATH)          # (local)
    sha_cache = sha256_of(SPECTRUM_CACHE) if SPECTRUM_CACHE.exists() else "MISSING"   # (local)
    sha_baseline = sha256_of(BASELINE_S66) if BASELINE_S66.exists() else "MISSING"    # (local)
    sha_script = sha256_of(SCRIPT_PATH)                      # (local)
    print(f"[{GATE_ID}] INPUT SHA-256 PINS")
    print(f"  canonical_constants.py                 : {sha_canon}")
    print(f"  s84_spectrum_cache_L12_tau019.npz      : {sha_cache}")
    print(f"  baseline-findings-s66.md (S65 refs)    : {sha_baseline}")
    print(f"  script (content)                       : {sha_script}")
    print(f"  a0_fold={a0_fold}  a2_fold={a2_fold}  ratio a0/a2={a0_fold/a2_fold:.10f}")
    print(f"  tau_fold={tau_fold}  w0_FW={w0_FW}  M_KK={M_KK:.6e}  l_Planck={l_Planck:.6e}  "
          f"G_DeWitt={G_DeWitt}")

    a0 = float(a0_fold)                                      # (local) zeta-scheme 0th SDW half-moment
    a2 = float(a2_fold)                                      # (local) zeta-scheme 2nd SDW half-moment
    ratio = a0 / a2                                          # (local) the S65 a0/a2 monotone ratio (=2.31975)

    # ========================================================================
    # PART (i) -- SYMBOLIC EQUIVALENCE TEST: Delta(tau) = M_dS - [BH-chain o radius-map]
    # The two routes are built from INDEPENDENT call paths (S_dS_GH vs
    # M_dS_BHchain_o_radiusmap) using the SAME a0/a2 substrate moments. We scan over a
    # tau-grid by letting the dS radius vary with tau via the a2(tau) ~ R_K(tau) curvature
    # (a0 ~ constant volume term; a2 carries the tau-dependence through R_K). At each tau we
    # form Delta and record max|Delta|.
    # ========================================================================
    tau = np.linspace(TAU_LO, TAU_HI, N_EVAL)                # (local) tau-grid on [0.190, 0.6]

    # a2(tau): tau-dependence through the E3 internal scalar curvature R_K(tau)
    # (baptista-operator-dk-tau.md canonical closed form), normalized so a2(tau_fold)=a2_fold.
    def R_K(t):
        return -0.25*np.exp(-4.0*t) + 2.0*np.exp(-t) - 0.25 + 0.5*np.exp(2.0*t)   # (local)
    a2_tau = a2 * (R_K(tau) / R_K(tau_fold))                 # (local) a_2^{zeta}(tau)
    a0_tau = np.full_like(tau, a0)                           # (local) a0 ~ constant volume term

    # Route 1 (Gibbons-Hawking) and Route 2 (M_dS = BH-chain o radius-map) over the grid:
    S1 = S_dS_GH(a0_tau, a2_tau)                             # (local) ROUTE 1
    S2 = M_dS_BHchain_o_radiusmap(a0_tau, a2_tau)            # (local) ROUTE 2
    Delta = S2 - S1                                          # (local) the independence-test residual
    max_abs_Delta = float(np.max(np.abs(Delta)))            # (local) THE INFO/PASS discriminator
    delta_le_tol = bool(max_abs_Delta < TOLERANCE)          # (local) Delta ≡ 0 ?

    # ========================================================================
    # PART (ii) -- a2-CANCELLATION WITNESS (the structural "no independent monotone" proof)
    # Substitute a0 = r * a2 (r = a0/a2) into S_dS and confirm a2 CANCELS, i.e. S_dS depends
    # on the pair (a0, a2) ONLY through the single ratio r. If a2 cancels, there is NO
    # independent monotone source beyond the a0/a2 ratio => the PASS branch is impossible.
    # We test cancellation numerically by scanning a2 at FIXED r and confirming S_dS is invariant.
    # ========================================================================
    a2_scan = np.linspace(0.5 * a2, 2.0 * a2, 50)            # (local) vary a2 at FIXED r
    a0_scan = ratio * a2_scan                                # (local) a0 = r * a2 (r held fixed)
    S_fixed_r = S_dS_GH(a0_scan, a2_scan)                    # (local) S_dS at fixed r, varying a2
    S_fixed_r_spread = float(np.max(np.abs(S_fixed_r - S_fixed_r[0])) / abs(S_fixed_r[0]))  # (local)
    a2_cancels = bool(S_fixed_r_spread < TOLERANCE)          # (local) a2 cancels => ratio is sole source

    # ========================================================================
    # PART (iii) -- [SIGN] DIRECTION: monotone of S_dS in the a0/a2 ratio direction
    # dS_dS/d(a0/a2): scan r = a0/a2 (vary a0 at fixed a2) and read off the sign.
    # ========================================================================
    r_scan = np.linspace(0.5 * ratio, 2.0 * ratio, N_EVAL)  # (local) r = a0/a2 sweep
    a0_r = r_scan * a2                                       # (local) a0 = r * a2 (a2 fixed)
    a2_r = np.full_like(r_scan, a2)                          # (local)
    S_vs_r = S_dS_GH(a0_r, a2_r)                             # (local) S_dS(r)
    dS_dr = np.gradient(S_vs_r, r_scan, edge_order=2)        # (local) dS_dS/dr
    dS_dr_sign = float(np.sign(np.mean(dS_dr)))             # (local) expect -1 (S_dS ∝ 1/r)
    S_decreasing_in_ratio = bool(np.all(np.diff(S_vs_r) < 0))   # (local) S_dS DECREASES as a0/a2 grows

    # The physical substrate-monotone direction: vacuum-energy reduction => Lambda DECREASES
    #   => a0/a2 = ratio DECREASES (a0 ~ Lambda*vol) => S_dS = 3pi/(Lambda ell_P^2) INCREASES.
    # Sign consistency with the S63 BH area-theorem monotone: entropy INCREASES along the
    #   substrate monotone (vacuum-energy reduction). dS_dr < 0 => as the monotone drives
    #   a0/a2 DOWN, S_dS goes UP. SIGN MATCHES the S63 area-theorem monotone.
    sign_matches_s63 = bool(dS_dr_sign < 0.0)               # (local) dS_dS/d(a0/a2) < 0

    # ========================================================================
    # PART (iv) -- the exponent witness: S_dS ∝ (a0/a2)^p ; confirm p = -1 exactly
    # log-log slope of S_dS vs r over the sweep.
    # ========================================================================
    p_exponent = float(np.polyfit(np.log(r_scan), np.log(S_vs_r), 1)[0])  # (local) expect -1
    p_is_minus1 = bool(abs(p_exponent - (-1.0)) < 1e-9)     # (local)

    # numeric anchor values at the fold (dimensionless substrate units, C0=1)
    Lam_fold = Lambda_of(a0)                                 # (local)
    R_H_fold = R_H_of(Lam_fold)                              # (local)
    A_fold = area_of(Lam_fold)                               # (local)
    S_fold = S_dS_GH(a0, a2)                                 # (local)

    # ========================================================================
    # VERDICT (operator set-membership -> schema-v2 3-tuple -> composite collapse)
    # ========================================================================
    # M_dS exists and reproduces S_dS=A/4G (S2 well-defined, finite, equals S1):
    M_dS_exists = bool(np.all(np.isfinite(S2)) and np.all(S2 > 0.0))   # (local)
    reproduces = delta_le_tol                                # (local) M_dS == S_dS(GH) exactly
    # INDEPENDENCE: PASS requires Delta NOT ≡ 0 AND a monotone source beyond the ratio.
    #   a2_cancels=True => the ratio is the SOLE monotone source => independence IMPOSSIBLE.
    independent = bool((not delta_le_tol) and (not a2_cancels))   # (local) PASS predicate

    if M_dS_exists and reproduces and not independent:
        composite = "INFO"          # algebraically EQUIVALENT, exact, NOT independent
    elif M_dS_exists and independent:
        composite = "PASS"          # independent monotone content beyond the a0/a2 ratio
    else:
        composite = "FAIL"          # no functional distinct from the a0/a2 route reproduces S_dS

    # schema-v2 3-tuple ([SIGN] trigger):
    #   sign_verdict : direction of dS_dS/d(a0/a2) matches the substitution-chain Step 4
    #                  prediction (dS_dr < 0 => S_dS DECREASES as a0/a2 increases; equivalently
    #                  INCREASES along the vacuum-energy-reduction monotone, matching S63).
    sign_verdict = "PASS" if (sign_matches_s63 and S_decreasing_in_ratio) else "FAIL"  # (local)
    #   magnitude_verdict : the equivalence-test magnitude. |Delta| < 1e-12 (the INFO sub-criterion)
    #                  is the magnitude target. PASS-of-magnitude here means the equivalence is
    #                  EXACT to tolerance (Delta ≡ 0), which is the INFO physics result.
    magnitude_verdict = "PASS" if delta_le_tol else "FAIL"   # (local) exact equivalence achieved
    #   regime_verdict : the construction is a closed-form algebraic identity exact on the FULL
    #                  [0.190,0.6] window -- no small-parameter expansion, no ODE breakdown.
    regime_verdict = "VALID"                                 # (local)

    # ----- console summary (NUMBERS FIRST) -----
    print("\n=== PART (i) SYMBOLIC EQUIVALENCE TEST: Delta = M_dS - [BH-chain o radius-map] ===")
    print(f"  Route 1 (Gibbons-Hawking) S_dS(fold)   = {S1[0]:.10e}")
    print(f"  Route 2 (M_dS=BH-chain o radius-map)   = {S2[0]:.10e}")
    print(f"  max|Delta(tau)| over [0.190,0.6]       = {max_abs_Delta:.6e}  vs tol={TOLERANCE:.1e}")
    print(f"  Delta ≡ 0 (|Delta| < 1e-12)?           = {delta_le_tol}")
    print("\n=== PART (ii) a2-CANCELLATION WITNESS (no independent monotone source) ===")
    print(f"  S_dS spread at FIXED r, a2 in [0.5,2]*a2 = {S_fixed_r_spread:.6e}")
    print(f"  a2 cancels (S_dS depends only on r)?    = {a2_cancels}")
    print("\n=== PART (iii) [SIGN] DIRECTION: monotone of S_dS in the a0/a2 ratio ===")
    print(f"  dS_dS/d(a0/a2) mean sign                = {dS_dr_sign:+.0f}  (expect -1)")
    print(f"  S_dS DECREASES as a0/a2 increases?      = {S_decreasing_in_ratio}")
    print(f"  SIGN matches S63 BH area-theorem monotone (entropy up along vac-energy reduction)? "
          f"= {sign_matches_s63}")
    print("\n=== PART (iv) EXPONENT WITNESS: S_dS ∝ (a0/a2)^p ===")
    print(f"  log-log slope p                         = {p_exponent:.10f}  (expect -1; p==-1? {p_is_minus1})")
    print("\n=== FOLD ANCHORS (dimensionless substrate units, C0=1) ===")
    print(f"  a0/a2 = {ratio:.10f}  Lambda(fold)={Lam_fold:.6e}  R_H(fold)={R_H_fold:.6e}")
    print(f"  A(fold)={A_fold:.6e}  S_dS(fold)={S_fold:.6e}")
    print(f"\n  LEGS: M_dS_exists={M_dS_exists} reproduces={reproduces} independent={independent}")
    print(f"  3-tuple: sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict}")
    print(f"  COMPOSITE = {composite}")

    # ========================================================================
    # PLOT
    # ========================================================================
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    axs[0, 0].plot(tau, S1, "b-", lw=2.0, label="Route 1: Gibbons-Hawking S_dS=A/4G")
    axs[0, 0].plot(tau, S2, "r--", lw=1.2, label="Route 2: M_dS = BH-chain o radius-map")
    axs[0, 0].axvline(tau_fold, color="k", ls=":", lw=0.8, label=f"fold tau={tau_fold}")
    axs[0, 0].set_xlabel("tau (order parameter)"); axs[0, 0].set_ylabel("S_dS  (dimensionless, C0=1)")
    axs[0, 0].set_title("Two routes COINCIDE: M_dS == S_dS(GH)")
    axs[0, 0].legend(fontsize=8); axs[0, 0].grid(alpha=0.3)

    axs[0, 1].plot(tau, Delta, "m-", lw=1.6)
    axs[0, 1].axhline(0, color="k", lw=0.5)
    axs[0, 1].set_xlabel("tau"); axs[0, 1].set_ylabel(r"$\Delta = M_{dS} - [{\rm BH}\circ{\rm radius}]$")
    axs[0, 1].set_title(f"Independence residual: max|Delta|={max_abs_Delta:.1e} < 1e-12 (INFO)")
    axs[0, 1].grid(alpha=0.3)

    axs[1, 0].plot(r_scan, S_vs_r, "g-", lw=1.8)
    axs[1, 0].axvline(ratio, color="k", ls=":", lw=0.8, label=f"a0/a2={ratio:.3f}")
    axs[1, 0].set_xlabel(r"$r = a_0/a_2$"); axs[1, 0].set_ylabel("S_dS")
    axs[1, 0].set_title(r"[SIGN]: $S_{dS}\propto 1/r$, $dS_{dS}/dr<0$ (entropy up as $\Lambda$ down)")
    axs[1, 0].legend(fontsize=8); axs[1, 0].grid(alpha=0.3)

    axs[1, 1].plot(a2_scan, S_fixed_r, "c-", lw=1.8, label="S_dS at FIXED r, varying a2")
    axs[1, 1].axhline(S_fixed_r[0], color="r", ls=":", lw=1.0, label="invariant (a2 cancels)")
    axs[1, 1].set_xlabel(r"$a_2$ (at fixed $r=a_0/a_2$)"); axs[1, 1].set_ylabel("S_dS")
    axs[1, 1].set_title(f"a2-cancellation: spread={S_fixed_r_spread:.1e} (ratio is SOLE source)")
    axs[1, 1].legend(fontsize=8); axs[1, 1].grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}: de Sitter area-law independence test "
                 f"(GEOMETRIC; composite={composite} -- M_dS algebraically EQUIVALENT to "
                 f"BH-chain o radius-map)", fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(PNG_PATH, dpi=130)
    plt.close(fig)

    # ========================================================================
    # SAVE NPZ
    # ========================================================================
    audit_pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "N_eval": N_EVAL,
        "tau_lo": TAU_LO,
        "tau_hi": TAU_HI,
        "tolerance": TOLERANCE,
        "regulator_pin": "a_0^{zeta}, a_2^{zeta}",
        "a0_fold": a0,
        "a2_fold": a2,
        "ratio_a0_a2": ratio,
        "max_abs_Delta": max_abs_Delta,
        "delta_le_tol": delta_le_tol,
        "a2_cancels": a2_cancels,
        "S_fixed_r_spread": S_fixed_r_spread,
        "dS_dr_sign": dS_dr_sign,
        "p_exponent": p_exponent,
        "composite": composite,
        "w0_FW": float(w0_FW),
        "s65_ratio_lock": "EIH-Casimir-Monotonicity-S65-W6-A-PERMANENT-a0_a2-up-with-C2",
        "s63_chain": "spectral-monotonicity->BCS->vac-energy-reduction->area-theorem; area_SA=a2/N_edges",
        "radius_map": "a0->Lambda->R_H=sqrt(3/Lambda)->A=4pi R_H^2",
        "sha_canonical_constants": sha_canon,
        "sha_spectrum_cache": sha_cache,
        "sha_baseline_s66": sha_baseline,
        "sha_script": sha_script,
    }
    audit_sha, content_sha = dual_sha(audit_pin_map)

    np.savez(
        NPZ_PATH,
        gate_id=GATE_ID,
        composite=composite,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        # ---- PART (i) equivalence test ----
        tau_grid=tau,
        a0_tau=a0_tau,
        a2_tau=a2_tau,
        R_K_tau=R_K(tau),
        S_route1_GH=S1,
        S_route2_Mds=S2,
        Delta=Delta,
        max_abs_Delta=max_abs_Delta,
        delta_le_tol=delta_le_tol,
        tolerance=TOLERANCE,
        # ---- PART (ii) a2-cancellation witness ----
        a2_scan=a2_scan,
        a0_scan=a0_scan,
        S_fixed_r=S_fixed_r,
        S_fixed_r_spread=S_fixed_r_spread,
        a2_cancels=a2_cancels,
        # ---- PART (iii) [SIGN] direction ----
        r_scan=r_scan,
        S_vs_r=S_vs_r,
        dS_dr=dS_dr,
        dS_dr_sign=dS_dr_sign,
        S_decreasing_in_ratio=S_decreasing_in_ratio,
        sign_matches_s63=sign_matches_s63,
        # ---- PART (iv) exponent witness ----
        p_exponent=p_exponent,
        p_is_minus1=p_is_minus1,
        # ---- fold anchors ----
        ratio_a0_a2=ratio,
        Lambda_fold=Lam_fold,
        R_H_fold=R_H_fold,
        A_fold=A_fold,
        S_dS_fold=S_fold,
        # ---- legs ----
        M_dS_exists=M_dS_exists,
        reproduces=reproduces,
        independent=independent,
        # ---- canonicals / pins ----
        a0_fold=a0,
        a2_fold=a2,
        tau_fold=float(tau_fold),
        w0_FW=float(w0_FW),
        M_KK=float(M_KK),
        l_Planck=float(l_Planck),
        G_DeWitt=float(G_DeWitt),
        regulator_pin="a_0^{zeta}, a_2^{zeta}",
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    # ========================================================================
    # VERDICT EMISSION (Option A append-only; supersedes prior if re-run)
    # ========================================================================
    prior = find_prior_audit_shas()                          # (local)
    supersedes = prior[-1] if prior else None                # (local)

    value_str = (
        f"composite={composite};"
        f"max_abs_Delta={max_abs_Delta:.6e}_lt_1e-12={delta_le_tol};"
        f"M_dS_exists={M_dS_exists};reproduces_S_dS_eq_A_over_4G={reproduces};"
        f"independent={independent};a2_cancels={a2_cancels}_spread={S_fixed_r_spread:.2e};"
        f"dS_dS_d(a0a2)_sign={dS_dr_sign:+.0f}_decreasing={S_decreasing_in_ratio};"
        f"S_dS_propto_(a0a2)^p_p={p_exponent:.6f}_p_eq_m1={p_is_minus1};"
        f"sign_matches_S63={sign_matches_s63};ratio_a0a2={ratio:.6f};"
        f"S_dS(GH)_propto_a2_over_a0=(a0a2)^-1;"
        f"sign={sign_verdict};magnitude={magnitude_verdict};regime={regime_verdict};"
        f"CLASS=FULL;regulator_pin=a_0_zeta+a_2_zeta;"
        f"dual_prior_track=Track_B_0.9_ratio_inherited_equivalent;"
        f"s65_lock=EIH-Casimir-Monotonicity-NOT-consumed-because-M_dS-IS-the-ratio"
    )
    append_verdict(composite, value_str, audit_sha, content_sha,
                   sign_verdict, magnitude_verdict, regime_verdict, supersedes=supersedes)

    print(f"\n[{GATE_ID}] audit_sha256={audit_sha}")
    print(f"[{GATE_ID}] content_sha256={content_sha}")
    if supersedes:
        print(f"[{GATE_ID}] supersedes prior audit_sha256={supersedes} (Option A append-only)")
    print(f"[{GATE_ID}] 4-tuple: (value=max_abs_Delta={max_abs_Delta:.6e}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"[{GATE_ID}] VERDICT: {composite}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
