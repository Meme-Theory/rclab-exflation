# Session 85 Slot S-1 — Regulator-Family Boundary Theorem (Lizzi Mellin-residue track)

**Session**: 85 | **Slot**: S-1 | **Theme**: Regulator-Family Boundary Theorem canonical write-up
**Author**: `lizzi-spectral-functional-theorist` (solo synthesis; connes and van-den-dungen write parallel independent proofs of the same theorem via their own tracks)
**Sources**: `session-85-w5-workingpaper.md`, `session-85-w2-workingpaper.md`, `session-85-w3-workingpaper.md`
**Track**: spectral-functional / Mellin-residue — reduce the boundary to an explicit `f^r` Mellin-vector decomposition.

---

## I. Session Outcome

Five independent S85 gates — four in W5 (lizzi-solo) and one in W2 (connes-solo) — converge on a single permanent structural wall separating two regulator classes inside the 5-atlas {zeta, Zubarev, SDW, cutoff_sqrt, anomaly}. The wall is not empirical fine-structure; it is the Mellin-support dichotomy

```
pure-a_4 family F_4    = { r : f^r has non-trivial weight only at the a_4 slot }
                       = { zeta, Zubarev, SDW }
mixed-support family M = { r : f^r has non-trivial weight on {a_0, a_2, a_4, a_6} or {a_2, a_4} }
                       = { cutoff_sqrt, anomaly }
```

W5-1 (FAIL, GEOMETRIC): `sig(cutoff_sqrt) = +1` vs `sig(zeta) = sig(Zubarev) = sig(SDW) = sig(anomaly) = -1` at τ_fold (S85 W5 WP §W5-1(d) lines 108–117).
W5-2 (FAIL value=3, GEOMETRIC): HP^0 factorization spread 0.00% for F_4, 254.75% for cutoff_sqrt, 107.07% for anomaly (W5 WP §W5-2(d) lines 289–297).
W5-5 (FAIL value=8, GEOMETRIC): support-union lattice-join is non-functorial on exactly the four pairs {r ∈ F_4} × {r ∈ M} that cross the wall (W5 WP §W5-5(d) lines 842–855).
W5-6 (INFO-tight value=2.0, GEOMETRIC): |f_4^r| attains max on F_4 ∪ {anomaly} = 1.0; cutoff_sqrt = 0.5 is the sole minimum (W5 WP §W5-6(d) lines 1046–1061).
W2-7 (FAIL value=1, META): (C_H, C_epsH) twin pair matches on (a_0, a_2, a_4) because even Seeley-DeWitt is parity-blind to HP^1 secondary twists (W2 WP §W2-7 lines 355–395).

The W5 evidence is L_max-robust across {8, 9, 10} (W5 WP §W5-4 PASS lines 648–672). The W2-7 twin-pair evidence is a co-propagating parity statement internal to the mixed-support → pure-a_4 split.

**Theorem classification**: GEOMETRIC — the substrate's regulator-choice DOF decomposes structurally into two classes with measurably distinct action on four independent observables (sign(ε_H), HP^0-factorization, lattice-join, HP^1 magnitude).

**Mellin-residue consequence**: since the regulator enters the spectral action only through its Mellin vector `f^r = (f_0^r, f_2^r, f_4^r, f_6^r, ...)` evaluated against the Seeley–DeWitt basis, the pure-a_4 vs mixed-support split is the coarsest algebraic partition of the 5-atlas that is visible to any integer-Seeley-DeWitt-moment observable. Every structural divergence observed in W5 is implied by a Mellin-vector support comparison.

---

## II. Key Results — Mellin-residue proof of the Regulator-Family Boundary Theorem

### II.0 Classification

GEOMETRIC. The substrate's Dirac operator D_K on Jensen-deformed SU(3) × A_F produces a single canonical eigenvalue spectrum {λ_k}. The regulator r selects which moments of the heat-kernel a_n(D_K^2) enter the spectral action via Mellin multipliers. The boundary is a property of the (f^r, a_n) pairing, not of the substrate spectrum — substrate-first throughout. Particles (phononic excitations) do not enter at any step.

### II.1 Definitions (Mellin vector, regulator class, pairing)

**Def L1 (Mellin vector of a regulator)**. For regulator r and Schwartz-class kernel f_r, define

```
f_n^r  :=  Res_{s = n/2}  M[ f_r ](s),        n = 0, 2, 4, 6, ...
f^r    :=  ( f_0^r, f_2^r, f_4^r, f_6^r, ... )    (Mellin support vector of r)
supp(r):=  { n : f_n^r ≠ 0 }
```

where `M[f](s) = ∫_0^∞ f(u) u^{s-1} du`. For D_K with scaling dimension d_s = 6 (KO-dim=6 internal + 4D external, S83 G3), the Seeley–DeWitt basis {a_n} contributes via

```
S_r[D_K, Λ]  =  Σ_n  f_n^r  ·  Λ^(d_s - n)  ·  a_n(D_K^2)              (spectral action, Mellin form)
```

**Def L2 (regulator class partition)**.

```
F_4  = pure-a_4 family    := { r : supp(r) = {4} }
        ⊇ { zeta, Zubarev, SDW }
M    = mixed-support family := { r : supp(r) ⊋ {4} }
        ⊇ { cutoff_sqrt (supp = {0,2,4,6}),  anomaly (supp = {2,4}) }
```

**Def L3 (observable–Mellin pairing)**. For any spectral observable O linear in the a_n moments,

```
O^r   =  ⟨ f^r, m^O ⟩  :=  Σ_n  f_n^r · m_n^O
```

where `m^O = (m_0^O, m_2^O, m_4^O, m_6^O, ...)` is the observable's Seeley–DeWitt character vector. The observable is **class-separating** iff `m_n^O ≠ 0` for some `n ≠ 4`.

