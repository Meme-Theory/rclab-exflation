# Session 16, Round 2b: D_K and Generations
## Baptista-Analyst + KK-Theorist Joint Assessment
## Date: 2026-02-13
## Status: CONVERGED (both agents agree on all substantive points)

---

## EXECUTIVE SUMMARY

Three questions were addressed: (1) the exact specification of D_K from Baptista Paper 17, (2) the relationship between D_K on SU(3) and the CP^2 coset spectrum, and (3) the Z_3 generation mechanism from Paper 18. The main findings:

1. **D_K on SU(3) IS the correct mass operator** (Corollary 3.4). The Tier 1 eigenvalues are physical. No operator change needed.
2. **CP^2 modes are a SUBSET** of the SU(3) spectrum, selected by U(2) quantum numbers. The modification is labeling, not recomputation.
3. **Z_3 generation assignment is (p-q) mod 3** -- trivial to implement. The 2-week estimate was for the full spinor transport map; the representation-level test is nearly free.
4. **Feasibility: GREEN.** Total new code: ~315 lines. Timeline: ~2 days for U(2) labeling + Z_3 test combined.

---

## I. D_K MATHEMATICAL SPECIFICATION

### Paper 17, Corollary 3.4 (eq 3.8)

The 12-dimensional Dirac operator D_P on P = M^4 x K decomposes as:

```
D_P(psi^H tensor phi) = (D_M psi) tensor phi
    + sum_a A^a_mu gamma^mu psi tensor L_{e_a} phi
    + gamma_5 psi tensor D_K phi
    + (Pauli term)
```

where:
- D_M = 4D Dirac operator (kinetic term)
- L_{e_a} = Kosmann-Lichnerowicz derivative along gauge field (gauge coupling)
- **D_K = Dirac operator on (K, g_K)** -- this is the MASS TERM
- Pauli term = spin-orbit coupling (subdominant)

### The mass matrix

The 4D fermion mass matrix is (Paper 18, eq 7.5):

```
M_{alpha beta} = <phi_beta, D_K phi_alpha>_{L^2(K, S_K)}
```

where {phi_alpha} is an orthonormal basis of L^2 sections of the spinor bundle on K = SU(3).

### D_K in Peter-Weyl decomposition

On (SU(3), g_s) with left-invariant metric, D_K decomposes via Peter-Weyl as:

```
D_K = bigoplus_{(p,q)} D_{(p,q)} tensor I_{dim(p,q)}
```

where D_{(p,q)} acts on V_{(p,q)} tensor C^16 (spinor). Explicitly:

```
D_{(p,q)} = sum_{a,b} E_{ab}(s) [rho_{(p,q)}(X_b) tensor gamma_a] + I_{dim(p,q)} tensor Omega(s)
```

with:
- E_{ab}(s) = orthonormal frame for g_s (from Cholesky of g_s^{-1})
- rho_{(p,q)}(X_b) = representation of the LEFT-REGULAR action of X_b on V_{(p,q)}
- gamma_a = Cliff(R^8) generators (16x16 Hermitian, {gamma_a, gamma_b} = 2 delta_{ab})
- Omega(s) = spinor curvature offset = (1/4) sum_{a<b} Gamma_{ab}^c gamma_a gamma_b (16x16, anti-Hermitian)

**This is EXACTLY what `tier1_dirac_spectrum.py` computes.** The Tier 1 eigenvalues ARE D_K eigenvalues on SU(3). Confirmed by Paper 17 Corollary 3.4 and validated in Sessions 11-12.

### Key properties of D_K

| Property | Source | Status |
|----------|--------|--------|
| D_K is anti-Hermitian (math convention) | Standard Dirac theory | Verified numerically |
| {D_K, Gamma_K} = 0 (anticommutes with chirality) | Lichnerowicz theorem (Paper 17 line 1212) | Theorem-level |
| [D_K, R_{su(3)}] = 0 (commutes with right-regular) | g_s left-invariant => right translations are isometries | Geometric fact |
| [D_K, L_X] != 0 for non-Killing X | Paper 17 Proposition 1.2, eq 1.4 | Proven (S^2, T^2, general K) |
| [D_K, L_X] = 0 for Killing X (u(2) at s > 0) | Standard: Killing isometries commute with D | Geometric fact |

### Corollary 3.4 scope and limitations

Corollary 3.4 applies "in regions where g_K is constant along M^4." This means:
- **Vacuum spectrum** (fixed s_0, sigma_0): Corollary 3.4 APPLIES. D_K eigenvalues = 4D fermion masses.
- **Spacetime-varying moduli** sigma(x), s(x): Need full Proposition 3.3 (eq 3.7), which adds scalar kinetic terms and [X, v_i] commutators. These affect scattering amplitudes, not the mass spectrum.
- **Current computation**: Vacuum spectrum only. Corollary 3.4 is sufficient.

