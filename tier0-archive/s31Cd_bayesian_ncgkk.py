"""
N-31Cd: Bayesian NCG-KK Scale Tension Assessment
Session 31Ca -- Baptista agent

Quantifies the information-theoretic content of the B-31nck FAIL verdict
(Lambda_SA / M_KK = 10^6 at tau=0.21) using Bayesian methodology.

Log-uniform prior on M_KK in [10^14, 10^18] GeV.
Likelihood: L(M_KK) = exp(-(log10(Lambda_SA/M_KK))^2 / (2*sigma^2))
Posterior, Bayes factor, KL divergence computed analytically.
Sensitivity over sigma in {1, 2, 3, 5}.

Gate N-31Cd-G: INFORMATIVE if D_KL > 1 nat, DECISIVE if BF < 0.01.

Input: s31Ba_nck_tau021.npz, s30b_rge_running.npz
Output: s31Cd_bayesian_ncgkk.{npz,png}
"""

import numpy as np
from scipy import integrate
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Load input data ──
nck = np.load('tier0-computation/s31Ba_nck_tau021.npz', allow_pickle=True)
rge = np.load('tier0-computation/s30b_rge_running.npz', allow_pickle=True)

Lambda_SA = float(nck['Lambda_SA'])  # ~1.02e22 GeV at tau=0.21
tau_val = float(nck['tau'])
ratio_at_ref = float(nck['ratio'])  # Lambda_SA / M_KK_ref

# SM parameters for cross-check
alpha_1_inv_MZ = 59.0
alpha_2_inv_MZ = 29.6
b_1 = 41.0 / 10.0
b_2 = -19.0 / 6.0

print(f"Lambda_SA at tau={tau_val}: {Lambda_SA:.4e} GeV")
print(f"Lambda_SA / M_KK_ref(1e16): {ratio_at_ref:.4e}")

# ── Prior definition ──
log10_MKK_min = 14.0
log10_MKK_max = 18.0
log10_range = log10_MKK_max - log10_MKK_min  # 4 decades

log10_Lambda_SA = np.log10(Lambda_SA)
print(f"log10(Lambda_SA) = {log10_Lambda_SA:.4f}")

# The log-ratio at any M_KK:
# log10(Lambda_SA / M_KK) = log10(Lambda_SA) - log10(M_KK)
# At M_KK = 10^16: log10 ratio = 22.009 - 16 = 6.009

# ── Integration grid in log10(M_KK) ──
N_grid = 10000
log10_MKK = np.linspace(log10_MKK_min, log10_MKK_max, N_grid)
d_log10 = log10_MKK[1] - log10_MKK[0]

# Prior: uniform in log10(M_KK) => p(log10_MKK) = 1/log10_range
prior = np.ones(N_grid) / log10_range

# ── Sensitivity sweep over sigma ──
sigmas = np.array([1.0, 2.0, 3.0, 5.0])

