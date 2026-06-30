# Capstone Equation Review — hawking

**Date**: 2026-05-29
**Agent**: hawking-theorist (Hawking)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` ("The Phonon-Exflation Equation", S95-era capstone)
- `.claude/rules/phononic-framing.md` (framing law)
- Cross-checks: `mcp__knowledge__` (gates S85-W6-4, S95 W5/W4, GGE-BISPECTRUM-67), `computations/_shared/canonical_constants.py`

---

## I. Session Outcome

The capstone is, from the vantage of semiclassical gravity and black-hole thermodynamics, **the most internally disciplined statement the framework has produced about its own horizon physics**, and it is honest about its one load-bearing wound. Read substrate-first, the document does exactly what a sound analog-gravity programme should: it identifies the kinematic content (mode-mixing across a surface where an acoustic flow goes supersonic), computes the Bogoliubov output mode-by-mode (the block-diagonality of `D_K` makes the per-mode parametric oscillator an *identity*, §2.2), and refuses to let "thermal radiation" smuggle a Gibbs temperature into a state that never thermalizes. The Ordered Veil (§5.3) is correctly reframed as a **resolution of an analog information paradox by absence**: a unitary Bogoliubov transformation produces a pure product GGE (`S_ent = 0`, S95 W5), so there is no thermal scrambling, no Page curve to reproduce, and no horizon-entropy debt — the squeeze phase is retained in the conserved charges. That is the right answer for the right reason.

Three things are over-claimed or under-disambiguated and I flag them without overturning any recorded verdict: (1) the §7.1 headline `f_NL = −1.505` is the canonical *bound* `max_f_NL_FW = 1.505`, **not** a central GGE-bispectrum prediction (the central values are 0.05–1.12; GGE-BISPECTRUM-67); presenting a bound as a `0.47σ` point detection is a presentational over-tightening. (2) The §5.3 "third leg" — `τ_fold` as a double-root extremal Killing horizon with `T_H = 0` — coexists in the knowledge base with a Gibbons–Hawking construction giving `T_GH = 0.2172` (nonzero) at the *same* `τ = 0.190` (s29c); these are two different surface-gravity functionals at one surface and the document does not say so. (3) The analog-temperature ledger (§6.2) is now carefully KIND-tagged and is the strongest version I have seen, but the central claim "`7.578 M_KK` IS the OBSERVED relic spectral temperature" still rests on an unfired falsifier (F1) and one INFO-by-unavailability greybody integral.

The honest gap (§6.3, no derived `a(t)`) is correctly elevated to *the* caveat and correctly tied to the Jacobson-1995 reading: a substrate theory is *expected* not to carry a fundamental Friedmann equation, but it still owes a derived *effective* one, and the document says both halves. I endorse that framing completely — it is the microscopic version of "Einstein equations are an equation of state," which is the single most defensible thing the framework can say about why it has no `H(t)` of its own.

---

## II. Key Results

### II.1 The Ordered Veil as analog-information-paradox-by-absence

**Result**: GGE relic is an exact pure product state `S_ent = 0` (S95 W5), frozen by diabaticity `R_therm = t_therm/t_transit = 5251.82 ≫ 1` (S95 W5); `P_exc = 1.000`, bosonic normalization `|α_k|²−|β_k|²=1` mode-by-mode. **Classification: PHONONIC** (substrate quasiparticle excitations of `D_K`; the relic content is the Bogoliubov output of the fold transit).

This is the part of the capstone closest to my expertise and it is *correct in its structure*. The transit is a Bogoliubov transformation between the pre-fold and post-fold mode bases — unitary by construction. The information-paradox analogy is precise and the document draws it correctly: a black hole's thermal Hawking flux scrambles infalling information into a mixed external state, and the resolution problem (Page curve, islands, replica wormholes) exists *because the radiation is thermal*. Here the squeeze is **not** thermalized — the GGE is a product state in the Richardson–Gaudin eigenbasis with three Lagrange multipliers conjugate to conserved charges, *not* to energy, hence no temperature. The phase data of the Bogoliubov transformation (the `arg β_k`) is retained in those charges. So there is genuinely **no Page curve to reproduce** — not because unitarity is restored late, but because nothing was ever scrambled. The substrate carries no horizon-entropy debt across the fold.

I want to state plainly what makes this *sound* rather than evasive. The standard worry about "no information loss because nothing thermalizes" is that it might just be a refusal to compute the late-time entanglement. It is not, here, because the document supplies the diabaticity ratio `R_therm = 5252` as a *computed* quantity (the crossing is 5000× faster than the only surviving thermalization channel can act), and the `S_ent = 0` is an exact product-state result, not an assumption. The retracted-integrability caveat (S39: the 13% non-separable density–density channel, Brody β = 0.633) is handled exactly the way I would handle it: the relic is **frozen by the transit timescale, not protected by permanent integrability**. That is the difference between "the state cannot thermalize ever" (false, retracted) and "the state cannot thermalize *in the time available*" (true, computed). The document's Conflict-C2-RESOLVED language is the right epistemic status.

The third, geometric leg — `κ = 0`, `T_H = 0` at the extremal double-root horizon — I treat separately in II.2 because it is the one place the causal-side argument is under-specified.

### II.2 The extremal-horizon `T_H = 0` leg — solid mechanism, undisambiguated surface

**Result**: §5.3 claims `τ_fold = 0.190` is a "double-root extremal Killing horizon (`V = V′ = 0 ⟹ κ = 0, T_H = 0`)," cited as the causal-side corroboration that the relic never thermalizes. Gate S85-W6-4-EXTREMAL-HORIZON-FORMAL: PASS, `value=kappa=0.00e+00`, scheme `Jensen_V_tree`, convention `2D_modulus_metric`. **Classification: GEOMETRIC** (a property of the emergent modulus-space metric function `V(τ)`).

The *mechanism* is exactly right and I confirm it from first principles. For a Killing horizon at a root `r_h` of the relevant metric function `V`, the surface gravity is `κ = ½|V′(r_h)|` (in the standard normalization where the Killing field is unit-normalized at infinity). At a **simple** root `V(r_h)=0, V′(r_h)≠0` you get `κ > 0` and a finite Hawking temperature `T_H = κ/2π`. At a **double** root `V(r_h)=V′(r_h)=0` the surface gravity vanishes identically — this is the extremal Reissner–Nordström / Nariai structure, where the near-horizon geometry becomes `AdS₂×(sphere)` and `T_H → 0`. So "double root ⟹ `κ=0` ⟹ `T_H=0`" is a correct theorem of horizon thermodynamics, and the gate's `κ = 0.00e+00` PASS is consistent with it.

**The flag** (a genuine gap, reported as a boundary, not an overturn): the knowledge base also carries an s29c Gibbons–Hawking computation giving `T_GH = 0.2172` (nonzero, interpolated) at the *same* `τ = 0.190` (`T3-BATCH-S29C-GIBBONS-HAWKING-TEMPERATURE`, now INFO/migrated). These two results are not in contradiction *if* one recognizes they are **two different surface-gravity functionals evaluated at the same `τ`**:
- the S85 `κ=0` is the surface gravity of the **2D modulus-space metric function** `V(τ)` at its double root (`tau_dump = tau_fold = 0.19`, confirmed: both pin to `0.19`);
- the s29c `T_GH = 0.2172` is a **de-Sitter-style Gibbons–Hawking temperature** of the emergent cosmological horizon, a different construction with a different `κ`.

This is precisely the analog-temperature trap I have flagged before in my own methodology notes (separate WHICH surface from WHICH κ-convention BEFORE adjudicating). The §6.2 analog-T ledger has *learned this lesson* — it KIND-tags `a₂` (THERMODYNAMIC-kinematic), `a₄` (THERMODYNAMIC-spectral), and S63-BLV (SONIC) and is admirably careful. **But §5.3's `T_H=0` leg does not carry the same KIND tag** and so reads as if it were the unique Hawking temperature of the fold, when the corpus contains a second, nonzero temperature at the same surface. The fix is one sentence: state that the `T_H=0` is the *extremal-double-root surface gravity of the modulus metric* `V(τ)`, distinct in KIND from the s29c Gibbons–Hawking temperature of the emergent horizon, and that the "never thermalizes" corroboration rests on the former. Until that sentence is added, the third leg is **PRELIMINARY as stated** (the mechanism is solid; the surface identification is ambiguous).

### II.3 The acoustic white hole and the greybody filter

**Result**: §6.2 — exflation's causal architecture is an acoustic white hole, ASYMMETRIC (one entry sonic surface at `τ₀≈0.1125`, `κ_entry=+18.52 M_KK`, open supersonic exit), over-determined at six independent walls (S95 W-1). Scalar sector sees the white hole; tensor sector crosses freely on `g_M` (two null cones, [T3] `β_T=0`). Escaping amplitude `A_s = (produced squeeze) × ∫Γ(ω)dω` with `Γ(ω) ∈ [0,1]` a Pöschl–Teller potential-barrier transmission (S95 W4-3). **Classification: PHONONIC/GEOMETRIC** (the causal structure is geometric; the squeeze it filters is phononic).

This is well-built and I endorse the structure. Two specific points from my domain:

**(a) The greybody mechanism is now correct.** The document explicitly replaces the **retracted S73B dispersive-group-velocity greybody** (which is on my own permanent-retractions list — "H1 dispersive group-velocity greybody, S73B") with a frequency-dependent potential-barrier transmission `Γ(ω)`. This is the right object. In genuine Hawking physics the greybody factor *is* the transmission probability of the emitted mode through the effective potential surrounding the horizon (the Regge–Wheeler / Pöschl–Teller barrier), and the emitted spectrum is `thermal × Γ(ω)`, never the bare thermal factor. The framework's "the horizon determines what escapes, not what is produced" is the correct slogan and the Pöschl–Teller barrier (transmitted_fraction = 0.512 at the `a₄` edge) is the correct realization. This is a real improvement over the retracted mechanism and I record it as solid.

**(b) The asymmetry argument is genuinely over-determined and I find no hole in it.** The white hole being asymmetric (entry sonic surface, *open* supersonic exit, no future-trapped horizon, no bounce) follows from the monotone `dS/dτ = +58,673 > 0`: a one-signed `(c²−v²)` derivative permits exactly one crossing, so there cannot be a second sonic surface to close a throat. The c_s-softening challenge (does `c_BLV → 0` at the DOS singularity, opening a second crossing?) is answered structurally — the softening lives in the *condensate* band-edge channel `c_B2` (rho-pinned to `1/(πρ_B2) = 0.0227 M_KK`, finite, not zero), not in the *scalar* transit channel the discriminant is built on; and routing onto a softer channel only *deepens* the interior (B2-channel fold Mach 293.79 vs 13.75). The deepest of the six walls — the irreversibility of the Kibble–Zurek quench fixing the entropy arrow — is the one I find most compelling, and it is the *right* physical reason: an acoustic white hole is the time-reverse of an acoustic black hole, and what selects the white-hole (outflow) orientation is exactly that the quench is irreversible. The substrate IS the irreversible transit; the lab acoustic white hole models it. Direction held.

**The one honest weakness in §6.2** (flagged, not overturned): `A_s` is band-cited (`3.11–4.27×10⁻⁹`), not point-cited, *because* `∫Γ(ω)dω` has not collapsed to a number (the greybody narrows but does not close the band, and the live BAO/first-sound forecast S95 W6-2 was INFO-by-unavailability — the comparison value was missing, not the substrate forecast). So the squeeze→`A_s` transduction is structurally complete but numerically open. That is a clean carry-forward (see §V.1).

### II.4 The CC layer is correctly NOT a topological-protection statement — and correctly de-Sitter-thermodynamic

**Result**: §7.1 — the substrate is BDI / `N₃ = 0` (the ³He-B *child* class, inheritance morphism E57, `rank(ker ι_*)=2`), so the Fermi-point protection that shields a ³He-A vacuum is *absent*. The equilibrium vacuum energy is exactly zero by the Gibbs–Duhem identity (`ε−μq=−P=0`, S95 W5-3 PASS, Sage-rational 0), **not** by topological protection; the observed Λ is the non-equilibrium tracking residual `ρ_vac ∼ M_Pl²H²` (the de Sitter horizon energy density `H/2π = T_dS`), closing to `ρ_vac/ρ_obs = 1.032` (DILUTION-CC-66). **Classification: GEOMETRIC/PHONONIC** (the `a₀` moment is geometric; the tracking residual is a phononic effacement leak).

From the black-hole-thermodynamics vantage this is the most physically literate CC framing the framework has produced, for one reason the document states and I want to underline: **the tracking law `ρ_vac ∼ M_Pl²H²` IS the de Sitter horizon energy density.** `H/2π = T_dS` is the Gibbons–Hawking temperature of the cosmological horizon (memory: `T = H/(2π)`, exact in my limiting-cases checklist), and `M_Pl²H²` is, up to `O(1)`, the de Sitter horizon's energy density `ρ ∼ T_dS²M_Pl² ∼ H²M_Pl²`. So "the substrate tracks its own emergent de Sitter horizon" is a *thermodynamically grounded* statement, not an ad-hoc scaling — it is the holographic/horizon-thermodynamic reading of the relaxation residual. I endorse this as the correct semiclassical-gravity interpretation of E44/E45.

The two-clause discipline (Clause A: non-inheritance exact by Gibbs–Duhem; Clause B: observed magnitude conditional on C10 + external `H`) is exactly the right scoping and matches the generalized-second-law instinct: the equilibrium reference (`ρ_Λ=0`) is an *unattainable boundary* for a gapped substrate with no interior q-equilibrium (S62 #19, `dE_ZP/dq>0`), and the physical ground state sits *off* it (`N_pair=1`, `P_vac=−0.688≠0`). The framework has **located** the CC term (the `a₀` moment, geometrically natural) and computed the *ratio* (truncation-robust); it has **not** derived the absolute magnitude from `D_K` (that awaits SDW convergence, frontier #6, and the external `H`). The document says exactly this. No overclaim.

---

## III. Gate Verdicts

These are cited from the source and the knowledge base as authoritative; I do not re-adjudicate them. I list those that touch my domain.

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S85-ACOUSTIC-WHITE-HOLE-CAUSAL-DISCONNECT-FORMAL | PROVEN | pre/post-fold causally disconnected |
| S85-W6-4-EXTREMAL-HORIZON-FORMAL | PASS | `κ = 0.00e+00` (2D modulus metric, double root) |
| S95 W5 (R_therm) | PASS | `R_therm = t_therm/t_transit = 5251.82 ≫ 1` |
| S95 W5 (S_ent) | PASS | `S_ent = 0` (exact pure product state) |
| S95 W5-3 EQUILIBRIUM-CC-WARRANT | PASS | `ε−μq=−P=0` (Gibbs–Duhem, Sage-rational 0) |
| S95 W4-5 (12D censorship) | PASS | anisotropic `τ→∞` singularity, censored (NEC to `τ_NEC=1.383`) |
| S95 W4-3 (analog greybody) | (per source) | Pöschl–Teller `Γ`, transmitted_fraction = 0.512 |
| S95 W4-2 / W-1 (analog-T ledger) | PASS | κ-ratio reproduces corpus 9.61 to 0.018% |
| S95 W2-1 (`t*` one-loop closure) | FAIL | `R = |t*_pred − t*|/t* = 1.977` (corridor CLOSED) |
| S95 W2-3 (no-interior-saddle, one-loop) | PASS | `dΓ/dτ` fixed sign, 0 interior sign-changes |
| DILUTION-CC-66 | PASS | `ρ_vac/ρ_obs = 1.032` (CONDITIONAL on C10) |
| COSMIC-CENSORSHIP-49 | PROVEN | triple-layer; lifted to 12D by W4-5 |
| GGE-BISPECTRUM-67 | (registry) | `f_NL^equil ~ 1.12`, `f_NL^folded = 0.129`, total `~1.03` |

---

## IV. Structural Implications

**Constraint / Implication / Surviving space** (my memory's required format):

**Constraint 1 — The transit is a Bogoliubov transformation, and it is diabatic.**
*Implication*: the produced state is a multi-mode squeezed vacuum (`P_exc=1`, maximal mixing), the analog-cosmology *opposite* of the adiabatic Bunch–Davies no-particle vacuum. This is why the slow-roll relations (`r=16ε`, `n_s=1−6ε+2η`) are INAPPLICABLE *at the level of derivation assumptions*, not merely wrong-numbered (§5.1, five independent arguments). I confirm this is structurally correct: `r=16ε` is a theorem of the single-clock adiabatic vacuum (it follows from the same `c_s=1`, single-field, Bunch–Davies premises that make the mode functions valid), and the fold violates all three premises (diabatic sweep, BdG `c_s≠1`, multi-mode squeezed GGE). The framework is *right* to refuse the slow-roll consistency relation.
*Surviving space*: tensor observables must be obtained from the **CMB-transferred** consistency `n_T = −r/8` (S66, Falsifier #2), NOT the slow-roll `n_T=−r/8` (the two coincide numerically but have different derivations — the document is careful about this). The Path-H vs Path-C tensor discriminator (LiteBIRD 2030, 4.25σ) survives as the cleanest near-term tensor test.

**Constraint 2 — A pure product GGE leaves no horizon-entropy debt.**
*Implication*: there is no analog information paradox to resolve by island/replica methods, because there is no thermal radiation. The framework's "reheating" produces order, not thermalization (THE ORDERED VEIL). This *closes* the entire Page-curve/scrambling/firewall line of attack for the substrate transit — not by solving it, but by establishing the premises that generate it are absent.
*Surviving space*: the open question is **not** "where does the information go" (it stays in the conserved charges) but "is the GGE relic's gravitational fate benign" — i.e., LEGGETT-GRAV-DECAY-67 (`Γ_grav < H_0`?), on which `Ω_DM h² = 0.120` is CONDITIONAL (CRITICAL). If the Leggett mode gravitationally decays faster than `H_0`, the DM sector collapses. This is the live information-theoretic vulnerability, and it is a *decay-rate* question, not a paradox.

**Constraint 3 — `f` is a nuisance functional; the regulator sets the tilt sign.**
*Implication*: the CMB tilt sign flips between schemes (`ε_H = +0.0216` for `√x` vs `−0.0449` for zeta-`a₄`), and the FI/RD partition is the statement of which observables survive marginalizing `f` out. I read this through the lens of regularization in QFT-in-curved-spacetime: the *spectrum* `{λ_k}` is the physical data (the analog of the field modes), but the *number the trace returns* depends on how the high modes are weighted — exactly as the renormalized stress-energy tensor `⟨T_μν⟩_ren` depends on the subtraction scheme, while ratios and anomaly coefficients (the FI quantities) do not.
*Surviving space*: FI observables (`R₁ = a₀a₄/a₂² = 1.12865` Sage-verified, `c_s`, `g₁/g₂`, the rank-drift exponent, `n_s`-as-ratio) are robust and carry the genuine constraining power; RD observables (`ε_H` sign, `n_s` value, `m_H`, absolute vacuum energy) must be *determined*, and the `n_s` BMA band `0.969 ± 0.022` (marginalizing `f`) is the correct UQ object. This is sound. The open frontier is the *first-principles selection of `f`* (frontier #2) — and the document is honest that the red tilt is right *if* `f=√x`.

**Constraint 4 — The Seeley–DeWitt expansion's convergence is NOT certified.**
*Implication*: ratio-observables are truncation-robust; absolute-energy observables (CC absolute magnitude, `A_s`) are conditional on an SDW-convergence statement (JACOBSON-NONLOCAL-64, OPEN, frontier #6). This is the genuine residual risk and §8.5 states it without softening. From my vantage this is the analog of the question "does the heat-kernel expansion of `Tr f(D²/Λ²)` converge or is it merely asymptotic?" — which is a real and hard question for any spectral-action programme. The document does not oversell.
*Surviving space*: trust the topological/representation-theoretic outputs (they survive continuum dissolution, T3-S43, `ε_c ∼ N^{−0.457}`); hold the absolute geometric magnitudes pending convergence. The geometry-vs-topology organizing spine (§9) is the deepest available defense and I find it convincing as a *scoping* discipline.

**Constraint 5 — The `t*` admixture is genuinely empirical; the matrix-model rigidity is bounded.**
*Implication*: S95 W2-1 CLOSED the corridor "`t*` is the one-loop threshold coefficient" (FAIL, `R=1.977`; `Γ_1loop ≈ 26%` is ~3× too large to *be* `t*=0.08832`). So the field content is forced by the algebra (exhaustion S95 W2-2, `dim HH¹ = dim HH² = 0`), but the regulator's admixture weight is NOT forced by the spectrum. The ledger is `{τ, Λ, f₀, f₂, f₄} + t*`, not the de-empiricized version.
*Surviving space*: `t*` remains the single empirical functional coupling (the spectral-functional analog of `Λ_QCD`). The open question is whether *any* first principle selects it — a real and unsolved problem the document correctly does not paper over.

---

## V. Carry-Forward Computations

**MANDATORY.** Each entry is a runnable computation with all four fields. These are the harvest of the document's open questions read through black-hole-thermodynamics / semiclassical-gravity eyes.

```
V.1. Collapse the analog greybody integral ∫Γ(ω)dω to a point — close the A_s band
   - What: Numerically integrate the Pöschl–Teller transmission Γ(ω) over the
     condensate-squeeze support ω∈[0.82,1.06] M_KK at τ_fold, using the W4-3
     barrier profile, to produce a single ∫Γ(ω)dω and hence a POINT A_s =
     (produced squeeze)×∫Γ(ω)dω. Compare to Planck A_s = 2.1×10⁻⁹.
   - Inputs: s73a_exit_horizon_bog.npz (barrier/Bogoliubov), the W4-3 Pöschl–Teller
     profile, canonical_constants: tau_fold=0.19, Z_fold, d2S_fold, c_fabric=209.97368;
     squeeze amplitude from the BdG u_k at the fold.
   - Gate: NEW gate S96-GREYBODY-AS-POINT. PASS if point A_s ∈ [1.9,2.4]×10⁻⁹
     (Planck 1σ); INFO if within band [3.11,4.27]×10⁻⁹ but outside Planck 1σ;
     FAIL if the integrated transmission cannot collapse the band (degenerate Γ).
   - Effort: 3–4 hours, 1 agent session.

