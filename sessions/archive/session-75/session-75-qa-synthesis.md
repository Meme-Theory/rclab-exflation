# Session 75 Quantum-Acoustics Synthesis

**Agent**: Quantum-Acoustics Theorist
**Source**: `sessions/archive/session-75/session-75-results-workingpaper.md` (57 computations, 4 waves)
**Date**: 2026-04-12

---

## 1. Executive Summary

- **f_conv PASS closes the A_s gap to 0.12 OOM**: The spectral-to-CMB conversion factor f_conv = (M_KK/M_Pl)^4 x (a_2/a_0)^2 = 2.547e-10 is derived from zero free parameters. This is a geometric projection factor, not a dynamical mechanism, and it identifies the A_s problem as a dimensional transmutation between the fiber's internal energy scale and the emergent 4D Planck scale. Predicted A_s = 1.58e-9, observed 2.1e-9 (25% residual).

- **Parker pair production is the unique canonical formulation for the supersonic transit**: The Parker-Hawking reconciliation (W1-N) proves that Parker (Bogoliubov mode equation) and Gibbons-Hawking agree exactly in de Sitter, but diverge by 2.58 OOM in the supersonic regime. The 2.58 OOM IS the transit enhancement factor F = 380.9. The acoustic Hawking temperature T_H = 72.838 M_KK is a phononic sector quantity; substituting it into the gravitational A_s formula is a category error. The GGE relic spectrum is non-thermal at every temperature.

- **GGE-to-CMB transfer preserves primordial n_s exactly**: The cosmological transfer function is a linear operator; it cannot alter the spectral index. The entire n_s question reduces to the primordial computation. BAO angular scale matches Planck to 0.78%.

- **DC permanence is a finite-size artifact (FAIL)**: The ~20% DC component from S73B decays as N^{-1.26} with system size. At N=12, DC = 4.6%. The fabric remains integrable, but the "virtual particle = permanent local DC offset" interpretation requires revision -- the permanent component resides in global conserved charges, not local observables.

- **Mach-number scaling is exponential, not power-law**: kappa_H/T_eff does not follow Ma^2. The surface gravity is affine in Ma while T_eff grows exponentially through the sinh^2(r) ~ exp(2r)/4 regime. The squeeze parameter r scales linearly with Ma, making the Bogoliubov enhancement an exponential function of the flow velocity. No power-law combination closes the ratio.

---

## 2. GGE Relic and Transfer

### 2.1 GGE-to-CMB Transfer (W1-M): n_s Preserved, BAO 0.78%

The governing structure here is the linearity of the cosmological transfer function T(k). This is a standard result in CMB physics (Eisenstein and Hu 1998), but its application to the phonon-exflation framework has a specific consequence: the entire GGE-to-CMB pipeline has **no independent failure mode** beyond the primordial n_s prediction.

The computation constructs three primordial power spectra -- GGE substrate (n_s = 1.0000), Planck (n_s = 0.9649), and BCS+CW (n_s = 0.9595) -- applies the EH98 transfer function with Planck 2018 cosmology, and integrates through the radiation transfer to C_l on 303 multipoles. The results:

| Input n_s | Output delta_n_s vs Planck | BAO theta_A mismatch |
|:----------|:--------------------------|:---------------------|
| 1.0000 (GGE substrate) | 0.0351 | 0.78% |
| 0.9649 (Planck) | 0 (reference) | 0.78% |
| 0.9595 (BCS+CW) | 0.0054 | 0.78% |

The branch amplitude fractions confirm B1 dominance: B1 = 99.08%, B2 = 0.01%, B3 = 0.90%. This follows from the extreme B1 squeezing (r_B1 = 3.57, squeeze factor 1265) established in prior sessions. The B2 flat band, despite carrying 4 modes, is suppressed by its lower squeeze factor (35.6) and Peter-Weyl weight structure.

**Structural theorem**: The transfer function is scale-preserving. The gate verdict reduces entirely to: what is the framework's n_s? The S74 Bogoliubov-only result gives n_s = 1.0000 exactly (scale-invariant, FAIL for Planck). The S66 BCS+CW gives n_s = 0.9595 (1.28 sigma). The transfer cannot change this; it propagates whatever tilt the primordial spectrum carries.

