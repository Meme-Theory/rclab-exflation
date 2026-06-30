# Session 85 Plan — Wave W2: connes-origin reviewer wave

**Generated**: 2026-04-21
**Wave ID**: W2
**Theme**: connes-origin single-reviewer wave (13 carry-forward items from S84, conv=1, origin=connes)
**Owner**: connes-ncg-theorist
**Output verdict file**: `computations/s85_gate_verdicts.txt`
**Script prefix**: `s85_w2_<slug>.py`
**Batch assignment**: Batch 1 (dispatched alongside W0, W1a, W1b, W3, W4, W5, W6)

---

## Wave W2 Summary

Wave W2 is the connes-origin single-reviewer bucket from the S84 Stage-D collapse.
13 items land here — items identified in `session-85-partition.md` §"Wave W2":

| # | Gate-slug | Carry-forward title | Theme |
|--:|:---------|:--------------------|:------|
| W2-1 | ALPHA-S-AXIOM-MINIMALITY-AU | Axiom-minimality audit (W3-G54-style HP^even completeness applied to alpha_s pre-reg machinery) | ko-dim-pairing |
| W2-2 | CROSS-SESSION-THEOREM-FAMILY | Cross-session theorem family statement (the "disjoint-corridor + ε_H-wall + rank-scaling" unified family from S83-S84) | ko-dim-pairing |
| W2-3 | HP3-DISJOINT-CORRIDOR-THREE-WAY | HP^3 extension: three-way disjoint-corridor theorem (extend §VII.P from HP^2 pairwise to HP^3 triples) | cc-3-connes-moscovici |
| W2-4 | KO6-HIGGS-SIGN-DIRECTION | KO-dim 6 sign-direction proof at the Higgs sector (formalize the J^2=ε, Jγ=ε''γJ sign flow into the Higgs mass term) | ko-dim-pairing |
| W2-5 | PRE-CC-1-KO6-ON-ETA | PRE-CC-1 DIAGNOSTIC — KO-dim=6 constraint check on η-invariant (prerequisite to W0-23 CC-1) | cc-1-eta |
| W2-6 | QUANTUM-DISJOINT-CORRIDOR | Quantum-group extension: q-deformed disjoint-corridor (extend §VII.P to U_q(su(3))) | quantum-group-extension |
| W2-7 | DISJOINT-CORRIDOR-REGISTRY-LANDING | Registry landing of §VII.P (Cohomology-Disjoint-Corridor Theorem) with counter-construction audit | ko-dim-pairing |
| W2-8 | ALPHA-S-PRE-REG-REGISTRY-LANDING | Registry-landing consolidation under §VII.M.2 (Event-driven pre-registrations) | alpha-s-preregistration |
| W2-9 | S50-T15-REGISTRY-UPGRADE | S50 T15 registry-entry upgrade (promote T15 from session-local to permanent-results-registry) | alpha-s-preregistration |
| W2-10 | THREE-SOLO-CONVERGENCE-VERIFY | Three-solo convergence verification (Connes + Lizzi + vdd) — re-verify S84 W2a-11 §VII.M closure after the §VII.N route | van-den-dungen-bridge |
| W2-11 | PRE-CC-2-TRIALITY-ON-JENSEN | PRE-CC-2 DIAGNOSTIC — Triality preservation test on Jensen deformation (prerequisite to W0-10 CC-2) | cc-2-triality |
| W2-12 | BAND-DETECTOR-MAP-LEGGETT-BOG | Two-scale Leggett-Bogoliubov boundary mapping to CMB-S4 sensitivity | leggett-channel |
| W2-13 | PSG-§11.2-REVISION | §11.2 revision of `Phononic-Substrate-Geometry.md` (DOCUMENTATION) | framework-doc-revision |

Wave W2 is **NCG-heavy territory**. Every gate's hypothesis traces back to the spectral triple (A, H, D) and its axioms. Six of the 13 items (W2-1, W2-4, W2-5, W2-7, W2-10, W2-13) are AUDIT/VERIFY-THEOREM gates that do not require new numerical computation — they are axiom-verification or registry-landing gates. Five (W2-2, W2-3, W2-6, W2-8, W2-9) are VERIFY-THEOREM gates with modest numerical components (HP^k computation, q-deformation scan, registry diff). Two (W2-11, W2-12) carry numerical payloads (triality orbit sum on Jensen spectrum, Leggett-Bogoliubov boundary-vs-detector projection).

**Substrate-first framing**: every hypothesis of this wave starts from D_K eigenvalue spectrum data, or cyclic cohomology HP^k(A_F), or Jensen-deformed SU(3) structure. Nothing in this wave invokes "fields on a curved spacetime"; everything flows FROM the spectral triple TOWARD emergent physics.

**Specialist assignment**: connes-ncg-theorist owns all 13 gates (single-reviewer bucket). Three gates (W2-6 quantum group, W2-10 three-solo convergence, W2-12 band-detector map) suggest cross-specialist consultation (lizzi-spectral-functional-theorist, vdd-bridge-theorist) but the OWNER for each gate is connes-ncg-theorist.

---

## Wave W2 Decision Point Prerequisites

Wave W2 depends on W0 for the CC-family pre-CC diagnostics:

| Prereq | Source wave | Why W2 needs it |
|:-------|:------------|:----------------|
| W0-10 (CC-2 Spin(8) triality orbit sum) | W0 | W2-11 (PRE-CC-2) is the DIAGNOSTIC that precedes W0-10. Strictly speaking W2-11 should be evaluated BEFORE W0-10 is interpreted, but both run in Batch 1. If W2-11 FAILS (triality not preserved), W0-10's PASS/FAIL changes interpretation. Runtime ordering is independent; interpretation ordering is W2-11 → W0-10. |
| W0-11 (CC-3 Connes-Moscovici residue sum) | W0 | W2-5 (PRE-CC-1) and W2-3 (HP^3 extension) feed into CC-3's dimension-spectrum structure. |
| W0-12 (CC-4 Dai-Freed torsion) | W0 | W2-4 (KO-dim 6 sign direction at Higgs) feeds into the Dai-Freed Z/2 class via the η-invariant sign. |
| W0-16 (HP^1(A_F) dimension / generating-set) | W0 | W2-3 (HP^3 extension) builds on W0-16's HP^1 baseline. W2-7 (§VII.P registry landing) depends on the HP^1 dimension count being canonical. |
| W0-23 (CC-1 η-invariant of full Jensen-SU(3) × A_F triple) | W0 | W2-5 (PRE-CC-1 KO-dim constraint on η) is the diagnostic. |

**Runtime independence**: all W0 prereqs are in Batch 1, dispatched simultaneously with W2. Agents must NOT block on cross-wave outputs — each W2 gate uses input-pin SHAs of static canonical files, not runtime-dynamic W0 outputs. W0-interpretation of W2 results is a post-Batch-1 synthesis step, not a runtime dependency.

---

## §W2-1. S85-W2-ALPHA-S-AXIOM-MINIMALITY-AU

**Gate ID**: S85-W2-ALPHA-S-AXIOM-MINIMALITY-AU
**Trigger**: [AUDIT]
**Classification**: GEOMETRIC
**Agent type**: connes-ncg-theorist (solo)

**Hypothesis**: The alpha_s pre-registration pipeline currently invokes a superset of NCG axioms (dim, reg, fin, real, 1st-order, orient, PD); the minimal subset sufficient to PIN alpha_s is strictly smaller. Claim: alpha_s requires only {dim, reg, fin, real, 1st-order}; it does NOT require {orientability, Poincaré duality} because alpha_s is a 2nd spectral moment (a_4 coefficient), not a topological class.

**Method**:
- Import `from canonical_constants import *` at top of script.
- CPU-only (audit, no heavy linear algebra).
- Script: `computations/s85_w2_alpha_s_axiom_minimality.py`
- Read the 7-axiom checklist from the permanent-results-registry (source: `sessions/framework/permanent-results-registry.md`, §"NCG axiom roster").
- For each of the 7 axioms, read-only trace: does the alpha_s derivation (W3-G54 HP^even audit method applied to the a_4 coefficient) invoke this axiom? Produce a 7-row table: `{axiom, invoked (Y/N), invocation site, structural dependency}`.
- Emit closure JSON `s85_w2_alpha_s_axiom_minimality.json` recording the subset used.
- Output files: `s85_w2_alpha_s_axiom_minimality.py`, `s85_w2_alpha_s_axiom_minimality.json`.

