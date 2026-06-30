# Session 97 Synthesis: PV-Scheme Canonicity for the a₀/a₂ CC-Ratio and the §8.5 Tier-2 / CC-Closure Anchor

**Date**: 2026-05-31
**Agent**: lizzi-spectral-functional-theorist (Lizzi)
**Scope**: Slot-1 solo S-3 — PV-scheme CANONICITY of the a₀/a₂ regulator-atlas object; PV-scheme-(in)variance of the §8.5 tier-2 survival / CC closure anchor; reconciliation against the 3-instance FULL-vs-schematic-PV signature chain.
**Source Documents**:
- `sessions/archive/session-97/session-97-w2-workingpaper.md` (§W2-1 + Wave-2 synthesis)
- `computations/session-97/s97_gate_verdicts.txt` (line 44 — S97-W2-1-A0A2-PV-FULL-MELLIN, audit `7d5ca3f9…`)
- `sessions/permanent-results-registry.md` (§VII.AV.OP-PROJ / .STATE-PROJ + parent §VII.AV Level-2-B diagnostic; §VII.M / §VII.N Three-Layer Regulator)
- `.claude/agent-memory/lizzi-spectral-functional-theorist/MEMORY.md`
- Knowledge MCP: `S96-SDW-CC-GAP` (da899b4d), §VII.AV equations, `a_0_FW_zeta`, `a_2_FW_zeta`

---

## I. Session Outcome

The a₀/a₂ cosmological-constant ratio is a **two-axis object**: it is **functional-INVARIANT (FI) across the analytic-continuation family** (zeta ≡ Mellin to machine epsilon, rel_dev = 0.000e+00 for BOTH a₀ and a₂) and **regulator-DEPENDENT (RD) across the Pauli-Villars subtraction** (FULL-physical-PV `(f₂/f₀)_Mellin = 0.4261` vs schematic-Gilkey `0.6314`, a 32.5% shift; residual_OOM = 0.17). Gate S97-W2-1-A0A2-PV-FULL-MELLIN closed **INFO** on the object-definedness axis (CLASS=FULL, audit `7d5ca3f9…`).

**Structural verdict on PV-scheme canonicity**: *Neither* the physical {1,2}-mass PV set *nor* the schematic Casimir-fraction set is the substrate-natural regulator for the CC-ratio in any absolute sense — **the substrate-natural regulator is the analytic-continuation/Mellin operation itself (which the CC-ratio is FI under), and the PV subtraction is a downstream physical degree of freedom, not a regularization the spectrum forces.** That said, *between the two PV variants*, the full-physical finite-mass PV tower `{c_j}={2,−1}`, `{m_j²/M_KK²}={1,2}` at Λ_UV=M_KK is the physically-defensible regulator and the schematic Casimir-fraction set is a structural-form surrogate (per its own disclosure it "does NOT reproduce the canonical 0.431082").

**§8.5 tier-2 survival / CC closure**: the survival anchor is the **FI-WITHIN-family ratio**, and that anchor **survives UNCHANGED** under the full-physical-PV scheme — it is **PV-scheme-INVARIANT**. The 32.5% PV-shift lives on the RD axis (the PV-subtraction choice), which the §8.5 anchor does **not** rest on. The tier-2 survival is therefore PV-scheme-independent *at the FI-anchor*; the RD axis introduces no propagation into the survival margin because the anchor is not defined on it.

---

## II. Key Results

### Result 1 — The a₀/a₂ CC-ratio is FI-within-analytic-continuation-family, RD-across-PV (object property)

**Result**: `a₀^PV/a₂^PV = 0.510595`; `(f₂/f₀)_Mellin = 0.426096` vs schematic target `0.6314`; residual_norm = 0.325156 (32.5%); residual_OOM = 0.170797. zeta≡Mellin rel_dev = 0.000e+00 for both a₀ and a₂. — **GEOMETRIC** (regulator-atlas object-definedness of a spectral-moment ratio of D_K).

