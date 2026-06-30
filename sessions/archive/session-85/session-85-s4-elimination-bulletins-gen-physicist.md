# Session 85 Synthesis: S-4 Structural-Elimination Bulletins (gen-physicist)

**Date**: 2026-04-25
**Agent**: gen-physicist (cross-domain workhorse)
**Source Documents**:
- `sessions/archive/session-85/session-85-w0-workingpaper.md` (§W0-7 Zubarev L_max convergence)
- `sessions/archive/session-85/session-85-w2-workingpaper.md` (§W2-7 Disjoint-corridor registry landing)
- `sessions/archive/session-85/session-85-w3-workingpaper.md` (§W3-7 Branch-A A_s closure)
- `sessions/archive/session-85/session-85-w5-workingpaper.md` (§W5-1 FI-parity registry, §W5-4 L_max sanity, §W5-6 HP^1 magnitude)
- `.claude/agent-memory/gen-physicist/MEMORY.md`

**Scope**: Four W0–W5 FAIL verdicts re-read as structural-elimination bulletins per `.claude/rules/epistemic-discipline.md`. Each bulletin enumerates: the closed hypothesis as an explicit FALSE statement; the surviving mechanisms that now bear the load; evidence class (ALGEBRAIC / METHODOLOGICAL / TRUNCATION); and the dimensionality reduction of the constraint-map solution space.

**Knowledge-base check (before writing)**: `mcp__knowledge__search_knowledge` queried for "Jensen Zubarev identity", "Branch-A A_s closure K_substrate 2.035", "HP^1 parity wall epsilon_H", "disjoint corridor theorem Seeley-DeWitt", "eta invariant odd parity GV integral", "f_conv F_amp c_sub TD-path corrections", "A_s 30 percent band Planck strict factor 2". All four FAIL gates have downstream artefacts in the project knowledge index; none of the supposed identities being closed here have prior PROVEN status — they were conjectures or proposed registry landings, not theorems. The Zubarev identity in the index refers to the S46 thermodynamic identity `E_k n_k = T_k S_FD_k + Omega_k` (which is exact and unrelated), NOT to the ρ→−1 limit conjecture being refuted by W0-7.

---

## I. Session Outcome

The W0–W5 sweep produced four FAIL verdicts whose joint structural reading is: **two proposed permanent-registry landings (FI-parity wall §VII-B and disjoint-corridor §VII.P) and two zero-free-parameter closure conjectures (Jensen-Zubarev ρ=−1, Branch-A A_s within 30%) are eliminated under the pre-registered bands**. None of the four FAILs is an agent error; each is a constraint-map advance whose downstream effect is to narrow the surviving solution space to a smaller, more sharply-specified region. The single most consequential FAIL is W3-7 (Branch-A A_s = 3.30e−9, 57% above Planck) under the strict 30% reading; under the lenient (S80 factor-2) reading it remains a PASS-F2. The synthesis's main load-bearing observation is that **two of the four FAILs (W2-7, W5-1) simultaneously hardened the underlying substrate property they tested while invalidating the proposed registry landing** — i.e. these are FAIL-with-refinement verdicts, not refutations.

---

## II. Key Results

### II.A. FAIL #1 — W5-1 FI-Parity Registry (ε_H J-parity wall demoted)

**Result**: `S85-W5-1-FI-PARITY-REGISTRY: FAIL value=False`. sig(ε_H, cutoff_sqrt) = +1; sig(ε_H, {zeta, Zubarev, SDW, anomaly}) = −1 at τ_fold under KO-dim=6 J-canonical convention. **Classification: GEOMETRIC**.

**The closed hypothesis (NOW FALSE, written as an explicit statement)**:
> "ε_H J-parity under the KO-dim=6 real structure is a regulator-INDEPENDENT invariant suitable for permanent §VII-B wall registration. All five regulators in the canonical 5-atlas (zeta, Zubarev, SDW, cutoff_sqrt, anomaly) agree on sign(ε_H) at τ_fold."

This statement is empirically refuted. The cutoff_sqrt regulator (full heat-kernel, a_0-inclusive) sits in a different sign-class from the four a_4-dominant regulators. The §W5-1 INFO clause (single outlier = anomaly per S67 FUNCTIONAL-SELECT-67 structural exclusion) does NOT fire because the outlier is cutoff_sqrt, not anomaly.

**Surviving mechanism that carries the load**: §W5-6 `‖ε_H‖_{HP^1}` magnitude near-invariance (verdict INFO-tight, 2× regulator band, 190.5× reduction from S66/S75 raw 381× range). The HP^1 cohomological projection of ε_H is the actual regulator-invariant observable; what fails is sign-invariance, what survives is magnitude-invariance up to a factor of 2. The §VII-B candidate slot for "ε_H wall" is replaced by the §VII.M entry "ε_H J-parity is permanently SCHEME-DEPENDENT" plus a §VII-B near-invariant entry "‖[ε_H]‖_{HP^1} regulator-band ≤ 2×".

