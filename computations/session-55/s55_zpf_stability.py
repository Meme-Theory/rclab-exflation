"""
S55 W0-4: ZPF-STABILITY-55 — Zero-Point Fluctuation Stability of S_occ Minimum

Test whether zero-point fluctuations of the modulus field destabilize the
S_occ minimum. The resonance question: does the ground-state vibration of
the tau modulus fit inside the potential well, or does it slosh over the barrier?

Method:
  1. Load S_occ(tau) at Sharp cutoff from s54_sa_latt_occ.npz
  2. Compute S_occ'' at the minimum via finite differences
  3. omega_0 = sqrt(S_occ'' / M_eff) with M_eff = G_DeWitt = 5.0
  4. delta_tau_0 = 1 / sqrt(2 * M_eff * omega_0)  (ZPF amplitude)
  5. Estimate barrier width from S_occ curve
  6. Compare delta_tau_0 to barrier width
  7. Compare omega_0 to Leggett mode omega_L1 = 0.070 M_KK

Author: Tesla-Resonance
Session: S55, Wave 0
"""

import numpy as np
import sys
sys.path.insert(0, 'computations')

# ── Load data ──────────────────────────────────────────────────────────
data = np.load('computations/session-54/s54_sa_latt_occ.npz', allow_pickle=True)

tau = data['tau_values']          # (50,)
Lambda_vals = data['Lambda_values']  # [1., 2., 5.]
cutoff_names = data['cutoff_names']  # ['Exponential', 'Sharp', 'Polynomial']
has_min = data['has_minimum']     # (3, 3)
min_locs = data['minimum_locations']  # (3, 3)
barrier_h = data['barrier_heights']   # (3, 3)
min_vals = data['minimum_values']     # (3, 3)
S_occ_all = data['S_occ']            # (3, 3, 50)
Delta_primary = float(data['Delta_primary'])

dtau = tau[1] - tau[0]  # uniform grid spacing

print("=" * 70)
print("ZPF-STABILITY-55: Zero-Point Fluctuation Stability Analysis")
print("=" * 70)

# ── Identify the target: Sharp cutoff (index=1), occ_type=0 ───────────
# This is the strongest minimum (barrier = 0.0535)
icut = 1   # Sharp cutoff
iocc = 0   # occupation type 0

print(f"\nCutoff: {cutoff_names[icut]} (Lambda = {Lambda_vals[icut]})")
print(f"Occupation type: {iocc}")
print(f"Has minimum: {has_min[icut, iocc]}")
print(f"Minimum location (pre-computed): tau = {min_locs[icut, iocc]:.6f}")
print(f"Minimum value: S_occ = {min_vals[icut, iocc]:.8f}")
print(f"Barrier height (pre-computed): {barrier_h[icut, iocc]:.6f}")
print(f"Delta_primary (BCS gap): {Delta_primary:.6f}")

S = S_occ_all[icut, iocc, :]  # the S_occ curve

# ── Step 1: Locate minimum precisely ──────────────────────────────────
# Find the grid index of the minimum in the fold region [0.10, 0.30]
mask = (tau >= 0.10) & (tau <= 0.30)
idx_search = np.where(mask)[0]
i_min = idx_search[np.argmin(S[idx_search])]

tau_min = tau[i_min]
S_min = S[i_min]
print(f"\nGrid minimum: index={i_min}, tau={tau_min:.6f}, S_occ={S_min:.10f}")

# ── Step 2: Compute S_occ'' at the minimum ────────────────────────────
# Central finite difference: f''(x) = (f(x+h) - 2f(x) + f(x-h)) / h^2
# Need to handle the sharp jump at i=20 carefully

# Standard second derivative at the minimum
S_pp_center = (S[i_min + 1] - 2 * S[i_min] + S[i_min - 1]) / dtau**2

print(f"\n── Second Derivative at Minimum ──")
print(f"S(tau_min - h) = S[{i_min-1}] = {S[i_min-1]:.10f}")
print(f"S(tau_min)     = S[{i_min}]   = {S[i_min]:.10f}")
print(f"S(tau_min + h) = S[{i_min+1}] = {S[i_min+1]:.10f}")
print(f"h = dtau = {dtau:.8f}")
print(f"S_occ'' (central) = {S_pp_center:.6f}")

# Also compute via 5-point stencil for comparison
if i_min >= 2 and i_min <= len(tau) - 3:
    S_pp_5pt = (-S[i_min+2] + 16*S[i_min+1] - 30*S[i_min] + 16*S[i_min-1] - S[i_min-2]) / (12 * dtau**2)
    print(f"S_occ'' (5-point) = {S_pp_5pt:.6f}")
