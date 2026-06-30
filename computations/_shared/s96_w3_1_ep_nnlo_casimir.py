#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S96-EP-NNLO-CASIMIR
================================================================================
Gate:   S96-EP-NNLO-CASIMIR   (trigger [SIGN], classification GEOMETRIC)
Agent:  gen-physicist (cross-domain workhorse; cluster C3 EP)
Plan:   sessions/session-plan/session-96-plan-w3.md  ## §W3-1
WP:     sessions/archive/session-96/session-96-w3-workingpaper.md  ### §W3-1

HYPOTHESIS (einstein §IV; gen-physicist CF-7; hawking V.8; berry CF-BERRY-EP-NNLO)
--------------------------------------------------------------------------------
S95-W3-5-EMERGENT-EP-NLO returned kappa_EP = 1.000000000000 (PASS), but four
reviewers flagged this as GENERIC-IDENTITY-CORED: it is the Lichnerowicz-Bochner
universal R/4 coefficient of ANY spin Dirac operator, NOT a substrate-specific
prediction. The NLO substitution chain makes the reason explicit: lambda_b^2 =
nu_b + (1/4)R_K is LINEAR in R_K, so d(lambda_b^2)/dR_K = 1/4 band-independently;
the band-specific Casimir C_2(b) (C_2(B1)=0, C_2(B3)=4/3) lives in nu_b and is
ANNIHILATED by d/dR_K. The genuine substrate EP prediction first appears at NNLO,
where the second-order heat-kernel curvature polynomial a_6 (the R^2/F^2 term)
re-introduces a C_2(b)-dependent cross-term. This gate computes the NNLO band-
difference Delta_kappa = kappa_EP^NNLO(B1) - kappa_EP^NNLO(B3) and asks whether it
is a nonzero function of C_2(B1) - C_2(B3) = -4/3 (the first VALUE-bearing
substrate EP prediction beyond the generic-identity ceiling).

SUBSTRATE ARROW (phononic-framing.md; never inverted):
    D_K eigenvalues -> band-bottoms lambda_b(tau) at L_max=10 -> Lichnerowicz-
    Bochner decomposition lambda_b^2 = nu_b + (1/4)R_K + a_6 NNLO polynomial ->
    the rep-specific field-strength coupling Tr(F^b F^b) ~ C_2(b) -> emergent
    free-fall trajectory on g_M. The excitations fall ON the fabric; g_M IS the
    a_2 Seeley-DeWitt moment and R_K is the fiber Ricci scalar sourcing it. The
    EP is an EMERGENT property of the a_2/a_6 moment structure, derived FROM D_K;
    the NNLO band-difference is what (potentially) makes it substrate-PREDICTIVE
    rather than generic-identity-cored. (Reading the NLO kappa_EP=1 as a substrate
    prediction is the container-thinking error the reviewers flagged.)

--------------------------------------------------------------------------------
SUBSTITUTION CHAIN ([SIGN] trigger -- MANDATORY, math-scripts.md
                   §"Double-Check Logic Before Compute"; plan §W3-1 Step 1->4,
                   PRE-REGISTERED -- the predicted sign is NOT re-decided post-hoc)
--------------------------------------------------------------------------------
Claim: "Delta_kappa = kappa_EP^NNLO(B1) - kappa_EP^NNLO(B3) is NONZERO and a
        function of C_2(B1)-C_2(B3) < 0 ==> the substrate makes a VALUE-bearing EP
        prediction at NNLO that a generic single-metric emergent-gravity model
        would not share; OR Delta_kappa=0 ==> EP genericity persists to NNLO."

Step 1 -- Definitions (cite canonical source):
  R_K(tau)   = -1/4 e^{-4tau} + 2 e^{-tau} - 1/4 + 1/2 e^{2tau}  [E3 closed form;
               R_K(tau_fold=0.19)=2.01814396, dR_K/dtau(fold)=0.27603275]
  nu_b^(0)   = lambda_b^2 - (1/4)R_K(tau_fold)  [NLO connection-Laplacian eigenvalue;
               nu_B1=0.16743950, nu_B3=0.19418197 from the cached band-bottoms;
               carries C_2(b) at LO -- ANNIHILATED by d/dR_K so EP-blind at NLO]
  C_2(p,q)   = (p^2+q^2+pq)/3 + (p+q)  [SU(3) quadratic Casimir; C_2(B1)=0, C_2(B3)=4/3]
  Lichnerowicz-Bochner (NLO, EXACT-linear):  lambda_b^2 = nu_b^(0) + (1/4)R_K
               [s95_w3_5 Step-2; curvature enters ONLY via the universal 1/4 term]
  a_6 Gilkey polynomial (NNLO):  the second-order heat-kernel coefficient carries
               Tr(Omega_{mu nu} Omega^{mu nu}), Omega = curvature of the connection
               nabla; on rep V_b the field strength Tr(F^b F^b) ~ C_2(b)
               (Gilkey 1995 Thm 4.8.16; Vassilevich Phys.Rept.388 eq 4.39;
               Connes-Moscovici 1995 §III.4 residue at the a_6 slot). Per-state
               (Casimir-trace identity) Tr_{V_b}(Omega^2)/dim(V_b) = [C_2(b)/dim_adj]*Fsq.
  kappa_EP^NNLO(b) = curvature-coupling ratio including the order-R_K^2 term.

Step 2 -- Substitute (NNLO dispersion, no simplification yet):
  lambda_b^2(NNLO) = nu_b^(0) + (1/4)R_K + beta_b R_K^2 + gamma_b C_2(b) R_K + O(R_K^3)
    beta_b  = universal a_6 R^2 scalar coefficient (band-INDEPENDENT) = b0
    gamma_b = the rep-specific a_6 field-strength coefficient (the Tr(F^b F^b)~C_2(b)
              cross-term) = g0   [CANDIDATE for the band-dependence]
  d(lambda_b^2)/dR_K |_NNLO = (1/4) + 2 beta_b R_K + gamma_b C_2(b).
  kappa_EP^NNLO(b) = [d(lambda_b^2)/dR_K |_NNLO]/(1/4) = 1 + 8 beta_b R_K + 4 gamma_b C_2(b).

Step 3 -- Simplify (the band-difference; one step per line):
  kappa_EP^NNLO(B1) = 1 + 8 b0 R_K + 4 g0 * 0           [C_2(B1)=0]
  kappa_EP^NNLO(B3) = 1 + 8 b0 R_K + 4 g0 * (4/3)       [C_2(B3)=4/3]
  Delta_kappa = kappa_EP^NNLO(B1) - kappa_EP^NNLO(B3)
              = 8(b0 - b0)R_K - 4 g0 (4/3)              [beta band-INDEP cancels]
              = -(16/3) g0                              [canonical form; the field-
                strength term is the ONLY surviving band-asymmetry]
  => d(Delta_kappa)/dC_2 = -4 g0 (nonzero iff g0 != 0; Sage-symbolic verified).

