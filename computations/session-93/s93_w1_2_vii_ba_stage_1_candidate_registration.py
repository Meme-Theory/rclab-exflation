#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S93-W1-2-VII-BA-STAGE-1-CANDIDATE-REGISTRATION
==============================================

Registers the JOINT TWO-AXIS composite-bridge-map dimensional-class
admissibility theorem as STAGE-1-CANDIDATE in
`sessions/permanent-results-registry.md`, AUGMENTING the existing §VII.BA
section (the S91 W9-9 / S91 W1-14 layer-functor-F Wodzicki-BCS STAGE-1-CANDIDATE
entry, line 19676) with the JOINT TWO-AXIS clause text co-frozen at the S92 W-1
workshop Stage-0 freeze (`s92-vii-ba-composite-bridge-map-dimensional-class.md`,
CONVERGED 2026-05-23; corpus §18.0 directive + §18.1 K=1 instance).

This is a METHODOLOGY-class registry-landing gate per `wave-classification.md`
(M1 artifact-existence-with-substantive-content PASS predicate; M2 registry
Write + SHA-256 cross-checks; M3 verbatim Stage-0-frozen clause text from the
S92 W-1 workshop + corpus §18.0/§18.1). The producing script reads NO D_K
eigenvalues — it registers frozen clause text. mack-cosmic-bridge is the SOLE
registry writer per `feedback_mack-bridge-role.md`.

Single-shot bridge-landing AFTER pattern per
`registry-landing.md §"Bridge-Landing Script Architecture"` +
`computations/_bridge_landing_script_template.py`:
    build_promotion_text  ->  write_atomic_with_fsync  ->
    re_read + verify_section_matches  ->  emit-ONCE
No conditional rewrite / re-emit. A verify-FAIL emits FAIL once and the gate
closes honestly per `mechanical-closure-discipline.md`.

Audit-trail observation (BEFORE-pattern double-trio hazard avoided):
`computations/_bridge_landing_audit_trail_observation_S87_W5.md`.

The §VII.BA slot is NOT one of the 7 STAGE-3-collision slots reserved by
`sessions/framework/s93-slot-pre-allocation-lockfile.md` (AU/AW/AY/AV/AX/BB/BE);
this Stage-1 augmentation does NOT introduce a NEW `### §VII.*` header — the
joint sub-block lands as a `#### (h)` sub-section INSIDE the §VII.BA section
boundary (before the `### §VII.BB` header), so the cross_pillar_bridge_audit
BRIDGE_SECTION_REGEX keeps it within §VII.BA (no slot-label collision).

Verdict: [VERIFY-THEOREM]. METHODOLOGY-class dual-SHA closure
(`content_sha256` over the augmented §VII.BA section text; `audit_sha256` over
the input-pin map of source documents) per
`wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`.
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import re
import sys
from pathlib import Path

# --- canonical constants (mandatory per .claude/rules/math-scripts.md S34+) ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"  # (local)
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import Delta_BCS, M_KK, tau_fold  # noqa: F401

# _cross_pillar_bridge_audit verification pass (12-condition audit)
from _cross_pillar_bridge_audit import (  # noqa: E402
    audit_section,
    detect_composite_bridge_map_taxonomy,
    find_bridge_sections,
)

# ---------------------------------------------------------------------------
# Gate identity + canonical paths
# ---------------------------------------------------------------------------
GATE_ID = "S93-W1-2-VII-BA-STAGE-1-CANDIDATE-REGISTRATION"  # (local)
SCHEME = "registry-text-augmentation-AFTER-pattern-single-shot"  # (local)
CONVENTION = (  # (local)
    "VII-BA-joint-two-axis-composite-bridge-map-STAGE-1-CANDIDATE-"
    "clauses-a-e-connes-binding-mack-c-JOINT-corpus-18"
)
L_MAX = "N/A"  # (local) registry-landing of frozen clause text; no new compute

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-93" / "s93_gate_verdicts.txt"  # (local)
NPZ_PATH = (  # (local)
    PROJECT_ROOT
    / "computations"
    / "session-93"
    / "s93_w1_2_vii_ba_stage_1_candidate_registration.npz"
)

# Input-pin map (source documents the registration consumes; SHAs feed audit_sha256).
INPUT_FILES = [  # (local)
    REGISTRY_PATH,
    PROJECT_ROOT / "sessions" / "framework" / "registry" / "cross-pillar-bridge-corpus.md",
    SHARED_DIR / "_cross_pillar_bridge_audit.py",
    PROJECT_ROOT / "computations" / "_bridge_landing_script_template.py",
]

# Workshop closure SHA (Stage-0 freeze) — the §W1-4 composite Wodzicki∘HKR face,
# the FIRST evidence anchor of the joint theorem (corpus §18.1 face table).
WORKSHOP_CLOSURE_SHA = (  # (local)
    "fbfdbca22b5ec127de187a00ead168d5ffff6bee10755875d80182cc7878c129"
)
# §W2-3 M_KK^5 normalization-scalar face (the SECOND evidence anchor; T2 VACUOUS).
W2_3_FACE_SHA = (  # (local)
    "5395d9228df93174275531c15c27e6d618474d9c736282ae155d0223463b34fb"
)
# Insertion boundary: the joint sub-block lands immediately BEFORE this header,
# keeping the new text inside the §VII.BA section per BRIDGE_SECTION_REGEX.
NEXT_SECTION_HEADER = "### §VII.BB — HH^1 Cocycle Norm at Substrate-Distance-3"  # (local)