**Evidence class**: **METHODOLOGICAL** — the wall hypothesis was about regulator-class invariance of a sign observable, not about an algebraic identity inside one fixed regulator. The W5-4 L_max sanity PASS (sign matrix L-invariant across L ∈ {8,9,10}) certifies the FAIL is NOT a TRUNCATION artifact and removes the `L_max → ∞` rescue interpretation. So the elimination is methodological-with-truncation-clearance: regulator-family choice is a permanent physical degree of freedom for ε_H sign, not a renormalization scheme freedom that would dissolve at L_max → ∞.

**Constraint-map dimensionality reduction**: −1. The proposed §VII-B "ε_H sign wall" entry is removed from the candidate-walls set; the surviving walls set shrinks by one. Concurrently, the §VII.M observable list grows by one entry (SCHEME-DEPENDENT ε_H sign with cutoff_sqrt outlier) and §VII-B grows by one near-invariant entry (HP^1 magnitude). The NET change to permanent-registry slots is unchanged: one permanent-wall candidate eliminated, one near-invariant entry added. The framework's permanent-wall ledger does NOT advance via this gate; it stops short of advancing.

**Pre-registered NEXT-elimination gate**: If `‖[ε_H]‖_{HP^1}` later drops below the 2× band under any regulator extension (e.g. additional regulators added to the atlas), the surviving §VII-B near-invariant entry collapses too, and ε_H is downgraded to "no regulator-invariant content" — which would close the entire ε_H-class observable family. The next gate to test is §W5-6-EXTENDED with regulator-atlas size ≥ 7 (add Wodzicki-residue and ζ_KS regulators) at the same factor-2 INFO threshold; PASS at ≥7 atlas would harden HP^1 near-invariance to a permanent-wall claim, FAIL would close the ε_H observable family entirely.

### II.B. FAIL #2 — W2-7 Disjoint-Corridor Registry Landing (§VII.P landing blocked)

**Result**: `S85-W2-DISJOINT-CORRIDOR-REGISTRY-LANDING: FAIL value=1` (one counter-example across 21 pairs). The pair (C_H, C_epsH) shares (a_0, a_2, a_4) = (2, −0.0417, 0.0625) at max_rel_diff = 0.0e+00. **Classification: META** (counter-construction audit; structurally GEOMETRIC).

**The closed hypothesis (NOW FALSE)**:
> "§VII.P pairwise HP²-disjoint corridors produce DISTINCT even-parity Seeley-DeWitt signatures (a_0, a_2, a_4). Equivalently: HP^2(C_a ∩ C_b) = 0 implies (a_0(C_a), a_2(C_a), a_4(C_a)) ≠ (a_0(C_b), a_2(C_b), a_4(C_b))."

Substitution chain (lifted from W2-7):

```
Step 1 [definitions]:
  C_H     = corridor with factor support {H} (rank-1 idempotent in ℍ-factor)
  C_epsH  = corridor with factor support {H} carrying secondary HP^1 ε_H twist
  HP^k    = periodic cyclic cohomology of A_F, degree k mod 2
  a_n(C)  = nth Seeley-DeWitt coefficient of D_K restricted to corridor C

Step 2 [substitute]:
  HP^2(C_H ∩ C_epsH) = 0    [disjoint by hypothesis — both rank-1 idempotents]
  but factor support is identical, and a_n is a function of the EVEN-graded
  spectral content (a_2k via Tr(D^{-2s}) at s = -k);
  the difference between C_H and C_epsH is an HP^1 (ODD) twist invisible to
  even-parity moments.

Step 3 [simplify]:
  (a_0, a_2, a_4)(C_H) = (a_0, a_2, a_4)(C_epsH) = (2, -0.0417, 0.0625) exactly.

Step 4 [direction]:
  Disjointness in HP^2 (even cohomology) + identical factor support
  ⇒ identical even Seeley-DeWitt signature.
  The hypothesis fails by ALGEBRAIC obstruction: parity grading of HP^*
  vs parity grading of Seeley-DeWitt.
```

**Surviving mechanism that carries the load**: the **parity-blindness theorem** (W2-7 promotes this from observation to permanent structural constraint). Even-parity spectral moments cannot decode HP^1 secondary twists. Distinguishing (C_H, C_epsH)-type twin pairs requires odd-parity diagnostics: the η-invariant or the Godbillon-Vey integral (S83 G56 GODBILLON-VEY-HEITSCH; the GV class lives in H^3 = HP^odd via the odd-degree Connes-Moscovici residue).

The §VII.P landing decomposes into two refined slots:
- **§VII.P-v2** (HP^0-content-distinct corridors only, 20/21 pairs): even Seeley-DeWitt distinguishes pairs whose factor support differs (different dim_C contribution to a_0). This is a strictly weaker but provably correct theorem.
- **§VII.P′** (parity-extended, the remaining 1/21 pair): pair-distinguishability via odd-parity probe (η-invariant or GV integral) for HP^0-content-IDENTICAL pairs differing only by HP^1 secondary twist.

