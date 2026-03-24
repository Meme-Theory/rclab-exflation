# Session 16, Round 1b: Spectrum Coffee
## Gen-Physicist + Paasch-Analyst Joint Assessment
## Date: 2026-02-13

---

## PHI STATUS: One-Paragraph Honest Summary

The z=3.65 phi^1 clustering at Jensen s=1.14 is a REAL spectral feature of the Jensen TT-deformation on SU(3), confirmed by Monte Carlo against three independent null models (unconstrained diagonal, volume-preserving diagonal, perturbative general). It is NOT an artifact of the code, the metric, or insufficient sampling. However, after applying the look-elsewhere correction for scanning over s (Gross-Vitells: ~20 effective trials in [0,2]), the significance drops to approximately 2.5-3.0 sigma. The target phi=1.53158 was pre-specified from the Paasch research program, which partially mitigates target-selection penalties but does not eliminate them. Critically, the 667 phi-proximate pairs are BULK pairwise ratios across the full spectrum, dominated by high-multiplicity sectors at high (p,q) — exactly the eigenvalues LEAST relevant to physical particle masses. The physically meaningful quantity is the sector-specific ratio m_{(3,0)}/m_{(0,0)} = sqrt(7/3) = 1.5275 at s=0, which crosses phi at s approximately 0.15 (Session 12). This single ratio crossing is guaranteed by the intermediate value theorem and its proximity to phi at the crossing point is ~1.5 sigma. The phi^1 signal is real mathematics, not yet real physics. The decisive test is whether V_eff selects s_0 such that specific sector ratios equal phi — that computation has not been performed.

---

## PAASCH SURVIVAL SCORECARD

### Claim-by-Claim Assessment

Each claim is assessed in TWO domains: (A) as an empirical pattern in measured particle masses, and (B) as a feature of the D(SU(3)) Dirac spectrum.

| # | Claim | Measured masses | D(SU(3)) spectrum | Evidence |
|---|-------|----------------|-------------------|----------|
| 1 | **G(t) ~ 1/t (LNH)** | CLOSED | N/A | LLR: dG/dt/G < 2e-13/yr rules out 1/t by 100x |
| 2 | **phi = 1.53158 from ln(phi) = phi^{-2}** | ALIVE (algebraic) | phi^1 at z=3.65 | Transcendental equation is self-consistent. Value appears in spectrum at ~2.5-3 sigma after LEE. |
| 3 | **Mass spiral (phi^n series)** | Empirical pattern | CLOSED | MC definitive: phi^2 z=-0.29, phi^3 z=-0.16. Geometric series absent in spectrum. Empirical spiral never tested against D_K. |
| 4 | **Logarithmic spiral sequences (S1-S6)** | ALIVE (0.4% precision) | CLOSED | Measured masses align on spiral at 45-degree separations. NO angular structure in eigenvalue space. No consecutive ratio = phi. |
| 5 | **Mass integers N(j) = 7n** | ALIVE (empirical) | CLOSED (wrong integers) | N(mu)=35, N(pi)=42, N(K)=98, N(p)=150 exist empirically. Spectrum has lambda^2 = n/36 (different integer structure). |
| 6 | **f_N ~ 1.53 (inter-species scaling)** | ALIVE (1.5298 empirical) | UNTESTED on D_K | f_N = (2/Phi)^2 = 1.5279 theoretical. Close to sqrt(7/3) = 1.52753. Key Z_3 inter-sector test target. |
| 7 | **M-value golden ratio (0.618)** | ALIVE (Fig. 2 of 2016) | UNTESTED | M(i+1)/(2*M(i)) approaches golden ratio in measured masses. Not tested in sector eigenvalues. |
| 8 | **Proton mass m_p(m_e, alpha)** | ALIVE (6-digit) | N/A | Formula, not derivation. Independent of D(SU(3)). Would become prediction if N(b)=112 emerges from D_K. |
| 9 | **Neutron mass m_n(m_p, alpha, f_N)** | ALIVE (8-digit) | N/A | Uses f_N explicitly. Independent of D(SU(3)). |
| 10 | **Tau mass m_tau(m_p, m_e)** | ALIVE (5-digit) | N/A | Less precise than p, n. Independent of D(SU(3)). |
| 11 | **Inter-generation Z_3 ratios** | N/A | UNTESTED (swing vote) | Paper 18 App E provides mechanism. Computation not done. Bridge between domains. |
| 12 | **Koide-like relations** | ALIVE (Koide 1981) | UNTESTED | Lepton mass formula. Testable against sector eigenvalues at s_0. |
| 13 | **Fine structure constant alpha** | ALIVE (9-digit, pending circularity check) | N/A | alpha = (1/f)^{2*n_3} with n_3=10. Derives from phi + mass integers. Derivation chain: phi -> N(b), n_3 -> m_p -> m_b -> alpha. Measured alpha enters as CHECK not input. |

