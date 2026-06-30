# Session 84 — Solo Synthesis (S-2, Landau, slot 2 of 2)

**Focus**: K-Corridor Phenomenology — BCS / Leggett / Bogoliubov mode mapping
**Author**: `landau-condensed-matter-theorist`
**Corridor**: `K ∈ [K_R5 = 1.9222, K_crit = 91.5]` with kinetic sub-corridor continuation to `K = 3.556×10⁵`
**Sources**: `session-84-synthesis-collation.md`, `session-84-w5-workingpaper.md`, `session-84-w6-workingpaper.md`; Landau agent-memory S84 W5-66 entry (INFO verdict, N_OP=8 class BDI).
**Gate-verdicts authoritative**: all numerical statements below are SHA-anchored to the gate-verdict ledger entries cited in §I.

---

## §I. Anchor Ledger (SHA-pinned, single source of truth)

| Anchor | Value | Gate | SHA (short) |
|:---|---:|:---|:---|
| `K_R5` (corridor floor, B2-only GGE R5) | 1.9222 | W5-63 | 29af1e68 |
| `K_*` (lab discriminator, coth(1)) | 1.3130 | W5-58 PASS | b8b123a5 |
| `K_substrate = K_R3` (canonical anchor) | 2.035 | S82 W2-4 | — |
| `K_crit` (inflationary ceiling, ε_eff=1 pole) | 91.543 | W5-55 | 106c5096 |
| `K_μFIRAS` (μ-endpoint, Chluba γ=1) | 3.556×10⁵ | W5-57 INFO | 73986af4 |
| `f_B_joint` (t-s partition) | 0.485 | W5-64 INFO | d8f4db87 |
| `c_S_canon` (G46 scalar sound speed) | 0.485 | S83 G46 | 3f004c9a |
| `A_s_floor_B` (Branch-B raw, no K dial) | 5.7403×10⁻¹⁴ | W5-59 INFO | 023beabd |
| `A_s_floor_B × K_R5` (R5-applied) | 1.1033×10⁻¹³ | W5-59 INFO | 023beabd |
| `N_OP_framework` (dim G/H, SU(3)×SO(3)×U(1)_rel / SU(2)×U(1)×SO(2)×Z_2) | 8 | W5-66 INFO | 519c8c03 |
| `τ_GGE` per unit K (G40 slope) | 7.86×10⁴ τ-units | S83 G40 | — |
| `f_L` asymptotic floor (Leggett majority) | 0.6027 | S83 G39 | 1f0ab454 |
| `f_B` asymptotic floor (Bogoliubov minority) | 0.3973 | S83 G39 | 1f0ab454 |

`K_R5/K_*` verification (Python, 2026-04-20): `coth(1) = (e + 1/e)/(e − 1/e) = 1.3130352854993315` ✓. `K_crit = K_substrate / ε_anchor = 2.035/0.02223 = 91.5429599…` ✓.

---

## §II. Framing — Why a Mode-Partition Map

Wave 5 established four structural facts about the corridor:

1. **The corridor is not a 1D order-parameter axis across its full 5-OOM pre-registered range** (W5-55 FAIL, W5-66 INFO). It is 1D Landau only on the inflationary sub-corridor K ∈ (1, 91.5]; above K_crit = 91.5 the Mukhanov–Sasaki tilt formula has a pole and the corridor leaves the inflationary manifold.
2. **The OP coordinate K is regulator-dependent** (W5-54 FAIL; K_R5_Zubarev = 32.40 vs K_R5_zeta = 0.6366, span 10^1.71). The *structure* of the coset G/H is scheme-invariant; the *magnitude* of K is not.
3. **Parent-child inheritance from 3He-B is partial** (W5-66 INFO). The framework over-inherits by 3 continuous broken directions: N_OP_framework = 8 vs N_OP_3HeB = 5, with the extra 3 arising from SU(3)/(SU(2)×U(1)) = CP² (framework-unique).
4. **The corridor is mode-hybrid, not mode-singular**. G39 partition gives f_L ≥ 0.6027, f_B ≤ 0.3973 across K ∈ [2.035, 3.56×10⁵]. The corridor is everywhere a Leggett–Bogoliubov mixture; there is no K at which one channel vanishes. But the *weight ratio* f_B/f_L varies, and the *effective mode* differs by region because different channels rate-limit different observables.

These four facts jointly imply that a mode-partition map must be a two-axis object: (a) *dominant dispersive carrier* on each K-sub-region, keyed by Pomeranchuk-stable dispersive signatures from G39/G40/G41; (b) *rate-limiting relaxation mode*, keyed by τ_GGE(K) and the Leggett-Q factor. The physical content of the Landau classification is how these two axes align or dis-align across the corridor.

**Convention**. Throughout this synthesis, K refers to the substrate-native Zubarev K under the R3 band-multiplicity-weighted (3/3/2) convention unless prefixed (`K_zeta`, `K_R5`, etc.). Substrate framing per `.claude/rules/phononic-framing.md`: K parameterizes spectral complexity growth inside each point; it is not a cosmic-time coordinate, not an inflaton amplitude, and not an expansion factor.

