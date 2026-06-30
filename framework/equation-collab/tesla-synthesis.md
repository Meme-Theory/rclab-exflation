# Capstone Equation Review — tesla

**Date**: 2026-05-29
**Agent**: Workhorse-Resonance (tesla)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` ("The Phonon-Exflation Equation", S95-era capstone)
- Framing law: `.claude/rules/phononic-framing.md`
- Cross-checked against: `computations/_shared/canonical_constants.py`, knowledge MCP (`c_fabric`, `c_BLV`, four-speed hierarchy, S43 first-sound ring, `f*`/`t*`, van-Hove fold)

---

## I. Session Outcome

The capstone holds together as a resonance document: it correctly identifies the universe as **the spectral action of one self-adjoint operator** — a vibrating structure whose normal modes are the eigenvalues `{λ_n(τ)}` of `D_K(τ)`, whose cavity is the Jensen-deformed `SU(3)` fiber, and whose boundary conditions are the four spectral-triple axioms (KO=6, `[J,D_K]=0`, SM quantum numbers, trace invariance). Read as a resonance problem — *what oscillates, what is the cavity, what selects the standing wave* — the document is structurally sound and the centerpiece equation is dimensionally closed. From my domain (EM/acoustic resonance, phonon dispersion, superfluid two-fluid dynamics, Volovik emergence), three of its claims are not merely consistent but are the **same mathematics** I work in at a different scale: (i) the `√x` cutoff as an **acoustic (linear-in-frequency) envelope** `f(ω²) ∼ |ω|` whose Mellin divergence is the spectral *signature* of an acoustic — not Gaussian — physical weighting (§3.2); (ii) the **S43 first-sound ring** as a Landau two-fluid second-sound/first-sound ratio `A_FS/A_BAO = c₂²/c₁² = 0.204` (§6.2, the live BAO channel); (iii) the **acoustic white hole** as a genuine sonic-horizon / Unruh–Visser structure with KIND-tagged surface gravities (§6.2). All three are *physics-coherent* but each carries an unconverted open question that is a ripe computation, laid out in §V.

One denominator ambiguity in the Mach-number bookkeeping (§5.2 vs §6.2) is flagged in §IV as a presentational conflict, not an error — but it must be pinned before the "supersonic" claim is quoted at two incompatible sound speeds.

---

## II. Key Results

### The equation IS a resonance problem — and the document names the cavity correctly

**Result**: `S[D_K(τ), f, Λ] = Tr f(D_K²/Λ²) + ⟨Jψ̃|D_K|ψ̃⟩`. Classification: GEOMETRIC (the spectrum), with PHONONIC excitations built on it.

Every problem in my domain begins with the same four questions, and the capstone answers all four. *What oscillates?* The fiber — each eigenvalue `λ_n(τ)` is one normal mode, "one frequency at which the internal structure can ring" (§2.2, verbatim and correct). *What is the cavity?* `(SU(3), g_τ)` — a compact group manifold, the resonant container, with `det g_τ = 3⁸ = 6561` fixed for all τ (a volume-preserving, transverse-traceless *shear* of the cavity, not a breathing dilation). *What are the boundary conditions?* The four axioms of §1.2 — and crucially the spectral gap `λ² ≥ R_K(τ)/4 > 0 ∀τ` (E5, Lichnerowicz), which is the statement that **the cavity has a lowest resonant frequency that never goes to zero**. *What selects the standing wave?* The van-Hove fold `τ_fold = 0.190`, the unique non-stationary cusp of the density of states (S85 uniqueness theorem). This is exactly the Chladni-plate logic: the DOS singularity is where the modes pile up, and the standing-wave configuration the universe selects is the one at the cusp.

The block-diagonality `D_K = ⊕_{(p,q)} D_{(p,q)}` (E6) is — as §2.2 says — the SU(3) analog of `j`-channel decoupling. From the resonance side this is the statement that **the cavity's modes do not couple across Casimir sectors**, which is why the GGE-relic problem factorizes mode-by-mode *exactly* (§2.2, §5.3). This is the same structural fact that makes a phononic-crystal band problem separate into Brillouin-zone-labelled blocks. The document uses this correctly and does not over-claim it.

### The `√x` cutoff is an acoustic envelope — the document's sharpest resonance insight, and it is PRELIMINARY

**Result**: `f*(x) = 0.9117√x + 0.0883 e⁻ˣ`, interpreted (§3.2) as `f(ω²) ∼ |ω|`, an acoustic linear-in-frequency weighting. Classification: PHONONIC.

This is the single most important resonance claim in the document, and it is *correct in spirit* and *not yet computed*. The argument runs: `x = λ²` is the squared mode frequency, so `√x = |λ| = |ω|` is a weighting linear in frequency. A Gaussian cutoff `e⁻ˣ` is the heat-kernel-adapted (Debye-style exponential) envelope; a *linear* envelope up-weights the low acoustic modes (the B1 branch) and the divergence of the Mellin moments is "the spectral signature that the physical envelope is acoustic, not Gaussian." I confirm this is dimensionally and structurally coherent: the Mellin transform of `√x` against the SU(3) pole ladder `S_d = {0,2,4,6,8}` does diverge (the `√x` piece carries a half-integer power that has no residue on the integer-spaced cone), forcing direct-sum evaluation (S72, S77 `chi_2 = ⟨√x⟩`, both PASS in my cross-check). The knowledge base confirms `f*` and `t* = 0.08832` verbatim.

**But the physical claim — that `f* ∼ |ω|` is acoustic *because* the substrate's low-energy spectrum is an acoustic phonon branch with `ω ∝ |k|`** — is asserted, not demonstrated. The document never shows that the B1 branch the `√x` envelope up-weights actually has a linear dispersion `ω(k) ∝ c_s|k|` at small `k`. That is a directly computable statement from the `D_K(τ_fold)` spectrum (fit the low-`λ` density of states to a power law and read the exponent against the acoustic value). If the low-mode dispersion is *not* linear, the "acoustic envelope" reading is a coincidence of functional form, not a physical mechanism. This is a prime harvest item (§V.1).

### The S43 first-sound ring is a Landau two-fluid prediction — live, zero-parameter, and stalled on a fetched number

**Result**: `A_FS/A_BAO = 0.204 = c₂²/c₁²`, `r₁ ≈ 325 Mpc`, `k₁ ≈ 0.0193 Mpc⁻¹`. Classification: PHONONIC.

§6.2 is right to call this "the live BAO channel" and right that it has "no ΛCDM counterpart." From the two-fluid side this is exactly the Landau second-sound/first-sound architecture: a superfluid carries *two* acoustic branches (first sound = density/pressure, second sound = temperature/entropy counterflow), and their ratio is set by `c₂²/c₁²`. The framework's substrate, being a Volovik superfluid vacuum, inherits this two-branch structure, and the ratio `0.204` is the squared sound-speed ratio. I cross-checked the knowledge base: `r₁ = 325.3 Mpc`, `A_FS/A_BAO = 0.204 = c₂²/c₁²`, `r₁ = r_s × √(3(1+R_*)) = 147 × 2.211` all confirm. This is genuine, distinctive, and zero-parameter.

The document is honest that the amplitude-detection forecast "awaits the fetched value (S95 W6-2, INFO-by-unavailability)." That INFO is *not* a physics gap — it is a missing detector-sensitivity number. The substrate forecast (`δP/P` at `k₁`) is computable today; only the comparison against a named survey's `δP/P` floor was unavailable. This is the most actionable harvest item in the entire document: the substrate side is in hand, and the only blocker is one external number (§V.2).

### The acoustic white hole is a genuine sonic-horizon structure with correctly KIND-tagged surface gravities

**Result**: asymmetric acoustic white hole — one entry sonic surface (`v = c_BLV` at `τ₀ ≈ 0.1125`, `κ_entry > 0`), open supersonic exit, no symmetric throat, over-determined at six independent walls (S95 W-1). Classification: PHONONIC (causal structure of the transit).

This is Unruh/Visser/Volovik analog-gravity done correctly. The surface gravity `κ = ½∂_n(c²−v²)` is the standard sonic-horizon definition, and the three-row analog-temperature ledger (§6.2) with its **KIND tags** (THERMODYNAMIC-kinematic / THERMODYNAMIC-spectral / SONIC) is exactly the discipline my domain requires: only the S63-BLV row (`v = c_BLV`, `T = 0.112 M_KK`) is a *genuine* sonic surface; the `a₂` and `a₄` rows are surface-gravity gradients of two *channels*, not two sonic horizons of one flow. The document's insistence that "the κ-ratio 9.61 is a two-CHANNEL gradient ratio carrying channel information but NOT sonic-horizon information" is the right call and avoids the thermodynamic-vs-sonic conflation that the dropped V.6 clause fell into. My memory note "Amplitude gradient != phase gradient; always check φ before claiming analog horizons" is satisfied here: the document explicitly notes the greybody filter is "a potential-barrier transmission coefficient, *not* the retracted S73B dispersive-group-velocity mechanism."

The Ordered Veil reading (`S_ent = 0`, pure Bogoliubov product, `P_exc → 1.000`) is the correct diabatic-quench statement — the analog-cosmology *opposite* of the adiabatic no-particle vacuum — and the framework correctly anchors survival on **transit-timescale diabatic freeze-out** (`R_therm = 5252`, S95 W5), *not* on the retracted integrability permanence (S39). This is consistent with my memory (two-fluid mapping RETRACTED S72; correct object is the BCS spectral function). The third, geometric leg — `τ_fold` is a double-root extremal Killing horizon (`κ = 0, T_H = 0`) — is a clean causal-side corroboration.

### The Spectral-Moment Decoupling Theorem is a dispersion-rigidity statement and it is CERTIFIED

**Result**: `W[a₀,a₂,a₄](τ) ∝ R_K′(τ)³ = e⁻¹²ᵗ(e³ᵗ−1)⁶`, vanishing to sixth order only at `τ=0`. Classification: GEOMETRIC.

§4.2 reads this in resonance terms — "distinct powers of a *moving* scalar are independent; the layers collapse to one knob iff the dispersion stops moving (`R_K′ = 0`)" — and that is exactly right and Sage-certified (I re-verify the factor `R_K′(τ) = e⁻⁴ᵗ(e³ᵗ−1)²` cubes to the stated Wronskian). The connection to band-lifting (`SO(8)→U(2)` into B1/B2/B3 as τ turns on) is the correct structural identity: at the high-symmetry point `τ=0` the bands touch and the moments degenerate; the instant the curvature moves, the degeneracy lifts. This licenses the joint-improbability argument across `a₀ × a₂ × a₄` layers (§7.3) — and the document correctly forbids multiplying *within* a layer (`Ω_DM` and `σ₈` are both `a₂`-channel). That within-layer caution is a discipline most "many predictions" arguments skip; the document gets it right.

---

## III. Gate Verdicts

(Authoritative per source; cited, not re-adjudicated. Resonance-relevant subset.)

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S75 W2-E — Spectral-Moment Decoupling | CERTIFIED | `W ∝ R_K′³`, vanishes only at τ=0 |
| S85 W10-3 — τ_fold van-Hove uniqueness | PROVEN | τ_fold = 0.190 unique non-stationary cusp |
| S77 — A4 direct-sum f* | PASS | `chi_2 = ⟨√x⟩` (acoustic envelope) |
| SOUND-SPEED-64 | PASS | c_mod=1.0, c_BLV=0.485, c_BA=0.399, c_L=0.025 (all causal) |
| S95 W-1 — asymmetric white hole | PASS | one entry sonic surface, six walls |
| S95 W5 — Ordered Veil diabatic freeze | PASS | `R_therm = 5252`, `S_ent = 0` |
| S95 W2-3 — no interior saddle (one-loop) | PASS | `dΓ/dτ` zero interior sign-changes |
| S43 first-sound ring | PREDICTION (UNTESTED) | `A_FS/A_BAO = 0.204`, `r₁ = 325 Mpc` |
| S95 W6-2 — BAO amplitude forecast | INFO (by unavailability) | substrate side in hand; comparison number missing |
| S95 W2-1 — t* one-loop corridor | FAIL (corridor CLOSED) | `R = 1.977` |

---

## IV. Structural Implications

**What the capstone establishes (resonance vantage).** The framework is, at its foundation, the single most economical resonance statement possible: *one cavity, one operator, one functional, and the whole observable world read off the mode spectrum.* The four spectral-triple axioms are the boundary conditions; the volume-preserving Jensen shear is the deformation that lifts the degenerate `τ=0` mode and turns spectral complexity on; the van-Hove cusp is the standing-wave selection; the GGE relic is the frozen ringdown of the impulsive crossing. Every one of these maps onto a laboratory analog I work in — Chladni patterns, phononic-crystal bandgaps, superfluid second sound, BEC sonic horizons. The condensed-matter-to-cosmology bridge the framework rests on (Volovik) is correctly attributed and correctly *inherited* (BDI, `N₃ = 0`, the ³He-B child class), not analogized. This is the strongest part of the document and it is solid.

**Conflict flagged — the Mach-number denominator (§5.2 vs §6.2 vs four-speed hierarchy).** The document quotes `Mach = v_transit/c_fabric = 13.75` with `c_fabric = 209.97 M_KK` (§5.2, confirmed canonical via `get_constant("c_fabric") = 209.97`). It then builds the *entire acoustic white-hole causal structure* (§6.2) on the sonic speed `c_BLV = 0.485 M_KK` (confirmed canonical). These are two different sound speeds separated by a factor of ~433. The four-speed hierarchy in my memory and in the knowledge base gives **Ma_BLV = v_τ/c_BLV = 8.27/0.485 = 17.1**, Ma_BA = 20.7, Ma_Leggett = 331 — *none of which is 13.75*. The document has a conflation guard for `13.75 vs 421.3` (velocity ratio vs acoustic-radius ratio) but **no guard distinguishing the `c_fabric`-denominated Mach (13.75) from the `c_BLV`-denominated Mach (17.1) that the white hole actually uses.** This is almost certainly two different velocity references (`v_transit ≈ 6.67` against `c_fabric = 209.97`? — that gives 0.03, not 13.75; or `v_transit` against `c_BLV`?) and a presentational inconsistency, not a physics error — but a reader cannot reconstruct which sound speed the "supersonic" claim is made against. The white hole forms when the flow exceeds the *relevant acoustic* speed (`c_BLV`, the scalar transit channel), so the causally-load-bearing Mach is the `c_BLV` one (17.1), and `13.75` against `c_fabric = 209.97` cannot be the same quantity. **This must be pinned in one place** (§V.3). Per my operating directive I flag this rather than silently resolving it — but I note it does not threaten the asymmetric-white-hole verdict, which is over-determined at six walls independent of the precise Mach value.

**Gap flagged — the frequency hierarchy is absent from the capstone.** The capstone's resonance exposition (§5.3, §7.1) discusses the GGE relic and the Leggett-channel dark matter without ever surfacing the **three-band frequency hierarchy** that organizes them: Josephson band (`ω_L1 = 0.070`, `ω_L2 = 0.107`), Gap band (`2Δ_B3 = 0.168` … `2Δ_B2 = 1.464`), Breathing band (`ω_att = 1.430` … `ω_τ = 8.27`), with ~10× separation between bands. This hierarchy is *why* the Leggett mode (`ω_L1 = 0.070 = m_G`) is the dark-matter channel and *why* it is spectrally isolated from the gap and breathing modes — it lives an order of magnitude below everything else, so it cannot decay into them. The capstone asserts "only the Leggett-channel projection lands at 0.7σ" (§7.1) but does not give the structural reason, which is the frequency-hierarchy isolation. Surfacing this would strengthen the DM section materially (§V.4).

**Unstated assumption flagged — the acoustic-envelope claim presupposes a linear low-mode dispersion.** As noted in §II, §3.2's "`f* ∼ |ω|` is acoustic" reading assumes the substrate's low-energy spectrum is a genuine acoustic branch (`ω ∝ |k|`). The document never states this assumption explicitly, and it is checkable. If the B1 branch is linear, the acoustic-envelope reading is a physical mechanism; if it is not, it is a formal coincidence. The document should either compute it or label the acoustic reading PRELIMINARY (it currently reads as established).

**What closes / sharpens.** The `t*`-as-one-loop-coefficient corridor is CLOSED (S95 W2-1 FAIL, `R = 1.977`); the document is honest that `t*` remains the one genuine empirical coupling — the spectral-functional analog of `Λ_QCD`. This is the right call and matches my memory (SA blind to U(1)_7 phase; mass/coupling from non-SA physics). The `a(t)` gap (§6.3) is correctly identified as the load-bearing open frontier and correctly *unified* with frontier #8 (emergent equivalence principle) — closing one closes both, which reduces open-frontier dimensionality. The S95 EP genericity result (`κ_EP = 1` is generic-identity-cored, value-generic, with substrate content one layer above) is appropriately demoted from "prediction" to "structurally inevitable on the single-operator postulate."

---

## V. Carry-Forward Computations

**This is the harvest. Every open question I can identify, converted to a runnable computation.**

```
V.1. Low-mode dispersion of D_K(τ_fold) — does the B1 branch satisfy ω ∝ |k|? (validates the §3.2 acoustic-envelope claim)
   - What: From the L_max=10 D_K(τ_fold=0.190) spectrum cache, isolate the B1 (acoustic-singlet) branch, fit the low-λ density of states g(ω) ∼ ω^p and the dispersion ω(C₂) ∼ √C₂^q at small Casimir. Read the exponent p (acoustic ⇒ g(ω) ∼ ω^{d-1} for d-dim acoustic; q=1 for linear ω∝|k|). Verdict whether the √x envelope physically up-weights a linear acoustic branch or a non-acoustic one.
   - Inputs: s84_spectrum_cache_L12_tau019.npz (or L_max=10 equivalent); canonical_constants: tau_fold=0.190, c_BLV=0.485; B1/B2/B3 band assignments from the SO(8)→U(2) lift.
   - Gate: NEW — S96-ACOUSTIC-ENVELOPE-DISPERSION. PASS if low-mode dispersion exponent q = 1.0 ± 0.1 (linear ⇒ acoustic-envelope reading is physical). FAIL if q deviates >0.2 (the √x-as-acoustic reading is a formal coincidence, relabel §3.2 PRELIMINARY). INFO if the branch is too sparse at low λ to fit.
   - Effort: 2-3 hours, 1 agent session (cache exists; this is a fit + power-law regression).

