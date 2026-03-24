# Session 16, Round 2a: V_eff Deep Dive
## KK-Theorist + Gen-Physicist + Sim-Specialist
## Date: 2026-02-13
## Status: DRAFT v2 (Hawking thermodynamic layer incorporated; DOF counting still open)

---

## EXECUTIVE SUMMARY

The 1-loop Coleman-Weinberg effective potential for the Jensen shape modulus s is:

**V_eff(s) = V_tree(s) + V_CW^boson(s) - V_CW^fermion(s)**

- **V_tree**: Baptista eq 3.80 (analytical, coded). Monotonic runaway, no minimum.
- **V_CW^boson**: 4 massive C^2 gauge bosons, eq 3.87 (analytical, coded). Positive sign.
- **V_CW^fermion**: Full Dirac spectrum at p+q <= 6 (~12,000 eigenvalues). **Negative sign. NEW.**

**Key finding**: The fermion CW dominates by ~30,000x at p+q=6 due to UV-dominated |lam|^4 weighting. The minimum of V_eff (if it exists) arises from competition between the tree-level runaway (V_tree -> -infinity at large s) and the fermion CW (which also grows at large s, with negative sign, pulling V_eff DOWN). The bosonic CW is a small perturbation.

**Open issue**: The per-eigenvalue factor (1 vs 4 for 4D Dirac DOF) is under discussion. This changes the fermion-to-boson ratio by 4x.

**Code estimate**: ~300 lines new, ~2 days compute at p+q=6.
**Dependencies**: All existing infrastructure sufficient. No new operators needed.
**Pass/fail**: 5 tests defined (minimum existence, convergence, mu-sensitivity, boson-fermion balance, Baptista consistency).

---

## I. COMPLETE V_eff FORMULA WITH ALL TERMS ENUMERATED

### The Full Coleman-Weinberg Effective Potential

The effective potential for the Jensen shape parameter s (with sigma=0, i.e. fixed total volume) is:

```
V_eff(s) = V_tree(s) + V_CW^boson(s) + V_CW^fermion(s)
```

where each term is defined below.

### Term 1: Classical Tree-Level Potential (Baptista eq 3.80)

```
V_tree(s) = C_tree * { 1 - (1/10) * R_bracket(s) }
```

where:
- `R_bracket(s) = 2*e^{2s} - 1 + 8*e^{-s} - e^{-4s}`
- `C_tree` = overall constant involving Planck mass and internal volume (sets mass scale, not shape)
- At sigma=0, `V_tree(s) = baptista_V_potential(0, s)` in the existing code

**Properties:**
- V_tree(0) = 0 (bi-invariant is the reference)
- V_tree(s) -> -infinity as s -> +infinity (monotonic runaway for s > 0)
- V_tree(s) -> +infinity as s -> -infinity
- NO minimum at s > 0 from tree level alone

### Term 2: Bosonic Coleman-Weinberg (Baptista eq 3.87)

```
V_CW^boson(s) = + (N_b / (64 pi^2)) * sum_i m_i^4(s) * [ln(m_i^2(s)/mu^2) - 3/2]
```

**POSITIVE sign** (bosons raise the vacuum energy).

Bosonic modes enumerated:

| Mode | Count N_b | Mass formula m^2(s) | Source |
|------|-----------|---------------------|--------|
| **C^2 gauge bosons** | **4** | eq 3.84: `(3/2) * alpha * e^sigma * [(e^s - e^{-2s})^2 + (1 - e^{-s})^2]` | Baptista analytical |
| u(2) gauge bosons | 4 | **0** (massless, isometries preserved) | Exact by construction |
| Right-invariant bosons | 8 | **0** (massless, Killing for any left-inv metric) | Exact |
| Scalar modulus (radion) | 1 | `d^2 V_tree / ds^2` (positive near origin) | Derivable |
| KK gauge tower (C^2) | 4 x N_KK | NOT AVAILABLE (need Lichnerowicz on vectors) | **GAP** |
| KK scalar tower | N_KK | NOT AVAILABLE (need Laplacian on scalars) | **GAP** |

**For computation**: Only the 4 C^2 gauge bosons contribute to V_CW^boson in the Baptista EFT. At sigma=0:
```
m_C2^2(s) = c_0 * [(e^s - e^{-2s})^2 + (1 - e^{-s})^2]
```
where c_0 is the overall mass scale (absorbed into mu or set to 1 in natural units).

### Term 3: Fermionic Coleman-Weinberg (FROM DIRAC SPECTRUM -- NEW)

```
V_CW^fermion(s) = - (1 / (64 pi^2)) * sum_n d_n * |lambda_n(s)|^4 * [ln(|lambda_n(s)|^2/mu^2) - 3/2]
```

**NEGATIVE sign** (fermions lower the vacuum energy).

The sum runs over ALL eigenvalues of D_K on (SU(3), g_s):

| Sector (p,q) | dim | Eigenvalues per block | PW weight d_n | Total contribution |
|--------------|-----|----------------------|---------------|-------------------|
| (0,0) | 1 | 16 | 1 | 16 terms |
| (1,0) | 3 | 48 | 3 | 48 terms x weight 3 |
| (0,1) | 3 | 48 | 3 | 48 terms x weight 3 |
| (1,1) | 8 | 128 | 8 | 128 terms x weight 8 |
| (2,0) | 6 | 96 | 6 | 96 terms x weight 6 |
| (0,2) | 6 | 96 | 6 | 96 terms x weight 6 |
| (3,0) | 10 | 160 | 10 | 160 terms x weight 10 |
| (0,3) | 10 | 160 | 10 | 160 terms x weight 10 |
| (2,1) | 15 | 240 | 15 | 240 terms x weight 15 |
| (1,2) | 15 | 240 | 15 | 240 terms x weight 15 |
| ... | ... | ... | ... | ... |
| (3,3) | 64 | 1024 | 64 | 1024 terms x weight 64 |

