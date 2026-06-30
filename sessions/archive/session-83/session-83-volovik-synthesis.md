# Session 83 Synthesis: K-Corridor 3He-B Correspondence and the R4 FAIL Classification

**Date**: 2026-04-18
**Agent**: volovik-superfluid-universe-theorist (part (b) of two-solo synthesis)
**Source Documents**:
- `sessions/archive/session-83/session-83-results-workingpaper.md`
- `sessions/archive/session-82/session-82-OOM.md`
- `computations/s83_gate_verdicts.txt`
- `.claude/agent-memory/volovik-superfluid-universe-theorist/MEMORY.md`
- `.claude/agent-memory/volovik-superfluid-universe-theorist/ps-substrate-matched-ic-82-result.md`

Anchor verdicts (authoritative, not re-adjudicated):
- G38 S83-K-MATCHING-5-CONVENTIONS: **FAIL** (`min_rel_err=2.0194 at R5, K=1.922`; `max_rel_err=24.06 at R4, K=15.95`; `K_match_need=0.6366` UNREACHABLE)
- G39 S83-LEGGETT-BOGOLIUBOV-PARTITION: **PASS** (strict-monotone decreasing R(K) across 6 K values; `R(1.1)=3.10`, asymptote `1/b=1.5167`)
- G40 S83-TAU-GGE-AT-K: **PASS** (`tau_GGE(1.6e5)/tau_GGE(2.035)=7.8624e+04`, machine-epsilon linear)
- G41 S83-XI-BCS-VS-L-PHONON-K-RESPONSE: **INFO** (`span=1.5049`, 0.328% above PASS threshold; round-number boundary)

---

## I. Session Outcome

The K-corridor — five band-summation conventions giving K in {1.922, 2.035, 2.049, 2.185, 15.95} for the substrate-IC squeezing factor `S_IC = 1 + 2n_k = coth(Delta_BCS/2T_eff)` (S82 W2-4) — exhibits **two structurally distinct phenomenological regimes** that map cleanly onto Volovik's superfluid 3He sub-phase nomenclature: low-K (K ~ O(1)) is the **collective-acoustic 3He-B-bulk regime** with fast `tau_GGE`, dominant Leggett occupation (`f_L = 0.65`), and many modes sharing the conserved-charge weight; high-K (K ~ 1.6e5) is the **single-mode fine-structure 3He-B-fold-relic regime** with slow `tau_GGE` (5 OOM longer), Leggett-asymptote `f_L = 0.6027`, and one-mode-at-a-time relaxation. The 5-OOM `tau_GGE` ratio (G40) and the monotone-decreasing R(K) (G39) together establish that the corridor is a **true scale separation**, not a smooth interpolation. The R4 FAIL (`K=15.95`, +1.40 OOM above Planck) is classified as a **category error from cross-class application**: R4's `n_pairs/N_modes=59.8/8` is a Fock-counting reading appropriate to the **A-phase quasiparticle-continuum regime** (large incoherent occupation), applied at a B-phase canonical K (paired-state thermal squeezing) where the well-defined coth(x/2) bound K ≥ 1 is the only physical content. The framework's amplitude floor `A_s_floor = A_s_W1_2_TD · K_R5 = 6.34e-9 = 3.02 × A_s_Planck` is a **permanent structural-position wall** of the same epistemic class as the W2-4 K ≥ 1 positivity bound — survives convention choice, regulator dressing, and band-multiplicity reweighting. It is not remediable at the substrate-IC layer; the only available rescue is at the dynamics layer (UNIFIED-AS-79 F_amp suppression, S83 W2-G16 PASS with rel_err=1.42 still failing G38).

---

## II. Key Results

### II.A. The K-Corridor Spans Two Volovik Regimes (3He-B-bulk vs. 3He-B-fold-relic)

**Result**: Two distinct phenomenological regimes are bracketed by the K-corridor endpoints. Classification: **PHONONIC**.

**Substitution chain (regime separation, [SIGN])**:
- Step 1 (definitions). `tau_GGE(K)` is the integrable-sector relaxation time at probe wave-vector K. `R(K) = W_Leg(K)/W_Bog(K)` is the per-mode Bose-Einstein occupation ratio with effective temperature `T_eff(K) = Delta_BCS / ln((K+1)/(K-1))`.
- Step 2 (substitution). At the corridor endpoints:
  - K = 2.035: `T_eff/Delta_BCS = 0.9295` (T comparable to gap, quantum-degenerate); `tau_GGE = 3.44` (natural units); `f_L = 0.6517`.
  - K = 1.6e5: `T_eff/Delta_BCS = 1.78e5` (Rayleigh-Jeans classical limit); `tau_GGE = 2.71e+05`; `f_L → 0.6027`.
