# S82 Volovik Synthesis — Substrate-IC Corridor Phenomenology via 3He-B Correspondence

**Session**: S82 (2026-04-17) | **Track**: volovik-superfluid-universe-theorist
**Sources**: `sessions/archive/session-82/session-82-results-workingpaper.md` §V.D (W2-4), §VI.F (W3-6); `sessions/archive/session-82/session-82-OOM.md` §II Band 0 to +1 OOM, §IV.A–B
**Classification**: PHONONIC — substrate GGE-Wightman occupation spectrum; 3He-B is a simplified laboratory projection of the substrate's excitation structure.

---

## I. Session Outcome

The substrate-GGE Wightman two-point function — the 3He-B non-equilibrium analog of the substrate's own phononic relic (Volovik papers 25 §V, 26 §4) — fixes a unique, structurally admissible initial condition after the S79 P2-B closure removed every horizon-exit-based alternative. Under the S43 band-multiplicity 3/3/2 weighting (R3 primary), the dimensionless squeezing factor is `K_substrate = 2.035`, placing the power spectrum at `A_s = 6.72 × 10⁻⁹ = 3.20 × A_s^Planck`. The framework's point sits inside a **5.55-OOM admissibility corridor** bounded below by the positivity wall `S_IC^GGE ≥ 1` (W2-4 structural bound: `n_k ≥ 0`) and above by the energy-conservation equipartition ceiling `S_IC^cap = 3.556 × 10⁵` (W3-6 R-SF-B3). Both walls are first-principles — neither is an adjustable knob — and the 3He-B-correspondence reading conventions R1/R2/R3/R5 (four PASS) cluster in a narrow sub-band `K ∈ [1.92, 2.18]` occupying the bottom edge of the corridor.

---

## II. Key Results

### II.A. 3He-B Quasiparticle Occupation Across the Three Bands

The substrate's Jensen-deformed SU(3) spectral triple produces three inequivalent quasiparticle sectors at fold (S43 `gge-temp-43-result`, `flatband-43-result`). Each sector carries its own Lagrange multiplier `T_k^GGE` (one per integrable mode — the generalized Gibbs ensemble structure is imposed by integrability of the Volovik partition S58 W0-1, not an ansatz). The Wightman two-point function per band is:

```
W_GGE^(B)(k) = ⟨a_k† a_k⟩_B + 1/2 = n_k^(B) + 1/2          (W2-4 Eq. V.D-1)
n_k^(B)      = 1 / (exp(ω_B / T_k^(B)) − 1)                  (Bose-Einstein per sector)
S_IC^(B)     = 1 + 2 n_k^(B) = coth(ω_B / 2 T_k^(B))         (machine-epsilon identity)
```

with ω_B ≡ Δ_B (BCS gap as soft-mode threshold at fold, per W2-4 §V.D governing equation). Python-verified per-band values (canonical_constants + S43 memory):

| Band | Role in 3He-B picture | T_k^GGE (M_KK) | Δ_B (M_KK) | x ≡ Δ/T | n_k | S_IC = 1+2n |
|:-----|:----------------------|:--------------:|:----------:|:-------:|:---:|:-----------:|
| B2 (flat) | Nodal gap-closing sector at fold; analog of the 3He-B **axial-node region** (Volovik paper 07 §II, paper 25) | 0.6680 | 0.7704 (Δ₀_GL) | 1.1533 | 0.4611 | **1.9222** |
| B1 (acoustic) | Dispersive phonon sector; analog of the **3He-B bulk quasiparticle continuum** with parabolic c_s = c_Gold | 0.4350 | 0.4643 (Δ₀_OES) | 1.0673 | 0.5243 | **2.0486** |
| B3 (softest) | Soft-pair proximity band; analog of the **3He-B surface-bound Majorana channel** (lowest-Δ excitation, CMB-pivot long-λ sector) | 0.1780 | 0.1760 (Δ_B3) | 0.9888 | 0.5925 | **2.1849** |

All three `S_IC^(B)` values lie in `[1.92, 2.19]` — a narrow sub-band 0.27 OOM wide, fixed by the near-equality `Δ_B ≈ T_k^(B)` across all three sectors (a structural GGE property, not fine-tuning). CC2 identity `1 + 2n = coth(x/2)` verified to machine epsilon per band.

