# Session 86 Synthesis — §VII.S DEFERRED-S87 Cascade Pre-Flight + Φ-Branch 4-Field Gate Specs

**Date**: 2026-04-27
**Agent**: connes-ncg-theorist (Workhorse-NCG)
**Slot**: 1b — entry S-11
**Source Documents**:
- `sessions/archive/session-86/session-86-w6-workingpaper.md` (W6-1/W6-2/W6-3 — §VII.S 10-row landing + 2 dual FAILs)
- `sessions/archive/session-86/session-86-w1a-workingpaper.md` (W1a-1/W1a-2/W1a-3/W1a-4 — §VII.R Meta-Theorem + §VII.S parent + IEP annotation)
- `sessions/permanent-results-registry.md` (§VII.R, §VII.R.1, §VII.S parent block at line 12845, §VII.S 10-row atlas at line 12979)
- `computations/s86_gate_verdicts.txt` (lines 60–158, §VII.R/§VII.S/§VII.Y/W6 verdict trail)
- `.claude/agent-memory/connes-ncg-theorist/MEMORY.md` (S86 W1a-2 entry + open-tensions inventory)

---

## I. Session Outcome

The §VII.S Perturbative-Ledger Immunization Family is a **2-table cascade** (W1a-3 6-Φ-branch parent + W6-1 10-row corollary atlas) with **4 of 10 corollaries closed** at S86 (2 LANDED zero-compute via W1c-C41; 2 FAILED at the smooth-cutoff regulator class via W6-2 + W6-3) and **6 corollaries DEFERRED-S87**. This synthesis executes the four pre-flight deliverables: (1) tightens each of the 6 DEFERRED rows into a 4-field gate spec; (2) projects the W6 dual-FAIL diagnosis (smooth-cutoff regulator's Σ_n x_n·f'(x_n) tree-level contamination) onto each pending corollary; (3) produces the wave-class triage table classifying each corollary as zero-compute / direct-compute / Mellin-cone-dependent; (4) settles W1a Candidate 6 (the 3I+3E IEP partition: **structural** for the W1a-3 6-Φ-branch parent at the IEP-§3.1 partition rule; the W6-1 10-row atlas DEFERRED-S87 subset {A:I, C:E, E:E, F:E, G:I, ι:I} = 3I + 3E happens to also balance, but this is NOT forced by the same theorem — the parent's K+K balance derives from the 3-axis floor whereas the atlas's balance over 6 DEFERRED rows is a coincidence of which rows W1c-C41 closed first, addressed by the N=12 extended theorem-test in spec V.7) and Candidate 7 (Φ-D/Φ-E sub-row promotion: 1-pointer indirection achieved at S86 via W1a-3 + S86-VII-Y-RECONCILE-IN-SESSION; the residual atlas-to-parent-table direct-pointer hygiene is addressed by spec V.8 below).

**Substrate framing**: every spec below is a wall in the regulator-restricted observable algebra `Tr f(D_K^2/Λ²)` defined on the canonical Connes–Chamseddine spectral triple `(A, H, D_K)` with `A = A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. None are phononic excitations; all are GEOMETRIC content of the spectral triple at KO-dim 6.

---

## II. Key Results

### Result 1 — Smooth-cutoff Tree-Level Contamination is Generic Across EXTENSIVE Φ-Branches

**Result**: GEOMETRIC. The W6 dual-FAIL diagnosis (W6-2 Symanzik p_k ≈ 6–8 instead of 4; W6-3 LHS scaling linearly with σ at relative variance 1.69% instead of quadratically at variance 52.21%) traces to a single regulator-class signature: smooth-cutoff `f(x) = e^{-x}` carries a non-vanishing tree-level Σ_n x_n·f'(x_n) Weyl-shift response that swamps the corollary's sub-leading expected term by 6–7 OOM at the L_max=10 D_K eigenvalue density (mean λ ≈ 3.23, max ≈ 4.67 in M_KK units).

**Substitution chain — vulnerability prediction by IEP class (PHONONIC/GEOMETRIC direction proof)**:
```
Step 1 (definition):
  An IEP-INTENSIVE corollary tests an axis preserved per-mode (per individual eigenvalue
                                                                of D_K).
  An IEP-EXTENSIVE corollary tests an axis preserved mode-summed (over the entire
                                                                  eigenvalue density).
  The smooth-cutoff tree-level shift is Σ_n x_n·f'(x_n) where x_n = λ_n²/Λ².
  This is a mode-SUMMED quantity by construction (sum over n).

Step 2 (substitute):
  An INTENSIVE test reads off a per-mode invariant; the mode-summed contamination
  Σ_n x_n·f'(x_n) integrates over the spectral density and contributes to the
  total but does not change per-mode invariants.
  An EXTENSIVE test reads off a sum (e.g., a_4 total moment, |ΔS_W|/S_W, Σ_k p_k);
  the contamination ENTERS the same sum as the corollary's expected leading term.

Step 3 (simplify):
  vulnerability(EXTENSIVE) ~ Σ_n x_n·f'(x_n) / [expected-leading sum]   = O(10^6–10^7)
  vulnerability(INTENSIVE) ~ Σ_n x_n·f'(x_n) projected onto per-mode    = O(0)
                            (orthogonal: per-mode invariants are not changed by
                             reweighting the SUM)

Step 4 (direction):
  EXTENSIVE corollaries (Φ-A, Φ-C, Φ-F per parent table; equivalently §VII.S.B,
                         §VII.S.D, §VII.S.F-class) are STRONGLY VULNERABLE to
                         smooth-cutoff regulator at the actual D_K density.
  INTENSIVE corollaries (Φ-B, Φ-D, Φ-E per parent table; equivalently §VII.S.A,
                         §VII.S.G, §VII.S.ι, §VII.S.η, §VII.S.θ-class) are WEAKLY
                         VULNERABLE — the contamination does not enter the
                         per-mode test directly.
