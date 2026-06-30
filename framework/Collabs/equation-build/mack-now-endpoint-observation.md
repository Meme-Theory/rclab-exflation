# §7 — THE EQUATION AT NOW: WHERE IT TOUCHES DATA

> **Section author**: mack-cosmic-bridge (Katie Mack — Cosmic Bridge). Sole writer of `sessions/framework/registry/falsifier-master-inventory.md` per `feedback_mack-bridge-role.md`.
> **Owns**: the endpoint. What the single equation predicts *at τ_now* that observation tests — the foot of the "to NOW" arc.
> **Canonical sourcing**: every framework value is pulled from `mcp__knowledge__.get_constant` / `falsifier-master-inventory.md` / `mack-observational-constraints.md` (AMRI-promoted) / atlas-03 E-numbers. Observational anchors (Planck/DESI/PDG/ACT) appear as **comparison only** — the substrate does not fit them; it predicts past them. PRELIMINARY tags mark anything non-canonical.

---

## 7.0 The endpoint is not a fit — it is a readout

The whole document has assembled ONE equation, the Chamseddine–Connes spectral action of the Jensen-deformed Dirac operator (E4):

$$
S[D_K,\,f,\,\Lambda] \;=\; \mathrm{Tr}\, f\!\left(\frac{D_K(\tau)^2}{\Lambda^2}\right)
\;=\; \underbrace{2 f_4 \Lambda^4\, a_0}_{\text{a}_0\ \to\ \text{CC / dark energy}}
\;+\; \underbrace{2 f_2 \Lambda^2\, a_2(\tau)}_{\text{a}_2\ \to\ \text{gravity}}
\;+\; \underbrace{f_0\, a_4(\tau)}_{\text{a}_4\ \to\ \text{YM + Higgs}}
\;+\;\ldots
$$

Section 7 closes the arc. Everything upstream ran the equation *at-τ* and *at-time-t*, from the τ=0 vacuum floor through the first-order transit at τ_fold = 0.190 to τ_now. **The point of §7 is that the same equation, evaluated once, emits numbers we can put a detector on today.** No observable below is fit. Each is a spectral moment of $D_K$ at the same single modulus τ. When the substrate measures one of these quantities, the substrate is probing itself — every CMB photon, every BAO ruler, every SN distance is an active acoustic perturbation of the same fabric whose $D_K$-spectrum generated the prediction. There is no container the measurement happens "in." The measurement IS substrate-on-substrate (per `phononic-framing.md §"IS Space, Not IN Space"`).

The honest endpoint has three faces, and §7 keeps them distinct: **(7.1)** what the equation predicts at τ_now, layer by layer; **(7.2)** which of those predictions a detector can falsify, and when; **(7.3)** the scorecard — zero-free-parameter passes set against the open gaps, with no aggregate score because an aggregate would hide the structure.

---

## 7.1 Observational outputs of the single equation at τ_now

Each row ties an observable to its **spectral-moment layer** (which Seeley–DeWitt coefficient it descends from) and its **E-number** in atlas-03. Framework values are canonical (sourced as noted); observational values are comparison anchors only.

### 7.1.1 The a₀ layer — dark energy and the cosmological constant

The zeroth spectral moment $a_0$ is the cosmological term. It is a *different* moment from gravity ($a_2$) — this separation is the framework's structural answer to "why is the CC not the Planck density": the two scales are not the same coefficient (per `phononic-framing.md`, the LCDM conflation "vacuum energy = gravity" is a category error here).

| Observable | Layer / E-no. | Framework value (canonical) | Comparison anchor | Status |
|:-----------|:--------------|:----------------------------|:------------------|:-------|
| **w₀** (DE equation of state, z=0) | a₀ / **E28, E44, E45** | **w₀ = −0.918** (`w0_FW`, Volovik partition + effacement Γ_eff = 0.99970; S58) | DESI DR2: w₀ = −0.752 ± 0.057. DES-Dovekie+DR2+Planck/ACT/SPT: w₀ = −0.803 ± 0.054 (arXiv:2511.07517v3) | LIVE. Post-Dovekie σ-distance **2.130σ** (was 2.91σ vs DR2-DESY5) |
| **w₀** (branch-iv alt.) | a₀ / **E44 / R_842** | **w₀ = −0.842454** (`w0_FW_R842`, substrate-compaction branch, S83/S84) | same | Post-Dovekie **0.731σ** (was 1.59σ). W0-workshop promotion **conditional on DESI DR3 PASS** |
| **wₐ** | a₀ / four-fold lock | **wₐ = 0** (structural four-fold lock) | DESI DR2: wₐ = −0.73 ± 0.25; Dovekie: wₐ = −0.72 ± 0.21 | Post-Dovekie **3.429σ** — tension ADVANCED +0.51σ by σ-tightening at ~unchanged central value. The honest tension (see 7.3) |
| **CC closure ratio** | a₀ / **E45** | **ρ_vac(today)/ρ_obs = 1.032** (0.01 OOM; CC_OOM = 115.5) | observed Λ | PASS (DILUTION-CC-66, Scenario B). Sole-surviving CC-closure mechanism post-S66 |