results = {}
for sigma in sigmas:
    # Log-ratio for each M_KK value
    log_ratio = log10_Lambda_SA - log10_MKK  # log10(Lambda_SA/M_KK)

    # Likelihood: L(M_KK) = exp(-log_ratio^2 / (2*sigma^2))
    chi2 = log_ratio**2 / sigma**2
    likelihood = np.exp(-chi2 / 2.0)

    # Unnormalized posterior
    posterior_unnorm = likelihood * prior

    # Evidence (marginal likelihood) = integral of L * prior
    evidence = np.trapezoid(posterior_unnorm, log10_MKK)

    # Normalized posterior
    posterior = posterior_unnorm / evidence if evidence > 0 else posterior_unnorm

    # Posterior mode
    mode_idx = np.argmax(posterior)
    mode_log10 = log10_MKK[mode_idx]

    # Credible intervals (68% and 95%)
    cumulative = np.cumsum(posterior) * d_log10
    cumulative /= cumulative[-1]

    ci68_lo = log10_MKK[np.searchsorted(cumulative, 0.16)]
    ci68_hi = log10_MKK[np.searchsorted(cumulative, 0.84)]
    ci95_lo = log10_MKK[np.searchsorted(cumulative, 0.025)]
    ci95_hi = log10_MKK[np.searchsorted(cumulative, 0.975)]

    # Bayes Factor: evidence for compatibility vs incompatibility
    # Under H0 (compatible): likelihood ~ 1 (ratio ~ 1, log_ratio ~ 0)
    # Under H1 (random): prior alone = uniform
    # BF = evidence / (1/range) = evidence * range... but more precisely:
    # BF = P(data | compatible) / P(data | incompatible)
    # P(data | compatible) = evidence (integral of L * prior)
    # P(data | incompatible) = 1 (always "predicts" the data with flat likelihood)
    # So BF = evidence / (1) ... but we need to be careful.
    #
    # The CORRECT Bayes factor is:
    # H_compatible: log_ratio ~ Normal(0, sigma)  => L as defined
    # H_incompatible: M_KK uniform on prior (no constraint from NCG)
    # BF = integral[L(M_KK) * prior(M_KK)] d(M_KK) / integral[1 * prior(M_KK)] d(M_KK)
    #    = evidence / 1 = evidence
    # Since prior is normalized, integral of prior = 1.
    # And under H_incompatible, the "likelihood" is 1 everywhere.
    BF = evidence  # P(data | H_compatible) / P(data | H_incompatible)

    # KL divergence: D_KL(posterior || prior)
    # = integral posterior * log(posterior / prior) d(log10_MKK)
    mask = posterior > 1e-300  # avoid log(0)
    kl_integrand = np.zeros(N_grid)
    kl_integrand[mask] = posterior[mask] * np.log(posterior[mask] / prior[mask])
    D_KL = np.trapezoid(kl_integrand, log10_MKK)

    # Store
    key = f"sigma_{sigma:.0f}"
    results[key] = {
        'sigma': sigma,
        'evidence': evidence,
        'BF': BF,
        'D_KL': D_KL,
        'mode_log10_MKK': mode_log10,
        'ci68': (ci68_lo, ci68_hi),
        'ci95': (ci95_lo, ci95_hi),
        'posterior': posterior,
        'likelihood': likelihood,
    }

    print(f"\n--- sigma = {sigma:.0f} ---")
    print(f"  Evidence (BF): {BF:.6e}")
    print(f"  D_KL: {D_KL:.4f} nats")
    print(f"  Posterior mode: log10(M_KK) = {mode_log10:.2f} ({10**mode_log10:.2e} GeV)")
    print(f"  68% CI: [{ci68_lo:.2f}, {ci68_hi:.2f}]")
    print(f"  95% CI: [{ci95_lo:.2f}, {ci95_hi:.2f}]")
    print(f"  Mode in GUT window [15,17]? {'YES' if 15 <= mode_log10 <= 17 else 'NO'}")

# ── RGE cross-check ──
# At what M_KK do gauge couplings unify?
# alpha_i^{-1}(M) = alpha_i^{-1}(M_Z) - b_i/(2*pi) * ln(M/M_Z)
# Unification: alpha_1(M_U) = alpha_2(M_U)
# => alpha_1^{-1}(M_Z) - b_1/(2*pi)*ln(M_U/M_Z) = alpha_2^{-1}(M_Z) - b_2/(2*pi)*ln(M_U/M_Z)
# => (b_2 - b_1)/(2*pi) * ln(M_U/M_Z) = alpha_2^{-1}(M_Z) - alpha_1^{-1}(M_Z)
M_Z = 91.2  # GeV
delta_alpha_inv = alpha_2_inv_MZ - alpha_1_inv_MZ  # 29.6 - 59.0 = -29.4
delta_b = b_2 - b_1  # -19/6 - 41/10 = -3.167 - 4.1 = -7.267
ln_MU_MZ = delta_alpha_inv / (delta_b / (2 * np.pi))
log10_M_unif = np.log10(M_Z) + ln_MU_MZ / np.log(10)
M_unif = 10**log10_M_unif

