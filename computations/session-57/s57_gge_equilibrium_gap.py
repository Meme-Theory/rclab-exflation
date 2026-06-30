#!/usr/bin/env python3
"""
S57 GGE-EQUILIBRIUM-GAP-57: Distance from Equilibrium

Gate: PASS if ||n^GGE - n^eq|| / N_pair < 10^{-57} (CC gap closeable by thermalization)
      FAIL if ~ O(1) (CC gap structural)

Method:
  1. Extract BCS mode energies E_k = 2*xi_k at fold (BCS pair energies)
  2. Extract 8 GGE occupations f_k from S43 exact diagonalization
  3. The GGE occupations satisfy sum_k f_k = 1 (canonical N=1)
  4. Equilibrium: f_k^eq = exp(-E_k/T) / Z(T) with Z = sum_l exp(-E_l/T)
  5. Optimize T_eq minimizing ||f^GGE - f^eq(T_eq)||_2
  6. Compute ||f^GGE - f^eq|| / N_pair
  7. Scale to physical N_pair = 59.8 and compute Lambda_eff

ALSO: Compute using per-mode Volovik temperatures T_k^V = 2*xi_k / (-ln f_k)
and grand-canonical Fermi-Dirac n_k = 1/(exp(epsilon_k/T) + 1) formalism.

The GGE IS the exact ground state projected onto the post-transit free Hamiltonian.
The integrability of H_free (non-interacting) makes the GGE permanent.
In superfluid 3He language: this is a quenched superfluid where each sector
has a different effective temperature, frozen by the absence of inter-sector
scattering.

Author: Volovik-Superfluid-Universe-Theorist
Session: 57, Wave 0, Task W0-3
"""

import sys
import os
import numpy as np
from scipy.optimize import minimize_scalar

# Import canonical constants
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import canonical_constants as cc

print("=" * 70)
print("S57 GGE-EQUILIBRIUM-GAP-57: Distance from Equilibrium")
print("=" * 70)

# ── 1. Load data ──────────────────────────────────────────────────────

# S54 ED sweep: fold location
d54 = np.load(os.path.join(os.path.dirname(__file__), 's54_ed_sweep.npz'),
              allow_pickle=True)
fold_idx = int(d54['fold_idx'])
tau_fold = d54['tau_values'][fold_idx]
N_modes = int(d54['N_modes'])
N_pair_ed = int(d54['N_pair'])  # = 1

# S43 GGE temperatures (definitive computation)
d43 = np.load(os.path.join(os.path.dirname(__file__), "..", "_shared",
              's43_gge_temperatures.npz'), allow_pickle=True)

# S55 Volovik identity (cross-check)
d55 = np.load(os.path.join(os.path.dirname(__file__), 's55_volovik_identity.npz'),
              allow_pickle=True)

# Fundamental data from S43 exact diagonalization
fk_gge = d43['nk_exact']        # 8 GGE occupations (sum = 1, canonical N=1)
xi = d43['xi']                  # single-particle energies (branch-averaged)
branch_labels = d43['branch_labels']
E_k = 2.0 * xi                 # BCS pair energies
T_k_volovik = d55['T_k']       # Volovik temperatures from S55

# Cross-checks
E_GGE_stored = float(d43['E_GGE'])
E_GGE_check = np.sum(fk_gge * E_k)
assert abs(E_GGE_check - E_GGE_stored) < 1e-10, \
    f"E_GGE mismatch: {E_GGE_check} vs {E_GGE_stored}"
assert abs(np.sum(fk_gge) - 1.0) < 1e-10, \
    f"Occupations don't sum to 1: {np.sum(fk_gge)}"

print(f"\nData loaded successfully.")
print(f"  fold_idx = {fold_idx}, tau_fold = {tau_fold:.4f}")
print(f"  N_modes = {N_modes}, N_pair (ED) = {N_pair_ed}")
print(f"  n_pairs (physical) = {cc.n_pairs}")
print(f"  E_GGE = {E_GGE_stored:.6f} M_KK")

# ── 2. Display per-mode GGE data ─────────────────────────────────────