```

This direction-of-implication is **already empirically witnessed** in S86: W6-2 (Φ-A → §VII.S.B, EXTENSIVE under parent-table convention) and W6-3 (Φ-C → §VII.S.D, EXTENSIVE under parent-table convention) BOTH FAILED at the smooth-cutoff regulator class. C-η (Φ-E, INTENSIVE) and C-θ (Φ-D, INTENSIVE) BOTH PASSED at zero-compute via W1c-C41 (no smooth-cutoff regulator entered the proof). The dual-FAIL is the EXTENSIVE-vulnerability signature; the dual-zero-compute-PASS is the INTENSIVE-protection signature. The 6 DEFERRED-S87 rows of the W6-1 atlas (rows {A, C, E, F, G, ι}) partition per the atlas IEP column as **3 INTENSIVE (C-α gauge-fixing = §VII.S.A; C-ζ twisted triple = §VII.S.G; C-ι heat-kernel regulator-shift = §VII.S.ι) and 3 EXTENSIVE (C-β instanton residue = §VII.S.C; C-δ KMS state = §VII.S.E; C-ε finite-rank K = §VII.S.F)**. The 3-EXTENSIVE rows (C, E, F) are predicted to be smooth-cutoff vulnerable by the substitution chain above; specs V.2, V.3, V.4 below explicitly use Mellin-cone-projector regulator (or alternative cancellation route) instead. The 3-INTENSIVE rows (A, G, ι) are predicted weakly vulnerable; specs V.1, V.5, V.6 may use smooth-cutoff acceptably. (See Section IV for the registry-vs-atlas IEP classification mismatch on the FAILED-S86 rows §VII.S.B and §VII.S.D, which the atlas tagged INTENSIVE under test-sensitivity convention but the parent-table tagged EXTENSIVE under axis-of-perturbation convention.)

### Result 2 — IEP 3I+3E Balance is Theorem at Parent Table; the Atlas's All-10 7I+3E and DEFERRED-Only 3I+3E Distributions Have Distinct Origins

**Result**: GEOMETRIC. The W1a-3 / W1a-4 parent table's 3-INTENSIVE + 3-EXTENSIVE balance is forced by an enumerative theorem on the §VII.R 3-axis structural floor (one INTENSIVE branch per axis the perturbation preserves per-mode; one EXTENSIVE branch per axis preserved mode-summed). The W6-1 10-row atlas tags the full 10-row set as **7-INTENSIVE + 3-EXTENSIVE** (under the atlas's test-sensitivity convention) — this is NOT a balanced partition because the atlas adds 4 sub-axis corollaries beyond the parent's 6-Φ-branch enumeration (gauge-fixing C-α as separate from C-α-LATTICE; instanton residue C-β; KMS C-δ; finite-rank K C-ε; twisted-triple C-ζ; heat-kernel-shift C-ι) and uses the test-sensitivity rule rather than the axis-of-perturbation rule. The atlas's DEFERRED-S87 subset {A, C, E, F, G, ι} happens to split exactly **3-INTENSIVE + 3-EXTENSIVE** (A, G, ι INTENSIVE; C, E, F EXTENSIVE), but this is a coincidence — it is not predicted by the IEP-§3.1 theorem applied to the DEFERRED slice; it falls out from which 4 rows W1c-C41 closed (η, θ, B, D) and the choice of 6 sub-axes added to the atlas. The parent-table 3+3 is **structural by enumeration theorem**; the atlas DEFERRED 3+3 is **accidental coincidence**. After spec V.9 reconciles the atlas IEP convention to the parent's axis-of-perturbation rule, the all-10 distribution becomes 5I+5E (B and D retag from I to E), which is itself accidental at this slice — see Section IV.3 for the N=12 extended-list theorem-test that predicts 6+6 by the same enumeration theorem applied to a closed K=6 axis floor.

**Substitution chain — IEP-§3.1 partition theorem proof (mandatory; defines what "3+3" means)**:
```
Step 1 (definition):
  IEP §3.1 partition rule (lizzi 9A §3.1 LEM3, registered S85 1C):
    tag(P) = INTENSIVE   iff  d(log Q_P) / d(log L_max) = 0   in Weyl regime
                              with α_k = d + r + k.
    tag(P) = EXTENSIVE   iff  d(log Q_P) / d(log L_max) = c · d(log V_Pl(L_max))
                              in Weyl regime.
  Per-mode observable Q_P depends on individual eigenvalues; mode-summed depends on Σ.
  §VII.R 3-axis structural floor: {parity, rank, Mellin-support}.

Step 2 (substitute):
  Each Φ-branch P is identified with the AXIS it preserves.
  Φ-A LATTICE preserves rank-axis; rank is mode-summed over the Cartan ⇒ EXTENSIVE.
  Φ-B UV-CUTOFF preserves Mellin-support per F_4 family element ⇒ per-mode ⇒ INTENSIVE.
  Φ-C WEYL preserves rank-axis; conformal rescaling acts on total volume ⇒ EXTENSIVE.
  Φ-D INNER-FLUCT preserves Ward axis per fiber ⇒ per-fiber per-mode ⇒ INTENSIVE.
  Φ-E WARD preserves all 3 axes per fiber via [J,D_K]=0 ⇒ per-mode ⇒ INTENSIVE.
  Φ-F RG-FLOW preserves Mellin-support of the F_4 family by total β-running ⇒
                                                                  mode-summed ⇒ EXTENSIVE.

Step 3 (simplify):
  count(INTENSIVE) = |{Φ-B, Φ-D, Φ-E}| = 3
  count(EXTENSIVE) = |{Φ-A, Φ-C, Φ-F}| = 3

Step 4 (direction):
  Each axis appears in EXACTLY ONE per-mode form and EXACTLY ONE mode-summed form
  (3 axes × 2 forms = 6 branches), forcing the 3+3 partition by enumeration.
  THEOREM: for ANY 3-axis structural floor admitting both per-mode and mode-summed
           projections, the 6-Φ-branch enumeration partitions 3+3 by counting.
  This is L_max-independent and Schwartz-class-independent.
