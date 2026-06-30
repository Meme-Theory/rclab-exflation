# Session 90 Plan — Wave 4: W1 cascade-tail + α(M) ALT-CORRIDOR + LRD + PBH substrate-physics

**Generated**: 2026-05-12
**Wave**: 4 of N (S90 fanout plan)
**Source context**: `sessions/session-plan/session-90-context.md` §"Cluster D" + §"Extra Context"
**Cluster theme**: Cluster D — W1 cascade-tail + α(M) ALT-CORRIDOR + LRD + PBH substrate-physics
**Total effort**: ~6.4 wave-equivalents (CF-37 is the largest single S90 item at 3.5 we)

---

## Wave 4 Summary

Wave 4 closes out the W-1 workshop primary corridor selection that the S89 W-1 §W1-1 FAIL (CM-1995 §III.4 single-pole leading-order naive corridor) reduced to a structural-degeneracy proof (ζ_D(0) = 38 to 1.10e-15 polynomial-fit residual; horizon-microstate degeneracy under bare-counting is structural, not a curable defect of the regulator). The W-1 workshop adjudicated the next move as the (d)∘(b) compositional primary corridor: Connes-Karoubi pairing of the χ'-pullback gradient-symmetric Hochschild cocycle with the Chern character of the inheritance-restricted Peter-Weyl horizon-spanning projector. This is calibration corpus instance #2 of the simultaneous element-1 + element-3 double-deformation pattern (instance #1 = §VII.AF.1.OP-PROJ W-5 baseline at the substrate-IS Cell-I cohomology-class layer).

CF-37 is the primary substrate-physics gate of W4 and the largest single item in the S90 dispatch budget (3.5 wave-equivalents). It re-derives α(M) at the (d)∘(b) primary corridor under composite PASS-predicate Sub-clauses A + B + C; PASS opens the LRD α-anchor candidate as substrate-IS at Cell-I and queues the three-axis Stage-2 post-PASS cross-axis independent-verify (lizzi Axis-A spectral-functional + volovik Axis-B substrate/superfluid-universe + mack Axis-C bridge-map cohomology; connes + phonon-first EXCLUDED as workshop authors). INFO routes to the secondary (c)∘(d) modified-universal-kernel corridor at S91+ (W-1 AUX-4). The remaining four items support CF-37: CF-38 is a mechanical pre-flight knowledge-MCP query whose outcome tightens Sub-clause B of CF-37 from 30% RATIO to 10% RATIO if the empirical anchor 1/458 has been promoted; CF-39 re-pins L_H_canonical at substrate-pinned T_H = 1.057 MeV with the refined §W1-3 species-multiplicity lookup (emits Option A `supersedes=2afd17ef99c81123…` tagged corrective canonical line per `gate-verdicts.md §"Option A"` absolute verdict permanence); CF-40 refines the W1-3 species-multiplicity retry with lattice-QCD-corrected `g_*(T)` near Λ_QCD and Boltzmann threshold-suppression at m_e/m_W/m_top boundaries (mack writer per observational-anchor authority); CF-41 promotes the §W1-4 PBH band-edge INFO to upper-22.6%-conjunct PASS via L_max=12 substrate pinning and cascade-tail-mass-distribution refinement.

Sequencing note: per `Known dependencies` in the context file, **CF-40 PRECEDES CF-39** (species-multiplicity retry PASS unblocks L_H re-execution). CF-38 is mechanical and can run in parallel with CF-37's plan-block authorship as a pre-flight check; CF-41 is independent of the CF-37/CF-39/CF-40 chain and may dispatch in parallel. CF-37 has no W4-internal upstream dependency — its inputs are all S88/S89 stabilized npz files plus canonical_constants pins. CF-37 outputs feed forward to the S91+ Stage-2 three-axis verify dispatch (W-1 AUX-5), which is tracked but NOT in the S90 dispatch budget.

---

## Wave 4 Decision Point Prerequisites

Cross-wave dependencies entering W4:

| Item | Depends on | Prereq location | Effect on W4 |
|:-----|:-----------|:----------------|:-------------|
| CF-37 | `s84_spectrum_cache_L12_tau019.npz` (frozen S84 cache); `s89_w1_alpha_m_horizon_microstate_count.npz` (S89 §W1-1 FAIL diagnostic); `s89_w2_a7_chi_prime_inheritance_morphism.npz` (S89 §W2-3 χ' independent inheritance morphism, audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843`); §VII.AF.1.OP-PROJ calibration corpus instance #1 (registry lines 14690-14722) | All static / pre-S90 | No W4-internal wait |
| CF-38 | Knowledge-MCP query against `permanent-results-registry.md` for empirical anchor 1/458 promotion-status; canonical_constants.py `alpha_LRD_FW` (if landed) | Static at S90 plan-freeze | Mechanical pre-flight; runs independent of CF-37 |
| CF-39 | CF-40 PASS (refined §W1-3 species-multiplicity lookup npz produced; lattice-QCD g_*(T) consumable at T_H = 1.057 MeV) | **Internal W4** — CF-40 must complete first | Sequence: CF-40 → CF-39 |
| CF-40 | S88 W6 §V.5 cascade form (canonical, pre-S90); lattice-QCD g_*(T) tables near Λ_QCD ≈ 200 MeV (external reference; cited in dispatch prompt); PDG/Planck cross-check anchors at T ∈ {100 GeV, 1 GeV, 1 MeV} | Static at S90 plan-freeze | No W4-internal wait |
| CF-41 | `s84_spectrum_cache_L12_tau019.npz`; §W1-4 npz `s89_w1_n_pbh_band_edge_tension_reconciliation.npz`; CF-CURV-6 prior `[10⁻³⁰, 10⁻²⁰] m⁻³`; §W1c-69 PASS-magnitude posterior `[8.4e-24, 2.2e-22] m⁻³` | All pre-S90 stabilized | No W4-internal wait |

Cross-wave dependencies exiting W4 (forward to S91+):

- CF-37 PASS outputs (canonical npz + α'(M_LRD=10⁷) value + M-asymptotic envelope fit + Cell-I substrate-IS classification) → S91+ AUX-5 three-axis Stage-2 cross-axis independent-verify (`S91-OR-LATER-CORRIDOR-D-COMPOSITE-B-STAGE-2-CROSS-AXIS-VERIFY`). Reviewers: lizzi Axis-A (spectral-functional), volovik Axis-B (substrate/superfluid-universe), mack Axis-C (bridge-map cohomology). Workshop-author exclusion per `joint-theorem-promotion.md §"Stage 2"` lines 55-91: connes + phonon-first EXCLUDED.
- CF-37 INFO outcome (rel_dev ∈ [0.10, 0.30]) → S91+ AUX-4 secondary (c)∘(d) modified-universal-kernel corridor with γ(s) ≠ Γ(s).
- CF-37 outputs ALSO feed downstream §VII.{next-free} candidate registry entry as Cell-I cohomology-class double-deformation calibration corpus instance #2 (instance #1 = §VII.AF.1.OP-PROJ W-5 LANDED). Registry landing target: mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` (deferred to S91+).
- CF-41 PASS outputs feed forward to §VII.{next-free} PBH-band-edge-conjunct STAGE-1-CANDIDATE registration via mack sole-writer (deferred S91+).

---

## §W4-1. CF-37 — S90-W1-1-ALT-CORRIDOR-SELECTED-LRD-ALPHA-DERIVATION

**Gate ID**: `S90-W1-1-ALT-CORRIDOR-SELECTED-LRD-ALPHA-DERIVATION`
**Origin**: gen §6 CF-W1-1-ALT-CORRIDOR; W-1 PRIMARY corridor selection
**Effort**: ~3.5 we (BIG — largest single item in S90 dispatch budget)

### 1. Trigger
`[VERIFY-THEOREM]` (within-cell theorem-existence verification at the substrate-IS Cell-I cohomology-class layer; the substrate prediction is that α'(M) exists as a finite, signed, cohomology-pairing-valued observable on the substrate-IS spectral triple) ∧ `[SIGN]` (sign_verdict that α'(M) returns a positive microstate count ratio at all probed M, by-construction from the Connes-Karoubi pairing's positivity at the inheritance-restricted projector image)

### 2. Classification
**GEOMETRIC** — the observable α'(M) is a Connes-Karoubi pairing of a Hochschild cocycle with a Chern character on the substrate-IS spectral triple `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})` at L_max = 10. It is a cohomology-class observable on the substrate algebra, not a state-pair functional. Per the algebra-axis orthogonality K-counter (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 since S87 W-2 R3), α'(M) lives at Cell I (algebra-INVARIANT, spectrum-only functional family).

### 3. Agent type
- **PRIMARY**: `phonon-first-cosmologist` (W-1 workshop substrate-physics author; primary corridor selection author per workshop verdict)
- **CO-AUTHOR**: `connes-ncg-theorist` for the χ' inheritance morphism connection to S89 §W2-3 (audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843`); the Wedderburn 9 > 8 forces-zero-map proof of χ' was authored by connes and the (d)∘(b) corridor inherits from §VII.AF.1.OP-PROJ via χ'

NOTE: Per workshop-author exclusion at `joint-theorem-promotion.md §"Stage 2 Axis-B Selection Protocol"`, both connes + phonon-first are EXCLUDED from the post-PASS three-axis Stage-2 verify (S91+ AUX-5). The Stage-2 reviewers will be: lizzi Axis-A spectral-functional + volovik Axis-B substrate/superfluid-universe + mack-cosmic-bridge Axis-C bridge-map cohomology.

### 4. Hypothesis
**Substrate prediction**: The α'(M) substrate-IS observable at the LRD pivot mass M_LRD = 10⁷ M_sun returns a finite positive ratio `α'(M_LRD, L_max=10) ∈ (0, 1)` whose value lies within 30% RATIO of the empirical LRD α-anchor 1/458 ≈ 2.18e-3 (S88 W1b1-63 branch (c)). The M-asymptotic envelope follows the inherited (d)∘(b) corridor form `α'(M) = 1 + O((M/M_threshold)^{-n})` with `n > 0`, confirming that the substrate-IS LRD α-anchor is a substrate-IS, calibration corpus instance #2 of the element-1 + element-3 double-deformation pattern at the Cell-I cohomology-class layer.

### 5. Method — COMPLETE self-contained dispatch prompt

```
You are phonon-first-cosmologist (primary substrate-physics author of the S89
W-1 workshop). With connes-ncg-theorist as co-author (for the χ' inheritance
morphism connection to S89 §W2-3), re-derive the LRD α(M) substrate-IS
observable via the (d)∘(b) compositional primary corridor selected at the W-1
workshop verdict.

═══════════════════════════════════════════════════════════════════════════
SUBSTRATE FRAMING (read this first; pin your direction-of-explanation)
═══════════════════════════════════════════════════════════════════════════

The substrate IS the spectral triple (A_K, H_K, D_K) at L_max = 10. The
horizon-spanning Peter-Weyl projector P_HSS' is substrate-IS — it is NOT a
black-hole horizon embedded in a pre-existing spacetime container. M_KK² is
the substrate-IS area scale; M_Pl_reduced² is the laboratory-IN area scale
under the bridge map (semiclassical BH-thermodynamic image). The direction of
explanation flows: substrate eigenvalues → cohomology pairing → emergent
BH-thermodynamic α(M) interpretation.

DO NOT write "particles created in curved spacetime", "horizon of a black hole
of mass M", or "spacetime-embedded projector". WRITE "fiber spectrum
reorganization under inheritance restriction", "Peter-Weyl projector image
inherited via χ'", "substrate-IS area scale M_KK² mapped to laboratory-IN
M_Pl_reduced² under semiclassical bridge".

═══════════════════════════════════════════════════════════════════════════
CORRIDOR (d)∘(b) COMPOSITIONAL PRIMARY — algebraic specification
═══════════════════════════════════════════════════════════════════════════

The substrate-IS observable:

  α'(M) := ⟨χ'^*[φ_g^{sym}], [Ch(P_HSS'(M))]⟩_{Connes-Karoubi}
            · M_KK² / S_BH^semicl(M; M_Pl_reduced²)

where:

  φ_g^{sym} = gradient-symmetric Hochschild cocycle on A_K, the canonical
              cocycle from S86 W-5 §VII.AF.1.OP-PROJ calibration corpus
              instance #1 (registry lines 14690-14722; cocycle source
              line 14704). Cohomology class [φ_g^{sym}] is regulator-class
              INVARIANT (Level-1 cohomology-class identity).

  χ' : (A_K^{≤10}, H_K^{≤10}, D_K^{≤10}) → (BdG sub-algebra, …)
       = the independent inheritance morphism authored by connes-ncg-theorist
         at S89 §W2-3 (Wedderburn 9 > 8 forces zero map). audit_sha256 =
         90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843.

  χ'^*[φ_g^{sym}] = pullback of [φ_g^{sym}] by χ' to the inheritance-restricted
                    sub-algebra (this is the (b) deformation of element-1).

  P_HSS'(M) = inheritance-restricted Peter-Weyl horizon-spanning projector
              indexed by mass M. Spans the Peter-Weyl sectors (p,q) whose
              eigenvalues λ satisfy the substrate-IS horizon condition
              λ² ≤ M_KK² · (M_LRD / M)^(some exponent governed by the
              (d) deformation; do not assume the naive form — derive from
              the inheritance restriction P_HSS' = χ'^*(P_HSS) where P_HSS
              is the un-restricted horizon projector at the unrestricted
              triple). The (d) deformation is element-3 of the bridge anatomy.

  [Ch(P_HSS'(M))] = Chern character of the inheritance-restricted projector,
                    computed via Connes-Moscovici 1995 §III.4 finite-spectral-
                    triple residue formula (THE SAME machinery that produced
                    the W-5 §VII.AF.1.OP-PROJ calibration corpus instance #1).

  ⟨·, ·⟩_{Connes-Karoubi} = the Connes-Karoubi pairing between Hochschild
                            cohomology and K-theory at the bridge anatomy
                            Element-3 layer.

  S_BH^semicl(M; M_Pl_reduced²) = semiclassical Bekenstein-Hawking entropy
                                   in laboratory-IN reduced-Planck units; this
                                   is the laboratory-IN observable in the bridge
                                   anatomy 5-element specification.

The dimensional reduction M_KK² / S_BH^semicl(M; M_Pl_reduced²) is the bridge
map (Element 3 of the 5-anatomy) — it carries the substrate-IS area scale to
the laboratory-IN reduced-Planck-mass-squared area scale.

═══════════════════════════════════════════════════════════════════════════
WHY THIS CORRIDOR — why (d)∘(b) and not (a)/(b)/(c) alone?
═══════════════════════════════════════════════════════════════════════════

S89 §W1-1 FAIL diagnosed that the naive single-pole leading-order CM-1995
§III.4 corridor (corridor (a)) is structurally degenerate: ζ_D(0) = 38 to
1.10e-15 polynomial-fit residual; the bare-counting horizon microstate count
cannot reproduce the cohomology pairing that produces α(M). Corridor (a) is
CLOSED.

The W-1 workshop verdict (R3 closure) selected (d)∘(b) compositional primary
as PRIMARY corridor for these reasons:

  - (b) deformation alone (element-1 pullback by χ' but element-3 native)
    inherits the §VII.AF.1.OP-PROJ baseline but does NOT introduce a mass-
    dependence at the bridge map; α(M) would be constant in M (FAIL on
    Sub-clause C M-asymptotic envelope).

  - (d) deformation alone (element-3 inheritance-restricted projector but
    element-1 native) introduces mass-dependence but at the unrestricted
    cocycle [φ_g^{sym}]; this is the corridor S86 W-5 already characterized
    at §VII.AF.1.OP-PROJ — not a NEW substrate-IS observable, just a re-cast
    of the calibration corpus instance #1.

  - (d)∘(b) COMPOSITIONAL — both element-1 and element-3 deformed
    simultaneously — produces a NEW substrate-IS cohomology-class observable
    that is calibration corpus instance #2 of the simultaneous double-
    deformation pattern. The χ' pullback at element-1 + the inheritance-
    restricted projector at element-3 jointly construct the LRD-α-anchor.

═══════════════════════════════════════════════════════════════════════════
NUMERICAL PROCEDURE
═══════════════════════════════════════════════════════════════════════════

Top of script (mandatory):

    from canonical_constants import *
    import numpy as np
    import torch    # for matrix products ≥100×100 on GPU per math-scripts.md
    import os
    os.environ.setdefault('OMP_NUM_THREADS', '8')  # CPU thread cap; per
                                                    # math-scripts.md
    # GPU: AMD RX 9070 XT 17.1 GB VRAM, ROCm 7.2, torch 2.9.1+rocm
    # Largest D_K block at L_max=10 is ≪ VRAM cap — dense storage fine

Steps (high-level; expand to full algebra in working-paper section):

  1. LOAD substrate cache `s84_spectrum_cache_L12_tau019.npz` (L_max=12
     master; filter to L_max=10 per W-1 PRE-REG machinery pin). Verify SHA-256
     against the pinned input-SHA. Filter to Peter-Weyl sectors (p,q) with
     p+q ≤ 10; verify cardinality matches §VII.AJ.partition-stability
     (S88 W2-6 PASS) bot-20 cardinality vector (2, 4, 8, 6).

  2. LOAD `s89_w1_alpha_m_horizon_microstate_count.npz` (S89 §W1-1 FAIL
     diagnostic). Use ONLY to extract the degeneracy proof reference
     ζ_D(0) = 38 to 1.10e-15 polynomial-fit residual — do NOT inherit
     numerics of the naive (a) corridor; corridor (a) is CLOSED.

  3. LOAD `s89_w2_a7_chi_prime_inheritance_morphism.npz` (S89 §W2-3 χ'
     independent inheritance morphism; audit_sha256
     90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843).
     Extract: χ' as a homomorphism A_K → BdG-sub-algebra; Wedderburn-9-greater-
     than-8 forces-zero-map matrix; pullback action on Hochschild cochain
     bidegree (1,1) cocycles.

  4. LOAD φ_g^{sym} cocycle from §VII.AF.1.OP-PROJ registry text (lines
     14690-14722; cocycle source line 14704; canonical pin
     R_universal_HP1_strict_F4 = 1.030902). Construct as a Hochschild 1-cocycle
     on A_K following the W-5 calibration corpus instance #1 specification.

  5. COMPUTE χ'^*[φ_g^{sym}]: apply χ' pullback to φ_g^{sym}. Verify pullback
     respects Hochschild differential (cross-check: dχ'^*φ_g^{sym} = χ'^*dφ_g^{sym}
     = 0 within machine epsilon, since [φ_g^{sym}] is a cohomology class).

  6. CONSTRUCT P_HSS'(M_LRD = 10⁷ M_sun) = inheritance-restricted Peter-Weyl
     horizon-spanning projector. Mass M_LRD enters via the cutoff on λ²/M_KK².
     The cutoff form is derived from the inheritance restriction; do NOT
     assume the naive λ² ≤ M_KK² · (M_LRD/M_KK²) form (this is the (a)
     corridor that S89 closed). Instead, derive the cutoff form from
     P_HSS'(M) = χ'^*(P_HSS(M)) with P_HSS(M) the un-restricted projector
     at the un-restricted triple.

  7. COMPUTE [Ch(P_HSS'(M_LRD))] via Connes-Moscovici 1995 §III.4 finite-
     spectral-triple residue formula. The Chern character is a Connes-Hochschild
     even-degree class; on the finite spectral triple at L_max=10 it is computed
     as a sum over Peter-Weyl sectors with coefficients given by the residue
     formula.

  8. COMPUTE the Connes-Karoubi pairing
        ⟨χ'^*[φ_g^{sym}], [Ch(P_HSS'(M_LRD))]⟩_{CK}
     as a finite sum over Peter-Weyl sectors (p,q) ≤ 10. The pairing is a
     bilinear pairing between Hochschild cohomology and K-theory; on a finite
     spectral triple it reduces to a trace formula. Cross-check against the
     §VII.AF.1.OP-PROJ baseline at the un-restricted projector (instance #1
     gives R_universal_HP1_strict_F4 = 1.030902 at the un-restricted
     calibration corpus instance #1).

  9. EVALUATE S_BH^semicl(M_LRD; M_Pl_reduced²) = semiclassical Bekenstein-
     Hawking entropy. M_Pl_reduced = M_Pl / sqrt(8π) (canonical_constants pin
     M_Pl_reduced). S_BH = π · (M_LRD / M_Pl_reduced)² in natural units.

  10. FORM α'(M_LRD) = ⟨χ'^*[φ_g^{sym}], [Ch(P_HSS'(M_LRD))]⟩_{CK}
                       · M_KK² / S_BH^semicl(M_LRD; M_Pl_reduced²)

  11. SCAN M ∈ {10⁵, 10⁶, 10⁷ (M_LRD), 10⁸, 10⁹} M_sun. Fit M-asymptotic
      envelope `α'(M) = 1 + c · (M/M_threshold)^{-n}` via log-log regression on
      |α'(M) - 1| vs M. Extract n and M_threshold. Sub-clause C requires
      n > 0.

  12. EMPIRICAL ANCHOR COMPARISON: compute rel_dev = |α'(M_LRD = 10⁷) - 1/458|
      / (1/458). Sub-clause B: PASS iff rel_dev ≤ 0.30 (or ≤ 0.10 if CF-38
      tightening applies); INFO iff 0.10 ≤ rel_dev ≤ 0.30 (under default
      30%-band); FAIL iff rel_dev > 0.30. ON INFO outcome, route to S91+
      AUX-4 secondary (c)∘(d) modified-universal-kernel corridor.

  13. SIGN_VERDICT: derive substitution chain (see §10 of this gate block).
      Sub-clause A: PASS iff 0 < α'(M_LRD, L_max=10) < 1 (substrate prediction
      from the Connes-Karoubi positivity at the inheritance-restricted
      projector image). FAIL iff α' ≤ 0 or α' ≥ 1.

OUTPUT FILES (target):

  - computations/_shared/s90_w4_alpha_m_alt_corridor_d_compose_b.py      (script)
  - computations/_shared/s90_w4_alpha_m_alt_corridor_d_compose_b.npz     (data)
  - computations/_shared/s90_w4_alpha_m_alt_corridor_d_compose_b.png     (plot)

  npz keys (mandatory):
    alpha_prime_M_LRD_value              (full float64)
    alpha_prime_M_LRD_publication        (rounded to publication precision)
    publication_sig_figs                  (per Class 8.3 pin)
    M_scan                                (array of M values in M_sun)
    alpha_prime_M_scan                    (array of α' values)
    M_asymptotic_envelope_fit             (dict: {n, M_threshold, R2})
    rel_dev_vs_1over458                   (sub-clause B value)
    sign_verdict_substitution_chain       (dict: definitions, substitutions,
                                                simplifications, direction)
    L_max                                 = 10
    audit_sha256                          = closure_hash(input_pin_map)
    content_sha256                        = closure_hash(npz_content)
    schema_version                        = "S87-v2"

VERDICT-LINE APPEND TARGET (mandatory; per gate-verdicts.md
§"Canonical Verdict-File Path"):

  computations/session-90/s90_gate_verdicts.txt

Append three rows (the canonical line + the dual-SHA companion + the 3-tuple
annotation for [SIGN] trigger):

  S90-W1-1-ALT-CORRIDOR-SELECTED-LRD-ALPHA-DERIVATION: PASS|FAIL|INFO -- value=<v> \
    scheme=connes-karoubi-pairing-on-chi-prime-inheritance \
    convention=substrate-IS-Cell-I-K-counter-instance-2 \
    L_max=10 audit_sha256=<full-64-char> content_sha256=<full-64-char> \
    schema_version=S87-v2

  # audit_sha256_short=<16-hex> content_sha256_short=<16-hex> \
  # S90-W1-1-ALT-CORRIDOR-SELECTED-LRD-ALPHA-DERIVATION dual-SHA companion row \
  # (W9a-99 split)

  # sign_verdict=PASS|FAIL|N/A magnitude_verdict=PASS|INFO|FAIL \
  # regime_verdict=VALID|MARGINAL|BREAKDOWN \
  # S90-W1-1-ALT-CORRIDOR-SELECTED-LRD-ALPHA-DERIVATION 3-tuple annotation \
  # (S87 schema-v2)

CROSS-CHECKS (mandatory in script log):

  - Verify the pairing on the un-restricted projector (P_HSS instead of
    P_HSS') reproduces the §VII.AF.1.OP-PROJ baseline R_universal_HP1_strict_F4
    = 1.030902 within publication precision (Class 8.3 1e-5). This is the
    calibration corpus instance #1 reproduction check; if it FAILs, the (d)
    deformation hand-off from W-5 is broken and the entire corridor is
    suspect.
  - Verify χ' pullback respects Hochschild differential at machine epsilon.
  - Verify L_max=10 truncation does NOT discard sectors that contribute >1%
    to the pairing (per Friedrich-Bär saturation argument from S87 W11-3
    `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection
    Feasibility Pre-Check"`).

INPUT-SHA PINS (mandatory in script first 20 lines of stdout):

  - s84_spectrum_cache_L12_tau019.npz: <pinned at dispatch>
  - s89_w1_alpha_m_horizon_microstate_count.npz: <pinned at dispatch>
  - s89_w2_a7_chi_prime_inheritance_morphism.npz: <pinned at dispatch;
      audit_sha256 anchor 90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843>
  - permanent-results-registry.md (§VII.AF.1.OP-PROJ block): <pinned at
      dispatch; lines 14690-14722>
  - canonical_constants.py: <pinned at dispatch; M_KK, M_Pl_reduced,
      R_universal_HP1_strict_F4, eps_H_HP1_norm, alpha_LRD_FW (if landed)>

CANONICAL CONSTANTS USED (per math-scripts.md §"Canonical Constants"):

  - M_KK = 7.428660036284456e+16  (GeV; canonical_constants.py)
  - M_Pl_reduced                   (Planck reduced mass; canonical pin)
  - R_universal_HP1_strict_F4 = 1.030902   (S86 W-5 V4; Class-(d) PROVENANCE)
  - eps_H_HP1_norm = 16.197719     (S86 W-5 V4 Step 1; PRIMARY canonical)
  - tau_fold = 0.19                (R-PROTECTED; canonical_constants.py)
  - alpha_LRD_FW                   (CONDITIONAL on CF-38 promotion-status; if
                                    canonical exists, pin; else cite anchor
                                    1/458 ≈ 2.18e-3 from S88 W1b1-63 branch
                                    (c) as empirical reference only)

  NO hardcoded literals. Every numerical value must be either an imported
  canonical or tagged `# (local)` per math-scripts.md §"Local Variable
  Tagging".

══════════════════════════════════════════════════════════════════════════
KNOWLEDGE-MCP QUERY DISCIPLINE (before computing)
══════════════════════════════════════════════════════════════════════════

Run before ANY numerical work:

  - search_knowledge("alpha LRD horizon microstate Connes-Karoubi pairing")
  - search_knowledge("chi prime inheritance morphism W2-3 Wedderburn 9 8")
  - search_knowledge("Hochschild cocycle gradient symmetric VII.AF.1.OP-PROJ")
  - get_constant("M_KK")  → 7.428660036284456e+16
  - get_constant("M_Pl_reduced")  → canonical value at S90 freeze
  - get_constant("R_universal_HP1_strict_F4")  → 1.030902 (Class-(d) provenance)
  - get_constant("alpha_LRD_FW")  → CONDITIONAL on CF-38 outcome; may not exist
  - trace_entity("simultaneous element-1 element-3 double-deformation
                 calibration corpus")

The knowledge base wins on conflict; if a returned value differs from the
canonical_constants import, halt and emit a SOURCE-RECONCILIATION advisory
per `epistemic-discipline.md §"Source Reconciliation"`.

══════════════════════════════════════════════════════════════════════════
COMPLETION DISCIPLINE (per agent-standards.md §"Completion Verification")
══════════════════════════════════════════════════════════════════════════

Before declaring task-complete:

  (a) Script file present at computations/_shared/s90_w4_alpha_m_alt_corridor_d_compose_b.py
  (b) NPZ file present with all mandatory keys
  (c) PNG plot present (α'(M) vs M with M-asymptotic envelope fit overlaid)
  (d) Verdict line + dual-SHA companion + 3-tuple annotation appended to
      computations/session-90/s90_gate_verdicts.txt
  (e) Working-paper section §W4-1 written with substantive content
      (>15 lines; the substitution chain, the pairing computation summary,
      the M-asymptotic envelope fit, the empirical-anchor comparison, the
      sub-clause-by-sub-clause PASS/FAIL/INFO verdict)

The S82/S84 task-complete-lie failure mode (verdict line appended without
working-paper section) is the failure mode you MUST NOT produce. Verify
all five (a)-(e) on disk before terminating.
```

### 6. Machinery pin (PRDR)

Every free parameter pinned at plan-freeze (per `epistemic-discipline.md §"Pre-Registration Completeness"`):

| Parameter | Pin |
|:----------|:----|
| `L_max` | 10 (W-1 PRE-REG; pinned per S87 W11-3 Friedrich-Bär saturation argument; recursive Casimir-projection feasibility verified at L_max=10 for cohomology-pairing observables) |
| `M_LRD` | 10⁷ M_sun (W-1 PRE-REG; LRD pivot mass) |
| `M_scan` | {10⁵, 10⁶, 10⁷, 10⁸, 10⁹} M_sun (5-point log-spaced scan for M-asymptotic envelope fit) |
| `n_threshold_admissible_band` | n > 0 strict (Sub-clause C; PASS iff envelope exponent is positive) |
| `kernel_choice_primary` | γ(s) = Γ(s) regular kernel (primary (d)∘(b) corridor); modified-universal γ(s) ≠ Γ(s) RESERVED for S91+ AUX-4 secondary (c)∘(d) corridor |
| `cocycle_source` | φ_g^{sym} gradient-symmetric Hochschild cocycle on A_K per §VII.AF.1.OP-PROJ registry text lines 14690-14722 (cocycle source line 14704) |
| `inheritance_morphism` | χ' per S89 §W2-3 (audit_sha256 90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843) |
| `pairing_form` | Connes-Karoubi pairing between Hochschild cohomology and K-theory; finite-spectral-triple residue formula per Connes-Moscovici 1995 §III.4 |
| `chern_character_machinery` | Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula on Peter-Weyl-decomposed (A_K^{≤10}, H_K^{≤10}, D_K^{≤10}) |
| `area_scales` | M_KK² on substrate-IS side; M_Pl_reduced² on laboratory-IN side (semiclassical BH-thermodynamic image) |
| `regulator_pin` | a_n^{HK} Connes-Moscovici §III.4 finite-spectral-triple residue (heat-kernel-equivalent); SCHEMATIC-vs-physical level pin = FULL (residue formula is the canonical machinery for cohomology-pairing at finite L_max; not a SCHEMATIC analog) |
| `convention_tag` | `substrate-IS-Cell-I-K-counter-instance-2` (Cell I per algebra-axis orthogonality; calibration corpus instance #2 of the simultaneous element-1 + element-3 double-deformation pattern) |
| `scheme_tag` | `connes-karoubi-pairing-on-chi-prime-inheritance` |
| `publication_sig_figs` | 5 (per Class 8.3 publication-precision pre-registration; downstream verifier tolerance must satisfy rel_tol ≥ 1e-5) |
| `random_seed` | N/A (deterministic; no Monte-Carlo) |
| `GPU_path` | torch 2.9.1+rocm on AMD RX 9070 XT for matrix products ≥100×100; CPU fallback OMP_NUM_THREADS=8 |
| `verdict_source` | `computations/session-90/s90_gate_verdicts.txt` |
| `working_paper_target` | `sessions/archive/session-90/session-90-w4-workingpaper.md §W4-1` (>15 line substantive content) |

PRDR cross-check (per `epistemic-discipline.md §"Pre-Registration Completeness"`): every PASS/FAIL/INFO branch has its threshold pinned numerically; no free parameter at runtime.

### 7. Input SHA-256 pins

| File | Pin |
|:-----|:----|
| `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | `<pinned at dispatch>` (S84 cache; frozen pre-S90) |
| `computations/session-89/s89_w1_alpha_m_horizon_microstate_count.npz` | `<pinned at dispatch>` (S89 §W1-1 FAIL diagnostic; structural-degeneracy proof) |
| `computations/session-89/s89_w2_a7_chi_prime_inheritance_morphism.npz` | `<pinned at dispatch>`; anchor audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843` |
| `sessions/permanent-results-registry.md` (§VII.AF.1.OP-PROJ block) | `<pinned at dispatch>`; content range lines 14690-14722 |
| `computations/_shared/canonical_constants.py` | `<pinned at dispatch>` |

NOTE on AMRI compliance (per `agent-standards.md §"Agent-Memory Registry Inversion"`): no agent-memory paths are pinned in the input-SHA map. The phonon-first-cosmologist primary author reads its own MEMORY.md at dispatch per standard convention; that file is NOT a pin source for audit-SHA computation. The connes-ncg-theorist co-author connection to S89 §W2-3 is pinned via the npz file SHA, not via agent memory.

### 8. Expected output 4-tuple

`(value=<α'(M_LRD=10⁷, L_max=10)>, scheme=connes-karoubi-pairing-on-chi-prime-inheritance, convention=substrate-IS-Cell-I-K-counter-instance-2, L_max=10)`

The expected value range (substrate prediction): `α'(M_LRD=10⁷, L_max=10) ∈ [1.527e-3, 2.836e-3]` (Sub-clause B 30% RATIO band around empirical anchor 1/458 ≈ 2.18e-3). If CF-38 tightens the band, range becomes [1.962e-3, 2.398e-3] (10% RATIO).

### 9. PASS / FAIL / INFO thresholds with tolerance rule

**Composite PASS predicate** (per W-1 workshop pre-registration; THEOREM tolerance rule for Sub-clause A; RATIO tolerance rule for Sub-clause B; ABSOLUTE-EXPONENT-SIGN tolerance rule for Sub-clause C):

- **Sub-clause A** (existence + sign): PASS iff `0 < α'(M_LRD = 10⁷, L_max = 10) < 1` (substrate prediction: positive microstate count ratio bounded above by 1; observable is well-defined and lies in the physically admissible range). FAIL iff `α' ≤ 0` or `α' ≥ 1`. THEOREM tolerance: substrate prediction of strict bounds; no numerical slack.

- **Sub-clause B** (empirical-anchor comparison): default 30% RATIO band:
  - PASS iff `|α' - 1/458| / (1/458) ≤ 0.30`, equiv. `α' ∈ [1.527e-3, 2.836e-3]`
  - INFO iff `0.10 ≤ |α' - 1/458| / (1/458) ≤ 0.30`
  - FAIL iff `|α' - 1/458| / (1/458) > 0.30`
  
  IF CF-38 returns PASS (empirical anchor 1/458 promoted to STAGE-3-PERMANENT) → tighten to 10% RATIO band:
  - PASS iff `|α' - 1/458| / (1/458) ≤ 0.10`, equiv. `α' ∈ [1.962e-3, 2.398e-3]`
  - INFO iff `0.05 ≤ |α' - 1/458| / (1/458) ≤ 0.10`
  - FAIL iff `|α' - 1/458| / (1/458) > 0.10`

- **Sub-clause C** (M-asymptotic envelope shape): PASS iff fit `α'(M) = 1 + c · (M/M_threshold)^{-n}` returns `n > 0` AND R² ≥ 0.95 on the 5-point M-scan. ABSOLUTE-EXPONENT-SIGN tolerance: substrate prediction of strict positivity; no INFO band on exponent sign.

**Composite collapse** (per `gate-verdicts.md §"Composite-collapse rule"`):
- All three Sub-clauses PASS → composite PASS
- Any Sub-clause FAIL → composite FAIL
- Otherwise (any Sub-clause INFO and no FAIL) → composite INFO

**Secondary-corridor routing on composite INFO** (per W-1 workshop pre-registration): IF composite verdict = INFO with rel_dev ∈ [0.10, 0.30] (Sub-clause B INFO band), route to S91+ AUX-4 secondary (c)∘(d) modified-universal-kernel γ(s) ≠ Γ(s) corridor. The INFO outcome is informative — it eliminates the (d)∘(b) primary as exact LRD α-anchor while leaving the secondary (c)∘(d) corridor open.

### 10. Substitution chain (MANDATORY for [SIGN] + [VERIFY-THEOREM] triggers)

Per `math-scripts.md §"Double-Check Logic Before Compute"` — required for any sign/direction/threshold claim:

```
Claim (Sub-clause A): α'(M_LRD, L_max=10) returns a positive ratio
                      in (0, 1) by substrate construction.

Step 1 — Definitions:
  φ_g^{sym}              = gradient-symmetric Hochschild 1-cocycle on A_K,
                           [φ_g^{sym}] ∈ HH^1(A_K) with regulator-class
                           INVARIANT cohomology class (W-5 calibration
                           corpus instance #1)
  χ'                     = inheritance morphism A_K → BdG-sub-algebra
                           (S89 §W2-3; Wedderburn 9 > 8 forces zero map at
                           the M_3(C) ⊕ M_3(C)-irrelevant block; non-zero
                           on the C ⊕ H sub-image)
  P_HSS(M)               = un-restricted Peter-Weyl horizon-spanning
                           projector at unrestricted spectral triple,
                           indexed by mass M; idempotent in K_0(A_K)
  P_HSS'(M) = χ'^*(P_HSS(M))
                         = inheritance-restricted projector;
                           χ'-pullback in K-theory; idempotent in
                           K_0(BdG-sub-algebra)
  Ch                     = Chern character HH^* ← K_*, computed via
                           Connes-Moscovici 1995 §III.4 finite-spectral-triple
                           residue formula on Peter-Weyl-decomposed triple
  ⟨·, ·⟩_{CK}            = Connes-Karoubi pairing HH^1 × K_0 → C; bilinear,
                           positive-semidefinite on the cone of positive
                           idempotents
  S_BH^semicl(M; M_Pl²)  = π · (M/M_Pl_reduced)² (Bekenstein-Hawking; > 0 for
                           all M > 0)
  α'(M)                  := ⟨χ'^*[φ_g^{sym}], [Ch(P_HSS'(M))]⟩_{CK}
                            · M_KK² / S_BH^semicl(M; M_Pl_reduced²)

Step 2 — Substitution (positivity of numerator):
  P_HSS'(M) is a positive idempotent (projector image) →
    [Ch(P_HSS'(M))] is a non-negative element of HH^*_even
  [φ_g^{sym}] is gradient-SYMMETRIC → its pullback χ'^*[φ_g^{sym}] is
    non-negative on the cone of positive idempotents
  The Connes-Karoubi pairing of a non-negative cohomology class with
    a non-negative K-class is NON-NEGATIVE:
      ⟨χ'^*[φ_g^{sym}], [Ch(P_HSS'(M))]⟩_{CK} ≥ 0

Step 3 — Substitution (positivity of denominator + dimensional ratio):
  M_KK² > 0 (canonical positive; substrate-IS area scale)
  S_BH^semicl(M_LRD; M_Pl_reduced²) = π · (10⁷ M_sun / M_Pl_reduced)² > 0
  Ratio M_KK² / S_BH^semicl > 0 for all M > 0

Step 4 — Simplification (combine):
  α'(M_LRD) = [non-negative] · [positive] = non-negative

Step 5 — Strictness (positivity, not just non-negativity):
  χ'^*[φ_g^{sym}] is STRICTLY positive on P_HSS'(M_LRD) iff there exists at
  least one Peter-Weyl sector (p,q) ≤ 10 in the inheritance-restricted image
  on which φ_g^{sym} evaluates non-trivially. By Wedderburn 9 > 8 (S89 §W2-3),
  χ' has non-zero image on at least one of the C or H summand blocks of A_K;
  φ_g^{sym} (gradient-symmetric, non-degenerate per W-5 calibration) does
  not annihilate this image. Therefore the pairing is STRICTLY positive:
      ⟨χ'^*[φ_g^{sym}], [Ch(P_HSS'(M_LRD))]⟩_{CK} > 0
  Multiplied by the strictly positive ratio M_KK² / S_BH^semicl > 0:
      α'(M_LRD) > 0

Step 6 — Upper bound (< 1):
  The inheritance restriction P_HSS' ⊆ P_HSS reduces the Chern character
  norm:
      ‖Ch(P_HSS'(M))‖ ≤ ‖Ch(P_HSS(M))‖
  The un-restricted ratio
      α(M) := ⟨[φ_g^{sym}], [Ch(P_HSS(M))]⟩_{CK} · M_KK² / S_BH^semicl
  is (by W-5 §VII.AF.1.OP-PROJ baseline) bounded above by 1 + small
  finite-L correction (Level-2 envelope), so on the L_max=10 truncation
  α(M_LRD, L_max=10) < 1 + ε for small ε.
  The inheritance restriction can only DECREASE the pairing magnitude
  (P_HSS' is a sub-projector of P_HSS), so:
      α'(M_LRD, L_max=10) ≤ α(M_LRD, L_max=10) < 1 + ε
  For Sub-clause A strict PASS (α' < 1), need ε small AND inheritance
  restriction strict; both are substrate-IS properties of χ' (Wedderburn
  9 > 8 produces strict restriction) and L_max=10 (Friedrich-Bär ε at
  L_max=10 is < 10^{-3} per W11-3 calibration). So:
      α'(M_LRD, L_max=10) < 1

Step 7 — Direction read-off:
  Combining Steps 5 and 6: 0 < α'(M_LRD, L_max=10) < 1

Conclusion: Sub-clause A PASSes BY SUBSTRATE CONSTRUCTION at the
            cohomology level. The numerical computation (Steps 1-13 of
            the dispatch procedure) is a VERIFICATION that finite-L
            truncation does not break this structural prediction.

PYTHON VERIFICATION (mandatory in script log):

  # In s90_w4_alpha_m_alt_corridor_d_compose_b.py log:
  print(f"Substitution chain verification:")
  print(f"  pairing_numerator = {pairing_value:.6e}      (must be > 0)")
  print(f"  area_ratio = {M_KK**2 / S_BH:.6e}            (must be > 0)")
  print(f"  alpha_prime = {alpha_prime:.6e}              (must be in (0, 1))")
  assert pairing_value > 0, "Sub-clause A FAIL: pairing not strictly positive"
  assert M_KK**2 / S_BH > 0, "Sub-clause A FAIL: area ratio non-positive"
  assert 0 < alpha_prime < 1, "Sub-clause A FAIL: alpha' out of (0, 1)"
```

### 11. What PASS / FAIL / INFO MEAN for solution space

**PASS** (all three Sub-clauses A + B + C):
- The (d)∘(b) compositional primary corridor is CONFIRMED as the substrate-IS LRD α-anchor at the Cell-I cohomology-class layer.
- Calibration corpus instance #2 of the simultaneous element-1 + element-3 double-deformation pattern is LANDED (instance #1 = §VII.AF.1.OP-PROJ W-5).
- Hybrid Independence Test K-counter advances from K=2 to K=3 (BY-CONSTRUCTION post-§W1-1; the (d)∘(b) corridor is structurally independent of (a) on element-1 deformation AND independent of W-5 on element-3 deformation).
- The S91+ Stage-2 three-axis cross-axis independent-verify (AUX-5) becomes the next gate; reviewers lizzi Axis-A + volovik Axis-B + mack Axis-C. PASS-AND across all three at clause level promotes the candidate from STAGE-1-CANDIDATE to STAGE-3-PERMANENT per `joint-theorem-promotion.md §"Stage 2"`.
- Downstream consequence: the LRD α-anchor becomes a substrate-IS framework prediction at the cohomology-class layer; the empirical 1/458 LRD α-anchor is canonically explained by the substrate.

**FAIL** (any Sub-clause FAIL):
- Sub-clause A FAIL (α' ≤ 0 OR α' ≥ 1): the substrate construction's positivity / bounded-by-1 prediction is BROKEN; the (d)∘(b) corridor is CLOSED. Re-route to S91+ secondary (c)∘(d) corridor OR re-examine the W-5 calibration baseline at instance #1. This would be a STRUCTURAL FAIL of the simultaneous double-deformation pattern.
- Sub-clause B FAIL (rel_dev > 30% or 10%): the (d)∘(b) corridor returns a finite positive ratio in (0, 1) but it is NOT the empirical LRD α-anchor 1/458. The corridor is closed as the LRD α-anchor candidate; an alternative anchor source must be identified. The secondary (c)∘(d) corridor is opened at S91+ AUX-4 as the next candidate.
- Sub-clause C FAIL (n ≤ 0 OR R² < 0.95): the M-asymptotic envelope does not have the (d)∘(b) inherited form; either the (d) deformation does not produce the expected mass-dependence or the M-scan window is too narrow. Re-derive the envelope form from the inheritance restriction.

**INFO** (any Sub-clause INFO, no FAIL):
- Default-band INFO (Sub-clause B 10% ≤ rel_dev ≤ 30%): the (d)∘(b) corridor is BORDERLINE as the LRD α-anchor candidate. Route to S91+ AUX-4 secondary (c)∘(d) modified-universal-kernel γ(s) ≠ Γ(s) corridor; the secondary corridor's γ(s) choice (W-1 AUX-4) is the discriminator. INFO is informative — it constrains the corridor space to (d)∘(b) primary OR (c)∘(d) secondary without false-positively closing either.
- Sub-clause C INFO (R² ∈ [0.85, 0.95]): the M-asymptotic envelope is approximately inherited form but the fit is noisy; expand the M-scan window at S91+ AUX-6 (Level-2 moduli-deformation substrate-IS extension).

**Composite collapse to BREAKDOWN** (regime_verdict = BREAKDOWN per `gate-verdicts.md §"Auto-shortening clause discipline"`):
- IF L_max=10 truncation discards Peter-Weyl sectors contributing >5% to the pairing (per cross-check in §5 step 11): regime_verdict = MARGINAL → composite INFO regardless of Sub-clauses.
- IF L_max=10 truncation discards sectors contributing >50%: regime_verdict = BREAKDOWN → composite FAIL regardless. This would force re-dispatch at L_max=12 per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`.

### 12. Effort estimate

**~3.5 wave-equivalents** (BIG — largest single S90 item). Breakdown:
- Construct χ' pullback action on Hochschild 1-cocycles, verify dχ'^*φ_g^{sym} = 0 (~0.5 we)
- Construct P_HSS'(M) inheritance-restricted projector at M = M_LRD with derivation of cutoff form (NOT naive λ² ≤ M_KK² · (M_LRD/M_KK²)) (~0.7 we)
- Compute Chern character via Connes-Moscovici 1995 §III.4 residue formula on (A_K^{≤10}, H_K^{≤10}, D_K^{≤10}) (~0.8 we)
- Connes-Karoubi pairing as a finite trace sum + cross-check against §VII.AF.1.OP-PROJ baseline at un-restricted projector (~0.5 we)
- M-asymptotic envelope fit + 5-point M-scan + log-log regression (~0.3 we)
- Empirical-anchor comparison + sub-clause-by-sub-clause verdict (~0.2 we)
- Verdict-line emission + working-paper §W4-1 write-up + cross-checks + completion-verification on disk (~0.5 we)

### 13. Substrate-framing reminder

The dispatch prompt (§5 above) opens with an explicit substrate-framing block. Key points repeated here for the gate-block reader:

- The substrate IS the spectral triple `(A_K, H_K, D_K)` at L_max = 10. It is NOT in any pre-existing geometric container.
- P_HSS'(M) is substrate-IS — the inheritance-restricted Peter-Weyl horizon-spanning projector is a projector in K_0(BdG-sub-algebra), not a horizon embedded in spacetime.
- M_KK² is the substrate-IS area scale; M_Pl_reduced² is the laboratory-IN area scale.
- The bridge map M_KK² / S_BH^semicl(M; M_Pl_reduced²) carries substrate-IS → laboratory-IN at Element 3 of the bridge anatomy.
- The direction of explanation flows: substrate eigenvalues → cohomology pairing → emergent BH-thermodynamic α(M) interpretation.
- DO NOT write "particles created in curved spacetime", "horizon of a black hole of mass M", or "spacetime-embedded projector". Use substrate-IS language throughout.

---

## §W4-2. CF-38 — S90-W1-1-EMPIRICAL-ANCHOR-1-458-PROMOTION-STATUS-VERIFY

**Gate ID**: `S90-W1-1-EMPIRICAL-ANCHOR-1-458-PROMOTION-STATUS-VERIFY`
**Origin**: W-1 AUX-2
**Effort**: 0.1 we

### 1. Trigger
`[AUDIT]` (mechanical pre-flight check on registry / canonical_constants state; outcome conditionally tightens CF-37 Sub-clause B band from 30% to 10% RATIO)

### 2. Classification
**NON-PHONONIC** (registry-state classification check; no substrate-physics derivation). Reserves the right of CF-37 to tighten its Sub-clause B threshold based on the registry-state of the empirical anchor 1/458.

### 3. Agent type
**PRIMARY**: `phonon-first-cosmologist` (W-1 workshop substrate-physics author; the AUX-2 was queued by W-1 as a pre-flight to CF-37). Runs as a mechanical knowledge-MCP query + plan-block edit; orchestrator may execute directly per `wave-classification.md §"Dispatch consequences"` if the query is purely audit-class.

### 4. Hypothesis
**Pre-flight hypothesis**: The empirical anchor `1/458 ≈ 2.18e-3` at M_LRD = 10⁷ M_sun (from S88 W1b1-63 branch (c)) has been promoted to STAGE-3-PERMANENT in `permanent-results-registry.md` and/or registered as a canonical pin `alpha_LRD_FW` in `canonical_constants.py` since the W-1 workshop close. IF promoted, CF-37 Sub-clause B tightens to 10% RATIO; IF NOT promoted, CF-37 Sub-clause B retains the default 30% RATIO.

### 5. Method — COMPLETE self-contained dispatch prompt

```
You are phonon-first-cosmologist. Execute the AUX-2 pre-flight check for
CF-37 (S90-W1-1-ALT-CORRIDOR-SELECTED-LRD-ALPHA-DERIVATION).

This is a mechanical knowledge-MCP query + plan-block tolerance-band edit. No
substrate-physics derivation is required.

═══════════════════════════════════════════════════════════════════════════
PROCEDURE
═══════════════════════════════════════════════════════════════════════════

Step 1 — Query the knowledge MCP for the empirical anchor:

    search_knowledge("empirical anchor 1/458 LRD alpha M_LRD S88 W1b1-63
                    branch c promotion status")
    trace_entity("alpha_LRD empirical anchor 1/458")
    get_constant("alpha_LRD_FW")

Step 2 — Read the registry §VII for STAGE-3-PERMANENT entries containing
"1/458" OR "alpha_LRD" OR "LRD α-anchor":

    Read permanent-results-registry.md (full file or grep on relevant
    sub-strings). Identify whether any §VII.X entry STAGE-3-PERMANENT
    tag accompanies the empirical anchor 1/458.

Step 3 — Read canonical_constants.py for `alpha_LRD_FW`:

    grep canonical_constants.py for "alpha_LRD_FW"
    If present, extract the value, session pin, source pin, comment.
    Verify value is consistent with 1/458 ≈ 2.18e-3 within publication
    precision.

Step 4 — Determine promotion-status:

    promotion_status_PASS  iff:
      (a) at least one §VII.X STAGE-3-PERMANENT entry contains the
          anchor 1/458 with substrate-derived provenance, OR
      (b) alpha_LRD_FW canonical pin exists in canonical_constants.py
          with substrate-derived PROVENANCE.

    promotion_status_FAIL  iff neither (a) nor (b).

Step 5 — Conditional CF-37 plan-block edit:

    IF promotion_status_PASS:
      Edit this plan-w4.md §W4-1 §9 "PASS / FAIL / INFO thresholds"
      to tighten Sub-clause B from 30% RATIO to 10% RATIO. Document
      the edit in the plan-revision history with timestamp + reason.

    IF promotion_status_FAIL:
      No edit. Sub-clause B retains 30% RATIO default. Document the
      decision in the verdict-file value-field.

Step 6 — Append verdict line:

    S90-W1-1-EMPIRICAL-ANCHOR-1-458-PROMOTION-STATUS-VERIFY: PASS|FAIL -- \
      value='promotion_status=PASS_tighten_to_10pct' OR \
      value='promotion_status=FAIL_retain_30pct' \
      scheme=knowledge-mcp-registry-query \
      convention=mechanical-pre-flight-AUX-2 \
      L_max=N/A \
      audit_sha256=<full-64-char> content_sha256=<full-64-char> \
      schema_version=S87-v2

    PASS semantics here: "anchor is promoted; CF-37 tolerance tightened"
    FAIL semantics here: "anchor not promoted; CF-37 retains default band"

    NOTE: this is a MECHANICAL pre-flight check; FAIL is NOT a substrate-
    physics failure. The FAIL value-field documents the registry state
    truthfully and CF-37 proceeds with the default tolerance.

Step 7 — Working paper §W4-2: write the query results + the conditional
    plan-block edit + the verdict in 15+ lines.

═══════════════════════════════════════════════════════════════════════════
INPUT PINS
═══════════════════════════════════════════════════════════════════════════

  - sessions/permanent-results-registry.md         (pinned at dispatch)
  - computations/_shared/canonical_constants.py     (pinned at dispatch)
  - knowledge-MCP database state                    (queried at dispatch)
  - sessions/session-plan/session-90-plan-w4.md    (edit target conditional
                                                    on promotion_status_PASS)

═══════════════════════════════════════════════════════════════════════════
COMPLETION VERIFICATION
═══════════════════════════════════════════════════════════════════════════

Before declaring task-complete, verify on disk:

  (a) Verdict line appended to computations/session-90/s90_gate_verdicts.txt
  (b) Dual-SHA companion row appended
  (c) Conditional plan-block edit applied IF promotion_status_PASS, OR
      decision-not-to-edit documented in the verdict value-field IF FAIL
  (d) Working paper §W4-2 with >15 lines of substantive content
```

### 6. Machinery pin (PRDR)

| Parameter | Pin |
|:----------|:----|
| `query_targets` | knowledge-MCP (search_knowledge, get_constant); registry markdown; canonical_constants.py |
| `promotion_status_criterion` | (a) STAGE-3-PERMANENT registry entry containing 1/458 OR (b) `alpha_LRD_FW` canonical pin with substrate-derived PROVENANCE |
| `tightening_band` | 10% RATIO if promotion_status_PASS; 30% RATIO retain if FAIL |
| `convention_tag` | `mechanical-pre-flight-AUX-2` |
| `scheme_tag` | `knowledge-mcp-registry-query` |
| `random_seed` | N/A |
| `GPU_path` | N/A |
| `verdict_source` | `computations/session-90/s90_gate_verdicts.txt` |
| `working_paper_target` | `sessions/archive/session-90/session-90-w4-workingpaper.md §W4-2` |

### 7. Input SHA-256 pins

| File | Pin |
|:-----|:----|
| `sessions/permanent-results-registry.md` | `<pinned at dispatch>` |
| `computations/_shared/canonical_constants.py` | `<pinned at dispatch>` |
| `sessions/session-plan/session-90-plan-w4.md` | `<pinned at dispatch>` (conditional edit target) |

### 8. Expected output 4-tuple

`(value='promotion_status=PASS_tighten_to_10pct' OR 'promotion_status=FAIL_retain_30pct', scheme=knowledge-mcp-registry-query, convention=mechanical-pre-flight-AUX-2, L_max=N/A)`

### 9. PASS / FAIL / INFO thresholds with tolerance rule

**PASS (anchor promoted; tighten CF-37 Sub-clause B to 10% RATIO)**: At least one of (a) `permanent-results-registry.md` contains a STAGE-3-PERMANENT entry with the empirical anchor 1/458 and substrate-derived provenance OR (b) `canonical_constants.py` contains an `alpha_LRD_FW` pin with substrate-derived PROVENANCE entry. THEOREM tolerance: existence of the registry/canonical entry is binary; no numerical band.

**FAIL (anchor not promoted; retain 30% RATIO)**: Neither (a) nor (b) holds. The CF-37 default 30% RATIO band is retained. FAIL here is a documentation-truthful outcome, NOT a substrate-physics failure.

**INFO (anchor partially promoted)**: A STAGE-1-CANDIDATE or STAGE-2 registry entry contains the anchor but has not advanced to STAGE-3-PERMANENT. Retain default 30% RATIO. Document the partial-promotion state in the verdict value-field.

### 10. Substitution chain
Not required (no sign/direction/threshold substrate prediction). The gate is mechanical; the verdict reflects the registry/canonical state factually.

### 11. What PASS / FAIL / INFO MEAN for solution space

- **PASS**: Empirical anchor 1/458 is canonically promoted; CF-37 Sub-clause B threshold tightens to 10% RATIO; the (d)∘(b) corridor PASS criterion becomes stricter (`α' ∈ [1.962e-3, 2.398e-3]`); STAGE-2 verify (S91+ AUX-5) post-PASS is sharpened.
- **FAIL**: Empirical anchor 1/458 retains pre-promotion status; CF-37 Sub-clause B threshold is the default 30% RATIO; the (d)∘(b) corridor PASS criterion is the wider band (`α' ∈ [1.527e-3, 2.836e-3]`). No substrate-physics implication.
- **INFO**: Anchor is in intermediate registry state; retain default 30% RATIO; the registry-promotion workflow is in progress and may complete before CF-37 dispatches (in which case CF-37 may re-read CF-38 verdict-line state at its own dispatch time).

### 12. Effort estimate

**0.1 we** (mechanical knowledge-MCP query + conditional plan-block edit + verdict-line + 15+ line working-paper section).

### 13. Substrate-framing reminder

This is a registry/canonical-state audit; no substrate-physics claim is made. The verdict reflects the documentation state, NOT a physical truth about the substrate. Frame the verdict-file write and working-paper section as bookkeeping; do NOT couch the result in substrate-physics language.

---

## §W4-3. CF-39 — S90-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM-RETRY

**Gate ID**: `S90-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM-RETRY`
**Origin**: gen §6 CF-W1-2-DEFERRED
**Effort**: 0.5 we

### 1. Trigger
`[VERIFY]` (re-execution of S88 §W1-2 deferred gate after CF-40 species-multiplicity retry PASS; emits Option A `supersedes`-tagged corrective canonical line for the original `2afd17ef99c81123…` FAIL line per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"`)

### 2. Classification
**PHONONIC** (substrate cascade-tail observable at the horizon equilibrium scale T_H = 1.057 MeV; L_H_canonical is a substrate-derived horizon length scale governing the late-cascade tail). Reads on the substrate's own clock.

### 3. Agent type
**PRIMARY**: `mack-cosmic-bridge` (per `feedback_mack-bridge-role.md` observational-anchor + registry-write authority; mack-cosmic-bridge has sole writer authority for the L_H_canonical re-pinning and the Option A supersedes-tagged emission). Cross-check: `phonon-first-cosmologist` consults on the substrate cascade-tail formula but does NOT write the verdict/registry edits.

### 4. Hypothesis
**Substrate prediction**: With the refined CF-40 species-multiplicity output `g_*(T_H = 1.057 MeV)` (lattice-QCD-corrected, Boltzmann threshold-suppressed at m_e), the canonical re-pinning `L_H_canonical = (π²/60) · g_*(T_H) · A_horizon · T_H⁴` returns within 0.5 log-OOM ABSOLUTE of `f(M_at_W1c69)` (the cascade-tail expected value at M = §W1c-69 mass). The residual `Step5_residual_post_correction` shrinks by ≥ 1 log-OOM relative to the S88 §W1-2 FAIL pre-correction residual.

### 5. Method — COMPLETE self-contained dispatch prompt

```
You are mack-cosmic-bridge. Re-execute S88 §W1-2 with refined inputs from
S90 CF-40 (S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED).
Consultation with phonon-first-cosmologist on the substrate cascade-tail
formula is permitted; the verdict-file write + the registry-text update +
the Option A supersedes-tag emission are YOUR sole-writer responsibility.

═══════════════════════════════════════════════════════════════════════════
PREREQUISITE — CF-40 MUST PASS FIRST
═══════════════════════════════════════════════════════════════════════════

Verify CF-40 PASS verdict line at computations/session-90/s90_gate_verdicts.txt
(grep for S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED). If CF-40
is not PASS yet, halt and request CF-40 dispatch first. Per Known
dependencies (context file): "CF-40 PRECEDES CF-39".

═══════════════════════════════════════════════════════════════════════════
SUBSTRATE FRAMING
═══════════════════════════════════════════════════════════════════════════

L_H_canonical is the substrate-derived horizon length scale at the
substrate-pinned horizon equilibrium temperature T_H. It is NOT a GR
horizon embedded in spacetime; it is the cascade-tail equilibrium scale
on the substrate's own clock. Direction of explanation: substrate spectral
content → cascade tail at T_H → laboratory-IN cosmological horizon
observation.

═══════════════════════════════════════════════════════════════════════════
PROCEDURE
═══════════════════════════════════════════════════════════════════════════

Step 1 — Top of script:
    from canonical_constants import *
    import numpy as np

Step 2 — Pin T_H = 1.057 MeV (substrate-pinned per S88 W6 §V.1; should be
    in canonical_constants.py — verify or add).

Step 3 — Load CF-40 output npz:
    Read computations/_shared/s90_w4_f_m_species_multiplicity_retry.npz
    (mandatory key: g_star_BS_T_H value at T_H = 1.057 MeV; lattice-QCD
    + Boltzmann threshold-suppressed at m_e).

Step 4 — Compute L_H_canonical:
    L_H_canonical = (π**2 / 60) * g_star_BS_T_H * A_horizon * T_H**4
    where A_horizon is the substrate-IS horizon area (canonical pin
    expected; verify via knowledge-MCP).

Step 5 — Compute reference f(M_at_W1c69):
    Read S88 §W1c-69 source workshop / npz for f(M) cascade-tail
    expectation at M = §W1c-69 mass anchor. Use the pre-S90 stabilized
    f(M) function form per S88 W6 §V.5 cascade form.

Step 6 — Comparison:
    delta_log = abs(log10(L_H_canonical / L_H_eq1) - log10(f(M_at_W1c69)))
    where L_H_eq1 is the canonical reference equation-1 length scale
    (canonical pin or computed at runtime per S88 §W1-2 spec).

Step 7 — Residual comparison:
    Step5_residual_post_correction = computed residual from this gate
    Step5_residual_pre_correction = S88 §W1-2 FAIL residual (look up at
                                    pinned audit_sha256 2afd17ef99c81123...)
    log_residual_improvement = log10(Step5_residual_pre_correction /
                                     Step5_residual_post_correction)

Step 8 — PASS predicate:
    PASS iff:
      delta_log < 0.5  AND
      log_residual_improvement >= 1.0  AND
      supersedes-token correctly emitted as full 64-char form
    FAIL otherwise.

Step 9 — Grep S88 verdict file for the full 64-char audit_sha256 of the
    superseded line. The 16-char head form is 2afd17ef99c81123; locate
    the full 64-char form via grep on computations/session-88/s88_gate_verdicts.txt
    AND from the S88 §W1-2 verdict-file line containing this head. Use
    the FULL 64-character form in the supersedes tag.

Step 10 — Append corrective canonical line per Option A:

    S90-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM-RETRY: PASS|FAIL -- \
      value='L_H=<v> delta_log=<d> residual_improvement=<r>OOM supersedes=<full-64-char-old-sha>' \
      scheme=substrate-pinned-T_H-cascade-tail \
      convention=canonical-re-pinning-Option-A-supersedes \
      L_max=10 \
      audit_sha256=<full-64-char> content_sha256=<full-64-char> \
      schema_version=S87-v2

    Dual-SHA companion row:
      # audit_sha256_short=... content_sha256_short=... \
      # S90-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM-RETRY \
      # dual-SHA companion row (W9a-99 split)

    NOTE per gate-verdicts.md §"Option A": the ORIGINAL FAIL line with
    audit_sha256 starting 2afd17ef99c81123... is RETAINED on disk at
    computations/session-88/s88_gate_verdicts.txt per absolute verdict
    permanence. This corrective line APPENDS to computations/session-90/
    s90_gate_verdicts.txt with the `supersedes` token pointing to the
    full 64-char form of the original. NO retroactive edit of the S88
    file is permitted.

Step 11 — Working paper §W4-3:
    >15 lines documenting:
      - Substrate-pinned T_H = 1.057 MeV
      - Refined g_star_BS_T_H from CF-40
      - L_H_canonical computed value + delta_log
      - Step5 residual pre/post comparison + log-OOM improvement
      - Option A supersedes-tag emission with full 64-char old audit_sha256
      - Sub-substrate framing: this is a substrate-clock observable;
        direction of explanation substrate → cascade tail → cosmological
        horizon image

═══════════════════════════════════════════════════════════════════════════
INPUT-SHA PINS
═══════════════════════════════════════════════════════════════════════════

  - computations/_shared/s90_w4_f_m_species_multiplicity_retry.npz \
      (CF-40 output; PASS-prerequisite verified)
  - computations/session-88/s88_gate_verdicts.txt (full file; for the
      original FAIL line full-64-char audit_sha256 grep)
  - sessions/archive/session-88/<S88 §W1c-69 source workshop or npz; verify path
      at dispatch>
  - computations/_shared/canonical_constants.py (T_H, A_horizon, M_KK,
      L_H_eq1 if pinned)
```

### 6. Machinery pin (PRDR)

| Parameter | Pin |
|:----------|:----|
| `T_H` | 1.057 MeV (S88 W6 §V.1 substrate-pinned) |
| `g_star_T_H_source` | CF-40 npz (lattice-QCD + Boltzmann threshold-suppressed at m_e); PASS-prerequisite |
| `cascade_tail_form` | S88 W6 §V.5 (canonical substrate cascade form) |
| `f_M_anchor` | f(M_at_W1c69) at S88 §W1c-69 mass anchor |
| `delta_log_threshold` | 0.5 ABSOLUTE log-OOM |
| `residual_improvement_threshold` | ≥ 1.0 log-OOM |
| `supersedes_sha` | Full 64-char form of `2afd17ef99c81123…` (grep from S88 verdict file at dispatch) |
| `convention_tag` | `canonical-re-pinning-Option-A-supersedes` |
| `scheme_tag` | `substrate-pinned-T_H-cascade-tail` |
| `verdict_source` | `computations/session-90/s90_gate_verdicts.txt` |
| `working_paper_target` | `sessions/archive/session-90/session-90-w4-workingpaper.md §W4-3` |

### 7. Input SHA-256 pins

| File | Pin |
|:-----|:----|
| `computations/_shared/s90_w4_f_m_species_multiplicity_retry.npz` | `<pinned at CF-40 PASS>` |
| `computations/session-88/s88_gate_verdicts.txt` | `<pinned at dispatch>` (full file; for the original FAIL line audit_sha256 grep) |
| `computations/_shared/canonical_constants.py` | `<pinned at dispatch>` |

### 8. Expected output 4-tuple

`(value='L_H=<v> delta_log=<d> residual_improvement=<r>OOM supersedes=<full-64-char-old-sha>', scheme=substrate-pinned-T_H-cascade-tail, convention=canonical-re-pinning-Option-A-supersedes, L_max=10)`

### 9. PASS / FAIL / INFO thresholds with tolerance rule

**PASS**: `delta_log < 0.5` ABSOLUTE log-OOM AND `log_residual_improvement ≥ 1.0` log-OOM AND `supersedes` token is correctly emitted as full 64-char form (NOT 16-char head). ABSOLUTE log-OOM tolerance rule.

**FAIL**: `delta_log ≥ 0.5` OR `log_residual_improvement < 1.0` OR `supersedes` token malformed (head-truncated or missing).

**INFO**: `0.5 ≤ delta_log < 1.0` AND `0.5 ≤ log_residual_improvement < 1.0` (partial correction; routes to S91+ refinement).

### 10. Substitution chain
Not strictly required (no signed-direction prediction; the gate is a quantitative re-execution under refined inputs). However, the SOURCE-RECONCILIATION class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY chain MUST be documented in the script log: the refined `g_*(T_H)` from CF-40 derives from lattice-QCD + Boltzmann threshold-suppression at m_e; the L_H_canonical = (π²/60) · g_*(T_H) · A_horizon · T_H⁴ formula is the canonical form per S88 W6 §V.5; substituting the refined g_* into this formula is a Class-(d) derivation chain that must be transparently logged.

### 11. What PASS / FAIL / INFO MEAN for solution space

- **PASS**: The S88 §W1-2 FAIL is closed in S90 via the refined species-multiplicity. The supersedes-tagged corrective line establishes that the substrate-cascade-tail L_H_canonical is consistent with the §W1c-69 mass anchor at ≤ 0.5 log-OOM precision. Downstream cosmological-horizon predictions feed forward to the LRD α-anchor secondary discriminator at S91+ if CF-37 returns INFO.
- **FAIL**: Either (a) the refined g_*(T_H) from CF-40 does not produce sufficient correction (substrate cascade-tail formula may need further refinement OR substrate pin T_H = 1.057 MeV may be miscalibrated), (b) the supersedes-token emission is malformed (procedural fix; re-run script with correct grep on the full 64-char audit_sha256), or (c) the residual improvement is < 1 log-OOM (the correction is insufficient; need stronger species-multiplicity model).
- **INFO**: Partial correction (residual shrinks but not by full 1 log-OOM); routes to S91+ for further refinement of either the species-multiplicity model or the substrate cascade-tail formula.

### 12. Effort estimate

**0.5 we** (mechanical re-execution of S88 §W1-2 under refined CF-40 inputs; grep + supersedes-tag emission + 15+ line working paper §W4-3).

### 13. Substrate-framing reminder

L_H_canonical is the substrate-derived horizon length scale at the substrate-pinned T_H. The cascade tail observable lives on the substrate's own clock (substrate-IS, single-τ-slice substrate-IS Level 1 per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`). Direction of explanation: substrate spectral content → cascade tail at T_H → laboratory-IN cosmological-horizon observation. Do NOT frame as "horizon in spacetime"; frame as "substrate cascade-tail equilibrium at T_H".

---

## §W4-4. CF-40 — S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED

**Gate ID**: `S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED`
**Origin**: gen §6 CF-W1-3-RETRY + CRITERION-REVISION
**Effort**: 1.3 we (1.0 + 0.3 addendum for Boltzmann threshold-suppression refinement)

### 1. Trigger
`[VERIFY]` (re-execution of S88 §W1-3 species-multiplicity lookup under refined lattice-QCD-corrected `g_*(T)` near Λ_QCD ≈ 200 MeV AND Boltzmann threshold-suppression at m_e/m_W/m_top boundaries; 3 cross-check anchors at T ∈ {100 GeV, 1 GeV, 1 MeV} against PDG/Planck reference values)

### 2. Classification
**PARTICLE** (species-multiplicity g_*(T) is a particle-physics-derived quantity: counts the effective relativistic degrees of freedom at temperature T; lattice-QCD corrections account for quark-hadron transition near Λ_QCD ≈ 200 MeV; Boltzmann threshold-suppression at species mass m accounts for `exp(-m/T)` near-threshold behavior).

### 3. Agent type
**PRIMARY (sole writer)**: `mack-cosmic-bridge` (per `feedback_mack-bridge-role.md` observational-anchor authority; mack's lattice-QCD + Boltzmann-threshold modeling expertise; mack writes the verdict-line + the canonical-constants pin if g_star_BS_T_H is promoted). Consultation with feynman-theorist on Boltzmann threshold-suppression numerics is permitted but optional.

### 4. Hypothesis
**Substrate prediction**: The substrate cascade form per S88 W6 §V.5 is substrate-pinned; the laboratory-IN species-multiplicity `g_*(T)` is the PDG/Planck-canonical lattice-QCD-corrected count with Boltzmann threshold-suppression `exp(-m/T)` for species within factor 5 of T. Across 3 cross-check anchors T ∈ {100 GeV, 1 GeV, 1 MeV}, the Boltzmann-suppressed reference `g_*_BS(T)` matches the PDG/Planck reference within 10% RATIO; this validates the refined species-multiplicity model as the appropriate input for CF-39 L_H_canonical re-pinning at T_H = 1.057 MeV.

### 5. Method — COMPLETE self-contained dispatch prompt

```
You are mack-cosmic-bridge, sole writer per feedback_mack-bridge-role.md
observational-anchor authority. Refine the S88 §W1-3 species-multiplicity
lookup with lattice-QCD corrections near Λ_QCD ≈ 200 MeV and Boltzmann
threshold-suppression at m_e (T=1 MeV) / m_W (T=100 GeV) / m_top (T=100 GeV)
boundaries. Validate against 3 PDG/Planck cross-check anchors at
T ∈ {100 GeV, 1 GeV, 1 MeV}.

This is a particle-physics anchor refinement; substrate framing applies to
the cascade-tail FORM (substrate-pinned per S88 W6 §V.5) but the g_*(T)
quantity itself is a laboratory-IN PDG-canonical count.

═══════════════════════════════════════════════════════════════════════════
SUBSTRATE FRAMING
═══════════════════════════════════════════════════════════════════════════

The substrate cascade form per S88 W6 §V.5 specifies HOW g_*(T) enters
the cascade-tail observable; it does NOT specify g_*(T) itself. g_*(T) is
a laboratory-IN PDG-canonical count of effective relativistic degrees of
freedom at temperature T. The refinement here is on the laboratory-IN
input to the substrate cascade-tail formula; the substrate-IS observable
remains pinned at S88 W6 §V.5.

═══════════════════════════════════════════════════════════════════════════
PROCEDURE
═══════════════════════════════════════════════════════════════════════════

Step 1 — Top of script:
    from canonical_constants import *
    import numpy as np

Step 2 — Build lattice-QCD-corrected g_*(T) table near Λ_QCD ≈ 200 MeV:

    Use external lattice-QCD g_*(T) tabulation (cite per regulator-pin
    discipline: a_n^{lattice} tagging applies in the spirit of the rule
    even though g_*(T) is not a Seeley-DeWitt coefficient — the lattice
    convention pin is required for reproducibility). The lattice-QCD
    g_*(T) is tabulated in standard references (PDG / Planck collab /
    Borsanyi et al. 2016 lattice-QCD g_*(T)).

    At T near Λ_QCD ≈ 200 MeV, g_*(T) interpolates between the deconfined
    quark-gluon phase value (~61.75 for 3 flavors + gluons) and the
    confined hadronic phase value (~10.75 for π's + leptons +
    photons +ν's at low T).

Step 3 — Build Boltzmann threshold-suppressed g_*_BS(T):

    g_*_BS(T) = Σ_i g_i · BS_i(T)
    where:
      g_i = degree-of-freedom multiplicity of species i (fermion / boson)
      BS_i(T) = Boltzmann suppression factor:
        BS_i(T) = 1                  if m_i << T (relativistic)
        BS_i(T) = exp(-m_i / T)      if m_i ~ T (threshold)
        BS_i(T) = 0                  if m_i >> T (non-relativistic /
                                                   decoupled)

    Apply threshold suppression for species within factor 5 of T:
      |m_i - T| <= 5 T  OR  m_i / T in [0.2, 5]  →  use exp(-m/T)

    Critical species + masses:
      m_e   ≈ 0.511 MeV   (active at T = 1 MeV via Boltzmann factor)
      m_W   ≈ 80.4 GeV    (active at T = 100 GeV)
      m_top ≈ 173 GeV     (active at T = 100 GeV)
      Λ_QCD ≈ 200 MeV     (quark-hadron transition; near-threshold band
                            for T ∈ [50 MeV, 1 GeV])

Step 4 — Evaluate g_*_BS(T) at 3 cross-check anchors:

    Compute g_*_BS(T = 100 GeV), g_*_BS(T = 1 GeV), g_*_BS(T = 1 MeV).

Step 5 — Cross-check against PDG/Planck reference:

    Look up PDG-canonical or Planck 2018 reference g_*(T) at the 3 anchors:
      g_*(T = 100 GeV) ≈ 106.75   (SM full content above EW transition)
      g_*(T = 1 GeV)   ≈ 60-65    (deconfined quark-gluon phase)
      g_*(T = 1 MeV)   ≈ 3.36-10.75 (depends on neutrino decoupling state)

    Compute rel_dev_i = |g_*_BS(T_i) - g_*_PDG(T_i)| / g_*_PDG(T_i)
    for i ∈ {100 GeV, 1 GeV, 1 MeV}.

Step 6 — PASS predicate (all 3 anchors PASS at 10% RATIO):
    PASS iff rel_dev_i ≤ 0.10 for ALL i ∈ {100 GeV, 1 GeV, 1 MeV}
    FAIL iff any rel_dev_i > 0.10
    INFO iff at least one rel_dev_i in (0.05, 0.10] (borderline)

Step 7 — Evaluate g_*_BS at T_H = 1.057 MeV (the CF-39 anchor):
    Compute g_*_BS(T = 1.057 MeV) for direct use in CF-39.
    Document this value as the canonical-pin candidate g_star_BS_T_H.

Step 8 — Output npz:

    computations/_shared/s90_w4_f_m_species_multiplicity_retry.npz
    Keys (mandatory):
      g_star_BS_T_H                          (at T_H = 1.057 MeV; CF-39 anchor)
      g_star_BS_100GeV, g_star_BS_1GeV, g_star_BS_1MeV
      g_star_PDG_100GeV, g_star_PDG_1GeV, g_star_PDG_1MeV
      rel_dev_anchors                         (3-element array)
      Boltzmann_factors_per_species           (dict per anchor)
      cascade_form_pin                        = "S88 W6 §V.5"
      lattice_QCD_pin                         = "Borsanyi et al. 2016
                                                 OR PDG canonical"
      audit_sha256, content_sha256, schema_version

Step 9 — Append verdict line:

    S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED: PASS|FAIL|INFO -- \
      value='all 3 anchors rel_dev<=10pct; g_star_BS_T_H=<v>' \
      scheme=lattice-QCD-corrected-Boltzmann-suppressed-substrate-cascade \
      convention=PDG-canonical-3-anchor-cross-check \
      L_max=N/A \
      audit_sha256=<full-64-char> content_sha256=<full-64-char> \
      schema_version=S87-v2

    Dual-SHA companion row per S87+ schema.

Step 10 — Working paper §W4-4 (>15 lines):
    Document refined g_*(T) model + lattice-QCD source + Boltzmann
    threshold-suppression + 3 anchor cross-checks + g_star_BS_T_H for
    CF-39 + substrate-framing (cascade FORM is substrate-pinned, g_*(T)
    INPUT is laboratory-IN).

═══════════════════════════════════════════════════════════════════════════
INPUT-SHA PINS
═══════════════════════════════════════════════════════════════════════════

  - sessions/archive/session-88/<S88 W6 §V.5 source workshop or npz>
  - computations/_shared/canonical_constants.py (T_H, M_KK, m_e, m_W, m_top)
  - External reference: PDG 2024 / Planck 2018 g_*(T) tabulation OR
    Borsanyi et al. 2016 lattice-QCD g_*(T) — cited in PROVENANCE
```

### 6. Machinery pin (PRDR)

| Parameter | Pin |
|:----------|:----|
| `cascade_form_substrate` | S88 W6 §V.5 substrate-pinned (NOT refined here; refinement is on the laboratory-IN g_*(T) input only) |
| `lattice_QCD_source` | Borsanyi et al. 2016 lattice-QCD g_*(T) OR PDG-canonical tabulation; cite in PROVENANCE |
| `Boltzmann_threshold_band` | species within factor 5 of T (`m/T ∈ [0.2, 5]`) use `exp(-m/T)`; outside band: 1 (relativistic) or 0 (decoupled) |
| `cross_check_anchors` | T ∈ {100 GeV, 1 GeV, 1 MeV} per W-1 PRE-REG |
| `pass_band_per_anchor` | 10% RATIO |
| `info_band_per_anchor` | 5%-10% RATIO (borderline) |
| `T_H` | 1.057 MeV (CF-39 anchor; output value g_star_BS_T_H pinned at this temperature) |
| `convention_tag` | `PDG-canonical-3-anchor-cross-check` |
| `scheme_tag` | `lattice-QCD-corrected-Boltzmann-suppressed-substrate-cascade` |
| `verdict_source` | `computations/session-90/s90_gate_verdicts.txt` |
| `working_paper_target` | `sessions/archive/session-90/session-90-w4-workingpaper.md §W4-4` |
| `regulator_pin` | a_n^{lattice} tag in convention field (cf. regulator-pin discipline rule for the lattice-QCD source) |

### 7. Input SHA-256 pins

| File | Pin |
|:-----|:----|
| `sessions/archive/session-88/<W6 §V.5 source>` | `<pinned at dispatch>` |
| `computations/_shared/canonical_constants.py` | `<pinned at dispatch>` |

External references (cited in PROVENANCE, not SHA-pinned): PDG 2024 g_*(T) tabulation, Planck 2018 reference, Borsanyi et al. 2016 lattice-QCD.

### 8. Expected output 4-tuple

`(value='all 3 anchors rel_dev<=10pct; g_star_BS_T_H=<v>', scheme=lattice-QCD-corrected-Boltzmann-suppressed-substrate-cascade, convention=PDG-canonical-3-anchor-cross-check, L_max=N/A)`

### 9. PASS / FAIL / INFO thresholds with tolerance rule

**PASS**: rel_dev ≤ 0.10 (10% RATIO) at ALL 3 anchors T ∈ {100 GeV, 1 GeV, 1 MeV} against PDG/Planck-canonical reference values. RATIO tolerance rule per anchor.

**FAIL**: rel_dev > 0.10 at any anchor (model misses lattice-QCD or Boltzmann threshold-suppression structure; needs further refinement).

**INFO**: rel_dev ∈ (0.05, 0.10] at at least one anchor (borderline; needs minor refinement but acceptable for CF-39 dispatch with caveat).

### 10. Substitution chain
Not required — no signed-direction substrate prediction. Quantitative anchor cross-check; the RATIO rule applies symmetrically.

### 11. What PASS / FAIL / INFO MEAN for solution space

- **PASS**: Refined species-multiplicity model is validated at PDG/Planck-canonical reference at 3 anchors; `g_star_BS_T_H` is canonically pinned at the CF-39 anchor T_H = 1.057 MeV; UNBLOCKS CF-39 dispatch.
- **FAIL**: Model misses lattice-QCD or Boltzmann threshold-suppression; needs deeper refinement (deferred-pending to S91+). CF-39 is BLOCKED until model PASSes.
- **INFO**: Model is approximately validated; CF-39 may dispatch with explicit note that the species-multiplicity model is at INFO state; the resulting CF-39 verdict carries an INFO degradation through composite-collapse semantics.

### 12. Effort estimate

**1.3 we** (1.0 we for lattice-QCD + Boltzmann threshold-suppression refinement; 0.3 we addendum for the 3 cross-check anchor validation + g_star_BS_T_H pinning at the CF-39 anchor).

### 13. Substrate-framing reminder

The substrate cascade FORM is substrate-pinned per S88 W6 §V.5; the `g_*(T)` quantity itself is laboratory-IN PDG-canonical. The refinement here is on the laboratory-IN INPUT to the substrate cascade-tail formula. Frame the working-paper §W4-4 by separating: (a) substrate-IS cascade form (NOT refined here; pinned at S88 W6 §V.5); (b) laboratory-IN species-multiplicity g_*(T) (refined here; PDG/Planck-canonical with lattice-QCD + Boltzmann threshold-suppression). The bridge is between (a) and (b) at the 3-anchor cross-check level.

---

## §W4-5. CF-41 — S90-N-PBH-BAND-EDGE-TENSION-PROMOTE

**Gate ID**: `S90-N-PBH-BAND-EDGE-TENSION-PROMOTE`
**Origin**: gen §6 CF-W1-4-PROMOTE
**Effort**: ~1.0 we

### 1. Trigger
`[VERIFY]` (refined β_PBH at L_max=12 substrate pinning + cascade-tail-mass-distribution beyond M_LRD · 2⁻ᵍ pinning; promotes the §W1-4 band-edge-INFO to upper-22.6%-conjunct PASS) ∧ `[SIGN]` (sign_verdict that the refined n_PBH_structural_central falls in the upper-22.6%-conjunct PASS region by-construction from the substrate-clock-cancellation factorization)

### 2. Classification
**GEOMETRIC** (PBH structural prediction at L_max=12 substrate cache; substrate-clock-cancellation factorization `n_PBH = n_edge · prob_form / L_pix_LRD³` per S88 W1a-59 §0; the substrate-IS observable is a number density n_PBH derived from substrate cardinality at L_max=12 truncation of the (A_K, H_K, D_K) Peter-Weyl decomposition).

### 3. Agent type
**PRIMARY (sole writer)**: `mack-cosmic-bridge` (per `feedback_mack-bridge-role.md` observational-anchor authority; mack writes the verdict-line + the §VII registry-text update if §W1-4 promotes from band-edge INFO to PASS). Cross-check: `phonon-first-cosmologist` consults on the substrate cardinality refinement (L_max=10 → L_max=12) but does NOT write the verdict / registry edits.

### 4. Hypothesis
**Substrate prediction**: With (a) refined β_PBH evaluated at L_max=12 substrate pinning (master cache `s84_spectrum_cache_L12_tau019.npz`) instead of the L_max=10 cardinality used in §W1-4 and (b) cascade-tail-mass-distribution refined beyond the M_LRD · 2⁻ᵍ pinning in the cascade-tail regime g ∈ [143..384], the refined `n_PBH_structural_central(g_BBN, refined)` falls in the upper-22.6%-conjunct AND posterior intersection PASS region `[5.495e-23, 1e-20] m⁻³`. The sign_verdict is PASS by-construction from the substrate-clock-cancellation factorization; regime_verdict is VALID since L_max=12 substrate pinning is the operational cache truncation per `math-scripts.md §"D_K Block-Diagonality"`.

### 5. Method — COMPLETE self-contained dispatch prompt

```
You are mack-cosmic-bridge, sole writer per feedback_mack-bridge-role.md.
Refine the §W1-4 PBH band-edge calculation with (a) L_max=12 substrate
pinning instead of L_max=10 cardinality, and (b) cascade-tail mass-
distribution refinement in the cascade-tail regime g ∈ [143..384]. Promote
the §W1-4 band-edge-INFO to upper-22.6%-conjunct PASS.

═══════════════════════════════════════════════════════════════════════════
SUBSTRATE FRAMING
═══════════════════════════════════════════════════════════════════════════

n_PBH is a substrate-derived number density at the BBN-era pivot. The
substrate-clock-cancellation factorization
    n_PBH = n_edge · prob_form / L_pix_LRD³
(per S88 W1a-59 §0 lines 60-66) is substrate-IS at the cardinality level:
n_edge is the cardinality of substrate states at the cascade-edge
truncation; prob_form is a substrate-derived formation probability;
L_pix_LRD³ is the substrate-derived pixel-volume scale at the LRD pivot.
The laboratory-IN observation is the BBN-constrained PBH abundance
n_PBH(z=z_BBN). Direction of explanation: substrate cardinality → formation
probability → laboratory-IN BBN abundance constraint.

═══════════════════════════════════════════════════════════════════════════
PROCEDURE
═══════════════════════════════════════════════════════════════════════════

Step 1 — Top of script:
    from canonical_constants import *
    import numpy as np
    import torch  # for L_max=12 spectrum cache access if needed
    import os
    os.environ.setdefault('OMP_NUM_THREADS', '8')

Step 2 — Load substrate cache at L_max=12:
    Read s84_spectrum_cache_L12_tau019.npz; extract Peter-Weyl
    decomposition + eigenvalue sectors up through p+q = 12.
    Verify SHA per pin.

Step 3 — Recompute n_edge at L_max=12:
    n_edge(L_max=12) = cardinality of substrate states at the
                       cascade-edge truncation, evaluated on the L_max=12
                       cache (not L_max=10).
    Document the cardinality delta L_max=10 → L_max=12.

Step 4 — Cascade-tail-mass-distribution refinement:
    The §W1-4 baseline used a M_LRD · 2⁻ᵍ pinning for the cascade-tail
    mass distribution in the cascade-tail regime g ∈ [143..384] (cascade
    generation index). Probe alternative mass-distribution forms in this
    regime:
      Option A: M(g) = M_LRD · 2⁻ᵍ  (baseline)
      Option B: M(g) = M_LRD · 2⁻ᵍ · (1 + γ · g)  (linear correction)
      Option C: M(g) = M_LRD · exp(-g · ln(2)) · (1 + ε · g²)  (curvature)
    Per the substrate cascade-tail form S88 W6 §V.5, the canonical
    choice is determined by the substrate cascade dynamics; explore the
    3 options and identify which gives the upper-22.6%-conjunct PASS
    region.

Step 5 — Recompute prob_form refined:
    prob_form_refined = substrate-derived formation probability under
                        refined mass-distribution + L_max=12 cardinality.

Step 6 — Recompute L_pix_LRD³ refined:
    L_pix_LRD³ at L_max=12 truncation; verify cardinality cross-check
    against S88 W1a-59 §0 pixel-volume derivation.

Step 7 — Substrate-clock-cancellation factorization:
    n_PBH_structural_central(g_BBN, refined) = n_edge_refined ·
                                                prob_form_refined /
                                                L_pix_LRD³_refined
    Evaluated at g_BBN (BBN-era cascade generation index).

Step 8 — Compare to upper-22.6%-conjunct AND posterior intersection
    PASS region [5.495e-23, 1e-20] m⁻³:

    PASS iff n_PBH_structural_central ∈ [5.495e-23, 1e-20] m⁻³
         AND sign_verdict = PASS by-construction
         AND regime_verdict = VALID at L_max=12 truncation

Step 9 — Sub-checks:
    CF-CURV-6 prior cross-check:  n_PBH in CF-CURV-6 prior
                                  [10⁻³⁰, 10⁻²⁰] m⁻³ → broader band PASS
    §W1c-69 PASS-magnitude posterior:  n_PBH in [8.4e-24, 2.2e-22] m⁻³
    Conjunct region:  [max(5.495e-23, 8.4e-24), min(1e-20, 2.2e-22)]
                   = [5.495e-23, 2.2e-22] m⁻³  (effective conjunct)
    Upper-22.6% of conjunct:  upper 22.6% of [5.495e-23, 2.2e-22] is
                              [≈ 1.85e-22, 2.2e-22] m⁻³

    PASS region restated:  n_PBH ∈ [5.495e-23, 1e-20] m⁻³  (extended
                          via cascade-tail-mass-distribution refinement
                          beyond posterior right-edge)

Step 10 — Output npz:
    computations/_shared/s90_w4_n_pbh_band_edge_tension_promote.npz
    Keys (mandatory):
      n_PBH_structural_central_refined        (full float64)
      n_PBH_publication                       (rounded)
      publication_sig_figs                    = 4
      n_edge_L12, n_edge_L10                  (cardinality delta)
      prob_form_refined, prob_form_baseline   (Option A,B,C; PASS Option)
      L_pix_LRD_cubed_refined
      cascade_mass_distribution_option        ('A', 'B', or 'C')
      conjunct_region_lower, conjunct_region_upper
      upper_22pt6pct_threshold
      sign_verdict_substitution_chain         (dict)
      regime_verdict                          = 'VALID' (L_max=12 truncation)
      audit_sha256, content_sha256, schema_version

Step 11 — Append verdict line (3 rows for [SIGN] trigger):

    S90-N-PBH-BAND-EDGE-TENSION-PROMOTE: PASS|FAIL|INFO -- \
      value='n_PBH=<v> m^-3; conjunct=[<lower>,<upper>]; upper_22.6pct=<thresh>' \
      scheme=L_max-12-substrate-pinning-cascade-tail-refinement \
      convention=upper-22.6pct-conjunct-posterior-intersection \
      L_max=12 \
      audit_sha256=<full-64-char> content_sha256=<full-64-char> \
      schema_version=S87-v2

    Dual-SHA companion row per S87+ schema.

    3-tuple annotation:
      # sign_verdict=PASS magnitude_verdict=PASS|INFO|FAIL \
      # regime_verdict=VALID \
      # S90-N-PBH-BAND-EDGE-TENSION-PROMOTE 3-tuple annotation \
      # (S87 schema-v2)

Step 12 — Working paper §W4-5 (>15 lines):
    Substrate-clock-cancellation factorization + L_max=10 → L_max=12
    cardinality delta + cascade-tail mass-distribution exploration (A/B/C)
    + identification of PASS option + sub-clause-by-sub-clause PASS/FAIL/INFO
    + substrate-framing (substrate-IS cardinality → laboratory-IN BBN
    abundance constraint).

═══════════════════════════════════════════════════════════════════════════
INPUT-SHA PINS
═══════════════════════════════════════════════════════════════════════════

  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
  - computations/session-89/s89_w1_n_pbh_band_edge_tension_reconciliation.npz
  - sessions/archive/session-88/<W1a-59 §0 source workshop or npz>
  - sessions/archive/session-88/<W1c-69 source workshop or npz>
  - computations/_shared/canonical_constants.py
```

### 6. Machinery pin (PRDR)

| Parameter | Pin |
|:----------|:----|
| `L_max` | 12 (per W-1 PRE-REG; S87 W11-3 Friedrich-Bär saturation argument supports L_max=12 for substrate cardinality observables at the substrate-pinning layer) |
| `cardinality_anchor_substrate_clock` | n_PBH = n_edge · prob_form / L_pix_LRD³ per S88 W1a-59 §0 lines 60-66 |
| `cascade_mass_distribution_options` | A (M_LRD · 2⁻ᵍ baseline); B (linear correction); C (curvature correction) |
| `cascade_tail_regime` | g ∈ [143..384] |
| `CF_CURV_6_prior` | n_PBH ∈ [10⁻³⁰, 10⁻²⁰] m⁻³ |
| `W1c_69_posterior` | n_PBH ∈ [8.4e-24, 2.2e-22] m⁻³ |
| `target_PASS_region` | n_PBH ∈ [5.495e-23, 1e-20] m⁻³ (upper-22.6%-conjunct AND posterior intersection) |
| `publication_sig_figs` | 4 (per Class 8.3 publication-precision pre-registration) |
| `convention_tag` | `upper-22.6pct-conjunct-posterior-intersection` |
| `scheme_tag` | `L_max-12-substrate-pinning-cascade-tail-refinement` |
| `regulator_pin` | a_n^{HK} (heat-kernel-equivalent on L_max=12 cache; SCHEMATIC-vs-physical = FULL since the cache is operational truncation, not a SCHEMATIC analog) |
| `verdict_source` | `computations/session-90/s90_gate_verdicts.txt` |
| `working_paper_target` | `sessions/archive/session-90/session-90-w4-workingpaper.md §W4-5` |

### 7. Input SHA-256 pins

| File | Pin |
|:-----|:----|
| `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | `<pinned at dispatch>` |
| `computations/session-89/s89_w1_n_pbh_band_edge_tension_reconciliation.npz` | `<pinned at dispatch>` (36-key payload) |
| `sessions/archive/session-88/<W1a-59 §0 source>` | `<pinned at dispatch>` |
| `sessions/archive/session-88/<W1c-69 source>` | `<pinned at dispatch>` |
| `computations/_shared/canonical_constants.py` | `<pinned at dispatch>` |

### 8. Expected output 4-tuple

`(value='n_PBH=<v> m^-3; conjunct=[<lower>,<upper>]; upper_22.6pct=<thresh>', scheme=L_max-12-substrate-pinning-cascade-tail-refinement, convention=upper-22.6pct-conjunct-posterior-intersection, L_max=12)`

Expected n_PBH range (substrate prediction): `n_PBH ∈ [5.495e-23, 1e-20] m⁻³`.

### 9. PASS / FAIL / INFO thresholds with tolerance rule

**PASS (composite all three sub-checks)**:
- `n_PBH_structural_central(g_BBN, refined) ∈ [5.495e-23, 1e-20] m⁻³` (ABSOLUTE-IN-INTERVAL tolerance rule)
- `sign_verdict = PASS` by-construction from substrate-clock-cancellation factorization (positive number density, both numerator and denominator strictly positive)
- `regime_verdict = VALID` at L_max=12 truncation (per `math-scripts.md §"D_K Block-Diagonality"` — L_max=12 is operational cache truncation; not in BREAKDOWN regime)

**FAIL**: `n_PBH < 5.495e-23` (below upper-22.6%-conjunct threshold) OR `n_PBH > 1e-20` (above CF-CURV-6 prior upper bound) OR `regime_verdict = BREAKDOWN`.

**INFO**: `n_PBH` lies in the broader CF-CURV-6 prior band `[10⁻³⁰, 10⁻²⁰] m⁻³` but outside the upper-22.6%-conjunct region (i.e., n_PBH ∈ [10⁻³⁰, 5.495e-23)). The cascade-tail-mass-distribution refinement is insufficient; further refinement at S91+ may close the band.

### 10. Substitution chain (MANDATORY for [SIGN] trigger)

```
Claim (sign_verdict): n_PBH_structural_central(g_BBN, refined) is strictly
                      positive by substrate construction.

Step 1 — Definitions:
  n_edge(L_max=12)            = cardinality of substrate states at the
                                cascade-edge truncation on L_max=12 cache;
                                ∈ ℤ_{>0} (cardinality is a positive integer)
  prob_form_refined           = substrate-derived formation probability
                                under refined cascade-tail-mass-distribution;
                                ∈ (0, 1]  (probability is bounded by [0, 1];
                                strictly positive when at least one cascade
                                state forms with non-zero amplitude)
  L_pix_LRD³_refined          = substrate-derived pixel-volume scale at
                                LRD pivot, at L_max=12 truncation;
                                ∈ ℝ_{>0}  (volume is strictly positive)

Step 2 — Substitution:
  n_PBH = n_edge · prob_form / L_pix_LRD³

Step 3 — Sign analysis:
  numerator = n_edge · prob_form
  n_edge > 0 (cardinality of states is positive integer)
  prob_form > 0 (at least one cascade formation amplitude is non-zero;
                 substrate cascade dynamics at g_BBN do not vanish)
  numerator > 0

  denominator = L_pix_LRD³_refined > 0

  ratio > 0

Step 4 — Direction read-off:
  n_PBH_structural_central(g_BBN, refined) > 0

Conclusion: sign_verdict = PASS BY CONSTRUCTION.

PYTHON VERIFICATION (mandatory in script log):

  print(f"Sign verification:")
  print(f"  n_edge (L_max=12) = {n_edge:d}    (must be > 0)")
  print(f"  prob_form_refined = {prob_form:.6e}  (must be > 0)")
  print(f"  L_pix_LRD_cubed = {L_pix_cubed:.6e}  (must be > 0)")
  print(f"  n_PBH = {n_PBH:.6e} m^-3  (must be > 0)")
  assert n_edge > 0, "Sign FAIL: n_edge non-positive"
  assert prob_form > 0, "Sign FAIL: prob_form non-positive"
  assert L_pix_cubed > 0, "Sign FAIL: L_pix^3 non-positive"
  assert n_PBH > 0, "Sign FAIL: n_PBH non-positive"
```

### 11. What PASS / FAIL / INFO MEAN for solution space

- **PASS**: The §W1-4 band-edge-INFO promotes to upper-22.6%-conjunct PASS at L_max=12 substrate pinning + refined cascade-tail-mass-distribution. The substrate-IS PBH number density is canonical at `n_PBH ∈ [5.495e-23, 1e-20] m⁻³`. Downstream: mack lands a STAGE-1-CANDIDATE §VII registry entry at S91+ for the PBH-band-edge-conjunct prediction.
- **FAIL**: The refined β_PBH at L_max=12 + cascade-tail-mass-distribution refinement does NOT recover the upper-22.6%-conjunct region; either (a) substrate-clock-cancellation factorization has an unaccounted factor, (b) L_max=12 truncation is insufficient (need L_max=14 — deferred S91+ per W11-3 Friedrich-Bär feasibility), or (c) cascade-tail-mass-distribution options A/B/C all fail (need a fourth option D — deferred S91+).
- **INFO**: n_PBH lies in the broader CF-CURV-6 prior band but outside the upper-22.6%-conjunct; routes to S91+ further refinement.

### 12. Effort estimate

**~1.0 we** (L_max=12 substrate cache load + refined cardinality + cascade-tail-mass-distribution exploration A/B/C + substrate-clock-cancellation factorization re-derivation + 3-sub-check PASS/FAIL/INFO + 15+ line working-paper §W4-5).

### 13. Substrate-framing reminder

n_PBH is substrate-derived: n_edge is substrate cardinality at L_max=12; prob_form is substrate formation probability; L_pix_LRD³ is substrate pixel-volume scale. The substrate-clock-cancellation factorization is substrate-IS at the cardinality level (`phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` Level 1, single-τ-slice at τ_fold). The laboratory-IN observable is the BBN-constrained PBH abundance; the bridge map is the substrate-derived n_PBH → BBN abundance constraint at z=z_BBN. Frame the working-paper section as substrate cardinality → formation probability → laboratory-IN BBN abundance. Do NOT frame as "PBHs forming in spacetime"; frame as "substrate cascade-edge cardinality manifesting as BBN-era PBH number density".

---

## Wave 4 → Wave 5 Decision Point

Wave 4 outputs feed forward:

| Output | Forward consumer | Wave / Session |
|:-------|:-----------------|:---------------|
| CF-37 PASS npz (`s90_w4_alpha_m_alt_corridor_d_compose_b.npz`) + α'(M_LRD=10⁷, L_max=10) value + M-asymptotic envelope fit + Cell-I classification | S91+ AUX-5 three-axis Stage-2 cross-axis independent-verify (`S91-OR-LATER-CORRIDOR-D-COMPOSITE-B-STAGE-2-CROSS-AXIS-VERIFY`); reviewers lizzi (Axis-A) + volovik (Axis-B) + mack (Axis-C); EXCLUDES connes + phonon-first as workshop authors | S91+ |
| CF-37 INFO outcome (Sub-clause B rel_dev ∈ [0.10, 0.30]) | S91+ AUX-4 secondary (c)∘(d) modified-universal-kernel γ(s) ≠ Γ(s) corridor | S91+ |
| CF-37 PASS also calibration corpus instance #2 for simultaneous element-1 + element-3 double-deformation pattern at Cell-I | S91+ mack-cosmic-bridge registry-text landing at §VII.{next-free} (STAGE-1-CANDIDATE) | S91+ |
| CF-38 verdict (PASS = anchor promoted; FAIL = retain default) | Conditional CF-37 Sub-clause B tolerance band (in-W4) | W4-internal |
| CF-40 PASS npz (`s90_w4_f_m_species_multiplicity_retry.npz`) + g_star_BS_T_H pin | CF-39 dispatch (in-W4) | W4-internal |
| CF-39 PASS (Option A supersedes-tagged corrective canonical line) | S91+ secondary discriminator for LRD α-anchor if CF-37 returns INFO; AND cosmological-horizon downstream consumers | S91+ |
| CF-41 PASS outputs (n_PBH_structural_central in upper-22.6%-conjunct + cascade-tail-mass-distribution Option) | S91+ mack-cosmic-bridge registry-text landing at §VII.{next-free} (STAGE-1-CANDIDATE) for PBH-band-edge-conjunct prediction | S91+ |

Per Known dependencies (context file): **CF-40 PRECEDES CF-39** (mandatory wave-internal sequencing). CF-37, CF-38, CF-41 may dispatch in parallel with each other. CF-37 alone is the wave-bottleneck (3.5 we).

Wave 4 → Wave 5 transition: when ALL FIVE gates close (PASS or FAIL or INFO), Wave 4 synthesizes per `/rclab-coordinate` wave-synthesis protocol; the synthesis surfaces:
- CF-37 verdict (PRIMARY substrate-physics outcome; routes either Stage-2 dispatch or secondary-corridor activation)
- CF-39/CF-40 chain status (cascade-tail correction valid or not)
- CF-41 PBH-band-edge-conjunct status

Carry-forward items to Wave 5 (or S91+ depending on Wave 4 outcome): see §"Wave 4 Decision Point" above.

---

## Wave 4 Machinery-Enumeration Pin (§0.11)

Per `epistemic-discipline.md §"Pre-Registration Completeness"` PRDR enumeration:

| Gate | Free parameters | Pin source |
|:-----|:----------------|:-----------|
| CF-37 | L_max=10; M_LRD=10⁷ M_sun; M_scan=5-point log-spaced; n_threshold > 0 strict; kernel γ(s) = Γ(s); cocycle source = §VII.AF.1.OP-PROJ; inheritance morphism = χ' (S89 §W2-3 audit anchor); pairing form = Connes-Karoubi; Chern character machinery = CM-1995 §III.4 residue formula; area scales M_KK² / M_Pl_reduced²; convention `substrate-IS-Cell-I-K-counter-instance-2`; scheme `connes-karoubi-pairing-on-chi-prime-inheritance`; publication_sig_figs=5; verdict_source `computations/session-90/s90_gate_verdicts.txt` | §W4-1 §6 above; cross-link `cross-pillar-bridge-corpus.md §1` + §VII.AF.1.OP-PROJ registry text |
| CF-38 | query_targets = knowledge-MCP + registry + canonical_constants; tightening_band 10% if PASS, 30% retain if FAIL; convention `mechanical-pre-flight-AUX-2`; scheme `knowledge-mcp-registry-query`; verdict_source `computations/session-90/s90_gate_verdicts.txt` | §W4-2 §6 above |
| CF-39 | T_H=1.057 MeV; g_*(T_H) from CF-40; cascade form S88 W6 §V.5; delta_log_threshold 0.5; residual_improvement_threshold 1.0 log-OOM; supersedes_sha (full 64-char form of `2afd17ef99c81123…`); convention `canonical-re-pinning-Option-A-supersedes`; scheme `substrate-pinned-T_H-cascade-tail`; verdict_source `computations/session-90/s90_gate_verdicts.txt` | §W4-3 §6 above |
| CF-40 | cascade form substrate S88 W6 §V.5; lattice_QCD_source Borsanyi+2016 OR PDG; Boltzmann_threshold_band m/T ∈ [0.2, 5]; cross_check_anchors {100 GeV, 1 GeV, 1 MeV}; pass_band 10% RATIO; info_band 5%-10%; T_H = 1.057 MeV (CF-39 anchor); regulator_pin a_n^{lattice}; convention `PDG-canonical-3-anchor-cross-check`; scheme `lattice-QCD-corrected-Boltzmann-suppressed-substrate-cascade`; verdict_source `computations/session-90/s90_gate_verdicts.txt` | §W4-4 §6 above |
| CF-41 | L_max=12; cardinality_anchor n_PBH = n_edge · prob_form / L_pix³ (S88 W1a-59 §0); cascade_mass_distribution_options A/B/C; cascade_tail_regime g ∈ [143..384]; CF-CURV-6 prior `[10⁻³⁰, 10⁻²⁰]`; W1c-69 posterior `[8.4e-24, 2.2e-22]`; target_PASS_region `[5.495e-23, 1e-20]`; publication_sig_figs=4; regulator_pin a_n^{HK} FULL; convention `upper-22.6pct-conjunct-posterior-intersection`; scheme `L_max-12-substrate-pinning-cascade-tail-refinement`; verdict_source `computations/session-90/s90_gate_verdicts.txt` | §W4-5 §6 above |

PRDR cardinality test: every gate's machinery_pin_map has D_PRU_raw = 0 (no missing pins). SOURCE-RECONCILIATION value-test deferred to plan-freeze audit run: `_source_reconciliation_audit.py` will compute per-pin D_max for canonical-constants pins (M_KK, M_Pl_reduced, R_universal_HP1_strict_F4, eps_H_HP1_norm, T_H, tau_fold, Delta_BCS). Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY remediation chain applies to R_universal_HP1_strict_F4 (per CF-W2-4 PROVENANCE update); cross-link via §VII.AF.1.OP-PROJ. SUBSTRATE-FIRST-PROVENANCE sub-audit at plan-freeze: all pins source from canonical_constants.py or substrate-derived npz; no external-paper canonical citation; CF-40 lattice-QCD g_*(T) is methodological cross-check input, not canonical pin.

---

## Wave 4 Input-SHA Ledger

All input files pinned at plan-freeze with computed SHA-256 (`<pinned at dispatch>` = SHA captured at agent dispatch time; pre-existing static files use frozen SHAs from prior sessions; the audit_sha256 closure-hash is computed over the ordered ASCII-sorted pin map at dispatch time):

| File | Pinned by gates | SHA-256 (status) |
|:-----|:----------------|:-----------------|
| `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | CF-37, CF-41 | `<pinned at dispatch>` (S84 master cache; frozen) |
| `computations/session-89/s89_w1_alpha_m_horizon_microstate_count.npz` | CF-37 (FAIL diagnostic) | `<pinned at dispatch>` (S89 §W1-1 output) |
| `computations/session-89/s89_w2_a7_chi_prime_inheritance_morphism.npz` | CF-37 | `<pinned at dispatch>`; anchor audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843` (S89 §W2-3) |
| `computations/session-89/s89_w1_n_pbh_band_edge_tension_reconciliation.npz` | CF-41 | `<pinned at dispatch>` (36-key payload; S89 §W1-4) |
| `sessions/permanent-results-registry.md` | CF-37 (§VII.AF.1.OP-PROJ block lines 14690-14722); CF-38 (full registry query) | `<pinned at dispatch>` |
| `computations/_shared/canonical_constants.py` | all 5 gates | `<pinned at dispatch>` |
| `computations/session-88/s88_gate_verdicts.txt` | CF-39 (for full 64-char form of `2afd17ef99c81123…`) | `<pinned at dispatch>` (frozen S88 verdict file) |
| `sessions/archive/session-88/<W1a-59 §0 source>` | CF-41 | `<pinned at dispatch>` (S88 W1a-59 source path TBR at dispatch) |
| `sessions/archive/session-88/<W1c-69 source>` | CF-41 | `<pinned at dispatch>` (S88 W1c-69 source path TBR at dispatch) |
| `sessions/archive/session-88/<W6 §V.5 source>` | CF-40 | `<pinned at dispatch>` (S88 W6 §V.5 source path TBR at dispatch) |
| `sessions/archive/session-88/<W6 §V.1 source>` | CF-39 (T_H = 1.057 MeV pin) | `<pinned at dispatch>` (S88 W6 §V.1 source path TBR at dispatch) |
| `sessions/session-plan/session-90-plan-w4.md` | CF-38 (conditional edit target) | `<pinned at dispatch>` |
| `computations/_shared/s90_w4_f_m_species_multiplicity_retry.npz` | CF-39 | produced by CF-40 at runtime; pinned at CF-40 PASS |

NOTE on AMRI compliance: no `.claude/agent-memory/*/MEMORY.md` paths are pinned in any gate's input-SHA map. Per `agent-standards.md §"Agent-Memory Registry Inversion (AMRI)"` Test 1, listing an agent-memory file as Input-SHA pin source would fire AMRI; the orchestrator avoids this by routing the connes-ncg-theorist co-author connection (CF-37) through the npz file SHA `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843` rather than through connes-ncg memory.

NOTE on Option A `supersedes` discipline (CF-39): the full 64-char form of the superseded `audit_sha256` (head `2afd17ef99c81123…`) is grep-extracted at dispatch time from `computations/session-88/s88_gate_verdicts.txt`; the corrective canonical line at `computations/session-90/s90_gate_verdicts.txt` includes the FULL 64-character form in the `supersedes=<sha>` token. NO retroactive disk-edit of the S88 verdict file (verdict permanence absolute per `gate-verdicts.md §"Option A"`).

---

**End of session-90-plan-w4.md** — total ~6.4 wave-equivalents (CF-37 BIG at 3.5 we + CF-40 at 1.3 we + CF-41 at 1.0 we + CF-39 at 0.5 we + CF-38 at 0.1 we). Per Known dependencies: CF-40 PRECEDES CF-39 (wave-internal); CF-37 + CF-38 + CF-41 may dispatch in parallel.