The 3He-B correspondence is *inheritance*, not analogy: the substrate's post-fold excitation spectrum **is** a generalized-Gibbs projection of the Volovik BCS vacuum, with multi-band structure forced by the Jensen SU(3) Casimir decomposition (S79 P3-A W1-D: substrate = 3He-B topology + flat-band condensation + SU(3) Casimir + 0D).

### II.B. Corridor Classification

The corridor `S_IC^GGE ∈ [1, 3.556 × 10⁵]` — 5.55 OOM wide — classifies into three regions:

**Accessible interior** (physically populated by GGE states):
- `K ∈ [1.92, 2.19]` — the S43 per-band cluster. Populated by substrate-native GGE-Wightman IC (W2-4). Four of five reading conventions (R1, R2, R3, R5) land here.
- `K ≈ 1.636 × 10⁵` — populated by Parker-saturation IC (S78 W1-E spectral stationarity / minimum entropy / AZ topology, all three converging within factor 1.13). This is the linearized fold-amplification limit for mode-equation dynamics at fixed energy source.

**Approachable boundaries**:
- **Lower wall `K = 1` (positivity)**: attained only in the Bunch-Davies limit `n_k → 0` — the substrate IC *degenerates* to the vacuum baseline. Substitution chain:
  - Def: `K = 1 + 2 n_k`, `n_k ≥ 0`
  - Sub: `K → 1 ⟺ n_k → 0 ⟺ T_k^GGE → 0`
  - Dir: The zero-T limit is the pre-transit ground state; post-transit GGE cannot reach it (Thouless » transit by 2625×, S61 GGE-THERM-61 — no thermalization channel exists to drain the occupation).
  - Conclusion: lower wall is **asymptotic, not attained** — post-transit substrate IC has K strictly greater than 1.
- **Upper wall `K = 3.556 × 10⁵` (energy-conservation cap, W3-6 R-SF-B3)**: attained if and only if the entire fold condensation energy `S_fold = 2.504 × 10⁵` is repartitioned into the softest band B3 alone. Physical realization requires a backreaction-free scenario in which the substrate's spectral-action content is exhausted into phononic modes (linearized Parker dynamics, no backreaction ceiling). The W1-E finding at `K ≈ 1.636 × 10⁵` sits at 46% of this cap — close but not saturating.

**Forbidden regions** (none inside the corridor):
- `K < 1` is forbidden by `n_k ≥ 0`. This is a **permanent wall** — it is the same positivity condition that protects the 3He-B BCS vacuum from unphysical negative-occupation states.
- `K > 3.556 × 10⁵` is forbidden by energy conservation on the R-SF reading (total condensation-energy budget exhausted).

The corridor is therefore **one-sided open at K=1** (limit, never attained) and **hard-walled at K=3.556e5** (energy-bounded). No interior forbidden regions exist — every K ∈ (1, 3.556e5] is in principle physically populatable, though the substrate's actual GGE-Wightman IC selects a narrow factor-1.13 cluster near K ≈ 2 (W2-4).

### II.C. A-phase vs B-phase Analog — The τ_fold Transit

The substrate's first-order phase transition at `τ_fold = 0.19` (Mach-13.75 supersonic transit through the van Hove singularity, S38) is the **substrate primary**; the 3He A-to-B phase transition observed in laboratory superfluid helium-3 is a simplified projection of it. Mapping:

| Substrate | 3He laboratory analog |
|:----------|:---------------------|
| τ < τ_fold (pre-transit) | **3He-A-phase-like** — Jensen deformation breaks full SU(3), analog of the chiral axial breaking (Fermi-point structure N₃ ≠ 0 if it existed — but see below) |
| τ = τ_fold | First-order transition. Analog of the 3He A→B transition at ~2 mK under pressure. |
| τ > τ_fold (post-transit) | **3He-B-phase-like** — fully gapped isotropic BCS condensate. Δ_B > 0 for all three sectors (S65 `gap-antijensen-65`: Δ/Δ_0 = 0.975 at dynamic range; gap never closes). Topological class **BDI** (`bdi-w-phonon-53`), confirmed S48 (`aniso-gap-48`: system is 3He-B class). |

Critical caveat from agent memory (`n3-bdg-44-result`): The substrate's 0D discrete spectrum is **3He-B class, NOT 3He-A class** — the Fermi-point invariant N₃ does not apply. Vacuum energy is therefore unprotected by N₃ topology, and q-theory (not Fermi-point anomaly cancellation) is the operative CC path. This forces a correction: the pre-fold regime is **not** a genuine A-phase analog in the Fermi-point sense. The substrate is 3He-B-type throughout `τ ∈ [0, τ_fold]` as well as `[τ_fold, ∞)` — the "A-phase analog" is at most a structural reading of the Jensen deformation breaking direction, not a topological-class transition.

