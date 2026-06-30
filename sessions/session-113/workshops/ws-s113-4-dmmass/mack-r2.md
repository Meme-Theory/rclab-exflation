# WS-S113-4 DMMASS — Round 2 (rebuttal)

**Author / pole**: mack-cosmic-bridge — Round 2, rebuttal (defending Reading B: the Leggett-DM mass is irreducibly unanchored in magnitude).
**One line**: Landau's strongest move — "the 170× is measured against the wrong branch; against the Leggett anchor the target is only ~14× Δ_BCS, already inside the Γ-point ladder" — has a real core that I concede *strengthens* the in-spectrum picture, but the specific number is conflated (the corrected Leggett-relative target is **2.13×**, i.e. **25.5× Δ_BCS**, which lands on the **Higgs amplitude** branch, not a Leggett inter-band moment), so landau's `[12,16]× Δ_BCS` gate is mis-calibrated AND any mode at the target *changes the DM's identity* (breaking the abundance + Z₂-protection that make it DM). The σ_SI NULL is robust under both the 170× and the corrected 2.13× — the falsifier sharpening holds regardless.

---

## 1. Crediting landau's real structural work (not a strawman)

Landau's R1 is a strong, honest piece of physics, and I want to be precise about what I accept before I push back:

- **Accept: the single-band framing is a category error.** Landau is right that "multiply Δ_BCS by ~170" mis-poses the problem. The DM is the Leggett inter-band relative-phase mode (branch 3), and the right question is "which spectral *moment* of the multiband BdG operator is the structure-formation mass." I conceded this implicitly in my R1 §3.2 (the "ratio reading"); landau has now made it concrete with the order-parameter structure and the three-branch decomposition. That is the correct substrate-IS framing.
- **Accept: B-3 and B-4 are the same wall seen twice.** The constraint-map read — both closures are upward pumps on the (0,0) single-particle/phase sector, both defeated by `D_s ≫ Δ_BCS` — is correct and well-argued. The inter-band sector is genuinely a *different* operator that those two walls do not directly touch.
- **Accept: landau surfaced his own strongest counter (the wall-#11 Z₂ gauge degeneracy) instead of hiding it.** That is exactly the discipline the framing law demands, and it is the honest core of his liability.

So this is not a weak-pole rebuttal. Landau has a structurally live corridor (S-a) and a real gate. My rebuttal is that **(i) the specific gate is built on a conflated number, (ii) when the number is corrected the corridor either lands on the wrong branch or covertly re-identifies the DM, and (iii) none of this touches the σ_SI sharpening — which the corrected number actually reinforces.**

---

## 2. The conflated number (the load-bearing correction)

Landau's "single most decisive consideration" is that the 170 is Goldstone-relative, and *"against the Leggett anchor the target is only 170/11.97 = 14.20× Δ_BCS, which sits inside the framework's already-computed Γ-point multiband ladder."* His PASS band is `ω_Leggett^{B2-B3}/Δ_BCS ∈ [12, 16]`, built on that 14.2.

**The 14.2 is a unit error.** I went to the source — `sessions/framework/Collabs/atlas-spectral-geometer-collab.md §5` (the origin of the 170 figure) — and read it directly. It states, verbatim:

> "The 170x shortfall is between the **Goldstone mass** (a collective excitation on the fabric) and the mass required for n_s = 0.965 at K_pivot = 2.0 ... **the target of 11.85 M_KK**."

So the source carries BOTH numbers explicitly: `m_G = 0.070 M_KK` (Goldstone) and `m_required = 11.85 M_KK` (the target). The 170 is `m_required/m_G = 11.85/0.070 = 169.3`. Landau then forms `170/11.97` — but that divides a **Goldstone-relative ratio** by the **Leggett-in-Δ_BCS-units anchor**, which is dimensionally incoherent (it mixes the m_G-normalized 170 with the Δ_BCS-normalized 11.97). The correct Leggett-relative target uses the *source* `m_required` (Sage-exact, `RealField(200)`):

```
m_Leggett   = 11.97 × Δ_BCS = 11.97 × 0.4642547 = 5.5571 M_KK
m_required  = 11.85 M_KK                          [collab §5, explicit]

target / Leggett anchor = m_required / m_Leggett = 11.85 / 5.5571 = 2.1324×
m_required in Δ_BCS units = 11.85 / 0.4642547    = 25.525 × Δ_BCS
```

**The corrected Leggett-relative target is 2.13× (i.e. 25.5× Δ_BCS) — NOT 14.2×.** Landau's `[12,16]× Δ_BCS` PASS band *excludes the actual target* (25.5× Δ_BCS): the gate as written would return FAIL-by-construction for the right scale and could only "PASS" on a value that is not the structure-formation requirement. The gate is mis-calibrated at the pre-registration level (a Class-8 PRU defect: the threshold pins the wrong target band).

This is not a quibble — it is the number the entire (S-a) corridor is steered by. A gate whose PASS band is set against a conflated target cannot adjudicate the mass anchor.

---

## 3. The correction cuts BOTH ways — and the honest part helps landau's *thesis* while sinking his *mechanism*

I will not cherry-pick. The corrected number 25.5× Δ_BCS does something landau will (correctly) seize on: it **strengthens his underlying "the scale is already in the spectrum" claim**, because the target lands essentially *on top of* a computed sibling:

```
m_required = 11.85  M_KK  (= 25.52 × Δ_BCS)
omega_H3   = 11.465 M_KK  (= 24.70 × Δ_BCS)   [canonical_constants.py:766, BCS-Higgs amplitude Γ-point]
ratio = omega_H3 / m_required = 0.9675   ⇒ 3.2% apart.
```

The structure-formation target and the Higgs-3 amplitude sibling **coincide to 3.2%.** On its face this is the *strongest* possible version of Reading A: the required scale is not just "inside the ladder," it is realized *almost exactly* by an already-computed zero-free-parameter mode. I concede that fully — and it means the corrected number does NOT simply defeat landau.

**But it relocates the DM, and that is fatal to using it as a mass anchor.** The mode that sits at the target (omega_H3 = 11.465 M_KK) is the **Higgs (amplitude) branch** — landau's own branch 2, "gapped at 2Δ" — NOT the **Leggett inter-band relative-phase branch** (branch 3) that *is* the DM. To anchor the DM mass at the structure-formation target via this sibling, one would have to **identify the DM with the Higgs-3 amplitude mode instead of the Leggett mode.** That re-identification breaks the two properties that make the DM viable in the first place:

1. **Abundance.** Ω_DM h² = 0.120 (the 0.6% Planck match, §VII C7/C11) is computed for the **Leggett mode** at 11.97·Δ_BCS via the n_pairs = 59.8 saturated partition. The abundance is mode-specific. Move the DM to the Higgs-3 amplitude branch and the relic-abundance derivation no longer applies — you would have to re-derive Ω_DM for the amplitude mode, and there is no reason it lands at 0.120. **The framework's single biggest DM success is forfeited.**
2. **Z₂-protection / non-annihilation.** The DM is stable because the Leggett mode is a Z₂-odd inter-band *relative*-phase excitation (LEGGETT-GRAV-DECAY-73a + S67 frustration), forbidding single-quantum decay. The Higgs (amplitude) mode is NOT Z₂-odd in the same way — it is the `|S|²` amplitude oscillation, which couples to pairs and is *not* the protected channel. Move the DM there and you lose the stability/non-annihilation that defines it as DM.

So the corrected coincidence is a **trap, not a solution**: the scale that matches structure formation is on the wrong branch, and adopting it dissolves the DM identity. Landau's branch-3 corridor (S-a) needs the **Leggett** inter-band gap specifically to hit 25.5× Δ_BCS — and the Leggett anchor is at 11.97× Δ_BCS, a factor 2.13× below. So within branch 3, the shortfall is *not* closed by the ladder; the only ladder member at the target is on a *different* branch that cannot be the DM.

**Net:** the correction (a) breaks landau's specific [12,16] gate, and (b) shows the one ladder member at the target is the wrong branch. Landau's "which spectral moment?" reframe is correct as a *question*, but the answer the spectrum gives at the target is "the amplitude moment," which is not the DM. To keep the DM as the Leggett mode AND hit the target, branch 3 must produce a 2.13× upward shift of its *own* inter-band gap — which lands us back at landau's (S-a) gate, now correctly targeted at **25.5× Δ_BCS** rather than 14.2×, and facing his own un-resolved wall-#11 Z₂ degeneracy.

---

## 4. Does (S-a) supply the magnitude at 0 params, or covertly import a scale? (the direct rebuttal questions)

The team-lead's two questions, answered head-on:

**(a) Does landau's mechanism genuinely supply the mass MAGNITUDE from the substrate at 0 free params?** **No — at the magnitude level it does not, and it does not claim to.** Read carefully, (S-a) supplies a *dimensionless ratio* `ω_Leggett^{B2-B3}/Δ_BCS` (landau's own gate observable is a ratio). The dimensionful magnitude in GeV is still `[that ratio] × Δ_BCS × M_KK` — it rides M_KK exactly as I argued in R1 §1. Landau concedes this in his §4: *"the M_KK import is the SAME single import the whole framework makes once."* **We are in violent agreement on the magnitude**: the dimensionful scale is M_KK, imported once, permanent-external (S112 FAIL). The only live disagreement is whether the *dimensionless* prefactor that multiplies M_KK is (Reading A) a computable 25.5 inter-band moment or (Reading B) carries an irreducible piece. landau has NOT exhibited a 0-param mechanism that *outputs 25.5*; he has proposed a gate that *might* output something in [12,16] (the wrong band). The magnitude is not anchored at 0 params today — it is a *pending dimensionless computation* whose target landau mis-stated.

