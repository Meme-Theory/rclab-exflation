#!/usr/bin/env python3
"""
S112 W2-3 CF-S112-M1-INTERTWINER-STAGE2 — Stage-2 cross-axis PASS-AND collation
==============================================================================

Gate: CF-S112-M1-INTERTWINER-STAGE2 ([VERIFY-THEOREM])

Theorem under verify: §VII.CI — Categorical Two-Conjunct Obstruction Theorem for
  the χ Inheritance Morphism (χ : A_K = ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ) is the Connes-Karoubi
  DELETION for ALL constructions/bridges, NOT the Kasparov shriek π_!^{CP²}).
  The discharge condition for LBA-5 is a CONJUNCTION: a vertically-elliptic σ_v
  must (i) SELECT ker(ι_*)=M_3(ℂ) AND (ii) carry a NON-trivial integrated
  K-homology class. CONJUNCT (i) [Axis-2 C*-algebra-type] forecloses the SELECTION
  on ALL homomorphism-type constructions; CONJUNCT (ii) [Axis-1 K-homology]
  forecloses the NON-trivial image on ALL K-natural bridges. The two scopes are
  DISJOINT (K-natural XOR not) + EXHAUSTIVE, so (i)∧(ii) is the categorical
  obstruction (not "two decidable axes").

Pre-registered threshold (the gate OPERATOR — a deterministic logical conjunction,
NOT a numerical inequality; per `joint-theorem-promotion.md §"Stage 2"`, plan
§W2-3 PASS-AND form):

  composite = PASS  iff  ( A.conjunct_ii == PASS )
                    AND  ( B.conjunct_i  == PASS )
                    AND  ( A.joint == PASS  AND  B.joint == PASS )  # complementary-conjunct JOINT, PASS-AND'd across BOTH

  where A = lizzi-spectral-functional-theorist (Axis-A K-homology / algebra-INVARIANT;
            clauses conjunct_ii, joint)
        B = kaluza-klein-theorist (Axis-B C*-algebra-type / algebra-DEPENDENT;
            clauses conjunct_i, joint)

  ANY clause literally FAIL → composite FAIL (theorem stays STAGE-1-CANDIDATE).
  No FAIL but ANY clause literally INFO → composite INFO (Stage-2-INFO-deferred).
  A non-gating wording-nit / ORTHOGONAL-COMPANION-reading note carried in the
  reviewers' `notes` is INFO-CONTENT, NOT a literal clause verdict — it does NOT
  collapse the composite. (Plan §W2-3 INFO_meaning: collapse only if a clause
  field is literally "INFO".)

Inputs (SHA-256 dual-pinned at runtime — see §4; S84+ schema). The audit_sha256
input-pin map (per plan §W2-3 audit_discriminators) is 7-wide:
  - script bytes (feeds BOTH audit_sha256 and content_sha256)
  - sessions/permanent-results-registry.md §VII.CI body (anchor-extracted block)
  - computations/session-111/s111_m1_intertwiner_conjunct_i.npz   (Axis-2 conjunct (i) artifact)
  - computations/session-111/s111_m1_conjunct_ii_khomology.npz     (Axis-1 conjunct (ii) artifact; STATIC SHA pin)
  - computations/session-112/s112_m1_intertwiner_stage2_axisA_lizzi.json (Axis-A clause verdicts)
  - computations/session-112/s112_m1_intertwiner_stage2_axisB_kk.json    (Axis-B clause verdicts)
  - canonical_constants.py (feeds audit_sha256 only)

Output 4-tuple:
  (value=<clause-matrix summary>, scheme=STAGE-2-CROSS-AXIS-PASS-AND,
   convention=COMPLEMENTARY-CONJUNCT-LOGICAL-AND, L_max=N/A)

Classification: GEOMETRIC (intra-NCG categorical / K-homology structural theorem;
  no laboratory-IN observable; L-INDEPENDENT — K^0(A_K)=ℤ³ is fixed by Morita
  invariance independent of any truncation).

METHODOLOGY
-----------
Deterministic collation: read the two NON-AUTHOR cross-reviewer clause-verdict
JSONs, build the per-reviewer per-clause verdict matrix, compute the logical
PASS-AND of the four clause positions (conjunct_ii on Axis-A; conjunct_i on
Axis-B; joint complementary-conjunct, PASS-AND'd across BOTH reviewers), and emit
the composite verdict. NO physics is re-adjudicated — the verdict is a pure
boolean function of the reviewer-emitted clause verdicts (`emit_verdict` enforces
the line grammar). The audit_sha256 closes over the ordered 7-input pin map
[script, §VII.CI body, conjunct_i npz, conjunct_ii npz, reviewer_A_json,
reviewer_B_json, canonical]; content_sha256 over script bytes only. The Axis-1
conjunct_ii npz carries a STATIC SHA pin (47b7bac1…, the §VII.CI Option-A re-pin);
the script HARD-asserts the on-disk SHA matches, so a stale/swapped npz surfaces
as a script error (exit != 0), never a silent drift.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-only (JSON read + boolean AND + hashlib); OMP_NUM_THREADS capped at 8
- SHA-256 of all input files logged in first lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe):
  this script PRINTS the payload (`print_verdict_payload`); the dispatching AGENT
  reads it and calls `mcp__knowledge__emit_verdict(**payload)`. The script does
  NOT write s112_gate_verdicts.txt directly.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (collation only; no GPU linear algebra) + path bootstrap
# ---------------------------------------------------------------------------
import os
import sys
from pathlib import Path as _Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# Make computations/_shared importable so `from canonical_constants import *`
# resolves when the script is invoked from the project root.
sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "_shared"))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
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

SESSION = "S112"                                                   # (local)
GATE_ID = "CF-S112-M1-INTERTWINER-STAGE2"                          # (local)
SCHEME = "STAGE-2-CROSS-AXIS-PASS-AND"                             # (local)
CONVENTION = "COMPLEMENTARY-CONJUNCT-LOGICAL-AND"                  # (local)
L_MAX = "N/A"                                                      # (local) L-INDEPENDENT categorical/K-homology theorem

# Registered theorem + its anchor (the §VII.CI block is the source-of-truth the
# reviewers audit; we anchor-extract its body for the audit_sha256 input).
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"      # (local)
VII_CI_START_ANCHOR = "### §VII.CI — Categorical Two-Conjunct Obstruction Theorem"  # (local)
VII_CI_END_ANCHOR = "### §VII.CJ —"                              # (local) next-entry boundary

# Cross-reviewer clause-verdict JSONs
REVIEWER_A_JSON = SESSION_DIR / "s112_m1_intertwiner_stage2_axisA_lizzi.json"     # (local)
REVIEWER_B_JSON = SESSION_DIR / "s112_m1_intertwiner_stage2_axisB_kk.json"        # (local)

# Conjunct artifacts (S111; pinned in the audit_sha256 input map per plan §W2-3)
CONJUNCT_I_NPZ = COMPUTATIONS_DIR / "session-111" / "s111_m1_intertwiner_conjunct_i.npz"        # (local) Axis-2
CONJUNCT_II_NPZ = COMPUTATIONS_DIR / "session-111" / "s111_m1_conjunct_ii_khomology.npz"        # (local) Axis-1
# STATIC SHA pin for the authoritative Axis-1 npz (the §VII.CI Option-A re-pin).
CONJUNCT_II_NPZ_PINNED_SHA = "47b7bac1c2f5ac635d95a382e226c1e35218dba713a176f3e4afeef3e920a68f"  # (local)

# Reviewer / axis identities (for the matrix + audit pinmap)
REVIEWER_A_NAME = "lizzi-spectral-functional-theorist"            # (local)
REVIEWER_B_NAME = "kaluza-klein-theorist"                         # (local)

# Clause ownership: which reviewer owns which clause position.
#   Axis-A (lizzi): conjunct_ii + joint
#   Axis-B (kk): conjunct_i + joint
# JOINT complementary-conjunct is PASS-AND'd across BOTH reviewers.
AXIS_A_SINGLE_CLAUSES = ["conjunct_ii"]                           # (local)
AXIS_B_SINGLE_CLAUSES = ["conjunct_i"]                            # (local)
JOINT_CLAUSE = "joint"                                            # (local)

# Original-author exclusions (Stage-0 WS-M1-INTERTWINER authors; recorded for the WP audit)
#   connes = conjunct (ii)/Axis-1; van-den-dungen = conjunct (i)/Axis-2.
EXCLUDED_AUTHORS = ["connes-ncg-theorist", "van-den-dungen-bridge-theorist"]      # (local)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s112_cf_m1_intertwiner_stage2.npz"
OUT_PNG = SESSION_DIR / "s112_cf_m1_intertwiner_stage2.png"
# The verdict file is written by the emit_verdict MCP tool — NOT by this script.

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
    CONJUNCT_I_NPZ,
    CONJUNCT_II_NPZ,
    REVIEWER_A_JSON,
    REVIEWER_B_JSON,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first lines of stdout)
#
# S84+ DUAL-SHA SCHEMA:
#   audit_sha256   = sha256( bytes(script) || bytes(canonical) || bytes(pinmap_json) )
#   content_sha256 = sha256( bytes(script) )
#
# pinmap_json is the canonical (sorted) JSON of {relpath_or_anchor: sha256} over
# the ordered audit inputs (7-wide per plan §W2-3 audit_discriminators): script,
# §VII.CI body block, conjunct_i npz, conjunct_ii npz, reviewer_A_json,
# reviewer_B_json, canonical_constants.py. The §VII.CI body is anchor-extracted
# (NOT the whole 22k-line registry) so the SHA tracks the theorem text.
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def extract_section(path: Path, start_anchor: str, end_anchor: str) -> str:
    """Extract the registry block from start_anchor up to (not incl.) end_anchor.

    Returns the block text. HARD-asserts the block is non-empty and contains BOTH
    conjunct-foreclosure markers, so a slot-drift / anchor-mismatch surfaces as a
    script error (exit != 0), never a silent empty-SHA PASS.
    """
    text = path.read_text(encoding="utf-8")  # (local)
    i = text.find(start_anchor)  # (local)
    if i < 0:
        raise SystemExit(f"FATAL: start anchor {start_anchor!r} not found in {path}")
    j = text.find(end_anchor, i + len(start_anchor))  # (local)
    if j < 0:
        raise SystemExit(f"FATAL: end anchor {end_anchor!r} not found after start in {path}")
    block = text[i:j]  # (local)
    # Distinctive interior markers unique to the §VII.CI two-conjunct obstruction body.
    if "CONJUNCT (i) VERDICT: FORECLOSED" not in block:
        raise SystemExit("FATAL: §VII.CI block missing 'CONJUNCT (i) VERDICT: FORECLOSED' marker — wrong slot extracted")
    if "CONJUNCT (ii) VERDICT: FORECLOSED" not in block:
        raise SystemExit("FATAL: §VII.CI block missing 'CONJUNCT (ii) VERDICT: FORECLOSED' marker — wrong slot extracted")
    if "complementary-conjunct" not in block.lower():
        raise SystemExit("FATAL: §VII.CI block missing the complementary-conjunct JOINT marker — wrong slot extracted")
    return block


def sha256_of_text(s: str) -> str:
    """SHA-256 over a unicode string's UTF-8 bytes."""
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def log_input_pins() -> dict[str, str]:
    """Print SHA-256 of each audit input; return {key: sha} for closure hash.

    Keys are project-relative paths, except the registry which is keyed by its
    §VII.CI ANCHOR (the SHA is over the extracted block, not the whole file).
    HARD-asserts the Axis-1 conjunct_ii npz matches its STATIC pinned SHA.
    """
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)

    # script bytes
    script_path = Path(__file__).resolve()  # (local)
    pins["computations/session-112/s112_cf_m1_intertwiner_stage2.py"] = sha256_of(script_path)

    # canonical_constants.py
    can_path = SHARED_DIR / "canonical_constants.py"  # (local)
    pins["computations/_shared/canonical_constants.py"] = sha256_of(can_path)

    # §VII.CI body block (anchor-extracted)
    ci_block = extract_section(REGISTRY_PATH, VII_CI_START_ANCHOR, VII_CI_END_ANCHOR)  # (local)
    ci_sha = sha256_of_text(ci_block)  # (local)
    pins["sessions/permanent-results-registry.md#§VII.CI-body"] = ci_sha

    # conjunct artifacts (S111)
    ci_i_sha = sha256_of(CONJUNCT_I_NPZ)  # (local)
    ci_ii_sha = sha256_of(CONJUNCT_II_NPZ)  # (local)
    pins["computations/session-111/s111_m1_intertwiner_conjunct_i.npz"] = ci_i_sha
    pins["computations/session-111/s111_m1_conjunct_ii_khomology.npz"] = ci_ii_sha

    # STATIC pin assertion on the authoritative Axis-1 conjunct_ii npz.
    if ci_ii_sha != CONJUNCT_II_NPZ_PINNED_SHA:
        raise SystemExit(
            "FATAL: conjunct_ii npz SHA mismatch — on-disk "
            f"{ci_ii_sha} != pinned {CONJUNCT_II_NPZ_PINNED_SHA} "
            "(§VII.CI Option-A re-pin authoritative Axis-1 npz drifted/swapped)"
        )

    # reviewer JSONs
    pins["computations/session-112/s112_m1_intertwiner_stage2_axisA_lizzi.json"] = sha256_of(REVIEWER_A_JSON)
    pins["computations/session-112/s112_m1_intertwiner_stage2_axisB_kk.json"] = sha256_of(REVIEWER_B_JSON)

    for k, v in sorted(pins.items()):
        print(f"  {k}: {v[:16]}...")
    print(f"  §VII.CI body block: {len(ci_block)} chars, sha {ci_sha[:16]}...")
    print(f"  conjunct_ii npz STATIC pin verified: {ci_ii_sha[:16]}... == pinned {CONJUNCT_II_NPZ_PINNED_SHA[:16]}...")
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(pins: dict[str, str]) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256:
        sha256( bytes(script) || bytes(canonical_constants.py) || pinmap_json )
        where pinmap_json is the canonical sorted JSON of the FULL ordered 7-input
        pin map (script, §VII.CI body, conjunct_i npz, conjunct_ii npz, both
        reviewer JSONs, canonical).
    content_sha256:
        sha256( bytes(script) ) — responds to script edits only.
    """
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute (the PASS-AND collation)
# ---------------------------------------------------------------------------

def load_clause_verdicts(path: Path, expected_axis: str, expected_clauses: list[str]) -> dict:
    """Load a reviewer's clause-verdict JSON; HARD-assert schema + clause presence.

    Returns {clause: verdict_str} for the expected clauses. Raises if the gate_id
    / theorem / axis mismatch, or any expected clause is missing.
    """
    data = json.loads(path.read_text(encoding="utf-8"))  # (local)
    if data.get("gate_id") != GATE_ID:
        raise SystemExit(f"FATAL: {path.name} gate_id {data.get('gate_id')!r} != {GATE_ID}")
    if data.get("theorem") != "§VII.CI":
        raise SystemExit(f"FATAL: {path.name} theorem {data.get('theorem')!r} != §VII.CI")
    if data.get("axis") != expected_axis:
        raise SystemExit(f"FATAL: {path.name} axis {data.get('axis')!r} != {expected_axis}")
    clauses = data.get("clauses", {})  # (local)
    out: dict[str, str] = {}  # (local)
    for c in expected_clauses:
        if c not in clauses:
            raise SystemExit(f"FATAL: {path.name} missing clause {c!r}")
        v = clauses[c].get("verdict")  # (local)
        if v not in ("PASS", "FAIL", "INFO"):
            raise SystemExit(f"FATAL: {path.name} clause {c!r} verdict {v!r} not in PASS/FAIL/INFO")
        out[c] = v
    return out


def compute() -> dict:
    """Collate the two reviewer JSONs into the composite PASS-AND verdict."""
    # Axis-A (lizzi) owns conjunct_ii + joint
    a = load_clause_verdicts(REVIEWER_A_JSON, "A", AXIS_A_SINGLE_CLAUSES + [JOINT_CLAUSE])  # (local)
    # Axis-B (kk) owns conjunct_i + joint
    b = load_clause_verdicts(REVIEWER_B_JSON, "B", AXIS_B_SINGLE_CLAUSES + [JOINT_CLAUSE])  # (local)

    # The four clause POSITIONS that enter the PASS-AND, with their owning reviewer.
    #   conjunct_ii -> Axis-A only
    #   conjunct_i  -> Axis-B only
    #   joint       -> JOINT (complementary-conjunct): BOTH A and B must PASS independently
    clause_matrix = {  # (local)
        "conjunct_ii@A": a["conjunct_ii"],
        "conjunct_i@B": b["conjunct_i"],
        "joint@A": a[JOINT_CLAUSE],
        "joint@B": b[JOINT_CLAUSE],
    }

    all_verdicts = list(clause_matrix.values())  # (local)
    any_fail = any(v == "FAIL" for v in all_verdicts)  # (local)
    any_info = any(v == "INFO" for v in all_verdicts)  # (local)
    all_pass = all(v == "PASS" for v in all_verdicts)  # (local)

    # Composite collapse (pre-registered, plan §W2-3):
    #   ANY literal FAIL            -> FAIL
    #   no FAIL but ANY literal INFO -> INFO
    #   all PASS                    -> PASS
    if any_fail:
        composite = "FAIL"  # (local)
    elif any_info:
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)

    # Sanity: the three branches partition exhaustively.
    assert composite in ("PASS", "FAIL", "INFO")
    assert all_pass == (composite == "PASS")

    # JOINT complementary-conjunct PASS-AND across both reviewers (the structural-
    # independence guarantee: BOTH NON-AUTHOR reviewers must independently PASS the
    # complementary-conjunct exhaustiveness JOINT).
    joint_pass_and = (a[JOINT_CLAUSE] == "PASS") and (b[JOINT_CLAUSE] == "PASS")  # (local)

    # Overall axis verdicts the reviewers self-reported (cross-check only).
    a_overall = json.loads(REVIEWER_A_JSON.read_text(encoding="utf-8")).get("overall_axis_verdict")  # (local)
    b_overall = json.loads(REVIEWER_B_JSON.read_text(encoding="utf-8")).get("overall_axis_verdict")  # (local)

    return {
        "composite": composite,
        "clause_matrix": clause_matrix,
        "axis_A": a,
        "axis_B": b,
        "joint_pass_and": joint_pass_and,
        "axis_A_overall": a_overall,
        "axis_B_overall": b_overall,
        "any_fail": any_fail,
        "any_info": any_info,
        "all_pass": all_pass,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    companion_note: str = "",
    extra_rows: list[str] | None = None,
) -> dict:
    """Print the verdict PAYLOAD for the dispatching AGENT to pass to emit_verdict.

    [VERIFY-THEOREM] gate — NO 3-tuple (sign/magnitude/regime). The script does
    NOT write the verdict file; the agent reads this delimited JSON block and
    calls mcp__knowledge__emit_verdict(**payload).
    """
    payload: dict = {  # (local)
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
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first lines of stdout)
    pins = log_input_pins()
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    audit_sha, content_sha = compute_dual_sha(pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute the PASS-AND collation
    result = compute()  # (local)
    composite = result["composite"]  # (local)

    print("=== clause-verdict matrix (per-reviewer per-clause) ===")
    print(f"  Axis-A ({REVIEWER_A_NAME}): conjunct_ii={result['axis_A']['conjunct_ii']}  "
          f"joint={result['axis_A'][JOINT_CLAUSE]}  "
          f"[overall={result['axis_A_overall']}]")
    print(f"  Axis-B ({REVIEWER_B_NAME}): conjunct_i={result['axis_B']['conjunct_i']}  "
          f"joint={result['axis_B'][JOINT_CLAUSE]}  "
          f"[overall={result['axis_B_overall']}]")
    print(f"  JOINT complementary-conjunct PASS-AND (A∧B): {result['joint_pass_and']}")
    print(f"  PASS-AND over {{conjunct_ii@A, conjunct_i@B, joint@A, joint@B}}: composite={composite}")
    print()

    # 3. Build the compact value payload string (no single-quote chars; emit_verdict
    #    wraps value='...').
    cm = result["clause_matrix"]  # (local)
    value = (
        f"composite={composite};"
        f"conjunct_ii@A={cm['conjunct_ii@A']};conjunct_i@B={cm['conjunct_i@B']};"
        f"joint@A={cm['joint@A']};joint@B={cm['joint@B']};"
        f"joint_complementary_conjunct_passAND={result['joint_pass_and']};"
        f"axisA_overall={result['axis_A_overall']};axisB_overall={result['axis_B_overall']};"
        f"STRUCTURAL-ORTHOGONAL-COMPANION=Axis1-algebra-INVARIANT_Axis2-algebra-DEPENDENT_NOT-cross-corner-co-primary;"
        f"VII-CI-flip=STAGE-1-CANDIDATE-to-STAGE-3-PERMANENT-on-PASS"
    )  # (local)

    # 4. Persist the clause-verdict matrix to npz
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        theorem="§VII.CI",
        composite=composite,
        clause_keys=np.array(list(cm.keys())),
        clause_verdicts=np.array(list(cm.values())),
        axisA_reviewer=REVIEWER_A_NAME,
        axisB_reviewer=REVIEWER_B_NAME,
        axisA_conjunct_ii=result["axis_A"]["conjunct_ii"],
        axisA_joint=result["axis_A"][JOINT_CLAUSE],
        axisB_conjunct_i=result["axis_B"]["conjunct_i"],
        axisB_joint=result["axis_B"][JOINT_CLAUSE],
        joint_complementary_conjunct_pass_and=result["joint_pass_and"],
        axisA_overall=result["axis_A_overall"],
        axisB_overall=result["axis_B_overall"],
        any_fail=result["any_fail"],
        any_info=result["any_info"],
        all_pass=result["all_pass"],
        excluded_authors=np.array(EXCLUDED_AUTHORS),
        conjunct_ii_npz_pinned_sha=CONJUNCT_II_NPZ_PINNED_SHA,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  wrote {OUT_NPZ.name}")

    # 5. Emit 4-tuple + PRINT the emit_verdict payload.
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)

    companion = (
        f"§VII.CI Stage-2 cross-axis PASS-AND: A({REVIEWER_A_NAME})={result['axis_A_overall']} "
        f"B({REVIEWER_B_NAME})={result['axis_B_overall']}; JOINT complementary-conjunct A∧B="
        f"{result['joint_pass_and']}; composite={composite}; "
        f"conjunct (ii)/Axis-1 K-homology @A ∧ conjunct (i)/Axis-2 C*-algebra-type @B; "
        f"STRUCTURAL-ORTHOGONAL-COMPANION (algebra-INVARIANT + algebra-DEPENDENT), never cross-corner co-primary"
    )  # (local)
    extra = [
        f"# excluded_authors={','.join(EXCLUDED_AUTHORS)} (Stage-0 WS-M1-INTERTWINER; connes=conjunct(ii)/Axis-1, vdd=conjunct(i)/Axis-2; original-author exclusion + downstream-inheritance reach)",
        "# JOINT complementary-conjunct PASS-AND'd across BOTH NON-AUTHOR reviewers (structural-independence guarantee; neither read the WS-M1-INTERTWINER workshop)",
        "# on PASS: §VII.CI STAGE-1-CANDIDATE -> STAGE-3-PERMANENT (mack applies the registry tag-flip); LICENSES atlas-04 N7 / §VII.W-3.SUBSTRATE(c) / atlas-08 Q10-Q9 categorical upgrade",
    ]  # (local)
    print_verdict_payload(composite, value, audit_sha, content_sha,
                          companion_note=companion, extra_rows=extra)

    # 6. Final summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    # Exit 0 on any valid scientific verdict (PASS/FAIL/INFO); != 0 only on breakage.
    return 0


if __name__ == "__main__":
    sys.exit(main())