**Machinery pin (PRDR)**:
- `N_eval`: N/A (audit gate; no eigenvalue evaluation)
- `L_max`: N/A
- `scan_range`: N/A
- `step_size`: N/A
- `tolerance`: N/A (binary Y/N per axiom)
- `scheme`: "axiom-invocation-trace"
- `convention`: Chamseddine-Connes-Marcolli 2007 axiom list (§1.12-§1.20)
- `random_seed`: N/A
- `GPU path`: none (CPU-only audit)
- Input SHA-256 pins:
  - `sessions/framework/permanent-results-registry.md`: `<computed-at-runtime>`
  - `researchers/Connes/` axiom roster: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<subset_cardinality>, scheme=axiom-invocation-trace, convention=CCM-2007, L_max=N/A)` where `subset_cardinality` is the number of axioms invoked (expected: 5 of 7).

**PASS/FAIL/INFO thresholds**:
- **PASS**: subset_cardinality ≤ 5, i.e. at least 2 axioms (orient, PD) are unused by alpha_s derivation → minimality audit SUCCEEDS (strict subset found).
- **FAIL**: subset_cardinality = 7 → all axioms invoked → no minimality gain, but informative.
- **INFO**: subset_cardinality = 6 → only one axiom is non-minimal; marginal case.

**Substitution chain**: N/A — this is an [AUDIT] gate, not a [SIGN] or [VERIFY] with sign-direction claim. Audit tallies Y/N per axiom with no algebraic direction flow.

**What PASS means**: The alpha_s derivation is robust to relaxations of the orientability / Poincaré duality axioms. This opens a corridor for alpha_s in Pati-Salam extensions where PD may be replaced by a weaker pairing.
**What FAIL means**: alpha_s is structurally coupled to the full 7-axiom set; no corridor for alpha_s under weaker NCG assumptions.

**Effort**: LIGHT (audit-only, 15-30 min, no numerics).

**Substrate framing reminder**: alpha_s is the value of the a_4 Seeley-DeWitt coefficient at the CC-coupling scale. The axiom audit asks which PIECES of the spectral triple (A, H, D) are load-bearing for a_4. We are NOT asking whether alpha_s is "consistent with QFT" — we are asking which axioms of the substrate define it.

---

## §W2-2. S85-W2-CROSS-SESSION-THEOREM-FAMILY

**Gate ID**: S85-W2-CROSS-SESSION-THEOREM-FAMILY
**Trigger**: [VERIFY-THEOREM]
**Classification**: GEOMETRIC
**Agent type**: connes-ncg-theorist (solo)

**Hypothesis**: The S83 Cartan Level-2 Exclusion (§VII.J), the S84 Three-Layer Regulator (§VII.M/N, L1 ζ / L2 Zubarev / L3 per-Q span), and the S83 HP^even completeness (§VII.K) are *not three separate results* but a **single theorem family** parameterized by (cohomology layer k, regulator class R, fiber group G). Claim: there exists a unified statement of the form "For (A, H, D) satisfying axioms {dim, reg, fin, real, 1st-order}, HP^k-triviality of the fiber sector forces suppression of all R-regulated observables at rank r(G) ≥ r_crit."

**Method**:
- CPU-only (structural theorem-statement gate).
- Script: `computations/s85_w2_theorem_family.py`
- Read the three existing registry entries (§VII.J, §VII.K, §VII.M) from `sessions/framework/permanent-results-registry.md`.
- Extract the (k, R, G, r_crit, conclusion) tuple from each registry row.
- Emit a unified statement: parameterized template + three instantiations proving the three existing theorems fall out.
- Output files: `s85_w2_theorem_family.py`, `s85_w2_theorem_family_statement.tex`, `s85_w2_theorem_family_verification.json`.

**Machinery pin (PRDR)**:
- `N_eval`: N/A
- `L_max`: N/A
- `scan_range`: (k ∈ {1,2,3}, R ∈ {ζ, Zubarev, per-Q-span}, G ∈ {simply-laced A_n, D_n, E_n, non-simply-laced B_n, C_n, G_2, F_4})
- `step_size`: N/A
- `tolerance`: THEOREM (either the unified statement subsumes all three, or it does not)
- `scheme`: "theorem-family-unification"
- `convention`: Permanent-results-registry §VII.J/K/M canonical statements (S83-W3-G62, S83-W3-G54, S84-W2a-11)
- `random_seed`: N/A
- `GPU path`: none
- Input SHA-256 pins:
  - `sessions/framework/permanent-results-registry.md` §VII.J/K/M: `<computed-at-runtime>`
  - `.claude/agent-memory/connes-ncg-theorist/s83-w3-g62-vii-j-landing.md`: `<computed-at-runtime>`
  - `.claude/agent-memory/connes-ncg-theorist/s83-w3-g54-hp-even-audit.md`: `<computed-at-runtime>`
  - `.claude/agent-memory/connes-ncg-theorist/s84-w2a-11-vii-m-landing.md`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<family_member_count>, scheme=theorem-family-unification, convention=registry-§VII-unified, L_max=N/A)` where `family_member_count = 3` if the unification subsumes the three existing theorems and `< 3` otherwise.

**PASS/FAIL/INFO thresholds**:
- **PASS**: family_member_count = 3 AND the unified statement is strictly more general (at least one new instantiation outside §VII.J/K/M is predicted).
- **FAIL**: family_member_count < 3 (at least one existing theorem is NOT an instantiation of the proposed family) → the three theorems are genuinely separate.
- **INFO**: family_member_count = 3 but no new instantiations predicted → family exists but is tautological (no predictive power).

**Substitution chain**: N/A — [VERIFY-THEOREM] gate, structural, no sign/direction claim.

**What PASS means**: S83-S84 produced not three theorems but one theorem + three corollaries. This is a major structural consolidation of the permanent-results-registry.
**What FAIL means**: The three theorems have genuinely distinct algebraic origins; no unification. This is *also* a permanent structural result — it constrains future theorem-hunting away from attempting further unification.

**Effort**: MODERATE (structural theorem-statement + three-verification proofs; 2-3 hours no-compute).

**Substrate framing reminder**: The cohomology classes HP^k(A_F) ARE the substrate — they are the homological structure of the internal algebra of the spectral triple. The unification asks: is there one substrate property that governs three separate observational consequences? If so, the substrate is even more rigid than we thought.

---

## §W2-3. S85-W2-HP3-DISJOINT-CORRIDOR-THREE-WAY

**Gate ID**: S85-W2-HP3-DISJOINT-CORRIDOR-THREE-WAY
**Trigger**: [VERIFY-THEOREM]
**Classification**: GEOMETRIC
**Agent type**: connes-ncg-theorist (solo, may consult lizzi on HP^k computation)

**Hypothesis**: §VII.P (Cohomology-Disjoint-Corridor Theorem, S84) states that HP^2-disjoint corridors in A_F support distinct spectral-functional signatures (pairwise). Claim: this extends to HP^3-disjoint *triples* — given three corridors C_1, C_2, C_3 satisfying HP^3(C_i ∩ C_j) = 0 for all i ≠ j, the three corridors carry distinguishable spectral-functional signatures IN EVERY TRIPLE COINCIDENCE POINT of the observational Fisher matrix.

**Method**:
- CPU-only for HP^3 symbolic computation; GPU (torch.linalg) if any eigenvalue projection onto triple-intersection subspace is needed.
- Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"` — GPU path via `torch.linalg` only if triple-projection operator D^3_triple has dim ≥ 100.
- Script: `computations/s85_w2_hp3_disjoint_corridor.py`
- Given A_F = C ⊕ H ⊕ M_3(C), enumerate pairwise-HP^2-disjoint corridor set from §VII.P. For each triple (C_i, C_j, C_k), compute HP^3(C_i ∩ C_j ∩ C_k) using the Hochschild complex on the mutual-intersection subalgebra.
- If HP^3 = 0 for all triples, the "three-way" extension holds trivially. If HP^3 ≠ 0 for some triple, produce the obstruction class explicitly.
- Output files: `s85_w2_hp3_disjoint_corridor.py`, `s85_w2_hp3_disjoint_corridor.npz` (Hochschild cochain matrices), `s85_w2_hp3_disjoint_corridor.png` (triple-intersection lattice diagram).