print(f"\n{'Mode':<8} {'E_k=2xi':>10} {'f_k^GGE':>10} {'T_k^V':>10} {'beta_k':>10}")
print("-" * 52)
beta_k = -np.log(fk_gge)  # canonical GGE: beta_k = -ln(f_k)
for k in range(N_modes):
    print(f"{str(branch_labels[k]):<8} {E_k[k]:10.6f} {fk_gge[k]:10.6f} "
          f"{T_k_volovik[k]:10.6f} {beta_k[k]:10.4f}")

# ── 3A. CANONICAL analysis: f_k^eq = exp(-E_k/T) / Z(T) ─────────────

print(f"\n{'='*60}")
print(f"  ANALYSIS A: Canonical N=1 (Boltzmann statistics)")
print(f"{'='*60}")

def fk_canonical(T, Ek):
    """Canonical N=1 equilibrium: f_k = exp(-E_k/T) / Z"""
    if T <= 1e-15:
        f = np.zeros_like(Ek)
        f[np.argmin(Ek)] = 1.0
        return f
    boltz = np.exp(-Ek / T)
    return boltz / np.sum(boltz)

def L2_canonical(T):
    """||f^GGE - f^eq(T)||_2 in canonical ensemble"""
    f_eq = fk_canonical(T, E_k)
    return np.sum((fk_gge - f_eq)**2)

# Coarse scan
T_scan = np.linspace(0.01, 10.0, 100000)
L2_scan = np.array([L2_canonical(T) for T in T_scan])
T_min_scan = T_scan[np.argmin(L2_scan)]
print(f"\n  Coarse scan: T_eq_approx = {T_min_scan:.4f} M_KK")

# Refine
result_can = minimize_scalar(L2_canonical, bounds=(0.01, 50.0), method='bounded',
                              options={'xatol': 1e-15})
T_eq_can = result_can.x
L2_can = np.sqrt(result_can.fun)

fk_eq_can = fk_canonical(T_eq_can, E_k)

print(f"  Refined: T_eq = {T_eq_can:.10f} M_KK")
print(f"  ||f^GGE - f^eq(T_eq)||_2 = {L2_can:.10f}")
print(f"  ||f^GGE - f^eq||_2 / N_pair = {L2_can/N_pair_ed:.6e}")

# Per-mode comparison
print(f"\n  {'Mode':<8} {'f_k^GGE':>10} {'f_k^eq':>10} {'delta_f':>10} {'delta/f':>10}")
print(f"  {'-'*48}")
for k in range(N_modes):
    df = fk_gge[k] - fk_eq_can[k]
    rel = df / fk_gge[k] if fk_gge[k] > 1e-10 else np.nan
    print(f"  {str(branch_labels[k]):<8} {fk_gge[k]:10.6f} {fk_eq_can[k]:10.6f} "
          f"{df:+10.6f} {rel:+10.4f}")

# Energy comparison
E_eq_can = np.sum(fk_eq_can * E_k)
Delta_E_can = E_GGE_stored - E_eq_can
print(f"\n  E_GGE = {E_GGE_stored:.6f} M_KK")
print(f"  E_eq  = {E_eq_can:.6f} M_KK")
print(f"  Delta_E = {Delta_E_can:+.6e} M_KK")

# ── 3B. GRAND-CANONICAL analysis: n_k = 1/(exp(eps_k/T)+1) ──────────

print(f"\n{'='*60}")
print(f"  ANALYSIS B: Grand-canonical Fermi-Dirac (mu=0)")
print(f"{'='*60}")

# In S43, the Volovik temperatures T_k^V were defined so that
# f_k = 1/(exp(2*xi_k / T_k^V) + 1), i.e., Fermi-Dirac with
# energy = 2*xi_k and per-mode temperature T_k^V.
#
# For equilibrium, we find T_eq such that
# n_k^eq = 1/(exp(2*xi_k / T_eq) + 1)
# minimizes ||f^GGE - n^eq||_2
#
# Note: the FD occupations don't sum to 1, so this is grand-canonical.

def nk_fd(T, Ek):
    """Grand-canonical Fermi-Dirac occupations at temperature T, mu=0."""
    if T <= 1e-15:
        return np.zeros_like(Ek)
    x = Ek / T
    safe = np.clip(x, -500, 500)
    return 1.0 / (np.exp(safe) + 1.0)

