# S82 Mack Synthesis — Falsifier Campaign Inventory and Observational Roadmap

**Author**: katie-mack-cosmic-bridge
**Track**: observational-priority (S82 falsifier roadmap)
**Date**: 2026-04-18
**Source docs**: `sessions/archive/session-82/session-82-results-workingpaper.md` §§V.F, V.G, V.N, VI.D, VI.I, VI.J; `sessions/archive/session-82/session-82-OOM.md` §§II, III.A
**Convention**: all channels are spectral-moment signatures of D_K on the Jensen-deformed SU(3) substrate, probed by instruments. "Observable" denotes a substrate moment carried into a measurable channel by a specific GGE relay; "detector" denotes an experimental apparatus that samples that channel.

---

## I. Session Outcome

S82 registers five classes of sign-definite substrate-moment falsifiers and leaves two open tensions on the watchlist. Of the seven channels, **DESI DR3 binary rectangle** is the single highest-EVOI upcoming observation (EVOI ≈ 0.21, reach 2026-2027) — it closes two currently-open observables (w_0, w_a) in one binary SURVIVE/FAIL decision that moves P_obs_aligned either to 9/9 (if the DR3 point lands inside [-0.94,-0.88] × [-0.10,+0.10]) or to 5/9 (if either axis lands outside the rectangle). The four remaining observationally-reachable channels (sin²θ_W EW-closure, n_T sign, C_cons > 0.033, α_f_NL = 0) line up on a 2030-2040+ timeline. The **GW α-vs-γ discrimination** is theoretically decisive (29.6 OOM ratio) but 47-77 OOM below LISA at 1 mHz — it is dormant in the observational-priority tree until an ultra-high-frequency detector concept reaches the 10⁶-10⁸ Hz f_peak band.

Two caveats propagate forward:

1. **n_T scale-transfer caveat** (S66 TENSOR-TRANSFER-66, memory `project_s66_tensor_transfer`): the +0.468 BLUE tilt is localized at k_transit ≈ 54 decades above the CMB. At observable CMB scales the framework tensor tilt is `n_T(k_CMB) = -3.02e-3` — slow-roll-like RED. W3-9 treats the sign-definite BLUE statement as a structural discriminator; LiteBIRD would test the scale-transferred CMB-scale value, which is NOT BLUE under the framework's own transfer analysis. This weakens the "BLUE tilt is the distinguisher" claim against LiteBIRD unless a distinct k_transit probe is identified.

2. **A_s Branch provisionality**: the entire 7/9 count currently depends on W1-2 Branch-A PASS-F2 (A_s = 3.30×10⁻⁹, 1.57× Planck). If S83+ delivers a Branch-B LI-recovery re-verdict, the replacement-space pinned in W3-9 absorbs the re-roll — six adjacent observables are enumerated with sign-definite substitution chains, so the falsifier inventory does not collapse.

---

## II. Falsifier Channel Catalog

### II.A. α_f_NL = 0 across 5 decades k (W3-4)

**Framework prediction** (S82 §VI.D): f_NL^{GGE,fabric}(k) = 0.054702 exactly across k ∈ {10⁻⁴, 10⁻³, 10⁻², 10⁻¹, 10⁰} Mpc⁻¹ (W2-15 phase-alignment k-scan confirmed 0% variation across 5 decades).

**Substitution chain (direction)**:
- Step 1 (definition): α_f_NL := d ln f_NL / d ln k
- Step 2 (substitution): f_NL(k) = |f_NL^cell| · N_cells / E_pathB² with |f_NL^cell| set at the fold, k-independent
- Step 3 (simplification): only the dispersion phase k²·r_s·c_fabric / (2·ω_a·M_KK) introduces k-dependence; at CMB scales this is O(10⁻⁵¹) rad/mode
- Step 4 (direction): α_f_NL = 0 to machine precision (numerically verified ≤ 10⁻¹⁵ across the 5-decade span)

This is a **STRUCTURAL FLAT** prediction: the squeezing phase φ_squeeze is set once at the fold; the k-dependence of observables rides only on residual dispersion that is geometrically suppressed by k²/M_KK² at observable scales. Standard single-field inflation generically produces running f_NL via c_s(k), ε(k), η(k); a non-zero α_f_NL measurement at ≤ 10⁻² reach falsifies the GGE origin.

**Pre-registered threshold**: any detection of |α_f_NL| > 0.01 at 3σ.

**Detector / sensitivity trajectory**:
- Planck 2018: no meaningful constraint on scale-dependent f_NL (sigma ~ 0.04 on running, unconstrained at current precision)
- CMB-S4 (~2030, Abazajian et al. 2022 Science Book): σ(f_NL^equil) ≈ 5 amplitude; no primary α_f_NL deliverable (limited k-lever arm at CMB)
- SKA-era 21-cm intensity mapping (2035-2040+, Karagiannis et al. 2020 MNRAS 492 4045): σ(α_f_NL) ≈ 0.01-0.02 via bispectrum scale-dependence across l_max ~ 10⁵
- Reach mode: 21-cm bispectrum at high-k, post-reionization IM era

**Reach date**: 2035+ (SKA phase 2 full deployment, sensitivity build-up through 2040s)

**Current status**: FUTURE-ONLY. No existing survey constrains α_f_NL at decisive precision.

**EVOI**: 0.033 (P(decisive-by-2040) ≈ 0.30; |ΔP_obs_aligned| = 1/9 for null PASS). Rate-limited by SKA funding + atmospheric window + foreground mitigation.

---

### II.B. n_T > 0 BLUE tensor tilt (W3-9, S65)

**Framework prediction** (S82 §VI.I, Observable 4): sign(n_T^{framework}) = +1 at k_transit; opposite sign from single-field slow-roll n_T = -r/8 = -0.004125 (with r = 0.033).

**Substitution chain (sign direction)**:
- Step 1 (definition): n_T(k) := d ln P_T(k) / d ln k
- Step 2 (substitution): at k_transit the post-fold GGE tensor occupation squeezes with positive log-derivative driven by the H2 theorem's volume-preserving Jensen flow (S65 NT-BLUE-65)
- Step 3 (simplification): n_T(k_transit) = +0.468 (S65 numerical)
- Step 4 (direction): sign(+0.468) = +1, OPPOSITE to slow-roll sign(-0.004125) = -1

**CRITICAL CAVEAT (S66 TENSOR-TRANSFER-66 FAIL)**: the blue tilt is **localized at k_transit only** — 54 decades above the CMB. Scale-transfer to k_CMB yields n_T(k_CMB) = -3.02×10⁻³ (slow-roll-like RED). A LiteBIRD measurement samples k_CMB, not k_transit. Under the framework's own transfer analysis, the observable CMB-scale tensor tilt is NOT BLUE. The sign-definite "BLUE distinguisher" claim in W3-9 is at best a scale-localized structural prediction, not a CMB-observable falsifier.

**Pre-registered threshold**: a direct detection of n_T(k_CMB) > 0 at 2σ would falsify the S66 transfer analysis (not the BLUE-at-transit claim itself, which lives at inaccessible scales).

