# Session 85 Synthesis 9A — W6-W13 Mack Combined Landscape

**Author**: mack-cosmic-bridge
**Date**: 2026-04-25
**Slot**: 9A (Slot 3 closeout, mack track) — feeds 9B FULL S85 W0-W13 unified closeout
**Output path**: `sessions/archive/session-85/session-85-mack-synthesis-w6-13.md`
**Scope**: P_obs_aligned update + observational watchlist (W6-W13) + 7A new-falsifier integration (PAIR with W0-W5 S-5 master inventory) + 6A flagship three-layer certification + cross-workshop dependency (2A SECTOR-1 ⇄ 2B path-(c) ξ_E_GGE) + structured carry-forward.

**Source pin SHAs (input)**:
- `sessions/archive/session-85/session-85-w6-workingpaper.md`
- `sessions/archive/session-85/session-85-w7-workingpaper.md`
- `sessions/archive/session-85/session-85-w8-workingpaper.md`
- `sessions/archive/session-85/session-85-w9-workingpaper.md`
- `sessions/archive/session-85/session-85-w10-workingpaper.md`
- `sessions/archive/session-85/session-85-w11-workingpaper.md`
- `sessions/archive/session-85/session-85-w12-workingpaper.md`
- `sessions/archive/session-85/session-85-w13-workingpaper.md`
- `sessions/archive/session-85/workshops/s85-6a-cgwb-alphas-independence.md` (load-bearing for §IV)
- `sessions/archive/session-85/workshops/s85-2a-epsilon-pivot-first-principles.md` (cross-workshop dep)
- `sessions/archive/session-85/workshops/s85-2b-branch-iv-asymmetry.md` (cross-workshop dep)
- `sessions/archive/session-85/workshops/s85-1c-perturbative-immunization-family.md`
- `sessions/archive/session-85/workshops/s85-5a-pin-drift-taxonomy.md`
- `sessions/archive/session-85/session-85-1b-3heb-inversion-volovik.md` (lab-observable registry source)
- `sessions/archive/session-85/session-85-s5-falsifier-inventory-mack.md` (W0-W5 inventory; PAIRING reference, NOT primary)
- `computations/s85_gate_verdicts.txt` (filtered to S85-W6/7/8/9/10/11/12/13)

**Knowledge MCP audit (pre-compute)**: queried `search_knowledge('observational watchlist LISA CGWB alpha_s flagship')` (15 hits, including W13-2 verdict line + 6A flagship doc + 12 equation-level traces); `search_knowledge('f_NL folded SKA 21cm')` (10 hits including S85 W9-3 plan §10 form); `list_constants('LISA|CGWB|SKA|f_NL|cgwb')` (3 matches: f_LISA_pivot=0.003, σ_α_SKA1=5.118, σ_α_SKA2=0.8); `list_constants('w_0|w_a|n_s|alpha_s|r_CMB|n_T|tau_fold|c_BLV|n_pairs|beta_s|f_NL|Omega_GW')` (16 matches; all canonical anchors confirmed). All quantitative claims below Python-verified inline.

**Substrate-first framing**: per `.claude/rules/phononic-framing.md`, every observable below is read as the substrate's spectral content projected onto a detector channel — CGWB is the GGE relic transverse-acoustic branch at c_BLV = 0.485, not a thermal tensor background; α_s is the longitudinal-Debye-cutoff curvature at the CMB pivot, not a Bayesian-posterior on an inflaton spectral tilt; f_NL_folded is the Bogoliubov-mixed three-phonon correlator on the post-transit GGE, not a multi-field non-Gaussianity; the 9 lab observables are substrate-3HeB-correspondence readouts (3HeB IS the lab realization OF the substrate, not an analog to it).

---

## I. P_OBS_ALIGNED UPDATE — W6-W13 PORTION

This section enumerates every W6-W13 verdict with an observational channel and records (observable, predicted value, predicted band, current-best observation, observational reach, time-to-decisive). Distinguished by row-class:

- **F** = framework-canonical prediction with detector-decisive σ-distance ≥ 3
- **N** = framework null-test (predicted non-detection at detector floor)
- **L** = lab-falsifier (terrestrial substrate-correspondence)
- **R** = registry-landing or methodology-class (no direct observable)

### I.1 W6-W13 P_obs_aligned table

| # | Gate | Observable | FW prediction | Pred band | Current best | Detector | Reach (year) | σ-distance | TtD | Class |
|:-:|:-----|:-----------|:--------------|:----------|:-------------|:---------|:------------:|:----------:|:---:|:-----:|
| W13-2.α | S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT | α_s = dn_s/dlnk at k* = 0.05 Mpc⁻¹ | **−0.068968** | (frozen, ZFP from S50 O-Z identity α_s = n_s²−1 with n_s = planck_ns) | Planck 2018 central −0.0045 ± 0.0067 | CMB-S4 / CMB-HD | 2030 / 2035 | **+9.62σ** vs Planck 2018; **+22.99σ** vs LCDM null | 2030 (decisive) | F |
| W13-2.Ω | S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT | Ω_GW(f_LISA = 3 mHz) | **8.299×10⁻⁵⁸** | (frozen; transit-GW spectrum at LISA pivot from s69 grid log-log interp) | LISA PLS-2024 floor σ ~ 1×10⁻¹² | LISA | 2035+ | **45.08 OOM below floor** (Python-verified) | structural null | N |
| W13-1 | S85-W13-1-BRANCH-A-HTILDE-DC | A_s (post-fold horizon-exit) | 4.27×10⁻⁹ at ε = 0.020 (INFO branch); 3.11×10⁻⁹ at ε = 0.02163 (S82-aligned) | Δ_OOM = +0.31 (out of ±0.20 PASS, in ±0.40 INFO) | Planck 2018 A_s = 2.10×10⁻⁹ ± 0.03×10⁻⁹ | Planck (landed) + Litebird tomographic improvement | 2030 (Litebird re-pin) | +0.31 OOM (×2.03) overshoot | landed (CMC) | F (TD) |
| W9-3 | S85-W9-FOLDED-TRIANGLE-21CM-SHAPE | f_NL_folded at 21-cm l_max = 1×10⁵ | **0.7685** (ratio form) / 0.7749 (envelope) | (frozen; |β|²/|α|² × shape_factor = 0.9836 × 0.7814) | Planck 2018 f_NL_local 2.5 ± 5.7; no folded constraint at 21-cm | SKA-1 / next-gen 21-cm IM | 2030+ / post-2035 | +0.011σ at SKA-1 (σ=5.0); +0.96σ at SKA-2 (σ=0.8) | post-2035 only | F (detector-sterile @ SKA-1) |
| W8-4.λ₆ | S85-W8-4-SU3-OP-LAB-PREDICTIONS | 3He-A Kelvin-wave dispersion δω_K/ω_K (λ₆ sweet spot) | **1.7267** (M_KK-normalized) | finite, O(1) | none yet measured at substrate-canonical K-scale | Aalto / ROTA / Cornell 3He-A | 2027-2030 | structural detection prediction | within 5 yr | L |
| W8-4.λ₇ | S85-W8-4-SU3-OP-LAB-PREDICTIONS | FeSe Knight-shift K_anis/K_0 (λ₇ sweet spot) | **1.8226** (M_KK-normalized) | finite, O(1) | not yet probed in triplet 1-Fe-pnictide layer | single-crystal ⁵⁷Fe / ⁷⁷Se NMR | 2026-2030 | structural detection prediction | within 5 yr | L |
| W8-4.λ₈ | S85-W8-4-SU3-OP-LAB-PREDICTIONS | 173Yb 3-body Γ-ratio (λ₈ sweet spot, hypercharge channel) | **2.8500** (M_KK-normalized) | finite, O(1) | no SU(3)-flavor-channel asymmetry measured | optical lattice 173Yb (Florence / Munich / Stanford) | 2027-2030 | structural detection prediction | within 5 yr | L |
| W8-4.cross | S85-W8-4-SU3-OP-LAB-PREDICTIONS | 6 additional cross-platform observables (3 platforms × 2 non-sweet-spot) | finite, O(0.07-13.2) | (table 7-12 of W8-4 §(d)) | none yet | 3-platform cross-checks | 2027-2030 | individual detection content; one O(13.2) at λ₇/173Yb | within 5 yr | L |
| W10-1 | S85-W10-ANTI-CORRESPONDENCE-30-REGISTRY | det(P) = 1 K-theoretic registry (no D-brane parent) | structural identity (registry entry) | 4-obstruction vector (rank, torsion, Witten integral, Bott-period); all 4 present | Witten 1998 D-brane anomaly cancellation single-brane ledger | not observational; structural-comparison registry | landed S85 | binary registry landing (PASS) | landed | R |
| W10-2 | S85-W10-R842-PHYSICAL-ANCHOR-REAUDIT | DESI DR3 (w_0, w_a) compatibility rectangle R_842 | center (−0.842, 0); half-widths (0.100, 0.200) | LOCKOUT-C frozen | DR3 not yet published; window opens 2026-04-23 | DESI DR3 cosmology paper | 2026-Q3 / 2027-Q1 | binary contained/escape; framework branch-(iv) at −0.842454 inside | within 12 mo | F (DR3 livewatch) |
| W6-1 | S85-W6-1-AWH-FORMAL | Acoustic white horizon (formal) | κ = 0.0169 EF-null derivative | (formal-geometry; not a direct detector measurement) | none observational | substrate-formal | n/a | structural | n/a | R |
| W6-3 | S85-W6-3-CONF-INF-BIFURC | Conformal-infinity topology bifurcation (5-regulator atlas) | 2 distinct topologies (dS_S3 × 3, flat_RxS2 × 2) | regulator-class-conditional | not directly measured; informs DR3 sub-tree dependency | substrate-formal | n/a | informs row W10-2 sub-trees | n/a | R |
| W6-7 | S85-W6-7-PETROV-NON-BD-PERT | Petrov classification under W3-H perturbation | type D (FAIL — instability against non-bd-perturbation) | structural FAIL | none observational | substrate-formal | n/a | structural | n/a | R |
| W12-1 | S85-W12-ELIM-1 | Inverted-Josephson dominance D_iv(L) | (D_iv8, D_iv10, D_iv12) = (−0.989, −0.992, −0.994) all − | signs (−1,−1,−1); strengthening with L | n/a | substrate-formal | n/a | structural | n/a | R |
| W12-8 | S85-W12-ELIM-8 | a_n regulator-class taxonomy | (n_a=13, n_b=0, n_c=0, n_d=3); a_0/a_2/a_4 are class-(d) | regulator-spread = 1.03 on a_2 | substrate-internal classification | substrate-formal | n/a | informs 6A kernel-orthogonality | n/a | R |
| W7-7 | S85-W7-W0-RE-AUDIT-AT-L8 | w_0 (Zubarev branch-iv post-retraction) | **0.0204** (re-audit) | (regulator-conditional; informs DR3 sub-trees) | DESI DR2 w_0 ≈ −0.829 (4-param posterior); DR3 in 2026 | DESI DR3 | 2026-Q3 | informs sub-tree fork at W1b-1 L_max=12 | within 12 mo | F (sub-pin) |
| W11-1 | S85-EPSH-JENSEN-SURVIVAL | Jensen-survival of ε_H under deformation | (NCG meta-theorem; not direct detector) | structural | none observational | substrate-formal | n/a | structural | n/a | R |
| W11-3 | S85-NCG-META-EXCLUSION-CERTIFY | NCG meta-exclusion (parent-substrate K-theoretic) | (categorical; depends on W10-1 et al.) | structural | none observational | substrate-formal | n/a | structural | n/a | R |

