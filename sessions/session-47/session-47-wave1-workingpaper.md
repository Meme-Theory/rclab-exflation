# Session 47 Wave 1: BCS-Accessible Pi-Phase Ratio

**Date**: 2026-03-16
**Mode**: Compute (parallel independent)
**Objective**: Correct the S46 ratio of 2.19x (131 PW-weighted pi-phases / 59.8 pairs) by filtering to BCS-accessible channels only.

**User hypothesis**: the 2.19x comes from inflating the numerator with inert channels (B1 Trap 1, K₇-blocked B3). The true ratio within the active sector may be ~1.

---

## W1-1: Sector Classification of Pi-Phase States (PI-SECTOR-47)

**Agent**: spectral-geometer
**Gate**: PI-SECTOR-47

### Gate PI-SECTOR-47: PASS

All 13 pi-phase states classified into B1/B2/B3. No ambiguous boundary assignments.

### Method

Within each Peter-Weyl sector (p,q), the 16*dim(p,q) Dirac eigenvalues at the fold are rank-ordered by |lambda|. The lowest 2*dim states are B1 (U(2) singlet spinor sector), the next 8*dim are B2 (U(2) fundamental), and the top 6*dim are B3 (SU(2) adjoint). This rank assignment inherits from the B1 < B2 < B3 eigenvalue ordering at the bi-invariant point (tau=0) via adiabatic continuity.

**Verification**: On the (0,0) sector, rank-based classification reproduces the known B1(mult=2, |lambda|=0.820), B2(mult=8, |lambda|=0.845), B3(mult=6, |lambda|=0.971) exactly.

**Caveat**: In higher PW sectors, the spinor K_7 operator does NOT commute with D_K (verified: ||[I tensor iK_7, D_K]||/||D_K|| = 7.5% for (0,1)). This means eigenstates are MIXTURES of spinor sectors, and the rank-based classification is approximate near sector boundaries. All 13 pi-phase states sit well away from boundaries (zero ambiguous assignments).

### Cluster Boundaries

From the (0,0) sector:
- B1: |lambda| = 0.8197 (mult 2)
- B2: |lambda| = 0.8452 (mult 8)
- B3: |lambda| = 0.9714 (mult 6)

Within each (p,q) sector, rank boundaries:
- B1: ranks 0 to 2*dim-1
- B2: ranks 2*dim to 10*dim-1
- B3: ranks 10*dim to 16*dim-1

### Sector-Resolved Pi-Phase Table

| Rep (p,q) | dim | n_pi | |eval| at fold | Rank | Phase/pi | Sector | PW_pi |
|-----------|-----|------|---------------|------|----------|--------|-------|
| (0,1)     | 3   | 1    | 1.0784        | 20   | -0.991   | B2     | 3     |
| (0,2)     | 6   | 1    | 1.3697        | 43   | +0.999   | B2     | 6     |
| (0,3)     | 10  | 1    | 1.7590        | 97   | +0.980   | B2     | 10    |
| (0,3)     | 10  | 1    | 1.7915        | 108  | -0.990   | B3     | 10    |
| (1,0)     | 3   | 1    | 1.0752        | 16   | +0.993   | B2     | 3     |
| (1,1)     | 8   | 1    | 1.3862        | 75   | -0.970   | B2     | 8     |
| (2,0)     | 6   | 1    | 1.4304        | 54   | +0.982   | B2     | 6     |
| (2,1)     | 15  | 1    | 1.5965        | 105  | +0.993   | B2     | 15    |
| (2,1)     | 15  | 1    | 1.3658        | 24   | -0.988   | B1     | 15    |
| (2,1)     | 15  | 1    | 1.4279        | 42   | -0.969   | B2     | 15    |
| (2,1)     | 15  | 1    | 1.4691        | 52   | +0.977   | B2     | 15    |
| (2,1)     | 15  | 1    | 1.7233        | 168  | -0.979   | B3     | 15    |
| (3,0)     | 10  | 1    | 1.8190        | 114  | -0.984   | B3     | 10    |
| **Total** |     | **13** |            |      |          |        | **131** |

### PW-Weighted Sector Totals

| Sector | n_pi (unweighted) | PW_pi (weighted) | Fraction |
|--------|-------------------|------------------|----------|
| B1     | 1                 | 15               | 11.5%    |
| B2     | 9                 | 81               | 61.8%    |
| B3     | 3                 | 35               | 26.7%    |
| **Total** | **13**         | **131**          | 100%     |

### BCS Accessibility Assessment

- **B1 (PW=15)**: INERT. Trap 1 (V(B1,B1) = 0 exact, U(2) singlet selection rule). These pi-phases cannot contribute to BCS pair creation.
- **B2 (PW=81)**: ACTIVE. The BCS pairing channel. Cooper pairs carry K_7 charge +/-1/4.
- **B3 (PW=35)**: NEEDS K7 CHECK. B3 states have K_7 = 0 in the (0,0) sector, but the pairing matrix element V(B3,B3) is nonzero. The K_7 selection rule for B3 pairing requires downstream verification (W1-2).

BCS-accessible pi-phase count (B2 only): 81 PW-weighted.
Corrected ratio: 81 / 59.8 = **1.35x** (down from 2.19x).

If B3 is also BCS-accessible: (81 + 35) / 59.8 = **1.94x**.
If only B2 is accessible: 81 / 59.8 = **1.35x**.

### Files

- Script: `tier0-computation/s47_pi_sector.py`
- Data: `tier0-computation/s47_pi_sector.npz`
- Plot: `tier0-computation/s47_pi_sector.png`

---

## W1-2: K₇ Selection Filter (K7-FILTER-47)

**Agent**: dirac-antimatter-theorist
**Gate**: K7-FILTER-47

### Gate K7-FILTER-47: PASS

The K₇ selection filter reduces BCS-accessible pi-phases from 131 to 81 (conservative) or 116 (moderate). B1 (PW=15) is inert in ALL scenarios.

### Algebraic Structure of K₇ Mixing

The Dirac operator on a Peter-Weyl sector (p,q) has the form:

  D_{(p,q)} = sum_{a,b} E_{ab} rho(X_b) tensor gamma_a + I tensor Omega

The operator I tensor iK_7 commutes with the second term ([iK_7, Omega] = 0, verified to machine precision). The commutator is:

  [I tensor iK_7, D_{(p,q)}] = i * sum_{a,b} E_{ab} rho(X_b) tensor [iK_7, gamma_a]

This is STRUCTURALLY nonzero whenever rho is nontrivial: the generators gamma_{3,4,5,6} (the C_2 coset directions) do not commute with iK_7, and rho(X_b) weighs these contributions by representation matrices rather than scalars.

In the (0,0) sector, rho(X_b) = 0 for all b (trivial rep), so the commutator vanishes identically — recovering the S34 result [iK_7, D_{(0,0)}] = 0. This is the ONLY sector where K_7 is an exact quantum number.

### K₇ Commutator Norms by Rep

| Rep (p,q) | dim | ||[I tensor iK₇, D]||/||D|| |
|-----------|-----|----------------------------|
| (0,0)     | 1   | 0.000 (exact)              |
| (0,1)     | 3   | 0.095                      |
| (1,0)     | 3   | 0.095                      |
| (1,1)     | 8   | 0.118                      |
| (0,2)     | 6   | 0.121                      |
| (2,0)     | 6   | 0.121                      |
| (0,3)     | 10  | 0.134                      |
| (2,1)     | 15  | 0.131                      |
| (3,0)     | 10  | 0.134                      |

Mean: 11.9%. The mixing grows with rep dimension but remains bounded. The formula [I tensor iK_7, D] = i * sum E_{ab} rho(X_b) tensor [iK_7, gamma_a] is verified to machine precision in all sectors.

### K₇ Charge Uncertainty in Dirac Eigenstates

In the (0,0) sector, B2 eigenstates carry pure K₇ = +/-1/4. In higher reps, eigenstates become MIXTURES of K₇ eigenspaces. The variance of K₇ expectation values measures this mixing:

| Rep   | sqrt(max var(q₇)) in B2 | V_cross/V_same estimate |
|-------|-------------------------|------------------------|
| (0,1) | 0.125                   | 12.5%                  |
| (1,0) | 0.125                   | 12.5%                  |
| (1,1) | 0.250                   | 25.0%                  |
| (0,2) | 0.137                   | 13.7%                  |
| (2,0) | 0.137                   | 13.7%                  |
| (0,3) | 0.183                   | 18.3%                  |
| (2,1) | 0.190                   | 19.0%                  |
| (3,0) | 0.183                   | 18.3%                  |

The cross-charge pairing V(q+,q-), which is machine-zero in the (0,0) sector, leaks to 12-25% of V_same in higher reps. This is a perturbative correction, not a structural change.

### BCS Accessibility Classification

**B1 (PW=15): INERT (all scenarios)**
- Trap 1: V_BCS(B1,B1) = 0 to 3.4e-29 (S34). This follows from U(2) Schur's lemma, INDEPENDENT of K₇ conservation. It is structural and permanent.

**B2 (PW=81): ACTIVE (all scenarios)**
- V(B2,B2) = 0.256 (dominant pairing channel). Cooper pairs carry K₇ = +/-1/4 in (0,0). In higher reps, K₇ mixing shifts charges but same-charge pairing remains the dominant channel (75-87% of total V).

**B3 (PW=35): MARGINAL**
- V(B3,B3) = 0.0034 (76x weaker than V(B2,B2)). V(B2,B3) = 0.029 enables proximity gap Delta_B3 = 0.084.
- In (0,0): B3 has K₇ = 0, so K₇ does not block B3 self-pairing.
- In higher reps: B3 acquires <|q₇|> ~ 0.10-0.11, but with large variance (sqrt(var) ~ 0.14). K₇ does not sharpen a selection rule for B3 because B3 was never in a definite K₇ state to begin with outside (0,0).
- B3 participates in the condensate via proximity coupling to B2, but its self-interaction is weak. Classification: accessible but subdominant.

### Three Scenarios

| Scenario      | PW_accessible | PW_inert | Sectors active        | Rationale |
|---------------|--------------|----------|----------------------|-----------|
| Conservative  | 81           | 50       | B2 only              | B3 self-pairing too weak (V/V_B2 = 1.3%); treat as inert |
| Moderate      | 116          | 15       | B2 + B3              | B3 proximity gap is nonzero; K₇ does not block; B3 participates |
| Liberal       | 116          | 15       | B2 + B3 (+ K₇ cross) | K₇ mixing opens cross-charge in B2 at 12-25% level |

Moderate and liberal give the same count because K₇ cross-charge leakage does not add new pairing CHANNELS — it modifies existing matrix elements by O(15%).

### Assessment

The K₇ selection filter is a genuine structural constraint. In the (0,0) sector, K₇ conservation is exact and cross-charge pairing is forbidden to machine precision. In higher PW sectors, this exactness degrades to approximate conservation at the 12-25% level, but the qualitative structure persists: B2 dominates pairing, B1 is inert (by Schur, not K₇), and B3 is marginal.

The W1-1 finding that [iK₇, D] != 0 outside (0,0) is confirmed and QUANTIFIED. The algebraic origin is transparent: the commutator equals sum E_{ab} rho(X_b) tensor [iK₇, gamma_a], which is nonzero because rho(X_b) are nontrivial matrices in higher reps while [iK₇, gamma_a] != 0 for the four C₂ coset directions (a = 3,4,5,6). The (0,0) sector uniquely has rho = 0 (trivial rep), making K₇ exact ONLY there.

For the corrected ratio calculation (W1-3), the conservative estimate gives PW_accessible = 81, the moderate gives 116.

### Files

- Script: `tier0-computation/s47_k7_filter.py`
- Data: `tier0-computation/s47_k7_filter.npz`
- Plot: `tier0-computation/s47_k7_filter.png`

---

## W1-3: Corrected Ratio and S46 Audit (RATIO-CORRECT-47)

**Agent**: feynman-theorist
**Gate**: RATIO-CORRECT-47

### Gate RATIO-CORRECT-47: PASS

R_B2 = 81 / 54.22 = **1.494**. The S46 discrepancy (2.19x) is RESOLVED as base-mixing. Within the active B2 sector, topology and dynamics are matched to within a factor of 1.5.

### The Denominator Problem

S46 computed 131 / 59.8 = 2.19. Both numbers are correct individually. The error is that they come from different bases:

- **Numerator 131**: PW-weighted pi-phase states across ALL sectors (B1=15, B2=81, B3=35)
- **Denominator 59.8**: total quasiparticle pairs from the 992-mode sudden quench (all sectors combined)

To construct a sector-matched ratio, we must decompose the 59.8 pairs into B1/B2/B3. Three methods were tested:

| Method | Basis | N_B1 | N_B2 | N_B3 | R_B2 | Problem |
|--------|-------|------|------|------|------|---------|
| A: ED fractions | 8-mode n_occ | 29.53 | 29.40 | 0.87 | 2.755 | B1 at 49% from cross-channel entanglement |
| B: BCS v2 fractions | v2*mult ratios | 4.96 | 54.22 | 0.62 | **1.494** | SELECTED |
| C: v2 * mode count | v2*N_modes absolute | 5.54 | 60.54 | 0.69 | 1.338 | Total = 66.8, overshoots 59.8 |