### Summary Statistics

- **CLOSED in both domains**: 1 claim (LNH)
- **Empirically alive, CLOSED on D(SU(3))**: 3 claims (spiral sequences, mass integers, geometric phi^n series)
- **Empirically alive, UNTESTED on D_K**: 3 claims (f_N, golden ratio M-values, Koide)
- **Empirically alive, independent of spectrum**: 5 claims (phi algebraic, m_p, m_n, m_tau, alpha)
- **UNTESTED bridge**: 1 claim (Z_3 inter-generation = swing vote)

### Key Insight (Paasch-Analyst)

The algebraic core (phi, mass formulas, alpha derivation) was NEVER tested against D(SU(3)). It stands or falls on its own phenomenological foundation. The claims that died on D(SU(3)) -- geometric series, spiral sequences, integer mapping -- were the STRUCTURAL predictions, not the algebraic core. The Z_3 test bridges these two domains: if it works, the algebraic core finds its geometric home; if it fails, it remains an orphaned empirical pattern.

### The Kepler Analogy (refined)

Paasch's empirical mass formulas are like Kepler's laws: remarkably accurate patterns extracted from data using scaffolding (LNH for Paasch, circular orbits for Kepler) that turns out to be wrong. The algebraic core (phi, mass integers, f_N) is scaffolding-independent — just as the period-distance relation T^2 proportional to a^3 survived the demise of circular orbits. The question is whether the Baptista spectral geometry provides the "Newton" that explains WHY these patterns exist.

---

## PRE-REGISTERED PREDICTIONS

All predictions stated BEFORE computation. Significance thresholds specified. Null models defined.

### Prediction 1: V_eff minimum at physically significant s_0

**Target**: V_eff(s) = Sum_n (d_n/64pi^2) lambda_n^4(s) [ln(lambda_n^2(s)/Lambda^2) - 3/2] has a unique local minimum at s_0.

**Test statistic**: Location of s_0 and whether m_{(3,0)}(s_0)/m_{(0,0)}(s_0) is within 1% of phi = 1.53158.

**Threshold**:
- s_0 exists with unique minimum: PASS/FAIL (binary)
- |ratio - phi|/phi < 0.01 at s_0: SUGGESTIVE (but depends on number of sectors tested)
- |ratio - phi|/phi < 0.001 at s_0: STRONG (0.1% is well below typical spacing)

**Null model**: Probability that a randomly chosen s in [0, 2] gives |m_{(3,0)}/m_{(0,0)} - phi|/phi < threshold. From Session 12 scan, ratio varies smoothly from sqrt(7/3) = 1.5275 (s=0) through phi at s approximately 0.15 to larger values. Null probability for 1% tolerance approximately 5% (from 1/20 of the scan range). For 0.1% tolerance approximately 0.5%.

### Prediction 2: Z_3 generation splitting

**Target**: At s_0, each (p,q) sector with dim >= 3 splits into 3 sub-eigenvalues under Z_3 action.

**IMPORTANT DISTINCTION**: Paasch's f_N ~ 1.53 connects successive particle SPECIES (pion -> kaon -> proton), NOT successive generations (e -> mu -> tau). SM generation ratios are m_mu/m_e = 206.8, m_tau/m_mu = 16.8 (leptons), m_c/m_u ~ 500, m_t/m_c ~ 140 (quarks). These are MUCH larger than f_N. So f_N is NOT the expected within-sector Z_3 ratio.

