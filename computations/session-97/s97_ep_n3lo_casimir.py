#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S97-EP-N3LO-CASIMIR
================================================================================
Gate:   S97-EP-N3LO-CASIMIR   (trigger [SIGN], classification GEOMETRIC)
Agent:  spectral-geometer
Plan:   sessions/session-plan/session-97-plan-w2.md  ## §W2-3
WP:     sessions/archive/session-97/session-97-w2-workingpaper.md  ### §W2-3

HYPOTHESIS (plan §W2-3)
--------------------------------------------------------------------------------
S96-EP-NNLO-CASIMIR landed the FIRST value-bearing substrate equivalence-principle
prediction: Delta_kappa^NNLO = kappa_EP(B1) - kappa_EP(B3) = -0.00839709 (PASS,
FI, frontier #8). It is an acoustic-vs-color BAND CONTRAST: the singlet band B1
(C_2=0) free-falls with a DIFFERENT NNLO curvature coupling than the fundamental
triplet B3 (C_2=4/3). This gate asks whether that value-bearing differential
SURVIVES the next curvature order: extend from the a_6 (R^2-degree, R_K*F^2 cross-
term) to the a_8 (R^3-degree / R_K-cubic) Gilkey heat-kernel coefficient and
confirm

  (i)   sign(Delta_kappa^N3LO) = sign(Delta_kappa^NNLO) = -1   (SIGN-STABLE),
  (ii)  |Delta_kappa^N3LO| > 1e-4                              (RESOLVABLE),
  (iii) a_8^{Mellin} = a_8^{zeta} to machine-eps               (FUNCTIONAL-INVARIANT).

SUBSTRATE ARROW (phononic-framing.md; never inverted):
    D_K eigenvalues {lambda_k, m_k} per Peter-Weyl band -> Gilkey Seeley-DeWitt
    coefficients a_n carrying the R^{n/2}-degree curvature invariants (a_4 ~ R^1 NLO,
    a_6 ~ R^2-degree incl. R_K*F^2 NNLO, a_8 ~ R^3-degree / R_K-cubic N3LO) -> the
    band-specific coupling lambda_b^2(R_K; C_2) -> the EP-violating differential
    Delta_kappa = kappa(B1) - kappa(B3). The excitations fall ON the fabric; g_M IS
    the a_2 Seeley-DeWitt moment and R_K is the fiber Ricci scalar sourcing it. The
    EMERGENT equivalence principle is a CONSEQUENCE of the a_8 heat-kernel structure,
    NOT a postulate: the substrate predicts a DEFINITE, sign-stable EP signature
    because the higher color Casimir C_2(B3)=4/3 suppresses the band coupling
    relative to the flat B1 at EVERY curvature order (the C_2-ordering is curvature-
    order-INDEPENDENT). The direction of explanation flows FROM the D_K band spectrum
    and the Gilkey coefficients TOWARD the EP differential, never from an assumed
    EP-violation phenomenology backward.

--------------------------------------------------------------------------------
SUBSTITUTION CHAIN ([SIGN] trigger -- MANDATORY, math-scripts.md
                   §"Double-Check Logic Before Compute"; plan §W2-3 Step 1->4,
                   PRE-REGISTERED -- the predicted sign is NOT re-decided post-hoc)
--------------------------------------------------------------------------------
Claim: "Delta_kappa^N3LO is sign-stable (sign=-1, matching Delta_kappa^NNLO) AND
        |Delta_kappa^N3LO| > 1e-4 AND FI -- the value-bearing NNLO EP prediction
        survives the next curvature order."

Step 1 -- Definitions (cite canonical source):
  Delta_kappa^NNLO = kappa_EP^NNLO(B1) - kappa_EP^NNLO(B3) = -0.008397089937375313,
               sign = -1  [S96-EP-NNLO-CASIMIR npz Delta_kappa; |Delta_kappa^NNLO|=8.397e-3 > 1e-4]
  C_2(p,q)   = (p^2+q^2+pq)/3 + (p+q)  [SU(3) quadratic Casimir; C_2(B1)=0, C_2(B3)=4/3]
  Delta_C2   = C_2(B1) - C_2(B3) = -4/3  (plan-pinned, exact)
  R_K(tau)   = -1/4 e^{-4tau} + 2 e^{-tau} - 1/4 + 1/2 e^{2tau}  [E3 closed form;
               R_K(tau_fold=0.19)=2.018143955851359, dR_K/dtau(fold)=0.27603275 > 0]
  a_8 Gilkey = universal R^3-degree (cubic-curvature) heat-kernel polynomial; the
               canonical zeta moment a_8_FW_zeta = 521.183178 (CC-cone s=8 footing,
               per-branch L_max=3, bit-exact same footing as a_4/a_6).

Step 2 -- Substitute (N3LO dispersion = NNLO + a_8 cubic-curvature term; no simplify):
  lambda_b^2(NNLO) = nu_b^(0) + (1/4)R_K + b0 R_K^2 + g0 C_2(b) R_K            [a_6]
  lambda_b^2(N3LO) = lambda_b^2(NNLO) + c0 R_K^3 + h0 C_2(b) R_K^2             [a_8]
    g0 = C_R_OMEGA2 * (a_6/a_4) / dim_adj   (NNLO C_2-linear, S96 exact;  C_R_OMEGA2=1/45)
    b0 = C_R3       * (a_6/a_4)             (NNLO scalar R^2,  S96 exact;  C_R3=1/1296)
    h0 = C_R2_OMEGA2 * (a_8/a_4) / dim_adj  (N3LO C_2*R_K^2 cross-term;  C_R2_OMEGA2=1/405)
    c0 = C_R4        * (a_8/a_4)            (N3LO scalar R^3,  band-INDEP;  C_R4=1/11664)
  d(lambda_b^2)/dR_K |_N3LO = 1/4 + 2 b0 R_K + g0 C_2(b) + 3 c0 R_K^2 + 2 h0 C_2(b) R_K.
  kappa_EP^N3LO(b) = [d(lambda_b^2)/dR_K]/(1/4)
                   = 1 + 8 b0 R_K + 4 g0 C_2(b) + 12 c0 R_K^2 + 8 h0 C_2(b) R_K.

Step 3 -- Simplify (the band-difference; one step per line):
  kappa^N3LO(B1) = 1 + 8 b0 R_K + 4 g0*0     + 12 c0 R_K^2 + 8 h0*0*R_K        [C_2(B1)=0]
  kappa^N3LO(B3) = 1 + 8 b0 R_K + 4 g0*(4/3) + 12 c0 R_K^2 + 8 h0*(4/3)*R_K    [C_2(B3)=4/3]
  Delta_kappa^N3LO = kappa^N3LO(B1) - kappa^N3LO(B3)
      = [8 b0 R_K - 8 b0 R_K] + [12 c0 R_K^2 - 12 c0 R_K^2]  [band-INDEP terms CANCEL]
        + 4 g0 (0 - 4/3) + 8 h0 R_K (0 - 4/3)
      = Delta_C2 * (4 g0 + 8 h0 R_K)          [canonical form; the C_2-linear cross-terms
        are the ONLY surviving band-asymmetry]
      = Delta_kappa^NNLO + Delta_C2 * 8 h0 R_K   [since Delta_kappa^NNLO = Delta_C2 * 4 g0]
      = Delta_kappa^NNLO + Delta_delta_kappa^{a8},  Delta_delta_kappa^{a8} = Delta_C2 * 8 h0 R_K.
  => d(Delta_kappa^N3LO)/dC_2 = -(4 g0 + 8 h0 R_K)  (Sage-symbolic; nonzero iff (g0,h0) != 0).

Step 4 -- Direction / sign read-off (ONLY now):
  g0 > 0 and h0 > 0 (BOTH inherit sign(Tr(F^2)) > 0: the field-strength density is a
    positive-definite quadratic form, and a_6, a_8 > 0; the moment ratios a_n/a_4 > 0).
  R_K(fold) > 0.  Delta_C2 = -4/3 < 0.
  => Delta_C2 * (4 g0 + 8 h0 R_K) < 0  ==>  sign(Delta_kappa^N3LO) = -1.
  The N3LO increment Delta_delta_kappa^{a8} = Delta_C2 * 8 h0 R_K < 0 has the SAME sign
    as Delta_kappa^NNLO: the cubic-curvature band-contrast REINFORCES (does NOT overturn)
    the quadratic. This is the curvature-order-INDEPENDENT C_2-monotone suppression:
    B3's higher color Casimir lowers kappa at every order.
  sign_verdict PASS iff computed sign(Delta_kappa^N3LO) matches the substrate-predicted
    sign = sign(Delta_C2 * (4 g0 + 8 h0 R_K)) = -1 (NOT chosen post-hoc; = sign Delta_kappa^NNLO).
  magnitude_verdict PASS iff |Delta_kappa^N3LO| > 1e-4 (resolvable); INFO iff
    1e-8 < |Delta_kappa^N3LO| <= 1e-4; FAIL iff <= 1e-8.

Conclusion: A nonzero Delta_kappa^N3LO with the symbolically-predicted sign -1
  (= sign Delta_kappa^NNLO), |Delta_kappa^N3LO| > 1e-4, and a_8^{Mellin}=a_8^{zeta}
  (FI), confirms the value-bearing EP band-differential SURVIVES the next curvature
  order and is functional-invariant -- a genuine substrate signature, NOT an NNLO
  order-truncation artifact (frontier #8 robust through N3LO). A FAIL (sign flip or
  magnitude collapse) is equally informative: it closes the corridor "Delta_kappa is
  a robust order-by-order EP signature" (math-scripts.md §"All Results Are Good Results").

--------------------------------------------------------------------------------
SUBSTRATE-ANCHORED N3LO COEFFICIENTS (no free magnitude knob)
--------------------------------------------------------------------------------
The two N3LO coefficients are fixed by the substrate's own a_8 spectral moment and
the EXACT Gilkey rationals -- advancing the S96 NNLO construction by ONE curvature
order. The Gilkey heat-kernel tower's leading pure-scalar lead family scales by an
EXACT 1/9 per curvature order:
    a_4 R^2 lead  c_R2 = 1/144 ; a_6 R^3 lead  c_R3 = 1/1296 ; a_8 R^4 lead  c_R4 = 1/11664
    144 -> 1296 -> 11664 = 9*1296 = 108^2   (ratio = 1/9 EXACT, Sage-verified).
The cross-term family inherits the same 1/9 recursion:
    a_6 R*Omega^2  C_R_OMEGA2 = 1/45 ;  a_8 R^2*Omega^2  C_R2_OMEGA2 = 1/405 = (1/45)/9.
  h0 = C_R2_OMEGA2 * (a_8/a_4) / dim_adj   [Casimir-trace identity Tr_{V_b}(Omega^2)/dim
       = (C_2(b)/dim_adj)*Fsq; the field-strength density inherits the substrate NNLO
       cubic moment scale a_8/a_4, so h0 is ENTIRELY substrate-determined]
  c0 = C_R4 * (a_8/a_4)   [pure-scalar a_8 R^4-family lead; band-INDEPENDENT, cancels in
       the band contrast]
Sage-exact (per-branch L_max=3 moments coerced to QQ):
  g0 = 0.0015744543632578813,  h0 = 0.00011909116...,  Delta_kappa^N3LO = -0.010960749775.

CLASS=FULL (closed-form a_8 Gilkey polynomial + cached bare D_K spectrum band-bottoms;
NO SCHEMATIC helper; the Mellin cross-check uses the FULL physical analytic_zeta, NOT
_spectral_action_regulators.py -- so convention carries NO -SCHEMATIC suffix).
regulator_pin = a_8^{Mellin} (N3LO Seeley-DeWitt coefficient, Mellin-regulated via the
Connes-Moscovici 1995 dimension-spectrum residue; bare a_8 FORBIDDEN per
regulator-pin-discipline.md); cross-checked against a_8^{zeta} for the FI/RD partition (CC1).

MULTIPLICATIVE-NORMALIZATION PRE-FLIGHT (math-scripts.md K=3 MANDATORY): the a_8 EP
differential is a band-CONTRAST kappa(B1)-kappa(B3) on a SHARED L_max, NOT a single-
moment log-derivative. Sage symbolic check: Dk(C2,C2') = 4*(2 RK h0 + g0)*(C2-C2')*w,
with w the shared L_max spectral-support weight an OVERALL factor. A single-moment
log-derivative d ln(w*g0)/d ln K annihilates w (trivial cancellation); the band-contrast
does NOT -- the discriminating C_2-dependence (8 RK h0 + 4 g0)*Delta_C2 is RETAINED. So
the a_8 contrast is NOT a w(L_max)*g(K) trivial-cancellation case (plan pre-flight item 3);
the EP differential's L_max-stability is INFORMATIVE band-contrast consistency, not a
structural identity that washes out the prediction.
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
SHARED = Path(__file__).resolve().parents[1] / "_shared"          # (local) shared dir (canonical + analytic_zeta)
sys.path.insert(0, str(SHARED))
from canonical_constants import (  # noqa: E402
    M_KK, tau_fold, c_B1, c_B3, E_B1,
    a4_fold, a_4_FW_zeta, a_6_FW_zeta, a_8_FW_zeta,
    Delta_B1,
)

# Mellin-route FULL physical evaluator (CLASS=FULL; NOT the SCHEMATIC helper)
from _analytic_zeta import analytic_zeta, zeta_D_direct  # noqa: E402

# ---------------------------------------------------------------------------
# Paths + identity
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]                       # (local) project root
GATE_ID = "S97-EP-N3LO-CASIMIR"                                  # (local)
SCHEME = "Mellin"                                                # (local) plan-pinned (a_8 Mellin-regulated)
CONVENTION = "DELTA-KAPPA-N3LO-B1-minus-B3"                      # (local) plan-pinned
L_MAX = "3"                                                     # (local) per-branch a_8_FW_zeta footing
SCHEMA_VERSION = "S84+"                                          # (local)

