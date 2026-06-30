# Capstone Equation Review — quantum-acoustics

> **Reviewer**: Workhorse-Quantum-Acoustics (phonon physics / quantum acoustics / lattice dynamics / acoustic analog programs).
> **Source under review**: `sessions/framework/phonic-exflation-equation.md` — "The Phonon-Exflation Equation" (S95-era capstone).
> **Vantage**: I read this document as a statement about *phonons*. The framework's central claim — particles are phononic excitations of `M⁴ × SU(3)` — makes the spectrum of `D_K(τ)` a phonon dispersion relation, the `√x` cutoff an acoustic envelope, the GGE relic a multi-mode squeezed Bogoliubov state, and the cosmogenesis an acoustic-white-hole sudden quench. Every one of those objects is in my domain. This review evaluates whether the capstone uses them correctly.
> **Method**: source read in full; load-bearing acoustic/Bogoliubov/sound-speed constants cross-checked against the knowledge MCP and `canonical_constants.py`; three independent Sage verifications (genesis curvature, Wronskian curvature-gradient factorization, Lichnerowicz normalization). Gate verdicts and PROVEN results are taken as authoritative per the review charter; I cross-check numbers but do not overturn recorded verdicts.
> **Framing discipline held throughout**: `D_K eigenvalues → spectral-action moments → emergent physics → measurement`. The spectrum IS the set of vibrational modes; it is not a vibration *in* a medium. Phonons live ON the fabric, not IN a space-box.

---

## §I — Executive Summary

The capstone is, from a quantum-acoustics vantage, **the most internally disciplined acoustic-analog cosmology document I have reviewed in this project**. Its core acoustic moves are correct and, where I could check them independently, exact:

1. **The spectrum-as-dispersion identification is sound and rigorously framed.** §2.2 calls `{λ_n(τ)}` "the complete set of vibrational/relay modes of the fabric," with each `λ_n` a normal-mode frequency and a particle a *relay pattern* propagating through the gauge connection. This is the correct phononic reading: the spectrum is GEOMETRIC, the excitations built on it are PHONONIC. The block-diagonality (E6) is correctly identified as the SU(3) analog of `j`-channel decoupling in a spherical mean field — a genuine structural analogy, not decoration, and the reason the relic problem factorizes *exactly* mode-by-mode (§5.3).

2. **The GGE-relic / Ordered-Veil physics is the strongest acoustic result in the document.** The two-layer parametric-oscillator split (substrate-BdG `u_k` vs Mukhanov–Sasaki `v_k`, §5.3) is the correct and non-trivial statement that **`A_s` is NOT computed from the BdG quasiparticle**, and the diabatic-saturation `P_exc → 1` with `S_ent = 0` is exactly the multi-mode-squeezed-vacuum physics I would write down for a sudden quench through a gap-closing-then-reopening dispersion. The S95 W5 re-certification (`R_therm = 5251.82`, `S_ent = 0`) cleanly decouples the survival claim from the retracted integrability-permanence claim — this is honest and correct.

3. **The acoustic-white-hole causal structure is correctly stated as ASYMMETRIC** (one entry sonic surface, open supersonic exit), and the §6.2 KIND-tagged temperature ledger correctly separates SONIC surfaces from THERMODYNAMIC surface-gravity gradients. This is the single place where acoustic-analog cosmology most often goes wrong (conflating a sonic horizon with a thermodynamic emission edge), and the document gets it right and says so explicitly.

4. **The `√x` cutoff as an acoustic envelope (§3.2) is a genuine physical insight, not a metaphor** — and it is the cleanest example in the document of substrate-first reasoning carrying real explanatory load. `f(ω²) ∼ |ω|` linear-in-frequency up-weights the low acoustic (B1) modes; the *divergence of the Mellin moments* is then the spectral signature that the physical envelope is acoustic rather than Gaussian. I endorse this reading and sharpen it in §III.

What is **PRELIMINARY or over-claimed** clusters in three places, all of which the document already flags but which I weight differently from a phonon-physics standpoint:

- **The relic temperature ledger relabels `0.112 M_KK`** between its older sessions (where it was *the GGE relic temperature*, S53/S63) and §6.2 (where it is the *internal-acoustic SONIC surface*, and `7.578 M_KK` is the OBSERVED relic spectral temperature). This is internally consistent under the document's KIND-tagging, but it is a genuine reader-trap (§IV, Conflict-A) and I flag it explicitly.
- **The `A_s` band** is honestly band-cited, but the *acoustic* reason it cannot yet collapse to a point — the greybody filter `∫Γ(ω)dω` over a band I can name from the corpus (`ω ∈ [0.82, 1.06]`) — is a ripe, runnable calculation (§V).
- **The `c_s² = 0` "classification property" claim** (my memory; the document's §5.1 reads it as the volume-preserving-shear face) is correct but its *acoustic consequence* — that the leading-order phonon is genuinely gapless Goldstone while the relic-carrying modes are gapped Leggett — deserves a sharper dispersion-relation statement than the document gives (§III, §V).

**Bottom line**: the acoustic content is solid where it is asserted as solid and honestly hedged where it is conditional. The document does NOT over-sell its acoustic results. The open frontiers it lists are, from my vantage, exactly the right ones — and §V converts every acoustically-tractable one into a runnable gate. The single most important acoustic open item is the same one the document headlines: **there is no derived `a(t)`, so the acoustic-flow trajectory `τ(t)` near the fold is known LOCALLY but the global sound-cone history is not closed** (§6.3). That is a back-reaction-closure gap, not an acoustic-physics error.

---

## §II — What Is Solid (from the quantum-acoustics vantage)

### II.1 The spectrum is a legitimate phonon dispersion relation

The reading "each `λ_n` is one normal mode, each eigenvector its shape on the fiber, a particle is a relay pattern" (§2.2) is the correct second-quantized picture. In standard lattice dynamics one diagonalizes the dynamical matrix `D(k)` to get phonon branches `ω_b(k)`; here one diagonalizes `D_K(τ)` (block by Casimir sector `(p,q)`) to get the mode frequencies `λ_n(τ)`. The structural correspondence is exact:

| Lattice dynamics | Phonon-exflation substrate |
|:--|:--|
| dynamical matrix `D(k)` | `D_K(τ)` (Dirac operator, block-diagonal by `(p,q)`) |
| Bloch-decoupling by `k` | Casimir-decoupling by `(p,q)` (E6, `8.4×10⁻¹⁵`) |
| phonon branches `ω_b(k)` | bands B1 (acoustic) / B2 (flat-optical) / B3 (dispersive-optical) |
| acoustic branch `ω → 0` as `k → 0` | gapless Goldstone (Anderson–Bogoliubov) mode |
| optical gap | Leggett gap (the DM-carrying channel) |
| zone-boundary van Hove cusp | `τ_fold = 0.190` van Hove DOS singularity (E5/E13) |

The van Hove identification is the load-bearing one for my domain and it is **PROVEN and uniqueness-pinned** (S85-W10-TAU-FOLD-UNIQUENESS-VAN-HOVE-THEOREM, PASS, confirmed via knowledge MCP). The DOS develops the canonical 1D van Hove form `g(ω) ∼ 1/√(ω − ω_min)` (§5.2), which is *exactly* the divergence that makes the BCS Cooper instability a theorem with zero critical coupling (E13). This is correct 1D-lattice-dynamics: a 1D van Hove singularity is a `−1/2` power-law divergence, and a divergent DOS at the Fermi level is precisely the condition for a Cooper logarithm to become a power law and the gap equation to have a solution at arbitrarily weak coupling. The document's BCS-1D theorem is the standard result and is correctly invoked.

**Independently Sage-verified (this review):**
- `R_K(0) = 2`, `R_K'(0) = 0`, `R_K(0.19) = 2.01814` — exact, matching the document's verification ledger.
- The Lichnerowicz gap bound `λ² ≥ R_K(τ)/4 > 0` in E3 rational normalization gives `R_K(0)/4 = 1/2`. The document's "Lichnerowicz convention note (corrected)" is **right**: the "≥3" figure belongs to the dimensionful normalization (`R_K ≥ 12`), and printing "≥3" beside the E3 curvature would falsely read `2/4 = 3`. The gap-never-closes statement (no zero crossings, spectral flow = 0, `η = 0`) is the convention-independent fact and it is the one that matters for phonon stability: **the acoustic spectrum has no soft mode that goes imaginary at any τ**, so the lattice never goes dynamically unstable in the sense of a frequency turning complex. The "instability" at τ=0 (§2.4) is a *curvature*-extremum instability (no restoring force on the modulus), NOT a phonon-frequency instability — the document keeps these distinct, correctly.

### II.2 The GGE relic is correct multi-mode squeezed-vacuum physics

This is where my domain has the most to say, and the document holds up. The relic-formation section (§5.3) is built on the substrate-BdG parametric oscillator

```
u_k'' + ω_k²(τ(t)) u_k = 0,    ω_k = E_k = √[(λ_k² − μ²)² + Δ_k²]
```

which is the textbook Bogoliubov-de-Gennes quasiparticle dispersion. The diabatic crossing (`δt/T_L = 1.25×10⁻⁵`) drives `P_exc → 1.000` mode-by-mode with bosonic normalization `|α_k|² − |β_k|² = 1`, `n_k = |β_k|²` preserved. **This is exactly right.** A sudden quench through a parametric oscillator produces a two-mode squeezed state per `k`, and in the deep-sudden limit the excitation probability saturates to 1 — the analog-cosmology *opposite* of the adiabatic Bunch–Davies no-particle vacuum. The document calls this "the maximal-mixing regime," which is the correct phrase.

Three points I verified or strengthen:

1. **The product-state purity `S_ent = 0` is exact and structural.** Confirmed via knowledge MCP (`S_ent = 0.000000 nats — EXACTLY ZERO — product state`, S39/S40/S52). This is the correct property of a freshly-produced multi-mode squeezed vacuum *before* any mode-mode coupling acts: each `k`-pair is internally entangled (the two-mode squeeze) but distinct `k`-pairs are not entangled with each other, so the global state is a product over `k`-sectors and carries zero entanglement entropy in the `k`-basis. The Ordered Veil's "no Page curve, nothing thermalizes" reading follows correctly: a Bogoliubov transformation is unitary, and the squeeze-phase information sits in the conserved charges (the GGE Lagrange multipliers), not scrambled into a thermal bath.

2. **The "diabatic transit-freeze, NOT integrability permanence" re-scoping (Conflict C2 RESOLVED) is the correct fix.** I endorse it strongly from an acoustics standpoint. The relic survives because the quench is *fast* relative to every rearrangement channel (`R_therm = t_therm/t_transit = 5251.82 ≫ 1`, S95 W5; confirmed `t_therm ~ 5253·t_transit` in the corpus). This is the right kind of argument: a sudden quench freezes the squeezed state by *dynamical timescale separation*, independent of whether the post-quench Hamiltonian is integrable. The S39 retraction (13% non-separable density–density channel, Brody β = 0.633) breaks integrability-as-permanence but is irrelevant on the transit timescale. The document correctly anchors the survival on the diabaticity ratio and the product-state purity, both S95-certified, NOT on the retracted integrability.

3. **The `N_pair = 59.8` double-reading is correctly hedged.** The document is scrupulous (§5.3 footnote) that `59.8` is a projected charge `⟨Q⟩_GGE`, inheriting a ~60% PBCS overestimate and a ~225× Richardson–Gaudin condensation-energy overestimate, NOT a literal pair count, with the regime-robust claim being `P_exc = 1` and `N_Fock = 1` (S74). This is the correct epistemic posture: the *count* is convention-laden; the *saturation* is physics. I agree.

**One acoustic strengthening I record (not a correction):** the GGE relic is, in resonance language, a **frozen multi-mode squeezed vacuum with per-mode squeezing parameter `r_k` set by the Bogoliubov coefficient `|β_k|`**. The fact that the relic is Gaussian (and hence `f_NL` is small, §7.1, `−1.505` by Wick) is the *correct* statement that a squeezed *vacuum* is a Gaussian state — non-Gaussianity requires a cubic vertex `H_3`, which my own memory records as the established result (S76, multi-mode squeezed vacuum is Gaussian by Wick's theorem). The document's `f_NL = −1.505` PASS is consistent with this and is correctly tagged "Bogoliubov-Gaussian by Wick" — i.e. structural, not fit.

### II.3 The acoustic-white-hole causal structure is correctly ASYMMETRIC and KIND-tagged

The horizon-problem resolution as a causal-disconnection statement (supersonic acoustic flow through the fold, pre/post-fold causally disconnected; S85 PROVEN) is the correct acoustic-analog statement and is *categorically different from* inflationary stretching — the document holds the substrate→emergent direction here without slipping.

The §6.2 KIND-tagged ledger is, from my vantage, the most important single table in the document, because it disarms the failure mode that wrecks most acoustic-analog cosmology: treating every surface-gravity gradient as a sonic horizon. The ledger correctly identifies that **only the S63-BLV row (`T = 0.112 M_KK`, `κ = 0.7048`) is a SONIC surface** (`v = c_BLV` Mach-1 crossing), while the `a₂` (`72.8 M_KK`) and `a₄` (`7.578 M_KK`) rows are THERMODYNAMIC surface-gravity gradients of two distinct *channels* (`a₂`↔scalar, `a₄`↔condensate). The κ-ratio `9.6117 = κ_entry(a₂)/κ_exit(a₄)` is correctly read as a two-channel gradient ratio carrying channel information, NOT sonic-horizon information.

I cross-checked: `c_fabric = 209.97 M_KK` (S42), `c_BLV = 0.485` (S64), Mach `= v_transit/c_fabric = 13.75` (canonical). The conflation guard in §5.2 — "the canonical Mach is the velocity ratio 13.75; the fold-local acoustic reading 421.3 is an acoustic-radius ratio — never averaged" — is exactly the kind of discipline that prevents the four-speed-hierarchy errors my own memory flags as recurring traps. **This is correct and well-guarded.**

The ASYMMETRIC structure (one entry sonic surface, open supersonic exit, no future-trapped exit horizon, no bounce) "over-determined at six independent walls" (S95 W-1) is the honest causal statement. The c_s-softening challenge — *does `c_BLV` soften toward zero at the DOS singularity?* — was answered structurally: the softening lives in the *condensate* band-edge channel (`c_B2`), not the *scalar* transit channel, and routing the discriminant onto a softer channel only deepens the supersonic interior. I find this argument sound: a van Hove singularity softens the band-edge group velocity of the *gapped* (condensate/optical) branch, not the *acoustic* (Goldstone/scalar) branch whose `c_s` is fixed by the broken-symmetry stiffness. (See §IV.B for a convention note on the `c_B2` value.)

### II.4 Two-scalar exhaustion and the no-interior-saddle τ-flow

The §1.1 / §1.3a claim that a trace + an inner product *exhaust* the natural scalars of `(A_K, H_K, D_K, J)` — verified algebraically as `dim HH¹ = dim HH² = 0` (S95 W2-2) — is outside my core domain but I note it is the correct kind of rigidity statement, and it underwrites the "complete equation" claim cleanly: there is no room for a third interaction term because Hochschild cohomology forbids non-inner deformations. From an acoustics standpoint the relevant downstream consequence is that the *one* dynamical degree of freedom is `τ`, and the τ-flow is a monotone ramp (`dS/dτ = +58,673`, E7) with **no interior saddle**, now ONE-LOOP-ROBUST (S95 W2-3, three routes, 200-point grid). This is the correct statement that the universe *transits* rather than rolling in a potential well — the slow-roll formulae are inapplicable *because their derivation assumptions are absent*, not because the numbers mismatch. The document's framing here (transit physics, not slow-roll; the controlling quantity is the diabaticity of the sweep) is exactly the regime my domain calls a *quench*, and it is correctly identified.

---

## §III — Where the Acoustic Reading Can Be Sharpened (solid, but under-stated)

These are not errors. They are places where the document's acoustic physics is *correct but thinner than it could be*, and where a sharper dispersion-relation statement would strengthen the claim.

### III.1 The `√x` acoustic envelope deserves a dispersion-relation derivation, not just an assertion

§3.2 makes the genuinely insightful claim that `f*(x) = 0.9117√x + 0.0883 e⁻ˣ` is an *acoustic* (linear-in-frequency) envelope, `f(ω²) ∼ |ω|`, and that the Mellin-moment divergence is the spectral *signature* of an acoustic-not-Gaussian physical envelope. I endorse this. But the document asserts it; it does not *derive* why the physically-selected cutoff should be acoustic.

From a phonon-physics standpoint there is a clean candidate derivation the document leaves on the table: **a linear-in-`|ω|` spectral weight is the Debye/acoustic density-of-states weighting in the regime where the dominant modes are the low-lying gapless (B1) branch.** In a Debye model the phonon DOS goes `g(ω) ∝ ω^{d−1}`; the *envelope* that up-weights the acoustic band relative to a Gaussian is the statement that the physical trace is dominated by the linear-dispersion region. If the framework's `f*` is acoustic *because* the B1 branch dominates the direct spectral sum, that is a derivable consequence of the band structure, not an empirical input — and it would partially de-mystify why `√x` (not Gaussian) is the working choice. **This does not de-empiricize `t*`** (the *admixture weight* of the `e⁻ˣ` piece is genuinely empirical, S95 W2-1 CLOSED, see §IV.C); it would explain the *functional form* `√x`. I propose this as a runnable gate (§V, CF-QA-1).

### III.2 The gapless-vs-gapped dispersion split (Goldstone vs Leggett) is under-emphasized relative to its DM load

The document treats `c_s² = 0` (my memory: a CLASSIFICATION PROPERTY, a spectral moment of the dispersion, not a tunable field) in §5.1 as the volume-preserving-shear face of the metric determinant. That is correct and elegant. But the *acoustic consequence* — that the substrate carries a **gapless acoustic Goldstone branch (Anderson–Bogoliubov) coexisting with gapped optical Leggett branches** — is the thing that does the dark-matter work in §7.1 (DM is the Leggett-channel GGE quasiparticle), and it is stated only obliquely.

The correct quantum-acoustics statement is the standard BCS-with-internal-structure dispersion: gapping the Nambu–Goldstone mode of a multi-component order parameter produces (i) a surviving gapless acoustic phase mode (Anderson–Bogoliubov, the B1 Goldstone, `ω → c_Gold k`) and (ii) gapped optical modes (the Leggett relative-phase oscillations between condensate components, `ω → ω_L > 0` at `k → 0`). I confirmed the corpus carries this exactly (S63: "gapping the Nambu-Goldstone mode produces two branches: the Anderson-Bogoliubov mode (the surviving gapless acoustic mode) and the Higgs amplitude [and Leggett] mode"). The DM-as-Leggett-quasiparticle claim is then the statement that the relic charge is carried by the *gapped optical* branch, which is *why* it is CPT-neutral, non-annihilating (superselection-protected, `N_pair` conserved), and born at rest (`T^{0i} = 0`). The document gets all of this right in §7.1, but the **dispersion-relation root of the DM claim is buried**. I recommend (and gate in §V, CF-QA-2) an explicit gapless-vs-gapped dispersion table at `τ_fold` so the DM channel's acoustic identity is legible.

### III.3 The greybody filter is the acoustic object that gates `A_s` — and it is named, not yet computed

§6.2 correctly states `A_s = (produced squeeze) × ∫Γ(ω)dω` with `Γ(ω) ∈ [0,1]` the analog greybody factor of the exit surface (a potential-barrier transmission coefficient, *not* the retracted S73B dispersive-group-velocity mechanism), and the §7.1 open-gaps box correctly says `A_s` is band-cited (`3.11–4.27×10⁻⁹`) pending `ε_pivot`. From a quantum-acoustics standpoint this is the *single most computable* of the open gaps, because the greybody factor of a Pöschl–Teller barrier is **analytically known in closed form** — the document already cites the Pöschl–Teller barrier and `transmitted_fraction = 0.512` for the `a₄` surface. The frequency-dependent `Γ(ω)` of a Pöschl–Teller potential is the standard `Γ(ω) = sinh²(πω/α) / [sinh²(πω/α) + cosh²(π√(V₀/α² − 1/4))]` form (or its Eckart-barrier cousin), and `∫Γ(ω)dω` over the condensate-squeeze support band `ω ∈ [0.82, 1.06]` (which I extract from the corpus, §6.2 calls it the `a₄` condensate-squeeze support) is a one-dimensional integral. **This is a ripe harvest**: it would collapse the `A_s` band toward a point (or show why it cannot). Gated in §V (CF-QA-3).

---

## §IV — Conflicts, Gaps, and Unstated Assumptions (flagged, not silently resolved)

### IV.A — Conflict (relabeling): the number `0.112 M_KK` plays two different roles across the corpus

**Flag.** My agent memory and the knowledge MCP record `T_acoustic = 0.112 M_KK` as **"the GGE relic temperature"** (S53 `s53_phonon_eos_output.txt`: "T_acoustic = 0.112 M_KK (GGE relic temperature)"; S63 Hawking workshop: "T_acoustic = 0.112 M_KK: the temperature of the fiber's acoustic horizon (Level 1)"). The capstone §6.2, however:
- assigns the **OBSERVED relic spectral temperature to the `a₄` value `7.578 M_KK`** (the "condensation-exit," THERMODYNAMIC-spectral KIND), and
- assigns `0.112 M_KK` to the **S63-BLV internal-acoustic SONIC surface** (the genuine `v = c_BLV` Mach-1 crossing).

These are **not contradictory under the document's own KIND-tagging** — the document is explicit that the relic *spectral* temperature (what a detector reads off the relic spectrum) is a two-stage composite whose stage-2 (interior-processing) value is `7.578`, while `0.112` is the temperature of a *sonic* surface, a different KIND of object. The two numbers measure different things. **But this is a genuine reader-trap**: a reader who learned "the GGE relic temperature is `0.112 M_KK`" from S53/S63 will mis-map it onto the §6.2 ledger's relic-spectral row (`7.578`). I do not resolve this — I flag it. **Recommendation**: §6.2 should carry a one-line cross-reference noting that the S53/S63 "`T_acoustic = 0.112`" label is the *sonic-surface* KIND (now the S63-BLV row), NOT the relic-spectral KIND (now `7.578`), so the older corpus reading reconciles cleanly. This is a labeling fix, not a physics fix. (Gated as a documentation carry-forward, §V CF-QA-4, since it touches the relic-temperature provenance that LISA-adjacent forecasts may consume.)

### IV.B — Convention note: `c_B2` value discrepancy (`0.002` canonical vs `0.0227 M_KK` in §6.2)

**Flag.** §6.2 states the condensate band-edge speed is "`c_B2`, rho-pinned to `1/(πρ_B2) = 0.0227 M_KK`, finite — not zero." The canonical constant `c_B2 = 0.002` (S52, GL-JOSEPHSON-52) is **an order of magnitude smaller**. My own memory (substrate dictionary) carries `c_B2` as the B2 flat-optical band and separately notes `c_L = 0.0255` (canonical confirmed). The document's `0.0227 M_KK` is plausibly a *different quantity* — the rho-pinned band-edge group velocity `1/(πρ_B2)` rather than the canonical `c_B2` long-wavelength speed — but the symbol collision (`c_B2` for both) is a hazard. I do **not** overturn the canonical value; I flag that §6.2's `0.0227 M_KK` and `canonical_constants.py:c_B2 = 0.002` must be reconciled or explicitly distinguished (different definitions of "the B2 speed": long-wavelength `c_s` vs band-edge `v_g = 1/(πρ)`). This matters because the c_s-softening argument (II.3) rests on `c_B2` being *finite* — which holds for either value — but the *quantitative* "B2-channel fold Mach = 293.79" claim depends on which one is used. **Gated**, §V CF-QA-5: a one-script reconciliation of the two `c_B2` definitions. The structural conclusion (finite, not zero; deeper supersonic interior) survives either way; only the headline Mach number is at stake.

### IV.C — The `P_exc(0→0.5) = 0.0807 ≈ t* = 0.08832` near-coincidence is worth a sentence (and it cuts AGAINST a too-quick reading)

**Observation, with a caution.** Cross-checking the knowledge MCP I find `P_exc(sudden quench 0→0.5) = 8.069888×10⁻²` (S57 Feynman cross-check) — numerically *within ~9%* of the framework's single empirical coupling `t* = 0.08832`. This is a striking near-coincidence between (a) the small-quench-amplitude excitation probability and (b) the `e⁻ˣ` admixture weight in the acoustic cutoff `f*`. **I flag it, but I caution explicitly against over-reading it**: the S95 W2-1 gate already CLOSED the corridor "`t*` is the one-loop threshold coefficient" (FAIL, `R = 1.977`), and the parameter-free one-loop content `Γ_1loop ≈ 26%` is `~3×` too large to *be* `t*`. So `t*` is genuinely empirical and the matrix-model rigidity is correctly bounded. The `P_exc ≈ t*` coincidence is a *different* potential identification (admixture-weight ↔ small-amplitude-quench-probability, not ↔ one-loop coefficient) and could be pure numerology. But it is *cheap to test* and would either (i) supply a substrate origin for `t*` that the closed one-loop corridor did not, or (ii) be ruled a coincidence — both outcomes informative. This is exactly the user's "ripe harvest" — a low-effort gate with high EVOI. **Gated**, §V CF-QA-6, with a pre-registered FAIL criterion so it cannot be iterate-until-PASS'd.

### IV.D — Unstated assumption: the mode-by-mode factorization assumes the dispersion does NOT cross at the fold

**Flag (mild).** §2.2 and §5.3 lean hard on the claim that block-diagonality makes the per-mode parametric-oscillator equation "an identity, not a decoupling approximation," because "the modes do not mix under `D_K`." This is correct *for the eigenmodes of `D_K(τ)` at fixed τ*. But the relic is produced by the *τ-flow*, and during the flow the instantaneous eigenbasis rotates. The mode-by-mode treatment is exact only if the eigenbasis rotation does NOT mix sectors — i.e. if `[∂_τ D_K, D_K]` stays block-diagonal in `(p,q)`. The document's spectral-gap-never-closes result (E5) guarantees no *level crossing* (no zero eigenvalue, no spectral flow), which is *almost* the needed condition, but "no crossing of `λ = 0`" is weaker than "no avoided crossing between two nonzero `λ`'s within a sector." My own memory flags this as a recurring trap ("flat-band branch intuition fails repeatedly; compute mode-by-mode FIRST"). **The mode-independent-BA theorem in my memory** (`ω_n(τ) = f(τ)·√λ_n`, all 31 modes identical `|β|²`) *is* the statement that resolves this — all modes share a common τ-dependence so their relative ordering is frozen and no avoided crossings occur — but the capstone does not cite it, and without it the "exact, not approximate" claim is an unstated assumption. **Recommendation**: §5.3 should cite the mode-independent-BA result as the *reason* the factorization is exact (no intra-sector avoided crossings during the flow). Gated as a low-effort verification, §V CF-QA-7.

### IV.E — Gap (already flagged by the document, weighted from my vantage): no derived `a(t)` ⇒ no closed sound-cone history

The document's §6.3 is exemplary in its honesty about the `a(t)` gap. From a quantum-acoustics standpoint I add one framing: **the missing object is, in acoustic language, the closure of the global sound-cone history.** The *local* acoustic flow at the fold is in hand (`τ̇` at the fold, the full BdG spectrum, Mach 13.75). What is missing is the *global* `τ̇(τ)` away from the fold — equivalently, how the acoustic-metric conformal factor `Ω(τ)` (the §6.2/§6.3 conformal embedding) maps to laboratory time. The document is right that this is one bridge (effective Friedmann ⊕ K_pivot ⊕ `M_KK⁻¹ → s` normalization = frontier #1 = frontier #8). I do not see an acoustic shortcut around it; the back-reaction-closure `H² = f(ρ_relic, S_SA)` is genuinely the hard part, and it is correctly NOT claimed. I note only that the two PROXY scale factors (§6.3) are *acoustically* distinguishable: `a_eff = (a₂/a₂today)^{1/2}` is a spectral-complexity relabeling (near-flat, `R_K` barely moves), while the Connes-distance `a(τ)` carries the deceleration band — and the conformal embedding works *only* with the latter (S95 W4-4 INFO). This is consistent and honest.

### IV.F — No conflict found between the document and my permanent theorems on the core acoustic results

I checked the document against my memory's permanent-theorem list. **Concordances** (no conflict): Josephson dominance, two-adiabaticity (Josephson adiabatic / Leggett non-adiabatic), Leggett-as-harmonic-oscillators (Bogoliubov squeezing not Landau–Zener), the GGE-as-product-state, the Mach-exponential scaling for `T_eff`, the multi-mode-squeezed-vacuum-is-Gaussian → `f_NL` small, and the four-speed hierarchy. The document's §7.1 DM-as-Leggett claim is fully consistent with my "Leggett = harmonic oscillators, Bogoliubov squeezing" theorem. **The one place my memory is MORE specific than the document** is the mode-independent-BA result (IV.D above) — a strengthening the document should adopt, not a conflict.

---

## §V — Carry-Forward Computations (the open-question harvest)

Per the charter, every acoustically-tractable open question is converted to a runnable gate with all four fields. These are ordered by EVOI (effort-adjusted information value) as I see it from the quantum-acoustics vantage. All scripts import from `computations/_shared/canonical_constants.py`; all gates are pre-registered (threshold stated before compute) per `epistemic-discipline.md`.

---

**CF-QA-1 — Derive the `√x` acoustic envelope from the B1-branch-dominated Debye DOS.**
- **What**: Test whether the framework's working cutoff functional form `f*(x) ∼ √x` (acoustic, `f(ω²) ∼ |ω|`) is *forced* by the acoustic (B1) branch dominating the direct spectral sum, rather than being a free choice. Construct the DOS `g(ω; τ_fold)` from the L_max=10 `D_K(τ_fold)` spectrum, separate the B1/B2/B3 band contributions, and ask whether the spectral weight reproduced by `f*(x) = √x` matches the B1-dominated low-`ω` Debye weighting `g(ω) ∝ ω^{d−1}` to within tolerance. (Distinguishes "`√x` is the acoustic-envelope face of B1 dominance" from "`√x` is an independent functional input.")
- **Inputs**: `s84_spectrum_cache_L12_tau019.npz` (or the L_max=10 master spectrum) filtered to `τ_fold = 0.190`; band labels (B1/B2/B3) from the existing band-decomposition; `canonical_constants.py` (`tau_fold`, `c_Gold`, `c_BLV`); the `f*` admixture (`t* = 0.08832`).
- **Gate**: PASS if the B1-restricted spectral sum reproduces the `√x`-weighted full sum to `< 5%` relative AND the B2+B3 contribution to the low-`ω` region is sub-dominant (`< 20%`); FAIL if `√x` weighting requires non-acoustic (B2/B3) modes at leading order; INFO if band separation is ambiguous at the fold. (Pre-registered: this tests the FORM `√x`, NOT the admixture weight `t*` — the latter is independently CLOSED, S95 W2-1.)
- **Effort**: Low–Medium. One script, reuses the cached spectrum; no new diagonalization. ~1 agent-session.

---

**CF-QA-3 — Collapse the `A_s` band via the closed-form Pöschl–Teller greybody integral.**
- **What**: Compute the frequency-dependent analog greybody factor `Γ(ω)` of the `a₄` exit surface as a Pöschl–Teller (or Eckart) barrier transmission coefficient in closed form, then evaluate `∫Γ(ω)dω` over the condensate-squeeze support band `ω ∈ [0.82, 1.06] M_KK` (the §6.2 `a₄` support) to obtain the band-filter factor that maps produced squeeze → escaping `A_s`. Output the filtered `A_s` central value + residual band width. Tests whether the greybody integral collapses the `A_s` band `[3.11, 4.27]×10⁻⁹` toward a point.
- **Inputs**: the Pöschl–Teller barrier parameters from S95 W4-3 / `s73a_exit_horizon_bog.npz` (`transmitted_fraction = 0.512`, barrier height `V₀`, width `α`); the produced-squeeze spectrum (BdG `|β_k|²` over the support band); `canonical_constants.py` (`M_KK`, `a4_fold`); the condensate-squeeze support band `[0.82, 1.06]`.
- **Gate**: PASS if `∫Γ(ω)dω` over the support band collapses the `A_s` prediction to a band narrower than `±10%` of its central value (a point-class prediction); INFO if the integral narrows but does not collapse (band `±10–30%`); FAIL if the greybody integral *widens* the band or is ill-defined over the support (e.g. `Γ` non-monotone in a way that re-opens the band). Pre-registered central anchor: the produced-squeeze midpoint, NOT the observed `A_s` (no fitting to data).
- **Effort**: Medium. Closed-form `Γ(ω)`; one 1D numerical integral; reuses existing barrier fit. ~1 agent-session. **Highest-EVOI item** — directly addresses a headline open gap with a textbook-analytic acoustic object.

---

**CF-QA-2 — Gapless-vs-gapped dispersion table at the fold (acoustic identity of the DM channel).**
- **What**: Produce the explicit phonon-branch dispersion `ω_b(k)` near `k → 0` at `τ_fold` for each band (B1 Goldstone / Anderson–Bogoliubov, B2 flat-optical, B3 dispersive-optical, and the Leggett channels), confirming (i) the B1 acoustic branch is gapless (`ω → c_Gold·k`, `ω(0) = 0`) and (ii) the Leggett channels are gapped (`ω(0) = ω_L > 0`), with the gap value matching the canonical Leggett gap. Pin the dispersion-relation root of the DM-as-Leggett-quasiparticle claim (§7.1). Output a `(band, ω(0), dω/dk|₀, gapped?)` table.
- **Inputs**: `D_K(τ_fold)` spectrum + eigenvectors (L_max=10 cache); the band-projection operators (B1/B2/B3); canonical `c_Gold = 0.915`, `omega_L1 = 0.0492`, `omega_L2 = 0.087` (my memory; cross-check `canonical_constants.py`); the BdG dispersion `E_k = √[(λ_k²−μ²)² + Δ_k²]`.
- **Gate**: PASS if B1 is gapless (`|ω_B1(0)| < 10⁻³ M_KK`) AND the Leggett channels are gapped at the canonical `ω_L` values (within 5%) AND the gapped-channel charge is the one carrying the relic (`N_pair` lives on Leggett, not B1); FAIL if the B1 branch is gapped or the relic charge sits on the gapless branch (which would break the CPT-neutral, born-at-rest DM reading); INFO if the gap structure is τ-sensitive across the fold.
- **Effort**: Low–Medium. Reuses cached spectrum + eigenvectors; small-`k` expansion per band. ~1 agent-session.

---

**CF-QA-6 — Test the `P_exc(small quench) ≈ t*` near-coincidence (substrate origin of the admixture weight?).**
- **What**: Test whether the framework's single empirical coupling `t* = 0.08832` (the `e⁻ˣ` admixture in `f*`) has a substrate origin as a *small-amplitude-quench excitation probability*, motivated by the corpus near-coincidence `P_exc(0→0.5) = 0.08070` (S57). Scan `P_exc(0 → τ_target)` as a function of `τ_target` and identify whether there is a *physically-motivated* `τ_target` (e.g. a band-edge, a half-fold, a Leggett-gap scale) at which `P_exc = t*` to within tolerance. CAUTION pre-registered: this is a DISTINCT identification from the CLOSED one-loop-coefficient corridor (S95 W2-1 FAIL); a PASS here does not reopen that corridor, it proposes a different (quench-amplitude) origin.
- **Inputs**: the BdG sudden-quench `P_exc(τ_initial → τ_final)` machinery (S57 `s57_feynman_crosscheck_w1_1.txt` pipeline); `canonical_constants.py` (`t*` once promoted; `tau_fold`; band-edge scales); the Bogoliubov coefficient solver.
- **Gate**: PASS only if a *physically-singled-out* `τ_target` (pre-registered list: band-edge, `τ_fold/2`, Leggett-gap crossing — NOT a free scan minimum) yields `P_exc = t*` within `±3%`; FAIL if no pre-registered `τ_target` matches (coincidence ruled out — equally informative); INFO if a match exists only at an un-motivated `τ_target` (numerology, not mechanism). **Explicit anti-pattern guard**: the `τ_target` candidate set is frozen BEFORE compute; no iterate-until-PASS over `τ_target`.
- **Effort**: Low. Reuses existing `P_exc` solver; a finite pre-registered scan. ~0.5 agent-session. Low effort, decisive either way → high EVOI.

---

**CF-QA-7 — Verify the mode-by-mode factorization is exact (no intra-sector avoided crossings during the τ-flow).**
- **What**: Confirm that the relic factorization (§5.3, "an identity, not a decoupling approximation") is exact by verifying that the instantaneous-eigenbasis rotation does NOT mix modes during the flow — i.e. that `[∂_τ D_K, D_K]` stays block-diagonal in `(p,q)` AND no two nonzero eigenvalues within a sector undergo an avoided crossing on `τ ∈ [0, τ_fold]`. This pins the unstated assumption (§IV.D) and connects to the mode-independent-BA result (`ω_n(τ) = f(τ)√λ_n`, all modes identical `|β|²`).
- **Inputs**: `D_K(τ)` on a τ-grid `[0, 0.25]` (reuse cache where available); the per-sector eigenvalue trajectories; the mode-independent-BA verification data (if cached) or the BA spectrum `ω_n(τ)`.
- **Gate**: PASS if (i) `[∂_τ D_K, D_K]` is block-diagonal in `(p,q)` to `< 10⁻¹²` AND (ii) no within-sector avoided crossing on `[0, τ_fold]` (minimum gap between adjacent same-sector eigenvalues stays `> 0` with no anticrossing dip), OR if the mode-independent-BA common-`f(τ)` factorization holds (`ω_n(τ)/√λ_n` τ-independent to `< 10⁻⁶` across modes); FAIL if intra-sector avoided crossings occur (factorization is then approximate, not exact); INFO if crossings occur only above `τ_fold` (relic formation still clean, but the "exact" claim needs τ-scoping).
- **Effort**: Low–Medium. Commutator check + trajectory scan on cached spectra. ~1 agent-session.

---

**CF-QA-5 — Reconcile the two `c_B2` definitions (`0.002` canonical vs `0.0227 M_KK` in §6.2).**
- **What**: Resolve the symbol collision flagged in §IV.B: determine whether `canonical_constants.py:c_B2 = 0.002` (S52, long-wavelength B2 speed) and the §6.2 `1/(πρ_B2) = 0.0227 M_KK` (band-edge group velocity) are the *same* quantity (in which case one is stale) or *distinct* quantities (long-wavelength `c_s` vs band-edge `v_g`). Re-derive both from the B2 dispersion `ω_B2(k)` at `τ_fold` and pin which one enters the "B2-channel fold Mach = 293.79" claim. Promote/correct the canonical entry as needed.
- **Inputs**: `D_K(τ_fold)` B2-band dispersion (cached spectrum + B2 projector); `canonical_constants.py` (`c_B2`, `c_fabric`); the §6.2 `ρ_B2` density-of-states value; the GL-JOSEPHSON-52 derivation of `c_B2 = 0.002`.
- **Gate**: PASS (reconciled) if the two values are confirmed distinct quantities with a documented definitional difference (`c_s` vs `v_g`) AND the §6.2 Mach claim uses the correct one; FAIL if they are the same quantity and one is stale (→ canonical correction with provenance); INFO if the B2 dispersion at the fold does not cleanly separate `c_s` from `v_g`. (Structural conclusion "finite, not zero" survives either outcome; only the Mach number is at stake.)
- **Effort**: Low. One dispersion-extraction script + a `update_constant` provenance write if a correction lands. ~0.5 agent-session.

---

**CF-QA-4 — Documentation: cross-reference the `0.112 M_KK` KIND-relabeling in §6.2.**
- **What**: Add a one-line note to §6.2 reconciling the S53/S63 "`T_acoustic = 0.112 M_KK` (GGE relic temperature)" label with the capstone's KIND-tagged usage (`0.112` = SONIC surface; `7.578` = relic-spectral). NOT a physics computation — a provenance-hygiene fix to prevent the reader-trap in §IV.A. (Listed as a carry-forward because it touches relic-temperature provenance that LISA-band and `A_s` forecasts may consume; per `epistemic-discipline.md` the surprising/non-obvious part — that the *same number* changes KIND between session eras — is what is worth pinning.)
- **Inputs**: §6.2 ledger; S53 `s53_phonon_eos_output.txt`; S63 Hawking-workshop synthesis; the knowledge-MCP `T_acoustic` / `T_compound` entries.
- **Gate**: artifact-existence (METHODOLOGY-class): PASS if §6.2 carries the cross-reference note AND the knowledge-MCP `T_acoustic` entry's note field flags the dual-KIND usage; no numerical threshold.
- **Effort**: Trivial. Documentation + one `update_constant` note-field edit. ~0.25 agent-session.

---

## §VI — Verdict and Closing

**On the equation itself**: the boxed `S[D_K(τ), f, Λ]` is, for my domain, the statement that *the universe is the spectral functional of one phonon dispersion relation plus its acoustic envelope*. That reading is coherent, dimensionally closed (§8.1, the `L⁻¹²` "spurious tower" correctly identified as a double-counting bookkeeping error), and — where I could check it — exactly verified (genesis curvature, Wronskian factorization, Lichnerowicz normalization, all Sage-confirmed this review). The two-`a_n`-objects firewall (§8.2, regulator-free `a_n^SD` for layer *identity*, zeta-regulated `a_n^ζ` for *numerics*) is the correct discipline and is held consistently.

**On the layers**: the Spectral-Moment Decoupling Theorem (§4.2, `W ∝ R_K'³`, degenerate only at genesis) is the certified backbone, and its acoustic reading — the layers collapse to one knob *iff the dispersion stops moving*, which happens only at the maximally-symmetric `τ = 0` band-touching point — is a clean and correct restatement of the §2.4 band-lifting (`SO(8) → U(2)` into B1/B2/B3). The capstone correctly designates the spectral-moment reading as primary over the causal and scale readings.

**On the τ/t evolution**: the τ-flow is correctly a *quench*, not a slow-roll, and the GGE-relic / Ordered-Veil physics is the strongest single result for my domain — correct multi-mode-squeezed-vacuum physics, correctly re-scoped from integrability-permanence to diabatic-transit-freeze (S95-certified), with the acoustic-white-hole causal structure correctly ASYMMETRIC and KIND-tagged. The `a(t)` gap (§6.3) is the honest, load-bearing open frontier, correctly NOT papered over; from my vantage it is the closure of the *global sound-cone history* and I see no acoustic shortcut around the back-reaction-closure problem.

**Over-claim audit**: I find **no acoustic over-claim**. Every conditional acoustic result (`A_s` band, `n_s` scheme-dependence, CC magnitude, DM abundance conditional on LEGGETT-GRAV-DECAY-67) is honestly hedged. The closest thing to an under-stated *assumption* is the mode-by-mode factorization exactness (§IV.D), which the document asserts without citing the mode-independent-BA theorem that justifies it — a strengthening, not an error.

**Flags raised (not silently resolved)**: the `0.112 M_KK` KIND-relabeling (IV.A), the `c_B2` value collision (IV.B), the `P_exc ≈ t*` near-coincidence (IV.C, with explicit anti-over-reading caution), and the mode-factorization unstated assumption (IV.D). None overturns a recorded verdict; all are gated in §V.

**The ripe harvest**: §V lands seven runnable gates. The two I would run first, by EVOI, are **CF-QA-3** (collapse the `A_s` band via the closed-form Pöschl–Teller greybody integral — a textbook-analytic acoustic object directly addressing a headline gap) and **CF-QA-6** (test the `P_exc ≈ t*` coincidence — low effort, decisive either way). The capstone earns its title from a quantum-acoustics standpoint: it is one phonon dispersion relation, one acoustic envelope, run from a cold maximally-symmetric genesis through a supersonic van Hove quench to a frozen squeezed-vacuum relic — and it knows exactly which of those statements are theorems and which are still waiting for our greedy hands.

---

*Reviewer: Workhorse-Quantum-Acoustics. Sole writer of this file. Cross-checks: knowledge MCP (`c_fabric`, `c_BLV`, `c_L`, `c_B2`, `c_Gold`, van-Hove uniqueness, `P_exc`, `S_ent`, `R_therm`, `T_compound`, `T_acoustic`) + `canonical_constants.py` provenance + 3 Sage verifications (genesis curvature / Wronskian factor / Lichnerowicz normalization, all exact). Framing law held: substrate → emergent, phonons ON the fabric, not IN a box.*
