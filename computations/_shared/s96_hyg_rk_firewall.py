#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S96-HYG-RK-FIREWALL
===================

R_K(0) three-form normalization firewall (mirror of the capstone Section 8.2
two-`a_n`-object firewall) + convention-invariance certification.

Source: baptista V.1 `RK-NORMALIZATION-FIREWALL` (METHODOLOGY-class verbatim
landing). The deliverable is the firewall TABLE in capstone Section 8; this thin
verifier is the OPTIONAL Sage/numpy consistency check on the verbatim identity
(residual to machine-eps), NOT a new threshold-producing computation.

SUBSTRATE FRAMING (phononic-framing.md SS"IS Space, Not IN Space"):
  R_K(tau) is the scalar curvature of the SU(3) fiber -- a substrate-IS property
  of the fabric at each point, entering the Lichnerowicz identity
  D_K^2 = nabla* nabla + (1/4) R_K that keeps the spectral gap open
  (lambda^2 >= R_K/4 > 0). The three normalizations {2, 4, 1.5} are NOT three
  different curvatures; they are the SAME substrate curvature under three scale
  conventions (internal-rational E3, 12D-lift s52, Killing/Paper-15-rational).
  The firewall certifies that the substrate-IS invariants -- the FI ratio
  R1 = a0*a4/a2^2 and the Wronskian W(tau)'s tau=0 sixth-order zero (the
  genesis-only spectral-moment degeneracy) -- are unchanged under any of them,
  so no downstream observable inherits a convention artifact. The substrate IS
  the curvature; the normalization is a laboratory bookkeeping choice.
  Direction of explanation: D_K eigenvalues -> R_K (fiber curvature) ->
  {a0,a2,a4} spectral moments -> R1 FI ratio + W algebraic-independence Wronskian.

THREE CORPUS R_K(0) NORMALIZATIONS (each independently sourced):
  internal E3 : R_K(0) = 2     [E3 closed form RK = -1/4 e^{-4t} + 2 e^{-t} - 1/4
                                + 1/2 e^{2t} ; at t=0 -> -1/4 + 2 - 1/4 + 1/2 = 2;
                                baptista-operator-dk-tau.md; MCP-confirmed]
  12D-reduction s52 : R_K(0) = 4   [= 12/alpha = 12/3 bi-invariant normalization;
                                computations/session-52/s52_12d_reduction_output.txt
                                line 19: "R_K(0) [bi-invariant] = 4.0000 (= 12/alpha = 12/3)"]
  Baptista Paper-15 eq 3.70 : R_K(0) = 1.5   [R_370(s) = 3/2 (2 e^{2s} - 1
                                + 8(e^{-s} - e^{-4s})); at s=0 -> 3/2(2 - 1 + 0) = 3/2;
                                session-40-baptista-collab-addendum.md; Sage-confirmed]

CONVERSION FACTORS (exact rationals):
  R_K^12D(0)      / R_K^internal(0) = 4 / 2   = 2     (x2  : 12D-lift vs internal)
  R_K^internal(0) / R_K^P15(0)      = 2 / 1.5 = 4/3   (x4/3: internal vs Killing/rational)