**Total at p+q <= 6**: 28 irreps, ~10,000 eigenvalues, each weighted by PW degeneracy.

### CRITICAL PHYSICS POINT: Why the Dirac Spectrum Is All Fermionic

In KK theory on M^4 x K, the spectrum of the internal Dirac operator D_K gives the mass tower for 4D FERMIONS (Baptista Paper 17, Corollary 3.4, eq 3.8). The 4D effective Lagrangian is:

```
L_4D = sum_n psi_bar_n (i gamma^mu D_mu - m_n) psi_n
```

where m_n = eigenvalue of D_K. Each eigenvalue corresponds to a 4D Dirac fermion (4 real DOF per mass eigenvalue). The sign flip in the CW formula relative to bosons is the standard textbook result: fermionic functional determinants enter with -1/2 instead of +1/2.

Bosonic masses (gauge bosons, scalars) come from DIFFERENT operators:
- Gauge bosons: Hodge Laplacian on 1-forms restricted to Killing directions
- Scalars: scalar Laplacian on K
- Graviton KK modes: Lichnerowicz Laplacian on symmetric 2-tensors

Only the lightest gauge boson masses are available analytically (Baptista eq 3.84). This is the EFT motivation: include only the light modes in the loop.

### DOF COUNTING SUBTLETY (CRITICAL -- NEEDS TEAM CONVERGENCE)

The CW formula for a field of spin j with n_j real DOF per mass eigenvalue:

```
V_CW = (-1)^{2j} * n_j / (64 pi^2) * m^4 * [ln(m^2/mu^2) - c_j]
```

where c_j = 3/2 (scalars, fermions in MS-bar) or 5/6 (vectors in MS-bar).

Standard DOF counting:
- Real scalar: n_0 = 1
- Complex scalar: n_0 = 2
- Weyl fermion: n_{1/2} = 2 (with negative sign)
- Dirac fermion: n_{1/2} = 4 (with negative sign)
- Massive 4D vector boson: n_1 = 3

**For our Dirac spectrum:**

Each eigenvalue |lam| of the D_{(p,q)} block (dimension dim(p,q) * 16) corresponds to a mass eigenstate in the internal space. In the 4D reduction (Paper 17, Corollary 3.4):
- The 12D spinor bundle decomposes as S_{12D} = S_{4D} tensor S_{8D}
- S_{4D} has dimension 4 (Dirac spinor in 4D)
- S_{8D} = S_K has dimension 16 (our Cliff(R^8) spinor)
- Each eigenvalue of D_K on S_K gives a 4D Dirac mass for a 4D Dirac fermion

**So each D_K eigenvalue corresponds to n_{1/2} = 4 real fermionic DOF in 4D.**

However, the D_K eigenvalues come in +/- pairs (chirality). For the CW formula, positive and negative eigenvalues give the SAME m^2 = |lam|^2. So each +/- pair contributes TWICE (once from +lam, once from -lam) to the sum over absolute values. If we sum over ALL eigenvalues (both signs), we automatically count both chiralities.

**Net fermion prefactor per eigenvalue (both +lam and -lam counted):**
- From +lam: -4/(64 pi^2) * |lam|^4 * [...]
- From -lam: -4/(64 pi^2) * |lam|^4 * [...] (same |lam|^2)
- Total per pair: -8/(64 pi^2) * |lam|^4 * [...]

BUT if we're already summing over ALL eigenvalues in the block (including both +/-), the factor of 2 is automatic, and we just need n_{1/2} = 4 per eigenvalue.

**WAIT**: The question is whether the existing code's sum over all eigenvalues in a dim(p,q)*16 block already double-counts the +/- pairs. In the collect_spectrum() code, ALL dim(p,q)*16 eigenvalues are returned, including both +lam and -lam. So the sum already includes both chiralities. The per-eigenvalue CW contribution should use n_{1/2} = 4 (Dirac fermion DOF in 4D), NOT n_{1/2} = 1.

**FOR BAPTISTA'S BOSONIC FORMULA**: The factor "3" in eq 3.87 is the massive vector boson DOF count (3 polarizations). Combined with the "4" for the number of C^2 directions, Baptista's formula gives:
```
V_CW^boson = 4 * 3 / (64 pi^2) * m_C2^4 * ln(m_C2^2/mu^2) = 12 / (64 pi^2) * m_C2^4 * ln(...)
```

**UPDATED FERMION FORMULA**: With the 4D Dirac factor:
```
V_CW^fermion = - (4 / (64 pi^2)) * sum_n d_n * |lam_n|^4 * [ln(|lam_n|^2/mu^2) - 3/2]
```

where d_n is the PW multiplicity and the sum runs over ALL eigenvalues (both +/-). If we sum only over POSITIVE eigenvalues (deduplicating the +/- pair), we need a factor of 2*4 = 8.

**THIS NEEDS CONFIRMATION FROM GEN-PHYSICIST.** The factor of 4 vs 1 changes the fermion-to-boson ratio by a factor of 4, which significantly impacts whether a minimum exists and where.

### Combined Formula (Two Variants)

**Variant A: Baptista EFT (Controlled, 1 free parameter)**

```
V_eff^A(s; kappa, mu) = V_tree(s)
    + 4 * kappa * (3/(64 pi^2)) * m_C2^4(s) * ln(m_C2^2(s)/mu^2)     [bosonic, eq 3.87]
    - (1/(64 pi^2)) * SUM_{n in EFT} d_n * |lam_n(s)|^4 * [ln(|lam_n(s)|^2/mu^2) - 3/2]    [fermionic]
```