**Method B is correct.** The BCS occupation amplitude v2_bcs = [0.0446, 0.1220, 0.0019] per mode, weighted by multiplicity [1, 4, 3], gives sector fractions: B1 = 8.3%, B2 = 90.7%, B3 = 1.0%. Applied to 59.8 total pairs: N_B2 = 54.22.

Method A is WRONG because the 8-mode ED populates B1 at 49.4% through off-diagonal V(B1,B2) = 0.130 cross-channel entanglement, not BCS self-pairing. Method C overshoots because the 8-mode v2 per mode does not transfer to 992 modes with a different density of states.

### Ratio Table

| Label | Numerator | Denominator | Ratio | Base |
|:------|:----------|:------------|:------|:-----|
| R_raw (S46) | 131 (all pi-phases) | 59.80 (all pairs) | **2.191** | All sectors, mismatched |
| R_B2 (BCS fractions) | 81 (B2 pi-phases) | 54.22 (B2 BCS pairs) | **1.494** | B2-only, sector-matched |
| R_B2+B3 (moderate) | 116 (B2+B3 pi-phases) | 54.84 (B2+B3 pairs) | **2.115** | Active sectors |
| R_B2 (ED fractions) | 81 (B2 pi-phases) | 29.40 (B2 ED pairs) | **2.755** | WRONG: ED inflates B1 |

The correction decomposes as:
- Numerator: 131 -> 81 (factor 0.618, removing 50 inert/marginal channels)
- Denominator: 59.8 -> 54.22 (factor 0.907, B2 carries 91% of BCS weight)
- Net: 2.19 -> 1.49 (32% reduction)

The numerator shrinks more than the denominator because B1 contributes 11.5% of pi-phases but only 8.3% of BCS pairs.

### S46 Correction Notice

**RETRACTED**: The number 2.19x (131 pi-phases / 59.8 pairs). This was computed from mismatched bases.

**Specific error**: Base-mixing. S46 divided a topological count (PW-weighted pi-phase multiplicity across all sectors) by a dynamical count (quasiparticle pairs from all sectors) without restricting both to the same dynamically active sector. The numerator counted 15 channels in B1 where V(B1,B1) = 0 (Trap 1, permanent). The denominator included B1 pairs that are cross-channel entanglement through V(B1,B2), not BCS self-pairing.

**Corrected value**: R_B2 = 81 / 54.22 = 1.494 (B2-only, BCS v2 fraction decomposition).

**What survives from S46**:
- 131 PW-weighted pi-phases total (topological fact, verified in W1-1)
- 59.8 total quasiparticle pairs (S38 sudden quench, not recomputed)
- Sector-resolved V matrix: V(B1,B1) = 0, V(B2,B2) = 0.256, V(B3,B3) = 0.003
- v2_bcs = [0.0446, 0.1220, 0.0019] per mode
- BCS gap hierarchy: Delta = [0.372, 0.732, 0.084]
- B2 dominates both topology (81/131 = 62%) and dynamics (v2_B2 * 4 = 91%)

### The B1 Occupation Paradox

In the 8-mode ED ground state (N=1 pair sector), B1 carries 49.4% of the pair weight despite V(B1,B1) = 0 exactly.

This is NOT B1 self-pairing. It is cross-channel entanglement:

- The ED Hamiltonian includes off-diagonal V(B1,B2) = 0.130, which is 50.8% of V(B2,B2) = 0.256.
- The ground state wavefunction is |psi> = -0.307|B1> - 0.474|B2_1> - 0.474|B2_2> - 0.474|B2_3> - 0.474|B2_4> - 0.054|B3_1> - ...
- B1 participates in the correlated pair state through its coupling to B2, not through self-interaction.

In the BCS (mean-field) treatment, B1 has v2 = 0.045 per mode (8.3% of total), which correctly reflects the proximity-induced gap Delta(B1) = 0.372. This gap is entirely generated by V(B1,B2) coupling to the B2 condensate.

The lesson: the 8-mode ED ground state is correlated beyond mean field. Using ED occupation fractions to decompose 992-mode BCS pairs double-counts cross-channel correlations. The BCS v2 fractions are the correct sector decomposition for BCS pairs.

### Assessment

The S46 ratio 2.19x retracts. The corrected ratio R_B2 = 1.494 is within a factor of 2 of unity, consistent with the user hypothesis that the original discrepancy was base-mixing.

The residual factor of 1.5 has a simple interpretation: within B2, there are ~1.5 PW-weighted topological channels (pi-phase states) per Cooper pair. This is a moderate topological surplus -- not the factor-of-2 structural BDI result that S46 claimed, but a nontrivial observation that more topological channels exist than are dynamically occupied.

The deeper structural result is the B2 dominance: 62% of pi-phase topology and 91% of BCS dynamics both concentrate in the B2 (U(2) fundamental) sector. Topology and dynamics select the SAME sector, with a 1.5:1 ratio within it.

### Files

- Script: `tier0-computation/s47_ratio_correct.py`
- Data: `tier0-computation/s47_ratio_correct.npz`

---

## W2-1: BCS Condensate Density on the Maximal Torus (CONDENSATE-T2-47)

**Agent**: landau-condensed-matter-theorist
**Gate**: CONDENSATE-T2-47 (INFO)

### Gate CONDENSATE-T2-47: INFO

The BCS condensate |Delta(theta_1,theta_2)|^2 on the maximal torus T^2 in SU(3) is **strongly concentrated at the identity** with a contrast ratio exceeding 3 million. The pattern exhibits exact S_3 Weyl symmetry (verified to 4e-14). The Haar-weighted density peaks at r = 0.85 rad (~0.27*pi) from the identity, reflecting the competition between the identity-peaked condensate and the Haar measure that vanishes at the identity.

### Method

1. **Characters via Weyl formula.** For each (p,q) rep with p+q <= 3, the SU(3) character chi_{(p,q)}(theta_1,theta_2) is computed via the Weyl character formula:

     chi_{(p,q)} = A_{rho+lambda} / A_{rho}

   where A_mu = det[e^{i mu_{sigma(j)} phi_j}] summed over S_3 with signs, rho = (2,1,0), lambda = (p+q,q,0). Singular points (Weyl chamber walls where A_rho = 0) are handled by fallback to direct weight enumeration via Fourier analysis of the Weyl formula. All 9 reps verified: Weyl formula matches direct weight sum to 1.3e-14 at test points, and chi_{(p,q)}(0,0) = dim(p,q) for all reps.

2. **BCS weighting.** The condensate on T^2 is:

     Delta(theta) = sum_{(p,q)} w_{(p,q)} * chi_{(p,q)}(theta)

   where the BCS weight w_{(p,q)} = w_avg * dim(p,q) * exp(-(eps_{(p,q)} - eps_{(0,0)})^2 / (2*Delta_B2^2)).

   - w_avg = sum_s frac_s * Delta_s = 0.444 (sector-averaged gap, same for all reps)
   - frac_s = {B1: 2/16, B2: 8/16, B3: 6/16} (spinor structure)
   - Delta_s = {0.372, 0.732, 0.084} (S46 BCS gaps)
   - eps_{(p,q)} from S44 spectrum: (0,0) at 0.838, up to (0,3) at 1.901
   - Delta_B2 = 0.732 sets the BCS energy scale

   BCS suppression factors: (0,0): 1.000, (1,0): 0.979, (0,1): 0.936, (1,1): 0.864, (2,0): 0.783, (0,2): 0.724, (2,1): 0.620, (3,0): 0.494, (0,3): 0.348.

3. **Grid.** 200x200 over (theta_1, theta_2) in [0, 2*pi)^2.

4. **Haar measure.** The SU(3) Haar measure restricted to T^2 is proportional to |Delta_W|^2 where Delta_W = prod_{alpha>0} sin((alpha.theta)/2), i.e.:

     d(Haar) ~ |sin((t1-t2)/2) * sin((t1+2t2)/2) * sin((2t1+t2)/2)|^2 * dt1 dt2

   This vanishes at the identity (and all Weyl chamber walls), peaks at the Z_3 center.

### Numerical Results

| Quantity | Value |
|:---------|:------|
| Maximum location | (0, 0) = identity |
| Minimum location | (1.46*pi, 0.85*pi) |
| Contrast ratio (max/min) | 3.14 x 10^6 |
| Coefficient of variation | 3.04 |
| (0,0) Fourier fraction | 9.8% |
| |Delta|^2 at identity | 1.000 (normalized) |
| |Delta|^2 at Z_3 center (2pi/3, 2pi/3) | 0.125 |
| |Delta|^2 at (-1,-1,1) point (pi, pi) | 0.0013 |
| 1/e^2 radius from identity | 0.78 rad = 0.247*pi |
| Haar-weighted peak radius | 0.85 rad = 0.271*pi |
| S_3 Weyl symmetry error | 4.1 x 10^{-14} |

### Physical Interpretation

The condensate is **maximally concentrated at the identity element** of SU(3). This is a direct consequence of character coherence: all characters satisfy chi_{(p,q)}(identity) = dim(p,q), and the coherent sum Sum w_{(p,q)} * chi_{(p,q)} reaches its absolute maximum when all terms contribute with the same sign and maximum magnitude.

**Key structural facts:**

1. **The condensate is NOT uniform on the internal space.** The contrast ratio of 3 million means the Cooper pairs concentrate in a narrow region around the identity on SU(3). This breaks the naive expectation that a BCS condensate on a compact Lie group would spread uniformly.

2. **S_3 Weyl symmetry is exact.** Characters are class functions (constant on conjugacy classes), so the condensate on T^2 inherits the full Weyl group symmetry. This is verified to machine precision.

3. **Competition with Haar measure.** The Haar density vanishes at the identity (the Weyl denominator has a zero there), so the Haar-weighted condensate density peaks not at the identity but at r ~ 0.85 rad from it. The physically observable quantity -- the condensate integrated over an SU(3) volume element -- sees a shell-like structure.

4. **The (0,0) Fourier mode carries only 9.8% of the power.** The condensate is dominated by higher harmonics, confirming that it is far from uniform. The ratio |Delta|^2(identity)/|Delta|^2(Z_3) = 8:1 shows the condensate prefers the trivial Z_3 phase.

5. **The 1/e^2 radius of 0.25*pi defines a "condensate coherence patch" on SU(3).** Cooper pairs live predominantly within this angular distance of the identity on the maximal torus. This is approximately 1/8 of the torus period, placing the coherence scale at ~1/8 of the SU(3) diameter.

### Connection to Framework

The identity-peaked condensate has a Landau-theoretic interpretation. The BCS order parameter Delta(x) is a section of a vector bundle over SU(3). Its spatial profile on the internal manifold determines:

- **Which modes carry pairing weight**: modes near the identity (low PW quantum numbers) dominate. This is consistent with the B2 dominance finding (W1-1 through W1-3) -- the lowest-energy B2 modes sit in the (0,0) and low-(p,q) sectors, which are the ones with the largest character values near the identity.

- **Defect structure**: in the phonon-exflation transit, the condensate destruction (P_exc = 1.000, S38) produces quasiparticle excitations. The identity-peaked spatial profile means these excitations are born concentrated near the identity -- they are NOT uniformly distributed on SU(3).

- **Kibble-Zurek density**: the defect density after transit depends on the correlation length of the order parameter, which our 1/e^2 radius quantifies at 0.25*pi ~ pi/4. This is an O(1) fraction of the SU(3) scale -- the 0D limit (L/xi_GL = 0.031) means the condensate coherence patch covers the entire system.

### Files

- Script: `tier0-computation/s47_condensate_torus.py`
- Data: `tier0-computation/s47_condensate_torus.npz`
- Main plot: `tier0-computation/s47_condensate_torus.png`
- Analysis plot: `tier0-computation/s47_condensate_torus_analysis.png`
- Haar-weighted plot: `tier0-computation/s47_condensate_torus_haar.png`
- Character atlas: `tier0-computation/s47_condensate_torus_characters.png`

---

## W2-3: Spectral Landscape Figure (Spectral-Geometer)

### Gate: SPECTRAL-LANDSCAPE-47 (INFO)

Publication-quality figure showing the full 992-mode Dirac spectrum at the fold (tau = 0.19), annotated with sector structure, pi-phase topology, and BCS pairing.

### Method

1. **Classification**: All 992 eigenvalues from `s44_dos_tau.npz` grouped by PW degeneracy dim(p,q)^2 into 9 representations (p+q <= 3). Within each rep, eigenvalues sorted by magnitude and assigned to sectors by rank: lowest 2*dim -> B1 (trivial), next 8*dim -> B2 (U(2) fundamental), top 6*dim -> B3 (SU(2) adjoint).

2. **Density of states**: PW-weighted DOS rho_PW(omega) = sum_k dim_k^2 * delta(omega - omega_k) computed with Gaussian smoothing (sigma = 0.012), sector-decomposed into stacked area fill.

