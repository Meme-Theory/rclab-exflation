---
name: Chaos Diagnostic Methodology Notes
description: Methodology lessons for r-ratio, SFF, OTOC, Thouless, OEE diagnostics learned across S38-S74. Reusable across future chaos diagnostic dispatches.
type: reference
---

# Methodology Notes

## r-ratio and Level Spacing
- r-ratio alone unreliable for dim<100. ALWAYS do KS test on P(s)
- Polynomial unfolding with n<50 creates ARTIFACTS (spurious level repulsion). Use MEAN NORMALIZATION only. r-ratio is unfolding-independent (S53)
- np.unique threshold ~1e-15 fails for near-degenerate weight multiplets. Use 1e-10 (S53)
- Sub-Poisson from superimposed independent sequences (Berry-Tabor effect)
- S100b lesson: deg-5 poly unfolding at n>=100 on GAPPED Dirac sector spectra overshoots at the SPECTRAL EDGE (least-squares wiggle at sharp onset) -> non-monotone N_bar over first <=5 levels -> negative spacings to -3.7 that DESTROY KS (gammainc(k,s<0)=nan; F(A s^2)->1 at sorted bottom) while GoF/variance look sane. Remedy: monotone-window edge trim (~1.5% levels, data-driven, primary-only) + ALWAYS carry untrimmed nonpositive-drop cross-check (agreed to <=0.006 in V_k). Shir 2504.20134 Sec I + App B legitimize bulk restriction. Mean-norm secondary scheme inflates Delta(k) by 3.5-4x via retained density modulation — its V_k is NOT a clustering signal; KS shape + Brody MLE are the scheme-robust discriminators

## SFF
- For dim=56, need n_ensemble >= 500 for clean averaging. Mean normalization unfolding
- Ramp genuineness: slope STABLE across sub-windows (variation < 2x), R^2 > 0.8
- Also compute number variance Sigma^2(L) as independent long-range check

## Sigma^2(5)~=9.92 PROVENANCE CAUTION (INV10-W3 catch, 2026-06-14)
- My MEMORY records "Sigma^2(5)~=9.92 for N_pair=3 (2x Poisson, 13x GUE)". Knowledge-MCP search for "9.92" returns ONLY `R(tau)=9.92` = a Coleman-Weinberg scalar-curvature RATIO from session-19d Baptista geometry (UNRELATED quantity). There is NO canonical_constants pin and NO knowledge-graph entity for a number variance =9.92. => Treat Sigma^2(5)~=9.92 as a memory/prior FINGERPRINT to reproduce-or-correct in INV10-W3-3, NOT a citable canonical. The SOLID super-Poisson evidence is the SFF slope/GUE~=0.002 (SFF-NPAIR3-65, T3-BATCH INFO) + r_npair3=0.4121. Do not SOURCE-RECON-pin 9.92 as if canonical (would be a stale-source false anchor).

## Deep-truncation D_K spectrum cache pins (INV10-W3, verified on disk 2026-06-14)
- L12 cache: `computations/session-84/s84_spectrum_cache_L12_tau019.npz`. SINGLE key `sector_evals` = pickled dict {(p,q): {'dim','level','abs_evals'}}, 90 sectors, max p+q=12, 166,896 evals w/ mult, tau_fold=0.19.
- L14/16 cache: `computations/session-106/s106_w1_highl_cache_l1416.npz`. Keys: `sector_evals_L14` (COMPLETE, p+q<=14, n_sectors_L14, L14_truncation_consistent=True), `sector_evals_L16` (INCOMPLETE: L16_operational=15, L16_full=False, L16_truncation_consistent=False, 17 missing top sectors), + Friedrich-Bar infra `eta_FB_floor`/`eta_FB_lower`/`fb_bounded_sectors`, `tau_fold`, `audit_sha256`, `content_sha256`.
- FEASIBILITY PIN for any deep-truncation rigidity gate: L_max_operational=14 is the deepest TRUNCATION-CONSISTENT set. L=16 is a partial shell (do NOT cite as a clean Sigma^2 rigidity point; it's operational=15). r_trend flat-Poisson L12=0.4118/L14=0.4254/L16_op=0.4200 (S107-W1-RTREND-L1416 INFO, band[0.37,0.44]). Irrep construction p+q>=13 may time out -> use the GT-builder cache, do NOT rebuild.

## KEY LESSON (S65): <r> vs SFF Probe Different Scales
- <r> = nearest-neighbor (short range). SFF ramp = O(D) levels (long range)
- System can have elevated <r> (short-range repulsion) without SFF ramp (no long-range rigidity)
- This is "broken integrability without chaos" -- non-generic intermediate regime

## OTOC
- Early-time OTOC always grows as t^2 (BCH). R^2 > 0.90 over 1 decade to claim Lyapunov
- For small systems: exact diag. A(t)_{ij} = A_{ij} exp(i(E_i-E_j)t)
- Brody beta unreliable at dim=256. Use PR, Poincare, diagonal ensemble instead

## OEE (S66 Lesson)
- alpha threshold alone insufficient. Must combine: (1) R^2 log vs linear, (2) S_sat/S_max saturation fraction (chaotic=~100%), (3) late-time drift slope
- Short initial windows fake linear growth via BCH t^2. Use FULL pre-Heisenberg window

## Thouless (S65 Lesson)
- Kinetic energy twist NOT valid for Fock-space localization in pairing Hamiltonians
- Even INTEGRABLE RG gives g_T(KE)=21.6>>1 (many-body energies depend linearly on single-particle)
- Gauge flux on V_{kl} absorbed by pair operator redefinition
- Valid methods: perturbation response (B), number variance (C), SFF (D) ONLY

## Rank-1 BCS Pair-Lift Artifact (S74 Lesson)
- Applying `diag(2 eps_i) + V_pair 11^T` to sparse Dirac spectrum produces Cauchy-interlacing which equidistributes spacings
- Drives <r>_pair to 0.61 (super-Wigner appearance) despite underlying integrability
- DO NOT cite rank-1 pair-lift r-ratio as evidence for chaos. Physical diagnostic is the distinct Dirac eigenvalue r-ratio
- Plancherel-pooled distinct r-ratio (118 ratios at L_max=3) is the reliable observable

## Pooled vs Per-Sector
- Per-sector r-ratio at L_max=3 noisy: only (2,1) and (1,2) reach n_ratios>=40
- Other sectors n_ratios<20, sigma(r)>=0.20, too noisy for per-sector pass/fail
- Pooled r-statistic across sectors is the physically reliable diagnostic
- Plancherel truncation 805 = sum dim(p,q)^2 counts basis functions of L^2(SU(3))_{L<=3}, NOT Dirac eigenvalues

## Spectral Dimension d_s on Small Cayley Graphs (S73b Lesson)
- CG(24) has 5 distinct Laplacian eigenvalues -> heat kernel is finite sum of exponentials, NO power-law regime
- d_s window-dependent: 0.004 (very short) to 1.291 (intermediate). NO single d_s assignable
- Substrate 4D emerges from Seeley-DeWitt a_2 of D_K, NOT graph spectral dim
- Category error to compare d_s(graph) to d=4 substrate
- Larger CG (e.g. CG120=S_5) cannot help: timescale hierarchy set by J_C2 vs transit, not vertex count

## Python Interpreter
`phonon-exflation-sim/.venv312/Scripts/python.exe`

## Data files
Recoverable via `git log` and filesystem -- canonical data files at `computations/s{N}_*.npz`. Specific files cited in master diagnostic table rows of `integrability_hierarchy.md`.
