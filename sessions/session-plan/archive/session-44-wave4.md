## III-d. Wave 4: Diagnostics (4 tasks, partially depends on W1-1)

### W4-1: Strutinsky Smoothing Diagnostic (STRUTINSKY-DIAG-44)

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are applying the Strutinsky energy averaging method to the 992-mode Dirac spectrum to decompose the spectral action into smooth (liquid-drop) and oscillating (shell correction) components. The Strutinsky smoothing parameter gamma determines the split between UV-smooth and oscillating parts. Identifying the plateau region constrains the regime of validity of the heat kernel expansion.

**Context.** S43 UV/IR workshop (Nazarewicz R1 Section 2c): "Lambda in the spectral action plays the role of the Strutinsky smoothing parameter gamma. At Lambda/lambda_max ~ 10^{2.2}, the framework is in the over-smoothing regime: gamma/E_F ~ 1." This means the heat kernel expansion has washed out all microscopic content.

In nuclear physics (Paper 13 in `researchers/Nazarewicz/`), the Strutinsky prescription requires d << gamma << E_F where d is the mean level spacing and E_F is the Fermi energy. The "plateau condition" is that the smoothed energy E_smooth(gamma) is independent of gamma over some range. If no plateau exists, the decomposition is invalid.

**Computation Steps**:

1. Load all 992 eigenvalues from `tier0-computation/s42_hauser_feshbach.npz` with multiplicities.

2. **Construct the discrete level density.** g(E) = sum_k d_k delta(E - |lambda_k|). Use binning with bin width 0.01 M_KK.

3. **Strutinsky smoothing.** Convolve g(E) with a Gaussian of width gamma:

   $$\tilde{g}(E, \gamma) = \int g(E') \frac{1}{\gamma\sqrt{2\pi}} e^{-(E-E')^2/(2\gamma^2)} \, dE'$$

   Compute for gamma = 0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00, 5.00 M_KK.

4. **Smoothed energy.** E_smooth(gamma) = integral_0^{E_F} tilde{g}(E, gamma) E dE.

5. **Shell correction.** delta_E(gamma) = E_discrete - E_smooth(gamma).

6. **Plateau identification.** Plot E_smooth(gamma) and delta_E(gamma) vs gamma. Identify the plateau region where d(E_smooth)/d(gamma) ~ 0. The plateau width determines the regime where the Strutinsky decomposition is valid.

7. **Comparison to heat kernel.** The Seeley-DeWitt expansion S = f_0 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f_4 a_4 corresponds to E_smooth with gamma ~ Lambda. If the plateau exists at gamma ~ M_KK (the spectral edge), the heat kernel is valid. If no plateau exists below gamma ~ 10 M_KK, the heat kernel is in the over-smoothing regime.

8. **Report.** Plateau range [gamma_min, gamma_max], smoothed energy vs heat kernel, shell correction magnitude and sign.

**Pre-registered gate STRUTINSKY-DIAG-44**:
- PASS: Plateau identified with width > 1 decade (heat kernel regime valid)
- FAIL: No plateau (heat kernel in over-smoothing regime, confirming UV/IR workshop diagnosis)
- INFO: Narrow plateau (<0.5 decade) with marginal agreement

