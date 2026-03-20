"""
CC-ARITH-37: Cosmological Constant from Spectral Action at the Fold
====================================================================
Einstein's computation, 15+ sessions in the making.

Computes V_vac(tau_fold) from the spectral action heat kernel expansion,
adds BCS condensation energy, and compares to Lambda_observed.

Pre-registered gate:
  R_CC < 10:  PASS
  10-60:      INTERESTING
  60-100:     NEUTRAL
  100-122:    SOFT FAIL
  > 122:      HARD FAIL

Secondary gate CC-GRADIENT-37: sign of dLambda_eff/dtau at fold.

Input data:
  - s36_sfull_tau_stabilization.npz (eigenvalues at multiple tau)
  - s36_multisector_ed.npz (E_BCS = -0.137)
  - s36_species_scale.npz (Lambda_sp/M_KK = 2.06)
"""

import numpy as np
from pathlib import Path

print("=" * 70)
print("CC-ARITH-37: Cosmological Constant from Spectral Action at the Fold")
print("=" * 70)

# ─── 1. Load data ───────────────────────────────────────────────────
data_dir = Path("tier0-computation")

stab = np.load(data_dir / "s36_sfull_tau_stabilization.npz", allow_pickle=True)
ed = np.load(data_dir / "s36_multisector_ed.npz", allow_pickle=True)
sp = np.load(data_dir / "s36_species_scale.npz", allow_pickle=True)

E_BCS = float(ed["E_cond_full"])  # -0.137
Lambda_sp_ratio = float(sp["x4_fold"])  # 2.06 (d=4 convention)
from canonical_constants import M_KK_gravity as M_KK  # 7.43e16 GeV (was 1e16)
from canonical_constants import M_Pl_reduced as M_P

print(f"\nE_BCS (8-mode ED) = {E_BCS:.6f}")
print(f"Lambda_sp / M_KK  = {Lambda_sp_ratio:.4f}")
print(f"M_KK = {M_KK:.1e} GeV")
print(f"M_P  = {M_P:.3e} GeV")

# ─── 2. Define sectors and multiplicities ───────────────────────────
sectors = [
    (0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2),
    (3, 0), (0, 3), (2, 1), (1, 2)
]

