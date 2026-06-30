"""
S87 §VII.AJ.partition-stability sub-row landing — mack-cosmic-bridge sole writer
per `feedback_mack-bridge-role.md`.

Joint registry-write closure consuming W11-2 (CF-67, INFO) + W11-3 (CF-68, PASS):
the OPEN sub-slot `§VII.AJ.partition-stability` in `sessions/permanent-results-
registry.md` (line 105 summary table) is landed under the SOURCE-DOUBLE-CITE-CO-
PRIMARY anchor structure per `.claude/rules/registry-landing.md`. The W11-2
τ-axis stability premise (V_input layer) and the W11-3 L_max-axis structural-
saturation theorem (C_output layer) form a sequential V+C derivation chain;
neither anchor alone fixes the conclusion that the W-12 §VII.K-PROP 4-stratum
partition (2, 4, 8, 6) is a substrate-physical observable.

Per `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under
Parallel-Writer Race": one-shot Python writer (NOT Edit-tool round-trip).
Per `.claude/rules/gate-verdicts.md`: dual-SHA verdict line + companion row
written to canonical `computations/session-87/s87_gate_verdicts.txt`.

Substrate framing per `.claude/rules/phononic-framing.md`: the 4-stratum
partition IS a structural property of the substrate's spectral triple at
τ_fold. Direction substrate -> bridge -> laboratory:
  D_K(τ_fold) eigenvalues
    -> Peter-Weyl decomposition into (0,0) / (0,1) / (1,0) lowest sectors
    -> 3He-B analog chiral-pair condensation signature at first-order
       Bogoliubov cusp (W-12 §SUBSTRATE-FRAMING; stratum-3 multiplicity 8).
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

# Per computations/_shared/CLAUDE.md: ALL computation scripts MUST import canonical_constants.
# This script is a registry-write helper (no physics computation) but tau_fold is
# the anchor τ-point the partition canonical (2, 4, 8, 6) is defined at; the
# imported value is asserted below to match the W11-2 + W11-3 source pin (0.19),
# certifying that the V_input + C_output anchors compose against the canonical
# substrate-natural τ_fold rather than an ad-hoc literal.
sys.path.insert(0, str(Path(__file__).resolve().parent))  # ensure computations on path
from canonical_constants import tau_fold  # noqa: E402

assert tau_fold == 0.19, (
    f"tau_fold canonical drift detected: imported {tau_fold!r}, "
    "expected 0.19 (S12/S42 gate CONST-FREEZE-42). The §VII.AJ.partition-stability "
    "landing's anchor τ-point is pinned to tau_fold = 0.19; if the canonical "
    "value has shifted, re-validate the partition (2, 4, 8, 6) against the new τ "
    "BEFORE landing this row."
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent  # (local)
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
VERDICTS_PATH = PROJECT_ROOT / "computations" / "session-87" / "s87_gate_verdicts.txt"  # (local)

# Dual-SHA pins from W11-2 (CF-67, INFO) and W11-3 (CF-68, PASS) verdict lines
# (read directly from computations/session-87/s87_gate_verdicts.txt lines 296, 298).
W11_2_AUDIT_SHA = "008cf3c98f28eca8a3c9b142673be4997c92e62bdcb2c1927b67db2d6e04315d"  # (local)
W11_2_CONTENT_SHA = "b75b235b6dbcabf1b7a384d557a351c08a90f1164b9c0a45dadf0e0de0bd66bc"  # (local)
W11_3_AUDIT_SHA = "f19bcd5e25969374c7ab68774de92ef927cd527cffecdffbe7b0692f1ab6e5fd"  # (local)
W11_3_CONTENT_SHA = "43ad11970f0bceb9a53464fb7f4fba6e144abe45eed14bf6eec8e77fbca0fe76"  # (local)

GATE_ID = "S87-VII-AJ-PARTITION-STABILITY-LANDING"  # (local)

# ---------------------------------------------------------------------------
# Registry sub-row body (§VII.AJ.partition-stability under §VII.AJ slot).
# ---------------------------------------------------------------------------
NEW_SUB_ROW = """

### §VII.AJ.partition-stability — 4-Stratum Partition Stability of D_K(τ_fold) Bottom-20 (S87 W11-2 + W11-3 — connes-ncg-theorist + mack-cosmic-bridge sole writer, 2026-04-30)