**Machinery pin (PRDR)**:
- `N_eval`: N/A (symbolic HP^3 computation, not eigenvalue sum)
- `L_max`: N/A
- `scan_range`: all ordered triples (i, j, k) with i < j < k from the §VII.P corridor list (expected 6-10 triples depending on §VII.P enumeration)
- `step_size`: N/A
- `tolerance`: THEOREM (dim HP^3 = 0 or > 0 exactly)
- `scheme`: "hochschild-triple-intersection"
- `convention`: CM-2008 cyclic-cohomology computation conventions; agreement with Loday (1992) Ch. 2 on HP^k for direct sums
- `random_seed`: N/A (symbolic)
- `GPU path`: only if dim(triple-intersection subalgebra) ≥ 100 (unlikely for A_F = C ⊕ H ⊕ M_3(C); realistically stays CPU-only symbolic)
- Input SHA-256 pins:
  - §VII.P canonical statement (permanent-results-registry): `<computed-at-runtime>`
  - `.claude/agent-memory/connes-ncg-theorist/s83-w3-g62-vii-j-landing.md`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<num_nontrivial_HP3_obstructions>, scheme=hochschild-triple-intersection, convention=CM-2008, L_max=N/A)` where value = 0 (extension holds) or > 0 (extension fails for specific triples).

**PASS/FAIL/INFO thresholds**:
- **PASS**: num_nontrivial_HP3_obstructions = 0 → extension holds for all triples → §VII.P strengthens to HP^3.
- **FAIL**: num_nontrivial_HP3_obstructions ≥ 1 → extension fails → §VII.P stays pairwise. This is informative — identifies which triples carry Hochschild obstructions.
- **INFO**: N/A (binary)

**Substitution chain**: N/A — [VERIFY-THEOREM] gate.

**What PASS means**: Three-way corridor separation is as strong as pairwise → Fisher-matrix triple coincidence points CANNOT confuse three corridors simultaneously. Strongest possible statement of the Disjoint-Corridor Theorem.
**What FAIL means**: Some triples do share HP^3 structure → three-way separation not guaranteed → Fisher-matrix triple coincidence points may confuse. Identifies specific experimental regimes where corridor ambiguity persists.

**Effort**: MODERATE-HEAVY (symbolic Hochschild computation on direct-sum algebra; 3-5 hours compute + proof writeup).

**Substrate framing reminder**: "Corridor" here is a sub-algebra of A_F = C ⊕ H ⊕ M_3(C), i.e. a substructure of the substrate's internal algebra. HP^3-disjointness is a statement about the substrate's OWN Hochschild homology. "Three observational corridors are distinguishable" is the EMERGENT consequence; the substrate property is "three sub-algebras have trivial mutual HP^3".

---

## §W2-4. S85-W2-KO6-HIGGS-SIGN-DIRECTION

**Gate ID**: S85-W2-KO6-HIGGS-SIGN-DIRECTION
**Trigger**: [SIGN]
**Classification**: PARTICLE
**Agent type**: connes-ncg-theorist (solo)

**Hypothesis**: The KO-dimension 6 signature (ε, ε', ε'') = (+1, +1, −1) enforces a SPECIFIC sign in the Higgs mass term generated by the a_2 Seeley-DeWitt coefficient. Claim: the Higgs quadratic μ^2 |H|^2 has coefficient sign = −ε'' × (trace-sign of Jensen-SU(3) × A_F) = +1 × (+1) = +1 in the convention where V(H) = μ^2 |H|^2 + λ |H|^4, μ^2 < 0 at the physical electroweak vacuum.

**Method**:
- CPU-only (sign-flow tracing through the J, γ, ε'' algebra).
- Script: `computations/s85_w2_ko6_higgs_sign.py`
- Import `J_C2` from `canonical_constants` (see `.claude/agent-memory/connes-ncg-theorist/` for J convention).
- Compute ε = J^2 = +1 (KO-6 row), ε' = (Jγ = ε''γJ coefficient) = −1 (KO-6), ε'' = JD = ε' DJ coefficient = +1 (KO-6).
- Trace the sign through the a_2 coefficient: a_2 ⊃ −(1/12) R |H|^2 + (terms from [J, D, γ])) → extract μ^2 sign.
- Verify against Chamseddine-Connes 2010 (Phys. Rev. D 82, 085015) Higgs-mass derivation, §IV eq. 4.15.
- Output files: `s85_w2_ko6_higgs_sign.py`, `s85_w2_ko6_higgs_sign_trace.json`.

**Machinery pin (PRDR)**:
- `N_eval`: N/A
- `L_max`: N/A
- `scan_range`: N/A (single sign-flow trace)
- `step_size`: N/A
- `tolerance`: ABSOLUTE (sign is +1 or −1, no margin)
- `scheme`: "ko6-sign-flow"
- `convention`: Chamseddine-Connes-Marcolli 2007 (ε, ε', ε'') KO-6 row = (+, +, −); AC-2010 Higgs-mass extraction
- `random_seed`: N/A
- `GPU path`: none
- Input SHA-256 pins:
  - `canonical_constants.py::J_C2`: `<computed-at-runtime>`
  - CCM-2007 KO-dim table (paper file in `researchers/Connes/`): `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<mu2_sign_in_convention>, scheme=ko6-sign-flow, convention=CCM-2007/AC-2010, L_max=N/A)` where value ∈ {−1, +1}; expected value = −1 (physical EWSB vacuum).

**PASS/FAIL/INFO thresholds**:
- **PASS**: mu2_sign = −1 exactly (matches physical EWSB).
- **FAIL**: mu2_sign = +1 (unbroken EW vacuum, contradicts observation).
- **INFO**: N/A (binary).

**Substitution chain** (MANDATORY for [SIGN] gate):
```
Step 1: Define ε = J² (KO-6 row of Table 1, CCM-2007, eq. 1.158)
Step 2: Define ε' = coefficient in Jγ = ε' γ J (KO-6 row of same table)
Step 3: Define ε'' = coefficient in JD = ε'' D J (KO-6 row)
Step 4: Read the KO-6 row: (ε, ε', ε'') = (+1, +1, −1)   [definition, not derivation]
Step 5: In the finite spectral triple (A_F, H_F, D_F) with H_F = C^32 and D_F carrying the Yukawa + Majorana blocks, the Higgs-quadratic term in a_2 is:
        μ² |H|² coefficient = −(ε'' × Tr_F[Y†Y])/(internal normalization)
        where Y is the Yukawa matrix (Chamseddine-Connes 2010, eq. 4.15)
Step 6: Substitute ε'' = −1 (from Step 4, KO-6 row):
        μ² |H|² coefficient = −(−1) × Tr_F[Y†Y]/N = +Tr_F[Y†Y]/N
Step 7: But Tr_F[Y†Y] is a sum of squared Yukawas, which is strictly > 0.
        Therefore bare μ² coefficient from a_2 is POSITIVE.
Step 8: EWSB requires physical μ² < 0 at the physical vacuum. The bare sign from a_2 is POSITIVE — this is flipped by the a_4 correction (Higgs quartic) via RG flow (Chamseddine-Connes 2010 §V, eq. 5.12).
Step 9: Read off: the KO-6 signature directly enters ε'' = −1; this forces the bare a_2 Higgs-quadratic sign to +1; physical μ² < 0 requires the a_4 RG flow to flip the sign. The SIGN-DIRECTION CLAIM is: "KO-6 forces a_2-bare μ² > 0, RG-corrected μ² < 0 at physical vacuum".
Conclusion: mu2_sign_in_convention (bare, a_2) = +1; mu2_sign_in_convention (RG-corrected, physical) = −1. The gate's expected output must specify which.
```

The expected output in PASS/FAIL thresholds refers to BARE a_2 sign (before RG) → mu2_sign_bare = +1; physical vacuum is separate question closed by RG flow (not in this gate's scope).

**REVISED PASS/FAIL** (in light of substitution chain):
- **PASS**: mu2_sign_bare = +1 AND the script outputs both bare (+1) and RG-corrected (−1) values, matching AC-2010.
- **FAIL**: mu2_sign_bare = −1 (KO-6 signature does not flip through ε'') → sign flow is broken.

**What PASS means**: The KO-6 signature (+, +, −) and the Chamseddine-Connes Higgs-mass derivation AC-2010 §IV are mutually consistent at the sign-flow level. Higgs sector substrate-derivation is sign-certified.
**What FAIL means**: The sign-flow through J, γ, ε'' has an error in the Connes framework's treatment of KO-6 for the finite spectral triple — this would be a foundational anomaly requiring re-derivation.

**Effort**: LIGHT-MODERATE (2-3 hours: trace sign through AC-2010 eqs., cross-check against CCM-2007 table 1).

**Substrate framing reminder**: The Higgs field is not a fundamental scalar "added" to spacetime. It is the inner-fluctuation component of D_F in the A_F direction. The sign of μ² is fixed by the KO-6 signature of the substrate, not by QFT ad-hocery.

---

## §W2-5. S85-W2-PRE-CC-1-KO6-ON-ETA

**Gate ID**: S85-W2-PRE-CC-1-KO6-ON-ETA
**Trigger**: [VERIFY]
**Classification**: GEOMETRIC
**Agent type**: connes-ncg-theorist (solo)

**Hypothesis**: Before W0-23 CC-1 (η-invariant of the full Jensen-SU(3) × A_F triple) can be interpreted, the KO-dim=6 constraint on η must be verified. Specifically: for a KO-6 triple (A, H, D), the spectral η-invariant η(D, s=0) is valued in {0, 1/2} mod Z (APS boundary theorem + KO-6 reality condition). Claim: the η-invariant of Jensen-SU(3) × A_F is constrained to {0, 1/2} mod Z; no other value is admissible.

**Method**:
- CPU-only (constraint verification, not η computation; the η value itself is computed in W0-23 CC-1).
- Script: `computations/s85_w2_pre_cc1_ko6_on_eta.py`
- Verify: (i) J^2 = +1 for product triple (Jensen-SU(3) × A_F), (ii) Jγ = +γJ (KO-6 row), (iii) JD = −DJ (KO-6 row).
- Derive: under these constraints, η(D, 0) ∈ {0, 1/2} mod Z (APS + anti-commutation of J with D forces η = η̄ (complex conjugate) AND Jγ = γJ forces η + η̄ = η (self-conjugate), giving 2η ∈ Z, so η ∈ {0, 1/2} mod Z).
- Output files: `s85_w2_pre_cc1_ko6_on_eta.py`, `s85_w2_pre_cc1_ko6_on_eta.json`.

**Machinery pin (PRDR)**:
- `N_eval`: N/A
- `L_max`: N/A (constraint gate; η is NOT computed here)
- `scan_range`: N/A
- `step_size`: N/A
- `tolerance`: ABSOLUTE (3 algebraic identities must hold exactly)
- `scheme`: "ko6-eta-constraint-verification"
- `convention`: Atiyah-Patodi-Singer (APS) η-invariant normalization; CCM-2007 KO-6 signature
- `random_seed`: N/A
- `GPU path`: none
- Input SHA-256 pins:
  - `canonical_constants.py::J_C2`: `<computed-at-runtime>`
  - CCM-2007 KO-dim table: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<constraint_cardinality>, scheme=ko6-eta-constraint-verification, convention=APS+CCM-2007, L_max=N/A)` where value ∈ {0, 1, 2, 3} is the number of KO-6 algebraic identities verified; expected = 3.

**PASS/FAIL/INFO thresholds**:
- **PASS**: constraint_cardinality = 3 AND the derivation "2η ∈ Z" follows from the 3 identities.
- **FAIL**: constraint_cardinality < 3 (at least one identity fails) → Jensen-SU(3) × A_F is NOT a KO-6 triple → CC-1 gate in W0 requires re-scoping.
- **INFO**: N/A (binary).

**Substitution chain** (MANDATORY for [VERIFY] with constraint-derivation):
```
Step 1: For KO-6 triple, the APS η-invariant satisfies η(D*, 0) = η̄(D, 0) (complex conjugate under adjoint).
Step 2: Since D is self-adjoint on a real K-theoretic Hilbert space, η(D, 0) is real.
Step 3: KO-6 implies Jγ = γJ and JD = -DJ (from KO-6 row of CCM-2007 Table 1).
Step 4: Under J, eigenvalues of D pair up: D|λ⟩ = λ|λ⟩ → D(J|λ⟩) = JDJ^{-1}(J|λ⟩) = -λ(J|λ⟩) [using JD = -DJ].
        Therefore eigenvalues come in pairs (λ, -λ) → spectrum is symmetric about zero.
Step 5: η(D, 0) = (1/2)[η̃(D, 0) + dim ker(D)] where η̃ is the regularized sum over nonzero eigenvalues sign(λ) |λ|^{-s}|_{s=0}.
        Step 4 implies η̃(D, 0) = 0 (odd function over symmetric spectrum).
Step 6: Substitute into Step 5: η(D, 0) = dim(ker D)/2.
Step 7: dim(ker D) is an integer ≥ 0.
        Therefore η(D, 0) = k/2 for some k ∈ Z_{≥0}, i.e. η(D, 0) ∈ (1/2) Z.
Step 8: Modulo Z: η(D, 0) mod Z ∈ {0, 1/2}.
Conclusion: CONSTRAINT VERIFIED. η-invariant of a KO-6 triple is valued in {0, 1/2} mod Z, under the three KO-6 identities plus self-adjointness of D.
```

**What PASS means**: W0-23 CC-1 η-computation is constrained to return 0 or 1/2 mod Z. Any other value → computational bug in W0-23, not substrate claim. This is a physically meaningful Z/2 class (it is the Dai-Freed class referenced in CC-4, W0-12).
**What FAIL means**: Jensen-SU(3) × A_F fails one of the three KO-6 identities → the "full triple" is not KO-6 in the naive product sense → CC-1, CC-2, CC-3, CC-4 all require re-scoping. FAIL here is a major structural result.

**Effort**: LIGHT (3 algebraic identity checks, ~1 hour).

**Substrate framing reminder**: η is not a "twist" added to D. It is an intrinsic spectral invariant of the substrate's Dirac operator. The constraint "η ∈ {0, 1/2}" is a substrate geometry statement that forces the emergent Z/2 class (the Dai-Freed torsion anomaly of CC-4) to be Z/2, not Z/n for any other n.

---

## §W2-6. S85-W2-QUANTUM-DISJOINT-CORRIDOR

**Gate ID**: S85-W2-QUANTUM-DISJOINT-CORRIDOR
**Trigger**: [VERIFY-THEOREM]
**Classification**: GEOMETRIC
**Agent type**: connes-ncg-theorist (solo; S83-W2-G20 quantum Cartan protection provides the baseline method)

**Hypothesis**: The §VII.P Disjoint-Corridor Theorem (formulated for classical A_F = C ⊕ H ⊕ M_3(C)) extends to the q-deformed setting: for A_F^q := U_q(C ⊕ H ⊕ M_3(C)) (or more precisely, A_F deformed at each simple factor where applicable), HP^2-disjoint corridors remain HP^2-disjoint at generic q ∈ (0, 1) ∪ (1, ∞), q not a root of unity.

**Method**:
- CPU-only (cyclic-cohomology HKR + SBI spectral sequence at generic q).
- Script: `computations/s85_w2_quantum_disjoint_corridor.py`
- Extend the S83-W2-G20 quantum Cartan protection method (HKR + SBI, H^2_dR(S^1_q) = 0 at generic q) to the A_F^q direct sum.
- 4-route confluence requirement (per S83 agent-memory `s83-w2-g20-quantum-cartan-protection.md`): (i) HKR + SBI at q = e^{iπ/N}, (ii) H^2_dR(S^1_q) = 0 via Woronowicz differential calculus, (iii) q-scan over q ∈ {0.8, 0.9, 1.1, 1.2} at generic values, (iv) pullback kills quantum volume-class.
- Output files: `s85_w2_quantum_disjoint_corridor.py`, `s85_w2_quantum_disjoint_corridor.npz` (q-scan HP^2 tables), `s85_w2_quantum_disjoint_corridor.png` (q-scan plot).

**Machinery pin (PRDR)**:
- `N_eval`: N/A (HP^2 symbolic)
- `L_max`: N/A
- `scan_range`: q ∈ {0.70, 0.80, 0.90, 0.95, 0.99, 1.01, 1.05, 1.10, 1.25, 1.50} (10 generic values, none root-of-unity)
- `step_size`: variable (enumerated)
- `tolerance`: THEOREM (dim HP^2 = 0 at each q-value for each disjoint corridor pair)
- `scheme`: "q-deformed-HKR-SBI"
- `convention`: Connes-Moscovici cyclic cohomology conventions; Woronowicz differential calculus on SU_q(2); S83-W2-G20 method
- `random_seed`: N/A (symbolic)
- `GPU path`: none
- Input SHA-256 pins:
  - `.claude/agent-memory/connes-ncg-theorist/s83-w2-g20-quantum-cartan-protection.md`: `<computed-at-runtime>`
  - §VII.P canonical statement (permanent-results-registry): `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<q-values_where_HP2_nonzero>, scheme=q-deformed-HKR-SBI, convention=CM-cyclic+Woronowicz, L_max=N/A)` where value = 0 (corridor disjointness preserved at all generic q) or > 0 (some q-values break disjointness).

**PASS/FAIL/INFO thresholds**:
- **PASS**: q-values_where_HP2_nonzero = 0 across the full 10-value scan AND at least 3 of the 4 confluence routes agree.
- **FAIL**: q-values_where_HP2_nonzero ≥ 1 OR fewer than 3 confluence routes agree.
- **INFO**: PASS at generic q-values but at least one root-of-unity in the scan carries nonzero HP^2 (expected — quantum protection weakens at roots of unity; this is a sanity check, not a gate failure).

**Substitution chain**: N/A — [VERIFY-THEOREM].

**What PASS means**: The Disjoint-Corridor Theorem is robust to quantum deformation of the substrate. The Z_2 spin structure of the fiber survives into the quantum (non-commutative) generalization. This opens a corridor for *quantum* substrate models (e.g. Majid-Connes 2019 noncommutative Standard Model).
**What FAIL means**: §VII.P is a CLASSICAL statement only; quantum deformation breaks corridor separation. Restricts the theorem's scope.

**Effort**: MODERATE (4-route confluence, following S83-W2-G20 template; 3-4 hours).

**Substrate framing reminder**: "Quantum deformation" here is deformation of the substrate's internal algebra A_F, NOT a "quantization of gravity". The substrate structure itself becomes non-commutative at a deeper level; emergent physics inherits the deformation.

---

## §W2-7. S85-W2-DISJOINT-CORRIDOR-REGISTRY-LANDING

**Gate ID**: S85-W2-DISJOINT-CORRIDOR-REGISTRY-LANDING
**Trigger**: [AUDIT]
**Classification**: META
**Agent type**: connes-ncg-theorist (solo)

**Hypothesis**: §VII.P (Cohomology-Disjoint-Corridor Theorem, S84) needs a counter-construction audit before landing in the permanent-results-registry. Audit claim: the §VII.P theorem survives a counter-construction attempt that tries to build a pair of corridors (C_a, C_b) with HP^2(C_a ∩ C_b) = 0 but identical spectral-functional signatures. If such a pair exists, §VII.P is FALSE; if no such pair exists after systematic search, §VII.P is promoted to the registry.

**Method**:
- CPU-only.
- Script: `computations/s85_w2_disjoint_corridor_counter_construction.py`
- Enumerate all pairs (C_a, C_b) of 2-element corridors from the §VII.P corridor set with HP^2(C_a ∩ C_b) = 0.
- For each pair, evaluate spectral-functional signatures (a_0, a_2, a_4 values on Jensen-SU(3) × C_a vs × C_b).
- If any pair has matching (a_0, a_2, a_4) to within machine precision, §VII.P FAILS (counter-example found).
- Output files: `s85_w2_disjoint_corridor_counter_construction.py`, `s85_w2_disjoint_corridor_counter_construction.npz`, `s85_w2_disjoint_corridor_counter_construction.png`.

**Machinery pin (PRDR)**:
- `N_eval`: N/A at HP^2 level; eigenvalue sums for (a_0, a_2, a_4) use `N_eval = M_KK` from canonical_constants
- `L_max`: 8 (for Jensen-SU(3) spectrum truncation)
- `scan_range`: all corridor pairs (i, j) with i < j from §VII.P list with HP^2(C_i ∩ C_j) = 0
- `step_size`: N/A (pair enumeration)
- `tolerance`: RATIO 1e-8 per Seeley-DeWitt coefficient; ABSOLUTE "different" if any coefficient differs by > 1e-8 relative
- `scheme`: "counter-construction-spectral-moment-match"
- `convention`: Seeley-DeWitt a_k coefficients in CCM-2007 normalization
- `random_seed`: N/A (deterministic enumeration)
- `GPU path`: GPU (torch.linalg) for Jensen-SU(3) spectrum eigenvalues when matrix dim ≥ 100
- Input SHA-256 pins:
  - §VII.P canonical statement: `<computed-at-runtime>`
  - Jensen-SU(3) spectrum at L_max=8: `<computed-at-runtime>`
  - `canonical_constants.py::M_KK, tau_fold`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<num_counter_examples>, scheme=counter-construction-spectral-moment-match, convention=CCM-2007, L_max=8)` where value = 0 (no counter-examples → §VII.P holds → landing proceeds) or > 0 (counter-examples → §VII.P FALSE → landing blocked).

**PASS/FAIL/INFO thresholds**:
- **PASS**: num_counter_examples = 0 → §VII.P survives counter-construction → permanent-results-registry landing APPROVED.
- **FAIL**: num_counter_examples ≥ 1 → §VII.P FALSE → registry landing BLOCKED, counter-example published as new structural constraint.
- **INFO**: N/A.

**Substitution chain**: N/A — [AUDIT].

**What PASS means**: §VII.P joins the permanent-results-registry. Disjoint-corridor separability is now a canonical substrate-property referenced in future theorem-proving.
**What FAIL means**: §VII.P is FALSE. The framework discovers a counter-example where two corridors look spectrally identical despite HP^2-disjointness → a NEW structural constraint ("HP^2-disjointness is insufficient for spectral separability"). This is a stronger (negative) result than FAIL normally indicates.

**Effort**: MODERATE (pair enumeration + spectral-moment computation at L_max=8; 2-3 hours with GPU).

**Substrate framing reminder**: A "counter-construction" is an attempt to falsify a substrate property by finding two internal algebra configurations that are spectrally indistinguishable. If found, it means the substrate's HP^2 structure is less rigid than we thought.

---

## §W2-8. S85-W2-ALPHA-S-PRE-REG-REGISTRY-LANDING

**Gate ID**: S85-W2-ALPHA-S-PRE-REG-REGISTRY-LANDING
**Trigger**: [AUDIT]
**Classification**: META
**Agent type**: connes-ncg-theorist (solo; coordinate with mack-cosmic-bridge on observational side)

**Hypothesis**: The alpha_s pre-registrations scattered across S82-S84 (CMB-S4 flagship, CMB-HD MacInnis-explicit, LiteBIRD Hazumi-verified, joint Fisher correlated, prior-range LCDM, transit PS-67 simultaneous) need consolidation under a single registry section §VII.M.2 (Event-driven pre-registrations). The audit verifies no contradictions exist between the 8 individual pre-registrations.

**Method**:
- CPU-only.
- Script: `computations/s85_w2_alpha_s_pre_reg_landing.py`
- Collect the 8 pre-registrations (W0 CMB-S4, W1a ALPHA-S-REGISTRY-UPGRADE, W1b multiple) from plan files and S82-S84 session files.
- For each: extract (channel, central, 1σ, 2σ, pass-range, fail-range, prior).
- Verify: no two pre-registrations assign contradictory pass-bands to the same observable.
- Emit §VII.M.2 registry section draft.
- Output files: `s85_w2_alpha_s_pre_reg_landing.py`, `s85_w2_alpha_s_pre_reg_landing_section.md`.

**Machinery pin (PRDR)**:
- `N_eval`: N/A
- `L_max`: N/A
- `scan_range`: N/A (consolidation, not scan)
- `step_size`: N/A
- `tolerance`: THEOREM (pre-reg consolidation is complete and consistent)
- `scheme`: "pre-reg-consolidation-audit"
- `convention`: Permanent-results-registry §VII.M.2 schema (to be defined in this gate)
- `random_seed`: N/A
- `GPU path`: none
- Input SHA-256 pins:
  - 8 alpha_s pre-reg items (W0, W1a, W1b, this wave): `<computed-at-runtime>`
  - S82 CMB-S4 flagship doc: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<num_contradictions>, scheme=pre-reg-consolidation-audit, convention=registry-§VII.M.2, L_max=N/A)` where value = 0 (consolidation proceeds) or > 0 (contradictions found → blocks landing).