V.2. Disambiguate the two surface-gravity functionals at τ=0.190 (KIND-tag the T_H=0 leg)
   - What: Recompute, side-by-side at τ=0.190, (a) the 2D-modulus-metric double-root
     surface gravity κ_V = ½|V′(τ_h)| (S85 W6-4 reproduction, expect κ=0) and
     (b) the Gibbons–Hawking temperature T_GH of the emergent horizon (s29c
     reproduction, expect ~0.2172). Emit an explicit KIND table (THERMODYNAMIC-modulus
     vs GIBBONS-HAWKING-emergent) and a one-paragraph note pinning which one the
     Ordered-Veil "never thermalizes" leg rests on.
   - Inputs: s85_w6_extremal_horizon_formal.npz, s29c_gibbons_hawking_temperature.npz,
     canonical_constants: tau_fold=tau_dump=0.19.
   - Gate: NEW gate S96-EXTREMAL-VS-GH-KIND-TAG. PASS if both functionals reproduce
     their recorded values AND the KIND distinction is documented (κ_V=0 is the
     modulus double-root; T_GH≠0 is the emergent-horizon GH temperature — NOT a
     contradiction); INFO if values reproduce but KIND ambiguity persists.
   - Effort: 2–3 hours, 1 agent session.

V.3. Re-cite f_NL as a bound, not a point — separate max_f_NL_FW from the central prediction
   - What: Verify against canonical_constants that max_f_NL_FW=1.505 is the BOUND on
     |f_NL| and that the central GGE-bispectrum prediction is f_NL^total≈1.03
     (folded 0.129, equilateral ~1.12). Compute the σ-distance of the CENTRAL value
     (not the bound) against Planck (−0.9±5.1 equilateral; −26±47 folded). Replace the
     §7.1 headline "f_NL=−1.505 (0.47σ)" with the central value + its σ-distance, and
     relabel −1.505 as the saturation bound.
   - Inputs: canonical_constants: max_f_NL_FW=1.505, f_NL_FW_S67_folded=0.129,
     f_NL_FW_S82_equilateral=0.0547; GGE-BISPECTRUM-67 (f_NL^equil~1.12, total~1.03);
     s74_gge_bispectrum_output (f_NL^equil=0.853526); Planck 2018 fNL.
   - Gate: NEW gate S96-FNL-BOUND-VS-POINT. PASS if the document's headline is the
     central value with correct σ-distance AND −1.505 is labeled as the bound;
     INFO if central and bound are reconciled but the sign convention needs a note;
     FAIL if no central value reproduces inside Planck 1σ.
   - Effort: 2 hours, 1 agent session.

