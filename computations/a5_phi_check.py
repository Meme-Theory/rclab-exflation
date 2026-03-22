"""
URGENT: The energy-per-mode ratio E_ferm/E_bos at the gap edge equals
phi^{3/2} at tau=0.50. Is this real or numerical coincidence?

phi = (1 + sqrt(5))/2 = 1.6180339887...
phi^{3/2} = 2.0581710272... NO WAIT
phi as the Paasch phi = 1.53158... (the mass ratio, NOT golden ratio)

Let me be precise about which "phi" we're tracking.
"""
import numpy as np

phi_golden = (1 + np.sqrt(5)) / 2  # 1.6180339887
phi_paasch = 1.531580  # Session 12 sector-specific ratio m(3,0)/m(0,0)

print("="*70)
print("PHI CHECK: Gap-edge energy ratio vs known phi values")
print("="*70)

# From the computation:
# tau=0.50: E_ferm/mode = 0.467230, E_bos/mode = 0.246502
# ratio = 1.8954

# But let me recompute precisely
ferm_gap_050 = 0.873214  # from output
bos_gap_050 = 0.243052

E_ferm = 0.5 * np.sqrt(ferm_gap_050)
E_bos = 0.5 * np.sqrt(bos_gap_050)
ratio = E_ferm / E_bos

print(f"\nGap-edge energy ratio at tau=0.50:")
print(f"  E_ferm/mode = 0.5 * sqrt({ferm_gap_050}) = {E_ferm:.8f}")
print(f"  E_bos/mode  = 0.5 * sqrt({bos_gap_050}) = {E_bos:.8f}")
print(f"  Ratio = {ratio:.8f}")

print(f"\nCompare to phi values:")
print(f"  phi_golden    = {phi_golden:.8f}")
print(f"  phi_golden^(3/2) = {phi_golden**1.5:.8f}")
print(f"  phi_paasch    = {phi_paasch:.8f}")
print(f"  phi_paasch^(3/2) = {phi_paasch**1.5:.8f}")
print(f"  sqrt(ferm/bos eigenvalue) = sqrt({ferm_gap_050}/{bos_gap_050}) = {np.sqrt(ferm_gap_050/bos_gap_050):.8f}")

# The ratio is really sqrt(lambda_ferm / lambda_bos)
r_eig = ferm_gap_050 / bos_gap_050
print(f"\n  lambda_ferm / lambda_bos = {r_eig:.8f}")
print(f"  sqrt(ratio) = {np.sqrt(r_eig):.8f}")

print(f"\n  Ratio vs phi_paasch^(3/2) = {phi_paasch**1.5:.6f}")
print(f"  Actual ratio             = {ratio:.6f}")
print(f"  Match: {abs(ratio - phi_paasch**1.5)/phi_paasch**1.5*100:.3f}% off")

# Now check at all tau values
print("\n" + "="*70)
print("RATIO AT ALL AVAILABLE TAU VALUES")
print("="*70)

# From the output data
data = [
    (0.00, 0.833333, 0.444444),
    (0.15, 0.832, 0.369216),  # approximate ferm gap from output
    (0.30, 0.822148, 0.307918),
    (0.50, 0.873214, 0.243052),
]

# More precise: reload and compute directly
ferm_data = np.load('s19a_sweep_data.npz', allow_pickle=True)
bos_data = np.load('kk1_bosonic_spectrum.npz', allow_pickle=True)

tau_ferm = ferm_data['tau_values']
bos_tau_keys = sorted([k for k in bos_data.keys()])
bos_taus = [float(k.split('_')[1]) for k in bos_tau_keys]

print(f"\n  {'tau':>5s} | {'ferm_gap':>10s} | {'bos_gap':>10s} | {'sqrt(f/b)':>10s} | {'phi_p^3/2':>10s} | {'match':>8s}")
print(f"  {'-'*5}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}-+-{'-'*8}")

for j, (tau, bkey) in enumerate(zip(bos_taus, bos_tau_keys)):
    # Fermionic gap
    fi = np.argmin(np.abs(tau_ferm - tau))
    eigs = ferm_data[f'eigenvalues_{fi}']
    fmult = ferm_data[f'fermionic_mult_{fi}']
    mask = (fmult > 0) & (np.abs(eigs) > 1e-12)
    fgap = np.min(np.abs(eigs[mask]))

    # Bosonic gap
    rec = bos_data[bkey]
    bgap = np.min(np.abs(rec['eigenvalue'][np.abs(rec['eigenvalue']) > 1e-12]))

    ratio = np.sqrt(fgap / bgap)
    pct = abs(ratio - phi_paasch**1.5) / phi_paasch**1.5 * 100

    print(f"  {tau:5.2f} | {fgap:10.6f} | {bgap:10.6f} | {ratio:10.6f} | {phi_paasch**1.5:10.6f} | {pct:6.2f}%")

# Also check: what IS phi_paasch^{3/2}?
print(f"\n  phi_paasch = {phi_paasch}")
print(f"  phi_paasch^(3/2) = {phi_paasch**1.5:.8f}")
print(f"  phi_paasch^(3/2) = phi_paasch * sqrt(phi_paasch) = {phi_paasch * np.sqrt(phi_paasch):.8f}")