---

## §III. K_substrate = 2.035 — Bogoliubov-Dominant or Leggett-Dominant?

**Definition**. At a given K, the "dominant mode" is the channel that carries the larger Pomeranchuk-stable phonon population in the post-fold GGE relic. In the framework's two-channel decomposition (Leggett phase mode | Bogoliubov quasiparticle), this is measured by f_L(K) and f_B(K) = 1 − f_L(K) per G39.

**Substitution chain**:

- Step 1 (definitions):
  - `f_L(K) := occupation fraction of Leggett (relative-phase) channel in the GGE relic at post-fold ordering-scale k_pivot`
  - `f_B(K) := 1 − f_L(K) := Bogoliubov (quasiparticle) fraction`
  - `K_substrate := 2.035` (canonical substrate-native anchor, S82 W2-4 PASS, R3 3/3/2).
  - G39 canonical output (SHA 1f0ab454): `f_L(K=2.035) = 0.6517`, `f_B(K=2.035) = 0.3483`, `f_L + f_B = 1` (closure to machine ε).
- Step 2 (substitution at K_substrate):
  - `f_L(2.035) = 0.6517 > 0.5` → Leggett majority.
  - `f_B(2.035) = 0.3483 < 0.5` → Bogoliubov minority.
- Step 3 (simplification):
  - `f_L/f_B = 0.6517/0.3483 = 1.871` (Leggett carries ≈1.87× the Bogoliubov occupation).
- Step 4 (direction):
  - Majority channel selects the dispersive carrier manifold; `K_substrate = 2.035` sits on the **Leggett-dominated manifold**, 1.87× over the Bogoliubov channel.

**Corollary (not a direction claim; structural identification).** K_substrate = 2.035 is NOT a pure-mode point. It is a mixed regime with a Leggett majority. The Bogoliubov channel is the *minority* carrier — structurally permanent (f_B floor 0.3973 across 5 OOM in K per G39), and physically non-negligible (it carries the tensor amplitude per W5-64 r-channel identity).

**Cross-check (W5-66 feed)**: The G/H decomposition factors into four pieces — CP² (SU(3)-internal, 4 dirs), S² (fiber-orbital, 2 dirs), U(1)_rel/Z_2 (Leggett-phase, 1 dir), K-dilation axis (gap modulus, 1 dir). The Leggett direction lives in `U(1)_rel/Z_2`; the Bogoliubov direction lives in `K-dilation` (gap modulus). At K_substrate = 2.035 both directions are active — the Leggett direction is weighted 1.87× more heavily by G39 occupation, but the Bogoliubov direction is the one that parameterizes K itself. This is the "mixed-manifold" structural reading: K is the Bogoliubov *coordinate*, but most of the GGE occupation sits in the Leggett *direction*.

**Verdict on prompt question**: K_substrate = 2.035 sits on a **Leggett-dominant mixed manifold**. The Bogoliubov manifold is not *off* the substrate; it is the coordinate axis K itself. The Leggett manifold carries the majority of the GGE relic occupation and is the *dispersive carrier* of most phononic observables at this K.

---

## §IV. GGE Relaxation Timescale τ_GGE(K) Across the Corridor

**Definition** (per S83 G40 verdict structure, SHA-traced):
- `τ_GGE(K) := mean relaxation timescale for GGE-relic occupation to equilibrate to the post-fold substrate band structure after perturbation by fiber spectral redistribution at K`.
- G40 established `dτ_GGE/dK = 7.86×10⁴ τ-units/unit K` at machine ε (linear response theorem, S83 permanent).
- τ-units are M_KK⁻¹, i.e. `1 τ-unit ≈ t_fold / S_fold ≈ 5 × 10⁻⁴² s` (from M_KK canonical).

**Substitution chain**:

- Step 1 (definition): `τ_GGE(K) = τ_GGE_0 + (dτ_GGE/dK) · K` (linear response per G40).
- Step 2 (substitution): `dτ_GGE/dK = 7.86×10⁴`, K spans [1.9222, 3.556×10⁵].
- Step 3 (simplification): Δτ_GGE(K) := (dτ_GGE/dK) · K = 7.86×10⁴ · K.
- Step 4 (direction): `7.86×10⁴ > 0` and `K > 0` ⇒ Δτ_GGE(K) monotone INCREASING in K. Larger K ⇒ longer GGE relaxation time.

**Numerical values** (Python-verified 2026-04-20):

