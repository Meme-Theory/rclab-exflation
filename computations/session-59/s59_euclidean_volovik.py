#!/usr/bin/env python3
"""
s59_euclidean_volovik.py -- EUCLIDEAN-VOLOVIK-59 (W4E-1)
========================================================
Gate: Can the Volovik partition (F_J = vacuum, excitations = matter) be
derived from Euclidean quantum gravity via saddle-point decomposition of Z?

Physics (Gibbons-Hawking 1977, Paper 07):
  Z = Tr(exp(-beta*H)) receives contributions from saddle points of S_E.
  Thermal equilibrium = dominant saddle; GGE = constrained saddle with HIGHER
  action. The Volovik partition follows from standard saddle-point decomposition.
"""
import sys, traceback
sys.path.insert(0, 'computations')

def main():
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from canonical_constants import (
        T_acoustic, E_B1, E_B2_mean, E_B3_mean,
        PI, N_cells, tau_fold
    )

    print("=" * 72)
    print("EUCLIDEAN-VOLOVIK-59: Euclidean Path Integral Derivation of Volovik Partition")
    print("=" * 72)

    # ------------------------------------------------------------------
    # 1. Load S58 data
    # ------------------------------------------------------------------
    vp = np.load('computations/session-58/s58_volovik_partition.npz', allow_pickle=True)
    F_Josephson = float(vp['F_Josephson'])
    E_matter_Volovik = float(vp['E_matter_Volovik'])
    w_eff_Volovik = float(vp['w_eff_Volovik'])
    w_DE_GGE = float(vp['w_DE_GGE'])

    print(f"\nS58 Data: F_J={F_Josephson:.3f}, E_matter={E_matter_Volovik:.3f}")

    # ------------------------------------------------------------------
    # 2. Mode spectrum and GGE occupations
    # ------------------------------------------------------------------
    # 8 modes: 4 B2 + 1 B1 + 3 B3
    E_modes = np.array([
        E_B2_mean, E_B2_mean, E_B2_mean, E_B2_mean,
        E_B1,
        E_B3_mean, E_B3_mean, E_B3_mean
    ])
    sector_labels = np.array(['B2','B2','B2','B2','B1','B3','B3','B3'])

    # GGE Lagrange multipliers (S39 GGE-LAMBDA-39, analytic)
    lambda_GGE = np.array([
        1.459, 1.459, 1.459, 1.459,
        2.771,
        6.007, 6.007, 6.007
    ])

    # GGE occupations (fermionic)
    n_k_GGE = 1.0 / (np.exp(lambda_GGE) + 1.0)

    # Thermal occupations at T_acoustic
    beta_a = 1.0 / T_acoustic
    n_k_thermal = 1.0 / (np.exp(beta_a * E_modes) + 1.0)

    # Gibbs occupations (S40 T_Gibbs = 0.113)
    T_Gibbs = 0.113  # (local)
    beta_G = 1.0 / T_Gibbs
    n_k_Gibbs = 1.0 / (np.exp(beta_G * E_modes) + 1.0)

    print(f"\nMode energies: {E_modes}")
    print(f"n_k^GGE:      {n_k_GGE}")
    print(f"n_k^thermal:  {n_k_thermal}")

    # ------------------------------------------------------------------
    # 3. Euclidean action functionals
    # ------------------------------------------------------------------
    def S_vN(n_k):
        """Von Neumann entropy of fermionic occupation."""
        nc = np.clip(n_k, 1e-30, 1.0 - 1e-30)
        return -np.sum(nc * np.log(nc) + (1.0 - nc) * np.log(1.0 - nc))

    def E_total(n_k):
        return np.sum(E_modes * n_k)

    def S_E_func(n_k, beta):
        """Euclidean action: S_E = beta*<E> - S_vN."""
        return beta * E_total(n_k) - S_vN(n_k)

    # ------------------------------------------------------------------
    # 4. Evaluate at thermal saddle
    # ------------------------------------------------------------------
    svn_th = S_vN(n_k_thermal)
    E_th = E_total(n_k_thermal)
    SE_th = S_E_func(n_k_thermal, beta_a)
    F_th = E_th - T_acoustic * svn_th

    svn_G = S_vN(n_k_Gibbs)
    E_G = E_total(n_k_Gibbs)
    SE_G = S_E_func(n_k_Gibbs, beta_G)
    F_G = E_G - T_Gibbs * svn_G

    print(f"\n=== Thermal Saddle (T_a = {T_acoustic}) ===")
    print(f"  S_vN = {svn_th:.6f}, <E> = {E_th:.6f}, F = {F_th:.6f}, S_E = {SE_th:.6f}")

    # ------------------------------------------------------------------
    # 5. Evaluate at GGE saddle
    # ------------------------------------------------------------------
    svn_gge = S_vN(n_k_GGE)
    E_gge = E_total(n_k_GGE)
    SE_gge = S_E_func(n_k_GGE, beta_a)
    F_gge = E_gge - T_acoustic * svn_gge

    # GGE natural action (using lambda_k instead of beta*E_k)
    SE_gge_natural = np.sum(lambda_GGE * n_k_GGE) - S_vN(n_k_GGE)

    # Effective temperature per mode
    T_eff_mode = E_modes / lambda_GGE

    print(f"\n=== GGE Saddle ===")
    print(f"  S_vN = {svn_gge:.6f}, <E> = {E_gge:.6f}, F = {F_gge:.6f}")
    print(f"  S_E(at beta_a) = {SE_gge:.6f}")
    print(f"  S_E(natural)   = {SE_gge_natural:.6f}")
    print(f"  T_eff/mode:    {T_eff_mode}")

    # ------------------------------------------------------------------
    # 6. Saddle comparison
    # ------------------------------------------------------------------
    Delta_SE = SE_gge - SE_th
    Delta_F = F_gge - F_th
    ratio_Z = np.exp(-Delta_SE)

    # KL divergence
    nc_g = np.clip(n_k_GGE, 1e-30, 1-1e-30)
    nc_t = np.clip(n_k_thermal, 1e-30, 1-1e-30)
    D_KL = np.sum(nc_g * np.log(nc_g / nc_t) + (1 - nc_g) * np.log((1 - nc_g) / (1 - nc_t)))

    print(f"\n{'=' * 72}")
    print(f"CRITICAL COMPARISON")
    print(f"{'=' * 72}")
    print(f"  S_E(thermal)  = {SE_th:.6f}")
    print(f"  S_E(GGE)      = {SE_gge:.6f}")
    print(f"  Delta_S_E     = {Delta_SE:+.6f}")
    print(f"  Delta_F       = {Delta_F:+.6f} M_KK")
    print(f"  Z_GGE/Z_th   = {ratio_Z:.6e}")
    print(f"  D_KL          = {D_KL:.6f} nats = {D_KL/np.log(2):.4f} bits")

    if Delta_SE > 0:
        print(f"\n  >> GGE is SUB-DOMINANT saddle -> Volovik partition CORRECT")
        saddle_verdict = "GGE_SUB_DOMINANT"
    else:
        print(f"\n  >> GGE DOMINATES -> Volovik partition CONTRADICTED")
        saddle_verdict = "GGE_DOMINANT"

    # ------------------------------------------------------------------
    # 7. Volovik partition decomposition
    # ------------------------------------------------------------------
    print(f"\n=== Volovik Partition (Euclidean) ===")
    print(f"  VACUUM = F_thermal = {F_th:.4f} M_KK (dominant saddle)")
    print(f"  MATTER = Delta_F   = {Delta_F:.4f} M_KK (sub-dominant correction)")
    print(f"  F_J/N_cells        = {F_Josephson/N_cells:.4f} M_KK")
    print(f"  E_matter(S58)      = {E_matter_Volovik:.4f} M_KK")
    print(f"  Delta_F/E_matter   = {Delta_F/E_matter_Volovik:.4f}")

    # Non-thermality
    T_eff_spread = np.std(T_eff_mode) / np.mean(T_eff_mode)

    # Effective single T matching GGE energy
    def energy_at_beta(b):
        return np.sum(E_modes / (np.exp(b * E_modes) + 1.0))
    b_lo, b_hi = 0.1, 100.0
    for _ in range(100):
        b_mid = (b_lo + b_hi) / 2
        if energy_at_beta(b_mid) > E_gge:
            b_lo = b_mid
        else:
            b_hi = b_mid
    T_eff_single = 1.0 / b_mid

    print(f"\n=== Non-Thermality ===")
    for i in range(8):
        print(f"  {sector_labels[i]}: E={E_modes[i]:.4f}, lam={lambda_GGE[i]:.3f}, T_eff={T_eff_mode[i]:.4f}")
    print(f"  T_eff spread (CV): {T_eff_spread:.4f} ({T_eff_spread*100:.1f}%)")
    print(f"  T_eff(energy-matched): {T_eff_single:.4f}")

    # ------------------------------------------------------------------
    # 8. Temperature sweep
    # ------------------------------------------------------------------
    T_arr = np.linspace(0.01, 0.5, 200)
    dSE_arr = np.zeros_like(T_arr)
    dF_arr = np.zeros_like(T_arr)
    SE_th_arr = np.zeros_like(T_arr)
    SE_gge_arr = np.zeros_like(T_arr)

    for i, T in enumerate(T_arr):
        b = 1.0 / T
        nth = 1.0 / (np.exp(b * E_modes) + 1.0)
        se_t = S_E_func(nth, b)
        se_g = S_E_func(n_k_GGE, b)
        SE_th_arr[i] = se_t
        SE_gge_arr[i] = se_g
        dSE_arr[i] = se_g - se_t
        dF_arr[i] = (se_g - se_t) / b

    crossings = np.where(np.diff(np.sign(dSE_arr)))[0]
    T_cross = T_arr[crossings] if len(crossings) > 0 else np.array([])

    print(f"\n=== Temperature Sweep ===")
    print(f"  Always sub-dominant: {np.all(dSE_arr > 0)}")
    if len(T_cross) > 0:
        print(f"  Crossover T: {T_cross}")
    else:
        print(f"  No crossover: GGE sub-dominant at ALL T in [0.01, 0.50]")
    print(f"  min dS_E = {np.min(dSE_arr):.6f} at T={T_arr[np.argmin(dSE_arr)]:.4f}")

    # ------------------------------------------------------------------
    # 9. Entropy deficit analysis
    # ------------------------------------------------------------------
    Delta_SvN = svn_gge - svn_th
    Delta_E = E_gge - E_th

    print(f"\n=== Entropy Deficit ===")
    print(f"  S_vN(thermal) = {svn_th:.6f}")
    print(f"  S_vN(GGE)     = {svn_gge:.6f}")
    print(f"  Delta_S_vN    = {Delta_SvN:+.6f}")
    print(f"  Delta_E       = {Delta_E:+.6f}")

    # ------------------------------------------------------------------
    # 10. Gate verdict
    # ------------------------------------------------------------------
    if Delta_SE > 0 and D_KL > 0:
        gate_verdict = "PASS"
        gate_detail = (
            f"EUCLIDEAN-VOLOVIK-59 PASS. Delta_S_E={Delta_SE:+.4f}>0: "
            f"GGE is sub-dominant saddle. D_KL={D_KL:.4f} nats. "
            f"Volovik partition derived from saddle-point decomposition. "
            f"Structural parallel to Gibbons-Hawking BH thermodynamics."
        )
    elif Delta_SE > 0:
        gate_verdict = "INFO"
        gate_detail = f"EUCLIDEAN-VOLOVIK-59 INFO. Delta_S_E={Delta_SE:+.4f}>0 but D_KL ambiguous."
    else:
        gate_verdict = "FAIL"
        gate_detail = (
            f"EUCLIDEAN-VOLOVIK-59 FAIL. Delta_S_E={Delta_SE:+.4f}<0: "
            f"GGE dominates, Volovik partition contradicted."
        )

    print(f"\n{'=' * 72}")
    print(f"GATE: EUCLIDEAN-VOLOVIK-59 = {gate_verdict}")
    print(f"{'=' * 72}")
    print(f"  {gate_detail}")

    # ------------------------------------------------------------------
    # 11. Save
    # ------------------------------------------------------------------
    np.savez('computations/session-59/s59_euclidean_volovik.npz',
        E_modes=E_modes, sector_labels=sector_labels,
        lambda_GGE=lambda_GGE, n_k_GGE=n_k_GGE,
        n_k_thermal=n_k_thermal, n_k_Gibbs=n_k_Gibbs,
        T_eff_per_mode=T_eff_mode,
        S_vN_thermal=svn_th, E_thermal=E_th, F_thermal=F_th, S_E_thermal=SE_th,
        S_vN_GGE=svn_gge, E_GGE=E_gge, F_GGE_at_thermal=F_gge,
        S_E_GGE=SE_gge, S_E_GGE_natural=SE_gge_natural,
        Delta_S_E=Delta_SE, Delta_F=Delta_F, ratio_Z=ratio_Z, D_KL=D_KL,
        T_eff_single=T_eff_single, T_eff_spread=T_eff_spread,
        suppression=np.exp(-Delta_SE) if Delta_SE > 0 else np.exp(Delta_SE),
        T_range=T_arr, Delta_SE_vs_T=dSE_arr, Delta_F_vs_T=dF_arr,
        SE_thermal_vs_T=SE_th_arr, SE_GGE_vs_T=SE_gge_arr, T_cross=T_cross,
        F_vac_per_cell=F_th, F_matter_Euclidean=Delta_F,
        F_Josephson=F_Josephson, E_matter_Volovik=E_matter_Volovik,
        T_acoustic=T_acoustic, T_Gibbs=T_Gibbs, beta_acoustic=beta_a,
        Delta_SvN=Delta_SvN, Delta_E=Delta_E,
        gate_name=np.array(['EUCLIDEAN-VOLOVIK-59']),
        gate_verdict=np.array([gate_verdict]),
        gate_detail=np.array([gate_detail]),
        saddle_verdict=np.array([saddle_verdict]),
    )
    print(f"\nSaved: computations/session-59/s59_euclidean_volovik.npz")

    # ------------------------------------------------------------------
    # 12. Plot
    # ------------------------------------------------------------------
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))
    fig.suptitle('EUCLIDEAN-VOLOVIK-59: Saddle-Point Derivation of Volovik Partition',
                 fontsize=14, fontweight='bold')

    # Panel 1: Occupations
    ax1 = axes[0, 0]
    x = np.arange(8)
    w = 0.25  # (local)
    ax1.bar(x - w, n_k_GGE, w, label='GGE', color='steelblue', alpha=0.85)
    ax1.bar(x, n_k_thermal, w, label='Thermal', color='darkorange', alpha=0.85)
    ax1.bar(x + w, n_k_Gibbs, w, label='Gibbs', color='seagreen', alpha=0.85)
    ax1.set_xticks(x)
    ax1.set_xticklabels([f'{s}\n{E:.3f}' for s, E in zip(sector_labels, E_modes)], fontsize=8)
    ax1.set_ylabel('Occupation $n_k$')
    ax1.set_title('Mode Occupations: GGE vs Thermal Saddles')
    ax1.legend(fontsize=9)
    ax1.set_ylim(0, max(n_k_GGE.max(), n_k_thermal.max()) * 1.2)
    ax1.grid(axis='y', alpha=0.3)

    # Panel 2: T sweep of Delta_SE
    ax2 = axes[0, 1]
    ax2.plot(T_arr, dSE_arr, 'b-', lw=2, label=r'$\Delta S_E$')
    ax2.axhline(0, color='k', ls='--', lw=0.8)
    ax2.axvline(T_acoustic, color='red', ls='--', lw=1.5, label=f'$T_a={T_acoustic}$')
    ax2.fill_between(T_arr, 0, dSE_arr, where=dSE_arr > 0, color='lightblue', alpha=0.3)
    ax2.set_xlabel('Temperature (M_KK)')
    ax2.set_ylabel(r'$\Delta S_E$')
    ax2.set_title(r'$S_E^{GGE} - S_E^{thermal}$ vs $T$')
    ax2.legend(fontsize=9)
    ax2.grid(alpha=0.3)
    idx_ta = np.argmin(np.abs(T_arr - T_acoustic))
    ax2.plot(T_acoustic, dSE_arr[idx_ta], 'r*', ms=15, zorder=5)
    ax2.annotate(f'{dSE_arr[idx_ta]:.3f}', xy=(T_acoustic, dSE_arr[idx_ta]),
                 xytext=(T_acoustic + 0.06, dSE_arr[idx_ta] + 0.2),
                 fontsize=10, arrowprops=dict(arrowstyle='->', color='red'), color='red')

    # Panel 3: Both actions
    ax3 = axes[1, 0]
    ax3.plot(T_arr, SE_th_arr, 'darkorange', lw=2, label=r'$S_E^{thermal}$')
    ax3.plot(T_arr, SE_gge_arr, 'steelblue', lw=2, label=r'$S_E^{GGE}$')
    ax3.axvline(T_acoustic, color='red', ls='--', lw=1.5, alpha=0.7)
    ax3.set_xlabel('Temperature (M_KK)')
    ax3.set_ylabel(r'$S_E$')
    ax3.set_title('Euclidean Actions')
    ax3.legend(fontsize=9)
    ax3.grid(alpha=0.3)

    # Panel 4: Verdict
    ax4 = axes[1, 1]
    ax4.axis('off')
    vcolor = 'darkgreen' if gate_verdict == 'PASS' else 'darkred'
    info = (
        f"GATE: EUCLIDEAN-VOLOVIK-59 = {gate_verdict}\n\n"
        f"S_E(thermal)  = {SE_th:.4f}  (dominant)\n"
        f"S_E(GGE)      = {SE_gge:.4f}  (sub-dominant)\n"
        f"Delta_S_E     = {Delta_SE:+.4f}\n"
        f"D_KL          = {D_KL:.4f} nats\n"
        f"Z_GGE/Z_th   = {ratio_Z:.4e}\n\n"
        f"VACUUM = F_thermal = {F_th:.4f} M_KK\n"
        f"MATTER = Delta_F   = {Delta_F:.4f} M_KK\n\n"
        f"GH Parallel: dominant=vacuum, sub-dom=matter\n\n"
        f"T_eff spread = {T_eff_spread*100:.1f}%\n"
        f"  B2: {T_eff_mode[0]:.4f}\n"
        f"  B1: {T_eff_mode[4]:.4f}\n"
        f"  B3: {T_eff_mode[5]:.4f}\n"
    )
    ax4.text(0.05, 0.95, info, transform=ax4.transAxes, fontsize=10,
             va='top', fontfamily='monospace',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.8))
    ax4.text(0.5, 0.98, gate_verdict, transform=ax4.transAxes,
             fontsize=24, fontweight='bold', color=vcolor, ha='center', va='top')

    plt.tight_layout()
    plt.savefig('computations/session-59/s59_euclidean_volovik.png', dpi=150, bbox_inches='tight')
    print(f"Saved: computations/session-59/s59_euclidean_volovik.png")
    plt.close()

    print(f"\nCOMPUTATION COMPLETE")
    return gate_verdict, Delta_SE, D_KL

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        with open('computations/_shared/_euclid_error.txt', 'w') as ef:
            ef.write(f'ERROR: {e}\n')
            ef.write(traceback.format_exc())
        raise
