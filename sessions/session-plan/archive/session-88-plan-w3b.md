# Session 88 Plan — Wave 3b: 3He-B Inheritance Theorem + Chiral-Pair Multiplicity + chi_A Verification

> **Wave authorship**: planner-w3b (orchestrator-direct, connes-ncg-theorist orchestrator role).
> **Provenance**: split of stalled S88 W3 (planner-w3 timed out at full-wave authorship); W3a covers items 1-14 (NCG axiom + heat-kernel + spectral-action items); W3b (this file) covers items 15 / 20 / 28 (3He-B inheritance theorem rescue-class + chiral-pair multiplicity + chi_A direct verification); W3c covers items 16-19 + 21-27 + 29+ (remaining inheritance-falsifier-protocol gates).
> **Wave-class**: COMPUTE (all three gates are computation numerical verifications with pre-registered PASS/FAIL/INFO thresholds; per `.claude/rules/wave-classification.md` M1 fails ⇒ COMPUTE-class fallthrough).
> **Owner assignment**: connes-ncg-theorist PRIMARY for #15 (rescue-class theorem-side); volovik-superfluid-universe-theorist + connes-ncg-theorist JOINT for #20 (Peter-Weyl chiral-pair multiplicity + Casimir-derived f_67/f_88) and #28 (chi_A = 3/2 axisymmetric FS-average direct verification).

---

## Wave 3b Summary

This wave closes the substrate-physics half of the inheritance-morphism falsifier-protocol calibration corpus. Three independent gates land:

1. **§W3b-15** — Direct numerical verification at L_max=10 that the inheritance morphism `χ : A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ)` satisfies the rescue-class kernel-degenerate-escape (KDE) condition. Two sub-tests: (i) spec(D_K) at τ_fold has no zero eigenvalues (substrate-physics vacuous-PASS clearing the kernel-degeneracy obstruction); (ii) the M_3(ℂ) block of A_K maps to zero in M_2(ℂ) at machine precision under χ_*. Both at L_max ∈ {10, 11, 12} with L^{-3} algebraic envelope per cross-pillar-bridge-anatomy.md Level 2 d=4 calibration.

2. **§W3b-20** — Two-part substrate-physics derivation of the chiral-pair multiplicity ratio. Part D-A: closed-form `f_67/f_88` derivation from SU(3) Casimir on the (λ_6, λ_7) off-diagonal chiral-pair sub-block vs the λ_8 angular-diagonal sub-block, anchored in inheritance-falsifier-protocol.md first principles. Part D-B: full Peter-Weyl character evaluation `χ_67(p,q)` and `χ_88(p,q)` at p+q ≤ 10. Combined verdict: substrate-derived rank-2 cohomology-asymmetry ratio prediction at lab-side under the Class-B Gate-2 0.1% band, target value `7.324992` (W-5 Sage-exact).

3. **§W3b-28** — Independent direct numerical verification of `χ_A = 3/2` per Volovik 2003 §3.4 axisymmetric A-phase Fermi-surface average `⟨|Δ_A(k)|²⟩_FS`. This closes the substrate provenance of the chiral correction factor used in the (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5).

The wave is structurally tight: items #15 and #20 jointly close the §VII.AF.1 cross-pillar bridge's empirical anchor at L_max=10; item #28 closes the substrate-anchor for the lab-conversion-factor cancellation theorem invoked by every inheritance-falsifier-protocol Class-B gate.

### Wave classification (per `.claude/rules/wave-classification.md`)

- **M1 test**: PASS predicate is numerical comparison against pre-registered tolerance bands (e.g., `|χ_A − 3/2| < 1e-12`, ratio in `[7.3177, 7.3323]`, M_3(ℂ) image Frobenius norm `< 1e-12`). M1 FAILS the methodology-class test → COMPUTE-class.
- **M2 test**: Producing operations are `.py` scripts with eigenvalue computations + linear-algebra reductions + Casimir contractions. M2 FAILS methodology-class.
- **M3 test**: Source is substrate-first first-principles derivation (Casimir contractions + Peter-Weyl evaluations), NOT verbatim sub-diff from a closed workshop. M3 FAILS methodology-class.
- **M4 test**: Gate-IDs not in `methodology-wave-allowlist.md`. M4 FAILS methodology-class.

All four tests fail the methodology-class conjunction → wave is unambiguously COMPUTE-class.

---

## Wave 3b Decision Point Prerequisites

The three W3b gates depend on the following upstream artifacts, all of which are PASS-pinned at S87 close:

| Prerequisite | Source artifact | Status at W3b-dispatch | Failure consequence |
|:-------------|:----------------|:-----------------------|:--------------------|
| L=12 master spectrum cache | `computations/s84_spectrum_cache_L12_tau019.npz` (SHA `9e6d9cf7fd6a6949...`) | PASS-pinned (S84 W3) | All three gates HARD-HALT; cache regen carry-forward |
| W-5 cocycle norms | `cocycle_norm_phi67 = 0.793346 M_KK²`, `cocycle_norm_phi88 = 0.108307 M_KK²` (S86 W-5 §VII.AF.1) | PASS-pinned (S86 W-5 DONE-5) | #20 D-A FAILs without substrate anchor |
| W-5 Sage-exact ratio | `substrate_cocycle_ratio_67_88 = 7.324992` (canonical_constants.py) | PASS-pinned (S86 W-5 W11-C5 calibration) | #20 D-A FAILs against tolerance band |
| A_F SINGLETON theorem | A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) (S84 W8-87b) | PASS-pinned (KO-dim=6 derived) | #15 STRUCTURAL FAIL (algebra mis-specified) |
| Inheritance morphism χ definition | `χ : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ)` with M_3(ℂ) → 0 (`.claude/rules/inheritance-falsifier-protocol.md`) | PASS-pinned (S86 W-5 RULE-3) | #15 SCHEMA-MISSING (HARD-HALT) |
| (Δ_B/Δ_A)^p cancellation theorem | S86 W-5 DONE-5 machine-precision residual 0.0e+00 | PASS-pinned | #28 useless without cancellation-theorem applicability |
| Volovik 2003 §3.4 axisymmetric A-phase FS-average formula | Volovik 2003 monograph §3.4 (researchers/Volovik/) | PASS-pinned (heritage citation) | #28 STRUCTURAL FAIL (definition missing) |
| canonical_constants.py imports | `from canonical_constants import *` mandatory per `.claude/rules/math-scripts.md` | PASS-pinned | All three gates HARD-HALT |