where "n in EFT" means Dirac eigenvalues BELOW the cutoff (|lam_n| < Lambda_EFT). The kappa parameter absorbs the overall normalization mismatch between the Baptista formula (which uses a specific convention for the mass dimension) and the Dirac spectrum units.

**Variant B: Full Spectral CW (Uncontrolled, 1 free parameter)**

```
V_eff^B(s; Lambda) = V_tree(s)
    + 4 * (1/(64 pi^2)) * m_C2^4(s) * [ln(m_C2^2(s)/Lambda^2) - 3/2]    [bosonic]
    - (1/(64 pi^2)) * SUM_{all n} d_n * |lam_n(s)|^4 * [ln(|lam_n(s)|^2/Lambda^2) - 3/2]    [fermionic]
```

where the sum runs over ALL computed eigenvalues (p+q <= max_pq_sum). Lambda is the UV cutoff.

---

## II. CODE SPECIFICATION

### Pseudocode for `compute_veff_full()`

```python
def compute_veff_full(s, gens, f_abc, gammas, max_pq_sum=6,
                      kappa=1.0, mu=1.0, approach='baptista_eft',
                      lambda_eft_cutoff=None):
    """
    Compute the full V_eff(s) including boson + fermion CW.

    Args:
        s: Jensen deformation parameter
        gens, f_abc, gammas: SU(3) infrastructure (precomputed)
        max_pq_sum: truncation level for Dirac spectrum
        kappa: coupling constant for Baptista bosonic CW
        mu: renormalization scale
        approach: 'baptista_eft' (Variant A) or 'full_spectral' (Variant B)
        lambda_eft_cutoff: if set, only include |lam_n| < this in fermion sum

    Returns:
        V_eff: total effective potential
        V_tree: classical part
        V_boson: bosonic CW
        V_fermion: fermionic CW
        diagnostics: dict with eigenvalue stats, convergence info
    """
    # Step 1: Classical tree-level
    V_tree = baptista_V_potential(0.0, s)

    # Step 2: Bosonic CW (4 C^2 gauge bosons)
    m2_C2, _ = gauge_boson_masses_baptista(0.0, s)

    if m2_C2 > 1e-30:
        if approach == 'baptista_eft':
            V_boson = 4 * kappa * (3.0 / (64 * pi**2)) * m2_C2**2 * log(m2_C2 / mu**2)
        else:  # full_spectral
            V_boson = 4 * (1.0 / (64 * pi**2)) * m2_C2**2 * (log(m2_C2 / mu**2) - 1.5)
    else:
        V_boson = 0.0

    # Step 3: Fermionic CW (Dirac spectrum)
    all_evals, eval_data = collect_spectrum(s, gens, f_abc, gammas,
                                           max_pq_sum=max_pq_sum, verbose=False)

    V_fermion = 0.0
    n_modes_included = 0
    n_modes_excluded = 0
    max_lam_included = 0.0

    for ev, pw_mult in all_evals:
        lam = abs(ev)
        if lam < 1e-12:
            continue  # skip zero modes

        if lambda_eft_cutoff is not None and lam > lambda_eft_cutoff:
            n_modes_excluded += 1
            continue

        lam2 = lam**2
        lam4 = lam2**2

        # NEGATIVE sign for fermions
        V_fermion -= pw_mult * (1.0 / (64 * pi**2)) * lam4 * (log(lam2 / mu**2) - 1.5)

        n_modes_included += 1
        max_lam_included = max(max_lam_included, lam)

    V_eff = V_tree + V_boson + V_fermion

    diagnostics = {
        'n_modes_fermi': n_modes_included,
        'n_modes_excluded': n_modes_excluded,
        'max_lam': max_lam_included,
        'V_tree': V_tree,
        'V_boson': V_boson,
        'V_fermion': V_fermion,
        'ratio_fermi_boson': abs(V_fermion / V_boson) if abs(V_boson) > 1e-30 else float('inf'),
    }

    return V_eff, V_tree, V_boson, V_fermion, diagnostics
```

### Pseudocode for `veff_sweep()`

```python
def veff_sweep(s_values, gens, f_abc, gammas, max_pq_sum=6,
               kappa=1.0, mu=1.0, approach='baptista_eft',
               lambda_eft_cutoff=None):
    """
    Sweep V_eff over s-values. Core computation.

    OPTIMIZATION: Precompute SU(3) infrastructure ONCE.
    The Dirac spectrum must be recomputed at each s because
    the metric (and hence connection, Omega) changes.

    CACHING: For convergence tests, store eigenvalues at each (s, max_pq_sum)
    in a dict or file.
    """
    results = {
        's': s_values,
        'V_eff': np.zeros(len(s_values)),
        'V_tree': np.zeros(len(s_values)),
        'V_boson': np.zeros(len(s_values)),
        'V_fermion': np.zeros(len(s_values)),
    }

    for i, s in enumerate(s_values):
        V_eff, V_t, V_b, V_f, diag = compute_veff_full(
            s, gens, f_abc, gammas, max_pq_sum=max_pq_sum,
            kappa=kappa, mu=mu, approach=approach,
            lambda_eft_cutoff=lambda_eft_cutoff
        )
        results['V_eff'][i] = V_eff
        results['V_tree'][i] = V_t
        results['V_boson'][i] = V_b
        results['V_fermion'][i] = V_f

    # Find minimum
    idx_min = np.argmin(results['V_eff'])
    s_0 = s_values[idx_min]

    return results, s_0
```

### Pseudocode for `convergence_test()`

```python
def convergence_test(s_test_values, gens, f_abc, gammas,
                     pq_levels=[3, 4, 5, 6], kappa=1.0, mu=1.0):
    """
    Test convergence of V_eff and s_0 with max_pq_sum.

    CRITICAL TEST: If s_0 changes by more than 0.1 between
    pq_levels, the truncation is unreliable.
    """
    for max_pq in pq_levels:
        results, s_0 = veff_sweep(s_test_values, ..., max_pq_sum=max_pq, ...)
        record(max_pq, s_0, results)

    # Report s_0(max_pq) and |s_0(6) - s_0(3)|
```

