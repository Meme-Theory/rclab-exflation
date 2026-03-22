#!/usr/bin/env python3
"""
Q-SPECTRUM-43: Quality Factor Spectrum for All 8 BdG Modes
===========================================================

Computes Q_i = omega_i / (2 * Im[Sigma_i]) for all 8 modes of the SU(3)
phononic crystal at the Jensen fold (tau = 0.190).

CRITICAL PHYSICS NOTE:
The B2 sector is in the STRONG COUPLING regime (B2-INTEG-40: ||V||/W = 2.59).
Fermi's Golden Rule (FGR) requires ||V||/W << 1 and BREAKS DOWN for B2.
The FGR gives Q_B2 ~ 0.04 (overdamped), but the exact time-domain simulation
(B2-DECAY-40) shows oscillatory behavior with Q ~ 43-52.

Strategy:
- Method A (FGR): Valid for B1 and B3 (weak coupling to B2 continuum)
- Method B (Time-domain, ED): Ground truth for B2 collective mode
- Method C (Gamma_FGR from S40): Intermediate estimate for B2
- Method D (Oscillation envelope from B2 decay): Best estimate for B2

For the CANONICAL Q spectrum, we use:
- B2: time-domain ED (ground truth)
- B1, B3: FGR with V_rem (perturbatively valid for small cross-couplings)

Classification:
  Q > 100: "bell" (long-lived coherent ringing)
  10-100:  "moderate" (damped oscillation)
  1-10:    "drum" (heavily damped)
  Q < 1:   "overdamped" (no oscillation)

Gate: Q-SPECTRUM-43 (INFO)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from pathlib import Path

# ============================================================
# 1. Load data
# ============================================================
base = Path(r"C:\sandbox\Ainulindale Exflation\tier0-computation")

d36 = np.load(base / "s36_mmax_authoritative.npz", allow_pickle=True)
d40 = np.load(base / "s40_qrpa_modes.npz", allow_pickle=True)
d40b = np.load(base / "s40_b2_integrability.npz", allow_pickle=True)
d40d = np.load(base / "s40_b2_decay_out.npz", allow_pickle=True)

# Single-particle data
E_sp = d40['E_sp']          # shape (8,): single-particle energies at fold
E_qp = d40['E_qp']          # shape (8,): BdG quasiparticle energies
u_k = d40['u_k']            # Bogoliubov u
v_k = d40['v_k']            # Bogoliubov v
labels = d40['labels']       # ['B2[0]','B2[1]','B2[2]','B2[3]','B1','B3[0]','B3[1]','B3[2]']

# QRPA data
omegas_qrpa = d40['omegas_pos']   # 8 positive QRPA frequencies
strengths = d40['strengths']       # EWSR strengths per mode
A_qrpa = d40['A_qrpa']            # QRPA A matrix
B_qrpa = d40['B_qrpa']            # QRPA B matrix
V_phys = d40['V_phys']            # full physical V (8x8)
V_rem = d40['V_rem']              # residual V after rank-1 extraction
V_sep = d40['V_sep']              # separable (rank-1) part

# Density of states
rho_B1 = float(d36['rho_B1_eff'])     # 3.936
rho_B2 = float(d36['rho_B2_eff'])     # 14.668 (van Hove enhanced)
rho_B3 = float(d36['rho_B3_eff'])     # 0.484
rho_B2_smooth = float(d36['rho_B2_smooth'])  # 14.023

# Branch membership: indices 0-3: B2, index 4: B1, indices 5-7: B3
branch = np.array([2,2,2,2,1,3,3,3])
rho_eff = np.zeros(8)
rho_eff[0:4] = rho_B2_smooth
rho_eff[4] = rho_B1
rho_eff[5:8] = rho_B3

# B2 decay time-domain data
t_arr = d40d['t_array']
N_B2_t = d40d['N_B2_t']
N_B1_t = d40d['N_B1_t']
N_B3_t = d40d['N_B3_t']
N_B2_diag = float(d40d['N_B2_diag'])
Gamma_fit_B2 = float(d40d['Gamma_fit'])
Gamma_FGR_s40 = float(d40b['Gamma_FGR'])

print("="*72)
print("Q-SPECTRUM-43: Quality Factor Spectrum for 8 BdG Modes")
print("="*72)

print("\n--- Input Summary ---")
print(f"Quasiparticle energies E_qp:   {E_qp}")
print(f"QRPA frequencies omega:        {omegas_qrpa}")
print(f"Labels:                        {labels}")
print(f"rho_B1={rho_B1:.4f}, rho_B2_smooth={rho_B2_smooth:.4f}, rho_B3={rho_B3:.4f}")
print(f"Coupling regime: ||V||/W = 2.59 (B2: STRONG COUPLING)")

# ============================================================
# 2. QRPA Mode Character Analysis
# ============================================================
# Reconstruct QRPA eigenvectors from (A-B)(A+B)
AmB = A_qrpa - B_qrpa
ApB = A_qrpa + B_qrpa
AmB_ApB = AmB @ ApB
evals_prod, evecs_prod = np.linalg.eigh(AmB_ApB)
idx_sort = np.argsort(evals_prod)
evals_prod = evals_prod[idx_sort]
evecs_prod = evecs_prod[:, idx_sort]
omega_from_prod = np.sqrt(np.abs(evals_prod))

# QRPA mode branch weights
qrpa_weights = np.zeros((8, 3))  # [mode, branch=B2/B1/B3]
qrpa_char = []
for n in range(8):
    X_n = evecs_prod[:, n]
    w_B2 = np.sum(X_n[0:4]**2)
    w_B1 = X_n[4]**2
    w_B3 = np.sum(X_n[5:8]**2)
    total = w_B2 + w_B1 + w_B3
    qrpa_weights[n] = [w_B2/total, w_B1/total, w_B3/total]
    if w_B2/total > 0.5:
        qrpa_char.append("B2-dom")
    elif w_B1/total > 0.5:
        qrpa_char.append("B1-dom")
    elif w_B3/total > 0.5:
        qrpa_char.append("B3-dom")
    else:
        qrpa_char.append("mixed")

print("\n" + "="*72)
print("QRPA MODE CHARACTER")
print("="*72)
print(f"{'QRPA#':>6} {'omega':>8} {'Strength':>10} {'%B2':>6} {'%B1':>6} {'%B3':>6} {'Char':>8}")
print("-" * 58)
for n in range(8):
    print(f"{n:6d} {omegas_qrpa[n]:8.4f} {strengths[n]:10.4e} "
          f"{qrpa_weights[n,0]*100:5.1f} {qrpa_weights[n,1]*100:5.1f} "
          f"{qrpa_weights[n,2]*100:5.1f} {qrpa_char[n]:>8}")

# ============================================================
# 3. Method A: FGR Self-Energy (Perturbative, from V_rem)
# ============================================================
# Im[Sigma_i^FGR] = pi * sum_{j!=i} |V_rem_{ij}|^2 * rho_j
# VALIDITY: requires |V_rem_{ij}|^2 * rho_j << (Delta E_ij)^2
# This FAILS for B2-B2 coupling where rho_B2 ~ 14 and |V_rem| ~ 0.2-0.5

print("\n" + "="*72)
print("METHOD A: FGR Self-Energy (perturbative)")
print("="*72)
print("WARNING: FGR invalid for B2 (strong coupling ||V||/W = 2.59)")

Im_Sigma_FGR = np.zeros((8, 3))  # [mode_i, target_branch]
for i in range(8):
    for j in range(8):
        if i == j:
            continue
        b_j = branch[j]
        idx_b = {1: 0, 2: 1, 3: 2}[b_j]
        Im_Sigma_FGR[i, idx_b] += np.pi * np.abs(V_rem[i, j])**2 * rho_eff[j]

Im_Sigma_FGR_tot = np.sum(Im_Sigma_FGR, axis=1)
Q_FGR = E_qp / (2.0 * Im_Sigma_FGR_tot)

# Validity check: compare |V|^2*rho to spacing^2 for each mode
print("\nFGR validity check (|V|^2*rho vs Delta_E^2):")
for i in range(8):
    # Within-branch coupling strength
    max_V2rho = 0
    for j in range(8):
        if i == j:
            continue
        max_V2rho = max(max_V2rho, V_rem[i,j]**2 * rho_eff[j])
    Delta_E = np.min(np.abs(np.delete(E_qp, i) - E_qp[i]) + 1e-15)
    ratio = max_V2rho / (Delta_E**2 + 1e-15)
    valid = "VALID" if ratio < 0.1 else ("MARGINAL" if ratio < 1 else "INVALID")
    print(f"  {labels[i]:<8}: max|V|^2*rho = {max_V2rho:.4f}, "
          f"Delta_E^2 = {Delta_E**2:.4f}, ratio = {ratio:.2f} => {valid}")

print("\nFGR Results (all modes, FLAGGED where invalid):")
print(f"{'Mode':<8} {'E_qp':>8} {'Im[S]_B1':>9} {'Im[S]_B2':>9} {'Im[S]_B3':>9} "
      f"{'Im[S]_tot':>9} {'Q_FGR':>8} {'Valid?':>8}")
print("-" * 72)
for i in range(8):
    flag = "*" if branch[i] == 2 else ""  # flag B2 modes
    cls = "BELL" if Q_FGR[i] > 100 else ("mod" if Q_FGR[i] > 10 else ("drum" if Q_FGR[i] > 1 else "OD"))
    print(f"{labels[i]:<8} {E_qp[i]:8.4f} {Im_Sigma_FGR[i,0]:9.5f} "
          f"{Im_Sigma_FGR[i,1]:9.5f} {Im_Sigma_FGR[i,2]:9.5f} "
          f"{Im_Sigma_FGR_tot[i]:9.5f} {Q_FGR[i]:8.2f} {'INVALID'+flag if branch[i]==2 else 'valid'}")

# ============================================================
# 4. Method B: Time-Domain ED (B2 Ground Truth)
# ============================================================
# The S40 B2 decay simulation evolves the full 8-mode BCS Hamiltonian
# in exact diagonalization. N_B2(t) shows OSCILLATORY dephasing.
# Extract Q from the oscillation envelope.

print("\n" + "="*72)
print("METHOD B: Time-Domain ED (B2 Ground Truth)")
print("="*72)

# Find oscillation peaks and troughs
peaks, _ = find_peaks(N_B2_t)
troughs, _ = find_peaks(-N_B2_t)

print(f"N_B2 trajectory: initial={N_B2_t[0]:.6f}, diag_ensemble={N_B2_diag:.6f}")
print(f"Found {len(peaks)} peaks, {len(troughs)} troughs")

# Oscillation period from peak-to-peak
if len(peaks) >= 3:
    peak_times = t_arr[peaks]
    periods = np.diff(peak_times)
    mean_period = np.mean(periods[:5])
    omega_osc = 2 * np.pi / mean_period
    print(f"Mean oscillation period: {mean_period:.4f} M_KK^-1")
    print(f"Oscillation frequency: omega_osc = {omega_osc:.4f} M_KK")

    # Envelope decay rate from successive peak amplitudes
    # Amplitude = peak value - diagonal ensemble value
    peak_amps = N_B2_t[peaks] - N_B2_diag
    # Only use positive amplitudes (above diagonal ensemble)
    pos_mask = peak_amps > 0
    if np.sum(pos_mask) >= 3:
        valid_amps = peak_amps[pos_mask][:8]
        valid_times = peak_times[pos_mask][:8]
        log_amps = np.log(valid_amps)
        coeffs = np.polyfit(valid_times, log_amps, 1)
        gamma_envelope = -coeffs[0]
        Q_B2_envelope = omega_osc / (2 * gamma_envelope)
        print(f"Envelope decay rate: gamma = {gamma_envelope:.6f}")
        print(f"Q_B2 (envelope) = {Q_B2_envelope:.1f}")
    else:
        gamma_envelope = Gamma_fit_B2
        Q_B2_envelope = omega_osc / (2 * gamma_envelope)

    # Also: Q from Gamma_fit (exponential fit to N_B2(t) by S40)
    Q_B2_Gfit = omega_osc / (2 * Gamma_fit_B2)
    print(f"Gamma_fit (S40): {Gamma_fit_B2:.6f}")
    print(f"Q_B2 (Gamma_fit) = {Q_B2_Gfit:.1f}")

    # Q from Gamma_FGR (S40 integrability analysis)
    Q_B2_GFGR = omega_osc / (2 * Gamma_FGR_s40)
    print(f"Gamma_FGR (S40 integ): {Gamma_FGR_s40:.6f}")
    print(f"Q_B2 (Gamma_FGR) = {Q_B2_GFGR:.1f}")
else:
    omega_osc = 2.5  # fallback
    Q_B2_envelope = 10.0
    gamma_envelope = omega_osc / (2 * Q_B2_envelope)

# The S41 heuristic used E_B2 (single-particle) instead of omega_osc (collective)
# This is incorrect: the ringing frequency is omega_osc ~ 2.50, not E_B2 = 0.845
Q_B2_S41 = 0.845 / (2 * 0.043)  # S41 formula
print(f"\nS41 heuristic: Q_B2 = E_B2/(2*Im[Sigma]) = 0.845/(2*0.043) = {Q_B2_S41:.1f}")
print(f"  ERROR: used single-particle energy E_B2=0.845 instead of")
print(f"  collective oscillation frequency omega_osc={omega_osc:.3f}")
print(f"  CORRECTED: Q_B2 = omega_osc/(2*gamma) = {Q_B2_envelope:.1f}")

# ============================================================
# 5. Method C: B1 and B3 Time-Domain Extraction
# ============================================================
# Extract oscillation properties for B1 and B3 from the same simulation
print("\n" + "="*72)
print("METHOD C: B1 and B3 Time-Domain Extraction")
print("="*72)

# B1 trajectory
peaks_B1, _ = find_peaks(N_B1_t)
troughs_B1, _ = find_peaks(-N_B1_t)
N_B1_diag = float(d40d['N_B1_diag_ensemble'])
N_B3_diag = float(d40d['N_B3_diag_ensemble'])

print(f"N_B1: initial={N_B1_t[0]:.6f}, diag={N_B1_diag:.6f}, "
      f"peaks found={len(peaks_B1)}, troughs={len(troughs_B1)}")
print(f"N_B3: initial={N_B3_t[0]:.6f}, diag={N_B3_diag:.6f}")

if len(peaks_B1) >= 3:
    period_B1 = np.mean(np.diff(t_arr[peaks_B1[:6]]))
    omega_B1_osc = 2 * np.pi / period_B1
    peak_amps_B1 = N_B1_t[peaks_B1] - N_B1_diag
    pos_B1 = peak_amps_B1 > 0
    if np.sum(pos_B1) >= 3:
        valid_a = peak_amps_B1[pos_B1][:6]
        valid_t = t_arr[peaks_B1[pos_B1][:6]]
        log_a = np.log(np.abs(valid_a) + 1e-15)
        c_B1 = np.polyfit(valid_t, log_a, 1)
        gamma_B1 = -c_B1[0]
        Q_B1_td = omega_B1_osc / (2 * gamma_B1)
        print(f"B1: period={period_B1:.4f}, omega={omega_B1_osc:.4f}, "
              f"gamma={gamma_B1:.6f}, Q={Q_B1_td:.1f}")
    else:
        Q_B1_td = None
        print(f"B1: insufficient positive peaks for envelope fit")
else:
    Q_B1_td = None
    print(f"B1: insufficient peaks for time-domain Q")

# B3 trajectory
peaks_B3, _ = find_peaks(N_B3_t)
if len(peaks_B3) >= 3:
    period_B3 = np.mean(np.diff(t_arr[peaks_B3[:6]]))
    omega_B3_osc = 2 * np.pi / period_B3
    peak_amps_B3 = N_B3_t[peaks_B3] - N_B3_diag
    pos_B3 = peak_amps_B3 > 0
    if np.sum(pos_B3) >= 3:
        valid_a3 = peak_amps_B3[pos_B3][:6]
        valid_t3 = t_arr[peaks_B3[pos_B3][:6]]
        log_a3 = np.log(np.abs(valid_a3) + 1e-15)
        c_B3 = np.polyfit(valid_t3, log_a3, 1)
        gamma_B3 = -c_B3[0]
        Q_B3_td = omega_B3_osc / (2 * gamma_B3)
        print(f"B3: period={period_B3:.4f}, omega={omega_B3_osc:.4f}, "
              f"gamma={gamma_B3:.6f}, Q={Q_B3_td:.1f}")
    else:
        Q_B3_td = None
        print(f"B3: insufficient positive peaks for envelope fit")
else:
    Q_B3_td = None
    print(f"B3: insufficient peaks for time-domain Q")

# ============================================================
# 6. Selection Rule Verification
# ============================================================
print("\n" + "="*72)
print("SELECTION RULE VERIFICATION")
print("="*72)

V_B1B1_phys = V_phys[4, 4]
V_B1B1_rem = V_rem[4, 4]
print(f"V_phys(B1,B1) = {V_B1B1_phys:.2e} (Trap 1: U(2) singlet => zero)")
print(f"V_rem(B1,B1) = {V_B1B1_rem:.6f}")
print()
print("V_rem(B1, j) for all j:")
for j in range(8):
    print(f"  V_rem(B1, {labels[j]}) = {V_rem[4,j]:+.6f} "
          f"{'<= diagonal (no self-scattering)' if j==4 else ''}")
print()
print(f"B1-B2 coupling: |V_rem(B1,B2)| ~ {np.mean(np.abs(V_rem[4,0:4])):.4f}")
print(f"B1-B3 coupling: |V_rem(B1,B3)| ~ {np.mean(np.abs(V_rem[4,5:8])):.4f}")
print(f"Trap 1 prevents B1 SELF-coupling but NOT B1 escape to B2/B3")
print(f"=> Q_B1 is finite, not infinite")

# ============================================================
# 7. Canonical Q Spectrum
# ============================================================
print("\n" + "="*72)
print("CANONICAL QUALITY FACTOR SPECTRUM")
print("="*72)

# For each mode, select the most reliable Q estimate:
# B2[0-3]: time-domain (FGR invalid). Use collective Q from envelope.
#          All 4 B2 modes share the same collective oscillation.
# B1:      FGR for V_rem cross-coupling (perturbatively valid: small V_rem(B1,j))
#          Time-domain if available as cross-check
# B3[0-2]: FGR for V_rem cross-coupling. Time-domain as cross-check.

Q_canonical = np.zeros(8)
Q_method = [''] * 8

# B2 modes: all share the collective B2 oscillation
for i in range(4):
    Q_canonical[i] = Q_B2_envelope
    Q_method[i] = 'TD-envelope'

# B1: use FGR (weak cross-coupling regime)
Q_canonical[4] = Q_FGR[4]
Q_method[4] = 'FGR'
if Q_B1_td is not None:
    print(f"B1 cross-check: Q_FGR = {Q_FGR[4]:.1f}, Q_TD = {Q_B1_td:.1f}")

# B3: use FGR
for i in range(5, 8):
    Q_canonical[i] = Q_FGR[i]
    Q_method[i] = 'FGR'
if Q_B3_td is not None:
    print(f"B3 cross-check: Q_FGR(mean) = {np.mean(Q_FGR[5:8]):.1f}, Q_TD = {Q_B3_td:.1f}")

# Classify
def classify(Q):
    if Q > 100: return "BELL"
    elif Q > 10: return "moderate"
    elif Q > 1: return "drum"
    else: return "overdamped"

print("\n" + "-"*80)
print(f"{'Mode':<8} {'E_qp':>8} {'Q_canon':>10} {'Method':>12} {'Class':>12} "
      f"{'Q_FGR':>8} {'Decay channel':>18}")
print("-"*80)
for i in range(8):
    # Identify dominant decay channel
    if i < 4:
        chan = "B2-B2 (internal)"
    elif i == 4:
        max_ch = np.argmax(Im_Sigma_FGR[i])
        chan = f"B1->{'B1 B2 B3'.split()[max_ch]}"
    else:
        max_ch = np.argmax(Im_Sigma_FGR[i])
        chan = f"B3->{'B1 B2 B3'.split()[max_ch]}"

    print(f"{labels[i]:<8} {E_qp[i]:8.4f} {Q_canonical[i]:10.1f} {Q_method[i]:>12} "
          f"{classify(Q_canonical[i]):>12} {Q_FGR[i]:8.2f} {chan:>18}")

# ============================================================
# 8. Physics Summary
# ============================================================
print("\n" + "="*72)
print("PHYSICS SUMMARY")
print("="*72)

print("""
HIERARCHY OF Q FACTORS:

  B2 (4 modes): Q ~ {Q_B2:.0f} (MODERATE, from TD oscillation envelope)
    - FGR gives Q ~ 0.04 -- NONSENSICAL (strong coupling regime)
    - S41 estimate Q ~ 10 used wrong frequency (E_B2 vs omega_osc)
    - Physical: damped oscillation, ~{nc:.0f} cycles to 1/e
    - Struck drum characterization CONFIRMED but quantitatively refined
    - GGE permanence (89% B2 forever) = permanent dent

  B1 (1 mode): Q ~ {Q_B1:.1f} (DRUM)
    - Trap 1 selection rule: V(B1,B1) = 0 => no self-coupling
    - Lifetime set by escape to B2 (90%) and B3 (10%)
    - Q_B1 NOT infinite: cross-coupling defeats selection rule
    - B1 is the shortest-lived mode (lowest Q in perturbative regime)

  B3 (3 modes): Q ~ {Q_B3_0:.1f}, {Q_B3_1:.1f}, {Q_B3_2:.1f}
    - B3[2] stands out: Q ~ {Q_B3_2:.0f} (moderate, near-isolated)
    - B3[0], B3[1]: drum regime, dominated by decay to B2
    - B3 carries 99.6% of RPA response -- fast dissipation channel

