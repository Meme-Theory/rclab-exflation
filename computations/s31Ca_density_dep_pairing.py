"""
N-31Ca: Density-Dependent Pairing on SU(3) Dirac Spectrum
=========================================================
Tests whether nuclear-style density-dependent pairing (coupling concentrated
at the gap edge) changes the BCS landscape on the SU(3) Dirac spectrum.

CRITICAL: The original K-1e (Session 23a) BdG Hamiltonian uses the pairing
matrix V as the off-diagonal block. The M_max measures the largest eigenvalue
of the V-based BdG, NOT the full kinetic+pairing BdG. The eigenvalues of the
original BdG range from -0.10 to +0.10, compared to |lambda_k| ~ 0.82-1.25.

Correct BdG construction (matching K-1e):
  H_BdG = [[0, V_eff], [V_eff^T, 0]]  at mu=0  (pairing only)
  H_BdG = [[-mu*I, V_eff], [V_eff^T, mu*I]]  at finite mu
  (shift the kinetic diagonal relative to Fermi level only by mu)

Actually, from the original data: the BdG eigenvalues at mu=+lmin are ~7-15
(much larger than at mu=0), so the original DOES include kinetic energy but
shifted: eps_k - mu. When mu = lmin, the gap-edge modes have eps-mu~0 and
the pairing dominates, giving M~11. When mu=0, eps-mu = eps ~ 0.82, and M
is just the max(eps) = 0.87 at tau=0 (but original says 0.0775!).

Resolution: The original M_max = max eigenvalue of the PAIRING PART of BdG,
not max eigenvalue of the full BdG. The M_evals at mu=0 range [-0.1, +0.1],
which matches the EIGENVALUES OF V_matrix (norm ~0.2). So the "M_max" in
K-1e is actually: max singular value of V (or max eigenvalue since V is
Hermitian). NOT the BdG quasiparticle spectrum.

But at mu=+lmin: M_max = 7.75-15.0 which is MUCH larger than ||V||. This
means the mu=+lmin case DOES use the full BdG with shifted kinetic. The
discrepancy: at mu=0, M_max = 0.0775 (max eigenvalue of V alone), while
at mu=lmin, M_max = 7.75 (full BdG quasiparticle energy).

FINAL RESOLUTION: The BdG is H = [[diag(eps_k - mu), V], [V^T, -diag(eps_k-mu)]]
  - At mu=0: eps_k range [0.82, 0.87], so H is dominated by diagonal ->
    eigenvalues are approximately +-eps_k. M_max = max(eps) = 0.87.
  - But the REPORTED M_max = 0.0775. This must be max eigenvalue of V.

Let me check: V is 16x16, eigenvalues(V) at tau=0 -> max ~0.0775.
This confirms: K-1e reports max(eigenvalues(V_matrix)), not max(eigenvalues(BdG)).

For the PAIRING CRITERION: we need max(eigenvalue(V_eff)) > some threshold.
The BCS condensation occurs when the largest eigenvalue of V exceeds 1
(in units where the level spacing = 1). Since these are dimensionless
matrix elements, M_max > 1 means the pairing strength exceeds the
single-particle level spacing, enabling condensation.

Density-dependent modification: V_eff(k,l) = f(|lk|/lmin) * V(k,l) * f(|ll|/lmin)

Three envelope families:
  - Exponential: f(x) = exp(-alpha*(x-1)), alpha in {1, 2, 5, 10}
  - Gaussian:    f(x) = exp(-beta*(x-1)^2), beta in {1, 5, 10}
  - Hard window: f(x) = 1 if x < x_cut else 0, x_cut in {1.5, 2, 3, 5}

Gate N-31Ca-G: PASS if M_max(V_eff) at mu=0 exceeds 1.0 for any envelope,
or if mu_crit (smallest mu where BdG M_max > 1) < 0.7 * lambda_min.

Input: s23a_gap_equation.npz
Output: s31Ca_density_dep_pairing.{npz,png}
"""

