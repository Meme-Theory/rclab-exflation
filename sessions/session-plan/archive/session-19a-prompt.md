# Session 19a: Spectral Complexity Diagnostics — Is the Vacuum a Phase?

## Session Type: Computation from Existing Data (HOURS)
## Agents: phonon-exflation-sim + tesla-resonance
## Session Goal: Compute 5 spectral diagnostics from existing eigenvalue data. Binary closure/confirm of the spectral complexity hypothesis in a single session.

---

# I. CONTEXT

Eighteen sessions established an extraordinary algebraic skeleton: KO-dimension 6, SM quantum numbers, chirality, Jensen geometry, gauge structure, 67 verification checks at machine epsilon, zero contradictions.

Session 18 delivered the decisive V_eff result:

> **V_eff(tau) is monotonically decreasing for all tau > 0.**

The 1-loop Coleman-Weinberg effective potential has NO minimum. Fermionic DOF (439,488) overwhelm bosonic (52,556) at every tau, ratio 8.4:1. Three independent computations confirm to 4 significant figures. 1-loop CW stabilization is CLOSED.

**The spectral complexity hypothesis** (Session 19 Primer): The vacuum is NOT a point in tau-space but a PHASE of the spectral statistics. As the Jensen deformation parameter tau increases from 0, the Dirac operator D_K(tau) undergoes a transition from integrable (Poisson level statistics, bi-invariant symmetry) to chaotic (GOE level statistics, broken symmetry). The critical point tau_c of this transition — the Anderson transition of the internal Dirac operator — selects the vacuum without any potential minimum.

**Why these agents**: phonon-exflation-sim owns the eigenvalue computation infrastructure (tier1_dirac_spectrum.py) and handles heavy numerical work. tesla-resonance co-authored the Session 19 primer, has deep expertise in resonance phenomena, spectral analysis, Anderson localization, and the Berry-Tabor/BGS conjecture chain that underpins the entire analysis.

---

# II. REQUIRED READING

## For phonon-exflation-sim:

1. **Tier 1 Dirac spectrum script**: `tier0-computation/tier1_dirac_spectrum.py` — You wrote/maintained this. Functions: collect_spectrum(), sweep_s(), jensen_metric(), get_irrep_matrices(). This is the eigenvalue infrastructure.

2. **Session 18 V_eff convergence**: `sessions/session-18/session-18-veff-convergence.md` — The monotonicity result. DOF counts. Convergence between mps=5 and mps=6.

3. **Session 19 primer, Sections II + VI**: `sessions/session-19/session-19-primer.md` — The spectral complexity framework and computation plan. Your computation assignments are items 1-6 from Section VI.

4. **Your agent memory**: `.claude/agent-memory/phonon-exflation-sim/` — Check for Session 18 notes, sweep_s implementation details, and eigenvalue data format.

## For tesla-resonance:

5. **Session 19 primer (FULL)**: `sessions/session-19/session-19-primer.md` — You co-authored this. Sections II-IV are your framework. Section VI is the computation plan.

6. **Random matrix theory background**: The Brody distribution, Berry-Tabor conjecture (integrable => Poisson), BGS conjecture (chaotic => GOE), Anderson localization transition. You know this material.

7. **Session 18 wrapup, Section XII.7**: `sessions/session-18/session-18-wrapup.md` (lines 734-757) — "Complexity from the Inside." The conceptual framing that these diagnostics formalize.

8. **Your agent memory**: `.claude/agent-memory/tesla-resonance/` — Check for prior Session 19 primer context.

## Key Equations (for reference):

- **Jensen metric**: eq 3.68-3.72 (Paper 15). lambda_1=e^{2tau}, lambda_2=e^{-2tau}, lambda_3=e^{tau}. Volume-preserving.
- **Dirac eigenvalues**: lambda^2 = C_2(p,q)/3 at tau=0 (bi-invariant). Shift with tau via Jensen scale factors.
- **KL derivative**: Paper 17 eq 3.8, 4.1. Non-Killing C^2 fields create inter-sector coupling that grows with tau.
- **Gauge boson mass**: eq 3.84. m^2(tau) ~ [(e^tau - e^{-2tau})^2 + (1-e^{-tau})^2]/5. Quantifies inter-sector coupling growth.

---

# III. DATA AVAILABLE

All diagnostics use the **same eigenvalue data**. Generate it ONCE.