**Substrate reading (a₀ layer).** Dark energy is *not* a quintessence field rolling in a potential — the clock constraint (E27) closes all rolling quintessence at 15,000× the atomic-clock bound. It is the **effacement residual**: the 0.03% leakage through the impedance mismatch Γ = 0.99970 between the Josephson-condensate sector and the GGE relic. The CC is the $a_0$ moment relaxing as ρ_vac ~ M_Pl² H²(t) (Volovik tracking vacuum, E44), which closes the notorious 114-OOM gap to 0.01 OOM *today* — reframing the CC "problem" as an expansion-history observable, not a fine-tuning. The DESI wₐ tension is the framework's sharpest live exposure: a four-fold structural lock predicts wₐ = 0, and the data is drifting toward wₐ ≠ 0. **This is binding, not cosmetic.**

> **Convention note (substrate-first translation).** w₀ has a dual canonical: `canonical_constants.py:w0_FW = −0.918` is the *structural* Volovik-partition value (four-fold lock, S58); branch-(iv) −0.842454 is the substrate-compaction reading promoted *conditionally* on DR3. The L_max-stability of w₀ is regulator-conditional: Zubarev L_max ∈ {5,10} → −0.918 (cell A1); L_max=12 → −0.635 (cell B2, quintessence regime). The DR3-class L_max-stability gates are convention-locked to the canonical-anchored convention (CAC) per `regulator-convention-lockdown.md` — w₀(L=10) ≡ −0.918 exactly by construction.

### 7.1.2 The a₂ layer — the CMB tilt sector (n_s, r, n_T, α_s)

The second spectral moment $a_2$ generates the Einstein–Hilbert action; the Goldstone/SA-correlator sector built on it sets the primordial tilt. These are the **acoustic signature of the GGE relic**, not thermal-equilibrium fluctuations.

| Observable | Layer / E-no. | Framework value (canonical) | Comparison anchor | Status |
|:-----------|:--------------|:----------------------------|:------------------|:-------|
| **n_s** (scalar tilt) | a₂/Goldstone / **E22–E24, E31** | **SCHEME-DEPENDENT** — see box. Canonical `ns_framework = 0.9595` (S65 BCS+1-loop); atlas-04 reports **0.9590** (sqrt-cutoff family); geometric tilt **n_s = 1 − 2ε_H = 0.9561** (`n_s_FW_exact`, S57/S73a) | Planck 2018: n_s = 0.9649 ± 0.0042 | LIVE. 1.40σ (0.9590) / **2.10σ** (0.9561) from Planck |
| **r** (tensor-to-scalar) | a₂ (tensor sector) / **E2 partition** | **r = 0.033** (S64 TENSOR-BURST + TENSOR-SCALAR, two independent PASS); CMB-transfer image **r_CMB = 0.011731522** (`r_CMB_framework`, S83 G46) | BICEP/Keck: r < 0.036 (2σ) | PASS (within BK 2σ). Dual-pathway: Path-H 0.00745 vs Path-C 0.0117 |
| **n_T** (tensor tilt) | a₂ (transit-scale) / **E (NT-BLUE)** | **n_T(transit) = +0.468** (S65 NT-BLUE PASS, at f_transit = 8.55×10³⁷ Hz); **n_T(k_CMB) = −3.02×10⁻³** (S66 TENSOR-TRANSFER) | slow-roll consistency −r/8 | Blue tilt LOCALIZED at transit scale; CMB-scale tilt is standard slow-roll. 54.04 decades separate the scales |
| **α_s** (running of n_s) | a₂/a₄ ratio / **E48, E23(superseded)** | **DUAL (scale, channel)** — see box. Substrate-distance running **α_s^substrate = −0.08587279** (`alpha_s_substrate_distance_1`); Goldstone-pivot running **α_s^pivot ≈ 0** (`alpha_s_pivot_goldstone`) | Planck 2018: α_s = −0.0045 ± 0.0067; ACT DR4+Planck (Aiola 2020): +0.0023 ± 0.0063 | **RESOLVED S93 W7-1**: pivot image +0.67σ **consistent**; substrate-distance is a ~34σ-reach CMB-S4/CMB-HD prediction |