**PASS/FAIL/INFO thresholds**:
- **PASS**: num_contradictions = 0 → §VII.M.2 section drafted and ready for registry commit.
- **FAIL**: num_contradictions ≥ 1 → at least two alpha_s pre-registrations contradict → resolution required before landing.
- **INFO**: PASS with ≥1 pre-registration carrying a documentation gap (missing prior, missing 2σ band) — landing proceeds with gap note.

**Substitution chain**: N/A — [AUDIT].

**What PASS means**: §VII.M.2 is the canonical registry section for all alpha_s event-driven pre-registrations. Future sessions cite §VII.M.2 without re-enumerating.
**What FAIL means**: The framework's pre-registration hygiene has a bug (two pre-regs assign contradictory pass-bands). Must resolve before landing.

**Effort**: LIGHT-MODERATE (documentation audit, 2 hours).

**Substrate framing reminder**: α_s is the emergent observational quantity from the substrate's a_4 Seeley-DeWitt coefficient. Pre-registrations are how we pin a *future* observational measurement against the substrate's current prediction. Consolidation = tidy record-keeping on substrate-predicted observables.

---

## §W2-9. S85-W2-S50-T15-REGISTRY-UPGRADE

**Gate ID**: S85-W2-S50-T15-REGISTRY-UPGRADE
**Trigger**: [AUDIT]
**Classification**: META
**Agent type**: connes-ncg-theorist (solo)

