# Session 82 Synthesis: Substrate-IC Corridor Phenomenology via BCS Coherence Mapping

**Date**: 2026-04-18
**Agent**: landau-condensed-matter-theorist
**Source Documents**:
- `sessions/archive/session-82/session-82-results-workingpaper.md` (§V.D W2-4, §V.I W2-9, §VI.F W3-6, §VI.K W3-11)
- `sessions/archive/session-82/session-82-OOM.md` (§II Bands 0 to +1 OOM; §IV.A walls; §IV.B measurements)
- `.claude/agent-memory/landau-condensed-matter-theorist/MEMORY.md`

---

## I. Session Outcome

Under the BCS-coherence reading of the substrate-IC corridor `S_IC^GGE ∈ [1, 3.556 × 10⁵]` (5.551 OOM wide), the substrate's own quasiparticle occupation at the CMB pivot sits at `T_eff/Δ = 0.9295` — within 7% of the isothermal point `T_eff = Δ`. This is the **weak-coherence, pair-activated regime**: neither fully coherent (`T ≪ Δ`) nor fully decoherent (`T ≫ Δ`), but the unique intermediate point set by the S43 band-multiplicity (3/3/2) weighting of coth(Δ_i/2T_i^GGE) across B1/B2/B3. The 3.20×-Planck framework point (K=2.035) is **structurally anchored** by three independent BCS diagnostics: (a) pair-breaking Bogoliubov activation barely opens (B3 gap `2Δ_B3 = 0.352 M_KK` is thermally accessible at `T_eff ~ 0.18`), (b) Leggett inter-band phase mode is marginally active (K_Leggett ≈ 1.10 < 2.035 ⇒ Leggett-populated), and (c) the W3-11 proof `ξ_BCS ∥ ℓ_phonon` on `Δ_BCS(τ)` means the CMB pivot inherits Δ_BCS as the sole parent scale, so K is not a free dial — it is fixed by the substrate's spectral gap. No K along the 5.55-OOM corridor admits exact Planck match (structural wall K ≥ 1 forbids `K_matching^nominal = 0.636`); the framework's PASS-F2 at K=1 survives by a factor-2 band with 0.196 OOM margin, and the K=2.035 primary adds 0.309 OOM on top of that.

---

## II. Key Results

### II.A. K → T_eff/Δ_BCS mapping across the corridor

**Result**: Inversion `T_eff/Δ = 1/[2 · arccoth(K)]`; corridor spans `T_eff/Δ ∈ [0, 1.78 × 10⁵]` over `K ∈ [1, 3.556 × 10⁵]`. **PHONONIC** (BCS coherence regime labeling of the GGE quasiparticle occupation).

**Substitution chain** (pre-registered, [SIGN] trigger):

```
Step 1 (def):   K ≡ S_IC^GGE = coth(Δ/(2T_eff))       [W2-4 canonical form; Volovik 3He-B]
Step 2 (subst): let x ≡ Δ/T_eff; then K = coth(x/2)
Step 3 (simpl): arccoth(K) = x/2 = (1/2) · ln[(K+1)/(K−1)]
                ⇒  T_eff/Δ = 1/x = 1 / [2 · arccoth(K)]
                           = 1 / ln[(K+1)/(K−1)]
Step 4 (dir):   K → 1⁺  ⇒  T_eff/Δ → 0⁺   (fully coherent: T_eff ≪ Δ, ground-state BCS)
                K → ∞    ⇒  T_eff/Δ → ∞     (fully decoherent: T_eff ≫ Δ, normal-state-like)
```

**Python-verified table** (per-K inversion; cross-checked vs W2-4 CC2 per-band coth identity at machine precision):

| K | T_eff/Δ | Regime label | BCS classification |
|:-:|:-------:|:-------------|:------------------|
| 1.000 + ε | 0.0689 | Fully coherent (floor) | ground-state BCS; all modes paired |
| 1.100 | 0.3285 | Strong-coherence | T ≪ Δ; Bogoliubov-activation exponentially suppressed |
| 1.500 | 0.6213 | Weak-coherence | T ~ Δ/2; pair-breaking Boltzmann factor ~ e⁻¹ |
| **2.035** (PRIMARY) | **0.9295** | **Near-isothermal (T ≈ Δ)** | **Pair-breaking activated; Leggett populated** |
| 3.000 | 1.4427 | Supra-isothermal | T > Δ; Bogoliubov-continuum dominates |
| 10.00 | 4.983 | Strong-decoherence | T = 5Δ; BCS amplitude remains but phase thermal |
| 100.0 | 50.00 | Classical regime | T = 50Δ; coth ≈ 2T/Δ (Rayleigh-Jeans) |
| 1000. | 500.0 | Normal-state analog | gap irrelevant; `n_k ≈ T/ω` |
| 3.556 × 10⁵ | 1.778 × 10⁵ | Equipartition cap | W3-6 energy-conservation ceiling |

**Per-band reproduction** (CC2 machine-epsilon identity verified):
- B2 (flat): `x = 1.1533`, `T/Δ = 0.867`, `coth(x/2) = 1.9222` ✓
- B1 (acoustic): `x = 1.0674`, `T/Δ = 0.937`, `coth(x/2) = 2.0484` ✓
- B3 (softest): `x = 0.9888`, `T/Δ = 1.011`, `coth(x/2) = 2.1849` ✓

**Structural content**. K=2.035 corresponds to per-mode occupation `n_k = 0.518` — the substrate is in its own **weakly-excited BCS phase**, with roughly one thermal quantum per every two pair modes. The proximity to T_eff = Δ is NOT a coincidence: it is the statement that the GGE Lagrange multipliers `T_k^GGE` per band are tuned by the substrate's own spectral action to saturate the individual pair gaps — a condition that Volovik's 3He-B correspondence (paper 25, §V) identifies as the relaxed post-quench fixed point of the GGE. The fabric sits at its own BCS activation threshold, permanently.

### II.B. Leggett-vs-Bogoliubov manifold diagnosis at K = 2.035