else:
    S_pp_5pt = S_pp_center

# Use central difference as the primary value (most robust at grid minimum)
S_pp = S_pp_center

# Sanity check: S_pp should be positive at a minimum
if S_pp <= 0:
    print(f"WARNING: S_occ'' = {S_pp:.6f} <= 0. Not a proper minimum on this grid.")
    # Try using only the LEFT side (smooth descent)
    # Left-side second derivative
    S_pp_left = (S[i_min] - 2*S[i_min-1] + S[i_min-2]) / dtau**2
    print(f"S_occ'' (left-side) = {S_pp_left:.6f}")

# ── Step 3: Harmonic frequency and ZPF amplitude ──────────────────────
M_eff = 5.0  # DeWitt metric on moduli space  # (local)

print(f"\n── Harmonic Analysis ──")
print(f"M_eff (DeWitt) = {M_eff}")

if S_pp > 0:
    omega_0 = np.sqrt(S_pp / M_eff)
    delta_tau_0 = 1.0 / np.sqrt(2.0 * M_eff * omega_0)

    print(f"omega_0 = sqrt(S_occ'' / M_eff) = sqrt({S_pp:.4f} / {M_eff}) = {omega_0:.6f}")
    print(f"delta_tau_0 = 1/sqrt(2 * M_eff * omega_0) = {delta_tau_0:.6f}")

    # Dimensional check: omega_0 in units of M_KK (natural units)
    # delta_tau_0 is dimensionless (tau is dimensionless)

    # Energy of ZPF: E_zpf = (1/2) * omega_0
    E_zpf = 0.5 * omega_0
    print(f"E_zpf = omega_0 / 2 = {E_zpf:.6f} (in M_KK units)")
else:
    print("S_occ'' <= 0: no harmonic oscillator. Well is not convex at grid level.")
    omega_0 = 0
    delta_tau_0 = np.inf

# ── Step 4: Barrier width estimation ──────────────────────────────────
print(f"\n── Barrier Width ──")

# Find the barrier: the local maximum after the minimum
# Look for the first local max after i_min
i_barrier = None
for i in range(i_min + 1, min(i_min + 15, len(tau) - 1)):
    if S[i] > S[i-1] and S[i] >= S[i+1]:
        i_barrier = i
        break

if i_barrier is None:
    # The barrier is the immediate jump at i_min+1
    i_barrier = i_min + 1
    for i in range(i_min + 1, min(i_min + 10, len(tau) - 1)):
        if S[i] > S[i_barrier]:
            i_barrier = i

S_barrier = S[i_barrier]
tau_barrier = tau[i_barrier]
barrier_height = S_barrier - S_min

print(f"Barrier location: index={i_barrier}, tau={tau_barrier:.6f}")
print(f"Barrier height: {barrier_height:.8f}")
print(f"Pre-computed barrier height: {barrier_h[icut, iocc]:.8f}")

# Barrier width at half-maximum
half_barrier = S_min + barrier_height / 2

# Left side of barrier (from minimum going left)
# Find where S crosses half_barrier on the descent into the minimum
i_left_half = None
for i in range(i_min, 0, -1):
    if S[i] >= half_barrier:
        # Linear interpolation
        frac = (half_barrier - S[i]) / (S[i-1] - S[i]) if S[i-1] != S[i] else 0
        tau_left = tau[i] - frac * dtau  # wrong direction
        frac = (half_barrier - S[i]) / (S[i] - S[i+1]) if S[i] != S[i+1] else 0
        tau_left = tau[i]
        i_left_half = i
        break

# Right side of barrier (going right past the barrier peak)
i_right_half = None
for i in range(i_barrier, min(i_barrier + 15, len(tau) - 1)):
    if S[i] <= half_barrier and i > i_barrier:
        # Linear interpolation
        if S[i-1] != S[i]:
            frac = (S[i-1] - half_barrier) / (S[i-1] - S[i])
            tau_right = tau[i-1] + frac * dtau
        else:
            tau_right = tau[i]
        i_right_half = i
        break

# A more robust width estimate: distance from minimum to barrier peak
# This is the "escape width" — how far tau must fluctuate to reach the barrier top
Delta_tau_escape = abs(tau_barrier - tau_min)
print(f"\nEscape width (min to barrier peak): Delta_tau = {Delta_tau_escape:.6f}")

# Also compute the FWHM-style barrier width
if i_left_half is not None and i_right_half is not None:
    Delta_tau_fwhm = tau_right - tau_left
    print(f"FWHM barrier width: Delta_tau_fwhm = {Delta_tau_fwhm:.6f}")