**Hypothesis**: S50 theorem T15 (currently session-local) meets the canonical-entry criteria (proven, cross-referenced from ≥ 2 later sessions, integrated into ≥ 1 closure chain) and should be promoted to the permanent-results-registry.

**Method**:
- CPU-only.
- Script: `computations/s85_w2_s50_t15_registry_upgrade.py`
- Read S50 theorem T15 statement from `sessions/archive/session-50/`.
- Count cross-references in S51-S84 sessions. Must find ≥ 2.
- Verify T15 appears in at least one closure chain (e.g. from closed mechanisms in permanent-results-registry).
- If all criteria met: emit upgrade diff (T15 → permanent-results-registry §X).
- Output files: `s85_w2_s50_t15_registry_upgrade.py`, `s85_w2_s50_t15_diff.md`.

**Machinery pin (PRDR)**:
- `N_eval`: N/A
- `L_max`: N/A
- `scan_range`: sessions S51-S84 (34 sessions)
- `step_size`: N/A
- `tolerance`: THEOREM (3 criteria: proven, ≥ 2 refs, ≥ 1 closure chain)
- `scheme`: "registry-upgrade-criteria-check"
- `convention`: permanent-results-registry promotion standard (defined in `.claude/rules/` or `sessions/framework/`)
- `random_seed`: N/A
- `GPU path`: none
- Input SHA-256 pins:
  - `sessions/archive/session-50/` T15 statement: `<computed-at-runtime>`
  - S51-S84 session files: `<computed-at-runtime>` (list in script output)

**Expected output 4-tuple**: `(value=<num_criteria_met>, scheme=registry-upgrade-criteria-check, convention=registry-promotion-standard, L_max=N/A)` where value ∈ {0, 1, 2, 3}; expected = 3.

**PASS/FAIL/INFO thresholds**:
- **PASS**: num_criteria_met = 3 → T15 upgraded to permanent-results-registry.
- **FAIL**: num_criteria_met < 3 → T15 stays session-local; document which criterion failed.
- **INFO**: num_criteria_met = 3 but upgrade diff introduces a collision with an existing registry entry — resolve before commit.

**Substitution chain**: N/A — [AUDIT].

**What PASS means**: T15 is now canonical; future work cites it without re-proving.
**What FAIL means**: T15 is not yet canonical; specific criterion (proof gap, insufficient reference count, no closure role) identifies the next step.

**Effort**: LIGHT (audit, 1-2 hours).

**Substrate framing reminder**: T15 is a theorem about substrate structure — the upgrade is administrative (registry hygiene), not new physics. But the criterion "used in ≥ 1 closure chain" ensures only substrate-load-bearing theorems land in the registry.

---

## §W2-10. S85-W2-THREE-SOLO-CONVERGENCE-VERIFY