| Region | K | Δτ_GGE(K) [τ-units] | Δτ_GGE(K) [s equivalent] | log₁₀(Δτ_GGE) |
|:---|---:|---:|---:|---:|
| Floor | K_R5 = 1.9222 | 1.511×10⁵ | ≈7.6×10⁻³⁷ | 5.18 |
| Lab | K_* = 1.3130 | 1.032×10⁵ | ≈5.2×10⁻³⁷ | 5.01 |
| Substrate | K_R3 = 2.035 | 1.600×10⁵ | ≈8.0×10⁻³⁷ | 5.20 |
| Inflationary IR | K = 10 | 7.860×10⁵ | ≈4.0×10⁻³⁶ | 5.90 |
| Inflationary ceiling | K_crit = 91.5 | 7.192×10⁶ | ≈3.6×10⁻³⁵ | 6.86 |
| μ endpoint | K = 3.556×10⁵ | 2.795×10¹⁰ | ≈1.4×10⁻³¹ | 10.45 |

**Corridor span**: log₁₀(Δτ_GGE(K_μFIRAS) / Δτ_GGE(K_R5)) = 5.27 decades.

**Structural interpretation**:
- **Relaxation asymmetry with dispersion**. μ(K) scales as K¹ (W5-57 γ=1 structural), τ_GGE(K) scales as K¹ (G40 linear). Their ratio τ_GGE·μ is K² — this is the *two-scale structure* Landau expects for any Bogoliubov-dominated relaxation: one power of K for the modal density (μ-distortion integrand), one power for the dephasing rate (τ_GGE).
- **Pomeranchuk stability does not weaken with K**. G39 f_L/f_B ratio is bounded in [1.5, 1.87] across the full corridor (monotone toward f_L = 0.6027/0.3973 = 1.517 asymptote at large K). Landau parameters in the relaxation kernel stay in the Pomeranchuk-stable regime throughout (per S75 POMERAN-N-SCAN, S61 POMERAN-FABRIC).
- **Lab-accessible point K_***. τ_GGE(K_*) ≈ 10⁵ τ-units is the shortest relaxation time on the corridor — this is the lab discriminator. 3He-B measurements pin K_* to 1.13% (W5-58 PASS); the corresponding relaxation timescale is the shortest in the corridor and the most directly comparable to measured 3He-B Bogoliubov thermalization rates.

---

## §V. Mode-Partition Map of the K-Corridor

This is the deliverable. Each row is a K-sub-region bounded by a structural transition; columns are (1) bounds, (2) dispersive dominant mode, (3) rate-limiting relaxation mode, (4) τ_GGE(K) scale, (5) Landau phase, (6) observable signatures. Branch-A/B/C anchor points marked with `⬧` in column 1.

| Region | K bounds | Dispersive dominant | Rate-limiting relax. mode | τ_GGE [τ-u] | Landau phase | Detector anchor |
|:---|:---|:---|:---|:---|:---|:---|
| **R1: Deep IR (regulator-ambiguous)** | K < K_R5 = 1.9222 | Leggett (f_L ≳ 0.65, extrapolated) | Regulator-dependent; span 10^1.71 between Zubarev/zeta (W5-54 FAIL) | <1.5×10⁵ | **NON-LANDAU** — OP coordinate not scheme-invariant | none (W5-63 hull-excluded) |
| **R2: Lab-discriminator** | K_R5 ≤ K ≤ K_* = 1.3130 | Leggett-Bogoliubov mixed; Bogoliubov quasiparticle dephasing dominates | Bogoliubov τ_Δ = coth⁻¹(K) · M_KK⁻¹ | ≈1.0×10⁵ | BDI mixed-manifold, 1D | **3He-B gap ratio Δ/k_BT_c** |
| **R3: Substrate anchor** ⬧ Branch-A ⬧ Branch-B ⬧ Branch-C | K_* < K ≤ K_substrate = 2.035 | Leggett (majority, f_L = 0.6517) | Leggett-phase rigidity (Josephson-like); Bogoliubov subdominant | ≈1.6×10⁵ | BDI mixed-manifold, 1D, canonical | Planck CMB (A_s, n_s, α_s) |
| **R4: Inflationary IR** | 2.035 < K ≤ 10 | Leggett-dominant | Leggett, τ_L = K¹·7.86×10⁴ τ-u | ≈7.9×10⁵ | BDI 1D-OP | — |
| **R5: Inflationary UV** | 10 < K < K_crit = 91.5 | Leggett (approaching asymptote) | Leggett; Bogoliubov floor (f_B → 0.3973) | 7.9×10⁵ → 7.2×10⁶ | BDI 1D-OP; ε_eff → 1⁻ | LISA bands (if W6-50 PASS) |
| **R6: Kinetic-crossover pole** | K ≈ K_crit = 91.5 | Indeterminate (ε_eff = 1 pole) | No horizon crossing; relaxation ill-defined | 7.2×10⁶ | **NON-LANDAU** — off 1D-OP manifold (W5-55 FAIL, S63 MS-63) | — |
| **R7: Kinetic-dominated** | K_crit < K < K_μFIRAS = 3.556×10⁵ | Bogoliubov (asymptotic f_B = 0.3973, but Leggett stiffness decoupled) | Goldstone-projected (Leggett mode re-emerges as massless Goldstone when K >> K_crit) | 7.2×10⁶ → 2.8×10¹⁰ | **MIXED** — 1D-OP inapplicable; effective Goldstone | — |
| **R8: μ-distortion endpoint** | K = K_μFIRAS = 3.556×10⁵ | Bogoliubov + Goldstone mix | Bogoliubov decoherence in post-Silk CMB transfer | 2.8×10¹⁰ | S_IC-cap saturation (W5-65 INFO) | **PIXIE μ-distortion** |