Two distinct predictions:

**Prediction 2a (Z_3 splitting pattern)**:
- The Z_3-split sub-eigenvalues within a sector should have ratios consistent with the SM generation mass hierarchy
- For the lepton-identified sector: sub-eigenvalue ratios r_1:r_2:r_3 ~ 1 : 207 : 3477 (matching m_e : m_mu : m_tau)
- For quark-identified sectors: matching m_u : m_c : m_t or m_d : m_s : m_b
- Tolerance: 30% (given uncertainties in quark mass measurements and sector identification)

**Prediction 2b (Inter-sector ratios)**:
- The ACROSS-SECTOR eigenvalue ratios (comparing the same Z_3 sub-component) should be:
  - Close to f_N = 1.5279-1.5298 (Paasch inter-species scaling)
  - Or close to phi = 1.53158
  - Or close to sqrt(7/3) = 1.52753

**Test statistic**:
- For 2a: Compute the ratio of largest to smallest sub-eigenvalue within each sector. Compare to SM generation ratios.
- For 2b: Compute cross-sector ratios of corresponding Z_3 sub-eigenvalues. Count phi/f_N-proximate pairs.

**Threshold**:
- z > 3.0 (pre-LEE) for a single pre-specified target: SUGGESTIVE
- z > 5.0: EVIDENCE
- z < 2.0: NOISE

**Null model**: Permutation null — shuffle sub-eigenvalue assignments across sectors, preserving multiplicities. N=500 samples minimum.

**Tiered priors (Gen-Physicist / Paasch-Analyst consensus)**:

| Outcome | Gen-Physicist prior | Paasch-Analyst prior | Consensus |
|---------|--------------------|--------------------|-----------|
| Z_3 gives 3 generations, hierarchical | 50-60% | 40-50% | ~50% |
| Ratios within 30% of SM masses | 35-45% | 25-35% | ~35% |
| Ratios within 5% of Paasch's specific formulas | 10-20% | 10-15% | ~15% |

**Note on radiative corrections (Paasch-Analyst)**: Tree-level D_K eigenvalues miss QCD binding energy, EM corrections, and CKM mixing. These are a few-percent effect for mass RATIOS within sectors (same quantum numbers cancel many corrections), but could be order-of-magnitude for absolute masses. The 30% threshold accounts for this.

### Prediction 3: Sector eigenvalue ratios at s_0 reproduce Paasch mass numbers

**Target**: At s_0, the ratios of U(2)-singlet eigenvalues across (p,q) sectors satisfy:

- lambda_{(p1,q1)} / lambda_{(p2,q2)} = (N(j1)/N(j2))^{1/2} for identified particle-sector pairs

where N(j) are Paasch mass numbers (35, 42, 98, 105, 133, 145, 150).

**Test**: Identify which (p,q) sectors correspond to which particles (electron, muon, pion, kaon, proton). This identification must be made on theoretical grounds (quantum numbers, U(2) branching), NOT fitted. Then check eigenvalue ratios against mass number ratios.

**Threshold**:
- 3+ correct ratios within 5%: SUGGESTIVE
- 5+ correct ratios within 1%: STRONG
- 0-1 correct ratios: NULL

**Null model**: Random assignment of particles to sectors (permutation test, N=1000).

### Prediction 4: f_N in spectral action coefficients

**Target**: The Seeley-DeWitt coefficient ratio a_4/a_2 at s_0 involves f_N or phi.

**Test statistic**: Compute a_n at s_0 from the converged (p+q <= 6) spectral action. Check ratio.

**Threshold**: Within 1% of phi or f_N: SUGGESTIVE. This is a secondary test.

---

## STATISTICAL PROTOCOL FOR ROUND 2

### Mandatory Requirements for All New Claims

**A. Pre-Registration Protocol**

Before ANY computation that will be used to make a claim:
1. STATE the target value (numerical, exact)
2. STATE the test statistic (formula)
3. STATE the significance threshold (z-score or p-value)
4. STATE the null model (algorithm for generating null samples)
5. RECORD all of the above in the Round output BEFORE reporting results

Violation of pre-registration invalidates the claim. Post-hoc discoveries are labeled "exploratory" and carry no significance weight.

