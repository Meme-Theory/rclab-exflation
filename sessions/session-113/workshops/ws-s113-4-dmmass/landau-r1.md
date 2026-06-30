# WS-S112-4 DMMASS — Round 1 (Reading A)

**Workshop**: WS-S112-4 DMMASS (Session 113 EVOI-frontier campaign)
**Author**: `landau-condensed-matter-theorist` — Round 1, steelman Reading A (surviving mass-anchor mechanism)
**Thesis (one line)**: The four closed corridors (NSR / Imry-Ma / PBH-from-fold / CFL) all attacked the *same* upward-pump on the *single* (0,0) gap scale, and all died for the *same* structural reason — the substrate condensate is strong-coupling **phase-rigid** (`D_s ≫ Δ_BCS`); but the Leggett mode lives in the **multiband B2–B3 sector**, whose spectral ladder is already populated at 1.4–25× Δ_BCS, so a *second-band / inter-band coherence-gap* mechanism (not yet tested, and orthogonal to all four closures) remains a live, **pre-registrable** mass-anchor corridor.

---

## 0. Framing and method (symmetry-first)

I begin where I always begin: order parameter, symmetry-breaking pattern, then the free-energy functional, and only then the dynamics. This matters here because the entire tension is being mis-posed as "find one more knob to multiply `Δ_BCS` by ~170." That framing is the trap the four closures fell into. The substrate-IS picture (`phononic-framing.md`) forces a different question: *which spectral moment of the multiband BdG operator on `(A_K, H_K, D_K)` is the DM rest-mass, and is the ~170 a magnitude the moment can carry?*