| Source | What | How to Access |
|:-------|:-----|:-------------|
| sweep_s output | Eigenvalues at 21 tau-values (0 to 2.0, step 0.1), 28 irreps (max_pq_sum=6) | Call sweep_s() from tier1_dirac_spectrum.py |
| Per-tau spectrum | ~1400 distinct eigenvalues per tau, with (p,q) sector labels and multiplicities | collect_spectrum() returns (eigenvalues, sector_labels, multiplicities) |
| Multiplicities | dim(p,q)^2 * 16 for each eigenvalue | Computed from irrep dimensions |

**Typical runtime**: ~8.7 seconds per tau-value at max_pq_sum=6. Full sweep of 21 values: ~3 minutes.

**Environment**: System Python (`python`). Uses numpy + scipy only. No GPU needed.

---

# IV. CALCULATION ASSIGNMENTS

## Agent Allocation

| Assignment | Primary | Secondary | Rationale |
|:-----------|:--------|:----------|:----------|
| S-1: Level statistics | phonon-exflation-sim | tesla-resonance (interpretation) | Heavy eigenvalue computation + RMT expertise |
| S-2: Spectral dimension | phonon-exflation-sim | tesla-resonance (CDT connection) | Heat kernel numerics + CDT knowledge |
| S-3: Entropy + heat capacity | phonon-exflation-sim | tesla-resonance (MEPP framework) | Thermodynamic computation + entropy production theory |
| S-4: Spectral gap check | phonon-exflation-sim | — | Straightforward from existing data |
| S-5: Complexity functional | tesla-resonance | phonon-exflation-sim (data) | Synthesis requires cross-domain perspective |

**Workflow**: phonon-exflation-sim generates the sweep_s data and runs S-1 through S-4 computationally. tesla-resonance provides the theoretical framework for interpretation and leads S-5 synthesis. Both agents validate each other's work.

---

### Assignment S-1: Level Statistics q(tau) (Priority: HIGHEST)

**THE single most decisive computation of Session 19.**

#### Background

The Berry-Tabor conjecture (1977): integrable quantum systems have Poisson nearest-neighbor spacing statistics, P(s) = exp(-s). The BGS conjecture (Bohigas-Giannoni-Schmit 1984): classically chaotic systems have GOE statistics, P(s) ~ (pi*s/2) exp(-pi*s^2/4).

At tau=0, D_K on bi-invariant SU(3) is block-diagonal in the Peter-Weyl basis. Each (p,q) sector is independently solvable. The (SU(3) x SU(3))/Z_3 isometry group makes the system integrable. **Expected: Poisson statistics.**

At tau>0, the Jensen deformation breaks to (SU(3) x SU(2) x U(1))/Z_6. Non-Killing C^2 fields couple different (p,q) sectors via the Kosmann-Lichnerowicz derivative (Paper 17, eq 3.8). D_K is no longer block-diagonal. **Expected: transition toward GOE.**

#### Computation Steps

1. **Generate eigenvalue data**: Call sweep_s() or collect_spectrum() at 21 tau-values (0.0, 0.1, ..., 2.0). Store ALL eigenvalues with sector labels and multiplicities.

2. **Spectral unfolding**: At each tau, sort all eigenvalues. Fit the smooth (Weyl) density N_smooth(lambda) by polynomial or staircase smoothing. Define unfolded eigenvalues x_n = N_smooth(lambda_n). This normalizes the mean spacing to 1.

   **IMPORTANT**: Unfold the FULL spectrum (all sectors combined), not individual sectors. The inter-sector statistics are what we're testing.

3. **Nearest-neighbor spacings**: s_n = x_{n+1} - x_n. Compute the histogram P(s) from the {s_n}.

4. **Brody fit**: Fit P(s) to the Brody distribution:
   ```
   P_Brody(s, q) = (q+1) * b * s^q * exp(-b * s^{q+1})
   b = [Gamma((q+2)/(q+1))]^{q+1}
   ```
   q=0 is Poisson. q=1 is GOE. Fit q by maximum likelihood or chi-squared.

5. **Number variance**: For cross-validation, compute:
   ```
   Sigma^2(L, tau) = <(n(L) - <n(L)>)^2>
   ```
   where n(L) is the number of unfolded eigenvalues in an interval of length L. Poisson: Sigma^2 = L. GOE: Sigma^2 ~ (2/pi^2)(ln(2*pi*L) + gamma + 1 - pi^2/8).

6. **Track q(tau)**: Plot q vs tau. Find the inflection point d^2q/dtau^2 = 0. This defines tau_c.

7. **INTER-SECTOR analysis** (critical): Repeat steps 2-6 using ONLY pairs of consecutive eigenvalues that come from DIFFERENT (p,q) sectors. This isolates the inter-sector coupling effect from intra-sector structure. The inter-sector q(tau) is the physically meaningful diagnostic.

#### Closure / Confirm

