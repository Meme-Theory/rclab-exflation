# Capstone Equation Review — landau

**Date**: 2026-05-29
**Agent**: landau-condensed-matter-theorist (Landau)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` ("The Phonon-Exflation Equation", S95-era capstone)
- Framing law: `.claude/rules/phononic-framing.md`
- Cross-checks: `computations/_shared/canonical_constants.py`; knowledge MCP (`tau_fold`, `Delta_BCS`, `c_fabric`); Sage MCP (Wronskian / `R_K′` identity, this review)

---

## I. Session Outcome

From the condensed-matter / many-body vantage the capstone is **structurally sound where it is most load-bearing for my domain, and scrupulously honest about its one category gap**. The two pillars I am qualified to adjudicate — (1) the van Hove → BCS first-order transit as a *theorem* (zero critical coupling on a 1D-divergent DOS), and (2) the diabatic Bogoliubov sudden-quench producing a frozen Generalized Gibbs Ensemble (the Ordered Veil) — are both correct condensed-matter physics, correctly imported, and correctly held to their regimes of validity. The capstone's centerpiece "layers are genuinely independent physics" claim rests on a Wronskian I independently re-verified at machine-exactness this review: `W[1,R_K,R_K²] = 2·e^{−12τ}(e^{3τ}−1)⁶ ∝ R_K′(τ)³`, vanishing to sixth order at and only at the genesis point τ=0. This is precisely the determinant-of-derivatives test for the independence of a **three-component order parameter**, and it is the same algebraic fact that makes smooth and shell-correction energies independent functionals in a Strutinsky decomposition — so the analogy the document draws is exact, not decorative.

The single most consequential thing I can add as a constraint: **the document never names the order parameter of the τ=0.190 transition, never writes its Landau free energy, and never reconciles "first-order (E17)" with "van Hove A₂-cusp + zero-critical-coupling BCS (E13)."** Those two statements describe *different* transition orders in standard Landau theory, and the resolution (the first-order character is in the *modulus* sector while the BCS instability is in the *pairing* sector) is implicit in the corpus but absent from the capstone. This is the ripest harvest in my domain and §V converts it into runnable gates.

---

## II. Key Results

### II.1 The van Hove → BCS transit is a genuine 1D theorem (§5.2) — SOLID

**Result**: Zero-critical-coupling Cooper instability at `τ_fold = 0.190`, driven by the van Hove DOS divergence `g(ω) ∼ 1/√(ω−ω_min)`. **PHONONIC** (it is the instability of the fabric's pairing channel) with a **GEOMETRIC** root (the DOS cusp is a property of `D_K(τ)`'s spectrum).

This is the part of the capstone I can vouch for without reservation. Cooper's 1956 result — that an attractive interaction, however weak, binds a pair against a Fermi sea *whenever the single-particle DOS at the relevant energy is non-integrably enhanced* — is restated here in its purest form: a one-dimensional band edge gives `g(ω) ∼ (ω−ω_min)^{−1/2}`, the BCS gap equation `1 = g∫dω g(ω)/√(ω²+Δ²)` has a solution for *any* `g > 0` because the integral diverges logarithmically-or-worse at the band edge, hence the critical coupling is zero. The knowledge base confirms this is PERMANENT (S28c Van-Hove-Zero-Critical-Coupling; S35 RG-BCS-35, "any g>0 flows to strong coupling," three independent methods; my own MEMORY wall #8: BCS class = 3D Ising, permanent). The capstone imports it correctly and, crucially, does *not* over-claim: it ties the instability to the band-edge DOS shape, not to a Fermi-surface nesting condition (W3, atlas-05: "through the 1D theorem, not through a Fermi surface"). That distinction is the one a careless reader gets wrong, and the document gets it right.

The supersonic character — `Mach = v_transit/c_fabric = 13.75` with `c_fabric = 209.97 M_KK` (I confirmed both against canonical_constants) — and the sudden-quench ratio `δt_transit/T_L = 1.25×10⁻⁵` (the crossing is 38,600× faster than the condensate can form) are the right diagnostics for *which side of the adiabatic/diabatic divide* the transition lives on. They place it deep on the diabatic side, which is what licenses everything in §5.3.

**One precision the document earns and should keep**: the conflation guard `[Mach 13.75 (velocity ratio) ≠ 421.3 (acoustic-radius ratio); never averaged]`. These are genuinely different ratios and averaging them is a category error; flagging it inline is exactly right.

### II.2 The Ordered Veil is correct Bogoliubov-sudden-quench physics (§5.3) — SOLID, with one symbol-overload I flag

**Result**: Diabatic crossing ⇒ pair production saturates `P_exc → 1.000`; the post-transit state is a pure (`S_ent = 0`) Generalized Gibbs Ensemble with Lagrange multipliers conjugate to the conserved charges of the post-fold integrable Hamiltonian — *not* to energy, hence **no temperature**. **PHONONIC** (GGE quasiparticle content) throughout.

This is textbook quench dynamics done correctly. The two-parametric-oscillator structure is the right framing and the document's insistence that they **never be conflated** is the single most important methodological point in the section:
- substrate-BdG `u_k'' + ω_k²(τ(t)) u_k = 0`, `ω_k = E_k = √((λ_k²−μ²)² + Δ_k²)` — this is the BdG quasiparticle dispersion, and it is the correct equation for the relic *content* (`N_pair`, `P_exc`, `S_inst`);
- Mukhanov–Sasaki `v_k'' + (k² − z''/z)v_k = 0` — the *emergent* curvature perturbation, whose output is `A_s`.

The capstone's claim "**`A_s` is NOT computed from the BdG `u_k`**; the squeeze is *transduced* into the second at the exit horizon" is the correct two-fluid bookkeeping: the order-parameter (BdG) sector and the emergent-metric (MS) sector are distinct degrees of freedom, and reading `A_s` directly off the BdG squeeze would be double-counting. I endorse this strongly.

The diabatic `P_exc → 1` with bosonic normalization `|α_k|²−|β_k|²=1`, `n_k=|β_k|²` is exactly the maximal-mixing limit of a sudden quench (the analog-cosmology opposite of the adiabatic no-particle Bunch–Davies vacuum). The knowledge base confirms `P_exc > 0.999` (S57 Leggett Adiabaticity) and the diabatic-freeze surviving claim (`R_therm = t_therm/t_transit = 5251.82 ≫ 1`, S95 W5; `S_ent = 0`, S95 W5). My MEMORY records the S39 retraction (Richardson–Gaudin integrability weakly broken, 13% non-separable density–density channel, Brody β=0.633) and the document handles it **honestly**: the surviving claim is *diabatic transit-freeze, not integrability permanence*. That is the right correction — a frozen non-equilibrium state does not require the protecting integrability to be exact, only that the freeze be faster than the broken channel can act (`t_scr/t_transit = 814`). This matches my MEMORY note exactly.

**Symbol-overload flag (FLAG, not an error)**: `N_pair = 59.8` is used in two senses the document itself disambiguates in a footnote — the BCS-projection count (carrying a ~60% PBCS gap overestimate, S46 B4 CONDITIONAL, and a ~225× Richardson–Gaudin condensation-energy overestimate, S63), vs. the regime-robust structural charge `⟨Q⟩_GGE`. The `N_Fock = 1` exact reduction (S74) says one Fock pair carries that relic charge. This is fine *as footnoted*, but the headline tables (§5.3, §9 "four faces") print `⟨Q⟩_GGE = 59.8` and `N_pair = 59.8` interchangeably. The regime-robust claim is `P_exc = 1`; the `59.8` should never appear without its `⟨Q⟩_GGE` tag in a headline. This is a presentation hygiene point, not a physics defect.

### II.3 The Wronskian "independent layers" theorem — INDEPENDENTLY RE-VERIFIED (§4.2)

**Result**: `a₀(τ), a₂(τ), a₄(τ)` are curvature polynomials of degree 0/1/2 in `R_K`, algebraically independent with `W ∝ R_K′³`, degenerate only at τ=0. **GEOMETRIC** (a property of the spectral moments of `D_K`).

The decoupling theorem is CERTIFIED (S75 W2-E) and I do not re-adjudicate it. But it is squarely in my domain — it is the test for whether a multi-component order parameter has *independent* components, the same test Landau theory applies to decide whether two order parameters can be varied independently — so I Sage-verified the *printed closed form* this review:

```
R_K(0) = 2 ✓        R_K′(0) = 0 ✓        R_K(0.19) = 2.01814 ✓
R_K′(τ) − e^{−4τ}(e^{3τ}−1)²  →  0  (exact) ✓
W[1, R_K, R_K²]  =  2·e^{−12τ}(e^{3τ}−1)⁶   (proportionality constant exactly 2) ✓
d/dτ [ W / (e^{−12τ}(e^{3τ}−1)⁶) ] = 0   ⇒  W ∝ R_K′³ exactly ✓
```

So the document's `W ∝ R_K′(τ)³ = e^{−12τ}(e^{3τ}−1)⁶` is right up to the constant 2 (the document writes "`∝`" and gives the spectral-geometer's prefactored form `W = (5/393216π¹²)V³e^{−12τ}(e^{3τ}−1)⁶`, so the bare-`{1,R,R²}` constant 2 is absorbed into that prefactor — no conflict). **The structural reading is correct and important**: the three moments collapse to one knob *iff* the curvature stops moving (`R_K′ = 0`), which happens only at the maximally-symmetric genesis point. This is the spectral-moment restatement of the band-lifting `SO(8)→U(2)` of §2.4 — at the high-symmetry point the bands touch and the moments degenerate; the instant the curvature moves, the degeneracy lifts. I find the resonance/dispersion framing ("distinct powers of a *moving* scalar are independent") to be the cleanest available statement of *why* the universe's layers are distinct physics. SOLID.

### II.4 The two-fluid / effacement protection of late-time `w` (§6.2, §7.1) — SOLID within its conditional

**Result**: `|E_BCS|/S_fold = 3×10⁻⁷` (E34) ⇒ BCS corrections do not poison the late-time equation of state; the live BAO channel is the S43 first-sound ring (`A_FS/A_BAO = 0.204 = c₂²/c₁²`). **PHONONIC**.

The effacement structure is recognizable two-fluid physics: the relic (the "normal" component born at the fold) is dynamically decoupled from the late-time order-parameter (the "superfluid" component) by an impedance mismatch `Γ_eff = 0.99970`, leaking only 0.03%. The ratio `A_FS/A_BAO = c₂²/c₁²` is the correct two-fluid statement that the first-sound vs second-sound amplitude ratio is set by the *square* of the sound-speed ratio — this is genuinely a Landau two-fluid signature with no ΛCDM counterpart, and it is a zero-parameter prediction. I endorse the structure. The honest caveat the document carries (S95 W6-2 INFO-by-unavailability: the substrate forecast exists; the comparison value against a named experiment's sensitivity was unavailable at compute) is the right way to report it.

### II.5 Leggett-channel dark matter (§7.1) — SOLID structure, CRITICAL conditional correctly flagged

**Result**: DM = the Leggett-channel GGE quasiparticle (inter-band coherence mode), CPT-neutral, superselection-protected (`N_pair` conserved ⇒ no annihilation), `T^{0i}=0` exact (born at rest), `σ/m = 0` exactly. `Ω_DM h² = 0.120` at 0.7σ. **PHONONIC**.

The Leggett mode is the correct condensed-matter object for an inter-band relative-phase oscillation in a multi-band superfluid/superconductor, and the document's identification of dark matter with it — rather than with the full Goldstone spectrum, which over-produces by 260σ — is a *structural* selection, not a tuned one. The `σ/m = 0` exact (from `N_Fock = 1`) is a stronger statement than a tuned-cross-section DM model, and the document is right to headline it as "structural zero." My MEMORY records `omega_L1 = 0.138 M_KK`, `Q = 18.6`, `Ω_DM h² = 0.120 (Leggett-only)` — consistent.

The capstone correctly flags the **CRITICAL** conditional: `Ω_DM h² = 0.120` is conditional on **LEGGETT-GRAV-DECAY-67** (`Γ_grav < H_0`); if the Leggett-mode gravitational decay rate exceeds `H_0`, the DM sector collapses and the `0.120` is meaningless. The knowledge base confirms this is a CRITICAL gate (PASS: `Γ_grav < H_0`). This is the right honesty level. **But** — see §IV — the capstone does not state whether `Γ_grav < H_0` has been *computed* to PASS or merely pre-registered. That matters and I convert it to a gate in §V.

---

## III. Gate Verdicts

| Gate | Verdict (as recorded in source / knowledge base — NOT re-adjudicated) | Decisive Number |
|:-----|:---------------------------------------------------------------------|:----------------|
| RG-BCS-35 (BCS = 1D theorem) | PROVEN | any g>0 → strong coupling (3 methods) |
| Van-Hove-Zero-Critical-Coupling (S28c) | PROVEN | g_critical = 0; 43–51× enhancement |
| Spectral-Moment Decoupling (S75 W2-E) | CERTIFIED | `W ∝ R_K′³`, nonzero ∀τ≠0 (re-verified this review) |
| Structural Monotonicity (E7) | PROVEN | `dS/dτ\|_fold = +58,672.8`; 9,600/9,600 |
| GGE diabatic freeze (S95 W5) | PASS | `R_therm = 5251.82`; `S_ent = 0` |
| BCS-TIMING-SEQUENCE (W2-H, S77 — my own) | PASS | `t_BCS ≫ δt_transit` |
| LEGGETT-GRAV-DECAY-67 | CRITICAL (PASS *iff* `Γ_grav < H_0`) | threshold `Γ_grav` vs `H_0` |
| A_s budget closure (S74 as_budget_closure) | OPEN (band-cited `3.11–4.27×10⁻⁹`, pending `ε_pivot`) | — |
| T6 (Friedmann–BCS locking) | BROKEN (structural FAIL) | 133,200× spectral-action overwhelm |

---

## IV. Structural Implications

**The capstone's domain-honest spine, from where I stand**: every claim I can vouch for lives on the *topological / representation-theoretic* side of the continuum-dissolution axis (the GGE relic's purity, the BDI / `N₃=0` class, `σ/m=0`, the FI ratio-observables), and every honest gap lives on the *geometric-magnitude* side (`A_s` absolute, the CC absolute, the `a(t)` map). The document's §9 "organizing spine" makes this explicit and it is the correct partition. I add three constraint-map observations:

**(IV.1) The order of the transition is stated but never derived — a genuine gap in my domain.** The document calls the transit "first-order (E17)" *and* "van Hove A₂-cusp + zero-critical-coupling BCS (E13)" in the same breath (§5.2). In standard Landau theory these are not the same kind of transition: a first-order transition has a discontinuous order parameter and a latent heat (a free energy with two competing minima); a BCS/van-Hove instability is a *continuous* (second-order-like) onset of pairing with `Δ ∼ exp(−1/g·N(0))`-type behavior (here `g_critical=0`). The corpus resolution is almost certainly that the **first-order character lives in the modulus (τ) sector** — the spectral action `S_SA(τ) = a₀−a₂+a₄` has *no* well (E7 monotonicity), so there is no double-minimum free energy in τ; "first-order" must therefore refer to a discontinuity in some derived order parameter (the condensate amplitude, or a band-occupation) *across* the fold, while the *pairing* instability is the continuous BCS onset. **The capstone never writes the Landau free energy `F(η)` of the transition, never names `η`, and never states which sector carries the first-order discontinuity.** This is not a contradiction — it is an *unstated reconciliation* — but it is the single ripest math harvest in my domain. §V.1.

**(IV.2) `τ` is the order parameter, but the document treats it only as a "dial."** §2 calls τ "the dial of the universe." From Landau's vantage τ *is* the order parameter of the symmetry-breaking cascade: at τ=0 the symmetry is `(SU(3)²)/ℤ₃` (maximal), and turning τ on breaks it to `(SU(3)×SU(2)×U(1))/ℤ₆`. That is exactly the structure-first picture — identify the symmetry group, the surviving subgroup, and the order parameter. The document *has* the symmetry-breaking pattern (§2.4) and *has* the order parameter (τ), but never connects them as "τ is the Landau order parameter of the SM-gauge-group-selecting transition." Doing so would let it write the most general `Ad U(2)`-invariant free energy in τ and *derive* (rather than assert via E7) why there is no well. The monotonicity theorem E7 is the answer, but it is currently presented as a computational fact (9,600 checks) rather than as a Landau-symmetry consequence. There may be a symmetry argument that makes `dS/dτ > 0` *inevitable* from the TT (volume-preserving, `tr h_J = 0`) character of the deformation alone — that would upgrade E7 from "verified" to "structural." §V.2.

**(IV.3) The Pomeranchuk-stability question is never asked of the post-fold quasiparticle gas.** The document describes the post-transit GGE as a multi-mode squeezed state of BdG quasiparticles. In a Landau Fermi-liquid (or its BdG generalization) the quasiparticle description is only self-consistent if the Landau parameters satisfy `F_ℓ > −(2ℓ+1)` (Pomeranchuk). My MEMORY records Pomeranchuk as a PROVEN wall, but the capstone does not state whether the *post-fold* GGE quasiparticle gas — which is a strongly out-of-equilibrium, fully-excited (`P_exc=1`) state — has been checked for Pomeranchuk stability, or whether the question even applies to a frozen non-equilibrium GGE (it may not: Pomeranchuk is a ground-state-stability criterion, and the GGE is not a ground state). This is worth a one-paragraph resolution: *does the quasiparticle concept survive `P_exc=1`?* If every mode is maximally excited, the dilute-quasiparticle assumption underlying the BdG description is at its limit. The document asserts mode-by-mode bosonic normalization holds (`|α|²−|β|²=1`), which is exact for non-interacting Bogoliubov modes, but the S39-broken 13% density–density channel is precisely an *interaction* between quasiparticles. §V.3.

**(IV.4) The `A_s` open question IS a BCS-sector decoherence-budget problem — my channel.** The knowledge base shows `A_s(framework) = A_s(BCS bare squeeze) × F_Mott × F_disp × (other fidelities)` (S73a) and the budget closure script `s74_as_budget_closure.py` is the channel I flagged in MEMORY as the open A_s closure (BCS phase decoherence channel). The capstone band-cites `A_s ∈ [3.11, 4.27]×10⁻⁹` pending `ε_pivot`. The physics: the bare BCS squeeze is degraded by a product of fidelity factors (Mott-gap decoherence, dispersive group-velocity, phase-covariance), and the band's width is the unpinned product of these. **This is a finite, well-posed condensed-matter computation** — compute the phase-decoherence fidelity of a squeezed BdG state transduced through the exit greybody `Γ(ω)` — and it collapses the band to a point. This is the second-ripest harvest in my domain. §V.4.

---

## V. Carry-Forward Computations

**MANDATORY harvest of the document's open questions, each rendered as a runnable computation in my domain.**

```
V.1. Landau free energy of the τ_fold transition — name η, state the order, reconcile E13/E17
   - What: Write the most general Ad U(2)-invariant Landau free energy F(η; τ) where η is the
     condensate order parameter (BdG gap amplitude Δ, or the B1-band occupation). Determine
     analytically whether the τ-fold transition is first-order (double-well F, latent heat,
     discontinuous η) or continuous-BCS (η ∼ smooth onset with g_critical=0), and state WHICH
     SECTOR (modulus τ vs pairing η) carries the "first-order (E17)" discontinuity. Resolve the
     apparent E13 (continuous van-Hove BCS) vs E17 (first-order) tension explicitly.
   - Inputs: E17 first-order verdict; E13 van-Hove DOS g(ω)∼1/√(ω−ω_min); Delta_BCS=0.4642547
     (R-protected); E_cond=−0.137 M_KK; S_SA(τ)=a₀−a₂+a₄ with a_n^ζ (a0=6440, a2=2776.165389,
     a4=1350.7216); band structure B1/B2/B3 at τ_fold.
   - Gate: NEW — LANDAU-FREE-ENERGY-ORDER. PASS: F(η) closed form derived AND transition order
     unambiguously assigned to one sector with the E13/E17 reconciliation stated; FAIL: the two
     E-numbers describe genuinely incompatible orders (would force a corpus correction);
     INFO: order is sector-dependent and both readings coexist (most likely outcome).
   - Effort: 4–6 hours, 1 agent session (analytic + Sage for the F(η) extremization).