All prerequisites are upstream-PASS at W3b-dispatch; no W3b gate is structurally blocked by upstream-FAIL.

---

## §W3b-15. S88-CHI-INHERITANCE-OF-KERNEL-DEGENERATE-ESCAPE-COMPLETE

### 1. What

Numerical verification at L_max ∈ {10, 11, 12} that the inheritance morphism `χ : A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ)` satisfies the rescue-class kernel-degenerate-escape (KDE) condition, completing the substrate provenance of the §VII.AF.1 cross-pillar bridge theorem.

Two sub-tests:

- **Sub-test A (kernel-degeneracy clearance)**: spec(D_K) at τ_fold = 0.190 has no zero eigenvalues (i.e., D_K is invertible on H_K^{≤L_max}). This is the substrate-physics vacuous-PASS condition: if D_K had a zero eigenvalue, the inheritance morphism would carry that eigenmode into M_2(ℂ) and the KDE rescue would fail by kernel-collision. Threshold: `|λ|_min(L_max) > 0.01 / r(τ_fold)` (canonical Casimir-floor).
- **Sub-test B (M_3(ℂ) block χ-killing)**: the M_3(ℂ) sub-block of the A_K representation is mapped to zero in M_2(ℂ) under χ_*. Concretely, for the canonical 8-dim M_3(ℂ) generator basis `{T_a}_{a=1..8}` (Gell-Mann), evaluate `‖χ_*(N_lift(T_a))‖_F` and verify all 8 norms are below 1e-12. This is the rescue-class theorem-side requirement: A_F admits Frobenius division-algebra blocks {ℝ,ℂ,ℍ} (which inherit) OR the matrix block must be χ-killed (M_3(ℂ) annihilated).

### 2. Why (substrate-physics rationale)

The inheritance-falsifier-protocol.md rule requires that `ker(ι_*)` be characterized for any rank-2 inheritance morphism. Item #15 establishes the KERNEL itself: M_3(ℂ) is in `ker(χ_*)` by construction (the inheritance morphism's defining datum), and the cocycles φ_67 + φ_88 living on the (λ_6, λ_7) chiral-pair + λ_8 angular-diagonal sub-blocks of M_3(ℂ) are therefore in `ker(χ_*)` rank-wise. This is the rescue-class theorem (a0-r-protection workshop CF-C): A_F's structural composition forbids matrix-block inheritance into the BdG sector M_2(ℂ) UNLESS the matrix block is annihilated by χ_*. Sub-test B is the direct numerical verification of this annihilation; Sub-test A is the auxiliary clearance that the kernel itself is rank-clean (no D_K zero eigenvalues collapsing the rank-counting).

The substrate-physics interpretation: phononic excitations of the M_3(ℂ) gauge sector (color SU(3)) are CONFINED in the laboratory image at the BdG sector — they cannot escape into the BdG band structure as quasiparticle modes. The cocycles φ_67 + φ_88 carry the substrate's color-sector content; their lab images vanish identically under χ_* (the kernel-degenerate escape).

### 3. Method (substrate-first)

```
Step 1: Load s84_spectrum_cache_L12_tau019.npz (SHA-pinned).
Step 2: For each L_max in {10, 11, 12}:
        a. Filter cache to bottom-K eigenvalues of D_K(τ_fold) at p+q ≤ L_max.
        b. Sub-test A: compute |λ|_min = min_k |λ_k|; verify > 0.01 / r(τ_fold).
        c. Sub-test B:
           - Construct A_F generator basis: {1_C, e_R, e_L, σ_1, σ_2, σ_3, T_1, ..., T_8}.
             (4 ℂ-block + 4 ℍ-block + 8 M_3(ℂ)-block generators)
           - Lift each generator to H_K via Peter-Weyl decomposition under canonical embedding.
           - Apply inheritance morphism χ_*: M_3(ℂ) generators map to 0 in M_2(ℂ); ℂ + ℍ generators
             map to canonical embedding ℂ⊕ℍ ↪ M_2(ℂ) (per S86 W-5 RULE-3 inheritance protocol).
           - Compute ‖χ_*(N_lift(T_a))‖_F for a = 1..8.
           - Verify all 8 Frobenius norms < 1e-12.
Step 3: Cross-validate L^{-3} algebraic envelope:
        - Compute |verdict(L) − verdict(L_max=12)| at L ∈ {10, 11}; verify scaling ≤ C · L^{-3}
          for C ≤ 10.0 (cross-pillar-bridge-anatomy.md Level 2 envelope at d=4).
Step 4: Emit dual-SHA verdict line per .claude/rules/gate-verdicts.md schema_version=S84+.
```

### 4. PASS / FAIL / INFO criteria (pre-registered)

- **PASS** (Sub-test A AND Sub-test B AND L^{-3} envelope all pass):
  - Sub-test A: `|λ|_min(L_max=10) > 0.01 / r(0.190)` (numerical floor; r(0.190) ≈ 0.5 ⇒ floor 0.02 in M_KK units)
  - Sub-test B: `max_a ‖χ_*(N_lift(T_a))‖_F < 1e-12` for a ∈ {1, ..., 8}
  - L^{-3} envelope: `|max_norm(L) − max_norm(12)| < 10.0 · L^{-3}` for L ∈ {10, 11}
- **FAIL** (any sub-test exceeds threshold): structural rescue-class theorem fails; A_F admits an inheritance pathway not anticipated; route to next-session NEEDS-INVESTIGATION carry-forward with diagnostic.
- **INFO** (Sub-tests pass but L^{-3} envelope marginal at 10.0 < scaling-constant ≤ 50.0): rescue-class holds but algebraic envelope wider than d=4 anchor; route to S89 envelope-tightening carry-forward.

### 5. Output artifacts