- **CLOSED**: q(tau) ~ 0 for all tau (including inter-sector). No Poisson-to-GOE transition. Spectral complexity path is CLOSED.
- **CONFIRM**: q(tau) rises monotonically with inflection at tau_c. If tau_c in [0.15, 0.30], three independent routes converge (gauge couplings at 0.2994, mass ratio phi at 0.15, spectral transition at tau_c).

#### Deliverable
- Plot of q(tau) (full spectrum AND inter-sector only)
- Value of tau_c (inflection point), if it exists
- Number variance Sigma^2(L) at tau=0 and tau=tau_c
- P(s) histograms at tau=0, tau=tau_c, and tau=2.0

---

### Assignment S-2: Spectral Dimension d_s(tau, sigma) (Priority: HIGH)

#### Background

The spectral dimension is defined via the heat kernel trace:
```
K(tau, sigma) = Sum_n mult_n * exp(-sigma * lambda_n(tau)^2)
d_s(tau, sigma) = -2 * d(log K) / d(log sigma)
```

For a d-dimensional Riemannian manifold, Weyl's law gives d_s -> d as sigma -> 0. At tau=0 (homogeneous SU(3)), d_s = 8 at ALL scales (high degeneracies enforce this). Any departure from d_s = 8 at tau > 0 is a definitive signature of broken homogeneity.

CDT (Causal Dynamical Triangulations, Ambjorn et al. 2005) finds d_s flowing from ~2 at Planck scales to ~4 at macroscopic scales. If the Jensen deformation produces a d_s = 4 crossing, this is a direct CDT connection.

#### Computation Steps

1. At each of 21 tau-values, compute K(tau, sigma) for sigma in np.logspace(-2, 2, 50).
2. Extract d_s = -2 * d(log K)/d(log sigma) via central finite differences in log-space.
3. Plot the 2D surface d_s(tau, sigma).
4. **Validation**: Confirm d_s(0, sigma) = 8 for all sigma (within numerical precision).
5. Search for contour d_s = 4 in the (tau, sigma) plane.

#### Closure / Confirm

- **CLOSED**: d_s(tau, sigma) = 8 everywhere. No dimensional reduction. CDT connection fails.
- **CONFIRM**: d_s = 4 crossing exists at some (tau_c, sigma_c). Direct CDT link.

#### Deliverable
- 2D contour plot of d_s(tau, sigma)
- Location of d_s = 4 crossing (tau_c, sigma_c), if any
- d_s(tau) at fixed sigma = 1.0 (1D slice for comparison with CDT literature)

---

### Assignment S-3: Spectral Entropy + Heat Capacity (Priority: HIGH)

#### Background

Define the spectral partition function and thermodynamic quantities:
```
Z(tau, beta) = Sum_n mult_n * exp(-beta * lambda_n(tau)^2)
p_n(tau, beta) = mult_n * exp(-beta * lambda_n^2) / Z
S(tau, beta) = -Sum_n p_n * log(p_n)        [Shannon entropy]
C(tau, beta) = beta^2 * (<lambda^4> - <lambda^2>^2)  [heat capacity]
```

The entropy production rate dS/dtau measures spectral complexification speed. A maximum in dS/dtau identifies the MEPP (Maximum Entropy Production Principle) selected state. A peak in C(tau) at fixed beta is a lambda-point analog — a second-order phase transition in the internal geometry.

#### Computation Steps

1. Compute Z(tau, beta) at each of 21 tau-values for beta in np.logspace(-2, 2, 50).
2. Compute probabilities p_n = mult_n * exp(-beta * lambda_n^2) / Z.
3. Shannon entropy: S = -Sum p_n * log(p_n). Scan over beta to find beta-independent features.
4. Entropy production rate: dS/dtau via central differences.
5. Heat capacity: C = beta^2 * (Sum p_n * lambda_n^4 - (Sum p_n * lambda_n^2)^2).
6. Search for MAXIMUM in dS/dtau across tau.
7. Search for PEAK in C(tau) at each fixed beta.
8. Check for beta-independent features (if extrema shift with beta, the diagnostic loses predictive power).

#### Closure / Confirm

- **CLOSED**: dS/dtau monotonically increasing with no extremum. Entropy picture adds nothing beyond V_eff.
- **CONFIRM**: Peak in C(tau) at tau_c corroborating S-1 inflection. Phase transition confirmed independently.

#### Deliverable
- S(tau) at 3 representative beta values
- dS/dtau plot with extrema marked
- C(tau) at 3 representative beta values, with peaks marked
- Beta-independence check: tau_c vs beta

---

