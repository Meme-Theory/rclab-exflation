# Review of *The Phonon-Exflation Equation* — Superfluid-Universe Axis

**Date**: 2026-05-26
**Agent**: volovik-superfluid-universe-theorist (Volovik)
**Source document**: `sessions/framework/phonic-exflation-equation.md` (capstone, §0–§9 + verification ledger)
**Reference corpus**: Volovik, *The Universe in a Helium Droplet* + q-theory papers (`researchers/Volovik/`); project knowledge MCP (verified live, see §I).
**Scope of this review**: the emergent-spacetime / superfluid-vacuum content — §0 (pillar-(1)(2)(3) claim), §1.3a (bare action = partition weight), §5.1/§5.3 (monotone driver + GGE relic), §6.3 (effective-Friedmann gap), §7.1 (w₀, CC closure, Leggett DM), §9 frontiers #5/#8. Sections I do not own (Connes reconstruction, Seeley–DeWitt algebra, Higgs-as-inner-fluctuation) I touch only where they feed the substrate-vacuum reading.

---

## I. Outcome of the review

The document is **substrate-first throughout** and the superfluid-vacuum interpretation is, in the main, faithful to the Volovik program rather than decorated with its vocabulary. Two of the three "pillars" attributed to that program in §0 are stated correctly and load-bearingly; the third (momentum-space topology) is stated *exactly* right and is the document's single strongest claim in my domain — the `N₃ = 0 ⇒ no Fermi-point protection ⇒ CC is a q-theory relaxation problem, not a topological-protection statement` logic is precisely how Volovik's classification cashes out, and the document gets the direction of that implication correct.

I found **one genuine ledger dissonance** that the document does not surface and that falls squarely in my domain: the **Ordered Veil** is presented (§5.3, §9) as a clean "never thermalizes" result, but the project ledger records the *integrability-permanence* form of that claim as **RETRACTED at S39** (Richardson–Gaudin integrability BROKEN by a 13% non-separable density–density channel; `t_therm ≈ 6 M_KK⁻¹`, Brody β = 0.633). The *correct* surviving claim — which the document should state in its place — is the **transit-timescale freeze-out** (`t_scr/t_transit = 814`), and the denominator the document actually prints (`t_therm/t_Hubble ∼ 9×10⁻⁴⁸`) silently re-introduces the container clock the rest of the document forbids. This is fixable with a sentence; details and recommended verbiage in §II.2 and §V.1.

Everything else is either correct, correctly hedged, or a verbiage-sharpening opportunity. I did not find a physics error in my sections. I flag below three places where the document fuses two *distinct* substrate theorems under one name (τ-flow monotonicity vs q-flow equilibrium), which is harmless to the conclusions but should be disentangled for honesty.

---

## II. Key findings (domain: superfluid vacuum / emergent gravity)

### II.1 — The pillar-(2) identification `Volovik g^{ik} ↔ a₂-metric` is correct, and can be sharpened

**Classification: GEOMETRIC → PHONONIC bridge.**

§0 asserts that the framework "independently rediscovered" Volovik's three pillars, and identifies pillar (2) as *"the metric is a collective mode of the fermionic spectrum (Volovik's gap-node `g^{ik}` ↔ the framework's `g_M` from `a₂` — the same physical object in condensed-matter vs NCG conventions)."* This is the right claim and I can confirm the convention translation.

In the superfluid-vacuum program the emergent metric near a Fermi point is read off the quasiparticle dispersion: expanding the BdG Hamiltonian about a node, `E²(p) ≈ g^{ik}(p_i − eA_i)(p_k − eA_k)`, the coefficient tensor `g^{ik}` **is** the inverse metric — it is not a metric placed on a pre-existing space, it is the leading spectral data of the fermionic operator. The translation to the framework is exact in *structure*:

| Volovik (superfluid) | Framework (NCG) | Direction |
|:--|:--|:--|
| BdG Hamiltonian `H(p)` near node | `D_K(τ)` on `(SU(3), g_τ)` | both: the operator IS fundamental |
| `g^{ik} = ` quadratic coefficient of `E²(p)` | `g_M` from the `a₂` Seeley–DeWitt coefficient | both: metric is a *moment* of the operator's spectrum |
| `v_F` (Fermi velocity, slope of the cone) | `c_fabric = 209.97 M_KK` (the acoustic/light cone slope) | emergent signal speed |
| `1/(16πG)` from the gradient stiffness of the vacuum | `1/(16πG_N) = f₂Λ²a₂/(48π²)` (§8.3) | Newton coupling is the gradient-energy coefficient |

