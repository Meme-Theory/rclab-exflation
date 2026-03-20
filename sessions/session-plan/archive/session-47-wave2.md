## Wave 2: Crystal Geometry Visualization (3 tasks, parallel)

The substrate is SU(3) with a Jensen-deformed left-invariant metric. 47 sessions of spectral computation have characterized it algebraically — eigenvalues, selection rules, curvatures, condensate structure — but no one has drawn it. This wave produces three complementary visualizations of the crystal's geometry at the fold (tau=0.19).

---

### W2-1: Condensate Density on the Maximal Torus (CONDENSATE-T2-47)

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: MEDIUM (harmonic sum over PW reps on 2D grid)

**Prompt**:

You are computing and visualizing the BCS condensate density |Δ(θ₁,θ₂)|² restricted to the maximal torus T² ⊂ SU(3). This shows WHERE on SU(3) the Cooper pairs concentrate — the spatial structure of the order parameter.

**Background**: The maximal torus of SU(3) is the set of diagonal unitary matrices:

  g(θ₁,θ₂) = diag(e^{iθ₁}, e^{iθ₂}, e^{-i(θ₁+θ₂)})

with θ₁, θ₂ ∈ [0, 2π). Every Peter-Weyl harmonic D^{(p,q)}_{mn}(g) restricts to a known weight factor on T²:

  D^{(p,q)}_{mn}(g(θ₁,θ₂)) = δ_{mn} × exp(i(w₁θ₁ + w₂θ₂))

where (w₁,w₂) is the weight of state m in the (p,q) representation. The condensate gap function in the PW basis is:

  Δ(x) = Σ_k Δ_k × ψ_k(x)

where Δ_k is the BCS gap amplitude for mode k and ψ_k is the corresponding eigenmode. On T², this becomes a sum of weighted exponentials.

**Verified data locations**:

- `tier0-computation/s46_number_projected_bcs.npz`:
  - `v2_bcs: shape=(3,)` — [0.045, 0.122, 0.002] per sector
  - `Delta_bcs_fold: shape=(3,)` — [0.372, 0.732, 0.084] BCS gaps per sector
  - `V_mat_constrained: shape=(3,3)` — sector V matrix

- `tier0-computation/s46_rg_pair_transfer.npz`:
  - `mode_eps: shape=(8,)` — eigenvalues
  - `mode_sector: shape=(8,)` — B1/B2/B2/B2/B2/B3/B3/B3
  - `n_occ: shape=(8,)` — per-mode occupations

- `tier0-computation/s44_dos_tau.npz`:
  - `tau0.19_all_omega: shape=(992,)` — full spectrum at fold
  - `tau0.19_all_dim2: shape=(992,)` — PW degeneracies

- `tier0-computation/s47_pi_sector.npz` (from W1-1):
  - Sector assignments per (p,q) rep

- `tier0-computation/canonical_constants.py`

**Computation Steps**:

1. **Build the weight system.** For each (p,q) rep with max_pq_sum ≤ 3, construct the weight diagram of the SU(3) representation. Each weight is a pair (w₁, w₂) in the root lattice. The weights of (p,q) are the integer points in the weight diagram. Use the standard SU(3) weight construction (highest weight (p,q), subtract simple roots to generate all weights with multiplicities).

2. **Construct Δ(θ₁,θ₂).** For each (p,q) rep and each spinor eigenvalue in that rep:
   - Determine the sector (B1/B2/B3) using the rank-based classification from W1-1
   - Assign the BCS gap: Δ_k = Delta_bcs_fold[sector_index]
   - Weight by v_k = sqrt(v2_bcs[sector_index])
   - The contribution to Δ on T² is: Σ_{weights (w₁,w₂)} v_k × Δ_k × exp(i(w₁θ₁ + w₂θ₂))

3. **Compute |Δ|² on a grid.** Evaluate on a 200×200 grid in (θ₁,θ₂) ∈ [0,2π)². Take |Δ(θ₁,θ₂)|².

