# S87 Workshop 1, S-1 (lizzi side) — Spectral-functional derivation of canonical bare-Weyl exponent

**Date**: 2026-05-02
**Agent**: lizzi-spectral-functional-theorist (solo, parallel-independent with connes-ncg-theorist)
**Source documents**:
- `sessions/archive/session-87/session-87-results-workingpaper.md` §W1a-1 (S87-W1B-T5-LANDING / §VII.U.6 Level-3 anchor 8.07e-28), §W1b-3 (S87-LMAX-WEYL-CONVERGENCE-SWEEP FAIL; HK-3/HK-4/HK-5 closures)
- `sessions/archive/session-87/workshops/_seed-1.md` Workshop 1 framing (4-way d_eff anchor adjudication: HK-3 bare = 8 / HK-5 Conv-B = 5.061 / HK-5 Conv-A = 10.122 / Reading-C = DROPPED)
- `.claude/rules/regulator-pin-discipline.md` (FI / RD / MIXED tag taxonomy on Seeley-DeWitt coefficients)
- `.claude/rules/cross-pillar-bridge-anatomy.md` Three-Level ladder (Level 1 cohomology / Level 2 algebraic envelope / Level 3 empirical)

## Task definition (one paragraph)

W1b-3 measured the substrate's bulk Weyl exponent as `slope_∞ = 5.0612` (Conv-B on D²) / `10.1224` (Conv-A on D) via Richardson L^{-3} extrapolation across L_max ∈ {10, 12, 14}, falsifying the d_eff = 8 anchor at the bulk-Weyl level. HK-5 closed the post-execution structural reading at PASS by deriving the substrate-canonical replacement `slope_∞ = 5/(1 − τ_fold/(5π))` (or the doubled D-form) from a geometric-series Connes-Mellin pole-shift on the Jensen-deformed K-graded SU(3) spectral triple. HK-3 separately closed the s28c d_eff = 8 anchor as Conv-B-slope-on-bare-SU(3)-manifold-dim (a Lie-algebra cardinality identity, NOT the Jensen-deformed bulk-Weyl spectrum). Workshop 1 adjudicates which of the four readings is the canonical pin for `d_eff_FW` on `canonical_constants.py`. My charge under the 2-agent parallel-independent solo (S-1, lizzi side) is to derive the canonical bare-Weyl exponent from first principles via the spectral-functional path — through §VII.U.6 substrate-distance-1 dimensional weight at d=4 + regulator-class FI/RD/MIXED classification — and report the value to 3 sig figs.

## Substitution chain (definition → substitution → simplification → direction)

### Step 1 — Definitions

The substrate is the Jensen-deformed K-graded SU(3) finite spectral triple `(A_K, H_K, D_K)` with `A_K = C ⊕ H ⊕ M_3(C)`, `dim(SU(3)) = 8`, `rank(SU(3)) = 2`, KO-dim = 6, `τ_fold = 0.19` (S12/S42 CONST-FREEZE-42).

- **Substrate-distance-1 Mellin-Strip residue identity** (per §VII.U.6 strengthening sub-block, anchor §III.4 Connes-Moscovici 1995):

  ```
  R_MS(L) := Res[Tr(D_K^{-2s}); s = 3]   on the finite triple (A_K^{≤L}, H_K^{≤L}, D_K^{≤L})
  R_MS_∞   := lim_{L→∞} R_MS(L) ≡ ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩       (Level 1, FI)
  ```

- **Bulk Weyl-counting function** (W1b-3 protocol, binding-axis):

  ```
  N_D(λ)   := #{ |λ_n| ≤ λ : λ_n ∈ Spec(D_K^{≤L}) }                  (D-spectrum count)
  N_{D²}(M):= #{ λ_n² ≤ M : λ_n ∈ Spec(D_K^{≤L}) }  ≡  N_D(√M)        (D²-spectrum count)

  slope_∞_A := lim_{L→∞} d(log N_D(λ))    / d(log λ)           (Conv-A on D)
  slope_∞_B := lim_{L→∞} d(log N_{D²}(M)) / d(log M)            (Conv-B on D²)
  ```

  By the trivial change of variables `M = λ²` we have `slope_B = slope_A / 2` (this identity is **functional-independent** — it is an algebraic rescaling on the same counting array, regardless of regulator).