**(b) Does (S-a) actually evade the four corridors, or re-skin one?** **It evades B-3/B-4/PBH/CFL — I grant that — but it inherits B-3's wall in inverted form, and landau's own wall-#11 is the live obstruction.** landau's §2.1 "stiffness inversion" argument (large `D_s` *raises* ω_Leggett because a stiff relative phase resists inter-band counterflow) is physically real for a generic two-band superfluid (Leggett 1966; the `ω_Leggett² ∝ Δ_1Δ_2/J_12` structure). But it is precisely *here* that wall-#11 bites: the S82 W2-11 Z₂ gauge degeneracy scrambles the relative-phase observable on the projected inter-band Josephson subspace, and `J_12` (the denominator that controls whether ω_Leggett goes UP) is exactly the gauge-ambiguous quantity. landau himself flags that the gate is "well-posed *only* on the full B2⊕B3 BdG sector" and that "a Stage-1 dry-run must verify Z₂-gauge-invariance before dispatch." **That pre-flight is unresolved.** Until it is, (S-a) is not a re-skin of a closed corridor, but it is also not a demonstrated open one — it is a corridor whose *well-posedness* is contingent on a check landau has not run and has correctly identified as a real risk. The honest status is: **(S-a) is admissible-pending-Z₂-preflight, targeting 25.5× Δ_BCS (corrected), not yet shown to land there.**

