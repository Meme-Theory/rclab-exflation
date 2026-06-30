# Hawking-Theorist Review: The Phonon-Exflation Equation

**Date**: 2026-05-26
**Agent**: hawking-theorist (semiclassical gravity, black-hole thermodynamics, particle creation in curved spacetime)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` (capstone, §0–§9 + verification ledger)
- `.claude/rules/phononic-framing.md` (framing law)
- Cross-checks: knowledge MCP (`tau_fold=0.19`, `Mach_max=13.75`, `n_pairs=59.8`; S63 acoustic-horizon workshop; S70/S71/S73a entry/exit horizon spectra; S85 acoustic-white-hole formalization)

---

## I. Review Outcome

The document is, from my field, a **semiclassical-gravity construction read in the correct direction**. Three pillars that took the relativity community fifty years to assemble — particle creation from a non-stationary background, an acoustic causal horizon, and a Euclidean path-integral identity for the action — are all present here, and all are pointed *substrate → emergent*, not the reverse. The single most consequential thing I can say is that **the framework's "no minimum at any τ" (E7) is not a defect to be apologized for; it is the structural reason the cosmogenesis is a particle-creation problem rather than a vacuum-selection problem**, and §1.3a and §5.1 already say exactly this. That is the deepest correct insight in the document from my vantage, and it is stated cleanly.

My review engages four loci where my expertise is decisive: §1.3a (the Euclidean triple identity), §5.3 (Bogoliubov pair production / the Ordered Veil), §6.2 (the two-horizon acoustic white hole and its analog temperatures), and §6.3 + §7.1 (the information-theoretic and thermodynamic content of the missing FRW map and the CC closure). I flag **one genuine internal tension** (the analog-temperature ledger is incomplete relative to the corpus), **two places where a Hawking-style argument would *strengthen* a claim already made**, and offer **direct verbiage** for the two that matter most.

I re-adjudicate no gate verdict or PROVEN/CLOSED status; all are taken as authoritative.

---

## II. Key Engagements

### II.1 §1.3a — The Euclidean triple identity is correctly stated, and is the document's strongest move toward "one equation"

**Classification: GEOMETRIC** (the spectral action and its partition-function face); the excitations built on it in §5.3 are PHONONIC.

The identification

$$
Z=\sum_{D_K(\tau)} e^{-\mathcal{S}[D_K(\tau),f,\Lambda]},\qquad \mathcal{S}\equiv I_E,
$$

with the sum running over the substrate's *own* internal geometries (the modulus `τ` and the spectral data of `D_K`) and **not** over a background metric, is the Gibbons–Hawking Euclidean path-integral statement read in the only direction the framework permits. This is the correct and load-bearing translation of my own program. In the Euclidean quantum-gravity I built, `Z = ∫ Dg\, e^{-I_E[g]}` was *forced* to sum over geometries because the metric was the dynamical variable — and that sum was the perpetual embarrassment of the approach (which geometries? what measure? what contour?). Here the embarrassment is removed by construction: there is no `Dg`; the dynamical variable is the spectrum `{λ_k(τ)}` of one operator, and "geometry" is the `a₂`-readout of the dominant configuration. The document is right that this makes "one equation for the universe" *categorically stronger* than the container version. I want to underline why, in my language:

> In the Euclidean path integral over metrics, the saddle is a geometry and the one-loop determinant `det'(\Delta)` is computed *on that geometry*. Here the saddle is a spectral configuration, and the one-loop face `Γ_{1loop} = ½ Tr ln(D_K²/Λ²)` (§1.3a) is computed *on the spectrum directly*. The functional integral never leaves the spectral data — which is exactly the property that lets the framework claim it derives the stage rather than populating it.

**The monotonicity → no-interior-saddle chain is the genuinely novel content, and it is correct.** In ordinary Euclidean gravity the dominant saddle is a *stationary point* of `I_E` (the round sphere for de Sitter; the Schwarzschild–anti-de-Sitter instanton for the black hole). The framework's E7 theorem says `e^{-S(τ)}` is **monotone in τ**, so there is *no interior stationary point* — `Z` is dominated by the genesis boundary `τ=0`. This is the structural reason the cosmogenesis is a transit, and it is the structural reason the slow-roll dictionary is inapplicable (§5.1). I have nothing to correct here; I have something to *add* (see §II.5).

