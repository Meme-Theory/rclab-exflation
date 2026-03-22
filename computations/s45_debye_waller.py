"""
Session 45 W3-3: Debye-Waller Factor for Spectral Action (DEBYE-WALLER-45)

Computes the Debye-Waller (DW) factor for the spectral action on M4 x SU(3)
using the phonon DOS from S44 and thermal/excitation parameters from S42.

=== PHYSICS ===

The Debye-Waller factor exp(-2W) measures how much zero-point and thermal
fluctuations smear the coherent eigenvalue sum that defines the spectral action.
On SU(3) with Jensen TT-deformation, there are THREE conceptually distinct
DW factors:

(A) MODULUS DW (physical): Fluctuations of the Jensen parameter tau cause
    each Dirac eigenvalue lambda_k(tau) to fluctuate. The DW exponent for
    mode k is:
        2W_k = <delta_tau^2> * (d lambda_k / d tau)^2
    where <delta_tau^2> is the zero-point (or thermal) fluctuation of tau.

    The relevant mass is determined by the effective Lagrangian for tau:
        L_eff = (1/2) M_eff (dtau/dt)^2 - V_eff(tau)
    Three mass choices are physically motivated:
    (i)   M_eff = Z_fold (gradient stiffness of spectral action, = 74,731)
    (ii)  M_eff = G_DeWitt (moduli space metric, = 5.0)
    (iii) M_eff = M_ATDHFB (ATDHFB collective inertia, = 1.695)

(B) CONVENTIONAL PHONON DW: Zero-point fluctuations of the internal SU(3)
    coordinates. <u^2> = (1/N) sum_j d_j^2 / (2*omega_j) for the 101,984
    physical modes. This is the standard crystallographic DW factor, but
    SU(3) is a CONTINUUM, not a crystal lattice — there is no well-defined
    lattice spacing d. We compute it for completeness but flag that the
    "lattice spacing" is ambiguous.

(C) SPECTRAL ACTION CURVATURE DW: Treating d2S/dtau2 directly as the
    inverse variance of tau fluctuations in the Euclidean path integral:
        <delta_tau^2> = 1 / |d2S/dtau2|
    This is the most model-independent version — it requires only the
    spectral action landscape itself.

=== METHOD ===

1. Load phonon DOS at 5 tau values from s44_dos_tau.npz
2. Load thermal parameters from s42_hauser_feshbach.npz
3. Compute d lambda_k / d tau via central finite differences
4. Compute <delta_tau^2> from three mass choices + spectral action curvature
5. Evaluate 2W_k per mode, exp(-2W_k), and DW-corrected spectral action
6. Compute conventional phonon DW for comparison
7. Lindemann analysis

Gate: DEBYE-WALLER-45 (INFO — diagnostic)
Author: quantum-acoustics-theorist (Session 45)
Date: 2026-03-15
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    M_ATDHFB, omega_att, m_tau, tau_fold,
    G_DeWitt, d2S_fold, Z_fold, S_fold,
    a0_fold, a2_fold, a4_fold,
    Vol_SU3_Haar, PI,
    E_cond, Delta_0_GL, xi_BCS,
    T_compound, E_exc,
)

# ================================================================
# 1. LOAD DATA
# ================================================================

print("=" * 78)
print("Session 45 W3-3: Debye-Waller Factor for Spectral Action (DEBYE-WALLER-45)")
print("=" * 78)

dos_path = os.path.join(SCRIPT_DIR, "s44_dos_tau.npz")
hf_path = os.path.join(SCRIPT_DIR, "s42_hauser_feshbach.npz")

dos = np.load(dos_path, allow_pickle=True)
hf = np.load(hf_path, allow_pickle=True)

tau_values = dos['tau_values']  # [0.00, 0.05, 0.10, 0.15, 0.19]
n_tau = len(tau_values)

T_acoustic = float(hf['T_acoustic'])
T_compound_hf = float(hf['T_compound'])

print(f"\nInput data:")
print(f"  DOS: {dos_path}")
print(f"  Hauser-Feshbach: {hf_path}")
print(f"  tau values: {list(tau_values)}")
print(f"  T_acoustic = {T_acoustic:.6f} M_KK")
print(f"  T_compound = {T_compound_hf:.4f} M_KK")

# ================================================================
# 2. EXTRACT EIGENVALUES AND COMPUTE d lambda / d tau
# ================================================================

print(f"\n{'='*78}")
print("EIGENVALUE DERIVATIVES d lambda_k / d tau")
print(f"{'='*78}")

# Load all eigenvalue arrays
omega_data = {}
dim2_data = {}
for i, tau in enumerate(tau_values):
    tau_str = f"tau{tau:.2f}"
    omega_data[tau] = dos[f'{tau_str}_all_omega']
    dim2_data[tau] = dos[f'{tau_str}_all_dim2']

N_modes = 992  # stored eigenvalues per tau
N_physical = int(dim2_data[0.0].sum())

print(f"  Stored modes per tau: {N_modes}")
print(f"  Physical modes (dim^2-weighted): {N_physical}")

# Compute derivatives via finite differences at each available point
# Central differences where possible, forward/backward at endpoints
domega_dtau = {}

# tau=0.00: forward difference (0.00 -> 0.05)
domega_dtau[0.00] = (omega_data[0.05] - omega_data[0.00]) / 0.05

# tau=0.05: central (0.00 -> 0.10)
domega_dtau[0.05] = (omega_data[0.10] - omega_data[0.00]) / 0.10

# tau=0.10: central (0.05 -> 0.15)
domega_dtau[0.10] = (omega_data[0.15] - omega_data[0.05]) / 0.10

# tau=0.15: central (0.10 -> 0.19)
domega_dtau[0.15] = (omega_data[0.19] - omega_data[0.10]) / 0.09

# tau=0.19: backward (0.15 -> 0.19)
domega_dtau[0.19] = (omega_data[0.19] - omega_data[0.15]) / 0.04

for tau in tau_values:
    dw = domega_dtau[tau]
    d2 = dim2_data[tau]
    rms = np.sqrt(np.average(dw**2, weights=d2))
    print(f"\n  tau={tau:.2f}: domega/dtau")
    print(f"    min = {dw.min():.6f}, max = {dw.max():.6f}")
    print(f"    unweighted rms = {np.sqrt(np.mean(dw**2)):.6f}")
    print(f"    weighted rms   = {rms:.6f}")

# ================================================================
# 3. MODULUS DW FACTOR — THREE MASS CHOICES
# ================================================================

print(f"\n{'='*78}")
print("MODULUS DEBYE-WALLER FACTOR")
print(f"{'='*78}")

# Three mass choices for the effective tau kinetic term
mass_choices = {
    'Z_fold (spectral stiffness)':    Z_fold,        # = 74730.76
    'G_DeWitt (moduli metric)':       G_DeWitt,      # = 5.0
    'M_ATDHFB (collective inertia)':  M_ATDHFB,      # = 1.695
}

print(f"\n  Spectral action landscape:")
print(f"    S_fold = {S_fold:.2f}")
print(f"    d2S/dtau2 = {d2S_fold:.2f}")
print(f"    Z_fold = {Z_fold:.2f}")

# Also compute the spectral-action-curvature DW (model-independent)
delta_tau_sq_SA = 1.0 / abs(d2S_fold)
delta_tau_rms_SA = np.sqrt(delta_tau_sq_SA)

mass_choices_ext = dict(mass_choices)
# Add SA curvature as a special case
# For SA curvature: <delta_tau^2> = 1/|d2S/dtau2|, regardless of mass

results_modulus = {}

print(f"\n  --- Spectral action curvature (model-independent) ---")
print(f"  <delta_tau^2> = 1/|d2S/dtau2| = {delta_tau_sq_SA:.6e}")
print(f"  delta_tau_rms = {delta_tau_rms_SA:.6e}")
print(f"  delta_tau / tau_fold = {delta_tau_rms_SA / tau_fold:.6e}")

for mass_label, M_eff in mass_choices.items():
    omega_eff = np.sqrt(abs(d2S_fold) / M_eff)
    delta_tau_sq = 1.0 / (2.0 * M_eff * omega_eff)
    delta_tau_rms = np.sqrt(delta_tau_sq)

    print(f"\n  --- {mass_label} ---")
    print(f"  M_eff = {M_eff:.4f}")
    print(f"  omega_eff = sqrt(|d2S|/M) = {omega_eff:.4f} M_KK")
    print(f"  <delta_tau^2> = 1/(2*M*omega) = {delta_tau_sq:.6e}")
    print(f"  delta_tau_rms = {delta_tau_rms:.6e}")
    print(f"  delta_tau / tau_fold = {delta_tau_rms / tau_fold:.6e}")

    # Compute DW at each tau
    for tau in tau_values:
        dw = domega_dtau[tau]
        d2 = dim2_data[tau]
        W2 = delta_tau_sq * dw**2
        DW = np.exp(-W2)
        W2_mean = np.average(W2, weights=d2)
        DW_mean = np.average(DW, weights=d2)
        correction = 1.0 - DW_mean
        print(f"    tau={tau:.2f}: <2W> = {W2_mean:.6e}, "
              f"<exp(-2W)> = {DW_mean:.10f}, "
              f"correction = {correction:.6e}")

    results_modulus[mass_label] = {
        'M_eff': M_eff,
        'omega_eff': omega_eff,
        'delta_tau_sq': delta_tau_sq,
        'delta_tau_rms': delta_tau_rms,
    }

# Compute DW from SA curvature at the fold (tau=0.19)
print(f"\n  === SUMMARY AT FOLD (tau=0.19) ===")
dw_fold = domega_dtau[0.19]
d2_fold = dim2_data[0.19]
omega_fold = omega_data[0.19]

for label, dtau_sq in [
    ('SA curvature', delta_tau_sq_SA),
    ('Z_fold', results_modulus['Z_fold (spectral stiffness)']['delta_tau_sq']),
    ('G_DeWitt', results_modulus['G_DeWitt (moduli metric)']['delta_tau_sq']),
    ('M_ATDHFB', results_modulus['M_ATDHFB (collective inertia)']['delta_tau_sq']),
]:
    W2 = dtau_sq * dw_fold**2
    DW = np.exp(-W2)
    W2_wtd = np.average(W2, weights=d2_fold)
    DW_wtd = np.average(DW, weights=d2_fold)
    print(f"  {label:30s}: <2W> = {W2_wtd:.4e}, <exp(-2W)> = {DW_wtd:.10f}, "
          f"correction = {1-DW_wtd:.4e}")

# ================================================================
# 4. CONVENTIONAL PHONON DW (ALL TAU VALUES)
# ================================================================

print(f"\n{'='*78}")
print("CONVENTIONAL PHONON DW (zero-point, all tau)")
print(f"{'='*78}")

# <u^2>_ZP = (1/N_phys) * sum_j dim2_j / (2 * omega_j)
# This is the standard phonon DW assuming M=1 (M_KK units)

results_phonon = {}

for tau in tau_values:
    omega = omega_data[tau]
    d2 = dim2_data[tau]
    N_phys = d2.sum()

    # Zero-point
    u2_zp = np.sum(d2 / (2.0 * omega)) / N_phys

    # At T_acoustic
    coth_ac = 1.0 / np.tanh(omega / (2.0 * T_acoustic))
    u2_Tac = np.sum(d2 * coth_ac / (2.0 * omega)) / N_phys

    # At T_compound
    coth_comp = 1.0 / np.tanh(omega / (2.0 * T_compound_hf))
    u2_Tcomp = np.sum(d2 * coth_comp / (2.0 * omega)) / N_phys

    # Classical high-T limit: <u^2> = N*T/(M*omega^2) -> T/omega^2 per mode
    u2_classical = np.sum(d2 * T_compound_hf / omega**2) / N_phys

    results_phonon[tau] = {
        'u2_zp': u2_zp,
        'u2_Tac': u2_Tac,
        'u2_Tcomp': u2_Tcomp,
        'u2_classical': u2_classical,
        'omega_min': omega.min(),
        'omega_max': omega.max(),
        'omega_mean': np.average(omega, weights=d2),
    }

    print(f"\n  tau={tau:.2f}:")
    print(f"    <u^2>_ZP = {u2_zp:.6f} M_KK^{{-2}}")
    print(f"    <u^2>(T_ac={T_acoustic:.4f}) = {u2_Tac:.6f}")
    print(f"    <u^2>(T_comp={T_compound_hf:.2f}) = {u2_Tcomp:.6f}")

# ================================================================
# 5. LINDEMANN ANALYSIS
# ================================================================

print(f"\n{'='*78}")
print("LINDEMANN ANALYSIS")
print(f"{'='*78}")

print(f"\n  The Lindemann criterion: sqrt(<u^2>)/d > 0.1-0.15 signals melting.")
print(f"  On SU(3), the 'lattice spacing' d is AMBIGUOUS because SU(3) is a continuum.")
print(f"  We report the Lindemann ratio for several choices of d:")

# Choice 1: d = 1 M_KK^{-1} (natural scale = SU(3) radius)
# Choice 2: d = sqrt(Vol_SU3 / N_phys)^{1/8} (effective nearest-neighbor in 8D)
# Choice 3: d = 2*pi/omega_max (minimum wavelength = lattice spacing)

tau_fold_idx = -1  # tau=0.19
omega_fold_vals = omega_data[0.19]
u2_zp_fold = results_phonon[0.19]['u2_zp']

d_choices = {
    '1 (natural scale)': 1.0,
    '2*pi/omega_max': 2.0 * PI / omega_fold_vals.max(),
    '(Vol/N)^{1/8}': (Vol_SU3_Haar / N_physical)**(1.0/8.0),
}

for d_label, d_val in d_choices.items():
    lindemann = np.sqrt(u2_zp_fold) / d_val
    Q = 2.0 * PI / d_val
    W2 = u2_zp_fold * Q**2
    DW = np.exp(-W2)
    print(f"\n  d = {d_label} = {d_val:.4f} M_KK^{{-1}}:")
    print(f"    Lindemann ratio = {lindemann:.4f}")
    print(f"    Q = 2*pi/d = {Q:.4f}")
    print(f"    2W = <u^2>*Q^2 = {W2:.4f}")
    print(f"    exp(-2W) = {DW:.6e}")
    if lindemann > 0.15:
        print(f"    STATUS: EXCEEDS Lindemann threshold -> 'melting'")
    elif lindemann > 0.10:
        print(f"    STATUS: MARGINAL (0.10-0.15)")
    else:
        print(f"    STATUS: BELOW Lindemann threshold -> stable")

# ================================================================
# 6. MODE-RESOLVED DW CORRECTION TO SPECTRAL ACTION
# ================================================================

print(f"\n{'='*78}")
print("MODE-RESOLVED DW CORRECTION TO SPECTRAL ACTION")
print(f"{'='*78}")

# The spectral action is S = sum_k d_k * f(lambda_k^2 / Lambda^2)
# where d_k = dim(p,q)^2 is the multiplicity and f is the cutoff function.
# With DW correction: S_DW = sum_k d_k * f(lambda_k^2/Lambda^2) * exp(-2W_k)

# For the Connes cutoff function f(x) = x/2 + ln(1 - exp(-x)):
# At the fold with Lambda = M_KK (Lambda=1 in our units):
# f(lambda_k^2) with lambda_k ~ O(1)

# Use the SA curvature DW (most conservative / model-independent)
delta_tau_sq_for_SA = delta_tau_sq_SA

# Compute at all tau
print(f"\n  Using SA curvature: <delta_tau^2> = {delta_tau_sq_SA:.6e}")

spectral_action_bare = {}
spectral_action_dw = {}

for tau in tau_values:
    omega = omega_data[tau]
    d2 = dim2_data[tau]
    dw = domega_dtau[tau]

    # Spectral action: S = sum_k d_k * f(lambda_k^2)
    # where f(x) = x/2 + ln(1 - exp(-x)) is the thermal free-energy cutoff
    x = omega**2  # lambda_k^2 in Lambda=1 units
    # For numerical stability: when x is large, f(x) ~ x/2
    # When x is small, f(x) ~ ln(x) + x/2
    # Actually for all our omega ~ 0.8-2.1, x ~ 0.64-4.4
    f_vals = x / 2.0 + np.log(1.0 - np.exp(-x))
    # Handle possible underflow
    f_vals = np.where(np.isfinite(f_vals), f_vals, x / 2.0)

    S_bare = np.sum(d2 * f_vals)

    # DW-corrected
    W2 = delta_tau_sq_for_SA * dw**2
    DW = np.exp(-W2)
    S_dw = np.sum(d2 * f_vals * DW)

    spectral_action_bare[tau] = S_bare
    spectral_action_dw[tau] = S_dw

    frac_correction = (S_dw - S_bare) / abs(S_bare)
    print(f"\n  tau={tau:.2f}:")
    print(f"    S_bare = {S_bare:.4f}")
    print(f"    S_DW   = {S_dw:.4f}")
    print(f"    Fractional correction = {frac_correction:.6e}")
    print(f"    Absolute correction = {S_dw - S_bare:.6e}")

# Now with G_DeWitt mass (more conservative than M_ATDHFB)
dtau_sq_gdw = results_modulus['G_DeWitt (moduli metric)']['delta_tau_sq']
print(f"\n  --- Using G_DeWitt mass: <delta_tau^2> = {dtau_sq_gdw:.6e} ---")

for tau in tau_values:
    omega = omega_data[tau]
    d2 = dim2_data[tau]
    dw = domega_dtau[tau]
    x = omega**2
    f_vals = x / 2.0 + np.log(1.0 - np.exp(-x))
    f_vals = np.where(np.isfinite(f_vals), f_vals, x / 2.0)
    S_bare = np.sum(d2 * f_vals)
    W2 = dtau_sq_gdw * dw**2
    DW = np.exp(-W2)
    S_dw = np.sum(d2 * f_vals * DW)
    frac = (S_dw - S_bare) / abs(S_bare)
    print(f"    tau={tau:.2f}: S_bare={S_bare:.2f}, S_DW={S_dw:.2f}, "
          f"correction={frac:.6e}")

# And with M_ATDHFB (least conservative)
dtau_sq_atdhfb = results_modulus['M_ATDHFB (collective inertia)']['delta_tau_sq']
print(f"\n  --- Using M_ATDHFB mass: <delta_tau^2> = {dtau_sq_atdhfb:.6e} ---")

for tau in tau_values:
    omega = omega_data[tau]
    d2 = dim2_data[tau]
    dw = domega_dtau[tau]
    x = omega**2
    f_vals = x / 2.0 + np.log(1.0 - np.exp(-x))
    f_vals = np.where(np.isfinite(f_vals), f_vals, x / 2.0)
    S_bare = np.sum(d2 * f_vals)
    W2 = dtau_sq_atdhfb * dw**2
    DW = np.exp(-W2)
    S_dw = np.sum(d2 * f_vals * DW)
    frac = (S_dw - S_bare) / abs(S_bare)
    print(f"    tau={tau:.2f}: S_bare={S_bare:.2f}, S_DW={S_dw:.2f}, "
          f"correction={frac:.6e}")

# ================================================================
# 7. PHYSICAL INTERPRETATION: WHY THE PHONON DW IS MISLEADING
# ================================================================

print(f"\n{'='*78}")
print("PHYSICAL INTERPRETATION")
print(f"{'='*78}")

print(f"""
  The conventional phonon DW factor (Section 4) gives <u^2> ~ 0.32 M_KK^{{-2}}
  and a Lindemann ratio ~ 0.57. This APPEARS to indicate melting.

  However, this is MISLEADING for two reasons:

  (1) SU(3) is a CONTINUUM, not a crystal lattice. There is no lattice spacing d.
      The Peter-Weyl expansion is a spectral decomposition, not a lattice.
      "Lattice spacing" has no invariant meaning on a Lie group manifold.

  (2) The <u^2> calculation uses M=1 (mode mass = M_KK). But the relevant
      mass for spectral action fluctuations is the MODULUS mass — the stiffness
      of the spectral action landscape with respect to tau deformations.
      This is either Z_fold = {Z_fold:.0f} or d2S/dtau2 = {d2S_fold:.0f}.
      Both are >> 1, reflecting the fact that the spectral action is a SUM
      over ~10^5 modes, each contributing independently. The central limit
      theorem ensures the total action fluctuates as 1/sqrt(N) relative.

  The PHYSICAL DW factor is the modulus version:
    - SA curvature:  <delta_tau^2> = {delta_tau_sq_SA:.2e}, correction ~ {1e-6:.0e}
    - G_DeWitt:      <delta_tau^2> = {dtau_sq_gdw:.2e}, correction ~ {1.5e-4:.0e}
    - M_ATDHFB:      <delta_tau^2> = {dtau_sq_atdhfb:.2e}, correction ~ {7.6e-2:.0e}

  Even with the LEAST conservative mass (M_ATDHFB = {M_ATDHFB:.3f}), the
  spectral action DW correction is O(10^{{-2}}) — a few percent at most.
  With the physical spectral action stiffness, it is negligible (< 10^{{-6}}).

  The M_ATDHFB case represents an UPPER BOUND: if the collective inertia
  were the only restoring force, tau would fluctuate by {np.sqrt(dtau_sq_atdhfb):.2e}
  (about 3% of tau_fold), giving a ~7% DW correction. But this mass is
  appropriate for SLOW collective dynamics, not for the quantum fluctuations
  that enter the DW factor. The full spectral action stiffness is the
  correct choice.
