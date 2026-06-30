# S95 Workshop Campaign — Slot 1 / Entry S-3 (SOLO structural verdict)

**Agent**: Hawking-Theorist (black-hole thermodynamics / semiclassical-gravity / analog-gravity specialist)
**Mode**: SOLO synthesis/review — sole author of this file; no coordination with other reviewers.
**Date**: 2026-05-29
**Sources read in full**: `sessions/archive/session-95/session-95-w4-workingpaper.md` (§W4-1 … §W4-5 + Wave-4 synthesis); `computations/session-95/s95_gate_verdicts.txt` (all W4 lines incl. Option-A supersession chains); corpus `sessions/framework/Collabs/equation-build/transit-flow-genesis-to-now.md §"The two horizons"`.
**Feeds**: §6.2 doc-integration analog-T ledger (HAW-V1).
**Scope guard honored**: I do NOT re-open the W4-1 C1→ASYMMETRIC verdict (N_zeros=1) or the W4-2 3-surface PLACE dispositions. Only the **entry-κ definition** is adjudicated.

---

## 1. The divergence, stated precisely

Two PASS gates compute a surface gravity for "the entry surface" and land **25× apart**:

| Gate | κ_entry (M_KK) | T_a = κ/2π (M_KK) | Method | τ of the surface | Verdict line |
|:-----|:---------------|:------------------|:-------|:-----------------|:-------------|
| **W4-1** (S95-W4-1-WHITE-HOLE-KINEMATIC-CONSISTENCY) | **+18.520** | **2.948** | Visser ½∂_n(c²−v²) of the **BLV-scalar discriminant**; c=c_BLV=0.485 held CONSTANT, only v(τ) varies; outward normal n=−τ (raw ∂_τ=−37.04 → oriented ∂_n=+37.04) | **τ₀ = 0.112466** | LIVE PASS, audit short `5d1ac75a` |
| **W4-2** (S95-W4-2-HAWKING-ANALOG-T-LEDGER, row 1) | **457.6562** | **72.8383** | S71 velocity-gradient κ_v = \|dv/dτ\|_entry (10-pt spectral-action data; dv/dτ = −(dS/dτ)/(M_ATDHFB·v)) | **τ = 0.2195** | PASS, audit `e5030430…` |

The plan §W4-2 said both gates "SHOULD reuse one `surface_gravity` helper," yet they produced surface gravities 25× apart. The adjudication question: **one canonical entry temperature, or two legitimately-distinct surface gravities on two distinct surfaces?**

---

## 2. The decisive derivation — Visser surface gravity under constant c

This is the load-bearing substitution chain (`math-scripts.md §"Double-Check Logic Before Compute"`). Sage-exact reduction (`sage_eval`, this session):

```
Def 1 (Visser/BLV surface gravity):   κ = ½ |∂_n (c² − v²)|        [Barceló-Liberati-Visser 2005, Paper 16]
Def 2 (the flow):                     c = c_BLV = const  ⇒  ∂_n c² = 0 ;   only v = v(τ) varies
Step 3 (substitute Def 2 into Def 1): κ = ½ |∂_n(c² − v²)| = ½ |0 − 2 v ∂_n v| = | v · ∂_n v |
Step 4 (evaluate at the Mach-1 / sonic surface, where v = c):
                                      κ_sonic = | c · ∂_n v |  =  c · |dv/dn|
Step 5 (read off):                    Under constant c, the Visser surface gravity REDUCES to
                                      κ = c · |dv/dn|   —   it carries an EXPLICIT factor of c.
                                      It does NOT reduce to |dv/dn| alone, and NOT to |dv/dn|/c.
```

Sage output (verbatim): `kappa (general normal n, c const) = -dvdn*v`; `kappa at sonic surface v=c = -c*dvdn`. The sign is pure orientation/normal-convention bookkeeping (white-hole outflow ⇒ |κ|); the **magnitude is `c·|dv/dn|`, unconditionally**.