else:
    # Fallback: use the distance between points where S is above half_barrier
    above_half = np.where(S > half_barrier)[0]
    # Find the contiguous segment containing the barrier
    near_barrier = above_half[(above_half >= i_min) & (above_half <= i_min + 15)]
    if len(near_barrier) > 0:
        Delta_tau_fwhm = (tau[near_barrier[-1]] - tau[near_barrier[0]]) + dtau
        print(f"FWHM barrier width (from grid): Delta_tau_fwhm = {Delta_tau_fwhm:.6f}")
    else:
        Delta_tau_fwhm = Delta_tau_escape * 2
        print(f"FWHM barrier width (estimated): Delta_tau_fwhm = {Delta_tau_fwhm:.6f}")

# The physically relevant width is the escape distance
Delta_tau = Delta_tau_escape

# ── Step 5: Stability comparison ──────────────────────────────────────
print(f"\n{'=' * 70}")
print(f"STABILITY ASSESSMENT")
print(f"{'=' * 70}")

print(f"\ndelta_tau_0 (ZPF amplitude)     = {delta_tau_0:.6f}")
print(f"Delta_tau (escape to barrier)   = {Delta_tau:.6f}")

if delta_tau_0 < np.inf:
    ratio = delta_tau_0 / Delta_tau
    print(f"delta_tau_0 / Delta_tau          = {ratio:.4f}")
    print(f"delta_tau_0 / (Delta_tau / 2)    = {2*ratio:.4f}")
    print(f"delta_tau_0 / (Delta_tau / 4)    = {4*ratio:.4f}")

    print(f"\nCriteria:")
    if delta_tau_0 > Delta_tau / 2:
        stability = "UNSTABLE"
        print(f"  delta_tau_0 > Delta_tau/2: QUANTUM TUNNELING DESTROYS MINIMUM")
    elif delta_tau_0 < Delta_tau / 4:
        stability = "STABLE"
        print(f"  delta_tau_0 < Delta_tau/4: MINIMUM SURVIVES ZPF")
    else:
        stability = "MARGINAL"
        print(f"  Delta_tau/4 < delta_tau_0 < Delta_tau/2: MARGINAL (WKB analysis needed)")

    # Gamow tunneling estimate
    # WKB tunneling probability: P ~ exp(-2 * integral sqrt(2M(V-E)) dtau)
    # For a rough estimate: P ~ exp(-2 * sqrt(2 * M_eff * barrier_height) * Delta_tau)
    exponent = 2 * np.sqrt(2 * M_eff * barrier_height) * Delta_tau
    P_tunnel = np.exp(-exponent) if exponent < 500 else 0.0
    print(f"\n  WKB tunneling exponent: 2*sqrt(2*M*V_b)*Delta_tau = {exponent:.4f}")
    print(f"  Gamow tunneling probability: P ~ exp(-{exponent:.2f}) = {P_tunnel:.2e}")

    # Number of ZPF oscillations to tunnel (inverse of probability)
    if P_tunnel > 0:
        N_oscillations = 1.0 / P_tunnel
        print(f"  Oscillations to tunnel: ~ {N_oscillations:.2e}")

    # Barrier height in units of omega_0 (number of quanta)
    n_quanta = barrier_height / omega_0
    print(f"\n  Barrier height / omega_0 = {n_quanta:.4f} quanta")
    if n_quanta > 1:
        print(f"  Barrier is {n_quanta:.1f} quanta tall: classically stable against ZPF")
    else:
        print(f"  Barrier is sub-quantum: ZPF easily reaches barrier top")

else:
    ratio = np.inf
    stability = "ILL-DEFINED"
    print("  S_occ'' <= 0: no harmonic well. Stability undefined.")

# ── Step 6: Compare omega_0 to Leggett mode ──────────────────────────
omega_L1 = 0.070  # Leggett mode frequency in M_KK units

print(f"\n── Frequency Comparison ──")
print(f"omega_0 (well frequency)  = {omega_0:.6f} M_KK")
print(f"omega_L1 (Leggett mode)   = {omega_L1:.6f} M_KK")
if omega_0 > 0:
    print(f"omega_0 / omega_L1        = {omega_0 / omega_L1:.4f}")

    if abs(omega_0 - omega_L1) / omega_L1 < 0.3:
        print("  NEAR RESONANCE with Leggett mode — energy exchange possible")
    elif omega_0 > omega_L1:
        print("  Well frequency ABOVE Leggett mode — well is stiffer than pairing dynamics")
    else:
        print("  Well frequency BELOW Leggett mode — well is softer than pairing dynamics")

