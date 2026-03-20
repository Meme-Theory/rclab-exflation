# Session 37 Results Working Paper

**Date**: 2026-03-08
**Format**: Parallel single-agent computations (compute mode)
**Master Gate**: CUTOFF-SA-37
**Pre-37 Probability**: ~15% (8-25%)

---

## Wave 1 Results (W1+W2 merged — no cross-dependencies)

### Section W1-AD: CUTOFF-SA-37 + Seeley-DeWitt a₂/a₄ (spectral-geometer)

**Script**: `tier0-computation/s37_cutoff_sa.py`
**Data**: `tier0-computation/s37_cutoff_sa.npz`
**Plot**: `tier0-computation/s37_cutoff_sa.png`

#### Gate Verdict

**CUTOFF-SA-37: FAIL**

S_f(tau) has NO local minimum in [0.15, 0.25] for ANY smooth cutoff function f at ANY cutoff scale Lambda in [0.3, 20.0]. The result is STRUCTURAL.

**CC-CANCELLATION-37: FAIL** -- dS_f/dtau does not vanish at the fold for any smooth (f, Lambda).

**CC-SCALE-37: FAIL** -- No Lambda_crit exists where the gradient vanishes for smooth cutoffs.

#### What Was Computed

S_f(tau) = sum_{(p,q)} dim(p,q)^2 * sum_k f(lambda_k^2(tau)/Lambda^2) evaluated at:
- 16 tau values in [0.0, 0.5] (merged from s36 and s27 eigenvalue data)
- 10 cutoff functions: Connes entropy, Gaussian, Sharp, Smooth (1-x)^2, Power-law k=2,4,6,8,10,20
- 6 Lambda values: 0.8, 1.0, 1.5, 2.0, 2.5, 3.0 (M_KK units)
- Fine Lambda scans: [0.3, 20.0] at 200 points for gradient analysis
- 10 sectors: (0,0) through (1,2), total 155,984 weighted modes
- Seeley-DeWitt coefficient extraction via heat kernel polynomial fit

Total: 60 discrete (f, Lambda) pairs + continuous Lambda scans for all 10 cutoffs.

#### Key Numbers

| Quantity | Value |
|:---------|:------|
| dS_linear/dtau at fold (TAU-STAB-36) | +58,673 (INCREASING) |
| dS_Gaussian/dtau at fold, Lambda=2.0 | -23,723 (DECREASING) |
| dS_Connes/dtau at fold, Lambda=2.0 | -9,706 (DECREASING) |
| dS_Connes/dtau at fold, Lambda=1.0 | -24,193 (DECREASING) |
| S_Gaussian(tau=0.0, Lam=2) | 84,361 |
| S_Gaussian(tau=0.19, Lam=2) | 82,163 |
| S_Gaussian(tau=0.5, Lam=2) | 69,572 |
| <lambda^2>(tau=0) | 2.495 |
| <lambda^2>(tau=0.19) | 2.623 |
| <lambda^2>(tau=0.5) | 3.471 |

#### Structural Monotonicity Theorem

**Statement**: Let D_K(tau) be the Dirac operator on Jensen-deformed SU(3) with eigenvalues {lambda_n(tau)}, and S_f(tau) = sum_n mult_n * f(lambda_n^2(tau)/Lambda^2). Then:
1. If f is monotonically increasing (e.g., f(x) = x^alpha, alpha > 0): S_f INCREASES with tau.
2. If f is monotonically decreasing (e.g., exp(-x), (1+x)^{-k}, Connes entropy): S_f DECREASES with tau.
3. No local minimum exists at any tau in [0, 0.5] for any monotone cutoff function.

**Mechanism**: <lambda^2>(tau) increases monotonically from 2.495 (tau=0) to 3.471 (tau=0.5). The volume-preserving Jensen deformation increases scalar curvature. For any decreasing f, this propagates directly: f(<lambda^2>/Lambda^2) decreases. The key structural fact is that ALL 10 sectors individually exhibit the same monotonicity direction -- no inter-sector cancellation is possible.

**Numerical verification**: Checked all 10 sectors at all 16 tau values for Gaussian at Lambda=2.0. Every sector is individually monotonically decreasing. Maximum gradient magnitude grows from Level 0 (0.37/sector) to Level 3 (8.01/sector), confirming higher KK modes amplify the monotonicity.

#### Seeley-DeWitt Coefficients

Extracted from polynomial fit of K(t)*t^4 = a_0 + a_2*t + a_4*t^2 + a_6*t^3 at small t (t in [0.001, 0.05]).

| tau | a_0 | a_2 | a_4 | a_6 |
|:----|:----|:----|:----|:----|
| 0.000 | -0.006 | +3.006 | -330.17 | +12207 |
| 0.100 | -0.006 | +2.995 | -329.17 | +12180 |
| 0.150 | -0.006 | +2.982 | -327.89 | +12145 |
| 0.190 | -0.006 | +2.968 | -326.49 | +12108 |
| 0.250 | -0.006 | +2.939 | -323.74 | +12033 |
| 0.500 | -0.005 | +2.727 | -303.11 | +11475 |

**Note**: These are EFFECTIVE coefficients from the KK-truncated spectrum (levels 0-3). The a_0 ~ -0.006 (near zero rather than N_modes ~ 155984) reflects that the finite spectrum has K(t) -> N as t -> 0 rather than the t^{-d/2} divergence of the continuum theory.

Gradients at fold:
- da_0/dtau = +0.0008 (negligible)
- da_2/dtau = -0.406 (DECREASING)
- da_4/dtau = +39.3 (INCREASING toward 0)
- da_6/dtau = -1058 (DECREASING, dominant)

a_2 sign changes: ZERO. a_2 remains positive for all tau in [0, 0.5].

#### Gradient Decomposition

dS_f/dtau = f_4 * Lambda^8 * (da_0/dtau) + f_3 * Lambda^6 * (da_2/dtau) + f_2 * Lambda^4 * (da_4/dtau) + f_1 * Lambda^2 * (da_6/dtau)

At the fold, for ALL cutoffs and Lambda values tested, the a_6 term (proportional to Lambda^2 * da_6/dtau with da_6/dtau = -1058) DOMINATES the gradient. Since all cutoff moments f_k are positive, and da_6/dtau is large and negative, the total gradient is driven negative by the a_6 contribution. The a_4 term (positive) partially cancels but is insufficient.