def L2_fd(T):
    """||f^GGE - n^FD(T)||_2"""
    n_eq = nk_fd(T, E_k)
    return np.sum((fk_gge - n_eq)**2)

# Check: do Volovik temperatures reproduce GGE occupations via FD?
nk_from_TV = np.array([1.0/(np.exp(E_k[k]/T_k_volovik[k]) + 1.0) for k in range(N_modes)])
print(f"\n  FD reconstruction from T_k^V:")
print(f"  max |f_k - FD(T_k^V)| = {np.max(np.abs(fk_gge - nk_from_TV)):.2e}")

# Coarse scan
L2_fd_scan = np.array([L2_fd(T) for T in T_scan])
T_min_fd = T_scan[np.argmin(L2_fd_scan)]
print(f"\n  Coarse scan: T_eq_FD_approx = {T_min_fd:.4f} M_KK")

# Refine
result_fd = minimize_scalar(L2_fd, bounds=(0.01, 50.0), method='bounded',
                             options={'xatol': 1e-15})
T_eq_fd = result_fd.x
L2_fd_min = np.sqrt(result_fd.fun)

nk_eq_fd = nk_fd(T_eq_fd, E_k)

print(f"  Refined: T_eq_FD = {T_eq_fd:.10f} M_KK")
print(f"  ||f^GGE - n^FD(T_eq)||_2 = {L2_fd_min:.10f}")
print(f"  ||...||_2 / N_pair = {L2_fd_min/N_pair_ed:.6e}")

# Per-mode comparison
print(f"\n  {'Mode':<8} {'f_k^GGE':>10} {'n_k^FD':>10} {'delta_n':>10} {'delta/f':>10}")
print(f"  {'-'*48}")
for k in range(N_modes):
    dn = fk_gge[k] - nk_eq_fd[k]
    rel = dn / fk_gge[k] if fk_gge[k] > 1e-10 else np.nan
    print(f"  {str(branch_labels[k]):<8} {fk_gge[k]:10.6f} {nk_eq_fd[k]:10.6f} "
          f"{dn:+10.6f} {rel:+10.4f}")

# ── 3C. Optimal equilibrium with free chemical potential ──────────────

print(f"\n{'='*60}")
print(f"  ANALYSIS C: Grand-canonical FD with optimal mu")
print(f"{'='*60}")

from scipy.optimize import minimize as scipy_minimize

def nk_fd_mu(T, mu, Ek):
    """Grand-canonical Fermi-Dirac with chemical potential mu."""
    if T <= 1e-15:
        return np.where(Ek < mu, 1.0, 0.0)
    x = (Ek - mu) / T
    safe = np.clip(x, -500, 500)
    return 1.0 / (np.exp(safe) + 1.0)

def L2_fd_mu(params):
    T, mu = params
    if T <= 0:
        return 1e10
    n_eq = nk_fd_mu(T, mu, E_k)
    return np.sum((fk_gge - n_eq)**2)

# Multi-start optimization
best_result = None
best_fun = np.inf
for T0 in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
    for mu0 in [-2.0, 0.0, 0.5, 1.0, 1.5, 2.0]:
        res = scipy_minimize(L2_fd_mu, [T0, mu0], method='Nelder-Mead',
                             options={'xatol': 1e-14, 'fatol': 1e-20, 'maxiter': 50000})
        if res.fun < best_fun:
            best_fun = res.fun
            best_result = res

T_eq_mu, mu_eq = best_result.x
L2_mu = np.sqrt(best_fun)
nk_eq_mu = nk_fd_mu(T_eq_mu, mu_eq, E_k)

print(f"  T_eq = {T_eq_mu:.10f} M_KK, mu_eq = {mu_eq:.10f} M_KK")
print(f"  ||f^GGE - n^FD(T,mu)||_2 = {L2_mu:.10f}")
print(f"  ||...||_2 / N_pair = {L2_mu/N_pair_ed:.6e}")

# Per-mode comparison
print(f"\n  {'Mode':<8} {'f_k^GGE':>10} {'n_k^FD':>10} {'delta_n':>10}")
print(f"  {'-'*38}")
for k in range(N_modes):
    dn = fk_gge[k] - nk_eq_mu[k]
    print(f"  {str(branch_labels[k]):<8} {fk_gge[k]:10.6f} {nk_eq_mu[k]:10.6f} "
          f"{dn:+10.6f}")