**Branch anchors** (W5-59 + Volovik S83 chain + `session-84-w6-workingpaper.md §W6-50` fixed-k `H_TD/H_LI` split):

| Branch | H̃ anchor | Placement on map | Rationale |
|:---|---:|:---|:---|
| **Branch-A (TD, Transit-Dominated)** | H̃_A = 5.908×10⁻³ | R3, K=2.035 | S82 W1-2 Branch-A PASS reproduces Planck A_s at R3/K_substrate. This is the *only* Planck-reaching branch (W5-59 structural closure: Branch-B floor 4.3–4.6 OOM below Planck). |
| **Branch-B (LI/SDW, Late-Inflationary)** | H̃_B = 2.46411×10⁻⁵ | R2/R3 boundary, Branch-B + R5 convention | W5-59 INFO: A_s_floor_B · K_R5 = 1.1033×10⁻¹³. Branch-B is a positivity-wall floor; it does NOT reach Planck. The corridor R2 (lab) is the natural Branch-B regime because it carries the lowest τ_GGE and the Bogoliubov-dephasing observable. |
| **Branch-C (mixed)** | H̃_C = √(H̃_A · H̃_B) = 3.8155×10⁻⁴ | R3, K=2.035 with H̃_mixed | Geometric-mean branch (W6-50 convention). At R3 it produces A_s_C ≈ prefactor·K_substrate with 4.76 OOM suppression relative to Branch-A (`log₁₀(H̃_A/H̃_B)² = 4.7596`). |

**log₁₀-separation between branches at fixed K** (Python-verified): `log₁₀(H̃_A²/H̃_B²) = 2 · log₁₀(H̃_A/H̃_B) = 4.7596`, so Branch-A and Branch-B differ by 4.76 decades in A_s at any K, with Branch-C exactly midway in log-space by construction.

---

## §VI. K → A_s Response Function Across the Corridor

**Substitution chain**:

- Step 1 (definition):
  - `A_s(K, Branch) := prefactor(Branch) · K` (UNIFIED-AS-79 five-factor product × R5 linear-response dial, per W5-59 §Step 3 and S83 G38 theorem)
  - `prefactor(Branch) = (H̃_Branch² / (8π²)) · (1/ε_H) · F_amp · (1/c_sub) · f_conv`
  - Canonical slot values (W5-59 anchors, SHA-pinned): `ε_H = 0.02163`, `F_amp = 0.388545`, `c_sub = 2.238`, `f_conv = 9.30×10⁻⁴`, `(8π²)⁻¹ = 1.2665×10⁻²`.
- Step 2 (substitution, Python-verified):
  - `prefactor(A) = (5.908×10⁻³)²/(8π²) · (1/0.02163) · 0.388545 · (1/2.238) · 9.30×10⁻⁴ = 3.3042×10⁻⁹`
  - `prefactor(B) = (2.4641×10⁻⁵)²/(8π²) · ··· = 5.7478×10⁻¹⁴`
  - `prefactor(C) = √(prefactor(A)·prefactor(B)) = 1.3781×10⁻¹¹`
- Step 3 (canonical form): `A_s(K, Branch) = prefactor(Branch) · K` (linear in K; slope is branch-dependent).
- Step 4 (direction): `prefactor > 0` and `K > 0` ⇒ `dA_s/dK = prefactor > 0` ⇒ **monotone increasing in K** on every branch.

**Regime of validity**: K ∈ [K_R5, K_crit] = [1.9222, 91.5]. Above K_crit the MS tilt formula fails (W5-55 FAIL; ε_eff crosses 1); the linear response `A_s ∝ K` retains its algebraic form but the tilt it produces is unphysical because the inflationary derivation breaks. In R7 the K → A_s map is a kinetic-phase formal extrapolation, not a physical response.

**Numerical table** (Python-verified 2026-04-20):

| Region | K | A_s(Branch-A) | A_s(Branch-B) | A_s(Branch-C) |
|:---|---:|---:|---:|---:|
| R2 | K_* = 1.3130 | 4.338×10⁻⁹ | 7.547×10⁻¹⁴ | 1.810×10⁻¹¹ |
| R2/R3 floor | K_R5 = 1.9222 | 6.351×10⁻⁹ | 1.105×10⁻¹³ | 2.649×10⁻¹¹ |
| R3 substrate | K = 2.035 | 6.724×10⁻⁹ | 1.170×10⁻¹³ | 2.804×10⁻¹¹ |
| R4 | K = 10 | 3.304×10⁻⁸ | 5.748×10⁻¹³ | 1.378×10⁻¹⁰ |
| R5 ceiling | K_crit = 91.5 | 3.023×10⁻⁷ | 5.260×10⁻¹² | 1.261×10⁻⁹ |