**B. Null Models (minimum 3 for any claim)**

| Model | Purpose | Implementation |
|-------|---------|----------------|
| Spectral null | Random left-invariant metrics | mc_phi_significance.py framework, N >= 200 |
| Permutation null | Break geometric correlations | Shuffle labels within sectors, N >= 500 |
| GUE null | Generic Hermitian matrix statistics | Matched spectral range and density, N >= 200 |

For V_eff-related claims, add:
| Random potential null | Random smooth V(s) with same boundary conditions | Polynomial or Fourier with random coefficients, N >= 200 |

**C. Correction Hierarchy**

Apply ALL applicable corrections in this order:
1. **Bonferroni**: If testing K targets simultaneously, multiply p-values by K
2. **Gross-Vitells (LEE)**: If scanning a parameter, apply trial factor = (scan range)/(correlation length)
3. **Target selection**: If target was chosen from a set of algebraic numbers, apply factor = |set|
4. **Operator mismatch**: If testing on D(SU(3)) but claiming D_K(CP^2) relevance, flag as "indirect"

**D. Significance Scale**

| z-score (after ALL corrections) | Label | Action |
|-------------------------------|-------|--------|
| z > 5.0 | EVIDENCE | Report as main result |
| 3.0 < z < 5.0 | SUGGESTIVE | Report with caveats |
| 2.0 < z < 3.0 | HINT | Exploratory only |
| z < 2.0 | NOISE | Do not claim significance |

**E. Reporting Requirements**

Every claimed result must include:
- Raw z-score (before corrections)
- Corrected z-score (after ALL applicable corrections)
- List of corrections applied with justification
- Null model sample size and convergence check
- Bootstrap 95% CI on the z-score itself
- Whether the claim was pre-registered or exploratory
- Sensitivity to tolerance window (report z at 1%, 2%, 3%, 4%, 5%)
- Spectral density control: is the bin containing the target generically dense?

**F. Blind Analysis (recommended for decisive tests)**

For high-stakes tests (V_eff minimum, Z_3 splitting), use blind analysis:
- Agent A computes the spectrum/eigenvalues
- Agent B computes the statistics and significance
- Neither shares intermediate results until the final answer
- This prevents unconscious optimization of analysis choices

**G. Special Rule for V_eff**

The V_eff minimum s_0 is computed FIRST and INDEPENDENTLY. All mass ratio tests are performed AT s_0. No scanning over s is permitted for mass ratio claims — s_0 is an OUTPUT, not a parameter. This eliminates the LEE that plagued the Session 12-14 phi analysis.

---

## D/H AND d_pair_factor ASSESSMENT

### d_pair_factor = 1.5: Hidden Fifth Parameter

The Phase 2B validation (handout section 2B.6) reveals d_pair_factor as a hidden tuning parameter with 2 OOM sensitivity (D/H ranges from 2.4e-6 to 2.9e-4 across d_pair_factor in [1.0, 2.5]). This does NOT invalidate the simulation but it DOES:

1. **Downgrade D/H from "8% match" to "order-of-magnitude feasibility demonstration"**
2. **Expose a definitional gap**: What constitutes a "bound" vortex-antivortex pair is not defined by the theory
3. **Add a 5th free parameter** to what was already a 4-parameter fit to 1 observable
4. **Confirm Session 3's assessment**: D/H is a fit, not a prediction

### What Survives

- GPE vortex dynamics CAN produce D/H in the correct order of magnitude (10^{-5})
- Grid convergence is excellent (2.4% spread at 1024-2048)
- The geometric mechanism (healing length growth suppresses pairs) is robust
- Energy conservation is maintained to 7.8e-7 relative drift

### Path to Predictivity

d_pair_factor should emerge from the theory via:
1. V_eff determines s_0 (zero free parameters)
2. At s_0, the binding energy E_bind of vortex-antivortex pairs is calculable from the spectral geometry
3. The binding criterion (what counts as "bound") follows from E_bind vs thermal energy
4. d_pair_factor becomes a derived quantity, not a fitted one

Until Phase 4a (coupled V_eff ODEs) is complete, the simulation D/H result carries weight only as a mechanism demonstration.