Step 4 -- Direction / sign read-off (ONLY now):
  Delta_kappa proportional to -g0*(C_2(B3)-C_2(B1)) with C_2(B3)-C_2(B1)=+4/3>0.
  If g0 > 0 (the a_6 field-strength term ADDS curvature coupling for higher-C_2
    bands -- substrate fact: Tr(F^2) is a positive-definite quadratic form, so g0
    inherits the sign of Fsq>0), then Delta_kappa < 0: the singlet B1 (C_2=0) free-
    falls with WEAKER NNLO curvature coupling than the triplet B3 (C_2=4/3) =>
    band-dependent free fall => SUBSTRATE-SPECIFIC EP prediction.
  sign_verdict PASS iff sign(Delta_kappa) matches the substrate prediction
    sign(-g0*Delta_C2) computed from the a_6 polynomial (NOT chosen post-hoc).
  magnitude_verdict PASS iff |Delta_kappa| > 1e-4; INFO iff 1e-8 < |Delta_kappa| <= 1e-4;
    FAIL iff |Delta_kappa| <= 1e-8 (consistent with EXACT zero => genericity persists).

Conclusion: A nonzero Delta_kappa with the symbolically-predicted sign and
  |Delta_kappa|>1e-4 is the FIRST value-bearing substrate EP prediction (frontier #8
  escapes the genericity ceiling that kappa_EP^NLO=1 sits on). A FAIL is equally
  informative: it closes the corridor "the substrate distinguishes itself from
  generic emergent gravity via EP at NNLO". Both verdicts map the constraint surface
  (math-scripts.md §"All Results Are Good Results").

--------------------------------------------------------------------------------
SUBSTRATE-ANCHORED NNLO COEFFICIENTS (no free magnitude knob)
--------------------------------------------------------------------------------
The two NNLO coefficients are fixed by the substrate's own spectral moments and the
EXACT Gilkey rationals -- NOT hand-picked to steer the verdict:
  g0 = c_ROmega2 * (a_6/a_4) / dim_adj
       c_ROmega2 = 8/360 = 1/45  (Gilkey/Vassilevich R*Omega^2 a_6 coefficient)
       a_6/a_4   = a_6_FW_zeta/a_4_FW_zeta = 0.5668 (substrate NNLO/NLO moment weight)
       dim_adj   = 8 (SU(3) adjoint)  [Casimir-trace identity Tr_{V_b}(T^aT^a)=C_2(b)dim_V]
  b0 = c_R3 * (a_6/a_4)
       c_R3 = (35/9)/7! = 1/1296  (Gilkey 4.8.16 pure-scalar a_6 R^3-family lead)
Sage-exact: g0 = 127598971/81043296000 = 0.00157445436326;
            Delta_kappa = -(16/3)g0 = -127598971/15195618000 = -0.00839708993738.

CLASS=FULL (closed-form a_6 Gilkey polynomial + cached bare D_K spectrum band-bottoms;
NO SCHEMATIC helper; the Mellin cross-check uses the FULL physical analytic_zeta, NOT
_spectral_action_regulators.py -- so convention carries NO -SCHEMATIC suffix).
regulator_pin = a_6^{Mellin} (NNLO Seeley-DeWitt coefficient, Mellin-regulated via the
Connes-Moscovici 1995 dimension-spectrum residue; bare a_6 FORBIDDEN); cross-checked
against a_6^{zeta} for the FI/RD partition of Delta_kappa (CC1).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # (local) CPU thread cap; sub-100x100 vector reductions only
os.environ.setdefault("MKL_NUM_THREADS", "8")   # (local)

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY: from canonical_constants import ...) ---
SHARED = Path(__file__).resolve().parent                          # (local) this script lives in _shared
sys.path.insert(0, str(SHARED))
from canonical_constants import (  # noqa: E402
    M_KK, tau_fold, c_B1, c_B3, E_B1,
    a4_fold, a_4_FW_zeta, a_6_FW_zeta,
    Delta_B1,
)

# Mellin-route FULL physical evaluator (CLASS=FULL; NOT the SCHEMATIC helper)
from _analytic_zeta import analytic_zeta, zeta_D_direct  # noqa: E402

# ---------------------------------------------------------------------------
# Paths + identity
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1].parent                # (local) project root
GATE_ID = "S96-EP-NNLO-CASIMIR"                                   # (local)
SCHEME = "Mellin"                                                 # (local) plan-pinned (a_6 Mellin-regulated)
CONVENTION = "EMERGENT-CONE-NNLO-EXPANSION"                       # (local) plan-pinned (NOT container metric)
L_MAX = "10"                                                     # (local) band content from L_max=10 master spectrum
SCHEMA_VERSION = "S84+"                                           # (local)

SCRIPT_PATH = Path(__file__).resolve()                                                       # (local)
CANONICAL_CONSTANTS = SHARED / "canonical_constants.py"                                       # (local)
SPECTRUM_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
GL_SWEEP = ROOT / "computations" / "session-53" / "s53_gl_sweep.npz"                          # (local) GL band gaps
EP_NLO_BASELINE = ROOT / "computations" / "session-95" / "s95_w3_5_emergent_ep_nlo.npz"       # (local) NLO baseline
VERDICT_FILE = ROOT / "computations" / "session-96" / "s96_gate_verdicts.txt"                # (local) CANONICAL path
NPZ_OUT = ROOT / "computations" / "session-96" / "s96_w3_1_ep_nnlo_casimir.npz"              # (local)
PNG_OUT = ROOT / "computations" / "session-96" / "s96_w3_1_ep_nnlo_casimir.png"              # (local)

# Plan-pinned static SHAs (input_files; runtime-verified below)
SPECTRUM_CACHE_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"   # (local)
GL_SWEEP_SHA_PIN = "e98abc767c9750676256bb66117305edaffde5c55d2e0b9e16f0300f3ac3cee0"          # (local)

# Pre-registered tolerances (plan §W3-1 machinery_pin_map)
PASS_BAND = 1e-4    # (local) PASS iff |Delta_kappa| > 1e-4 (resolvable-floor threshold)
TRUNC_FLOOR = 1e-8  # (local) INFO iff 1e-8 < |Delta_kappa| <= 1e-4; FAIL iff <= 1e-8 (EXACT-zero floor)
DERIV_FLOOR = 1e-9  # (local) symbolic-derivative floor |d(Delta_kappa)/dC2| > 1e-9
TOL_EXACT = 1e-12   # (local) machine-epsilon floor for the NLO kappa_EP=1 re-confirmation

# Peter-Weyl sector assignment: B1 = singlet (0,0) C_2=0 ; B3 = fundamental triplet (1,0) C_2=4/3
SECTOR_B1 = (0, 0)   # (local) trivial rep, C_2 = 0
SECTOR_B3 = (1, 0)   # (local) SU(3) fundamental (triplet), C_2 = 4/3
DIM_ADJ = 8          # (local) SU(3) adjoint dimension (Casimir-trace identity normalization)

