# Session 99 Synthesis: JWST Little Red Dots — Demographics, Seeding Forks, and Structure-Timing Constraints (S99 Sweep G8)

**Date**: 2026-06-04
**Agent**: little-red-dots-jwst-analyst
**Source Documents**:
- `downloads/research-sweep-s99/jwst-lrd/00-INDEX.md` (10-paper fetched-text index; authoritative per sweep protocol)
- `downloads/research-sweep-s99/jwst-lrd/07_Ji_PANORAMIC-...pdf` + arXiv 2604.05022 (spot-verified σ_CV; PDF Read-blocked, fell back to `read_arxiv_paper`)
- `downloads/research-sweep-s99/jwst-lrd/09_Whitler_JADES-...pdf` + arXiv 2501.00984 (spot-verified faint-end α + ρ_UV; same fallback)
- Canonical anchors (knowledge MCP): `LEGGETT-MOMENT-70`, `tau_fold`, `a_2_FW_zeta`, `Omega_DM_h2`, registries `framework-dm-properties.md` / `lrd-observational-constraints.md` / `falsifier-watchlist.md`

---

## I. Session Outcome

The S99 LRD sweep (group G8) resolves into **two structurally independent forks the substrate framework must navigate**, plus a **selection-discipline floor** that conditions every demographic claim. (1) The **seeding fork** is clean and decisive *for the framework's dark sector*: Ilie's Supermassive Dark Star (paper 06) channel is structurally CLOSED to the framework because it REQUIRES annihilating 100 GeV WIMP DM, while the framework's DM is the PROVEN CPT-neutral, NON-annihilating Leggett-channel GGE quasiparticle (`LEGGETT-MOMENT-70`, Annihilation = 0 PASS at baseline) — whereas Pacucci's gas-dynamical DCBH channel (paper 10) is framework-COMPATIBLE and supplies the six-puzzle benchmark the a_2-channel collapse must reproduce or supersede. (2) The **mass-scale tension** is a genuine JOINT constraint: Sacchi's 390 Ms Chandra stack null (paper 01) argues LRD masses/luminosities are overestimated, but Juodžbalis's dynamical Keplerian ~5×10⁷ M⊙ floor at z=7 (paper 02) removes the line-width-decoupling escape for at least Abell2744-QSO1 — both must be held simultaneously, not adjudicated away. The TWINKLE non-variability null (paper 05) is the cleanest model-independent discriminator and points toward coherent-envelope readings, with the caveat that 9 non-LRDs also do not twinkle. The structure-timing anchors (papers 07, 09) are two-axis targets; **spot-verification corrected the truncated index numbers and surfaced that paper 07's clustering excess is "mild tension / low significance," NOT a decisive signal**. No gates were computed this session — this is a literature synthesis producing pre-registered carry-forward specs.

---

## II. Key Results

### II.1 — The Seeding Fork: Dark-Star Channel CLOSED, DCBH Channel OPEN

**Result**: Paper 06 (Ilie SMDS) requires annihilating DM as the seed power source → structurally CLOSED to the framework. Paper 10 (Pacucci DCBH) is gas-dynamical → framework-COMPATIBLE. Classification: **PHONONIC** (seed = GGE acoustic interference pattern self-organizing through the a_2 channel).

Ilie's Supermassive Dark Star mechanism powers a zero-metallicity hydrostatic cloud by **dark matter annihilation** (fiducial 100 GeV WIMP via MESA), staying cool (T_eff ≲ few×10⁴ K) and extended until GR instability at a central ~few×10⁵ M⊙ region growing to ~6×10⁵ M⊙, delivering a prompt BH seed ≳10% of the progenitor mass. DM annihilation IS the thermostat and IS the seeding enabler. The framework's DM is the Leggett-channel GGE quasiparticle: an inter-band coherence mode, CPT-neutral, NON-annihilating (`LEGGETT-MOMENT-70` PROVEN, S70; Mass_LeggettDM/Δ_BCS = 11.97; `baseline-findings-s66` Annihilation = 0 PASS). There is no DM-annihilation luminosity in the framework to power a dark star — **the SMDS seeding pathway is closed by the same structural property that defines the framework's dark sector**. This is the single sharpest seed-epoch discriminator in the sweep: a confirmed DM-annihilation-powered SMDS LRD progenitor (with its predicted cool/extended spectral signature) would challenge the non-annihilating-DM property; a null for that signature is consistent with it.

Pacucci's DCBH channel reaches the same observed LRD phenomenology by a route that needs NO DM annihilation: radiation-hydrodynamic collapse of a pristine atomic-cooling halo (M_g ≈ 10⁷ M⊙ contracted to a few pc, n > 10⁷⁻⁸ cm⁻³) onto an M_• = 10⁵ M⊙ seed, with the Compton-thick accretion flow itself filtering the X-rays (the screen IS the flow, not a separate torus) and the relic neutral medium producing Balmer absorption. This maps cleanly onto the substrate frame: a heavy seed IS the GGE acoustic interference pattern self-organizing through the a_2 (gravity) channel into a compact relay-pattern attractor, with the contracted gas envelope as the laboratory-IN restatement of the substrate-IS coherent collapse. The framework's non-annihilating DM still contributes gravitational adiabatic-contraction / dynamical-friction to the halo collapse — it just does not power it. **The two forks are not symmetric**: paper 06 is closed by a proven framework property; paper 10 is open and benchmark-setting.

### II.2 — The Mass-Scale Tension: Chandra Null vs Dynamical Keplerian Floor (JOINT constraint)