3. **Spectral strip**: Each eigenvalue plotted at its (|lambda|, rep) position, colored by sector, marker size proportional to sqrt(dim^2). The 13 pi-phase states marked with star symbols and labeled by (p,q) rep.

4. **BCS gap edges**: Quasiparticle gap 2*Delta_sector centered on sector Fermi energies sqrt(lam2_fold). B2 gap (2*Delta = 1.464) shown with shading and double-arrow annotation. B1 and B3 gaps shown with lighter shading.

5. **Sector decomposition inset**: Three horizontal stacked bars comparing B1/B2/B3 fractions across (a) total PW-weighted mode count, (b) pi-phase PW weight, (c) BCS v^2 pairing weight.

### Results

**Verified counts**:
- 992 total eigenvalues plotted (124 B1 + 496 B2 + 372 B3)
- 13 pi-phase annotations visible, colored by sector
- 3 sector colors distinguishable (Okabe-Ito palette: blue/vermillion/green)
- 12 van Hove singularities marked

**Sector decomposition** (the central visual result):

| Measure | B1 | B2 | B3 |
|:--------|:---|:---|:---|
| PW-weighted modes | 12.5% | 50.0% | 37.5% |
| Pi-phase PW weight | 11.5% | 61.8% | 26.7% |
| BCS v^2 pairing | 8.3% | 90.7% | 1.0% |

The progressive concentration from modes (50%) to topology (62%) to dynamics (91%) in B2 is the defining structural feature of the crystal. Topology selects B2 over the geometric baseline by a factor 62/50 = 1.24x; BCS dynamics amplifies this to 91/50 = 1.82x. The B3 sector, despite carrying 37.5% of PW-weighted modes, accounts for only 1% of pairing weight — a 37.5x suppression from V(B3,B3) = 0.003.

**BCS gap structure**: The B2 gap (2*Delta = 1.464 M_KK) spans from |lambda| = 0.113 to 1.577, encompassing all B1 and most B2 eigenvalues. The B1 gap (2*Delta = 0.744) and B3 gap (2*Delta = 0.168) are proximity-induced and intrinsic respectively.

**Spectral strip structure**: The eigenvalue distribution is highly non-uniform across representations. The (0,0) singlet (dim=1) contributes 16 modes in a narrow band [0.820, 0.971]. Higher reps spread across the full range [0.820, 2.061], with the (2,1) rep (dim=15) producing the densest coverage. The pi-phase states are distributed across 7 of the 9 reps, with the (2,1) rep hosting 5 of the 13 pi-phases.

### Files

- Script: `tier0-computation/s47_spectral_landscape.py`
- Data: `tier0-computation/s47_spectral_landscape.npz`
- Figure: `tier0-computation/s47_spectral_landscape.png` (300 dpi)
- Figure: `tier0-computation/s47_spectral_landscape.pdf`

---

## W2-2: Curvature Anatomy of Jensen-Deformed SU(3) (CURVATURE-ANATOMY-47)

**Agent**: Baptista-Spacetime-Analyst
**Gate**: CURVATURE-ANATOMY-47 (INFO — visualization task)

### Setup

Computed all 28 = C(8,2) sectional curvatures K(e_a, e_b; tau) for the Jensen-deformed left-invariant metric on SU(3), using the Riemann tensor infrastructure from `tier1_dirac_spectrum.py` (validated at 147/147 checks in r20a). The Jensen deformation decomposes su(3) = u(1) + su(2) + C^2 with scale factors L_1 = e^{2tau} (u(1), 1D), L_2 = e^{-2tau} (su(2), 3D), L_3 = e^{tau} (C^2, 4D).

The 28 pairs classify into 5 types: SU2-SU2 (3), SU2-C2 (12), C2-C2 (6), U1-SU2 (3), U1-C2 (4).

### Validation (3/3 PASS)

1. **R(0) = 2.0**: Scalar curvature at tau=0 matches bi-invariant value to |err| = 6.7e-16.
2. **Bi-invariant formula**: K(X,Y) = (1/4)|[X,Y]|^2 verified for all 28 pairs at tau=0 (max err = 8.3e-17).
3. **R cross-check at fold**: R(0.19) = 2.018143955851 matches s46_geometric_a2.npz to relative error 0.0e+00.

### Branch Structure at tau = 0 (bi-invariant metric)

SU(3) with bi-invariant metric is NOT a constant-curvature space (unlike SU(2) = S^3). At tau=0, the 28 sectional curvatures split into 4 distinct values:

| K value | Deg | Types | Exact fraction |
|:--------|:----|:------|:---------------|
| 0.0000 | 3 | U1-SU2 | 0 (commuting generators) |
| 0.0208 | 16 | C2-C2 + SU2-C2 | 1/48 |
| 0.0625 | 4 | U1-C2 | 1/16 |
| 0.0833 | 5 | C2-C2 + SU2-SU2 | 1/12 |

The K=0 branch exists because [u(1), su(2)] = 0 (these subalgebras commute within u(2)).

### Branch Structure at the Fold (tau = 0.19)

The Jensen deformation splits the 4 branches at tau=0 into 6 branches at the fold:

| K value | Deg | Type | Change from tau=0 |
|:--------|:----|:-----|:-------------------|
| 0.00000000 | 3 | U1-SU2 | 0 (protected, exact) |
| 0.00974305 | 12 | SU2-C2 | -0.0111 (flattening) |
| 0.03968411 | 4 | C2-C2 | +0.0189 (splitting from 0.0208) |
| 0.05892389 | 2 | C2-C2 | -0.0244 (splitting from 0.0833) |
| 0.06250000 | 4 | U1-C2 | 0.0000 (PROTECTED, exact) |
| 0.12185705 | 3 | SU2-SU2 | +0.0385 (steepening) |

**Anisotropy ratio**: K_max/K_min (positive) = 12.51 at fold (vs 4.0 at tau=0).
**No negative curvatures** at any tau in [0, 0.25].
**3 exactly flat directions** (U1-SU2) at all tau.

### Two Structural Theorems (new)

**Theorem 1 (U1-SU2 flatness)**: K(u(1), su(2)) = 0 exactly for all tau.

*Proof*: The u(1) generator lambda_8 commutes with all su(2) generators lambda_{1,2,3} in the Lie algebra su(3). The sectional curvature formula for a left-invariant metric on a Lie group gives K(X,Y) = R^X_{YYX}, which for commuting X,Y reduces to terms involving only the connection, not the structure constants directly. For the Jensen deformation, u(1) and su(2) both reside within u(2), and the metric scales each block independently without mixing. The connection coefficients Gamma^a_{bc} with a in su(2) and b,c being (u(1), su(2)) vanish identically due to the block structure, forcing K=0.

Verified numerically: K(lambda_i, lambda_8) = 0.000000000000 for i=1,2,3 at all 26 tau values (max deviation < 1e-15).

**Theorem 2 (U1-C2 curvature invariance)**: K(u(1), C^2) = 1/16 = 0.0625 exactly for all tau.

*Evidence*: K(lambda_j, lambda_8) = 0.062500000000 for j=4,5,6,7 at all 26 tau values spanning [0, 0.25], invariant to machine epsilon. The curvature of u(1)-C^2 planes is a Jensen-deformation invariant.

*Significance*: This invariant defines a protected energy scale in the KK tower. The u(1) direction (hypercharge) couples to the C^2 directions (off-diagonal generators) with a fixed geometric "spring constant" K = 1/16 regardless of modulus tau. Combined with the k7 charge conservation ([iK_7, D_K] = 0 at all tau), this provides a geometric anchor for the BCS pairing channel.

### Physical Interpretation

The "body plan" of the Jensen crystal consists of:

1. **Hard directions** (SU2-SU2, K = 0.122): The su(2) planes become more sharply curved under the Jensen deformation. This corresponds to the su(2) subgroup "stiffening" — it costs more curvature energy to bend in these directions.

2. **Protected directions** (U1-C2, K = 1/16 = const): The u(1)-C^2 planes maintain exactly constant curvature. This is a rigidity result — the hypercharge-coset coupling is geometrically fixed.

3. **Soft directions** (SU2-C2, K = 0.0097): The cross-coupling between su(2) and C^2 becomes very weak. These 12 planes carry the smallest positive curvature at the fold, representing the most "malleable" geometric directions.

4. **Flat directions** (U1-SU2, K = 0): Three exactly flat planes that never curve. These correspond to the exact commutativity within u(2).

5. **Splitting directions** (C2-C2): The C^2 internal curvature splits into two sub-branches (deg 4 and deg 2), reflecting the breaking of the full SU(3) symmetry into a U(2)-invariant structure by the Jensen deformation.

### Files

- Script: `tier0-computation/s47_curvature_anatomy.py`
- Data: `tier0-computation/s47_curvature_anatomy.npz`
- Figure: `tier0-computation/s47_curvature_anatomy.png`

---

## W3-1: Paasch Spiral Analysis of Full Dirac Spectrum (PAASCH-SPIRAL-47)

**Agent**: paasch-mass-quantization-analyst
**Gate**: PAASCH-SPIRAL-47

### Gate PAASCH-SPIRAL-47: FAIL

The phase distribution of the 120 unique Dirac eigenvalues on the Paasch logarithmic spiral is consistent with uniform at the fold (tau=0.19). No angular sequence structure is detected. Zero clusters found at the 2-sigma threshold.

### Method

The Paasch spiral maps masses onto a logarithmic spiral m(angle) = m_0 * exp(k * angle), where k = ln(phi)/(2*pi) = 0.06785 and phi = 1.53158 (from x = e^{-x^2}, Eq. 2g of Paasch 2009). One full turn of the spiral corresponds to multiplication by phi. If eigenvalues organize into discrete sequences, their phases (angle mod 2*pi) cluster at specific angular positions.

**Data**: 992 eigenvalues at max_pq_sum=3 from `s44_dos_tau.npz`, grouped into 120 unique magnitudes (tolerance 1e-8). Analysis performed at all 5 available tau values (0.00, 0.05, 0.10, 0.15, 0.19) and also at max_pq_sum=4 (255 unique eigenvalues from `s46_max_pq_sum_4.npz`).

**Spectral window limitation**: The spectrum spans [0.820, 2.061] at the fold, giving a ratio max/min = 2.514. On the Paasch spiral this covers only **2.16 turns** (778 degrees). Paasch's original analysis of the particle mass spectrum spans ~50+ turns (electron at 0 degrees to top quark). The Dirac spectrum probes a very narrow angular window.

### Statistical Tests at Fold (tau=0.19, 120 unique eigenvalues)

| Test | Statistic | p-value | Interpretation |
|:-----|:----------|:--------|:---------------|
| Rayleigh (unweighted) | R_bar = 0.0544 | 0.702 | No unimodal clustering |
| Rayleigh (PW-weighted) | R_bar = 0.1401 | 0.228 | No unimodal clustering |
| KS vs. uniform | D = 0.0570 | 0.808 | Consistent with uniform |
| Watson U^2 | U^2 = 0.0562 | -- | Low (uniform) |
| Harmonic h=2 | R = 0.0666 | 0.589 | No 2-fold clustering |
| Harmonic h=3 | R = 0.0249 | 0.929 | No 3-fold clustering |
| Harmonic h=4 | R = 0.0567 | 0.681 | No 4-fold clustering |
| Harmonic h=6 | R = 0.0510 | 0.732 | No 6-fold clustering |
| Harmonic h=8 | R = 0.0622 | 0.629 | No 8-fold clustering |
| Angular clustering (36 bins, 2-sigma) | -- | -- | **0 clusters** |

No test rejects uniformity at p < 0.01. No test rejects uniformity at p < 0.05.

### Evolution with tau

| tau | n_unique | Spiral turns | Rayleigh p (unweighted) | KS p | n_clusters |
|:----|:---------|:-------------|:------------------------|:-----|:-----------|
| 0.00 | 16 | 1.81 | 0.849 | 0.549 | 1 |
| 0.05 | 120 | 1.89 | 0.289 | **0.019** | 2 |
| 0.10 | 120 | 1.97 | 0.369 | 0.205 | 3 |
| 0.15 | 120 | 2.08 | 0.528 | 0.312 | 1 |
| 0.19 | 120 | 2.16 | 0.702 | 0.808 | 0 |

The tau=0.05 point shows marginal KS rejection (p=0.019) and significant h=4 harmonic Rayleigh (p=2.1e-5). This transient structure at early deformation disappears entirely by the fold. The h=4 significance at tau=0.05 corresponds to approximate 4-fold angular symmetry in the phase distribution at that particular deformation parameter, but it does not survive increasing Jensen deformation.

### 45-Degree Bin Counts (Paasch Sequences S1-S6)

Paasch's framework predicts 6 principal sequences at 45-degree angular separation. At the fold (tau=0.19):

| Bin | Count | Ratio to uniform |
|:----|:------|:-----------------|
| [0-45) | 17 | 1.13 |
| [45-90) | 14 | 0.93 |
| [90-135) | 13 | 0.87 |
| [135-180) | 15 | 1.00 |
| [180-225) | 20 | 1.33 |
| [225-270) | 16 | 1.07 |
| [270-315) | 13 | 0.87 |
| [315-360) | 12 | 0.80 |