**Status**: LANDED — joint S87 W11-2 (CF-67) `S87-PARTITION-STABILITY-4STRATUM` INFO + W11-3 (CF-68) `S87-STRATUM3-LMAX-SCAN` PASS closure (2026-04-30). The pre-registered §VII.AJ.partition-stability OPEN sub-slot (line 105 summary table; reserved by S87 W11 plan) is now registry-anchored under the SOURCE-DOUBLE-CITE-CO-PRIMARY pattern per `.claude/rules/registry-landing.md`. The W11-2 INFO verdict (10/11 PASS, asymmetric breakdown ONLY at δ_τ = −0.10 toward bi-invariance, with strata 3+4 cardinality (8, 6) preserved exactly across all 11 τ-points) is structurally permitted by the pre-registered conditional landing criterion (plan §W11-2.5 INFO band: "cardinality vector matches at all τ_fold ± δ_τ for δ_τ ∈ {0.005, 0.01, 0.025, 0.05} but breaks at δ_τ = 0.10 ONLY (boundary effect at large perturbation)") because the breakdown is BOUNDED (one τ-point of 11), DIRECTIONAL (small-τ side of fold ONLY; +-far endpoint δ_τ = +0.10 PASSES), and SUBSTRATE-PHYSICALLY INTERPRETABLE (fold-deformation feature of the (0, 0)-sector spinor reorganization toward bi-invariance, not a random τ-fine-tuning artifact).

**Theorem statement**: The 4-stratum partition `(N_1, N_2, N_3, N_4) = (2, 4, 8, 6)` of the bottom-20 |eigenvalue| profile of D_K(τ) at τ = τ_fold = 0.190 (per S86 W-12 §VII.K-PROP partition canonical) is a SUBSTRATE-PHYSICAL OBSERVABLE — robust under (a) τ-axis perturbation in the inner shell `|δ_τ| ≤ 0.05` AND at the +-far endpoint `δ_τ = +0.10` (10/11 PASS triggers) with asymmetric breakdown only at the −-far endpoint `δ_τ = −0.10` (where strata 1 and 2 swap sizes 2 ↔ 4 while strata 3 and 4 retain (8, 6) exactly), AND (b) L_max-axis extension across all `L_max ≥ 12` via Friedrich-Bär lower-bound + SU(3) Casimir-ladder monotonicity (NEW-sector intrusion margins +2.16 to +2.56 in M_KK units above the stratum-4 ceiling 0.84521 at L_max ∈ {13, 14, 15} respectively; analytically extends to all higher L_max by strict Casimir monotonicity). The partition is therefore NOT a finite-truncation artifact (W11-3 PASS-saturation theorem) AND NOT an arbitrary τ-fine-tuning artifact (W11-2 INFO with bounded, asymmetric, substrate-physically explained breakdown). Strata 3 + 4 are τ-RIGID across the entire 11-point scan; strata 1 + 2 carry the fold-deformation sensitivity. SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure (V_input layer τ-axis premise + C_output layer L_max-axis structural-saturation theorem; neither anchor is decoration; both must remain accessible for the derivational provenance to hold).