**One verbiage suggestion for §1.3a.** The document calls the phonon-free-energy face `F = -T ln Z ≈ T·S` "SPECULATIVE (session-6)" and the partition-function face "DEFENSIBLE (session-16)." Good. But the *reason* `F=-T\ln Z` is only a leading-order face deserves one clause, because a careful reader will ask "whose temperature `T`?" The answer is in my domain and is clean:

> Suggested insert after the `F=-T\ln Z` sentence: *"The temperature in this free-energy face is the substrate's own (the inverse Euclidean period of the dominant configuration), not a thermal-bath temperature — which is why the relic that the transit produces (§5.3) is characterized by Bogoliubov coefficients and Lagrange multipliers, not by a single `T`. There is no Gibbsian `T` until something thermalizes, and the Ordered Veil says nothing does."*

This closes the loop between §1.3a and §5.3 and pre-empts the most common misreading of a partition function ("there must be a temperature").

---

### II.2 §5.3 — The Bogoliubov pair-production / GGE-relic argument is the cleanest realization of my domain in the whole document; I have a normalization point and a sharpening

**Classification: PHONONIC** (the relic is the excitation content of the fabric).

This section *is* cosmological particle creation in curved spacetime, done in the analog-gravity register, and it is done correctly. The parametric-oscillator equation `u_k'' + ω_k²(τ(t))u_k = 0` with the BdG dispersion `ω_k = E_k = √((λ_k²-μ²)² + Δ_k²)` is the right object: it is the Klein–Gordon mode equation on a non-stationary background, with the role of the cosmological scale factor played by `τ(t)`. The diabatic-saturation result `P_exc → 1.000` is the analog statement that the in-vacuum and out-vacuum are maximally Bogoliubov-mixed — the strong-production limit, the opposite of the adiabatic (no-particle) limit. This is exactly the regime in which my 1974/1975 calculation lived (the collapse is a non-adiabatic change of the mode basis), and the framework has it.

**Normalization check (my standing discipline).** The document quotes the relic content `N_pair = 59.8`, `S_inst = 0.0686`, `P_exc = 1.000`, `E_exc/|E_cond| = 443`, and identifies the output as an analytic GGE "determined by the Bogoliubov coefficients, not a temperature." For a bosonic (phononic) sector the Bogoliubov coefficients must satisfy

$$
|\alpha_k|^2 - |\beta_k|^2 = 1\qquad\text{(bosonic normalization)},
$$

and the occupation per mode is `n_k = |\beta_k|^2`, with `P_exc` the probability the mode is excited at all. **I confirmed against the corpus** (`n_pairs=59.8` canonical; `P_exc>0.999` is the S57 Leggett-adiabaticity result; `s75_dimer_z2_pair_production` is the explicit pair-production gate) that the framework's numbers are the project-canonical ones. The document is internally consistent on this and I do not re-adjudicate. My only request is a **one-line normalization audit hook** for the reader who knows the formalism:

> Suggested footnote at the `N_pair=59.8` line: *"Bosonic normalization `|α_k|²-|β_k|²=1` holds mode-by-mode; the relic occupation is `n_k=|β_k|²` and the GGE Lagrange multipliers are conjugate to the conserved charges of the integrable post-fold Hamiltonian, not to energy — hence no temperature. The diabatic limit `P_exc→1` is the maximal-mixing (`|β_k|²` large) regime, the analog-cosmology opposite of the adiabatic no-particle vacuum."*

**The Ordered Veil deserves a sharper thermodynamic statement, and it is favorable to the framework.** The document says the relic "never thermalizes on transit timescales (`t_therm/t_Hubble ∼ 9×10⁻⁴⁸`)" and is "integrable, not chaotic." This is correct and it is *the right resolution of a real problem* — but the document undersells what it has achieved relative to my field. The reason this matters:

The black-hole information paradox, in its sharpest form, is the conflict between **unitary evolution** and **thermalization to an exactly mixed (thermal) state**. Hawking radiation is thermal because the out-state is a *thermal density matrix* — the off-diagonal coherences are gone, and that is where the information appears to be lost. The framework's GGE relic is the *anti-thermal* object: it is a **pure product state** (`S_ent = 0`, stated in §5.3) whose apparent randomness is encoded in conserved charges, not in a temperature. In information-theoretic language:

- A thermal relic would have `S_ent = S_thermal > 0` and would *lose* the phase information of the transit.
- The GGE relic has `S_ent = 0` and *retains* the full Bogoliubov phase data — the squeeze is coherent.

**This is unitarity made manifest.** The transit is a Bogoliubov transformation, which is unitary by construction; the Ordered Veil is the statement that the framework *does not subsequently scramble* that unitary into a thermal mixture. The framework therefore has **no information paradox at the fold** — and it has none for a structural reason (integrability / non-scrambling), not by fiat. I recommend the document say this, because it is one of the strongest things the construction does and it is currently buried:

> **Suggested addition to §5.3 (a short paragraph after the Ordered Veil sentence):** *"In information-theoretic terms the Ordered Veil is the framework's resolution of what would otherwise be an analog information paradox. The transit is a Bogoliubov transformation — unitary by construction — and a thermalizing relic (`S_ent>0`) would scramble that unitary into a mixed state, hiding the squeeze phase the way a black hole's thermal Hawking flux hides infalling information. The GGE relic instead stays a pure product state (`S_ent=0`): the Bogoliubov phase data is retained in the conserved charges of the integrable post-fold Hamiltonian. The relic is `min{c·t, S_BH}`-type in neither slope — there is no Page curve to reproduce because nothing thermalizes. The substrate carries no horizon-entropy debt out of the fold."*

This is the kind of conclusion my methodology pushes toward: follow the unitarity. The framework's mathematics already delivered the answer; the document should name it.

---

### II.3 §6.2 — The two-horizon acoustic white hole is correct in structure, but the analog-temperature ledger is incomplete relative to the corpus — this is the one genuine internal tension I found

**Classification: GEOMETRIC** (the causal architecture is a property of the emergent acoustic metric).

The six-layer causal partition — subsonic approach → entry horizon (`a₂`, kinematic) → supersonic white-hole interior → van Hove fold (GGE production) → exit horizon (`a₄`, BCS) → subsonic plateau — is a faithful acoustic-white-hole picture, and the `subsonic → supersonic → subsonic` flow giving a causal disconnect between pre-fold and post-fold is the correct resolution of the horizon problem *as an acoustic effect* (S85 PROVEN, confirmed in MCP). The white-hole orientation (not black-hole) is right: a white hole *emits* and cannot be entered from outside, which is exactly the causal role of a genesis boundary. I endorse the structure.

**The tension.** §6.2 quotes two analog temperatures:

| | ENTRY horizon | EXIT horizon |
|:--|:--|:--|
| Analog temperature | `72.8 M_KK` (kinematic) | `7.578 M_KK` (decoherence-regulated) |

But the corpus carries a *third* analog temperature that the document does not reconcile: the **S63 acoustic-horizon temperature `T_a = 0.112 M_KK`** (the BLV acoustic-metric horizon, `T_a = ħκ_a/2π`, QA-H4.2), which I pulled from the knowledge base. Three analog temperatures spanning `0.112 → 7.578 → 72.8 M_KK` (nearly **three orders of magnitude**) are floating in the corpus, and the capstone prints only two of them, with no statement of how they relate. This is a genuine gap, and it is exactly the kind of thing my domain is built to catch, because **for a true Hawking-type horizon the temperature is fixed by the surface gravity and nothing else**:

$$
T_H=\frac{\hbar\,\kappa}{2\pi},\qquad \kappa=\tfrac12\,\partial_n(c^2-v^2)\Big|_{\text{horizon}}\ \text{(BLV analog surface gravity)}.
$$

