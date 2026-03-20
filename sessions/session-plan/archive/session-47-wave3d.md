## Wave 3d: Superfluid Density Tensor on Jensen-Deformed SU(3) (1 task)

W3-3 closed the character coherence function as a substrate diagnostic — it's 95% truncation-determined. Volovik's response identified the failure mode: state functions (what the system IS) can't detect "near are like." Response functions (how the system RESPONDS) can. The superfluid density tensor ρ_s^{ab}(τ) is the canonical response function for this: it measures the stiffness of the BCS order parameter against phase twists in each of the 8 su(3) directions.

Crucially, ρ_s uses Bogoliubov eigenvectors (fully dynamical, BCS-state-dependent), not characters (kinematic, tau-independent). This avoids the truncation-dominance problem that killed W3-3.

Landau proposed this as S-4 in her collab review. Volovik endorsed it and grounded it in the Peotta-Torma flat-band formula. Now Landau executes.

---

### W3-4: Superfluid Density Tensor (RHOS-TENSOR-47)

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: MEDIUM (BdG eigenvector computation at 5 tau values)

**Prompt**:

You proposed this computation as S-4 in your collab review of the crystal geometry document. Volovik endorsed it as the decisive probe for substrate self-coherence after the character coherence function failed (W3-3: ARTIFACT). Now you execute it.

### Background

The superfluid density tensor ρ_s^{ab} measures the free energy cost of imposing a phase gradient on the order parameter in direction a of the Lie algebra:

  F(q) = F(0) + (1/2) Σ_{ab} ρ_s^{ab} q_a q_b

where q_a is the superfluid momentum (phase twist) in direction a ∈ su(3). This is a RESPONSE function — it tells you how RIGID the condensate is along each geometric direction. It is NOT a Fourier property of the wavefunction; it requires the Bogoliubov eigenvectors, which are BCS-state-dependent and tau-dependent.

### Why this avoids the W3-3 problem

The character coherence function C(θ; τ) was dominated by characters (tau-independent basis functions), with BCS weights contributing only 0.13% dynamical content. The superfluid density tensor is constructed from:

1. **Bogoliubov eigenvectors** (u_k, v_k) — these ARE the BCS state, fully tau-dependent
2. **Current matrix elements** ⟨k|J_a|k'⟩ — these couple eigenstates through the Lie algebra generators
3. **Energy denominators** 1/(E_k + E_k') — these weight contributions by the BdG spectrum

None of these are character-based. The entire computation is in the BdG eigenvector space, not the Peter-Weyl character space.

### The Peotta-Torma Formula

For a multi-band BCS system with flat or narrow bands, the superfluid weight (Peotta-Torma, 2015) is:

  D_s^{ab} = Σ_{k,n≠m} [f(E_n) - f(E_m)] / [E_m - E_n] × ⟨n,k|J_a|m,k⟩⟨m,k|J_b|n,k⟩

At T=0 this simplifies using the BdG eigenvectors. For the BCS state on SU(3), the "bands" are the Dirac eigenvalue sectors (B1/B2/B3) and the "momentum" is the representation label (p,q).

For a more direct approach, use the standard BCS superfluid density:

  ρ_s^{ab} = Σ_k (Δ_k² / E_k³) × ⟨k|J_a|k⟩⟨k|J_b|k⟩ + (interband terms)

where E_k = sqrt(ξ_k² + Δ_k²) is the BdG quasiparticle energy, and J_a is the current operator for direction a in su(3).

### Verified data locations

**s46_number_projected_bcs.npz**:
- `Delta_bcs_fold: shape=(3,)` — [0.372, 0.732, 0.084] gaps per sector
- `v2_bcs: shape=(3,)` — [0.045, 0.122, 0.002] occupations per sector
- `V_mat_constrained: shape=(3,3)` — sector V matrix
- `lam2_fold: shape=(3,)` — [0.672, 0.714, 0.944] eigenvalues² per sector

**s46_qtheory_selfconsistent.npz**:
- `Delta_B1_sc: shape=(60,)`, `Delta_B2_sc: shape=(60,)`, `Delta_B3_sc: shape=(60,)`
- `tau_scan: shape=(60,)` — 60-point tau grid
- `lam2_B1_interp: shape=(60,)`, `lam2_B2_interp: shape=(60,)`, `lam2_B3_interp: shape=(60,)`

**s44_dos_tau.npz** — eigenvalues at 5 tau values:
- `tau0.XX_all_omega: shape=(992,)` and `tau0.XX_all_dim2: shape=(992,)` at tau = 0.00, 0.05, 0.10, 0.15, 0.19

**s47_curvature_anatomy.npz** (from W2-2):
- Curvature data for cross-referencing: do soft curvature directions have low ρ_s or high ρ_s?

**tier0-computation/canonical_constants.py**

### Computation Steps

1. **Set up the current operators.** The current operator for direction a ∈ su(3) acting on the Dirac eigenspace is:

   J_a = representation of X_a on the spinor bundle

   In the (0,0) Peter-Weyl sector, J_a acts on the 16-dimensional spinor space via the gamma matrices and structure constants. For the 8-mode model (1 B1 + 4 B2 + 3 B3):
   - J_a is an 8×8 matrix for each of the 8 su(3) generators
   - Matrix elements ⟨k|J_a|k'⟩ connect different modes

   The simplest approach: use the Dirac operator structure. The current in direction a is related to the derivative of D_K with respect to the metric in direction a. For left-invariant metrics, this is:

   J_a = ∂D_K/∂(metric component g_{aa})

   Alternatively, in the Peter-Weyl basis, J_a = ρ(X_a) ⊗ I_spinor (the representation matrix of generator X_a acting on the PW component, tensored with identity on the spinor).

   For the (0,0) sector: ρ(X_a) = 0 (trivial rep), so the (0,0) contribution to interband current vanishes. The current matrix elements come from HIGHER (p,q) reps where ρ(X_a) is nontrivial.

2. **Compute the BdG spectrum at each tau.** At each of the 5 tau values with full eigenvalue data:
   - Eigenvalues ξ_k = |λ_k| (with mu=0)
   - Gaps Δ_k = Delta_sector(k) (from sector assignment)
   - BdG energies E_k = sqrt(ξ_k² + Δ_k²)
   - BdG amplitudes u_k² = (1/2)(1 + ξ_k/E_k), v_k² = (1/2)(1 - ξ_k/E_k)

3. **Compute ρ_s^{ab} in the sector-diagonal approximation.** Start with the simplest version: ignore interband (cross-sector) current matrix elements. In this approximation:

   ρ_s^{ab}(τ) = Σ_k (Δ_k² / E_k³) × |⟨k|J_a|k⟩|² × δ_{ab}

   This gives the DIAGONAL elements of the 8×8 tensor. If J_a is diagonal in the eigenvalue basis (which it may not be), this captures the leading contribution.

4. **Compute the full 8×8 tensor if feasible.** The off-diagonal elements require interband current matrix elements ⟨k|J_a|k'⟩ for k ≠ k'. These come from the Dirac operator structure. In the 8-mode model, the 8×8 J_a matrices can be constructed from the Dirac matrix in the Peter-Weyl basis.

   If the full matrix construction is too complex, report the diagonal approximation and flag the off-diagonal elements as a follow-up.

5. **Extract physical observables.**
   - **Eigenvalues of ρ_s**: the 8 eigenvalues of the ρ_s tensor. Are they degenerate? Do they split by sector (B1/B2/B3)?
   - **Anisotropy**: ratio of largest to smallest eigenvalue. Compare to the curvature anisotropy (K_max/K_min = 12.5).
   - **Sector decomposition**: what fraction of the total ρ_s comes from B1, B2, B3?
   - **tau dependence**: how do the eigenvalues change across the 5 tau values?

6. **The decisive correlation.** Plot ρ_s eigenvalues vs tau. Compare to Delta_B2(τ). Unlike the character coherence function (which was 0.13% dynamical), ρ_s should have O(1) tau-dependence because it's built from Δ²/E³ which depends strongly on the gap.

   Also: cross-reference the ρ_s anisotropy pattern with the curvature anatomy. Do the soft curvature directions (su(2)-C², K=0.010) correspond to HIGH or LOW superfluid stiffness? If high ρ_s in soft directions → the condensate is RIGID where the geometry is soft → "near are like" is dynamically enforced.

7. **Visualize.**
   - **Plot A**: ρ_s eigenvalues vs tau (5 points). Color by su(3) direction type (u(1), su(2), C²).
   - **Plot B**: ρ_s anisotropy pattern at the fold — bar chart of all 8 eigenvalues, labeled by direction, with curvature K overlaid for comparison.
   - **Plot C**: ρ_s(B2 component) vs Delta_B2 scatter plot. Is the response function dynamically determined?

### Pre-registered gate RHOS-TENSOR-47
- **PASS**: ρ_s eigenvalue variation across tau > 10% AND anisotropy > 5 at the fold
- **INFO**: Eigenvalue variation > 10% but anisotropy < 5 (isotropic but dynamical)
- **FAIL**: Eigenvalue variation < 10% (ρ_s is also effectively constant, like C was)

### Output files
- Script: `tier0-computation/s47_rhos_tensor.py`
- Data: `tier0-computation/s47_rhos_tensor.npz`
- Plot: `tier0-computation/s47_rhos_tensor.png`

### Working paper section: W3-4

### Critical notes
- The current operator J_a in the Peter-Weyl basis requires the representation matrices ρ(X_a). For (0,0), these vanish (trivial rep). The superfluid density gets contributions from HIGHER reps where ρ(X_a) ≠ 0. This means ρ_s is dominated by higher PW sectors — the opposite of the character coherence function which was dominated by low sectors.
- mu = 0 (PH symmetry, S34). So ξ_k = |λ_k|.
- The Peotta-Torma formula was designed for flat-band systems where geometric (quantum metric) contributions dominate over conventional (Fermi velocity) contributions. The SU(3) Dirac spectrum has narrow bands (the van Hove singularities), making this formula particularly appropriate.
- If the full 8×8 J_a construction is intractable in one session, compute in the DIAGONAL approximation and report what's missing. A partial result with honest error bars is better than no result.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.