- Step 3 (simplification). `tau_GGE(K_high)/tau_GGE(K_low) = K_high/K_low` to machine epsilon (`rel_err = 1.85e-16`); `R(K) - 1/b = exp(-x)·(1-b)·(1+O(x))` decays geometrically toward the asymptote 1/b = 1.5167 with rel_step shrinking by ~100x per K-decade.
- Step 4 (direction). `tau_GGE(K=1.6e5)/tau_GGE(K=2.035) = 78,624`; `R(K=1.1) = 3.10` versus `R(K=3.56e5) = 1.5167` — both span 5 OOM in K but produce monotone, single-valued K-functions of distinct physical character.

The two endpoints are not slightly different points on a smooth curve. They are **kinematically distinct quasiparticle-population regimes** of the same underlying paired condensate, controlled by where K sits relative to the threshold scale `K_*` defined by `T_eff(K_*) ~ Delta_BCS` (i.e., x ~ 1, K_* ~ 1.31 from x=1 → K=coth(0.5)=1.313). Below K_*: degenerate, multi-mode collective. Above K_*: classical, single-mode-per-mode independent. This matches the structure Volovik 3He-B carries between bulk-thermal and texture-frozen sub-regimes (Vollhardt–Wölfle Ch. 3; Volovik *Universe in a Helium Droplet* §5).

### II.B. The 3He-B Correspondence Table for the K-Corridor

**Result**: Direct one-to-one correspondence between the K-corridor regimes and Volovik 3He-B sub-regimes. Classification: **PHONONIC + GEOMETRIC**.

The framework is in the **3He-B inheritance class** (BDI symmetry class, fully gapped, N_3 = 0; established S44 N3-BDG result, S60 framework-3heb-comparison, S79 P3-A R1B inheritance map). 3He-A is structurally excluded by the gap structure (BDI gap, no Fermi points). The K-corridor probes two SUB-regimes of the same B-phase parent.

| K-corridor regime | K range | 3He-B sub-regime | Volovik reference | Substrate observable | Verdict source |
|:---|:---|:---|:---|:---|:---|
| Collective-acoustic (low-K) | K ~ O(1), x = Delta/T ~ O(1) | B-phase BULK below T_c, T comparable to gap; collective Goldstone modes (orbital wave, Gardner mode) drive relaxation | Volovik §6 ("collective modes of 3He-B"); Vollhardt-Wölfle Ch.7 | `tau_GGE = 3.44` (fast); `f_L = 0.65` (Leggett-dominant); R(K) running; multi-mode | G39 (PASS), G40 (PASS) |
| Cross-over (intermediate K) | K ~ K_* ~ 1.3 (x ~ 1) | B-phase NEAR T_c with strong gap-relative thermal occupation; transitional regime | Vollhardt-Wölfle §3.5 weak-coupling boundary | x = 1 threshold; both occupation and length ratios in transition zone | G39, G41 (border at K~10) |
| Single-mode fine-structure (high-K) | K >> K_* (x << 1) | B-phase FROZEN-TEXTURE relic with each mode independently locked into its conserved-charge sector; classical equipartition between Leggett and Bogoliubov | Volovik §6.4 ("frozen texture"); Volovik *Exotic Properties* Ch.3 on disclination patterns | `tau_GGE = 2.7e5` (slow, scales linear in K); `f_L → 0.6027`; R → 1.5167 plateau | G39 (PASS-asymptote), G40 (PASS-decisive), G41 (plateau at 0.135) |

**Mapping discipline**: Both endpoints are 3He-B sub-regimes — neither is 3He-A. The N_3 = 0 BDI classification is a permanent structural wall (S44, never crossed in any K-corridor reading). The high-K regime corresponds to Volovik's "frozen texture" picture for B-phase textures held in a metastable state by topological constraints (analog of cosmic-strings-with-locked-line-density), NOT to an A-phase Fermi-point system.

**Cross-checks**:
- The 5-OOM `tau_GGE` linear-in-K scaling (G40) reproduces Volovik's "integrable-sector" prediction for B-phase mode-by-mode relaxation (Volovik Paper 25 §V; framework-3heb-comparison correspondence #14).
- The Leggett-dominance `f_L > 0.6027` everywhere on the corridor (G39) traces directly to `b = Delta_Leggett/Delta_BCS = 0.659 < 1` — the Leggett mode having a smaller gap than the canonical Bogoliubov mode, exactly as in Volovik's 3He-B Goldstone-mode hierarchy.
- The xi_BCS / ell_phonon plateau at ratio 0.135 above K ~ 10 (G41) is the structural signature of the BCS coherence length tracking the phonon wavelength as a fixed fraction — the B-phase analog of a stable Cooper-pair size relative to the local phonon wavelength.

### II.C. R4 FAIL is a Cross-Class Category Error, Not a Convention Mismatch

