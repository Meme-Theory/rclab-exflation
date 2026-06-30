"""
_pauli_villars_subtraction.py — PRIMARY full-physical Pauli-Villars helper
==========================================================================

Implements PRIMARY full-physical Pauli-Villars regularization with
mass-scale running per Connes-Chamseddine 1996 §2.2-2.3, suitable for
substrate-spectral-moment evaluation on the L_max=10 D_K^2 spectrum.

Created: S88 W13-159 (lizzi-spectral-functional-theorist) — TIER1 lift of
W7-3 C-γ-WEAK from SCHEMATIC `_spectral_action_regulators.pauli_villars_a_n`
to PRIMARY level per `substrate-first-canonical-sourcing.md` §(iv).

PRIMARY full-physical specification (Connes-Chamseddine 1996 §2.2-2.3
spectral-action multiplier-vector grading):

    A 2-point Pauli-Villars regulator on the squared-Dirac spectrum lifts
    the Mellin moment from
        M^bare(s) = Σ_k m_k · λ_k^{-2s}                           (SCHEMATIC: f_2-only)
    to
        M^PV_primary(s) = Σ_k m_k · w_PV(λ_k^2; s) · λ_k^{-2s}
    with the multiplier
        w_PV(λ^2; s) = 1 - Σ_{r=1..2} c_r · (M_r^2 / (λ^2 + M_r^2))^s
    where {c_r, M_r} satisfies the Pauli-Villars consistency identities
        Σ_r c_r = 1                       (UV finiteness; identity reproduced
                                           at λ^2 → ∞)
        Σ_r c_r · M_r^2 = 0               (no quadratic divergence; Mellin
                                           multiplier-vector grading
                                           f_0^anomaly = 0 per Andrianov-
                                           Lizzi 1001.2036 §V)
    and the masses run with M_KK as the natural UV scale:
        M_1 = M_KK                        (canonical mass-scale)
        M_2 = M_KK · √2                   (2-point PV pair, Connes-
                                           Chamseddine 1996 §2.2 standard)
        c_1 = +2,  c_2 = -1               (chosen to satisfy the two
                                           consistency identities exactly:
                                           c_1 + c_2 = 1, c_1·M_1² + c_2·M_2² = 2 - 2 = 0)

In the dimensionless eigenvalue convention used by the L_max=10 cache
(λ_k stored in M_KK units), the dimensionless masses are
    m_1 = 1.0,  m_2 = √2  (= 1.4142135...).

This implementation is full-physical (PRIMARY tier per substrate-first-
canonical-sourcing.md §iv) — it carries the explicit 2-point PV pair with
mass-scale running, NOT the single-subtraction SCHEMATIC truncation
`1/λ^{2n} - 1/(λ^2 + M_PV^2)^n` of `_spectral_action_regulators.pauli_villars_a_n`.

Substitution chain (PRIMARY-vs-SCHEMATIC propagation):

    Definitions:
        M^SCH(s) = Σ_k m_k · (λ_k^{-2s} - (λ_k^2 + M_PV^2)^{-s})       (single-subtraction; M_PV² = 0.1·C_max)
        M^PRIM(s) = Σ_k m_k · w_PV(λ_k^2; s) · λ_k^{-2s}              (2-point with running; this module)

    Substitution:
        ratio_PRIM_c(s) = M_R^c,PRIM(s=4) / M_R^c,PRIM(s=2)
        ratio_SCH_c(s)  = M_R^c,SCH(s=4)  / M_R^c,SCH(s=2)

    Simplification:
        For the 4 "bare" classes (zeta/SDW/Zubarev/cutoff_sqrt) the PV
        multiplier w_PV is N/A (these classes' regulators do not invoke
        PV); their ratios are SAME between SCHEMATIC and PRIMARY (no PV
        applied). Only class 5 (anomaly = Pauli-Villars) sees the lift.

    Direction:
        |ratio_PRIM_5 / ratio_SCH_5 - 1| = δ measures the SCHEMATIC-
        vs-PRIMARY propagation factor at class 5; the n_c=(10,10,10,11,13)
        signature is reproduced iff δ < ε_R2 = 0.05 at the integer-fit
        residual threshold.
"""

from __future__ import annotations

import numpy as np