> **GAP — n_s scheme-dependence (Window-7 / FUNCTIONAL-SELECT-67, OPEN).** The framework's n_s is **conditional on the choice of spectral cutoff function f(x)**. The ε_H slow-roll parameter *sign-flips* between the sqrt(x) cutoff (red tilt, ε_H drives +0.022 Mellin-slope) and the zeta-a₄ cutoff (blue tilt, −0.045); the n_s range across three cutoffs spans 0.164 (S66 CUTOFF-NS-66 FAIL). The canonical reportable is n_s = 0.9590 (sqrt family, S65) / 0.9561 (geometric 1−2ε_H), but **which spectral functional generates the physical n_s is not closed** — Window-7 (`atlas-05`) is the open gate, bracket-FAIL if no functional family lands n_s ∈ [0.9550, 0.9700]. I flag this as the single most important *internal* under-determination touching CMB data. It is honest to say: the framework predicts a red tilt of the right magnitude IF f(x)=sqrt(x); the cutoff-selection is unsolved.

> **α_s — the most-misread row, now structurally resolved.** The naive statement "α_s = −0.0859 vs Planck −0.0045 is a 12σ tension" is **wrong as a single-label conflation** (per `phononic-framing.md §"Scale-and-channel-tagging"`). The substrate carries **TWO scale-separated α_s observables**: (a) a substrate-distance running −0.08587279 at the s=3 Mellin pole, evaluated INSIDE the Brillouin zone at O(M_KK), FI-class regulator-invariant across the 5-regulator atlas, sign-walled negative by spectral-action monotonicity; and (b) a Goldstone-pivot running ≈ 0 (P_∇φ = K²·K⁻² = K⁰ transported to the CMB pivot, machine-zero 8.4×10⁻¹⁵). **Which one Planck measures is set by a single computable homogeneity degree deg(T_{BZ→pivot}).** S93 W7-1 RESOLVED this: deg = +2 (NON-SCALAR), so the −12.146σ "tension" was the *scalar-transport leaf*, now FALSIFIED — the −0.0859 value relocates OFF the Planck pivot to the CMB-S4/CMB-HD substrate-sensitivity channel (~34σ-reach falsifier). On the matched channel, **the pivot image ≈0 sits at +0.67σ from Planck — consistent**. This is not a tension defined out of existence; it is a substrate-distance prediction relocated to its correct detector channel, leaving a genuine ~34σ falsifier at CMB-S4. (Historical: `alpha_s_inflation_framework = −0.068968` was the pre-Route-B estimate; superseded by the Sage-QQ bit-exact n_s² − 1 at S89 W7a.)

**Substrate reading (a₂ layer).** The CMB tilt is not "density perturbations in expanding space." It is the **interference pattern of post-transit GGE acoustic excitations** — the SA-correlator (E22) and Goldstone propagator (E20) mixed convexly (E24), then mapped through the load-bearing scale relation K_fabric = k_CMB·e^N/M_KK (E31). The decisive conditional gate is E31 (EFOLD-MAPPING-52): viable n_s requires K < 0.087 M_KK, needing ≥ 3.1 e-folds. The tensor sector partitions into B1/B2 substrate eigenvalue modes, giving the Path-H/Path-C dual r-prediction that LiteBIRD will discriminate.

### 7.1.3 The a₄ layer — the Higgs (fiber sector)

The fourth spectral moment $a_4$ carries Yang–Mills + the Higgs quartic. The Higgs is the **transverse oscillation of the fiber embedding** (the |S|² mode), with its mass set by KK-threshold corrections at the Jensen-deformed fiber.

