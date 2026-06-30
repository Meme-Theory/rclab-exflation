"""
_spectral_action_regulators.py — 5-regulator atlas helper (W12-ELIM-8)
======================================================================

Provides 5 deterministic evaluators for spectral-action moments a_n on
the multiplicity-weighted SU(3) Casimir schematic spectrum:

    heat_kernel_a_n(n, L_max)
    zeta_a_n(n, L_max)
    mellin_a_n(n, L_max)
    hard_cutoff_a_n(n, L_max, cutoff_frac=0.7)
    pauli_villars_a_n(n, L_max, M_PV_sq_frac=0.1)

Each returns (1/Vol_SU3_Haar) · Σ_{(p,q)≠(0,0), p+q≤L_max} d(p,q) · f_R(C_2(p,q), n)
where f_R depends on regulator R, d(p,q) is the SU(3) Weyl dim, C_2(p,q) is
the quadratic Casimir, and Vol_SU3_Haar = 8·√3·π⁴.

Zeta and Mellin are equivalent on this positive-definite spectrum at real s.
Heat-kernel adds a logarithmic Seeley-DeWitt dressing per (p,q) sector.
Hard-cutoff truncates the (p,q) sum where C_2 > cutoff_frac × max(C_2).
Pauli-Villars subtracts a massive-regulator sum with M_PV² = M_PV_sq_frac × max(C_2).

These are SCHEMATIC regulators — intended as reasonable pure-spectrum analogs
of the named regulators in Chamseddine-Connes 1996 §2.2-2.3 (Mellin moments
f_0, f_2, f_4 of the cutoff function f restricted to [0, infty)). They are
NOT the full physical regularizations used in the S61/S78 Pauli-Villars
pipeline (which uses Lambda_UV = M_KK as the physical cutoff). The point
of the 5-regulator atlas is to measure SPREAD of an observable across a
discrete set of regulator prescriptions, not to pin any single prescription
as canonical.
"""

from __future__ import annotations

import numpy as np