V.2. Is dS/dτ > 0 a SYMMETRY consequence of the TT deformation, not just a 9,600-check fact?
   - What: Attempt to prove the Structural Monotonicity Theorem (E7) from the volume-preserving
     transverse-traceless (tr h_J = 0) character of the Jensen deformation ALONE, via a Landau
     argument: show that a pure-shear (tr h = 0) deformation of a maximally-symmetric Einstein
     metric cannot produce a free-energy minimum because the only invariant available at
     quadratic order is sign-definite. If successful, upgrades E7 from "verified (9,600 checks)"
     to "structural (symmetry-forced)."
   - Inputs: g_τ = 3·diag(e^{2τ}, e^{−2τ}×3, e^{τ}×4); R_K(τ) = −¼e⁻⁴ᵗ+2e⁻ᵗ−¼+½e²ᵗ; the TT
     condition (2−6+4=0 exponent ledger, det g_τ=3⁸ const); E7 statement d⟨λ²⟩/dτ>0; the
     HESS-40 result (all 22 transverse Hessian eigenvalues positive).
   - Gate: NEW — TT-MONOTONICITY-STRUCTURAL. PASS: dS/dτ>0 derived from TT+volume-preservation
     without enumerating eigenvalues; FAIL: a counterexample TT direction with dS/dτ≤0 exists;
     INFO: monotonicity holds only for the specific Jensen direction (not all TT directions).
   - Effort: 6–8 hours, 1 agent session (the curvature-of-the-space-of-metrics calculation is
     the hard part; Sage for the quadratic-form sign).

