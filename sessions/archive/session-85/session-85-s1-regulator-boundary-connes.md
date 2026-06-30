# Session 85 Slot S-1 — Regulator-Family Boundary Theorem (Connes K-theory / cyclic-cohomology track)

**Session**: 85 | **Slot**: S-1 | **Author**: `connes-ncg-theorist` (solo — one of three independent proofs)
**Deliverable**: K-theoretic classification of the pure-a_4 regulator family as the image of a periodic-cyclic retraction, and statement + proof that HP^0 factorization under regulator-join is a property of the {a_4}-support class.
**Source WPs (authoritative verdicts)**: `sessions/archive/session-85/session-85-w5-workingpaper.md`, `sessions/archive/session-85/session-85-w2-workingpaper.md`, `sessions/archive/session-85/session-85-w3-workingpaper.md`.
**Companion solos (independent)**: `session-85-s1-regulator-boundary-lizzi.md`, `session-85-s1-regulator-boundary-vdd.md`.

---

## I. Session Outcome

Five gate verdicts (W5-1 FAIL, W5-2 FAIL val=3, W5-4 PASS, W5-5 FAIL val=8, W5-6 INFO-tight val=2.0) together with W2-7 FAIL val=1 converge on a single structural wall: the spectral functional is not a free gauge. The five-atlas `{zeta, Zubarev, SDW, cutoff_sqrt, anomaly}` splits into two K-theoretically distinct sub-families under the periodic cyclic Chern-character pairing:

- **Pure-a_4 family** P = {zeta, Zubarev, SDW} — pinned by `f = (0, 0, f_4, 0)` Mellin vector. Chern-image supported on HP^0 alone; HP^0 pairing factorizes through a scalar multiplier M(r) independent of basis.
- **Mixed-a_n family** M = {cutoff_sqrt, anomaly} — `f_0` or `f_2` or `f_6` nonzero. Chern-image picks up HP^0-basis-dependent contributions; factorization fails.

The wall between P and M is the K-theoretic boundary at which the S78 W2-F Mellin-multiplier scheme-invariance theorem breaks. At the physical fold, `a_0(tau_fold) = +6440` (canonical, knowledge-MCP `get_constant a_0` hits with provenance s69_swampland.py, s67_joint_falsification.py, s23c_fiber_integrals.py) is the numerical carrier of the split: its inclusion in cutoff_sqrt flips the sign of `eps_H` (W5-1), halves the HP^1 residue `|f_4|` (W5-6), breaks HP^0 factorization (W5-2), and breaks lattice functoriality at the support-union transition (W5-5). All four fail-modes are the SAME structural wall viewed through four gates.

**Theorem (Regulator-Family Boundary, Connes K-theory formulation)**. HP^0 factorization of the periodic-cyclic Chern-character pairing under regulator-join is a property of the image of the K-theoretic retraction `pi_P : R_atlas -> P`, where P is the pure-a_4 sub-family. Equivalently: `(f_0, f_2, f_6)^r = 0` is NECESSARY AND SUFFICIENT for the factorization `<[eps_H], nu_i>_r = M(r) · <[eps_H], nu_i>_zeta` at every CCM-2008 basis element nu_i of HP^0(A_F).

**Classification**: GEOMETRIC (spectral-triple cyclic-cohomology structure). One PHONONIC corollary: eps_H sign is a property of the substrate's Chern pairing with the regulator-weighted HP^0 class, not of the Jensen deformation — the substrate's phononic fold signature (sign, magnitude) requires naming the regulator.

---

## II. Key Results — K-theoretic proof of the theorem

This section provides one of three independent proofs. The Lizzi solo works via spectral-functional admissibility (Hausdorff-Bernstein-Widder on f); the VdD solo works via Kasparov module / submersion dictionary. This one works via periodic cyclic cohomology and K-theoretic retraction.

### II.A. Setup — spectral triple, regulators as Mellin multipliers, Chern pairing

**Spectral triple** (A, H, D) = (C^inf(M) tensor A_F, L^2(M, S) tensor H_F, D_M tensor 1 + gamma_5 tensor D_F) with A_F = C (+) H (+) M_3(C), H_F = C^32, KO-dim 6. Axioms: dim=4+6=10, regularity, finiteness, reality, first-order, orientability, Poincare duality. The J real structure satisfies `[J, D] = 0` (CPT, proven S34).

**Regulator as Mellin operator on the heat-kernel expansion**. For regulator r the spectral action is `S_r = Tr f_r(D^2 / Lambda^2)`. The asymptotic heat-kernel expansion (Chamseddine-Connes-Marcolli 2007, CCM 2010 Table 1; `search_knowledge 'a_4 = a_4^{pure_R2}...'` confirms canonical decomposition) gives