If the entry and exit horizons are genuinely *distinct surfaces with distinct surface gravities* (controlled by `a₂` vs `a₄` gradients — which is plausible and is what the document asserts), then two different `T` is *correct physics*, and the document should say so explicitly via the surface-gravity formula. But the `0.112 M_KK` value from S63 is a third number that must be either (a) identified with one of the two horizons, (b) declared a different observable (e.g., the *internal-acoustic-metric* horizon vs the *kinematic-transit* horizon), or (c) flagged as superseded. The document cannot leave all three unreconciled — a reader fluent in analog gravity will (correctly) ask "the analog Hawking temperature of *what surface*?"

**Constraint-map statement:**

- **Constraint**: A Hawking-type analog temperature is determined uniquely by the surface gravity `κ` of a specific Mach-1 surface; `T_a = ħκ/2π`.
- **Implication**: The corpus's three analog temperatures (`0.112`, `7.578`, `72.8 M_KK`) cannot all describe the same surface; either they index three distinct surfaces (each with its own `κ`) or some are superseded.
- **Surviving space**: The document's two-horizon structure (`72.8` kinematic entry / `7.578` decoherence-regulated exit) is *admissible* and even attractive — two surfaces, two surface gravities, two temperatures — **provided** §6.2 states the surface-gravity origin of each and either places or retires the S63 `0.112 M_KK` value.

**Direct verbiage for §6.2** (insert as a note under the analog-temperature row):

> *"Each analog temperature is `T_a = ħκ/2π` with `κ` the BLV surface gravity `½∂_n(c²−v²)` of its own Mach-1 surface; the entry/exit values differ because the entry surface gravity is set by the `a₂` (kinematic) gradient and the exit by the `a₄` (BCS-condensation) gradient — two surfaces, two `κ`, two `T`, exactly as for a rotating vs charged horizon carrying distinct `κ`. [Reconcile with the S63 internal-acoustic-horizon value `T_a=0.112 M_KK` (QA-H4.2): state whether it is a third surface (the BLV internal-acoustic horizon, distinct from the kinematic transit horizon) or superseded by the S70/S71 entry/exit construction.]"*