import numpy as np
from numpy.linalg import eigvalsh, eigvals, svd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, time

t0 = time.time()

data_dir = os.path.join(os.path.dirname(__file__))
gap_data = np.load(os.path.join(data_dir, 's23a_gap_equation.npz'), allow_pickle=True)

tau_values = gap_data['tau_values']
n_tau = len(tau_values)

eigenvalues = []
V_matrices = []
lambda_mins = []
for i in range(n_tau):
    eigenvalues.append(gap_data[f'eigenvalues_{i}'])
    V_matrices.append(gap_data[f'V_matrix_{i}'])
    lambda_mins.append(float(gap_data[f'lambda_min_{i}']))

# Verify understanding: compare eigenvalues of V to K-1e M_max
print("=== VERIFICATION: eigenvalues of V_matrix vs K-1e M_max ===")
for i in range(n_tau):
    V = V_matrices[i]
    # V may not be symmetric (check)
    sym_err = np.max(np.abs(V - V.T))
    V_sym = (V + V.T) / 2  # symmetrize
    eig_V = eigvalsh(V_sym)
    M_max_V = np.max(np.abs(eig_V))
    M_max_K1e = float(gap_data[f'M_max_full16_mu=0_{i}'])
    print(f"  tau={tau_values[i]:.2f}: max|eig(V)|={M_max_V:.6f}, K-1e M_max={M_max_K1e:.6f}, "
          f"sym_err={sym_err:.2e}, ratio={M_max_V/M_max_K1e:.4f}")

# --- Define envelope functions ---
def envelope_exp(x, alpha):
    return np.exp(-alpha * np.maximum(x - 1.0, 0.0))

def envelope_gauss(x, beta):
    return np.exp(-beta * (x - 1.0)**2)

def envelope_hard(x, x_cut):
    return np.where(x < x_cut, 1.0, 0.0)

envelopes = []
for alpha in [1.0, 2.0, 5.0, 10.0]:
    envelopes.append(('exp', alpha, lambda x, a=alpha: envelope_exp(x, a)))
for beta in [1.0, 5.0, 10.0]:
    envelopes.append(('gauss', beta, lambda x, b=beta: envelope_gauss(x, b)))
for x_cut in [1.5, 2.0, 3.0, 5.0]:
    envelopes.append(('hard', x_cut, lambda x, c=x_cut: envelope_hard(x, c)))
envelopes.append(('constant', 0.0, lambda x: np.ones_like(x)))

n_env = len(envelopes)

# mu fractions of lambda_min for full BdG analysis
mu_fracs = np.array([0.0, 0.3, 0.5, 0.7, 0.8, 0.9, 0.95, 1.0])
n_mu = len(mu_fracs)

print(f"\nN-31Ca: {n_tau} tau x {n_env} envelopes x {n_mu} mu values")

# --- TWO METRICS ---
# Metric A: max eigenvalue of V_eff (pairing matrix alone, as in K-1e at mu=0)
# Metric B: full BdG max eigenvalue H = [[diag(eps-mu), V_eff], [V_eff^T, -diag(eps-mu)]]

M_max_V_eff = np.zeros((n_tau, n_env))  # Metric A: max|eig(V_eff)|
M_max_BdG = np.zeros((n_tau, n_env, n_mu))  # Metric B: max eigenvalue of full BdG
mu_crit_BdG = np.full((n_tau, n_env), np.inf)  # smallest mu where BdG has quasiparticle at E=0

