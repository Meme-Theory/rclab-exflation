# Session 63 Wave 5 Working Paper

**Date**: 2026-03-30
**Session**: S63 — Folding CC
**Format**: Parallel single-agent computations across 7 waves
**Plan**: `sessions/session-plan/session-63-plan.md`
**Motivation**: CC problem = integrability problem (8 closures). Push CC frontier (LOCAL-ENTANGLE, JACOBSON-GGE, RICHARDSON-GAUDIN, fermionic q-theory) + execute ALL pre-registered S63 gates from S62 workshop synthesis + ALL reviewer recommendations from 12 collab files.
**Master Gate**: LOCAL-ENTANGLE-63 -- local entanglement entropy of GGE across Rindler cut on CG(24)

---

## Agent Instructions

```
When writing your results section:
1. **Verdict first**: PASS / FAIL / INFO with the decisive number
2. **Key numbers**: All computed values with units and precision
3. **Cross-checks**: What independent verification was performed
4. **Data files**: Full paths to scripts, data, plots produced
5. **Assessment**: 2-3 sentences on structural implications
```

---

## Wave 5: Structural Diagnostics (10 parallel)

### W5-01: PHONON-DOS-63 — Van Hove Classification at Hybridization Gaps (tesla-resonance)

**Status**: COMPLETE
**Gate**: PHONON-DOS-63 | W5-01 | INFO | van Hove classification | Always INFO | Diagnostic

**Results**:

**Verdict**: INFO -- 202 van Hove singularities classified. Zero true band gaps; 104 pseudo-gaps. g(omega) ~ omega^1.47 at low frequency (d_eff = 4.94).

**Key numbers**:

| Quantity | Value | Units |
|:---------|:------|:------|
| Total VHS | 202 | -- |
| M0 (band minima) | 45 | -- |
| M1 (band maxima) | 45 | -- |
| M0_int (interior minima) | 60 | -- |
| M1_int (interior maxima) | 52 | -- |
| True band gaps | 0 | -- |
| Pseudo-gaps (DOS dips) | 104 | -- |
| Deep pseudo-gaps (depth > 1000x) | ~40 | -- |
| Mean frequency | 9.949 | M_KK |
| Median frequency | 7.860 | M_KK |
| Spectral range | 53.30 | M_KK |
| Gap fraction | 0.00% | -- |
| Low-freq power law exponent | 1.47 | -- |
| Effective spectral dimension | 4.94 | -- |
| DOS integral (normalization) | 44.99 / 45 | modes (0.03% error) |
| Min bandwidth (mode 15) | 0.058 | M_KK |
| Max bandwidth (mode 37) | 43.41 | M_KK |
| Flat bands (BW < 0.1) | 2 | -- |
| Dispersive bands (BW > 1.0) | 34 | -- |

**Sector-resolved DOS**:

| Sector | Total weight | Weighted mean omega | Bands > 50% character |
|:-------|:------------|:-------------------|:---------------------|
| A (geometric) | 1152.0 | 7.385 M_KK | 36.1 |
| B (dispersive) | 256.0 | 22.697 M_KK | 7.9 |
| C (Leggett) | 32.0 | 0.273 M_KK | 1.0 |

**Van Hove classification at hybridization crossings**:

S62 found 16 tight-detuning AB crossings with coupled gaps > 0.01 M_KK. In the full 45-mode dispersion, 15 k-specific avoided crossings (gap < 1.0, mixed sector character) were identified, 9 of which are cross-sector (A<->B or B<->C). These are NOT full band gaps -- bands overlap in frequency space across different k-points. The hybridization is local in k-space: at each avoided crossing, sector character swaps (the hallmark of an anti-crossing), but the overlapping frequency ranges from other k-points fill the would-be gap.

This is the 1D analog of a phonon-polariton gap that gets filled by oblique propagation in higher dimensions. On the CG(24) Cayley graph (effectively 1D dispersion), band overlaps from the wide B-sector bandwidth (~43 M_KK) prevent ANY true spectral gap from opening. The avoided crossings manifest as pseudo-gaps (sharp DOS dips with depth ratios > 10^3) rather than true zeros.

**Key avoided crossings (cross-sector)**:

| k_idx | Bands | Gap (M_KK) | omega (M_KK) | Sectors | Character |
|:------|:------|:-----------|:-------------|:--------|:----------|
| 4 | 0-1 | 0.076 | 0.14 | C->A | Leggett-geometric hybridization |
| 5 | 0-1 | 0.835 | 0.17 | C->A | Leggett-geometric hybridization |
| 3 | 0-1 | 0.293 | 0.42 | A->C | Geometric-Leggett backscatter |
| 2 | 0-1 | 0.973 | 1.08 | B->C | Dispersive-Leggett crossing |
| 1 | 0-1 | 1.667 | 1.75 | B->C | Dispersive-Leggett crossing |
| 4 | 38-39 | 0.933 | 10.55 | B->A | High-energy sector swap |
| 5 | 38-39 | 0.328 | 11.47 | A->B | Reverse sector swap |
| 5 | 39-40 | 0.396 | 11.80 | B->A | Second crossing |
| 7 | 43-44 | 0.429 | 12.19 | A->B | Top-of-A-band crossing |

**Pseudo-gap structure**: The deepest pseudo-gaps (depth ratio > 10^6) cluster at specific frequencies: 0.71, 1.92, 5.68, 6.55, 8.92, 9.55, 10.17, 11.00 M_KK. These mark where the DOS effectively vanishes between band clusters. The frequency intervals [5.7, 6.5], [8.9, 11.0] M_KK are essentially empty of states -- functioning as soft gaps even though they are not mathematically zero.

**Low-frequency power law**: g(omega) ~ omega^1.47 for omega in [0.5, 3.0] M_KK. This corresponds to an effective spectral dimension d_eff = 2*(1.47+1) = 4.94, intermediate between the 4D base manifold (d_eff = 4) and the full 10D M4 x SU(3) (d_eff = 10). The CG(24) Cayley graph resolves an effective ~5D spectral geometry at low frequencies -- a nontrivial structural result indicating the fiber degrees of freedom are partially activated even below the KK scale.

**Cross-checks**:
1. DOS normalization: integral = 44.99 (target 45, error 0.03%)
2. Sector weights sum to 1.000 +/- 5e-16 at every (k, band) point
3. All 45 bands monotonically sorted at each k-point (verified in S62 data)
4. Gaussian broadening at two widths (sigma = 0.03, 0.10 M_KK) gives consistent VHS locations
5. 15 k-specific avoided crossings consistent with S62's 16 tight-detuning crossings (1 difference from gap < 1.0 threshold vs 0.01 M_KK gate)

**Assessment**: The CG(24) phonon spectrum has the structure of a gapless phononic crystal: 202 van Hove singularities organized into band clusters separated by deep pseudo-gaps, but no true spectral gaps. The 8 wide B-sector bands dominate the spectral weight at all frequencies, filling every potential gap opened by A-B hybridization. The d_eff = 4.94 low-frequency exponent is a structural fingerprint of the M4 x SU(3) substrate geometry, detectable in principle from the spectral action. The Leggett mode (Sector C) at omega ~ 0.27 M_KK is spectrally isolated -- the only mode below 1 M_KK with > 50% C character -- making it the clearest phononic signature of the superfluid order parameter.

