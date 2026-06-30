# Session 99 Synthesis: C10/CC Residual — Substrate Early-Vacuum Time-Profile vs the ΔN_eff < 0.107 Budget (X-cut, Tier-1 #2)

**Date**: 2026-06-04
**Agent**: mack-cosmic-bridge (Katie Mack — Cosmic Bridge)
**Source Documents**:
- `downloads/research-sweep-s99/dark-energy-observational/00-INDEX.md` (Channel-5 BBN top-up: papers 09 Allali-Notari-Rompineve, 10 Seto-Toda, 11 Goldstein-Hill)
- `downloads/research-sweep-s99/emergent-spacetime-superfluid/00-INDEX.md` (q-theory sources: papers 02 Volovik f(R), 04 Klinkhamer-Savelainen-Volovik, 06 Klinkhamer-Volovik)
- `sessions/archive/session-99/session-99-litrev-dark-energy-mack.md` (R1, G2 — input, not authority)
- `sessions/archive/session-99/session-99-litrev-dark-energy-sagan.md` (R1, G2 — input, not authority)
- `sessions/archive/session-99/session-99-litrev-emergent-spacetime-volovik.md` (R1, G1 — input, not authority)
- `sessions/archive/session-99/session-99-litrev-emergent-spacetime-phonon-first.md` (R1, G1 — input, not authority)
- Canonical state via knowledge MCP (`get_constant`, `search_knowledge`, `query_entity`, `trace_entity`): gates `S98-MK3-2-BBN-VACUUM-FRACTION`, `S99-W2-BBN-RELIEF`, `S99-W2-RELAXATION-CLOSURE`, `S98-W2-2-RELAXATION-CLOSURE`, `S98-MK3-1-C10-SUBLEADING-SIGN`, `DILUTION-CC-66`; constants `delta_N_eff_vacuum_BBN_below`, `rho_vac_over_rho_rad_BBN_below`, `rho_vac_over_rho_obs`; open-channel Q29/Window-8; the S99 W2 working paper; the S100 W2 plan

---

## I. Session Outcome

This is a cross-cutting second-layer review of the C10/CC residual, not a compute session — **no gate verdict is re-adjudicated, no framework probability moves**. The deliverable is a relief-corridor map for the standing `S98-MK3-2-BBN-VACUUM-FRACTION = FAIL` (ΔN_eff(vacuum) = 2.0873) against the current state-of-the-art budget ΔN_eff < 0.107 (95% C.L., Goldstein-Hill paper 11), a 19.51× exceedance (Sage-exact). Every framework-state claim is anchored to canonical first; where the spawn Focus, the indexes, or the four R1 syntheses drift from the register, I flag it.

The single most consequential structural fact — and it sharpens the Focus's own framing — is this: **the framework's early-vacuum energy is a Volovik *tracking* vacuum, `rho_vac = alpha_V M_Pl^2 H^{n_eff}` with `n_eff = 1.978` ≈ 2, which is the radiation-like (all-history, near-constant-fraction) worst case BY CONSTRUCTION, not by an avoidable modelling choice.** During radiation domination H ∝ a^{−2}, so ρ_vac/ρ_rad ∝ a^{2(2−n_eff)} = a^{+0.0438} (Sage-exact) — nearly flat across cosmic history. The two time-profile relief corridors the Focus asks me to adjudicate (post-BBN production; EDE-like peaked-and-diluting) are **NOT refinements of this tracking law — they are departures from it.** An EDE-like profile would need ρ_vac to dilute *faster* than radiation (negative a-exponent); the canonical tracking vacuum dilutes *slower* (positive a-exponent), which is the opposite sign. So the corridor map's load-bearing verdict is: **the canonical mechanism sits on the radiation-like worst-case branch that papers 09/10/11 jointly exclude at extreme significance; relief requires the substrate to supply a *non-tracking* early-time ρ_vac(a), which is exactly what the q-theory sources (papers 02/04/06) and the live successor CF-S100-W2-1-QEQ-DRIVE bear on.**