---

## CONVERGENCE NOTES

### Points of Agreement (Gen-Physicist + Paasch-Analyst)

1. **z=3.65 is a real spectral feature, NOT a Paasch signature**: Both agents agree the MC result is genuine geometry of the Jensen deformation. It is a SINGLE-POWER phenomenon, not the geometric series required by Paasch's mass spiral. Pre-registration of tolerance windows is essential.

2. **Mass spiral ON D(SU(3)) is closed**: Geometric series (phi^n for n > 1), consecutive ratio matching, spiral angular structure, and N(j)=7n integer mapping all fail on the Dirac spectrum. The algebraic core (phi, mass formulas, alpha derivation) is UNTOUCHED because it was never tested against D(SU(3)) — it stands on its own phenomenological foundation.

3. **Z_3 is the swing vote**: The inter-generation test from Paper 18 App E is the ONLY known bridge between the empirically alive Paasch core and the geometrically proven Baptista spectrum. Both agents agree this is the highest-value theoretical computation.

4. **d_pair_factor makes D/H a 5-parameter fit**: The simulation demonstrates OOM feasibility but is not predictive. Phase 4a (coupled V_eff ODEs) is essential. Both agents agree the mechanism (healing length growth) is robust even if the precise value is tuned.

5. **Pre-registration mandatory, report negatives**: Both agents converged on the need for pre-registration of target values, tolerances, and null models. Null results carry equal scientific weight.

6. **~40-50% of original Paasch claims viable**: The algebraic core is independent of D(SU(3)) and the structural predictions failed on D(SU(3)). Roughly half the framework survives in its original empirical domain.

### Points of Disagreement (Resolved or Narrowed)

1. **f_N vs f_M nomenclature**: Gen-physicist identified f_N ~ 1.53 (N-value ratio), Paasch-analyst initially quoted f_N ~ 1.24 (M-value ratio f_M). **RESOLVED**: f_M = 2/Phi = 1.236 is the M-value ratio; f_N = f_M^2 = (2/Phi)^2 = 1.528 is the N-value ratio. Both are correct, operating at different levels of the Paasch hierarchy. The Z_3 inter-sector test should target f_N = 1.528.

2. **Z_3 prior probability**: Gen-physicist gives 35-45% for 30% match; Paasch-analyst gives 25-35%. Difference reflects weighting of radiative correction effects on tree-level ratios. **NARROWED**: Both agree on tiered structure (pattern: ~50%, 30% match: ~30-40%, 5% Paasch-precise: ~10-20%). The ~10% spread reflects honest uncertainty about QCD/EM correction cancellation in ratio comparisons.

3. **Spectral density in phi bin**: Paasch-analyst flags that the [1.50-1.55] bin was never independently tested for generic density. Gen-physicist argues MC null models implicitly account for this. **PARTIALLY RESOLVED**: The null models do test whether random metrics produce the same density, but an explicit bin-width-independent spectral density test would be cleaner. Added to Round 2 protocol.

4. **Alpha derivation circularity**: Gen-physicist labeled this "circular?" based on the appearance that mass integers use alpha while alpha is derived from mass integers. Paasch-analyst notes the derivation chain is: phi -> mass integers N(b), n_3 -> proton mass -> constituent mass -> alpha. The MEASURED alpha enters only as a check, not as input. **STATUS**: Needs closer reading of the derivation chain. Labeled ALIVE pending verification rather than circular.

---

## KEY TECHNICAL INSIGHTS

### The 1.53 Cluster: Four Independent Quantities

Four algebraically independent quantities cluster within 0.27% of each other near 1.53:

| Quantity | Value | Origin | Algebraic source |
|----------|-------|--------|-----------------|
| phi (Paasch) | 1.53158 | ln(phi) = phi^{-2} | Transcendental equation |
| N(p)/N(K) | 1.53061 | 150/98 | Paasch mass number empirical ratio |
| f_N (theoretical) | 1.52786 | (2/Phi)^2 | Golden ratio M-value structure |
| sqrt(7/3) | 1.52753 | Parthasarathy bound | SU(3) Casimir ratio |