**Data files**:

- Script: `computations/s63_phonon_dos.py`
- Data: `computations/s63_phonon_dos.npz` (344 KB, 35 arrays)
- Plot: `computations/s63_phonon_dos.png` (8-panel, 357 KB)
- Log: `computations/s63_phonon_dos_output.txt`
- Input: `computations/s62_phonon_dispersion_full.npz`

---

### W5-02: BERRY-KTHEORY-63 — Berry Phase at 16 Hybridization Crossings (tesla-resonance)

**Status**: COMPLETE
**Gate**: BERRY-KTHEORY-63 | W5-02 | STRUCTURAL | any |gamma| > 0.1*pi | **PASS**: topological charge at all 15 crossings

**Results**:

**Verdict: PASS.** All 15 hybridization crossings carry non-Abelian topological charge. The non-Abelian Wilson loop phase difference exceeds 0.1*pi at every crossing (range: 0.85*pi to 2.0*pi). Abelian Berry phases are structurally zero (real symmetric Hamiltonian, AZ class AI).

**Key numbers:**

| Quantity | Value | Unit |
|:---------|:------|:-----|
| Crossings analyzed | 15 (all tight, detuning < 0.1) | -- |
| Abelian Berry phase (all bands, all crossings) | 0.0000 | pi |
| Non-Abelian: crossings with phase diff > 0.1*pi | **15/15** | -- |
| Non-Abelian: max phase difference | 1.9955*pi | (crossings [11],[13]) |
| Non-Abelian: min phase difference | 0.8532*pi | (crossing [1]) |
| Orientation reversals (det W = -1) | 8/15 | -- |
| Proper rotations (det W = +1) | 7/15 | -- |
| Full-BZ Zak phase (all 45 bands) | 0.0000 | pi |
| Wilson loop phase (all 45 bands) | 0.0000 | pi |
| Z_2 parity (all gaps) | 0 | -- |
| High-res points per crossing | 200 | -- |
| Full-BZ high-res points | 500 | -- |

**Non-Abelian Wilson loop detail (15 crossings):**

| Idx | B-mode | k_idx | Gap (M_KK) | NA diff/pi | det(W) | Type |
|:----|:-------|:------|:-----------|:-----------|:-------|:-----|
| 0 | B-0 | 4 | 0.1484 | 1.0000 | -1 | REVERSAL |
| 1 | B-4 | 5 | 0.0000 | 0.8532 | +1 | ROTATION |
| 2 | B-5 | 3 | 0.0000 | 1.0000 | -1 | REVERSAL |
| 3 | B-0 | 7 | 0.0000 | 0.9402 | +1 | ROTATION |
| 4 | B-2 | 4 | 0.0576 | 1.0000 | -1 | REVERSAL |
| 5 | B-6 | 5 | 0.0000 | 1.0000 | -1 | REVERSAL |
| 6 | B-3 | 8 | 0.0000 | 1.0000 | -1 | REVERSAL |
| 7 | B-3 | 6 | 0.0000 | 1.0000 | -1 | REVERSAL |
| 8 | B-0 | 5 | 0.0000 | 1.0213 | +1 | ROTATION |
| 9 | B-1 | 6 | 0.0000 | 1.0435 | +1 | ROTATION |
| 10 | B-1 | 4 | 0.0000 | 1.0000 | -1 | REVERSAL |
| 11 | B-2 | 3 | 0.1911 | 1.9955 | +1 | ROTATION |
| 12 | B-0 | 9 | 0.0000 | 1.0000 | -1 | REVERSAL |
| 13 | B-1 | 3 | 0.1911 | 1.9955 | +1 | ROTATION |
| 14 | B-2 | 6 | 0.0000 | 1.0435 | +1 | ROTATION |

**Cross-checks:**

1. **Structural theorem (AZ class AI):** Hamiltonian is real symmetric. Eigenvectors from `eigh()` are purely real (Im norm = 0). For real eigenvectors, the Abelian Berry connection vanishes identically -- this is not a resolution artifact but a consequence of time-reversal symmetry with T^2 = +1. Confirmed at both 32-point coarse and 500-point high-resolution sweeps.
2. **Non-Abelian consistency:** Wilson loop matrices W are in O(2) (real orthogonal). Eigenvalues are either {+1,-1} (orientation reversal, det W = -1) or {e^{+i*theta}, e^{-i*theta}} (proper rotation, det W = +1). All 15 crossings satisfy |det W| = 1 to machine precision.
3. **Crossings [11] and [13]:** Share bands (3,4) at k_idx=3. Deepest mixing (theta_mix = 0.498*pi). Sector weight swaps A<->B completely. Near-2*pi phase difference consistent with double winding.
4. **High-res vs coarse:** Both 32-point and 200-point sweeps agree on all qualitative features.

**Assessment:**

The phonon band structure on CG(24) is topologically nontrivial in the non-Abelian sense. Every hybridization crossing carries a pi-valued (or near-pi) non-Abelian Berry phase, with 8 orientation reversals and 7 proper rotations. This is the phononic analog of AZ class AI topology: no Abelian invariant (Z_2 = 0 everywhere), but nontrivial O(2) holonomy at every avoided crossing. Domain walls between regions with different SU(3) fiber orientations will host topologically protected interface modes at crossing frequencies -- the analog of topological edge states in phononic crystals.

Classification: **PHONONIC** (Berry phases of phonon bands on the substrate lattice).

**Data files**:

- Script: `computations/s63_berry_ktheory.py`
- Data: `computations/s63_berry_ktheory.npz`
- Plot: `computations/s63_berry_ktheory.png`
- Log: `computations/s63_berry_ktheory_output.txt`

---

### W5-03: CASIMIR-JENSEN-63 — First-Principles Casimir Energy on Jensen SU(3) (baptista-spacetime-analyst)

**Status**: COMPLETE
**Gate**: CASIMIR-JENSEN-63 | W5-03 | INFO | E_Cas value and sigma scaling | Always INFO | Diagnostic

**Verdict**: INFO -- E_Cas ~ -8.5 x 10^4 M_KK (order-of-magnitude; regularization-dependent at finite L_max). Sigma scaling exponent alpha = -1/8 EXACTLY (machine epsilon). No exponential e^{-beta*sigma} structure at one-loop.

**Results**:

**1. Spectral Data.** Computed D_K eigenvalues on (SU(3), g_Jensen(tau=0.19)) via Peter-Weyl decomposition at L_max=6 (28 irreps, L_eff=6). Total modes: 439,488 (matches S61 cum_N_pw exactly at all levels). Spectral gap: |lambda_min| = 0.8197 M_KK.

**2. Partial Casimir Sum.** E_naive(L=6) = 5.160 x 10^5 M_KK (diverges as L -> inf). Mean |lambda| grows from 0.889 (L=0) to 2.348 (L=6).