Maximum deviation from uniform: the [180-225) bin at 1.33x. This is well within Poisson fluctuations (expected sigma for 15 counts = 3.9, so 20 is a 1.3-sigma upward fluctuation). No evidence for preferential alignment with 45-degree sequence positions.

### Phi Ratio Pair Counting

Pairs where lambda_j/lambda_i is within 1% of phi = 1.53158:

| | Count |
|:--|:------|
| Observed | 109 |
| Expected (random uniform) | 158.2 +/- 15.3 |
| Z-score | **-3.20** |

The observed count is **below** random expectation by 3.2 sigma. The Dirac spectrum has *fewer* phi-ratio pairs than a random uniform spectrum with the same range, not more. This is an anti-correlation: eigenvalues are not randomly distributed but are *avoiding* phi-ratio relationships.

The deficit occurs because the Dirac eigenvalues cluster more tightly (most NN ratios are near 1.00-1.01) than a uniform distribution over the same range. The nearest-neighbor ratios have:
- Range: [1.000055, 1.0965]
- Mean: 1.0078
- NN ratios within 1% of phi: **0/119**
- NN ratios within 5% of phi: **0/119**

No nearest-neighbor pair achieves a ratio anywhere close to phi. The eigenvalues are spaced too densely for phi-ratio structure to appear in adjacent pairs.

### Extended Spectrum (max_pq_sum=4, 255 unique eigenvalues)

The s46 data provides 2912 eigenvalues (255 unique) spanning [0.820, 2.431], covering 2.55 turns:

| Test | Value | p-value |
|:-----|:------|:--------|
| Rayleigh | R_bar = 0.0887 | 0.135 |
| KS | D = 0.0528 | 0.459 |
| Clusters (2-sigma) | 1 cluster at 325 deg | -- |

The larger spectrum also fails to show significant structure. The single cluster at 325 degrees is borderline (the bin count barely exceeds the 2-sigma threshold) and is not reproduced at max_pq_sum=3.

### Sector Cross-Reference

The 13 pi-phase states (from W1-1) map onto the spiral as follows:

| Rep | Sector | |lambda| | Phase (deg) | Turn |
|:----|:-------|:--------|:------------|:-----|
| (1,0) | B2 | 1.075 | 229.1 | 0.636 |
| (0,1) | B2 | 1.078 | 231.6 | 0.643 |
| (2,1) | B1 | 1.366 | 71.1 | 1.198 |
| (0,2) | B2 | 1.370 | 73.5 | 1.204 |
| (1,1) | B2 | 1.386 | 83.6 | 1.232 |
| (2,1) | B2 | 1.428 | 108.7 | 1.302 |
| (2,0) | B2 | 1.430 | 110.1 | 1.306 |
| (2,1) | B2 | 1.469 | 132.7 | 1.369 |
| (2,1) | B2 | 1.597 | 202.9 | 1.564 |
| (2,1) | B3 | 1.723 | 267.5 | 1.743 |
| (0,3) | B2 | 1.759 | 284.8 | 1.791 |
| (0,3) | B3 | 1.792 | 300.2 | 1.834 |
| (3,0) | B3 | 1.819 | 313.1 | 1.870 |

The pi-phase states span turns 0.6 to 1.9 (just over one full turn) and do not cluster at common angular positions. Their phases span [71-313] degrees -- almost the full circle. This rules out the possibility that the topologically interesting states form a Paasch sequence.

### Assessment

**The Dirac spectrum on Jensen-deformed SU(3) does not exhibit Paasch sequence structure.** This is a clean negative result with three independent lines of evidence:

1. **No angular clustering**: All statistical tests (Rayleigh, KS, Watson, harmonic Rayleigh) fail to reject uniformity at the fold. Zero clusters detected.

2. **Anti-correlated phi-ratio pairs**: The spectrum has 3.2-sigma *fewer* phi-ratio pairs than random, not more. Eigenvalues are too densely packed (NN ratios ~1.008) for the phi=1.53 ratio to appear between adjacent levels.

3. **Structure disappears with deformation**: The marginal structure at tau=0.05 (h=4 Rayleigh p=2.1e-5) vanishes completely by the fold (tau=0.19). Whatever 4-fold symmetry exists at early deformation is a feature of the bi-invariant limit (tau=0.00 has exact SU(3) symmetry producing highly degenerate eigenvalues), not of the Jensen crystal.

**Why the single phi ratio survives while the sequences do not**: The S12 result phi_paasch = m_{(3,0)}/m_{(0,0)} = 1.531580 at tau=0.15 is REAL -- it is the ratio of the highest to lowest eigenvalue in the (0,0) singlet sector. This ratio emerges from the specific structure of the Jensen deformation on the 16-dimensional spinor space at the (0,0) Peter-Weyl level. But it is a property of ONE sector (the trivial representation) acting on the spinor module, not a global organizing principle for the full Dirac spectrum across all PW sectors. The phi ratio is a structural fact about the (0,0) B3/B1 gap, not evidence for logarithmic mass quantization across the entire eigenvalue spectrum.

**Connection to Paasch's original analysis**: Paasch's particle mass spectrum spans ~50 turns of the spiral covering 10 orders of magnitude (electron to Planck mass). The Dirac spectrum at max_pq_sum=3 covers only 2.16 turns over 0.4 orders of magnitude. Even if the particle mass spectrum genuinely organizes into Paasch sequences, one would not necessarily expect the same structure to appear in a 2-turn window of eigenvalues produced by a single compact operator. The test is conclusive at this truncation but silent about the broader mass spectrum phenomenology.

### Files

- Script: `tier0-computation/s47_paasch_spiral.py`
- Data: `tier0-computation/s47_paasch_spiral.npz`
- Plot: `tier0-computation/s47_paasch_spiral.png`

---

## W3-2: BdG-Dressed Phi Ratio Across Tau (PHI-BDG-47)

**Agent**: paasch-mass-quantization-analyst
**Gate**: PHI-BDG-47

### Gate PHI-BDG-47: FAIL

BCS dressing destroys the phi ratio. The dressed inter-sector ratio R_dressed never reaches phi_paasch = 1.53158 at any tau in [0.025, 0.40], in all three gap-assignment scenarios tested. Maximum R_dressed = 1.465 (Scenario C), 7.6 sigma below phi.

### Provenance Correction

**W3-1 (line 624) contained an error**: it described the phi ratio as "the ratio of the highest to lowest eigenvalue in the (0,0) singlet sector." This is wrong. The phi ratio is INTER-SECTOR:

    R = min|lambda_{(3,0)}| / min|lambda_{(0,0)}| = 1.261834 / 0.823873 = 1.531588

at tau = 0.15, matching phi_paasch to 5.3 ppm. The intra-(0,0) ratio B3/B1 at the same tau is only 1.1475 -- nowhere near phi.

The (3,0) and (0,0) sectors are decoupled by the block-diagonal theorem (S22b). Under BCS, they receive independent gap dressing.

### Method

The BdG quasiparticle energy is E_qp = sqrt(lambda^2 + Delta^2), with mu = 0 forced by PH symmetry. The inter-sector dressed ratio is:

    R_dressed = sqrt(lam_{30}^2 + Delta_{30}^2) / sqrt(lam_{00}^2 + Delta_{00}^2)

Three gap-assignment scenarios for the (3,0) sector:

| Scenario | Delta_(3,0) | Physical basis |
|:---------|:------------|:---------------|
| A | 0 (undressed) | No pairing in (3,0) |
| B | Delta_B3 ~ 0.084 | s45 heuristic (Casimir-matched) |
| C | Delta_B1 ~ 0.372 | Equal to (0,0) gap (upper bound) |

The (0,0) B1 eigenvalue always receives Delta_B1 ~ 0.372 (the dominant gap). Since Delta_B1 >> Delta_B3, the denominator grows much more than the numerator, pulling R_dressed below R_bare.

**Data sources**: (3,0) eigenvalues from s44_dos_tau.npz (5 tau points, cubic-spline interpolated to 60-point grid). (0,0) eigenvalues from s46_qtheory_selfconsistent.npz (20-point interpolation). BCS gaps from s46 self-consistent solution on 60-point grid. Cross-check: s44 and s46 (0,0) B1 eigenvalues agree to 2.7e-4 in the interpolation range.

### Results

#### Bare ratio R_bare(tau) = min|lambda_{(3,0)}| / min|lambda_{(0,0)}|

| tau | min|(3,0)| | min|(0,0)| | R_bare | Deficit from phi |
|:----|:-----------|:-----------|:-------|:-----------------|
| 0.00 | 1.32288 | 0.86603 | 1.527525 | +0.26% |
| 0.05 | 1.30091 | 0.84702 | 1.535873 | -0.28% |
| 0.10 | 1.28051 | 0.83307 | **1.537088** | -0.36% (maximum) |
| 0.15 | 1.26183 | 0.82387 | **1.531588** | -0.0005% (5 ppm) |
| 0.19 | 1.24826 | 0.81974 | 1.522754 | +0.57% |

The bare ratio peaks near tau ~ 0.10 and crosses phi downward at **tau = 0.150** (linear interpolation from data points). This confirms the S12 finding.

#### Dressed ratios at tau = 0.15

| Quantity | Value |
|:---------|:------|
| lambda_(0,0) B1 | 0.82329 |
| lambda_(3,0) min | 1.26033 |
| Delta_B1 (for 0,0) | 0.37136 |
| Delta_B3 (for 3,0) | 0.08405 |
| R_bare | 1.5308 |
| R_dressed_A (30 undressed) | 1.3954 (shift -8.8%) |
| R_dressed_B (30 = Delta_B3) | 1.3985 (shift -8.6%) |
| phi_paasch | 1.53158 |

#### Maximum dressed ratios across full tau range

| Scenario | Max R_dressed | At tau | Deficit from phi |
|:---------|:--------------|:-------|:-----------------|
| A (undressed) | 1.4121 | 0.025 | 7.8% |
| B (Delta_B3) | 1.4148 | 0.025 | 7.6% |
| C (Delta_B1) | 1.4652 | 0.025 | 4.3% |

No scenario crosses phi at any tau. The maximum dressed ratio occurs at the SMALLEST tau (weakest deformation), not near the fold. BCS dressing pushes the ratio away from phi everywhere.

#### Gap ratio sensitivity

To maintain R_dressed = phi at tau = 0.15 would require Delta_(3,0) = 0.570, which is 6.78x the actual Delta_B3 and 1.535x Delta_B1. The required ratio Delta_(3,0)/Delta_B1 = 1.535 is remarkably close to phi itself (1.532), but there is no known mechanism to generate such a gap in the decuplet sector. The (3,0) sector's own BCS channel has not been computed from first principles -- the Delta_B3 assignment is heuristic.

### Assessment

**BCS dressing categorically destroys the phi ratio.** The mechanism is straightforward: the (0,0) singlet has the strongest BCS gap (Delta_B1 = 0.372) because it sits at the van Hove gap edge. The (3,0) decuplet, 28% higher in energy, has a much weaker gap (Delta_B3 ~ 0.084 heuristic). The asymmetric gap dressing inflates the denominator relative to the numerator by ~9%.

Three independent features conspire against phi:

1. **Gap hierarchy**: Delta_B1/Delta_B3 = 4.4 (the gap edge has 4x more pairing than the band interior). This is structural -- it follows from the V matrix selection rules and the DOS profile.

2. **Block-diagonal isolation**: The (0,0) and (3,0) sectors cannot share a gap through cross-sector pairing. Each runs its own independent BCS channel. There is no mechanism to equalize their gaps.

3. **Energy ordering**: The (3,0) eigenvalues are ABOVE the (0,0) eigenvalues. In BCS, higher-energy modes get weaker pairing (further from the gap edge). This reinforces the gap asymmetry.

**Structural interpretation**: The 5 ppm phi match at tau = 0.15 is a property of the BARE Dirac spectrum -- the geometry of Jensen-deformed SU(3) acting on the spinor module through the Peter-Weyl decomposition. It belongs to the single-particle Hamiltonian, not to the many-body ground state. Once the BCS condensate forms, the relevant excitations are Bogoliubov quasiparticles, not bare eigenvalues, and the phi relationship is lost.

This does not diminish the mathematical interest of the bare result (5 ppm is remarkable for a ratio between irrep sectors), but it means the phi ratio cannot be a physical observable of the BCS-dressed crystal. The bare Dirac spectrum at tau = 0.15 produces a geometric coincidence; the many-body physics at the fold does not preserve it.

### Files

- Script: `tier0-computation/s47_phi_bdg.py`
- Data: `tier0-computation/s47_phi_bdg.npz`
- Plot: `tier0-computation/s47_phi_bdg.png`

---

## W3-3: Deformation Response of Character Coherence (COHERENCE-RESPONSE-47)

**Agent**: nazarewicz-nuclear-structure-theorist
**Gate**: COHERENCE-RESPONSE-47

### Pre-registered predictions

**Null (artifact)**: r_C approximately constant across tau. Characters are tau-independent, so the identity peak is kinematic. BCS weights modulate weakly.