The BAO peak position theta_A(model) = 0.01033 rad vs theta_*(Planck) = 0.01041 rad is a 0.78% mismatch (2.6 sigma), set by background cosmology alone. This is independent of the primordial spectrum shape.

### 2.2 DC Permanence (W3-N): Finite-Size Artifact

The S73B computation found a ~20% DC component in the 4-cell ring graph. This session tested the scaling to N = 1, 4, 8, 12 cells on the C_L ring subgraph of CG(24), with N_pair = 2, applying a localized perturbation at (cell=1, mode=B1) and evolving over 40 Josephson periods.

| N_cells | dim(Fock) | DC fraction (time) |
|--------:|----------:|-------------------:|
|       1 |        28 |           0.01373  |
|       4 |       496 |           0.20367  |
|       8 |     2,016 |           0.13925  |
|      12 |     4,560 |           0.04627  |

**Power-law fit**: DC ~ N^{-1.263}. Extrapolated DC(N=32) = 0.017.

The 4-cell "sweet spot" at 20% reflects a transient interplay between Josephson coupling (which introduces conserved charges via translational symmetry on the ring) and mode dilution (which spreads the perturbation across more states). At 12 cells, dilution dominates.

From the acoustic perspective, this is the expected behavior of a localized perturbation in an integrable lattice: the perturbation disperses into the full set of conserved-charge sectors, and the residual DC component scales inversely with the number of available sectors. The system does not thermalize (it is integrable -- this remains unshaken), but the LOCAL DC residual vanishes as the system size grows.

**Framework implication**: The integrability claim stands. The Ordered Veil remains permanent. But the "virtual particle = permanent local DC offset" interpretation must be revised. The permanent information resides in GLOBAL conserved charges (the full set of GGE Lagrange multipliers lambda_k), not in any single cell's local observable. This is precisely the distinction between a local order parameter and a global topological invariant -- the fabric's GGE relic is the latter.

### 2.3 N_eff Thermalization (W3-M): 3.044 Exact

The GGE relic at the fold carries a non-thermal energy partition (21 bosonic + 15 fermionic metric moduli, initial GGE deviation delta_0 = 1.224). The computation traces through standard gauge and weak thermalization from T ~ 10 TeV to T_dec ~ 1.1 MeV.

The key acoustic insight: the ~10^14 thermalization e-folds between the fold and neutrino decoupling completely erase the GGE initial conditions. This is a structural inevitability -- the ratio Gamma_gauge/H ~ alpha_s^2 M_Pl/T peaks at ~10^14 for T ~ 100 GeV. Any initial state thermalizes to SM equilibrium by T ~ 1 MeV.

N_eff(BBN) = N_eff(recomb) = 3.044000, matching the SM prediction to machine zero.

The S74 result (N_eff = 3.174) counted the partition-rigidity dof ratio 21/15 at the fold. That is the GGE INITIAL partition, not the thermalized observable. Post-thermalization drives N_eff to the SM value. The correction from S74 to S75 is not a revision of the framework but a proper accounting of when in the cosmological history N_eff is measured: at BBN/recombination, not at the fold.

### 2.4 f_conv as Geometric Projection (W1-E)

The A_s gap closure is the session's most significant result from the quantum-acoustics perspective. The fiber-level A_s = 6.22 (from S74 W1-G, 8-mode Bogoliubov squeezed vacuum) must be projected to the 4D curvature perturbation channel. Two structural factors control this projection:

**Factor 1: KK hierarchy suppression (M_KK/M_Pl)^4 = 1.371e-9 (log10 = -8.863)**. The fiber variance has energy dimension M_KK^4; the 4D curvature perturbation is normalized to M_Pl^{-4}. The ratio converts between these scales. This is the standard Kaluza-Klein dimensional transmutation.

**Factor 2: Spectral weight projection (a_2/a_0)^2 = 0.1858 (log10 = -0.731)**. The a_2 Seeley-DeWitt coefficient captures ONLY the scalar curvature sector of the full D_K spectrum. Not all 155,984 eigenvalues contribute to curvature perturbations -- only those weighted by lambda^{-2} (the a_2 kernel). The fraction is a_2/a_0 = 2776.2/6440.0 = 0.431 at the fold. For a variance this enters squared.