**Input files**:
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s36_sfull_tau_stabilization.npz`
- `tier0-computation/s42_constants_snapshot.npz`

**Output files**:
- Script: `tier0-computation/s44_strutinsky_diag.py`
- Data: `tier0-computation/s44_strutinsky_diag.npz`
- Plot: `tier0-computation/s44_strutinsky_diag.png`

**Working paper section**: W4-1

---

### W4-2: Self-Consistent G_N from Bosonic a_2 (INDUCED-G-44)

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: LOW

**Prompt**:

You are computing the self-consistent G_N from the bosonic a_2 Seeley-DeWitt coefficient alone (since S_F^Connes = 0, the fermionic spectral action vanishes). This provides a cross-check to SAKHAROV-GN-44 (W1-1) and determines whether the gravity route and gauge route M_KK values can be reconciled.

**Context.** S43 CC workshop emerged E2: S_F^Connes = 0 by BDI symmetry. G_N comes from the BOSONIC spectral action only. The bosonic a_2 coefficient encodes the Einstein-Hilbert term. S43 MKK-BAYES-43: 0.70-decade tension between gravity route (M_KK = 10^{16.87}) and gauge route (M_KK = 10^{17.57}).

The bosonic spectral action is the trace over fluctuation operators (connection Laplacians, not the Dirac operator). The a_2 coefficient for a connection Laplacian on a vector bundle over K is:

$$a_2(\nabla^2_A) = \frac{1}{(4\pi)^{d/2}} \int_K \left[\frac{R_K}{6} \cdot \text{rk}(A) - \text{tr}(F_{A}^2)\right] \, dV_K$$

where R_K is the Ricci scalar of K and F_A is the gauge field strength.

**Computation Steps**:

1. Load constants from `tier0-computation/s42_constants_snapshot.npz` and metric data.

2. **Bosonic a_2.** The bosonic contributions to G_N come from: graviton fluctuations on K (symmetric TT tensors), gauge field fluctuations (connection 1-forms), and scalar fluctuations (conformal factor). For each:
   - TT tensors: a_2^{TT} from Lichnerowicz Laplacian on symmetric 2-tensors
   - Gauge: a_2^{gauge} from Hodge Laplacian on 1-forms
   - Scalar: a_2^{scalar} from scalar Laplacian

3. **Total bosonic a_2.** Sum all contributions:

   $$a_2^{\text{bos}} = a_2^{TT} + a_2^{\text{gauge}} + a_2^{\text{scalar}}$$

4. **G_N from bosonic a_2.** Extract:

   $$\frac{1}{16\pi G_N^{\text{bos}}} = f_2 \Lambda^2 \cdot a_2^{\text{bos}}$$

5. **Comparison.** Report:
   - G_N^{bos} (bosonic spectral action only)
   - G_N^{Dirac} (from Dirac a_2, used in S42)
   - G_N^{Sakharov} (from W1-1 if available)
   - G_N^{obs}

6. **Reconciliation.** If G_N^{bos} agrees with G_N^{Sakharov}, the cutoff function f is self-consistently determined. If not, the 0.70-decade tension reflects a genuine functional form discrepancy.

**Pre-registered gate INDUCED-G-44**:
- PASS: G_N^{bos} within 1 OOM of G_N^{Sakharov} (self-consistent)
- FAIL: > 3 OOM discrepancy (functional form genuinely wrong)
- INFO: intermediate

**Input files**:
- `tier0-computation/s42_constants_snapshot.npz`
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s43_lichnerowicz.npz`
- Papers 40, 55 in `researchers/Baptista/`

**Output files**:
- Script: `tier0-computation/s44_induced_g.py`
- Data: `tier0-computation/s44_induced_g.npz`
- Plot: `tier0-computation/s44_induced_g.png`

**Working paper section**: W4-2

---

### W4-3: Friedmann-BCS epsilon_H Audit After E-to-F Correction (FRIEDMANN-BCS-AUDIT-44)

**Agent**: `einstein-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**:

You are auditing the FRIEDMANN-BCS-43 result (epsilon_H shortfall 60,861x) after accounting for the E-vs-F correction identified in the S43 audit. The question: does replacing S(tau) with E(tau) in the Friedmann equation change the epsilon_H shortfall enough to matter?

**Context.** S43 E-vs-F audit Instance 3: epsilon_H = (dV/dtau)^2 / (V^2 * Z). Since dV/dtau = dE/dtau (derivatives unchanged) and V -> E = f*V: epsilon_H -> epsilon_H / f^2. If f < 1 (E < S): epsilon_H INCREASES. If f > 1 (E > S): epsilon_H DECREASES. For the conclusion to flip, need f ~ 250 (impossible for a Legendre correction).

S43 FRIEDMANN-BCS-43: n_s constraint surface EMPTY. epsilon_H = 1.4e-6 (BCS-only, no tilt) or 3.0 (stiff matter, too much tilt). Target epsilon_H = 0.0176 requires 60,861x more energy than BCS provides.

**Computation Steps**:

1. Load from `tier0-computation/s43_friedmann_bcs.npz` (if exists, otherwise from source data: `s36_sfull_tau_stabilization.npz`, `s42_gradient_stiffness.npz`, `s38_cc_instanton.npz`).

2. **E-vs-F correction factor.** The correction is f = E/S where E = S - sum_k T_k (dS/dT_k). Since dS/dT_k is uncomputed, estimate the correction:
   - Lower bound: f = 1 (no correction, E = S)
   - Upper bound: f = E/S ~ 1 + T_max * delta(mode structure) / S ~ 1 + O(10^{-3})
   - The GGE temperatures T_B2 = 0.668, T_B1 = 0.435, T_B3 = 0.178 are all O(1) M_KK. The spectral action S_fold = 250,361 M_KK^4. The correction sum_k T_k dS/dT_k involves derivatives with respect to Lagrange multipliers, not tau.

3. **Corrected epsilon_H.** epsilon_H_corrected = epsilon_H / f^2. Report for f = 0.5, 1.0, 2.0, 10.0.

4. **Shortfall persistence.** The target is epsilon_H = 0.0176. The shortfall = 0.0176 / epsilon_H_corrected. Report whether the shortfall changes qualitatively.

5. **Impact on n_s constraint surface.** The constraint surface is EMPTY if there is no epsilon_H value between 10^{-6} and 3.0 that gives n_s = 0.965. Does the E-vs-F correction create new solutions? Only if f interpolates between these extremes, which requires f ~ 250 (Step 2 shows this is impossible).

6. **Report.** Corrected epsilon_H range, shortfall, verdict on whether the constraint surface remains empty.

**Pre-registered gate FRIEDMANN-BCS-AUDIT-44**:
- PASS: Shortfall narrows by >10x (E-vs-F correction significant)
- FAIL: Shortfall persists within factor 2 (E-vs-F correction irrelevant)
- INFO: correction computed, shortfall changed but surface still empty

**Input files**:
- `tier0-computation/s36_sfull_tau_stabilization.npz`
- `tier0-computation/s42_gradient_stiffness.npz`
- `tier0-computation/s38_cc_instanton.npz`
- `tier0-computation/s42_gge_energy.npz`

**Output files**:
- Script: `tier0-computation/s44_friedmann_bcs_audit.py`
- Data: `tier0-computation/s44_friedmann_bcs_audit.npz`
- Plot: `tier0-computation/s44_friedmann_bcs_audit.png`

**Working paper section**: W4-3

---

### W4-4: Non-Monotone Cutoff from Foam Decoherence (F-FOAM-2)

**Agent**: `quantum-foam-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are testing whether quantum foam decoherence at the Planck scale can create a non-monotone effective cutoff function f_eff, producing a local minimum in the spectral action that stabilizes tau at the fold.