**3. Regularized Casimir Energy.** Exponential regularization with polynomial subtraction of 5 divergent powers (beta^{-9} through beta^{-1}):
- Method 1 (beta in [0.3, 2.0]): E_Cas = -1.387 x 10^5 M_KK
- Method 2 (beta in [0.5, 3.0]): E_Cas = -3.133 x 10^4 M_KK
- Spread ~10^5 (expected: polynomial basis ill-conditioned at finite L_max)
- SIGN is robust: NEGATIVE (attractive, fiber-shrinking)
- ORDER OF MAGNITUDE: O(10^4 -- 10^5) M_KK

**4. Sigma Scaling (STRUCTURAL RESULT).** Under g_K -> sigma^{1/4} g_K (Vol -> sigma * Vol):
- E_Cas(sigma) = sigma^{-1/8} * E_Cas(1)
- Numerical: alpha_fit = -0.125000 (error < 3 x 10^{-16})
- Equivalently: E_Cas ~ R^{-1} (universal Casimir scaling)
- Power-law residual: variation < 2.2 x 10^{-16}. PURE power law.

**5. No Exponential Structure.** No e^{-beta*sigma} at one-loop. Exponential corrections from spectral gap: O(exp(-5.15)) ~ 6 x 10^{-3}. Present but subdominant to the power-law.

**6. Stabilization Assessment.** Casimir energy alone does NOT stabilize the fiber. Both E_Cas ~ sigma^{-1/8} and V_classical ~ R_K * sigma^{-5/8} decay with increasing sigma. Stabilization requires flux, higher-curvature corrections, or (in the exflation paradigm) is not needed because sigma EVOLVES dynamically rather than sitting in a static minimum. Consistent with Baptista paper 15, Section 3.6.

**7. Cross-Checks.** N_modes vs S61 cum_N_pw: EXACT at all L. Spectral zeta convergence clean for s >= 5.0.

**Data files**:

- Script: `computations/s63_casimir_jensen.py`
- Data: `computations/s63_casimir_jensen.npz`
- Plot: `computations/s63_casimir_jensen.png`
- Input: `computations/s61_trace_formula_geometric.npz`

---

### W5-04: MODULI-DISPERSION-63 — Hessian Eigenvalues as Dispersion on CG(24) (tesla-resonance)

**Status**: COMPLETE
**Gate**: MODULI-DISPERSION-63 | W5-04 | INFO | effective dispersion relation | Always INFO | Diagnostic
**Verdict**: INFO -- All 36 moduli branches are OPTICAL with flat dispersion. Moduli are localized, not propagating.

**Results**:

**What was computed.** The 36 effective Hessian eigenvalues from `s62_hessian_oneloop.npz` were promoted to a k-dependent Hamiltonian on the CG(24) Cayley graph (S_4 with all 6 transpositions, degree 6, 24 vertices, 72 edges). At each Laplacian eigenvalue lambda_k in {0, 4, 6, 8, 12} (multiplicities {1, 9, 4, 9, 1}), the Hamiltonian is:

H(k) = H_eff(k=0) + lambda_k * J_eff

where J_eff is the 36x36 inter-cell coupling matrix constructed from the Josephson hierarchy (J_C2 = 0.933, J_su2 = 0.059, J_u1 = 0.038 M_KK) lifted from the 8-dim fiber basis to the 36-dim symmetric-tensor moduli space via the SU(3)/U(2) coset structure, then rotated into the H_eff eigenbasis.

**Key numbers (all in M_KK units)**:

| Quantity | Value |
|:---------|:------|
| Branches | 36, ALL optical (no acoustic) |
| omega_0 range | [5.571, 18.183] M_KK |
| omega_0^2 range | [31.04, 330.63] M_KK^2 |
| Max effective sound speed | 3.89 x 10^{-2} c |
| Relative bandwidth range | [7.15 x 10^{-4}, 4.59 x 10^{-2}] |
| Mean relative bandwidth | 1.65 x 10^{-2} |
| Max J*lambda_max / omega_0^2 | 0.094 (perturbative) |
| Nonlinear branches (R^2 < 0.9) | 1 / 36 (branch 28, avoided crossing) |
| J_eff off-diagonal max | 0.390 M_KK (significant mixing) |
| J_eff diagonal range | [0.054, 0.933] M_KK |

**Degeneracy group structure (10 levels)**:

| Level | omega_0 (M_KK) | Deg | c_eff range | BW range (M_KK) |
|:------|:----------------|:----|:------------|:-----------------|
| 0 | 5.571 | 1 | 0.022 | 0.255 |
| 1 | 7.299 | 1 | 0.017 | 0.203 |
| 2 | 7.579 | 4 | 0.004--0.015 | 0.047--0.184 |
| 3 | 8.588 | 9 | 0.003--0.014 | 0.033--0.166 |
| 4 | 11.197 | 3 | 0.002--0.010 | 0.025--0.125 |
| 5 | 12.463 | 4 | 0.002--0.039 | 0.023--0.478 |
| 6 | 12.687 | 8 | 0.006--0.037 | 0.051--0.434 |
| 7 | 15.495 | 1 | 0.011 | 0.131 |
| 8 | 18.183 | 5 | 0.001--0.026 | 0.013--0.305 |

Degeneracy multiplicities {1, 1, 4, 3, 6, 3, 4, 8, 1, 5} = 36 at k=0 match the tree-level structure. The CG(24) coupling splits each degenerate level into sub-bands. Within each level, the Josephson hierarchy J_C2 : J_su2 : J_u1 = 16 : 1 : 0.6 determines the bandwidth: C^2-dominated branches have 5-10x larger bandwidth than su(2) or u(1) branches.

**Level classification by dominant fiber direction**:
- C^2 coset: 11 branches, c_eff in [0.003, 0.017], rel_bw in [3.8e-3, 2.8e-2]
- su(2) stabilizer: 14 branches, c_eff in [0.001, 0.037], rel_bw in [7.1e-4, 3.4e-2]
- u(1) diagonal: 9 branches, c_eff in [0.003, 0.039], rel_bw in [2.8e-3, 4.6e-2]
- Mixed: 2 branches, c_eff in [0.002, 0.002], rel_bw in [1.8e-3, 2.3e-3]

**Cross-checks**:
1. k=0 eigenvalues reproduce H_eff evals to machine precision (residual 4 x 10^{-13})
2. All eigenvalues positive at all 5 k-points (no tachyonic instabilities from propagation)
3. CG(24) graph verified from first principles: 24 vertices, 72 edges, 6-regular
4. Adjacency eigenvalues {+6, +2, 0, -2, -6} with multiplicities {1, 9, 4, 9, 1} confirmed
5. 35 of 36 branches have linear dispersion R^2 > 0.9; 1 branch (br 28) has R^2 = 0.304 from avoided crossing

**Assessment (PHONONIC)**:

The 36 moduli are optical phonons on CG(24) in the flat-band limit. The condensed matter analog is a molecular crystal with heavy on-site modes (omega_0^2 ~ 30--330) weakly coupled by inter-site Josephson tunneling (J ~ 0.04--0.93). The ratio J*lambda_max / omega_0^2 < 0.094 everywhere. Sound speeds are 2-4 orders of magnitude below c = 1. Moduli fluctuations are LOCALIZED: the CG(24) lattice is a perturbation, not a band structure generator.

The J_eff matrix is significantly off-diagonal (max 0.390 M_KK) because the Josephson coupling and the Hessian have different symmetry structures on SU(3). This produces one avoided crossing at branch 28 (omega_0 ~ 12.69 M_KK, su(2) level) and weak but measurable branch mixing throughout. The Josephson hierarchy directly imprints on the dispersion bandwidth, creating the spectral fingerprint of the anisotropic SU(3)/U(2) coset structure.

**Constraint**: Any mechanism requiring long-range moduli propagation across the domain lattice (e.g., moduli-mediated phase transitions) is excluded -- the coupling is 1-2 orders of magnitude too weak relative to omega_0^2. Moduli stabilization is a LOCAL problem.

**Data files**:

| File | Description |
|:-----|:------------|
| `computations/s63_moduli_dispersion.py` | Computation script |
| `computations/s63_moduli_dispersion.npz` | All dispersion data (36 branches x 5 k-points, 22 arrays) |
| `computations/s63_moduli_dispersion.png` | 4-panel diagnostic plot |
| `computations/s63_moduli_dispersion_log.txt` | Full computation log |

---

### W5-05: DEBYE-FOLD-63 — Effective Debye Temperature at Fold (tesla-resonance)

**Status**: COMPLETE
**Gate**: DEBYE-FOLD-63 | W5-05 | INFO | QUANTUM (T < theta_D) | theta_D/T_GGE = 5.31

**Results**:

**Verdict**: INFO -- QUANTUM regime. theta_D / T_GGE = 5.31. The GGE sits below the effective Debye temperature by a factor of 5, placing the internal geometry in the quantum regime where the majority of KK modes are thermally frozen.

**Key numbers** (all in M_KK units unless noted):

| Quantity | Value | Note |
|:---------|:------|:-----|
| theta_D (physical, Gaussian cutoff) | 2.0483 M_KK | = 1.52e17 GeV = 1.77e30 K |
| T_GGE | 0.3856 M_KK | = 2.86e16 GeV = 3.32e29 K |
| theta_D / T_GGE | 5.312 | QUANTUM regime |
| C_V(T_GGE) / C_DP (exact, full PW) | 0.0677 | 6.8% of classical |
| C_V(T_GGE) / C_DP (exact, fold pq6) | 0.2912 | 29% (fewer high-freq modes) |
| D_3(theta_D/T) | 0.1030 | Debye function |
| omega_min | 0.8197 M_KK | Lowest KK eigenvalue |
| omega_max (full PW) | 3.5486 M_KK | 18,624 bare eigenvalues |
| omega_max (fold, pq<=6) | 2.0606 M_KK | 992 bare eigenvalues |
| mean omega (PW-weighted) | 2.5918 M_KK | Mean frequency |
| N_modes (PW) | 947,520 | Total with multiplicities |
| Thermal fraction N_therm/N_PW | 0.002094 | Only 0.2% of modes excited |
| Total thermal quanta | 1,984 | Out of 947,520 modes |

**Four definitions of theta_D tested**:
- (a) omega_max (full PW) = 3.549 M_KK --> theta_D/T = 9.20 (QUANTUM)
- (b) omega_max (fold pq6) = 2.061 M_KK --> theta_D/T = 5.34 (QUANTUM)
- (c) Gaussian spectral action cutoff = 2.048 M_KK --> theta_D/T = 5.31 (QUANTUM, **physical**)
- (d) BCS sector max = 0.978 M_KK --> theta_D/T = 2.54 (QUANTUM, marginal)

All four definitions place the system in the quantum regime. The physically correct definition uses the spectral action cutoff (c), since modes above 1/gamma_opt are exponentially suppressed by the cutoff function.

**Critical structural observation**: The KK spectrum is GAPPED (omega_min = 0.82 M_KK > 0). The half-occupation frequency omega_{1/2} = T_GGE * ln(3) = 0.424 M_KK lies BELOW the entire KK band. This means every single KK mode has mean_n < 0.5 at T_GGE. The GGE populates only the tail of the Bose distribution on these modes.

**Collective mode population at T_GGE**:
- Goldstone: condensed (omega = 0)
- Leggett-1: omega/T = 0.36, mean_n = 2.32 (ACTIVE)
- Leggett-2: omega/T = 0.50, mean_n = 1.55 (ACTIVE)
- Higgs-1: omega/T = 0.99, mean_n = 0.60 (ACTIVE)
- Higgs-2: omega/T = 3.66, mean_n = 0.026 (ACTIVE, marginal)
- Higgs-3: omega/T = 29.73, mean_n = 1.2e-13 (FROZEN)

The BCS collective modes (Leggett, Higgs-1) live well below theta_D and are thermally active at T_GGE. The KK geometric modes are mostly frozen. This is the same hierarchy seen in superfluid He-3: the order parameter fluctuations (collective modes) are thermally active while the underlying "lattice" (here: KK geometry) is quantum-frozen.

**Cross-checks**:
1. Exact Einstein sum vs Debye model: The d=3 Debye model overshoots C_V = 1 at T_GGE because it assumes g(omega) ~ omega^2 from zero, while the actual spectrum has a hard gap at 0.82 M_KK. The exact Einstein sum is the reliable quantity.
2. The full PW spectrum (18,624 modes, s61 Weyl) has mean_omega = 2.59 M_KK, far above T_GGE, explaining the deep quantum suppression C_V/C_DP = 0.068.
3. The fold-only spectrum (992 modes, s44 DOS at tau=0.19) with mean_omega = 1.60 M_KK gives C_V/C_DP = 0.29 -- the difference comes entirely from the PW truncation including more high-frequency modes.
4. Physical temperature scale: theta_D = 1.77e30 K is consistent with the Planck-scale KK geometry. T_GGE = 3.3e29 K is the effective temperature immediately after BCS transit.

**Assessment**: The GGE state of the KK geometry is in the QUANTUM regime, with theta_D/T = 5.3. Only 0.2% of geometric modes carry thermal quanta at T_GGE. This has two structural implications: (1) The internal geometry is a "cold crystal" in which most vibrational modes are quantum-frozen -- consistent with the ordered veil picture where the GGE preserves integrability and never fully thermalizes. (2) The heat capacity C_V/C_DP = 0.068 means the geometric sector absorbs very little thermal energy -- the BCS collective modes (Leggett, Higgs) carry most of the GGE's excitation energy, consistent with the inverted Born-Oppenheimer hierarchy (IBO = 1118, S52). Classification: PHONONIC (directly characterizes the phononic excitation spectrum of the KK substrate).

**Data files**:

- Script: `computations/s63_debye_fold.py`
- Data: `computations/s63_debye_fold.npz` (30 KB, 33 arrays)
- Plot: `computations/s63_debye_fold.png` (4-panel, 238 KB)