**Evidence class**: **ALGEBRAIC**. The obstruction is intrinsic to the cohomological grading: HP^* on a finite-dim semisimple A_F has HP^odd carrying the secondary twists that even Seeley-DeWitt residues cannot see. This is theorem-grade: no truncation, regulator, or convention choice can rescue the original §VII.P hypothesis as written.

**Constraint-map dimensionality reduction**: −1 in the candidate-theorems set, +2 in the refined-theorems set (§VII.P-v2 + §VII.P′). The NET change is +1 to the permanent-registry landing queue, with stronger structural content than the original §VII.P would have provided. The W2-3 (HP^3 three-way PASS, 0 obstructions on 35 triples) and W2-6 (q-deformed PASS, 4-route confluence) results are independent of this FAIL: three-way separability and quantum-deformation rigidity both extend §VII.P, not §VII.P-v2, but their proofs rely on factor-support discrimination, not HP^1 twist discrimination, so they survive the refinement intact.

**Pre-registered NEXT-elimination gate**: §VII.P′ requires explicit computation of η(C_H) vs η(C_epsH). Pre-register at: `|η(C_H) − η(C_epsH)| / max(|η(C_H)|, |η(C_epsH)|, ε_machine)` with PASS ≥ 1.0 (well-separated mod ℤ); INFO ∈ [1/2, 1.0); FAIL < 1/2. If η is also parity-blind to the ε_H twist (which would require ε_H to lie in a kernel of the η character), then the ENTIRE corridor-disjointness program collapses and (C_H, C_epsH) become spectrally indistinguishable by any regulator-class diagnostic — at which point §VII.P-v2 and §VII.P′ both close and §VII.P is permanently retired.

### II.C. FAIL #3 — W3-7 Branch-A A_s Closure (the most consequential of the four)

**Result**: `S85-W3-CF-1-BRANCH-A-A_S-CLOSURE-K2035: FAIL value=3.2994e−09`. A_s_framework / A_s_Planck = 1.5712; |relerr| = 57.1%, exceeding W3 strict 30% FAIL band. **Classification: PHONONIC**.

**The closed hypothesis (NOW FALSE under the strict 30% reading)**:
> "K_substrate = 2.035 Branch-A TD path is the sole surviving A_s pathway that reproduces Planck 2018 central A_s = 2.10e−9 within 30% under the 5-regulator atlas. Specifically: A_s_framework(K=2.035; F_amp=1.0166, c_sub=2.238, f_conv=9.3e−4) lies inside the strict 30% band around 2.10e−9."

Substitution chain:

```
Step 1 [definitions]:
  A_s^{UNIFIED} = A_s_bare · F_amp · c_sub^{-1} · f_conv     [S80 UNIFIED-AS-79 form]
  A_s_bare      = H_tilde^2 / (8 π^2 ε_H)                   [Mukhanov-Sasaki bare]
  Planck central = 2.10 × 10^{-9}
  strict band   = |A_s − A_s_Planck| / A_s_Planck ≤ 0.30 (FAIL threshold)

Step 2 [substitute the S80 cache values]:
  F_amp_canonical    = 1.0166
  c_sub              = 2.2380
  f_conv             = 9.3000e-4
  → A_s_framework    = 3.2994 × 10^{-9}

Step 3 [simplify]:
  |3.2994e-9 − 2.10e-9| / 2.10e-9 = 1.1994e-9 / 2.10e-9 = 0.5712

Step 4 [direction]:
  0.5712 > 0.30 strict FAIL band ⇒ FAIL.
  But: 0.5712 < log10(2)/log10(e) ⇒ |Δ_OOM| = log10(3.2994/2.10) = +0.196 < 0.301 (factor-2 PASS-F2 band, S80 pre-registration).
  The verdict is band-dependent: STRICT-30% FAIL, FACTOR-2 PASS.
```

**The 30%-vs-factor-2 conflict is unresolved across waves**. W3-7 was pre-registered with a stricter band than S80; both are pre-registered numbers computed against pre-registered thresholds; neither is post-hoc. Under `.claude/rules/epistemic-discipline.md` source-authority hierarchy, both gates are valid; the elimination semantics depend on which band is authoritative going forward. The W-2 workshop carry-forward (per the focus brief) is the appropriate venue to resolve the band-authority question.

**Surviving mechanisms (three branches, mutually exclusive)**:

1. **Lenient branch** (S80 factor-2 band is authoritative): Branch-A K=2.035 remains the surviving A_s pathway with a PASS-F2 verdict. The "57% above Planck" relerr is inside the factor-2 band (|Δ_OOM| = 0.196 < 0.301). Strong observational support under zero-free-parameter prediction (BF ~ 1000 per `feedback_reporting-framing.md`). The closed corridor is empty; no mechanism is eliminated.