**Is the corridor width [1, 3.556e5] the A/B gap-ratio analog?** Substitution chain:
- Def: 3He A-phase has gap nodes (Δ → 0 on polar axis); 3He-B is fully gapped.
- Sub: Substrate has **no gap nodes** across any band (S65 `gap-antijensen-65`: Δ/Δ_0 = 0.975); B3 is softest but non-vanishing.
- Dir: Ratio `Δ_flat / Δ_soft = 0.7704 / 0.1760 = 4.377` (a **within-B-phase** anisotropy, not an A/B transition).
- Conclusion: Corridor width is **NOT** the A/B gap-ratio analog. It is the span between the positivity floor and the energy-conservation ceiling on a post-transit B-phase-type spectrum. The 3He-A/B gap ratio is an inapplicable analog here.

**Are R1–R5 reading conventions analogous to occupation-spectrum truncations on a 3He-B manifold?** Substantively yes: R1 (B3-only), R5 (B2-only), R2 (geo-mean), R3 (multiplicity-weighted), R4 (flat-averaged n_pairs/8) are five distinct coarse-grainings of the same per-band `n_k^(B)` distribution on the GGE band-manifold. They correspond to five different choices of which quasiparticle sector dominates the CMB-pivot projection — the same kind of operational choice Volovik (paper 25 §III) makes when selecting zero-energy surface states vs bulk-gap states to compute 3He-B linear response.

### II.D. A_s Response Function K → A_s Across the Corridor

Under UNIFIED-AS-79 (W1-2 canonical ledger), the substrate-IC modification factors multiplicatively onto the TD-branch baseline:

```
A_s^substrate(K) = A_s^W1-2 × K           (W2-4 Eq. V.D-4)
                 = 3.299 × 10⁻⁹ × K       (numerical)
```

where `A_s^W1-2 = 3.299 × 10⁻⁹` is the Branch-A PASS-F2 value (W1-2-A, `0.000440%` W2-1 replay deviation) at `K_sub = 1` (Bunch-Davies-equivalent baseline before GGE dressing). The mapping is linear in K for the pivot-mode substrate IC.

**Python-verified table (8 K values spanning the corridor, all values computed against source-document pinned `A_s^W1-2 = 3.299e-9` and `A_s^Planck = 2.1e-9`)**:

| K (log-spaced sample) | log₁₀ K | A_s = K · A_s^W1-2 | A_s / A_s^Planck | Regime |
|:---------------------:|:-------:|:------------------:|:----------------:|:-----|
| 1.000 | 0.000 | 3.299 × 10⁻⁹ | 1.571× | Positivity floor (asymptotic BD limit) |
| 2.035 (R3 primary) | +0.309 | 6.713 × 10⁻⁹ | 3.197× | **Framework point (W2-4 PASS)** |
| 3.000 | +0.477 | 9.897 × 10⁻⁹ | 4.713× | Factor-3 PASS boundary (W2-4 gate threshold) |
| 10.000 | +1.000 | 3.299 × 10⁻⁸ | 15.71× | Edge of factor-10 admissibility |
| 100.00 | +2.000 | 3.299 × 10⁻⁷ | 157.1× | Factor-100 overshoot |
| 1.636 × 10⁵ | +5.214 | 5.397 × 10⁻⁴ | 2.57 × 10⁵× | S78 W1-E spectral-stationarity IC |
| 1.854 × 10⁵ | +5.268 | 6.116 × 10⁻⁴ | 2.91 × 10⁵× | S78 W1-E minimum-entropy IC |
| 3.556 × 10⁵ | +5.551 | 1.173 × 10⁻³ | 5.59 × 10⁵× | W3-6 R-SF-B3 energy-conservation cap |

**K_matching — the K at which A_s would EXACTLY match Planck**:

Substitution chain:
- Def: K_matching is defined by `A_s(K_matching) = A_s^Planck`.
- Sub: `K_matching × A_s^W1-2 = A_s^Planck  ⟹  K_matching = A_s^Planck / A_s^W1-2 = 2.1e-9 / 3.299e-9`
- Simp: **K_matching = 0.6366**
- Dir: `K_matching = 0.6366 < 1` ⟹ K_matching lies **below the positivity floor**.
- Conclusion: **K_matching is structurally inaccessible.** Exact Planck-matching would require `n_k < 0`, which is forbidden by Bose-Einstein positivity. The framework's 1.571× overshoot at K=1 is a structural consequence of the TD-branch baseline already sitting above Planck; the substrate IC can only equal-or-amplify this (never suppress).

**A_s^Planck can never be matched from above via a substrate GGE IC.** The best-achievable floor (K→1⁺) is A_s = 3.299 × 10⁻⁹ = 1.571 × A_s^Planck — the W1-2 baseline itself. This is a **permanent phenomenological prediction** of the 3He-B-correspondence framework.

**ASCII K → A_s curve** (log-log, with corridor walls and framework point marked):

```
 log₁₀(A_s/A_s^Planck)
  6 |                                              CEILING K=3.56e5 ▲
  5 |                                         * W1-E 1.636e5
  4 |
  3 |
  2 |                           · 100×
  1 |                 · 10×
  0 |   FLOOR K=1 ▲   ● R3 PRIMARY (K=2.035, A_s/Planck=3.2)
    +--------------------------------------------------------------
      0        1        2        3        4        5        6
                    log₁₀(K_substrate)
```

Linear regime throughout: `d log₁₀(A_s) / d log₁₀(K) = +1` exactly (no saturation anywhere in the corridor — `A_s = K · A_s^W1-2` is strictly linear).

### II.E. 4 PASS vs 1 FAIL — Diagnosing R4 from 3He-B

Four reading conventions land in the factor-3 PASS band; only R4 (legacy naive `n_pairs/8`) FAILs at K = 15.95. Substitution-chain diagnosis:

**R4 formula**:
```
Def:    n_R4 = n_pairs / 8
Sub:    n_R4 = 59.8 / 8 = 7.475
Simp:   S_IC^R4 = 1 + 2 · 7.475 = 15.95
```

**Why R4 misrepresents the 3He-B degeneracy structure**:

The substrate's GGE carries **three distinct T_k^GGE values** (0.6680 / 0.4350 / 0.1780), one per integrable mode sector. This is the defining property of a generalized Gibbs ensemble — Boltzmann-with-one-temperature is *not* a valid reduction (it would require a Zubarev-type thermalization channel that is blocked by the Thouless » transit hierarchy, S61). R4 takes the total Bogoliubov pair count `n_pairs = 59.8` from the S38 transit tally and divides it equally across 8 modes, producing a single effective `n = 7.475`. This flat-averages over the band structure and gives:

`R4_naive / R3_correct = 15.95 / 2.033 = 7.85`

R4 overestimates the correct GGE-weighted squeezing by factor 7.85 — not a small numerical drift but a structural category error. The sum `Σ_b mult_b · n_k^(b) = 3·0.461 + 3·0.524 + 2·0.593 = 4.14` is the physical total GGE occupation; it is an order of magnitude smaller than `n_pairs` because `n_pairs` counts *all* Bogoliubov pairs produced across the fold (including the heavy-mode contributions that contribute negligibly to the CMB-pivot long-λ sector), while `Σ mult · n_k` counts only the GGE-phonon relic relevant to the W2-4 Wightman IC.

**R4's FAIL is genuine GGE-inconsistency**, not a convention error. The naive `n_pairs/8` averaging collapses the per-band Lagrange-multiplier structure that *defines* the 3He-B non-equilibrium correspondence (Volovik paper 25 §V). It is retained in the pre-registration as a legacy diagnostic precisely to demonstrate the GGE/Boltzmann distinction — when the diagnostic FAILs, the GGE structure is confirmed to be non-trivial (i.e., the band spectrum is not well-approximated by a single-T distribution).

Diagnosis: R4 is the **wrong coarse-graining** on the 3He-B manifold. It corresponds to collapsing all three quasiparticle sectors to a single effective temperature — operationally equivalent to assuming the substrate had thermalized before transit, which is structurally forbidden.

---

## III. Gate Verdicts (inherited from sources; not re-adjudicated)