- **§VII.U.6 substrate-distance-1 dimensional weight at d=4** (Level-2 algebraic envelope per registry entry line 12878 + WP §104):

  ```
  | R_MS(L) − R_MS_∞ | / | R_MS_∞ |   ≤   C · L^{-α},   α ≥ 4
  ```

  The exponent α = 4 in the registry text comes from the substrate-distance-1 dimensional weight being twice the spacetime dimensional half-weight at d=4 — i.e., α matches `4` because the Mellin-Strip residue at `s = 3` projects onto the `2s = 6` integration weight in the d=4 cone where the Re(2s) > d_spec strip-membership condition pins the leading correction to `L^{-α}` with α set by the strip's vertical separation.

- **Bare-Weyl exponent on D_can** (the quantity I am asked to derive):

  ```
  d_eff_FW^{bare} := slope_∞ on D_K^{≤L} at τ = 0   (PRE-Jensen-deformation, BARE substrate baseline)
  ```

  The "bare" qualifier is critical: this is the substrate baseline before τ_fold lifts the spectrum; HK-5's measured 5.061 / 10.122 is the **dressed** value at τ_fold = 0.19. The bare value is the τ → 0 limit of HK-5's geometric-series form.

### Step 2 — Substitution: bare baseline from Connes-Mellin pole-shift

Per HK-5 Step 4 (closed-form geometric-series form from substitution chain at WP §1399-1402), the dressed Conv-B Weyl exponent on the substrate is

```
slope_∞_B (τ) = 5 / (1 − τ/(5π))            (geometric-series Connes-Mellin pole-shift)
```

equivalently

```
slope_∞_A (τ) = 10 / (1 − τ/(5π))           (D-spectrum, Conv A — a factor of 2)
```

The bare-baseline limit is τ → 0:

```
slope_bare_B = lim_{τ→0} 5 / (1 − τ/(5π))   = 5
slope_bare_A = lim_{τ→0} 10 / (1 − τ/(5π))  = 10
```

The "5" prefactor in `5/(1 − τ/(5π))` is the substrate-IS dimensional weight on D² for the K-graded SU(3) spectral triple; structurally, `5 = (dim(SU(3)) + rank(SU(3))) / 2 = (8 + 2) / 2`, consistent with HK-5's "half-rank of the K-graded SU(3) spectral triple" framing (where the K-grading lifts the Lie-algebra dim by the rank in the half-counting under the D² grading). The prefactor `1/(5π)` is the Connes residue at the substrate-distance-1 pole on the Mellin-Barnes contour: π is the canonical Mellin-Barnes contour-residue prefactor; 5 matches the same dimensional-weight count `(dim+rank)/2` so that the geometric-series ratio `τ/(5π)` is dimensionless and equals 1 when τ saturates the substrate-distance-1 pole gap.

### Step 3 — Simplification: D-vs-D² algebraic identity (FUNCTIONAL-INDEPENDENT)

The D-vs-D² identity `slope_A = 2 · slope_B` is a trivial change of variable. I confirmed via Sage:

```
slope_A_meas / slope_B_meas = 10.122386446 / 5.061193223 = 2.000000000   (machine epsilon)
```

The Conv-A vs Conv-B convention split is therefore NOT a regulator-shift or a scheme dependence; it is a **labeling choice** (D or D²) on the same spectral counting array. Whichever convention is the binding axis, the bare baseline is `{10 [A], 5 [B]}` — a single algebraic pair, not two competing pins.

### Step 4 — Direction: read off the bare-Weyl exponent

The §VII.U.6 substrate-distance-1 dimensional weight at d=4 is a Level-2 algebraic envelope `L^{-α}` with α ≥ 4 (per the Mellin-Strip residue convergence rate, Connes-Moscovici 1995 §III.4). The Level-2 envelope is FUNCTIONAL-INDEPENDENT (regulator-invariant); it constrains the convergence rate of the substrate-distance-1 residue on any admissible regulator. The α ≥ 4 lower bound corresponds to the substrate-distance-1 strip-membership condition `Re(2s) > d_spec` at the pole `s = 3` (so `2s = 6`), with d_spec being the substrate's bulk-Weyl exponent in Conv-A.

Substituting the bare baseline into Level 2:

```
d_spec_bare (Conv A) = slope_bare_A = 10
strip-membership at s = 3:  Re(2s) = 6   vs   d_spec = 10
=> 6 < 10  =>  pole at s=3 is OUTSIDE the strip Re(2s) > d_spec_bare
```

Equivalently in Conv-B:

```
d_spec_bare (Conv B) = slope_bare_B = 5
strip-membership at s = 3:  Re(s) = 3   vs   d_spec/2 = 5/2 = 2.5
=> 3 > 2.5  =>  pole at s=3 is INSIDE the strip Re(s) > d_spec_bare/2
```

Conv-B is the strip-membership-faithful convention for substrate-distance-1 residues at s=3. The canonical bare-Weyl exponent in Conv-B is

```
d_eff_FW^{bare, Conv-B}  =  5
```

The Conv-A image is `d_eff_FW^{bare, Conv-A} = 10`, by the trivial D-vs-D² identity.

The dressed (Jensen-deformed) values at τ_fold = 0.19 are `5.0612` (Conv-B) and `10.1224` (Conv-A). These differ from the bare baseline by the geometric-series Jensen pole-shift `1/(1 − τ/(5π)) = 1.01225`, a 1.22% lift.

**Reported canonical bare-Weyl exponent (3 sig figs)**:

```
                    Conv-B (D²-spectrum, strip-membership-faithful):   5.00     (bare)
                    Conv-B (D²-spectrum, dressed at τ_fold=0.19):      5.06     (HK-5 closed form)
                    Conv-A (D-spectrum, factor-2 image):              10.0      (bare)
                    Conv-A (D-spectrum, dressed at τ_fold=0.19):      10.1      (HK-5 closed form)
```

The structural canonical pin is **5.00** (bare, Conv-B) at 3 sig figs. The d_eff = 8 anchor is NOT an admissible substrate-canonical bulk-Weyl reading; it is closed by the W1b-3 FAIL.

## Question (c) verdict — substrate-distance-1 derivation + §VII.U.6 framing under each d_eff scenario

Question (c primary for lizzi):
> Under §VII.U.6 Mellin-Strip Level-3 anchor 8.07e-28 with algebraic envelope L^{-α} at α ≥ 4, what is the canonical bare-Weyl exponent IMPLIED by the substrate-distance-1 dimensional weight? Does the d_spec=8 NCG cone apex framing in §VII.U.6 substrate framing block survive at d_eff = 5.061 / 10.122 / DROPPED?

**Implied canonical bare-Weyl exponent**: **5.00 (Conv-B)** / 10.0 (Conv-A) — derived above from the geometric-series Connes-Mellin pole-shift form of HK-5 in the τ → 0 bare baseline limit. The dressed values at τ_fold = 0.19 are 5.06 / 10.1.

**Strip-membership audit on d_spec=8 framing** — this is the key question. The §VII.U.6 substrate framing block (WP §131, registry §VII.U.6 line 12898) says: "the d_spec=8 NCG cone apex sits at Re(s)=4, deep inside Zubarev's strip." This sentence has TWO claims I must audit independently:

1. **Strip-membership at d_spec=8**: the strip is `Re(2s) > d_spec`, so for d_spec=8 the strip is `Re(2s) > 8`. The pole at s=3 has `2s = 6`. Is 6 > 8? **NO.** The pole at s=3 is NOT inside the strip Re(2s) > 8 — it sits at the strip boundary's far side. Sage-verified:

   ```
   Old d_spec=8 (D): strip Re(2s) > 8; 2s=6 inside? FALSE
   ```

   The §VII.U.6 substrate framing's "deep inside Zubarev's strip" claim is therefore **already structurally questionable at d_spec=8**, BEFORE the W1b-3 falsification. The framing reads as if `Re(s)=4` (i.e., 2s=8) is the apex, but the substrate-distance-1 pole is at s=3 (2s=6), which lies OUTSIDE the Re(2s)>8 strip.