2. **Strict branch** (W3-7 30% band is authoritative): Branch-A is closed. Surviving paths require either:
   - **Re-opening S70-S77 closed A_s mechanisms** (the 25-mechanism closure ledger gets de-incremented if any of those closures was conditional on the strict band failing them by less than 57%);
   - OR a NEW path from substrate first principles that does not pass through the S80 TD multiplicative chain.

3. **Diagnostic-trace branch** (the 57% is attributable to one specific factor mis-pinning): trace which of (f_conv = 9.3e−4, F_amp = 1.0166, c_sub = 2.238) carries the surplus. The bare Mukhanov gives ~ 2.04 × 10^{-5}; the S80 cache gives 3.30 × 10^{-9}; the ratio is 6193. Some combination of the three multiplicative factors produces this 6193 suppression. If one factor is mis-pinned by ~ 36% (the residual surplus relative to Planck), the strict reading is rescued without dissolving any of S80's structure.

**Evidence class**: **METHODOLOGICAL** at the band-selection level (which pre-registered band is authoritative is a methodology question, not an algebraic one), with a **TRUNCATION** subsidiary in the diagnostic-trace branch (the f_conv computation involves 2-loop Z_R cluster-sum convergence that is L_max-sensitive — see W3-1 and W3-3).

**Constraint-map dimensionality reduction**:
- Under strict reading: **−1 in the surviving A_s pathways**, with the count of "viable A_s mechanisms" dropping to zero unless one of the three rescue branches above succeeds. This is the FAIL with the largest solution-space-dimensionality consequence in the W0–W5 sweep.
- Under lenient reading: **0** (the surviving pathway is unchanged; the only update is that a finer-grained pre-registration was attempted and not satisfied — informative but not eliminating).

**Pre-registered NEXT-elimination gate**: a band-authority audit gate, pre-registered as: `S86-AS-BAND-AUDIT: PASS iff a single canonical band is selected for A_s gates with substantive justification + pre-registered tolerance; INFO iff both bands are retained as parallel reads with documented carry-forward per band; FAIL iff iterate-until-PASS pattern detected (S78 Class 6) where band is widened post-hoc to recover PASS`. Concurrent with the audit, a TD-path corrections trace gate `S86-AS-TD-PATH-TRACE` enumerates the contribution of each of (f_conv, F_amp, c_sub) to the 6193 ratio; PASS iff one factor isolates ≥ 50% of the relerr surplus; INFO iff a uniform attribution across factors; FAIL iff none of the three explain ≥ 30% of the surplus (which would force re-derivation from substrate first principles).

### II.D. FAIL #4 — W0-7 Zubarev L_max Convergence to −1 (conjecture refuted under tested kernel)

**Result**: `S85-ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE: FAIL value=-6.348854e-01`. Fit-intercept c_0 = −0.8104 (R² = 0.99995); constrained fit forcing c_0 = −1 gives R² = 0.9305 (much worse). Direction-of-motion: monotone decreasing in L_max ∈ {8..12} with |Δρ| also decreasing. **Classification: GEOMETRIC**.

**The closed hypothesis (NOW REFUTED NUMERICALLY under the tested kernel normalization)**:
> "ρ_Zubarev(L_max → ∞) = −1 exactly (Jensen-Zubarev identity conjecture). The Zubarev Mellin-cone moment of D_K, weighted under the canonical Connes-Moscovici-1995 kernel, converges to the simple rational −1 in the L_max → ∞ limit, with residual 1/L² + 1/L⁴ decay."

Three surviving interpretations (mutually exclusive at the structural level):

1. **The conjecture is numerically wrong**. If the fit model is correct, the true asymptote is c_0 ≈ −0.81. The Zubarev ρ-limit is then an irrational or framework-constant-dependent number, not the simple rational −1. This would close the conjecture as written and re-open the question "what IS the Zubarev limit?" as a substrate-intrinsic computation.

2. **Higher-order 1/L⁶ or log(L) terms matter**. The fit ρ(L) = c_0 + α/L² + β/L⁴ truncates after 1/L⁴. With 5 data points and 3 fit parameters, adding 1/L⁶ would overfit. Successor: extend L_max ∈ {13, 14} for a 6–7 point sweep; the 1/L⁶ term is justified iff the 6-point R² still favors c_0 = −1.

3. **Kernel normalization differs from the conjecture's canonical form**. The −1 target is conjectured under a specific Connes-Moscovici-1995 §4 kernel; the S85 script may use a different normalization (Zubarev-1974 raw vs CM-1995-normalized). Successor: kernel-normalization audit comparing the script's Mellin kernel to the conjecture's canonical form.

**Surviving mechanism that carries the load**: NONE of the three interpretations is yet selected. The conjecture is in INFO-with-three-branches-open status; W2 connes-ncg-theorist carry-forwards must NOT cite the Jensen-Zubarev identity as theorem-grade pending resolution. Downstream gate W0-20 MELLIN-CONE-S3-RESIDUE shares the same D_K eigenvalue caches and is therefore exposed to interpretation (3) — kernel-normalization audit applies there too.

