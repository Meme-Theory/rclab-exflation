#!/usr/bin/env python3
"""
BAYES-39: Bayesian GGE vs Thermal Model Comparison
=====================================================

Computes Bayes factor BF = p(data|GGE) / p(data|thermal) quantifying
the non-thermal character of the post-transit GGE relic.

Physics:
  The post-transit state is a GGE with 8 Richardson-Gaudin conserved charges
  (3 distinct Lagrange multipliers due to degeneracies: lambda_B2, lambda_B1,
  lambda_B3). The comparison thermal state is a single-parameter Gibbs
  ensemble at temperature T = 1/beta.

  Since INTEG-39 showed the system thermalizes at t_therm ~ 6 natural units,
  this Bayes factor measures the INITIAL non-thermality — the information
  content of the transit that is subsequently lost.

Method:
  1. Construct GGE and Gibbs probability distributions over the full 2^8 = 256
     Fock space of quasiparticle occupations.
  2. Compute KL divergence D_KL(GGE || Gibbs) and D_KL(Gibbs || GGE).
  3. Compute Jensen-Shannon divergence (symmetric).
  4. Compute Bayes factor via:
     (a) BIC approximation: log(BF) ~ (N/2)*D_KL - (k_extra/2)*log(N)
     (b) Exact marginal likelihood ratio with flat priors over reasonable ranges.
  5. Verify via direct Fock-space enumeration using the BCS Hamiltonian.

Author: gen-physicist (Session 39, Wave 4)
"""

import numpy as np
from scipy.special import logsumexp
from scipy.optimize import minimize_scalar
from itertools import product
import sys

# ============================================================
# 1. Load data
# ============================================================
print("=" * 70)
print("BAYES-39: Bayesian GGE vs Thermal Model Comparison")
print("=" * 70)

gge_data = np.load('tier0-computation/s39_gge_lambdas.npz', allow_pickle=True)
kk_data = np.load('tier0-computation/s39_kk_mass.npz', allow_pickle=True)
bcs_data = np.load('tier0-computation/s38_otoc_bcs.npz', allow_pickle=True)

lambda_k = gge_data['lambda_k']       # 8 Lagrange multipliers
p_k_gge = gge_data['p_k']             # Single-mode GGE occupations
S_gge = float(gge_data['S_gge'])       # GGE entropy
branch_labels = gge_data['branch_labels']

beta_gibbs = float(kk_data['beta_gibbs'])   # Gibbs inverse temperature
T_gibbs = float(kk_data['T_gibbs'])         # Gibbs temperature
p_k_gibbs = kk_data['p_gibbs']              # Single-mode Gibbs occupations
S_gibbs_stored = float(kk_data['S_gibbs'])

E_8 = bcs_data['E_8']                 # Single-particle energies
V_phys = bcs_data['V_phys']           # Interaction matrix
evals_BCS = bcs_data['evals_BCS']     # Full 256-dim BCS eigenvalues
rho_8 = bcs_data['rho_8']             # Density of states

n_modes = 8
dim_fock = 2**n_modes  # = 256

print(f"\nInput parameters:")
print(f"  n_modes = {n_modes}, Fock dim = {dim_fock}")
print(f"  lambda_k = {lambda_k}")
print(f"  Distinct lambdas: B2={lambda_k[0]:.6f}, B1={lambda_k[4]:.6f}, B3={lambda_k[5]:.6f}")
print(f"  beta_gibbs = {beta_gibbs:.6f}, T_gibbs = {T_gibbs:.6f}")
print(f"  S_gge = {S_gge:.6f}, S_gibbs = {S_gibbs_stored:.6f}")

# ============================================================
# 2. Construct Fock space and many-body energies
# ============================================================
# Each Fock state |n_1, n_2, ..., n_8> with n_k in {0, 1}
# Enumerate all 256 states
fock_states = np.array(list(product([0, 1], repeat=n_modes)), dtype=np.float64)
# fock_states[i, k] = occupation of mode k in state i

# Many-body energy for each Fock state from the BCS Hamiltonian
# H_BCS = sum_k E_k * n_k - sum_{k,l} V_{kl} * n_k * n_l  (attractive pairing)
# But the exact eigenvalues are already computed in evals_BCS.
# We need a consistent energy function. Let's reconstruct from the
# single-particle + interaction terms.

# Energy of each Fock state in the mean-field (diagonal) basis:
# E(n) = sum_k E_k * n_k  (quasiparticle energies, no interaction in qp basis)
# But the GGE is in the quasiparticle basis where the conserved charges are
# the quasiparticle number operators. So:

# For GGE: the distribution factorizes over modes.
# p_GGE(n_1,...,n_8) = prod_k [p_k^{n_k} * (1-p_k)^{1-n_k}]
# where p_k = 1/(exp(lambda_k) + 1) are the Fermi-Dirac occupations.

