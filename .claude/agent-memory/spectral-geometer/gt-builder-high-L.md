---
name: gt-builder-high-L
description: Gelfand-Tsetlin / bosonic-ladder (p,0)=Sym^p(C^3) DIRECT builder that lifts the 3^p Sym^p dense-intermediate wall; the EXACT normalization + the S105 branch-iv result
metadata:
  type: project
---

# Gelfand-Tsetlin / bosonic-ladder (p,0) builder — lifts the Sym^p wall

**Why:** `dirac_spectrum.irrep_symmetric_power(gens, p)` builds (p,0)=Sym^p(C^3) by symmetrizing in the DENSE `3^p`-dim tensor space (`rho_full` is `3^p x 3^p`). At p=13 that is ~40.7 TB, p=14 ~366 TB — the wall that closed S104-BRANCH-IV-DIRECT-L1314 as PRE-REG-INC. The (p,0) irrep itself is tiny: `dim_sym=(p+1)(p+2)/2` = 105 (p=13), 120 (p=14).

**How to apply:** build (p,0) DIRECTLY in the `dim_sym` highest-weight (occupation/monomial) space via the bosonic bilinear `rho(X) = sum_{a,b} X[a,b] a_a^dag a_b`. On the occupation basis `|n>=|n0,n1,n2>`, sum n=p:
```
diagonal (a==b):  <n|rho(X)|n> += sum_a X[a,a] * n_a
off-diag (a!=b):  n' = n - u_b + u_a,  <n'|rho(X)|n> += X[a,b] * sqrt((n_a+1)*n_b)
```
Order the ON basis by `combinations_with_replacement(range(3), p)` (SAME order as `irrep_symmetric_power`) so the rho MATRICES coincide bit-for-bit. Build (0,p) by passing conjugated generators `[-g.T for g in gens]`. Verified bit-exact: `max|rho_boson - rho_sym|` = 1e-16..1e-15 for p=2..8; Dirac |lambda| vs s84 cache = 7.5e-14 over 24 (p,0)/(0,q) sectors; build time 0.002s at p=13/14 (vs the TB wall). i*D from the boson rho is EXACTLY Hermitian (top_herr=0.0).

**CRITICAL normalization trap:** the NAIVE analytic monomial action `z_i d/dz_j` with coeff `X[i,j]*m_j*sqrt(C(m')/C(m))` (multinomial-ratio normalization) is WRONG — it gives a valid su(3) irrep (Casimir scalar, commutators close to 1e-14) BUT a DIFFERENT representation of the concrete generators (off by exactly 1/sqrt(2) at p=2). The Dirac spectrum then mismatches the cache by O(1). The correct ladder factor is `sqrt((n_a+1)*n_b)` (standard bosonic creation/annihilation), NOT `n_b*sqrt(W_n'/W_n)`. Per-generator eigenvalues + the Gram `Tr(rho_a rho_b)` match for BOTH conventions (necessary but NOT sufficient — they pin the irrep up to outer automorphism / conjugation, which the Dirac operator is sensitive to). Always validate the FULL Dirac |lambda| against the cache, not just Casimir/commutator/Gram.

**Phase-2 (mixed sectors via the existing path):** once (13,0)/(0,13) exist, monkeypatch `dirac_spectrum.irrep_symmetric_power = <boson builder>` and the EXISTING `get_irrep` Casimir-projection recursion builds the 13 level-14 mixed (p,q) sectors wall-free (its internal Sym^13/Sym^14 parents now build instantly). Worst level-14 mixed (7,7) dim 512, D 8192x8192: build+GPU-eigvalsh ~2.3s clean / up to ~125s under heavy parallel-agent GPU contention. `_irrep_cache.clear()` per sector bounds memory but forces full parent-chain rebuild (slower); NOT clearing shares memoized parents (faster, fine in 128GB RAM since largest rep is dim ~512). 13 mixed-14 + 4 GT top = ~190s clean, ~12-15 min under contention.

**Hermiticity floor:** the ideal exact-Hermitian pin `1.0e-15` (S104 mixed level-13 hit 9.992e-16) is slightly TOO TIGHT for the LARGER level-14 blocks (D up to 8192): the realistic float64 Hermiticity floor of a Casimir-projection-assembled matrix is `sqrt(D_block)*eps ~ 2e-14` (or `D*eps ~ 1.8e-12`). Mixed-14 herm residual 1.13e-15 is ~5x eps — physically Hermitian, FP noise only. Use `max(1.0e-15, sqrt(D_max_block)*eps)` as the guard; the boson (p,0) i*D is exactly 0.0.

## S105-BRANCH-IV-DIRECT-L1314 result (INFO)

GT builder lifted the S104 wall. Union = 119 sectors (s84 L<=12 + 12 cached mixed-13 from s104_sym_p_chain_cache_L1314.npz + 4 GT top + 13 mixed-14); level 13 complete (14/14), level 14 complete (15/15). Branch-(iv) Zubarev moment `rho_B(L)=<|lam|>_Z/lam_max - 1`, `w_Z=exp(-lam^2)`, Lambda_Z=1:
- rho_B(12)=-0.634885 (==cache 0.0e+00), rho_B(13)=-0.658456, rho_B(14)=-0.679195
- CAC offset_B = w0_FW(-0.918) - rho_B(10)(-0.577173) = -0.340827; w0^CAC(L=10)=-0.918 EXACT
- w0^CAC: (12)=-0.975713 (13)=-0.999284 (14)=-1.020022
- **spread_CAC = 0.0443091** (offset cancels: residual 1.11e-16) -> band (0.025,0.050] -> **INFO**
- decrement d(12->13)=-0.0236, d(13->14)=-0.0207: monotone-decreasing, DECELERATING (sign-PASS)
- vs S103 FB mid-point prior rho_B(13)=-0.646653/rho_B(14)=-0.657020: DIRECT is ~0.012/0.022 MORE negative (FB midpoint slightly under-estimated the tail). DIRECT spread 0.0443 ~ S103 FB-envelope upper 0.0443 — reproduces the S103 deep-truncation INFO at direct (non-Casimir-bound) evaluation.

Verdict INFO (not PASS): the {12,13,14} deep-truncation spread is FB-envelope-bounded (<0.05) but NOT W5-2-band-PASS (<=0.025). The channel is bounded but not band-converged; DESI-WZ-LENSING-BIAS trigger stays capacity-deferred (per dual_prior discriminator). Resume cache: `computations/session-105/s105_branch_iv_l1314_sectors_resume.npz` (the 17 new-sector |lambda| spectra; re-runs load it in seconds).