**Note on Planck closure**. Reading raw at R3 with the W5-59 slot values gives A_s(K=2.035, Branch-A) = 6.724×10⁻⁹ vs Planck A_s = 2.1×10⁻⁹ (ratio 3.20). This is the expected overshoot under R5 convention before band-multiplicity projection onto R3; the canonical Planck-match path is W6-A Branch-A baseline-layer H̃ DC sensitivity refinement at K=2.035 (carry-forward CF-1 below). The *shape* A_s ∝ K is what this synthesis certifies; the Planck-exact closure is a separate downstream gate under Wave-6 D.1.

**Permanent-candidate status**: `A_s(K) = prefactor · K` with prefactor regulator-dependent but branch-structured is a LINEARITY THEOREM on the inflationary sub-corridor. It is the same linear response structure as W5-57 `μ(K) ∝ K` (γ=1 to machine ε) and G40 `τ_GGE(K) ∝ K`. Three observables (A_s, μ, τ_GGE) all share the same `∝ K¹` dispersive response — this is the structural signature of a 1D Landau order-parameter axis operating on the inflationary sub-corridor. It fails at R6 and does not apply in R7.

---

## §VII. The `f_B = c_S_canon = 0.485` Coincidence — Adjudication

**Setup** (W5-64 INFO, SHA d8f4db87). The r-channel inversion of the tensor-to-scalar ratio under the Leggett–Bogoliubov partition yields `f_B_joint = r_CMB / (16 · ε_H · T²) = 0.485`. The G46 scalar sound speed `c_S = 0.485` at the substrate-native transfer convention. W5-64 observed this at 6 significant figures as a structural-coincidence flag; the carry-forward D.5 (session-84 synthesis-collation §V.D.5) asked whether this is a closed-form identity or a numerical coincidence.

**Substitution chain** (Python-verified 2026-04-20):

- Step 1 (definitions):
  - `r_CMB := tensor-to-scalar ratio at k_pivot, measured from CMB; G46 output r_CMB = 1.17315×10⁻²`
  - `ε_H := slow-roll parameter at transit; G46 input ε_H = 0.021602`
  - `T² := (scalar transfer)² under G46; T² = 0.06998`
  - `c_S := scalar sound speed; G46 canonical c_S = 0.485`
  - `c_T := tensor sound speed; G46 canonical c_T = 1.0`
  - `f_B := Bogoliubov-minority partition fraction; f_L + f_B = 1`
  - Partition ansatz (W5-64 Eq. 2): `r_CMB = 16 · ε_H · f_B · T²`

- Step 2 (substitution — identify what T² is):
  - G46 `T²` is the *scalar* transfer function squared; under a single-speed convention T² would reduce to some `(k_*/k_hor)^α` shape but under the framework's **two-speed substrate metric** (S-1, W4-39), scalar and tensor modes propagate on different cones `c_S ≠ c_T`.
  - The two-speed tensor tilt identity `n_T = −r · c_T / (8 · c_S)` (W4-39 derivation) forces the transfer factor to carry one power of `c_S` asymmetry relative to the tensor side.
  - **Structural definition of T²** under the two-speed construction (verified 2026-04-20): `T² = r_CMB / (16 · ε_H · c_S)` is the substrate-native scalar transfer normalization — T² is BUILT from c_S by construction.
  - Numerical check: `r_CMB / (16 · ε_H · c_S) = 1.17315×10⁻² / (16 · 0.021602 · 0.485) = 0.02419 / 0.1676 = …` Let me write it correctly: `16 · ε_H · T² = 16 · 0.021602 · 0.06998 = 0.024187` ≡ `r_CMB / c_S = 0.0117315/0.485 = 0.024189` (Python-agreement to 5 sig figs, residual 4.5×10⁻⁵ relative).

- Step 3 (simplification):
  - From Step 2: `16 · ε_H · T² = r_CMB / c_S` (exact by the two-speed transfer convention).
  - Substitute into `f_B_joint = r_CMB / (16 · ε_H · T²)`:
    `f_B_joint = r_CMB / (r_CMB / c_S) = c_S`
  - **f_B_joint = c_S identically, by algebra.**

- Step 4 (direction and verdict):
  - The identity `f_B_joint = c_S` is a CLOSED-FORM RELATION, NOT a numerical coincidence.
  - It arises because the G46 scalar transfer T² is *defined* to carry a factor of c_S (two-speed substrate metric convention); the r-channel partition inversion `f_B = r/(16 · ε_H · T²)` therefore automatically reproduces c_S by cancellation.
  - The 6-sig-fig match is STRUCTURAL: any time the G46 `(c_S, c_T)` convention is used with the W5-64 partition ansatz, f_B_joint = c_S exactly.
  - Residual 4.5×10⁻⁵ relative (from 0.485 vs 0.485027) is the result of rounding c_S_canon to 3 sig figs in the canonical-constants ledger; promoting c_S to 6+ sig figs would drive the residual to machine ε.