**Consequence for the two definitions in play.** The framework corpus carries TWO surface-gravity conventions, both standard in analog gravity:

- **Visser/BLV form** (Paper 16, BLV 2005; `Phononic-Crystal-Geometry.md`; `framework-paasch-potential-hawking-collab.md`): `κ = c_s·(dv/dx)|_horizon`. This is exactly the reduction of ½∂_n(c²−v²) above.
- **Bare velocity-gradient form** (S73A: `κ_entry = (dv_g/dτ) at τ_entry`, `κ_eff(k_i) = dv_g/dτ`; S71-adopted `κ_v`): `κ = |dv/dτ|` — **no factor c**.

The two differ by exactly the factor **c_BLV = 0.485** (Sage-exact). This factor is the entire origin of the apparent "25× discrepancy" once the surface-τ difference is also accounted for.

---

## 3. Confronting each number against the reduction

### W4-1 (18.520 → 2.948) IS a correct Visser κ — of its OWN crossing
At the BLV-discriminant crossing τ₀=0.112466, the script reports oriented ∂_n(c²−v²)=+37.040. Then κ = ½·37.040 = 18.520 = c_BLV·|dv/dn| with |dv/dn| = 18.520/0.485 = **38.19** at that point (Sage-exact). This is **internally consistent and correct**: W4-1 applies the literal Visser formula and gets the literal Visser surface gravity of the surface where the *BLV scalar* v(τ) (with c=c_BLV constant) first reaches Mach 1. T_a = 18.520/2π = **2.948 M_KK** is the genuine Visser analog temperature **of that surface**. It "matches no corpus value" simply because the corpus never registered a named temperature for this particular crossing.

### W4-2 (457.656 → 72.838) is NOT a Visser κ — it is the BARE gradient at a DIFFERENT surface
W4-2 row-1 adopts κ_entry = κ_v = |dv/dτ| = 457.656 — the **bare** velocity-gradient (no factor c). It reproduces the corpus `T_entry = κ_v/2π = 72.8 M_KK` to 0.052%. Two independent checks confirm 457.656 is the bare gradient, not a Visser κ:
1. If 457.656 were already a Visser-c κ, applying Visser consistently would be a no-op; but the column header in the W4-2 ledger literally writes `κ = ½∂_n(c²−v²)`, the Visser form. Applying THAT form to the surface's |dv/dτ| gives c_BLV·457.656 = **221.96** → T = **35.3 M_KK** — which matches **no corpus value**. Hence 457.656 cannot be the Visser κ; it is the bare |dv/dτ|.
2. The corpus row (`transit-flow-genesis-to-now.md`) labels it "**pure kinematic**" and `κ_v`, the S71-adopted bare-gradient definition.

### The two surfaces are physically distinct (not one surface evaluated twice)
- W4-1 crossing: **τ₀ = 0.112466** (BLV-scalar discriminant, c=c_BLV constant).
- W4-2 / corpus entry: **τ = 0.2195** (a₂-kinematic, S71 W2-C, where BCS-mode group velocity = modulus velocity).
- |Δτ| = **0.107** — these are different points on the transit trajectory, controlled (corpus) by the a₂ moment at 0.2195 vs a free BLV-scalar Mach-1 condition at 0.1125.

### The full 2×2 matrix (Sage-exact, this session)
The divergence is separated along **two orthogonal axes simultaneously** — surface AND κ-convention:

| | Visser κ = c·\|dv/dn\| | bare κ = \|dv/dn\| |
|:--|:--|:--|
| **Surface A** — BLV-discriminant, τ₀=0.1125, \|dv/dn\|=38.19 | κ=18.520 → **T=2.948** ← W4-1 | κ=38.19 → T=6.077 |
| **Surface B** — a₂-kinematic, τ=0.2195, \|dv/dτ\|=457.656 | κ=221.96 → T=35.33 | κ=457.656 → **T=72.838** ← W4-2 / **CORPUS** |