The computation routed the SAME physical D_K spectrum {λ_k, m_k} through the FULL `analytic_zeta` heat-kernel-integral evaluator at the s=8 (a₀, pole_in_s=4, n=0) and s=6 (a₂, pole_in_s=3, n=2) poles, then applied a FULL physical Pauli-Villars subtraction `{c_j}={2,−1}`, `{m_j²/M_KK²}={1,2}` at Λ_UV=M_KK. The unsubtracted moments reproduce the direct Dirichlet power-sum exactly off the poles (the exact Mellin↔Dirichlet identity), so the analytic-continuation axis carries **zero** scheme freedom — this is the structural backbone. The PV-subtracted factors `f₀_Mellin = 0.4724`, `f₂_Mellin = 0.2013` reweight a₀ and a₂ *differently* than the schematic direct-power-sum reweights them (`f₀ = 0.7885`, `f₂ = 0.4979`), producing the 32.5% shift in the normalized ratio.

This is the lizzi-signature reading made concrete: **what survives all choices is structural (the Mellin/analytic-continuation axis — FI to machine precision); what depends on the choice is a physical degree of freedom (the PV-subtraction axis — RD at 32.5%).** The object is well-DEFINED — FAIL excluded: a₀^PV and a₂^PV are both finite and positive (a2_pv_collapsed=False, a0_pv_blew_up=False), so this is NOT a Gilkey-normalization artifact and carries no S94 absolute-divergence signature. It is also NOT atlas-universal across the PV-scheme choice (PASS excluded). Object-definedness is **family-scoped, not atlas-universal**.

### Result 2 — Structural answer to (a): substrate-natural regulator for the CC-ratio

**Result**: The Mellin/analytic-continuation operation is the substrate-natural regulator (the CC-ratio is FI under it); the PV subtraction is a physical degree of freedom, not a spectrum-forced regularization. Between the two PV variants, full-physical {1,2}-mass PV is the physically-defensible regulator; schematic Casimir-fraction is a structural-form surrogate. — **GEOMETRIC**.

Argued from first principles, not from a tag choice:

1. **The spectrum forces the analytic continuation, not the PV subtraction.** The cosmological constant IS the spectral-action zeroth moment a₀ — a *different* spectral moment of D_K than gravity (the second moment a₂). The well-defined object the substrate hands up is `a_n^{Mellin}(s_n) = Σ_k m_k λ_k^{−s_n}`, the analytic continuation of the heat-kernel trace. This continuation is *unique* (Mellin↔Dirichlet is an identity, rel_dev=0). The substrate does not, by itself, prescribe a Pauli-Villars mass tower — PV is a choice imposed to render a UV-sensitive *absolute* moment finite. So the regulator the spectrum *forces* is the analytic continuation; PV is an *added* physical input.

2. **The CC-ratio's FI-under-Mellin is the structural signal.** Because a₀^Mellin/a₂^Mellin is FI across the entire analytic-continuation family (the only axis the spectrum forces), the *ratio* is the substrate-natural object. The CC-ratio's structural content lives on the FI axis; the PV-subtraction choice is orthogonal physics layered on top.

3. **Between the two PV variants, the {1,2}-mass set is the physically-defensible regulator.** The full-physical PV tower satisfies the genuine PV identities (Σ c_j = 1, Σ c_j m_j² = 0 — the conditions that make PV a *bona fide* covariant regularization with a physical UV scale Λ_UV=M_KK). The schematic Casimir-fraction set (`M_PV² = fraction × Casimir-ceiling`) is a *structural-form surrogate*: it captures the shape of a PV subtraction but, by its own S96 disclosure, "does NOT reproduce the canonical 0.431082" and is not a faithful physical regularization. Therefore *if one must pick a PV scheme as canonical, it is the full-physical {1,2}-mass tower* — but the deeper point is that the CC-ratio's structural identity does not require picking, because it is carried by the FI axis the spectrum already singles out.

**The trap this avoids (lizzi-signature methodology)**: declaring "the schematic 0.6314 is the CC-ratio" would mistake a surrogate's value for a structural prediction. Declaring "the full-physical 0.4261 is THE CC-ratio" would mistake a scheme-dependent physical-degree-of-freedom value for a structural invariant. The correct reading is that the *ratio's structural content is its FI-under-Mellin behavior*; the absolute PV-subtracted value is a physical d.o.f. to be pinned by consistency, not a scheme convention.