**Alternative (substrate)**: r_C tracks 1/Delta_B2(tau). Wider coherence when pairing weaker, narrower when stronger.

**Decisive criterion**: |r| > 0.9 between r_C and Delta_B2 -> SUBSTRATE. |r| < 0.3 -> ARTIFACT. Between -> AMBIGUOUS.

### Method

The coherence function on T^2 restricted to the radial cut (theta_1 = theta, theta_2 = 0):

C(theta; tau) = [Sum_{(p,q)} w_{(p,q)}(tau) * |chi_{(p,q)}(theta, 0)|^2] / [Sum_{(p,q)} w_{(p,q)}(tau) * dim(p,q)^2]

where C(0; tau) = 1 by construction.

**Characters are tau-INDEPENDENT.** The SU(3) characters chi_{(p,q)}(theta_1, theta_2) on T^2 are fixed by the group -- they do not depend on the Jensen deformation parameter tau. All 9 reps with p+q <= 3 computed once via the Weyl character formula, verified at identity: chi_{(p,q)}(0,0) = dim(p,q) to machine epsilon.

**Weights are tau-DEPENDENT.** At each of 60 self-consistent tau values from `s46_qtheory_selfconsistent.npz`:

w_{(p,q)}(tau) = [Sum_s frac_s * v_s(tau) * Delta_s(tau)]^2

where frac_s = {2/16, 8/16, 6/16} for B1, B2, B3; the BCS occupations v_s^2 = (1/2)(1 - sqrt(lam2_s) / sqrt(lam2_s + Delta_s^2)); and a rep-dependent energy scaling factor eps^2_{(p,q)} = lam2_s * R_{(p,q)} with R_{(p,q)} calibrated from 5-point s44_dos_tau.npz spectrum (R ranges from 1.000 for (0,0) to 4.825 for (0,3)).

The 1/e^2 radius r_C(tau) is extracted at each tau by linear interpolation where C(theta; tau) drops to e^{-2} = 0.135.

### Results

**r_C is effectively constant: r_C = 0.9192 +/- 0.0003 rad (CV = 0.036%)**

| Quantity | Value |
|:---------|:------|
| r_C mean | 0.9192 rad (0.2926 pi) |
| r_C range | [0.91898, 0.92034] rad |
| r_C total variation | 0.00136 rad |
| CV(r_C) | 0.000362 (0.036%) |
| Delta_B2 range | [0.6956, 0.7320] |
| Delta_B2 total variation | 0.0365 (5.02%) |
| r(r_C, Delta_B2) | -0.9996 (p = 2.2e-92) |
| r(r_C, 1/Delta_B2) | +0.9993 (p = 1.5e-84) |
| Spearman rho | 0.9815 (p = 2.5e-43) |
| Elasticity d(ln r_C)/d(ln Delta_B2) | 0.030 |
| Uniform-weight control r_C | 0.8730 rad |
| BCS static shift | +0.0462 rad (+5.3%) |
| Contrast range | [107.8, 109.4] |
| Contrast CV | 0.0036 |

### Decomposition

The coherence radius decomposes into three parts:

| Component | Value (rad) | Fraction of r_C |
|:----------|:------------|:----------------|
| Geometric (character truncation) | 0.8730 | 95.0% |
| BCS static shift (tau-independent) | 0.0462 | 5.0% |
| BCS dynamic variation (tau-dependent) | +/- 0.0012 | 0.13% |

The character truncation at p+q <= 3 determines 95% of the coherence width. The BCS pairing shifts r_C by +5.3% (making the peak slightly wider than the uniform-weight control), but this shift is the SAME for all tau. The tau-dependent BCS variation is 0.13% of r_C.

### Gate Verdict: ARTIFACT

**The raw |r| = 0.9996 mechanically passes the SUBSTRATE threshold.** However, this is a pathological case where both r_C(tau) and Delta_B2(tau) have smooth parabolic profiles peaking near the fold, and the Pearson correlation measures shape agreement, not amplitude. The 0.036% CV simultaneously passes the CONSTANT threshold.

**The elasticity resolves the tension.** d(ln r_C)/d(ln Delta_B2) = 0.030 means the coherence radius responds at 3% of the gap variation rate. A 5% change in Delta_B2 produces a 0.15% change in r_C. This is a perturbative correction to a geometrically rigid observable, not a dynamically determined response.

**Nuclear analogy (Paper 03, Section IV).** This is the charge radius problem: r_charge correlates with neutron number at |r| > 0.99, but the variation per neutron is 0.1%. The radius is determined by the liquid-drop term (A^{1/3}), with shell corrections providing perfectly correlated but negligible wiggles. Here:

- A^{1/3} term = character truncation (95.0%)
- Static shell correction = BCS occupation shift (5.0%)
- Dynamic shell correction = tau-dependent BCS modulation (0.13%)

**The coherence width is a property of the truncated Peter-Weyl basis, not of the BCS condensate.**

### Self-correction

The pre-registered gate was poorly designed. It tested correlation (shape agreement) without testing amplitude (how much does r_C actually move). The correct test would have been:

- SUBSTRATE: elasticity > 0.5 (r_C responds proportionally to Delta_B2)
- ARTIFACT: elasticity < 0.1 (r_C barely responds)

By this correct criterion: elasticity = 0.030 -> ARTIFACT with wide margin.

I designed this test in the substrate reframe document. The result falsifies my own prediction that "r_C tracks 1/Delta_B2." It does track it -- but only at the 0.13% level. The tracking is a perturbative correction to a geometrically rigid coherence width. The null hypothesis (artifact) is the correct interpretation.

### What this constrains

This result closes one direction of the substrate-vs-artifact question for coherence on T^2:

1. The 1/e^2 radius is 95% geometric (character truncation at p+q <= 3)
2. BCS pairing provides a tau-independent 5% widening (static) and a 0.13% tau-dependent modulation (dynamic)
3. The coherence pattern is NOT a substrate diagnostic -- it is a truncation artifact with a perturbative BCS correction
4. Adding more reps (p+q > 3) would change r_C by O(5%), confirming its truncation dependence

The coherence radius cannot distinguish the BCS ground state from any other state that has the same sector fractions. It is insensitive to the pairing amplitude.

### Files

- Script: `tier0-computation/s47_coherence_response.py`
- Data: `tier0-computation/s47_coherence_response.npz`
- Plot: `tier0-computation/s47_coherence_response.png` (6-panel diagnostic)
- Plot: `tier0-computation/s47_coherence_response_contrast.png`

---

## W3-4: Superfluid Density Tensor on Jensen-Deformed SU(3) (RHOS-TENSOR-47)

**Agent**: Landau-Condensed-Matter-Theorist
**Gate**: RHOS-TENSOR-47

### Gate RHOS-TENSOR-47: PASS

- Eigenvalue variation across tau: 163.7% (threshold: >10%)
- Anisotropy at fold: 24.4 (threshold: >5)

### Motivation

W3-3 showed that the character coherence function on T^2 is 95% truncation-determined (CV = 0.036%). The user's "near are like" intuition requires a RESPONSE function -- how the system responds to perturbation, not what it looks like in a basis expansion. The superfluid density tensor rho_s^{ab} is the canonical response function for condensate rigidity: the second derivative of the BCS free energy with respect to gauge phase twists in each of the 8 su(3) directions.

### Method

The Dirac operator on the (0,0) singlet sector is D = Omega(tau), the 16x16 spin connection offset. Under a gauge twist q_a in su(3) direction a:

D(q) = Omega + i * sum_a q_a * gamma_a

The superfluid density tensor is:

rho_s^{ab} = d^2 F_BCS / dq_a dq_b |_{q=0}

Computed by central finite differences on the sector-traced BCS energy (mean |eigenvalue| within each degenerate sector B1/B2/B3), which avoids level-crossing artifacts from degeneracy splitting. Convergence verified to 1e-5 relative error between dq=1e-4 and dq=5e-5. Normal state (Delta=0) gives rho_s = 0 identically (PASS).

Self-consistent BCS gaps from s46_qtheory_selfconsistent.npz at each tau. 16 tau values from 0.03 to 0.40.

### Current Operator Structure

The current operators J_a = -gamma_a in the Dirac eigenbasis have a clean selection-rule structure dictated by the reductive decomposition su(3) = u(1) + su(2) + C^2:

| Direction type | B1-B1 | B1-B2 | B1-B3 | B2-B2 | B2-B3 | B3-B3 |
|:---------------|:------|:------|:------|:------|:------|:------|
| su(2) (a=0,1,2) | 0 | 0 | 1.414 | 2.828 | 0 | 2.000 |
| C^2 (a=3,4,5,6) | 0 | 1.414 | 0 | 0 | 2.449 | 0 |
| u(1) (a=7)       | 1.414 | 0 | 0 | 2.828 | 0 | 2.449 |

Key structure: su(2) generators connect B1<->B3 and are diagonal on B2, B3. C^2 generators connect B1<->B2 and B2<->B3 exclusively. u(1) is purely diagonal. This is the representation-theoretic consequence of the reductive decomposition.

### Results at Fold (tau = 0.19)

The tensor is DIAGONAL in the su(3) decomposition basis with three distinct eigenvalues:

| Direction type | rho_s^{aa} | Degeneracy |
|:---------------|:-----------|:-----------|
| C^2            | 7.962      | 4          |
| su(2)          | 0.505      | 3          |
| u(1)           | 0.327      | 1          |

Anisotropy ratios:
- C^2 / u(1) = **24.4x**
- C^2 / su(2) = **15.8x**

The condensate is overwhelmingly stiff in the C^2 directions (the coset space SU(3)/U(2)) and relatively compliant in the u(1) and su(2) directions. This has a transparent physical interpretation: the C^2 generators connect B1<->B2 and B2<->B3, which are the inter-sector pairings that carry the BCS condensation energy. Twisting the phase in these directions disrupts the inter-sector coherence, costing large energy. The su(2) and u(1) generators are within-sector or connect B1<->B3 (weakly paired), so the condensate barely responds.

### Tau Dependence

| tau | rho_su2 | rho_C2 | rho_u1 | Tr(rho_s) | Anisotropy |
|:----|:--------|:-------|:-------|:----------|:-----------|
| 0.03 | 0.508 | 20.00 | 0.170 | 82.2 | 107 |
| 0.05 | 0.527 | 14.99 | 0.222 | 61.7 | 68 |
| 0.10 | 0.534 | 10.02 | 0.262 | 42.0 | 38 |
| 0.19 | 0.505 | 7.96  | 0.327 | 33.7 | 24 |
| 0.25 | 0.459 | 7.46  | 0.356 | 31.6 | 21 |
| 0.35 | 0.352 | 6.82  | 0.369 | 28.7 | 18 |

- **Max direction CV: 40.2%** (C^2 directions)
- **Max range/mean: 163.7%** (C^2 directions)
- Comparison: W3-3 artifact CV = 0.036%. The rho_s variation is **1116x** the artifact.

The C^2 stiffness drops monotonically from 20 to 6.8 across the sweep (factor 2.9), while su(2) shows a non-monotonic peak near tau=0.10. The u(1) direction grows monotonically. The anisotropy itself decreases from 107 at tau=0.03 to 18 at tau=0.40 -- the condensate becomes more isotropic as the fold is approached and passed.

### Curvature Cross-Reference

Pearson correlation between per-direction average sectional curvature K and rho_s diagonal:

**r = -0.906 (p = 0.002)**

This is a strong ANTI-correlation: directions with HIGH geometric curvature have LOW superfluid stiffness, and vice versa. The C^2 directions have the LOWEST average curvature (K=0.033) but the HIGHEST stiffness (rho_s=7.96). The su(2) directions have the HIGHEST average curvature (K=0.040) but low stiffness (rho_s=0.50).

Physical interpretation: The condensate is RIGID where the geometry is COMPLIANT, and SOFT where the geometry is CURVED. This is the opposite of the naive "stiffness follows curvature" expectation. The condensate fills the soft geometric directions, precisely because those are the directions where the inter-sector BCS pairing acts through the C^2 generators. The curved su(2) directions, being within the stabilizer U(2), do not participate in the dominant B1-B2 and B2-B3 pairing channels.

This anti-correlation IS the "near are like" mechanism in a response-function language: the BCS condensate dynamically selects the geometrically soft C^2 directions as its principal stiffness axes, creating a highly anisotropic superfluid that reinforces the coset structure SU(3)/U(2).

### Assessment

This is a genuine response-function diagnostic, not a truncation artifact. Three pieces of evidence:

1. **Normal state gives zero identically**: Delta=0 produces rho_s=0 to machine precision. The signal is entirely from the condensate.

2. **Variation 1116x the artifact**: CV=40% vs W3-3's 0.036%. The tau dependence is dynamical, driven by the self-consistent BCS gaps.

3. **Curvature anti-correlation at p=0.002**: The stiffness pattern is not random but systematically anti-correlated with geometric curvature -- a structural result that follows from the selection rules of the current operators.

The 24x anisotropy at the fold (C^2/u(1)) is a quantitative prediction of the framework. Any microscopic mechanism producing BCS pairing on Jensen-deformed SU(3) must produce a superfluid density tensor with this specific 3-eigenvalue structure (degeneracies 4, 3, 1) and this order of magnitude of anisotropy.