**Detector / sensitivity trajectory**:
- Current: BICEP/Keck 2021 (Ade et al. PRL 127 151301) constrains r < 0.036; no n_T constraint at sigma level
- LiteBIRD (JAXA L-class, launch projected 2032, Matsumura et al. 2014 JLTP 176 733): σ(r) ≈ 0.001, σ(n_T | r = 0.033 detected) ≈ 0.02 via spectral reconstruction across l ~ 2-200
- CMB-S4 (DOE/NSF, first light 2028, full 2030, Abazajian et al. 2022): σ(r) ≈ 5×10⁻⁴; n_T is secondary, sensitivity ~ 0.03-0.05 through joint analysis
- PICO (NASA probe concept, unfunded, >2035): σ(n_T) ≈ 0.02 target

**Reach date**: 2034-2036 (LiteBIRD launch + 4 yr analysis)

**Current status**: IN-PROGRESS (BICEP/Keck running, LiteBIRD build). No sigma-level n_T constraint yet.

**EVOI**: 0.056 (P(decisive-by-2036) ≈ 0.50; |ΔP_obs_aligned| = 1/9 for sign-PASS). Reduced EVOI because (a) S66 transfer caveat means the CMB-scale observable is not the BLUE sign prediction, (b) LiteBIRD launch risk moderate.

---

### II.C. C_cons = r + 8·n_T > 0.033 (W3-9)

**Framework prediction** (S82 §VI.I, Observable 5): C_cons^{framework} > 0.033 strict; single-field slow-roll consistency relation gives C_cons^{slow-roll} = 0 exactly.

**Substitution chain (strict inequality)**:
- Step 1 (definition): C_cons := r + 8·n_T
- Step 2 (substitution): r_framework = 0.033 (S64 TENSOR-BURST-64 two independent PASS); n_T at transit > 0 strict (S65 NT-BLUE-65)
- Step 3 (simplification): C_cons^framework = 0.033 + 8·(positive quantity) > 0.033
- Step 4 (direction): C_cons^framework > 0.033 > 0 = C_cons^slow-roll, strict lower bound by r alone

**CRITICAL CAVEAT** (same scale-transfer issue as II.B): at k_CMB the framework gives n_T(k_CMB) = -3.02×10⁻³, so C_cons(k_CMB) = 0.033 + 8·(-0.003) = 0.009 — STILL > 0 but below the 0.033 lower bound stated in W3-9. The W3-9 "> 0.033 strict" applies at k_transit; at k_CMB the observable bound is "> 0.009".

**Pre-registered threshold**: a joint (r, n_T) measurement with C_cons detected at > 2σ above zero falsifies standard slow-roll consistency; a measurement finding C_cons consistent with 0 (at σ ≤ 0.05) confirms standard inflation over the framework.

**Detector / sensitivity trajectory**:
- LiteBIRD + CMB-S4 joint (required for simultaneous r and n_T):
  - σ(r) ≈ 5×10⁻⁴ (CMB-S4 dominant)
  - σ(n_T) ≈ 0.02 (LiteBIRD dominant)
  - σ(C_cons) = √(σ_r² + 64·σ_nT²) ≈ 0.160 (verified via Python)
- Reach:  at σ(C_cons) ≈ 0.16, detection requires framework C_cons ≳ 0.32 for 2σ. Framework k_CMB value 0.009 is deeply below this — **NOT detectable via CMB alone at current projections**
- 21-cm tensor probes (post-2040 concept): could reach intermediate k where framework n_T is larger

**Reach date**: decisive distinction requires > 2040 unless an intermediate-scale tensor probe is developed.

**Current status**: FUTURE-ONLY; detection at k_CMB is sensitivity-limited below the framework signal.

**EVOI**: 0.050 (P(decisive-by-2040) ≈ 0.45; |ΔP_obs_aligned| = 1/9). Lower than II.B because C_cons requires joint measurement.

---

### II.D. DESI DR3 binary rectangle on (w_0, w_a) (W2-7-R3)

**Framework prediction** (S82 §V.G R3): binary SURVIVE/FAIL test
- w_0 SURVIVAL BAND: [-0.94, -0.88] (canonical w_0 = -0.918; offset lower 0.022 / upper 0.038, asymmetric per S73B W2-D σ_w0_scheme = 0.06)
- w_a SURVIVAL BAND: [-0.10, +0.10] (canonical w_a = 0.0 from S66 four-fold lock; ±0.10 is scheme uncertainty, not a prediction band)
- Absolute coordinates; no scenario conditioning; binary precedence.

**Substitution chain (decision rule)**:
- Step 1 (definition): E_survive ≡ (w_0^DR3 ∈ [-0.94, -0.88]) AND (w_a^DR3 ∈ [-0.10, +0.10])
- Step 2 (substitution): DR3 returns point (w_0^DR3, w_a^DR3) with covariance
- Step 3 (simplification): by DeMorgan, E_fail = (w_0 outside) OR (w_a outside)
- Step 4 (direction): binary, no continuous-tension override

**Current tensions** (before DR3):
- DESI DR2 central (w_0, w_a) = (-0.752, -0.730): both axes OUTSIDE; framework FAILS against DR2 center by 2.9σ on w_0 alone
- DR3 Sc.B forecast (LCDM-like) = (-0.918, 0.0): both axes INSIDE; framework trivially survives
- DR3 Sc.A forecast (DR2-like) = (-0.752, -0.730): both axes OUTSIDE; framework FAILS
- DR3 Sc.C forecast (intermediate) = (-0.850, -0.300): w_a outside; FAILS

**Pre-registered threshold**: registered and FROZEN at 2026-04-11 per S74 W4-Z closure. No post-hoc band adjustment; E2' permanence rule binds.

**Detector / sensitivity trajectory**:
- DESI DR1 (Adame et al. 2024 arXiv 2404.03002): σ(w_0) ~ 0.08, σ(w_a) ~ 0.31 (2.6σ DE hint)
- DESI DR2 (2025): σ(w_0) = 0.057, σ(w_a) = 0.25
- DESI DR3 (projected 2026-2027, per DESI collaboration public schedule): σ(w_0) ≈ 0.040, σ(w_a) ≈ 0.177 (S59 WA-ERROR-PROP-59 projection)
- Euclid (launched 2023, full analysis ~2029): σ(w_0)_Euclid+DESI ≈ 0.02
- LSST/Vera Rubin (first light 2025, 10-yr full ~2035): independent SN + WL channel

**Reach date**: 2026-2027 (DR3 FINAL release imminent)

**Current status**: PRE-REGISTERED FROZEN; activates on DR3 release. DR2 central already disfavors framework by 2.9σ on w_0 single-axis.

**EVOI**: **0.211** — HIGHEST. P(decisive-by-2028) ≈ 0.95; |ΔP_obs_aligned| = 2/9 (two gates close simultaneously). This is the single most informative observation on the framework's near-term horizon.

---

### II.E. GW α-vs-γ discrimination at 1 mHz (W2-6)

