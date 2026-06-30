# Capstone Equation Review — lqg

**Date**: 2026-05-29
**Agent**: loop-quantum-gravity-theorist (lqg)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` (THE capstone, S95-era; §0–§9 + verification ledger)
- `.claude/rules/phononic-framing.md` (framing law; binding)
- `researchers/Loop-Quantum-Gravity/` corpus (canonical/covariant LQG, LQC, EPRL/FK, isolated-horizon entropy, GFT, QG-dispersion phenomenology)
- knowledge MCP: `tau_fold=0.19`, `M_KK=7.4287×10¹⁶ GeV`, `ALPHA_BRIDGE_REQUIRED_FW=0.00481`, `T3-S43-SPECTRAL-DISSOLUTION` PASS, Lichnerowicz `λ²≥R_K/4` PROVEN
- my own S92 deliverables: `project_cross-framework-comparison-s92.md`, `project_s92-narrow-path-workshop.md`

---

## I. Session Outcome

The capstone is **structurally honest where it touches my domain** and does not over-reach the one place a loop-quantum-gravity specialist watches most carefully: the discreteness/continuum-limit story. Its §9 "geometry vs topology" spine — *finite spectral triple dissolves in the continuum (`T3-S43-SPECTRAL-DISSOLUTION` PASS, `ε_c ∼ N^{−0.457}`), topological/representation-theoretic outputs survive* — is the same epistemological move loop-quantum-gravity is forced to make about its own kinematical Hilbert space, and the document makes it cleanly rather than papering over it.

The single most consequential cross-framework finding: **the framework's spectral floor IS the Lichnerowicz gap `λ² ≥ R_K(τ)/4 > 0` (E5), and this is the structural analog of the loop-quantum-gravity area gap `a₀ = 4√3πγℓ_P²` — but the document never names this analogy, and naming it correctly is load-bearing.** It is **STRUCTURAL** at the level of "discrete/bounded spectrum of a gauge-invariant geometric operator, proven not assumed," and **ANALOGICAL** (with a known ~200× coefficient mismatch from my own S92 narrow-path workshop) at the level of numerical area-eigenvalue matching. The capstone elides this distinction by simply not raising it; that elision is a missed opportunity, not an error, and §V converts it into a runnable gate.

Second finding, also clean: the capstone's cosmogenesis (§5–§6) is **categorically distinct from the loop quantum cosmology bounce, and the document's own asymmetry theorem (§6.2, "one entry sonic surface, open supersonic exit, NO bounce, over-determined at six walls") makes the divergence sharp rather than fuzzy.** This is correct and it is the right thing to emphasize: a reader who imports loop quantum cosmology intuition about a symmetric quantum bounce will mis-read the entire transit, and the six-wall over-determination is exactly the defense against that mis-reading.

No recorded verdict is overturned. Three places need PRELIMINARY tags or sharper scoping (detailed in §II/§IV); the largest is the `α_LIV = 0` Lorentz-immunity claim in frontier #8, which is **correctly argued at leading order but reaches beyond what is proven at higher order**.

---

## II. Key Results

### II.1 The spectral floor `λ² ≥ R_K/4` is the framework's area gap — STRUCTURAL analog, ANALOGICAL match

**Result**: The Lichnerowicz bound (E5, §2.3) `D_K² = ∇*∇ + ¼R_K ⇒ λ² ≥ R_K(τ)/4 > 0 ∀τ` is the framework's discrete/bounded-spectrum floor. Its structural role is **identical** to the loop-quantum-gravity area gap. Classification: **GEOMETRIC** (it is a statement about the `D_K` spectrum, the fabric itself, not an excitation on it).

In canonical loop-quantum-gravity the area operator `Â(S)` on cylindrical functions of holonomies has discrete spectrum `A_n = 8πγℓ_P² Σ_p √(j_p(j_p+1))` (Rovelli–Smolin 1995; corpus Paper 05 Eq. 5.14, Paper 17 Eq. 17), with a strictly positive minimum nonzero eigenvalue — the **area gap** `a₀ = 4√3πγℓ_P²` (the `√3/2` factor is the `j=½` puncture minimum; my convention pin, `researchers/Loop-Quantum-Gravity/index.md:769-779`). The gap is a *theorem* of SU(2) representation theory on a gauge-invariant kinematical Hilbert space, not an input. The framework's `λ² ≥ R_K/4 > 0` is *exactly the same kind of object*: a strictly positive lower bound on the spectrum of a gauge-invariant geometric operator (`D_K` on the spectral triple `(A_K, H_K, D_K)`), proven (5 proofs, knowledge MCP `framework-mechanism-discussion-hawking-collab.md`: "On a compact positively-curved manifold, the gap is guaranteed"), with the gap controlling whether geometry can be arbitrarily fine. **This parallel is STRUCTURAL** — both are spectral gaps of gauge-invariant geometric operators on a finite/discrete kinematical layer, both proven, both the floor of geometric resolution.

Where it becomes **ANALOGICAL**, and where the capstone is silent in a way that matters: the *numerical* matching of an area eigenvalue. My S92 narrow-path workshop (`project_s92-narrow-path-workshop.md`) operationalized the §IX.7 derivation procedure (Peter-Weyl projection of `D_K` modes onto an emergent 2-surface → area-spectrum matching against `Â(S)`) and reduced it to a single empirical number: the bridge coefficient `α_bridge`. The knowledge MCP confirms the canonical pin `ALPHA_BRIDGE_REQUIRED_FW = 0.00481`. If the substrate produces `α_bridge ≈ 4.81×10⁻³` → Regime I, emergent `γ_emergent = γ_BH = 0.2375` (SU(2) convention) — a genuine match. If the substrate produces `α_bridge ∼ O(1)` → Regime II, `γ_emergent ∼ 50` (~200× too large) — a STRUCTURAL FAILURE with **no recovery mechanism**, because γ does NOT admit cutoff/RG running in canonical loop-quantum-gravity (Paper 03 §VII; my S92 Q2 answer). The substrate-side prior (the post-fold acoustic e-folds count `N_e ≈ 2.92` produces O(1) bulk-to-surface reductions, not 10⁻³-suppressed ones) puts the likely outcome at **Regime II**. The capstone's §9 "topological survives, geometric dissolves" spine is consistent with this — area-eigenvalue *matching* is a geometric-magnitude claim and would be on the dissolving side — but the document does not connect its own spine to the loop-quantum-gravity area-gap question, and that connection is exactly the kind of structural-vs-analogical adjudication my role exists to make explicit.

### II.2 The "geometry vs topology" spine is the loop-quantum-gravity continuum-limit problem, stated correctly

**Result**: §9's organizing spine — `(A_K, H_K, D_K(τ))` is GEOMETRY and dissolves in the continuum (`T3-S43-SPECTRAL-DISSOLUTION` PASS, knowledge MCP `s81_gate_verdicts.txt`, `ε_c ∼ N^{−0.457}`); topological/representation-theoretic outputs (GGE relic purity `S_ent=0`, BDI/`N₃=0` class, the `7.324992` cocycle ratio, `[J,D_K]=0` CPT, layer algebraic independence, FI ratios `R₁=1.12865`) survive — is the framework's version of loop-quantum-gravity's hardest open problem. Classification: **GEOMETRIC** (about the triple's continuum behavior).

This is the right move and I want to state plainly that it is *more honest than loop-quantum-gravity has historically been about the same issue*. Loop-quantum-gravity's semiclassical/continuum limit — recovering smooth general relativity from spin-network coherent states as `j → ∞` — remains **incomplete** (this is one of my standing "honest open problems"). The framework faces the structurally identical question (does the finite-`L_max` triple's physics survive `L_max → ∞`?) and answers it by *partitioning the outputs*: it trusts only the truncation-robust topological/ratio observables and explicitly holds the absolute-magnitude geometric observables pending an SDW-convergence statement (`JACOBSON-NONLOCAL-64`, OPEN; §8.5, frontier #6). That partition is sound. In loop-quantum-gravity terms: the area *gap* (a representation-theoretic floor) survives the continuum limit in the sense that it is a spectral-theoretic theorem; an individual area *magnitude* in physical units is the part that depends on the regulator/continuum details. The framework's `R₁ = a₀a₄/a₂² = 1.12865` (scheme-invariant ratio, Sage-verified `1.128655`) is the analog of a loop-quantum-gravity ratio-observable that is robust to the spin-network refinement, while the absolute CC magnitude is the analog of a quantity that is not. **The spine is solid; I cross-checked the dissolution exponent against the recorded gate and it holds.**

### II.3 Cosmogenesis: impulsive supersonic transit, NOT a loop-quantum-cosmology bounce — divergence is sharp and correct

**Result**: §5.1–§5.3, §6.2. The transit is a first-order, diabatic, supersonic (Mach 13.75) crossing of a van Hove fold at `τ_fold = 0.190` (knowledge MCP confirms `tau_fold = 0.19`), driven by a *monotone* gradient (`dS/dτ|_fold = +58,672.8`, E7) with **no potential well and no interior saddle**. The post-fold state is an analytic Generalized Gibbs Ensemble (`P_exc = 1.000`, `S_ent = 0`, the Ordered Veil). Classification: **PHONONIC** (the GGE relic IS the post-transit excitation content of the fabric).

This is a **NON-ANALOGOUS** cosmogenesis relative to loop quantum cosmology, and the capstone's framing is exactly right. Loop quantum cosmology replaces the Big Bang singularity with a **symmetric quantum bounce** at `ρ_c ≈ 0.41 ρ_Planck` (Ashtekar–Pawlowski–Singh; corpus Paper 17 Eq. 19, `ρ_sup = 18πGℏ²/Δ³`), via polymer modification of the effective Friedmann equation `H² = (8πG/3)ρ(1 − ρ/ρ_c)`. The loop-quantum-cosmology bounce is **quasi-equilibrium and adiabatic** — the universe passes smoothly through a minimum scale factor and re-expands, and the effective dynamics is governed by a stationary-point structure. The framework's transit is the **opposite regime in three independent ways**: (i) it is *impulsive/diabatic* (`δt_transit/T_L = 1.25×10⁻⁵`; the crossing is 38,600× faster than the condensate can form), not adiabatic; (ii) it has *no interior saddle* (E7 monotonicity, one-loop-robust per S95 W2-3), so there is no symmetric bounce point to pass through; (iii) §6.2's six-wall asymmetry theorem proves the causal structure is an **asymmetric acoustic white hole — one entry sonic surface, open supersonic exit, "no future-trapped exit horizon, no symmetric throat, no bounce."** I confirm this is a clean structural divergence: a reader carrying loop-quantum-cosmology intuition would expect a bounce and a near-`w ≈ −1` super-inflationary phase; the framework delivers neither (`w` decelerating, no accelerated phase). The capstone is correct to refuse the bounce vocabulary, and the over-determination at six walls is the right defense.

One sharpening for honesty: the *no-singularity-at-genesis* claim is genuinely weaker than loop quantum cosmology's, and the document already says so (§5.2: the genuine curvature singularity is *relocated to `τ→∞` and censored*, not absent — anisotropic Kasner-type, Kretschmann `K ∼ e^{4τ}`). This is the more honest statement and it is the loop-quantum-cosmology-distinct one: loop quantum cosmology *removes* the singularity by quantum geometry; the framework *censors* a classical singularity that still exists at the modulus boundary. Both resolve the observable pathology; the mechanisms are different, and the capstone names the difference. Good.

### II.4 The `α_LIV = 0` Lorentz-immunity claim — correct at leading order, over-reaching at higher order

**Result**: §9 frontier #8. The document claims the framework is immune to the modified-dispersion / Lorentz-violation tests (Fermi-LAT, LHAASO, interferometry) that constrain most quantum-gravity candidates, because "the substrate's discreteness is internal (the SU(3) fiber tower at `M_KK`) and the emergent metric `g_M` is the `a₂` moment of a *continuous* heat-kernel trace, not a discretized spacetime," with `α_LIV = 0` exactly, invoking Hossenfelder's no-go (Poincaré-invariant discrete *spacetime* networks are impossible). Classification: **GEOMETRIC**.

The structural argument is **correct as far as it goes, and the contrast with loop-quantum-gravity is real and worth stating from my side**: loop-quantum-gravity's discreteness *is* in the emergent spacetime (the area/volume operators measure emergent 3-geometry), which is precisely why loop-quantum-gravity has a live modified-dispersion phenomenology (corpus Paper 13, Amelino-Camelia–Smolin; the `E_QG` bounds from Fermi-LAT/HESS constrain Planck-scale spacetime granularity). The framework's discreteness is in the *internal fiber* (the `SU(3)` KK tower), and `g_M` is read off a continuous trace — so the naive "discrete spacetime → modified dispersion" pipeline genuinely does not fire. I agree the leading-order pipeline is absent.

**Where it over-reaches:** "`α_LIV = 0` exactly" is a statement about *all orders* of emergent Lorentz invariance, and the document's own frontier #8 immediately qualifies it: emergent Lorentz invariance / higher-order isotropy is registered **INFO, not PROVEN** (`T3-BATCH-S75-EMERGENT-LORENTZ`), and is *inherited* from the Volovik gap-node universality class, not derived. The S95 W3 update is even more candid: the two exact-PASS gates supporting emergent-EP promotion (`κ_EP = 1.000000`, conservation-closed `G_eff^{μν}`) are **generic-identity-cored** — `κ_EP = 1` is just the Lichnerowicz `R/4` coefficient of *any* spin Dirac operator, and the genuine substrate EP *prediction* first appears at NNLO (`CF-S96-EP-NNLO-CASIMIR-DISCRIMINATOR`). So the honest statement is: *leading-order Lorentz invariance and weak EP are structurally inevitable on the single-operator postulate (value-generic); higher-order emergent isotropy — and hence the actual magnitude of any residual LIV — is INFO, not zero-by-theorem.* "`α_LIV = 0` exactly" should be **`α_LIV = 0` at leading order; higher-order residual INFO, PRELIMINARY pending NNLO** to be consistent with frontier #8's own caveat. This is the loop-quantum-gravity-side point: loop-quantum-gravity *predicts* a (constrained) LIV signature; the framework's claim of *exact* immunity is a stronger statement than its own evidence, and the gap is exactly the NNLO Casimir-discriminator the document itself queues. The structural reason for *suppression* is solid; the claim of *exact zero to all orders* is not yet earned.

### II.5 The `a(t)` gap — the one place loop quantum cosmology delivers and the framework does not

**Result**: §6.1, §6.3, frontier #1. The framework has **no derived FRW scale factor `a(t)`**: C1 postulates "`τ` parameterizes cosmic time"; C2 (`K_pivot`) is BROKEN-WITH-LIVE-RESEARCH-PATHWAY; T6 (Friedmann–BCS locking) is BROKEN (155,984-mode spectral action overwhelms 8-mode BCS by 133,200×); the S74 W1-E Friedmann result is a *structural* FAIL. What exists are two non-interchangeable PROXY scale factors (`a_eff` from `a₂`, near-flat; `a(τ)` from Connes distance, carries the deceleration band). Classification: **GEOMETRIC** (a property of the emergent metric's construction).

This is the cleanest "loop-quantum-gravity could lend methodology" point in the whole document, and the capstone is scrupulously honest about it (§6.3 is the "most important caveat in the document, stated without softening" — I confirm it is the right caveat and it is stated at the right strength). **Loop quantum cosmology's signature achievement is precisely the object the framework lacks**: a derived *effective Friedmann equation* `H² = (8πG/3)ρ(1 − ρ/ρ_c)` obtained from polymer quantization of the homogeneous-isotropic sector — a substrate-derived `a(t)`. The framework derives that `τ` is a *legitimate monotone clock* (E7) but explicitly borrows the container-observer's FRW `H(t)` for every late-time observable (caveat C10). The structural difference is that loop quantum cosmology *symmetry-reduces first* (freezes to the homogeneous-isotropic minisuperspace, then quantizes) and gets `a(t)` directly, whereas the framework quantizes the full internal geometry and owes the *lift* `S_SA(τ) → 4D covariant action for g_M`. The document correctly identifies this as a single object that simultaneously closes frontiers #1 and #8 (effective Friedmann map = emergent equivalence principle = emergent Einstein–Infeld–Hoffmann), which *reduces* the open-frontier dimensionality. **There is a concrete methodology-transfer here** (GFT condensate cosmology — Oriti's reformulation of loop-quantum-gravity as a QFT on the group manifold — derives an effective Friedmann equation from condensate *hydrodynamics*, and the framework's GGE relic is structurally a non-perturbative many-quanta condensate-like state); whether that transfer is operational is a §V item.

---

## III. Gate Verdicts

No new gates are adjudicated in this review. The capstone-cited gates I cross-checked against the knowledge MCP (all confirmed, none overturned):

| Gate | Verdict (as recorded) | Decisive Number | Cross-check |
|:-----|:----------------------|:----------------|:------------|
| `T3-S43-SPECTRAL-DISSOLUTION` | PASS | `ε_c ∼ N^{−0.457}` | Confirmed `s81_gate_verdicts.txt`; underwrites §9 spine |
| Lichnerowicz gap (E5/W3) | PROVEN | `λ² ≥ R_K/4 > 0` | Confirmed `framework-mechanism-discussion-hawking-collab.md`; = framework area-gap analog |
| `CONST-FREEZE-42` (`tau_fold`, `M_KK`) | frozen | `0.19`; `7.4287×10¹⁶ GeV` | Confirmed via `get_constant` |
| `S95 W2-1` (t* one-loop corridor) | FAIL (CLOSED) | `R = 1.977` | Cited §1.4; not re-adjudicated |
| `ALPHA_BRIDGE_REQUIRED_FW` (my S92 pin) | canonical | `0.00481` | Confirmed via `get_constant`; Regime-I/II threshold (NOT in capstone) |
| `T3-BATCH-S75-EMERGENT-LORENTZ` | INFO | — | Cited frontier #8; supports my II.4 over-reach flag |

---

## IV. Structural Implications

**The capstone's discreteness story is loop-quantum-gravity-compatible and, on the continuum-limit question, more honest than loop-quantum-gravity's own.** The "topological survives, geometric dissolves" partition (§9) is the correct response to the question that has dogged loop-quantum-gravity for two decades (does the discrete kinematical structure survive the classical/continuum limit?). The framework answers it by trusting only truncation-robust observables. This is sound and I recommend it be read as a *strength* relative to background-independent quantum gravity generally, not as a hedge.

**The area-gap analogy is unstated and load-bearing.** The single highest-value addition my domain can make to this capstone is to name the structural analogy `λ² ≥ R_K/4` ↔ loop-quantum-gravity area gap explicitly, *and* to bound it correctly: STRUCTURAL at the spectral-floor-as-theorem level, ANALOGICAL (with the `α_bridge` Regime-II ~200× coefficient risk) at the area-eigenvalue-matching level. Leaving this implicit invites two opposite mis-readings: (a) a reader assumes the framework *is* loop-quantum-gravity-with-a-different-algebra (over-claim — the dynamics, the algebra `A_K = ℂ⊕ℍ⊕M₃(ℂ)` vs SU(2) holonomy-flux, and the spin-foam-vs-spectral-action split all diverge); or (b) a reader assumes there is no connection (under-claim — the kinematical structural commitments genuinely coincide: background independence, discrete/bounded geometric spectra proven not assumed, single-parameter pinning of substrate discreteness). The constraint-map update: the framework occupies the *kinematically-loop-quantum-gravity-adjacent, dynamically-distinct* region — the same region I mapped in S92. This capstone does not contradict that mapping; it instantiates it.

**Cosmogenesis is the cleanest divergence and should stay sharp.** The §6.2 asymmetry theorem (no bounce, six walls) is the right structural defense against loop-quantum-cosmology contamination. I recommend it not be softened: the framework's transit is *impulsive non-equilibrium* where loop quantum cosmology is *quasi-equilibrium adiabatic*, and conflating them would corrupt the GGE-relic reading (the Ordered Veil's `P_exc = 1` diabatic saturation is the *opposite* of the loop-quantum-cosmology adiabatic-vacuum no-particle limit). The capstone holds this line.

**Two scope-tightenings owed.** (1) `α_LIV = 0 exactly` (frontier #8) must read `= 0 at leading order; higher-order INFO/PRELIMINARY` to match its own NNLO caveat — otherwise the document claims, in one sentence, a stronger result than the frontier it sits inside admits. (2) The `a(t)` gap (§6.3) is correctly stated but its loop-quantum-cosmology contrast is absent: the document says "Friedmann is the wrong question at the fundamental level, the right question at the effective level" without noting that a *peer background-independent program (loop quantum cosmology) delivers exactly the effective object the framework owes*. Naming this is not a weakness-admission; it identifies a concrete methodology-transfer target (GFT-condensate → effective-Friedmann) and sharpens what "owed" means.

**No conflict between the capstone and my memory.** My S92 verdict ("share kinematical structure, diverge in dynamics") is reproduced, not contradicted, by every section I examined. The one item my memory holds that the capstone does *not* surface — the `α_bridge` Regime-I/II area-spectrum-matching gate — is an *addition*, not a conflict; it lives on the geometric-magnitude (dissolving) side of the document's own spine, which is internally consistent.

---

## V. Carry-Forward Computations

**The user's "ripe harvest" framing applied to my domain: each open question the capstone exposes at a loop-quantum-gravity contact point is converted to a runnable gate below.** Every entry has all four fields.

```
V.1. Area-spectrum matching: compute the substrate α_bridge and decide Regime I vs II
   - What: Evaluate the §IX.7 narrow-path area-spectrum match. Project the bottom-N D_K(τ_fold)
     eigenmodes (Peter-Weyl-decomposed) onto the acoustic-white-hole exit-horizon 2-surface
     (τ≈0.16, my S92 natural 2-surface), compute the Hochschild-cocycle pairing
     ⟨[S_exit-horizon]^♯, [Ch(P_0)]⟩ that yields the area-eigenvalue contribution, and extract
     the dimensionless bridge coefficient α_bridge. Compare against ALPHA_BRIDGE_REQUIRED_FW.
   - Inputs: s84_spectrum_cache_L12_tau019.npz (bottom-N eigenmodes); canonical_constants
     ALPHA_BRIDGE_REQUIRED_FW = 0.00481, tau_fold = 0.19, M_KK; LQG area operator target shape
     (Paper 05 Eq. 5.14; researchers/Loop-Quantum-Gravity/index.md:769-779); E5 Lichnerowicz
     floor λ² ≥ R_K/4; bridge-map class registry sessions/framework/correspondence/
     lqg-narrow-path-bridge-class.md (HKR with -Cheeger-Simons suffix).
   - Gate: NEW gate LQG-AREA-MATCH-S96. PASS (Regime I): |α_bridge − 0.00481|/0.00481 < 0.20
     ⇒ γ_emergent = γ_BH = 0.2375 recovered. FAIL (Regime II): α_bridge ∼ O(1) ⇒ γ_emergent
     ~200× too large, no recovery (γ has no cutoff running, Paper 03 §VII) ⇒ records the
     framework's spectral-floor↔area-gap parallel as STRUCTURAL-at-floor / ANALOGICAL-at-match.
     INFO: cocycle [S_exit-horizon]^♯ is HH-trivial (no non-trivial class on this triple).
   - Effort: 6-8 hours, 1 agent session (Hochschild cocycle machinery is the cost; eigenmode
     cache exists). Feeds the §9 geometry-vs-topology spine (locates area-matching on the
     dissolving side) and closes the S92 Workshop-6 first dispatch.

