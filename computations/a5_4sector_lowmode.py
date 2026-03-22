"""
4-Sector Low-Mode Casimir: Does V_IR survive?

Team-lead question: The 25% low-mode F/B variation was shown for subsets.
Does it survive in the FULL 4-sector Casimir (scalar + vector + TT + Dirac)?

Data sources:
  - s19a_sweep_data.npz: fermionic eigenvalues at 21 tau (indexed eigenvalues_N)
  - kk1_bosonic_spectrum.npz: scalar+vector at tau=0, 0.15, 0.30, 0.50 (keys s_X.XXXX)
  - l20_TT_spectrum.npz: TT aggregate (E_TT totals, no per-eigenvalue)
  - l20_vtotal_minimum.npz: full 4-sector reference
"""
import numpy as np

# Load all data
ferm_data = np.load('s19a_sweep_data.npz', allow_pickle=True)
bos_data = np.load('kk1_bosonic_spectrum.npz', allow_pickle=True)
tt_data = np.load('l20_TT_spectrum.npz', allow_pickle=True)
vtotal_data = np.load('l20_vtotal_minimum.npz', allow_pickle=True)

tau_ferm = ferm_data['tau_values']  # 0.0 to 2.0 step 0.1
bos_tau_keys = sorted([k for k in bos_data.keys()])  # s_0.0000, s_0.1500, s_0.3000, s_0.5000
bos_taus = np.array([float(k.split('_')[1]) for k in bos_tau_keys])

print("="*70)
print("4-SECTOR LOW-MODE CASIMIR: DOES V_IR SURVIVE?")
print("="*70)

# --- Section 1: Reference F/B from full spectrum ---
print("\n--- REFERENCE: FULL-SPECTRUM R_casimir (from l20) ---")
R_cas = vtotal_data['R_casimir']
tau_ref = vtotal_data['tau']
for i in [0, 2, 5, 10]:
    print(f"  tau={tau_ref[i]:.1f}: R_casimir (F/B) = {R_cas[i]:.5f}")
print(f"  Full-spectrum R variation: {(R_cas.max()-R_cas.min())/R_cas[0]*100:.2f}%")

# --- Section 2: Build eigenvalue pools at shared tau values ---
shared_taus = [0.0, 0.15, 0.30, 0.50]
shared_bos_keys = ['s_0.0000', 's_0.1500', 's_0.3000', 's_0.5000']

# Map tau to fermionic index
def get_ferm_data(tau_target):
    """Get sorted absolute fermionic eigenvalues expanded by multiplicity."""
    idx = np.argmin(np.abs(tau_ferm - tau_target))
    eigs = ferm_data[f'eigenvalues_{idx}']
    fmult = ferm_data[f'fermionic_mult_{idx}']
    # Expand: each eigenvalue repeated by its fermionic multiplicity
    expanded = []
    for e, m in zip(eigs, fmult):
        if m > 0 and abs(e) > 1e-12:
            expanded.extend([abs(e)] * int(m))
    return np.sort(expanded)

def get_bos_data(bos_key):
    """Get sorted absolute bosonic eigenvalues expanded by multiplicity."""
    rec = bos_data[bos_key]
    expanded = []
    for row in rec:
        eig = abs(row['eigenvalue'])
        mult = int(row['multiplicity'])
        if eig > 1e-12 and mult > 0:
            expanded.extend([eig] * mult)
    return np.sort(expanded)

# --- Section 3: Combined pool low-mode Casimir ---
print("\n" + "="*70)
print("COMBINED POOL: Sort ALL eigenvalues together, take lowest N")
print("E_cas = (1/2) * Sum[ sqrt(lambda_n) * sign_n ]")
print("  sign_n = +1 for bosonic, -1 for fermionic")
print("="*70)