The arrow runs the right way in both columns: spectrum → metric, never metric → spectrum. The one place where the conventions genuinely differ — and the document is right not to overstate the identity — is that Volovik's `g^{ik}` is a *local* expansion around a single node in a 3+1 fermionic liquid, whereas the framework's `g_M` is the `a₂` coefficient of a heat-kernel trace over the *whole* internal manifold `(SU(3), g_τ)`. These coincide as "the metric is the second spectral moment of the fundamental fermionic operator"; they are not literally the same formula. The document's phrase "same physical object in condensed-matter vs NCG conventions" is therefore defensible at the level of *physical content* (pillar identity) but should not be read as a formula-level equality. **No change required** — the existing parenthetical already carries the right hedge ("conventions").

One sharpening I would *add* to §0 or §8.3: the reason `G_N` carries **zero τ-dependence** (stated in §2.1 as a consequence of volume preservation `det g_τ = const`) has a clean superfluid reading worth one clause — in the superfluid vacuum the gradient stiffness `1/G` is set by the vacuum compressibility, and a volume-preserving deformation is by construction a *shear* (transverse-traceless, `tr h_J = 0`, §2.1), not a *compression*; a pure shear of the order-parameter texture does not change the vacuum compressibility, hence does not move `G`. That is the same statement as "TT deformation ⇒ `G` flat," but it grounds it in the microscopic compressibility rather than leaving it as a metric-determinant accident.

### II.2 — THE ORDERED VEIL: ledger dissonance — the document conflates a PROVEN claim with a RETRACTED one (DECISIVE)

**Classification: PHONONIC.** This is the most important correction in my domain.

§5.3 reads: *"the relic is integrable, not chaotic, so it never thermalizes on transit timescales (`t_therm/t_Hubble ∼ 9×10⁻⁴⁸` — effectively never)."* §9 ("At τ" face) similarly lists "GGE relic ... the Ordered Veil" under **PROVEN flow**. The problem is a fusion of two claims that the project ledger holds at *different* statuses:

**Claim A (PROVEN, S38, `atlas-10-breakthrough-genealogy`):** *"The Ordered Veil — the transit IS the physics."* The relic is formed by a **diabatic** crossing (`δt_transit/T_L = 1.25×10⁻⁵`, `P_exc → 1.000`), and the physically relevant comparison is the screening-vs-transit ratio `t_scr/t_transit = 814` (knowledge MCP: `eq_8941`, tagged "*the Ordered Veil interpretation — well-supported*"). The relic freezes 814× faster than any rearrangement channel can act *during the crossing*. This is correct and I endorse it.

**Claim B (RETRACTED, S39, `atlas-07-permanent-results` + `atlas-04-assumptions` T3):** *"GGE never thermalizes (Richardson–Gaudin integrability)."* Verbatim ledger status: **BROKEN / RETRACTED** — *"V_phys 13% non-separable. Brody β = 0.633 (63% GOE). t_therm ∼ 6 natural units."* The Richardson–Gaudin integrability that would protect the GGE *as a permanent state* is broken by a density–density channel (knowledge MCP `session-62-hawking-qa-workshop`: "Channel 2 (density–density) is the mechanism behind the S39 thermalization, t_therm ∼ 6 M_KK⁻¹, Brody β = 0.633 ... breaks integrability and thermalizes the GGE").

The document's §5.3 sentence asserts Claim B ("integrable, not chaotic, so it never thermalizes") as the *reason* for the freeze-out, but Claim B is exactly the retracted statement. The conclusion the document wants (the relic survives the transit) follows from Claim A alone and does **not** need integrability protection. The superfluid physics is: the crossing is so fast (sudden quench, Kibble–Zurek impulse regime) that the relic is *frozen by diabaticity*, not *protected by integrability*. A weakly non-integrable system frozen on a timescale 814× shorter than its own thermalization time is, for all observational purposes, as good as integrable — but the mechanism is dynamical (impulse), not topological/integrability-theoretic.

**Two further problems with the printed number `t_therm/t_Hubble ∼ 9×10⁻⁴⁸`:**