# ── Repeat for ALL combinations with minima ───────────────────────────
print(f"\n{'=' * 70}")
print(f"SURVEY: All Combinations with Minima")
print(f"{'=' * 70}")

print(f"\n{'Cutoff':>12s} {'Lambda':>6s} {'Occ':>4s} | {'tau_min':>8s} {'S_min':>10s} "
      f"{'Barrier':>10s} {'S_pp':>10s} {'omega_0':>8s} {'dtau_0':>8s} {'Dtau':>8s} {'ratio':>8s} {'Stable':>10s}")
print("-" * 120)

results = {}
for ic in range(3):
    for jo in range(3):
        if not has_min[ic, jo]:
            continue

        S_curve = S_occ_all[ic, jo, :]

        # Find minimum in [0.10, 0.35]
        mask2 = (tau >= 0.05) & (tau <= 0.35)
        idx2 = np.where(mask2)[0]
        im = idx2[np.argmin(S_curve[idx2])]

        # Second derivative
        spp = (S_curve[im+1] - 2*S_curve[im] + S_curve[im-1]) / dtau**2

        # Find barrier (first local max after minimum)
        ib = im + 1
        for ii in range(im+1, min(im+10, len(tau)-1)):
            if S_curve[ii] >= S_curve[ib]:
                ib = ii

        bh = S_curve[ib] - S_curve[im]
        dt_esc = abs(tau[ib] - tau[im])

        if spp > 0:
            w0 = np.sqrt(spp / M_eff)
            dt0 = 1.0 / np.sqrt(2.0 * M_eff * w0)
            rat = dt0 / dt_esc if dt_esc > 0 else np.inf
            if dt0 > dt_esc / 2:
                stab = "UNSTABLE"
            elif dt0 < dt_esc / 4:
                stab = "STABLE"
            else:
                stab = "MARGINAL"
        else:
            w0 = 0
            dt0 = np.inf
            rat = np.inf
            stab = "ILL-DEFINED"

        results[(ic, jo)] = {
            'tau_min': tau[im], 'S_min': S_curve[im], 'barrier': bh,
            'S_pp': spp, 'omega_0': w0, 'dtau_0': dt0,
            'Delta_tau': dt_esc, 'ratio': rat, 'stability': stab
        }

        print(f"{cutoff_names[ic]:>12s} {Lambda_vals[ic]:>6.1f} {jo:>4d} | "
              f"{tau[im]:>8.5f} {S_curve[im]:>10.6f} {bh:>10.6f} "
              f"{spp:>10.3f} {w0:>8.4f} {dt0:>8.5f} {dt_esc:>8.5f} {rat:>8.4f} {stab:>10s}")

# ── Final Summary ─────────────────────────────────────────────────────
print(f"\n{'=' * 70}")
print(f"GATE VERDICT: ZPF-STABILITY-55 (INFO)")
print(f"{'=' * 70}")

# Primary result: Sharp cutoff, occ_type=0
r = results[(1, 0)]
print(f"\nPrimary analysis: Sharp cutoff, Lambda=2.0, occ_type=0")
print(f"  tau_min = {r['tau_min']:.6f}")
print(f"  S_occ'' = {r['S_pp']:.3f}")
print(f"  omega_0 = {r['omega_0']:.6f} M_KK")
print(f"  delta_tau_0 = {r['dtau_0']:.6f}")
print(f"  Delta_tau (escape) = {r['Delta_tau']:.6f}")
print(f"  delta_tau_0 / Delta_tau = {r['ratio']:.4f}")
print(f"  Stability: {r['stability']}")
print(f"  omega_0 / omega_L1 = {r['omega_0'] / omega_L1:.4f}")

# Classification
print(f"\nPhysical interpretation:")
if r['stability'] == 'STABLE':
    print("  The S_occ minimum survives quantum zero-point fluctuations.")
    print("  The modulus is confined to the well at the quantum level.")
elif r['stability'] == 'UNSTABLE':
    print("  Zero-point fluctuations of the modulus field are larger than")
    print("  the barrier width. The minimum is quantum-mechanically unstable.")
    print("  The modulus tunnels out within O(1) oscillation periods.")
elif r['stability'] == 'MARGINAL':
    print("  ZPF amplitude is comparable to barrier width.")
    print("  Full WKB / instanton calculation needed for definitive assessment.")

# Phononic classification
print(f"\nPhononic classification: GEOMETRIC (modulus fluctuation = shape oscillation of cavity)")
print(f"Condensed matter analog: Debye-Waller factor for lattice position stability")

print(f"\nDone.")
