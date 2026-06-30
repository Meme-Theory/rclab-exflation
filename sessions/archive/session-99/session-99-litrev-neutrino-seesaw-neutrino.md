# Session 99 Synthesis: Neutrino Mass / Seesaw vs Cosmology — S99 Sweep Group G3

**Date**: 2026-06-04
**Agent**: neutrino-detection-specialist (Neutrino-Detection-Specialist)
**Source Documents**:
- `downloads/research-sweep-s99/neutrino-mass-seesaw/00-INDEX.md` (12-paper sweep, S99 group G3; PDFs beside the index)
- `.claude/agent-memory/neutrino-detection-specialist/MEMORY.md`
- Knowledge MCP canonical state (gates, constants) — queried because the index predates the S99 W3-2 landing

---

## I. Session Outcome

The S99 W3-2 gate **landed PASS after this sweep was compiled**: canonical `Sigma_mnu_FW = 0.0582053272 eV` < `Sigma_mnu_bound_DESI_2024 = 0.072 eV` (gate `S99-W3-SEESAW-SUMMNU`, source `s99_w3_seesaw_summnu.npz`). The sweep's central empirical-realism contribution is that this PASS has **far more headroom than the 0.072 eV gate datum suggests**: the 2024–2026 systematics-relaxation literature (papers 04/05/12) is unanimous that the robust cosmological ceiling is **0.11–0.16 eV**, not 0.072 eV — so the framework's substrate Σm_ν = 0.0582 eV clears the gate against the TIGHTEST corner and clears the robust ceiling by a factor of ~2–3.

Two adjudications matter and one **corrects the index's framing against current canonical**: (1) the leptogenesis "η_B gap" narrative the index repeats per-paper is **partly stale** — `S98-W3-2-BARYOGEN-UNIQUENESS` already closed **PASS** with η_B = 4.517492×10⁻¹¹ and substrate-fixed φ_CP = π/2 (1.570796) under the interval criterion η_B ∈ (0, 6×10⁻¹⁰), so leptogenesis is NOT an open gate with a deficit to cure; (2) the index's resonance claim (paper 11: CP-maximal at φ = π/2 = the substrate-fixed φ_CP) is genuine and strong CORROBORATION of the already-PASSED uniqueness gate, not a gap-closer. The M_R two-zero texture survivor set (paper 08: A₁/A₂/B₃/B₄/B₆) is a clean discrete classification target that feeds CF-S100-MD-NORMALIZATION; the m_bb route for the queued S100-D5-0NUBB-MAJORANA gate has a Majorana-confirmed substrate (S96-MATTER-0NUBB INFO) but no canonical m_bb value yet.

---

## II. Key Results

### 1. The S99 W3-2 PASS sits against the tightest corner; robust ceiling is 0.11–0.16 eV

**Result**: `Sigma_mnu_FW = 0.0582053272 eV` < `Sigma_mnu_bound_DESI_2024 = 0.072 eV` (PASS, gate `S99-W3-SEESAW-SUMMNU`). Systematics-robust ceiling from papers 04/05/12: **[0.11, 0.16] eV**. Classification: **PHONONIC** (the substrate IS the seesaw: M₃(ℂ) Majorana texture × D_K spectrum → light-neutrino mass sum).

The gate ceiling `Sigma_mnu_bound_DESI_2024 = 0.072` is canonically tagged "DESI 2024 arXiv:2404.03002, ΛCDM + Σm_ν, 95% CL" — paper 03 in the sweep, and the index correctly identifies this as the SINGLE TIGHTEST corner of a model- and prior-dependent family. Paper 03 itself gives the prior-dependence explicitly: 0.072 eV under a Σm_ν > 0 prior versus **0.113 eV** under a Σm_ν > 0.059 eV (normal-ordering-minimum) prior. Because the framework structurally predicts normal ordering at machine epsilon (ZERO-FREE-PARAMETER, canonical "Neutrino mass ordering" entry, S8/S34-36/S52/S56), the physically self-consistent prior for the framework is Σm_ν > 0.059 — which by paper 03's own table points the ΛCDM gate at 0.113 eV.