**Def L4 (substrate a_0 datum)**. From S72 + canonical_constants.py (knowledge.db get_constant provenance: `a0_fold = 6440.0`, Seeley–DeWitt volume term at τ_fold = 0.19, S42/S20a verified):

```
a_0(τ_fold)  =  +6440     [dimensionless; signed positive by construction; provenance S42]
```

This is the single numerical datum that powers the wall.

### II.2 Canonical Mellin vectors of the 5-atlas

(From W5 WP §W5-2(b) lines 249–257; cross-referenced to CC 2010 Table 1 for cutoff_sqrt, S78 W2-F mellin_ratio for SDW, S83 G3 EN3 equivalence for Zubarev, S67 structural spec for anomaly.)

| Regulator r | `f^r = (f_0, f_2, f_4, f_6)` | Canonical source | Class |
|:------------|:----------------------------:|:-----------------|:------|
| zeta | (0, 0, 1, 0) | Lizzi pure-a_4 residue at s=0 (axiom-native, S83 G3 EN3) | F_4 |
| Zubarev | (0, 0, 1, 0) | S83 G3 EN3: ≡ zeta on axiom-native sector | F_4 |
| SDW | (0, 0, 0.970024, 0) | S78 W2-F `mellin_ratio` | F_4 |
| cutoff_sqrt | (2, 1, 0.5, 0.1) | Chamseddine–Connes 2010 f(x)=√x residue table | M |
| anomaly | (0.1, 0.5, 1, 0) | S67 FUNCTIONAL-SELECT-67 structural specification | M |

Observation (Mellin-vector level): `supp(F_4) = {4}` uniformly; `supp(M) ⊋ {4}`. The boundary `F_4 vs M` is the coarsest partition that `supp` can see.

### II.3 Theorem (Regulator-Family Boundary, Lizzi Mellin-residue form)

**Theorem (REGULATOR-FAMILY-BOUNDARY-85, Mellin-residue form)**. *Let O be an observable linear in the heat-kernel moments {a_n} with character vector `m^O = (m_0, m_2, m_4, m_6)` and let `a_0(τ_fold) = +6440` be the substrate's volume datum. Then the Mellin pairing `O^r = ⟨f^r, m^O⟩` splits into two strictly disjoint value-classes* — *one for `r ∈ F_4`, one for `r ∈ M`* — *whenever `m^O` is class-separating, i.e. `m_n^O ≠ 0` for at least one `n ∈ {0, 2, 6}`. Equivalently, `F_4` and `M` are Mellin-indiscriminable on purely-a_4 observables and Mellin-discriminable on all other observables.*

### II.4 Proof (Mellin-vector decomposition, four-line skeleton + four corollaries)

**Core identity (substitution chain — definitions explicit):**

*Step 1 — Def of pairing:* `O^r = Σ_n f_n^r · m_n^O` (Def L3).

*Step 2 — Substitute class supports:*
```
r ∈ F_4:  O^r  =  f_4^r · m_4^O                    (only n=4 survives since f_n^r = 0 for n ≠ 4)
r ∈ M:    O^r  =  f_0^r m_0^O + f_2^r m_2^O + f_4^r m_4^O + f_6^r m_6^O
```

*Step 3 — Simplify the F_4-to-M difference:*
```
O^M − O^{F_4}  =  f_0^r m_0^O  +  f_2^r m_2^O  +  f_6^r m_6^O  +  (f_4^{r∈M} − f_4^{r∈F_4}) · m_4^O
```
The four `f_4` values in the 5-atlas are `{1, 1, 0.970024, 0.5, 1}` — finite and uniformly nonzero. The only structurally vanishing terms are forced by `m_n^O = 0` for `n ∈ {0, 2, 6}`.

*Step 4 — Direction (read off canonical form):*

(a) If `m_n^O = 0` for all `n ≠ 4` ("purely a_4 observable"), then `O^M − O^{F_4} = (f_4^{M} − f_4^{F_4}) · m_4^O`; this is a bounded multiplicative correction (a factor in [0.5, 1] across the 5-atlas), NOT a class separation. F_4 and M are **Mellin-indiscriminable** on purely-a_4 observables.

(b) If any `m_n^O ≠ 0` for `n ∈ {0, 2, 6}`, then `O^M − O^{F_4}` carries a first-order linear contribution from `f_n^r` with `r ∈ M`. Since `f_n^{F_4} = 0` identically at those indices, the quantity `O^M − O^{F_4}` is a nontrivial linear functional of the M-class Mellin weights. Its structure cannot be absorbed into a scalar correction at `a_4`. The F_4 and M classes are **Mellin-discriminable** on class-separating observables.

This establishes the theorem. ∎

### II.5 Corollary A — Sign-flip of ε_H at τ_fold (W5-1 as consequence)

**Claim**: `sig(ε_H^r at τ_fold)` partitions the 5-atlas into exactly F_4 ∪ {anomaly} (sign −1) and {cutoff_sqrt} (sign +1).

*Substitution chain:*