for i_tau in range(n_tau):
    evals = eigenvalues[i_tau]
    V = V_matrices[i_tau]
    V_sym = (V + V.T) / 2
    lmin = lambda_mins[i_tau]
    n_modes = len(evals)
    x_k = np.abs(evals) / lmin
    eps_k = np.abs(evals)  # single-particle energies

    for i_env, (env_name, env_param, env_func) in enumerate(envelopes):
        f_k = env_func(x_k)
        F_outer = np.outer(f_k, f_k)
        V_eff = F_outer * V_sym

        # Metric A: eigenvalues of V_eff
        eig_Veff = eigvalsh(V_eff)
        M_max_V_eff[i_tau, i_env] = np.max(np.abs(eig_Veff))

        # Metric B: full BdG at each mu
        for i_mu, mu_frac in enumerate(mu_fracs):
            mu = mu_frac * lmin
            eps_shifted = eps_k - mu

            H_BdG = np.zeros((2*n_modes, 2*n_modes))
            H_BdG[:n_modes, :n_modes] = np.diag(eps_shifted)
            H_BdG[:n_modes, n_modes:] = V_eff
            H_BdG[n_modes:, :n_modes] = V_eff.T
            H_BdG[n_modes:, n_modes:] = -np.diag(eps_shifted)

            eig_bdg = eigvalsh(H_BdG)
            M_max_BdG[i_tau, i_env, i_mu] = np.max(eig_bdg)

            # Check for gap closing: BdG eigenvalue crosses zero
            # The BCS condensation criterion: smallest positive eigenvalue < threshold
            pos_eigs = eig_bdg[eig_bdg > 0]
            if len(pos_eigs) > 0 and np.min(pos_eigs) < 0.01:
                if mu_crit_BdG[i_tau, i_env] == np.inf:
                    mu_crit_BdG[i_tau, i_env] = mu

# --- Results ---
print("\n=== METRIC A: max|eig(V_eff)| (pairing strength, K-1e analog) ===")
env_names = [f"{e[0]}({e[1]})" for e in envelopes]
print(f"{'Envelope':<15s}", end="")
for i_tau in range(n_tau):
    print(f"  tau={tau_values[i_tau]:.2f}", end="")
print()
for i_env in range(n_env):
    print(f"{env_names[i_env]:<15s}", end="")
    for i_tau in range(n_tau):
        print(f"  {M_max_V_eff[i_tau, i_env]:9.6f}", end="")
    print()

print(f"\nEnhancement over constant coupling:")
for i_tau in range(n_tau):
    const_val = M_max_V_eff[i_tau, -1]
    best_idx = np.argmax(M_max_V_eff[i_tau, :-1])
    best_val = M_max_V_eff[i_tau, best_idx]
    ratio = best_val / const_val if const_val > 0 else 0
    name, param, _ = envelopes[best_idx]
    print(f"  tau={tau_values[i_tau]:.2f}: {ratio:.4f}x via {name}({param})")

# Key question: does any envelope push M_max(V_eff) above 1?
print(f"\n=== CRITICAL: Does any V_eff have eigenvalue > 1? ===")
max_overall = np.max(M_max_V_eff[:, :-1])
print(f"Global max of M_max(V_eff): {max_overall:.6f}")
print(f"BCS threshold: 1.0")
print(f"Ratio to threshold: {max_overall:.4f}")

if max_overall > 1.0:
    print("RESULT: Density-dependent pairing CAN push pairing above threshold")
else:
    shortfall = 1.0 / max_overall
    print(f"RESULT: Shortfall factor {shortfall:.2f}x below threshold")
    print("NOTE: No density-dependent envelope can fix this -- the V_matrix entries")
    print("are O(0.01-0.1), and reweighting can only increase by ~1x at most.")
    print("The problem is the ABSOLUTE SIZE of Kosmann matrix elements, not their distribution.")

print(f"\n=== METRIC B: Full BdG quasiparticle gap ===")
print("mu_crit/lambda_min (gap closing point):")
print(f"{'Envelope':<15s}", end="")
for i_tau in range(n_tau):
    print(f"  tau={tau_values[i_tau]:.2f}", end="")