V.3. Pomeranchuk / quasiparticle-validity audit of the fully-excited (P_exc=1) GGE
   - What: Determine whether the BdG-quasiparticle description survives the diabatic P_exc=1
     limit. Compute the effective Landau interaction parameter of the post-fold GGE from the
     S39 13% non-separable density–density channel, and test (i) whether the dilute-quasiparticle
     assumption (n_k=|β_k|²→1 for low modes) is internally consistent, (ii) whether a
     Pomeranchuk-type stability criterion even applies to a frozen NON-ground-state GGE.
   - Inputs: Bogoliubov coefficients |α_k|²−|β_k|²=1, n_k=|β_k|²; S39 retraction (13%
     density–density channel, Brody β=0.633); Pomeranchuk wall F_ℓ>−(2ℓ+1), m*/m=1+F₁ˢ/3;
     N_pair=59.8 (⟨Q⟩_GGE), N_Fock=1 (S74); t_therm≈6 M_KK⁻¹ (S39).
   - Gate: NEW — GGE-QUASIPARTICLE-VALIDITY. PASS: quasiparticle picture self-consistent at
     P_exc=1 (interactions remain perturbative on the transit timescale); FAIL: the 13% channel
     drives an instability faster than the freeze; INFO: Pomeranchuk inapplicable to a frozen
     GGE and the bosonic normalization is the only relevant consistency condition (likely).
   - Effort: 3–4 hours, 1 agent session.