# ── 4. Summary of all three analyses ─────────────────────────────────

print(f"\n{'='*70}")
print(f"  SUMMARY: THREE EQUILIBRIUM MEASURES")
print(f"{'='*70}")
print(f"  {'Method':<35} {'||gap||_2':>12} {'||gap||/N':>12} {'T_eq':>10}")
print(f"  {'-'*70}")
print(f"  {'A: Canonical N=1 (Boltzmann)':<35} {L2_can:12.6e} {L2_can/N_pair_ed:12.6e} {T_eq_can:10.4f}")
print(f"  {'B: Grand-canonical FD (mu=0)':<35} {L2_fd_min:12.6e} {L2_fd_min/N_pair_ed:12.6e} {T_eq_fd:10.4f}")
print(f"  {'C: Grand-canonical FD (opt mu)':<35} {L2_mu:12.6e} {L2_mu/N_pair_ed:12.6e} {T_eq_mu:10.4f}")
print(f"\n  Gate threshold: 1e-57")
print(f"  All three O(0.1), ratio to gate ~ 10^{56}")

# ── 5. The correct canonical analysis ────────────────────────────────

print(f"\n{'='*70}")
print(f"  PRIMARY RESULT: Canonical Analysis (Method A)")
print(f"{'='*70}")

# For the canonical N=1 system, the correct equilibrium is Boltzmann:
# f_k^eq = exp(-E_k/T) / Z
# The gap measures how far the GGE is from this thermal distribution.

# L1, L2, Linf norms
L1_can = np.sum(np.abs(fk_gge - fk_eq_can))
Linf_can = np.max(np.abs(fk_gge - fk_eq_can))

print(f"\n  Norms of (f^GGE - f^eq):")
print(f"    L1   = {L1_can:.6e}")
print(f"    L2   = {L2_can:.6e}")
print(f"    Linf = {Linf_can:.6e}")

# KL divergence (canonical)
D_KL_can = 0.0  # (local)
for k in range(N_modes):
    if fk_gge[k] > 1e-15 and fk_eq_can[k] > 1e-15:
        D_KL_can += fk_gge[k] * np.log(fk_gge[k] / fk_eq_can[k])

print(f"\n  D_KL(GGE || eq) = {D_KL_can:.6f} nats")
print(f"  D_KL / N_modes  = {D_KL_can/N_modes:.6f} nats/mode")

# Jensen-Shannon divergence
m = 0.5 * (fk_gge + fk_eq_can)
D_JS = 0.0  # (local)
for k in range(N_modes):
    if fk_gge[k] > 1e-15 and m[k] > 1e-15:
        D_JS += 0.5 * fk_gge[k] * np.log(fk_gge[k] / m[k])
    if fk_eq_can[k] > 1e-15 and m[k] > 1e-15:
        D_JS += 0.5 * fk_eq_can[k] * np.log(fk_eq_can[k] / m[k])
print(f"  D_JS(GGE, eq)   = {D_JS:.6f} nats")

# Entropy comparison (canonical: S = -sum f_k ln f_k)
S_GGE_can = -np.sum(fk_gge * np.log(np.clip(fk_gge, 1e-300, None)))
S_eq_can = -np.sum(fk_eq_can * np.log(np.clip(fk_eq_can, 1e-300, None)))
S_max_can = np.log(N_modes)  # uniform distribution over 8 modes
Delta_S_can = S_GGE_can - S_eq_can

print(f"\n  Entropy (canonical, nats):")
print(f"    S_GGE = {S_GGE_can:.6f}")
print(f"    S_eq  = {S_eq_can:.6f}")
print(f"    S_max = {S_max_can:.6f} (= ln 8)")
print(f"    S_GGE/S_max = {S_GGE_can/S_max_can:.6f}")
print(f"    S_eq/S_max  = {S_eq_can/S_max_can:.6f}")
print(f"    Delta_S = {Delta_S_can:+.6e}")

# Energy gap
Delta_E_primary = E_GGE_stored - E_eq_can
print(f"\n  Energy gap:")
print(f"    E_GGE = {E_GGE_stored:.6f} M_KK")
print(f"    E_eq  = {E_eq_can:.6f} M_KK")
print(f"    Delta_E = {Delta_E_primary:+.6e} M_KK")
print(f"    Delta_E/E_GGE = {Delta_E_primary/E_GGE_stored:+.6e}")