### Real Code Plan

| File | New function | Lines est. | Dependencies |
|------|-------------|-----------|--------------|
| `spectral_veff.py` | `compute_veff_full()` | ~60 | `collect_spectrum`, `baptista_V_potential`, `gauge_boson_masses_baptista` |
| `spectral_veff.py` | `veff_sweep()` | ~40 | `compute_veff_full` |
| `spectral_veff.py` | `convergence_test()` | ~30 | `veff_sweep` |
| `spectral_veff.py` | `veff_kappa_scan()` | ~40 | `compute_veff_full` with kappa loop |
| `spectral_veff.py` | `veff_mu_sensitivity()` | ~20 | `veff_sweep` with mu loop |
| `spectral_veff.py` | `plot_veff_decomposition()` | ~30 | matplotlib |
| `run_veff.py` (new script) | `main()` | ~80 | All above |

**Total new code**: ~300 lines
**Modified code**: ~20 lines (adding imports to spectral_veff.py header)

---

## III. EIGENVALUE CATALOG: DETAILED INVENTORY

### Sector-by-Sector Eigenvalue Census at p+q <= 6

| (p,q) | dim | Block size | # eigenvalues | PW weight | Casimir C_2 | Expected |lam| range |
|-------|-----|-----------|--------------|-----------|-------------|-------------------|
| (0,0) | 1 | 16 | 16 | 1 | 0 | [0, ~0.5] (pure Omega) |
| (1,0) | 3 | 48 | 48 | 3 | 4/3 | [0.3, ~1.5] |
| (0,1) | 3 | 48 | 48 | 3 | 4/3 | [0.3, ~1.5] |
| (1,1) | 8 | 128 | 128 | 8 | 3 | [0.5, ~3.0] |
| (2,0) | 6 | 96 | 96 | 6 | 10/3 | [0.5, ~3.0] |
| (0,2) | 6 | 96 | 96 | 6 | 10/3 | [0.5, ~3.0] |
| (3,0) | 10 | 160 | 160 | 10 | 6 | [1.0, ~5.0] |
| (0,3) | 10 | 160 | 160 | 10 | 6 | [1.0, ~5.0] |
| (2,1) | 15 | 240 | 240 | 15 | 16/3 | [0.8, ~5.0] |
| (1,2) | 15 | 240 | 240 | 15 | 16/3 | [0.8, ~5.0] |
| (4,0) | 15 | 240 | 240 | 15 | 28/3 | [1.5, ~7.0] |
| (0,4) | 15 | 240 | 240 | 15 | 28/3 | [1.5, ~7.0] |
| (3,1) | 24 | 384 | 384 | 24 | 9 | [1.5, ~8.0] |
| (1,3) | 24 | 384 | 384 | 24 | 9 | [1.5, ~8.0] |
| (2,2) | 27 | 432 | 432 | 27 | 8 | [1.5, ~7.5] |
| (5,0) | 21 | 336 | 336 | 21 | 40/3 | [2.0, ~10.0] |
| (0,5) | 21 | 336 | 336 | 21 | 40/3 | [2.0, ~10.0] |
| (4,1) | 35 | 560 | 560 | 35 | 40/3 | [2.0, ~10.0] |
| (1,4) | 35 | 560 | 560 | 35 | 40/3 | [2.0, ~10.0] |
| (3,2) | 42 | 672 | 672 | 42 | 12 | [2.0, ~10.0] |
| (2,3) | 42 | 672 | 672 | 42 | 12 | [2.0, ~10.0] |
| (6,0) | 28 | 448 | 448 | 28 | 18 | [3.0, ~12.0] |
| (0,6) | 28 | 448 | 448 | 28 | 18 | [3.0, ~12.0] |
| (5,1) | 48 | 768 | 768 | 48 | 52/3 | [3.0, ~12.0] |
| (1,5) | 48 | 768 | 768 | 48 | 52/3 | [3.0, ~12.0] |
| (4,2) | 60 | 960 | 960 | 60 | 16 | [2.5, ~12.0] |
| (2,4) | 60 | 960 | 960 | 60 | 16 | [2.5, ~12.0] |
| (3,3) | 64 | 1024 | 1024 | 64 | 15 | [2.5, ~12.0] |

**Total eigenvalues at p+q <= 6**: ~12,000
**Total weighted modes (PW)**: sum_pq dim(p,q) * block_size ~ 500,000+

### Degeneracy Structure and Spin Statistics Signs

ALL eigenvalues from D_K are **fermionic** (negative sign in CW formula).

Within each sector (p,q), the dim(p,q)*16 eigenvalues come in +/- pairs (Dirac spectrum symmetry). The absolute values |lambda| are the physical masses. Each appears with Peter-Weyl weight d_n = dim(p,q) in the L^2 trace.

For the CW sum, the **effective fermion DOF** per eigenvalue is:
- 4 (= 2 spin x 2 from Dirac +/- pairing) for a 4D Dirac fermion
- But this is ALREADY accounted for in the block structure: the 16-dimensional spinor includes both chiralities

The per-eigenvalue CW contribution (before PW weighting) is:
```
delta V_fermion = - (1/(64 pi^2)) * |lam|^4 * [ln(|lam|^2/mu^2) - 3/2]
```

The PW-weighted contribution from sector (p,q) is:
```
V_fermion^{(p,q)} = - dim(p,q) * sum_{j=1}^{dim(p,q)*16} (1/(64 pi^2)) * |lam_j|^4 * [ln(|lam_j|^2/mu^2) - 3/2]
```