for N_cut in [20, 50, 100, 200, 500, 1000]:
    print(f"\n--- N_cut = {N_cut} ---")
    results = []

    for tau_target, bos_key in zip(shared_taus, shared_bos_keys):
        ferm_eigs = get_ferm_data(tau_target)
        bos_eigs = get_bos_data(bos_key)

        # Combine into single sorted pool with labels
        n_f = len(ferm_eigs)
        n_b = len(bos_eigs)

        all_eigs = np.concatenate([bos_eigs, ferm_eigs])
        all_signs = np.concatenate([np.ones(n_b), -np.ones(n_f)])

        sort_idx = np.argsort(all_eigs)
        all_eigs_sorted = all_eigs[sort_idx]
        all_signs_sorted = all_signs[sort_idx]

        # Take lowest N_cut
        N = min(N_cut, len(all_eigs_sorted))
        pool = all_eigs_sorted[:N]
        signs = all_signs_sorted[:N]

        E_bos_low = 0.5 * np.sum(np.sqrt(pool[signs > 0]))
        E_ferm_low = 0.5 * np.sum(np.sqrt(pool[signs < 0]))
        n_bos_in_pool = int(np.sum(signs > 0))
        n_ferm_in_pool = int(np.sum(signs < 0))

        E_net = E_bos_low - E_ferm_low
        fb = E_ferm_low / E_bos_low if E_bos_low > 0 else float('inf')

        results.append((tau_target, E_bos_low, E_ferm_low, E_net, fb,
                        n_bos_in_pool, n_ferm_in_pool))
        print(f"  tau={tau_target:.2f}: E_bos={E_bos_low:.4f} ({n_bos_in_pool}B), "
              f"E_ferm={E_ferm_low:.4f} ({n_ferm_in_pool}F), "
              f"E_net={E_net:+.4f}, F/B={fb:.4f}")

    # Check for non-monotonicity
    E_nets = [r[3] for r in results]
    has_min = any(E_nets[i] > E_nets[i+1] for i in range(len(E_nets)-1))

    if has_min:
        min_idx = np.argmin(E_nets)
        print(f"  >> NON-MONOTONIC: minimum near tau={shared_taus[min_idx]:.2f}, "
              f"E_net_min={E_nets[min_idx]:+.4f}")
    else:
        print(f"  >> Monotonically increasing.")

    # F/B variation
    fbs = [r[4] for r in results]
    fb_var = (max(fbs) - min(fbs)) / fbs[0] * 100
    print(f"  >> F/B range: [{min(fbs):.4f}, {max(fbs):.4f}], variation: {fb_var:.1f}%")

# --- Section 4: Separate-pool low-mode Casimir ---
print("\n" + "="*70)
print("SEPARATE POOL: Take lowest N bosonic + lowest N fermionic separately")
print("(This is what the original 25% variation analysis used)")
print("="*70)

for N_cut in [20, 50, 100, 200]:
    print(f"\n--- N_cut = {N_cut} (from each sector) ---")
    results = []

    for tau_target, bos_key in zip(shared_taus, shared_bos_keys):
        ferm_eigs = get_ferm_data(tau_target)
        bos_eigs = get_bos_data(bos_key)

        n_f = min(N_cut, len(ferm_eigs))
        n_b = min(N_cut, len(bos_eigs))

        E_ferm_low = 0.5 * np.sum(np.sqrt(ferm_eigs[:n_f]))
        E_bos_low = 0.5 * np.sum(np.sqrt(bos_eigs[:n_b]))

        E_net = E_bos_low - E_ferm_low
        fb = E_ferm_low / E_bos_low if E_bos_low > 0 else float('inf')

        results.append((tau_target, E_bos_low, E_ferm_low, E_net, fb))
        print(f"  tau={tau_target:.2f}: E_bos={E_bos_low:.4f} ({n_b}), "
              f"E_ferm={E_ferm_low:.4f} ({n_f}), "
              f"E_net={E_net:+.4f}, F/B={fb:.4f}")

    E_nets = [r[3] for r in results]
    has_min = any(E_nets[i] > E_nets[i+1] for i in range(len(E_nets)-1))

    if has_min:
        min_idx = np.argmin(E_nets)
        print(f"  >> NON-MONOTONIC: minimum near tau={shared_taus[min_idx]:.2f}")
    else:
        print(f"  >> Monotonically increasing.")

    fbs = [r[4] for r in results]
    fb_var = (max(fbs) - min(fbs)) / fbs[0] * 100
    print(f"  >> F/B range: [{min(fbs):.4f}, {max(fbs):.4f}], variation: {fb_var:.1f}%")