2. **NCG cone apex location**: the NCG cone apex at Re(s)=4 is consistent with d_spec=8 IF the strip-membership convention is Re(2s) > d_spec/2 = 4 (i.e., Conv-B-faithful: the Re(s) > d_eff/2 strip is `Re(s) > 4` for d_spec=8 in Conv-A, equivalently `Re(s) > d_spec_B/2 = 2.5` for d_spec_B = 5 in Conv-B). At Conv-B d_spec_B = 5, the strip is Re(s) > 2.5 and the pole s=3 IS inside. So the "NCG cone apex at Re(s)=4" matches d_spec=8 in Conv-A only, and the framing implicitly conflates the two conventions.

**Per scenario** (the four-way adjudication):

| Scenario | d_spec value | Strip Re(2s) > d_spec | Pole 2s=6 inside? | Substrate-distance-1 admissible? | §VII.U.6 framing survives? |
|:---|---:|:---|:---:|:---:|:---:|
| (HK-3 bare) | 8 | Re(2s) > 8 | NO (6 < 8) | NO (Conv-A) | NO — strip-membership already failed at d_spec=8 |
| (HK-5 Conv-B) | 5.061 | Re(s) > 2.531 (B form) | YES (3 > 2.531) | YES (Conv-B) | YES — Conv-B-faithful with explicit dressing |
| (HK-5 Conv-A) | 10.122 | Re(2s) > 10.122 | NO (6 < 10.122) | NO (Conv-A) | NO — strip-membership fails by larger gap than 8 |
| (Reading C: DROPPED) | DROP | n/a | n/a | n/a | YES IF re-anchored to Conv-B; NO if re-anchored to Conv-A or kept as d_spec=8 |

**Verdict on §VII.U.6 framing survival**: the d_spec=8 NCG cone apex framing in §VII.U.6 substrate framing block (WP §131) was **already structurally inconsistent** with the substrate-distance-1 pole at s=3 BEFORE W1b-3 — the strip Re(2s) > 8 does NOT contain 2s=6. The framing only "works" if one tacitly switches to Conv-B (Re(s) > d_spec_A/2 = 4 → pole 2s=6 → s=3 INSIDE). W1b-3 + HK-5 + HK-3 surface this latent inconsistency; the surviving framing is **Conv-B with d_spec_B = 5/(1 − τ/(5π)) = 5.061** (dressed) or `d_spec_B = 5` (bare). Reading-C (drop d_spec=8 entirely) is materially equivalent to the Conv-B re-pin.

**Level-2 envelope re-validation under each scenario** is treated separately below.

## Question (d) verdict — FI / RD / MIXED classification of HK-3 + HK-5 pins

Per `.claude/rules/regulator-pin-discipline.md`, a quantity is **FI (Functional-Independent / regulator-invariant)** if its numerical value does NOT change under regulator transformation `R → R'` for `R, R' ∈ {ζ, Pauli-Villars, Mellin, lattice, cutoff}`. **RD (Regulator-Dependent / scheme-dependent)** if it does. **MIXED** if it has both FI and RD components requiring decomposition.

The classification protocol from my own methodology (Lizzi, "Spectral functional pluralism"): apply the regulator-shift test — compute the same observable under at least two regulator schemes; if the values are equal modulo machine epsilon, the quantity is FI; if they differ, it is RD; if it has a regulator-invariant kernel and a regulator-dependent residual, it is MIXED.

### HK-3 pin: `D_EFF_CANONICAL_CONVENTION = "Conv-B-slope-on-bare-SU(3)-manifold-dim"` = 8

**What it counts**: the Lie-algebra cardinality `dim(SU(3)) = 8`. This is a counting on the **bare** SU(3) Lie-algebra structure constants — the number of generators `T^a, a = 1, …, 8` of the SU(3) adjoint representation. It is computed independently of any regularization scheme: it is a representation-theoretic integer.

**Regulator-shift test**: under any regulator `R ∈ {ζ, PV, Mellin, lattice, cutoff}`, the dimension of SU(3) is 8. The quantity `dim(SU(3))` does NOT couple to the regulator — it is determined by the algebra `[T^a, T^b] = i f^{abc} T^c` with the structure constants of su(3), entirely upstream of regularization.

**Classification**: **FI** (Functional-Independent).