- `computations/s88_w3b_chi_inheritance_kde_complete.py` — producing script (~400-500 lines, full sub-test A + sub-test B + envelope cross-check)
- `computations/s88_w3b_chi_inheritance_kde_complete.npz` — keys: `lambda_min_per_Lmax`, `chi_image_norms_M3_per_Lmax`, `chi_image_norms_C_per_Lmax`, `chi_image_norms_H_per_Lmax`, `envelope_residuals`, `verdict_per_subtest`, `verdict_combined`
- `computations/s88_w3b_chi_inheritance_kde_complete.png` — 3-panel figure: (left) `|λ|_min` vs L_max; (center) bar plot of `‖χ_*(T_a)‖_F` for a=1..8 at L_max=10; (right) L^{-3} envelope log-log plot
- Verdict line in `computations/s88_gate_verdicts.txt` per dual-SHA schema

### 6. Machinery pin (PRDR enumeration)

```
L_max_set                 = (10, 11, 12)             # plan-pinned
tau_fold                  = canonical_constants.tau_fold  # = 0.190
A_F_algebra               = "C+H+M3C"                # S84 W8-87b SINGLETON
A_F_generator_basis       = "Gell-Mann_for_M3C_+_Pauli_for_H_+_canonical_for_C"
chi_inheritance_morphism  = "M3C_to_zero_C_and_H_to_canonical_M2C"  # S86 W-5 RULE-3
zero_eigenvalue_floor     = 0.01 / r_tau(0.190)      # = 0.02 (M_KK units)
chi_image_norm_threshold  = 1e-12                    # Frobenius norm
envelope_constant_PASS    = 10.0                     # d=4 anchor
envelope_constant_INFO    = 50.0                     # widened band
spectrum_cache_path       = "s84_spectrum_cache_L12_tau019.npz"
spectrum_cache_sha        = "9e6d9cf7fd6a6949..."    # input-pin SHA
schema_version            = "S84+"
```

### 7. Depends on

- `computations/s84_spectrum_cache_L12_tau019.npz` (UPSTREAM CACHE; SHA `9e6d9cf7fd6a6949...`)
- `canonical_constants.py`: `tau_fold`, `M_KK`, `r_tau`, `cocycle_norm_phi67`, `cocycle_norm_phi88`
- A_F SINGLETON theorem (S84 W8-87b registry entry)
- Inheritance morphism χ definition (`.claude/rules/inheritance-falsifier-protocol.md`)
- Cross-pillar-bridge-anatomy.md L^{-3} d=4 envelope (Level 2)

### 8. Owner

connes-ncg-theorist PRIMARY (rescue-class theorem-side; A_F SINGLETON + inheritance morphism + KO-dim=6 axiomatic provenance)

### 9. Effort estimate

~1.0 wave-equivalents (single-script, three sub-tests share same eigvec-basis loading infrastructure)

### 10. Verdict source

`computations/s88_gate_verdicts.txt` (dual-SHA per `.claude/rules/gate-verdicts.md` schema_version=S84+)

### 11. Working-paper section

`sessions/archive/session-88/session-88-results-workingpaper.md §W3b-15` — substantive content (≥15 lines per `.claude/rules/agent-standards.md` Completion Verification): sub-test A interpretation + sub-test B interpretation + cross-validation against §VII.AF.1 cross-pillar bridge entry + substrate-framing paragraph + L^{-3} envelope cross-check vs Level-2 anchor.

### 12. Plan-freeze SHA pin

`sha256_of_plan_block(W3b-15) = pending` (computed at plan-freeze; recorded in §"Wave 3b Input-SHA Ledger" below)

### 13. Carry-forward conditions

- **PASS**: §VII.AF.1 cross-pillar bridge empirical anchor at L_max=10 strengthened by Sub-test B Frobenius-norm direct measurement; KDE rescue-class theorem promoted from STAGE-1-CANDIDATE to STAGE-3-PERMANENT (per `.claude/rules/joint-theorem-promotion.md`) once Stage-2 cross-axis verify lands at S89.
- **FAIL**: NEEDS-INVESTIGATION carry-forward `S89-CHI-INHERITANCE-KDE-FAIL-INVESTIGATION` with diagnostic on which sub-test failed + which generator (a ∈ {1..8}) violated the M_3(ℂ) annihilation.
- **INFO** (envelope marginal): carry-forward `S89-KDE-ENVELOPE-TIGHTENING` to extend L_max scan to 13-15 for tighter d=4 anchor.

---

## §W3b-20. S88-CHIRAL-PAIR-MULTIPLICITY-SYMMETRY-VERIFICATION-PLUS-LAB-CONVERSION-FACTOR-DERIVATION

### 1. What

TWO-PART substrate-physics derivation of the chiral-pair multiplicity ratio `f_67/f_88` from inheritance-falsifier-protocol.md first principles, combined with the full Peter-Weyl character evaluation `χ_67(p,q)` and `χ_88(p,q)` at p+q ≤ 10. The two parts combine to predict the rank-2 cohomology-asymmetry ratio at lab-side, target value `7.324992` (W-5 Sage-exact), against the Class-B Gate-2 0.1% tolerance band `[7.3177, 7.3323]`.

- **Part D-A (closed-form Casimir derivation)**: substrate-derive the multiplicity ratio `f_67/f_88` from SU(3) Casimir contractions on the (λ_6, λ_7) off-diagonal chiral-pair sub-block vs the λ_8 angular-diagonal sub-block. Closed-form output: `f_67/f_88 = C_2[(λ_6, λ_7) sub-block] / C_2[λ_8 sub-block]` with explicit Casimir eigenvalue evaluations.
- **Part D-B (Peter-Weyl character evaluation)**: full `χ_67(p,q)` and `χ_88(p,q)` evaluation at all (p,q) with p+q ≤ 10 (66 sectors). Sum the multiplicity-weighted contributions into `cocycle_norm_phi67_PW` and `cocycle_norm_phi88_PW` and verify against the W-5 Sage-exact pinned values.

### 2. Why (substrate-physics rationale)

The (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5) preserves the substrate-derived ratio `‖φ_67‖ / ‖φ_88‖` INTACT in the laboratory measurement under common-exponent p, INDEPENDENT of the precise (Δ_B/Δ_A) value. The cohomology-asymmetry test (Class-B Gate-2 of inheritance-falsifier-protocol.md) is therefore substrate-falsifying iff the substrate-derived ratio is independently anchored at first principles. Item #20 establishes this anchor via two independent computational routes (Part D-A closed-form, Part D-B numerical Peter-Weyl); convergence between the two routes validates the Sage-exact pinned ratio 7.324992 and certifies the rank-2 Class-B Gate-2 falsifier as a genuine substrate prediction (not a numerical accident).