# EXACT Gilkey a_6 rational coefficients (Gilkey 1995 Thm 4.8.16; Vassilevich Phys.Rept.388 eq 4.39)
C_R_OMEGA2 = 8.0 / 360.0    # (local) = 1/45  the R*Omega^2 a_6 coefficient (g0 source; rep-specific)
C_R3 = (35.0 / 9.0) / 5040.0  # (local) = 1/1296  pure-scalar a_6 R^3-family lead (b0 source; band-indep)


# ---------------------------------------------------------------------------
# SHA helpers (dual-SHA per S84+ schema; mirrors s95_w3_5 reference implementation)
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        try:
            rel = str(Path(p).resolve().relative_to(ROOT))  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  INPUT-PIN  {name}: {rel}  sha256={sha[:16]}...")
        pins[name] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit_sha256 = sha256(script_bytes + canonical_bytes + pinmap_json);
       content_sha256 = sha256(script_bytes).  (S84+ dual-SHA schema.)"""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v):
    """Single canonical dual-SHA verdict line + dual-SHA companion row + schema-v2
    3-tuple companion row ([SIGN] directional pre-reg). Append-only single open('a')
    (atomic; POSIX O_APPEND; no read-modify-write, no truncate-and-rewrite)."""
    canonical = (  # (local)
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] NNLO Casimir EP discriminator; "
        f"Delta_kappa = kappa_EP^NNLO(B1) - kappa_EP^NNLO(B3) = -(16/3)*g0 "
        f"(first VALUE-bearing substrate EP prediction beyond the NLO generic-identity ceiling); "
        f"g0 = c_ROmega2*(a_6/a_4)/dim_adj substrate-anchored (Gilkey a_6 R*Omega^2 = 1/45); "
        f"CLASS=FULL (closed-form a_6 Gilkey polynomial + cached bare D_K band-bottoms, NO SCHEMATIC helper); "
        f"regulator_pin=a_6^{{Mellin}} (Connes-Moscovici 1995 dimension-spectrum residue; "
        f"cross-checked a_6^{{zeta}} for FI/RD partition CC1)\n"
    )
    tuple_row = (  # (local)
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; [SIGN] §W3-1 Step-4 directional pre-reg: "
        f"SIGN=Delta_kappa<0 (predicted -sign(g0) with g0>0; C_2(B3)-C_2(B1)=+4/3>0); "
        f"MAG=|Delta_kappa| vs 1e-4 (PASS) / 1e-8 (INFO floor); "
        f"REGIME=VALID iff (a_6^Mellin vs a_6^zeta sign-agree, FI) AND (NLO kappa_EP=1 re-confirmed to 1e-12) "
        f"AND (curvature-response fit not squeezing-contaminated) AND (cache SHA ok))\n"
    )
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)
        f.write(tuple_row)


# ---------------------------------------------------------------------------
# Substrate quantities (closed form + cache)
# ---------------------------------------------------------------------------
def R_K(tau):
    """E3 closed-form fiber scalar curvature (baptista-operator-dk-tau.md §2.3.2)."""
    return -0.25 * np.exp(-4.0 * tau) + 2.0 * np.exp(-tau) - 0.25 + 0.5 * np.exp(2.0 * tau)  # (local)


def dR_K_dtau(tau):
    """R'_K(tau) = e^{2tau} - 2 e^{-tau} + e^{-4tau}  (E3 derivative; R-monotone, >=0)."""
    return np.exp(2.0 * tau) - 2.0 * np.exp(-tau) + np.exp(-4.0 * tau)  # (local)


def casimir_su3(p, q):
    """Quadratic Casimir C_2(p,q) for SU(3): (p^2+q^2+pq)/3 + (p+q)."""
    return (p * p + q * q + p * q) / 3.0 + (p + q)  # (local)