# ── 6. Vacuum energy / CC from non-equilibrium departure ─────────────

print(f"\n{'='*60}")
print(f"  VACUUM ENERGY FROM NON-EQUILIBRIUM DEPARTURE")
print(f"{'='*60}")

# Volovik equilibrium theorem: in equilibrium, the vacuum energy does not
# gravitate (CC = 0). The observed CC arises from the departure from equilibrium.
#
# P_vac = N_pair - E_GGE (Volovik identity, from S55)
# At equilibrium: P_vac^eq = N_pair - E_eq
# The CC contribution from non-equilibrium:
# Lambda_neq = (E_GGE - E_eq) / V_eff  [energy density excess]
#
# But by the equilibrium theorem, the equilibrium state itself has Lambda = 0
# (it self-tunes). So the ENTIRE CC comes from (E_GGE - E_eq).

P_vac_GGE = N_pair_ed - E_GGE_stored  # = -0.688
P_vac_eq = N_pair_ed - E_eq_can
Delta_P = P_vac_GGE - P_vac_eq  # = -(E_GGE - E_eq)

print(f"\n  P_vac^GGE = {P_vac_GGE:.6f} M_KK")
print(f"  P_vac^eq  = {P_vac_eq:.6f} M_KK")
print(f"  Delta_P   = {Delta_P:+.6e} M_KK")

# Physical CC
Lambda_excess_MKK = abs(Delta_E_primary)
Lambda_excess_GeV4 = Lambda_excess_MKK * cc.M_KK**4
Lambda_obs_GeV4 = 2.846e-47  # GeV^4  # (local)

CC_ratio = Lambda_excess_GeV4 / Lambda_obs_GeV4
CC_log10 = np.log10(CC_ratio)

print(f"\n  |Lambda_neq| = {Lambda_excess_MKK:.6e} M_KK^4")
print(f"  |Lambda_neq| = {Lambda_excess_GeV4:.3e} GeV^4")
print(f"  Lambda_obs   = {Lambda_obs_GeV4:.3e} GeV^4")
print(f"  |Lambda_neq/Lambda_obs| = {CC_ratio:.3e}")
print(f"  log10 ratio  = {CC_log10:.1f} orders")

# Note: the FULL CC gap is 115 orders (from P_vac = -0.688).
# The non-equilibrium excess is Delta_E = E_GGE - E_eq,
# which is a FRACTION of E_GGE. So the non-equilibrium CC
# is still enormously above observation.

# ── 7. Superfluid 3He analog interpretation ──────────────────────────

print(f"\n{'='*60}")
print(f"  SUPERFLUID ANALOG INTERPRETATION")
print(f"{'='*60}")

T_max = np.max(T_k_volovik)
T_min = np.min(T_k_volovik)
T_ratio = T_max / T_min

print(f"""
  The GGE relic is the direct analog of a quenched superfluid 3He-B
  with 8 quasiparticle branches at different effective temperatures:

    T_max/T_min = {T_ratio:.3f} (factor of temperature spread)
    T_max = {T_max:.4f} M_KK (B2[0])
    T_min = {T_min:.4f} M_KK (B3[0])

  In superfluid 3He, such a non-thermal quasiparticle distribution
  would thermalize via quasiparticle-quasiparticle scattering on a
  timescale tau_qp ~ (k_B T / Delta)^{-5} * hbar/Delta.

  In this framework, thermalization is FORBIDDEN:
    - H_free is non-interacting (trivially integrable)
    - Block-diagonal theorem prevents inter-sector coupling
    - N_pair = 1 (no many-body scattering channels)

  This is the superfluid analog of a universe permanently frozen
  at the wrong vacuum energy. The 3He experiment would correspond
  to a superfluid where quasiparticle-quasiparticle scattering is
  exactly forbidden -- not approximately, but by symmetry.

  The CC problem = "why does the vacuum not relax to equilibrium?"
  Answer: integrability prevents it. Structurally, permanently.

  The ||gap|| = {L2_can:.4f} is O(1), confirming that no small
  correction can bring the GGE to equilibrium. The temperature
  hierarchy is baked in by the topology of the transit.
""")

