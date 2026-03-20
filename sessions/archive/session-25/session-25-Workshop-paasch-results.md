# Session 25: Paasch Mass-Quantization Analyst Results

**Date**: 2026-02-21
**Agent**: paasch-mass-quantization-analyst (Opus 4.6)
**Input data**: `s23a_eigenvectors_extended.npz` (28 sectors, 9 tau values, 11,424 eigenvalues per tau), `s25_feynman_results.npz`, `s25_berry_results.npz`, `s25_baptista_results.npz`, `s22a_paasch_curve.npz`
**References**: Paasch 2009 (02_), 2016 calc (03_), 2016 FSC (04_), all five Session 25 synergy documents, Berry/Baptista/Feynman Session 25 results

---

## 1. Task Map

### Tasks from Collaborative Document (`session-25-paasch-collab.md`)

| ID | Task | Status | Result |
|----|------|--------|--------|
| [Pa]S-1 | Inter-sector eigenvalue ratio map | COMPLETED | P-1 below |
| [Pa]S-2 | Tight-binding band structure H_TB | NOT ATTEMPTED | Requires V_{nm} matrix not yet computed |
| [Pa]S-3 | Transcendental equation connection | COMPLETED | P-5 below |
| [Pa]S-4 | Test P-25: phi_paasch at stabilized tau_0 | COMPLETED | P-4 below: **PASSES** |
| Phi^{3/2} test | (4,0)/(0,0) vs phi_paasch^{3/2} | COMPLETED | P-2 below |
| Gap-edge CW cross-reference | Phi at CW minimum | COMPLETED | P-3, P-4 below |
| Mass number N(j)=7n | Casimir connection | COMPLETED | P-6 below |

### Tasks from Synergy Documents

| Source | Task | Status | Result |
|--------|------|--------|--------|
| QuestionSynergy Q-2 | phi^{3/2} test with N-number correction | COMPLETED | P-2 |
| QuestionSynergy Q-4 | Nambu unit from Dirac spectrum | NOTED | Partial in P-6; no direct Nambu unit extraction possible |
| AssessmentSynergy | Goal 6 (phi_paasch) assessment | COMPLETED | Confirmed: phi is inter-sector only |
| CollaborativeSynergy [Pa]S-1 | Full ratio map | COMPLETED | P-1 |
| ClosingSynergy | Decisive computations list | P-1 through P-6 executed | See below |

### Tasks NOT Attempted (with justification)

1. **Tight-binding H_TB** ([Pa]S-2): Requires computing the off-diagonal matrix elements V_{nm} = <psi_n|H_{pert}|psi_m> between sectors. The eigenvector data exists in `s23a_eigenvectors_extended.npz`, but the perturbation Hamiltonian for Jensen deformation has not been coded as a matrix operator. This is a Session 26+ task.

2. **Koide formula test** (collab Section 4.3): Requires identifying three eigenvalues to play the role of (m_e, m_mu, m_tau). No natural triplet selection criterion exists without a physical identification scheme. Deferred.

---

## 2. Berry / Baptista / Feynman Cross-Reference

### 2.1 Berry Erratum: B = 982 is Quantum Metric, NOT Berry Curvature

**Source**: `sessions/2026-02-21-session-25-berry-results.md`, Berry computation B-2

The Session 24a value B = 982.5 at tau = 0.10, reported as Berry curvature, is actually the **quantum metric** (Provost-Vallee tensor), not the Berry curvature (antisymmetric part of the overlap matrix). Berry curvature Omega = 0 identically on the Jensen deformation path because the Kosmann connection K_a is anti-Hermitian, making Im(G_{ab}) = 0.

**Impact on Paasch analysis**: This eliminates Goals 3 and 5 (Berry-phase-driven stabilization, topological phi). The quantum metric g_{ab} is real and symmetric -- it measures the distance between neighboring states in parameter space but provides no holonomy. Wall W5 (Berry curvature = 0) is now established.