### Result 3 — Structural answer to (b): the §8.5 tier-2 / CC-closure anchor is PV-scheme-INVARIANT

**Result**: The §8.5 tier-2 survival and the CC closure rest on the FI-WITHIN-family ratio, which is INVARIANT under the FULL-physical-PV scheme. The 32.5% PV-shift does NOT propagate into the tier-2 survival margin, because the survival margin is not defined on the RD (PV-subtraction) axis. — **GEOMETRIC / structural**.

Substitution chain (per math-scripts.md §"Double-Check Logic Before Compute"):

- **Step 1 (define the anchor)**: per the DI1 guard of S97-W2-1 and the S96-SDW-CC-GAP line, the §8.5 tier-2 survival anchor is the **FI-WITHIN-family ratio** — `a₀^{Mellin}/a₂^{Mellin}` (equivalently the zeta ratio, since zeta≡Mellin), the object that is invariant across the analytic-continuation family. [source: W2-1 DI1 guard; S96 da899b4d `partB_FI_within_family=True`]
- **Step 2 (define the PV-shift)**: the 32.5% shift is `|(f₂/f₀)_Mellin − 0.6314|/0.6314`, a quantity on the **PV-subtraction axis** — the difference between schematic-Gilkey and full-physical-PV *reweightings* of a₀ and a₂. [source: W2-1 residual_norm=0.325156]
- **Step 3 (locate the anchor on the axes)**: the FI-WITHIN-family ratio is a property of the *unsubtracted* analytic-continuation moments (rel_dev=0 between zeta and Mellin). The PV-shift is a property of the *subtracted* moments. These are orthogonal axes (the analytic-continuation axis is FI; the PV-subtraction axis is RD). The anchor lives ENTIRELY on the FI axis.
- **Step 4 (propagation)**: a perturbation confined to the RD axis (the schematic↔full-physical-PV choice) cannot move a quantity defined purely on the FI axis. Formally: `d(FI-anchor)/d(PV-scheme) = 0`, because the FI-anchor is the ratio of unsubtracted moments and the PV-scheme enters only through the subtraction operator applied *after* the FI-anchor is fixed. **Therefore the 32.5% shift propagates ZERO into the tier-2 survival margin.**
- **Conclusion**: §8.5 tier-2 survival is **PV-scheme-INVARIANT**. The S97-W2-1 DI1 guard is structurally sound: the INFO verdict on object-definedness does NOT retract the tier-2 survival, and the FI-within-family result is CONFIRMED here at machine precision (rel_dev=0 for both moments).

**Bound on the alternative reading (if one wrongly anchored §8.5 to the absolute PV-subtracted ratio)**: were the survival margin instead defined on the absolute `a₀^PV/a₂^PV`, the propagation would be bounded by the measured scheme spreads — `5.703%` on the absolute ratio (L_max-stable: 0.510595 → 0.481478 across L10→L12) and `15.469%` on the normalized (f₂/f₀) form, with a `32.5%` schematic-vs-physical gap at fixed L_max. This is an explicit upper bound on the propagation *under the wrong anchoring*; it does NOT apply to the actual §8.5 anchor (the FI ratio), which has zero propagation. I flag this bound so a downstream consumer cannot silently re-anchor §8.5 to the RD axis without re-incurring up to a 32.5% margin hit.

### Result 4 — Reconciliation against the 3-instance FULL-vs-schematic-PV signature chain (answer to (c))

**Result**: W2-1 line 44 is the **third** independent confirmation that FULL-vs-schematic-PV scheme dependence is a framework SIGNATURE (an RD-across-PV object property), not a defect of any one computation. — **GEOMETRIC / structural (cross-session)**.