| Observable | Layer / E-no. | Framework value | Comparison anchor | Status |
|:-----------|:--------------|:----------------|:------------------|:-------|
| **m_H** (Higgs mass) | a₄/fiber | **m_H ≈ 127.5–131.8 GeV** (Aitken-Gaussian, S62-S66, KK threshold to \|S\|² fiber mode); BCS-threshold route ≈ 129 GeV | PDG: m_H = 125.25 ± 0.17 GeV (`m_H_obs` = 125.1) | PASS-class — within ~2–5% from zero geometric free parameters. **Caveat below.** |

> **GAP / caveat — m_H route-dependence.** The clean, headline-worthy statement is **m_H ≈ 127.5 GeV from KK threshold corrections, within ~2% of the measured 125.25 GeV with zero adjustable parameters** — this is a genuine zero-free-parameter near-hit (see 7.3). But fidelity requires the caveat: the value is route-dependent. S62–S66 Aitken–Gaussian gives 127.5–131.8 GeV; the zeta-regulated route (HIGGS-ZETA-67) gives 138.5 GeV (excluded); and an S84 bi-criterion μ_BC fit returned 188 GeV and was flagged **ACCOMMODATION** in the falsifier-rigor registry (a fit, not a prediction). The defensible canonical headline is the KK-threshold band 127.5–131.8 GeV; I do **not** cite the μ_BC-fit value as a prediction. PRELIMINARY on the precise central value pending a single canonical Higgs-mass route.

### 7.1.4 Dark matter — the Leggett-channel GGE quasiparticle (E47)

Dark matter is not a thermal relic WIMP. It is the **Leggett-mode collective excitation** of the vacuum variable — inter-band coherence δq fluctuations, CPT-neutral, non-annihilating (σ/m = 0 exactly, N_pair = 1).

| Observable | Layer / E-no. | Framework value (canonical) | Comparison anchor | Status |
|:-----------|:--------------|:----------------------------|:------------------|:-------|
| **Ω_DM h²** (Leggett-only) | a₂ (Leggett gap) / **E47, E29** | **Ω_DM h² = 0.120** (Leggett-only = 0.03985 × 3.010; Q_Leggett = 670,000) | Planck: Ω_c h² = 0.1186 ± 0.0020 | **PASS, 0.7σ (0.6%)** (Door-S66-Leggett, 5 channels PASS) |
| **f_DM** | a₂ / E47 | **f_DM = 0.947** (S65, graph-gapped Goldstones) | — | full-DM route (Ω_DM h² = 0.400) **excluded at 260σ**; Leggett-only is the surviving channel |
| **σ/m** (self-interaction) | E29 | **σ/m = 0 exactly** (N_pair = 1) | Bullet Cluster: σ/m < 1.25 cm²/g | PASS (structural) |
| **m_WDM-equiv / T(k)** | E29 | m_WDM ≈ 10²⁰·⁴ keV; T(k) = 1.0000 at all observable scales | Lyα: m_WDM > 5.3 keV | PASS (19 OOM margin); phononic DM is effectively CDM for all LSS |

**Substrate reading (DM).** The relic is the δq oscillation of the vacuum variable q around q₀ — a two-fluid collective mode that is essentially undamped (Q = 18.6, Z = 0.972, Lorentzian lineshape, LEGGETT-SPECTRAL-66 PASS). The DM-to-DE ratio is set by the ratio of two gaps, ε = Δ_Leggett/Δ_Josephson ≈ 0.005–0.011 (E47). It is a Type-F single-summand central-projection trace — algebra-INVARIANT, mechanically evaluable (per `mechanical-closure-discipline.md §"Layer-separability carve-out"`). The honest constraint: the full-DM route over-closes at 260σ; only the Leggett-*only* channel passes, requiring the BA phonons to decay before z ~ 3400 (z_eq = 3425, 0.88σ, Z-EQ-CHECK-66 PASS).

### 7.1.5 σ₈ — structure-growth normalization

| Observable | Layer / E-no. | Framework value (canonical) | Comparison anchor | Status |
|:-----------|:--------------|:----------------------------|:------------------|:-------|
| **σ₈** | a₂ (growth) / **E33** | **σ₈ = 0.799** (zero-free-parameter; O-Z rigid); growth-factor variant **0.793** (S59) | Planck: σ₈ = 0.829 ± 0.014 (registry); lensing ~0.76 ± 0.03 | **VIABLE** — sits *between* Planck and weak-lensing. PASS-class |