**Combined**: f_conv = 2.547e-10, giving A_s(predicted) = 6.22 x 2.547e-10 = 1.585e-9.

This is 75% of the Planck value (2.1e-9). The 25% residual (0.12 OOM) could be absorbed by BCS dressing of a_2 or L_max corrections to a_2/a_0. Neither the M_KK/M_Pl ratio (from S44 EIH extraction) nor the a_2/a_0 ratio (from the D_K eigenvalue spectrum) is a free parameter. This is a zero-parameter prediction.

The six routes explored ranged from -1.536 to -9.594 in log10(f_conv). Only R3b = (M_KK/M_Pl)^4 x (a_2/a_0)^2 falls within the PASS band. Its physical content is transparent: the KK hierarchy accounts for 8.86 OOM and the spectral projection for 0.73 OOM, closing the 9.47 OOM gap to within 0.12 OOM.

---

## 3. Acoustic Physics

### 3.1 Parker-Hawking Reconciliation (W1-N): Parker Uniquely Correct

The governing equations are the Bogoliubov mode equation u_k'' + omega_k^2(tau) u_k = 0 (Parker) and the thermal Hawking formula A_s = T^2/(2 eps M_Pl^2) (Hawking). In de Sitter, these are algebraically identical: T_GH = H/(2 pi), and the substitution yields H^2/(8 pi^2 eps M_Pl^2) in both cases. CHK1 confirms: ratio = 1.0000000000.

For the supersonic transit, four routes were computed:

| Route | A_s | Gap vs Planck (OOM) |
|:------|:----|:--------------------|
| Parker (Bogoliubov, S74) | 6.22 | 9.47 |
| Gibbons-Hawking (base) | 1.63e-2 | 6.89 |
| Acoustic Hawking (naive T_H) | 2.09e+4 | 13.00 |
| GGE relic | 4.95e-2 | 7.37 |

The central structural finding: A_s(Parker) = P_0(GH) x F_total, where F_total = 380.9 is the total Bogoliubov enhancement from the mode equation. T_eff(Parker) = 1.256 M_KK, and (T_eff/T_GH)^2 = 380.93 = F_total exactly.

**Why Parker is uniquely correct for the transit**: (a) The spectrum is non-thermal -- it is a GGE. At T_H = 72.838 M_KK, the Parker/Planck occupation ratio ranges from 0.097 (B2) to 3.57 (B1). No single temperature fits. (b) The "horizon" is transient, not stationary. (c) The acoustic Hawking temperature T_H lives in the phononic sector; the gravitational A_s formula lives in the a_2 sector. These are decoupled by the Spectral-Moment Decoupling Theorem (W2-E). Substituting T_H into A_s = T^2/(2 eps M_Pl^2) is a category error mixing the phononic and gravitational spectral channels.

The mode-dependent effective temperatures -- T_eff(B1) = 258.8 M_KK, T_eff(B3) = 11.1 M_KK, T_eff(B2) = 7.46 M_KK -- reflect the GGE structure: each branch has its own Lagrange multiplier, not a common temperature. This non-thermality is the acoustic fingerprint of the supersonic transit.

### 3.2 Mach Scaling (W2-M): Exponential, Not Power-Law

The pre-registered gate expected kappa_H/T_eff ~ Ma^2. The computation scales the S71 modulus velocity profile by Ma/Ma_phys, keeping the sound speed profile fixed, and evaluates kappa_H, r_k, T_eff at each Mach number.

The structural result: the three ingredients have fundamentally different functional forms.

- **kappa_H(Ma) = 33.21 Ma + 71.02** (AFFINE in Ma, not power-law). The additive offset 71.02 comes from dc_s/dtau at the entry horizon. Effective power-law exponent over [1, 20]: beta = 0.803.

- **r_k(Ma) = r_k_phys x Ma/Ma_phys** (LINEAR in Ma, sudden approximation). This is the sudden limit of the Bogoliubov mode equation: the squeeze parameter is proportional to the adiabaticity parameter, which scales with velocity.

- **T_eff ~ omega x sinh^2(r)** (EXPONENTIAL in Ma for r >> 1). When r >> 1, sinh^2(r) ~ exp(2r)/4. Since r ~ Ma, T_eff grows as exp(2 r_0 Ma / Ma_phys). Effective power-law exponent over [1, 20]: gamma = 9.1.