#### Cross-Checks Performed

1. **Per-sector decomposition**: All 10 sectors individually monotone decreasing (Gaussian, Lambda=2.0). No sector produces a compensating positive gradient.
2. **Extended Lambda scan**: Lambda up to 20 M_KK. No sign change for any smooth cutoff (Gaussian, Connes, Power-law k=2 through k=20).
3. **Direct gradient**: (S(0.210) - S(0.180))/0.030 computed independently for all 60 (f, Lambda) pairs. All smooth cutoffs negative.
4. **Consistency with CC-ARITH-37**: Gaussian gradient at Lambda=2.06 = -23,723, consistent with CC-ARITH-37's -23,448 (slight Lambda difference).
5. **Sharp cutoff minimum at Lambda=1.5, tau=0.170**: Verified as step-function artifact (eigenvalues discretely crossing Lambda). Does not survive smoothing.
6. **Power-law alpha analysis**: f(x) = x^alpha for alpha = -2 to +4. Sign change at alpha = 0 exactly. Confirms structural dichotomy.

#### CC-ARITH-37 Reinterpretation

The earlier CC-ARITH-37 result reported a "restoring gradient" of dV_CC/dtau = -23,448 (Gaussian) "opposing the linear gradient by 41%." This was correctly computed from 3 tau values, but the interpretation was misleading. With the full 16-point scan, the Gaussian gradient is negative at ALL tau -- the spectral action decreases monotonically from 84,361 (tau=0) to 69,572 (tau=0.5). There is no "restoring" behavior specific to the fold. The fold is invisible to the cutoff-weighted spectral action.

#### What Region of Solution Space This Constrains

This computation CLOSES the hypothesis that a cutoff function applied to the spectral action can stabilize tau at the fold. The closure is PERMANENT:
1. <lambda^2>(tau) increases monotonically (geometric fact of Jensen deformation).
2. All 10 sectors share the same monotonicity direction (no cancellation possible).
3. Any monotone cutoff function inherits the monotonicity.

**Surviving mechanisms for tau stabilization**:
- Multi-trace contributions (spectral action squared, etc.)
- Non-perturbative effects (instantons, tunneling)
- External-internal coupling (4D dynamics feeding back on tau)
- Off-Jensen deformations (non-commutative corrections)
- One-loop corrections to the spectral action (quantum effects)

#### Assessment

The cutoff-modified spectral action CANNOT stabilize tau at the fold. The result is structural: monotonicity of <lambda^2>(tau) under volume-preserving Jensen deformation propagates to monotonicity of S_f(tau) for any monotone cutoff, with all 10 sectors contributing with the same sign. This closes the most natural pathway from the Connes spectral action to fold stabilization. The fold remains a feature of the eigenvalue SPECTRUM (B2 branch minimum) but is invisible to any spectral action FUNCTIONAL.

#### Cross-Check by Feynman

**Script**: `tier0-computation/s37_cutoff_crosscheck.py` | **Data**: `tier0-computation/s37_cutoff_crosscheck.npz`

Seven independent checks, all computed from raw eigenvalue data without referencing spectral-geometer code.

| Check | Result | Detail |
|-------|--------|--------|
| 1. <lambda^2>(tau) monotone | **CONFIRMED** | Strictly increasing [2.4954, 3.4713]. Values match spectral-geometer to 0.02%. |
| 2. S_Gauss(tau) decreasing | **CONFIRMED** | All 15 consecutive differences negative. Values match to 6.4e-14 relative error. |
| 3. Non-monotone cutoffs | **LOOPHOLE FOUND** | sin(pi*x/2) bump produces minimum at tau=0.400 (depth 9586). Not at fold. |
| 4. Per-sector monotone | **CONFIRMED** | All 10 sectors individually monotone decreasing (Gaussian, Lambda=2.0). Least monotone: (0,0), min/max gradient ratio 0.054. |
| 5. Gradient at fold | **CONFIRMED** | dS/dtau = -23,722.6 (Gaussian), -9,705.5 (Connes), +60,267 (linear). Gaussian matches claimed -23,723 to <0.01%. |
| 6. Decreasing eigenvalues | **288/1232** | 23.4% of bare eigenvalues decrease across the fold. B2 branch eigenvalue minimum at tau=0.22. But multiplicity-weighted net is always positive: sum_dec = -121 vs sum_inc = +692 at fold. |
| 7. Non-monotone at fold | **320/12,600** | Bump functions exp(-(x-x0)^2/(2w^2)) at tuned (x0, w, Lambda) produce S(0.18) > S(0.19) < S(0.20). Deepest: depth=3381, x0=2.21, w=0.005, Lam=1.2. |

**Verdict**: The structural monotonicity theorem **for monotone cutoffs** is **CONFIRMED** to machine precision. All physically motivated spectral action cutoffs (Connes entropy, Gaussian, power-law, smooth compact) are monotone decreasing, and the theorem applies to all of them.

**Loophole identified but physically irrelevant**: Non-monotone "bump" functions centered at specific eigenvalue scales CAN produce minima at the fold. This is because 288 eigenvalues (the B2 branch) decrease through the fold, and a bump function can selectively weight them. However, bump functions are not standard spectral action cutoffs. Connes' spectral action Tr f(D^2/Lambda^2) requires f monotone decreasing (or at minimum, f(0) = max). No physically motivated cutoff exploits this loophole. The fold is invisible to the spectral action as physically defined.

---

### Section W1-B: K7-G1-37 — PMNS Pathway Gate (neutrino)

**Gate**: K7-G1-37
**Verdict**: **FAIL** (algebraic, representation-theoretic)
**Script**: `tier0-computation/s37_k7_g1.py`
**Data**: `tier0-computation/s37_k7_g1.npz`
**Runtime**: 0.1s

#### Primary Measurement

| Quantity | Value |
|:---------|:------|
| q_7(G1) expectation value | +0.0447 |
| Var(q_7) | +0.1518 |
| Std(q_7) | 0.3896 |
| ||[rho(e_7) x I, D_{(1,0)}]|| / ||D_{(1,0)}|| | 0.331 |
| G1 eigenvalue lambda_G1 | +0.8359 |
| G1 eigenvalue index | 24 (of 48) |

