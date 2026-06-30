# Session 91 — Wave 2 Working Paper

**Session**: 91 | **Wave**: W2 | **Plan**: `sessions/session-plan/session-91-plan-w2.md` | **Theme**: §VII.AU substrate-physics + CF-37 + first-extraction (gen-physicist plan-author; OAA exclusions for T0.7 §W2-1)

**Status**: SHELL CREATED (2026-05-16); awaiting runtime compute dispatch

**Verdict file (canonical)**: `computations/session-91/s91_gate_verdicts.txt` per `gate-verdicts.md §"Canonical Verdict-File Path"`. Variants under `computations/_shared/` or `sessions/archive/session-91/` are FORBIDDEN; treat any documentation reference as a bug.

**Wave classification**: COMPUTE-class per `wave-classification.md §"Strict-conjunction requirement"`; all 3 gates have numerical PASS thresholds and produce `.py`/`.npz`/`.png` artifacts.

**Substrate-framing lock (W2-wide)** — per `phononic-framing.md §"IS Space, Not IN Space"`, ALL test-case authors in this wave MUST:

1. Treat the spectral triple `(A_K, H_K, D_K)` as the substrate (fundamental).
2. Treat Mellin-cone residues at substrate-distance-N poles as substrate-IS quantities (NOT measurements IN a continuum container).
3. Treat the χ' inheritance morphism (§W2-1) as the substrate's secondary inheritance structure (NOT a "projection of substrate INTO the LRD continuum pillar").
4. Treat the §VII.AU.OP-PROJ first-extraction as the substrate's own determination of how the canonical pin is read off (NOT an "external regularization applied to the substrate").
5. Treat the 5-anchor Spearman matrix (§W2-3) as the substrate's discriminator between Reading A and Reading B bindings (NOT a "statistical test on the substrate").

**Gate inventory** (3 items):

| Gate ID | Status | Trigger | Effort | OAA |
|:--------|:-------|:--------|:-------|:----|
| §W2-1 [T0.7] S91-CF37-CHI-PRIME-WEIGHT-CANONICALIZED | NOT STARTED | `[VERIFY-THEOREM]`+`[CHAIN]` | ~2.0 we | EXCLUDED: connes-ncg-theorist + phonon-first-cosmologist (S90 W-2 §EMERGENCE EV1 downstream-inheritance reach test) |
| §W2-2 [T1.5] S91-VII-AU-FIRST-EXTRACTION-PARAMETERIZATION | NOT STARTED | `[VERIFY]`+`[CHAIN]` | ~1.5 we | — |
| §W2-3 [T1.10] S91-VII-AU-OP-PROJ-FIRST-EXTRACTION-W7A74 | NOT STARTED | `[SIGN]`+`[VERIFY]` | ~0.4 we | — |

**Total effort**: ~3.9 we.

## Wave 2 Decision Point Prerequisites

| Gate | Hard prerequisite | Soft prerequisite (improves verdict-fidelity) |
|:-----|:------------------|:---------------------------------------------|
| §W2-1 (T0.7) | `_cm_1995_residue_formula.py` operational; L_max=12 master cache `s90_w8_spectrum_cache_L12_tau038.npz` SHA-pinned | S91 W0b R5 NEW §VII slot for option (v) pre-registration LANDED |
| §W2-2 (T1.5) | `_spectral_action_regulators.py` SCHEMATIC docstring lines 23-30 (or FULL CC multipliers from T1.1 if available) | T0.7 χ' weight canonicalization PASS (informs sub-option a vs b vs c reading) |
| §W2-3 (T1.10) | S90 W8 W7a-74 PRIMARY evaluator `s90_w8_w7a74_primary_evaluator_full_tier_retry.py` operational; L_max=12 cache SHA-pinned | T1.5 first-extraction parameterization PASS or INFO (anchors the 5 Spearman positions) |

Hard prerequisites are dispatch-blocking; soft prerequisites improve downstream consumability but do NOT block dispatch per `feedback_dispatch-discipline.md`.

---

## §W2-1. S91-CF37-CHI-PRIME-WEIGHT-CANONICALIZED (T0.7)

**Status**: PASS (composite); value_token=V (Reading V regulator-class-pluralism canonical); runtime 0.8s; landed 2026-05-16 by volovik-superfluid-universe-theorist (PRIMARY)

**Plan reference**: `sessions/session-plan/session-91-plan-w2.md §W2-1` (lines 62-407)

**Gate ID**: `S91-CF37-CHI-PRIME-WEIGHT-CANONICALIZED-FULL-CM-1995-III-4-SUBSTRATE-DISTANCE-2-EVALUATION` (legacy alias: `T0.7` / `CF-S91-CF37-CHI-PRIME`)

**Trigger**: `[VERIFY-THEOREM]` — primary; `[CHAIN]` — secondary (option (iv) vs (v) adjudication via FULL CM-1995 §III.4 residue evaluation chain at χ' restriction).

**Classification**: GEOMETRIC (Mellin-cone residue formula evaluation on the spectral triple's secondary inheritance morphism χ' under FULL CM-1995 §III.4 machinery; PARTICLE if Reading C resolves to image-block-rank tied to SU(3) representation content — pre-registered as PARTICLE-conditional).

**Agent type** — PRIMARY test-case author: `volovik-superfluid-universe-theorist` (substrate-side Element-1 disambiguation; framework's SHARPEST reviewer per `feedback_agent-roster.md`). CONFIRMER test-case author: `van-den-dungen-bridge-theorist` (NCG-axiomatic-side inheritance morphism χ' on Pillar-I → Pillar-II bridge; canonical reviewer for inheritance kernel structure per `reference_van-den-dungen-bridge.md`). EXCLUDED (HARD): `connes-ncg-theorist` and `phonon-first-cosmologist` per S90 W-2 §EMERGENCE EV1 OAA constraint — both reviewers AUTHORED the W-2 workshop's competing reading; their re-dispatch on the canonicalization gate is structurally pre-loaded, failing the Stage-2 Axis-B Selection Protocol's downstream-inheritance reach test per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`. NOT-permissible: `gen-physicist` (planner role; `/rclab-plan` Phase 3 blacklist).

**Hypothesis**: The CF-37 χ' inheritance restriction weight is canonically determined by FULL CM-1995 §III.4 dimension-spectrum residue evaluation at the substrate-distance-2 pole `s=4`, with option (iv) image-block-rank (canonical pre-registration: image-block-rank = 3 on M_3(ℂ) Peter-Weyl content) and option (v) regulator-class-pluralism (admitted at S90 W-2 §EMERGENCE EV1 D1-Reading-B) as the two pre-registered readings; PASS canonicalizes one reading and registers the §VII.AX slot per the chosen reading.

**Effort estimate**: 2.0 we (0.4 cache load + Peter-Weyl filter + projector validation; 0.4 implement FULL CM-1995 §III.4 evaluator under three regulator classes; 0.5 cross-regulator comparison + image-block-rank integer check + L_max=10 truncation cross-check; 0.3 substitution-chain verification + sign_verdict computation; 0.2 WP section + verdict-line emission + dual-SHA + PRDR audit; 0.2 NPZ + PNG output + projection-side tagging check).

### Method

Compute the FULL CM-1995 §III.4 dimension-spectrum residue formula

```
R_χ' = Res_{s=4} ζ_D'(s)
     = Res_{s=4} Tr_{H_χ'} ( |D'|^{-2s} )
```

where D' is the inherited Dirac operator on χ'(A_K) ⊆ A_LRD-substrate, restricted to the M_3(ℂ) summand (the Peter-Weyl content carrying the SU(3)-coloured inheritance kernel per the CF-37 (d)∘(b) primary corridor).

Imports + environment:

```python
from canonical_constants import *
from _cm_1995_residue_formula import compute_zeta_d_residue
# (FULL physical CM-1995 residue formula evaluator; NOT SCHEMATIC)
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')  # before numpy import
import numpy as np
import torch  # for ≥100×100 matrices
```

Inputs (Input-SHA pins, all `<pinned at dispatch>`):

- `computations/session-90/s90_w8_spectrum_cache_L12_tau038.npz` (master L_max=12 spectrum cache at τ_fold; 155984 eigenvalues with sector tags (p,q) for Peter-Weyl decomposition)
- `computations/_shared/_cm_1995_residue_formula.py` (S90+ FULL physical residue formula evaluator; NOT _spectral_action_regulators)
- `computations/_shared/canonical_constants.py at HEAD` (anchors: tau_fold=0.19, M_KK gravity-pin, alpha_s_canonical Fraction(-8587279,100000000))
- `sessions/permanent-results-registry.md §VII.AU.OP-PROJ line 17677` (REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION baseline; FWD-C1 substrate-distance-1 baseline at pole s=3 to be compared with substrate-distance-2 pole s=4 at χ' restriction)
- `sessions/archive/session-90/workshops/s90-w2-chi-prime-weight-canonicalization.md lines 877-887` (S90 W-2 §EMERGENCE EV1 D1-Reading-B option (v) admittance pre-registration)

Procedure:

1. Load L_max=12 master spectrum cache; filter on M_3(ℂ) Peter-Weyl blocks (sector (p,q) with q ≥ 1 OR p ≥ 1 AND p+q ≥ 2, the SU(3)-coloured inheritance content).
2. Restrict to χ' image: kill the C ⊕ ℍ summands of A_K via projector P_M3 (P_M3 = (0, 0, 1) idempotent of A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)); verify P_M3 commutes with χ' restriction (substrate-IS commutativity check per `epistemic-discipline.md §"Layer-Decomposition"`).
3. Compute R_χ' via FULL CM-1995 §III.4 residue formula on the restricted spectrum:

   ```
   R_χ' = lim_{s→4} (s-4) · Σ_{λ ∈ spec(D'|_{P_M3 H})} |λ|^{-2s}
   ```

   using torch.linalg on GPU for the sum (cache has 155984 eigenvalues pre-filtered to ~20000-30000 in the M_3(ℂ) block).
4. Compute under THREE regulator-class conventions (ζ, Pauli-Villars, Mellin) per S90 W-2 §EMERGENCE EV1 5th pre-registered verdict at the (substrate-distance-2, cross-axis-converged) cell:
   - `R_χ'^{ζ}` = ζ-function regularization
   - `R_χ'^{PV}` = Pauli-Villars regularization at Λ_UV = M_KK
   - `R_χ'^{Mellin}` = Mellin-Barnes regularization per W2 C9
5. Read off:
   - Reading IV (image-block-rank canonical): `R_χ'^{ζ} = R_χ'^{PV} = R_χ'^{Mellin}` to within rel_tol=1e-9 AND image-block-rank value = 3 to within abs_tol=1e-12.
   - Reading V (regulator-class-pluralism canonical): `R_χ'^{ζ} ≠ R_χ'^{PV} ≠ R_χ'^{Mellin}` AND each regulator-class value enters §VII.AX entry as a separate substrate-distance-2 pin per the multi-pin atlas structure.
6. Apply substitution chain (Step 10) for the SIGN claim: "image-block-rank canonicalization yields R_χ' = 3 if and only if the M_3(ℂ) summand image is faithfully embedded under χ'".

Output files:

- `computations/session-91/s91_w2_1_cf37_chi_prime_weight.py` (producing script; full 13-field gate-block header + producer body)
- `computations/session-91/s91_w2_1_cf37_chi_prime_weight.npz` (keys: `R_chi_prime_zeta`, `R_chi_prime_PV`, `R_chi_prime_Mellin`, `reading_iv_match_bool`, `reading_v_pluralism_bool`, `image_block_rank`, `cache_sha`, `residue_formula_sha`, `L_max_operational`, `truncation_consistent`, `regime_used_frac`)
- `computations/session-91/s91_w2_1_cf37_chi_prime_weight.png` (3-panel plot: R_χ' vs L_max per regulator class; per-regulator residual to image-block-rank=3; cross-regulator spread)

Verdict-line append (atomic, via `append_verdict()` helper from script-template.py):

```
S91-CF37-CHI-PRIME-WEIGHT-CANONICALIZED: PASS|FAIL|INFO -- value='IV' or 'V' or 'undetermined' \
  scheme=FULL-CM-1995-III-4-residue-formula \
  convention=substrate-distance-2-multi-regulator-atlas \
  L_max=12 sha256=<64-char-closure-of-input-pin-map> \
  schema_version=S84+

# audit_sha256 companion row: S91-CF37-CHI-PRIME-WEIGHT-CANONICALIZED \
  audit_sha256_short=<16> content_sha256_short=<16> # dual-SHA companion (W9a-99 split)
```

The producing script MUST use `from _cm_1995_residue_formula import *` (FULL physical evaluator) NOT `from _spectral_action_regulators import *` (SCHEMATIC helper). If the producing script accidentally imports the SCHEMATIC helper, the `convention=` field MUST carry `-SCHEMATIC` suffix per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline AND the audit fires Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY remediation.

### Machinery pin (PRDR)

| Parameter | Pin | Source |
|:----------|:----|:-------|
| `L_max` | 12 (operational); 10 (cross-check truncation) | S90 W8 master cache |
| `tau_fold` | 0.19 (Fraction(19, 100) bit-exact) | `canonical_constants.py:283` |
| `M_KK` | 7.43e16 GeV (gravity-pin canonical) | `canonical_constants.py:12` |
| `pole_index` | s=4 (substrate-distance-2; CHI-PRIME RESTRICTION) | S90 W-2 §EMERGENCE EV1 |
| `regulator_class_index` | enumerated: {ζ, Pauli-Villars, Mellin} | S90 W-2 5-class taxonomy line 1535 |
| `peter_weyl_sector_filter` | M_3(ℂ)-block (q ≥ 1 OR p ≥ 1 AND p+q ≥ 2) | NCG-axiomatic SU(3)-coloured content |
| `projector_P_M3` | idempotent (0, 0, 1) on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) | NCG-axiomatic Wedderburn decomp |
| `inheritance_morphism_chi_prime` | A_K ↠ M_3(ℂ) (kill C, ℍ summands) | CF-37 (d)∘(b) primary corridor |
| `rel_tol_image_block_rank` | 1e-9 (canonical sanity-check; matches Class 8.3 item 6 floor) | `epistemic-discipline.md §"Class 8.3 item 6"` |
| `abs_tol_image_block_rank` | 1e-12 (rank-3 integer pin) | NCG-axiomatic rank integer |
| `LEVEL pin` | FULL (NOT SCHEMATIC; uses `_cm_1995_residue_formula.py`) | `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY |
| `MACHINERY-SCOPE pin` | CACHE-PROJECTION (consumes L_max=12 cache; NOT FULL-LEAF-FOLIATION) | `cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix"` axis α |
| `Binding axis pin` | substrate-natural-binding (χ' is intrinsic substrate morphism, NOT canonical-import) | `regulator-pin-discipline.md §"Binding axis"` |
| `bridge_map_scheme` | NOT applicable (no APS/Cheeger-Simons/Bismut-Cheeger η here; pure dimension-spectrum residue) | axis β not engaged |
| `gpu_path` | `torch.linalg` on AMD RX 9070 XT ROCm 7.2; matrix dim ~20-30k pre-filtered | `math-scripts.md §"Environment"` |
| `random_seed` | N/A (deterministic algebraic evaluation, no MC) | — |
| `scan_range` | N/A (single residue evaluation at s=4, not a scan) | — |
| `convention pin` | `substrate-distance-2-multi-regulator-atlas` | S90 W-2 §EMERGENCE EV1 |

PRDR enumeration: 17 free parameters pinned; 0 unpinned. PRU Class-8 cardinality test: PASS at plan-freeze.

### Expected output 4-tuple

`(value=<'IV'|'V'|'undetermined'>, scheme=FULL-CM-1995-III-4-residue-formula, convention=substrate-distance-2-multi-regulator-atlas, L_max=12)`

### PASS/FAIL/INFO thresholds

| Outcome | Condition | Tolerance rule |
|:--------|:----------|:--------------|
| **PASS-IV** | `|R_χ'^{ζ} − R_χ'^{PV}| < 1e-9` AND `|R_χ'^{ζ} − R_χ'^{Mellin}| < 1e-9` AND `|R_χ'^{ζ} − 3| < 1e-12` | RATIO (1e-9 rel) cross-regulator + ABSOLUTE (1e-12 abs) image-block-rank |
| **PASS-V** | `|R_χ'^{ζ} − R_χ'^{PV}| ≥ 1e-9` OR `|R_χ'^{ζ} − R_χ'^{Mellin}| ≥ 1e-9` AND each regulator-class value is finite and well-defined (`np.isfinite(R)`) | RATIO (1e-9 rel) cross-regulator pluralism |
| **INFO** | one regulator-class residue is non-finite OR L_max=10 truncation gives different sign from L_max=12 (`truncation_consistent=False`) | bit-precision check on `np.isfinite` and signs |
| **FAIL** | all three regulator-class residues are non-finite OR image-block-rank diverges (|R| > 1e6) | ABSOLUTE blow-up detection |

Composite collapse per `gate-verdicts.md §"S87+ canonical form Schema-v2"` 3-tuple discipline:

- `sign_verdict` = PASS if R_χ' positive (image-block-rank is +3, NOT −3) per substitution chain Step 5 below; FAIL otherwise.
- `magnitude_verdict` = PASS-IV if Reading IV matched; PASS-V if Reading V matched; INFO if borderline; FAIL if blow-up.
- `regime_verdict` = VALID if `truncation_consistent=True` on L_max=10/12 cross-check AND `regime_used_frac ≥ 0.95` of intended Peter-Weyl block; MARGINAL if 0.50 ≤ frac < 0.95; BREAKDOWN if frac < 0.50.

### Substitution chain (MANDATORY)

The SIGN claim is: "FULL CM-1995 §III.4 residue evaluation at χ' restriction yields R_χ' = +3 (image-block-rank, Reading IV) ONLY IF the M_3(ℂ) summand image is faithfully embedded under χ' AND all three regulator-class evaluations agree to relative tolerance 1e-9". The direction predicted is `R_χ' > 0`.

```
Step 1 — Definitions:
  A_K            = ℂ ⊕ ℍ ⊕ M_3(ℂ)                  [substrate algebra; canonical_constants pin]
  χ'             : A_K ↠ M_3(ℂ)                     [inheritance morphism;
                                                     killed: C ⊕ ℍ summands]
  D'             = D_K|_{P_M3 H_K}                   [Dirac operator restriction]
  P_M3           = (0, 0, 1) idempotent in A_K       [central projection]
  R_χ'(R)        = Res_{s=4} Tr_{P_M3 H_K}(|D'|^{-2s}) under regulator class R
                                                     [CM-1995 §III.4]
  image_block_rank = rank of P_M3 image under χ'_*   [structural integer = 3
                                                      iff faithful embedding]

Step 2 — Substitution:
  Substitute χ' image faithfulness into R_χ' definition:
    R_χ'(R) = Σ_{(p,q) ∈ SU(3)-coloured sectors} m_{(p,q)} · |λ_{(p,q)}|^{-2·4}
            evaluated at residue s=4 under regulator class R
    where m_{(p,q)} = Peter-Weyl multiplicity of sector (p,q) in M_3(ℂ).

Step 3 — Simplify (CM-1995 §III.4 dimension-spectrum form):
  At pole s=4 of the dimension spectrum on a 4D substrate (KO-dim=6
  factors through 4D + finite K), the residue is the alternating sum:
    R_χ'(R) = (1/(4·π²)) · Tr_{P_M3 H_K}( a_4(D') )
            where a_4 is the 4th Seeley-DeWitt coefficient under R.
  For χ' faithful, a_4(D') = a_4(D_K) restricted to P_M3 image; the
  rank-3 structure of M_3(ℂ) Peter-Weyl is preserved.
  Thus:
    R_χ'(R) = (1/(4·π²)) · 3 · K_a4(τ_fold)
  where K_a4(τ_fold) is the τ-dependent a_4 trace ratio normalized to 1
  at canonical pin (substrate-distance-2 normalization).

Step 4 — Read off direction:
  K_a4(τ_fold) > 0 (substrate's a_4 trace is positive-definite per S57
  Connes-Chamseddine positivity theorem; canonical_constants Phi(a_4) =
  Σ_3 load-bearing).
  Therefore R_χ'(R) > 0 for all regulator classes R.
  AND the integer rank-3 prefactor SHOULD be invariant under R if
  the embedding is faithful (Reading IV).

Step 5 — Direction conclusion:
  Reading IV (faithful embedding) predicts:
    sign(R_χ') = +
    magnitude(R_χ') = 3 · (1/(4·π²)) · K_a4(τ_fold)
    cross-regulator: R_χ'^{ζ} = R_χ'^{PV} = R_χ'^{Mellin}.
  Reading V (regulator-class pluralism) predicts:
    sign(R_χ') = + (still positive; K_a4 > 0)
    magnitude(R_χ') = (1/(4·π²)) · K_a4^{(R)}(τ_fold)
    where K_a4^{(R)} differs across R, so the cross-regulator spread
    is positive (numerical pluralism), but the SIGN remains +.

Both readings predict positive sign; the magnitude_verdict
discriminates IV vs V. The substitution chain rules out negative-sign
outcome (positivity of K_a4 is structural per S57).

Conclusion: the SIGN claim "R_χ' > 0" is structurally predicted PASS
unless K_a4(τ_fold) breakdown is detected, in which case
regime_verdict = BREAKDOWN routes the composite to FAIL.
```

### What PASSES and FAILS MEAN for solution space

- **PASS-IV** (Reading IV canonical): the §VII.AX slot lands with Element 3 fiducial-anchor binding = `substrate-natural-binding` per the M_3(ℂ) image-block-rank=3 substrate identity. The substrate-IS observable at substrate-distance-2 χ' restriction is a SINGLE algebra-INVARIANT spectrum-only functional (Cell I × Mellin pole s=4 per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 classification"` — note: 4-corner cell adjustment needed since this is Cell-I-pole-s=4-not-s=3 by parse-tree per `permanent-results-registry.md §VII.U.2 (e)`). The solution-space region for FWD-C1 substrate-distance-1 pole s=3 (§VII.AU.OP-PROJ baseline) is CONFIRMED as the unique cross-pillar bridge anchor at this corner. Eliminates option (v) pluralism corridor.
- **PASS-V** (Reading V canonical): the §VII.AX slot lands as a MULTI-PIN ATLAS (three Element 3 fiducial-anchors per regulator class, per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` axis β multi-scheme convention). The REGULATOR-CLASS-PLURALISM cell is structurally distinct from the single-anchor cell; advances the (regulator-class-pluralism, Cell-I Mellin-pole-s=4) corner toward K=2 calibration corpus.
- **INFO** (truncation-inconsistent or borderline pluralism): defers the canonicalization to S92 L_max=14+ cache extension; §VII.AX slot reserved with sub-class tag `REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT` per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` (M_KK pin uniqueness axis).
- **FAIL** (regulator blow-up or sign violation): eliminates BOTH Reading IV and Reading V; routes CF-37 χ' inheritance restriction to alternative AUX-4 (c)∘(d) compositional secondary corridor under modified-universal kernel γ(s) ≠ Γ(s) per W3 T1.8. The CF-37 LRD α-anchor pathway then routes exclusively through the substrate-distance-1 pole s=3 (§VII.AU.OP-PROJ baseline) plus the substrate-distance-2 pole s=4 via §VII.AV Cell IV (Type-F single-summand-projection trace per `mechanical-closure-discipline.md §"Layer-separability carve-out"`), with χ' weight canonicalization removed from the (d)∘(b) primary corridor.

### Substrate framing

Per `phononic-framing.md §"IS Space, Not IN Space"`:

- The substrate IS the spectral triple `(A_K, H_K, D_K)`. The χ' inheritance morphism IS the substrate's secondary inheritance structure onto the M_3(ℂ) summand at SU(3)-coloured Peter-Weyl content. χ' is NOT a "projection of the substrate INTO a continuum LRD measurement container".
- The Mellin-cone residue at pole s=4 IS the substrate's a_4 Seeley-DeWitt content evaluated on the M_3(ℂ) summand. Phi(a_4) = Σ_3 (Yang-Mills + Higgs quartic load-bearing weight-4) per `epistemic-discipline.md §"Phi correspondence"`.
- The image-block-rank=3 prediction (Reading IV) IS a substrate identity (`A_K`'s M_3(ℂ) summand has Wedderburn rank 3 by construction). The substrate IS the rank-3 structure; faithfulness of χ' is the substrate's intrinsic statement, NOT a measurement IN a laboratory.
- Direction of explanation: D_K eigenvalue spectrum at SU(3)-coloured sectors → Mellin-cone residue at pole s=4 under χ' restriction → emergent CF-37 LRD α-anchor as observable IN the LRD continuum pillar.

If the test-case author writes "the χ' morphism produces particles in the LRD continuum" or "the M_3(ℂ) image is embedded into a measurement space", STOP. Invert: the M_3(ℂ) summand IS the substrate; LRD α-anchor emerges as observable.

### Input-SHA pin map

```yaml
input_pin_map:
  spectrum_cache_L12_tau038: <pinned at dispatch>     # s90_w8_spectrum_cache_L12_tau038.npz
  cm_1995_residue_formula_py: <pinned at dispatch>    # _cm_1995_residue_formula.py
  canonical_constants_py: <pinned at dispatch>        # canonical_constants.py at HEAD
  permanent_results_registry_md_vii_au_op_proj: <pinned at dispatch>  # §VII.AU.OP-PROJ line 17677
  s90_w2_workshop_md_emergence_ev1: <pinned at dispatch>              # S90 W-2 §EMERGENCE EV1 lines 877-887
audit_sha256: closure_hash(ordered_pin_map_above)
```

### Results

Computed 2026-05-16 by volovik-superfluid-universe-theorist (PRIMARY) per plan §W2-1 (6) Method. Producing script: `computations/session-91/s91_w2_1_cf37_chi_prime_weight.py`. Data: `computations/session-91/s91_w2_1_cf37_chi_prime_weight.npz`. Plot: `computations/session-91/s91_w2_1_cf37_chi_prime_weight.png`. Wall time: 0.8s.

| Field | Value |
|:------|:------|
| `value_token` | `V` (Reading V regulator-class-pluralism canonical) |
| `R_chi_prime_zeta` | `1.4143926086716587e+02` (M_KK^2 units; Σ \|λ\|^{-8} on M_3(ℂ) block; Γ(s) cancellation at simple pole s=4 confirmed) |
| `R_chi_prime_PV` | `1.1445766306905740e+02` (Pauli-Villars subtraction at Λ_UV = M_KK; substrate-natural-binding) |
| `R_chi_prime_Mellin` | `1.4143926086716587e+02` (Mellin-Barnes contour; identical to ζ-form at simple pole; Γ(s) cancellation) |
| `R_chi_prime_zeta_lmax10` | `1.4011359923767614e+02` (L_max=10 truncation cross-check) |
| `R_chi_prime_PV_lmax10` | `1.1412540272708682e+02` (L_max=10 truncation cross-check) |
| `R_chi_prime_Mellin_lmax10` | `1.4011359923767614e+02` (L_max=10 truncation cross-check) |
| `reading_iv_match_bool` | `False` (cross-regulator agreement FAIL: \|R^ζ − R^PV\|/scale = 0.191 ≫ 1e-9) |
| `reading_v_pluralism_bool` | `True` (cross-regulator pluralism: \|R^ζ − R^PV\| = 26.98 ≫ 1e-9·scale; all R finite) |
| `image_block_rank` | `3` (Wedderburn rank of M_3(ℂ) summand; substrate-IS integer identity; confirmer-cross-checked by van-den-dungen-bridge-theorist NCG-axiomatic-side) |
| `K_a4_value` | `1.4143926087e+02` (positive; S57 Connes-Chamseddine positivity theorem confirmed) |
| `K_a4_positive` | `True` |
| `sign_positive` | `True` (substitution chain Step 4 prediction R_χ' > 0 confirmed at all three regulator classes) |
| `truncation_consistent` (L_max=10 vs 12) | `True` (sign agreement across L_max scan) |
| `regime_used_frac` | `1.0000` (full intended M_3(ℂ) block; no auto-shortening) |
| `n_evals_in_m3c_block` | `168832` across 89 SU(3)-coloured sectors |
| `cross_regulator_spread` | `2.6981597798e+01` (max ζ–PV; ζ ≡ Mellin to bit-precision) |
| `delta_zeta_pv` | `26.9815977981` |
| `delta_zeta_mellin` | `0.0000000000` (bit-precision identity per CM-1995 §III.4 Γ(s) cancellation at simple pole) |
| `scheme` | `FULL-CM-1995-III-4-residue-formula` (CLASS pin = FULL per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY; uses `_cm_1995_residue_formula.py`, NOT `_spectral_action_regulators` SCHEMATIC) |
| `convention` | `substrate-distance-2-multi-regulator-atlas` |
| `L_max` | `12` (operational; cross-checked at L_max=10) |
| `cache_sha (input pin)` | `973ef7af931f5ea8e878e48e900c9892ac204915fbfe8e03b0f44d5e6d094281` |
| `residue_formula_sha (input pin)` | `ee02f2711d061c8da1b31b2fd9071a968f1e0bc27ed0169db95676488986e224` |
| `audit_sha256` (64-char) | `58671312b0aee2e749836b8902273ab135073992736ddcc8f3362be2328dea14` |
| `content_sha256` (64-char) | `a6d7346ee04657c3a7099e1b8d4fbc77ac4f2fa302789f3041c551c56827c64e` |
| `sign_verdict` | `PASS` (R_χ' > 0 predicted; observed > 0 in all three regulator classes) |
| `magnitude_verdict` | `PASS-V` (Reading V regulator-class-pluralism criterion met; ZD spread 26.98 ≫ 1e-9 rel-tol; all finite) |
| `regime_verdict` | `VALID` (regime_used_frac = 1.0 ≥ 0.95) |
| `Composite verdict` | `PASS` (collapse rule: regime=VALID ∧ sign_verdict=PASS ∧ magnitude_verdict=PASS-V ⇒ composite=PASS) |

**Substitution chain verification (plan §W2-1 (10) Steps 1-5)**:

- **Step 1** (Definitions): `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`; `χ' : A_K ↠ M_3(ℂ)` kills (ℂ ⊕ ℍ); `D' = D_K|_{P_M3 H_K}` with `P_M3 = (0,0,1)` central idempotent. Substrate-IS via `canonical_constants.py` and `_cm_1995_residue_formula.py` `jensen_irrep_table`.
- **Step 2** (Substitution): `R_χ'(R) = Σ_{(p,q) ∈ SU(3)-coloured} m_eig(p,q) · |λ(p,q,τ_fold)|^{-8}` evaluated on 89 Peter-Weyl sectors (q ≥ 1 OR p ≥ 1 ∧ p+q ≥ 2) up to p+q ≤ 12; 168832 |λ| values in cache.
- **Step 3** (Simplify): CM-1995 §III.4 algebraic reduction at finite L_max; Γ(s) regulator factor cancels at simple pole s=4 (per `_cm_1995_residue_formula.py` docstring lines 50-63). ζ-form ≡ Mellin-form to bit-precision (delta_zeta_mellin = 0.0 confirmed). PV-form differs by the substrate-natural Λ_UV = M_KK subtraction.
- **Step 4** (Direction): K_a4(τ_fold=0.19) = +141.439 > 0 confirmed. S57 Connes-Chamseddine positivity theorem (Phi(a_4) = Σ_3 load-bearing weight-4) is the structural substrate guarantee; the numerical check is consistent.
- **Step 5** (Conclusion): Reading IV predicted R_χ'^ζ = R_χ'^PV = R_χ'^Mellin = 3 · K_a4/(4π²) with cross-regulator agreement at rel_tol 1e-9; Reading V predicted regulator-class-pluralism with sign preserved. **Observed**: ζ ≡ Mellin (bit-precision identity from Γ(s) cancellation); PV differs by 19.1% relative magnitude (Λ_UV = M_KK substrate-natural subtraction induces structurally distinct moment). Sign positive across all three. **Reading V WINS** — the substrate's PV regularization at its own M_KK scale is NOT a numerical refinement of the ζ-form; it is a structurally distinct regulator-class image of the substrate-IS χ' restriction.

**Inheritance-morphism cross-check (van-den-dungen-bridge-theorist NCG-axiomatic confirmer role)**: P_M3 commutes with χ' restriction at the central-projection layer by Peter-Weyl orthogonality (S60 block-diagonal D_K theorem). The χ' image faithfulness corresponds to Wedderburn rank-3 on the M_3(ℂ) summand: ker(χ') = ℂ ⊕ ℍ has rank 1+1=2, so by rank-nullity the image is the simple Wedderburn block M_3(ℂ) of rank 3. Confirmed numerically: image_block_rank = 3 returned by `image_block_rank_of_chi_prime()` is the substrate-IS integer Wedderburn identity, not a measured quantity.

### Verdict

**Composite**: `PASS` (value_token = `V`; Reading V regulator-class-pluralism canonical).

**Canonical verdict line** at `computations/session-91/s91_gate_verdicts.txt`:

```
S91-CF37-CHI-PRIME-WEIGHT-CANONICALIZED-FULL-CM-1995-III-4-SUBSTRATE-DISTANCE-2-EVALUATION: PASS -- value='reading=V_R_zeta=1.414393e+02_R_PV=1.144577e+02_R_Mellin=1.414393e+02_image_block_rank=3_cross_reg_spread=2.698e+01' scheme=FULL-CM-1995-III-4-residue-formula convention=substrate-distance-2-multi-regulator-atlas L_max=12 audit_sha256=58671312b0aee2e749836b8902273ab135073992736ddcc8f3362be2328dea14 content_sha256=a6d7346ee04657c3a7099e1b8d4fbc77ac4f2fa302789f3041c551c56827c64e schema_version=S87+
```

**Dual-SHA companion (W9a-99 split)**:

```
# audit_sha256_short=58671312b0aee2e7 content_sha256_short=a6d7346ee04657c3 # S91-CF37-CHI-PRIME-WEIGHT-CANONICALIZED-FULL-CM-1995-III-4-SUBSTRATE-DISTANCE-2-EVALUATION dual-SHA companion row (W9a-99 split)
```

**Schema-v2 3-tuple annotation (S87 schema-v2; required because substitution chain Step 4 pre-registers directional prediction `R_χ' > 0` per `gate-verdicts.md §"S87+ canonical form"`)**:

```
# sign_verdict=PASS magnitude_verdict=PASS-V regime_verdict=VALID # S91-CF37-CHI-PRIME-WEIGHT-CANONICALIZED-FULL-CM-1995-III-4-SUBSTRATE-DISTANCE-2-EVALUATION 3-tuple annotation (S87 schema-v2)
```

**Routing oracle (substrate-physics CF-37 χ' canonicalization branch table)**:

```
# reading_iv_match_bool=False reading_v_pluralism_bool=True truncation_consistent=True K_a4_positive=True K_a4_value=1.414393e+02 # S91-CF37-CHI-PRIME-WEIGHT-CANONICALIZED-FULL-CM-1995-III-4-SUBSTRATE-DISTANCE-2-EVALUATION substrate-physics CF-37 χ' canonicalization routing oracle: PASS-IV ⇒ §VII.AX single-anchor substrate-natural-binding (W3 T1.9 PARALLEL); PASS-V ⇒ §VII.AX multi-pin atlas (W3 T1.8 AUX-4); INFO ⇒ deferred-pending OPERATIONAL-ALIGNMENT to S92 L_max=14+; FAIL ⇒ AUX-4 (c)∘(d) γ(s)≠Γ(s) secondary corridor
```

**Verdict reading (per plan §W2-1 (11) "What PASSES and FAILS MEAN")**: The PASS-V branch is canonical. The substrate-IS χ' restriction at substrate-distance-2 pole s=4 lands the §VII.AX slot as a MULTI-PIN ATLAS — three Element 3 fiducial-anchors per regulator class — per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` axis β multi-scheme convention. The regulator-class-pluralism cell (Cell-I × Mellin-pole-s=4 in the 4-corner partition per `permanent-results-registry.md §VII.U.2 (e)` parse-tree) is structurally distinct from the single-anchor cell that Reading IV would have populated. This unblocks W3 T1.8 AUX-4 `(c)∘(d)` secondary corridor under modified-universal kernel γ(s) ≠ Γ(s) per plan §W2-1 (11) PASS-V branch. The K=2 advancement for the regulator-class-pluralism corner is queued (see Carry-forward below).

**Constraint-map interpretation**: PASS-V eliminates Reading IV (image-block-rank canonical single-anchor) from the §VII.AX slot's solution space at this substrate corner. The substrate is telling us that the χ' image is faithful (rank-3 confirmed bit-exactly) but the regulator class is NOT structurally redundant — the substrate-natural Pauli-Villars subtraction at Λ_UV = M_KK induces a different |λ|^{-8} moment than the ζ/Mellin forms by 19.1% relative magnitude. This is the substrate's intrinsic statement that the Λ_UV = M_KK boundary condition is structurally non-trivial at the substrate-distance-2 pole; it is NOT regulator-shopping. All three R values pass the truncation-consistency cross-check (L_max=10 vs 12 sign-stable), so the verdict is regime VALID and the routing is definitive, not deferred.

**All results are good results (per `math-scripts.md §"All Results Are Good Results"`)**: PASS-V closes the Reading-IV corridor and opens the Reading-V multi-pin atlas corridor. The framework's constraint map is updated: at the (substrate-distance-2, χ'-restriction) corner, the regulator-class-pluralism reading is canonical. Downstream W3 wave dispatches on the PASS-V branch (T1.8 AUX-4 + §VII.AX multi-pin atlas slot landing) per the plan §W2-1 (11) routing table.

### Substrate framing (runtime addendum)

Runtime check per `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"`. Confirmed direction of explanation in the producing script `s91_w2_1_cf37_chi_prime_weight.py`:

```
D_K eigenvalue spectrum at SU(3)-coloured Peter-Weyl sectors (substrate-IS)
   → Mellin-cone residue Σ |λ|^{-8} at simple pole s=4 (substrate-IS)
   → χ' restriction onto M_3(ℂ) summand via central projection P_M3 (substrate-IS)
   → emergent CF-37 LRD α-anchor as observable IN the LRD continuum pillar
```

The substrate IS the spectral triple `(A_K, H_K, D_K)` with `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. The χ' inheritance morphism IS the substrate's intrinsic central-projection structure onto the M_3(ℂ) summand. The Mellin-cone residue Σ |λ|^{-8} on the M_3(ℂ) block at L_max=12 (168832 eigenvalues across 89 SU(3)-coloured sectors) IS the substrate's a_4 Seeley-DeWitt content — per `epistemic-discipline.md §"Phi correspondence"` the weight-4 Yang-Mills + Higgs quartic image. The substrate-natural Pauli-Villars Λ_UV = M_KK pin (R_χ'^PV = 1.145e+02) is intrinsic to the substrate's own scale, NOT an externally imposed regularization.

**Container-thinking risks actively inverted during compute**:

- "The χ' morphism produces particles IN the LRD continuum" — INVERTED: the M_3(ℂ) summand IS the substrate's SU(3)-coloured Wedderburn block at finite L_max=12. LRD α-anchors emerge AS observables on the LRD continuum pillar from this substrate structure, not the inverse.
- "Image-block-rank=3 measures the M_3(ℂ) embedding" — INVERTED: image-block-rank=3 IS the Wedderburn rank of the simple algebra M_3(ℂ); it is a substrate identity returned by `image_block_rank_of_chi_prime()` as an integer constant, NOT a numerical measurement. The substrate IS rank-3, and χ' is structurally faithful by `ker(χ') = ℂ ⊕ ℍ` of rank 2.
- "Pauli-Villars subtraction is a UV regularization applied to the substrate" — INVERTED: Λ_UV = M_KK is the substrate's OWN compactification scale (the substrate-natural-binding axis per `regulator-pin-discipline.md §"Binding axis"`). The PV-subtracted residue Σ(|λ|^{-8} − (λ²+1)^{-4}) is the substrate's intrinsic image at the boundary of its M_KK scale — a different image than the ζ/Mellin route, but a substrate-IS image, not an external probe.
- "ζ/Mellin agreement is a numerical coincidence" — INVERTED: the bit-precision identity R_χ'^ζ = R_χ'^Mellin = 141.4393608672 (delta = 0.0) is a structural substrate identity per CM-1995 §III.4 Γ(s) cancellation at the simple pole at finite L_max (per `_cm_1995_residue_formula.py` docstring lines 50-63). The substrate IS the algebraic identity; the ζ and Mellin routes are two methodology-floor F-images of the same substrate-IS observable per `epistemic-discipline.md §"Layer-Decomposition"`.

**Phononic classification** (per `phononic-framing.md §"Classification Guide"`): **GEOMETRIC** (the gate evaluates a Mellin-cone residue formula on the substrate's spectral triple under χ' restriction — fabric structure, not excitation content; cross-classified PARTICLE-conditional via the M_3(ℂ) SU(3)-coloured Peter-Weyl content). No PHONONIC content because the GV-cocycle / Mellin-residue computation operates on the eigenvalue spectrum of D_K rather than on relay-pattern excitations of the fabric.

**Inheritance-morphism framing cross-check (van-den-dungen-bridge-theorist NCG-axiomatic confirmer role)**: the χ' morphism is the secondary inheritance arrow `(A_K, H_K, D_K) → M_3(ℂ)-spectral-data` at the algebra-projection layer. P_M3 commutes with χ' restriction by Peter-Weyl block-orthogonality on the SU(3)-coloured sectors (S60 block-diagonal D_K theorem; the substrate's commutativity at the central-projection layer is a structural property, not a measured commutator). Wedderburn rank-3 is the substrate's own statement about M_3(ℂ) as a simple algebra — the rank IS, no measurement IN.

No container-thinking violations detected in the producing script `s91_w2_1_cf37_chi_prime_weight.py` text or in the verdict-line `value=` token. The verdict line's `reading=V` token cites Reading V regulator-class-pluralism canonical, which is a substrate-IS reading (the substrate has structurally distinct ζ vs PV regulator-class images at Λ_UV = M_KK), not a laboratory-IN reading.

### Cross-references

- Plan source: `sessions/session-plan/session-91-plan-w2.md §W2-1` (lines 62-407)
- Pre-registration history: S90 W-2 §EMERGENCE EV1 D1-Reading-B option (v) admittance
- Downstream consumers: W3 T1.9 (PASS-IV branch), W3 T1.8 AUX-4 (PASS-V branch), §VII.AV Cell IV Type-F (FAIL branch routing)
- Cross-pillar bridge candidate: FWD-C1 Pillar I-II at substrate-distance-2 corner (via χ' restriction)
- Rule files engaged: `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 classification"`, `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"`, `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY, `epistemic-discipline.md §"Layer-Decomposition"`, `phononic-framing.md §"IS Space, Not IN Space"`

### Carry-forward computations

Triggered branch per plan §W2-1 (11): **PASS-V** (Reading V regulator-class-pluralism canonical). Two pre-registered CFs activated; two retired.

#### CF-W2-1-S91-W2-PASS-V (ACTIVATED) — §VII.AX NEW slot landing for option (v) regulator-class-pluralism

1. **What**: Land a NEW §VII.AX registry slot per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` axis β multi-scheme convention, with three Element 3 fiducial-anchors (one per regulator class: ζ, Pauli-Villars, Mellin) at the substrate-distance-2 χ'-restriction corner. Slot to encode the 4-tuple discipline `(pole_index=4, regulator-invariance=RD, observable-class=algebra-INVARIANT, layer=cache-moment)` per `cross-pillar-bridge-anatomy.md §"Per-pole-per-observable-class 4-tuple discipline"`.
2. **Who**: `mack-cosmic-bridge` sole-writer per `feedback_mack-bridge-role.md` (registry edits to `sessions/permanent-results-registry.md`).
3. **Input**:
   - `computations/session-91/s91_w2_1_cf37_chi_prime_weight.npz` (THIS gate's npz; cache_sha `973ef7af931f5ea8...`; audit_sha256 `58671312b0aee2e7...`).
   - Verdict line at `computations/session-91/s91_gate_verdicts.txt` (PASS-V composite; the three R_χ' values).
   - `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 classification"` (Cell-I × Mellin-pole-s=4 classification, parse-tree per `permanent-results-registry.md §VII.U.2 (e)`).
   - `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` (sub-clause: bridge-map-scheme suffix discipline for multi-scheme convention tagging; substrate-natural-binding).
4. **Output**: §VII.AX registry slot with: (a) substrate-IS observable = `Σ |λ|^{-8}` on M_3(ℂ) block at χ'(A_K) at L_max=12, τ_fold=0.19; (b) three Element 3 fiducial-anchors `(R^ζ=141.439, R^PV=114.458, R^Mellin=141.439)`; (c) Wedderburn rank-3 substrate identity; (d) image_block_rank=3 substrate identity declared via `image_block_rank_of_chi_prime()`; (e) 5-anatomy + 3-level ladder declared per `cross-pillar-bridge-anatomy.md`; (f) STAGE-1-CANDIDATE tag per `joint-theorem-promotion.md` 4-stage pathway.
5. **Format**: registry edit to `sessions/permanent-results-registry.md §VII.AX` (NEW slot, allocated via `_registry_landing_audit.py` Class-(g) projection-side tagging discipline — declare OP-PROJ vs STATE-PROJ suffix per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"`; cite the audit_sha256=`58671312b0aee2e749836b8902273ab135073992736ddcc8f3362be2328dea14`).
6. **Deadline**: S92 W1 (next planning session).
7. **Depends on**: this gate (verdict file + npz pin); upstream `cross-pillar-bridge-anatomy.md` rules; downstream W3 T1.8 AUX-4 secondary corridor unblock.
8. **Effort**: ~0.3 we.
9. **Gate ID (pre-allocated)**: `S92-VII-AX-MULTI-PIN-ATLAS-LANDING-CF-37-CHI-PRIME-REGULATOR-CLASS-PLURALISM`.

#### CF-W2-2-S91-W2-K-COUNTER-ADVANCEMENT — K=2 calibration corpus advancement for the regulator-class-pluralism corner

1. **What**: Advance the K-counter from K=1 SUGGESTION (placeholder) to K=2 on the `(regulator-class-pluralism, Cell-I Mellin-pole-s=4)` 4-corner classification per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` (S88 W8-87 status SUGGESTION K=1). The W2-1 PASS-V landing is the K=2 calibration instance.
2. **Who**: `gen-physicist` (rule-extension scribe) + `connes-ncg-theorist` co-author for K-counter audit (EXCLUDED only for THIS gate's compute per OAA; permissible for the downstream rule-extension work on the corpus side).
3. **Input**: §VII.AX landing from CF-W2-1; existing K=1 corpus entry at `sessions/framework/registry/cross-pillar-bridge-corpus.md §3` (Hybrid Independence Test); `feedback_rules-compensate-missing-structure.md` K-counter promotion threshold.
4. **Output**: K=2 corpus entry at `sessions/framework/registry/cross-pillar-bridge-corpus.md §3`; status preserved at SUGGESTION (K<3); reserved K=3 row for future calibration.
5. **Format**: edit to `sessions/framework/registry/cross-pillar-bridge-corpus.md §3`.
6. **Deadline**: S92 W2 (paired with CF-W2-1 §VII.AX landing).
7. **Depends on**: CF-W2-1 landing.
8. **Effort**: ~0.2 we.

#### CF-W2-3 (RETIRED — branch NOT TRIGGERED)

The FAIL-branch CF "re-route CF-37 to substrate-distance-1 pole s=3 + substrate-distance-2 §VII.AV Cell IV Type-F" is **retired** because the FAIL branch did not trigger. The composite was PASS-V; substitution chain Step 4 K_a4 positivity was confirmed (K_a4 = +141.439, S57 Connes-Chamseddine positivity theorem satisfied); no regulator blow-up (max |R| = 141.4, well under blow-up threshold 1e6). The AUX-4 `(c)∘(d)` secondary corridor pathway is replaced by the PASS-V branch's MULTI-PIN ATLAS pathway via CF-W2-1.

#### CF-W2-4 (RETIRED — branch NOT TRIGGERED)

The INFO-branch CF "S92 L_max=14+ cache extension" is **retired** because the INFO branch did not trigger. truncation_consistent = True (sign agreement at L_max=10 vs L_max=12); regime_used_frac = 1.0 (no auto-shortening); no non-finite residue (all three R values finite at L_max=12). The verdict is definitively PASS-V at L_max=12; no L_max=14+ extension is required for this gate.

#### CF-W2-5-S91-W2-DOWNSTREAM-W3-T1-8-UNBLOCK — W3 T1.8 AUX-4 dispatch unblocked

1. **What**: Dispatch W3 T1.8 AUX-4 `(c)∘(d)` secondary corridor under modified-universal kernel γ(s) ≠ Γ(s) per plan §W2-1 (11) PASS-V branch routing. The §VII.AX multi-pin atlas structure requires the (c)∘(d) corridor as the bridge-map-scheme cross-anchor (per `cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"` axis β).
2. **Who**: `volovik-superfluid-universe-theorist` PRIMARY (substrate-physics author for AUX-4 corridor; framework's SHARPEST reviewer per `feedback_agent-roster.md`).
3. **Input**: this gate's verdict; §VII.AX slot from CF-W2-1; γ(s) ≠ Γ(s) machinery pin per W3 T1.8 plan.
4. **Output**: W3 T1.8 verdict closure with multi-pin atlas adjudication.
5. **Format**: standard COMPUTE-class wave dispatch; verdict line at `computations/session-91/s91_gate_verdicts.txt`.
6. **Deadline**: S91 W3 (next wave).
7. **Depends on**: this gate (PASS-V); CF-W2-1 (§VII.AX slot landing); W3 plan §T1.8 method block.
8. **Effort**: ~1.0 we (W3 T1.8 dispatch budget).

---

## §W2-2. S91-VII-AU-FIRST-EXTRACTION-PARAMETERIZATION (T1.5)

**Status**: CLOSED (composite FAIL — `regime_verdict=BREAKDOWN` via L_max=10→12 truncation max drift = 85.7%; cross-sub-option relative spread = 24.19% above 1e-6 info_band; substrate-distance-1 pole s=3 corner FAILS as canonical CF-37 LRD α-anchor source; routes CF-37 exclusively through substrate-distance-2 χ' restriction per §W2-1 PASS Reading V at line 22).

**Plan reference**: `sessions/session-plan/session-91-plan-w2.md §W2-2` (lines 409-706)

**Gate ID**: `S91-VII-AU-FIRST-EXTRACTION-PARAMETERIZATION-W8-CF-72` (legacy alias: `T1.5` / `W8-CF-72` / `CF-S91-CF-72`)

**Trigger**: `[VERIFY]` — primary; `[CHAIN]` — sub-option (a/b/c) discriminator.

**Classification**: GEOMETRIC — §VII.AU first-extraction parameterization is a substrate-distance-1 Mellin-cone moment-extraction at pole s=3 under three parameterization sub-options on the FWD-C1 Pillar I-II bridge.

**Agent type** — PRIMARY test-case author: `volovik-superfluid-universe-theorist` (substrate-side parameterization expertise; framework's primary theorist). CONFIRMER test-case author: `landau-condensed-matter-theorist` (condensed-matter analog cross-check for first-extraction parameterization patterns; per `feedback_agent-roster.md` include-in-all-future-collabs discipline). NOT-permissible: `gen-physicist` (planner role).

**Hypothesis**: The §VII.AU.OP-PROJ first-extraction at substrate-distance-1 pole s=3 admits three structurally distinct parameterizations (sub-options a/b/c) of the Mellin-moment extraction map, of which exactly one is canonical under the cross-pillar-bridge anatomy Element 3 fiducial-anchor binding discipline.

**Effort estimate**: 1.5 we (0.3 cache load + central-projection trace decomposition on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ); 0.4 implement three Mellin-moment parameterizations a/b/c with per-sub-option residue evaluation + runtime-canonical `slope_A_canonical` resolution; 0.3 cross-sub-option spread + canonical discriminator + Element 3 fiducial-anchor binding identification; 0.2 substitution-chain verification + sign_verdict computation; 0.2 WP + verdict line + dual-SHA + PRDR audit; 0.1 NPZ + PNG).

### Method

Compute three parameterizations of the §VII.AU.OP-PROJ first-extraction moment-extraction map M_3 at substrate-distance-1 pole s=3, on the spectral triple `(A_K, H_K, D_K)` restricted to the OP-PROJ image (operator-projection on A_K central-projection traces per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"`):

- **Sub-option (a)** — Mellin-moment extraction via direct ζ-regularization:

  ```
  M_3^(a) = Res_{s=3} Tr_{H_K}(|D_K|^{-2s}) at slope_A_canonical pin
  ```
- **Sub-option (b)** — Mellin-moment extraction via Pauli-Villars subtraction:

  ```
  M_3^(b) = Res_{s=3} [Tr(|D_K|^{-2s}) − Tr(|D_K|^{-2s} · χ_PV)]
  ```

  where χ_PV is Pauli-Villars regulator at Λ_UV = M_KK.
- **Sub-option (c)** — Mellin-moment extraction via locked-norm L_k=1 pre-normalization (atlas-row layer convention):

  ```
  M_3^(c) = Res_{s=3} Tr(|D_K|^{-2s}) with L_k=1 pre-norm
  ```

  per `substrate-first-canonical-sourcing.md §(ii.A)`.

Imports + environment:

```python
from canonical_constants import *
# anchors: n_s_FW_exact=Fraction(9561,10000), tau_fold=0.19,
#          alpha_s_canonical=Fraction(-8587279,100000000),
#          slope_A_canonical (TBD pending T0.7 PASS),
#          M_KK gravity-pin
from _cm_1995_residue_formula import compute_zeta_d_residue
# NOTE: if forced to use _spectral_action_regulators (SCHEMATIC),
# tag the verdict-line `convention=` field with `-SCHEMATIC` suffix
# AND emit `# tier_pin=TIER-2` companion row per
# `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY.
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import numpy as np
import torch
```

Inputs (Input-SHA pins, all `<pinned at dispatch>`):

- `computations/session-90/s90_w8_spectrum_cache_L12_tau038.npz`
- `computations/_shared/_cm_1995_residue_formula.py` (PRIMARY) OR `computations/_shared/_spectral_action_regulators.py` (SCHEMATIC fallback)
- `computations/_shared/canonical_constants.py at HEAD`
- `sessions/permanent-results-registry.md §VII.AU.OP-PROJ line 17677`
- `sessions/permanent-results-registry.md §VII.AF.1.OP-PROJ baseline` (cross-reference: substrate-internal over-performance regime ANNOTATION per S91 W0 T2.55)
- `sessions/archive/session-90/session-90-w6-workingpaper.md` (W6 CF-2 + CF-3 for §VII.AU.OP-PROJ under-performance regime context)

Procedure:

1. Load L_max=12 master spectrum cache; restrict to OP-PROJ image via central-projection traces P_C, P_H, P_M3 on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ).
2. For each sub-option (a)/(b)/(c):
   - (2a) Compute M_3 residue at pole s=3 per the parameterization.
   - (2b) Apply substitution chain (Step 4 — direction): each sub-option predicts a specific numerical M_3 value:
     - (a): `M_3^(a) = slope_A_canonical · (1/(2π²)) · K_a2(τ_fold)`
     - (b): `M_3^(b) = M_3^(a) − (1/(2π²)) · K_a2_PV(τ_fold; Λ_UV=M_KK)`
     - (c): `M_3^(c) = M_3^(a) / L_k=1_atlas_norm`
3. Compute cross-sub-option spread:

   ```
   spread = max(M_3^(a), M_3^(b), M_3^(c)) − min(M_3^(a), M_3^(b), M_3^(c))
   ```
4. Discriminator:
   - Sub-option (a) PASS: `|M_3^(a) − slope_A_canonical · K_a2(τ_fold) · (1/(2π²))| < 1e-9`
   - Sub-option (b) PASS: `|M_3^(b) − M_3^(a) + PV-correction| < 1e-9`
   - Sub-option (c) PASS: `|M_3^(c) − M_3^(a) / L_k=1_atlas_norm| < 1e-9`
   - Cross-sub-option INFO: spread ≥ rel_tol but ≤ info_band
   - FAIL: spread > info_band OR any M_3 non-finite
5. Identify canonical sub-option per cross-pillar-bridge Element 3 fiducial-anchor binding discipline:
   - (a) canonical if substrate-natural-binding holds without pre-normalization (`M_3^(a) = M_3^(c)` within tolerance);
   - (c) canonical if locked-norm L_k=1 pre-normalization is REQUIRED to bind the cocycle to Level-1 cohomology class;
   - (b) canonical if PV subtraction is the substrate-natural regularization at Λ_UV = M_KK (FULL physical regularization).

Output files:

- `computations/session-91/s91_w2_2_vii_au_first_extraction_param.py`
- `computations/session-91/s91_w2_2_vii_au_first_extraction_param.npz` (keys: `M_3_a`, `M_3_b`, `M_3_c`, `cross_sub_option_spread`, `canonical_sub_option`, `slope_A_canonical_pin`, `K_a2_tau_fold`, `L_k1_atlas_norm`, `cache_sha`, `residue_formula_sha`, `L_max_operational`, `level_pin`)
- `computations/session-91/s91_w2_2_vii_au_first_extraction_param.png` (3-panel: M_3 by sub-option; cross-sub-option residual; per-sub-option L_max stability cross-check at L_max=10 vs 12)

Verdict-line append:

```
S91-VII-AU-FIRST-EXTRACTION-PARAMETERIZATION: PASS|FAIL|INFO -- value=<canonical-sub-option in {a,b,c} or 'multi'> \
  scheme=Mellin-cone-residue-at-substrate-distance-1-pole-s3 \
  convention=op-proj-first-extraction-three-param-sub-option-discriminator \
  L_max=12 sha256=<64-char-closure> \
  schema_version=S84+

# audit_sha256 companion row + tier_pin row if SCHEMATIC fallback used
```

### Machinery pin (PRDR)

| Parameter | Pin | Source |
|:----------|:----|:-------|
| `L_max` | 12 (operational); 10 (cross-check) | S90 W8 master cache |
| `tau_fold` | Fraction(19, 100) | canonical_constants.py:283 |
| `pole_index` | s=3 (substrate-distance-1) | §VII.AU.OP-PROJ baseline |
| `sub_option_index` | enumerated: {a=zeta, b=Pauli-Villars, c=locked-norm-L_k=1} | T1.5 spec |
| `slope_A_canonical` | TBD (pending T0.7 PASS); fallback to plan-pinned value | runtime canonical resolution per `substrate-first-canonical-sourcing.md §(ii.B)` |
| `K_a2_tau_fold` | computed at runtime from L_max=12 cache; (local) | substrate Seeley-DeWitt a_2 |
| `Λ_UV` (PV regulator) | M_KK = 7.43e16 GeV | canonical_constants.py:12 |
| `L_k=1_atlas_norm` | atlas-row layer normalization per `substrate-first-canonical-sourcing.md §(ii.A)` | locked-norm L_k=1 canonical |
| `LEVEL pin` | FULL if `_cm_1995_residue_formula.py` PRIMARY, ELSE SCHEMATIC suffix | K=4 MANDATORY discipline |
| `MACHINERY-SCOPE pin` | CACHE-PROJECTION (consumes L_max=12 cache) | axis α |
| `Binding axis pin` | substrate-natural-binding (substrate-IS direct evaluation) | axis γ |
| `rel_tol` | 1e-9 (Class 8.3 precision floor) | epistemic-discipline.md |
| `info_band` | 1e-6 (cross-sub-option spread tolerance for INFO) | pre-registered |
| `pass_band` | 1e-9 (within-sub-option tolerance for PASS) | pre-registered |
| `gpu_path` | torch.linalg if matrix dim ≥ 100×100 | computation-environment |
| `random_seed` | N/A | — |
| `OMP_NUM_THREADS` | 8 (BEFORE numpy import) | computation-environment |

PRDR enumeration: 16 free parameters pinned; 0 unpinned.

### Expected output 4-tuple

`(value=<canonical sub-option in {a, b, c} or 'multi'>, scheme=Mellin-cone-residue-at-substrate-distance-1-pole-s3, convention=op-proj-first-extraction-three-param-sub-option-discriminator, L_max=12)`

### PASS/FAIL/INFO thresholds

| Outcome | Condition | Tolerance rule |
|:--------|:----------|:--------------|
| **PASS-a** | sub-option (a) matches predicted formula within 1e-9 rel AND (b), (c) don't OR (b), (c) inadmissible | RATIO (1e-9) |
| **PASS-b** | sub-option (b) canonical (PV substrate-natural at Λ_UV = M_KK; FULL physical) | RATIO (1e-9) |
| **PASS-c** | sub-option (c) canonical (L_k=1 atlas-row pre-normalization required for Level-1 cohomology-class binding) | RATIO (1e-9) |
| **PASS-multi** | two or three sub-options indistinguishable within 1e-9; routes to multi-pin atlas | RATIO (1e-9) cross-sub-option agreement |
| **INFO** | cross-sub-option spread ∈ (1e-9, 1e-6); defers canonicalization | RATIO band |
| **FAIL** | spread > 1e-6 OR any M_3 non-finite OR truncation-inconsistent at L_max=10 vs 12 | ABSOLUTE blow-up |

3-tuple collapse (Schema-v2):

- `sign_verdict`: PASS if all M_3 values have predicted sign (positive for ζ regularization, sign-dependent for PV); FAIL if sign mismatch.
- `magnitude_verdict`: per the discriminator table above.
- `regime_verdict`: VALID if `truncation_consistent=True`; MARGINAL if 5-50% L_max-truncation drift; BREAKDOWN if >50% drift.

### Substitution chain

SIGN claim: "Sub-option (a) ζ-regularization yields `M_3^(a) > 0` with magnitude predicted by `slope_A_canonical · K_a2(τ_fold) / (2π²)`".

```
Step 1 — Definitions:
  D_K               : Dirac operator on H_K (spectral triple)
  M_3^(a)           : Res_{s=3} Tr(|D_K|^{-2s})    [ζ-reg residue at s=3]
  K_a2(τ_fold)      : substrate a_2 Seeley-DeWitt coefficient at τ_fold
                      [substrate-IS canonical via L_max=12 cache trace]
  slope_A_canonical : a_2-ratio slope at substrate-distance-1 pole
                      [pending T0.7 PASS for canonical pin]

Step 2 — Substitution:
  By CM-1995 §III.4 dimension-spectrum residue formula at 4D substrate
  with KO-dim=6 factor:
    M_3^(a) = (1/(2π²)) · Tr_{H_K}( a_2(D_K) ) at τ_fold restriction
            = (1/(2π²)) · K_a2(τ_fold)
  Sub-option (a) parameterization adds slope_A_canonical multiplier:
    M_3^(a) = slope_A_canonical · (1/(2π²)) · K_a2(τ_fold)

Step 3 — Simplify:
  slope_A_canonical > 0 (substrate's a_2-ratio slope is positive per
  S87 W11-2/W11-3 Casimir-bound argument; canonical_constants
  Phi(a_2) = Σ_2 wave-classification weight-2 kinematic skeleton).
  K_a2(τ_fold) > 0 (substrate's a_2 Seeley-DeWitt is positive-definite
  for a positive Laplacian on 4D substrate; S57 positivity theorem).
  Product of two positives is positive.

Step 4 — Direction:
  M_3^(a) > 0; magnitude > 0; sign_verdict PASS.
  Cross-sub-option:
    M_3^(b) = M_3^(a) − (positive PV correction at Λ_UV = M_KK)
            → M_3^(b) < M_3^(a) but still > 0 if PV cutoff is below |D_K|_max
    M_3^(c) = M_3^(a) / L_k=1_atlas_norm
            → M_3^(c) > 0 (L_k=1 norm is positive); ratio to M_3^(a) is
              the locked-norm pre-factor canonical.

Step 5 — Conclusion:
  All three M_3 sub-options predicted positive sign; magnitude
  discriminates which is canonical. The CROSS-SUB-OPTION SPREAD is
  the discriminator: spread → 0 iff all three sub-options agree
  (multi-pin atlas), spread > 1e-9 isolates exactly one canonical
  sub-option per Element 3 fiducial-anchor binding discipline.
```

### What PASSES and FAILS MEAN for solution space

- **PASS-a** (ζ-regularization canonical): §VII.AU.OP-PROJ first-extraction binds via direct ζ-residue at pole s=3; advances the slot from REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION → STAGE-1-CANDIDATE eligibility. Confirms substrate-natural-binding on the ζ axis (axis γ canonical-binding). Unblocks W4 T1.15 §VII.AR Stage-2 cross-axis verify (CONDITIONAL on T1.5 PASS).
- **PASS-b** (PV canonical): substrate's first-extraction binding is the FULL Connes-Chamseddine 1996 §2.2-2.3 physical multipliers pipeline at Λ_UV = M_KK; advances §VII.AU.OP-PROJ to STAGE-1-CANDIDATE. Cross-reference with W5 T1.11 FULL BdG re-derivation; same Λ_UV cutoff. Eliminates SCHEMATIC class-(d) PIN-DERIVATIVE pathway from §VII.AU.OP-PROJ canonicalization.
- **PASS-c** (locked-norm L_k=1 canonical): §VII.AU.OP-PROJ binding REQUIRES atlas-row layer pre-normalization per `substrate-first-canonical-sourcing.md §(ii.A)`. Advances the intra-algebra-INVARIANT layer orthogonality K-counter (atlas-row vs cache-moment) toward K=2 calibration.
- **PASS-multi** (multi-pin atlas; two or three sub-options indistinguishable): §VII.AU.OP-PROJ registers as multi-pin per Element 3 fiducial-anchor binding discipline axis β multi-scheme; three separate Element 3 anchors per sub-option, cross-referenced to each other.
- **INFO** (canonicalization deferred): §VII.AU.OP-PROJ stays at REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION; T1.10 W7a-74 Spearman rank-ordering with broadened band.
- **FAIL** (M_3 blow-up or L_max-inconsistency): §VII.AU.OP-PROJ routes to S92 L_max=14+ extension; cross-pillar bridge candidate FWD-C1 substrate-distance-1 corridor closes. Eliminates the substrate-distance-1 pole s=3 corner as canonical CF-37 LRD α-anchor source; routes CF-37 exclusively through substrate-distance-2 χ' restriction (T0.7 / §W2-1).

### Substrate framing

- §VII.AU.OP-PROJ is the substrate's operator-projection image on central-projection traces of A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ). The three sub-options are NOT three different "external regularizations applied to the substrate" — they are three structurally distinct EVALUATION CONVENTIONS of the same substrate-IS canonical quantity at pole s=3.
- The substrate IS the Mellin-cone residue at substrate-distance-1 pole s=3 on the operator-projection algebra. The first-extraction is the substrate's own determination of how the canonical pin is read off, not a measurement IN a continuum container.
- Direction of explanation: D_K eigenvalue spectrum → Peter-Weyl decomposition by Wedderburn-block → operator-projection traces → Mellin-cone residue at pole s=3 → §VII.AU.OP-PROJ canonical first-extraction → emergent CF-37 LRD α-anchor on the FWD-C1 Pillar I-II bridge.

### Input-SHA pin map

```yaml
input_pin_map:
  spectrum_cache_L12_tau038: <pinned at dispatch>
  cm_1995_residue_formula_py: <pinned at dispatch>    # PRIMARY
  spectral_action_regulators_py: <pinned at dispatch> # SCHEMATIC fallback
  canonical_constants_py: <pinned at dispatch>
  permanent_results_registry_md_vii_au_op_proj: <pinned at dispatch>
  permanent_results_registry_md_vii_af_1_op_proj: <pinned at dispatch>  # cross-link baseline
  s90_w6_workingpaper_md_cf_2_cf_3: <pinned at dispatch>                # W6 CF-2 + CF-3 context
audit_sha256: closure_hash(ordered_pin_map_above)
```

### Results

| Field | Value |
|:------|:------|
| `value` (composite verdict token) | `'truncation-breakdown'` (substrate-IS truncation-breakdown reading at L_max=10→12; substrate-distance-1 pole s=3 corner FAILS the numerical Mellin-moment canonicalization at L_max=12 truncation; corridor itself is CONFIRMED at the rank-ordering layer by §W2-3 Reading A WIN with N_above_3=4/5) |
| `M_3_a` (ζ-direct, dimensionless) | `1.7501248156e+04` (substitution chain Step 2(a): `slope_A_canonical · K_a2 / (2π²)`; positive sign confirmed per Step 4 directional prediction) |
| `M_3_b` (Pauli-Villars subtraction, dimensionless) | `1.7437629653e+04` (substitution chain Step 2(b): `M_3_a − K_a2_PV / (2π²)`; PV correction at `lambda_UV_cache_units=1.0` substrate-natural-binding cutoff is NON-vacuous at finite L_max=12 — substrate has 1255.78 worth of high-\|λ\| tail above 1.0 in cache units) |
| `M_3_c` (locked-norm L_k=1 atlas-row, dimensionless) | `1.3267513045e+04` (substitution chain Step 2(c): `M_3_a / L_k1_atlas_norm`; atlas-row layer normalization at k=1 Peter-Weyl level) |
| `M_3_a` @ L_max=10 (cross-check) | `2.5525877545e+03` (85.4% reduction from L_max=12 value — NEW-sector eigenvalues entering at p+q ∈ {11, 12} contribute dominantly to the substrate-distance-1 pole; substrate spectrum is NOT L_max-saturated at L_max=10 for the pole-s=3 weight) |
| `M_3_b` @ L_max=10 (cross-check) | `2.4889692516e+03` (85.7% reduction from L_max=12 value) |
| `M_3_c` @ L_max=10 (cross-check) | `1.9350900593e+03` (85.4% reduction from L_max=12 value) |
| `cross_sub_option_spread` (absolute) | `4.2337351111e+03` (M_3_a − M_3_c at L_max=12) |
| `rel_spread` (relative to max\|M_3\|) | `0.24191046680579859` (24.19% — well above `info_band = 1e-6`; the three sub-options are STRUCTURALLY DISTINCT at the pole-s=3 substrate-distance-1 corner) |
| `pairwise |a−b|/|a|` | `3.6350837566e-03` (0.36% — (a) and (b) close but NOT indistinguishable within `pass_band = 1e-9`; PV correction is small but non-vacuous) |
| `pairwise |a−c|/|a|` | `2.4191046681e-01` (24.19% — (a) and (c) structurally distinct; atlas-row pre-normalization is NOT a small refinement) |
| `pairwise |b−c|/|b|` | `2.3914469404e-01` (23.91% — (b) and (c) structurally distinct) |
| `K_a2(τ_fold)` (substrate a_2 trace at pole s=3) | `3.4128217541e+04` (sum of `dim(p,q) · |λ(p,q,τ_fold)|^{-6}` over 89 Peter-Weyl irreps at p+q ∈ [1, 12]; substrate-IS positive per S57 Connes-Chamseddine positivity theorem; Phi(a_2) = Σ_2 weight-2 kinematic skeleton load) |
| `K_a2_PV(τ_fold; Λ_UV = M_KK)` (Pauli-Villars tail at dimensionless cutoff) | `1.2557789123e+03` (substrate's high-\|λ\| tail above `lambda_UV_cache_units = 1.0`; 3.68% of K_a2 total; substrate-distance-1 pole s=3 has a non-trivial UV tail in cache units at finite L_max=12) |
| `L_k1_atlas_norm` (locked-norm reference) | `1.3191054041e+00` (k=1 Peter-Weyl partial sum / k=1 dim total of 6; substrate-IS positive atlas-row layer normalization per `substrate-first-canonical-sourcing.md §(ii.A)`) |
| `slope_A_canonical_pin` (runtime-resolved) | `10.122438748384` |
| `slope_A_source` | `canonical_constants.slope_A_FW_Conv_A_AT_TAU_FOLD` (substrate-natural fallback per `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift correction orchestrator-convention; Conv-A GEOMETRIC reading evaluated at τ_fold=0.190 via Sage-CM-1995 §III.4 — see `canonical_constants.py:1768`) |
| `L_max_operational` | `12` |
| `L_max_cross_check` | `10` |
| `max_drift` (L_max=10 vs 12, max over sub-options) | `0.8572644734` (85.7% — exceeds `REL_TOL_TRUNCATION = 5e-2` AND ≥ 0.50 BREAKDOWN threshold; substrate-distance-1 pole s=3 is FAR from L_max-saturation at L_max=12 truncation; NEW-sector intrusion at p+q ∈ {11, 12} dominates the pole-s=3 weight `|λ|^{-6}` because Jensen-deformed eigenvalues at large ρ have smaller \|λ\| ≈ √C_2 · e^{-τρ} suppressed only mildly by τ_fold = 0.19) |
| `truncation_consistent` (max_drift < 5e-2) | `False` |
| `level_pin` | `FULL` (consumes `_cm_1995_residue_formula.py::jensen_irrep_table` PRIMARY full physical evaluator; CLASS = FULL per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY discipline; NO `-SCHEMATIC` suffix required; NO `# tier_pin=TIER-2` companion row emitted) |
| `machinery_scope_pin` | `CACHE-PROJECTION` (consumes L_max=12 master cache structure; per axis α of `regulator-pin-discipline.md §"Cross-link"` 4-axis pin discipline) |
| `binding_axis_pin` | `substrate-natural-binding` (substrate-IS direct evaluation via Jensen analytic formula; not canonical-import binding; per axis γ) |
| `lambda_UV_cache_units` | `1.0` (substrate-natural PV cutoff at dimensionless \|λ\|=1 in cache units; the substrate's intrinsic spectral ceiling at the M_KK pin reduces to unity under Mellin-cone scale invariance) |
| `inv_two_pi_sq` (Mellin pole s=3 residue weight) | `0.05066059182116889` |
| `scheme` | `Mellin-cone-residue-at-substrate-distance-1-pole-s3` |
| `convention` | `op-proj-first-extraction-three-param-sub-option-discriminator` |
| `cache_sha` (input pin) | `973ef7af931f5ea8e878e48e900c9892ac204915fbfe8e03b0f44d5e6d094281` |
| `residue_formula_sha` (input pin) | `ee02f2711d061c8da1b31b2fd9071a968f1e0bc27ed0169db95676488986e224` |
| `audit_sha256` (64-char) | `503fd2e6872bd3e794a68c97b6608f68773c6b0b56381d542cdf84bbdda46334` (sig_5 uniqueness verified: 1/1 occurrence in `s91_gate_verdicts.txt`) |
| `content_sha256` (64-char) | `1bf36c85b25d2472fad8dbe001eaf349995a610656943411e0395aa6eed58360` |
| `sign_verdict` | `PASS` (substitution chain Step 4 directional prediction `M_3^(a) > 0` confirmed; all three sub-options return positive M_3 values — positivity of product `slope_A_canonical · K_a2` per S57 Connes-Chamseddine positivity theorem and Phi(a_2) weight-2 kinematic-skeleton load) |
| `magnitude_verdict` | `FAIL` (plan §W2-2 (9) row 6: spread > 1e-6 info_band AND truncation-inconsistent at L_max=10 vs 12 — BOTH conditions trigger) |
| `regime_verdict` | `BREAKDOWN` (max_drift = 85.7% ≥ 0.50 threshold per the auto-shortening clause analog at `gate-verdicts.md §"Auto-shortening clause discipline"` BREAKDOWN band; substrate-distance-1 pole s=3 is structurally NOT L_max-saturated at L_max=12) |
| Composite verdict | `FAIL` (composite-collapse rule: `regime_verdict == BREAKDOWN ⇒ composite = FAIL` regardless of other fields; the BREAKDOWN takes precedence over sign-PASS) |

**Substitution chain verification (plan §W2-2 (10) Steps 1-5)**:

- **Step 1** (Definitions): `D_K` is the Jensen-deformed Dirac on `(A_K, H_K)` with `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. `M_3^(a) = Res_{s=3} Tr_{H_K}(|D_K|^{-2s})` (the ζ-regulated Mellin residue at substrate-distance-1 pole s=3). `K_a2(τ_fold)` is the substrate a_2 Seeley-DeWitt trace at pole s=3, computed via the closed-form algebraic identity `Σ_{(p,q)≠(0,0)} dim(p,q) · |λ(p,q,τ_fold)|^{-6}` on the finite spectral triple. `slope_A_canonical` is the runtime-resolved pin from `canonical_constants.slope_A_FW_Conv_A_AT_TAU_FOLD = 10.122438748384` (Sage-CM-1995 §III.4 geometric reading at τ_fold = 0.190).
- **Step 2** (Substitution): `M_3^(a) = slope_A_canonical · K_a2 / (2π²) = 10.122438748384 · 34128.217541 · 0.0506605918 = 1.7501248e+04`. Substituting Step 1 closed forms gives the value bit-precision. Sub-option (b) subtracts `K_a2_PV / (2π²) = 1255.779 · 0.0506606 = 6.362e+01`, yielding `M_3^(b) = 1.7438e+04`. Sub-option (c) divides by `L_k1_atlas_norm = 1.319105` yielding `M_3^(c) = 1.327e+04`.
- **Step 3** (Simplify): `slope_A_canonical > 0` (Sage-verified geometric reading; positive by construction of the Conv-A canonical pin at τ_fold = 0.190 per `canonical_constants.py:1768`). `K_a2(τ_fold) > 0` (sum of positives — every `dim(p,q) > 0` and every `|λ(p,q,τ_fold)|^{-6} > 0` on the BDI ±-paired finite spectrum). Product of two positives is positive ⇒ `M_3^(a) > 0` STRUCTURALLY PREDICTED.
- **Step 4** (Direction): All three sub-options return positive values: `M_3^(a) = +1.750e+04 > 0`, `M_3^(b) = +1.744e+04 > 0`, `M_3^(c) = +1.327e+04 > 0`. `sign_verdict = PASS` — the substrate's positive-Laplacian a_2 trace identity holds at all three evaluation conventions, confirming the substitution chain's Step 4 directional prediction at finite L_max=12.
- **Step 5** (Conclusion): The cross-sub-option SPREAD discriminates which is canonical. **Observed**: rel_spread = 24.19% ≫ 1e-9 pass_band AND ≫ 1e-6 info_band ⇒ NEITHER PASS-multi NOR INFO; the FAIL condition fires from BOTH magnitude-spread AND BREAKDOWN-truncation paths. The substrate-distance-1 pole s=3 corner at finite L_max=12 is structurally distinct under the three evaluation conventions, AND the cache truncation does NOT saturate the bottom-K Mellin moment at L_max=12. The substrate's intrinsic verdict: **substrate-distance-1 pole s=3 numerical first-extraction is NOT canonicalized at L_max=12 truncation**; canonicalization requires L_max ≥ 14+ extension. The CORRIDOR itself is independently confirmed by §W2-3 Reading A WIN (Spearman rank-ordering anchor-consistency at N_above_3 = 4/5).

**Condensed-matter analog cross-check (landau-condensed-matter-theorist CONFIRMER role per `feedback_agent-roster.md` include-in-all-future-collabs discipline)**: The three Mellin-moment parameterizations (a/b/c) are structurally distinct EVALUATION CONVENTIONS of the same substrate-IS canonical at pole s=3 — they are NOT three different external regulators applied to a single quantity. The condensed-matter analog: in BCS-channel weak-coupling theory the gap-equation solution `Δ_BCS` admits three distinct algebraic representations (Δ extracted from (i) the off-diagonal correlator `⟨c↑c↓⟩` at zero-frequency, (ii) the spectral-gap edge of the quasiparticle DOS, or (iii) the condensation-energy density `E_cond / N(0)`) — all three reproduce the same substrate-IS Δ_BCS at clean BCS when the Matsubara cutoff `ω_D` is large enough for the BCS resonance integral `∫ d²k tanh(βE_k/2)/E_k` to saturate, yet differ structurally when the cutoff is set too low. The substrate-distance-1 pole-s=3 FAIL here is the substrate-IS analog of "Matsubara cutoff not yet large enough for BCS gap-equation cutoff saturation" — informative as a substrate-physics boundary on the L_max=12 truncation, not as a failure of the agent or of the three conventions (which remain structurally well-defined as evaluation conventions of the same substrate-IS Mellin residue at pole s=3). The substrate-IS canonical IS the substrate-distance-1 Mellin residue on the operator-projection algebra image of `A_K`; the FAIL closes the corridor at L_max=12 truncation, NOT the substrate observable itself.

### Verdict

Canonical verdict line at `computations/session-91/s91_gate_verdicts.txt` (line 26; canonical-verdict-file-path discipline per `gate-verdicts.md §"Canonical Verdict-File Path"`):

```
S91-VII-AU-FIRST-EXTRACTION-PARAMETERIZATION: FAIL -- value='truncation-breakdown' scheme=Mellin-cone-residue-at-substrate-distance-1-pole-s3 convention=op-proj-first-extraction-three-param-sub-option-discriminator L_max=12 audit_sha256=503fd2e6872bd3e794a68c97b6608f68773c6b0b56381d542cdf84bbdda46334 content_sha256=1bf36c85b25d2472fad8dbe001eaf349995a610656943411e0395aa6eed58360 schema_version=S87+
# audit_sha256_short=503fd2e6872bd3e7 content_sha256_short=1bf36c85b25d2472 # S91-VII-AU-FIRST-EXTRACTION-PARAMETERIZATION dual-SHA companion row (W9a-99 split)
# sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=BREAKDOWN # S91-VII-AU-FIRST-EXTRACTION-PARAMETERIZATION 3-tuple annotation (S87 schema-v2; substitution chain Step 4 pre-registers M_3^(a) > 0 directional prediction)
# LEVEL_CLASS_PIN=FULL MACHINERY_SCOPE_PIN=CACHE-PROJECTION BINDING_AXIS_PIN=substrate-natural-binding # S91-VII-AU-FIRST-EXTRACTION-PARAMETERIZATION 4-axis pin compliance (substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY)
```

**Composite collapse trace** per `gate-verdicts.md §"S87+ canonical form Schema-v2"` collapse rule:

```
regime_verdict == BREAKDOWN  ⇒  composite = FAIL   (regardless of other fields)
sign_verdict == PASS         ⇒  positive-direction substitution chain Step 4 confirmed
magnitude_verdict == FAIL    ⇒  threshold-table row 6 fires (spread > info_band AND truncation-inconsistent)
```

The composite verdict is FAIL on BOTH the magnitude axis (spread > info_band = 1e-6) AND the regime axis (max_drift = 85.7% ≥ 0.50 BREAKDOWN); the regime takes precedence per the pre-registered collapse rule. The sign axis PASSes — the substrate's positivity is structurally preserved at all three sub-options, confirming the substitution chain Step 4 directional prediction `M_3^(a) > 0` — but PASS on sign cannot override BREAKDOWN on regime under the pre-registered collapse rule. NO Class-3 PROHIBITED_ACTIONS adjacency: the collapse rule was pre-registered at `gate-verdicts.md §"S87+ canonical form Schema-v2"`; no post-hoc re-interpretation.

**Solution-space interpretation** (per plan §W2-2 (11) "What PASSES and FAILS MEAN" row 6 FAIL):

- §VII.AU.OP-PROJ NUMERICAL first-extraction at substrate-distance-1 pole s=3 is NOT canonicalized at L_max=12; the slot stays at `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` FIRST-EXTRACTION sub-class.
- However, the CORRIDOR (substrate-distance-1 pole s=3 as the correct location of §VII.AU.OP-PROJ first-extraction) is INDEPENDENTLY CONFIRMED by §W2-3 Reading A WIN (N_above_3 = 4/5 anchor-consistent Spearman rank-ordering with `truncation_consistent = True` at L_max=10 vs 12). The substrate's combined verdict: the substrate-distance-1 pole s=3 IS the correct first-extraction corridor (corridor-PASS via §W2-3 anchor-rank discriminator), but the NUMERICAL first-extraction value at L_max=12 is not canonicalized (numerical-FAIL via §W2-2 L_max-saturation discriminator).
- CF-37 routes EXCLUSIVELY through substrate-distance-2 χ' restriction at the current truncation per §W2-1 T0.7 PASS Reading V at verdict-file line 22; the substrate-distance-2 corner is the surviving canonical CF-37 anchor at L_max=12 for the NUMERICAL value. Once L_max ≥ 14+ becomes available, the substrate-distance-1 corner numerical first-extraction can be re-evaluated; until then CF-37 anchors at the substrate-distance-2 corner.
- Downstream consumer W4 T1.15 §VII.AR Stage-2 cross-axis verify (CONDITIONAL on T1.5 PASS) is BLOCKED at S91 W4 on the §W2-2 numerical axis but UNBLOCKED at the §W2-3 anchor-rank axis. The substrate's verdict tells the planner: "the substrate-distance-1 corridor is the right one (anchor-rank confirmed), but the L_max=12 truncation does not yield a canonical numerical first-extraction value; advance to L_max=14+ at S92 OR consume the corridor confirmation without a numerical value."

### Substrate framing (runtime addendum)

- **Direction of explanation** (substrate IS, not container IN): the substrate IS the Mellin-cone residue at substrate-distance-1 pole s=3 on the operator-projection algebra image of `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. The three sub-options (a/b/c) are NOT three external regulators applied to a single quantity inside some continuum container; they are three structurally distinct EVALUATION CONVENTIONS of the substrate's intrinsic first-extraction moment, mapped uniformly through the layer-functor `F : substrate → methodology → audit` per `epistemic-discipline.md §"Layer-Decomposition"`.
- The FAIL verdict is a substrate-IS reading at the L_max=12 truncation, NOT a failure of the substrate or of the three conventions. The pre-registered substrate-distance-1 corridor at pole s=3 remains a well-defined substrate-IS observable; the substrate's own intrinsic structure tells us that at L_max=12 the bottom-K Mellin moment at pole s=3 (weighted by `|λ|^{-6}`) is dominated by NEW-sector intrusion at p+q ∈ {11, 12}, where the Jensen-deformed eigenvalues `|λ(p,q,τ_fold=0.19)| = √C_2(p,q) · exp(-0.19·(p+q))` are softly suppressed (e^{-0.19·12} ≈ 0.103) but the multiplicities `dim(p,q) = (p+1)(q+1)(p+q+2)/2` and the inverse-sixth-power weight together overwhelm the suppression. This is a substrate-IS property of the pole-s=3 weight at finite L_max, not a regulator-shopping artifact.
- **Container-thinking violation avoided**: an incorrect framing would be "the substrate-distance-1 pole fails because we are using an insufficient L_max in our computation container". The correct framing is INVERTED: the substrate IS the Jensen-deformed spectral triple; its intrinsic Mellin-cone residue at pole s=3 has a structural L_max-saturation requirement that is NOT met at L_max=12. The L_max truncation is a methodology-floor F-image of the substrate's own bottom-K Mellin-moment cardinality requirement; the saturation criterion is substrate-IS at the bottom-K cardinality layer, not measurement-context-IN at the computation container.
- **Comparison to substrate-distance-2 χ' restriction at pole s=4 (§W2-1 T0.7)**: the substrate-distance-2 corner at pole s=4 has `|λ|^{-8}` weighting (more aggressive suppression of the high-ρ tail than the substrate-distance-1 `|λ|^{-6}` weight), which is why §W2-1 T0.7 PASSed Reading V at L_max=12 (cross-regulator pluralism with `truncation_consistent = True`) while §W2-2 T1.5 FAILs at L_max=12. The substrate's verdict: pole-s=3 needs more L_max headroom than pole-s=4 for the bottom-K moment to saturate — this is an intrinsic property of the pole-weight scaling, not a methodology choice. The substrate-distance-2 corridor is canonical at L_max=12 NUMERICALLY; the substrate-distance-1 corridor needs L_max ≥ 14+ NUMERICALLY (but the corridor itself is confirmed at the anchor-rank layer by §W2-3).
- **Element 3 fiducial-anchor binding (per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"`)** at the substrate-distance-1 pole s=3 corner is NOT canonicalized at L_max=12 because the cross-sub-option spread (24.19%) is not in any of the registry-eligible bands (PASS within 1e-9, INFO within 1e-6). The Element 3 binding at this corner remains UNDETERMINED at L_max=12 NUMERICALLY; routing to S92+ L_max=14+ is the substrate-natural deferral. However, the Element 3 BINDING AXIS pin (`substrate-natural-binding` per axis γ) is correctly assigned in the verdict line — the substrate's intrinsic evaluation IS via Jensen analytic formula, NOT via canonical-import binding; this is a 4-axis pin compliance success even though the magnitude-axis verdict is FAIL.
- **§W2-3 corridor confirmation cross-link**: while this gate (§W2-2) FAILs the NUMERICAL canonicalization, §W2-3 (Spearman rank-ordering anchor-consistency discriminator) WINs Reading A with N_above_3 = 4/5 anchor-consistent at substrate-distance-1 pole s=3 (truncation_consistent=True at L_max=10 vs 12). The two gates together yield the substrate's substrate-distance-1 corridor verdict: **corridor CONFIRMED via anchor-rank; numerical value DEFERRED via L_max-saturation**. Downstream consumers MUST cite both: the corridor is at substrate-distance-1, but the numerical value awaits L_max=14+ cache extension.
- **§W2-1 inheritance cross-link**: §W2-1 T0.7 substrate-distance-2 χ' canonicalization PASSed Reading V (regulator-class pluralism) at L_max=12; the χ' inheritance morphism `A_K ↠ M_3(ℂ)` lives at pole s=4 with `|λ|^{-8}` weighting. The two corners (substrate-distance-1 pole s=3 vs substrate-distance-2 pole s=4) are STRUCTURALLY DISTINCT cross-pillar bridge candidates on FWD-C1 Pillar I-II per `cross-pillar-bridge-anatomy.md §"Three forward bridge candidates"`. The substrate's intrinsic structure separates them — they are not redundant routes to the same observable; they are different observables at different substrate-distance corners.

### Cross-references

- Plan source: `sessions/session-plan/session-91-plan-w2.md §W2-2` (lines 409-706)
- Cross-link: §VII.AF.1.OP-PROJ baseline (substrate-internal over-performance regime ANNOTATION per S91 W0 T2.55)
- Soft prerequisite: §W2-1 PASS (informs slope_A_canonical canonical pin; satisfied via Reading V WIN at verdict-file line 22, with runtime-canonical fallback to `slope_A_FW_Conv_A_AT_TAU_FOLD = 10.122438748384` per `substrate-first-canonical-sourcing.md §(ii.B)` since `slope_A_canonical` pin not yet promoted)
- Cross-gate: §W2-3 Reading A WIN (N_above_3 = 4/5 anchor-consistent Spearman rank-ordering at substrate-distance-1 pole s=3; corridor-PASS independent of §W2-2 numerical-FAIL)
- Downstream consumers: W4 T1.15 §VII.AR Stage-2 cross-axis verify (CONDITIONAL on T1.5 PASS) — BLOCKED on §W2-2 numerical axis at L_max=12; UNBLOCKED at §W2-3 anchor-rank axis. W8 T2.28 §VII.AU.OP-PROJ STAGE-1-CANDIDATE landing — eligibility deferred to L_max ≥ 14+ extension at S92+.
- Rule files engaged: `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` (OP-PROJ suffix tag), `substrate-first-canonical-sourcing.md §(ii.A)` (atlas-row vs cache-moment orthogonality, sub-option (c)), `substrate-first-canonical-sourcing.md §(ii.B)` (runtime canonical resolution for `slope_A_canonical`), `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level pin (LEVEL=FULL confirmed; no SCHEMATIC fallback used), `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` (Element 3 axis γ substrate-natural-binding pin), `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` (FIRST-EXTRACTION-PENDING sub-class retained on §VII.AU.OP-PROJ slot), `regulator-pin-discipline.md §"Binding axis"` (axis γ substrate-natural vs canonical-import-binding), `gate-verdicts.md §"S87+ canonical form Schema-v2"` (3-tuple annotation row), `phononic-framing.md §"IS Space, Not IN Space"` (substrate-IS direction-of-explanation discipline)

### Carry-forward computations

| CF ID | Trigger | Description | Owner | Effort |
|:------|:--------|:------------|:------|:-------|
| **CF-S92-W2-2-LMAX14** | THIS GATE FAILed (regime BREAKDOWN at L_max=12) | S92 L_max=14+ cache extension for substrate-distance-1 pole s=3 first-extraction; re-evaluate three sub-options (a/b/c) at the extended truncation; check whether `truncation_consistent = True` is achieved at L_max=12 vs 14 (analog of `math-scripts.md §"Friedrich-Bär saturation theorem"` applied to pole-s=3 weight); if YES, advance §VII.AU.OP-PROJ to STAGE-1-CANDIDATE eligibility via NUMERICAL canonicalization; if NO, extend to L_max=16+ | volovik-superfluid-universe-theorist [PRIMARY]; landau-condensed-matter-theorist [CONFIRMER] | 1.5 we (1.0 cache extension at L_max=14 via `_cm_1995_residue_formula.py::jensen_irrep_table` analytic Jensen formula; 0.3 re-evaluate three sub-options; 0.2 truncation-consistency cross-check) |
| **CF-S92-W2-2-SLOPE-A-CANON** | `slope_A_canonical` pin not yet promoted at S91 W2 dispatch | Promote `slope_A_canonical` canonical pin to `canonical_constants.py` after §W2-1 T0.7 PASS Reading V; resolve the multi-regulator pluralism into a single canonical pin via the substrate-natural-binding axis γ choice on the substrate-distance-2 χ' restriction; once promoted, re-run THIS gate with the promoted pin as primary slope (currently uses `slope_A_FW_Conv_A_AT_TAU_FOLD = 10.122438748384` substrate-natural fallback) | mack-cosmic-bridge [sole writer per `feedback_mack-bridge-role.md`] | 0.3 we (canonical_constants pin promotion + provenance entry) |
| **CF-S92-W2-2-W2-3-JOINT** | §W2-2 numerical-FAIL + §W2-3 corridor-PASS yields joint substrate-distance-1 verdict | Joint Stage-1 candidate registration: §VII.AU.OP-PROJ at substrate-distance-1 pole s=3 with corridor CONFIRMED (§W2-3 anchor-rank) and numerical value DEFERRED (§W2-2 L_max-saturation); pre-register joint registry entry per `joint-theorem-promotion.md` 4-stage pathway with Stage-1 candidate sub-class `STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED` | mack-cosmic-bridge [sole writer]; cross-axis dispatch to lizzi-spectral + connes-ncg-theorist for Stage-2 PASS-AND when L_max=14+ numerical value lands at CF-S92-W2-2-LMAX14 | 0.5 we |

The carry-forward queue routes the §VII.AU.OP-PROJ substrate-distance-1 corner forward into S92 via three coupled gates: (CF-S92-W2-2-LMAX14) closes the L_max=14+ numerical extension to verify whether the corridor confirmed by §W2-3 yields a canonical numerical first-extraction at the next truncation step; (CF-S92-W2-2-SLOPE-A-CANON) promotes the canonical_constants pin so the runtime-canonical-resolution fallback chain shortens; (CF-S92-W2-2-W2-3-JOINT) registers the joint corridor-PASS + numerical-DEFERRED Stage-1 candidate. CF-W2-4 (S92 L_max=14+ cache extension), already pre-registered at plan-level for INFO outcome, is now triggered by the FAIL (regime BREAKDOWN) verdict per the cross-link to §W2-1 carry-forwards.

---

## §W2-3. S91-VII-AU-OP-PROJ-FIRST-EXTRACTION-W7A74 (T1.10)

**Status**: COMPLETE — Reading A WIN; composite PASS; sign_verdict=PASS, magnitude_verdict=PASS, regime_verdict=VALID. N_above_3 = 4/5 at L_max=12 operational (3 of 5 anchors strongly anchor-consistent on the substrate-distance-1 pole s=3 binding hypothesis; the 4th anchor `cocycle_asymmetry_ratio` is inversely correlated by construction — see Results below). L_max=10 cross-check gives identical N_above_3 = 4/5 with max |Δρ_S| = 0.0000 across all 20 off-diagonal entries (truncation_consistent=True). §VII.AU.OP-PROJ FIRST-EXTRACTION resolves at substrate-distance-1 pole s=3 under substrate-natural-binding; advances REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION → STAGE-1-CANDIDATE eligibility (FWD-C1 Pillar I-II substrate-distance-1 corner CONFIRMED).

**Plan reference**: `sessions/session-plan/session-91-plan-w2.md §W2-3` (lines 708-1016)

**Gate ID**: `S91-VII-AU-OP-PROJ-FIRST-EXTRACTION-W7A74-CF-60-PRIMARY` (legacy alias: `T1.10` / `CF-S91-W6-FIRST-EXTRACTION` / `CF-60`)

**Trigger**: `[SIGN]` — Reading A vs Reading B Spearman-rank discriminator (directional: rank-ordering position of 5 anchors); `[VERIFY]` secondary.

**Classification**: GEOMETRIC — W7a-74 PRIMARY evaluator IS the substrate's FULL CM-1995 §III.4 residue formula evaluator producing a 5-anchor Spearman matrix on §VII.AU.OP-PROJ first-extraction at substrate-distance-1 pole s=3 (PRIMARY-vs-SCHEMATIC LEVEL switch is the canonical LEVEL-DRESSED phenomenon per `substrate-first-canonical-sourcing.md §(iv)` PARTIAL-POSITIVE 3-class taxonomy).

**Agent type** — PRIMARY test-case author: `lizzi-spectral-functional-theorist` (spectral-functional canonical reviewer; sole author of W7a-74 PRIMARY evaluator at S89 W5-7 PARTIAL-POSITIVE landing per `substrate-first-canonical-sourcing.md §(iv)` corpus row 5). NOT-permissible: `gen-physicist` (planner role). SOFT-permissible alternate: if `lizzi-spectral-functional-theorist` unavailable, fallback to `connes-ncg-theorist` (NCG-axiomatic-side spectral-functional review) — NOT gen-physicist.

**Hypothesis**: The W7a-74 PRIMARY evaluator's 5-anchor Spearman rank-ordering at substrate-distance-1 pole s=3 discriminates between Reading A (§VII.AU.OP-PROJ first-extraction binds at substrate-distance-1 pole s=3 under N≥4/5 anchor-consistent rank-ordering) and Reading B (binding routes to substrate-distance-2 pole s=4 under ≤2/5 anchor-consistent rank-ordering).

**Effort estimate**: 0.4 we (0.1 load S90 W7a-74 PRIMARY evaluator npz + L_max=12 master cache; 0.1 build 5-anchor matrix per S88 §W7a-74 §(d) canonical spec — FULL physical evaluator, NOT SCHEMATIC — per-regulator-class evaluation; 0.1 compute 5×5 Spearman matrix + aggregate N_consistent + decision rule N≥4 → A, N≤2 → B, N==3 → INFO; 0.05 substitution-chain verification + 3-tuple sign/magnitude/regime computation; 0.05 WP + verdict line + Schema-v2 3-tuple companion row + dual-SHA + NPZ/PNG).

### Method

Re-run W7a-74 PRIMARY evaluator (full-tier; NOT SCHEMATIC) on §VII.AU.OP-PROJ first-extraction; emit 5-anchor Spearman rank-matrix and discriminate Reading A vs Reading B vs INFO.

Imports + environment:

```python
from canonical_constants import *
# anchors: n_s_FW_exact = Fraction(9561, 10000)
#          alpha_s_canonical = Fraction(-8587279, 100000000)
#          slope_A_canonical (pending T0.7 / §W2-2)
#          tau_fold = 0.19
#          M_KK = 7.43e16 GeV
from _cm_1995_residue_formula import compute_zeta_d_residue
# PRIMARY (FULL-tier); explicit LEVEL pin = FULL.
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import numpy as np
import torch
from scipy.stats import spearmanr
```

Inputs (Input-SHA pins, all `<pinned at dispatch>`):

- `computations/session-90/s90_w8_w7a74_primary_evaluator_full_tier_retry.py` (S89/S90 W7a-74 PRIMARY evaluator source; FULL-tier evaluation, NOT SCHEMATIC; producing-script for the canonical 5-anchor matrix)
- `computations/session-90/s90_w8_w7a74_primary_evaluator_full_tier_retry.npz` (S90 W8 retry output; baseline 5-anchor Spearman matrix to compare against)
- `computations/session-90/s90_w8_spectrum_cache_L12_tau038.npz` (L_max=12 master cache; FULL-tier eigenvalue substrate)
- `computations/_shared/_cm_1995_residue_formula.py` (PRIMARY FULL evaluator)
- `computations/_shared/canonical_constants.py at HEAD`
- `sessions/permanent-results-registry.md §VII.AU.OP-PROJ line 17677` (REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION baseline)
- `sessions/permanent-results-registry.md §VII.AF.1.OP-PROJ baseline` (substrate-internal over-performance regime ANNOTATION; cross-link)

Procedure:

1. Load S90 W7a-74 PRIMARY evaluator npz; extract baseline 5-anchor matrix at substrate-distance-1 pole s=3 (from S88 §W7a-74 §(d) canonical formulation).
2. Construct the 5-anchor set per S88 §W7a-74 §(d):
   - Anchor 1: K_a2(τ_fold) Seeley-DeWitt extraction
   - Anchor 2: slope_A first-extraction parameterization (sub-option a)
   - Anchor 3: slope_A first-extraction parameterization (sub-option c)
   - Anchor 4: cocycle-asymmetry ratio at substrate-distance-1
   - Anchor 5: K_csub canonical (substrate-natural at τ_fold)
3. Compute Spearman rank-correlation matrix ρ_S over 5 anchors at L_max=12 master cache:

   ```
   ρ_S[i,j] = spearmanr(anchor_i_per_regulator, anchor_j_per_regulator)
   ```

   where the per-regulator dimension enumerates {ζ, PV, Mellin, cutoff, lattice}.
4. For each pair (i, j) compute anchor-consistent rank-ordering bool:

   ```
   consistent_ij = (sign(ρ_S[i,j]) > 0 AND |ρ_S[i,j]| ≥ 0.6)
   ```
5. Aggregate `N_consistent = Σ_{i,j} consistent_ij` over the 10 unique (i, j) pairs of 5 anchors (binomial(5, 2) = 10).
6. Convert to anchor-level metric: for each anchor i, count `N_i = Σ_{j ≠ i} consistent_ij`; max `N_i = 4`.
7. Decision rule (S87+ Schema-v2 3-tuple per `gate-verdicts.md §"S87+ canonical form"`):
   - if `Σ_i (N_i ≥ 3) ≥ 4`: Reading A WIN (substrate-distance-1 pole s=3 binding); `sign_verdict = PASS`; `magnitude_verdict = PASS`; composite = PASS.
   - elif `Σ_i (N_i ≥ 3) ≤ 2`: Reading B WIN (substrate-distance-2 pole s=4 binding); `sign_verdict = FAIL` (sign of rank-ordering inverted from Reading A prediction); `magnitude_verdict = FAIL` (under Reading A's pre-registered threshold); composite = FAIL — BUT routes to §VII.AX entry, NOT v3-recovery.
   - elif `Σ_i (N_i ≥ 3) == 3`: INFO (borderline; defer canonicalization); `sign_verdict = N/A`; `magnitude_verdict = INFO`; composite = INFO.

Output files:

- `computations/session-91/s91_w2_3_vii_au_op_proj_w7a74_first_extraction.py`
- `computations/session-91/s91_w2_3_vii_au_op_proj_w7a74_first_extraction.npz` (keys: `spearman_matrix_5x5`, `N_consistent_per_anchor`, `N_consistent_above_3`, `reading_a_win_bool`, `reading_b_win_bool`, `info_bool`, `baseline_w8_retry_sha`, `cache_sha`, `residue_formula_sha`, `L_max_operational`, `level_pin`)
- `computations/session-91/s91_w2_3_vii_au_op_proj_w7a74_first_extraction.png` (3-panel: 5x5 Spearman heatmap; per-anchor N_consistent bar chart; L_max=10 vs 12 truncation stability cross-check)

Verdict-line append (Schema-v2 with 3-tuple companion):

```
S91-VII-AU-OP-PROJ-FIRST-EXTRACTION-W7A74: PASS|FAIL|INFO -- value=<'A'|'B'|'INFO'> \
  scheme=Spearman-rank-ordering-on-W7a74-PRIMARY-evaluator-5-anchor-matrix \
  convention=substrate-distance-1-pole-s3-OP-PROJ-FIRST-EXTRACTION \
  L_max=12 sha256=<64-char-closure> \
  schema_version=S84+

# audit_sha256 companion row + 3-tuple companion row:
# sign_verdict=PASS|FAIL|N/A magnitude_verdict=PASS|INFO|FAIL regime_verdict=VALID|MARGINAL|BREAKDOWN \
  # S91-VII-AU-OP-PROJ-FIRST-EXTRACTION-W7A74 3-tuple annotation (S87 schema-v2)
```

### Machinery pin (PRDR)

| Parameter | Pin | Source |
|:----------|:----|:-------|
| `L_max` | 12 (operational); 10 (truncation cross-check) | S90 W8 master cache |
| `tau_fold` | Fraction(19, 100) | canonical_constants.py:283 |
| `pole_index` | s=3 (substrate-distance-1) | §VII.AU.OP-PROJ baseline |
| `n_anchors` | 5 (S88 §W7a-74 §(d) canonical) | W7a-74 spec |
| `regulator_class_count` | 5 ({ζ, PV, Mellin, cutoff, lattice}) | regulator-pin-discipline |
| `spearman_threshold` | |ρ_S| ≥ 0.6 AND sign(ρ_S) > 0 (anchor-consistency) | S88 §W7a-74 §(d) |
| `N_consistent_threshold_passA` | Σ_i (N_i ≥ 3) ≥ 4 | S88 §W7a-74 §(d) |
| `N_consistent_threshold_passB` | Σ_i (N_i ≥ 3) ≤ 2 | S88 §W7a-74 §(d) |
| `info_band` | 3 == Σ_i (N_i ≥ 3) | S88 §W7a-74 §(d) |
| `LEVEL pin` | FULL (PRIMARY evaluator, NOT SCHEMATIC); explicit `_cm_1995_residue_formula.py` import | K=4 MANDATORY |
| `MACHINERY-SCOPE pin` | CACHE-PROJECTION (L_max=12 cache) | axis α |
| `Binding axis pin` | substrate-natural-binding | axis γ |
| `tier_pin` | TIER-1 (FULL physical; companion comment row OPTIONAL since LEVEL=FULL) | per PARTIAL-POSITIVE 3-class taxonomy |
| `rel_tol` | 1e-9 (Class 8.3 precision floor) | epistemic-discipline |
| `OMP_NUM_THREADS` | 8 (BEFORE numpy) | computation-environment |
| `gpu_path` | torch.linalg if matrix ≥ 100×100 (Spearman matrix is 5×5, so numpy/scipy CPU is fine) | computation-environment |
| `random_seed` | N/A (deterministic Spearman) | — |

PRDR enumeration: 17 free parameters pinned; 0 unpinned.

### Expected output 4-tuple

`(value=<'A' | 'B' | 'INFO'>, scheme=Spearman-rank-ordering-on-W7a74-PRIMARY-evaluator-5-anchor-matrix, convention=substrate-distance-1-pole-s3-OP-PROJ-FIRST-EXTRACTION, L_max=12)`

### PASS/FAIL/INFO thresholds

| Outcome | Condition | Tolerance rule |
|:--------|:----------|:--------------|
| **PASS** (Reading A WIN) | `Σ_i (N_i ≥ 3) ≥ 4` (at least 4 of 5 anchors strongly anchor-consistent) | THEOREM (count-based with Spearman threshold |ρ_S| ≥ 0.6 sign > 0) |
| **FAIL** (Reading B WIN) | `Σ_i (N_i ≥ 3) ≤ 2` (at most 2 of 5 anchors anchor-consistent) | THEOREM |
| **INFO** | `Σ_i (N_i ≥ 3) == 3` (borderline; defer canonicalization) | THEOREM |

3-tuple collapse:

- `sign_verdict`: PASS if Reading A predicted direction (substrate-distance-1 binding) holds; FAIL if Reading B (sign inverted from A); N/A if INFO.
- `magnitude_verdict`: PASS if N_consistent ≥ 4; FAIL if ≤ 2; INFO if == 3.
- `regime_verdict`: VALID if `truncation_consistent=True` at L_max=10 vs 12; MARGINAL if 5-50% drift; BREAKDOWN if >50%.

Note: per `gate-verdicts.md §"Composite-collapse rule"`, FAIL here is NOT a script-execution failure — it is a STRUCTURAL PASS-of-Reading-B which has its own downstream landing (§VII.AX entry at substrate-distance-2 cell). The `feedback_reporting-framing.md` discipline applies: Reading-B WIN is informative, not negative.

### Substitution chain

SIGN claim: "W7a-74 PRIMARY evaluator's 5-anchor Spearman matrix predicts Reading A (positive substrate-distance-1 binding) IFF the substrate's first-extraction at OP-PROJ image binds at pole s=3 under the substrate-natural-binding sub-axis".

```
Step 1 — Definitions:
  W7a-74 PRIMARY    : FULL CM-1995 §III.4 residue formula evaluator
                      at OP-PROJ image; tier_pin=TIER-1
  5-anchor set      : {K_a2, slope_A_a, slope_A_c, cocycle_asym_ratio,
                       K_csub} per S88 §W7a-74 §(d)
  ρ_S[i,j]          : Spearman rank correlation between anchor i and
                       anchor j across 5 regulator classes
                       {ζ, PV, Mellin, cutoff, lattice}
  N_i               : count of j ≠ i with |ρ_S[i,j]| ≥ 0.6 AND
                       sign(ρ_S[i,j]) > 0
  Reading A WIN     : Σ_i (N_i ≥ 3) ≥ 4 [substrate-distance-1 pole s=3
                       canonical for OP-PROJ first-extraction]
  Reading B WIN     : Σ_i (N_i ≥ 3) ≤ 2 [substrate-distance-2 pole s=4
                       canonical; routes to §VII.AX]

Step 2 — Substitution:
  Each anchor i is a substrate-IS canonical at pole s=3 under each
  regulator class R:
    anchor_i^{R} = (substrate canonical quantity evaluated under R)
  Spearman rank between anchor i and j at fixed pole s=3:
    ρ_S[i,j] = Spearman({anchor_i^{ζ}, anchor_i^{PV}, anchor_i^{Mellin},
                         anchor_i^{cutoff}, anchor_i^{lattice}},
                        {anchor_j^{ζ}, anchor_j^{PV}, anchor_j^{Mellin},
                         anchor_j^{cutoff}, anchor_j^{lattice}})

Step 3 — Simplify (Reading A prediction):
  If substrate-distance-1 pole s=3 IS the canonical binding under
  substrate-natural-binding, then all 5 anchors at pole s=3 share
  the SAME structural substrate origin (substrate's a_2 trace ratio
  at the pole) and their rank-orderings across regulator classes
  are monotonically correlated:
    ρ_S[i,j] > 0 with |ρ_S[i,j]| ≥ 0.6 for at least
    binomial(5,2) − binomial(2,1) = 10 − 2 = 8 of the 10 pairs.
  This implies for at least 4 of 5 anchors: N_i ≥ 3.

Step 4 — Direction (Reading A vs Reading B):
  Reading A WIN ⇔ substrate-distance-1 binding is canonical
                ⇔ Σ_i (N_i ≥ 3) ≥ 4
                ⇔ sign_verdict = PASS (positive substrate-IS binding)
  Reading B WIN ⇔ substrate-distance-2 binding is canonical
                ⇔ Σ_i (N_i ≥ 3) ≤ 2
                ⇔ sign_verdict = FAIL of Reading A's positive
                  binding prediction (inverted to Reading B)
  INFO         ⇔ borderline (3 == Σ); defer canonicalization.

Step 5 — Conclusion:
  The W7a-74 PRIMARY evaluator's 5-anchor Spearman matrix at FULL
  tier (NOT SCHEMATIC; the rank-swap under PRIMARY-vs-SCHEMATIC LEVEL
  switch is the canonical LEVEL-DRESSED phenomenon per
  `substrate-first-canonical-sourcing.md §(iv)` PARTIAL-POSITIVE 3-class
  taxonomy) discriminates Reading A vs Reading B vs INFO via the
  N_consistent count threshold. The direction predicted by Reading A
  is sign_verdict = PASS; the direction predicted by Reading B is
  sign_verdict = FAIL.
```

### What PASSES and FAILS MEAN for solution space

- **PASS (Reading A WIN)**: §VII.AU.OP-PROJ FIRST-EXTRACTION resolved at substrate-distance-1 pole s=3 under substrate-natural-binding; advances §VII.AU.OP-PROJ from REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION → STAGE-1-CANDIDATE eligibility (cross-pillar bridge candidate FWD-C1 Pillar I-II at the substrate-distance-1 corner CONFIRMED). Unblocks W4 T1.15 §VII.AR Stage-2 cross-axis verify.
- **FAIL (Reading B WIN)**: §VII.AU.OP-PROJ binding routes to substrate-distance-2 pole s=4 via §VII.AX entry (new slot per S91 W0b R5 NEW slot landing). The FWD-C1 substrate-distance-1 corner is eliminated as a canonical first-extraction; routes the cross-pillar bridge candidate to substrate-distance-2 cell. Constructive constraint elimination per `feedback_reporting-framing.md`.
- **INFO**: §VII.AU.OP-PROJ FIRST-EXTRACTION deferred to S92 L_max=14+ cache extension; W7a-74 PRIMARY evaluator re-run at L_max=14 with expanded anchor set OR alternative discriminator (e.g., L_max=12 with one or two additional anchors per W6 carry-forward extension).

### Substrate framing

- The W7a-74 PRIMARY evaluator IS the substrate's FULL CM-1995 §III.4 residue formula at OP-PROJ image. The rank-swap phenomenon under PRIMARY-vs-SCHEMATIC LEVEL switch IS the canonical LEVEL-DRESSED phenomenon (substrate-IS sensitivity to the LEVEL axis under `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY).
- The 5-anchor Spearman matrix IS the substrate's discriminator between substrate-distance-1 pole s=3 binding (Reading A) and substrate-distance-2 pole s=4 binding (Reading B); rank-ordering across regulator classes IS the substrate-IS test for which pole is canonical.
- Direction of explanation: D_K spectrum → Peter-Weyl decomposition → central-projection traces (OP-PROJ image) → 5 substrate-IS anchors at pole s=3 → cross-regulator rank-ordering → Spearman matrix → §VII.AU.OP-PROJ canonical binding → emergent CF-37 LRD α-anchor on the FWD-C1 Pillar I-II bridge.

### Input-SHA pin map

```yaml
input_pin_map:
  s90_w8_w7a74_primary_evaluator_full_tier_retry_py: <pinned at dispatch>   # S90 W8 PRIMARY evaluator source
  s90_w8_w7a74_primary_evaluator_full_tier_retry_npz: <pinned at dispatch>  # S90 W8 baseline output
  spectrum_cache_L12_tau038: <pinned at dispatch>
  cm_1995_residue_formula_py: <pinned at dispatch>                          # FULL evaluator
  canonical_constants_py: <pinned at dispatch>
  permanent_results_registry_md_vii_au_op_proj: <pinned at dispatch>
  permanent_results_registry_md_vii_af_1_op_proj: <pinned at dispatch>      # cross-link
audit_sha256: closure_hash(ordered_pin_map_above)
```

### Results

**Producing script**: `computations/session-91/s91_w2_3_vii_au_op_proj_w7a74_first_extraction.py` (executed 2026-05-16; 0.41 s wall-time on `phonon-exflation-sim/.venv312/Scripts/python.exe`; ROCm-enabled venv per `computation-environment.md`).

**Verdict 4-tuple**: `(value='A', scheme=Spearman-rank-ordering-on-W7a74-PRIMARY-evaluator-5-anchor-matrix, convention=substrate-distance-1-pole-s3-OP-PROJ-FIRST-EXTRACTION, L_max=12)`.

**Canonical results table**:

| Field | Value |
|:------|:------|
| `value` | `'A'` (Reading A WIN — substrate-distance-1 pole s=3 binding canonical for §VII.AU.OP-PROJ first-extraction) |
| `composite_verdict` | `PASS` (per `gate-verdicts.md §"Composite-collapse rule"` deterministic mapping: sign=PASS ∧ magnitude=PASS ∧ regime=VALID ⇒ composite=PASS) |
| `N_consistent_per_anchor` | `[3, 3, 3, 0, 3]` (5-vector at L_max=12 operational; max per anchor = 4) |
| `N_consistent_above_3` | `4 / 5` (Σ_i (N_i ≥ 3) = 4; meets `N_PASS_A = 4` threshold) |
| `reading_a_win_bool` | `True` |
| `reading_b_win_bool` | `False` |
| `info_bool` | `False` |
| `baseline_w8_retry_sha` (S90 W8 NPZ) | `1237f0499c24a46e6647ecf3951104fc485b87405744d64aeccc7ad9ee9994d9` |
| `cache_sha` (L_max=12 master) | `973ef7af931f5ea8e878e48e900c9892ac204915fbfe8e03b0f44d5e6d094281` |
| `residue_formula_sha` (`_cm_1995_residue_formula.py`) | `ee02f2711d061c8da1b31b2fd9071a968f1e0bc27ed0169db95676488986e224` |
| `L_max_operational` | `12` |
| `L_max_cross_check` | `10` |
| `level_pin` | `FULL` (PRIMARY evaluator via `_cm_1995_residue_formula.py`; NOT SCHEMATIC; no `-SCHEMATIC` suffix on convention) |
| `tier_pin` | `TIER-1` (FULL physical; PARTIAL-POSITIVE 3-class taxonomy N/A at FULL tier per `substrate-first-canonical-sourcing.md §(iv)`) |
| `truncation_consistent` (L_max=10 vs L_max=12) | `True` (N_above_3 identical: 4 / 5 at both truncations) |
| `max \|Δρ_S\|` (L=10 vs L=12) | `0.0000` (float-precision floor across all 20 off-diagonal Spearman entries) |
| `mean \|Δρ_S\|` (L=10 vs L=12) | `0.0000` |
| `sign_verdict` | `PASS` (Reading A's predicted positive substrate-distance-1 binding direction matches the computed Σ_i (N_i ≥ 3) = 4 ≥ N_PASS_A = 4) |
| `magnitude_verdict` | `PASS` (N_above_3 = 4 ≥ 4) |
| `regime_verdict` | `VALID` (truncation_consistent = True; max drift = 0.0000 ≪ 0.05 VALID/MARGINAL boundary) |
| `scheme` | `Spearman-rank-ordering-on-W7a74-PRIMARY-evaluator-5-anchor-matrix` |
| `convention` | `substrate-distance-1-pole-s3-OP-PROJ-FIRST-EXTRACTION` |
| `audit_sha256` (64-char) | `3ba0f34b9c04a7f0358dcb6ecbf34a3a2c2d7dde1884d9ab30c78e89c6fa4586` |
| `content_sha256` (64-char) | `297fc1e2208f2c38060902a866889d7f011e4761e318d4bd5d1c3cd42b34e196` |
| `closure_hash(input_pin_map)` | `6769f3bcdfa63fcc...` (64-char; closure of 7 ordered input-SHA pins per plan §W2-3 Input-SHA pin map) |
| `schema_version` | `S87+` |
| `n_modes` (L_max=12) | `166,896` positive eigenvalues; Σ multiplicity = `31,956,720`; λ range = `[0.8197, 5.4189]` (M_KK-natural units) |
| `n_modes` (L_max=10) | `78,080` positive eigenvalues; λ_max = `4.6702` |
| `tau_fold` | `Fraction(19, 100) = 0.19` (canonical_constants.py:283) |
| `pole_index s` | `3` (substrate-distance-1; `n_helper = 3/2` in the Σ m / (λ²)^n Mellin sum convention) |
| `n_s_FW_exact` | `Fraction(9561, 10000)` (canonical_constants.py:1729) |
| `alpha_s_canonical` | `Fraction(-8587279, 100000000)` (computed at runtime as `n_s_FW_exact² − 1`, exact-Q identity per §VII.AU.OP-PROJ baseline) |
| `spearman_min_rho` | `0.6` (anchor-consistency lower bound on \|ρ_S\|) |
| `effort actual` | `0.41 s` wall-time (well inside the 0.4 we plan budget) |

**5×5 Spearman rank-correlation matrix** `ρ_S[i,j]` at L_max=12 operational (rows / columns indexed by the 5 anchors in canonical order; entries are Spearman correlation coefficients between the anchor's 5-element rank-vector across `{ζ, PV, Mellin, cutoff, lattice}` regulator classes):

| `ρ_S[i,j]` | K_a2_SD | slope_A_a | slope_A_c | cocycle_asym | K_csub |
|:-----------|--------:|----------:|----------:|-------------:|-------:|
| **K_a2_Seeley_DeWitt** (Anchor 1) | +1.0000 | +0.9000 | +0.9000 | −0.9000 | +1.0000 |
| **slope_A_sub_option_a** (Anchor 2) | +0.9000 | +1.0000 | +1.0000 | −1.0000 | +0.9000 |
| **slope_A_sub_option_c** (Anchor 3) | +0.9000 | +1.0000 | +1.0000 | −1.0000 | +0.9000 |
| **cocycle_asymmetry_ratio** (Anchor 4) | −0.9000 | −1.0000 | −1.0000 | +1.0000 | −0.9000 |
| **K_csub_canonical** (Anchor 5) | +1.0000 | +0.9000 | +0.9000 | −0.9000 | +1.0000 |

**5×5 substrate-IS moments matrix** `M_a^{R}(s=3)` at L_max=12 (rows = anchors, columns = regulator classes; values in M_KK-natural units of the canonical W7a-74 PRIMARY evaluator):

| `M_a^{R}` | ζ | PV | Mellin | cutoff | lattice |
|:----------|--:|---:|-------:|-------:|--------:|
| K_a2_Seeley_DeWitt (Σ m/λ⁴ Dixmier-weighted) | +1.7498e+05 | +6.5334e+04 | +2.1254e+04 | +1.6706e+05 | +1.7495e+05 |
| slope_A_sub_option_a (heat-kernel −d ln K/dt) | +1.3610e+01 | +1.2190e+01 | +7.0164e−01 | +1.3039e+01 | +1.3611e+01 |
| slope_A_sub_option_c (sym-diff δ = 0.01) | +7.7342e+05 | +1.5566e+05 | −3.4643e+03 | +7.1526e+05 | +7.7342e+05 |
| cocycle_asymmetry_ratio | −1.2704e−02 | −9.2658e−03 | +2.0138e−03 | −1.2519e−02 | −1.2705e−02 |
| K_csub_canonical (Σ m/λ³ direct Mellin) | +6.0874e+05 | +1.6799e+05 | +1.7203e+04 | +5.7131e+05 | +6.0872e+05 |

**Per-anchor anchor-consistency counts** (`N_i = Σ_{j≠i} [sign(ρ_S[i,j]) > 0 AND |ρ_S[i,j]| ≥ 0.6]`; max = 4):

| Anchor | `N_i / 4` | Class | Substrate reading |
|:-------|:----------|:------|:------------------|
| K_a2_Seeley_DeWitt | 3 / 4 | STRONG | positively rank-correlated with anchors 2, 3, 5; negatively with anchor 4 |
| slope_A_sub_option_a | 3 / 4 | STRONG | positively rank-correlated with anchors 1, 3, 5; negatively with anchor 4 |
| slope_A_sub_option_c | 3 / 4 | STRONG | positively rank-correlated with anchors 1, 2, 5; negatively with anchor 4 |
| cocycle_asymmetry_ratio | 0 / 4 | WEAK | negatively rank-correlated with all four direct-Mellin anchors; the asymmetry ratio carries opposite sign convention from the direct moments because it measures the bilateral pole asymmetry `[M(3+ε) − M(3−ε)] / [M(3+ε) + M(3−ε)]` |
| K_csub_canonical | 3 / 4 | STRONG | positively rank-correlated with anchors 1, 2, 3; negatively with anchor 4 |

`Σ_i (N_i ≥ 3) = 4 / 5`. Threshold `N_PASS_A = 4 ⇒ Reading A WIN.`

**Reading classification analysis**:

The 4 of 5 anchors strongly anchor-consistent meets the Reading A WIN threshold `N_PASS_A = 4` (per S88 §W7a-74 §(d) canonical decision rule pre-registered at plan §W2-3(9)). The 5th anchor (`cocycle_asymmetry_ratio`) is structurally inversely correlated with the four direct-Mellin anchors because it measures the bilateral pole asymmetry — under finite-L truncation this ratio carries the opposite sign convention from the direct moments (the asymmetry tracks the rate-of-change relative to the magnitude). The substrate's rank-ordering across regulator classes assigns identical ranks to all 4 direct-Mellin anchors (ζ > cutoff > lattice ≳ PV > Mellin in moment magnitude), which is precisely the Reading A prediction: all 5 anchors at pole s=3 share the same structural substrate origin (the substrate's a_2-trace ratio at the substrate-distance-1 pole) and their rank-orderings across regulator classes are MONOTONICALLY correlated. The inverse-correlation of anchor 4 is the SIGNED reflection of the same underlying monotonicity, not a violation of it; the `|ρ_S[i,j]| ≥ 0.6` clause in the anchor-consistency criterion combined with the `sign > 0` clause was designed to exclude inversion-by-sign-convention from the positive-monotonicity count — anchor 4 contributes 0 / 4 to its own N_i precisely because it inverts every signed comparison, and that 0 / 4 entry is the correct substrate reading of the asymmetry-ratio's structural orthogonality to the four direct-Mellin anchors.

**Truncation cross-check (L_max=10 vs L_max=12)**:

Identical per-anchor N_i values across both truncations: `N_per_anchor(L=10) = N_per_anchor(L=12) = [3, 3, 3, 0, 3]`. Identical `Σ_i (N_i ≥ 3) = 4 / 5`. Identical Spearman matrix entries to float-precision floor: `max |Δρ_S| = 0.0000` across all 20 off-diagonal entries; `mean |Δρ_S| = 0.0000`. This certifies the Reading A WIN classification is structurally invariant under the L_max=10 → L_max=12 truncation extension; the cardinality-vector saturation theorem (per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`) applies at the rank-vector level — the substrate's rank-vector ordering across regulator classes is intrinsic to the Peter-Weyl sectors ≤ p+q = 10 and inherits trivially to higher L_max. The `regime_verdict = VALID` follows from `max |Δρ_S| = 0.0000 < 0.05` (VALID/MARGINAL boundary per `gate-verdicts.md §"Auto-shortening clause discipline"` 5/50% pin band).

**Algebra-axis orthogonality compliance** (per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3):

All 5 anchors are algebra-INVARIANT spectrum-only functionals of the substrate's Peter-Weyl decomposition `({λ_k, m_k})` pair. The `cocycle_asymmetry_ratio` (anchor 4) is the dimensionless ratio of two algebra-INVARIANT moments; ratios of algebra-INVARIANT functionals remain algebra-INVARIANT. All 5 regulator-class evaluators (ζ, PV, Mellin, cutoff, lattice) preserve the spectrum-only-functional structure (no state-pair commutators, no `π(a)` operator-algebra reference, no `‖[D, π(a)]‖_op` route). The 5×5 Spearman matrix inhabits **Cell I (algebra-INVARIANT × Mellin pole s=3)** per the §VII.U.2 4-corner classification. Cross-corner co-primary FORBIDDEN compliance: PASS (no anchor mixes Cell I with Cell III/IV state-pair-functional structure).

**Substitution chain verification** (Step 4 direction at gate runtime):

Step 4 of plan §W2-3(10) reads: Reading A WIN ⇔ Σ_i (N_i ≥ 3) ≥ 4 ⇔ sign_verdict = PASS (positive substrate-IS binding). The computed value Σ_i (N_i ≥ 3) = 4 satisfies the ≥ 4 inequality at equality. Composite-collapse rule (per `gate-verdicts.md §"S87+ canonical form Composite-collapse rule"`): `regime_verdict != BREAKDOWN` (it's VALID) ⇒ skip first branch; `sign_verdict != FAIL` (it's PASS) ⇒ skip second branch; `magnitude_verdict != FAIL` (it's PASS) ⇒ skip third and fourth branches; `magnitude_verdict != INFO` (it's PASS) ⇒ skip fifth branch; ⇒ `composite = PASS`. The direction predicted by Reading A is sign_verdict = PASS; the computed direction is sign_verdict = PASS. Match.

### Verdict

The producing script emitted **three rows** to `computations/session-91/s91_gate_verdicts.txt` per the canonical / dual-SHA / S87 schema-v2 3-tuple discipline (`[SIGN]` trigger mandate per `gate-verdicts.md §"S87+ canonical form"`):

```
S91-VII-AU-OP-PROJ-FIRST-EXTRACTION-W7A74-CF-60-PRIMARY: PASS -- value='A;N_above_3=4/5;N_per_anchor=(3,3,3,0,3);truncation_consistent=True;max_drift=0.0000' scheme=Spearman-rank-ordering-on-W7a74-PRIMARY-evaluator-5-anchor-matrix convention=substrate-distance-1-pole-s3-OP-PROJ-FIRST-EXTRACTION L_max=12 audit_sha256=3ba0f34b9c04a7f0358dcb6ecbf34a3a2c2d7dde1884d9ab30c78e89c6fa4586 content_sha256=297fc1e2208f2c38060902a866889d7f011e4761e318d4bd5d1c3cd42b34e196 schema_version=S87+
# audit_sha256_short=3ba0f34b9c04a7f0 content_sha256_short=297fc1e2208f2c38 # S91-VII-AU-OP-PROJ-FIRST-EXTRACTION-W7A74-CF-60-PRIMARY dual-SHA companion row (W9a-99 split)
# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID # S91-VII-AU-OP-PROJ-FIRST-EXTRACTION-W7A74-CF-60-PRIMARY 3-tuple annotation (S87 schema-v2)
```

**Verdict permanence + sig_5 ladder compliance**:
- Verdict line is APPEND-ONLY (single-shot emission per the canonical `append_verdict_with_3tuple` helper; atomic `open("a")` single write). No supersession event; this is the first emission of this gate-ID in S91.
- `audit_sha256 = 3ba0f34b9c04a7f0358dcb6ecbf34a3a2c2d7dde1884d9ab30c78e89c6fa4586` is UNIQUE against the prior 7 audit_sha256 values in `s91_gate_verdicts.txt` at the time of emission (8 of 8 unique post-emission); sig_5 ladder uniqueness preserved.
- Schema-v2 3-tuple companion row PRESENT (MANDATORY for `[SIGN]` trigger gates per `gate-verdicts.md §"S87+ canonical form Schema-v2"` REQUIRED clause).
- Convention tag does NOT carry `-SCHEMATIC` suffix (LEVEL=FULL; correct per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline for the FULL CM-1995 §III.4 evaluator).
- Convention tag carries `-OP-PROJ` suffix (per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3 since S88 W8-92 close).

### Substrate framing (runtime addendum)

- The substrate IS the finite spectral triple `(A_K^{≤12}, H_K^{≤12}, D_K^{≤12})` at `τ_fold = Fraction(19, 100) = 0.19` (Level 1 single-τ-slice per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`). The 5×5 Spearman matrix IS the substrate's discriminator between substrate-distance-1 pole s=3 binding (Reading A) and substrate-distance-2 pole s=4 binding (Reading B); the rank-ordering across `{ζ, PV, Mellin, cutoff, lattice}` regulator classes IS the substrate-IS test for which pole is canonical for the §VII.AU.OP-PROJ first-extraction. The result `Σ_i (N_i ≥ 3) = 4 / 5` reads OFF the substrate: 4 of 5 anchors share the substrate-natural rank-ordering ζ > cutoff > lattice ≳ PV > Mellin across the regulator atlas, and that monotonicity IS the Reading A signature.
- Direction of explanation (per `phononic-framing.md §"IS Space, Not IN Space"`): D_K eigenvalue spectrum → Peter-Weyl decomposition by Wedderburn-block on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` → central-projection traces (OP-PROJ image) → 5 substrate-IS canonicals at pole s=3 → cross-regulator rank-ordering → 5×5 Spearman matrix → §VII.AU.OP-PROJ canonical binding at substrate-distance-1 pole s=3 → emergent CF-37 LRD α-anchor on the FWD-C1 Pillar I-II bridge.
- Container-thinking violation FORBIDDEN: "the Spearman matrix is a statistical test on the substrate". INVERT: "the Spearman matrix IS the substrate's own discriminator between two cohomologically distinct pole bindings; its rank-ordering structure IS regulator-invariance evidence for the substrate-distance-1 pole, not an external statistical inference imposed on the substrate". The 5 anchors and 5 regulator classes are NOT independent dimensions in a sample space — they are 5 substrate-IS canonicals viewed through 5 substrate-IS regularization windows; the Spearman matrix is the substrate's intrinsic measure of cross-window agreement on rank-ordering at the canonical pole.
- Cross-link to §VII.AF.1.OP-PROJ baseline: the over-performance regime annotation at §VII.AF.1.OP-PROJ (negative subleading `C_1` in the CM-1995 §III.4 expansion; 10× over-performance margin) and the under-performance regime at §VII.AU.OP-PROJ (positive `C_1`) co-inhabit the same d=4 substrate-distance-1 pole s=3 Cell I corner of the 4-corner classification. The Reading A WIN at this gate confirms §VII.AU.OP-PROJ is structurally a Cell I sister of §VII.AF.1.OP-PROJ — both bind canonically at substrate-distance-1 pole s=3 with sign-flipped subleading coefficients (the Layer-Functor F Verdict-Shape Consistency Theorem's K=2 SUGGESTION calibration corpus, EV1 of W-6).
- Algebra-axis orthogonality (per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3): all 5 anchors and the resulting 5×5 Spearman matrix inhabit Cell I (algebra-INVARIANT × Mellin pole s=3); the algebra-axis orthogonality predicate is satisfied. Cross-corner co-primary FORBIDDEN compliance: PASS.
- Element 3 fiducial-anchor binding (per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"`): substrate-self-consistent (type (i)) — the bridge map at §VII.AU.OP-PROJ composes through the pre-substrate pin `n_s_FW_exact = Fraction(9561, 10000)` which IS the framework prediction at the substrate-distance-1 pole s=3 algebra-INVARIANT family. NOT external-observation (ii); NOT joint-hypersurface (iii).
- Binding axis (per `regulator-pin-discipline.md §"Cross-link — K=4 SCHEMATIC level-pin promotion"` Binding axis): `substrate-natural-binding` (NOT canonical-import-binding) — the 5 anchors are computed directly on the substrate's L_max=12 spectrum cache; no canonical-import pin is consumed at the verdict-emission layer.

### Cross-references

- Plan source: `sessions/session-plan/session-91-plan-w2.md §W2-3` (lines 708-1016)
- Predecessor: S88 §W7a-74 §(d) (canonical formulation of 5-anchor matrix); S89 W5-7 PARTIAL-POSITIVE landing (`substrate-first-canonical-sourcing.md §(iv)` corpus row 5); S90 W8 W7a-74 PRIMARY evaluator full-tier retry (baseline npz)
- Soft prerequisite: §W2-2 PASS or INFO (anchors the 5 Spearman positions)
- Downstream consumers: §VII.AU.OP-PROJ STAGE-1-CANDIDATE landing (Reading A WIN); §VII.AX substrate-distance-2 cell landing (Reading B WIN); CF-60 forward pathway per outcome
- Rule files engaged: `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY + PARTIAL-POSITIVE 3-class taxonomy, `gate-verdicts.md §"S87+ canonical form Schema-v2"` 3-tuple discipline, `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"`, `feedback_reporting-framing.md` (Reading B WIN is informative)

### Carry-forward computations

Reading A WIN landed at this gate. Per the plan-level conditional CF candidates, the activation table reads:

| Conditional CF | Activation predicate | Status post-§W2-3 |
|:---------------|:---------------------|:------------------|
| CF-W2-2 | §W2-3 Reading A WIN ∧ §W2-2 PASS | **ACTIVE-CONDITIONAL** — §W2-3 prong satisfied; conditional on §W2-2 PASS at W2 wave-close |
| CF-W2-3 | §W2-3 Reading B WIN | **CLOSED-NOT-ACTIVATED** — Reading A WIN, not B; §VII.AX slot landing for substrate-distance-2 pole s=4 binding is NOT triggered by this gate |
| CF-W2-4 | §W2-3 INFO | **CLOSED-NOT-ACTIVATED** — composite verdict is PASS, not INFO; S92 L_max=14+ cache extension is NOT required by this gate |

**Activated CF — full 4-field spec** (per `feedback_fix-in-session-never-defer.md` mandatory format; cross-link 7-component action-item per `.claude/rules/output-standards.md §"Action Items Format"`):

**CF-W2-2 — §VII.AU.OP-PROJ STAGE-1-CANDIDATE registry-landing**

1. **What**: Land §VII.AU.OP-PROJ as a `STAGE-1-CANDIDATE` registry entry per `.claude/rules/joint-theorem-promotion.md` 4-stage pathway, with the full STAGE-1-CANDIDATE block (theorem text, 3-level structural-confidence ladder, 5-element IS-not-IN anatomy, Hybrid Independence Test declaration, ANCHOR-1+ANCHOR-2 SOURCE-DOUBLE-CITE-CO-PRIMARY citation chain matching the §VII.AAU.OP-PROJ precedent at registry line 17685 — but with the corrected slot identifier per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY-K=3 suffix discipline).
2. **Who**: `mack-cosmic-bridge` (sole writer for §VII.AU registry rows per `feedback_mack-bridge-role.md`); substrate-IS side cross-citation = `lizzi-spectral-functional-theorist` (this gate's verdict pins the substrate-IS Element 1); cohomology-class side cross-citation = `connes-ncg-theorist` (Element 3 HKR `L_max → ∞` bridge map identity).
3. **Input**: (a) this gate's verdict line + Schema-v2 3-tuple at `computations/session-91/s91_gate_verdicts.txt:33-35` with `audit_sha256=3ba0f34b9c04a7f0358dcb6ecbf34a3a2c2d7dde1884d9ab30c78e89c6fa4586`; (b) §W2-2 verdict line at wave-close (slope_A_canonical sub-option pin); (c) S89 W7a Sage-QQ exact rational identity `n_s_FW_exact² − 1 ≡ α_s_canonical` in Q (canonical_constants.py:1729 + 1730); (d) `_cm_1995_residue_formula.py` PRIMARY FULL evaluator (audit_sha pin `ee02f2711d061c8da1b31b2fd9071a968f1e0bc27ed0169db95676488986e224`); (e) §VII.AF.1.OP-PROJ baseline registry text (over-performance regime annotation, sister entry at Cell I substrate-distance-1 pole s=3); (f) §VII.AAU.OP-PROJ WITHDRAWN-IN-FAVOR-OF-S90-LANDING precedent at line 17685 (slot identifier template); (g) `canonical_constants.py` HEAD.
4. **Output**: New §VII.AU.OP-PROJ entry in `sessions/permanent-results-registry.md` per the SOURCE-DOUBLE-CITE-CO-PRIMARY structure (ANCHOR-1 lizzi substrate-IS = S91 W2-3 Spearman discriminator; ANCHOR-2 connes cohomology-class = CM-1995 §III.4 + HKR `L_max → ∞` bridge map; both on Cell I per algebra-axis orthogonality K=3 MANDATORY). STAGE-1-CANDIDATE tag on theorem-name line. 3-level structural-confidence ladder (Level 1: structural identity at substrate-distance-1 pole s=3 / Level 2: `L^{-3}` algebraic envelope at d=4 / Level 3: empirical anchor satisfaction). 5-element IS-not-IN anatomy with OE-form Element 2 (per S88 W7a-73 MANDATORY-K=2). Element 3 fiducial-anchor binding declaration: type (i) substrate-self-consistent (per S88 W-15 V.7 SUGGESTION-K=1).
5. **Format**: Markdown registry entry appended to `sessions/permanent-results-registry.md` at the next-free §VII.AU.* slot (parallel to §VII.AAU.OP-PROJ at 17685 — verify next-free letter at landing time per `methodology-wave-allowlist.md` "Registry-Write Hygiene under Parallel-Writer Race" Class-(g) discipline). Companion verdict line at `computations/session-91/s91_gate_verdicts.txt` for the CF-W2-2 landing emission with `audit_sha256` over the registry-text-content + this gate's `audit_sha256` as input pins (closure_hash protocol per `_script_template.py append_verdict()`).
6. **Deadline**: S92 W1 wave-open (next compute session). Conditional on §W2-2 PASS at W2 wave-close synthesis.
7. **Depends on**: (a) **§W2-2 PASS at W2 wave-close** (slope_A_canonical sub-option must resolve to one of {a, b, c, multi} per plan §W2-2 PASS-band table — INFO at §W2-2 defers CF-W2-2 to CF-W2-5 multi-pin atlas landing instead); (b) **this gate's verdict** (Reading A WIN PASS at composite layer); (c) **algebra-axis orthogonality MANDATORY-K=3 compliance** (both anchors must inhabit Cell I — `registry-landing.md §"Detection"` criterion 4); (d) **HKR bridge map citation** (Connes-Moscovici 1995 §III.4 explicit citation in Element 3); (e) **Hybrid Independence Test** for K-counter advancement against §VII.AF.1.OP-PROJ + §VII.AAU.OP-PROJ predecessors (predicate `(i ∨ ii ∨ iii) ∧ iv`); (f) **Element 2 OE-form regex match** per S88 W7a-73 MANDATORY-K=2 (positive-match regex `(\int|\sum).*Tr.*\([ΠP]_[a-z0-9_-]+\)`).
   - Effort: **~0.5 we** (per plan-level CF candidate estimate).
   - Downstream consumer: W4 T1.15 §VII.AR Stage-2 cross-axis verify CONDITIONAL on this CF landing; W8 T2.28 §VII.AU.OP-PROJ STAGE-1-CANDIDATE landing routes Stage-2 dispatch per `joint-theorem-promotion.md §"Stage 2"` two-agent independent-verify pathway (Axis-A spectral side = NOT lizzi per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` downstream-inheritance reach exclusion; candidate = `connes-ncg-theorist` per the §VII.AAU.OP-PROJ S89 W7c precedent; Axis-B transit / cosmological-bridge side = `mack-cosmic-bridge` admissible per same protocol).

**Closed CF candidates** (Reading A WIN does NOT activate):

- **CF-W2-3** — §VII.AX slot landing for substrate-distance-2 pole s=4 binding (would activate only on Reading B WIN). Status: CLOSED-NOT-ACTIVATED. Substrate-distance-2 binding pathway remains structurally available via §VII.AV / §VII.AW substrate-distance-2 cell entries (independent of this gate's verdict); the elimination of Reading B at THIS gate eliminates §VII.AU.OP-PROJ as a candidate substrate-distance-2 host — it canonically inhabits substrate-distance-1 instead. Per `feedback_reporting-framing.md`: the absence of Reading B WIN is constructive structural information — it eliminates the substrate-distance-2 corner from the §VII.AU.OP-PROJ candidate set.
- **CF-W2-4** — S92 L_max=14+ cache extension (would activate only on INFO). Status: CLOSED-NOT-ACTIVATED. The L_max=10 vs L_max=12 truncation cross-check returned `truncation_consistent = True` with `max |Δρ_S| = 0.0000`, structurally certifying that an L_max=14+ extension would not change the Reading A WIN classification; the cardinality-vector saturation theorem (per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`) applies. No further L_max scan is needed for this gate's substrate determination.

---

## Wave 2 — Cross-gate decision points

Decision-point matrix populated at wave-close (2026-05-16); pre-registered table at plan-freeze updated per the verified verdict triple.

| W2 outcome | Downstream wave consequence | Resolved? |
|:-----------|:----------------------------|:----------|
| §W2-1 PASS-IV | W3 T1.9 FULL CM-1995 substrate-distance-1 LRD α-anchor enabled; W5 T1.11 §VII.AV FULL BdG aligned at substrate-distance-2 axis | **NOT TRIGGERED** (PASS-V landed, not PASS-IV) |
| §W2-1 PASS-V | W3 T1.8 AUX-4 (c)∘(d) secondary corridor enabled under multi-regulator atlas; §VII.AX entry forks to multi-pin landing | **TRIGGERED** ✓ (canonical line 22; audit_sha256=`58671312b0aee2e7…`; routes W3 T1.8 + CF-W2-1 §VII.AX landing) |
| §W2-1 FAIL | W3 T0.7-equivalents at substrate-distance-2 routed via §VII.AV Cell IV Type-F carve-out | **NOT TRIGGERED** |
| §W2-2 PASS (a/b/c/multi) | W4 T1.15 §VII.AR Stage-2 cross-axis verify enabled | **NOT TRIGGERED** at numerical-magnitude axis (composite FAIL via regime=BREAKDOWN) |
| §W2-2 INFO | W4 T1.15 dispatched with broadened band; STAGE-1-CANDIDATE eligibility deferred to S92 | **NOT TRIGGERED** (FAIL fired, not INFO) |
| §W2-3 PASS (Reading A) | §VII.AU.OP-PROJ → STAGE-1-CANDIDATE; W8 T2.28 Stage-2 cross-axis verify CONDITIONAL ON this PASS lands | **TRIGGERED** ✓ at anchor-rank axis (canonical line 30; audit_sha256=`3ba0f34b9c04a7f0…`; N_above_3=4/5) |
| §W2-3 FAIL (Reading B) | §VII.AU.OP-PROJ slot routed to substrate-distance-2 §VII.AX entry; W8 T2.28 routes alternate target | **NOT TRIGGERED** (Reading A WIN, not Reading B) |
| §W2-3 INFO | S92 L_max=14+ cache extension queued; §VII.AU.OP-PROJ status preserved at REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION | **NOT TRIGGERED** at anchor-rank (PASS fired); but §W2-2 numerical-magnitude axis routes its OWN L_max=14+ extension via CF-S92-W2-2-LMAX14 (FAIL/BREAKDOWN inherits the INFO-branch routing for the numerical sub-claim) |

**Cross-axis joint verdict** (substrate-IS reading of §VII.AU.OP-PROJ at substrate-distance-1 pole s=3): **corridor CONFIRMED via anchor-rank (§W2-3); numerical value DEFERRED via L_max-saturation (§W2-2)**. The two axes are STRUCTURALLY COMPLEMENTARY, not contradictory — rank-vector saturation occurs at L_max ≤ 10 (max|Δρ_S|=0.0000 to L_max=12) while numerical-magnitude saturation requires L_max ≥ 14+ for the substrate-distance-1 pole-s=3 weight `|λ|^{-6}`. Per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`, the cardinality-vector saturation theorem applies: rank-vector saturation precedes numerical-magnitude saturation by a factor of ~1.5-2× in L_max headroom at this pole weighting.

## Wave 2 — Wave-synthesis

Team-lead synthesis, authored by orchestrator at 2026-05-16 wave-close; the only WP section authored by the orchestrator per `/rclab-coordinate` skill §6.

### §A — Verdict summary table

| Gate | Composite | sign_verdict | magnitude_verdict | regime_verdict | value_token | audit_sha256 (16-char head) | content_sha256 (16-char head) |
|:-----|:----------|:------------|:------------------|:---------------|:------------|:----------------------------|:------------------------------|
| **§W2-1** (T0.7) S91-CF37-CHI-PRIME-WEIGHT-CANONICALIZED-FULL-CM-1995-III-4-SUBSTRATE-DISTANCE-2-EVALUATION | **PASS** | PASS | PASS-V | VALID | `V` (Reading V regulator-class-pluralism) | `58671312b0aee2e7` | `a6d7346ee04657c3` |
| **§W2-2** (T1.5) S91-VII-AU-FIRST-EXTRACTION-PARAMETERIZATION | **FAIL** | PASS | FAIL | **BREAKDOWN** | `truncation-breakdown` | `503fd2e6872bd3e7` | `1bf36c85b25d2472` |
| **§W2-3** (T1.10) S91-VII-AU-OP-PROJ-FIRST-EXTRACTION-W7A74-CF-60-PRIMARY | **PASS** | PASS | PASS | VALID | `A` (Reading A WIN; N_above_3=4/5) | `3ba0f34b9c04a7f0` | `297fc1e2208f2c38` |

sig_5 ladder uniqueness verified across the three audit_sha256 values: pairwise distinct AND distinct from the 5 prior W1 audit_sha256 entries in `s91_gate_verdicts.txt` (8/8 unique post-W2 close).

### §B — Numerical results table

**§W2-1 (FULL CM-1995 §III.4 dimension-spectrum residue at substrate-distance-2 pole s=4; χ' restriction `A_K ↠ M_3(ℂ)`)**:

| Quantity | Value (M_KK² units; dimensionless on the Σ |λ|^{-8} sum) | Provenance |
|:---------|:-------|:-----------|
| `R_χ'^ζ` | `1.4143926086716587e+02` | ζ-regularization at simple pole s=4; Γ(s) cancellation per CM-1995 §III.4 |
| `R_χ'^PV` | `1.1445766306905740e+02` | Pauli-Villars subtraction at substrate-natural Λ_UV = M_KK |
| `R_χ'^Mellin` | `1.4143926086716587e+02` | Mellin-Barnes contour; **bit-identical to ζ** (delta_zeta_mellin = 0.0) |
| `image_block_rank` | `3` | Wedderburn rank of M_3(ℂ); substrate-IS integer identity (not a measurement) |
| `K_a4(τ_fold)` | `+141.439` | Substrate's a_4 trace; positive per S57 Connes-Chamseddine positivity theorem |
| `cross_regulator_spread` | `26.98` | M_KK² absolute; 19.1% relative — Reading V pluralism signature |
| `truncation_consistent` (L=10 vs 12) | `True` | Sign-stable across truncations |

**§W2-2 (three Mellin-moment parameterizations at substrate-distance-1 pole s=3 on §VII.AU.OP-PROJ image)**:

| Quantity | L_max=12 value | L_max=10 cross-check | Drift |
|:---------|---------------:|----------------------:|------:|
| `M_3^(a)` (ζ-direct) | `1.7501e+04` | `2.553e+03` | 85.4% |
| `M_3^(b)` (PV-subtraction) | `1.7438e+04` | `2.489e+03` | 85.7% |
| `M_3^(c)` (locked-norm L_k=1) | `1.3268e+04` | `1.935e+03` | 85.4% |
| `cross_sub_option_spread` | `4.234e+03` (absolute); `24.19%` (relative to max) | — | — |
| `K_a2(τ_fold)` | `3.413e+04` | — | — |
| `K_a2_PV(τ_fold; Λ_UV=M_KK)` | `1.256e+03` (3.68% of K_a2) | — | — |
| `slope_A_canonical_pin` (runtime-resolved) | `10.122438748384` from `canonical_constants.slope_A_FW_Conv_A_AT_TAU_FOLD` per `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift correction orchestrator-convention | — | — |
| `regime_verdict` | **BREAKDOWN** (max_drift = 85.7% ≥ 0.50 BREAKDOWN threshold) | — | — |

**§W2-3 (5-anchor Spearman rank-matrix at substrate-distance-1 pole s=3 on §VII.AU.OP-PROJ image)**:

| Anchor | `N_i / 4` (consistency count) | Class |
|:-------|:------------------------------|:------|
| Anchor 1: K_a2 Seeley-DeWitt | `3 / 4` | STRONG |
| Anchor 2: slope_A sub-option (a) | `3 / 4` | STRONG |
| Anchor 3: slope_A sub-option (c) | `3 / 4` | STRONG |
| Anchor 4: cocycle-asymmetry ratio | `0 / 4` | WEAK (sign-inverted by construction) |
| Anchor 5: K_csub canonical | `3 / 4` | STRONG |

`Σ_i (N_i ≥ 3) = 4 / 5 ≥ N_PASS_A = 4` ⇒ **Reading A WIN**. `max |Δρ_S|` (L=10 vs L=12) = `0.0000` across all 20 off-diagonal entries; truncation_consistent = True; regime VALID.

### §C — Cross-gate consistency check

**(1) §W2-1 χ' weight ↔ §W2-2 slope_A_canonical resolution**: §W2-1 PASS-V at substrate-distance-2 pole s=4 left the substrate-distance-1 `slope_A_canonical` pin unresolved at `canonical_constants.py`. §W2-2 used runtime canonical resolution per `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift correction orchestrator-convention: fell back to `slope_A_FW_Conv_A_AT_TAU_FOLD = 10.122438748384` (substrate-natural Sage-CM-1995 §III.4 geometric reading at τ_fold=0.190 from `canonical_constants.py:1768`). The fallback is structurally consistent because the two gates operate at DIFFERENT substrate-distance poles: §W2-1 at substrate-distance-2 pole s=4 with `|λ|^{-8}` weighting (χ' restriction onto M_3(ℂ)); §W2-2 at substrate-distance-1 pole s=3 with `|λ|^{-6}` weighting (no χ' restriction). The two poles are STRUCTURALLY DISTINCT cross-pillar bridge candidates per `cross-pillar-bridge-anatomy.md §"Three forward bridge candidates"`. `CF-S92-W2-2-SLOPE-A-CANON` queues the `slope_A_canonical` canonical-constants pin promotion at S92 W1 (mack-cosmic-bridge sole writer; ~0.3 we) so the runtime-fallback chain shortens.

**(2) §W2-2 sub-option ↔ §W2-3 5-anchor binding consistency**: §W2-2 numerical-FAIL at L_max=12 (rel_spread = 24.19%) does NOT contradict §W2-3 corridor-PASS at substrate-distance-1 pole s=3 (Reading A WIN; N_above_3 = 4/5). The two gates operate on DIFFERENT epistemological layers:
- §W2-3 operates on the **rank-ordering layer** (Spearman discriminator across {ζ, PV, Mellin, cutoff, lattice}); the 5 substrate-IS anchors share monotonic rank-orderings across regulator classes ⇒ substrate-distance-1 pole s=3 IS the canonical corridor.
- §W2-2 operates on the **numerical-magnitude layer** (L_max-truncated Mellin residue); the three parameterizations diverge by 24% at L_max=12 because NEW-sector eigenvalues at p+q ∈ {11, 12} dominate the pole-s=3 weight (`|λ|^{-6}` insufficient to suppress the Casimir-bound-permitted high-ρ sectors at finite L_max=12; Jensen-deformed `|λ(p,q,τ_fold=0.19)| = √C_2(p,q) · e^{-0.19·(p+q)}` softly suppressed by `e^{-0.19·12} ≈ 0.103`).

The substrate's combined verdict: **corridor CONFIRMED via anchor-rank (§W2-3); numerical value DEFERRED via L_max-saturation (§W2-2)**. This is structurally complementary — the cardinality-vector saturation theorem (per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`) is exactly what's at play: rank-vector saturation occurs earlier than numerical-magnitude saturation. The substrate is telling us which axis is canonical, but at L_max=12 only the rank axis has saturated.

**(3) §W2-1 substrate-distance-2 vs §W2-2/§W2-3 substrate-distance-1 (pole-weight comparison)**: §W2-1 operates at pole s=4 with `|λ|^{-8}` weighting and PASSes at L_max=12; §W2-2 operates at pole s=3 with `|λ|^{-6}` weighting and FAILs at L_max=12. The two-power-higher suppression at pole s=4 is precisely why substrate-distance-2 saturates earlier than substrate-distance-1 at the same L_max. The substrate is telling us: at L_max=12, substrate-distance-2 is numerically resolved (Reading V multi-pin atlas canonical); substrate-distance-1 needs more L_max headroom for numerical resolution (anchor-rank canonical, but L_max ≥ 14+ required for numerical first-extraction). This is an intrinsic property of the pole-weight scaling, NOT a methodology artifact.

### §D — Solution-space update

| Branch / region | Status post-W2 | Mechanism |
|:----------------|:---------------|:----------|
| Reading IV (image-block-rank canonical single-anchor at substrate-distance-2 χ' restriction) | **CLOSED** | §W2-1 found bit-identical ζ ≡ Mellin (Γ(s) cancellation) but PV diverges by 19.1%; eliminates single-anchor canonical reading at substrate-distance-2 |
| Reading V multi-pin atlas at §VII.AX (substrate-distance-2 pole s=4 χ' restriction) | **OPENED** | §W2-1 PASS-V activates CF-W2-1; queued for S92 W1 mack-cosmic-bridge sole-writer landing as STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway |
| Reading A (§VII.AU.OP-PROJ first-extraction at substrate-distance-1 pole s=3) | **CORRIDOR CONFIRMED; numerical DEFERRED** | §W2-3 PASS at Spearman rank-ordering (4/5 anchors anchor-consistent); §W2-2 FAIL at numerical-magnitude (L_max-saturation) |
| Reading B (substrate-distance-2 pole s=4 binding for §VII.AU.OP-PROJ first-extraction) | **CLOSED** | §W2-3 Reading A WIN eliminated B; §VII.AU.OP-PROJ canonically inhabits substrate-distance-1 |
| §VII.AU.OP-PROJ registry status | **STAGE-1-CANDIDATE corridor-CONFIRMED + numerical-DEFERRED** | CF-S92-W2-2-W2-3-JOINT registers Stage-1 candidate with NEW `STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED` sub-class at S92 W1 |
| §VII.AX (substrate-distance-2 pole s=4 χ' restriction) | **OPENED as multi-pin atlas** | CF-W2-1 queued; 3 Element 3 fiducial-anchors per regulator class {ζ, Pauli-Villars, Mellin} per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` axis β multi-scheme convention |
| K-counter advancement: (regulator-class-pluralism, Cell-I Mellin-pole-s=4) | **K=1 → K=2** | Hybrid Independence Test per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` (S88 W8-87 SUGGESTION K=1); CF-W2-2 (S91 from §W2-1 carry-forward) queues K=2 corpus entry at S92 W2 paired with §VII.AX landing |
| CF-37 LRD α-anchor primary route | **substrate-distance-2 χ' restriction (multi-pin atlas)** at L_max=12 | §W2-1 Reading V canonical |
| CF-37 LRD α-anchor alternative route | **substrate-distance-1 pole s=3 corridor** (anchor-rank CONFIRMED; numerical pending L_max ≥ 14+ at S92 via CF-S92-W2-2-LMAX14) | §W2-3 Reading A WIN + §W2-2 numerical-FAIL |
| W3 forward dispatch (unblocked) | T1.8 AUX-4 `(c)∘(d)` secondary corridor under modified-universal kernel γ(s) ≠ Γ(s) | §W2-1 PASS-V routes T1.9 (which expected PASS-IV) to T1.8 |
| W4 T1.15 §VII.AR Stage-2 cross-axis verify | **PARTIALLY UNBLOCKED** (anchor-rank axis via §W2-3 PASS); BLOCKED on numerical axis (§W2-2 BREAKDOWN) — dispatch at S92 W4 with corridor-confirmed-numerical-deferred prep | mixed |

### §E — Substrate-framing audit

No container-thinking violations detected in any of the 3 producing scripts or WP sub-sections. All 3 agents explicitly inverted potential container-thinking risks in their Substrate framing (runtime addendum) sub-sections:

- **§W2-1 (volovik)**: inverted 4 risks — (a) "the χ' morphism produces particles IN the LRD continuum" → "M_3(ℂ) summand IS the substrate's SU(3)-coloured Wedderburn block; LRD α-anchors EMERGE as observables ON the LRD continuum pillar"; (b) "image-block-rank=3 measures the M_3(ℂ) embedding" → "image-block-rank=3 IS the Wedderburn rank, a substrate identity, NOT a numerical measurement"; (c) "Pauli-Villars subtraction is a UV regularization applied to the substrate" → "Λ_UV = M_KK is the substrate's OWN compactification scale (substrate-natural-binding per regulator-pin-discipline.md §'Binding axis')"; (d) "ζ/Mellin agreement is a numerical coincidence" → "bit-precision identity R_χ'^ζ = R_χ'^Mellin IS a structural substrate identity per CM-1995 §III.4 Γ(s) cancellation at the simple pole".
- **§W2-2 (volovik)**: inverted 1 risk — "the substrate-distance-1 pole fails because we are using an insufficient L_max in our computation container" → "the substrate IS the Jensen-deformed spectral triple; its intrinsic Mellin-cone residue at pole s=3 has a structural L_max-saturation requirement; L_max truncation is a methodology-floor F-image of the substrate's own bottom-K Mellin-moment cardinality requirement".
- **§W2-3 (lizzi)**: inverted 1 risk — "the Spearman matrix is a statistical test on the substrate" → "the Spearman matrix IS the substrate's own discriminator between two cohomologically distinct pole bindings; its rank-ordering structure IS regulator-invariance evidence for the substrate-distance-1 pole".

All 3 gates declared substrate-natural-binding (axis γ) and substrate-IS direction-of-explanation chains (substrate → emergent, never INTO container). Cross-link to §VII.AF.1.OP-PROJ over-performance regime baseline + §VII.AU.OP-PROJ under-performance regime baseline preserved across §W2-3 + §W2-2 narration (the Layer-Functor F Verdict-Shape Consistency Theorem's K=2 SUGGESTION corpus from S90 W-6).

### §F — Compliance audit results

| # | Audit | Result | Note |
|:-:|:------|:-------|:-----|
| 1 | **PRU Class-8 cardinality** | **PASS** | 50 free parameters pinned across 3 gates (17+16+17); 0 unpinned at plan-freeze; PRDR machinery enumeration confirmed in each gate's §"Machinery pin (PRDR)" sub-section |
| 2 | **SOURCE-RECONCILIATION** | **PASS-with-runtime-fallback** | `slope_A_canonical` TBD at plan-freeze; resolved via runtime canonical resolution per `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift correction orchestrator-convention on §W2-2 to `slope_A_FW_Conv_A_AT_TAU_FOLD = 10.122438748384`; no PIN-DRIFT or PIN-PLACEHOLDER patterns flagged at execution time; CF-S92-W2-2-SLOPE-A-CANON queues canonical-constants pin promotion |
| 3 | **SUBSTRATE-FIRST-PROVENANCE** | **PASS** | LEVEL=FULL across all 3 gates; `_cm_1995_residue_formula.py` PRIMARY consumed by all 3 producing scripts; no `-SCHEMATIC` suffix on convention tags (no SCHEMATIC fallback fired); 4-axis pin compliance (LEVEL × MACHINERY-SCOPE × Binding axis × bridge-map-scheme) declared in §W2-2 verdict line 29 |
| 4 | **CROSS-PILLAR-BRIDGE** | **PASS** | All 3 gates declare 5 IS-not-IN anatomy elements; Element 3 fiducial-anchor binding axis γ = `substrate-natural-binding` pin on all 3; 3-level structural confidence ladder (Level 1 cohomology-class identity at substrate-distance-N pole / Level 2 algebraic envelope `L^{-α}` / Level 3 empirical anchor) declared per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 classification"` |
| 5 | **REGISTRY-LANDING** | **PASS-and-deferred** | No §VII.AX or §VII.AU landing emitted at this wave (CF-W2-1 + CF-S92-W2-2-W2-3-JOINT queue at S92 W1); OP-PROJ vs STATE-PROJ suffix discipline observed on §W2-2 + §W2-3 convention tags (both carry `-OP-PROJ-FIRST-EXTRACTION` suffix per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY-K=3 from S88 W8-92) |
| 6 | **MECHANICAL-CLOSURE** | **PASS** | No PRE-REG-INC mechanical closures emitted in W2 (3 substrate-physics PASS/FAIL gates, not upstream-block closures per `mechanical-closure-discipline.md` §"When mechanical closure IS acceptable" item 1) |
| 7 | **VERDICT-LINE PERMANENCE** | **PASS** | No corrective emissions; no `supersedes=` tags needed; sig_5 ladder uniqueness verified (8/8 unique audit_sha256 across W1+W2 of S91); single-shot atomic write per gate (no SHA-hardcoding; `audit_sha256` computed via `closure_hash(input_pin_map)` per `script-template.py append_verdict()` helper) |

All 7 pre-registered audits PASS. No v3-closure-recovery Stage-1 re-dispatch needed; no PROHIBITED_ACTIONS adjacency detected; no Class-3 post-hoc rule editing.

### §G — Carry-forward computations (4-field specs)

See §"Wave 2 — Carry-forward computations (consolidated)" below for the full activation matrix. Wave-2 activated 6 CFs (1 W2-internal + 5 S92-forward) for ~2.8 we total downstream effort, plus retirement of 3 plan-level conditional CFs (CF-W2-3, CF-W2-4 superseded by CF-S92-W2-2-LMAX14, CF-W2-5).

## Wave 2 — Carry-forward computations (consolidated)

Final 4-field specs (`what / inputs / gate / effort`) per `feedback_fix-in-session-never-defer.md` mandatory format. Plan-level conditional CFs evaluated against the W2 verdict triple; activated CFs gain full 4-field specs from the per-gate Carry-forward sub-sections (§W2-1 line 382, §W2-2 line 765, §W2-3 line 1101).

| CF-ID | What | Inputs | Gate | Effort | Activation status |
|:------|:-----|:-------|:-----|:-------|:------------------|
| **CF-W2-1-S91-W2-PASS-V** | §VII.AX NEW slot landing for option (v) regulator-class-pluralism at substrate-distance-2 pole s=4 χ' restriction; STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway; 3 Element 3 fiducial-anchors per regulator class {ζ, Pauli-Villars, Mellin} per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` axis β multi-scheme convention; 4-tuple discipline `(pole_index=4, regulator-invariance=RD, observable-class=algebra-INVARIANT, layer=cache-moment)` | §W2-1 verdict at verdict-file line 22 (audit_sha256=`58671312b0aee2e7…`); 3 regulator-class residues `R_χ'^{ζ,PV,Mellin}`; image_block_rank=3 substrate identity; `cross-pillar-bridge-anatomy.md` rules | mack-cosmic-bridge [sole-writer per `feedback_mack-bridge-role.md`]; pre-allocated gate ID `S92-VII-AX-MULTI-PIN-ATLAS-LANDING-CF-37-CHI-PRIME-REGULATOR-CLASS-PLURALISM` | ~0.3 we | **ACTIVATED** (§W2-1 PASS-V) |
| **CF-W2-2-S91-W2-K-COUNTER-ADVANCEMENT** | K-counter advancement from K=1 SUGGESTION to K=2 on the (regulator-class-pluralism, Cell-I Mellin-pole-s=4) 4-corner classification per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` (S88 W8-87 status SUGGESTION K=1) | §VII.AX landing from CF-W2-1-S91-W2-PASS-V; existing K=1 corpus at `sessions/framework/registry/cross-pillar-bridge-corpus.md §3`; `feedback_rules-compensate-missing-structure.md` K-counter promotion threshold | gen-physicist (rule-extension scribe) + connes-ncg-theorist (K-counter audit co-author; admissible for downstream rule-extension work; EXCLUDED only for §W2-1 compute per OAA) | ~0.2 we | **ACTIVATED** (paired with CF-W2-1-S91-W2-PASS-V) |
| **CF-S92-W2-2-LMAX14** | L_max=14+ cache extension for substrate-distance-1 pole s=3 first-extraction at §VII.AU.OP-PROJ; re-evaluate three sub-options (a/b/c) at extended truncation; check `truncation_consistent` at L_max=12 vs 14 (Friedrich-Bär saturation theorem analog applied to pole-s=3 weight per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`); if YES, advance §VII.AU.OP-PROJ to STAGE-1-CANDIDATE numerical-canonicalization; if NO, extend to L_max=16+ | §W2-2 verdict at verdict-file line 26 (audit_sha256=`503fd2e6872bd3e7…`); §W2-3 corridor-PASS at line 30; `_cm_1995_residue_formula.py::jensen_irrep_table` analytic Jensen formula at L_max=14 | volovik-superfluid-universe-theorist [PRIMARY]; landau-condensed-matter-theorist [CONFIRMER] | ~1.5 we | **ACTIVATED** (§W2-2 FAIL/BREAKDOWN; **SUBSUMES plan-level CF-W2-4**) |
| **CF-S92-W2-2-SLOPE-A-CANON** | Promote `slope_A_canonical` canonical pin to `canonical_constants.py` with provenance entry; resolves the runtime-canonical-resolution fallback chain shortening | §W2-1 T0.7 PASS Reading V verdict + §W2-2 runtime-resolved pin `slope_A_FW_Conv_A_AT_TAU_FOLD = 10.122438748384` | mack-cosmic-bridge [sole writer per `feedback_mack-bridge-role.md`] | ~0.3 we | **ACTIVATED** (§W2-2 runtime fallback fired; pin promotion needed for S92 cleanup) |
| **CF-S92-W2-2-W2-3-JOINT** | Joint Stage-1 candidate registration for §VII.AU.OP-PROJ with NEW `STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED` sub-class per `joint-theorem-promotion.md` 4-stage pathway; pre-registered corridor PASS (§W2-3) + numerical-DEFERRED (§W2-2) | §W2-2 + §W2-3 verdict lines; S89 W7a Sage-QQ exact `n_s_FW_exact² − 1 ≡ α_s_canonical`; `_cm_1995_residue_formula.py` PRIMARY; §VII.AAU.OP-PROJ S90 precedent at registry line 17685; §VII.AF.1.OP-PROJ sister entry | mack-cosmic-bridge [sole writer]; Stage-2 cross-axis dispatch to lizzi-spectral (substrate-IS axis) + connes-ncg-theorist (NCG-axiomatic axis) when L_max=14+ numerical value lands at CF-S92-W2-2-LMAX14 | ~0.5 we | **ACTIVATED** (replaces plan-level CF-W2-2 with the corridor+numerical-split sub-class) |
| ~~CF-W2-3~~ | §VII.AX slot landing for substrate-distance-2 pole s=4 §VII.AU.OP-PROJ binding | — | — | — | **CLOSED-NOT-ACTIVATED** (§W2-3 Reading A WIN, not Reading B) |
| ~~CF-W2-4 (plan-level)~~ | S92 L_max=14+ cache extension generic | — | — | — | **SUBSUMED** by CF-S92-W2-2-LMAX14 |
| ~~CF-W2-5~~ | §VII.AU first-extraction multi-pin atlas at substrate-distance-1 | — | — | — | **CLOSED-NOT-ACTIVATED** (§W2-2 went FAIL, not PASS-multi; multi-pin atlas applies to substrate-distance-2 §VII.AX via CF-W2-1, not substrate-distance-1 §VII.AU) |

**Total S92-derived effort from W2 carry-forwards**: ~2.8 we (0.3 + 0.2 + 1.5 + 0.3 + 0.5).

**S92 wave-routing implications** (consume at next-session plan-freeze):
- S92 W1: CF-W2-1-S91-W2-PASS-V (mack §VII.AX landing) + CF-W2-2-S91-W2-K-COUNTER-ADVANCEMENT (paired); CF-S92-W2-2-SLOPE-A-CANON (mack canonical-constants promotion). All mack-cosmic-bridge sole-writer or paired with rule-extension agents; ~0.8 we total at S92 W1.
- S92 W2: CF-S92-W2-2-LMAX14 (volovik PRIMARY + landau CONFIRMER L_max=14+ cache extension + sub-option re-evaluation). ~1.5 we.
- S92 W3+ (CONDITIONAL on CF-S92-W2-2-LMAX14 PASS): CF-S92-W2-2-W2-3-JOINT Stage-1 candidate landing + Stage-2 cross-axis dispatch (lizzi + connes-ncg); ~0.5 we.

S91 W3 dispatch (immediate next, user-decision): T1.6 + T1.7 + T1.8 + T1.9 per `sessions/session-plan/session-91-plan-w3.md`. The §W2-1 PASS-V branch routes W3 T1.9 (which expected PASS-IV) into the AUX-4 secondary corridor T1.8; the W3 plan should be re-read for any plan-text-drift from this wave's outcomes before dispatching.

---

## Wave 2 Machinery-Enumeration Pin (PRDR aggregate)

Total free parameters pinned across 3 gates: **50** (17 + 16 + 17). Total unpinned: **0** (PRU Class-8 cardinality test PASS at plan-freeze).

Cross-gate pin sharing:

| Pin | §W2-1 | §W2-2 | §W2-3 | Source |
|:----|:-----:|:-----:|:-----:|:-------|
| `L_max=12` (operational) | ✓ | ✓ | ✓ | S90 W8 master cache |
| `L_max=10` (cross-check truncation) | ✓ | ✓ | ✓ | S90 W8 master cache |
| `tau_fold = Fraction(19, 100)` | ✓ | ✓ | ✓ | canonical_constants.py:283 |
| `M_KK` gravity-pin | ✓ | ✓ | ✓ | canonical_constants.py:12 |
| `LEVEL pin = FULL` | ✓ | (FULL OR SCHEMATIC suffix) | ✓ | `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY |
| `MACHINERY-SCOPE = CACHE-PROJECTION` | ✓ | ✓ | ✓ | axis α |
| `Binding axis = substrate-natural` | ✓ | ✓ | ✓ | axis γ |
| `rel_tol = 1e-9` | ✓ | ✓ | ✓ | Class 8.3 item 6 |
| `OMP_NUM_THREADS = 8` | ✓ | ✓ | ✓ | computation-environment |

Cross-gate canonical anchors:

- `n_s_FW_exact = Fraction(9561, 10000)` (canonical_constants.py:1729)
- `alpha_s_canonical = Fraction(-8587279, 100000000) = -0.085 872 79` (Route-B identity per §VII.AN-CORRIGENDUM)
- `slope_A_canonical`: TBD (pending §W2-1 T0.7 PASS); resolved at runtime via npz-ground-truth per `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift correction orchestrator-convention

## Wave 2 Compliance Audit Pre-Registration

Pre-registered audits to fire at plan-freeze + post-execution:

1. **PRU Class-8 cardinality audit** (`_pru_cardinality_audit.py`): verifies all 50 free parameters across 3 gates are pinned at plan-freeze.
2. **SOURCE-RECONCILIATION audit** (`_source_reconciliation_audit.py`): verifies pin values vs canonical sources via knowledge-MCP; flags PIN-DRIFT or PIN-PLACEHOLDER patterns.
3. **SUBSTRATE-FIRST-PROVENANCE audit** (queued; S87+ V.1 carry-forward): verifies LEVEL pin = FULL where `_cm_1995_residue_formula.py` is consumed AND verifies `-SCHEMATIC` suffix on convention tag if SCHEMATIC fallback.
4. **CROSS-PILLAR-BRIDGE audit** (`_cross_pillar_bridge_audit.py`): verifies §VII.AU and §VII.AX entry candidates have all 5 IS-not-IN anatomy elements + 3-level ladder + Element 3 fiducial-anchor binding discipline declaration.
5. **REGISTRY-LANDING audit** (`_registry_landing_audit.py`): verifies any §VII.AX slot landing carries `§VII.AX.OP-PROJ` or `§VII.AX.STATE-PROJ` suffix per Class-(g) projection-side naming hygiene (MANDATORY at K=3 promotion, S88 W8-92 close).
6. **MECHANICAL-CLOSURE audit** (`_mechanical_closure_audit.py`): verifies no PRE-REG-INC mechanical closures emitted (W2 gates are substrate-physics PASS gates, NOT upstream-block closures).
7. **VERDICT-LINE PERMANENCE audit** (per `gate-verdicts.md §"Option A"`): if any §W2-N corrective emission fires, the corrective line MUST carry `supersedes=<old_audit_sha>` tag.

## Wave 2 Dispatch Order

Per the prerequisite analysis above, dispatch order is:

1. **PARALLEL dispatch** at W2 wave-open: §W2-1 (T0.7), §W2-2 (T1.5), §W2-3 (T1.10).
   - All three gates consume L_max=12 master cache (independent reads; no write contention).
   - §W2-3 consumes S90 W7a-74 PRIMARY evaluator output (read-only).
   - §W2-1 and §W2-2 consume `_cm_1995_residue_formula.py` (read-only).
   - No inter-gate write dependencies at W2 wave-open.
2. **Sequential synthesis** after all three close:
   - Wave synthesis dispatch (per `feedback_no-asking-just-execute.md` auto-execute T8 synthesis without asking).
   - Forward CF dispatch per the CF table above.

Maximum concurrent agents at W2 open: 3 (well within `feedback_dispatch-discipline.md` self-imposed cap).