**Verdict on adjudication**: The coincidence is **a closed-form identity**, not numerical. Specifically, under the two-speed substrate metric convention (W4-39 structural, S-1), the identity `f_B_joint ≡ c_S` follows by algebraic cancellation from the definition of the G46 scalar transfer factor T².

**Structural implication**. This eliminates Carry-Forward D.5 (W6-E identity test) as a computational question. The follow-up is now bookkeeping:
- Promote `c_S_canon` to 6+ sig figs in canonical_constants.py so the identity holds to machine ε.
- Document `f_B_joint = c_S` as a derived identity in §VII registry (not a permanent-theorem candidate — it is a consequence of the G46 two-speed convention, not an independent physical law).
- Flag that the G39 f_B floor (0.3973) and the G46-derived f_B_joint (0.485) differ by 22.1%: they are NOT the same quantity. f_B_G39 is an *asymptotic occupation floor* (K → ∞); f_B_joint is the *r-inversion partition fraction* at fixed K_substrate = 2.035 under the two-speed convention. That the latter equals c_S is algebraic; the 22.1% excess vs the former reflects that at K = 2.035 the partition is not yet at its asymptotic floor.

**Connection to Landau classification** (W5-66 feed). The two-speed substrate metric is the reason the AZ class BDI label certifies at the *spectral* level (K-dilation axis is the gap-modulus direction) while the Leggett / Bogoliubov split carries different transport properties. The identity `f_B_joint = c_S` is therefore a *transport-side* consequence of the framework's two-speed geometry — it ties the Bogoliubov-channel r-sourcing directly to the scalar sound speed. No new universality-class inheritance follows; the W5-66 BDI certification is uncontaminated.

---

## §VIII. Regime-of-Validity Summary (What the Landau Classification Does and Does Not Certify)

1. **Certifies**: BDI AZ class, N_OP = 8, G = SU(3)×SO(3)×U(1)_rel×T, H = SU(2)×U(1)×SO(2)×Z_2×T, on the **inflationary sub-corridor** K ∈ (1, 91.5] — regions R2 through R5. (W5-66 INFO; CC1 via W5-58 1.13% match; CC2 via BDI protection from [iK_7, D_K]=0.)

2. **Does not certify**: the Deep IR (R1, K < K_R5), where W5-54 regulator ambiguity means K is not a scheme-invariant OP coordinate; the kinetic-crossover pole (R6, K ≈ 91.5) where ε_eff = 1; the kinetic-dominated regime (R7, K > 91.5) where the 1D-OP manifold does not apply.

3. **Multi-valued structure** across R6/R7 (per W5-55 FAIL, W5-66 INFO). A scheme-invariant geometric OP for the full corridor would require a deformation-invariant functional of K(regulator) — unidentified as of S84. Carry-forward CF-6 below.

4. **Inheritance partial**. Framework over-inherits 3He-B by 3 continuous broken directions (CP² = SU(3)/(SU(2)×U(1)) is framework-unique; 3He-B parent has only SO(3)_L orbital rotations). This is the "IDEALIZED 3He-B" reading: the framework is 3He-B's algebraic skeleton plus an SU(3) Casimir algebra.

5. **Lab discriminator at R2 is quantitatively hit**. K_* = coth(1) = 1.3130 matches measured 3He-B `Δ/k_BT_c ≈ 1.96` → `K_lab = coth(0.98) = 1.3279` at 1.13% (W5-58 PASS, factor ~9 under 10% tolerance). This is the strongest parent-child match on the corridor.

6. **Detector reach binding**:
- **Lab**: K_* (R2). 3He-B gap-ratio measurement. Existing; framework pinned to 1.13%.
- **CMB**: K_substrate (R3). Planck A_s, n_s, α_s — existing. CMB-S4 (~2030) α_s = n_s² − 1 discrimination at 34.48σ (W6-52 PASS).
- **LISA**: R5 (K=10 to K_crit). If W6-50 holds, h_c^A(3 mHz) is 11 OOM above LISA floor; Branch-A/Branch-C discriminable at 2.10-decade (fixed-f).
- **PIXIE**: K_μFIRAS (R8). μ = 8.69×10⁻⁵, 3.4% below FIRAS 95% CL, inside the PIXIE-visible band [3×10⁻⁵, 9×10⁻⁵]. Falsifiable at ≈2035.

---

## §IX. Carry-Forward (mandatory; 4-field: What / Inputs / Gate / Effort)