**Substrate reading (σ₈).** σ₈ = 0.799 is a zero-free-parameter prediction landing in the gap between the high (CMB-inferred) and low (lensing) values — i.e., the framework predicts a value consistent with a *partial* resolution of the σ₈ tension direction. f·σ₈(z) differs from LCDM by 3.9–4.1% at z = 0.3–0.7 with a systematic negative sign (GROWTH-FACTOR-59) — a coherent, correlated discriminant driven by the single deviation w₀ − (−1) = 0.082, not an independent knob.

---

## 7.2 Falsifier anchors — which predictions are decisive, and when

These rows are the live falsifier inventory I maintain as sole writer (`falsifier-master-inventory.md`). I report the **decisive** channels, their detectors, and the live-watch envelopes. The discipline (per `evoi-prioritization.md`): a prediction's falsifier weight is set by its detector reach and the σ-separation from the null, not by counting predictions.

### 7.2.1 The decisive near-term channels (2026–2035)

| Inventory row | Observable | Decisive detector | Live-watch envelope | What a detection/null does |
|:--------------|:-----------|:-------------------|:--------------------|:---------------------------|
| **#1** | **w₀** | **DESI DR3** (window opens 2026-04-23) | R_842 = [−0.94, −0.88]; branch-iv −0.842454 | DR3 is the **R_842 binding instrument**. Adjudicates Volovik-partition (−0.918) vs substrate-compaction (−0.842454). Hard pre-commitment locked (S84 lockouts A–F) |
| **#2** | **r** (dual-function) | **BICEP/Keck Array 2026** → **LiteBIRD 2030** | [0.005, 0.015]; r_CMB target 0.01173 | (i) live-watch envelope; (ii) Path-H (0.00745) vs Path-C (0.0117) discriminator — LiteBIRD **4.250σ decisive** via the n_T = −r/8 consistency relation; BK-Array 2026 1.417σ marginal |
| **#3** | **α_s** (substrate-distance channel) | **CMB-S4 2030** (σ_α ≈ 2.3×10⁻³) → **CMB-HD 2035** (σ_α ≈ 1.1×10⁻³) | substrate-distance −0.08587279 at the substrate-sensitivity channel | ~34σ-reach falsifier of the s=3 Mellin-residue identity at the *matched* channel. Pivot channel (≈0) is +0.67σ consistent — NOT the falsifier. An opposite-sign reading at substrate-sensitivity falsifies the n_s²−1 identity |
| **#7** | **CGWB ρ_AC** | **LISA ~2034+** (f_pivot = 3 mHz) | (A) acoustic band 11 OOM above LISA-PLS vs (C) Companion-null 8.299×10⁻⁵⁸ | **FLAGSHIP-DECISIVE** (S85 W1a-7, SNR = 1.68×10¹³). LISA detection at Ω_GW > 10⁻¹² over 4-yr falsifies the (C) class; non-detection falsifies (A). 47.081-OOM (A)/(C) split |
| **#12** | **A_s** | CMB-S4 / CMB-HD | band 3.11×10⁻⁹ → 4.27×10⁻⁹ (ε_pivot-sensitive) | band-cited not point-cited until ε_pivot resolves (W5a P3 carry-forward). Planck A_s = (2.10 ± 0.03)×10⁻⁹ |
| **CF-35** | **3He-B cocycle ratio** | **Aalto LTL / Lancaster MCT-3**, 2028–2029 | lab(F₁)/lab(F₂) = 7.324992 ± 1% (→ ±0.1% substrate-natural) | Pillar V superfluid-lab falsifier, **structurally orthogonal** to the CMB channels. (Δ_B/Δ_A)^p cancellation makes the ratio lab-conversion-INDEPENDENT |

### 7.2.2 Detector-decisive timeline (consolidated)

- **2026** — BICEP/Keck Array (r, σ_r ≈ 0.003); **DESI DR3** (w₀, wₐ — the R_842 binding event).
- **2027–2028** — DESI DR4 (σ(wₐ) ~ 0.12).
- **2030** — LiteBIRD (n_T B-mode; **GEOMETRIC FLOOR** for the transit-scale signal — note the 54.04-decade k-separation means LiteBIRD probes k_CMB, where the transit-scale blue tilt is NOT directly detector-comparable; it is the slow-roll consistency relation that discriminates Path-H/Path-C); CMB-S4 commissioning (α_s, f_NL, β_s).
- **2034+** — **LISA** (Ω_GW at 3 mHz — flagship-decisive).
- **2035** — CMB-HD (α_s ≥ 30σ reach on the substrate-distance channel).

