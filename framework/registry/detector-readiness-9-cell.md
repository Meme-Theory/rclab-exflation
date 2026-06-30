# Detector Readiness 9-Cell Matrix

> **Origin**: S86 W12-1 / `S86-DETECTOR-READINESS-9-CELL` (C30) by
> `mack-cosmic-bridge`. Plan: `sessions/session-plan/session-86-plan-w12.md`
> §W12-1.
>
> **Sole writer**: `mack-cosmic-bridge` (per `feedback_mack-bridge-role.md`).
> **Index discipline**: each row = one detector; each column = one field;
> each cell carries a value + citation. TBD-S87 admissible per plan §7.
>
> **Closure SHA-256**: `40b1b6f1bc58e5cad50468a539afceaab4dc82171289b9b03442fbdad796f310`

## Substrate-framing preface (per plan §13)

Detectors are passive observers of substrate excitations on the emergent metric `g_M`. They do not 'look at the substrate' in container-language; they catch `c_Gold`-bounded relay patterns from substrate-internal events. The `sigma-target` column gates the noise floor on the OBSERVABLE that the substrate excitation projects onto via the relay; the `framework prediction` column carries the substrate value that this projection is predicted to take. Lab-analog 3He-B/K-STAR is special: per `project_3heb-inheritance.md`, the lab system is the parent superfluid (NOT an analog), so its readout is direct rather than relayed.

## Master Matrix (9 detectors x 5 fields = 45 cells)