### Truncation Error Bounds

The CW sum is weighted by |lam_n|^4. The dominant contribution comes from the HIGHEST eigenvalues included. At p+q = N, eigenvalues scale roughly as:

```
|lam|_max ~ sqrt(C_2(N,0)/c) ~ N * sqrt(1/c)     (for Casimir scaling)
```

where c depends on the metric normalization.

**Weyl's law asymptotic**: For the Dirac operator on an 8-dimensional manifold, the eigenvalue counting function satisfies:
```
N(Lambda) ~ C * Lambda^8     (as Lambda -> infinity)
```

This means the CW sum weighted by lam^4 converges like:
```
sum_{|lam| > Lambda_cut} |lam|^4 ~ integral from Lambda_cut to infinity of lam^4 * lam^7 d(lam) / lam^8 = DIVERGENT
```

**The CW sum is UV-DIVERGENT in the full theory.** Truncation at p+q <= 6 is a UV REGULATOR, not an approximation. The physical content is in the s-DEPENDENCE of the truncated sum, not the absolute value.

This means:
1. The SHAPE of V_eff(s) should stabilize with increasing max_pq_sum (modes at high p+q contribute roughly equally at all s)
2. The LOCATION s_0 of the minimum should converge
3. The ABSOLUTE VALUE of V_eff does NOT converge (requires renormalization)

**Convergence test prescription**: Plot s_0(max_pq_sum) for max_pq = 3, 4, 5, 6. If s_0 changes by less than 0.1 from pq=5 to pq=6, declare convergence. If it changes by more than 0.5, truncation is unreliable.

---

## IV. NUMERICAL HAZARD ANALYSIS

### Hazard 1: UV Dominance (CRITICAL)

The |lam|^4 weighting means high-lying modes dominate the CW sum. At p+q=6:
- Largest |lam| ~ 12 (in Killing metric units)
- |lam|^4 ~ 20,000
- PW weight for (3,3): 64
- Single mode contribution: ~ 64 * 20000 / (64 pi^2) ~ 2000

Compare to the 4 C^2 bosons at s=1:
- m_C2^2(s=1) ~ 3 (from Baptista formula)
- m_C2^4 ~ 9
- Bosonic CW: 4 * 9 / (64 pi^2) ~ 0.06

**The fermion CW is ~30,000x larger than the bosonic CW at p+q=6.**

This is not a bug -- it reflects the physical fact that there are FAR more fermionic KK modes than light bosonic modes. The minimum of V_eff comes from the COMPETITION between V_tree (positive at large s) and the fermion CW (negative, growing faster than V_tree).

**Mitigation**: Work with normalized quantities. Define V_eff_norm(s) = V_eff(s) - V_eff(s_ref) for a reference point s_ref (e.g. s=0). The mu-dependent constant cancels. Alternatively, use the mu-independent combination: d V_eff/ds.

### Hazard 2: Logarithmic Sensitivity to mu (MODERATE)

The CW formula contains ln(|lam|^2/mu^2). Changing mu shifts V_eff by a constant (mu-independent):
```
V_eff(s; mu') = V_eff(s; mu) + C * ln(mu'^2/mu^2)
```
where C = sum d_n |lam_n(s)|^4 (depends on s only through the spectrum).

**The location s_0 is mu-DEPENDENT** in general. However, if the dominant contribution to the minimum comes from the interplay between V_tree (mu-independent) and V_CW (mu-dependent), then s_0(mu) traces a curve. The physical mu is set by the compactification scale ~ Planck mass.

**Mitigation**: Sweep mu over [0.1, 10] and report s_0(mu). If s_0 varies by less than 0.2, the result is robust. If it varies by more than 1.0, the calculation is unreliable.

### Hazard 3: Zero Mode Singularity (LOW)

At s=0, some eigenvalues may be zero (e.g. from the (0,0) sector). The ln(|lam|^2) term diverges.

**Mitigation**: Skip modes with |lam| < epsilon (say 1e-12). Zero modes do not contribute to the s-derivative dV/ds (they are s-independent to leading order), so they do not affect the minimum location.

### Hazard 4: Numerical Cancellation (MODERATE)

The fermion sum involves ~12,000 terms at p+q=6, each of order 10^3 to 10^5 (from lam^4 * ln(lam^2) weighting). The total is O(10^7). The s-derivative (which determines the minimum) may involve cancellations.

**Mitigation**: Use double precision throughout (sufficient for ~15 digits). If cancellation is suspected, verify by computing dV/ds via finite differences: [V(s+h) - V(s-h)]/(2h) for h = 1e-5, 1e-6, 1e-7 and checking consistency.

### Hazard 5: Eigensolver Stability at Large Block Sizes (LOW)

At (3,3), the Dirac block is 1024 x 1024 complex. numpy.linalg.eigvals on a 1024x1024 matrix is routine (milliseconds). But eigenvalue accuracy may degrade for near-degenerate eigenvalues.

**Mitigation**: Use eigvalsh on the Hermitian matrix i*D (which has real eigenvalues) instead of eigvals on D. This is already done for the trivial sector but not for general sectors in the current code (line 1328 uses eigvals, not eigvalsh).

### Hazard Summary Table

| Hazard | Severity | Impact on s_0 | Mitigation |
|--------|----------|---------------|------------|
| UV dominance | CRITICAL | Large fermion >> small boson | Use normalized V_eff or dV/ds |
| mu sensitivity | MODERATE | s_0(mu) curve, not point | Sweep mu, report range |
| Zero modes | LOW | None (skip) | epsilon threshold |
| Cancellation | MODERATE | dV/ds accuracy | Finite difference check |
| Eigensolver | LOW | Eigenvalue accuracy | Use eigvalsh on i*D |

