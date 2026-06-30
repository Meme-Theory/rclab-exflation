# WS-S112-4 DMMASS — Round 2 (rebuttal)

**Author**: `landau-condensed-matter-theorist` — Round 2, rebuttal
**Posture**: Reading-A pole, engaging mack's Reading-B (irreducibly-unanchored) case at its strongest, with a major in-round correction forced by the provenance of the "170."

**One-line update**: Mack's *bridge-map distinction* (§3.1) is the correct load-bearing axis and I concede it largely defeats my R1's "inter-band ratio anchors the magnitude in GeV" framing — BUT tracing the provenance of the "170" reveals it is the **n_s SA-Goldstone target (Wall W9), not a DM structure-formation requirement**, which means neither the abundance NOR the σ_SI falsifier depends on it, and the honest verdict is sharper than either R1: the *DM* mass has **no independent 170× problem at all** — the 170 is an n_s-sector number transplanted onto the DM sector without a DM-internal derivation.

---

## 1. Conceding mack's strongest point cleanly (the bridge-map distinction)

Mack's decisive move is his §3.1, and I will not strawman it by retreating to "some mechanism will turn up." His point, stated precisely:

> `11.97` is BdG-**internal** (both numerator `Mass_LeggettDM` and denominator `Δ_BCS` are substrate-IS spectral-triple observables). The candidate 170 is a **bridge-map ratio**: `m_required/m_Leggett` with a substrate-IS denominator and a numerator `m_required` set *outside* the BdG sector. To *predict* 170, a mechanism must derive `m_required` itself — a different and harder derivation than an internal gap ratio.

This is correct as a structural taxonomy, and it directly punctures my R1 §2.2/§4 claim that "`14.2× Δ_BCS` sits inside the already-computed multiband ladder, therefore the mass is anchored." **Sitting inside the ladder is necessary but not sufficient.** Even if the inter-band BdG operator on B2⊕B3 produces a coherence-gap moment at exactly `14.2× Δ_BCS`, that would only anchor the moment *as a dimensionless multiple of M_KK* — the magnitude in GeV would still ride M_KK (`M_DM = 5.557·M_KK`), exactly as mack's structural-ledger row 4 shows. My R1 conflated "the dimensionless moment is computable" (true, and my contribution) with "the magnitude is anchored" (false — the magnitude rides the single M_KK import). I retract the stronger claim.

So on the **magnitude-in-GeV** question, mack is right and I concede: the DM mass magnitude inherits M_KK's permanent-external fate (S112 `CF-S112-MKK-SUBSTRATE-ANCHOR` FAIL). No condensed-matter pairing/gap mechanism on a finite spectral triple supplies a dimensionful scale — the calculus is ratio-valued. The four closed corridors are the structural signature of that wall, as mack argues in §1a. I authored two of them and I agree with his reading of why they failed.

**But** the concession is narrower than mack's verdict claims, and the reason is the provenance of the "170" — which neither R1 traced to its origin.

---

## 2. The decisive in-round finding: the "170" is the n_s Wall-W9 number, NOT a DM structure-formation requirement

I traced `m_required` to its definition. It is **not** a dark-matter quantity. From four independent framework sources:

- **atlas-05 §W9** (Convex Combination Theorem, S51): *"The obstruction is the mass problem: K_pivot/K* = 22.9, placing the Goldstone deep in its K⁻² regime. The Goldstone mass 0.070 M_KK is 170x below the required 11.85 M_KK."* — `m_required` is the mass the **SA-Goldstone mixing model needs to produce `n_s = 0.965` at `K_pivot = 2.0 M_KK`**.
- **atlas-string-collab §3**: *"The Goldstone mass m_L = 0.070 M_KK ... is 170x below the m_required = 11.85 M_KK needed for **n_s = 0.965** at K_pivot = 2.0."*
- **atlas-spectral-geometer-collab §5**: the 170 is *"between the Goldstone mass (a collective excitation) and the mass required for **n_s = 0.965** at K_pivot = 2.0"* — and the collab explicitly notes Window 1 (remap K_pivot < K* = 0.087) *"avoids the 170x problem entirely."*
- **atlas-nazarewicz-collab §3**: *"The mass problem (m_required/m_Leggett = 11.85/0.070 = 170x, Wall W9) asks whether any mechanism can enhance the **Goldstone** mass by a factor of 170."*

So the canonical "170×" is:

```
170  =  m_required / m_G  =  11.85 M_KK / 0.070 M_KK            (Eq. 1)
        [SA-Goldstone n_s=0.965 target] / [Anderson-Bogoliubov Goldstone mass]
```

**This is an n_s spectral-tilt wall on the gapless branch, and it already has a door** — Window 1 / EFOLD-MAPPING-52 (remap K_pivot to K < K*, where both correlators are flat and `n_s = 0.965` is achievable with β > 0.9 without the Goldstone reaching 11.85). The n_s "170× problem" is NOT a standing open gap; it is a wall with a documented escape.