V.4. Derive the back-reaction closure H² = f(ρ_relic, S_SA) — the a(t) gap, frontier #1/#8
   - What: Attempt the derived effective Friedmann map by promoting the produced
     relic energy density ρ_relic (from the BdG Bogoliubov spectrum, N_pair charge,
     E_exc) into a source for an emergent expansion rate, via a Jacobson-style
     entropy-balance on the a₂-emergent horizon (δQ = T δS ⟹ G_eff^{μν}=8πG T_μν).
     Target the emergent Bianchi identity ∇_μ G_eff^{μν}=0 on g_M (the lift of the
     internal-K EIH, S44, to the emergent metric). Output a candidate H²(ρ_relic,S_SA).
   - Inputs: S_SA(τ)=a₀−a₂+a₄ (E7); a₂^ζ=2776.165389, a₀^ζ=6440, a₄^ζ=1350.7216;
     M_KK=7.4287×10¹⁶ GeV; the W3-1 conservation-closed G_eff^{μν} (noether_ratio=½);
     W3-5 κ_EP=1.000000; relic E_exc/|E_cond|=443, N_pair charge.
   - Gate: feeds C2 (K_pivot, BROKEN-WITH-LIVE-RESEARCH-PATHWAY) and T6 (Friedmann–BCS,
     BROKEN). NEW gate S96-BACKREACTION-CLOSURE. PASS if a generally-covariant H²
     emerges with ∇_μG_eff=0 to machine-ε on g_M; INFO if the internal-K EIH lifts
     but the M_KK⁻¹→seconds normalization remains open; FAIL if the 155,984-mode
     spectral action cannot be closed against the relic source (the T6 overwhelm
     persists at the emergent level).
   - Effort: 1–2 agent sessions (this is the load-bearing frontier; expect partial).