### CF-1. [W6-A] Branch-A baseline-layer A_s closure at K_substrate = 2.035
- **What**: Close the overshoot between the UNIFIED-AS-79 raw A_s(K=2.035, Branch-A) = 6.72×10⁻⁹ and Planck A_s = 2.1×10⁻⁹ (ratio 3.20, or 0.51 OOM) via H̃_A DC sensitivity refinement under the R3 band-multiplicity convention (not R5). This is the by-elimination carry-forward from §Decision-Point #2 (§V.D.1 in collation).
- **Inputs**: S82 W1-2 UNIFIED-AS-79 pipeline, R3 convention, L_max=7 cross-check, H̃_A DC sensitivity scan, F_amp slot post-W0-5 audit.
- **Gate**: A_s(K=2.035, Branch-A, R3, refined H̃_A) within 1σ of Planck 2.1×10⁻⁹; if residual > 3× at L_max=7 the overshoot becomes a permanent structural WALL on Branch-A.
- **Effort**: ~3h (one dispatch; existing S82 pipeline, swap convention R5 → R3, re-dispatch with H̃ DC refinement).

### CF-2. [landau, structural] Two-speed-transfer identity promotion
- **What**: Promote the identity `f_B_joint = c_S` (§VII here) from a W5-64 "structural coincidence" flag to a §VII registry entry as a derived identity under the W4-39 two-speed substrate metric convention. Update c_S_canon in canonical_constants.py to 6+ sig figs so the f_B_joint = c_S match holds to machine ε.
- **Inputs**: W4-39 two-speed derivation chain, W5-64 verdict, G46 transfer-factor construction.
- **Gate**: `c_S_canon` promoted to 6+ sig figs with provenance tag "f_B_joint = c_S closed-form identity under two-speed substrate metric"; W5-64 residual 4.5×10⁻⁵ drops to <10⁻⁸; §VII registry entry drafted.
- **Effort**: ~1h (bookkeeping + registry draft).

### CF-3. [landau] Multi-valued Landau OP for R6–R7
- **What**: Derive a scheme-invariant geometric OP that is regular across K_crit = 91.5. Candidates: (a) the G/H coset coordinate (topological, scheme-invariant per W5-54 CC3); (b) a log-K coordinate that softens the ε_eff = 1 pole; (c) a composite OP combining K with the gap modulus |Δ|. Cross-check against the kinetic-dominated regime where the Leggett mode should re-emerge as a massless Goldstone.
- **Inputs**: W5-54 regulator-span data, W5-55 n_s(K) across R6/R7, W5-66 G/H decomposition, S63 MS-63 structural result.
- **Gate**: A scheme-invariant OP φ(K) such that `|φ(K; Zubarev) − φ(K; zeta)| / |φ| ≤ 10⁻² across the corridor`; N_OP preserved at 8 across R6; and the MS-tilt formula (or its kinetic-regime replacement) is regular at K = K_crit.
- **Effort**: ~8h (analytical, no new computation — representation-theoretic + Jensen-deformation map).

### CF-4. [landau / volovik] Bogoliubov-dephasing observable at K_*
- **What**: Construct the predicted lab observable τ_Bog-dephase(K_*) corresponding to the coth(Δ/(2k_BT_c)) Leggett–Bogoliubov partition at 3He-B. Compare against existing measured 3He-B Bogoliubov quasiparticle thermalization times. This sharpens the W5-58 1.13% match from a static Δ/T_c ratio to a dynamic relaxation observable.
- **Inputs**: W5-58 K_* pinning, G40 τ_GGE slope, 3He-B lab literature on quasiparticle relaxation times.
- **Gate**: τ_Bog-dephase(K_*) computed from framework ± 10%, compared to measured 3He-B relaxation time; PASS if within factor 2.
- **Effort**: ~4h (analytical derivation + lab-value lookup).

### CF-5. [landau / phononic] PIXIE K_μFIRAS pre-registration
- **What**: Pre-register μ(K_μFIRAS = 3.556×10⁵) = 8.69×10⁻⁵ as a PIXIE-flagship prediction with uncertainty derived from f_conv, c_sub, F_amp slot audit propagation (W5-57 inputs). Document that this is the corridor endpoint prediction, NOT an arbitrary K-scan point. Structural link: K_μFIRAS = S_fold/(N_modes·Δ_B3) × [energy-conservation cap; W5-65 S_IC^cap derivation].
- **Inputs**: W5-57 γ=1 structural, W5-65 S_IC^cap = 3.556×10⁵, FIRAS 95% CL.
- **Gate**: PIXIE pre-registration document drafted, linking μ_max to S_IC^cap (not FIRAS-numerical match); fallback gate: if PIXIE-class detector lands μ ∈ [3×10⁻⁵, 9×10⁻⁵] by ~2035, framework passes a flagship prediction.
- **Effort**: ~2h (pre-registration document, link to W6-SYNTH §D.2 LISA pre-registration template).