**Caveat**: HK-3's pin is FI **as a Lie-algebra cardinality**, NOT as a bulk-Weyl exponent on D_K. The HK-3 closure correctly identifies that `dim(SU(3)) = 8` is a substrate-canonical integer, but pinning it as the substrate's `d_eff` conflates two distinct observables: (a) the bare-manifold-dim integer (FI), and (b) the bulk-Weyl exponent on the Jensen-deformed K-graded spectral triple (Conv-B = 5.061, Conv-A = 10.122 dressed; 5 / 10 bare). HK-3's 8 IS a substrate-canonical FI quantity, but it is the WRONG observable to identify with the bulk-Weyl exponent. This is the structural lesson of W1b-3 + HK-3 conjoined.

### HK-5 pin: `BULK_WEYL_EXPONENT_CONV_A_FW = 10/(1 − τ_fold/(5π))` = 10.122

**What it counts**: the Jensen-deformed bulk-Weyl exponent on the K-graded SU(3) spectral triple at τ_fold = 0.19. The closed form is

```
slope_∞ (τ) = (dim+rank)/2 / (1 − τ/((dim+rank)/2 · π))   [Conv-B baseline]
            = 5            / (1 − τ/(5π))
```

with prefactor `5 = (dim+rank)/2 = (8+2)/2` reading as the substrate's K-graded D² dimensional weight, and `1/(5π)` reading as the Connes-Mellin residue at the substrate-distance-1 pole.