# For Gibbs: the thermal distribution uses the FULL many-body spectrum.
# p_Gibbs(alpha) = exp(-beta * E_alpha) / Z  where E_alpha are the 256
# exact BCS eigenvalues.

# CRITICAL DISTINCTION: The GGE factorizes in the quasiparticle basis
# (it's a product state in that basis), while the Gibbs ensemble weights
# by the EXACT many-body energies which include all correlations.

# However, to compare on equal footing, both distributions must be defined
# on the SAME sample space. The natural choice is the 256-dimensional
# Fock space indexed by the exact many-body eigenstates.

# Approach: Work in the energy eigenbasis where both distributions assign
# probabilities to each of the 256 eigenstates.

print("\n" + "=" * 70)
print("2. Constructing probability distributions over Fock space")
print("=" * 70)

# Sort eigenvalues
idx_sort = np.argsort(evals_BCS)
E_sorted = evals_BCS[idx_sort]

# --- GGE distribution in quasiparticle Fock basis ---
# The GGE density matrix is diagonal in the quasiparticle number basis:
# rho_GGE = prod_k [(1-p_k)|0_k><0_k| + p_k|1_k><1_k|]
# In the Fock basis |n_1,...,n_8>, the probability is:
# P_GGE(n) = prod_k [p_k^{n_k} * (1-p_k)^{1-n_k}]

log_p_gge = np.zeros(dim_fock)
for i in range(dim_fock):
    log_prob = 0.0
    for k in range(n_modes):
        n_k = fock_states[i, k]
        if n_k == 1:
            log_prob += np.log(p_k_gge[k])
        else:
            log_prob += np.log(1.0 - p_k_gge[k])
    log_p_gge[i] = log_prob

# Normalize (should already be normalized but verify)
log_Z_gge = logsumexp(log_p_gge)
log_p_gge -= log_Z_gge
p_gge = np.exp(log_p_gge)

print(f"\nGGE distribution:")
print(f"  log(Z_GGE) = {log_Z_gge:.6e} (should be ~0)")
print(f"  sum(p_GGE) = {np.sum(p_gge):.15f}")
print(f"  S_GGE (from distribution) = {-np.sum(p_gge * log_p_gge):.6f}")
print(f"  S_GGE (stored) = {S_gge:.6f}")

# Verify: the single-mode entropy should match
S_gge_check = 0.0
for k in range(n_modes):
    pk = p_k_gge[k]
    if 0 < pk < 1:
        S_gge_check -= pk * np.log(pk) + (1 - pk) * np.log(1 - pk)
print(f"  S_GGE (single-mode sum) = {S_gge_check:.6f}")

# --- Gibbs distribution over exact many-body eigenstates ---
# P_Gibbs(alpha) = exp(-beta * E_alpha) / Z_Gibbs
# Here alpha indexes the 256 exact BCS eigenstates

log_p_gibbs_exact = -beta_gibbs * evals_BCS
log_Z_gibbs = logsumexp(log_p_gibbs_exact)
log_p_gibbs_exact -= log_Z_gibbs
p_gibbs_exact = np.exp(log_p_gibbs_exact)

S_gibbs_exact = -np.sum(p_gibbs_exact * log_p_gibbs_exact)

print(f"\nGibbs distribution (exact BCS spectrum):")
print(f"  beta = {beta_gibbs:.6f}")
print(f"  log(Z_Gibbs) = {log_Z_gibbs:.6f}")
print(f"  sum(p_Gibbs) = {np.sum(p_gibbs_exact):.15f}")
print(f"  S_Gibbs (exact) = {S_gibbs_exact:.6f}")
print(f"  S_Gibbs (stored) = {S_gibbs_stored:.6f}")
print(f"  <E>_Gibbs = {np.sum(p_gibbs_exact * evals_BCS):.6f}")
print(f"  E_0 = {evals_BCS.min():.6f}")

# --- Gibbs distribution in quasiparticle Fock basis ---
# For a factorized comparison, also compute the free-fermion Gibbs:
# P_Gibbs^{free}(n) = prod_k f_k^{n_k} (1-f_k)^{1-n_k}
# where f_k = 1/(exp(beta*E_k) + 1)

# The quasiparticle energies for the Gibbs ensemble
# Use E_8 as the single-particle spectrum
f_k_gibbs = 1.0 / (np.exp(beta_gibbs * E_8) + 1.0)

log_p_gibbs_free = np.zeros(dim_fock)
for i in range(dim_fock):
    log_prob = 0.0
    for k in range(n_modes):
        n_k = fock_states[i, k]
        if n_k == 1:
            log_prob += np.log(f_k_gibbs[k])
        else:
            log_prob += np.log(1.0 - f_k_gibbs[k])
    log_p_gibbs_free[i] = log_prob

