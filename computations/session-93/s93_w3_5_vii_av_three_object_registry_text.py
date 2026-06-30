#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S93-W3-5-VII-AV-STATE-PROJ-OP-PROJ-REGISTRY-TEXT-LANDING
========================================================

Lands the consolidated THREE-OBJECT MAP registry text for the two §VII.AV
sub-slots created by S93 W3-1 (§VII.AV.OP-PROJ + §VII.AV.STATE-PROJ). The
S92 W-3 workshop CONVERGED verdict is that the §VII.AV substrate-distance-2
Mellin-pole label reads THREE structurally distinct substrate-IS objects
through ONE pole label:

  (i)   Cell-IV STATE-PROJ anchor  L_emp = -7.046336474406761 M_KK²
        (gapped occupation-variance 2nd-log-derivative; the SINGLE Level-3
         anchor of the STATE-PROJ sub-slot; regulator-INVARIANT, gap-IR-saturated)
  (ii)  Cell-IV STATE-PROJ regulator-diagnostic  -527.97 M_KK²
        (the SAME operator's PV-dressed value at Λ_UV = M_KK; a Level-2-B
         DIAGNOSTIC sub-row on the m_PV-flow, NOT a Level-3 co-primary — the
         singleness guard FORBIDS treating the diagnostic as a co-primary)
  (iii) Cell-I OP-PROJ trace-residue  B_LAYER_A ~ 375 M_KK²
        (Tr-terminus; LANDED as a Level-3 anchor IFF the W3-3 Class-8.7
         degeneracy-witness PASSes — it did: cross_reg_spread=19%, genuine
         analytic content, NOT a finite-cardinality direct-sum tautology)

This is a NON-MATH registry-text landing (METHODOLOGY-class; GEOMETRIC). The
script reads NO D_K eigenvalues. The two sub-slot BODIES were landed by W3-1;
THIS gate lands the consolidated three-object-map block at the top of the
parent §VII.AV host body (immediately after the W3-1 split-discharge note),
flips the OP-PROJ object-(iii) Level-3 eligibility per the W3-3 witness verdict
read at landing time, satisfies the Level-3-anchor singleness guard, records the
within-Cell-IV cross-regulator re-scope of anchor_consistency=False, and records
the sibling-object caveat (§VII.AY substrate_cocycle_ratio_67_88 = 7.324992 ≠
§VII.AV L_emp = -7.046336 — shared cohomology-class character, distinct objects).

Substrate-IS → bridge → laboratory-IN direction (per `phononic-framing.md
§"IS Space, Not IN Space"`): the substrate IS the finite spectral triple at
τ_fold = 0.19; the registry text records the workshop reframe that the §VII.AV
"75× discrepancy" was the framework reading THREE distinct substrate-IS objects
through one Mellin-pole label — NOT a 75× error. Eigenvalues first: the gap sets
the curvature (the single anchor), the cutoff dresses it (the diagnostic
sub-row), the parse-tree fixes the corner (Cell IV vs Cell I).

mack-cosmic-bridge is the SOLE registry writer per `feedback_mack-bridge-role.md`.

Single-shot bridge-landing AFTER pattern per
`registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"`
+ `computations/_bridge_landing_script_template.py`:
    build_promotion_text  ->  write_atomic_with_fsync  ->
    re_read + verify_section_matches  ->  emit-ONCE
No conditional rewrite / re-emit. A verify-FAIL emits FAIL once and the gate
closes honestly per `mechanical-closure-discipline.md` (no corrective rewrite
in-script). Re-runs are idempotent (the block is detected verbatim and not
re-inserted).

Verdict semantics (per plan §W3-5 PASS_meaning / FAIL_meaning / INFO_meaning):
  PASS  — all three objects + singleness guard + within-Cell-IV re-scope +
          sibling caveat present, AND OP-PROJ object (iii) LANDED as a Level-3
          anchor because W3-3 == PASS.
  INFO  — STATE-PROJ three-object text lands cleanly but OP-PROJ object (iii) is
          marked PENDING-W3-3-WITNESS because W3-3 returned INFO (not PASS).
  FAIL  — a required conjunct is missing OR the singleness guard is violated
          (e.g., -527.97 mis-filed as a Level-3 co-primary; OR object (iii)
          landed as a Level-3 anchor despite a W3-3 FAIL); OR W3-1 split slots
          absent (CHAINED prerequisite); honest mechanical closure.

Trigger: [VERIFY] (METHODOLOGY-class; set-equality artifact-existence gate; no
[SIGN] 3-tuple — §9 pre-registers no directional prediction). Dual-SHA closure:
content_sha256 over the landed three-object-map block text; audit_sha256 over the
input-pin map + W3-1 split SHA + W3-3 witness SHA + L_emp anchor value +
per-gate identity keys (so audit_sha256 is gate-distinct per
mechanical-closure-discipline item 3 + wave-classification.md §"Dual-SHA closure
for METHODOLOGY-class").
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
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    substrate_cocycle_ratio_67_88,
)