# What about just at tau=0?
print(f"\n  At tau=0: sqrt(25/36 / 16/81) = sqrt(25*81 / 36*16)")
print(f"  = sqrt(2025/576) = sqrt({2025/576}) = {np.sqrt(2025/576):.8f}")
print(f"  = 45/24 = 15/8 = {15/8:.8f}")

# So at tau=0, the ratio is exactly 15/8 = 1.875
# phi_paasch^{3/2} = 1.8954
# Difference: (1.8954 - 1.875)/1.875 = 1.1%

print(f"\n  EXACT at tau=0: ratio = 15/8 = 1.875")
print(f"  phi_paasch^(3/2) = {phi_paasch**1.5:.6f}")
print(f"  Difference: {abs(15/8 - phi_paasch**1.5)/phi_paasch**1.5*100:.2f}%")

# What about the bosonic gap: is it exactly 4/9?
print(f"\n  Bosonic gap at tau=0: {0.444444:.8f}")
print(f"  4/9 = {4/9:.8f}")
print(f"  Match: {abs(0.444444 - 4/9):.2e}")
print(f"  So: ferm_gap/bos_gap = (5/6)/(4/9) = 45/24 = 15/8 exactly")
print(f"  sqrt(15/8) = {np.sqrt(15/8):.8f}")
print(f"  But the energy ratio is sqrt(ferm_gap)/sqrt(bos_gap) = sqrt(5/6)/sqrt(4/9)")
print(f"  = sqrt(5/6 * 9/4) = sqrt(45/24) = sqrt(15/8) = {np.sqrt(15/8):.8f}")
print(f"  = {np.sqrt(15/8):.8f}")

# Hmm, that's 1.3693, not 1.8954. Let me recheck.
# Energy = (1/2)*sqrt(eigenvalue)
# Ratio = sqrt(ferm_gap) / sqrt(bos_gap) = (ferm_gap/bos_gap)^{1/2}
# At tau=0: (5/6) / (4/9) = (5*9)/(6*4) = 45/24 = 15/8
# sqrt(15/8) = 1.3693

print(f"\n  CORRECTION: energy ratio = sqrt(lambda_f)/sqrt(lambda_b)")
print(f"  = sqrt(lambda_f/lambda_b) = sqrt(15/8) = {np.sqrt(15/8):.6f}")
print(f"  This matches the output: 1.3693")
print(f"  The 1.8954 number was ferm_gap/bos_gap directly (eigenvalue ratio)")
print(f"  phi_paasch^(3/2) comparison should be against eigenvalue ratio, not energy ratio")

# So: eigenvalue ratio at tau=0.50 = 0.873214/0.243052 = 3.5927
# sqrt of that = 1.8954 (energy ratio)
# phi_paasch^{3/2} = 1.8954

# WAIT. Let me be very precise.
print(f"\n" + "="*70)
print("PRECISE PHI CHECK")
print("="*70)
# Energy ratio = sqrt(ferm_gap) / sqrt(bos_gap)
# At tau=0.50: sqrt(0.873214) / sqrt(0.243052) = 0.93446 / 0.49301 = 1.8954

# phi_paasch = m(3,0)/m(0,0) at tau=0.15 = 1.531580
# phi_paasch^{3/2} = 1.531580^1.5

pp32 = 1.531580**1.5
print(f"  phi_paasch^(3/2) = 1.531580^1.5 = {pp32:.8f}")

# Let me recompute the tau=0.50 energy ratio precisely
fi = np.argmin(np.abs(tau_ferm - 0.50))
eigs = ferm_data[f'eigenvalues_{fi}']
fmult = ferm_data[f'fermionic_mult_{fi}']
mask = (fmult > 0) & (np.abs(eigs) > 1e-12)
fgap = np.min(np.abs(eigs[mask]))

rec = bos_data['s_0.5000']
bgap = np.min(np.abs(rec['eigenvalue'][np.abs(rec['eigenvalue']) > 1e-12]))

energy_ratio = np.sqrt(fgap) / np.sqrt(bgap)
eig_ratio = fgap / bgap

print(f"  ferm_gap(0.50) = {fgap:.10f}")
print(f"  bos_gap(0.50)  = {bgap:.10f}")
print(f"  eigenvalue ratio = {eig_ratio:.10f}")
print(f"  energy ratio     = {energy_ratio:.10f}")
print(f"  phi_paasch^(3/2) = {pp32:.10f}")
print(f"  Match (energy):  {abs(energy_ratio - pp32)/pp32*100:.4f}%")
print(f"  Match (eigval):  {abs(eig_ratio - pp32)/pp32*100:.4f}%")

# Check sqrt(eigenvalue ratio)
print(f"\n  sqrt(eig_ratio) = {np.sqrt(eig_ratio):.10f}")
print(f"  vs phi_paasch^(3/2) = {pp32:.10f}")
print(f"  Match: {abs(np.sqrt(eig_ratio) - pp32)/pp32*100:.4f}%")

# The energy ratio IS sqrt(eig_ratio), and THAT matches phi_paasch^{3/2}?
print(f"\n  So: sqrt(lambda_f(0.50)/lambda_b(0.50)) = phi_paasch^(3/2)?")
print(f"  {energy_ratio:.8f} vs {pp32:.8f}")
print(f"  Difference: {abs(energy_ratio - pp32):.6f}")
print(f"  This is {abs(energy_ratio - pp32)/pp32*100:.2f}% — {'MATCH' if abs(energy_ratio - pp32)/pp32 < 0.01 else 'NO MATCH'}")