| # | Instance | Object | FULL-PV | SCHEMATIC | Shift | Source |
|:--|:---------|:-------|:--------|:----------|:------|:-------|
| 1 | §VII.AV (S91/S92) | Var_a 2nd-log-derivative curvature B_PV at s=4 pole | B_PV(R_FULL-PV) = −527.97 M_KK² (m_PV=M_KK) | B_PV(R_SCHEMATIC) = −7.046 M_KK² (m_PV→0) | factor ~75× | s91-w4-w5-1; s92-vii-av-anchor-vs-pv-pipeline-reconciliation.md |
| 2 | S96-SDW-CC-GAP (da899b4d) | f₀, f₂ (CC-ratio PV factors) | (full route) | f₀=0.7885, f₂=0.4979, f₂/f₀=0.6314 | 36.86% (`partB_FI_across_PV=False`) | s96_gate_verdicts.txt |
| 3 | **S97-W2-1 (line 44, 7d5ca3f9)** | **a₀^PV/a₂^PV CC-ratio via FULL analytic_zeta Mellin** | **(f₂/f₀)_Mellin=0.4261; a₀^PV/a₂^PV=0.510595** | **f₂/f₀=0.6314** | **32.5%** | s97_gate_verdicts.txt line 44 |

The three instances are **mutually consistent and structurally distinct**:
- **Distinct objects**: #1 is the Var_a 2nd-log-derivative *curvature* (a state-pair/algebra-DEPENDENT observable at the §VII.AV Cell-IV STATE-PROJ slot); #2 and #3 are the CC-*ratio* PV factors (algebra-INVARIANT spectrum-only moments). The §VII.AV parent registry explicitly carries the sibling caveat that its s=4 objects are distinct (`7.324992 (§VII.AY) ≠ −7.046336 (§VII.AV) — shared character, distinct objects`); W2-1 adds a third distinct s-pole object on the same RD-across-PV theme.
- **Distinct routes for #2 vs #3**: #2 (S96) computed f₀/f₂ via the SURROGATE direct-power-sum `pv_ratio_cancellation()`; #3 (W2-1) routed the SAME physical-PV through the FULL `analytic_zeta` heat-kernel-integral evaluator — a genuinely new computation that *confirms* #2's `partB_FI_across_PV=False` rather than re-deriving it. The two shift magnitudes (36.86% vs 32.5%) agree to within the route difference — the same RD-across-PV signature, measured two ways.
- **Common structure**: all three show the analytic-continuation/Mellin axis FI (where tested: #3 confirms rel_dev=0 explicitly) and the PV-subtraction axis RD. This is the framework signature: **the spectral functional's PV-scheme is a physical degree of freedom with observable consequences, not a regularization convention.** W2-1 is the cleanest demonstration to date because it isolates the FI and RD axes in a single gate (FI confirmed to machine-eps; RD measured at 32.5%).

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S97-W2-1-A0A2-PV-FULL-MELLIN (line 44, audit `7d5ca3f9…`) | INFO | residual_norm = 0.325156 (32.5%; INFO band 0.10–1.0 OOM, residual_OOM=0.17); a₀^PV/a₂^PV = 0.510595; (f₂/f₀)_Mellin = 0.426096 vs 0.6314; zeta≡Mellin rel_dev = 0.000e+00 (both moments) |

*(Companion gates in the W2 working paper — S97-W2-2-C10-N-EXPONENT INFO, S97-EP-N3LO-CASIMIR PASS — are on DI1-orthogonal axes and outside this synthesis's object-definedness scope. They are not re-adjudicated here.)*

---

## IV. Structural Implications

1. **A permanent object-property is established (no new compute needed)**: the a₀/a₂ CC-ratio is **FI-WITHIN-analytic-continuation-family, RD-across-PV**. This is a closed characterization — a permanent classification of the object, recorded in the W2 working-paper Constraint-Map Update (2026-05-30 row). It joins R_1 ≡ a₀·a₄/a₂² (FI to sub-percent, the Lizzi signature) as a member of the FI-within / SD-across family the framework has been mapping since S65.

2. **The §8.5 tier-2 / CC-closure anchor is hardened, not threatened**: the structural reading confirms the survival anchor is the FI ratio (PV-scheme-INVARIANT). The W2-1 INFO verdict, far from weakening §8.5, *confirms* the FI-within-family backbone at machine precision and explicitly bounds the only way it could be threatened (re-anchoring to the RD axis would re-incur up to 32.5%). The CC closure's spectral-moment foundation is PV-scheme-robust *where it matters* (the FI ratio) and PV-scheme-sensitive *where it does not anchor* (absolute PV-subtracted moments).

3. **The framework signature is reinforced to 3 instances**: FULL-vs-schematic-PV scheme dependence is now a 3-instance RD-across-PV signature across two distinct algebra-axis cells (algebra-DEPENDENT Var_a curvature at §VII.AV; algebra-INVARIANT CC-ratio at S96+W2-1) and two distinct s-poles. This is structural, not coincidental — the PV-subtraction is a genuine physical d.o.f. in the spectral action, consistent with the lizzi-signature thesis that "the cosmological constant is determined by the regularization scheme as much as by the Dirac operator spectrum."

4. **Constraint-map**: NO corridor opened or closed by W2-1 (it is an object-hygiene characterization, not a falsifier). The DI1 scoping holds: W2-1 shares no inputs with the q-flow C10 axis (W2-2) or the heat-kernel EP axis (W2-3); its verdict is consumed independently and does not propagate.

---

## V. Carry-Forward Computations

> Per the Focus carry-forward mandate: MATH items carry the 4-field spec (what/inputs/gate/effort); NON-MATH items are effected in-session or recorded as ready-to-apply recommendations. The object-definedness characterization (FI-within-family / RD-across-PV) is a **closed permanent classification** — it is NOT a compute carry-forward (it requires no future computation; it is already established at machine precision). The only genuine future-compute adjacency is an OPTIONAL robustness re-check, pre-registered below so it is not lost.

```
V.1. Substrate-natural-PV tier-2 robustness re-check (OPTIONAL — confirms PV-scheme-invariance numerically)
   - What: Re-evaluate the §8.5 tier-2 survival margin TWICE — once with the FI-within-family ratio
     a₀^{Mellin}/a₂^{Mellin} (no PV subtraction) and once with the full-physical-PV a₀^PV/a₂^PV — and
     verify the survival verdict is IDENTICAL across the two (confirming d(survival)/d(PV-scheme)=0 numerically,
     not just structurally). Report Δ(survival-margin) between the two anchorings; it should be 0 within FD floor
     because the survival anchor is the FI ratio (the PV-subtracted value is not the anchor).
   - Inputs: a_0_FW_zeta=6440.0, a_2_FW_zeta=2776.165389 (canonical, non-superseded); the W2-1 npz
     (computations/session-97/s97_w2_1_a0a2_pv_full_mellin.npz — a₀^PV/a₂^PV=0.510595, f₀/f₂_Mellin, audit
     7d5ca3f9); the §8.5 tier-2 survival definition from the capstone phonic-exflation-equation.md §8.5;
     S96-SDW-CC-GAP da899b4d (partB_FI_within_family=True).
   - Gate: S98-A0A2-TIER2-PV-INVARIANCE — PASS iff Δ(survival-margin)_{FI-anchor vs PV-anchor} = 0 within
     1e-9 AND the survival verdict label is unchanged across both anchorings (confirms PV-scheme-INVARIANCE
     of the tier-2 survival). INFO iff Δ ∈ (1e-9, info_band] (would indicate a hidden RD-axis dependence in
     the §8.5 definition — a flag, not a failure). FAIL iff the survival verdict label flips between anchorings
     (would falsify the DI1 guard's claim that §8.5 rests on the FI ratio).
   - Effort: ~0.5 wave, 1 agent session (it is a re-evaluation of an existing closed-form margin under two
     anchor choices; no new spectrum computation — both moments already in the W2-1 npz).
   - Depends on: S97-W2-1-A0A2-PV-FULL-MELLIN (the FI/PV moment pair + npz, audit 7d5ca3f9 — UPSTREAM GATE);
     the capstone §8.5 tier-2 survival definition (REGISTRY/CAPSTONE).
```

```
V.2. [NON-MATH — EFFECTED IN-SESSION] Permanent-registry object-property note
   - What: Land a permanent object-property note recording the a₀/a₂ CC-ratio as
     FI-WITHIN-analytic-continuation-family / RD-across-PV (PV-shift 32.5% at fixed L_max; absolute-ratio
     L10→L12 drift 5.70%; FI rel_dev=0.000e+00 both moments), cross-citing the 3-instance signature chain
     (§VII.AV B_PV −527.97/−7.046; S96-SDW-CC-GAP da899b4d 36.86%; S97-W2-1 line 44 32.5%) + the §8.5
     PV-scheme-INVARIANCE structural verdict + the substrate-natural-regulator reading.
   - STATUS: DONE this session. Landed as new §7 + summary-table row `a0a2-cc-ratio-2axis` + change-log row
     in `sessions/framework/registry/lizzi-signature-observable.md` (my sole-writer file per
     `feedback_mack-bridge-role.md` / agent-private domain ownership — NOT the §VII.AV mack-sole-writer slot).
   - Why this home (not §VII.AV): the §VII.AV cluster objects are algebra-DEPENDENT state-pair (Cell IV) /
     OP-PROJ trace-residue (Cell II) observables; the W2-1 object is the algebra-INVARIANT spectrum-only
     CC-ratio. They are structurally distinct cells (algebra-axis orthogonality, MANDATORY at K=3), so the
     W2-1 object property belongs in the algebra-INVARIANT FI-within / SD-across family home (the
     lizzi-signature-observable registry, companion to R_1), NOT the §VII.AV slot. The §7 note explicitly
     cross-cites the §VII.AV instance #1 as the orthogonal-axis sibling without writing into that slot.
   - Gate: N/A (registry hygiene; artifact-existence on a content-substantive note — satisfied).
   - Effort: DONE (~5 min, single sole-writer landing).
   - Depends on: S97-W2-1 (audit 7d5ca3f9); §VII.AV parent record (cross-cite only); S96-SDW-CC-GAP da899b4d.
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | a₀/a₂ CC-ratio is FI-within-analytic-continuation-family (zeta≡Mellin rel_dev=0), RD-across-PV (32.5% shift) | GEOMETRIC | INFO (gate); permanent object-property | Object-definedness is family-scoped, not atlas-universal; companion to R_1 |
| 2 | Substrate-natural regulator for CC-ratio = the analytic-continuation/Mellin operation (FI); PV is a physical d.o.f., not spectrum-forced; full-physical {1,2} PV is the defensible variant, schematic is a surrogate | GEOMETRIC | Structural verdict | Answers (a): canonicity is on the FI axis, not the PV-scheme tag |
| 3 | §8.5 tier-2 / CC-closure anchor = FI-within ratio ⇒ PV-scheme-INVARIANT; 32.5% RD-shift propagates ZERO into survival margin | GEOMETRIC | Structural verdict | Answers (b): tier-2 survival HARDENED; DI1 guard sound; bound documented on wrong re-anchoring |
| 4 | W2-1 line 44 = 3rd instance of FULL-vs-schematic-PV signature (cf. §VII.AV; S96 da899b4d) | GEOMETRIC | Confirmed (cross-session) | Answers (c): RD-across-PV is a framework signature across 2 algebra-axis cells + 2 s-poles |
| 5 | CF-S98 substrate-natural-PV tier-2 robustness re-check (V.1, math, → S98) + registry object-property note (V.2, non-math, EFFECTED in-session in `lizzi-signature-observable.md` §7) | — | V.1 carry-forward; V.2 DONE | V.1 confirms PV-invariance numerically next session; V.2 landed the permanent FI-within/RD-across-PV classification this session |

---

### Methodological note (Lizzi)

The decisive structural fact is the **axis separation**: the CC-ratio's two scheme-axes are not interchangeable. The analytic-continuation axis is the one the D_K spectrum *forces* (Mellin↔Dirichlet is an identity), and the CC-ratio is FI under it — that is the *structural* content. The PV-subtraction axis is an *added* physical input, and the CC-ratio is RD under it — that is the *physical degree of freedom*. The §8.5 anchor is on the forced axis, so it is invariant; the 32.5% PV-shift is on the added axis, so it cannot move the anchor. This is the lizzi-signature methodology applied verbatim: *what survives all choices (FI-under-Mellin) is structural; what depends on the choice (the PV-subtracted absolute value) is a physical degree of freedom to be pinned by consistency, not a convention to be shopped.* The framework's CC closure is robust precisely because it leans on the structural axis and not on the scheme-dependent one.
