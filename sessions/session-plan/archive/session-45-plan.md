# Session 45 Plan: Occupied-State Spectral Action, Bogoliubov n_s, and CC Routes

**Date**: 2026-03-15
**Author**: Gen-Physicist (session plan)
**Format**: Parallel single-agent computations across 8 waves
**Source**: S44 quicklook (31 computations, 8 structural results, 7 closures), S44 collab reviews (9 specialists + Sagan + Landau framework doc + master synthesis), S45 prereg (4 tiers, 42 distinct suggestions, 6 convergence clusters), S45 occupied-state specification, Landau classification document
**Motivation**: Session 44 proved G_N from three independent routes (factor 2.3 agreement), established CDM by algebraic construction (T^{0i}=0), closed the entire amplitude-projection class for n_s (epsilon_H ratio invariance theorem), and deepened the CC to an honest 110.5 orders. The session raised P from 12% to 23% on the strength of G_N triple convergence and CDM, but n_s remains the framework's most severe deficit. Session 45 attacks the two session-defining computations: the occupied-state spectral action (sole surviving tau-stabilization route) and the Kibble-Zurek Bogoliubov spectrum (sole surviving dynamical n_s route). The CC is addressed through analytic torsion and q-theory on the corrected discrete KK tower.
**Results file**: `sessions/session-45/session-45-results-workingpaper.md`

---

## I. Session Objective

Session 45 asks: **Does the occupied-state spectral action S_occ(tau) have a minimum, and does the Bogoliubov quench spectrum produce n_s = 0.965?**

These are the two remaining existential computations:

1. **Tau-stabilization (OCC-SPEC-45).** The S37 monotonicity theorem closed vacuum spectral action. S44 W4-4 closed foam-modified cutoffs. The sole surviving route is the occupied-state spectral action (Paper 16: Dong-Khalkhali-van Suijlekom 2022), which weights modes by BCS occupation numbers n_k(tau). The n_k are not monotone in tau because they depend on the self-consistent gap equation, which depends on van Hove singularity structure (9 at tau=0, 12 at tau>0, near-crossing at tau=0.19 with delta=0.0008). The S37 theorem's condition 3 (unit weighting) is violated. This is where the one-body / many-body partition dissolves: the spectral action (one-body) weighted by the BCS state (many-body) = Landau free energy evaluated at the physical state.

2. **Spectral tilt (KZ-NS-45).** The epsilon_H ratio invariance theorem (S44 W4-3, PERMANENT) closed the entire amplitude-projection class. The Lifshitz eta route is closed at 889 sigma (S44 W1-3). The spectral dimension flow has zero predictive dimension without scale selection (S44 W2-2). The sole surviving dynamical route is the Kibble-Zurek Bogoliubov spectrum: compute |beta_k|^2 from the sudden quench, extract P(k) = |beta_k|^2, and read off n_s from the slope. Six of seven S44 collab reviewers independently proposed this. Volovik's cross-check in S44: "n_s is quench dynamics (HOW FAST populated), not internal geometry (WHICH modes exist)."

**Sagan assessment (S44)**: Both PASS -> P = 60-75%. Both FAIL -> P = 3-8%. KZ-NS alone PASS -> P > 50%. OCC-SPEC alone PASS -> P = 35-45%.

**Landau prediction**: KZ-NS-45 will FAIL (n_s too red from d=3 KZ universality: n_s = -0.68). If correct, OCC-SPEC-45 is sole survivor.

**Pre-registered master gates**:
- **OCC-SPEC-45**: PASS if S_occ(tau) has local minimum at tau_min in [0.10, 0.25] with barrier > 1%. FAIL if monotone at all Lambda and all tau in [0.00, 0.50]. BONUS if tau_min within 10% of tau_fold = 0.190.
- **KZ-NS-45**: PASS if n_s in [0.955, 0.975] from Bogoliubov coefficients. FAIL if n_s outside [0.80, 1.10].

---

## II. Wave Structure

### Dependency Graph

```
WAVE 1 (ROOT -- 2 session-defining, parallel)
  W1-1: OCC-SPEC-45          [tau-stab: occupied-state SA minimum search]
  W1-2: KZ-NS-45             [n_s: Bogoliubov quench spectrum]
         |              |
         v              v
     DECISION POINT 1
         |
         v
WAVE 2 (depends on W1 verdicts)
  W2-1: ANALYTIC-TORSION-45   [CC: Ray-Singer torsion on SU(3)]
  W2-2: ALPHA-EFF-45           [DM/DE: non-eq specific heat from GGE]
  W2-3: Q-THEORY-KK-45         [CC: q-theory on discrete KK tower]
  W2-4: LK-RELAX-45            [IF OCC-SPEC PASS: relaxation dynamics]
       OR SIGMA-SELECT-45      [IF KZ-NS FAIL: scale selection principle]
         |              |
         v              v
WAVE 3 (depends on W1-W2 landscape)
  W3-1: MKK-TENSION-45         [resolve 0.83-decade M_KK tension]
  W3-2: ECOND-RECONCILE-45     [resolve 0.115 vs 0.137]
  W3-3: DEBYE-WALLER-45        [thermal correction to spectral action]
  W3-4: QNM-NS-45              [linearized Friedmann-modulus QNM spectrum]
         |              |
         v              v
WAVE 4 (diagnostics + infrastructure)
  W4-1: DATA-PROVENANCE-45     [complete S7-S24 upstream audit]
  W4-2: KRETSCHNER-12D-45      [R_{abcd}R^{abcd} on M^4 x SU(3)]
  W4-3: DOS-FINE-SCAN-45       [tau in [0.19, 0.21], T3-T5 crossing]
  W4-4: EULER-DEFICIT-45       [prove E = sum T_k S_k - PV + sum mu_k N_k + |E_cond|]
         |              |
         v              v
WAVE 5 (specialist -- remaining collab suggestions)
  W5-1: SAKHAROV-UV-DISSOLUTION-45  [link Lambda_eff ~ 10 M_KK to dissolution]
  W5-2: OCCUPIED-CYCLIC-45     [cyclic cohomology for occupied-state triple]
  W5-3: GL-GGE-STABILITY-45    [GL free energy landscape F(T_1,...,T_8)]
  W5-4: RUNNING-GN-45          [Sakharov G_N(tau) across full transit]
  W5-5: WEAK-ORDER-ONE-45      [weak order-one condition test, Connes Paper 25]
         |              |
         v              v
WAVE 6 (specialist -- remaining collab suggestions continued)
  W6-1: BAYESIAN-MODEL-45      [q-theory vs spectral action Bayes factor]
  W6-2: ACOUSTIC-CASIMIR-45    [phononic Casimir force between domain walls]
  W6-3: PETER-WEYL-CENSORSHIP-45  [non-singlet leakage at 1/sqrt(N)]
  W6-4: GGE-BEATING-45         [autocorrelation C(t) from 8 GGE modes]
  W6-5: TWO-FLUID-DESI-45      [Landau-Khalatnikov cosmology -> DESI w(z)]
  W6-6: SPECTRAL-PENROSE-45    [spectral Penrose diagram (tau, lambda_k)]
         |              |
         v              v
WAVE 7 (reconciliation)
  W7-1: FORMULA-AUDIT-REPORT   [audit all S45 formulas per protocol]
  W7-2: CC-GAP-UPDATE-45       [updated CC gap with S45 results]
  W7-3: CONSTRAINT-MAP-45      [full constraint surface update]
         |
         v
WAVE 8 (assessment -- LAST)
  W8-1: Sagan Assessment        [probability update from 23% prior]
```

### Decision Points

**DECISION POINT 1** (after Wave 1):

| OCC-SPEC-45 | KZ-NS-45 | Wave 2 Configuration |
|:------------|:---------|:--------------------|
| PASS (minimum found) | PASS (n_s in window) | W2-4 = LK-RELAX-45 (relaxation dynamics near minimum). Compute r from Bogoliubov. Framework VIABLE. |
| PASS (minimum found) | FAIL (n_s outside) | W2-4 = LK-RELAX-45. n_s from relaxation near minimum (different route). Framework partially viable. |
| FAIL (monotone) | PASS (n_s in window) | W2-4 = no LK-RELAX. n_s EXPLAINED but tau-stab unsolved. Spectral action exhausted for tau-stab. Add SIGMA-SELECT-45. |
| FAIL (monotone) | FAIL (n_s outside) | W2-4 = SIGMA-SELECT-45. Both session-defining gates FAIL. P drops to 3-8%. Compute whether any path remains. |

### Task Count by Wave

| Wave | Tasks | Priority |
|:-----|:------|:---------|
| 1 | 2 | CRITICAL |
| 2 | 4 | HIGH |
| 3 | 4 | HIGH/MEDIUM |
| 4 | 4 | MEDIUM |
| 5 | 5 | MEDIUM/LOW |
| 6 | 6 | LOW |
| 7 | 3 | META |
| 8 | 1 | META |
| **Total** | **29** | -- |

### Standing Sentinels (no computation, monitoring)

| ID | Trigger | Instrument |
|:---|:--------|:-----------|
| W-FOAM-8 | sigma_wa < 0.172 | DESI DR3 |
| GQUEST-NULL | Any pixellon signal | GQuEST |
| SIMONS-43 | >3 sigma CMB lensing enhancement | Simons Obs |
| BICEP-R | r > 10^{-5} | LiteBIRD/CMB-S4 |

---

## III. Wave Prompts

Each wave is in a separate file for deployment:

- **Wave 1**: `sessions/session-plan/session-45-wave1.md` (2 CRITICAL session-defining)
- **Wave 2**: `sessions/session-plan/session-45-wave2.md` (4 HIGH CC + DM/DE + conditional)
- **Wave 3**: `sessions/session-plan/session-45-wave3.md` (4 HIGH/MEDIUM diagnostics)
- **Wave 4**: `sessions/session-plan/session-45-wave4.md` (4 MEDIUM infrastructure)
- **Wave 5**: `sessions/session-plan/session-45-wave5.md` (5 specialist)
- **Wave 6**: `sessions/session-plan/session-45-wave6.md` (6 specialist continued)
- **Wave 7**: `sessions/session-plan/session-45-wave7.md` (3 reconciliation)
- **Wave 8**: `sessions/session-plan/session-45-wave8.md` (1 Sagan assessment)

---

## III-a. Wave 1: CRITICAL PATH (2 session-defining, parallel)

### W1-1: Occupied-State Spectral Action Minimum Search (OCC-SPEC-45)

**Agent**: `connes-ncg-theorist` (primary), `nazarewicz-nuclear-structure-theorist` (cross-check)
**Additional Researcher Context**: `researchers/Connes/16_2022_Dong_Khalkhali_van_Suijlekom_Second_quantization_spectral_action.md`, `researchers/Landau/index.md`
**Model**: opus
**Cost**: HIGH (BCS self-consistent gap at 20 tau values x 992 modes)

**Prompt**:

You are computing the single most important quantity remaining in the phonon-exflation framework: the occupied-state spectral action S_occ(tau), and whether it has a local minimum that could stabilize the Jensen modulus tau.

**Why this is critical.** The S37 Structural Monotonicity Theorem (CUTOFF-SA-37) proved that for any monotone decreasing cutoff function f, S_vac(tau) = Tr f(D_K(tau)^2 / Lambda^2) is monotone increasing in tau. This closed tau-stabilization through the vacuum spectral action. Session 44 W4-4 (F-FOAM-2) closed foam-modified non-monotone cutoffs: 0/900 minima found. Every attempt to find a minimum in the vacuum spectral action has failed across Sessions 37-44. The occupied-state spectral action is the SOLE SURVIVING route within the spectral action framework.

**The loophole.** The S37 theorem sums over ALL modes with UNIT weight. The physical system does not populate all modes equally. Paper 16 (Dong-Khalkhali-van Suijlekom 2022, `researchers/Connes/16_2022_Dong_Khalkhali_van_Suijlekom_Second_quantization_spectral_action.md`) extends the spectral action to finite density:

    S_occ(tau) = sum_k d_k * n_k(tau) * f(lambda_k(tau)^2 / Lambda^2)

where n_k(tau) = v_k(tau)^2 = (1/2)(1 - xi_k(tau) / E_k(tau)) are the BCS Bogoliubov occupation numbers. These depend on tau through BOTH the eigenvalues lambda_k(tau) AND the self-consistent gap Delta(tau). The S37 theorem's proof requires:

1. f is monotone decreasing (retained)
2. lambda_k(tau) are eigenvalues of D_K on the Jensen family (retained)
3. The sum runs over ALL modes with unit weight (VIOLATED by n_k)

The occupation numbers n_k are NOT monotone in tau because they depend on the van Hove singularity structure, which changes during the transit (S44 W6-8: 9 singularities at tau=0, 12 at tau>0, near-crossing at tau=0.19 with delta=0.0008).

**Landau interpretation.** The vacuum spectral action S_vac(tau) is the Landau free energy F(eta) evaluated at the VACUUM (all modes equally weighted, no condensate). The occupied-state spectral action S_occ(tau) is F(eta_0) -- the free energy evaluated at the PHYSICAL STATE (modes weighted by BCS occupation numbers). The S37 theorem proves F(0) is monotone. It says nothing about F(eta_0). In Landau theory, F(eta_0) is NOT monotone: the condensation energy F_cond = -a^2(T_c - T)^2 / (4b) creates a turning point below T_c.