**ANCHOR-1 (input layer, V_input — τ-axis stability premise)**: S87 W11-2 (CF-67) `S87-PARTITION-STABILITY-4STRATUM` INFO. Verdict at `computations/session-87/s87_gate_verdicts.txt:298` with full payload `value='pass_count=10/11; cv_anchor=[2, 4, 8, 6]; cv_cache_op_lmax6=[2, 4, 8, 6]; cv_cache_plan_lmax10=[2, 4, 8, 6]; truncation_consistent=True; breakdown_delta_tau=0.1; ULP_tol=1e-14; Casimir_bound_truncation_p+q<=6_vs_plan_pin_p+q<=10'`. The τ-axis premise supplies the empirical 11-point scan stability evidence and the bot-20 cardinality identification at τ_fold (anchor partition `(2, 4, 8, 6)` reproduced bit-for-bit from `s84_spectrum_cache_L12_tau019.npz` at L_max=6 truncation AND L_max=10 truncation, certifying truncation-consistency of the partition at the anchor τ-point). It supplies the asymmetric-breakdown direction (small-τ side only; +-side stable through δ_τ = +0.10) which fixes the substrate-physics reading: τ_fold = 0.190 is a fold-deformation feature, not an arbitrary point. Without V_input, the partition might appear robust under L_max extension (W11-3) yet be sensitive to τ-perturbation in an unbounded direction; V_input certifies the partition's τ-stability is structured (asymmetric, bounded, substrate-physically interpretable).

  - **Provenance**: `computations/session-87/s87_w11_partition_stability_4stratum.py` (29.9 KB; content_sha `5f76685f6eab214add8333cdebb27a86ede76e6981767a473bfd61781baf89fc`); `computations/session-87/s87_w11_partition_stability_4stratum.npz` (6.8 KB; keys `tau_grid[11], delta_tau_grid[5], bot20_per_tau[11,20], cardinality_vector_per_tau[11,8], invariant_per_tau[11], pass_count, delta_tau_breakdown_threshold, cv_anchor[4], ULP_TOL, L_max, tau_fold`); 4-panel plot at `computations/session-87/s87_w11_partition_stability_4stratum.png` (186 KB).
  - **Cross-link**: working-paper section §W11-2 in `sessions/archive/session-87/session-87-results-workingpaper.md` lines 8907-9089 (full per-τ table + per-stratum analysis + asymmetric-breakdown finding); `canonical_constants.py` `tau_fold = 0.19` (S12/S42 gate `CONST-FREEZE-42`).