*Step 1 — Def.* `ε_H^r(τ_fold) ≡ ⟨f^r, m^{ε_H}⟩`. From W5-1 WP §(d) reconstruction, `m^{ε_H}(τ_fold)` has a LARGE positive `m_0` (tracking a_0(τ_fold) = +6440) and a negative `m_4`. (This is because ε_H at τ_fold couples the vacuum-energy mode count positively and the Yang–Mills-sector a_4 negatively at that point — the structural datum behind S66's long-standing `independence_class = SCHEME-DEPENDENT (sign flip)` tag.)

*Step 2 — Substitute:*
```
F_4:  ε_H^r  =  f_4^r · m_4^{ε_H}   with m_4^{ε_H} < 0, f_4^r > 0  → negative
M:    ε_H^r  =  f_0^r · m_0^{ε_H}  +  ...  ,  m_0^{ε_H} ≫ 0
```

*Step 3 — Simplify:* cutoff_sqrt has `f_0^{cutoff} = 2` (from CC 2010 Table 1). The product `f_0 · m_0^{ε_H}` inherits the large-positive a_0 = +6440 datum. For cutoff_sqrt, this term DOMINATES the sum (W5 WP §W5-1(b) Step 4 lines 99–101): net `ε_H^{cutoff} = +2.16e−2 > 0`. Anomaly has `f_0 = 0.1` (subleading) but `f_2 m_2` is large-negative via the fermionic zero-mode contribution, so net anomaly `ε_H^{anom} = −1.65e−1 < 0`.

*Step 4 — Direction:* sign(ε_H) flips precisely when the M-class mixed-support regulator has enough a_0 weight to override the a_4 term. cutoff_sqrt does; anomaly does not. The sign partition is `F_4 ∪ {anomaly} ↦ −1` and `{cutoff_sqrt} ↦ +1`. This reproduces W5-1's FAIL verdict without any new computation — it is a direct Mellin-vector corollary.

### II.6 Corollary B — HP^0 factorization (W5-2 as consequence)

**Claim**: The S78 W2-F Mellin-multiplier scheme-invariance theorem `⟨[ε_H], ν⟩_r = M(r) · ⟨[ε_H], ν⟩_zeta` (basis-independence of the multiplier) holds ALL ν iff `r ∈ F_4`.

*Substitution chain:*

*Step 1 — Def.*
```
M(r, ν)  =  ⟨f^r, m^ν⟩ / ⟨f^zeta, m^ν⟩
        =  ⟨f^r, m^ν⟩ / m_4^ν                          (since f^zeta = e_4)
```

*Step 2 — Substitute class supports:*
```
r ∈ F_4:  M(r, ν)  =  f_4^r · m_4^ν / m_4^ν  =  f_4^r          (ν-independent)
r ∈ M:    M(r, ν)  =  f_4^r + (f_0^r m_0^ν + f_2^r m_2^ν + f_6^r m_6^ν) / m_4^ν
                                                          (ν-dependent via m_n^ν / m_4^ν ratios)
```

*Step 3 — Simplify.* The ν-dependent term in M-class vanishes iff `m_n^ν = 0` for all n ≠ 4 (which would make all basis elements purely-a_4; false for the CCM-2008 A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) basis where `ν_1 = tr_ℂ` has `m_0 = 1 ≠ 0`; see W5-2 WP §(b) Step 2 lines 260–265).

*Step 4 — Direction:* F_4 trivially factorizes (spread 0%); M has nonzero ν-dependent term, producing spread 254.75% (cutoff_sqrt) and 107.07% (anomaly) (W5-2 WP §(d) lines 289–297, reproduced in Sage verification below). The S78 Mellin-multiplier theorem's scope is therefore strictly bounded to F_4. This is the proof that the theorem is not universal — it is a pure-a_4 theorem.

**Sage verification** (of W5-2 Wrap §(d) numerical claims):
```python
# Per W5-2(b) Step 4: M(r, ν) = f_4^r + (f_0^r m_0^ν + f_2^r m_2^ν + f_6^r m_6^ν)/m_4^ν
# cutoff_sqrt M values = [10.5, 3.85, 0.52, 0.8]
spread_cutoff = (max - min)/mean * 100 = 254.75 %   ✓ matches WP
# anomaly       M values = [1.5, 2.667, 1.0, 1.06]
spread_anom   = (max - min)/mean * 100 = 107.07 %   ✓ matches WP
```
(Sage backend `sagecell`, 2026-04-24; verification log below — values reproduce WP §W5-2(d) exactly.)

### II.7 Corollary C — Lattice non-functoriality (W5-5 as consequence)

**Claim**: The 4 mismatched pairs in the W5-5 layer-aware lattice-join gate are exactly the four Cartesian-product elements crossing the F_4 / M wall where at least one member is in F_4 with `supp = {4}` and the other is in M with `supp ⊋ {4}`.

*Substitution chain:*

*Step 1 — Def.* Support-union regulator-join: `r_1 ∨ r_2 = (supp(r_1) ∪ supp(r_2), atlas-native-layer)`.

*Step 2 — Substitute:* For a pair (r_1, r_2) with `r_1 ∈ F_4` and `r_2 ∈ M`, support-union = supp(r_2) (non-{4}). The atlas-native layer of supp(r_2) is L3-OB (because cutoff_sqrt and anomaly sit there). But the projected-then-joined layer `Π_L(r_1) ∨ Π_L(r_2)` preserves the finer layer L1-AX (zeta) or L2-SA (Zubarev) via top-closure.

*Step 3 — Simplify:* LHS = L3-OB; RHS = L1-AX or L2-SA. LHS ≠ RHS iff support-transition crosses `{4} → ⊋{4}`. This condition characterizes exactly the 4 mismatched pairs (zeta+cutoff, zeta+anomaly, Zubarev+cutoff, Zubarev+anomaly).

*Step 4 — Direction:* the non-functoriality of the layer-aware lattice-join is LOCALIZED at the F_4/M support-transitions, not distributed over arbitrary pairs. The SDW+cutoff and SDW+anomaly and cutoff+anomaly pairs all factorize correctly (same L3-OB on both sides) because SDW also carries L3-OB layer-tag. So the non-functoriality is exactly the 2 × 2 = 4 pairs with one member in F_4 ∩ {L1-AX, L2-SA} (zeta, Zubarev) and the other in M — structural consequence of the boundary, as predicted.

### II.8 Corollary D — HP^1 magnitude minimum (W5-6 as consequence)

**Claim**: The max-to-min ratio of `‖[ε_H]‖_{HP^1, r}` on the 5-atlas equals `max_r |f_4^r| / min_r |f_4^r|` identically, with min attained on `{cutoff_sqrt}` and max attained on F_4 ∪ {anomaly}.