**Result**: K = 2.035 lies in the **mixed manifold regime**, with dominant contribution from the Leggett inter-band phase-coherence mode and sub-leading activation of pair-breaking Bogoliubov quasiparticles. **PHONONIC** (quasiparticle-manifold diagnosis of the substrate's spectral excitation).

The 8-mode B1/B2/B3 band structure of the substrate Dirac spectrum supports two structurally distinct quasiparticle manifolds at fold:

**Bogoliubov (pair-breaking) manifold**:
- Excitations: single-quasiparticle pair-breaking at threshold `ω_B_i ≥ 2Δ_B_i`
- Per-band thresholds: `2Δ_B1 = 0.929`, `2Δ_B2 = 1.541`, `2Δ_B3 = 0.352` (all in M_KK)
- Softest threshold `2Δ_B3 = 0.352` is thermally accessible at `T_eff_B3 = 0.178` (i.e., `T ≈ 2Δ_B3/2`), since `x_B3 = 0.9888` gives Boltzmann factor `e^(−x_B3) = 0.372` — not exponentially suppressed.

**Leggett (collective inter-band phase) manifold**:
- Excitations: collective oscillation of relative phase between bands, activated when `T_eff` exceeds the interband splitting `Δ_Leggett ~ min(|Δ_B_i − Δ_B_j|) = 0.3061` (B1↔B2 splitting).
- Activation threshold: K_Leggett ≈ coth(Δ_B1/Δ_Leggett) = **1.101** (Python-verified).
- Since K_canonical = 2.035 > K_Leggett = 1.101, the Leggett manifold is **populated**.

**Mixing diagnosis**. Per W3-11 (§VI.K.4) under Scenario A (Landau-damping onset), K*(τ) tracks the pair-breaking gap 2Δ, so the collective (Leggett) and pair-breaking (Bogoliubov) thresholds co-scale. This is the W3-11 structural finding: ξ_BCS ∥ ℓ_phonon on `Δ_BCS(τ)` means the two manifolds cannot be separated by a τ-deformation — they share the SAME parent gap. At K = 2.035 the corridor position is `log(K−1)/log(K_ceil−1) = 0.27%` into the corridor by the K−1 proxy, but by the full log-width it is 5.56% — either way, deep in the **near-floor** region of the corridor, where the BCS amplitude is preserved and the excitation content is a **superposition of activated Bogoliubov pair-breaking (B3 soft) + populated Leggett mode (B1↔B2 inter-band phase)**.

**Cross-check against W2-9 (multi-pair Pauli wall)**: W2-9 showed `E_cond(N=2)/E_cond(N=1) = 1.601 < 3` (FAIL). The saturation arises because Pauli-blocking of the B1 flat-band level (after the first pair) leaves B2/B3 channels to absorb further pairs with weaker off-diagonal coupling. This is a **pair-breaking-manifold** statement: adding pairs in the Bogoliubov sector saturates because the softest channel is exhausted. It does NOT constrain the Leggett manifold, which is a collective inter-band mode orthogonal to adding pairs. So at K = 2.035 the Leggett populating channel remains viable even after the pair-breaking channel saturates — consistent with the corridor floor being dominated by Leggett collective modes while the ceiling is set by Bogoliubov pair-breaking energy.

### II.C. GGE relaxation timescale τ_GGE(K)

**Result**: `τ_GGE(K) = π·K / (4·Δ_BCS)` in natural units. **Monotone increasing** in K across the entire corridor. At K=2.035, τ_GGE = 3.44 /M_KK (= 3046× dt_transit). **PHONONIC** (relaxation timescale of the substrate's GGE quasiparticle distribution).

**Substitution chain** ([SIGN] trigger):

```
Step 1 (def):   τ_GGE = π·ℏ / [4·Δ·tanh(Δ/(2T))]    [standard quenched BCS; Anderson-Morel]
Step 2 (subst): tanh(Δ/(2T)) = 1/K (from K = coth(Δ/(2T)))
Step 3 (simpl): τ_GGE(K) = π·K / (4·Δ)              [ℏ = 1, Δ in M_KK]
Step 4 (dir):   dτ_GGE/dK = π/(4Δ) > 0
                ⇒  τ_GGE is monotone-increasing in K
                ⇒  K floor (K=1): τ_GGE_min = π/(4Δ) = 1.69 /M_KK (SHORT relaxation)
                ⇒  K ceil (K=3.556e5): τ_GGE_max = 6.02e5 /M_KK (LONG relaxation)
```

**Python-verified table** (Δ_BCS = 0.4643 M_KK, dt_transit = 1.13e−3 /M_KK):

| K | τ_GGE (/M_KK) | τ_GGE / dt_transit | Regime |
|:-:|:-------------:|:------------------:|:-------|
| 1.000 | 1.692 | 1.50 × 10³ | SHORT (fast GGE equilibration) |
| 1.500 | 2.537 | 2.25 × 10³ | short |
| **2.035** | **3.442** | **3.05 × 10³** | **short (fast relaxation at K_primary)** |
| 10.00 | 16.92 | 1.50 × 10⁴ | medium |
| 100.0 | 169.2 | 1.50 × 10⁵ | long |
| 1000. | 1692. | 1.50 × 10⁶ | long |
| 3.556 × 10⁵ | 6.015 × 10⁵ | 5.32 × 10⁸ | LONG (equipartition ceiling) |

**Regime assignment of the 5 readings**:
- R1 (K=2.185), R2 (K=2.049), R3 (K=2.035), R5 (K=1.922): ALL cluster at τ_GGE/dt_transit ~ 3 × 10³ → **SHORT-RELAXATION END** of corridor.
- R4 (K=15.95): τ_GGE/dt_transit = 2.4 × 10⁴ → one OOM longer, but still short-relaxation quadrant.

All five readings occupy the **short-relaxation 3-OOM band** of the corridor, consistent with W3-6's finding that the ceiling is a conservation envelope rather than a dynamical attractor. The corridor's 5.55 OOM width is mostly the long-relaxation tail; the **physical readings all avoid it**.

**Cross-check against S61 GGE-THERM-61** (cited in W2-4): the Thouless time / transit ratio was reported as 2625×. That bounds how much the GGE occupation can drift during transit; since the five readings have τ_GGE/dt_transit ~ 10³ > 2625×, the GGE occupation is preserved at leading order through the fold — the substrate's own relaxation is slow compared to the transit it undergoes. This is the Volovik 3He-B-correspondence condition: the post-transit state inherits the pre-transit GGE intact.

### II.D. A_s(K) response function across [1, 3.556 × 10⁵]

**Result**: `A_s(K) = A_s_W1-2 · K = 3.299 × 10⁻⁹ · K`; the linear response is **proportional, structural, and without free parameters**. `K_matching^nominal = 0.636` would give exact Planck match but is **UNREACHABLE** (K ≥ 1 wall); the minimum-K structural floor gives `A_s(K=1)/A_s_Planck = 1.571` (+0.196 OOM; the W1-2 PASS-F2 verdict). **PHONONIC** (linear response of scalar spectrum to substrate squeezing factor).

**Python-verified response table** (10 log-spaced K points across the full corridor):

| K | A_s(K) | A_s(K) / A_s_Planck | log₁₀(A_s/A_Planck) | Band verdict |
|:-:|:------:|:-------------------:|:-------------------:|:-----------:|
| 1.000 (floor) | 3.299 × 10⁻⁹ | 1.571 | **+0.196** | **PASS-F2** |
| 1.500 | 4.949 × 10⁻⁹ | 2.356 | +0.372 | PASS-F3 |
| **2.035 (R3 primary)** | **6.715 × 10⁻⁹** | **3.198** | **+0.505** | **PASS-F4 (factor-3 band)** |
| 7.046 | 2.325 × 10⁻⁸ | 11.07 | +1.044 | FAIL-GT10 |
| 33.10 | 1.092 × 10⁻⁷ | 52.00 | +1.716 | FAIL |
| 155.5 | 5.129 × 10⁻⁷ | 244.2 | +2.388 | FAIL |
| 730.3 | 2.409 × 10⁻⁶ | 1147. | +3.060 | FAIL |
| 3431. | 1.132 × 10⁻⁵ | 5390. | +3.732 | FAIL |
| 1.612 × 10⁴ | 5.316 × 10⁻⁵ | 2.53 × 10⁴ | +4.403 | FAIL |
| 7.570 × 10⁴ | 2.497 × 10⁻⁴ | 1.19 × 10⁵ | +5.075 | FAIL |
| 3.556 × 10⁵ (ceil) | 1.173 × 10⁻³ | 5.59 × 10⁵ | +5.747 | FAIL (ceiling) |

**Key landmarks**:
- `K_matching_nominal = A_s_Planck / A_s_W1-2 = 0.6366` — **violates K ≥ 1 wall; unreachable on corridor**
- `K_PASS_F3_edge = 3.00` (factor-3 band upper edge) — R3, R2, R5 PASS; R1 barely PASS
- `K_FAIL_GT10_onset ≈ 6.37` — all five documented readings PASS below this
- `K_FIRAS_structural = 3.68 × 10⁵` — from µ ∼ K scaling at FIRAS bound 9 × 10⁻⁵; effectively coincides with W3-6 structural cap `S_IC^cap = 3.556 × 10⁵` (within factor 1.03)
- `K = 2.035` position: 0.27% of corridor by K-1 proxy; 5.56% by log-width

**Substitution chain for K_FIRAS**:
```
Step 1 (def):   µ_CMB ∝ ∫ S_IC(k) · W_µ(k) dk       [Chluba kernel; W2-14]
Step 2 (subst): substrate-IC reading: S_IC(k_pivot) = K       [W2-4]
                at K=2.035, µ_W2-14-like = 4.98e−10
Step 3 (simpl): µ(K) / µ(K=2.035) = K / 2.035      [linear scaling]
Step 4 (dir):   FIRAS bound: µ < 9e−5
                ⇒ K_FIRAS = 2.035 · 9e−5 / 4.98e−10 = 3.68 × 10⁵
                ≈ 1.03 × S_IC^cap (W3-6 energy-conservation ceiling)
```

**The K-independent observational match is impossible** under the substrate-IC reading: any K ≥ 1 over-amplifies Planck by at least factor 1.571 = +0.196 OOM. The framework's only path to PASS is the factor-2 or factor-3 band; at the K=1 floor it clears factor-2 by 0.105 OOM; at K=2.035 primary it clears factor-3 by 0.168 OOM. The PASS is permanent but tight — the corridor is **over-amplifying by construction**, and only the near-floor region is observationally viable.

### II.E. 4 PASS vs 1 FAIL (R4) diagnosis from BCS perspective

**Result**: R4 (legacy `n_pairs=59.8/8`) FAILs not because the numerator-denominator scheme is wrong, but because it **mixes two different BCS statistics**: a Fock-space pair count (`n_pairs`, a many-body integer) normalized by a mode count (8 single-particle modes on the fiber). The resulting K = 15.95 represents an average occupation per *mode* rather than per *band-averaged quasiparticle*, which is not the correct per-mode squeezing factor entering `|v_k|² = S_IC/(2ω)`. **PHONONIC** (convention-consistency diagnosis at the BCS many-body level).

**Why R4 fails structurally**. Per the W2-4 canonical formula `S_IC^GGE(k) = 1 + 2 n_k^GGE` where `n_k^GGE = 1/(e^(ω_k/T_k) − 1)` is a **per-mode thermal occupation**, the natural averaging over 8 modes is an average of `1+2n_k` (the squeezing factor itself) — not an average of `n_pair` (pair count) over mode count. The R1/R2/R3/R5 readings all satisfy this:
- R1: `S_IC(k_B3)` = single-mode squeezing at B3
- R2: geometric mean of `S_IC` over three band samples (Haar-isotropic)
- R3: arithmetic mean of `S_IC` weighted by band multiplicity 3/3/2 (S43 canonical)
- R5: `S_IC(k_B2)` = single-mode squeezing at B2

R4, however, computes `K_R4 = 1 + 2·(n_pairs/N_modes) = 1 + 2·(59.8/8) = 15.95`. The quantity `n_pairs` is the total Bogoliubov pair count (from S38 transit), which is NOT a per-mode occupation — it is a **many-body integer** that collapses the per-mode Fock structure. Dividing by 8 modes averages pair count by mode, a quantity dimensionally distinct from `n_k^GGE`. The BCS Fock-space distinction is: `n_pairs = Σ_k ⟨b_k^† b_k⟩` where `b_k` is a Cooper-pair operator, while `n_k^GGE = ⟨a_k^† a_k⟩` where `a_k` is a single-mode Bogoliubov operator. **These differ by the pair correlator** — in the GGE, `n_pairs ≠ (1/2)Σ_k n_k^GGE` unless the system is in a BCS coherent state, which the post-transit GGE is not (it is a non-equilibrium 3He-B-analog).

**Evidence cited**:
1. **W2-9 confirms the 8-mode Fock structure is Pauli-blocked beyond N=1 pair**: the ratio `E_cond(N=2)/E_cond(N=1) = 1.601 < 3` (FAIL). This means the 8-mode fiber does NOT naively support 59.8 pairs in an additive-binding sense — the pair count is distributed across many bands and correlated by Pauli blocking. Dividing 59.8 by 8 modes is therefore **a double-counting of pair correlations**, which the per-band `S_IC^GGE(k)` formula correctly resolves.
2. **W3-11 confirms `ξ_BCS ∥ ℓ_phonon`** on `Δ_BCS(τ)`: pair-correlation length and Goldstone-phase-correlation length share the gap as parent. This means the pair count `n_pairs` and the mode count 8 are NOT dimensionally commensurate; the natural commensurate ratio is `n_k^GGE` (per-band per-mode), not `n_pairs/N_modes`.

R4's FAIL is therefore a **BCS-consistency failure, not a numerical boundary**. R4 mixes Fock-space integers (`n_pairs`) with single-particle mode-count (`N_modes = 8`) in a way that violates the per-mode Bogoliubov expectation-value structure. The 4 PASS readings respect the per-mode structure; the 1 FAIL reading does not.

### II.F. Corridor width: physics or methodology?

**Result**: The 5.551 OOM width is **structural** — floor K=1 from fermi-statistics (n_k ≥ 0) and ceiling K = 3.556 × 10⁵ from energy-conservation (equipartition across 8-mode fiber). Under B3-only restriction, the **residual width** is `log₁₀(S_IC^cap_R-SF-B3 / 1) = 5.551 OOM` (unchanged). Under R4-convention removal (so the naive 15.95 is excluded), the corridor is UNAFFECTED — R4 sat inside corridor, not defining it. The width is a **permanent feature of the 8-mode BCS quasiparticle spectrum**, not a weighting artifact.

**Why B3 restriction does not narrow it**. The W3-6 energy-conservation cap at B3 (`S_IC^cap_R-SF-B3 = 3.556e5`) is the **softest-band, most permissive** ceiling by construction — smaller bands would give proportionally lower caps. B2 (flat) gives `S_IC^cap_R-SF-B2 = 8.12e4` (log-width 4.91 OOM), B1 (acoustic) gives `S_IC^cap_R-SF-B1 = 1.35e5` (log-width 5.13 OOM). Restricting to any single band reduces but does not eliminate the multi-OOM corridor; the floor K=1 is band-independent (positivity).

**Why the multi-OOM corridor is structural, not methodological**:
1. **Floor K=1 is positivity**: `n_k ≥ 0` is the BCS Fock-space wall. No band-weighting scheme can move it.
2. **Ceiling S_IC^cap ~ 10⁵–10⁶ is equipartition**: the substrate's spectral-action budget `S_fold = 2.504 × 10⁵` in M_KK⁴ units divided across 8 modes at B3's soft gap gives ~10⁵. This is tied to the substrate's own spectral geometry (via `S_fold`), not to the weighting scheme.
3. **R4's K=15.95 is INSIDE the corridor**, not at its edge. R4 would FAIL the A_s gate regardless of corridor boundaries — it is excluded by the Planck factor-3 band at K ~ 3, well below the corridor ceiling.

The 5.55 OOM width is therefore an **unavoidable feature of the 8-mode BCS quasiparticle spectrum on the Jensen-deformed SU(3) fiber** — it reflects the dimensional gap between the quantum floor (positivity) and the thermodynamic ceiling (energy conservation), set by the substrate's own spectral-action geometry.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number | BCS-reading classification |
|:-----|:--------|:----------------|:--------------------------|
| W2-4 PS-SUBSTRATE-MATCHED-IC | **PASS** (factor-3) | K=2.035; A_s=6.72e−9; +0.505 OOM vs Planck | Near-isothermal regime; Leggett-populated, Bogoliubov-activated |
| W3-6 SIC-PHYSICAL-CAP | **PASS** | S_IC^cap = 3.556e5; ratio cap/obs = 2.174 | Long-relaxation ceiling; equipartition-bounded |
| W2-9 MULTIPAIR-ECOND | **FAIL** (structural) | E_cond(N=2)/E_cond(N=1) = 1.601 | Pauli blocking of B1 flat-band; Fock-saturation on Bogoliubov manifold |
| W3-11 XI-BCS-VS-L-PHONON | **PASS** | variation 7.78% (Scenario B conservative) | ξ_BCS ∥ ℓ_phonon on Δ_BCS(τ) — single parent scale |

All four gate verdicts inherited as authoritative from source docs; no re-adjudication.

---

## IV. Structural Implications

### IV.A. What the corridor says about the substrate

1. **Amplify only, never suppress** (W2-4 wall: K ≥ 1 from n_k ≥ 0). The substrate's own quasiparticle content can augment or match the Bunch-Davies scalar amplitude, but cannot reduce it. This is the first STRUCTURAL asymmetry of the phonon-first picture vs the QFT-in-curved-spacetime picture: BD vacuum is the **minimum** admissible state, not the canonical one. Any physical state is on or above the floor.

2. **Equipartition-capped at 5.55 OOM above the floor** (W3-6 wall: K ≤ 3.556e5 at R-SF-B3). The substrate has a finite spectral-action energy budget (`S_fold`), and distributing it isotropically across the 8-mode fiber at the softest band saturates at `n_k ~ 10⁵`. This ceiling is **substrate-native** — it does not require a cosmological reference. It is a statement about how much phononic occupation the fabric can carry given its own internal spectral action geometry.

3. **Physical readings cluster at the near-floor end** (five readings at K ∈ [1.92, 15.95]). The documented per-band per-mode Bogoliubov occupations all lie within the first ~1 OOM of the corridor (log K ∈ [0.28, 1.20]). The corridor's upper 4-OOM tail is empty of physically-admissible readings — it represents what the substrate **could** support under energy conservation, not what it **does** in the GGE-Wightman fixed point.

### IV.B. What the Leggett-vs-Bogoliubov diagnosis says about A_s's physical origin

The K=2.035 primary sits at T_eff/Δ = 0.93, where:
- **Leggett mode is populated** (K_Leggett-activation = 1.10 < 2.035): inter-band phase-coherence oscillations between B1, B2, B3 are thermally excited.
- **Bogoliubov pair-breaking is marginally activated** on the softest band (B3): `x_B3 = 0.9888`, so the exp(−x_B3) = 0.372 suppression is modest, not exponential.

This is the **A_s-physical-origin statement**: the factor-2-above-BD amplification at the CMB pivot is a **mixed phase-and-amplitude** response. It is not purely Bogoliubov (pair-breaking-continuum-generated) because B3 is only marginally activated; it is not purely Leggett (inter-band-phase-coherence-generated) because Bogoliubov activation contributes too. The A_s amplification IS THE SUBSTRATE'S MIXED-MODE GGE RESPONSE, with per-mode occupation n_k ~ 0.5 distributed between both manifolds.

**Consequence for S83 observational discrimination**. A pure Leggett-origin A_s and a pure Bogoliubov-origin A_s would have distinguishable k-dependence and non-Gaussianity signatures: Leggett modes give inter-band-correlated f_NL with phase structure, Bogoliubov pair-breaking gives adiabatic-continuum-like spectra. The W3-4 result `f_NL^GGE = 0.0547` (0.43σ vs Planck 2.5 ± 5.7) and `α_{f_NL} = 0` (machine-precision k-flat) are not yet sharp enough to separate the two — the pure-Bogoliubov and pure-Leggett both predict sub-unity f_NL in the GGE regime. But the near-isothermal regime at K=2.035 suggests the f_NL prediction has a DUAL origin, which could be tested with orthogonal-template f_NL and τ_NL trispectrum (already carry-forwards in S83).

### IV.C. Constraint map updates

**Opens**:
- Leggett-vs-Bogoliubov partition of S_IC across the corridor (carry-forward V.2): provides a discriminator between phase-coherence and pair-breaking physical origin for A_s.
- Inversion of K → T_eff/Δ provides a **new classification axis**: each reading convention R1–R5 maps to a specific regime label on the Bogoliubov/Leggett manifold; the five PASSes cluster at near-isothermal, the single FAIL (R4) at supra-isothermal (T ≈ 7Δ under R4=15.95, T/Δ = 7.97).

**Closes** (strengthens existing closures):
- R4's FAIL as BCS-consistency failure (II.E): R4 mixes Fock integers with mode counts, not a per-mode thermal occupation. This is stronger than the source doc's "legacy naive" characterization — it identifies a specific dimensional-analysis violation.
- W2-9's FAIL as Bogoliubov-manifold-exhaustion on B1 flat-band: extends the source doc's "Pauli blocking" statement into the quasiparticle manifold language. The 8-mode fiber's pair-breaking manifold saturates at N=1, forcing further excitation into the collective (Leggett) manifold.

**Preserves**:
- W2-4's structural bound K ≥ 1 (positivity wall, permanent).
- W3-6's energy-conservation ceiling (substrate-native, not cosmological).
- W3-11's `ξ_BCS ∥ ℓ_phonon` (single parent scale Δ_BCS(τ)).

---

## V. Carry-Forward Computations

**Structured 4-field carry-forwards (What / Inputs / Gate / Effort). Every entry is a concrete BCS/Leggett computation derived from Sections II–IV. All numerical anchors were pre-verified via Python against `canonical_constants.py` using the substitution-chain discipline.**

### V.1. K_matching under each of 5 reading conventions (R1–R5)

- **What**: For each reading R_i ∈ {R1 band-summed B3, R2 3/3/2-weighted geometric-mean, R3 3/3/2 primary, R4 naive `n_pairs/N_modes=59.8/8`, R5 energy-weighted B2}, derive the K that satisfies `A_s(K) = A_s_Planck` exactly under the linear response `A_s(K) = A_s_{W1-2} · K`. The five R_i differ only in how K is extracted from band data (convention layer), not in the K→A_s linear map (dynamics layer). Output variable: `{K_match_R_i, admissibility_R_i}` for i∈{1..5}. Python-pre-verified: `K_match = A_s_Planck / A_s_{W1-2} = 2.10e−9 / 3.299e−9 = 0.6366` (identical across all five R_i by construction of linear response). Per-convention K-values (already Python-verified) are R1=2.185, R2=2.049, R3=2.035, R4=15.95, R5=1.922.
- **Inputs**: `canonical_constants.py` (`A_s_Planck=2.10e−9`, `A_s_W1-2_TD=3.299e−9`, `Delta_BCS=0.4643·M_KK`, `M_KK=7.429e+16 GeV`); S43 band-multiplicity 3/3/2 (B1/B2/B3); W2-4 canonical K-values for R1–R5 from `sessions/archive/session-82/session-82-results-workingpaper.md` §V.D; structural wall K≥1 from W2-4 positivity.
- **Gate**: **GATE-KMATCH-CONVENTION-83**. PASS-EXCLUSION if all five K_match_R_i < 1 (structural floor wall excludes exact match under every convention; confirms the "amplify-only, never suppress" wall at the convention layer). PASS-INCLUSION if any K_match_R_i ≥ 1 (at least one convention admits exact match; identifies a preferred convention). INFO if convention-layer differs from dynamics-layer K_match (i.e., R_i conventions modify the linear response in a way that breaks convention-independence). Python-pre-verified expectation: all five K_match_R_i = 0.6366 < 1 ⇒ PASS-EXCLUSION. No convention admits exact Planck match; R4 is the ONLY reading failing the factor-3 band (R4 gives A_s/A_Planck = 25.1, +1.399 OOM; all other R_i give +0.48 to +0.54 OOM, all PASS factor-3 band).
- **Effort**: 1–2 hours, 1 agent session. Pure algebraic closure + Python verification; no new iteration needed.

### V.2. Leggett-vs-Bogoliubov partition of S_IC across the corridor K∈{1.1, 2.035, 10, 100, 1000, 3.56e5}

- **What**: Compute the per-manifold fractional contribution to S_IC^GGE(K) at each of six K-grid points, partitioning into (a) Leggett inter-band phase-coherence modes with activation gap Δ_Leggett ≈ 0.3061·M_KK (B1↔B2 interband splitting), and (b) Bogoliubov pair-breaking modes with gap Δ_BCS = 0.4643·M_KK. Partition formula: `frac_L(K) = n_L(T(K))/[n_L(T(K))+n_B(T(K))]` where `n_i = 1/(exp(Δ_i/T_eff(K))−1)` and `T_eff(K)/Δ_BCS = 1/ln[(K+1)/(K−1)]`. Output variable: `{frac_L(K), frac_B(K), K_crossover (if any)}`. Python-pre-verified: at K=2.035 primary, `frac_L=0.652`, `frac_B=0.348` ⇒ Leggett DOMINATES at framework's K=2.035 (65% of S_IC). Asymptotic: `frac_L → 0.603`, `frac_B → 0.397` at K→∞; `frac_L → 0.756`, `frac_B → 0.244` at K=1.1. **No crossover exists; Leggett dominates across entire corridor**.
- **Inputs**: `canonical_constants.py` (`Delta_BCS=0.4643·M_KK`); Δ_Leggett = 0.3061·M_KK from II.B (B1-B2 interband splitting, derived from S43 band data); inversion `T_eff/Δ = 1/ln[(K+1)/(K−1)]` from II.A; per-band gaps `2Δ_B1=0.929`, `2Δ_B2=1.541`, `2Δ_B3=0.352` in M_KK.
- **Gate**: **GATE-LB-PARTITION-83**. PASS-LEGGETT if `frac_L(K=2.035) > 0.55`: framework primary is Leggett-manifold-dominated (consistent with W2-9's Pauli-blocking-of-Bogoliubov at N=1; Leggett is the only open channel for further excitation). PASS-BOGOLIUBOV if `frac_B(K=2.035) > 0.55`: primary is pair-breaking-dominated. INFO if `frac_L ∈ [0.45, 0.55]` (balanced mixed manifold). FAIL if either fraction is negative (violates spectral-function positivity). Pre-verified result: `frac_L(K=2.035) = 0.652 > 0.55` ⇒ **PASS-LEGGETT**, confirming II.D's mixed-mode-with-Leggett-dominant diagnosis and II.B's "Leggett-populated" structural claim.
- **Effort**: 3–4 hours, 1 agent session. Python + plot across 6 grid points; confirm monotonicity of `frac_L(K)` and verify no crossover in corridor interior.

### V.3. τ_GGE full-formula at K = 2.035 (framework primary) vs single-scale estimate

- **What**: Evaluate τ_GGE(K=2.035) with the full per-band-weighted quenched BCS formula `τ_GGE^full = Σ w_i·τ_i / Σ w_i` where `τ_i = π/[4·Δ_i·tanh(x_i/2)]`, using S43 weights w = (3,3,2) for (B1,B2,B3), per-band gaps (Δ_B1, Δ_B2, Δ_B3) = (0.4645, 0.7705, 0.176)·M_KK from II.B, and per-band dimensionless `x_i = Δ_i/T_{eff,i}^{GGE}` from II.A per-band reproduction (x_B1=1.0674, x_B2=1.1533, x_B3=0.9888). Compare to the single-scale estimate `τ_GGE^simple = π·K/(4·Δ_BCS) = 3.442/M_KK`. Python-pre-verified: `τ_B1=3.463`, `τ_B2=1.959`, `τ_B3=9.750` (all in 1/M_KK units); weighted mean `τ_full = 4.471/M_KK`; ratio `τ_full/τ_simple = 1.299`.
- **Inputs**: `canonical_constants.py` (`Delta_BCS=0.4643·M_KK`, `dt_transit=1.130e−3/M_KK`, `tau_fold=0.190`, `hbar_GeV_s=6.582e−25`, `M_KK=7.429e+16 GeV`); per-band x values from II.A verified table; S43 3/3/2 band weights; Anderson-Morel quenched-BCS relaxation formula (cite Volovik paper 25 §V; S77 GGE-relaxation framework; S63 N_pair superselection permanence).
- **Gate**: **GATE-TAUGGE-FULL-83**. PASS if `τ_full / τ_simple ∈ [1/1.5, 1.5]`. INFO if ratio ∈ [1/3, 3] but outside 1.5 band. FAIL if ratio > 3 (per-band detail breaks single-scale approximation; substrate relaxation is not a single-Debye process). Pre-verified result: 1.299 ∈ [0.667, 1.500] ⇒ **PASS**. Derived quantity `τ_full/dt_transit = 4.471/1.130e−3 = 3956×` ⇒ slow compared to transit, fast compared to post-fold Hubble time (1/H_fold ~ 1/M_KK). Consistent with S77 `tau_relax/dt_transit=60.1` for a DIFFERENT (phase-scrambling, not GGE) relaxation process; S63 confirms GGE is globally permanent via N_pair superselection while local τ_GGE controls approach to the GGE fixed point. Cross-check: `τ_GGE(K=2.035) / 1/H_fold ≈ 3.442 / (1/0.190) ≈ 0.654` ⇒ τ_GGE is **sub-Hubble** at fold; GGE reaches fixed point within one e-fold of the fold ⇒ post-fold kinematic window for GGE relaxation is SATISFIED.
- **Effort**: 2–3 hours, 1 agent session. Python numerics + comparison to S63/S77 GGE relaxation memos; write §V.3 closure paragraph in §VI of next-session working paper.

### V.4. N_pair = 3 accessibility on 8-mode fiber (Pauli-wall extension beyond N=2)

- **What**: Test whether the Pauli wall established by W2-9 at N=2 (E_cond(N=2)/E_cond(N=1) = 1.601 < 3) extends to N=3 on the 8-mode B1/B2/B3 fiber. Compute `ratio(N=3) ≡ E_cond(N=3)/E_cond(N=1)` via two independent methods: (a) explicit 8-mode Richardson-ED at N_pair=3 (analogous to the W2-11 2-sector diagonalization in agent memory, but extended to 3 sectors with N_pair_cutoff=3), and (b) geometric-degradation model with per-pair Pauli-deficit factor r = `ratio(N=2) − 1` = 0.601 ⇒ `ratio(N=k)_model = Σ_{j=0}^{k−1} r^j = (1−r^k)/(1−r)`. Python-pre-verified geometric model: `ratio(N=3) = 1 + 0.601 + 0.361 = 1.962`; saturation `ratio(N→∞) = 1/(1−r) = 2.506` = asymptotic binding ceiling on 8-mode fiber. Compare ED result against geometric model as independent structural cross-check.
- **Inputs**: `canonical_constants.py` (`Delta_BCS`, `E_cond`, band structure); `researchers/Landau/` Richardson-Gaudin model references; W2-9 2-pair ED script in `computations/s82_*_multipair_ed.py` (extend to N_pair_cutoff=3); W2-11 S++-FULL-ED script `computations/s82_w2_11_s_pp_full_ed.py` as structural template (8-mode Hilbert-space construction); 3/3/2 band multiplicity.
- **Gate**: **GATE-NPAIR3-PAULI-83**. FAIL if `ratio(N=3) ≤ 2` (Pauli wall EXTENDS; N=3 is Pauli-suppressed; same structural pattern as N=2; W2-9 closure is not accidental but generalizes across Fock levels). PASS if `ratio(N=3) ≥ 3` (naive additive; N=3 is newly accessible; Pauli wall is N=2-specific). INFO if `ratio(N=3) ∈ (2, 3)` (partial Pauli suppression; no sharp wall transition). Pre-verified geometric-model expectation: `1.962 ≤ 2` ⇒ **FAIL pre-registered**, confirming the Pauli wall extends to N=3. Consequence: the 8-mode fiber's Bogoliubov pair-breaking channel has a structural binding ceiling ≈ 2.506·E_cond(N=1); further excitation must enter the LEGGETT collective manifold (consistent with V.2 `frac_L=0.652` dominance at K=2.035). Cross-check against asymptotic `ratio(N→∞) = 1/(1−r) = 2.506`: if ED disagrees with geometric model, geometric is a leading-order estimate and ED defines the true constraint.
- **Effort**: 6–8 hours, 1 agent session. Richardson-ED extension from 2-sector to 3-sector requires Hilbert-space bloat (dim from O(10²) to O(10³)); GPU eigvalsh on 8-mode RX 9070 XT via `torch.linalg` per project `.claude/rules/math-scripts.md`. Verification: Z_2 gauge degeneracy of W2-11 should generalize (check 3-sector partition has same unitary invariance).

### V.5. τ_GGE at K = 1.6 × 10⁵ (W1-E reconciliation point) vs detector observability windows

- **What**: Compute τ_GGE(K_W1E) in SI seconds for the W1-E Friedmann-BCS reconciliation point K = 1.6e5, then compare against LISA [10, 1e5] s, Pulsar Timing Array (PTA) [1e7, 1e9] s, and CMB [1.2e13 s] observability windows. Physical question: can the substrate's GGE relaxation at K=1.6e5 (a point in the corridor ~4.3 OOM above the primary K=2.035) be directly probed by any gravitational-wave or cosmological detector? Output variable: `{τ_GGE(K_W1E) in seconds, τ_GGE(K_W1E) / W_detector for each detector window}`. Python-pre-verified: τ_GGE(1.6e5) = 2.707e+05 / M_KK; converted via `1/M_KK = hbar_GeV_s/M_KK = 8.860e−42 s`: **τ_GGE(K=1.6e5) = 2.40e−36 s**. LISA floor (10 s) exceeds this by 37 OOM; PTA floor (1e7 s) exceeds by 43 OOM; CMB (1.2e13 s) exceeds by 49 OOM. All detector windows structurally inaccessible; substrate relaxation is sub-Planck-time (t_Planck = 5.39e−44 s; τ_GGE/t_Planck = 4.5e7 ⇒ 7.7 OOM above Planck time but still 36 OOM below any observable).
- **Inputs**: `canonical_constants.py` (`M_KK`, `Delta_BCS`, `hbar_GeV_s`, `dt_transit`, `t_Planck`); detector window bounds from `researchers/Mack/` LISA/PTA references (or pulsar-timing-array observation-window standard values: f_min=1e-9 Hz, f_max=1e-7 Hz; LISA f_min=1e-5 Hz, f_max=1e-1 Hz); S77 Parker-pair-production context (59.8 quasiparticle pairs from transit); W1-E coupled-dynamics K=1.6e5 value from W1-E source doc.
- **Gate**: **GATE-DETECTOR-WINDOW-83**. PASS-DETECTABLE if τ_GGE(K_W1E) lies in any detector window. PASS-STRUCTURAL-CLOSURE if τ_GGE(K_W1E) is below all detector windows by > 10 OOM (substrate relaxation is **not directly observable** at cosmological scales; the framework's signature must be imprinted via surviving GGE occupation — i.e., A_s, n_s — not via real-time dynamics). INFO if τ_GGE lies within 1–10 OOM of any window (marginal observability; worth deeper instrument-specific modeling). Pre-verified result: 2.40e−36 s < 10 s by **37 OOM** ⇒ **PASS-STRUCTURAL-CLOSURE**. Conclusion: the substrate's GGE relaxation is a **static-in-cosmological-time quasi-instantaneous equilibration**; only the relic occupation pattern (imprinted on A_s, n_s, f_NL) carries observational content. This REINFORCES the framework's commitment to spectroscopic-signature observables (CMB, LSS) and CLOSES the real-time-GW-observability channel for substrate quasiparticle dynamics.
- **Effort**: 1–2 hours, 1 agent session. Pure unit conversion + comparison; primary value is the structural closure statement (relaxation dynamics are static on cosmological timescales).

### V.6. K-response of the W3-11 co-scaling ratio ξ_BCS / ℓ_phonon across K-corridor

- **What**: Recompute the W3-11 co-scaling ratio `R_W3-11(τ, K) ≡ ξ_BCS(τ, K) / ℓ_phonon(τ, K)` across the joint (τ, K)-grid with τ ∈ {0.10, 0.15, 0.19, 0.22, 0.25} and K ∈ {1.0, 2.035, 10, 100, 3.556e5}. The W3-11 PASS (7.78% variation under Scenario B) was at canonical K=2.035; test whether the "single parent scale Δ_BCS(τ)" claim survives across the corridor. Output variable: `{R_W3-11(τ, K), max_τ-variation_at_fixed_K}` for each K. **Substitution chain**: (1) both ξ_BCS = v_F/(π·Δ_BCS) and ℓ_phonon = v_s/ω_peak scale with Δ_BCS(τ); (2) K enters only via per-mode occupation, not via the length scales themselves; (3) ratio should be K-independent at leading order. Prediction: R_W3-11(τ, K) ≈ R_W3-11(τ) for all K; if NOT, identifies a new dynamical regime where ξ and ℓ decouple at high-K.
- **Inputs**: `canonical_constants.py` (`Delta_BCS`, `v_F_substrate`, `v_s_substrate`, `tau_fold`); W3-11 source script `computations/s82_w3_11_xi_bcs_vs_l_phonon.py`; corridor K-values from II.D Python-verified table; S63 GGE superselection reference for N_pair-independence of length scales.
- **Gate**: **GATE-W3-11-KSWEEP-83**. PASS if `max_K max_τ |R(τ, K)/R(τ, K=2.035) − 1| < 10%` (K-independence survives; single parent scale confirmed across corridor). INFO if `∈ [10%, 30%]` at any (τ, K) (mild K-coupling; corridor interior has weak dynamical gradient). FAIL if `> 30%` at any (τ, K) (new dynamical regime at high K; ξ and ℓ decouple; substrate has TWO parent scales at high occupation, not one). Expected: K-independence at leading order (length scales share Δ_BCS parent); PASS is the structural prediction, FAIL would be the new-physics signal.
- **Effort**: 4–6 hours, 1 agent session. Extend existing W3-11 script over K-grid (5 × 5 = 25 evaluations); Python + GPU eigvalsh where needed; write §VI reconciliation paragraph.

### V.7. Convention-invariance proof for A_s(K) linear response

- **What**: Formal derivation that the map K → A_s(K) is **convention-invariant** across R1–R5 — i.e., once K is extracted from band data under any valid convention, the A_s response is the SAME linear function `A_s(K) = A_s_{W1-2}·K`. Decompose A_s into (convention layer: band weighting → K) × (dynamics layer: K → A_s); show the dynamics layer is structural (Mukhanov-Sasaki kernel + BCS squeezing factor), the convention layer is representational. The 5 readings explore the convention layer; the linear response is the dynamics layer.
- **Inputs**: W1-2 TD-branch Mukhanov-Sasaki derivation from `sessions/archive/session-82/session-82-results-workingpaper.md`; S43 band-multiplicity spec; W2-4 S_IC^GGE canonical form `1+2n_k`; convention definitions for R1–R5.
- **Gate**: **GATE-KA-CONV-INV-83**. PASS if the decomposition {convention layer, dynamics layer} is rigorously separable AND the dynamics layer is proven linear in K. INFO if linearity holds only to leading order (nonlinear corrections at K→∞ from W3-6 equipartition ceiling). FAIL if the decomposition cannot be made (the two layers mix nonlinearly). Expected: PASS at leading order; INFO from the equipartition ceiling softening the linear response near K=3.556e5. This carry-forward formalizes the implicit structure underlying V.1 and makes the "convention-independent K_match" statement a theorem rather than a Python-verification.
- **Effort**: 2–3 hours, 1 agent session. Primarily a derivation + structural write-up; no heavy numerics.

---

## VI. Summary Table

| # | BCS-Reading Claim | Classification | Status | Structural Consequence |
|:--|:------------------|:---------------|:-------|:-----------------------|
| 1 | K = coth(Δ/(2T_eff)) map invertible on K ∈ (1, ∞) | PHONONIC | machine-precision verified | Defines corridor-positioning coordinate T_eff/Δ |
| 2 | K = 2.035 ⇒ T_eff/Δ = 0.9295 (near-isothermal) | PHONONIC | Python-verified | Substrate GGE sits at its own BCS activation threshold |
| 3 | Leggett activation at K_L ≈ 1.10 < K_canonical = 2.035 | PHONONIC | derived and verified | Leggett mode IS populated at framework's K=2.035 point |
| 4 | Bogoliubov pair-breaking on B3: x_B3 = 0.989 (marginal activation) | PHONONIC | W2-4 CC2 | Pair-breaking NOT Boltzmann-suppressed at K=2.035 |
| 5 | A_s(K) = A_s_W1-2 · K (linear response, zero free parameters) | PHONONIC | Python-verified 10 pts | K is the ONLY dial; no tunable amplitude |
| 6 | K_matching_nominal = 0.637 < 1 (UNREACHABLE) | PHONONIC | Python-verified | Exact Planck match structurally excluded under any convention |
| 7 | K = 1 structural floor gives +0.196 OOM (PASS-F2) | PHONONIC | W1-2 inherited | Minimum admissible A_s still clears factor-2 band |
| 8 | K = 2.035 gives +0.505 OOM vs Planck (PASS-F3) | PHONONIC | W2-4 inherited | Factor-3 band clearance at tight 0.168 OOM margin |
| 9 | τ_GGE(K) = π·K/(4Δ) monotone increasing | PHONONIC | substitution chain + Python | Corridor ceiling = LONG relaxation; floor = SHORT relaxation |
| 10 | 5 readings cluster at τ_GGE/dt_transit ~ 3×10³ (short-end) | PHONONIC | Python table II.C | Long-relaxation tail of corridor is empty of physical readings |
| 11 | R4's FAIL is BCS-dimensional inconsistency | PHONONIC | II.E diagnosis | Excludes Fock-count/mode-count mixing conventions permanently |
| 12 | Corridor 5.55 OOM width is structural (floor+ceiling both physical) | PHONONIC | W2-4 + W3-6 walls | Width cannot be reduced by weighting scheme changes |
| 13 | W2-9 Pauli saturation = Bogoliubov-manifold-exhaustion | PHONONIC | structural | Further excitation forced into Leggett collective manifold |
| 14 | W3-11 ξ_BCS ∥ ℓ_phonon on Δ_BCS(τ) (single parent scale) | PHONONIC | 7.78% variation | A_s, pair-correlation length, Goldstone-cutoff all share gap |
| 15 | K_FIRAS ≈ 3.68 × 10⁵ ≈ S_IC^cap (within factor 1.03) | PHONONIC | µ ~ K scaling | FIRAS and energy-conservation ceilings approximately coincide |

---

*End of session-82 landau-synthesis. BCS-coherence mapping places the framework's K=2.035 primary at T_eff/Δ = 0.93 (near-isothermal, mixed Leggett/Bogoliubov manifold), τ_GGE ≈ 3046× dt_transit (short-relaxation end), A_s = 6.72e−9 (PASS at factor-3). Corridor width 5.55 OOM is structural: floor from positivity (K ≥ 1), ceiling from equipartition (S_IC^cap = 3.556 × 10⁵). Three S83 carry-forwards registered: K_matching per convention (structural exclusion test), Leggett/Bogoliubov partition of S_IC (discriminator), full-formula τ_GGE at K=2.035 (dynamical timescale).*