# ---------------------------------------------------------------------------
# SHA helpers (canonical dual-SHA per the S84+ schema; matches
# computations/_shared/s93_w0_1_stage_3_promotion_sequencing_prereg.py)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return "0" * 64


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    section_text: str, pins: dict[str, str]
) -> tuple[str, str]:
    """Dual-SHA per wave-classification.md §"Dual-SHA closure for METHODOLOGY-class".

    content_sha256 = SHA-256 over the augmented §VII.BA section text (the F-image
                     of the numerical PASS-predicate eigenvalue under
                     substrate <-> methodology per epistemic-discipline.md
                     §"Layer-Decomposition").
    audit_sha256   = SHA-256 over the input-pin map of source documents.
    """
    h_content = hashlib.sha256()  # (local)
    h_content.update(section_text.encode("utf-8"))
    content = h_content.hexdigest()  # (local)

    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(pinmap_json)
    # per-gate identity keys embedded so audit_sha256 is gate-distinct
    h_audit.update(f"{GATE_ID}|{SCHEME}|{CONVENTION}".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Step (1) — build_promotion_text  (pure function; no I/O)
# ---------------------------------------------------------------------------
def build_joint_subblock() -> str:
    """The JOINT TWO-AXIS sub-block text. Pure; substrate-IS -> bridge -> lab-IN.

    Lands as a `#### (h)` sub-section INSIDE the §VII.BA section. Carries:
      - STAGE-1-CANDIDATE tag on the sub-section name line
      - the joint theorem statement (Stage-0-frozen, corpus §18.0)
      - 5 IS-not-IN anatomy elements (Element 3 = composite B=f⊙g + taxonomy)
      - 3-level structural-confidence ladder (Level-1 FI THEOREM / Level-2-B RD
        DIAGNOSTIC / Level-3 per-formulation anchor)
      - clause attributions (a)/(e) connes + (binding) mack + (c) JOINT-flagged
      - workshop closure SHA pin + corpus §18.0/§18.1 cites

    Element-2 OE-form: written operator-expression-first (∫...dE...Tr_{M_2(ℂ)}
    (P_BdG · ...)) to satisfy ELEMENT_2_OE_POSITIVE_REGEX and AVOID the
    negative-match (no "Element 2 ...: <prose> measurement.|test.|spectroscopy.").
    """
    delta_bcs = f"{Delta_BCS:.16g}"  # (local) R-PROTECTED dimensionless ratio
    return f"""#### (h) JOINT TWO-AXIS Composite-Bridge-Map Dimensional-Class Admissibility Theorem (STAGE-1-CANDIDATE — S93 W1-2)

**STAGE-1-CANDIDATE tag**: per `joint-theorem-promotion.md` §"Stage 1 — S87 (next-session) Registration as Candidate". This sub-section registers a SECOND, structurally distinct §VII.BA theorem co-located with the §(a)-(g) layer-functor-F Wodzicki-BCS theorem above: the **JOINT TWO-AXIS composite-bridge-map admissibility theorem** whose Element 3 is a COMPOSITE bridge map `B = f⊙g` (NOT the single F-functor of §(a)-(g)). Stage 0 (workshop-internal authoring) is the S92 W-1 §VII.BA composite-bridge-map dimensional-class workshop (`sessions/archive/session-92/workshops/s92-vii-ba-composite-bridge-map-dimensional-class.md`, CONVERGED 2026-05-23; connes-ncg-theorist + mack-cosmic-bridge); the clause text was Stage-0-frozen at that workshop and recorded in `sessions/framework/registry/cross-pillar-bridge-corpus.md §18.0` (DIRECTIVE) + `§18.1` (K=1 calibration instance). Stage 1 (this entry) registers the joint theorem as CANDIDATE with all 5-anatomy elements + 3-level ladder + joint-clause flags. Stage 2 (two-agent parallel cross-axis verify) is queued: Axis-A (spectral/NCG-axiomatic) = `connes-ncg-theorist`; Axis-B (substrate/superfluid-universe) selection EXCLUDES `volovik-superfluid-universe-theorist` per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` (original-authoring + downstream-inheritance reach). Stage 3 (STAGE-3-PERMANENT) CONDITIONAL on Stage-2 PASS-AND across both axes with the substrate-input-orthogonality predicate satisfied at >= 1 observable (the §W1-4 envelope-alpha data file vs the §W2-3 normalization-cancellation data file, loaded by SEPARATE reviewers) per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` MANDATORY-K=3.

> **Theorem text (statement; Stage-0-frozen at S92 W-1; corpus §18.0)**:
>
> "Let `(A_K, H_K, D_K)` be the framework's NCG-axiomatic spectral triple at `tau_fold = {tau_fold}` with `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. Let `B = f⊙g` be a COMPOSITE bridge map (Element 3 of the 5-anatomy block) at substrate-distance pole `s>0`, with canonical Level-3 anchor of homogeneity degree `d_A`. Then `B` is **admissible** iff BOTH conjuncts hold: **(Conjunct 1 — homogeneity axis)** `deg(B) = d_A` — the Wodzicki-trace factor `Res_W` carries degree `−2s ≠ 0` by Wodzicki uniqueness (the trace on `Ψ(A_K)` is unique up to scalar; Connes 1994 §2.3), the HKR factor carries degree `0` by the orientability axiom + Chern character (Connes 1994 §III axiom 6 / §4); `d_τ(s) = −2s` is an index-type invariant, non-deformable in moduli, so no pole `s>0` reaches `d_τ→0` (boundary `s=0`, `ζ_D(0)`, carries no coupling/BCS-sector content). **(Conjunct 2 — substrate-natural-binding axis)** `B` carries non-trivial substrate-natural L_max-dependence that survives the dimensionless ratio — a degree-match achieved by a canonical-import SCALAR (unit conversion) is VACUOUS (it cancels in the dimensionless ratio with no L_max-dependence to close the numerical gap); admissible degree-matching requires a substrate-natural structural morphism (a same-class ratio at distinct poles, or a K_0-pairing carrying the substrate's own inheritance-class degree). The conjunction is IRREDUCIBLE: T1 satisfies conjunct 2 but fails conjunct 1 (wrong degree); T2 and T4|_{{s=s'}} satisfy conjunct 1 but fail conjunct 2 (scalar corrector / equal-pole cancellation); neither conjunct alone excludes both forbidden classes. Operational equivalent test: `B` is two-axis-admissible iff the cross-secondary-class scheme-spread `Δ_scheme(B) → machine-zero` across {{APS-1975-secondary-class, Cheeger-Simons, Bismut-Cheeger}} — necessary ∧ sufficient on the secondary-class-suffix axis."

**Joint-clause attribution + flags** (per `joint-theorem-promotion.md §"Stage 1"`; corpus §18.0 "Joint-theorem-promotion" cross-link):

| Clause | Content | Author-side | JOINT? | Stage-2 verify |
|:-------|:--------|:------------|:-------|:---------------|
| (a) | homogeneity-degree obstruction: `deg(Res_W) = −2s ≠ 0` (Wodzicki uniqueness) + `deg(HKR) = 0` (orientability + Chern) | **connes** (NCG-axiomatic / spectral) | no (single-axis) | Axis-A connes |
| (e) | pole-scoping + index-rigidity: `d_τ(s) = −2s` non-deformable in moduli; no pole `s>0` reaches `d_τ→0`; boundary at `s=0` | **connes** (NCG-axiomatic / spectral) | no (single-axis) | Axis-A connes |
| (binding) | a degree-match by a canonical-import SCALAR is VACUOUS; admissible degree-matching requires a substrate-natural structural morphism (T3 / T4 at s≠s' / T5) | **mack** (cosmic-bridge / substrate-natural-binding) | no (single-axis) | Axis-B (mack-side) |
| (c) | `Δ_scheme(B) → machine-zero` across {{APS-1975 / Cheeger-Simons / Bismut-Cheeger}} is necessary ∧ sufficient on the secondary-class axis | **JOINT** (homogeneity ∧ substrate-natural-binding) | **YES — JOINT-FLAG** | PASS-AND across Axis-A connes ∧ Axis-B mack-side (both must independently PASS) |

The **JOINT-FLAGGED** clause (c) requires Stage-2 PASS-AND across BOTH axes (logical AND, not OR) per `joint-theorem-promotion.md §"Stage 2"`. Clauses (a)/(e) are connes-side single-axis; clause (binding) is mack-side single-axis.

##### 5-IS-not-IN Anatomy Elements (composite-Element-3 case)

Per `cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy (5 elements)"` MANDATORY-K=3 + §"Composite Bridge-Map Dimensional-Class Admissibility":

- **Element 1 (substrate-IS observable)**: `Res_W(D_K^{{-2s}})` on `A_K` at `L_max = 12`. The substrate IS the Wodzicki residue (the unique trace on the pseudodifferential ideal `Ψ(A_K)`, a substrate-intrinsic functional NOT a container-side accounting) at substrate-distance pole `s`. **EXPLICIT LEVEL TAG**: Level 1 single-τ-slice at `tau_fold = {tau_fold}` per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY. The homogeneity degree `deg(Res_W) = −2s` is intrinsic to D_K's eigenvalue spectrum — upstream of every truncation/regularization scheme.

- **Element 2 (laboratory-IN observable; OE-form MANDATORY per S88 W7a-75)**: the composite's degree-0 Level-3 anchor is the HKR cohomology RATIO image at Pillar V (3He-B superfluid/BdG), specified in operator-expression form
  ```
  Δ_BCS_lab = ∫_0^{{Λ_UV}} dE · Tr_{{M_2(ℂ)}}(P_BdG · G_E^{{(R)}}(E))
  ```
  with **integration domain** `∫_0^{{Λ_UV}} dE` over BdG quasiparticle energies `E ∈ [0, Λ_UV]`; **trace** `Tr_{{M_2(ℂ)}}` over the BdG sub-algebra `A_BdG = M_2(ℂ) ⊂ A_K`; **named projector** `P_BdG ≡ Π^{{BdG}}_{{Nambu-Gor'kov}}` (the Nambu-Gor'kov spinor projector). The R-PROTECTED canonical `Δ_BCS = {delta_bcs}` (M_KK units = dimensionless ratio; S70 `BCS-GAP-CANONICAL-70`) is the degree-0 anchor against which the composite's degree is matched. OE-form satisfied: integration domain (∫dE) + trace (Tr_{{M_2(ℂ)}}) + named projector (P_BdG) all present.

- **Element 3 (bridge map — COMPOSITE)**: `B = f⊙g`, a composite of a trace SUM factor (`Res_W`, deg `−2s`) and/or a cohomology RATIO factor (HKR `ρ_FULL`, deg `0`). Five-formulation taxonomy (substrate-distance-1 pole `s=3`, operator power `|λ|^{{−6}}`; type theorem pole-universal for `s>0`):
  - **T1** `Res_W(s)·ρ_FULL(s)` — (trace SUM, deg −2s) × (cohomology RATIO, deg 0) — deg `−2s ≠ 0` — **FORBIDDEN** (conjunct 1; §W1-4 α=−3.41).
  - **T2** `N·Res_W(s)`, `N` scalar — (trace SUM) × (constant) — deg `d_A` by construction — **FORBIDDEN / VACUOUS** (conjunct 2; scalar cancels in the dimensionless ratio; §W2-3 `ratio_pre = ratio_post = 3.769067e+05`).
  - **T3** `ρ_FULL(s)/ρ_FULL(s')` — (cohomology RATIO)/(cohomology RATIO) — deg `0` — **ADMISSIBLE** (both conjuncts pass; degree-0 FI cohomology target).
  - **T4** `Res_W(s)/Res_W(s')` (same algebra) — (trace SUM)/(trace SUM) — deg `2(s'−s)` — **ADMISSIBLE iff s≠s'** matched to a degree-`2(s'−s)` anchor; **T4|_{{s=s'}} ≡ 1 → FORBIDDEN/VACUOUS** (equal-pole ratio carries zero L_max-dependence; conjunct 2 fail — the SHARPEST forbidden-cell witness).
  - **T5** `⟨[φ], Ch(P_0)⟩` direct Connes-Karoubi K_0-pairing — single cohomology pairing — index-fixed degree — **ADMISSIBLE** iff the K_0 class is the substrate's own χ-image BdG inheritance class (not a canonical-import reference class).
  **Admissible re-route** (per corpus §18.0 cross-link CF-S93-W2-1): the Element-3 F-functor image-normalization morphism Φ MUST adopt a degree-matched NON-SCALAR morphism **T3 / T4|_{{s≠s'}} / T5** (executed at S93 W1-3 `S93-W1-3-VII-BA-F-FUNCTOR-NON-SCALAR-RECONSTRUCTION`); a T2 canonical-import scalar is a Class-8 PRU plan-authorship defect detectable before compute. **Element 3 binding type**: (i) substrate-self-consistent. **Binding axis**: SUBSTRATE-NATURAL-BINDING. **Bridge-map class**: composite (SUM)/(RATIO) — distinct from the single F-functor of §(a)-(g) and from {{HKR, K-theory boundary, Connes-Karoubi pairing}} taken singly; the COMPOSITE structure is the HIT axis-(iii) distinct bridge-map class.

- **Element 4 (algebraic envelope)**: per-formulation convergence rate `L^{{−α(s)}}` at d=4. For a FORBIDDEN composite (T1) the truncated envelope diverges (Res_W-dominated `~L^{{3.4}}` against a degree-0 anchor ⇒ α<0; §W1-4 `α_composite_Wodzicki = −3.411597` at R²=0.999997). For an ADMISSIBLE re-route (T3/T4|_{{s≠s'}}/T5) the envelope `L^{{−α}}` binds the degree-matched Level-3 anchor (the Level-3<Level-2 PASS-test, executed at W1-3). **Level-2 sub-class**: Level-2-B RD DIAGNOSTIC (the numerical envelope exponent α(s, regulator) is pole + UV-regulator keyed; shifts across {{ζ, Pauli-Villars, Mellin}} but stays negative-sign for a forbidden composite; NEVER a Level-1 dissolution).

- **Element 5 (empirical anchor)**: the two evidence faces of the SINGLE substrate fact `deg(Res_W) = −2s ≠ 0` (corpus §18.1): (i) envelope-exponent face `S92-W1-CF-W9-8-1-COMPOSITE-BRIDGE-MAP-WODZICKI-HKR` (FAIL; `α=−3.411597`; `Res_W(L=8/10/12)={{4.346e4, 9.340e4, 1.750e5}}~L^{{3.4}}` SUM; `HKR(L)={{1.0196, 1.0137, 1.0101}}→~1.008` RATIO; degree-0 anchor `1.0076927826`; audit_sha256=`{WORKSHOP_CLOSURE_SHA}`); (ii) normalization-scalar face `S92-W2-CF-W9-9-1-WODZICKI-F-FUNCTOR-M-KK-5-NORMALIZATION` (FAIL; scalar `N=M_KK^5`; `ratio_pre = ratio_post = 3.769067e+05`, `M_KK_cancels_in_ratio=TRUE`; audit_sha256=`{W2_3_FACE_SHA}`). The `Δ_scheme` operational anchor: `S91-BRIDGE-MAP-SCHEME-INDEPENDENCE-AUDIT` Reading A returned `max_pairwise_diff = 0.000000e+00` across {{APS-1975 / Cheeger-Simons / Bismut-Cheeger}} (`GV_APS_L12 = GV_CS_L12 = −1.2081580929e+08` to float64) — a degree-matched odd-grading object machine-zero across the three secondary-class schemes (CF-55 K=1 anchor).

##### Three-Level Structural-Confidence Ladder

Per `cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"` MANDATORY-K=3 + §"Composite Bridge-Map Dimensional-Class Admissibility" Level-classification:

- **Level 1 — STRUCTURAL THEOREM (FI, pole-universal, four-axis-invariant)**: the (SUM)×(RATIO) [conjunct-1 fail] and (degree-matched scalar / equal-pole) [conjunct-2 fail] inadmissibility is INVARIANT on all four pin axes (UV-regulator, Level, MACHINERY-SCOPE, Binding per `regulator-pin-discipline.md §"four-axis orthogonality"`). Double-warranted: PROOF (Wodzicki uniqueness + HKR degree-0) AND MEASUREMENT (CF-55 machine-zero scheme-spread). Regulator-INVARIANT; L-INDEPENDENT; holds at every pole `s>0`; boundary at `s=0`. This is the substrate-IS structural identity at the cohomology-class / homogeneity-degree layer.

- **Level 2 — STRUCTURAL PREDICTION (Level-2-B RD, pole + UV-regulator-keyed DIAGNOSTIC)**: the numerical envelope exponent `α(s, regulator)`; L_max-dependent; algebraically derived; shrinks in magnitude as `s` grows; shifts across UV-regulators but stays negative-sign for a forbidden composite. The algebraic convergence envelope `L^{{−α(s)}}` at d=4. NEVER a Level-1 dissolution (a Level-2-B sub-row reading cannot veto the Level-1 structural THEOREM per `cross-pillar-bridge-anatomy.md` Level-2 sub-class discipline).

- **Level 3 — EMPIRICAL CONFIRMATION (per-formulation anchor)**: per-formulation PASS test (Level-3 < Level-2 at canonical L_max). T1 / T2 / T4|_{{s=s'}} FAIL (the forbidden cells; numerical anchor at canonical `L_max = 12`: §W1-4 `α=−3.41` FAIL; §W2-3 `ratio_pre=ratio_post` FAIL). T3 / T4|_{{s≠s'}} / T5 to be computed (the admissible re-route; W1-3 executes the degree-matched NON-SCALAR Φ reconstruction at L_max=12 with the Friedrich-Bär asymptote where the cache binds).

**Registry-PASS criterion** (per `cross-pillar-bridge-anatomy.md §"Registry-PASS criterion"`): Level-3 empirical value < Level-2 envelope at canonical L_max, counted toward registry-PASS only when Level-2 is Level-2-binding. **STAGE-1-CANDIDATE deferred**: the full Registry-PASS is CONDITIONAL on Stage-2 cross-axis PASS-AND at S93/S94 (the admissible-re-route Level-3 anchor lands at W1-3; the substrate-input-orthogonality predicate at >= 1 observable is verified at the §VII.BA joint Stage-2). This Stage-1 entry pre-registers the structural ladder for downstream consumption. (`REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` of the admissible-re-route Level-3 anchor; the FORBIDDEN-cell Level-3 anchors T1/T2/T4|_{{s=s'}} are already extracted and FAIL by construction — that is the wall, not an incompleteness.)

##### Provenance + Cross-References

> **Provenance**: S92 W-1 §VII.BA composite-bridge-map dimensional-class workshop (`sessions/archive/session-92/workshops/s92-vii-ba-composite-bridge-map-dimensional-class.md`; CONVERGED 2026-05-23; connes-ncg-theorist + mack-cosmic-bridge). Stage-0-frozen clause text + K=1 calibration instance: `sessions/framework/registry/cross-pillar-bridge-corpus.md §18.0` (DIRECTIVE) + `§18.1` (the N=2 SUM-factor corpus: Wodzicki∘HKR §W1-4 α=−3.41 + MS∘HKR `S91-W1-14-COMPOSITE-BRIDGE-MAP-RDX` α=−1.518765). Workshop closure SHA (first evidence face): `{WORKSHOP_CLOSURE_SHA}`. Sole registry writer: mack-cosmic-bridge per `feedback_mack-bridge-role.md`.
>
> **THIRD framework joint cross-axis theorem** to enter the `joint-theorem-promotion.md` 4-stage pathway (after §VII.AH and Var_a). Stage-2 cross-axis verify queued: Axis-A = `connes-ncg-theorist` (clauses (a)/(e) + JOINT (c)); Axis-B (mack-side, EXCLUDING volovik) audits clause (binding) + JOINT (c); JOINT clause (c) PASS-AND'd across both. Substrate-input-orthogonality at >= 1 observable: the §W1-4 envelope-α data file (`s92_w1_cf_w9_8_1_composite_bridge_map_wodzicki_hkr.npz`) loaded by ONE reviewer, the §W2-3 normalization-cancellation data file by the OTHER.

- `cross-pillar-bridge-anatomy.md §"Composite Bridge-Map Dimensional-Class Admissibility"` (the joint two-axis criterion + five-formulation taxonomy; SUGGESTION at K=1; corpus §18).
- `cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy (5 elements)"` MANDATORY-K=3 (all 5 elements populated; Element 3 = COMPOSITE bridge map).
- `cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"` MANDATORY-K=3 (Level-1 FI THEOREM / Level-2-B RD DIAGNOSTIC / Level-3 per-formulation anchor).
- `joint-theorem-promotion.md §"Stage 1"` (STAGE-1-CANDIDATE tag); §"Stage 2" (JOINT clause (c) PASS-AND); §"Substrate-input-orthogonality clause" MANDATORY-K=3.
- `epistemic-discipline.md §"Layer-Decomposition"` (the four-axis-invariance basis of the Level-1 FI claim).
- `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"` (direction substrate → emergent, below).
- `registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"` (this entry landed via the AFTER pattern; exactly one canonical verdict line).
- Downstream consumers: CF-S93-W2-1 / S93 W1-3 (Element-3 F-functor NON-SCALAR reconstruction); CF-S94-W1-6 (α_s direct-Connes-Karoubi T5 recovery at the a_4 channel, s=2 — a NEW cross-pillar bridge requiring the full 5-anatomy + Stage-2 PASS-AND).

##### Substrate Framing

Per `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"`:

**Substrate IS the NCG-axiomatic spectral triple `(A_K, H_K, D_K)`** at `tau_fold = {tau_fold}`. The Wodzicki residue `Res_W: Ψ(A_K) → ℂ` IS the substrate's intrinsic algebraic-trace functional on the pseudodifferential ideal; its homogeneity degree `−2s` IS intrinsic to D_K's eigenvalue spectrum (Wodzicki uniqueness), NOT an imported continuum-geometry constraint. The composite bridge map's admissibility flows: `Ψ(A_K) → Res_W homogeneity degree (substrate-IS) → composite B = f⊙g → degree-matching-and-non-scalar test against the degree-0 Δ_BCS Level-3 anchor → laboratory image at Pillar V 3He-B BdG`. The substrate is logically prior at the `deg(Res_W) = −2s` layer.

**FORBIDDEN inversion** (container thinking): "the lab anchor or the truncation scheme can override the composite's degree". **INVERT** (substrate thinking): "the substrate's own algebraic-trace dimensional structure dictates what its bridge maps CAN be; degree is upstream of every truncation/regularization scheme; the lab observable at Pillar V is the F-image of the substrate-IS composite, not the empirical test that exists prior to the substrate."

"""


def build_promotion_text(registry_text: str, joint_subblock: str) -> tuple[str, int]:
    """Insert the joint sub-block immediately before the §VII.BB header,
    keeping it inside the §VII.BA section. Pure function; no I/O.

    Returns (full_new_registry_text, insertion_char_offset).
    """
    idx = registry_text.find(NEXT_SECTION_HEADER)  # (local)
    if idx == -1:
        raise RuntimeError(
            f"insertion anchor not found: {NEXT_SECTION_HEADER!r} "
            "(cannot locate §VII.BB header to land before)"
        )
    # Land the sub-block before §VII.BB, leaving a trailing blank line.
    new_text = (  # (local)
        registry_text[:idx] + joint_subblock + "\n" + registry_text[idx:]
    )
    return new_text, idx


# ---------------------------------------------------------------------------
# Step (2) — write_atomic_with_fsync
# ---------------------------------------------------------------------------
def write_atomic_with_fsync(text: str, path: Path) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())