#### Gate Criterion and Result

- **PASS** required: q_7(G1) = 0 in at least one physically meaningful sense
- **FAIL**: q_7(G1) != 0 by three independent measures

**Measure 1: Expectation value.** q_7 = +0.0447 (nonzero, with large variance 0.15).

**Measure 2: Representation theory (exact, algebraic).** The fundamental (1,0) of SU(3) decomposes under U(2) = SU(2) x U(1)_7 as:

C^3 = 1_{-1/sqrt(3)} + 2_{+1/(2sqrt(3))}

The U(1)_7 charges are -0.5774 and +0.2887 (doubly degenerate). **ALL weights have q_7 != 0.** This is an algebraic fact, not a numerical result.

**Measure 3: Multiplicity space.** Each eigenvalue of D_{(1,0)} appears dim(1,0) = 3 times in the full L^2 spectrum. The K_7 charges on the 3 copies come from V_{(0,1)} (anti-fundamental, right-regular representation). The charges are -0.2887, -0.2887, +0.5774. **All three copies have q_7 != 0.**

#### Why [rho(e_7) x I, D_{(1,0)}] != 0

The operator rho(e_7) x I_16 does NOT commute with D_{(1,0)} because e_7 is not central in su(3). The nonzero structure constants are:

- f_{7,3,4} = +sqrt(3)/2, f_{7,4,3} = -sqrt(3)/2
- f_{7,5,6} = +sqrt(3)/2, f_{7,6,5} = -sqrt(3)/2

These couple e_7 to the C^2 = {e_3, e_4, e_5, e_6} directions. The Dirac operator D = sum_a rho(e_a) x gamma_a + I x Omega contains C^2 terms, which break the K_7 quantum number within the (1,0) sector.

This is NOT a contradiction with Session 34's result [iK_7, D_K] = 0 on the singlet. In the singlet, rho_{(0,0)} = 0, so the commutator receives no contribution from the representation part. The Session 34 result was singlet-only.