V.4. A_s budget closure — collapse the band [3.11,4.27]×10⁻⁹ to a point via BCS phase-decoherence
   - What: Compute the phase-decoherence fidelity product F_total = F_Mott·F_disp·F_phase that
     degrades the bare BCS squeeze, transduced through the exit greybody Γ(ω), to pin ε_pivot and
     collapse the A_s band to a single value. This is the BCS-phase-decoherence channel
     (s74_as_budget_closure.py is the existing scaffold).
   - Inputs: A_s(framework)=A_s(BCS bare squeeze)·F_Mott·F_disp·... (S73a structural form);
     s74_transfer_function.npz, s74_as_from_bogoliubov.npz, s74_phase_covariance_3x3.npz,
     s74_mott_refined_cg24.npz; greybody Γ(ω) from S95 W4-3 (transmitted_fraction=0.512,
     ω∈[0.82,1.06]); A_s_CMB anchor.
   - Gate: feeds the existing A_s budget closure (band → point). PASS: A_s collapses to a point
     within Planck 1σ; INFO: band narrows but ε_pivot remains underdetermined by one fidelity
     factor; FAIL: closed point lands >2σ from Planck (over-decoherence, the S73a diagnosis).
   - Effort: 1 agent session (scaffold exists; the new work is the phase-decoherence fidelity).