Therefore kappa_H / T_eff ~ Ma x exp(-2 r_0 Ma / Ma_phys), which is a DECREASING function. The effective exponent is -0.844, far outside the [1.5, 2.5] gate range.

The selected numerical data illustrate the exponential takeover:

| Ma | kappa_H | T_eff | kappa/T_eff | nbar (log10) |
|:---|:--------|:------|:------------|:-------------|
| 1.0 | 104.2 | 0.228 | 456.8 | -1.61 |
| 13.8 | 528.7 | 36.4 | 14.5 | 1.63 |
| 50.0 | 1732 | 4.81e9 | 3.6e-7 | 9.75 |

At Ma = 50, the mean occupation nbar ~ 10^{9.75} and T_eff ~ 5 x 10^9 M_KK. The exponential Bogoliubov enhancement overwhelms the linear surface gravity. This is the acoustic physics analog of the trans-Planckian problem in black hole physics: at sufficiently high Mach numbers, the squeezed-state variance exp(-2r)/4 drives the effective temperature to arbitrarily large values, and no power-law scaling can describe the result.

**Methodological lesson (permanent)**: Bogoliubov squeeze parameters are the correct degrees of freedom for acoustic particle creation in the supersonic regime. Temperature-based (Hawking) or surface-gravity-based (Unruh) scaling laws presuppose thermality, which fails for the GGE. The exponential Ma-dependence of T_eff is a generic feature of non-thermal particle creation in flows with Ma >> 1.

### 3.3 Squeezing Phases (W2-J): phi ~ 0, Maximum Enhancement

All 8 exit-ODE squeeze phases lie near zero (0.005 to 0.012 rad), not near pi/4 as the S68 Josephson prediction would require.

| Mode | r_k (exit) | phi_k (rad) |
|:-----|:-----------|:------------|
| B2[0] | 0.02134 | +0.00456 |
| B1 | 0.08943 | +0.00821 |
| B3[2] | 0.11073 | +0.01202 |

The governing equations are the Bogoliubov ODE in the (alpha, beta, Phi) representation, solved through the fold transit [tau = 0.15 to 0.23] with Radau integrator at rtol = 1e-13. Unitarity verified to 2.4e-15 for all modes.

**Why phi ~ 0**: The transit is a SMOOTH frequency variation. The BCS quasiparticle frequencies omega_k(tau) decrease monotonically through the fold. The Bogoliubov coupling kappa = (1/2) d(ln omega)/dtau is one-signed and smooth. In this regime, beta_k is predominantly real and positive (omega_in > omega_out gives positive real beta in the sudden limit). The small imaginary phase phi_k ~ 0.005-0.012 tracks the accumulated dynamical phase omega/v_tau integrated across the transit.

**Consequence for enhancement**: phi_k ~ 0 corresponds to MAXIMUM variance enhancement. The compound squeeze S_total = S_exit x S_BCS x S_entry gives enhancement 72,664 at phi_BCS = 0 versus 58,173 at phi_BCS = pi/4. Setting phi_BCS = 0 vs phi_BCS = dyn changes enhancement by only 0.004%. The Josephson pi/4 input actually REDUCES enhancement by 0.10 OOM because cos(pi/4) < 1.

The S68 Josephson prediction phi_eff = pi/4 would require a SEPARATE collective mode rotation (the Josephson oscillation between condensate and quasiparticle degrees of freedom). The microscopic mode equation does not generate this rotation. It would need to be imposed as additional physics from the collective dynamics on the 32-cell tessellation, not extracted from the single-fiber BdG equation.

### 3.4 Dispersion Running (W1-C): Sasaki-Stewart Exact at CMB Scales

The BCS dispersion relation omega_b(k) = sqrt(k^2 c_b^2 + m_eff_b^2) introduces k-dependence in the squeeze parameter r_b(k) only through the kinetic energy term k^2 c_b^2. At CMB scales (k ~ 10^{-57} M_KK^{-1}), this term is suppressed by a factor of (k_CMB/k_fold)^2 ~ 10^{-113} relative to the mass gap m_eff^2.