### Files

- Script: `tier0-computation/s47_rhos_tensor.py`
- Data: `tier0-computation/s47_rhos_tensor.npz`
- Plot: `tier0-computation/s47_rhos_tensor.png` (3-panel: stiffness vs tau, anisotropy at fold, scatter vs curvature)

---

## W4-2: Anisotropic Non-Singlet Dissipation (ANISO-DISSIP-47)

**Agent**: landau-condensed-matter-theorist
**Gate**: ANISO-DISSIP-47

### Gate ANISO-DISSIP-47: INFO

- **PASS** threshold: shortfall < 2.0x
- **INFO** threshold: 2.0x < shortfall < 3.8x
- **FAIL** threshold: shortfall >= 3.8x
- **Result (strict)**: shortfall = 3.76x (unchanged from S46)
- **Result (generous screening bound)**: shortfall = 2.22x at fold, 1.85x at tau = 0.40

### Background

S46 W4-5 computed non-singlet LZ dissipation isotropically: gamma_LZ_ns = 564.74 M_KK, shortfall 3.76x from gamma_needed = 2120.94 M_KK. The W3-4 rho_s tensor shows 24x anisotropy (C^2 = 7.96, su(2) = 0.50, u(1) = 0.33). This computation tests whether direction-dependent weighting modifies the friction.

### Three Structural Theorems

**Theorem 1 (Block-Diagonality of dH/dtau):**
The perturbation dH/dtau = i * dOmega/dtau from the Jensen modulus has ZERO inter-sector matrix elements:

| Sector pair | ||dH/dtau||^2 |
|:------------|:-------------|
| B1-B1 | 0.0094 |
| B2-B2 | 3.5612 |
| B3-B3 | 2.7361 |
| B1-B2, B1-B3, B2-B3 | < 10^{-28} |

All LZ transitions are INTRA-SECTOR. The inter-sector fraction is < 10^{-28}. This is a consequence of the Jensen deformation preserving the left-invariant metric structure.

**Theorem 2 (Clifford Order):**
dOmega/dtau is pure order-3 in the Clifford algebra (100% in gamma_i gamma_j gamma_k). It has ZERO projection onto single current operators J_a = gamma_a, because order-1 and order-3 Clifford elements are orthogonal by the trace formula Tr(gamma_a * gamma_i gamma_j gamma_k) = 0.

Order-3 direction decomposition:
- su(2)-su(2)-su(2): 69.6% (gamma_012 volume form)
- C^2-C^2-u(1): 21.7% (gamma_{34}7, gamma_{56}7)
- C^2-C^2-su(2): 8.8% (mixed terms)

**Theorem 3 (Schur Isotropic Casimir):**
For any SU(3) irreducible representation (p,q), Tr(T_a^2) = I(p,q) for all a = 1,...,8, where I(p,q) = dim(p,q) * C2(p,q) / 8 is the Dynkin index. Each of the 8 generators contributes C2/8 to the quadratic Casimir. The effective BCS gap is INDEPENDENT of rho_s anisotropy for all non-singlet modes: Delta_eff = Delta_0 regardless of representation.

### Physical Consequence

Combining Theorems 1-3: the 24x anisotropy of rho_s^{ab} (which measures inter-sector gauge stiffness) is STRUCTURALLY DECOUPLED from the LZ dissipation (which involves intra-sector transitions). The S46 isotropic computation stands as the correct result.

Key observations from the current operator structure:
- C^2 generators: ZERO intra-sector norms (purely inter-sector)
- su(2) generators: zero on B1, nonzero on B2 and B3
- u(1) generator: nonzero on all sectors

The 24x anisotropy lives entirely in the INTER-SECTOR channel, which is orthogonal to the intra-sector LZ transitions driven by dH/dtau.

### Generous Upper Bound (Screening)

A secondary effect: quasiparticle creation requires screening of the created current. By Jensen's inequality, the anisotropic screening cost <1/rho_s> = 1.188 exceeds the isotropic value 1/<rho_s> = 0.237 by a factor of 5.0. This adds screening energy delta_E = (1/2) * omega_k^2 * (<1/rho_s> - 1/rho_iso) to each excitation.

IF all screening energy is dissipated (generous assumption), the enhancement is 1.695x at the fold, reducing shortfall from 3.76x to 2.22x. This is still INFO, not PASS.

### Tau Sweep Sensitivity

| tau | Jensen ratio | Enhancement | Shortfall |
|:----|:-------------|:------------|:----------|
| 0.03 | 15.13 | 1.925 | 1.95 |
| 0.10 | 6.44 | 1.759 | 2.14 |
| 0.19 | 5.00 | 1.695 | 2.22 |
| 0.30 | 5.00 | 1.775 | 2.12 |
| 0.40 | 5.76 | 2.034 | 1.85 |

Best-case: shortfall = 1.85x at tau = 0.40 (early transit, larger anisotropy). Even generously, the screening correction alone does not close the gap at the fold where the transition matters.

### Constraint Map Update

The n_s shortfall of 3.76x is a STRUCTURAL feature of the intra-sector LZ dissipation, not an approximation error from isotropic averaging. The 24x superfluid anisotropy cannot couple to it because:
1. The perturbation (dH/dtau) is block-diagonal
2. The perturbation is orthogonal to single-direction currents
3. The effective gap is isotropic by Schur's lemma

This CONSTRAINS future resolution strategies: the n_s gap must be closed by mechanisms that increase either (a) the NUMBER of LZ transitions (transition probabilities P_k), or (b) the INTER-SECTOR coupling (currently zero for dH/dtau). Direction-dependent weighting within the current framework is structurally excluded.

### Files

- Script: `tier0-computation/s47_aniso_dissip.py`
- Data: `tier0-computation/s47_aniso_dissip.npz`
- Plot: `tier0-computation/s47_aniso_dissip.png` (6-panel: anisotropy, block-diag, Clifford, enhancement, shortfall, current norms)

---

## W4-3: BdG Spectral Flow and n_s (SPECTRAL-FLOW-NS-47)

**Author**: Volovik (Superfluid Universe Theorist)
**Date**: 2026-03-16

### Gate Pre-Registration

SPECTRAL-FLOW-NS-47:
- PASS: n_s in [0.93, 0.99]
- INFO: k-dependent flow (alpha != 0) but n_s outside [0.93, 0.99]
- FAIL: k-independent flow (alpha ~ 0) or mechanism structurally inapplicable

### Mechanism

This computation tests whether ADIABATIC SPECTRAL FLOW of BdG levels during tau evolution can produce a primordial perturbation spectrum. This is distinct from pair creation (all prior n_s routes). As tau evolves through the q-theory potential well, the BdG spectrum E_k(tau) = sqrt(omega_k(tau)^2 + Delta_sector(tau)^2) changes continuously. If the flow rate dE_k/dtau is k-dependent, the GGE relic inherits a k-dependent occupation spectrum. That IS the primordial perturbation spectrum.

In 3He-A (Paper 09), spectral flow through the Fermi point produces the chiral anomaly: dN/dt = N_3 x rate. The framework has N_3 = 0 (BDI class, Paper 28) and a GAP, not a Fermi point. The question is whether gap-edge spectral flow carries spectral weight information even without topological protection.

### Results

**Step 1: BdG quasiparticle energies E_k(tau)**

Three-sector representative energies computed at 60 tau points:

| Sector | E(tau=0.025) | E(tau=0.19) | E(tau=0.40) | Variation |
|:-------|:-------------|:------------|:------------|:----------|
| B1 | 0.929 | 0.900 | 0.912 | 3.4% |
| B2 | 1.117 | 1.118 | 1.115 | 0.27% |
| B3 | 0.881 | 0.975 | 1.144 | 26.7% |

B3 dominates the spectral flow (27% energy variation), B2 is essentially static (flat band + large gap = frozen BdG energy), B1 is intermediate.

**Step 2: Spectral flow rates dE_k/dtau**

Decomposition at fold (tau = 0.19):

| Sector | dE/dtau | Geometric | BCS | |Geom/BCS| |
|:-------|:--------|:----------|:----|:----------|
| B1 | -0.0635 | -0.0628 (98.9%) | -0.0007 (1.1%) | 93.0 |
| B2 | -0.0024 | -0.0003 (13.8%) | -0.0021 (86.2%) | 0.16 |
| B3 | +0.6725 | +0.6725 (100.0%) | -0.00003 (0.0%) | 21034 |

Critical finding: The geometric contribution (domega_k/dtau, eigenvalue evolution under Jensen deformation) overwhelmingly dominates in B1 and B3. The BCS contribution (dDelta/dtau) dominates only in B2, where it is sector-uniform (flat band = all modes identical). The overall flow rate varies by 275x between B3 (+0.672) and B2 (-0.002).

**Step 3: Spectral flow index alpha**

992-mode computation:
- Uniform gap: alpha = 2.63, n_s = 2.63 (blue, 827 sigma from Planck)
- Three-sector gap: alpha = 3.51, n_s = 3.51 (even bluer)

The steep positive alpha means the flow rate INCREASES with mode energy. Higher-KK modes flow faster, producing a blue spectrum (n_s > 1), not red (n_s < 1).

**Step 4: Total spectral flow**

N_flow(up) = 784, N_flow(down) = 208, net = 576. NOT zero. BDI PH symmetry requires net flow = 0 in the BdG Hilbert space, but this computation tracks omega_k (Dirac eigenvalues), not BdG quasiparticle levels. The net positive flow reflects the spectral spreading of eigenvalues under Jensen deformation (bandwidth increases by 28% from tau=0 to tau=0.19).

**Step 5: Van Hove singularity in flow rate**

The highest Van Hove point (omega = 2.05 at fold) shows flow rate 6.0x the mean. But this is the high-energy end of the spectrum, reinforcing the blue tilt. No Van Hove PEAK in flow rate at intermediate energies that could create a feature in the primordial spectrum.

**Step 6: Occupation spectrum**

| Model | n_k dependence | n_s | Deviation |
|:------|:---------------|:----|:----------|
| Adiabatic (1/|dE/dtau|) | E^{-3.51} | -2.51 | 827 sigma |
| Sudden quench ((Delta/omega)^4) | E^{-6.17} | -5.17 | 1470 sigma |
| Planck | -- | 0.9649 | -- |

The adiabatic limit is LESS steep than sudden quench (as expected -- slow evolution produces less k-dependent occupation than violent quench). But both are deeply red, not nearly flat.

**Step 7: Structural analysis**

The spectral flow rate decomposes as:

    dE_k/dtau = (omega_k/E_k)(domega_k/dtau) + (Delta_k/E_k)(dDelta_k/dtau)

Three structural obstructions prevent this from producing n_s ~ 0.965:

1. **BCS flow is k-INDEPENDENT within each sector.** dDelta/dtau is sector-level, not mode-level. For B2 (496 modes, flat band), dE/dtau is literally identical for all modes. This produces zero spectral tilt from the BCS channel.

2. **Geometric flow has the wrong slope.** domega_k/dtau increases steeply with omega_k (alpha ~ 2.6). Higher-energy modes flow faster because they are more sensitive to the metric deformation. This is the SAME structural problem as in pair creation: the eigenvalue span 2.5x across the KK tower forces a steep power law.

3. **No topological protection.** In 3He-A, spectral flow is topologically quantized (N_3 = +/-2 counts level crossings through zero energy). In BDI with an open gap, levels never cross zero. The "spectral flow" is just adiabatic spectrum evolution -- no anomaly, no quantization, no protected index.

### 3He-A vs Framework: Spectral Flow Comparison

| Property | 3He-A (Paper 09) | Framework BDI |
|:---------|:-----------------|:--------------|
| Topology | N_3 = +/-2 (Fermi point) | N_3 = 0 (no Fermi point) |
| Flow mechanism | Through zero energy | Along gap edge |
| Rate | dN/dt = N_3 (e l-dot)/(2 pi^2) | dE_k/dtau = geom + BCS |
| Quantization | YES (topological) | NO |
| Spectral index | N/A (total flow, not spectrum) | alpha = 2.6 (steep) |
| Protection | Momentum-space winding | None (BDI Z protects gap, not flow rate) |

The 3He-A chiral anomaly produces a NET CURRENT (baryon number violation), not a spectrum. The framework needs a SPECTRUM. Even if N_3 were nonzero, the chiral anomaly would not directly produce n_s.

### Gate Verdict

**SPECTRAL-FLOW-NS-47: INFO**

The spectral flow IS k-dependent (alpha = 2.63, unambiguously nonzero). But n_s = -2.51 (adiabatic) to -5.17 (sudden), both 827+ sigma from Planck 0.9649.

This is the 6th n_s route to produce the wrong answer for the SAME structural reason: the eigenvalue span 2.5x across the KK tower forces alpha >> 0.035. Whether the perturbation spectrum comes from pair creation (|beta_k|^2), forward/backward asymmetry, Landau-Zener transitions, or adiabatic spectral flow, the underlying spectrum of the KK tower imposes a steep power law. The spectral index is a property of the SPECTRUM, not of the physical process reading it out.

