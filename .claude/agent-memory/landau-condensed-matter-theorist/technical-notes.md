---
name: Technical Notes
description: Code pitfalls, environment setup, data file locations, entropy lesson
type: reference
---

# Technical Notes

## Environment
- Papers: `researchers/Landau/` (40 papers + AGENTS.md + index.md)
- Python: ALWAYS `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
- Sessions: `sessions/`, Computation: `computations/`, Archive: `computations/`

## Code Pitfalls
- `.npz` Landau coefficients are 1D arrays. Use `float(np.asarray(d['key']).flat[0])`
- `.npz` 0D scalars: `d['M_8x8']` can be 0-dim. Use `float(np.asarray(d[k]).flat[0])`
- numpy 2.x: use `np.trapezoid` not `np.trapz` (renamed)
- `s36_mmax_authoritative.npz`: key is 'M_8x8' NOT 'M_max'. Always inspect keys first.
- `d2S_fold` and `dS_fold` in s36 are 1D arrays, not scalars
- Riemann tensor sign: Koszul-formula gives NEGATIVE Ric for compact groups. Fix: negate contraction. Verified at tau=0: R=+6 for SU(3).
- Working paper modified by other agents between Read and Edit. Use Python open/write for reliable updates.
- Bisection for m_base: use arithmetic mean, bracket from [8,15]. Geometric mean on steep function converges wrong.
- **D_K cache fiber ≠ NCG-SM particle fiber (S117-W8-1 gotcha).** `s84/s87_spectrum_cache_*.npz` store `sector_evals[(p,q)] = {dim,level,abs_evals}` with **16 abs_evals per sector = the Cliff(R⁸) SPINOR dim** (`D_pi = ΣE_ab ρ(X_b)⊗γ_a + I⊗Ω`, gammas are 16×16; (0,0)=Ω). This is a DIFFERENT ℂ¹⁶ from the W5 bimodule particle fiber ℂ³² (lepL/lepR/quarkL/quarkR). The cache carries NO particle-fiber index. To resolve the D_K spectrum by an A_K=ℂ⊕ℍ⊕M₃ algebra summand, do NOT compress by W5 spinor-index sets — that is **labeling-dependent** (R flips sign under spinor relabeling) and wrongly lets M₃ act on color-singlets. The **faithful, labeling-independent lift** of a central projection is via the Peter-Weyl COLOR-SECTOR structure (geometric SU(3) ≡ color SU(3)_c): `1_{M₃}` = projection onto color-charged (p,q)≠(0,0); complement `1_ℂ+1_ℍ` = color-singlet (0,0) electroweak content.
- **Counting-axis is sign-load-bearing for per-channel inter-summand DOS** (S117-W8-1; regulator-pin-discipline §"Counting axis"). intensive RATIO-NORMALIZED-TRACE-MEAN (ρ_g=P_g/Tr(P_g), per-mode) vs extensive RATIO-BLOCKSUM (block-sum) FLIP THE SIGN when summand mode-counts differ wildly (e.g. 16 vs 166,880): per-mode edge density vs total tower weight. Pin the counting axis explicitly; the vanishing test |R|≥1e-3 holds on both.
- **D_K has a hard spectral gap**: `|ξ|_min = 0.8197 M_KK = 1.766×Δ_BCS` at sector (0,0) (τ_fold=0.19). No near-zero modes ⇒ BCS condensation weight |w|=||ξ|−E+Δ²/2E| is **spectral-edge-localized** (|w|∝Δ⁴/8|ξ|³ for |ξ|≫Δ), NOT "|ξ|≲Δ"-localized. Reframe any gap-localization check accordingly.

## Critical Entropy Lesson (S46)
- Shannon: S = -sum n_k ln(n_k). Max = ln(N) at uniform.
- Fermi-Dirac: S = -sum[n ln n + (1-n)ln(1-n)]. Max = N*ln(2) at n=1/2.
- The (1-n)ln(1-n) hole entropy is ESSENTIAL for fermions.
- NEVER mix Shannon numerator with FD denominator.

## Key Data Files
- S36: `computations/s36_sfull_tau_stabilization.npz`, `s36_mmax_authoritative.npz`
- S41: `computations/s41_spectral_refinement.npz`
- S43: `computations/s43_lifshitz_class.npz`, `s43_bcs_universality.npz`
- S52+: all in `computations/` with session prefix