**The derivative decomposition.** The key equation:

    dS_occ/dtau = sum_k d_k [(dn_k/dtau) * f(lambda_k^2/Lambda^2) + n_k * f'(lambda_k^2/Lambda^2) * 2*lambda_k * (dlambda_k/dtau) / Lambda^2]

The second term (eigenvalue change) has the same sign as in S37 (monotone contribution). The FIRST term (occupation change) has no definite sign. Near a van Hove singularity where dn_k/dtau is large and positive (pairing spike), the first term can overwhelm the second, creating a non-monotone S_occ.

**Known adversarial risks (from `s45-prereg-occupied-state.md` Section "Why This Might Fail"):**
1. Occupation numbers may be too smooth (BCS mean-field washes out van Hove spikes)
2. The gap may vanish before the fold (n_k -> step function, reducing to monotone)
3. The near-crossing at tau=0.19 may be too weak (delta=0.0008)
4. Wrong functional (S_occ may not be the gravitating functional)
5. Truncation artifact (992 modes at max_pq_sum=6 insufficient near van Hove)

**Computation Steps**:

1. **Load spectrum.** Eigenvalues lambda_k(tau) from `tier0-computation/s41_spectral_refinement.npz` (multiple tau) and `tier0-computation/s36_sfull_tau_stabilization.npz`. Peter-Weyl degeneracies d_k = dim(p,q)^2 = ((p+1)(q+1)(p+q+2)/2)^2 from standard formula. Also load: `tier0-computation/s42_hauser_feshbach.npz` (992 eigenvalues at fold, sector labels, multiplicities), `tier0-computation/s38_cc_instanton.npz` (BCS coupling, Delta_0), `tier0-computation/s44_dos_tau.npz` (van Hove tracking), `tier0-computation/s44_vanhove_track.npz`.

2. **BCS gap equation at each tau.** For tau = 0.00, 0.02, 0.05, 0.08, 0.10, 0.12, 0.14, 0.16, 0.17, 0.18, 0.185, 0.190, 0.195, 0.20, 0.22, 0.25, 0.30, 0.35, 0.40, 0.50:
   - Compute eigenvalues at that tau (use `tier0-computation/tier1_dirac_spectrum.py` if not already stored)
   - Compute DOS N(E, tau) from eigenvalues
   - Solve the self-consistent BCS gap equation: 1/g = sum_k d_k / (2 * E_k) where E_k = sqrt(xi_k^2 + Delta^2) and xi_k = lambda_k - mu (mu=0, S34 result). Use the BCS coupling from S35/S38: the B2 pairing interaction V_eff
   - Obtain Delta(tau) and the Bogoliubov amplitudes u_k(tau), v_k(tau)
   - Compute occupation numbers: n_k(tau) = v_k(tau)^2 = (1/2)(1 - xi_k / E_k)

3. **Occupied-state spectral action.** For each tau, compute:

       S_occ(tau) = sum_k d_k * n_k(tau) * f(lambda_k(tau)^2 / Lambda^2)

   with THREE cutoff functions for robustness:
   - f(x) = exp(-x) (standard exponential)
   - f(x) = theta(1-x) (sharp cutoff)
   - f(x) = (1+x)^{-3} (polynomial decay)

   Use Lambda = M_KK as the natural scale.

4. **Vacuum spectral action comparison.** Compute S_vac(tau) = sum_k d_k * f(lambda_k^2/Lambda^2) at the same 20 tau points. Verify monotonicity (S37 theorem cross-check). If S_vac is NOT monotone in your computation, there is a bug. This is a hard cross-check.

5. **Search for minimum.** Plot S_occ(tau). Check:
   - Is there a local minimum? (dS_occ/dtau = 0 with d^2S_occ/dtau^2 > 0)
   - Where is it? (tau_min)
   - How deep? (barrier = max(S_occ(tau_shoulder), S_occ(0)) - S_occ(tau_min))
   - Barrier height as fraction of S_occ(tau_min): must exceed 0.01 for PASS
   - Cutoff-robust? (does it survive all three f choices?)

6. **Decompose the mechanism.** If minimum found, identify which modes drive it:
   - Compute dS_occ/dtau = sum_k d_k [dn_k/dtau * f + n_k * f' * 2*lambda_k * dlambda_k/dtau / Lambda^2]
   - Separate the occupation-change term (first) from the eigenvalue-change term (second)
   - Which sectors (B1, B2, B3) contribute to each?
   - Is the van Hove near-crossing at tau=0.19 (W6-8: T3-T5, delta=0.0008) the driver?

7. **Barrier dynamics.** If minimum exists, compute:
   - Barrier height in M_KK^4 units
   - Oscillation frequency at the minimum: omega_osc^2 = d^2S_occ/dtau^2 (in appropriate kinetic normalization)
   - Dwell time: t_dwell ~ 1/omega_osc
   - Does dwell time exceed H^{-1}? (tau-stabilization criterion)

8. **Bosonic ratio check.** S44 W4-2 proved a_2^bos/a_2^Dirac = 61/20 exact (tau-independent) for the VACUUM spectral action. Compute the occupied-state analog: a_2^{occ,bos} / a_2^{occ,Dirac}. Is the 61/20 ratio preserved, or does occupation-weighting break it?

**FORMULA AUDIT PROTOCOL** (mandatory, 4/7 convergence):
- (a) State every formula with explicit units before computing
- (b) Dimensional check: verify [S_occ] = [dimensionless] (cutoff-weighted eigenvalue sum)
- (c) Limiting case: at n_k = 1 for all k, S_occ = S_vac (must recover vacuum result)
- (d) Cite: Paper 16 Theorem 4 for S_occ definition; S38 for BCS parameters; S34 for mu=0

**Pre-registered gate OCC-SPEC-45**:
- **PASS**: S_occ(tau) has a local minimum at tau_min in [0.10, 0.25] with barrier height > 0.01 * S_occ(tau_min)
- **FAIL**: S_occ(tau) is monotone at all Lambda and all tau in [0.00, 0.50]
- **INFO**: Minimum exists but barrier height < 0.01 (too shallow for dynamical trapping)
- **BONUS**: tau_min within 10% of tau_fold = 0.190 (self-consistent fold selection)

**Input files**:
- `tier0-computation/s41_spectral_refinement.npz`
- `tier0-computation/s36_sfull_tau_stabilization.npz`
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s38_cc_instanton.npz`
- `tier0-computation/s36_mmax_authoritative.npz`
- `tier0-computation/s44_dos_tau.npz`
- `tier0-computation/s44_vanhove_track.npz`
- `tier0-computation/tier1_dirac_spectrum.py` (for new tau values)
- `researchers/Connes/16_2022_Dong_Khalkhali_van_Suijlekom_Second_quantization_spectral_action.md`

**Output files**:
- Script: `tier0-computation/s45_occ_spectral.py`
- Data: `tier0-computation/s45_occ_spectral.npz`
- Plot: `tier0-computation/s45_occ_spectral.png`

**Working paper section**: W1-1

**Cross-check agent**: nazarewicz-nuclear-structure-theorist
- Independent BCS gap solver (Strutinsky-smoothed DOS vs raw)
- Verify n_k(tau) at 5 anchor points (tau = 0.00, 0.10, 0.19, 0.25, 0.50)
- Flag if S_vac monotonicity cross-check fails
- Report: `tier0-computation/s45_occ_spectral_crosscheck.py`

---

### W1-2: Kibble-Zurek Bogoliubov Spectrum for n_s (KZ-NS-45)

**Agent**: `volovik-superfluid-universe-theorist` (primary), `einstein-theorist` (cross-check)
**Additional Researcher Context**: `researchers/Volovik/index.md`, `researchers/Einstein/index.md`
**Model**: opus
**Cost**: HIGH

**Prompt**:

You are computing the single most diagnostic cosmological quantity for the framework: the spectral tilt n_s from the Bogoliubov particle creation spectrum during the transit. This is the framework's LAST surviving route to n_s after the epsilon_H ratio invariance theorem (S44 W4-3) permanently closed all amplitude-projection mechanisms, the Lifshitz eta route closed at 889 sigma (S44 W1-3), and the spectral dimension flow was shown to have zero predictive dimension (S44 W2-2).

**Why Bogoliubov.** The transit is a SUDDEN QUENCH, not a slow-roll inflation. S38 established: P_exc = 1.000, tau_Q / tau_BCS ~ 10^{-5}, S_inst = 0.069 (quantum critical, not tunneling). The perturbation spectrum is NOT set by the potential shape (epsilon_H = 2.999, invariant under any projection). It is set by the Bogoliubov coefficients |beta_k|^2, which depend on how the eigenvalue spectrum changes during the quench. This is Parker-type cosmological particle creation (S38: NOT Hawking, no horizon, no thermal spectrum).

**The computation.** For a mode with eigenvalue lambda_k that changes from lambda_k^{in} (pre-transit) to lambda_k^{out} (post-transit), the Bogoliubov coefficient is:

    |beta_k|^2 = (Delta E_k)^2 / (4 E_k^{in} E_k^{out})

where E_k = sqrt(xi_k^2 + Delta^2) is the BdG quasiparticle energy. For a sudden quench (instantaneous change), this gives the occupation of the post-transit modes in terms of pre-transit quantum numbers. The power spectrum:

    P(k) = |beta_k|^2 * k^3

where k is the 4D wavenumber corresponding to mode k (requires the KK -> 4D scale mapping). The spectral tilt:

    n_s - 1 = d ln P(k) / d ln k  evaluated at the pivot scale k_* = 0.05 Mpc^{-1}

**Landau's adversarial prediction.** The Landau classification document (Section VI.C) predicts KZ-NS-45 will FAIL. The standard KZ formula gives:

    n_s - 1 = -d * z * nu / (1 + z * nu)

For d=3, z=2.024, nu=0.6301 (3D Ising, S43 BCS-CLASS-43): n_s = -0.68 (far too red). For d=1 (single modulus): n_s = 0.44 (still too red by 20 sigma). The Landau argument is that NO combination of d=1,2,3 with the framework's z and nu gives n_s in the Planck window.

**The counter-argument.** The KZ formula applies to DEFECT DENSITY from continuous symmetry breaking. The framework's transit is: (a) a quench of discrete modes on a compact manifold (not continuous defect formation), (b) the relevant spectrum is the BdG quasiparticle spectrum (not the order parameter field), and (c) the sudden-quench limit (tau_Q << tau_BCS) may give different scaling from the adiabatic-impulse approximation. The Bogoliubov computation does NOT assume the KZ scaling formula -- it computes |beta_k|^2 directly from the eigenvalue change. This is why 6/7 reviewers converged on it: it bypasses the KZ formula entirely.

**Computation Steps**:

1. **Load eigenvalue data.** From `tier0-computation/s42_hauser_feshbach.npz` (992 eigenvalues at fold), `tier0-computation/s41_spectral_refinement.npz` (eigenvalues at multiple tau), `tier0-computation/s38_cc_instanton.npz` (BCS parameters, quench parameters), `tier0-computation/s44_dos_tau.npz` (van Hove evolution).

2. **Pre-transit and post-transit spectra.** Define:
   - Pre-transit: lambda_k^{in} at tau = 0 (round SU(3), maximal degeneracy)
   - Post-transit: lambda_k^{out} at tau = tau_fold = 0.190 (Jensen-deformed SU(3))
   - BCS gap: Delta(tau=0.19) from s38 data (or recompute from gap equation)
   - Chemical potential: mu = 0 (S34 result, PH-forced)

3. **Bogoliubov coefficients.** For each of the 992 modes, compute:

       E_k^{in} = sqrt((lambda_k^{in})^2 + Delta_0^2)
       E_k^{out} = sqrt((lambda_k^{out})^2 + Delta_out^2)

   where Delta_0 is the gap at pre-transit and Delta_out is the gap at post-transit (possibly zero, since P_exc = 1.000 means condensate destroyed).

   For the sudden quench:

       |beta_k|^2 = ((E_k^{in} - E_k^{out})/(2*sqrt(E_k^{in} * E_k^{out})))^2

   FORMULA AUDIT: (a) Units: |beta_k|^2 is dimensionless (ratio of energies squared). (b) Dimensional check: [E] = M_KK in both numerator and denominator. (c) Limiting case: if lambda_k^{in} = lambda_k^{out} and Delta_0 = Delta_out, then |beta_k|^2 = 0 (no particle creation from no change). (d) Cite: Parker (1968), Birrell-Davies Ch. 3, S38 W4 (Parker-type identification).

4. **4D wavenumber assignment.** The KK modes (p,q) have an internal "momentum" proportional to the Casimir C_2(p,q) = (p^2 + q^2 + pq + 3(p+q))/3. The 4D wavenumber k_4D corresponding to a KK mode is determined by the Hubble rate at the time of creation:

       k_4D = a(t_creation) * H(t_creation)

   For modes created at different times during the transit, the mapping k_4D = k_4D(lambda_k, tau_creation) must be specified. Compute this from the Friedmann equation using S44 W4-3 parameters (H, a, epsilon_H at the fold).

   Alternative approach: if all modes are created simultaneously (sudden quench), then k_4D depends only on the internal quantum numbers through the mode's contribution to the 4D metric perturbation. In this case:

       k_4D / k_0 = sqrt(C_2(p,q) / C_2(0,0))

   where k_0 is the pivot scale. Use BOTH approaches and compare.

5. **Power spectrum.** Compute:

       P(k) = sum_{modes at k} d_k * |beta_k|^2

   where the sum is over all KK modes that map to the same 4D wavenumber k. Plot P(k) vs k.

6. **Spectral tilt.** Fit ln P(k) vs ln k in the range around the pivot scale. Extract:

       n_s - 1 = d ln P / d ln k

   Report n_s with uncertainty from the fit.

7. **Running.** Compute the running:

       alpha_s = d n_s / d ln k

   Report and compare to Planck constraint alpha_s = -0.0045 +/- 0.0067.

8. **Tensor spectrum.** If PASS, compute the tensor power spectrum from the same Bogoliubov coefficients applied to the tensor sector. Extract r = P_T / P_S. Compare to S44 W3-4 result r = 3.86e-10.

9. **Sensitivity analysis.** Report n_s for:
   - Delta_0 varied by +/- 50%
   - tau_fold varied by +/- 10% (0.17, 0.19, 0.21)
   - Quench profile: sudden vs linear ramp over delta_tau = 0.01, 0.05
   - k_4D mapping: both approaches from step 4

**FORMULA AUDIT PROTOCOL** (mandatory):
- (a) State |beta_k|^2 formula with explicit dimensions
- (b) Verify [|beta_k|^2] = dimensionless
- (c) Limiting case: no quench -> |beta_k|^2 = 0 for all k
- (d) Cite: Parker (1968), Birrell-Davies (1982) Ch. 3

**Pre-registered gate KZ-NS-45**:
- **PASS**: n_s in [0.955, 0.975] from Bogoliubov coefficients
- **FAIL**: n_s outside [0.80, 1.10] (extended window acknowledging systematic uncertainties in k-mapping)
- **INFO**: n_s in [0.80, 1.10] but outside [0.955, 0.975] (within extended window, not Planck-precise)
- **BONUS**: alpha_s consistent with Planck within 2 sigma

**Input files**:
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s41_spectral_refinement.npz`
- `tier0-computation/s38_cc_instanton.npz`
- `tier0-computation/s44_dos_tau.npz`
- `tier0-computation/s44_vanhove_track.npz`
- `tier0-computation/s42_constants_snapshot.npz`
- `researchers/Volovik/21_2016_Kibble_Zurek_Phase_Transitions.md` (if available)

**Output files**:
- Script: `tier0-computation/s45_kz_ns.py`
- Data: `tier0-computation/s45_kz_ns.npz`
- Plot: `tier0-computation/s45_kz_ns.png`

**Working paper section**: W1-2

**Cross-check agent**: einstein-theorist
- Independent Bogoliubov coefficient computation
- Verify |beta_k|^2 vanishes for modes with lambda_k^{in} = lambda_k^{out}
- Test alternative quench profiles (linear ramp, tanh profile)
- Report: `tier0-computation/s45_kz_ns_crosscheck.py`

---

## III-b. Wave 2: HIGH PRIORITY (4 tasks, depends on W1 verdicts)

### W2-1: Analytic Torsion of SU(3) at the Fold (ANALYTIC-TORSION-45)

**Agent**: `connes-ncg-theorist` (primary), `nazarewicz-nuclear-structure-theorist` (Strutinsky cross-check)
**Additional Researcher Context**: `researchers/Spectral-Geometry/index.md`, `researchers/Connes/index.md`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are computing the Ray-Singer analytic torsion T(SU(3), g_fold) at the fold metric. This is the geometric contribution to the post-transit CC. S44 W1-4 established that the post-transit BCS vacuum energy is exactly zero (P_exc = 1.000, condensate destroyed). The residual CC is purely GEOMETRIC: Tr ln(D_K^2) evaluated on SU(3) at the Jensen-deformed metric. The analytic torsion measures this geometric contribution.

**Definition.** The Ray-Singer analytic torsion is:

    T(M, g) = exp(-(1/2) sum_q (-1)^q q zeta'_{Delta_q}(0))

where zeta_{Delta_q}(s) = Tr(Delta_q^{-s}) is the spectral zeta function of the Laplacian on q-forms on M.

For our purposes, the relevant quantity is the spectral zeta function of D_K^2:

    zeta_{D_K^2}(s) = sum_k d_k lambda_k^{-2s}

and the analytic torsion contribution:

    T = exp(-(1/2) zeta'_{D_K^2}(0))

Compute zeta'(0) by numerical differentiation of the partial sums of lambda_k^{-2s} at s -> 0 (using Hurwitz zeta techniques or direct analytic continuation).

**Gate ANALYTIC-TORSION-45**: PASS if log10(T) < -50 (at least 50 orders of CC suppression). FAIL if T = O(1) (no suppression). INFO if T computed but interpretation unclear.

**FORMULA AUDIT**: (a) Units: T is dimensionless (exponential of a spectral invariant). (b) Dimensional check: zeta'(0) is dimensionless (spectral zeta at s=0). (c) Limiting case: for S^1 of length L, T(S^1) = L/(2 pi). For round S^3, T = 1. (d) Cite: Ray-Singer (1971), Cheeger-Muller theorem.

**Input files**: `tier0-computation/s42_hauser_feshbach.npz`, `tier0-computation/s41_spectral_refinement.npz`
**Output files**: Script `tier0-computation/s45_analytic_torsion.py`, Data `tier0-computation/s45_analytic_torsion.npz`, Plot `tier0-computation/s45_analytic_torsion.png`
**Working paper section**: W2-1

---

### W2-2: Non-Equilibrium Specific Heat for DM/DE (ALPHA-EFF-45)

**Agent**: `volovik-superfluid-universe-theorist` (primary), `landau-condensed-matter-theorist` (cross-check)
**Additional Researcher Context**: `researchers/Volovik/index.md`, `researchers/Landau/index.md`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are computing the non-equilibrium specific heat exponent alpha_eff from the 8-temperature GGE, which determines the DM/DE ratio. S44 W6-4 found the best equilibrium estimate: DM/DE = 1.06 (2.7x observed 0.387). The GGE has 8 independent temperatures (S44 W6-5), 3 of which are negative. The equilibrium specific heat exponents (Bose alpha=3, Fermi alpha=2, 3D Ising alpha=0.110) do not match the observed 0.387. The non-equilibrium computation is needed.

**Method.** From the 8 Richardson-Gaudin conserved integrals I_k and the GGE Lagrange multipliers lambda_k (the "8 temperatures"):
1. Load 8 GGE temperatures from `tier0-computation/s44_multi_t_jacobson.npz`
2. Compute the energy-temperature response matrix C_kl = dE_k / dT_l
3. Diagonalize C_kl to obtain heat capacity eigenvalues (3 negative from S44 W6-5)
4. Define alpha_eff from Omega_DM / Omega_DE = f(eigenvalue spectrum)
5. Test whether the 3 negative eigenvalues produce sublinear alpha_eff ~ 0.39

**Gate ALPHA-EFF-45**: PASS if alpha_eff in [0.3, 0.5]. FAIL if alpha_eff > 2.0. INFO if computed but model-dependent.

**FORMULA AUDIT**: (a) C_kl in units of dimensionless (energy/temperature). (b) Dimensional check. (c) Limiting case: if all T_k equal, C_kl reduces to scalar C = dE/dT, and alpha_eff = equilibrium alpha. (d) Cite: Landau Paper 04 Section 4, Volovik Paper 05 Section 2.

**Input files**: `tier0-computation/s44_multi_t_jacobson.npz`, `tier0-computation/s42_gge_energy.npz`, `tier0-computation/s44_dm_de_ratio.npz`
**Output files**: Script `tier0-computation/s45_alpha_eff.py`, Data `tier0-computation/s45_alpha_eff.npz`, Plot `tier0-computation/s45_alpha_eff.png`
**Working paper section**: W2-2

---

### W2-3: Volovik q-Theory on Discrete KK Tower (Q-THEORY-KK-45)

**Agent**: `volovik-superfluid-universe-theorist` (primary), `hawking-theorist` (Gibbs-Duhem cross-check)
**Additional Researcher Context**: `researchers/Volovik/15_2009_Volovik_Topology_Vacuum_Energy.md`, `researchers/Volovik/16_2008_Volovik_q_Theory_Cosmological_Constant.md`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are computing the Volovik q-theory self-tuning mechanism on the CORRECTED discrete KK tower (trace-log functional + EIH singlet projection + discrete eigenvalue spectrum). S43 QFIELD-43 found a zero-crossing at tau ~ 1.23 (outside physical domain [0, 0.50]). The three S44 corrections (trace-log: 5.11 orders, EIH singlet: 4.25 orders, corrected Vol(SU(3))) change the integrand by ~10 orders. Does the crossing move into the physical domain?

**Method.**
1. Construct the q-theory vacuum variable: q = trace-log vacuum energy density (not polynomial spectral action)
2. Apply EIH singlet projection: only the (0,0) representation gravitates (f_s = 5.684e-5, S44 W2-3)
3. Use the corrected discrete KK tower (992 eigenvalues from s42_hauser_feshbach.npz)
4. Solve the stationarity condition d rho(q) / dq = 0 for q_0(tau)
5. Evaluate rho(q_0(tau)) across tau in [0.00, 0.50] at 50 points
6. Search for zero-crossing: rho(q_0(tau*)) = 0

**Gate Q-THEORY-KK-45**: PASS if zero-crossing at tau* in [0.10, 0.25]. FAIL if no crossing in [0.00, 0.50]. INFO if crossing exists but at different tau.

**FORMULA AUDIT**: (a) rho(q) in GeV^4. (b) Dimensional check: q is dimensionless, rho has mass dimension 4. (c) Limiting case: continuous spectrum -> Volovik Papers 15-16 result. (d) Cite: Volovik Papers 15-16 (q-theory), S44 W1-4 (trace-log), S44 W2-3 (EIH singlet).

**Input files**: `tier0-computation/s43_qtheory_selftune.npz`, `tier0-computation/s44_tracelog_cc.npz`, `tier0-computation/s44_eih_grav.npz`, `tier0-computation/s42_hauser_feshbach.npz`
**Output files**: Script `tier0-computation/s45_qtheory_kk.py`, Data `tier0-computation/s45_qtheory_kk.npz`, Plot `tier0-computation/s45_qtheory_kk.png`
**Working paper section**: W2-3

---

### W2-4: CONDITIONAL — Depends on Wave 1 Verdicts

**IF OCC-SPEC-45 PASS**: LK-RELAX-45 (Landau-Khalatnikov Relaxation Dynamics)

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt (if deployed)**:

OCC-SPEC-45 found a minimum in S_occ at tau_min. You are computing the Landau-Khalatnikov relaxation dynamics near this minimum: the oscillation frequency, damping rate, dwell time, and the n_s prediction from relaxation near the minimum.

Solve the LK equation (Paper 09, eq. 1):

    d(tau)/dt = -(1/tau_0) dS_occ/dtau

Linearize near tau_min: d(delta_tau)/dt = -(1/tau_0) S_occ''(tau_min) delta_tau

omega_osc = sqrt(S_occ''(tau_min) / tau_0). Dwell time ~ 1/omega_osc. N_e during oscillation ~ H / omega_osc.

**Gate LK-RELAX-45**: PASS if N_e > 10 during dwell (sufficient for observable signature). FAIL if N_e < 0.1. INFO otherwise.

**IF KZ-NS-45 FAIL**: SIGMA-SELECT-45 (Scale Selection Principle)

**Agent**: `connes-ncg-theorist` (primary), `hawking-theorist` (backreaction)
**Model**: opus
**Cost**: LOW

**Prompt (if deployed)**:

KZ-NS-45 failed to produce n_s in the Planck window. S44 W2-2 found n_s = 0.961 at sigma = 1.10 in the spectral dimension flow, but sigma is unfixed. You are searching for a self-consistency principle that selects sigma.

Test three routes:
1. Backreaction: Lambda = Lambda(tau, d_s) self-consistency loop
2. Hubble matching: sigma = 1/H^2 at the pivot scale
3. Occupied-state sigma: replace D_K^2 with n_k * D_K^2 in the heat kernel

**Gate SIGMA-SELECT-45**: PASS if self-consistent sigma found. FAIL if no fixed point. INFO if multiple.

**Input files**: `tier0-computation/s44_dimflow.npz`, `tier0-computation/s42_constants_snapshot.npz`
**Output files**: Script `tier0-computation/s45_sigma_select.py`
**Working paper section**: W2-4

---

## III-c. Wave 3: HIGH/MEDIUM (4 tasks)

### W3-1: M_KK Tension Resolution (MKK-TENSION-45)

**Agent**: `baptista-spacetime-analyst` (primary), `connes-ncg-theorist` (NCG cross-check)
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

S44 W7-1 confirmed the M_KK tension (0.83 decades between gravity and gauge routes) is real and Vol-independent. The S44 team-lead audit found Vol(SU(3)) = 1349.7 (not 8880.9), potentially resolving the tension to 0.013 decades. This result is PROVISIONAL (Sagan Section 6B). You are performing the definitive audit.

Computation:
1. Derive Vol(SU(3)) from the bi-invariant (round) metric analytically. Use the Macdonald formula Vol(SU(n)) = sqrt(n) * (2 pi)^{n(n+1)/2} / prod_{k=1}^{n-1} k!
2. Trace exactly where Vol(SU(3)) enters the Kerner formula for gauge coupling extraction
3. Recompute M_KK from both routes with the correct volume
4. Compute KK threshold corrections to alpha_EM at M_KK
5. Test Baptista hypercharge normalization variants (Paper 14 factor 3 vs SU(5) 5/3)

**Gate MKK-TENSION-45**: PASS if tension narrows to < 0.2 decades. FAIL if structural and irreducible. INFO if partially resolved.

**Input files**: `tier0-computation/s44_mkk_reconcile.npz`, `tier0-computation/s44_constants_corrected.npz`, `tier0-computation/s42_constants_snapshot.npz`
**Output files**: Script `tier0-computation/s45_mkk_tension.py`, Data `tier0-computation/s45_mkk_tension.npz`
**Working paper section**: W3-1

---

### W3-2: E_cond Reconciliation (ECOND-RECONCILE-45)

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**:

S44 data provenance found E_cond = 0.115 M_KK (s42_hauser_feshbach, hardcoded) vs 0.137 M_KK (s37 ED, 256-state Fock space, machine epsilon). The s37 value is more authoritative (full exact diagonalization vs approximate). Determine the authoritative value and rerun the 6 downstream scripts that depend on E_cond.

Steps:
1. Load s37_pair_susceptibility.npz and s42_hauser_feshbach.npz, extract E_cond from each
2. Identify the computation method behind each value (BCS mean-field vs exact diagonalization)
3. Declare the authoritative value with justification
4. Rerun: s38_cc_instanton, s42_gge_energy, s44_tracelog_cc, s44_dm_de_ratio, s44_multi_t_jacobson, s44_cc_gap_audit
5. Report which results change by > 5%

**Gate ECOND-RECONCILE-45**: INFO (determine authoritative value, quantify downstream impact).

**Input files**: `tier0-computation/s37_pair_susceptibility.npz`, `tier0-computation/s42_hauser_feshbach.npz`
**Output files**: Script `tier0-computation/s45_econd_reconcile.py`, Data `tier0-computation/s45_econd_reconcile.npz`
**Working paper section**: W3-2

---

### W3-3: Debye-Waller Factor for Spectral Action (DEBYE-WALLER-45)

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**:

The Debye-Waller factor exp(-2W) suppresses coherent scattering in crystals. On SU(3), the phonon spectrum (S44 W5-3: gap stable, bandwidth +28%) provides a DW factor for the spectral action eigenvalues. If 2W ~ O(1), the spectral action receives significant thermal corrections. Compute this.

Steps:
1. Load DOS from `tier0-computation/s44_dos_tau.npz`
2. Compute the mean-square displacement <u^2> from the phonon DOS using standard Debye theory
3. Evaluate 2W = <u^2> * (2 pi / d)^2 where d is the nearest-neighbor distance on SU(3)
4. Compute exp(-2W) and report whether the DW correction is percent-level or larger
5. If 2W ~ O(1), compute the corrected spectral action S_DW(tau) = sum_k d_k f(lambda_k^2/Lambda^2) * exp(-2W_k)

**Gate DEBYE-WALLER-45**: INFO (diagnostic, whether DW factor modifies spectral action at percent level).

**Input files**: `tier0-computation/s44_dos_tau.npz`, `tier0-computation/s42_hauser_feshbach.npz`
**Output files**: Script `tier0-computation/s45_debye_waller.py`, Data `tier0-computation/s45_debye_waller.npz`
**Working paper section**: W3-3

---

### W3-4: Linearized Friedmann-Modulus QNM Spectrum (QNM-NS-45)

**Agent**: `schwarzschild-penrose-theorist` (primary), `connes-ncg-theorist` (cross-check)
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

S44 SP collab proposed linearizing the coupled Friedmann-modulus system to extract quasi-normal mode (QNM) frequencies. The QNM spectrum determines the perturbation decay rate and can contribute to n_s through mode-dependent damping. SP's naive test found sigma=591 (not 1.10), so the QNM route needs careful construction.

Steps:
1. Linearize the coupled system {H(t), tau(t)} around the transit trajectory
2. Compute the QNM spectrum omega_QNM from the linearized equations
3. Extract the effective n_s from QNM-dependent damping: n_s - 1 ~ -2 Im(omega_QNM) / Re(omega_QNM)
4. Compare to the Bogoliubov n_s from W1-2

**Gate QNM-NS-45**: INFO (diagnostic, comparing QNM route to Bogoliubov route).

**Input files**: `tier0-computation/s44_friedmann_bcs_audit.npz`, `tier0-computation/s44_dimflow.npz`
**Output files**: Script `tier0-computation/s45_qnm_ns.py`, Data `tier0-computation/s45_qnm_ns.npz`
**Working paper section**: W3-4

---

## III-d. Wave 4: MEDIUM (4 tasks, diagnostics + infrastructure)

### W4-1: Data Provenance Complete Audit (DATA-PROVENANCE-45)

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: LOW

**Prompt**:

Complete the upstream audit of all tier0 .npz files for consistency. The S44 parallel audit found 3 issues (Vol(SU(3)) 3 values, E_cond 2 values, stale M_KK). Complete the S7-S24 foundational script audit. Produce a CANONICAL CONSTANTS FILE imported by all future scripts.

Steps:
1. Catalog every .npz file in tier0-computation/ with creation date and key quantities stored
2. Cross-check: every file that stores M_KK, E_cond, Vol_SU3, Delta_0, mu must agree with the authoritative values
3. Flag any inconsistencies with file path, stored value, and authoritative value
4. Write `tier0-computation/s45_canonical_constants.py` that defines ALL authoritative constants in one place
5. Verify the authoritative values: M_KK (gravity route), E_cond (from ECOND-RECONCILE-45), Vol(SU(3)) (from MKK-TENSION-45), Delta_0 (from s38), mu=0 (from S34 theorem)

**Gate DATA-PROVENANCE-45**: INFO (audit, produce canonical constants file).

**Output files**: `tier0-computation/s45_canonical_constants.py`, `tier0-computation/s45_data_provenance_audit.md`
**Working paper section**: W4-1

---

### W4-2: Kretschner Scalar on M^4 x SU(3) (KRETSCHNER-12D-45)

**Agent**: `schwarzschild-penrose-theorist` (primary), `connes-ncg-theorist` (cross-check)
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Compute the Kretschner scalar K = R_{abcd}R^{abcd} on the full 12D manifold M^4 x SU(3) at the fold metric, as proposed in the Connes-SP joint workshop (S44 collab R2). This is a geometric diagnostic: K measures the curvature complexity of the internal space.

Steps:
1. Construct the 12D metric: ds^2 = g_{mu nu}^{(4)} dx^mu dx^nu + g_{ab}^{SU(3)}(tau) dy^a dy^b
2. Compute the Riemann tensor R^{a}_{bcd} on SU(3) at tau_fold = 0.190 using the Jensen-deformed metric
3. Contract: K_internal = R_{abcd}R^{abcd} on SU(3)
4. For the full 12D: K_total = K_4D + K_internal + K_mixed (cross terms)
5. Report K_internal / K_4D ratio and K at round vs fold

**Gate KRETSCHNER-12D-45**: INFO (geometric diagnostic).

**Input files**: `tier0-computation/s42_hauser_feshbach.npz` (metric data)
**Output files**: Script `tier0-computation/s45_kretschner.py`, Data `tier0-computation/s45_kretschner.npz`
**Working paper section**: W4-2

---

### W4-3: Van Hove Fine Scan at tau = 0.19-0.21 (DOS-FINE-SCAN-45)

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

S44 W6-8 found a near-crossing at tau=0.19: trajectories T3, T4, T5 approach within delta=0.0008. This near-crossing is critical for OCC-SPEC-45 (it determines whether the van Hove enhancement is sufficient to create a turning point in S_occ). Perform a fine scan at 20 tau values in [0.19, 0.21].

Steps:
1. Compute eigenvalues at 20 tau values: 0.190, 0.191, ..., 0.209
2. Track the 12 van Hove trajectories from S44 W6-8 with fine resolution
3. Determine: do T3, T4, T5 CROSS or merely approach?
4. If they cross: identify the crossing topology (avoided crossing, true crossing, triple point)
5. Compute the DOS at each tau value, focusing on the gap-edge structure

**Gate DOS-FINE-SCAN-45**: INFO (diagnostic feeding OCC-SPEC interpretation).

**Input files**: `tier0-computation/s44_vanhove_track.npz`, `tier0-computation/tier1_dirac_spectrum.py`
**Output files**: Script `tier0-computation/s45_dos_fine_scan.py`, Data `tier0-computation/s45_dos_fine_scan.npz`, Plot `tier0-computation/s45_dos_fine_scan.png`
**Working paper section**: W4-3

---

### W4-4: Euler Deficit Identity Proof (EULER-DEFICIT-45)

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**:

S44 W6-5 (MULTI-T-JACOBSON-44) found the Euler deficit = |E_cond| = 6.8% (new identity connecting GGE non-thermality to BCS order). Volovik S44 collab proposed proving the exact identity:

    E = sum_k T_k S_k - PV + sum_k mu_k N_k + |E_cond|

where the sum runs over the 8 sectors, T_k and S_k are the sector temperatures and entropies, P is the pressure, V is the volume, mu_k are the chemical potentials, and |E_cond| is the BCS condensation energy.

Steps:
1. Start from the standard Euler relation E = TS - PV + mu N
2. Generalize to the 8-temperature GGE: replace T S -> sum_k T_k S_k
3. Show that the residual |E_cond| arises from the non-equilibrium character of the GGE
4. Verify numerically using S44 W6-5 data
5. Prove or disprove: is this exact, or does it have corrections?

**Gate EULER-DEFICIT-45**: INFO (structural result, connects to CC through vacuum energy accounting).

**Input files**: `tier0-computation/s44_multi_t_jacobson.npz`, `tier0-computation/s42_gge_energy.npz`
**Output files**: Script `tier0-computation/s45_euler_deficit.py`
**Working paper section**: W4-4

---

## III-e. Wave 5: SPECIALIST (5 tasks)

### W5-1: Sakharov UV Cutoff and Dissolution Scale (SAKHAROV-UV-DISSOLUTION-45)

**Agent**: `quantum-foam-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**:

S44 W1-1 (corrected) found Lambda_eff ~ 10 x M_KK. S44 W6-7 found epsilon_c ~ 1/sqrt(N). Is there a relationship? At N ~ (Lambda_eff/M_KK)^8 = 10^8, the dissolution scale epsilon_c ~ 10^{-4}. Does this match the foam strength? Compute and report.

**Gate SAKHAROV-UV-DISSOLUTION-45**: INFO (link between UV physics and emergence).

**Input files**: `tier0-computation/s44_sakharov_gn_audit.npz`, `tier0-computation/s44_dissolution_scaling.npz`
**Output files**: Script `tier0-computation/s45_sakharov_dissolution.py`
**Working paper section**: W5-1

---

### W5-2: Cyclic Cohomology for Occupied-State Triple (OCCUPIED-CYCLIC-45)

**Agent**: `connes-ncg-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

The occupied-state spectral action (Paper 16) defines a modified spectral triple. Compute the Connes-Chern character and verify the cyclic cohomology pairing is nondegenerate. This is the mathematical foundation for OCC-SPEC-45 — if the cyclic cohomology pairing is degenerate, the occupied-state spectral action may not be physically meaningful.

**Gate OCCUPIED-CYCLIC-45**: INFO (mathematical foundation for OCC-SPEC).

**Input files**: `researchers/Connes/16_2022_Dong_Khalkhali_van_Suijlekom_Second_quantization_spectral_action.md`
**Output files**: Script `tier0-computation/s45_occupied_cyclic.py`
**Working paper section**: W5-2

---

### W5-3: Ginzburg-Landau Free Energy Landscape (GL-GGE-STABILITY-45)

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Construct the GL free energy F(T_1, ..., T_8) on the 8-temperature GGE manifold. S44 W6-5 found 3/8 heat capacity eigenvalues negative (saddle directions). Map the free energy landscape: where are the minima, saddle points, and barriers?

**Gate GL-GGE-STABILITY-45**: INFO (landscape topology for DM/DE and stability analysis).

**Input files**: `tier0-computation/s44_multi_t_jacobson.npz`, `tier0-computation/s42_gge_energy.npz`
**Output files**: Script `tier0-computation/s45_gl_gge.py`, Data `tier0-computation/s45_gl_gge.npz`
**Working paper section**: W5-3

---

### W5-4: Running Sakharov G_N(tau) (RUNNING-GN-45)

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

S44 W1-1 computed G_N^{Sakharov} at the fold. Compute G_N(tau) across the full transit (tau = 0.00 to 0.50 at 20 points) using the Sakharov formula. Report how G_N evolves during the transit and whether it is monotone.

**Gate RUNNING-GN-45**: INFO (diagnostic, tau-dependence of gravitational coupling).

**Input files**: `tier0-computation/s44_sakharov_gn_audit.npz`, `tier0-computation/s41_spectral_refinement.npz`
**Output files**: Script `tier0-computation/s45_running_gn.py`, Data `tier0-computation/s45_running_gn.npz`, Plot `tier0-computation/s45_running_gn.png`
**Working paper section**: W5-4

---

### W5-5: Weak Order-One Condition (WEAK-ORDER-ONE-45)

**Agent**: `connes-ncg-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**:

Test the weak order-one condition from Connes Paper 25 on the framework's spectral triple at the fold. The order-one condition [[D, a], b^0] = 0 constrains the Dirac operator. The WEAK version allows deviations controlled by the inner fluctuations. Report whether the framework satisfies the weak condition and what the deviation measures.

**Gate WEAK-ORDER-ONE-45**: INFO (structural condition on the spectral triple).

**Input files**: `tier0-computation/s42_hauser_feshbach.npz`, `researchers/Connes/25_2023_Connes_Spectral_Action_Weak_Order_One.md` (if available)
**Output files**: Script `tier0-computation/s45_weak_order_one.py`
**Working paper section**: W5-5

---

## III-f. Wave 6: SPECIALIST continued (6 tasks)

### W6-1: q-Theory vs Spectral Action Bayes Factor (BAYESIAN-MODEL-45)

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus
**Cost**: LOW

Compute the Bayes factor between q-theory and spectral action for the CC, using the S44 data (G_N agreement, CC gap, trace-log suppression). Which framework better accounts for the observed CC?

**Gate BAYESIAN-MODEL-45**: INFO (model comparison).

**Output files**: Script `tier0-computation/s45_bayesian_model.py`
**Working paper section**: W6-1

---

### W6-2: Phononic Casimir Force Between Domain Walls (ACOUSTIC-CASIMIR-45)

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: MEDIUM

Compute the phononic Casimir force between KZ domain walls in the internal space. S44 W3-2 (COHERENT-WALL-44) found per-wall reflectivity |r| = 0.003-0.009 (acoustically transparent). The Casimir force from the phonon spectrum with boundary conditions at the walls may provide a long-range inter-domain interaction.

**Gate ACOUSTIC-CASIMIR-45**: INFO (acoustic interaction between domains).

**Input files**: `tier0-computation/s44_coherent_wall.npz`, `tier0-computation/s44_dos_tau.npz`
**Output files**: Script `tier0-computation/s45_acoustic_casimir.py`
**Working paper section**: W6-2

---

### W6-3: Peter-Weyl Censorship at 1/sqrt(N) (PETER-WEYL-CENSORSHIP-45)

**Agent**: `schwarzschild-penrose-theorist`
**Model**: opus
**Cost**: LOW

S44 W2-3 (EIH-GRAV-44) found S_singlet/S_fold = 5.684e-5 (17,594x suppression). S44 W6-7 found epsilon_c ~ 1/sqrt(N). At finite N (truncation), the Peter-Weyl block-diagonality is approximate. Compute the non-singlet leakage rate at 1/sqrt(N) and whether the 17,594x suppression survives.

**Gate PETER-WEYL-CENSORSHIP-45**: INFO (robustness of EIH singlet projection).

**Input files**: `tier0-computation/s44_eih_grav.npz`, `tier0-computation/s44_dissolution_scaling.npz`
**Output files**: Script `tier0-computation/s45_peter_weyl_censorship.py`
**Working paper section**: W6-3

---

### W6-4: GGE Beat Frequencies (GGE-BEATING-45)

**Agent**: `tesla-resonance-specialist`
**Model**: opus
**Cost**: LOW

Compute the autocorrelation function C(t) = <O(t) O(0)>_GGE from the 8 GGE modes. The beat frequencies between the 8 Richardson-Gaudin modes produce observable temporal structure. Report the dominant beat periods and their amplitudes.

**Gate GGE-BEATING-45**: INFO (GGE temporal structure).

**Input files**: `tier0-computation/s44_multi_t_jacobson.npz`, `tier0-computation/s42_gge_energy.npz`
**Output files**: Script `tier0-computation/s45_gge_beating.py`
**Working paper section**: W6-4

---

### W6-5: Two-Fluid Landau-Khalatnikov Cosmology -> DESI w(z) (TWO-FLUID-DESI-45)

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM

Map the two-fluid (superfluid + normal) post-transit state to an effective w(z) equation of state. Compare to DESI DR1 w(z) data. S42 tessellation-lensing-bias hypothesis: DESI w != -1 may be lensing bias from 32-cell tessellation, not real dynamical DE. Test whether the two-fluid model reproduces the DESI signal OR the lensing bias.

**Gate TWO-FLUID-DESI-45**: INFO (w(z) prediction for DESI comparison).

**Input files**: `tier0-computation/s44_dm_de_ratio.npz`, `tier0-computation/s42_constants_snapshot.npz`
**Output files**: Script `tier0-computation/s45_two_fluid_desi.py`, Data `tier0-computation/s45_two_fluid_desi.npz`
**Working paper section**: W6-5

---

### W6-6: Spectral Penrose Diagram (SPECTRAL-PENROSE-45)

**Agent**: `schwarzschild-penrose-theorist`
**Model**: opus
**Cost**: LOW

Construct the spectral Penrose diagram in the (tau, lambda_k) plane, colored by Bogoliubov occupation number n_k. This is the visualization proposed in the Connes-SP joint workshop R2, replacing the (rejected) 10D Penrose diagram. The diagram should show: eigenvalue trajectories, van Hove singularities, BCS gap, and particle creation intensity.

**Gate SPECTRAL-PENROSE-45**: INFO (visualization).

**Input files**: `tier0-computation/s41_spectral_refinement.npz`, `tier0-computation/s44_vanhove_track.npz`, `tier0-computation/s42_hauser_feshbach.npz`
**Output files**: Script `tier0-computation/s45_spectral_penrose.py`, Plot `tier0-computation/s45_spectral_penrose.png`
**Working paper section**: W6-6

### W6-7: Dissolution Entanglement Entropy (DISSOLUTION-ENTROPY-45)

**Agent**: `quantum-foam-theorist`
**Model**: opus
**Cost**: MEDIUM

Compute the entanglement entropy across the Poisson → GOE level statistics transition as a function of perturbation strength epsilon. S44 W6-7 characterized the dissolution by epsilon_c ~ N^{-0.457} (crossover in <r> statistic). The entanglement entropy provides a complementary characterization: how much quantum information is shared between blocks as the block-diagonal structure fragments?

**Method**:
1. Load eigenvalue data from `tier0-computation/s42_hauser_feshbach.npz` and dissolution data from `tier0-computation/s44_dissolution_scaling.npz`.
2. For each truncation level (max_pq_sum = 1 through 5), construct the block-diagonal D_K and add random perturbation of strength epsilon.
3. Partition the Hilbert space into blocks. Compute the reduced density matrix rho_A = Tr_B(|psi><psi|) for the ground state of the perturbed Hamiltonian.
4. Compute S_ent(epsilon) = -Tr(rho_A ln rho_A) at 20 epsilon values from 0 to 10*epsilon_c.
5. Track S_ent(epsilon_c) vs N. Does it scale as ln(N) (area law), N^alpha (volume law), or constant?
6. Report the universality class of the dissolution transition from the entanglement perspective.

**Formula audit**: (a) S_ent = -Tr(rho ln rho) in nats. (b) Dimensional check: S_ent is dimensionless. (c) Limiting case: S_ent = 0 at epsilon = 0 (product state). (d) Reference: Page (1993) for random state entanglement.

**Gate DISSOLUTION-ENTROPY-45**: INFO (entanglement characterization of dissolution).

**Input files**: `tier0-computation/s42_hauser_feshbach.npz`, `tier0-computation/s44_dissolution_scaling.npz`
**Output files**: Script `tier0-computation/s45_dissolution_entropy.py`, Data `.npz`, Plot `.png`
**Working paper section**: W6-7

---

## III-g. Wave 7: Reconciliation (3 tasks)

### W7-1: Formula Audit Report (FORMULA-AUDIT-REPORT)

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: ZERO

Compile the formula audit results from ALL S45 computations. For each computation that ran, verify: (a) formula stated with units, (b) dimensional check passed, (c) at least one limiting case verified, (d) original derivation cited. Report any violations.

**Gate FORMULA-AUDIT-REPORT**: META (process quality).

**Output files**: `sessions/session-45/s45_formula_audit.md`
**Working paper section**: W7-1

---

### W7-2: CC Gap Update (CC-GAP-UPDATE-45)

**Agent**: `einstein-theorist`
**Model**: opus
**Cost**: LOW

Update the CC gap calculation from S44's 110.5 orders, incorporating: analytic torsion (W2-1), q-theory (W2-3), any new suppressions identified in W1-W6. Report the new honest gap.

**Gate CC-GAP-UPDATE-45**: INFO (updated CC accounting).

**Input files**: All s45_*.npz CC-related
**Output files**: Script `tier0-computation/s45_cc_gap_update.py`
**Working paper section**: W7-2

---

### W7-3: Constraint Map Update (CONSTRAINT-MAP-45)

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: ZERO

Update the full constraint surface: new walls, new gate verdicts, new closures, surviving regions. This feeds into the Sagan assessment.

**Gate CONSTRAINT-MAP-45**: META (bookkeeping).

**Output files**: Section in working paper
**Working paper section**: W7-3

---

## III-h. Wave 8: Assessment (1 task, runs LAST)

### W8-1: Sagan Assessment and Probability Update

**Agent**: `sagan-empiricist`
**Model**: opus
**Cost**: ZERO

**Prompt**:

Evaluate ALL Session 45 results (W1 through W7) against pre-registered gates. Issue probability update from 23% prior (68% CI 15-32%, S44).

This runs LAST so Sagan has access to all computation results from all 7 waves.

**Context.** S44 Sagan assessment: P = 23% (68% CI 15-32%). BF = 2.18. The make-or-break computation is KZ-NS-45. PASS -> P > 50%. FAIL -> P ~ 8%. OCC-SPEC-45 PASS alone -> P = 35-45%.

**Assessment Protocol**:

1. **Gate audit.** For each pre-registered gate in S45, record: Gate ID, criterion, result, verdict.

2. **OCC-SPEC assessment.** Did the occupied-state spectral action find a minimum? If PASS: is it deep enough for dynamical trapping? Is tau_min near tau_fold? If FAIL: is the 6th monotonicity confirmation definitive? Is spectral action exhausted for tau-stab?

3. **KZ-NS assessment.** Did the Bogoliubov spectrum give n_s in [0.955, 0.975]? If PASS: is this a genuine prediction or was k-mapping tuned? Sensitivity analysis: how much does n_s change with Delta_0, tau_fold, quench profile? If FAIL: is the Landau adversarial prediction confirmed? What n_s was obtained and why?

4. **CC assessment.** Updated gap from W7-2. Did analytic torsion or q-theory contribute new suppression?

5. **DM/DE assessment.** Did alpha_eff match 0.39? Was the factor 2.7 resolved?

6. **Adversarial tests.** Apply maximum adversarial pressure to the best results. Are there hidden assumptions, tuned parameters, or correlated errors?

7. **Probability update.** Prior = 23%. Gate-by-gate Bayes factors. Combined BF. Posterior. Evidence level.

8. **Structural content.** Update P(structural content). New theorems, closures, permanent results.

9. **S46 recommendations.** Ranked by diagnostic power. Pre-registerable gates specified.

**Pre-registered gate SAGAN-45**: META (probability update, not PASS/FAIL).

**Critical notes**:
- Read ALL W1-W7 results before writing. Do not assess results you have not read.
- The assessment must be ADVERSARIAL. If a result looks too good, interrogate it harder.
- Do not state probabilities without showing the Bayesian calculation.
- The constraint map IS the assessment.
- Distinguish structural constraints from framework-specific results.
- No filler, no enthusiasm, no discouragement. Just the physics.
- The Venus standard: has ANY computation produced a prediction that could be tested by independent observation? If so, how?

**Output**: `sessions/session-45/s45_sagan_assessment.md`

---

## IV. Key Numbers (Reference Table for All Agents)

| Quantity | Value | Source |
|:---------|:------|:------|
| S_fold | 250,361 M_KK^4 | s36 |
| S(0) | 244,839 M_KK^4 | s36 |
| Delta_S | 5,522 M_KK^4 | s36 |
| M_KK (gravity) | 7.4e16 GeV | s42 |
| M_KK (gauge) | 5.0e17 GeV (or 7.66e16 if Vol corrected) | s42 / s44 audit |
| M_KK (Bayesian mode) | 3.1e17 GeV | s43 |
| E_exc (GGE) | 50.9 M_KK (or 60.7 if E_cond = 0.137) | s42 / s44 |
| n_pairs | 59.8 | s38 |
| Z_fold | 74,731 | s42 |
| E_cond | -0.115 M_KK (s42) or -0.137 M_KK (s37 ED) | RECONCILE in W3-2 |
| Spectral gap | 0.819 M_KK | s36 |
| B2 bandwidth | 0 (exact, Schur) | s43 |
| u_2 (second sound) | c/sqrt(3) | s43 |
| epsilon_H | 2.999 (INVARIANT, theorem) | s44 W4-3 |
| r (tensor-to-scalar) | 3.86e-10 | s44 W3-4 |
| G_N^{Sak} / G_N^{obs} | 2.29 at Lambda = 10 M_KK | s44 W1-1 (corrected) |
| a_2^bos / a_2^Dirac | 61/20 = 3.05 (EXACT) | s44 W4-2 |
| T^{0i}_4D (GGE) | 0 (CDM by construction) | s44 W1-2 |
| CC gap (honest) | 110.5 orders | s44 W7-2 |
| DM/DE ratio (best) | 1.06 (2.7x observed) | s44 W6-4 |
| GGE T_max/T_min | 3.755 | s43 |
| 3/8 negative heat capacity eigenvalues | -4.51, -1.60, -0.68 | s44 W6-5 |
| Van Hove near-crossing (T3-T5) | delta = 0.0008 at tau = 0.19 | s44 W6-8 |
| prior probability | 23% (68% CI 15-32%) | s44 Sagan |

---

## V. Agent-Model Assignments

All physics agents use **opus**. Only the knowledge-weaver (if spawned for index rebuild) uses sonnet.

| Agent | Waves | Tasks |
|:------|:------|:------|
| connes-ncg-theorist | W1, W2, W3, W5 | OCC-SPEC (lead), ANALYTIC-TORSION, SIGMA-SELECT (if needed), OCCUPIED-CYCLIC, WEAK-ORDER-ONE |
| volovik-superfluid-universe-theorist | W1, W2, W4, W5, W6 | KZ-NS (lead), ALPHA-EFF, Q-THEORY-KK, EULER-DEFICIT, RUNNING-GN, TWO-FLUID-DESI |
| nazarewicz-nuclear-structure-theorist | W1, W3, W6 | OCC-SPEC (cross-check), ECOND-RECONCILE, BAYESIAN-MODEL |
| einstein-theorist | W1, W7 | KZ-NS (cross-check), CC-GAP-UPDATE |
| landau-condensed-matter-theorist | W2, W5 | LK-RELAX (if OCC-SPEC PASS), ALPHA-EFF (cross-check), GL-GGE-STABILITY |
| baptista-spacetime-analyst | W3 | MKK-TENSION |
| schwarzschild-penrose-theorist | W3, W4, W6 | QNM-NS, KRETSCHNER-12D, PETER-WEYL-CENSORSHIP, SPECTRAL-PENROSE |
| quantum-acoustics-theorist | W3, W4, W6 | DEBYE-WALLER, DOS-FINE-SCAN, ACOUSTIC-CASIMIR |
| hawking-theorist | W2 | Q-THEORY-KK (cross-check) |
| quantum-foam-theorist | W5 | SAKHAROV-UV-DISSOLUTION |
| tesla-resonance-specialist | W6 | GGE-BEATING |
| gen-physicist | W4, W7 | DATA-PROVENANCE, FORMULA-AUDIT-REPORT, CONSTRAINT-MAP |
| sagan-empiricist | W8 | Assessment |

---

## VI. Formula Audit Protocol (S45 Mandatory)

S44 had 3 formula errors (Sakharov normalization, Stieltjes ordering, Vol(SU(3))). All shared the same signature: correct arithmetic, wrong formula provenance. The pipeline verifies numbers to machine precision while failing to independently derive the connecting formulas.

**Every S45 computation must include** (4/7 collab convergence):

1. **State formula with units** before computing. Write the formula in LaTeX notation with explicit dimensions on every quantity.
2. **Dimensional check.** Verify the formula is dimensionally consistent. Report the dimensions of each factor.
3. **At least one limiting case.** Identify a regime where the formula reduces to a known result. Compute both and verify agreement.
4. **Cite original derivation.** Reference the paper, textbook, or prior session computation where the formula was derived. If the formula is new, provide the derivation.

Violations of this protocol should be flagged in the formula audit report (W7-1).

---

## VII. Global Rules

1. **ALL physics agents use opus.** Sonnet only for knowledge-weaver bookkeeping.
2. **Script prefix**: `s45_`
3. **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
4. **Output directory**: `tier0-computation/`
5. **Gate IDs**: as specified in each wave prompt. No collisions with S44 IDs (all S44 gates end in `-44`).
6. **Working paper**: `sessions/session-45/session-45-results-workingpaper.md`
7. **One writer per output file.** Other agents contribute via SendMessage.
8. **Pre-register gates BEFORE computation.** Define pass/fail, then compute.
9. **Negative results are boundaries, not failures.** They constrain the solution space.
10. **Path quoting**: ALL bash paths containing "Ainulindale Exflation" must be double-quoted.
11. **Formula audit protocol**: mandatory for all computations (Section VI).
12. **Decision points**: Wave 2 configuration depends on Wave 1 verdicts (Section II).

---

## VIII. Constraint Gate Summary

### Pre-Registered Gates (S45)

| Gate ID | Agent | Criterion (PASS) | Criterion (FAIL) |
|:--------|:------|:-----------------|:-----------------|
| OCC-SPEC-45 | connes (lead), naz (cross) | Local min in [0.10, 0.25], barrier > 1% | Monotone at all Lambda, tau in [0.00, 0.50] |
| KZ-NS-45 | volovik (lead), einstein (cross) | n_s in [0.955, 0.975] | n_s outside [0.80, 1.10] |
| ANALYTIC-TORSION-45 | connes, naz | log10(T) < -50 | T = O(1) |
| ALPHA-EFF-45 | volovik, landau | alpha_eff in [0.3, 0.5] | alpha_eff > 2.0 |
| Q-THEORY-KK-45 | volovik, hawking | Zero-crossing at tau in [0.10, 0.25] | No crossing in [0.00, 0.50] |
| MKK-TENSION-45 | baptista, connes | Tension < 0.2 decades | Structural, irreducible |
| LK-RELAX-45 (conditional) | landau | N_e > 10 during dwell | N_e < 0.1 |
| SIGMA-SELECT-45 (conditional) | connes, hawking | Self-consistent sigma found | No fixed point |

### INFO Gates (S45)

| Gate ID | Agent | Purpose |
|:--------|:------|:--------|
| ECOND-RECONCILE-45 | nazarewicz | Authoritative E_cond + downstream |
| DATA-PROVENANCE-45 | gen-physicist | Canonical constants file |
| DEBYE-WALLER-45 | quantum-acoustics | Thermal correction diagnostic |
| QNM-NS-45 | SP, connes | QNM comparison to Bogoliubov |
| KRETSCHNER-12D-45 | SP, connes | Curvature diagnostic |
| DOS-FINE-SCAN-45 | quantum-acoustics | T3-T5 crossing topology |
| EULER-DEFICIT-45 | volovik | GGE thermodynamic identity |
| SAKHAROV-UV-DISSOLUTION-45 | quantum-foam | UV/emergence link |
| OCCUPIED-CYCLIC-45 | connes | Mathematical foundation for OCC-SPEC |
| GL-GGE-STABILITY-45 | landau | Free energy landscape |
| RUNNING-GN-45 | volovik | G_N(tau) evolution |
| WEAK-ORDER-ONE-45 | connes | Spectral triple condition |
| BAYESIAN-MODEL-45 | nazarewicz | Model comparison |
| ACOUSTIC-CASIMIR-45 | quantum-acoustics | Inter-domain interaction |
| PETER-WEYL-CENSORSHIP-45 | SP | EIH robustness |
| GGE-BEATING-45 | tesla | Temporal structure |
| TWO-FLUID-DESI-45 | volovik | w(z) prediction |
| SPECTRAL-PENROSE-45 | SP | Visualization |
| CC-GAP-UPDATE-45 | einstein | Updated CC accounting |

---

## IX. Bundle Coverage

The S45 investigation bundle (S44 quicklook lines 349-441) listed 42 distinct suggestions in 6 convergence clusters, plus 11 newly identified from collab reviews. This plan covers 29 computations + 1 Sagan assessment = 30 tasks.

### Covered (29 computations)

Both CRITICAL items: OCC-SPEC-45, KZ-NS-45.

All 3 HIGH items: ANALYTIC-TORSION-45, ALPHA-EFF-45, Q-THEORY-KK-45.

Both conditional HIGH items: LK-RELAX-45 (if OCC-SPEC PASS), SIGMA-SELECT-45 (if KZ-NS FAIL).

6 of 8 MEDIUM items: MKK-TENSION-45, ECOND-RECONCILE-45, DATA-PROVENANCE-45, DEBYE-WALLER-45, QNM-NS-45, KRETSCHNER-12D-45.

10 SPECIALIST items: DOS-FINE-SCAN-45, EULER-DEFICIT-45, SAKHAROV-UV-DISSOLUTION-45, OCCUPIED-CYCLIC-45, GL-GGE-STABILITY-45, RUNNING-GN-45, WEAK-ORDER-ONE-45, BAYESIAN-MODEL-45, ACOUSTIC-CASIMIR-45, PETER-WEYL-CENSORSHIP-45.

6 additional from collab reviews: GGE-BEATING-45, TWO-FLUID-DESI-45, SPECTRAL-PENROSE-45, FORMULA-AUDIT-REPORT, CC-GAP-UPDATE-45, CONSTRAINT-MAP-45.

### Omitted (5 suggestions) with reasons

| ID | What | Why omitted |
|:---|:-----|:------------|
| PHONON-GREENS-45 | Full propagator G(omega, (p,q), (p',q')) | HIGH cost, LOW diagnostic value relative to OCC-SPEC which already probes the occupied-state physics. Defer to S46 if OCC-SPEC opens a new direction. |
| FULL-HFB-LOOP-45 | Self-consistent HFB: D_K -> BCS -> BdG -> tau* | Deferred since S41. The full self-consistent loop requires OCC-SPEC to first establish whether S_occ has a minimum. If OCC-SPEC PASS, this becomes S46 priority. |
| ~~DISSOLUTION-ENTROPY-45~~ | ~~Entanglement entropy across Poisson -> GOE~~ | MOVED to W6-7 (user request). |
| QUASIPARTICLE-LIFETIME-45 | Integrability-breaking lifetime | LOW priority (Landau suggestion). The GGE has infinite quasiparticle lifetime by integrability. Breaking integrability requires going beyond the exactly solvable model, which is a different computation. |
| BRANCH-DM-DE-45 | Branch-resolved DM/DE from acoustic branch counting | MEDIUM (Tesla suggestion). Subsumed by ALPHA-EFF-45 which computes the full non-equilibrium DM/DE from the 8-temperature GGE, which already includes branch structure. |

### Subsumed

| Bundle ID | Subsumed by | Reason |
|:----------|:-----------|:-------|
| FORMULA-AUDIT-PROTOCOL | Built into every computation + W7-1 | The protocol is now mandatory (Section VI), not a standalone computation. |
| VOL-AUDIT-45 (Sagan rec. #2) | MKK-TENSION-45 | The Vol(SU(3)) analytic verification is the first step of MKK-TENSION-45. |

---

## X. Probability Decision Matrix

Summary of how S45 outcomes map to probability updates, from S44 Sagan assessment and S45 prereg.

| Outcome | BF | P_post (from 23% prior) |
|:--------|:---|:------------------------|
| OCC-SPEC PASS + KZ-NS PASS | 50-100 | **60-75%** |
| KZ-NS PASS alone | 10-20 | **50-65%** |
| OCC-SPEC PASS + KZ-NS INFO | 5-10 | **40-55%** |
| OCC-SPEC PASS alone | 3-5 | **35-45%** |
| Both INFO (n_s in extended window, shallow minimum) | 1.5-3 | **28-40%** |
| Both FAIL | 0.1-0.3 | **3-8%** |
| KZ-NS FAIL + OCC-SPEC FAIL + ALPHA-EFF PASS | 0.5 | **12-15%** |
| KZ-NS FAIL + OCC-SPEC PASS + ANALYTIC-TORSION PASS | 5-8 | **40-55%** |

The session is existentially decisive. The range of possible posteriors spans 3% to 75%.
