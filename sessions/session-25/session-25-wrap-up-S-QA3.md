# Session 25 Wrap-Up: [QA]S-3 -- Tight-Binding Extension (Full Ladder)

**Agent**: Gen-Physicist (Opus 4.6)
**Date**: 2026-02-22
**Status**: DEFERRED -- converges with [Te]S-4 and [Pa]S-2

---

## Summary

Quantum Acoustics proposed extending the tight-binding model from Session 23a (within-singlet V_{nm}) to all 28 sectors at p+q <= 6. For each sector: extract eigenvalue levels, compute Kosmann coupling V_{nm}, construct H_TB, diagonalize for molecular-orbital spectrum, compute Zak phase per band.

This proposal is IDENTICAL in mathematical content to [Te]S-4 (spectral zeta as Brillouin zone) and closely related to [Pa]S-2 (spectral ladder band structure). All three converge on the same computation: within-sector tight-binding Hamiltonian from Kosmann matrix elements.

## What Exists

### From Session 23a (s23a_kosmann_singlet.npz)

The (0,0) singlet Kosmann data includes:
- 16 eigenvalues (8 positive, 8 negative by BDI) at 9 tau values
- Kosmann coupling matrix V_{nm} within the singlet sector
- Key finding: V(gap,gap) = 0 EXACTLY (selection rule)
- V(gap,nearest) = 0.093 at tau = 0.30 (tridiagonal dominance)

### From s23a_eigenvectors_extended.npz

All 11,424 eigenvectors at p+q <= 6 across 9 tau values. This is the DATA needed for the full-ladder computation.

## Computation Plan

### Step 1: Within-sector Kosmann matrices (new computation)

For each of the 28 sectors (p,q) with p+q <= 6:

```python
# For each sector (p,q) at each tau:
psi_sector = eigenvectors for sector (p,q)  # shape: (n_eigs, dim_spinor)
K_a = Kosmann generators  # 8 matrices of size dim_spinor x dim_spinor

# Kosmann coupling matrix:
V_nm = np.zeros((n_eigs, n_eigs))
for a in range(8):
    V_nm += np.abs(psi_sector.conj() @ K_a[a] @ psi_sector.T)**2

# Or more physically: V_nm = sum_a <n|K_a|m>
```

**Data requirement**: The Kosmann generators K_a must be coded as matrices in the D_K representation. These are the covariant derivatives along the 8 left-invariant vector fields on SU(3), acting on 32-dimensional spinors. The structure exists in the spectral triple infrastructure from Sessions 7-8 but has not been exported as explicit matrix operators for all sectors.

### Step 2: Tight-binding Hamiltonian per sector

```python
H_TB = np.diag(eigenvalues_sector) + V_nm_sector
dressed_spectrum = np.linalg.eigvalsh(H_TB)
```

### Step 3: Band structure analysis

- Plot dressed eigenvalues vs bare eigenvalues at each tau
- Compute mass ratios in dressed spectrum
- Check for flat bands (bandwidth < threshold)
- Identify band crossings as function of tau

### Step 4: Zak phase (MOOT by W5)

Berry curvature = 0 identically -> Zak phases = 0 for all bands. Topological analysis provides no information. Skip.

## Block-Diagonality Constraint (W2)

The inter-sector Kosmann matrix elements V_{nm}^{(p1,q1)(p2,q2)} vanish identically for (p1,q1) != (p2,q2) by the block-diagonality theorem (Session 22b). This means:

- The full-ladder H_TB is a DIRECT SUM of sector-specific H_TB matrices
- No inter-sector band crossings
- No inter-sector hybridization
- The "full ladder" IS the collection of independent sector ladders

This does not eliminate the computation's value -- the within-sector dressed spectra have never been computed and could reveal sector-specific structure (e.g., the (3,0) sector's phi_paasch ratio might shift under Kosmann dressing).

## Pre-Registered Gates

**FL-1**: Does Kosmann dressing shift the phi_paasch crossing (m_{(3,0)}/m_{(0,0)} = 1.531580) to a different tau? If the dressed ratio crosses phi_paasch at tau = 0.15 +/- 0.01, the dressing preserves the match. If it shifts by > 0.05, the bare eigenvalue match was fortuitous.

**FL-2**: Is the dressed gap-edge splitting (within any sector) non-monotone? If dressing introduces non-monotonicity in any sector's gap-edge levels, it provides a new mechanism not present in bare eigenvalues.

## Assessment

**Recommended priority**: Identical to [Te]S-4 -- MEDIUM for Session 26. The computation is feasible (< 1 hour total for all sectors) but requires coding the Kosmann generators as matrix operators, which is new infrastructure.

---

*Wrap-up file for Session 25 Collaborative Workshop [QA]S-3. Gen-Physicist, 2026-02-22.*