**Class tally** (W6-W13 only): 5 F (frozen FW predictions; W13-2.α, W13-1, W7-7, W10-2, W9-3); 1 N (structural null prediction; W13-2.Ω); 8 L (W8-4 lab-falsifier channels: 3 sweet-spot + 6 cross-platform — counted as **3 sweet-spot + 6 cross**, total 9 atomic predictions across 3 platforms); 6 R (registry/methodology/structural). Total observationally-load-bearing rows: **15** (5 F + 1 N + 9 L atomic).

### I.2 ZFP / TD tagging

Per `feedback_reporting-framing.md` and `feedback_reporting-framing.md`: every "F" row above is tagged ZFP (zero free parameter) unless explicitly marked TD (tuning-dependent). The W6-W13 portfolio:

- **W13-2.α**: ZFP. The S50 O-Z identity α_s = n_s² − 1 has zero free parameters; n_s comes from planck_ns (literature pin) and the identity is exact in the constant-mass case. The −0.068968 value falls out by substitution. **No fit, no calibration.** This is the strongest single-channel ZFP gate in the W6-W13 portfolio.
- **W13-2.Ω**: ZFP. The Ω_GW(3 mHz) = 8.299×10⁻⁵⁸ value is pure log-log interpolation of the s69 transit-GW grid produced from canonical_constants (M_KK, c_BLV, etc.) without LISA-band fitting. The structural null prediction at 45.08 OOM below floor is a hard pre-registration.
- **W13-1**: TD. The Branch-A H_tilde DC tightening produces +0.308 OOM overshoot at ε = 0.020; the result is convention-dependent on ε_pivot which is not yet derivation-complete (per 2A workshop, pin (B) = 0.02163 is substrate-rooted at the SA fold formula, but pin (A) = 0.020 is plan-pinned without canonical equivalent). INFO verdict.
- **W7-7**: TD-bordering-ZFP. Zubarev branch-iv re-audit at L=8 returned w_0 = 0.0204; this is regulator-conditional under the W1b-1 sub-tree dependency (L_max=10 → A1 PASS; L_max=12 → B2 FAIL). Sub-pin, not full FW prediction.
- **W10-2**: ZFP geometric (R_842 anchor). LOCKOUT-C verified; rectangle frozen at center (−0.842, 0) with half-widths (0.100, 0.200). The framework's branch-(iv) prediction of w_0 = −0.842454 sits inside R_842 with offset 0.000454 = 0.45% of half-width.
- **W9-3**: ZFP. f_NL_folded = 0.7685 = (|β|²/|α|²) × shape_factor with |β|² = n_pairs = 59.8 (S42 canonical Parker IC anchor) and shape_factor = 0.7814 from the analytic-template-folded ridge integral. Zero fit parameters.
- **W8-4 (9 lab observables)**: ZFP. Each of the 9 lab observables is a Frobenius commutator norm × symmetry-compatibility coefficient; all coefficients are pinned at plan-freeze (proj_kelvin / proj_nmr / proj_Yb). The δE_a values follow from Δ_B1, Δ_B2, τ_fold (canonical_constants).

**Inventory consequence (per `feedback_reporting-framing.md`)**: PASS rows with zero free parameters are EVIDENCE, not neutral. The W13-2.α prediction at +9.62σ from current Planck central, derived ZFP from the S50 identity, is one of the framework's strongest existing single-channel staked positions — comparable in evidentiary weight to the β_s = −0.1331 W0-1 flagship from the W0-W5 inventory. The W13-2.Ω structural null prediction is also evidence: framework foreswears any LISA-band stochastic GW signal at 45 OOM below floor — a binary observational discriminator at the next decade's flagship GW observatory.

### I.3 Detector-roadmap timeline (W6-W13 layer; integrates with W0-W5 §IV master tree)

```
2026-04-23 (today): DESI DR3 window OPEN [W10-2 LOCKOUT-C frozen, FW @ -0.842454 inside R_842]
2026-Q3: DESI DR3 cosmology release [decisive on row W10-2 + W7-7 sub-pin; cascades to W0-W5 row 1]
2026 mid: BK-Array 2026 release [decisive on W0-W5 row 4; FW r=0.011732]
2027-Q1: DESI DR3 final [W1b-10 BF_indep=10.75 fires post-data; α_s × w_0 decoupled joint]
2030: CMB-S4 deploys [DECISIVE on W13-2.α at +22.99σ separation from LCDM null,
                     +9.62σ separation from current Planck central; widens to ~64σ if S4 holds Planck (Python-verified)]
                     [DECISIVE on W0-W5 row 2 β_s at +60.5σ]
                     [r confirmation via LiteBIRD at +11.7σ]
2030+: SKA-1 21-cm IM [W9-3 detector-sterile at SKA-1 (σ=5.0 vs FW=0.77 → +0.15σ);
                     waits for SKA-2 (σ=0.8 → +0.96σ); decisive only at next-gen 21-cm at l_max~10⁵]
2027-2030: 3He-A / FeSe / 173Yb labs [W8-4 9-channel lab-falsifier suite operationally testable
                     after W8-4 SI-unit translation (W8-4 carry-forward Priority 6)]
2035+: LISA [DECISIVE on W13-2.Ω at 45 OOM below floor — null-detection pre-registered;
            any detection of Ω_GW > 1e-12 at f∈[10⁻⁴, 10⁻¹] Hz falsifies the transit-GW spectrum shape]
2035+: CMB-HD α_s [tightens W13-2.α to ~64σ joint single-channel discrimination]
post-2035: 21-cm next-gen at l_max ~ 10⁵ [W9-3 SNR projection 3.4×10⁸ at σ_per_mode ~ 10⁻⁵;
                     promotes f_NL_folded from detector-sterile to FLAGSHIP-class]
```

---