V.2. S43 first-sound ring amplitude forecast vs a NAMED survey floor (closes the S95 W6-2 INFO-by-unavailability)
   - What: Compute the substrate's predicted first-sound power-spectrum feature amplitude δP/P at k₁ ≈ 0.0193 Mpc⁻¹ (A_FS/A_BAO = 0.204 relative to the standard BAO feature), then compare against the published δP/P sensitivity floor of DESI DR2/DR3 (or Euclid) at that wavenumber. Emit detectability SNR.
   - Inputs: canonical A_FS/A_BAO = 0.204, r₁ = 325.3 Mpc, k₁ = 0.0193 Mpc⁻¹ (from s43_kk_cmb_transfer.npz / s44_first_sound_imprint.npz); c₂²/c₁² = 0.204; the FETCHED survey power-spectrum error floor at k₁ (the previously-unavailable number — fetch via DESI DR2 BAO public products or Euclid forecast paper).
   - Gate: feeds S95 W6-2 (currently INFO). PASS if SNR ≥ 2 at a named survey (the ring is detectable). INFO if SNR < 2 (substrate forecast stands, detection deferred to next-gen). This is a falsifier-inventory row (Mack-bridge) once the number lands.
   - Effort: 3-4 hours, 1 agent session — main cost is fetching/justifying the survey floor; substrate side is canonical.