---

## V. PASS/FAIL CRITERIA

### Test 1: V_eff Minimum Existence

| Criterion | Condition | Verdict |
|-----------|-----------|---------|
| PASS | V_eff has a local minimum at s_0 > 0 for natural kappa (0.1-10) or natural mu | Framework viable |
| STRONG PASS | Minimum at s_0 where m_{(3,0)}/m_{(0,0)} within 1% of phi_paasch | Framework predictive |
| FAIL | V_eff monotonic for ALL kappa in [0.01, 1000] AND ALL mu in [0.01, 100] | Perturbative stabilization CLOSED |

### Test 2: Convergence with Truncation

| Criterion | Condition | Verdict |
|-----------|-----------|---------|
| PASS | |s_0(pq=6) - s_0(pq=5)| < 0.1 | Truncation reliable |
| MARGINAL | 0.1 < |s_0(pq=6) - s_0(pq=5)| < 0.5 | Results indicative, not conclusive |
| FAIL | |s_0(pq=6) - s_0(pq=5)| > 0.5 | Truncation unreliable, need higher pq |

### Test 3: mu-Sensitivity

| Criterion | Condition | Verdict |
|-----------|-----------|---------|
| PASS | |s_0(mu=0.1) - s_0(mu=10)| < 0.3 | Robust prediction |
| FAIL | |s_0(mu=0.1) - s_0(mu=10)| > 1.0 | mu-dependent, not predictive |

### Test 4: Boson-Fermion Balance

| Criterion | Condition | Verdict |
|-----------|-----------|---------|
| HEALTHY | |V_fermion(s_0)|/|V_boson(s_0)| in [0.5, 100] | Balance reasonable |
| UNNATURAL | Ratio > 1000 | Fine-tuning required |

### Test 5: Baptista Consistency

| Criterion | Condition | Verdict |
|-----------|-----------|---------|
| PASS | Shape of V_eff^A(s) qualitatively matches V_eff^B(s) | Approaches consistent |
| FAIL | Different number of minima or minimum at opposite s | Approaches contradict |

### Combined Outcomes

| If... | Then... | Framework impact |
|-------|---------|-----------------|
| Minimum exists at natural params + converged + robust | PROCEED to mass ratios, gauge couplings | +10-15% |
| Minimum exists but mu-sensitive or unconverged | INDICATIVE only, need higher pq or non-pert | +5% |
| No minimum for any params | Perturbative V_eff CLOSED, Pfaffian route essential | -5% (already in base rate) |
| Minimum at s_0 where phi_paasch appears in mass ratios | MAJOR RESULT | +15-20% |

---

## VI. TIMELINE AND DEPENDENCIES

### Phase 1: Infrastructure (Day 1, ~4 hours)

1. Add `compute_veff_full()` to `spectral_veff.py`
2. Add `veff_sweep()` to `spectral_veff.py`
3. Test at max_pq_sum=3 (fast, ~5 min for 50 s-points)
4. Verify against existing `baptista_Veff()` (bosonic-only should match)

### Phase 2: Production Run (Day 1-2, ~12 hours compute)

1. Run veff_sweep at max_pq_sum=6, 200 s-points in [0, 2.5]
   - Estimated: 200 * 30s = 100 min per (kappa, mu) pair
   - With 5 kappa values and 3 mu values: 15 * 100min = 25 hours
   - OPTIMIZATION: Cache eigenvalues per s-value and reuse across kappa/mu
   - With caching: 100 min (eigenvalues) + 15 * 5 min (CW evaluation) = ~175 min
2. Run convergence_test at max_pq = 3, 4, 5, 6
   - Estimated: 4 * 100 min = ~7 hours (can be parallelized)

### Phase 3: Analysis (Day 2, ~2 hours)

1. Identify s_0 (if exists) for each (kappa, mu)
2. Compute mass ratios at s_0
3. Compute gauge couplings at s_0
4. Apply pass/fail criteria
5. Write results into meeting minutes

### Dependencies

```
[Precomputed] SU(3) infrastructure (gens, f_abc, gammas)
    |
    v
[Phase 1] compute_veff_full() + veff_sweep()
    |
    v
[Phase 2a] Eigenvalue caching at max_pq=6, 200 s-values  <-- BOTTLENECK
    |
    v
[Phase 2b] CW evaluation sweep (fast, uses cached eigenvalues)
    |         |
    v         v
[Phase 3a] s_0 identification    [Phase 3b] Convergence test
    |
    v
[Phase 3c] Mass ratios + gauge couplings at s_0
    |
    v
[Phase 3d] Pass/fail evaluation
```

### Blocking Issues

1. **Runtime at max_pq=6**: The (3,3) block is 1024x1024 and takes ~1-2s to diagonalize. With 28 sectors and 200 s-points, total is ~200 * 28 * 0.5s ~ 47 min for just eigenvalue computation. Not blocking but should start early.

2. **Memory for eigenvalue cache**: 28 sectors * 200 s-points * ~500 eigenvalues avg * 16 bytes = ~45 MB. Not blocking.

3. **No new mathematical infrastructure needed**: All functions (collect_spectrum, baptista_V_potential, gauge_boson_masses_baptista) exist. Only ~300 lines of new code.

---

## VII. SPECTRAL vs EFT FORMULATION OF V_1loop

### Two Distinct Formulations

**Formulation 1: Spectral (zeta-function / heat kernel)**

The one-loop effective action from integrating out a field with kinetic operator D^2 is:
```
Gamma_1loop = -(1/2) * sign * Tr(ln(D^2/mu^2))
            = -(1/2) * sign * sum_n ln(lam_n^2/mu^2)
```
where sign = +1 for bosons, -1 for fermions.

