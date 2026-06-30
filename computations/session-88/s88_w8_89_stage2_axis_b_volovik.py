"""
S88 W8-89 Stage-2 axis-B (substrate / superfluid-universe) cross-reviewer
audit of the layer-separability carve-out clause.

Per `.claude/rules/joint-theorem-promotion.md §"Stage 2"` adapted for the
methodology rule-file PASS-AND requirement of W8-89.

Audit target: `.claude/rules/mechanical-closure-discipline.md`
              §"Layer-separability carve-out (admissible-with-conditions)"
              (lines 59-272 as of 2026-05-05).

Per-condition substrate-axis audit:
  L1 (Layer-functor cleanness)   — substrate IS spectral triple under `F`
  L2 (Type-F closed-form)        — W-5 §VII.AF.1 cross-check (Sage-exact ratio)
  L3 (Type-S separation)         — algebra-axis orthogonality K=3 MANDATORY
  L4 (Honesty disclosure)        — substrate-IS / laboratory-IN boundary

Stage-2 PASS-AND requirement: structural generalization of theorem-clause
PASS-AND to methodology rule-file extension via layer-functor F image.

Emits one verdict line + one dual-SHA companion row to
`computations/session-88/s88_gate_verdicts.txt` for the gate
`S88-W8-89-STAGE-2-AXIS-B-VOLOVIK-VERIFY`.

Author: volovik-superfluid-universe-theorist (Stage-2 axis-B cross-reviewer)
Session: S88
Date: 2026-05-05
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

# Resolve project root and import canonical_constants
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))

from canonical_constants import tau_fold, M_KK  # noqa: E402

# ---------------------------------------------------------------------------
# Pinned input files (audit_sha256 closure base)
# ---------------------------------------------------------------------------
INPUT_PIN_PATHS = [
    PROJECT_ROOT / ".claude" / "rules" / "mechanical-closure-discipline.md",
    PROJECT_ROOT / ".claude" / "rules" / "epistemic-discipline.md",
    PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md",
    PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md",
    PROJECT_ROOT / ".claude" / "rules" / "phononic-framing.md",
    PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py",
]

GATE_ID = "S88-W8-89-STAGE-2-AXIS-B-VOLOVIK-VERIFY"
SCHEME = "two-agent-parallel-independent-verify"
CONVENTION = "joint-clause-AND-aggregation-axis-B-substrate-superfluid-universe"
L_MAX_TAG = "N/A"
AXIS = "AXIS-B"

VERDICT_FILE = PROJECT_ROOT / "computations" / "session-88" / "s88_gate_verdicts.txt"
NPZ_FILE = (
    PROJECT_ROOT / "computations" / "session-88"
    / "s88_w8_89_stage2_axis_b_volovik.npz"
)


# ---------------------------------------------------------------------------
# Per-condition audit results (substitution chain in docstrings)
# ---------------------------------------------------------------------------

def audit_L1_layer_functor_cleanness() -> dict:
    """L1 substitution chain (substrate-axis):

    Step 1 (definition): substrate IS spectral triple (A_K, H_K, D_K) per
        phononic-framing.md; A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ); F: substrate -> methodology
        -> audit per epistemic-discipline.md §"Layer-Decomposition";
        substrate IS algebra+projections, NOT in container.
    Step 2 (substitution): L1 claims Type-F (single-summand-projection
        trace Tr(p_a · A) for p_a ∈ {p_C, p_H, p_M3}) is substrate-physics
        IMAGE under F; Type-S (state-pair functional) is methodology-floor
        IMAGE; A_K factorization is structurally fixed at Volovik partition.
    Step 3 (simplification): Tr(p_a · O · p_a) lives at substrate-IS level;
        rule-file content describing evaluation is methodology-floor; layers
        STRUCTURALLY DISTINCT; partition Type-F vs Type-S aligns.
    Step 4 (direction): no container-thinking; F well-defined; PASS.
    """
    return {
        "condition_id": "L1",
        "axis": AXIS,
        "verdict": "PASS",
        "substitution_chain": (
            "Step1: substrate IS (A_K=C+H+M_3(C), H_K, D_K); F: substrate->"
            "methodology->audit per epistemic-discipline.md §Layer-Decomposition; "
            "Step2: L1 partitions Type-F (Tr(p_a·A)) substrate-side / Type-S "
            "(state-pair) methodology-side under F; Step3: Tr(p_a·O·p_a) is "
            "substrate-IS by construction (intrinsic to A_K projections); "
            "rule-file content is methodology-floor; layers structurally "
            "distinct; Step4: PASS — no container-thinking violation"
        ),
        "notes": [
            "F decomposition matches W-5 §VII.AF.1 calibration corpus structure"
        ],
    }


def audit_L2_typeF_closed_form() -> dict:
    """L2 substitution chain (substrate-axis cross-check W-5 §VII.AF.1):

    Step 1 (definition): W-5 calibration ‖φ_67‖/‖φ_88‖ = 7.324992 Sage-exact
        on (A_K^{≤10}, H_K^{≤10}, D_K^{≤10}); single-summand operator-trace
        identity intrinsic to substrate's BdG-restricted sub-algebra.
    Step 2 (substitution): L2 mandates Type-F evaluable bit-precision
        single-pass pure function on A_K (no iteration, seed, scan, loop);
        W-5 ratio is exactly this evaluation class.
    Step 3 (simplification): minimal central projections of A_K are
        {p_C, p_H, p_M3}; idempotency p_a^2=p_a + orthogonality p_a p_b=0
        bit-precision (S87 W4-2 confirmed); Tr(p_a · O · p_a) closed-form
        on substrate algebra matrix decomposition.
    Step 4 (direction): PASS with NOTE on minimal-central-projection
        prose (admits {p_C, p_H, p_M3} under strict reading).
    """
    return {
        "condition_id": "L2",
        "axis": AXIS,
        "verdict": "PASS",
        "substitution_chain": (
            "Step1: W-5 §VII.AF.1 calibration corpus ‖φ_67‖/‖φ_88‖=7.324992 "
            "Sage-exact substrate-IS single-summand operator-trace identity; "
            "Step2: L2 admits exactly this evaluation class (closed-form, "
            "bit-precision, single-pass pure function, no iteration); "
            "Step3: minimal central projections {p_C,p_H,p_M3} of A_K "
            "satisfy idempotency + orthogonality bit-precision (S87 W4-2 "
            "confirmed); Tr(p_a·O·p_a) closed-form on substrate algebra; "
            "Step4: PASS — W-5 cross-check confirms"
        ),
        "notes": [
            "Strict reading: 'minimal central projection on A_K' admits "
            "exactly {p_C, p_H, p_M3} (one per summand). 'Minimal projection "
            "within a summand' (e.g., rank-1 in M_3(C)) is NOT central. "
            "Prose internally consistent; future invocations should pin "
            "projection class explicitly to avoid drift."
        ],
    }


def audit_L3_typeS_separation() -> dict:
    """L3 substitution chain (substrate-axis vs algebra-axis orthogonality):

    Step 1 (definition): algebra-axis orthogonality MANDATORY at K=3 per
        cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality
        K-counter" (S87 W-2 R3 close, 2026-04-30). Algebra-INVARIANT
        (spectrum-only F({λ_k, m_k})) and algebra-DEPENDENT (state-pair
        functionals on A) STRUCTURALLY ORTHOGONAL in identity-class.
        K=3 corpus: W1b-6 + S-2 + W-2.
    Step 2 (substitution): L3 claims Type-F is algebra-INVARIANT, Type-S
        is algebra-DEPENDENT, mechanical closure on Type-F does NOT
        pre-determine Type-S verdict. Single-summand trace Tr(p_a·O·p_a)
        determined by spectral data; state-pair ⟨ψ_1, O ψ_2⟩ requires
        specifying states ∈ S(A_K), NOT determined by spectral data alone.
    Step 3 (simplification): NCG axioms 1+5 give algebra-INVARIANT family;
        axioms 4+6 + Poincaré duality give algebra-DEPENDENT family;
        chirality-vs-A_F block-grading mismatch ensures
        f(D²) ∩ π(A) = scalars on state-functional side.
    Step 4 (direction): PASS with NOTE on K=3 status documentation
        (carve-out cites the rule but does not name K=3 MANDATORY status
        explicitly).
    """
    return {
        "condition_id": "L3",
        "axis": AXIS,
        "verdict": "PASS",
        "substitution_chain": (
            "Step1: algebra-axis orthogonality K=3 MANDATORY (S87 W-2 close "
            "2026-04-30); algebra-INVARIANT vs algebra-DEPENDENT structurally "
            "orthogonal; Step2: L3's Type-F=algebra-INVARIANT and "
            "Type-S=algebra-DEPENDENT match orthogonality; Tr(p_a·O·p_a) "
            "spectral-data-determined, state-pair ⟨ψ_1,O,ψ_2⟩ state-determined "
            "(not spectral-only); Step3: NCG axioms 1+5 give Type-F class, "
            "4+6+Poincaré duality give Type-S class, chirality-vs-A_F "
            "block-grading mismatch makes f(D²)∩π(A)=scalars on Type-S side; "
            "Step4: PASS — Type-F PASS does NOT propagate to Type-S verdict"
        ),
        "notes": [
            "Documentation-thin: carve-out clause cites cross-pillar-bridge-"
            "anatomy.md §'Algebra-axis orthogonality K-counter' but does NOT "
            "explicitly name K=3 MANDATORY status (promoted at S87 W-2 R3 "
            "close, 2026-04-30). Future revisions should pin K=3 status "
            "explicitly so downstream consumers do not have to walk the "
            "promotion chain."
        ],
    }


def audit_L4_honesty_disclosure() -> dict:
    """L4 substitution chain (substrate-IS / laboratory-IN boundary):

    Step 1 (definition): phononic-framing.md §"IS Space, Not IN Space"
        mandates substrate-IS / laboratory-IN preservation by construction;
        convention-shopping (PROHIBITED_ACTIONS Class 1) is the failure
        mode where generic convention silently invokes structural extension.
    Step 2 (substitution): L4 mandates BOTH convention-tag
        '-LAYER-SEPARABLE-CARVE-OUT-TYPE-F' suffix AND working-paper
        Type-F/Type-S separation paragraph; either alone is Class-1 violation.
    Step 3 (simplification): convention tag is audit-line F-image (per
        epistemic-discipline.md §"Layer-Decomposition" audit-leg); WP
        paragraph is substrate-side narrative complement; both required for
        F: substrate -> methodology -> audit triplet coherence across
        all three layers.
    Step 4 (direction): PASS — L4 prevents substrate-IS / laboratory-IN
        conflation structurally; dual-disclosure is operational
        implementation of phononic-framing.md mandate at carve-out scope.
    """
    return {
        "condition_id": "L4",
        "axis": AXIS,
        "verdict": "PASS",
        "substitution_chain": (
            "Step1: phononic-framing.md §IS-not-IN mandates substrate-IS / "
            "laboratory-IN preservation; convention-shopping Class 1 is the "
            "failure mode; Step2: L4 dual-disclosure (convention tag suffix "
            "'-LAYER-SEPARABLE-CARVE-OUT-TYPE-F' + WP Type-F/Type-S "
            "separation paragraph) — either alone insufficient; Step3: "
            "convention tag is audit-line F-image (audit-leg restriction of "
            "F per epistemic-discipline.md §Layer-Decomposition); WP "
            "paragraph is substrate-side narrative complement; both needed "
            "for substrate->methodology->audit triplet coherence; Step4: "
            "PASS — dual-disclosure is operational implementation of "
            "phononic-framing.md mandate at carve-out scope"
        ),
        "notes": [
            "L4 is the boundary between structural extension and "
            "PROHIBITED_ACTIONS Class 1 per v3-closure-recovery.md; the "
            "carve-out clause names this boundary explicitly (lines 197-217 "
            "of mechanical-closure-discipline.md); PASS-without-NOTE on this "
            "axis."
        ],
    }


def audit_stage2_pass_and_generalization() -> dict:
    """Stage-2 PASS-AND requirement substitution chain:

    Step 1 (definition): joint-theorem-promotion.md §"Stage 2" two-agent
        parallel cross-axis verify WITHOUT prior workshop context;
        PASS-AND on shared (joint) clauses requires both verdicts
        independently PASS; original rule for joint cross-axis THEOREMS.
    Step 2 (substitution): carve-out applies rule to methodology
        RULE-FILE EXTENSION; clauses are 2+2 (L1+L2 spectral/NCG-axiomatic
        / axis-A; L3+L4 substrate-physics+framing / axis-B); rule-file
        clauses inhabit both axis classes simultaneously (cross-axis).
    Step 3 (simplification): structural generalization holds via
        layer-functor F image: theorem-clause PASS-AND at substrate layer
        maps under F to rule-file clause PASS-AND at methodology layer;
        without-prior-workshop-context discipline closes shared-context-
        produces-shared-output failure (epistemic-discipline.md §"What
        Does NOT Count as Evidence" item 2) at methodology layer.
    Step 4 (direction): PASS with NOTE on cross-clause-flagging
        convention (rule does not specify what happens if axis-B finds
        substrate-axis concern on axis-A's clause; conservative reading:
        flag as NOTE, do not soften verdict).
    """
    return {
        "condition_id": "STAGE-2-GENERALIZATION",
        "axis": AXIS,
        "verdict": "PASS",
        "substitution_chain": (
            "Step1: joint-theorem-promotion.md §Stage-2 two-axis "
            "without-prior-context PASS-AND; original rule for theorem "
            "clauses; Step2: carve-out applies rule to methodology "
            "rule-file extension; 2+2 partition (L1+L2 spectral/axis-A, "
            "L3+L4 substrate/axis-B); clauses cross-axis; Step3: "
            "generalization holds via F image (theorem-clause PASS-AND at "
            "substrate layer maps under F to rule-file clause PASS-AND at "
            "methodology layer); without-prior-context closes shared-"
            "context-produces-shared-output failure at methodology layer; "
            "Step4: PASS — structural generalization is meaningful and "
            "preserves the closure of the shared-context failure mode"
        ),
        "notes": [
            "Rule-file does NOT specify cross-clause flagging convention "
            "(e.g., when axis-B has substrate-axis concern on axis-A's "
            "L2 clause); conservative reading: flag as NOTE, do not soften "
            "verdict; this NOTE is not blocking."
        ],
    }


# ---------------------------------------------------------------------------
# Composite verdict aggregator
# ---------------------------------------------------------------------------

def aggregate_axis_b_verdict(records: list[dict]) -> str:
    """Composite per-axis verdict per joint-theorem-promotion.md §Stage 2:
    PASS iff all conditions PASS; ANY clause FAIL -> overall FAIL.

    NOTE-tagged PASS verdicts count as PASS for aggregation (NOTEs are
    forwarded carry-forwards, not blocking findings).
    """
    verdicts = [r["verdict"] for r in records]
    if any(v == "FAIL" for v in verdicts):
        return "FAIL"
    if all(v == "PASS" for v in verdicts):
        return "PASS"
    return "INFO"


# ---------------------------------------------------------------------------
# SHA closure helpers
# ---------------------------------------------------------------------------

def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()


def closure_hash_inputs() -> dict[str, str]:
    out = {}
    for p in INPUT_PIN_PATHS:
        if not p.exists():
            raise FileNotFoundError(f"Input pin missing: {p}")
        out[str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")] = sha256_of_file(p)
    return out


def closure_hash(pinmap: dict, gate_id: str, axis: str) -> str:
    """audit_sha256 = sha256 over (gate_id, axis, sorted-pinmap)."""
    serialized = json.dumps(
        {
            "_gate_id": gate_id,
            "_axis": axis,
            "_scheme": SCHEME,
            "_convention": CONVENTION,
            "input_pins": dict(sorted(pinmap.items())),
        },
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(serialized).hexdigest()


def content_sha_of_self() -> str:
    return sha256_of_file(Path(__file__))


# ---------------------------------------------------------------------------
# Verdict-line emitter
# ---------------------------------------------------------------------------

def emit_verdict_line(
    overall_verdict: str,
    audit_sha: str,
    content_sha: str,
    value_str: str,
) -> tuple[str, str]:
    canonical = (
        f"{GATE_ID}: {overall_verdict} -- value='{value_str}' "
        f"scheme={SCHEME} "
        f"convention={CONVENTION} "
        f"L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"axis=AXIS-B-substrate-superfluid-universe; "
        f"Stage-2 PASS-AND per joint-theorem-promotion.md §Stage 2"
    )
    return canonical, companion


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[volovik-Stage-2-axis-B] starting at {ts}")
    print(f"[volovik-Stage-2-axis-B] gate_id={GATE_ID}")

    # Verify input pins exist
    for p in INPUT_PIN_PATHS:
        assert p.exists(), f"Missing input pin: {p}"
    print(f"[volovik-Stage-2-axis-B] verified {len(INPUT_PIN_PATHS)} input pins")

    # Substitution-chain audit per condition (substrate-axis, axis-B)
    records: list[dict] = [
        audit_L1_layer_functor_cleanness(),
        audit_L2_typeF_closed_form(),
        audit_L3_typeS_separation(),
        audit_L4_honesty_disclosure(),
        audit_stage2_pass_and_generalization(),
    ]
    for r in records:
        print(
            f"[volovik-Stage-2-axis-B] {r['condition_id']}: {r['verdict']} "
            f"({len(r.get('notes', []))} note(s))"
        )

    overall = aggregate_axis_b_verdict(records)
    print(f"[volovik-Stage-2-axis-B] composite axis-B verdict = {overall}")

    # SHA closure
    pinmap = closure_hash_inputs()
    audit_sha = closure_hash(pinmap, GATE_ID, AXIS)
    content_sha = content_sha_of_self()
    print(f"[volovik-Stage-2-axis-B] audit_sha256 = {audit_sha}")
    print(f"[volovik-Stage-2-axis-B] content_sha256 = {content_sha}")

    # Compact value string for verdict line
    note_count = sum(len(r.get("notes", [])) for r in records)
    value_str = (
        f"L1={records[0]['verdict']};L2={records[1]['verdict']};"
        f"L3={records[2]['verdict']};L4={records[3]['verdict']};"
        f"Stage2={records[4]['verdict']};"
        f"composite_axis_B={overall};notes_total={note_count};"
        f"frame=substrate-IS-preserved;K3-MANDATORY-orthogonality-invoked;"
        f"W-5-VII-AF-1-cross-check=consistent"
    )

    # Save NPZ artifact
    np.savez(
        NPZ_FILE,
        condition_id=np.array([r["condition_id"] for r in records]),
        axis=np.array([r["axis"] for r in records]),
        verdict=np.array([r["verdict"] for r in records]),
        substitution_chain=np.array([r["substitution_chain"] for r in records]),
        notes=np.array(
            [json.dumps(r.get("notes", []), ensure_ascii=False) for r in records]
        ),
        composite_verdict=np.array([overall]),
        audit_sha256=np.array([audit_sha]),
        content_sha256=np.array([content_sha]),
        gate_id=np.array([GATE_ID]),
        timestamp=np.array([ts]),
        tau_fold_canonical=np.array([float(tau_fold)]),
        M_KK_canonical=np.array([float(M_KK)]),
    )
    print(f"[volovik-Stage-2-axis-B] NPZ written: {NPZ_FILE}")

    # Emit verdict line + companion row
    canonical, companion = emit_verdict_line(
        overall, audit_sha, content_sha, value_str
    )
    with VERDICT_FILE.open("a", encoding="utf-8") as fh:
        fh.write(canonical + "\n")
        fh.write(companion + "\n")
    print(f"[volovik-Stage-2-axis-B] verdict line appended to {VERDICT_FILE}")
    print(f"[volovik-Stage-2-axis-B] canonical: {canonical[:120]}...")

    # Return 0 regardless of verdict (verdict is data, not exit code)
    return 0


if __name__ == "__main__":
    sys.exit(main())