### Theta redefinition (eq 3.11): eigenvalues INVARIANT

Paper 17 eq 3.11 defines a 4D spinor redefinition:

```
theta = (1/sqrt(2))(I + i*gamma_5) * psi = exp(i*gamma_5*pi/4) * psi
```

This transforms the non-standard Dirac equation (3.9) with `m * gamma_5 * psi` into the standard form (3.12) with `m * theta`. Crucially:

1. **The mass m IS the D_K eigenvalue** -- Paper 17, line 833: "writing m for the respective eigenvalue"
2. **Theta acts on psi (4D part), NOT on phi (internal part)**
3. **The eigenvalue m is UNCHANGED** -- it's a 4D convention, not a spectral transformation
4. **Gauge coupling matrix elements** <phi_alpha, L_{e_a} phi_beta> are also unchanged

**Conclusion**: The D_K eigenvalues from our Tier 1 computation are the physical 4D fermion masses DIRECTLY, with no normalization correction from the theta redefinition. Confirmed independently by both agents and consistent with Round 1a finding: "Spinor redefinition theta (eq 3.11): convention change, eigenvalues invariant."

---

## II. CP^2 vs SU(3) SPECTRAL COMPARISON

### The claim: "wrong operator" (Handout Part C.III)

The handout asserts we used "D on SU(3) instead of D_K on CP^2." Round 1a partially corrected this. Here is the precise analysis.

### Why K = SU(3), not CP^2

Baptista's framework has the total space P = M^4 x K where **K = SU(3)** (the full group manifold, 8-dimensional). The coset space CP^2 = SU(3)/U(2) (4-dimensional) is NOT the internal space. It appears as:

- The **base** of the principal U(2)-bundle SU(3) -> CP^2
- The **moduli space** of gauge-equivalent internal configurations
- The space on which CP^2 "harmonics" live (Kaluza-Klein scalar functions)

The internal Dirac operator D_K acts on spinors of the 8-dimensional manifold K = SU(3), NOT on the 4-dimensional coset CP^2. This is explicit in Corollary 3.4: D_K is the Dirac operator on (K, g_K) where K is the full internal space.

### What changes vs what's preserved

| Aspect | SU(3) spectrum (current) | CP^2 spectrum (subset) |
|--------|------------------------|----------------------|
| Operator | D_K on (SU(3), g_s) | D_{spin^c} on (CP^2, induced metric) |
| Dimension | 8D spin manifold | 4D spin^c manifold |
| Peter-Weyl | L^2(SU(3), S) = bigoplus V_{(p,q)} tensor V^*_{(p,q)} tensor C^16 | L^2(CP^2, S tensor L^k) = bigoplus V_{(p,q)}^{U(2)-equivariant} tensor C^4 |
| Eigenvalues | ALL (p,q) sectors, all U(2) reps within each | ONLY U(2)-equivariant modes |
| Physical content | Full KK tower | Specific particle types |

**KEY POINT**: The spectrum of D_K on SU(3) CONTAINS the CP^2 spectrum as a subset. No eigenvalues need to be recomputed. The modification is to LABEL existing eigenvalues by U(2) quantum numbers and identify which ones correspond to which 4D particles.

### CP^2 spin structure subtlety

CP^2 does NOT admit a spin structure (w_2 != 0). It admits a spin^c structure. The Dirac-type operator on CP^2 is the spin^c Dirac operator, acting on spinors twisted by a line bundle L^k.

However, this subtlety is RESOLVED by working on SU(3) (which IS spin, being simply connected and parallelizable). The spinor bundle on SU(3) is globally trivial. The U(2)-equivariant modes of D_K on SU(3) correspond to sections of specific spin^c bundles on CP^2, with the "charge" k determined by the U(2) representation.

The code needs to identify which U(2) representation each eigenvector belongs to. This determines:
1. Which 4D particle type the eigenvalue corresponds to (gauge quantum numbers)
2. Which spin^c bundle on CP^2 the mode belongs to
3. Which Z_3 generation (see Section III)

### U(2) quantum number extraction

For each eigenvector psi of D_{(p,q)} in sector (p,q), the U(2) quantum numbers are:

**Hypercharge Y**: Eigenvalue of rho_{(p,q)}(e_8) tensor I_16 + I_{dim} tensor (spinor Y component)

**Isospin j**: Determined by C_2(SU(2)) = sum_{a=1}^{3} [rho_{(p,q)}(e_a)]^2

Since the U(2) generators are a subset of the su(3) generators (indices 0,1,2 for SU(2) and index 7 for U(1)), the representation matrices are already available: they are rho[0], rho[1], rho[2], rho[7] from `get_irrep()`.

The Dirac block D_{(p,q)} has size dim(p,q) * 16. The U(2) generators act on the V_{(p,q)} factor (dim(p,q) x dim(p,q)) tensored with identity on the C^16 spinor factor. The SPINOR factor also carries U(2) quantum numbers (from the embedding of U(2) in Spin(8)), which must be added.