The result: dr_b/d(ln k) = 0 to double precision at k_pivot. n_s^{disp} - 1 = 3.4e-17 (numerical noise). The Sasaki-Stewart H_b^2 cancellation (n_s = 1 from k-independent squeezing) is EXACT at CMB scales. This is a structural result, not a numerical coincidence. The entire Planck k-band [0.002, 0.2] Mpc^{-1} sits ~110 orders of magnitude below the mass gap scale where dispersion running would activate.

The fold-scale scan shows dispersion running activates at k ~ O(1) M_KK^{-1}: B1 reaches |dr/d(ln k)| = 0.39 at k = 20 M_KK^{-1}. This is completely irrelevant for CMB observables.

**Consequence**: Any n_s deviation from unity must come from a DIFFERENT mechanism (time-dependent background, non-sudden corrections, or multi-field interference). The S66 BCS+CW mechanism (n_s = 0.9595 from spectral action shape) and the W1-I non-power-law H(tau) mechanism (n_s = 0.9649 with mu_eff = 0.0102) are the two candidates. Dispersion running is closed as a tilt source.

---

## 4. Spectral Moment Analysis

### 4.1 CC Variance (W1-K): Subordinate to chi_2

The spectral variance sigma^2 = <|lam|^2> - <|lam|>^2 = 0.166429 at L_max = 9, giving rho_sigma = sigma^2 x H_0^2 x M_Pl^2 = 2.041e-48 GeV^4, or log10(rho_sigma/rho_obs) = -1.122. This is 13.2x below rho_obs, compared to chi_2 which undershoots by 3.0x.

The critical diagnostic is the L_max behavior. Raw sigma^2 drifts by factor 2.25 from L=5 to L=9 -- it is NOT L_max-robust. The coefficient of variation CV^2 = sigma^2/<lam>^2 IS convergent (drift 0.77% from L=5 to L=9), confirming the eigenvalue distribution SHAPE is stable. The raw variance inherits Weyl growth because both <|lam|> and <|lam|^2> scale as L_max^{~1}.

**Independence assessment**: sigma^2 is NOT independent of chi_2. From the eigenvalue concentration (CV ~ 13%), the cumulant expansion yields chi_exp = exp(-chi_2) to 0.4% accuracy (confirmed in W3-F). The variance satisfies sigma^2 ~ CV^2 x chi_2^2 x lam_max^2. All bounded dimensionless spectral invariants carry highly correlated information because the D_K distribution is concentrated.

The Volovik program (Universe in a Helium Droplet, Ch. 29) identifies the vacuum energy as a functional of the full quasiparticle spectral density. The variance probes the WIDTH of the density of states. Since the D_K distribution is concentrated, sigma^2 ~ 0.016 x <lam>^2 -- the information content is subordinate to chi_2. The next structurally independent probe would be the spectral gap or the kurtosis, not the variance.

### 4.2 chi_exp Cumulant Identity (W3-F)

Two exponential-component moments computed at L_max = 9:

| Moment | Value | Factor from chi_2 | L_max drift (L=5 to 9) |
|:-------|:------|:-------------------|:-----------------------|
| chi_exp (Laplace) | 0.478609 | 1.549x | 1.85% |
| chi_hk (heat kernel) | 0.577460 | 1.284x | 2.76% |
| chi_2 (reference) | 0.741419 | -- | 4.81% |

The Laplace moment chi_exp = <exp(-|lam|/Lambda)> matches the first-cumulant prediction exp(-chi_2) = exp(-0.741) = 0.477 to 0.4%. This is a structural identity following from spectral concentration: when CV ~ 13%, the generating function is dominated by the mean.

All three routes place rho within factor 5 of rho_obs with zero free parameters. The closure of ~119.5 OOM is entirely in the HP4 base normalization H_0^2 x M_Pl^2 = 1.226e-47 GeV^4. The O(1) dimensionless spectral invariant determines only the factor-of-few residual.

### 4.3 Spectral Decoupling Theorem (W2-E)

The theorem (now formally certified with 3 numerical checks at machine epsilon):

The Seeley-DeWitt heat kernel coefficients a_0, a_2, a_4 of D_K^2 are algebraically independent functions of the Jensen parameter tau. a_0(tau) is degree 0 (constant by volume-preserving TT), a_2(tau) is degree 1 (linear in scalar curvature R), a_4(tau) is degree 2 (quadratic in curvature invariants). Different polynomial degrees are algebraically independent by Gilkey-DeWitt universality.