Pairwise fractional differences:
- phi vs f_N: 0.24%
- phi vs sqrt(7/3): 0.26%
- f_N vs sqrt(7/3): **0.022%** (nearly identical)
- N(p)/N(K) vs sqrt(7/3): 0.20%

The near-identity of f_N and sqrt(7/3) is the most striking: f_N = 4/(Phi+1) involves sqrt(5) while sqrt(7/3) involves sqrt(7) and sqrt(3). These are **algebraically independent** — equality would require (3+sqrt(5))/2 = sqrt(48/7), which is false. Yet they differ by only 0.022%. This is a genuine numerical coincidence between the golden ratio (Paasch's empirical mass scaling) and the SU(3) Casimir structure (Parthasarathy bound). If the spectral geometry provides a mechanism connecting these two algebraic families, it would be a highly non-trivial structural result. The Z_3 computation is the test.

### The Two Phis

There are TWO distinct mathematical constants in this framework:
1. **Paasch phi = 1.53158**: Solution of ln(phi) = phi^{-2}. Appears as the spiral factor in Paasch's exponential mass model. Found at z=3.65 in Dirac spectrum pairwise ratios.
2. **Golden ratio Phi = 1.61803**: Appears in Paasch's M-value ratios (M(i+1)/(2M(i)) -> 0.618 = 1/Phi) and in the exponential scaling factor f_N = (2/Phi)^2.

These are algebraically linked via f_N = (2/Phi)^2 = 1.5279 (theoretical) or f_N = 1.5298 (empirical), which is numerically close to phi = 1.53158 (0.1% difference) but algebraically distinct. The Dirac spectrum tests phi, not Phi. The Z_3 generation test should check BOTH phi and f_N as separate targets.

### Paasch's Algebraic Core (LNH-Independent)

Stripped of the G(t)~1/t scaffolding, Paasch's surviving structure is:
1. phi = 1.53158 (transcendental equation, dimensionless)
2. Mass numbers N(j) = integer (empirical assignment)
3. f_N = (2/Phi)^2 = 1.5279 (connecting successive mass scales; empirical ~ 1.5298)
4. m_p = m_e * F(N(b), n_3, alpha) (6-digit formula)
5. m_n = m_p * G(f_N, n_3) (8-digit formula)

Items 1-3 are algebraic structure that COULD emerge from spectral geometry. Items 4-5 are formulas that would become predictions if their ingredients (N(b), n_3) are derivable from D_K eigenvalues.

### Why the Z_3 Test Is Decisive

The Z_3 generation mechanism (Paper 18 App E) is the ONLY known path from the Baptista geometry to inter-generation mass ratios. If it produces f_N or phi as within-sector eigenvalue ratios, it:
- Explains the phi^1 signal in the bulk spectrum (as a shadow of sector-specific structure)
- Derives the Paasch scaling factor from geometry (f_N becomes computable)
- Makes the mass formulas predictive (N(j) maps to (p,q) labels)
- Elevates the framework probability by 10-15 percentage points

If it fails, the Paasch connection is severed and the phi^1 signal becomes an unexplained curiosity.

---

## SUMMARY TABLE

| Category | Item | Status |
|----------|------|--------|
| Phi (z=3.65) | Real mathematics, not yet physics | ~2.5-3.0 sigma after LEE |
| Paasch: closed in both domains | 1 of 13 | LNH |
| Paasch: empirical alive, closed on D(SU(3)) | 3 of 13 | Spiral sequences, mass integers, phi^n series |
| Paasch: empirical alive, untested on D_K | 3 of 13 | f_N, golden ratio, Koide |
| Paasch: empirically alive, spectrum-independent | 5 of 13 | phi algebraic, m_p, m_n, m_tau, alpha |
| Paasch: bridge test | 1 of 13 | Z_3 inter-generation (swing vote) |
| Pre-registered predictions | 4 | V_eff minimum, Z_3 splitting, mass numbers, SD coefficients |
| Statistical protocol | Defined | Pre-registration mandatory, 3 null models, Bonferroni+LEE |
| d_pair_factor | Hidden 5th parameter | Downgrades D/H to OOM demonstration |
| Decisive computation | V_eff minimum s_0 | Determines all downstream predictions |
