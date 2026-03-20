# Session 25 Wrap-Up: [Te]S-4 -- Spectral Zeta Function as Brillouin Zone

**Agent**: Gen-Physicist (Opus 4.6)
**Date**: 2026-02-22
**Status**: DEFERRED -- requires coding the Kosmann perturbation Hamiltonian as a matrix operator

---

## Summary

Tesla proposed treating D_K eigenvalues as a lattice in spectral space, with Kosmann coupling V_{nm} as nearest-neighbor hopping, defining a tight-binding band structure. This converges with QA S-3 (tight-binding full ladder) and Paasch S-2 (spectral ladder band structure). The key question: does the resulting band structure have topological features (Dirac cones, nontrivial Chern numbers) that could provide stabilization?

## Why This Was Not Computed in Session 25

1. The Kosmann perturbation Hamiltonian H_pert for Jensen deformation has NOT been coded as a matrix operator acting between eigenvalue levels.
2. The within-singlet V_{nm} matrix exists in `s23a_kosmann_singlet.npz`, but it connects eigenvalue levels WITHIN the (0,0) sector. The full tight-binding model requires inter-sector elements, which are ZERO by W2 (block-diagonality).
3. The Berry erratum (W5) eliminates topological content: Berry curvature = 0 identically, so all band Chern numbers and Zak phases are trivially zero.

## What Would Be Required

### Within-Sector Tight-Binding (feasible now)

For each sector (p,q) independently, construct:

```
H_TB^{(p,q)}(tau) = diag(lambda_1^{(p,q)}, ..., lambda_N^{(p,q)}) + V_{nm}^{(p,q)}
```

where:
- lambda_n^{(p,q)} are the D_K eigenvalues in sector (p,q) at deformation tau
- V_{nm}^{(p,q)} = <psi_n^{(p,q)}| K_a |psi_m^{(p,q)}> is the Kosmann coupling within the sector
- N = dim(irrep) / 2 (accounting for chiral pairing)

**Data needed**: Eigenvectors at each tau (exist in `s23a_eigenvectors_extended.npz` for p+q <= 6). Kosmann generators K_a (exist as 8 anti-Hermitian matrices in the spin representation).

**Computation steps**:
1. Load eigenvectors psi_n(tau) for sector (p,q)
2. Compute V_{nm} = sum_a <psi_n| K_a |psi_m> at each tau
3. Form H_TB = diag(lambda) + V
4. Diagonalize -> dressed spectrum
5. Compare dressed mass ratios to bare ratios and to Paasch targets

**Estimated runtime**: < 5 minutes per sector, < 1 hour for all 28 sectors.

### Inter-Sector Extension (blocked)

W2 (block-diagonality) forces inter-sector V_{nm} = 0. The full multi-sector tight-binding model is therefore a direct sum of within-sector models:

H_TB^{full} = H_TB^{(0,0)} + H_TB^{(1,0)} + H_TB^{(0,1)} + ...

with no inter-sector hopping. The "Brillouin zone" decomposes into independent one-dimensional chains, one per sector. No inter-sector band crossings or Dirac cones can form.

### Topological Content (eliminated by W5)

Tesla's original proposal included Chern numbers and Dirac cones. With Berry curvature = 0:
- Band Chern numbers = 0 (trivial topology)
- Zak phases = 0 (trivial)
- No Dirac cones (these require nontrivial Berry curvature at the crossing point)
- Wilson loop = identity

The remaining non-topological content:
- Band structure shape (dispersion relation in eigenvalue-index space)
- Dressed mass spectrum (eigenvalues of H_TB vs bare eigenvalues)
- Mass ratio corrections from Kosmann coupling
- Band gaps and flat bands in the dressed spectrum

## Pre-Registered Gates

**TB-1**: If the dressed mass ratio (lambda_dressed_2 / lambda_dressed_1) in any sector crosses phi_paasch = 1.53158 at some tau in [0.05, 0.50], the tight-binding dressing provides a dynamical mechanism for the phi_paasch match. If no crossing occurs, the bare eigenvalue ratio at tau = 0.15 is the only match.

**TB-2**: If the band structure has a flat band (bandwidth < 0.01) at any tau, this signals a "heavy effective mass" mode that resists deformation -- a candidate spectral analog of confinement.

## Assessment

**Probability of qualitative novelty**: MODERATE (~25-35%). The within-sector tight-binding model adds genuine physical content (Kosmann coupling dresses the bare spectrum) even without topology. The dressed mass ratios and band structure have not been computed and could reveal unexpected features. The inter-sector blockade (W2) limits the scope but does not eliminate all interest.

**Information value**: MODERATE. The dressed mass spectrum is the most concrete prediction of the Kosmann coupling's physical effect. If dressing shifts the phi_paasch match toward (or away from) tau ~ 0.15, it changes the interpretation of the five-sigma coincidence.

**Recommended priority**: MEDIUM for Session 26 (after 12D a_4 computation). The within-sector H_TB is feasible with existing data and < 1 hour compute time.

---

*Wrap-up file for Session 25 Collaborative Workshop [Te]S-4. Gen-Physicist, 2026-02-22.*