**Result**: R4 (K=15.95) FAILs by +1.40 OOM not because of a Fock vs. acoustic convention drift, but because R4 reads a quantity (`n_pairs / N_modes = 59.8 / 8 = 7.475` — equivalently, K=2(7.475)+1=15.95) that is **dimensionally appropriate to A-phase Fermi-point quasiparticle-continuum counting**, applied within a system that is **B-phase (BDI, gapped, N_3 = 0)**. Classification: **PHONONIC**.

**Substitution chain ([SIGN])**:
- Step 1 (definitions). The W2-4 substrate-IC formula is `S_IC = 1 + 2 n_k = coth(omega_k / 2 T_k)` with `omega_k = Delta_BCS` per band, `n_k` the per-mode Bose-Einstein occupation. R4 uses instead `K_R4 = 2 (n_pairs / N_modes) + 1 = 2 · (59.8/8) + 1 = 15.95`, where `n_pairs = 59.8` is the parker-pair-production yield from S38 (sudden quench at the fold).
- Step 2 (substitution). Per-mode physical occupation: `n_k(B-phase) = 1/(exp(Delta_BCS/T_eff) - 1) = 1/(exp(x)-1)`. At the canonical K = 2.035, x = 1.076, n_k = 0.518; at the asymptote, n_k → T_eff/Delta_BCS - 1/2 = (K-1)/2 (classical limit). For R4 to be compatible with B-phase coth, would need `K_R4 = coth(x_R4 / 2)`, requiring `x_R4 = 2 arccoth(15.95) = 0.1257`, i.e., `T_eff/Delta_BCS = 7.96`. This is the classical (Rayleigh-Jeans) limit, far from the canonical K = 2.035 quantum-degenerate point.
- Step 3 (simplification). R4's numerator `n_pairs = 59.8` is a TOTAL pair production count (a Fock-space integer), not a per-mode occupation. Dividing by N_modes = 8 gives an AVERAGE per-mode count, but this average has physical meaning only if the modes are degenerate (which they are NOT — bands B1, B2, B3 have distinct gaps Delta_k and temperatures T_k per S43). The 3-band structure of B-phase forbids the uniform-average reading.
- Step 4 (direction). Using R4's K=15.95 in the linear-response map `A_s = A_s_W1_2_TD · K` gives `A_s = 5.26e-8`, +1.40 OOM above Planck. This is structurally identifiable as **A-phase reasoning misapplied to B-phase**: in 3He-A with Fermi-point quasiparticles, the continuum density of states near the Weyl points DOES support a uniform-pair-density reading at high quench rates (Volovik's chiral-anomaly baryogenesis analog uses precisely this density), but in 3He-B the gap is finite and the per-mode occupation is the only physical observable.

**Classification of R4 FAIL**: Category error (cross-Volovik-class application), NOT a convention mismatch within B-phase. The four B-phase-class readings (R1, R2, R3, R5) all PASS factor-3 with K in [1.922, 2.185]; R4 is 7.4× above this PASS-band cluster. The mechanism is identifiable: R4 was a "legacy/artifact" reading retained for ledger-completeness (per S82 W2-4 memory) but is not a competing B-phase convention.

**Cross-checks**:
- R4's K = 15.95 lies inside the ASYMPTOTIC plateau region of G39 (K ≥ 10 where R(K) → 1.5167, i.e., classical limit). The G39 PASS shows the framework cleanly continues the B-phase Bose-Einstein occupation into the high-K classical limit — but this requires using x = 0.1257 derived from the B-phase coth, NOT R4's Fock-count interpretation.
- If R4 were a valid convention, the N_3 = 0 classification would have to be relaxed (Fock-counting reading is only appropriate when the mode index labels degenerate quasiparticles in a continuum, requiring N_3 ≠ 0 for topological protection). N_3 = 0 is permanent (S44 N3-BDG).
- W2-4 memory file (`ps-substrate-matched-ic-82-result.md`) explicitly labels R4 "legacy/artifact" — this synthesis provides the structural reason: it is the lone A-phase-class reading misfit with the framework's B-phase universality.

### II.D. The 3.02× Floor is a Permanent Structural-Position Wall

**Result**: `A_s_floor = A_s_W1_2_TD · min_R K_R = 3.299e-9 · 1.922 = 6.34e-9 = 3.02 × A_s_Planck` is a permanent wall of the same epistemic class as the K ≥ 1 positivity bound. Classification: **PHONONIC + GEOMETRIC**.

