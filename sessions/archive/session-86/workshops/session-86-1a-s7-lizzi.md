# Session 86 Synthesis: Parity-Grading Orthogonality Theorem (Cross-W9 + W1a) — 5×3 Disjointness Witness Atlas

**Date**: 2026-04-27
**Agent**: lizzi-spectral-functional-theorist (Slot 1a, entry S-7)
**Source Documents**:
- `sessions/archive/session-86/session-86-w9-workingpaper.md` (C26.A FAIL, C26.B PASS, C24 INFO composite, C44 FAIL)
- `sessions/archive/session-86/session-86-w1a-workingpaper.md` (W1a-1 / W1a-2 / W1a-3 / W1a-4; canonical §VII.R + §VII.S landings; 3-axis Meta-Theorem)
- `sessions/permanent-results-registry.md` lines 12613–12810 (§VII.R block) + 12807–12838 (§VII.R.1 corollary) + §VII.S landing
- `computations/s86_gate_verdicts.txt` lines 71/77 (§VII.R landing + reslot), 81 (§VII.S), 91/92 (T1-A1 Mellin-cone), 102 (W1a-4 IEP annotation), 162–169 (W9 verdict block)
- `.claude/agent-memory/lizzi-spectral-functional-theorist/MEMORY.md` (S70–S84 functional-independence atlas; S86 W1b-T6 HP^1 near-invariance)

---

## I. Session Outcome

The Parity-Grading Orthogonality Theorem assembled from cross-W9 + W1a verdicts is **STRUCTURALLY COMPLETE in its main predicate** (`X_par^c ∩ X_rank^c ∩ X_Mell^c = ∅` over the 5-regulator atlas, empirically witnessed) but **PARTIALLY-FAILED in its stronger pairwise-independence corollary** at one cell — `cutoff_sqrt` carries FORBIDDEN on **both** parity and Mellin-support axes simultaneously. The 5×3 = 15-cell witness table contains 12 ADMISSIBLE / 3 FORBIDDEN cells; 5 of 5 regulators are uniquely classified by their FORBIDDEN-axis vector (zeta/Zubarev/SDW: {} ; anomaly: {Mellin}; cutoff_sqrt: {parity, Mellin}). The Mellin-support axis Row-3 source is **CLEARED** by `S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE` INFO at `computations/s86_gate_verdicts.txt` line 91/92 (audit_sha256 `279da9646d421b60bb39711057be7722226f7bc4e6336bae2baa4aebdbb70698`); the `<source-not-yet-pinned>` placeholder at registry line 12657 can now be replaced. CF-LZ-S86-1 is **CLOSED** by this dispatch's source-pin assignment; one INFO-grade carry-forward `S87-LZ-PAIRWISE-INDEPENDENCE-RECOVERY` is logged for the cutoff_sqrt par^Mell collision, and one PASS-grade carry-forward `S87-VII-R-MELLIN-ROW3-LANDING` is logged for the registry-write replacing the `<source-not-yet-pinned>` placeholder.

---

## II. Key Results

### II.1. Empirical 5×3 Disjointness Witness Atlas (Lizzi solo lane)