The substrate-physics interpretation: φ_67 lives on the off-diagonal chiral-pair sub-block of M_3(ℂ) (the (λ_6, λ_7) Gell-Mann generators, which span the SO(2) ≅ U(1)_chiral subgroup orthogonal to the Cartan); φ_88 lives on the diagonal hypercharge λ_8 (Cartan element). The Casimir on the off-diagonal pair scales as `2 · (1/2)^2 · |W_chiral|` where W_chiral is the chiral Weyl orbit; the Casimir on λ_8 scales as `(1/√3)^2 · 1`. The Cartan-vs-off-diagonal asymmetry is the structural origin of the 7.324992 ratio.

### 3. Method (substrate-first; two-route convergence)

```
PART D-A (closed-form Casimir derivation):
  Step A1: Construct SU(3) Casimir C_2 = Σ_a (T_a)² in adjoint rep on (λ_6, λ_7) sub-block.
           Off-diagonal pair lifts via raising/lowering operators E_67 = (λ_6 + i λ_7)/2.
           C_2 |E_67⟩ = c_67 |E_67⟩ where c_67 is the chiral-pair Casimir eigenvalue.
  Step A2: Construct Casimir on λ_8 = diag(1, 1, -2)/√3 (hypercharge generator).
           C_2 |λ_8⟩ = c_88 |λ_8⟩.
  Step A3: f_67/f_88 = c_67 / c_88 (Casimir-weighted multiplicity ratio).
  Step A4: Numerical evaluation of c_67, c_88 in canonical SU(3) normalization.

PART D-B (Peter-Weyl character evaluation):
  Step B1: For each (p,q) with p+q ≤ 10 (66 sectors):
           - Compute irrep dim d(p,q) and Weyl character χ_(p,q)(g) sampled on Cartan torus.
           - Compute χ_67(p,q) = ∫_T |χ_(p,q)(diag(α, β, -α-β))|² · |projection on (λ_6,λ_7)|² dα dβ.
           - Compute χ_88(p,q) = ∫_T |χ_(p,q)(diag(α, β, -α-β))|² · |projection on λ_8|² dα dβ.
  Step B2: Sum over sectors:
           cocycle_norm_phi67_PW = Σ_(p,q) m_(p,q) · χ_67(p,q) · |λ_min((p,q),τ_fold)|^{-2}
           cocycle_norm_phi88_PW = Σ_(p,q) m_(p,q) · χ_88(p,q) · |λ_min((p,q),τ_fold)|^{-2}
           where m_(p,q) is the Peter-Weyl multiplicity (= d(p,q)²) and λ_min is the bottom eigenvalue
           of D_K in sector (p,q) at τ_fold.
  Step B3: ratio_PW = cocycle_norm_phi67_PW / cocycle_norm_phi88_PW.
  Step B4: rel_dev_DA = |ratio_DA − 7.324992| / 7.324992
           rel_dev_DB = |ratio_PW − 7.324992| / 7.324992
           rel_dev_AB = |ratio_DA − ratio_PW| / max(|ratio_DA|, |ratio_PW|)

PART COMBINED:
  Step C1: Verify both rel_dev_DA and rel_dev_DB lie in W-5 Sage-exact tolerance band [7.3177, 7.3323] / 7.324992.
  Step C2: Verify two-route convergence rel_dev_AB < 1e-9 (independent route cross-check).
  Step C3: Emit dual-SHA verdict line.
```

### 4. PASS / FAIL / INFO criteria (pre-registered)

- **PASS** (all three sub-criteria):
  - Part D-A: `|ratio_DA − 7.324992| / 7.324992 < 1e-3` (Class-B Gate-2 0.1% band)
  - Part D-B: `|ratio_PW − 7.324992| / 7.324992 < 1e-3` (Class-B Gate-2 0.1% band)
  - Two-route convergence: `|ratio_DA − ratio_PW| / max(|ratio_DA|, |ratio_PW|) < 1e-9` (independent-route bit-precision cross-check)
- **FAIL** (any of the three exceeds threshold): substrate-derived 7.324992 ratio does not survive first-principles Casimir + Peter-Weyl independent-route verification; route to NEEDS-INVESTIGATION carry-forward with diagnostic on which route diverged.
- **INFO** (Parts D-A AND D-B both PASS but two-route convergence in [1e-9, 1e-6]): substrate ratio confirmed at Class-B Gate-2 band but two routes disagree at sub-percent precision floor; carry-forward to tighten Peter-Weyl truncation to p+q ≤ 12.

### 5. Output artifacts

- `computations/s88_w3b_chiral_pair_multiplicity_two_route.py` — producing script (~600-700 lines; Part D-A Casimir derivation + Part D-B 66-sector Peter-Weyl loop + convergence cross-check)
- `computations/s88_w3b_chiral_pair_multiplicity_two_route.npz` — keys: `c_67_casimir_eigenvalue`, `c_88_casimir_eigenvalue`, `ratio_DA`, `chi_67_per_sector`, `chi_88_per_sector`, `cocycle_norm_phi67_PW`, `cocycle_norm_phi88_PW`, `ratio_PW`, `rel_dev_DA`, `rel_dev_DB`, `rel_dev_AB`, `sector_multiplicities`, `lambda_min_per_sector`
- `computations/s88_w3b_chiral_pair_multiplicity_two_route.png` — 4-panel figure: (top-left) Casimir eigenvalues bar chart c_67 / c_88; (top-right) per-sector χ_67(p,q) heatmap on (p,q) lattice; (bottom-left) per-sector χ_88(p,q) heatmap; (bottom-right) running cumulative `cocycle_norm_phi67/88_PW` vs sector index, with horizontal line at W-5 Sage-exact target
- Verdict line in `computations/s88_gate_verdicts.txt`

### 6. Machinery pin (PRDR enumeration)