### 7.2.3 What is decisive vs what is suggestive (the ranking)

1. **DESI DR3 on w₀/wₐ** — decisive THIS YEAR. The wₐ = 0 four-fold lock is the framework's most exposed prediction; DR3 either relieves the 3.4σ wₐ tension or sharpens it past the breaking point. Binding instrument, hard pre-commitment.
2. **LISA on the CGWB** — flagship. An 11-OOM (A)/(C) discriminator at SNR ~ 10¹³ is the single cleanest yes/no the framework offers; nothing in LCDM predicts the acoustic-class spectral density at 3 mHz.
3. **α_s at CMB-S4/CMB-HD** — the first multi-σ falsifier at the *substrate-sensitivity* channel (~34σ reach). The signed substrate-distance running is structural (sign-walled by monotonicity); an opposite sign falsifies the identity.
4. **r / n_T at BK-Array → LiteBIRD** — Path-H vs Path-C discrimination at 4.25σ by 2030.

---

## 7.3 The honest scorecard

**No aggregate metric.** I report no PASS/FAIL ratio and no "master gate" (per `feedback_reporting-framing.md`, `epistemic-discipline.md`). A count of passes proves nothing; the structure is what matters. What follows is the structure: zero-free-parameter passes (genuine evidence) on one side, open gaps (genuine constraints) on the other.

### 7.3.1 Zero-free-parameter passes — these ARE evidence

Each of these emerged from $D_K$ with **no adjustable cosmological parameter**. A prediction landing near data from zero free parameters across a wide prior predictive range is Bayesian evidence with a large likelihood ratio — it is emphatically **not** "case unchanged":

- **Ω_DM h² = 0.120 at 0.7σ (0.6%) from Planck** — from the ratio of two collective-mode gaps. The relic abundance is normally a tuned thermal cross-section; here it is a geometric gap ratio. (E47)
- **CC closure ρ_vac/ρ_obs = 1.032 (0.01 OOM)** — the 114-OOM cosmological-constant gap closed to 1% by the Volovik tracking-vacuum relaxation law, with zero tuning. (E45)
- **σ₈ = 0.799, between Planck and lensing** — zero-free-parameter, landing in the tension gap with the correct sign of deviation. (E33)
- **m_H ≈ 127.5 GeV (KK threshold), within ~2% of measured** — the Higgs mass from fiber geometry, no Higgs-sector free parameter. (a₄ layer; caveat 7.1.3)
- **r = 0.033 within BICEP/Keck 2σ; σ/m = 0 exactly; T(k) = 1 at all LSS scales** — tensor amplitude, DM collisionlessness, and transfer function all structural.

The joint statement is the strong one: the chance that one randomly chosen internal geometry reproduces the relic abundance AND the CC scale AND σ₈ AND the Higgs mass simultaneously is the *product* of the individual improbabilities, not their average. That product is what makes the endpoint evidential.

### 7.3.2 Open gaps — these are genuine constraints, reported as boundaries

- **wₐ = 0 vs DESI (3.429σ post-Dovekie, ADVANCING).** The four-fold structural lock predicts wₐ = 0; the data is drifting away. This is the framework's sharpest live exposure and DESI DR3 (2026) is the binding test. Honest: if DR3 confirms wₐ ≠ 0 at ≥ 3σ, the four-fold lock is in serious trouble (note: a strong wₐ ≠ 0 also excludes LCDM, so the discriminant is FW-vs-Quintom, not FW-vs-LCDM).
- **n_s scheme-dependence (Window-7 / FUNCTIONAL-SELECT-67, OPEN).** n_s ∈ {0.9561, 0.9590, 0.9595} depending on the spectral cutoff f(x); ε_H sign-flips between sqrt and zeta-a₄. The framework gives a red tilt of the right magnitude IF f(x) = sqrt(x), but the functional selection is unsolved. The decisive gate E31 (EFOLD-MAPPING-52) is CONDITIONAL.
- **α_s at the substrate-sensitivity channel (~34σ-reach, awaiting CMB-S4).** Resolved as consistent (+0.67σ) at the pivot; the substrate-distance value is a clean falsifier *waiting for the detector*. Not a current tension — a pre-registered future test.
- **m_H route-dependence.** The KK-threshold band (127.5–131.8 GeV) is the defensible headline; the zeta route (138.5 GeV) is excluded and the μ_BC route (188 GeV) is an ACCOMMODATION, not a prediction. A single canonical Higgs-mass route is the open hygiene item.
- **A_s band, not point** (3.11–4.27 ×10⁻⁹), pending ε_pivot (W5a P3).
- **Missing a(t).** The capstone's "to NOW" arc is, on the cosmological-history side, **not yet a closed scale-factor evolution**. The framework has w(z), the relic abundance, and the CC relaxation law, but a first-principles a(t) from the substrate (the Friedmann-level expansion history derived from $D_K$ rather than mapped onto FRW) remains a gap — the S74 W1-E "Friedmann is the wrong question" result is structural, not a weakness, but it does mean §7's endpoint is grounded in *observables at τ_now*, not in a derived a(t) trajectory connecting them. I flag this explicitly so the document does not overclaim a closed expansion history.