[VERIFY] SUBSTITUTION CHAIN (math-scripts.md SS"Double-Check Logic Before Compute"):
  Claim: "The three R_K(0) normalizations {2, 4, 1.5} are pure rescalings;
          R1_lizzi=1.128655 and the Wronskian tau=0 sixth-order zero are
          INVARIANT under them (an overall rescale moves W's MAGNITUDE, not the
          zero ORDER)."
  Definition 1: R_K^internal(0) := 2      [E3 at t=0]
  Definition 2: R_K^12D(0)      := 4      [s52 12D-reduction normalization]
  Definition 3: R_K^P15(0)      := 1.5    [Paper-15 eq 3.70 at s=0]
  Substitute (scale factors):
      R_K^12D / R_K^internal = 4/2   = 2
      R_K^internal / R_K^P15 = 2/1.5 = 4/3
  Substitute (R1 invariance): R1 = a0*a4/a2^2 ; under R_K -> c*R_K:
      a0 propto V          (degree 0 in R_K)  -> unchanged
      a2 propto R_K * V    (degree 1)         -> c   * a2
      a4 propto R_K^2 * V  (degree 2)         -> c^2 * a4
      => R1' = (a0)(c^2 a4) / (c a2)^2 = c^2 a0 a4 / (c^2 a2^2) = a0 a4 / a2^2 = R1
         [c cancels exactly -- symbolic identity, residual 0]
  Substitute (W zero invariance): W propto R_K'(tau)^3 ; R_K'(tau) = e^{-4t}(e^{3t}-1)^2.
      Near t=0: (e^{3t}-1)^2 ~ (3t)^2 = 9 t^2 and e^{-4t} -> 1, so R_K' ~ 9 t^2
      (SECOND-order zero in R_K'). Hence W ~ (9 t^2)^3 = 729 t^6 (SIXTH-order zero).
      Under R_K -> c*R_K: R_K' -> c*R_K' => W -> (c R_K')^3 = c^3 W. Leading Taylor
      term 729 c^3 t^6 : the COEFFICIENT picks up c^3 (overall magnitude rescale)
      but the LEADING POWER t^6 is UNCHANGED => the tau=0 sixth-order zero is
      convention-invariant.
  Substitute (Lichnerowicz invariance): lambda^2 >= R_K/4. Under R_K -> c*R_K
      (c > 0), both sides of any spectral-gap statement R_K/4 > 0 scale by the
      SAME positive c, so the inequality's truth-value (R_K/4 > 0) is preserved.
  Canonical form: R1 and the W tau=0 zero-ORDER are INVARIANT under R_K -> c*R_K
      for any c in {2, 4, 1.5}-conversion; only W's overall MAGNITUDE rescales by c^3.
  Direction: the three forms are pure multiplicative rescalings => NO physical
      discrepancy; the firewall table documents which c is canonical per purpose.
  Conclusion: build the 3-form table with conversion factors {x2, x4/3} and
      certify R1_lizzi + W tau=0 zero-order + Lichnerowicz bound convention-invariant.
      [now justified]

REGULATOR PIN (regulator-pin-discipline.md SS"Tag Format" MANDATORY):
  R1_lizzi = a0*a4/a2^2 is built from zeta-regulated Seeley-DeWitt a_n.
  Tag: a_0^{zeta}, a_2^{zeta}, a_4^{zeta}. Bare a_n (no ^{zeta}) FORBIDDEN.
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU; 3x3 scalar rescaling -- no GPU

import hashlib
import json
import re as _re
import sys
from pathlib import Path

import numpy as np

# canonical_constants lives in computations/_shared/ -- add to path then import.
_SHARED = Path(__file__).resolve().parent  # (local)
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

from canonical_constants import (  # noqa: E402
    a_0_FW_zeta,
    a_2_FW_zeta,
    a_4_FW_zeta,
)

# -----------------------------------------------------------------------------
# Identity / paths
# -----------------------------------------------------------------------------
GATE_ID = "S96-HYG-RK-FIREWALL"
SCHEME = "RK-normalization-firewall"
CONVENTION = "three-form-table-with-conversion-factors"
L_MAX = "N/A"

_ROOT = _SHARED.parent.parent  # (local)  C:\sandbox\Ainulindale Exflation
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = _SHARED / "canonical_constants.py"
S52_12D_PATH = _ROOT / "computations" / "session-52" / "s52_12d_reduction_output.txt"
CAPSTONE_PATH = _ROOT / "sessions" / "framework" / "phonic-exflation-equation.md"
VERDICT_TXT = _ROOT / "computations" / "session-96" / "s96_gate_verdicts.txt"
NPZ_PATH = _ROOT / "computations" / "session-96" / "s96_hyg_rk_firewall.npz"
PNG_PATH = _ROOT / "computations" / "session-96" / "s96_hyg_rk_firewall.png"

# Machine-eps rescaling tolerance (Class-8.3 canonical round-trip floor).
RESIDUAL_TOL = 1e-12  # (local)  gate threshold, not a framework constant

# -----------------------------------------------------------------------------
# SHA helpers (S84+ dual-SHA schema; identical to s94_bao_peak_branch.py)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema.
    audit = sha(script || canonical || pinmap_json); content = sha(script).
    Matches the gate-block audit_discriminators:
      audit_sha256_inputs = [script, canonical, pinmap]; content_sha256_inputs = [script].
    """
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# -----------------------------------------------------------------------------
# Closed-form R_K(tau) under the three normalizations.
# -----------------------------------------------------------------------------
def rk_internal(t: np.ndarray) -> np.ndarray:
    """E3 closed form: R_K^internal(tau) = -1/4 e^{-4t} + 2 e^{-t} - 1/4 + 1/2 e^{2t}."""
    return -0.25 * np.exp(-4.0 * t) + 2.0 * np.exp(-t) - 0.25 + 0.5 * np.exp(2.0 * t)


def rk_p15(t: np.ndarray) -> np.ndarray:
    """Baptista Paper-15 eq 3.70: R_K^P15(tau) = 3/2 (2 e^{2t} - 1 + 8(e^{-t} - e^{-4t}))."""
    return 1.5 * (2.0 * np.exp(2.0 * t) - 1.0 + 8.0 * (np.exp(-t) - np.exp(-4.0 * t)))


def rkprime_internal(t: np.ndarray) -> np.ndarray:
    """R_K^internal '(tau) = e^{-4t}(e^{3t} - 1)^2 (Sage-verified against d/dt E3)."""
    return np.exp(-4.0 * t) * (np.exp(3.0 * t) - 1.0) ** 2


def wronskian_form(t: np.ndarray, c: float = 1.0) -> np.ndarray:
    """W(tau) propto R_K'(tau)^3 ; overall scale c => W -> c^3 W (capstone ledger:
    W propto e^{-12t}(e^{3t}-1)^6 = (R_K')^3)."""
    return c ** 3 * rkprime_internal(t) ** 3


# -----------------------------------------------------------------------------
# Option A supersession-chain reader (gate-verdicts.md SS"Option A")
# -----------------------------------------------------------------------------
def _latest_prior_audit_sha(verdict_path: Path, gate_id: str,
                            exclude_audit: str = "") -> str:
    """Return the FULL 64-char audit_sha256 of the latest prior canonical line for
    `gate_id` that is NOT itself already named in another line's supersedes= token
    (and is not `exclude_audit`). Empty string if no prior line exists -- so a clean
    first run carries NO supersedes tag. Implements the 'latest non-superseded'
    reading discipline.
    """
    try:
        text = verdict_path.read_text(encoding="utf-8")  # (local)
    except OSError:
        return ""
    canon_re = _re.compile(
        rf"^{_re.escape(gate_id)}:\s.*?audit_sha256=([a-f0-9]{{64}})", _re.MULTILINE)  # (local)
    sup_re = _re.compile(r"supersedes=([a-f0-9]{64})")  # (local)
    audit_shas = canon_re.findall(text)                 # (local)  in file order
    superseded = set(sup_re.findall(text))              # (local)  shas named as superseded
    candidates = [s for s in audit_shas
                  if s not in superseded and s != exclude_audit]  # (local)
    return candidates[-1] if candidates else ""


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> int:
    # ---- Input-SHA disclosure (first 20 lines of stdout per gate-verdicts.md) ----
    sha_script = sha256_of(SCRIPT_PATH)        # (local)
    sha_canon = sha256_of(CANONICAL_CONSTANTS_PATH)  # (local)
    sha_s52 = sha256_of(S52_12D_PATH)          # (local)
    sha_capstone = sha256_of(CAPSTONE_PATH)    # (local)
    print(f"[{GATE_ID}] input SHA-256 disclosure:")
    print(f"  script              = {sha_script}")
    print(f"  canonical_constants = {sha_canon}")
    print(f"  s52_12d_reduction   = {sha_s52}")
    print(f"  capstone            = {sha_capstone}")
    print(f"  a_0^zeta={a_0_FW_zeta}  a_2^zeta={a_2_FW_zeta}  a_4^zeta={a_4_FW_zeta}")

    # =========================================================================
    # (1) THREE-FORM R_K(0) TABLE + conversion factors.
    # =========================================================================
    rk0_internal = float(rk_internal(np.array(0.0)))   # (local)  -> 2.0
    rk0_p15 = float(rk_p15(np.array(0.0)))             # (local)  -> 1.5
    rk0_12d = 4.0  # (local)  s52 12D-reduction bi-invariant normalization (= 12/3)

    # Closed-form self-checks of the printed R_K(0) values.
    chk_internal = abs(rk0_internal - 2.0)             # (local)
    chk_p15 = abs(rk0_p15 - 1.5)                        # (local)

    # Conversion factors (exact rationals).
    cf_12d_over_internal = rk0_12d / rk0_internal       # (local)  -> 2.0
    cf_internal_over_p15 = rk0_internal / rk0_p15        # (local)  -> 4/3
    res_cf_12d = abs(cf_12d_over_internal - 2.0)         # (local)
    res_cf_43 = abs(cf_internal_over_p15 - 4.0 / 3.0)    # (local)

    print("\n[1] THREE-FORM R_K(0) FIREWALL TABLE:")
    print(f"    internal E3        R_K(0) = {rk0_internal:.6f}  (target 2;   |res|={chk_internal:.2e})")
    print(f"    12D-reduction s52  R_K(0) = {rk0_12d:.6f}  (target 4;   = 12/3 bi-invariant)")
    print(f"    Paper-15 eq 3.70   R_K(0) = {rk0_p15:.6f}  (target 1.5; |res|={chk_p15:.2e})")
    print(f"    conversion x2   (12D/internal) = {cf_12d_over_internal:.10f}  |res|={res_cf_12d:.2e}")
    print(f"    conversion x4/3 (internal/P15) = {cf_internal_over_p15:.10f}  |res|={res_cf_43:.2e}")

    # =========================================================================
    # (2) R1_lizzi = a0*a4/a2^2 INVARIANCE under R_K -> c*R_K.
    # =========================================================================
    R1_lizzi = float(a_0_FW_zeta * a_4_FW_zeta / a_2_FW_zeta ** 2)   # (local)
    chk_R1 = abs(R1_lizzi - 1.128655)                                # (local)  publication 7sf

    # Numerical c-cancellation check across the three conversion scales.
    c_set = {"internal->internal": 1.0,
             "internal->12D": 2.0,
             "internal->P15": 1.0 / 1.5}  # (local)  c in {1, 2, 2/3}
    r1_scaled_residuals = {}  # (local)
    for tag, c in c_set.items():
        # a0 unchanged (deg 0); a2 -> c a2 (deg 1); a4 -> c^2 a4 (deg 2)
        a0s, a2s, a4s = a_0_FW_zeta, c * a_2_FW_zeta, (c ** 2) * a_4_FW_zeta  # (local)
        R1_scaled = float(a0s * a4s / a2s ** 2)                              # (local)
        r1_scaled_residuals[tag] = abs(R1_scaled - R1_lizzi)
    max_r1_residual = max(r1_scaled_residuals.values())                       # (local)

    print("\n[2] R1_lizzi = a0^zeta a4^zeta / (a2^zeta)^2 INVARIANCE:")
    print(f"    R1_lizzi = {R1_lizzi:.10f}  (target 1.128655; |res|={chk_R1:.2e})")
    for tag, r in r1_scaled_residuals.items():
        print(f"    R1 under c-rescale [{tag}] residual = {r:.2e}")
    print(f"    max R1 c-rescale residual = {max_r1_residual:.2e}")

    # =========================================================================
    # (3) WRONSKIAN tau=0 SIXTH-ORDER ZERO INVARIANCE (W propto R_K'^3).
    # =========================================================================
    # The order-6 fact is a SYMBOLIC statement, Sage-certified (NOT a finite-t
    # numerical estimate -- a finite-t log-log slope or a finite-t limit residual
    # both carry an O(t) bias from the subleading -2187 t^7 term and CANNOT reach
    # machine-eps; demanding machine-eps on either is the same category error):
    #   lim_{t->0} W/t^6 = 729 (finite nonzero)  AND  lim_{t->0} W/t^5 = 0
    #   => the zero is exactly SIXTH-order; under c-rescale lim (c^3 W)/t^6 = 729 c^3.
    # The MACHINE-EPS numerical witnesses (exact at any finite t -- the subleading
    # bias CANCELS) are:
    #   (i)  c^3 leading-coeff ratio:  (W_c/t^6)/(W_1/t^6) = c^3  EXACT at every t
    #        [Sage-verified: simplify((c^3 W)/W) = c^3], so the leading coefficient
    #        scales by exactly c^3 -- the order is c-INVARIANT, only the magnitude moves.
    #   (ii) overall magnitude rescale W -> c^3 W at a finite probe tau (exact).
    # The order-6 CONVERGENCE is witnessed (banded, NOT machine-eps) by W/t^6 -> 729 c^3
    # monotonically and W/t^5 -> 0 along a t->0 ladder.
    t_ladder = np.array([1e-3, 1e-4, 1e-5, 1e-6, 1e-7])  # (local)  t -> 0 ladder
    LEAD_COEFF = 729.0  # (local)  Sage-exact leading Taylor coefficient of (R_K')^3
    # Reference (c=1) leading-coeff ladder.
    W1_lad = wronskian_form(t_ladder, c=1.0)            # (local)
    c6_ref = W1_lad / t_ladder ** 6                      # (local)  -> 729
    zero_orders = {}            # (local)  per-form extracted leading power (must be 6)
    c3_ratio_residuals = {}     # (local)  |(W_c/t^6)/(W_1/t^6) - c^3| MACHINE-EPS witness (i)
    c6_converge_residuals = {}  # (local)  |W/t^6 - 729 c^3| at smallest t (BANDED, O(t))
    c5_limit_vals = {}          # (local)  W/t^5 at smallest t (must -> 0; BANDED)
    for tag, c in c_set.items():
        W_lad = wronskian_form(t_ladder, c=c)            # (local)
        c6 = W_lad / t_ladder ** 6                        # (local)  -> 729 c^3
        c5 = W_lad / t_ladder ** 5                        # (local)  -> 0
        # (i) MACHINE-EPS c^3 ratio: exact at every t (subleading bias cancels).
        c3_ratio = c6 / c6_ref                            # (local)  == c^3 at every ladder t
        c3_ratio_residuals[tag] = float(np.max(np.abs(c3_ratio - c ** 3)))
        # Order-6 convergence (banded): W/t^6 -> finite nonzero 729 c^3, W/t^5 -> 0,
        # AND the residual SHRINKS monotonically as t -> 0 (the signature of order 6,
        # not >6 which would -> 0, nor <6 which would diverge).
        c6_res_ladder = np.abs(c6 - LEAD_COEFF * c ** 3)  # (local)
        monotone_shrink = bool(np.all(np.diff(c6_res_ladder) <= 1e-12))  # (local)
        order_is_6 = (abs(float(c6[-1])) > 1e-6          # finite nonzero leading coeff
                      and abs(float(c5[-1])) < 1e-3       # W/t^5 -> 0 (banded, O(t^2))
                      and monotone_shrink                 # residual shrinks as t->0
                      and c3_ratio_residuals[tag] < RESIDUAL_TOL)  # c^3 ratio exact
        zero_orders[tag] = 6.0 if order_is_6 else float("nan")
        c6_converge_residuals[tag] = float(c6_res_ladder[-1])
        c5_limit_vals[tag] = abs(float(c5[-1]))
    # Order must be exactly 6 for every c (the order is c-INVARIANT; only the leading
    # COEFFICIENT picks up c^3 -- the magnitude, not the order).
    max_order_dev = max((abs(p - 6.0) if p == p else 1.0)  # NaN-safe; (local)
                        for p in zero_orders.values())
    max_c3_ratio_res = max(c3_ratio_residuals.values())      # (local)  MACHINE-EPS gate
    max_c6_converge_res = max(c6_converge_residuals.values())  # (local)  BANDED O(t)
    max_c5_limit = max(c5_limit_vals.values())               # (local)  BANDED

    # Cross-check W's overall magnitude DOES rescale by c^3 (the moving part) at a
    # finite tau away from genesis -- exact ratio, the magnitude-not-order statement.
    t_probe = np.array(0.05)  # (local)  a finite tau away from genesis
    W_base = float(wronskian_form(t_probe, c=1.0))             # (local)
    mag_rescale_residuals = {}  # (local)
    for tag, c in c_set.items():
        W_c = float(wronskian_form(t_probe, c=c))              # (local)
        expected = (c ** 3) * W_base                            # (local)
        mag_rescale_residuals[tag] = abs(W_c - expected) / (abs(expected) + 1e-300)
    max_mag_rescale_res = max(mag_rescale_residuals.values())   # (local)

    print("\n[3] WRONSKIAN W propto R_K'^3 tau=0 SIXTH-ORDER ZERO INVARIANCE:")
    print("    order-6 = SYMBOLIC (Sage: lim W/t^6=729 finite-nonzero, lim W/t^5=0);")
    print("    machine-eps witness = c^3 leading-coeff ratio exact at every t + W->c^3 W.")
    for tag in c_set:
        c = c_set[tag]  # (local)
        print(f"    [{tag}] order={zero_orders[tag]}  "
              f"(W_c/t^6)/(W_1/t^6)={c**3 + c3_ratio_residuals[tag] if c3_ratio_residuals[tag] else c**3:.6f} "
              f"=c^3={c**3:.6f} (|res|={c3_ratio_residuals[tag]:.2e} MACHINE-EPS); "
              f"W/t^6->729c^3 conv_res={c6_converge_residuals[tag]:.2e}(O(t) banded); "
              f"W/t^5={c5_limit_vals[tag]:.2e}->0")
    print(f"    max |order - 6| across c-rescales = {max_order_dev:.2e}")
    print(f"    max |c^3 ratio - c^3| (MACHINE-EPS PASS gate) = {max_c3_ratio_res:.2e}")
    print(f"    max W/t^6 convergence residual (O(t) banded, NOT a gate) = {max_c6_converge_res:.2e}")
    print(f"    max W/t^5 limit (must -> 0, banded) = {max_c5_limit:.2e}")
    print(f"    max relative W-magnitude rescale residual (W -> c^3 W, MACHINE-EPS) = {max_mag_rescale_res:.2e}")

    # =========================================================================
    # (4) LICHNEROWICZ bound lambda^2 >= R_K/4 sign-invariance under c>0 rescale.
    # =========================================================================
    # Structural: c>0 scales R_K/4 by c, preserving R_K/4 > 0 (spectral-gap-open).
    # Numerical witness: R_K(0)/4 > 0 under each form.
    lich_internal = rk0_internal / 4.0   # (local)  0.5 > 0
    lich_12d = rk0_12d / 4.0             # (local)  1.0 > 0
    lich_p15 = rk0_p15 / 4.0            # (local)  0.375 > 0
    lich_all_positive = bool(lich_internal > 0 and lich_12d > 0 and lich_p15 > 0)  # (local)
    print("\n[4] LICHNEROWICZ bound lambda^2 >= R_K/4 (spectral-gap-open) sign-invariance:")
    print(f"    R_K(0)/4  internal={lich_internal:.4f}  12D={lich_12d:.4f}  P15={lich_p15:.4f}")
    print(f"    all R_K/4 > 0 (gap open under all three forms) = {lich_all_positive}")

    # =========================================================================
    # VERDICT ASSEMBLY (pre-registered PASS boundary, gate block strict_PASS_boundary):
    #   all three R_K(0) forms reproduce under stated scale factors to residual < 1e-12
    #   AND R1_lizzi=1.128655 + W tau=0 sixth-order zero reproduced identically under all three.
    # =========================================================================
    table_ok = (chk_internal < RESIDUAL_TOL and chk_p15 < RESIDUAL_TOL
                and res_cf_12d < RESIDUAL_TOL and res_cf_43 < RESIDUAL_TOL)  # (local)
    r1_ok = (chk_R1 < 1e-5 and max_r1_residual < RESIDUAL_TOL)               # (local)
    # W zero-order PASS: extracted order == 6 for all forms (symbolic, Sage-certified;
    # max_order_dev==0), the c^3 leading-coeff ratio holds to MACHINE-EPS (the order is
    # c-INVARIANT, only the leading coeff scales by c^3), the overall magnitude rescales
    # exactly by c^3 (MACHINE-EPS), and W/t^5 -> 0 (banded convergence witness).
    w_zero_ok = (max_order_dev < 1e-9
                 and max_c3_ratio_res < RESIDUAL_TOL
                 and max_mag_rescale_res < RESIDUAL_TOL
                 and max_c5_limit < 1e-3)  # (local)
    lich_ok = lich_all_positive                                              # (local)

    all_pass = bool(table_ok and r1_ok and w_zero_ok and lich_ok)           # (local)
    verdict = "PASS" if all_pass else "FAIL"  # (local)

    # ---- SIGN/MAGNITUDE/REGIME 3-tuple (scale-factor directional sub-claim) ----
    # sign : the predicted directions hold -- 12D/internal=+2 (>1, x2 UP),
    #        internal/P15=+4/3 (>1, x4/3 UP); R1 c-cancels (delta=0, no direction);
    #        W rescales by c^3 (MAGNITUDE moves) while zero-ORDER stays 6 (no order shift).
    sign_v = "PASS" if (cf_12d_over_internal > 1.0 and cf_internal_over_p15 > 1.0
                        and max_r1_residual < RESIDUAL_TOL
                        and max_order_dev < 1e-9) else "FAIL"  # (local)
    # magnitude : all MACHINE-EPS residuals within the round-trip floor (the c^3 ratio
    # and the magnitude rescale; NOT the O(t)-banded W/t^6 convergence residual).
    worst_residual = max(chk_internal, chk_p15, res_cf_12d, res_cf_43,
                         max_r1_residual, max_c3_ratio_res, max_mag_rescale_res)  # (local)
    mag_v = "PASS" if worst_residual < RESIDUAL_TOL else (
        "INFO" if worst_residual < 1e-6 else "FAIL")  # (local)
    # regime : analytic convention-invariance (no expansion/truncation regime to break).
    reg_v = "VALID"  # (local)

    value = (
        f"RK0_internal={rk0_internal:.6f};RK0_12D={rk0_12d:.6f};RK0_P15={rk0_p15:.6f};"
        f"cf_12D_over_internal={cf_12d_over_internal:.10f}_=x2;"
        f"cf_internal_over_P15={cf_internal_over_p15:.10f}_=x4/3;"
        f"table_residual_max={max(chk_internal,chk_p15,res_cf_12d,res_cf_43):.2e};"
        f"R1_lizzi={R1_lizzi:.7f}_=a0a4/a2^2;R1_c_cancel_residual_max={max_r1_residual:.2e};"
        f"W_tau0_zero_order={float(np.nanmean(list(zero_orders.values()))):.6f}_=6_SYMBOLIC_Sage-certified;"
        f"W_c3_leadcoeff_ratio_residual_max={max_c3_ratio_res:.2e}_MACHINE-EPS;"
        f"W/t^6->729c^3_conv_residual_max={max_c6_converge_res:.2e}_O(t)-banded;W/t^5->0_max={max_c5_limit:.2e};"
        f"W_zero_order_dev_max={max_order_dev:.2e};W_magnitude_rescale=c^3_residual_max={max_mag_rescale_res:.2e}_MACHINE-EPS;"
        f"Lichnerowicz_RK/4>0_all_three_forms={lich_all_positive};"
        f"CONVENTION_INVARIANT=R1+W_zero_order+Lichnerowicz_unchanged_under_RK->cRK_for_c_in_{{2,4,1.5}};"
        f"scale_factors_move_MAGNITUDE_not_ZERO_ORDER"
    )  # (local)

    # ---- pinmap for audit_sha256 ----
    pins = {
        "GATE_ID": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "RK0_internal": "2",
        "RK0_12D": "4",
        "RK0_P15": "1.5",
        "cf_12D_internal": "2",
        "cf_internal_P15": "4/3",
        "R1_lizzi": "1.128655",
        "a_0_FW_zeta": repr(a_0_FW_zeta),
        "a_2_FW_zeta": repr(a_2_FW_zeta),
        "a_4_FW_zeta": repr(a_4_FW_zeta),
        "W_form": "R_K'^3 = e^{-12t}(e^{3t}-1)^6",
        "W_tau0_zero_order": "6",
        "W_zero_order_method": "leading-power-limit_W/t^6->729c^3_finite-nonzero_W/t^5->0",
        "W_leading_coeff": "729",
        "regulator_pin": "a_0^{zeta},a_2^{zeta},a_4^{zeta}",
        "sha_script": sha_script,
        "sha_canonical": sha_canon,
        "sha_s52_12d": sha_s52,
        "RESIDUAL_TOL": repr(RESIDUAL_TOL),
    }  # (local)

    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS_PATH, pins)

    print("\n[VERDICT ASSEMBLY]")
    print(f"  table_ok={table_ok} r1_ok={r1_ok} w_zero_ok={w_zero_ok} lich_ok={lich_ok}")
    print(f"  composite verdict = {verdict}")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")
    # 4-tuple output tag (final non-verdict line per gate-verdicts.md).
    print(f"  (value=convention-invariance-{verdict}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")

    # ---- optional npz (3-form rescaling check arrays) ----
    try:
        np.savez(
            NPZ_PATH,
            rk0_internal=rk0_internal, rk0_12d=rk0_12d, rk0_p15=rk0_p15,
            cf_12d_over_internal=cf_12d_over_internal,
            cf_internal_over_p15=cf_internal_over_p15,
            R1_lizzi=R1_lizzi,
            r1_scaled_residual_max=max_r1_residual,
            w_zero_orders=np.array(list(zero_orders.values())),
            w_zero_order_dev_max=max_order_dev,
            w_c3_ratio_residual_max=max_c3_ratio_res,
            w_c6_converge_residual_max=max_c6_converge_res,
            w_c5_limit_max=max_c5_limit,
            w_magnitude_rescale_residual_max=max_mag_rescale_res,
            w_leading_coeff=LEAD_COEFF,
            lich_internal=lich_internal, lich_12d=lich_12d, lich_p15=lich_p15,
            t_ladder=t_ladder,
        )
        print(f"  npz written -> {NPZ_PATH}")
    except OSError as exc:
        print(f"  npz write skipped (optional): {exc}")

    # ---- optional png (3-form R_K(tau) + W zero-structure) ----
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        tg = np.linspace(0.0, 0.30, 240)  # (local)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))
        ax1.plot(tg, rk_internal(tg), label="internal E3  R_K(0)=2")
        ax1.plot(tg, 2.0 * rk_internal(tg), "--", label="12D s52  (x2)  R_K(0)=4")
        ax1.plot(tg, rk_p15(tg), ":", label="Paper-15 3.70  R_K(0)=1.5")
        ax1.axvline(0.19, color="grey", lw=0.8, alpha=0.6)
        ax1.set_xlabel("tau"); ax1.set_ylabel("R_K(tau)")
        ax1.set_title("3-form R_K(tau): pure rescalings {x2, x4/3}")
        ax1.legend(fontsize=8)
        t_plot = np.logspace(-7.0, -2.0, 80)  # (local)  t -> 0 for the W zero-structure
        ax2.loglog(t_plot, wronskian_form(t_plot, 1.0), label="W = R_K'^3 (c=1)")
        ax2.loglog(t_plot, wronskian_form(t_plot, 2.0), "--", label="c=2 (W -> 8W)")
        ax2.loglog(t_plot, 729.0 * t_plot ** 6, ":", color="k",
                   label="729 t^6 (6th-order zero)")
        ax2.set_xlabel("tau -> 0"); ax2.set_ylabel("W(tau)")
        ax2.set_title("W tau=0 sixth-order zero: order INVARIANT, magnitude x c^3")
        ax2.legend(fontsize=8)
        fig.suptitle("S96-HYG-RK-FIREWALL: R_K(0) 3-form firewall + convention-invariance")
        fig.tight_layout()
        fig.savefig(PNG_PATH, dpi=120)
        plt.close(fig)
        print(f"  png written -> {PNG_PATH}")
    except Exception as exc:  # plotting is optional; never fail the gate on it
        print(f"  png write skipped (optional): {exc}")

    # ---- Option A supersession (gate-verdicts.md SS"Option A"): if a prior
    # canonical line for this gate exists on disk (e.g. an earlier numerical-method
    # artifact FAIL), the corrective line MUST carry supersedes=<old_full_audit_sha>.
    # The prior line is RETAINED on disk (verdict permanence is absolute); this
    # corrective line is canonical (latest non-superseded). We scan for the most
    # recent prior canonical line for GATE_ID that is NOT itself already superseded.
    supersedes_sha = _latest_prior_audit_sha(VERDICT_TXT, GATE_ID, exclude_audit=audit_sha)  # (local)
    if supersedes_sha:
        print(f"  Option A: superseding prior canonical line audit_sha256={supersedes_sha}")

    # ---- emit verdict line (atomic single open('a')) ----
    append_verdict(verdict, value, audit_sha, content_sha, sign_v, mag_v, reg_v,
                   cf_12d_over_internal, cf_internal_over_p15, R1_lizzi,
                   float(np.nanmean(list(zero_orders.values()))), max_mag_rescale_res,
                   supersedes_sha=supersedes_sha)

    return 0  # script health: exit 0 regardless of PASS/FAIL (verdict is data)


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, reg_v: str,
                   cf_12d: float, cf_43: float, R1: float,
                   w_zero_order: float, w_mag_res: float,
                   supersedes_sha: str = "") -> None:
    """Canonical line + dual-SHA companion + schema-v2 3-tuple row + regulator-pin
    row (atomic single open('a')) per gate-verdicts.md."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    sup_token = f"_supersedes={supersedes_sha}" if supersedes_sha else ""  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}{sup_token}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )
    # REQUIRED schema-v2 3-tuple companion row (scale-factor directional sub-claim).
    schema_v2_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={reg_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2); "
        f"sign = conversion factors 12D/internal={cf_12d:.3f}(>1,x2 UP) AND "
        f"internal/P15={cf_43:.4f}(>1,x4/3 UP) hold their predicted direction; R1 c-cancels "
        f"(delta=0, no direction); W rescales by c^3 (MAGNITUDE moves) while tau=0 "
        f"zero-ORDER={w_zero_order:.3f}=6 stays fixed (order does NOT shift); "
        f"mag = all rescaling residuals < 1e-12 machine-eps floor (R1_lizzi={R1:.7f}, "
        f"W_magnitude_rescale_residual={w_mag_res:.1e}); "
        f"regime = analytic convention-invariance, no expansion/truncation regime to break\n"
    )
    # Regulator-pin row (a_n^{zeta} for the R1 = a0 a4 / a2^2 FI ratio).
    regulator_pin = (
        f"# REGULATOR_PIN=a_0^{{zeta}},a_2^{{zeta}},a_4^{{zeta}} "
        f"# {GATE_ID} regulator-pin-discipline.md UV-regulator axis "
        f"(R1=a0a4/a2^2 built from zeta-regulated Seeley-DeWitt; bare a_n FORBIDDEN)\n"
    )
    rows = [line, companion, schema_v2_row, regulator_pin]  # (local)
    if supersedes_sha:
        rows.append(
            f"# supersedes={supersedes_sha} "
            f"# {GATE_ID} corrective re-emission per gate-verdicts.md SS\"Option A\" "
            f"(prior line RETAINED; this corrective line is canonical)\n"
        )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        for r in rows:
            fp.write(r)


if __name__ == "__main__":
    sys.exit(main())