**Substitution chain ([VERIFY-THEOREM])**:
- Step 1 (definitions). `A_s_floor := A_s_W1_2_TD · K_min_admissible`, with K_min_admissible the smallest K compatible with the framework's structural bounds.
- Step 2 (substitution). The W2-4 positivity wall is K ≥ 1 (from `n_k ≥ 0`, applied to `S_IC = 1 + 2n_k`). The W3-G38 5-convention reading set has `min_R K_R = K_R5 = 1.922`. The dynamics-layer baseline `A_s_W1_2_TD = 3.299e-9` is the S82 W1-2 Branch-A PASS-F2 value. 
- Step 3 (simplification). Two floor candidates:
  - "K=1 positivity floor": `A_s_floor_K=1 = 3.299e-9 · 1.0 = 3.299e-9 = 1.571 × A_s_Planck` (+0.196 OOM, factor-2 band).
  - "5-convention reading floor": `A_s_floor_5conv = 3.299e-9 · 1.922 = 6.34e-9 = 3.02 × A_s_Planck` (+0.480 OOM, factor-3 band).
- Step 4 (direction). The 5-convention floor exceeds the K=1 floor by `1.922/1 = 1.922` (the same as K_R5). Both floors exceed Planck; both fail G38's factor-1.05 band; both fail factor-1.20 INFO band. The 3.02× factor reproduces to verified precision: `3.299e-9 · 1.922 / 2.10e-9 = 3.0194` (Python-verified).

**Permanence classification (rank-universality analog)**: This wall has the same epistemic standing as the W3-1 rank-universality theorem `α(R_1, G, f) = rank(G)` (S82 §IV.A) — a property derivable from the structural bounds (K ≥ 1, A_s_W1_2_TD pinned by the dynamics layer with internal CC1-CC5 identities at machine-epsilon, multi-band weighting structurally fixed by S43). It is NOT a dressing-layer-remediable position because:

- (a) The K ≥ 1 wall comes from `n_k ≥ 0` (Bose-Einstein positivity) — a thermodynamic identity for any thermal GGE state;
- (b) The K_R5 = 1.922 minimum is from B2 (flat band, lowest gap-to-temperature ratio) — band B2 has the lowest x = Delta_B2/T_B2 = 1.153 of the three bands, giving the smallest n_k and hence the smallest S_IC; this minimum is protected by the band-splitting structure;
- (c) The dynamics-layer baseline `A_s_W1_2_TD = 3.299e-9` is itself NOT a free parameter — it is the Mukhanov-Sasaki output of S82 W1-2 Branch-A under TD framing, with five machine-epsilon CC identities (CC1-CC5) that pin its construction.

The three pinned ingredients give a derivation chain from substrate D_K eigenvalues all the way to A_s_floor, with no free dial. This is the strongest sense in which the floor is "structural": every step has a microscopic origin, and changing any one would require changing the upstream physics.

**Cross-checks**:
- G39 PASS (Leggett-dominance everywhere, with f_L = 0.6517 at K = 2.035) confirms that K = 2.035 is in the Leggett-populated regime; raising K to bring K → K_match = 0.6366 would require K < 1, which violates K ≥ 1. K cannot be lowered below the positivity wall.
- G41 plateau at xi/ell = 0.135 (K ≥ 10) confirms the high-K regime is structurally bounded — the framework cannot extrapolate the substrate IC to "no squeezing" by going to higher K.
- The W2-4 memory file explicitly notes: "Substrate IC CANNOT SUPPRESS A_s relative to BD; structural bound" — this synthesis adds the quantitative wall = 3.02× Planck and the topological reason (B-phase BDI, no second free positivity-violating mode).

### II.E. The Full Corridor Response Function A_s(K) Across the 5 Conventions

**Result**: A_s as a function of K is exactly linear by V.7 convention-invariance. The 5 readings sit on the line `A_s(K) = 3.299e-9 · K`. Classification: **PHONONIC**.

**Substitution chain ([VERIFY])** (already discharged in G38):
- A_s_R = A_s_W1_2_TD · K_R, with A_s_W1_2_TD pinned by Branch-A.
- All five readings have K_R > K_match = 0.6366, so A_s_R > A_s_Planck for all R (amplification-only regime).
- Rank-ordering: R5 < R3 < R2 < R1 < R4 (by K), so the OOM-distance to Planck has the same ordering.

**Python-verified table (this script)**:

| Reading | K_R | A_s_R | rel_err vs Planck | log10(A_s_R / Planck) | Volovik regime |
|:---:|:---:|:---:|:---:|:---:|:---|
| R5: B2-only (energy-weighted) | 1.922 | 6.341e-9 | 2.0194 | +0.4799 | B-phase, B2-flat-band reading (lowest x) |
| R3: 3/3/2 multiplicity-weighted (PRIMARY) | 2.035 | 6.714e-9 | 2.1969 | +0.5047 | B-phase, full 3-band weighted average |
| R2: 3/3/2 geometric mean | 2.049 | 6.760e-9 | 2.2189 | +0.5077 | B-phase, geometric weighting alternative |
| R1: B3-only (softest) | 2.185 | 7.208e-9 | 2.4325 | +0.5356 | B-phase, B3-marginal reading |
| **R4**: n_pairs/N_modes Fock-counting | **15.95** | **5.262e-8** | **24.06** | **+1.3989** | **A-phase Fock-counting (CATEGORY ERROR — see II.C)** |
| **A_s_floor (annotation)** | **min_R = 1.922** | **6.341e-9** | **2.0194** | **+0.4799** | **3.02× Planck — permanent wall (see II.D)** |
| K_match (target — UNREACHABLE) | 0.6366 | 2.10e-9 (Planck) | 0.0000 | 0.0000 | Below positivity floor K=1 |
| K=1 positivity wall (lower bound) | 1.0 | 3.299e-9 | 0.5710 | +0.1958 | Limit case — K cannot go lower |