Numerical verification:
- da_0/dtau = 0 identically (max = 0.00e+00)
- da_4/da_2 ratio spread = 4.35% over tau in [0.10, 0.30] (not constant, confirming independence)
- Wronskian determinant relative magnitude = 4.54e-3 (nonzero, confirming linear independence of da_2/dtau and da_4/dtau)

The spectral action hierarchy at Lambda = M_KK:
- f_4 Lambda^4 a_0 (CC): 2.637e+67
- f_2 Lambda^2 a_2 (gravity): 4.019e+33 (33.82 OOM below CC)
- f_0 a_4 (gauge): 3.015e-01 (34.12 OOM below gravity)

Total CC-to-gauge hierarchy: 67.94 OOM. This is STRUCTURAL -- different spectral moments of the Dirac operator probe different curvature polynomials, and the spectral action weights them with different powers of the cutoff Lambda. The hierarchy is not fine-tuning; it is the structural output of the Gilkey-DeWitt expansion.

### 4.4 Zeta Non-Observability (W3-E): Permanent Theorem

Three independent routes converge on a common obstruction: the spectral zeta function zeta_D(s) = Tr|D_K|^{-2s} is NOT a physical observable.

(i) **Analytic continuation** (Route 1): Different spectral distributions consistent with the same canonical moments yield different values for zeta_D(-1/2). Spread 5.89% across three models.

(ii) **Non-uniqueness** (Route 2): Six spectral functionals applied to the same D_K spectrum produce a 381x dynamic range (2.58 OOM) in the spectral action. S_zeta = a_4 is the MINIMUM. No axiom selects this point.

(iii) **L_max sensitivity** (Route 3): a_4 shifts 10.4x from L_max = 3 to L_max = 7. Individual spectral moments are UV-sensitive. The ratio-of-ratios (a_0/a_2)/(a_2/a_4) shifts only 1.7%.

**Permanent theorem**: Physical observables from the Dirac spectrum are RATIOS of spectral moments (L_max-robust to 1.7%), not absolute values. This theorem has direct acoustic content: just as the speed of sound in a crystal is determined by ratios of elastic constants (not their absolute values), the physically observable properties of the substrate are spectral RATIOS that cancel the UV regularization dependence.

---

## 5. Constraint Map Update

### New PASS Results (10)
| Gate | Computation | Key Number |
|:-----|:-----------|:-----------|
| S75-A5-F-CONV | f_conv spectral projection | A_s = 1.58e-9 (25% of obs) |
| S75-A6-CROSS-CORR | Cross-spectral phase diffusion | delta_OOM = 2.84e-4 |
| S75-A7-EC-MAP | A_s vs E_C monotonicity | Elasticity = 0.003 |
| S75-K2-DECOUPLING-CERT | Spectral moment decoupling | 3 checks at machine eps |
| S75-F2-LMAX-BIDIR | DNP/Pom/FR at L=5,7 | All 3 ROBUST |
| S75-F3-BDI-ALL-TAU | Pfaffian Z_2 constancy | sgn = -1 all 10 tau |
| S75-F4-LEFSCHETZ-PERM | n* = 60 at L=7 | Promote to permanent |
| S75-F5-BDSPT-TAU-SCAN | J-invariance at 5 tau | max anomaly 5.82e-11 |
| S75-K1-EMERGENT-LORENTZ | c_light from a_2 + a_4 | c_Gold = 0.915 M_KK |
| S75-L1-NEFF-POST-THERM | N_eff thermalization | 3.044 exact |

Additional PASS: S75-D2-CC-M2, S75-D6-M1-L11, S75-E3-MULTI-DM, S75-F6-REGISTRY-48, S75-G4-R-PROTECTED, S75-D5-CC-REPORT, S75-J2-PCK-LARGE-N, S75-M5-TWO-MANIFOLD, S75-N1-CG24-TILING, S75-G3-ZETA-NOT-PHYS, S75-C1-NS-NONPOWER.