**Framework prediction** (S82 §V.F): Ω_GW(γ)/Ω_GW(α) = 4.249×10²⁹ at f = 1 mHz, where γ is the gravity-only reheat channel (T_rh = 1.691×10¹⁵ GeV) and α is the instanton-mediated subdominant additive (T_rh = 2.460×10⁸ GeV).

**Substitution chain (scaling)**:
- Step 1 (definition): Ω_GW^prod = α_GW · (Γ/m_τ)² · (m_τ/M_Pl_red)⁴, with Γ ∝ T_rh²
- Step 2 (substitution): Ω_GW^prod ∝ Γ² ∝ T_rh⁴
- Step 3 (MD-era dilution): Ω_GW^decay = Ω_GW^prod · (Γ/H_prod)^(2/3) ⇒ Ω_GW^peak ∝ T_rh^(16/3)
- Step 4 (f_peak redshift): f_peak ∝ T_rh^(1/3)
- Step 5 (Parker f³ tail): Ω_GW(f) ∝ Ω_peak · (f/f_peak)³ for f ≪ f_peak
- Step 6 (simplification): Ω_GW(1 mHz) ∝ T_rh^(16/3) · T_rh^(-1) = T_rh^(13/3)
- Step 7 (direction): (T_rh^γ / T_rh^α)^(13/3) = (6.875×10⁶)^(13/3) = 4.249×10²⁹ ⇒ Ω_GW^γ ≫ Ω_GW^α

**Observational status**:
- Ω_GW^α(1 mHz) = 4.235×10⁻⁸⁹ — 77 OOM below LISA sensitivity (10⁻¹²)
- Ω_GW^γ(1 mHz) = 1.800×10⁻⁵⁹ — 47 OOM below LISA sensitivity
- Neither route is directly detectable by LISA

**Pre-registered threshold**: |Δlog₁₀ Ω_GW| ≥ 2 at 1 mHz. Computed value 29.6 OOM ≫ 2.

**Detector / sensitivity trajectory**:
- LISA (ESA L3, launch confirmed 2035 per Amaro-Seoane et al. 2017 LISA Mission Proposal): Ω_GW(1 mHz) floor ≈ 10⁻¹²
- DECIGO (JAXA concept, unfunded, >2040): would target 0.1-1 Hz, below framework f_peak (10⁶-10⁸ Hz)
- UHF-GW concepts (CAST-like magnetic conversion, levitated sensors, per Aggarwal et al. 2021 Living Rev. Relativ. 24 4): exploratory concept stage; no funded mission targeting 10⁶-10⁸ Hz band
- Ground-based pulsar timing arrays + LIGO-A+ (∼2030-2035): nHz and ∼100 Hz bands; do not touch mHz sub-peak or f_peak

**Reach date**: NEVER at 1 mHz with LISA. f_peak band (10⁶-10⁸ Hz) requires ultra-high-frequency concepts, no funded mission; reach timeline indefinite (> 2050 best case).

**Current status**: THEORETICALLY DECISIVE, OBSERVATIONALLY NEUTRAL.

**EVOI**: 0.000 (P(decisive-result) ≈ 0.01; |ΔP_obs_aligned| = 0, no P_obs_aligned effect because the channel does not map to a 9-slot observable). The channel is a lever for non-equilibrium theoretical reasoning (channel α survives as the instanton-mediated sub-additive to the gravity-only floor), not a near-term falsifier.

---

### II.F. w_0 / w_a open tension (W2-7-R1, 2.9σ against DR2)

**Framework prediction** (S82 §V.G R1): w_0^{fresh} = -0.9173 from fresh Volovik partition extraction using independently-provenanced inputs (ρ_J, ρ_GGE, w_J, w_GGE). Reproduces canonical w0_FW = -0.918 to 4 decimal places (|Δ| = 0.000724).

**Substitution chain (tension)**:
- Step 1 (definition): σ_tension := |w_0^framework − w_0^observational| / σ_observational
- Step 2 (substitution): |(-0.918) − (-0.752)| / 0.057
- Step 3 (simplification): 0.166 / 0.057
- Step 4 (direction): σ_tension = 2.912 (verified via Python)

**Pre-registered status**: OPEN. The R1 verdict confirms the framework's internal consistency (Pattern-3 concern retired), not its consistency with data.

**Detector / sensitivity trajectory**: Same as II.D — DESI DR3 is the decisive detector. The R1/R3 channels are coupled: if DR3 lands in the R3 rectangle, this tension closes; if outside, tension escalates.

**Reach date**: 2026-2027 (DR3)

**Current status**: ACTIVE TENSION (2.9σ); closes via II.D on DR3 release.

**EVOI**: folded into II.D (DR3 rectangle test replaces this tension in one shot). Standalone EVOI not applicable.

---

### II.G. sin²θ_W INFO at 3.98σ (W3-10)

**Framework prediction** (S82 §VI.J): sin²(M_Z)_pred = 0.231379 (cubic BC 0.23480 imposed at μ_BC = 2·M_Z = 182.38 GeV, run down via 2-loop SM RG).

**Substitution chain (sign of RG flow)**:
- Step 1 (definition): sin²(μ) = 3·α_1(μ) / (3·α_1(μ) + 5·α_2(μ))
- Step 2 (substitution): b_1 = +41/10 > 0 (dA > 0), b_2 = -19/6 < 0 (dB < 0)
- Step 3 (simplification): d(sin²)/d(ln μ) = [B·dA − A·dB] / (A+B)² > 0 (numerical +0.00499 at M_Z)
- Step 4 (direction): sin² INCREASES with μ; imposing 0.23480 > 0.23122 at μ > M_Z and running DOWN gives sin²(M_Z) < 0.23480

**Tension**: 3.98σ INFO (improvement from S78 W3-J 31.6σ FAIL at M_KK BC; factor 7.93× ≈ 0.9 OOM).

**Pre-registered threshold**: PASS if within 1σ (|dev| < 4×10⁻⁵); INFO if within 5σ; FAIL if > 5σ. Currently INFO.

**Detector / sensitivity trajectory**: theoretical closure path, not observational. Required work:
- 2-loop top-Yukawa RGE contribution (estimated 10⁻⁴ shift at M_Z, potentially closing the 3.98σ gap)
- 3-loop SM RG (~10⁻⁵ at M_Z)
- Framework-internal identification of μ_BC ≈ 188.44 GeV (factor-of-1.033 shift from 2·M_Z)

No new observational input needed; PDG 2024 value sin²(M_Z) = 0.23122 ± 0.00004 is already decisive. The closure is on the theory side.

**Reach date**: S83-S85 (session-scale theoretical work; top-Yukawa 2-loop RGE is a single-session compute)

**Current status**: OPEN AT INFO (3.98σ); not currently observational-blocking.

**EVOI**: 0.078 (P(decisive-by-S85) ≈ 0.70; |ΔP_obs_aligned| = 1/9 if 2-loop closes INFO to PASS). Second-highest non-trivial EVOI.

---

## III. Timeline (GANTT-style)