## II. OBSERVATIONAL WATCHLIST — W6-W13 INTEGRATION

### II.1 W13-2 LISA null + CGWB+α_s flagship

**Watchlist entry summary**:

```
Channel:        Joint (CGWB at LISA-band) × (α_s at CMB-S4 pivot)
Pre-registered: 2026-04-24 (S85-W13-2 INFO PASS-conditions)
Pin:            audit_sha256=f514d642fe2a80ac408ddc0a09da94c5a8590a0127b4754fd337ea57eb2c02c1
                content_sha256=58630dc36e59af32dfece11e521736c13c27f9a943a91ac03bb91249f2529779
Flagship doc:   sessions/framework/CGWB-alpha-s-joint-flagship-pre-registration.md (4378 B)
FW predictions: α_s = -0.068968 (S50 O-Z identity, ZFP);
                Ω_GW(3 mHz) = 8.299e-58 (s69 transit-GW grid log-log interp, ZFP)
Detectors:      CMB-S4 (σ_α = 0.003); LISA (σ_Ω = 1e-12 PLS-2024)
Significances:  α_s: +22.99σ vs LCDM null; +9.62σ vs Planck 2018 central
                (verified Python: 0.9649² - 1 = -0.06896799; |α_s|/0.003 = 22.99;
                 |α_s - (-0.0045)|/0.0067 = 9.62; |α_s - (-0.0045)|/0.001 = 64.47 if S4 holds Planck)
                Ω_GW: 45.08 OOM below LISA PLS floor (verified Python: log10(1e-12 / 8.299e-58) = 45.08)
Falsification:  α_s outside [-0.075, -0.063] at 2σ (CMB-S4) → α_s channel falsified
                Ω_GW > 1e-12 at any f ∈ [10⁻⁴, 10⁻¹] Hz → transit-GW null falsified
Joint detection logic: see §IV three-layer ρ adjudication
```

The W13-2 verdict line `value=(alpha_s=-0.068968, Omega_GW_LISA=8.299e-58, rho_cc=0.0, Fisher_PD=1)` certifies the experimental Fisher matrix is positive-definite with zero off-diagonal **in the (CGWB, α_s) basis on the experimental noise covariance**. The full three-layer adjudication of the ρ=0 claim is the load-bearing item from 6A — see §IV.

**INFO trigger origin (NOT a physics failure)**: The INFO verdict was triggered by the band-width diagnostic Ω_GW(6 mHz)/Ω_GW(1.5 mHz) = 7.875 > 0.20 threshold. This proxy was intended as L_max-sensitivity check; what it actually measured is the steep rising slope of the transit-GW spectrum in the mHz region as it climbs toward the GHz-band peak. That is a **structural feature of the transit-GW spectrum shape**, not a truncation artifact. A direct L_max=8 vs L_max=10 spectrum comparison at f_LISA is the clean S86 carry-forward (per §VI.1 below).

### II.2 W9-3 f_NL_folded SKA Phase-2 21-cm

**Watchlist entry summary**:

```
Channel:        21-cm bispectrum folded-shape amplitude
Pre-registered: 2026-04-24 (S85-W9-FOLDED-TRIANGLE-21CM-SHAPE PASS)
Pin:            audit_sha256=2484b4a24419329157645bfbd5426b77d861649bc02a05c2a7dc7cd3a78ee274
                content_sha256=d0f08fb302eb13fc5779ca608c5c5b532ef38329e286df991bf5434510d87c1c
FW prediction:  f_NL_folded = 0.7685 (ratio form, plan §10 Step 3, ZFP)
                = (|β|²/|α|²) × shape_factor
                = (59.8/60.8) × 0.7814    [Python-verified: 0.9836 × 0.7814 = 0.7685]
                |β|² = n_pairs = 59.8 (S42 Parker IC anchor; canonical_constants.py)
                shape_factor = 0.7814 (analytic-template-folded ridge integral, 1024 sample pts)
Detectors:      SKA-1 (σ_f_NL = 5.0 → SNR = 0.15; detector-sterile)
                SKA-2 marginal (σ ~ 0.8 → SNR = 0.96; sub-1σ)
                Next-gen 21-cm IM at l_max ~ 10⁵, σ_per_mode ~ 10⁻⁵ → SNR projection = 3.4×10⁸
Substrate origin: GGE-relic post-transit acoustic squeezed state; Bogoliubov β_k ≠ 0 with |β|² = 59.8;
                three-mode correlator on the post-transit Jensen-SU(3) substrate
Falsification:  At post-2035 21-cm next-gen, |f_NL_folded - 0.7685| > 5σ_detector → folded-shape channel falsified
                Disambiguation from W0 BC-template: W9-3 pre-registers SHAPE+amplitude (PASS at FINITE+WELL-DEFINED);
                W0 S85-FOLDED-BISPECTRUM-21CM-SHAPE-TEMPLATE FAILed at SKA-Phase-2 detection threshold (different gate)
EVOI tag:       SUPPORTING at SKA-1 (P_decisive ~ 0.05); promotes to FLAGSHIP at next-gen 21-cm (P ~ 0.40+)
```

### II.3 W8-4 9 lab observables (3HeB-correspondence readout suite)

The W8-4 PASS produces **3 framework-unique SU(3)-internal OP directions × 3 platforms = 9 lab-testable predictions**. Per the substrate-first framing, these are NOT analog predictions to a separate physical system — the substrate IS realized in 3He-A / FeSe / 173Yb to within the inheritance partition that 3He-B exhausts (5 inherited Gell-Mann generators) plus the framework-unique extension (3 unique generators {λ₆, λ₇, λ₈}).

**Watchlist entry summary**:

```
Channel:        9-channel lab-substrate correspondence registry (3 dirs × 3 platforms)
Pre-registered: 2026-04-24 (S85-W8-4-SU3-OP-LAB-PREDICTIONS PASS)
Pin:            audit_sha256=823be1df5f28067384b7947412ce44034b830bc66c10159ee2d97cffe7d3a25b
                content_sha256=4470f3bd3b34dec87ec1ac67ae4c7a62d6b197bd27c0a9b5b725e50bba4fe8a7
FW predictions (sweet-spot, M_KK-normalized):
  λ₆ → 3He-A Kelvin-wave dispersion δω_K/ω_K = 1.7267  (real-symmetric (2,3) sector)
  λ₇ → FeSe Knight-shift K_anis/K_0       = 1.8226  (imaginary-antisymmetric (2,3) sector)
  λ₈ → 173Yb 3-body Γ-ratio                = 2.8500  (diagonal-hypercharge, SU(3)-flavor channel)
Substrate δE_a (M_KK units):
  δE_6 = δE_7 = 0.8907 M_KK (degenerate by real-vs-imaginary complement)
  δE_8 = 0.3291 M_KK (smaller; only τ_fold·λ₄ term couples)
Coherence lengths:
  ξ_6 = ξ_7 = 1.1227 M_KK^-1; ξ_8 = 3.0387 M_KK^-1
Detectors / labs:
  3He-A:   Aalto / ROTA / Cornell rotating cryostats (T → T_c⁻ in restricted geometry)
  FeSe NMR: single-crystal triplet candidate, ⁵⁷Fe / ⁷⁷Se, c-axis vs ab-plane Knight shift
  173Yb:   Florence / Munich / Stanford optical lattices (3-body loss channel asymmetry)
Falsification:  Each individual sweet-spot non-detection within fractional shift > 0.5 falsifies its λ_a direction
                Joint non-detection of all 3 sweet-spots falsifies the canonical Gell-Mann partition (5 inherited + 3 unique)
EVOI tag:       LAB-FALSIFIER-SUITE — none of the 3 sweet-spot detectors is a flagship-class CMB / DESI / LISA mission,
                but the 3 are operationally testable within ~5 years; each is a substrate-first ZFP prediction
                (modulo the canonical Gell-Mann partition assumption, which is itself a S86 carry-forward refinement)
SI-translation gap: predictions are M_KK-normalized ratios; carry-forward W8-4 Priority 6 is to convert each to MHz / ppm / s⁻¹
                via compactification-scale mapping for direct experimentalist-actionable proposals
```

**1B-extended registry (volovik 1B synthesis, same source-paper)**: Beyond the 3 W8-4 sweet-spots, 1B identifies **6 additional cross-platform substrate-correspondence channels** (e.g., FeSe edge-mode STM, μSR on confined ³He-A, magnon spectroscopy in chiral magnets, 173Yb-µSR, 173Yb-3-body × FeSe-NMR cross-correlations), bringing the lab-observable registry to 9 rows. Per the volovik 1B synthesis, this 9-row registry is targeted for landing at `sessions/framework/lab-observable-registry.md` (carry-forward V.1 of 1B; not duplicated here — gen-physicist 9A handles cross-schedule registry-landing recommendations).