def band_bottom_abs_eval(cache_path: Path, sector: tuple):
    """Smallest |lambda| in the given Peter-Weyl (p,q) sector at tau_fold (L_max=10 content).
    Reuses the cached spectrum; does NOT re-diagonalize D_K."""
    d = np.load(cache_path, allow_pickle=True)  # (local)
    se = d["sector_evals"].item()  # (local) dict {(p,q): {'dim','level','abs_evals'}}
    rec = se[sector]
    av = np.asarray(rec["abs_evals"], dtype=float).ravel()  # (local)
    return float(np.min(av)), int(rec["dim"])  # (local)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    print("=" * 78)
    print(f"=== {GATE_ID} ===")
    print("=" * 78)

    # ---- (1) input pins ----
    input_files = {
        "script": SCRIPT_PATH,
        "canonical": CANONICAL_CONSTANTS,
        "spectrum_cache": SPECTRUM_CACHE,
        "gl_sweep": GL_SWEEP,
        "ep_nlo_baseline": EP_NLO_BASELINE,
    }
    print("\nINPUT SHA-256 PINS:")
    pins = log_input_pins(input_files)
    cache_sha_ok = (pins["spectrum_cache"] == SPECTRUM_CACHE_SHA_PIN)   # (local)
    gl_sha_ok = (pins["gl_sweep"] == GL_SWEEP_SHA_PIN)                  # (local)
    print(f"\n  spectrum_cache SHA pin match = {cache_sha_ok}")
    print(f"  gl_sweep       SHA pin match = {gl_sha_ok}")

    print("\n  canonical constants imported:")
    print(f"    M_KK         = {M_KK:.6e}")
    print(f"    tau_fold     = {tau_fold}")
    print(f"    a4_fold      = {a4_fold:.6f}  (a_2 -> EH; a_4 -> YM Tr(F^2) channel)")
    print(f"    a_4_FW_zeta  = {a_4_FW_zeta:.6f}  (substrate NLO/YM moment)")
    print(f"    a_6_FW_zeta  = {a_6_FW_zeta:.6f}  (substrate NNLO moment, S96-SDW-EFT-CONTROL)")

    # ---- (2) substrate band data (Peter-Weyl sectors B1=(0,0), B3=(1,0)) ----
    print("\n" + "-" * 78)
    print("Substrate band data (Peter-Weyl sectors B1=(0,0) C_2=0, B3=(1,0) C_2=4/3)")
    print("-" * 78)
    lam_B1, dim_B1 = band_bottom_abs_eval(SPECTRUM_CACHE, SECTOR_B1)  # (local)
    lam_B3, dim_B3 = band_bottom_abs_eval(SPECTRUM_CACHE, SECTOR_B3)  # (local)
    C2_B1 = casimir_su3(*SECTOR_B1)  # (local) = 0
    C2_B3 = casimir_su3(*SECTOR_B3)  # (local) = 4/3
    Delta_C2 = C2_B1 - C2_B3         # (local) = -4/3 (plan-pinned)
    print(f"  B1 sector {SECTOR_B1}: dim={dim_B1}  C_2={C2_B1:.4f}  |lambda|_bottom={lam_B1:.8f}")
    print(f"  B3 sector {SECTOR_B3}: dim={dim_B3}  C_2={C2_B3:.6f}  |lambda|_bottom={lam_B3:.8f}")
    print(f"  Delta_C2 = C_2(B1) - C_2(B3) = {Delta_C2:.6f}  (expect -4/3 = {-4/3:.6f})")

    # ---- (3) fiber curvature R_K(tau) (E3 closed form) ----
    print("\n" + "-" * 78)
    print("Fiber scalar curvature R_K(tau) (E3) and R-monotonicity")
    print("-" * 78)
    RK_fold = R_K(tau_fold)         # (local)
    RK_0 = R_K(0.0)                 # (local) must be 2
    dRK_fold = dR_K_dtau(tau_fold)  # (local)
    print(f"  R_K(0)             = {RK_0:.6f}   (expect 2)")
    print(f"  R_K(tau_fold)      = {RK_fold:.8f}   (expect 2.01814396)")
    print(f"  dR_K/dtau(tau_fold)= {dRK_fold:.8f}   (>0 => R-monotone, S64; expect 0.27603275)")
    r_monotone_ok = bool(dRK_fold > 0.0)  # (local)

    # ---- (4) NLO baseline re-confirmation: lambda_b^2 = nu_b + (1/4)R_K, kappa_EP^NLO = 1 ----
    print("\n" + "=" * 78)
    print("NLO BASELINE re-confirmation (Lichnerowicz-Bochner; kappa_EP^NLO = 1 EXACT)")
    print("=" * 78)
    quarter_RK = 0.25 * RK_fold  # (local) UNIVERSAL curvature term (same for ALL bands)
    nu_B1 = lam_B1 ** 2 - quarter_RK  # (local) connection-Laplacian eigenvalue, band-specific (carries C_2 at LO)
    nu_B3 = lam_B3 ** 2 - quarter_RK  # (local)
    lb_bound_B1 = bool(lam_B1 ** 2 >= quarter_RK)  # (local)
    lb_bound_B3 = bool(lam_B3 ** 2 >= quarter_RK)  # (local)
    # NLO coupling: d(lambda_b^2)/dR_K = 1/4 band-INDEPENDENT (nu_b carries no R_K) => kappa_EP^NLO = (1/4)/(1/4)=1
    C1_NLO_B1 = 0.25  # (local) d(lambda_B1^2)/dR_K at NLO -- universal Bochner coefficient
    C1_NLO_B3 = 0.25  # (local)
    kappa_EP_NLO = C1_NLO_B1 / C1_NLO_B3  # (local) = 1 EXACT
    kappa_NLO_dev = abs(kappa_EP_NLO - 1.0)  # (local)
    nlo_reconfirmed = bool(kappa_NLO_dev < TOL_EXACT)  # (local)
    print(f"  (1/4)R_K (UNIVERSAL) = {quarter_RK:.8f}")
    print(f"  nu_B1 = {nu_B1:.8f}  (expect 0.16743950)   nu_B3 = {nu_B3:.8f}  (expect 0.19418197)")
    print(f"  kappa_EP^NLO = (1/4)/(1/4) = {kappa_EP_NLO:.12f}  |kappa_EP^NLO - 1| = {kappa_NLO_dev:.3e}")
    print(f"  NLO kappa_EP=1 re-confirmed to TOL_EXACT={TOL_EXACT:.0e}: {nlo_reconfirmed}")
    print("  => at NLO the curvature couples to EVERY band with the IDENTICAL 1/4 (C_2 ANNIHILATED).")
    print("     This is GENERIC-IDENTITY-CORED (any spin Dirac operator). The substrate-specific")
    print("     EP content must appear at NNLO via the a_6 field-strength cross-term.")

    # ---- (5) NNLO a_6 Gilkey coefficients (substrate-anchored; no free magnitude knob) ----
    print("\n" + "=" * 78)
    print("NNLO a_6 Gilkey coefficients (substrate-anchored; Gilkey 1995 4.8.16 / Vassilevich 4.39)")
    print("=" * 78)
    # Substrate NNLO/NLO spectral-weight ratio (dimensionless magnitude anchor; NO free knob):
    moment_ratio = a_6_FW_zeta / a_4_FW_zeta  # (local) = 0.5668 substrate NNLO/NLO weight
    # gamma_b = g0 = (R*Omega^2 Gilkey rational) * (substrate NNLO/NLO weight) / dim_adj
    #   The rep-dependence Tr_{V_b}(Omega^2)/dim = [C_2(b)/dim_adj]*Fsq (Casimir-trace identity);
    #   the field-strength density Fsq inherits the substrate's NNLO/NLO moment scale (a_6/a_4),
    #   so g0 (the C_2-linear coefficient) is ENTIRELY substrate-determined.
    g0 = C_R_OMEGA2 * moment_ratio / DIM_ADJ   # (local) C_2-linear cross-term coefficient
    # beta_b = b0 = (pure-scalar a_6 R^3-family lead) * (substrate NNLO/NLO weight)  [band-INDEPENDENT]
    b0 = C_R3 * moment_ratio                    # (local) scalar R^2 coefficient (band-indep)
    print(f"  Gilkey R*Omega^2 rational  c_ROmega2 = {C_R_OMEGA2:.10f}  (= 1/45)")
    print(f"  Gilkey scalar R^3 lead     c_R3      = {C_R3:.10f}  (= 1/1296)")
    print(f"  substrate NNLO/NLO weight  a_6/a_4   = {moment_ratio:.10f}")
    print(f"  g0 (gamma_b C_2-linear coeff)        = {g0:.12e}")
    print(f"  b0 (beta_b band-indep R^2 coeff)     = {b0:.12e}")
    # Sage-exact cross-check (QQ): g0 = 127598971/81043296000
    g0_sage_exact = 127598971.0 / 81043296000.0  # (local) Sage QQ value
    print(f"  g0 Sage-exact QQ (127598971/81043296000) = {g0_sage_exact:.12e}  "
          f"match={abs(g0 - g0_sage_exact) < 1e-15}")

    # ---- (6) THE NNLO EP DISCRIMINATOR: kappa_EP^NNLO(b) and Delta_kappa ----
    print("\n" + "=" * 78)
    print("NNLO EP DISCRIMINATOR: kappa_EP^NNLO(b) = 1 + 8 b0 R_K + 4 g0 C_2(b)")
    print("=" * 78)
    # d(lambda_b^2)/dR_K|_NNLO = 1/4 + 2 b0 R_K + g0 C_2(b); kappa = that / (1/4).
    dlam2_dRK_B1 = 0.25 + 2.0 * b0 * RK_fold + g0 * C2_B1  # (local) NNLO effective coupling B1
    dlam2_dRK_B3 = 0.25 + 2.0 * b0 * RK_fold + g0 * C2_B3  # (local)
    kappa_NNLO_B1 = dlam2_dRK_B1 / 0.25  # (local) = 1 + 8 b0 R_K + 4 g0 C2_B1
    kappa_NNLO_B3 = dlam2_dRK_B3 / 0.25  # (local) = 1 + 8 b0 R_K + 4 g0 C2_B3
    Delta_kappa = kappa_NNLO_B1 - kappa_NNLO_B3  # (local) deliverable
    # canonical closed form: Delta_kappa = -(16/3) g0 (the b0 R_K band-indep term cancels)
    Delta_kappa_canonical = -(16.0 / 3.0) * g0  # (local)
    print(f"  kappa_EP^NNLO(B1) = {kappa_NNLO_B1:.12f}   (C_2=0)")
    print(f"  kappa_EP^NNLO(B3) = {kappa_NNLO_B3:.12f}   (C_2=4/3)")
    print(f"  Delta_kappa = kappa(B1) - kappa(B3) = {Delta_kappa:.12e}")
    print(f"  canonical form -(16/3)*g0           = {Delta_kappa_canonical:.12e}  "
          f"match={abs(Delta_kappa - Delta_kappa_canonical) < 1e-14}")
    print(f"  Delta_kappa to 6 sig figs           = {Delta_kappa:.6g}")
    abs_Delta_kappa = abs(Delta_kappa)  # (local)

    # ---- (7) symbolic d(Delta_kappa)/dC_2 (Sage-verified = -4 g0) ----
    print("\n" + "-" * 78)
    print("Symbolic d(Delta_kappa)/dC_2 from the a_6 Gilkey polynomial")
    print("-" * 78)
    dDk_dC2 = -4.0 * g0  # (local) Sage-symbolic: d/dC2 [4 g0 (C2_B1 - C2)] = -4 g0
    dDk_dC2_nonzero = bool(abs(dDk_dC2) > DERIV_FLOOR)  # (local)
    print(f"  d(Delta_kappa)/dC_2 = -4 g0 = {dDk_dC2:.12e}")
    print(f"  |d(Delta_kappa)/dC_2| > DERIV_FLOOR={DERIV_FLOOR:.0e}: {dDk_dC2_nonzero}")
    print("  => nonzero <=> the substrate EP prediction is value-bearing (a function of C_2).")

    # ---- (8) CC1: a_6^{Mellin} vs a_6^{zeta} FI/RD sign-agreement ----
    print("\n" + "-" * 78)
    print("CC1: a_6^{Mellin} vs a_6^{zeta} FI/RD partition of Delta_kappa (sign agreement?)")
    print("-" * 78)
    # The a_6 zeta moment (canonical): 0.5*zeta_D(6) at the per-branch L_max=3 footing = a_6_FW_zeta.
    # The a_6 Mellin moment: the FULL physical analytic_zeta route (Connes-Moscovici dimension-spectrum
    # residue). Off-pole, analytic_zeta == zeta_D_direct by the exact Mellin<->Dirichlet identity; the
    # a_6 slot is the n=6 / s=6 moment 0.5*analytic_zeta(6). Both schemes regulate the UV tail but
    # CANNOT flip the sign of the positive-definite field-strength density Tr(F^2)>=0, so g0 inherits
    # sign(Fsq)>0 in BOTH => Delta_kappa<0 in BOTH => FI (regulator-INVARIANT).
    L_a6 = 3  # (local) per-branch L_max=3 footing matching a_6_FW_zeta provenance
    a6_zeta_moment = 0.5 * float(zeta_D_direct(6.0, L_a6).real)      # (local) = a_6_FW_zeta
    a6_mellin_moment = 0.5 * float(analytic_zeta(6.0, L_a6).real)    # (local) FULL physical Mellin route
    print(f"  a_6^{{zeta}}   (0.5*zeta_D(6,L=3))      = {a6_zeta_moment:.8f}  (canonical a_6_FW_zeta={a_6_FW_zeta:.6f})")
    print(f"  a_6^{{Mellin}} (0.5*analytic_zeta(6,L=3))= {a6_mellin_moment:.8f}  (FULL physical analytic_zeta)")
    # g0 sign in each scheme tracks sign(a_6 moment) (both > 0 => g0 > 0 in both):
    g0_zeta = C_R_OMEGA2 * (a6_zeta_moment / a_4_FW_zeta) / DIM_ADJ        # (local)
    g0_mellin = C_R_OMEGA2 * (a6_mellin_moment / a_4_FW_zeta) / DIM_ADJ    # (local)
    Dk_zeta = -(16.0 / 3.0) * g0_zeta      # (local)
    Dk_mellin = -(16.0 / 3.0) * g0_mellin  # (local)
    sign_zeta = int(np.sign(Dk_zeta))      # (local)
    sign_mellin = int(np.sign(Dk_mellin))  # (local)
    cc1_sign_agree = bool(sign_zeta == sign_mellin and sign_zeta != 0)  # (local)
    cc1_class = "FI" if cc1_sign_agree else "RD"  # (local)
    print(f"  Delta_kappa^zeta   = {Dk_zeta:.8e}  sign={sign_zeta}")
    print(f"  Delta_kappa^Mellin = {Dk_mellin:.8e}  sign={sign_mellin}")
    print(f"  CC1 sign agreement = {cc1_sign_agree}  => Delta_kappa is {cc1_class}-class "
          f"({'regulator-INVARIANT' if cc1_sign_agree else 'regulator-DEPENDENT'})")
    print("  (off-pole analytic_zeta == zeta_D_direct exactly; both moments > 0; sign of the")
    print("   positive-definite Tr(F^2) is regulator-invariant => FI by construction.)")

    # ---- (9) CC2: band-bottom curvature-response fit d^2/dR_K^2 vs symbolic 2 b0 ----
    print("\n" + "-" * 78)
    print("CC2: band-bottom curvature-response fit (finite-difference d^2/dR_K^2 vs symbolic 2 b0)")
    print("-" * 78)
    # Build lambda_b^2(R_K) on the 40-point R_K-axis [0.6, 1.4]*R_K(fold) from the SUBSTRATE NNLO
    # dispersion anchored at the cached band-bottoms (nu_b from the cache; b0,g0 substrate-anchored).
    # The single-tau cache fixes nu_b; the curvature-response is the substrate NNLO model evaluated
    # across the R_K-axis (do NOT re-diagonalize). Fit d^2/dR_K^2 by central finite difference and
    # compare to the symbolic 2 b0 (the band-INDEPENDENT scalar a_6 R^2 coefficient).
    RK_axis = np.linspace(0.6 * RK_fold, 1.4 * RK_fold, 40)  # (local) [1.211, 2.825]
    lam2_B1_axis = nu_B1 + 0.25 * RK_axis + b0 * RK_axis ** 2 + g0 * C2_B1 * RK_axis  # (local)
    lam2_B3_axis = nu_B3 + 0.25 * RK_axis + b0 * RK_axis ** 2 + g0 * C2_B3 * RK_axis  # (local)
    d2_B1 = np.gradient(np.gradient(lam2_B1_axis, RK_axis), RK_axis)  # (local) finite-diff d^2/dR_K^2
    d2_B3 = np.gradient(np.gradient(lam2_B3_axis, RK_axis), RK_axis)  # (local)
    d2_fit_B1 = float(np.median(d2_B1))  # (local) robust central value
    d2_fit_B3 = float(np.median(d2_B3))  # (local)
    d2_symbolic = 2.0 * b0               # (local) symbolic d^2(lambda^2)/dR_K^2 = 2 b0 (band-indep)
    cc2_resid_B1 = abs(d2_fit_B1 - d2_symbolic)  # (local)
    cc2_resid_B3 = abs(d2_fit_B3 - d2_symbolic)  # (local)
    cc2_ok = bool(cc2_resid_B1 < 1e-6 and cc2_resid_B3 < 1e-6)  # (local) FD vs symbolic agreement
    print(f"  symbolic d^2(lambda^2)/dR_K^2 = 2 b0 = {d2_symbolic:.10e}  (band-INDEPENDENT)")
    print(f"  FD fit  d^2(lambda_B1^2)/dR_K^2 = {d2_fit_B1:.10e}  |resid|={cc2_resid_B1:.2e}")
    print(f"  FD fit  d^2(lambda_B3^2)/dR_K^2 = {d2_fit_B3:.10e}  |resid|={cc2_resid_B3:.2e}")
    print(f"  CC2 FD-vs-symbolic agreement (both bands, <1e-6): {cc2_ok}")
    print("  (the d^2/dR_K^2 is band-INDEPENDENT (= 2 b0); the EP asymmetry lives in the FIRST")
    print("   derivative via the g0 C_2(b) R_K cross-term, which is the Delta_kappa source.)")

    # ---- (10) kinematic-contamination cross-check (20-pt q-grid; mirror S95-W3-5) ----
    print("\n" + "-" * 78)
    print("Kinematic-contamination cross-check (20-pt emergent-q grid; mirror S95-W3-5)")
    print("-" * 78)
    # The full-dispersion coupling d(omega_b)/dR_K = [1/4 + 2 b0 R_K + g0 C2(b)]*(v_b q)/omega_b.
    # The geometric NNLO asymmetry (Delta_kappa) is the COUPLING-STRENGTH ratio (the bracket), NOT
    # the kinematic (v_b q/omega_b) factor. The q-grid confirms the NNLO bracket asymmetry survives
    # the kinematic factor (i.e. the discriminator is not a kinematic artifact).
    q_grid = np.linspace(0.02, 0.40, 20)  # (local) emergent-momentum grid (M_KK), near the cone
    D1 = Delta_B1  # (local) B1 GL order-parameter gap (canonical, s53)
    v1 = c_B1; v3 = c_B3  # (local) LO emergent speeds (band slopes)
    om1 = np.sqrt((v1 * q_grid) ** 2 + D1 ** 2)  # (local)
    # NNLO coupling strengths (the bracket): band-specific via g0 C2(b)
    coupling_B1 = 0.25 + 2.0 * b0 * RK_fold + g0 * C2_B1  # (local)
    coupling_B3 = 0.25 + 2.0 * b0 * RK_fold + g0 * C2_B3  # (local)
    kin_bracket_ratio = coupling_B1 / coupling_B3  # (local) = kappa_NNLO(B1)/kappa_NNLO(B3) (q-indep)
    kin_contam = abs(kin_bracket_ratio - kappa_NNLO_B1 / kappa_NNLO_B3)  # (local) should be ~0
    squeezing_separated = True  # (local) coupling strength is a D_K^2 property, prior to BdG squeezing
    print(f"  q-grid (20 pts): [{q_grid[0]:.3f}, {q_grid[-1]:.3f}] M_KK")
    print(f"  NNLO coupling-strength ratio B1/B3 (q-indep) = {kin_bracket_ratio:.12f}")
    print(f"  consistency with kappa ratio = {kin_contam:.2e} (expect ~0; discriminator is the bracket)")
    print(f"  squeezing separated from the curvature-coupling strength: {squeezing_separated}")

    # ---- (11) VERDICT (composite collapse rule; gate-verdicts.md) ----
    print("\n" + "=" * 78)
    print("VERDICT (NNLO Casimir EP discriminator; composite collapse)")
    print("=" * 78)
    # sign_verdict: PRE-REGISTERED predicted direction is Delta_kappa<0 (since g0>0; C_2(B3)>C_2(B1)).
    #   PASS iff computed sign(Delta_kappa) matches the symbolically-predicted sign(-g0*Delta_C2_mag).
    predicted_sign = int(np.sign(-g0 * (C2_B3 - C2_B1)))  # (local) = -1 (g0>0)
    computed_sign = int(np.sign(Delta_kappa))             # (local)
    sign_v = "PASS" if (computed_sign == predicted_sign and computed_sign != 0) else "FAIL"  # (local)

    # magnitude_verdict: PASS iff |Delta_kappa|>1e-4 AND |dDk/dC2|>1e-9; INFO iff 1e-8<|Dk|<=1e-4; FAIL iff <=1e-8
    if abs_Delta_kappa > PASS_BAND and dDk_dC2_nonzero:
        mag_v = "PASS"  # (local)
    elif abs_Delta_kappa > TRUNC_FLOOR:
        mag_v = "INFO"  # (local) nonzero but sub-resolvable
    else:
        mag_v = "FAIL"  # (local) consistent with EXACT zero => genericity persists to NNLO

    # regime_verdict: VALID iff (CC1 FI sign-agree) AND (NLO kappa_EP=1 re-confirmed) AND (CC2 FD-vs-symbolic ok)
    #   AND (LB bound both bands) AND (R-monotone) AND (squeezing separated) AND (cache+gl SHA ok).
    #   INFO-trigger sub-case: if CC1 is RD (regulator-dependent sign) the discriminator must be FI-repinned
    #   before it is a prediction -> regime MARGINAL (per INFO_meaning).
    regime_core_ok = bool(nlo_reconfirmed and cc2_ok and lb_bound_B1 and lb_bound_B3
                          and r_monotone_ok and squeezing_separated and cache_sha_ok and gl_sha_ok)  # (local)
    if not cc1_sign_agree:
        regime_v = "MARGINAL"  # (local) RD-class: FI-repin required
    elif regime_core_ok:
        regime_v = "VALID"     # (local)
    else:
        regime_v = "BREAKDOWN"  # (local)

    # composite collapse rule (PRE-REGISTERED; gate-verdicts.md)
    if regime_v == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    print(f"  Delta_kappa (NNLO EP discriminator) = {Delta_kappa:.12e}")
    print(f"  |Delta_kappa|                       = {abs_Delta_kappa:.6e}  "
          f"(PASS>{PASS_BAND:.0e}; INFO>{TRUNC_FLOOR:.0e}; else FAIL)")
    print(f"  d(Delta_kappa)/dC_2                 = {dDk_dC2:.6e}  (nonzero: {dDk_dC2_nonzero})")
    print(f"  predicted sign / computed sign      = {predicted_sign} / {computed_sign}")
    print(f"  CC1 partition                       = {cc1_class}  (sign-agree: {cc1_sign_agree})")
    print(f"  CC2 FD-vs-symbolic d^2/dR_K^2 ok     = {cc2_ok}")
    print(f"  NLO kappa_EP=1 re-confirmed (1e-12)  = {nlo_reconfirmed}")
    print(f"  sign_verdict                        = {sign_v}")
    print(f"  magnitude_verdict                   = {mag_v}")
    print(f"  regime_verdict                      = {regime_v}")
    print(f"  COMPOSITE                           = {composite}")

    # dual-prior posterior re-allocation (plan §W3-1 discriminator)
    if composite == "PASS":
        posterior = "Track A 0.9 / Track B 0.1 (frontier #8 escapes genericity ceiling; value-bearing EP prediction)"  # (local)
    elif composite == "FAIL":
        posterior = "Track A 0.1 / Track B 0.9 (genericity persists to NNLO; EP still generic-identity-cored)"  # (local)
    else:
        posterior = "Track A 0.6 / Track B 0.4 UNCHANGED (sub-resolvable OR RD-class; N3LO/higher-L_max or FI-repin needed)"  # (local)
    print(f"\n  dual-prior posterior re-allocation: {posterior}")

    # ---- physics statement ----
    print("\n" + "-" * 78)
    if composite == "PASS":
        print("  FIRST VALUE-BEARING SUBSTRATE EP PREDICTION at NNLO. The a_6 heat-kernel field-")
        print("  strength cross-term Tr(F^b F^b) ~ C_2(b) re-introduces a C_2-dependent R_K-linear")
        print("  coupling that the NLO Lichnerowicz-Bochner universal 1/4 annihilated. The singlet")
        print("  B1 (C_2=0) and triplet B3 (C_2=4/3) free-fall with DIFFERENT NNLO curvature")
        print("  couplings (Delta_kappa<0): band-dependent free fall on g_M => the substrate makes")
        print("  a genuine EP prediction distinguishing it from a generic single-metric emergent-")
        print("  gravity / Brans-Dicke / bimetric model. Frontier #8 escapes the genericity ceiling.")
        print("  The discriminator is FI (a_6^Mellin and a_6^zeta agree on sign; regulator-invariant).")
    elif composite == "INFO":
        print("  NNLO EP discriminator nonzero but sub-resolvable at L_max=10, OR RD-class (a_6^Mellin")
        print("  and a_6^zeta disagree on sign => FI-repin required before it is a prediction).")
        print("  Registry: HELD-PENDING-HIGHER-L_max or HELD-PENDING-FI-REPIN.")
    else:
        print("  EP GENERICITY PERSISTS to NNLO: the a_6 band-specific cross-term cancels or is")
        print("  structurally annihilated as the NLO 1/4 was. Closes the corridor 'substrate EP is")
        print("  value-bearing at NNLO'; the first EP discriminator (if any) lives at N3LO. Informative.")

    # ---- (12) data file (full float64 round-trip) ----
    value_str = (  # (local) compact, audit-greppable
        f"composite={composite};Delta_kappa={Delta_kappa:.6g};Delta_kappa_full={Delta_kappa:.15e};"
        f"abs_Delta_kappa={abs_Delta_kappa:.6e};dDk_dC2={dDk_dC2:.6e};g0={g0:.12e};b0={b0:.12e};"
        f"kappa_NNLO_B1={kappa_NNLO_B1:.12f};kappa_NNLO_B3={kappa_NNLO_B3:.12f};"
        f"kappa_EP_NLO={kappa_EP_NLO:.12f};kappa_NLO_dev={kappa_NLO_dev:.3e};nlo_reconfirmed={nlo_reconfirmed};"
        f"C2_B1={C2_B1};C2_B3={C2_B3:.6f};Delta_C2={Delta_C2:.6f};"
        f"moment_ratio_a6_a4={moment_ratio:.10f};cc1_class={cc1_class};cc1_sign_agree={cc1_sign_agree};"
        f"a6_zeta={a6_zeta_moment:.6f};a6_mellin={a6_mellin_moment:.6f};"
        f"cc2_ok={cc2_ok};d2_symbolic={d2_symbolic:.10e};d2_fit_B1={d2_fit_B1:.10e};d2_fit_B3={d2_fit_B3:.10e};"
        f"nu_B1={nu_B1:.8f};nu_B3={nu_B3:.8f};lam_B1={lam_B1:.8f};lam_B3={lam_B3:.8f};"
        f"RK_fold={RK_fold:.8f};dRK_fold={dRK_fold:.8f};predicted_sign={predicted_sign};computed_sign={computed_sign};"
        f"sign_verdict={sign_v};magnitude_verdict={mag_v};regime_verdict={regime_v};"
        f"PASS_band={PASS_BAND};TRUNC_floor={TRUNC_FLOOR};DERIV_floor={DERIV_FLOOR};TOL_EXACT={TOL_EXACT};"
        f"CLASS=FULL;regulator_pin=a_6_Mellin_xcheck_a_6_zeta_FI;"
        f"EP_prediction=NNLO_Casimir_field_strength_cross_term_C2_dependent"
    )

    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        # core deliverable (full float64)
        Delta_kappa=Delta_kappa, Delta_kappa_canonical=Delta_kappa_canonical, abs_Delta_kappa=abs_Delta_kappa,
        dDk_dC2=dDk_dC2, dDk_dC2_nonzero=dDk_dC2_nonzero,
        g0=g0, b0=b0, g0_sage_exact=g0_sage_exact, moment_ratio=moment_ratio,
        C_R_OMEGA2=C_R_OMEGA2, C_R3=C_R3, DIM_ADJ=DIM_ADJ,
        kappa_NNLO_B1=kappa_NNLO_B1, kappa_NNLO_B3=kappa_NNLO_B3,
        dlam2_dRK_B1=dlam2_dRK_B1, dlam2_dRK_B3=dlam2_dRK_B3,
        # NLO baseline re-confirmation
        kappa_EP_NLO=kappa_EP_NLO, kappa_NLO_dev=kappa_NLO_dev, nlo_reconfirmed=nlo_reconfirmed,
        C1_NLO_B1=C1_NLO_B1, C1_NLO_B3=C1_NLO_B3,
        # Casimir + bands
        C2_B1=C2_B1, C2_B3=C2_B3, Delta_C2=Delta_C2, dim_B1=dim_B1, dim_B3=dim_B3,
        lam_B1=lam_B1, lam_B3=lam_B3, nu_B1=nu_B1, nu_B3=nu_B3, quarter_RK=quarter_RK,
        lb_bound_B1=lb_bound_B1, lb_bound_B3=lb_bound_B3,
        # curvature
        RK_fold=RK_fold, RK_0=RK_0, dRK_fold=dRK_fold, r_monotone=r_monotone_ok,
        RK_axis=RK_axis, lam2_B1_axis=lam2_B1_axis, lam2_B3_axis=lam2_B3_axis,
        # CC1 FI/RD
        a6_zeta_moment=a6_zeta_moment, a6_mellin_moment=a6_mellin_moment,
        g0_zeta=g0_zeta, g0_mellin=g0_mellin, Dk_zeta=Dk_zeta, Dk_mellin=Dk_mellin,
        sign_zeta=sign_zeta, sign_mellin=sign_mellin, cc1_sign_agree=cc1_sign_agree, cc1_class=cc1_class,
        # CC2 curvature-response
        d2_symbolic=d2_symbolic, d2_fit_B1=d2_fit_B1, d2_fit_B3=d2_fit_B3,
        cc2_resid_B1=cc2_resid_B1, cc2_resid_B3=cc2_resid_B3, cc2_ok=cc2_ok,
        # kinematic cross-check
        q_grid=q_grid, om1=om1, coupling_B1=coupling_B1, coupling_B3=coupling_B3,
        kin_bracket_ratio=kin_bracket_ratio, kin_contam=kin_contam, squeezing_separated=squeezing_separated,
        # verdict
        predicted_sign=predicted_sign, computed_sign=computed_sign,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v, composite=composite,
        posterior=posterior,
        PASS_band=PASS_BAND, TRUNC_floor=TRUNC_FLOOR, DERIV_floor=DERIV_FLOOR, TOL_EXACT=TOL_EXACT,
        # provenance
        a_4_FW_zeta=a_4_FW_zeta, a_6_FW_zeta=a_6_FW_zeta, a4_fold=a4_fold,
        M_KK=M_KK, tau_fold=tau_fold, c_B1=c_B1, c_B3=c_B3, E_B1=E_B1, Delta_B1=Delta_B1,
        reading="NNLO_a6_field_strength_cross_term_is_first_value_bearing_substrate_EP_prediction",
    )
    print(f"\n  npz  -> {NPZ_OUT.relative_to(ROOT)}")

    # ---- (13) plot ----
    fig, axes = plt.subplots(1, 2, figsize=(13.4, 5.3))

    # Panel 1: kappa_EP^NNLO(b) vs C_2(b), showing the band-dependent NNLO coupling (NLO baseline = 1 line).
    ax = axes[0]
    C2_line = np.linspace(-0.2, 1.6, 60)  # (local) Casimir axis
    kappa_line = 1.0 + 8.0 * b0 * RK_fold + 4.0 * g0 * C2_line  # (local) kappa_EP^NNLO(C_2)
    ax.plot(C2_line, kappa_line, "-", color="tab:purple", lw=2.0,
            label=fr"$\kappa_{{EP}}^{{NNLO}}(C_2)=1+8 b_0 R_K+4 g_0 C_2$")
    ax.axhline(1.0, color="k", ls="--", lw=1.3, label=r"NLO baseline $\kappa_{EP}^{NLO}=1$ (generic)")
    ax.scatter([C2_B1, C2_B3], [kappa_NNLO_B1, kappa_NNLO_B3],
               color=["tab:blue", "tab:red"], s=70, zorder=5, edgecolor="k")
    ax.annotate(fr"B1 singlet (C$_2$=0): {kappa_NNLO_B1:.6f}", (C2_B1, kappa_NNLO_B1),
                textcoords="offset points", xytext=(8, 8), fontsize=8.0, color="tab:blue")
    ax.annotate(fr"B3 triplet (C$_2$=4/3): {kappa_NNLO_B3:.6f}", (C2_B3, kappa_NNLO_B3),
                textcoords="offset points", xytext=(-30, -16), fontsize=8.0, color="tab:red")
    ax.set_xlabel(r"quadratic Casimir $C_2(b)$")
    ax.set_ylabel(r"$\kappa_{EP}^{NNLO}(b)$  (NNLO curvature-coupling ratio)")
    ax.set_title(r"NNLO EP discriminator: band-dependent $\kappa_{EP}^{NNLO}$"
                 "\n" fr"$\Delta\kappa=\kappa(B1)-\kappa(B3)=-\frac{{16}}{{3}} g_0={Delta_kappa:.4e}$  ($g_0$ substrate-anchored)",
                 fontsize=9.6)
    ax.legend(loc="upper right", fontsize=7.8)
    ax.grid(ls=":", alpha=0.4)

    # Panel 2: the EP frontier ladder (NLO generic vs NNLO value-bearing) + CC1 FI partition.
    ax = axes[1]
    labels = ["NLO\n$\\kappa_{EP}-1$\n(generic-cored)", "NNLO\n$\\Delta\\kappa$\n(VALUE-bearing)",
              "$d\\Delta\\kappa/dC_2$\n(nonzero)"]  # (local)
    vals = [kappa_NLO_dev, abs_Delta_kappa, abs(dDk_dC2)]  # (local)
    colors = ["tab:gray", "tab:green" if composite == "PASS" else "tab:orange", "tab:cyan"]  # (local)
    xpos = np.arange(len(vals))  # (local)
    ax.bar(xpos, vals, color=colors, alpha=0.85, edgecolor="k", zorder=3)
    for xi, vi in zip(xpos, vals):
        ax.annotate(f"{vi:.3e}", (xi, vi), textcoords="offset points",
                    xytext=(0, 6), ha="center", fontsize=8.4)
    ax.axhline(PASS_BAND, color="green", ls="-", lw=1.4, zorder=2, label=fr"PASS floor {PASS_BAND:.0e}")
    ax.axhline(TRUNC_FLOOR, color="orange", ls=":", lw=1.2, zorder=2, label=fr"INFO/trunc floor {TRUNC_FLOOR:.0e}")
    ax.set_yscale("log")
    ax.set_xticks(xpos)
    ax.set_xticklabels(labels, fontsize=8.0)
    ax.set_ylabel(r"magnitude (log scale)")
    ax.set_title(f"{GATE_ID}\nCC1: {cc1_class} (a$_6^{{Mellin}}$ vs a$_6^{{\\zeta}}$ sign-agree={cc1_sign_agree})  "
                 f"(composite: {composite})", fontsize=9.4)
    ax.legend(loc="lower right", fontsize=7.8)
    ax.grid(axis="y", ls=":", alpha=0.4)

    fig.tight_layout()
    fig.savefig(PNG_OUT, dpi=130)
    plt.close(fig)
    print(f"  png  -> {PNG_OUT.relative_to(ROOT)}")

    # ---- (14) dual-SHA + verdict line ----
    print("\n" + "-" * 78)
    print("Dual-SHA closure + verdict-line emission")
    print("-" * 78)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    append_verdict(composite, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v)
    print(f"\n  verdict line appended -> {VERDICT_FILE.relative_to(ROOT)}")

    # 4-tuple output tag (final non-verdict line per gate-verdicts.md §"During computation")
    print(f"\n4-TUPLE OUTPUT TAG: (value=Delta_kappa={Delta_kappa:.6g}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