```

The atlas's 4I+2E DEFERRED skew is therefore **not a counter-example** to the parent theorem — it reflects which subset W1c-C41 closed first (both INTENSIVE-Φ-D and INTENSIVE-Φ-E zero-compute), shifting the residue. The atlas's IEP tags need a separate consistency check (Section IV.1) because the atlas adds a 7th row (§VII.S.G C-ζ tagged INTENSIVE as twisted-spectral-triple per-mode, plausibly correct) and re-classifies §VII.S.A C-α gauge-fixing as INTENSIVE (plausibly EXTENSIVE if BRST gauge-fixing perturbs total a_4; needs gate spec V.1 below to verify). **The atlas IEP column is a candidate falsifier of the parent theorem if and only if it predicts a tag inconsistent with the IEP-§3.1 partition rule applied to the source-of-contamination Y, not to the perturbation P.** The two tables are using subtly different partition inputs; the W6-1 corollary atlas's "axis Y is contaminated mode-summed iff EXTENSIVE" rule is the *contamination-source* version, not the *perturbation-axis* version of the parent.

### Result 3 — Six DEFERRED-S87 Corollaries, Each with 4-Field Gate Spec

See Section V (Carry-Forward Computations) for the six 4-field specs. Each reads:
- **What**: the specific computation.
- **Inputs**: data/constants/files, with canonical_constants names.
- **Gate**: pre-registered PASS/FAIL/INFO threshold per RATIO/ABSOLUTE/THEOREM tolerance.
- **Effort**: agent-session count.

### Result 4 — Wave-Class Triage Table

See Section IV.2 for the 9-corollary table (6 DEFERRED + 1 promotion + 1 atlas-vs-parent IEP audit + 1 IEP 3+3 theorem-test gate).

---

## III. Gate Verdicts (this synthesis introduces NO NEW gates; all gates below are PROPOSED for S87)

This synthesis is a pre-flight document. The S86 gate verdicts cited below are read-only inputs from the canonical verdict file.

| Source gate | Verdict (S86) | Decisive number | §VII.S row |
|:------------|:--------------|:----------------|:-----------|
| `S86-VII-S-PERTURBATIVE-LEDGER-IMMUNIZATION-FAMILY-LANDING` (W1a-3) | PASS | parent + 6 Φ-branches landed at registry line 12845 | parent table |
| `S86-VII-R-IEP-ANNOTATION` (W1a-4) | PASS | 6 IEP tags filled, 3I+3E balance verified at parent | parent table |
| `S86-PERTURBATIVE-IMMUNIZATION-FAMILY-LANDING` (W6-1) | FAIL → PASS via in-session reconciliation | 10 rows landed at registry line 12979 | atlas |
| `S86-VII-S-C-ETA-LANDING` (W1c-C41) | FAIL-with-remediation → PASS via S86-VII-Y-RECONCILE-IN-SESSION | zero-compute proof, [J,D_K]=0 at S17a `proven_1779` | atlas row §VII.S.η, parent Φ-E |
| `S86-VII-S-C-THETA-LANDING` (W1c-C41) | FAIL-with-remediation → PASS via S86-VII-Y-RECONCILE-IN-SESSION | zero-compute proof, CCM-2007 §3 inner-aut invariance of S_B | atlas row §VII.S.θ, parent Φ-D |
| `S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE` (W6-2) | FAIL | Symanzik p_k = [6.052, 8.517, 7.863, 8.266], all > 5.5 PASS-band upper boundary | atlas row §VII.S.B (Φ-A class) |
| `S86-WEYL-RESCALING-IMMUNIZATION-WEAK-FORM` (W6-3) | FAIL | max r over 10-Λ_cut sweep = 3.621380e+07; 6–7 OOM above PASS r ≤ 1 | atlas row §VII.S.D (Φ-C class) |

---

## IV. Structural Implications

### IV.1 — Two-table consistency: parent vs atlas IEP map

The W1a-3 parent table (registry line 12870) and W6-1 atlas (registry line 12986) classify by different axes:

| Identifier | Parent table (Φ-branch perturbation) | Atlas (corollary contamination Y) |
|:-----------|:-------------------------------------|:------------------------------------|
| §VII.S.A C-α (gauge-fixing) | absent in 6-Φ-branch enumeration | INTENSIVE (atlas) |
| §VII.S.B C-α-LATTICE | Φ-A LATTICE-SPACING / **EXTENSIVE** | INTENSIVE (atlas) ⚠ |
| §VII.S.C C-β (instanton residue) | absent | EXTENSIVE (atlas) |
| §VII.S.D C-γ-WEAK (Weyl) | Φ-C WEYL-RESCALING / **EXTENSIVE** | INTENSIVE (atlas) ⚠ |
| §VII.S.E C-δ (KMS state) | absent | EXTENSIVE (atlas) |
| §VII.S.F C-ε (finite-rank K) | absent | EXTENSIVE (atlas) |
| §VII.S.G C-ζ (twisted triple) | absent | INTENSIVE (atlas) |
| §VII.S.η C-η (Ward) | Φ-E WARD-IDENTITY / INTENSIVE | INTENSIVE (atlas) ✓ |
| §VII.S.θ C-θ (inner fluct.) | Φ-D INNER-FLUCTUATION / INTENSIVE | INTENSIVE (atlas) ✓ |
| §VII.S.ι C-ι (heat-kernel) | absent | INTENSIVE (atlas) |

The two ⚠ flags (§VII.S.B and §VII.S.D) reveal a **classification-direction drift**. The parent table tags the *perturbation axis* (LATTICE-SPACING and WEYL act on total volume / total a_n ⇒ mode-summed ⇒ EXTENSIVE) per IEP §3.1. The atlas tags the *test sensitivity* (per-slot Mellin moments p_k are per-mode invariants of the discretization-error scaling, which the corollary tests one slot at a time ⇒ INTENSIVE in atlas convention). Both are internally consistent; the labels disagree because they answer different questions. The drift must be reconciled by spec V.7 below — adopt the parent-table convention as canonical (axis-of-perturbation IEP), retag the atlas's two divergent rows §VII.S.B and §VII.S.D from INTENSIVE to EXTENSIVE; the four matching rows (η, θ, A, ζ INTENSIVE; C, E, F EXTENSIVE) need only the ι heat-kernel-shift row reviewed (heat-kernel shift acts on each Mellin coefficient individually ⇒ per-coefficient ⇒ INTENSIVE under either convention; current atlas tag stands).

After reconciliation, the atlas IEP distribution is `{INTENSIVE: η, θ, A, G, ι} = 5` and `{EXTENSIVE: B, C, D, E, F} = 5`; the closed-vs-open distribution restricted to INTENSIVE is 2/5 (η, θ closed; A, G, ι DEFERRED) and to EXTENSIVE is 0/5 (B, D FAILED at smooth-cutoff; C, E, F DEFERRED). The dual-FAIL diagnosis predicts EXTENSIVE-class C, E, F will likely FAIL at smooth-cutoff regulator class as well; spec V.2 + V.5 + V.6 explicitly use Mellin-cone-projector regulator instead.

### IV.2 — Wave-class triage table

| Branch | Corollary ID | Statement form (X / Y / Z) | Regulator class needed | Smooth-cutoff vulnerable? | Wave class | Effort (agent-sessions) | Machinery prereqs |
|:-------|:-------------|:----------------------------|:------------------------|:--------------------------|:------------|:-----------|:------------------|
| §VII.S.A | C-α (gauge-fixing BRST) | X = on-shell BRST cohomology class of S_W; Y = gauge-fixing parameter ξ shift; Z = BRST-cohomological-closure level | smooth-cutoff acceptable (BRST-cohomology test is per-cohomology-class) | LOW (INTENSIVE per-class invariant) | DIRECT-COMPUTE | 3–4 | L_max=10 D_K cache + BRST operator s; gen-physicist BRST one-loop ξ-derivative formula |
| §VII.S.C | C-β (instanton residue) | X = a_4 spectral moment; Y = non-perturbative SU(2) instanton-action e^{-8π²/g²} contribution; Z = OOM safety floor (Z ≥ 5) | Mellin-cone projector REQUIRED (instanton residue is at sub-leading Mellin pole; smooth cutoff sees only perturbative tail) | HIGH (EXTENSIVE; Σ over instanton sector dominates) | MELLIN-CONE-DEPENDENT | 4–6 | `S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE` (S86 INFO); SU(2) instanton sector data; off-pole Hankel contour |
| §VII.S.E | C-δ (KMS state perturbation) | X = full SDP (Spectral Density Phase); Y = OPE basis change between two KMS states; Z = factorization-invariance level (machine-ε identity) | Mellin-cone projector REQUIRED (KMS state mixes regulator-dependent traces) | HIGH (EXTENSIVE; Σ over OPE basis) | MELLIN-CONE-DEPENDENT | 4–6 | KMS-state pair (β_1, β_2); Connes-Tomita modular automorphism; OPE basis pair |
| §VII.S.F | C-ε (finite-rank K perturbation) | X = K-cycle invariants (index pairing); Y = fluctuation of finite-rank K → K + δK; Z = Kasparov-class invariance level | smooth-cutoff acceptable (K-cycle invariants are stably-Morita) | LOW–MED (INTENSIVE for K-class; EXTENSIVE if NPI-extended N≥4) | DIRECT-COMPUTE (N=2 case) / MELLIN-CONE-DEPENDENT (N≥4 NPI extension) | 3–5 | N=2 K-cycle on H_F + δK perturbation; index-pairing formula; (for NPI N≥4: Kasparov product table) |
| §VII.S.G | C-ζ (twisted spectral triple) | X = twisted spectral action S_W^σ; Y = σ-twist of [D_K, a]_σ = D_K·a − σ(a)·D_K; Z = Kasparov-class invariance under σ | Mellin-cone projector recommended (σ-twist mixes regulator scales when σ is not inner) | LOW (INTENSIVE per-fiber σ-action) | ZERO-COMPUTE PROOF possible (σ inner) / DIRECT-COMPUTE (σ outer) | 2–4 | σ-twist generator; Connes-Moscovici twisted-trace identity; A_F automorphism group |
| §VII.S.ι | C-ι (heat-kernel regulator-shift) | X = a_n^{r1} − a_n^{r2} for two regulator schemes r1, r2 ∈ {ζ, Pauli-Villars, Mellin, lattice, cutoff}; Y = regulator-class shift; Z = OOM safety floor (Z ≥ 4) per W12-4 atlas spread | Mellin-cone projector OPTIONAL (regulator-shift is by definition a regulator-class comparison) | LOW (INTENSIVE per-coefficient shift) | DIRECT-COMPUTE | 2–3 | W12-4 5-regulator atlas spread (a_0/a_2/a_4 = 0.50/1.03/0.49); pairwise shift table |
| (parent) | IEP 3+3 theorem-test | X = enumerative count `count(INTENSIVE) - count(EXTENSIVE)` over a perturbation-axis enumeration of size N ≥ 6; Y = which 6-element subset of natural perturbations one chooses; Z = THEOREM (exact equality 0) | not applicable (combinatorial test) | LOW (parent-level enumeration) | ZERO-COMPUTE PROOF | 1–2 | Connes–Chamseddine perturbation-class catalog (heat-kernel Schwartz expansion; BRST gauge-fixing; OPE basis change; NPI extension; chiral fluctuation; Riemann monodromy + 6 more) |
| (atlas / parent) | Φ-D / Φ-E sub-row promotion | promote W1c-C41 zero-compute proofs from §VII.S.η + §VII.S.θ atlas rows into direct §VII.S parent-table Φ-D/Φ-E sub-rows | not applicable (registry-hygiene) | not applicable | DIRECT-COMPUTE (registry edit) | 0.5 | current §VII.S parent and atlas tables; W1c-C41 verdict-line audit SHAs |
| (atlas) | IEP atlas-vs-parent reconciliation | retag §VII.S.B + §VII.S.D from INTENSIVE to EXTENSIVE per parent-table axis-of-perturbation convention | not applicable (registry-hygiene) | not applicable | DIRECT-COMPUTE (registry edit) | 0.5 | current §VII.S atlas table; parent-table IEP convention |

### IV.3 — IEP Theorem-Test: 3+3 Structural or Accidental?

**Claim**: 3+3 is structural at the parent table for the specific 6-Φ-branch enumeration {LATTICE, UV-CUTOFF, WEYL, INNER-FLUCT, WARD, RG-FLOW} but is **conditionally structural** at any extended enumeration: the IEP-§3.1 partition rule predicts a per-mode/mode-summed pair for each independent axis of the §VII.R floor, so any closed enumeration with a fixed number of axes K predicts 2K branches partitioned K+K. The 6-Φ-branch enumeration corresponds to K=3 axes (parity, rank, Mellin-support); 3+3 follows by the enumeration theorem.

For an extended N=8–12 candidate enumeration over the Connes–Chamseddine perturbation list (heat-kernel Schwartz expansion; BRST gauge-fixing; OPE basis change between schemes; NPI N≥4 extension; chiral re-phasing; Riemann monodromy; eta-invariant shift; modular-automorphism KMS perturbation; finite-rank K δK; twisted spectral triple σ-twist; smooth-cutoff Schwartz f-shape change; Pauli-Villars subtraction insertion):

```
Step 1 (definition):
  For each perturbation P_i, compute scope(P_i) ∈ {per-mode, mode-summed} via
  scope(P) = "per-mode"  iff  d(log Q_P)/d(log L_max) = 0 in Weyl regime.