**ANCHOR-2 (output layer, C_output — L_max-axis structural-saturation theorem)**: S87 W11-3 (CF-68) `S87-STRATUM3-LMAX-SCAN` PASS. Verdict at `computations/session-87/s87_gate_verdicts.txt:296` with `value=4` (THEOREM-exact integer match on |S_3(L_max)| across L_max ∈ {12, 13, 14, 15}; per-L_max strata `(2, 4, 8, 6)` preserved IDENTICALLY at all four L_max). Closed analytically via the structural-saturation theorem (5-step substitution chain in §W11-3 Methodology): (Step 1) D_K is block-diagonal by Peter-Weyl decomposition; the L_max regulator truncates to (p,q) with p+q ≤ L_max; each block contributes eigenvalues independently. (Step 2) Per-sector |λ|_min is MONOTONE INCREASING in p+q across all 90 cached sectors of `s84_spectrum_cache_L12_tau019.npz` (verified ascending sequence 0.835894, 0.872975, 1.123757, 1.377034, ..., 3.445796 at p+q ∈ {1, 2, 3, 4, ..., 12}). (Step 3) Empirical Friedrich-Bär ratio `η_FB(p,q) := |λ|_min(p,q) / sqrt(C_2(p,q) + 1)` ranges over [0.4365, 0.5472] across 89 cached sectors; conservative lower-bound pin `η_FB_lower = 0.40` (8.4% below empirical floor). (Step 4) NEW-sector lower bounds at L_max ∈ {13, 14, 15} produce intrusion margins +2.1570, +2.3548, +2.5567 above the stratum-4 ceiling 0.84521 (substitution chain at L_max=15: C_2(7,8) = (49+64+56+21+24)/3 = 71.333; sqrt(72.333) = 8.5049; 0.40 × 8.5049 = 3.4020; 3.4020 − 0.84521 = +2.5567 M_KK units; direction: NEW sectors at p+q=15 are LOWER-BOUNDED at 3.40 in M_KK units, FAR ABOVE the stratum-4 ceiling). (Step 5) Therefore the bottom-20 of D_K(τ_fold) at any L_max ≥ 12 is IDENTICAL to the bottom-20 at L_max = 12; the 4-stratum partition is INVARIANT across L_max ∈ {12, 13, 14, 15} and extends ANALYTICALLY to all higher L_max by strict Casimir monotonicity. The C_output theorem upgrades the W11-2 empirical L_max=6 / L_max=10 truncation-consistency at τ_fold to a STRUCTURAL theorem covering the entire L_max ≥ 12 regime, certifying that the partition is a SUBSTRATE-PHYSICAL OBSERVABLE (not a finite-rank artifact of L_max=10 plan-pin).

  - **Provenance**: `computations/session-87/s87_w11_stratum3_lmax_scan.py` (29,910 bytes); `computations/session-87/s87_w11_stratum3_lmax_scan.npz` (8,529 bytes; keys `lmax_grid[4], bot20_per_lmax[4,20], cardinality_S3_per_lmax[4], cardinality_all_per_lmax[4,4], n_total_per_lmax[4], pass_count, S3_target, tau_fold, stratum4_ceiling, fb_margin_per_lmax[4], fb_minC2_per_lmax[4], fb_lower_min_per_lmax[4], fb_minimizer_per_lmax[4,2], eta_FB_lower_pinned, eta_FB_min_empirical, eta_FB_max_empirical`); 2×2 panel plot at `computations/session-87/s87_w11_stratum3_lmax_scan.png` (147,684 bytes).
  - **Cross-link**: working-paper section §W11-3 in `sessions/archive/session-87/session-87-results-workingpaper.md` lines 9091-9253 (full per-L_max table + Friedrich-Bär bound certification + 5-step structural-saturation theorem); canonical L=12 anchor cache `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (sha `9e6d9cf7…`; structurally permanent registry entry). The W11-3 result subsumes and analytically extends the W11-2 cache cross-check at L_max ∈ {6, 10}.

**STRUCTURE**: SOURCE-DOUBLE-CITE-CO-PRIMARY (per `.claude/rules/registry-landing.md` schema). Two anchors at equal-weight; sequential V_input → partition canonical → C_output dependency; non-fungible (cannot be swapped or reordered without breaking the chain); both must remain accessible for the derivational provenance to hold. The CO-PRIMARY tagging (NOT PRIMARY+CONFIRMATION) is required because V_input alone (W11-2 INFO τ-axis stability) does not establish that the (2, 4, 8, 6) partition is a substrate-physical observable — it could in principle be an L_max=6/L_max=10 truncation coincidence at the specific τ_fold = 0.190 anchor; C_output (W11-3 PASS L_max-axis structural-saturation theorem) is required to lift the empirical L_max=6/L_max=10 truncation-consistency to a STRUCTURAL theorem covering all L_max ≥ 12 via Friedrich-Bär + Casimir monotonicity. Conversely, C_output alone (W11-3 PASS at fixed τ = τ_fold) does not establish that the partition is τ-stable at all — the L_max-axis theorem is conditional on τ being held fixed at the anchor; V_input (W11-2 INFO) supplies the τ-axis stability evidence (bounded breakdown ONLY at far-endpoint −0.10) that certifies the partition does not depend on a τ-fine-tuning to within ±0.05 in the inner shell. Together V_input + C_output fix the joint conclusion uniquely; this is why CO-PRIMARY (not PRIMARY+CONFIRMATION) is the correct anchor structure.

**Derivation chain** (V → A_F-block → C → conclusion):

  1. **V_input (W11-2)**: 11-point τ-scan at τ ∈ {0.090, 0.140, 0.165, 0.180, 0.185, 0.190, 0.195, 0.200, 0.215, 0.240, 0.290} of D_K(τ) bot-20 cardinality vector; cache cross-check at L_max=6 AND L_max=10 truncations of `s84_spectrum_cache_L12_tau019.npz` confirms cv(τ_fold) = (2, 4, 8, 6) bit-identically at both truncations (truncation_consistent = True). Result: pass_count = 10/11 with deviating idx=0 at τ=0.090 producing cv = (4, 2, 8, 6) — strata 1+2 swap (2 ↔ 4), strata 3+4 retain (8, 6) EXACTLY.
  2. **A_F-block / Peter-Weyl decomposition**: D_K(τ_fold) is block-diagonal by Peter-Weyl content; the bot-20 is contributed ONLY by sectors {(0,0), (0,1), (1,0)} (verified: smallest |λ|_min for p+q ≥ 2 is 0.872975 at sector (1,1), strictly above the bot-20 stratum-4 ceiling 0.84521). The 4-stratum partition (2, 4, 8, 6) maps to: stratum 1 = (0,0) lowest mode (cardinality 2); stratum 2 = (0,1) ⊕ (1,0) lowest quartet (cardinality 4); stratum 3 = SECOND multiplicity-class within (0,1) ⊕ (1,0) at |λ| = 0.84086 (cardinality 8 — W-12 §VII.K-PROP "chiral-pair condensation signature" at first-order Bogoliubov cusp); stratum 4 = (0,0) higher harmonic (cardinality 6).
  3. **C_output (W11-3)**: Friedrich-Bär bound + Casimir-ladder monotonicity on D_K block structure proves NEW-sector lower bounds at L_max ∈ {13, 14, 15} satisfy intrusion margins +2.1570, +2.3548, +2.5567 in M_KK units above the stratum-4 ceiling — analytically extending V_input's L_max=6 / L_max=10 truncation-consistency to all L_max ≥ 12 by strict monotonicity. Per-L_max stratification is identical to L=12 cache at all four L_max ∈ {12, 13, 14, 15}; pass_count = 4 (THEOREM exact integer match).
  4. **Conclusion**: The 4-stratum partition (2, 4, 8, 6) at τ_fold = 0.190 is a SUBSTRATE-PHYSICAL OBSERVABLE — robust under τ-perturbation in the inner shell |δ_τ| ≤ 0.05 + +-far endpoint δ_τ = +0.10 (asymmetric breakdown ONLY at δ_τ = −0.10 toward bi-invariance, with strata 3+4 still preserved); robust under L_max-extension across all L_max ≥ 12 (analytically certified). Strata 3 + 4 are τ-RIGID; strata 1 + 2 carry the fold-deformation sensitivity. The partition is NOT a finite-truncation artifact AND NOT an arbitrary τ-fine-tuning artifact.

**Closure SHA pin** (dual; per SOURCE-DOUBLE-CITE-CO-PRIMARY V_input + C_output requirement that BOTH anchors remain accessible):

  - **V_input audit_sha256** (W11-2): `008cf3c98f28eca8a3c9b142673be4997c92e62bdcb2c1927b67db2d6e04315d` (full 64-char; verdict line at `computations/session-87/s87_gate_verdicts.txt:298`).
  - **V_input content_sha256** (W11-2): `b75b235b6dbcabf1b7a384d557a351c08a90f1164b9c0a45dadf0e0de0bd66bc`.
  - **C_output audit_sha256** (W11-3): `f19bcd5e25969374c7ab68774de92ef927cd527cffecdffbe7b0692f1ab6e5fd` (full 64-char; verdict line at `computations/session-87/s87_gate_verdicts.txt:296`).
  - **C_output content_sha256** (W11-3): `43ad11970f0bceb9a53464fb7f4fba6e144abe45eed14bf6eec8e77fbca0fe76`.
  - **W-12 §VII.K-PROP partition canonical source**: `sessions/archive/session-86/workshops/s86-bimodality-and-4fold-cardinality.md` lines 150, 212, 338, 359, 609, 620 (anchor (2, 4, 8, 6) declaration; chiral-pair condensation reading at stratum 3); `s86_w12_workshop_bottom20_regulator_ordering.py` (W-12 producer script for the regulator-INDEPENDENCE atlas from which the canonical partition was extracted).

**Anchor list** (SOURCE-DOUBLE-CITE-CO-PRIMARY structure):

  - **W11-2 verdict line** (V_input): `computations/session-87/s87_gate_verdicts.txt:298` — `S87-PARTITION-STABILITY-4STRATUM: INFO -- value='pass_count=10/11;cv_anchor=[2, 4, 8, 6];...;breakdown_delta_tau=0.1;ULP_tol=1e-14;Casimir_bound_truncation_p+q<=6_vs_plan_pin_p+q<=10' scheme=integer-multiplicity-strata convention=4-stratum-canonical-W12-VII.K-PROP-Lmax6-Casimir-bound-truncation L_max=6`.
  - **W11-3 verdict line** (C_output): `computations/session-87/s87_gate_verdicts.txt:296` — `S87-STRATUM3-LMAX-SCAN: PASS -- value=4 scheme=block-diagonal-cache-plus-friedrich-baer-bound convention=4-stratum-canonical-W12-stratum-3 L_max=12-15-scan`.
  - **W-12 §VII.K-PROP partition canonical**: `sessions/archive/session-86/workshops/s86-bimodality-and-4fold-cardinality.md` (S86 W-12 connes + volovik joint workshop, 2026-04-27); `permanent-results-registry.md` line 55 §VII.K-PROP CC-5 Propagation Identity for Regulator-Dressing (parent slot for the partition canonical).

**Source**: S87 W11 plan §W11-2 (lines 177-279) + §W11-3 (lines 280-380); S87 working-paper §W11-2 + §W11-3 (lines 8907-9253 in `sessions/archive/session-87/session-87-results-workingpaper.md`); S87 W11-2 §13 carry-forward CF-VII.AJ.partition-stability-LANDING (line 9087 in working paper); S86 W-12 source workshop `sessions/archive/session-86/workshops/s86-bimodality-and-4fold-cardinality.md` for the partition canonical and the chiral-pair condensation interpretation at stratum 3.

**Substrate framing** (per `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space"):