This is what `one_loop_potential_zeta()` computes (with sign = +1, treating all modes as bosonic). The minimum of Gamma_1loop gives the shape that minimizes the functional determinant -- i.e. the SPECTRAL free energy. This is the Chamseddine-Connes approach.

**Formulation 2: Coleman-Weinberg (EFT)**

After integrating out a field at one loop in 4D, the contribution to the effective potential is:
```
V_CW = sign * (n_j / (64 pi^2)) * m^4 * [ln(m^2/mu^2) - c_j]
```
where:
- sign = +1 for bosons, -1 for fermions
- n_j = real DOF per mode (1 for real scalar, 2 for complex scalar, 4 for Dirac fermion, 3 for massive vector)
- c_j = 3/2 (scalars, fermions) or 5/6 (vectors) in MS-bar
- m = mass of the 4D field = D_K eigenvalue for fermions

This is the QFT formula for the effective potential in 4D. Baptista's eq 3.87 is this formula.

### Connection Between Formulations

They are related by dimensional analysis. In the spectral formulation, we sum ln(lam^2). In the CW formulation, we sum lam^4 * ln(lam^2). The difference is that the CW formula has already performed the momentum integration in 4D, which gives the lam^4 factor (the 4D field has mass lam, and integrating the 4D loop gives m^4 * ln(m^2)).

**Which should we use?**