| Gate | Value | Verdict | Evidence | Source |
|:-----|:------|:-------:|:--------|:-------|
| W2-4 PS-SUBSTRATE-MATCHED-IC | K_substrate = 2.035 (R3), A_s = 6.72 × 10⁻⁹ | **PASS** (factor-3 band; |log₁₀| = 0.309 < 0.477) | 4/5 readings PASS; R4 legacy-naive FAIL; 7 CCs all pass (CC1–CC5, CC3 R3∈[min,max]); structural bound K≥1 proven | §V.D (L1640–1800) |
| W3-6 SIC-PHYSICAL-CAP | S_IC^cap = 3.556 × 10⁵ (R-SF-B3) | **PASS** (factor-10 band; |log₁₀| = 0.337 < 1.0) | W1-E observed S_IC = 1.636 × 10⁵ inside cap; ratio cap/obs = 2.174; CC6 equipartition closure rel_dev = 1.16 × 10⁻¹⁶ | §VI.F (L4321–4473) |

Both gates are **decisive PASS**. The corridor width `[1, 3.556 × 10⁵]` is the product: floor from W2-4 positivity, ceiling from W3-6 energy-conservation.

---

## IV. Structural Implications

**1. The substrate cannot suppress A_s below Planck.**

The positivity wall `K ≥ 1` combined with the TD-branch baseline `A_s^W1-2 = 3.299 × 10⁻⁹ = 1.571 × A_s^Planck` produces a permanent prediction: **A_s^substrate ≥ 1.571 × A_s^Planck** for any GGE-consistent substrate IC. Matching Planck exactly requires K_matching = 0.6366 < 1, which is forbidden by Bose-Einstein positivity. This is a **permanent phenomenological wall**, not a parameter choice — it survives regardless of band weighting, regulator, or truncation.