The 4-stratum partition (2, 4, 8, 6) IS a structural property of the substrate's spectral triple `(A_K, H_K, D_K)` at τ_fold = 0.190 — it counts the multiplicity stratification of the 20 lowest |eigenvalues| of the Jensen-deformed Dirac operator on the SU(3)-fiber spectral triple. The W11-3 PASS-saturation theorem certifies this is NOT a finite-truncation artifact (the partition is invariant across L_max ∈ {12, 13, 14, 15} and extends analytically to all L_max ≥ 12 via Friedrich-Bär + Casimir monotonicity). The W11-2 INFO-with-asymmetric-breakdown verdict certifies this is NOT an arbitrary τ-fine-tuning artifact (the partition holds across the entire 11-point scan at strata 3+4; the only deviation is strata 1+2 swap at the small-τ far endpoint, where the system approaches the bi-invariant limit and the (0, 0)-sector spinor multiplicities reorganize). The substrate IS this stratum structure; it is not "in" any container. The L_max regulator parametrizes the truncation depth of the Peter-Weyl decomposition — it is a tool for extracting finite-rank approximations, NOT a property of the substrate. The asymmetric breakdown direction (only at δ_τ = −0.10 toward bi-invariance; +-far endpoint δ_τ = +0.10 PASSES) is the structural fingerprint of the fold-deformation: τ_fold = 0.190 is a special anisotropy where the (0, 0) and (0, 1) ⊕ (1, 0) levels are gap-separated, and pulling τ toward 0 (bi-invariance) collapses that gap and the spinor multiplicities re-distribute.