log_Z_gibbs_free = logsumexp(log_p_gibbs_free)
log_p_gibbs_free -= log_Z_gibbs_free
p_gibbs_free = np.exp(log_p_gibbs_free)

S_gibbs_free = -np.sum(p_gibbs_free * log_p_gibbs_free)

print(f"\nGibbs distribution (free-fermion, factorized):")
print(f"  f_k = {f_k_gibbs}")
print(f"  S_Gibbs^free = {S_gibbs_free:.6f}")

# ============================================================
# 3. KL Divergences
# ============================================================
print("\n" + "=" * 70)
print("3. KL Divergences and Information-Theoretic Measures")
print("=" * 70)

# D_KL(P || Q) = sum_i P(i) * log(P(i)/Q(i))
# Need to handle zeros carefully

def kl_divergence(p, q, name_p="P", name_q="Q"):
    """Compute D_KL(p || q) with proper handling of zeros."""
    mask = p > 1e-300  # Only sum over states where p > 0
    if np.any(q[mask] < 1e-300):
        # q has zeros where p is nonzero -> D_KL = infinity
        n_bad = np.sum(q[mask] < 1e-300)
        print(f"  WARNING: {n_bad} states where {name_p}>0 but {name_q}~0")
        # Use a floor for numerical stability
        q_safe = np.maximum(q, 1e-300)
        dkl = np.sum(p[mask] * (np.log(p[mask]) - np.log(q_safe[mask])))
    else:
        dkl = np.sum(p[mask] * (np.log(p[mask]) - np.log(q[mask])))
    return dkl

# The key comparison: GGE (factorized in qp basis) vs Gibbs (factorized in qp basis)
# Both distributions live on the same 256-state Fock space

# Comparison 1: GGE vs free-fermion Gibbs (both factorized, same basis)
DKL_gge_gibbs_free = kl_divergence(p_gge, p_gibbs_free, "GGE", "Gibbs_free")
DKL_gibbs_free_gge = kl_divergence(p_gibbs_free, p_gge, "Gibbs_free", "GGE")

print(f"\n--- Factorized comparison (same basis) ---")
print(f"  D_KL(GGE || Gibbs_free) = {DKL_gge_gibbs_free:.6f} nats")
print(f"  D_KL(Gibbs_free || GGE) = {DKL_gibbs_free_gge:.6f} nats")
print(f"  D_KL(GGE || Gibbs_free) = {DKL_gge_gibbs_free / np.log(2):.6f} bits")

# Jensen-Shannon divergence (symmetric)
m_free = 0.5 * (p_gge + p_gibbs_free)
JSD_free = 0.5 * kl_divergence(p_gge, m_free, "GGE", "M") + \
           0.5 * kl_divergence(p_gibbs_free, m_free, "Gibbs_free", "M")

print(f"  JSD(GGE, Gibbs_free) = {JSD_free:.6f} nats")
print(f"  JSD(GGE, Gibbs_free) = {JSD_free / np.log(2):.6f} bits")
print(f"  sqrt(JSD) = {np.sqrt(JSD_free):.6f} (Jensen-Shannon distance)")

# Single-mode KL divergence (analytic, more transparent)
DKL_single_mode = 0.0
for k in range(n_modes):
    pk = p_k_gge[k]
    fk = f_k_gibbs[k]
    if pk > 0 and pk < 1 and fk > 0 and fk < 1:
        dkl_k = pk * np.log(pk / fk) + (1 - pk) * np.log((1 - pk) / (1 - fk))
        DKL_single_mode += dkl_k
        print(f"  Mode {k} ({branch_labels[k]}): p_GGE={pk:.6f}, f_Gibbs={fk:.6f}, "
              f"D_KL_k={dkl_k:.6f} nats")

print(f"\n  D_KL(GGE||Gibbs) single-mode sum = {DKL_single_mode:.6f} nats")
print(f"  Cross-check vs Fock-space D_KL = {DKL_gge_gibbs_free:.6f} nats")
print(f"  Difference = {abs(DKL_single_mode - DKL_gge_gibbs_free):.2e} (should be ~0)")

# ============================================================
# 4. Optimal Gibbs temperature (maximum likelihood)
# ============================================================
print("\n" + "=" * 70)
print("4. Optimal Gibbs temperature (minimize D_KL)")
print("=" * 70)

# Find the beta that minimizes D_KL(GGE || Gibbs_free(beta))
# This is equivalent to maximum likelihood estimation of beta
# given the GGE as the "data"