# ---------------------------------------------------------------------------
# 2-point Pauli-Villars consistency check (constants frozen at module load)
# ---------------------------------------------------------------------------

# Coefficients chosen to satisfy:
#   c_1 + c_2 = 1         (UV identity reproduction; Σ c_r = 1)
#   c_1 m_1² + c_2 m_2² = 0     (no quadratic divergence; Σ c_r M_r² = 0)
# With m_1 = 1, m_2 = √2:
#   c_1 + c_2 = 1
#   c_1 · 1 + c_2 · 2 = 0   →   c_2 = -c_1
# Intersect: 2 c_1 - c_1 · 1 = c_1, ... → c_1 = 2, c_2 = -1.

PV_PRIMARY_C = np.array([+2.0, -1.0], dtype=np.float64)
PV_PRIMARY_M_DIMLESS = np.array([1.0, np.sqrt(2.0)], dtype=np.float64)
# (dimensionless: when λ_k is in M_KK units, m_r is dimensionless mass ratio)


def _verify_pv_identities(c_arr=PV_PRIMARY_C, m_arr=PV_PRIMARY_M_DIMLESS):
    """Verify Σ c_r = 1 and Σ c_r m_r² = 0 to machine precision."""
    s_c = float(np.sum(c_arr))
    s_cm2 = float(np.sum(c_arr * m_arr * m_arr))
    return s_c, s_cm2


# Module-load self-check
_S_C_CHECK, _S_CM2_CHECK = _verify_pv_identities()
assert abs(_S_C_CHECK - 1.0) < 1e-15, f"PV Σc_r = {_S_C_CHECK} != 1"
assert abs(_S_CM2_CHECK) < 1e-15, f"PV Σc_r·m_r² = {_S_CM2_CHECK} != 0"


# ---------------------------------------------------------------------------
# PRIMARY 2-point Pauli-Villars multiplier
# ---------------------------------------------------------------------------

def pv_multiplier_primary(lambda_sq, s, c_arr=PV_PRIMARY_C, m_arr=PV_PRIMARY_M_DIMLESS):
    """w_PV(λ²; s) = 1 - Σ_r c_r · (m_r² / (λ² + m_r²))^s.

    Parameters
    ----------
    lambda_sq : ndarray of float
        Squared dimensionless eigenvalues λ_k² (M_KK units).
    s : float
        Mellin index (dimensional convention: Mellin moment is Σ m_k · w · λ_k^{-2s}).

    Returns
    -------
    ndarray of float, same shape as lambda_sq
        Pauli-Villars multiplier w_PV evaluated point-wise.

    Notes
    -----
    With c_1=+2, c_2=-1, m_1=1, m_2=√2, this satisfies:
      - lim_{λ²→∞} w_PV = 1 - 0 = 1 (UV identity reproduction; Σc_r=1)
      - At λ² = 0:  w_PV(0;s) = 1 - (c_1 · 1 + c_2 · 1) = 1 - (2 - 1) = 0
                   (IR finite at zero mass; substrate has spectral gap λ_min ≈ 0.836)
    """
    # Sum over the 2-point PV pair (broadcast along last axis)
    lam2 = np.asarray(lambda_sq, dtype=np.float64)
    out = np.ones_like(lam2)
    for c_r, m_r in zip(c_arr, m_arr):
        out -= c_r * np.power(m_r * m_r / (lam2 + m_r * m_r), s)
    return out


def pv_mellin_moment_primary(s, lambdas, mults,
                             c_arr=PV_PRIMARY_C, m_arr=PV_PRIMARY_M_DIMLESS):
    """M^PV_primary(s) = Σ_k m_k · w_PV(λ_k²; s) · λ_k^{-2s}.

    Parameters
    ----------
    s : float
        Mellin index.
    lambdas : ndarray of float
        Dimensionless eigenvalues |λ_k| (M_KK units).
    mults : ndarray of float
        Multiplicities m_k (per-eigenvalue; SU(3) Weyl-dim weighting baked in).

    Returns
    -------
    float
        Pauli-Villars-regulated Mellin moment at index s.
    """
    lam = np.asarray(lambdas, dtype=np.float64)
    m = np.asarray(mults, dtype=np.float64)
    lam2 = lam * lam
    w = pv_multiplier_primary(lam2, s, c_arr=c_arr, m_arr=m_arr)
    # Σ_k m_k · w_k · λ_k^{-2s}
    return float(np.sum(m * w * np.power(lam2, -s)))