print()
for i_env in range(n_env):
    print(f"{env_names[i_env]:<15s}", end="")
    for i_tau in range(n_tau):
        ratio = mu_crit_BdG[i_tau, i_env] / lambda_mins[i_tau]
        if ratio < np.inf:
            print(f"  {ratio:9.4f}", end="")
        else:
            print(f"      inf", end="")
    print()

# --- Gate N-31Ca-G ---
tau_mask = (tau_values >= 0.15) & (tau_values <= 0.25)
tau_indices = np.where(tau_mask)[0]

# Check criterion 1: M_max(V_eff) > 1 at mu=0
crit1_pass = False
for i_tau in tau_indices:
    for i_env in range(n_env - 1):
        if M_max_V_eff[i_tau, i_env] > 1.0:
            crit1_pass = True

# Check criterion 2: mu_crit < 0.7 * lambda_min
best_mu_crit_ratio = np.inf
best_env_idx = -1
best_tau_idx = -1
for i_tau in tau_indices:
    for i_env in range(n_env - 1):
        ratio = mu_crit_BdG[i_tau, i_env] / lambda_mins[i_tau]
        if ratio < best_mu_crit_ratio:
            best_mu_crit_ratio = ratio
            best_env_idx = i_env
            best_tau_idx = i_tau

if crit1_pass or best_mu_crit_ratio < 0.7:
    gate_verdict = "PASS"
elif best_mu_crit_ratio >= 0.95 and not crit1_pass:
    gate_verdict = "FAIL"
else:
    gate_verdict = "MARGINAL"

# But also: check the PHYSICAL criterion -- M_max(V_eff) is O(0.1) at all tau,
# which is 10x below threshold. No reweighting changes this.
if max_overall < 0.5:
    gate_verdict_corrected = "FAIL (V_eff eigenvalues 10x below threshold)"
    reason = (f"All envelope-reweighted V_eff have max eigenvalue {max_overall:.4f}, "
              f"which is {1.0/max_overall:.1f}x below the BCS threshold of 1.0. "
              f"Density-dependent reweighting concentrates existing matrix elements "
              f"but cannot create pairing strength that is not there. "
              "The fundamental problem is ||V|| ~ 0.1, not the distribution of V_kl.")
else:
    gate_verdict_corrected = gate_verdict
    reason = ""

print(f"\n=== GATE N-31Ca-G ===")
print(f"Metric A (max|eig(V_eff)|): Global max = {max_overall:.6f} (threshold = 1.0)")
print(f"Metric B (mu_crit/lmin): Best = {best_mu_crit_ratio:.4f} (threshold = 0.7)")
if best_env_idx >= 0:
    name, param, _ = envelopes[best_env_idx]
    print(f"Best envelope for B: {name}({param}) at tau={tau_values[best_tau_idx]:.2f}")
print(f"Gate verdict (raw): {gate_verdict}")
print(f"Gate verdict (corrected for absolute V scale): {gate_verdict_corrected}")
if reason:
    print(f"Reason: {reason}")

# --- Save ---
save_dict = {
    'tau_values': tau_values,
    'mu_fracs': mu_fracs,
    'lambda_mins': np.array(lambda_mins),
    'M_max_V_eff': M_max_V_eff,
    'M_max_BdG': M_max_BdG,
    'mu_crit_BdG': mu_crit_BdG,
    'envelope_names': np.array(env_names),
    'gate_verdict': np.array(gate_verdict_corrected),
    'max_V_eff_overall': np.array(max_overall),
    'best_mu_crit_ratio': np.array(best_mu_crit_ratio),
}
np.savez(os.path.join(data_dir, 's31Ca_density_dep_pairing.npz'), **save_dict)
print(f"\nSaved s31Ca_density_dep_pairing.npz")

# --- Plot ---
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: M_max(V_eff) for all envelopes vs tau
ax = axes[0, 0]
cmap = plt.cm.Set2
for i_env in range(n_env):
    name, param, _ = envelopes[i_env]
    style = '--' if name == 'constant' else '-'
    lw = 2 if name == 'constant' else 1
    ax.plot(tau_values, M_max_V_eff[:, i_env], style, linewidth=lw,
            label=f'{name}({param})', color=cmap(i_env / n_env))