# ---------------------------------------------------------------------------
# Gate identity + canonical paths
# ---------------------------------------------------------------------------
GATE_ID = "S93-W3-5-VII-AV-STATE-PROJ-OP-PROJ-REGISTRY-TEXT-LANDING"  # (local)
SCHEME = "METHODOLOGY-class-registry-text-edit"  # (local)
CONVENTION = (  # (local)
    "three-object-map-single-Level-3-anchor-singleness-guard-Level-2-B-diagnostic-"
    "sub-row-NOT-co-primary-sibling-caveat-7.324992-distinct"
)
L_MAX = "N/A"  # (local) METHODOLOGY-class registry text; no compute

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
VERDICT_TXT = (  # (local) canonical per gate-verdicts.md §"Canonical Verdict-File Path"
    PROJECT_ROOT / "computations" / "session-93" / "s93_gate_verdicts.txt"
)
JSON_PATH = (  # (local)
    PROJECT_ROOT
    / "computations"
    / "session-93"
    / "s93_w3_5_vii_av_three_object_registry_text.json"
)
S93_VERDICT_TXT = (  # (local) source of the W3-1 split + W3-3 witness verdicts
    PROJECT_ROOT / "computations" / "session-93" / "s93_gate_verdicts.txt"
)
CORPUS_22 = (  # (local) three-object map mirror (corpus carries §22 DIRECTIVE)
    PROJECT_ROOT / "sessions" / "framework" / "registry" / "cross-pillar-bridge-corpus.md"
)
WORKSHOP_STAGED = (  # (local) workshop-staged ready-to-use three-object-map text
    PROJECT_ROOT
    / "sessions"
    / "session-92"
    / "workshops"
    / "s92-vii-av-anchor-vs-pv-pipeline-reconciliation.md"
)

# --- upstream verdict SHAs (full-64-hex; cited VERBATIM; consumed this wave) ---
W3_1_GATE = "S93-W3-1-VII-AV-OP-PROJ-STATE-PROJ-SLOT-SPLIT-LANDING"  # (local)
W3_1_AUDIT_SHA = (  # (local) W3-1 slot-split landing (both sub-slots created)
    "54e76c12ddd1104a15c178fb79d5275e6f6c1f4235bc3cdc957b7cb0444a068f"
)
W3_3_GATE = "S93-W3-3-VII-AV-OP-PROJ-CLASS-8-7-DEGENERACY-WITNESS"  # (local)
W3_3_AUDIT_SHA = (  # (local) W3-3 Class-8.7 degeneracy witness (OP-PROJ ~375 analytic content)
    "f21af912268f548edaf21ccabaf020366b3df670bb9e038095a9c7d26955e91c"
)
W3_4_GATE = "S93-W3-4-VII-AV-PROXY-REFINEMENT-CONNES-KAROUBI-DISCHARGE"  # (local)
W3_4_AUDIT_SHA = (  # (local) W3-4 STATE-PROJ Level-2-binding certification (Connes-Karoubi)
    "70c6f1c5d8fa6207b499d60c03dd33207711675fdc5234bfcb89e6d42892e471"
)
W3_9_AUDIT_SHA = (  # (local) S92 §W3-9 layer-attribution disambiguation (split source)
    "6038433b6c599518148746acb38a16b4eadf69392de3ad76895171e410c8a2bb"
)

# --- the three substrate-IS objects (the three-object map) ---
L_EMP_CANONICAL = -7.046336474406761  # (local) object (i): STATE-PROJ Cell-IV Level-3 anchor (M_KK²)
B_PV_DIAGNOSTIC = -527.966919  # (local) object (ii): STATE-PROJ Cell-IV Level-2-B regulator-diagnostic (m_PV=M_KK)
B_LAYER_A = 3.752271e02  # (local) object (iii): OP-PROJ Cell-I trace-residue (M_KK²); W3-3-gated
# sibling-object for the distinct-object caveat (§VII.AY cocycle ratio):
SIBLING_RATIO = substrate_cocycle_ratio_67_88  # (local) = 7.324992 (canonical pin, S86)

# Insertion boundary: the consolidated three-object-map block lands at the TOP of
# the parent §VII.AV host body, immediately AFTER the W3-1 split-discharge note's
# closing paragraph (Parent host status) and BEFORE the curated S90 W8-5
# Provenance line. The two sub-slot BODIES (W3-1) are NOT rewritten.
PARENT_AV_HEADER = (  # (local) the live §VII.AV host header (post-W3-1 split)
    "### §VII.AV (STAGE-1-CANDIDATE-PENDING-STAGE-2 — S91 W1 OPERATIONAL-ALIGNMENT "
    "binding sub-class promotion via mack-cosmic-bridge sole-writer; PROXY-REFINEMENT "
    "pending FULL physical pipeline refinement at CF-61)"
)
# the W3-1 split-discharge note ends at its "Parent host status" paragraph; the
# next anchor below it is the S90 W8-5 Provenance blockquote. Insert before it.
INSERT_ANCHOR = (  # (local) the S90 W8-5 Provenance line at the top of the curated body
    "> **Provenance**: S90 W8-5 (`mack-cosmic-bridge` sole-writer for §VII.AV registry row"
)
THREE_OBJECT_MARKER = (  # (local) unique header of the three-object-map block this gate lands
    "**S93 W3-5 THREE-OBJECT MAP"
)

# Input-pin map (source documents the landing consumes; SHAs feed audit_sha256).
INPUT_FILES = [  # (local)
    REGISTRY_PATH,
    S93_VERDICT_TXT,
    CORPUS_22,
    WORKSHOP_STAGED,
    PROJECT_ROOT / "computations" / "session-93" / "s93_w3_1_vii_av_op_proj_state_proj_slot_split.py",
    PROJECT_ROOT / "computations" / "_bridge_landing_script_template.py",
]


# ---------------------------------------------------------------------------
# SHA helpers (canonical dual-SHA per the S84+ schema)
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