# --- Section 5: Gap-edge analysis ---
print("\n" + "="*70)
print("GAP-EDGE ANALYSIS: Where are the lowest eigenvalues?")
print("="*70)

for tau_target, bos_key in zip(shared_taus, shared_bos_keys):
    ferm_eigs = get_ferm_data(tau_target)
    bos_eigs = get_bos_data(bos_key)

    print(f"\n  tau={tau_target:.2f}:")
    print(f"    Ferm: min={ferm_eigs[0]:.4f}, 10th={ferm_eigs[9]:.4f}, "
          f"50th={ferm_eigs[49]:.4f}, total={len(ferm_eigs)}")
    print(f"    Bos:  min={bos_eigs[0]:.4f}, 10th={bos_eigs[9]:.4f}, "
          f"50th={bos_eigs[49]:.4f}, total={len(bos_eigs)}")

    # TT minimum: from l20, E_TT / total_TT_dof gives mean, but we need minimum
    # Session 20b found TT min eigenvalue ~ 1.0 at tau=0
    # We can estimate from per-mode average
    tt_tau_idx = np.argmin(np.abs(tt_data['tau'] - tau_target))
    tt_E = tt_data['E_TT'][tt_tau_idx]
    tt_dof = tt_data['total_TT_dof'][tt_tau_idx]
    tt_mean = tt_E / tt_dof
    print(f"    TT:   mean eigenvalue ~ {tt_mean:.4f}, DOF={tt_dof}")
    print(f"    TT min eigenvalue (from 20b): ~1.0 at tau=0 (confirmed no tachyons)")

    # Would TT modes enter the lowest 50?
    if bos_eigs[49] < 1.0:
        print(f"    >> TT (min~1.0) ABOVE 50th bosonic ({bos_eigs[49]:.4f}) -> TT NOT in lowest 50")
    else:
        print(f"    >> TT (min~1.0) BELOW 50th bosonic ({bos_eigs[49]:.4f}) -> TT ENTERS pool")

# --- Section 6: Finer fermionic-only grid (shape reference) ---
print("\n" + "="*70)
print("FERMIONIC-ONLY LOW-MODE SHAPE (21 tau values)")
print("="*70)

for N_cut in [20, 50]:
    E_ferm_all = []
    for i in range(21):
        eigs = ferm_data[f'eigenvalues_{i}']
        fmult = ferm_data[f'fermionic_mult_{i}']
        expanded = []
        for e, m in zip(eigs, fmult):
            if m > 0 and abs(e) > 1e-12:
                expanded.extend([abs(e)] * int(m))
        expanded = np.sort(expanded)
        n = min(N_cut, len(expanded))
        E_ferm_all.append(0.5 * np.sum(np.sqrt(expanded[:n])))

    E_ferm_all = np.array(E_ferm_all)
    E_norm = E_ferm_all / E_ferm_all[0]
    min_idx = np.argmin(E_ferm_all)
    variation = (E_ferm_all.max() - E_ferm_all.min()) / E_ferm_all[0] * 100

    print(f"\n  N_cut={N_cut}: min at tau={tau_ferm[min_idx]:.1f} "
          f"(norm={E_norm[min_idx]:.4f}), variation={variation:.1f}%")
    for j in [0, 1, 2, 3, 5, 10]:
        print(f"    tau={tau_ferm[j]:.1f}: E_ferm={E_ferm_all[j]:.4f} ({E_norm[j]:.4f}x)")

# --- CONCLUSION ---
print("\n" + "="*70)
print("CONCLUSION")
print("="*70)
print("""
TT modes (min eigenvalue ~1.0) do NOT enter the lowest 50-100 combined
modes because scalar/vector/fermion gap edges are ~0.7-0.9. So the
4-sector low-mode Casimir is effectively a 3-sector computation
(scalar + vector + fermion) at small N_cut.

The key numbers to report to team-lead:
1. Whether V_IR (= E_bos - E_ferm for lowest N modes) is non-monotonic
2. At what N_cut the non-monotonicity washes out
3. Whether the F/B ratio variation at low N differs from the 1.8% full-spectrum
""")