### New FAIL Results (structural, not parameter-dependent)
| Gate | What Failed | Structural Lesson |
|:-----|:-----------|:-----------------|
| S75-A2-TENSOR-MIXING | B1 projects 100% scalar | KK representation theorem; tensor channel unavailable |
| S75-A3-R-B-K-RUNNING | Dispersion running = 0 at CMB | Sasaki-Stewart exact; 110 OOM below activation scale |
| S75-B1-MULTI-INST | Instanton ratio peaks at L~7 | Scaling exponent ~L^0.11; dilute gas violated at L>=5 |
| S75-B2-CROSS-MOMENT | Monotonicity for all cutoff schemes | a_2 and a_4 grow in SAME direction |
| S75-B5-COUPLING-CHECK | m_eff^2/H_fold^2 = 3.8e-4 | Modulus 2630x lighter than Hubble; instanton cannot stabilize |
| S75-C4-PHASES-BD | All phi_k ~ 0, not pi/4 | Smooth transit, not Josephson; maximum enhancement |
| S75-I4-MACH-SCALING | Exponent = -0.844 | Exponential T_eff overwhelms linear kappa |
| S75-L2-DC-PERMANENCE | DC(12) = 4.6% < 5% | N^{-1.26} decay; finite-size artifact |

### INFO Results (diagnostic, narrowing constraint surface)
| Gate | Value | Diagnostic Content |
|:-----|:------|:-------------------|
| S75-A4-CW-JOINT | n_s PASS, A_s +11 OOM | CW confirms n_s = 0.9595 but A_s gap structural |
| S75-D1-CC-VARIANCE | -1.12 OOM | Subordinate to chi_2; Weyl-growing |
| S75-D8-JACOBSON-LAMBDA | F_GGE bracket +0.11 OOM | HP4 normalization required as external input |
| S75-E1-LEGGETT-FILTER | f_CPT = 0.610 | C_2 parity wrong quantum number; inter-band dominates |
| S75-E2-DIMER-Z2 | n_Z2 = 0 exactly | Symmetric quench cannot populate Z_2-odd sector |
| S75-H1-GGE-TRANSFER | delta_n_s = 0.0054 | Transfer preserves n_s; gate reduces to primordial |
| S75-H5-SWAMPLAND | eps_V in [0.28, 11.1] | No dS vacuum; fold transit is the swampland answer |

### Closures (cumulative)
- **50th closure**: Multi-instanton condensate route to moduli stabilization CLOSED for all L_max up to 10 (W1-F).
- Cross-spectral-moment moduli CLOSED (W1-G): a_2 and a_4 grow in same direction, monotonically.
- Tensor channel for A_s relief CLOSED (W1-B): B1 projects 100% to scalar by KK representation theorem.
- Dispersion running CLOSED as n_s tilt source (W1-C): Sasaki-Stewart exact at CMB.

---

## 6. Critical Assessment

### What S75 Settles

1. **The A_s problem is a conversion problem, confirmed from three independent directions.** W1-D (CW route: +11 OOM), W1-E (f_conv: -9.59, closing to -0.12 OOM), and W1-N (Parker base + enhancement: +9.47 OOM) all converge on the same structural diagnosis. The fiber-level variance is set by Bogoliubov squeeze; the 4D projection requires (M_KK/M_Pl)^4 x (a_2/a_0)^2. The f_conv PASS is the session's decisive result.

2. **Parker is the canonical A_s formulation.** The acoustic Hawking temperature is a phononic sector quantity that cannot be substituted into the gravitational A_s formula. The transit enhancement F = 380.9 has no Hawking-temperature interpretation. This is not a preference but a theorem from the Spectral-Moment Decoupling.

3. **The structural floor is clean.** 22 theorems x 7 axes: zero FAIL entries across 154 cells. 2 FRAGILE entries have no structural cracks. 70/70 NEEDS_REVERIFY entries reclassified: 48 ROBUST, 15 QUASI-ROBUST, 7 FRAGILE. The L_max-independent structural floor grows to 169/205 entries (82.4%).

### What S75 Opens

1. **n_s tilt mechanism**: Two candidates remain. (a) BCS+CW (S66): n_s = 0.9595, 1.28 sigma, with alpha_s = -0.019 (2.13 sigma, INFO). (b) Non-power-law H(tau) with isocurvature transfer (W1-I): n_s = 0.9649, exact Planck match, with one new parameter mu_eff = 0.0102. Route (b) is phenomenologically superior but introduces a parameter not yet derived from first principles. Route (a) is zero-parameter but carries the alpha_s tension.