### 2.1 How the n_s number got transplanted onto the DM sector

The DM Leggett anchor is a **separate, later** object: `Mass_LeggettDM/Δ_BCS = 11.97` (S70, the *gapped* Leggett inter-band branch). The conflation happens in exactly one place — **atlas-04 P2** lists *both* in the same CONDITIONAL cell: *"mass problem 170x. **S70 LEGGETT-MOMENT** anchors Mass_LeggettDM/Δ_BCS = 11.97."* Two distinct numbers (the n_s wall's 170, the DM anchor's 11.97) in one sentence.

Then **inv-5 W2** (the actual DM excursion — which I authored) *re-purposed* the 170 as a DM "structure-formation target" WITHOUT an independent structure-formation derivation. The WP is explicit (line 80): *"`m_required/m_Leggett = 170` confirmed as atlas-spectral-geometer-collab §5 equation (NOT a canonical pin; **consumed as the structure-formation target**)."* It defines `m_struct = 170·Δ_BCS = 78.92 M_KK` and the two-anchor target `r = 170/11.97 = 14.20`. **The "structure-formation" label is inv-5's own relabeling of the n_s number; collab §5 (its cited source) calls it the `n_s = 0.965` requirement, not a free-streaming/structure-suppression constraint.**

This matters for mack's bridge-map argument, and it cuts both ways:

- **Against mack's stated rationale (§3.1):** mack wrote that `m_required` is *"set by the free-streaming / structure-suppression requirement (a measured cosmological constraint)"* — i.e., laboratory-IN. **That is not what `m_required` is.** It is the SA-Goldstone *n_s-mixing* target keyed to `K_pivot = 2.0 M_KK` — a substrate-MODEL scale, not a laboratory free-streaming measurement. There is no DESI/Lyman-α/half-mode warm-DM bound that sets 11.85 M_KK. Mack's conclusion (bridge-map, not internal) may still hold, but his *reason* (it's a measured cosmological constraint) is factually wrong; the numerator is a substrate-model n_s target, not a lab observable.

- **Against my R1:** the target I claimed `14.2× Δ_BCS` should hit is the **n_s-sector number**, transplanted. It is neither a clean substrate-IS-internal DM ratio nor a clean laboratory-IN DM constraint — it is a number from a *different observable* (n_s) imported into the DM sector. My R1 "the required DM mass is inside the multiband ladder" is built on a target of *contested applicability to DM at all*.

### 2.2 The sharper truth: does the DM mass even HAVE a 170× problem?

Here is the rebuttal's central claim, forced by the provenance: **the dark-matter Leggett mass has no independently-derived 170× shortfall.** The DM sector's substrate-IS deliverables are:

- abundance `Ω_DM h² = 0.120` (0.6% match) — uses `n_pairs = 59.8` (a count) and the partition fraction (dimensionless); **mass-magnitude-independent** (mack's ledger, correct);
- the rest-mass *ratio* `11.97·Δ_BCS` (dimensionless, PROVEN);
- `σ_SI = 1.299e-63 cm²` NULL — gravitational floor, **mass-anchor-robust by ≥26.5 OOM** (mack's Sage stress-test, which I accept).

**None of these three has a 170× shortfall.** The 170 enters ONLY through the inv-5 relabeling of the n_s-sector `m_required` as a DM "structure-formation target" — and that relabeling has no DM-internal derivation. There is no free-streaming computation in the framework that says the Leggett DM must be `170×` heavier than `m_G` (or `14.2×` heavier than `Δ_BCS`) for *structure formation*. The structure-formation requirement on DM is about the free-streaming length / half-mode mass, and **that computation has not been done against the Leggett mass** — what was done (inv-5) imported the n_s number as a proxy.

So my honest position inverts: I am NOT defending "a surviving mechanism supplies the DM 170× magnitude." I am asserting **the DM 170× is a phantom of registry-cell conflation** — the real 170× is the n_s Wall-W9 (which has Window-1 escape), and the DM mass's actual open question is the *magnitude-in-GeV* (which mack correctly attributes to the M_KK import).

---

## 3. Where this leaves each pole (honest re-scoring)

### What mack gets right (and I now agree)

1. The DM mass **magnitude in GeV rides M_KK** (`5.557·M_KK`) and inherits the permanent-external fate. No condensed-matter mechanism supplies it. **Conceded.**
2. The four closed corridors fail on the ratio-vs-magnitude axis. **Agreed** (I authored two).
3. The σ_SI NULL is **mass-anchor-robust** and the unanchored reading **sharpens** it. **Agreed** — his Sage stress-test (≥26.5 OOM across the 170×-wide window, exclusion frozen) is sound; the gravitational floor `σ ~ (G_N M_DM m_Xe)²/π` is structural because `G_N = 6.7e-39 GeV⁻²` is tiny in particle units. I have no rebuttal to this and it is the strongest single result in the workshop.

### What mack's verdict over-claims

4. Mack frames the 170× as a real "shortfall" that the unanchored reading *dissolves into a structural feature parallel to M_KK*. **The provenance shows the DM 170× was never a substrate-derived DM requirement** — it is the n_s Wall-W9 number transplanted. So the correct verdict is not "the DM mass-shortfall is a structural feature like M_KK" but "**there is no DM mass-shortfall to begin with**; the 170 belongs to the n_s mechanism (where it has a Window-1 door), and the DM mass's only open question is the magnitude-in-GeV = the M_KK import." This is a *cleaner* result than mack's and removes a phantom open gap from the DM ledger.

5. Mack's bridge-map *rationale* (numerator = measured free-streaming constraint) is factually off; the numerator is an n_s-model target. The bridge-map *conclusion* survives but should be restated: the 170 is a **cross-observable transplant** (n_s-sector → DM-sector), not a substrate-IS-vs-laboratory-IN bridge.

### What survives of my Reading-A

6. The **inter-band Leggett-gap moment** (R1 §2, gate `S113-LEGGETT-INTERBAND-GAP-DM`) is still a real, pre-registrable computation — but its *purpose* is now corrected. It does NOT "anchor the DM mass magnitude" (conceded to mack). Its value is to test whether the **n_s SA-Goldstone target `14.2× Δ_BCS` is realized by an inter-band coherence moment** — i.e., it is an **n_s-sector gate**, not a DM-sector gate. If `ω_Leggett^{B2-B3}/Δ_BCS ∈ [12,16]`, it would supply the W9 `m_required` from the gapped inter-band branch (rather than demanding it of the gapless Goldstone), reopening the *additive-mixing n_s route* without Window-1 remapping. That is a genuine forward gate, but it lives in the n_s sector, and it does not touch the DM magnitude or the σ_SI NULL.

---

## 4. Updated lean + the single crux for R3

### Updated honest lean

**On the DM mass MAGNITUDE: I concede Reading B.** The magnitude in GeV is `5.557·M_KK`, a dimensionless multiple of the single M_KK import; it inherits M_KK's permanent-external status (S112 keystone FAIL); no condensed-matter pairing/gap mechanism supplies a dimensionful scale; the four closures confirm the wall. My R1's "surviving mechanism anchors the magnitude" is wrong and I retract it.

**On the framing of the gap itself: I now hold a position SHARPER than either R1.** The "170× DM-mass shortfall" is **mis-attributed**. The 170 is the n_s Wall-W9 ratio (`m_required(SA-Goldstone, n_s=0.965, K_pivot=2.0) / m_G = 11.85/0.070`), which has a documented Window-1 escape. It was transplanted onto the DM sector by registry-cell conflation (atlas-04 P2) and inv-5's relabeling, with **no independent DM structure-formation derivation**. The DM sector's three real deliverables (abundance, the 11.97 ratio, the σ_SI NULL) **have no 170× shortfall** — abundance and σ_SI are mass-magnitude-independent (mack, correct), and the 11.97 ratio is itself PROVEN at zero free parameters. The DM mass's *only* open question is the magnitude-in-GeV, which is the M_KK import, full stop.

So I do **not** concede "irreducibly unanchored DM mass-shortfall" as mack frames it — because there is no DM mass-shortfall. I concede the strictly correct sub-claim ("the DM magnitude rides M_KK") and replace mack's "structural feature parallel to M_KK" with the cleaner "the DM 170× is a phantom; the 170 is the n_s wall."

### The single crux R3 must resolve

**Is the "170× DM-mass shortfall" a genuine dark-matter requirement, or is it the n_s Wall-W9 number (m_required for n_s=0.965 at K_pivot=2.0, vs the Goldstone m_G=0.070) transplanted onto the DM sector without a DM-internal structure-formation derivation?**

- If **transplanted (my R2 finding)**: HK-170X-DM should be **re-scoped/closed as mis-attributed** — the n_s 170× has Window-1 escape (EFOLD-MAPPING-52); the DM mass's only open item is the magnitude = M_KK import; the σ_SI NULL is anchor-robust regardless. The DM ledger loses a phantom open gap.
- If **a genuine DM requirement (mack's framing, if an independent free-streaming derivation exists that I did not find)**: then mack's verdict stands — abundance-fixed/magnitude-unanchored, σ_SI sharpens, parallel to M_KK.

The decider is purely a **provenance/derivation question, answerable from the ledger**: does any framework computation derive a `170×` (or `14.2× Δ_BCS`) DM mass requirement from a *structure-formation / free-streaming* argument that is **independent of the n_s SA-Goldstone `m_required`**? My trace says NO (every source roots the 170 in the `n_s=0.965` SA-Goldstone target; inv-5 imported it as a proxy). If R3 confirms NO, the workshop's structural verdict is the re-scoping; if R3 finds an independent DM free-streaming derivation, the verdict is mack's sharpened-falsifier statement. Either way, the σ_SI NULL is anchor-robust and the DM magnitude rides M_KK — those two are settled.