# ---------------------------------------------------------------------------
# Step (3) — re_read + verify_section_matches
# ---------------------------------------------------------------------------
def verify_landing(joint_subblock: str) -> dict:
    """Re-read the registry; verify the joint sub-block landed verbatim INSIDE
    the §VII.BA section, and run the 12-condition cross_pillar_bridge audit on
    the §VII.BA section + the composite-taxonomy detector.

    Returns a dict of the audit booleans (NOT a write — pure verification).
    """
    actual = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)

    # (i) the joint sub-block is present verbatim
    subblock_present = joint_subblock in actual  # (local)

    # (ii) it landed INSIDE the §VII.BA section (between §VII.BA and §VII.BB)
    ba_idx = actual.find("### §VII.BA — Wodzicki-BCS Bridge Theorem")  # (local)
    bb_idx = actual.find(NEXT_SECTION_HEADER)  # (local)
    sub_idx = actual.find(  # (local)
        "#### (h) JOINT TWO-AXIS Composite-Bridge-Map Dimensional-Class"
    )
    inside_ba_section = (  # (local)
        ba_idx != -1 and bb_idx != -1 and sub_idx != -1 and ba_idx < sub_idx < bb_idx
    )

    # (iii) the 12-condition cross_pillar_bridge audit on the §VII.BA section.
    # PRIMARY instrument: direct header-slice (regex-independent) — robust even
    # if BRIDGE_SECTION_REGEX scope drifts. The S93 W1-2 fix widened the regex
    # to cover §VII.B* (it capped at AZ and was BLIND to §VII.BA); the direct
    # slice does not depend on that fix and is the authoritative section text.
    ba_section_text = (  # (local)
        actual[ba_idx:bb_idx] if (ba_idx != -1 and bb_idx != -1) else ""
    )
    ba_section = (  # (local)
        {
            "anchor": "### §VII.BA — Wodzicki-BCS Bridge Theorem STAGE-1-CANDIDATE",
            "letter": "BA",
            "start": ba_idx,
            "end": bb_idx,
            "text": ba_section_text,
        }
        if ba_section_text
        else None
    )
    # CROSS-CONFIRM via the (now-regex-fixed) find_bridge_sections.
    regex_sections = find_bridge_sections(actual)  # (local)
    regex_found_ba = any(s["letter"] == "BA" for s in regex_sections)  # (local)

    if ba_section is None:
        return {
            "subblock_present": subblock_present,
            "inside_ba_section": inside_ba_section,
            "ba_section_found": False,
            "regex_found_ba": regex_found_ba,
            "audit_verdict": "FAIL",
            "diagnostic_fail_count": 1,
            "tier_present_count": 0,
            "anatomy_present_count": 0,
            "oe_form_pass": False,
            "composite_taxonomy_severity": "S2",
            "composite_has_reroute": False,
        }

    sec_audit = audit_section(ba_section)  # (local)
    composite = detect_composite_bridge_map_taxonomy(  # (local)
        ba_section["text"], ba_section["anchor"]
    )

    # diagnostic-FAIL count: the audit_section verdict (PASS iff tier==3 AND
    # anatomy==5 AND oe_form_pass) is the 12-condition gate; the composite
    # taxonomy S2 advisory is INFO-level (NOT a HARD-HALT, K=1 SUGGESTION).
    diagnostic_fail_count = 0 if sec_audit["verdict"] == "PASS" else 1  # (local)

    return {
        "subblock_present": subblock_present,
        "inside_ba_section": inside_ba_section,
        "ba_section_found": True,
        "regex_found_ba": regex_found_ba,
        "audit_verdict": sec_audit["verdict"],
        "diagnostic_fail_count": diagnostic_fail_count,
        "tier_present_count": sec_audit["tier_present_count"],
        "anatomy_present_count": sec_audit["anatomy_present_count"],
        "oe_form_pass": sec_audit["oe_form_check"]["oe_form_pass"],
        "missing_tiers": sec_audit["missing_tiers"],
        "missing_anatomy_elements": sec_audit["missing_anatomy_elements"],
        "missing_oe_form": sec_audit["missing_oe_form"],
        "composite_taxonomy_severity": composite["severity"],
        "composite_has_reroute": composite["has_admissible_reroute"],
        "composite_forbidden_witnesses": composite["forbidden_witnesses"],
    }


