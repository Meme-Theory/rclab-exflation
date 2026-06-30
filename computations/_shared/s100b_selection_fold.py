#!/usr/bin/env python3
"""
s100b_selection_fold — reusable LRD selection-function folding wrapper (S100b W7-1)
===================================================================================

Producing gate: S100b-SELECTION-FUNCTION-FLOOR
Plan: sessions/session-plan/session-100b-plan-w7.md §W7-1 (method, part (a))

THE RINALDI DISCIPLINE (arXiv 2604.07138, JADES GOODS-S/N LRD census):
classic extreme color cuts (F277W-F444W > 1.5 mag; Akins 2025 / Barro 2024)
isolate only <= 25% of the LRD population. Any substrate number-density-vs-z
prediction is testable ONLY against a stated selection function S_i(z);
comparison against a bare selection-convolved LF without folding is an
INVALID TEST. This module is the single reusable implementation of that fold.

CONVENTION: CAPTURE-FRACTION-MULTIPLICATIVE
    n_obs(z) = S(z) * n_int(z)          [fold: intrinsic -> observable]
    n_int(z) = n_obs(z) / S(z)          [unfold: observable -> intrinsic]
with the capture fraction S in (0, 1]. The published Rinaldi floor is
    S_floor = S_capture_floor_LRD_classic = 0.25
and the default selection band is S_band = [S_floor, 1.0] = [0.25, 1.0]
(classic-cut floor .. inclusive unity). Unfolding through the band yields the
intrinsic-abundance band
    [n_obs / S_max, n_obs / S_min] = [n_obs / 1.0, n_obs / 0.25]
                                   = [n_obs, 4 * n_obs],
i.e. the intrinsic band extends UPWARD by the widening factor
    W = 1 / S >= 1 / 0.25 = 4   (= +0.602 dex)
for classic-cut-selected samples (plan §W7-1 substitution chain).

Per-z capture fractions S_i(z): loaded from the Rinaldi extraction where
recoverable; the S100b W7-1 extraction found NO per-z capture table in the
fetched text (declared pin gap, INFO branch), so the band is FLAT at
S_floor = 0.25 across the grid. Downstream consumers (W7-2 C2b, W7-3, any
future demographic gate) call `selection_band` / `unfold` / `load_band_npz`.

Classification: NON-PHONONIC (laboratory-IN survey arithmetic; no substrate
excitation content). Substrate framing: the substrate's post-transit structure
IS the GGE acoustic-excitation interference pattern self-organized through the
a_2^{zeta} channel; what JWST counts is that pattern shadowed through a
color-cut selection capturing <= 25% of the population — the laboratory-IN
shadow is up to 4x (0.602 dex) thinner than the substrate-IS pattern at the
classic-cut floor. Direction of explanation preserved: D_K eigenvalues ->
spectral moments -> emergent assembly -> SELECTION-FOLDED measurement.
"""

from __future__ import annotations

from canonical_constants import S_capture_floor_LRD_classic  # = 0.25 (Rinaldi floor)

import numpy as np

# Default selection band: [classic-cut capture floor, inclusive unity] = [0.25, 1.0]
S_FLOOR_DEFAULT = S_capture_floor_LRD_classic            # 0.25 — canonical import
S_BAND_DEFAULT = (S_FLOOR_DEFAULT, 1.0)


def fold(n_intrinsic, S):
    """Fold an intrinsic abundance through the selection function.

    n_obs(z) = S(z) * n_int(z)   [intrinsic -> observable; multiplicative capture]

    Parameters
    ----------
    n_intrinsic : float or array — intrinsic (substrate-side) abundance(s)
    S : float or array — capture fraction(s), each in (0, 1]

    Returns the observable (selection-convolved) abundance, same shape.
    """
    n_intrinsic = np.asarray(n_intrinsic, dtype=float)
    S = np.asarray(S, dtype=float)
    if np.any(S <= 0.0) or np.any(S > 1.0):
        raise ValueError("capture fraction S must lie in (0, 1]")
    return n_intrinsic * S