The total U(2) charge of an eigenvector is the sum of the representation charge and the spinor charge.

### Which (p,q) sectors have U(2)-singlets in V_{(p,q)}?

**IMPORTANT SUBTLETY (converged between both agents)**: The notion of "U(2)-singlet" needs careful definition.

For the standard embedding phi(a) = diag(det(a)^{-1}, a), the U(2) action on V_{(p,q)} can have:
- **Full U(2)-singlets** (Y=0, j=0): These are sections of the trivial bundle on CP^2
- **SU(2)-singlets with nonzero U(1) charge** (Y != 0, j=0): These are sections of line bundles L^k on CP^2

For CP^2 SPINORS, the relevant modes are **U(2)-equivariant**, not U(2)-invariant. This is because CP^2 does not admit a spin structure (w_2 != 0) and only admits spin^c structures. The spin^c Dirac operator acts on spinors twisted by a line bundle L^k, where k is determined by the U(1) charge.

**U(2) branching for low-lying irreps** (KK-theorist computation):

| (p,q) | dim | Full U(2)-singlet (Y=0, j=0) | SU(2)-singlet (j=0, any Y) | Y value of SU(2)-singlet |
|-------|-----|------------------------------|---------------------------|-------------------------|
| (0,0) | 1 | 1 | 1 | Y=0 |
| (1,0) | 3 | 0 | 1 | Y=-1 |
| (0,1) | 3 | 0 | 1 | Y=+1 |
| (1,1) | 8 | 1 | 2 | Y=0, Y=0 |
| (2,0) | 6 | 0 | 1 | Y=-2 |
| (0,2) | 6 | 0 | 1 | Y=+2 |
| (3,0) | 10 | 0 | 1 | Y=-3 |
| (0,3) | 10 | 0 | 1 | Y=+3 |
| (2,1) | 15 | 0 | 1 | Y=-1 |
| (1,2) | 15 | 0 | 1 | Y=+1 |

**Physical interpretation**: Each SU(2)-singlet in V_{(p,q)} corresponds to a spin^c mode on CP^2 with U(1) charge Y. The D_K eigenvalue for this mode is the mass of a 4D particle with hypercharge Y in the (p,q) KK level. The (3,0) SU(2)-singlet with Y=-3 was identified in Session 12 as the Parthasarathy-saturating mode.

**For the code**: The U(2) Casimir null-space method (KK-theorist proposal) finds the SU(2)-singlets. The U(1) charge is then read off from rho_{(p,q)}(e_8) on the singlet subspace. This correctly captures the spin^c structure without needing to explicitly construct the CP^2 Dirac operator.

---

## III. Z_3 GENERATION MECHANISM

### Paper 18, Appendix E: Z_3 x Z_3 center

The gauge group G = (SU(3)_L x SU(3)_R)/Z_3 has universal cover G~ = SU(3) x SU(3) with center Z(G~) = Z_3 x Z_3.

The Z_3 center of SU(3) is generated by:

```
zeta = exp(2*pi*i/3) * I_3
```

Under the irreducible representation V_{(p,q)}, this acts as a SCALAR:

```
rho_{(p,q)}(zeta) = omega^{(p-q) mod 3} * I_{dim(p,q)}
```

where omega = exp(2*pi*i/3). This follows from the fact that the highest weight (p,q) has z-center charge = (p-q) mod 3.

### Generation assignment: (p-q) mod 3

The full Dirac spectrum on SU(3) decomposes into THREE sectors by Z_3 character:

**Generation 0** [(p-q) = 0 mod 3]:
  (0,0), (1,1), (3,0), (0,3), (2,2), (4,1), (1,4), (3,3), (6,0), (0,6)

**Generation 1** [(p-q) = 1 mod 3]:
  (1,0), (0,2), (2,1), (4,0), (0,5), (3,2), (1,3)

**Generation 2** [(p-q) = 2 mod 3]:
  (0,1), (2,0), (1,2), (0,4), (5,0), (2,3), (3,1)

### Properties of the Z_3 decomposition

1. **Automatic**: The decomposition follows from representation theory. It requires NO computation beyond labeling.

2. **Preserved by D_K**: The Z_3 center commutes with D_K (center elements are isometries for any left-invariant metric). Therefore Z_3 charge is a conserved quantum number, and D_K does not mix generations.

3. **Same gauge content per generation**: Each Z_3 sector contains representations with the SAME set of U(2) quantum numbers (by the periodicity of branching rules under p -> p+3 or q -> q+3). This means each generation has the same particle types.

4. **Different masses per generation**: Different (p,q) sectors in the same Z_3 class have different Casimir values C_2(p,q), hence different D_K eigenvalues. The inter-generation mass hierarchy is:
   - Lightest generation: smallest C_2 within each Z_3 sector
   - Heaviest generation: largest C_2 within each Z_3 sector