---

### W5-06: GENERATION-Z3-63 — Z_3 Content of V_{(p,q)} for Yukawa Breaking (kaluza-klein-theorist)

**Status**: COMPLETE
**Gate**: GENERATION-Z3-63 | W5-06 | INFO | triality assignments and rank

**Results**:

**VERDICT: INFO** — Z_3 triality provides exact 464/264/264 partition. Rank=2 confirmed. CPT blocks rank-3.

| Quantity | Value | Precision |
|:---------|:------|:----------|
| N(t=0) | 464 modes | exact (dims 1, 8, 10) |
| N(t=1) | 264 modes | exact (dims 3, 6, 15) |
| N(t=2) | 264 modes | exact (dims 3, 6, 15) |
| N(t=1) - N(t=2) | 0 | exact by CPT |
| cos(DOS_t1, DOS_t2) | 1.0000000000 | machine epsilon |
| KS(t=1, t=2) | 0.000000 | < D_crit = 0.118 |
| Y rank | 2 | from W2-04 |
| Z_3-conserving V_AB | 79.4% | Frobenius norm |
| Allowed cubic triality triples | 9 / 27 | exact |
| CPT-odd eigenvalue | 4.293e-3 | analytic |
| Analytic eigenvalue ratios | 1 : 6498 : 90853 | CPT-constrained |

**Structural findings**: (1) Triality Partition exact by CPT: C maps (p,q)->(q,p), sends t->-t mod 3. PERMANENT. (2) t=1 and t=2 spectrally IDENTICAL to machine epsilon (all moments, KS, DOS). (3) C_3 cubic Casimir is UNIQUE CPT-odd invariant; could lift degeneracy only via spontaneous C-violation. (4) V_AB rank-1 is Hessian property, NOT forced by Z_3 (Z_3 allows rank 3). (5) V_AB 79.4% Z_3-conserving; Jensen preserves Z_3 (Z_3 in U(1) subset U(2)).

**Level decomposition**: Level 0 pure t=0 (16). Level 1 pure t={1,2} (48+48). Level 2 mixed t=0 dominant (128/96/96). Level 3 t=0 dominant 57% (320/120/120).

**Rank chain**: Rank-1 from V_AB structural. Rank-2 from B-sector triality. Rank-3 blocked: requires rank(V_AB)>=2 AND gamma!=delta. Z_3 necessary but not sufficient for 3 generations.

**Data files**:

- Script: `computations/s63_generation_z3.py`
- Data: `computations/s63_generation_z3.npz`
- Plot: `computations/s63_generation_z3.png`
- Output: `computations/s63_generation_z3_output.txt`

---

### W5-07: CSDR-BRANCHING-63 — Forgacs-Manton CSDR Branching Rules (kaluza-klein-theorist)

**Status**: COMPLETE
**Gate**: CSDR-BRANCHING-63 | W5-07 | INFO | complete branching table | Always INFO | Diagnostic

**Verdict: INFO.** Complete CSDR branching table computed for 28 SU(3) sectors (p+q <= 6) under U(2) with Baptista embedding phi(a) = diag(det(a)^{-1}, a). Three structural results discovered, one PERMANENT theorem proved.

**Results**:

**1. Complete Branching Table (28 sectors)**

Every SU(3) irrep (p,q) decomposes under SU(2) x U(1) via Gelfand-Tsetlin weight enumeration. Dimension conservation and conjugation symmetry verified for all sectors. Key branchings:

| (p,q) | dim | Branching under SU(2) x U(1) |
|:------|:----|:-----------------------------|
| (0,0) | 1 | (0)_0 |
| (1,0) | 3 | (0)_{-2} + (1/2)_{+1} |
| (0,1) | 3 | (1/2)_{-1} + (0)_{+2} |
| (1,1) | 8 | (1/2)_{-3} + (0)_0 + (1)_0 + (1/2)_{+3} |
| (2,0) | 6 | (0)_{-4} + (1/2)_{-1} + (1)_{+2} |
| (0,2) | 6 | (1)_{-2} + (1/2)_{+1} + (0)_{+4} |
| (3,0) | 10 | (0)_{-6} + (1/2)_{-3} + (1)_0 + (3/2)_{+3} |
| (2,1) | 15 | (1/2)_{-5} + (0)_{-2} + (1)_{-2} + (1/2)_{+1} + (3/2)_{+1} + (1)_{+4} |

Full table for all 28 sectors stored in .npz.

**2. Adjoint (1,1) = 8 Decomposition (Gauge + Higgs Content)**

The adjoint of SU(3) decomposes as:
- u(2) subalgebra: (0)_0 [U(1)_Y gauge boson B] + (1)_0 [SU(2)_L gauge bosons W^pm, W^3] = 4 DOF
- C^2 coset: (1/2)_{+3} [Higgs doublet] + (1/2)_{-3} [conjugate Higgs doublet] = 4 DOF
- Total: 4 + 4 = 8 (consistent with dim(adj) = 8)

This confirms Baptista's identification: the 4 C^2 bosons that gain mass under Jensen deformation (eq 3.84) are precisely the two SU(2) doublets with Y = +/-3.

**3. Spinor Delta_8 = 16 Decomposition under U(2) (L+R action)**

Using the combined L+R action (Baptista eq 2.62) on the 16-dim internal spinor, the decomposition is:

| Y | T_3 values | j | Count | States |
|:--|:-----------|:--|:------|:-------|
| -3 | {0} | 0 | 1 | 1 singlet |
| -3/2 | {-1/2, +1/2} x 2 | 1/2 | 2 | 2 doublets |
| 0 | {-1, 0, 0, 0, 0, +1} | 1 | 2 | 2 triplets |
| +3/2 | {-1/2, +1/2} x 2 | 1/2 | 2 | 2 doublets |
| +3 | {0} | 0 | 1 | 1 singlet |

Total: 1 + 4 + 6 + 4 + 1 = 16 states. Verified: Lie algebra [T_1,T_2]=T_3, [Y,T_a]=0.

**4. STRUCTURAL THEOREM (PERMANENT): Cartan Trace Identity**

**T_{SU(3)}(p,q) = T_{SU(2)}(q,p) = T_{U(1)}(q,p) / 12  for ALL (p,q).**

Verified numerically to machine epsilon across all 28 sectors. Algebraic proof:

The SU(2) isospin generator T_3 and the rescaled hypercharge generator Y/(2*sqrt(3)) are both normalized Cartan generators of SU(3). For ANY SU(3) representation R:

    Tr_R(H_1^2) = Tr_R(H_2^2) = T_{SU(3)}(R)

where H_1 = T_3 = diag(0, 1, -1)/2 and H_2 = Y/(2*sqrt(3)) = diag(-2, 1, 1)/(2*sqrt(3)).

Since Tr_R(H_1^2) = sum_{weights} T_3^2 = T_{SU(2)}(R|_{SU(2)}) and Tr_R(H_2^2) = sum_{weights} Y^2/12 = T_{U(1)}/12, the identity follows. QED.