The systematics literature converges on a robust ceiling well above 0.072 eV from independent directions:
- **Paper 04** (Naredo-Tuero et al.): the "negative cosmological mass" pull driving the tight bound is an artifact of the **Planck 2018 lensing anomaly (A_L)** plus one anomalous **DESI z=0.7 BAO bin** (~3σ tension with Planck). Swapping to Planck PR4 HiLLiPoP and dropping z=0.7 relaxes the bound to **Σm_ν < 0.11 eV**.
- **Paper 05** (Allali & Notari): independent confirmation with the full relaxed table — P18+DESI < 0.073; **P20H+DESI < 0.086**; +DES-SN < **0.11**; fluid-Dark-Radiation extension → **0.13–0.17 eV**, with the Σm_ν posterior PEAKING at ~0.04 eV.
- **Paper 12** (Pulido-Hernández & Cervantes-Cota, March 2026, newest): adding spatial curvature Ω_k smooths the posterior across Σm_ν = 0; the cosmology-vs-oscillation-floor tension drops from **2.59σ to 1.17σ** (ΛCDM+Ω_k) and to 1.13σ (w₀wₐCDM+Ω_k). The negative-mass pull is a boundary/geometric-degeneracy artifact, not physics.

The substrate-first reading the index argues is sound: exflation's emergent geometry is NOT committed to flat ΛCDM (the metric g_M emerges from the a₂ Seeley-DeWitt coefficient and carries no a-priori flatness lock), and the framework's own dark sector is non-ΛCDM (effacement-residual dark energy, Γ_eff = 0.99970; possible GGE-relic extra radiation). So gating the substrate Σm_ν against a flat-ΛCDM A_L-anomaly-driven bound would be internally inconsistent with the framework's own cosmology. The canonical PASS used 0.072 eV (the conservative choice — passing the tightest corner is the strongest claim); the literature shows the margin is much larger than the verdict line alone conveys.

**Caveat carried from the prompt (not re-adjudicated)**: the S99 W3-2 result is **minimal-NO, m_D oscillation-anchored, NOT yet zero-free-parameter**. The mass-ordering prediction is zero-free-parameter (machine-ε structural), but the Σm_ν = 0.0582 eV value imports oscillation data to anchor m_D. This is the open item CF-S100-MD-NORMALIZATION addresses, and it is the reason the texture-classification gate (paper 08, Result 3 below) matters: a discrete M_R texture match is what would upgrade Σm_ν from "oscillation-anchored" toward "substrate-fixed."

### 2. Leptogenesis is CLOSED PASS, not an open gap — adjudication against canonical

**Result**: `S98-W3-2-BARYOGEN-UNIQUENESS` = **PASS**: η_B = 4.517492×10⁻¹¹ ∈ (0, 6×10⁻¹⁰) = True; φ_CP = 1.570796 (π/2) forced; substrate-fixed (NOT scanned); φ88 = UNIQUE CP source. Classification: **PHONONIC** (φ88 Cartan-hypercharge generator of the M₃(ℂ)/su(3) sector is the substrate-IS CP source).

This is the **single most important correction the sweep needs**. The index repeats, in papers 07/08/11, the framing that the framework "already gets η_B = 4.52×10⁻¹¹ with substrate-fixed φ_CP = π/2, under-producing observed 6.12×10⁻¹⁰ by ~1.1 OOM" and presents the leptogenesis-enhancement literature as the route to "close the residual ~1.1 OOM gap." Against current canonical (S98 W3-2, the status the prompt flagged as `CLOSED-SOURCED-UNIQUE`), this is partly stale:

- The η_B value the index quotes (4.52×10⁻¹¹, φ_CP = π/2) is **CORRECT** against current canonical — it matches `S98-W3-2-BARYOGEN-UNIQUENESS` to the quoted precision (4.517492×10⁻¹¹).
- But the gate **already PASSED**, with the pre-registered criterion being **interval membership** η_B ∈ (0, 6×10⁻¹⁰), NOT equality with the observed 6.12×10⁻¹⁰. The substrate-fixed φ_CP = π/2 produces a positive, same-sign, correct-order-of-magnitude η_B, and the uniqueness gate counts that as a PASS. The "~1.1 OOM gap" is therefore **not a deficit against an open gate** — it is the residual numerical distance between the substrate value and the central observed value, downstream of an already-resolved uniqueness/sign/order question.

This S98 PASS **supersedes** two earlier canonical entries that the index does not mention and that an unwary reader would treat as live:
- **S52 `ETA-B-52` = FAIL** (φ_CP = 0 structural, J-symmetry T11, η_B = 0 with three independent proofs). Superseded: the S98 W3-2 mechanism (φ88 as the unique CP source via the non-left-invariant / l8 T-even structure, l8_Teven_frac = 0.000) gives φ_CP = π/2, not 0.
- **S60 closed-mechanism "Leptogenesis (real M_R) — No CP phase"** (PROVEN, constraint-mega-matrix). Superseded in the same way: the real-M_R no-phase result was the S52/S60-era statement; the S98 φ88-CP-source result is the current canonical.