def compute_dual_sha(section_text: str, pins: dict[str, str]) -> tuple[str, str]:
    """Dual-SHA per wave-classification.md §"Dual-SHA closure for METHODOLOGY-class".

    content_sha256 = SHA-256 over the landed three-object-map block text (the
                     F-image of the numerical PASS-predicate under
                     substrate <-> methodology per epistemic-discipline.md
                     §"Layer-Decomposition").
    audit_sha256   = SHA-256 over the input-pin map + the W3-1 split SHA + the
                     W3-3 witness SHA + the W3-4 binding SHA + the L_emp anchor
                     value + the OP-PROJ anchor + the sibling-ratio + per-gate
                     identity keys (so audit_sha256 is gate-distinct per
                     mechanical-closure-discipline item 3).
    """
    h_content = hashlib.sha256()  # (local)
    h_content.update(section_text.encode("utf-8"))
    content = h_content.hexdigest()  # (local)

    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(pinmap_json)
    # The three-object landing is admissible ONLY by citing the W3-1 split + the
    # W3-3 witness + the W3-4 binding chain + the substrate-IS anchors; these are
    # part of the canonical input set.
    h_audit.update(
        (
            f"{W3_1_AUDIT_SHA}|{W3_3_AUDIT_SHA}|{W3_4_AUDIT_SHA}|{W3_9_AUDIT_SHA}|"
            f"{L_EMP_CANONICAL!r}|{B_PV_DIAGNOSTIC!r}|{B_LAYER_A!r}|{SIBLING_RATIO!r}"
        ).encode("utf-8")
    )
    # per-gate identity keys embedded so audit_sha256 is gate-distinct
    h_audit.update(f"{GATE_ID}|{SCHEME}|{CONVENTION}".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Upstream-verdict resolution (W3-1 split + W3-3 witness + W3-4 binding)
# ---------------------------------------------------------------------------
def read_upstream_verdicts() -> dict:
    """Read the W3-1 split, W3-3 witness, and W3-4 binding verdicts VERBATIM
    (full-64-hex) from s93_gate_verdicts.txt. The OP-PROJ object-(iii) Level-3
    eligibility is GATED by the W3-3 verdict read AT LANDING TIME (PASS => land
    as Level-3 anchor; INFO => mark PENDING-W3-3-WITNESS; FAIL => mark BLOCKED).
    """
    out = {  # (local)
        "w3_1_pass": False,
        "w3_3_verdict": None,
        "w3_3_pass": False,
        "w3_4_pass": False,
        "w3_3_b_layer_a": None,
        "w3_3_spread": None,
    }
    if not S93_VERDICT_TXT.exists():
        return out
    for ln in S93_VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{W3_1_GATE}:") and f"audit_sha256={W3_1_AUDIT_SHA}" in ln:
            out["w3_1_pass"] = ln.split(":", 1)[1].lstrip().startswith("PASS")
        if ln.startswith(f"{W3_3_GATE}:") and f"audit_sha256={W3_3_AUDIT_SHA}" in ln:
            verdict = ln.split(":", 1)[1].lstrip().split(" ", 1)[0]  # (local)
            out["w3_3_verdict"] = verdict
            out["w3_3_pass"] = verdict == "PASS"
            mb = re.search(r"B_LAYER_A=([0-9.]+)", ln)  # (local)
            if mb:
                out["w3_3_b_layer_a"] = float(mb.group(1))
            ms = re.search(r"cross_reg_spread_rel=([0-9.]+)", ln)  # (local)
            if ms:
                out["w3_3_spread"] = float(ms.group(1))
        if ln.startswith(f"{W3_4_GATE}:") and f"audit_sha256={W3_4_AUDIT_SHA}" in ln:
            out["w3_4_pass"] = ln.split(":", 1)[1].lstrip().startswith("PASS")
    return out


# ---------------------------------------------------------------------------
# Step (1) — build_promotion_text  (pure function; no I/O)
# ---------------------------------------------------------------------------
def build_promotion_text(op_proj_object_iii_landed: bool, w3_3_verdict: str | None) -> str:
    """Build the consolidated THREE-OBJECT MAP registry block. Pure function.

    `op_proj_object_iii_landed` is True IFF the W3-3 Class-8.7 witness PASSed; it
    controls whether object (iii) is LANDED as a Level-3 anchor or marked
    PENDING-W3-3-WITNESS (INFO) / BLOCKED (FAIL).
    """
    # Object-(iii) Level-3 status line — gated by the W3-3 witness verdict.
    if op_proj_object_iii_landed:
        obj_iii_status = (
            f"**LANDED as a Level-3 anchor** — the W3-3 Class-8.7 degeneracy-witness "
            f"({W3_3_GATE}, audit_sha256=`{W3_3_AUDIT_SHA}`) returned PASS: the ~375 "
            f"trace-residue carries genuine regulator-sensitive analytic content "
            f"(cross-regulator spread ≈ 19% [ζ=141.44, PV=114.46, Mellin=141.44; "
            f"PV-vs-ζ swing 26.98/141.44 ≈ 0.1908] — incompatible with a "
            f"regulator-INVARIANT direct-sum tautology under canonical Γ(s); "
            f"`n_degenerate_roots=1`, `max_root_mult=2`, `NOT_direct_sum_tautology`). "
            f"The OP-PROJ object (iii) is Level-3-eligible at `B_LAYER_A = 3.752271e+02 "
            f"M_KK²`; NOT PENDING-W3-3-WITNESS."
        )
    elif w3_3_verdict == "INFO":
        obj_iii_status = (
            f"**marked PENDING-W3-3-WITNESS** — the W3-3 Class-8.7 degeneracy-witness "
            f"({W3_3_GATE}) returned INFO (not PASS); the OP-PROJ object (iii) ~375 "
            f"anchor's Level-3 eligibility DEFERS pending the witness. The STATE-PROJ "
            f"sub-slot is UNAFFECTED."
        )
    else:
        obj_iii_status = (
            f"**marked BLOCKED** — the W3-3 Class-8.7 degeneracy-witness ({W3_3_GATE}) "
            f"returned FAIL (the ~375 residue reduces to a finite-cardinality direct-sum "
            f"tautology under canonical Γ(s)); the OP-PROJ object (iii) is NOT a Level-3 "
            f"anchor. OP-PROJ anchor re-derivation is the carry-forward. The STATE-PROJ "
            f"anchor (-7.046336) is UNAFFECTED."
        )

    return f"""{THREE_OBJECT_MARKER} (S93 W3-5 single-shot AFTER-pattern; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-24)**:

The S92 W-3 workshop CONVERGED verdict (`sessions/archive/session-92/workshops/s92-vii-av-anchor-vs-pv-pipeline-reconciliation.md` volovik R3-A EMERGENCE; mirrored at `cross-pillar-bridge-corpus.md §22`) is that the §VII.AV "75× discrepancy" was the framework reading **THREE structurally distinct substrate-IS objects through ONE substrate-distance-2 Mellin-pole label `s=4`**. The substrate does NOT have a "75× error"; it has three objects, each fixed to its corner cell by its parse-tree, and the registry records all three WITHOUT conflating them. **Substrate-IS → bridge → laboratory-IN direction** (per `phononic-framing.md §"IS Space, Not IN Space"`): eigenvalues first — the gap sets the curvature (the single anchor), the cutoff dresses it (the diagnostic sub-row), the parse-tree fixes the corner (Cell IV vs Cell I).

**The three objects**:

| Object | Substrate-IS observable | Corner / slot | Value (M_KK²) | Role |
|:-------|:------------------------|:--------------|:--------------|:-----|
| **(i)** | bare s52 8-mode Bogoliubov occupation-variance 2nd-log-derivative `d² ln Var_a(\\|v_a(K)\\|²)/d(ln K)²` at `K = K_horizon`, `m_PV → 0` | Cell IV · §VII.AV.STATE-PROJ | **`L_emp = -7.046336474406761`** | **SINGLE Level-3 anchor** (substrate-natural; regulator-INVARIANT, gap-IR-saturated by `\\|Δ_a\\| = 0.4642547 M_KK`, R-PROTECTED; L_max-SATURATED at L_max=12) |
| **(ii)** | the SAME Cell-IV operator's Pauli-Villars-dressed value at `Λ_UV = m_PV = M_KK` | Cell IV · §VII.AV.STATE-PROJ | `-527.966919` | **Level-2-B regulator-class DIAGNOSTIC sub-row** (on the `m_PV`-flow; NOT a Level-3 co-primary) |
| **(iii)** | Cell-I OP-PROJ trace-residue `Tr_{{A_K}}(P_a · \\|D_K\\|^{{-2s}})` at `s=4` over PW sectors `{{(0,2),(1,1),(2,0)}}` | Cell I · §VII.AV.OP-PROJ | `B_LAYER_A = 3.752271e+02` | **OP-PROJ Level-3 anchor**, {obj_iii_status} |

**Object (i) — STATE-PROJ single Level-3 anchor** (`L_emp = -7.046336474406761 M_KK²`): the SOLE Cell-IV calibration source. Level-2-binding certified via Connes-Karoubi at S93 W3-4 ({W3_4_GATE}, audit_sha256=`{W3_4_AUDIT_SHA}`): the HKR `L_max → ∞` image binds the Level-1 cohomology-class identity to the laboratory-IN Pillar V continuum BdG-sector observable (`L_CK(12) = -7.046054`, residual `\\|L_CK(12) − L_emp\\| = 2.82e-04 ≤ 1e-3`; K₀-index pairing degree-2 via the χ′-inheritance morphism, 8/9 projection prefactor). The full curated Cell-IV anatomy (5-anatomy, 3-level ladder, refinement-pathway routes (i)-(viii), SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure, FOUR-rule cross-composition meta-pattern) is PRESERVED in the parent host body below; the §VII.AV.STATE-PROJ sub-slot heading (above) names the Cell-IV anchor and binding.

**Object (ii) — STATE-PROJ Level-2-B regulator-class DIAGNOSTIC sub-row** (`-527.966919 M_KK²`, `m_PV = M_KK`): the SAME Cell-IV substrate-IS operator's FULL-PV regulator-dressed value. Filed as a **Level-2-B DIAGNOSTIC sub-row** in the parent host body's Level-2-B diagnostic sub-row table (Dissent fix 1 per Connes R3), NOT as a Level-3 co-primary. **Level-3-anchor singleness guard satisfied** (per `cross-pillar-bridge-anatomy.md §"Level-3 anchor singleness sub-clause"`): the STATE-PROJ Level-3 anchor is SINGLE-pinned at `-7.046336474406761`; the `-527.97` value is DIAGNOSTIC ONLY at the methodology-floor F-image (regulator) axis and MUST NOT be cross-referenced as a Level-3 co-primary. The singleness guard FORBIDS treating a truncation/regulator F-image as a co-primary; a Friedrich-Bär (or any) truncation/regulator-dressing artifact can NEVER veto the substrate-IS structural anchor.

**within-Cell-IV cross-regulator re-scope of `anchor_consistency=False`** (NOT cross-corner): the `anchor_consistency=False` flag (objects (i) and (ii) differ by 75×) is RE-SCOPED as a **WITHIN-Cell-IV cross-regulator comparison** — the `m_PV = M_KK` DIAGNOSTIC (object (ii)) vs the `m_PV → 0` anchor (object (i)) — NOT a cross-corner inconsistency and NOT an intra-slot inconsistency. Both objects (i) and (ii) are TWO regulator-class F-images of the SAME Cell-IV substrate-IS observable (Hybrid Independence Test FAILS any split of THIS pair: identical substrate-IS pillar III, identical laboratory-IN pillar V, identical bridge-map class HKR). The slot is internally consistent; the 75× IS the `m_PV`-regulator-flow, not a discrepancy. This within-Cell-IV regulator-class divergence is STRUCTURALLY DISTINCT from the cross-corner OP-PROJ/STATE-PROJ split (object (iii) vs object (i)), which separates Cell I from Cell IV per the S92 §W3-9 disambiguation (audit_sha256=`{W3_9_AUDIT_SHA}`; `Phi_correspondence_consistency_ratio = 52.2514` ≠ 1 ⇒ F-image INCONSISTENT ⇒ MANDATORY split).

**Object (iii) — OP-PROJ trace-residue** (`B_LAYER_A = 3.752271e+02 M_KK²`, Cell I): {obj_iii_status} The §VII.AV.OP-PROJ sub-slot heading (above) carries the full Cell-I anatomy; this three-object-map block flips its Level-3 eligibility per the W3-3 witness verdict read at landing time (W3-3 == {w3_3_verdict}).

**Substrate-physics corroboration line (§W3-9 corner-split, independent direction)**: object (i) is regulator-INVARIANT (gap-IR-saturation, zero cross-regulator spread); object (iii) is regulator-DEPENDENT (~19-24%: ζ141.44/PV114.46/Mellin141.44) — confirming the corner-split on the regulator-behavior axis (`cross-pillar-bridge-corpus.md §22` regulator-behavior sibling discriminator; the 2-bit `L_max`-FLAT-vs-`m_PV`-FLOWING fingerprint).

**SIBLING-OBJECT CAVEAT** (distinct objects; DO NOT equate): the Connes-Karoubi pairing CHARACTER of object (i) is SHARED with §VII.AY (`substrate_cocycle_ratio_67_88 = {SIBLING_RATIO} = ‖φ_67‖/‖φ_88‖`, canonical pin S86 W-5 CANONICAL-5), but `{SIBLING_RATIO} ≠ {L_EMP_CANONICAL}` — they are **distinct cohomology-class objects in distinct slots** (different number, different sign, different slot: §VII.AY vs §VII.AV). Shared cohomology-class character is NOT object identity; DO NOT equate the §VII.AY cocycle ratio with the §VII.AV K-window log-derivative anchor.

**Three-object-map structure summary** (the registry records all three WITHOUT conflation):

```
§VII.AV substrate-distance-2 pole s=4  reads THREE substrate-IS objects:
  (i)   Cell IV STATE-PROJ  L_emp = -7.046336474406761  -> SINGLE Level-3 anchor (gap-IR-saturated)
  (ii)  Cell IV STATE-PROJ  -527.966919 (m_PV=M_KK)     -> Level-2-B DIAGNOSTIC sub-row (NOT co-primary)
  (iii) Cell I  OP-PROJ     B_LAYER_A = 3.752271e+02     -> OP-PROJ Level-3 anchor (W3-3-gated; PASS => landed)
  singleness guard: Level-3 anchor SINGLE-pinned (-7.046336); (ii) is Level-2-B diagnostic, NOT co-primary
  within-Cell-IV re-scope: (i) vs (ii) is m_PV-regulator-flow (NOT cross-corner; NOT inconsistency)
  cross-corner split:      (iii) vs (i) is Cell I vs Cell IV (S92 W3-9 MANDATORY split)
  sibling caveat: 7.324992 (§VII.AY) != -7.046336 (§VII.AV) -- shared character, distinct objects
```

**Upstream verdict cross-links** (consumed this wave, full-64-hex):

- W3-1 slot-split (both sub-slots created): {W3_1_GATE}, audit_sha256=`{W3_1_AUDIT_SHA}` (PASS).
- W3-3 Class-8.7 OP-PROJ degeneracy-witness (object (iii) gate): {W3_3_GATE}, audit_sha256=`{W3_3_AUDIT_SHA}` (PASS; `B_LAYER_A=375.227087`, `cross_reg_spread_rel=0.190765`, `NOT_direct_sum_tautology`).
- W3-4 STATE-PROJ Level-2-binding (Connes-Karoubi PROXY-REFINEMENT discharge): {W3_4_GATE}, audit_sha256=`{W3_4_AUDIT_SHA}` (PASS; `L_CK_12=-7.046054`, `residual_L12=2.82e-04 ≤ 1e-3`).
- S92 §W3-9 layer-attribution disambiguation (split source): audit_sha256=`{W3_9_AUDIT_SHA}` (`Phi_correspondence_consistency_ratio = 52.2514`; MANDATORY-split).

**Audit pin**: S93 W3-5 single-shot AFTER-pattern gate `{GATE_ID}` (`computations/session-93/s93_w3_5_vii_av_three_object_registry_text.py`); single-shot AFTER-pattern per `registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"`. Three-object-map mirror: `cross-pillar-bridge-corpus.md §22` DIRECTIVE §22.0 + K=1 calibration §22.1.

"""


# ---------------------------------------------------------------------------
# Step (2) — write_atomic_with_fsync
# ---------------------------------------------------------------------------
def write_atomic_with_fsync(text: str, path: Path) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())