**Result**: Paper 01 stacked L_bol < 3×10⁴³ erg/s (390 Ms, z≈6) vs paper 02 dynamical log M_BH ≈ 7.7 at z=7. Classification: **PHONONIC** (broad Balmer = acoustic-excitation envelope; but a genuine point mass removes the decoupling escape for QSO1).

These two papers pull in opposite directions and must both be carried. Sacchi stacks Chandra for 55 LRDs (CDF-S, ~390 Ms total) to a clean non-detection (35±38 soft, 33±61 hard net counts); with k_bol = 16.7 this gives L_bol < 3×10⁴³ erg/s, >1 OOM below the JWST-inferred LRD average of ~5×10⁴⁴ erg/s. The stack RULES OUT current super-Eddington intrinsic-X-ray-weakness models (all predict detectable soft Γ ≳ 3 spectra), leaving only extreme Compton-thick N_H ≳ 10²⁵ cm⁻² (CF=1) OR the authors' preferred resolution: **LRD masses AND luminosities are overestimated**, so standard sub-Eddington accretion suffices. In the substrate frame this is welcome — a population-wide X-ray null is exactly what the substrate WANTS if the broad Balmer line is an acoustic-excitation envelope rather than a virialized accretion disk + corona.

But Juodžbalis attacks Abell2744-QSO1 (lensed, triply-imaged, z=7, μ≈6) DYNAMICALLY — spectroastrometry on the Hα narrow-line region plus resolved kinematics plus MOKA3D modeling, with NO a priori BH-mass assumption. The rotation curve is inconsistent with a nuclear star cluster and well-fit by KEPLERIAN rotation around a point mass ~5×10⁷ M⊙ (log M_BH ≈ 7.7), consistent with the virial Balmer estimate; the stellar-mass upper limit is ~1 dex below, so stars are conclusively excluded as the dominant virial-mass contributor. **This removes the line-width-decoupling escape hatch for THIS object**: independent of line-width virialization, a real central point mass is pinned. The framework must therefore produce a genuine compact ~10⁷·⁷ M⊙ relay-pattern attractor at z=7 for QSO1, OR demonstrate the spectroastrometric+MOKA3D inference is biased. The honest joint statement: **paper 01 caps the POPULATION's intrinsic AGN luminosity (no 5×10⁴⁴ erg/s type-1 disks survive the stack), while paper 02 establishes that at least one LRD hosts a real ≥5×10⁷ M⊙ point mass.** A blanket "all virial masses inflated by ~2 OOM" fix (paper 01's preferred reading, echoing the e-scattering-correction literature in `lrd-observational-constraints.md`, Paper 15 Rusakov) is FALSIFIED for QSO1. The two coexist because QSO1 is the easiest case (lensed, spectroastrometry-tractable), not a random draw — a single dynamical detection does not validate the population's virial masses, but it does forbid the universal-deflation escape.

### II.3 — TWINKLE Non-Variability: the Model-Independent Discriminator

**Result**: Paper 05 — <10% variability across continuum + Hα flux + Hα profile over ~200-day rest-frame baseline, all 18 LRDs (+ 9 non-LRDs). Classification: **PHONONIC** (coherent excitation envelope predicts non-variability; stochastic accretion does not).

TWINKLE is the first joint spectroscopic+photometric time-domain LRD study (JWST NIRCam WFSS, Cycle 4 PID 7404), monitoring an Hα-flux-limited sample over the longest rest-frame blank-field JWST baseline to date (~200 days). The result is a clean null in all three diagnostics — every emitter falls inside the 95th-percentile measurement-noise envelope, consistent with <10% variability (caveat: for the faintest sources the per-source 3σ imaging sensitivity exceeds 10%, so 10%-level variability is not ruled out there). Luminosity-matched SDSS-RM JAVELIN AGN light curves, Monte-Carlo'd to the baseline, say typical local broad-line AGN WOULD have varied detectably. A standard accreting SMBH disk MUST twinkle on month-to-year timescales (thermal/magnetic fluctuations); the flat light curves say the rest-optical emission is NOT a bare AGN disk. In the substrate frame the emission is a post-transit GGE acoustic-excitation interference pattern self-organized through the a_2 channel — a coherent, envelope-mediated structure, so the ABSENCE of stochastic variability is PREDICTED, not anomalous. The "dense gas cocoon damps variability" reading (the Black-Hole-Star / BH* picture) is the laboratory-IN restatement of a substrate-IS coherent relay pattern. **Caveat (honest):** the 9 non-LRDs ALSO do not twinkle, so flat light curves are not uniquely an LRD trait — the null strengthens the case that broad Hα at these redshifts need not trace a virialized disk, but it does not by itself prove a coherent-envelope mechanism over a quiescent-disk mechanism. This null is also a direct cross-check of Pacucci's puzzle (f) (>100 Myr, slowly variable, radiation-pressure-regulated) — paper 10 predicts paper 05.

### II.4 — Structure-Timing Two-Axis Targets (Papers 07, 09) — NUMBERS CORRECTED

**Result**: Paper 07 — ≥1 dex quiescent-abundance excess at z≳4 (decisive) + σ_CV ≈ 0.7 ± 0.3 clustering excess (MILD tension only). Paper 09 — ρ_UV = 2.82×10²⁵ erg s⁻¹ Hz⁻¹ Mpc⁻³ at z~10, steep faint-end α = −2.36₋₀.₁₈⁺⁰·²⁰ (Schechter) to −2.60 (DPL). Classification: **PHONONIC** (post-transit GGE interference self-organized through a_2; spatially correlated by construction).