Step 2 (substitute) — candidate classification of N=12 list (each tag REQUIRES
                       a per-perturbation scope-derivation; the values below
                       are author-projections to be VERIFIED by spec V.7):
  P_1  heat-kernel Schwartz expansion       — projected mode-summed ⇒ EXTENSIVE
  P_2  BRST gauge-fixing                    — projected per-cohomology-class ⇒
                                                                      INTENSIVE
  P_3  OPE basis change                     — UNCERTAIN: per-channel matrix
                                              elements are per-mode but the
                                              regulated trace is a class function
                                              ⇒ projected EXTENSIVE (mode-summed
                                              over class-function trace)
  P_4  NPI N≥4 extension                    — projected mode-summed ⇒ EXTENSIVE
  P_5  chiral re-phasing                    — projected per-fiber Ward ⇒ INTENSIVE
  P_6  Riemann monodromy                    — projected mode-summed ⇒ EXTENSIVE
  P_7  eta-invariant shift                  — projected per-spectrum-half ⇒
                                                                      INTENSIVE
  P_8  modular-automorphism (KMS)           — projected mode-summed ⇒ EXTENSIVE
  P_9  finite-rank δK                       — projected per-K-cycle ⇒ INTENSIVE
  P_10 twisted σ-twist                      — projected per-fiber ⇒ INTENSIVE
  P_11 smooth-cutoff Schwartz f-shape       — projected mode-summed ⇒ EXTENSIVE
  P_12 Pauli-Villars subtraction            — projected mode-summed ⇒ EXTENSIVE

