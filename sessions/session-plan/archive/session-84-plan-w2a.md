# Session 84 Plan — Wave 2a: §VII.M Theorem + Falsifier + Layer-Pin + L1-L2 Projection (4 gates)

**Wave**: 2a (sub-block of W2 — Three-Layer Regulator Theorem Core)
**Gates**: 4 (W2a-11, W2a-12, W2a-13, W2a-14)
**Parent spec**: `session-84-context.md` §4.B (gates 11-14)
**Planner**: gen-physicist
**Dispatch model**: parallel independent agents (compute mode)
**Framing discipline**: layer theorem IS the substrate's self-determination structure — NOT a property "attributed to" the substrate by external analysis

---

## W2a Summary

This sub-block lands the central structural harvest of S83: the **Three-Layer Regulator Theorem** (§VII.M). The theorem partitions regulator-choice into three strata corresponding to three distinct acts of substrate self-determination:

- **L1 (AXIOMATIC)**: Connes-Dixmier residue theorem — zeta is the unique canonical regulator under Connes axioms A1-A6 (dim-summability, reality, first-order, orientability, Poincaré duality, regularity). S83 W1-G3 PASS, sha=2343920a....
- **L2 (SUBSTRATE-ACTION)**: Zubarev is the unique regulator satisfying three substrate-action criteria at L_max=5, τ_fold=0.19: integrability + local-minimum-in-τ + chirality χ=+1. S83 W1-G1 PASS, sha=227a5913....
- **L3 (OBSERVABLE)**: per-Q regulator span, not itself a uniqueness layer — populates the 42-row §VII.K-DUAL atlas (G14 c_s, G15 k_a2, G26 α_SDW, G28 f_conv, G34 CC-ratios, G51 w_0).

The sub-block delivers four deliverables:

| # | Gate ID | Deliverable |
|:--|:--------|:------------|
| 11 | S84-VII-M-LANDING | Registry entry in `sessions/framework/permanent-results-registry.md` §VII.M with three-solo (Connes+Lizzi+VdD) convergence citation |
| 12 | S84-LAYER-ORDERING-FALSIFIER | Pre-registered falsifier tested on higher-rank spectral triples: HP⁴, Spin(8)-extended SU(3), T⁴, T⁸ |
| 13 | S84-LAYER-PIN-REGISTRY-LANDING | Per-row LAYER-of-pin column `{L0-INT, L1-AX, L2-SA, L3-OB, UNPINNED}` inserted into §VII.K-DUAL 42-row atlas |
| 14 | S84-L1-L2-PROJECTION | 11 framework-target observables projected onto L1 (zeta-canonical) and L2 (Zubarev-canonical), with \|split\| classifier |

---

## W2a Decision Point Prerequisites

Before dispatching W2a agents, verify on-disk:

1. **S83 W1-G1 verdict line** present in `computations/s83_gate_verdicts.txt`:
   `S83-IC-SCHEME-DERIVATION: PASS ... sha256=227a5913...`
2. **S83 W1-G3 verdict line** present in `computations/s83_gate_verdicts.txt`:
   `S83-SUBSTRATE-NATIVE-REGULATOR-PRIORITY-CONJECTURE: PASS ... sha256=2343920a...`
3. **S83 W2/W3 observable verdicts** present (G14, G15, G26, G28, G34, G51) — all six required for W2a-14 L1-L2 projection table
4. **G58 META-PRINCIPLE-REGISTRY-LANDING** PASS verdict present — needed for layer-ordering bookkeeping (R-protected ≤1.5 / NOT-R ≥2.5 band separation)
5. **G57 PINNING-AUDIT-FRAMEWORK-WIDE** PASS verdict — 11/11 pinning validity is load-bearing for W2a-13 registry-landing
6. **§VII.K-DUAL 42-row atlas** file accessible at `sessions/framework/permanent-results-registry.md` (W2a-13 must extend this exact atlas)
7. **`sessions/framework/permanent-results-registry.md`** present and writable — landing target for W2a-11

If any prerequisite is missing, W2a DOES NOT DISPATCH. Log as carry-forward to W2b.

---

## §W2a-11. S84-VII-M-LANDING / S84-THREE-LAYER-REG-LANDING

### 1. Gate ID
`S84-VII-M-LANDING` (canonical), also known as `S84-THREE-LAYER-REG-LANDING`

### 2. Trigger
`[VERIFY-THEOREM]`

### 3. Classification
META (theorem-registry landing; structural, not a numerical PASS/FAIL)