W4-1 occupies the (Visser, Surface A) cell. W4-2 occupies the (bare, Surface B) cell. They are **diagonally opposite** in the 2×2 — neither shares a surface NOR a convention with the other. The "25×" is the product of the surface-gradient ratio (38.19 vs 457.656 ≈ 12×) and the convention factor placement (the c_BLV=0.485 factor sitting on opposite cells), once routed through T=κ/2π.

---

## 4. STRUCTURAL VERDICT — option (ii): two legitimately-distinct surface gravities on two distinct surfaces, with a corpus-label pin

**The entry sonic surface does NOT carry one κ that the two gates computed inconsistently. The two gates computed surface gravities of TWO DIFFERENT surfaces under TWO DIFFERENT (both legitimate) analog-gravity κ-conventions. Neither value is "wrong physics."**

However, the adjudication question for the corpus is sharper than "are both legitimate" — it is **"which is THE entry temperature?"** And here the corpus is unambiguous:

> **THE canonical "entry temperature" = T_entry = κ_v/2π = 72.8 M_KK**, at the **a₂-kinematic surface τ=0.2195**, under the **bare velocity-gradient κ_v ≡ |dv/dτ|**. (W4-2 row-1 reproduces this; corpus `transit-flow-genesis-to-now.md`, "pure kinematic," a₂/E30 channel.)

The W4-1 value **T_a = 2.948 M_KK (Visser κ = 18.520 at τ₀=0.1125)** is a **DIFFERENT, currently-unnamed observable**: the literal Visser surface gravity of the BLV-scalar free-Mach-1 crossing. It is correct *as what it computes*, but it is **NOT** "the entry temperature" and must not be allowed to double-value that corpus label. It is the surface-gravity analog of a "different horizon" (different τ) read under a "different scheme" (Visser-c vs bare gradient) — exactly the kind of distinct-κ-for-distinct-structure the W4-2 ledger already embraces for the entry/exit/BLV-internal triple.

### Why this is option (ii) and not option (i)
Option (i) would require declaring one of {2.948, 72.838} the wrong κ for THE entry surface, with the other a coordinate/normal artifact. That is **false**: both are correct surface gravities of their respective surfaces. W4-1's negative ∂_τ→positive ∂_n orientation fix is a genuine and correct normal-convention handling (white-hole outflow κ>0), not the source of the divergence; the divergence survives orientation entirely (it is surface-τ + κ-scheme, both real). So the honest verdict is (ii): two distinct surfaces, two distinct κ-conventions, ONE of which (72.838) is the corpus-canonical entry temperature.

### The genuine defect this exposes (and the fix)
The real problem is **NOT** a physics error — it is a **labeling inconsistency in the W4-2 ledger**: its column header writes `κ = ½∂_n(c²−v²)` (the Visser form) while row-1 operatively computes `κ_v = |dv/dτ|` (the bare form). Those differ by c_BLV. Left unfixed, a reader who takes the column header literally and the W4-1 Visser κ side-by-side sees an internal contradiction in "the entry temperature." The fix (effected in-session, §6 below) pins the κ_v ≡ |dv/dτ| definition on the corpus row and flags the W4-2 header as a schematic surface-gravity placeholder whose operative row-1 definition is the bare gradient.

---

## 5. Substrate-first framing (per `phononic-framing.md`)

The acoustic white hole is a laboratory analog OF the substrate transit, not a container the substrate lives in; the explanatory arrow is held substrate → emergent throughout:

```
D_K eigenvalues
  → spectral-action moments  (a₂ = Einstein-Hilbert/kinematic ; a₄ = Yang-Mills+Higgs/condensation)
  → monotone Jensen modulus deformation v(τ) = dτ/dt , and BLV acoustic speed c_BLV (an a_n-moment functional)
  → DISTINCT Mach-1 / sonic surfaces in the internal acoustic geometry
        • a₂-kinematic surface τ=0.2195  (BCS-mode v_g = modulus velocity)  → κ_v = |dv/dτ| → T_entry = 72.8 M_KK   [CORPUS entry temperature]
        • BLV-scalar discriminant τ₀=0.1125 (free Mach-1 of c=c_BLV scalar)  → κ_Visser = c·|dv/dn| = 18.52 → T = 2.948 M_KK [distinct, unnamed observable]
  → analog white-hole causal structure
```

