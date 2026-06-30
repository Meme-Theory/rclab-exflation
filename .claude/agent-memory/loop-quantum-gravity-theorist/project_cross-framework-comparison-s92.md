# Project — S92 LQG ↔ Phonon-Exflation Cross-Framework Comparison

**Captured**: 2026-05-22 (S92, first invocation)
**Status**: Primary deliverables landed; workshops pre-registered; carry-forwards routed to S93 via WP-style CF entries

## What I wrote in S92

Two artifacts on disk:

1. **`sessions/archive/session-92/session-92-lqg-phonon-exflation-comparison.md`** (633 lines, ~85KB)
   - §I Substrate Scale (kinematical Hilbert space + discrete spectra)
   - §II Cosmogenesis (LQC bounce vs τ_fold transit)
   - §III Black Holes (puncture counting vs spectral monotonicity)
   - §IV Observational + Synthesis (headline question: same, distinct, or partial overlap?)
   - §V Structural-vs-Analogical Parallels Table (~25 distinct parallels enumerated)
   - §VI Workshop Candidates (5 workshops + 3 dropped)
   - §VII Cross-References (citations to LQG corpus, framework corpus, atlas, methodology rules, knowledge MCP)
   - §VIII Closing Note

2. **`sessions/archive/session-92/s92-lqg-comparison-workshop-seeds.md`** (179 lines)
   - 5 workshops re-formatted standalone for /rclab-investigate downstream consumption
   - 3 dropped candidates documented
   - 4 carry-forward computations routed to /rclab-plan (NOT workshops)
   - Recommended dispatch order (highest EVOI first: W4 → W1 → W5 → W3 → W2)

## Headline structural verdict (cite this whenever asked)

**LQG and phonon-exflation share KINEMATICAL structure; they diverge in DYNAMICS.**

Both are honest, well-developed, background-independent quantum gravity programs with discrete substrate spectra, single-parameter pinning, and singularity resolution. They are not the same theory expressed differently. They are not in conflict. They are parallel structural programs with distinct implementations.

The productive cross-framework work lies in identifying:
- where the structural dictionary exists (kinematical layer — see §I)
- where it breaks (dynamical layer — see §II, §III)
- where each could borrow methodology from the other (see §IV.3)

## Six shared structural commitments (across all axes)

1. Background independence
2. Discrete geometric spectra (proven, not assumed)
3. Gauge-invariant kinematical Hilbert space with uniqueness theorem
4. Single-parameter pinning of substrate discreteness (γ vs τ_fold)
5. Singularity resolution via substrate transition
6. Continuum geometry as emergent

## Six distinctive structural commitments (where they diverge)

1. Algebra: SU(2) holonomy-flux / SL(2,ℂ) covariant (LQG) vs `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` NCG triple (framework)
2. Dynamics: combinatorial sum over labelled 2-complexes with 15j (LQG) vs scalar functional `Tr f(D_K/Λ)` with Seeley-DeWitt (framework)
3. Time: emergent internal time from scalar `φ` (LQG/LQC) vs substrate's deformation modulus τ (framework)
4. Cosmogenesis regime: quasi-equilibrium polymer bounce (LQC) vs impulsive supersonic transit (framework)
5. EOS: `w_eff ~ -1` (LQC inflation-like) vs `w = 0.202` (framework decelerating; no accelerated phase)
6. Falsifiability surface: model-dependent (LQC) vs over-constrained by multiple independent conditions (framework)

## What was DEFERRED to follow-up workshops

The 5 workshops in §VI are the deferred adjudications. They are not "computations I didn't do" — they are STRUCTURAL adjudications that genuinely require two-agent adversarial review (per `.claude/rules/Investigating-Workshops.md` 4-condition test).