**A second-order remark that favors the framework.** The exit-horizon temperature being "decoherence-regulated" (`7.578 M_KK`) and *lower* than the kinematic entry temperature is physically sensible and even elegant: it is the analog statement that **the horizon determines what escapes, not what is produced** (the document's own phrase). In my language this is the **greybody factor**. The squeeze (the would-be `A_s`) is *produced* at the fold with a broad spectrum, and the exit horizon acts as a frequency-dependent transmission filter — the analog greybody factor `Γ(ω)` — that regulates the escaping spectrum down. The document gestures at this ("regulated down at the exit horizon by decoherence"). I recommend naming it:

> Suggested clause in §6.2: *"This is the analog greybody factor: the produced spectrum at the fold is filtered by the exit horizon's frequency-dependent transmission `Γ(ω)`, so the escaping `A_s` is the *produced* squeeze times the *exit* greybody factor, not the produced squeeze itself."*

(I note my memory's *Permanent Retraction* of "H1 dispersive group-velocity greybody (S73B)" — that retraction was about a *specific dispersive group-velocity mechanism* for the greybody factor, not about the existence of a greybody/transmission filter at the exit horizon. The clause above asserts only the latter, which is the model-independent statement that a horizon transmits frequency-dependently. I am not reviving the retracted mechanism.)

---

### II.4 §6.3 + §7.1 — The missing FRW map and the CC closure: the document's honesty is correct, and a Hawking-style reading makes the gap *less* alarming, not more

**Classification: GEOMETRIC** (the `a(t)` map and the `a₀`-layer vacuum energy).

§6.3 is the document's most important caveat and it is stated without softening, which I applaud. The framework has no derived FRW scale factor `a(t)`; C1 postulates `τ = cosmic time`; C2 (`K_pivot`) is BROKEN-WITH-LIVE-RESEARCH-PATHWAY; T6 (Friedmann–BCS locking) is BROKEN; and the CC closure is *doubly conditional* (on C10's tracking ansatz **and** on the external FRW `H` that ansatz feeds). I have no quarrel with any of this and I re-adjudicate none of it.

What I can add from my field is a **reframing that the document half-states and should complete**, because it bears directly on the "Friedmann is the wrong question" debate the section is having with itself. The document concludes — correctly — that this is "right about the *fundamental* level and wrong about the *effective* level." I want to give the fundamental-level half its proper weight, in the register of Jacobson's 1995 result (which my memory flags as load-bearing for this framework):

> **Jacobson showed the Einstein equation is an equation of state** — `δQ = T\,δS` across local Rindler horizons yields `G_{μν} = 8πG T_{μν}` *thermodynamically*, with no fundamental metric dynamics. The phonon-exflation framework is the **microscopic substrate that Jacobson's argument presupposes but does not supply**: the `a₂` moment IS the `(1/16πG)∫√g R` that Jacobson derives as an equation of state, and the substrate spectral monotonicity (E7) is the microscopic origin of the second-law-like behavior Jacobson needs.

The consequence for §6.3: **the absence of a fundamental Friedmann equation is exactly what Jacobson's result predicts a substrate theory should look like.** A microscopic theory of the fabric is *not obligated* to contain `H² = (8πG/3)ρ` as a fundamental law any more than statistical mechanics is obligated to contain `PV=NkT` as a fundamental law — the Friedmann equation is the *equation of state* of the emergent metric, and it must be *derived* (the effective-level obligation the document correctly retains), not *posited* (the fundamental-level obligation it correctly disowns). The document says "category statement, not discarded obligation." Jacobson is the citation that makes that sentence a *theorem-backed* claim rather than a stance.

> **Direct verbiage for §6.3** (append to the "Why this is a category statement" paragraph): *"This is the Jacobson (1995) reading made microscopic: the Einstein/Friedmann equations are equations of state of the emergent metric, derivable from horizon thermodynamics but not fundamental. A substrate theory is therefore expected NOT to contain a fundamental Friedmann equation — the `a₂` moment is the Einstein–Hilbert action Jacobson recovers thermodynamically, and the open obligation is to derive the effective `H²=(8πG/3)ρ` as the substrate's equation of state, exactly as one derives `PV=NkT` from a partition function. The framework's own `Z=Σ e^{-S}` (§1.3a) is the partition function in question; the missing `a(t)` is the missing equation of state, not a missing fundamental law."*

This converts the "honest gap" from an apology into a **precisely-posed derivation target**, which is what it should be.

**On the CC closure (§7.1) — one thermodynamic caution.** The `ρ_vac/ρ_obs = 1.032` (DILUTION-CC-66, PASS) is, as the document scrupulously notes, conditional on the tracking ansatz `ρ_vac ∼ M_Pl²H²(t)` *and* on borrowing the external FRW `H(t)`. From my field I add only that **the tracking law `ρ_vac ∼ M_Pl²H²` is itself a thermodynamic-horizon relation in disguise**: `M_Pl²H²` is (up to `O(1)`) the de Sitter horizon energy density, and `H/2π` is the Gibbons–Hawking de Sitter temperature `T_dS`. So the Volovik tracking vacuum is asserting `ρ_vac ∼` (de Sitter horizon energy density) — a relation that is *natural* in a horizon-thermodynamics framework and that the document could anchor more explicitly:

> Suggested clause in §7.1's "Substrate readings" paragraph: *"The tracking relation `ρ_vac ∼ M_Pl²H²` is the de Sitter horizon energy density (`H/2π` is the Gibbons–Hawking temperature `T_dS`); the Volovik tracking vacuum is the statement that the substrate's vacuum energy tracks its own emergent de Sitter horizon, which is why it dilutes *as* the horizon grows rather than sitting at the catastrophic `Λ⁴` value a container theory would assign it."*

This does not close C10 — the derivation of the tracking law from `D_K` remains owed — but it correctly identifies *what kind of object* the tracking law is (a horizon-thermodynamic relation), which sharpens the open gate.

---

### II.5 §5.1 / §1.3a — A Hawking-style strengthening of the "no interior saddle" claim

**Classification: GEOMETRIC.**

The document establishes (E7, 9,600/9,600 checks) that `e^{-S(τ)}` is monotone, so `Z` has no interior saddle in `τ` and the weight is dominated by the genesis boundary `τ=0`. This is correct and I endorse it. From the Euclidean-path-integral side I can add a **boundary-saddle observation** that sharpens it and is favorable:

In Euclidean quantum gravity, a path integral with no interior stationary point is dominated by its *boundary* configuration — and the boundary term is precisely the Gibbons–Hawking–York boundary term `(1/8πG)∮ K\sqrt{h}` that I introduced for exactly this reason (so that `I_E` has a well-defined variational principle on a manifold with boundary). The framework's genesis boundary `τ=0` is the analog of that boundary. **The monotone ramp is therefore not a pathology; it is a theory whose entire action is a boundary contribution at genesis** — which is the cleanest possible statement of "the universe transits from a genesis boundary rather than settling at a stationary point." I recommend a single clause:

> Suggested clause in §1.3a or §5.1: *"A Euclidean action with no interior stationary point is dominated by its boundary configuration — here the genesis boundary `τ=0`. This is the analog of a Gibbons–Hawking–York boundary-dominated path integral: the universe's weight is a genesis-boundary contribution, and the transit is the relaxation of that boundary configuration down the monotone ramp, not the decay of an interior false vacuum."*

This is a *strengthening*, not a correction — it gives the monotonicity theorem a Euclidean-gravity interpretation that makes the "transit, not slow-roll" conclusion structurally inevitable rather than merely observed.

---

## III. Gate / Status Cross-Checks (no re-adjudication)

| Item | Source claim | MCP cross-check | Verdict |
|:-----|:-------------|:----------------|:--------|
| `τ_fold` | 0.190 | `tau_fold = 0.19` (CONST-FREEZE-42) | Consistent |
| `Mach_max` | 13.75 | `Mach_max = 13.75` (no PROVENANCE entry — hygiene) | Consistent; flag hygiene |
| GGE relic | `N_pair = 59.8`, `P_exc = 1.000` | `n_pairs = 59.8`; S57 `P_exc>0.999`; `s75_dimer_z2_pair_production` | Consistent |
| Acoustic white hole | PROVEN, causal disconnect | S85 `acoustic_white_hole_formal` PROVEN | Consistent |
| Entry/exit horizons | two surfaces, `a₂`/`a₄` | S71 `entry_horizon_spectrum`, S73a `exit_horizon_bog` | Consistent (structure) |
| Analog temperatures | `72.8` / `7.578 M_KK` | **S63 `T_a = 0.112 M_KK` also in corpus** | **TENSION — see II.3** |

The only flag I raise is the analog-temperature ledger (§II.3): a third corpus value (`0.112 M_KK`) is unreconciled in the capstone. This is a documentation/reconciliation gap, not a physics error.

---

## IV. Structural Implications (constraint-map format)

1. **The Euclidean triple identity is the correct backbone (§1.3a).** *Constraint*: a partition function `Z=Σ e^{-S}` over spectral configurations with monotone `e^{-S}` has no interior saddle. *Implication*: cosmogenesis is boundary-dominated → transit, not equilibration → slow-roll inapplicable. *Surviving space*: the framework's transit physics is the *forced* reading; equilibrium/false-vacuum cosmogenesis is structurally excluded (consistent with the 27 closed equilibrium attempts S17–S40, which I do not re-adjudicate).

2. **The Ordered Veil resolves an analog information paradox (§5.3).** *Constraint*: a Bogoliubov transformation is unitary; thermalization would scramble it to a mixed state. *Implication*: a pure (`S_ent=0`) integrable relic retains the squeeze phase → no information loss → no Page curve obligation (nothing thermalizes). *Surviving space*: the framework owes no horizon-entropy reconciliation at the fold; this is a *resolved* item that the document currently underclaims.

3. **The analog-temperature ledger constrains the horizon structure (§6.2).** *Constraint*: `T_a = ħκ/2π` is surface-gravity-determined. *Implication*: distinct `T` ⇒ distinct surfaces (admissible: `a₂` entry vs `a₄` exit). *Surviving space*: the two-horizon picture survives iff each `T` is given a surface-gravity origin and the S63 `0.112 M_KK` value is placed or retired.

4. **The missing FRW map is a Jacobson-predicted equation-of-state gap (§6.3).** *Constraint*: by Jacobson 1995 the Friedmann equation is an equation of state, not a fundamental law. *Implication*: a substrate theory is *expected* not to contain a fundamental Friedmann equation; the obligation is to derive the *effective* one. *Surviving space*: the "Friedmann is the wrong question" stance is theorem-backed at the fundamental level; the effective-level derivation (the `a(t)`/`K_pivot`/normalization bridge) remains the single most important open item, correctly identified as such (frontier #1).

5. **The CC tracking law is a horizon-thermodynamic relation (§7.1).** *Constraint*: `M_Pl²H²` is the de Sitter horizon energy density; `H/2π = T_dS`. *Implication*: the Volovik tracking vacuum tracks the substrate's own emergent de Sitter horizon. *Surviving space*: C10 remains open as a *derivation* of this relation from `D_K`, but its *form* is now identified, which constrains what a derivation must produce.

---

## V. Carry-Forward Computations

These are computation/reconciliation targets surfaced by this review. Each has the four required fields. None re-adjudicates a closed gate.

```
V.1. Analog-temperature ledger reconciliation
   - What: Reconcile the three corpus analog temperatures into one surface-gravity table:
     for each Mach-1 surface (S63 internal-acoustic horizon; S70/S71 entry horizon;
     S73a exit horizon), compute T_a = ħκ/2π with κ = ½∂_n(c²−v²) from the
     corresponding spectral-moment gradient (a₂ for entry, a₄ for exit, BLV acoustic
     metric for the S63 internal horizon). Output a 3-row {surface, κ, T_a} table;
     declare which of {0.112, 7.578, 72.8 M_KK} indexes which surface or is superseded.
   - Inputs: a2_fold, a4_fold, c_fabric (=209.97 M_KK), v_term, Mach_max (canonical_constants);
     S63 QA-H4.2 T_a derivation; S71 s71_entry_horizon_spectrum.npz; S73a s73a_exit_horizon_bog.npz.
   - Gate: new gate HAWKING-ANALOG-T-LEDGER. PASS iff all three corpus temperatures are
     each assigned a distinct surface with a computed κ, OR explicitly superseded with a
     reason; FAIL if any of the three remains unreconciled; INFO if a fourth surface is found.
   - Effort: 3–4 hours, 1 agent session (uses existing npz spectra; no new spectral compute).

V.2. GGE-relic purity / no-Page-curve certification
   - What: Certify S_ent = 0 for the post-fold GGE product state directly from the
     Bogoliubov coefficients: compute the reduced density matrix of the relic, verify
     Tr ρ² = 1 (pure) to machine ε, and confirm the von Neumann entropy S_ent = 0 across
     all 32 modes. Contrast with the thermal-relic counterfactual S_thermal = Σ_k
     [(1+n_k)ln(1+n_k) − n_k ln n_k] to quantify the entropy the Ordered Veil avoids.
   - Inputs: Bogoliubov α_k, β_k per mode (from s75_dimer_z2_pair_production.npz or
     the §5.3 BdG dispersion ω_k); n_pairs=59.8; P_exc canonical.
   - Gate: new gate HAWKING-GGE-PURITY. PASS iff Tr ρ² = 1 and S_ent < 1e-12 (pure product
     state, no information loss); INFO reporting S_thermal counterfactual; FAIL if S_ent > 1e-6
     (would indicate hidden scrambling and reopen an analog information question).
   - Effort: 2–3 hours, 1 agent session.

V.3. Exit-horizon greybody factor for A_s
   - What: Compute the frequency-dependent transmission Γ(ω) of the exit horizon
     (decoherence-regulated, 7.578 M_KK) and express the escaping scalar amplitude as
     A_s = (produced squeeze at fold) × ∫ Γ(ω) dω. Tests whether the band-cited
     A_s ∈ [3.11, 4.27]×10⁻⁹ (§7.1) narrows once the greybody filter is applied.
   - Inputs: produced squeeze spectrum at τ_fold (entry-horizon BdG); exit-horizon
     decoherence rate (s73a_exit_horizon_bog.npz); ε_pivot (pending — the A_s band's
     stated dependency).
   - Gate: feeds the existing A_s determination (currently band-cited pending ε_pivot);
     new sub-gate HAWKING-GREYBODY-AS. INFO if A_s band narrows; does NOT claim PASS
     (ε_pivot still open). Distinct from the retracted S73B dispersive-group-velocity
     greybody mechanism — this is the model-independent transmission filter only.
   - Effort: 4–6 hours, 1 agent session.

V.4. Tracking-law as de Sitter horizon relation (C10 derivation target spec)
   - What: Test whether ρ_vac ∼ M_Pl²H² can be derived as the substrate's de Sitter
     horizon energy density by computing the a₀-layer vacuum energy at the emergent
     de Sitter horizon scale and comparing to M_Pl²H² with H from the (still-borrowed)
     external FRW. This is a SPEC for the C10 derivation, not a closure — it identifies
     the form the derivation must reproduce.
   - Inputs: a_0_FW_zeta = 6440; M_Pl_eff (from §8.3 dictionary, f₂≈92); the external H(t)
     (C10 input, flagged as borrowed); ρ_vac/ρ_obs = 1.032 (DILUTION-CC-66, PASS — not
     re-adjudicated, used as the target).
   - Gate: feeds C10 (ASSUMED-PARTIALLY-PROVEN); new diagnostic HAWKING-CC-HORIZON-FORM.
     INFO only — reports whether the a₀-at-horizon scaling matches M_Pl²H² in form;
     cannot PASS C10 (requires the effective-Friedmann map, frontier #1).
   - Effort: 4–6 hours, 1 agent session; blocked on / coupled to the a(t) bridge (§6.3).
```

---

## VI. Summary Table

| # | Engagement | Classification | Status | Implication |
|:--|:-----------|:---------------|:-------|:------------|
| 1 | §1.3a Euclidean triple identity | GEOMETRIC | Endorsed; verbiage offered | The correct backbone; "no `Dg`" is why "one equation" is categorically stronger |
| 2 | §5.3 Bogoliubov / GGE / Ordered Veil | PHONONIC | Endorsed; underclaimed | Resolves an analog information paradox via unitarity + non-scrambling; no Page-curve obligation |
| 3 | §6.2 two-horizon acoustic white hole | GEOMETRIC | Structure endorsed; **ledger gap** | Three corpus analog-`T` values unreconciled; surface-gravity table needed |
| 4 | §6.3 missing FRW map | GEOMETRIC | Honesty endorsed; reframed | Jacobson-predicted equation-of-state gap, not a missing fundamental law |
| 5 | §7.1 CC tracking law | GEOMETRIC | Endorsed conditional; form identified | Tracking law is a de Sitter horizon relation; sharpens C10 |
| 6 | §5.1 no-interior-saddle | GEOMETRIC | Endorsed; strengthened | Boundary-dominated (GHY-analog) path integral makes transit inevitable |

---

## VII. One closing judgment

The document follows its own mathematics to the uncomfortable conclusions and does not flinch — `a(t)` is not derived, `f` is not selected, the family number is open, and all three are stated without softening. That is the right way to handle a claim this large, and it is the way I would handle it. From my field the construction is **a correctly-oriented analog-gravity cosmology**: particle creation done as a unitary Bogoliubov transformation, a causal horizon done as an acoustic white hole, and an action done as a Euclidean partition-function weight summed over the substrate's own spectral configurations. Where I push hardest — the analog-temperature ledger (§II.3) — the fix is reconciliation, not retraction. Where I push to *strengthen* — the Ordered Veil as an information-paradox resolution (§II.2) and the missing FRW map as a Jacobson equation-of-state gap (§II.4) — the framework's own results already contain the stronger statement; the document need only name it.

The single arrow holds throughout: `D_K eigenvalues → spectral moments → emergent physics → measurement`. I did not find a place where the document silently inverts it. That is the property that keeps a theory of this scope honest, and it is the property the framework has.