5. **Generation splitting is automatic at s=0**: Even for the bi-invariant metric, different generations have different masses because C_2(p,q) depends on both p and q (not just (p-q) mod 3). The Jensen deformation MODIFIES the inter-generation ratios but does not CREATE them.

### Left vs right Z_3

Paper 18 discusses Z_3 x Z_3, with factors from left and right SU(3):

**Left Z_3** (center of SU(3)_L): Acts on the LEFT-regular representation, i.e., the V_{(p,q)} factor in Peter-Weyl. Selects (p-q) mod 3. This is the generation selector described above.

**Right Z_3** (center of SU(3)_R): Acts on the RIGHT factor V_{(p,q)}^* in Peter-Weyl. Since D_K commutes with R_{su(3)}, the right Z_3 preserves D_K eigenspaces. It acts WITHIN each eigenspace, selecting sub-components. This is relevant for the finer structure (mass integrals, CKM mixing).

For the generation-level test (which (p,q) sectors belong to which generation), only the LEFT Z_3 matters.

### The spinor transport subtlety (Paper 18 eq 5.10)

Paper 18 introduces the spinor transport map Phi: S_g -> S_{g-hat}, which is a canonical isomorphism between spinor bundles for two different metrics (g = g_s Jensen, g-hat = g_0 bi-invariant). This map satisfies the Clifford equivariance (B.4):

```
Phi(V . psi) = Phi(V) . Phi(psi)
```

where the two dots denote Clifford multiplication for g and g-hat respectively. For the Jensen metric, Phi is block-diagonal:

```
Phi|_{u(1)} = e^s * id,   Phi|_{su(2)} = e^{-s} * id,   Phi|_{C^2} = e^{s/2} * id
```

**IMPORTANT**: Phi is NOT trivial, despite being diagonal. It maps between DIFFERENT spinor bundles, not within one. The transported Lie derivative (eq 5.11) has a correction term:

```
L_V psi = L_V psi + (1/4) sum_{j != k} g(Phi^{-1}(L_V Phi)(v_j), v_k) v_j . v_k . psi
```

This correction vanishes iff V is conformal Killing for BOTH g and g-hat (Proposition B.1). The right Z_3 vector field IS Killing for g-hat (bi-invariant) but NOT for g_s (s != 0). So the correction is non-zero.

**Physical consequence** (Paper 18, Section 6, after eq 6.6): The representation rho_V (eq 6.1) does NOT preserve D_K-eigenspaces for non-Killing V. The right Z_3 maps a D_K-eigenspinor to a SUPERPOSITION of eigenspinors with different eigenvalues. This is the generation mechanism: the Z_3 relates fermions with the same gauge quantum numbers but different masses.

**Why Lambda is NOT needed for the generation test**: The generation ASSIGNMENT is determined by the Peter-Weyl decomposition -- the Z_3 center acts on V_{(p,q)} by the scalar omega^{(p-q) mod 3}. This is a purely algebraic statement about the Z_3 character of the representation and does not require computing Phi. The generation MASSES are the D_K eigenvalues per (p,q) sector, already computed in Tier 1.

The spinor transport becomes essential ONLY for:
1. The mass integral <phi_beta, D_K phi_alpha> (Paper 18 eq 7.5) -- which needs eigenvectors in the REPRESENTATION basis, not the mass basis
2. CKM mixing angles -- which depend on the misalignment between mass eigenstates (D_K-eigenspaces E_m) and gauge eigenstates (representation spaces W_{m,rho})
3. CP violation (Paper 18 Section 7) -- which depends on phases arising from this misalignment
4. Non-minimal coupling ea-prime (eq 7.2) -- which involves Phi^{-1}(L_{e_a} Phi) directly

These are Tier 2 computations, not needed for the generation-level test.

### Inter-generation mass scale (Paper 18, Appendix E, lines 2560-2567)

Paper 18 provides the physical expectation for the inter-generation mass splitting:

- Before the second symmetry breaking (isometry G_SM = SU(3) x U(2)/Z_3): the right Z_3 lies INSIDE the isometric subgroup G~ = SU(3) x U(2). It relates DEGENERATE fermions (same mass).
- After the second symmetry breaking (isometry SU(3) x U(1)): the right Z_3 lies OUTSIDE G~. Mass splitting appears at the PERTURBATION SCALE (electroweak, not Planck).

This means the inter-generation mass hierarchy is of order m_EW/m_Pl ~ 10^{-17}, far too small. The observed hierarchy (m_tau/m_e ~ 3500) requires either:
1. Large corrections from the non-minimal coupling ea-prime, or
2. A non-perturbative mechanism, or
3. The hierarchy coming from the sector-specific D_K eigenvalues at the UNBROKEN level