4. **Plot.** Create a 2D heatmap of |Δ(θ₁,θ₂)|² with:
   - Axes labeled θ₁, θ₂
   - Colorbar showing condensate density
   - Overlay the Weyl chamber boundaries (the fundamental domain of the Weyl group S₃)
   - Mark the identity (θ₁=θ₂=0) and any symmetry points
   - Title: "BCS condensate density on T² ⊂ SU(3) at tau=0.19"

5. **Characterize the pattern.** Is the condensate uniform on T²? Concentrated at specific points? Does it respect the Weyl group symmetry (S₃ permutations of eigenvalues)?

**Pre-registered gate CONDENSATE-T2-47**:
- INFO: Report the condensate pattern. No pass/fail — this is visualization.
- NOTABLE: If the condensate concentrates at specific Weyl chamber vertices or edges.
- NOTABLE: If the pattern has lower symmetry than S₃ (spontaneous breaking on the torus).

**Output files**:
- Script: `tier0-computation/s47_condensate_torus.py`
- Data: `tier0-computation/s47_condensate_torus.npz`
- Plot: `tier0-computation/s47_condensate_torus.png`

**Working paper section**: W2-1

**Critical notes**:
- The maximal torus is the "skeleton" of SU(3). The condensate density on T² captures the angular structure but misses the radial (root direction) structure. This is a projection, not the full picture.
- The spinor structure adds complexity: each eigenvalue corresponds to a spinor-valued harmonic, not a scalar one. The simplest approach is to sum |Δ_k|² × |D^{(p,q)}|² over weights, ignoring spinor phase structure. This gives the condensate DENSITY (not the order parameter itself).
- If the weight construction is too involved, use the CHARACTER of the (p,q) rep on T²: χ_{(p,q)}(θ₁,θ₂) = Σ_weights exp(i(w₁θ₁+w₂θ₂)). Then |Δ|² ∝ Σ_{(p,q)} |Δ_{(p,q)}|² × |χ_{(p,q)}|². This is the density-of-states weighted approach.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.

---

### W2-2: Curvature Anatomy (CURVATURE-ANATOMY-47)

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: MEDIUM (curvature computation at multiple tau)

**Prompt**:

You are computing and visualizing the sectional curvature landscape of Jensen-deformed SU(3). This shows the "body plan" of the crystal — which directions are positively curved (sphere-like), negatively curved (saddle-like), or flat, and how this changes during the Jensen deformation.

**Background**: For a left-invariant metric on SU(3), the sectional curvature K(X,Y) for orthonormal vectors X,Y ∈ su(3) is given by the Milnor formula (1976). At tau=0 (bi-invariant), all sectional curvatures are K = 1/4 (constant curvature). As tau increases, the Jensen deformation breaks this uniformity: root directions scale by e^{2tau} relative to Cartan directions, creating curvature anisotropy.

The Lie algebra su(3) has 8 generators. Under the Cartan decomposition:
- 2 Cartan generators (H₃, H₈ in Gell-Mann convention)
- 6 root generators (E_±α₁, E_±α₂, E_±(α₁+α₂))

The Jensen deformation scales: g(X_root, X_root) = e^{2tau} × g(X_root, X_root)|_{tau=0}, while Cartan directions are unchanged.

**Verified data locations**:

- `tier0-computation/s46_geometric_a2.npz`:
  - Contains Ricci scalar data at the fold

- `researchers/Baptista/13_Baptista_KK_Paper13.md` through `18_Baptista_KK_Paper18.md`:
  - Metric components, structure constants, curvature formulas

- `tier0-computation/canonical_constants.py`:
  - `tau_fold`, structure constants

**Computation Steps**:

1. **Set up the metric.** The left-invariant metric on SU(3) in the basis {X_1,...,X_8} of su(3) is g_ij(tau). Under Jensen deformation:
   - g(H_a, H_b) = delta_{ab} (Cartan: indices a,b ∈ {3,8} in Gell-Mann convention, or equivalently the Cartan subalgebra generators)
   - g(E_α, E_β) = e^{2tau} × delta_{αβ} (root directions)
   - g(H_a, E_α) = 0 (orthogonality)

   Use the structure constants [X_i, X_j] = f^k_{ij} X_k from the su(3) algebra. Import from canonical_constants.py if available, otherwise use the standard Gell-Mann structure constants.

2. **Compute sectional curvatures.** For each pair of basis vectors (X_i, X_j) with i<j (28 pairs), compute K(X_i, X_j) using the Milnor formula for left-invariant metrics:

   K(X,Y) = (1/4)|[X,Y]_m|² - (3/4)|[X,Y]_p|² + terms involving U

   where the exact formula depends on the decomposition. Alternatively, use the O'Neill formula or compute directly from the Riemann tensor R_{ijij}/(g_{ii}g_{jj} - g_{ij}²).

   Compute at tau = 0, 0.05, 0.10, 0.15, 0.19 (matching the 5 tau values in s44_dos_tau).

3. **Classify the 28 sectional curvatures** by type:
   - Cartan-Cartan (1 pair: H₃∧H₈)
   - Cartan-Root (2×6 = 12 pairs)
   - Root-Root, same root space (3 pairs: α₁∧(-α₁), etc.)
   - Root-Root, different root spaces (12 pairs)

4. **Visualize.** Create two plots:

   **Plot A: Curvature rose at the fold.** A polar/bar chart showing K for all 28 sectional curvatures at tau=0.19, colored by type (Cartan-Cartan, Cartan-Root, Root-Root). This is the "shape" of curvature anisotropy.

   **Plot B: Curvature evolution.** Line plot of the 28 (or grouped) sectional curvatures as functions of tau from 0 to 0.19. Shows how the crystal deforms from uniform (K=1/4 at tau=0) to anisotropic.

5. **Report**: Min/max curvature at fold, ratio K_max/K_min, which directions are most/least curved, whether any become negative.

**Pre-registered gate CURVATURE-ANATOMY-47**:
- INFO: Report curvature landscape. No pass/fail.
- NOTABLE: If any sectional curvature becomes negative (saddle directions appear).
- NOTABLE: If the Cartan-Cartan curvature diverges relative to Root-Root.

**Output files**:
- Script: `tier0-computation/s47_curvature_anatomy.py`
- Data: `tier0-computation/s47_curvature_anatomy.npz`
- Plot: `tier0-computation/s47_curvature_anatomy.png`

**Working paper section**: W2-2

**Critical notes**:
- The Milnor formula for left-invariant metrics on Lie groups is the standard reference. For SU(3), the computation is explicit once the structure constants and metric are specified.
- At tau=0, K=1/4 for all sectional curvatures (bi-invariant metric on simple group, normalized).
- The Jensen deformation preserves volume (S12 result), so the scalar curvature integrates to a topological invariant. But sectional curvatures can redistribute.
- Baptista Paper 13 (section 5) has explicit curvature formulas for the Jensen family. CHECK THERE FIRST before deriving from scratch.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.

---

### W2-3: Spectral Landscape Figure (SPECTRAL-LANDSCAPE-47)

**Agent**: `spectral-geometer`
**Model**: opus
**Cost**: LOW (visualization of existing data)

**Prompt**:

You are creating a publication-quality spectral landscape figure showing all 992 Dirac eigenvalues at the fold, annotated with sector structure, pi-phase topology, and BCS pairing information. This is the "fingerprint" of the crystal.

**Verified data locations**:

- `tier0-computation/s44_dos_tau.npz`:
  - `tau0.19_all_omega: shape=(992,)` — all eigenvalues |λ| at fold
  - `tau0.19_all_dim2: shape=(992,)` — PW degeneracy of each eigenvalue