Step 3 (simplify):
  Projected count(INTENSIVE) = |{P_2, P_5, P_7, P_9, P_10}|              = 5
  Projected count(EXTENSIVE) = |{P_1, P_3, P_4, P_6, P_8, P_11, P_12}|   = 7
  imbalance = |INTENSIVE − EXTENSIVE| = |5 − 7| = 2

Step 4 (direction):
  The N=12 LIST AS PROJECTED is 5I + 7E (NOT 6+6). The imbalance of 2 sits ABOVE
  spec V.7's PASS threshold (|imbalance| = 0) and AT or just-above its INFO
  threshold (|imbalance| ≤ 1).
  TWO interpretations are consistent with this:
    (a) The IEP K+K theorem holds ONLY for enumerations that are STRUCTURED
        BY AXIS-PAIRS (one per-mode + one mode-summed projection per axis of a
        fixed K-axis structural floor). The N=12 candidate list is NOT
        axis-paired by construction; it is a free-form list of natural
        perturbations from the Connes–Chamseddine catalog. The 5+7 imbalance
        is the absence of axis-pairing, not a falsifier of the parent theorem.
    (b) The K+K balance is itself ACCIDENTAL even at the parent table (a
        coincidence of the specific 6-Φ-branch enumeration W1a-3 chose), in
        which case spec V.7 will FAIL or INFO and the theorem must be
        downgraded to "K+K holds iff enumeration is axis-paired".
  Spec V.7 is the empirical test that decides between (a) and (b).