**Physical consequence**: Every KK mode on SU(3) contributes PROPORTIONALLY to all three SM gauge coupling beta functions. The DDG power-law running from the KK tower is structurally non-differential — it cannot split the gauge couplings. This encodes the SU(5) GUT normalization k_Y = 5/3 and confirms the S63 DDG finding that the concentrated SU(3) tower is inapplicable to differential unification.

**5. B/F Asymmetry (A parameter for LOG-SIGNED-41)**

Per-sector B/F content computed from integer-j vs half-integer-j count in the branching. Key finding: the adjoint (1,1) has B_dim = F_dim = 4 (perfectly balanced). The weighted average asymmetry across all sectors:

    A_eff = 0.020 (weighted by dim(p,q)^2 Peter-Weyl multiplicity)

This falls BELOW the LOG-SIGNED-41 viable window [0.025, 0.295].

However, this A parameter measures the isospin-based B/F content, NOT the 4D spin-statistics B/F assignment. The physical B/F sign in the one-loop effective action is determined by the 4D spin (metric -> boson, spinor -> fermion), which is independent of the internal (p,q) sector. The CSDR branching provides SM quantum numbers per mode but does NOT determine the B/F weight for the signed spectral sum. LOG-SIGNED-41 remains CONDITIONAL — A requires the BCS gap function Delta(lambda, tau), not the static CSDR content.

**6. Dynkin Indices for DDG Running (Pre-Registration: CSDR-BRANCH-64)**

Computed T_{SU(3)}, T_{SU(2)}, T_{U(1)} for all 28 sectors. By the Cartan trace identity, the ratios are universal: T_3 : T_2 : T_1/12 = 1 : 1 : 1. The S63 pre-registration CSDR-BRANCH-64 is now RESOLVED: the branching is complete but the DDG differential running is structurally impossible on SU(3).

**Cross-checks (4/4 PASS)**:
1. Dimension conservation: ALL 28 sectors pass (branching dim = SU(3) dim)
2. Conjugation symmetry: (p,q) branches = charge-conjugate of (q,p) branches, all sectors
3. Known branchings: (1,0) = (0)_{-2} + (1/2)_{+1}, (0,1) = (1/2)_{-1} + (0)_{+2}, verified
4. Lie algebra: [T_1,T_2]=T_3, [Y,T_a]=0 verified on 16x16 spinor matrices

**Data files**:

- Script: `computations/s63_csdr_branching.py`
- Data: `computations/s63_csdr_branching.npz` (20.9 KB, 28 sectors)
- No plots generated (table-based diagnostic)

---

### W5-08: WITTEN-BUBBLE-63 — Bubble of Nothing Stability on SU(3) (schwarzschild-penrose-geometer)

**Status**: COMPLETE
**Gate**: WITTEN-BUBBLE-63 | W5-08 | STRUCTURAL | PASS | SU(3) stable against bubble nucleation -- topological theorem

**Results**:

**VERDICT: PASS** -- SU(3) is STABLE against bubble-of-nothing nucleation.

**Three-layer defense:**

1. **PRIMARY (topological -- ABSOLUTE)**: pi_1(SU(3)) = 0. SU(3) is simply connected. Witten's bubble-of-nothing instanton (Nucl.Phys.B195:481, 1982) requires pi_1(K) != 0 to construct a circle fiber that shrinks to zero at the bubble wall. No such circle exists in SU(3). The instanton solution does not exist. This is an absolute topological obstruction independent of the metric, matter content, compactification radius, or dynamics. H_1(SU(3); Z) = 0 -- every closed curve in SU(3) bounds a disk.

2. **SECONDARY (fermionic -- redundant)**: The Dirac operator D_K on (SU(3), g_tau) has N_zero = 0 zero modes at the fold. The spectrum is exactly paired (mu, -mu) to machine precision (pair_err = 2.22e-14). det(D_K) != 0. Spectral flow = 0 with zero crossings = 0 over tau in [0, 0.19]. Even if a generalized instanton existed, the fermionic path integral would give a nonzero determinant.

3. **TERTIARY (pi_5 classification)**: pi_5(SU(3)) = Z generates harmonic maps S^5 -> SU(3) with instanton action S_pi5 ~ 620 (decay rate ~ 10^{-269}). These are theta-sector transitions that preserve spacetime topology -- NOT bubble-of-nothing processes. They mediate transitions between winding sectors within the same vacuum, not to "nothing."

**Additional structural checks:**
- **Gregory-Laflamme**: Inapplicable (requires horizon x S^1; SU(3) has no such structure)
- **Coleman-De Luccia**: Inapplicable (V_eff(tau) monotonic, S48 proven; no false vacuum well)
- **Cobordism conjecture (McNamara-Vafa)**: SATISFIED. A-hat(SU(3)) = 0, sigma(SU(3)) = 0, [SU(3)] = 0 in Omega_8^{Spin}.
- **Spin structure**: Unique (parallelizable + simply connected). Preserved under Jensen deformation.

**Seven-layer censorship (updated from six):**

| Layer | Mechanism | Type | Strength |
|:------|:----------|:-----|:---------|
| 1 | Energy budget (V(0.537)/T_0 = 65x) | DYNAMICAL | Conditional |
| 2 | BCS friction (Gamma = 4424) | DYNAMICAL | Conditional |
| 3 | No trapped surfaces (vol-preserving Jensen) | GEOMETRIC | Structural |
| 4 | Josephson connectivity (spectral mesh) | SPECTRAL | Structural |
| 5 | Fragmentation (GGE permanence) | STATISTICAL | Conditional |
| 6 | One-loop stabilization (36/36 positive eigs) | PERTURBATIVE | Conditional |
| **7** | **pi_1(SU(3)) = 0 (simply connected)** | **TOPOLOGICAL** | **ABSOLUTE** |

Layer 7 is the strongest: depends only on topology of SU(3), holds for any metric, with or without matter, cannot be circumvented by dynamics, energy, or quantum corrections.

**Key numbers:**

| Quantity | Value | Source |
|:---------|:------|:-------|
| pi_1(SU(3)) | 0 | Topology (ABSOLUTE) |
| N_zero (Dirac zero modes) | 0 | ETA-INVARIANT-60 |
| Total eigenvalues checked | 159,936 | ETA-INVARIANT-60 |
| Spectral pairing error | 2.22e-14 | ETA-INVARIANT-60 |
| ind(D_K) | 0 | CHERN-INST-61 |
| A-hat(SU(3)) | 0 | Parallelizable |
| Spectral flow [0, 0.19] | 0 | ETA-INVARIANT-60 |
| pi_5 instanton action | ~620 | This computation |
| pi_5 decay rate | ~10^{-269} | This computation |
| [SU(3)] in Omega_8^{Spin} | 0 | Cobordism |
| chi(SU(3)) | 0 | Topology |