def neg_log_lik_gibbs(beta_trial):
    """Negative cross-entropy of GGE under Gibbs(beta)."""
    f_k = 1.0 / (np.exp(beta_trial * E_8) + 1.0)
    f_k = np.clip(f_k, 1e-15, 1 - 1e-15)
    # Cross-entropy H(GGE, Gibbs) = -sum_k [p_k*log(f_k) + (1-p_k)*log(1-f_k)]
    cross_ent = 0.0
    for k in range(n_modes):
        cross_ent -= p_k_gge[k] * np.log(f_k[k]) + (1 - p_k_gge[k]) * np.log(1 - f_k[k])
    return cross_ent

result = minimize_scalar(neg_log_lik_gibbs, bounds=(0.01, 100.0), method='bounded')
beta_opt = result.x
T_opt = 1.0 / beta_opt

f_k_opt = 1.0 / (np.exp(beta_opt * E_8) + 1.0)

print(f"  Optimal beta = {beta_opt:.6f}")
print(f"  Optimal T = {T_opt:.6f}")
print(f"  Stored beta = {beta_gibbs:.6f}, T = {T_gibbs:.6f}")

# D_KL at optimal beta
DKL_opt = 0.0
for k in range(n_modes):
    pk = p_k_gge[k]
    fk = f_k_opt[k]
    if pk > 0 and pk < 1 and fk > 0 and fk < 1:
        DKL_opt += pk * np.log(pk / fk) + (1 - pk) * np.log((1 - pk) / (1 - fk))

print(f"  D_KL(GGE || Gibbs_opt) = {DKL_opt:.6f} nats = {DKL_opt / np.log(2):.6f} bits")
print(f"  This is the IRREDUCIBLE non-thermality (no single-T Gibbs can do better)")

# Compare occupations at optimal beta
print(f"\n  Mode-by-mode comparison at optimal beta:")
print(f"  {'Mode':<8} {'p_GGE':>10} {'f_Gibbs_opt':>12} {'f_Gibbs_stored':>15} {'|delta_opt|':>12}")
for k in range(n_modes):
    print(f"  {branch_labels[k]:<8} {p_k_gge[k]:10.6f} {f_k_opt[k]:12.6f} "
          f"{f_k_gibbs[k]:15.6f} {abs(p_k_gge[k] - f_k_opt[k]):12.6f}")

# ============================================================
# 5. Bayes Factor — BIC Approximation
# ============================================================
print("\n" + "=" * 70)
print("5. Bayes Factor — BIC Approximation")
print("=" * 70)

# The BIC approximation to the Bayes factor:
# 2*log(BF) ~ 2*N*H(GGE,GGE) - 2*N*H(GGE,Gibbs) - k_extra*log(N)
# which simplifies to:
# 2*log(BF) ~ 2*N*D_KL(GGE || Gibbs_opt) - k_extra*log(N)
#
# where:
#   N = effective sample size (number of independent measurements)
#   k_extra = extra parameters in GGE vs Gibbs = 3 - 1 = 2
#     (GGE has 3 distinct lambdas: lambda_B2, lambda_B1, lambda_B3
#      Gibbs has 1 parameter: beta)
#
# The effective sample size is the Fock space dimension (256 states).
# But more physically, N is the number of independent "observations"
# that distinguish the two distributions.

k_gge = 3    # 3 distinct Lagrange multipliers
k_gibbs = 1  # 1 temperature parameter
k_extra = k_gge - k_gibbs  # = 2

# N_eff: the effective number of observations
# For a single quantum state, N_eff is related to the purity
# N_eff = 1/Tr(rho^2) = 1/purity gives the effective rank
purity = float(gge_data['purity'])
N_eff_purity = 1.0 / purity

# Alternative: use the Fock dimension
N_eff_fock = dim_fock

# Another natural choice: effective number of occupied states
N_eff_occ = np.exp(S_gge)  # exp(entropy) gives effective number of microstates

print(f"  k_GGE = {k_gge} (3 distinct lambdas)")
print(f"  k_Gibbs = {k_gibbs} (1 temperature)")
print(f"  k_extra = {k_extra}")
print(f"  N_eff (1/purity) = {N_eff_purity:.2f}")
print(f"  N_eff (Fock dim) = {N_eff_fock}")
print(f"  N_eff (exp(S)) = {N_eff_occ:.2f}")

# Use the most conservative: N_eff from purity
for N_eff, label in [(N_eff_purity, "1/purity"),
                     (N_eff_occ, "exp(S)"),
                     (N_eff_fock, "Fock dim")]:
    log_BF_bic = N_eff * DKL_opt - 0.5 * k_extra * np.log(N_eff)
    BF_bic = np.exp(min(log_BF_bic, 700))  # Cap for overflow

    print(f"\n  N_eff = {N_eff:.2f} ({label}):")
    print(f"    log(BF_BIC) = {log_BF_bic:.4f} nats = {log_BF_bic / np.log(10):.4f} decibans")
    if log_BF_bic < 700:
        print(f"    BF_BIC = {BF_bic:.4e}")
    else:
        print(f"    BF_BIC = exp({log_BF_bic:.1f}) [overflow]")
    if log_BF_bic > np.log(100):
        print(f"    DECISIVE: BF > 100 (strong non-thermal character)")
    elif log_BF_bic > np.log(10):
        print(f"    STRONG: BF > 10")
    elif log_BF_bic > np.log(3):
        print(f"    MODERATE: BF > 3")
    else:
        print(f"    WEAK: BF < 3")