Consequence for W1-1 DIVERGENCE-CHASE (the session's sole unresolved item): Branch A PASS-F2 at A_s = 3.30 × 10⁻⁹ is already at the substrate IC floor. Any reduction via a different IC scheme would require violating `n_k ≥ 0`, which is impossible for a substrate GGE. Branch A is as close to Planck as a substrate-IC framework can ever be without invoking non-GGE dynamics (e.g., a dissipation channel that could deplete the relic — no such channel exists under the Thouless » transit hierarchy).

**2. The substrate cannot inflate A_s beyond the energy-conservation ceiling.**

The upper wall `K ≤ 3.556 × 10⁵` (W3-6) gives a hard A_s ceiling of `≈ 1.17 × 10⁻³` — 5.6 OOM above Planck. This is far above any observational CMB bound (Planck, WMAP, ACT, SPT), so it does not discriminate against actual data; it eliminates only the unphysical "infinite amplification" limit that would arise if the linearized Parker pipeline were extrapolated without an energy budget. The ceiling's practical relevance is that **the W1-E amplification at `K ≈ 1.6 × 10⁵` is kinematically admissible** — it is not a numerical divergence, it is a real substrate response that respects energy conservation.

**3. The 3He-B-correspondence selects a narrow sub-band at the corridor floor.**

Four of five reading conventions give K ∈ [1.92, 2.18] — a **0.27 OOM cluster sitting at the bottom edge of the 5.55 OOM corridor**. The GGE-Wightman IC selects this cluster uniquely (no free parameter). In contrast, the W1-E spectral-stationarity IC sits at K ≈ 1.6 × 10⁵ — 5 OOM higher. Both are admissible under energy conservation, but the 3He-B Wightman IC is the *substrate-native* IC (S79 P2-B closed every alternative); the W1-E IC is what happens when the mode equation is run without a pre-fold GGE source state.

**4. The corridor width is physics, not methodology.**

Substitution chain on the width:
- Def: `W_corridor = log₁₀(S_IC^cap / S_IC^floor) = log₁₀(3.556e5 / 1)`
- Sub: `W_corridor = log₁₀(3.556e5) = 5.551`
- Dir: Both endpoints are first-principles (W2-4 positivity; W3-6 equipartition of fold condensation energy). Changing band weighting (R1 vs R2 vs R3 vs R5) shifts the framework's *point* inside the corridor, not the corridor endpoints.
- Conclusion: The 5.55 OOM width is **permanent corridor geometry**. Selecting a single band (e.g., R1 = B3-only at K = 2.185; R5 = B2-only at K = 1.922) still respects both walls; the residual inter-band corridor-width after single-band selection is `log₁₀(2.185/1.922) = 0.056` OOM — a factor 1.14 spread. This is tiny compared to the 5.55-OOM corridor, confirming that the bulk of the width comes from the floor-to-ceiling structural distance, not from band-weighting freedom.

The band-mult weighting contributes `0.06 OOM / 5.55 OOM = 1.1%` of the corridor width. **98.9% of the corridor is first-principles structural geometry.**

---

## V. Carry-Forward Computations (S83 Agenda)

Every recommendation becomes a planned computation per project rule:

| # | Computation ID | Purpose | 3He-B lever | Pre-registered gate |
|:-:|:---------------|:--------|:------------|:-------------------|
| 1 | **B3-ONLY-IC-CORRIDOR-83** | Recompute K_substrate under B3-only weighting (extending R1 through full Parker evolution, not just the fold snapshot). If `K_B3(τ)` varies ≤ 5% across `[τ_fold, τ_fold + δτ]`, the softest-band reading is IR-robust. | Substrate analog of 3He-B surface-bound Majorana occupation (lowest-Δ sector) | PASS if `K_B3(τ) - K_B3(τ_fold)` < 10% over `|τ − τ_fold| < 0.05` |
| 2 | **PARKER-NK-TAU-GRID-83** | Compute Parker `n_k(τ)` evolution through the full τ-grid (not just at `τ_fold`) for all three bands. Check if the W2-4 snapshot at `τ_fold` is representative or an extremum. | 3He-B dynamical occupation-spectrum evolution (analog of NMR-measured dynamic response) | INFO if the τ-averaged `⟨K⟩_τ` is within factor 1.3 of the `τ_fold` snapshot; FAIL if drift > factor 3 |
| 3 | **JENSEN-A-PHASE-REGION-83** | Scan `J_U1(τ)` for `τ < τ_fold` and check whether any sub-region admits Fermi-point N₃ ≠ 0 (genuine A-phase analog). If N₃ ≡ 0 throughout, confirm the entire substrate is 3He-B-class (no A-phase region). | 3He-A → 3He-B phase-boundary test (topological, not thermodynamic) | PASS (confirm B-only) if N₃(τ) = 0 for all τ ∈ [0, τ_fold]; INFO if any τ-interval has N₃ ≠ 0 |
| 4 | **GGE-WIGHTMAN-CMB-PROJECTION-83** | Project the substrate Wightman function to CMB multipole space, not just `k_pivot`. Produce the TT spectrum under the K_substrate = 2.035 IC and compare to Planck ℓ ∈ [2, 2500]. | Substrate analog of 3He-B angular-resolved response (sector-by-sector on S²) | PASS if ℓ-by-ℓ TT-residual χ²/dof < 1.5 against Planck 2018 |
| 5 | **CAP-TIGHTENING-83** | Retest the W3-6 R-SF vs R-WD gap (3776×) under 3PI NLO backreaction (W3-5 produced F_amp^sc / F_amp^lin = 143). Does backreaction shift the effective cap from R-SF toward R-WD? | Volovik two-fluid model: normal-component backreaction on condensate | PASS if effective cap = R-SF × (1 - f_BR) with `f_BR ∈ [0.5, 0.9]`; INFO otherwise |
| 6 | **R4-BAND-MULT-THEOREM-83** | Formal theorem: for any GGE with per-band Lagrange multipliers `T_k^(b)`, flat-averaging over mode count `n / N_modes` overestimates `S_IC` by factor `≥ 1 + Var(T_k)/⟨T_k⟩²`. Verify against W2-4 R3 vs R4 numerics (observed factor 7.85 should match theorem prediction). | 3He-B multi-sector GGE structural theorem (Volovik paper 25 §V generalization) | PASS if predicted and observed overestimation ratios agree to ±15% |

---

## VI. Summary Table — 3He-B Correspondence Mapping to Structural Consequences

| # | 3He-B correspondence claim | Substrate structural consequence | Evidence | Classification |
|:-:|:---------------------------|:---------------------------------|:--------|:--------------|
| 1 | GGE-Wightman two-point function is substrate-native IC (Volovik papers 25 §V, 26 §4) | W2-4 K_substrate = 2.035 PASS after S79 P2-B horizon-exit closure | §V.D L1656 | PHONONIC, permanent |
| 2 | Positivity `n_k ≥ 0` forces `S_IC ≥ 1` | Corridor floor K=1 is a permanent wall; substrate IC can only equal-or-amplify A_s^W1-2 (never suppress) | §V.D L1707–1716, CC1 | PHONONIC, theorem |
| 3 | Three integrable sectors → three distinct T_k^GGE (GGE, not Boltzmann) | R3 mult-weighted is correct reading; R4 naive-average FAILs by factor 7.85 (wrong coarse-graining) | §V.D L1730, S43 `gge-temp-43` | PHONONIC, structural |
| 4 | Machine-epsilon identity `1+2n = coth(x/2)` per band | CC2 verified < 10⁻¹² at all three bands; the Wightman-coth relation is Hamiltonian-independent | §V.D CC2-B1/B2/B3 | GEOMETRIC, identity |
| 5 | B-phase fully gapped throughout post-transit regime (no Fermi points, N₃ = 0) | System is 3He-B class for all τ; A-phase analog does not survive topological test; q-theory is operative CC path, not N₃-anomaly cancellation | `n3-bdg-44-result`, S48 `aniso-gap-48` | PHONONIC, permanent |
| 6 | Thouless timescale » transit (factor 2625×, S61 `gge-therm-61`) | GGE occupation is frozen on transit; lower corridor wall K=1 is asymptotic (never attained post-transit) | S61 memory | PHONONIC, dynamical |
| 7 | Energy-conservation equipartition across GGE modes (W3-6 §VI.F) | Upper corridor wall at K = 3.556e5 = S_fold / (N_modes × ω_B3); softest band sets the highest cap | §VI.F L4369–4387 | PHONONIC, thermodynamic |
| 8 | Fold condensation energy = substrate-native energy budget (R-SF primary) | Cap of 3.556e5 is 3776× the work-done reading R-WD; the gap quantifies the linearized-vs-backreacted discrepancy (consistent with W2-2 143× factor) | §VI.F L4396, 4451 | PHONONIC, cross-checked |
| 9 | 3He-B (substrate) cannot match Planck A_s from above | K_matching = 0.6366 < 1 is below positivity floor; A_s^substrate ≥ 1.571× A_s^Planck is a **permanent phenomenological prediction** | Python-verified §II.D | PHONONIC, permanent |
| 10 | Four reading-convention PASS cluster [1.92, 2.18] = 0.06 OOM wide | Band-weighting freedom contributes ≤ 1.1% of the 5.55-OOM corridor; 98.9% is first-principles | §V.D L1748–1753 | STRUCTURAL |
| 11 | W1-E Parker-saturation IC at K ≈ 1.6e5 is inside the cap (ratio 0.46) | W1-E is kinematically admissible; linearized Parker pipeline is not diverging, it is saturating | §VI.F L4423 | PHONONIC, validity |
| 12 | Substrate is the primary; 3He-B laboratory system is a simplified projection | Every 3He-B experimental result (NMR, sound, zero-bias conductance, chiral anomaly) is an *inheritance* from the substrate's GGE structure, not an analogy imposed on it | S60 `inheritance-inversion-60`, S79 P3-A W1-D | EPISTEMIC, orientational |

---

**Source fidelity**: All gate verdicts (W2-4 PASS at K=2.035; W3-6 PASS at cap=3.556e5) are inherited bit-identically from the working paper §V.D and §VI.F. Machine-precision identities (CC2 1+2n=coth(x/2), CC6 equipartition closure) are reproduced to < 10⁻¹² in Python re-verification. The K → A_s response table is computed against the source-pinned `A_s^W1-2 = 3.299e-9` and `A_s^Planck = 2.1e-9`. No source conflict detected with Volovik corpus (papers 07, 25, 26, S43 GGE-TEMP, S58 Volovik partition, S61 GGE-THERM) within the scope of this synthesis.

**Convention translation note**: Volovik's condensed-matter `Δ, v_F, T_c, n_s` map to substrate quantities `Δ_B (M_KK units), c_Gold, T_k^GGE (Lagrange multipliers, not thermodynamic T), a_0 (spectral moment)`. The 3He-B coth-Wightman identity is transcribed faithfully; the band-multiplicity 3/3/2 is not a 3He-B structure per se (3He-B has one J=0 BCS gap in the isotropic state) but an SU(3)-Casimir-decomposition-induced extension — the 3He-B inheritance is at the **occupation-spectrum level**, not at the irrep-count level.

*End Volovik S82 synthesis. 12-row summary table. Corridor classified: 1 floor (permanent, asymptotic), 1 ceiling (hard, energy-bounded), 4-PASS narrow-band interior cluster (0.06 OOM). K_matching = 0.6366 structurally inaccessible. 6 S83 carry-forwards queued.*