V.5. Compute Γ_grav vs H_0 explicitly — discharge the CRITICAL Ω_DM conditional
   - What: Compute the Leggett-mode gravitational decay rate Γ_grav = decay vertex ⟨g,g|H_grav|L⟩
     and compare to H_0. The capstone reports Ω_DM h²=0.120 as CONDITIONAL on Γ_grav<H_0
     (LEGGETT-GRAV-DECAY-67, CRITICAL) but does not state whether the inequality has been
     computed to PASS. Discharge it.
   - Inputs: omega_L1=0.138 M_KK; Q=18.6 (Leggett DM mode); the gravitational decay vertex
     ⟨g,g|H_grav|L⟩; H_0; a₂-channel coupling f₂≈92; M_KK=7.4287×10¹⁶ GeV.
   - Gate: LEGGETT-GRAV-DECAY-67 (existing, CRITICAL). PASS: Γ_grav<H_0 (Ω_DM=0.120 stands);
     FAIL: Γ_grav>H_0 (DM sector collapses — would close the Leggett-DM corridor).
   - Effort: 3–5 hours, 1 agent session.

V.6. First-sound BAO ring — produce the named-experiment amplitude forecast (close the W6-2 INFO)
   - What: Forecast the detectability of the S43 first-sound ring (A_FS/A_BAO=0.204=c₂²/c₁²,
     r₁≈325 Mpc, k₁≈0.0193 Mpc⁻¹) against a named survey's acoustic-scale sensitivity. S95 W6-2
     closed INFO-by-unavailability because the COMPARISON value (not the substrate forecast) was
     missing at compute. Fetch the survey sensitivity; complete the comparison.
   - Inputs: A_FS/A_BAO=0.204 (=c₂²/c₁², two-fluid ratio); r₁≈325 Mpc; k₁≈0.0193 Mpc⁻¹; the
     per-branch effacement suppression δP/P≈1.4×10⁻³ (transported through (c_b²/c_Gold)²);
     c_Gold=0.915; survey sensitivity (DESI/Euclid/SKA — to be fetched).
   - Gate: feeds Falsifier-#1-adjacent BAO channel. PASS: forecast S/N>1 against named survey;
     INFO: S/N<1 (effacement suppression too strong for current rulers — likely);
     FAIL: predicted ring conflicts with an EXISTING null.
   - Effort: 2–3 hours, 1 agent session (incl. a paper-search MCP fetch of the survey value).