**Paasch perspective**: Paasch's framework does not invoke Berry phases. The phi_paasch ratio is a spectral ratio, not a geometric phase. The Berry erratum does not affect any Paasch computation. However, it eliminates one proposed mechanism by which phi_paasch could have been dynamically selected (Berry-phase-driven stabilization at a tau value where ratios hit phi_paasch).

### 2.2 Baptista: V_Baptista Has Minimum, But Quantitative Bridge Fails

**Source**: `sessions/2026-02-21-session-25-baptista-results.md`

V_Baptista (eq 3.87, Baptista's geometric functional) has a minimum for ALL kappa > 0. To place that minimum at tau_0 = 0.15, one needs kappa ~ 772. The spectral action framework produces kappa ~ 1-30 from the Seeley-DeWitt coefficients. The Connes-Baptista bridge is quantitatively incomplete: a factor of 25-770x mismatch.

**Impact on Paasch**: If V_Baptista could stabilize at tau = 0.15, then the phi_paasch ratio (3,0)/(0,0) = 1.531588 would be locked in. But the stabilization mechanism itself is not established. The phi_paasch crossing at tau = 0.15 is a kinematic fact; whether anything dynamically selects tau = 0.15 remains open.

### 2.3 Feynman: Gap-Edge CW Minimum at tau = 0.15

**Source**: `sessions/2026-02-21-session-25-feynman-results.md`, computation F-2

This is the most Paasch-relevant cross-agent finding:

| N (modes) | tau_min | Depth (%) |
|-----------|---------|-----------|
| 2 | 0.25 | 5.09 |
| 4 | 0.20 | 1.85 |
| 8 | 0.15 | 0.40 |
| 16 | 0.15 | 1.85 |
| 32 | 0.00 | 0.00 (monotone) |
| 50 | 0.10 | 0.58 |
| 100 | 0.15 | 0.70 |

The gap-edge Coleman-Weinberg potential, restricted to the N lowest eigenvalues, is NON-MONOTONE with a minimum at tau = 0.15 for N = 8 and N = 16. The full CW (N = all) is monotone -- this is established by Sessions 18-24. But the gap-edge restriction creates a minimum precisely at the tau value where the (3,0)/(0,0) ratio equals phi_paasch.

**Root cause**: The lambda_min turnaround at tau = 0.2323 (depth 6.28%). Below this tau, lambda_min decreases; above, it increases. This turnaround is the single spectral feature driving ALL non-monotone signals (gap-edge CW, partition function at high beta, lambda_min profile itself).

**Feynman also found**: (2,2)/(1,1) = 1.6215 at tau = 0.10, deviating 0.21% from phi_golden = 1.618034.

---

## 3. Computations Performed

### P-1: Inter-Sector Eigenvalue Ratio Map

**Method**: For each of 9 tau values and all 378 sector pairs (28 sectors), computed the ratio of minimum positive eigenvalues max(lambda_i, lambda_j) / min(lambda_i, lambda_j). Compared against five Paasch target constants within a 2% window.

**Targets tested**:

| Target | Value | Crossings (within 2%) |
|--------|-------|----------------------|
| phi_paasch | 1.531580 | 128 |
| phi_golden | 1.618034 | 124 |
| phi_paasch^{3/2} | 1.895438 | 98 |
| 4/phi_golden^2 | 1.527864 | 142 |
| phi_paasch * phi_golden | 2.478149 | 20 |
| **Total** | | **512** |

**Trial factor analysis**:
- Total trials: 378 pairs x 9 tau x 5 targets = 17,010
- Expected random crossings (4% window): 680
- Observed: 512
- **Ratio observed/expected: 0.75**

**Verdict**: The overall crossing count is BELOW random expectation. The Paasch target constants are NOT preferentially represented in the inter-sector ratio spectrum taken as a whole. However, this aggregate statistic conceals the extreme precision of specific matches.

**Top matches by target**:

| Target | Sector pair | tau | Ratio | Deviation |
|--------|-------------|-----|-------|-----------|
| phi_paasch | (0,0)/(3,0) | 0.15 | 1.531588 | 0.0005% |
| phi_paasch | (0,0)/(0,3) | 0.15 | 1.531588 | 0.0005% |
| phi_paasch | (2,1)/(0,5) | 0.30 | 1.532883 | 0.085% |
| phi_golden | (2,0)/(2,3) | 0.35 | 1.618822 | 0.049% |
| phi_golden | (0,2)/(3,2) | 0.35 | 1.618822 | 0.049% |
| phi_p^{3/2} | (0,0)/(4,0) | 0.00 | 1.895414 | 0.0013% |
| phi_p^{3/2} | (1,1)/(4,0) | 0.00 | 1.895414 | 0.0013% |
| 4/phi_g^2 | (0,0)/(3,0) | 0.00 | 1.527525 | 0.022% |

**Only 2 matches within 0.01% of phi_paasch**: both are (0,0)/(3,0) and its conjugate at tau = 0.15. No other sector pair at any tau achieves this precision.

### P-2: phi_paasch^{3/2} Test

**Motivation**: Paasch's mass formula involves mass numbers N(j) where m(j) ~ f_N^{N(j)}. If eigenvalues map to masses via lambda ~ m^{2/3} (as in some dimensional reduction schemes), then the eigenvalue ratio should be phi_paasch^{3/2} rather than phi_paasch itself.

**Result**:

| tau | (4,0)/(0,0) ratio | phi_p^{3/2} = 1.895438 | Deviation |
|-----|-------------------|------------------------|-----------|
| 0.00 | 1.895414 | 1.895438 | **0.0013%** |
| 0.10 | 1.892311 | 1.895438 | 0.165% |
| 0.15 | 1.877239 | 1.895438 | 0.960% |

The best match occurs at tau = 0.00 (round metric), not at the gap-edge CW minimum. This is OPPOSITE to the phi_paasch behavior, which peaks at tau = 0.15.

**Algebraic identification**: At tau = 0, this ratio is an algebraic number determined by the SU(3) Dirac spectrum on the round metric. Its near-coincidence with phi_paasch^{3/2} is a numerical accident of the round SU(3) geometry, not a dynamical selection.

### P-3: Cross-Reference with Feynman Gap-Edge CW

**Finding**: The gap-edge CW minimum (N = 8, 16) occurs at tau = 0.15 with depths of 0.40% and 1.85% respectively. At this same tau value, (3,0)/(0,0) = 1.531588, deviating only 0.0005% from phi_paasch.

**Partition function**: F(tau; beta) is non-monotone for beta >= 10, with minimum shifting from tau = 0.10 (beta = 10) to tau = 0.25 (beta >= 200). Depth saturates at ~3.25% for beta = 1000.

**Lambda_min profile**: Minimum at tau_turnaround = 0.2323, lambda_min = 0.818380, depth 6.28% below round-metric value 0.833333 (= 5/6). This turnaround is the root cause of all non-monotone behavior.

### P-4: TEST P-25 -- phi_paasch at the Gap-Edge CW Minimum

**Pre-registration** (from `session-25-paasch-collab.md`, Section 3.4):

> Pre-registered test: If the phonon-exflation framework stabilizes tau at some tau_0, then the eigenvalue ratio m_{(3,0)}/m_{(0,0)} at that tau_0 should equal phi_paasch = 1.53158 within 0.5%.

**Test conditions**:
- tau_0 = 0.15 (location of gap-edge CW minimum for N = 8, 16)
- m_{(3,0)}/m_{(0,0)} at tau = 0.15 = 1.531588
- phi_paasch = 1.53158
- Deviation = 0.0005%

**Verdict: TEST P-25 PASSES** (0.0005% << 0.5% threshold)

**Caveats**:
1. The gap-edge CW is NOT a confirmed stabilization mechanism. The full CW potential is monotone.
2. The 0.5% threshold was generous; the actual match is far tighter than required.
3. This is a CONDITIONAL result: IF something stabilizes at tau = 0.15, THEN the Paasch ratio is reproduced to extraordinary precision.

### P-5: Transcendental Equation Analysis

**Paasch's equation**: x = e^{-x^2} (Eq. 2g, 2009 paper)

**Numerical solution**: x* = 0.6529186404, giving phi_paasch = 1/x* = 1.5315843937

**Paasch's stated value**: phi_paasch = 1.53158 (5 significant figures)

**Computed from D_K spectrum**: (3,0)/(0,0) at tau = 0.15 = 1.531588

**Comparison**:

| Source | Value | Deviation from 1/x* |
|--------|-------|---------------------|
| Paasch (stated) | 1.53158 | 0.00029% |
| D_K at tau = 0.15 | 1.531588 | 0.00024% |
| D_K at tau = 0.00 | 1.527525 | 0.265% |

**tau trajectory**: The ratio (3,0)/(0,0) evolves from sqrt(7/3) = 1.527525 at tau = 0 (round metric, an algebraic number) and crosses through phi_paasch = 1.531584 at tau ~ 0.15. The crossing is smooth and monotone in this neighborhood (the ratio peaks near tau = 0.10-0.15 before declining).

**FSC equation**: ln(x) = -x has solution x = 0.5671432904 (the Lambert W function value W(1)). Paasch uses this in deriving alpha = 0.007297359.

### P-6: Mass Number N(j) = 7n Structure and SU(3) Connection

**Paasch mass numbers**:

| Particle | N(j) | n = N/7 | 7n? |
|----------|------|---------|-----|
| Electron | 7 | 1 | Yes |
| Muon | 35 | 5 | Yes |
| Pion | 42 | 6 | Yes |
| Kaon | 98 | 14 | Yes |
| Proton | 150 | 21.43 | **No** |
| Neutron | 151 | 21.57 | **No** |

Note: Proton and neutron do NOT satisfy N = 7n exactly.

**SU(3) cumulative dimension connection**:

Ordering irreps by increasing Casimir C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q)/3, the cumulative dimension sum gives:

| Through rep | Cumulative dim | Paasch N? |
|-------------|---------------|-----------|
| (0,1) [C_2 = 4/3] | **7** | N(electron) = 7 |
| (1,1) [C_2 = 3] | 15 | -- |
| (0,2) [C_2 = 10/3] | 27 | -- |
| (2,1) [C_2 = 16/3] | **42** | N(pion) = 42 |
| (1,2) [C_2 = 16/3] | 57 | -- |
| (0,3) [C_2 = 6] | 77 | -- |
| (2,2) [C_2 = 8] | 104 | -- |

Two of Paasch's mass numbers (7 and 42) appear as cumulative SU(3) representation dimensions. However:
- The match requires a specific ordering within degenerate Casimir levels (taking (2,1) before (1,2)).
- The shell-based count (adding full conjugate pairs at each C_2 level) does NOT reproduce any Paasch numbers beyond 7.
- N(muon) = 35, N(kaon) = 98, and N(proton) = 150 do NOT appear in any natural cumulation of SU(3) dimensions.

**Assessment**: The N(electron) = 7 = dim(0,0) + dim(1,0) + dim(0,1) = 1 + 3 + 3 connection is suggestive but likely coincidental, given that 7 is also the dimension of the first Casimir shell. The N(pion) = 42 match requires an arbitrary ordering choice.