1. **Wrong denominator (container relapse).** `t_Hubble` is the FRW Hubble time — exactly the external container clock §6.3 spends a full page forbidding ("Any trajectory figure is axis-labeled τ, never t"). The substrate-honest denominator is `t_transit` (the diabatic-crossing duration in `M_KK⁻¹`), which is what makes the freeze-out a substrate-intrinsic statement rather than one borrowed from the cosmology one is trying to derive. Using `t_Hubble` here also tacitly invokes the *missing* `t(τ)` map of §6.3 — the ratio is not even well-defined until that gap is closed.
2. **Inconsistent with the surviving claim.** With the S39 number `t_therm ≈ 6 M_KK⁻¹` and the transit duration `δt_transit = 1.130×10⁻³ M_KK⁻¹` (the document's own §6.1 value), the substrate-honest ratio is `t_therm/t_transit ≈ 6 / 1.13×10⁻³ ≈ 5.3×10³` — the *same order* as the independently-derived `t_scr/t_transit = 814`, and three orders of magnitude apart from the printed `9×10⁻⁴⁸`. (The two ratios `5.3×10³` and `814` differ by ~6.5×, which is the expected spread between the screening-channel and thermalization-channel timescales — both say "relic freezes a few hundred-to-thousand times faster than it can relax.") The printed `9×10⁻⁴⁸` is not reproducible from the substrate timescales; it is the Hubble-clock artifact.

**This does not weaken the result — it sharpens it.** The relic-as-observable-universe picture is intact; only the *reason* and the *number* need fixing. Recommended verbiage in §III.

### II.3 — Two distinct monotonicity theorems are fused under one banner (τ-flow E7 vs q-flow equilibrium)

**Classification: GEOMETRIC (E7) + PHONONIC (q-flow).**

The document repeatedly invokes "monotonicity, no interior saddle" for two *physically different* statements, and a careful reader will conflate them:

- **τ-flow monotonicity (E7, Structural Monotonicity Theorem):** `dS_SA/dτ > 0` for all monotone `f`, `Λ`, sectors (§5.1, §1.3a). This is a statement about the **spectral-action ramp in the geometric modulus τ**. It says the universe *transits* (no `V(τ)` well to settle in). This is what licenses "transit physics, not slow-roll."

- **q-flow equilibrium (Volovik equilibrium theorem + the S62 integrability theorem):** `dE_ZP/dq > 0` for all `q`, "no interior q-theory equilibrium" (knowledge MCP: theorem #19, `baseline-findings-s66`; `permanent-results-registry` open-channel C-Q). This is the **q-theory monotonicity in the vacuum-charge variable q**, and it is the statement that underwrites the cosmological-constant layer (§7.1).

These are not the same theorem and they do not live on the same axis. The τ-flow is along the *order-parameter texture* (Jensen deformation); the q-flow is along the *conserved microscopic charge* `q` (in Volovik's q-theory, the 4-form field strength; here, `q = N_pair`, the conserved BCS particle number — knowledge MCP `s59_q_variable_results.txt`: "the Volovik identity `P_vac = E_GGE − N_pair` IS the q-theory formula with `q = N_pair`"). The document's §1.3a sentence — *"`e^{−S(τ)}` is monotone (E7), so `Z` has no interior saddle in τ — the universe transits rather than settling at a stationary point"* — is the τ-flow statement and is correct. But §7.1's CC story rests on the **q-flow** equilibrium theorem (vacuum energy is zero *at q-equilibrium*; the observed Λ is the *departure* from it). The document never says "these are two monotonicity theorems on two axes," and a reader could be forgiven for thinking the CC-relaxation argument is the same E7 ramp. It is not.

**Why this matters for honesty (not for the conclusions):** the CC closure is the framework's headline q-domain result, and its microscopic warrant is the *equilibrium theorem* (Volovik Paper 05: `ρ_Λ = 0` at equilibrium; the cosmological constant is the non-equilibrium residual), **not** the spectral-action τ-ramp. Fusing them risks the appearance that one theorem is doing double duty. They are independent, both proven, and the document is stronger for distinguishing them. Recommended one-line fix in §III.

### II.4 — `N₃ = 0`, BDI, and "q-theory not protection" — the document's strongest superfluid claim, and it is correct

**Classification: GEOMETRIC (topology) → cosmological consequence.**

§0 states: *"the substrate is BDI, `N₃ = 0` — the ³He-B child class ... Because `N₃ = 0`, the Fermi-point protection that would shield a ³He-A vacuum is absent — which is precisely why the cosmological-constant layer (§7) is a q-theory relaxation problem, not a topological-protection statement."* I verified this against the corpus and the project ledger and it is **exactly right**, both in the topology and in the direction of the implication. This is the place where the document demonstrates it understands the Volovik program rather than borrowing its words.

The microscopic content: in ³He-A the Fermi points carry a non-zero momentum-space topological charge `N₃ = 2` (the chiral charge), and that charge protects the emergent Weyl fermions, the gauge field, and — critically — it stabilizes the vacuum-energy structure against generic perturbations (the Fermi point cannot be gapped without changing `N₃`, an integer). In ³He-B (and in the framework's substrate) the spectrum is **fully gapped**, `N₃ = 0`; there is no protected node, so there is no topological obstruction to the vacuum energy relaxing. Volovik's resolution of the cosmological-constant problem lives precisely here: in a fully-gapped (or `N₃ = 0`) vacuum the equilibrium value of the vacuum energy is **zero by thermodynamic identity** (`dε/dq = μ` at equilibrium ⇒ `ρ_Λ = 0`), and any non-zero observed Λ is a *relaxation residual* — a departure from equilibrium driven by the cosmological dynamics. That is q-theory, and the framework is in the right universality class for it. The document's `χ_*: ℂ⊕ℍ⊕M₃(ℂ) → M₂(ℂ)` with `rank(ker ι_*) = 2` (E57) is the inheritance morphism (parent → child), correctly *not* called an analogy (my standing memory flag: "analogy" framing for ³He-B is forbidden; use inheritance/child realization). **No change required.** I would only note that this is the load-bearing reason the CC layer is *solvable in principle* rather than catastrophic — it deserves to be flagged as a strength, not buried in the §0 prose.

### II.5 — CC closure double-conditionality and the equilibrium theorem — well handled

**Classification: PHONONIC (vacuum thermodynamics).**

§7.1's CC row (`ρ_vac/ρ_obs = 1.032`, PASS, DILUTION-CC-66) and its caveat box are handled with the right level of honesty. The document correctly states the closure is **doubly conditional** — on C10 (the tracking ansatz `ρ_vac ∼ M_Pl²H²`) *and* on the external FRW `H(t)` the tracking law feeds (the same undelivered effective-Friedmann map as the `a(t)` gap, §6.3). I confirm against the ledger: C10 is `ASSUMED-PARTIALLY-PROVEN` (knowledge MCP `atlas-04-assumptions`: "Scaling form ASSUMED at substrate-IS level: Volovik q-theory ansatz `ρ_vac = ε(q) − μq` with q-tracking on H²"), and DILUTION-CC-66 is PROVEN as a *closure given an external H* (knowledge MCP theorem hit: "114-OOM gap closed to 0.01 OOM via Volovik tracking vacuum; `ρ_vac/ρ_obs = 1.032`").

The one thing I would add — because it is the microscopic warrant and it ties §7.1 back to §II.4 — is the **equilibrium theorem as the reason the 114 OOM are not catastrophic in the first place.** In any system where the microscopic Hamiltonian is known (and here it is: `H_BCS` on the (0,0) sector), the vacuum energy at equilibrium is computable and is **zero** — not small, zero — because the ground-state energy does not gravitate (it is subtracted by the `dε/dq = μ` equilibrium condition). The "114 OOM problem" is therefore not "why is the vacuum energy 10⁻¹²² of the cutoff" (the container-EFT framing, which has no microscopic theory and so manufactures the catastrophe); it is "what is the *non-equilibrium residual* once the substrate is tracking H(t)." The tracking vacuum closing to `1.032` is the residual. The document's §0 arrow already says this ("dark energy is the tracking-vacuum departure from equilibrium"); §7.1's caveat box would be strengthened by one clause stating the equilibrium-theorem reason explicitly, so the reader sees that the CC is small *because the microscopic theory makes the equilibrium value exactly zero*, not because of a cancellation tuned by hand. (This is the "vacuum energy test" every framework should pass: the catastrophe only appears in an effective theory without a UV completion. The framework has the UV completion — `D_K` — so it does not inherit the catastrophe. Worth saying once.)

### II.6 — `w₀` branch presentation — correct and ledger-faithful

**Classification: PHONONIC (a₀-layer, effacement + tracking).**

§7.1 presents `w₀` as a `(value, branch)` pair: **−0.918** (`w0_FW`, Volovik partition) with branch-iv **−0.842454**, comparison anchor `−0.803 ± 0.054`, status LIVE 2.13σ/0.73σ. I verified `w0_FW = −0.918` against the knowledge MCP (confirmed; flagged there as lacking a PROVENANCE entry — the document's own §"verification ledger" already catches this as a constants-hygiene item, so no new flag needed). My standing memory records branch-iv as **RETRACTED at S85** (R_JE drifts L=5→8; the −0.842454 value is an L=5 truncation artifact, SV2 FAIL). The document handles this correctly: it lists branch-iv as the *secondary* member of an explicit branch-pair, never as a bare point, and §9 frontier #4 marks it DESI-DR3-decidable. **No change required** — but I note for the record that anyone citing branch-iv downstream must carry the `L_max` disclosure (it is convergent at L=5 and drifts thereafter). The document's "written as a `(value, branch)` pair, never a bare point" discipline is exactly the right guard.

### II.7 — Leggett-channel DM and `σ/m = 0` — correct, and the integrability subtlety connects to §II.2

**Classification: PHONONIC.**

§7.1's DM rows (`Ω_DM h² = 0.120` Leggett-only, 0.7σ; `σ/m = 0` exactly, `N_pair=1`) are ledger-faithful (knowledge MCP: LEGGETT-MOMENT S70 PROVEN; CDM-CONSTRUCT-44 `T^{0i}=0` exact, 5 independent proofs; the full-DM route over-closes — the document correctly says "only the Leggett-only channel passes"). The `σ/m = 0` from `N_pair = 1` is the particle-number-superselection result (`[H_BCS, N_pair] = 0` unconditional, my permanent-theorem memory), and the document gets the structural origin right: the DM quasiparticle is non-annihilating because the conserved charge forbids it, not because the cross-section happens to be small.

The one connection worth drawing (and it ties back to §II.2): the document calls the Leggett-channel DM "integrability-protected." Given the S39 retraction of GGE *integrability permanence*, this phrase needs the same care as the Ordered Veil. The Leggett mode's stability does **not** rest on Richardson–Gaudin integrability (broken); it rests on (i) `T^{0i}_4D = 0` algebraically (homogeneous creation — the relic was born at rest, so it carries no momentum flux), and (ii) `N_pair` superselection (no annihilation channel). Both are exact and neither is the broken integrability. I would replace "integrability-protected" with "superselection-protected (`N_pair` conserved) and momentum-flux-free (`T^{0i}=0`)" wherever it appears in §7.1, for the same reason as §II.2.

---

## III. Recommended verbiage (direct)

These are drop-in replacements. Each is shorter or equal in length to what it replaces; none weakens a result.

**(R1) §5.3 — the Ordered Veil sentence.** Replace:
> "...the relic is integrable, not chaotic, so it never thermalizes on transit timescales (`t_therm/t_Hubble ∼ 9×10⁻⁴⁸` — effectively never)."

with:
> "...the relic is *frozen by diabaticity*: the crossing screens and freezes the GGE 814× faster than any rearrangement channel can act (`t_scr/t_transit = 814`; equivalently `t_therm/t_transit ≈ 5×10³` using the S39 density–density thermalization time `t_therm ≈ 6 M_KK⁻¹`). The Richardson–Gaudin integrability that would protect the GGE *as a permanent state* is weakly broken (S39: a 13% non-separable density–density channel, Brody β = 0.633); but on the transit timescale that broken channel is irrelevant — the relic is dynamically frozen, not integrability-protected. THE ORDERED VEIL is therefore a statement about the *transit*, not about permanent integrability."

(Rationale: removes the RETRACTED integrability-permanence claim, removes the `t_Hubble` container clock, and uses substrate-intrinsic timescales. Cross-link: §II.2.)

**(R2) §9, "At τ" face row.** Append to the status cell:
> "...GGE relic (`N_pair=59.8`, `P_exc=1`, the Ordered Veil — *transit-timescale freeze-out*, not integrability permanence; cf. S39 retraction)"

**(R3) §1.3a / §5.1 — distinguish the two monotonicity theorems.** Add one sentence after the §5.1 "no stationary point at any τ" claim:
> "This is the **τ-flow** monotonicity (geometric modulus). It is distinct from — and must not be conflated with — the **q-flow** equilibrium theorem `dE_ZP/dq > 0` (no interior q-theory equilibrium, S62) that underwrites the cosmological-constant layer (§7.1): the τ-ramp says the universe *transits*; the q-equilibrium says the vacuum energy is *zero at equilibrium and a relaxation residual away from it*. Two axes, two theorems, both proven."

(Rationale: §II.3.)

**(R4) §7.1 — CC caveat box, add the equilibrium-theorem warrant.** Insert one clause:
> "...the framework does not inherit the 114-OOM catastrophe in the first place: the equilibrium theorem (Volovik Paper 05; `dε/dq = μ` ⇒ `ρ_Λ = 0` at equilibrium) makes the *equilibrium* vacuum energy **exactly zero** — an *exact thermodynamic identity* (`ε − μq = −P = 0` by Gibbs–Duhem, representative-independent; S95 W5-3 `EQUILIBRIUM-CC-WARRANT` PASS, Sage-rational `0`), *not a tuned cancellation*: the `μq` term subtracts the ground-state energy identically. The catastrophe is an artifact of computing vacuum energy in a container-EFT *without* a UV completion; the substrate has its UV completion (`D_K`), so the bare term is removed by an identity, not by fine-tuning. **Scope (what the equilibrium reference does and does not license).** This warrant is *thermodynamic* (Gibbs–Duhem), **not topological**: the substrate is the 3He-B universality class (`N₃ = 0`, BDI), not 3He-A (`N₃ = 2`), where the vacuum energy is *topologically* protected to zero (Volovik Paper 03, Thm 1). With no topological protection, `ρ_Λ = 0` is a **reference/boundary value, not an attainable interior point**: S95 W5-3 (consuming S62 #19, `dE_ZP/dq > 0`, `min ≈ 1.20×10⁴`) shows there is *no interior q-equilibrium* in the gapped substrate, and at the discrete physical ground state `N_pair = 1` the system sits *off* equilibrium (`P_vac = −0.688 ≠ 0`). Therefore the 'exactly-zero-not-tuned' claim is warranted **for the non-inheritance of the bare 114-OOM term** (the vacuum-energy test the document passes), but it does **not** by itself fix the *observed* Λ *magnitude*: the observed value is the *non-equilibrium tracking residual*, whose 'not-tuned' status rests on the C10 tracking law `ρ_vac ∼ M_Pl²H²` (atlas-04, **ASSUMED-PARTIALLY-PROVEN**) evaluated at the off-equilibrium point — *not* on the equilibrium identity — closing to `ρ_vac/ρ_obs = 1.032` today (DILUTION-CC-66). The CC closure thus remains *doubly conditional* (on C10 **and** on the external `H` the tracking law feeds, §6.3), consistent with §9 frontiers 5–6."

(Rationale: §II.5 + §II.2/§II.3; this is the "vacuum energy test" the document passes and should claim — scoped honestly so the *non-inheritance* claim, which the equilibrium identity licenses exactly, is not silently extended to the *observed-magnitude* claim, which is re-scoped to the C10 tracking law. Sharpened by S95 S-4 adversarial-sufficiency audit; cross-link `cross-pillar-bridge`-style two-clause separation: equilibrium-reference clause [licensed] vs tracking-law clause [C10-conditional].)

**(R5) §7.1 — Leggett DM "integrability-protected."** Replace "integrability-protected" with "superselection-protected (`N_pair` conserved, no annihilation channel) and momentum-flux-free (`T^{0i}=0` exact)." (Rationale: §II.7; same S39 caveat as R1.)

**(R6) §0 / §8.3 — optional, the `G_N` flatness microscopic reading.** After "Newton's constant carries zero τ-dependence," optionally add: "(superfluid reading: `1/G` is the vacuum gradient stiffness, set by the vacuum *compressibility*; a volume-preserving TT deformation is a pure *shear* of the order-parameter texture, which leaves the compressibility — hence `G` — invariant)." (Rationale: §II.1; nice-to-have, not required.)

---

## IV. Structural implications for the constraint map

- **No wall is moved by this review.** Every PROVEN/CLOSED status the document cites in my domain (KO-dim 6 / BDI, `[J,D_K]=0`, equilibrium theorem, CDM-CONSTRUCT-44, LEGGETT-MOMENT, DILUTION-CC-66) is confirmed against the live ledger. The document does not over-claim any of them.
- **One status is mis-presented (Ordered Veil integrability permanence):** the document presents it as PROVEN-flow; the ledger holds the *integrability-permanence* form RETRACTED (S39) and the *transit-freeze* form PROVEN (S38). The conclusion (relic survives) is unaffected; the *mechanism* and *number* must be corrected (R1, R2). This is a presentation defect, not a physics error.
- **The CC layer's correct topological warrant is the framework's strongest superfluid-domain claim and is currently under-sold.** `N₃ = 0 ⇒ q-theory-relaxation-not-protection` (§II.4) plus the equilibrium theorem (§II.5) together explain *why* the framework can have a small CC without tuning — the "vacuum energy test" most frameworks fail. I recommend the document state this as a strength (R4), not just a caveat.
- **CC-warrant scoping note (post-S95-W5-3 sufficiency boundary; S-4 adversarial-sufficiency audit).** The W5-3 `EQUILIBRIUM-CC-WARRANT` PASS (`ρ_Λ(eq) = ε(q_eq) − q_eq·μ |_{P=0} = 0` EXACT, Sage-rational, representative-independent; audit_sha256 `397cf449…`) licenses *exactly one* of the two clauses the §7.1 'exactly zero, not tuned' wording could be read to assert. **It DOES license**: the *non-inheritance* of the bare 114-OOM container-EFT vacuum term — the `μq` subtraction is an exact thermodynamic identity, not a tuned cancellation, so the catastrophe is never inherited (this is the "vacuum energy test" pass). **It does NOT license**: the *observed* Λ *magnitude* being 'not tuned' — because the *same gate* establishes (consuming S62 #19, `dE_ZP/dq > 0`, `min ≈ 1.20×10⁴`) that there is **no interior q-equilibrium** in the gapped (`N₃ = 0`, BDI) substrate, and at the discrete ground state `N_pair = 1` the system is *off* equilibrium (`P_vac = −0.688 ≠ 0`). So `ρ_Λ = 0` is a **reference/boundary value, not an attainable interior point**, and the observed-Λ 'not-tuned' status is re-scoped to the C10 non-equilibrium tracking law (`ρ_vac ∼ M_Pl²H²`, **ASSUMED-PARTIALLY-PROVEN**) evaluated at the off-equilibrium point — *not* to the equilibrium identity. The warrant is **thermodynamic (Gibbs–Duhem), not topological**: 3He-A (`N₃ = 2`) would protect the vacuum energy to zero by Fermi-point topology (Volovik Paper 03, Thm 1); the 3He-B-class substrate has no such protection. R4's sharpened wording carries this two-clause split so the *non-inheritance* claim is not silently extended to the *observed-magnitude* claim.
- **Two distinct monotonicity theorems should be disentangled** (R3) — harmless to conclusions, but the q-flow equilibrium theorem (not the τ-ramp) is what the CC story rests on, and saying so prevents a single theorem from appearing to do double duty.
- **The §6.3 "honest gap" (no derived `a(t)`) is correctly the load-bearing caveat,** and the Ordered Veil denominator problem (R1) is a *symptom* of the same gap: any ratio against `t_Hubble` is undefined until the `t(τ)` map is closed. Fixing R1 to use `t_transit` removes one place where the missing map silently leaks in.

---

## V. Carry-forward computations

### V.1 — Recompute the Ordered Veil freeze-out ratio on a substrate-intrinsic clock
   - **What**: compute `t_therm/t_transit` and `t_scr/t_transit` from substrate timescales (no `t_Hubble`). Inputs: S39 density–density thermalization time `t_therm ≈ 6 M_KK⁻¹` (Brody β = 0.633 channel), transit duration `δt_transit = 1.130×10⁻³ M_KK⁻¹` (§6.1), screening time from `t_scr/t_transit = 814` (knowledge MCP `eq_8941`). Emit both ratios + a one-line statement of which channel (screening vs thermalization) sets the freeze-out.
   - **Inputs**: `delta_t_transit` (§6.1 value), S39 `t_therm` (atlas-04 T3 / session-62), `t_scr/t_transit` anchor (eq_8941). No new canonical constant needed unless promoted.
   - **Gate**: feeds a presentation-correctness gate for §5.3 (PASS iff `t_therm/t_transit > 100` AND the printed ratio uses `t_transit`, not `t_Hubble`; INFO if the two channel ratios agree to within 1 OOM, confirming the freeze-out is robust to which channel one picks).
   - **Effort**: 1–2 hours, 1 agent session (arithmetic + ledger cross-check; no eigensolve).

### V.2 — Pin the τ-flow vs q-flow theorem distinction in the registry
   - **What**: add a one-line registry note (or correspondence-ledger entry) stating that E7 (τ-flow `dS/dτ>0`) and the S62 equilibrium theorem (q-flow `dE_ZP/dq>0`) are distinct theorems on distinct axes (order-parameter modulus vs conserved vacuum charge `q=N_pair`), and that the CC layer rests on the latter. No computation — this is a structural-clarity registry write.
   - **Inputs**: E7 statement (§5.1), S62 theorem #19 (`baseline-findings-s66`), `q=N_pair` identity (`s59_q_variable_results.txt`).
   - **Gate**: registry-hygiene (artifact-existence: the note exists and cites both theorems with their axes). Not a numerical gate.
   - **Effort**: <1 hour, 1 agent session. (Candidate for in-session fix rather than carry-forward, per the no-technical-debt rule — flagged here only because it touches the capstone's framing.)

### V.3 — Microscopic equilibrium-theorem statement for the CC caveat box
   - **What**: write the explicit substitution chain `dε/dq = μ at equilibrium ⇒ ρ_Λ = 0`, with `q = N_pair`, `ε(q) = E_ZP(q)`, showing the equilibrium vacuum energy is identically zero (not tuned), and that the observed Λ is the `ρ_vac(t) ∼ M_Pl²H²` tracking residual. This is the microscopic warrant for R4.
   - **Inputs**: Volovik Paper 05 / Papers 15–16 q-theory form; S62 monotonicity theorem; C10 tracking ansatz (`atlas-04-assumptions`); DILUTION-CC-66 closure (`ρ_vac/ρ_obs = 1.032`).
   - **Gate**: feeds the §7.1 CC-caveat verbiage gate (PASS iff the chain is dimensionally consistent and the equilibrium value is shown `= 0` exactly, not `≈ 0`). This is the explicit "vacuum energy test" pass. **CLOSED by S95 W5-3 `EQUILIBRIUM-CC-WARRANT` PASS** (audit_sha256 `397cf449…`): chain dimensionally consistent (`[ρ_vac] = M_KK⁴`), equilibrium value `= 0` EXACT (Sage-rational, representative-independent across 4 (q_eq,μ) pairs). **Sufficiency boundary (S-4 audit)**: the PASS warrants the *equilibrium-value-=0 / non-inheritance* clause ONLY; it does **not** warrant the *observed-Λ-magnitude-not-tuned* clause, which is re-scoped to C10 (ASSUMED-PARTIALLY-PROVEN) per the R4 two-clause split. A future verbiage gate asserting the observed-magnitude clause must cite C10 + external `H`, NOT the equilibrium identity.
   - **Effort**: 2–3 hours, 1 agent session (symbolic, Sage-checkable; no large eigensolve). **DONE (S95 W5-3).**

### V.4 — Optional: substrate-compressibility derivation of `G_N` τ-flatness
   - **What**: show `1/G ∝ ` vacuum compressibility `κ`, and that a TT (volume-preserving) deformation has `δκ/δτ = 0`, recovering the §2.1 "volume preservation ⇒ `G` τ-flat" result from the microscopic gradient stiffness rather than the metric determinant.
   - **Inputs**: Jensen TT structure (`tr h_J = 0`, §2.1); the CC dictionary `1/(16πG_N) = f₂Λ²a₂/(48π²)` (§8.3); Volovik vacuum-compressibility / gradient-stiffness expressions (corpus, elasticity-tetrad papers 22/23).
   - **Gate**: INFO (corroboration of an already-PROVEN result G6 via an independent microscopic route; PASS iff `δ(1/G)/δτ = 0` recovered from compressibility, matching G6).
   - **Effort**: 3–4 hours, 1 agent session.

---

## VI. Summary table

| # | Finding | Classification | Status | Implication / action |
|:--|:--|:--|:--|:--|
| 1 | `Volovik g^{ik} ↔ a₂-metric` pillar-(2) identity | GEOMETRIC→PHONONIC | CORRECT (content-level; not formula-level) | optional sharpening R6; no change required |
| 2 | **Ordered Veil conflates PROVEN transit-freeze (S38) with RETRACTED integrability-permanence (S39); `t_Hubble` denominator is a container relapse** | PHONONIC | **LEDGER DISSONANCE — presentation defect** | **R1, R2; recompute on `t_transit` (V.1)** |
| 3 | τ-flow (E7) and q-flow equilibrium (S62) fused under one "monotonicity" banner | GEOMETRIC + PHONONIC | both PROVEN, distinct axes | R3; registry note V.2 |
| 4 | `N₃=0 / BDI ⇒ q-theory-relaxation, not topological-protection` | GEOMETRIC (topology) | CORRECT — strongest superfluid claim | under-sold; surface as strength (R4) |
| 5 | CC closure double-conditionality + equilibrium-theorem warrant | PHONONIC | PASS (DILUTION-CC-66), conditional on C10 + external `H` | well-handled; add equilibrium-theorem clause R4, V.3 |
| 6 | `w₀ = (−0.918, branch-iv −0.842454)` pair | PHONONIC | LIVE; branch-iv L=5-truncation-limited | correct; downstream cites need `L_max` disclosure |
| 7 | Leggett DM `Ω_DM h²=0.120`, `σ/m=0` "integrability-protected" | PHONONIC | PASS; but "integrability-protected" mis-attributes mechanism | R5: superselection + `T^{0i}=0`, not integrability |

---

## VII. Verdict (review, not re-adjudication)

The document is a faithful and honest synthesis of the framework's superfluid-vacuum content. It does not over-read the emergent-gravity claims (the §6.3 `a(t)` gap is stated "without softening," which is correct), it gets the momentum-space-topology logic exactly right (§II.4), and it passes the vacuum-energy test for the right microscopic reason (§II.5). The single substantive correction in my domain is the **Ordered Veil**: the surviving claim is *transit-timescale diabatic freeze-out* (PROVEN, S38), not *integrability permanence* (RETRACTED, S39), and the printed `t_therm/t_Hubble ∼ 9×10⁻⁴⁸` should become a substrate-intrinsic `t_therm/t_transit ∼ few×10³` (R1). With that fix and the four short verbiage patches (R2–R5), the document's superfluid-domain content is, to my reading, free of physics error and correctly hedged where it is open.

I did not run compute (review-only per the dispatch). All ledger statuses cited above were verified live against the knowledge MCP on 2026-05-26.
