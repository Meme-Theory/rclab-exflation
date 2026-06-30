# WX-W4-1 — Current S93-Era Whole-Project State-of-Domain Map: Causal Architecture

**Gate**: `WX-W4-1-AGGREGATE-DOMAIN-SURVEY-C-CAUSALITY` ([AUDIT])
**Domain**: causal architecture / `c`-as-emergent-`a_2` / PROPAGATION-vs-SUBSTRATE-DYNAMICS / Spectral-Moment Decoupling / the `c-compare` algorithm.
**Method**: heavy KB sweep (knowledge MCP) across ~93 sessions; `search_knowledge` × ~15 topic threads → `trace_entity`/`get_constant`/`list_constants`/`query_entity` drill-downs. Query manifest in §W4-1 of the working paper.
**Scope of "current"**: S74 (document authored 2026-04-11) → S93. Direction of explanation per `phononic-framing.md` §"IS Space, Not IN Space": `D_K` eigenvalues → `a_2` Seeley-DeWitt → emergent `g_M` → `c_Gold`. The map records what the project NOW knows about how the substrate's spectral structure GENERATES causal architecture; the document's coverage is compared against it in `sx_w4_gap_analysis.md`.

> Reading discipline: this is the **state-of-domain** (the territory). The **gap analysis** is the doc-vs-territory diff. PASS of WX-W4-1 = territory mapped (this file) AND diff enumerated with citations + doc-target-sections (gap file) AND OQ1–OQ10 landed-verdict audit complete (gap file).

---

## Region 1 — Spectral-Moment Decoupling Theorem (the structural core)

**Current state**: LANDED **PASS** at S75 W2-E — "Spectral-moment decoupling CERTIFIED": `a_0, a_2, a_4` algebraically independent (distinct curvature polynomial degrees), Wronskian nonzero (`session-75-tesla-synthesis.md`, `session-75-mack-synthesis.md`; producing script `s75_spectral_decoupling_cert.py`, gate `CERT-75`; imports `a0_fold`, `a2_fold`, `a4_fold`). Subsequently MIGRATED **INFO** at S81 batch hygiene: `T3-BATCH-S75-SPECTRAL-DECOUPLING-CERT: INFO`, `scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA`, `sha256=55a1b9e0a8bebc05d1cecfab1a398c16619f4efddcd36dd19cfc083ea1b7b81e`.

**Mathematical anchor**: Gilkey local index theorem (1975, 1995) — heat-kernel expansion `Tr e^{−tP} ~ Σ_n t^{(n−d)/2} a_n[P]` with `a_n` of distinct dimensional degree `2n−d`, linearly independent as local invariants; Chamseddine-Connes 1996 spectral action `S = Tr f(D²/Λ²) ~ f_4 Λ⁴ a_0 + f_2 Λ² a_2 + f_0 a_4 + …` (cutoff `f(x)~exp(−x)`). This is a theorem of local index theory, NOT a framework convention.

**Companion**: BCS-Sakharov decoupling [PERMANENT, S66 W1]: `a_2, a_4` orthogonal projections, `r_2 = 0.892`. Note: caveat (S64 `a_0/a_2` trap) — the decoupling is about rate-comparability (velocities), NOT value-independence (decreasing `a_2` still worsens CC via the `a_0/a_2` ratio).

