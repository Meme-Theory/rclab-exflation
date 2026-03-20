# Little-Red-Dots-JWST-Analyst Agent Memory

## Operating Principles
- **No probability estimation.** Sagan owns probabilities. This agent delivers structural truths, observational constraints, surviving solution space.
- **Constraint-map framing.** Every closed mechanism: Constraint / Implication / Surviving space.
- **Pre-registered evidence only.** Only new computational results against pre-registered gates change knowledge state.
- **Bookkeeping is reference, not narrative.** Closure counts are lookup tables, not rhetorical arguments.

## Paper Corpus
- Location: `researchers/Little-Red-Dots/` (66 papers + AGENTS.md + index.md)
- Papers 01-24: discovery, spectroscopy, demographics, X-ray/radio, seeds, dust, variability, clustering, hosts
- Papers 25-66: de Graaff BH Stars, Chandra deep, reviews, RUBIES, PBH, modified cosmology, e-scattering debate, SIDM/FDM models, local analogs, mass bias, unification, supermassive stars, environment, direct mass, Balmer break physics, MIRI SED, globular clusters, binary disappearance
- 7 duplicate arXiv pairs identified (15/57, 16/63, 17/58, 19/60, 20/64, 23/65, 24/62)
- Full structured index: `researchers/Little-Red-Dots/index.md` (rebuilt 2026-03-13 with 66 papers)

## Key Observational Constraints
| Constraint | Value | Source |
|:-----------|:------|:-------|
| LRD number density | ~10^{-5} to 10^{-4} cMpc^{-3}, z~4-8 | Papers 01, 04, 14 |
| BH masses (virial, naive) | 10^6-10^9 M_sun | Papers 01, 03, 05 |
| BH masses (e-scattering corrected) | 10^5-10^7 M_sun | Paper 15 (Rusakov) |
| X-ray weakness | 100-10,000x below L_X-L_Halpha | Paper 06 |
| Radio non-detections | ~95% undetected, log R ~ -4 to -6 | Paper 10 |
| ALMA dust upper limit | M_dust < 10^6 M_sun | Paper 19 |
| Variability | 97.5% non-variable (8/314) | Paper 18 |
| Companion fraction | 43% UV-bright neighbor <5 kpc (85% luminous) | Paper 16 |
| Host galaxies | 1/8 detected, 10-100x below local scaling | Paper 22 |
| Narrow-line fraction | ~20% photometric LRDs lack broad lines | Paper 20 |
| Dual LRDs | 3 pairs at 1-2 kpc, 300x excess over random | Paper 21 |
| BIC galaxy-only preferred | 75% (79% with MIRI) | Paper 23 |
| BHMF peak | M_BH ~ 10^7 M_sun at z~5 | Paper 14 |
| LRD duty cycle | 50-500 Myr, f_duty ~ 0.1-0.3 | Paper 14 |
| GN-z11 BH mass | 1.6 x 10^6 M_sun at z=10.6 | Paper 05 |
| LW flux at companions | J_21 ~ 10^{2.5}-10^5 | Paper 16 |

## Three Competing Interpretive Frameworks
1. **Super-Eddington BH in dense gas envelope** (Papers 11, 15, 24): M_BH ~ 10^6-10^7, e-scattering broadening, Balmer break from gas
2. **Accreting DCBH** (Papers 08, 16, 17): M_BH ~ 10^4-10^6, pristine halo collapse, UV companion LW flux
3. **Compact star-forming galaxies** (Paper 23): No AGN for 75% of LRDs, BIC prefers galaxy-only

## Phonon-Exflation Framework Connection (consolidated)
**Central result**: Framework degenerate with LCDM at all z < z_BCS ~ 10^{28}. LRDs CANNOT discriminate. "Too massive too early" tension is 1-2 sigma after Rusakov + Wang corrections. Framework inherits LCDM predictions identically.
- **g_1/g_2 = 0.684 at tau_frozen=0.19** (Session 32): 3.5% below measured 0.709. RGE running is dominant correction needed. **RGE gate OUTSTANDING since Session 29.**
- **w = -1 exactly**: omega_wall/H_0 ~ 10^{58}. Pre-registerable vs DESI DR2 (sigma ~ 0.04).
- **Cocoon analogy**: LRD e-scattering cocoon (Rusakov, Paper 15) parallels BCS condensate at domain walls. Both are feedback attractors hiding intrinsic physics.
- **Framework tests are particle physics, not cosmology**: Proton lifetime (tau_p ~ 10^{36} yr, Hyper-K ~10^{35}), gauge couplings (RGE gate), Weinberg angle.
- **RGE gate structure** (my contribution): Part A = ratio g_1/g_2 running M_KK to M_Z (zero-parameter). Part B = absolute normalization (one-parameter, M_KK). Existential test.
- **One-parameter web** (my contribution): M_KK anchors proton lifetime, T_RH, couplings, BAO r_s, CC sector sum. Over-constrained.
- **Derived vs adjacent**: Gauge couplings, Weinberg angle, proton lifetime = derived. Emergent G_eff, condensate vortices = adjacent (Volovik imports, not computed).
- **24-order gap**: k_transition = 9.4e23 h/Mpc structural for ALL KK compactifications at M_KK >> eV.
- Key files: `sessions/archive/session-29/session-29-observational-excursion.md`, `sessions/archive/session-32/session-32-little-red-dots-collab.md`, `sessions/archive/session-34/session-34-little-red-dots-collab.md`
- Workshop files: `sessions/archive/session-32/session-32-hawking-cosmic-web-workshop.md`, `session-32-connes-qa-workshop.md`, `session-32-sp-naz-workshop.md`

