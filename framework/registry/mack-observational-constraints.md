# Mack Observational Constraints (Consolidated Reference Snapshot)

> **Provenance**: AMRI-promoted from `.claude/agent-memory/mack-cosmic-bridge/reference_key-constraints.md` on 2026-04-28 during S87 W0 `/shortterm` collapse pass. Cross-agent overlap test fired with `falsifier-master-inventory.md`, `branch-iv-canonical.md`, `pre-registered-observations.md`; input-pin test fired via `sessions/session-plan/archive/session-85-plan-w4.md:357,826`, `session-86-plan-w15.md:240`, `session-87-plan-w9a.md:848`, `archive/session-68-context.md:158` per AMRI Tests 1 + 3 (`.claude/rules/agent-standards.md` §AMRI).
>
> **Sole writer**: mack-cosmic-bridge per `.claude/agent-memory/mack-cosmic-bridge/MEMORY.md` (orchestrator-direct-write granted in this AMRI landing pass; subsequent edits by mack-cosmic-bridge only).

## Authority Hierarchy (READ THIS FIRST)

This file is a **consolidated observational-reference snapshot** carried forward from mack-cosmic-bridge's pre-AMRI agent memory. For canonical values, read the authoritative sister registries; this file is the ergonomic single-page reference, not the source of truth:

| Topic | Canonical source | This file's role |
|:------|:-----------------|:-----------------|
| Pre-registered framework predictions | `sessions/framework/registry/pre-registered-observations.md` | snapshot copy with session provenance |
| Falsifier observables + detector roster | `sessions/framework/registry/falsifier-master-inventory.md` | observational-anchor side only |
| Branch-iv (substrate compaction) canonicals | `sessions/framework/registry/branch-iv-canonical.md` | numerical-pin cross-cite |
| Canonical numerical pins | `computations/canonical_constants.py` | live values; this file may lag |
| Live-watch live envelopes | `sessions/framework/registry/falsifier-watchlist.md` | passive copy of envelopes |
| Detector readiness 9-cell | `sessions/framework/registry/detector-readiness-9-cell.md` | passive copy of detector states |

If any value here disagrees with the canonical sister registry, the sister wins. Conflict reports go to mack-cosmic-bridge for adjudication.

## Retraction discipline

Strikethrough (`~~text~~`) entries are RETRACTED with their retraction provenance noted on the same line. Do not cite retracted values; they remain in this file ONLY for audit-trail reproducibility of pre-retraction reasoning. The S60 H_0 = 68.8 km/s/Mpc retraction is the canonical example.

---

## Planck 2018 (Paper 29)

- H_0 = 67.74 +/- 0.46 km/s/Mpc
- Omega_m = 0.3089 +/- 0.0062
- Omega_c h^2 = 0.1186 +/- 0.0020 (CDM)
- n_s = 0.9655 +/- 0.0062
- sigma_8 = 0.829 +/- 0.014
- r < 0.11 (tensor-to-scalar)
- sum(m_nu) < 0.17 eV
- N_eff = 3.15 +/- 0.23
- w = -1 consistent

## DESI DR1 (Paper 30)

- Omega_m = 0.299 +/- 0.014
- w (constant) = -0.98 +/- 0.05
- Dynamical DE: w_0 = -0.72 +/- 0.08, w_a = -0.41 +/- 0.31 (2.6 sigma hint)
- H_0 = 67.9 +/- 1.1 km/s/Mpc
- Omega_K = -0.003 +/- 0.006 (flat)

## DESI DR2 (cited in framework docs)

- w_0 = -0.752 +/- 0.057, w_a = -0.73 +/- 0.25

## DES-Dovekie 2026 (with DR2 + Planck/ACT/SPT)