- **Workshop 1**: Area gap vs D_K spectral floor — same structural role at different scales? (me + connes-ncg-theorist)
- **Workshop 2**: LQC polymer bounce vs τ_fold first-order transit — complementary or incompatible? (me + transit-dynamics-aether-mechanic)
- **Workshop 3**: EPRL vertex amplitude vs spectral action — dictionary, duality, or distinct? (me + connes-ncg-theorist)
- **Workshop 4**: Immirzi γ vs τ_fold — parallel single-parameter pinnings or structurally different? (me + volovik-superfluid-universe-theorist)
- **Workshop 5**: BH entropy — spin-network punctures vs acoustic white hole and spectral monotonicity (me + hawking-theorist)

## Carry-forward computations (routed to /rclab-plan, NOT workshops)

Four solo computations also emerged from the synthesis:

- **CF-S93-LQG-CMB-CROSS-CHECK**: LQC pre-inflationary power spectrum at ℓ ∈ [2, 30] vs framework `n_s = 0.9561` joint Planck fit
- **CF-S93-GFT-BLV-DICTIONARY**: explicit map between GFT condensate cosmology and BLV acoustic metric
- **CF-S93-IMMIRZI-MULTI-CONSTRAINT-INVENTORY**: catalogued constraint count on γ vs τ_fold
- **CF-S93-ACOUSTIC-WHITE-HOLE-LQG-ANALOG-SEARCH**: investigate whether LQG has any transient acoustic-white-hole analog

These are documented in `s92-lqg-comparison-workshop-seeds.md` under the "Carry-forwards" section.

## Methodology decisions I made (cite these in future LQG-side work)

- **Structural-vs-analogical tagging is MANDATORY** for every cross-framework parallel I assert. Tabulated 25+ parallels in §V; ~11 STRUCTURAL, ~7 STRUCTURAL-AT-META-LEVEL-ANALOGICAL-AT-CONTENT-LEVEL, ~5 NON-ANALOGOUS, ~2 LQG-features-the-framework-could-borrow.
- **Convention discipline on Immirzi γ**: U(1) Chern-Simons gives `γ_0 ≈ 0.127`; SU(2) refinements give `γ_0 ≈ 0.2375`. ALWAYS state convention.
- **Substrate-direction discipline**: every parallel flows `Substrate → Bridge → Laboratory`. Inverting is forbidden.
- **Five workshops, three dropped, four carry-forwards** — honest count, not inflated.

## What's NOT covered (open for future LQG-side work)

- The relationship between LQG canonical and covariant formulations on one side, and the framework's `(a_0, a_2, a_4)` Seeley-DeWitt decomposition on the other — this requires the EPRL ↔ spectral action workshop (W3) to resolve.
- Whether the framework's Friedrich-Bär saturation envelope at L_max=12 has any LQG-side analog (LQG truncation is at the graph-level, not the spectral-cardinality level).
- Detailed comparison of LQG's GFT condensate vs the framework's GGE relic — both are non-perturbative many-quanta states post-cosmogenesis; structural dictionary is open.
- Whether LQG's modified-dispersion phenomenology (Paper 13 Amelino-Camelia-Smolin) has any operational connection to the framework's c_Gold = 0.915 M_KK throughput envelope.

These belong to next sessions if a workshop is dispatched.

## What I learned about myself in this work

- The structural-vs-analogical discipline is harder than it looks. The temptation to label a parallel "structural" when it is only "structural at the meta-level" is real. I caught myself doing this in the first table draft and re-tagged everything with explicit sub-tags (STRUCTURAL at X; ANALOGICAL at Y) where the parallel is partial.
- The substrate-direction discipline is also harder. I drafted phrases like "GR's area theorem implies..." several times and had to invert to "the area theorem is DERIVED from substrate spectral monotonicity" each time.
- The Knowledge MCP is essential. The framework constants (`τ_fold`, `M_KK`, `c_sub_baseline`, `w0_FW`, `n_s_canonical`) have provenance entries I would have gotten wrong if I'd inferred from the markdown alone.
- The framework's open problems (FRIEDMANN-BCS-38, FUNCTIONAL-SELECT-67, eps_H sign reversal, τ_fold axiomatic deferred) are NOT failures — they are the constraint map. Stating them honestly is the methodology, not a weakness.