**Context.** S43 DISSOLUTION-43: epsilon_crossover ~ 0.014; spectral triple is EMERGENT (dissolves under foam). 100x hierarchy: left-invariant sensitivity 10^{-4} vs non-left-invariant 0.01. S43 FOAM-GGE-43: GGE occupations are EXACT invariants under diagonal foam; spectral triple dissolves but GGE survives. S43 GQUEST-43: fabric gapped; all interferometric searches null.

S37 monotonicity theorem: the spectral action with any monotone cutoff f gives a monotone S(tau). This PROVED that no minimum exists for monotone f (S37 CUTOFF-SA-37 closure). But if f_eff is non-monotone (dipped at specific scales due to foam), the theorem does not apply.

The proposal: Planck-scale foam introduces decoherence that selectively damps high-lying eigenvalues. If the damping rate depends on |lambda|^alpha, and alpha > 2, high eigenvalues contribute LESS than low ones. The effective cutoff function:

$$f_{\text{eff}}(x) = f(x) \cdot e^{-\gamma x^{\alpha/2}}$$

where gamma parametrizes foam strength. For alpha > 2, f_eff is NON-monotone (rises then falls).

**Computation Steps**:

1. Load eigenvalue data from `tier0-computation/s42_hauser_feshbach.npz` and spectral action from `tier0-computation/s36_sfull_tau_stabilization.npz`.

2. **Foam-modified spectral action.** Compute:

   $$S_{\text{foam}}(\tau) = \sum_k d_k \cdot f\left(\frac{\lambda_k(\tau)^2}{\Lambda^2}\right) \cdot e^{-\gamma |\lambda_k(\tau)|^{\alpha}}$$

   for f(x) = exp(-x) (standard exponential cutoff), gamma in [10^{-6}, 10^{-1}], and alpha in {2, 3, 4}.

3. **Search for minimum.** For each (gamma, alpha), compute S_foam(tau) at tau = 0.00, 0.05, 0.10, 0.15, 0.19, 0.25, 0.30. Does S_foam have a local minimum near the fold (tau ~ 0.19)?

4. **If minimum found:** compute the barrier height, oscillation frequency, and dwell time. Does the dwell time exceed H^{-1}?

5. **Constraint from DISSOLUTION-43.** The foam strength gamma is bounded by epsilon_crossover ~ 0.014 (the point where the spectral triple dissolves). Verify that the gamma range producing a minimum is consistent with epsilon_crossover.

6. **Report.** Whether any (gamma, alpha) combination produces a fold-stabilizing minimum while respecting epsilon_crossover and other constraints.

**Pre-registered gate F-FOAM-2**:
- PASS: Minimum found in S_foam near tau ~ 0.19 for gamma < epsilon_crossover
- FAIL: No minimum for any gamma, alpha in physical range
- INFO: minimum found but gamma > epsilon_crossover (requires foam stronger than dissolution threshold)

**Input files**:
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s36_sfull_tau_stabilization.npz`
- `tier0-computation/s43_dissolution.npz`
- `tier0-computation/s43_foam_gge.npz`

**Output files**:
- Script: `tier0-computation/s44_foam_cutoff.py`
- Data: `tier0-computation/s44_foam_cutoff.npz`
- Plot: `tier0-computation/s44_foam_cutoff.png`

**Working paper section**: W4-4

---
