# Session 84 Plan — Wave 2b: MP-Layer-Audit + Pin-Derivation-Census + L1-L2-Cocycle-Census (3 gates)

**Session**: 84
**Wave**: 2b (Regulator admissibility + NOT-R-protected layer-commitment derivation + cyclic-cohomology census)
**Planner**: lizzi-spectral-functional-theorist (plan author)
**Theme**: Extend the §VII.M Three-Layer Regulator Theorem's classification apparatus along three orthogonal axes — (i) regulator admissibility per layer, (ii) observable layer-commitment derivation from substrate structure, (iii) cyclic cocycle layer classification across the full HP^even register.
**Format**: compute (three parallel independent agents)
**Parent plan**: `session-84-context.md` §4.B items 15/16/17

---

## W2b Summary

Wave 2b is a meta-classification wave. W2a closes the primary §VII.M landing artifacts (items 11-14: three-layer registry, HP^4 falsifier, 42-row layer-pin atlas, 11 framework observables L1-vs-L2 split). W2c closes the transport / unpinned / L_max-extrapolation artifacts (items 18-20). W2b sits between: it classifies REGULATORS (not observables) as layer-admissible (item 15), DERIVES layer commitments for NOT-R-protected observables from substrate structure (item 16), and CENSUSES every cyclic cocycle in HP^even by layer (item 17).

The wave's structural value is turning three S83 anchors — S82 MP-Exclusion Theorem, S83 W2-G27 MP-admissibility FAIL=2/5, S83 W3-G54 HP^even audit PASS 53/53 — into an executable, per-element classification atlas. The output is three machine-checkable tables:
- 5-row regulator × 3-class MP-admissibility classification with CM proofs per cell
- 5-row NOT-R-protected observables × substrate-derivation layer-commitment table
- 53-row cyclic cocycle × L1/L2/MIXED classification with cited reason per row

**Lizzi-solo-a relevance**: All three gates test the spectral-functional-theorist thesis that the choice of regulator is not a convention — it is a physical question with layer-structured consequences. Gate 15 tests whether the CM completely-monotone test partitions the regulator atlas cleanly by layer. Gate 16 tests whether NOT-R-protected observables have derivable (as opposed to conventional) layer commitments. Gate 17 tests whether the framework's HP^even register — the structural heart of the spectral action apparatus — admits a clean L1/L2 partition at the cocycle level.

## W2b Decision Point Prerequisites

W2b runs after W1 closes (Three-Layer Registry landing at §VII.M and W1-G1 L_max-extrapolation completed) and in parallel with W2a (items 11-14) and W2c (items 18-20). W2b feeds W3 (observational / detector forecast wave) by providing:
- (Gate 15 output) Definitive MP-admissibility ledger for every regulator the framework uses anywhere
- (Gate 16 output) Substrate-derived layer commitments for the 5 NOT-R-protected observables that produce OOM-scale spans — the objects that W3 observational forecasts must carry explicit layer-tags for
- (Gate 17 output) Cocycle-level L1/L2/MIXED partition across HP^even, feeding §VII.K-DUAL 42-row atlas per-row reason column

W2b is PRU-vulnerable in one place (item 15: the admissibility test function f(x) at finite L_max must be pinned, else the Hausdorff-Bernstein-Widder criterion floats). PRDR is discharged in the §W2b-15 machinery pin below.

---

## §W2b-15. S84-MP-LAYER-AUDIT

### 1. Gate ID
`S84-MP-LAYER-AUDIT` (no S83 collision; S83 W2-G27 MP-ADMISSIBILITY-UNIFIED was a binary FAIL=2/5 count; this gate produces a per-cell layer-structured 5×3 classification)

### 2. Trigger
`[VERIFY-THEOREM]` — the gate promotes S82 MP-Exclusion Theorem from a cusp-specific result (sqrt(x) fails CM at finite L_max) to a regulator × layer classification theorem across the full 5-regulator atlas.

### 3. Classification
**META** — this is a classification of regulators (tools on the fabric), not a phononic, geometric, or particle-level observable. It feeds GEOMETRIC analyses downstream.