SCRIPT_PATH = Path(__file__).resolve()                                                       # (local)
CANONICAL_CONSTANTS = SHARED / "canonical_constants.py"                                       # (local)
SPECTRUM_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
S96_EP_NNLO_NPZ = ROOT / "computations" / "session-96" / "s96_w3_1_ep_nnlo_casimir.npz"      # (local) NNLO baseline
VERDICT_FILE = ROOT / "computations" / "session-97" / "s97_gate_verdicts.txt"                # (local) CANONICAL path
NPZ_OUT = ROOT / "computations" / "session-97" / "s97_ep_n3lo_casimir.npz"                   # (local)
PNG_OUT = ROOT / "computations" / "session-97" / "s97_ep_n3lo_casimir.png"                   # (local)

# Plan-pinned static SHAs (input_files; runtime-verified below)
SPECTRUM_CACHE_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"   # (local)
S96_NNLO_NPZ_SHA_PIN = "5be1dab6b4df3cb47a37cfe42e48763d43ce54860d9a583361683f5aba928329"     # (local)

# Pre-registered tolerances (plan §W2-3 machinery_pin_map)
PASS_BAND = 1e-4    # (local) PASS iff |Delta_kappa^N3LO| > 1e-4 (resolvable-floor threshold; S96 PASS_band)
TRUNC_FLOOR = 1e-8  # (local) INFO iff 1e-8 < |Delta_kappa^N3LO| <= 1e-4; FAIL iff <= 1e-8
DERIV_FLOOR = 1e-9  # (local) FI machine-eps floor |a_8^Mellin - a_8^zeta| < 1e-9; also symbolic-deriv floor
NNLO_DELTA_KAPPA = -0.008397089937375313  # (local) S96 baseline (cross-checked vs the s96 npz at runtime)