Option 3 is what our Z_3 test probes: the mass ratios between different (p,q) sectors with the same U(2) quantum numbers but different Z_3 character. If these ratios are O(1) at the Jensen level and become hierarchical at the stabilized s_0, the generation mechanism works without relying on the perturbation.

---

## IV. Z_3 TEST PROCEDURE (Step-by-Step)

### Step 1: Generation labeling (TRIVIAL)

For each (p,q) sector in the eigenvalue catalog, assign:
```python
generation = (p - q) % 3
```

### Step 2: Group eigenvalues by generation (TRIVIAL)

Partition the eigenvalue catalog into three groups:
```python
gen0_evals = {(p,q,lam) : (p-q) % 3 == 0}
gen1_evals = {(p,q,lam) : (p-q) % 3 == 1}
gen2_evals = {(p,q,lam) : (p-q) % 3 == 2}
```

### Step 3: U(2) quantum number assignment (MEDIUM)

For each eigenvector in each (p,q) block, compute (Y, j) from the representation matrices:
```python
# U(1) charge
Y_op = np.kron(rho_pq[7], np.eye(16)) + np.kron(np.eye(dim_pq), Y_spinor)
y_val = psi.conj() @ Y_op @ psi

# SU(2) Casimir
C2_SU2 = sum(np.kron(rho_pq[a], np.eye(16)) + np.kron(np.eye(dim_pq), T_spinor[a]))**2 for a=0,1,2)
j_val = psi.conj() @ C2_SU2 @ psi
```

where Y_spinor and T_spinor[a] are the U(2) generators in the 16-dim spinor representation (already computed in `branching_computation.py`).

### Step 4: Particle type assignment

Map each (Y, j) pair to a SM particle type using Baptista eq 2.66:

| (Y, j) | Particle type |
|---------|--------------|
| (0, 0) | nu_R (right-handed neutrino) |
| (-1, 0) | e_R (right-handed electron) |
| (1/6, 1/2) | (u_L, d_L) quark doublet |
| (2/3, 0) | u_R (right-handed up quark) |
| (-1/3, 0) | d_R (right-handed down quark) |
| (-1/2, 1/2) | (nu_L, e_L) lepton doublet |

Note: actual Y values depend on normalization convention. The RELATIVE structure is what matters.

### Step 5: Inter-generation mass ratios

For each particle type (Y, j), extract the lowest D_K eigenvalue from each generation:

```python
m_gen0 = min(|lam| for lam in gen0_evals if (Y,j) matches)
m_gen1 = min(|lam| for lam in gen1_evals if (Y,j) matches)
m_gen2 = min(|lam| for lam in gen2_evals if (Y,j) matches)
```

Compute ratios: m_gen1/m_gen0, m_gen2/m_gen0, m_gen2/m_gen1.

### Step 6: Compare to physical mass ratios

| Ratio | Predicted (D_K at s_0) | Observed (SM) |
|-------|----------------------|--------------|
| m_mu/m_e | ? | 206.768 |
| m_tau/m_e | ? | 3477.15 |
| m_tau/m_mu | ? | 16.817 |
| m_c/m_u | ? | ~515 |
| m_t/m_u | ? | ~86,000 |
| m_s/m_d | ? | ~20 |
| m_b/m_d | ? | ~900 |

### Step 7: Pass/fail criteria

| Criterion | Condition | Verdict |
|-----------|-----------|---------|
| THREE generations | Each Z_3 sector has same (Y,j) content | Structural (should PASS by construction) |
| Mass hierarchy exists | m_gen0 < m_gen1 < m_gen2 (or some ordering) for each (Y,j) | Z_3 mass splitting works |
| Hierarchy ratio > 10 | At least one inter-generation ratio > 10 | Nontrivial hierarchy (not near-degenerate) |
| Charged lepton ratio order-of-magnitude | m_mu/m_e within factor 10 of 207 | Quantitative match |
| phi_paasch in inter-generation ratio | Any inter-generation ratio within 1% of phi_paasch | Paasch connection |

---

## V. CODE MODIFICATION PLAN

### File: `tier0-computation/tier1_dirac_spectrum.py`

#### Modification 1: Store eigenvectors in `collect_spectrum()`

Currently, `collect_spectrum()` calls `np.linalg.eigvals()` and discards eigenvectors. Change to `np.linalg.eigh()` on the Hermitianized operator i*D (converged recommendation from both agents).

```python
# OLD (line 1328):
evals_pi = np.linalg.eigvals(D_pi)

# NEW (preferred -- Hermitian eigensolver, faster + real eigenvalues):
evals_h, evecs_h = np.linalg.eigh(1j * D_pi)
# D eigenvalues are -1j * evals_h (purely imaginary)
# Physical masses are |evals_h| (real, positive)
evals_pi = -1j * evals_h
evecs_pi = evecs_h
```