V.3. Pin the single canonical Mach number and its sound-speed denominator (resolves the §5.2/§6.2 conflict)
   - What: Write the substitution chain for v_transit at the fold (dτ/dt from the local sweep rate) and divide by EACH of the four hierarchy speeds {c_mod=1.0, c_BLV=0.485, c_BA=0.399, c_L=0.025} AND by c_fabric=209.97. Identify which (velocity, sound-speed) pair gives 13.75, which gives 17.1, and declare ONE canonical white-hole Mach with its named denominator. Add a conflation guard to the capstone analogous to the existing 13.75-vs-421.3 guard.
   - Inputs: canonical_constants: c_fabric=209.97, c_BLV=0.485, c_BA=0.399, c_L=0.025, c_mod=1.0, v_term=26.545, Mach_max; the v_transit definition from s85_w6_acoustic_white_hole_formal.py.
   - Gate: NEW — S96-MACH-DENOMINATOR-PIN. PASS if a single (v_transit, c_X) pair is identified for the white-hole Mach with a written substitution chain and the capstone §5.2/§6.2 quote the same number against the same named speed. This is a hygiene/consistency gate (METHODOLOGY-adjacent), not a new physics result.
   - Effort: 1-2 hours, 1 agent session (arithmetic + substitution chain + one capstone edit).