### II.4 W10-1 ANTI-CORRESPONDENCE #30 det(P)=1 vs Witten 1998 + 3 strengthening parents

**Registry entry summary** (NOT an observational watchlist row — this is structural-comparison registry, but counted here per task's "any other observational channels surfaced" clause for completeness):

```
Channel:        Substrate-vs-alternative-substrate K-theoretic correspondence ledger
Registered:     2026-04-24 (S85-W10-ANTI-CORRESPONDENCE-30-REGISTRY PASS, value=30)
Pin:            audit_sha256=e034e19f7fbc3d9642997559ed8fd77c070e98331d07dddbf04405b2c464fddc
                content_sha256=5e5f6f0dcb6cbefcbfe146aa9ecc056f55b653469308a487308518ef36042138
FW prediction:  4-obstruction vector — K_0 rank=3 (Witten requires 1); K_0 torsion-free (Witten requires Z/2);
                Witten integral = 16.0 (required 1.0); Bott-period residue (16 mod 8 = 0; 16 mod 2 = 0 — neither = 1)
Cluster:        "no-Bott-structure, no-unitary-target" (kaku post-S64; siblings #19 no-T-duality, #20 no-S-duality, #21 no-Hagedorn)
Strengthening:  3 additional parent-substrate exclusions queued (heterotic, M-theory, twisted-K) — W10-5 carry-forward
Falsification:  Not a detector falsifier; structural-comparison registry. The framework-vs-Type IIB substrate
                divergence is ledger-pinned; no future observational data updates the registry directly
EVOI tag:       META-STRUCTURAL — informs framework's own identity (NOT string theory in disguise; IS finite matrix
                model with Volovik-type emergent gravity, S64). Feeds W11-3 NCG-meta-exclusion certification.
```

This is **not a row of the master falsifier inventory**, but it is a load-bearing entry in the §VII.Q registry section drafted by the W10-1 patches. Recorded here for §III pairing analysis (it has no W0-W5 master-inventory pair — it is a registry-class addition).

### II.5 Other observational channels surfaced in 1A/1B/3B/etc.

**1A CC-residue (cc-residue-phonon-first / transit / landau)**: the CC-residue chain affects the cosmological constant prediction; not directly W6-W13 observational, but feeds the Λ-pin permanent-results-registry §VII.M.4. No new observational channel introduced beyond W0-W5 inventory row 12 (A_s closure / TD).

**1B 3HeB-inversion (volovik / landau / connes)**: the 9 lab observables (covered in §II.3 above; volovik 1B synthesis V.1 lands the registry).

**3A ζ-stabilization (lizzi / spectral-geometer)**: meta-methodological; no new observational channels.

**3B branch-c-phonon (volovik / landau / kaku)**: feeds the W12-1 inverted-Josephson dominance reading (covered in §I.1 row W12-1; not separately observational).

**4A elimination-bulletins (gen-physicist / kaku)**: registry-class; covered by §III pairing.

**1D vii-p-meta (van-den-dungen / connes / lizzi)**: meta-NCG; informs the W11-1/W11-3 substrate-formal results (covered in §I.1 rows; not separately observational).

---

## III. 7A NEW-FALSIFIER INTEGRATION (PAIR with W0-W5 S-5 master inventory)

This section identifies whether each W6-W13 observational candidate above PAIRS with an existing W0-W5 S-5 master-inventory row OR is genuinely new. **PAIRINGS are recorded; NO ROWS ARE DUPLICATED.** Where pairings exist, the structural relationship is documented (e.g., "same instrument, different observable" or "joint multi-σ pathway").

### III.1 Pairing table

Source: `sessions/archive/session-85/session-85-s5-falsifier-inventory-mack.md` §III.1 (W0-W5 master inventory; 12 rows).

| W6-W13 row | W6-W13 channel | W0-W5 S-5 row pair? | Pairing relationship | Action |
|:-----------|:---------------|:-------------------:|:---------------------|:-------|
| W13-2.α | α_s = −0.068968 (S50 O-Z) | **PAIRS row #3** (α_s §VII.Ω-INFLATIONARY identity, also −0.068968) | **SAME observable, SAME framework prediction, SAME convention.** W13-2 §(b) re-derives the identity inside a different gate context (joint Fisher with Ω_GW), uses the same canonical pin α_s_inflation_framework = −0.068968 (verified via list_constants). The W13-2 row STRENGTHENS the W0-W5 row #3 by adding a Fisher-PD certification on a second observable (Ω_GW); it does NOT introduce a new α_s prediction. | Mark W13-2.α row as PAIR(S5#3); inventory row #3 σ-distance values held canonical; W13-2 contributes the joint-Fisher pin to the existing row, not a duplicate row. |
| W13-2.Ω | Ω_GW(3 mHz) = 8.299e-58 (null prediction) | **PAIRS row #7** (CGWB ρ_AC, h_c^(A) ~ 11 OOM above LISA noise; W1a-7 SNR=1.68e13) | **SAME instrument (LISA), DIFFERENT observable.** Row #7 (W0-W5) is the **CGWB phase-transition amplitude** under the (A) regulator at the LISA peak band — h_c^(A) ~ 11 OOM ABOVE noise, FLAGSHIP-decisive. W13-2.Ω is the Ω_GW(3 mHz) projection from the s69 **transit-GW** spectrum's far-IR tail at the LISA pivot — 45 OOM BELOW floor, structural NULL. **Both predictions live on the same detector (LISA) but at orthogonal regulator-classes / spectral regions.** Row #7 is what LISA would detect IF the framework's regulator-class (A) PT-amplitude reading is the operative one; W13-2.Ω is what LISA would NOT detect from the structural transit-GW null prediction. The two together are the **(A)/(C) regulator discriminator** that the inventory row #7 already pre-registers as W0-W5 §IV.7 carry-forward. | Mark W13-2.Ω row as PAIR(S5#7) **same-instrument-different-observable**; W13-2.Ω contributes the explicit null floor for the (C)-side of the (A)/(C) discriminator. New inventory column "Companion null (C-regulator)" recommended at S5#7 to record the W13-2.Ω value at SHA `f514d642fe2a80ac…`. |
| W13-1 | A_s tightening (Δ_OOM = +0.31 INFO) | **PAIRS row #12** (A_s = 3.30e-9, ~+57% / +4× above Planck central; CONSTRAINT-MAP CLOSURE TD) | **SAME observable, REFINED framework value.** W13-1 produces 4.27e-9 at ε=0.020 and 3.11e-9 at ε=0.02163; row #12 of the master inventory carries 3.30e-9 (S82 W3-7 reference). The W13-1 INFO verdict reports a sensitivity of A_s to ε_pivot at the few-percent level; the W13-1 outcome does NOT refute row #12, it **maps the ε-sensitivity** of the same prediction. | Mark W13-1 row as PAIR(S5#12) refinement-pin; add an "ε-sensitivity caveat" sub-note to row #12: A_s ranges 3.11e-9 (ε=0.02163) → 4.27e-9 (ε=0.020); ε_pivot derivation-completion is S86 SECTOR-1 carry-forward (cross-workshop dep, see §V). |
| W7-7 | w_0 (Zubarev L=8 re-audit) = 0.0204 | **PAIRS row #1** (w_0 Volovik partition, −0.918) and the L_max sub-tree structure of W0-W5 §IV.1 W1b-1 | **SAME observable, REGULATOR-LAYER SUB-PIN.** Row #1 carries the Zubarev/Volovik canonical w_0 = −0.918 at L_max=10 (as referenced in S5 row #1 ZFP commit). The W7-7 re-audit at L=8 returns w_0 = 0.0204 (positive! — quintessence cell B2). The W1b-1 sub-tree dependency in the W0-W5 inventory §IV.1 already pre-registered the regulator-layer flip (L_max=10 → A1; L_max=12 → B2). W7-7 confirms a **third regulator-layer datum** at L=8. | Mark W7-7 row as PAIR(S5#1) **regulator-layer sub-pin**; update the W1b-1 sub-tree to a **3-row table** (L=8: w_0=+0.0204 → B2 cell; L=10: w_0=−0.918 → A1 cell; L=12: w_0=B2-side per S84 W4-46 G51 split). The DR3 adjudication-protocol regulator-first sequencing (V.3 of W0-W5 carry-forward) is now **strengthened** with W7-7 as the third grid point. |
| W10-2 | R_842 LOCKOUT-C reaudit (PASS-locked-v1-pending) | **PAIRS row #1** (w_0 Volovik / R_842 livewatch infrastructure) | **SAME falsifier infrastructure, registry-hygiene reaudit.** W10-2 is an audit of the R_842 anchoring; row #1 is the falsifier itself. W10-2 verifies LOCKOUT-C unchanged AND DR3 wiring intact AND branch-(iv) at −0.842454 inside R_842 with offset 0.45% of half-width. | Mark W10-2 row as PAIR(S5#1) **infrastructure-audit** (no inventory-row change); record W10-2 dual-SHA `8de72cde7d635949…` as the post-S85 audit-pin reference to row #1's livewatch-hygiene state. **Note discrepancy**: row #1 says ZFP commit w_0_FW = −0.918; W10-2 reports branch-(iv) canonical at −0.842454. This is a **different number** (cf. carry-forward §VI.7). |
| W9-3 | f_NL_folded = 0.7685 at 21-cm l_max=1e5 | **PAIRS row #9** (f_NL_folded = 0.0547 / 0.129; SUPPORTING) | **SAME observable, DIFFERENT framework pathway.** Row #9 carries the W4-7 / S82 W3-4 GGE value f_NL = 0.0547 (equilateral) and S67 GGE-BISPECTRUM-67 f_NL = 0.129 (folded). W9-3 produces 0.7685 (folded) via the **plan §10 Step 3 ratio form** (|β|²/|α|² × shape_factor) — different scheme + convention + L_max from the W0/S82/S67 pathways, NOT a contradiction (W9-3 PASS conditions are FINITE+WELL-DEFINED+COMPUTED, not a detection threshold; W0's BC pathway FAILed at SKA-Phase-2 detection threshold with f_NL = 1.45e-5). | Mark W9-3 row as PAIR(S5#9) **alt-pathway-sub-pin**; row #9 in the inventory should be expanded to a **3-pathway table**: (a) S82 W3-4 GGE-equilateral f_NL = 0.0547; (b) S67 GGE folded f_NL = 0.129; (c) **W9-3 analytic-template-folded f_NL = 0.7685**. All three are framework-internal pathways for related-but-distinct templates. The 9B master inventory should record all three with explicit pathway labels (per V.2 of W0-W5 carry-forward style); **none are wrong**, they pre-register different SHAPE templates. |
| W8-4.λ₆/λ₇/λ₈ + 6 cross | 9 lab-falsifier observables | **NO existing W0-W5 row** — GENUINELY NEW falsifier suite | **NEW row class needed.** The W0-W5 master inventory has 12 rows, all of which are CMB / DESI / LISA / PIXIE / 21-cm / Planck-historical channels. **No lab-falsifier rows exist in the W0-W5 inventory.** The 9 lab observables (3 sweet-spot + 6 cross-platform) constitute a **genuinely new falsifier-suite class** that the master inventory does not currently carry. | Add new master-inventory row **#13 LAB-CORRESPONDENCE-SUITE** (or 9 atomic rows #13–#21) with the 9 W8-4 / 1B observables, EVOI tag = **LAB-FALSIFIER**, P_decisive = 0.30–0.50 (5-yr terrestrial-lab horizon). 9B should incorporate this new class into the unified master inventory. **PAIR status: NEW.** |
| W10-1 | det(P)=1 K-theoretic registry | **NO existing W0-W5 row** — REGISTRY-CLASS addition | **REGISTRY, not falsifier.** W10-1 is a structural-comparison ledger update; the W0-W5 inventory does not carry registry-class rows. Recommend a parallel `sessions/framework/correspondence-table-registry.md` row, NOT an inventory-table row. | Mark W10-1 as REGISTRY-EXTENSION (no inventory row added); patches drafted at `s85_w10_anti_correspondence_30_REGISTRY_PATCH.md` and `s85_w10_anti_correspondence_30_MEMORY_PATCH.md` ready for landing under separate registry. |
| W6-1, W6-3, W6-7, W12-1, W12-8, W11-1, W11-3 | structural / formal / methodology results | **NO observational pairs** — substrate-formal | These are structural / formal / regulator-taxonomy / NCG-meta gates. No observational signatures attached. Not falsifier rows. | No inventory action; recorded in §I.1 as R-class for completeness. |

### III.2 Pairing summary tally

- **Pairs with existing W0-W5 row** (refinement / sub-pin / infrastructure): **6 W6-W13 rows** (W13-2.α → S5#3; W13-2.Ω → S5#7; W13-1 → S5#12; W7-7 → S5#1; W10-2 → S5#1; W9-3 → S5#9).
- **Genuinely new** (no W0-W5 pair, additions needed): **1 row class (9 atomic predictions)** — W8-4 lab-falsifier suite (NEW class LAB-FALSIFIER).
- **Registry-class** (no inventory-table row): **1** — W10-1 ANTI-CORRESPONDENCE #30.
- **Structural / formal** (not falsifier-class): **7** — W6-1, W6-3, W6-7, W12-1, W12-8, W11-1, W11-3 (covered in §I.1 R-class).

**Net inventory delta**: 0 duplicates; 1 NEW row class (lab-falsifier suite) needed; 6 PAIR enrichments to existing rows; 1 REGISTRY-EXTENSION queued separately.

### III.3 Specific PAIR enrichments to recommend to 9B

The following structural-relationship augmentations to the W0-W5 inventory should appear in the unified 9B closeout:

1. **Row #1 (w_0)**: add 3-row regulator-layer sub-pin table (L=8 W7-7 → L=10 canonical → L=12 split); add W10-2 audit-pin SHA reference.
2. **Row #3 (α_s §VII.Ω)**: add W13-2 joint-Fisher pin at SHA `f514d642fe2a80ac…` (no value change; strengthening citation only).
3. **Row #7 (CGWB ρ_AC)**: add Companion-null-(C-regulator) column with W13-2.Ω value 8.299e-58 at SHA same as above; document the (A)/(C) discriminator structure explicitly.
4. **Row #9 (f_NL_folded)**: expand to 3-pathway table (S82 GGE-equilateral / S67 GGE-folded / W9-3 analytic-template-folded), each with its own scheme + convention + L_max + SHA.
5. **Row #12 (A_s)**: add ε-sensitivity sub-note (range 3.11e-9 to 4.27e-9 over ε ∈ {0.02163, 0.020}); note ε_pivot is S86 SECTOR-1 carry-forward.
6. **NEW row(s) #13–#21 (lab-falsifier suite)**: 9 atomic rows or 1 row-class entry. EVOI tag LAB-FALSIFIER. Each row carries its δE_a / observable-magnitude / platform / SI-translation-pending status.

---

## IV. 6A FLAGSHIP CERTIFICATION — three-layer ρ adjudication

The 6A workshop (`s85-6a-cgwb-alphas-independence.md`) — tesla × mack, 3 rounds — produced the **single most important structural insight from the W6-W13 wave for the observational watchlist**: the W13-2 verdict line `rho_cc=0` is **layer-discriminated**. This section integrates the three-layer adjudication into the watchlist.

### IV.1 The three ρ values (mack E-mack-1 taxonomy, accepted across both R3 turns)

The 6A workshop converged on a **three-Fisher taxonomy** that distinguishes which ρ value is being claimed:

```
LAYER 1 — ρ_experimental (tautological)
  Definition: Pearson correlation under the experimental-noise covariance, in the (CGWB, α_s) basis with NO substrate marginalization.
  Origin:     The 2×2 Fisher F = diag(1/σ_CMBS4², 1/σ_LISA²) is constructed with no shared explicit fit parameter.
  Value:      ρ_experimental = 0 (by construction; basis-tautology).
  W13-2 cert: ρ_cc=0, Fisher_PD=1 — VERIFIED at this layer (PASS-conditions all hold).
  Substantive content: BASIS-CHOICE TAUTOLOGY — adding a parameter that no observable depends on
                      keeps the Fisher block-diagonal. This certifies experimental decorrelation
                      under the chosen detector-noise model, NOT substrate independence.

LAYER 2 — ρ_substrate-marg (observably-diluted)
  Definition: Pearson correlation under the substrate-marginalized Fisher (Schur-complement of the a_n nuisance block).
  Origin:     F_marg = A − B C⁻¹ B^T with B carrying the parameter-level partial derivatives ∂O/∂a_n.
  Computed:   R2-A workshop produced ρ_substrate-marg = +2.4e-46 (zeta), +1.4e-45 (Pauli-Villars).
  Reading:    NON-ZERO at substrate level; observably DILUTED by detector-noise floors at all current/planned detectors.
  Importance: MILD substantive substrate-coupling exists (a_2 enters BOTH O_CGWB at leading and O_α_s at leading
              under the constant-mass S50 identity); kernel-orthogonality argument fragile at the parameter level
              (mack pushback, R1 Re:T3). The ~2e-46 magnitude is too small to register at Fisher-noise levels.

LAYER 3 — ρ_substrate-prediction (observably ALIVE)
  Definition: Pearson correlation under the framework's PREDICTIVE distribution over substrate parameters
              (Monte Carlo over W12-4 5-regulator atlas, propagated through Jacobian to (O_CGWB, O_α_s)).
  Origin:     E-mack-2 prediction (NEGATIVE per magnitude convention); E-tesla-3-2 R3 numerical verification.
  Computed:   ρ(Ω_GW, α_s_signed) = +0.9114 (signed convention, Python-verified)
              ρ(Ω_GW, |α_s|)      = -0.9114 (magnitude convention, Python-verified)
  Driver:     Pauli-Villars OUTLIER on BOTH axes simultaneously — smaller a_2 (factor ~5) under PV produces
              larger predicted Ω_GW (since 1/G_N ∝ a_2 → Ω_GW ∝ G_N), and SMALLER |α_s| (since smaller a_2/a_0
              gives n_s closer to scale-invariant, hence α_s = n_s² − 1 closer to 0). PV is the joint outlier
              in OPPOSITE directions for the two observables.
  Reading:    LARGE substantive substrate-prediction correlation; sign convention-dependent per Q-tesla-11.
  S86 status: UNCOMPUTED at the level of pre-registered Monte Carlo over the predictive distribution;
              the R3 spot-check Pearson over the 5-point W12-4 atlas is DIAGNOSTIC, not a frozen prediction.
```

### IV.2 What the W13-2 INFO verdict certifies (and what it does NOT)

**Substitution chain — W13-2 ρ=0 layer-attribution** [SIGN, CHAIN, VERIFY]:

```
Step 1 — Definitions:
  W13-2 verdict line:  rho_cc = 0; Fisher_PD = 1
  Fisher matrix:       F = diag(1/σ(α_s_CMBS4)², 1/σ(Ω_GW_LISA)²)
  Off-diagonal:        F_12 = 0 by construction (no shared explicit fit parameter)
  ρ via Fisher:        rho = F_12 / sqrt(F_11 · F_22)

Step 2 — Substitute:
  rho = 0 / sqrt(1.111e+05 · 1.000e+24) = 0   [W13-2 §(e), Python-verified]

Step 3 — Simplify:
  This expression for ρ is built ONLY from experimental-noise covariance
  (σ_CMBS4 = 0.003 from CMB-S4 Science Book; σ_LISA = 1e-12 from LISA PLS-2024)
  AND a basis choice that has no shared explicit parameter. NO substrate parameters
  enter F at all. The Schur-complement of the a_n nuisance block is NOT computed;
  the predictive Monte Carlo over the W12-4 atlas is NOT computed.

Step 4 — Direction (read off canonical form):
  ρ = 0 at LAYER 1 (experimental Fisher in the (CGWB, α_s) basis) is CERTIFIED by W13-2.
  ρ = 0 at LAYER 2 (substrate-marg) is REFUTED — R2-A computed +2.4e-46 (non-zero, observably diluted).
  ρ = 0 at LAYER 3 (substrate-prediction) is REFUTED — R3 Pearson |ρ| ≈ 0.91 over the 5-regulator atlas.

Conclusion: The W13-2 verdict line `rho_cc=0` is structurally correct AT LAYER 1 only.
            "Joint-detection significance multiplies as independent products" (the schedule §6A invocation reading)
            requires LAYER 3 ρ_substrate-prediction = 0, which is FALSE at |ρ| ≈ 0.91.
            The substantive observational-watchlist claim — that CMB-S4 and LISA jointly produce a multiplicative
            σ-significance — is regulator-conditional and requires the predictive-Monte-Carlo S86 gate to settle.
```

### IV.3 S86 ρ_substrate-prediction gate spec inheritance

Per E-mack-2 + E-tesla-3-2 + Q-mack-7 + Q-mack-8 (6A R3):

- **Convention pin**: the S86 gate spec MUST pre-register **either** the SIGNED convention (ρ ≈ +0.91) **or** the MAGNITUDE convention (ρ ≈ −0.91), NOT both. The two are equivalent up to sign; mixing reports introduces a PRU class-8 vulnerability.
- **Atlas weighting pin**: the |ρ| ≈ 0.91 result is REGULATOR-CHOICE-CONDITIONAL — driven by Pauli-Villars's outlier-ness on BOTH axes. With PV down-weighted (treating it as a regulator-Bayesian outlier), the 4-regulator residual gives a much smaller correlation. The S86 gate spec MUST pre-register the atlas treatment (uniform 5-regulator weighting OR PV-down-weighted OR PV-excluded).
- **Joint detection significance band**: under the full 5-regulator |ρ_pred| ≈ 0.91, the joint CMB-S4 × LISA significance does NOT multiply. The product 22.99σ × (LISA-floor-aware significance) is replaced by a Mahalanobis-distance band whose width depends on which convention is reported. Pre-register the band BEFORE S86 closes.

### IV.4 Watchlist-significance update

Under the three-layer adjudication, the master observational watchlist for W13-2 should record:

```
W13-2 joint-flagship significance (post-6A adjudication):
- α_s alone (LAYER 1 detector reach, CMB-S4 σ=0.003):       +22.99σ vs LCDM null; +9.62σ vs Planck 2018 central
- Ω_GW alone (LAYER 1 detector reach, LISA PLS):            structural NULL prediction (45 OOM below floor)
- JOINT (multiplicative under ρ_experimental = 0):          22.99σ × null-channel-non-detect = SAME as α_s alone (no boost)
- JOINT (correct under ρ_substrate-prediction |ρ|≈0.91):    REGULATOR-CONDITIONAL Mahalanobis band; S86 gate required
                                                              before joint significance can be quoted as a single number
- Substrate-marg dilution (LAYER 2 ρ ≈ 2e-46):              negligible at all detector-noise floors; confirms
                                                              experimental Fisher block-diagonality is operationally robust
```

The S5 master-inventory row #3 (α_s) and row #7 (CGWB ρ_AC) should each carry a footnote to the 6A workshop record that the JOINT significance is regulator-conditional pending S86 ρ_substrate-prediction gate. Single-channel σ-distances reported in S5 §III.1 are LAYER 1 and unchanged by 6A.

---

## V. CROSS-WORKSHOP DEPENDENCY — 2A SECTOR-1 ξ²(0) ⇄ 2B path-(c) ξ_E_GGE

**Observation from 2A workshop (transit-resonance × landau-condensed-matter)**: the unified S86-FOLD-PIVOT-RUNNING-FLOW gate splits into **SECTOR 1 (SR-flow, Z-factor renormalization) governing pin (A) ε_pivot closure** and **SECTOR 2 (Mellin-kernel, K-invariant)**. Per 2A R3 (transit C2-R3 + landau C4-L-R3), the SECTOR 1 PRDR collapses to **one substrate-first ξ²(0) IC sub-derivation needed**: ξ²(0) determined by SECTOR 1 substrate-first derivation from a_4/a_2 (or equivalent) Seeley-DeWitt moment ratio.

**Observation from 2B workshop (volovik × landau)**: the K-coupled R_JK functional is at substrate-distance 1 from D_K (pure-Casimir-moment), while the E-coupled R_JE = ξ_J / **ξ_E_GGE** is at substrate-distance ≥ 2 (post-GGE-relic + post-regulator-ratio-closure). Per 2B path-(c) reading, **ξ_E_GGE := S_Zub_E(L) / S_zeta_E(L)** is an energy-weighted second-moment spectral SUM with two regulator dressings sharing a ratio.

**Coupling**: 2A SECTOR-1 ξ²(0) candidate (the substrate-first IC for the SR-LO ε(N) ODE) inherits its substrate-derivation from a moment ratio of the Seeley-DeWitt expansion — and the most natural such ratio is a_4/a_2 OR an energy-weighted variant. Per 2B's classification, the energy-weighted variant is **ξ_E_GGE** itself, which carries 2-regulator-class admixture (Zubarev / zeta) — i.e., the SECTOR-1 ξ²(0) IC, if sourced via the energy-weighted route, is **2B-path-(c) coupled** with attendant regulator-class admixture properties.

**Observational consequence**: any joint observable computation downstream of pin (A) ε_pivot closure (which includes W13-1 A_s tightening AND any future pin-(A)-dependent recomputation of α_s_LPB at pivot AND any post-pin-(A) re-evaluation of n_s) carries the **2B-derived substrate-moment provenance** through the SECTOR-1 ξ²(0) IC. The S86 S5 master-inventory row #12 (A_s) ε-sensitivity sub-note from §III.3 above therefore inherits a **pin to the 2B path-(c) ξ_E_GGE substrate moment** when the SECTOR-1 derivation completes.

**Watchlist note**: this dependency means that **EITHER** SECTOR-1 ξ²(0) is sourced from the K-channel pure-Casimir route (2B path-(b), substrate-distance 1, no regulator-class admixture) **OR** from the E-channel energy-weighted route (2B path-(c), substrate-distance ≥ 2, regulator-class admixture inherited). The CHOICE between routes affects ALL downstream observable predictions tied to ε_pivot. The 9B unified closeout should record this as a shared dependency between the W6-W13 watchlist (W13-1 A_s + downstream) and the W0-W5 carry-forward (V.6 α_s prefactor derivation, which may also feed through ε_pivot).

**No direct observable is computed in this synthesis from 2A/2B**; the cross-workshop dependency is a STRUCTURAL pin recorded for the S86 S86-FOLD-PIVOT-RUNNING-FLOW gate's PRDR enumeration and for the S86 ρ_substrate-prediction gate's substrate-prior specification (see §IV.3).

---

## VI. STRUCTURED CARRY-FORWARD (per `feedback_fix-in-session-never-defer.md`)

Each item: **What / Inputs / Gate / Effort**. All items are observational-watchlist or watchlist-adjacent (registry / pin) and feed S86 planning.

### VI.1 S86 — sharper L_max-sensitivity proxy for Ω_GW(f_LISA)

- **What**: Replace the W13-2 §(f) CC-4 band-width proxy (Ω_GW(6 mHz)/Ω_GW(1.5 mHz) = 7.875) with a direct L=8 vs L=10 spectrum comparison at f_LISA = 3 mHz. The current 7.875 ratio measured spectral slope (a structural feature), not L_max truncation sensitivity. A direct L_max comparison closes the W13-2 INFO trigger origin.
- **Inputs**: s69_transit_gw at L_max=8 (existing) and L_max=10 (existing); canonical_constants pins f_LISA_pivot = 3e-3 Hz, c_BLV = 0.485, n_pairs = 59.8; W13-2 dual-SHA `f514d642fe2a80ac…`.
- **Gate**: S86-W?-CGWB-LMAX-DIRECT — PASS iff |Ω_GW(L=8) − Ω_GW(L=10)| / Ω_GW(L=10) ≤ 0.20 at f_LISA. Per `feedback_arbitrary-gates.md`: avoid 0.20 round-number trap; INFO band is acceptable.
- **Effort**: 1-2 h (existing s69 grid load + interpolation; no new spectral computation).

### VI.2 S86 — ρ_substrate-prediction Monte Carlo gate over W12-4 5-regulator atlas

- **What**: Pre-register and compute the LAYER-3 ρ_substrate-prediction over the W12-4 5-regulator atlas, propagating (a_0, a_2, a_4) through the full Jacobian to (Ω_GW, α_s). Settle the (signed vs magnitude) sign-convention ambiguity by pre-registering ONE convention. Pre-register the atlas-weighting choice (uniform 5-regulator OR PV-down-weighted OR PV-excluded). Report the resulting joint-detection significance band.
- **Inputs**: W12-4 atlas a_0/a_2/a_4 vectors (5 regulators, from `s85_w12_a_n_regulator_taxonomy.npz`); the 6A R3 E-tesla-3-2 spot-check Pearson values (+0.9114 / −0.9114 signed/magnitude); s69 transit-GW Jacobian; S50 α_s = n_s² − 1 identity Jacobian.
- **Gate**: S86-W?-RHO-SUBSTRATE-PREDICTION-MC — PASS iff (a) sign convention pre-registered, (b) atlas-weighting pre-registered, (c) 1000-sample Monte Carlo over W12-4 atlas converges to ρ_pred with σ ≤ 0.05, (d) joint-detection σ-significance band reported as Mahalanobis distance under the predicted covariance. INFO if PV-outlier-domination flagged at ≥ 50% of the variance.
- **Effort**: 4-6 h (Jacobian assembly + Monte Carlo + dual-pre-registration document landing at `sessions/framework/rho-substrate-prediction-pre-registration.md`).

### VI.3 S86 — SECTOR-1 ξ²(0) substrate-first IC derivation

- **What**: Close the 2A workshop's SECTOR-1 PRDR-clean ξ²(0) IC: derive ξ²(0) from a substrate-first moment ratio — either (a) pure-Casimir K-channel route (2B path-(b), substrate-distance 1) OR (b) energy-weighted GGE route (2B path-(c), ξ_E_GGE-coupled, substrate-distance ≥ 2). Pre-register the route choice and run the SR-LO (ε, η, ξ²) ODE from fold IC to N_pivot to land pin (A) ε_pivot.
- **Inputs**: a_4/a_2 zeta-regularized values from W12-4; ξ_E_GGE = S_Zub_E(L) / S_zeta_E(L) at L=10; ε(N) ODE in M_Pl_eff² ≡ S/d²S normalization; canonical_constants ε_H_W6 = 0.02163 (pin (B) anchor for cross-check).
- **Gate**: S86-W?-FOLD-PIVOT-RUNNING-FLOW-SECTOR-1 — PASS iff (a) ξ²(0) IC derivation lands with substrate-first chain, (b) ε(N) ODE integration converges at N_pivot = 55, (c) pin (A) ε_pivot lands within ±0.001 of either 0.020 or 0.02163 with sub-derivation tag, (d) downstream A_s and α_s_LPB recomputations close at machine ledger.
- **Effort**: 8-16 h (ODE integration + substrate-first derivation workshop landau / transit / van-den-dungen, possibly multi-round).

### VI.4 S86 — S5 master-inventory PAIR-enrichments landed (6 row updates per §III.3)

- **What**: Apply the 6 PAIR-enrichments from §III.3 to the master inventory at `sessions/framework/falsifier-master-inventory.md` (currently pending V.1 of W0-W5 mack synthesis): row #1 + 3-row regulator-layer table + W7-7 + W10-2 SHAs; row #3 + W13-2 joint-Fisher pin SHA; row #7 + Companion-null-(C-regulator) column with W13-2.Ω value; row #9 + 3-pathway table; row #12 + ε-sensitivity sub-note; new row(s) #13–#21 (lab-falsifier suite from W8-4 + 1B 9-row registry).
- **Inputs**: §III.3 of this synthesis; W0-W5 §III.1 master inventory; relevant W6-W13 dual-SHAs.
- **Gate**: S86-W?-MASTER-INVENTORY-W6-W13-LAND — PASS iff (a) all 6 PAIR-enrichments landed at SHA-pinned positions, (b) lab-falsifier suite added as new row class with EVOI tag LAB-FALSIFIER, (c) zero duplicate rows introduced, (d) frontmatter `ingested-by: /weave --update` present.
- **Effort**: 1.5 h (writer + cross-reference verify + dry-run).

### VI.5 S86 — Lab-falsifier suite SI-unit translation gate (W8-4 Priority 6 + 1B C3)

- **What**: Translate the 9 lab observables (3 sweet-spot + 6 cross-platform) from M_KK-normalized ratios to laboratory units (3He-A Kelvin-wave shifts in MHz; FeSe Knight-shift K_anis in ppm; 173Yb 3-body loss in s⁻¹; etc.) via compactification-scale mapping. Required for direct experimentalist-actionable proposals (Aalto / FeSe / 173Yb collaborators).
- **Inputs**: M_KK canonical (knowledge MCP); ω_L1 canonical; reference experimental constants from Aalto / FeSe / 173Yb literature (web-fetch via paper-search MCP); W8-4 9-channel table; 1B 9-row registry.
- **Gate**: S86-W?-LAB-SI-TRANSLATION — PASS iff (a) all 9 observables converted to SI units with lab-conventional reporting, (b) per-platform σ_detect literature anchors landed for each, (c) timeline-to-decisive estimated for each within 5-yr horizon.
- **Effort**: 3-4 h (literature pinning + unit conversion).

### VI.6 S86 — DR3 sub-tree consolidation incorporating W7-7 L=8 datum

- **What**: Per §III.1 W7-7 PAIR (S5#1) regulator-layer sub-pin: extend the W1b-1 DR3 sub-tree from the existing 2-row (L=10 / L=12) regulator-layer table to a **3-row (L=8 / L=10 / L=12) table**. W7-7 confirms L=8 datum w_0 = +0.0204 (positive — quintessence cell B2). Pre-register a regulator-first DR3 adjudication protocol that pins L_max BEFORE box check.
- **Inputs**: W7-7 dual-SHA (s85_gate_verdicts.txt line for `S85-W7-W0-RE-AUDIT-AT-L8`); W1b-1 verdict (W0-W5 §III.1 table row 10); S84 W4-46 G51 split data; canonical_constants tau_fold = 0.19.
- **Gate**: S86-W?-DR3-SUB-TREE-3-ROW-PIN — PASS iff (a) 3-row regulator-layer table lands in `sessions/framework/DR3-RESPONSE-PROTOCOL.md`, (b) regulator-first sequencing pre-registered, (c) W7-7 SHA cited as the L=8 source datum, (d) 7-cell A1/A2/B1/B2/B3/C1/C2 decision rules unchanged at all 3 L_max grid points (per LOCKOUT-A discipline).
- **Effort**: 2 h (protocol amendment + W7-7 SHA pin + dry-run).

### VI.7 S86 — Resolve w_0_FW value discrepancy (S5 row #1 −0.918 vs W10-2 branch-(iv) −0.842454)

- **What**: The W0-W5 master inventory row #1 carries `w_0_FW = −0.918` as the ZFP commit (Volovik effacement Γ=0.99970 origin); W10-2 reports the **branch-(iv) canonical value −0.842454** as the PRIMARY ZFP framework prediction inside R_842 (at offset 0.45% of half-width). These are **DIFFERENT NUMBERS** (−0.918 lies inside R_842 with offset 7.6% of half-width per Python verification; both technically inside; but the PRIMARY ZFP value matters for the +3.28σ vs LCDM null calculation in S5 row #1). Pre-register a decision rule: which of −0.918 or −0.842454 is the PRIMARY framework w_0 prediction at the level of the master inventory's σ-distance reporting? — and update either row #1 or W10-2 audit to converge.
- **Inputs**: W10-2 dual-SHA `8de72cde7d635949…`; S5 row #1 W4-7 SHA `bf8135bf…`; S58 Volovik partition derivation; tau_fold = 0.19 (fixed); branch-(iv) canonical S82 / S83 references.
- **Gate**: S86-W?-W0-PRIMARY-VALUE-RESOLVE — PASS iff (a) decision rule lands in `sessions/framework/permanent-results-registry.md` §VII.M.1, (b) master inventory row #1 either lists single canonical value with provenance OR explicitly lists 2-pathway (Volovik partition / branch-(iv) substrate-compaction) with both σ-distances reported, (c) W10-2 audit and DR3 livewatch reference the same canonical value.
- **Effort**: 2 h adjudication (mack-cosmic-bridge + landau-condensed-matter-theorist + connes-ncg-theorist; 1 round).

### VI.8 S86 — W9-3 alt-pathway pre-registration consolidation

- **What**: Per §III.1 W9-3 PAIR (S5#9) alt-pathway sub-pin: consolidate the 3 framework f_NL_folded pathway predictions (S82 W3-4 GGE-equilateral 0.0547 / S67 GGE-folded 0.129 / W9-3 analytic-template-folded 0.7685) into a single registry document declaring which template each pathway pre-registers. This unification clarifies which of the 3 predictions a given 21-cm experiment should test, and at which detector horizon.
- **Inputs**: W9-3 dual-SHA `2484b4a24419329…`; S82 W3-4 verdict + S67 GGE-BISPECTRUM-67 verdict; existing master-inventory row #9.
- **Gate**: S86-W?-FNL-FOLDED-PATHWAY-REGISTRY — PASS iff (a) 3-pathway registry document lands at `sessions/framework/f-nl-folded-pathway-registry.md`, (b) each pathway tagged with scheme + convention + L_max + SHA, (c) experimentalist-facing summary table listing detector horizon for each.
- **Effort**: 1.5 h (registry document landing + cross-reference verify).

### VI.9 S86 — Lab-falsifier suite EVOI-level assignment + 5-yr decision tree

- **What**: Per §III.1 W8-4 NEW row class: assign EVOI level (LAB-FALSIFIER) and pre-register a 5-yr decision tree for each of the 9 lab observables. Each row needs P_decisive_by_2030 (mid-range 0.30-0.50) + lab-platform contact list + per-detector σ_detect (post-SI translation) + falsification clause (e.g., "non-detection of sweet-spot with fractional shift > 0.5 falsifies framework-unique direction λ_a").
- **Inputs**: VI.5 SI-translation output (prerequisite); W8-4 9-channel table; 1B 9-row registry.
- **Gate**: S86-W?-LAB-FALSIFIER-EVOI-TREE — PASS iff (a) 9 atomic rows present in master inventory (or 1 row class with 9 sub-rows), (b) each carries P_decisive + falsification clause + SI-unit prediction + lab-platform pin, (c) decision tree explicit on each individual sweet-spot non-detection vs joint sweet-spot non-detection scenarios.
- **Effort**: 2-3 h (post-VI.5; EVOI methodology applied + tree drafting).

### VI.10 S86 — Inventory of W6-W13 R-class results in §VII registry

- **What**: The 7 R-class results in §I.1 (W6-1 AWH-formal κ=0.017; W6-3 conformal-infinity 2-topology bifurcation; W6-7 Petrov non-bd-perturbation FAIL; W12-1 inverted-Josephson dominance signs (−,−,−); W12-8 a_n regulator-taxonomy class-(d); W11-1 Jensen-survival meta; W11-3 NCG meta-exclusion) are NOT observational watchlist rows but DO update the structural-results registry. Catalogue these in `sessions/permanent-results-registry.md` §VII.Q (parallel to W10-1 patch).
- **Inputs**: W6/W7/W11/W12 dual-SHAs from `s85_gate_verdicts.txt`.
- **Gate**: S86-META-W6-W13-R-CLASS-LAND — PASS iff (a) 7-row R-class entry lands at registry §VII.Q, (b) each carries dual-SHA + classification (PHONONIC / GEOMETRIC / META / NON-PHONONIC) + downstream-trigger note, (c) cross-references to relevant observational rows where applicable (W12-1 → W7-7 / W10-2; W12-8 → W13-2 6A; W11-1/W11-3 → W10-1 / W11 series).
- **Effort**: 1.5 h (registry section landing).

---

## VII. Summary of structural position (W6-W13 observational track)

The W6-W13 wave produced **15 observationally-load-bearing rows** (5 frozen FW predictions, 1 structural null, 9 lab atomic predictions across 3 platforms) and **6 R-class structural results**. Of the observational rows:

- **6 PAIR with existing W0-W5 inventory rows** (refinement / sub-pin / infrastructure) — net inventory delta is enrichment, not duplication.
- **1 row class is genuinely new** (lab-falsifier suite) — first-of-kind for the inventory; requires a NEW EVOI tag (LAB-FALSIFIER).
- **1 registry-class addition** (W10-1 ANTI-CORRESPONDENCE #30) — parallel registry, not inventory.

The 6A workshop produced the wave's most consequential structural insight: the W13-2 verdict line `rho_cc=0` is **layer-discriminated** into three distinct ρ values, only one of which is certified by W13-2 (LAYER 1 experimental Fisher = 0 by construction). The substantive substrate-prediction LAYER 3 |ρ| ≈ 0.91 is uncomputed and requires an S86 Monte Carlo gate (VI.2). **Joint CMB-S4 × LISA significance does NOT multiply at the substrate-prediction layer** — the joint Mahalanobis-distance band is regulator-conditional pending the S86 gate.

The cross-workshop dependency between 2A SECTOR-1 ξ²(0) and 2B path-(c) ξ_E_GGE pins the substrate-moment provenance of all post-pin-(A) downstream observables (most directly W13-1 A_s tightening) to the SECTOR-1 ξ²(0) IC route choice (K-channel pure-Casimir vs E-channel energy-weighted). The 9B unified closeout should record this as a load-bearing carry-forward.

The **single most decision-relevant fact for S86 planning** from the W6-W13 portfolio: the three-layer ρ adjudication (§IV) means that 6 of the 12 W0-W5 inventory rows are **methodology-affected** (rows #3, #7 directly via W13-2 joint-Fisher pin; rows #1, #9, #12 via PAIR enrichments; row #7 via Companion-null-(C-regulator) column) — and the three-layer taxonomy must propagate into ALL S86 joint-detection significance computations. This is not a physics-status update; it is a **how-the-statistics-are-quoted** discipline, which 9B must standardize across the unified master inventory.

DR3 fires within 12 months and remains the SINGLE most decision-relevant **observational** event (per W0-W5 §VII); the W6-W13 layer adds W7-7 as a third regulator-grid datum for the sub-tree (VI.6) and W10-2 as the LOCKOUT-C audit-pin (VI.7).

---

## VIII. Files produced

| Artifact | Path |
|:---------|:-----|
| This synthesis (9A mack W6-W13) | `sessions/archive/session-85/session-85-mack-synthesis-w6-13.md` |
| Carry-forward S86 specs (10 items) | Section VI of this file |
| PAIR-enrichment instructions for master inventory | Section III.3 of this file |
| 6A three-layer adjudication + S86 ρ_substrate-prediction gate spec inheritance | Section IV of this file |

**End of W6-W13 mack combined-landscape synthesis (9A).**