```
L_max_PW                  = 10                       # p+q ≤ 10 → 66 sectors
tau_fold                  = canonical_constants.tau_fold  # = 0.190
SU3_Casimir_normalization = "Gell-Mann_canonical_T_a_T_a_=_4/3_id_on_fundamental"
chiral_pair_generators    = "(lambda_6, lambda_7)_Gell-Mann"
hypercharge_generator     = "lambda_8_=_diag(1,1,-2)/sqrt(3)"
Peter_Weyl_integration    = "Cartan_torus_sampling_with_Vandermonde_measure"
W5_Sage_exact_target      = 7.324992                 # canonical_constants.substrate_cocycle_ratio_67_88
class_B_band_relative     = 1e-3                     # 0.1% per inheritance-falsifier-protocol.md Gate-2
two_route_convergence     = 1e-9                     # PASS-bit-precision floor
two_route_INFO_band       = (1e-9, 1e-6)             # marginal-INFO band
spectrum_cache_path       = "s84_spectrum_cache_L12_tau019.npz"
spectrum_cache_sha        = "9e6d9cf7fd6a6949..."
schema_version            = "S84+"
```

### 7. Depends on

- `computations/s84_spectrum_cache_L12_tau019.npz` (UPSTREAM CACHE; SHA `9e6d9cf7fd6a6949...`)
- `canonical_constants.py`: `tau_fold`, `M_KK`, `cocycle_norm_phi67`, `cocycle_norm_phi88`, `substrate_cocycle_ratio_67_88`
- S86 W-5 §VII.AF.1 cross-pillar bridge entry (cocycle-norm pinning)
- S86 W-5 W11-C5 falsifier inventory entry (Class-B Gate-2 0.1% band)
- `.claude/rules/inheritance-falsifier-protocol.md` §"Class B — Cohomology-Asymmetry Test"
- `.claude/rules/cross-pillar-bridge-anatomy.md` §"Forward-looking convention-pin" (FWD-C3 bridge)

### 8. Owner

volovik-superfluid-universe-theorist + connes-ncg-theorist JOINT
- Volovik PRIMARY on Part D-A (substrate-physics interpretation: chiral-pair vs hypercharge sub-block decomposition; physical content of (λ_6, λ_7) ≅ U(1)_chiral)
- Connes PRIMARY on Part D-B (Peter-Weyl character calculus; SU(3) representation theory; Casimir adjoint computation)
- Joint synthesis on two-route convergence verdict + working-paper §W3b-20 substrate-framing paragraph

### 9. Effort estimate

~1.5 wave-equivalents (two-route methodology requires independent script paths + convergence cross-check; 66-sector Peter-Weyl loop is computationally non-trivial but precomputed eigenvalues from cache make per-sector cost O(d(p,q)²))

### 10. Verdict source

`computations/s88_gate_verdicts.txt`

### 11. Working-paper section

`sessions/archive/session-88/session-88-results-workingpaper.md §W3b-20` — substantive content (≥15 lines): Part D-A Casimir derivation explicit equations + Part D-B Peter-Weyl integration explicit formula + two-route convergence interpretation + cross-link to §VII.AF.1 cross-pillar bridge + substrate-framing paragraph on chiral-pair-vs-hypercharge structural origin of the 7.324992 ratio + cancellation-theorem applicability declaration.

### 12. Plan-freeze SHA pin

`sha256_of_plan_block(W3b-20) = pending` (computed at plan-freeze)

### 13. Carry-forward conditions

- **PASS**: substrate-derived 7.324992 ratio promoted from S86 W-5 Sage-exact pin to two-route-verified canonical; FWD-C3 bridge candidate (cross-pillar-bridge-anatomy.md §"Forward template-adoption" K-counter) advances toward MANDATORY-status threshold (K=2 → K=3 once W3b-20 lands as second instance of two-route closure).
- **FAIL**: NEEDS-INVESTIGATION carry-forward with diagnostic on Part D-A vs Part D-B divergence; possible structural revision of the chiral-pair-vs-hypercharge sub-block decomposition.
- **INFO** (two-route marginal): carry-forward `S89-CHIRAL-PAIR-PW-TIGHTEN` extending Peter-Weyl truncation to p+q ≤ 12 (351 sectors).

---

## §W3b-28. S88-CHI-A-CHIRAL-CORRECTION-VERIFICATION

### 1. What

Independent direct numerical verification of the substrate provenance of `χ_A = 3/2 = 1.500000` via direct evaluation of the Volovik 2003 §3.4 axisymmetric A-phase Fermi-surface average `⟨|Δ_A(k)|²⟩_FS`. This closes the substrate-anchor for the (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5) by establishing that χ_A is a substrate-first computed constant (not an empirically fit parameter).

The chiral correction χ_A enters every inheritance-falsifier-protocol Class-B gate via the lab-conversion factor `(Δ_B/Δ_A)^p`; its value is canonically `3/2` per Volovik 2003 §3.4 axisymmetric A-phase FS-average. Item #28 verifies this value by independent direct numerical FS integration.

### 2. Why (substrate-physics rationale)

The (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5; machine-precision residual 0.0e+00) requires that χ_A and χ_B be substrate-first constants, NOT empirical fit parameters. Otherwise the cancellation theorem's structural-falsifier status collapses to a numerical coincidence. Item #28 establishes χ_A's substrate provenance by direct FS-integration over the axisymmetric A-phase gap function `Δ_A(k) = Δ_0 · sin(θ_k) · e^{i φ_k}` (Volovik 2003 §3.4).

The substrate-physics interpretation: the A-phase gap is point-node (vanishing at θ_k = 0, π); the FS-average `⟨|Δ_A|²⟩` factors into a polar integral `⟨sin²(θ)⟩_FS = ∫_0^π sin²(θ) · sin(θ) dθ / ∫_0^π sin(θ) dθ = 2/3` (using FS-volume-element `sin(θ) dθ dφ`). The ratio `⟨|Δ_A|²⟩ / |Δ_0|² = 2/3` gives the gap-renormalization factor; the χ_A = 3/2 value emerges as the inverse `(2/3)^{-1} = 3/2`. This is the structural origin: χ_A measures the FS-averaged "gap deficit" of the A-phase relative to the isotropic B-phase reference (where ⟨|Δ_B|²⟩ = |Δ_0|² so χ_B = 1).