V.5. Compute the generalized second law across the asymmetric white hole
   - What: Verify the generalized second law (GSL) for the exflation transit:
     show δ(S_matter + A_entry/4G_eff) ≥ 0 across the entry sonic surface, using the
     GGE relic entropy as S_matter (S_ent=0 for the pure relic, but S_GGE>0 for the
     thermodynamic von-Neumann entropy of the conserved-charge ensemble) and the
     entry-horizon area A_entry on g_acoustic. This tests whether the substrate
     respects the GSL even though it carries no thermal Hawking flux.
   - Inputs: κ_entry=+18.52 M_KK, τ₀≈0.1125; S_GGE≈2.21 nats (s52_bekenstein),
     S_ent=0 (S95 W5); entry-horizon area on g_acoustic∝√(ρ_s/c_s);
     canonical_constants: c_fabric, c_BLV=0.485.
   - Gate: NEW gate S96-GSL-WHITE-HOLE. PASS if δ(S_GGE + A_entry/4G_eff) ≥ 0 across
     the transit; INFO if the area term requires the (undelivered) effective G_eff
     normalization to sign; FAIL if GSL is violated (would signal the asymmetric
     white-hole construction is thermodynamically inconsistent).
   - Effort: 4–5 hours, 1 agent session. (Depends partly on V.4 for G_eff.)

