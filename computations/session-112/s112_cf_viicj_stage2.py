#!/usr/bin/env python3
"""
S112 W2-4 CF-S112-VIICJ-STAGE2 — Stage-2 cross-axis PASS-AND collation
======================================================================

Gate: CF-S112-VIICJ-STAGE2 ([VERIFY-THEOREM])

Theorem under verify: §VII.CJ — McLachlan Tongue-Half-Width Cutoff-Robustness
  Scaling-EXPONENT Theorem. The n-th Mathieu instability-tongue half-width about
  a=n^2 has leading power EXACTLY n on q (Sage/sympy-exact: n=1->q, n=2->q^2/4,
  n=3->q^3/64; degree_q==n, convention-INDEPENDENT), so any NEW relic mode admitted
  by an L_max>=12 truncation extension carries higher Casimir C_2(p,q) => higher
  A=omega^2 => lands near zone n=round(sqrt(A))>=3 (low-n zones SATURATED by the L12
  modes; npz: among the 80 relic modes with A>9, nearest_n in {3,4} ONLY) => gets an
  exponentially-suppressed tongue => |Tr M|<2 for every new mode => §VII.BP
  H-PARITY-DRIVE-EXCLUSION stays DEAD at any L_max>=12. The EXPONENT n is the
  registered structural claim; the x16 and ALL coefficient prefactors are
  DIAGNOSTIC-ONLY, convention-ambiguous, NOT registered.

Pre-registered threshold (the gate OPERATOR — a deterministic logical conjunction,
NOT a numerical inequality; per `joint-theorem-promotion.md §"Stage 2"`; plan §W2-4):

  composite = PASS  iff  ( A.casimir_A_placement   == PASS )
                    AND  ( B.exponent_and_nooverlap == PASS )
                    AND  ( A.joint_exponent == PASS  AND  B.joint_exponent == PASS )  # JOINT EXPONENT-n, PASS-AND'd across BOTH

  where A = connes-ncg-theorist (Axis-A spectral / D_K Casimir-ladder / A-placement;
            clauses casimir_A_placement, joint_exponent)
        B = landau-condensed-matter-theorist (Axis-B Mathieu-tongue / monodromy
            band-stability; clauses exponent_and_nooverlap, joint_exponent)

  ANY clause literally FAIL -> composite FAIL (theorem stays STAGE-1-CANDIDATE).
  No FAIL but ANY clause literally INFO -> composite INFO (Stage-2-INFO-deferred).
  Per-reviewer reach-INFO / diagnostic-side notes (e.g. the mnemonic-vs-exact
  prefactor disclosure, or the stored-quantity full-vs-half-width labeling note in
  the landau `notes`) are INFO-CONTENT, NOT a literal clause verdict — they do NOT
  collapse the composite. (Plan §W2-4 INFO_meaning: collapse only if a clause field
  is literally "INFO".)

Inputs (SHA-256 dual-pinned at runtime — see §4; S84+ schema):
  - computations/session-112/s112_viicj_stage2_axisA_connes.json   (Axis-A clause verdicts)
  - computations/session-112/s112_viicj_stage2_axisB_landau.json   (Axis-B clause verdicts)
  - sessions/permanent-results-registry.md §VII.CJ body (anchor-extracted block to EOF; feeds audit_sha256)
  - computations/investigation-12/inv12_w3_2_floquet_ordered_veil_resonance.npz (no-overlap certificate source; feeds audit_sha256)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

The audit_discriminators (plan §W2-4) pin the audit_sha256 inputs in order:
  [script, registered_entry_§VII.CJ_body, inv12_w3_2_npz,
   reviewer_A_clause_verdict_json, reviewer_B_clause_verdict_json, pinmap].
content_sha256 inputs: [script].

Output 4-tuple:
  (value=<clause-matrix summary>, scheme=STAGE-2-CROSS-AXIS-PASS-AND,
   convention=JOINT-EXPONENT-LOGICAL-AND, L_max=12)

Classification: PHONONIC (intra-pillar structural theorem on the substrate's own
  Ordered-Veil relic spectrum; the relic IS the post-fold Bogoliubov output state;
  the cutoff-robustness fact is L-EXTENSION-ROBUST by construction).

METHODOLOGY
-----------
Deterministic collation: read the two NON-AUTHOR cross-reviewer clause-verdict
JSONs, build the per-reviewer per-clause verdict matrix, compute the logical
PASS-AND of the four clause positions (casimir_A_placement on Axis-A;
exponent_and_nooverlap on Axis-B; joint_exponent JOINT, PASS-AND'd across BOTH
reviewers), and emit the composite verdict. NO physics is re-adjudicated — the
verdict is a pure boolean function of the reviewer-emitted clause verdicts
(`emit_verdict` enforces the line grammar). The inv12_w3_2 npz is loaded only to
echo the no-overlap certificate facts (0-of-1248 overlap; max|Tr M|=1.99999996;
worst-case i_closest=1168 A=9.000371 nearest_n=3) into the matrix + npz output for
the audit trail and to bind the certificate source into the audit_sha256 — those
facts are NOT re-derived here (the reviewers already verified them from first
principles). The audit_sha256 closes over the ordered input-pin map [script,
§VII.CJ body, inv12 npz, reviewer_A_json, reviewer_B_json, canonical];
content_sha256 over script bytes only.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-only (JSON read + npz echo + boolean AND + hashlib); OMP_NUM_THREADS capped at 8
- SHA-256 of all input files logged in first 20 lines of stdout
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
GATE_ID = "CF-S112-VIICJ-STAGE2"                                   # (local)
SCHEME = "STAGE-2-CROSS-AXIS-PASS-AND"                             # (local)
CONVENTION = "JOINT-EXPONENT-LOGICAL-AND"                          # (local)
L_MAX = "12"                                                       # (local) inv12_w3_2 relic spectrum + s84 L12 master cache; CLAIM is L>=12-extension-robust

# Registered theorem + its anchor (the §VII.CJ block is the source-of-truth the
# reviewers audit; we anchor-extract its body for the audit_sha256 input).
# §VII.CJ is the FINAL registry entry -> the block runs from the start-anchor to
# EOF (no next-entry end-anchor exists). extract_section handles end_anchor=None.
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"      # (local)
VII_CJ_START_ANCHOR = "### §VII.CJ —"                             # (local)
VII_CJ_END_ANCHOR = None                                          # (local) §VII.CJ is the last entry -> extract to EOF

# Cross-reviewer clause-verdict JSONs
REVIEWER_A_JSON = SESSION_DIR / "s112_viicj_stage2_axisA_connes.json"             # (local)
REVIEWER_B_JSON = SESSION_DIR / "s112_viicj_stage2_axisB_landau.json"            # (local)

# No-overlap-certificate source (inv-12 W3-2 survey npz) — pinned into the
# audit_sha256 per the plan audit_discriminators; facts echoed into the matrix.
INV12_NPZ = COMPUTATIONS_DIR / "investigation-12" / "inv12_w3_2_floquet_ordered_veil_resonance.npz"  # (local)

# Reviewer / axis identities (for the matrix + audit pinmap)
REVIEWER_A_NAME = "connes-ncg-theorist"                            # (local)
REVIEWER_B_NAME = "landau-condensed-matter-theorist"             # (local)

# Clause ownership: which reviewer owns which clause position.
#   Axis-A (connes): casimir_A_placement + joint_exponent
#   Axis-B (landau): exponent_and_nooverlap + joint_exponent
# JOINT joint_exponent is PASS-AND'd across BOTH reviewers.
AXIS_A_SINGLE_CLAUSES = ["casimir_A_placement"]                   # (local)
AXIS_B_SINGLE_CLAUSES = ["exponent_and_nooverlap"]                # (local)
JOINT_CLAUSE = "joint_exponent"                                  # (local)

# Original-author exclusion (Stage-0 + Stage-1 author; the Floquet/Bogoliubov/
# Mathieu/McLachlan math owner + inv-12 W3-2 survey author; recorded for the WP).
EXCLUDED_AUTHORS = ["transit-dynamics-theorist"]                  # (local)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s112_cf_viicj_stage2.npz"
OUT_PNG = SESSION_DIR / "s112_cf_viicj_stage2.png"
# The verdict file is written by the emit_verdict MCP tool — NOT by this script.


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
#
# S84+ DUAL-SHA SCHEMA:
#   audit_sha256   = sha256( bytes(script) || bytes(canonical) || bytes(pinmap_json) )
#   content_sha256 = sha256( bytes(script) )
#
# pinmap_json is the canonical (sorted) JSON of {relpath_or_anchor: sha256} over
# the ordered audit inputs: script, §VII.CJ body block, inv12_w3_2 npz,
# reviewer_A_json, reviewer_B_json, canonical_constants.py. The §VII.CJ body is
# anchor-extracted (NOT the whole 22k-line registry) so the SHA tracks the theorem
# text.
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def extract_section(path: Path, start_anchor: str, end_anchor: str | None) -> str:
    """Extract the registry block from start_anchor to end_anchor (exclusive).

    If end_anchor is None, extract from start_anchor to EOF (used here because
    §VII.CJ is the LAST registry entry, so there is no next-entry header to bound
    it). HARD-asserts the block is non-empty and carries the EXPONENT-theorem +
    no-overlap markers, so a slot-drift / anchor-mismatch surfaces as a script
    error (exit != 0), never a silent empty-SHA PASS.
    """
    text = path.read_text(encoding="utf-8")  # (local)
    i = text.find(start_anchor)  # (local)
    if i < 0:
        raise SystemExit(f"FATAL: start anchor {start_anchor!r} not found in {path}")
    if end_anchor is None:
        block = text[i:]  # (local) §VII.CJ runs to EOF
    else:
        j = text.find(end_anchor, i + len(start_anchor))  # (local)
        if j < 0:
            raise SystemExit(f"FATAL: end anchor {end_anchor!r} not found after start in {path}")
        block = text[i:j]  # (local)
    # HARD-assert the EXPONENT theorem + the no-overlap certificate are present —
    # the two load-bearing facts that identify §VII.CJ uniquely.
    if "Leading Power EXACTLY n on q" not in block:
        raise SystemExit("FATAL: §VII.CJ block missing the EXPONENT-theorem marker — wrong slot extracted")
    if "NO-OVERLAP certificate" not in block and "no-overlap certificate" not in block:
        raise SystemExit("FATAL: §VII.CJ block missing the no-overlap-certificate marker — wrong slot extracted")
    if "§VII.BP" not in block:
        raise SystemExit("FATAL: §VII.CJ block missing the §VII.BP-DEAD confirmatory reference — wrong slot extracted")
    return block


def sha256_of_text(s: str) -> str:
    """SHA-256 over a unicode string's UTF-8 bytes."""
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def log_input_pins() -> tuple[dict[str, str], int]:
    """Print SHA-256 of each audit input; return ({key: sha}, len_of_CJ_block).

    Keys are project-relative paths, except the registry which is keyed by its
    §VII.CJ ANCHOR (the SHA is over the extracted block, not the whole file).
    Ordered per the plan audit_discriminators:
      script, §VII.CJ body, inv12 npz, reviewer_A_json, reviewer_B_json, canonical.
    """
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)

    # script bytes
    script_path = Path(__file__).resolve()  # (local)
    pins["computations/session-112/s112_cf_viicj_stage2.py"] = sha256_of(script_path)

    # §VII.CJ body block (anchor-extracted to EOF)
    cj_block = extract_section(REGISTRY_PATH, VII_CJ_START_ANCHOR, VII_CJ_END_ANCHOR)  # (local)
    cj_sha = sha256_of_text(cj_block)  # (local)
    pins["sessions/permanent-results-registry.md#§VII.CJ-body"] = cj_sha

    # inv-12 W3-2 no-overlap-certificate npz
    pins["computations/investigation-12/inv12_w3_2_floquet_ordered_veil_resonance.npz"] = sha256_of(INV12_NPZ)

    # reviewer JSONs
    pins["computations/session-112/s112_viicj_stage2_axisA_connes.json"] = sha256_of(REVIEWER_A_JSON)
    pins["computations/session-112/s112_viicj_stage2_axisB_landau.json"] = sha256_of(REVIEWER_B_JSON)

    # canonical_constants.py
    can_path = SHARED_DIR / "canonical_constants.py"  # (local)
    pins["computations/_shared/canonical_constants.py"] = sha256_of(can_path)

    for k, v in sorted(pins.items()):
        print(f"  {k}: {v[:16]}...")
    print(f"  §VII.CJ body block: {len(cj_block)} chars, sha {cj_sha[:16]}...")
    return pins, len(cj_block)


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
        where pinmap_json is the canonical sorted JSON of the FULL ordered
        input-pin map (script, §VII.CJ body, inv12 npz, both reviewer JSONs,
        canonical).
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
    if data.get("theorem") != "§VII.CJ":
        raise SystemExit(f"FATAL: {path.name} theorem {data.get('theorem')!r} != §VII.CJ")
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