**Evidence class**: **TRUNCATION** at the surface level (L_max ∈ {8..12} sweep is finite; the asymptote is extracted by fit); **METHODOLOGICAL** at the structural level (the kernel-normalization choice is a convention decision that the canonical form must specify before the gate can be re-run). **NOT ALGEBRAIC**: the FAIL does not establish an algebraic obstruction to the conjecture; it shows the conjecture's literal formulation is not satisfied at the L=12 truncation under the chosen kernel normalization. Under interpretation (1), this is upgraded to ALGEBRAIC (the conjecture's literal closed form is wrong, and the Zubarev limit is then determined by the substrate's own spectral content, not by an external rational target).

**Constraint-map dimensionality reduction**: −1 in the conjecture set (Jensen-Zubarev identity is removed from the "presumed-PROVEN" candidate list) and +1 in the open-question set ("what is ρ_Zubarev(∞)?" enters the open-questions ledger as a substrate-intrinsic computation). NET on permanent-registry: 0 (no permanent slot was claimed; only a candidate identity was floated). The downstream effect on W2 is structural: any W2 carry-forward citing this identity as theorem-grade must be amended to cite it as conjecture-with-numerical-FAIL.

**Pre-registered NEXT-elimination gate**: `S86-W0-7-EXTENDED: extend L_max ∈ {13, 14}, refit with 1/L⁶ term added, AND audit kernel normalization against CM-1995 §4 canonical form. PASS iff (a) extended fit with 1/L⁶ recovers c_0 ∈ [−1.01, −0.99], OR (b) kernel-normalization fix shifts the L=12 anchor by ≥ 0.18 toward −1. INFO iff the extended fit recovers c_0 ∈ [−1.05, −0.95] (factor-of-2 in deviation). FAIL iff neither (a) nor (b) succeeds, which would establish interpretation (1) — the conjecture is numerically refuted at theorem-grade, not just truncation-grade.`

---

## III. Gate Verdicts (FAIL bulletins covered)

| Gate | Verdict | Decisive Number | Wave | Evidence Class |
|:-----|:--------|:----------------|:-----|:---------------|
| S85-W5-1-FI-PARITY-REGISTRY | FAIL | sig(cutoff_sqrt)=+1 vs sig(others)=−1 | W5 | METHODOLOGICAL |
| S85-W2-7-DISJOINT-CORRIDOR-REGISTRY-LANDING | FAIL-with-refinement | num_counter_examples=1 (C_H, C_epsH) max_rel_diff=0 | W2 | ALGEBRAIC |
| S85-W3-CF-1-BRANCH-A-A_S-CLOSURE-K2035 | FAIL (strict reading) | A_s = 3.2994e−9; |relerr|=57.1% > 30% band | W3 | METHODOLOGICAL (band) + TRUNCATION (TD-path) |
| S85-ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE | FAIL | c_0 = −0.8104 (vs target −1.0); deviation 0.1896 | W0 | TRUNCATION (surface) → METHODOLOGICAL → ALGEBRAIC under interp (1) |
| (cross-ref) S85-W5-4-PARITY-LMAX-SANITY | PASS | column_constant=True; matches §W5-1 anchor | W5 | TRUNCATION (clearance) |
| (cross-ref) S85-W5-6-HP1-MAGNITUDE | INFO-tight | max/min = 2.000; 190.5× reduction | W5 | structural surviving mechanism |

---

## IV. Structural Implications

**The four FAILs are NOT four independent eliminations.** They cluster into two structural pairs:

**Pair 1 (W5-1 + W2-7): registry-landing FAILs that hardened the underlying substrate property they tested.** Both gates proposed a permanent-registry landing for an observable that was true at lower resolution (regulator-invariant magnitude in the W5-1 case; HP^0-content-distinct corridor pairs in the W2-7 case) but failed to extend to the strict statement (sign-invariance for W5-1; ALL pairs for W2-7). The structural lesson is that the substrate's regulator-class boundary (W5-1) and its parity-grading boundary (W2-7) are physical degrees of freedom, not artefacts to be eliminated. Both FAILs are FAIL-with-refinement: the substrate property is hardened, the proposed landing is blocked pending a refined statement.

**Pair 2 (W3-7 + W0-7): closed-form-conjecture FAILs that depend on convention choice.** Both gates attempted to certify a specific closed-form numerical target — Planck A_s within 30% (W3-7); Jensen-Zubarev ρ = −1 (W0-7) — and both refute the strict form while leaving open a convention-choice rescue path (band-authority for W3-7; kernel-normalization for W0-7). Neither is an algebraic obstruction at the surface level; both can be promoted to algebraic obstruction only after the convention audit is closed.

**Constraint-map summary update**:

| Item | Prior state | Post-W0-W5 state | Net dimensionality change |
|:-----|:------------|:-----------------|:--------------------------|
| §VII-B candidate "ε_H sign wall" | candidate | **CLOSED** (replaced by §VII.M scheme-dependent observable + §VII-B HP^1 magnitude near-invariant) | −1 wall, +2 §VII.M / §VII-B-near-inv slots, NET +1 |
| §VII.P landing | proposed | **BLOCKED**; refined to §VII.P-v2 (HP^0-distinct) + §VII.P′ (parity-extended, GV-required) | −1 candidate, +2 refined slots, NET +1 |
| Branch-A A_s pathway | candidate (S80 PASS-F2) | **CLOSED** under strict 30% reading; surviving under lenient factor-2 reading | −1 (strict) or 0 (lenient); band audit pending |
| Jensen-Zubarev ρ=−1 identity | conjectured | **NUMERICALLY REFUTED** under tested kernel; three rescue interpretations open | −1 conjecture, +1 open question, NET 0 on permanent registry |
| Parity-blindness theorem (even SD vs HP^1) | implicit | **PROMOTED** to permanent structural constraint | +1 wall (NEW) |

The framework's permanent-walls ledger advances by **+1 net wall** (the parity-blindness theorem is promoted via the W2-7 FAIL-with-refinement) and reorganizes one ε_H slot. The candidate-closure ledger loses two conjectures (Jensen-Zubarev identity and Branch-A within-30% under strict reading); these are open-status, not eliminated-status, until the convention audits close.

**Substrate-framing lock-check** (per `.claude/rules/phononic-framing.md`): all four FAILs flow from `D_K eigenvalues → spectral action moments → substrate observable → pre-registered threshold`. None of the four invokes a GR-as-container framing. The W3-7 phrasing "inflationary anchor" is read substrate-first as "the τ_fold slice of the Jensen flow at K_substrate=2.035 produces a power-spectrum amplitude observable through the post-fold acoustic emission". The W0-7 Zubarev kernel is a Mellin-cone moment of D_K, not a thermal partition function. The W5-1 sign-flip is a regulator-family boundary in the spectral-functional space, not a temperature-dependent convention shift.

---

## V. Carry-Forward Computations

V.1. **§W5-1 / §W5-6 regulator-extension audit**
   - **What**: extend the canonical 5-regulator atlas to ≥ 7 regulators (add Wodzicki-residue and ζ_KS regulators per S77 framework regulator catalogue) and re-run §W5-6 HP^1 magnitude scan + §W5-1 sign scan. Compute max/min ratio of `‖[ε_H]‖_{HP^1, r}` across the extended atlas; tabulate sign(ε_H) per regulator at τ_fold.
   - **Inputs**: S85 W5-6 npz cache; S85 W5-1 cache; canonical_constants `tau_fold`, `M_KK`, `L_max=10`; D_K eigenvalue cache from `s85_w0_zubarev_lmax_convergence_to_minus_one.npz` (shared eigenvalues at L=10); Wodzicki + ζ_KS kernel definitions per Connes-Moscovici-1995 §4 + Kontsevich-Vishik-1995.
   - **Gate**: NEW gate `S86-EPSILON-H-EXTENDED-ATLAS-7-REGULATORS`. PASS iff (max/min) ≤ 2.0 across 7-atlas AND sign(ε_H, cutoff_sqrt) remains the unique outlier. INFO iff max/min ∈ (2.0, 4.0]. FAIL iff max/min > 4.0 (HP^1 near-invariance collapses; ε_H observable family closes entirely).
   - **Effort**: 2-3 hours, 1 agent session (gen-physicist or lizzi).

V.2. **§W2-7 odd-parity GV / η-invariant probe for (C_H, C_epsH) twin pair**
   - **What**: compute η-invariant η(C_H) and η(C_epsH) using the Connes-Moscovici-1995 odd-parity residue formula (Atiyah-Patodi-Singer setup); compute the Godbillon-Vey integral GV(C_H) and GV(C_epsH) from S83 G56 GODBILLON-VEY-HEITSCH machinery. Tabulate `|η(C_H) − η(C_epsH)|` and `|GV(C_H) − GV(C_epsH)|`.
   - **Inputs**: S85 W2-7 npz (corridor structure + Seeley-DeWitt cache); S83 G56 GV-Heitsch cache; D_K spectrum at L_max = 10; ε_H twist data from S66/S75; canonical_constants `tau_fold`.
   - **Gate**: NEW gate `S86-W2-VII-P-PRIME-PARITY-PROBE`. PASS iff `|η(C_H) − η(C_epsH)| / max(|η|, ε_machine) ≥ 1.0` (well-separated mod ℤ) OR `|GV(C_H) − GV(C_epsH)| / max(|GV|, ε_machine) ≥ 1.0`. INFO iff [0.5, 1.0). FAIL iff < 0.5 (η AND GV are also parity-blind to ε_H twist; §VII.P entire program closes).
   - **Effort**: 4-6 hours, 1 agent session (connes-ncg-theorist).