## Session 42 Key Findings (from my collab review)
- **C-FABRIC-42 PASS**: sigma/m = 5.7e-51 cm^2/g, lambda_fs = 3.1e-48 Mpc. CDM-like DM. NFW 1/r cusp DERIVED.
- **DM-PROFILE-42 PASS**: v_c rises 7.7% (10-30 kpc). 5 LCDM DM free params eliminated (identity, mass, sigma/m, production, coupling).
- **W-Z-42 (REDO #2) FAIL/GEOMETRIC LAMBDA**: w = -1 + O(10^{-29}). Effacement ratio |E_BCS|/S_fold ~ 10^{-6} + expansion dilution a^{-1} ~ 10^{-22}. DESI Year 3+ at > 5sigma would exclude framework.
- **TAU-DYN-REOPEN-42 FAIL**: Z(tau) irrelevant for homogeneous dynamics (nabla tau = 0). Shortfall 35,393x survives. TV delta_M/M = 2.6e-6 (suppressed by c_fabric^3).
- **HF-KK-42 FAIL**: All 992 KK modes massive (0.819-2.077 M_KK). No massless radiation channel. DR = 1.51 decades (sector). But eta = 3.4e-9 is 0.75 decades from observed.
- **CONST-FREEZE-42 PASS**: M_KK(gravity) = 7.4e16 GeV, M_KK(gauge) = 5.0e17 GeV. |Delta log10| = 0.83 < 1 OOM. GUT-scale range.
- **HOMOG-42 INTERMEDIATE**: Gravity route PASSES FIRAS (delta_tau/tau = 1.75e-6). Gauge route FAILS (3.11e-5). Constrains M_KK < 1.07e17 GeV. FAVORS gravity route.
- **NS-TILT-42 FAIL**: n_s = 0.746 (52 sigma from Planck). eta = 0.243 structural. KZ route survives.
- **Observational degeneracy**: CONFIRMED for 7th consecutive session (S34-S42).
- **Collab file**: `sessions/archive/session-42/session-42-little-red-dots-collab.md`
- **Key discriminants identified**: (1) SIDM clustering b~4.5 vs CDM b~2 (Paper 55 vs Paper 23), (2) DESI w(z) at > 5sigma, (3) Simons Observatory CMB lensing (Paper 30, 10.4sigma by 2028), (4) Resolved DM profiles in lensed LRD hosts (Paper 51 method extended)

## Session 40 Key Findings (from my collab review)
- **HESS-40 FAIL**: 27th closure. Jensen fold is 28D local minimum (22/22 positive, min H=+1572, margin 1.57e7). Spectral action cannot stabilize tau in ANY direction. Compound nucleus dissolution = unique surviving interpretation.
- **T-ACOUSTIC-40 PASS**: Acoustic Hawking temperature T_a/T_Gibbs = 0.993 (0.7% agreement, acoustic metric). T_acoustic/Delta_pair = 0.34 in nuclear backbending range.
- **CC-TRANSIT-40 PASS**: delta_Lambda/S_fold = 2.85e-6. Transit decoupled from CC by 5.5 orders of magnitude.
- **NOHAIR-40 FAIL**: T varies 64.6% with v_transit, S varies only 18%. Gap hierarchy (v_crit spans 4 decades) breaks no-hair on T. Distinguishing prediction from BH thermodynamics.
- **B2-INTEG-40 PASS**: B2 near-integrable (<r>=0.401 Poisson, g_T=0.087 localized). B2 weight corrected 93%->82%.
- **M-COLL-40 FAIL (CLASSICAL)**: M_ATDHFB = 1.695 (0.34x G_mod, NOT 50-170x). sigma_ZP = 0.026 << 0.09. Van Hove is velocity zero with LARGE gap, not gap closure.
- **Graviton channel identified**: m_graviton ~ 0.079 M_KK (from softest HESS-40 direction H=1572). Lighter than all 8 scalars. Kinematically open decay channel. Rate UNCOMPUTED.
- **Observational degeneracy**: CONFIRMED for 6th consecutive session (S34, S35, S36, S39, S40).
- **Collab file**: `sessions/archive/session-40/session-40-little-red-dots-collab.md`

## Session 36 Key Findings (from my collab review)
- **Needle hole**: S_full(tau) monotonically increasing. Gradient 376,000x > E_BCS. Transit 38,600x too fast. Mechanism chain BROKEN for linear SA.
- **Cascade hypothesis**: tau cascade {0.54, 0.34, 0.24, 0.190} proposed but saddle-to-redshift mapping UNCOMPUTED (CASCADE-DYN-37).
- **Observational degeneracy**: CONFIRMED for 5th consecutive session. LRDs cannot discriminate cascade from LCDM.
- **"Too massive too early" tension**: 1-2 sigma after Rusakov (Paper 15) + Wang (Paper 23). No observational pressure for non-LCDM.
- **Cascade predictions for LRDs**: qualitative only. No computation of perturbation spectrum, seed mass function, or n_LRD(z) from cascade D(z).
- **Outstanding gates**: CASCADE-DYN-37 (redshift assignment), CUTOFF-SA-37 (fold minimum with cutoff), CASCADE-NLRD-37 (n_LRD from cascade).
- **W6 resolved**: Lambda_species/M_KK = 2.06. Largest structural concern removed.

## Session 34 Key Findings (from my collab review)
- **TRAP-33b RETRACTED**: Frame-space V=0.287 was wrong; spinor V=0.057 is correct. Schur's lemma on B2 makes this basis-independent.
- **Van Hove rescue**: rho_smooth = 14.02/mode (2.6x over step), M_max = 1.445 with corrected impedance.
- **[iK_7, D_K] = 0**: SU(3) -> U(1)_7 exact. B2 = +/-1/4, B1 = 0, B3 = 0. Permanent.
- **mu = 0 forced**: Both canonical (PH symmetry) and grand canonical (Helmholtz convexity). Chemical potential route CLOSED.
- **Corridor**: M_max in [0.94, 1.43] depending on N_eff and impedance. Survives if N_eff > 5.5.
- **Cocoon/wall analogy strengthened**: Van Hove singularity = spectral cocoon. Medium IS the mechanism. Self-reinforcing structures.
- **Observational degeneracy**: CONFIRMED for 4th consecutive session. 24-order gap permanent. LRDs cannot discriminate.
- **Outstanding**: RGE gate (since S29), N_eff determination, BCS-dressed gauge coupling, impedance at smooth wall.

## Common Mathematical Errors in LRD Literature
- L_Edd: use 1.3e38*(M/M_sun) or 1.3e46*(M/10^8 M_sun), NOT 1.3e38*(M/10^8)
- BH growth: dM/dt = (1-epsilon)*M_dot (accretion adds, radiation removes). Paper 13 uses wrong sign.
- Cosmic age at z=8: LCDM = ~0.63 Gyr, EdS = ~0.35 Gyr
- Survey solid angle: 640 arcmin^2 ~ 1.5e-5 sr

## Meta-Analysis (2026-03-13, updated)
- See `meta_analysis_2026_03.md` for session-level findings
- 66 papers now on file (up from 24). All major 2025-2026 papers acquired.
- de Graaff 2025 (Paper 25): 116-source "Black Hole Stars", T_eff ~ 4900 K Hayashi-like
- E-scattering debate UNRESOLVED: Rusakov (Paper 15) vs MNRAS (Paper 31) vs RT effects (Paper 37)
- Direct dynamical mass (Paper 51): M_BH = 50 +/- 10 M M_sun at z=7.04, ~50% below virial
- Selection bias (Paper 38): corrected mass function consistent with LCDM (SUPPORTS framework)
- LCDM heavy seeds natural (Paper 40): AREPO confirms CDM viability (SUPPORTS framework)
- SIDM/FDM models (Papers 32-34, 55-56): ALL incompatible with phonon-exflation sigma/m ~ 10^{-51}
- CMB test (Paper 30): Simons Observatory by 2028, 10.4sigma discrimination power
- Observational degeneracy CONFIRMED: framework degenerate with LCDM at z<10^28

## Notes
- Paper 10 (Draca): author/journal unverifiable
- Paper 14 (Akins): first author = Hollis B., not Hannah