For determining s_0, we need the CW formulation (Formulation 2) because:
1. It correctly accounts for the 4D field content (spin statistics, DOF)
2. It matches Baptista's eq 3.87 (which uses the CW formula for bosons)
3. The spectral formulation (Formulation 1) gives V_zeta minimum at s=0, which is the WRONG physics (it doesn't account for the tree-level potential)

The tree-level V_tree + CW correction is the standard procedure in effective field theory.

### Reconciliation

V_eff = V_tree + V_CW (Formulation 2) is the correct formula.

The spectral action Tr(f(D^2/Lambda^2)) (Formulation 1, with exponential cutoff) is a DIFFERENT object: it encodes the GEOMETRY of the internal space, not the 4D effective potential. Its minimum at s=0 tells us the internal geometry prefers maximum symmetry -- which is correct, as confirmed by the tree-level potential V_tree having no non-trivial minimum. The CW correction adds quantum effects that can break this preference.

---

## VIII. OPEN QUESTIONS FOR TEAM CONVERGENCE

### Q1: EFT Cutoff for Fermion Sum

Should we include ALL Dirac eigenvalues up to p+q=6, or only the "light" modes below some EFT cutoff Lambda_EFT?

**KK-theorist position**: The physically correct approach is the EFT one: include only modes with |lam| < Lambda_EFT, where Lambda_EFT is the scale at which the 4D effective theory breaks down (typically the compactification scale). The full sum is UV-divergent and requires renormalization. The truncation at p+q=6 is a proxy for this cutoff.

**Issue**: We don't know Lambda_EFT a priori. It should be self-consistently determined by the eigenvalue spectrum (roughly, Lambda_EFT ~ |lam|_min at (1,0) sector, i.e. the lightest KK mass).

**Proposal**: Run both:
- Full sum (all modes up to p+q=6): this is what Feynman asked for
- EFT sum (only modes with |lam| < 5 * |lam_min|): this is what Baptista intended
- Compare s_0 from both

### Q2: Kappa vs Lambda Normalization

Baptista's eq 3.87 uses kappa (dimensionless), while the full CW uses Lambda (energy scale). The relationship is:

```
kappa * (3/(64 pi^2)) * m^4 * ln(m^2/mu^2)  <==>  (1/(64 pi^2)) * m^4 * [ln(m^2/Lambda^2) - 3/2]
```

Matching: kappa * 3 * ln(m^2/mu^2) = ln(m^2/Lambda^2) - 3/2

This gives: Lambda^2 = mu^2 * exp(3/2 - 3*kappa*ln(m^2/mu^2))

There is NO clean 1-to-1 mapping because kappa multiplies the ENTIRE bosonic term in Baptista's formula, while the full CW has NO free prefactor. They are DIFFERENT EFT truncations.

**Proposal**: Report results for BOTH approaches with their respective free parameters.

### Q3: Should the Radion Mass Enter?

The scalar modulus s itself has a mass m_s^2 = d^2 V_tree / ds^2. This is a BOSONIC mode that contributes to V_CW with positive sign. Including it creates a self-consistency loop: V_eff depends on m_s^2 which depends on V_eff.

**KK-theorist position**: For the FIRST computation, EXCLUDE the radion. Its mass at s=0 is zero (flat direction of V_tree), so it contributes nothing at s=0. At s > 0, the radion mass is O(V_tree''(s)) which is parametrically smaller than the KK tower. Including it is a higher-order correction.

---

## IX. SUMMARY

### What We're Computing

The 1-loop Coleman-Weinberg effective potential V_eff(s) for the Jensen shape modulus, including:
- Tree-level: Baptista eq 3.80 (analytical, coded)
- Bosonic CW: 4 C^2 gauge bosons, Baptista eq 3.84/3.87 (analytical, coded)
- **NEW**: Fermionic CW from the FULL Dirac spectrum at p+q <= 6 (~12,000 eigenvalues, negative sign)

### Why It Matters

This is the FIRST computation to include both bosonic and fermionic 1-loop contributions. All previous V_eff analyses (Sessions 13-14) used only the bosonic part. The fermion sign could dramatically shift s_0.

### What It Will Tell Us

1. Whether perturbative moduli stabilization WORKS (exists a minimum)
2. The value of s_0 (and whether mass ratios at s_0 are physically interesting)
3. Whether the truncation at p+q=6 is reliable
4. Whether Feynman's fermion-sign insight produces natural kappa values

### What It Won't Tell Us

1. Whether s_0 is the TRUE vacuum (could be local minimum, not global)
2. Non-perturbative corrections (instantons, condensates)
3. Topological stabilization (Pfaffian -- separate computation)
4. Absolute mass scale (requires fixing overall constants)

---

## X. HAWKING THERMODYNAMIC LAYER (Incorporated from Round 2a Hawking contribution)

See full document: `session-16-round-2a-hawking-thermodynamics.md`

### Key Identification Adopted

V_CW IS the Helmholtz free energy: F = U - TS, where T ~ Lambda^2 (UV cutoff = temperature).
This is not a relabeling -- it makes three predictions absent from the bare V_eff framework:

1. **Thermal restoration**: At T >> T_c, entropy dominates, s_0 = 0 (symmetric phase). The internal space was symmetric in the early universe.
2. **Continuous transition**: Jensen family is smooth. No barrier. Transition from s=0 to s_0 > 0 is second-order or BKT-like.
3. **Critical temperature T_c**: Calculable from spectral data. Above T_c: s_0=0. Below T_c: s_0(T) > 0 smoothly.

### Four Additional Diagnostics (ADOPTED, add to code spec)

**D1. Thermodynamic decomposition** -- At every s, output U(s) and T*S(s) separately:
```
U(s) = (1/64*pi^2) * Sum_n d_n * |lam_n(s)|^4
TS(s) = (1/64*pi^2) * Sum_n d_n * |lam_n(s)|^4 * ln(|lam_n(s)|^2)
```
Reveals whether minimum is energy-driven (fragile) or entropy-driven (robust).

**D2. Spectral entropy** -- Shannon entropy of Boltzmann-weighted eigenvalue distribution:
```
S_spectral(s) = -Sum_n p_n(s) * ln(p_n(s))
where p_n(s) = d_n * exp(-|lam_n(s)|^2/Lambda^2) / Z(s)
```
Prediction: S_spectral maximum correlates with V_eff minimum (|s_max - s_0| < 0.3).

**D3. Phase transition scan** -- Sweep Lambda over [0.01, 100], track s_0(Lambda).
Prediction: continuous onset at Lambda_c (second-order). Plot s_0 vs Lambda.

**D4. Specific heat sign** -- d^2V_CW/d(mu^2)^2 at s_0.
C_V > 0: standard equilibrium. C_V < 0: Bekenstein-Hawking regime (gravitational thermodynamics).

### Six Binding Consistency Checks (ADOPTED)

At every candidate s_0, ALL must pass:

| # | Check | Formula | If fails |
|---|-------|---------|----------|
| 1 | Free energy ordering | F(s_0) < F(0) | s_0 is metastable, not ground state |
| 2 | Stability | d^2F/ds^2 > 0 at s_0 | Saddle point, not minimum |
| 3 | Finite specific heat | C_s finite | Phase transition AT s_0 |
| 4 | Bekenstein bound | S_spectral(s_0) <= O(1) at R~l_Pl | Planck-scale assumption violated |
| 5 | Species bound | N_species * m_lightest^2 <= M_Pl^2 | Trivially satisfied at our truncation |
| 6 | GSL | dS_gen/dt >= 0 on trajectories | Non-binding at equilibrium |

### Hawking's Prediction: Natural kappa

With fermion sign included, the boson-fermion competition should give s_0 at LOWER kappa than bosons-only. Round 1c found kappa ~ 50-100 for s_0 = 0.15 (bosons only). Hawking predicts kappa ~ 1-10 with fermions. If this does NOT happen, entropy argument fails.

### KK-Theorist Response: Temperature Regime Question (OPEN)

Hawking identifies mu as temperature. But there is a critical subtlety:

- **CW regime (T << m_n)**: V ~ m^4 * ln(m^2/T^2). UV-dominated (|lam|^4 weighting). This is what we specified in Sections I-VII.
- **High-T regime (T >> m_n)**: V ~ T^2 * Sum m_n^2(s). UV-tamer (|lam|^2 weighting). Qualitatively different behavior.

At the compactification scale, ALL KK modes have m ~ O(1/R) ~ M_Pl, and T ~ Lambda^2 ~ M_Pl^2. So T >> m for ALL modes. The high-T expansion may be the physically correct one.

**Resolution**: Compute BOTH regimes. If they agree on s_0 location, robust. If they disagree, the temperature assignment becomes load-bearing.

### DOF Envelope Computation (from Hawking Section VIII, ADOPTED)

Run V_eff at n_{1/2} = 1 and n_{1/2} = 4 per Dirac eigenvalue. If both show minimum at similar s_0, result is robust. Zero additional infrastructure cost.

---

## XI. CONSOLIDATED PASS/FAIL CRITERIA (Merged: Sections V + X)

### Tier 1: Existence Tests (BLOCKING)
1. V_eff(s) has a local minimum at s_0 > 0 (not at boundary)
2. F(s_0) < F(0) (Hawking Check 1: broken phase wins)
3. d^2F/ds^2 > 0 at s_0 (Hawking Check 2: genuine minimum)

### Tier 2: Robustness Tests (QUALITY)
4. |s_0(pq=6) - s_0(pq=5)| < 0.1 (truncation convergence)
5. s_0(n_{1/2}=1) and s_0(n_{1/2}=4) agree within 0.2 (DOF robustness)
6. s_0 stable under mu variation by factor 2 (shift < 0.3)
7. CW regime and high-T regime give same s_0 qualitatively

### Tier 3: Physics Tests (SIGNIFICANCE)
8. Mass ratios m_{(p,q)}/m_{(p',q')} at s_0 compared to SM ratios
9. Gauge couplings g_i(s_0) compared to SM values
10. Spectral entropy maximum correlates with s_0 (|s_max - s_0| < 0.3)
11. C_V sign at s_0 (canonical stability vs gravitational regime)