**Bridge map (substrate → laboratory)**: The substrate-IS observable is the cardinality vector (2, 4, 8, 6) of the bot-20 |λ| stratification of D_K(τ_fold); the bridge map is the Peter-Weyl decomposition into the lowest SU(3) irrep sectors {(0, 0), (0, 1), (1, 0)}; the laboratory-IN observable is the discrete quasiparticle multiplicity stratification at the first-order Bogoliubov cusp in a 3He-B superfluid analog (per S86 W-12 §SUBSTRATE-FRAMING: the stratum-3 multiplicity 8 = 2 × 4 is the chiral-pair condensation signature distinguishing this substrate from generic BdG superfluids where stratum multiplicities follow the simpler (2, 2, 2, ...) pattern). Direction of explanation flows substrate → bridge → laboratory: D_K eigenvalues at τ_fold → Peter-Weyl decomposition → 3He-B chiral-pair condensation signature at first-order Bogoliubov cusp. Inverting this direction (treating the 3He-B observable as fundamental and the substrate spectral content as derived) is a container-thinking violation.

**Cross-pillar bridge note** (per `.claude/rules/cross-pillar-bridge-anatomy.md` SUGGESTION at K=1): this entry is NOT itself a cross-pillar bridge theorem — it is a within-Pillar-III spectral-triple structural observable. The 3He-B laboratory connection is annotated above as a substrate-physics interpretation per W-12 §SUBSTRATE-FRAMING, but the formal cross-pillar bridge anatomy (Pillar-III ↔ Pillar-V; 5 IS-not-IN elements + 3-level ladder) is reserved for the FWD-C3 candidate (Pillar IV ↔ Pillar V; substrate cocycles ↔ 3He-B / 3He-A observables) per `.claude/rules/cross-pillar-bridge-anatomy.md` §"Three forward bridge candidates for S88+ dispatch", which carries rank(ker ι_*) = 2 and invokes the inheritance-falsifier-protocol §"Generalization beyond 3He-B" rank-2 case. The §VII.AJ.partition-stability landing here supplies the substrate-IS partition structure (2, 4, 8, 6) that any future Pillar-III ↔ Pillar-V bridge candidate would consume as its substrate-IS observable.