### 7.3.3 The category that is neither pass nor gap

The substrate *says* things observation does not yet address: the CGWB acoustic-class spectral density at 3 mHz (LISA-decisive but pre-detector), the 3He-B cocycle ratio 7.324992 (Pillar-V lab, 2028–2029), the n_T blue tilt at the transit scale (54 decades from any CMB detector). These are pre-registered predictions in regions no current instrument reaches — neither passes nor gaps, but **the forward edge of the falsifier inventory**.

---

## Consideration — the headline test of "the universe equation," and a caveat

**My pick for the headline test: LISA's Cosmic Gravitational-Wave Background discriminator (row #7).** Here is the reasoning, from an observational-priorities standpoint.

The capstone's thesis is that the *entire* universe collapses into one equation. The headline test should therefore be the one that is (a) a clean yes/no, (b) unique to *this* equation — not shared with LCDM or generic quintessence — and (c) decisive at a signal-to-noise that leaves no wiggle room. LISA's CGWB row is all three: the (A) acoustic-class spectral density sits **11 orders of magnitude** above the LISA power-law-sensitivity curve, against a Companion-null (C) at 8.299×10⁻⁵⁸ — a 47-OOM split, at SNR ~ 10¹³. Crucially, the acoustic-class CGWB is a *direct consequence of the transit physics* — the GGE relic forming from supersonic (Mach 13.75) passage through the van Hove fold — which is the part of the equation that has no LCDM analog at all. LCDM has no fold, no acoustic white hole, no GGE relic; it makes no prediction here. So a LISA detection in the (A) band is not just a pass — it is a signature of the *exflation mechanism itself*, the thing that distinguishes "spectral complexity grows inside each point" from "space expands." That is the headline-worthy claim: the one equation predicts a gravitational-wave background that the standard model of cosmology does not, and we will know by ~2035.

**Two caveats, in order of weight.**

1. **DESI DR3 (2026) is the more urgent test, even if LISA is the more spectacular one.** The wₐ = 0 four-fold lock is exposed *now* and the tension is *advancing* (3.4σ post-Dovekie). If I had to name the test most likely to move the framework's status in the next eighteen months, it is DR3 on wₐ — and it could move it *against* the framework. LISA is the headline; DESI DR3 is the cliff-edge. The capstone should be honest that the nearest decisive test is also the most dangerous one.

2. **The α_s row is the framework's best illustration of why "substrate-first" is not hand-waving — but only because of S93 W7-1.** Before the transport-degree resolution, this looked like a 12σ catastrophe. The resolution (deg(T_{BZ→pivot}) = +2, non-scalar) is a *genuine* structural result that relocated the −12σ off the pivot and left a +0.67σ consistency plus a ~34σ future falsifier. I want to be candid that this is exactly the move a critic will scrutinize hardest: relocating a tension by a scale-tagging argument can look like saving the phenomenon. The defense is that the transport degree is *computed* (the w(L_max)·κ(k) factorization, factorization_holds = False, two-pole deg = +2), not chosen — and it leaves behind a SHARPER falsifier (34σ at CMB-S4), not a softer one. A prediction that survives by *generating a new decisive test* is doing the opposite of saving the phenomenon. But the burden is on us to keep that computation airtight, because it is the row where the substrate-first methodology is most load-bearing and most contestable.

The endpoint, in one line: **the single equation, evaluated once at τ_now, hands us a relic abundance at 0.6%, a CC at 1%, a Higgs at 2%, a σ₈ in the tension gap, and a gravitational-wave background that LCDM cannot produce — with the wₐ four-fold lock as the live wager DESI is about to call.**