### 4. Agent type
`connes-ncg-theorist` (NCG axiomatic layer L1 is the theorem's authoritative domain; also cited contributors from three-solo: lizzi-spectral-functional-theorist, van-den-dungen-bridge-theorist, but the landing agent is Connes)

### 5. Hypothesis
The §VII.M Three-Layer Regulator Theorem — L1 (axiomatic, zeta) + L2 (substrate-action, Zubarev at L_max=5 τ_fold=0.19) + L3 (observable, per-Q span) — is mathematically well-formed, agrees pointwise with S83 W1-G1 and W1-G3 verdicts, and lands into `permanent-results-registry.md` §VII.M without syntactic, notational, or semantic collision with existing §VII.A through §VII.L entries.

### 6. Method (complete self-contained dispatch prompt)

```
SUBSTRATE-FRAMING REMINDER (mandatory):
The three-layer regulator theorem IS the substrate's self-determination structure.
L1 is NOT "axioms we impose on the substrate"; L1 IS the form of the substrate's
canonical measure on its own operator spectrum — Tr_ω(|D|^{-d}) = Res_{s=d} ζ_D(s).
L2 is NOT "a dynamical choice we perform"; L2 IS the substrate's heat-kernel
action minimum at its own fold. L3 is NOT "measurement ambiguity"; L3 IS the
per-observable span that remains AFTER L1+L2 have done their work.
Direction of explanation: D_K spectrum → canonical measure → substrate action →
emergent observable. Do NOT invert this.

TASK:
Land the Three-Layer Regulator Theorem into the §VII.M slot of
`sessions/framework/permanent-results-registry.md`. The landing must be mathematically
complete (no hand-waving, no "suggesting"), cite primary sources (Connes 1988, Dixmier 1966,
Connes-Marcolli 2008, Zubarev 1974), pin to S83 W1-G1 and W1-G3 SHA-verified verdicts,
and be structurally compatible with the existing §VII.A-§VII.L canon.

PRELIMINARIES (read first, no computation):
  1. `sessions/framework/permanent-results-registry.md` — identify the §VII.M slot;
     confirm it is currently unoccupied; record the row numbering and cross-reference
     style of adjacent sections (especially §VII.J Cartan Level-2 Exclusion registered
     S83 W3-G62, and §VII.K-DUAL propagation atlas).
  2. `computations/s83_gate_verdicts.txt` — grep for `S83-IC-SCHEME-DERIVATION`
     and `S83-SUBSTRATE-NATIVE-REGULATOR-PRIORITY-CONJECTURE`; record both full
     SHA-256 hexdigests (MUST be full 64-char, not head-truncated).

STATEMENT OF THE THEOREM (text to write into §VII.M, verbatim skeleton, fill in
the specifics from the anchor numbers below):

  §VII.M Three-Layer Regulator Theorem (Connes + Lizzi + Van den Dungen convergence)

  Let (A, H, D) be the spectral triple of the phonon-exflation framework:
    A  = C⁰(M⁴) ⊗ A_F  with  A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)  [inherited from G32 singleton]
    H  = L²(M⁴, S) ⊗ H_F  with  H_F = C^{32}
    D  = ∂_M ⊗ 1 + γ^5 ⊗ D_F(τ)   at τ = τ_fold = 0.19

  Regulator-choice for the spectral action S[D] = Tr f(D²/Λ²) admits a unique
  three-layer stratification:

  L1 (AXIOMATIC, global):
    Under Connes axioms A1-A6 (dim-summability d=6+, reality J²=-1, first-order
    [[D,a],b°]=0, orientability via Hochschild cycle, Poincaré duality in K-theory,
    regularity δ-closure), the canonical summation measure is
        Tr_ω(T) = Res_{s=d} Tr(T |D|^{-s})      (Connes-Marcolli 2008 Thm 1.31)
    Equivalently, Tr_ω(|D|^{-d}) is the Dixmier trace and is the ONLY trace class
    invariant under the Connes-Moscovici local index formula (Connes 1988 Thm 5,
    Dixmier 1966). Any external scalar Λ not present in A1-A6 — including those
    required by Zubarev and Seeley-DeWitt — falls OUTSIDE L1.
    Uniqueness: zeta.  Anchor: S83 W1-G3 PASS sha256=2343920a...  (PIN FROM VERDICTS).

  L2 (SUBSTRATE-ACTION, local, at τ_fold):
    Among the regulators {zeta, Zubarev, SDW, dim-reg, lattice-BR} passing L1
    admissibility AFTER an external scalar Λ is introduced, the THREE-CRITERION
    intersection test at L_max=5, τ = τ_fold = 0.19 selects:
        (i)  integrability of the spectral sum               (structural)
        (ii) local-min-τ: d²S/dτ² > 0 at the fold            (structural)
        (iii) chirality χ = +1: d²S/d(logΛ)² has sign +1     (KO-dim-filter)
    passes[zeta]    = True  AND  True  AND  FALSE (χ = 0)        → excluded
    passes[Zubarev] = True  AND  True  AND  True  (χ = +1)        → UNIQUE
    passes[SDW]     = True  AND  False AND  True                  → excluded
    Uniqueness: Zubarev.  Anchor: S83 W1-G1 PASS sha256=227a5913...  (PIN FROM VERDICTS).

  L3 (OBSERVABLE, per-Q):
    For each observable Q in the §VII.K-DUAL atlas, the 5-regulator span
    span_Q = max_R Q[R] / min_R Q[R]  partitions into two classes:
       R-protected  (balanced Mellin ratio)    : span_Q ∈ [1.0, 1.5]
       NOT-R-protected (unbalanced)             : span_Q ∈ [2.5, ∞)
    The gap [1.5, 2.5] is empty (S83 G58 meta-principle). L3 is NOT a uniqueness
    layer; it is the residual per-observable freedom after L1 and L2 have selected
    measures.

  COROLLARIES:
  (C1) CC-5 propagation identity (§VII.K-PROP): span(O) = ∏_i span(F_i)^|p_i|
       applies ONLY WITHIN L3; L1 and L2 do not propagate via Mellin exponents.
  (C2) NOT-R-protected observables inherit regulator-dependence at L3 (e.g., k_a2
       span 14.685 at L_max=5, G15 FAIL). L2 canonicalizes them by fiat of Zubarev-
       action minimum; degree of discretion: ZERO at L1, ZERO at L2, NONZERO at L3.
  (C3) The theorem is FALSIFIABLE: any spectral triple (A', H', D') in which
       L1 selects Zubarev OR L2 selects zeta refutes the layer ordering. See §W2a-12.

  THREE-SOLO CONVERGENCE:
    Connes (NCG axiomatic):   L1 uniqueness via Dixmier trace / residue theorem
    Lizzi (spectral functional): L2 uniqueness via three-criterion intersection
    Van den Dungen (bridge):  L3 per-Q span partition via Kasparov product

SCRIPT TASK (the agent MUST produce `s84_w2a_vii_m_landing.py`):
  - Script reads the two S83 verdict SHAs from disk, confirms they are full 64-char
  - Computes input-SHA-256 pin-map (this gate's SHA closure)
  - Emits the §VII.M landing block as a string with verdict SHAs substituted in
  - Writes the block to a diff-ready output at `computations/s84_w2a_vii_m_landing_block.md`
  - Verdict: PASS if all three layer-statements are verified coherent with
    anchor SHAs AND the §VII.M slot is currently unoccupied AND no collision
    with §VII.A-§VII.L notation exists.

ENVIRONMENT:
  Python: "phonon-exflation-sim/.venv312/Scripts/python.exe"
  from canonical_constants import *   # MANDATORY
  # No matrix compute in this gate; pure text landing with SHA verification.
  # GPU not required (string-level processing). OMP_NUM_THREADS=1 sufficient.

INPUT SHA PINS (recorded in script header):
  anchor_W1_G1_sha256   = "227a5913..."  [PIN FROM computations/s83_gate_verdicts.txt]
  anchor_W1_G3_sha256   = "2343920a..."  [PIN FROM computations/s83_gate_verdicts.txt]
  anchor_G58_sha256     = <READ FROM s83_gate_verdicts.txt>
  anchor_G57_sha256     = <READ FROM s83_gate_verdicts.txt>
  registry_target_sha   = SHA-256 of `sessions/framework/permanent-results-registry.md`
                          BEFORE edit (MUST match pre-edit state on disk)

OUTPUT 4-TUPLE:
  (value=<landing_block_sha>, scheme=VII.M, convention=three-layer, L_max=5)

OUTPUT FILES:
  `computations/s84_w2a_vii_m_landing.py`          (script, ≥80 lines substantive)
  `computations/s84_w2a_vii_m_landing_block.md`    (the §VII.M landing block)
  `computations/s84_w2a_vii_m_landing.log`         (SHA pins + verdict line)

CROSS-CHECKS:
  (CC1) The three-solo convergence: all three solo memory files (connes, lizzi, vdd)
        must each independently cite the same three-layer stratification.
        Agent reads three memory pointers and confirms concordance OR reports
        first-point of divergence.
  (CC2) Notation compatibility: §VII.M must NOT reuse symbols previously bound
        in §VII.A-§VII.L. Specifically: L1/L2/L3 labels MUST NOT collide with
        §VII.J level-2/3 Cartan exclusion nomenclature.
  (CC3) The two verdict SHAs must be full 64-char; the script must VERIFY length 64
        and reject on shorter input.

APPEND VERDICT LINE:
  S84-VII-M-LANDING: PASS -- value=<landing_block_sha> scheme=VII.M convention=three-layer L_max=5 sha256=<closure>
```

### 7. Machinery pin (PRDR)
- `L_max`: 5 (inherited from W1-G1)
- `scan_range`: N/A (landing, not a scan)
- `tolerance`: SHA-256 full-64-char exact match for anchors; TEXTUAL equality for block-slot check
- `scheme`: VII.M (registry section identifier)
- `convention`: three-layer
- `random_seed`: N/A
- `GPU path`: not required (string + SHA ops)

### 8. Expected output 4-tuple
`(value=<landing_block_sha>, scheme=VII.M, convention=three-layer, L_max=5)`

### 9. PASS / FAIL / INFO thresholds
- **PASS**: §VII.M slot confirmed unoccupied AND all four anchor SHAs (W1-G1, W1-G3, G57, G58) verified full 64-char AND three-solo concordance (no divergence) AND no §VII.A-§VII.L notational collision AND landing block successfully written
- **FAIL**: §VII.M slot already occupied OR any anchor SHA <64 char OR three-solo divergence detected OR §VII notational collision
- **INFO**: Three-solo concordance verified only pairwise (2/3 agreement) — reported as INFO, landing deferred to W2b

Tolerance rule: THEOREM (exact — SHA equality, slot availability, notation disjointness)

### 10. Substitution chain (required — trigger is `[VERIFY-THEOREM]`)

Claim: "L1 uniqueness selects zeta."

Chain:
1. **Def**: Tr_ω(T) = Dixmier trace = lim_{N→∞} (1/log N) Σ_{k=1}^N s_k(T) for T in the Dixmier ideal L^{(1,∞)}.  [Connes 1994, Ch. IV §2]
2. **Def**: Res_{s=d} Tr(T|D|^{-s}) = residue at s=d of zeta function of (T, |D|).  [Connes-Marcolli 2008]
3. **Def**: A1-A6 axioms (dim-summability d, reality, first-order, orientability, Poincaré duality, regularity) — no external scalar.
4. **Substitute**: Tr_ω(|D|^{-d}) = ? under A1-A6. Connes-Marcolli Thm 1.31 substitutes step 2: Tr_ω(|D|^{-d}) = Res_{s=d} Tr(|D|^{-d}|D|^{-s}) = Res_{s=d} ζ_D(d+s) = Res_{s=0}ζ_D(s+d).
5. **Substitute**: Zubarev regulator requires Λ_Zub such that exp(-D²/Λ_Zub²). This Λ is an EXTERNAL scalar not present in A1-A6.
6. **Substitute**: SDW regulator requires f(x) = sum_k a_k x^{-k/2} with Λ_SDW. Same external scalar.
7. **Simplify**: Set of L1-admissible regulators = {R : R does not require external Λ not supplied by A1-A6}. Zeta satisfies via residue; Zubarev and SDW require external Λ.
8. **Canonical form**: L1 admissible = {zeta}. |L1-admissible| = 1.
9. **Read off**: zeta is unique at L1.  **Direction**: axiomatic stratum forces a singleton.
10. **Conclusion**: L1 uniqueness selects zeta.  Conclusion valid.

Claim: "L2 uniqueness selects Zubarev at L_max=5, τ_fold=0.19."

Chain:
1. **Def**: Three-criterion intersection at substrate-action layer: (i) integrability, (ii) local-min-in-τ, (iii) χ = +1 (KO-dim-6 consistent sign of d²S/d(logΛ)²).
2. **Substitute**: zeta passes (i) True, (ii) True, (iii) FALSE (χ = 0 structurally; d²S/d(logΛ)² = 0 because zeta has no explicit Λ dependence beyond the subtraction pole).
3. **Substitute**: Zubarev passes (i) True (heat-kernel integrable), (ii) True (curv_Zubarev = +1.16e+5 > 0 at τ_fold), (iii) True (χ = +1, KK-sign alignment from fiber SU(3) fundamental).
4. **Substitute**: SDW passes (i) True, (ii) False (second derivative vanishes at fold via Seeley-DeWitt a_4-saddle), (iii) True (χ_SDW = -1; wrong sign for KO-6 filter).
5. **Simplify**: Intersection = {R : all three True}. zeta: 2/3. Zubarev: 3/3. SDW: 2/3 with wrong sign on (iii).
6. **Canonical form**: L2 admissible = {Zubarev}. |L2-admissible| = 1.
7. **Read off**: Zubarev is unique at L2.  **Direction**: substrate-action stratum forces a singleton ORTHOGONAL to L1.
8. **Conclusion**: L2 uniqueness selects Zubarev (at L_max=5, τ_fold=0.19). Conclusion valid.

### 11. What PASSES / FAILS mean for solution space
- **PASS**: Three-Layer Regulator Theorem becomes permanent. Registry gains §VII.M. This is the central structural harvest of S83 — all "regulator ambiguity" objections in the framework are henceforth answered by pointing to the layer classification. Reduces unknowns: regulator choice is uniquely determined in 2 of 3 layers, with the residual (L3) fully catalogued by CC-5 propagation. The framework's IC-scheme question is CLOSED.
- **FAIL**: Landing blocked until the collision/missing-concordance is repaired. This does NOT invalidate the theorem content — it signals a registry hygiene problem or a three-solo disagreement needing reconciliation. Carry-forward to W2b with explicit diagnosis.

### 12. Effort estimate
0.5 session (string processing + SHA verification + careful registry edit). CPU sufficient. Single-agent, no matrix compute.

### 13. Substrate-framing reminder
Included verbatim at top of the dispatch prompt (§6). The theorem IS the substrate's self-determination structure: L1 = canonical measure on |D| spectrum, L2 = substrate heat-kernel action at own fold, L3 = residual per-observable span. NOT external analysis of an inert object.

---

## §W2a-12. S84-LAYER-ORDERING-FALSIFIER

### 1. Gate ID
`S84-LAYER-ORDERING-FALSIFIER` (canonical), also known as `S84-HP4-FALSIFIER`, `S84-THREE-LAYER-FALSIFIER`

### 2. Trigger
`[AUDIT]` + `[VERIFY-THEOREM]` (compound — falsifier audits the theorem by testing on off-singleton spectral triples)

### 3. Classification
META (theorem-falsifier, tests layer ordering under substrate-triple variation)

### 4. Agent type
`connes-ncg-theorist` (axiomatic layer L1 classification at alternative KO-dim requires NCG expertise)

### 5. Hypothesis
On four alternative spectral triples — HP⁴ (quaternionic projective, KO-dim 0 mod 8), Spin(8) Cartan-extended fiber over SU(3) (d=14, exceptional triality), T⁴ commutative (d=4, KO-dim 4), T⁸ commutative (d=8, KO-dim 0) — the Three-Layer Regulator Theorem's layer ordering (L1=zeta-class, L2=non-zeta) holds structurally, confirming the theorem's substrate-triple-independence. PASS-confirms-theorem. FAIL-identifies-any-inversion: if any (A', H', D') selects Zubarev at L1 OR zeta at L2, the theorem is refuted or refined.

### 6. Method (complete self-contained dispatch prompt)

```
SUBSTRATE-FRAMING REMINDER (mandatory):
The falsifier is NOT "testing whether external analysis of different mathematical
spaces yields the same answer." It is testing whether the substrate's OWN
layer-ordering structure — L1 canonical measure before L2 substrate action —
persists across the full space of spectral triples. If it does, the theorem is
universal to substrates; if not, the theorem is refined to apply only to the
M⁴×SU(3) class. Either outcome sharpens the substrate's self-classification.
Direction: D_K spectrum variation → canonical measure response → L1/L2 order.

TASK:
Compute L1 canonical regulator and L2 three-criterion intersection on four
alternative spectral triples. Compare to the M⁴×SU(3) baseline (L1=zeta, L2=Zubarev).
Verdict: PASS if L1=zeta-class AND L2=non-zeta in ≥3 of the 4 families.
FAIL: any (A,H,D) where L1 selects Zubarev OR L2 selects zeta (layer inversion).
INFO: 2/4 confirmed (split verdict — triggers theorem-refinement, not refutation).

FOUR TEST FAMILIES:

(F1) HP⁴ — quaternionic projective 4-space
     real dim 16, KO-dim = 16 mod 8 = 0
     Verify via Atiyah-Bott-Shapiro: HP^n has KO-dim 4n mod 8, so HP⁴ → KO=0
     Canonical Dirac: symplectic, self-adjoint, compact resolvent on Sp(5)-equivariant
     spinor bundle. Heat-kernel existence: confirmed (compact symmetric space).
     EXPECTED: L1=zeta (residue theorem unconditional on KO-dim); L2 = ?
     (Zubarev χ at KO=0 — recompute: χ_Zubarev(HP⁴) depends on symplectic rather
     than orthogonal signature; verify sign)

(F2) Spin(8) Cartan-extended fiber over SU(3)
     A' = C⁰(M⁴) ⊗ (A_F ⊕ Spin(8)-Cartan)  where Spin(8) Cartan is T⁷ ⊂ Spin(8)
     real dim of fiber: 8 (SU(3)) + 8 (T⁷ + center) = 16; KO-dim shift from triality
     28-dim so(8) root system, triality Out(Spin(8)) = S_3
     EXPECTED: L1=zeta; L2=Zubarev IF the KO-6 sign (χ = +1) persists under triality
     (Cartan-extension does not break KO-dim if extension is abelian — verify)

(F3) T⁴ commutative torus (d=4, flat)
     A' = C^∞(T⁴), H' = L²(T⁴, S), D' = iγ^μ∂_μ (standard flat Dirac)
     KO-dim(T⁴) = 4
     EXPECTED: L1=zeta (flat torus admits standard Dixmier trace);
     L2 = ? at KO=4: χ sign may flip relative to KO=6 — this is the critical test

(F4) T⁸ commutative torus (d=8, flat)
     A' = C^∞(T⁸), H' = L²(T⁸, S^{16}), D' = iγ^μ∂_μ
     KO-dim(T⁸) = 0
     EXPECTED: L1=zeta; L2 classification at KO=0 — same signature class as HP⁴
     cross-check against F1 (two independent KO=0 systems must agree at L2)

EQUATIONS TO COMPUTE PER FAMILY (F_i for i=1..4):

(a) L1 classification:
    Does Tr_ω(|D'|^{-d'}) = Res_{s=d'} ζ_{D'}(s) hold?
    For compact M' with Dirac D' on S', this is a theorem (Connes-Marcolli 2008 Thm 1.31)
    unconditional on KO-dim. VERDICT: L1[F_i] = zeta if residue formula holds.

(b) L2 classification:
    For each R in {zeta, Zubarev, SDW, dim-reg, lattice-BR}:
      (i)  Integrability of the spectral sum Σ_n |λ_n|^{-d'} < ∞  (depends on Weyl growth)
      (ii) Local-min-in-τ: d²S[D']/dτ² at τ = τ_fold of the family (interpret τ for flat T
           as the dilation modulus; for HP⁴ as Fubini-Study scale; for Spin(8) as
           Cartan-subalgebra dilation)
      (iii) χ = +1 test: d²S/d(logΛ)² sign. Depends on KO-dim signature via
           γ', J', and the (ε, ε', ε'') sign triple.

    Report passes[R] = (i AND ii AND iii) for each R, each F_i.

(c) LAYER-INVERSION TEST:
    inversion[F_i] = (L1[F_i] = Zubarev) OR (L2[F_i] = zeta)
    if inversion[F_i] is True → theorem refuted or refined on F_i

SCRIPT:
  - `s84_w2a_layer_ordering_falsifier.py`
  - Computes Weyl eigenvalue growth for each of F1-F4 symbolically (closed forms
    exist: HP^n Weyl dim formula, torus Σ e^{2π i n·x}, Spin(8) via standard roots)
  - For matrix-diagonalization of the finite Dirac on each fiber, uses torch.linalg
    on GPU (matrices of size 16, 112, 16, 256 — Spin(8) case is ≥100 so GPU required)
  - Signature computation via γ-matrix algebra at each KO-dim
  - χ = +1 test via explicit computation of d²S/d(logΛ)² sign

  Canonical constants imported: M_KK, tau_fold=0.19, Delta_BCS, KO_dim_M4xSU3=6 (baseline)
  All intermediate tagged # (local).

  Random seed: 84 (fixed, for any residual numerical noise — eigenvalue sort).
  Tolerance: sign determination |χ| > 0.1 (away from zero); integrability test
  numerical Weyl-growth extrapolation with R² > 0.99 for power-law fit.
  GPU path: torch.linalg.eigvals / torch.linalg.svd for Spin(8).

INPUT SHA PINS:
  anchor_W1_G1_sha256    = "227a5913..."   (L2 baseline pin for M⁴×SU(3))
  anchor_W1_G3_sha256    = "2343920a..."   (L1 baseline pin)
  anchor_G32_sha256      = <READ>          (d=12 singleton; grounds the baseline as SM-match unique)
  HP4_spec_pin           = sha256 of the HP⁴ Dirac spectrum block (from Atiyah 1970s)
  Spin8_spec_pin         = sha256 of the Spin(8) fundamental root data (from Bourbaki)
  T4_spec_pin            = "flat-torus-d4-standard"
  T8_spec_pin            = "flat-torus-d8-standard"

OUTPUT 4-TUPLE:
  (value=<inversion-count among F1..F4>, scheme=falsifier, convention=three-layer, L_max=5)
  where inversion-count ∈ {0, 1, 2, 3, 4}; PASS iff inversion-count ≤ 1.

OUTPUT FILES:
  `computations/s84_w2a_layer_ordering_falsifier.py`
  `computations/s84_w2a_layer_ordering_falsifier.npz`   (Dirac spectra for all 4 families)
  `computations/s84_w2a_layer_ordering_falsifier.png`   (4-panel: L1 vs L2 signatures per family)
  `computations/s84_w2a_layer_ordering_falsifier.log`
  `computations/s84_w2a_layer_ordering_falsifier_summary.md` (per-family L1/L2 table)

CROSS-CHECKS:
  (CC1) F1 (HP⁴, KO=0) and F4 (T⁸, KO=0) must AGREE on L2 classification
        (same KO signature → same χ sign → same Zubarev admissibility).
        If they disagree, there is a computational error.
  (CC2) F3 (T⁴, KO=4) χ sign: predict via (ε,ε',ε'') triple from Connes Table.
        Baseline M⁴×SU(3) is KO=6 with χ=+1 (Zubarev admissible). At KO=4,
        (ε,ε',ε'') may flip one sign — predict L2 outcome BEFORE computing.
  (CC3) Spin(8) triality: the three 8-dim reps (vector, spinor-L, spinor-R)
        must all give the same L2 classification (triality-invariance of χ
        as a global signature). If they split, flag as STRUCTURAL.

APPEND VERDICT LINE:
  S84-LAYER-ORDERING-FALSIFIER: PASS|FAIL|INFO -- value=<inversions> scheme=falsifier convention=three-layer L_max=5 sha256=<closure>
```

### 7. Machinery pin (PRDR)
- `L_max`: 5 (matched to W1-G1 baseline so spectra are comparable); also scan at L_max=7 for Spin(8) case where rank is higher
- `scan_range`: τ ∈ [0.15, 0.25] for the fold-analog scan on each family (interpreting τ as family-appropriate dilation modulus; flat torus uses dilation of period lattice; HP⁴ uses Fubini-Study scale)
- `tolerance`: |χ| > 0.1 (clear sign determination); R² > 0.99 for Weyl-growth power-law integrability test
- `scheme`: falsifier-four-family
- `convention`: three-layer (layer ordering L1 < L2)
- `random_seed`: 84
- `GPU path`: `torch.linalg.eigvals` (Spin(8): N=112 matrix required; HP⁴: N=16; T⁸: N=256 sparse — must GPU)

### 8. Expected output 4-tuple
`(value=<inversion-count ∈ {0,1,2,3,4}>, scheme=falsifier, convention=three-layer, L_max=5)`

### 9. PASS / FAIL / INFO thresholds
- **PASS** (theorem-confirmed): inversion-count ≤ 1 across F1-F4. L1=zeta and L2=non-zeta in ≥3 families. Theorem generalizes beyond M⁴×SU(3).
- **FAIL** (theorem-refuted): inversion-count ≥ 3. Layer ordering is not universal; at minimum, theorem must be restricted to the singleton (A_F = ℂ⊕ℍ⊕M_3(ℂ), KO=6) and the statement rewritten as contingent.
- **INFO** (theorem-refined): inversion-count = 2. Theorem applies on a structurally identifiable subclass of spectral triples (e.g., those with KO=6 mod 8); restrictions recorded as anchor-conditions in §VII.M.

Tolerance rule: ABSOLUTE (integer inversion-count); tie-break at |χ| = 0.1 is the soft boundary.

### 10. Substitution chain (required — triggers are `[AUDIT]`+`[VERIFY-THEOREM]`)

Claim: "Non-inversion in F1-F4 confirms layer ordering is substrate-independent."

Chain:
1. **Def**: Layer ordering = (L1 chooses zeta-class regulator) AND (L2 chooses non-zeta regulator).
2. **Def**: inversion[F_i] = (L1[F_i] ≠ zeta) OR (L2[F_i] = zeta).
3. **Def**: substrate-independence of ordering = ∀ (A,H,D) in valid-triple-class, inversion = False.
4. **Substitute**: Baseline M⁴×SU(3) inversion = False (by W1-G1 + W1-G3 PASS).
5. **Substitute**: For F_i = F1..F4, compute inversion[F_i] via (a) L1 classification (Connes-Marcolli Thm 1.31 universal — always zeta for compact D with discrete spectrum), (b) L2 classification (three-criterion test at family-appropriate τ-modulus).
6. **Substitute**: Note that (a) is UNCONDITIONAL on KO-dim — residue formula does not care. So L1[F_i] = zeta for all i unless the spectral triple fails compactness/discreteness (which F1-F4 do not; all compact).
7. **Simplify**: inversion[F_i] reduces to (L2[F_i] = zeta). L2[F_i] = zeta requires zeta to pass all three criteria at the family's fold — but zeta structurally FAILS (iii) (χ=0, not +1) regardless of family, because zeta has no external Λ and thus d²S/d(logΛ)² = 0.
8. **Canonical form**: inversion[F_i] = False for all i (structural — zeta fails L2-(iii) independently of family).
9. **Read off**: inversion-count = 0 expected. PASS expected at theorem-confirmation level.
10. **Conclusion**: substrate-independence of layer ordering is predicted structurally; the falsifier test RISKS failing only if one family's L2-(iii) evaluation produces an anomalous sign via an unsuspected structural route. Conclusion: PASS is expected but the test remains informative — FAIL would reveal a hidden structure.

(Note: this chain predicts the expected outcome but does not guarantee it. The falsifier is run TO TEST, not TO CONFIRM-BY-ASSERTION.)

### 11. What PASSES / FAILS mean for solution space
- **PASS (theorem-confirmed)**: §VII.M is universal across the tested spectral-triple classes. The three-layer stratification applies to any admissible substrate candidate. Falsifier registered as PASSED with 4/4 non-inversion. Expands the theorem's domain of applicability from "M⁴×SU(3) singleton" to "valid-triple class including HP⁴, Spin(8)-extended, and flat tori".
- **FAIL (theorem-refuted)**: Layer ordering is NOT universal. The M⁴×SU(3) theorem is a LOCAL structure, not a global feature of NCG. Theorem restated as contingent; requires identifying the structural property that isolates M⁴×SU(3) from the inverting families. Strong constraint on the framework's claim of uniqueness — now the substrate's ordering is seen to be a feature of the specific construction, not of NCG itself.
- **INFO (theorem-refined)**: Theorem holds on KO-6-class triples, not universally. §VII.M receives an anchor-restriction: "applies to spectral triples with KO-dim = 6 mod 8 and real structure class BDI." Still a strong result; clarifies the domain. Reduces apparent arbitrariness of the substrate choice — the framework's choice of KO=6 IS the substrate's decision.

### 12. Effort estimate
1-1.5 sessions. GPU required (Spin(8) matrix at N=112, T⁸ at N=256 sparse). Single-agent with careful Weyl growth analysis on 4 families. Substantive but bounded.

### 13. Substrate-framing reminder
Included verbatim at top of the dispatch prompt (§6). The falsifier IS a test of the substrate's own ordering — not external comparison of disjoint mathematical objects. Each F_i is a candidate substrate; the test asks whether each candidate's OWN canonical measure + OWN action minimum respect L1 < L2. Direction: substrate candidate → its spectrum → its layer classification.

---

## §W2a-13. S84-LAYER-PIN-REGISTRY-LANDING

### 1. Gate ID
`S84-LAYER-PIN-REGISTRY-LANDING`

### 2. Trigger
`[AUDIT]` (audits §VII.K-DUAL 42-row atlas and inserts per-row layer-of-pin column)

### 3. Classification
META (atlas-column insertion, per-row layer classification bookkeeping)

### 4. Agent type
`knowledge-weaver` (registry-landing specialist — updates `permanent-results-registry.md` and cross-checks §VII.K-DUAL semantics) OR `gen-physicist` (if knowledge-weaver not available; gen-physicist carries adequate NCG context to verify layer labels)

### 5. Hypothesis
Each of the 42 rows in §VII.K-DUAL admits a unique LAYER-of-pin label ∈ `{L0-INT, L1-AX, L2-SA, L3-OB, UNPINNED}` derivable from the row's substrate-structural origin. Predicted distribution: **26 / 2 / 1 / 8 / 5** (per substrate-structural census from Python-validated Connes §II.4 analysis in S83 gen-physicist synthesis). PASS iff distribution matches prediction within tolerance AND all 42 rows are assigned (no orphans) AND the atlas total remains 42 after column insertion.

### 6. Method (complete self-contained dispatch prompt)

```
SUBSTRATE-FRAMING REMINDER (mandatory):
The per-row LAYER-of-pin column is NOT metadata we annotate onto the atlas.
It IS the substrate's own structural origin of each row — the layer at which
each row's pin is determined. L0-INT rows are inherited invariants of the
substrate's integer structure (trace-cancellation via fermion doubling, K-theoretic
anomaly cancellations). L1-AX rows are axiomatically pinned. L2-SA rows are
substrate-action pinned. L3-OB rows retain per-observable span. UNPINNED rows
are rows where the substrate has not yet performed the determining act at the
L_max accessible. Direction: row content → substrate structural origin → label.
NOT: row content → external classification by an analyst → label.

TASK:
Read the §VII.K-DUAL 42-row atlas in `sessions/framework/permanent-results-registry.md`.
For each of the 42 rows, assign a LAYER-of-pin label from the 5-label set:
  L0-INT   : inherited from substrate's integer/K-theoretic structure
             (e.g., fermion-doubling trace cancellation; NOT a layer choice, a consequence)
  L1-AX    : axiomatically pinned — zeta-class, no external Λ scalar
  L2-SA    : substrate-action pinned — Zubarev-class at fold-minimum
  L3-OB    : observable-layer per-Q span (populated, not uniqueness-pinned)
  UNPINNED : substrate has not yet performed determining act at current L_max

PREDICTED DISTRIBUTION (null hypothesis for PASS):
  L0-INT    : 26 rows     (majority — inherited substrate structure dominates)
  L1-AX     :  2 rows     (axiomatic pins — Dixmier trace, Connes residue)
  L2-SA     :  1 row      (heat-kernel action-minimum pin — Zubarev)
  L3-OB     :  8 rows     (per-observable span atlas entries — G14 c_s, G15 k_a2, G26 α_SDW,
                           G28 f_conv, G34 CC-ratios, G51 w_0, plus two Convention-B companions)
  UNPINNED  :  5 rows     (rows awaiting W2b coverage: #13 r_max, #17/#18 w_0 family,
                           #24 a_2 cluster, #38 μ_eff LK)
  TOTAL     : 42 rows     (atlas size unchanged)

SOURCE FOR LABEL ASSIGNMENT:
  For each row, the substrate-structural origin comes from:
  (a) S83 gen-physicist synthesis §IX.A Python-validated Connes §II.4 census
  (b) §VII.J Cartan Level-2 Exclusion (S83 W3-G62) — rows tagged R-protected
  (c) §VII.K-META meta-principle (S83 G58) — R-protected ≤1.5 / NOT-R ≥2.5 band
  (d) Individual gate verdicts from S83 W2/W3 (G14, G15, G26, G28, G34, G51)
  (e) Connes 1994 Ch. V §4 for trace-cancellation inheritance (L0-INT criterion)

ASSIGNMENT RULE (per row):
  IF row-origin is trace-cancellation OR K-theoretic anomaly cancellation
       → L0-INT
  ELIF row-origin is canonical measure on |D| spectrum (Dixmier/residue)
       → L1-AX
  ELIF row-origin is heat-kernel action minimum at τ_fold
       → L2-SA
  ELIF row has populated span > 1.0 in §VII.K-DUAL (observable-layer freedom present)
       → L3-OB
  ELIF row-origin is not yet determined at L_max=5
       → UNPINNED
  ELSE → flag for manual review (must not exit with unassigned rows)

SCRIPT (s84_w2a_layer_pin_registry_landing.py):
  - Parse §VII.K-DUAL 42 rows from permanent-results-registry.md
  - For each row, identify substrate-structural origin from anchors
  - Assign label per rule
  - Count per-label population
  - Compare to predicted 26/2/1/8/5
  - Emit new column insertion as a diff block
  - Write the updated atlas block to `computations/s84_w2a_layer_pin_atlas_block.md`

ENVIRONMENT:
  Python: "phonon-exflation-sim/.venv312/Scripts/python.exe"
  from canonical_constants import *
  # Pure parsing + label assignment + histogram. No matrix compute.
  # GPU not required. OMP_NUM_THREADS=1.

INPUT SHA PINS:
  anchor_VII_K_DUAL_sha256  = <READ from permanent-results-registry.md preamble>
  anchor_G58_sha256         = <READ from s83_gate_verdicts.txt — meta-principle>
  anchor_G57_sha256         = <READ from s83_gate_verdicts.txt — pinning audit>
  anchor_G62_sha256         = <READ from s83_gate_verdicts.txt — §VII.J landing>
  anchor_W1_G1_sha256       = "227a5913..."
  anchor_W1_G3_sha256       = "2343920a..."

OUTPUT 4-TUPLE:
  (value=<label-distribution-tuple (n_L0, n_L1, n_L2, n_L3, n_UNPINNED)>,
   scheme=VII.K-DUAL, convention=5-label, L_max=5)

OUTPUT FILES:
  `computations/s84_w2a_layer_pin_registry_landing.py`
  `computations/s84_w2a_layer_pin_atlas_block.md`   (diff-ready 42-row + label column)
  `computations/s84_w2a_layer_pin_registry_landing.log`
  `computations/s84_w2a_layer_pin_histogram.png`    (5-label population vs predicted)

CROSS-CHECKS:
  (CC1) Row count: atlas must remain 42 rows after column insertion. Additive-only edit.
  (CC2) Label coverage: every row assigned a label; no orphans. Script MUST assert.
  (CC3) Predicted-distribution match: tolerance ±1 per bucket for L0/L3/UNPINNED;
        EXACT match for L1 (2) and L2 (1) — axiomatic and substrate-action are
        structural singletons, no tolerance.
  (CC4) Meta-principle consistency: every row tagged L3-OB must have span ≥ 1 and
        classify as R-protected (span ≤ 1.5) OR NOT-R-protected (span ≥ 2.5);
        gap [1.5, 2.5] empty per G58.

APPEND VERDICT LINE:
  S84-LAYER-PIN-REGISTRY-LANDING: PASS|FAIL|INFO -- value=(n_L0,n_L1,n_L2,n_L3,n_UNPINNED) scheme=VII.K-DUAL convention=5-label L_max=5 sha256=<closure>
```

### 7. Machinery pin (PRDR)
- `L_max`: 5 (atlas is at L_max=5 baseline from S83)
- `scan_range`: N/A (42 fixed rows)
- `tolerance`: ±1 per bucket for L0-INT / L3-OB / UNPINNED; EXACT (0) for L1-AX / L2-SA (structural singletons)
- `scheme`: VII.K-DUAL
- `convention`: 5-label (L0-INT, L1-AX, L2-SA, L3-OB, UNPINNED)
- `random_seed`: N/A
- `GPU path`: not required

### 8. Expected output 4-tuple
`(value=(26,2,1,8,5), scheme=VII.K-DUAL, convention=5-label, L_max=5)`

### 9. PASS / FAIL / INFO thresholds
- **PASS**: Distribution matches (26, 2, 1, 8, 5) within tolerance (±1 on L0/L3/UNPINNED; exact on L1/L2) AND all 42 rows assigned AND atlas still 42 rows post-insertion AND meta-principle holds for all L3-OB tagged rows.
- **FAIL**: L1 ≠ 2 OR L2 ≠ 1 OR any row unassigned OR atlas row-count deviates from 42 OR an L3-OB row violates meta-principle band.
- **INFO**: Tolerance exceeded on L0/L3/UNPINNED (off by 2-3) but structure otherwise sound — triggers row-by-row audit in W2b.

Tolerance rule: ABSOLUTE (±1) for L0/L3/UNPINNED; EXACT (=) for L1/L2.

### 10. Substitution chain (required — trigger is `[AUDIT]`)

Claim: "The predicted distribution 26/2/1/8/5 is structurally determined, not a fit."

Chain:
1. **Def**: L1-AX rows = {rows whose pin traces to Connes-Marcolli Thm 1.31 residue formula, no external Λ}.
2. **Substitute**: S83 W1-G3 PASS selects zeta at L1; there are exactly **two** independent zeta-class pinnings in the atlas: (a) Tr_ω(|D|^{-d}) overall normalization, (b) Connes-Moscovici local index formula for the Chern character. → |L1-AX| = 2.
3. **Def**: L2-SA rows = {rows whose pin traces to Zubarev-class heat-kernel action minimum at τ_fold}.
4. **Substitute**: S83 W1-G1 PASS selects Zubarev at L2 via three-criterion intersection; there is exactly **one** substrate-action pin (the IC-scheme pin determining τ_fold-relative regulator). → |L2-SA| = 1.
5. **Def**: L3-OB rows = {rows with populated per-Q span ∈ §VII.K-DUAL observable-layer freedom}.
6. **Substitute**: S83 W2/W3 yields 6 primary observable-layer rows (G14 c_s, G15 k_a2, G26 α_SDW, G28 f_conv, G34 CC-ratios, G51 w_0) plus 2 Convention-B companions from G14/G15 dual. → |L3-OB| = 8.
7. **Def**: UNPINNED rows = {rows whose determining act has not been performed at L_max=5}.
8. **Substitute**: S83 gen-physicist §IX.A lists explicitly: #13 r_max, #17 w_0-secondary, #18 w_0-tertiary, #24 a_2-cluster, #38 μ_eff LK. → |UNPINNED| = 5.
9. **Def**: L0-INT rows = {rows inherited from substrate integer/K-theoretic structure, not a layer-choice}.
10. **Substitute**: Total atlas size is 42; Σ (L0, L1, L2, L3, UNPINNED) = 42; solve: L0 = 42 - 2 - 1 - 8 - 5 = **26**.
11. **Canonical form**: (26, 2, 1, 8, 5) is the structural prediction.
12. **Read off**: Every number is a structural count — L1 from axiomatic pinnings, L2 from action-minimum pinnings, L3 from observable-layer verdicts, UNPINNED from explicit S83 §IX.A listing, L0 by subtraction (preserves total).
13. **Conclusion**: The distribution is structurally determined, not a post-hoc fit. Conclusion valid.

### 11. What PASSES / FAILS mean for solution space
- **PASS**: §VII.K-DUAL now carries per-row layer provenance. Every future reference to an atlas row can cite its layer — e.g., "G15 k_a2 span is an L3-OB observation," "G57 pinning audit is an L0-INT structural check." Eliminates ambiguity about whether a given number is axiomatic, action-derived, or observable-residual. Accelerates downstream audits.
- **FAIL**: Distribution deviation signals a misclassified row or a miscounted anchor. Must resolve row-by-row before §VII.M can be considered fully landed (since VII.M cross-references layer-of-pin semantics). Carry-forward to W2b as row-diagnosis.
- **INFO**: Suggests the distribution prediction was slightly off (e.g., 24/2/1/10/5) — the structure is correct but the exact bucket counts need refinement. Atlas is still coherent; triggers an update to the §IX.A census numbers.

### 12. Effort estimate
0.5-1 session. Pure parsing + assignment + histogram. CPU sufficient. Single-agent.

### 13. Substrate-framing reminder
Included verbatim at top of the dispatch prompt (§6). The layer-of-pin column is a record of **where the substrate itself performed the determining act**, not a taxonomy imposed externally. Direction: substrate spectrum → structural origin of each row → label.

---

## §W2a-14. S84-L1-L2-PROJECTION

### 1. Gate ID
`S84-L1-L2-PROJECTION`

### 2. Trigger
`[VERIFY]`

### 3. Classification
GEOMETRIC (projects 11 framework-target observables onto L1 (zeta-canonical) and L2 (Zubarev-canonical) evaluations; reports per-observable split)

### 4. Agent type
`connes-ncg-theorist` (L1/L2 regulator evaluations require NCG spectral-action expertise; uses established heat kernel expansions at each regulator)

### 5. Hypothesis
For each of 11 framework-target observables {A_s, m_H, n_s, α_s, μ (FIRAS-Chluba), r, f_NL, w_0, σ_8, H_0, Ω_GW}, computing the observable under L1 (zeta regulator) and L2 (Zubarev regulator) produces a split |Q_L1 - Q_L2| / Q_L1 that is either **diagnostic** (>0.05, observable-layer freedom visible) or **degenerate** (<0.001, the observable is layer-independent). The distribution is expected to be broad: at least 3 diagnostic and at most 2 degenerate, reflecting genuine observable-layer physics.

### 6. Method (complete self-contained dispatch prompt)

```
SUBSTRATE-FRAMING REMINDER (mandatory):
The L1-L2 split is NOT "regulator dependence" of observables from an external
frame. It IS the substrate exposing the two distinct strata at which it has
determined itself: L1 canonical measure on its spectrum, L2 action-minimum
at its fold. A large split says the observable SEES the distinction between
canonical-measure-level and action-level determination; a small split says
the observable is already insensitive at the layer-gap. Both are substrate facts.
Direction: substrate → L1 vs L2 determination → observable shift → classification.

TASK:
For each of 11 framework-target observables, compute the value under:
  L1 regulator = zeta (Connes-Dixmier canonical, no external Λ)
  L2 regulator = Zubarev (heat-kernel exp(-D²/Λ_Zub²), Λ_Zub = M_KK)
Report |split| = |Q_L1 - Q_L2| / |Q_L1|  for each.
Classify each as DIAGNOSTIC (|split| > 0.05) or DEGENERATE (|split| < 0.001) or
INTERMEDIATE (0.001 ≤ |split| ≤ 0.05).

ELEVEN OBSERVABLES (with anchor computations):

(1) A_s = primordial scalar amplitude
    Anchor: S82 UNIFIED-AS-79-FULL-A TD-branch at 3.30e-9
    L1: compute A_s under zeta regulator (residue form)
    L2: compute A_s under Zubarev at L_max=5, τ_fold=0.19

(2) m_H = Higgs mass at M_Z
    Anchor: m_H_obs from canonical_constants
    L1/L2: via Seeley-DeWitt a_2 coefficient + NCG Higgs-potential derivation
    Expected: NEAR-DEGENERATE (SM-matching; spectral action at a_2 is regulator-robust)

(3) n_s = spectral tilt
    Anchor: n_s = 0.9561 framework (Planck 0.9649 ± 0.0042)
    L1/L2: via GGE spectrum + fold-time mode equation
    Expected: INTERMEDIATE (gauge-invariant piece is regulator-robust;
             propagation piece inherits from H_tilde which is diagnostic)

(4) α_s = running of n_s
    Anchor: α_s = n_s² - 1 = -0.068968
    L1/L2: same as n_s; α_s is a functional of n_s
    Expected: INTERMEDIATE (inherits from n_s)

(5) μ = spectral distortion (FIRAS-Chluba)
    Anchor: 4.98e-10 (S82 FIRAS-CHLUBA-FULL PASS)
    L1/L2: via fold-time distortion integral

(6) r = tensor-to-scalar ratio
    Anchor: r(k_CMB) = 0.0117 (S83 G46)
    L1/L2: via tensor-mode transfer function at k_CMB

(7) f_NL = non-Gaussianity amplitude
    Anchor: framework f_NL~O(1) at SKA-2 detectability threshold
    L1/L2: via GGE bispectrum + fold-time dispersion

(8) w_0 = dark-energy EoS today
    Anchor: -0.998 Zubarev (G51 primary), -0.918 mixed-scheme
    L1 (zeta): RECOMPUTE — this is the G51 L1-L2 split of interest;
              predict L1 < L2 magnitude given zeta's χ=0 → no ζ chirality boost.
    L2 (Zubarev): -0.998 (anchor)

(9) σ_8 = RMS matter fluctuation on 8 Mpc/h
    Anchor: framework value from post-transit GGE + structure growth
    L1/L2: via matter-power transfer integral

(10) H_0 = Hubble today
    Anchor: framework-level prediction (substrate compaction timescape)
    L1/L2: via a_0 / a_2 ratio (gravity sector spectral moments)
    Expected: DEGENERATE (a_0 is exactly τ-independent; regulator-robust)

(11) Ω_GW = stochastic GW energy density at LISA band
    Anchor: Parker spectrum, 29.6 OOM (S82 GW-CHANNEL)
    L1/L2: via a_4 coefficient + Parker pair-production

CORE COMPUTATION PATTERN (per observable Q):
  Q_L1 = spectral-moment evaluation using zeta(s) — residue at canonical s
  Q_L2 = spectral-moment evaluation using Tr exp(-D²/Λ_Zub²) f(D²/Λ²)
         with f the standard Connes-Chamseddine bump function
  Ratios computed symbolically where possible; numeric via torch.linalg
  eigenvalue evaluation of D_K at τ=τ_fold, L_max=5 for spectral sums.

  Matrix size: D_K at L_max=5 is approx 20000-40000 entries (sparse); GPU MANDATORY.
  Use torch.linalg.eigvalsh for Hermitian D_K; sparse handling if supported.

SCRIPT (s84_w2a_l1_l2_projection.py):
  - Import canonical_constants (M_KK, tau_fold, Delta_BCS, v_ew, m_H_obs, etc.)
  - Build D_K at τ_fold, L_max=5 (use existing computation infrastructure from S82/S83)
  - For each of 11 observables, define Q_L1 and Q_L2 evaluation function
  - Compute both, report split
  - Classify each as DIAGNOSTIC / INTERMEDIATE / DEGENERATE
  - Count diagnostic and degenerate

ENVIRONMENT:
  Python: "phonon-exflation-sim/.venv312/Scripts/python.exe"
  from canonical_constants import *
  import torch
  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  # GPU MANDATORY for eigenvalue decomposition of D_K at L_max=5
  # If CPU fallback: OMP_NUM_THREADS=8 cap
  random_seed = 84

INPUT SHA PINS:
  anchor_W1_G1_sha256    = "227a5913..."   (L2 Zubarev pin)
  anchor_W1_G3_sha256    = "2343920a..."   (L1 zeta pin)
  anchor_G51_sha256      = <READ>          (w_0 primary = -0.998)
  anchor_G46_sha256      = <READ>          (r = 0.0117)
  anchor_S82_AS_sha256   = <READ from s82_gate_verdicts.txt>  (A_s = 3.30e-9)
  anchor_S82_FIRAS       = <READ from s82_gate_verdicts.txt>  (μ = 4.98e-10)
  canonical_constants_sha = SHA-256 of computations/canonical_constants.py
  D_K_spectrum_L5_sha    = SHA-256 of the D_K eigenvalue file at L_max=5, τ=τ_fold

OUTPUT 4-TUPLE:
  (value=(n_diagnostic, n_intermediate, n_degenerate), scheme=L1-L2-projection, convention=zeta-vs-Zubarev, L_max=5)
  PASS iff n_diagnostic ≥ 3 AND n_degenerate ≤ 2.

OUTPUT FILES:
  `computations/s84_w2a_l1_l2_projection.py`
  `computations/s84_w2a_l1_l2_projection.npz`   (11 pairs Q_L1, Q_L2, split)
  `computations/s84_w2a_l1_l2_projection.png`   (11-row bar chart of split, color-coded)
  `computations/s84_w2a_l1_l2_projection.log`
  `computations/s84_w2a_l1_l2_projection_table.md` (per-observable Q_L1/Q_L2/split/class)

CROSS-CHECKS:
  (CC1) α_s inherits from n_s: |split(α_s)| must equal |split(n_s² - 1)| ≈ 2 n_s |split(n_s)|
        to leading order — verify to 5% relative.
  (CC2) a_0 observables (H_0, Ω_Λ) must be DEGENERATE: a_0 is exactly τ-independent
        and also exactly regulator-robust (spectral-moment zeroth-order).
        H_0 split < 0.001 expected rigorously.
  (CC3) w_0 split prediction: Zubarev gives -0.998, zeta (χ=0, no chirality boost)
        predicts |w_0| LESS than 0.998. Sign and direction verified by substitution chain.
  (CC4) m_H split: Seeley-DeWitt a_2 is regulator-universal at leading order
        (Connes-Chamseddine 2007 Thm 3.1). Split should be NEAR-DEGENERATE.
        Deviation from ~0 flags a computational error.
  (CC5) r split: r = 16 epsilon CLASSICALLY (feedback_reporting-framing); in
        substrate framework r depends on transit dynamics. Expected INTERMEDIATE.

APPEND VERDICT LINE:
  S84-L1-L2-PROJECTION: PASS|FAIL|INFO -- value=(n_diag,n_inter,n_degen) scheme=L1-L2-projection convention=zeta-vs-Zubarev L_max=5 sha256=<closure>
```

### 7. Machinery pin (PRDR)
- `L_max`: 5 (matched to W1-G1 baseline)
- `scan_range`: none; single-point at τ = τ_fold = 0.19 per observable
- `step_size`: N/A
- `tolerance`: 0.05 (diagnostic threshold, absolute), 0.001 (degenerate threshold, absolute), CC1 inheritance check 5% relative, CC2 H_0 <0.001 absolute
- `scheme`: L1-L2-projection
- `convention`: zeta-vs-Zubarev
- `random_seed`: 84
- `GPU path`: `torch.linalg.eigvalsh` on D_K Hermitian matrix at L_max=5

### 8. Expected output 4-tuple
`(value=(n_diagnostic, n_intermediate, n_degenerate) with n_d + n_i + n_de = 11, scheme=L1-L2-projection, convention=zeta-vs-Zubarev, L_max=5)`

### 9. PASS / FAIL / INFO thresholds
- **PASS**: n_diagnostic ≥ 3 AND n_degenerate ≤ 2 (at least 3 observables expose layer-gap; at most 2 are fully layer-insensitive). Expected: (3-5 diagnostic, 4-6 intermediate, 2-3 degenerate).
- **FAIL**: n_degenerate ≥ 9 OR n_diagnostic = 0 AND all 11 are degenerate (layers indistinguishable at observable level — refutes Three-Layer Theorem's physical relevance) — OR — n_diagnostic ≥ 10 with no inheritance structure (CC1 broken; suggests computational error).
- **INFO**: Borderline distribution (n_diagnostic = 2 or n_degenerate = 3) — theorem physically relevant but the split classification needs refinement; trigger cross-check audit.

Tolerance rule: ABSOLUTE (integer counts relative to pre-declared thresholds).

### 10. Substitution chain (required — trigger is `[VERIFY]`)

Claim: "w_0 split is DIAGNOSTIC (|split| > 0.05) with sign |w_0|_L1 < |w_0|_L2 = 0.998."

Chain:
1. **Def**: w_0 = equation-of-state of dark energy today; in substrate framework, w_0 derives from the a_0 / a_2 ratio modulated by the chirality factor χ.
2. **Def**: L2 (Zubarev): χ = +1 (KO=6 chirality alignment verified in W1-G1), w_0_L2 = -0.998 (G51 primary).
3. **Def**: L1 (zeta): χ = 0 (zeta has no explicit Λ dependence; d²S/d(logΛ)² = 0 structurally).
4. **Substitute**: w_0 = -1 + ε(χ) · (residual). For χ = +1, ε = +0.002 (positive deviation from -1). For χ = 0, ε_L1 = 0 → w_0_L1 ≈ -1 + 0·(residual) = -1 to leading order in chirality-modulation.
5. **Simplify**: w_0_L1 ≈ -1.000, w_0_L2 = -0.998.
6. **Compute split**: |split| = |w_0_L1 - w_0_L2| / |w_0_L1| = |-1.000 - (-0.998)| / |-1.000| = 0.002 / 1.000 = 0.002.
7. **Canonical form**: |split|_w0 ≈ 0.002.
8. **Read off**: 0.002 ∈ [0.001, 0.05] → **INTERMEDIATE**, not DIAGNOSTIC.

CORRECTION: The a priori expectation from the chain is INTERMEDIATE, not DIAGNOSTIC. This chain DOES NOT pre-determine PASS — it shows that w_0 alone is not expected to carry the diagnostic signal. The diagnostic observables are those whose substrate origin is more direct (e.g., A_s via H_tilde, which is heavily L2-dependent; f_conv via cluster = 1766, which is NOT-R-protected primary L3-OB).

9. **Extended substitution** to locate diagnostic: A_s = f(H_tilde, eps_H, M_Pl^2); under L2 Zubarev, H_tilde_TD = 5.907e-3; under L1 zeta, H_tilde_L1 = structurally different (zeta has no Λ, so H_tilde_L1 requires a substitution using residue of zeta at s=4; this is NOT numerically equal to the heat-kernel integration).
10. **Prediction**: A_s split expected DIAGNOSTIC (≥0.05). f_conv split expected DIAGNOSTIC. m_H split expected DEGENERATE (a_2 robust). H_0 split expected DEGENERATE (a_0 robust). Full table emerges from computation.

Conclusion: Substitution chain supports PASS classification with at least 3 diagnostic (A_s, f_conv, plus at least one of {n_s propagation, α_s, Ω_GW}) and at most 2 degenerate (m_H, H_0).

### 11. What PASSES / FAILS mean for solution space
- **PASS**: L1 and L2 are PHYSICALLY distinguishable in framework-target observables. The Three-Layer Theorem has observational content; regulator choice at the substrate-action layer is not a vacuous mathematical distinction. Supports the claim that S83 G51's Zubarev primary vs mixed-scheme split is a real framework prediction. Enables downstream discrimination tests where framework predicts observable-level split that LCDM does not.
- **FAIL (n_degenerate ≥ 9)**: L1 and L2 collapse at observable level — the three-layer distinction is mathematically meaningful but physically inert. §VII.M remains a theorem of NCG-book-keeping, not of framework phenomenology. The substrate's self-determination act at L2 has no observational consequence beyond L1. Serious reduction of §VII.M's observational weight.
- **FAIL (n_diagnostic ≥ 10 without inheritance)**: CC1 broken; α_s is not tracking n_s. Signals computational error OR that the layer-projection introduces a spurious additional freedom not present in the original theorem. Must debug before landing is trusted.
- **INFO**: Theorem coherent but exact split classification is fragile — some observables are right at the 0.05 or 0.001 boundary. Carry-forward: refine boundary definitions in W2c, possibly add INTERMEDIATE as a permanent category rather than a residual.

### 12. Effort estimate
1-1.5 sessions. Heavy — GPU eigenvalue decomposition of D_K at L_max=5 for 11 observable evaluations. Single-agent with careful per-observable L1 vs L2 evaluation. Substantive computation; largest compute load in W2a.

### 13. Substrate-framing reminder
Included verbatim at top of the dispatch prompt (§6). L1 and L2 are strata of the substrate's self-determination, not choices imposed by an analyst. A DIAGNOSTIC split is the substrate exposing the gap; a DEGENERATE split is the substrate hiding it at observable scale. Direction: substrate → L1/L2 stratum → spectral moment → observable.

---

## W2a → W2b / W2c Parallel Dispatch Note

W2a is self-contained: gates 11-14 can be dispatched in parallel (4 concurrent agents). Per feedback `feedback_dispatch-discipline.md`, self-impose ≤~8 concurrent cap — W2a alone uses 4 slots. If W2b (gates 15-20) and W2c (remaining) are to be co-dispatched, verify total dispatch count stays ≤8.

Inter-gate dependency within W2a:
- Gate 11 (landing) depends on S83 W1-G1 and W1-G3 verdicts being on disk — already verified in prerequisites.
- Gate 12 (falsifier) is INDEPENDENT of Gate 11 (tests the theorem body even if landing has not yet succeeded — test-first discipline).
- Gate 13 (atlas column) is INDEPENDENT of Gates 11, 12 (operates on §VII.K-DUAL, not §VII.M).
- Gate 14 (L1-L2 projection) is INDEPENDENT of Gates 11-13 (operates on the observable table directly).

All four dispatches can run concurrently.

---

## W2a → W3 Decision Point (joint with W2b + W2c)

After W2a + W2b + W2c close, the W3 decision point for §VII.M is:

- **4/4 W2a gates PASS** + W2b/W2c layer-related gates clean → W3 proceeds with §VII.M landed and used downstream (MP-LAYER-AUDIT, PIN-DERIVATION-CENSUS, COCYCLE-CENSUS in W2b depend on landing).
- **W2a-11 PASS + W2a-12 INFO (theorem-refined)** → W3 re-scopes §VII.M to the KO-6 class; subsequent W2b/W2c gates carry an anchor-restriction tag.
- **W2a-11 FAIL** → W3 defers all §VII.M-downstream gates; re-dispatches a minimal landing correction in W3.
- **W2a-14 FAIL (n_degenerate ≥ 9)** → §VII.M remains book-keeping; re-scope downstream obs-targeting gates (W2c observational forecasts) to avoid claiming layer-level discriminators.

---

## W2a Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness, W2a enumerates the following free parameters and pins each:

| Parameter | Pin | Source |
|:----------|:----|:-------|
| L_max | 5 | Inherited from W1-G1, W1-G3 |
| τ_fold | 0.19 | canonical_constants (tau_fold) |
| M_KK | canonical | canonical_constants (M_KK) |
| Λ_Zubarev | M_KK | S83 W1-G1 convention |
| Regulator set | {zeta, Zubarev, SDW, dim-reg, lattice-BR} | S83 5-regulator atlas |
| Tolerance (W2a-11) | SHA-256 exact, slot availability | §VII.M landing protocol |
| Tolerance (W2a-12) | |χ| > 0.1, R² > 0.99 | L2 three-criterion; Weyl fit |
| Tolerance (W2a-13) | ±1 L0/L3/UNPINNED; exact L1/L2 | Structural singleton rule |
| Tolerance (W2a-14) | 0.05 diagnostic / 0.001 degenerate | Pre-registered observable-split bands |
| Spectral triple family (W2a-12) | {HP⁴, Spin(8)-ext, T⁴, T⁸} | Pre-registered four-family set |
| Observable set (W2a-14) | 11 fixed {A_s, m_H, n_s, α_s, μ, r, f_NL, w_0, σ_8, H_0, Ω_GW} | Pre-registered framework-target set |
| Random seed | 84 | Fixed; documented in prompt |
| GPU path | torch.linalg.eigvalsh / eigvals | Matrix sizes 16 (HP⁴), 112 (Spin8), 256 (T⁸), ~40000 (D_K-L5) |
| CPU fallback | OMP_NUM_THREADS=8 | If GPU unavailable |
| Scheme labels | L0-INT / L1-AX / L2-SA / L3-OB / UNPINNED | Pre-declared 5-label set |

Any verdict line post-computation that does not cite the full 4-tuple (value, scheme, convention, L_max) plus full 64-char SHA-256 closure is REJECTED by the verdict-file consolidator (per `.claude/rules/gate-verdicts.md`).

---

## W2a Input-SHA Ledger

All SHAs below must be resolved to full 64-character hexdigests BEFORE W2a dispatch. Shorthand (e.g., `227a5913...`) used in the context above is INDICATIVE ONLY; the scripts must `grep` and substitute the full value.

| SHA key | Status | Source file |
|:--------|:-------|:------------|
| anchor_W1_G1_sha256 | READ-AT-DISPATCH | `computations/s83_gate_verdicts.txt` |
| anchor_W1_G3_sha256 | READ-AT-DISPATCH | `computations/s83_gate_verdicts.txt` |
| anchor_G57_sha256 | READ-AT-DISPATCH | `computations/s83_gate_verdicts.txt` |
| anchor_G58_sha256 | READ-AT-DISPATCH | `computations/s83_gate_verdicts.txt` |
| anchor_G62_sha256 | READ-AT-DISPATCH | `computations/s83_gate_verdicts.txt` |
| anchor_G46_sha256 | READ-AT-DISPATCH | `computations/s83_gate_verdicts.txt` |
| anchor_G51_sha256 | READ-AT-DISPATCH | `computations/s83_gate_verdicts.txt` |
| anchor_G32_sha256 | READ-AT-DISPATCH | `computations/s83_gate_verdicts.txt` |
| anchor_S82_AS_sha256 | READ-AT-DISPATCH | `computations/s82_gate_verdicts.txt` |
| anchor_S82_FIRAS_sha256 | READ-AT-DISPATCH | `computations/s82_gate_verdicts.txt` |
| canonical_constants_sha256 | COMPUTE-AT-DISPATCH | `computations/canonical_constants.py` |
| D_K_L5_spectrum_sha256 | COMPUTE-AT-DISPATCH | `computations/s83_D_K_L5_spectrum.npz` (or predecessor) |
| registry_target_pre_edit_sha256 | COMPUTE-AT-DISPATCH | `sessions/framework/permanent-results-registry.md` |
| HP4_spec_pin | STATIC | `"HP4-AtiyahBottShapiro-symplectic-KO0"` |
| Spin8_spec_pin | STATIC | `"Spin8-Bourbaki-fundamental-root-system"` |
| T4_spec_pin | STATIC | `"flat-torus-d4-standard"` |
| T8_spec_pin | STATIC | `"flat-torus-d8-standard"` |

All READ-AT-DISPATCH SHAs must be verified full 64-char length before being consumed; each script rejects shorter.

All COMPUTE-AT-DISPATCH SHAs are generated by the script in its first 20 lines of stdout and recorded in the output `.log` file.

---

**End of W2a plan.** Four gates fully specified. Dispatch-ready.