def dim_pq(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2

def mult_pq(p, q):
    """Peter-Weyl multiplicity = dim(p,q)^2."""
    return dim_pq(p, q) ** 2

print("\n─── Sector multiplicities ───")
total_modes_weighted = 0
for (p, q) in sectors:
    d = dim_pq(p, q)
    m = mult_pq(p, q)
    key = f"evals_tau0.190_{p}_{q}"
    n_evals = stab[key].shape[0]
    total_modes_weighted += m * n_evals
    print(f"  ({p},{q}): dim={d}, mult={m}, n_evals={n_evals}, weighted={m*n_evals}")
print(f"  Total weighted modes: {total_modes_weighted}")

# ─── 3. Compute heat kernel K(t) at multiple tau values ─────────────
tau_values = [0.180, 0.190, 0.210]  # fold + neighbors for gradient
tau_labels = ["0.180", "0.190", "0.210"]

# t grid for heat kernel
t_grid = np.logspace(-4, 2, 200)

results = {}

for tau_str in tau_labels:
    print(f"\n{'─' * 50}")
    print(f"Computing at tau = {tau_str}")
    print(f"{'─' * 50}")

    # Collect eigenvalues
    all_evals = {}
    total_bare_modes = 0
    for (p, q) in sectors:
        key = f"evals_tau{tau_str}_{p}_{q}"
        evals = stab[key]
        all_evals[(p, q)] = evals
        total_bare_modes += len(evals)

    # ── Method A: Direct spectral sums (moments) ────────────────
    # S_n = sum_{(p,q)} mult * sum_k |lambda_k|^n
    S0 = 0  # = a_0 (mode count)
    S1 = 0  # = sum |lambda|  (linear spectral action)
    S2 = 0  # ~ a_2 (related to scalar curvature)
    S4 = 0  # ~ a_4 (related to gauge kinetic terms)
    S6 = 0  # ~ a_6
    S8 = 0  # ~ a_8

    for (p, q) in sectors:
        evals = all_evals[(p, q)]
        m = mult_pq(p, q)
        abs_e = np.abs(evals)
        S0 += m * len(evals)
        S1 += m * np.sum(abs_e)
        S2 += m * np.sum(abs_e ** 2)
        S4 += m * np.sum(abs_e ** 4)
        S6 += m * np.sum(abs_e ** 6)
        S8 += m * np.sum(abs_e ** 8)

    print(f"\n  Direct spectral sums (Method A):")
    print(f"    S0 (mode count a_0) = {S0}")
    print(f"    S1 (linear SA)      = {S1:.4f}")
    print(f"    S2 (~ a_2)          = {S2:.4f}")
    print(f"    S4 (~ a_4)          = {S4:.4f}")
    print(f"    S6 (~ a_6)          = {S6:.4f}")
    print(f"    S8 (~ a_8)          = {S8:.4f}")

    # ── Method B: Heat kernel trace ─────────────────────────────
    K_trace = np.zeros_like(t_grid)
    for (p, q) in sectors:
        evals = all_evals[(p, q)]
        m = mult_pq(p, q)
        evals_sq = evals ** 2
        for i, t in enumerate(t_grid):
            K_trace[i] += m * np.sum(np.exp(-t * evals_sq))

    # Fit K(t) * t^4 = a_0 + a_2*t + a_4*t^2 + ... at small t
    # Use t < 0.05 for the fit
    mask = t_grid < 0.05
    t_fit = t_grid[mask]
    y_fit = K_trace[mask] * t_fit ** 4

    # Polynomial fit: y = a_0 + a_2*t + a_4*t^2
    coeffs = np.polyfit(t_fit, y_fit, 2)
    a4_hk = coeffs[0]
    a2_hk = coeffs[1]
    a0_hk = coeffs[2]

    print(f"\n  Heat kernel fit (Method B, K(t)*t^4 = a0 + a2*t + a4*t^2):")
    print(f"    a_0 (HK) = {a0_hk:.4f}  (vs direct S0 = {S0})")
    print(f"    a_2 (HK) = {a2_hk:.4f}  (vs direct S2 = {S2:.4f})")
    print(f"    a_4 (HK) = {a4_hk:.4f}  (vs direct S4 = {S4:.4f})")

    # ── Vacuum energy computation ────────────────────────────────
    # V_vac = f_4 * Lambda^4 * a_0 + f_2 * Lambda^2 * a_2 + f_0 * a_4
    # For sharp cutoff: f_4 = 1/2, f_2 = 1, f_0 = 1
    # For Gaussian (heat kernel): f_k = Gamma(k/2)
    #   f_4 = Gamma(2) = 1, f_2 = Gamma(1) = 1, f_0 = Gamma(0) -> diverges
    #   Use proper moments: f_4 = 1/2, f_2 = 1, f_0 = 1 (sharp cutoff)

    Lambda = Lambda_sp_ratio  # in M_KK units

    # Method A: use direct spectral sums as the Seeley-DeWitt coefficients
    # The spectral action Tr f(D^2/Lambda^2) with sharp cutoff gives:
    # SA = (Lambda^4/2) * a_0 + Lambda^2 * a_2 + a_4  (keeping only first 3 terms)
    # But a_0, a_2, a_4 in the Seeley-DeWitt expansion are NOT the same as S0, S2, S4
    # a_n are coefficients in K(t) ~ sum a_n t^{(n-d)/2}
    # For d=8: K(t) ~ a_0 t^{-4} + a_2 t^{-3} + a_4 t^{-2} + ...

    # The spectral action with sharp cutoff f = Theta(1-x):
    # Tr f(D^2/Lambda^2) = #{eigenvalues with |lambda| < Lambda}
    # This is just a mode count up to Lambda

    # For the vacuum energy, the relevant quantity is:
    # Tr f(D^2/Lambda^2) = sum f(lambda_k^2/Lambda^2)
    # With sharp cutoff: = #{|lambda_k| < Lambda} (weighted by mult)

    # Count modes below cutoff
    N_below = 0
    S1_below = 0
    S2_below = 0
    S4_below = 0
    N_total = 0
    for (p, q) in sectors:
        evals = all_evals[(p, q)]
        m = mult_pq(p, q)
        abs_e = np.abs(evals)
        below = abs_e < Lambda
        N_below += m * np.sum(below)
        S1_below += m * np.sum(abs_e[below])
        S2_below += m * np.sum(abs_e[below] ** 2)
        S4_below += m * np.sum(abs_e[below] ** 4)
        N_total += m * len(evals)

    print(f"\n  Mode counting with Lambda = {Lambda:.4f} M_KK:")
    print(f"    N_total (all modes)  = {N_total}")
    print(f"    N_below (|lam|<Lam)  = {N_below}")
    print(f"    Fraction below cutoff = {N_below/N_total:.4f}")
    print(f"    S1_below             = {S1_below:.4f}")
    print(f"    S2_below             = {S2_below:.4f}")
    print(f"    S4_below             = {S4_below:.4f}")

    # ── The CC from the spectral action ──────────────────────────
    # Method 1: V_vac from SD coefficients (HK fit) + sharp cutoff moments
    f4, f2, f0 = 0.5, 1.0, 1.0  # sharp cutoff moments
    V_sd = f4 * Lambda**4 * a0_hk + f2 * Lambda**2 * a2_hk + f0 * a4_hk

    # Method 2: Direct cutoff sum = Tr(1) for |lam| < Lambda
    # This counts modes, which is a_0-type contribution
    V_direct_count = N_below  # this IS the spectral action with f = Theta

    # Method 3: Full spectral action with cutoff
    # Tr f(D^2/Lambda^2) where f(x) = 1 for x<1, 0 otherwise
    # = sum_{|lam_k| < Lambda} 1 = N_below  (mode count)
    # For the VACUUM ENERGY, the relevant quantity is the spectral action VALUE
    # not the mode count. The spectral action IS the vacuum energy in NCG.
    # S_f = sum_k f(lam_k^2/Lambda^2) is a number.

    # More physically: with f(x) = exp(-x) (heat kernel regularization):
    V_gauss = 0
    for (p, q) in sectors:
        evals = all_evals[(p, q)]
        m = mult_pq(p, q)
        V_gauss += m * np.sum(np.exp(-evals**2 / Lambda**2))

    # With f(x) = (1-x)^2 Theta(1-x) (smooth compact support):
    V_smooth = 0
    for (p, q) in sectors:
        evals = all_evals[(p, q)]
        m = mult_pq(p, q)
        x = evals**2 / Lambda**2
        mask = x < 1
        V_smooth += m * np.sum((1 - x[mask])**2)

    print(f"\n  Vacuum energy V_vac (spectral action value, in spectral units):")
    print(f"    Method SD (HK coeffs):    V_sd     = {V_sd:.4f}")
    print(f"    Method sharp cutoff:      N_below  = {N_below}")
    print(f"    Method Gaussian:          V_gauss  = {V_gauss:.4f}")
    print(f"    Method smooth (1-x)^2:    V_smooth = {V_smooth:.4f}")

    # ── Add BCS condensation energy ──────────────────────────────
    for label, V in [("SD_HK", V_sd), ("sharp", float(N_below)),
                     ("Gaussian", V_gauss), ("smooth", V_smooth)]:
        Lambda_eff = V + E_BCS
        print(f"\n  {label}: V_vac = {V:.4f}, Lambda_eff = V + E_BCS = {Lambda_eff:.4f}")

    # Store results for this tau
    results[tau_str] = {
        "S0": S0, "S1": S1, "S2": S2, "S4": S4, "S6": S6, "S8": S8,
        "a0_hk": a0_hk, "a2_hk": a2_hk, "a4_hk": a4_hk,
        "N_below": N_below, "V_sd": V_sd, "V_gauss": V_gauss, "V_smooth": V_smooth,
        "K_trace": K_trace, "t_grid": t_grid
    }

# ─── 4. Physical units conversion ───────────────────────────────────
print("\n" + "=" * 70)
print("PHYSICAL UNITS CONVERSION")
print("=" * 70)

# Observed CC
from canonical_constants import Lambda_obs_MP4 as rho_obs_MP4  # in M_P^4 units
rho_obs_GeV4 = rho_obs_MP4 * M_P**4  # in GeV^4
print(f"\nObserved: rho_obs = {rho_obs_MP4:.3e} M_P^4")
print(f"        = {rho_obs_GeV4:.3e} GeV^4")

# Framework prediction
# rho_vac = Lambda_eff * M_KK^4 / (8 pi^2)
# The spectral action is dimensionless. The physical action is:
# S_phys = Tr f(D^2/Lambda^2) where D is in units of M_KK
# The vacuum energy density is rho = S_phys * M_KK^4 / Vol(M^4)
# For the CC, the relevant quantity is the 4D effective CC from the internal integral:
# Lambda_4D = (M_KK^4 / M_P^2) * Lambda_eff / (8 pi^2)  (from KK reduction)
# But more simply: rho_vac = Lambda_eff * M_KK^4 / (8*pi^2*Vol(K))
# The spectral action already integrates over the internal space,
# so: rho_vac ~ Lambda_eff * M_KK^4 (up to geometric prefactors)

# Let's be careful. The spectral action on M^4 x K gives:
# Tr f(D^2/Lambda^2) = integral_M4 L_eff(x) d^4x
# where L_eff contains the CC, EH, gauge terms
# The CC contribution is: L_CC = f_4 * Lambda^4 * a_0(K) / (4*pi^{d/2})
# where a_0(K) = rank(S) * Vol(K) / (4*pi)^{d/2}
# For d=8: L_CC = f_4 * Lambda^4 * a_0(K) / (4*pi^4)

# But our "Lambda_eff" is already the FULL sum including multiplicities.
# The spectral action value IS the dimensionless CC in units where M_KK = 1.
# Physical: rho_CC = Lambda_eff * M_KK^4 / (normalization)
# The normalization from Connes' spectral action (CCM eq 1.186):
# S = Tr f(D^2/Lambda^2) -> integral (f4*Lambda^4*a_0 + f2*Lambda^2*a_2 + f0*a_4 + ...)/(16*pi^2)
# But on the INTERNAL space alone, the spectral action value IS Lambda_eff.
# When we do the KK reduction, the 4D CC is:
# Lambda_4D = Lambda_eff * M_KK^4  (in natural units where 8*pi*G = M_P^{-2})
# More precisely: Lambda_4D / (8*pi*G) = rho_vac = Lambda_eff * M_KK^4 * prefactor

# For order-of-magnitude (which is what we need for R_CC):
prefactor = 1.0 / (16 * np.pi**2)  # standard spectral action normalization

tau_fold = "0.190"
r = results[tau_fold]

print(f"\n─── At fold tau = {tau_fold} ───")
print(f"{'Method':<20} {'V_vac':>12} {'V+E_BCS':>12} {'rho/rho_obs':>15} {'R_CC':>8} {'Verdict':<15}")
print("─" * 85)

for label, V_key in [("SD (HK fit)", "V_sd"), ("Sharp cutoff", "N_below"),
                      ("Gaussian", "V_gauss"), ("Smooth (1-x)^2", "V_smooth")]:
    V = r[V_key]
    if isinstance(V, np.integer):
        V = float(V)
    Leff = V + E_BCS

    # Physical vacuum energy
    rho_vac = abs(Leff) * prefactor * M_KK**4
    ratio = rho_vac / rho_obs_GeV4
    R_CC = np.log10(ratio) if ratio > 0 else -999

    if R_CC < 10:
        verdict = "PASS"
    elif R_CC < 60:
        verdict = "INTERESTING"
    elif R_CC < 100:
        verdict = "NEUTRAL"
    elif R_CC < 122:
        verdict = "SOFT FAIL"
    else:
        verdict = "HARD FAIL"

    print(f"{label:<20} {V:>12.4f} {Leff:>12.4f} {ratio:>15.4e} {R_CC:>8.2f} {verdict:<15}")

# ─── 5. CC Gradient (secondary gate) ────────────────────────────────
print("\n" + "=" * 70)
print("CC-GRADIENT-37: dLambda_eff/dtau at the fold")
print("=" * 70)

for label, V_key in [("SD (HK fit)", "V_sd"), ("Sharp cutoff", "N_below"),
                      ("Gaussian", "V_gauss"), ("Smooth (1-x)^2", "V_smooth")]:
    V_180 = results["0.180"][V_key]
    V_190 = results["0.190"][V_key]
    V_210 = results["0.210"][V_key]

    # Forward difference (0.190 -> 0.210, step = 0.020)
    dV_fwd = (float(V_210) - float(V_190)) / 0.020
    # Backward difference (0.180 -> 0.190, step = 0.010)
    dV_bwd = (float(V_190) - float(V_180)) / 0.010
    # Central estimate
    dV_cen = (float(V_210) - float(V_180)) / 0.030

    sign_str = "RESTORING (toward fold)" if dV_cen < 0 else "DESTABILIZING (away from fold)"
    print(f"\n  {label}:")
    print(f"    V(0.180) = {float(V_180):.4f}")
    print(f"    V(0.190) = {float(V_190):.4f}")
    print(f"    V(0.210) = {float(V_210):.4f}")
    print(f"    dV/dtau (fwd)     = {dV_fwd:+.4f}")
    print(f"    dV/dtau (bwd)     = {dV_bwd:+.4f}")
    print(f"    dV/dtau (central) = {dV_cen:+.4f}")
    print(f"    Sign: {sign_str}")

# ─── 6. Detailed breakdown of contributions ─────────────────────────
print("\n" + "=" * 70)
print("DETAILED BREAKDOWN AT FOLD (tau = 0.190)")
print("=" * 70)

r = results[tau_fold]
print(f"\nSeeley-DeWitt coefficients (from heat kernel fit):")
print(f"  a_0 = {r['a0_hk']:.6f}  (should ~ {r['S0']} = total weighted modes)")
print(f"  a_2 = {r['a2_hk']:.6f}")
print(f"  a_4 = {r['a4_hk']:.6f}")

Lambda = Lambda_sp_ratio
print(f"\nCutoff scale Lambda = {Lambda:.4f} M_KK")
print(f"  Lambda^4 = {Lambda**4:.4f}")
print(f"  Lambda^2 = {Lambda**2:.4f}")
print(f"\nSD expansion terms (f4=0.5, f2=1, f0=1):")
print(f"  f4 * Lam^4 * a_0 = {0.5 * Lambda**4 * r['a0_hk']:.4f}")
print(f"  f2 * Lam^2 * a_2 = {1.0 * Lambda**2 * r['a2_hk']:.4f}")
print(f"  f0 * a_4         = {1.0 * r['a4_hk']:.4f}")
print(f"  Sum = V_sd        = {r['V_sd']:.4f}")

# Per-sector breakdown
print(f"\nPer-sector contributions to S2 (curvature term):")
for (p, q) in sectors:
    key = f"evals_tau{tau_fold}_{p}_{q}"
    evals = stab[key]
    m = mult_pq(p, q)
    s2_sector = m * np.sum(evals**2)
    print(f"  ({p},{q}): mult={m:>6}, sum(lam^2)={np.sum(evals**2):>10.4f}, weighted={s2_sector:>12.4f}")

# ─── 7. BCS correction detail ───────────────────────────────────────
print(f"\nBCS condensation energy breakdown:")
print(f"  E_BCS (8-mode ED, full sector) = {E_BCS:.6f}")
print(f"  |E_BCS| / V_sd = {abs(E_BCS) / abs(r['V_sd']):.2e}")
print(f"  |E_BCS| / V_gauss = {abs(E_BCS) / abs(r['V_gauss']):.2e}")
print(f"  The BCS correction is {'NEGLIGIBLE' if abs(E_BCS/r['V_sd']) < 0.01 else 'SIGNIFICANT'} compared to V_vac")

# ─── 8. Save results ────────────────────────────────────────────────
np.savez(data_dir / "s36_cc_arithmetic.npz",
         # Spectral sums at fold
         S0=r['S0'], S1=r['S1'], S2=r['S2'], S4=r['S4'],
         S6=r['S6'], S8=r['S8'],
         # HK coefficients at fold
         a0_hk=r['a0_hk'], a2_hk=r['a2_hk'], a4_hk=r['a4_hk'],
         # Vacuum energies
         V_sd=r['V_sd'], V_gauss=r['V_gauss'], V_smooth=r['V_smooth'],
         N_below=r['N_below'],
         # BCS
         E_BCS=E_BCS,
         # Physical
         M_KK=M_KK, M_P=M_P, Lambda_sp_ratio=Lambda_sp_ratio,
         # Gate results
         tau_fold=0.190,
         # Gradient data
         V_sd_180=results["0.180"]["V_sd"],
         V_sd_190=results["0.190"]["V_sd"],
         V_sd_210=results["0.210"]["V_sd"],
         V_gauss_180=results["0.180"]["V_gauss"],
         V_gauss_190=results["0.190"]["V_gauss"],
         V_gauss_210=results["0.210"]["V_gauss"],
         )

print(f"\nResults saved to {data_dir / 's36_cc_arithmetic.npz'}")
print("\n" + "=" * 70)
print("CC-ARITH-37 COMPUTATION COMPLETE")
print("=" * 70)