# ---------------------------------------------------------------------------
# SCHEMATIC reference (for SCHEMATIC-vs-PRIMARY propagation comparison)
# ---------------------------------------------------------------------------

def pv_mellin_moment_schematic(s, lambdas, mults, M_PV_sq):
    """SCHEMATIC single-subtraction PV (matches `_spectral_action_regulators.pauli_villars_a_n`).

    M^SCH(s) = Σ_k m_k · (λ_k^{-2s} - (λ_k^2 + M_PV²)^{-s})
    """
    lam = np.asarray(lambdas, dtype=np.float64)
    m = np.asarray(mults, dtype=np.float64)
    lam2 = lam * lam
    bare = np.sum(m * np.power(lam2, -s))
    pv_shift = np.sum(m * np.power(lam2 + M_PV_sq, -s))
    return float(bare - pv_shift)


# ---------------------------------------------------------------------------
# Bare Mellin moment (zeta/SDW class — no PV factor)
# ---------------------------------------------------------------------------

def bare_mellin_moment(s, lambdas, mults):
    """Bare moment: Σ_k m_k · λ_k^{-2s}. Used for class 1 (zeta) and class 2 (SDW)."""
    lam = np.asarray(lambdas, dtype=np.float64)
    m = np.asarray(mults, dtype=np.float64)
    return float(np.sum(m * np.power(lam * lam, -s)))


# ---------------------------------------------------------------------------
# Heat-kernel-dressed moment (Zubarev class)
# ---------------------------------------------------------------------------

def heat_kernel_mellin_moment(s, lambdas, mults, t_ref):
    """Zubarev / heat-kernel: Σ_k m_k · exp(-t_ref · λ_k²) · λ_k^{-2s}.

    The heat-kernel dressing exp(-t·λ²) is the canonical Zubarev regulator;
    at t_ref → 0+ it reduces to the bare moment.
    """
    lam = np.asarray(lambdas, dtype=np.float64)
    m = np.asarray(mults, dtype=np.float64)
    lam2 = lam * lam
    return float(np.sum(m * np.exp(-t_ref * lam2) * np.power(lam2, -s)))


# ---------------------------------------------------------------------------
# Hard-cutoff moment (cutoff_sqrt class)
# ---------------------------------------------------------------------------

def hard_cutoff_mellin_moment(s, lambdas, mults, cutoff_frac=0.7):
    """Hard-cutoff: truncate at λ² ≤ cutoff_frac · max(λ²)."""
    lam = np.asarray(lambdas, dtype=np.float64)
    m = np.asarray(mults, dtype=np.float64)
    lam2 = lam * lam
    threshold = cutoff_frac * float(np.max(lam2))
    mask = lam2 <= threshold
    return float(np.sum(m[mask] * np.power(lam2[mask], -s)))


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("PV PRIMARY multi-point regulator self-test")
    print(f"  c_arr = {PV_PRIMARY_C.tolist()}")
    print(f"  m_arr = {PV_PRIMARY_M_DIMLESS.tolist()}")
    sc, scm2 = _verify_pv_identities()
    print(f"  Σ c_r          = {sc:.16e} (target: 1.0)")
    print(f"  Σ c_r · m_r²   = {scm2:.16e} (target: 0.0)")
    # Synthetic 5-eigenvalue spectrum
    lam_test = np.array([1.0, 1.5, 2.0, 3.0, 4.0])
    m_test = np.array([2.0, 4.0, 8.0, 16.0, 32.0])
    print(f"  test λ        = {lam_test.tolist()}")
    print(f"  test m_k      = {m_test.tolist()}")
    for s in (1.0, 2.0, 3.0, 4.0):
        m_p = pv_mellin_moment_primary(s, lam_test, m_test)
        m_s = pv_mellin_moment_schematic(s, lam_test, m_test, M_PV_sq=0.1 * 16.0)
        m_b = bare_mellin_moment(s, lam_test, m_test)
        print(f"  s={s}: M_bare={m_b:.6e}, M_SCH={m_s:.6e}, M_PRIM={m_p:.6e}")