---

## 5. The σ_SI NULL sharpening is REINFORCED by the correction

My R1 decisive consideration was that the σ_SI = 1.299e-63 cm² NULL is mass-anchor-robust. landau did not contest this (his case is about the mass scale, not the direct-detection channel), and the corrected number makes it *stronger*:

- In R1 I stress-tested the full 170× rescaling: NULL survives by 26.5 OOM (worst case, mass ×170, σ∝M², exclusion frozen).
- Under the **corrected** 2.13× shift (the actual Leggett→target factor): σ_SI rises to 5.91e-63 cm², still **30.26 OOM below LZ-2024** (Sage-exact). The smaller, correct shortfall barely moves the NULL at all.

So whatever the (S-a) gate returns — whether the Leggett inter-band gap lands at 11.97×, or is pumped to 25.5× Δ_BCS — the direct-detection prediction stays a clean zero-free-parameter NULL 30 OOM below every detector. **The falsifier is orthogonal to the entire mass-anchor debate.** This is the part of Reading B that does not move regardless of who wins the spectral-moment question: the framework's *live, falsifiable* DM contact is the gravitational-floor NULL (Row #79), and it is anchor-robust by construction (σ_SI ~ (G_N M_DM m_Xe)², and G_N in particle units is 6.7e-39 GeV⁻², making the floor astronomically tiny for any mass in the window). Reading B's structural claim — "abundance-predicted, falsifier-anchored, *magnitude*-unanchored" — survives landau's R1 intact on the two flanks that matter (abundance + falsifier); only the *middle* (is the magnitude-prefactor a closable dimensionless moment) remains contested, and that is exactly the crux for R3.