V.3. **W3-7 band-authority audit + TD-path corrections trace**
   - **What**: (a) band-authority audit — enumerate every A_s gate in the S70-S85 ledger with its pre-registered band; produce a ledger of (gate, band, verdict-under-band) and select a single canonical band with substantive justification (S80 factor-2 framework-internal vs Planck strict 30% observational). (b) Decompose A_s_framework = 6193 × A_s_bare into multiplicative contributions from f_conv = 9.3e−4, F_amp = 1.0166, c_sub^{-1} = 0.4467 with explicit dimensional consistency check; compute the relative-error surplus contribution per factor.
   - **Inputs**: S80 UNIFIED-AS-79 npz (`s80_unified_as_79_full.npz`); S82 W2-1 replay npz; S85 W3-7 npz; canonical_constants `A_s_CMB_obs`, `H_tilde_canonical`, `eps_H`, `F_amp`, `c_sub`, `f_conv`; A_s gate ledger from `computations/s*_gate_verdicts.txt` (S70-S85).
   - **Gate**: NEW gate `S86-AS-BAND-AUDIT-AND-TD-PATH-TRACE`. PASS iff a single canonical band is selected (with substantive justification, NOT iterate-until-PASS) AND one of {f_conv, F_amp, c_sub} isolates ≥ 50% of the 57% surplus. INFO iff band selected but no factor isolates ≥ 30%. FAIL iff convention-shopping (S78 Class 1) detected during band selection.
   - **Effort**: 4-6 hours, 2 agent sessions (mack-cosmic-bridge for band authority, landau or feynman for TD-path trace).

V.4. **W0-7 extended L_max sweep + kernel-normalization audit**
   - **What**: extend the ρ_Zubarev(L) sweep to L_max ∈ {13, 14} (sweep total = 7 points, L ∈ {8..14}); refit with the 4-parameter form ρ(L) = c_0 + α/L² + β/L⁴ + γ/L⁶ (justified at 7 points); separately, compare the script's kernel normalization against Connes-Moscovici-1995 §4 canonical form (audit the Mellin-cone weight function and the regulator prefactor).
   - **Inputs**: D_K eigenvalue cache extended to L_max=14 (compute via `phonon-exflation-sim/.venv312/Scripts/python.exe` with `torch.linalg.eigvals` on ROCm GPU; matrix dim ~ 250,000+ at L=14); CM-1995 §4 canonical kernel reference; W0-7 script `s85_w0_zubarev_lmax_convergence_to_minus_one.py`.
   - **Gate**: NEW gate `S86-W0-7-EXTENDED-LMAX-AND-KERNEL-AUDIT`. PASS iff (a) extended fit with 1/L⁶ recovers c_0 ∈ [−1.01, −0.99] AND R² ≥ 0.999 (the 1/L⁶ term is the resolution); OR (b) kernel-normalization fix shifts the L=12 anchor by ≥ 0.18 toward −1 (the convention is the resolution). INFO iff extended fit gives c_0 ∈ [−1.05, −0.95] (within factor-2 of target). FAIL iff neither (a) nor (b) succeeds — Jensen-Zubarev identity is permanently refuted; ρ_Zubarev(∞) is then a substrate-intrinsic irrational to be computed, not assumed.
   - **Effort**: 6-8 hours (eigenvalue computation at L=14 is ~ 5-OOM heavier than L=12; needs GPU; +1 hour for kernel audit), 1 agent session (gen-physicist).

V.5. **Parity-blindness theorem permanent-registry landing**
   - **What**: write the permanent-registry §VII-X entry for the parity-blindness theorem promoted by W2-7. The statement: "Even-parity Seeley-DeWitt moments (a_0, a_2, a_4) are blind to HP^1 secondary twists; pair-distinguishability of (C_a, C_b) with shared HP^0 factor support requires odd-parity diagnostics (η-invariant or GV integral) for HP^1-distinguished pairs." Pin proof anchors: HP^* parity grading, Connes-Moscovici-1995 odd-residue formula, S83 G56 GV-Heitsch.
   - **Inputs**: S85 W2-7 npz; S83 G56 cache; permanent-results-registry skeleton (note from W3-10 INFO: this file does not yet exist; carry-forward V.6 below creates it).
   - **Gate**: NEW gate `S86-W2-PARITY-BLINDNESS-LANDING`. PASS iff entry committed to `sessions/framework/permanent-results-registry.md` AND knowledge.db sync via `/weave --update`. INFO iff entry drafted but registry file still pending. FAIL iff entry conflicts with an existing registry slot.
   - **Effort**: 2-3 hours, 1 agent session (connes-ncg-theorist).