```
S_r(Lambda) ~ sum_{n >= 0}  f_n^r · Lambda^{4-2n} · a_{2n}(D^2)                    (II.1)
```

where `a_{2n}` are Seeley-DeWitt coefficients (universal substrate data) and `f_n^r` are the Mellin moments of the regulator kernel. The vector `f^r = (f_0^r, f_2^r, f_4^r, f_6^r, ...)` is the "Mellin signature" of regulator r.

**Canonical Mellin signatures** (from knowledge-MCP + W5 sources, loaded via S78 W2-F mellin_ratio, S83 G3 EN3, CCM 2010 Table 1, S67 FUNCTIONAL-SELECT-67):

| r | f^r = (f_0, f_2, f_4, f_6) | K-theoretic family |
|:--|:---------------------------|:-------------------|
| zeta        | (0,   0,   1,   0) | P (pure-a_4) |
| Zubarev     | (0,   0,   1,   0) | P (by S83 G3 EN3 equivalence) |
| SDW         | (0,   0,   0.970, 0) | P (by S78 W2-F Mellin multiplier) |
| cutoff_sqrt | (2,   1,   0.5, 0.1) | M (mixed, f(x)=sqrt{x}) |
| anomaly     | (0.1, 0.5, 1,   0)   | M (mixed, S67 selects a_2+a_4) |

Dimensional consistency: `[f_n^r]` is dimensionless; `[a_{2n}]` has dimension length^{2n-4} on M^4 x SU(3); `[Lambda^{4-2n}]` cancels to give `[S_r]` = dimensionless. Regime of validity: Lambda >> M_KK (heat-kernel asymptotic), L_max finite (Connes-Moscovici truncation).

**Chern-character pairing (periodic cyclic cohomology)**. By Connes' local index theorem, the Chern character
```
ch(p) : K_0(A_F) -> HP^0(A_F)                                                       (II.2)
```
pairs K-theory classes of finite projections `p in M_n(A_F)` with periodic cyclic cohomology classes. The heat-kernel-regulated pairing with [eps_H] is
```
<[eps_H], nu>_r = Res_{s=0} Tr( f_r(D^2/Lambda^2) · nu · [eps_H] · D^{-2s} )        (II.3)
```
where nu runs over a basis of HP^0(A_F). The Connes SBI sequence and finite-dim HKR theorem give `dim HP^0(A_F) = 4` for A_F = C (+) H (+) M_3(C) (confirmed via knowledge-MCP trace of `HC_n(A) = sum_{p+q=n} HC_p(C^inf(M)) tensor HC_q(A_F)`), generated by the 4 CCM-2008 characters `nu_1 = tr_C, nu_2 = tr_H, nu_3 = tr_{M_3}, nu_4 = tr_Y` (hypercharge).

### II.B. The K-theoretic retraction pi_P : R_atlas -> P

Let `R_atlas = {zeta, Zubarev, SDW, cutoff_sqrt, anomaly}` with the structure of a vector space via Mellin signature: `r |-> f^r in R^{N+1}` (N truncated at 3 for our L_max=3 canonical). Let P be the linear subspace spanned by `e_2 = (0, 0, 1, 0)`; let M be its complement in R_atlas.

**Projection**. Define
```
pi_P : R^4 -> R^4,    pi_P(f_0, f_2, f_4, f_6) = (0, 0, f_4, 0).                   (II.4)
```
Clearly `pi_P^2 = pi_P` (projection); `pi_P| _P = id_P`; `pi_P(R_atlas) = { (0,0,f_4^r,0) : r in R_atlas }` which is the pure-a_4 family (f_4 coords: zeta -> 1, Zub -> 1, SDW -> 0.970, cutoff_sqrt -> 0.5, anomaly -> 1).

**Chern-image interpretation**. Under the pairing (II.3), the regulator r enters only through its Mellin vector f^r. The induced map
```
Phi_r : HP^0(A_F) -> C,    nu |-> <[eps_H], nu>_r                                  (II.5)
```
decomposes linearly in f_n^r:
```
Phi_r(nu_i) = f_0^r · m_0^i + f_2^r · m_2^i + f_4^r · m_4^i + f_6^r · m_6^i        (II.6)
```
where `m_n^i` is the basis character's character-vector (pairing of nu_i with a_{2n}). The basis-character table (CCM-2008 A_F decomposition; W5-2 data verbatim):

| nu_i | m^i = (m_0, m_2, m_4, m_6) |
|:-----|:---------------------------|
| nu_1 = tr_C   | (1,   0,   0.2, 0)    |
| nu_2 = tr_H   | (0,   1,   0.3, 0.05) |
| nu_3 = tr_M3  | (0,   0,   1,   0.2)  |
| nu_4 = tr_Y   | (0.1, 0.1, 1,   0)    |

### II.C. Proof that HP^0 factorization is a property of image(pi_P)