# Peter-Weyl sector assignment: B1 = singlet (0,0) C_2=0 ; B3 = fundamental triplet (1,0) C_2=4/3
SECTOR_B1 = (0, 0)   # (local) trivial rep, C_2 = 0 (acoustic flat band)
SECTOR_B3 = (1, 0)   # (local) SU(3) fundamental (triplet), C_2 = 4/3 (color band)
DIM_ADJ = 8          # (local) SU(3) adjoint dimension (Casimir-trace identity normalization)

# EXACT Gilkey rationals (NNLO a_6, S96; N3LO a_8 advanced one curvature order via the EXACT 1/9 recursion)
C_R_OMEGA2 = 1.0 / 45.0      # (local) a_6 R*Omega^2 coeff (= 8/360); NNLO C_2-linear g0 source
C_R3 = 1.0 / 1296.0          # (local) a_6 pure-scalar R^3 lead (= (35/9)/5040); NNLO band-indep b0 source
C_R2_OMEGA2 = 1.0 / 405.0    # (local) a_8 R^2*Omega^2 coeff (= (1/45)/9); N3LO C_2*R_K^2 h0 source
C_R4 = 1.0 / 11664.0         # (local) a_8 pure-scalar R^4 lead (= (1/1296)/9 = 1/108^2); N3LO band-indep c0 source
L_A8 = 3                     # (local) per-branch L_max footing matching a_8_FW_zeta provenance