print(f"\n=== RGE Cross-Check ===")
print(f"  SM unification scale: {M_unif:.4e} GeV (log10 = {log10_M_unif:.2f})")
print(f"  Lambda_SA / M_unif = {Lambda_SA / M_unif:.4e}")
print(f"  log10(Lambda_SA / M_unif) = {log10_Lambda_SA - log10_M_unif:.2f}")

# ── Gate classification ──
sigma_ref = 3.0  # reference sigma
r = results[f"sigma_{sigma_ref:.0f}"]
is_informative = r['D_KL'] > 1.0
is_decisive = r['BF'] < 0.01
mode_in_gut = 15.0 <= r['mode_log10_MKK'] <= 17.0

print(f"\n=== GATE N-31Cd-G ===")
print(f"  D_KL = {r['D_KL']:.4f} nats (threshold: 1.0)")
print(f"  BF = {r['BF']:.6e} (threshold: 0.01)")
print(f"  Mode at log10(M_KK) = {r['mode_log10_MKK']:.2f}")
if is_decisive:
    verdict = "DECISIVE"
    print(f"  VERDICT: DECISIVE -- BF = {r['BF']:.2e} < 0.01, strong evidence for NCG-KK incompatibility")
elif is_informative:
    verdict = "INFORMATIVE"
    print(f"  VERDICT: INFORMATIVE -- D_KL = {r['D_KL']:.2f} > 1 nat, B-31nck carries significant information")
else:
    verdict = "INCONCLUSIVE"
    print(f"  VERDICT: INCONCLUSIVE -- D_KL = {r['D_KL']:.2f} < 1 nat")

if not mode_in_gut:
    print(f"  NOTE: Posterior mode ({r['mode_log10_MKK']:.2f}) OUTSIDE standard GUT window [15, 17]")

# ── Save results ──
save_dict = {
    'Lambda_SA': Lambda_SA,
    'tau': tau_val,
    'log10_Lambda_SA': log10_Lambda_SA,
    'log10_MKK': log10_MKK,
    'prior': prior,
    'sigmas': sigmas,
    'verdict': verdict,
    'log10_M_unif': log10_M_unif,
    'M_unif': M_unif,
}

for sigma in sigmas:
    key = f"sigma_{sigma:.0f}"
    r = results[key]
    save_dict[f'posterior_{key}'] = r['posterior']
    save_dict[f'likelihood_{key}'] = r['likelihood']
    save_dict[f'BF_{key}'] = r['BF']
    save_dict[f'D_KL_{key}'] = r['D_KL']
    save_dict[f'mode_{key}'] = r['mode_log10_MKK']
    save_dict[f'ci68_{key}'] = np.array(r['ci68'])
    save_dict[f'ci95_{key}'] = np.array(r['ci95'])

np.savez('tier0-computation/s31Cd_bayesian_ncgkk.npz', **save_dict)
print("\nSaved: tier0-computation/s31Cd_bayesian_ncgkk.npz")

# ── Plot ──
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Posterior for all sigma values
ax = axes[0, 0]
colors = ['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4']
for i, sigma in enumerate(sigmas):
    key = f"sigma_{sigma:.0f}"
    r = results[key]
    ax.plot(log10_MKK, r['posterior'], color=colors[i], linewidth=1.5,
            label=f'sigma={sigma:.0f}, BF={r["BF"]:.2e}')
ax.axvline(log10_Lambda_SA, color='red', linestyle='--', alpha=0.5, label=f'log10(Lambda_SA)={log10_Lambda_SA:.1f}')
ax.axvspan(15, 17, alpha=0.1, color='green', label='GUT window')
ax.set_xlabel('log10(M_KK / GeV)')
ax.set_ylabel('Posterior density')
ax.set_title('N-31Cd: Posterior p(M_KK | NCG-KK constraint)')
ax.legend(fontsize=8)
ax.set_xlim(log10_MKK_min, log10_MKK_max)