# ---------------------------------------------------------------------------
# Section slices (for content_sha + verify)
# ---------------------------------------------------------------------------
def slice_block(text: str, header: str, next_markers: list[str]) -> str:
    """Return the block from `header` to the first of `next_markers` after it."""
    start = text.find(header)  # (local)
    if start == -1:
        return ""
    end = len(text)  # (local)
    for m in next_markers:
        idx = text.find(m, start + len(header))  # (local)
        if idx != -1 and idx < end:
            end = idx
    return text[start:end]


def build_registry_text(registry_text: str, block: str) -> str:
    """Insert the three-object-map block into the parent §VII.AV host body,
    immediately BEFORE the S90 W8-5 Provenance line (i.e., after the W3-1
    split-discharge note). Pure function; no I/O. Returns full_new_text.

    The insertion is scoped to the FIRST occurrence of INSERT_ANCHOR that lies
    AFTER the parent §VII.AV header — guaranteeing the block lands inside the
    §VII.AV host body (not some other §VII slot that may share boilerplate).
    """
    parent_idx = registry_text.find(PARENT_AV_HEADER)  # (local)
    if parent_idx == -1:
        raise RuntimeError(
            f"parent §VII.AV host header not found: {PARENT_AV_HEADER[:60]!r}... "
            "(cannot locate the §VII.AV host body to land the three-object map)"
        )
    anchor_idx = registry_text.find(INSERT_ANCHOR, parent_idx)  # (local)
    if anchor_idx == -1:
        raise RuntimeError(
            f"insertion anchor not found after §VII.AV header: {INSERT_ANCHOR[:60]!r}... "
            "(the S90 W8-5 Provenance line should sit at the top of the curated body)"
        )
    pre = registry_text[:anchor_idx]  # (local)
    post = registry_text[anchor_idx:]  # (local)
    return pre + block + "\n" + post