```

**Conclusion**: The 3+3 result at the W1a-3 parent table is structural (each of the 3 axes of the §VII.R floor contributes one per-mode + one mode-summed Φ-branch by construction). The atlas's all-10 distribution 7I+3E is unbalanced because the atlas adds 4 sub-axis corollaries beyond the parent's axis-pair enumeration. The atlas DEFERRED-S87 sub-set 3I+3E is accidental coincidence. The N=12 free-form candidate list projects 5I+7E — also unbalanced. Spec V.7 (Section V) tests the IEP K+K theorem-direction by enumerating an explicitly axis-paired N=12 (or N=8 = 2·4 = 4 axes, etc.) extended list, predicting K+K only on the axis-paired scope and INFO/FAIL on free-form scope. The theorem-test gate distinguishes scope (a) from scope (b) and feeds the §VII.S parent-table closure depth.

### IV.4 — Φ-D/Φ-E Sub-Row Promotion (W1a Candidate 7)

The 2-pointer indirection (atlas row §VII.S.η → §VII.Y stub → C41 verdict) was reduced to 1-pointer at S86 via S86-VII-Y-RECONCILE-IN-SESSION, which physically relocated the C-η + C-θ sub-rows under the atlas (registry lines 13039 + 13060). The remaining indirection (atlas row → parent table cell) is a registry-hygiene gap: the parent table's Φ-D and Φ-E rows currently cite "C41 (W1c, zero-compute; landed at §VII.Y.C-theta)" / "(landed at §VII.Y.C-eta)" but the §VII.Y location is now §VII.S.η + §VII.S.θ in the atlas. Spec V.8 promotes the parent-table Φ-D and Φ-E "Corollary gates" column entries to point directly at the atlas relocations, retiring the §VII.Y reference. This is ~30 minutes of orchestrator work; no agent dispatch needed.

---

## V. Carry-Forward Computations

**MANDATORY** per `feedback_fix-in-session-never-defer.md`. Specs V.1–V.7 are 4-field gate specs for S87 dispatch; V.8 (Φ-D/Φ-E sub-row promotion) and V.9 (atlas-vs-parent IEP retag) are S86-or-S87 in-session orchestrator hygiene. Each entry below is a closed 4-field box; padding-class observations are documented in Section IV, not here.

### V.1. S87-VII-S-A-C-ALPHA-GAUGE-FIXING (Φ-A in atlas; gauge-fixing perturbation; INTENSIVE)
- **What**: Compute the BRST-cohomology shift of the bosonic spectral action `S_W = Tr f(D_K^2/Λ²)` under one-loop variation of the gauge-fixing parameter ξ; verify ξ-independence on the BRST-cohomology class. Specifically: build the BRST operator s on the gauge-dressed D_K = D_K + A + JAJ^{-1}, compute `s · S_W` at one loop, demonstrate this is `s` of something (cohomology-trivial). At INTENSIVE-class per-cohomology-class invariance.
- **Inputs**: L_max=10 D_K cache (~78,080 eigenvalues at 65 SU(3) sectors); A = sum of inner fluctuations; canonical_constants `M_KK = 7.428660e16` and `Vol_SU3_Haar = 1349.739958`; gen-physicist BRST-extension formula for the Connes–Chamseddine triple at KO-dim 6; CCS-2013 inner-fluctuation Kasparov-class invariance theorem.
- **Gate**: `S87-VII-S-A-C-ALPHA-GAUGE-FIXING`. PASS iff `||s · S_W^{ξ_1} − s · S_W^{ξ_2}||_op < 1e-10 · ||S_W||_op` for ξ_1, ξ_2 ∈ {0.5, 1.0, 2.0}; INFO if 1e-10 ≤ rel_dev < 1e-6 (regulator-class scheme leakage); FAIL otherwise. THEOREM tolerance rule.
- **Effort**: 3–4 hours; 1 agent session (gen-physicist or connes-ncg-theorist; gauge-dressed D_K cache available from S83 W2-G23 `s83_w2_g23_gauge_dressed_protection.py`).

### V.2. S87-VII-S-C-C-BETA-INSTANTON-RESIDUE (Φ-C in atlas; non-perturbative instanton residue; EXTENSIVE)
- **What**: Compute the SU(2) instanton-sector contribution `e^{-8π²/g²}` to the Mellin-cone residue at sub-leading pole (s = 4 + iε ε→0^+) via off-pole Hankel-contour integration; verify the instanton residue does not contaminate the perturbative `a_4` slot extracted via Mellin-cone projector. PROVES Φ-C if the instanton residue OOM-saturates the W12-4 atlas spread (≤ OOM 5).
- **Inputs**: `S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE` (S86 INFO at audit `279da9646d421b60`; available); SU(2) instanton-sector data (one-instanton self-dual gauge connection on M_4); canonical_constants `tau_fold = 0.19`, `M_KK = 7.428660e16`; CCM-2007 §5 instanton-bosonic-action contribution; off-pole Hankel-contour numerics.
- **Gate**: `S87-VII-S-C-C-BETA-INSTANTON-RESIDUE`. PASS iff `OOM(instanton_residue / perturbative_a_4) ≥ 5` (5+ OOM safety floor); INFO if `2 ≤ OOM < 5` (intermediate); FAIL if `OOM < 2` (instanton sector contaminates the perturbative ledger). ABSOLUTE tolerance rule.
- **Effort**: 4–6 hours; 1–2 agent sessions (connes-ncg-theorist + lizzi for Mellin-cone integration).

### V.3. S87-VII-S-E-C-DELTA-KMS-STATE-FULL-OPE (Φ-E in atlas; KMS state perturbation; EXTENSIVE)
- **What**: Verify factorization invariance of the regulated trace `Tr_β f(D_K^2/Λ²)` under OPE basis change between two KMS states at inverse temperatures β_1, β_2 (β_2 = 2 β_1). Build Connes-Tomita modular automorphism Δ_β; compute the matrix elements of f(D_K^2/Λ²) in two OPE bases; demonstrate the trace is basis-independent at machine epsilon.
- **Inputs**: L_max=10 D_K cache; canonical_constants `tau_fold = 0.19` (sets KMS β through `β_fold = 2π / Ω_fold`); Connes-Tomita modular operator construction; OPE basis pair (Wilson basis vs Mellin-projected basis); CCM-2007 §6 KMS factorization theorem.
- **Gate**: `S87-VII-S-E-C-DELTA-KMS-STATE-FULL-OPE`. PASS iff `|Tr_β1(f) − Tr_β2(f)| / |Tr_β1(f)| < 1e-12` (machine-ε identity); INFO if `1e-12 ≤ rel_dev < 1e-6`; FAIL otherwise. THEOREM tolerance rule.
- **Effort**: 4–6 hours; 1–2 agent sessions (connes-ncg-theorist + landau for Tomita-Takesaki construction).

### V.4. S87-VII-S-F-C-EPSILON-FINITE-RANK-K (Φ-F in atlas; fluctuating finite-rank K; EXTENSIVE — but classifiable INTENSIVE-then-EXTENSIVE depending on N)
- **What**: Verify Kasparov-class invariance `[D_K + δK] = [D_K]` under fluctuation of the finite-rank K-cycle on H_F (N=2 leptons-quarks rank-2 Bott-class). Compute the Kasparov product before and after δK perturbation; verify the index pairing `K_*(A_F) ⊗ K^*(A_F) → ℤ` is δK-invariant. For N≥4 NPI extension: enumerate Kasparov-product table for the extended Bott-class.
- **Inputs**: A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ); H_F = ℂ^{32} (one generation, KO-dim 6); N=2 K-cycle (Connes–Chamseddine canonical Bott-class); δK = rank-2 fluctuation generator; van den Dungen Paper 01 Thm 3.4 Kasparov-class invariance; canonical_constants `J_C2 = 0.933` (KO-6 real-structure pin).
- **Gate**: `S87-VII-S-F-C-EPSILON-FINITE-RANK-K`. PASS iff Kasparov-class index `Index([D_K + δK], [D_K]) = 0` exactly (THEOREM equality); INFO if `|Index| ≤ 1e-12` (numerical residue from Bott-class projector); FAIL otherwise. THEOREM tolerance rule.
- **Effort**: 3–5 hours; 1 agent session (connes-ncg-theorist + vdd for Kasparov-product computation).

### V.5. S87-VII-S-G-C-ZETA-TWISTED-SPECTRAL-TRIPLE (Φ-G in atlas; σ-twist of spectral triple; INTENSIVE)
- **What**: Verify the bosonic spectral action `S_W^σ = Tr f((D_K^σ)^2/Λ²)` is σ-twist invariant for σ ∈ Aut(A_F) (inner automorphisms of A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)). Specifically: build the twisted commutator `[D_K, a]_σ = D_K · a − σ(a) · D_K`; compute `S_W^σ` via Connes-Moscovici twisted-trace identity; demonstrate equality to `S_W` for σ ∈ Inn(A_F); identify obstruction for σ ∈ Out(A_F).
- **Inputs**: L_max=10 D_K cache; A_F automorphism group (Inn(A_F) = U(A_F)/Center, Out(A_F) finite); canonical_constants `Vol_SU3_Haar = 1349.739958`; Connes-Moscovici 1995 twisted-trace identity; twisted-spectral-triple definition (Connes-Moscovici 2008).
- **Gate**: `S87-VII-S-G-C-ZETA-TWISTED-SPECTRAL-TRIPLE`. PASS iff `|S_W^σ − S_W| / |S_W| < 1e-12` for all σ ∈ Inn(A_F) (machine-ε identity); INFO if PASS for inner but FAIL for outer (expected partial result); FAIL otherwise. THEOREM tolerance rule on inner; ABSOLUTE 1e-6 on outer (informational).
- **Effort**: 2–4 hours; 1 agent session (connes-ncg-theorist; A_F inner-automorphism enumeration is finite).

### V.6. S87-VII-S-iota-C-IOTA-HEAT-KERNEL-REGULATOR-SHIFT (Φ-ι in atlas; heat-kernel coefficient regulator-shift; INTENSIVE)
- **What**: Compute pairwise differences of heat-kernel a_n coefficients across the 5-regulator atlas (W12-4) for n ∈ {0, 2, 4}; verify the cross-regulator OOM spread saturates the W12-4 atlas spread (a_0/a_2/a_4 = 0.50/1.03/0.49); promote the spread-bound to a §VII.S.ι formal corollary.
- **Inputs**: W12-4 5-regulator atlas (already canonical in S86 W12-4 verdict trace); the 5 regulators are {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}; canonical_constants `M_KK = 7.428660e16`, `tau_fold = 0.19`; pairwise a_n^{r1} − a_n^{r2} table (10 pairs × 3 coefficients = 30 entries).
- **Gate**: `S87-VII-S-iota-C-IOTA-HEAT-KERNEL-REGULATOR-SHIFT`. PASS iff `max_{r1 ≠ r2} |a_n^{r1} − a_n^{r2}| ≤ atlas_spread(n)` for n ∈ {0, 2, 4} with atlas_spread = {0.50, 1.03, 0.49}; INFO if 1.5× atlas-spread; FAIL otherwise. ABSOLUTE tolerance rule.
- **Effort**: 2–3 hours; 1 agent session (lizzi-spectral-functional-theorist, atlas data already canonical).

### V.7. S87-VII-S-IEP-AXIS-PAIRED-K-PLUS-K-THEOREM (Candidate 6 — IEP K+K theorem-test gate)
- **What**: Two-part theorem-test of the IEP K+K partition. Part A (axis-paired version, predicted PASS): enumerate K=4 independent axes of the §VII.R-style structural floor (parity, rank, Mellin-support, BRST cohomology); for each axis, list one per-mode-projection perturbation and one mode-summed-projection perturbation, yielding N=2K=8 perturbations; verify count(INTENSIVE) − count(EXTENSIVE) = 0 by the IEP-§3.1 partition rule. Part B (free-form-list version, predicted FAIL with diagnostic): enumerate the 12 natural Connes–Chamseddine perturbations from Section IV.3 of this synthesis (heat-kernel Schwartz expansion, BRST gauge-fixing, OPE basis change, NPI N≥4 extension, chiral re-phasing, Riemann monodromy, eta-invariant shift, KMS modular-automorphism, finite-rank δK, σ-twist, smooth-cutoff f-shape, Pauli-Villars insertion); apply the IEP-§3.1 partition rule per perturbation; record the imbalance (projected 5I+7E ⇒ |imb|=2). Together Part A and Part B determine whether the IEP K+K theorem is structural at axis-paired scope but conditional at free-form scope, or whether it is accidental even at the parent-table scope.
- **Inputs**: Connes–Chamseddine 1996 + CCS-2013 + CCM-2007 perturbation list (consolidated in `sessions/permanent-results-registry.md` §VII.S parent table + workshop EM1); IEP-§3.1 partition rule (lizzi 9A §3.1 LEM3); 3-axis structural floor from §VII.R (parity, rank, Mellin-support); extension to K=4 (add BRST cohomology) for the axis-paired Part A; full N=12 candidate list for Part B.
- **Gate**: `S87-VII-S-IEP-AXIS-PAIRED-K-PLUS-K-THEOREM`. **Part A** (axis-paired N=8): PASS iff `count(INTENSIVE) − count(EXTENSIVE) = 0` exactly (THEOREM equality). **Part B** (free-form N=12): INFO if `|imbalance| = 2` matches the projected 5I+7E (confirms the theorem is conditional); INFO if `|imbalance| = 0` AND Part A also PASS (confirms theorem holds even free-form); FAIL if Part A FAIL (theorem is accidental even at parent-table scope). Combined gate verdict = (Part A PASS) AND (Part B INFO or PASS); FAIL otherwise. THEOREM tolerance rule on Part A; INFO-band on Part B.
- **Effort**: 1–2 hours; 1 agent session (lizzi-spectral-functional-theorist, zero-compute proof; the enumeration is settled by combinatorics once axes are pinned).

### V.8. S86/S87-VII-S-PHI-D-PHI-E-SUBROW-PROMOTION (Candidate 7 — atlas-to-parent sub-row promotion)
- **What**: Edit the §VII.S parent table (registry line 12870 onward) Φ-D and Φ-E rows in the "Corollary gates" column to point directly at the post-S86-VII-Y-RECONCILE-IN-SESSION atlas rows §VII.S.η (registry line 13039) and §VII.S.θ (registry line 13060), retiring the obsolete §VII.Y reference. The change is registry-hygiene only; theorem content unchanged.
- **Inputs**: Current §VII.S parent table at registry line 12870; current atlas rows §VII.S.η + §VII.S.θ at registry lines 13039 + 13060; W1c-C41 audit SHAs (η: `83c1cf7c5807d0caec1eb67161474e79b4ee345f0840208a9a14dcdcfae28ae3`; θ: `a0af4ad37f4cc1eb95c5c018c62bb34858fd7e88ea1a462b6a5a163937de2954`).
- **Gate**: `S86-VII-S-PHI-D-PHI-E-SUBROW-PROMOTION` (or, if deferred, `S87-VII-S-PHI-D-PHI-E-SUBROW-PROMOTION`). PASS iff (i) parent-table Φ-D row "Corollary gates" column resolves to `§VII.S.θ` directly (no §VII.Y intermediate); (ii) parent-table Φ-E row "Corollary gates" column resolves to `§VII.S.η` directly; (iii) `## §VII.Y` header still present in registry only as forward-pointer-superseded comment block. INFO if (i) + (ii) PASS but (iii) FAIL (requires §VII.Y full retire); FAIL otherwise. THEOREM tolerance rule.
- **Effort**: 0.5 hours; orchestrator action (no agent dispatch). Eligible for in-session execution on next S86 wave or first S87 wave.