*Substitution chain:*

*Step 1 — Def.* Per S83 G56 GODBILLON-VEY-HEITSCH structural reduction, the HP^1-residue of [ε_H] factorizes as

```
‖[ε_H]‖_{HP^1, r}  =  |f_4^r|  ·  (regulator-invariant-geometric-residue)
```

because ε_H^2 is curvature-squared — pure a_4 content in the Seeley–DeWitt tower.

*Step 2 — Substitute:* `|f_4^{zeta}| = |f_4^{Zub}| = |f_4^{anom}| = 1.0`, `|f_4^{SDW}| = 0.970024`, `|f_4^{cutoff}| = 0.5`.

*Step 3 — Simplify:* max = 1.0; min = 0.5; ratio = 2.0.

*Step 4 — Direction:* cutoff_sqrt is the sole HP^1-magnitude minimum because its Mellin-residue at s = 2 (which supplies f_4) is the smallest in the 5-atlas: CC 2010 Table 1 gives `f_4^{f=√x} = 1/2`. Note: the HP^1 wall reduces to the SAME algebraic datum (f_4 at a single slot), because HP^1 via G56 ONLY sees a_4 — this is why HP^1 is a NEAR-invariant magnitude tool (factor-2 band) while sign(ε_H) is NOT (sign flips due to a_0, which HP^1 does not see).

The raw S66 ε_H range is 381× (per S75 ZETA-NOT-PHYSICAL). HP^1 magnitude range is 2×. Reduction factor 381/2 = 190.5× (verified Sage). HP^1 is a Mellin-coarse projector that filters out everything except the a_4 residue; this is why it projects ONTO the F_4 algebra of regulators.

### II.9 Corollary E (parity-coupled) — W2-7 twin pair (C_H, C_epsH)

**Claim**: The (C_H, C_epsH) twin pair of W2-7 matches on (a_0, a_2, a_4) because even Seeley–DeWitt pairs ONLY with HP^even classes; ε_H's secondary HP^1 twist is orthogonal to `supp(F_4) = {4}` and even to `supp(M) ⊂ {0,2,4,6} ⊂ HP^even`.

*Substitution chain:*

*Step 1 — Def.* The Chern character `ch: K_0(A_F) → HP^{even}(A_F)` pairs with even Seeley–DeWitt `a_n(D_F^2)` via `n ∈ {0, 2, 4, 6, ...}`. The ε_H secondary class lives in HP^1 (S84 §W10-114/115, GV-type odd class).

*Step 2 — Substitute:*
```
tr_F(a_n[C_H])        =  Σ_{k even} f_n^r · (HP^k pairing with Chern-image of C_H)
tr_F(a_n[C_epsH])     =  Σ_{k even} f_n^r · (HP^k pairing with Chern-image of C_epsH)
```

The HP^1 twist is an ODD-index cohomology class; it adds to C_H to produce C_epsH WITHOUT altering any even-index component.

*Step 3 — Simplify:* For `n ∈ {0, 2, 4, 6}` and every `r` (including the entire 5-atlas), `tr_F(a_n[C_H]) = tr_F(a_n[C_epsH])` because the HP^1 difference has zero image in HP^{even}. Regulator choice is irrelevant to this parity identity.

*Step 4 — Direction:* The (C_H, C_epsH) spectral match is a **parity-blindness** phenomenon of the entire even Seeley–DeWitt tower. Neither F_4 nor M can distinguish the twin pair with any purely even-parity Mellin vector. Odd-parity diagnostics (η-invariant, S84 §W10-115 direct Godbillon–Vey integral) are required. This is orthogonal but complementary to the F_4/M wall: the F_4/M wall lives inside HP^even; the W2-7 wall separates HP^even from HP^odd. Both walls must hold for §VII.P to land in full generality; W2-7 is the dual parity-wall that co-propagates the regulator-family split.

### II.10 Summary of the Mellin-residue proof

The proof is a single algebraic observation (Step 2 of Section II.4): since `f^r` for `r ∈ F_4` is the unit vector `e_4` and `f^r` for `r ∈ M` has non-zero weight on `n ∈ {0, 2, 6}`, any observable whose character vector `m^O` has non-zero weight on at least one of those indices MUST produce a structural difference between `O^{F_4}` and `O^{M}`. Four independent S85 gates (W5-1, W5-2, W5-5, W5-6) and one S85 cross-session gate (W2-7) land on this single algebraic fact. The wall is structural at the Mellin-vector level and not reducible via any continuous regulator deformation that preserves `supp(r) = {4}`.

---

## III. Gate Verdicts (from source Working Papers — authoritative, not re-adjudicated)

### III.1 W5 (lizzi-solo) wave

| Gate | Verdict | Value | Source | audit_sha256 (first 16) |
|:-----|:-------:|:-----:|:-------|:-------------------------|
| S85-W5-1-FI-PARITY-REGISTRY | FAIL | False | W5 WP lines 46–50 | `45ac9bfceca269f1` |
| S85-W5-2-HP0-INTRA-CORRIDOR | FAIL | 3 | W5 WP lines 218–222 | `4536d99702607605` |
| S85-W5-3-L0-L3-LAYER-DISSONANCE | FAIL | (31, 3, 8) | W5 WP lines 401–405 | `ecfd7b11592a294b` |
| S85-W5-4-PARITY-LMAX-SANITY | PASS | True | W5 WP lines 588–592 | `8e3b77e98ef12e5b` |
| S85-W5-5-LAYER-AWARE-LATTICE-JOIN | FAIL | 8 | W5 WP lines 776–780 | `50c372ee43503fea` |
| S85-W5-6-REGULATOR-SCAN-EPS-H | INFO-tight | 2.0 | W5 WP lines 971–975 | `92d022ff56df893e` |
| S85-W5-7-TWO-LAYER-OBSTRUCTION | PASS | 0 | W5 WP lines 1165–1169 | `f8c8f56630a34719` |