# ---------------------------------------------------------------------------
# Step (5) — emit ONCE
# ---------------------------------------------------------------------------
def find_latest_prior_audit_sha() -> str | None:
    """Scan the verdict file for the latest NON-SUPERSEDED canonical line for
    this gate-ID; return its full-64-char audit_sha256 (or None if no prior).

    Used to emit the `supersedes=<old_audit_sha>` tag per
    `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute
    verdict permanence"` rule (5): every corrective verdict line MUST carry the
    supersedes tag at emission time, naming the most-recent-prior canonical line.
    """
    if not VERDICT_TXT.exists():
        return None
    superseded: set[str] = set()  # (local)
    candidates: list[str] = []  # (local)
    for ln in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{GATE_ID}:") and "audit_sha256=" in ln:
            m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)  # (local)
            if m:
                candidates.append(m.group(1))
            sm = re.search(r"supersedes=([a-f0-9]{64})", ln)  # (local)
            if sm:
                superseded.add(sm.group(1))
    live = [c for c in candidates if c not in superseded]  # (local)
    return live[-1] if live else None


def append_verdict(
    verdict: str, value, audit_sha: str, content_sha: str, supersedes: str | None = None
) -> None:
    """Append a single canonical dual-SHA verdict line + companion row.

    Atomic append (single `open("a")`). METHODOLOGY-class artifact-existence
    closure; [VERIFY-THEOREM] trigger — no [SIGN] 3-tuple companion row.
    When `supersedes` is set, the corrective line carries the
    `supersedes=<full-64-char-old-audit-sha>` token in its value= field per
    `gate-verdicts.md` Option A rule (2)/(5).
    """
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    value_field = value if supersedes is None else f"{value}_supersedes={supersedes}"  # (local)
    line = (  # (local)
        f"{GATE_ID}: {verdict} -- value={value_field!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    supersedes_note = (  # (local)
        f"; supersedes={supersedes}" if supersedes else ""
    )
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"METHODOLOGY-class registry-landing artifact-existence; "
        f"[VERIFY-THEOREM] no [SIGN] 3-tuple{supersedes_note}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Main — single-shot AFTER pattern