### 3. Method (substrate-first; direct FS integration)

```
Step 1: Define A-phase gap function on the unit S² Fermi surface:
        Δ_A(θ, φ) = Δ_0 · sin(θ) · exp(i · φ)        # axisymmetric, point-node at poles
        |Δ_A(θ, φ)|² = |Δ_0|² · sin²(θ)

Step 2: Compute FS-average via numerical quadrature (Gauss-Legendre on [0, π] × [0, 2π]):
        ⟨|Δ_A|²⟩_FS = (1/4π) · ∫_0^π ∫_0^{2π} |Δ_A(θ, φ)|² · sin(θ) dφ dθ
                    = (1/4π) · 2π · |Δ_0|² · ∫_0^π sin³(θ) dθ
                    = (1/2) · |Δ_0|² · [4/3]                 # ∫_0^π sin³(θ) dθ = 4/3 exact
                    = (2/3) · |Δ_0|²

Step 3: Compute ratio_A = ⟨|Δ_A|²⟩_FS / |Δ_0|² (numerical via Gauss-Legendre at N=128, 256, 512)
        Verify ratio_A → 2/3 at machine precision.

Step 4: Compute χ_A = 1 / ratio_A = 3/2.
        Verify χ_A − 3/2 < 1e-12 at N=512 quadrature.

Step 5: Cross-check via analytic closed form:
        ∫_0^π sin³(θ) dθ = ∫_0^π (1 − cos²(θ)) sin(θ) dθ
                         = [−cos(θ) + cos³(θ)/3]_0^π
                         = (1 − 1/3) − (−1 + 1/3)
                         = 2/3 + 2/3
                         = 4/3                              # exact
        Therefore ⟨|Δ_A|²⟩_FS = (2/3) |Δ_0|² and χ_A = 3/2 ANALYTICALLY EXACT.

Step 6: Cross-validate against Volovik 2003 §3.4 axisymmetric A-phase chiral correction.
        (Heritage citation: researchers/Volovik/, monograph §3.4.)

Step 7: Emit dual-SHA verdict line.
```

### 4. PASS / FAIL / INFO criteria (pre-registered)

- **PASS** (all three sub-criteria):
  - Numerical Gauss-Legendre at N=512: `|χ_A_numerical − 1.5| < 1e-12`
  - Convergence: `|χ_A(N=512) − χ_A(N=256)| < 1e-13` (quadrature stability)
  - Analytic cross-check: `χ_A_analytic = 3/2` exact (Sage-symbolic verification of `∫_0^π sin³(θ) dθ = 4/3`)
- **FAIL** (any sub-criterion exceeds threshold): Volovik 2003 §3.4 chiral-correction value cannot be reproduced from first-principles axisymmetric FS-average; route to NEEDS-INVESTIGATION carry-forward — possible misidentification of A-phase gap function or FS-volume-element convention.
- **INFO** (numerical PASS but Sage-symbolic analytic step skipped due to environment unavailability): partial-PASS with carry-forward to S89 to complete Sage-symbolic analytic cross-check.

### 5. Output artifacts

- `computations/s88_w3b_chi_a_chiral_correction_verification.py` — producing script (~250-350 lines; Gauss-Legendre quadrature loop + Sage-symbolic analytic cross-check via mcp__sage if available, else mpmath fallback)
- `computations/s88_w3b_chi_a_chiral_correction_verification.npz` — keys: `chi_A_per_N`, `N_quadrature_grid`, `chi_A_analytic`, `chi_A_numerical_at_N512`, `convergence_residual`, `analytic_residual`, `verdict`
- `computations/s88_w3b_chi_a_chiral_correction_verification.png` — 2-panel figure: (left) χ_A_numerical vs N (log-x); (right) convergence residual `|χ_A(N) − 3/2|` vs N (log-log)
- Verdict line in `computations/s88_gate_verdicts.txt`

### 6. Machinery pin (PRDR enumeration)

```
N_quadrature_grid         = (32, 64, 128, 256, 512)  # Gauss-Legendre nodes per dimension
chi_A_target_value        = 1.5                       # = 3/2 per Volovik 2003 §3.4
chi_A_PASS_tolerance      = 1e-12                     # numerical machine-epsilon floor
chi_A_convergence_tol     = 1e-13                     # N=512 vs N=256 stability
quadrature_scheme         = "Gauss-Legendre_separable_polar_azimuthal"
A_phase_gap_function      = "Delta_A = Delta_0 · sin(theta) · exp(i · phi)"  # Volovik 2003 §3.4
FS_volume_element         = "sin(theta) dtheta dphi"  # canonical S² volume form
analytic_cross_check_tool = "mcp__sage_eval if available, else mpmath.quad"
schema_version            = "S84+"
```

### 7. Depends on

- Volovik 2003 §3.4 axisymmetric A-phase FS-average formula (researchers/Volovik/ heritage citation; structural definition of Δ_A(k))
- `canonical_constants.py`: `chi_A_FW = 1.5` (S58 baseline; promoted post-W3b-28 PASS to dual-anchor pin via update_constant call)
- S86 W-5 DONE-5 (Δ_B/Δ_A)^p cancellation theorem residual 0.0e+00
- `.claude/rules/inheritance-falsifier-protocol.md` §"(Δ_B/Δ_A)^p Cancellation Theorem"

### 8. Owner

volovik-superfluid-universe-theorist + connes-ncg-theorist JOINT
- Volovik PRIMARY on substrate-physics derivation (Volovik 2003 §3.4 heritage; A-phase gap structure; FS-average physical interpretation)
- Connes PRIMARY on numerical-quadrature execution + analytic Sage cross-check
- Joint synthesis on cancellation-theorem applicability declaration

### 9. Effort estimate

~0.5 wave-equivalents (single-script, well-conditioned numerical integration + analytic cross-check; no eigvec basis loading required)

### 10. Verdict source

`computations/s88_gate_verdicts.txt`

### 11. Working-paper section

`sessions/archive/session-88/session-88-results-workingpaper.md §W3b-28` — substantive content (≥15 lines): A-phase gap function definition + FS-average derivation + analytic cross-check (∫_0^π sin³(θ) dθ = 4/3 explicit) + Volovik 2003 §3.4 heritage citation + (Δ_B/Δ_A)^p cancellation-theorem applicability + substrate-framing paragraph on point-node-vs-isotropic gap-deficit structural origin of χ_A = 3/2.