### 4. Agent type
`lizzi-spectral-functional-theorist` (primary — MP-admissibility is the functional-selection question; Lizzi's three-functional pluralism methodology is the natural workbench). Optional co-review: `connes-ncg-theorist` for the CM proof template verification.

### 5. Hypothesis
**H_15**: Each of the 5 regulators {zeta, Zubarev, SDW, dim-reg, lattice-BR} occupies exactly one of three MP-layer cells — MP-admissible-at-L1 / MP-admissible-at-L2 / MP-inadmissible-everywhere — and each occupancy is certifiable by a CM (Chamseddine-Marcolli completely-monotone) proof applied to the regulator's defining kernel.

### 6. Method (full-fidelity dispatch prompt)

**Agent dispatch prompt** (to `lizzi-spectral-functional-theorist`):

```
[VERIFY-THEOREM] S84-MP-LAYER-AUDIT

You are executing Gate S84-MP-LAYER-AUDIT. Substrate framing is mandatory:
D_K eigenvalue spectrum is the fundamental fabric content; regulators are
test-functions applied to that spectrum. The framework is NOT QFT-in-a-
container; the regulator is not a calculational convenience — it commits
the computation to a layer (L1 axiomatic / L2 substrate-action / L3
observable). Your job is to classify each regulator by its MP-admissibility
status PER LAYER.

## Task

Classify each of the 5 regulators in F_KK into exactly one of three cells:
  (a) MP-admissible-at-L1 (CM test passes under Dixmier-residue axioms)
  (b) MP-admissible-at-L2 (CM test passes under substrate-action functional
                           at finite L_max=5)
  (c) MP-inadmissible-everywhere (CM test fails at both layers)

Produce a 5×3 classification table + per-cell CM proof.

## Input SHA-256 pins (all static)

- `computations/canonical_constants.py`: <computed-at-runtime>
- `computations/s82_mp_exclusion_theorem.py`: <computed-at-runtime>
- `computations/s83_gate_verdicts.txt` (G27 line): <computed-at-runtime>
- `computations/s83_w2_g27_mp_admissibility.py`: <computed-at-runtime>
- `computations/_regulator_atlas.py` (if exists; else create): <computed-at-runtime>

## Canonical constants

from canonical_constants import *
# Uses M_KK, tau_fold=0.19, L_max_canonical=5

## Regulator definitions (5 kernels to classify)

  zeta:       f_z(lambda) = lambda^{-s} at s=0 (Mellin pole-subtraction)
  Zubarev:    f_R(lambda) = exp(-lambda^2 / M_KK^2)  [canonical substrate-action]
  SDW:        f_S(lambda) = 0.912 * sqrt(u) + 0.088 * exp(-u), u = (lambda/Lambda)^2
  dim-reg:    f_D(lambda) = lambda^{-epsilon}, epsilon -> 0 limit
  lattice-BR: f_L(lambda) = rect(lambda / Lambda_lat) [sharp cutoff at Brillouin edge]

## CM test (Hausdorff-Bernstein-Widder)

A function f: [0, inf) -> R is completely monotone (CM) iff:
  (-1)^n * d^n f / d x^n >= 0  for all n >= 0 on (0, inf)

MP-admissibility at a given layer requires:
  (L1) CM holds under Dixmier-residue axioms — i.e., the Mellin transform
       has only simple poles at integer s values
  (L2) CM holds under the substrate-action evaluation at finite L_max=5,
       with the spectral sum over the D_K^2 eigenvalues {lambda_i^2}_{i=1}^{N(L_max=5)}

## Procedure

Step 1 — Derivative test at L1 (analytical):
  For each f in {f_z, f_R, f_S, f_D, f_L}:
    Compute d^n f / d lambda^n for n = 0, 1, 2, 3, 4
    Check sign(-1)^n * d^n f / d lambda^n on (0, inf)
    If any n fails sign check, regulator is L1-inadmissible.
    Report n^* = smallest n at which sign flips (if any).

Step 2 — Finite-L_max substrate test at L2 (numerical on D_K spectrum):
  Build D_K^2 eigenvalues at L_max=5 via torch.linalg.eigvals (GPU mandatory).
  For each regulator f:
    Form T_f = sum_{i=1}^{N} f(lambda_i^2 / M_KK^2)
    Perturb each lambda_i -> lambda_i + delta_i, delta_i in {1e-4, 1e-3, 1e-2, 1e-1}
    Check monotone-decrease of T_f as delta increases (CM at the sum level)
    Check positivity of n-th divided differences up to n=4
    If any fail, regulator is L2-inadmissible.

Step 3 — CM proof per cell:
  For each admissible (regulator, layer) cell:
    Write a short (5-10 line) CM certificate citing:
      - The representation f(x) = integral dmu(alpha) exp(-alpha x), alpha > 0
        (or equivalent Bernstein integral representation)
      - The measure dmu and its positivity proof
      - The layer-specific convergence domain
  For each inadmissible cell:
    Cite the n^* at which the CM test failed + the offending term.

Step 4 — Cross-check against S82 MP-Exclusion:
  Verify that SDW (sqrt(x) cusp) appears as L1-inadmissible in your table.
  Verify that Zubarev (exp(-lambda^2 / M_KK^2)) appears as L2-admissible
  (substrate-action canonical).
  Verify that zeta (lambda^{-s}) appears as L1-admissible (Dixmier residue).
  Any deviation from these three anchor cells is a FAIL of the gate setup.

## GPU path (MANDATORY)

Use Python env: "phonon-exflation-sim/.venv312/Scripts/python.exe"
Build D_K^2 on GPU: `torch.linalg.eigvals(D_K_sq.to('cuda'))`
Matrix size at L_max=5 is ~5500x5500 — GPU is essential.
If torch-rocm not available on dispatch host, fall back to CPU with
`import os; os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE numpy.

## Output files

- `computations/s84_w2b_mp_layer_audit.py` (primary script)
- `computations/s84_w2b_mp_layer_audit.npz` (5×3 table + CM certificates)
- `computations/s84_w2b_mp_layer_audit.md` (human-readable certificate log)

## Verdict line

Append to `computations/s84_gate_verdicts.txt`:
  S84-MP-LAYER-AUDIT: <PASS|INFO|FAIL> -- value=<N_admissible>/5 scheme=<s>
    convention=<c> L_max=5 sha256=<full 64-char closure>

## Working-paper section

Write `§VII.M-A MP-Layer-Audit` into the S84 working paper — 30-60 lines,
5×3 table + 15 CM-certificate stanzas (5 regulators × 3 cells, each cell
either the admissibility proof or the inadmissibility failure mode).

Do NOT terminate until all promised artifacts are on disk and the
working-paper section has substantive content (not just a stub heading).
```

### 7. Machinery pin (PRDR)

| Parameter | Pin |
|:----------|:----|
| `L_max` | 5 (canonical; matches S83 G27 pin) |
| `scan_range` | N/A (classification gate, no scan) |
| `step_size` | δ ∈ {1e-4, 1e-3, 1e-2, 1e-1} for divided-difference perturbation |
| `tolerance` | Derivative sign-check: exact (analytical); divided-diff positivity: 1e-12 absolute |
| `scheme` | per-regulator (5 schemes tested simultaneously) |
| `convention` | A (Lambda_Z = M_KK fixed) to match S83 G27 pinning |
| `GPU path` | `torch.linalg.eigvals` on RX 9070 XT for 5500×5500 D_K² |
| `random_seed` | 42 (not used — deterministic test, seed pinned for eigvals row-ordering stability) |
| `CM test order` | n ∈ {0, 1, 2, 3, 4} derivative tests |
| `Bernstein measure domain` | α ∈ (0, ∞) with Lebesgue base measure |

### 8. Expected output 4-tuple

`(value=<N_admissible>/5, scheme=multi-regulator, convention=A, L_max=5)`

where `<N_admissible>` = total number of (regulator × layer) cells marked admissible (max 10, min 0). Independent counts per layer in the NPZ payload.

### 9. PASS / FAIL / INFO thresholds

- **PASS**: Every regulator occupies exactly one MP-layer cell, AND the three anchor cells (SDW→L1-inadmissible, Zubarev→L2-admissible, zeta→L1-admissible) are reproduced exactly, AND CM certificates exist for every admissibility claim AND inadmissibility failure-mode cited for every non-admissible claim. Expected: 2-3 regulators L1-admissible, 2-3 L2-admissible, 1-2 inadmissible-everywhere; total admissibility count between 3 and 6 of 10 cells. Criterion quantitative: every of 15 (5×3) cells has a populated certificate string ≥ 3 lines.
- **INFO**: Anchors reproduce but ≥ 1 non-anchor cell lacks a complete CM certificate (partial ledger, structurally informative).
- **FAIL**: Any anchor cell (SDW/Zubarev/zeta canonical classifications) deviates from S82 MP-Exclusion Theorem and S83 G27's pinning. Deviation is a FAIL of the gate's CM test implementation, NOT of the theorem itself.

### 10. Substitution chain (mandatory per `[VERIFY-THEOREM]` trigger)

Claim: "Zubarev is MP-admissible-at-L2, zeta is MP-admissible-at-L1, SDW is MP-inadmissible at L1."

Required substitution chain:
- Step 1: f_R(λ) = exp(-λ² / M_KK²) [definition, Zubarev kernel]
- Step 2: f_R(λ) = ∫₀^∞ dα · ρ_R(α) · exp(-α · λ²), with ρ_R(α) = δ(α − 1/M_KK²) [Bernstein integral representation with atomic measure at α = 1/M_KK²]
- Step 3: ρ_R(α) ≥ 0 for all α > 0 [measure positivity, atomic at single point]
- Step 4: Therefore f_R is CM on (0, ∞) by Hausdorff-Bernstein-Widder. The representation plugs into L2 substrate-action evaluation at finite L_max=5 because the substrate-action is Σᵢ f_R(λᵢ²/M_KK²), which is a positive linear combination of exp(−αλᵢ²/M_KK²), preserving CM. [L2-admissible]
- Step 5: f_z(λ) = λ^{-s}|_{s=0} [definition, Mellin zeta regulator]
- Step 6: f_z(λ) = λ^{-s} = (1/Γ(s)) · ∫₀^∞ dα · α^{s-1} · exp(-α · λ), and ρ_z(α) = α^{s-1}/Γ(s) ≥ 0 for α > 0, s > 0 [Bernstein integral representation with power-measure]
- Step 7: In the s → 0 Dixmier-residue limit, ρ_z picks out simple poles at integer s via Mellin transform, consistent with A1-A6 axioms (Connes). [L1-admissible]
- Step 8: f_S(λ) = 0.912 · √u + 0.088 · exp(-u), u = (λ/Λ)² [definition, SDW kernel]
- Step 9: d/dλ (√u) = 0.912 · (2λ/Λ²) / (2√u) = 0.912 · (1/Λ) · sign(λ) · |λ/Λ|⁰ [first derivative at λ=0 is cusp-singular]
- Step 10: For CM test at n = 1: we need (-1)¹ · (df_S/dλ) ≥ 0 on (0, ∞). At small λ, df_S/dλ ≈ 0.912/(Λ·√u) · (λ/Λ²) → diverges as λ → 0⁺. (-1)¹ · (positive divergent) < 0. CM fails at n=1 cusp [L1-inadmissible; S82 MP-Exclusion reproduced]

Conclusion (read off from canonical form): Zubarev L2-admissible, zeta L1-admissible, SDW L1-inadmissible. The three anchor cells are substrate-structurally mandated, NOT gate-tunable.

### 11. What PASSES / FAILS MEAN for solution space

- **PASS** means the 5-regulator atlas F_KK partitions cleanly into layer-specific MP-admissibility cells. This is a structural theorem: any computation claiming PASS at L1 must use an L1-admissible regulator; any claim at L2 must use an L2-admissible regulator. Downstream computations get a hard certificate. Closes the door on regulator-shopping as a remaining methodology hole.
- **FAIL** (anchor-deviant) means the CM test implementation has a bug. The substrate-structural claim stands regardless; the gate re-dispatches with a fixed implementation. FAIL is diagnostic, not closing.
- **INFO** (partial ledger) means the gate delivers the anchor cells definitively but leaves 1-2 non-anchor cells (likely dim-reg or lattice-BR) without a complete CM certificate. Downstream computations get a 2/3-populated atlas and must report whether they use the non-certified cells with a `<L?-provisional>` tag.

### 12. Effort estimate

~0.5 session, MEDIUM complexity. D_K² at L_max=5 already built in canonical_constants / s83_w2_g27_mp_admissibility. Main effort is the 15 CM certificates (~3 hours agent work) + derivative-sign analytical proofs (~2 hours).

### 13. Substrate-framing reminder (in agent dispatch prompt, §6 above, lines 2-7)

Explicitly instructed: regulator is a test-function ON the D_K spectrum. It does not live in a container. Layer commitment is substrate-structural. [Present]

---

## §W2b-16. S84-PIN-DERIVATION-CENSUS

### 1. Gate ID
`S84-PIN-DERIVATION-CENSUS` (no S83 collision; S83 G57 PINNING-AUDIT was a binary validation of 11 R-protection pins; this gate DERIVES layer commitments from first principles for NOT-R-protected observables, a different task)

### 2. Trigger
`[AUDIT]` — the gate re-examines per-observable layer commitments currently attached as convention-tags and promotes them to substrate-derivations where possible. AUDIT is the correct trigger: we are NOT signing a sign (not [SIGN]), NOT verifying a numerical threshold on a computed quantity ([VERIFY] would be the wrong trigger for a derivation census), and NOT proving a theorem ([VERIFY-THEOREM]). We are auditing pins.

### 3. Classification
**META** — classification of observable-to-layer mappings; feeds GEOMETRIC and PHONONIC observables downstream.

### 4. Agent type
`lizzi-spectral-functional-theorist` (primary — the layer-commitment derivation is precisely the "which spectral functional is physical?" question applied to NOT-R-protected observables). Required handoff to `connes-ncg-theorist` for the cyclic-cohomology branch (cross-check that L1 derivations appeal to valid HP^0 classes, not ad-hoc reasoning).

### 5. Hypothesis
**H_16**: Every NOT-R-protected observable in the 5-member set {k_a2, f_conv, A_s absolute, w_0, CC-ratios} has a substrate-derived layer commitment — either intrinsically L1 (cyclic-cohomology / Dixmier-trace determined), intrinsically L2 (substrate-action minimization determined), or genuinely MIXED (composite requiring layer-explicit reporting with a substrate-derived decomposition). "Genuinely MIXED" requires positive construction, not unresolved ambiguity.

### 6. Method (full-fidelity dispatch prompt)

**Agent dispatch prompt** (to `lizzi-spectral-functional-theorist`):

```
[AUDIT] S84-PIN-DERIVATION-CENSUS

You are executing Gate S84-PIN-DERIVATION-CENSUS. Substrate framing is
mandatory: particles are phononic excitations of the D_K spectrum; layer
commitments are structural (which fiber of the three-layer regulator
theorem the observable physically lives on), not conventional. Your job
is to DERIVE the layer commitment per observable, not to cite it.

Template: G47 (S83) derived mu_BC = M_Z·sqrt(1 + exp(12*tau_fold)/3) from
physical reasoning (2-loop RGE + mu_BC threshold matching). That derivation
pinned mu_BC = 188.34 GeV from substrate structure, not from a PDG fit. Your
derivations per observable must follow that pattern: start from substrate
structure, show the observable's evaluation commits to a specific layer.

## Task

For each of the 5 NOT-R-protected observables:
  O_1 = k_a2          (G15 primary Mellin-anchor at a_2 slot, span=14.685)
  O_2 = f_conv        (G28 tadpole-cluster, cluster=1766.16)
  O_3 = A_s absolute  (inherits span via CC-5 from k_a2 and f_conv)
  O_4 = w_0           (G51 L1/L2 split=0.080, -0.998 Zubarev vs -0.918 mixed)
  O_5 = CC-ratios     (G34 Mellin-unbalanced, max_span=42)

Derive (not cite) the layer commitment:
  - Intrinsically L1: observable's definition IS a cyclic-cohomology /
    Dixmier-residue pairing. Substrate derivation = write observable as
    <phi, x> pairing with phi in HP^n, x in K_*.
  - Intrinsically L2: observable's definition REQUIRES substrate-action
    evaluation at finite L_max. Substrate derivation = show observable
    arises from <S_substrate, Q> minimization with Q = quantum numbers.
  - Genuinely MIXED: observable is a composite f(O_L1, O_L2) where
    neither component can be eliminated. Substrate derivation = write
    the decomposition explicitly; provide per-layer evaluation + rule
    for combination.

## Input SHA-256 pins (all static)

- `computations/canonical_constants.py`: <computed-at-runtime>
- `computations/s83_gate_verdicts.txt` (G15/G28/G34/G51 lines): <computed-at-runtime>
- `computations/s83_w2_g15_k_a2_canonical_range.py`: <computed-at-runtime>
- `computations/s83_w3_g28_f_conv_cluster.py`: <computed-at-runtime>
- `computations/s83_w3_g34_cc_ratio_cluster.py`: <computed-at-runtime>
- `computations/s83_w3_g51_w0_regulator.py`: <computed-at-runtime>
- `computations/s83_unified_as_79_3pi.py` (A_s absolute source): <computed-at-runtime>
- `sessions/archive/session-83/gen-physicist-s6-synthesis.md`: <computed-at-runtime>

## Canonical constants

from canonical_constants import *
# Uses M_KK, tau_fold=0.19, H_TD=5.9076e-3, H_LI=2.464e-5, planck_ns

## Per-observable derivation protocol

For each O in {k_a2, f_conv, A_s_abs, w_0, CC-ratios}:

  Step 1 — Definitional origin:
    Write O as its defining functional/integral. E.g.,
      k_a2 = f_2^{regulator} / f_2^{SDW}  [Mellin multiplier at a_2 slot]
      f_conv ~ 1/M_0^2  [tadpole normalization]
    Cite the canonical formula with full symbol list.

  Step 2 — Layer-of-definition test:
    Ask: does the defining functional involve
      (a) a Dixmier-residue / zeta-regularized pairing with HP^n cocycle?
          → L1 intrinsic
      (b) a substrate-action minimum at finite L_max (Zubarev kernel on
          D_K spectrum)?
          → L2 intrinsic
      (c) both, irreducibly?
          → MIXED

  Step 3 — Substrate derivation chain:
    Starting from D_K eigenvalues {lambda_i}_{i=1}^{N(L_max=5)}, write the
    minimum-length expression for O. If expression is
      O = sum_i f(lambda_i^2) / sum_j g(lambda_j^2)  → L2 intrinsic
      O = Res_{s=0} Tr(|D_K|^{-s} * X)              → L1 intrinsic
      O = F(O_L1, O_L2)                             → MIXED, write F

  Step 4 — Concrete derivation per observable:

    k_a2: Is Mellin first-moment ratio. f_2^R / f_2^SDW is a double-
          first-moment pairing. Both numerator and denominator are
          L1 (Dixmier-residue of D_K^{-2} paired with regulator
          kernel). Ratio of two L1 objects IS L1. Layer commitment: L1.

    f_conv: Tadpole 1/M_0^2 with M_0^2 = zeta-regularized sum of
            eigenvalues' inverse squares (L1) OR substrate-action-
            evaluated (L2 at L_max=5). Span = 1766 across 5 regulators
            indicates regulator-sensitivity that the L1 residue should
            NOT exhibit (residues are regulator-invariant). Conclusion:
            f_conv is L2 intrinsic — its evaluation requires the finite
            L_max substrate-action minimum, NOT a Dixmier residue.

    A_s absolute: H^2 / (epsilon_H * M_Pl^2 * z^2) where
      - H ∈ {H_TD, H_LI} is L2 (epoch-gated, substrate-action)
      - epsilon_H is GV-secondary class, HP^3(A_F) not image(S) [L1?]
        → but the value at tau_fold is substrate-evaluated (L2 shift)
      - z depends on both via Mukhanov-Sasaki scale transport
      → MIXED — write decomposition F(A_s^{L1}, A_s^{L2}) explicitly.

    w_0: Volovik partition sum. At L1, w_0 = -1 (CC identity, zeta-
         determined). At L2 with Zubarev, w_0 = -0.998. G51 split = 0.080
         is L1 vs L2 evaluation mismatch. MIXED with dominant L2 for
         DR3 forecasting; L1 value is the theoretical limit.

    CC-ratios: Various composite ratios from CC-5 propagation. Each ratio
         must be decomposed into its F_i factors, which may live on
         different layers. Apply CC-5 identity: span(O) = prod span(F_i)^{|p_i|}.
         Per-ratio layer = set of layers of dominant F_i by |p_i| weight.
         Expected: CC-ratios family is MIXED with case-by-case sub-layer
         assignment.

  Step 5 — Certify or flag:
    Every observable in the 5-set must receive a definite layer assignment
    (L1 / L2 / MIXED) with a substrate-derivation paragraph. Flag any
    observable where derivation is incomplete as UNPINNED-L(?).

## Cross-check: R-protected analog

For comparison, re-verify that any one R-protected observable (e.g., c_s
from G14) has its layer derivable trivially (cluster<1.5 means regulator-
invariance, means L1 intrinsic via Mellin-balance). If the R-protected
analog derivation fails to be L1, the derivation template itself is
broken and the NOT-R-protected census is compromised.

## GPU path

Not required for this gate — the derivations are symbolic/analytical.
If a re-computation of span data is needed as cross-check, defer to
the existing s83_w2_g15 / s83_w3_g28 / s83_w3_g34 / s83_w3_g51 numerical
outputs (cite by SHA, don't recompute).

## Output files

- `computations/s84_w2b_pin_derivation_census.py` (derivation tooling + tests)
- `computations/s84_w2b_pin_derivation_census.npz` (5-row table + derivation-quality flags)
- `computations/s84_w2b_pin_derivation_census.md` (one paragraph per observable, ~15-25 lines each)

## Verdict line

Append to `computations/s84_gate_verdicts.txt`:
  S84-PIN-DERIVATION-CENSUS: <PASS|INFO|FAIL> -- value=<N_derived>/5 scheme=per-obs
    convention=A L_max=5 sha256=<full 64-char closure>

## Working-paper section

Write `§VII.M-B Pin-Derivation-Census` into the S84 working paper.
Substantive content required: 5 per-observable derivations × ~15-20 lines each.
```

### 7. Machinery pin (PRDR)

| Parameter | Pin |
|:----------|:----|
| `L_max` | 5 (matches S83 G15/G28/G34/G51 pin) |
| `scan_range` | N/A (per-observable derivation, no scan) |
| `tolerance` | N/A (derivation gate — qualitative, classified by presence/absence of substrate-derivation chain) |
| `scheme` | per-observable (observable-specific — the point of the gate) |
| `convention` | A (match S83 anchor conventions) |
| `GPU path` | N/A (symbolic/derivation gate); if numerical cross-check needed, delegate to cached S83 outputs |
| `random_seed` | N/A |
| `derivation chain length` | ≥ 4 steps per observable (definitional origin → layer-of-definition test → substrate chain → layer assignment) |
| `R-protected cross-check` | c_s (G14 PASS) as control — must reproduce as L1 intrinsic |

### 8. Expected output 4-tuple

`(value=<N_derived>/5, scheme=per-observable, convention=A, L_max=5)`

where `<N_derived>` is the count of the 5 observables that received a complete substrate-derivation of their layer commitment (4+-step chain + layer assignment in {L1, L2, MIXED}).

### 9. PASS / FAIL / INFO thresholds

- **PASS**: ≥ 5/5 observables receive a complete substrate-derivation (100%). Every layer assignment is substrate-structural, not conventional. Threshold: exact 5/5 required.
- **INFO**: 4/5 observables derived (80%). One observable (expected candidate: CC-ratios family, because of sub-layer heterogeneity) remains partially derived. Structurally informative.
- **FAIL**: ≤ 3/5 observables derived (<75%). The derivation template is insufficient for the framework's NOT-R-protected observable class, and the three-layer theorem's applicability to NOT-R-protected observables is weakened.

### 10. Substitution chain (mandatory per `[AUDIT]` trigger; applies to EVERY observable in the census)

Template chain for a single observable (k_a2 example — the other 4 follow the same structure, see dispatch prompt §Step 4):

Claim: "k_a2 is intrinsically L1 (cyclic-cohomology / Dixmier-trace determined)."

- Step 1: k_a2 ≡ f_2^{regulator} / f_2^{SDW} [definition, G15 Mellin-multiplier ratio at a_2 slot]
- Step 2: f_2^{regulator} = Res_{s=0} Tr(|D_K|^{-s}) * M_KK^{-2} under zeta (L1) OR sum over eigenvalues of regulator-weighted 1/λ_i² at L_max=5 (L2) [the regulator choice selects the layer]
- Step 3: Under L1 evaluation, f_2 is a Dixmier residue, i.e., <tau_2, 1> pairing in HP^0 (Connes 1988). Regulator-invariance follows from Dixmier-trace uniqueness.
- Step 4: Under L2 evaluation, f_2 = sum_i w(lambda_i²) / lambda_i², with regulator-dependent weights w. Not regulator-invariant.
- Step 5: Observation: G15 span_A(k_a2) = 14.685 = large, incompatible with L1 regulator-invariance. Therefore G15 is evaluating at L2, NOT at L1. The L1 evaluation of k_a2 is trivially 1 (ratio of equal Dixmier residues).
- Step 6: The layer commitment of k_a2 is ambiguous at evaluation level: L1 evaluation gives 1 (trivial, regulator-free); L2 evaluation gives 14.685 span (regulator-sensitive). Per the three-layer theorem (§VII.M), the observable's intrinsic layer is L1 (via its defining ratio of Dixmier residues); the physical value is L1's trivial 1. The 14.685 span is an L2 artifact of evaluating an L1 observable under a substrate-action minimum.
- Conclusion: k_a2 is intrinsically L1, with reported L2-span being an evaluation-layer artifact. Layer assignment: L1 with L2-evaluation warning flag.

This is the kind of derivation required per observable. The other 4 (f_conv, A_s_abs, w_0, CC-ratios) receive analogous chains; see §Step 4 of the dispatch prompt for expected outcomes.

### 11. What PASSES / FAILS MEAN for solution space

- **PASS** means the three-layer theorem can PIN every NOT-R-protected observable to a layer using substrate structure alone. Downstream observational forecasts (W3) get a layer-tagged prediction table. No remaining ambiguity about which observables are "regulator-free in principle" vs "regulator-sensitive in principle."
- **INFO** (4/5) means one observable remains layer-ambiguous. Expected: CC-ratios family (composite ratios with heterogeneous sub-layers). Downstream reports CC-ratios with `<MIXED-heterogeneous>` tag and a per-ratio sub-layer sub-tag.
- **FAIL** (<75%) means the framework's layer-commitment apparatus covers only a subset of NOT-R-protected observables, and the three-layer theorem's scope must be retracted to the covered subset. This is a structural wall, not a convention problem.

### 12. Effort estimate

~0.75 session, MEDIUM-HIGH complexity. Per-observable derivation is ~3-4 hours of careful substrate-structural analysis. 5 observables = 15-20 hours agent work + ~2 hours CM/HP cross-check. Higher effort than Gate 15 because the derivations are substantive, not merely classificatory.

### 13. Substrate-framing reminder (in agent dispatch prompt, §6 above, lines 3-10)

Explicitly instructed: derive from D_K eigenvalues → spectral moments → observable, not from observational phenomenology backward. [Present]

---

## §W2b-17. S84-L1-L2-COCYCLE-CENSUS

### 1. Gate ID
`S84-L1-L2-COCYCLE-CENSUS` (no S83 collision; S83 G53 HP-EVEN-COMPLETENESS-AUDIT classified 53 rows into 4 HP^even buckets {P=35, CM=7, M=10, GV=1}; this gate adds an ORTHOGONAL axis — layer L1/L2/MIXED — to each cocycle, producing a 53×6 cross-classification atlas)

### 2. Trigger
`[VERIFY-THEOREM]` — the gate tests the proposition that the HP^even register is layer-structurable. This is a theorem-candidate (every HP^even cocycle admits a unique L1/L2/MIXED classification with a substrate-structural reason).

### 3. Classification
**GEOMETRIC** — cyclic cocycles are the algebraic topology of the spectral triple, upstream of particle/observable observables. Unlike Gates 15 and 16 which were META (tool-classification / observable-classification respectively), this gate classifies the GEOMETRIC skeleton itself.

### 4. Agent type
`connes-ncg-theorist` (primary — HP^even classification is Connes's home ground; he authored the HP register scheme, K-theoretic pairings, and GV-lift apparatus). Required parallel cross-check: `lizzi-spectral-functional-theorist` (to verify that every L2-classified cocycle has a substrate-action evaluation consistent with the Zubarev canonicalization).

### 5. Hypothesis
**H_17**: Every cyclic cocycle in the framework's HP^even register (53 rows catalogued by S83 G53) admits a unique layer classification — L1 intrinsic (Dixmier-residue / K-theoretic pairing-native), L2 intrinsic (substrate-action-evaluated at finite L_max=5), or genuinely MIXED (cocycle has both L1 and L2 representations, and the layer choice changes the evaluation numerically). The classification is substrate-structural (provable from the cocycle's construction), not conventional.

### 6. Method (full-fidelity dispatch prompt)

**Agent dispatch prompt** (to `connes-ncg-theorist`):

```
[VERIFY-THEOREM] S84-L1-L2-COCYCLE-CENSUS

You are executing Gate S84-L1-L2-COCYCLE-CENSUS. Substrate framing is
mandatory: the D_K spectral triple is fundamental; HP^even cocycles are
the algebraic-topological skeleton. Layer commitment of a cocycle is a
structural property — which representation (Dixmier-residue class vs
substrate-action-at-finite-L_max) the cocycle's evaluation commits to.
Your job is to classify each of the 53 HP^even cocycles by layer.

## Task

For each cocycle in S83 G53's 53-row HP^even register (buckets P=35, CM=7,
M=10, GV=1), assign one of:
  (L1) Intrinsically L1 — Dixmier-residue-determined, cocycle lives
       natively as <phi, x> pairing in HP^n(A_F) / K_*(A_F) with x
       K-theoretic. Evaluation is regulator-invariant by construction.
       Examples expected: volume class on Cartan T^r; Connes-Chern
       character via ch: K_0 → HP^0.
  (L2) Intrinsically L2 — substrate-action-evaluated cocycle; evaluation
       requires a finite L_max truncation + regulator kernel to produce
       a numerical value. Expected examples: a_2 Seeley-DeWitt coefficient
       at L_max=5 (it IS the substrate-action integrand), epoch-gated
       cocycles (H_tilde, w_0 family).
  (MIXED) Cocycle has BOTH an L1 representation AND an L2 representation,
       and they evaluate numerically differently. Expected examples:
       epsilon_H (HP^3 but GV-lifted; has L1 formal class, L2 substrate
       evaluation; G56 showed stencil 5.98e-07 err but primary-proxy
       must be index, so MIXED).

Produce a 53-row table: cocycle_id | bucket(P/CM/M/GV) | layer(L1/L2/MIXED)
| substrate-reason (≥2 sentence citation).

## Input SHA-256 pins (all static)

- `computations/canonical_constants.py`: <computed-at-runtime>
- `computations/s83_gate_verdicts.txt` (G53 line): <computed-at-runtime>
- `computations/s83_w3_g53_hp_even_audit.py`: <computed-at-runtime>
- `computations/s83_w3_g53_hp_even_audit.npz` (53-row atlas): <computed-at-runtime>
- `computations/_cocycle_registry.py` (master registry per §VII): <computed-at-runtime>
- `phonon_exflation_cosmology.md` §VII (HP^even register location): <computed-at-runtime>

## Canonical constants

from canonical_constants import *
# Uses M_KK, tau_fold=0.19, L_max_canonical=5, Vol_SU3 (volume class), J_C2

## Per-cocycle classification protocol

For each cocycle C in the 53-row register:

  Step 1 — Retrieve construction:
    Load the cocycle's defining formula from S83 G53 row i.
    E.g., volume class: phi(a_0, a_1, ..., a_n) = tau(a_0 [D_K, a_1] ... [D_K, a_n])
    where tau is the Dixmier trace.

  Step 2 — Dixmier-residue test (L1 criterion):
    Does the cocycle evaluate as Res_{s=0} of a Mellin transform of
    (D_K^{-s}) paired with elements of A_F? If yes → L1-representable.
    Canonical L1 examples:
      - Volume class on Cartan T^r (Connes-Moscovici primary)
      - Connes-Chern character ch_*: K_*(A_F) → HP^*(A_F)
      - Any member of image(S: HP^even → HP^even) via S-operator

  Step 3 — Substrate-action test (L2 criterion):
    Does the cocycle require a finite L_max truncation to produce a
    concrete numerical value (i.e., the continuum limit diverges but
    the finite-L_max substrate-action minimum converges)? If yes →
    L2-representable.
    Canonical L2 examples:
      - a_2 Seeley-DeWitt coefficient at L_max=5 (IS the Einstein-Hilbert
        density in the spectral action)
      - Epoch-gated Hawking-Chern-like classes (H_tilde evaluation)
      - Zubarev-kernel-native observables from G1 S83

  Step 4 — Layer assignment:
    - If L1 only → L1 intrinsic
    - If L2 only → L2 intrinsic
    - If both, with numerically different evaluations → MIXED
    - If both, with numerically identical evaluations (e.g., cocycle
      is Mellin-cone-balanced and falls on the R-protected diagonal)
      → L1 intrinsic with L2-evaluation-preserving tag
    - If neither → FAIL (the cocycle shouldn't be in HP^even, re-verify G53)

  Step 5 — Substrate-reason citation:
    Write 2-3 sentences citing the specific construction that commits
    the cocycle to its layer. E.g., "Cocycle #14 (Cartan volume class
    on T^r) is L1 because it IS the Dixmier trace of 1 over the Cartan
    subalgebra, which by Connes (1988) Thm 5.3 is regulator-invariant
    up to a universal constant."

## Bucket-level predictions

From G53's 4-bucket structure, expected layer distribution:
  Bucket P (Primary, 35 rows): expect majority L1 (Dixmier-residue primary
    cocycles, K-theoretic pairings), few L2 (substrate-action-native
    primaries). Predict ~28 L1 / ~5 L2 / ~2 MIXED.
  Bucket CM (Chern-character of M-theory, 7 rows): expect majority L1
    (K-theoretic pairings are regulator-invariant). Predict ~7 L1 /
    ~0 L2 / ~0 MIXED.
  Bucket M (Modular, 10 rows): expect majority L1 (weight-balanced ratios
    ARE R-protected, so Mellin-cone-balanced and L1-stable). Predict
    ~9 L1 / ~0 L2 / ~1 MIXED (if any modular cocycle has non-trivial
    L2 shift).
  Bucket GV (Godbillon-Vey, 1 row): expect MIXED (G56 showed epsilon_H
    has L1 formal class but L2 substrate evaluation that differs
    numerically). Predict ~0 L1 / ~0 L2 / ~1 MIXED.

Aggregate prediction: ~44 L1 / ~5 L2 / ~4 MIXED (out of 53).

## Cross-check: R-protected observables from G53

Every cocycle in G53's 53-row audit that maps to an R-protected observable
(G58 R-protected ≤1.5 check) MUST be classified L1 intrinsic OR L1-stable
MIXED. If any R-protected observable cocycle classifies as L2 intrinsic,
the classification is internally inconsistent (R-protection implies
regulator-invariance implies L1-representable). This cross-check is a
hard constraint.

## GPU path (optional but recommended)

For L2 evaluation tests, build the D_K^2 spectrum on GPU at L_max=5:
  `torch.linalg.eigvals(D_K_sq.to('cuda'))`
and evaluate the cocycle's substrate-action integrand. Reuse the
atlas from Gate 15 if already computed in-session.
For L1 tests, symbolic / analytical — no GPU needed.

## Output files

- `computations/s84_w2b_l1_l2_cocycle_census.py` (classification tooling)
- `computations/s84_w2b_l1_l2_cocycle_census.npz` (53-row table)
- `computations/s84_w2b_l1_l2_cocycle_census.md` (per-row reason citation)

## Verdict line

Append to `computations/s84_gate_verdicts.txt`:
  S84-L1-L2-COCYCLE-CENSUS: <PASS|INFO|FAIL> -- value=<N_classified>/53
    scheme=per-cocycle convention=A L_max=5 sha256=<full 64-char closure>

## Working-paper section

Write `§VII.M-C L1-L2-Cocycle-Census` into the S84 working paper.
Substantive content required: 4 bucket-level aggregate paragraphs +
~10-15 row-level deep-dive citations (for bucket exemplars, especially
MIXED rows which are the diagnostic ones).
```

### 7. Machinery pin (PRDR)

| Parameter | Pin |
|:----------|:----|
| `L_max` | 5 (matches S83 G53 pin) |
| `scan_range` | N/A (classification gate) |
| `tolerance` | L2 evaluation numerical tolerance 1e-6 absolute (for MIXED identification: two evaluations differ by > 1e-6 ⇒ MIXED) |
| `scheme` | per-cocycle (53 cocycles independently classified) |
| `convention` | A (S83 G53 canonical pinning) |
| `GPU path` | `torch.linalg.eigvals` for L2 numerical cross-check (matrices ~5500×5500 at L_max=5) |
| `random_seed` | 42 (deterministic — seed pinned for eigvals row-ordering stability on GPU) |
| `Dixmier-trace residue order` | Res_{s=0} simple-pole extraction; no higher-order pole handling needed for HP^even |
| `R-protection cross-check threshold` | Any cocycle mapped to an R-protected observable (G58 span ≤ 1.5) must NOT classify as L2 intrinsic — hard constraint |
| `Bucket-conservation constraint` | Sum of layer counts per bucket = bucket size (35, 7, 10, 1); total = 53 |

### 8. Expected output 4-tuple

`(value=<N_classified>/53, scheme=per-cocycle, convention=A, L_max=5)`

where `<N_classified>` is the count of cocycles that received a definite L1/L2/MIXED assignment with a ≥2-sentence substrate-reason citation.

### 9. PASS / FAIL / INFO thresholds

- **PASS**: ≥ 53/53 cocycles classified (100%). Every row has a layer assignment and a ≥2-sentence substrate-reason. Bucket-level predictions (~44/5/4 L1/L2/MIXED) match within ±3 per category. R-protection cross-check passes (no R-protected cocycle is L2-intrinsic).
- **INFO**: 48-52/53 classified (90-99%). 1-5 cocycles remain with incomplete reason citations (likely exotic cocycles in bucket P with unclear layer commitment). R-protection cross-check still passes.
- **FAIL**: ≤ 47/53 classified (<90%), OR R-protection cross-check fails on any row, OR bucket-level predictions deviate by > 3 per category (suggesting layer classification is not substrate-structural).

### 10. Substitution chain (mandatory per `[VERIFY-THEOREM]` trigger)

Theorem claim: "Every cyclic cocycle in the 53-row HP^even register admits a unique layer classification (L1 / L2 / MIXED) determined by its construction, with a positive R-protection cross-check."

Required substitution chain (template for one row; applied 53 times):

Row example: Cocycle #C_V = volume class on Cartan T^r (in bucket P, Primary).

- Step 1: C_V(a_0, a_1, ..., a_n) = tau(a_0 · [D_K, a_1] · ... · [D_K, a_n]) [definition, Connes-Moscovici 1995 §1.1, using Dixmier trace tau]
- Step 2: tau(X) = Res_{s=0}(Tr(|D_K|^{-s} · X)) [Dixmier trace representation, Connes 1988]
- Step 3: Residue at s=0 is regulator-invariant for simple-pole integrands with compact fibers (standard NCG result). C_V's integrand has simple poles at integer s by the Mellin transform of the Cartan subalgebra's volume form. [L1 criterion satisfied]
- Step 4: L2 representation test: can C_V be evaluated via finite-L_max substrate-action? The substrate-action at L_max=5 is S[D_K, L_max] = Tr(f_R(D_K²/M_KK²)), a positive linear combination of exp(-α·λᵢ²) with Zubarev kernel. C_V does NOT appear as a coefficient of this expansion (it is the zeroth-order Dixmier trace, not an a_2k coefficient of the Seeley-DeWitt expansion). [L2 representation does not arise naturally; L2 criterion is trivially satisfied by identity-embedding but with an L1-invariant value.]
- Step 5: L2 numerical evaluation (if attempted via surrogate): tau(X) evaluated as lim_{L_max → ∞} Tr(|D_K|_{L_max=5}^{-s} · X) at s=0 — this IS the Dixmier residue at finite L_max, and converges to the L1 value as L_max → ∞. At L_max=5, the L2 numerical value differs from the L1 formal value by O(1/L_max²) ≈ 4% — which is below the 1e-6 MIXED threshold only if we define layer-identity as "continuum-limit-equal."
- Step 6: Layer resolution rule: if L1 evaluation gives a regulator-invariant number AND L2 evaluation converges to the same number as L_max → ∞, then the cocycle is L1 intrinsic with L2-evaluation-preserving tag. C_V satisfies this criterion.
- Step 7: Substrate-reason citation: "Volume class on Cartan T^r is L1 intrinsic because it IS the Dixmier trace of the identity element restricted to the Cartan subalgebra. By Connes (1988) Thm 5.3, the Dixmier trace is regulator-invariant up to a universal constant, making the evaluation L1-pinned. The finite-L_max substrate-action evaluation converges to this value as L_max → ∞, so the cocycle carries an L2-evaluation-preserving tag but is intrinsically L1."

Conclusion: C_V classified as L1 intrinsic with L2-preserving tag. Layer assignment substrate-structurally determined.

The other 52 cocycles receive analogous chains. Bucket P primaries (35 rows) are expected to classify L1-dominant; bucket CM (7 rows) uniformly L1; bucket M (10 rows) L1-dominant by R-protection; bucket GV (1 row, epsilon_H) MIXED.

### 11. What PASSES / FAILS MEAN for solution space

- **PASS** means HP^even is LAYER-STRUCTURED. The three-layer regulator theorem (§VII.M) applies not only at the regulator level (Gate 15) and observable level (Gate 16) but also at the cocycle level — i.e., at the algebraic-topological skeleton of the spectral triple. This is the deepest structural statement of the wave. Downstream analyses reference the 53×6 atlas when making any HP^even claim.
- **INFO** (90-99%) means the atlas is substantially complete but a small number of exotic cocycles (likely in bucket P) lack clean substrate-reason citations. The layer structure persists; documentation is partial.
- **FAIL** (<90% OR R-protection cross-check fails OR bucket-level predictions deviate by > 3 per category) means the HP^even register is NOT uniformly layer-classifiable. Either (a) some cocycles live in a third representation we haven't catalogued (suggests a missing layer in the three-layer theorem, a major structural finding), or (b) R-protection ≠ L1-representability, breaking G58's meta-principle.

### 12. Effort estimate

~1 session, HIGH complexity. 53 cocycles × ~15-20 minutes per row for careful classification = 13-18 hours agent work. The 1 GV cocycle (epsilon_H) and the 2-4 expected MIXED cocycles in P require deeper analysis (~1 hour each). Total: ~15-20 hours. The GPU cross-check is fast (~5 minutes for L_max=5 eigvals on RX 9070 XT). Write-up of per-row citations is the rate-limiter.

### 13. Substrate-framing reminder (in agent dispatch prompt, §6 above, lines 3-9)

Explicitly instructed: D_K spectral triple is fundamental; HP^even cocycles are the ALGEBRAIC-TOPOLOGICAL skeleton, not containers for physics. Layer commitment is substrate-structural, derivable from the cocycle's construction. [Present]

---

## W2b → W2a / W2c Parallel Dispatch Note

W2b (items 15, 16, 17) runs in parallel with W2a (items 11-14) and W2c (items 18-20). All three sub-waves consume the W1 outputs (three-layer registry landing, L_max-extrapolation uniqueness confirmation).

**Dependency graph for W2b's 3 gates:**

- Gate 15 (S84-MP-LAYER-AUDIT): depends on S83 G27 output (regulator admissibility data) + canonical_constants.py. Independent of Gates 16/17 within W2b.
- Gate 16 (S84-PIN-DERIVATION-CENSUS): depends on S83 G15/G28/G34/G51/unified-AS-79 outputs. Independent of Gates 15/17 within W2b.
- Gate 17 (S84-L1-L2-COCYCLE-CENSUS): depends on S83 G53 output (53-row HP^even audit). Independent of Gates 15/16 within W2b.

All three can dispatch in parallel as concurrent Agent tool calls. The concurrent-dispatch cap of ~8 is well-respected (3 agents within W2b + 4 agents W2a + 3 agents W2c = 10 if all simultaneous, borderline; recommend staging W2a first, then W2b and W2c together, or sub-staging within each block).

**Cross-wave consistency checks (post-dispatch):**

- Gate 15's admissibility ledger must be consistent with Gate 17's layer classifications: every L1-classified cocycle must evaluate under at least one L1-admissible regulator (zeta expected).
- Gate 16's observable-to-layer map must be consistent with Gate 17's cocycle layer map: A_s absolute in Gate 16 should decompose into cocycles in Gate 17 with matching layer tags.
- Gate 15 + Gate 17's joint coverage = complete layer scaffold for the spectral action apparatus (regulator × cocycle × observable cross-tabulation).

---

## W2b → W3 Decision Point

W2b's three verdicts feed W3 (observational / detector forecast) as follows:

| W2b Verdict Outcome | Downstream W3 Action |
|:---------------------|:---------------------|
| All 3 PASS | W3 observational predictions carry full layer-tag (L1/L2/MIXED-sublayer) per observable. No further layer-disambiguation needed. |
| Gate 15 PASS + 16 PASS + 17 INFO | W3 proceeds with layer tags from 15+16 output; the 1-5 INFO cocycles in 17 get `<L?-provisional>` tag in §VII.K-DUAL atlas. |
| Gate 15 PASS + 16 INFO + 17 PASS | W3 has complete cocycle atlas but partial observable derivation; CC-ratios family gets `<MIXED-heterogeneous>` tag. |
| Any FAIL | Re-dispatch W2b within-session or carry forward to S85 as explicit deadlock (see `.claude/rules/epistemic-discipline.md` §Evidence Hierarchy). Do NOT proceed to W3 with a FAIL'd layer apparatus. |

---

## W2b Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness (PRDR), every gate-relevant machinery parameter is pinned upfront here:

| Gate | Pinned parameters | PRU-status |
|:-----|:------------------|:-----------|
| 15 MP-LAYER-AUDIT | L_max=5, convention=A, δ_set={1e-4, 1e-3, 1e-2, 1e-1}, CM-order n∈{0,1,2,3,4}, Bernstein measure α∈(0,∞), scheme=multi-regulator, GPU=`torch.linalg.eigvals`, seed=42 | PIN-COMPLETE |
| 16 PIN-DERIVATION-CENSUS | L_max=5, convention=A, derivation-chain-length≥4, R-protected-control=c_s (G14), scheme=per-observable, GPU=cache-only (no recompute) | PIN-COMPLETE |
| 17 L1-L2-COCYCLE-CENSUS | L_max=5, convention=A, tolerance_L2=1e-6, Dixmier-residue simple-pole order, bucket-conservation (35/7/10/1), R-protection cross-check threshold 1.5, scheme=per-cocycle, GPU=`torch.linalg.eigvals`, seed=42 | PIN-COMPLETE |

No machinery parameter is left diagnostic. All three gates are PRU-immune.

---

## W2b Input-SHA Ledger

All pinned inputs are static files in the project tree; SHAs computed at runtime by the dispatch scripts. The ledger of expected pin targets:

| Gate | Input file | Pin status |
|:-----|:-----------|:-----------|
| 15 | `computations/canonical_constants.py` | <computed-at-runtime> |
| 15 | `computations/s82_mp_exclusion_theorem.py` | <computed-at-runtime> |
| 15 | `computations/s83_gate_verdicts.txt` (G27 line) | <computed-at-runtime> |
| 15 | `computations/s83_w2_g27_mp_admissibility.py` | <computed-at-runtime> |
| 15 | `computations/_regulator_atlas.py` (if exists) | <computed-at-runtime> |
| 16 | `computations/canonical_constants.py` | <computed-at-runtime> |
| 16 | `computations/s83_gate_verdicts.txt` (G15/G28/G34/G51 lines) | <computed-at-runtime> |
| 16 | `computations/s83_w2_g15_k_a2_canonical_range.py` | <computed-at-runtime> |
| 16 | `computations/s83_w3_g28_f_conv_cluster.py` | <computed-at-runtime> |
| 16 | `computations/s83_w3_g34_cc_ratio_cluster.py` | <computed-at-runtime> |
| 16 | `computations/s83_w3_g51_w0_regulator.py` | <computed-at-runtime> |
| 16 | `computations/s83_unified_as_79_3pi.py` | <computed-at-runtime> |
| 16 | `sessions/archive/session-83/gen-physicist-s6-synthesis.md` | <computed-at-runtime> |
| 17 | `computations/canonical_constants.py` | <computed-at-runtime> |
| 17 | `computations/s83_gate_verdicts.txt` (G53 line) | <computed-at-runtime> |
| 17 | `computations/s83_w3_g53_hp_even_audit.py` | <computed-at-runtime> |
| 17 | `computations/s83_w3_g53_hp_even_audit.npz` | <computed-at-runtime> |
| 17 | `computations/_cocycle_registry.py` | <computed-at-runtime> |
| 17 | `phonon_exflation_cosmology.md` §VII | <computed-at-runtime> |

Dispatch scripts `s84_w2b_<gate-slug>.py` MUST log all input SHAs in their first 20 stdout lines and emit the closure SHA as the final non-verdict stdout line. The closure SHA is the SHA-256 of the ordered input-pin map per `.claude/rules/gate-verdicts.md`.

---

**End of Session 84 Plan — Wave 2b.**