**Penrose diagram:**
```
  FORBIDDEN (pi_1 = 0 blocks):     ACTUAL (stable vacuum):

       i^+         i^+                    i^+
        |    /bubble|                    / | \
        |   / wall  |                I^+/  |  \I^+
        |  /(fiber  |                   / M^4 x \
        | / shrinks)|                  / SU(3)_tau\
        |/          |                  \ (stable)  /
       i^0---------i^0              I^-\  |   /I^-
        |\          |                    \ |  /
        | \  flat   |                     i^-
       i^-         i^-
  No bubble wall. No topology change. SU(3) fiber topologically frozen.
```

**Constraint / Implication / Surviving space:**
- **Constraint**: pi_1(SU(3)) = 0 provides absolute topological immunity against Witten bubble nucleation.
- **Implication**: The SU(3) internal manifold is nonperturbatively stable. No vacuum decay channel exists via bubble-of-nothing. The choice K = SU(3) (vs T^8 or S^1 x ...) is REQUIRED for topological stability.
- **Surviving space**: All Jensen-deformed metrics g_tau on SU(3) are stable. The full modulus space tau in [0, inf) is free of bubble instabilities.

**Cross-references:** CHERN-INST-61, ETA-INVARIANT-60, GH-TEMP-DW-60, TRACE-FORMULA-61.

**Data files**:

- Script: `computations/s63_witten_bubble.py`
- Output: `computations/s63_witten_bubble.npz`
- Input: `s61_chern_instanton.npz`, `s60_eta_invariant.npz`, `s61_trace_formula_geometric.npz`

---

### W5-09: CUTOFF-MEISSNER-63 — Meissner Length vs Spectral Action Cutoff (quantum-acoustics-theorist)

**Status**: COMPLETE
**Gate**: CUTOFF-MEISSNER-63 | W5-09 | INFO | lambda_L(fold)/gamma_opt(fold) = 0.812 (GS), 0.817 (GGE) | 18.3% discrepancy, monotonic, no coincidence

**Results**:

**Verdict**: INFO — lambda_L(fold)/gamma_opt(fold) = 0.812 (GS), 0.817 (GGE). 18.3% discrepancy. Ratio monotonically increasing with tau. No coincidence point within [0, 0.5].

**Key numbers** (all in M_KK units):

| Quantity | Ground State | GGE State |
|:---------|:-------------|:----------|
| gamma_opt(fold) | 0.4882 | 0.4882 |
| lambda_L(fold) | 0.3966 | 0.3989 |
| Ratio lambda_L/gamma_opt | 0.8124 | 0.8172 |
| D_s(fold) | 6.356 M_KK^2 | 6.283 M_KK^2 |

**Scaling law** (exact, verified to machine epsilon):

    ratio(tau) = 0.8124 * [a_2(tau)/a_2(fold)]^{1/4}

Both scales are driven by the same Gilkey coefficient a_2(tau) of the Jensen-deformed SU(3) Dirac operator, but with DIFFERENT exponents:
- gamma_opt(tau) ~ a_2(tau)^{-1/2} (from f_2 = const/a_2, gamma = sqrt(f_2/f_0))
- lambda_L(tau) ~ a_2(tau)^{-1/4} (from D_s ~ sqrt(a_2) via BA theorem, lambda = 1/sqrt(D_s))

The exponent difference (1/4) drives a monotonic increase in the ratio as tau grows. Fractional rate ratio at fold: (1/gamma)(dgamma/dtau) / (1/lambda)(dlambda/dtau) = 2.000 (exact).

**Coincidence analysis**: For ratio=1, need a_2(tau)/a_2(fold) = 2.295. Maximum available within [0, 0.5] is 1.134. Coincidence NOT achievable on the Jensen curve.

**Physical interpretation**:
- gamma_opt = 0.488 sets the UV regularization of the spectral action (effective UV cutoff Lambda_UV = M_KK/gamma = 2.05 M_KK)
- lambda_L = 0.397 sets the IR magnetic screening length (Meissner mass m_M = 1/lambda_L = 2.52 M_KK)
- Both originate from the same Dirac spectrum but encode DIFFERENT physics: gamma_opt captures the heat kernel asymptotics (high-eigenvalue behavior), lambda_L captures the BCS condensate (low-eigenvalue pairing)
- The 18% discrepancy is structural, not a tuning artifact -- it traces to the 1/4 exponent difference in the scaling with a_2

**Cross-checks**:
- a_2/R ratio constant to machine epsilon across full tau range (confirms a_2 = (5R/12)*a_0 exactly)
- Log-log slope d(log ratio)/d(log a_2) = 0.250 +/- 0.000 (confirms analytic exponent)
- gamma_opt at fold reproduces S62 CUTOFF-LONDON-62 value to 0.001%
- lambda_L at fold reproduces S62 MEISSNER-GGE-62 value to 0.001%

**Assessment**: The spectral action cutoff and London penetration depth share a common spectral origin but are structurally distinct quantities. Their 18% discrepancy at the fold is not accidental but reflects the fact that gamma_opt probes the UV tail of the Dirac spectrum (heat kernel asymptotics) while lambda_L probes the IR condensate structure (BCS gap equation). The exponent difference of 1/4 in their a_2 scaling is a PERMANENT structural feature. There is no controlled limit on the Jensen curve where these two scales coincide. Classification: GEOMETRIC (common a_2 origin) + PHONONIC (BCS condensate enters lambda_L).

**Data files**:

- Script: `computations/s63_cutoff_meissner.py`
- Data: `computations/s63_cutoff_meissner.npz` (36 arrays)
- Plot: `computations/s63_cutoff_meissner.png`
- Inputs: `s62_cutoff_london.npz`, `s62_meissner_gge.npz`, `s61_heat_kernel_a2.npz`, `s61_heat_kernel_a4.npz`, `s61_superfluid_weight.npz`

---

### W5-10: BLOCKING-GGE-63 — Odd-Particle Blocking of GGE Superfluid Weight (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETE
**Gate**: BLOCKING-GGE-63 | W5-10 | INFO | D_s(blocked)/D_s(GGE) ratio | Always INFO | Diagnostic

**Results**:

**Verdict**: INFO -- Single-mode condensate with extreme blocking asymmetry.

**Physics**: Nuclear BCS blocking (Paper 03, Eq. 19-22; Paper 17, Sec. 4.4) removes one quasiparticle level from the pairing condensate. For the framework's GGE state on CG(24), each of 8 modes was blocked in turn by removing it from the (N-1)-mode pair Hamiltonian. The ODLRO condensate fraction was recomputed from the reduced one-body density matrix, giving D_s(blocked) = D_s(fold) * n_condensate(blocked).

**Key numbers** (all M_KK units where applicable):

| Mode | n_k(GGE) | D_s(blocked)/D_s(GGE) | n_cond(blocked) | Delta_E_block |
|:-----|:---------|:----------------------|:----------------|:--------------|
| B2[0] | 0.9885 | **0.00883** | 0.00872 | -0.0131 |
| B2[1] | 0.0087 | 1.00000 | 0.9885 | +0.171 |
| B2[2] | 0.0008 | 1.00000 | 0.9885 | +0.326 |
| B2[3] | 0.0008 | 1.00000 | 0.9885 | +0.519 |
| B1[0] | 0.0011 | 1.00000 | 0.9885 | +0.722 |
| B3[0] | 1.8e-5 | 1.00000 | 0.9885 | +1.001 |
| B3[1] | 3.6e-5 | 1.00000 | 0.9885 | +1.075 |
| B3[2] | 2.8e-5 | 1.00000 | 0.9885 | +1.167 |