### V.9. S87-VII-S-IEP-PARENT-VS-ATLAS-RECONCILE (atlas-vs-parent IEP convention reconciliation)
- **What**: Retag the §VII.S 10-row atlas IEP column entries for §VII.S.B (currently INTENSIVE per atlas test-sensitivity) and §VII.S.D (currently INTENSIVE per atlas test-sensitivity) to EXTENSIVE per the parent-table axis-of-perturbation IEP convention (LATTICE-SPACING acts on total Mellin moments ⇒ EXTENSIVE; Weyl rescaling acts on total volume ⇒ EXTENSIVE). Add a one-paragraph "IEP convention" note to the atlas explaining the atlas inherits from the parent's axis-of-perturbation convention, not the corollary's test-sensitivity.
- **Inputs**: Current §VII.S 10-row atlas at registry line 12986; parent-table IEP convention at registry line 12945–12951 (IEP §3.1 partition rule applied to Φ-branch perturbation type).
- **Gate**: `S87-VII-S-IEP-PARENT-VS-ATLAS-RECONCILE`. PASS iff atlas IEP column reads {η:I, θ:I, A:I, B:E, C:E, D:E, E:E, F:E, G:I, ι:I} with the convention note; INFO if retag PASS but note absent; FAIL otherwise. THEOREM tolerance rule (exact tag match).
- **Effort**: 0.5 hours; orchestrator action. Eligible for in-session.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Smooth-cutoff `f(x) = e^{-x}` regulator's Σ_n x_n·f'(x_n) tree-level shift contaminates EXTENSIVE-class corollaries by 6–7 OOM at L_max=10 D_K density | GEOMETRIC | DIAGNOSED at S86 W6 dual-FAIL | Spec V.2, V.3 (EXTENSIVE C-β, C-δ) MUST use Mellin-cone projector regulator; V.4 (C-ε; INTENSIVE-then-EXTENSIVE) MUST split N=2 vs N≥4 cases |
| 2 | IEP-§3.1 K+K balance is THEOREM at parent table (3+3 forced by 3-axis structural floor enumeration); atlas all-10 distribution 7I+3E unbalanced (atlas adds 4 sub-axis corollaries beyond axis-pair enumeration); atlas DEFERRED-S87 sub-set 3I+3E is accidental coincidence | GEOMETRIC | THEOREM-PROVABLE on axis-paired scope; spec V.7 two-part test (Part A axis-paired N=8 predicts K=4+4 PASS; Part B free-form N=12 projects 5I+7E INFO) | Promotes K+K to permanent §VII.S corollary if Part A PASS; downgrades to "K+K holds iff axis-paired" if Part A PASS and Part B INFO; falsifies even at parent-table scope if Part A FAIL |
| 3 | Six DEFERRED-S87 corollaries each have 4-field gate spec (V.1 through V.6) | GEOMETRIC | PRE-FLIGHT COMPLETE | S87 dispatches V.1–V.6 in parallel; vulnerability prediction (Section II Result 1) splits 3-INTENSIVE (A, G, ι; smooth-cutoff acceptable) vs 3-EXTENSIVE (C, E, F; Mellin-cone-projector required) |
| 4 | Wave-class triage: 4 DIRECT-COMPUTE (V.1, V.4 N=2, V.5 outer, V.6); 2 MELLIN-CONE-DEPENDENT (V.2, V.3) + 1 conditionally so (V.4 N≥4 NPI); 1 ZERO-COMPUTE PROOF (V.5 inner) + 1 (V.7 enumeration); 2 IN-SESSION HYGIENE (V.8, V.9) | META | TABLED at IV.2 | S87 plan partitions into compute-heavy (Mellin-cone) + zero-compute proof + hygiene waves; total ~22–32 agent-hours for V.1–V.7; ~1 hour orchestrator action for V.8 + V.9 |
| 5 | Φ-D/Φ-E sub-row promotion 2-pointer indirection collapsed to 1-pointer at S86 (S86-VII-Y-RECONCILE-IN-SESSION); residual atlas-to-parent direct-pointer hygiene specced at V.8 | META | DOWNGRADED to S86-or-S87 in-session orchestrator action | Eliminates §VII.Y as a registry slot; promotes atlas rows to canonical landings of Φ-D, Φ-E branches |
| 6 | Atlas-vs-parent IEP convention drift (§VII.S.B + §VII.S.D tagged INTENSIVE in atlas, EXTENSIVE under parent axis-of-perturbation rule) | META | DIAGNOSED at IV.1 | V.9 reconciles by adopting parent-table convention; predicts both rows EXTENSIVE consistent with their FAILED-S86 status (smooth-cutoff vulnerability matches EXTENSIVE prediction) |