- `tier0-computation/s47_pi_sector.npz` (from W1-1):
  - `pi_phase_eigenvalues` — |eigenvalue| for each of the 13 pi-phase states
  - `pi_phase_sectors` — B1/B2/B3 label for each
  - `pi_phase_reps` — (p,q) rep label for each
  - `pw_pi_B1`, `pw_pi_B2`, `pw_pi_B3`

- `tier0-computation/s46_number_projected_bcs.npz`:
  - `Delta_bcs_fold: shape=(3,)` — [0.372, 0.732, 0.084] BCS gaps
  - `v2_bcs: shape=(3,)` — [0.045, 0.122, 0.002] occupations

- `tier0-computation/s46_berry_phase.npz`:
  - Per-(p,q) berry phase arrays (for context)

- `tier0-computation/canonical_constants.py`

**Computation Steps**:

1. **Load the 992-mode spectrum.** From s44_dos_tau: tau0.19_all_omega and tau0.19_all_dim2.

2. **Sector-color the spectrum.** Assign each of the 992 eigenvalues to B1/B2/B3 using the rank-based method from W1-1 (within each (p,q) rep: lowest 2*dim → B1, next 8*dim → B2, top 6*dim → B3). Color: B1=blue, B2=red, B3=green (or appropriate scheme).

3. **Create the main figure.** A horizontal strip plot or stem plot:
   - x-axis: |λ| (eigenvalue magnitude)
   - y-position or marker size: PW degeneracy (dim²)
   - Color: sector (B1/B2/B3)
   - Annotate the 13 pi-phase states with star markers or arrows
   - Mark the BCS gaps (Δ_B1, Δ_B2, Δ_B3) on the eigenvalue axis
   - Mark the van Hove singularities from s44_dos_tau (`tau0.19_vh_omega`)

4. **Add a density panel.** Below or above the strip plot, show the PW-weighted density of states ρ(ω) = Σ dim² × δ(ω - ω_k) smoothed with a kernel. Color-shade by sector contribution.

5. **Add an inset or second panel**: pie chart or stacked bar showing the sector decomposition: B1/B2/B3 fractions of (a) total modes, (b) pi-phase states, (c) BCS pairing weight.

6. **Figure quality.** Use matplotlib with:
   - Clear axis labels with units
   - Legend identifying sectors and annotations
   - Appropriate font sizes for publication
   - Save as both PNG (300 dpi) and PDF

**Pre-registered gate SPECTRAL-LANDSCAPE-47**:
- INFO: Visualization task. No pass/fail.
- Verify: 992 total eigenvalues, 13 pi-phase annotations, 3 sector colors.

**Output files**:
- Script: `tier0-computation/s47_spectral_landscape.py`
- Data: `tier0-computation/s47_spectral_landscape.npz` (processed visualization data)
- Plot: `tier0-computation/s47_spectral_landscape.png`
- Plot: `tier0-computation/s47_spectral_landscape.pdf`

**Working paper section**: W2-3

**Critical notes**:
- The (p,q) rep labels for each of the 992 eigenvalues are NOT directly stored in s44_dos_tau. You need to reconstruct them: the 992 modes come from max_pq_sum=3, covering 9 reps: (0,0)16, (0,1)48, (0,2)96, (0,3)160, (1,0)48, (1,1)128, (2,0)96, (2,1)240, (3,0)160. Total = 992. Each rep contributes 16×dim(p,q) eigenvalues. The ordering within tau0.19_all_omega may be by (p,q) rep or by eigenvalue magnitude — check which.
- The tau0.19_all_dim2 array gives the PW degeneracy dim(p,q)² for each eigenvalue. Use this to identify which rep each eigenvalue belongs to: dim²=1→(0,0), dim²=9→(0,1)or(1,0), dim²=36→(0,2)or(2,0), dim²=64→(1,1), dim²=100→(0,3)or(3,0), dim²=225→(2,1).
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.