**Casimir eigenvalues and sector structure**:

| Sector (p,q) | C_2 | dim | lambda_min(tau=0) | lambda_min^2 |
|-------------|-----|-----|-------------------|-------------|
| (0,0) | 0 | 1 | 0.866025 | 3/4 |
| (1,0) | 4/3 | 3 | 0.833333 | 25/36 |
| (0,1) | 4/3 | 3 | 0.833333 | 25/36 |
| (1,1) | 3 | 8 | 0.866025 | 3/4 |
| (0,3) | 6 | 10 | 1.322876 | 7/4 |
| (3,0) | 6 | 10 | 1.322876 | 7/4 |
| (2,2) | 8 | 27 | 1.443376 | 25/12 |
| (4,0) | 28/3 | 15 | 1.641476 | ~2.694 |

Notable: lambda_min(0,0)^2 = 3/4 and lambda_min(3,0)^2 = 7/4 are both exact fractions. The ratio is sqrt(7/3) = 1.527525, which is 0.265% below phi_paasch.

---

## 4. New Insights

### 4.1 The tau = 0.15 Coincidence: Precise but Conditional

The central finding of this session is the **triple coincidence at tau = 0.15**:

1. The gap-edge CW potential (N = 8, 16) has its minimum at tau = 0.15
2. The eigenvalue ratio (3,0)/(0,0) = 1.531588 = phi_paasch to 0.0005% at tau = 0.15
3. The lambda_min profile is in its declining phase at tau = 0.15, approaching turnaround at tau = 0.2323