V.6. Land falsifier F1 — scan for the a₂ kinematic-carrier squeeze branch near 72.8 M_KK
   - What: Search the Bogoliubov output spectrum for a scalar-channel squeeze branch
     near the a₂ kinematic-carrier temperature 72.8 M_KK (an order of magnitude above
     the a₄ condensate-squeeze support ω∈[0.82,1.06]). Both readers predict NULL,
     which would confirm the a₂ carrier is observationally invisible and license the
     categorical "a₂ carries no observed quantum." Until F1 lands, the COMPOSITE
     two-stage temperature is asserted but the categorical claim is NOT.
   - Inputs: the full BdG Bogoliubov spectrum at the fold (s73a / W4-2 npz),
     analog-T ledger T_a₂=72.8 M_KK (κ=457.66), T_a₄=7.578 M_KK (κ=47.61);
     condensate-squeeze support ω∈[0.82,1.06].
   - Gate: NEW gate S96-F1-A2-CARRIER-NULL. PASS (=NULL) if no scalar-channel squeeze
     branch with appreciable amplitude exists near 72.8 M_KK (confirms invisibility);
     FAIL if a squeeze branch IS found (the a₂ carrier would then carry an observable
     quantum, contradicting the composite-temperature reading).
   - Effort: 3 hours, 1 agent session.