**Gate ID**: S85-W2-THREE-SOLO-CONVERGENCE-VERIFY
**Trigger**: [VERIFY-THEOREM]
**Classification**: META
**Agent type**: connes-ncg-theorist (solo; this IS the connes-solo re-verification after the Lizzi + VdD solos completed in S84)

**Hypothesis**: The S84 W2a-11 three-solo convergence (Connes + Lizzi + VdD) that landed §VII.M had 4 anchors full-64-char and routed through §VII.N (because §VII.M was occupied by DR3-RESPONSE-PROTOCOL from W1b-9). Claim: with the §VII.N routing now committed, the three-solo convergence is still VALID — no new anchor drift, no theorem-content loss, closure SHA cf3b7443 still reproducible.

**Method**:
- CPU-only.
- Script: `computations/s85_w2_three_solo_convergence_verify.py`
- Re-compute the 4-anchor SHA chain (W1-G1, W1-G3, G57, G58) from the S84 W2a-11 agent-memory note (`.claude/agent-memory/connes-ncg-theorist/s84-w2a-11-vii-m-landing.md`).
- Verify each anchor still produces the full 64-char SHA.
- Verify closure SHA cf3b7443 matches the S84 recorded closure.
- Verify §VII.M / §VII.N routing still coherent (the §VII.M slot remains occupied by DR3-RESPONSE-PROTOCOL; §VII.N holds the three-solo closure).
- Output files: `s85_w2_three_solo_convergence_verify.py`, `s85_w2_three_solo_anchor_sha.json`.

**Machinery pin (PRDR)**:
- `N_eval`: N/A
- `L_max`: N/A
- `scan_range`: 4 anchors (W1-G1, W1-G3, G57, G58)
- `step_size`: N/A
- `tolerance`: ABSOLUTE (SHA-256 byte-exact match)
- `scheme`: "three-solo-sha-reproduction"
- `convention`: S84 W2a-11 closure-protocol (`cf3b7443...`)
- `random_seed`: N/A
- `GPU path`: none
- Input SHA-256 pins:
  - `.claude/agent-memory/connes-ncg-theorist/s84-w2a-11-vii-m-landing.md`: `<computed-at-runtime>`
  - Permanent-results-registry §VII.M and §VII.N: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<num_anchors_verified>, scheme=three-solo-sha-reproduction, convention=S84-W2a-11, L_max=N/A)` where value ∈ {0,1,2,3,4}; expected = 4.

**PASS/FAIL/INFO thresholds**:
- **PASS**: num_anchors_verified = 4 AND closure SHA prefix matches `cf3b7443`.
- **FAIL**: num_anchors_verified < 4 OR closure SHA mismatch → three-solo convergence no longer reproducible → §VII.N landing is unstable.
- **INFO**: N/A.

**Substitution chain**: N/A — [VERIFY-THEOREM] with SHA-reproduction.

**What PASS means**: S84 W2a-11 three-solo closure is stable under §VII.N routing. The Connes + Lizzi + VdD three-specialist convergence is a robust permanent result.
**What FAIL means**: The §VII.N routing broke something the §VII.M landing assumed. Requires re-opening the three-solo collaboration.

**Effort**: LIGHT (SHA reproduction + routing coherence check, 1 hour).

**Substrate framing reminder**: "Three-solo convergence" is a meta-result about how three independent specialists (Connes, Lizzi, VdD) converged on the SAME substrate property from three different methodological starting points. The gate verifies the meta-result holds under plan-routing changes.

---

## §W2-11. S85-W2-PRE-CC-2-TRIALITY-ON-JENSEN

**Gate ID**: S85-W2-PRE-CC-2-TRIALITY-ON-JENSEN
**Trigger**: [VERIFY]
**Classification**: GEOMETRIC
**Agent type**: connes-ncg-theorist (solo)

**Hypothesis**: Before W0-10 (CC-2 Spin(8) triality orbit sum of χ_2) can be interpreted, Spin(8) triality must be verified to be preserved under Jensen deformation of SU(3). Claim: the three outer automorphisms of Spin(8) (two triality + identity) commute with the Jensen-TT deformation operator T_s : SU(3) → SU(3)_s, so triality orbits on the spectrum of D_K(s) are well-defined for all s ∈ [0, s_fold].

**Method**:
- GPU (torch.linalg) for Jensen-SU(3) spectral computation.
- Script: `computations/s85_w2_pre_cc2_triality_jensen.py`
- Compute eigenvalues of D_K on Jensen-SU(3) at L_max = 8 and τ = 0 (baseline) and τ = τ_fold (end of corridor).
- Apply the 3 triality automorphisms of Spin(8) (each permutes the 3 8-dimensional irreps: 8_V, 8_S+, 8_S-).
- For each τ, verify the spectrum is invariant under each triality automorphism (orbit structure preserved).
- Output files: `s85_w2_pre_cc2_triality_jensen.py`, `s85_w2_pre_cc2_triality_jensen.npz`, `s85_w2_pre_cc2_triality_jensen.png`.

**Machinery pin (PRDR)**:
- `N_eval`: 155,984 eigenvalues at L_max = 8 (full Jensen-SU(3) spectrum)
- `L_max`: 8
- `scan_range`: τ ∈ {0.00, 0.05, 0.10, 0.15, 0.190} (baseline + 3 intermediate + fold); 5 points
- `step_size`: τ-step = 0.0475 (not uniform; anchored to τ_fold = 0.190 from canonical_constants)
- `tolerance`: RATIO 1e-10 per eigenvalue (machine precision for triality-invariance)
- `scheme`: "triality-orbit-spectrum-match"
- `convention`: Spin(8) triality via the 8_V, 8_S+, 8_S- outer automorphism acting on the fundamental rep; Jensen-TT from `canonical_constants.py`
- `random_seed`: N/A (deterministic eigensolver)
- `GPU path`: torch.linalg.eigvalsh on 155,984-dim Hermitian D_K (GPU, AMD RX 9070 XT per `.claude/rules/math-scripts.md`)
- Input SHA-256 pins:
  - `canonical_constants.py::tau_fold, M_KK`: `<computed-at-runtime>`
  - Jensen-SU(3) fiber metric at L_max=8: `<computed-at-runtime>`
  - Spin(8) triality generators (canonical convention): `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<max_orbit_deviation>, scheme=triality-orbit-spectrum-match, convention=Spin(8)-triality, L_max=8)` where value is the maximum relative deviation across all eigenvalues and all 5 τ-points between the spectrum and its triality-image; expected value < 1e-10.

**PASS/FAIL/INFO thresholds**:
- **PASS**: max_orbit_deviation < 1e-10 at all 5 τ-points → triality preserved → W0-10 CC-2 computation proceeds as planned.
- **FAIL**: max_orbit_deviation ≥ 1e-10 at any τ-point → triality broken at that τ → W0-10 triality-orbit-sum reinterprets as broken-triality sum.
- **INFO**: max_orbit_deviation ∈ [1e-12, 1e-10] → marginal; possibly numerical precision issue; investigate.

**Substitution chain** (MANDATORY for [VERIFY] with preservation claim):
```
Step 1: Define T_s : SU(3) → SU(3)_s the Jensen-TT deformation at parameter s, with s ∈ [0, s_fold].
        At s = 0, T_0 = id. At s = s_fold, T_s_fold is the fully-deformed fiber.
Step 2: Define triality generators σ_1, σ_2 ∈ Out(Spin(8)) acting on the three 8-dim irreps.
        These are group-level automorphisms of the SU(4) ⊂ Spin(8) that acts on the 8 real coordinates of the A_F embedding.
Step 3: The Jensen deformation acts on the METRIC of SU(3), not on the FIBER STRUCTURE (A_F = C ⊕ H ⊕ M_3(C)).
        Therefore T_s commutes with A_F-level automorphisms by construction.
Step 4: Triality σ_i acts on the Spin(8) sector of A_F (via Spin(8) ⊃ SU(4)_embedding ⊃ SU(3) × U(1)).
        This is an A_F-level automorphism.
Step 5: Substitute Step 3 into Step 4: [T_s, σ_i] = 0 for i = 1, 2.
Step 6: Therefore the spectrum of D_K(s) = D_M(s) ⊗ 1_F + γ_M ⊗ D_F is invariant under σ_i for all s.
        (D_F depends on A_F, σ_i acts trivially on D_F; D_M(s) is Jensen-deformed Dirac on SU(3), independent of σ_i.)