```
TIME WINDOW │ CHANNEL ACTIVATION
════════════╪═════════════════════════════════════════════════════════════════
PRE-2028    │ [D] DESI DR3 binary rectangle          ← HIGHEST-EVOI
            │ [G] sin²θ_W 2-loop closure (S83-S85 theoretical)
            │ [F] w_0/w_a tension closes via [D]
            │ ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
2028-2030   │ [C partial] CMB-S4 first light, σ(r) ≈ 5×10⁻⁴
            │     — detects or excludes r = 0.033 at 60-70σ
            │ Euclid full data ~ 2029
            │     — combined (Euclid + DESI) σ(w_0) ≈ 0.02
            │ ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
2030-2035   │ [C] C_cons via CMB-S4 + LiteBIRD joint
            │     — σ(C_cons) ≈ 0.16 via √(σ_r² + 64σ_nT²)
            │     — at k_CMB the framework value is ~0.009 (below sensitivity)
            │ LiteBIRD launch (2032) + first year data (2033-2034)
            │ [B] n_T sign via LiteBIRD if r = 0.033 detected
            │     — σ(n_T | r detected) ≈ 0.02
            │     — S66 transfer caveat: CMB-scale observable is RED, not BLUE
            │ [E] LISA launch 2035 — BOTH routes 47-77 OOM below sensitivity
            │ ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
2035+       │ [A] α_f_NL via SKA phase 2 full deployment
            │     — σ(α_f_NL) ≈ 0.01 via 21-cm bispectrum, l_max ~ 10⁵
            │     — decisive reach 2040+
            │ [E] f_peak band (10⁶-10⁸ Hz) requires UHF-GW concept
            │     — PERMANENTLY INACCESSIBLE with current detector roadmap
            │     — reach date indefinite (>2050)
════════════╧═════════════════════════════════════════════════════════════════
```

---

## IV. Falsifier Watchlist (EVOI-ordered)

EVOI = P(decisive-result-in-window) × |ΔP_obs_aligned|

| Rank | Channel | P(decisive) | reach | \|ΔP_obs_aligned\| | EVOI | Rationale |
|:-:|:-----|:-:|:-:|:-:|:-:|:-----|
| 1 | **D. DESI DR3 rectangle** | 0.95 | 2026-2027 | 2/9 | **0.211** | Closes two OPEN observables (w_0, w_a) in one binary test. Sc.B-like DR3 ⇒ SURVIVE and P_obs_aligned → 9/9; Sc.A/Sc.C-like ⇒ FAIL and → 5/9. DR2 central already at 2.9σ against framework. |
| 2 | G. sin²θ_W 2-loop closure | 0.70 | S83-S85 | 1/9 | 0.078 | Theoretical closure; top-Yukawa 2-loop RGE estimated to shift sin²(M_Z) by ~10⁻⁴, potentially closing the 3.98σ INFO to PASS. No new observation needed. |
| 3 | B. n_T sign via LiteBIRD | 0.50 | 2034-2036 | 1/9 | 0.056 | LiteBIRD launch 2032; σ(n_T \| r=0.033) ≈ 0.02. S66 transfer caveat: CMB-scale observable is RED, not BLUE — the sign-definite distinguisher lives at k_transit, not k_CMB. |
| 4 | C. C_cons > 0.033 (joint r + n_T) | 0.45 | 2035+ | 1/9 | 0.050 | Requires LiteBIRD + CMB-S4 joint. σ(C_cons) ≈ 0.16; framework k_CMB value 0.009 is below sensitivity — formal test possible but weak discrimination. |
| 5 | A. α_f_NL = 0 k-flat | 0.30 | 2035-2040+ | 1/9 | 0.033 | SKA phase 2 21-cm bispectrum decisive at σ ~ 0.01-0.02; structural flat prediction is a distinctive falsifier of GGE origin vs. single-field inflation. |
| 6 | E. GW α-vs-γ at 1 mHz | 0.01 | NEVER at LISA | 0 | 0.000 | 47-77 OOM below LISA; no P_obs_aligned effect because channel does not map to a 9-slot observable. Theoretically decisive but observationally neutral. |

**Operational reading**: The single most informative upcoming observation is **DESI DR3 binary rectangle** (EVOI ≈ 0.21, 3× the second-ranked channel). All other channels are 2030+ and individually move P_obs_aligned by at most 1/9. The DR3 test is the only one that moves the ratio by 2/9 in either direction and within < 2 years.

---

## V. Carry-Forward Computations

Each falsifier channel in §II-§IV generates one or more structured carry-forward computations for S83 planning. All entries use the 4-field **What / Inputs / Gate / Effort** format. Observational-reach computations only; theory-only closure (sin²θ_W 2-loop) is included because the arithmetic is a sign-definite RGE integration that feeds directly back into an observational gate.

---

### V.1. DR3 binary-rectangle live-watch