V.2. Joint pre-flight: substrate Cauchy-Schwarz ∧ LQG area-volume uncertainty
   - What: The highest-EVOI test from my S92 narrow-path workshop. Compute, substrate-side, the
     Cauchy-Schwarz bound on the (area-proxy, volume-proxy) D_K-moment pair at τ_fold; compute,
     LQG-side, the Bojowald area-volume uncertainty relation ΔÂ·ΔV̂ ≥ |⟨[Â,V̂]⟩|/2 for the
     matched intertwiner content; check whether the substrate pair SATURATES or VIOLATES the
     LQG-side uncertainty floor. Saturation → Regime-I-consistent; gross violation → the
     substrate's narrow-path effective theory is LQG-like in form, distinct in coefficient.
   - Inputs: s84_spectrum_cache_L12_tau019.npz; area-volume uncertainty form (Paper 04 Bojowald
     2001, researchers/Loop-Quantum-Gravity/index.md:786); E5 gap; volume operator analog
     (second D_K moment); canonical_constants tau_fold, M_KK.
   - Gate: NEW gate LQG-UNCERTAINTY-JOINT-S96. PASS: substrate pair satisfies the LQG-side
     uncertainty floor within factor 2. FAIL: violates by >1 OOM ⇒ substrate kinematics is
     structurally non-LQG at the operator-algebra level. INFO: the commutator [Â,V̂]-analog
     vanishes on the substrate (operators commute) ⇒ no uncertainty relation to test.
   - Effort: 4-5 hours, 1 agent session. This is the gate the S92 workshop pre-registered as
     the Wave-1 verdict that decides Workshop-6's target; LQG-AREA-MATCH (V.1) is its companion.