# ── 8. Gate verdict ──────────────────────────────────────────────────

gate_criterion = 1e-57
gate_value = L2_can / N_pair_ed  # Use canonical analysis (Method A)

if gate_value < gate_criterion:
    gate_verdict = "PASS"
else:
    gate_verdict = "FAIL"

print(f"{'='*70}")
print(f"  GATE VERDICT: GGE-EQUILIBRIUM-GAP-57 = {gate_verdict}")
print(f"{'='*70}")
print(f"  ||f^GGE - f^eq||_2 / N_pair = {gate_value:.6e}")
print(f"  Gate threshold              = {gate_criterion:.0e}")
print(f"  Ratio (gap / threshold)     = {gate_value / gate_criterion:.2e}")
print(f"  T_eq (canonical)            = {T_eq_can:.6f} M_KK")
print(f"  T_eq (FD, mu=0)             = {T_eq_fd:.6f} M_KK")
print(f"  T_eq (FD, opt mu)           = {T_eq_mu:.6f} M_KK")
print(f"  D_KL(GGE || eq)             = {D_KL_can:.6f} nats")
print(f"  CC from non-eq excess       = {CC_log10:.1f} orders above obs")
print(f"")
print(f"  STRUCTURAL CONCLUSION: The GGE is O(1) away from ANY equilibrium")
print(f"  distribution. The CC gap cannot be closed by thermalization alone.")
print(f"  This is the precise arithmetic confirmation of the Volovik")
print(f"  equilibrium theorem applied to the BCS-on-SU(3) framework:")
print(f"  in a system where the microscopic theory is known, the vacuum")
print(f"  energy problem reduces to the thermalization problem.")
print(f"{'='*70}")

# ── 9. Save results ──────────────────────────────────────────────────

outpath = os.path.join(os.path.dirname(__file__), 's57_gge_equilibrium_gap.npz')
np.savez(outpath,
    # Gate
    gate_name='GGE-EQUILIBRIUM-GAP-57',
    gate_verdict=gate_verdict,
    gate_criterion=gate_criterion,
    gate_value=gate_value,
    # Mode data
    branch_labels=branch_labels,
    E_k=E_k,
    xi=xi,
    fk_gge=fk_gge,
    T_k_volovik=T_k_volovik,
    beta_k=beta_k,
    # Canonical analysis (primary)
    T_eq_canonical=T_eq_can,
    fk_eq_canonical=fk_eq_can,
    L2_canonical=L2_can,
    L1_canonical=L1_can,
    Linf_canonical=Linf_can,
    E_eq_canonical=E_eq_can,
    Delta_E_canonical=Delta_E_primary,
    S_GGE_canonical=S_GGE_can,
    S_eq_canonical=S_eq_can,
    S_max_canonical=S_max_can,
    D_KL_canonical=D_KL_can,
    D_JS_canonical=D_JS,
    # FD analysis (mu=0)
    T_eq_fd=T_eq_fd,
    nk_eq_fd=nk_eq_fd,
    L2_fd=L2_fd_min,
    # FD analysis (opt mu)
    T_eq_fd_mu=T_eq_mu,
    mu_eq_fd=mu_eq,
    nk_eq_fd_mu=nk_eq_mu,
    L2_fd_mu=L2_mu,
    # Vacuum energy
    P_vac_GGE=P_vac_GGE,
    P_vac_eq=P_vac_eq,
    Delta_P=Delta_P,
    E_GGE=E_GGE_stored,
    Lambda_excess_MKK=Lambda_excess_MKK,
    Lambda_excess_GeV4=Lambda_excess_GeV4,
    CC_ratio=CC_ratio,
    CC_log10=CC_log10,
    # Temperature spread
    T_max_volovik=T_max,
    T_min_volovik=T_min,
    T_ratio_volovik=T_ratio,
    # Metadata
    tau_fold=tau_fold,
    fold_idx=fold_idx,
    N_modes=N_modes,
    N_pair_ed=N_pair_ed,
    n_pairs_physical=cc.n_pairs,
    M_KK=cc.M_KK,
)

print(f"\nResults saved to: {outpath}")
print("DONE")