Step 7: Read off direction: spectrum(D_K(s)) = spectrum(σ_i · D_K(s) · σ_i^{-1}) exactly, for all s, for all σ_i.
Conclusion: TRIALITY PRESERVED under Jensen. Numerical test of max_orbit_deviation should return machine-epsilon.
```

**What PASS means**: W0-10 CC-2 χ_2 triality orbit sum is well-defined at all τ in the Jensen corridor. The 3 Spin(8) irreps (8_V, 8_S+, 8_S-) are spectrally degenerate at each τ.
**What FAIL means**: Jensen breaks Spin(8) triality at some τ > 0 → the "orbit sum" in W0-10 does not exist as a single object → CC-2 must be reformulated as a broken-orbit sum. This is a MAJOR substrate discovery (Jensen deformation has more structure than just metric deformation).

**Effort**: MODERATE (GPU eigenvalue at L_max=8 × 5 τ-points; 2-3 hours on AMD RX 9070 XT).

**Substrate framing reminder**: Jensen deformation is a substrate-level deformation of the SU(3) fiber metric. Triality is a substrate-level automorphism of the A_F internal algebra. The gate asks: do the two substrate structures commute? If yes, the substrate has a product-decomposition; if no, there is deeper structural entanglement.

---

## §W2-12. S85-W2-BAND-DETECTOR-MAP-LEGGETT-BOG

**Gate ID**: S85-W2-BAND-DETECTOR-MAP-LEGGETT-BOG
**Trigger**: [VERIFY]
**Classification**: PHONONIC
**Agent type**: connes-ncg-theorist (solo; coordinate with mack-cosmic-bridge on CMB-S4 projection)

**Hypothesis**: The two-scale Leggett-Bogoliubov band structure (L1 acoustic / L2 Leggett sub-leading) maps onto CMB-S4 sensitivity bands (α_s running domain, β_s curvature domain) via a single transfer coefficient T_LB. Claim: T_LB is computable from the substrate spectral triple (no free parameters) and projects the L1/L2 boundary at K_crit onto a specific l-value in CMB-S4 sensitivity (expected l_crit ≈ 5000).

**Method**:
- GPU (torch.linalg) for BdG spectrum sampling; CPU for transfer-coefficient evaluation.
- Script: `computations/s85_w2_band_detector_map.py`
- Load BdG band structure (L1 acoustic, L2 Leggett) from S82-S84 canonical spectra.
- Compute K_crit (L1/L2 boundary in K-space) from canonical_constants (K_crit ~ 2.0 per S70-S74).
- Compute T_LB = substrate spectral overlap integral between L1 and L2 band eigenstates.
- Project K_crit to l_crit via the CMB-S4 k-to-l transfer function (Mukhanov-Sasaki at CMB recombination); use k_pivot = 0.05 Mpc^{-1} per canonical_constants.
- Compare l_crit to CMB-S4 sensitivity band (l ∈ [300, 5000]).
- Output files: `s85_w2_band_detector_map.py`, `s85_w2_band_detector_map.npz`, `s85_w2_band_detector_map.png`.

**Machinery pin (PRDR)**:
- `N_eval`: N_eval = M_KK = canonical_constants value
- `L_max`: 10 (for BdG spectrum — matches S74 canonical)
- `scan_range`: K ∈ [K_R5, K_crit] = [1.9222, 2.035] per S80-S84 canonical corridor
- `step_size`: ΔK = 0.01
- `tolerance`: RATIO 10% on l_crit (detector-projection precision; Mukhanov-Sasaki transfer carries ~5% uncertainty at recombination)
- `scheme`: "two-scale-band-to-l"
- `convention`: Mukhanov-Sasaki at CMB recombination; CMB-S4 sensitivity band per Abazajian 2016
- `random_seed`: N/A
- `GPU path`: torch.linalg for BdG spectrum at L_max=10
- Input SHA-256 pins:
  - `canonical_constants.py::M_KK, tau_fold, K_crit, K_R5`: `<computed-at-runtime>`
  - BdG spectrum (L_max=10, tau_fold): `<computed-at-runtime>`
  - CMB-S4 sensitivity table (Abazajian 2016 Table 3): `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<l_crit>, scheme=two-scale-band-to-l, convention=Mukhanov-Sasaki-recomb, L_max=10)` where value is the projected l at K_crit; expected l_crit ∈ [3000, 7000] (CMB-S4 sensitivity band).

**PASS/FAIL/INFO thresholds**:
- **PASS**: l_crit ∈ [300, 5000] AND T_LB computed from substrate (no free parameters) → substrate L1/L2 boundary is detector-accessible.
- **FAIL**: l_crit ∉ [300, 5000] → L1/L2 boundary is outside CMB-S4 sensitivity → no detector prediction.
- **INFO**: l_crit ∈ [5000, 10000] → marginal; requires CMB-HD (not CMB-S4) to detect.

**Substitution chain** (MANDATORY for [VERIFY] with sensitivity-band claim):
```
Step 1: Define K_crit = value of K-parameter where L1 (acoustic) band ends and L2 (Leggett sub-leading) begins. Source: S70-S74 canonical, K_crit ≈ 2.035.
Step 2: Define Mukhanov-Sasaki transfer: k_phys = a(t_recomb) × k_comoving; l = k_phys × D_A (comoving angular-diameter distance to recombination).
Step 3: Define k_comoving at K_crit via the substrate-to-comoving relation: k = K × k_pivot, where k_pivot = 0.05 Mpc^{-1} per canonical_constants (Planck 2018 convention).
Step 4: Substitute K_crit into Step 3: k_phys ≈ K_crit × k_pivot = 2.035 × 0.05 Mpc^{-1} ≈ 0.1018 Mpc^{-1}.
Step 5: Using D_A ≈ 14000 Mpc (Planck 2018 best-fit): l_crit ≈ k_phys × D_A = 0.1018 × 14000 ≈ 1425.
Step 6: Wait — this seems TOO LOW for the "L1/L2 boundary mapped to CMB-S4 band" claim. Re-examine Step 3: the K-parameter in the L1/L2 band structure is NOT the same as the Mukhanov-Sasaki k_comoving. It is the SUBSTRATE K-parameter (ratio of energy scales in BdG band). The map is K_substrate -> k_comoving via: K = k_comoving / k_KK where k_KK is the KK threshold.
Step 7: Substitute correctly: K_crit = k_comoving / k_KK → k_comoving = K_crit × k_KK = 2.035 × (M_KK in inverse-Mpc). Need M_KK value in canonical_constants.
Step 8: If M_KK ≈ 0.001 Mpc^{-1} (a typical KK scale): k_comoving ≈ 0.002 Mpc^{-1}, l ≈ 28. If M_KK ≈ 0.1 Mpc^{-1}: l ≈ 2850. If M_KK ≈ 1 Mpc^{-1}: l ≈ 28500.
Step 9: The script must READ M_KK from canonical_constants (M_KK has fixed value per S80-W0-8 memory: axiomatic sole external pin). Without it, the direction-claim is undetermined.
Step 10: Read off direction: l_crit = K_crit × M_KK × D_A. INCREASING M_KK increases l_crit. The PASS/FAIL decision depends on M_KK being in the specific range where l_crit falls in [300, 5000].
Conclusion: The pre-registered PASS range assumes M_KK is in a specific band. The gate's PASS-threshold [300, 5000] implies 300/(2.035 × 14000) ≤ M_KK ≤ 5000/(2.035 × 14000), i.e. M_KK ∈ [1.05e-2, 1.75e-1] in inverse-Mpc. Run the script; read the substrate M_KK; report.
```

**What PASS means**: The substrate's L1/L2 band structure projects into CMB-S4's l-sensitivity band. This is a ZERO-PARAMETER prediction of a specific l-value at which the acoustic-to-Leggett transition becomes observable.
**What FAIL means**: The substrate's L1/L2 boundary is outside CMB-S4 reach. Identifies a detector gap; would need CMB-HD or LiteBIRD for detection.
**What INFO means**: The boundary is at the CMB-S4/HD transition; requires joint CMB-S4 + CMB-HD analysis.

**Effort**: MODERATE-HEAVY (BdG spectrum at L_max=10 + Mukhanov-Sasaki projection + comparison table; 3-4 hours).

**Substrate framing reminder**: L1 (acoustic) and L2 (Leggett) are two distinct eigenvalue bands of the Bogoliubov-de-Gennes operator on the substrate. The "detector map" asks which l-value of the CMB power spectrum corresponds to the substrate's BdG band boundary. This is a substrate-first prediction: the substrate has a band structure, and the CMB inherits a specific feature at a specific l.

---

## §W2-13. S85-W2-PSG-§11.2-REVISION

**Gate ID**: S85-W2-PSG-SECTION-11-2-REVISION
**Trigger**: [AUDIT]
**Classification**: META
**Agent type**: connes-ncg-theorist (solo)

**Hypothesis**: §11.2 of `sessions/framework/Phononic-Substrate-Geometry.md` (PSG) requires revision to incorporate the S84 three-layer regulator result (§VII.M/N) and the S84 Disjoint-Corridor Theorem (§VII.P). Current §11.2 predates both.

**Method**:
- CPU-only (documentation revision).
- Script: `computations/s85_w2_psg_section_11_2_revision.py` (light helper; most work is in the .md edit).
- Read current `sessions/framework/Phononic-Substrate-Geometry.md` §11.2.
- Draft revised §11.2 incorporating:
  1. S84 §VII.M three-layer regulator (L1 ζ / L2 Zubarev / L3 per-Q-span) — add as sub-section 11.2.X
  2. S84 §VII.P Disjoint-Corridor Theorem — add as sub-section 11.2.Y
  3. Cross-references to S85 W2-7 (disjoint-corridor registry landing) and W2-6 (quantum extension)
- Emit diff for user review BEFORE committing to PSG file.
- Output files: `s85_w2_psg_section_11_2_revision.py`, `s85_w2_psg_section_11_2_diff.md`, `s85_w2_psg_section_11_2_revised.md`.

**Machinery pin (PRDR)**:
- `N_eval`: N/A
- `L_max`: N/A
- `scan_range`: N/A
- `step_size`: N/A
- `tolerance`: THEOREM (revision integrates all 3 new-since-§11.2 items)
- `scheme`: "documentation-revision-audit"
- `convention`: PSG style guide (inferred from current PSG)
- `random_seed`: N/A
- `GPU path`: none
- Input SHA-256 pins:
  - `sessions/framework/Phononic-Substrate-Geometry.md`: `<computed-at-runtime>`
  - permanent-results-registry §VII.M, §VII.N, §VII.P: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<integration_count>, scheme=documentation-revision-audit, convention=PSG-style, L_max=N/A)` where value = 3 (§VII.M/N + §VII.P + cross-refs) or < 3 (some integration missed).