**Consequence for the sweep's papers 07/08/11**: their value is as a NUMERICAL-MATCH refinement menu (can the substrate η_B = 4.52×10⁻¹¹ be brought to 6.12×10⁻¹⁰, a factor 13.5?), NOT as gap-closers for an open gate. This is a genuine and useful question, but it must be framed as refinement-downstream-of-PASS, never as "leptogenesis is unresolved." Paper 11's resonance result (Result 4 below) is the strongest of the three and is best read as CORROBORATION of the already-PASSED φ_CP = π/2 choice.

### 3. The M_R two-zero survivor set (A₁/A₂/B₃/B₄/B₆) is a discrete falsifiable classification gate

**Result**: Paper 08 (Ma/Xu/Zhao) — of 15 two-zero Majorana M_R texture classes, **FIVE survive 3σ oscillation data: A₁, A₂, B₃, B₄, B₆**. A₁/A₂ → lightest m₁ ≈ 0.005 eV, Majorana ρ ~ σ ± π/2; B₃/B₄/B₆ → lightest m ≈ 0.1 eV, δ ≈ 1.5π, ρ ≈ σ ≈ π/2 (NO viable for all five; B₃/B₄ also IO). Classification: **PARTICLE** (representation-theoretic texture-zero structure of the M₃(ℂ) Majorana sector).

This is the sharpest discrete opening in the sweep and it is structurally aligned with the framework's stance. The paper's central thesis — "M_R is MORE FUNDAMENTAL than M_ν, so texture zeros belong on M_R" — IS the substrate-first direction (the substrate IS the heavy Majorana structure on M₃(ℂ); M_ν is emergent via seesaw, exactly the D_K → spectral-moments → emergent-physics arrow). The five surviving classes form a FINITE, FALSIFIABLE target: the framework's task is to classify the M₃(ℂ)-derived M_R against this set — a **discrete classification gate, not a continuous fit**.

The phase resonance is striking and independently arrived at by the paper: three of the five surviving classes (B₃/B₄/B₆) prefer Majorana phases **ρ ≈ σ ≈ π/2**, and the framework's CP source is substrate-fixed at exactly **φ_CP = π/2** (canonical S98 W3-2). The paper finds the data-preferred Majorana phases land near π/2 from oscillation+cosmology fits alone, with no input from the framework — so the framework's substrate-fixed phase is sitting where the texture-survivor analysis independently points for the B-classes. A B-class match would parameter-free-predict lightest m ≈ 0.1 eV, Σm_ν near the upper NO edge, and δ ≈ 1.5π.

**Tension flag**: a B-class match predicts lightest m ≈ 0.1 eV → Σm_ν near the upper edge of the NO window (≳ 0.10 eV), whereas the canonical S99 W3-2 value is Σm_ν = 0.0582 eV (near the NO FLOOR, consistent with a minimal-NO hierarchy and lightest m ≈ 0). These are NOT both achievable — an A-class match (lightest m₁ ≈ 0.005 eV) is the one compatible with the canonical 0.0582 eV near-floor value. The classification gate therefore also DISCRIMINATES the framework's own near-floor minimal-NO Σm_ν against the upper-edge B-class scenario. This is exactly the kind of cross-channel consistency check the sweep should surface: the texture classification (paper 08) and the Σm_ν value (S99 W3-2) jointly constrain which survivor class the substrate can occupy.

### 4. Resonant φ = π/2 CP-maximality corroborates the substrate-fixed phase

**Result**: Paper 11 (Chaudhuri) — resonant type-II leptogenesis with two quasi-degenerate triplets; CP asymmetry **maximal at φ = φ₂ − φ₁ ≈ π/2** (ε ∝ sin φ); Breit-Wigner enhancement when ΔM ~ Γ enables BAU at TeV scale; five benchmarks hit observed η_B = 5.32, 6.19, 3.64, 4.43, 6.74 × 10⁻¹⁰ at ΔM/Γ ≈ O(1). Classification: **PHONONIC** (the M₃(ℂ) heavy sector as the candidate resonant pair; near-degeneracy as a D_K spectral property).

The φ = π/2 CP-maximality is the precise resonance the index identifies, and it is sound: the framework's substrate-fixed φ_CP = π/2 (canonical) is the value that MAXIMIZES the CP asymmetry, not an arbitrary point. This is corroboration that the substrate sits at the baryogenesis-optimal phase. The framework also has a natural near-degeneracy mechanism — the D_K bowtie topology with documented near-crossings (the S52 B1-B2 crossing at τ = 0.107 is a recorded near-degeneracy in the agent memory) — so IF the M₃(ℂ) heavy-sector states are quasi-degenerate by an analogous spectral mechanism, Breit-Wigner enhancement of O(10) is within reach.