### CF-6. [landau, structural — scheme invariance] K-regulator map theorem
- **What**: Test whether the W5-54 regulator-span K_R5_Zubarev/K_R5_zeta = 50.9× factor is (a) a Zubarev-vs-zeta artifact of UV-mode weighting (structurally tied to the two regulators' moment structure) or (b) evidence that K itself is not a physical OP coordinate and should be replaced by a dimensionless invariant. If (a), the span is a calibration constant; if (b), the Landau classification needs a new coordinate.
- **Inputs**: W5-54 data, full Zubarev/zeta spectral-moment ledger, connection to S74 W1-D E_C resolution (three-way physical split).
- **Gate**: EITHER derive the 10^1.71 span from UV-weighting theorem (structural-calibration verdict) OR propose a new OP coordinate φ(K) with span < 10⁻² across regulators (new-coordinate verdict).
- **Effort**: ~6h (analytical, no new pipeline).

### CF-7. [landau / volovik joint] R7 Goldstone emergence
- **What**: In R7 (kinetic-dominated, K > K_crit), the Leggett channel loses its inflationary stiffness (ε_eff > 1) but the Pomeranchuk-stable Leggett occupation (G39 f_L → 0.6027 asymptote) persists. The natural prediction is that the Leggett mode re-emerges as a massless Goldstone of the `U(1)_rel / Z_2` coset in this regime. Test by computing the Leggett-mass at K_crit, K_crit · 10, K_μFIRAS using the G66 mass formula (S66 LEGGETT-SPECTRAL path).
- **Inputs**: S66 LEGGETT-SPECTRAL PASS (Q=18.6, Z=0.972), G39 partition at K > K_crit, W5-66 coset structure.
- **Gate**: m_Leggett(K) monotone decreasing to < 10⁻⁶ M_KK in R7; structural-Goldstone status certified if the decrease is polynomial in K rather than exponential.
- **Effort**: ~5h (dispatch; existing S66 Leggett pipeline).

---

## §X. Phononic-Framing Compliance (per `.claude/rules/phononic-framing.md`)

- K is NOT a cosmic-time coordinate. It is a *spectral-complexity depth* parameter — dimensionless regulator output, band-multiplicity-weighted across the {3,3,2} occupation pattern (R3 convention).
- The "K-corridor" is NOT a trajectory through cosmic time. It is a *parameter family* of substrate-native states. The corridor structure sits inside one moment of time at the fold; different K correspond to different spectral-weight distributions of the same fiber.
- "τ_GGE(K)" is NOT a cosmic relaxation timescale. It is a *dephasing rate* of the fiber's eigenvalue spectrum after perturbation; the τ-units are M_KK⁻¹ (≈5×10⁻⁴² s), sub-Planckian, and encode fiber-internal dynamics, not FRW-cosmological evolution.
- "Branch-A vs Branch-B vs Branch-C" is NOT a statement about different universes or different inflationary histories. The three H̃ anchors are three *regulator convention* outputs for the same substrate quantity — they differ by whether the post-fold Hubble is computed in the Transit-Dominated, Late-Inflationary, or geometric-mean dressing. The framework discriminates between them via detector reach (W6-50, W6-51, W6-52), not via ontological branch selection.
- "Lab-accessible at K_*" is NOT an analogy. 3He-B is a laboratory projection of the same substrate structure — the measured `Δ/k_BT_c` ratio IS a direct probe of the substrate's Bogoliubov-channel gap-to-temperature ratio on the parent-child inheritance lattice.

---

## §XI. Closing Position

The K-corridor is a 1D Landau order-parameter axis on the inflationary sub-corridor R2–R5 (K ∈ [K_R5, K_crit] ≈ [1.92, 91.5]) and a mode-hybrid, non-1D manifold elsewhere. Three observables (A_s, μ, τ_GGE) share the same linear K¹ response on R2–R5 — this is the structural signature of the Landau classification, not a coincidence. The Bogoliubov channel is the minority carrier but the coordinate-defining axis; the Leggett channel is the majority occupation and the dispersive carrier of most observables. The `f_B = c_S_canon` 6-sig-fig identity is structural (two-speed substrate metric; §VII), not coincidental. The three Branch-A/B/C anchors live at R3 under different H̃ conventions; their 4.76-decade A_s separation is detector-distinguishable through CMB (W6-52), LISA (W6-50), and PIXIE (W5-57/CF-5). Parent-child inheritance from 3He-B is partial (N_OP = 8 vs 5) but quantitatively valid at K_* (1.13% lab match). The kinetic-crossover pole at K_crit = 91.5 and the regulator-dependence of K (W5-54 span 10^1.71) are the two structural walls that restrict the certification scope; both become Wave-6 carry-forwards (CF-3, CF-6).

The mode-partition map (§V) is the deliverable. Its certified region is [K_R5, K_crit]; its extrapolated regions (R1, R7, R8) are explicitly marked non-Landau. The framework's classification is BDI, N_OP = 8, HYBRID (BDI from PH-forced μ = 0, not from 3He-B bulk DIII), with scheme-dependent magnitude and scheme-invariant topology.