- **What**: automated pipeline that ingests the DESI DR3 public release (w_0, w_a, covariance) the moment it drops, applies the pre-registered rectangle decision rule `E_survive ≡ (w_0 ∈ [-0.94, -0.88]) AND (w_a ∈ [-0.10, +0.10])`, and emits the binary SURVIVE/FAIL verdict. Computes the off-diagonal-corrected single-axis tensions |Δw_0| / σ_{w_0}, |Δw_a| / σ_{w_a} using the DR3 covariance matrix C_{ij} with the canonical frozen point (w0_FW = -0.918, w_a = 0) via χ²(2D) = Δw^T C^{-1} Δw.
- **Inputs**: (a) DR3 public data release tarball (target: desi.lbl.gov/DR3 2026-2027); (b) canonical_constants: `w0_FW = -0.918`, `wa_FW = 0.0`, rectangle bounds `[-0.94, -0.88] × [-0.10, +0.10]`; (c) S74 registration JSON with SHA `7a5bfd68ddfec0b28eaaba2cc550dc12fd18cd32d8a972c00c47d901d3abdf88` (frozen 2026-04-11); (d) past-session files `project_s74_dr3_w0_falsifier.md`, `project_s71_desi_dr3_scenario_b.md`.
- **Gate**: feeds W2-7-R3 registered 2026-04-11. Decision: PASS if both axes inside rectangle (P_obs_aligned → 9/9); FAIL if either axis outside (P_obs_aligned → 5/9, triggers Pattern 3' audit per S79 P2-C). No intermediate/INFO outcome; E2' permanence rule binds.
- **Effort**: polling script + χ² computation = 2-3 hours, 1 agent session. Live-watch is asynchronous; the gate evaluates only when DR3 drops.

---

### V.2. LiteBIRD σ(n_T) vs detector-year reach curve

- **What**: compute σ(n_T | r = 0.033 detected) as a function of (detector-year t, launch-schedule scenario). Substitution chain: (Step 1) σ(n_T) ~ σ(r)/r / ln(l_max/l_min); (Step 2) at l ∈ [2, 200], ln = 4.605; (Step 3) σ(r) ∝ 1/sqrt(t) per Gaussian noise-limited scaling; (Step 4) direction: longer t → smaller σ(n_T), monotone. Baseline Matsumura 2014: 3-yr survey → σ(n_T) = 0.020. Tabulate t ∈ {1, 2, 3, 5, 7} yr and launch-year ∈ {2032, 2034, 2036}. Verified via Python: σ(n_T) = {0.0346, 0.0245, 0.0200, 0.0155, 0.0131} at t = {1, 2, 3, 5, 7}.
- **Inputs**: (a) LiteBIRD noise curves from Matsumura et al. 2014 JLTP 176 733; (b) canonical_constants: `r = 0.033` (S64 TENSOR-BURST-64), `n_T_kCMB = -3.02e-3` (S66 TENSOR-TRANSFER-66); (c) framework prediction files `project_s68_liteb_r_forecast.md`, `project_s66_tensor_transfer.md`.
- **Gate**: creates new gate LITEB-NT-REACH-83 INFO. Threshold: σ(n_T) ≤ 0.05 at baseline (my prior projection) requires t ≥ 1.2 yr; σ(n_T) ≤ 0.02 requires t ≥ 3 yr. PASS if LiteBIRD on-schedule-for-2032 + 3-yr survey would put σ(n_T) ≤ 0.02; INFO if launch slips to 2034-2036 forces extension; FAIL if no launch scenario reaches σ(n_T) ≤ 0.05 by 2038. Feeds II.B via EVOI update.
- **Effort**: analytic reach scan = 1-2 hours, 1 agent session.

---

### V.3. CMB-S4 σ(C_cons) sensitivity table

- **What**: tabulate σ(C_cons) = sqrt(σ_r² + 64·σ_nT²) vs (integration time t_int, frequency-coverage channels Nf, f_sky). Sagan flagged σ(C_cons) = 0.40 as 12× too coarse to resolve C_cons = 0.033; compute the (t_int, Nf) combination that brings σ(C_cons) ≤ 0.011 (3σ detection of framework prediction). Substitution chain: (Step 1) σ(C_cons)² = σ_r² + 64·σ_nT² (error propagation, direct); (Step 2) σ_r ∝ 1/sqrt(t_int·f_sky·Nf); (Step 3) σ_nT dominated by LiteBIRD at low-l, not CMB-S4; (Step 4) direction: at σ_r = 5×10⁻⁴ and σ_nT = 1.37×10⁻³, σ(C_cons) = 0.011 (verified via Python). Framework k_CMB value is 0.009 (from n_T(k_CMB) = -3.02e-3 per S66): detection requires σ(C_cons) < 0.005 for 2σ on k_CMB value — NOT reachable with current projections. Output: a (σ_r, σ_nT) grid showing where C_cons = 0.033 is detectable vs where C_cons(k_CMB) = 0.009 is detectable.
- **Inputs**: (a) CMB-S4 noise curves from Abazajian et al. 2022 Science Book; (b) LiteBIRD σ(n_T) from V.2 above; (c) canonical_constants: `r = 0.033`, `n_T_kCMB = -3.02e-3`; (d) past-session files `project_s68_cmbs4_fnl_forecast.md`, `project_s66_tensor_transfer.md`.
- **Gate**: creates new gate CMBS4-CCONS-SENSITIVITY-83 INFO. PASS if (t_int, Nf, f_sky) exists that reaches σ(C_cons) ≤ 0.011 at 2 × k_transit reach; INFO if C_cons = 0.033 reachable but k_CMB value 0.009 is not; FAIL if no reachable configuration passes either bound. Feeds II.C EVOI update.
- **Effort**: sensitivity scan + grid plot = 2-3 hours, 1 agent session.

---

### V.4. 21-cm σ(α_f_NL) reach curve (SKA phase-1 vs phase-2)

- **What**: compute σ(α_f_NL) as a function of SKA phase (1-early, 1-full, 2), survey volume V_survey, k_max, integration time. Substitution chain: (Step 1) σ(α_f_NL) ∝ 1/sqrt(V · k_max³) at fixed bispectrum SNR; (Step 2) phase-1/phase-2 collecting-area ratio is 1/4, so σ ratio is 2; (Step 3) phase-1 early vs full is 1/4 of full deployment, factor 2 in σ; (Step 4) direction: phase-2 ~ 0.015 at 5-decade coverage, phase-1 early ~ 0.060 (verified via Python). Cross-check: CMB-S4 via f_NL/ln(l) gives σ(α_f_NL) ≈ 0.46-0.79 depending on integration time — 2 OOM above framework reach.
- **Inputs**: (a) SKA phase-1/phase-2 forecasts from Karagiannis et al. 2020 MNRAS 492 4045; (b) canonical_constants: `f_NL_GGE = 0.0547`, framework α_f_NL prediction = 0 (k-flat); (c) past-session files `project_s67_gge_bispectrum.md`, `project_s82_w3_4_gge_fnl.md`.
- **Gate**: creates new gate SKA-ALPHA-FNL-REACH-83 INFO. Threshold: PASS if SKA phase-2 σ(α_f_NL) ≤ 0.01 confirmed at 5-decade k coverage (reaches framework null at 1σ); INFO if σ(α_f_NL) ∈ [0.01, 0.03]; FAIL if all phases deliver σ(α_f_NL) > 0.03 by 2040. Feeds II.A EVOI update and P_obs_aligned PASS threshold for channel A.
- **Effort**: analytic reach scan + bispectrum mode-count = 2-3 hours, 1 agent session.

---

### V.5. TENSOR-TRANSFER k_transit → k_CMB computation

- **What**: the scale-transfer problem flagged in S66 TENSOR-TRANSFER-66 FAIL (memory `project_s66_tensor_transfer`). Current state: n_T(k_transit) = +0.468 (BLUE), n_T(k_CMB) = -3.02×10⁻³ (RED), transfer factor spans 54 decades of k. Computation: derive n_T(k_CMB) from n_T(k_transit) via the substrate dispersion relation ω²(k) = c_sub²·k² + (k²·r_s·c_fabric / (2·ω_a·M_KK))² evaluated between k_transit ~ 10⁵² Mpc⁻¹ and k_CMB ~ 0.05 Mpc⁻¹. Substitution chain: (Step 1) P_T(k) = P_T(k_ref) · (k/k_ref)^{n_T}; (Step 2) apply transfer function T_T(k, τ_dec) with substrate dispersion; (Step 3) n_T^{obs}(k_CMB) = n_T(k_transit) + d ln T_T² / d ln k|_{k_CMB}; (Step 4) direction: the transfer log-derivative is negative at CMB scales because the substrate dispersion is k²-dominated (linear acoustic) not k⁴-dominated (Jensen-like), driving the observed n_T toward slow-roll −r/8. Output: explicit n_T^{obs}(k_CMB) computation from first-principles dispersion + verification that -3.02×10⁻³ emerges rather than being an empirical fit.
- **Inputs**: (a) canonical_constants: `c_fabric`, `c_Gold`, `M_KK`, `omega_L1`, `dS_fold`, `tau_fold`; (b) past-session data `project_s66_tensor_transfer.md`, `project_s65_blue_tensor_tilt.md`; (c) substrate dispersion relation from S66 W2-14 or equivalent.
- **Gate**: closes (or reopens) TENSOR-TRANSFER-66. PASS if the from-first-principles computation yields n_T(k_CMB) ∈ [-5×10⁻³, -1×10⁻³] (captures observed -3.02×10⁻³ within a factor 5); INFO if the value reproduces within an OOM; FAIL if the computed n_T(k_CMB) has the wrong sign or is 2+ OOM off. Feeds II.B and II.C critically: if FAIL, the transfer analysis was wrong and the BLUE sign claim applies at k_CMB — which would raise LiteBIRD EVOI. If PASS, confirms the k_CMB observable is RED and n_T channel is observationally degenerate with slow-roll.
- **Effort**: 4-6 hours, 1 agent session (substrate-dispersion integration is non-trivial; may need 2 sessions if transfer function requires coupled-mode solver).

---

### V.6. sin²θ_W 2-loop top-Yukawa closure + μ_BC natural-threshold scan

- **What**: close the 3.98σ INFO from S82 W3-10 CUBIC-SIN2-W-EW. Two sub-computations. **(a) 2-loop top-Yukawa RGE**: integrate the SM 2-loop β-functions for α_1, α_2 from μ_BC down to M_Z with top-Yukawa y_t contributions included. Substitution chain: (Step 1) β_i^{(2)} = β_i^{(1-loop)} + (loop factor) · [matrix terms + y_t contribution]; (Step 2) y_t enters via b_{i,y} = diag(17/10, 3/2, 0) · y_t²; (Step 3) integrate from μ_BC = 182.38 GeV downward; (Step 4) direction: top-Yukawa contribution to sin²(M_Z) is sign-definite because d(sin²)/d y_t² > 0 at M_Z (verified numerically by comparing 1-loop vs 2-loop integrations). Estimated shift: |Δ sin²(M_Z)| ~ 10⁻⁴. **(b) μ_BC natural-threshold scan**: identify framework-internal mass scales in [150, 300] GeV (cubic-BC candidates, threshold-like scales from D_K eigenvalue spectrum at L_max=10) and test whether μ_BC = 188.44 GeV (factor-1.033 shift from 2·M_Z) has a structural justification.
- **Inputs**: (a) canonical_constants: `m_t_pole`, `alpha_s_MZ_obs`, `sin2theta_W_PDG = 0.23122`, `M_Z`, cubic BC 0.23480; (b) SM 2-loop β-functions from Machacek-Vaughn or equivalent reference; (c) past-session files `project_s78_w3p_pati_salam.md`, `project_s82_w3_10_cubic_sin2_w_ew.md`; (d) D_K eigenvalue spectrum at L_max=10 for candidate μ_BC identification.
- **Gate**: closes (or refines) CUBIC-SIN2-W-EW at S83. PASS if |dev| < 1σ (|Δ sin²(M_Z)| < 4×10⁻⁵) after 2-loop + natural μ_BC; INFO if 1σ ≤ |dev| < 5σ (improvement from 3.98σ to ≤ 4σ); FAIL if 2-loop + natural μ_BC makes tension WORSE (> 3.98σ). Feeds G-channel in §IV Watchlist (P_obs_aligned 7/9 → 8/9 on PASS).
- **Effort**: 4-6 hours, 1-2 agent sessions. 2-loop RGE integration is standard but tedious; natural-threshold scan requires D_K spectrum post-processing.

---

### V.7. P_obs_aligned ratio update rules (structured spec for S83 planning)

- **What**: translate the qualitative update-logic table (prior §V, now §VI) into a structured ingest format that the S83 planning pipeline can parse. For each of the six observational channels (A α_f_NL, B n_T sign, C C_cons, D DR3 rectangle, E GW α-γ, G sin²θ_W) emit a 3-branch decision tree (PASS / NULL / FAIL) with explicit P_obs_aligned deltas. Substitution chain for the arithmetic: (Step 1) P_obs_aligned := N_PASS / N_slots with N_slots = 9; (Step 2) each channel outcome updates N_PASS by {+1, 0, -1} for {PASS, NULL, FAIL} except D which updates by {+2, n/a, -2}; (Step 3) aggregate: P_obs_aligned^{S83+} = (7 + Σ δ_channel) / 9; (Step 4) direction: cumulative ceiling at all-PASS sweep = 9/9; floor at all-FAIL sweep = 3/9; single-channel D-FAIL = 5/9 (most likely near-term negative). Output: machine-readable JSON with schema `{channel: {PASS: {δ, condition}, NULL: {...}, FAIL: {...}}}`.
- **Inputs**: (a) current synthesis §II falsifier catalog; (b) canonical P_obs_aligned = 7/9 post-S82 (per OOM §III.A); (c) W2-7-R3 registration JSON; (d) past-session files `project_s80_p_obs_catalog.md` (channel enumeration), `project_s82_w3_4_gge_fnl.md` (f_NL slot).
- **Gate**: creates pre-registration-infrastructure gate POA-UPDATE-SPEC-83 (meta, not observational). PASS if JSON schema parses and all 6 channels have valid decision trees with sign-definite δ values; INFO if one channel has ambiguity (e.g., NULL vs PASS overlap); FAIL if any channel's decision tree produces inconsistent δ (e.g., same outcome gives different P_obs_aligned). No direct observational EVOI; enables S83 planning to ingest.
- **Effort**: 1-2 hours, 1 agent session. Format + schema validation only; no new physics computation.

---

### V.8. DR3 covariance-off-diagonal contingency (sub-item of V.1)

- **What**: auxiliary to V.1. The pre-registered rectangle test treats (w_0, w_a) as independent axes, but the DR3 covariance will have non-zero off-diagonal ρ_{w_0, w_a}. Compute the 2D tension χ²(2D) = Δw^T C^{-1} Δw as a diagnostic alongside the binary rectangle verdict, so if the rectangle FAILS we can report whether the FAIL is driven by correlated motion (physical) or by one axis alone. Substitution chain: (Step 1) define Δw = (w_0^DR3 − w_0^FW, w_a^DR3 − w_a^FW); (Step 2) C^{-1} = (1/det) · [[σ_wa², -ρσ_w0σ_wa], [-ρσ_w0σ_wa, σ_w0²]]; (Step 3) χ²(2D) = σ_wa² Δw_0² + σ_w0² Δw_a² - 2ρσ_w0σ_wa Δw_0 Δw_a, all / det(C); (Step 4) direction: χ²(2D) > χ²(1D-sum) when ρ is opposite-sign to the Δw correlation, < when same-sign. Report both as INFO.
- **Inputs**: DR3 covariance matrix C (from V.1 inputs), canonical (w0_FW, wa_FW), S59 WA-ERROR-PROP projections σ(w_0) ≈ 0.040, σ(w_a) ≈ 0.177.
- **Gate**: diagnostic-only INFO gate DR3-COV-DIAG-83. No PASS/FAIL; reports 2D tension alongside V.1 binary verdict.
- **Effort**: 1 hour, bundled into V.1 agent session.

---

### V.9. EVOI watchlist refresh for S83

- **What**: recompute the EVOI table (§IV) with updated P(decisive-by-window) factors after V.1-V.8 sensitivity curves deliver refined detector reach. Substitution chain: (Step 1) EVOI = P(decisive) × |Δ P_obs_aligned|; (Step 2) P(decisive) updates from V.2 (LiteBIRD), V.3 (CMB-S4), V.4 (SKA) launch-schedule scenarios; (Step 3) |Δ P_obs_aligned| unchanged (structural); (Step 4) direction: longer-baseline schedules reduce P(decisive) within the 2030-2040 window, lowering EVOI for downstream channels but not for the DR3 rectangle (which is within 2 years). Report as updated §IV table for S83 carry-forward.
- **Inputs**: V.2-V.4 output files, current §IV Watchlist table, `sessions/evoi-framework.md`.
- **Gate**: INFO-only update to EVOI table. No new gate; feeds next session's priority ordering.
- **Effort**: 1 hour, agent-session bundled into S83 planning.

---

## VI. P_obs_aligned Update Logic

Current state: **P_obs_aligned = 7/9 = 0.7778** (post-S82, per §III.A of OOM ladder).

The 7/9 slots (P5-A registered observables): A_s (Branch-A PASS-F2, conditional), n_s (1.3-1.9σ OPEN), r (PASS), μ-distortion (PASS), f_NL (PASS, new S82 W3-4), β_iso (PASS), m_H (PASS), N_eff (PASS), f_NL refined + adjacent-obs enumeration (W3-9 structural; counted as single slot upgrade from 6/9 → 7/9).

The 2 OPEN slots (not yet PASS or FAIL): w_0 (2.9σ against DR2), w_a (2.9σ against DR2). Prior FAILs (sin²θ_W, α_s) are non-observables under current re-cast; sin²θ_W is INFO at 3.98σ after S82 W3-10.

| Channel | Current | PASS outcome | NULL outcome | FAIL outcome |
|:-----|:-:|:-----|:-----|:-----|
| **A. α_f_NL = 0** | 7/9 | 8/9 (α=0 confirmed at σ<0.01) | 7/9 (σ>0.01 but no detection) | 6/9 (α≠0 detected at >3σ; structural FAIL) |
| **B. n_T sign** | 7/9 | 8/9 (n_T(k_CMB) > 0 or n_T(k_transit) probed and >0) | 7/9 (no detection) | 6/9 (n_T(k_CMB) < -0.05 at >2σ; transfer analysis wrong) |
| **C. C_cons > 0.033** | 7/9 | 8/9 (C_cons > 0 at >2σ) | 7/9 (C_cons consistent with 0 within σ) | 6/9 (C_cons < -0.05 at >2σ) |
| **D. DESI DR3 rectangle** | 7/9 | 9/9 (both w_0, w_a SURVIVE rectangle; 2 OPEN → 2 PASS) | n/a (binary test, no null) | 5/9 (either axis outside; 2 OPEN → 2 FAIL, plus potential A_s Branch-B re-roll) |
| **E. GW α-vs-γ** | 7/9 | 7/9 (no mapping to 9-slot observables) | 7/9 | 7/9 (observationally neutral) |
| **F. w_0/w_a tension** | 7/9 | closes via D | closes via D | closes via D |
| **G. sin²θ_W 2-loop** | 7/9 | 8/9 (INFO→PASS if 2-loop shift ≈10⁻⁴ closes 3.98σ to <1σ) | 7/9 (no shift; stays INFO) | 6/9 (2-loop worsens tension; INFO→FAIL) |

**Cumulative ceilings and floors**:
- **Upper ceiling at full-PASS sweep** (all of A, B, C, D, G PASS): P_obs_aligned → 9/9 = 1.000 (since D alone saturates 9/9 if SURVIVE, further PASS on A/B/C/G is redundant for the metric but strengthens joint probability)
- **Lower floor at full-FAIL sweep** (all FAIL): P_obs_aligned → 3/9 ≈ 0.333 (5/9 from D-FAIL, minus 1/9 each for A, B, C, G failing)
- **Single-channel D-FAIL** (most likely near-term negative): P_obs_aligned → 5/9 = 0.556 (2 OPEN → 2 FAIL)

---

## VII. Detector Risk Factors

**DESI DR3 (reach 2026-2027)**:
- Low risk: survey is operating; DR2 released; DR3 is extension of existing pipeline
- Systematics: BAO reconstruction, quasar tracer evolution, LRG2 z = 0.706 bin bottleneck (S70 DESI-DR3-UPDATE flagged this as the constraint on w_a precision)
- Schedule risk: slippage from 2027 to 2028 plausible but unlikely to delay beyond 2028

**Euclid (reach 2029 full analysis)**:
- Low risk: operating since 2023; BAO + WL pipeline mature
- Systematics: photo-z calibration for WL; galaxy sample bias
- Joint with DESI: partial double-counting at low-z; marginalize carefully

**LiteBIRD (reach 2034-2036)**:
- Medium risk: JAXA confirmed 2023, launch projected 2032 but L-class missions slip 1-3 yr commonly
- Systematics: 1/f noise at low-l crucial for r detection; foreground subtraction at 10-30 GHz and 200-300 GHz
- If r = 0.033 not detected at > 5σ, the n_T measurement becomes null (no tensor spectrum to tilt)

**CMB-S4 (reach 2028-2030)**:
- Medium risk: DOE/NSF joint funding confirmed 2023; first light 2028 target
- Systematics: atmospheric window (Pole + Chile); foreground polarization
- Site risks: Pole infrastructure upgrade, weather

**SKA Phase 2 + 21-cm IM arrays (reach 2035-2040+)**:
- High risk: SKA Phase 2 budget pending 2030 review; 21-cm IM arrays (CHIME, HERA, HIRAX) upgrading
- Systematics: foreground subtraction (radio sources, galactic synchrotron) dominates 21-cm; bispectrum pipeline immature
- Atmospheric window: ground-based IM constrained to redshifted band 30-200 MHz; RFI risk

**LISA (reach 2035)**:
- Low-medium risk: ESA L3 class, launch 2035 confirmed; LISA Pathfinder demonstrated key technologies 2016-2017
- For the framework: detector is on schedule but framework signal is 47-77 OOM below threshold — no amount of LISA improvement reaches the signal.

**UHF-GW (reach >2050)**:
- Very high risk: concept stage; no funded mission for 10⁶-10⁸ Hz band
- Technology: magnetic conversion detectors (CAST-like), levitated sensors; all exploratory
- The framework's f_peak prediction drives interest in this band but is not sufficient to justify a mission alone

---

## VIII. Summary Table

| # | Channel | Framework prediction | Detector | Reach date | Pre-reg threshold | EVOI | P_obs_aligned Δ on PASS / FAIL |
|:-:|:-----|:-----|:-----|:-:|:-----|:-:|:-----|
| 1 | **DESI DR3 rectangle** | (w_0, w_a) ∈ [-0.94,-0.88] × [-0.10,+0.10] | DESI | 2026-2027 | binary SURVIVE/FAIL, σ(w_0)=0.040, σ(w_a)=0.177 | **0.211** | +2/9 / -2/9 |
| 2 | sin²θ_W EW-closure | sin²(M_Z) = 0.23138; want <1σ from PDG 0.23122±4×10⁻⁵ | PDG (data existing); closure theoretical | S83-S85 | |dev| < 4×10⁻⁵ PASS; <2×10⁻⁴ INFO | 0.078 | +1/9 / -1/9 |
| 3 | n_T sign (via LiteBIRD) | n_T(k_transit) > 0 strict; n_T(k_CMB) = -3×10⁻³ (S66 transfer) | LiteBIRD + CMB-S4 | 2034-2036 | σ(n_T \| r=0.033) ≈ 0.02 | 0.056 | +1/9 / -1/9 |
| 4 | C_cons > 0.033 | r + 8·n_T > 0 strict; k_CMB value ≈ 0.009 | LiteBIRD + CMB-S4 joint | 2035+ | σ(C_cons) ≈ 0.16 | 0.050 | +1/9 / -1/9 |
| 5 | α_f_NL = 0 | flat across 5 decades k; machine-precision zero | SKA + 21-cm IM | 2035-2040+ | σ(α_f_NL) ≤ 0.01 | 0.033 | +1/9 / -1/9 |
| 6 | GW α-vs-γ at 1 mHz | ratio 4.25×10²⁹; α=4.23×10⁻⁸⁹, γ=1.80×10⁻⁵⁹ | LISA (invisible); UHF-GW concept | NEVER at 1 mHz; >2050 for f_peak | \|Δlog Ω_GW\| ≥ 2 | 0.000 | 0 / 0 |
| 7 | w_0 tension (open) | w_0 = -0.918 via Volovik partition | DESI (DR3 closes this) | 2026-2027 | closes via #1 | folded into #1 | folded into #1 |
| 8 | w_a = 0 (open) | w_a = 0 exact (four-fold lock) | DESI (DR3 closes this) | 2026-2027 | closes via #1 | folded into #1 | folded into #1 |
| 9 | f_NL amplitude (PASS already) | 0.0547 at 0.43σ vs Planck 2.5±5.7 | Planck (done); CMB-S4 refines | 2030 refinement | σ(f_NL^equil) ≈ 5 CMB-S4 | PASS locked | — |
| 10 | τ_NL Suyama-Yamaguchi (untested) | τ_NL ≥ (6 f_NL / 5)² = 0.0043 | CMB-S4 + 21-cm bispectrum | 2030-2040 | structural inequality | not yet registered | +1/9 if registered and PASS |

---

## Methodological Notes

1. **Sigma-reach numerics verified via Python** (direction chain + numerical verification in the session transcript):
   - w_0 DESI DR2 tension: 2.912σ (|−0.918 − (−0.752)|/0.057)
   - f_NL σ-band: 0.429 (|0.0547 − 2.5|/5.7)
   - C_cons σ-reach: √(σ_r² + 64 σ_nT²) = 0.160 with (σ_r, σ_nT) = (0.001, 0.02)
   - GW ratio: (6.875×10⁶)^(13/3) = 4.249×10²⁹, alpha 76.4 OOM below LISA, gamma 46.7 OOM below LISA
   - n_T slow-roll: −0.033/8 = −0.004125 (RED)
   - C_cons framework at k_CMB: 0.033 + 8·(−0.003) = 0.009 (still > 0 but 1.7 OOM below the k_transit bound)

2. **Scale-transfer caveat (memory `project_s66_tensor_transfer`)**: the BLUE tensor tilt and C_cons > 0.033 statements in W3-9 are the k_transit-scale substitution chain; the CMB-scale observables are n_T(k_CMB) = -3×10⁻³ and C_cons(k_CMB) ≈ 0.009. A LiteBIRD measurement cannot distinguish the framework from standard inflation at the W3-9 stated thresholds without a k_transit probe, which has no current observational route.

3. **P_obs_aligned arithmetic is a bookkeeping metric, not a probability** (per `.claude/rules/evoi-prioritization.md` and `feedback_reporting-framing`). Treat 7/9 as a constraint-map index, not a confidence level. A framework at 9/9 with one decisive sign-test against it still fails; a framework at 5/9 with two passes on a k-flat prediction is not falsified by those passes alone.

4. **EVOI values are operational**, not posterior: P(decisive-by-window) reflects detector-schedule + atmospheric/budget risk; |ΔP_obs_aligned| reflects the bookkeeping move. EVOI is the work-prioritization signal per the `.claude/rules/evoi-prioritization.md` rule.

5. **Detector timelines cross-referenced** with: Abazajian et al. 2022 (CMB-S4 Science Book), Matsumura et al. 2014 JLTP 176 733 (LiteBIRD), DESI Collaboration schedule updates 2024, Amaro-Seoane et al. 2017 (LISA Mission Proposal), Karagiannis et al. 2020 MNRAS 492 4045 (21-cm bispectrum), Aggarwal et al. 2021 Living Rev. Relativ. 24 4 (UHF-GW concepts). No direct conflict between memory timelines (S68 LITEB-R-FORECAST at 24.2σ LiteBIRD, S68 CMBS4-FNL-FORECAST at σ_eq=5.0) and public TDR timelines.

6. **Registration SHA-256 pins** (for citability):
   - W2-7-R3 DR3 falsifier: `7a5bfd68ddfec0b28eaaba2cc550dc12fd18cd32d8a972c00c47d901d3abdf88` (registration JSON frozen 2026-04-11)
   - W3-4 GGE-FNL: `fe8c7d0e6b96187d5139a78adbea67a67736d75e555488fd9aa4c47889b483c9`
   - W3-9 AS-ADJACENT-OBS: `0d2eeabd7d4f8a40c87b8d6cdae391ae900b5b69451d35dbf434f76078448531`
   - W2-6 GW-CHANNEL: `0c33cc9bd06e0b4f6af05b9949950d69cad404e288e2d51e52690351df72a2ab`
   - W2-14 FIRAS-CHLUBA-FULL: `dea8a6c73b961acb72ce9122b7306226aadd9d6b319e3b904e1956d68026b7ed`
   - W3-10 CUBIC-SIN2-W-EW: `62a1dd7e346f82b4fb803a44af7297ba95228b3c4eb3eddc8318dc88d610f54d`

---

## File paths

- **Synthesis output**: `C:\sandbox\Ainulindale Exflation\sessions\archive\session-82\session-82-mack-synthesis.md`
- **Source**: `C:\sandbox\Ainulindale Exflation\sessions\archive\session-82\session-82-results-workingpaper.md` §§V.F, V.G, V.N, VI.D, VI.I, VI.J
- **OOM ladder**: `C:\sandbox\Ainulindale Exflation\sessions\archive\session-82\session-82-OOM.md` §§II, III.A, IV.B
- **Agent memory referenced**: `C:\sandbox\Ainulindale Exflation\.claude\agent-memory\mack-cosmic-bridge\` — `project_s66_tensor_transfer.md`, `project_s60_dr3_preregister.md`, `project_s68_liteb_r_forecast.md`, `project_s68_cmbs4_fnl_forecast.md`, `project_s74_dr3_w0_falsifier.md`, `reference_key-constraints.md`