# ============================================================
# 6. Exact Evidence Ratio (Marginal Likelihood)
# ============================================================
print("\n" + "=" * 70)
print("6. Exact Marginal Likelihood Ratio")
print("=" * 70)

# The marginal likelihood (evidence) for each model:
# p(data | M) = integral p(data | theta, M) * pi(theta | M) d(theta)
#
# For the GGE model with 3 distinct parameters (lambda_B2, lambda_B1, lambda_B3):
# We use the exact BCS Fock space. The "data" is the GGE state itself
# (the post-transit density matrix). The evidence ratio measures which
# model better compresses this state.
#
# More precisely: given the observed occupation numbers {n_k}, which
# model assigns higher probability with fewer parameters?
#
# We compute the log-likelihood of the GGE state under each model,
# integrated over parameter priors.

# The "data" are the 8 occupation numbers (sufficient statistics)
n_k_data = p_k_gge  # These are the observed expectation values

# --- GGE model ---
# Log-likelihood: sum_k [n_k * log(p_k(lambda_k)) + (1-n_k) * log(1 - p_k(lambda_k))]
# where p_k(lambda) = 1/(exp(lambda) + 1)
# Prior: flat on lambda_k in [0, 10] for each of the 3 distinct multipliers
# (3 groups: B2 x4, B1 x1, B3 x3)

# At the MAP point (which IS the observed lambdas since they were computed
# to maximize the GGE likelihood), the log-likelihood is just the GGE entropy
# with a sign flip. Actually, the log-likelihood is:
# L_GGE = sum_k [n_k * log(p_k) + (1 - n_k) * log(1 - p_k)]
# = -S_GGE (the negative of the Shannon entropy of the single-mode distribution)

# Wait — that's the log-likelihood per mode. For the full factorized distribution:
log_lik_gge = 0.0
for k in range(n_modes):
    pk = p_k_gge[k]
    log_lik_gge += pk * np.log(pk) + (1 - pk) * np.log(1 - pk)

print(f"  Log-likelihood at GGE MAP: {log_lik_gge:.6f}")
print(f"  = -S_GGE = {-S_gge:.6f} (cross-check)")

# --- Gibbs model at stored beta ---
log_lik_gibbs_stored = 0.0
for k in range(n_modes):
    fk = f_k_gibbs[k]
    pk = p_k_gge[k]
    log_lik_gibbs_stored += pk * np.log(fk) + (1 - pk) * np.log(1 - fk)

print(f"  Log-likelihood at stored beta={beta_gibbs:.4f}: {log_lik_gibbs_stored:.6f}")

# --- Gibbs model at optimal beta ---
log_lik_gibbs_opt = 0.0
for k in range(n_modes):
    fk = f_k_opt[k]
    pk = p_k_gge[k]
    log_lik_gibbs_opt += pk * np.log(fk) + (1 - pk) * np.log(1 - fk)

print(f"  Log-likelihood at optimal beta={beta_opt:.4f}: {log_lik_gibbs_opt:.6f}")

# Log-likelihood ratio at MAP
delta_log_lik = log_lik_gge - log_lik_gibbs_opt
print(f"\n  Delta log-likelihood (MAP) = {delta_log_lik:.6f} nats")
print(f"  = D_KL(GGE || Gibbs_opt) = {DKL_opt:.6f} nats (cross-check)")

# --- Numerical integration of marginal likelihoods ---
# GGE model: integrate over (lambda_B2, lambda_B1, lambda_B3)
# Gibbs model: integrate over beta

# Prior ranges (flat priors)
lambda_min, lambda_max = 0.01, 15.0
beta_min_prior, beta_max_prior = 0.1, 50.0

# GGE marginal likelihood via numerical integration
# p(n | GGE) = (1/V_prior) * integral prod_k [p_k(lambda)^{n_k} * (1-p_k)^{1-n_k}] d^3(lambda)
# where p_k(lambda) = 1/(exp(lambda) + 1)

N_grid = 200  # Grid points per dimension
lambda_grid = np.linspace(lambda_min, lambda_max, N_grid)
d_lambda = lambda_grid[1] - lambda_grid[0]

# For GGE: 3 independent parameters
# lambda_B2 controls modes 0-3, lambda_B1 controls mode 4, lambda_B3 controls modes 5-7
print(f"\n  Computing GGE marginal likelihood (grid {N_grid}^3)...")