V.7. SDW-convergence test for the absolute a₀ moment — close JACOBSON-NONLOCAL-64
   - What: Test whether the Seeley–DeWitt expansion Tr f(D²/Λ²) ~ Σ f_{d−n}Λ^{d−n}a_n
     converges (vs is merely asymptotic) by computing the a₆, a₈ terms (the finite
     pole-ladder tail S_d={0,2,4,6,8}) and the ratio |a₈ term|/|a₆ term| and
     |a₆ term|/|a₄ term| at τ_fold. A bounded, decreasing ratio supports
     convergence of the a₀-dominated vacuum-energy sum; a growing ratio confirms
     asymptotic-only status (CC absolute magnitude stays conditional).
   - Inputs: dimension spectrum S_d={0,2,4,6,8} (E38, Connes–Moscovici 1995);
     a₀^ζ=6440, a₂^ζ=2776.165389, a₄^ζ=1350.7216; ζ_{D_K}(s) residues at s=(d−n)/2;
     L_max=10 spectrum cache.
   - Gate: JACOBSON-NONLOCAL-64 (OPEN), frontier #6. NEW gate S96-SDW-CONVERGENCE.
     PASS (convergent) if successive ratios decrease below 1; INFO if bounded but
     not monotone; FAIL (asymptotic-only) if ratios grow — in which case the CC
     ABSOLUTE magnitude remains permanently conditional (the ratio R₁ is unaffected).
   - Effort: 4–6 hours, 1 agent session.