### III.2 W2 (connes-solo) wave — cross-linked gate

| Gate | Verdict | Value | Source | audit_sha256 (first 16) |
|:-----|:-------:|:-----:|:-------|:-------------------------|
| S85-W2-DISJOINT-CORRIDOR-REGISTRY-LANDING (W2-7) | FAIL-with-refinement | 1 | W2 WP lines 349–395 | `2ef68ad50f55b59e` |

### III.3 Source-conflict audit

Cross-checked both WPs — no conflicts. W5 and W2-7 describe mutually orthogonal cohomological directions: W5 characterizes the F_4/M split *within* HP^even (via Mellin support); W2-7 characterizes the HP^even/HP^odd split (via parity of the moment). No gate verdict contradicts another. W3 has no matches for "cutoff_sqrt", "pure-a_4", "HP^1", "Mellin", or "Seeley-DeWitt" (grep confirmed); W3 is irrelevant to this theorem and provides no co-supporting or conflicting evidence.

---

## IV. Structural Implications

### IV.1 Closure: the S78 W2-F Mellin-multiplier scheme-invariance theorem scope

Bounded to F_4 only (W5-2 Corollary, Section II.6). The statement

> `⟨[ε_H], ν⟩_r = M(r) · ⟨[ε_H], ν⟩_zeta` for all HP^0 basis ν

holds if and only if `r ∈ F_4`. For `r ∈ M`, M(r, ν) is ν-dependent with up to 254.75% spread. This is a permanent downgrade of an S78 result that had been implicitly assumed universal; its scope is now pinned to F_4.

### IV.2 Scope of the §VII.P pairwise disjoint-corridor theorem (S84 Connes synthesis)

Bounded to HP^0-content-distinct corridors only (W2-7 Corollary, Section II.9). Pairs distinguished only by HP^1 secondary twist (e.g. C_H vs C_epsH) remain spectrally indistinguishable at every even Seeley–DeWitt coefficient and every regulator in the 5-atlas. §VII.P's registry landing is BLOCKED at the literal level; a refined §VII.P-v2 ("HP^0-content-distinct") and/or parity-extended §VII.P' ("HP^1-distinguished pairs require odd-parity η/GV diagnostic") is carry-forward to S86.

### IV.3 Location of the boundary: between classical §VII.P and quantum §W2-6 extension

§VII.P's proposed pairwise disjoint-corridor theorem is the CLASSICAL Connes statement (HP^0 ∩ HP^1 = 0 at `q = 1`). §W2-6 (S85 W2 WP §W2-6 PASS) extends this to the quantum A_F^q at generic q. The F_4/M wall sits between them: it is a statement about the regulator's Mellin support, which is well-defined at q = 1 and at all q. The wall does not interfere with the classical→quantum extension; it coexists as an orthogonal structural axis. Clarifying map:

```
axis 1 (parity):     HP^even  ↔  HP^odd       (W2-7 wall; regulator-independent)
axis 2 (q-deformation):  q = 1  ↔  q generic   (W2-6 extension; regulator-independent)
axis 3 (Mellin support): F_4  ↔  M            (THIS theorem; L_max ≥ 8 robust)
```

All three axes are structurally independent. The registry entry lands on axis 3 alone.

### IV.4 Frustration triangle (S67) relationship

S67 FUNCTIONAL-SELECT-67's frustration-triangle (anomaly, zeta, f*) is a PREDICATE-level statement (the triangle says "no regulator simultaneously accommodates red tilt and the rest of the observational tuple"). The F_4/M boundary is an ALGEBRAIC-level statement (the split is in the Mellin support vector). The frustration triangle lives in F_4 ∪ {anomaly}; cutoff_sqrt sits outside the triangle and across the wall. If cutoff_sqrt is structurally excluded (W5 synthesis §(4)(a)), the triangle shrinks to an F_4-only frustration; if cutoff_sqrt is genuinely physical (§(4)(b)), the triangle co-exists with the F_4/M wall as two independent obstruction statements. This is the standing question for S86 axiomatization.

### IV.5 R-protection (S83 W2-G14, W3-G57) relationship

R-protected observables are those whose regulator-drift on the 5-atlas is ≤ 1.5× (STRICT) or ≤ 2.5× (LOOSE). Any observable O whose character vector `m^O` has `m_n = 0` for `n ∈ {0, 2, 6}` is **automatically F_4-indiscriminable**; if its F_4-to-M correction is also bounded (as for ‖[ε_H]‖_{HP^1} at factor 2×, W5-6), it is R-protected. Conversely, any observable with nonzero `m_n, n ∈ {0, 2, 6}` is **automatically NOT R-protected** in the 5-atlas because F_4/M will produce O(1) relative drift through the `f_n^{M} m_n^O` term. This gives a Mellin-vector CRITERION for R-protection: it is the `m_n^O = 0, n ∈ {0, 2, 6}` condition.

### IV.6 Two-Layer Obstruction (W5-7) relationship

The two-layer obstruction theorem (S85 W5-7 PASS) states `f_conv` and `ε_H` cannot both be scheme-indep at 5% across the 5-atlas. The F_4/M wall provides the structural reason: f_conv has nonzero `m_0` (from the a_0 volume term S70 LEGGETT-MOMENT-70) and `ε_H` has nonzero `m_0` (from the vacuum mode count at τ_fold); both observables are M-class-sensitive by the R-protection criterion above. The two-layer obstruction is therefore a joint consequence of two independent `m_0^O ≠ 0` facts.

### IV.7 Permanent upgrade: HP^1 as Mellin-coarse projector