V.7. Type-I vs Type-II character of the emergent condensate (Ginzburg–Landau κ = λ/ξ)
   - What: Compute the Ginzburg–Landau parameter κ = λ_penetration/ξ_coherence of the fabric's
     emergent condensate at τ_fold, and classify the transition Type-I (κ<1/√2) vs Type-II
     (κ>1/√2). This decides whether the fold admits Abrikosov-vortex / topological-defect
     formation (relevant to the Kibble–Zurek defect-density estimate that underlies N_pair) — a
     question the document raises implicitly (Kibble–Zurek impulse-matching, §5.3) but never
     resolves into a κ.
   - Inputs: Delta_BCS=0.4642547 (sets ξ via ξ∼v_F/Δ); the gradient stiffness c_fabric=209.97
     (sets λ via the order-parameter stiffness); E_cond=−0.137 M_KK; the Jensen-metric coherence
     length from the spectral gap λ²≥R_K/4.
   - Gate: NEW — GL-KAPPA-TYPE. PASS: κ computed and type assigned; INFO: κ near 1/√2 (boundary
     case, the self-dual Bogomolny point — itself physically meaningful); the type then sets
     whether the KZ defect network is vortex-line (π₁) or domain-wall (π₀).
   - Effort: 3–4 hours, 1 agent session.