**PASS/FAIL/INFO thresholds**:
- **PASS**: integration_count = 3 → revised §11.2 ready for commit.
- **FAIL**: integration_count < 3 → one or more post-S82 substrate results not integrated → revision incomplete.
- **INFO**: PASS with stylistic gap (e.g. §11.2 length grows > 2x) — flag but proceed.

**Substitution chain**: N/A — [AUDIT].

**What PASS means**: `Phononic-Substrate-Geometry.md` §11.2 is current as of S85 start. Future agents reading §11.2 get the full post-S84 picture.
**What FAIL means**: Documentation drift — §11.2 lags the permanent-results-registry. Future agents may reason from an incomplete substrate description.

**Effort**: LIGHT-MODERATE (documentation revision, 2 hours).

**Substrate framing reminder**: §11.2 IS the substrate-description reference. Revising it is substrate-first discipline — the picture agents carry into future sessions updates to match the post-S84 substrate structure.

---

## Wave W2 → Wave W3 Decision Point

Wave W2 outputs feed into:

| W2 gate | Feeds into | How |
|:--------|:-----------|:----|
| W2-5 (PRE-CC-1 η constraint) | W0-23 (CC-1 η-invariant) | Interpretation filter; W0-23 must return value in {0, 1/2} mod Z |
| W2-11 (PRE-CC-2 triality preservation) | W0-10 (CC-2 triality orbit sum) | Interpretation filter; W0-10 sum is orbit-valid only if W2-11 PASSES |
| W2-3 (HP^3 three-way extension) | W0-11 (CC-3 Connes-Moscovici residue), W0-16 (HP^1 baseline) | Extends the cohomology-disjointness theorem into higher ranks |
| W2-7 (§VII.P registry landing) | Permanent-results-registry | Landing approves use of §VII.P in S86+ theorem proofs |
| W2-10 (three-solo SHA reproduction) | Permanent-results-registry §VII.N stability | Confirms S84 closure is stable |

**No direct dependencies on W3 (landau-origin) or other Batch-1 waves**. W2 is substrate-interior (NCG-heavy) while W3 is substrate-exterior (Landau class). Wave-level orthogonality is preserved by construction.

---

## Wave W2 Machinery-Enumeration Pin

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness, every gate enumerates its PRDR parameters. Summary of machinery parameters across all 13 W2 gates:

| Parameter class | W2-1 | W2-2 | W2-3 | W2-4 | W2-5 | W2-6 | W2-7 | W2-8 | W2-9 | W2-10 | W2-11 | W2-12 | W2-13 |
|:----------------|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:------|:------|:------|:------|
| N_eval          | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | M_KK | N/A  | N/A  | N/A   | 155984| M_KK  | N/A   |
| L_max           | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | 8    | N/A  | N/A  | N/A   | 8     | 10    | N/A   |
| scan_range      | N/A  | N/A  | pair triples | N/A | N/A | 10 q-values | corridor pairs | 8 pre-regs | S51-S84 | 4 anchors | 5 τ-points | K ∈ [R5, crit] | N/A |
| tolerance       | N/A  | THEOREM | THEOREM | ABS sign | ABS cardinality | THEOREM dim=0 | RATIO 1e-8 | THEOREM | THEOREM | SHA-256 byte | RATIO 1e-10 | RATIO 10% l | THEOREM |
| scheme          | axiom-trace | family-unif | HKR-intersect | KO6-sign-flow | KO6-eta-constraint | q-HKR-SBI | counter-construct | pre-reg-consolidation | registry-upgrade | three-solo-SHA | triality-orbit | two-scale-band-to-l | doc-revision |
| convention      | CCM-2007 | registry-§VII-unif | CM-2008 | CCM-2007/AC-2010 | APS+CCM-2007 | CM-cyclic+Woronowicz | CCM-2007 | registry-§VII.M.2 | registry-promote | S84-W2a-11 | Spin(8) | MS-recomb | PSG-style |
| random_seed     | N/A (all gates deterministic) |
| GPU path        | none | none | none | none | none | none | torch.linalg | none | none | none | torch.linalg | torch.linalg | none |
| Agent type      | solo (connes) for all 13 gates |

**PRDR completeness**: every W2 gate has all 9 PRDR parameters either pinned, marked N/A, or enumerated with explicit scan values. No gate is PRU-vulnerable (Class 8).

**GPU allocation** (RX 9070 XT, 17.1 GB VRAM):
- W2-7: ~100 MB (Jensen-SU(3) spectrum at L_max=8, one-shot)
- W2-11: ~500 MB (Jensen-SU(3) spectrum at L_max=8 × 5 τ-points, plus triality projections)
- W2-12: ~300 MB (BdG spectrum at L_max=10)
- Total peak: ~1 GB across the 3 GPU gates; serialization across gates is safe (no two gates run simultaneously since agent is single-threaded at wave level).

**CPU-only gates** (10 of 13): W2-1, W2-2, W2-3, W2-4, W2-5, W2-6, W2-8, W2-9, W2-10, W2-13.

---

## Wave W2 Input-SHA Ledger

All W2 scripts MUST compute and log SHA-256 of the following input files (SHAs marked `<computed-at-runtime>` in the gate blocks above; enumerated here for completeness):

| Input file | Used by gates |
|:-----------|:--------------|
| `computations/canonical_constants.py` | W2-4, W2-5, W2-7, W2-11, W2-12 (via `J_C2`, `M_KK`, `tau_fold`, `K_crit`, `K_R5`) |
| `sessions/framework/permanent-results-registry.md` (full file, or §VII.M/N/P by section) | W2-1, W2-2, W2-3, W2-6, W2-7, W2-8, W2-9, W2-10, W2-13 |
| `sessions/framework/Phononic-Substrate-Geometry.md` | W2-13 |
| `.claude/agent-memory/connes-ncg-theorist/s84-w2a-11-vii-m-landing.md` | W2-2, W2-10 |
| `.claude/agent-memory/connes-ncg-theorist/s83-w3-g62-vii-j-landing.md` | W2-2, W2-3 |
| `.claude/agent-memory/connes-ncg-theorist/s83-w3-g54-hp-even-audit.md` | W2-2 |
| `.claude/agent-memory/connes-ncg-theorist/s83-w2-g20-quantum-cartan-protection.md` | W2-6 |
| Researchers corpus: CCM-2007 NCG-SM paper (`researchers/Connes/`) | W2-1, W2-4, W2-5, W2-7 |
| Researchers corpus: AC-2010 Higgs-mass paper (`researchers/Connes/`) | W2-4 |
| CMB-S4 sensitivity table (Abazajian 2016, `researchers/` or fetched) | W2-12 |
| Jensen-SU(3) fiber metric at L_max=8 (canonical computation-archive) | W2-7, W2-11 |
| BdG spectrum at L_max=10 (canonical computation-archive) | W2-12 |
| Session archives S51-S84 (for cross-reference counts) | W2-9 |

Each script's first 20 stdout lines log the SHA-256 of every input it reads. The final verdict line pins the closure SHA-256 per `.claude/rules/gate-verdicts.md` (S81+ canonical form).

**Verdict-file path**: `computations/s85_gate_verdicts.txt` (single canonical location, per `.claude/rules/gate-verdicts.md`).

---

## Closing note

Wave W2 is substrate-theoretic and axiom-verification-heavy. Eight of 13 gates are AUDIT/VERIFY-THEOREM/META (documentation, registry landing, theorem-family unification, constraint verification). Three are [VERIFY] with numerical payload (W2-5 η-constraint, W2-11 triality, W2-12 band-detector-map). Two are [SIGN] or [AUDIT] with trivial compute (W2-4, W2-7).

No gate in this wave re-runs a previously-closed computation. Every gate either:
  (a) verifies a DIFFERENT predicate on an existing closure (W2-4, W2-5, W2-10, W2-11),
  (b) extends a closed theorem to a broader class (W2-2, W2-3, W2-6),
  (c) promotes session-local to permanent-registry (W2-7, W2-8, W2-9),
  (d) audits minimality or documentation (W2-1, W2-13), or
  (e) makes a new substrate-to-detector prediction (W2-12).

All 13 gates honor the substrate-first framing: D_K eigenvalues → spectral action moments → emergent physics, with no appeal to QFT-in-curved-spacetime ordering.