# Panel 2: Likelihood
ax = axes[0, 1]
for i, sigma in enumerate(sigmas):
    key = f"sigma_{sigma:.0f}"
    r = results[key]
    ax.plot(log10_MKK, r['likelihood'], color=colors[i], linewidth=1.5,
            label=f'sigma={sigma:.0f}')
ax.axvline(log10_Lambda_SA, color='red', linestyle='--', alpha=0.5)
ax.axvspan(15, 17, alpha=0.1, color='green')
ax.set_xlabel('log10(M_KK / GeV)')
ax.set_ylabel('Likelihood L(M_KK)')
ax.set_title('NCG-KK compatibility likelihood')
ax.legend(fontsize=9)
ax.set_xlim(log10_MKK_min, log10_MKK_max)

# Panel 3: BF and D_KL vs sigma
ax = axes[1, 0]
bfs = [results[f"sigma_{s:.0f}"]['BF'] for s in sigmas]
dkls = [results[f"sigma_{s:.0f}"]['D_KL'] for s in sigmas]
ax2 = ax.twinx()
l1 = ax.semilogy(sigmas, bfs, 'ro-', markersize=8, linewidth=2, label='Bayes Factor')
ax.axhline(0.01, color='red', linestyle=':', alpha=0.5, label='BF=0.01 (decisive)')
l2 = ax2.plot(sigmas, dkls, 'bs-', markersize=8, linewidth=2, label='D_KL (nats)')
ax2.axhline(1.0, color='blue', linestyle=':', alpha=0.5, label='D_KL=1 (informative)')
ax.set_xlabel('sigma (log-decades tolerance)')
ax.set_ylabel('Bayes Factor', color='red')
ax2.set_ylabel('D_KL (nats)', color='blue')
ax.set_title('Sensitivity: BF and D_KL vs sigma')
lines = l1 + l2
labels = [l.get_label() for l in lines]
ax.legend(lines, labels, fontsize=9)

# Panel 4: Summary table
ax = axes[1, 1]
ax.axis('off')
table_data = [['sigma', 'BF', 'D_KL (nats)', 'Mode (log10)', '68% CI', 'Verdict']]
for sigma in sigmas:
    key = f"sigma_{sigma:.0f}"
    r = results[key]
    bf_str = f"{r['BF']:.2e}"
    dkl_str = f"{r['D_KL']:.2f}"
    mode_str = f"{r['mode_log10_MKK']:.1f}"
    ci_str = f"[{r['ci68'][0]:.1f}, {r['ci68'][1]:.1f}]"
    if r['BF'] < 0.01:
        verd = "DECISIVE"
    elif r['D_KL'] > 1:
        verd = "INFORMATIVE"
    else:
        verd = "INCONCLUSIVE"
    table_data.append([f"{sigma:.0f}", bf_str, dkl_str, mode_str, ci_str, verd])

table = ax.table(cellText=table_data, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.0, 1.5)
# Header row bold
for j in range(len(table_data[0])):
    table[0, j].set_text_props(fontweight='bold')
ax.set_title(f'N-31Cd Gate: {verdict} at sigma=3\n'
             f'Lambda_SA = {Lambda_SA:.2e} GeV, log10 = {log10_Lambda_SA:.2f}\n'
             f'SM unification: {M_unif:.2e} GeV (log10 = {log10_M_unif:.1f})',
             fontsize=10)

plt.tight_layout()
plt.savefig('tier0-computation/s31Cd_bayesian_ncgkk.png', dpi=150, bbox_inches='tight')
print("Saved: tier0-computation/s31Cd_bayesian_ncgkk.png")

print("\n=== COMPUTATION COMPLETE ===")
print(f"Gate N-31Cd-G: {verdict}")
print(f"  sigma=3 reference: BF = {results['sigma_3']['BF']:.6e}, D_KL = {results['sigma_3']['D_KL']:.4f} nats")
print(f"  Posterior mode: log10(M_KK) = {results['sigma_3']['mode_log10_MKK']:.2f}")