V.3. GFT-condensate → effective-Friedmann transfer for the a(t) gap
   - What: Test whether Oriti's GFT condensate-hydrodynamics derivation of an effective Friedmann
     equation can be transplanted onto the framework's GGE relic. Treat the post-fold GGE
     (59.8-pair-charge product state, S_ent=0) as a condensate of D_K quasiparticles; write the
     condensate "mean-field" expectation as a function of τ; derive the hydrodynamic continuity +
     "Friedmann-like" equation for the condensate-density analog; check whether it reproduces a
     monotone H(τ)-analog consistent with the Connes-distance proxy a(τ) (q from −0.97 to +0.81,
     SCALE-FACTOR-54) rather than the near-flat a_eff.
   - Inputs: GFT condensate-Friedmann formalism (Oriti, LQG corpus GFT papers); GGE relic data
     (E18: N_pair=59.8, P_exc=1.000, S_inst=0.0686); SCALE-FACTOR-54 Connes-distance a(τ) and
     its q-band; the broken T6 result (133,200× overwhelm) as the obstruction to beat;
     canonical_constants tau_fold, M_KK, c_fabric=209.97 M_KK.
   - Gate: NEW gate GFT-FRIEDMANN-TRANSFER-S96. PASS: condensate-hydrodynamic H(τ)-analog
     reproduces the SCALE-FACTOR-54 q-band within 20% ⇒ a candidate derived-effective-Friedmann
     route for frontier #1/#8. FAIL: the transfer produces near-flat a_eff or diverges ⇒ GFT
     route does NOT close the a(t) gap, eliminating one adjacency. INFO: transfer is formally
     ill-posed because the GGE is a non-equilibrium frozen state, not a GFT equilibrium condensate
     (the loop-quantum-cosmology-distinct regime — would itself be a structural result).
   - Effort: 8-10 hours, 1 agent session. Directly attacks the document's single most important
     open frontier; the loop-quantum-gravity side (GFT condensate cosmology) is the peer program
     that already has the missing object.