- **Source**: Popovic et al. (DES Collaboration), arXiv:2511.07517v3 (27 Mar 2026; original posting Nov 2025). DES SN Program 5-year sample recalibrated and renamed **DES-Dovekie** — 1,623 likely Type-Ia DES SNe + 197 low-z SNe = 1,820 total. Joint Flat w0waCDM constraint with DESI DR2 BAO + Planck 2018 + ACT-DR6 + SPT-3G CMB.
- **Headline methodological changes** (DES-SN5YR → DES-Dovekie): photometric cross-calibration upgrade ("Fragilistic" → "Dovekie") using new DA white dwarf observations (CALSPEC update); SALT3 light-curve model retrained (`SALT3.DES5YR` → `SALT3.DOV`); F99 host-galaxy color law approximate → exact; posterior sampler MCMC → Nautilus (nested sampling); BAO SDSS → DESI DR2; CMB Planck-only → Planck + ACT + SPT.
- **Flat ΛCDM** (DES-Dovekie alone): Ωm = 0.330 ± 0.015 (lowers Ωm by 0.022 vs DES-SN5YR's ~0.352).
- **Flat w0waCDM** (DES-Dovekie + Planck + ACT + SPT + DESI DR2): **w_0 = −0.803 ± 0.054**, **w_a = −0.72 ± 0.21**.
- **Significance against ΛCDM**: 3.2σ (frequentist Wilks; reduced from DES-SN5YR's 4.2σ); Bayesian model odds ~5:1 in favor of w0waCDM (paper characterizes as "weak preference").
- **Nuisance parameters** (data vs SNANA simulations): α = 0.169 ± 0.003 (sim 0.140); β = 3.14 ± 0.03 (sim 2.80); γ = 0.033 ± 0.008 (sim 0.0); Hubble residual RMS = 0.169 mag.
- **NOT a new DESI release**: this is a DES-SN reanalysis joint with DESI DR2 BAO + Planck/ACT/SPT, NOT a DESI DR3 release. The R_842 binding event is NOT triggered by this paper (binding instrument is DESI DR3, not DES-SN reanalysis on DR2 BAO). DR3 release window opens 2026-04-23.
- **Framework σ-distances** (post-Dovekie, mack-arxiv `s88-mack-arxiv-2511-07517-desi-review.md` §3): canonical w0_FW = -0.918 → 2.130σ (was 2.91σ vs DR2-DESY5; reduction = 0.78σ); branch-(iv) w0_FW_R842 = -0.842454 → 0.731σ (was 1.59σ; reduction = 0.86σ); w_a (four-fold lock = 0) → 3.429σ (was 2.92σ; ADVANCED by +0.51σ from σ-tightening 0.25→0.21 at essentially unchanged central value -0.73→-0.72).
- **Source SHA**: mack-arxiv report `9e2225fc756a359f9e12a21a1a2cb154c1d69232e0531ab51aed606d5f61c69a`.

## Framework Pre-Registered (S49 P-8)

- w_0 = -0.509 +/- 0.079, w_a = -0.009 +/- 0.02

## Key Framework Numbers (S66, updated from S65)

- Omega_DM h^2 = 0.120 at canonical (Volovik partition), bracket [0.013, 0.143] (narrowed from [0.017, 0.188])
- Omega_Lambda = 0.685 at canonical
- f_DM = 0.947 (S65, graph-gapped Goldstones, FDMPW-65 PASS). Omega_DM h^2 = 0.400 (3.3x above Planck 0.1186). Required f_coll = 0.266
- w_0 = -0.918 (Volovik Interp A, combined Josephson+GGE). 2.9-sigma from DESI DR2
- w_0 = -0.408 (Interp B, GGE only). EXCLUDED at 6.0-sigma from DESI DR2
- w_a < 0.03 (both interps). In tension with DESI DR2 w_a = -0.73
- Lambda_eff / Lambda_obs = 1.93 x 10^{114} (unchanged; Volovik saves 3 OOM via cancellation)
- T_init = 8.32 x 10^{15} GeV
- n_s = 0.9590 (S65 BCS+one-loop, BCS-NS-FULL-65 INFO). BCS shift +0.0031, one-loop -0.0010, cross-term +0.0002. Planck: 0.9649 +/- 0.0042 (1.40-sigma). Two-loop negligible (6e-8). Structurally frozen.
- r = 0.033 (S64 TENSOR-BURST-64 + TENSOR-SCALAR-64, two independent PASS). H2 theorem kills 1st-order. Second-order: 16*eps^2*c_BLV*(1+2|beta|^2)^2. BICEP/Keck r < 0.036.
- n_T = +0.468 (S65 NT-BLUE-65 PASS). BLUE tensor tilt at transit scale. 113x slow-roll. r+8*n_T=3.77 vs 0.
- n_T(k_CMB) = -3.02e-3 (S66 TENSOR-TRANSFER-66 FAIL). Blue tilt LOCALIZED at k_transit (54 decades above CMB). CMB tilt is standard slow-roll -2*eps. r(CMB) = 0.024 (BICEP/Keck PASS).
- Joint (n_s, r) tension: 2.15-sigma (Planck+BK18), 1.56-sigma (BK15). 2D > 1D by 0.74-sig due to rho(n_s,r)=+0.25 (S66 NS-R-JOINT-66 INFO).
- alpha_s = -0.038 at L_max=4 (S66 RUNNING-NS-66 FAIL, 5.0-sigma). Casimir smoothing ineffective (0.01% reduction). Richardson extrap to L->inf: -0.037 (4.9-sig). Intrinsic to spectral geometry.
- A_s gap = 3.15 OOM (S66 AMPLITUDE-NORM-66 FAIL marginal, Route A). Route B direct (no PW): 1.47 OOM (INFO). PW projection is dominant mechanism.
- Scheme dependence: eps_H SIGN FLIP between sqrt (red tilt, +0.022) and zeta a_4 (blue tilt, -0.045). n_s range across 3 cutoffs = 0.164. n_s prediction CONDITIONAL on f(x) = sqrt(x). (S66 CUTOFF-NS-66 FAIL, ZETA-SA-66 INFO)
- CC: Volovik q-theory relaxation ONLY surviving route. rho_vac(today)/rho_obs = 1.032 via rho~H^2 (S66 DILUTION-CC-66 PASS Scenario B). Discrete self-tuning FAIL (QTHEORY-NPAIR-66). Entropy cutoff FAIL (Chebyshev theorem). B/F splitting = 0 exactly (PERMANENT, both bare and BCS).
- Leggett-only DM: Omega_DM h^2 = 0.120 (0.6% from Planck). z_eq = 3425 (0.88-sig, S66 Z-EQ-CHECK-66 PASS). Full DM (0.400) excluded at 260-sigma. BA phonons must decay before z~3400.
- Leggett quasiparticle quality: Q = 18.6, Z = 0.972, Lorentzian lineshape (S66 LEGGETT-SPECTRAL-66 PASS).
- w_a substrate compaction: CLOSED for DESI comparison. Actual EoS w_a = +1.121 (wrong sign). S59 w_a=-0.645 was distance-fit artifact (S66 WA-REASSESS-66 INFO). Pure FW (w_0=-0.918, w_a=0) remains best.
- A_s gap = 3.16 OOM (S64, reduced from 8.01). Chain: BCS occupation -1.12, PW selection -3.50 (structural), gap tunneling -0.23. Trans-Planckian universality PASS (factor 1.33 across cutoffs).
- N_e = 3.73e-3 (physical transit, S64 SELF-CONSISTENT-NE-64). 5 methods agree [4.5e-4, 7.9e-3]. M-S inapplicable (permanent): N_e=7.75 total, eta_H=0.96, n_s(MS)=-0.17.
- c_BLV = 0.485 (BLV fabric sound speed, S64). Four-speed hierarchy: c_mod=1.0 > c_BLV=0.485 > c_BA=0.399 > c_L=0.025. All causal.
- Mach = 13.8 (supersonic, corrected S64 W3-E). W1-E subsonic claim RETRACTED.
- c_fabric/c_Gold = 229.5 (2.72 acoustic e-folds)
- P_exc = 0.081 (2-cell, physical rate)
- Gap scaling alpha = -0.652 (CG(24), revised from -1.84 chain)
- epsilon_direct = 0.00143 +/- 39% (V_bare, revised from S49 0.00248)
- M_Pl_eff = 4.79 x 10^19 GeV (3.92x unreduced M_Pl; if spinor-corrected H_0 = 65.4 km/s/Mpc)
- m_B2(fold) = 0.723 M_KK (30% below round-SU(3) value 1.026)
- NROY = 0.18% (Variant B), 0.00% (Variant A)

## Hidden DM Constraint (Paper 16)

- z_tr > 6.2 x 10^7 (relativistic-to-NR transition)
- Framework: z_tr = 6.75 x 10^29 (PASS, 22 OOM margin)

## DM Self-Interaction (Paper 10 + cluster constraints)

- sigma/m < 1.25 cm^2/g (Bullet Cluster)
- Framework predicts sigma/m = 0 exactly (N_pair=1)

## Transfer Function / LSS (S58 W3-14, Papers 15-16)

- Lyman-alpha bound: m_WDM > 5.3 keV (Irsic et al. 2017)
- Framework: m_WDM equiv = 10^{20.4} keV (PASS, 19 OOM margin)
- T(k) = 1.0000 at all observable scales (k = 1, 10, 100, 1000 h/Mpc)
- k_cut = 4.3e23 h/Mpc, lambda_fs = 1.5e-23 Mpc/h
- Structural result: any m_DM > 10 keV passes; framework gives m_DM ~ M_KK ~ 10^17 GeV
- Phononic DM is effectively CDM for all LSS purposes
- This does NOT address the f_DM problem (framework gives 0.209 vs observed 0.844)

## Friedmann Equation (S58 W3-16)

- H_0_SA = 3.61 km/s/Mpc (18.7x below observed)
- If spinor normalization corrected (divide a_2 by 16): H_0 = 65.4 km/s/Mpc (3% of obs)
- CC from SA: rho_Lambda = -3.32e71 GeV^4 (10^118 problem, unchanged)
- Two-level architecture: spectral->gravity (structural), Volovik->cosmology (contingent)

## CC Near-Cancellation (S58 W0-2)

- R_cancel = [0.002, 0.007] across transit [0.10, 0.30]: STRUCTURAL
- Saves 3 OOM (CC gap = 111, not 114)
- Lambda_eff always positive (accelerating)
- w(tau) in [-0.45, -0.41], always < -1/3

## DESI DR3 Projections (S59, WA-ERROR-PROP-59)

- Projected sigma(w_0) = 0.040, sigma(w_a) = 0.177 (sqrt(2) improvement from DR2)
- w_a = 0 excluded at 4.13-sigma (1D), framework at 4.29-sigma (2D)
- 95% contour overlap (FW & DR3) = 0.00%
- P(DR3 excludes w_a=0 at 3-sigma) = 87%
- Critical: w_a < -0.530 for 3-sigma, w_a < -0.884 for 5-sigma exclusion of framework
- LCDM at 6.50-sigma projected tension with DR3

## Observational Discriminants: Framework vs LCDM (S59, OBS-DISCRIMINANT-59)

- BAO D_V(z): best discriminant. Euclid 5.71-sigma (6 bins), DESI 3.19-sigma
- f*sigma_8(z): 3.9-4.1% difference at z=0.3-0.7 (GROWTH-FACTOR-59 exact ODE). Max 1.0-sigma per-bin at current DESI. Systematic sign (negative) across all z
- Direct w_0: 0.082 from -1.0. Planck constant-w 2.73-sigma
- ISW: 0.82% power difference, cosmic-variance limited, < 0.03-sigma. NOT viable
- l=721 feature: no physical derivation, < 1-sigma even if existed. NOT viable
- All discriminants correlated (driven by single parameter w_0 - (-1) = 0.082)
- CONTEXT: meaningless if DESI DR3 confirms w_a != 0 (both FW and LCDM excluded)

## S60 Updates to Framework Numbers

- H_0 = 68.8 km/s/Mpc **RETRACTED** (PW-H0-CONV-60: S44 missing (1,2) irrep, PW sum diverges L^6.2; N(L=3)=4.859 not 3.920)
- H_0 prediction currently UNDEFINED pending proper heat kernel a_2 computation
- N_a4/N_a2 = 1.823 (82% non-cancellation; 35% Higgs mass systematic)
- Fold SA Hessian: (0+, 3-) — maximum in all 3 directions; a_4 Hessian all-positive; alpha_crit = 55
- GGE permanence: CONDITIONAL (RG integrals broken delta_k=0.33 in fabric, 99.8% Josephson)
- PENROSE-ACCESS-59 downgraded: P(alpha > alpha_crit) = 0.574 (Bayesian)
- CC closures: 33+ total (S60 added 6: unimodular, staircase, inter-sector, Bekenstein, entanglement, Penrose SR)
- Leptogenesis: CLOSED (W_J forces M_R real, epsilon_1 = 0 exact)
- Leggett DM: CLOSED (overclosure 26.4 OOM, tau_L = 3.6e-34 s)

## S59 Updates to Framework Numbers (prior to S60 corrections)

- ~~H_0 = 68.8 km/s/Mpc (zero free params, SPINOR-NORM-59 PASS, N=3.920)~~ RETRACTED S60
- f_DM(z=0) = 1.000 (f_DM-DEPLETION-59 PASS, BA + BCS fully depleted)
- f_DM(B) = 0.365 at transit (DM-RECALC-59 INFO, corrected epsilon)
- Delta_N_eff = 0.027 (NEFF-BA-59 INFO, 1 Goldstone, CMB-S4 testable)
- CC: non-equilibrium path CLOSED (ZUBAREV + JOSEPHSON-PHASE). Redirect to q-theory
- R_cancel: saturates at 1.000 for PW levels >= 1 (PW-CC-59 INFO)
- Stochastic GW: f_peak = 1.86e7 Hz (STOCHASTIC-GW-59 FAIL, inaccessible)
- sigma_8(fw) = 0.793 (from GROWTH-FACTOR-59, vs LCDM 0.811)

## DESI-DV-64 Model-Independent Distance Comparison (S64)

- D_V(z)/r_d computed at 7 DESI bins for 4 models, bypassing CPL parameterization
- Framework-LCDM: 3.77-sigma (DR2), 5.33-sigma (DR3 projected)
- Framework distances 1.1-1.7% shorter than LCDM (correct DESI direction, monotonic)
- Pattern correlation with DESI Quintom B: FW r=-0.036, Compaction r=+0.817
- Framework CLOSER to DESI best-fit than LCDM is: FW-DESI = 1.50-sigma, LCDM-DESI = 4.66-sigma
- Compaction (w_a=-0.645) opposes DESI at z>0.5 (makes distances LONGER, DESI wants SHORTER)
- DR3 decision: w_a < -0.530 => FW excluded; D_V(z=0.934)/r_d < 19.364 => FW excluded
- Key structural constraint: framework's monotonic deviation cannot reproduce Quintom B z-crossing

## Key Open Questions (Post-S59)

- Peter-Weyl convergence of H_0: does N approach 4.00 at max(p+q)=4,5?
- Timescape screening: can delta_G/G and delta_alpha/alpha be decoupled from D_H correction?
- What fixes N_pair=1? CC as charge-quantization problem
- Leggett mode gravitational decay lifetime: Gamma ~ m_L^3/M_Pl^2?
- Majorana sector of D_F: complex M_R entries for leptogenesis?
- DESI DR3 adjudication: pre-register w_a forecast before data


## S89-Close Observational Constraints Snapshot (added 2026-05-13 via CF-32 S90 W2)

> **Provenance**: appended via CF-32 S90 W2 by mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` (AMRI-PROMOTED 2026-04-28). DEPENDENCY: CF-29 PASS landed at S90 W2-12 (audit_sha256=92c09dc0a053354b…); this section cross-links the post-CF-29 falsifier-master-inventory Row #3 state.

### Substrate-canonical S89 PASS results

| Quantity | Substrate-canonical value | Provenance | Cross-link |
|:---------|:--------------------------|:-----------|:-----------|
| `n_s_FW_exact` | `Fraction(9561, 10000) = 0.9561` (bit-exact Route-B identity at substrate-distance-1 Mellin pole s=3) | S88 ledger B.1 LANDED | `canonical_constants.py:1681` |
| `α_s_canonical` | `-8587279/100000000 ≈ -0.085 872 79` (Sage-QQ bit-exact = `n_s_FW_exact² − 1`) | S89 W7a Sage-QQ triple-verified (audit_sha256=`01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17`) | `canonical_constants.py` (CF-27 + CF-28 PROVENANCE blocks per S90 W2-10/W2-11); `falsifier-master-inventory.md` Row #3 (post-CF-29 update) |
| joint χ²_diag (n_s, α_s) vs Planck 2018 | `43.09` (Class-8.5 PRU 2D verdict-line value-field calibration instance #1) | S89 W4-4 hypersurface lab-discrimination (audit_sha256=`e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89`) | `falsifier-master-inventory.md` Row #3.audit-CF-29 + `canonical_constants.py` |

### Observational anchors (S89 close)

| Anchor | Value | Source |
|:-------|:------|:-------|
| Planck 2018 `n_s` | `0.9649 ± 0.0042` | `canonical_constants.py` |
| Planck 2018 `α_s` | `-0.0045 ± 0.0067` | `canonical_constants.py` |
| ACT DR4 + Planck (Aiola 2020) `α_s` | `+0.0023 ± 0.0063` | `canonical_constants.py`; S85 W1b-8 carry-forward pin |

### Discriminator gap analysis

| Substrate-canonical | Observational | Gap (σ) | Falsifier status |
|:--------------------|:--------------|:--------|:-----------------|
| `n_s_FW_exact = 0.9561` | Planck 2018 `n_s = 0.9649 ± 0.0042` | `(0.9649 - 0.9561) / 0.0042 = 2.10σ` | currently 2σ-region; CMB-S4 σ_n_s target ≈ 1.8e-3 ⇒ ≥ 4σ at CMB-S4 horizon |
| `α_s_canonical = -0.085 87` | Planck 2018 `α_s = -0.0045 ± 0.0067` | `12.15σ` | **FIRST multi-σ falsifier within near-term observational reach** (per `falsifier-master-inventory.md` Row #3 CF-29 update) |
| `α_s_canonical = -0.085 87` | ACT DR4 + Planck `α_s = +0.0023 ± 0.0063` | `13.99σ` | within CMB-S4 + CMB-HD horizon (≥ 5σ + ≥ 30σ respectively) |

### Substitution chains (Sage-QQ exact in Q)

**n_s substitution chain** (Route-B identity at substrate-distance-1 Mellin pole s=3):
- Definition: `n_s_FW_exact := Fraction(9561, 10000)` per S88 ledger B.1
- Decimal: `0.9561`
- Gap_σ vs Planck 2018: `|0.9649 − 0.9561| / 0.0042 = 0.0088 / 0.0042 ≈ 2.10σ`
- Direction: substrate prediction MORE NEGATIVE deviation from Planck-2018; CMB-S4 (σ_n_s ≈ 1.8e-3) will tighten by ~2.3× → expected ≥ 4σ at S4 horizon.

**α_s substitution chain** (Route-B identity `α_s = n_s² − 1` at s=3):
- Step 1: `n_s_FW_exact² = Fraction(9561², 10000²) = Fraction(91413721, 100000000)`
- Step 2: `α_s_canonical = n_s_FW_exact² − 1 = Fraction(91413721 − 100000000, 100000000) = Fraction(−8587279, 100000000)` (Sage-QQ exact in Q; S89 W7a triple-verified at audit `01c1ac83569dc92f…`)
- Step 3: Decimal: `-0.085 872 79`
- Step 4: Gap_σ vs Planck 2018: `|(-0.085872) − (-0.0045)| / 0.0067 = 0.081372 / 0.0067 ≈ 12.15σ`
- Step 5: Gap_σ vs Aiola 2020 ACT DR4 + Planck: `|(-0.085872) − (+0.0023)| / 0.0063 = 0.088172 / 0.0063 ≈ 13.99σ`
- Direction: substrate prediction is SIGN-OPPOSITE both observational anchors AND multi-σ outside both bands ⇒ FIRST multi-σ falsifier within near-term observational reach.

### Cross-references

- `computations/_shared/canonical_constants.py`: `n_s_FW_exact` (Fraction pin per S88 B.1) + `α_s_canonical` (Sage-QQ bit-exact); CF-27 + CF-28 PROVENANCE blocks (S90 W2-10/W2-11) carry the Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY chain for the related observable `R_universal_HP1_strict_F4` (derivative form of `eps_H_HP1_norm` PRIMARY).
- `sessions/framework/registry/falsifier-master-inventory.md` Row #3: α_s_canonical "first multi-σ falsifier" tag (post-CF-29 S90 W2-12 update; audit_sha256=`92c09dc0a053354b…`).
- `sessions/framework/registry/falsifier-master-inventory.md` Row #3.audit-CF-29: full 64-char audit_sha256 pins for S89 W7a + W4-4 (verbatim cross-link source).
- `joint-theorem-promotion.md` Stage-2 PASS-AND patterns: S89 W4-4 IS the FIRST Class-8.5 PRU 2D verdict-line value-field calibration instance per `epistemic-discipline.md §"Pre-Registration Completeness"`.

### Cosmological detector horizon (S89-current consensus)

- **2026 (BICEP/Keck Array)**: `r` (tensor-to-scalar); BK Array σ_r ≈ 0.003.
- **2026-04-23 (DESI DR3)**: `w_0`, `w_a` (DR3 window opens); R_842 rectangle binding event.
- **2027-2028 (DESI DR4)**: σ(w_a) ~ 0.12.
- **2030 (LiteBIRD launch / CMB-S4 commissioning)**: `n_T` B-mode (LiteBIRD STRUCTURAL-FLOOR per S85 W1a); `α_s` discrimination at CMB-S4 (σ_α_s ≈ 2.3e-3 ⇒ ≥ 5σ on α_s_canonical); `f_NL` (CMB-S4); β_s (CMB-S4).
- **2034+ (LISA)**: Ω_GW at f_pivot = 3 mHz (FLAGSHIP-DECISIVE per S85 W1a-7 SNR=1.68e13).
- **2035 (CMB-HD)**: σ_α_s ≈ 1.1e-3 ⇒ ≥ 30σ on α_s_canonical; CMB-HD tightens by 2× over CMB-S4.

### Substrate framing (mandatory per `phononic-framing.md §"IS Space, Not IN Space"`)

The substrate IS the spectral triple `(A_K, H_K, D_K(τ))` at τ_fold = 0.19; n_s_FW_exact + α_s_canonical ARE substrate-IS spectrum-only-functional images at the substrate-distance-1 Mellin pole s=3 (Cell I of §VII.U.2 4-corner classification, algebra-INVARIANT). The Planck 2018 + ACT DR4 + Aiola-2020 observational anchors are laboratory-IN measurements on the FRW background CMB. Direction substrate → emergent: substrate-canonical predictions ARE prior; observational gap_σ values follow.

The Route-B identity `α_s = n_s² − 1` at substrate-distance-1 Mellin pole s=3 IS the substrate-IS algebraic identity in Q (Sage-QQ bit-exact). The 12-14σ gap between substrate-canonical α_s and observational anchors is structurally INFORMATIVE: it constrains either (i) n_s_FW=0.9561 substrate prediction (already 2σ below Planck), (ii) Route-B identity application (which connects n_s and α_s via s=3), or (iii) substrate-physics interpretation of α_s as substrate-distance-1 pole running. Per `feedback_reporting-framing.md` discipline: this is INFORMATIVE constraint-map data, NOT meaningless FAIL.

---

## CF-35 — 3He-B Aalto LTL First-Contact Liaison (Pillar V; Q4 2026 deadline)

> **Provenance**: S91 W9-2 (CF-35; gate ID `S91-CF-35-3HE-B-AALTO-LTL-FIRST-CONTACT-LIAISON`); mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`. Pre-registration source: `sessions/session-plan/session-91-plan-w9.md §W9-2` (lines 232-402). Substrate canonical pin source: S86 W-5 R2-B Convergence #3 + R2-A EMERGENCE #2 (`W-5 CANONICAL-5`); `computations/_shared/canonical_constants.py:276` `substrate_cocycle_ratio_67_88 = 7.324992`. Forward-pinning: PASS at S91 W9 closure = liaison block landed; NO direct measurement at S91 (long-lead-time observational anchor; 2028-2029 feasibility window).

This block is the framework's FIRST observational liaison pre-registration for a Pillar V superfluid-laboratory falsifier. It is STRUCTURALLY ORTHOGONAL to the Pillar I CMB-S4 / CMB-HD α_s cosmological falsifier (the α_s_canonical 12-14σ multi-σ discriminator above) per `phononic-framing.md §"IS Space, Not IN Space"` Pillar partition.

### Substrate framing (mandatory per `phononic-framing.md §"IS Space, Not IN Space"`)

The substrate IS the inheritance morphism `ι: A_K → A_BdG = M_2(ℂ)` between the framework's NCG-axiomatic spectral triple `(A_K, H_K, D_K(τ))` and the laboratory-IN 3He-B BdG sub-algebra image. The kernel `ker(ι_*)` IS the substrate's degrees-of-freedom that DO NOT inherit; the cocycle-ratio `‖[φ_67]‖ / ‖[φ_88]‖ = 114453/15625` IS the substrate's intrinsic cohomology-asymmetry ratio at the (chiral-pair, Cartan-hypercharge) generator pair. The Aalto LTL Lancaster MCT-3 measurement of `lab(F_1) / lab(F_2)` (Caroli-Matricon ladder asymmetry) IS the laboratory image of this substrate-IS ratio under the inheritance morphism's image-on-spectrum. Direction:

```
Substrate (Pillar IV NCG-axiomatic) IS ‖[φ_67]‖ / ‖[φ_88]‖
   → Bridge map (Connes-Karoubi pairing; inheritance morphism ι)
   → Laboratory (Pillar V 3He-B BdG) IN lab(F_1) / lab(F_2) Caroli-Matricon ladder asymmetry
```

FORBIDDEN container-inversion: "3He-B is an analog of the framework substrate" → INVERT: "3He-B IS the Pillar V laboratory image of the substrate's `ker(ι_*)` under the inheritance morphism; the framework substrate is logically prior".

### 5-Element CF-35 Pre-Registration

#### Element 1 — Substrate prediction (Sage-QQ exact)

| Quantity | Value | Form |
|:---------|:------|:-----|
| `cocycle_ratio_67_88` | `‖[φ_67]‖ / ‖[φ_88]‖` | Sage-QQ exact |
| Sage-QQ canonical form | `Rational(114453, 15625)` | lowest terms (gcd = 1; 15625 = 5⁶) |
| Decimal (6 sig-fig) | `7.324992` | machine-precision float-exact image |
| 4-sig-fig form | `7.3250` | publication rounding |
| `canonical_constants` pin | `substrate_cocycle_ratio_67_88 = 7.324992` | `canonical_constants.py:276` |
| Sage-QQ ↔ canonical_constants cross-pin residual | `< 1e-12` | machine precision |

The Sage-QQ exact form `Rational(114453, 15625)` is the **substrate-IS canonical form** at the rank-2 anchor `(C_H, C_εH)` parity-twin pair generators in `ker(ι_*)` (chiral pair [φ_67] + Cartan hypercharge [φ_88]). It is the framework's published canonical per S86 W-5 R2-B Convergence #3 (workshop §R2-B; line provenance in `pru-class-corpus.md`). Cross-link: `inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem (operational form)"` — substrate-derived ratio preserved INTACT in laboratory measurement at 0.0e+00 machine-precision residual (W-5 DONE-5).

#### Element 2 — Measurement protocol (Caroli-Matricon ladder asymmetry on F_1/F_2)

| Row | Observable | Substrate generator | Platform |
|:----|:-----------|:--------------------|:---------|
| F_1 | Caroli-Matricon ladder asymmetry on 3He-B vortex-core spectroscopy (ν_pump scan; left/right circulation ladder spacing asymmetry) | [φ_67] chiral-pair clean | Lancaster MCT-3 cell (G.R. Pickett / R.P. Haley group) |
| F_2 | Caroli-Matricon ladder spacing parity on 3He-B vortex-core | [φ_88] Cartan hypercharge clean | Helsinki ROTA cell (Aalto LTL; T.S. Riekki or successor) |
| F_5 | Decisive-triplet third row (auxiliary cross-check on F_1+F_2 PASS-AND) | substrate-clean per inheritance morphism | Lancaster MCT-3 + Helsinki ROTA cross-platform corroboration |

**Lab observable form**: `lab(F_i) = ‖[φ_a_i]‖ × (Δ_B/Δ_A)^p_i` where `Δ_B`, `Δ_A` are BdG gap magnitudes and `p_i` is the lab-conversion exponent for row F_i.

**Common-exponent condition**: For the F_1/F_2 decisive doublet, the lab-conversion exponents satisfy `p_1 = p_2 = p`, so the lab-conversion factor `(Δ_B/Δ_A)^p` cancels exactly between numerator and denominator of the ratio. Per `inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem"` W-5 DONE-5 machine-precision Python verification at 0.0e+00 residual:

```
lab(F_1) / lab(F_2) = [‖[φ_67]‖ × (Δ_B/Δ_A)^p] / [‖[φ_88]‖ × (Δ_B/Δ_A)^p]
                    = ‖[φ_67]‖ / ‖[φ_88]‖                  [common (Δ_B/Δ_A)^p cancels]
                    = Rational(114453, 15625)              [substrate Sage-QQ exact]
                    = 114453/15625                         [lowest terms; gcd = 1]
                    = 7.324992                             [decimal to 6 sig-fig]
```

The ratio is preserved INTACT, INDEPENDENT of (Δ_B/Δ_A) AND p. The substrate cocycle-norm ratio is the ONLY substrate-physics input.

#### Element 3 — Tolerance band

| Band class | Value | Source |
|:-----------|:------|:-------|
| Substrate-natural (Class-B cohomology-asymmetry) | `±0.1%` | substrate-level pin per `inheritance-falsifier-protocol.md §"Pre-registration discipline"` item 4 |
| Lab-systematic (Aalto LTL routine spectroscopy precision) | `±1%` | 4-sig-fig form for first-contact discriminator |
| Combined for FIRST-CONTACT discriminator | `±1%` | conservative envelope; tightens to ±0.1% at S92-S95 substrate-side re-verification at L_max=12 master cache |

Lab-measured ratio PASSes the framework's Class-B cohomology-asymmetry falsifier iff `|lab(F_1)/lab(F_2) − 7.324992| / 7.324992 < 0.01` (±1% combined band at first contact; tightens to ±0.001 substrate-natural band).

#### Element 4 — Contact partners (Pillar V superfluid laboratory roster)

| Tier | Partner | Role |
|:-----|:--------|:-----|
| Primary | Aalto LTL Helsinki ROTA-cell group (P.I. T.S. Riekki or equivalent successor) | F_2 Cartan-hypercharge clean measurement; Caroli-Matricon ladder spacing parity on 3He-B vortex-core |
| Secondary | Lancaster MCT-3 cell (G.R. Pickett / R.P. Haley group) | F_1 chiral-pair clean measurement; vortex-core ν_pump scan; cross-platform corroboration of F_1/F_2 ratio |
| Tertiary | G.E. Volovik (substrate-physics adjudication) | framework's BCS-canonical interpreter; substrate-IS adjudication of measurement ↔ inheritance morphism map |

Liaison letter Q4 2026 names all three tiers with framework prediction `lab(F_1)/lab(F_2) = 7.324992 ± 0.01` and measurement protocol per Element 2.

#### Element 5 — Timeline

| Date | Event | Status |
|:-----|:------|:-------|
| Q4 2026 | Liaison letter sent; framework prediction + measurement protocol + tolerance band specified to Aalto LTL + Lancaster MCT-3 + Volovik | PRE-REGISTERED |
| 2028-2029 | Apparatus availability + Pickett/Haley calibration schedule window opens; measurement campaign feasibility | PRE-REGISTERED forward target |
| S92-S95 (framework session count) | Substrate-side cocycle ratio re-verified at L_max=12 master cache; ±0.1% substrate-natural band tightened | reserved forward target |
| 2030+ | Cross-platform F_5 corroboration; Class-A kernel-signature NULL on F_1+F_2+F_5 decisive triplet + Class-B cohomology-asymmetry ratio 7.3250 ± 0.1% PASS-AND | structural ceiling for framework's first observational anchor at Pillar V |

Forward-pinning: PASS at S91 W9 closure = liaison block landed (this section); NO direct measurement at S91 (long-lead-time observational anchor; first-contact deadline Q4 2026 met by Q4 2026 liaison letter as the artifact-existence predicate).

### (Δ_B/Δ_A)^p Cancellation Theorem — substitution chain (verbatim from plan §W9-2 Field 6)

```
Step 1 — Definitions:
  lab(F_i) = (substrate cocycle-norm) × (lab-conversion factor)^p_i
  lab-conversion factor = (Δ_B / Δ_A)^p   where Δ_B, Δ_A are BdG gap magnitudes
  Common-exponent condition: p_i = p_j = p for F_i, F_j of interest

Step 2 — Substitution:
  lab(F_1) / lab(F_2) = [‖[φ_67]‖ × (Δ_B/Δ_A)^p] / [‖[φ_88]‖ × (Δ_B/Δ_A)^p]
                     = ‖[φ_67]‖ / ‖[φ_88]‖     [common (Δ_B/Δ_A)^p cancels]
                     = 114453 / 15625          [substrate Sage-QQ exact]
                     = 7.324992                [decimal form to 6 sig-fig]

Step 3 — Simplify:
  The ratio is INDEPENDENT of (Δ_B/Δ_A) AND p; ONLY the substrate cocycle-norm
  ratio enters.

Step 4 — Direction:
  Substrate predicts lab(F_1) / lab(F_2) > 7.0 AND < 7.7 (±5% conservative band)
  Substrate predicts within ±0.1% AND ±1% lab-systematic combined band

Step 5 — PASS criterion:
  Q4 2026 PASS iff liaison block on disk with all 5 elements
  AND substrate prediction matches 114453/15625 Sage-QQ
  AND contact-partner names cited
```

W-5 DONE-5 Python verification: machine-precision 0.0e+00 residual on the cancellation identity (substrate ratio preserved INTACT under arbitrary common-exponent (Δ_B/Δ_A)^p lab-conversion).

### Falsifier classification (Class-A + Class-B per `inheritance-falsifier-protocol.md`)

| Class | Test | F-rows | Substrate prediction |
|:------|:-----|:-------|:---------------------|
| Class-A — Kernel-signature row-wise NULL | Decisive triplet | F_1 + F_2 + F_5 | NULL (no signal) when parent BDI symmetry intact; each row tests one [φ_a] in `ker(ι_*)` |
| Class-B — Cohomology-asymmetry cross-cocycle ratio | F_1 / F_2 ratio | F_1 and F_2 simultaneously | `lab(F_1)/lab(F_2) = 7.324992 ± 0.01` (W-5 (Δ_B/Δ_A)^p cancellation) |
| Class-A — Supporting | Supporting pair | F_3 + F_4 | NULL substrate-clean on rows not entering the Class-B ratio |
| Discrimination | Slope analysis | F_4 multi-pressure 0-34 bar | Jacobi-cubic vs φ_88-linear slope-direction discrimination on cocycle-degenerate F_4 row |

Per `inheritance-falsifier-protocol.md §"Why both classes are required"`: a non-NULL detection of Class-A can be reinterpreted as parent-symmetry breakdown without falsifying the substrate; the Class-B cohomology-asymmetry ratio test is what makes the substrate prediction lab-conversion-INDEPENDENT and substrate-falsifying. Both classes saturate the substrate's predictive content.

### Calibration corpus (W11-C5 / W11-C6 from `inheritance-falsifier-protocol.md §"Calibration corpus"`)

- **S86 W-5 W11-C5** (3He-B vortex-core spectroscopy): F_1 = Caroli-Matricon ladder asymmetry, [φ_67]-clean, decisive. Gate 1 NULL on F_1+F_2+F_5; Gate 2 ratio `7.3250 ± 0.1%`; Gate 3 NULL on F_3+F_4; Gate 4 F_4 multi-pressure slope discrimination. Lab platforms: Lancaster MCT-3 + Helsinki ROTA cells.
- **S86 W-5 W11-C6** (3He-A µSR): same 4-gate structure with A-phase chirality discrimination; lab-conversion factors phase-dependent but substrate ratios identical (`Rational(114453, 15625) = 7.324992`).

### Comparison row (Pillar V superfluid laboratory)

| Substrate-canonical | Observational | Falsifier status | Detector horizon |
|:--------------------|:--------------|:-----------------|:------------------|
| `cocycle_ratio_67_88 = Rational(114453, 15625) = 7.324992` | Aalto LTL `lab(F_1)/lab(F_2)` Caroli-Matricon ladder asymmetry (NOT YET MEASURED) | FIRST observational liaison at Pillar V superfluid laboratory; STRUCTURALLY ORTHOGONAL to Pillar I CMB-S4 α_s falsifier | Q4 2026 first contact; 2028-2029 feasibility window; ±1% combined band at first contact; ±0.1% substrate-natural band at S92-S95 substrate-side re-verification |

### Cross-references

- `.claude/rules/inheritance-falsifier-protocol.md` — 4-gate structure (Class-A + Class-B + supporting + slope) + (Δ_B/Δ_A)^p Cancellation Theorem
- `.claude/rules/inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"` — rank-2 case (this CF-35); rank ≥ 3 binomial(rank, 2) cross-cocycle enumeration forward
- `.claude/rules/cross-pillar-bridge-anatomy.md §"5-anatomy + 3-level discipline"` MANDATORY at K=3 — Pillar IV substrate-IS ↔ Pillar V laboratory-IN bridge anatomy
- `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"` — substrate → bridge → laboratory direction (FORBIDDEN inversion: "3He-B IS analog of substrate")
- `sessions/framework/registry/falsifier-master-inventory.md` Row #F-3HE-B-COCYCLE-67-88 (mack-cosmic-bridge sole-writer; pending S92 W0 inventory landing)
- `computations/_shared/canonical_constants.py:276` `substrate_cocycle_ratio_67_88 = 7.324992` (S86 W-5 CANONICAL-5)
- `sessions/permanent-results-registry.md §VII.AY-OP-PROJ` — INFO-class arithmetic gloss on registry-claimed `Fraction(114453, 15625)` vs empirical rank-2 anchor `Fraction(793346, 108307)` (delta 1.76e-5 at 6th sig-fig; carry-forward S92 corrigendum per S91 W8-3/W8-5/W8-6 closeout; the CF-35 published canonical is the lowest-terms Sage-QQ form `Rational(114453, 15625)`, NOT the empirical anchor)
- Aalto LTL Helsinki ROTA-cell group (T.S. Riekki) + Lancaster MCT-3 (G.R. Pickett / R.P. Haley) + G.E. Volovik (substrate-physics adjudicator) — contact roster per Element 4

### Substrate framing (closing note)

The substrate IS the inheritance morphism `ι: A_K → A_BdG = M_2(ℂ)` between the framework's NCG-axiomatic spectral triple and the laboratory-IN 3He-B BdG sub-algebra image. The kernel `ker(ι_*)` carries substrate degrees-of-freedom that DO NOT inherit into the laboratory parent; the cocycle-ratio `‖[φ_67]‖ / ‖[φ_88]‖ = Rational(114453, 15625) = 7.324992` IS the substrate's intrinsic cohomology-asymmetry at the rank-2 anchor (chiral-pair, Cartan-hypercharge) generator pair. The Aalto LTL Lancaster MCT-3 measurement of `lab(F_1)/lab(F_2)` IS the laboratory image of this substrate-IS ratio under the inheritance morphism's image-on-spectrum. The (Δ_B/Δ_A)^p Cancellation Theorem (W-5 DONE-5; 0.0e+00 Python residual) preserves the substrate ratio INTACT in lab measurement under any common-exponent lab-conversion factor. This is the framework's FIRST observational liaison at a Pillar V superfluid laboratory; STRUCTURALLY ORTHOGONAL to the Pillar I CMB-S4 / CMB-HD α_s cosmological falsifier (the α_s_canonical 12-14σ discriminator above). Per `feedback_reporting-framing.md` discipline: a Q4 2026 PASS on liaison letter delivery + 2028-2029 measurement window opening + Class-B ratio 7.3250 ± 0.01 lab confirmation would be the framework's first observational anchor at Pillar V, locking in a multi-platform cross-check (Lancaster MCT-3 + Helsinki ROTA) under a substrate-IS cohomology-asymmetry prediction that is lab-conversion-INDEPENDENT.

---