V.6. **Permanent-results-registry skeleton + first-row landings**
   - **What**: create `sessions/framework/permanent-results-registry.md` with the standard registry-template structure; populate first three rows: (a) Landau structural block (from W3-8 INFO); (b) BDI AZ class (from W3-10 INFO); (c) parity-blindness theorem (from V.5 above). Run `/weave --update` post-creation.
   - **Inputs**: `sessions/framework/_registry-template.md`; W3-8 npz; W3-10 npz; W2-7 npz; V.5 above.
   - **Gate**: NEW gate `S86-PERMANENT-REGISTRY-SKELETON`. PASS iff file created with ≥ 3 rows AND `/weave --update` runs cleanly AND knowledge.db indexes the new entries. INFO iff file created but `/weave --update` flags inconsistencies. FAIL iff file creation conflicts with existing registry references in CLAUDE.md or other framework docs.
   - **Effort**: 2-3 hours, 1 agent session (orchestrator + gen-physicist).

V.7. **Cross-FAIL audit: convention-choice frequency in W0-W5**
   - **What**: tabulate every W0-W5 gate where the verdict depends on a convention/normalization choice (band, kernel, regulator, scheme). Test for the S78 convention-shopping pattern: are any conventions changed between gate pre-registration and gate computation? Output a structured ledger with columns (gate, convention, pre-registered, computed-under, drift-status).
   - **Inputs**: all S85 W0-W5 plan files; all S85 W0-W5 working papers; all S85 verdict file lines.
   - **Gate**: NEW gate `S86-S85-CONVENTION-SHOP-AUDIT`. PASS iff zero convention drifts detected across W0-W5. INFO iff drifts detected but pre-registered with INFO-clauses. FAIL iff any S78 Class-1 convention-shopping pattern is found post-hoc.
   - **Effort**: 3-4 hours, 1 agent session (any audit-class agent).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | W5-1 ε_H sign wall: regulator-class FAIL | GEOMETRIC | FAIL (METHODOLOGICAL); §VII-B candidate eliminated | sign(ε_H) is permanent SCHEME-DEPENDENT (§VII.M); HP^1 magnitude near-invariant survives at 2× band (§VII-B-near-inv) |
| 2 | W5-4 L_max sanity: §W5-1 FAIL is truncation-robust | GEOMETRIC | PASS (TRUNCATION clearance) | §W5-1 FAIL cannot be rescued by L_max → ∞; demotion is permanent |
| 3 | W5-6 HP^1 magnitude near-invariance | GEOMETRIC | INFO-tight (2× band, 190.5× reduction) | The actual ε_H regulator-invariant observable; replaces the proposed sign wall |
| 4 | W2-7 §VII.P landing: (C_H, C_epsH) twin pair | GEOMETRIC (META audit) | FAIL-with-refinement (ALGEBRAIC); landing BLOCKED | Parity-blindness theorem PROMOTED to permanent wall; §VII.P refines to v2 + ′ (η/GV required) |
| 5 | W3-7 Branch-A A_s closure at K=2.035 | PHONONIC | FAIL strict / PASS-F2 lenient (METHODOLOGICAL band-authority + TRUNCATION TD-path) | Most consequential FAIL of W0-W5; if 30% band authoritative, closes the framework's current A_s pathway entirely |
| 6 | W0-7 Jensen-Zubarev ρ → −1 conjecture | GEOMETRIC | FAIL (TRUNCATION → METHODOLOGICAL → ALGEBRAIC under interpretation (1)) | Conjecture removed from theorem-grade citations in W2 carry-forwards; three rescue branches open pending L_max=14 + kernel audit |

---

## Closing Note (gen-physicist, 2026-04-25)

The W0–W5 sweep produced four FAILs whose joint structural reading is sharper than any one of them taken individually. Two FAILs (W5-1, W2-7) are FAIL-with-refinement: they hardened the underlying substrate property (regulator-class boundary; parity-grading of HP^*) while invalidating the proposed permanent-registry landing. The substrate gains a new wall (parity-blindness of even Seeley-DeWitt to HP^1 twists) and reorganizes one ε_H slot. Two FAILs (W3-7, W0-7) are convention-dependent: both refute a strict closed-form target (Planck within 30%; Jensen-Zubarev = −1 exact), but both leave open a convention-audit rescue path (band-authority for W3-7; kernel-normalization for W0-7). Until those audits close, neither FAIL is upgraded from METHODOLOGICAL/TRUNCATION to ALGEBRAIC.

The most consequential FAIL is W3-7. If the strict 30% band is authoritative going forward, the framework's surviving A_s pathway is closed and the surviving-mechanisms list for the inflationary anchor must be extended with a new path (re-opened S70-S77 mechanism or substrate-first re-derivation). If the lenient factor-2 band is authoritative, W3-7 is informationally a tightening attempt that did not succeed, but does not eliminate. The W-2 workshop carry-forward is the appropriate venue to resolve the band-authority question; until then both readings are explicitly retained.

The FAILs are well-structured constraint-map advances. None of the four is an agent execution failure; each is the structural boundary the gate was built to measure. Per `feedback_reporting-framing.md`: PASS and FAIL are equally informative; the position of each gate in the constraint surface is the result, not the verdict label. The framework's permanent-walls ledger advances by +1 net wall (parity-blindness theorem); the candidate-closure ledger loses two conjectures pending audits. This is what disciplined elimination-by-pre-registration looks like in practice.