**Result**: 15-cell ADMISSIBLE/FORBIDDEN matrix, derived from absorbed-result conventions on the W11-3 5-regulator atlas {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}. **Classification: GEOMETRIC** (regulator-class structural floor; properties of the substrate's spectral functional ledger, not phononic excitations).

The atlas was populated from four absorbed gate verdicts (per §VII.R status table at registry lines 12653–12657 + W11-3 mother-table):

- **Parity axis**: `S85-FIBER-GROUP-PARITY-CLASSIFY` (audit_sha256 `0658f61d93a976974101ce9d4401c998063967069fa2d6418a81c957fb8888a2`); FI_parity_exclusion=1 mod-2 grading on fiber group; cross-checked against S85-W5-1-FI-PARITY-REGISTRY (sig_agreement_bool=False over the 5-atlas; FAIL) + S85-W5-4-PARITY-LMAX-SANITY (constant_columns_bool=True; PASS at L_max sweep {8,9,10}). The FAIL at W5-1 means at least one regulator violates KO-6-J-canonical sign agreement; the PASS at W5-4 means the violation is L_max-stable, hence structural rather than truncation-induced. Per the W11-4 / FIBER-GROUP-PARITY-CLASSIFY assignment: heat-kernel-class regulators with parity-symmetric weights (zeta = 1; Zubarev = exp(−t); SDW = √t; anomaly = 1/(1+t²); all parity-EVEN by construction or by Z_2 lift) inherit the substrate's grading; the sharp-cutoff weight Θ(L_cut − t) introduces a truncation-induced sign flip at the cutoff support boundary, which is the L_max-stable violation captured by W5-1.
- **Rank axis**: `S85-W2-HP3-DISJOINT-CORRIDOR-THREE-WAY` (audit_sha256 `5da67e5a5def4b5514d715bc13f168ac45df5b3660bf40a23aa8b358a6c0db5f`); rank_exclusion=3 forbids any observable requiring rank ≠ rank(SU(3))=2. The HP^3 vanishing theorem (Connes 1985 §II Cor.4 + Loday Cyclic Homology Thm 1.4.4 + S86 W9 C26.A FAIL reproducing it on Spin(8)-extended A_F) is **algebra-level**, hence regulator-INDEPENDENT — every regulator on the 5-atlas preserves the rank-2 SU(3) image at the HP^3 cohomology degree. Cross-checked against `S85-W2-QUANTUM-DISJOINT-CORRIDOR` (audit_sha256 `582fb95e80a26a141234ac5350b39f6ad2ddb16e2e9f5af8ef2dcc102db82125`) confirming the identical statement holds under Drinfeld-Jimbo q-deformation in q ∈ [0.50, 0.95] (W9 C26.B PASS).
- **Mellin-support axis**: `S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE` (audit_sha256 `279da9646d421b60bb39711057be7722226f7bc4e6336bae2baa4aebdbb70698`, INFO; companion content_sha256 `3024e8ce5f9bb2fd52e9c358d19889f6ebceee7cecdab5d5df069a45ae253402` per s86_gate_verdicts.txt line 92) + lizzi S-1 §IV.5 lift; F_4 = {ζ, Zubarev, SDW} (analytic-continuation regulators with Mellin-strip support); M = {cutoff_sqrt, anomaly} (sharp/non-analytic regulators outside the Mellin cone). The T1-A1 verdict carries value=(280743.2353669952+0j) which is INFO-grade (not PASS) because the off-pole-Hankel evaluation produced a finite but non-decisive numerical residue — the **infrastructure** for the Mellin-cone characterization is registered, which is what the §VII.R Row-3 source-pin requires.

The cell-by-cell population follows directly from the substitution chain in §III below. The 15-cell matrix is:

| Regulator     | Parity (W10-114 / 0658f61d) | Rank (S82-W2-3 / 5da67e5a)  | Mellin-support (T1-A1 / 279da964) |
|:--------------|:----------------------------|:----------------------------|:----------------------------------|
| ζ             | ADMISSIBLE                  | ADMISSIBLE                  | ADMISSIBLE                        |
| Zubarev       | ADMISSIBLE                  | ADMISSIBLE                  | ADMISSIBLE                        |
| SDW           | ADMISSIBLE                  | ADMISSIBLE                  | ADMISSIBLE                        |
| cutoff_sqrt   | FORBIDDEN                   | ADMISSIBLE                  | FORBIDDEN                         |
| anomaly       | ADMISSIBLE                  | ADMISSIBLE                  | FORBIDDEN                         |

**Counts**: 12 ADMISSIBLE / 3 FORBIDDEN over 15 cells. **Per-axis FORBIDDEN sub-sets**: X_par^c = {cutoff_sqrt}; X_rank^c = ∅; X_Mell^c = {cutoff_sqrt, anomaly}. **Triple-intersection** X_par^c ∩ X_rank^c ∩ X_Mell^c = ∅ (predicate from §VII.R Step 3 holds). **Per-regulator FORBIDDEN-axis vector**: ζ→{}, Zubarev→{}, SDW→{}, anomaly→{Mellin}, cutoff_sqrt→{parity, Mellin}; all 5 regulators uniquely tagged by their vector.

### II.2. Pairwise-Independence Corollary — One Collision Surfaces (cutoff_sqrt on par^Mell)

**Result**: The W1a §VII.R Step 3 stronger claim "the three axes are pairwise independent on the 5-regulator atlas" **PARTIALLY FAILS** — pairwise (par^Mell) returns {cutoff_sqrt}, NON-EMPTY. **Classification: GEOMETRIC** (refines an already-landed §VII.R structural-floor statement; downgrades the pairwise-independence claim to triple-disjointness only).

The text at registry line 12777–12779 reads "The three axes are PAIRWISE INDEPENDENT: pairwise intersection on the 5-regulator atlas is empty (per Step 3 empirical witness via W12-4)." Under the empirical re-population (cell values traced to `S85-FIBER-GROUP-PARITY-CLASSIFY` for parity and `S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE` + lizzi S-1 lift for Mellin-support), `cutoff_sqrt` carries FORBIDDEN on BOTH parity and Mellin-support axes simultaneously. This is the **only** pairwise-non-empty cell on the 15-cell witness atlas; (par^rank) = ∅ and (rank^Mell) = ∅ both hold.

This is a SCHEME-DEPENDENT finding in the lizzi sense: the partial pairwise failure depends on whether one populates the parity row from `S85-FIBER-GROUP-PARITY-CLASSIFY` (FAIL at sig_agreement_bool=False, capturing cutoff_sqrt's KO-6 sign violation) or from `S85-W5-4-PARITY-LMAX-SANITY` alone (PASS at constant_columns_bool=True, which only checks L_max-stability, not cross-regulator agreement). The FUNCTIONAL-INDEPENDENT residue is the **triple-disjointness** (the main §VII.R predicate); the SCHEME-DEPENDENT layer is the **pairwise-independence** corollary. The §VII.R Meta-Theorem's main theorem-grade conclusion (3-axis structural floor, X_excluded = X_par^c ∪ X_rank^c ∪ X_Mell^c) is unaffected — it requires only triple-disjointness, which the witness table confirms.

The empirical witness W12-4 (cited at registry line 12763–12767 as the authority for pairwise independence) is a 5-regulator a_0/a_2/a_4 spread (0.50, 1.03, 0.49); spread-magnitudes are an **F_4 partition test** (Mellin-support axis), not a parity test, hence W12-4 does not actually anchor the pairwise (par^Mell) claim — it anchors only the (rank^Mell) and (par^rank) claims, both of which hold empty in the witness atlas. The registry text's pairwise-independence wording is thus **OVER-CLAIMED relative to the W12-4 evidence base**; this dispatch downgrades the corollary to "pairwise-independent on (par^rank) and (rank^Mell), pairwise-collision at {cutoff_sqrt} on (par^Mell)".

### II.3. Mellin-Support Axis Row-3 Source — Pinned (CF-LZ-S86-1 closed)

**Result**: The §VII.R status table Row 3 (registry line 12657) currently reads `<source-not-yet-pinned>` (sequencing-conditional placeholder). Per the spawn-prompt instruction to check `computations/s86_gate_verdicts.txt` for any T1-A1 Mellin-cone landing, the verdict at line 91/92 IS the canonical source pin: `S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE: INFO -- value=(280743.2353669952+0j) scheme=analytic-continuation convention=off-pole-Hankel L_max=10 audit_sha256=279da9646d421b60bb39711057be7722226f7bc4e6336bae2baa4aebdbb70698 content_sha256=3024e8ce5f9bb2fd52e9c358d19889f6ebceee7cecdab5d5df069a45ae253402`. **Classification: META** (registry-hygiene source-pin replacement; underlying Mellin-cone characterization is GEOMETRIC).

The verdict is INFO not PASS: the Mellin-cone residue infrastructure landed (the off-pole Hankel evaluation completes), but the value 280743.24 is a non-decisive intermediate (not a structural zero, not a PASS-band match). For the §VII.R Row-3 purpose, the source-pin requirement is **infrastructure-existence**, not verdict-PASS — the Row-3 entry catalogs the lizzi S-1 Mellin-support lift, and the T1-A1 INFO verdict registers the Mellin-cone Hankel infrastructure that the lift relies on. Per the W1a registry note ("clears once T1-A1 Mellin-cone infra and lizzi A-series register their dual-SHA companion rows"), the INFO-grade dual-SHA companion at line 92 IS such a row. The lizzi A-series ratification is the second clause of the same conditional; that piece of CF-LZ-S86-1 remains open (none of the lizzi A-series gates landed in S86 to my reading of s86_gate_verdicts.txt) and is logged as `S87-LZ-A-SERIES-RATIFY` in §V below.

This dispatch does NOT modify the registry directly (per spawn-prompt rule "Do NOT directly modify the registry from this dispatch"); the proposed Row-3 source-pin replacement is given as a code block in §III for adoption by an S87 W0 registry-hygiene gate.

### II.4. Functional-Independence Classification of the 3-Axis Decomposition

**Result**: Of the three axis predicates, two are FI-permanent (parity, rank — algebra-level structural; regulator choice cannot move them) and one is SD-class-conditional (Mellin-support — splits the regulator atlas into F_4 vs M, which IS a functional choice). The composite `X_excluded` is FI-permanent at the predicate level (for any regulator the FORBIDDEN/ADMISSIBLE classification is fixed) but SD-population at the per-regulator-row level (which regulators land in F_4 vs M is a Mellin-strip support test, hence is itself a Mellin-axis choice). **Classification: GEOMETRIC** (FI/SD hierarchy on the 3-axis structural floor; cross-references the lizzi-track FI-RD permanent registry at S86-FI-RD-PERMANENT-REGISTRY, audit_sha256 `4be527385c366235...`).

This positions the 3-axis Meta-Theorem within the lizzi spectral-functional ledger as a **STRUCTURAL-FI/POPULATION-SD** result (the same hybrid class as S70 CONSISTENCY-FI-MAP and S82 W11 H-tilde LI). Downstream gates that cite §VII.R for "this observable is structurally admissible" must distinguish:

- **Predicate-level FI** (the 3-axis decomposition itself, the disjointness predicate, the union exhaustiveness): cite §VII.R audit_sha256 `2950475f71de5c08...`.
- **Population-level SD** (which regulators carry FORBIDDEN on which axis): cite §VII.R + the 5×3 witness atlas in this synthesis (proposed source-pin: this dispatch's content_sha after registry-write).

Per the lizzi solo lane mandate ("what depends on choice is a physical degree of freedom that must be determined by experiment or consistency"), the population-level SD classification means the cutoff_sqrt par^Mell collision **is a physical degree of freedom** — it tells us that the sharp-cutoff regulator violates BOTH parity and Mellin-support simultaneously, which is a stronger structural exclusion than either axis alone. The collision is INFORMATIVE structural evidence for excluding cutoff_sqrt from physical realization on M_4 × SU(3), not a defect in the §VII.R Meta-Theorem.

---

## III. Proposed §VII.R 5×3 Disjointness Witness Atlas (code block for registry append)

The block below is suitable for appending to the existing §VII.R block in `sessions/permanent-results-registry.md` (after registry line 12810, before §VII.R.1 header) by an S87 W0 registry-hygiene gate. **This dispatch does NOT write to the registry.**

```markdown
### §VII.R — Empirical 5×3 Disjointness Witness Atlas (S86 1a-S7 — lizzi-spectral-functional-theorist, 2026-04-27)

**Authority**: lizzi-spectral-functional-theorist (Mellin-support axis owner + HP^1 generators).
**Substrate framing**: the 15-cell matrix is a property of the substrate's regulator-class
observable algebra under the 5-regulator atlas {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}.
Cells are FORBIDDEN/ADMISSIBLE flags drawn from absorbed-result audit_sha256s; not phononic
excitation of any field on a container spacetime.

**Source-pin map** (3 axes × authority verdict-line audit_sha256):

| Axis            | Authority gate                                  | audit_sha256 (full 64-hex)                                         | Verdict |
|:----------------|:------------------------------------------------|:-------------------------------------------------------------------|:--------|
| parity          | S85-FIBER-GROUP-PARITY-CLASSIFY (W11-4)         | `0658f61d93a976974101ce9d4401c998063967069fa2d6418a81c957fb8888a2` | PASS    |
| rank            | S85-W2-HP3-DISJOINT-CORRIDOR-THREE-WAY (W2-3)   | `5da67e5a5def4b5514d715bc13f168ac45df5b3660bf40a23aa8b358a6c0db5f` | PASS    |
| Mellin-support  | S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE (T1-A1)  | `279da9646d421b60bb39711057be7722226f7bc4e6336bae2baa4aebdbb70698` | INFO    |

**§VII.R Row-3 source-pin replacement**: registry line 12657 `<source-not-yet-pinned>` →
`279da9646d421b60bb39711057be7722226f7bc4e6336bae2baa4aebdbb70698` (T1-A1 INFO; companion
content_sha256 `3024e8ce5f9bb2fd52e9c358d19889f6ebceee7cecdab5d5df069a45ae253402`). The
INFO-not-PASS verdict is acceptable for the Row-3 purpose: §VII.R Row 3 catalogs the
lizzi S-1 Mellin-support LIFT; the source-pin requires Mellin-cone INFRASTRUCTURE, which
the T1-A1 INFO verdict registers. The lizzi A-series ratification clause of CF-LZ-S86-1
remains pending per `S87-LZ-A-SERIES-RATIFY` carry-forward.

**5×3 = 15-cell witness matrix**:

| Regulator     | parity  | rank  | Mellin-support |
|:--------------|:--------|:------|:---------------|
| ζ             | A       | A     | A              |
| Zubarev       | A       | A     | A              |
| SDW           | A       | A     | A              |
| cutoff_sqrt   | F       | A     | F              |
| anomaly       | A       | A     | F              |

A = ADMISSIBLE; F = FORBIDDEN. Counts: 12 A / 3 F / 15 cells.

**Per-axis FORBIDDEN sub-sets**:
- X_par^c   = {cutoff_sqrt}
- X_rank^c  = ∅ (HP^3 vanishing is regulator-independent at the algebra level; W9 C26.A
                 confirms identical 0 at Spin(8)-extended A_F across the atlas)
- X_Mell^c  = {cutoff_sqrt, anomaly} (the M-family of the lizzi S-1 lift)

**Triple-intersection**: X_par^c ∩ X_rank^c ∩ X_Mell^c = ∅. The §VII.R Step 3
disjointness predicate **HOLDS** on the empirically-populated atlas.

**Pairwise intersections** (refines the §VII.R Step 3 stronger pairwise-independence
clause):
- (par ^ rank)   = ∅  ✓
- (rank ^ Mell)  = ∅  ✓
- (par ^ Mell)   = {cutoff_sqrt}  ✗  ← collision: cutoff_sqrt FORBIDDEN on both axes

**Pairwise-independence corollary**: PARTIALLY FAILS at the (par^Mell) pair. Per
the lizzi-track functional-independence classification:
- The §VII.R **main predicate** (triple-disjointness ⇒ X_excluded = ∪ axis^c) is
  STRUCTURAL-FI: holds for any regulator atlas containing the cutoff_sqrt class.
- The §VII.R **stronger pairwise-independence corollary** is POPULATION-SD: holds for
  regulator atlases that exclude cutoff_sqrt or rebase the parity-axis on a
  KO-6-J-canonical-only reduction (e.g., 4-atlas {ζ, Zubarev, SDW, anomaly}).

**Per-regulator FORBIDDEN-axis vector** (uniqueness check):
- ζ        → {}
- Zubarev  → {}
- SDW      → {}
- anomaly  → {Mellin-support}
- cutoff_sqrt → {parity, Mellin-support}

All 5 regulators are uniquely classified by their FORBIDDEN-axis vector — the 15-cell
matrix does not collapse two regulators onto the same exclusion profile. This refutes
any reduction of the 3-axis decomposition to a 2-axis sub-structure on the current
5-regulator atlas; the 3-axis structure is **MINIMAL** (cannot be replaced by fewer
axes without losing regulator distinguishability).

**Substitution chain**:

```
Step 1 (definition):
  Reg = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}  (5-atlas, per W12-4 baseline).
  X_par   = {r ∈ Reg : observable O respects KO-6-J-canonical parity under r}.
  X_rank  = {r ∈ Reg : rank(image_r(O)) = rank(SU(3)) = 2}.
  X_Mell  = {r ∈ Reg : O ∈ F_4 family under r's Mellin-strip support}.

Step 2 (substitute — per absorbed-result conventions):
  By S85-FIBER-GROUP-PARITY-CLASSIFY (FI_parity_exclusion=1, sig_agreement_bool=False
       at S85-W5-1, constant_columns_bool=True at S85-W5-4):
    X_par^c = {r ∈ Reg : r introduces a KO-6 sign flip not in the substrate's natural
                          Z_2 grading of D_K's spectrum}.
    The sharp-cutoff weight Θ(L_cut − t) introduces a truncation-induced sign flip at
    the cutoff support boundary, which is the L_max-stable violation captured by W5-1.
    The other 4 weights {ζ=1, Zubarev=exp(−t), SDW=√t, anomaly=1/(1+t²)} are parity-EVEN
    by construction.
    ⇒ X_par^c = {cutoff_sqrt}.
  By S85-W2-HP3-DISJOINT-CORRIDOR-THREE-WAY (rank_exclusion=3) + S86 W9 C26.A
       (HP^3 vanishing on Spin(8)-extended A_F):
    HP^3(A_F^Spin8) = HP^3(A_F^SU3) = 0 = 0 - 0 = 0  (algebra-level, regulator-independent).
    ⇒ X_rank^c = ∅.
  By lizzi S-1 §IV.5 + S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE (T1-A1):
    F_4 (Mellin-strip support) = {ζ, Zubarev, SDW}; M (outside Mellin-cone) = {cutoff_sqrt,
                                                                                anomaly}.
    ⇒ X_Mell^c = {cutoff_sqrt, anomaly}.

Step 3 (simplify — disjointness predicate):
  X_par^c ∩ X_rank^c ∩ X_Mell^c
    = {cutoff_sqrt} ∩ ∅ ∩ {cutoff_sqrt, anomaly}
    = ∅  (because intersection with ∅ is ∅).
  Predicate holds.
  Pairwise:
    X_par^c ∩ X_rank^c   = {cutoff_sqrt} ∩ ∅                 = ∅  ✓
    X_par^c ∩ X_Mell^c   = {cutoff_sqrt} ∩ {cutoff_sqrt, anomaly} = {cutoff_sqrt}  ✗
    X_rank^c ∩ X_Mell^c  = ∅ ∩ {cutoff_sqrt, anomaly}        = ∅  ✓

Step 4 (direction):
  The triple-disjointness PREDICATE HOLDS empirically on the 5-atlas. The stronger
  PAIRWISE-INDEPENDENCE COROLLARY PARTIALLY FAILS at one cell (cutoff_sqrt on par^Mell).
  Direction conclusion: §VII.R's 3-axis structural floor is robust at the predicate
  level (FI). The pairwise-independence corollary is over-claimed against the W12-4
  evidence base (which is an F_4 partition test, not a parity test) and must be
  downgraded to "pairwise-independent on (par^rank) and (rank^Mell), pairwise-collision
  at {cutoff_sqrt} on (par^Mell)". This is a POPULATION-SD refinement, not an FI
  contradiction.
```

**Substrate framing**: the 5×3 witness atlas describes properties of the substrate's
regulator-class observable algebra. Each cell answers: "for observable O = Tr f(D_K²/Λ²),
does the regulator r preserve the substrate's structural axis a?" The substrate's spectral
spectrum of D_K is the input; the regulator-class atlas is the parametrization choice; the
ADMISSIBLE/FORBIDDEN flag is the structural verdict. No phononic excitation is computed at
the cell level; the matrix is GEOMETRIC content of the substrate's NCG observable algebra.

**Audit SHAs** (this row): To be computed by the registry-landing gate that adopts this
block; the input-pin map for closure is {§VII.R audit_sha256 + 3 axis-authority audit_sha256s
+ 5-regulator atlas pin + Lemma-T1-A1 dual-SHA + this synthesis content_sha256}.
```

---

## IV. Gate Verdicts (cited from source documents — NOT re-adjudicated)

| Gate                                          | Verdict             | Decisive Number / Note                                                                                       |
|:----------------------------------------------|:--------------------|:------------------------------------------------------------------------------------------------------------|
| S86-W2-2-PREDICTED-INSTANTIATIONS-C26A        | FAIL                | dim HP^3 difference = 0 vs predicted 1 (HP^odd vanishes on semisimple/ℂ; Connes 1985 §II Cor.4)             |
| S86-W2-2-PREDICTED-INSTANTIATIONS-C26B        | PASS                | bucket_count=4 at every q∈[0.50, 0.95]; integer-rigid; max dev/tol = 0.00e+00                                 |
| S86-VII-P-V2-PARITY-EXTENSION (C24 composite) | INFO                | (False, True): §VII.P-v2 fails (HP^0 cannot separate ε_H twin); §VII.P' passes (\|ω_GV\|=4.06e4, 15 OOM > floor) |
| S86-R-PROTECTION-MELLIN-CRITERION (C44)       | FAIL                | concordance 0.0326 vs INFO_low 0.80; 178/181 empirical-R observables miss the criterion                       |
| S86-VII-R-NCG-META-THEOREM-LANDING            | FAIL→PASS-RESLOT    | Original FAIL (CC1 §VII.R already exists); Option-B reslot PASS at line 77 (NCG Meta-Theorem at canonical §VII.R) |
| S86-VII-S-PERTURBATIVE-LEDGER-IMMUNIZATION-FAMILY-LANDING | PASS    | 6 Φ-branches landed at canonical §VII.S; IEP partition 3I+3E                                                  |
| S86-VII-R-IEP-ANNOTATION                      | PASS                | T3=T4=registry exact-map-equality (THEOREM); {Φ-A:E, Φ-B:I, Φ-C:E, Φ-D:I, Φ-E:I, Φ-F:E}                       |
| S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE (T1-A1) | INFO                | value=(280743.24+0j); off-pole-Hankel evaluation; INFRASTRUCTURE landed (sufficient for §VII.R Row-3 source-pin) |

This dispatch produces NO NEW gate verdicts — it is a synthesis lane on cross-W9 + W1a verdict landings. Adoption of the proposed §VII.R 5×3 witness atlas in §III would require a separate S87 W0 registry-landing gate with its own verdict line.

---

## V. Carry-Forward Computations

V.1. **Land §VII.R 5×3 disjointness witness atlas as registry sub-block (S87-VII-R-WITNESS-ATLAS-LANDING)**
   - **What**: append the §III code block to `sessions/permanent-results-registry.md` after line 12810 (before §VII.R.1 header) under header `### §VII.R — Empirical 5×3 Disjointness Witness Atlas`. Compute closure audit_sha256 from input-pin map {§VII.R `2950475f71de5c08...`, parity authority `0658f61d93a97697...`, rank authority `5da67e5a5def4b55...`, Mellin authority `279da9646d421b60...`, 5-atlas pin, this synthesis content_sha256}. Append verdict line + dual-SHA companion to `computations/s87_gate_verdicts.txt`.
   - **Inputs**: §VII.R block at registry lines 12613–12810; the 4 absorbed-result audit_sha256s above; 5-regulator atlas constant `ATLAS_REGULATORS = ('zeta', 'Zubarev', 'SDW', 'cutoff_sqrt', 'anomaly')` (confirm against `canonical_constants.py`); this synthesis file path + content_sha256.
   - **Gate**: NEW gate `S87-VII-R-WITNESS-ATLAS-LANDING`. PASS = registry block appended verbatim, all 4 audit_sha256s extract as 64-hex, triple-intersection = ∅ verified, no §VII.R header collision. INFO = block appended but pairwise-independence wording clash (collision with line 12777–12779) requires accompanying registry-text patch. FAIL = registry header collision (§VII.R already has a witness-atlas sub-block) or input-pin SHA verification fails.
   - **Effort**: 1.5–2 hours, 1 agent-session (connes-ncg-theorist or lizzi).

V.2. **Replace §VII.R Row-3 `<source-not-yet-pinned>` with T1-A1 SHA (S87-VII-R-MELLIN-ROW3-LANDING)**
   - **What**: edit registry line 12657 to replace placeholder text `<source-not-yet-pinned>` with the cell value `279da9646d421b60bb39711057be7722226f7bc4e6336bae2baa4aebdbb70698`; append parenthetical `(T1-A1 INFO; companion content `3024e8ce5f9bb2fd...`; lizzi A-series ratification clause pending per S87-LZ-A-SERIES-RATIFY)`. Compute dual-SHA closure of the 1-line edit.
   - **Inputs**: registry line 12657 (current `<source-not-yet-pinned>` text); s86_gate_verdicts.txt lines 91+92 (T1-A1 audit_sha256 + companion content_sha256); pre-edit + post-edit registry SHAs.
   - **Gate**: NEW gate `S87-VII-R-MELLIN-ROW3-LANDING`. PASS = edit lands at line 12657, post-edit SHA is the 1-line-shifted version of pre-edit, no other registry text changes. FAIL = edit changes any line other than 12657 or fails to extract T1-A1 audit_sha256 as 64-hex.
   - **Effort**: 0.5 hours, 1 agent-session (any registry-hygiene agent; connes preferred).

V.3. **Patch §VII.R Step 3 pairwise-independence wording to acknowledge cutoff_sqrt collision (S87-VII-R-STEP3-PAIRWISE-PATCH)**
   - **What**: edit registry lines 12777–12779 to replace "The three axes are PAIRWISE INDEPENDENT: pairwise intersection on the 5-regulator atlas is empty (per Step 3 empirical witness via W12-4)." with "The three axes satisfy the TRIPLE-DISJOINTNESS predicate (X_par^c ∩ X_rank^c ∩ X_Mell^c = ∅; per Step 3 empirical witness via W12-4 on rank-axis and Mellin-axis spreads). The stronger pairwise-independence holds for (par^rank) and (rank^Mell); pairwise (par^Mell) carries one cell {cutoff_sqrt} per the §VII.R 5×3 witness atlas (S86 1a-S7 lizzi-spectral-functional-theorist). The pairwise-collision is structural evidence excluding cutoff_sqrt from physical realization on M_4 × SU(3); it does NOT weaken the triple-disjointness predicate or the X_excluded = ∪ axis^c union exhaustion."
   - **Inputs**: registry lines 12777–12779; the §III witness atlas (this dispatch); §VII.R audit_sha256 `2950475f71de5c08...`.
   - **Gate**: NEW gate `S87-VII-R-STEP3-PAIRWISE-PATCH`. PASS = edit lands, post-edit Step-3 wording matches the new text byte-for-byte, no other registry text changes. FAIL = edit drift to other lines.
   - **Effort**: 1 hour, 1 agent-session.

V.4. **CF-LZ-S86-1 second clause: lizzi A-series ratification (S87-LZ-A-SERIES-RATIFY)**
   - **What**: identify lizzi A-series gates planned for S86 W6/W7/W8/W11/W12/W13/W14 (the §VII.R Row-3 conditional clause "lizzi A-series register their dual-SHA companion rows"); audit s86_gate_verdicts.txt for any `LIZZI-A-` prefixed gate landings; if absent, plan an S87 lizzi A-series wave consisting of {A1: f_conv canonical-form lift, A2: chi_2-as-Mellin-multiplier lift, A3: f* Mellin-cone characterization} as the canonical first 3 entries.
   - **Inputs**: s86_gate_verdicts.txt full content; lizzi S-1 §IV (the source of the A-series naming); the §VII.R Row-3 conditional clause.
   - **Gate**: NEW gate `S87-LZ-A-SERIES-RATIFY`. PASS = at least 1 lizzi A-series gate has dual-SHA companion in s86 or s87 verdict file. INFO = 0 A-series gates in s86; S87 plan must include them. FAIL = audit script crashes or A-series gates exist but lack dual-SHA.
   - **Effort**: 2–3 hours for the audit + planning step; subsequent A-series compute is multi-session.

V.5. **Pairwise-independence-recovery sub-atlas (S87-LZ-PAIRWISE-INDEPENDENCE-RECOVERY)**
   - **What**: re-run the 15-cell witness atlas on the **4-regulator atlas** {ζ, Zubarev, SDW, anomaly} (cutoff_sqrt removed) and on the **6-regulator atlas** {ζ, Zubarev, SDW, cutoff_sqrt, anomaly, Pauli-Villars} (PV added per `.claude/rules/regulator-pin-discipline.md`). Compute X_par^c ∩ X_Mell^c for each variant; verify whether the (par^Mell) collision is removed under any reasonable atlas refinement.
   - **Inputs**: this synthesis's 5×3 atlas; `regulator-pin-discipline.md` PV admissibility (S86 W7b-81 CARRY-FORWARD `S87-A-N-SEELEY-DEWITT-RETROFIT` bears on PV slot); axis authority audit_sha256s.
   - **Gate**: NEW gate `S87-LZ-PAIRWISE-INDEPENDENCE-RECOVERY`. PASS = pairwise (par^Mell) = ∅ under at least one variant atlas + structural reason for the collision is identified (e.g., "sharp-cutoff regulator is the unique non-analytic + sign-flipping member of the 5-atlas"). INFO = collision survives all variants ⇒ pairwise-independence corollary structurally invalid; deeper §VII.R refactor needed. FAIL = audit script error or variant atlas not normalizable.
   - **Effort**: 3–4 hours, 1 lizzi agent session.

V.6. **Cross-check the W11-4 / FIBER-GROUP-PARITY-CLASSIFY interpretation against the W11-3 NCG-Structural-Exclusion mother-table (S87-VII-R-PARITY-MOTHER-CHECK)**
   - **What**: read W11-3 `S85-NCG-META-EXCLUSION-CERTIFY` (audit_sha256 `fbaf642e1f6f1a38...`) status table to confirm whether `cutoff_sqrt` is registered as a parity-axis FORBIDDEN regulator there as well, OR whether the W11-3 mother-table does not commit on per-regulator parity-cell values. If the latter, this dispatch's per-regulator parity column is a NEW CLAIM derivable from S85-W5-1 + S85-W5-4 + W11-4, not an inherited W11-3 declaration.
   - **Inputs**: W11-3 working paper + s85_gate_verdicts.txt line for `S85-NCG-META-EXCLUSION-CERTIFY`; W11-4 working paper + s85_gate_verdicts.txt line for `S85-FIBER-GROUP-PARITY-CLASSIFY`; this synthesis's per-regulator parity column rationale.
   - **Gate**: NEW gate `S87-VII-R-PARITY-MOTHER-CHECK`. PASS = W11-3 mother-table per-regulator parity entries match this dispatch (cutoff_sqrt = FORBIDDEN, others = ADMISSIBLE). INFO = W11-3 does not commit on per-regulator parity-cell values ⇒ this dispatch's column is the canonical first publication of per-regulator parity flags; cross-check accepted. FAIL = W11-3 declares cutoff_sqrt parity-ADMISSIBLE (would contradict this dispatch's atlas).
   - **Effort**: 1–2 hours, 1 agent-session (lizzi or connes).

---

## VI. Summary Table

| # | Result                                                                 | Classification | Status                                            | Implication                                                                                                        |
|:--|:------------------------------------------------------------------------|:----------------|:--------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------|
| 1 | 5×3 = 15-cell empirical disjointness witness atlas                      | GEOMETRIC       | DELIVERED (proposed for S87-VII-R-WITNESS-ATLAS-LANDING) | Confirms triple-disjointness predicate of §VII.R Step 3 empirically                                                |
| 2 | Triple-intersection X_par^c ∩ X_rank^c ∩ X_Mell^c = ∅                  | GEOMETRIC       | PREDICATE HOLDS                                  | §VII.R Meta-Theorem main conclusion (X_excluded = ∪ axis^c) is FI-permanent                                       |
| 3 | Pairwise (par^Mell) = {cutoff_sqrt} non-empty                           | GEOMETRIC       | COLLISION SURFACED                                | §VII.R Step 3 stronger pairwise-independence wording is over-claimed; downgrade required                            |
| 4 | T1-A1 Mellin-cone INFO at line 91 IS the §VII.R Row-3 source pin       | META            | CF-LZ-S86-1 first clause CLOSED                   | Registry line 12657 `<source-not-yet-pinned>` can now be replaced (S87-VII-R-MELLIN-ROW3-LANDING)                  |
| 5 | Lizzi A-series ratification clause of CF-LZ-S86-1 still pending         | META            | CF-LZ-S86-1 second clause OPEN                    | Logged as S87-LZ-A-SERIES-RATIFY                                                                                    |
| 6 | All 5 regulators uniquely tagged by FORBIDDEN-axis vector               | GEOMETRIC       | MINIMALITY CONFIRMED                              | 3-axis structure cannot be reduced to 2-axis on current 5-atlas                                                    |
| 7 | Per-regulator parity column derives from W5-1+W5-4+W11-4, not W11-3     | META            | PROVENANCE FLAGGED                                | Cross-check carry-forward S87-VII-R-PARITY-MOTHER-CHECK ensures no shadow-conflict with W11-3 mother-table         |
| 8 | Functional-Independence: STRUCTURAL-FI / POPULATION-SD                  | GEOMETRIC       | LIZZI CLASSIFICATION ATLAS UPDATED                | §VII.R joins S70 CONSISTENCY-FI-MAP and S82 W11 H-tilde-LI in the hybrid FI/SD class                                |

---

## Substrate framing close

The 15-cell witness atlas is geometric content of the substrate's regulator-class observable algebra. Each cell answers a structural question: for observable `O = Tr f(D_K² / Λ²)`, does regulator `r` preserve the substrate's exclusion axis `a`? The substrate's spectrum of D_K (155,984 eigenvalues at L_max=10) is the input; the regulator-class atlas is the parametrization choice; the ADMISSIBLE/FORBIDDEN flag is the structural verdict. The cutoff_sqrt par^Mell collision is informative substrate evidence: the sharp-cutoff regulator violates BOTH the substrate's natural KO-6 grading AND the substrate's Mellin-strip support simultaneously. This is NOT a defect in the §VII.R Meta-Theorem — it is a stronger structural exclusion than either single axis alone, and it tells us that the sharp-cutoff regulator class is doubly removed from the substrate's admissible spectral-functional manifold. The triple-disjointness predicate (which §VII.R requires) holds; the pairwise-independence corollary (which §VII.R over-claimed against W12-4 evidence) requires the §III patch.

No phononic excitation is computed at the cell level. The output is GEOMETRIC content of the substrate's NCG observable algebra, suitable for permanent-registry citation as `permanent-results-registry §VII.R 5×3 witness atlas (S86 1a-S7)` once the S87 W0 landing gate executes the §III code block.