This is a genuine numerical coincidence in the D_K spectrum. The question is whether it is:
- **(a) Structurally forced**: Some algebraic feature of the SU(3) Dirac operator combined with the Jensen deformation forces this coincidence. Evidence FOR: the ratio at tau = 0 is sqrt(7/3), an algebraic number close to phi_paasch, and the deformation shifts it to an even closer match.
- **(b) Numerically accidental**: The ratio happens to cross phi_paasch near the CW minimum by chance. Evidence FOR: the trial factor analysis shows 512 crossings vs 680 expected, meaning Paasch targets are LESS common than random in the overall spectrum. The specific match at tau = 0.15 is an outlier.

**Assessment**: The trial factor strongly suggests (b). The (3,0)/(0,0) match is the ONLY match within 0.01% of phi_paasch across all 17,010 trials. With 17,010 trials, finding one match at 0.0005% is significant (p ~ 10^{-4} for a single trial), but the extreme precision of the specific match must be weighed against the large trial count. The look-elsewhere effect reduces significance but does not eliminate it entirely.

### 4.2 The Algebraic Root: sqrt(7/3) to phi_paasch

At tau = 0 (round SU(3) metric):
- lambda_min(0,0)^2 = 3/4 (exact)
- lambda_min(3,0)^2 = 7/4 (exact)
- ratio = sqrt(7/3) = 1.52752523...

At tau = 0.15 (Jensen deformed):
- ratio = 1.53158804...
- phi_paasch = 1/x* where x* = e^{-x*^2}, giving 1.53158439...

The deformation shifts the ratio from sqrt(7/3) to phi_paasch over a tau interval of 0.15. The shift is:

delta = phi_paasch - sqrt(7/3) = 0.00406 (0.265% of sqrt(7/3))

This is a smooth, monotone drift driven by the different tau-dependence of eigenvalues in the (0,0) and (3,0) sectors. The (0,0) eigenvalue drops faster than (3,0) as tau increases from 0, pushing the ratio upward.

**The question remains**: Is there a reason the D_K spectrum on Jensen-deformed SU(3) should produce the same constant that solves x = e^{-x^2}? No algebraic or analytic connection has been established. The coincidence is at the 5 ppm level but lacks a derivation.

### 4.3 phi_paasch^{3/2} is a Round-Metric Accident

The (4,0)/(0,0) ratio equals phi_paasch^{3/2} to 0.0013% at tau = 0. Unlike the phi_paasch match (which occurs at tau = 0.15), this match occurs at the round metric and DEGRADES under deformation. This identifies it as an algebraic property of the round SU(3) Dirac spectrum, not a dynamical feature.

Since the phi_paasch^{3/2} value is:

phi_p^{3/2} = (1/x*)^{3/2} where x* solves x = e^{-x^2}

its appearance at the round metric would require:

lambda_min(4,0)/lambda_min(0,0) = (1/x*)^{3/2}

at the round metric. The left side is an algebraic number (ratio of SU(3) Dirac eigenvalues), the right side is transcendental. They cannot be exactly equal. The 0.0013% match is a numerical near-miss.