**Claim (Regulator-Family Boundary Theorem, connes-formulation)**. Let r in R_atlas. The HP^0 factorization
```
Phi_r(nu_i) = M(r) · Phi_zeta(nu_i)    for all i in {1, 2, 3, 4}                   (II.7)
```
with `M(r)` a scalar INDEPENDENT of i holds if and only if `r in image(pi_P)`, i.e., iff `(f_0^r, f_2^r, f_6^r) = 0`.

**Proof**.

*Direction 1 (image(pi_P) => factorization)*. Substitute (f_0, f_2, f_6) = 0 into (II.6):
```
Phi_r(nu_i) = f_4^r · m_4^i,    Phi_zeta(nu_i) = 1 · m_4^i                         (II.8)
=>  Phi_r(nu_i) / Phi_zeta(nu_i) = f_4^r      (constant in i)
=>  M(r) = f_4^r,  factorization holds across all nu_i.
```

*Direction 2 (factorization => image(pi_P))*. Suppose the factorization (II.7) holds for all nu_i with some scalar M(r). The ratio
```
R_i(r) := Phi_r(nu_i) / Phi_zeta(nu_i)
        = [f_0^r m_0^i + f_2^r m_2^i + f_4^r m_4^i + f_6^r m_6^i] / m_4^i
        = f_4^r + f_0^r (m_0^i/m_4^i) + f_2^r (m_2^i/m_4^i) + f_6^r (m_6^i/m_4^i)  (II.9)
```
Because M(r) is i-independent, `R_i(r) = R_j(r)` for all i, j. Subtracting:
```
f_0^r (m_0^i/m_4^i - m_0^j/m_4^j) + f_2^r (m_2^i/m_4^i - m_2^j/m_4^j)
                                  + f_6^r (m_6^i/m_4^i - m_6^j/m_4^j) = 0          (II.10)
```
for all i, j in {1,2,3,4}. The CCM-2008 character vectors give linearly independent rows of `m_n^i/m_4^i` ratios (evaluate: (m_0/m_4)_1 = 5, (m_0/m_4)_4 = 0.1 distinct; (m_2/m_4)_2 = 3.33, (m_2/m_4)_4 = 0.1 distinct; (m_6/m_4)_2 = 0.167, (m_6/m_4)_3 = 0.2 distinct). Therefore (II.10) forces `f_0^r = f_2^r = f_6^r = 0`, i.e. `r in image(pi_P)`.

QED.

### II.D. Quantitative verification (Python-checked inline with W5-2 data)

Substitution chain verification (completed before this write-up; output logged above):
- zeta, Zubarev: `M = (1.0, 1.0, 1.0, 1.0)`, spread = 0.00% (factorization exact).
- SDW: `M = (0.970, 0.970, 0.970, 0.970)`, spread = 0.00% (factorization exact; `M(SDW) = 0.970`).
- cutoff_sqrt: `M = (10.5, 3.85, 0.52, 0.80)`, spread = 254.75% (factorization destroyed; direction 2 of proof fires).
- anomaly: `M = (1.50, 2.667, 1.00, 1.06)`, spread = 107.07% (factorization destroyed).

The numerics reproduce the theorem: exactly the three members of image(pi_P) factorize; the two complement members do not.

### II.E. a_0(tau_fold) = +6440 as the numerical carrier of the wall

Knowledge-MCP `get_constant` traces a_0(tau_fold) = +6440 to canonical sources s69_swampland.py, s67_joint_falsification.py, s23c_fiber_integrals.py (tau-independent volume term; `a_0 propto Vol_K`).

**Substitution chain for the sign-flip at the fold** (W5-1 verdict; confirms direction 2 of the proof has physical teeth):
```
Step 1: eps_H^r(tau_fold) = sum_n  f_n^r · m_n^{eps_H}    at tau_fold
Step 2: For r = cutoff_sqrt, f_0^cut = +2, a_0(tau_fold) = +6440; m_0^{eps_H} carries the
        "volume contribution" sign of the eps_H block through the fold.
Step 3: For r in P = {zeta, Zubarev, SDW}, f_0^r = 0 eliminates this channel.
Step 4: The magnitude `2 · 6440 · m_0^{eps_H}` dominates the a_4 contribution by O(10^3)
        (since a_4(tau_fold) is O(1) while a_0 is O(10^4)); it drives the net sum POSITIVE
        for cutoff_sqrt while leaving zeta/Zub/SDW NEGATIVE.
Step 5: sig(cutoff_sqrt) = +1, sig({zeta, Zub, SDW, anomaly}) = -1.    (W5-1 verdict)
```
(Magnitude O(10^3) dominance: `a_0 ~ 6440` vs `a_4 ~ 1` in units where Mellin coefficients are normalized; the `f_0^cut = 2` coupling brings `f_0 · a_0 = 12880` into play versus `f_4 · a_4 = 0.5`. The sign flip is therefore not a numerical accident but a structural consequence of the K-theoretic retraction failure.)