**Paper 07 (Ji PANORAMIC) — spot-verified against arXiv 2604.05022 fetched text** (the index's σ_CV decimal was truncated; I recovered it and one material caveat the truncation hid):
- **Abundance axis (decisive)**: empirical models AND cosmological simulations UNDERPREDICT massive (M* ≥ 10¹⁰ M⊙) quiescent galaxies at z≳4 by **≳1 dex** across 34 independent sightlines (406 quiescent z~3–8; 101 gold + 137 silver massive). This is the most cosmic-variance-robust such measurement to date (sixfold sightline increase over prior 2–6-sightline studies).
- **Clustering axis (MILD)**: observed **σ_CV ≈ 0.7 ± 0.3** (gold+silver, single-NIRCam-pointing scale) vs UniverseMachine sSFR-matched mock **σ_CV ~ 0.43** and halo-mass-matched mock **σ_CV ~ 0.51** — observation exceeds both mocks. **CRITICAL CORRECTION**: the paper's own language is **"only at low significance"** / **"mild tension"** (the ~0.7±0.3 error bar overlaps the ~0.43–0.51 mock predictions). The index's truncated extraction ("HIGH cosmic variance EXCEEDING predictions") overstated the strength. The clustering excess is *suggestive and directionally substrate-favorable* but **NOT a decisive second fingerprint at present** — it sharpens only with more sightlines.

**Paper 09 (Whitler JADES z≳9 UVLF) — spot-verified against arXiv 2501.00984 fetched text** (the index's α was a truncated placeholder):
- **Both-ends excess**: bright (M_UV ≲ −20) excess in tension with models, especially z≳12, with only a slow decline to z~13; AND faint-end (−18 ≲ M_UV ≲ −17) over-abundance.
- **Steep faint-end slope (corrected)**: **α = −2.36₋₀.₁₈⁺⁰·²⁰** (Schechter, z~9–12 bin) to **−2.60₋₀.₁₉⁺⁰·¹⁷** (DPL); the abstract characterizes the population as **−2.5 ≲ α ≲ −2.3** — steeper than the index's truncated "α ≲ −2" placeholder (which was the *prior-literature* comparison value, not this paper's measurement).
- **Normalization (corrected)**: **ρ_UV = 2.82₋₀.₃₃⁺⁰·³⁴ × 10²⁵ erg s⁻¹ Hz⁻¹ Mpc⁻³ at z~10** (Schechter; DPL 2.98), declining by **~3×** to **0.93 × 10²⁵ at z~13**, then **≳4×** further to **< 2.51 × 10²⁴** at higher z. The high normalization + steep faint end together imply reionization is appreciably underway by z=10.

Both papers generalize the LRD "too early" tension to STELLAR mass, and both are explicitly TWO-AXIS targets. In the substrate picture, post-transit structure IS the GGE acoustic-excitation interference pattern self-organized through the a_2 (gravity) moment (`a_2_FW_zeta = 2776.17`, S88; `tau_fold = 0.19`), so assembly speed is set by how fast the interference pattern collapses through the a_2 channel, NOT by ΛCDM hierarchical merger trees — and the pattern is spatially correlated BY CONSTRUCTION (coherent post-transit standing-wave, not Poisson-sampled halos), which is why over-clustering is the substrate-favorable direction. **The discipline (mirroring the LRD joint-constraint discipline): a substrate assembly prediction must hit BOTH axes of BOTH papers** — abundance ≳1 dex excess AND clustering excess (paper 07); slow bright-end decline to z~13 AND faint-end excess with steep α (paper 09). Matching one axis while missing the other fails the joint constraint. Note the abundance axis is decisive in both papers; the clustering axis (paper 07) is currently only mild.

### II.5 — Reionization Budget Gate (Paper 08 Singha) — LRDs-as-Type-I-Subset CLOSES the Budget

**Result**: Paper 08 — AGN supply 31–75% of ionizing photons at z>5; combined AGN+galaxy emissivity (5–12)×10⁵¹ s⁻¹ Mpc⁻³ → Γ_HI ≈ (1–2)×10⁻¹² s⁻¹, matching the z≃6 Lyα forest; LRDs absorbed as Type-I subset at η = 0.10 ± 0.02. Classification: **PHONONIC** (substrate emergent-physics chain must land inside the Lyα-forest Γ_HI window; no recombination-era modification).

Singha models the rest-UV AGN LF at 4.5 < z < 6.5 as two physical populations (unobscured Type I Schechter + obscured Type II DPL) and places LRDs/XRW/XRB AGN as **magnitude-dependent SELECTIONS** of the underlying populations, not independent contributors. Deeper spectra confirm LRDs almost always show broad lines → Type I; their LF differs only because photometric selection enhances faint and suppresses bright detections. Best-fit mixture η = 0.10 ± 0.02 for combined LRD+XRB relative to Type I; treating LRDs as independent yields no statistical gain (ΔAIC ≈ −2) and risks double-counting. The two-population model is strongly preferred (0.22 dex RMS vs 0.41 dex single-LF; ΔAIC = −52, ΔBIC = −27). The closure test: combined AGN+galaxy emissivity (5–12)×10⁵¹ photons s⁻¹ Mpc⁻³ gives Γ_HI ≈ (1–2)×10⁻¹² s⁻¹, in full agreement with Lyα-forest measurements (folding in mean-free-path + IGM clumpiness); NO photon-budget crisis for galaxy escape f_gal_esc ≤ 5% (grazes the envelope at 10%, overshoots at 20%). Even under extreme host-subtraction (f_nuc as low as 0.3), AGN stay at 31–75% (18–59% in the strict minimum-AGN case).

This is the conservative, framework-COMPATIBLE outcome. The framework does NOT modify recombination-era physics, so the CMB optical-depth budget is a place where the substrate must AGREE with standard reionization — and Singha shows standard AGN+galaxy sources already close the budget without exotic input. The substrate's emergent-physics chain (D_K eigenvalues → spectral moments → ionizing-photon production → IGM ionization → CMB τ) must reproduce the (5–12)×10⁵¹ window and the Γ_HI ≈ (1–2)×10⁻¹² floor. **The framework-compatible reading is LRDs-as-Type-I-subset (η ≈ 0.10), contributing no budget excess and no CMB-τ tension** — a substrate model that adds LRDs as copious EXTRA ionizing sources on top of the standard budget would overshoot the Lyα-forest Γ_HI and is disfavored. This couples to paper 09's "reionization underway by z=10": the substrate must supply enough EARLY UV to start reionization early WITHOUT overshooting the z≃6 Γ_HI — a two-sided gate (enough at z~10, not too much by z~6).

### II.6 — Selection-Function Floor (Paper 04 Rinaldi) — Conditions Every Demographic Comparison

**Result**: Paper 04 — classic extreme color cuts capture only ≲25% of the LRD population; demographic z-evolution is selection-driven. Paper 03 — sharp physical LF cutoff at λL_5100 ≈ 2×10⁴⁵ erg/s. Classification: **NON-PHONONIC** (systematic-uncertainty / observational-methodology constraints; they WIDEN the substrate-allowed space rather than test it directly).

Rinaldi (JADES GOODS-S+N, ~349 arcmin², inclusive selection: relaxed redness + stricter compactness + brown-dwarf rejection → 598 + 218 objects) demonstrates that classic "V-shaped SED" cuts isolate only **≲25%** of the population; the majority span a broader, largely unexplored color space. The inferred trends (LRDs appear at z≈8, peak z≈5–6, decline by z≲4) are **STRONGLY DRIVEN BY SELECTION BIASES**, and at fixed M_UV, LRDs span the full redness range — so UV-selected samples are a heterogeneous mix whose mixing biases the UVLF and its evolution. This is the systematic-uncertainty paper that WIDENS the substrate-allowed parameter space: the "too massive / too abundant too early" tension is only as sharp as the selection function is clean, and at ≲25% capture it is not. **Discipline (binding on every demographic carry-forward below): any substrate number-density-vs-z prediction is testable ONLY against a stated selection function S_i(z); comparison against a single published (selection-convolved) LRD LF without folding through S_i(z) is NOT a valid test.** Ma (paper 03, 15.5 deg², single luminous candidate) supplies the complementary bright-end shape: a sharp physical cutoff at λL_5100 ≈ 2×10⁴⁵ erg/s with both QLF slopes shallower than the LRD bright-end slope → the cutoff is physical, not a Schechter artifact, implying low-mass BHs with a narrow near/super-Eddington range. The substrate need NOT produce quasar-luminosity LRDs (no luminous tail to reproduce), and a substrate model predicting a power-law bright-end tail is falsified by the single-candidate-in-15.5-deg² null.

---

## III. Gate Verdicts

No computational gates were run this session (literature synthesis). The table below records the OBSERVATIONAL gate each paper sets for future framework computation — these are the externally-imposed thresholds, not framework verdicts.

| Observational gate (paper) | Threshold the substrate must satisfy | Decisive number |
|:---------------------------|:-------------------------------------|:----------------|
| X-ray null (01 Sacchi) | LRD intrinsic AGN L_bol below stacked ceiling | L_bol < 3×10⁴³ erg/s (390 Ms, z≈6) |
| Dynamical floor (02 Juodžbalis) | ≥1 LRD hosts a real point mass at z=7 | log M_BH ≈ 7.7 (~5×10⁷ M⊙), Keplerian |
| LF cutoff (03 Ma) | no power-law bright-end tail to quasar L | λL_5100 cutoff ≈ 2×10⁴⁵ erg/s; <10⁻⁷ Mpc⁻³ mag⁻¹ |
| Selection floor (04 Rinaldi) | prediction folded through S_i(z) | ≲25% color-cut capture fraction |
| Variability null (05 Liu/TWINKLE) | non-variable emission mechanism | <10% over ~200 d rest-frame (continuum+Hα flux+profile) |
| Seed-DM discriminator (06 Ilie) | NO DM-annihilation-powered seed | seed-epoch SMDS spectral signature absence |
| Quiescent abundance (07 Ji) | over-produce early-quenched massive by ~1 dex | ≳1 dex excess at z≳4 (34 sightlines) |
| Clustering (07 Ji) | over-cluster vs abundance-matched mocks | σ_CV ≈ 0.7±0.3 vs mock ~0.43–0.51 (MILD) |
| Ionizing budget (08 Singha) | land inside Lyα-forest Γ_HI window | Γ_HI ≈ (1–2)×10⁻¹² s⁻¹; emissivity (5–12)×10⁵¹; η≈0.10 |
| UVLF excess (09 Whitler) | both-ends excess + steep α + slow z~13 decline | ρ_UV = 2.82×10²⁵ at z~10; α = −2.36 to −2.60 |
| DCBH benchmark (10 Pacucci) | reproduce six-puzzle closure via a_2 collapse, NO DM annihilation | M_• = 10⁵ M⊙ seed; >100 Myr slow-variable obscured phase |

---

## IV. Structural Implications

**What the framework's dark sector decides at the seed epoch (CLOSED).** The non-annihilating property of the Leggett-channel DM (`LEGGETT-MOMENT-70`, PROVEN; Annihilation = 0 PASS) is not a free choice — it is the same structural property that the SMDS dark-star channel (paper 06) requires its DM to VIOLATE. So the framework's dark sector forecloses one of the two heavy-seed channels currently on the table at the seed-formation epoch. This is a genuine FALSIFIABLE fork, not a softening: if JWST confirms LRD progenitors are DM-annihilation-powered dark stars with the predicted cool/extended SMDS signature, the framework's non-annihilating-DM property is challenged. The framework's surviving seeding route is the gas-dynamical one (paper 10 DCBH ↔ a_2-channel GGE collapse), with the framework's DM contributing only gravitational adiabatic-contraction / dynamical-friction, never annihilation heating.

**The mass-scale tension is a TWO-SIDED wall, not a one-sided escape.** Prior framework framing (and the `lrd-observational-constraints.md` "too massive too early" row, 1–2σ after Rusakov+Li corrections) leaned on the line-width-decoupling reading: broad Balmer as an acoustic-excitation envelope, so virial masses need not be real. Paper 02 walls off that escape for QSO1 — a DYNAMICAL Keplerian point mass is independent of line-width virialization. Simultaneously paper 01 walls off the opposite extreme — no population of true 5×10⁴⁴ erg/s type-1 disks survives the 390 Ms stack. The substrate must therefore thread a needle: produce SOME genuine compact ~10⁷·⁷ M⊙ relay-pattern attractors (QSO1) while keeping the POPULATION's intrinsic AGN luminosity below the Chandra ceiling (most LRDs not luminous type-1 disks). The line-width-decoupling mechanism survives as a POPULATION statement but not as a UNIVERSAL one.

**Structure-timing tension generalizes from BHs to stellar mass, but the clustering fingerprint is currently weak.** Papers 07 + 09 move the "too early" tension off the BH axis onto early-quenched stellar mass (≳1 dex abundance excess, decisive) and early star-forming UV (both-ends UVLF excess, steep α, decisive). The substrate's a_2-channel assembly is the candidate mechanism for "more efficient early structure formation" that competes against the standard menu (high SFE, bursty SF, low dust, top-heavy IMF, ΛCDM modification). BUT: spot-verification demoted paper 07's clustering axis from "decisive second fingerprint" (index narrative) to "mild tension / low significance" (paper's own language) — the σ_CV ≈ 0.7±0.3 error bar overlaps the ~0.43–0.51 mock predictions. The substrate's spatial-correlation-by-construction prediction (coherent standing-wave, not Poisson halos) is directionally favored but NOT yet observationally decisive on the clustering axis. The abundance axis carries the weight.

**The reionization budget is a no-modification agreement zone, double-sided.** Because the framework leaves recombination-era physics unmodified, the CMB-τ / Γ_HI budget is a CONSISTENCY zone, not a discriminator. Paper 08 shows standard AGN+galaxy sources close the budget (Γ_HI ≈ (1–2)×10⁻¹², no crisis for f_gal_esc ≤ 5%) with LRDs as a Type-I subset (η≈0.10). The substrate must (a) supply enough early UV to begin reionization by z~10 (paper 09) WHILE (b) not overshooting the z≃6 Γ_HI (paper 08). A substrate that makes LRDs copious EXTRA ionizing sources fails side (b).

**Everything demographic is selection-conditioned.** Rinaldi's ≲25% capture fraction is the systematic floor under every number-density carry-forward. This WIDENS the substrate-allowed space (the tension is softer than a clean selection function would make it) but also DISCIPLINES every future test: a substrate abundance-vs-z prediction is only falsifiable against a stated S_i(z).

**Existing framework touchpoints.** A prior LRD-clustering computation exists (`s43_lrd_clustering`, gate CLUST-43) — the paper-07 clustering axis is the natural successor target, now with 34-sightline data and a mock-comparison protocol. The framework's `f_DM = 0.209` (Leggett-only) vs 0.844 observed remains the SOLE BOTTLENECK (S58 Volovik partition, `framework-dm-properties.md`); none of these 10 papers touch that partition directly, but the DCBH/a_2 seeding route and the structure-timing assembly route both depend on the DM playing its gravitational (not annihilation) role, which the Leggett channel does (CDM-like T(k)=1.0000 on all probed scales). The S99 sweep adds NO new canonical constants and changes NO framework verdict — it sharpens six external observational gates and closes one seeding channel by a pre-existing proven property.

---

## V. Carry-Forward Computations

**MANDATORY — primary input to the next session's planning.** Every entry has all four fields. Each is a genuine future computation (per `feedback_fix-in-session-never-defer.md`), not a hygiene item.

```
V.1. a_2-channel heavy-seed collapse vs DCBH six-puzzle benchmark (seeding fork, OPEN side)
   - What: Compute whether GGE acoustic interference self-organizing through the a_2 channel
     yields a compact relay-pattern attractor of prompt mass M_seed ~ 10^5 M_sun under
     gas-dynamical collapse with NO DM-annihilation power source. Target the Pacucci DCBH
     benchmark: M_• = 10^5 M_sun seed in an atomic-cooling-halo-equivalent overdensity,
     reproducing puzzles (a) X-ray weak via self-screening, (e) abundance, (f) >100 Myr
     slow-variable obscured phase.
   - Inputs: a_2_FW_zeta = 2776.17, tau_fold = 0.19, kappa_2_substrate_FW = 0.0210181;
     GGE post-transit structure (atlas-04 T2, S39); Pacucci paper 10 RHD density profile
     (n > 10^7-8 cm^-3, M_g ~ 10^7 M_sun) as the laboratory-IN target; L_bol < 3e43 erg/s
     ceiling (paper 01) as the X-ray-self-screening consistency check.
   - Gate: NEW — A2-DCBH-SEED-BENCHMARK. PASS: a_2-channel collapse produces M_seed ~ 10^5 M_sun
     at a substrate-derived overdensity abundance matching the DCBH host abundance within 0.5 dex,
     WITHOUT an annihilation term. FAIL: collapse requires an energy source beyond the a_2 moment
     (would force the framework toward an annihilation channel it does not have). INFO: produces a
     seed but at an abundance/redshift the substrate cannot independently source (couples to V.5/V.6).
   - Effort: 6-9 hours, 2 agent sessions (RHD-analog + abundance cross-check).

V.2. Dark-star NON-channel forward falsifier row (seeding fork, CLOSED side)
   - What: Register the SMDS dark-star channel as a CLOSED-to-framework forward falsifier in
     falsifier-master-inventory.md (mack-cosmic-bridge sole writer): substrate predicts NO
     DM-annihilation-powered LRD progenitor; the discriminating observable is the SMDS spectral
     signature (cool T_eff <~ few x 10^4 K + extended + DM-annihilation-dominated luminosity).
     Pre-register PASS/FAIL bands tied to the Leggett-channel non-annihilating property.
   - Inputs: LEGGETT-MOMENT-70 (Mass_LeggettDM/Delta_BCS = 11.97, S70); baseline Annihilation = 0
     PASS (baseline-findings-s66); Ilie paper 06 SMDS signature (100 GeV WIMP, MESA sequence,
     GR-instability at few x 10^5 M_sun); cross-link framework-dm-properties.md.
   - Gate: NEW — SMDS-NONCHANNEL-FALSIFIER. INFO/registry-landing: row added with substrate
     prediction = NULL dark-star signature, falsifier consequence = confirmed DM-annihilation SMDS
     LRD progenitor challenges non-annihilating-DM property. (Sole-writer = mack-cosmic-bridge per
     feedback_mack-bridge-role.md; this is a registry write, not a numerical gate.)
   - Effort: 1-2 hours, 1 agent session (registry landing + 4-element rubric per Class 8.2).

V.3. QSO1 dynamical-mass joint constraint with the Chandra population ceiling (mass-scale tension)
   - What: Compute whether the substrate can simultaneously (i) seed/grow a genuine ~5x10^7 M_sun
     point mass by z=7 (Juodzbalis QSO1 dynamical floor) AND (ii) keep the POPULATION-mean intrinsic
     AGN luminosity below L_bol < 3e43 erg/s (Sacchi stack). Quantify the implied accretion-rate /
     radiative-efficiency the substrate relay-pattern attractor must have to be X-ray-quiet at
     log M_BH = 7.7. Test whether the acoustic-excitation-envelope emission mechanism reproduces the
     broad Halpha WITHOUT an X-ray corona at this mass.
   - Inputs: log M_BH = 7.7 at z=7 (paper 02); L_bol < 3e43 erg/s, k_bol = 16.7 (paper 01);
     substrate emission-envelope model (II.3 coherent relay pattern); Eddington relation
     L_Edd = 1.3e38 * (M/M_sun) erg/s [MEMORY: use M/M_sun NOT M/10^8].
   - Gate: NEW — QSO1-XRAY-JOINT. PASS: substrate produces a 5x10^7 M_sun attractor whose acoustic
     envelope reproduces broad Halpha at L_X below the stacked ceiling (lambda_Edd and efficiency
     self-consistent). FAIL: the only way to be X-ray-quiet at this mass is universal virial-mass
     deflation, which paper 02 forbids for QSO1. INFO: requires Compton-thick N_H >~ 10^25 cm^-2
     (the surviving non-substrate alternative).
   - Effort: 4-6 hours, 1-2 agent sessions.

V.4. TWINKLE non-variability as a substrate emission-mechanism gate
   - What: Compute the expected variability amplitude of the substrate's post-transit GGE
     acoustic-excitation envelope on a ~200-day rest-frame baseline and confirm it is intrinsically
     <10% (coherent envelope, not stochastic accretion). Contrast against a damped-random-walk
     accretion-disk model Monte-Carlo'd to the same baseline (luminosity-matched SDSS-RM, per paper 05).
   - Inputs: GGE coherence structure (atlas-04 T2, S39; THE ORDERED VEIL — integrable not chaotic,
     never thermalizes); paper 05 control envelope (<10% over continuum + Halpha flux + profile);
     SDSS-RM JAVELIN comparison parameters. Caveat to fold in: 9 non-LRDs also non-variable.
   - Gate: NEW — TWINKLE-SUBSTRATE-VARIABILITY. PASS: substrate envelope predicts <10% variability
     intrinsically (no stochastic accretion fluctuation), consistent with TWINKLE null AND with
     Pacucci puzzle (f). FAIL: substrate emission requires a fluctuating accreting point engine
     (correlated UV-optical variations) -> falsified by the null. INFO: <10% achievable only with
     an additional damping mechanism beyond the coherent envelope.
   - Effort: 3-4 hours, 1 agent session.

V.5. a_2-channel early-quenched massive abundance vs PANORAMIC (structure-timing axis 1)
   - What: Compute the substrate's comoving number density of massive (M* >= 10^10 M_sun) quenched
     systems at z = 3-8 from a_2-channel assembly + impedance-effacement shutoff, and test against
     the >=1 dex abundance excess (decisive axis). The early-quenching mechanism = the same
     impedance-effacement that yields the dark sector shuts off further growth after rapid a_2 collapse.
   - Inputs: a_2_FW_zeta = 2776.17, tau_fold = 0.19; impedance-effacement Gamma_eff = 0.99970
     (effacement residual, phononic-framing dark-energy mapping); Ji paper 07 abundance (406 quiescent;
     101 gold + 137 silver massive; >=1 dex underprediction at z>~4); MUST fold through a selection
     function (Rinaldi S_i(z) discipline, paper 04, <=25% capture).
   - Gate: NEW — A2-QUIESCENT-ABUNDANCE. PASS: substrate over-produces early-quenched massive
     galaxies by ~1 dex at z>~4 (selection-folded) matching paper 07. FAIL: a_2 assembly + effacement
     shutoff underproduces (no excess) -> the standard-baryonic-physics fixes are not displaced.
     INFO: matches abundance but the effacement-shutoff timing is unconstrained.
   - Effort: 6-8 hours, 2 agent sessions.

V.6. a_2-channel clustering / cosmic-variance vs PANORAMIC (structure-timing axis 2) — successor to CLUST-43
   - What: Compute the substrate's predicted fractional cosmic variance sigma_CV of the early-quenched
     population (coherent standing-wave spatial correlation, NOT Poisson halo sampling) on a single-
     NIRCam-pointing scale across 34 sightlines, and compare to the observed sigma_CV ~ 0.7+-0.3 and
     UniverseMachine mocks (sSFR-matched ~0.43, halo-mass-matched ~0.51). NOTE: the observed clustering
     excess is MILD (low significance); pre-register that a PASS here is suggestive, not decisive,
     until sightline number grows.
   - Inputs: prior s43_lrd_clustering / CLUST-43 result and machinery; paper 07 sigma_CV = 0.7+-0.3
     (SPOT-VERIFIED arXiv 2604.05022) + mock values 0.43 / 0.51; substrate standing-wave correlation
     length from GGE post-transit interference structure.
   - Gate: NEW — A2-CLUSTERING-SIGMACV. PASS: substrate predicts sigma_CV > mock ~0.43-0.51 (over-
     clustering, substrate-favorable direction). INFO (expected most-likely): substrate over-clusters
     but within the 0.7+-0.3 error bar — consistent but not decisive (matches the paper's own "mild
     tension" framing). FAIL: substrate predicts sigma_CV <= mock (Poisson-like) -> contradicts the
     coherent-standing-wave construction.
   - Effort: 4-6 hours, 1-2 agent sessions (reuses CLUST-43 machinery).

V.7. a_2-channel z>~9 UVLF: both-ends excess + steep faint-end slope (structure-timing, star-forming)
   - What: Compute the substrate's rest-UV luminosity function at z ~ 9-13 from a_2-channel collapse
     into luminous star-forming knots, and test BOTH ends: bright (M_UV <~ -20, slow decline to z~13)
     AND faint (-18 <~ M_UV <~ -17 excess) with a steep faint-end slope alpha.
   - Inputs: a_2_FW_zeta, tau_fold; Whitler paper 09 SPOT-VERIFIED numbers: rho_UV = 2.82e25 erg s^-1
     Hz^-1 Mpc^-3 at z~10, ~3x decline to 0.93e25 at z~13, alpha = -2.36(-0.18/+0.20) Schechter to
     -2.60 DPL; fragmentation-to-small-scales from GGE interference-pattern mode structure.
   - Gate: NEW — A2-HIGHZ-UVLF. PASS: substrate over-produces galaxies at BOTH M_UV <~ -20 AND
     M_UV ~ -17 vs constant-SFE LCDM, reproduces alpha <~ -2.3 AND the slow bright-end decline to z~13.
     FAIL: substrate matches only the bright excess (the usual feedback-free fix) while missing the
     faint-end excess / steep slope. INFO: matches normalization but not the slope.
   - Effort: 6-8 hours, 2 agent sessions. Depends on: V.5 (shared a_2-assembly machinery).

V.8. Substrate ionizing-photon emissivity vs Lyman-alpha-forest Gamma_HI two-sided gate (reionization)
   - What: Compute the substrate's emergent ionizing-photon emissivity (D_K eigenvalues -> spectral
     moments -> ionizing-photon production) across 4.5 < z < 6.5 and verify it lands inside the
     (5-12)x10^51 photons s^-1 Mpc^-3 window AND yields Gamma_HI ~ (1-2)x10^-12 s^-1 at z~6, with LRDs
     as a Type-I subset (eta ~ 0.10), NOT as extra sources. Two-sided: enough early UV to start
     reionization by z~10 (couple to V.7), not too much by z~6.
   - Inputs: Singha paper 08 emissivity window (5-12)x10^51, Gamma_HI (1-2)x10^-12, eta = 0.10+-0.02,
     f_esc ladder (0.91/0.64/0.25/0.08); paper 09 z~10 rho_UV for the early-onset side; framework
     reionization chain (no recombination-era modification).
   - Gate: NEW — SUBSTRATE-GAMMA-HI-CLOSURE. PASS: substrate emissivity lands inside the Lyα-forest
     window with LRDs as a Type-I subset (no budget excess, no CMB-tau tension). FAIL: substrate makes
     LRDs copious extra ionizing sources -> overshoots Gamma_HI. INFO: closes at z~6 but cannot
     simultaneously source the z~10 onset (tension with V.7).
   - Effort: 5-7 hours, 1-2 agent sessions. Depends on: V.7 (z~10 UV onset).

V.9. Selection-function discipline wrapper for all LRD/quiescent demographic gates
   - What: Build a substrate-side S_i(z) folding wrapper so that V.5/V.6/V.7 abundance/clustering/UVLF
     predictions are compared to data ONLY after passing through a stated selection function, per the
     Rinaldi <=25%-capture discipline. Quantify how much the <=25% capture fraction widens the
     substrate-allowed abundance band.
   - Inputs: Rinaldi paper 04 S_i(z) machinery + <=25% color-cut capture fraction; median M_UV 5-sigma
     completeness limits; the V.5/V.6/V.7 raw substrate predictions.
   - Gate: NEW — SELECTION-FOLD-DISCIPLINE. INFO (methodology gate): produces the selection-folded
     comparison band for each demographic gate; a demographic PASS/FAIL is only VALID once folded.
     (This is the systematic floor, not a physics discriminator — but every demographic gate above
     depends on it being applied.)
   - Effort: 3-4 hours, 1 agent session. Feeds: V.5, V.6, V.7 (all demographic comparisons).
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Paper 06 SMDS dark-star seeding REQUIRES annihilating DM | PHONONIC | CLOSED to framework | Foreclosed by PROVEN non-annihilating Leggett-channel DM (`LEGGETT-MOMENT-70`); clean seed-epoch falsifier (V.2) |
| 2 | Paper 10 DCBH gas-dynamical seeding | PHONONIC | OPEN / compatible | Benchmark the a_2-channel collapse must reproduce or supersede (V.1) |
| 3 | Paper 01 Chandra null L_bol < 3×10⁴³ erg/s (390 Ms) | PHONONIC | JOINT constraint (a) | Population intrinsic AGN luminosity capped; X-ray null is substrate-expected |
| 4 | Paper 02 QSO1 dynamical log M_BH ≈ 7.7 at z=7 | PHONONIC | JOINT constraint (b) | Removes line-width-decoupling escape for QSO1; real point mass required (V.3) |
| 5 | Paper 05 TWINKLE <10% / ~200 d variability null | PHONONIC | Model-independent discriminator | Favors coherent-envelope; caveat 9 non-LRDs also flat (V.4) |
| 6 | Paper 07 quiescent abundance ≳1 dex excess at z≳4 | PHONONIC | Two-axis target, axis 1 (decisive) | a_2-assembly + effacement-shutoff candidate (V.5) |
| 7 | Paper 07 σ_CV ≈ 0.7±0.3 vs mock ~0.43–0.51 | PHONONIC | Two-axis target, axis 2 (MILD) | CORRECTED: "mild tension / low significance"; directionally substrate-favored, not decisive (V.6) |
| 8 | Paper 09 ρ_UV = 2.82×10²⁵ at z~10, α = −2.36 to −2.60 | PHONONIC | Two-end target | CORRECTED α (was truncated); both-ends UVLF excess + steep slope (V.7) |
| 9 | Paper 08 AGN 31–75% ionizing; Γ_HI (1–2)×10⁻¹²; η≈0.10 | PHONONIC | Two-sided consistency zone | No recombination-era modification; LRDs-as-Type-I-subset, no τ tension (V.8) |
| 10 | Paper 04 ≲25% color-cut capture; selection-driven z-evolution | NON-PHONONIC | Systematic floor | Widens substrate-allowed space; conditions every demographic gate (V.9) |
| 11 | Paper 03 sharp physical LF cutoff at λL_5100 ≈ 2×10⁴⁵ erg/s | NON-PHONONIC | Bright-end shape | No quasar-luminosity LRD tail to reproduce; low-mass-BH narrow-Eddington reading |

---

**Provenance note**: Framework-state claims anchored to canonical via knowledge MCP — `LEGGETT-MOMENT-70` (PROVEN, S70), `tau_fold = 0.19` (CONST-FREEZE-42), `a_2_FW_zeta = 2776.17` (S88), `kappa_2_substrate_FW = 0.0210181` (S89), `Omega_DM_h2 = 0.12` (Planck observational anchor; LEGGETT-MOMENT-70 coincides at 0.6%; NOT a substrate prediction), `f_DM = 0.209` SOLE BOTTLENECK (`framework-dm-properties.md`, S58 Volovik partition), `Annihilation = 0` PASS (`baseline-findings-s66`), prior LRD clustering `CLUST-43` (`s43_lrd_clustering`). Existing LRD observational registry: `lrd-observational-constraints.md` (paper numbers there index the PRE-EXISTING `researchers/Little-Red-Dots/` corpus, DISTINCT from the S99 sweep paper numbers used in this synthesis). Two flagged-truncated index numbers were spot-verified against fetched paper text (PDFs Read-blocked → `read_arxiv_paper`): paper 07 σ_CV = 0.7±0.3 (arXiv 2604.05022, with the "mild tension" caveat the truncation hid) and paper 09 α = −2.36(−0.18/+0.20) Schechter / −2.60 DPL + ρ_UV = 2.82×10²⁵ at z~10 (arXiv 2501.00984). The S99 sweep adds NO new canonical constants and changes NO framework verdict.