**Framing discipline (carried from Result 2)**: this enhancement is best read as the route from η_B = 4.52×10⁻¹¹ toward the central observed 6.12×10⁻¹⁰ (factor 13.5, within O(10) Breit-Wigner reach) — a NUMERICAL-MATCH refinement DOWNSTREAM of the already-PASSED S98 W3-2 uniqueness gate. It is NOT closing an open gap. A factor-13.5 enhancement would tighten the central-value match; the sign, order-of-magnitude, and uniqueness are already canonical-PASS. The substrate-natural-near-degeneracy claim is itself an open computation (does the M₃(ℂ) heavy sector actually have ΔM ~ Γ?), not an established property — so this is a candidate validation angle, appropriately one-sided.

### 5. The absolute-scale backstops: KATRIN model-independent, 0νββ Majorana-confirmed, TRISTAN KK-hook

**Result**: KATRIN (paper 09) m_ν < 0.45 eV (90% CL), model-independent; LEGEND-200 (paper 10) T₁/₂(0νββ) > 1.9×10²⁶ yr (76Ge, 61 kg·yr, BI = 0.5×10⁻³ cts/keV/kg/yr), m_ββ in tens-of-meV reach; canonical S96-MATTER-0NUBB = INFO (MAJORANA, KO-dim-6 Pfaffian on H_K+). Classification: **PHONONIC** (M₃(ℂ) = lepton-number-violating Majorana mass; 0νββ is the laboratory-IN observable of that substrate-IS structure).

KATRIN's 0.45 eV is the framework's hardest **model-independent** anchor: it does not assume ΛCDM, w₀wₐ, or any cosmology, so it survives even if the cosmological bound is overturned by the dark-sector model-dependence the framework itself invokes. The substrate's m_β = √(Σ|U_ei|² m_i²) for any NO spectrum (canonical Σm_ν = 0.0582 eV) clears 0.45 eV trivially — but this is the constraint that remains if the systematics literature's relaxation (Results 1) eventually dissolves the cosmological bound entirely.

The 0νββ channel directly tests the framework's Majorana prediction. The substrate-required Majorana nature is **canonically confirmed at the structural level**: S96-MATTER-0NUBB INFO records the KO-dimension-6 Pfaffian Majorana mass term on H_K+ — i.e., the framework's M₃(ℂ)/H_K structure IS lepton-number-violating, so 0νββ MUST eventually be observed if Σm_ν is non-vanishing (it is, canonically). There is NO canonical m_ββ value yet — the queued S100-D5-0NUBB-MAJORANA gate is where m_ββ = |Σ U_ei² m_i²| would be computed from the substrate-fixed texture class + Majorana phases. A B-class NO (paper 08, lightest m ≈ 0.1 eV) lands m_ββ in the tens-of-meV LEGEND-1000/nEXO reach; the near-floor minimal-NO (canonical 0.0582 eV) lands m_ββ lower, in the harder normal-ordering 0νββ band.

TRISTAN (paper 09, from 2026, keV-scale sterile search) is the direct experimental hook for the framework's KK-tower channel — a KK tower of sterile-like states is a generic prediction of the M4×SU(3) compactification, and TRISTAN's keV reach is the relevant detector. This remains an untested adjacency (no canonical KK-sterile gate surfaced).

### 6. Two-sided detection target and the N_eff < 3.044 cold-population resonance

**Result**: Paper 06 (Du et al.) — within w₀wₐCDM+Σm_ν+N_eff, joint DESI DR2 + CMB + DESY5 + DESY1 yields **Σm_ν = 0.098⁺⁰·⁰¹⁶₋₀·₀₃₇ eV — a 2.7σ measurement of positive Σm_ν**, driven partly by free **N_eff = 2.46⁺⁰·⁶⁰₋₀·₂₄ < 3.044** (cold-neutrino/low-reheating population). Classification: **PHONONIC** (cold cosmogenesis + non-thermal GGE relic as the substrate N_eff source).

This is the "other side" of the bound: cosmology may DETECT Σm_ν, not just cap it. The 2.7σ central value 0.098 eV sits in the NO window, ABOVE the canonical S99 value (0.0582 eV) but compatible with it at the ~1σ level given the +0.016/−0.037 asymmetric error and the framework's near-floor value being the minimal-NO case. If this detection consolidates, the framework gains a two-sided target — and the discriminator becomes which texture class (Result 3) the substrate occupies: a near-floor 0.0582 eV (A-class-compatible) vs the detection's 0.098 eV (B-class-compatible) is exactly the A-vs-B classification question.