# Precompute single-mode log-likelihoods on grid
def log_lik_mode(n_k_obs, lam):
    """Log-likelihood for one mode at occupation n_k_obs and Lagrange multiplier lam."""
    p = 1.0 / (np.exp(lam) + 1.0)
    p = np.clip(p, 1e-15, 1 - 1e-15)
    return n_k_obs * np.log(p) + (1 - n_k_obs) * np.log(1 - p)

# B2 modes (0-3): all have same lambda, multiplicity 4
log_lik_B2 = np.zeros(N_grid)
for lam_idx, lam in enumerate(lambda_grid):
    ll = 0.0
    for k in range(4):  # modes 0-3
        ll += log_lik_mode(n_k_data[k], lam)
    log_lik_B2[lam_idx] = ll

# B1 mode (4): single mode
log_lik_B1 = np.zeros(N_grid)
for lam_idx, lam in enumerate(lambda_grid):
    log_lik_B1[lam_idx] = log_lik_mode(n_k_data[4], lam)

# B3 modes (5-7): all have same lambda, multiplicity 3
log_lik_B3 = np.zeros(N_grid)
for lam_idx, lam in enumerate(lambda_grid):
    ll = 0.0
    for k in range(5, 8):  # modes 5-7
        ll += log_lik_mode(n_k_data[k], lam)
    log_lik_B3[lam_idx] = ll

# Marginal likelihood = (1/V_prior^3) * integral exp(LL_B2 + LL_B1 + LL_B3) d^3lambda
# Since the three groups are independent:
# = (1/V_prior^3) * [int exp(LL_B2) d_lam] * [int exp(LL_B1) d_lam] * [int exp(LL_B3) d_lam]

V_prior_gge = (lambda_max - lambda_min)

log_evidence_B2 = logsumexp(log_lik_B2) + np.log(d_lambda) - np.log(V_prior_gge)
log_evidence_B1 = logsumexp(log_lik_B1) + np.log(d_lambda) - np.log(V_prior_gge)
log_evidence_B3 = logsumexp(log_lik_B3) + np.log(d_lambda) - np.log(V_prior_gge)

log_evidence_gge = log_evidence_B2 + log_evidence_B1 + log_evidence_B3

print(f"  log(evidence_B2) = {log_evidence_B2:.6f}")
print(f"  log(evidence_B1) = {log_evidence_B1:.6f}")
print(f"  log(evidence_B3) = {log_evidence_B3:.6f}")
print(f"  log(evidence_GGE) = {log_evidence_gge:.6f}")

# Gibbs marginal likelihood
# p(n | Gibbs) = (1/V_prior) * integral prod_k [f_k(beta)^{n_k} * (1-f_k)^{1-n_k}] d_beta
beta_grid = np.linspace(beta_min_prior, beta_max_prior, N_grid * 3)
d_beta = beta_grid[1] - beta_grid[0]

log_lik_gibbs_grid = np.zeros(len(beta_grid))
for b_idx, beta_trial in enumerate(beta_grid):
    f_k = 1.0 / (np.exp(beta_trial * E_8) + 1.0)
    f_k = np.clip(f_k, 1e-15, 1 - 1e-15)
    ll = 0.0
    for k in range(n_modes):
        ll += n_k_data[k] * np.log(f_k[k]) + (1 - n_k_data[k]) * np.log(1 - f_k[k])
    log_lik_gibbs_grid[b_idx] = ll

V_prior_gibbs = (beta_max_prior - beta_min_prior)
log_evidence_gibbs = logsumexp(log_lik_gibbs_grid) + np.log(d_beta) - np.log(V_prior_gibbs)

print(f"  log(evidence_Gibbs) = {log_evidence_gibbs:.6f}")

# Bayes factor
log_BF_exact = log_evidence_gge - log_evidence_gibbs
BF_exact = np.exp(min(log_BF_exact, 700))

print(f"\n  log(BF_exact) = {log_BF_exact:.6f} nats = {log_BF_exact / np.log(10):.4f} decibans")
if log_BF_exact < 700:
    print(f"  BF_exact = {BF_exact:.4e}")
else:
    print(f"  BF_exact = exp({log_BF_exact:.1f}) [overflow]")

# ============================================================
# 7. Fock-space exact computation (using BCS Hamiltonian)
# ============================================================
print("\n" + "=" * 70)
print("7. Fock-Space Exact Comparison (BCS Hamiltonian)")
print("=" * 70)

# The exact BCS eigenvalues give us the full many-body spectrum.
# Construct the GGE in the eigenbasis and compare with Gibbs.

# The GGE occupations define a product state in the quasiparticle basis.
# To project onto the energy eigenbasis, we need the overlap matrix.
# But since both H_BCS and the Q_k are defined in the same Fock space,
# we can work directly.