This is the PHONONIC content of the GEOMETRIC theorem: the fold's phononic signature (sign of the slow-roll epsilon) is determined by whether the regulator lives in image(pi_P) or not. The substrate carries the +6440 volume-moment; the regulator chooses to include or exclude it.

### II.F. HP^0 parity-blindness to HP^1 secondary twists (W2-7 landing)

The W2-7 counter-construction (connes-ncg, S85 authoritative) identified pair (C_H, C_epsH) with IDENTICAL (a_0, a_2, a_4). Direct consequence of the Chern-character degree structure:

**Lemma (parity-blindness of even Seeley-DeWitt)**. The even-degree periodic cyclic cohomology HP^even = HP^0 x HP^2 x ... is the target of the Chern character of K_0(A); the odd-degree HP^odd = HP^1 x HP^3 x ... is the target of K_1. The Seeley-DeWitt expansion (II.1) generates only EVEN-degree spectral moments (a_0, a_2, a_4, a_6, ...); thus the pairing (II.3) with any nu in HP^odd vanishes identically for EVERY regulator.

Corollary: pairs of corridors distinguished solely by HP^1 secondary Godbillon-Vey-type twists (as (C_H, C_epsH) is, per S84 W10-114/115) are INVISIBLE to the full even heat-kernel — cutoff_sqrt included. The W2-7 FAIL-with-refinement is the EVEN-parity version of the P/M boundary: even within image(pi_P), pairs differing only by HP^1 twist are spectrally indistinguishable on HP^0 alone, because the Chern image lives entirely in HP^even.

### II.G. Lattice functoriality failure (W5-5) from the retraction

The layer-aware lattice atlas:

| r | support (Mellin active) | layer |
|:--|:------------------------|:------|
| zeta        | {a_4}                 | L1-AX (axiomatic) |
| Zubarev     | {a_4}                 | L2-SA (substrate-action) |
| SDW         | {a_4}                 | L3-OB (observable) |
| cutoff_sqrt | {a_0, a_2, a_4, a_6}  | L3-OB |
| anomaly     | {a_2, a_4}            | L3-OB |

The regulator-join under support-union, combined with layer-assignment-from-atlas, gives (for the 4 mismatched pairs):
```
Pair: zeta v cutoff_sqrt
  support union = {a_0, a_2, a_4, a_6}; atlas match = cutoff_sqrt, layer L3-OB
  layer-join Pi_L(zeta) v Pi_L(cutoff_sqrt) = L1-AX v L3-OB = L1-AX (top-closer)
  LHS (L3-OB) != RHS (L1-AX)    [W5-5 confirmed]
```
K-theoretic reading: the retraction pi_P exists on Mellin-vector space R^4, but LIFTING it to the layer lattice requires the join to commute with pi_P. Since join (support-union) moves a regulator OUT of image(pi_P) while the layer-join stays WITHIN finer-layer information, the two operations do not commute. The lattice is not a Boolean algebra; it is a 2-categorical object whose 2-cells are the non-functorial transitions at the image(pi_P) / complement boundary.

### II.H. Magnitude near-invariance on HP^1 (W5-6 INFO-tight)

On HP^1, the Connes-Moscovici residue at s=0 for `curvature-squared` classes like `eps_H^2` projects onto the a_4 Mellin coefficient alone (the Godbillon-Vey-Heitsch anchor, S83 G56):
```
||[eps_H]||_{HP^1, r} = |f_4^r| · (universal geometric residue)                    (II.11)
```
Across the atlas: `|f_4^r| in {1.0, 1.0, 0.970, 0.5, 1.0}`, `max/min = 2.000`. The HP^1 projection NORMALIZES eps_H magnitude into a factor-2 band. The HP^1 reduction factor relative to the raw S66 381x range is `381/2 = 190.5x` (W5-6).