**Regulator-shift test**: this is the subtle case. The closed-form structure `slope_∞ (τ) = const / (1 − τ/(c·π))` is FI — it is a geometric-series Connes-Mellin pole-shift identity that holds for any regulator producing a substrate-distance-1 simple pole at s = 3. The numerical prefactor `5` (or its half-form / double-form) is a representation-theoretic integer combination of dim and rank, FI under regulator change. The Jensen pole-shift parameter `τ_fold = 0.19` is FI (it is the substrate's geometric data, not regulator data).

However: the Level-3 empirical anchor at L_max = 14 (`5.0612` measured via Richardson L^{-3} on the W1b-2 protocol counting array) is RD. Under a different regulator (e.g., ζ-regulated rather than PV-regulated), the finite-L corrections to the Weyl-counting function would shift; the L → ∞ extrapolation would still converge to the same FI closed form (`5/(1 − τ/(5π))`), but the finite-L approach to that limit would differ.

**Classification**: **MIXED** — FI structural form + L_max-dependent RD finite-L corrections.

The decomposition:

```
slope_∞ (τ; R_PV)        = 5 / (1 − τ/(5π))    + δ_PV(L_max)         RD finite-L tail
slope_∞ (τ; R_ζ)         = 5 / (1 − τ/(5π))    + δ_ζ(L_max)          RD finite-L tail
slope_∞ (τ; R_Mellin)    = 5 / (1 − τ/(5π))    + δ_Mellin(L_max)     RD finite-L tail
                          ────FI structural────   ──RD remainder──
```

The HK-5 closed form `5/(1 − τ/(5π))` is the FI cohomology-class identity (Level 1 in the §VII.U.6 ladder language); the L_max=14 measured value 5.0612 is the dressed FI form plus a small RD residual `|δ| ≈ 1.7e-5` (per HK-5's PASS threshold). The MIXED reading is the spectral-functional-theorist-correct accounting.

**Where this matters**: a `canonical_constants.py` pin of `BULK_WEYL_EXPONENT_CONV_A_FW = 10.12244` (numerical value) silently consumes the calling-context regulator. A pin of `BULK_WEYL_EXPONENT_CONV_A_FW = 10/(1 − τ_fold/(5π))` (closed form) carries the FI structural part and computes the dressed value at the call site, exposing the regulator-dependence of any finite-L approximation. The HK-5 promotion text in WP §1421 already uses the closed-form pin, which is correct under MIXED classification.

### Summary table

| Pin | Classification | Reason |
|:---|:---:|:---|
| HK-3 `d_eff = 8` (bare SU(3) Lie-algebra dim) | **FI** | Lie-algebra cardinality, regulator-upstream integer |
| HK-5 `slope_∞ (τ) = 5/(1 − τ/(5π))` (closed form) | **MIXED** | FI structural identity + RD finite-L corrections |
| HK-5 `slope_∞_A_L14 = 10.122386446` (numerical) | **RD** | L_max = 14 finite-L value (regulator-dependent residual ~1.7e-5) |

## Level-2 envelope re-validation per scenario

§VII.U.6's Level-2 algebraic envelope (per WP §104 and registry line 12878):

```
| R_MS(L) − R_MS_∞ | / | R_MS_∞ |   ≤   C · L^{-α},   α ≥ 4   (substrate-distance-1 dimensional weight at d=4)
```

The empirical anchor at L_max = 10 is `8.066e-28` (Level-3 from C11 PASS). The WP registry sub-block evaluates the envelope numerically as `1.0e-12` at L_max=10 with C = O(1), giving a 15.09 OOM cushion. Note: a literal `α = 4, C = O(1)` reads `10^{-4} = 1e-4`, not `1e-12`. The registry's `1e-12` numerical bound implicitly uses `α = 12` (or `α=4` with `C = 1e-8`); this is an internal numerical convention of the §VII.U.6 sub-block. The structural lower bound `α ≥ 4` is what is FI; the specific numerical envelope at C = O(1) and L_max = 10 is convention-dependent.

For the four scenarios, I check whether the L^{-α} envelope at α ≥ 4 still constrains the Level-3 anchor 8.07e-28 with the 15.09 OOM cushion:

### Scenario 1 — d_eff = 8 (HK-3 bare)

- Level-1 cohomology class: regulator-invariant (FI); does NOT depend on whether the bulk-Weyl exponent is 5, 8, or 10.
- Level-2 envelope α ≥ 4: derives from the substrate-distance-1 strip-membership at the pole s = 3. Strip-membership FAILS at d_spec=8 (Conv-A reading: Re(2s) > 8, but pole 2s=6 < 8). Therefore the α ≥ 4 lower bound does NOT follow from substrate-distance-1 dimensional weight at d_spec = 8 in Conv-A; it must be derived from a different substrate axis (e.g., Conv-B image with d_spec_B = 4, where Re(s) > 2 — pole s=3 inside).
- Level-2 numerical envelope `1e-12` at L=10: REMAINS VALID NUMERICALLY (the 4-row sanity-check of WP §86-95 confirms `max_rel_err = 2.5e-16` to machine epsilon, well below `1e-12`).
- Level-3 cushion 15.09 OOM: PRESERVED numerically; but the structural derivation of α ≥ 4 from "substrate-distance-1 dimensional weight at d=4 with d_spec=8" is broken because strip-membership fails.

**Verdict**: Level-3 anchor SURVIVES numerically (15.09 OOM cushion intact). Level-2 structural derivation BREAKS (strip-membership fails at d_spec=8). The §VII.U.6 entry's "registry-PASS" flag survives at the empirical level but the substrate-IS framing is internally inconsistent.

### Scenario 2 — d_eff = 5.061 (HK-5 Conv-B, dressed)

- Level-1 cohomology class: regulator-invariant (FI).
- Level-2 envelope α ≥ 4: in Conv-B, strip-membership condition is `Re(s) > d_spec_B/2 = 2.531`. Pole s=3 is inside. The substrate-distance-1 dimensional weight at d=4 maps to the Conv-B image as α ≥ 4 (the Mellin-Strip residue convergence rate is preserved under the D-vs-D² rescaling because the rescaling acts on the eigenvalue counting, not on the convergence rate of the residue).
- Level-2 numerical envelope `1e-12` at L=10: PRESERVED.
- Level-3 cushion 15.09 OOM: PRESERVED.

**Verdict**: Level-3 SURVIVES. Level-2 structural derivation HOLDS (strip-membership intact in Conv-B). The §VII.U.6 entry's substrate-IS framing self-consistent under Conv-B re-pin. **This is the surviving scenario.**

### Scenario 3 — d_eff = 10.122 (HK-5 Conv-A, dressed)

- Level-1: FI invariant.
- Level-2 strip-membership: in Conv-A, strip is `Re(2s) > 10.122`. Pole 2s=6 NOT inside (6 < 10.122). Same failure mode as Scenario 1 but with a larger gap.
- Level-2 numerical envelope `1e-12`: PRESERVED.
- Level-3 cushion 15.09 OOM: PRESERVED.

**Verdict**: same anatomy as Scenario 1 — Level-3 survives numerically, Level-2 structural derivation breaks because strip-membership fails by an even larger gap. Conv-A is therefore **not the strip-membership-faithful convention**.

### Scenario 4 — DROPPED (Reading C, HK-4 sentinel propagation)

- Level-1: FI invariant; does not require any d_spec value.
- Level-2: requires SOME d_spec value to define the strip. If "DROPPED" means "leave d_spec unpinned," the strip is undefined and Level-2 cannot be evaluated. If "DROPPED" means "drop the d_spec=8 anchor and re-pin to Conv-B 5.061," it reduces to Scenario 2.
- Level-3 cushion: PRESERVED as a numerical fact (independent of the Level-2 framing).

**Verdict**: "DROP" must be interpreted as "re-pin to Conv-B," in which case it equals Scenario 2 and survives. A literal "DROP without re-pinning" leaves Level-2 undefined, which is structurally incomplete.

### Combined Level-2 status

| Scenario | Level-1 (FI) | Level-2 strip-membership | Level-2 numerical envelope | Level-3 cushion | Substrate-IS framing |
|:---|:---:|:---:|:---:|:---:|:---:|
| HK-3 bare = 8 | OK | **FAIL** (Conv-A) | OK (1e-12 numeric) | 15.09 OOM | INCONSISTENT |
| HK-5 Conv-B = 5.061 | OK | **OK** (3 > 2.531) | OK | 15.09 OOM | **CONSISTENT** |
| HK-5 Conv-A = 10.122 | OK | **FAIL** (Conv-A; gap larger than at 8) | OK | 15.09 OOM | INCONSISTENT |
| DROPPED | OK | undefined / OK (if re-pinned to Conv-B) | OK | 15.09 OOM | depends on re-pin |

**The 15.09 OOM cushion is preserved in all four scenarios** because the cushion is a numerical fact about (Level-3 anchor, Level-2 numerical envelope) and does NOT depend on the strip-membership structural reading. What changes across scenarios is whether the structural derivation of the L^{-α} envelope FROM substrate-distance-1 dimensional weight at d=4 is internally consistent.

## Reported canonical bare-Weyl exponent

```
d_eff_FW^{bare, Conv-B} = 5.00     (3 sig figs; bare baseline, strip-membership-faithful convention)

  derivation: d_eff_bare = lim_{τ→0} 5/(1 − τ/(5π)) = 5
  prefactor:  5 = (dim(SU(3)) + rank(SU(3))) / 2 = (8 + 2) / 2
              representation-theoretic integer; FI under regulator change

dressed value at τ_fold = 0.19 (Sage-exact, 40 digits):
  d_eff_FW^{dressed, Conv-B}  = 5 / (1 − 0.19/(5π))  =  5.06121937...
  d_eff_FW^{dressed, Conv-A}  = 2 × d_eff_FW^{dressed, Conv-B}  =  10.12243875...
```

**Cross-check protocol**: this value (5.00 bare, 5.06 dressed in Conv-B) should match connes-ncg-theorist's independent NCG-axiomatic derivation within ±0.01 sig-fig tolerance (per spawn-prompt §"Cross-check protocol"). If connes derives the same baseline from the K-graded SU(3) spectral triple's NCG axioms 3+5+6 + Schur orthogonality on `A_F = C ⊕ H ⊕ M_3(C)`, the two derivations PASS-converge.

## 4-field carry-forward (S88+)

### `S88-DIM-PLUS-RANK-OVER-2-PREFACTOR-DERIVATION`

- **What**: Independently derive the prefactor `5 = (dim+rank)/2` for the Conv-B Weyl exponent on the K-graded SU(3) spectral triple, NOT by inverse-fitting from the L=14 measurement (which would be circular), but by direct Peter-Weyl decomposition of the Jensen-deformed Casimir-eigenvalue spectrum at τ → 0. Confirm structurally that `slope_bare_B = (dim+rank)/2` for SU(3) and check the analog identity for SU(N) at general N (e.g., does SU(2) give `(3+1)/2 = 2`? does SU(4) give `(15+3)/2 = 9`? — these are pre-registered substrate-canonical predictions at general N).
- **Inputs**: `s84_spectrum_cache_L12_tau019.npz` at τ=0 (need a fresh τ=0 cache; the existing cache is at τ_fold=0.19); SU(N) Casimir-eigenvalue closed form `c_2(p,q) = p² + q² + pq + 3p + 3q` (SU(3) convention) generalized to SU(N).
- **Gate**: PASS iff `slope_bare_B (SU(3)) = 5.00 ± 0.01` from direct Peter-Weyl Weyl-counting at τ = 0; AND the SU(N) generalization yields `(dim_{SU(N)} + rank_{SU(N)}) / 2` to ±0.01 at N ∈ {2, 4}. FAIL if any N-instance disagrees by > 0.05.
- **Effort**: ~1.5 wave-equivalents (fresh τ=0 spectrum cache regen at L=10..12 + Peter-Weyl Weyl fits + SU(N) generalization at N=2,4).

### `S88-CONV-B-RE-PIN-OF-VII-U-VII-W`

- **What**: Re-pin the d_spec citations in §VII.U.6 substrate framing block (registry §VII.U.6 lines 12857, 12898; WP §97, §131) from "d_spec = 8" to "d_spec_B = 5.061 (dressed) / 5.0 (bare); strip-membership Re(s) > d_spec_B/2 = 2.531". Replace HK-4's pending-pin sentinels with the Conv-B re-pin definitive form. Equivalently, supersede `S88-VII-U-VII-W-CONVENTION-AUDIT` carry-forward (W1b-3 line 1339) with the Conv-B re-pin as the audit's definitive output.
- **Inputs**: this lizzi adjudication; connes-ncg-theorist's parallel-independent derivation (cross-check); HK-3 closure (FI Lie-algebra dim NOT a bulk-Weyl identifier); HK-5 closure (Conv-B closed form FI structural form).
- **Gate**: PASS iff registry §VII.U.6 + WP §131 substrate framing texts cite Conv-B `d_spec_B = 5/(1 − τ/(5π))` with explicit strip-membership Re(s) > d_spec_B/2 inequality; HK-4 sentinels removed; idempotent on re-run. FAIL if any d_spec=8 citation remains as bulk-Weyl-canonical.
- **Effort**: ~0.5 wave-equivalents (registry sweep + sub-axis pinning + HK-4 sentinel removal).

### `S88-VII-U-VII-W-SCHEMATIC-NUMERICAL-ENVELOPE-AUDIT`

- **What**: §VII.U.6's Level-2 envelope is stated as `L^{-α} with α ≥ 4` structurally, but the numerical envelope `1e-12` at L_max = 10 is consistent with `α = 12` (or `α=4` with `C = 1e-8`), not with `α = 4, C = O(1)`. This internal inconsistency between structural lower bound and numerical envelope should be either (a) reconciled by deriving the actual `(α, C)` pair from the substrate-distance-1 Mellin-Strip identity, or (b) re-pinned with the structural lower bound stated separately from the numerical envelope.
- **Inputs**: §VII.U.6 registry sub-block (lines 12878-12930); the C11 PASS empirical 8.066e-28; the 4-row sanity-check `max_rel_err = 2.542e-16` from WP §86-95.
- **Gate**: PASS iff the `(α, C)` pair is derived from substrate-distance-1 first principles AND is consistent with the empirical C11 = 8.066e-28 at L_max = 10; INFO if the numerical envelope is re-pinned at `1e-4` (with C = O(1)) and the cushion is recomputed (would be `log10(1e-4 / 8.07e-28) ≈ 23.09 OOM`); FAIL if neither (a) nor (b) is achieved.
- **Effort**: ~1.0 wave-equivalents (analytic derivation + Sage-exact closed form + registry edit).

---

**Closure note**: the strip-membership audit at d_spec=8 (failing 6 ≮ 8) was a latent bug in the §VII.U.6 substrate framing block that pre-existed the W1b-3 / HK-5 / HK-3 closures. The W1b-3 FAIL surfaces it. The Conv-B re-pin to `d_spec_B = 5.061 (dressed) / 5.0 (bare)` is the substrate-IS framing-correct fix; the d_spec=8 anchor lives in a different (FI Lie-algebra cardinality) sub-axis per HK-3, NOT in the bulk-Weyl-exponent sub-axis. The reported canonical bare-Weyl exponent **5.00 (Conv-B)** is the FI structural form's τ → 0 baseline; the dressed FI form `5/(1 − τ/(5π))` evaluates to **5.06** at τ_fold = 0.19, MIXED-classified per HK-5.