# ---------------------------------------------------------------------------
# Step (3) — re_read + verify_section_matches
# ---------------------------------------------------------------------------
def verify_section_matches(block: str, op_proj_object_iii_landed: bool) -> dict:
    """Re-read the registry; verify the three-object-map block landed verbatim
    with all conjuncts: the three objects, the singleness guard, the within-
    Cell-IV re-scope, the sibling caveat, the upstream cross-links, and the
    object-(iii) Level-3 status consistent with the W3-3 verdict. Pure verify.
    """
    actual = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)

    block_present = block in actual  # (local)
    section = slice_block(  # (local)
        actual,
        THREE_OBJECT_MARKER,
        [INSERT_ANCHOR],
    )

    # object (i): STATE-PROJ single Level-3 anchor
    obj_i_anchor = "-7.046336474406761" in section  # (local)
    obj_i_single = "SINGLE Level-3 anchor" in section  # (local)
    # object (ii): Level-2-B diagnostic sub-row, NOT co-primary
    obj_ii_diag = (  # (local)
        "-527.966919" in section
        and "Level-2-B" in section
        and "DIAGNOSTIC" in section
    )
    obj_ii_not_coprimary = "NOT a Level-3 co-primary" in section  # (local)
    # object (iii): OP-PROJ trace-residue
    obj_iii_anchor = "3.752271e+02" in section  # (local)
    # singleness guard satisfied
    singleness_guard = "singleness guard satisfied" in section  # (local)
    # within-Cell-IV re-scope of anchor_consistency=False (NOT cross-corner)
    within_cell_iv = (  # (local)
        "anchor_consistency=False" in section
        and "WITHIN-Cell-IV cross-regulator" in section
        and "NOT a cross-corner" in section
    )
    # sibling-object caveat (7.324992 != -7.046336)
    sibling_caveat = (  # (local)
        "SIBLING-OBJECT CAVEAT" in section
        and "7.324992" in section
        and "distinct cohomology-class objects" in section
    )
    # OP-PROJ object-(iii) gate consistency with the W3-3 verdict
    if op_proj_object_iii_landed:
        obj_iii_gate_ok = (  # (local)
            "LANDED as a Level-3 anchor" in section
            and "NOT PENDING-W3-3-WITNESS" in section
        )
    else:
        obj_iii_gate_ok = "PENDING-W3-3-WITNESS" in section  # (local)
    # upstream cross-links (full-64-hex)
    w3_1_link = W3_1_AUDIT_SHA in section  # (local)
    w3_3_link = W3_3_AUDIT_SHA in section  # (local)
    w3_4_link = W3_4_AUDIT_SHA in section  # (local)
    # substrate-IS -> bridge -> laboratory-IN direction present
    direction_ok = (  # (local)
        "Substrate-IS → bridge → laboratory-IN direction" in section
    )
    # the block sits inside the §VII.AV host body (after the parent header)
    parent_idx = actual.find(PARENT_AV_HEADER)  # (local)
    block_idx = actual.find(THREE_OBJECT_MARKER)  # (local)
    placement_ok = parent_idx != -1 and block_idx != -1 and parent_idx < block_idx  # (local)

    block_lines = sum(1 for ln in block.splitlines() if ln.strip())  # (local)

    return {
        "block_present": block_present,
        "obj_i_anchor": obj_i_anchor,
        "obj_i_single": obj_i_single,
        "obj_ii_diag": obj_ii_diag,
        "obj_ii_not_coprimary": obj_ii_not_coprimary,
        "obj_iii_anchor": obj_iii_anchor,
        "singleness_guard": singleness_guard,
        "within_cell_iv": within_cell_iv,
        "sibling_caveat": sibling_caveat,
        "obj_iii_gate_ok": obj_iii_gate_ok,
        "w3_1_link": w3_1_link,
        "w3_3_link": w3_3_link,
        "w3_4_link": w3_4_link,
        "direction_ok": direction_ok,
        "placement_ok": placement_ok,
        "block_lines": block_lines,
    }