def echo_no_overlap_certificate() -> dict:
    """Echo the no-overlap-certificate facts from the inv-12 W3-2 npz.

    These are NOT re-derived (the reviewers verified them from first principles);
    they are echoed for the audit trail / npz output and to bind the certificate
    source into the run. HARD-asserts the certificate holds (0 overlap, |Tr M|<2)
    so a corrupt / wrong npz surfaces as a script error.
    """
    d = np.load(INV12_NPZ, allow_pickle=True)  # (local)
    A = d["A_relic"]  # (local)
    dist = d["dist_to_zone_A"]  # (local)
    nn = d["nearest_n"]  # (local)
    th = d["tongue_halfwidth_relic"]  # (local)
    tr = d["tr_relic"]  # (local)
    h_par = float(d["h_par"])  # (local)
    i_closest = int(d["i_closest"])  # (local)

    n_modes = int(A.shape[0])  # (local)
    overlap_count = int((th >= dist).sum())  # (local) modes whose stored full-width >= detuning
    max_abs_trM = float(np.abs(tr).max())  # (local)
    A_worst = float(A[i_closest])  # (local)
    nn_worst = int(nn[i_closest])  # (local)
    dist_worst = float(dist[i_closest])  # (local)
    n_modes_Agt9 = int((A > 9).sum())  # (local)
    nn_set_Agt9 = sorted(set(int(x) for x in nn[A > 9]))  # (local)
    A_min = float(A.min())  # (local)
    A_max = float(A.max())  # (local)

    # HARD-assert the certificate the §VII.CJ theorem rests on.
    if overlap_count != 0:
        raise SystemExit(f"FATAL: inv12 npz no-overlap certificate VIOLATED — {overlap_count} of {n_modes} modes overlap")
    if not (max_abs_trM < 2.0):
        raise SystemExit(f"FATAL: inv12 npz max|Tr M|={max_abs_trM} is NOT < 2 — re-pumping certificate VIOLATED")
    if nn_set_Agt9 not in ([3, 4], [3], [4]):
        raise SystemExit(f"FATAL: inv12 npz A>9 modes carry nearest_n {nn_set_Agt9}, expected subset of {{3,4}}")

    return {
        "n_modes": n_modes,
        "overlap_count": overlap_count,
        "max_abs_trM": max_abs_trM,
        "i_closest": i_closest,
        "A_worst": A_worst,
        "nn_worst": nn_worst,
        "dist_worst": dist_worst,
        "n_modes_Agt9": n_modes_Agt9,
        "nn_set_Agt9": nn_set_Agt9,
        "A_min": A_min,
        "A_max": A_max,
        "h_par": h_par,
    }