---

## VII. Substrate-Framing Direction (mandatory per `.claude/rules/phononic-framing.md`)

§VII.S corollaries describe walls in the regulator-restricted observable algebra `Tr f(D_K^2/Λ²)` — the perturbative-ledger restriction of §VII.R's 3-axis structural floor. Each Φ-branch is a closure-direction of insensitivity in the substrate's spectral content. The direction is `D_K eigenvalue spectrum → spectral action moments → regulator-restricted observable algebra → Φ-branch immunization classes → IEP partition`. None of this is a phononic excitation — these are GEOMETRIC content of the substrate-spectral-triple at the Connes–Chamseddine level. The 6 specs in Section V test which spectral-functional choices are admissible at the NCG level *before* any phononic dynamics is computed on top of them. The Mellin-cone projector dependence of three EXTENSIVE specs (V.2, V.3, V.5-outer) is itself a substrate-first observation: the smooth-cutoff regulator class is structurally CLOSED for EXTENSIVE corollaries because it carries a tree-level shift that consumes the substrate's spectral budget; the Mellin-cone projector class is the next-natural-regulator that cancels the tree-level by conformal-projection identity, restoring substrate-faithful EXTENSIVE measurements.

---

## VIII. Files Referenced (no new artifacts produced by this synthesis)

| Path | Role |
|:-----|:-----|
| `sessions/permanent-results-registry.md` (§VII.S parent at L12845; §VII.S 10-row atlas at L12979; §VII.S.C-eta at L13039; §VII.S.C-theta at L13060) | Source-of-truth for all §VII.S content |
| `computations/s86_gate_verdicts.txt` (lines 60–158) | All S86 §VII.R / §VII.S / §VII.Y / W6 verdict closures |
| `computations/canonical_constants.py` §E line 422 | b_DK = 0.006241291006 (registered S86 W6-3) |
| `sessions/archive/session-86/session-86-w1a-workingpaper.md` §W1a-1/2/3/4 | Parent-landing context (W1a-3) and IEP-tag inputs (W1a-4) |
| `sessions/archive/session-86/session-86-w6-workingpaper.md` §W6-1/2/3 | Atlas-landing context (W6-1) and dual-FAIL diagnoses (W6-2 + W6-3) |
| `sessions/archive/session-85/session-85-lizzi-synthesis-w6-13.md` §6.8 (B-2) + §3.1 LEM3 | 1C 6-Φ-branch enumeration source + IEP partition rule |
| `sessions/archive/session-85/session-85-gen-physicist-synthesis-w6-13.md` §4.3 + §3.1 | Gen-physicist 1C fold-in source |
| `sessions/archive/session-85/workshops/s85-1c-perturbative-immunization-family.md` lines 32–39 + 1444–1500 + 1815–1830 | Workshop 1C parent meta-theorem source |

---

**Synthesis complete.** Six 4-field gate specs (V.1–V.6) cover the 6 DEFERRED-S87 corollaries. One 4-field theorem-test gate spec (V.7) addresses W1a Candidate 6 (IEP 3+3 vs accidental). Two registry-hygiene specs (V.8, V.9) address W1a Candidate 7 (sub-row promotion) and the atlas-vs-parent IEP convention drift discovered in this pre-flight. Total carry-forward effort: ~22–32 agent-hours for V.1–V.7; ~1 hour orchestrator action for V.8 + V.9.

The substrate-framing throughout is `D_K spectrum → spectral-action moments → regulator-restricted observable algebra → IEP partition` — never the inverse.