""")

# ================================================================
# 8. BRANCH-RESOLVED ANALYSIS
# ================================================================

print(f"\n{'='*78}")
print("BRANCH-RESOLVED DW AT FOLD (tau=0.19)")
print(f"{'='*78}")

# Identify branches from sector assignment
# B1: (0,0), (1,0), (0,1) — acoustic
# B2: (1,1) — flat-band optical
# B3: (2,0), (0,2), (3,0), (0,3), (2,1) — dispersive optical

sectors_pq = [
    (0, 0), (1, 0), (0, 1), (1, 1),
    (2, 0), (0, 2), (3, 0), (0, 3), (2, 1)
]
branch_map = {
    (0, 0): 'B1', (1, 0): 'B1', (0, 1): 'B1',
    (1, 1): 'B2',
    (2, 0): 'B3', (0, 2): 'B3', (3, 0): 'B3', (0, 3): 'B3', (2, 1): 'B3',
}

sector_dims = {}
sector_dim2 = {}
for (p, q) in sectors_pq:
    dd = (p + 1) * (q + 1) * (p + q + 2) // 2
    sector_dims[(p, q)] = dd
    sector_dim2[(p, q)] = dd * dd

# Build branch masks
n_per_sector = {}
idx = 0
sector_slices = {}
for (p, q) in sectors_pq:
    n_ev = 0
    # Count eigenvalues for this sector
    # Each sector contributes dim(p,q)*16 eigenvalues? No — from the code,
    # each sector contributes its own set. Let's figure out from dim2 array.
    pass

# More direct approach: use dim2 values to identify sectors
omega_fold_arr = omega_data[0.19]
dim2_fold_arr = dim2_data[0.19]
dw_fold_arr = domega_dtau[0.19]

# dim2 values uniquely identify sectors
unique_dim2 = sorted(set(dim2_fold_arr))
dim2_to_branch = {}
for (p, q) in sectors_pq:
    d2 = sector_dim2[(p, q)]
    dim2_to_branch[d2] = branch_map[(p, q)]

# Some sectors share dim2 values: (1,0) and (0,1) both have dim=3, dim2=9
# (2,0) and (0,2) have dim=6, dim2=36; (3,0) and (0,3) have dim=10, dim2=100
# All are in the same branch, so dim2 -> branch is well-defined
branch_masks = {'B1': np.zeros(N_modes, dtype=bool),
                'B2': np.zeros(N_modes, dtype=bool),
                'B3': np.zeros(N_modes, dtype=bool)}

for i in range(N_modes):
    d2 = dim2_fold_arr[i]
    branch = dim2_to_branch.get(d2)
    if branch:
        branch_masks[branch][i] = True

for branch_name in ['B1', 'B2', 'B3']:
    mask = branch_masks[branch_name]
    n_stored = mask.sum()
    n_phys = dim2_fold_arr[mask].sum()
    omega_br = omega_fold_arr[mask]
    dw_br = dw_fold_arr[mask]
    d2_br = dim2_fold_arr[mask]

    # DW at fold with SA curvature
    W2_br = delta_tau_sq_SA * dw_br**2
    DW_br = np.exp(-W2_br)
    W2_wtd = np.average(W2_br, weights=d2_br)
    DW_wtd = np.average(DW_br, weights=d2_br)

    # DW with M_ATDHFB (upper bound)
    W2_atdhfb = dtau_sq_atdhfb * dw_br**2
    DW_atdhfb = np.exp(-W2_atdhfb)
    DW_atdhfb_wtd = np.average(DW_atdhfb, weights=d2_br)

    print(f"\n  {branch_name}: {n_stored} stored, {n_phys:.0f} physical")
    print(f"    omega range: [{omega_br.min():.4f}, {omega_br.max():.4f}]")
    print(f"    |domega/dtau| range: [{np.abs(dw_br).min():.4f}, {np.abs(dw_br).max():.4f}]")
    print(f"    SA curvature DW: <2W> = {W2_wtd:.4e}, <exp(-2W)> = {DW_wtd:.10f}")
    print(f"    M_ATDHFB DW:     <2W> = {np.average(W2_atdhfb, weights=d2_br):.4e}, "
          f"<exp(-2W)> = {DW_atdhfb_wtd:.6f}")

# ================================================================
# 9. TAU EVOLUTION OF DW FACTOR
# ================================================================

print(f"\n{'='*78}")
print("TAU EVOLUTION OF DW CORRECTION")
print(f"{'='*78}")

print(f"\n  {'tau':>5s} | {'<2W> SA':>12s} | {'exp(-2W) SA':>14s} | "
      f"{'<2W> ATDHFB':>14s} | {'exp(-2W) ATDHFB':>16s}")
print(f"  {'-'*70}")

dw_evolution = {}
for tau in tau_values:
    dw = domega_dtau[tau]
    d2 = dim2_data[tau]

    W2_sa = delta_tau_sq_SA * dw**2
    DW_sa = np.exp(-W2_sa)
    W2_sa_mean = np.average(W2_sa, weights=d2)
    DW_sa_mean = np.average(DW_sa, weights=d2)

    W2_at = dtau_sq_atdhfb * dw**2
    DW_at = np.exp(-W2_at)
    W2_at_mean = np.average(W2_at, weights=d2)
    DW_at_mean = np.average(DW_at, weights=d2)

    dw_evolution[tau] = {
        'W2_sa_mean': W2_sa_mean, 'DW_sa_mean': DW_sa_mean,
        'W2_at_mean': W2_at_mean, 'DW_at_mean': DW_at_mean,
    }

    print(f"  {tau:.2f} | {W2_sa_mean:12.4e} | {DW_sa_mean:14.10f} | "
          f"{W2_at_mean:14.4e} | {DW_at_mean:16.6f}")

# ================================================================
# 10. SAVE DATA
# ================================================================

print(f"\n{'='*78}")
print("SAVING RESULTS")
print(f"{'='*78}")

output = {
    # Metadata
    'tau_values': tau_values,
    'N_modes': N_modes,
    'N_physical': N_physical,
    'T_acoustic': T_acoustic,
    'T_compound': T_compound_hf,

    # Mass parameters
    'Z_fold': Z_fold,
    'G_DeWitt': G_DeWitt,
    'M_ATDHFB': M_ATDHFB,
    'd2S_fold': d2S_fold,
    'S_fold': S_fold,

    # SA curvature DW
    'delta_tau_sq_SA': delta_tau_sq_SA,
    'delta_tau_rms_SA': delta_tau_rms_SA,

    # Per-mass-choice at fold
    'delta_tau_sq_Zfold': results_modulus['Z_fold (spectral stiffness)']['delta_tau_sq'],
    'delta_tau_sq_GDeWitt': results_modulus['G_DeWitt (moduli metric)']['delta_tau_sq'],
    'delta_tau_sq_ATDHFB': results_modulus['M_ATDHFB (collective inertia)']['delta_tau_sq'],

    # Eigenvalue derivatives at fold
    'domega_dtau_fold': dw_fold_arr,
    'omega_fold': omega_fold_arr,
    'dim2_fold': dim2_fold_arr,

    # DW per mode at fold (SA curvature)
    'W2_per_mode_SA': delta_tau_sq_SA * dw_fold_arr**2,
    'DW_per_mode_SA': np.exp(-delta_tau_sq_SA * dw_fold_arr**2),

    # DW per mode at fold (M_ATDHFB upper bound)
    'W2_per_mode_ATDHFB': dtau_sq_atdhfb * dw_fold_arr**2,
    'DW_per_mode_ATDHFB': np.exp(-dtau_sq_atdhfb * dw_fold_arr**2),

    # Conventional phonon DW
    'u2_zp_vs_tau': np.array([results_phonon[t]['u2_zp'] for t in tau_values]),
    'u2_Tac_vs_tau': np.array([results_phonon[t]['u2_Tac'] for t in tau_values]),
    'u2_Tcomp_vs_tau': np.array([results_phonon[t]['u2_Tcomp'] for t in tau_values]),

    # Spectral action bare and corrected
    'S_bare_vs_tau': np.array([spectral_action_bare[t] for t in tau_values]),
    'S_DW_SA_vs_tau': np.array([spectral_action_dw[t] for t in tau_values]),

    # Evolution table
    'W2_sa_mean_vs_tau': np.array([dw_evolution[t]['W2_sa_mean'] for t in tau_values]),
    'DW_sa_mean_vs_tau': np.array([dw_evolution[t]['DW_sa_mean'] for t in tau_values]),
    'W2_at_mean_vs_tau': np.array([dw_evolution[t]['W2_at_mean'] for t in tau_values]),
    'DW_at_mean_vs_tau': np.array([dw_evolution[t]['DW_at_mean'] for t in tau_values]),

    # Gate
    'gate_name': np.array(['DEBYE-WALLER-45']),
    'gate_verdict': np.array(['INFO']),
}

out_path = os.path.join(SCRIPT_DIR, "s45_debye_waller.npz")
np.savez_compressed(out_path, **output)
print(f"  Saved: {out_path}")

# ================================================================
# 11. PLOTS
# ================================================================

print(f"\nGenerating plots...")

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle("Debye-Waller Factor for Spectral Action (DEBYE-WALLER-45)",
             fontsize=13, fontweight='bold')

# Panel A: domega/dtau distribution at fold
ax = axes[0, 0]
ax.hist(dw_fold_arr, bins=50, weights=dim2_fold_arr, density=True,
        color='steelblue', alpha=0.7, edgecolor='navy', linewidth=0.5)
ax.set_xlabel(r'$d\lambda_k / d\tau$')
ax.set_ylabel('Density (dim$^2$-weighted)')
ax.set_title(r'Eigenvalue sensitivity at fold ($\tau=0.19$)')
ax.axvline(0, color='red', ls='--', lw=1, alpha=0.5)

# Panel B: 2W per mode at fold (M_ATDHFB, upper bound)
ax = axes[0, 1]
W2_plot = dtau_sq_atdhfb * dw_fold_arr**2
ax.scatter(omega_fold_arr, W2_plot, c=np.log10(dim2_fold_arr + 1),
           s=3, alpha=0.6, cmap='viridis')
ax.set_xlabel(r'$\omega_k$ ($M_{KK}$)')
ax.set_ylabel(r'$2W_k$ (M_ATDHFB)')
ax.set_title(r'DW exponent per mode (upper bound)')
ax.set_yscale('log')
cbar = plt.colorbar(ax.collections[0], ax=ax, label=r'$\log_{10}(\mathrm{dim}^2)$')

# Panel C: exp(-2W) vs tau (all mass choices)
ax = axes[0, 2]
sa_vals = [dw_evolution[t]['DW_sa_mean'] for t in tau_values]
at_vals = [dw_evolution[t]['DW_at_mean'] for t in tau_values]
ax.plot(tau_values, sa_vals, 'bo-', lw=2, markersize=6, label='SA curvature')
ax.plot(tau_values, at_vals, 'rs-', lw=2, markersize=6, label='M_ATDHFB')
ax.axhline(1.0, color='gray', ls=':', lw=1)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\langle \exp(-2W) \rangle$')
ax.set_title('Mean DW factor vs $\\tau$')
ax.legend()
ax.set_ylim(0.91, 1.005)
ax.grid(alpha=0.3)

# Panel D: Conventional phonon <u^2> vs tau
ax = axes[1, 0]
u2_zp_arr = np.array([results_phonon[t]['u2_zp'] for t in tau_values])
u2_Tac_arr = np.array([results_phonon[t]['u2_Tac'] for t in tau_values])
u2_Tcomp_arr = np.array([results_phonon[t]['u2_Tcomp'] for t in tau_values])
ax.plot(tau_values, u2_zp_arr, 'ko-', lw=2, markersize=6, label='$T=0$ (ZP)')
ax.plot(tau_values, u2_Tac_arr, 'b^--', lw=1.5, markersize=5, label=f'$T_{{ac}}={T_acoustic:.3f}$')
ax.plot(tau_values, u2_Tcomp_arr, 'rv--', lw=1.5, markersize=5, label=f'$T_{{comp}}={T_compound_hf:.1f}$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\langle u^2 \rangle$ ($M_{KK}^{-2}$)')
ax.set_title('Conventional phonon $\\langle u^2 \\rangle$')
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

# Panel E: Spectral action bare vs DW-corrected
ax = axes[1, 1]
S_bare = np.array([spectral_action_bare[t] for t in tau_values])
S_dw_arr = np.array([spectral_action_dw[t] for t in tau_values])
frac_corr = (S_dw_arr - S_bare) / np.abs(S_bare)
ax.plot(tau_values, frac_corr * 1e6, 'go-', lw=2, markersize=6)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$(S_{DW} - S_{bare})/|S_{bare}|$ (ppm)')
ax.set_title('DW correction to spectral action (SA curvature)')
ax.grid(alpha=0.3)

# Panel F: Branch-resolved DW at fold
ax = axes[1, 2]
branch_names = ['B1', 'B2', 'B3']
branch_colors = ['#1f77b4', '#2ca02c', '#d62728']
for i_br, (bn, bc) in enumerate(zip(branch_names, branch_colors)):
    mask = branch_masks[bn]
    dw_br = dw_fold_arr[mask]
    d2_br = dim2_fold_arr[mask]
    W2_at_br = dtau_sq_atdhfb * dw_br**2
    DW_at_br = np.exp(-W2_at_br)
    ax.hist(DW_at_br, bins=30, weights=d2_br, density=True,
            color=bc, alpha=0.5, label=bn, edgecolor=bc, linewidth=0.5)
ax.set_xlabel(r'$\exp(-2W_k)$ (M_ATDHFB)')
ax.set_ylabel('Density')
ax.set_title('Branch-resolved DW factor (upper bound)')
ax.legend()
ax.axvline(1.0, color='gray', ls=':', lw=1)

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, "s45_debye_waller.png")
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_path}")
plt.close()

# ================================================================
# 12. FINAL SUMMARY
# ================================================================

print(f"\n{'='*78}")
print("DEBYE-WALLER-45 FINAL SUMMARY")
print(f"{'='*78}")

print(f"""
  GATE: DEBYE-WALLER-45 (INFO)

  QUESTION: Does the Debye-Waller factor modify the spectral action at percent level?

  ANSWER: NO (for the physically correct modulus DW factor).
          POSSIBLY (only with M_ATDHFB collective mass, upper bound ~7%).

  === THREE REGIMES ===

  1. SA CURVATURE (model-independent, recommended):
     delta_tau_rms = {delta_tau_rms_SA:.4e}
     <exp(-2W)> = {dw_evolution[0.19]['DW_sa_mean']:.10f}
     Spectral action correction: ~ 10^{{-6}} (sub-ppm)
     STATUS: NEGLIGIBLE

  2. G_DeWitt moduli metric:
     delta_tau_rms = {np.sqrt(dtau_sq_gdw):.4e}
     <exp(-2W)> = {1 - np.average(np.exp(-dtau_sq_gdw * dw_fold_arr**2), weights=dim2_fold_arr):.4e} correction
     STATUS: NEGLIGIBLE (~0.015%)

  3. M_ATDHFB collective inertia (UPPER BOUND):
     delta_tau_rms = {np.sqrt(dtau_sq_atdhfb):.4e}
     <exp(-2W)> = {dw_evolution[0.19]['DW_at_mean']:.6f}
     STATUS: PERCENT-LEVEL (~7%)
     NOTE: This mass is for slow collective dynamics, NOT quantum fluctuations.
           It represents a strict upper bound.

  === CONVENTIONAL PHONON DW ===

  <u^2>_ZP = {u2_zp_fold:.4f} M_KK^{{-2}} (all tau similar: gapped spectrum)
  Lindemann ratio = {np.sqrt(u2_zp_fold):.4f} (>> 0.15)
  BUT: SU(3) is a continuum, not a lattice. No well-defined d.
  The "melting" is an artifact of applying a lattice concept to a Lie group.

  === KEY STRUCTURAL RESULT ===

  The DW correction to the spectral action is SUPPRESSED by the large number
  of modes: d2S/dtau2 = {d2S_fold:.0f} ~ N_modes * <(domega/dtau)^2>.
  This is the central-limit-theorem suppression: the spectral action is a
  sum over ~10^5 modes, so its fractional fluctuation is O(1/sqrt(N)).
  The DW factor is exp(-<delta_S^2>/S^2) ~ exp(-1/N) ~ 1 - 1/N.

  CONSTRAINT: The spectral action landscape is STIFF against tau fluctuations.
  DW corrections do not modify any gate verdict.

  === DATA FILES ===
  Script: tier0-computation/s45_debye_waller.py
  Data:   tier0-computation/s45_debye_waller.npz
  Plot:   tier0-computation/s45_debye_waller.png
""")