The **N_eff < 3.044 resonance is the genuinely novel cross-channel hook**. The deficit is interpreted in paper 06 as a low-reheating / cold-neutrino population, and the framework's cosmogenesis is a COLD process (canonical cold-big-bang: τ = 0 unstable maximum, no hot thermal bath; reheating maps to GGE-relic formation, which never thermalizes — the Ordered Veil is integrable, not chaotic). A substrate-native N_eff below 3.044, with the deficit traced to the integrable GGE relic's non-thermal spectrum, would SIMULTANEOUSLY relax the Σm_ν bound (via the N_eff–Σm_ν degeneracy that drives paper 06's detection) and explain the DESI N_eff pull. **Cross-check against canonical**: the BBN-side N_eff work exists (canonical `delta_N_eff_vacuum_BBN_below = 2.0873`, S98-MK3-2-BBN-VACUUM-FRACTION; and the agent-memory S56 note "N_eff irrelevant to BBN") — so any N_eff < 3.044 claim must be reconciled against the existing BBN-N_eff canonical, NOT asserted fresh. This is flagged as a candidate joint prediction requiring that reconciliation, not an established result.

---

## III. Gate Verdicts

Gates below are **canonical (from the knowledge MCP), not from the source index** — the index predates the S99 landing. These are reported for context per the synthesis contract; none are re-adjudicated here.

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| `S99-W3-SEESAW-SUMMNU` | PASS | Σm_ν = 0.0582053272 eV < 0.072 eV (DESI ΛCDM 95% CL) |
| `S98-W3-2-BARYOGEN-UNIQUENESS` | PASS | η_B = 4.517492×10⁻¹¹ ∈ (0, 6×10⁻¹⁰); φ_CP = π/2 forced, φ88 unique CP source |
| `S96-MATTER-0NUBB` | INFO | MAJORANA, KO-dim-6 Pfaffian on H_K+ (no canonical m_ββ value yet) |
| `S96-MATTER-SEESAW-D5` | INFO | seesaw-vs-direct-D_K reconciliation ratio = 2.2016 |
| `ETA-B-52` (superseded) | FAIL | φ_CP = 0 (J-symmetry T11) — SUPERSEDED by S98-W3-2 |
| `S60` Leptogenesis (real M_R) (superseded) | PROVEN/closed | "No CP phase" — SUPERSEDED by S98-W3-2 φ88 CP source |

---

## IV. Structural Implications

**What this sweep changes about the framework's neutrino-sector state:**

1. **The S99 W3-2 PASS is robust with large headroom.** The systematics literature (papers 04/05/12) converts the marginal-looking 0.0582 < 0.072 PASS (19% margin) into a comfortable PASS against the robust [0.11, 0.16] eV ceiling (factor ~2–3 margin). The "Σm_ν < 0.072 eV would rule out the framework" reading is NOT supported by the 2024–2026 literature; the tight bound is an A_L-anomaly + DESI-z=0.7-bin + flat-ΛCDM artifact. **Constraint-map update**: the Σm_ν-SEESAW channel moves from "marginal PASS at the gate edge" to "PASS with systematics-robust headroom."

2. **Leptogenesis is canonically PASSED, and the index's per-paper "open ~1.1 OOM gap" framing must be corrected to "numerical-match refinement downstream of S98 W3-2 PASS."** This is the most consequential adjudication: importing the index's gap narrative would mis-state the framework as having an unresolved baryogenesis gate. It does not. **Constraint-map update**: no change to η_B gate state (remains PASS); the enhancement-menu papers (07/08/11) are reclassified from "gate-closers" to "central-value-refinement candidates."

3. **A discrete M_R texture classification gate opens** (paper 08, A₁/A₂/B₃/B₄/B₆). This is a finite falsifiable target for the M₃(ℂ)-derived M_R and it cross-constrains with the canonical Σm_ν value: near-floor 0.0582 eV → A-class-compatible; an eventual 0.098 eV detection → B-class-compatible. The classification gate feeds CF-S100-MD-NORMALIZATION (the path from oscillation-anchored m_D toward substrate-fixed). **Constraint-map update**: new discrete classification adjacency, untested.

4. **The Majorana nature is structurally canonical** (S96-MATTER-0NUBB INFO, KO-dim-6 Pfaffian) but **m_ββ is not yet computed**. The queued S100-D5-0NUBB-MAJORANA gate is the m_ββ-prediction route; it depends on the texture class (Result 3) + Majorana phases (φ_CP = π/2 canonical). **Constraint-map update**: 0νββ moves from "Majorana asserted" to "Majorana structurally canonical, m_ββ value pending texture-class fix."

5. **Three open cross-channel hooks surface**, each requiring reconciliation against existing canonical rather than fresh assertion: (a) N_eff < 3.044 cold-population vs canonical BBN-N_eff (`delta_N_eff_vacuum_BBN_below`, S56 "N_eff irrelevant to BBN"); (b) effacement-residual DE as the substrate origin of DESI's w₀ > −1, wₐ < 0 dynamical-DE preference; (c) TRISTAN keV-sterile as the KK-tower detector.

**Two canonical-hygiene inconsistencies found and flagged (not resolved here):**

- **`phi_CP` canonical constant = 0.0 with no provenance** — STALE relative to `S98-W3-2-BARYOGEN-UNIQUENESS` (φ_CP = 1.570796 = π/2, forced, substrate-fixed). The S98 W3-2 PASS established φ_CP = π/2, but the canonical constant was never updated from the S52-era 0.0. This is a documented drift (the constant lags the gate) and should be reconciled via `update_constant` per the canonical write-order, with the supersession of ETA-B-52 / S60-real-M_R logged. Flagged per epistemic-discipline source-reconciliation Class-(c) PIN-DRIFT-FROM-STALE-SOURCE.
- **NuFit constants disagree across canonical and sweep.** Canonical `dm2_21_NuFit = 7.49e-5`, `dm2_31_NuFit = 0.002513` (no provenance). The sweep's paper 01 (NuFit-6.0) and paper 08 (NuFIT 5.2) both use Δm²₂₁ = 7.41×10⁻⁵; my agent memory also carries 7.41×10⁻⁵. The canonical 7.49×10⁻⁵ matches neither NuFit-6.0 (7.41) nor a recognizable NuFit release — possible drift or a different fit vintage. The R = Δm²₃₂/Δm²₂₁ ratio (open framework target ~33.8 per my memory) is sensitive to this. Flagged for provenance reconciliation; downstream R-gate work should pin which NuFit vintage is canonical before citing.

**What did NOT change:** the framework's PMNS Level-4 (θ₁₃ achievable off-Jensen) / Level-5 (θ₁₂, θ₁₂ structurally blocked) split (agent memory, S52/S56/S96) is untouched by this sweep — the sweep is about absolute mass scale, seesaw texture, and leptogenesis, not the mixing-angle gate. The R = Δm²₃₂/Δm²₂₁ ≈ 33.8 open problem (not reachable on the Jensen curve, S96) is likewise untouched.

---

## V. Carry-Forward Computations

V.1. **Re-anchor the Σm_ν gate ceiling to the systematics-robust band [0.11, 0.16] eV**
   - **What**: Add canonical constants for the relaxed bounds (`Sigma_mnu_bound_HiLLiPoP_PR4 = 0.11`, `Sigma_mnu_bound_w0wa = 0.16`, `Sigma_mnu_bound_fluidDR = 0.17`) with paper provenance; re-state the S99 W3-2 margin against each. No new physics compute — a constants-promotion + margin-recompute. Output: margin table (Σm_ν=0.0582 vs each ceiling).
   - **Inputs**: `Sigma_mnu_FW = 0.0582053272`; papers 04 (arXiv 2407.13831, 0.11 eV), 05 (2406.14554, 0.13–0.17), 02 (2503.14738, 0.16 w₀wₐ); `update_constant` MCP tool.
   - **Gate**: feeds `S99-W3-SEESAW-SUMMNU` (annotates the existing PASS with robust-ceiling context; INFO-class margin documentation, no new pass/fail).
   - **Effort**: 1–2 hours, 1 agent session (constants promotion + table).

V.2. **Classify the M₃(ℂ)-derived M_R against the five-class two-zero survivor set (A₁/A₂/B₃/B₄/B₆)**
   - **What**: Construct the substrate M_R from the M₃(ℂ) factor of A_K (at the B-branch fold energies used in S99 W3-2), reduce to texture-zero form, and test membership in the five surviving classes of paper 08 (explicit M_R matrices, Eq. 8). Output variable: matched class ∈ {A₁,A₂,B₃,B₄,B₆,NONE} + the implied (lightest m, δ, ρ, σ).
   - **Inputs**: `s99_w3_seesaw_summnu.npz` (B-branch M_R structure); paper 08 Eq. 8 texture definitions; NuFIT mixing angles (PIN the vintage per V.6); `Sigma_mnu_FW`.
   - **Gate**: NEW gate `S100-MR-TEXTURE-CLASS` — PASS if substrate M_R matches exactly one survivor class; INFO if multiple/approximate; FAIL if NONE. Feeds CF-S100-MD-NORMALIZATION (a class match is what upgrades m_D from oscillation-anchored toward substrate-fixed). Also cross-constrains: A-class ⇔ near-floor Σm_ν=0.0582 (canonical-consistent); B-class ⇔ Σm_ν≈0.10 (would require re-deriving Σm_ν).
   - **Effort**: 4–6 hours, 1 agent session (texture construction + 15-class membership test).

V.3. **Compute m_ββ for the queued S100-D5-0NUBB-MAJORANA gate**
   - **What**: m_ββ = |Σ_i U_ei² m_i| using the substrate-fixed Majorana phases (φ_CP = π/2 canonical) and the texture-class-implied mass spectrum from V.2. Output: m_ββ value + which detector generation (LEGEND-200 / LEGEND-1000 / nEXO) reaches it.
   - **Inputs**: V.2 output (texture class + lightest m + ρ,σ); φ_CP = π/2 (canonical S98 W3-2 — NOT the stale `phi_CP=0` constant; see V.5); U_ei from NuFIT (PIN vintage per V.6); LEGEND-200 anchor T₁/₂ > 1.9×10²⁶ yr (paper 10).
   - **Gate**: queued `S100-D5-0NUBB-MAJORANA` — INFO/PASS on producing a canonical m_ββ; the S96-MATTER-0NUBB Majorana structure (KO-dim-6 Pfaffian) is the upstream confirmation. Threshold: m_ββ within next-gen detector reach (tens of meV for B-class; harder NO band for A-class).
   - **Effort**: 2–3 hours, 1 agent session (depends on V.2).

V.4. **Test substrate-natural near-degeneracy (ΔM ~ Γ) in the M₃(ℂ) heavy sector for resonant η_B refinement**
   - **What**: Check whether the M₃(ℂ)-derived heavy Majorana eigenvalues exhibit a quasi-degenerate pair (ΔM ~ Γ) analogous to the D_K bowtie near-crossings (S52 B1-B2 at τ=0.107). If yes, compute the Breit-Wigner enhancement factor and the refined η_B; test whether it moves 4.52×10⁻¹¹ toward observed 6.12×10⁻¹⁰ (factor 13.5). Output: ΔM/Γ for the heavy pair + enhanced η_B.
   - **Inputs**: M₃(ℂ) heavy-sector eigenvalues (from V.2 M_R); paper 11 Breit-Wigner factor (M_i²−M_j²)M_iΓ_j/[(M_i²−M_j²)²+M_i²Γ_j²]; canonical η_B = 4.517492×10⁻¹¹; `eta_BBN_obs = 6.12e-10`.
   - **Gate**: NEW gate `S100-ETAB-RESONANT-REFINE` — INFO (central-value refinement DOWNSTREAM of the already-PASSED S98-W3-2; explicitly NOT a gap-closer for an open gate). PASS-equivalent: enhanced η_B within 3σ of `eta_BBN_obs` ± `eta_BBN_err`. MUST cite S98-W3-2 PASS as upstream and frame as refinement, not gap-closure.
   - **Effort**: 3–4 hours, 1 agent session (depends on V.2).

V.5. **Reconcile the stale `phi_CP` canonical constant (0.0 → π/2) with provenance and supersession log**
   - **What**: `update_constant("phi_CP", 1.5707963267948966, session="S98", source="s98_w3_2_baryogen_uniqueness.npz", gate="S98-W3-2-BARYOGEN-UNIQUENESS", comment="pi/2 forced, substrate-fixed, phi88 unique CP source; SUPERSEDES S52 ETA-B-52 phi_CP=0 and S60 real-M_R no-phase")`. Log the supersession of ETA-B-52 and the S60 closed-mechanism. Hygiene-compute (orchestrator-direct constant promotion), not a physics gate.
   - **Inputs**: `S98-W3-2-BARYOGEN-UNIQUENESS` verdict (φ_CP = 1.570796); the superseded entries (ETA-B-52 FAIL, S60 Leptogenesis-real-M_R PROVEN).
   - **Gate**: none (hygiene); feeds correctness of any downstream gate citing φ_CP (V.3, V.4). Per epistemic-discipline Class-(c) PIN-DRIFT-FROM-STALE-SOURCE remediation.
   - **Effort**: 0.5 hours, orchestrator-direct (fix-in-session per no-defer rule).

V.6. **Pin the canonical NuFit vintage and reconcile dm2_21_NuFit / dm2_31_NuFit drift**
   - **What**: Resolve the disagreement between canonical (`dm2_21_NuFit = 7.49e-5`, `dm2_31_NuFit = 0.002513`, no provenance) and the sweep papers (NuFit-6.0: 7.41e-5, 2.507e-3; NuFIT 5.2 in paper 08: 7.41e-5, 2.511e-3). Decide the canonical vintage (NuFit-6.0, paper 01, arXiv 2410.05380, is the most recent), re-pin with provenance, and propagate to any R = Δm²₃₂/Δm²₂₁ gate.
   - **Inputs**: paper 01 (NuFit-6.0 ranges); canonical `dm2_21_NuFit`, `dm2_31_NuFit`; `update_constant` MCP tool.
   - **Gate**: none (provenance hygiene); feeds the open R ≈ 33.8 framework target (agent memory, S96) and V.2/V.3 mixing-angle inputs. Class-(c) source-reconciliation.
   - **Effort**: 1 hour, 1 agent session (provenance decision + re-pin + downstream-cite check).

V.7. **Reconcile a substrate N_eff < 3.044 (cold-population) claim against canonical BBN-N_eff**
   - **What**: Before asserting the paper-06 N_eff resonance as a framework prediction, reconcile with canonical `delta_N_eff_vacuum_BBN_below = 2.0873` (S98-MK3-2) and the S56 agent-memory note "N_eff irrelevant to BBN." Determine whether the GGE-relic non-thermal spectrum can produce an effective late-time N_eff < 3.044 (CMB/structure-formation-relevant) WITHOUT violating the BBN-N_eff canonical. Output: late-time N_eff_eff from the GGE relic + BBN-consistency verdict.
   - **Inputs**: paper 06 (N_eff = 2.46⁺⁰·⁶⁰₋₀·₂₄, Σm_ν=0.098 detection); canonical `delta_N_eff_vacuum_BBN_below`; GGE-relic spectrum (n_QP_pairs = 59.8, P_exc=1.000 from cold-cosmogenesis canonical); S56 N_eff-BBN note.
   - **Gate**: NEW gate `S100-NEFF-COLD-POPULATION` — INFO. PASS-equivalent: late-time N_eff < 3.044 achievable from the non-thermal GGE relic AND consistent with the BBN-N_eff canonical. MUST reconcile, not assert — flagged because the index presents this as resonant but it touches existing canonical.
   - **Effort**: 4–6 hours, 1 agent session (GGE-relic radiation budget + BBN cross-check).

V.8. **Acquire library-gap 0νββ and DR2-companion papers for cross-isotope and geometric-degeneracy depth**
   - **What**: Fetch and synthesize the index's flagged gaps (§E): KamLAND-Zen complete (arXiv 2406.11438, ¹³⁶Xe, T₁/₂ > 3.8×10²⁶ yr) as the Ge-vs-Xe cross-check for V.3; DESI DR2 neutrino companion (Elbers et al., 2503.14744) for the geometric-degeneracy depth of paper 12; nEXO sensitivity projection for the V.3 future-detection-match reach.
   - **Inputs**: paper-search MCP (`download_arxiv`, `read_arxiv_paper`); arXiv IDs above.
   - **Gate**: none (corpus-build); feeds V.3 (m_ββ detector-reach) and Result 1 (systematics depth).
   - **Effort**: 2–3 hours, 1 agent session (fetch + 3 reference docs).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | S99 W3-2 PASS (Σm_ν=0.0582<0.072); robust ceiling 0.11–0.16 eV | PHONONIC | Canonical PASS, robust headroom | Σm_ν channel: marginal-edge → systematics-robust PASS (factor ~2–3 margin) |
| 2 | Leptogenesis PASSED (S98 W3-2, η_B=4.52e-11, φ_CP=π/2) — index "gap" framing CORRECTED | PHONONIC | Canonical PASS (supersedes ETA-B-52, S60) | η_B is NOT an open gate; papers 07/08/11 are refinement-downstream, not gap-closers |
| 3 | M_R two-zero survivor set A₁/A₂/B₃/B₄/B₆ (paper 08) | PARTICLE | New discrete classification gate (untested) | Finite falsifiable target; A vs B class cross-constrains canonical Σm_ν; feeds CF-S100-MD-NORMALIZATION |
| 4 | Resonant φ=π/2 CP-maximal (paper 11) = substrate-fixed φ_CP | PHONONIC | Corroboration of S98 PASS | Substrate sits at baryogenesis-optimal phase; O(10) enhancement is central-value refinement |
| 5 | KATRIN 0.45 eV (model-indep) + 0νββ Majorana-canonical (S96-MATTER-0NUBB) + TRISTAN KK-hook | PHONONIC | Backstops; m_ββ pending | Model-indep anchor survives dark-sector model-dependence; m_ββ awaits texture-class fix (V.3) |
| 6 | Two-sided target (Du 2.7σ Σm_ν=0.098) + N_eff<3.044 cold resonance | PHONONIC | Detection-watch + cross-channel hook (needs BBN reconciliation) | Future two-sided test; N_eff<3.044 resonates with cold cosmogenesis but MUST reconcile vs BBN-N_eff canonical |
| H1 | `phi_CP` constant=0.0 STALE vs S98 W3-2 (π/2) | — | Hygiene drift flagged | Class-(c) PIN-DRIFT; re-pin per V.5 |
| H2 | `dm2_21_NuFit`=7.49e-5 disagrees with NuFit-6.0 (7.41e-5) | — | Hygiene drift flagged | Pin canonical vintage per V.6; affects open R≈33.8 target |