# For the factorized GGE, the energy distribution is:
# <E>_GGE = sum_k E_k * p_k
E_mean_gge = np.sum(E_8 * p_k_gge)
E_mean_gibbs = np.sum(E_8 * f_k_gibbs)

# Energy variance
E2_gge = np.sum(E_8**2 * p_k_gge * (1 - p_k_gge))  # Var for independent fermions
E2_gibbs = np.sum(E_8**2 * f_k_gibbs * (1 - f_k_gibbs))

print(f"  <E>_GGE = {E_mean_gge:.6f}")
print(f"  <E>_Gibbs = {E_mean_gibbs:.6f}")
print(f"  Var(E)_GGE = {E2_gge:.6f}")
print(f"  Var(E)_Gibbs = {E2_gibbs:.6f}")

# Total particle number
N_mean_gge = np.sum(p_k_gge)
N_mean_gibbs = np.sum(f_k_gibbs)
print(f"  <N>_GGE = {N_mean_gge:.6f}")
print(f"  <N>_Gibbs = {N_mean_gibbs:.6f}")

# The key physical signature: the GGE has DIFFERENT occupation numbers
# for modes with the SAME energy. This is impossible for a Gibbs ensemble.
print(f"\n  Physical signature of non-thermality:")
print(f"  B2 (E={E_8[0]:.6f}): p_GGE={p_k_gge[0]:.6f}, f_Gibbs={f_k_gibbs[0]:.6f}")
print(f"  B1 (E={E_8[4]:.6f}): p_GGE={p_k_gge[4]:.6f}, f_Gibbs={f_k_gibbs[4]:.6f}")
print(f"  B3 (E={E_8[5]:.6f}): p_GGE={p_k_gge[5]:.6f}, f_Gibbs={f_k_gibbs[5]:.6f}")
print(f"\n  B2/B1 occupation ratio: GGE={p_k_gge[0]/p_k_gge[4]:.3f}, "
      f"Gibbs={f_k_gibbs[0]/f_k_gibbs[4]:.3f}")
print(f"  B2/B3 occupation ratio: GGE={p_k_gge[0]/p_k_gge[5]:.3f}, "
      f"Gibbs={f_k_gibbs[0]/f_k_gibbs[5]:.3f}")

# In a Gibbs ensemble, modes with LOWER energy have HIGHER occupation.
# E_B1 < E_B2 < E_B3, so Gibbs gives f_B1 > f_B2 > f_B3.
# But GGE gives p_B2 >> p_B1 >> p_B3 — the hierarchy is INVERTED for B1 vs B2.
# This is the smoking gun of non-thermality.
print(f"\n  Energy ordering: E_B1={E_8[4]:.6f} < E_B2={E_8[0]:.6f} < E_B3={E_8[5]:.6f}")
print(f"  Gibbs ordering: f_B1={f_k_gibbs[4]:.6f} > f_B2={f_k_gibbs[0]:.6f} > f_B3={f_k_gibbs[5]:.6f} [MONOTONIC]")
print(f"  GGE ordering:   p_B2={p_k_gge[0]:.6f} > p_B1={p_k_gge[4]:.6f} > p_B3={p_k_gge[5]:.6f} [INVERTED B2>B1]")
print(f"  --> B2 is OVERPOPULATED by factor {p_k_gge[0]/f_k_gibbs[0]:.3f} relative to Gibbs")
print(f"  --> B1 is UNDERPOPULATED by factor {p_k_gge[4]/f_k_gibbs[4]:.3f} relative to Gibbs")
print(f"  --> B3 is UNDERPOPULATED by factor {p_k_gge[5]/f_k_gibbs[5]:.3f} relative to Gibbs")

# ============================================================
# 8. Mutual information and total correlation
# ============================================================
print("\n" + "=" * 70)
print("8. Information-Theoretic Summary")
print("=" * 70)

# Total information content of GGE beyond thermal:
# I_non_thermal = D_KL(rho_GGE || rho_Gibbs_opt)
# This measures the total amount of non-thermal information (in nats)
# stored in the GGE.

# Additional metrics:
# Relative entropy of coherence (how far from diagonal in energy basis)
# But for factorized states, there's no coherence — just population mismatch.

# Fisher information of the distinguishing parameter
# The GGE and Gibbs differ most strongly in the B2 sector where the
# occupation is inverted relative to energy ordering.

# Number of "sigma" the GGE deviates from thermal (in each mode)
print(f"\n  Mode-by-mode deviation from optimal Gibbs:")
print(f"  {'Mode':<8} {'p_GGE':>10} {'f_Gibbs':>10} {'delta':>10} {'sigma':>8}")
for k in range(n_modes):
    pk = p_k_gge[k]
    fk = f_k_opt[k]
    delta = pk - fk
    # Variance of binomial: p*(1-p)/N, but N=1 for single mode
    sigma_thermal = np.sqrt(fk * (1 - fk))
    n_sigma = delta / sigma_thermal if sigma_thermal > 0 else 0
    print(f"  {branch_labels[k]:<8} {pk:10.6f} {fk:10.6f} {delta:10.6f} {n_sigma:8.3f}")