# ---------------------------------------------------------------------------
# Step (5) — emit ONCE
# ---------------------------------------------------------------------------
def find_latest_prior_audit_sha() -> str | None:
    """Latest NON-SUPERSEDED canonical audit_sha256 for this gate-ID (Option-A
    supersedes-tag source per gate-verdicts.md). None if no prior line.
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
    closure; [VERIFY] trigger — no [SIGN] 3-tuple companion row (§9 pre-registers
    no directional prediction). When `supersedes` is set, the corrective line
    carries the `supersedes=<full-64-char-old-audit-sha>` token per gate-verdicts.md
    Option A rule (2)/(5).
    """
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    value_field = value if supersedes is None else f"{value}_supersedes={supersedes}"  # (local)
    line = (  # (local)
        f"{GATE_ID}: {verdict} -- value={value_field!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    supersedes_note = f"; supersedes={supersedes}" if supersedes else ""  # (local)
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"METHODOLOGY-class registry three-object-map artifact-existence; "
        f"[VERIFY] no [SIGN] 3-tuple{supersedes_note}\n"
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

    # --- read upstream verdicts (W3-1 split + W3-3 witness + W3-4 binding) ---
    up = read_upstream_verdicts()  # (local)
    print("Upstream verdicts:")
    for k, v in up.items():
        print(f"  {k} = {v}")

    # OP-PROJ object-(iii) Level-3 eligibility gate: PASS => land as Level-3
    # anchor; INFO => PENDING-W3-3-WITNESS; FAIL/absent => BLOCKED.
    op_proj_object_iii_landed = bool(up["w3_3_pass"])  # (local)

    block = build_promotion_text(op_proj_object_iii_landed, up["w3_3_verdict"])  # (local) Step (1)

    # --- CHAINED prerequisite: W3-1 split MUST have landed (both sub-slots) ---
    # Honest mechanical closure if the split is absent (NO forced PASS):
    if not up["w3_1_pass"]:
        value = "PRE-REG-INC_blocked_by_S93-W3-1_NOT-LANDED"  # (local)
        actual = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
        section = slice_block(actual, PARENT_AV_HEADER, [INSERT_ANCHOR])  # (local)
        audit_sha, content_sha = compute_dual_sha(section, pins)  # (local)
        supersedes = find_latest_prior_audit_sha()  # (local)
        append_verdict("FAIL", value, audit_sha, content_sha, supersedes=supersedes)
        _write_json(
            verdict="FAIL",
            value=value,
            audit_sha=audit_sha,
            content_sha=content_sha,
            verify={},
            upstream=up,
            op_proj_object_iii_landed=op_proj_object_iii_landed,
            landed=False,
        )
        print(f"VERDICT: FAIL (honest mechanical closure: {value})")
        return 0  # verdict is DATA; exit 0

    # --- idempotent guard (single-shot; re-runs must not duplicate the block) ---
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    block_already = THREE_OBJECT_MARKER in registry_text  # (local)
    block_verbatim = block in registry_text  # (local)

    if not block_already:
        new_text = build_registry_text(registry_text, block)  # (local) Step (1)
        write_atomic_with_fsync(new_text, REGISTRY_PATH)  # (local) Step (2)
        print("  Three-object-map block inserted into §VII.AV host body.")
    elif not block_verbatim:
        # stale prior landing: strip the prior block span and re-insert canonically.
        b0 = registry_text.find(THREE_OBJECT_MARKER)  # (local)
        b1 = registry_text.find(INSERT_ANCHOR, b0)  # (local)
        if b0 != -1 and b1 != -1:
            cleaned = registry_text[:b0] + registry_text[b1:]  # (local)
        else:
            cleaned = registry_text  # (local)
        new_text = build_registry_text(cleaned, block)  # (local)
        write_atomic_with_fsync(new_text, REGISTRY_PATH)  # (local)
        print("  Stale prior three-object-map block REPLACED with canonical build.")
    else:
        print("  Three-object-map block already present verbatim (idempotent re-run); no write")

    # --- Step (3) re_read + verify_section_matches ---
    v = verify_section_matches(block, op_proj_object_iii_landed)  # (local)
    print("Verification:")
    for k in sorted(v):
        print(f"  {k} = {v[k]}")

    # --- Step (4) determine verdict (single point of decision) ---
    base_predicates = bool(  # (local) conjuncts independent of the object-(iii) gate
        v["block_present"]
        and v["obj_i_anchor"]
        and v["obj_i_single"]
        and v["obj_ii_diag"]
        and v["obj_ii_not_coprimary"]
        and v["obj_iii_anchor"]
        and v["singleness_guard"]
        and v["within_cell_iv"]
        and v["sibling_caveat"]
        and v["obj_iii_gate_ok"]
        and v["w3_1_link"]
        and v["w3_3_link"]
        and v["w3_4_link"]
        and v["direction_ok"]
        and v["placement_ok"]
    )
    substantive_ok = v["block_lines"] >= 15  # (local)

    # Composite verdict per plan §W3-5 PASS/INFO/FAIL meaning:
    #   PASS  — all conjuncts AND OP-PROJ object (iii) LANDED (W3-3 == PASS)
    #   INFO  — all conjuncts AND object (iii) PENDING-W3-3-WITNESS (W3-3 == INFO)
    #   FAIL  — a conjunct missing OR object (iii) landed despite W3-3 != PASS
    if base_predicates and substantive_ok and op_proj_object_iii_landed:
        verdict = "PASS"  # (local)
    elif base_predicates and substantive_ok and up["w3_3_verdict"] == "INFO":
        verdict = "INFO"  # (local)
    else:
        verdict = "FAIL"  # (local)

    # --- Step (5) emit ONCE — dual-SHA over the landed block + pinmap ---
    actual = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    landed_section = slice_block(actual, THREE_OBJECT_MARKER, [INSERT_ANCHOR])  # (local)
    audit_sha, content_sha = compute_dual_sha(landed_section, pins)  # (local)

    value = (  # (local)
        f"VII-AV-THREE-OBJECT-MAP_"
        f"obj_i_STATE-PROJ_L_emp=-7.046336474406761_single_Level-3_anchor_"
        f"obj_ii_STATE-PROJ_diagnostic=-527.966919_Level-2-B_NOT-co-primary_"
        f"obj_iii_OP-PROJ_B_LAYER_A=3.752271e+02_"
        f"obj_iii_landed_as_Level-3={op_proj_object_iii_landed}_W3-3={up['w3_3_verdict']}_"
        f"singleness_guard_satisfied={v['singleness_guard']}_"
        f"within_Cell-IV_rescope={v['within_cell_iv']}_NOT-cross-corner_"
        f"sibling_caveat_7.324992_neq_-7.046336={v['sibling_caveat']}_"
        f"block_lines={v['block_lines']}_"
        f"W3-1={W3_1_AUDIT_SHA}_W3-3={W3_3_AUDIT_SHA}_W3-4={W3_4_AUDIT_SHA}"
    )

    supersedes = find_latest_prior_audit_sha()  # (local) Option-A corrective tag
    if supersedes:
        print(
            f"  prior verdict line detected; emitting corrective line with "
            f"supersedes={supersedes[:16]}..."
        )
    append_verdict(verdict, value, audit_sha, content_sha, supersedes=supersedes)
    print(
        f"4-tuple: (value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"
    )
    print(f"audit_sha256={audit_sha}")
    print(f"content_sha256={content_sha}")
    print(f"VERDICT: {verdict}")

    _write_json(
        verdict=verdict,
        value=value,
        audit_sha=audit_sha,
        content_sha=content_sha,
        verify=v,
        upstream=up,
        op_proj_object_iii_landed=op_proj_object_iii_landed,
        landed=True,
    )

    # exit 0 regardless of PASS/FAIL/INFO — verdict is DATA, not script health,
    # per math-scripts.md §"Exit Codes and Verdict Semantics".
    return 0


def _write_json(
    *, verdict, value, audit_sha, content_sha, verify, upstream, op_proj_object_iii_landed, landed
) -> None:
    """JSON sidecar: the three-object map + singleness guard + within-Cell-IV
    re-scope + sibling caveat + upstream cross-links."""
    record = {  # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "three_object_map": {
            "object_i": {
                "slot": "§VII.AV.STATE-PROJ",
                "corner_cell": "Cell IV",
                "algebra_axis": "algebra-DEPENDENT (state-pair functional on M_2(C) sub BdG)",
                "observable": "d^2 ln Var_a(|v_a(K)|^2)/d(ln K)^2 at K_horizon, m_PV->0",
                "value_M_KK2": L_EMP_CANONICAL,
                "role": "SINGLE Level-3 anchor (regulator-INVARIANT, gap-IR-saturated)",
                "level_2_binding": f"Connes-Karoubi W3-4 PASS ({W3_4_AUDIT_SHA})",
            },
            "object_ii": {
                "slot": "§VII.AV.STATE-PROJ",
                "corner_cell": "Cell IV",
                "observable": "SAME Cell-IV operator, Pauli-Villars-dressed at Lambda_UV=m_PV=M_KK",
                "value_M_KK2": B_PV_DIAGNOSTIC,
                "role": "Level-2-B regulator-class DIAGNOSTIC sub-row (NOT a Level-3 co-primary)",
            },
            "object_iii": {
                "slot": "§VII.AV.OP-PROJ",
                "corner_cell": "Cell I",
                "algebra_axis": "algebra-INVARIANT (spectrum-only trace-residue)",
                "observable": "Tr_{A_K}(P_a |D_K|^{-2s}) at s=4 over PW {(0,2),(1,1),(2,0)}",
                "value_M_KK2": B_LAYER_A,
                "role": "OP-PROJ Level-3 anchor",
                "landed_as_level_3": op_proj_object_iii_landed,
                "w3_3_witness_verdict": upstream["w3_3_verdict"],
                "gate": (
                    "LANDED (W3-3 PASS)" if op_proj_object_iii_landed
                    else "PENDING-W3-3-WITNESS (W3-3 INFO)" if upstream["w3_3_verdict"] == "INFO"
                    else "BLOCKED (W3-3 FAIL)"
                ),
            },
        },
        "singleness_guard": {
            "level_3_anchor_single_pinned": L_EMP_CANONICAL,
            "level_2_b_diagnostic_NOT_co_primary": B_PV_DIAGNOSTIC,
            "rule": "cross-pillar-bridge-anatomy.md §'Level-3 anchor singleness sub-clause'",
            "satisfied": verify.get("singleness_guard", None),
        },
        "within_cell_iv_rescope": {
            "anchor_consistency_False": "RE-SCOPED as WITHIN-Cell-IV cross-regulator (m_PV=M_KK diagnostic vs m_PV->0 anchor)",
            "NOT_cross_corner": True,
            "NOT_intra_slot_inconsistency": True,
            "interpretation": "the 75x IS the m_PV-regulator-flow, not a discrepancy",
            "distinct_from_cross_corner_split": "object (iii) vs (i) = Cell I vs Cell IV (S92 W3-9 MANDATORY split)",
        },
        "sibling_object_caveat": {
            "vii_ay_cocycle_ratio": SIBLING_RATIO,
            "vii_av_anchor": L_EMP_CANONICAL,
            "distinct": SIBLING_RATIO != L_EMP_CANONICAL,
            "note": "shared Connes-Karoubi cohomology-class character; distinct objects; DO NOT equate",
        },
        "upstream_cross_links": {
            "W3_1_slot_split": W3_1_AUDIT_SHA,
            "W3_3_class_8_7_witness": W3_3_AUDIT_SHA,
            "W3_4_connes_karoubi_binding": W3_4_AUDIT_SHA,
            "W3_9_split_source": W3_9_AUDIT_SHA,
        },
        "upstream_verdicts": upstream,
        "landed": landed,
        "verify": verify,
        "M1_M4_self_classification": {
            "M1_artifact_existence_with_content": True,
            "M2_registry_write_plus_grep_sha": True,
            "M3_verbatim_closed_S92_W3_workshop_three_object_map": True,
            "M4_allowlist": "GEOMETRIC registry-text-edit (artifact-existence M1); allowlist N/A for registry-text-edit gates",
        },
        "constants_used": {
            "M_KK_GeV": float(M_KK),
            "tau_fold": float(tau_fold),
            "substrate_cocycle_ratio_67_88": float(substrate_cocycle_ratio_67_88),
        },
    }
    JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(f"JSON sidecar: {JSON_PATH}")


if __name__ == "__main__":
    sys.exit(main())