### 12. Plan-freeze SHA pin

`sha256_of_plan_block(W3b-28) = pending` (computed at plan-freeze)

### 13. Carry-forward conditions

- **PASS**: χ_A = 3/2 promoted to dual-anchor canonical (Volovik 2003 §3.4 heritage + S88 W3b-28 substrate-first verification); cancellation-theorem structural-falsifier status of every Class-B inheritance-falsifier-protocol gate is reinforced.
- **FAIL**: structural revision of A-phase gap function or FS-average convention required; carry-forward `S89-CHI-A-VOLOVIK-DEFINITION-RECONCILE` with bibliographic re-audit of Volovik 2003 §3.4.
- **INFO** (Sage-symbolic step deferred): carry-forward `S89-CHI-A-SAGE-SYMBOLIC-COMPLETE` to land the analytic cross-check via mcp__sage_eval.

---

## Wave 3b → Wave 3c Decision Point

### Decision rule

The W3b → W3c transition is GATE-COUNT dependent (no semantic prerequisite blocks W3c on W3b verdicts; W3c covers items 16-19 + 21-27 + 29+ which are independent gates of the chi/chi_A/multiplicity-ratio rescue-class triple).

**Trigger to dispatch W3c**: all three W3b verdict lines appended to `computations/s88_gate_verdicts.txt` (PASS / FAIL / INFO, all three are valid scientific outcomes per `.claude/rules/math-scripts.md` §"All Results Are Good Results"; FAIL on a W3b gate does NOT block W3c dispatch).

### W3c dispatch consequences (forward-looking; not authored here)