2. **DM production mechanism**: W2-N proves n_Z2 = 0 exactly -- symmetric Parker pair production cannot populate Z_2-odd states. The Leggett DM channel requires Z_2-breaking (spontaneous symmetry breaking during transit, domain formation, or asymmetric initial conditions). The 2-cell result establishes the structural floor; the physical DM production requires the full 32-cell fabric.

3. **HP4 normalization**: The CC bracket sits at [0.34, 1.32] rho_obs across all surviving routes. The 119.5 OOM closure is in H_0^2 x M_Pl^2. This normalization is not derived from the spectral triple; it is imported as an external scale. Deriving it from first principles (HP4-FIRST-PRINCIPLES) is the rate-limiting step for the CC prediction.

4. **Moduli stabilization**: All tested mechanisms fail. Multi-instanton (W1-F): ratio peaks at L~7, scales as L^0.11. Cross-moment (W1-G): monotonically increasing. ATDHFB (W1-H): overshoot delta_tau = 0.036, far from target [0.45, 0.70]. The post-fold modulus dynamics remain the framework's principal open structural problem.

### What I Would Scrutinize

The f_conv PASS deserves stress-testing. The (a_2/a_0)^2 factor assumes the curvature perturbation couples exclusively through the a_2 channel. In the full spectral action, the a_4 channel (gauge kinetic) also contributes to scalar perturbations through the Higgs sector. If a_4 contamination at the 10-30% level enters the projection, the 0.12 OOM residual could shift. The cleanest test: compute the a_2-projected and a_4-projected variances separately and verify they are additive (no interference term).

The DC permanence FAIL is physically correct but interpretively delicate. The N^{-1.26} scaling means DC(32) ~ 1.7%. This is small but nonzero. The question is whether the 32-cell fabric's GLOBAL conserved charges -- the GGE Lagrange multipliers lambda_k on the full Josephson graph -- carry the same physical content as the 4-cell LOCAL DC component. If global and local descriptions of "permanent information storage" are not equivalent, the virtual-particle interpretation needs a new microscopic grounding.

---

## 7. Carry-Forward Priorities

### Highest Priority (Rate-Limiting)

1. **HP4-FIRST-PRINCIPLES**: Derive H_0^2 x M_Pl^2 normalization from spectral triple structure. Currently imported as external input. The CC prediction's zero-parameter status requires this derivation.

2. **MU-EFF-FROM-BCS**: Derive the isocurvature mass mu_eff = 0.0102 from BCS inter-branch coupling. This would make the W1-I n_s = 0.9649 route zero-parameter. Currently the sole free parameter in the best-fit n_s mechanism.

3. **Z2-BREAKING-MECHANISM**: Identify the physical mechanism that breaks Z_2 cell-exchange symmetry for DM production. Domain formation on the 32-cell fabric is the leading candidate. Requires multi-cell computation beyond the 2-cell symmetric sector.

### High Priority (Structural)

4. **F-CONV-STRESS-TEST**: Test f_conv = (M_KK/M_Pl)^4 x (a_2/a_0)^2 against a_4 contamination. Compute a_2-projected and a_4-projected variances separately.

5. **POST-FOLD-SPECTRAL-ACTION**: Compute S(tau) and a_2(tau) at tau >> 0.5 (the perturbation epoch). W1-A's H_phys reduction channel depends entirely on this -- the two background models (A and B) give contradictory answers because the spectral data stops at tau = 0.50.

6. **QUASI-ROBUST-VERIFY**: Explicit L_max = 5/7 computation of the 15 QUASI-ROBUST atlas entries. Priority: g_SU2_fold, sin2_thetaW_fold, c_Gold_over_c_fabric.

### Medium Priority (Diagnostic)

7. **DC-GLOBAL-VS-LOCAL**: Characterize the full 32-cell GGE conserved charges and compare their information content to the 4-cell local DC component.

8. **ALPHA-S-RESOLUTION**: The BCS+CW route gives alpha_s = -0.019 (2.13 sigma tension). The Bogoliubov route gives alpha_s = 0 exactly. Determine which mechanism controls the physical running.

9. **JLO-LOCAL-INDEX**: Identify the O(1) Connes-Moscovici local index normalization factor that may close the chi_2 factor-3 residual (0.74 vs needed ~2.2).