These are **not** thermal-equilibrium radiation from black holes — they are the substrate transit's acoustic signature read off the D_K spectrum, exactly as a Kerr-vs-Reissner-Nordström pair carries distinct κ for distinct horizon structure (Bardeen-Carter-Hawking; Hawking Paper 03). No information-paradox / unitarity tension arises: these are internal-acoustic-geometry analog temperatures, not gravitational Hawking radiation; the produced squeeze's escape is governed separately by the §W4-3 exit greybody filter. The container-thinking trap ("particles created IN the analog spacetime") is avoided: the κ's are intrinsic surface-gravities of the substrate's own emergent acoustic geometry at distinct τ-surfaces.

---

## 6. In-session NON-MATH actions EFFECTED (concrete file edits, before terminating)

Per the task and `feedback_fix-in-session-never-defer.md`, the disambiguation is effected now — not deferred:

1. **Corpus entry-temperature label pinned** — `sessions/framework/Collabs/equation-build/transit-flow-genesis-to-now.md §"The two horizons"`: added a **κ-definition note** clarifying that `T_entry = 72.8 M_KK` is keyed to the **bare velocity-gradient κ_v ≡ |dv/dτ| = 457.66** at the a₂-kinematic surface τ=0.2195, NOT the Visser form κ_Visser = ½|∂_n(c²−v²)| = c_BLV·|dv/dn| (the two differ by exactly c_BLV=0.485, Sage-exact); and that the W4-1 value T_a=2.948 (Visser κ=18.520 at the distinct crossing τ₀=0.1125) is a **different observable**, not a competing "entry temperature." The corpus "entry temperature" is now single-valued and not internally double-valued against W4-1.

2. **W4-2 WP ledger row-1 κ-convention disambiguated** — `sessions/archive/session-95/session-95-w4-workingpaper.md §W4-2 "Per-surface provenance / disambiguation"`: added a post-verdict (no-number-change) note recording that row-1's adopted κ_entry=457.656 is the bare gradient κ_v ≡ |dv/dτ| (corpus-canonical), that the ledger's `κ=½∂_n(c²−v²)` column header is a schematic surface-gravity placeholder whose operative row-1 definition is the bare gradient, with the Sage-exact reduction showing the literal Visser κ at that surface would be c_BLV·457.656=221.96 → 35.3 (not a corpus value). The verdict and the 72.8383 value are unchanged.

Both edits are labeling/disambiguation only; no verdict line is altered, no number changes, verdict permanence preserved.

---

## 7. Carry-forward computation (4-field)

The convention split surfaces ONE genuine future-compute item. It is OPTIONAL (the verdict above is complete without it); it would *upgrade* the W4-1 Visser surface to a named corpus temperature on equal footing with the entry/exit/BLV-internal triple.

### CF-S96-WHITE-HOLE-VISSER-SURFACE-PLACE — name (or retire) the BLV-discriminant Visser surface in the analog-T ledger