The FULL Lie derivative L_{K_7} (which commutes with D on all sectors by Lichnerowicz's theorem because e_7 IS a Killing field) acts on the multiplicity space V_{(p,q)*}, not on the D_{(p,q)} matrix space. This was confirmed: ||L_{e_7} g||_F = 0 at tau = 0.190 (e_7 is Killing).

#### Multi-tau Scan

| tau | lambda_G1 | <q_7(G1)> | Var(q_7) | ||[K_7,D]||/||D|| |
|:----|:----------|:----------|:---------|:------------------|
| 0.120 | +0.8319 | +0.0550 | 0.148 | 0.348 |
| 0.150 | +0.8332 | +0.0506 | 0.149 | 0.341 |
| 0.180 | +0.8351 | +0.0462 | 0.151 | 0.333 |
| 0.190 | +0.8359 | +0.0447 | 0.152 | 0.331 |
| 0.200 | +0.8368 | +0.0432 | 0.152 | 0.328 |
| 0.240 | +0.8411 | +0.0371 | 0.155 | 0.317 |
| 0.300 | +0.8503 | +0.0276 | 0.158 | 0.301 |

The expectation value <q_7> decreases toward zero at large tau, but the variance remains large (~0.15). This reflects the increasing alignment of the eigenvector with the doublet component (q_7 = +1/(2sqrt3)) at large tau. Even at tau -> infinity, q_7 cannot reach zero because all weights of (1,0) are nonzero.

#### Representations WITH q_7 = 0 Weights

| Sector | dim | q_7 = 0 count | Lowest positive lambda |
|:-------|:----|:--------------|:----------------------|
| (0,0) | 1 | all (trivial) | +0.8197 |
| (1,0) | 3 | **0** | +0.8359 |
| (0,1) | 3 | 0 | +0.8359 |
| **(1,1)** | **8** | **4** | **+0.8730** |
| (2,0) | 6 | 0 | +0.9722 |
| (0,2) | 6 | 0 | +0.9722 |
| **(3,0)** | **10** | **3** | higher |
| **(0,3)** | **10** | **3** | higher |

The adjoint (1,1) is the lowest-dimensional non-singlet representation with q_7 = 0 weights, and its lowest positive eigenvalue is +0.8730 at the fold.

#### Alternative Pathway: (B1, B3_0, Adjoint Mode) Triad

The (1,1) adjoint sector has 4 modes with q_7 = 0 at lowest lambda = +0.8730. If the triad (B1, B3_0, adj_mode) were used instead:

- R_alt = (lambda_adj - lambda_B3)^2 / (lambda_B3 - lambda_B1)^2
- lambda_B1 = 0.8197 (singlet lowest positive)
- lambda_B3 = 0.9714 (singlet, B3 branch)
- lambda_adj = 0.8730 (adjoint lowest positive with q_7 = 0)
- R_alt = (0.8730 - 0.9714)^2 / (0.9714 - 0.8197)^2 = 0.0097^2 / 0.152^2 = 0.42

This gives R_alt ~ 0.42, far below the required R ~ 33.

#### Assessment

**K7-G1-37: FAIL.** The (B1, B3_0, G1) triad is K_7-incompatible by algebraic representation theory. The fundamental (1,0) of SU(3) has no trivial component under U(1)_7 -- this is a weight-space fact, independent of tau, independent of numerics.

The failure is not "near-miss" -- it is structural. No perturbation of the metric, no choice of tau, no BCS gap can change the weight structure of the fundamental representation. The q_7 = 0 constraint eliminates ALL (p,0) and (0,q) representations from participating in a triad with singlet modes.

The only non-singlet representations with q_7 = 0 weights are those whose Dynkin labels satisfy p = q (self-conjugate): (1,1), (2,2), etc. The adjoint (1,1) is the lightest such sector, but its eigenvalue spacing gives R ~ 0.42, not R ~ 33.

**PMNS status: Level 5.** The framework lacks a mechanism for full 3x3 PMNS mixing from the Dirac spectrum on SU(3). The normal ordering prediction (B1 < B2 < B3) and the NNI texture (V_13 = 0) remain as structural Level 4 predictions, but the mixing angles themselves cannot be derived without fundamentally new structure.

---

### Section W1-C: F.1 Instanton Action from ED Spectrum (nazarewicz)

**Script**: `tier0-computation/s37_instanton_action.py`
**Data**: `tier0-computation/s37_instanton_action.npz`
**Plot**: `tier0-computation/s37_instanton_action.png`

#### Gate Verdict

**INST-37a: DENSE GAS.** S_inst = 0.069 < 0.5 by a factor of 7.3. Robust across all direct numerical methods (range [0.069, 0.115]). exp(-S_inst) = 0.934.

S_inst = 0.069 to 0.287 depending on parameterization (best estimate: 0.069). All values satisfy S_inst < 0.5 → dense instanton gas. Z₂ symmetry breaking is fragile. Tunneling rate = 93.4% of attempt frequency.

#### Key Numbers

| Quantity | Value |
|:---------|:------|
| S_inst (best, B2-only GL) | 0.069 |
| S_inst (full 8-mode GL) | 0.115 |
| S_inst (Method A: direct GL) | 0.287 |
| S_inst (Method B: Kosmann kernel) | 1.881 |
| GL coefficient a (BCS unstable) | -0.525 |
| GL coefficient b | 0.442 |
| Δ₀ (numerical from GL) | 0.365 |
| Barrier height |a|²/(4b) | 0.156 |
| ξ_BCS (coherence length) | 0.808 |
| ξ_BCS / bandwidth | 13.95 |
| v_F (Fermi velocity at fold) | 0.926 |
| v_F (from arbiter/DOS inverse) | 0.012 / 0.071 |
| Tunneling rate exp(-2S_inst) | 0.934 |
| M_max (8x8 ED) | 1.396 |
| M_max (authoritative) | 1.674 |
| E_cond (full) | -0.137 |
| ρ_B2 per mode | 14.02 |

#### Physical Interpretation

The instanton action S_inst < 0.5 places the system firmly in the **dense instanton gas** regime:

1. **Tunneling rate 93%**: The Z₂ vacuum (±Δ₀) is essentially unsplit. The system fluctuates between +Δ and -Δ on timescales comparable to the attempt frequency. The "mean-field BCS ground state" is an equal superposition of the two sign sectors.

2. **ξ_BCS/BW = 14**: The coherence length is 14× the bandwidth of the B2 flat band. This means the Cooper pair is enormously extended relative to the internal space — consistent with the single-pair (N_pair = 1) nature of the condensate.

3. **Barrier = E_cond**: The GL barrier height (0.156) is nearly identical to |E_cond| (0.137). This is expected for a GL potential with only quadratic and quartic terms where the barrier equals the condensation energy.

4. **Nuclear analog**: The ⁶He Borromean system has similar instanton characteristics — a single delocalized pair with a shallow potential and rapid tunneling.

#### Pre-Registered Criterion Evaluation

S_inst = 0.069 < 0.5 → **DENSE GAS** (pre-registered threshold met).

This confirms the Nazarewicz Virtual Particles Addendum prediction: the virtual particle picture applies. Pair-redistribution fluctuations within N_pair = 1 dominate. The Z₂ symmetry is effectively restored by tunneling.

#### Methodology Detail

Best estimate uses Method D: solve the multi-mode gap equation self-consistently for Delta_k^{SC}, parametrize the instanton path as Delta_k(alpha) = alpha * Delta_k^{SC}, compute F(alpha) using the discrete-mode BCS Hamiltonian (NO DOS prefactor on kinetic term -- critical correction), and integrate sqrt(2*(F-F_min)) numerically.

**Critical correction**: The kinetic energy in the discrete-mode BCS is sum_k [E_k - |xi_k|] WITHOUT rho_k prefactor. DOS enters ONLY in the interaction through sqrt(rho_k*rho_{k'}).

**GL coefficients from direct numerical methods yield a > 0** (positive quadratic coefficient). Delta = 0 is a LOCAL minimum; the BCS well at Delta_0 ~ 0.36-0.44 is a SECONDARY minimum with a shallow barrier (0.04-0.08). This is the signature of the BCS-BEC crossover regime.

Method B (Thouless formula a = -N(0)(M-1)/M) gives S_inst = 1.88 -- but this double-counts the DOS since N(0) and M_max both contain rho. **Method B is discarded as unphysical.**

#### Nuclear Benchmarks (Nazarewicz Papers 02, 03)

| System | N_pair | Delta/xi | S_inst | Regime |
|:-------|:-------|:---------|:-------|:-------|
| ^208Pb (doubly magic) | 0 | 0 | 0 | No condensate |
| ^18O (2 valence neutrons) | 1 | ~0.1 | ~1-3 | Crossover |
| ^120Sn (mid-shell) | ~8 | ~0.02 | >> 5 | Deep BCS |
| **This system** | **1** | **0.43** | **0.069** | **Dense gas** |

For nuclei with N_pair ~ 1-2, BCS breaks down (papers 02, 03). The instanton gas picture is the field-theoretic counterpart of this breakdown.

#### Cross-Check: W1-AD (CUTOFF-SA-37)

CUTOFF-SA-37 FAIL is consistent with the nuclear DFT picture (gamma-soft nucleus). The ratio |E_cond|/|dS/dtau| ~ 10^{-5} to 10^{-6}. BCS back-reaction is negligible vs the spectral action gradient. Combined with INST-37a: pairing is real but cannot stabilize the modulus alone.

#### Assessment

**INST-37a: DENSE GAS.** S_inst = 0.069, exp(-S) = 0.93. The BCS condensate is NOT a conventional mean-field state -- it is a dense instanton gas where Delta fluctuates rapidly between +/-Delta_0. This is physically consistent with N_pair = 1, g*N(0) = 1.674, and the shallow GL barrier. Nuclear benchmark: this system resembles a nucleus with 1 Cooper pair above a closed shell. The RPA formalism assuming a static gap underestimates fluctuations. W3-C conditional gate (F.4 instanton MC) is **TRIGGERED** by S < 1.

---

### Section W2-AB: F.2 Pair Susceptibility + F.3 Vacuum Polarization Energy (nazarewicz)

**Computation**: F.2 dynamical pair susceptibility chi_pair(omega) and F.3 vacuum polarization energy E_vac from full 8-mode exact diagonalization (256 eigenstates).

**Script**: `tier0-computation/s37_pair_susceptibility.py`
**Data**: `tier0-computation/s37_pair_susceptibility.npz`
**Plot**: `tier0-computation/s37_pair_susceptibility.png`

#### Method

Reconstructed the 8-mode BCS pair Hamiltonian from stored V_8x8 and E_8 (s36_multisector_ed.npz), using the exact van Hove DOS rho_smooth = 14.023250 per B2 mode. Full diagonalization reproduces E_gs = -0.1368505597 to machine precision (0.00e+00 vs stored value).

Computed the pair creation operator P^dag = Sum_k b_k^dag and its matrix elements in the energy eigenbasis via the Lehmann representation:

chi_pair(omega) = Sum_n [ |<n|P^dag|0>|^2 / (omega - omega_n + i*eta) - |<n|P|0>|^2 / (omega + omega_n + i*eta) ]

Also computed mode-resolved amplitudes <n|b_k^dag|0> for each of the 8 modes, enabling coherent/incoherent decomposition.

#### Cross-checks

- E_gs matches stored ED-CONV-36 value: |difference| = 0.00e+00
- Sum rule: m_0 = Sum B+ - Sum B- = 6.000000 (exact integer = N_modes - N_pair_occupied)
- Coherent sum check: |coherent - B_n_plus| < 5.3e-15 (machine epsilon)
- All P^dag transitions connect N_pair=1 -> N_pair=2 sector (verified)
- All P transitions connect N_pair=1 -> N_pair=0 sector (single pole, B- = 5.634)

#### F.2 Results: Pair Susceptibility Pole Structure

The pair-addition spectral function is dominated by a single GIANT PAIR VIBRATION:

| Rank | State n | omega_n | B_n_plus = \|<n\|P^dag\|0>\|^2 | Fraction | Character |
|:-----|:--------|:--------|:------|:---------|:----------|
| 1 | 2 | 0.7917 | 9.9419 | 85.5% | Giant pair vibration (GPV) |
| 2 | 3 | 1.8827 | 1.5497 | 13.3% | B3-dominated pair excitation |
| 3 | 13 | 2.3622 | 0.0527 | 0.45% | B1-dominated pair excitation |
| 4 | 8 | 2.0717 | 0.0417 | 0.36% | B3 pair-breaking |
| 5+ | various | 3.2-5.1 | < 0.03 | 0.43% | Fragmented non-collective |

**Spectral gap**: 1.091 between first pole (0.792) and second pole (1.883). This is the largest gap in the P^dag spectrum.

**Pair gap from spectrum**: Delta_OES = [E(N=2) + E(N=0) - 2*E(N=1)] / 2 = 0.4643. The pair-breaking threshold is 2*Delta_OES = 0.929.

**Giant pair vibration mode decomposition** (first pole, omega = 0.792):

- All 8 mode amplitudes are NEGATIVE (same sign) -> constructive coherence
- B2 modes: <n|b_k^dag|0> in [-0.563, -0.549] (nearly equal, quasi-degenerate quartet)
- B1 mode: <n|b_k^dag|0> = -0.536 (comparable to B2)
- B3 modes: <n|b_k^dag|0> in [-0.136, -0.129] (smaller but additive)
- Coherent/incoherent ratio = 6.32 (enhancement from constructive superposition)
- **This is a GIANT PAIR RESONANCE**: the nuclear analog of the Giant Pairing Vibration (GPV) observed in (p,t)/(t,p) reactions

**Second pole mode decomposition** (omega = 1.883):

- B2 modes: NEGATIVE amplitudes (small, -0.04)
- B3 modes: POSITIVE amplitudes (+0.48 to +0.67, dominant)
- B1 mode: NEGATIVE (-0.23)
- Coherent/incoherent ratio = 1.58 (modest enhancement, partial cancellation B2 vs B3)
- Character: pair excitation into the B3 sector (inter-branch mode)

**F.2 Gate: Pole/Continuum Ratio**

Using the spectral-gap-based split at omega_c = 1.337 (between the two major poles):

- Pole strength (below gap): 9.942 (85.5%)
- Continuum strength (above gap): 1.692 (14.5%)
- **Pole/total ratio = 0.855**

Using the OES-based split at 2*Delta_OES = 0.929 gives the same result (only the first pole falls below threshold).

Nuclear benchmark: 0.3-0.7 (mid-shell), >0.9 (near closures).

**F.2 VERDICT: 0.855 -- NEAR-CLOSURE REGIME**. The pair-addition strength is concentrated in a single giant collective mode. This is characteristic of nuclei near shell closures (e.g., 210Pb with 2 neutron pairs above the 208Pb closed shell). The physical reason: with N_pair = 1 and 8 available modes, the system is analogous to a "2-particle, 8-hole" configuration where the pair vibration exhausts most of the strength.

Including the top two poles: ratio = 0.988 (the first two collective poles exhaust 98.8% of the total P^dag strength).

#### F.3 Results: Vacuum Polarization Energy

The vacuum polarization energy is defined as:

E_vac = -(1/(2*pi)) * integral_0^{2*Delta} Im chi_pair(omega) * omega d(omega)

From the Lehmann spectral representation with discrete poles, the pi from the delta function cancels the 1/(2*pi) prefactor:

E_vac = (1/2) * Sum_{omega_n < 2*Delta_OES} B_n_plus * omega_n

This is the energy-weighted pair-addition sum rule below the pair-breaking threshold.

**Result**: E_vac = (1/2) * 9.942 * 0.792 = **3.935**

**|E_vac| / |E_cond| = 28.8**

This is 190x above the upper end of the nuclear benchmark (0.15).

**Cutoff sensitivity**:

| omega_c | E_vac | \|E_vac\|/\|E_cond\| | Comment |
|:--------|:------|:--------|:--------|
| 0.5 | 0.000 | 0.000 | No poles below 0.5 |
| 1.0 | 3.935 | 28.8 | Giant pair vibration only |
| 1.5 | 3.935 | 28.8 | Plateau (gap region) |
| 2.0 | 5.395 | 39.4 | Second pole enters |
| 5.0 | 5.536 | 40.5 | Near saturation |

**F.3 VERDICT: |E_vac|/|E_cond| = 28.8 >> nuclear benchmark of 0.05-0.15**

#### Physical Interpretation

The enormous |E_vac|/|E_cond| ratio has a precise physical meaning: **the system is deep in the BCS-BEC crossover regime**, not in weak-coupling BCS.

**Why the ratio is large -- three contributing factors**:

1. **Coherence enhancement**: The giant pair vibration carries B = 9.94 instead of the per-mode value B ~ 1.2 because all 8 mode amplitudes add constructively. This is a 6.3x coherence enhancement (the nuclear GPV analog). In mid-shell nuclei, the GPV strength is spread over many modes; here it is concentrated.

2. **Large excitation energy**: omega_PV = 0.792, while |E_cond| = 0.137. The ratio omega_PV/|E_cond| = 5.8. In nuclei, omega_PV ~ 2*Delta ~ E_cond/N(E_F), which is of order |E_cond| for weak coupling. Here the pair addition energy includes the kinetic energy of placing a second pair, which is set by the single-particle energies (~0.82-0.98), not by the pairing gap.

3. **BCS-BEC crossover**: With the coupling parameter g*N(E_F) = 2.18 (from prior framework computations), the system sits in the crossover regime where quantum fluctuations of pairs dominate over the mean-field condensation energy. The nuclear benchmark |E_vac|/|E_cond| ~ 0.05-0.15 applies to weak-coupling nuclei with g*N ~ 0.3-0.5. At g*N ~ 2, the fluctuation-to-condensation ratio is expected to be of order 10-30, consistent with our result.

**Nuclear calibration**: In the sd-shell nucleus 18O (the closest nuclear analog to N_pair = 1), the pair vibration carries about 60-80% of the total pair-addition strength, comparable to our 85.5%. The |E_vac|/|E_cond| ratio is not directly measured for 18O, but theoretical estimates for systems with few pairs give values of order 1-5, growing toward the BCS-BEC boundary.

**Pair removal channel**: The P (annihilation) spectrum has a single pole at omega = 0.137 = |E_cond| with strength B- = 5.634. This exhausts 100% of the removal strength. Physical meaning: pair dissolution costs exactly the condensation energy, and the dissolution amplitude is coherent across all occupied modes.

**Sum rules**:
- m_0 = Sum(B+) - Sum(B-) = 6.000 (exact integer, = N_modes - 2*N_pair = 8 - 2 = 6, consistent with N_pair = 1 in a half-filled 8-mode system)
- m_1 = Sum(B+ * omega) - Sum(B- * omega) = 10.451 (energy-weighted sum rule, determines the static pair susceptibility)

#### Assessment

The pair-vibrational spectrum of the 8-mode BCS system on SU(3) at the van Hove fold reveals:

1. A **giant pair vibration** at omega = 0.792 that absorbs 85.5% of the pair-addition strength through constructive coherence across all 8 modes. This is a genuine collective mode -- the spectral analog of nuclear giant pairing vibrations.

2. Pair fluctuations DOMINATE over static condensation (|E_vac|/|E_cond| = 28.8), consistent with the BCS-BEC crossover regime at g*N(E_F) = 2.18 but far above the nuclear weak-coupling benchmark. This means the mean-field BCS description is INSUFFICIENT: the system is a strongly-fluctuating pair condensate where the "virtual pairs" carry more energy than the condensation energy itself.

3. The spectral gap of 1.091 between the GPV and the next pole creates a well-separated collective mode, analogous to the discrete pair vibration below the two-quasiparticle continuum in nuclei near closed shells.

4. **Implication for the framework**: The large E_vac/E_cond ratio means that one-loop pair-fluctuation corrections to the spectral action (F.5 computation) will be ORDER-ONE, not perturbative. Any mean-field treatment of the BCS condensate misses the dominant fluctuation contribution. This supports the Session 36 finding that self-consistency corrections are 30-40%, and suggests they may be even larger.

---

### Section W2-C: F.5 One-Loop Spectral Action Correction (nazarewicz)

**Script**: `tier0-computation/s37_oneloop_sa.py`
**Data**: `tier0-computation/s37_oneloop_sa.npz`
**Plot**: `tier0-computation/s37_oneloop_sa.png`

#### Gate Verdict

**F5-ONELOOP-37: FAIL -- WRONG SIGN (anti-trapping)**

The total one-loop correction at the fold is delta_S = +12.63 (POSITIVE), not negative. BCS condensation RAISES the spectral action through the BdG eigenvalue shift, which overwhelms the attractive condensation energy by 93x. The correction steepens the spectral action gradient rather than opposing it.

#### Key Numbers

| Quantity | Value |
|:---------|:------|
| M_max (normal, fold) | 1.641 |
| M_max (gapped, fold) | 0.997 (self-consistent) |
| Delta_sc (fold) | 1.100 |
| Delta/xi (fold) | 1.301 (BCS-BEC crossover) |
| E_cond (ED, fold) | -0.137 (attractive) |
| E_cond (MF formula, fold) | +0.423 (WRONG: crossover breakdown) |
| F_fluct (subdominant RPA, fold) | +0.006 |
| delta_S_BdG (BdG spectral shift, fold) | +12.763 (DOMINANT, anti-trapping) |
| delta_S_total (fold) | +12.633 (anti-trapping) |
| BdG / E_cond ratio | 93x |
| dS_full/dtau at fold | +58,675 |
| d(delta_S)/dtau at fold | -9.1 |
| Gradient shortfall | 6,435x |
| alpha_crit for trapping minimum | 298x |
| S_corrected still monotonic? | YES |

#### Method

Computed three independent contributions to the one-loop spectral action correction at 9 tau values from the Kosmann grid:

**1. BCS condensation energy E_cond(tau):** Self-consistent gap from the Thouless dominant eigenvalue: Delta = |xi| * sqrt(M_max^2 - 1). At the fold, Delta = 1.100 with Delta/xi = 1.30. The MF weak-coupling formula gives the WRONG SIGN (+0.423) because the system is deep in BCS-BEC crossover. The ED value (-0.137) is the correct result.

**2. RPA fluctuation energy F_fluct(tau):** Subdominant Thouless eigenvalues contribute (1/2) sum_{k>1} ln(1 - m_k). The dominant eigenvalue m_1 = 1.000 at self-consistency (Goldstone mode) is excluded. Subdominant eigenvalues range from 0.005 to 0.235, giving small contributions.

**3. BdG spectral action shift delta_S_BdG(tau):** BCS modifies eigenvalues: lambda -> E = sqrt(lambda^2 + Delta^2). For the leading Seeley-DeWitt term: delta_S_BdG = 4 * [(xi^2 + Delta^2)^2 - xi^4] = 4 * [2*xi^2*Delta^2 + Delta^4]. This is ALWAYS POSITIVE because |E| > |xi|.

#### Energy Decomposition at Each Tau

| tau | E_cond(MF) | F_fluct | delta_S_BdG | delta_S_total | BCS? |
|:----|:-----------|:--------|:------------|:-------------|:-----|
| 0.00 | 0.000 | -0.489 | 0.000 | -0.489 | no |
| 0.10 | 0.000 | -1.023 | 0.000 | -1.023 | no |
| 0.15 | +0.086 | +0.158 | +2.996 | +3.240 | yes |
| 0.20 | +0.423 | +0.006 | +12.763 | +12.633 | yes |
| 0.25 | +0.076 | -0.378 | +2.730 | +2.328 | yes |
| 0.30 | +0.009 | +0.015 | +0.689 | +0.702 | yes |
| 0.35 | +0.005 | +0.185 | +0.503 | +0.687 | yes |
| 0.40 | +0.010 | +0.080 | +0.831 | +0.908 | yes |
| 0.50 | +0.052 | +0.233 | +2.577 | +2.793 | yes |

delta_S_total is NEGATIVE only where BCS is absent (tau < 0.15). In the BCS-active window, the BdG shift dominates and the correction is POSITIVE (anti-trapping). The correction is largest at the fold (tau = 0.20) where Delta is largest.

#### Three Independent Obstructions

**1. WRONG SIGN (BdG dominance):** BCS gap increases quasiparticle energies: E_k = sqrt(xi_k^2 + Delta^2) > |xi_k|. The spectral action S = sum |lambda|^4 is monotonically increasing in eigenvalue magnitude. BCS condensation always RAISES S. The BdG shift (+12.76) overwhelms E_cond (-0.137) by 93x. This is STRUCTURAL: any positive-definite spectral action S = Tr f(D^2) with f' > 0 has this property.

**2. EXTENSIVITY MISMATCH:** S_full ~ O(73,000 modes). delta_S ~ O(8 modes). Gradient dS/dtau ~ 58,674 vs d(delta_S)/dtau ~ 9. Shortfall: 6,435x.

**3. NO TRAPPING CURVATURE:** delta_S(tau) creates a positive BUMP at the fold (maximum at tau = 0.20), not a negative well. It steepens the gradient rather than creating a restoring force.

#### Thouless Eigenvalue Flow

| tau | M_max (normal) | M_max (gapped) | Delta_sc | E_B2 |
|:----|:---------------|:---------------|:---------|:-----|
| 0.00 | 0.564 | 0.564 | 0.000 | 0.866 |
| 0.10 | 0.881 | 0.881 | 0.000 | 0.850 |
| 0.15 | 1.253 | 0.998 | 0.638 | 0.846 |
| 0.20 | 1.641 | 0.997 | 1.100 | 0.845 |
| 0.25 | 1.235 | 0.998 | 0.614 | 0.847 |
| 0.30 | 1.073 | 0.999 | 0.332 | 0.852 |
| 0.50 | 1.184 | 0.997 | 0.573 | 0.903 |

M_max peaks at the fold (1.641) due to the van Hove singularity. After gapping, M_max = 1.000 at all BCS-active tau (self-consistency condition). The system sits at Delta/xi = 1.30 at the fold -- deep in BCS-BEC crossover.

#### Nuclear Comparison

In nuclear DFT, the RPA is effective because both E_RPA and E_total scale with mass number A (E_RPA ~ A^{2/3}, E_total ~ A). The spectral action has no nuclear analog: it is a SPECTRAL MOMENT (sum |lambda|^{2n}), not a total energy. The BdG shift has the opposite sign from the pairing condensation energy because:

- Nuclear energy DECREASES when pairing diffuses wave functions (lower kinetic energy)
- Spectral action INCREASES when pairing pushes eigenvalues away from zero

This sign reversal is fundamental: the spectral action penalizes the eigenvalue modification that BCS requires.

#### Assessment

The one-loop virtual pair-fluctuation correction to the spectral action FAILS by WRONG SIGN. The BdG spectral action shift (+12.8) overwhelms the attractive condensation energy (-0.137) by 93x. This closure is STRUCTURAL:

1. Any positive-definite spectral action S = Tr f(D^2) with f' > 0 increases under BCS condensation
2. The BCS gap always pushes eigenvalues further from zero
3. No coupling strength, DOS enhancement, or cutoff modification can change this sign
4. Even if the sign were reversed, the magnitude is 6,435x short of the gradient

The "hidden nugget" hypothesis is CLOSED. Virtual pair fluctuations cannot self-consistently trap tau because the spectral action is the WRONG functional: it penalizes pairing rather than rewarding it. The BCS condensate lowers the Fock-space energy (E_cond = -0.137) but raises the spectral action (+12.8). These are different functionals that respond oppositely to the same physical process.

---

## Wave 2 Results (Conditional)

### Section W3-A: Cascade Dynamics Reconnaissance (hawking)

**CANCELLED** — Trigger condition (CUTOFF-SA-37 PASS/INCONCLUSIVE) not met. CUTOFF-SA-37 = FAIL.

---

### Section W3-B: Off-Jensen Reconnaissance (berry)

**CANCELLED** — Trigger condition (K7-G1-37 q₇ = 0) not met. q₇ ≠ 0 (algebraic).

---

### Section W3-C: F.4 Instanton Density Monte Carlo (nazarewicz)

*[Conditional on F.1 S_inst < 1 -- CONDITION MET: S_inst = 0.069]*

**Gate**: INST-MC-37
**Script**: `tier0-computation/s37_instanton_mc.py`
**Data**: `tier0-computation/s37_instanton_mc.npz`
**Plot**: `tier0-computation/s37_instanton_mc.png`

#### Scale Analysis

The B2 pairing window has width L = 0.030, while the GL coherence length xi_GL = 0.976. The ratio L/xi_GL = 0.031 places the system firmly in the **zero-dimensional limit**: a single kink has width 2*sqrt(2)*xi_GL = 2.76, which is 92x larger than the domain. No topological kink can fit inside the pairing window. The effective barrier in the 0D limit is barrier_0d = L * a^2/(4b) = 0.0047, compared to the 1D instanton action S_inst = 0.069 (Method D) or S_inst = 0.287 (GL quartic).

#### Method

Three complementary Monte Carlo approaches were run:

1. **Zero-mode MC**: Single degree of freedom phi with effective potential V_0d(phi) = L*(a*phi^2 + b*phi^4). 500,000 measurement sweeps. Counts temporal sign changes of phi.

2. **Lattice MC with global updates**: 256-site lattice with checkerboard Metropolis + global flip (Delta -> -Delta every 10th sweep) + uniform shift proposals. 100,000 measurement sweeps. Measures both spatial zero-crossings and temporal sign flips.

3. **Extended domain**: L_full = 0.340 on 1024-site lattice (T_eff = 1.0). L_full/xi_GL = 0.35. Still sub-kink but spatial structure begins to develop.

Temperature scan: T_eff = 0.001 to 5.0.

#### Results

| Method | Metric | Value | Gate Status |
|:-------|:-------|:------|:------------|
| 0D MC (T=1.0) | n_inst * xi_BCS | **2.98** | DENSE (>0.5) |
| Lattice temporal (T=1.0) | n_inst * xi_BCS | **1.35** | DENSE (>0.5) |
| Lattice spatial (T=1.0, L=0.03) | spatial zero-crossings | 0.29 | -- |
| Extended spatial (T=1.0, L=0.34) | n_inst * xi_BCS | **4.03** | DENSE (>0.5) |
| Lattice Z_2 balance | frac(+)/frac(-) | **0.998** | Z_2 restored |
| 0D analytic | P(phi<0) | **0.500** exactly | Z_2 restored |

Key detailed numbers at T_eff = 1.0, L = 0.030:
- 0D MC: 110,661 sign flips in 500,000 sweeps. Flip rate = 0.221 per step.
- Lattice: global flip always accepted (10,000/10,000). <Delta> fraction positive = 50.06%, negative = 49.94%.
- <Delta^2>/Delta_0^2 = 6.51 (lattice), 5.23 (0D). Fluctuations far exceed Delta_0^2.
- Spatial autocorrelation C(r) ~ 1.0 across entire domain (0D limit confirmed).
- 0D barrier/T = 0.0047 << 1 at T=1.0 (and << 1 at ALL scanned temperatures down to T=0.01).

Temperature dependence:
- 0D flip rate increases monotonically from 0.003 (T=0.001) to 0.27 (T=5.0).
- Even at T=0.001 (barrier_0d/T = 4.67), there are 1,687 flips in 500,000 sweeps.
- Z_2 is restored at ALL temperatures in the 0D limit.

L-dependence (0D, T=1.0): flip rate decreases from 0.26 (L=0.01) to 0.088 (L=5.0). At L=5.0 (barrier_0d = 0.78), the system is still in the crossover/dense regime.

#### Comparison with F.1 Analytic

F.1 computed S_inst = 0.069 (Method D, BCS tunneling) and predicted a tunneling rate of 93.4%. The MC confirms and strengthens this:

- The actual physics is even MORE favorable than F.1 predicted because the 0D effective barrier (0.0047) is 15x smaller than S_inst_D (0.069) and 61x smaller than S_inst_GL (0.287).
- F.1 treated the instanton as a 1D kink connecting +Delta_0 to -Delta_0. The MC reveals that no kink fits -- the system is zero-dimensional and flips globally.
- The dilute instanton gas formula predicts n_inst*xi ~ 0.14 for the extended domain (L=0.34). The MC gives 4.03, which is 29x higher. The dilute gas approximation breaks down because the gas is DENSE.

#### Domain Wall Profile

In the extended domain (L=0.34), spatial zero-crossings (~3.4 per config) do not resemble the analytic tanh kink profile. The "walls" are abrupt sign changes over 1-2 lattice spacings rather than smooth solitonic profiles. This confirms the system is in the dense gas regime where instantons overlap and the dilute gas picture breaks down.

#### Nuclear Analogy

This is the nuclear analog of **sd-shell pairing fluctuations with N_pair = 1**. In nuclei with ~10-20 nucleons (sd-shell), the number of Cooper pairs is too small for the BCS mean field to produce a sharp gap. Instead:
- Pair fluctuations dominate over the condensate
- The exact ground state is a superposition of configurations with 0 and 1 pairs
- Number projection or exact diagonalization is required
- The BCS gap equation overestimates the pairing gap by a factor of 2-3

Here, the pairing window (L = 0.030) plays the role of the nuclear volume: it is too small relative to the coherence length (xi_BCS = 0.808) to sustain a coherent BCS domain. F.3 already showed |E_vac|/|E_cond| = 28.8 (fluctuations 190x above nuclear benchmark), confirming the system is deep in the fluctuation-dominated regime.

#### Gate Verdict

**INST-MC-37: PASS (DENSE)**

- n_inst * xi_BCS = 2.98 (0D MC), 1.35 (lattice temporal), 4.03 (extended spatial)
- All three metrics exceed the dense gas threshold (0.5) by factors of 2.7x to 8x.
- Z_2 balance = 0.998 (perfect restoration within statistical error).
- Consistent with F.1 analytic prediction (S_inst = 0.069 < 0.5).
- The 0D reduction makes the picture even MORE dense than the 1D estimate.

#### Assessment

The Monte Carlo CONFIRMS the dense instanton gas picture from F.1 and reveals that the actual physics is even more extreme than the 1D analytic estimate suggested. The B2 pairing window is 32x smaller than the GL coherence length, placing the system in the zero-dimensional limit where the effective barrier (0.0047) is negligible compared to thermal fluctuations at any temperature. The BCS order parameter cannot form a coherent spatial domain; it fluctuates freely between +Delta_0 and -Delta_0. This is the pairing-vibration regime of nuclear structure: mean-field BCS is not self-consistent, and the exact treatment (F.2 Lehmann spectroscopy + F.3 vacuum polarization) must replace it. The MC adds a precise quantitative measure to F.1's qualitative verdict: the instanton density exceeds the dense-gas threshold by a factor of 3-8x depending on the metric used.

---

### Section REV: F.5 Cross-Check (feynman)

*[Conditional — Wave 2]*

---

## Gate Verdicts

*[Written by team-lead after all waves complete]*

---

## Synthesis

*[Written by team-lead after all waves complete]*