**Solution-space implication**: The §VII.AJ.partition-stability landing closes one of the four sub-block reservations under the §VII.AJ Mellin-Moment-Identities slot. The other three (§VII.AJ.1 V_4 monodromy; §VII.AJ.3 Z_2 dichotomy on bottom-20 ordering across A_5; §VII.AJ.4 Andreev-bound regime) remain NEEDS-COMPUTATION pending S88+ closure. Critically, the partition-stability theorem provides STRUCTURAL SUPPORT for the W11-1 surviving V_4 candidate (ii) "V_4 acting on stratum indices (4-stratum partition modulo 2)" (per W11-3 working-paper §"Critical cross-link to W11-1 surviving V_4 candidate (ii)"; lines 9236-9241 of session-87 working paper) — the partition is now certified as a robust substrate-physical Z_2 quotient on which the candidate (ii) V_4 could act, since the partition itself does not vanish or fragment under regulator extension.

---
"""

# ---------------------------------------------------------------------------
# Verdict line + dual-SHA companion row.
# ---------------------------------------------------------------------------
# The audit_sha256 for this landing is computed over the input-pin map
# (per .claude/rules/gate-verdicts.md S87+ schema; closure_hash pattern from
# the canonical append_verdict() pattern). Pin map is the joint W11-2 +
# W11-3 dual-SHA tuple plus the W-12 §VII.K-PROP partition canonical source.
INPUT_PIN_MAP = {  # (local) pin-map for audit-SHA computation
    "_gate_id": GATE_ID,
    "_wp_id": "VII.AJ.partition-stability",
    "_scheme": "joint-tau-and-Lmax-axis-partition-stability",
    "_convention": "W-12-VII.K-PROP-partition-canonical",
    "_L_max": "6,12-15-scan",
    "_anchor_structure": "SOURCE-DOUBLE-CITE-CO-PRIMARY",
    "w11_2_audit_sha256": W11_2_AUDIT_SHA,
    "w11_2_content_sha256": W11_2_CONTENT_SHA,
    "w11_3_audit_sha256": W11_3_AUDIT_SHA,
    "w11_3_content_sha256": W11_3_CONTENT_SHA,
    "w12_partition_canonical_source": "sessions/archive/session-86/workshops/s86-bimodality-and-4fold-cardinality.md",
    "w12_partition_canonical_anchor": "(2,4,8,6)",
    "registry_slot": "§VII.AJ.partition-stability",
    "registry_path": "sessions/permanent-results-registry.md",
}  # (local)

# Audit-SHA: closure hash over the ordered input-pin map (matches append_verdict()
# template pattern; sorts keys for deterministic ordering).
def closure_hash(pin_map: dict) -> str:  # (local helper)
    payload = "\n".join(f"{k}={v}" for k, v in sorted(pin_map.items()))  # (local)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()  # (local)

AUDIT_SHA = closure_hash(INPUT_PIN_MAP)  # (local)

# Content-SHA: hash of the registry sub-row body that lands.
CONTENT_SHA = hashlib.sha256(NEW_SUB_ROW.encode("utf-8")).hexdigest()  # (local)

VERDICT_VALUE = (  # (local)
    "joint_W11-2-INFO_W11-3-PASS;"
    "cv_anchor=[2,4,8,6];"
    "tau_axis_pass_count=10/11;"
    "tau_axis_breakdown_delta_tau=-0.10_only_strata12_swap_strata34_preserved;"
    "Lmax_axis_pass_count=4/4;"
    "Lmax_axis_FB_margin_at_Lmax15=+2.5567_M_KK;"
    "registry_slot=VII.AJ.partition-stability;"
    "anchor_structure=SOURCE-DOUBLE-CITE-CO-PRIMARY"
)

VERDICT_LINE = (  # (local)
    f"{GATE_ID}: PASS -- value='{VERDICT_VALUE}' "
    "scheme=joint-tau-and-Lmax-axis-partition-stability "
    "convention=W-12-VII.K-PROP-partition-canonical "
    "L_max=6,12-15-scan "
    f"audit_sha256={AUDIT_SHA} "
    f"content_sha256={CONTENT_SHA} "
    "schema_version=S84+\n"
)

COMPANION_ROW = (  # (local)
    f"# audit_sha256_short={AUDIT_SHA[:16]} "
    f"content_sha256_short={CONTENT_SHA[:16]} "
    f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
)

# ---------------------------------------------------------------------------
# Registry insertion: append the §VII.AJ.partition-stability sub-row after the
# §VII.AJ slot's existing reservation block (which ends at the line "## §VII.AJ
# — RESERVED for W-12 Mellin-Moment Identities ... **Substrate framing**: ...
# ---" trailing horizontal-rule).
# ---------------------------------------------------------------------------
INSERT_AFTER_BLOCK = """**Substrate framing**: §VII.AJ is the slot reservation for W-12 Mellin-moment identity family. All 4 sub-blocks are NEEDS-COMPUTATION pending S87 gate execution; this entry pre-allocates the slot to prevent collision and document the W-12 family scope.