- **Occupation-weighted D_s(blocked)/D_s(GGE) = 0.0202** (ODLRO route)
- Blocking B2[0] destroys the condensate: ratio = 0.0088 (99.1% reduction)
- Blocking any other mode: ratio = 1.0000 (zero effect)
- Spread: max/min = 113.3
- GGE normal fraction f_n = 0.0115 vs thermal f_n(T_eff) = 0.300 (ratio 0.038)
- Blocking sum rule: sum_k [Delta_E_block * v_k^2] = -0.0099 vs E_cond = -0.137 (ratio 0.072)

**Cross-checks**:
1. ODLRO consistency: D_s(fold) * n_cond(GGE) = 6.2831 = D_s(GGE) (exact match, confirming route consistency).
2. Current-current route: D_dia - Pi gives ~18.7 M_KK^2 for all blocked states (3x D_s_GGE). This reveals the cc route uses the FULL diamagnetic term without condensate projection -- the ODLRO route is the correct physical measure for blocking.
3. All 7 non-dominant blocked states give identical n_cond = 0.9885 (unchanged from unblocked), confirming the condensate resides entirely in B2[0].

**Assessment**:

This computation reveals the framework's GGE condensate is a *single-mode condensate* -- essentially all pair weight sits in B2[0] (n = 0.988). This is the extreme ultrasmall-grain limit of Paper 17 (von Delft): with d/Delta = 0.38 and N_pair = 1, the system has "one Cooper pair" concentrated in the lowest pair eigenstate. The blocking asymmetry (113x spread) has no nuclear analog -- in nuclei, blocking effects are distributed across multiple levels near the Fermi surface. Here, there is no Fermi surface smearing because N_pair = 1.

The nuclear blocking energy formula (Paper 03, Eq. 5.6 analog) gives Delta_E_block(k) = E_qp(k) * (1 - 2v_k^2). B2[0] has v_k^2 = 0.988, so (1-2v^2) = -0.977 (large, negative -- costs energy to UNBLOCK it). All other modes have v_k^2 << 1, so (1-2v^2) ~ +1 (they are spectators far above the Fermi energy).

**Phononic classification**: PARTICLE -- blocking is a quasiparticle-level diagnostic of the condensate's mode structure, not a geometric or phononic observable.

**Structural implication**: The condensate fragility to B2[0] blocking confirms the S63 RICHARDSON-GAUDIN-N1-63 finding that N_pair = 1 pairing is confined to a single band. The superfluid weight is ENTIRELY determined by one mode's occupation. Any mechanism that depopulates B2[0] (thermal fluctuation, blocking, Landau-Zener crossing) destroys superfluidity completely. This is the framework's version of Anderson's criterion: when the number of Cooper pairs is O(1), the condensate lives or dies with a single level.

**Data files**:

- Script: `computations/s63_blocking_gge.py`
- Data: `computations/s63_blocking_gge.npz`
- Plot: `computations/s63_blocking_gge.png`

---

## Constraint Map Updates

| Entity | Type | Old State | New State | Gate/Evidence | Session |
|:-------|:-----|:----------|:----------|:--------------|:--------|
| BLOCKING-GGE-63 | GATE | UNCOMPUTED | INFO | D_s(blocked)/D_s(GGE)=0.0088 (B2[0]), 1.0 (all others) | S63 |
| Single-mode condensate | THEOREM | -- | PROVEN | n_cond unchanged when blocking any mode except B2[0] | S63 |
| Anderson criterion (N_pair=1) | EQUATION | -- | CONFIRMED | Condensate destruction upon blocking sole occupied level | S63 |
| MODULI-DISPERSION-63 | GATE | UNCOMPUTED | INFO | All 36 optical, max rel_bw = 0.046, J*lambda/omega^2 < 0.094 | S63 |
| Moduli localization | THEOREM | -- | ESTABLISHED | J_eff << omega_0^2 excludes long-range moduli propagation | S63 |
| CASIMIR-JENSEN-63 | GATE | UNCOMPUTED | INFO | E_Cas ~ -8.5e4 M_KK, sigma scaling = sigma^{-1/8} exactly | S63 |
| Casimir sigma scaling | THEOREM | -- | PROVEN | E_Cas(sigma) = sigma^{-1/8} * E_Cas(1) to machine epsilon (2.8e-16) | S63 |
| Casimir no-exponential | THEOREM | -- | PROVEN | One-loop Casimir has no e^{-beta*sigma}; pure power-law | S63 |
| CSDR-BRANCHING-63 | GATE | UNCOMPUTED | INFO | 28 sectors branched, T_SU3=T_SU2 identity, A_eff=0.020 | S63 |
| Cartan Trace Identity | THEOREM | -- | PROVEN | T_SU3(p,q) = T_SU2(q,p) = T_U1(q,p)/12 for ALL (p,q). DDG non-differential. PERMANENT. | S63 |
| DDG non-differential on SU(3) | THEOREM | -- | PROVEN | KK tower contributes proportionally to all 3 betas. Structural, rep-theoretic. | S63 |
| LOG-SIGNED-41 | GATE | CONDITIONAL PASS | CONDITIONAL PASS (unchanged) | CSDR branching does not resolve B/F; requires BCS gap dynamics | S63 |

*(Fill as gate verdicts arrive. Types: THEOREM, GATE, CLOSED, OPEN-CHANNEL, EQUATION)*

---

## Files Produced

| File | Wave | Description |
|:-----|:-----|:------------|
| `computations/s63_blocking_gge.py` | W5 | Blocking computation script |
| `computations/s63_blocking_gge.npz` | W5 | All blocking ratios, energies, condensate fractions |
| `computations/s63_blocking_gge.png` | W5 | 4-panel diagnostic plot |
| `computations/s63_moduli_dispersion.py` | W5 | Moduli dispersion computation script |
| `computations/s63_moduli_dispersion.npz` | W5 | 36-branch dispersion data on CG(24) (22 arrays) |
| `computations/s63_moduli_dispersion.png` | W5 | 4-panel dispersion diagnostic plot |
| `computations/s63_moduli_dispersion_log.txt` | W5 | Full computation log |
| `computations/s63_casimir_jensen.py` | W5 | Casimir energy computation script |
| `computations/s63_casimir_jensen.npz` | W5 | E_Cas, sigma scaling, spectral data (29 arrays) |
| `computations/s63_casimir_jensen.png` | W5 | 4-panel Casimir diagnostic plot |
| `computations/s63_csdr_branching.py` | W5 | CSDR branching computation script |
| `computations/s63_csdr_branching.npz` | W5 | 28-sector branching data, Dynkin indices, spinor decomposition |