### n_s Route Closure Summary (cumulative: 11 routes)

| # | Route | Session | Result | Mechanism |
|:--|:------|:--------|:-------|:----------|
| 1 | Lifshitz eta | S44 | eta=0 (mean-field) | Wrong quantity |
| 2 | epsilon_H invariance | S44 | FAIL by construction | No slow-roll |
| 3 | Bogoliubov quench (KZ) | S45 | n_s=-0.588 (370 sigma) | (Delta/omega)^4 |
| 4 | Forward/backward asymmetry | S45 | n_s=-2.847 (908 sigma) | Same power law |
| 5 | Dense d_eff sweep | S46 | d_eff floor=3 (244 sigma) | K_7 topology |
| 6 | Hose count alpha | S46 | alpha=0.72 | Wrong exponent |
| 7 | Spectral flow (S46) | S46 | alpha=4.03 | UV-dominated |
| 8 | Landau-Zener | S46 | alpha=8.13 | Wrong regime |
| 9 | Transfer function | S46 | 56-order suppression | xi_KZ ~ 10^{-40} Mpc |
| 10 | e-fold count | S46 | 0.667 available | Need ~60 |
| 11 | **Adiabatic spectral flow** | **S47** | **n_s=-2.51 (827 sigma)** | **Same eigenvalue span** |

All routes produce n_s outside [0.93, 0.99]. All share the same root cause: the KK eigenvalue tower with span 2.5x and approximately uniform BCS gap.

### Remaining Open Paths

1. **Texture spectrum on fabric** (my S47 reassessment, Path C): Power spectrum of the condensate across the 32-cell tessellation, set by inter-cell coupling, not internal BCS spectrum. Analog of l-texture in 3He (Paper 14). NO session has attempted this.

2. **Topological defect correlations** (Path B): Vortex-vortex correlation function has power-law spectrum set by universality class, not gap structure. Outside Bogoliubov paradigm.

3. **k-dependent Delta(k)** (Path A): If the gap varied as k^{-0.76} across the tower, n_s could reach Planck. But flat band (B2) and Schur's lemma prevent this within the singlet sector.

### Files
- Script: `tier0-computation/s47_spectral_flow_ns.py`
- Data: `tier0-computation/s47_spectral_flow_ns.npz`
- Plot: `tier0-computation/s47_spectral_flow_ns.png` (6-panel: BdG energies, flow rates, geom-vs-BCS decomposition, alpha(tau), occupation spectra, summary)

---

## Synthesis

### Gate Verdicts

| Gate | Verdict | Key Number |
|:-----|:--------|:-----------|
| PI-SECTOR-47 | PASS | B1=15, B2=81, B3=35 (PW-weighted) |
| K7-FILTER-47 | PASS | Conservative: 81 accessible, Moderate: 116 |
| RATIO-CORRECT-47 | PASS | R_B2 = 1.494 (down from 2.19x) |
| SPECTRAL-LANDSCAPE-47 | INFO | 992 modes, 13 pi-phases, 3 sectors visualized |
| CURVATURE-ANATOMY-47 | INFO | 6 branches, K_max/K_min=12.5, 2 protected planes, no negative K |
| CONDENSATE-T2-47 | INFO | Identity-peaked, contrast 3.1M, 1/e^2 radius = 0.25*pi, S_3 exact |
| PAASCH-SPIRAL-47 | FAIL | Rayleigh p=0.70, KS p=0.81, 0 clusters, phi-ratio deficit 3.2-sigma |
| PHI-BDG-47 | FAIL | R_dressed max = 1.465 (all scenarios), 7.6-sigma below phi. BCS shift -8.6% |
| COHERENCE-RESPONSE-47 | ARTIFACT | |r|=0.9996 but CV=0.036%, elasticity=0.030. r_C 95% geometric, 0.13% BCS-dynamic |
| RHOS-TENSOR-47 | PASS | Anisotropy 24.4x (C^2/u1), CV=40%, 1116x artifact. Anti-correlated with curvature (r=-0.91, p=0.002) |
| ANISO-DISSIP-47 | INFO | Strict: 3.76x (unchanged). Generous screening: 2.22x. 24x anisotropy structurally decoupled from LZ friction (3 theorems) |
| SPECTRAL-FLOW-NS-47 | INFO | alpha=2.63, n_s=-2.51 (827 sigma). k-dependent but wrong slope. 11th n_s route closed. Same eigenvalue-span obstruction |

### S46 Correction

**2.19x RETRACTS.** Base-mixing error: numerator included 50 PW-weighted pi-phases in sectors where BCS pairing is forbidden (B1, Trap 1) or marginal (B3, V=0.003). Denominator included B1 cross-channel entanglement counted as BCS pairs.

**Corrected value: R_B2 = 1.494** (B2-only, sector-matched using BCS v² fractions).

### Structural Results

1. **B2 dominance confirmed from both sides**: 62% of pi-phase topology and 91% of BCS dynamics concentrate in B2. Topology and dynamics select the same sector.

2. **[iK₇, D_K] = 0 is exact ONLY in (0,0) sector**. Higher reps have 9.5-13.4% K₇ mixing from the algebraic structure [I⊗iK₇, D] = Σ E_ab ρ(X_b) ⊗ [iK₇, γ_a]. This is new — prior sessions assumed K₇ conservation held globally.

3. **B1 occupation paradox resolved**: 49.4% B1 weight in 8-mode ED is cross-channel entanglement through V(B1,B2) = 0.130, not self-pairing. BCS v² fractions (B1 = 8.3%) are the correct decomposition for BCS pair counts.

4. **Residual 1.5x**: Within B2, ~1.5 topological channels per Cooper pair. Moderate surplus — not the factor-of-2 BDI claim, but nontrivial.

5. **Two curvature invariants (new theorems)**:
   - K(u(1), su(2)) = 0 exactly at all tau — 3 flat directions from [u(1), su(2)] = 0
   - K(u(1), C²) = 1/16 exactly at all tau — protected hypercharge-coset curvature
   - Anisotropy K_max/K_min grows from 4.0 (bi-invariant) to 12.5 (fold). No negative curvatures.

6. **Condensate peaks at identity**: |Δ|² on T² has contrast ratio 3.14×10⁶, 1/e² radius = π/4. Cooper pairs concentrate within ~1/8 of the torus period around the identity element. S₃ Weyl symmetry exact (4.1e-14). Haar-weighted density peaks at r ≈ 0.85 rad (shell structure from Weyl denominator zero).

7. **B2 progressive concentration**: Modes 50% -> topology 62% -> BCS dynamics 91%. The crystal's active physics funnels through B2 at every level.

8. **Coherence width is geometric, not BCS-determined (W3-3)**: The 1/e^2 radius of the character coherence function C(theta; tau) on T^2 is 95.0% determined by the Peter-Weyl truncation (p+q <= 3), 5.0% by the BCS occupation shift (tau-independent), and 0.13% by tau-dependent BCS modulation. Despite |r(r_C, Delta_B2)| = 0.9996, the elasticity is 0.030 -- the coherence radius barely responds to BCS gap changes. The condensate pattern on T^2 is a truncation artifact with a perturbative BCS correction, not a substrate diagnostic. This self-corrects the prediction in the substrate reframe document.

9. **Superfluid density tensor is highly anisotropic and dynamical (W3-4)**: The BCS condensate stiffness rho_s^{ab} against gauge phase twists in 8 su(3) directions is diagonal with 3 distinct eigenvalues (degeneracies 4, 3, 1) reflecting the reductive decomposition su(3) = u(1) + su(2) + C^2. At the fold: C^2 stiffness = 7.96, su(2) = 0.50, u(1) = 0.33. Anisotropy 24.4x. CV across tau = 40.2%, which is 1116x the W3-3 artifact. This IS a genuine response function: it vanishes at Delta=0, varies strongly with tau, and reveals that the condensate is rigid in the C^2 (coset) directions and soft in the u(1) and su(2) (stabilizer) directions.

10. **Superfluid stiffness ANTI-correlates with curvature (W3-4)**: Pearson r = -0.906, p = 0.002. Directions with high geometric curvature have LOW superfluid stiffness, and vice versa. The condensate fills the geometrically compliant C^2 directions because those are the directions where the inter-sector B1-B2 and B2-B3 pairing acts. This is the "near are like" mechanism in response-function language: the BCS condensate dynamically reinforces the coset structure SU(3)/U(2).

11. **24x rho_s anisotropy STRUCTURALLY DECOUPLED from LZ friction (W4-2)**: Three independent theorems establish that the superfluid anisotropy cannot modify the non-singlet LZ dissipation: (a) dH/dtau is block-diagonal (zero inter-sector coupling to 10^{-28}), (b) dH/dtau is pure order-3 Clifford (orthogonal to single-direction current operators), (c) Schur's lemma forces isotropic effective gap for all (p,q). The 3.76x shortfall from S46 is a structural feature, not an approximation artifact. A generous screening upper bound gives 2.22x at fold, still INFO.

12. **Adiabatic spectral flow produces the SAME n_s obstruction as pair creation (W4-3)**: BdG spectral flow rate dE_k/dtau decomposes into geometric (domega_k/dtau) and BCS (dDelta/dtau) contributions. The BCS contribution is k-INDEPENDENT within each sector (flat band B2: all 496 modes identical). The geometric contribution is k-dependent but steep (alpha = 2.63). n_s = -2.51 (adiabatic), 827 sigma from Planck. This confirms that the eigenvalue-span obstruction (spectrum spans 2.5x, gap approximately uniform) is universal across ALL readout mechanisms: pair creation, spectral flow, Landau-Zener, forward/backward asymmetry. 11 routes now closed. No topological protection of spectral index (N_3 = 0, BDI class). The 3He-A chiral anomaly (Paper 09) is structurally inapplicable because it requires Fermi points (N_3 != 0) and produces a total current, not a spectrum.

### Files Produced

- `tier0-computation/s47_pi_sector.py` / `.npz` / `.png`
- `tier0-computation/s47_k7_filter.py` / `.npz` / `.png`
- `tier0-computation/s47_ratio_correct.py` / `.npz`
- `tier0-computation/s47_spectral_landscape.py` / `.npz` / `.png` / `.pdf`
- `tier0-computation/s47_curvature_anatomy.py` / `.npz` / `.png`
- `tier0-computation/s47_condensate_torus.py` / `.npz` / `.png` (+ `_analysis.png`, `_haar.png`, `_characters.png`)
- `tier0-computation/s47_paasch_spiral.py` / `.npz` / `.png`
- `tier0-computation/s47_coherence_response.py` / `.npz` / `.png` / `_contrast.png`
- `tier0-computation/s47_rhos_tensor.py` / `.npz` / `.png`
- `tier0-computation/s47_aniso_dissip.py` / `.npz` / `.png`
- `tier0-computation/s47_spectral_flow_ns.py` / `.npz` / `.png`

---

## W5-1: Josephson Phase Correlations Across Tessellation (TEXTURE-CORR-48)

**Agent**: landau-condensed-matter-theorist
**Gate**: TEXTURE-CORR-48

### Gate TEXTURE-CORR-48: PASS

P(K) has non-trivial K-dependence: P(K) ~ K^{-2} (Ornstein-Zernike, gapless Goldstone). Low-K slope = -1.955. Ratio P(K_1)/P(K_Nyquist) = 104x. Slope is within [-3, 0].

### Physics

Each of the 32 Kibble-Zurek domains has a BCS condensate with a spontaneously chosen U(1)_7 phase phi_i. The inter-cell coupling is Josephson:

    E = Sum_{<ij>} J_{ij} (1 - cos(phi_i - phi_j))

In the harmonic approximation (valid when phi_rms < 1):

    E ~ (1/2) Sum_{<ij>} J_{ij} (phi_i - phi_j)^2

The stiffness matrix M_{ij} is a discrete Laplacian weighted by J. The phase-phase correlation function is:

    C_{ij} = <phi_i phi_j> = T_eff * (M^+)_{ij}

where M^+ is the pseudoinverse (projecting out the Goldstone zero mode). The power spectrum P(K) = FT of C_{ij}.

### Josephson Coupling

The coupling between adjacent BCS condensates:

    J = |E_cond| * rho_s^{dir} * f_overlap

where |E_cond| = 0.137 M_KK (S36 ED, canonical), rho_s^{dir} is the direction-dependent superfluid stiffness from W3-4, and f_overlap = exp(-l_cell/xi_GL) = 0.856 accounts for the condensate wavefunction overlap.

| Direction | rho_s | J (M_KK) | T_acou/J | T_comp/J | Regime (acoustic) |
|-----------|-------|----------|----------|----------|-------------------|
| C^2 (4 dirs) | 7.962 | 0.933 | 0.120 | 8.13 | ORDERED |
| su(2) (3 dirs) | 0.505 | 0.059 | 1.90 | 128 | DISORDERED |
| u(1) (1 dir) | 0.327 | 0.038 | 2.93 | 198 | DISORDERED |

### Temperature Determination

Two temperature scales compete:

1. **T_compound = 7.58 M_KK**: Full quench energy divided by N_dof. This would make ALL directions disordered (T/J >> 1 everywhere).

2. **T_acoustic = 0.112 M_KK**: Acoustic bath temperature from S42 Hauser-Feshbach. This gives ordered C^2 and disordered su(2)/u(1).

The physically relevant temperature for phase fluctuations is **T_acoustic**, because:
- The BCS quench energy goes primarily into quasiparticle pair excitations (59.8 pairs), not phase modes
- The GGE (exact integrability, 8 Richardson-Gaudin conserved integrals, S38) prevents full thermalization
- Phase modes couple to the low-energy acoustic sector, which thermalizes at T_acoustic
- The block-diagonal theorem (S22b) separates the spectral sectors, preventing energy flow from high-energy pair modes to low-energy phase modes

### Key Results

**1. Power spectrum is exactly K^{-2} (Ornstein-Zernike).**

For a 1D ring of N cells with uniform Josephson coupling J, the exact result is:

    P(K_n) = T / (4J sin^2(pi n/N))

In the continuum limit: P(K) ~ T/(J K^2), giving n_s - 1 = -2 exactly. The full-range fit gives alpha = -1.69 due to lattice dispersion near the Brillouin zone boundary; the low-K fit gives -1.96, approaching -2.00. Machine-epsilon agreement between numerical and analytical results (max error 3e-14).

This is the universal spectrum of phase fluctuations in a system with spontaneously broken U(1) -- the Goldstone mode has no gap, so P(K) diverges as K -> 0.

**2. Anisotropic phase order at T_acoustic.**

| Direction | T_acou/J | xi_phase (cells) | Order |
|-----------|----------|-------------------|-------|
| C^2 | 0.120 | 532 | Long-range (> N=32) |
| su(2) | 1.90 | 34 | Marginal (~ N) |
| u(1) | 2.93 | 22 | Marginal (< N) |

The C^2 (coset) directions are phase-locked across the entire tessellation: xi_phase = 532 cells >> N = 32. The su(2) and u(1) (stabilizer) directions are near the order-disorder boundary.

At T_compound (pessimistic): xi_phase(C^2) = 7.9 cells. Even in the worst case, nearest-neighbor phase coherence survives.

**3. Harmonic approximation is valid at T_acoustic.**

phi_rms(C^2, acoustic) = 0.566 rad < 1. The harmonic (small-angle) approximation is self-consistent. At T_compound, phi_rms = 4.65 rad >> 1: the harmonic approximation fails, and the full cos(phi) potential dominates, pushing toward a disordered state.

**4. n_s from the texture route.**

The phase gradient spectrum P_{nabla phi}(K) = K^2 * P_phi(K) ~ K^0 is scale-invariant. If density perturbations couple to phase gradients (the natural coupling in superfluid hydrodynamics), the primordial spectrum is Harrison-Zel'dovich:

    n_s = 1 (HZ)

This is 0.035 from Planck (0.9649), or 8.3 sigma. A mild red tilt could arise from:
- Finite correlation length corrections (xi_GL/l_cell = 0.156 introduces a mass scale)
- BCS gap anisotropy modifying the effective J(K)
- GGE Lagrange multipliers deviating from thermal
- Running of rho_s with tau during transit

**5. Scale separation.**

At the M_KK scale, the tessellation operates at K ~ 10^{55}-10^{56} Mpc^{-1}, separated from the CMB pivot by 58 decades. However, at the S42 fabric scale (post-exflation), the tessellation has:

    l_cell = 450 Mpc, K_min = 4.4e-4 Mpc^{-1}, K_max = 7.0e-3 Mpc^{-1}

The CMB pivot K = 0.05 Mpc^{-1} is 7.2x above K_max. This means CMB scales probe WITHIN individual cells, not the inter-cell texture. The texture spectrum sets correlations at l > 450 Mpc (BAO and larger), not at CMB scales directly.

**6. Connection to superfluid textures (Volovik/Landau).**

This computation is the internal-space analog of the l-texture in 3He-A (Volovik, Paper 31 in my corpus). The phase field phi(x) across the tessellation is the internal-space equivalent of the l-vector orientation across a 3He-A container. The Josephson coupling J plays the role of the dipole-dipole interaction that orients the l-vector.

The key difference from 3He-A: there, pi_1(S^2/Z_2) = Z gives stable vortex lines (half-quantum vortices). Here, pi_1(U(1)) = Z gives quantized phase winding. The domain walls between KZ domains are the condensed-matter analog of cosmic strings.

### Structural Result (Theorem)

**For any Josephson-coupled array of BCS condensates on a lattice with coordination number z, spontaneously broken U(1) symmetry, and effective temperature T:**

    P(K) = T / (z J * (1 - gamma_K))

where gamma_K is the structure factor (= cos(K) for 1D, = (1/d) Sum_i cos(K_i) for d-dimensional cubic). This is:
- **K^{-2} for K -> 0** (Goldstone theorem: gapless phase mode)
- **Bounded at K_max** (P(K_max) = T/(2zJ))
- **Direction-dependent** through J = |E_cond| * rho_s^{dir}

The only free parameter is the ratio T/J. The spectrum shape is UNIVERSAL.

### Files

- Script: `tier0-computation/s47_texture_corr.py`
- Data: `tier0-computation/s47_texture_corr.npz`
- Plot: `tier0-computation/s47_texture_corr.png`

---

## W5-2: Scale Bridge — Exhaustive Enumeration of Framework Scales (SCALE-BRIDGE-48)

**Agent**: tesla-resonance
**Gate**: SCALE-BRIDGE-48

### Gate SCALE-BRIDGE-48: FAIL

No framework scale within a factor of 100 of the corrected target (2.67 Mpc) exists with a physical mechanism. Full analysis in `sessions/session-47/session-47-scale-bridge.md`.

### Algebra Error in Source

The task target of 151 Mpc originates from Volovik's wave5-texture plan (line 225), which inverts the Ornstein-Zernike formula. The correct derivation:

    P(K) = A / (K^2 + 1/xi^2)
    n_s - 1 = -2K^2 / (K^2 + 1/xi^2)
    At n_s = 0.965, K_pivot = 0.05 Mpc^{-1}:
    (K*xi)^2 = (1-n_s)/(1+n_s) = 0.035/1.965 = 0.01781
    xi = sqrt(0.01781) / 0.05 = 2.669 Mpc   (NOT 1/(0.05*sqrt(0.0175)) = 151 Mpc)

Verification: n_s(xi=2.67) = 0.965 (correct). n_s(xi=151) = -113.3 (wrong).

The inverted value 151 Mpc is within 2.7% of the BAO sound horizon r_s = 147 Mpc. This near-coincidence is an artifact of the algebra error, not a physical connection.

### Scale Enumeration Summary

All framework scales fall into two clusters separated by 58.6 decades:

| Cluster | Scale range (Mpc) | Contents |
|:--------|:-----------------|:---------|
| Internal | 10^{-58} to 10^{-53} | Eigenvalues, BCS gaps, curvature radii, coherence lengths, transit distances |
| External | 10^{3.1} to 10^{4.2} | Tessellation cells (4488), Hubble radius (4448), observable radius (14250) |

Target: xi = 2.67 Mpc = 10^{0.43} Mpc, sitting 55 decades above internal and 3.2 decades below external.

### Nearest Framework Combinations

| Combination | Value (Mpc) | Ratio to target | Mechanism? |
|:-----------|:------------|:----------------|:-----------|
| l_cell / N_cells | 140.3 | 52.5x too large | Tessellation resolution, not texture correlation |
| c/(H_0 * N_cells) | 139.0 | 52.1x too large | Same ratio via c/H_0 ~ l_cell |
| Silk damping scale | 8.38 | 3.1x too large | Standard baryon diffusion, not framework-derived |
| l_cell * K_protected^2 | 17.5 | 6.6x too large | No physical mechanism |

No product, ratio, or resonance of internal-scale quantities produces a macroscopic length. The gap is structural: the framework has an ultraviolet (M_KK) and an infrared (H_0), with no intermediate scale-generating mechanism.

### Structural Result

The n_s crisis is a SCALE crisis: the framework lacks any mechanism to generate spatial correlations at intermediate scales (1-1000 Mpc). The O-Z texture shape is generic and trivially matches any nearly-Gaussian perturbation spectrum. The physics is in the specific value xi = 2.67 Mpc, which requires a process operating at a Hubble rate H ~ m = 2.4e-39 GeV (corresponding to T ~ 0.5 eV, the recombination epoch). No known framework mechanism operates at this scale.

### Files

- `sessions/session-47/session-47-scale-bridge.md` (full analysis, 7 sections)

---

## W5-3: Acoustic Horizon at the BCS Transit (ACOUSTIC-HORIZON-48)

**Agent**: hawking-theorist
**Gate**: ACOUSTIC-HORIZON-48

### Gate ACOUSTIC-HORIZON-48: FAIL (Planck-scale)

The transit acoustic horizon is 60 orders of magnitude below 151 Mpc. Even after comoving stretching, 31 orders of magnitude short.

### Method

Computed the maximum distance correlations can propagate during the BCS transit using framework parameters from canonical_constants.py and upstream NPZ data (S38, S42). Four candidate sound speeds evaluated; the physically relevant one is c_fabric = c (Lorentz invariant, S42 C-FABRIC-42 PASS). The transit duration dt_transit = 1.130e-3 M_KK^{-1} is from S38 (Kibble-Zurek computation).

### Sound Speed Identification

Four candidates computed:

| Candidate | Value | Physical basis | Relevance |
|-----------|-------|----------------|-----------|
| c_fabric (A) | c = 1 | Spectral action Lorentz invariant | THE 4D propagation speed |
| c_BAO (B) | c/sqrt(3) = 0.577c | Baryon-photon plasma | Post-BBN only (not relevant at transit) |
| v_BCS(int) (C) | 0.024c | Pair vibration across internal fiber | Internal space, not 4D |
| v_g(k=H) (D) | 0.99999c | Group velocity at Hubble scale | Ultrarelativistic (H/m_tau = 284) |

The tau modulus mass m_tau = 2.062 M_KK is negligible at the transit epoch because H_fold = 586.5 M_KK >> m_tau. All Hubble-scale modes are ultrarelativistic with v_g ~ c to six significant figures.

### Key Numbers

| Quantity | M_KK units | Mpc |
|----------|-----------|-----|
| Transit duration dt_transit | 1.130e-3 | - |
| Transit acoustic horizon c*dt | 1.130e-3 | 9.73e-59 |
| Comoving transit horizon | - | 3.08e-29 |
| KZ correlation length xi_KZ | 0.808 | 6.96e-56 |
| Hubble radius at fold r_H | 1.705e-3 | 1.47e-58 |
| Standard BAO r_s | - | 147.09 |
| Target for n_s resolution | - | 151 |
| **Transit / Target** | - | **6.4e-61** |

### The BAO Connection

The standard BAO sound horizon r_s = 147.09 Mpc is set by baryon-photon plasma physics integrated from the big bang to the drag epoch (z_drag ~ 1060). The BCS transit occurs at z ~ 3.2e29 (T = M_KK = 7.43e16 GeV), separated from BBN by 20 decades in temperature. The framework INHERITS the standard r_s = 147 Mpc because:

1. The transit completes 10^{20} times before BBN. No framework modification of baryon-photon plasma physics is possible.
2. After thermalization (t_therm ~ 6 M_KK^{-1}), the universe enters standard radiation domination.
3. c_s in the baryon-photon plasma is determined by standard physics (c/sqrt(3*(1+R))), not by the spectral action.

The closeness of 147 Mpc and 151 Mpc is coincidental from the framework's perspective. Both are set by post-BBN plasma physics. The transit determines initial conditions (the primordial power spectrum), not the acoustic scale.

### The Friedmann Shortfall (Reconfirmed)

H_fold (framework) = 4.36e19 GeV vs H_Friedmann(T=M_KK) = 1.55e15 GeV. Ratio: 2.82e4. The framework H is driven by the spectral action gradient dS/dtau, not by the energy density rho. This is the previously identified 28,000-114,000x shortfall. The framework Hubble parameter at the fold is 28,000 times larger than what standard Friedmann gravity at T = M_KK would produce.

### Transit vs Correlation Length

d_transit / xi_KZ = 0.0014. The transit is 700x FASTER than the time for correlations to propagate across one BCS coherence length. The post-transit correlation pattern is set by the Kibble-Zurek mechanism (xi_KZ = 0.808 M_KK^{-1}), not by acoustic propagation during transit.

### Structural Result

The transit acoustic horizon is a Planck-scale distance (~10^{-35} m physical, ~10^{-58} Mpc). Even comoving stretching by (1+z) ~ 3e29 gives only ~10^{-6} m (~10^{-29} Mpc). The acoustic horizon route to 151 Mpc is CLOSED by 60 orders of magnitude (physical) or 31 orders (comoving).

The n_s = 0.965 correlation scale, if it exists in this framework, must be set by the primordial perturbation spectrum at formation, not by acoustic propagation during or after the transit.

### Files

- `tier0-computation/s47_acoustic_horizon.py` / `.npz`