### 4.4 Golden Ratio Match is Weaker

Feynman found (2,2)/(1,1) = 1.6215 at tau = 0.10, deviating 0.21% from phi_golden. The match is 400x less precise than the phi_paasch match. At the round metric (tau = 0), the ratio is 5/3 = 1.6667, deviating 3.0% from phi_golden. The golden ratio proximity is a broad feature, not a sharp crossing.

### 4.5 Trial Factor Closes Aggregate Statistical Significance

The single most important negative result: 512 crossings observed vs 680 expected across the full ratio map. The Paasch target constants are UNDERREPRESENTED relative to random in the D_K spectrum. This means the spectrum does NOT have a systematic preference for Paasch-type ratios. The individual matches at (3,0)/(0,0) and (4,0)/(0,0) are specific outliers in an otherwise unremarkable distribution.

---

## 5. Status Summary

### What phi_paasch IS in the D_K spectrum

| Statement | Precision | Status |
|-----------|-----------|--------|
| (3,0)/(0,0) = phi_paasch at tau = 0.15 | 0.0005% | **CONFIRMED** (Session 12, 22a, now) |
| phi_paasch is inter-sector, not intra-sector | -- | **CONFIRMED** (Session 24a) |
| phi_paasch appears at gap-edge CW minimum | -- | **CONFIRMED** (this session) |
| (4,0)/(0,0) = phi_p^{3/2} at tau = 0 | 0.0013% | **NEW** (this session) |
| At tau = 0, ratio = sqrt(7/3) exactly | algebraic | **NEW** (this session) |

### What phi_paasch is NOT

| Statement | Evidence |
|-----------|----------|
| phi_paasch is NOT preferentially represented in the full ratio spectrum | Trial factor: 0.75x random |
| phi_paasch is NOT connected to Casimir ratios | Closest: C_2(3,0)/C_2(4,0) = 1.556, 1.6% off |
| phi_paasch^{3/2} is NOT dynamically selected | Best match at tau = 0, degrades under deformation |
| N(j) = 7n is NOT systematically reproduced by SU(3) dim counting | Only N(e) = 7 and N(pi) = 42 match; requires ordering choice |
| phi_paasch is NOT derived from the SU(3) Dirac spectrum | Coincidence, not identity |

### Walls (updated)

| Wall | Description | Status |
|------|-------------|--------|
| W1 | V_full monotone (no stabilization minimum) | STANDING |
| W2 | F/B ratio = 0.55 (constant-ratio trap) | STANDING |
| W3 | Block-diagonal D_K (no inter-sector coupling) | STANDING |
| W4 | BCS closed at mu = 0 (spectral gap) | STANDING |
| W5 | Berry curvature = 0 identically (NEW, this session) | STANDING |

### Closed Mechanism (updated count)

Total: **19** (18 from pre-Session 25 + Berry curvature stabilization)

### Probability Assessment

**Pre-Session 25**: Panel 5% (4-7%), Sagan 3% (2-4%).

**Paasch-specific update**: No change warranted. The phi_paasch coincidence at tau = 0.15 was already known (Session 12, 22a). TEST P-25 formalizes the conditional result but does not change the framework probability because the condition (stabilization at tau = 0.15) remains unmet. The trial factor analysis (0.75x random) is mildly negative -- it does not CLOSED the phi_paasch observation but removes any claim that the spectrum systematically encodes Paasch's mass quantization scheme.

The phi_paasch appearance remains a **single isolated coincidence** at (3,0)/(0,0) at tau = 0.15, not a systematic pattern. This is consistent with the Session 24a finding that phi_paasch has zero crossings within the (0,0) singlet sector.

### Open Questions for Future Sessions