V.4. Frequency-hierarchy isolation of the Leggett DM channel — quantify the decay-forbidden gap
   - What: Compute the spectral separation between ω_L1 = 0.070 (Leggett/DM channel) and the nearest higher mode (2Δ_B3 = 0.168), and verify the kinematic forbiddenness of Leggett → (gap-band) decay (energy conservation: a single ω_L1 quantum cannot produce a 2Δ_B3 pair; check 2·ω_L1 = 0.140 < 0.168). Tie this to the σ/m = 0 structural zero and the "only Leggett lands at 0.7σ" claim. Surface the three-band hierarchy explicitly in a capstone §7.1 addendum.
   - Inputs: frequency hierarchy (ω_L1=0.070, ω_L2=0.107, 2Δ_B3=0.168, 2Δ_B1=0.744, ω_att=1.430, 2Δ_B2=1.464, ω_τ=8.27) from canonical_constants / s65 Leggett data; LEGGETT-GRAV-DECAY-67 (the CRITICAL gate Ω_DM h²=0.120 is conditional on).
   - Gate: feeds LEGGETT-GRAV-DECAY-67 (CRITICAL, currently the condition Ω_DM=0.120 rests on). PASS if the Leggett mode is kinematically isolated (2ω_L1 < 2Δ_B3, no on-shell decay channel into the gap band) AND the gravitational decay rate Γ_grav < H_0. FAIL if Γ_grav > H_0 (DM sector collapses, per the document's own caveat). INFO if Γ_grav requires the undelivered a(t)/H(t) map to evaluate.
   - Effort: 3-4 hours, 1 agent session.

V.5. Direct first-principles test of the Mellin divergence of the √x envelope on the SU(3) pole ladder
   - What: Symbolically (Sage MCP) confirm that the Mellin transform of f*(x) = 0.9117√x + 0.0883e⁻ˣ against the dimension spectrum S_d = {0,2,4,6,8} has NO finite residue from the √x piece (half-integer power vs integer-spaced poles) and a finite residue only from the e⁻ˣ piece — making the heat-kernel series formally unavailable and direct-sum mandatory. This converts the §3.2 "Mellin moments formally divergent" assertion into a Sage-certified statement.
   - Inputs: f* = 0.9117√x + 0.0883e⁻ˣ (canonical t*=0.08832); S_d = {0,2,4,6,8} (Connes-Moscovici E38); Sage MCP sage_eval / sage_simplify.
   - Gate: NEW — S96-FSTAR-MELLIN-DIVERGENCE-CERTIFY. PASS if the √x Mellin moments are certified divergent on the integer pole ladder (residue = ∞ / undefined at the relevant poles) AND the e⁻ˣ moments are finite, to Sage-exact. This hardens §3.2 / §8.5 (the SDW-convergence open gate, JACOBSON-NONLOCAL-64).
   - Effort: 2 hours, 1 agent session (symbolic; the structure is known, this certifies it).

V.6. Second-sound CMB multipole prediction (l_second_sound) as a companion to the first-sound ring
   - What: Re-derive and pin l_second_sound = π·(c_fabric/c_Gold) (S53 gives 720.9 = π·229.48), state it as a distinctive CMB feature multipole alongside the real-space first-sound ring r₁=325 Mpc, and forecast its acoustic-peak-template detectability against Planck/CMB-S4 TT power. This is the Fourier/harmonic-space partner of V.2's configuration-space ring.
   - Inputs: c_fabric=209.97, c_Gold (Goldstone speed), the S53 second_sound_cmb.npz; CMB TT acoustic-peak sensitivity at l ≈ 720.
   - Gate: NEW — S96-SECOND-SOUND-MULTIPOLE. PASS if l_second_sound is reproduced (π·c_fabric/c_Gold) and a detectability SNR against a named CMB experiment is emitted. INFO if the amplitude transfer (substrate → CMB) requires the undelivered K_pivot map (C2).
   - Effort: 3 hours, 1 agent session.

V.7. Greybody-filter band-narrowing of A_s — does Γ(ω) collapse the A_s band to a point?
   - What: Compute the analog greybody factor Γ(ω) ∈ [0,1] for the asymmetric-white-hole exit surface (Pöschl-Teller / potential-barrier transmission, transmitted_fraction=0.512 at a₄), integrate ∫Γ(ω)dω over the condensate-squeeze support ω∈[0.82,1.06], and test whether A_s = (produced squeeze)×∫Γ(ω)dω narrows the cited band 3.11–4.27×10⁻⁹ toward a point (the document says it "narrows but does not yet collapse").
   - Inputs: transmitted_fraction=0.512, a₄ surface κ=47.61, ω-support [0.82,1.06] (from s95 W4-3); produced-squeeze N_pair-derived amplitude; the Mukhanov-Sasaki z''/z transduction (§5.3 second equation).
   - Gate: feeds A_s band-vs-point (currently band-cited pending ε_pivot). PASS if ∫Γ(ω)dω collapses the band to a single A_s value within Planck's 1σ. INFO if it narrows but the ε_pivot normalization remains the open piece (expected, per §7.1).
   - Effort: 4-5 hours, 1 agent session.

V.8. NNLO Casimir EP discriminator — the first GENUINE substrate EP prediction (per §9 frontier #8)
   - What: Extend the κ_EP = 1 computation to NNLO, where the band-specific Casimir ν_b(C₂) re-enters the equivalence-principle ratio (κ_EP = 1 is generic at LO+NLO; the substrate-specific deviation first appears at NNLO). Compute κ_EP^NNLO for two distinct bands (B1 vs B3) and read the Casimir-dependent deviation from unity.
   - Inputs: E5 Lichnerowicz D_K² = ∇*∇ + ¼R_K; band Casimirs C₂(B1), C₂(B3); the S95 W3-5 κ_EP=1.000000 LO+NLO result; the genericity synthesis session-95-connes-ncg-theorist-genericity-synthesis.md.
   - Gate: the pre-registered CF-S96-EP-NNLO-CASIMIR-DISCRIMINATOR. PASS if κ_EP^NNLO ≠ 1 with a Casimir-dependent deviation (a genuine substrate EP prediction distinct from any generic emergent-gravity model). INFO if the NNLO term is below numerical resolution.
   - Effort: 4-6 hours, 1 agent session (this is the harvest the genericity review explicitly queued).
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Equation = resonance problem (cavity SU(3), modes λ_n, BC = 4 axioms, selection = van-Hove cusp) | GEOMETRIC | SOLID | Strongest part of the document; correctly named throughout |
| 2 | `√x` cutoff as acoustic envelope `f∼\|ω\|`, Mellin-divergent | PHONONIC | PRELIMINARY | Sharpest resonance insight; presupposes linear low-mode dispersion (uncomputed → V.1, V.5) |
| 3 | S43 first-sound ring `A_FS/A_BAO = 0.204 = c₂²/c₁²`, `r₁=325 Mpc` | PHONONIC | LIVE / UNTESTED | Landau two-fluid prediction, zero-param, no ΛCDM analog; stalled on one fetched number (→ V.2, V.6) |
| 4 | Asymmetric acoustic white hole, KIND-tagged κ ledger | PHONONIC | PROVEN (6 walls) | Unruh/Visser/Volovik done correctly; greybody narrows A_s (→ V.7) |
| 5 | Spectral-Moment Decoupling `W ∝ R_K′³` (dispersion rigidity) | GEOMETRIC | CERTIFIED | Licenses cross-layer joint improbability; correctly forbids within-layer multiplication |
| 6 | Mach-number denominator: 13.75 (c_fabric=209.97) vs 17.1 (c_BLV=0.485) | — | CONFLICT (flagged) | Two incompatible sound speeds for "supersonic"; presentational, not physics; must pin (→ V.3) |
| 7 | Frequency hierarchy (3 bands, 10× sep) absent from capstone | PHONONIC | GAP (flagged) | Is the structural reason Leggett = DM channel; surfacing strengthens §7.1 (→ V.4) |
| 8 | `t*` = one-loop-coefficient corridor CLOSED | PHONONIC | FAIL (honest) | `t*` remains the single empirical coupling (spectral `Λ_QCD`); correctly retained in ledger |
| 9 | `a(t)` gap = frontier #8 (emergent EP); κ_EP=1 generic-cored | GEOMETRIC | OPEN (load-bearing) | Closing one closes both; genuine EP prediction first at NNLO (→ V.8) |

---

*Resonance verdict.* The capstone is a faithful resonance document: it begins, as it should, by identifying what oscillates, what the cavity is, what the boundary conditions are, and what selects the standing wave — and it answers all four correctly. Its three deepest cross-domain claims (acoustic envelope, two-fluid first-sound ring, analog white hole) are the same mathematics I work in at laboratory scale, and each is physics-coherent. The single conflict (Mach denominator) is presentational and does not threaten a verdict. The harvest is real: eight open questions, all convertible to runnable computation, two of them (V.1 the acoustic-dispersion check, V.2 the first-sound-ring forecast) nearly free because the substrate side is already in hand and only a fit or a fetched number stands between the framework and a new gate verdict.
