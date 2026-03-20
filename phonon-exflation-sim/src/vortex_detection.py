"""
Vortex detection via plaquette circulation method.

For each plaquette (elementary square on the grid), compute the
accumulated phase around the loop. A vortex exists at the plaquette
center if the total circulation is +/- 2pi.

Gamma_plaquette = sum of [arg(psi_{i+1}) - arg(psi_i)] around loop
Vortex if |Gamma| ~ 2pi. Sign gives topological charge +/- 1.

Phase 2: KD-tree acceleration for pairing + soft pairing mode.
"""

import numpy as np
from scipy.spatial import cKDTree
from src.backend import xp, to_numpy, as_int


def detect_vortices(psi):
    """Detect vortices using plaquette circulation method.

    Works on GPU arrays; returns CPU-side positions.

    Returns:
        vortex_positions: list of (row, col, charge) tuples
        charge_field: 2D NumPy array of winding numbers at each plaquette
    """
    phase = xp.angle(psi)

    # Phase differences along x and y, wrapped to [-pi, pi]
    dx_phase = xp.angle(xp.exp(1j * (xp.roll(phase, -1, axis=1) - phase)))
    dy_phase = xp.angle(xp.exp(1j * (xp.roll(phase, -1, axis=0) - phase)))

    # Circulation around each plaquette (counterclockwise)
    circulation = (
        dx_phase
        + xp.roll(dy_phase, -1, axis=1)
        - xp.roll(dx_phase, -1, axis=0)
        - dy_phase
    )

    # Winding number
    winding = as_int(xp.round(circulation / (2 * np.pi)))

    # Transfer to CPU for position extraction
    winding_np = to_numpy(winding)

    vortex_positions = []
    vy, vx = np.where(winding_np != 0)
    for y, x in zip(vy, vx):
        vortex_positions.append((y, x, int(winding_np[y, x])))

    return vortex_positions, winding_np


def separate_by_charge(vortex_positions):
    """Separate vortices into positive and negative charge lists."""
    positive = [(y, x) for y, x, c in vortex_positions if c > 0]
    negative = [(y, x) for y, x, c in vortex_positions if c < 0]
    return positive, negative


def identify_pairs(vortex_positions, d_cut, L=None, soft_pairing=False,
                   n0=1.0, xi=1.0, H=0.0):
    """Identify bound vortex-antivortex pairs via mutual nearest-neighbor.

    Uses scipy.spatial.cKDTree for O(n log n) scaling with periodic BC.

    Args:
        vortex_positions: list of (row, col, charge)
        d_cut: maximum pairing distance (in grid units)
        L: box size for periodic boundary conditions (in grid units)
        soft_pairing: if True, return continuous weights instead of binary pairing
        n0: background density (for soft pairing binding energy)
        xi: healing length in grid units (for soft pairing)
        H: Hubble rate (for soft pairing kinetic energy)

    Returns:
        pairs: list of ((y1,x1), (y2,x2)) paired positions
        free_positive: list of unpaired positive positions
        free_negative: list of unpaired negative positions
        If soft_pairing: also returns pair_weights (list of floats in [0,1])
    """
    positive, negative = separate_by_charge(vortex_positions)

    if len(positive) == 0 or len(negative) == 0:
        if soft_pairing:
            return [], positive, negative, []
        return [], positive, negative

    pos_arr = np.array(positive, dtype=float)
    neg_arr = np.array(negative, dtype=float)

    # Build KD-trees with periodic BC
    boxsize = [float(L), float(L)] if L is not None else None
    pos_tree = cKDTree(pos_arr, boxsize=boxsize)
    neg_tree = cKDTree(neg_arr, boxsize=boxsize)

    # For each positive vortex, find nearest negative
    dist_pos_to_neg, idx_pos_to_neg = neg_tree.query(pos_arr, k=1)
    # For each negative vortex, find nearest positive
    dist_neg_to_pos, idx_neg_to_pos = pos_tree.query(neg_arr, k=1)

    # Mutual nearest neighbors within d_cut
    pairs = []
    pair_weights = []
    paired_pos = set()
    paired_neg = set()

    for i in range(len(pos_arr)):
        j = idx_pos_to_neg[i]
        dist_ij = dist_pos_to_neg[i]

        if dist_ij < d_cut:
            # Check mutual: is pos[i] also nearest positive for neg[j]?
            if idx_neg_to_pos[j] == i:
                pairs.append((positive[i], negative[j]))
                paired_pos.add(i)
                paired_neg.add(j)

                if soft_pairing:
                    # Binding energy: E_bind = pi * n0 * ln(d / xi)
                    # Negative when d < xi (cores overlap -> not a resolved pair)
                    d = max(dist_ij, 0.5)  # regularize at short range
                    xi_eff = max(xi, 0.5)
                    E_bind = np.pi * n0 * np.log(d / xi_eff)
                    # Expansion kinetic energy: E_kin = 0.5 * (H * d)^2
                    E_kin = 0.5 * (H * d) ** 2
                    # Sigmoid weight: 1 = fully bound, 0 = fully free
                    dE = E_bind - E_kin
                    weight = 1.0 / (1.0 + np.exp(-dE)) if abs(dE) < 50 else (1.0 if dE > 0 else 0.0)
                    pair_weights.append(weight)

    free_positive = [positive[i] for i in range(len(positive)) if i not in paired_pos]
    free_negative = [negative[j] for j in range(len(negative)) if j not in paired_neg]

    if soft_pairing:
        return pairs, free_positive, free_negative, pair_weights
    return pairs, free_positive, free_negative