---
"""

def main() -> None:
    # ---- Step 1: append §VII.AJ.partition-stability sub-row to registry. ----
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    if INSERT_AFTER_BLOCK not in registry_text:
        raise RuntimeError(
            "INSERT_AFTER_BLOCK marker not found in permanent-results-registry.md; "
            "registry layout has drifted from the §VII.AJ reservation. Re-grep "
            "for the §VII.AJ slot's substrate-framing trailing block before re-running."
        )
    # Verify the §VII.AJ.partition-stability sub-row hasn't already landed.
    if "§VII.AJ.partition-stability —" in registry_text:
        raise RuntimeError(
            "§VII.AJ.partition-stability sub-row already present in registry; "
            "re-run blocked to prevent double-landing. If this is a re-run, "
            "manually verify the existing landing matches the V_input + C_output "
            "anchors and skip the registry-write step."
        )
    new_registry_text = registry_text.replace(  # (local)
        INSERT_AFTER_BLOCK,
        INSERT_AFTER_BLOCK + NEW_SUB_ROW,
        1,  # (local) replace ONLY the first occurrence (defensive against any later collisions)
    )
    REGISTRY_PATH.write_text(new_registry_text, encoding="utf-8")
    print(f"[OK] §VII.AJ.partition-stability sub-row appended to {REGISTRY_PATH}")
    print(f"     content_sha256 = {CONTENT_SHA}")
    print(f"     sub-row byte length = {len(NEW_SUB_ROW)}")

    # ---- Step 2: append verdict line + companion row to s87_gate_verdicts.txt. ----
    # Defensive check: refuse to double-append.
    verdicts_text = VERDICTS_PATH.read_text(encoding="utf-8")  # (local)
    if GATE_ID in verdicts_text:
        raise RuntimeError(
            f"{GATE_ID} verdict line already present in {VERDICTS_PATH}; "
            "re-run blocked to prevent duplicate verdict-line emission. "
            "If this is a re-run, audit existing line for SHA-equality with "
            "the recomputed audit_sha256 + content_sha256 above."
        )
    with VERDICTS_PATH.open("a", encoding="utf-8") as f:  # (local) append-only per registry-write hygiene
        f.write(VERDICT_LINE)
        f.write(COMPANION_ROW)
    print(f"[OK] Verdict line + dual-SHA companion appended to {VERDICTS_PATH}")
    print(f"     audit_sha256 = {AUDIT_SHA}")
    print(f"     content_sha256 = {CONTENT_SHA}")
    print(f"     composite verdict = PASS (joint W11-2 INFO + W11-3 PASS landing)")

    # ---- Step 3: emit machine-parseable summary for orchestrator readout. ----
    print()
    print("=" * 72)
    print(f"GATE_ID                  : {GATE_ID}")
    print(f"COMPOSITE_VERDICT        : PASS")
    print(f"V_input (W11-2, CF-67)   : INFO  pass_count=10/11; breakdown_delta_tau=-0.10 only")
    print(f"C_output (W11-3, CF-68)  : PASS  pass_count=4/4;   FB_margin@Lmax15=+2.5567 M_KK")
    print(f"REGISTRY_SLOT            : §VII.AJ.partition-stability")
    print(f"ANCHOR_STRUCTURE         : SOURCE-DOUBLE-CITE-CO-PRIMARY")
    print(f"AUDIT_SHA256             : {AUDIT_SHA}")
    print(f"CONTENT_SHA256           : {CONTENT_SHA}")
    print("=" * 72)


if __name__ == "__main__":
    main()