V.4. Scope-tighten α_LIV: compute the NNLO Casimir-discriminator residual dispersion
   - What: Settle whether "α_LIV = 0 exactly" (frontier #8) survives to higher order. Compute the
     emergent dispersion relation ω(k) for the a₂-channel (tensor) and the scalar channel to NNLO
     in the heat-kernel expansion, where the band-Casimir ν_b(C₂) re-enters (the CF-S96-EP-NNLO
     discriminator the document queues). Extract any momentum-dependent correction δω/ω ∝ (k/M_KK)^n
     and compare its magnitude to the Fermi-LAT/LHAASO/interferometry E_QG bounds the document
     claims immunity from.
   - Inputs: D_K(τ) heat-kernel a₄, a₆ moments (the NNLO terms); band-Casimir ν_b(C₂) for
     B1/B3 bands; E5 Lichnerowicz coefficient (the generic-identity core κ_EP=1, S95 W3); LQG
     modified-dispersion bound forms (Paper 13 Amelino-Camelia–Smolin, E_QG ≳ M_Pl); M_KK.
   - Gate: NEW gate ALPHA-LIV-NNLO-S96. PASS: NNLO residual δω/ω < (current E_QG bound)/M_KK
     ⇒ α_LIV ≈ 0 confirmed to NNLO, the frontier-#8 immunity claim earns "to NNLO". FAIL: a
     non-zero NNLO LIV residual appears ⇒ "α_LIV = 0 exactly" must be retracted to leading-order;
     the residual becomes a falsifiable framework prediction (distinguishing it from exact
     immunity). INFO: residual is band-degenerate (cancels by the single-operator postulate).
   - Effort: 5-6 hours, 1 agent session. Converts the §II.4 over-reach flag into a verdict and
     either earns or bounds the document's strongest phenomenological-immunity claim.

V.5. Spectral-dimension closure: confirm no flow against the LQG/CDT reduction story
   - What: The capstone's §3.2 defensive note (no flowing spectral dimension, d_s ∼ 8 at the gap
     scale, S31Aa/S92) is the cross-framework contrast point with both CDT and string-worldsheet.
     Re-confirm d_s(σ) = −2 d ln P(σ)/d ln σ with P(σ) = Tr e^{−σD_K²} at τ_fold across the full
     diffusion-window range (σ → 0 Weyl asymptotic AND the fold window σ_* = 1.4005 M_KK^{−2}),
     and state explicitly the (observable, diffusion-window) pair on BOTH the substrate side and
     the CDT-reference side per the cross-pillar-bridge-anatomy diffusion-window specialization,
     so the "no UV reduction" claim is fair-compared (same Φ at same scale-type).
   - Inputs: d_s_fold_window_sigma = 1.4005 (canonical_constants); s84 spectrum cache (full
     eigenvalue set for the heat trace); the S92 ad-hoc workshop s92-adhoc-spectral-dimension-
     ds-flow-vs-cdt.md (eq_6590–6593); CDT/asymptotic-safety reference d_s plateau values;
     M_KK.
   - Gate: NEW gate SPECTRAL-DIM-NOFLOW-S96. PASS: d_s(σ→0) ≈ 8 (Weyl/manifold dimension) with
     NO 12→5.65→4 or 10→2→4 reduction in the gap window ⇒ confirms structural distinctness from
     CDT and string (a clean cross-framework contrast). FAIL: a genuine d_s flow appears ⇒ the
     §3.2 claim is wrong and the substrate DOES share CDT-like dimensional reduction. INFO: the
     windowed low-d_s reading is a diffusion-window artifact (the S92 finding) and not a flow.
   - Effort: 3-4 hours, 1 agent session (heat-trace evaluation is cheap; the discipline is the
     fair (observable, window) pairing). Validates a load-bearing defensive note that a
     quantum-gravity referee will probe first.
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| II.1 | `λ² ≥ R_K/4` (E5) IS the framework's area gap; STRUCTURAL analog of LQG `a₀=4√3πγℓ_P²`, ANALOGICAL at eigenvalue-matching (`α_bridge` Regime-II ~200× risk) | GEOMETRIC | SOLID (parallel); analogy UNSTATED in capstone | Highest-value domain addition; name it + bound it (→ V.1, V.2) |
| II.2 | §9 "topology survives, geometry dissolves" spine = LQG continuum-limit problem, answered by output-partition (`ε_c ∼ N^{−0.457}` PASS) | GEOMETRIC | SOLID; more honest than LQG's own semiclassical-limit story | Read as a strength vs background-independent QG generally |
| II.3 | Cosmogenesis = impulsive supersonic transit + asymmetric white hole (six walls, NO bounce) | PHONONIC | SOLID; sharp NON-ANALOGOUS divergence from LQC quasi-equilibrium bounce | Keep the §6.2 line sharp; do not soften toward a bounce |
| II.4 | `α_LIV = 0 exactly` (frontier #8) | GEOMETRIC | OVER-REACH; correct at LO, INFO at higher order (own NNLO caveat) | Tighten to "= 0 at LO; higher-order PRELIMINARY" (→ V.4) |
| II.5 | No derived FRW `a(t)`; LQC delivers exactly the effective-Friedmann object the framework owes | GEOMETRIC | GAP correctly stated; LQC contrast absent | Concrete methodology-transfer target: GFT-condensate → effective-Friedmann (→ V.3) |
| IV | §3.2 no-spectral-dimension-flow (`d_s ∼ 8`) = cross-framework contrast with CDT/string | GEOMETRIC | SOLID (S31Aa/S92); needs fair (observable, window) pairing | Validate before a QG referee probes it (→ V.5) |