**Performance note** (KK-theorist): eigh is ~3x faster than eig for dense Hermitian matrices. Using eigh(1j*D) instead of eigvals(D) may produce a NET SPEEDUP despite computing eigenvectors. Estimated total per s-value at p+q<=6: ~10-15s with eigh vs ~30s with eigvals currently.

Return `evecs_pi` as part of `eval_data`. Estimated: ~20 lines modified.

#### Modification 2: U(2) generator construction

New function `u2_generators_in_irrep(rho_pq, gammas)`:

```python
def u2_generators_in_irrep(rho_pq, gammas):
    """
    Construct U(2) generators on V_{(p,q)} tensor C^16.

    U(2) generators in su(3): indices [0,1,2] (SU(2)) and [7] (U(1)).
    These act on the V_{(p,q)} factor via rho_pq.
    The spinor factor C^16 also carries U(2) charges.

    Returns:
        Y_total: (dim_total, dim_total) hypercharge operator
        T_total: list of 3 isospin operators
        C2_SU2: SU(2) Casimir on total space
    """
    dim_rho = rho_pq[0].shape[0]
    dim_spin = 16

    # Representation part
    Y_rep = np.kron(rho_pq[7], np.eye(dim_spin))
    T_rep = [np.kron(rho_pq[a], np.eye(dim_spin)) for a in range(3)]

    # Spinor part (from branching_computation.py U(2) embedding)
    # Y_spinor, T_spinor to be computed from Cliff(8) embedding

    Y_total = Y_rep + np.kron(np.eye(dim_rho), Y_spinor)
    T_total = [T_rep[a] + np.kron(np.eye(dim_rho), T_spinor[a]) for a in range(3)]

    C2_SU2 = sum(T @ T for T in T_total)

    return Y_total, T_total, C2_SU2
```

Estimated: ~50 lines new.

#### Modification 3: Quantum number assignment

New function `assign_quantum_numbers(evecs, Y_op, C2_op)`:

```python
def assign_quantum_numbers(evecs, Y_op, C2_op):
    """
    For each eigenvector, compute (Y, j) quantum numbers.

    Args:
        evecs: (dim, dim) matrix of column eigenvectors
        Y_op: hypercharge operator
        C2_op: SU(2) Casimir

    Returns:
        quantum_numbers: list of (Y_val, j_val) per eigenvector
    """
    n = evecs.shape[1]
    qnums = []
    for i in range(n):
        psi = evecs[:, i]
        psi = psi / np.linalg.norm(psi)

        Y_val = np.real(psi.conj() @ Y_op @ psi)
        C2_val = np.real(psi.conj() @ C2_op @ psi)
        # j(j+1) = -C2_val (anti-Hermitian convention) or +C2_val (Hermitian)
        j_val = (-1 + np.sqrt(1 + 4*abs(C2_val))) / 2  # solve j(j+1) = |C2|

        qnums.append((round(Y_val, 4), round(j_val * 2) / 2))  # round j to half-integer

    return qnums
```

Estimated: ~40 lines new.

#### Modification 4: Z_3 labeling

Trivial addition to the eigenvalue catalog:

```python
generation = (p - q) % 3  # Z_3 character
```

Estimated: ~5 lines.

#### Modification 5: Generation-grouped analysis

New function `analyze_generations(eval_data_labeled, s)`:

```python
def analyze_generations(eval_data_labeled, s):
    """
    Group eigenvalues by Z_3 generation and (Y,j) particle type.
    Compute inter-generation mass ratios.
    """
    # Group by (generation, Y, j)
    gen_particle_map = defaultdict(list)
    for (p, q, lam, Y, j, gen) in eval_data_labeled:
        gen_particle_map[(gen, round(Y,2), round(j,1))].append(abs(lam))

    # For each particle type, find lightest mass per generation
    particle_types = set((Y, j) for (gen, Y, j) in gen_particle_map.keys())

    results = {}
    for (Y, j) in sorted(particle_types):
        masses = {}
        for gen in [0, 1, 2]:
            key = (gen, round(Y,2), round(j,1))
            if key in gen_particle_map and gen_particle_map[key]:
                masses[gen] = min(gen_particle_map[key])

        if len(masses) >= 2:
            results[(Y, j)] = masses

    return results
```

Estimated: ~60 lines new.

#### Modification 6: phi_paasch test in inter-generation ratios

```python
def test_phi_in_generations(gen_results, phi=1.53158):
    """
    Check if phi_paasch (1.53158) appears in inter-generation mass ratios.
    """
    phi_hits = []
    for (Y, j), masses in gen_results.items():
        sorted_masses = sorted(masses.values())
        for i, m1 in enumerate(sorted_masses):
            for m2 in sorted_masses[i+1:]:
                ratio = m2 / m1 if m1 > 0 else float('inf')
                if abs(ratio - phi) / phi < 0.01:
                    phi_hits.append((Y, j, m1, m2, ratio))
    return phi_hits
```