def compute() -> dict:
    """Collate the two reviewer JSONs into the composite PASS-AND verdict."""
    # Axis-A (connes) owns casimir_A_placement + joint_exponent
    a = load_clause_verdicts(REVIEWER_A_JSON, "A", AXIS_A_SINGLE_CLAUSES + [JOINT_CLAUSE])  # (local)
    # Axis-B (landau) owns exponent_and_nooverlap + joint_exponent
    b = load_clause_verdicts(REVIEWER_B_JSON, "B", AXIS_B_SINGLE_CLAUSES + [JOINT_CLAUSE])  # (local)

    # The four clause POSITIONS that enter the PASS-AND, with their owning reviewer.
    #   casimir_A_placement    -> Axis-A only
    #   exponent_and_nooverlap -> Axis-B only
    #   joint_exponent         -> JOINT: BOTH A and B must PASS independently
    clause_matrix = {  # (local)
        "casimir_A_placement@A": a["casimir_A_placement"],
        "exponent_and_nooverlap@B": b["exponent_and_nooverlap"],
        "joint_exponent@A": a[JOINT_CLAUSE],
        "joint_exponent@B": b[JOINT_CLAUSE],
    }

    all_verdicts = list(clause_matrix.values())  # (local)
    any_fail = any(v == "FAIL" for v in all_verdicts)  # (local)
    any_info = any(v == "INFO" for v in all_verdicts)  # (local)
    all_pass = all(v == "PASS" for v in all_verdicts)  # (local)

    # Composite collapse (pre-registered, plan §W2-4):
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

    # JOINT EXPONENT-n PASS-AND across both reviewers (the structural-independence
    # guarantee: BOTH NON-AUTHOR reviewers must independently PASS the EXPONENT-n
    # claim — neither having read the inv-12 W3-2 survey workshop).
    joint_exponent_pass_and = (a[JOINT_CLAUSE] == "PASS") and (b[JOINT_CLAUSE] == "PASS")  # (local)

    # Overall axis verdicts the reviewers self-reported (cross-check only).
    a_overall = json.loads(REVIEWER_A_JSON.read_text(encoding="utf-8")).get("overall_axis_verdict")  # (local)
    b_overall = json.loads(REVIEWER_B_JSON.read_text(encoding="utf-8")).get("overall_axis_verdict")  # (local)

    # Echo the no-overlap certificate (audit trail; not re-derived).
    cert = echo_no_overlap_certificate()  # (local)

    return {
        "composite": composite,
        "clause_matrix": clause_matrix,
        "axis_A": a,
        "axis_B": b,
        "joint_exponent_pass_and": joint_exponent_pass_and,
        "axis_A_overall": a_overall,
        "axis_B_overall": b_overall,
        "any_fail": any_fail,
        "any_info": any_info,
        "all_pass": all_pass,
        "certificate": cert,
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

    # 1. Log input pins (first 20 lines of stdout)
    pins, cj_len = log_input_pins()
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
    cert = result["certificate"]  # (local)

    print("=== clause-verdict matrix (per-reviewer per-clause) ===")
    print(f"  Axis-A ({REVIEWER_A_NAME}): casimir_A_placement={result['axis_A']['casimir_A_placement']}  "
          f"joint_exponent={result['axis_A'][JOINT_CLAUSE]}  "
          f"[overall={result['axis_A_overall']}]")
    print(f"  Axis-B ({REVIEWER_B_NAME}): exponent_and_nooverlap={result['axis_B']['exponent_and_nooverlap']}  "
          f"joint_exponent={result['axis_B'][JOINT_CLAUSE]}  "
          f"[overall={result['axis_B_overall']}]")
    print(f"  JOINT joint_exponent PASS-AND (A∧B): {result['joint_exponent_pass_and']}")
    print(f"  PASS-AND over {{casimir_A_placement@A, exponent_and_nooverlap@B, joint_exponent@A, joint_exponent@B}}: composite={composite}")
    print()
    print("=== no-overlap certificate (echoed from inv12_w3_2 npz; NOT re-derived) ===")
    print(f"  n_modes={cert['n_modes']}  overlap_count={cert['overlap_count']}  max|Tr M|={cert['max_abs_trM']:.8f}")
    print(f"  worst-case i_closest={cert['i_closest']}  A={cert['A_worst']:.6f}  nearest_n={cert['nn_worst']}  detuning={cert['dist_worst']:.6e}")
    print(f"  A range=[{cert['A_min']:.6f},{cert['A_max']:.6f}]  A>9 modes={cert['n_modes_Agt9']} nearest_n∈{cert['nn_set_Agt9']}  h_par={cert['h_par']:.2e}")
    print()

    # 3. Build the compact value payload string (no single-quote chars; emit_verdict
    #    wraps value='...').
    cm = result["clause_matrix"]  # (local)
    value = (
        f"composite={composite};"
        f"casimir_A_placement@A={cm['casimir_A_placement@A']};"
        f"exponent_and_nooverlap@B={cm['exponent_and_nooverlap@B']};"
        f"joint_exponent@A={cm['joint_exponent@A']};joint_exponent@B={cm['joint_exponent@B']};"
        f"joint_exponent_passAND={result['joint_exponent_pass_and']};"
        f"axisA_overall={result['axis_A_overall']};axisB_overall={result['axis_B_overall']};"
        f"no_overlap={cert['overlap_count']}of{cert['n_modes']};maxTrM={cert['max_abs_trM']:.8f};"
        f"worst_A={cert['A_worst']:.6f}@n{cert['nn_worst']}_detuning={cert['dist_worst']:.4e};"
        f"VII.BP_DEAD_4th_orthogonal_pin_cutoff-robustness_CONFIRM-not-re-gate;"
        f"x16+prefactors_DIAGNOSTIC-ONLY_NOT-registered_EXPONENT-n_convention-INDEPENDENT"
    )  # (local)

    # 4. Persist the clause-verdict matrix + certificate echo to npz
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        theorem="§VII.CJ",
        composite=composite,
        clause_keys=np.array(list(cm.keys())),
        clause_verdicts=np.array(list(cm.values())),
        axisA_reviewer=REVIEWER_A_NAME,
        axisB_reviewer=REVIEWER_B_NAME,
        axisA_casimir_A_placement=result["axis_A"]["casimir_A_placement"],
        axisA_joint_exponent=result["axis_A"][JOINT_CLAUSE],
        axisB_exponent_and_nooverlap=result["axis_B"]["exponent_and_nooverlap"],
        axisB_joint_exponent=result["axis_B"][JOINT_CLAUSE],
        joint_exponent_pass_and=result["joint_exponent_pass_and"],
        axisA_overall=result["axis_A_overall"],
        axisB_overall=result["axis_B_overall"],
        any_fail=result["any_fail"],
        any_info=result["any_info"],
        all_pass=result["all_pass"],
        excluded_authors=np.array(EXCLUDED_AUTHORS),
        # no-overlap certificate echo (from inv12_w3_2 npz; not re-derived)
        cert_n_modes=cert["n_modes"],
        cert_overlap_count=cert["overlap_count"],
        cert_max_abs_trM=cert["max_abs_trM"],
        cert_i_closest=cert["i_closest"],
        cert_A_worst=cert["A_worst"],
        cert_nn_worst=cert["nn_worst"],
        cert_dist_worst=cert["dist_worst"],
        cert_n_modes_Agt9=cert["n_modes_Agt9"],
        cert_nn_set_Agt9=np.array(cert["nn_set_Agt9"]),
        cert_A_min=cert["A_min"],
        cert_A_max=cert["A_max"],
        cert_h_par=cert["h_par"],
        cj_block_len=cj_len,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  wrote {OUT_NPZ.name}")

    # 5. Emit 4-tuple + PRINT the emit_verdict payload.
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)

    companion = (
        f"§VII.CJ Stage-2 cross-axis PASS-AND: A({REVIEWER_A_NAME})={result['axis_A_overall']} "
        f"B({REVIEWER_B_NAME})={result['axis_B_overall']}; JOINT EXPONENT-n A∧B="
        f"{result['joint_exponent_pass_and']}; composite={composite}; "
        f"no-overlap {cert['overlap_count']}-of-{cert['n_modes']} (max|Tr M|={cert['max_abs_trM']:.8f}<2); "
        f"§VII.BP DEAD CONFIRMED (4th orthogonal pin: cutoff-robustness), NOT re-gated"
    )  # (local)
    extra = [
        f"# excluded_authors={','.join(EXCLUDED_AUTHORS)} (Stage-0+Stage-1 author; Floquet/Bogoliubov/Mathieu/McLachlan math owner + inv-12 W3-2 survey author; original-author exclusion + downstream-inheritance reach)",
        "# JOINT EXPONENT-n PASS-AND'd across BOTH NON-AUTHOR reviewers (structural-independence guarantee; neither read the inv-12 W3-2 survey workshop)",
        "# x16 + ALL coefficient prefactors DIAGNOSTIC-ONLY (convention-ambiguous), NOT registered; the EXPONENT n (degree_q==n) is the convention-INDEPENDENT registered claim",
        "# mnemonic-vs-exact (math-scripts.md): bare (q_M)^{n>=3} mnemonic LOOSE at broad-band-max ((q_M)^3=1.445e-7>1e-7); prefactor-correct q^3/64=2.258e-9 load-bearing; EXPONENT unaffected",
        f"# worst-case mode i_closest={cert['i_closest']} A={cert['A_worst']:.6f} nearest_n={cert['nn_worst']}: prefactor-correct half-width q^3/64=1.628e-09 << detuning {cert['dist_worst']:.4e} (~5.4-decade margin)",
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