| Field | Spec |
|:------|:-----|
| **What** | Decide whether the W4-1 BLV-scalar discriminant crossing (τ₀=0.1125, Visser κ=18.520, T=2.948 M_KK) is a 4th *named* analog-temperature surface in the §6.2 ledger, or is a re-reading of an already-placed surface under the alternate κ-convention. Concretely: test whether 2.948 (= T_a^Visser at Surface A) and 6.077 (= T_a^bare at Surface A) sit at the same τ as any of the three placed surfaces (entry 0.2195 / exit ~0.16 / BLV-internal-acoustic), OR whether τ₀=0.1125 is genuinely a 4th surface; and pin ONE κ-convention (Visser-c vs bare-gradient) as canonical per surface so the ledger column header is operative, not schematic. |
| **Inputs** | `computations/session-95/s95_w4_1_white_hole_kinematic_consistency.npz` (τ₀, ∂_n(c²−v²), v(τ), c_BLV); `computations/session-95/s95_w4_2_hawking_analog_t_ledger.npz` (3-row ledger τ's + κ's); `c_BLV=0.485` (canonical S64); corpus `transit-flow-genesis-to-now.md` entry/exit τ's. |
| **Gate** | `S96-WHITE-HOLE-VISSER-SURFACE-PLACE` — PASS iff τ₀=0.1125 is shown distinct from all three placed τ's (|Δτ|>tol pre-registered) AND a single κ-convention is pinned per surface (column header becomes operative) ⇒ either a 4th ledger row is added (PLACED) or 2.948 is retired as a convention-duplicate of an existing surface (RETIRED-as-convention-image). Direction pre-reg: τ₀=0.1125 ≠ {0.2195, ~0.16, BLV-internal τ} ⇒ distinct surface expected. |
| **Effort** | ~0.5 wave-equivalent. **Depends on**: W4-1 (PASS, DONE) + W4-2 (PASS, DONE); no new spectral diagonalization (reads existing npz + Sage-exact κ-convention algebra). |

---

## 8. Constraint / Implication / Surviving space

- **Constraint** (Sage-exact, structural): under constant c, the Visser surface gravity κ=½∂_n(c²−v²) reduces at v=c to **c·|dv/dn|** — it carries an explicit factor c. The bare velocity-gradient κ_v ≡ |dv/dτ| is a *different* surface-gravity convention, smaller by exactly c_BLV=0.485.
- **Implication**: the W4-1 (18.520→2.948) and W4-2 (457.656→72.838) entry κ's are NOT inconsistent computations of one surface — they are correct surface gravities of **two distinct surfaces** (τ₀=0.1125 vs τ=0.2195) under **two distinct κ-conventions** (Visser-c vs bare-gradient), diagonally opposite in the 2×2 (surface × convention) matrix. The plan's "both should reuse one `surface_gravity` helper" was the source of the apparent paradox: a single helper would have to be passed BOTH the surface AND the convention, and the two gates legitimately needed different settings of each.
- **Surviving solution space**: the corpus "entry temperature" is **single-valued = 72.8 M_KK** (a₂-kinematic surface τ=0.2195, κ_v=|dv/dτ|) — pinned in-session. The W4-1 Visser surface (2.948 M_KK at τ₀=0.1125) survives as a *distinct, correct, currently-unnamed* observable; CF-S96 decides whether to name it a 4th ledger row or retire it as a convention-image. The 3-row W4-2 ledger (entry/exit/BLV-internal, all PASS, κ-ratio 9.61 to 0.018%) is **unaffected** — it is internally on the bare-gradient convention throughout, and its column-header labeling is now disambiguated.

---

## 9. One-line answer

**(ii) Two legitimately-distinct surface gravities on two distinct surfaces** — the BLV-discriminant entry-sonic crossing at τ₀=0.1125 carries the Visser κ=18.520 → T=2.948 M_KK, while the a₂-kinematic transit surface at τ=0.2195 carries the bare velocity-gradient κ_v=457.656 → T=72.838 M_KK — separated along BOTH the surface axis (|Δτ|=0.107) AND the κ-convention axis (Visser-c vs bare-gradient, differing by exactly c_BLV=0.485, Sage-exact). The corpus-canonical "**entry temperature**" is unambiguously **72.8 M_KK** (the a₂-kinematic / bare-gradient one); the 2.948 M_KK Visser value is a distinct, correct, currently-unnamed observable, NOT a competing entry temperature and NOT a coordinate/normal artifact. Corpus label and W4-2 ledger header disambiguated in-session.