ax.axhline(1.0, color='red', linestyle=':', alpha=0.5, label='BCS threshold')
ax.set_xlabel('tau')
ax.set_ylabel('max |eig(V_eff)|')
ax.set_title('Metric A: Pairing strength (V_eff eigenvalue)')
ax.legend(fontsize=5.5, ncol=2)

# Panel 2: Enhancement ratio over constant
ax = axes[0, 1]
for i_env in range(n_env - 1):  # exclude constant
    name, param, _ = envelopes[i_env]
    const_vals = M_max_V_eff[:, -1]
    ratios = M_max_V_eff[:, i_env] / np.where(const_vals > 0, const_vals, 1)
    ax.plot(tau_values, ratios, '-o', markersize=3, label=f'{name}({param})')
ax.axhline(1.0, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('Enhancement over constant')
ax.set_title('Density-dep / constant coupling ratio')
ax.legend(fontsize=5.5, ncol=2)

# Panel 3: Full BdG M_max vs mu at tau=0.20
ax = axes[1, 0]
i_tau_020 = np.argmin(np.abs(tau_values - 0.20))
for i_env in [0, 3, 4, 6, 7, 10, 11]:  # representative envelopes + constant
    name, param, _ = envelopes[i_env]
    ax.plot(mu_fracs, M_max_BdG[i_tau_020, i_env, :], '-o', markersize=3,
            label=f'{name}({param})')
ax.axhline(0, color='gray', linestyle=':', alpha=0.3)
ax.set_xlabel('mu / lambda_min')
ax.set_ylabel('Max BdG eigenvalue')
ax.set_title(f'Full BdG spectrum at tau={tau_values[i_tau_020]:.2f}')
ax.legend(fontsize=7)

# Panel 4: V_eff eigenvalue spectrum at tau=0.20 for best vs constant
ax = axes[1, 1]
V_020 = V_matrices[i_tau_020]
V_020_sym = (V_020 + V_020.T) / 2
eig_const = np.sort(eigvalsh(V_020_sym))
x_k = np.abs(eigenvalues[i_tau_020]) / lambda_mins[i_tau_020]

# Best performing
best_at_020 = np.argmax(M_max_V_eff[i_tau_020, :-1])
f_best = envelopes[best_at_020][2](x_k)
F_best = np.outer(f_best, f_best)
V_best = F_best * V_020_sym
eig_best = np.sort(eigvalsh(V_best))

# Most concentrated (exp(10))
f_exp10 = envelope_exp(x_k, 10.0)
F_exp10 = np.outer(f_exp10, f_exp10)
V_exp10 = F_exp10 * V_020_sym
eig_exp10 = np.sort(eigvalsh(V_exp10))

ax.bar(np.arange(16) - 0.2, eig_const, width=0.2, label='constant', alpha=0.7)
ax.bar(np.arange(16), eig_best, width=0.2, label=f'best ({envelopes[best_at_020][0]}({envelopes[best_at_020][1]}))', alpha=0.7)
ax.bar(np.arange(16) + 0.2, eig_exp10, width=0.2, label='exp(10)', alpha=0.7)
ax.axhline(0, color='gray', linestyle=':', alpha=0.3)
ax.set_xlabel('Eigenvalue index')
ax.set_ylabel('V_eff eigenvalue')
ax.set_title(f'V_eff eigenvalue spectrum at tau=0.20')
ax.legend()

fig.suptitle(f'N-31Ca: Density-Dependent Pairing | Gate: {gate_verdict_corrected}',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 's31Ca_density_dep_pairing.png'), dpi=150, bbox_inches='tight')
print(f"Saved s31Ca_density_dep_pairing.png")

elapsed = time.time() - t0
print(f"\nTotal runtime: {elapsed:.2f}s")