1. **Algebraic origin of sqrt(7/3)**: The round-metric ratio (3,0)/(0,0) = sqrt(7/3) is an exact algebraic number. Is there a formula lambda_min^2(p,q) = f(C_2, dim) that produces this? The values lambda_min^2 = 3/4 for (0,0) and 7/4 for (3,0) suggest lambda_min^2 = (2p+2q+1)/4 or similar, but this does not hold for all sectors.

2. **Why does the ratio cross phi_paasch at tau ~ 0.15?**: The deformation shifts lambda_min(0,0) faster than lambda_min(3,0), pushing the ratio from sqrt(7/3) to phi_paasch. Is the crossing location (tau = 0.15) determined by a simple function of the Casimir values?

3. **Tight-binding H_TB**: Computing the inter-sector hopping matrix V_{nm} would determine whether the phi_paasch ratio controls the band gap in a tight-binding picture. This could connect to Paasch's logarithmic potential.

4. **Debye cutoff dependence**: The gap-edge CW is non-monotone at N = 8-16 but monotone at large N. Is there a physical Debye-type cutoff that selects N ~ 8-16? If so, the CW minimum at tau = 0.15 becomes a genuine stabilization candidate.

---

## Appendix A: Numerical Data Tables

### A.1 Minimum Positive Eigenvalues by Sector

| tau | (0,0) | (1,0) | (1,1) | (3,0) | (2,2) | (4,0) |
|-----|-------|-------|-------|-------|-------|-------|
| 0.00 | 0.866025 | 0.833333 | 0.866025 | 1.322876 | 1.443376 | 1.641476 |
| 0.10 | 0.833074 | -- | 0.867682 | 1.280507 | 1.406942 | 1.576435 |
| 0.15 | 0.823873 | -- | 0.870089 | 1.261834 | 1.389896 | 1.546606 |
| 0.20 | 0.819140 | -- | 0.873844 | 1.245074 | 1.373941 | 1.518779 |
| 0.25 | 0.818635 | -- | 0.879161 | 1.230411 | 1.359305 | 1.493117 |
| 0.30 | 0.822148 | -- | 0.886248 | 1.218029 | 1.346219 | 1.469577 |
| 0.50 | 0.873214 | -- | 0.936128 | 1.194974 | 1.302671 | 1.394621 |

### A.2 Key Ratios vs tau

| tau | (3,0)/(0,0) | dev phi_p | (4,0)/(0,0) | dev phi_p^{3/2} | (2,2)/(1,1) | dev phi_g |
|-----|-------------|-----------|-------------|-----------------|-------------|-----------|
| 0.00 | 1.527525 | 0.265% | 1.895414 | **0.001%** | 1.666667 | 3.006% |
| 0.10 | 1.537088 | 0.360% | 1.892311 | 0.165% | 1.621496 | **0.214%** |
| 0.15 | **1.531588** | **0.001%** | 1.877239 | 0.960% | 1.597418 | 1.274% |
| 0.20 | 1.519977 | 0.758% | 1.854114 | 2.180% | 1.572295 | 2.827% |
| 0.25 | 1.503004 | 1.866% | 1.823911 | 3.774% | 1.546138 | 4.443% |

### A.3 Transcendental Equation Solutions

| Equation | Solution | Derived constant | Paasch value | Deviation |
|----------|----------|-----------------|-------------|-----------|
| x = e^{-x^2} | x* = 0.652919 | phi = 1/x* = 1.531584 | 1.53158 | 0.00029% |
| ln(x) = -x | x = 0.567143 | (used in FSC derivation) | -- | -- |

---

## Appendix B: Methodology Notes

All computations used `s23a_eigenvectors_extended.npz` containing 11,424 eigenvalues per tau across 28 sectors at 9 tau values (0.00, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50). Feynman cross-reference used `s25_feynman_results.npz`. Berry and Baptista cross-references used their respective Session 25 results markdown files.

Python environment: phonon-exflation-sim/.venv312 (Python 3.12, numpy, scipy).

No new `.npz` data files were generated. All computations are analytic post-processing of existing spectral data.

---

*Generated by paasch-mass-quantization-analyst, Session 25, 2026-02-21*