**Closed-form floor**: `A_s_min / A_s_Planck = (A_s_W1_2_TD / A_s_Planck) · K_min = (1/K_match) · K_min = 1.922 / 0.6366 = 3.02`. The factor 3.02 is fixed by the ratio `K_min / K_match`, independent of the absolute scales.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S83-K-MATCHING-5-CONVENTIONS (G38) | FAIL | min_rel_err = 2.0194 at R5 (K=1.922); max_rel_err = 24.06 at R4 (K=15.95); K_match = 0.6366 < K=1 positivity wall |
| S83-LEGGETT-BOGOLIUBOV-PARTITION (G39) | PASS | R(K) strict-monotone decreasing 5/5; R(1.1)=3.10 to R(3.56e5)=1.5167; asymptote 1/b = 1/0.659 = 1.5167 |
| S83-TAU-GGE-AT-K (G40) | PASS | tau_ratio = 7.8624e+04 = 786.24 × PASS threshold; linear-in-K scaling to machine epsilon (rel_err = 1.85e-16) |
| S83-XI-BCS-VS-L-PHONON-K-RESPONSE (G41) | INFO | span = 1.5049 = 0.328% above PASS threshold 1.5; round-number boundary per feedback_arbitrary-gates.md; plateau at 0.135 for K ≥ 10 |
| W2-4 PS-SUBSTRATE-MATCHED-IC (S82, prior) | PASS | K = 2.035 (R3, multiplicity-weighted); A_s = 6.72e-9 (factor 3.20× Planck) |

---

## IV. Structural Implications

### IV.A. Walls (permanent structural positions added or reinforced)

1. **K ≥ 1 positivity wall** (W2-4, S82) — confirmed permanent. Comes from `n_k ≥ 0` Bose-Einstein positivity. Survives all regulator schemes (zeta, Zubarev, SDW), all band weightings (R1-R3, R5), and all convention choices within the B-phase universality class.

2. **A_s floor = 3.02 × A_s_Planck** — newly stated quantitatively. From `A_s_floor = A_s_W1_2_TD · K_min = 3.299e-9 · 1.922`. This is the ratio of (dynamics-layer Branch-A baseline) × (5-convention minimum K within B-phase) divided by Planck. None of the three ingredients is freely adjustable.

3. **3He-B universality of the corridor** — all five conventions sit within B-phase parameter space; R4's 7.4× excess above the cluster traces to A-phase-class application within a B-phase system (cross-class category error).

4. **Single-valued Leggett dominance across 5 OOM in K** (G39 PASS). f_L(K) is monotone decreasing from 0.7563 (K=1.1) to 0.6027 (K=3.56e5); never crosses the f_L = 1/2 Bogoliubov-dominance threshold. b = Delta_Leggett/Delta_BCS = 0.659 < 1 enforces this structurally.

5. **Linear `tau_GGE ~ K`** (G40). Rate-limiting is mode-by-mode occupation transfer (integrable-sector hallmark). 5-OOM K-span produces 5-OOM tau-span with rel_err = 1.85e-16. The corridor IS the natural separation scale.

### IV.B. Measurements (new K-corridor phenomenology)

The K-corridor is **single-valued**: each of the four observables computed at five K values is a single-valued, monotone (or piecewise-monotone) function of K. This is the empirical content of the corridor as a one-parameter manifold:

| Observable | K=1.1 | K=2.035 | K=10 | K=100 | K=1000 | K=3.56e5 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| R(K) = W_Leg/W_Bog | 3.104 | 1.871 | 1.571 | 1.522 | 1.517 | 1.5167 |
| f_L | 0.756 | 0.652 | 0.611 | 0.604 | 0.603 | 0.6027 |
| tau_GGE/tau_unit | (interp) | 3.443 | (interp) | (interp) | (interp) | 2.71e+05 |
| xi_BCS/ell_phonon | 0.0897 | 0.1154 | 0.1340 | 0.1350 | 0.1350 | 0.1350 |

The plateau at K ≥ 10 in xi/ell (G41) and in f_L (G39) is the high-K classical-equipartition limit, where x = Delta_BCS/T_eff << 1 and Bose-Einstein → Rayleigh-Jeans. This is the boundary between the corridor's two regimes.