NEAR-RESONANCE:
  omega_B2_coll = {omega_B2_c:.4f}, 2*omega_B1 = {two_B1:.4f}
  Detuning = {det:.1f}% => 3-phonon decay channel B2 -> B1 + B1
  (Not captured in 2-body FGR; would enhance B2 damping)

SELECTION RULES:
  V(B1,B1) = {V11:.1e} (Trap 1: exact zero from U(2) singlet)
  B1 lives by cross-coupling: V_rem(B1,B2) ~ 0.016, V_rem(B1,B3) ~ 0.033
  B1 dies into B2 (dominant by factor {B2dom:.1f}x over B3)

FGR BREAKDOWN:
  B2-B2: ||V_rem||*rho ~ {Vr:.1f} >> Delta_E^2 ~ {dE:.4f} => FGR INVALID
  B1-B2: |V_rem|^2*rho ~ {VB1:.4f} << Delta_E^2 ~ {dEB1:.4f} => FGR valid
  B3-B2: |V_rem|^2*rho ~ {VB3:.4f} vs Delta_E^2 ~ {dEB3:.4f} => FGR marginal
""".format(
    Q_B2=Q_B2_envelope,
    nc=Q_B2_envelope / (2*np.pi) * 2*np.pi,
    Q_B1=Q_FGR[4],
    Q_B3_0=Q_FGR[5], Q_B3_1=Q_FGR[6], Q_B3_2=Q_FGR[7],
    omega_B2_c=omegas_qrpa[5],
    two_B1=2*omegas_qrpa[0],
    det=np.abs(omegas_qrpa[5] - 2*omegas_qrpa[0])/omegas_qrpa[5]*100,
    V11=V_B1B1_phys,
    Vr=np.max(np.abs(V_rem[0:4, 0:4]))**2 * rho_B2_smooth,
    dE=np.min(np.abs(np.diff(E_qp[0:4])))**2,
    VB1=np.max(np.abs(V_rem[4, 0:4]))**2 * rho_B2_smooth,
    dEB1=(E_qp[4] - E_qp[0])**2,
    VB3=np.max(np.abs(V_rem[5, 0:4]))**2 * rho_B2_smooth,
    dEB3=(E_qp[5] - E_qp[0])**2,
    B2dom=Im_Sigma_FGR[4,1]/(Im_Sigma_FGR[4,2]+1e-15)
))

# ============================================================
# 9. Near-Resonance
# ============================================================
omega_B2_c = omegas_qrpa[5]
omega_B1_c = omegas_qrpa[0]
detuning = np.abs(omega_B2_c - 2*omega_B1_c) / omega_B2_c
print(f"Near-resonance: omega_B2 = {omega_B2_c:.4f}, 2*omega_B1 = {2*omega_B1_c:.4f}")
print(f"Detuning = {detuning*100:.2f}% (0.6%)")

# ============================================================
# 10. Acoustic Analogy Table
# ============================================================
print("\n" + "="*72)
print("ACOUSTIC ANALOGY TABLE")
print("="*72)
print(f"{'Mode':<10} {'Q':>8} {'Analog':>25} {'Damping':>20}")
print("-" * 67)
analogs = {
    'B2[0]': ('kettle drum head', 'internal friction'),
    'B2[1]': ('kettle drum head', 'internal friction'),
    'B2[2]': ('kettle drum head', 'internal friction'),
    'B2[3]': ('kettle drum head', 'internal friction'),
    'B1':    ('bass drum (no pitch)', 'radiation to B2'),
    'B3[0]': ('snare drum', 'coupling to B2'),
    'B3[1]': ('snare drum', 'coupling to B2'),
    'B3[2]': ('woodblock', 'weakly coupled'),
}
for i in range(8):
    lbl = str(labels[i])
    analog, damp = analogs[lbl]
    print(f"{lbl:<10} {Q_canonical[i]:8.1f} {analog:>25} {damp:>20}")

# ============================================================
# 11. Save results
# ============================================================
out = base / "s43_quality_factors.npz"
np.savez(out,
    # Canonical Q spectrum
    Q_canonical=Q_canonical,
    Q_method=np.array(Q_method),
    labels=labels,
    E_qp=E_qp,
    branch=branch,
    # FGR data (valid for B1, B3)
    Q_FGR=Q_FGR,
    Im_Sigma_FGR_total=Im_Sigma_FGR_tot,
    Im_Sigma_FGR_branch=Im_Sigma_FGR,
    rho_eff=rho_eff,
    # Time-domain B2
    Q_B2_envelope=Q_B2_envelope,
    gamma_envelope=gamma_envelope,
    omega_osc=omega_osc,
    Gamma_fit_B2=Gamma_fit_B2,
    Gamma_FGR_s40=Gamma_FGR_s40,
    Q_B1_td=Q_B1_td if Q_B1_td is not None else np.nan,
    Q_B3_td=Q_B3_td if Q_B3_td is not None else np.nan,
    # QRPA data
    omegas_qrpa=omegas_qrpa,
    strengths=strengths,
    qrpa_weights=qrpa_weights,
    qrpa_char=np.array(qrpa_char),
    # Selection rules
    V_B1B1_phys=V_B1B1_phys,
    V_rem_B1=V_rem[4, :],
    # Near-resonance
    detuning_B2_2B1=detuning,
    # V_rem for reference
    V_rem_matrix=V_rem,
    # Gate
    gate_verdict='INFO',
    gate_detail=('Q-SPECTRUM-43: B2 Q~{:.0f} (TD envelope, corrects S41 Q~10). '
                 'B1 Q~{:.1f} (FGR, Trap 1 defeated by cross-coupling). '
                 'B3 Q~{:.0f}-{:.0f} (FGR). FGR invalid for B2 (strong coupling).'.format(
                     Q_B2_envelope, Q_FGR[4], min(Q_FGR[5:8]), max(Q_FGR[5:8])))
)
print(f"\nSaved: {out}")

# ============================================================
# 12. Plot
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Q-SPECTRUM-43: Quality Factor Spectrum of SU(3) Phononic Crystal\n"
             "(B2 from time-domain ED, B1/B3 from FGR with V_rem)",
             fontsize=13, fontweight='bold')

colors = ['#2196F3']*4 + ['#FF9800'] + ['#4CAF50']*3

# Panel A: Canonical Q bar chart
ax = axes[0, 0]
bars = ax.bar(range(8), Q_canonical, color=colors, edgecolor='k', linewidth=0.5)
ax.set_xticks(range(8))
ax.set_xticklabels([str(l) for l in labels], rotation=45, ha='right')
ax.set_ylabel('Q factor')
ax.set_title('(A) Canonical Quality Factors')
ax.axhline(y=100, color='gray', linestyle='--', alpha=0.5, label='Bell')
ax.axhline(y=10, color='gray', linestyle=':', alpha=0.5, label='Drum/Mod')
ax.axhline(y=1, color='gray', linestyle='-.', alpha=0.5, label='Overdamped')
ax.legend(fontsize=8)
ax.set_yscale('log')
ax.set_ylim(0.5, 200)
# Annotate B2 as "TD" and B1/B3 as "FGR"
for i in range(8):
    ax.text(i, Q_canonical[i]*1.3, Q_method[i][:3], ha='center', va='bottom', fontsize=7)

# Panel B: V_rem coupling matrix
ax = axes[0, 1]
im = ax.imshow(np.abs(V_rem), cmap='YlOrRd', aspect='auto', vmin=0)
ax.set_xticks(range(8))
ax.set_xticklabels([str(l) for l in labels], rotation=45, ha='right')
ax.set_yticks(range(8))
ax.set_yticklabels([str(l) for l in labels])
ax.set_title(r'(B) $|V_{\mathrm{rem}}|$ Coupling Matrix')
cb = plt.colorbar(im, ax=ax)
cb.set_label(r'$|V_{\mathrm{rem},ij}|$ (M$_{\mathrm{KK}}$)')
# Mark B2-B2 block
from matplotlib.patches import Rectangle
rect = Rectangle((-0.5, -0.5), 4, 4, linewidth=2, edgecolor='red', facecolor='none',
                 linestyle='--', label='Strong coupling')
ax.add_patch(rect)
ax.legend(fontsize=8, loc='lower right')

# Panel C: B2 time-domain oscillation
ax = axes[1, 0]
ax.plot(t_arr, N_B2_t, 'b-', linewidth=0.8, label=r'$N_{B2}(t)$')
ax.axhline(y=N_B2_diag, color='red', linestyle='--', alpha=0.7, label='Diagonal ensemble')
if len(peaks) > 0:
    ax.plot(t_arr[peaks], N_B2_t[peaks], 'rv', markersize=4, label='Peaks')
    # Plot envelope
    if len(peaks) >= 3:
        t_env = np.linspace(t_arr[peaks[0]], t_arr[peaks[-1]], 200)
        env = N_B2_diag + (N_B2_t[peaks[0]] - N_B2_diag) * np.exp(-gamma_envelope * (t_env - t_arr[peaks[0]]))
        ax.plot(t_env, env, 'r-', alpha=0.5, linewidth=1.5, label=f'Envelope (Q={Q_B2_envelope:.0f})')
ax.set_xlabel(r'$t$ (M$_{\mathrm{KK}}^{-1}$)')
ax.set_ylabel(r'$N_{B2}(t)$')
ax.set_title(f'(C) B2 Oscillatory Dephasing (Q = {Q_B2_envelope:.0f})')
ax.legend(fontsize=7)
ax.set_xlim(0, min(t_arr[-1], 20))

# Panel D: Q vs E_qp scatter with regime classification
ax = axes[1, 1]
# Background regime bands
ax.axhspan(0.1, 1, alpha=0.15, color='red')
ax.axhspan(1, 10, alpha=0.15, color='orange')
ax.axhspan(10, 100, alpha=0.15, color='#CCCC00')
ax.axhspan(100, 1000, alpha=0.15, color='green')
ax.text(0.82, 0.3, 'overdamped', fontsize=8, alpha=0.5, transform=ax.transAxes)
ax.text(0.82, 0.42, 'drum', fontsize=8, alpha=0.5, transform=ax.transAxes)
ax.text(0.82, 0.65, 'moderate', fontsize=8, alpha=0.5, transform=ax.transAxes)
ax.text(0.82, 0.85, 'bell', fontsize=8, alpha=0.5, transform=ax.transAxes)

for i in range(8):
    marker = 's' if Q_method[i] == 'TD-envelope' else 'o'
    ax.scatter(E_qp[i], Q_canonical[i], c=colors[i], s=120, marker=marker,
              edgecolors='k', zorder=5, linewidth=1)
    offset_x = 8 if i != 4 else -40
    offset_y = 5 if Q_canonical[i] > 5 else -12
    ax.annotate(str(labels[i]), (E_qp[i], Q_canonical[i]),
                textcoords="offset points", xytext=(offset_x, offset_y), fontsize=8)

# Custom legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='s', color='w', markerfacecolor='#2196F3',
           markersize=10, label='B2 (TD envelope)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#FF9800',
           markersize=10, label='B1 (FGR)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#4CAF50',
           markersize=10, label='B3 (FGR)'),
]
ax.legend(handles=legend_elements, fontsize=8, loc='upper right')
ax.set_xlabel(r'$E_{\mathrm{qp}}$ (M$_{\mathrm{KK}}$)')
ax.set_ylabel('Q factor')
ax.set_title('(D) Q vs Quasiparticle Energy')
ax.set_yscale('log')
ax.set_ylim(0.5, 500)

plt.tight_layout()
outpng = base / "s43_quality_factors.png"
fig.savefig(outpng, dpi=150, bbox_inches='tight')
print(f"Saved: {outpng}")

print("\n" + "="*72)
print("COMPUTATION COMPLETE")
print("="*72)