Estimated: ~30 lines new.

### New file: `tier0-computation/tier1_u2_projection.py`

Contains all U(2) labeling and Z_3 analysis functions. Imports from `tier1_dirac_spectrum.py`.

### Summary of modifications

| Component | File | New/Modified | Lines | Difficulty |
|-----------|------|-------------|-------|------------|
| Store eigenvectors | tier1_dirac_spectrum.py | Modified | ~20 | EASY |
| U(2) generators in irrep | tier1_u2_projection.py | New | ~50 | MEDIUM |
| Quantum number assignment | tier1_u2_projection.py | New | ~40 | MEDIUM |
| Z_3 labeling | tier1_u2_projection.py | New | ~5 | TRIVIAL |
| Generation analysis | tier1_u2_projection.py | New | ~60 | MEDIUM |
| phi_paasch test in generations | tier1_u2_projection.py | New | ~30 | EASY |
| U(2) spinor embedding | tier1_u2_projection.py | New | ~40 | MEDIUM |
| Particle type mapping | tier1_u2_projection.py | New | ~20 | EASY |
| Driver / main | tier1_u2_projection.py | New | ~50 | EASY |
| **TOTAL** | | | **~315** | |

---

## VI. FEASIBILITY ASSESSMENT: GREEN

### Timeline

| Phase | Content | Estimate |
|-------|---------|----------|
| Phase 1 | Store eigenvectors + U(2) generator construction | 4 hours |
| Phase 2 | Quantum number assignment + validation vs Tier 0 branching | 4 hours |
| Phase 3 | Z_3 labeling + generation analysis | 2 hours |
| Phase 4 | Run at s_0 candidates (0.15, 0.3, 0.6, 1.14) | 2 hours |
| Phase 5 | phi_paasch test + inter-generation ratio analysis | 2 hours |
| **Total** | | **~2 days** |

### Dependencies

```
[EXISTING] tier1_dirac_spectrum.py (eigenvalues + metric infrastructure)
    |
    v
[Phase 1] Modify collect_spectrum() to store eigenvectors
    |
    v
[Phase 2] U(2) quantum number assignment
    |                |
    v                v
[Phase 3a] Z_3 labeling    [Phase 3b] Particle type mapping
    |                |
    v                v
[Phase 4] Generation-grouped eigenvalue catalog at s_0
    |
    v
[Phase 5] Inter-generation mass ratios + phi_paasch test
```

### Blocking issues: NONE

1. **All infrastructure exists**: `get_irrep()`, `collect_spectrum()`, `orthonormal_frame()`, Clifford algebra -- all implemented and validated.
2. **U(2) generators are linear combinations of su(3) generators**: No new representation theory needed. Use rho_pq[0], rho_pq[1], rho_pq[2], rho_pq[7].
3. **Spinor U(2) embedding**: Already computed in `branching_computation.py` (Session 7). Need to extract and reuse.
4. **Z_3 labeling**: Pure integer arithmetic on (p,q) indices.

### Risk factors

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Eigenvector storage memory | LOW | At (3,3), 1024x1024 complex = 16 MB per sector | Store only at target s values |
| U(2) quantum numbers not cleanly quantized | MEDIUM | Numerical noise in (Y,j) | Round to nearest physical value; verify via trace of Casimir |
| Spinor U(2) embedding wrong normalization | MEDIUM | Systematic shift in Y values | Cross-validate against Tier 0 branching results |
| Not enough (p,q) sectors per Z_3 class at p+q<=6 | LOW | Poor statistics for generation ratios | p+q<=6 gives 9-10 sectors per Z_3 class (sufficient) |

---

## VII. RELATIONSHIP TO V_eff (ROUND 2a)

The U(2) labeling and Z_3 generation analysis connect directly to the V_eff computation from Round 2a:

1. **V_eff determines s_0**: The CW computation finds the physical value of the Jensen parameter. At s_0, the D_K eigenvalues give the physical mass spectrum.

2. **U(2) labeling at s_0 gives particle masses**: Each D_K eigenvalue at s_0 corresponds to a specific 4D particle (labeled by (Y, j, generation)).

3. **Z_3 generation ratios at s_0 give mass hierarchies**: The inter-generation ratios at s_0 are the physical mass ratios (up to overall scale).

4. **Gauge couplings at s_0**: The Jensen metric at s_0 determines the internal geometry, hence the gauge coupling constants g_1, g_2, g_3 via the Killing metric on u(1), su(2), and su(3) respectively.

The combined V_eff + U(2) labeling + Z_3 analysis would give, for the first time:
- Mass spectrum (zero free parameters after s_0 is fixed)
- Mass ratios (parameter-free predictions)
- Generation hierarchy (parameter-free prediction)
- Gauge couplings (parameter-free predictions)