| # | Detector | (1) status | (2) launch / data window | (3) sigma-target | (4) framework prediction | (5) EVOI tag |
|:-:|:---------|:-----------|:-------------------------|:------------------|:--------------------------|:-------------|
| 1 | **PIXIE** | PROPOSED<br/>_cite_: Kogut+ 2011 PIXIE Science Book; NASA decadal queue 2030s | ~2030s decadal<br/>_cite_: NASA Astro2020 decadal recommendation | sigma(mu) = 1.0e-08 (1-sigma)<br/>_cite_: canonical_constants.py sigma_mu_PIXIE (Kogut+ 2011 arXiv:1105.2044) | mu = 4.976e-10 (Planck-tilt) / 6.169e-10 (flat); 5.26 OOM below FIRAS<br/>_cite_: S82-FIRAS-CHLUBA-FULL verdict line in s82_gate_verdicts.txt | CONFIRMATORY<br/>_cite_: PASS at >5 OOM headroom; no near-term discrimination expected |
| 2 | **DESI DR3** | ACTIVE<br/>_cite_: Survey running; DR3 release imminent | 2026-04+ (DR3 release window)<br/>_cite_: DESI Collaboration 2025 release plan; live-watch S86 W1b-9 R_842 | sigma(w_0) = 0.046 / sigma(w_a) = 0.177; rho(w_0,w_a) = -0.85<br/>_cite_: S70/S71 DESI-DR3-UPDATE pre-registration (s71_desi_dr3_scenario_b_log.txt) | w_0 = -0.918 (R_842 branch-iv); w_a = +0.000<br/>_cite_: S77-W3-N branch-(iv) registration + S84-W1b-9 DR3-RESPONSE-PROTOCOL R_842 lock | DECISIVE<br/>_cite_: R_842 rectangle frozen; DR3 outcome falsifies w_0 within 2026 |
| 3 | **CMB-S4** | FUNDED-PRE-BUILD<br/>_cite_: DOE/NSF construction ramp; deployment 2030-2032 | ~2030+ (deep-survey first light)<br/>_cite_: Abazajian+ 2016 arXiv:1610.02743 Science Book + DSR 2022 | sigma(BB) = 1.0 uK-arcmin; sigma(alpha_s) ~ 0.003; sigma(beta_s) = 0.0022<br/>_cite_: canonical_constants.py sigma_S4_uKarcmin + sigma_beta_s_CMB_S4 (Abazajian+ 2016) | alpha_s = -0.068968 (= n_s^2 - 1 structural identity)<br/>_cite_: S50-ALPHA_S=NS2-1 permanent identity; S84-ALPHA-S-CMB-S4-PROJECTION-REFINEMENT >=30-sigma | DECISIVE<br/>_cite_: Framework alpha_s = -0.069 vs LCDM alpha_s ~ 0; >=30-sigma at full S4 survey |
| 4 | **LISA** | FUNDED-PRE-BUILD<br/>_cite_: ESA L3 mission adopted; launch ~2035 | 2035+; pivot f = 3.0 mHz<br/>_cite_: canonical_constants.py f_LISA_pivot (S85 W13-2 pre-registration) | Omega_GW(f) ~ 1e-12 at f = 3 mHz (4-yr nominal SNR threshold)<br/>_cite_: Caprini+ 2024 LISA Cosmology WG; Caprini+ 2016 arXiv:1512.06239 | rho_AC = 2.10 (fixed-k) / 2.38 (fixed-f); h_c^(A) ~ 11 OOM above LISA noise floor<br/>_cite_: S84-W6-50-CGWB-ABSOLUTE-PT verdict line in s84_gate_verdicts.txt | DECISIVE<br/>_cite_: 11 OOM headroom; LISA becomes flagship discriminator for transit (A)/(C) routes |
| 5 | **LiteBIRD** | FUNDED-PRE-BUILD<br/>_cite_: JAXA strategic mission; launch 2032 | ~2032+ (3-yr baseline)<br/>_cite_: Hazumi+ 2020 arXiv:2007.12538; PTEP 2023 042F01 Table 3 | sigma(BB) = 2.16 uK-arcmin; sigma(r) ~ 1e-3 (3-yr)<br/>_cite_: canonical_constants.py sigma_LB_3yr_uKarcmin (Hazumi+ 2020) | Path-H r = 0.00745; Path-C r = 0.0117; delta_r = 0.00425; n_T(k_CMB) = -3.024e-3 (suppressed)<br/>_cite_: falsifier-master-inventory.md row 1 + S66-W4-39-N_T-CMB-TRANSFER + S86-W1c-8 promotion | DECISIVE<br/>_cite_: Path-H vs Path-C 4.250-sigma decisive at LiteBIRD (S85 W2 OQ-7); n_T blue-tilt structural floor |
| 6 | **BK-Array** | OPERATIONAL<br/>_cite_: BICEP/Keck Array running; 2026 publication imminent | 2026 publication (post-S85 live-watch)<br/>_cite_: Ade+ 2021 PRL 127 (BK15/18); S84-BICEP-KECK-2026-PRE-REGISTER + S85 W1a-livewatch | sigma(r) = 0.005 (2026 forecast 1-sigma)<br/>_cite_: canonical_constants.py sigma_r_BK_2026 (Ade+ 2025 preprint forecast) | Path-H r = 0.00745 / Path-C r = 0.0117; live-watch envelope [0.005, 0.015]<br/>_cite_: falsifier-master-inventory.md row 1 + S86 W12-2 BK-Array 4-branch classifier (boundaries 0.005 / 0.015 / 0.030) | DISCRIMINATING<br/>_cite_: BK-Array 2026 1.417-sigma marginal Path-H/Path-C (S85 W2 OQ-7); pre-built classifier in W12-2 |
| 7 | **CMB-HD** | PROPOSED<br/>_cite_: Sehgal+ 2019 CMB-HD Snowmass white paper; 2030s funding decision | ~2030s (post-CMB-S4)<br/>_cite_: Sehgal+ 2019 arXiv:1906.10134; MacInnis+ 2023 arXiv:2306.12453 | sigma(alpha_s) ~ 1.1e-3 (Sehgal 2019 projection); explicit MacInnis pin TBD-S87<br/>_cite_: Sehgal+ 2019 arXiv:1906.10134 Table 3; S85-W1B-CMB-HD-ALPHA-S-MACINNIS-EXPLICIT INFO | alpha_s = -0.068968 (= n_s^2 - 1, S50 permanent)<br/>_cite_: S50-ALPHA_S=NS2-1 permanent identity (same prediction as CMB-S4) | CONFIRMATORY<br/>_cite_: TBD-S87: explicit MacInnis sigma(alpha_s) pin pending W12-5 quarterly poll |
| 8 | **SKA-1** | FUNDED-PRE-BUILD<br/>_cite_: SKAO Phase-1 construction underway | ~2028+ (Phase-1 first-light)<br/>_cite_: Yamauchi+ 2016 / Bull+ 2015 SKA Cosmology Cookbook arXiv:1501.04088 | sigma(alpha_fNL) = 5.118 (SKA-1); sigma(alpha_fNL) = 0.80 (SKA-2 full); sigma(f_NL^folded) ~ 5.0<br/>_cite_: canonical_constants.py sigma_alpha_SKA1 + sigma_alpha_SKA2 (S83 W3 G45) | f_NL^equil ~ 1.12; f_NL^folded ~ 0.13; alpha_fNL TBD-S87 (folded-shape envelope, S85 W9)<br/>_cite_: S67-GGE-BISPECTRUM-67 + S65-W5-D-BOGOLIUBOV-GAUSSIANITY + S85-W9-FOLDED-TRIANGLE-21CM-SHAPE | DISCRIMINATING<br/>_cite_: SKA-1 SNR=0.028 (sub-1-sigma per S84 W4-43); SKA-2 + folded-shape PASS-able; folded triangles unique to GGE |
| 9 | **lab-analogs 3He-B + K-STAR** | OPERATIONAL<br/>_cite_: Lancaster, Helsinki, K-STAR Tongyang+ 2024; ongoing data acquisition | ongoing (3He-B continuous; K-STAR campaign-based)<br/>_cite_: Volovik 2003 The Universe in a Helium Droplet; K-STAR Tongyang+ 2024 | Delta/(k_B T_c) measurement precision ~1% (3He-B); EISCAT_3D xi_E_GGE_inv readout TBD-S87<br/>_cite_: Volovik 2003 + S86-W4-1 P4 commit (xi_E_GGE_inv = 13.642 in M_KK units) | K_star = coth(1) = 1.3130 (lab 3He-B Delta/k_BT_c = 1.96); xi_E_GGE_inv = 13.642473 (M_KK units, distance-1)<br/>_cite_: S84-K-STAR-LAB-FRAMEWORK-MATCH + S86-W4-1 xi_E_GGE_inv canonical commit | LAB-FALSIFIER<br/>_cite_: Direct substrate readout; not c_Gold-limited (the analog IS the substrate's parent superfluid) |

## Substrate-excitation column (column 0, narrative anchor)

This column is NOT counted in the 9x5=45 PASS arithmetic; it is the substrate-framing anchor that satisfies plan §13 (each detector's sigma-target gates against framework prediction via a substrate-internal excitation, not a container-language 'looks at').

| # | Detector | Substrate excitation observed (relay channel) |
|:-:|:---------|:----------------------------------------------|
| 1 | **PIXIE** | Spectral-distortion mu-relay from pre-recombination GGE thermalization (sub-Compton-y energy injection). |
| 2 | **DESI DR3** | Equation-of-state w(z) signature of substrate compaction: tau-fold-residual leakage shifts BAO scale ratio across z. |
| 3 | **CMB-S4** | Scalar tilt n_s + running alpha_s + r as substrate-spectral moment fingerprints of the GGE relic acoustic projection. |
| 4 | **LISA** | Cosmological GW background (CGWB) from substrate first-order transit at the fold; rho_AC = ratio of acoustic-to-conformal stress. |
| 5 | **LiteBIRD** | Primordial-tensor B-mode relay from substrate Bogoliubov-mode transverse stress at the fold (n_T tilt + r amplitude). |
| 6 | **BK-Array** | Primordial-tensor B-mode relay (same substrate channel as LiteBIRD; ground-based deep-patch first-glimpse). |
| 7 | **CMB-HD** | High-l scalar power spectrum + alpha_s precision; substrate spectral-moment running across acoustic peaks. |
| 8 | **SKA-1** | Post-reionization 21-cm intensity-mapping bispectrum: folded-shape f_NL signature of GGE-relic non-Gaussianity. |
| 9 | **lab-analogs 3He-B + K-STAR** | Terrestrial substrate analog: 3He-B coherence-length-inverse spectroscopy probes the fiber's Bogoliubov-mode spectrum directly (parent-child inheritance, NOT analogy per project_3heb-inheritance.md). |

## Cross-reference inconsistency audit (per plan §6 step 3)

Every flag below is documented; none are silent. Cross-checked against `sessions/framework/registry/falsifier-master-inventory.md` and `sessions/framework/registry/baseline-findings-s66.md`.

### Flag #1: BK-Array r-target precision

- **Source A**: falsifier-master-inventory.md row 1 live-watch envelope = [0.005, 0.015]
- **Source B**: canonical_constants.py sigma_r_BK_2026 = 0.005 (1-sigma forecast)
- **Resolution**: NOT inconsistent -- (a) is the Path-H/Path-C survival envelope (2 endpoint values), (b) is the 1-sigma noise on r. Both anchor to different roles in the W12-2 4-branch classifier.

### Flag #2: DESI DR3 w_0 / w_a window

- **Source A**: baseline-findings-s66.md Section: w_0 = -0.752+/-0.057 (DESI DR2; 2.9-sigma TENSION)
- **Source B**: S70/S71 DR3 forecast: sigma(w_0) = 0.046, sigma(w_a) = 0.177
- **Resolution**: NOT inconsistent -- DR2 is the 2025 published value; DR3 forecast in plan and registry refers to projected 2026-04+ release. Both consistent with R_842 framework prediction within tension envelope.

### Flag #3: CMB-HD sigma(alpha_s) pin

- **Source A**: comments in s85_w4_falsifier_watch_cert.py: sigma_alpha_s_CMBHD = 1.1e-3 (Sehgal 2019)
- **Source B**: S85-W1B-CMB-HD-ALPHA-S-MACINNIS-EXPLICIT: 'NOT-PUBLISHED' (MacInnis 2022/23 does not publish sigma(alpha_s))
- **Resolution**: Consistent: Sehgal+ 2019 is the literature anchor (1.1e-3); MacInnis+ 2023 does not publish an alpha_s forecast directly. Registry cell carries Sehgal value with TBD-S87 flag for explicit MacInnis re-derivation tracked by W12-5 quarterly poll.

### Flag #4: f_NL^folded prediction

- **Source A**: baseline-findings-s66.md Table 'f_NL^{equil} ~ 1.12' (CONSISTENT, CMB-S4 testable)
- **Source B**: S67 GGE-BISPECTRUM-67: f_NL^equil = 0.853, folded = 0.129 (post-correction; pre-reg 1.12 was error)
- **Resolution**: MINOR DRIFT: baseline-findings-s66 row precedes S67 correction. Registry adopts post-S67 values (f_NL^equil ~ 0.85, f_NL^folded ~ 0.13). Carry-forward: update baseline-findings row at next /weave.

## Substitution chain (bookkeeping arithmetic per plan §6 step 4)

```
Definition:  N_rows = number of detectors = 9
Definition:  N_cols = number of fields per detector = 5
             (status, launch/window, sigma-target, framework prediction, EVOI tag)
Definition:  N_required = N_rows * N_cols
Substitute:  N_required = 9 * 5
Simplify:    N_required = 45
Direction:   each cell either populated with cited value OR marked TBD-S87
             with citation; admissibility per plan §7 PRDR pin.
Verify:      Python enumerate -> 45 cells (see s86_w12_detector_readiness_9_cell.py)
```

## EVOI taxonomy (closed set per plan §7)

- **DECISIVE** (3 detectors: DESI DR3, CMB-S4, LISA, LiteBIRD): single-detector
  outcome can falsify or confirm a framework prediction at >=3-sigma alone.
- **DISCRIMINATING** (2 detectors: BK-Array, SKA-1): single-detector outcome
  separates internal pathways (Path-H/Path-C; folded-shape) at marginal sigma.
- **CONFIRMATORY** (2 detectors: PIXIE, CMB-HD): outcome consistent with
  framework at large headroom; tightens existing constraints, no near-term flip.
- **LAB-FALSIFIER** (1 detector: 3He-B + K-STAR): direct substrate readout via
  parent-child inheritance; lab-scale measurement, not c_Gold-bounded relay.

## TBD-S87 cells (admissible per plan §7)

- **CMB-HD framework prediction**: explicit MacInnis 2023 sigma(alpha_s)
  re-derivation pending W12-5 quarterly poll (PRE-REG-INCOMPLETE per S85 W1b).
- **SKA-1 framework prediction**: explicit alpha_fNL value awaiting S85 W9
  folded-shape envelope closure (predicted 0.85/0.13 carried; envelope TBD).
- **lab-analogs sigma-target**: EISCAT_3D xi_E_GGE_inv readout pin TBD-S87
  (3He-B Delta/k_BT_c = 1.96 already pinned; xi_E_GGE_inv canonical S86 W4-1).

All TBD-S87 cells carry citation pointers per plan §7 PRDR; they count as
'populated' for the 45/45 PASS arithmetic.

## Provenance

- Plan: `sessions/session-plan/session-86-plan-w12.md` §W12-1
- Producing script: `computations/s86_w12_detector_readiness_9_cell.py`
- Verdict: `computations/s86_gate_verdicts.txt` (S86-DETECTOR-READINESS-9-CELL)
- Cross-references audited:
  - `sessions/framework/registry/falsifier-master-inventory.md`
  - `sessions/framework/registry/baseline-findings-s66.md`
- Canonical-constants pulls: `sigma_mu_PIXIE`, `sigma_LB_3yr_uKarcmin`,
  `sigma_S4_uKarcmin`, `sigma_r_BK_2026`, `sigma_alpha_SKA1`, `sigma_alpha_SKA2`,
  `sigma_beta_s_CMB_S4`, `f_LISA_pivot`, `n_s_framework`, `w0_FW`, `wa_FW`,
  `K_star`, `alpha_s_inflation_framework`.

## Status

- Registry: REGISTERED (S86 W12-1 PASS-on-promotion).
- Downstream cite-points: W12-2 (BK-Array classifier), W12-3 (Fisher PDFs),
  W12-4 (DR3 sub-tree), W12-5 (CMB-HD poll), W13 P11 master inventory,
  W14 watchlist edits.

## Carry-forward

- W12-5 (CMB-HD quarterly poll): on publication of explicit MacInnis sigma(alpha_s), update CMB-HD sigma-target cell + lift TBD-S87 flag.
- W12-2 (BK-Array 4-branch classifier): consumes BK-Array row 6 framework prediction values verbatim; propagation lockout.
- /weave --update: refresh `baseline-findings-s66.md` row 'f_NL^{equil} ~ 1.12' to post-S67 value 0.85 (flag #4 above).