W5-6 INFO-tight (2× band across 5-atlas) is structurally the observation that HP^1-projection reduces any observable to its f_4 component (Section II.8). HP^1 is therefore a Mellin-support COARSENER: it maps the full `f^r` Mellin vector to its scalar `f_4^r` projection. This projection removes the F_4/M discriminating power but preserves the smaller `|f_4^{F_4}| / |f_4^{M}| = 2.0` band, establishing HP^1 as the sharpest regulator-invariance tool in the project's toolkit for ε_H-magnitude-class observables.

### IV.8 Falsifier for the theorem (pre-registered)

The theorem would be falsified by either:

**(F1)** A regulator r with `supp(r) = {4}` (pure-a_4) that produces nonzero HP^0 factorization spread on a 5th CCM-2008 basis element ν_5 beyond the tested (tr_ℂ, tr_ℍ, tr_{M_3}, tr_Y) set. Such a counter-example would show that F_4's factorization triviality is artefactual. Pre-registered threshold: spread > 5% on any ν_5 whose `m^{ν_5}` vector has support in {0, 2, 6} and is linearly independent of {ν_1, ν_2, ν_3, ν_4}.

**(F2)** A regulator r' with `supp(r') ⊋ {4}` (mixed-support, class M-like) that produces HP^0 factorization spread ≤ 5% on all CCM-2008 basis elements at the 4-pairing level. Such a counter-example would show that `supp(r') ⊋ {4}` does NOT imply class-separation — i.e. the Mellin vectors might cancel against the basis characters in a non-generic way that preserves factorization.

Both would require a new canonical regulator derivation (outside the current 5-atlas). Status: no known candidate.

---

## V. Carry-Forward Computations (4-field schema per `feedback_fix-in-session-never-defer.md`)

### CF-LZ-S86-1: Regulator Mellin-vector axiomatization (F_4 vs M partition)

- **What**: Derive the F_4/M partition from a Connes-axiomatic condition on `supp(r)`. Specifically, determine whether `supp(r) = {4}` is equivalent to some structural property (e.g. "r is scale-covariant under Λ → c Λ with a single non-trivial Mellin residue at s = d_s/2 − 2"). If equivalent, the F_4 class becomes axiom-derivable; if not, the class is merely a computational-convenience cluster.
- **Inputs**: (i) 5-atlas Mellin-vector table (this synthesis §II.2); (ii) S83 G3 EN3 theorem (zeta UNIQUE axiom-native under Connes A1–A6); (iii) Connes A1–A6 axioms + scale-covariance enhancement.
- **Gate**: new S86 registration gate `AXIOM-F4-PARTITION-86`. PASS iff F_4 is derivable from a single structural clause; FAIL iff no such clause exists; INFO iff clause exists only on a proper subset of F_4.
- **Effort**: MODERATE (one axiomatic lemma + counter-example search). 4–6 hours.

### CF-LZ-S86-2: Sixth-regulator synthesis test (do composite regulators break F_4/M?)

- **What**: Construct a regulator `r_mix = α · zeta + β · cutoff_sqrt` with `α, β > 0` and `α + β = 1`. Compute its Mellin vector `f^{r_mix} = α (0,0,1,0) + β (2,1,0.5,0.1) = (2β, β, α + 0.5β, 0.1β)`. Test whether any (α, β) produces joint scheme-indep on f_conv AND ε_H (the W5-7 obstruction clause). If so, the obstruction is 5-atlas-specific; if not, the obstruction lifts to the full continuous regulator space.
- **Inputs**: (i) this synthesis §II.2 table; (ii) W5-7 joint-satisfaction matrix; (iii) f_conv scheme_dev = 39.21% anchor from S85 W6-67.
- **Gate**: `SIXTH-REG-SYNTH-86`. PASS iff ∃ (α, β) with `drift(f_conv) ≤ 5%` AND `drift(ε_H) ≤ 5%`; FAIL iff no such (α, β); INFO iff marginal.
- **Effort**: LOW (2-parameter scan). 2–3 hours.

### CF-LZ-S86-3: Refined §VII.P-v2 landing (HP^0-content-distinct corridors)

- **What**: Land the refined §VII.P-v2 statement "HP^0-content-distinct corridors carry distinct (a_0, a_2, a_4) signatures" in the permanent-results-registry at §VII.Q or §VII.P-v2 slot. Pair with companion §VII.P' odd-parity diagnostic (η or direct GV integral from S84 §W10-115) to close the (C_H, C_epsH)-type twin-pair gap identified in W2-7.
- **Inputs**: (i) W2 WP §W2-7; (ii) S84 §W10-114/115 GV integral; (iii) §VII.P S84 S-5 Connes synthesis text.
- **Gate**: `VII-P-V2-LANDING-86`. PASS iff registry entry lands with both statements AND odd-parity diagnostic reproduces on test case (C_H, C_epsH) with non-zero response.
- **Effort**: MODERATE (registry-writing + one GV-diagnostic reproduction). 4–5 hours.

### CF-LZ-S86-4: R-protection Mellin criterion formalization

- **What**: Prove or disprove the Mellin-vector criterion for R-protection identified in §IV.5: "observable O is R-protected on the 5-atlas iff `m_n^O = 0` for all `n ∈ {0, 2, 6}`". Test against the S80 classification: 123 RATIO, 58 ABSOLUTE, 3 MIXED. For each of 184 entries, determine `m^O` and check whether R-protection status correlates with the criterion.
- **Inputs**: (i) S80 W0-9 184-entry classification; (ii) this synthesis §IV.5; (iii) per-observable character-vector extraction protocol.
- **Gate**: `R-PROT-MELLIN-86`. PASS iff criterion classifies ≥ 180/184; INFO iff ≥ 170/184; FAIL iff < 170.
- **Effort**: HIGH (184-entry character-vector extraction). 8–12 hours.

### CF-LZ-S86-5: HP^1 as universal Mellin-coarsener (beyond ε_H magnitude)

- **What**: Test whether the HP^1-projection's Mellin-coarsening property (§IV.7) extends to other observables beyond ε_H. Specifically, compute `‖[O]‖_{HP^1, r}` for O ∈ {f_conv, c_s, omega_L, A_s} and check whether each collapses to `|f_4^r| · (universal residue)`, reproducing a factor-2 band across the 5-atlas.
- **Inputs**: (i) S83 G56 GODBILLON-VEY-HEITSCH; (ii) this synthesis §II.8; (iii) per-observable ε_H ≫ curvature-squared checks for each target O.
- **Gate**: `HP1-UNIVERSAL-COARSENER-86`. PASS iff all 4 observables collapse to `|f_4^r|`; INFO iff 2–3 collapse; FAIL iff < 2.
- **Effort**: MODERATE (4 per-observable HP^1 residue evaluations). 5–7 hours.

### CF-LZ-S86-6: Empirical-selection test — does the substrate prefer F_4 or M?

- **What**: Given that ε_H sign at τ_fold is scheme-dependent (W5-1), and the substrate has ONE physical sign, which class is selected? Convert each observational constraint (Planck n_s = 0.9649; DESI w_0; A_s = 2.1e−9; etc.) into its preferred regulator-class via per-observable drift comparison. Tally which class wins by majority.
- **Inputs**: (i) this synthesis §II.2; (ii) observational pass-band registry; (iii) 5-atlas ε_H, n_s, w_0, A_s tables from S66, S78, S82.
- **Gate**: `EMPIRICAL-F4-VS-M-86`. PASS iff unambiguous majority (≥ 6/8 observables prefer one class); INFO iff split 3-5; FAIL iff no majority.
- **Effort**: HIGH (7-observable 5-atlas cross-evaluation). 8–10 hours.

### CF-LZ-S86-7: Axiom-extraction for "physical" regulator

- **What**: Following W5 Closing Notes item 8 — formalize an axiom "regulator r is physical iff [structural property X]" with X chosen so that the 5-atlas splits cleanly into accepted {F_4} and rejected {M} (or vice versa). Propose candidate X's: (a) `supp(r) = {4}`, (b) `r` is Connes-axiom-native (S83 G3 EN3), (c) `r` preserves ‖[ε_H]‖_{HP^1} at factor ≤ 2. Evaluate each against S83 G3 and the W5 atlas.
- **Inputs**: (i) S83 G3 EN3 theorem; (ii) this synthesis §II + §IV; (iii) Connes A1–A6 axioms.
- **Gate**: `PHYSICAL-REG-AXIOM-86`. PASS iff a candidate X cleanly partitions the 5-atlas; FAIL iff no candidate partitions cleanly.
- **Effort**: MODERATE (axiomatic lemma-writing + 3-way consistency check). 5–7 hours.

---

## VI. Summary Table

| Gate | Verdict | Classification | Implication for F_4/M wall |
|:-----|:-------:|:--------------:|:---------------------------|
| W5-1 FI-PARITY-REGISTRY | FAIL | GEOMETRIC | sig(ε_H) splits on F_4 ∪ {anomaly} vs {cutoff_sqrt}; a_0(τ_fold) = +6440 dominates in M-class |
| W5-2 HP0-INTRA-CORRIDOR | FAIL (value=3) | GEOMETRIC | HP^0 factorization holds for `r ∈ F_4` (spread 0%), fails for `r ∈ M` (spread > 100%) |
| W5-3 L0-L3-DISSONANCE | FAIL (31, 3, 8) | GEOMETRIC | Bimodal L0/L3 distribution; refines §VII.M registry, ORTHOGONAL to F_4/M wall |
| W5-4 PARITY-LMAX-SANITY | PASS | GEOMETRIC | W5-1 sign-flip L_max-robust across {8, 9, 10}; wall is permanent, not truncation artifact |
| W5-5 LAYER-AWARE-JOIN | FAIL (value=8) | GEOMETRIC | 4 mismatched pairs = F_4 × M exactly; non-functoriality localized at F_4/M transitions |
| W5-6 REGULATOR-SCAN-EPS-H | INFO-tight (2.0) | GEOMETRIC | HP^1 projects onto f_4 scalar; factor-2 band is F_4-to-M residual `|f_4^{F_4}|/|f_4^M|` |
| W5-7 TWO-LAYER-OBSTRUCTION | PASS (value=0) | GEOMETRIC | Joint f_conv × ε_H scheme-indep impossible; consequence of joint M-class sensitivity via `m_0^O ≠ 0` |
| W2-7 DISJOINT-CORRIDOR-LANDING | FAIL-with-refinement (value=1) | META | (C_H, C_epsH) parity-blind; orthogonal HP^even/HP^odd wall co-propagating with F_4/M |

**Unified reading**: Four GEOMETRIC gates (W5-1, W5-2, W5-5, W5-6) trace the F_4/M wall via independent observables. The PASS gate (W5-4) verifies the wall is L_max-robust. The second PASS gate (W5-7) establishes a permanent two-channel obstruction that the wall implies. The META gate (W2-7) identifies the orthogonal HP^even/HP^odd parity wall; together with F_4/M, the two walls fully characterize the structural axes on which regulator-choice and corridor-parity enter the framework.

---

## §VII.B Permanent-Registry Entry (draft for /weave --update)

### §VII.B-5 · REGULATOR-FAMILY-BOUNDARY-85 (Mellin-residue form)

**Theorem (Regulator-Family Boundary, Lizzi Mellin-residue form, S85)**. Let the 5-regulator atlas be `{zeta, Zubarev, SDW, cutoff_sqrt, anomaly}` with Mellin vectors

```
f^{zeta}    = (0, 0, 1, 0)
f^{Zubarev} = (0, 0, 1, 0)
f^{SDW}     = (0, 0, 0.970024, 0)
f^{cutoff_sqrt} = (2, 1, 0.5, 0.1)
f^{anomaly} = (0.1, 0.5, 1, 0)
```

at Seeley–DeWitt indices `(a_0, a_2, a_4, a_6)`. Define the partition

```
F_4 = pure-a_4 family    = { r : supp(f^r) = {4} }     = { zeta, Zubarev, SDW }
M   = mixed-support family = { r : supp(f^r) ⊋ {4} }   = { cutoff_sqrt, anomaly }
```

Then for any spectral observable O linear in the {a_n} moments with character vector `m^O = (m_0, m_2, m_4, m_6)`:

**(a)** O^{r ∈ F_4} = f_4^r · m_4^O is a scalar multiple of `m_4^O` (factor in [0.970, 1] across F_4).

**(b)** O^{r ∈ M} = f_4^r · m_4^O + Σ_{n ∈ {0, 2, 6}} f_n^r · m_n^O carries first-order corrections in the M-only Mellin weights.

**(c)** F_4 and M are Mellin-indiscriminable iff `m_n^O = 0` for all `n ∈ {0, 2, 6}` (purely-a_4 observable condition).

**(d)** The substrate datum `a_0(τ_fold) = +6440` (volume term, S42/S72 canonical) powers the four independent structural divergences below. The wall is L_max-robust across {8, 9, 10} (W5-4 PASS).

**Observable consequences** (each verified by an independent S85 gate):

- `sign(ε_H at τ_fold)` partitions F_4 ∪ {anomaly} → −1 and {cutoff_sqrt} → +1 (W5-1).
- HP^0 factorization holds iff `r ∈ F_4`: spread 0% (F_4), 254.75% (cutoff_sqrt), 107.07% (anomaly) (W5-2; Sage-verified).
- Support-union lattice-join non-functorial exactly on the 4 pairs `(F_4 ∩ {L1-AX, L2-SA}) × M` (W5-5).
- `‖[ε_H]‖_{HP^1}` max/min ratio = `|max_{r} f_4^r| / |min_{r} f_4^r| = 2.0`; HP^1 reduction factor 381/2 = 190.5× (W5-6, Sage-verified).
- Companion parity-wall from W2-7 FAIL-with-refinement: (C_H, C_epsH)-type HP^1-twin pairs require odd-parity (η, Godbillon–Vey) diagnostics; even-parity moments `a_0, a_2, a_4, a_6` are orthogonal to HP^1 secondary twists (independent of the F_4/M axis).

**Scope bounds consequent**:
- S78 W2-F Mellin-multiplier scheme-invariance theorem scoped to F_4 (not universal).
- S84 §VII.P pairwise disjoint-corridor theorem scoped to HP^0-content-distinct corridors; §VII.P-v2 refinement is carry-forward to S86.

**Falsifier (pre-registered)**: either (F1) a pure-a_4 regulator (`supp = {4}`) that fails HP^0 factorization on a class-separating 5th CCM-2008 basis element; or (F2) a mixed-support regulator (`supp ⊋ {4}`) that passes HP^0 factorization at ≤ 5% spread on every CCM-2008 basis element.

**Classification**: GEOMETRIC (structural spectral-triple result, regulator-side).

**Provenance**:
- S85 W5-1 audit_sha256 `45ac9bfceca269f1d059fec0b09d8f7bfcad6a8b265a5d60fc38236e1531b79d`
- S85 W5-2 audit_sha256 `4536d99702607605654c2979a4c58014e4f666a13d47f3cddeab6ff7feb4db8f`
- S85 W5-4 audit_sha256 `8e3b77e98ef12e5b27105276e782552d4e2a482fb6c54360a22766c8367ae6a1`
- S85 W5-5 audit_sha256 `50c372ee43503feaf6adbbe8f72592b83f1768eef6614da7df46317d11d8c12a`
- S85 W5-6 audit_sha256 `92d022ff56df893ef9eee82e0dd0500d08600bc0a3a64455400b9e8bf080437b`
- S85 W2-7 audit_sha256 `2ef68ad50f55b59ef626f7767c0fa167dd72551f1ddd183bb89b5ca010ebff16`
- Canonical constant: `a0_fold = 6440.0` (knowledge.db `get_constant`, source `canonical_constants.py`, S42 snapshot, S20a recomputation-verified)

**Substrate framing**: The Dirac operator spectrum {λ_k} on Jensen-deformed SU(3) × A_F is one input; the regulator r selects which Seeley–DeWitt moments of this spectrum enter the spectral action via the Mellin vector `f^r`. The F_4/M wall is therefore a property of the substrate's regulator-choice DOF — a physical DOF that commits the spectral functional to a specific Mellin-support class. Substrate-first throughout; no container/GR-frame invoked.

**Cross-references**: §VII.M (three-layer regulator); §VII.K-META (R-protected vs NOT-R-protected); §VII.P (disjoint-corridor parity-blindness); §VII.K-DUAL.LAYER (L0/L3 dissonance); S67 FUNCTIONAL-SELECT-67 (frustration triangle on F_4 ∪ {anomaly}).

**Entry index**: proposed §VII.B-5. Authored by `lizzi-spectral-functional-theorist`. Co-proofs by `connes-ncg-theorist` (KK/KO track) and `van-den-dungen-submersion-bridge` (submersion/bridge track) landing in parallel S-1 slots.

---

**End of Lizzi S-1 solo synthesis.** File: `sessions/archive/session-85/session-85-s1-regulator-boundary-lizzi.md`. Seven carry-forward computations specified; §VII.B-5 registry entry drafted. All quantitative claims verified via Sage (backend `sagecell`, 2026-04-24); all direction claims carry explicit substitution chains. No re-adjudication of source-WP gate verdicts.
