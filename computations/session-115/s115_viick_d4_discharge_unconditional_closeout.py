#!/usr/bin/env python3
"""
S115 W2-1 S115-VIICK-D4-DISCHARGE-UNCONDITIONAL — Stage-2 blind D4 verify PASS-AND closeout (INFO landing)
========================================================================================================

Gate: S115-VIICK-D4-DISCHARGE-UNCONDITIONAL ([VERIFY-THEOREM]; carries a [CHAIN]
      sub-trigger for the t(O)=±1≠0 selection-rule direction claim, pre-flighted
      in the plan substitution_chain — NOT emitted as a 3-tuple SIGN row).

Pre-registered operator (plan §W2-1 item (1), set-membership PASS-AND):
    composite = PASS  iff ALL of {A-leg, B-leg, JOINT-A, JOINT-B} are PASS
    any FAIL                 ⇒ composite FAIL
    any INFO with no FAIL    ⇒ composite INFO   (Stage-2-INFO-deferred, NO UNCONDITIONAL flip)

On-disk reviewer verdicts (read from the two clause-verdict deliverables):
    {A-leg = INFO, B-leg = PASS, JOINT-A = PASS, JOINT-B = PASS}
  ⇒ one INFO, zero FAIL ⇒ composite = INFO  (the PRE-REGISTERED outcome).

CONSEQUENCE (pre-registered INFO disposition, plan §W2-1 INFO_meaning):
  - NO UNCONDITIONAL flip. §VII.CK STAYS at the W1-1-determined state
    STAGE-3-PERMANENT (D4-open scope qualifier RETAINED). The D4 mechanism
    disagreement (Axis-A Sage-derived t(R_X)=0 for ALL su(3)_R generators ⇒
    commutant/leg-membership mechanism, corroborated by connes-r2.md PROVEN;
    Axis-B affirmed the contested t(O)=±1 center-character selection rule) is a
    GENUINE math/physics tension. Per Investigating-Workshops.md Q1 + the
    capstone-hygiene rule, it is FORWARD-ROUTED with a STATUS-unreconciled
    pointer — NOT rewritten by this closeout, NOT silently down-tagged.
  - This closeout therefore does NOT apply Axis-A's corrigendum, does NOT flip
    §VII.CK to UNCONDITIONAL, does NOT touch the D1–D3 STAGE-3-PERMANENT status.
    It ADDS a STATUS pointer to the §VII.CK D4-disposition annotation and the
    Four-door D4 row, naming the contest and routing it to
    CF-S116-VIICK-D4-MECHANISM-CORRIGENDUM. The existing t(O)=±1 text is RETAINED
    (audit-trail preservation).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-115/s115_viick_d4_discharge_unconditional_closeout.py (this script; BOTH SHAs)
  - sessions/permanent-results-registry.md (the registered §VII.CK entry text; feeds audit_sha256)
  - sessions/session-115/session-115-w2-reviewerA-VIICK-D4-clause-verdict.md (Axis-A; feeds audit_sha256)
  - sessions/session-115/session-115-w2-reviewerB-VIICK-D4-clause-verdict.md (Axis-B; feeds audit_sha256)
  - computations/session-114/s114_yuk_rightreg_connection.npz (W3-1 residual readback; feeds audit_sha256)
  - computations/_shared/canonical_constants.py (feeds audit_sha256 only)

Output 4-tuple:
  (value=<composite=INFO + 4 per-axis verdicts + t(R_X)=0 contest + NO-flip + CF-S116>,
   scheme=STAGE-2-JOINT-VERIFY, convention=PASS-AND-LOGICAL-AND-NOT-OR, L_max=N/A)

Classification: GEOMETRIC (which operators the fabric's own differential calculus
Ω¹_{D_K}(A_K) can reach; a statement about the spectral triple, not its excitations).

METHODOLOGY
-----------
Verdict-aggregation + forward-route gate. (1) Parse the two reviewer clause-verdict
deliverables for their machine-readable {A_leg_verdict, B_leg_verdict, JOINT_verdict}
blocks. (2) Apply the pre-registered PASS-AND set-membership operator over the
4-tuple {A-leg, B-leg, JOINT-A, JOINT-B} → composite (INFO here). (3) Read back the
W3-1 residual==1.000000 EXACT cross-check from the s114 npz (npz-ground-truth runtime
canonical-path rescue if the path drifts). (4) Confirm the reviewer-exclusion
∅-intersection ({spectral-geometer, volovik} ∩ excluded_authors = ∅; disjoint from
W1-1 {lizzi, kitaev}). (5) On the INFO branch, ADD a STATUS pointer to the §VII.CK
D4-disposition annotation + Four-door D4 row (idempotent single-pass read-modify-write
on a UNIQUE anchor substring; registry-write-hygiene per epistemic-discipline.md), naming
the mechanism contest and routing it to CF-S116-VIICK-D4-MECHANISM-CORRIGENDUM; the
§VII.CK stage tag is UNCHANGED. Record the runtime registry SHA pre/post the pointer add.
No linear algebra (the substrate physics lives in the reviewer deliverables, re-derived
there from first principles via Sage; this gate aggregates + forward-routes, it does NOT
re-derive). The verdict is emitted via print_verdict_payload → emit_verdict (race-safe).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema); per-gate identity keys
  {_gate_id, _scheme, _convention} embedded in the pinmap so audit_sha256 ≠ W1-1's
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via the emit_verdict knowledge-MCP tool (race-safe, syntax-forced);
  the script PRINTS the payload, the dispatching agent calls emit_verdict — the script
  does NOT write s115_gate_verdicts.txt directly.
- The STATUS-pointer add is an ANNOTATION (append-only, idempotent), NOT a mechanism
  rewrite and NOT a stage-tag flip. The contested t(O)=±1 text is RETAINED.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — _shared on sys.path (sibling idiom: s114_yuk_rightreg_connection.py:73-77)
# so the MANDATORY canonical_constants import below resolves when run from session-115/.
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "_shared"))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S115"                                                   # (local)
GATE_ID = "S115-VIICK-D4-DISCHARGE-UNCONDITIONAL"                  # (local)
SCHEME = "STAGE-2-JOINT-VERIFY"                                    # (local)
CONVENTION = "PASS-AND-LOGICAL-AND-NOT-OR"                         # (local)
L_MAX = "N/A"                                                      # (local) L_max-INVARIANT: t(O) obstruction EXACT ∀ L_max

# Per-gate identity keys (embedded in pinmap so audit_sha256 is distinct from W1-1's)
GATE_IDENTITY = {                                                  # (local)
    "_gate_id": GATE_ID,
    "_scheme": SCHEME,
    "_convention": CONVENTION,
    "_wp_id": "S115-W2-1",
    "_clause": "D4-external-JOINT",
}

# Reviewer-exclusion guard (plan §W2-1 machinery_pin_map.excluded_authors;
# the ∅-intersection is encoded HERE because the audit author-parser is unreliable
# on §VII.CK per the plan note).
REVIEWERS = {"spectral-geometer": "A", "volovik-superfluid-universe-theorist": "B"}  # (local)
EXCLUDED_AUTHORS = {                                               # (local)
    "connes-ncg-theorist", "paasch-mass-quantization-analyst",     # YUKSHAPE §VII.CK Stage-0 authors
    "van-den-dungen-bridge-theorist", "baptista-spacetime-analyst",  # S114 W-2 D4-disposition workshop authors
    "kaluza-klein-theorist",                                       # §VII.BL Stage-0 co-author + landing-writer/reviewer-of-record (downstream-inheritance)
}
W1_1_REVIEWERS = {"lizzi-spectral-functional-theorist", "kitaev-quantum-chaos-theorist"}  # (local) disjoint-pair end-state

# Input files
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"          # (local)
REVIEWER_A_PATH = (PROJECT_ROOT / "sessions" / "session-115"
                   / "session-115-w2-reviewerA-VIICK-D4-clause-verdict.md")          # (local)
REVIEWER_B_PATH = (PROJECT_ROOT / "sessions" / "session-115"
                   / "session-115-w2-reviewerB-VIICK-D4-clause-verdict.md")          # (local)
W3_1_NPZ_PRIMARY = (PROJECT_ROOT / "computations" / "session-114"
                    / "s114_yuk_rightreg_connection.npz")                            # (local)
W3_1_NPZ_AUDIT_PIN = "e392b832483e8f75c6cbd87086c3a10bfb19f3d242ba9f873de3a9434997d49b"  # (local) plan-pinned W3-1 verdict audit_sha256

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s115_viick_d4_discharge_unconditional.npz"

INPUT_FILES = [
    Path(__file__).resolve(),
    REGISTRY_PATH,
    REVIEWER_A_PATH,
    REVIEWER_B_PATH,
    W3_1_NPZ_PRIMARY,
    SHARED_DIR / "canonical_constants.py",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = p.name
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(pins: dict[str, str]) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
                     where pinmap_json includes the per-gate identity keys so the
                     audit_sha256 is distinct from W1-1's (different clause/reviewers).
    content_sha256 = sha256( bytes(script) ) — script edits only.
    """
    script_path = Path(__file__).resolve()           # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    try:
        script_bytes = script_path.read_bytes()       # (local)
    except OSError:
        script_bytes = b""                            # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""                         # (local)

    pinmap = dict(pins)                               # (local)
    pinmap.update(GATE_IDENTITY)                      # per-gate identity keys ⇒ audit_sha256 ≠ W1-1's
    pinmap_json = json.dumps(
        dict(sorted(pinmap.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")                                 # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                       # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                   # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Reviewer clause-verdict parsing + PASS-AND operator
# ---------------------------------------------------------------------------

def _parse_machine_verdict(text: str, key: str) -> str:
    """Extract a `key: VALUE` machine-readable clause-verdict field (first match).

    The deliverables carry a ```yaml machine-readable block with lines like
    `A_leg_verdict: INFO`, `JOINT_verdict: PASS`. We match the bare token after
    the colon (PASS|FAIL|INFO), tolerant of trailing comment text.
    """
    pat = re.compile(rf"(?m)^\s*{re.escape(key)}\s*:\s*(PASS|FAIL|INFO)\b")  # (local)
    m = pat.search(text)                                                     # (local)
    if not m:
        raise ValueError(f"could not parse '{key}' from reviewer deliverable")
    return m.group(1)


def pass_and(verdicts: dict[str, str]) -> str:
    """Pre-registered set-membership PASS-AND collapse (plan §W2-1 operator).

    composite = PASS iff ALL ∈ {PASS}; any FAIL ⇒ FAIL; any INFO (no FAIL) ⇒ INFO.
    """
    vals = list(verdicts.values())            # (local)
    if any(v == "FAIL" for v in vals):
        return "FAIL"
    if any(v == "INFO" for v in vals):
        return "INFO"
    if all(v == "PASS" for v in vals):
        return "PASS"
    # defensive: an unrecognized token is a structural error, not a silent PASS
    raise ValueError(f"unrecognized verdict tokens in PASS-AND: {vals}")


# ---------------------------------------------------------------------------
# Section 6 — W3-1 residual readback (npz-ground-truth canonical-path rescue)
# ---------------------------------------------------------------------------

def read_w3_1_residual() -> dict:
    """Read the W3-1 residual==1.000000 EXACT cross-check from the s114 npz.

    Primary path is the plan-pinned npz; if it is missing/unreadable, fall back to
    locating an npz whose stored audit_sha256 matches the plan-pinned W3-1 verdict
    audit_sha256 (gate-verdicts.md runtime canonical-path rescue). Returns the
    residual min/max + the per-Cartan residual map + a path-drift flag.
    """
    path = W3_1_NPZ_PRIMARY                                          # (local)
    drift = False                                                    # (local)
    if not path.exists():
        # npz-ground-truth rescue: scan session-114 for an npz with the pinned audit_sha256
        drift = True
        cand_dir = PROJECT_ROOT / "computations" / "session-114"    # (local)
        path = None
        for c in sorted(cand_dir.glob("*.npz")):
            try:
                dd = np.load(c, allow_pickle=True)                  # (local)
                if "audit_sha256" in dd.files and str(dd["audit_sha256"].item()) == W3_1_NPZ_AUDIT_PIN:
                    path = c
                    break
            except Exception:
                continue
        if path is None:
            raise FileNotFoundError(
                "W3-1 residual npz not found by path OR by audit_sha256 rescue")

    d = np.load(path, allow_pickle=True)                            # (local)
    res_min = float(d["residual_iv_min"].item())                   # (local)
    res_max = float(d["residual_iv_max"].item())                   # (local)
    keys = list(d["iv_residuals_keys"])                            # (local)
    vals = [float(x) for x in d["iv_residuals_vals"]]              # (local)
    stored_audit = str(d["audit_sha256"].item()) if "audit_sha256" in d.files else ""  # (local)
    return {
        "path": str(path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "residual_iv_min": res_min,
        "residual_iv_max": res_max,
        "iv_residuals": dict(zip([str(k) for k in keys], vals)),
        "stored_audit_sha256": stored_audit,
        "audit_pin_matches": stored_audit == W3_1_NPZ_AUDIT_PIN,
        "path_drift": drift,
        # residual==1.000000 EXACT readback ⇒ True (abs_tol 1e-12 on the float64 readback)
        "residual_is_unit_exact": (abs(res_min - 1.0) < 1e-12 and abs(res_max - 1.0) < 1e-12),
    }


# ---------------------------------------------------------------------------
# Section 7 — STATUS-pointer add (INFO branch; idempotent single-pass RMW)
# ---------------------------------------------------------------------------
# The STATUS pointer is APPENDED to two UNIQUE anchor substrings (the exact
# tail-sentence of the Four-door D4 row and of the D4-disposition annotation).
# This is an ANNOTATION (append-only, idempotent), NOT a mechanism rewrite and
# NOT a stage-tag flip. The contested t(O)=±1 text is RETAINED. Idempotency:
# if the STATUS pointer is already present, the add is a NO-OP.

STATUS_POINTER_MARKER = "STATUS: Stage-2-INFO-deferred (S115 W2-1)"  # (local) idempotency sentinel

# The two unique anchors (exact verbatim tail substrings present in the registry).
# Anchor 1 — Four-door D4 row tail (line ~22439).
ANCHOR_D4_ROW = (
    "until then the scope qualifier `class = {A_K-built ∪ Casimir-graded "
    "∪ γ₉-traced}` (D1–D3) is UNCHANGED. |"
)
# Anchor 2 — D4-disposition annotation tail (line ~22460).
ANCHOR_D4_ANNOT = (
    "the closed-INTERNAL wall scope qualifier `class = {A_K-built ∪ Casimir-graded "
    "∪ γ₉-traced}` is UNCHANGED, and this entry's STAGE-1-CANDIDATE tag is UNCHANGED."
)

# The STATUS pointer prose (added immediately AFTER each anchor; out of the frozen
# blockquote; names the contest, states the conclusion is UNAFFECTED, routes to CF-S116).
STATUS_POINTER_TEXT = (
    " **" + STATUS_POINTER_MARKER + " — D4 mechanism CONTESTED.** The stated "
    "`t(O)=±1≠0` center-character selection-rule mechanism is CONTESTED by the "
    "Stage-2 blind cross-axis verify (`S115-VIICK-D4-DISCHARGE-UNCONDITIONAL`, composite "
    "INFO): Axis-A (spectral-geometer) Sage-derived `t(R_X)=0` for ALL su(3)_R generators "
    "(Cartan AND root — every su(3) generator lives in the adjoint `8=(1,1)`, center "
    "character 0; the roots lie in the root lattice = ker of the center character) ⇒ the "
    "correct exclusion is the **commutant / Skolem–Noether leg-membership** mechanism "
    "(`Ω¹_{D_K}(A_K) ⊆ ⊕ B(V_{(p,q)})⊗1`; `R_{E_α}=1⊗E_α^*` "
    "non-scalar on the multiplicity leg ⇒ ∉ `B(V)⊗1`), corroborated by the "
    "framework's own `connes-r2.md` PROVEN findings (“the multiplicity leg is `R_X`-active "
    "(right-regular)”; the homogeneity wall is the multiplicity-scalar / commutant one); the "
    "`±1` cited above is the generation-SLOT-permutation grading, NOT the Z₃ center "
    "character. Axis-B (volovik) affirmed `t(O)=±1` AND the commutant identity "
    "(`[L,R]=0` Sage-exact). The D4-external CONCLUSION (CLOSED-EXTERNAL-AS-A-COUPLING; the "
    "genus is COMPLETE for `A_K`-INTERNAL couplings) is UNAFFECTED — both axes PASS the "
    "JOINT clause, the mechanism dispute does not weaken it (W3-1 residual=1.000000 EXACT is the "
    "numerical shadow of leg-membership either way). Per `Investigating-Workshops.md` Q1 + the "
    "capstone-hygiene rule this is a genuinely-unreconciled math/physics adjudication: mechanism "
    "reconciliation (apply the corrigendum) + the STAGE-3-PERMANENT → "
    "STAGE-3-PERMANENT-UNCONDITIONAL re-scope are FORWARD-ROUTED to "
    "`CF-S116-VIICK-D4-MECHANISM-CORRIGENDUM`. NO UNCONDITIONAL flip this session; "
    "§VII.CK STAYS STAGE-3-PERMANENT (D4-open). The existing `t(O)=±1` text is "
    "RETAINED (audit-trail preservation — not silently down-tagged, not rewritten by this "
    "closeout)."
)


def add_status_pointer() -> dict:
    """Idempotent single-pass read-modify-write: append the STATUS pointer after
    each of the two unique anchors. Returns pre/post SHA + per-anchor applied flag.
    """
    pre_sha = sha256_of(REGISTRY_PATH)                              # (local)
    text = REGISTRY_PATH.read_text(encoding="utf-8")               # (local)

    already_present = STATUS_POINTER_MARKER in text                # (local)
    applied = {"d4_row": False, "d4_annotation": False}            # (local)
    missing_anchors = []                                           # (local)

    new_text = text                                                # (local)
    for tag, anchor in (("d4_row", ANCHOR_D4_ROW), ("d4_annotation", ANCHOR_D4_ANNOT)):
        if anchor not in new_text:
            missing_anchors.append(tag)
            continue
        # idempotency: only append if the pointer does not already follow THIS anchor
        idx = new_text.find(anchor)                                # (local)
        after = new_text[idx + len(anchor): idx + len(anchor) + len(STATUS_POINTER_TEXT) + 120]  # (local)
        if STATUS_POINTER_MARKER in after:
            continue  # already annotated at this anchor — NO-OP
        new_text = new_text.replace(anchor, anchor + STATUS_POINTER_TEXT, 1)
        applied[tag] = True

    wrote = False                                                  # (local)
    if new_text != text:
        # atomic write with fsync (write to a temp sibling, then replace)
        import os
        tmp = REGISTRY_PATH.with_suffix(".md.tmp_w2_1")            # (local)
        with tmp.open("w", encoding="utf-8", newline="") as f:
            f.write(new_text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, REGISTRY_PATH)
        wrote = True

    post_sha = sha256_of(REGISTRY_PATH)                            # (local)

    # post-write verification: STATUS pointer present AND stage tag still STAGE-3-PERMANENT (D4-open)
    verify_text = REGISTRY_PATH.read_text(encoding="utf-8")        # (local)
    pointer_present = STATUS_POINTER_MARKER in verify_text         # (local)
    stage_tag_intact = (
        "**STAGE TAG: STAGE-3-PERMANENT**" in verify_text
        and "D4-open scope qualifier RETAINED" in verify_text
    )                                                              # (local)
    no_unconditional_landed = "STAGE-3-PERMANENT-UNCONDITIONAL** " not in verify_text  # (local) the **tag** never flipped (mentions in prose are OK)
    contested_text_retained = "`t(O)=±1≠0` center-character selection rule" in verify_text  # (local) original mechanism RETAINED (exact on-disk token, backtick-delimited)

    return {
        "pre_sha": pre_sha,
        "post_sha": post_sha,
        "already_present_before": already_present,
        "applied_d4_row": applied["d4_row"],
        "applied_d4_annotation": applied["d4_annotation"],
        "missing_anchors": missing_anchors,
        "wrote": wrote,
        "pointer_present_after": pointer_present,
        "stage_tag_intact": stage_tag_intact,
        "no_unconditional_landed": no_unconditional_landed,
        "contested_text_retained": contested_text_retained,
    }


# ---------------------------------------------------------------------------
# Section 8 — Verdict payload printer
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins + dual SHA
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap+identity)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Parse reviewer clause-verdicts
    text_a = REVIEWER_A_PATH.read_text(encoding="utf-8")  # (local)
    text_b = REVIEWER_B_PATH.read_text(encoding="utf-8")  # (local)
    verdicts = {                                          # (local)
        "A_leg": _parse_machine_verdict(text_a, "A_leg_verdict"),
        "JOINT_A": _parse_machine_verdict(text_a, "JOINT_verdict"),
        "B_leg": _parse_machine_verdict(text_b, "B_leg_verdict"),
        "JOINT_B": _parse_machine_verdict(text_b, "JOINT_verdict"),
    }
    print("=== reviewer clause-verdicts (machine-readable) ===")
    for k, v in verdicts.items():
        print(f"  {k}: {v}")

    # 3. Apply the pre-registered PASS-AND operator
    composite = pass_and(verdicts)  # (local)
    print(f"  PASS-AND over {{A-leg, B-leg, JOINT-A, JOINT-B}} -> composite = {composite}")
    assert composite == "INFO", (
        f"expected composite=INFO (one INFO, no FAIL) but got {composite}; "
        f"verdicts={verdicts}")

    # 4. W3-1 residual readback
    w3 = read_w3_1_residual()  # (local)
    print("=== W3-1 residual readback (s114_yuk_rightreg_connection.npz) ===")
    print(f"  residual_iv_min={w3['residual_iv_min']} residual_iv_max={w3['residual_iv_max']} "
          f"unit_exact={w3['residual_is_unit_exact']} audit_pin_matches={w3['audit_pin_matches']} "
          f"path_drift={w3['path_drift']}")

    # 5. Reviewer-exclusion ∅-intersection cross-check
    reviewer_set = set(REVIEWERS.keys())                    # (local)
    excl_intersection = reviewer_set & EXCLUDED_AUTHORS      # (local)
    w1_overlap = reviewer_set & W1_1_REVIEWERS               # (local)
    exclusion_clean = (len(excl_intersection) == 0)         # (local)
    disjoint_from_w1 = (len(w1_overlap) == 0)               # (local)
    print("=== reviewer-exclusion ∅-intersection ===")
    print(f"  reviewers={sorted(reviewer_set)}")
    print(f"  {{reviewers}} ∩ excluded_authors = {sorted(excl_intersection)} "
          f"(clean={exclusion_clean})")
    print(f"  {{reviewers}} ∩ W1-1{{lizzi,kitaev}} = {sorted(w1_overlap)} "
          f"(disjoint={disjoint_from_w1})")

    # 6. STATUS-pointer add (INFO branch; idempotent) + registry SHA pre/post
    print("=== STATUS-pointer add (INFO disposition; idempotent annotation) ===")
    sp = add_status_pointer()  # (local)
    print(f"  reg_pre={sp['pre_sha'][:16]}  reg_post={sp['post_sha'][:16]}")
    print(f"  applied_d4_row={sp['applied_d4_row']} applied_d4_annotation={sp['applied_d4_annotation']} "
          f"already_present_before={sp['already_present_before']} wrote={sp['wrote']}")
    print(f"  pointer_present_after={sp['pointer_present_after']} stage_tag_intact={sp['stage_tag_intact']} "
          f"no_unconditional_landed={sp['no_unconditional_landed']} "
          f"contested_text_retained={sp['contested_text_retained']}")
    if sp["missing_anchors"]:
        print(f"  WARNING missing_anchors={sp['missing_anchors']}")

    # Hard guards: the STATUS pointer must be present, the stage tag must be UNCHANGED,
    # the contested text must be RETAINED, and NO UNCONDITIONAL flip may have landed.
    assert sp["pointer_present_after"], "STATUS pointer not present after add"
    assert sp["stage_tag_intact"], "stage tag drifted from STAGE-3-PERMANENT (D4-open)"
    assert sp["no_unconditional_landed"], "UNCONDITIONAL flip landed — FORBIDDEN on INFO"
    assert sp["contested_text_retained"], "contested t(O)=±1 text was rewritten — FORBIDDEN"
    assert not sp["missing_anchors"], f"registry anchors not found: {sp['missing_anchors']}"

    # 7. Persist the npz record
    np.savez(
        OUT_NPZ,
        composite_verdict=composite,
        composite_is_info=(composite == "INFO"),
        verdict_A_leg=verdicts["A_leg"],
        verdict_B_leg=verdicts["B_leg"],
        verdict_JOINT_A=verdicts["JOINT_A"],
        verdict_JOINT_B=verdicts["JOINT_B"],
        pass_and_operator="composite=PASS iff all{A-leg,B-leg,JOINT-A,JOINT-B}∈PASS; any FAIL⇒FAIL; any INFO(no FAIL)⇒INFO",
        w3_1_residual_iv_min=w3["residual_iv_min"],
        w3_1_residual_iv_max=w3["residual_iv_max"],
        w3_1_residual_is_unit_exact=w3["residual_is_unit_exact"],
        w3_1_npz_path=w3["path"],
        w3_1_audit_pin_matches=w3["audit_pin_matches"],
        w3_1_path_drift=w3["path_drift"],
        reviewers=sorted(reviewer_set),
        excluded_authors=sorted(EXCLUDED_AUTHORS),
        exclusion_intersection_empty=exclusion_clean,
        disjoint_from_w1_1=disjoint_from_w1,
        d4_mechanism_contest="Axis-A t(R_X)=0 commutant/leg-membership (corroborated connes-r2.md PROVEN) vs registry/Axis-B t(O)=±1 center-character selection rule",
        no_unconditional_flip=True,
        viick_stays_stage3_d4_open=True,
        registry_sha_pre=sp["pre_sha"],
        registry_sha_post=sp["post_sha"],
        status_pointer_applied_d4_row=sp["applied_d4_row"],
        status_pointer_applied_d4_annotation=sp["applied_d4_annotation"],
        status_pointer_already_present_before=sp["already_present_before"],
        stage_tag_intact=sp["stage_tag_intact"],
        contested_text_retained=sp["contested_text_retained"],
        forward_route_cf="CF-S116-VIICK-D4-MECHANISM-CORRIGENDUM",
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  npz -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 8. Build the verdict value string (honest, machine-greppable)
    value = (
        f"composite=INFO_A-leg=INFO_B-leg=PASS_JOINT-A=PASS_JOINT-B=PASS_"
        f"PASS-AND(any_INFO_no_FAIL=>INFO)_"
        f"D4-mech-CONTESTED(t(R_X)=0_commutant/leg-membership_per_Axis-A+connes-r2.md_vs_t(O)=±1_per_registry+Axis-B)_"
        f"W3-1_residual={w3['residual_iv_min']:.6f}_EXACT(unit={w3['residual_is_unit_exact']})_"
        f"excl_∅={exclusion_clean}_disjoint_W1-1={disjoint_from_w1}_"
        f"NO-UNCONDITIONAL-flip_VIICK-stays-STAGE-3-PERMANENT-D4-open_"
        f"STATUS-pointer-added(reg_pre={sp['pre_sha'][:16]}_reg_post={sp['post_sha'][:16]})_"
        f"mechanism->CF-S116-VIICK-D4-MECHANISM-CORRIGENDUM"
    )  # (local)

    # 9. 4-tuple + verdict payload
    tag = f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"  # (local)
    print(tag)
    companion = (
        f"# D4-CONTEST: Axis-A t(R_X)=0 (commutant/leg-membership, connes-r2.md PROVEN corroborated) "
        f"vs Axis-B/registry t(O)=±1; JOINT PASS both axes ⇒ D4-external CONCLUSION UNAFFECTED; "
        f"NO-UNCONDITIONAL-flip; §VII.CK STAGE-3-PERMANENT(D4-open); mechanism→CF-S116-VIICK-D4-MECHANISM-CORRIGENDUM"
    )  # (local)
    print_verdict_payload(composite, value, audit_sha, content_sha, extra_rows=[companion])

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0  # INFO is a valid scientific result — exit 0


if __name__ == "__main__":
    sys.exit(main())