A second consequential reconciliation: the Focus, the index Channel-5 framing, and the volovik R1 (§IV conflict 1) disagree about whether 0.107 is canonical. The phonon-first R1 has it right and I confirm it against the register: **0.107 is the EXTERNAL observational budget (Goldstein-Hill); 2.0873 is the framework's predicted value; they are directly comparable because the framework's S66 ΔN_eff formula and paper 11's Eq. 1 ρ_rad definition are bit-identical.** The volovik R1's instruction to "use the canonical fraction-test, not 0.107" is half-right (the *gate's pre-registered threshold* is the fraction-based 0.2271, correctly) and half-wrong (the *external falsification budget* the framework must ultimately clear IS 0.107, and pretending it is non-canonical understates the failure).

Third, a scope correction the corridor map turns on: **S99 W2 closed only the magnitude axis, not the time-profile axis.** Gate `S99-W2-BBN-RELIEF` (FAIL, audit `8fe0ef45…`) tested three *shrink-the-magnitude-at-fixed-full-BBN-presence* mechanisms — (a) a larger from-below Δn shift, (b) an epoch-dependent α_V, (c) a distinct dilution channel sub-selecting D_K modes — and found none substrate-justified. It did **not** test "shift ρ_vac production past BBN" or "ρ_vac is EDE-like and negligible at BBN." Q29/BBN-VOLOVIK-67 is tagged "additional-relief corridor CLOSED (structural)" — but that closure is scoped to the *magnitude* corridor S99 W2 actually ran. The time-profile corridors remain genuinely open and untested.

---

## II. Key Results

### II.1 — The canonical early-vacuum is a tracking vacuum: radiation-like by construction, not EDE-like

**Result**: `rho_vac = alpha_V M_Pl^2 H^{n_eff}`, `n_eff = 1.978111` (HARD from-below, S98 V.9, `divergence_type=A`). During radiation domination (H ∝ a^{−2}): ρ_vac/ρ_rad ∝ a^{2(2−n_eff)} = a^{+0.0438} (Sage-exact). Classification: **PHONONIC** (the a₀ Seeley-DeWitt zeroth spectral moment tracking the Hubble rate; `a_0_FW_zeta = 6440.0`, zeta-regulated — a DIFFERENT moment than gravity's a₂).

This is the structural pivot of the entire corridor map, and it must be stated against canonical precisely because the R1 syntheses (correctly, on their own terms) lean on the index's hopeful framing that the substrate profile "likely sits closer to the EDE-like (relieved) case" (mack R1 §II.4; sagan R1 §II.6). The register does not support that hope as the canonical reading. The canonical mechanism is `DILUTION-CC-66` Scenario B, the Volovik tracking vacuum ρ_vac ~ M_Pl² H² (`rho_vac_over_rho_obs = 1.032`, S66/S97). A tracking vacuum with n_eff exactly 2 is a *constant fraction* of the total density in every epoch where the dominant component sets H — that is the defining property of a tracking solution, and it is the radiation-like, all-history case in the paper-10 (Seto-Toda) taxonomy. The framework's `n_eff = 1.978 < 2` produces a small *positive* a-exponent (+0.0438), so the fraction shrinks weakly toward early times — this is the entire content of the "from-below relief direction" (`relief_factor = exp((n_eff−2)·X) = 0.414` over the BBN lever X = ln(H_BBN/H_0) = 40.2756).

The decisive sign check (substitution chain, Sage-verified):

```
Step 1: rho_vac/rho_rad propto a^{2(2 - n_eff)}     [radiation era H propto a^-2, tracking law H^n_eff]
Step 2: n_eff = 1.978111  =>  2 - n_eff = +0.021889  (POSITIVE)
Step 3: exponent = 2*(2 - n_eff) = +0.043778        (POSITIVE)
Step 4: positive a-exponent  =>  fraction GROWS toward late times (large a),
        SHRINKS toward early times (small a) -- this is "from-below relief"
Step 5: EDE-like REQUIRES the fraction to SHRINK toward late times (negative a-exponent),
        i.e. rho_vac diluting FASTER than radiation (rho_vac propto a^-n, n > 4).
        The canonical tracking vacuum has the OPPOSITE sign.
Conclusion: the canonical n_eff~2 tracking vacuum is radiation-like (near-flat fraction),
        NOT EDE-like. An EDE-like profile is a DEPARTURE from the tracking law, not a tuning of it.
```

This is why the C10 arm "currently treats ρ_vac as PRESENT at BBN with full magnitude 0.474" (both R1 syntheses note this as the worst-case *assumption*): it is not merely an assumption the framework happens to have made — **it is the direct consequence of the canonical tracking law.** Relabelling it as relievable by a time-profile argument requires the substrate to abandon n_eff ≈ 2 at early times, which is a substantive structural change to DILUTION-CC, not a free modelling latitude.

### II.2 — The 0.107 budget is external-and-comparable; the 19.51× exceedance is exact

**Result**: ΔN_eff(vacuum) = 2.0873 (canonical, `delta_N_eff_vacuum_BBN_below`); Goldstein-Hill (paper 11) ΔN_eff < 0.107 (95% C.L.) from N_eff = 2.990 ± 0.070; exceedance 2.0873/0.107 = 19.508 (Sage-exact). Classification: **PHONONIC** (the falsified quantity is the a₀ tracking-vacuum fraction at the radiation-dominated BBN epoch).

Convention reconciliation (this is the volovik-R1-vs-phonon-first-R1 conflict, adjudicated against the register):
- Paper 11 Eq. 1: `rho_rad = [1 + (7/8)(4/11)^{4/3} N_eff] rho_gamma`.
- Framework S66 formula: `Delta N_eff = (rho_vac/rho_rad)_BBN / [(7/8)(4/11)^{4/3}]`, with `(7/8)(4/11)^{4/3} = 0.227107` (Sage-exact).
- These use the IDENTICAL `(7/8)(4/11)^{4/3}` factor. There is **no convention mismatch**: 2.0873 and < 0.107 are directly comparable on the same N_eff axis. The volovik R1's claim (§IV.1) that "0.107 has no canonical match" conflates two distinct objects: the *gate's pre-registered PASS threshold* (the fraction-based 0.2271 = bound, correctly canonical and correctly what the gate tested against) versus the *external state-of-the-art falsification budget* (0.107, the current observational anchor the framework must ultimately clear). Both are real; they are not the same number and serve different roles. The phonon-first R1 (§IV) states this correctly: "0.107 is the EXTERNAL observational bound; 2.0873 is the framework's predicted value, which EXCEEDS the bound by ~19.5×."

Three-tier budget hierarchy (do not conflate; Sage-exact exceedances, reproduced from the R1 syntheses and confirmed):

| Budget | Source | Framework 2.0873 over-budget |
|:-------|:-------|:----------------------------:|
| 0.2271 | gate's own BBN element-abundance worst-case (the PASS threshold S98-MK3-2 tested) | 9.19× |
| 0.39 (free-streaming) / 0.46 (fluid), CMB-era | paper 09 (Allali-Notari-Rompineve, DESI+Planck+Pantheon+) | 5.35× / 4.54× |
| **0.107** (combined BBN+CMB+BAO, 95%) | **paper 11 (Goldstein-Hill, N_eff = 2.990 ± 0.070)** | **19.51×** |

The framework's gate currently fails its OWN threshold by 9.19×; against the most current combined-probe budget it fails by 19.51×. The radiation-like reading (which is the canonical reading, §II.1) is excluded at extreme significance.

### II.3 — S99 W2 closed the MAGNITUDE corridor only; the TIME-PROFILE corridor is untested

**Result**: `S99-W2-BBN-RELIEF = FAIL` (audit `8fe0ef45395c71d0233e5509cfaf0a3b10c5ec1758997cc57ea94e96d0e08949`); the three tested mechanisms (a)/(b)/(c) are magnitude-axis, fixed-full-BBN-presence. Open-channel Q29/BBN-VOLOVIK-67 tagged "CORRIDOR CLOSED (structural)" — scope: magnitude. Classification: **PHONONIC**.

The S99 W2-BBN-RELIEF gate (which I authored as mack-cosmic-bridge) tested exactly three relief mechanisms, each asking "what parameter shift, at full ρ_vac presence at BBN, would bring ΔN_eff down to 1?":

| Mechanism tested by S99 W2 | Required value to reach ΔN_eff = 1 | Substrate value | Axis |
|:--|:--|:--|:--|
| (a) larger from-below Δn | n_eff = 1.959839 (1.835× the substrate shift) | HARD 1.978111 | magnitude |
| (b) epoch-dependent α_V | α_V,BBN/α_V,0 = 0.479080 | single α_V (no z-dependence) | magnitude |
| (c) distinct dilution channel | 475 of 992 D_K modes | all 992 gravitate | magnitude |

All three hold ρ_vac PRESENT at BBN with full tracking magnitude and ask whether the *coefficient* can shrink. **None of the three is the post-BBN-production corridor (shift the production epoch) or the EDE-dilution corridor (change the a-scaling so ρ_vac is negligible at BBN).** The Q29 "CORRIDOR CLOSED (structural)" tag is therefore scoped to the magnitude corridor — it does NOT close the time-profile corridors, which S99 W2 never evaluated. This is the gap the corridor map (§IV) is built to surface, and it is the substantive correction to any reading (including a naive reading of the spawn Focus's "S99 W2-2 FAIL... no substrate-justified residual mechanism") that treats the BBN arm as having exhausted its relief options. It has exhausted the *magnitude* options; the *chronology/profile* options are open.

Note also a labelling precision the Focus inverts: the Focus says "S99 W2-1 FAIL closed the 'n=2 unforced attractor' corridor" and "S99 W2-2 FAIL [was] BBN from-below relief." Against the register, **`S99-W2-RELAXATION-CLOSURE` (the n=2-unforced-attractor closure) is W2-1 and `S99-W2-BBN-RELIEF` (the BBN from-below relief) is W2-2** — the Focus has the W2-1/W2-2 roles correctly mapped to content but the gate names are as canonical here. Both are FAIL; both close their respective corridors (relaxation-attractor and BBN-magnitude). The live math successor is `CF-S100-W2-1-QEQ-DRIVE`, which targets the W2-1 (relaxation attractor) leg — NOT directly the BBN arm.

### II.4 — q-theory sources supply candidate NON-tracking ρ_vac(a) profiles — but each must clear the early-time budget

**Result**: papers 02 (Volovik f(R), `ε_vac(H) = f(R=12H²)`), 04 (Klinkhamer-Savelainen-Volovik, friction-ODE `u_eff(τ)`: −0.883 → −1/3), 06 (Klinkhamer-Volovik, static-δq DE / oscillating-ξ DM). Classification: **PHONONIC** (q is the substrate's conserved vacuum charge; the relaxation feeds the GGE/reheating channel) / **GEOMETRIC** (the dS-thermodynamic / f(R) machinery is the a₀/a₂ spectral-moment shadow).

The G1 R1 syntheses (volovik §II.2, phonon-first §II.2/II.4) correctly identify these as the microscopic sources for C10's underived Object-C drive, and as candidate *time-profiles*. The cross-cut adjudication the X-review adds: **each candidate must be checked for which side of the radiation-like/EDE-like divide its early-time ρ_vac(a) lands on, because that — not the late-time DILUTION-CC closure — is what the 0.107 budget tests.** The three candidates differ structurally:

- **Klinkhamer-Savelainen-Volovik u_eff(τ) (paper 04)**: the dimensionless relaxation −0.883133 (de Sitter) → −1/3 (Minkowski) is a vacuum-energy *equation-of-state* trajectory, reached only on a measure-zero separatrix (1D fine-tuning in a 4D initial-condition space). This is a late-time/equilibrium trajectory; its early-time (radiation-era) ρ_vac(a) is set by the chosen (ε(q), G(q), Γ_q, Γ_H) tuple and is NOT specified by the trajectory alone. **It does not by itself tell us whether the BBN-epoch ρ_vac clears 0.107** — that requires propagating the specific substrate (ε, G) through the radiation era. The S99 W2-1 FAIL (`S99-W2-RELAXATION-CLOSURE`) already established that the substrate's *bare* friction ODE (convex well k_curv = +3586.5, complex roots −0.75 ± 59.9i) is a lightly-damped oscillator with NO unforced H-tracking tail — so the n_eff ≈ 2 tracking law is itself an *imposed fluid closure*, not a substrate-forced attractor. That is the central tension CF-S100-W2-1-QEQ-DRIVE inherits, and it is *upstream* of the BBN question: if the substrate cannot force the tracking law at all, then the radiation-like profile is an assumption that the substrate may or may not endorse once a genuine q_eq(H) drive is derived.
- **Volovik f(R) ε_vac(H) = f(R=12H²) (paper 02)**: this supplies a *computable* ρ_vac(H) profile once the substrate f(R) form is fixed (K = df/dR ↔ spectral gradient-stiffness Z(τ); G = 1/16πK ↔ a₂). Its early-time behaviour is the contested zone. This is the candidate most directly checkable against the 0.107 budget — and it is the one phonon-first V.3 / volovik V.3-V.4 already pre-spec.
- **Klinkhamer-Volovik static-δq / oscillating-ξ (paper 06)**: this is a DM/DE *split* statement (static δq = DE, oscillating ξ = DM), convergent with the framework's CDM-by-construction. It places DE as a static offset, which is a w = −1 limit — orthogonal to the BBN time-profile question (a static δq does not dilute at all, so it would be radiation-like in the *most extreme* sense if present at BBN; but the framework's DE is the present-epoch residual, not the BBN-epoch vacuum). This is the LEAST relevant of the three to the C10/BBN arm and is properly a DE-branch-hygiene item (phonon-first V.4), not a BBN-relief item.

The structural upshot for the corridor map: **the q-theory sources do not automatically relieve the BBN arm. They supply candidate drives whose early-time ρ_vac(a) must be computed and tested against 0.107. Two of the three (paper 04 separatrix, paper 02 f(R)) are genuine time-profile candidates; the third (paper 06 static-δq) is not a relief mechanism for this arm.** And all of them are downstream of the deeper W2-1 problem — whether the substrate forces *any* H-tracking at all.

### II.5 — Post-BBN-production corridor (Allali, paper 09): blocked by the tracking form, not the chronology

**Result**: paper 09 (Allali-Notari-Rompineve) — BBN element-abundance bounds "are avoided if DR is produced AFTER Big Bang Nucleosynthesis." Classification of the corridor for the framework: **STRUCTURALLY CLOSED under the canonical tracking law; conditionally open only if the tracking law is abandoned.**

The Focus asks whether the post-BBN-production loophole is available "if production completes after T ~ 1 MeV; requires checking the framework's own transit/GGE chronology." Against the register, the answer is structurally sharp and largely negative *for the canonical mechanism*, for a reason that is independent of the transit chronology:

The substrate's transit/GGE chronology actually *predates* BBN by an enormous margin — reheating is at T_RH = 1.70e15 GeV (S76; the GGE relic / Parker pair-production at the fold, n_pairs = 59.8, P_exc = 1.000, with N_decay ≈ 63.4 e-folds of reheating from modulus decay per session-77). BBN is at T_BBN ≈ 1 MeV = 0.001 GeV. So the GGE relic *forms* ~18 orders of magnitude in temperature *before* BBN, not after it. The post-BBN-production loophole requires the extra energy density to be *absent* at BBN and *built later* — the opposite of the framework's chronology, where the relic is long-since formed by BBN.

But the deeper blocker is the tracking *form* itself, and this is the cross-cut insight: **the post-BBN-production corridor is structurally incompatible with a tracking vacuum.** A tracking vacuum ρ_vac = α_V M_Pl² H^{n_eff} is present *whenever H is large*, by definition — it cannot be "produced after BBN" because it is locked to the Hubble rate at every epoch. H is *largest* at early times, so a tracking vacuum is *most* present at BBN, not least. The Allali loophole applies to a dark-radiation species with an independent production history (a freeze-in or late decay); it does not apply to an energy density that is algebraically slaved to H. So:

```
Corridor A (post-BBN production):
  - Available for: an energy density with an independent production epoch (dark radiation, late decay).
  - The framework's ρ_vac is a TRACKING vacuum (rho_vac propto H^n_eff): present whenever H is large,
    MOST present at BBN (H largest), CANNOT be "produced later."
  => Corridor A is STRUCTURALLY CLOSED for the canonical tracking vacuum.
  => Re-opens ONLY if the substrate replaces the tracking law with a genuinely produced-later
     component -- which is a different mechanism, not DILUTION-CC.
```

This is a stronger statement than either R1 synthesis made (both treated Corridor A as "open pending a chronology check"). The register shows the chronology check is moot: the tracking form forecloses Corridor A regardless of when the GGE relic forms.

### II.6 — EDE-like corridor (Seto-Toda, paper 10): requires departing from n_eff ≈ 2, and carries the Ω_b h² → D/H residual

**Result**: paper 10 (Seto-Toda, FOUNDATIONAL) — an EDE-like contribution (ρ_DE ∝ a^{−n}, n = 4 or 6, peaked near matter-radiation equality, negligible at BBN) evades the *direct expansion-rate* BBN channel but NOT the *inferred-baryon-density* (Ω_b h² → D/H) channel. Classification of the corridor: **CONDITIONALLY OPEN, but only as a DEPARTURE from the canonical tracking law, and with a residual side-channel and a strengthened (combined-probe) window.**

This is the corridor with genuine surviving potential, but its admissibility conditions are stricter than the R1 syntheses stated, on three counts the cross-cut review pins:

1. **It is a departure, not a tuning (§II.1).** EDE-like means ρ_vac ∝ a^{−n} with n > 4 (dilutes *faster* than radiation), i.e. a *negative* a-exponent on the fraction. The canonical tracking vacuum has a *positive* a-exponent (+0.0438). So the substrate cannot reach the EDE-like corridor by refining n_eff near 2 — it must produce a *qualitatively different* early-time scaling. The q-theory drive that does this (if any) is precisely the CF-S100-W2-1-QEQ-DRIVE deliverable: a substrate q_eq(H) that does NOT give the H^{n≈2} tracking form at early times.

2. **The budget is combined BBN+CMB+BAO, not BBN-only (paper 11).** Paper 10's evasion is of the *BBN-only* expansion-rate channel. Paper 11's 0.107 folds in CMB+BAO. So an EDE-like profile must be negligible at *both* BBN AND the CMB-N_eff-sensitive epoch (recombination), which is strictly stronger than paper-10 evasion. A profile peaked "near matter-radiation equality" (z_eq ≈ 3400) sits uncomfortably close to recombination (z ≈ 1100) — the peak must be early enough and narrow enough to be sub-0.107 at recombination too.

3. **The Ω_b h² → D/H residual side-channel (paper 10's own warning).** Even a fully BBN-and-CMB-N_eff-evading EDE-like profile is not automatically BBN-safe: fitting the CMB with an EDE component requires an increased Ω_b h², which lowers D/H and raises χ²_Cooke. So Corridor B has a residual gate even when the direct N_eff channels are cleared.

```
Corridor B (EDE-like dilution):
  - Requires: rho_vac propto a^-n, n > 4 (DEPARTURE from the canonical n_eff~2 tracking law).
  - Must clear: ΔN_eff < 0.107 at BOTH BBN (T~1 MeV) AND recombination (CMB N_eff window).
  - Residual: Omega_b h^2 -> D/H side-channel (paper 10) even after the N_eff windows are cleared.
  => Corridor B is CONDITIONALLY OPEN, contingent on a substrate q_eq(H) drive that produces a
     non-tracking, fast-diluting early-time profile -- i.e. contingent on CF-S100-W2-1-QEQ-DRIVE
     yielding something OTHER than the H^{n~2} tracking law.
```

### II.7 — Lever-alone relief falls short by 4.37×: the magnitude axis is genuinely exhausted

**Result**: clearing ΔN_eff < 0.107 by the n_eff from-below lever alone requires n_eff − 2 = −0.0957 (n_eff = 1.9043), which is **4.37× the substrate-derived shift** of −0.0219 (Sage-exact). Classification: **PHONONIC** (quantifies the magnitude-corridor shortfall against the current budget).

This number is the cross-cut sharpening of the S99 W2-BBN-RELIEF (a)-mechanism result. S99 W2 found that reaching the *looser* ΔN_eff = 1 bound needs n_eff = 1.959839 (a 1.835× shift). Against the *current* 0.107 budget, the required shift is 4.37× — more than twice as demanding. This confirms, quantitatively, that the magnitude axis is exhausted: no plausible refinement of the from-below sub-leading correction (a structurally fixed O(1%) effect) delivers a factor-4.37 enhancement. **The magnitude corridor is closed against 0.107 with margin to spare; the only surviving relief is on the time-profile axis (§II.5/II.6), and that axis requires departing from the tracking law (§II.1).**

---

## III. Gate Verdicts

These are CANONICAL gate verdicts retrieved from the knowledge MCP — NOT re-adjudicated here; cited so the corridor map and carry-forwards inherit correct upstream state.

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| `S98-MK3-2-BBN-VACUUM-FRACTION` (C10 arm) | FAIL | ΔN_eff = 2.0873; frac_below = 0.4740; bound = 0.2271; vs paper-11 0.107 → 19.51× |
| `S99-W2-BBN-RELIEF` (W2-2; magnitude corridor) | FAIL | dNeff = 2.0873; relief_factor = 0.4141; (a)/(b)/(c) all non-substrate-justified; audit `8fe0ef45…` |
| `S99-W2-RELAXATION-CLOSURE` (W2-1; n=2-unforced-attractor) | FAIL | slope_bare = 3.4159 (R²=0.079); slope_driven = 1.0083 only under imposed q_eq = c·H; audit `e0e16d24…` |
| `S98-W2-2-RELAXATION-CLOSURE` | FAIL (PRE-REG-INC) | blocked by AOFT conformally-stationary frame, q-attractor 0/0; deferred to CF-S99 |
| `S98-MK3-1-C10-SUBLEADING-SIGN` | PASS | divergence_type=A; sign_a3_meas=−1; a3_q0_analytic=−881.5351 (the drive SIGN is derived) |
| `DILUTION-CC-66` | PROVEN (S66) | rho_vac/rho_obs = 1.032; CC_OOM = 115.5; CONDITIONAL on C10 + external FRW H |
| C10 (atlas-04 status) | ASSUMED-PARTIALLY-PROVEN | rho_vac ~ M_Pl² H² scaling assumed; q_eq(H) drive NOT derived |
| Q29 / Window-8 (BBN-VOLOVIK-67) | CORRIDOR CLOSED (structural) — **scope: magnitude axis only** | S99-W2-BBN-RELIEF FAIL; ~2.087× short on magnitude |

---

## IV. Structural Implications — The Relief-Corridor Map

**The C10/BBN residual is a single FAIL with a precisely-located surviving relief region, and the region is narrower than the R1 syntheses implied.** The cross-cut review's contribution is to separate the two relief axes (magnitude vs time-profile), show the magnitude axis is exhausted against 0.107, and show that the time-profile axis is reachable only by *departing from* the canonical tracking law — which routes the entire surviving relief through the CF-S100-W2-1-QEQ-DRIVE successor, not through a BBN-specific patch.

### IV.A — Corridor map (open / closed / conditional, and on what)

| Corridor | Mechanism | Status | Closed/open ON WHAT |
|:---------|:----------|:-------|:--------------------|
| **Magnitude — larger from-below Δn** | shrink n_eff below 1.978 | **CLOSED** | n_eff is HARD-fixed by the S98 sub-leading-sign computation (divergence_type=A); clearing 0.107 needs a 4.37× larger shift (§II.7), not substrate-derived. S99 W2 (a). |
| **Magnitude — epoch-dependent α_V** | α_V(z) halves at BBN | **CLOSED** | DILUTION-CC uses ONE α_V (single a₀ tracking normalization); no substrate forces α_V(z). S99 W2 (b). |
| **Magnitude — distinct dilution channel** | sub-select ~475/992 D_K modes at BBN | **CLOSED** | a₀ = ζ_{D_K}(0) = Tr(1) counts ALL 992 modes; no substrate sub-selection. S99 W2 (c). |
| **Time-profile — post-BBN production** | ρ_vac absent at BBN, built later | **STRUCTURALLY CLOSED** for the tracking vacuum | A tracking vacuum ρ_vac ∝ H^{n_eff} is present whenever H is large (MOST present at BBN). Cannot be "produced later." Chronology check is moot (GGE relic forms at T_RH=1.7e15 GeV ≫ T_BBN). Re-opens only if the tracking law is replaced. (paper 09; §II.5) |
| **Time-profile — EDE-like dilution** | ρ_vac ∝ a^{−n}, n>4, negligible at BBN | **CONDITIONALLY OPEN** | Requires a substrate q_eq(H) drive giving a NON-tracking, fast-diluting early-time profile (opposite a-exponent sign to the canonical tracking law). Must clear 0.107 at BOTH BBN and recombination. Carries the Ω_b h²→D/H residual. (paper 10; §II.6) |
| **Upstream — substrate q_eq(H) drive** | derive a substrate-forced H-tracking (or non-tracking) law | **OPEN (the live successor)** | S99 W2-1 FAIL: the bare friction ODE gives no unforced H-tracking; n_eff≈2 is an IMPOSED fluid closure. CF-S100-W2-1-QEQ-DRIVE. This gate's OUTPUT determines whether the early-time profile is tracking (radiation-like, FAIL) or non-tracking (potentially EDE-like, conditional relief). |

### IV.B — The load-bearing dependency

The corridor map collapses to one structural statement: **every surviving relief route runs through `CF-S100-W2-1-QEQ-DRIVE`, because that gate decides whether the substrate forces a tracking law at all.** If CF-S100-W2-1-QEQ-DRIVE yields the H^{n≈2} tracking form (the imposed-closure outcome), the early-time profile is radiation-like and C10/BBN is robustly falsified by the 0.107 budget (19.51× over) — both time-profile corridors are foreclosed (post-BBN structurally, EDE-like by wrong-sign a-exponent). If CF-S100-W2-1-QEQ-DRIVE yields a NON-tracking q_eq(H) (a genuinely substrate-forced H-dependence that is NOT ∝ H^{n≈2}), then the EDE-like corridor *may* open, contingent on the early-time ρ_vac(a) of that drive clearing 0.107 at both BBN and recombination and surviving the Ω_b h² → D/H residual.

This is the key composition the spawn Focus asks for ("how it composes with CF-S100-W2-1-QEQ-DRIVE"): **a BBN-arm relief gate is NOT independent of CF-S100-W2-1-QEQ-DRIVE — it is strictly downstream of it.** A BBN-arm gate cannot be meaningfully run until the q_eq(H) drive is known, because the early-time ρ_vac(a) it tests IS the output of that drive. Pre-registering a BBN-arm gate NOW (§V.1) is admissible as a CONDITIONAL gate (trigger-first per `project_conditional-gate-and-qgge-dormancy`): it fires only if CF-S100-W2-1-QEQ-DRIVE returns a non-tracking drive (PASS or INFO with a derived q_eq(H)); if CF-S100-W2-1-QEQ-DRIVE FAILs (no substrate q_eq(H), tracking law stays an imposed closure), the BBN-arm gate closes as CONDITIONAL-SKIP-as-INFO with the radiation-like reading standing and C10/BBN robustly falsified.

### IV.C — What this does NOT change

- **The present-epoch DILUTION-CC closure is UNAFFECTED.** `rho_vac/rho_obs = 1.032` (z=0, lever=1) is the late-time arm; the BBN-arm tension is the high-z arm of the same tracking vacuum. The 114-OOM CC-gap closure stands; what is in tension is whether that *same* tracking vacuum survives nucleosynthesis. (This is the W2-2 working-paper finding, confirmed.)
- **C10 stays ASSUMED-PARTIALLY-PROVEN.** No verdict moves. The BBN arm sharpens the conditionality; it does not close or open the mechanism.
- **The DM-from-DE convergence (paper 06) is orthogonal.** The static-δq/oscillating-ξ split is a DM/DE-structure statement, not a BBN time-profile mechanism. It does not enter the corridor map.

### IV.D — Conflicts and reconciliations flagged

1. **Focus framing vs register (gate-name/role mapping)**: the Focus says "S99 W2-1 FAIL closed the n=2 unforced attractor corridor; S99 W2-2 FAIL [was] BBN from-below relief." Content-correct; the canonical gate IDs are `S99-W2-RELAXATION-CLOSURE` (W2-1, attractor) and `S99-W2-BBN-RELIEF` (W2-2, BBN). No substantive conflict — flagged for precision.
2. **Focus/index/mack-R1/sagan-R1 "EDE-like likely" vs register**: the index and both G2 R1 syntheses lean on "the substrate's actual time-profile likely sits closer to the EDE-like (relieved) case." The register does NOT support this as the canonical reading: the canonical mechanism is a tracking vacuum (n_eff≈2), which is radiation-like by construction (§II.1). EDE-like is a DEPARTURE, not the default. This is the single most important reconciliation in the cross-cut.
3. **volovik-R1 "0.107 non-canonical" vs phonon-first-R1 "0.107 external-and-comparable"**: phonon-first is correct and confirmed (§II.2). 0.107 is the external budget; the gate's PASS threshold is the fraction-based 0.2271; both are real and serve different roles. The volovik-R1 instruction to use only the fraction-test is correct for the gate's *internal* PASS criterion but understates the *external* falsification, which is against 0.107.
4. **Q29 "CORRIDOR CLOSED (structural)" scope**: closed on the MAGNITUDE axis only (the three mechanisms S99 W2 actually tested). The time-profile axis is NOT closed by Q29 (§II.3). Flagged so downstream consumers do not read Q29 as foreclosing the EDE-like corridor.

---

## V. Carry-Forward Computations

```
V.1. CF-S100-W2-BBN-PROFILE — early-time rho_vac(a) of the CF-S100-W2-1-QEQ-DRIVE output vs the 0.107 budget [CONDITIONAL, trigger-first]
   - What: TRIGGERED by CF-S100-W2-1-QEQ-DRIVE returning a derived substrate q_eq(H). Propagate the
     resulting rho_vac(a) through the radiation era (BBN, T~1 MeV) AND to recombination
     (CMB-N_eff-sensitive epoch, z~1100), and classify the profile: radiation-like (a-exponent of
     rho_vac/rho_rad >= 0, FAIL) vs EDE-like (a-exponent < 0, fast-diluting, candidate relief).
     Output: rho_vac(a) array; the two epoch-resolved fractions (rho_vac/rho_rad)_BBN and
     (rho_vac/rho_rad)_rec; the implied ΔN_eff at BOTH epochs; the radiation-like/EDE-like tag.
   - Inputs: CF-S100-W2-1-QEQ-DRIVE output q_eq(H) (the TRIGGER; must be a NON-tracking drive for relief
     to be possible -- a tracking H^{n~2} output forecloses both corridors); delta_N_eff_vacuum_BBN_below
     = 2.0873; rho_vac_over_rho_rad_BBN_below = 0.474049; canonical S66 formula
     ΔN_eff = (rho_vac/rho_rad) / [(7/8)(4/11)^{4/3}] with bound (7/8)(4/11)^{4/3} = 0.227107 (Sage-exact);
     X_BBN = ln(H_BBN/H_0) = 40.2756; X_rec (analogous lever to recombination, derive); paper 11 budget
     0.107 (external; combined BBN+CMB+BAO); paper 10 EDE-vs-radiation a-scaling taxonomy.
   - Gate: NEW CONDITIONAL gate S100-C10-BBN-PROFILE (trigger-first per
     project_conditional-gate-and-qgge-dormancy). FIRES iff CF-S100-W2-1-QEQ-DRIVE returns a derived
     non-tracking q_eq(H). PASS iff ΔN_eff < 0.107 at BOTH BBN AND recombination under the substrate
     profile; INFO iff the profile is EDE-like and clears BBN but the recombination window OR the
     Omega_b h^2->D/H side-channel (V.2) is unchecked; FAIL iff radiation-like (a-exponent >= 0 ⇒
     19.51x exceedance stands). CONDITIONAL-SKIP-as-INFO (radiation-like reading stands, C10/BBN
     robustly falsified) iff CF-S100-W2-1-QEQ-DRIVE FAILs (no substrate q_eq(H)).
   - Effort: 3-4 hours, 1 agent session (downstream of CF-S100-W2-1-QEQ-DRIVE; the radiation-era
     propagation is cheap once q_eq(H) is in hand).
   - Depends on: CF-S100-W2-1-QEQ-DRIVE (the TRIGGER and the rho_vac(a) source -- this gate cannot run
     before it).

V.2. CF-S100-W2-OMEGAB-DH — Omega_b h^2 -> D/H residual side-channel under an EDE-like substrate profile [CONDITIONAL on V.1 = EDE-like]
   - What: IF V.1 returns EDE-like (clears the direct N_eff windows), compute the residual BBN
     constraint via the inferred-baryon-density channel (paper 10's warning): the CMB-fit-required
     Omega_b h^2 shift and its propagated effect on D/H vs Cooke+18. Output: required Delta(Omega_b h^2),
     predicted D/H, chi^2_Cooke contribution.
   - Inputs: V.1 rho_vac(a) EDE-like profile; framework Omega_b (query get_constant; Omega_b = 0.0493
     per sagan-R1, omega_H2 = 1.41 -- VERIFY against canonical at run-time, these were sagan-R1 pins
     not independently confirmed here); paper 10 EDE-vs-N_eff baryon-density mechanism; paper 11
     compressed-datavector Omega_b h^2 = 0.022371; Cooke+18 D/H = 2.527 +/- 0.030 x 10^-5 (cite from
     paper 10/11 text).
   - Gate: NEW S100-C10-OMEGAB-DH (sub-gate of V.1; trigger-first, fires only if V.1 = EDE-like).
     PASS iff |D/H_pred - D/H_obs| < 2 sigma_Cooke under the EDE-like Omega_b h^2 shift; FAIL iff the
     baryon-density channel reintroduces a > 2 sigma D/H tension (EDE-like relief incomplete even after
     the N_eff windows clear).
   - Effort: 2-3 hours, 1 agent session.
   - Depends on: V.1 (fires only if V.1 = EDE-like).

V.3. CF-S100-W2-TRACKING-PROFILE-DIAGNOSTIC — pin the canonical tracking vacuum's a-scaling as the radiation-like baseline [unconditional, low-effort]
   - What: Document, as a standalone diagnostic baseline (independent of the CF-S100-W2-1 trigger), that
     the CANONICAL n_eff=1.978 tracking vacuum is radiation-like: compute rho_vac/rho_rad propto
     a^{2(2-n_eff)} = a^{+0.0438} (Sage-exact), confirm the positive a-exponent (fraction grows toward
     late times / shrinks toward early times = the from-below relief direction), and contrast against
     the EDE-like requirement (a-exponent < 0). This is the baseline that V.1 measures departures from.
     Output: the a-exponent, the radiation-like classification, and the explicit statement that EDE-like
     relief requires DEPARTING from the tracking law (opposite a-exponent sign).
   - Inputs: n_eff = 1.978111 (S98 V.9); rho_vac = alpha_V M_Pl^2 H^{n_eff} (S66/S73b tracking law);
     radiation-era H propto a^-2; X_BBN = 40.2756; canonical bound (7/8)(4/11)^{4/3} = 0.227107.
   - Gate: NEW S100-C10-TRACKING-DIAGNOSTIC (INFO-class; structural-baseline pin, not a relief test).
     PASS = the radiation-like a-exponent + the EDE-departure statement are pinned to canonical_constants
     and the falsifier-master-inventory (mack-cosmic-bridge sole writer); records that the canonical
     mechanism sits on the radiation-like worst-case branch the 0.107 budget excludes. This is a
     registry-write (artifact-existence predicate), the structural anchor the corridor map rests on.
   - Effort: 1-2 hours, 1 agent session (the a-exponent is Sage-exact; the rest is the inventory row).

V.4. CF-S100-W2-BUDGET-REPIN — re-pin the C10 external budget to Goldstein-Hill 0.107 and register the 3-tier hierarchy [unconditional, hygiene]
   - What: Register the current state-of-the-art external N_eff budget ΔN_eff < 0.107 (95%, combined
     BBN+CMB+BAO, N_eff = 2.990 +/- 0.070, paper 11) as a canonical observational anchor, alongside the
     existing gate PASS-threshold 0.2271 (BBN element-abundance) and the paper-09 CMB-era 0.39/0.46,
     so downstream consumers cite the right one for the right purpose. Document that the framework's S66
     ΔN_eff formula and paper-11 Eq. 1 rho_rad definition are bit-identical (no convention mismatch).
   - Inputs: paper 11 (arXiv 2603.13226) N_eff = 2.990 +/- 0.070, ΔN_eff < 0.107; paper 09 (arXiv
     2404.15220) 0.39/0.46; delta_N_eff_vacuum_BBN_below = 2.0873; the three Sage-exact exceedances
     (9.19x / 5.35x-4.54x / 19.51x).
   - Gate: registry-hygiene; update_constant for delta_N_eff_budget_combined_2026 = 0.107 (provenance:
     Goldstein-Hill 2026, external observational falsification anchor; DISTINCT from the gate's internal
     PASS threshold 0.2271). INFO-class (threshold-currency hygiene; resolves the volovik-R1-vs-
     phonon-first-R1 "is 0.107 canonical" conflict by registering BOTH the internal threshold and the
     external budget with explicit role tags). mack-cosmic-bridge sole writer of the falsifier-master-
     inventory row.
   - Effort: 1 hour, 1 agent session.
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Canonical early-vacuum is a TRACKING vacuum (n_eff=1.978≈2); ρ_vac/ρ_rad ∝ a^{+0.0438} | PHONONIC | Structural pivot | Radiation-like by CONSTRUCTION, NOT EDE-like; EDE-like is a DEPARTURE (opposite a-exponent sign), not a tuning |
| 2 | 0.107 is external-and-comparable (identical (7/8)(4/11)^{4/3}); exceedance 19.51× | PHONONIC | FAIL anchor | Resolves volovik-R1/phonon-first-R1 conflict: external budget 0.107 ≠ gate threshold 0.2271; both real |
| 3 | S99 W2-BBN-RELIEF closed MAGNITUDE axis only; (a)/(b)/(c) all magnitude-corridor | PHONONIC | FAIL (magnitude exhausted) | Q29 "CORRIDOR CLOSED" is scoped to magnitude; time-profile axis is UNTESTED |
| 4 | q-theory sources (P02 f(R), P04 u_eff, P06 δq) supply candidate NON-tracking profiles | PHONONIC/GEOMETRIC | Candidate drives | P02/P04 are time-profile candidates; P06 (static-δq) is NOT a BBN-relief mechanism |
| 5 | Post-BBN-production corridor (P09) | — | **STRUCTURALLY CLOSED** for tracking vacuum | A tracking vacuum is MOST present at BBN (H largest); cannot be "produced later"; chronology check moot |
| 6 | EDE-like corridor (P10) | — | **CONDITIONALLY OPEN** | Requires departing n_eff≈2; must clear 0.107 at BBN AND recombination; carries Ω_b h²→D/H residual |
| 7 | Lever-alone relief falls short by 4.37× vs 0.107 (vs 1.835× vs the looser ΔN_eff=1) | PHONONIC | Magnitude axis closed | Confirms the only surviving relief is time-profile, which requires departing from the tracking law |
| 8 | All surviving relief runs through CF-S100-W2-1-QEQ-DRIVE | — | Load-bearing dependency | A BBN-arm gate is strictly DOWNSTREAM of the q_eq(H) drive; pre-registerable NOW only as CONDITIONAL (trigger-first) |

---

**Cross-cut closing note.** The C10/BBN residual is not a tension awaiting a clever patch — it is a structural fork. The framework's canonical early-vacuum is a tracking vacuum, and a tracking vacuum is radiation-like, and the radiation-like reading is excluded at 19.51× by the current combined-probe budget. The magnitude axis is exhausted (lever-alone falls short by 4.37×; the three S99-W2 mechanisms are non-substrate-justified). The post-BBN-production corridor is structurally foreclosed by the tracking *form* itself, independent of the (early, T_RH=1.7e15 GeV) GGE chronology. The only surviving corridor — EDE-like dilution — requires the substrate to abandon the n_eff≈2 tracking law at early times, which is exactly what `CF-S100-W2-1-QEQ-DRIVE` is built to test. So the honest map is: **C10/BBN lives or dies on whether the substrate forces a tracking law (radiation-like, FAIL) or a non-tracking drive (potentially EDE-like, conditional relief through V.1) — and that single upstream gate, not any BBN-specific mechanism, is where the residual is decided.** A BBN-arm relief gate IS pre-registerable now (V.1), but only as a conditional successor triggered by, and strictly downstream of, the q_eq(H) drive. No probability moves until a pre-registered gate fires.

*Anchoring note: every framework-state claim verified against canonical via knowledge MCP (get_constant / search_knowledge / query_entity / trace_entity). The four R1 syntheses and both indexes treated as input, not authority, per the Focus. Six index/Focus/R1-vs-canonical reconciliations flagged: (1) the canonical mechanism is radiation-like (tracking vacuum), NOT "likely EDE-like"; (2) 0.107 is external-and-comparable, distinct from the gate's 0.2271 threshold; (3) Q29 "CORRIDOR CLOSED" is magnitude-scoped, not time-profile-scoped; (4) post-BBN production is structurally closed by the tracking form; (5) S99 gate IDs are RELAXATION-CLOSURE (W2-1) / BBN-RELIEF (W2-2); (6) all surviving relief is downstream of CF-S100-W2-1-QEQ-DRIVE. The a-exponent +0.0438, the relief_factor 0.414, the ΔN_eff 2.0873, the 19.51× exceedance, and the 4.37× lever-shortfall are Sage-verified.*