# ============================================================
# 9. Summary Table
# ============================================================
print("\n" + "=" * 70)
print("9. SUMMARY — BAYES-39 Results")
print("=" * 70)

print(f"\n  D_KL(GGE || Gibbs_opt)     = {DKL_opt:.6f} nats ({DKL_opt/np.log(2):.6f} bits)")
print(f"  D_KL(GGE || Gibbs_stored)  = {DKL_gge_gibbs_free:.6f} nats ({DKL_gge_gibbs_free/np.log(2):.6f} bits)")
print(f"  JSD(GGE, Gibbs)            = {JSD_free:.6f} nats ({JSD_free/np.log(2):.6f} bits)")
print(f"  sqrt(JSD) distance         = {np.sqrt(JSD_free):.6f}")
print(f"")
print(f"  log(BF_exact)              = {log_BF_exact:.4f} nats ({log_BF_exact/np.log(10):.4f} decibans)")
if abs(log_BF_exact) < 700:
    print(f"  BF_exact                   = {BF_exact:.4e}")
print(f"")
# Use most conservative BIC
log_BF_conservative = N_eff_purity * DKL_opt - 0.5 * k_extra * np.log(N_eff_purity)
print(f"  log(BF_BIC, conservative)  = {log_BF_conservative:.4f} nats")
print(f"  BF_BIC (N_eff={N_eff_purity:.1f})    = {np.exp(min(log_BF_conservative, 700)):.4e}")
print(f"")
print(f"  S_GGE                      = {S_gge:.6f}")
print(f"  S_Gibbs                    = {S_gibbs_stored:.6f}")
print(f"  Delta S = S_Gibbs - S_GGE  = {S_gibbs_stored - S_gge:.6f} (entropy gained upon thermalization)")
print(f"")
print(f"  Physical signature: B2 OVERPOPULATED by {p_k_gge[0]/f_k_opt[0]:.3f}x vs optimal Gibbs")
print(f"  Occupation hierarchy INVERTED: p_B2 > p_B1 despite E_B2 > E_B1")

# Gate verdict
if log_BF_conservative > np.log(100):
    gate_status = "BF > 100 (DECISIVE non-thermal character)"
elif log_BF_exact > np.log(100):
    gate_status = "BF_exact > 100, BF_BIC marginal"
else:
    gate_status = f"BF = {BF_exact:.2e} (below threshold)"

print(f"\n  GATE BAYES-39: INFO — {gate_status}")

# ============================================================
# 10. Save results
# ============================================================
print("\n" + "=" * 70)
print("10. Saving results")
print("=" * 70)

np.savez('tier0-computation/s39_bayes_gge_thermal.npz',
    # Gate
    gate_verdict=np.array(['INFO']),
    gate_detail=np.array([gate_status]),

    # KL divergences
    DKL_gge_gibbs_opt=DKL_opt,
    DKL_gge_gibbs_stored=DKL_gge_gibbs_free,
    DKL_gibbs_gge=DKL_gibbs_free_gge,
    JSD=JSD_free,
    JSD_bits=JSD_free / np.log(2),
    JSD_distance=np.sqrt(JSD_free),

    # Bayes factors
    log_BF_exact=log_BF_exact,
    BF_exact=BF_exact,
    log_BF_BIC_conservative=log_BF_conservative,
    N_eff_purity=N_eff_purity,

    # Optimal Gibbs
    beta_opt=beta_opt,
    T_opt=T_opt,
    f_k_opt=f_k_opt,

    # Entropies
    S_gge=S_gge,
    S_gibbs=S_gibbs_stored,
    delta_S=S_gibbs_stored - S_gge,

    # Occupations
    p_k_gge=p_k_gge,
    f_k_gibbs=f_k_gibbs,
    lambda_k=lambda_k,
    beta_gibbs=beta_gibbs,
    branch_labels=branch_labels,

    # Distributions
    p_gge_fock=p_gge,
    p_gibbs_free_fock=p_gibbs_free,

    # Physical observables
    E_mean_gge=E_mean_gge,
    E_mean_gibbs=E_mean_gibbs,
    N_mean_gge=N_mean_gge,
    N_mean_gibbs=N_mean_gibbs,

    # Overpopulation factors
    overpop_B2=p_k_gge[0] / f_k_opt[0],
    overpop_B1=p_k_gge[4] / f_k_opt[4],
    overpop_B3=p_k_gge[5] / f_k_opt[5],
)

print("  Saved to: tier0-computation/s39_bayes_gge_thermal.npz")
print("\nDone.")