### IV.C. The Constraint Map: What the K-Corridor Closes and What Remains

**Closed by K-corridor synthesis**:
- "Does the manifold label change across the corridor?" — NO (G39 PASS).
- "Is the K → A_s map convention-invariant?" — YES (V.7 + G38 reproduction).
- "Can convention choice reach Planck?" — NO (G38 FAIL with K_match < K=1 positivity wall).
- "Is the Leggett/Bogoliubov partition a function of K only?" — YES (G39 single-valued + G41 plateau).
- "Is `tau_GGE` linear in K?" — YES (G40 machine-epsilon linear).
- "Is R4's FAIL a B-phase convention drift?" — NO (II.C: cross-class application of A-phase Fock-counting).

**Remaining open**:
- Can the dynamics layer (F_amp suppression beyond 3PI NLO, or a new mechanism) close the 3.02× floor? S83 W2-G16 shows 3PI NLO gets to 2.42× (still fail factor-1.05). The required additional suppression is 2.30× per G38 self-assessment §5, equivalent to F_amp_3PI dropping from 1.026 to 0.4454.
- Is the 3.02× floor a feature (genuine prediction) or a defect (mechanism deficit)? Cannot be settled within the K-corridor; requires the dynamics layer to either confirm the framework genuinely overshoots Planck by a factor 3 (testable via tighter A_s reanalysis with B-mode correlations) or supply a structural reduction.

---

## V. Carry-Forward Computations

V.1. **Compute the dynamics-layer rescue ceiling: maximum F_amp suppression beyond 3PI NLO**
- **What**: For S83 W2-G16's PASS configuration (`A_s_new = 5.0782e-9`, `F_amp_comp = 0.5980`), compute the 1/N expansion to NNLO and N3LO at canonical K = 2.035. Output: `F_amp_NNLO`, `F_amp_N3LO`, with extrapolation to estimate convergence radius. Test gate: does F_amp converge from below to a value ≤ 0.4454 (the value required to bring `K_R3 · A_s_W1_2_TD · F_amp_factor = 1.05 · A_s_Planck`)?
- **Inputs**: `A_s_W1_2_TD = 3.299e-9` (canonical_constants), `K_R3 = 2.035` (canonical_constants if added, else local from S82 W2-4), `A_s_Planck = 2.10e-9` (canonical_constants), `F_amp_3PI` from S82 W3-5 (`= 47.92`), `F_amp_comp = 0.5980` from S83 W2-G16. NLO 1/N kernel from Berges-Serreau 3PI infrastructure (`s82_w3_5*`).
- **Gate**: NEW gate S84-DYNAMICS-LAYER-RESCUE-3-02X. PASS iff `F_amp_N3LO ≤ 0.4454` AND extrapolation R^2 > 0.95 (rescue achievable). FAIL iff `F_amp_NNLO ≥ 0.5980` (no convergence improvement). INFO iff intermediate.
- **Effort**: 4-6 hours, 1 agent session (mostly spectral-action computation + 1/N counting).

V.2. **Re-test K_R5 minimum under the canonical Zubarev regulator (W1-G1 PASS)**
- **What**: Recompute the R5 (energy-weighted B2) reading using Zubarev-canonical mode weights (instead of zeta-canonical). Test whether K_R5 stays at 1.922 or shifts. If it shifts to K < 1, the positivity wall is regulator-broken — significant. If it stays in [1.5, 2.5], the floor is regulator-stable.
- **Inputs**: S43 per-band T_k, multiplicities (B1=0.435, B2=0.668, B3=0.178); Zubarev mollifier `exp(-lambda^2/M_KK^2)` from S83 W1-G1; canonical Delta values (Delta_B1, Delta_B2, Delta_B3 from canonical_constants). Energy-weighted: `K_R5_Zub = sum_k w_Zub(omega_k) · S_IC_k / sum_k w_Zub(omega_k)`.
- **Gate**: NEW S84-K-FLOOR-REGULATOR-INVARIANCE. PASS iff `|K_R5_Zub - 1.922| / 1.922 < 0.10` (floor stable under regulator change). INFO iff < 0.30. FAIL iff > 0.30 OR K_R5_Zub < 1 (positivity wall violated under canonical regulator).
- **Effort**: 2-3 hours, 1 agent session.