# ---------------------------------------------------------------------------
def main() -> int:
    print(f"=== {GATE_ID} ===")
    print("Input-pin SHAs (first lines of stdout):")
    pins = log_input_pins(INPUT_FILES)  # (local)

    # idempotent guard: if the joint sub-block already landed VERBATIM, do NOT
    # re-insert (single-shot; re-runs must not duplicate the block). If the
    # header is present but the body differs from the canonical build (a prior
    # run landed a content-corrected-since version), REPLACE the sub-block
    # in-place — a documentation correction to registry PROSE (NOT a verdict-file
    # edit; PROHIBITED_ACTIONS Class 3 governs verdict pass_threshold/pass_band,
    # not registry markdown). Keeps a SINGLE authoritative §VII.BA joint sub-block.
    SUBBLOCK_HEADER = (  # (local)
        "#### (h) JOINT TWO-AXIS Composite-Bridge-Map Dimensional-Class"
    )
    joint_subblock = build_joint_subblock()  # (local) Step (1) pure build
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    header_present = SUBBLOCK_HEADER in registry_text  # (local)
    verbatim_present = joint_subblock in registry_text  # (local)

    if not header_present:
        new_text, ins_off = build_promotion_text(registry_text, joint_subblock)  # (local)
        write_atomic_with_fsync(new_text, REGISTRY_PATH)  # (local) Step (2)
        print(f"  joint sub-block inserted at char offset {ins_off} (before §VII.BB)")
    elif not verbatim_present:
        # stale prior landing: replace the sub-block span (header .. before
        # §VII.BB) with the canonical build.
        sub_start = registry_text.find(SUBBLOCK_HEADER)  # (local)
        bb_start = registry_text.find(NEXT_SECTION_HEADER, sub_start)  # (local)
        if sub_start == -1 or bb_start == -1:
            raise RuntimeError("stale-replace span resolution failed")
        new_text = (  # (local)
            registry_text[:sub_start] + joint_subblock + "\n" + registry_text[bb_start:]
        )
        write_atomic_with_fsync(new_text, REGISTRY_PATH)  # (local)
        print("  stale prior joint sub-block REPLACED in-place with canonical build")
    else:
        print("  joint sub-block already present verbatim (idempotent re-run); no write")

    # Step (3) re_read + verify_section_matches
    v = verify_landing(joint_subblock)  # (local)
    print("Verification:")
    for k in (
        "subblock_present",
        "inside_ba_section",
        "ba_section_found",
        "regex_found_ba",
        "audit_verdict",
        "diagnostic_fail_count",
        "tier_present_count",
        "anatomy_present_count",
        "oe_form_pass",
        "composite_taxonomy_severity",
        "composite_has_reroute",
    ):
        print(f"  {k} = {v.get(k)}")

    # Step (4) determine verdict (single point of decision)
    landed_ok = bool(v["subblock_present"] and v["inside_ba_section"])  # (local)
    audit_ok = (  # (local)
        v["ba_section_found"]
        and v["diagnostic_fail_count"] == 0
        and v["tier_present_count"] == 3
        and v["anatomy_present_count"] == 5
        and bool(v["oe_form_pass"])
    )
    # the composite-taxonomy detector S2 advisory is INFO-level (K=1 SUGGESTION,
    # NOT a HARD-HALT); a present admissible re-route clears it. Record it but
    # do NOT gate PASS on it (per detector docstring: "Does NOT route to
    # plan-freeze HARD-HALT").
    verdict = "PASS" if (landed_ok and audit_ok) else "FAIL"  # (local)

    # Step (5) emit ONCE — dual SHA over the augmented §VII.BA section text +
    # the input-pin map. content_sha256 over the full §VII.BA section as landed.
    actual = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    ba_idx = actual.find("### §VII.BA — Wodzicki-BCS Bridge Theorem")  # (local)
    bb_idx = actual.find(NEXT_SECTION_HEADER)  # (local)
    ba_section_text = actual[ba_idx:bb_idx] if (ba_idx != -1 and bb_idx != -1) else ""  # (local)
    audit_sha, content_sha = compute_dual_sha(ba_section_text, pins)  # (local)

    value = (  # (local)
        f"VII-BA-joint-two-axis-STAGE-1-CANDIDATE_"
        f"diagnostic_fail_count={v['diagnostic_fail_count']}_"
        f"tier={v['tier_present_count']}_anatomy={v['anatomy_present_count']}_"
        f"oe_form_pass={v['oe_form_pass']}_inside_ba={v['inside_ba_section']}_"
        f"composite_reroute={v['composite_has_reroute']}_"
        f"clauses=a_e_connes+binding_mack+c_JOINT"
    )

    supersedes = find_latest_prior_audit_sha()  # (local) Option-A corrective tag
    if supersedes:
        print(f"  prior verdict line detected; emitting corrective line with supersedes={supersedes[:16]}...")
    append_verdict(verdict, value, audit_sha, content_sha, supersedes=supersedes)
    print(f"4-tuple: (value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"audit_sha256={audit_sha}")
    print(f"content_sha256={content_sha}")
    print(f"VERDICT: {verdict}")

    # small audit-record npz (optional artifact per output_artifacts)
    try:
        import numpy as np  # noqa: E402

        np.savez(
            NPZ_PATH,
            gate_id=GATE_ID,
            verdict=verdict,
            diagnostic_fail_count=int(v["diagnostic_fail_count"]),
            tier_present_count=int(v["tier_present_count"]),
            anatomy_present_count=int(v["anatomy_present_count"]),
            oe_form_pass=bool(v["oe_form_pass"]),
            inside_ba_section=bool(v["inside_ba_section"]),
            subblock_present=bool(v["subblock_present"]),
            composite_taxonomy_severity=str(v["composite_taxonomy_severity"]),
            composite_has_reroute=bool(v["composite_has_reroute"]),
            audit_sha256=audit_sha,
            content_sha256=content_sha,
            scheme=SCHEME,
            convention=CONVENTION,
        )
        print(f"npz audit record: {NPZ_PATH}")
    except Exception as exc:  # noqa: BLE001
        print(f"npz save skipped (optional artifact): {exc}")

    # exit 0 regardless of PASS/FAIL — verdict is DATA, not script health,
    # per math-scripts.md §"Exit Codes and Verdict Semantics".
    return 0


if __name__ == "__main__":
    sys.exit(main())