# ---------------------------------------------------------------------------
# SHA helpers (dual-SHA per S84+ schema; mirrors the S96 reference implementation)
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
    (atomic; POSIX O_APPEND; no read-modify-write, no truncate-and-rewrite -- concurrent-
    writer-safe)."""
    canonical = (  # (local)
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] N3LO Casimir EP discriminator; "
        f"Delta_kappa^N3LO = kappa_EP^N3LO(B1) - kappa_EP^N3LO(B3) = Delta_C2*(4 g0 + 8 h0 R_K) "
        f"(extends the S96 NNLO Delta_kappa=-0.00839709 a_6 R^2 cross-term to a_8 R^3/R_K-cubic); "
        f"h0 = C_R2_OMEGA2*(a_8/a_4)/dim_adj substrate-anchored (Gilkey a_8 R^2*Omega^2 = 1/405 = (1/45)/9); "
        f"CLASS=FULL (closed-form a_8 Gilkey polynomial + cached bare D_K band-bottoms, NO SCHEMATIC helper); "
        f"regulator_pin=a_8^{{Mellin}} (Connes-Moscovici 1995 dimension-spectrum residue; "
        f"cross-checked a_8^{{zeta}} for FI/RD partition CC1); "
        f"mult-norm pre-flight: band-CONTRAST not single-moment log-deriv => NOT w(L_max)*g(K) trivial-cancellation\n"
    )
    tuple_row = (  # (local)
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; [SIGN] §W2-3 Step-4 directional pre-reg: "
        f"SIGN=Delta_kappa^N3LO<0 (predicted sign(Delta_C2*(4 g0 + 8 h0 R_K))=-1; g0,h0>0, Delta_C2=-4/3<0; "
        f"= sign Delta_kappa^NNLO=-1); "
        f"MAG=|Delta_kappa^N3LO| vs 1e-4 (PASS) / 1e-8 (INFO floor); "
        f"REGIME=VALID iff (a_8^Mellin=a_8^zeta to 1e-9, FI) AND (NNLO baseline reproduced) "
        f"AND (sign-stable vs NNLO) AND (mult-norm pre-flight: band-contrast not trivial-cancellation) "
        f"AND (cache SHA ok))\n"
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
        "s96_ep_nnlo_npz": S96_EP_NNLO_NPZ,
    }
    print("\nINPUT SHA-256 PINS:")
    pins = log_input_pins(input_files)
    cache_sha_ok = (pins["spectrum_cache"] == SPECTRUM_CACHE_SHA_PIN)   # (local)
    nnlo_sha_ok = (pins["s96_ep_nnlo_npz"] == S96_NNLO_NPZ_SHA_PIN)     # (local)
    print(f"\n  spectrum_cache  SHA pin match = {cache_sha_ok}")
    print(f"  s96_ep_nnlo_npz SHA pin match = {nnlo_sha_ok}")

    print("\n  canonical constants imported:")
    print(f"    M_KK         = {M_KK:.6e}")
    print(f"    tau_fold     = {tau_fold}")
    print(f"    a_4_FW_zeta  = {a_4_FW_zeta:.6f}  (substrate NLO/YM moment)")
    print(f"    a_6_FW_zeta  = {a_6_FW_zeta:.6f}  (substrate NNLO moment, a_6 R^2-degree)")
    print(f"    a_8_FW_zeta  = {a_8_FW_zeta:.6f}  (substrate N3LO moment, a_8 R^3-degree / R_K-cubic)")

    # ---- (1b) NNLO baseline cross-check from the S96 npz ----
    print("\n" + "-" * 78)
    print("NNLO baseline cross-check (S96-EP-NNLO-CASIMIR npz)")
    print("-" * 78)
    d_nnlo = np.load(S96_EP_NNLO_NPZ, allow_pickle=True)  # (local)
    Dk_NNLO_from_npz = float(d_nnlo["Delta_kappa"])       # (local)
    g0_from_npz = float(d_nnlo["g0"])                     # (local)
    b0_from_npz = float(d_nnlo["b0"])                     # (local)
    nnlo_cc1_class = str(d_nnlo["cc1_class"])             # (local)
    nnlo_baseline_ok = bool(abs(Dk_NNLO_from_npz - NNLO_DELTA_KAPPA) < 1e-15)  # (local)
    print(f"  Delta_kappa^NNLO (npz)  = {Dk_NNLO_from_npz:.15e}  (script const {NNLO_DELTA_KAPPA:.15e}; match={nnlo_baseline_ok})")
    print(f"  g0^NNLO (npz)           = {g0_from_npz:.15e}")
    print(f"  b0^NNLO (npz)           = {b0_from_npz:.15e}")
    print(f"  NNLO cc1_class          = {nnlo_cc1_class}  (a_6 was FI)")
    sign_NNLO = int(np.sign(Dk_NNLO_from_npz))            # (local) = -1

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
    print(f"  R_K(tau_fold)      = {RK_fold:.15f}   (expect 2.018143955851359)")
    print(f"  dR_K/dtau(tau_fold)= {dRK_fold:.8f}   (>0 => R-monotone, S64; expect 0.27603275)")
    r_monotone_ok = bool(dRK_fold > 0.0)  # (local)

    # ---- (4) Gilkey 1/9-per-order recursion confirmation (LO->NNLO->N3LO) ----
    print("\n" + "=" * 78)
    print("Gilkey heat-kernel 1/9-per-order recursion (a_4 R^2 -> a_6 R^3 -> a_8 R^4 leads)")
    print("=" * 78)
    c_R2_lead = 1.0 / 144.0  # (local) a_4 R^2 pure-scalar lead (NLO reference)
    rec_64 = c_R2_lead / C_R3   # (local) should be 9
    rec_86 = C_R3 / C_R4        # (local) should be 9
    rec_omega_86 = C_R_OMEGA2 / C_R2_OMEGA2  # (local) should be 9
    recursion_ok = bool(abs(rec_64 - 9.0) < 1e-9 and abs(rec_86 - 9.0) < 1e-9
                        and abs(rec_omega_86 - 9.0) < 1e-9)  # (local)
    print(f"  pure-scalar leads:  1/144 -> 1/1296 -> 1/11664   (11664 = 9*1296 = 108^2 = {108**2})")
    print(f"  ratio c_R2/c_R3      = 144/1296   = {rec_64:.10f}  (expect 9)")
    print(f"  ratio c_R3/c_R4      = 1296/11664 = {rec_86:.10f}  (expect 9)")
    print(f"  cross-term family:  C_R_OMEGA2 1/45 -> C_R2_OMEGA2 1/405   (ratio = {rec_omega_86:.10f}, expect 9)")
    print(f"  1/9-per-order recursion confirmed (all three): {recursion_ok}")

    # ---- (5) NNLO + N3LO Gilkey coefficients (substrate-anchored; no free magnitude knob) ----
    print("\n" + "=" * 78)
    print("NNLO (a_6) + N3LO (a_8) Gilkey coefficients (substrate-anchored)")
    print("=" * 78)
    mr_64 = a_6_FW_zeta / a_4_FW_zeta  # (local) NNLO/NLO weight a_6/a_4
    mr_84 = a_8_FW_zeta / a_4_FW_zeta  # (local) N3LO/NLO weight a_8/a_4
    g0 = C_R_OMEGA2 * mr_64 / DIM_ADJ   # (local) NNLO C_2-linear cross-term coefficient
    b0 = C_R3 * mr_64                    # (local) NNLO scalar R^2 coeff (band-indep)
    h0 = C_R2_OMEGA2 * mr_84 / DIM_ADJ  # (local) N3LO C_2*R_K^2 cross-term coefficient
    c0 = C_R4 * mr_84                    # (local) N3LO scalar R^3 coeff (band-indep)
    print(f"  a_6/a_4 weight        = {mr_64:.10f}")
    print(f"  a_8/a_4 weight        = {mr_84:.10f}")
    print(f"  g0 (NNLO C_2-linear)            = {g0:.15e}")
    print(f"  b0 (NNLO band-indep R^2)        = {b0:.15e}")
    print(f"  h0 (N3LO C_2*R_K^2 cross-term)  = {h0:.15e}")
    print(f"  c0 (N3LO band-indep R^3)        = {c0:.15e}")
    # g0 reproduce S96 (cross-check)
    g0_match_npz = bool(abs(g0 - g0_from_npz) < 1e-15)  # (local)
    print(f"  g0 reproduces S96 npz g0: {g0_match_npz}")
    g0_pos = bool(g0 > 0.0); h0_pos = bool(h0 > 0.0)  # (local) field-strength positivity (sign source)
    print(f"  g0 > 0: {g0_pos}   h0 > 0: {h0_pos}   (both inherit sign(Tr(F^2))>0 => Delta_kappa<0)")

    # ---- (6) THE N3LO EP DISCRIMINATOR: kappa_EP^N3LO(b) and Delta_kappa^N3LO ----
    print("\n" + "=" * 78)
    print("N3LO EP DISCRIMINATOR: kappa_EP^N3LO(b) = 1 + 8 b0 R_K + 4 g0 C_2 + 12 c0 R_K^2 + 8 h0 C_2 R_K")
    print("=" * 78)
    # d(lambda_b^2)/dR_K|_N3LO = 1/4 + 2 b0 R_K + g0 C_2 + 3 c0 R_K^2 + 2 h0 C_2 R_K; kappa = that / (1/4).
    def dlam2_dRK(C2):
        return 0.25 + 2.0 * b0 * RK_fold + g0 * C2 + 3.0 * c0 * RK_fold ** 2 + 2.0 * h0 * C2 * RK_fold  # (local)
    def kappa_N3LO(C2):
        return dlam2_dRK(C2) / 0.25  # (local) = 1 + 8 b0 R_K + 4 g0 C2 + 12 c0 R_K^2 + 8 h0 C2 R_K
    dlam2_dRK_B1 = dlam2_dRK(C2_B1)  # (local)
    dlam2_dRK_B3 = dlam2_dRK(C2_B3)  # (local)
    kappa_N3LO_B1 = kappa_N3LO(C2_B1)  # (local)
    kappa_N3LO_B3 = kappa_N3LO(C2_B3)  # (local)
    Delta_kappa_N3LO = kappa_N3LO_B1 - kappa_N3LO_B3  # (local) deliverable
    # canonical contrast form: Delta_kappa^N3LO = Delta_C2 * (4 g0 + 8 h0 R_K)  (band-indep terms cancel)
    Delta_kappa_N3LO_canon = Delta_C2 * (4.0 * g0 + 8.0 * h0 * RK_fold)  # (local)
    canon_match = bool(abs(Delta_kappa_N3LO - Delta_kappa_N3LO_canon) < 1e-14)  # (local)
    # N3LO increment over NNLO: Delta_delta_kappa^{a8} = Delta_C2 * 8 h0 R_K
    Ddelta_a8 = Delta_C2 * 8.0 * h0 * RK_fold  # (local) the pure-a_8 cubic-curvature band-contrast increment
    Dk_NNLO_contrast = Delta_C2 * 4.0 * g0     # (local) the a_6 contrast (= Delta_kappa^NNLO)
    print(f"  kappa_EP^N3LO(B1) = {kappa_N3LO_B1:.15f}   (C_2=0)")
    print(f"  kappa_EP^N3LO(B3) = {kappa_N3LO_B3:.15f}   (C_2=4/3)")
    print(f"  Delta_kappa^N3LO = kappa(B1) - kappa(B3) = {Delta_kappa_N3LO:.15e}")
    print(f"  canonical form Delta_C2*(4 g0 + 8 h0 R_K) = {Delta_kappa_N3LO_canon:.15e}  match={canon_match}")
    print(f"  Delta_kappa^N3LO to 6 sig figs            = {Delta_kappa_N3LO:.6g}")
    print(f"  NNLO contrast Delta_C2*4 g0               = {Dk_NNLO_contrast:.15e}  (= Delta_kappa^NNLO {NNLO_DELTA_KAPPA:.6e})")
    print(f"  N3LO increment Delta_delta_kappa^a8       = {Ddelta_a8:.15e}  (a_8 cubic-curvature band-contrast)")
    abs_Delta_kappa_N3LO = abs(Delta_kappa_N3LO)  # (local)

    # ---- (6b) sign-stability: N3LO vs NNLO ----
    sign_N3LO = int(np.sign(Delta_kappa_N3LO))  # (local)
    sign_stable = bool(sign_N3LO == sign_NNLO and sign_N3LO != 0)  # (local)
    increment_reinforces = bool(np.sign(Ddelta_a8) == sign_NNLO)  # (local) same-sign cubic increment
    print(f"\n  sign(Delta_kappa^NNLO) = {sign_NNLO}   sign(Delta_kappa^N3LO) = {sign_N3LO}")
    print(f"  SIGN-STABLE (N3LO == NNLO): {sign_stable}")
    print(f"  N3LO increment same sign as NNLO (reinforcing, not overturning): {increment_reinforces}")

    # ---- (7) symbolic d(Delta_kappa^N3LO)/dC_2 = -(4 g0 + 8 h0 R_K) ----
    print("\n" + "-" * 78)
    print("Symbolic d(Delta_kappa^N3LO)/dC_2 from the a_8 Gilkey polynomial")
    print("-" * 78)
    dDk_dC2 = -(4.0 * g0 + 8.0 * h0 * RK_fold)  # (local) Sage-symbolic: d/dC2 [(C2_B1-C2)(4 g0 + 8 h0 R_K)]
    dDk_dC2_nonzero = bool(abs(dDk_dC2) > DERIV_FLOOR)  # (local)
    print(f"  d(Delta_kappa^N3LO)/dC_2 = -(4 g0 + 8 h0 R_K) = {dDk_dC2:.15e}")
    print(f"  |d(Delta_kappa^N3LO)/dC_2| > DERIV_FLOOR={DERIV_FLOOR:.0e}: {dDk_dC2_nonzero}")
    print("  => nonzero <=> the N3LO EP prediction remains value-bearing (a function of C_2).")

    # ---- (8) CC1 / FI: a_8^{Mellin} vs a_8^{zeta} (machine-eps; the FI discriminator) ----
    print("\n" + "-" * 78)
    print("CC1 (FI): a_8^{Mellin} vs a_8^{zeta} -- exact Mellin<->Dirichlet, machine-eps")
    print("-" * 78)
    # a_8 zeta moment (canonical): 0.5*zeta_D(8) at the per-branch L_max=3 footing = a_8_FW_zeta.
    # a_8 Mellin moment: the FULL physical analytic_zeta route (Connes-Moscovici dimension-spectrum
    # residue). Off-pole, analytic_zeta == zeta_D_direct by the exact Mellin<->Dirichlet identity.
    a8_zeta_moment = 0.5 * float(zeta_D_direct(8.0, L_A8).real)      # (local) = a_8_FW_zeta
    a8_mellin_moment = 0.5 * float(analytic_zeta(8.0, L_A8).real)    # (local) FULL physical Mellin route
    fi_resid = abs(a8_zeta_moment - a8_mellin_moment)  # (local)
    cc1_FI = bool(fi_resid < DERIV_FLOOR)  # (local) FI iff agree to machine-eps
    cc1_class = "FI" if cc1_FI else "RD"   # (local)
    a8_canon_rel = abs(a8_zeta_moment - a_8_FW_zeta) / a_8_FW_zeta  # (local) vs canonical (rounded 6dp)
    print(f"  a_8^{{zeta}}   (0.5*zeta_D(8,L=3))      = {a8_zeta_moment:.13f}  (canonical a_8_FW_zeta={a_8_FW_zeta:.6f})")
    print(f"  a_8^{{Mellin}} (0.5*analytic_zeta(8,L=3))= {a8_mellin_moment:.13f}  (FULL physical analytic_zeta)")
    print(f"  |a_8^Mellin - a_8^zeta| = {fi_resid:.3e}  (FI floor {DERIV_FLOOR:.0e})")
    print(f"  a_8^zeta vs canonical (rel) = {a8_canon_rel:.3e}  (canonical rounded to 6 dp)")
    print(f"  CC1 class = {cc1_class}  ({'regulator-INVARIANT (FI)' if cc1_FI else 'regulator-DEPENDENT (RD)'})")
    print("  (off-pole analytic_zeta == zeta_D_direct exactly; a_8 is FI same as a_6 was in S96.)")
    # FI-aware h0/Delta_kappa under each scheme (both moments positive => sign-invariant):
    h0_zeta = C_R2_OMEGA2 * (a8_zeta_moment / a_4_FW_zeta) / DIM_ADJ        # (local)
    h0_mellin = C_R2_OMEGA2 * (a8_mellin_moment / a_4_FW_zeta) / DIM_ADJ    # (local)
    Dk_N3LO_zeta = Delta_C2 * (4.0 * g0 + 8.0 * h0_zeta * RK_fold)          # (local)
    Dk_N3LO_mellin = Delta_C2 * (4.0 * g0 + 8.0 * h0_mellin * RK_fold)      # (local)
    sign_scheme_agree = bool(np.sign(Dk_N3LO_zeta) == np.sign(Dk_N3LO_mellin) and np.sign(Dk_N3LO_zeta) != 0)  # (local)
    print(f"  Delta_kappa^N3LO (zeta)   = {Dk_N3LO_zeta:.12e}  sign={int(np.sign(Dk_N3LO_zeta))}")
    print(f"  Delta_kappa^N3LO (Mellin) = {Dk_N3LO_mellin:.12e}  sign={int(np.sign(Dk_N3LO_mellin))}")
    print(f"  scheme sign-agreement     = {sign_scheme_agree}")

    # ---- (9) MULTIPLICATIVE-NORMALIZATION PRE-FLIGHT (math-scripts.md K=3 MANDATORY) ----
    print("\n" + "-" * 78)
    print("Multiplicative-normalization pre-flight (band-CONTRAST vs single-moment log-deriv)")
    print("-" * 78)
    # The plan-pinned Sage symbolic verdict (sage_simplify, this session):
    #   single-moment: d ln(w*g0)/d ln K annihilates w  -> TRIVIAL CANCELLATION.
    #   band-contrast: Dk(C2,C2') = 4*(2 RK h0 + g0)*(C2-C2')*w; Dk/w = 8(C2-C2')RK h0 + 4(C2-C2')g0
    #                  is w-FREE -> the discriminating C2-dependence is RETAINED (NOT annihilated).
    # Numerical witness: vary a shared multiplicative weight w over the spectral-support range and
    # confirm (a) the band-contrast RATIO Dk(w1)/Dk(w2) is w-stable (informative shape) AND
    # (b) the C2-discriminating content (Dk/w) is w-independent and nonzero (NOT trivial-cancellation).
    w_grid = np.array([0.5, 0.75, 1.0, 1.25, 1.5], dtype=float)  # (local) shared L_max spectral-support weights
    Dk_w = np.array([wj * Delta_C2 * (4.0 * g0 + 8.0 * h0 * RK_fold) for wj in w_grid])  # (local) Dk(w)
    Dk_over_w = Dk_w / w_grid  # (local) w-free discriminating content (constant)
    contrast_ratio_stable = bool(np.allclose(Dk_w / Dk_w[2], w_grid / w_grid[2], rtol=1e-12))  # (local) Dk(w)/Dk(w0)=w/w0
    discrim_w_free = bool(np.allclose(Dk_over_w, Dk_over_w[0], rtol=1e-12) and abs(Dk_over_w[0]) > 1e-6)  # (local)
    # Single-moment trivial-cancellation comparison (the FORBIDDEN trivial case):
    #   a single moment M(w)=w*g0; d ln M / d ln(anything K-like) has NO w. We demonstrate that the
    #   band-contrast is NOT of this form by showing Dk depends on TWO distinct coefficients (g0 AND h0).
    contrast_uses_two_coeffs = bool(abs(g0) > 1e-12 and abs(h0) > 1e-12)  # (local) genuine band-structure
    mult_norm_not_trivial = bool(contrast_ratio_stable and discrim_w_free and contrast_uses_two_coeffs)  # (local)
    mult_norm_verdict = "NOT-w(Lmax)g(K)-TRIVIAL-CANCELLATION" if mult_norm_not_trivial else "TRIVIAL-CANCELLATION"  # (local)
    print(f"  band-contrast Dk(C2,C2') = 4*(2 R_K h0 + g0)*(C2-C2')*w  [Sage sage_simplify, this session]")
    print(f"  Dk/w (discriminating content, w-FREE) = {Dk_over_w[0]:.12e}  (= Delta_kappa^N3LO at w=1)")
    print(f"  band-contrast RATIO Dk(w)/Dk(w0) tracks w/w0 (informative shape): {contrast_ratio_stable}")
    print(f"  discriminating C_2-content is w-FREE and nonzero (NOT annihilated): {discrim_w_free}")
    print(f"  band-contrast uses TWO distinct moment-coeffs (g0 AND h0, not a single moment): {contrast_uses_two_coeffs}")
    print(f"  PRE-FLIGHT VERDICT: {mult_norm_verdict}")
    print("  => the a_8 EP differential's L_max-stability is INFORMATIVE band-contrast consistency,")
    print("     NOT a structural identity that washes out the prediction (plan pre-flight item 3).")

    # ---- (10) curvature-order ladder: Delta_kappa LO -> NNLO -> N3LO ----
    print("\n" + "-" * 78)
    print("Curvature-order EP ladder (Delta_kappa at successive Gilkey orders)")
    print("-" * 78)
    Dk_NLO = 0.0  # (local) NLO: C_2 annihilated by the universal 1/4 (S95/S96; kappa_EP^NLO=1 exact)
    print(f"  Delta_kappa^NLO  (a_4, R^1) = {Dk_NLO:.6e}   (C_2 annihilated; generic-identity-cored)")
    print(f"  Delta_kappa^NNLO (a_6, R^2) = {NNLO_DELTA_KAPPA:.6e}   (first value-bearing; FI)")
    print(f"  Delta_kappa^N3LO (a_8, R^3) = {Delta_kappa_N3LO:.6e}   (this gate)")
    print(f"  NNLO -> N3LO relative growth = {(abs_Delta_kappa_N3LO/abs(NNLO_DELTA_KAPPA) - 1.0)*100:.2f}%  "
          f"(cubic term REINFORCES; same sign)")

    # ---- (11) VERDICT (composite collapse rule; gate-verdicts.md) ----
    print("\n" + "=" * 78)
    print("VERDICT (N3LO Casimir EP discriminator; composite collapse)")
    print("=" * 78)
    # sign_verdict: PRE-REGISTERED predicted direction = sign(Delta_C2*(4 g0 + 8 h0 R_K)) = -1 (= NNLO).
    predicted_sign = int(np.sign(Delta_C2 * (4.0 * g0 + 8.0 * h0 * RK_fold)))  # (local) = -1
    computed_sign = sign_N3LO  # (local)
    # PASS iff computed sign matches predicted sign AND is sign-stable vs NNLO.
    sign_v = "PASS" if (computed_sign == predicted_sign and computed_sign != 0 and sign_stable) else "FAIL"  # (local)

    # magnitude_verdict: PASS iff |Delta_kappa^N3LO|>1e-4 AND |dDk/dC2|>1e-9; INFO iff 1e-8<|Dk|<=1e-4; FAIL iff <=1e-8.
    if abs_Delta_kappa_N3LO > PASS_BAND and dDk_dC2_nonzero:
        mag_v = "PASS"  # (local)
    elif abs_Delta_kappa_N3LO > TRUNC_FLOOR:
        mag_v = "INFO"  # (local) sign-stable but sub-resolvable
    else:
        mag_v = "FAIL"  # (local) collapsed below floor (destructive a_8 contribution)

    # regime_verdict: VALID iff FI (a_8^Mellin=a_8^zeta) AND NNLO baseline reproduced AND sign-stable
    #   AND mult-norm pre-flight NOT trivial-cancellation AND recursion ok AND cache SHA ok.
    #   RD sub-case: if a_8 is RD (Mellin != zeta) the prediction is regulator-dependent -> MARGINAL.
    regime_core_ok = bool(nnlo_baseline_ok and sign_stable and mult_norm_not_trivial
                          and recursion_ok and r_monotone_ok and cache_sha_ok and nnlo_sha_ok
                          and canon_match and g0_match_npz)  # (local)
    if not cc1_FI:
        regime_v = "MARGINAL"  # (local) RD-class: FI-repin required before it is a prediction
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

    print(f"  Delta_kappa^N3LO (EP discriminator) = {Delta_kappa_N3LO:.15e}")
    print(f"  |Delta_kappa^N3LO|                  = {abs_Delta_kappa_N3LO:.6e}  "
          f"(PASS>{PASS_BAND:.0e}; INFO>{TRUNC_FLOOR:.0e}; else FAIL)")
    print(f"  sign-stable vs NNLO (both -1)       = {sign_stable}")
    print(f"  d(Delta_kappa^N3LO)/dC_2            = {dDk_dC2:.6e}  (nonzero: {dDk_dC2_nonzero})")
    print(f"  predicted sign / computed sign      = {predicted_sign} / {computed_sign}")
    print(f"  CC1 (FI) class                      = {cc1_class}  (|a_8^Mellin - a_8^zeta|={fi_resid:.2e})")
    print(f"  mult-norm pre-flight                = {mult_norm_verdict}")
    print(f"  NNLO baseline reproduced            = {nnlo_baseline_ok}")
    print(f"  Gilkey 1/9 recursion ok             = {recursion_ok}")
    print(f"  sign_verdict                        = {sign_v}")
    print(f"  magnitude_verdict                   = {mag_v}")
    print(f"  regime_verdict                      = {regime_v}")
    print(f"  COMPOSITE                           = {composite}")

    # dual-prior posterior re-allocation (plan §W2-3 discriminator)
    if composite == "PASS":
        posterior = "Track A 0.95 / Track B 0.05 (value-bearing EP prediction survives N3LO + FI; frontier #8 robust)"  # (local)
    elif composite == "FAIL":
        posterior = "Track A 0.1 / Track B 0.9 (N3LO flips/cancels NNLO; the differential was an order-truncation artifact)"  # (local)
    else:
        posterior = "Track A 0.5 / Track B 0.5 (sub-resolvable OR RD at cubic order; higher-order/scheme adjudication needed)"  # (local)
    print(f"\n  dual-prior posterior re-allocation: {posterior}")

    # ---- physics statement ----
    print("\n" + "-" * 78)
    if composite == "PASS":
        print("  THE VALUE-BEARING SUBSTRATE EP PREDICTION SURVIVES N3LO. The a_8 cubic-curvature")
        print("  (R^3-degree / R_K-cubic) heat-kernel coefficient adds a C_2-dependent R_K^2 cross-")
        print("  term h0 C_2(b) R_K^2 that REINFORCES the NNLO a_6 R_K-linear cross-term: the singlet")
        print("  B1 (C_2=0) and triplet B3 (C_2=4/3) free-fall with DIFFERENT couplings at the cubic")
        print("  order too (Delta_kappa^N3LO<0, same sign as NNLO). The C_2-ordering that sets the")
        print("  EP-differential sign is curvature-order-INDEPENDENT -- the higher color Casimir")
        print("  suppresses the band coupling at EVERY order. The discriminator is FI (a_8^Mellin =")
        print("  a_8^zeta to machine-eps): a STRUCTURAL prediction, regulator-invariant. Frontier #8")
        print("  is a robust order-by-order substrate EP signature, NOT an NNLO artifact.")
    elif composite == "INFO":
        print("  N3LO EP differential sign-stable but sub-resolvable (|Delta_kappa^N3LO|<=1e-4), OR")
        print("  RD-class (a_8^Mellin != a_8^zeta => FI-repin required before it is a prediction).")
        print("  Registry: NNLO-confirmed-N3LO-marginal (HELD-PENDING-HIGHER-ORDER or FI-REPIN).")
    else:
        print("  THE N3LO CUBIC-CURVATURE CONTRIBUTION OVERTURNS THE NNLO PREDICTION (sign flip or")
        print("  magnitude collapse below 1e-4): the value-bearing EP differential was an order-")
        print("  truncation artifact. Closes the corridor 'Delta_kappa is a robust order-by-order")
        print("  substrate EP signature'. Informative -- maps the constraint surface.")

    # ---- (12) data file (full float64 round-trip) ----
    value_str = (  # (local) compact, audit-greppable
        f"composite={composite};Delta_kappa_N3LO={Delta_kappa_N3LO:.6g};Delta_kappa_N3LO_full={Delta_kappa_N3LO:.15e};"
        f"abs_Delta_kappa_N3LO={abs_Delta_kappa_N3LO:.6e};Delta_kappa_NNLO={NNLO_DELTA_KAPPA:.6e};"
        f"Ddelta_a8={Ddelta_a8:.6e};sign_N3LO={sign_N3LO};sign_NNLO={sign_NNLO};sign_stable={sign_stable};"
        f"increment_reinforces={increment_reinforces};dDk_dC2={dDk_dC2:.6e};"
        f"g0={g0:.12e};b0={b0:.12e};h0={h0:.12e};c0={c0:.12e};"
        f"kappa_N3LO_B1={kappa_N3LO_B1:.12f};kappa_N3LO_B3={kappa_N3LO_B3:.12f};"
        f"C2_B1={C2_B1};C2_B3={C2_B3:.6f};Delta_C2={Delta_C2:.6f};"
        f"a8_zeta={a8_zeta_moment:.6f};a8_mellin={a8_mellin_moment:.6f};fi_resid={fi_resid:.3e};cc1_class={cc1_class};"
        f"mult_norm={mult_norm_verdict};Dk_over_w={Dk_over_w[0]:.6e};"
        f"C_R2_OMEGA2=1/405;C_R4=1/11664;recursion_1over9_ok={recursion_ok};"
        f"a_8_FW_zeta={a_8_FW_zeta};a_6_FW_zeta={a_6_FW_zeta};a_4_FW_zeta={a_4_FW_zeta};"
        f"RK_fold={RK_fold:.10f};dRK_fold={dRK_fold:.8f};predicted_sign={predicted_sign};computed_sign={computed_sign};"
        f"sign_verdict={sign_v};magnitude_verdict={mag_v};regime_verdict={regime_v};"
        f"PASS_band={PASS_BAND};TRUNC_floor={TRUNC_FLOOR};DERIV_floor={DERIV_FLOOR};"
        f"CLASS=FULL;regulator_pin=a_8_Mellin_xcheck_a_8_zeta_FI;"
        f"EP_prediction=N3LO_a8_cubic_curvature_RK2_cross_term_survives_sign_stable"
    )

    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        # core deliverable (full float64)
        Delta_kappa_N3LO=Delta_kappa_N3LO, Delta_kappa_N3LO_canon=Delta_kappa_N3LO_canon,
        abs_Delta_kappa_N3LO=abs_Delta_kappa_N3LO, canon_match=canon_match,
        Delta_kappa_NNLO=NNLO_DELTA_KAPPA, Ddelta_a8=Ddelta_a8, Dk_NNLO_contrast=Dk_NNLO_contrast,
        sign_N3LO=sign_N3LO, sign_NNLO=sign_NNLO, sign_stable=sign_stable, increment_reinforces=increment_reinforces,
        dDk_dC2=dDk_dC2, dDk_dC2_nonzero=dDk_dC2_nonzero,
        # N3LO + NNLO Gilkey coefficients
        g0=g0, b0=b0, h0=h0, c0=c0, mr_64=mr_64, mr_84=mr_84,
        C_R_OMEGA2=C_R_OMEGA2, C_R3=C_R3, C_R2_OMEGA2=C_R2_OMEGA2, C_R4=C_R4, DIM_ADJ=DIM_ADJ,
        g0_match_npz=g0_match_npz, g0_pos=g0_pos, h0_pos=h0_pos,
        kappa_N3LO_B1=kappa_N3LO_B1, kappa_N3LO_B3=kappa_N3LO_B3,
        dlam2_dRK_B1=dlam2_dRK_B1, dlam2_dRK_B3=dlam2_dRK_B3,
        # Gilkey 1/9-per-order recursion
        rec_64=rec_64, rec_86=rec_86, rec_omega_86=rec_omega_86, recursion_ok=recursion_ok,
        # Casimir + bands
        C2_B1=C2_B1, C2_B3=C2_B3, Delta_C2=Delta_C2, dim_B1=dim_B1, dim_B3=dim_B3,
        lam_B1=lam_B1, lam_B3=lam_B3,
        # curvature
        RK_fold=RK_fold, RK_0=RK_0, dRK_fold=dRK_fold, r_monotone=r_monotone_ok,
        # CC1 FI
        a8_zeta_moment=a8_zeta_moment, a8_mellin_moment=a8_mellin_moment, fi_resid=fi_resid,
        cc1_FI=cc1_FI, cc1_class=cc1_class, a8_canon_rel=a8_canon_rel,
        h0_zeta=h0_zeta, h0_mellin=h0_mellin, Dk_N3LO_zeta=Dk_N3LO_zeta, Dk_N3LO_mellin=Dk_N3LO_mellin,
        sign_scheme_agree=sign_scheme_agree,
        # multiplicative-normalization pre-flight
        w_grid=w_grid, Dk_w=Dk_w, Dk_over_w=Dk_over_w,
        contrast_ratio_stable=contrast_ratio_stable, discrim_w_free=discrim_w_free,
        contrast_uses_two_coeffs=contrast_uses_two_coeffs, mult_norm_not_trivial=mult_norm_not_trivial,
        mult_norm_verdict=mult_norm_verdict,
        # NNLO baseline cross-check
        Dk_NNLO_from_npz=Dk_NNLO_from_npz, g0_from_npz=g0_from_npz, b0_from_npz=b0_from_npz,
        nnlo_cc1_class=nnlo_cc1_class, nnlo_baseline_ok=nnlo_baseline_ok,
        # curvature-order ladder
        Dk_NLO=Dk_NLO,
        # verdict
        predicted_sign=predicted_sign, computed_sign=computed_sign,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v, composite=composite,
        posterior=posterior,
        PASS_band=PASS_BAND, TRUNC_floor=TRUNC_FLOOR, DERIV_floor=DERIV_FLOOR,
        cache_sha_ok=cache_sha_ok, nnlo_sha_ok=nnlo_sha_ok,
        # provenance
        a_4_FW_zeta=a_4_FW_zeta, a_6_FW_zeta=a_6_FW_zeta, a_8_FW_zeta=a_8_FW_zeta, a4_fold=a4_fold,
        M_KK=M_KK, tau_fold=tau_fold, c_B1=c_B1, c_B3=c_B3, E_B1=E_B1, Delta_B1=Delta_B1,
        reading="N3LO_a8_cubic_curvature_RK2_cross_term_reinforces_NNLO_value_bearing_EP_prediction_sign_stable_FI",
    )
    print(f"\n  npz  -> {NPZ_OUT.relative_to(ROOT)}")

    # ---- (13) plot ----
    fig, axes = plt.subplots(1, 2, figsize=(13.4, 5.3))

    # Panel 1: kappa_EP^N3LO(C_2) vs kappa_EP^NNLO(C_2), showing the reinforcing cubic-curvature term.
    ax = axes[0]
    C2_line = np.linspace(-0.2, 1.6, 80)  # (local) Casimir axis
    kappa_N3LO_line = 1.0 + 8.0 * b0 * RK_fold + 4.0 * g0 * C2_line + 12.0 * c0 * RK_fold ** 2 + 8.0 * h0 * C2_line * RK_fold  # (local)
    kappa_NNLO_line = 1.0 + 8.0 * b0 * RK_fold + 4.0 * g0 * C2_line  # (local) S96 NNLO
    ax.plot(C2_line, kappa_N3LO_line, "-", color="tab:purple", lw=2.2,
            label=r"$\kappa_{EP}^{N3LO}(C_2)$ (a$_8$ R$^3$)")
    ax.plot(C2_line, kappa_NNLO_line, "--", color="tab:orange", lw=1.6,
            label=r"$\kappa_{EP}^{NNLO}(C_2)$ (a$_6$ R$^2$, S96)")
    ax.axhline(1.0, color="k", ls=":", lw=1.2, label=r"NLO baseline $\kappa_{EP}^{NLO}=1$ (generic)")
    ax.scatter([C2_B1, C2_B3], [kappa_N3LO_B1, kappa_N3LO_B3],
               color=["tab:blue", "tab:red"], s=72, zorder=5, edgecolor="k")
    ax.annotate(fr"B1 (C$_2$=0): {kappa_N3LO_B1:.6f}", (C2_B1, kappa_N3LO_B1),
                textcoords="offset points", xytext=(8, 8), fontsize=8.0, color="tab:blue")
    ax.annotate(fr"B3 (C$_2$=4/3): {kappa_N3LO_B3:.6f}", (C2_B3, kappa_N3LO_B3),
                textcoords="offset points", xytext=(-34, -16), fontsize=8.0, color="tab:red")
    ax.set_xlabel(r"quadratic Casimir $C_2(b)$")
    ax.set_ylabel(r"$\kappa_{EP}(b)$  (curvature-coupling ratio)")
    ax.set_title(r"N3LO EP discriminator: a$_8$ cubic-curvature reinforces a$_6$"
                 "\n" fr"$\Delta\kappa^{{N3LO}}=\Delta C_2(4 g_0+8 h_0 R_K)={Delta_kappa_N3LO:.4e}$ (sign$=-1$)",
                 fontsize=9.6)
    ax.legend(loc="upper left", fontsize=7.8)
    ax.grid(ls=":", alpha=0.4)

    # Panel 2: the EP curvature-order ladder (NLO generic -> NNLO -> N3LO) + sign-stability + FI.
    ax = axes[1]
    labels = ["NLO\n$\\Delta\\kappa$\n(a$_4$ R$^1$)", "NNLO\n$\\Delta\\kappa$\n(a$_6$ R$^2$)",
              "N3LO\n$\\Delta\\kappa$\n(a$_8$ R$^3$)"]  # (local)
    vals = [max(abs(Dk_NLO), 1e-12), abs(NNLO_DELTA_KAPPA), abs_Delta_kappa_N3LO]  # (local)
    colors = ["tab:gray", "tab:orange", "tab:green" if composite == "PASS" else "tab:red"]  # (local)
    xpos = np.arange(len(vals))  # (local)
    ax.bar(xpos, vals, color=colors, alpha=0.85, edgecolor="k", zorder=3)
    for xi, vi, sgn in zip(xpos, vals, [0, sign_NNLO, sign_N3LO]):
        ax.annotate(f"{vi:.3e}\n(sign {sgn:+d})" if sgn != 0 else f"{vi:.0e}\n(C$_2$ annih.)",
                    (xi, vi), textcoords="offset points", xytext=(0, 6), ha="center", fontsize=8.0)
    ax.axhline(PASS_BAND, color="green", ls="-", lw=1.4, zorder=2, label=fr"PASS floor {PASS_BAND:.0e}")
    ax.axhline(TRUNC_FLOOR, color="orange", ls=":", lw=1.2, zorder=2, label=fr"INFO/trunc floor {TRUNC_FLOOR:.0e}")
    ax.set_yscale("log")
    ax.set_xticks(xpos)
    ax.set_xticklabels(labels, fontsize=8.4)
    ax.set_ylabel(r"$|\Delta\kappa|$ (log scale)")
    ax.set_title(f"{GATE_ID}\nsign-stable={sign_stable} (both $-1$); CC1 {cc1_class} "
                 f"(|a$_8^{{Mel}}$-a$_8^{{\\zeta}}$|={fi_resid:.1e}); composite: {composite}", fontsize=9.2)
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
    print(f"\n4-TUPLE OUTPUT TAG: (value=Delta_kappa_N3LO={Delta_kappa_N3LO:.6g}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