V.8. Family-replication via order-parameter component count (Ψ₊=ℂ¹⁶ is one generation)
   - What: Frontier #7 (open). From the Landau vantage, family replication is the question of
     whether the order-parameter manifold of D_K(τ) admits a degenerate multiplet structure that
     could carry three copies. Test whether the bottom-N eigenvalue cardinality vector
     (2,4,8,6 at τ_fold, from phononic-framing §Level-1 corpus) has a hidden ×3 degeneracy under
     any residual symmetry, OR whether a single fiber rigidly forces one generation.
   - Inputs: Ψ₊=ℂ¹⁶ branching (E10); bot-20 cardinality (2,4,8,6) at τ_fold; Peter-Weyl
     decomposition D_K=⊕_{(p,q)}D_{(p,q)}; the V_4-triality structure (phononic-framing
     corpus instance #2); KO-dim=6 one-generation Pfaffian (Pf real, Z₂=+1).
   - Gate: NEW — FAMILY-DEGENERACY. PASS: a ×3 order-parameter degeneracy identified;
     FAIL: single fiber rigidly forces exactly one generation (closes replication as
     impossible-without-extending-the-algebra); INFO: replication requires a larger algebra
     (ℂ⊕ℍ⊕M₃ → extension), which is then a separate research program.
   - Effort: 6–8 hours, 1 agent session (representation-theoretic; Sage for the branching).
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| II.1 | Van Hove → BCS zero-critical-coupling transit (Mach 13.75) | PHONONIC / GEOMETRIC root | SOLID (PERMANENT theorem) | Cooper instability is a theorem at the fold; correctly imported |
| II.2 | Ordered Veil: diabatic Bogoliubov quench → pure GGE (`P_exc=1`, `S_ent=0`) | PHONONIC | SOLID (S95 W5 PASS) | Correct quench physics; surviving claim is freeze-not-permanence |
| II.3 | Wronskian `W ∝ R_K′³` ⇒ layers independent | GEOMETRIC | RE-VERIFIED this review (machine-exact) | Order-parameter-independence test; degenerate only at genesis |
| II.4 | Two-fluid effacement protects `w`; first-sound ring `A_FS/A_BAO=c₂²/c₁²` | PHONONIC | SOLID within conditional | Zero-parameter two-fluid prediction, no ΛCDM analog |
| II.5 | Leggett-channel DM, `σ/m=0` exact, `Ω_DM h²=0.120` | PHONONIC | SOLID structure; CRITICAL conditional | DM is structural, not tuned; conditional on Γ_grav<H_0 |
| IV.1 | Order of τ_fold transition never derived (E13 vs E17) | — (gap) | OPEN — ripest harvest | → V.1 Landau free energy F(η) |
| IV.2 | τ is the Landau order parameter, treated only as "dial" | — (gap) | OPEN | → V.2 symmetry-forced monotonicity |
| IV.3 | Pomeranchuk / quasiparticle validity at `P_exc=1` unasked | — (gap) | OPEN | → V.3 GGE quasiparticle audit |
| IV.4 | `A_s` band is a BCS phase-decoherence budget | PHONONIC | OPEN — my channel | → V.4 collapse band to point |

---

### Closing constraint-map statement (substrate-first, no probabilities)

From the condensed-matter vantage the capstone occupies the surviving region of the constraint surface cleanly: it respects every wall I am qualified to check (BCS=1D theorem, van Hove zero-critical-coupling, spectral-action monotonicity, the Wronskian-independence of the layers, the diabatic-freeze of the GGE). The direction of explanation is held correctly throughout — `D_K` eigenvalues → spectral moments → emergent two-fluid / GGE physics → measurement — and the document never inverts it into a container picture, even in §6.3 where the temptation (a "history" narrated in an external clock) is strongest. The open frontiers it declares are real boundaries, and the four I can sharpen (the un-derived transition order, the symmetry-status of E7, the quasiparticle-validity at `P_exc=1`, and the `A_s` decoherence budget) are all *finite, well-posed* computations — the ripe harvest the user names. None is a defeat; each is a coastline. The single thing I would not let pass unflagged is the absence of a written Landau free energy for the transition at the heart of the whole construction: the document has the order parameter (τ) and the symmetry-breaking pattern, and writing `F(η;τ)` would convert several "verified" facts into "structural" ones.