**The order-parameter structure.** The condensate order parameter is the BCS gap `Δ` on the (0,0) sector. Its symmetry-breaking pattern is `U(1)_7 → 1` (the phase-boson sector — wall #5, `[iK_7, D_K]=0`). The collective excitation spectrum of *any* multiband superfluid has THREE distinct branches, and the framework has all three:

1. **Anderson–Bogoliubov (phase / Goldstone)** — the gapless acoustic mode; `m_G = 0.070–0.138 M_KK` (atlas-07 vs canonical row). This is the mode the spectral-geometer collab §5 measures the "170×" against.
2. **Higgs (amplitude)** — gapped at `2Δ`; `c_Br5_Higgs3 = 11.465307 M_KK` (S82 Γ-point).
3. **Leggett (inter-band relative phase)** — the B2–B3 inter-band coherence mode (PROVEN classification, S80: *"Leggett mode is an inter-band phase excitation of the B2–B3 substrate sector"*); rest energy `11.97·Δ_BCS = 5.557 M_KK` (LEGGETT-MOMENT-70).

The DM is the Leggett mode (branch 3), CPT-neutral and non-annihilating because it is an inter-band *relative*-phase excitation (Z₂-odd, FORBIDDEN single-quantum decay — 73a + S67). **This is already a multiband object.** The single-band language ("multiply Δ_BCS by 170") is a category error the moment one writes down the order-parameter structure: there is no single-band superfluid here — there are (at least) the B2 (mult 4) and B3 (mult 3) bands, plus B1 (the (0,0) gap-edge), and the Leggett mode is *defined by* the relative phase between them.

This is the first-principles content of my pole: **the mass-anchor lives in the inter-band sector, and the inter-band sector has its own gap scale that none of the four closures touched.**

---

## 1. What the four closures actually ruled out (constraint-map geometry, not defeat)

Per the PI directive in my memory and `epistemic-discipline.md`: a closed corridor is a *wall* whose orientation I must read, not a count I tally. I authored two of these four walls myself (INV5-W2-2, INV5-W2-4), so I can state their orientation exactly.

| Corridor | Gate | Why it failed | **Orientation of the wall** |
|:---------|:-----|:--------------|:----------------------------|
| **NSR pseudogap two-scale (B-3)** | INV5-W2-2 | SIGN inverted: `Δ_pg − m_Meissner = −2.057 < 0`. The (0,0) gap is the *small* scale; phase-stiffness `D_s` is large (`m_Meissner = √D_s = 2.521 M_KK`). | Rules out raising the mass by **promoting the single-particle pseudogap of the (0,0) band**. The condensate is phase-RIGID, so `Δ_pg` cannot be pumped up. |
| **Imry-Ma disorder Goldstone (B-4)** | INV5-W2-4 | Disorder mass ~43× *smaller* than the bare anchor (`enh = 0.0231`); only the physically-unjustified construction E (C²-backbone-as-disorder) reached 6.76×, still 30× short. | Rules out raising the mass by **disorder-inducing a Goldstone mass**. The substrate is the ORDER (weak-disorder regime); there is no random-field reservoir. |
| **PBH-from-fold** | (inv-8/inv-11) | 37 OOM below the DM window. | Rules out a **gravitational-collapse seed** route — a wholly different (non-condensed-matter) mechanism. |
| **CFL mass-anchor** | (CFL pillar) | "soft" — CFL gap too small to anchor the magnitude. | Rules out **importing the high-density-QCD CFL gap** as the DM scale. |

**The decisive structural read.** B-3 and B-4 are *the same wall seen twice*. Both are **upward pumps on the (0,0) single-particle / phase sector**, and both are defeated by the *one* fact: `D_s ≫ Δ_BCS` (strong-coupling, BEC-side, `μ/E_F = 0.192`). The condensate is phase-rigid: you cannot grow the single-particle gap (B-3), and there is no disorder to soften the phase into a massive mode (B-4). PBH and CFL are not condensed-matter mechanisms at all — they are an external seed and an external gap import.

**What survives by elimination.** A surviving mechanism must NOT be another upward pump on the (0,0) phase/single-particle sector (that region is walled). It must instead be one of:

- **(S-a) An inter-band / second-band gap** — a *different spectral sector* (B2–B3 relative-phase gap, or a higher Peter–Weyl (p,q) sector's pairing gap) whose magnitude is set by inter-band physics, not the (0,0) single-particle gap. **Untested.**
- **(S-b) A transport/transfer-degree** — the ~170 is not a *pairing*-gap enhancement at all but a substrate→observable transport degree, exactly as `M_DM_Leggett_GeV = 4.13e17 GeV` already requires a 54.04-decade map from the M_KK-unit rest energy. **Reading-B-adjacent but pre-registrable as a degree, not a fit.**

I steelman (S-a) as the primary surviving mechanism and hold (S-b) as the fallback that *still* makes the magnitude substrate-derived.

---

## 2. The primary surviving mechanism: inter-band (Leggett) coherence-gap, not single-particle gap

### 2.1 The physics the closures skipped

In a multiband BCS condensate (Leggett 1966; Strinati 2018, corpus paper #25; the two-band MgB₂ analog I worked in S100b W6-3), the **Leggett mode frequency** is NOT set by the single-band gap `Δ`. It is set by the **inter-band Josephson coupling** `J_12` and the relative compressibility:

```
ω_Leggett² = (4 Δ_1 Δ_2 / J_12) · (n_1^{-1} + n_2^{-1})^{-1} · γ_12        (Eq. 1)
```

where `γ_12` is the inter-band pair-transfer amplitude and `n_a` are the band DOS at the gap edge. The key structural point: `ω_Leggett` can be **parametrically larger than `2Δ`** when the inter-band coupling `J_12` is weak relative to the intra-band couplings (the "stiff relative phase" regime) — this is the *opposite* sign-sensitivity from the Anderson–Bogoliubov mode, and it is exactly the regime the substrate sits in (`D_s ≫ Δ_BCS` means the phase sector is STIFF).

**This is the crucial inversion of the B-3 wall.** B-3 (INV5-W2-2) found `D_s ≫ Δ_pg` and read it as a *failure* (the single-particle pseudogap is small). But for the **inter-band Leggett mode**, large phase-stiffness is precisely what PUSHES `ω_Leggett` UP, because a stiff relative phase resists inter-band counterflow. The same fact (`D_s` large) that closed B-3 *opens* the Leggett-gap corridor. The wall I built in INV5-W2-2 is oriented *toward* this corridor, not against it — I read it as "the gap is small" but the physically operative DM-mass object is the inter-band coherence gap, which large stiffness amplifies.

### 2.2 The siblings are already on the ladder

The framework has already computed Leggett-mode siblings at scales that bracket the target:

- `c_Br4_Higgs2 = 1.409507 M_KK` (Higgs–Leggett hybrid Γ-point; ω_H2 = 1.410) — **3.04× Δ_BCS**
- `Mass_LeggettDM = 11.97·Δ_BCS = 5.557 M_KK` (S70 anchor) — **11.97× Δ_BCS**
- `c_Br5_Higgs3 = 11.465307 M_KK` (BCS-Higgs amplitude Γ-point) — **24.7× Δ_BCS**

The multiband collective spectrum already spans `3–25× Δ_BCS` at the Γ-point *with zero free parameters*. The "170×" target (against the Goldstone `m_G`, per collab §5) corresponds to `~12–14× Δ_BCS` in the *Leggett-anchor-relative* metric (`170/11.97 = 14.20`, the two-anchor target `r` in INV5-W2-2). **`14.2× Δ_BCS = 6.59 M_KK` sits squarely inside the already-populated `3–25× Δ_BCS` Γ-point ladder.** It is between the Leggett anchor (11.97) and the upper Higgs (24.7).

This is the strongest single fact for Reading A: **the required scale is not exotic — it is already inside the framework's own computed multiband collective spectrum.** The 170× is not "170× too small"; it is a mis-identification of *which moment* of the multiband BdG operator is the structure-formation mass. The collab §5 measures 170 against the *Goldstone* (the wrong branch — branch 1, the gapless mode); measured against the inter-band ladder (branch 3), the target is an O(10) moment that is already realized in siblings.

### 2.3 Why it evades each closure

- **Evades B-3 (NSR pseudogap):** B-3 promoted the *single-particle* pseudogap `Δ_pg` of the (0,0) band and found it small (phase-rigid). The Leggett-gap mechanism uses the *inter-band relative-phase* gap (Eq. 1), which *grows* with stiffness. Different operator, orthogonal sign-response. The 2-bit `(L_max-FLAT, m_PV-FLOWING)` fingerprint discipline (`regulator-pin-discipline.md §22`) applies: this is a genuinely-different operator, not a regulator-class shift of the same one.
- **Evades B-4 (Imry-Ma):** B-4 needed a disorder reservoir to mass a Goldstone; the Leggett gap is an *intrinsic* inter-band gap (clean limit), present at zero disorder. No disorder reservoir required; the weak-disorder verdict is irrelevant.
- **Evades PBH-from-fold:** entirely different mechanism (gravitational vs spectral). No overlap.
- **Evades CFL:** CFL imports an *external* gap; the Leggett gap is the substrate's *own* inter-band moment. No import.

### 2.4 Pre-registrable gate (the deliverable Reading A owes)

**Gate `S113-LEGGETT-INTERBAND-GAP-DM` (proposed):**

- **Substrate-IS observable**: the inter-band Leggett-mode frequency `ω_Leggett^{B2-B3}` computed from the *full multiband BdG operator* on the B2 (mult 4) ⊕ B3 (mult 3) sector at τ_fold = 0.190, via Eq. (1) with `J_12`, `Δ_2`, `Δ_3`, `n_2`, `n_3` extracted from the L_max=10 (or L12 cache) D_K spectrum — NOT the single-band (0,0) Δ_BCS.
- **Pre-registered PASS criterion**: `ω_Leggett^{B2-B3} / Δ_BCS ∈ [12, 16]` (the two-anchor target band `170/11.97 = 14.20 ± ~14%`, bracketing the structure-formation requirement). **PASS** ⇒ the inter-band gap supplies the structure-formation mass at zero free parameters; **FAIL** ⇒ corridor (S-a) closes and Reading B sharpens.
- **Machinery pins**: the BdG multiband construction (B2⊕B3 sector), `J_12` from the inter-band pair-transfer matrix element (the S82 W2-11 2-sector/1-bond Josephson — **caveat below**), `Δ_2, Δ_3` from the per-band Richardson–Gaudin gap (exact solution, PROVEN to work, S39).
- **Falsifiability**: a single pre-registered band; no convention freedom (the BdG operator and the cache are fixed).

**Honest threat to my own gate (the strongest counter I must surface):** my wall #11 (S82 W2-11, Z₂ gauge degeneracy on the 2-sector/1-bond Josephson projection) proved that the projected 2-sector/1-bond subspace cannot discriminate s++ vs s+- pairing — the inter-band phase is gauge-degenerate *on that projection*. If `J_12` is sourced from that same projected Josephson element, the Leggett-gap value may be gauge-ambiguous (the relative-phase observable is exactly what the Z₂ degeneracy scrambles). **The gate is only well-posed if `ω_Leggett^{B2-B3}` is computed from the FULL B2⊕B3 BdG spectrum (not the projected 1-bond subspace), where the Z₂ degeneracy is lifted by the full inter-band kinetic structure.** This is a real, pre-flightable risk: a Stage-1 dry-run must verify the Leggett observable is Z₂-gauge-invariant on the full sector before the gate is dispatched. I flag it because hiding it would be exactly the convention-shopping the rules forbid.

---

## 3. The fallback: transport-degree, not pairing-gap (the magnitude is still substrate-derived)

If the inter-band gap (S-a) lands below the band, Reading A is *not* defeated — it retreats to (S-b), which is structurally adjacent to Reading B but keeps the magnitude substrate-derived rather than free.

The framework ALREADY carries a substrate→lab transport map for this exact object: `M_DM_Leggett_GeV = Mass_LeggettDM/Δ_BCS · Δ_BCS · M_KK = 11.97 · 0.4643 · 7.43e16 = 4.13e17 GeV`. That is a **54-decade unit map** from the dimensionless M_KK-unit rest energy to the lab rest energy — and per the per-observable transport-degree theorem (`cross-pillar-bridge-anatomy.md §23`), the substrate-scale value and the structure-formation-scale value need NOT coincide: they differ by `deg(T_{BZ→structure})`, a substrate-natural morphism, NOT a fit.

**The reframe.** The "170×" is plausibly the **parity-selected, mass-dimension-indexed transport degree** between the substrate-IS Leggett rest energy (a `d_A = 1` mass-dimension-1 object, on the sign-locked `M_KK^1` scale leg per §23.0(5)) and the structure-formation free-streaming scale. A `d_A = 1` observable is forced onto the odd scale leg; the morphism sector (even-degree Wodzicki/HKR) cannot correct it — so a fixed, parity-determined factor between the substrate rest mass and the structure-formation mass is *exactly what §23's parity selection rule predicts*. The 170 would then be a **computable transport degree on the odd `M_KK^1` leg**, with a pre-registrable gate: compute `deg(T)` from the free-streaming/transfer-function bridge map and check `M_KK^{deg}` against 170.

This is weaker than (S-a) — it concedes the mass is not a pairing-gap moment — but it is still a *substrate-derived magnitude with a parity-fixed degree*, NOT an unanchored free scale. The difference from Reading B is precise: Reading B says "abundance-fixed, magnitude-FREE"; (S-b) says "abundance-fixed, magnitude fixed by a parity-selected transport degree the framework's own §23 machinery computes."

---

## 4. Engaging the strongest threat (the inter-band-coherence-scale = magnitude-free argument)

The hardest version of Reading B (which mack-cosmic-bridge will press in R2): *the Leggett mode is an inter-band coherence scale, and inter-band coherence scales are abundance-fixed but magnitude-free — structurally like M_KK, which the framework just conceded it cannot derive from within (the M_KK magnitude import).* On this reading, the 170× is not a gap to close but a *feature*: the substrate fixes the Leggett mode's *existence* (and hence the relic abundance, via n_pairs = 59.8 saturated, Ω_DM h² = 0.120, the 0.6% Planck match) but not its *magnitude*, because no single dimensional handle (N₃ = 0) can fix a dimensionful scale.

**My honest response.** This is the genuinely strong threat, and it has real force: the abundance match (§VII C7/C11) uses `n_pairs` (a *count*, dimensionless) and the partition fraction (dimensionless) — it does NOT use the Leggett *mass* magnitude. So the abundance is provably mass-magnitude-independent, which is exactly Reading B's wedge: the framework's DM *success* (abundance) does not depend on the *contested* quantity (mass). That asymmetry is real and I cannot wish it away.

But the threat is **not symmetric with M_KK**, for one structural reason: M_KK has `N₃ = 0` — a *single* dimensional handle, no second scale to form a ratio. The Leggett sector does NOT: it has the **full multiband ladder** (B1, B2, B3 gaps; the Higgs amplitude; the Anderson–Bogoliubov speed). The Leggett mass is `11.97·Δ_BCS`, and `Δ_BCS = 0.4643` is itself a *derived* ratio (BCS-GAP-CANONICAL-70, R-protected). So the Leggett mass is *already* a substrate-derived dimensionless ratio `× M_KK` — the M_KK import is the SAME single import the whole framework makes once; the *11.97* and the candidate *14.2* are dimensionless and live inside the spectrum. The question is therefore NOT "can the substrate fix a dimensionful scale" (it can't, and doesn't need to — it imports M_KK once). The question is the **dimensionless** one: "is the structure-formation mass a computable dimensionless moment (`~14.2`) of the multiband BdG operator?" That is a finite spectral computation, not a dimensional-handle obstruction. Reading B's M_KK analogy smuggles in the *dimensionful* obstruction where the actual open question is *dimensionless* — and dimensionless ratios are exactly what the framework derives best (g1/g2, n_s, phi_paasch, the entire §VII ladder).

So the steelman stands: the magnitude question reduces to a dimensionless inter-band moment, which (S-a) makes pre-registrable.

---

## 5. Closing

### (i) Honest current lean

**Leaning Reading-A-at-the-inter-band-moment, but with a real and specific liability I will not hide.** The constraint-map geometry genuinely favors a surviving mechanism: the four closures all walled the *single-band (0,0) phase/single-particle sector* and the *external-import* sector, leaving the **inter-band B2–B3 coherence-gap sector untested** — and that sector's already-computed siblings (3–25× Δ_BCS at the Γ-point) bracket the `~14.2× Δ_BCS` target. The required scale is *inside the framework's own multiband spectrum*; it is not exotic. This is a structurally strong position for a pole that is usually the one demanding rigor.

The liability is equally specific: my own wall #11 (Z₂ gauge degeneracy on the projected inter-band Josephson) is exactly positioned to scramble the relative-phase observable the Leggett-gap mechanism needs. The gate is well-posed *only* on the full B2⊕B3 BdG sector (not the projected subspace), and a Stage-1 dry-run must confirm Z₂-gauge-invariance of `ω_Leggett^{B2-B3}` before dispatch. If that pre-flight fails, (S-a) collapses to (S-b) — and (S-b) still keeps the magnitude substrate-derived (a parity-selected transport degree, §23.0(5)), not free.

I do NOT lean to "irreducibly unanchored." Reading B's strongest argument (the M_KK analogy) conflates a *dimensionful* obstruction (N₃ = 0, single handle) with the actual *dimensionless* open question (which multiband moment is the structure mass). The Leggett sector has a full ladder, not a single handle; the obstruction does not transfer.

### (ii) The single most decisive consideration

**The "170×" is measured against the wrong collective branch.** The spectral-geometer collab §5 (the source of the 170 figure) computes it against the **Goldstone mode** `m_G = 0.070 M_KK` (branch 1, the *gapless* Anderson–Bogoliubov phase mode) — but the DM is the **Leggett mode** (branch 3, the *gapped* inter-band relative-phase mode), and against the Leggett anchor the target is only `170/11.97 = 14.20× Δ_BCS`, which sits inside the framework's already-computed Γ-point multiband ladder (Higgs–Leggett hybrid at 3.04×, Leggett at 11.97×, Higgs at 24.7×). Whether the inter-band BdG operator on the B2⊕B3 sector actually realizes a `~14.2× Δ_BCS` coherence-gap moment — Z₂-gauge-invariantly on the full sector — is the single computation that decides the workshop. It is finite, pre-registrable, and convention-free. **The mass problem is, at root, a "which spectral moment?" question, and that is a question the substrate answers by diagonalization, not by import.**