---

## 6. Where this leaves the two poles (sharpened)

The R1 framing ("surviving mechanism" vs "irreducibly unanchored") was slightly too coarse; the correction sharpens the actual disagreement to a single dimensionless question:

| | Reading A (landau, corrected) | Reading B (mack) |
|:--|:--|:--|
| Magnitude in GeV | rides M_KK (imported once) — **AGREED** | rides M_KK (imported once) |
| Abundance Ω_DM h²=0.120 | mode-specific to Leggett — **AGREED** | mode-specific to Leggett (mass-magnitude-independent) |
| σ_SI NULL | anchor-robust — **AGREED / not contested** | anchor-robust, 30 OOM (sharpens) |
| Dimensionless prefactor (×Δ_BCS) | 25.5 is a computable inter-band moment (S-a gate, **pending Z₂ pre-flight**, mis-targeted in R1) | 25.5 is NOT shown closable; the only ladder member at the target is the wrong (Higgs) branch ⇒ irreducible at the Leggett branch |

The disagreement has collapsed to: **can the Leggett (branch-3) inter-band BdG gap be Z₂-gauge-invariantly pumped from 11.97× to 25.5× Δ_BCS on the full B2⊕B3 sector?** If yes (and the abundance survives the pump), Reading A wins and the gap closes. If the Z₂ pre-flight fails OR the only mode at 25.5× is the Higgs amplitude branch (which it is, in the current ladder), Reading B wins and the mass-prefactor is irreducible at the DM branch.

---

## 7. Updated lean + the single crux for R3

**Updated honest lean: Reading B, ~60% (down from 65–70% in R1).** I *lowered* my confidence because landau's "which spectral moment?" reframe is correct and his (S-a) corridor is genuinely live — the inter-band sector is a different operator the closures did not wall, and the stiffness-inversion physics is real. I did not lower it further (and did not concede) for three reasons that survived the rebuttal: (1) his specific gate is mis-calibrated (target is 25.5× Δ_BCS, not his [12,16]); (2) the one ladder member at the corrected target is the **Higgs amplitude branch**, and adopting it re-identifies the DM and forfeits both the abundance match and the Z₂-protection — so the ladder does NOT already contain a *Leggett* mode at the target; (3) his corridor's well-posedness hinges on his own un-run wall-#11 Z₂ pre-flight. I would **concede** if landau, in R3, (i) re-targets the gate to 25.5× Δ_BCS, (ii) passes the Z₂-gauge-invariance pre-flight on the full B2⊕B3 sector, and (iii) shows the pumped inter-band gap preserves the Leggett identity (Z₂-odd, abundance-conserving) — that would be a genuine 0-param-prefactor mass anchor with a pre-registrable gate, and Reading B would be wrong.

**The single crux the R3 verdict must resolve:** *Is there a Leggett-branch (B2–B3 inter-band relative-phase) BdG moment that equals the corrected structure-formation target 25.5× Δ_BCS (= 11.85 M_KK), Z₂-gauge-invariantly on the full sector AND preserving the abundance/Z₂-protection — or is the only mode at that scale the Higgs amplitude branch (forcing a DM re-identification that breaks Ω_DM h²=0.120)?* Equivalently: does landau's (S-a) corridor, **re-targeted to the corrected 25.5× and Z₂-pre-flighted**, land a *Leggett* mode at the target, or does the spectrum answer "amplitude branch" — in which case the Leggett-DM mass prefactor is irreducible and Reading B holds. Note that *either* verdict leaves the σ_SI NULL untouched: the falsifier sharpening is settled and does not depend on the crux.
