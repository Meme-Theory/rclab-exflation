---
name: feasibility-fallback-dense-irrep-wall
description: Pre-registered PRE-REG-INC fallback firing on the dense-3^p Sym^p irrep-construction wall (branch-IV deep-truncation ρ_B; DR3-class L_max-stability gates); honest mechanical closure, NOT a FAIL
metadata:
  type: project
---

When a deep-truncation spectral-moment gate (e.g. branch-IV w0 DR3-class L_max-stability, S104 W1-3) needs DIRECT D_K sectors at p+q ≥ 13, the wall is `dirac_spectrum.irrep_symmetric_power(gens, p)` building a DENSE `3^p × 3^p` complex tensor-space matrix before projecting to the dim_sym=(p+1)(p+2)/2 subspace.

**Why:** the dense allocation blows up super-polynomially: Sym^9=6.2 GB (S103 measured ≈200.9 s), Sym^10=55.8 GB, Sym^11=502 GB, **Sym^13=40.7 TB, Sym^14=366 TB** — physically impossible. The (p,0)/(0,p) pure-symmetric extremes are the ONLY walls; mixed (p,q) with p,q>0 build FAST via the `irrep_via_casimir_projection` tensor-product path (S104: 12/14 level-13 mixed sectors in 87.8 s on RX 9070 XT GPU eigvalsh of i·D). There is NO recursive (p,0) builder avoiding 3^p in `dirac_spectrum.py` (grep-verified); the mixed Casimir path can't bootstrap (p,0) because parent (p−1,0)=Sym^{p−1} is itself infeasible.

**How to apply:**
- The plan PRE-REGISTERS the feasibility fallback (dual_prior.discriminator + mechanical-closure-discipline.md): close as PRE-REG-INC `value='PRE-REG-INC_blocked_by_irrep_construction_wall_Sym13_Sym14'`, deferred to next session — NOT a FAIL, never fake/extrapolate/substitute envelope values for direct spectra. The prior session's Friedrich-Bär envelope BOUND (INFO) stands as the best available bound.
- BUILD-FIRST discipline still pays off: launch the Phase-1 builder as a background process with INCREMENTAL per-sector persist so partial progress (the mixed sectors) survives and seeds the next session. Watch the numpy `savez_compressed` filename quirk: it APPENDS `.npz` to a path not ending in `.npz`, so a `tmp = OUT + ".tmp"` → `os.replace(tmp, OUT)` FileNotFoundErrors (savez wrote `tmp.npz`). Use `tmp_base = OUT[:-4]+"_tmp"`, replace `tmp_base+".npz"`.
- The MOMENT-evaluator sentinel is the trust anchor: reproduce ρ_B(L) on the s84 L≤12 cache bit-exact (S104: diff 0.0 for L=8,10,12 vs S103 record) BEFORE consuming any new sectors — proves the evaluator is the consumed S85 W0-7 one (no re-fit/convention drift).
- CAC offset cancels in the span: `spread_CAC = max_L ρ_B(L) − min_L ρ_B(L)` over {12,13,14} is offset-INDEPENDENT, so the w0_FW(−0.918) vs W0_B(−0.842454) anchor choice is immaterial to the verdict; both give the identical spread. CAC mandatory (regulator-convention-lockdown.md, RDC FORBIDDEN); offset DERIVED at runtime, never hardcoded.
- The genuine S105 CF is a Gelfand-Tsetlin / monomial-basis (p,0) builder that constructs the rep DIRECTLY in dim_sym space (105/120-dim) via closed-form ladder matrix elements, never forming 3^p — the wall is an implementation artifact, NOT a physics obstruction (the (p,0) sector is finite-dimensional and exists). Substrate framing preserved: computational wall ≠ explanatory-direction inversion.