def unfold(n_observed, S_band=S_BAND_DEFAULT):
    """Unfold an observed abundance into the intrinsic band.

    Given the selection band S_band = [S_min, S_max] (default [0.25, 1.0]),
    the intrinsic band is
        [n_obs / S_max, n_obs / S_min]
    — lower edge at unity capture, upper edge widened by W = 1/S_min (>= 4
    = +0.602 dex at the Rinaldi classic-cut floor S_min = 0.25).

    Parameters
    ----------
    n_observed : float or array — observed (selection-convolved) abundance(s)
    S_band : (S_min, S_max) tuple with 0 < S_min <= S_max <= 1

    Returns (n_int_lo, n_int_hi) arrays: the intrinsic-abundance band.
    """
    S_min, S_max = float(S_band[0]), float(S_band[1])
    if not (0.0 < S_min <= S_max <= 1.0):
        raise ValueError("require 0 < S_min <= S_max <= 1")
    n_observed = np.asarray(n_observed, dtype=float)
    n_int_lo = n_observed / S_max
    n_int_hi = n_observed / S_min
    return n_int_lo, n_int_hi


def widening_factor(S):
    """Widening factor W = 1/S (>= 4 at the classic-cut floor S = 0.25).

    log10(W) is the upward extension of the intrinsic band in dex
    (log10(4) = 0.602 at the floor).
    """
    S = np.asarray(S, dtype=float)
    if np.any(S <= 0.0) or np.any(S > 1.0):
        raise ValueError("capture fraction S must lie in (0, 1]")
    return 1.0 / S


def selection_band(z_grid, per_z_S=None, S_floor=S_FLOOR_DEFAULT):
    """Per-z selection band [S_lo(z), S_hi(z)] on a redshift grid.

    Per the plan: per-z S_i(z) is loaded from the Rinaldi extraction where
    recoverable; FLAT S_floor (= 0.25) otherwise. The S100b W7-1 extraction
    recovered NO per-z capture table from the fetched text (declared pin
    gap), so the default is the flat bound-form band [0.25, 1.0] at every z.

    Parameters
    ----------
    z_grid : array of redshifts
    per_z_S : optional array, same shape as z_grid — recovered per-z capture
        fractions (each in (0, 1]). None => flat floor.
    S_floor : flat floor used when per_z_S is None (default 0.25, canonical)

    Returns (S_lo, S_hi, W) arrays: band edges and the upward widening
    factor W = 1/S_lo at each z.
    """
    z_grid = np.asarray(z_grid, dtype=float)
    if per_z_S is not None:
        S_lo = np.asarray(per_z_S, dtype=float)
        if S_lo.shape != z_grid.shape:
            raise ValueError("per_z_S must match z_grid shape")
        if np.any(S_lo <= 0.0) or np.any(S_lo > 1.0):
            raise ValueError("per-z capture fractions must lie in (0, 1]")
    else:
        S_lo = np.full_like(z_grid, float(S_floor))
    S_hi = np.ones_like(z_grid)
    W = widening_factor(S_lo)
    return S_lo, S_hi, W


def load_band_npz(npz_path):
    """Load the W7-1 selection-folded band npz for downstream consumption.

    Returns dict with z_grid, S_band_lo, S_band_hi, W_z, extraction_status.
    Downstream gates (W7-2 C2b, W7-3) consume the band arrays — NOT
    capture_wrapper (which is NaN under the bound-form/extraction-limited
    branch and must not be silently propagated).
    """
    d = np.load(npz_path, allow_pickle=False)
    return {
        "z_grid": d["z_grid"],
        "S_band_lo": d["S_band_lo"],
        "S_band_hi": d["S_band_hi"],
        "W_z": d["W_z"],
        "extraction_status": str(d["extraction_status"]),
    }