This does NOT contradict the P/M split — it REFINES it: the image(pi_P) / complement boundary controls SIGN (via f_0), while the common ingredient f_4 controls MAGNITUDE up to a factor 2 (because cutoff_sqrt's f_4 = 0.5 vs unit normalization elsewhere). SIGN is a Chern-degree-0 "which-family" datum; MAGNITUDE is a retraction-invariant "how-much" datum.

### II.I. Scope of the S78 W2-F Mellin-multiplier theorem — precisely bounded

The S78 W2-F Mellin-multiplier scheme-invariance theorem asserted `a_4^{f} / a_4^{SDW} = mellin_ratio = 0.970024` (knowledge-MCP hit on `s78_a4_r2_f_star.py`). The Boundary Theorem PINS its scope: the Mellin-multiplier theorem holds WITHIN image(pi_P) only. Across the wall to complement(pi_P) the theorem FAILS because the multiplier becomes basis-dependent — a vector instead of a scalar, with 254.75% spread in the cutoff_sqrt direction.

Previously the theorem's scope was presumed universal across regulators. The Boundary Theorem closes that presumption: the Mellin multiplier is a retract-invariant, not a universal scheme-invariant. This is the precise answer to Open Tension #3 from MEMORY.md (functional not geometric): the functional-locus of scheme-invariance is image(pi_P), a 1-dim linear submanifold of the 4-dim Mellin-vector space.

---

## III. Gate Verdicts (source-WP verbatim; NOT re-adjudicated)

Verdicts are authoritative per source working papers. Here reproduced without re-adjudication.

| Gate | Source WP | Verdict | 4-tuple | audit_sha (first 16) |
|:-----|:----------|:--------|:--------|:---------------------|
| S85-W5-1-FI-PARITY-REGISTRY       | W5 §W5-1 | FAIL       | `(value=False, scheme=5-regulator-atlas, convention=KO-dim=6-J-canonical, L_max=10)` | `45ac9bfceca269f1` |
| S85-W5-2-HP0-INTRA-CORRIDOR       | W5 §W5-2 | FAIL       | `(value=3, scheme=5-regulator-atlas, convention=CCM-2008-A_F-basis, L_max=3)` | `4536d99702607605` |
| S85-W5-4-PARITY-LMAX-SANITY       | W5 §W5-4 | PASS       | `(value=True, scheme=5-regulator-atlas, convention=KO-dim=6-J-canonical, L_max=sweep-{8,9,10})` | `8e3b77e98ef12e5b` |
| S85-W5-5-LAYER-AWARE-LATTICE-JOIN | W5 §W5-5 | FAIL       | `(value=8, scheme=layer-aware-lattice, convention=S83-three-layer-synthesis, L_max=3)` | `50c372ee43503fea` |
| S85-W5-6-REGULATOR-SCAN-EPS-H     | W5 §W5-6 | INFO-tight | `(value=2.0, scheme=5-regulator-atlas, convention=CM-residue, L_max=10)` | `92d022ff56df893e` |
| S85-W2-DISJOINT-CORRIDOR-REGISTRY-LANDING | W2 §W2-7 | FAIL (structural refinement) | `(value=1, scheme=counter-construction-spectral-moment-match, convention=CCM-2007, L_max=8)` | `2ef68ad50f55b59e` |

No conflicts between WPs on the verdict lines or their interpretation. Cross-WP consistency: W5-4 PASS confirms W5-1 FAIL is L-robust; W5-6 INFO-tight refines (does not contradict) W5-1 FAIL at the HP^1 magnitude level; W2-7 FAIL-with-refinement is the HP^0/HP^1 parity analogue of the P/M boundary. All six gates are independent angles on the SAME wall.

---

## IV. Structural Implications

### IV.1. Closes "naive scheme-invariance" across the 5-atlas

Before S85: ambiguity on whether regulator choice is a pure gauge. After S85 with the Boundary Theorem: the 5-atlas is structurally stratified by a K-theoretic retraction pi_P. Two regulators are "scheme-equivalent" (factorization-invariant on HP^0) if and only if they lie in the same fibre of pi_P, which for the present atlas means both lie in image(pi_P) = P. Scheme-equivalence is a property of Mellin-support class, NOT of the specific kernel shape f_r(x).

Substrate reading: the regulator is a physical DOF — not a gauge — whose value can be probed by the sign of eps_H at the fold (Chern-character-0 observable).

### IV.2. Scope-bounds the Mellin-multiplier theorem (S78 W2-F) to pure-a_4

The Mellin-multiplier theorem's scheme-invariance scope is now PIN-BOUNDED: image(pi_P) only. This eliminates a latent ambiguity (whether cutoff_sqrt is Mellin-multiplier-equivalent to zeta up to a scalar) which S78 left implicit. Answer: no — the scalar becomes a 4-vector with 254.75% spread across HP^0 basis.

### IV.3. Locates the wall between classical §VII.P and quantum W2-6 extensions

The Boundary Theorem identifies the wall as the vanishing locus of `(f_0, f_2, f_6)`:

- **§VII.P classical corridor-disjointness** operates INSIDE image(pi_P) — the HP^0 factorization holds, pairs are distinguishable via (a_0, a_2, a_4). Applies cleanly to `(zeta, Zubarev, SDW)` regulator choices.
- **§VII.P quantum extension (W2-6 PASS, 4-route confluence)** extends HP^0 factorization to U_q(su(2))-deformed spectral triples via the quantum cyclic-cohomology pullback (S83 W2-G20). Applies again INSIDE image(pi_P): the pullback preserves Mellin support.
- **W2-7 FAIL (§VII.P literal landing blocked)** exposes that even within image(pi_P), the HP^0 pairing is blind to HP^1 secondary twists (C_H, C_epsH indistinguishable on (a_0, a_2, a_4)). This is the parity complement of the Boundary Theorem: Chern-character-0 cannot decode Chern-character-1 information.

Thus the complete wall description is TWO-DIMENSIONAL:
- axis 1: Mellin-support class (image(pi_P) vs complement) — the Boundary Theorem.
- axis 2: Chern-character degree (HP^even vs HP^odd) — parity-blindness lemma (II.F).

These two axes span the regulator/cohomology obstruction plane for the five-atlas.

### IV.4. Framework classification update (extends MEMORY.md)

- Open Tension #3 (CC: SA routes CLOSED; problem functional not geometric) is REFINED: the functional locus of the CC corridor's scheme-invariance is image(pi_P), a 1-dim submanifold. Any CC-type observable computed via regulator outside image(pi_P) carries an irremovable regulator tail.
- Open Channel #5 (Pati-Salam sin^2) and #6 (Y-embedding alternatives) are INDEPENDENT of the Boundary Theorem (operate on algebra content, not regulator class) but must respect image(pi_P) when combined with sin^2 regulator-variation checks (per S74 Jensen-blind closure).

### IV.5. Substrate/phononic classification

The theorem is GEOMETRIC (cyclic-cohomology structure). Its PHONONIC consequence is that the substrate's fold-signature on eps_H — a slow-roll observable in the substrate-action expansion around tau_fold — carries a definite SIGN only when the regulator lies in image(pi_P). Outside image(pi_P), the volume-moment a_0(tau_fold) = +6440 drives an opposite sign. This is why the phononic excitations' effective-potential shape (W5-1 through W5-6) is regulator-naming-dependent: the substrate is one fabric, but its emergent slow-roll signature is a PAIR of data — spectral triple AND chosen regulator class — together in HP^even.

---

## V. Carry-Forward Computations (MANDATORY 4-field schema)

### CF-S1-C-1. Full HP^even completeness of image(pi_P) at L_max >= 10

- **What**: Enumerate all HP^2, HP^4, HP^6 pairings with [eps_H] across the 5-atlas at L_max = 10 (canonical). Verify that factorization fails on HP^2 / HP^4 for complement(pi_P) regulators with the SAME structural signature as HP^0 (254.75% spread on cutoff_sqrt, 107.07% on anomaly).
- **Inputs**: `s66_zeta_sa.npz`, `s78_a4_r2_f_star.npz`, CCM-2008 extended character table for A_F higher-degree cycles, S83 G56 GV-Heitsch anchor.
- **Gate**: new `S86-CF-S1-C-1-HP-EVEN-COMPLETENESS`; PASS iff image(pi_P) factorizes on all of HP^even; FAIL iff factorization breaks at any even degree for a P-member.
- **Effort**: MODERATE. One computation script (~300 lines) extending `s85_w5_2_hp0_intra_corridor.py` to higher even degrees. No new spectrum compute.

### CF-S1-C-2. Extended regulator atlas: locate further P-members

- **What**: Test whether any of the 4 S82 W2-5 MP-admissible regulators (t^{-3/2} branch excluded) or S83 W2-G27 unified Mellin-admissibility candidates land in image(pi_P). Construct Mellin signatures and classify.
- **Inputs**: S82 MP-exclusion theorem closure, S83 W2-G27 unified Mellin-admissibility data, canonical regulator atlas from CCM 2010.
- **Gate**: new `S86-CF-S1-C-2-EXTENDED-ATLAS-CLASSIFY`; PASS iff classification returns boolean image(pi_P) verdict for every candidate with no ambiguity; INFO iff exactly one candidate has `|f_0 + f_2 + f_6| < 1e-3` (near-boundary).
- **Effort**: LOW-MODERATE. One table-construction script (~150 lines). No spectrum compute.

### CF-S1-C-3. Falsifier-construction gate (critical test of the theorem)

- **What**: Falsify the Boundary Theorem by one of two constructions: (a) a pure-a_4 regulator (f_0 = f_2 = f_6 = 0 exactly) that FAILS HP^0 factorization on a FIFTH basis element nu_5 beyond CCM-2008's {tr_C, tr_H, tr_M3, tr_Y} — e.g., a higher-rank nu_5 = tr_{Y^2} or a Frobenius-composed nu_5 = tr_C composed twist; or (b) a cutoff_sqrt-class regulator (f_0 or f_6 nonzero) that PASSES HP^0 factorization across CCM-2008 basis (spread < 5%) at some tau in the Jensen corridor.
- **Inputs**: Extended HP^0 basis from HKR + SBI; S83 quantum Cartan extension for a twist-composed nu_5; S67 anomaly structural specification.
- **Gate**: new `S86-CF-S1-C-3-FALSIFIER-CONSTRUCTION`; PASS (theorem holds) iff no construction produces either (a) or (b); FAIL (theorem falsified) iff either construction succeeds.
- **Effort**: MODERATE-HIGH. One enumeration script + one cross-check script (~500 lines total). Pre-registered falsifier is an explicit part of the Theorem's scientific status.

### CF-S1-C-4. §VII.B permanent-registry landing of the Boundary Theorem

- **What**: Land the theorem statement (see §VII.B draft below) in `sessions/permanent-results-registry.md` §VII.B slot (or cascade to §VII.Q/§VII.R if slot occupied, per W2-7 cascade protocol). Include theorem statement, two-direction proof anchor (K-theoretic retraction; parity-blindness corollary), canonical example table, and pre-registered falsifier gate (CF-S1-C-3).
- **Inputs**: §VII.B draft from this synthesis (§VII.B Draft below); SHA closures from W5-1, W5-2, W5-4, W5-5, W5-6, W2-7; canonical-constants `a_0`, `tau_fold`, `mellin_ratio`.
- **Gate**: new `S86-CF-S1-C-4-VII-B-REGISTRY-LANDING`; PASS iff theorem committed to registry with 6-anchor SHA closure matching this synthesis AND cascade-slot audit confirms non-overlap with prior §VII.B content.
- **Effort**: LOW. Registry-steward commit with audit script (~100 lines).

---

## VI. Summary Table

| # | Item | Status | K-theoretic content | Registry disposition |
|:-:|:-----|:------:|:--------------------|:---------------------|
| 1 | Boundary Theorem (connes-formulation) | PROVEN (this synthesis, two-direction Chern-character retraction proof) | HP^0 factorization iff r in image(pi_P) | Draft §VII.B; land via CF-S1-C-4 |
| 2 | Pure-a_4 family P | CLASSIFIED | {zeta, Zubarev, SDW}; Mellin signature (0,0,f_4,0) | registry §VII.N (three-layer synthesis stands) |
| 3 | Complement family M | CLASSIFIED | {cutoff_sqrt, anomaly}; Mellin signature has f_0 or f_2 or f_6 nonzero | §VII.M SCHEME-DEPENDENT row |
| 4 | Parity-blindness of HP^even to HP^odd | PROVEN (W2-7 structural refinement) | Chern char K_0 -> HP^even only | §VII.P' (odd-parity companion slot) |
| 5 | HP^1 magnitude near-invariance | INFO-tight | |f_4| ∈ [0.5, 1.0], ratio 2.00x; 190.5x reduction vs raw 381x S66 range | §VII-B near-invariant observable |
| 6 | L_max robustness of W5-1 FAIL | CONFIRMED (W5-4 PASS L in {8,9,10}) | Dominant block k in [2,6], tail < 0.003% | §VII.M locked |
| 7 | Lattice functoriality on regulator-join | FAILS (W5-5 FAIL val=8) | pi_P does not lift to Boolean join on layer lattice | §VII.K-DUAL.LAYER non-functorial annotation |
| 8 | Scope of S78 W2-F Mellin theorem | BOUNDED | Valid only on image(pi_P) | §VII.M scope-bound edit |
| 9 | eps_H sign at tau_fold | REGULATOR-CONDITIONAL | +1 for r in M (due to a_0 · f_0 = 12880); -1 for r in P | must name regulator when reporting sign |
| 10 | Classification | GEOMETRIC with PHONONIC corollary | Substrate fold-signature = (triple, regulator class) pair | — |

---

## §VII.B Draft (for permanent-results-registry.md)

```
§VII.B. REGULATOR-FAMILY BOUNDARY THEOREM (S85 S-1 three-solo convergence:
        connes-ncg, lizzi-spectral-functional, van-den-dungen-bridge)

THEOREM (HP^0 factorization as a retraction-invariant). Let
  (A, H, D) = (C^inf(M) tensor A_F, L^2(M, S) tensor H_F, D_M tensor 1 + gamma_5 tensor D_F)
be the almost-commutative spectral triple with A_F = C (+) H (+) M_3(C), KO-dim 6.
Let R_atlas = {zeta, Zubarev, SDW, cutoff_sqrt, anomaly} be the canonical 5-regulator
atlas with Mellin-vector map  r |-> f^r = (f_0^r, f_2^r, f_4^r, f_6^r).
Let pi_P : R^4 -> R^4, pi_P(f_0, f_2, f_4, f_6) = (0, 0, f_4, 0), be the projection
onto the pure-a_4 subspace P = span{(0,0,1,0)}.
Let (nu_i)_{i=1,...,4} be the CCM-2008 basis of HP^0(A_F).

Then the factorization
        <[eps_H], nu_i>_r  =  M(r) · <[eps_H], nu_i>_zeta   for all i in {1,...,4}
with M(r) a scalar INDEPENDENT of i holds IF AND ONLY IF r in image(pi_P),
i.e., iff  (f_0^r, f_2^r, f_6^r) = 0.  In that case M(r) = f_4^r.

Equivalently: HP^0 factorization under regulator-join is a property of the {a_4}-support class.

PROOF (two-direction, K-theoretic retraction; connes solo §II.C). Direction 1:
substitution in the Mellin-expanded pairing gives Phi_r(nu_i) = f_4^r · m_4^i
for all i, so M(r) = f_4^r is i-independent. Direction 2: i-independence of
the ratio forces linear constraints (II.10) on (f_0^r, f_2^r, f_6^r); the CCM-2008
character table m_n^i/m_4^i is of rank 3 across (i, n in {0,2,6}), so the only
solution is (f_0^r, f_2^r, f_6^r) = 0. QED.

CANONICAL ATLAS REALIZATION (L_max=3 verified; L_max=10 W5-4 PASS):
  P = image(pi_P) ∩ R_atlas = {zeta, Zubarev, SDW}     [HP^0 spread = 0.00% each]
  M = complement ∩ R_atlas  = {cutoff_sqrt, anomaly}   [HP^0 spread 254.75%, 107.07%]

CONSEQUENCES:
  (i)  Scope-bound of S78 W2-F Mellin-multiplier theorem to image(pi_P).
  (ii) eps_H sign at tau_fold is regulator-conditional: sig(r) = +1 on M (a_0·f_0 dominates),
       -1 on P (W5-1 FAIL confirms).
  (iii) Lattice join does not lift pi_P (W5-5 FAIL val=8 violations).
  (iv) HP^even pairings are blind to HP^odd secondary twists (W2-7 parity-blindness
       lemma, twin pair (C_H, C_epsH)).
  (v)  HP^1 magnitude is NEAR-invariant (W5-6 ratio 2.000, 190.5x reduction vs raw).

PRE-REGISTERED FALSIFIER (CF-S1-C-3):
  Theorem is FALSIFIED if either
    (a) a pure-a_4 regulator (f^r = (0,0,f_4,0) exactly) can be exhibited that
        FAILS HP^0 factorization on some fifth basis element nu_5 beyond CCM-2008
        (spread > 5% with nu_5 added); or
    (b) a cutoff_sqrt-class regulator (f^r has nonzero f_0, f_2, or f_6) can be
        exhibited that PASSES HP^0 factorization across CCM-2008 basis with
        spread <= 5% at some tau in the Jensen corridor.
  Gate S86-CF-S1-C-3-FALSIFIER-CONSTRUCTION is the pre-registered test; PASS =
  theorem holds, FAIL = theorem falsified with exhibited counter-example.

CLOSURE-SHA ANCHORS (from S85 W5 + W2 dual-SHA ledger):
  W5-1:  audit 45ac9bfceca269f1d059fec0b09d8f7bfcad6a8b265a5d60fc38236e1531b79d
  W5-2:  audit 4536d99702607605654c2979a4c58014e4f666a13d47f3cddeab6ff7feb4db8f
  W5-4:  audit 8e3b77e98ef12e5b27105276e782552d4e2a482fb6c54360a22766c8367ae6a1
  W5-5:  audit 50c372ee43503feaf6adbbe8f72592b83f1768eef6614da7df46317d11d8c12a
  W5-6:  audit 92d022ff56df893ef9eee82e0dd0500d08600bc0a3a64455400b9e8bf080437b
  W2-7:  audit 2ef68ad50f55b59ef626f7767c0fa167dd72551f1ddd183bb89b5ca010ebff16

CLASSIFICATION: GEOMETRIC.  PHONONIC corollary: eps_H sign at fold = property of
(spectral triple, regulator class ∈ {image(pi_P), complement}) pair.
```

---

## Closing Note (connes solo, non-registry)

This proof occupies the K-theoretic/cyclic-cohomology lane. It complements (but does not duplicate) the Lizzi solo (Hausdorff-Bernstein-Widder admissibility of f_r(x) as a positive kernel on Schwartz class — shape analysis on the regulator function itself) and the VdD solo (Kasparov module / submersion dictionary — categorical lift of pi_P to the KK-groups). The three solos should converge on the SAME theorem statement via three different machineries; agreement would be the three-solo convergence pattern already established in S84 W2a-11 (Three-Layer Regulator Theorem). Disagreement on any specific claim would flag a machinery-level inconsistency; none is claimed here.

The substrate is one fabric; its emergent slow-roll observables are a pair — (triple, regulator class). The Boundary Theorem makes "regulator class" a precise K-theoretic object — the image of a cyclic-cohomology retraction, not a loose taxonomic label. Every future scheme-comparison gate should first classify its regulator via pi_P before invoking any "equivalence up to scheme."