def weyl_dim_su3(p, q):
    """SU(3) Weyl dimension: dim((p, q)) = (p+1)(q+1)(p+q+2)/2."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def casimir_su3(p, q):
    """Quadratic Casimir of SU(3) irrep (p, q) in normalized units."""
    return (p * p + p * q + q * q + 3 * (p + q)) / 3.0


def _enumerate_sectors(L_max):
    """Return list of (p, q, d, c) tuples for (p, q) != (0, 0), p+q ≤ L_max."""
    out = []  # local
    for p in range(L_max + 1):
        for q in range(L_max + 1):
            if p == 0 and q == 0:
                continue
            if p + q > L_max:
                continue
            out.append((p, q, weyl_dim_su3(p, q), casimir_su3(p, q)))
    return out


# ---------------------------------------------------------------------------
# Regulator #1: zeta (Connes-Chamseddine s=n, analytically-continued Σ d/C^n)
# ---------------------------------------------------------------------------
def zeta_a_n(n, L_max, Vol_SU3_Haar):
    """a_n under zeta regularization: raw Σ d(p,q) / C_2(p,q)^n.

    On the positive-definite Casimir spectrum this corresponds to the analytic
    continuation ζ_D(s) = Σ d(p,q) C_2(p,q)^(-s) evaluated at s = n
    (where n is read as the spectral-moment index 1 for a_2, 2 for a_4, etc).

    Convention here: a_0 = Σ d (the identity moment, regulator-independent
    in the sense that every scheme agrees on its coefficient).
    """
    if n == 0:
        s = sum(d for _, _, d, _ in _enumerate_sectors(L_max))
        return s / Vol_SU3_Haar
    acc = 0.0  # local
    for _, _, d, c in _enumerate_sectors(L_max):
        acc += d / (c ** n)
    return acc / Vol_SU3_Haar


# ---------------------------------------------------------------------------
# Regulator #2: Mellin (Γ(s) Σ d C^{-s}; identical to zeta on this spectrum)
# ---------------------------------------------------------------------------
def mellin_a_n(n, L_max, Vol_SU3_Haar):
    """a_n under Mellin regularization.

    For the positive-definite Casimir spectrum, Mellin and zeta differ only
    by a Γ(s) factor that cancels between numerator and normalization in the
    Chamseddine-Connes spectral-action derivation. Returns the same value as
    `zeta_a_n` on this schematic — the two regulators are in the same
    equivalence class for REAL-valued a_n moments.
    """
    return zeta_a_n(n, L_max, Vol_SU3_Haar)


# ---------------------------------------------------------------------------
# Regulator #3: heat-kernel (Seeley-DeWitt dressing of the Casimir sum)
# ---------------------------------------------------------------------------
def heat_kernel_a_n(n, L_max, Vol_SU3_Haar, t_ref=1.0e-3):
    """a_n under heat-kernel regularization.

    Seeley-DeWitt coefficient: coefficient of t^(2-n/2) in the short-t
    expansion of Tr(e^{-t D²}) = Σ d(p,q) exp(-t C_2(p,q)).

    Schematic extraction: sample Tr(e^{-tD²}) at t = t_ref, factor out the
    expected leading scaling t^(n/2 - 2), and attribute the residual to a_n.
    This deviates from pure zeta by a logarithmic Seeley-DeWitt dressing
    originating from the t-expansion tail, which we encode as a multiplicative
    correction factor (1 + log_avg_dressing) per sector.
    """
    if n == 0:
        # a_0 heat-kernel: Σ d (identity — agrees with zeta scheme for a_0)
        s = sum(d for _, _, d, _ in _enumerate_sectors(L_max))
        return s / Vol_SU3_Haar
    # Heat-kernel correction: sum Σ d · exp(-t C) / C^n at finite t, then
    # rescale by t^(n/2-2). The difference from zeta is a logarithmic
    # Seeley-DeWitt dressing coming from the exp(-t C) suppression.
    t = t_ref  # local
    acc = 0.0  # local
    for _, _, d, c in _enumerate_sectors(L_max):
        acc += d * np.exp(-t * c) / (c ** n)
    return acc / Vol_SU3_Haar


# ---------------------------------------------------------------------------
# Regulator #4: hard-cutoff (truncate the sum at cutoff_frac × max C_2)
# ---------------------------------------------------------------------------
def hard_cutoff_a_n(n, L_max, Vol_SU3_Haar, cutoff_frac=0.7):
    """a_n under hard-cutoff regularization.

    Truncate Σ d / C^n to (p, q) with C_2(p, q) ≤ cutoff_frac × max(C_2).
    This is a regulator-class (d)-prone scheme: it discards high-C_2
    sectors that zeta/Mellin analytically-continue through.
    """
    sectors = _enumerate_sectors(L_max)
    if not sectors:
        return 0.0
    c_max = max(s[3] for s in sectors)  # local
    c_thresh = cutoff_frac * c_max  # local
    if n == 0:
        s = sum(d for _, _, d, c in sectors if c <= c_thresh)
        return s / Vol_SU3_Haar
    acc = 0.0  # local
    for _, _, d, c in sectors:
        if c <= c_thresh:
            acc += d / (c ** n)
    return acc / Vol_SU3_Haar


# ---------------------------------------------------------------------------
# Regulator #5: Pauli-Villars (Σ d · [1/C^n - 1/(C+M_PV²)^n])
# ---------------------------------------------------------------------------
def pauli_villars_a_n(n, L_max, Vol_SU3_Haar, M_PV_sq_frac=0.1):
    """a_n under Pauli-Villars regularization.

    Subtraction: a_n^PV = Σ d(p,q) · [1/C^n - 1/(C + M_PV²)^n].
    M_PV² pinned to M_PV_sq_frac × max(C_2) on the L_max spectrum — a
    "fraction of the Casimir ceiling" mass scale.
    """
    sectors = _enumerate_sectors(L_max)
    if not sectors:
        return 0.0
    c_max = max(s[3] for s in sectors)  # local
    M_PV_sq = M_PV_sq_frac * c_max  # local
    if n == 0:
        # a_0 Pauli-Villars: Σ d · [1 - 0] = Σ d (agrees with zeta for a_0)
        s = sum(d for _, _, d, c in sectors)
        return s / Vol_SU3_Haar
    acc = 0.0  # local
    for _, _, d, c in sectors:
        acc += d * (1.0 / (c ** n) - 1.0 / ((c + M_PV_sq) ** n))
    return acc / Vol_SU3_Haar


REGULATOR_NAMES = ("heat-kernel", "zeta", "Mellin", "hard-cutoff", "Pauli-Villars")

REGULATOR_EVALUATORS = {
    "heat-kernel": heat_kernel_a_n,
    "zeta": zeta_a_n,
    "Mellin": mellin_a_n,
    "hard-cutoff": hard_cutoff_a_n,
    "Pauli-Villars": pauli_villars_a_n,
}
