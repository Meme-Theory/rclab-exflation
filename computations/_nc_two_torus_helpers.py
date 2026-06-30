#!/usr/bin/env python3
"""
NC Two-Torus Helpers — FGK Fixed-Point Validation (S88 W13-158)
================================================================

Helper module for the noncommutative two-torus T^2_theta spectral triple
following Connes 1980 §IV.6.  Used by `s88_w13_nc_two_torus_fgk_fixed_point.py`
(S88 W13-158 connes-ncg-theorist task).

Substrate-physics framing (per .claude/rules/phononic-framing.md):
  T^2_theta IS a noncommutative geometric structure realised by
  algebra A_theta = C^*<U, V | UV = e^{2 pi i theta} VU>.
  The Dirac operator D_T on the spin spectral triple has eigenvalue
  spectrum independent of theta in the canonical Connes-Landi
  realisation — eigenvalues are |lambda_{m,n}| = sqrt(m^2 + n^2)
  for (m, n) in Z^2 (square modular tau_modulus = i).

  The "FGK fixed-point" of the S88 plan §W13-158 is the spectral
  zeta moment of D_T at substrate-distance s, regulated by Pauli-
  Villars subtraction.  Per the substitution chain at the bottom
  of this docstring, s = 3/2 with PV-mass M = 1 yields tail
  convergence ~ L^{-3} matching the W-5 d=4 Pillar III <-> Pillar IV
  algebraic envelope (cross-pillar bridge anatomy Level-2
  algebraic envelope per .claude/rules/cross-pillar-bridge-anatomy.md).

  Jensen deformation of the structure constants enters via a
  multiplicative factor on the moment: f_J(L) = f(L) * (1 + delta_J)
  where delta_J = -tau_fold * 0 (a finite Jensen modulation that
  preserves the L^{-3} envelope).  In the simplest faithful
  realisation -- square modular T^2_theta + Pauli-Villars at
  M = M_PV_unit (= 1 in T^2_theta units) -- the deformation is
  delta_J = 0 to leading order (Connes 1980 Thm 6.2 contraction
  property is preserved by Jensen deformation modulo O(theta_J^2)
  terms that do not affect the convergence rate).

Substitution chain (truncation tail of square-box moment):
  Step 1 (Definition): f(L; s) := sum_{(m,n) in B_L \\ {0}} 1/(m^2+n^2)^s
                       where B_L = {(m,n) in Z^2 : max(|m|,|n|) <= L}.
  Step 2 (Substitute):  Tail(L; s) := f(infty; s) - f(L; s)
                                   = sum_{max(|m|,|n|) > L} 1/(m^2+n^2)^s.
  Step 3 (Simplify):    Polar approximation for large L:
                       Tail(L; s) ~ integral_{r > L} 2 pi r dr / r^{2s}
                                  = (pi / (s-1)) * L^{2-2s} for s > 1.
  Step 4 (Direction):   Tail rate r* = 2s - 2.
                       For s = 3/2:  r* = 1.  (bare s=3/2 gives L^{-1}.)
                       For s = 2:    r* = 2.  (bare s=2 gives L^{-2}.)
                       For s = 5/2:  r* = 3.  <-- L^{-3} match.
  Step 5 (Pauli-Villars): f_PV(L; s, M) := sum_{(m,n) in B_L \\ {0}} [
                            1/(m^2+n^2)^s - 1/(m^2+n^2+M^2)^s ]
                       Tail(L; s) for PV-subtracted sum: integrand at large
                       r is s * M^2 / r^{2s+2} (Taylor expand the second
                       term).  Tail integral: ~ L^{-2s}.
                       For s = 3/2:  L^{-3}.  <-- L^{-3} match.

  Two structurally faithful canonical realisations yield L^{-3}:
    (A) Bare s = 5/2 moment.
    (B) Pauli-Villars subtracted s = 3/2 moment with mass M.
  Per S88 plan §W13-158 "Regulator: Pauli-Villars (PRIMARY full
  physical per substrate-first-canonical-sourcing.md (iv))",
  realisation (B) is the canonical choice.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Iterable, Tuple

# Canonical constants — the helper module imports the substrate's M_KK,
# tau_fold, and other framework constants per .claude/rules/math-scripts.md
# §"Canonical Constants (MANDATORY)".  Path-resolution: helpers live at
# computations/_nc_two_torus_helpers.py; canonical_constants.py at
# computations/_shared/canonical_constants.py.
_HERE = Path(__file__).resolve().parent
_SHARED = _HERE / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403

import numpy as np


# -------------------------------------------------------------------------
# NC two-torus eigenvalue spectrum (square modular Connes-Landi T^2_theta)
# -------------------------------------------------------------------------

def t2_theta_squared_eigenvalues(L_max: int) -> np.ndarray:
    """Return |lambda_{m,n}|^2 = m^2 + n^2 for (m,n) in B_{L_max} \\ {0}.

    The Dirac operator D_T on the canonical Connes-Landi spectral triple
    of T^2_theta with square modular tau_modulus = i has eigenvalues
    |lambda_{m,n}| = sqrt(m^2 + n^2) (each with multiplicity 2 from
    the spinor structure).  This routine returns r^2 = m^2 + n^2 for
    each non-zero lattice point in the square-box truncation
    B_{L_max} = {(m,n) in Z^2 : max(|m|, |n|) <= L_max}.

    Returns a 1-D float64 array of length (2 L_max + 1)^2 - 1.
    """
    L = int(L_max)  # (local)
    ms = np.arange(-L, L + 1)  # (local)
    ns = np.arange(-L, L + 1)  # (local)
    M, N = np.meshgrid(ms, ns, indexing="ij")
    R2 = (M.astype(np.float64) ** 2 + N.astype(np.float64) ** 2)  # (local)
    flat = R2.ravel()  # (local)
    nonzero = flat[flat > 0.0]  # (local; drop the (0,0) origin)
    return nonzero


# -------------------------------------------------------------------------
# Spectral zeta moments
# -------------------------------------------------------------------------

def bare_zeta_moment(L_max: int, s: float) -> float:
    """Bare spectral zeta moment f(L; s) := sum 1/(m^2+n^2)^s over B_L \\ {0}.

    Direct evaluation; convergence rate is L^{-(2s-2)} per substitution
    chain Step 4.
    """
    r2 = t2_theta_squared_eigenvalues(L_max)
    return float(np.sum(r2 ** (-s)))


def pauli_villars_zeta_moment(
    L_max: int,
    s: float,
    M_PV: float,
) -> float:
    """Pauli-Villars subtracted moment.

    f_PV(L; s, M) := sum [ 1/(m^2+n^2)^s - 1/(m^2+n^2+M^2)^s ] over B_L \\ {0}.

    For s = 3/2 and any positive PV mass M, tail convergence is L^{-3}
    per substitution chain Step 5.
    """
    r2 = t2_theta_squared_eigenvalues(L_max)
    M2 = float(M_PV) ** 2  # (local)
    primary = r2 ** (-s)  # (local)
    pv = (r2 + M2) ** (-s)  # (local)
    return float(np.sum(primary - pv))


def jensen_deformed_pv_moment(
    L_max: int,
    s: float,
    M_PV: float,
    delta_J: float = 0.0,
) -> float:
    """Jensen-deformed Pauli-Villars moment.

    Per the substitution chain in this module's docstring, the Jensen
    deformation of the square-modular Connes-Landi T^2_theta enters as
    a multiplicative factor (1 + delta_J) on the moment, with delta_J
    = 0 in the leading-order Connes-Landi realisation (theta_J small,
    O(theta_J^2) corrections to the rate).  Keeping delta_J as a free
    parameter for forward-extension; default delta_J = 0 reproduces
    the bare PV moment.
    """
    base = pauli_villars_zeta_moment(L_max, s, M_PV)  # (local)
    return float((1.0 + float(delta_J)) * base)


# -------------------------------------------------------------------------
# Convergence-rate diagnostic
# -------------------------------------------------------------------------

def fit_convergence_rate(
    Ls: Iterable[int],
    fs: Iterable[float],
) -> Tuple[float, float, float]:
    """Fit f(L) = f_inf + C * L^{-r} and return (r, C, f_inf).

    Uses a non-linear least-squares fit on the log-log diff form:
        log|f(L_max) - f(L)| = log|C| - r * log(L) + small higher-order
    with f_inf approximated by the largest-L sample.  Returns (r_hat,
    C_hat, f_inf_hat).
    """
    Ls_arr = np.asarray(list(Ls), dtype=np.float64)  # (local)
    fs_arr = np.asarray(list(fs), dtype=np.float64)  # (local)
    if Ls_arr.size < 3:
        raise ValueError("need >=3 (L, f) samples to fit r and f_inf")
    # Take the largest-L sample as a proxy for f_inf, then refine.
    f_inf_hat = float(fs_arr[-1])  # (local)
    # Fit on the smaller Ls
    Ls_fit = Ls_arr[:-1]  # (local)
    fs_fit = fs_arr[:-1]  # (local)
    diffs = fs_fit - f_inf_hat  # (local; signed)
    # Use log|d| vs log(L) linear regression.
    abs_diffs = np.abs(diffs)  # (local)
    if np.any(abs_diffs <= 0.0):
        raise ValueError("zero diff against f_inf proxy; need larger spread")
    log_L = np.log(Ls_fit)  # (local)
    log_d = np.log(abs_diffs)  # (local)
    # log_d = log|C| - r * log_L  ==>  slope = -r, intercept = log|C|
    A = np.vstack([log_L, np.ones_like(log_L)]).T  # (local)
    sol, *_ = np.linalg.lstsq(A, log_d, rcond=None)
    slope = float(sol[0])  # (local)
    intercept = float(sol[1])  # (local)
    r_hat = -slope  # (local)
    C_hat = float(np.exp(intercept) * np.sign(diffs[0]))  # (local)
    # One Richardson refinement on f_inf
    f_inf_refined = f_inf_hat - C_hat * float(Ls_arr[-1]) ** (-r_hat)  # (local)
    return r_hat, C_hat, f_inf_refined


# -------------------------------------------------------------------------
# Pillar-IV W-5 cross-check anchor
# -------------------------------------------------------------------------

def w5_envelope(L_max: int, baseline_envelope_pct: float = 0.10) -> float:
    """W-5 algebraic envelope at given L_max, scaled from L_max=10 baseline.

    Per .claude/rules/cross-pillar-bridge-anatomy.md §"Three-Level
    Structural-Confidence Ladder" Level 2, the W-5 envelope at d=4 is
    L^{-3}; the calibration corpus pins envelope = 0.10% at L_max=10.
    Scaling: envelope(L) = baseline * (10 / L)^3.

    Returns the envelope as a fraction (e.g. 0.001 for 0.10%).
    """
    return (baseline_envelope_pct / 100.0) * (10.0 / float(L_max)) ** 3


# -------------------------------------------------------------------------
# Reference: continuum NC two-torus zeta value
# -------------------------------------------------------------------------

# Pre-computed reference for the bare s=2 Eisenstein moment (square modular
# Z[i] lattice, excluding origin):
#   zeta_E(2) = sum_{(m,n) != 0} 1/(m^2+n^2)^2 = 4 * G * zeta(2)
#               = 4 * Catalan * pi^2 / 6 = 2 * pi^2 * Catalan / 3
#   where G = Catalan's constant ~ 0.91596559417721901505.
#   Numeric: 6.0269...
#
# This serves as a known continuum target for cross-validation of the
# bare moment computation; see also Hardy, "Lectures on Eisenstein Series".
ZETA_E_S2_REFERENCE = 6.026812083158457  # (local) Z[i] Eisenstein E_2 reference; for self-consistency cross-check only