- If W3b-15 PASS + W3b-20 PASS + W3b-28 PASS: §VII.AF.1 cross-pillar bridge empirical anchor at L_max=10 is two-route-verified; W3c dispatches the remaining inheritance-falsifier-protocol Class-A row-wise NULL gates (#16-19) + Class-B cross-cocycle ratio extension gates (#21-27) + supporting F-row gates (#29+).
- If any W3b gate FAILs: W3c proceeds independently but W3b NEEDS-INVESTIGATION carry-forward is appended to S89 plan-freeze; FWD-C3 bridge candidate K-counter advancement (cross-pillar-bridge-anatomy.md §"Forward template-adoption") is BLOCKED until investigation closes.
- If any W3b gate INFOs: W3c proceeds; S89 carries forward the relevant precision-tightening (envelope, two-route convergence, Sage-symbolic, etc.).

---

## Wave 3b Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness", the following machinery parameters are enumerated and pinned for plan-freeze validation. Each parameter has an explicit pin source.

### Cross-gate machinery (shared across W3b-15, W3b-20, W3b-28)

```
session_label             = "S88"
wave_label                = "W3b"
plan_file                 = "sessions/session-plan/session-88-plan-w3b.md"
verdict_file              = "computations/s88_gate_verdicts.txt"
working_paper             = "sessions/archive/session-88/session-88-results-workingpaper.md"
schema_version            = "S84+"                         # gate-verdicts.md schema
wave_class                = "COMPUTE"                       # wave-classification.md M-test result
canonical_constants_pin   = "computations/canonical_constants.py"
spectrum_cache_pin        = "computations/s84_spectrum_cache_L12_tau019.npz"
spectrum_cache_sha        = "9e6d9cf7fd6a6949..."            # input-pin SHA
substrate_first_audit     = "_substrate_first_provenance_audit.py"  # forward audit (S87 carry-forward V.1)
source_recon_audit        = "_source_reconciliation_audit.py"
pru_audit                 = "_pru_cardinality_audit.py"
gate_verdict_helper       = "script-template.py append_verdict()"
```

### W3b-15 specific (chi inheritance KDE)

```
L_max_set                 = (10, 11, 12)
tau_fold                  = canonical_constants.tau_fold     # = 0.190
A_F_algebra               = "C+H+M3C"                        # S84 W8-87b
chi_inheritance_morphism  = "M3C_to_zero_C_and_H_to_canonical_M2C"
zero_eigenvalue_floor     = 0.02                              # = 0.01 / r_tau(0.190); M_KK units
chi_image_norm_threshold  = 1e-12
envelope_constant_PASS    = 10.0
envelope_constant_INFO    = 50.0
generator_basis_C         = "(1_C, e_R, e_L, sigma_3 in subspace)"     # 4 ℂ-block generators
generator_basis_H         = "(sigma_1, sigma_2, sigma_3, identity)"    # 4 ℍ-block generators
generator_basis_M3        = "Gell-Mann_T_1..T_8"                       # 8 M_3(ℂ) generators
```

### W3b-20 specific (chiral-pair multiplicity two-route)

```
L_max_PW                  = 10
SU3_Casimir_normalization = "Gell-Mann_canonical_T_a_T_a=4/3_id_on_fundamental"
chiral_pair_generators    = "(lambda_6, lambda_7)_Gell-Mann"
hypercharge_generator     = "lambda_8=diag(1,1,-2)/sqrt(3)"
Peter_Weyl_integration    = "Cartan_torus_sampling_with_Vandermonde_measure"
sectors_count             = 66                                  # p+q ≤ 10
W5_Sage_exact_target      = 7.324992
class_B_band_relative     = 1e-3                                # 0.1% per inheritance-falsifier-protocol.md
two_route_convergence_PASS = 1e-9
two_route_convergence_INFO = 1e-6                               # marginal-INFO upper bound
```

### W3b-28 specific (chi_A chiral correction)

```
N_quadrature_grid         = (32, 64, 128, 256, 512)
chi_A_target_value        = 1.5
chi_A_PASS_tolerance      = 1e-12
chi_A_convergence_tol     = 1e-13
quadrature_scheme         = "Gauss-Legendre_separable_polar_azimuthal"
A_phase_gap_function      = "Delta_A=Delta_0*sin(theta)*exp(i*phi)"
FS_volume_element         = "sin(theta)*dtheta*dphi"
analytic_cross_check_tool = "mcp__sage_eval_OR_mpmath_quad"
```

### PRDR completeness

All machinery parameters above are enumerated explicitly per the PRDR (Pre-Registration Dry-Run) discipline of `.claude/rules/epistemic-discipline.md`. No parameter is left as `<runtime-decided>` or `<TBD>`. PRU cardinality audit `_pru_cardinality_audit.py` should return D_PRU_raw = 0 for all three W3b gates at plan-freeze.

---

## Wave 3b Input-SHA Ledger

This ledger pins the SHA-256 hashes of all input files cited by the W3b gate blocks. Per `.claude/rules/agent-standards.md` §"AMRI Test 1 calibration", agent-memory files are NOT pinned here (only project-level files). Per `.claude/rules/epistemic-discipline.md` §"Source Reconciliation", these SHAs are computed at plan-freeze and the audit script `_source_reconciliation_audit.py` cross-checks them against canonical_constants and prior session artifacts.

| Input file | Role | SHA-256 (computed at plan-freeze) |
|:-----------|:-----|:----------------------------------|
| `computations/s84_spectrum_cache_L12_tau019.npz` | UPSTREAM CACHE (W3b-15, W3b-20) | `9e6d9cf7fd6a6949...` (full 64-hex pinned at dispatch) |
| `computations/canonical_constants.py` | constants pin (all three) | `<pinned at dispatch>` |
| `.claude/rules/inheritance-falsifier-protocol.md` | rule substrate (W3b-15, W3b-20, W3b-28) | `<pinned at dispatch>` |
| `.claude/rules/cross-pillar-bridge-anatomy.md` | rule substrate (W3b-15, W3b-20) | `<pinned at dispatch>` |
| `sessions/permanent-results-registry.md` (§VII.AF.1) | registry anchor (W3b-15, W3b-20) | `<pinned at dispatch>` |
| `sessions/framework/registry/falsifier-master-inventory.md` | falsifier-master-inventory anchor (W3b-15, W3b-20, W3b-28) | `<pinned at dispatch>` |

### Per-gate plan-block SHAs (computed at plan-freeze)

| Gate | sha256_of_plan_block |
|:-----|:--------------------|
| W3b-15 | `pending` (computed at plan-freeze) |
| W3b-20 | `pending` (computed at plan-freeze) |
| W3b-28 | `pending` (computed at plan-freeze) |

### audit_sha256 formula (per gate; computed at runtime)

```
audit_sha256 = closure_hash(
    canonical_constants_sha256,
    spectrum_cache_sha256 (if used),
    rule_file_shas (inheritance-falsifier-protocol.md, cross-pillar-bridge-anatomy.md as applicable),
    plan_block_sha256 (this gate's §W3b-{n} block),
    machinery_pin_map (the gate's §6 PRDR enumeration)
)
```

Per `.claude/rules/v3-closure-recovery.md` sig_5 uniqueness, audit_sha256 must be distinct across all three W3b gates. The per-gate plan-block SHA + per-gate machinery-pin distinguishes them by construction.

---

## Wave 3b Provenance & Cross-References

- **Workshop substrate**: S86 W-5 §VII.AF.1 (volovik+connes joint; HP^1 cohomology + quantum-metric bridge); S86 W-5 W11-C5 (3He-B vortex-core spectroscopy falsifier); S86 W-5 DONE-5 ((Δ_B/Δ_A)^p cancellation theorem)
- **Rule substrate**:
  - `.claude/rules/inheritance-falsifier-protocol.md` (Class A + Class B + (Δ_B/Δ_A)^p cancellation theorem; rank-2 generalization)
  - `.claude/rules/cross-pillar-bridge-anatomy.md` (5-element IS-not-IN anatomy; 3-level ladder; FWD-C3 bridge K-counter)
  - `.claude/rules/joint-theorem-promotion.md` (4-stage pathway; STAGE-1-CANDIDATE → STAGE-3-PERMANENT)
  - `.claude/rules/wave-classification.md` (M1-M4 conjunction; COMPUTE-class fallthrough)
  - `.claude/rules/math-scripts.md` (canonical_constants imports + double-check substitution chain)
- **Registry anchors**:
  - `sessions/permanent-results-registry.md §VII.AF.1` (Pillar III ↔ Pillar IV bridge theorem; substrate-IS HP^1 cohomology pairing; laboratory-IN Peotta-Törmä quantum-metric trace)
  - `sessions/framework/registry/falsifier-master-inventory.md` rows F1-F5 (3He-B kernel-signature + cohomology-asymmetry rows; Class A + Class B Gate-2)
- **Canonical constants** (cited by all three W3b gates):
  - `tau_fold = 0.190` (canonical_constants.py:1240)
  - `cocycle_norm_phi67 = 0.793346 M_KK²` (S86 W-5 §VII.AF.1)
  - `cocycle_norm_phi88 = 0.108307 M_KK²` (S86 W-5 §VII.AF.1)
  - `substrate_cocycle_ratio_67_88 = 7.324992` (W-5 Sage-exact)
  - `chi_A_FW = 1.5` (S58 baseline; W3b-28 PASS promotes to dual-anchor)
- **Spectrum cache**: `computations/s84_spectrum_cache_L12_tau019.npz` (S84 W3 PASS-pinned; SHA `9e6d9cf7fd6a6949...`)

---

## Wave 3b Authorship & Plan-Freeze Discipline

- **Plan author**: planner-w3b (split of stalled W3 per orchestrator dispatch protocol).
- **Plan-freeze validation queue** (run before W3b dispatch):
  1. `_pru_cardinality_audit.py` — verify D_PRU_raw = 0 for all three gates
  2. `_source_reconciliation_audit.py` — verify all input-SHA pins match canonical_constants + spectrum cache
  3. `_substrate_first_provenance_audit.py` (S87 carry-forward V.1; if implemented) — verify all PROVENANCE fields cite substrate-first sources, NOT external-paper placeholders
  4. `_wave_classification_audit.py` (W-13 AUDIT-2; if implemented) — verify W3b classified as COMPUTE
- **Dispatch-time check**: orchestrator post-dispatch verification per `.claude/rules/agent-standards.md` §"Completion Verification" — verify on-disk artifact existence + non-stub content for all three gates before declaring W3b closed.

---

*End of session-88-plan-w3b.md*
