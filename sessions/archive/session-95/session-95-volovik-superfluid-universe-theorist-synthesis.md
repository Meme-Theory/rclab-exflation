# S95 Workshop Campaign — Slot 1 Entry S-4 (SOLO Structural Verdict)

**Author**: volovik-superfluid-universe-theorist
**Date**: 2026-05-29
**Type**: Adversarial-sufficiency audit (SOLO; sole author)
**Target**: Does the W5-3 `EQUILIBRIUM-CC-WARRANT` PASS (`ρ_vac(eq) = ε(q_eq) − q_eq·μ |_{P=0} = 0` EXACT; audit_sha256 `397cf449…`) WARRANT the `phonic-exflation-equation.md` §7.1 caveat-box clause R4 ("exactly zero, not tuned") — given that the *same gate* reports the substrate provably NEVER sits at q-equilibrium?
**Scope guard**: This is an audit of an already-PASS gate's *sufficiency for a downstream doc-claim*. It does **NOT** re-open or re-adjudicate the W5-3 PASS verdict. The `ρ_Λ(eq) = 0` identity is exact and stands.

**Sources read in full**: `sessions/archive/session-95/session-95-w5-workingpaper.md` (§W5-1…§W5-6 + Wave-5 Synthesis); `computations/session-95/s95_gate_verdicts.txt` (all lines, W5-3 = line 73-75). Cross-referenced: `sessions/archive/session-60/framework-3HeB-comparison.md §II.2/§II.3` (the gate's cited substrate-physics authority); `sessions/framework/phonic-exflation-equation.md §7.1/§8.5/§9`; `sessions/framework/Collabs/phonic-exflation-equation-volovik-collab.md` (clause-R4 source; §III/§IV/§V); `sessions/archive/session-95/session-95-housekeeping.md §A17` (the doc-integration routing target); knowledge MCP (`C10` = `ASSUMED-PARTIALLY-PROVEN`; `DILUTION-CC-66` PROVEN; `rho_Lambda_obs = 2.7e-47`).

---

## I. Structural Verdict (headline)

**The claim "exactly zero, not tuned" is WARRANTED by the equilibrium identity ALONE for ONE of its two readable clauses, and must be RE-SCOPED to the non-equilibrium tracking law for the other.** The W5-3 identity is sufficient warrant for the clause it actually proves and insufficient for the clause it is at risk of being read to assert. The fix is not to weaken either reading but to **split the clause** so each rests on its correct warrant.

| Clause the §7.1 R4 wording could assert | Warranted by W5-3 equilibrium identity alone? | Correct warrant |
|:--|:--|:--|
| **(A) Non-inheritance**: the bare 114-OOM container-EFT vacuum term is NOT inherited; its removal is an exact identity, not a tuning | **YES — fully warranted** | The `μq` subtraction is a representative-independent thermodynamic identity (`ε − μq = −P = 0`, Gibbs–Duhem). W5-3 PASS is exactly this. |
| **(B) Observed-Λ magnitude**: the *observed* Λ value is "not tuned" | **NO — not warranted by the identity** | The C10 tracking law `ρ_vac ∼ M_Pl²H²` (**ASSUMED-PARTIALLY-PROVEN**) evaluated at the off-equilibrium point + external `H`; DILUTION-CC-66 closes to `1.032`. |

Reading A (the gate's) and Reading B (skeptical NCG/q-theory) are **both correct, on disjoint domains**. They are not rival readings of the same claim — they are warrants for two *different* claims that the single phrase "exactly zero, not tuned" silently fuses. The adversarial tension dissolves once the fusion is named: A licenses **non-inheritance** (the vacuum-energy test pass), B governs the **observed magnitude** (C10-conditional). Neither machinery can carry the other's clause, exactly as the dispatch framing anticipated.

**This is a Non-Promotion-by-Held-Number-adjacent structural read** (`cross-pillar-bridge-anatomy.md §"Non-Promotion-by-Held-Number Meta-Taxonomy"`): the theorem-STRUCTURE (the equilibrium identity) is permanent/proven; what is HELD is the *extension* of its warrant from clause (A) to clause (B). The differentia that fires is **scope-collision** — one exact statement (equilibrium reference) being read to discharge a second, distinct statement (observed magnitude) it does not bind.

---

## II. The two readings, adjudicated with substitution chains

Per `math-scripts.md §"Double-Check Logic Before Compute"`, the direction/sufficiency claims below are backed by explicit substitution chains (Sage-verified this session; chains reproduced).

### II.1 Reading A — the equilibrium identity is the legitimate exact REFERENCE (the gate's reading)

```
Def 1: q        = N_pair                 [conserved BCS particle number = Volovik q-theory 4-form charge; s59]
Def 2: ε(q)     = E_ZP(q)                [per-volume vacuum zero-point energy; S62 cache]
Def 3: μ        = dε/dq                  [chemical potential; thermodynamic conjugate of q]
Def 4: ρ_vac(q) = ε(q) − q·dε/dq         [Volovik gravitating vacuum energy; q-theory Paper 13-14]

Substitute equilibrium (dε/dq = μ) + Gibbs-Duhem P=0 closure (ε(q_eq) = q_eq·μ):
        ρ_vac(eq) = ε(q_eq) − q_eq·μ = −P|_eq = 0       [EXACT — Sage: simplify_full → 0]

Direction: the (μ·q) term EXACTLY subtracts the ground-state energy. NOT tuned —
           the subtraction is identically zero, representative-independent (4/4 (q_eq,μ) pairs, residual 0).
```

**Verdict on Reading A**: **CORRECT and exact.** It is the legitimate REFERENCE. It establishes that the framework does not inherit the 114-OOM catastrophe: the bare container-EFT vacuum term is removed by an *identity*, not by a fine-tuned cancellation between large numbers. This is precisely the "vacuum energy test" most EFT-based frameworks fail (they compute vacuum energy without a UV completion; the substrate has its UV completion `D_K`, so the `μq` subtraction is available and exact). **What Reading A licenses: clause (A), non-inheritance — fully.** What it does NOT do: assert anything about *which nonzero value* the observed Λ takes — the identity returns 0, and the observed Λ is manifestly ≠ 0.

### II.2 Reading B — the observed-Λ "not tuned" status is set by the tracking law, not the (unreachable) identity (skeptical reading)

```
Fact 1 (from the SAME gate, consuming S62 #19):  dE_ZP/dq > 0 ∀ q   [min ≈ 1.199e4, max ≈ 2.073e4]
                                                  ⇒ interior_equilibrium = False
Fact 2 (concrete representative ε(q)=√(λ²+q)):    ρ_vac(q) = (2λ²+q)/(2√(λ²+q)) > 0 ∀ q
                                                  ⇒ solve ρ_vac(q)=0 → ∅ (NO interior zero; Sage empty set)
Fact 3 (discrete physical ground state):          N_pair = 1 ⇒ P_vac = −0.688 ≠ 0  ⇒ OFF equilibrium
Fact 4 (gapped substrate ⇒ no topological zero):  N₃ = 0 (BDI), NOT N₃ = 2 (3He-A Fermi-point)
                                                  ⇒ NO topological protection of ρ_vac to 0 (Volovik Paper 03 Thm 1)

Substitute: the OBSERVED Λ is the value AT the off-equilibrium point, supplied by C10:
        ρ_observed = M_Pl²·H²        [C10 tracking ansatz; H > 0 ⇒ ρ_observed ≠ 0]
        Is ρ_observed forced to 0 by the equilibrium identity?  → NO (Sage: bool == 0 → False)

Direction: ρ_vac(eq) = 0 is a BOUNDARY/REFERENCE value the substrate approaches only as N≫1.
           The substrate is gapped (N₃=0) and discrete (N_pair=1), so it sits OFF that reference.
           ⇒ the observed-Λ magnitude is fixed by the tracking law (C10), NOT by the equilibrium identity.
```

**Verdict on Reading B**: **CORRECT as a sufficiency constraint.** The equilibrium identity is a statement about a point the substrate provably never reaches (no interior q-equilibrium; off-equilibrium at the discrete ground state; no topological protection to lock the zero). Therefore the *observed* Λ's "not tuned" status cannot be inherited from the (unreachable) equilibrium identity — it must be re-argued **at the tracking law**: what pins the residual to the observed magnitude rather than to an arbitrary off-equilibrium value? The answer is C10 (`ρ_vac ∼ M_Pl²H²`), which is itself tagged **ASSUMED-PARTIALLY-PROVEN** (knowledge MCP: "Scaling form ASSUMED at substrate-IS level (Volovik q-theory ansatz)"), and the external `H` it feeds is the same undelivered effective-Friedmann map as the §6.3 `a(t)` gap. **What Reading B governs: clause (B), observed magnitude — and it is C10-conditional, not identity-warranted.**

### II.3 Why both cannot be conflated (the structural core)

The decisive substitution-chain result this session: **`ρ_vac(eq) = 0` and `ρ_observed = M_Pl²H²` are different objects.** The equilibrium identity annihilates the ground-state energy at a reference point; the tracking law assigns the off-equilibrium value. Sage confirms the equilibrium identity does NOT force `ρ_observed` to 0 (`H > 0`). A single phrase "exactly zero, not tuned" that does not say *which* of these it is about is a scope-collision — structurally the same failure class the framework's own `α_s` row warns against (a single label conflating two scale-separated observables, `phononic-framing.md` exflation table). The substrate carries TWO CC statements: an *equilibrium-reference* zero (exact, identity-warranted) and an *off-equilibrium observed* magnitude (C10-warranted). Which one "exactly zero, not tuned" asserts is set by which clause it is read against — and the doc must tag it.

---

## III. What the q-equilibrium reference DOES license vs what it does NOT

Stated precisely so the doc-workshop can carry the boundary verbatim (this is the deliverable's central numbered output):

**LICENSED by the q-equilibrium identity (Reading A), with no C10 dependency:**

1. **Non-inheritance of the bare 114-OOM vacuum energy.** The container-EFT catastrophe (`Λ_eff ∼ 10^{114} Λ_obs`) sums zero-point modes *without* the `μq` subtraction. The substrate's `μq` subtraction is an exact, representative-independent thermodynamic identity (`ε − μq = −P = 0`). The bare term is removed by an *identity*, not a tuning. **This is the "vacuum energy test" pass** — and it is the framework's strongest superfluid-domain CC claim (currently under-sold in the doc per volovik-collab §IV).
2. **The equilibrium *reference* value is exactly 0, not ≈0.** `ρ_Λ(eq) = 0 M_KK⁴` EXACT (Sage-rational), not a numerically-small residual. This is what makes "exactly zero" (as opposed to "tuned to be small") a legitimate phrase — *for the reference*.
3. **The CC is the `a_0` (zeroth) spectral moment, structurally distinct from gravity (`a_2`, second moment).** The vacuum-energy channel is not the Einstein–Hilbert channel; the zero is in the right moment.

**NOT licensed by the q-equilibrium identity (must be re-scoped to C10 + external `H`):**

4. **The observed-Λ *magnitude* (`ρ_obs = 2.7×10⁻⁴⁷ GeV⁴`).** The substrate never sits at q-equilibrium (no interior zero; off-equilibrium at `N_pair=1`, `P_vac = −0.688 ≠ 0`). The observed value is the non-equilibrium tracking residual, fixed by C10 (`ρ_vac ∼ M_Pl²H²`, **ASSUMED-PARTIALLY-PROVEN**) closing to `ρ_vac/ρ_obs = 1.032` (DILUTION-CC-66) — *given* an external `H`. The "not tuned" status of *this number* rests on C10, not on the equilibrium identity.
5. **A from-`D_K` derivation of the dark-energy density.** The CC closure is **doubly conditional** — on C10 AND on the external `H` the tracking law feeds (the same undelivered `a(t)` map, §6.3). `1.032` is a genuine PASS *given* `H(t)`; it is not yet a substrate-derived dark-energy density. (The §7.1 doc already flags this at line 391 and §9 frontiers 5–6; the R4 clause must not contradict that honest framing by over-claiming the magnitude.)

**The clean one-line separation (for §7.1):** *the equilibrium identity warrants that the catastrophe is never inherited (exact, not tuned); the C10 tracking law — assumed, not derived — warrants the observed magnitude.* "Exactly zero, not tuned" is true of the **equilibrium reference / non-inheritance**, conditional of the **observed magnitude**.

---

## IV. Why the warrant is thermodynamic, not topological (the substrate-first reason)

Substrate-first per `phononic-framing.md` (explanation flows substrate → emergent; the CC warrant is a substrate-IS statement, not a container-thinking tuning argument):

The substrate IS the BCS condensate on Jensen-deformed SU(3) — a **fully gapped topological superfluid in the BDI class** (`N₃ = 0`, Pfaffian `Z₂ = −1`; the child of 3He-B by the inheritance morphism, NOT an analogy — `framework-3HeB-comparison §II.2`, `3HeB-inheritance-canonical`). The CC warrant's *kind* is fixed by this universality-class assignment:

- **3He-A (`N₃ = 2`, Fermi-point class)**: the vacuum energy is **topologically protected to zero** — the Fermi-point invariant forces it, robust against any symmetry-preserving deformation (Volovik Paper 03, Thm 1). If the substrate were 3He-A, "exactly zero" would be a *topological* statement, automatic and unconditional.
- **3He-B-class substrate (`N₃ = 0`, BDI)**: the `Z₂` Pfaffian protects the *gap* but **not the vacuum energy** (`framework-3HeB-comparison §II.2`: "The Z_2 protects the gap but not the vacuum energy... the CC problem exists precisely because the system is in the 3He-B universality class, not the 3He-A class"). The zero is a **thermodynamic (Gibbs–Duhem) equilibrium statement**, reachable only in the `N ≫ 1` limit — and the substrate is discrete (`N_pair = 1`), so it sits off that limit by construction.

This is the deepest substrate reason the two-clause split is *forced*, not stylistic: with topological protection (3He-A), clause (A) and clause (B) would coincide (the zero is locked and attainable). Without it (3He-B), clause (A) is an exact *reference identity* and clause (B) is an *off-equilibrium magnitude* governed by relaxation dynamics — they necessarily separate. The gate's own §W5-3 Substrate-physics assessment flags exactly this ("the q-theory equilibrium identity is the *thermodynamic* warrant (Gibbs-Duhem), not a topological one"); the W5-3 PASS is honestly scoped at the gate level. The audit's contribution is to ensure that honesty propagates into the §7.1 doc wording, where the compressed phrase risks losing it.

The corpus is fully self-consistent on this: `framework-3HeB-comparison §II.3` already states the skeptical reading in plain terms — *"The system cannot reach exact equilibrium. The CC gap of 113 orders is the cost of discreteness... The equilibrium theorem applies in the thermodynamic limit (N ≫ 1), not at N = 1."* The W5-3 gate, the comparison document, and this audit agree. The only place the boundary was at risk of being lost is the *compression* into the §7.1 one-phrase caveat — which is what the in-session edits below fix.

---

## V. Effect on the solution space

- **No wall moves.** W5-3 PASS stands (the equilibrium identity is exact). DILUTION-CC-66 stands (PROVEN). C10 stands at its existing status (**ASSUMED-PARTIALLY-PROVEN** — unchanged; this audit does not promote or demote it).
- **A sufficiency boundary is pinned.** The corridor "the equilibrium identity warrants the *observed-Λ* 'not tuned' claim" is **CLOSED** — the identity warrants *non-inheritance* only; the observed-magnitude claim is C10-conditional. This sharpens the §7.1 wording and prevents a downstream over-claim (a future verbiage gate asserting the observed-magnitude clause must cite C10 + external `H`, not the equilibrium identity).
- **The framework's strongest CC claim is correctly surfaced.** The non-inheritance / vacuum-energy-test pass (clause A) is exactly warranted and should be stated as a *strength*, not buried in a caveat — consistent with volovik-collab §IV's "under-sold" finding. The honest split *strengthens* the document: it lets clause (A) be claimed at full force precisely because clause (B) is honestly bounded.
- **Cross-axis consistency with W5-6.** The τ-flow/q-flow registry note (W5-6, A16) already establishes that the CC layer rests on the *q-flow* equilibrium theorem, not the τ-ramp. This audit is the magnitude-vs-reference refinement *within* the q-flow leg: the q-flow identity gives the reference zero; the q-flow tracking law (C10) gives the observed magnitude. No tension with W5-6.

---

## VI. In-session non-math actions EFFECTED (per directive — not deferred)

Both non-math items are effected at the **doc-integration source** the §7.1 doc-workshop consumes (`phonic-exflation-equation-volovik-collab.md`, the clause-R4 authority per housekeeping A17). The §7.1 edit itself lands in the curated doc via the routed doc-`/rclab-workshop` (curated-doc track per A17); sharpening the *source* is the correct in-session action — the workshop transcribes the sharpened clause.

1. **Sharpened §7.1 clause-R4 wording** — `sessions/framework/Collabs/phonic-exflation-equation-volovik-collab.md` §III (R4). The prior one-clause wording ("...the only question is the *non-equilibrium residual* — and the tracking vacuum closes that to 1.032") is replaced with the **two-clause split**: (i) the equilibrium identity makes the *equilibrium* vacuum energy exactly zero by an *exact thermodynamic identity, not a tuning* (W5-3 PASS, Sage-rational 0) ⇒ the bare 114-OOM term is *not inherited*; (ii) explicit scope — *thermodynamic not topological* (3He-B `N₃=0` vs 3He-A `N₃=2` Paper 03 Thm 1), `ρ_Λ=0` is a *reference not an interior point* (S62 #19 no interior eq; `N_pair=1` off-eq), and the *observed* magnitude is the C10 tracking residual (**ASSUMED-PARTIALLY-PROVEN**), so the closure is *doubly conditional* (C10 + external `H`, §6.3). Rationale updated to name the S-4 audit and the two-clause separation.

2. **CC-warrant scoping note** — same file §IV (new constraint-map bullet) + §V.3 gate sharpening. §IV bullet states the post-W5-3 sufficiency boundary: the PASS licenses clause (A) non-inheritance only, NOT clause (B) observed-magnitude; warrant is thermodynamic not topological. §V.3 gate is annotated **CLOSED by W5-3** with the explicit sufficiency boundary (equilibrium-value-=0 PASS does NOT license the observed-magnitude clause; a future verbiage gate asserting the magnitude must cite C10 + external `H`).

*(No edit to the curated `phonic-exflation-equation.md` itself: per housekeeping A17, the §7.1 R4 correction is routed to the doc-`/rclab-workshop` (curated-doc = separate doc-integration track). The §7.1 doc already flags the CC closure as "doubly conditional" at line 391 and lists C10/SDW-convergence as open frontiers §9 items 5–6 — so the doc is already consistent with this audit; the workshop will fold in the sharpened R4 clause from the now-updated source. Editing the curated doc directly here would bypass the routed workshop and violate the doc-integration track separation.)*

---

## VII. Carry-forward computation (4-field spec)

Only ONE genuine forward computation is implied (the non-math items are effected above; this is genuine future physics per `feedback_fix-in-session-never-defer.md`).

### CF-S96-C10-TRACKING-LAW-SUBSTRATE-DERIVATION — derive the C10 exponent `n=2` (`ρ_vac ∼ M_Pl²H²`) from substrate q-theory, not assume it

1. **What**: Promote C10 from **ASSUMED-PARTIALLY-PROVEN** toward PROVEN by deriving the tracking-law exponent `n` in `ρ_vac ∼ H^n` from the substrate q-theory relaxation dynamics (Volovik Papers 14/25: `ρ_vac ∼ |H|·Λ_QCD³`-type forms give specific exponents per the conserved-charge relaxation rate). Specifically: compute `n_eff = 2 + (correction from GGE pressure)` (the form flagged in `session-66-mack-transit-workshop` eq T.61) from the substrate's off-equilibrium `dρ_vac/dt` near the discrete `N_pair=1` ground state, and test whether `n = 2` is *forced* by the q-flow relaxation (which would make clause (B) substrate-derived) or is a free ansatz (which keeps it conditional). This is the gate that would let clause (B) inherit substrate warrant rather than remaining C10-conditional.
2. **Inputs**: `framework-3HeB-comparison §III.1` (q-theory CC self-tuning form); Volovik Paper 14 Eq.(6.3) (`ρ_vac ∼ |H|Λ_QCD³`) + Paper 25 Sec V (the `M_Pl²H²` tracking form); S62 `s62_cc_qtheory_gge.npz` (the `ε(q)`, `dE_ZP/dq` cache, off-equilibrium slope at `N_pair=1`); `canonical_constants.py` (`rho_Lambda_obs=2.7e-47`, `M_Pl_reduced`, `n_pairs`); C10 provenance (`atlas-04-assumptions`). **Depends on**: W5-3 `EQUILIBRIUM-CC-WARRANT` PASS (the equilibrium reference this CF measures departure from) — UPSTREAM GATE, audit_sha256 `397cf449…`.
3. **Gate**: `S96-C10-TRACKING-EXPONENT-ORIGIN`, `[CHAIN]`. PASS iff the substrate q-flow relaxation *forces* `n = 2` (`|n_derived − 2| < 0.1`, with the GGE-pressure correction quantified) AND the resulting `ρ_vac(today)/ρ_obs` reproduces the DILUTION-CC-66 `1.032` to within its stated band — i.e. C10 is substrate-derived, not assumed. INFO iff `n` is computed but the closure depends on the still-external `H` (clause B remains C10-conditional but the *exponent* is no longer free). FAIL iff `n` is unconstrained by the substrate (C10 stays a pure ansatz). Note: even on PASS, the external-`H` (`a(t)`) dependency of clause (B) persists until the §6.3 effective-Friedmann map is closed — so this CF sharpens but does not by itself fully discharge the double-conditionality.
4. **Effort**: ~1 wave-equivalent (symbolic q-theory relaxation derivation + S62 cache off-equilibrium-slope read; Sage-checkable; no large eigensolve).

*(Not a workshop per `Investigating-Workshops.md` Q1: this is a solo COMPUTE with a pre-registered threshold and machinery pin, not a competing-readings adjudication — route to `/rclab-plan` S96, not the workshop schedule. It is genuine NEW physics (derive a currently-assumed exponent), so it is a math CF, not a §B hygiene item.)*

---

## VIII. Verdict summary

- **W5-3 PASS stands** — the `ρ_Λ(eq) = 0` identity is exact, representative-independent, Sage-rational. NOT re-opened.
- **Clause-R4 "exactly zero, not tuned" is WARRANTED by the equilibrium identity ALONE for the NON-INHERITANCE clause** (the bare 114-OOM term is removed by an exact identity, not a tuning — the vacuum-energy test pass) **and must be RE-SCOPED to the C10 tracking law for the OBSERVED-MAGNITUDE clause** (the substrate never reaches q-equilibrium; the observed Λ is the non-equilibrium tracking residual, C10-conditional, ASSUMED-PARTIALLY-PROVEN).
- **The q-equilibrium reference LICENSES**: non-inheritance of the bare vacuum energy (the 114-OOM non-inheritance), the exact-not-≈ reference zero, and the `a_0`-moment placement. **It does NOT license**: the observed-Λ magnitude or a from-`D_K` dark-energy-density derivation (both re-scoped to C10 + external `H`).
- **The warrant is thermodynamic (Gibbs–Duhem), not topological** — forced by the 3He-B-class (`N₃=0`, BDI) inheritance, contrasted with 3He-A (`N₃=2`) Fermi-point protection (Volovik Paper 03 Thm 1).
- **In-session edits effected** (clause-R4 sharpening + CC-warrant scoping note + §V.3 gate sharpening, all in the doc-integration source `phonic-exflation-equation-volovik-collab.md`).
- **One math CF** (`CF-S96-C10-TRACKING-LAW-SUBSTRATE-DERIVATION`) — derive the C10 exponent from substrate q-theory so clause (B) can inherit substrate warrant rather than remaining a pure ansatz.

**Solution-space meaning**: the framework's CC story is stronger than the compressed §7.1 phrase let it claim *for clause (A)* (non-inheritance is exact, not tuned — state it as a strength) and exactly as conditional as the doc's own §9 frontiers say *for clause (B)* (observed magnitude is C10-and-`H`-conditional). The two-clause split is not a hedge — it lets the framework claim its genuine vacuum-energy-test win at full force while keeping the observed-magnitude claim honest. The next computable question is whether the C10 exponent `n=2` is substrate-forced (CF-S96).