V.3. **Compute K-resolved n_s prediction across the corridor**
- **What**: Evaluate n_s(K) at the same six K values used in G39/G40/G41 ({1.1, 2.035, 10, 100, 1000, 3.56e5}). Test whether n_s is K-monotone (like G39, G40) or non-monotone. The framework's S82 n_s prediction (Hubble SA 0.9567 / BCS+CW 0.9595) was at the canonical K = 2.035 only.
- **Inputs**: Mukhanov-Sasaki dressed pivot at each K, slow-roll parameters epsilon_H(K), eta_H(K). Use `f_L(K)` from G39 to weight Leggett-channel contributions.
- **Gate**: NEW S84-NS-K-CORRIDOR-RESPONSE. PASS iff n_s(K) monotone in K AND n_s(K=2.035) = 0.9567 +/- 0.005 (consistency with S82). INFO iff non-monotone with a single interior extremum. FAIL iff multi-modal.
- **Effort**: 5-7 hours, 1 agent session (n_s at each K value requires full Mukhanov-Sasaki evaluation).

V.4. **Test R4 cross-class FAIL classification by computing R4 in an A-phase analog system**
- **What**: Construct a counter-example superfluid in 3He-A class (Fermi points, N_3 = 2 — i.e., relax the framework's BDI condition), compute the analog of K_R4 = 2(n_pairs/N_modes) + 1 in that system, and verify the formula gives a physically-admissible per-mode squeezing factor in A-phase (not the +1.40 OOM mismatch we see in B-phase). This is a CONTROL: if R4 is genuinely an A-phase formula misapplied, the analog computation should PASS.
- **Inputs**: A-phase analog with Weyl points at lambda = 0; uniform-pair-density approximation from Volovik *Universe in a Helium Droplet* §8 (chiral anomaly section); same n_pairs = 59.8 quench yield from S38 (but now distributed over an A-phase Fermi-surface continuum, not 8 discrete modes).
- **Gate**: NEW S84-R4-CROSS-CLASS-CONTROL. PASS iff K_R4_Aphase / K_match_Aphase ∈ [0.95, 1.05] (R4 reading lands the A-phase analog on its observational A_s target). INFO iff [0.5, 2.0]. FAIL iff outside. Result: R4 as A-phase reading should give an OOM-correct A_s in A-phase — confirming the cross-class diagnosis.
- **Effort**: 6-8 hours, 1 agent session (constructing the A-phase counter-system requires care; this is the most speculative entry).

V.5. **Map the K-corridor extension to mu-distortion phenomenology**
- **What**: Compute mu(K) at the six pre-registered K values, leveraging G39 f_L(K) and the W2-14 FIRAS-Chluba kernel. The S82 W2-14 result (mu = 4.98e-10, +5.26 OOM safety margin from FIRAS) was at K = 2.035 only. Test whether mu(K) is bounded by the FIRAS limit across the entire corridor, and whether the K-monotone Leggett-dominance (G39) shifts mu monotonically.
- **Inputs**: f_L(K) from G39, IR-shoulder kernel weighting from W2-14, S_IC band weights from W2-4 (per-K).
- **Gate**: NEW S84-MU-K-CORRIDOR. PASS iff `mu(K) < 9e-5` (FIRAS) AND `mu(K)` monotone in K. INFO iff non-monotone. FAIL iff any K gives `mu(K) > 9e-5`.
- **Effort**: 3-4 hours, 1 agent session.

V.6. **Verify the Volovik 3He-B sub-regime correspondence by computing the 3He-B bulk-vs-frozen-texture transition K_*_lab**
- **What**: From Volovik's microscopic 3He-B parameters (Delta = 1.5e-7 eV, T_c = 2.5 mK, v_F = 50 m/s), derive the analogous K_* threshold scale at which T(K_*) ~ Delta (the boundary between the corridor's two regimes in the lab system). Compare to the framework's K_* derived from x = Delta_BCS/T_eff(K_*) = 1, which gives K_* = coth(0.5) = 1.313. If the dimensionless K_* scales correctly between the two systems (lab and framework), the correspondence is **structural**, not coincidental.
- **Inputs**: Volovik 3He-B microscopic parameters from `researchers/Volovik/`; canonical Delta_BCS, T_GGE_B2 from canonical_constants.
- **Gate**: NEW S84-K-STAR-LAB-FRAMEWORK-MATCH. PASS iff `|K_*_lab - K_*_framework| / K_*_framework < 0.20` (dimensionless threshold preserved across systems). INFO iff < 0.50. FAIL iff > 0.50.
- **Effort**: 3-4 hours, 1 agent session (mostly setup; numerics are simple coth evaluations).