V.8. NNLO emergent-EP Casimir discriminator — the first genuine substrate EP prediction
   - What: Compute κ_EP at NNLO where the band-specific Casimir ν_b(C₂) re-enters the
     ratio (at LO+NLO κ_EP=1 is generic-identity-cored per the S95 W3 genericity
     review — it is the Lichnerowicz R/4 coefficient of ANY spin Dirac operator). The
     NNLO term carries C₂(b) and is substrate-specific: a deviation κ_EP^NNLO ≠ 1 that
     a generic emergent-gravity model would NOT predict.
   - Inputs: E5 (D_K²=∇*∇+¼R_K), band Casimirs C₂(B1),C₂(B3); W3-5 κ_EP=1.000000
     (LO+NLO); R_K(τ_fold)=2.018, R_K′ via E3; the single-spectral-triple postulate.
   - Gate: NEW gate CF-S96-EP-NNLO-CASIMIR-DISCRIMINATOR (named in §9 frontier #8).
     PASS (=substrate-specific prediction) if κ_EP^NNLO computably ≠ 1 with a
     band-Casimir-dependent value; INFO if the NNLO term is below the framework's
     numerical resolution; FAIL if κ_EP^NNLO=1 persists (EP would be generic to
     all orders, no substrate prediction).
   - Effort: 1 agent session.

V.9. One-loop robustness of the no-interior-saddle result on the FULL τ-domain
   - What: Extend the S95 W2-3 one-loop no-interior-saddle PASS (dΓ/dτ fixed sign on
     τ∈[0,τ_now]) to the full τ∈[0,∞) domain including the overshoot turnaround
     τ=1.614 and the NEC boundary τ_NEC=1.383, to confirm Γ[τ]=S[D_K(τ)]+½Tr ln(D_K²/Λ²)
     has NO interior stationary point anywhere the censoring barrier allows the modulus
     to reach. This hardens the Gibbons–Hawking–York boundary-domination reading.
   - Inputs: S_SA(τ)=a₀−a₂+a₄; Γ_1loop=½Tr ln(D_K²/Λ²); the 200-point W2-3 grid
     extended; τ_NEC=1.383, overshoot τ=1.614, Kretschmann K∼e^{4τ}.
   - Gate: extends S95 W2-3. NEW gate S96-ONELOOP-SADDLE-FULL-DOMAIN. PASS if 0
     interior sign-changes of dΓ/dτ on [0,τ_NEC]; INFO if a sign-change appears only
     in the censored region τ>τ_NEC (irrelevant to physical epoch); FAIL if an
     interior saddle appears at τ<τ_NEC (would reopen the slow-roll/equilibrium reading).
   - Effort: 2–3 hours, 1 agent session.
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Ordered Veil = analog-info-paradox-by-absence; `S_ent=0`, `R_therm=5252` | PHONONIC | SOLID (S95 W5) | No Page curve to reproduce; no horizon-entropy debt; unitary Bogoliubov, pure GGE |
| 2 | Extremal double-root horizon `κ=0, T_H=0` (the 3rd Veil leg) | GEOMETRIC | MECHANISM SOLID; surface UNDISAMBIGUATED | s29c `T_GH=0.2172` at same τ is a different κ-functional — KIND-tag needed (V.2) |
| 3 | Acoustic white hole; greybody = Pöschl–Teller `Γ(ω)` (replaces retracted S73B) | PHONONIC/GEOMETRIC | SOLID; `A_s` band open | Correct greybody object; `∫Γdω` not yet collapsed to a point (V.1) |
| 4 | Asymmetric white hole over-determined at 6 walls | GEOMETRIC | SOLID | Irreversible quench fixes white-hole orientation; no bounce — endorsed |
| 5 | CC tracking `ρ_vac∼M_Pl²H²` IS de Sitter horizon energy `H/2π=T_dS` | GEOMETRIC/PHONONIC | SOLID framing; magnitude C10-conditional | Located CC term, computed ratio (1.032); absolute magnitude awaits SDW (V.7) |
| 6 | `f_NL = −1.505` headline | PHONONIC | OVER-TIGHTENED | `1.505` is the BOUND `max_f_NL_FW`; central GGE prediction is ~1.03 (V.3) |
| 7 | Slow-roll `r=16ε`, `n_s` formulae INAPPLICABLE (5 args) | PHONONIC | SOLID | Diabatic multi-mode squeezed vacuum; correct refusal; tensor via `n_T=−r/8` CMB-transferred |
| 8 | `t*` is genuinely empirical (W2-1 closed one-loop corridor) | GEOMETRIC | SOLID | Matrix-model rigidity bounded: field content forced, admixture weight not |
| 9 | No derived `a(t)` (frontier #1/#8) | — | OPEN, the load-bearing gap | Jacobson reading: substrate owes a *derived effective* Friedmann map, not a fundamental one (V.4) |
| 10 | SDW convergence not certified (frontier #6) | GEOMETRIC | OPEN | Ratio-observables robust; absolute-energy observables conditional (V.7) |
| 11 | LEGGETT-GRAV-DECAY-67 (`Γ_grav<H_0`?) | PHONONIC | OPEN (CRITICAL) | The live information-theoretic vulnerability: a decay-rate question, not a paradox |
| 12 | NNLO emergent-EP first genuine substrate prediction | GEOMETRIC | OPEN | LO+NLO `κ_EP=1` is generic-identity-cored; NNLO Casimir term is the discriminator (V.8) |

---

**Closing note (substrate-first, held throughout).** Every arrow in this review runs `D_K eigenvalues → spectral-action moments → emergent physics → measurement`. The acoustic white hole is the *laboratory realization of* the substrate's irreversible Kibble–Zurek transit, not a black hole the substrate sits inside; the de Sitter temperature `H/2π` is the *emergent* horizon's, read off the `a₂`-channel reorganization, not an external clock the vacuum decays in; the Page curve is absent because the GGE is a pure Bogoliubov product, not because unitarity is restored late in a thermal evaporation. The document holds this direction with unusual discipline. Its one place of genuine container-relapse risk — §6.3's history-narration — it pre-empts explicitly, and its single load-bearing wound (no derived `a(t)`) it states without softening and correctly diagnoses as a *category statement about the fundamental object*, not a discarded obligation. The harvest in §V is ripe precisely because the document has been honest about where the math is unfinished.