This is the FULL prediction pipeline from geometry to SM parameters.

---

## VIII. OPEN QUESTIONS

### Q1: Right-regular vs left-regular U(2) action

The Tier 1 code uses the LEFT-regular representation rho_L for the Peter-Weyl decomposition. The U(2) quantum numbers that label 4D particles correspond to the gauge symmetry, which acts via the LEFT action (L_{e_a}).

However, the Handout (Part C.III) and Round 1a discussed U(2)-singlets in V^*_{(p,q)} (the RIGHT factor). This distinction matters:

- **Left U(2) on V_{(p,q)}**: Determines gauge quantum numbers of 4D particles
- **Right U(2) on V^*_{(p,q)}**: Determines which modes live on CP^2 (= U(2)-right-invariant)

For the MASS SPECTRUM, both labelings are relevant:
- Particle identity (which fermion): LEFT U(2) quantum numbers
- KK tower truncation (which CP^2 mode): RIGHT U(2) quantum numbers

The eigenvectors of D_{(p,q)} live in V_{(p,q)} tensor C^16. The LEFT U(2) acts on V_{(p,q)}; the RIGHT U(2) acts on V^*_{(p,q)} (not directly on the eigenvectors). To extract RIGHT U(2) quantum numbers, we need the FULL Peter-Weyl two-sided structure, which requires storing the map between the D_{(p,q)} eigenspace and the L^2 space on SU(3).

**Resolution**: For the FIRST computation, use LEFT U(2) quantum numbers only (sufficient for particle identification). RIGHT U(2) projection is a Tier 2 refinement.

### Q2: Spinor U(2) charges

The spinor bundle on SU(3) has its own U(2) charges (from the embedding U(2) -> SO(8) -> Spin(8)). These were computed in `branching_computation.py` for the fundamental spinor representation. For the D_{(p,q)} block, the TOTAL U(2) charge is:

```
Y_total = Y_rep tensor I_16 + I_dim tensor Y_spinor
j_total from C2_total = (T_rep + T_spinor)^2
```

The spinor U(2) charges are the ones that give the SM particle identification (nu_R, e_R, quarks, etc.) from Session 7. The representation U(2) charges are the KK mode labels.

### Q3: Does Z_3 give EXACTLY three generations or more?

The Z_3 decomposition gives THREE sectors (by Z_3 character). Within each sector, there is an INFINITE tower of (p,q) representations (one for each p+q value satisfying the Z_3 condition). Each (p,q) contributes eigenvalues with dim(p,q)*16 modes.

So each "generation" actually contains infinitely many mass eigenvalues. The LIGHTEST eigenvalue in each generation + particle type gives the physical mass. The heavier eigenvalues are KK excitations.

The physical number of generations is:
- Z_3 gives 3 sectors: CORRECT
- Each sector has the same particle content: CORRECT (by periodicity of branching rules)
- Each sector gives one "lightest mass" per particle type: the PHYSICAL generation

This matches the SM: three generations with the same gauge quantum numbers but different masses.

---

## IX. SUMMARY AND NEXT STEPS

### What we've established

1. **D_K specification**: Fully explicit from Paper 17 Corollary 3.4. Matches existing code. No changes to the Dirac operator needed.

2. **CP^2 vs SU(3)**: The "wrong operator" claim is overblown. K = SU(3) is correct. CP^2 modes are a subset, selected by U(2) quantum numbers. The modification is labeling, not recomputation.

3. **Z_3 generations**: (p-q) mod 3 gives three sectors with same gauge content but different masses. Trivial to implement.

4. **Code plan**: ~315 new lines in `tier1_u2_projection.py` plus ~20 modified lines in `tier1_dirac_spectrum.py`.

5. **Feasibility**: GREEN. ~2 days. No blocking issues.

### Immediate next steps

1. **Implement Phase 1**: Modify `collect_spectrum()` to store eigenvectors
2. **Implement Phase 2**: U(2) quantum number assignment, cross-validate with Tier 0
3. **Implement Phase 3**: Z_3 labeling + generation analysis
4. **Run at s_0 from V_eff**: Once Round 2a produces s_0, evaluate the generation analysis at that specific s

### Decision matrix

| If... | Then... | Framework impact |
|-------|---------|-----------------|
| Z_3 gives 3 correct particle types per generation | Generation mechanism works | +5-10% |
| Inter-generation ratios order-of-magnitude match | Quantitative success | +10-15% |
| phi_paasch appears in inter-generation ratio | Paasch connection established | +15-20% |
| Z_3 sectors don't have same (Y,j) content | Generation mechanism fails | -5% (need alternative) |
| All inter-generation ratios near 1 | Hierarchy mechanism fails | -10% |

---

*Round 2b complete. D_K is the operator we already have. CP^2 is a labeling problem, not a computation problem. Z_3 is (p-q) mod 3. Everything is GREEN.*