### Assignment S-4: Near-Zero Spectral Density Check (Priority: MEDIUM)

#### Computation Steps

1. From the sweep_s eigenvalue data, extract the SMALLEST absolute eigenvalue at each tau.
2. Compute spectral density rho(lambda) near lambda = 0 (histogram in a window [-epsilon, +epsilon]).
3. Report minimum gap value and its (sector, tau) location across all 28 sectors and 21 tau-values.

Session 18 already found minimum gap = 0.818 at sector (0,0), tau ~ 0.26. This confirms it systematically.

#### Result

If gap > 0 everywhere: fermion condensate route (Banks-Casher) is CLOSED on compact SU(3). Table permanently.

#### Deliverable
- Minimum spectral gap vs tau (plot)
- Minimum gap value and location

---

### Assignment S-5: Complexity Functional Omega(tau) (Priority: MEDIUM)

**BLOCKED BY S-1, S-2, S-3.** tesla-resonance leads this synthesis.

#### Computation Steps

1. Compute inter-sector level repulsion:
   ```
   R_reg(tau) = Sum_{n<m, sectors differ} 1 / [(lambda_n - lambda_m)^2 + epsilon^2]
   ```
   where epsilon = typical intra-sector spacing (set to median spacing within the largest sector).

2. Combine the three diagnostics:
   ```
   Omega(tau) = d_s(tau, sigma_*) * S(tau, beta_*) * R_reg(tau) / R_reg(0)
   ```
   with sigma_* = 1.0 and beta_* chosen at the most beta-insensitive point from S-3.

3. Check for MAXIMUM or PLATEAU in Omega(tau).

#### Deliverable
- Omega(tau) plot
- Location of maximum/plateau (if any)
- Comparison: does Omega_max occur at tau_c from S-1?

---

# V. DECISION GATE (end of session)

| Result | Interpretation | Next Step |
|:-------|:--------------|:----------|
| q(tau) inflection at tau_c in [0.15, 0.30] | **Three independent routes converge** | Framework 55-70%. Write up. Proceed to 19b (rolling modulus) + 19c (eigenvectors). |
| q(tau) inflection at tau_c > 0.30 | Transition exists, doesn't match gauge constraint | Investigate. Proceed to 19b. |
| q(tau) ~ 0 for all tau | **Spectral complexity CLOSED** | Framework stays 35-50%. 19b (rolling modulus) becomes critical. |
| d_s = 4 crossing found | CDT connection | Major result independent of q(tau). |
| C(tau) peak at tau_c from S-1 | Phase transition doubly confirmed | Strongest possible outcome for Path A. |

---

# VI. SUCCESS CRITERIA

- [ ] S-1: q(tau) plot (full + inter-sector) + tau_c + number variance + P(s) histograms
- [ ] S-2: d_s(tau, sigma) surface + d_s=4 crossing check + 1D slice
- [ ] S-3: S(tau), dS/dtau, C(tau) + extrema + beta-independence check
- [ ] S-4: Spectral gap vs tau + minimum value
- [ ] S-5: Omega(tau) synthesis + maximum location

**5 deliverables. All from existing data. All computable in hours.**

All scripts go in `tier0-computation/`. Naming: `s19a_level_statistics.py`, `s19a_spectral_dimension.py`, `s19a_entropy_capacity.py`, `s19a_spectral_gap.py`, `s19a_complexity_functional.py`.

**Environment**: System Python (`python`). numpy + scipy + matplotlib. No GPU.

---

# VII. WHAT THIS SESSION DOES NOT COVER

The following are addressed in Sessions 19b and 19c:

| Item | Session | Why Separate |
|:-----|:--------|:-------------|
| Coupled (sigma, tau) FRW ODEs [Calc A] | 19b | Different expertise (cosmological dynamics, not spectral analysis) |
| Gauge coupling drift [Calc B] | 19b | Needs FRW solution from Calc A |
| w(z) vs DESI [Calc C] | 19b | Post-processing of Calc A |
| V_eff exponential fit + slow-roll params | 19b | Prerequisite for Calc A |
| Eigenvector extraction | 19c | Code infrastructure for Session 20 |
| D_total Pfaffian | 20+ | Needs eigenvectors from 19c |

---

*"The right question is: 'What phase is it in?' And the answer — testable from existing data — is: the spectral phase transition of the internal Dirac operator."* — Session 19 Primer

*"The spectral complexity path is the most RESONANT with the framework's own structure. The universe as a vibrating cavity, the vacuum as a spectral phase, the Anderson transition as vacuum selection — these are not imported analogies. They are CONSEQUENCES of having a Dirac operator on a deforming compact manifold."* — Tesla