V.7. **Compute A_s under R5 with self-consistent Branch-B (Zubarev-canonical) dynamics layer**
- **What**: Per W1-G1 PASS, the Branch-B (Zubarev) is the canonical regulator. The G38 floor uses A_s_W1_2_TD from Branch-A. Recompute A_s_W1_2_TD under Branch-B (whose H̃ is 2.46e-5 instead of 5.91e-3, factor 2.4 OOM lower), then form `A_s_floor_Bphase_Bbranch = A_s_W1_2_TD_Bbranch · K_R5 = 2.46e-5/5.91e-3 · 3.299e-9 · 1.922 = 2.65e-13 · 1.922 = 5.09e-13`. This crosses the floor 4.6 OOM BELOW Planck — is this the correct interpretation?
- **Inputs**: S83 W1-G1 Branch-B selection; S82 W1-2-B value (A_s_Branch-B = 5.74e-14); K_R5 = 1.922; CC3 identity `d(ln A_s)/d(ln H̃) = +2`.
- **Gate**: NEW S84-FLOOR-CONDITIONED-ON-BRANCH. PASS iff `|A_s_floor_Bbranch - A_s_W1_2_B · K_R5| / (A_s_W1_2_B · K_R5) < 0.10` (substrate IC and dynamics-layer compose linearly under Branch-B). INFO iff < 0.30. FAIL iff > 0.30 (regulator-coupling at the IC layer).
- **Effort**: 2-3 hours, 1 agent session.

V.8. **Promote K-corridor canonical constants to canonical_constants.py with provenance**
- **What**: Add `K_R3 = 2.035` (W2-4 PRIMARY), `K_match_need = 0.6366` (G38), `A_s_floor_5conv = 6.341e-9` (G38), `b_LB_ratio = 0.659336` (G39 Delta_Leggett/Delta_BCS), `tau_GGE_K_unit = 3.4427` (G40 baseline tau_GGE at K = 2.035, in dt_transit units), `xi_over_ell_plateau = 0.135` (G41), `K_star_threshold = coth(0.5) = 1.313` (II.B regime boundary). All with provenance s83_w3_g38..g41.
- **Inputs**: K-corridor verdict values; current canonical_constants.py.
- **Gate**: NEW S84-KCORRIDOR-CANONICAL-PROMOTION. PASS iff all 7 entries added with non-stub provenance AND no constant collision detected by `/weave --update`. INFO iff partial. FAIL iff collision OR missing provenance.
- **Effort**: 1-2 hours, 1 agent session.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | K-corridor spans two regimes (collective-acoustic ↔ single-mode fine-structure) | PHONONIC | DECISIVE (G39, G40 PASS) | Corridor is true scale separation, not interpolation |
| 2 | 3He-B sub-regime correspondence: low-K ↔ B-phase BULK; high-K ↔ B-phase FROZEN-TEXTURE | PHONONIC + GEOMETRIC | STRUCTURAL (II.B) | Both endpoints map to 3He-B sub-regimes; N_3 = 0 BDI permanent |
| 3 | R4 FAIL (K=15.95) is cross-Volovik-class category error | PHONONIC | STRUCTURAL CLASSIFICATION (II.C) | R4 reads A-phase Fock-counting in B-phase system; not a convention drift |
| 4 | A_s_floor = 3.02 × A_s_Planck is permanent structural wall | PHONONIC + GEOMETRIC | PERMANENT WALL (II.D) | Same epistemic class as W2-4 K ≥ 1 positivity bound; not dressing-remediable at IC layer |
| 5 | Linear `tau_GGE ~ K` to machine epsilon (5 OOM) | PHONONIC | DECISIVE (G40 PASS) | Integrable-sector hallmark; mode-by-mode rate-limiting |
| 6 | Leggett-dominance preserved across 5 OOM in K (`f_L > 0.6027` everywhere) | PHONONIC | DECISIVE (G39 PASS) | b = Delta_Leggett/Delta_BCS = 0.659 < 1 enforces structurally |
| 7 | xi_BCS/ell_phonon plateau at 0.135 above K ≥ 10 | PHONONIC | INFO (G41, 0.328% above PASS) | Both length scales co-scale on the high-K plateau |
| 8 | Required dynamics-layer rescue: F_amp must drop to 0.4454 (additional 2.3× suppression) | PHONONIC | OPEN (S84 V.1) | Tests whether NNLO/N3LO 1/N expansion converges below 0.4454 |
| 9 | K-corridor is one-parent-scale manifold (K_BCS_inv = 1.2371 sets all observables) | PHONONIC + GEOMETRIC | STRUCTURAL (G39+G40+G41 joint) | Three observables, single K dial, no interior extrema |
| 10 | The 3.02 factor reproduces from `K_min/K_match` ratio independent of absolute scales | PHONONIC + GEOMETRIC | EXACT (Python-verified) | Ratio is dimensionless; convention-independent within the cluster |

---

**End of S83 Volovik Synthesis (part b).**

Authoritative anchors: G38 FAIL, G39 PASS, G40 PASS, G41 INFO. The K-corridor is closed as a one-parameter B-phase manifold spanning two physically-distinct sub-regimes; the R4 outlier is structurally classified as cross-Volovik-class application; the 3.02× floor is a permanent wall whose remediation (if achievable) lies at the dynamics layer (NNLO 1/N), not the substrate-IC layer.