**Classification**: GEOMETRIC (the fabric's spectral-triple structure).

## Region 2 — `c_Gold` emergence (the Goldstone group-velocity envelope)

**Current state**: LANDED **PASS** at S75 W3-L — "Emergent c_light from a_2 + a_4": `c_Gold = 0.915 M_KK`, 3-speed hierarchy verified (`session-75-tesla-synthesis.md`; producing script `s75_emergent_lorentz.py`). MIGRATED **INFO** at S81: `T3-BATCH-S75-EMERGENT-LORENTZ: INFO`, `sha256=0f4a28335ed406854f42f2acfd2b2d47ea4b400082e92b2b10ca9a69019804c3`.

**Structural identity** (eq 4.1, S74 workshop E1): `c_Gold² = Z_Gold/M_Gold = 0.915² M_KK²`, where `Z_Gold` (kinetic stiffness, `a_4` projected onto Killing direction) and `M_Gold` (inertial density, `a_2` projected onto Killing direction) are FIXED by the spectral triple. `c_Gold` is a COMPUTATION OUTPUT (`get_constant("c_Gold") = 0.915`, **No PROVENANCE entry**). S52 GL-JOSEPHSON-52 PASS supplies the canonical pin. Structural bracket `[0.62, 1.73] M_KK` (Pippard lower / bi-invariant √3 upper).

**Three/six-speed hierarchy** (S64/S66/S80): `c_fabric = 209.97368021` (substrate sound speed scale, **No PROVENANCE entry**; `c_Gold/c_fabric = 0.00436`, the 229× hierarchy → 2.72 acoustic e-folds, theorem `proven_1157`); `c_mod = 1.000` (emergent photon by construction); `c_BLV = 0.485` (BLV / 3He-B four-speed scalar, **No PROVENANCE entry**); `c_BA = 0.399` (Bogoliubov-Anderson second sound, S56/S63); `c_L = 0.025` (Leggett phase-mode, R-protected LEGGETT-PARTITION-57/58); `K_star_goldstone = 0.185` (Goldstone-continuum crossover).

**Classification**: PHONONIC (group velocity of the Goldstone phononic branch).

## Region 3 — `a_2 → emergent gravity` (`M_Pl_eff = a_2/48π²`) [NEW SINCE S74]

**Current state**: S77 transit-einstein workshop established the quantitative `a_2 → M_Pl_eff → G_N` chain:
- `M_Pl_eff² = a_2(fold)/(48π²) = 2776.17/(48π²) = 5.862 M_KK²` (T2.7, T4.1) [`s76_spectral_perturbation_theory_output.txt`: `M_Pl_spec² = 5.8601 M_KK²`].
- `M_Pl_eff(GeV) = 1.80e17 GeV` (T3.14) from `M_Pl_eff² = a_2 M_KK²/(48π²)` with `M_KK = 7.43e16 GeV`.
- Einstein-Hilbert action: `S_EH = f_2 a_2 M_KK²/(48π²) · ∫ R √g d⁴x` (T5.2); `G_N = 48π²/(f_2 a_2 M_KK²)` (T5.13). The `a_2` Seeley-DeWitt coefficient quantitatively GENERATES Newton's constant.
- FULL-spectrum (L_max=10, 155,984 modes): `a_2(full L10) = 64308.24` → `M_Pl_eff(L10) = √(64308/48π²)·M_KK = 11.65 M_KK = 8.6551e17 GeV` (`s75_f_conv_spectral_output.txt`).

**Two-value distinction**: `a2_fold = 2776.1653888633655` (zeta-scheme half-`ζ_D(1)`, `0.5·Σ_n d_n/λ_n²`; canonical `a2_fold`, S42 CONST-FREEZE-42, line 453) vs `a_2(full L10) = 64308.24` (mode-sum on full spectrum). The fold value is the canonical Seeley-DeWitt coefficient; the L10 value is the truncated full-spectrum sum. The companion `a4_fold = 1350.7216415169728` (zeta-scheme half-`ζ_D(2)`, line ~414→453 region; vs `a_4(full L10) = 29086.18`).

**Classification**: GEOMETRIC (spectral moment → gravity).

## Region 4 — `H_transit` vs `H_Friedmann` two-rate formalism [NEW SINCE S74]

**Current state**: S76 W1-E (POST-FOLD-H-TAU resolution; open channel `Post_Fold_Background_Htransit_vs_HFriedmann_Resolved` closed_by W1-E) + S85 W7 formalization. The two rates (from `session-85-plan-w7.md`):
- `H_transit ≡ (1/Vol_SU3)·dS_fold/dτ` — the Jensen-parameter transit rate, NOT on `g_M` (a_0-sector functional derivative); `dS_fold = 58672.80241318` (S42, line 483).
- `H_Friedmann ≡ (8πG/3·ρ_eff)^{1/2}` — the emergent Hubble rate, `a_2` Seeley-DeWitt moment.
- Stretch factor `F_stretch ≡ (H_transit/H_Friedmann)²` enters the Mukhanov pump split `z″/z = H_Friedmann²·[2 − ε_H + F_stretch·(H_transit-conversion)]`.

This sharpens the document's §3.2/§5.1 statement ("the fold rate is dS/dτ, not a velocity") into the explicit two-rate formalism. `H_transit` is SUBSTRATE DYNAMICS (a_0); `H_Friedmann` is the emergent rate (a_2-derived).

**Classification**: SUBSTRATE DYNAMICS (`H_transit`) vs emergent (`H_Friedmann`).

## Region 5 — Two-Manifold Non-Embedding Theorem

**Current state**: FRIEDMANN-FROM-A2-74 **reframe PROVEN** (atlas-09-retractions Item 35: the assumption "a single `f_conv` scalar can bridge fold-epoch fiber-local energy density to today's emergent 4-metric `H_0`" is BROKEN). FRIEDMANN-BCS-38 **BROKEN** (shortfall 133,200× in coupled dynamics; "structurally addressed by Two-Manifold Non-Embedding Theorem but no replacement single-field formulation exists" — `loop-quantum-gravity-phonon-exflation-comparison.md`). Producing scripts: `s74_friedmann_from_a2.py`, `s75_two_manifold_nemb.py`. Both MIGRATED **INFO** at S81: `T3-BATCH-S74-FRIEDMANN-FROM-A2: INFO sha256=e5b37598547548a5fb6e7b6f48c802a49e57e1eecc72172a19ebe943dea3a913`; `T3-BATCH-S75-TWO-MANIFOLD-NEMB: INFO sha256=d7abcfd28d66a89729cecd866da8fea31c4a1f43632adb6d867f90fdaa703415`.

This UPGRADES the document's §3.2 "candidate pending OQ5" status: the 86-OOM bracket is now a reframe-PROVEN structural signature, and the downstream FRIEDMANN-BCS-38 is BROKEN with the two-manifold theorem as the structural cause.

**Classification**: GEOMETRIC (two distinct emergent `g_M` from two `a_2(τ)` values).

## Region 6 — Layer-1 / Layer-2 split + the S84 two-speed tensor-tilt theorem

**Current state**: The document's Layer-1/Layer-2 `O(τ)` split (§3.3, OQ1) was NEVER landed as a numbered S75 gate (no `LAYER-1-LAYER-2-DIFF-75` verdict in the KB). The closest landed quantitative content is the **S84 two-speed tensor-tilt theorem** [PROVEN, `session-84-mack-synthesis.md`]:
- `n_T(slow-roll, single-speed) = −r/8`; `n_T(two-speed) = −r·c_T/(8·c_S)` (Garriga-Mukhanov 1999 generalized consistency).
- Direction: `c_T/c_S > 1 ⟹ |n_T_two| > |n_T_single|` — the substrate two-speed metric makes the CMB-scale tensor tilt MORE negative than slow-roll consistency.
- `c_T = 1.000` (canonical, S83 G46); `c_S = 0.485` (= `c_BLV`, BCS-dressed + substrate-compaction). S85 W3-5 two-speed transfer identity `c_S_canon = f_B` PASS (machine precision; `max|ratio−1| = 0.000e+00` across all 5 regulators).
- Layer-taxonomy developed at S86 (`s86-sector-2-split-layer-taxonomy.md`, PROVEN, theorems proven_208–213).

So the document's "Layer-1 vs Layer-2 on gapped directions" thesis is realized in the cosmological tensor sector (`c_T` vs `c_S`), with a PROVEN directional theorem, not as a standalone S75 BAO-branch computation.

**Classification**: PHONONIC/GEOMETRIC (branch speeds on `g_M` + cosmological tensor tilt).

## Region 7 — Goldstone masslessness (Kasparov factorization)

**Current state**: `m_Goldstone^{4D} = 0` EXACTLY by Kasparov product factorization (`session-74-qa-vdd-workshop.md`; `[D_total] = π_! ⊗ [D_M⁴]`, Paper 01 van den Dungen 2018/2022, K-HOMOLOGY level). Kasparov product factorization (Paper 01) closed at S61 (all 5 conditions). The gapless Goldstone is the UNIQUE gapless mode on `g_M` (Theorem 3.4); it determines the `c_Gold` envelope. `K_star_goldstone = 0.185` Goldstone-continuum crossover. S82-KASPAROV-ABELIAN-PROOF PASS.

**Classification**: GEOMETRIC (K-theory of the spectral triple).

## Region 8 — NLO Lorentz violation (the unobservable structural prediction)

**Current state**: S83 NLO-1 / `S83-NNLO-BAND-BOUND: FAIL` value=0.000100 (`scheme=Berges-3PI-NNLO-Zubarev convention=W2-canonical-0.025-slope L_max=5`, `sha256=ec83c19fb7b1d4ad2a4b9929250b27de72ec873b6047b00acc66f30e23e671be`; producing script `s83_w2_g11_nnlo_band_bound.py`). The FAIL is a band-bound verdict (the NNLO/LO ratio band test), not a falsification of the zero-LIV claim. **C-FABRIC-42**: `c_fabric = c`, ZERO Lorentz invariance violation at any order; the Amelino-Camelia modified dispersion `v(E) = c(1−(E/E_QG)^β) → v(E) = c for all E` (`session-42-quantum-foam-collab.md`). Structural prediction `c_photon/c_Gold = 1 + α(M_KK/M_Pl)² + β(E/M_KK)²` with `(M_KK/M_Pl)² ~ 2.3e-5`, `(E/M_KK)² ~ 10^{-34}` at MeV; vs GW170817 bound `|c_GW/c_γ−1| < 3e-15` (passes by ~19 OOM).

**Classification**: PHONONIC (propagation NLO correction).

## Region 9 — Spectral-dimension `d_s` flow vs CDT [NEW SINCE S74 — a whole new axis]

**Current state**: S92 ad-hoc workshop (`s92-adhoc-spectral-dimension-ds-flow-vs-cdt.md`) + S93 W7 follow-up (`session-93-plan-w7.md`):
- `d_s(σ) = −2 d ln P(σ)/d ln σ`, `P(σ) = Tr e^{−σ D_K²} = Σ_{(p,q)} dim(p,q) Σ_i e^{−σ λ_i²}` (the return probability / heat trace on the NORMAL-STATE Δ=0 spectrum at converged L_max).
- Substrate `d_s → 8` Weyl asymptotic at the gap scale; NO CDT-like UV reduction in the internal SU(3) fiber (consistent with S31Aa, S34, S44).
- (observable, diffusion-window) discipline: `d_s(σ→0)` (Weyl/manifold dimension) and `d_s(σ_* ~ 1/E_0²)` (windowed at the feature energy, `σ_* = 1.4005 M_KK^{−2}` fold window) are DISTINCT functionals of the SAME `P(σ)`.
- Impedance product `Z(E) = ρ_E(E)·v_g(E)` (the decisive cancellation; the energy-axis DOS exponent `γ_E` is the discriminating sub-quantity).
- AH-PF-1 same-functional-different-scale fair-comparison rule (`phononic-framing.md` + `cross-pillar-bridge-anatomy.md §"Diffusion-window-observable specialization"`, SUGGESTION at K=2 post-S93 W7-3): do NOT compare the substrate's σ→0 asymptotic to CDT's intermediate-window value by letting CDT's scale-type be authoritative.

This is a NEW causal-architecture axis: the dimensionality that propagation "sees" on the substrate, an intrinsic functional of `D_K`.

**Classification**: GEOMETRIC (intrinsic functional of `D_K`).

## Region 10 — Two-scale `α_s` (the substrate-vs-pivot running) [SUPERSEDES §8.2 "flat"]

**Current state**: S92 AH-TR-1 + **S93 W7-1** `S93-W7-1-ALPHA-S-W-KAPPA-FACTORIZATION-DEG-TRANSPORT-BZ-PIVOT: PASS`. Verbatim verdict value: `factorization_holds=False, formulation=T4-non-scalar, deg_T=2.0000, reading=T_is_scalar=False, alpha_s_substrate=-0.08587279, alpha_s_pivot=0.0, shape_inv=5.174e-01, d2_inv=1.463e+00, delta_scheme=0.00`.
- `α_s^substrate = −0.08587279` (canonical `alpha_s_substrate_distance_1`, S92 AH-TR-1; `= (a_4/a_2)² − 1 = d²S_transfer/dk²` at the Mellin-cone pole `s=3`, INSIDE the BZ; orig S88 W4 P5, S91 W9 5-regulator).
- `α_s^pivot = 0.0` (canonical `alpha_s_pivot_goldstone`, S92 AH-TR-1; `= d²(ln P_ζ)/d(ln k_4D)²`, Goldstone-protected `~0`, `|α_s| ≤ 5e-3`, at the CMB pivot).
- `deg(T_{BZ→pivot}) = +2` NON-SCALAR ⟹ the two are DISTINCT observables (Reading-T substrate ≠ pivot). The off-pivot −12.146σ Planck "tension" relocates as a scale-mismatch; pivot-vs-Planck = +0.67σ.
- Governing rule: SCALE-AND-CHANNEL-TAGGING (S92 AH-TR-1, in `phononic-framing.md`): `O^pivot = O^substrate iff deg(T) is the §VII.BA T2-VACUOUS (scalar) case`. Here deg=+2 (non-scalar), so they differ. Both are real substrate-IS observables; which a detector measures is set by `deg(T)`.

This SUPERSEDES the document's §8.2 single-label "α_s = 8.4e-15 flat" claim (the machine-ε value is a Sasaki-Stewart fiber-level `H_b²`-cancellation artifact at one scale; the framework actually carries TWO scale-separated `α_s` observables).

**Classification**: PHONONIC/GEOMETRIC (spectral-tilt running; a velocity-independent observable — STEP 0/STEP 4 of c-compare classify it as not-a-propagation-velocity).

## Region 11 — Acoustic white hole / no-Hawking

**Current state**: S85 W6 `s85_w6_acoustic_white_hole_formal.py` ran (formal treatment; imports `Mach_max`, `tau_fold`, `v_term`); `S85-W6-4-EXTREMAL-HORIZON-FORMAL: PASS` (`value='kappa=0.00e+00' scheme=Jensen_V_tree convention=2D_modulus_metric`); gate `S85-ACOUSTIC-WHITE-HOLE-CAUSAL-DISCONNECT-FORMAL`. Scalar/tensor split (S63 vdd-hawking): `r_s = c_s·r_H` — scalars "see" the acoustic metric (WITH white hole), tensors "see" the gravitational metric (WITHOUT white hole). **Scalar-Tensor Kasparov Decoupling [T3, PERMANENT]**: `U_total = 1_M ⊗ U_K ⟹ β_T = 0` exactly at linear order (VdD-Hawking S63). The "Hawking-like radiation" is the squeezed vacuum `|0_out⟩ = S(r_k, φ_k)|0_in⟩`; no SECOND thermal spectrum on `g_M`.

This UPGRADES the document's §7.3 no-extra-Hawking claim with the landed S85 formalization + the PERMANENT scalar-tensor decoupling theorem.

**Classification**: PHONONIC/SUBSTRATE-DYNAMICS (decorrelation event in the BEC-internal fluctuation spectrum).

## Region 12 — Bogoliubov pair production / squeezing / `f_NL`

**Current state**: **Bogoliubov Gaussianity Preservation** [PERMANENT, S65 W5-D]: `f_NL = O(ε)` regardless of squeezing (Structural). Canonical `f_NL` values: `f_NL^total = 1.03` (S67 GGE-BISPECTRUM-67; 0.57σ vs Planck equilateral `−26 ± 47`); folded shape `f_NL^folded` unique to GGE (3-pathway: `f_NL_folded = 0.0547 + 0.1290 + 0.7685 = 0.9522` decomposition at S86; `0.056` at S82 W3-4 21-cm folded); max `|f_NL| = 1.505` (Bogoliubov-sudden). Squeezing magnitudes `r_B1 = 3.571`, `r_B2 = 1.786`, `r_B3 = 1.963`; `n_pair = 59.8`; per-branch `n̄ = 315.69 (B1), 8.40 (B2), 12.19 (B3)`. Mode equation `u_k″ + ω_k²(τ) u_k = 0`, `ω_k(τ) = √(ε_k² + Δ²)`, with `a_k^out = α_k a_k^in + β_k* (a_{-k}^in)†`, `⟨N_k⟩ = |β_k|² = sinh²(r_k)`, unitarity `|α_k|² − |β_k|² = 1`.

This is the squeezing-pattern observable directly relevant to §5.5/§8.2; the document mentions "f_NL folded shape (S66 Mack)" only in passing.

**Classification**: SUBSTRATE DYNAMICS (creation; mode equation in τ) → PROPAGATION (post-creation propagation on `g_M`).

## Region 13 — Mach 13.75 / sudden quench / 59.8 pairs

**Current state**: **Transit is sudden quench** [PROVEN, S36 T1]: `dt/T_L = 1.25e-5`, `P_exc = 1.000`, dwell time 38,600× shorter than BCS formation time; the transit is parametric, not adiabatic. **59.8 quasiparticle pairs** [PROVEN, S38 T4]: from sudden-quench Bogoliubov, `N_pair = 1` exact reduction confirmed at `1.2e-14`; pair wavefunction 93% B2, 6.3% B1. **Mach 13.75** (baseline-findings-s66): `= v_flow/c_s`, `v_flow ~ 6.667 M_KK`, `c_s = c_BLV = 0.4849 M_KK` (= `v_term/Mach_max = 26.5450/13.75 = 1.93` at the W6 normalization). `Mach_max = 13.75` (line 1844 `Mach_max_framework`, alias 1846). LUTTINGER-SUPERSONIC-73a PASS (`[H_BCS, N_pair] = 0`). S67 MULTI-LEVEL-LZ-67: N-level Landau-Zener saturation `P_exc = 1` in the sudden-quench limit.

This is CURRENT in the document (§2.2, §5.5, §7.2 cite these correctly).

**Classification**: SUBSTRATE DYNAMICS (Mach is a substrate-internal ratio, not a velocity on `g_M`).

## Region 14 — Cross-pillar acoustic-metric bridge / 3He-B BdG [NEW SINCE S74 — post-§VII program]

**Current state**: `cross-pillar-bridge-corpus.md` + atlas-11. Acoustic metric on the fabric: `ds²_acoustic = −(c_BdG² − v_mod²)dt² + (fabric metric)_ij dx^i dx^j` (atlas-qa-collab). **FWD-C3 Pillar IV ↔ Pillar V** (3He-B BdG, `c_BdG`) is the forward bridge candidate (S87 W11-5 instance_2 REGISTRY-FAIL Tier3 violates Tier2 by 21× → K-counter K=1→2 SUGGESTION; `S87-METH-CROSS-PILLAR-BRIDGE-K-COUNTER-UPDATE: PASS`). §VII.W (Pillar III↔IV; HP parity-grading orthogonality) is the first registered cross-pillar bridge [PERMANENT, S86 W-5]. The 5-anatomy IS-not-IN + 3-level discipline + the Level-2-A transit-dynamics audit axis govern registration.

This is the laboratory-IN image of `c_Gold`/`g_M` on the 3He-B child — entirely absent from the document (predates the §VII program).

**Classification**: PHONONIC (lab-IN BdG sound speed) bridged to GEOMETRIC (substrate spectral triple).

## Region 15 — The `c-compare` skill (OQ8 adoption artifact)

**Current state**: `.claude/skills/c-compare/SKILL.md` EXISTS — the 6-step deterministic classifier (STEP 0 spectral-moment localization + STEP 1a tensor existence + STEP 1b Lorentzian cone + STEP 2 source-receiver + STEP 3 dispersion + STEP 4 units + STEP 5 bound `v_g ≤ c_Gold`). The skill formalizes FOUR verdict classes: PROPAGATION / SUBSTRATE DYNAMICS / MIXED / CONTRADICTION, and carries 9 worked examples (the doc §6.3 has 7 edge cases and does NOT enumerate the MIXED/CONTRADICTION verdict classes explicitly). The skill cites the document §6 as its canonical source and is DOWNSTREAM of it. ⟹ OQ8 STEP-0-ALGORITHM-ADOPT-75 is realized (the skill IS the framework-wide adoption artifact).

**Classification**: methodology (a classifier over the causal axis).

## Region 16 — `n*=60` Lefschetz / `v_EW` winding (OQ2)

**Current state**: **`n*=60` PROMOTED PERMANENT** at S75 W3-C — Lefschetz winding `L_max`-invariant, `L_max=7` verified, topological invariant of `L_Y` (`session-75-tesla-synthesis.md`, `session-75-mack-synthesis.md`). The `n*=60 → v_EW` mapping: `v_ew = 246.0 GeV` (canonical_constants.py:1570), `OOM(M_KK/v_ew) = 14.4801` (Sage-Q exact). Producing script `s74_zero_mode_winding.py` (WINDING-74) → MIGRATED INFO at S81 (`T3-BATCH-S74-ZERO-MODE-WINDING: INFO sha256=a9066401de1cb2fbcc8d9c77924a7441979567c15118d0708c36fc6c46352641`). The OQ2 W4M-CHECK question (Bogoliubov-mediated vs direct a_0→a_2): the winding-to-VEV drop is the Higgs-driven 14.48-OOM reduction; the n*=60 dominance is the substrate-level Lefschetz saddle.

**Classification**: GEOMETRIC/PARTICLE (topological invariant of the Higgs bundle).

## Region 17 — Substrate-channel enumeration (OQ9)

**Current state**: S83 operationalized the channel enumeration (`enumerate_observable_channels_s83()` / `enumerate_substrate_admissible_dimensions()`, `session-83-plan.md`). The current substrate-dynamics observational channels: squeezing pattern (`r_k`, `φ_k`), Higgs VEV winding (`n*=60`), `Λ_eff` residual, Leggett DM occupation, squeezing phases. The two-scale `α_s` adds the substrate-distance running channel; the `d_s` diffusion probe adds the dimensionality channel.

**Classification**: PHONONIC (observational portal to substrate dynamics).

---

## State-of-domain summary

The causal architecture is **substantially more developed** at S93 than at S74:
- The five S74 structural theorems all have landed verdicts (Regions 1, 2, 5, 6, 7).
- THREE entirely new causal-architecture axes have appeared since S74: `a_2 → M_Pl_eff` quantitative gravity (Region 3), `d_s`-flow-vs-CDT dimensionality (Region 9), and the two-scale `α_s` substrate-vs-pivot running (Region 10).
- The `c-compare` skill (Region 15) realized the document's OQ8 algorithm framework-wide and EVOLVED the verdict-class enumeration past the document (MIXED + CONTRADICTION).
- The cross-pillar 3He-B BdG acoustic-metric bridge (Region 14) supplies the laboratory-IN image entirely absent from the document.
- Two PROVENANCE gaps remain in `canonical_constants.py`: `c_Gold` and `c_BLV` (and `c_fabric`) carry "No PROVENANCE entry".

The document is **19 sessions stale**: it pre-registered ten S75 computations and records none of their outcomes, and is missing every NEW-SINCE-S74 axis. The gap analysis (`sx_w4_gap_analysis.md`) enumerates the diff.
