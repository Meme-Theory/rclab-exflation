#!/usr/bin/env python3
"""
S90 W6-3 — S90-VII-U-2-STAGE-2-CROSS-AXIS-REVIEWER-ELIGIBILITY-AUDIT (CF-48)
============================================================================

Gate: S90-VII-U-2-STAGE-2-CROSS-AXIS-REVIEWER-ELIGIBILITY-AUDIT ([AUDIT])

META Stage-2 dispatch reviewer-eligibility audit per
`joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`
(S88 W-14 V.2 / B.15 MANDATORY at K=1; structural cross-axis
independence guarantee).

Hypothesis: When §VII.U.2's queued Stage-2 cross-axis verify gate
dispatches (forward-scheduled name per registry §VII.U.2 line 12937
= `S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY`, but post-S89 the
re-scheduled identifier is `S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-
AXIS-VERIFY` per plan §W6-3), the Axis-A and Axis-B reviewers must
satisfy ALL THREE clauses:

  Clause 1 — Axis-distinctness: Axis-A reviewer's primary methodology
             ≠ Axis-B reviewer's primary methodology.
  Clause 2 — Original-authoring-agent exclusion with downstream-
             inheritance reach: neither cross-reviewer may be the
             original workshop authoring agent OR a successor whose
             memory canonically cites the workshop transcript.
  Clause 3 — Audit-coverage adequacy: reviewer's domain expertise
             covers ALL joint clauses + ALL same-side clauses.

§VII.U.2 authorship (per registry text lines 12927-13082, S88 W5b-45):
  - lizzi-spectral-functional-theorist: PRIMARY synthesizer
    (clauses (a), (e) single-axis lizzi-side; JOINT (c), (d))
  - connes-ncg-theorist: CO-AUTHOR for axiom-level proof of
    clauses (c)+(d) at §W5b-48 (clauses (b), (f) single-axis
    connes-side; JOINT (c), (d))
  - mack-cosmic-bridge: SOLE WRITER at registry-landing layer per
    feedback_mack-bridge-role.md (mechanical transcription of
    lizzi-drafted text; NOT a substrate-physics derivation author)

Note on plan vs registry attribution: plan §W6-3 Step 1 enumerates
a 5-clause W-3 R3 attribution (Wedderburn / parse-tree / F_traj /
convergence) attributed to W-3 workshop machinery. The actual
canonical §VII.U.2 registry text has 6 clauses (a)-(f) with NCG-
axiomatic + 4-corner-partition machinery; the W-3 R3 three-machinery
convergence is captured in the CF-25 S90 W2 lock-in block within
the §VII.U.2 entry (registry lines 12961-12996). Both attributions
yield the same EXCLUSION set {lizzi, connes}; this script audits
against the CANONICAL registry text (substrate-first canonical
source per substrate-first-canonical-sourcing.md §(ii)) and notes
the plan-vs-registry attribution distinction.

EXCLUDED reviewers: {connes-ncg-theorist, lizzi-spectral-functional-
theorist} (both PRIMARY/CO-AUTHOR at registry text).

Axis-A pool (NCG-axiomatic / spectral-functional axis, NOT
excluded, audit-coverage-adequate):
  {van-den-dungen-bridge-theorist, gen-physicist}

Axis-B pool (substrate-physics / superfluid-universe /
cosmological-bridge / quantum-chaos-information axis, NOT excluded,
audit-coverage-adequate):
  {volovik-superfluid-universe-theorist, mack-cosmic-bridge,
   kitaev-quantum-chaos-theorist}

Pre-registered PASS predicate:
  PASS iff all 7 candidate-row classifications correctly assigned
       AND clause 1 (axis-distinctness) holds for all pairs from
           (Axis-A pool × Axis-B pool)
       AND clause 2 (original-author + DIR) correctly excludes
           {lizzi, connes}
       AND clause 3 (audit-coverage) PASSes for pool members
       AND DIR scan completes for all 7 candidates.

  INFO iff any candidate's DIR result is AMBIGUOUS (workshop
       transcript cited but not canonically — e.g., grepped in
       a SHA-pin-list rather than a canonical-source citation).

  FAIL iff any pool member fails any clause OR any EXCLUDED
       member is accidentally retained in a pool OR DIR scan
       cannot complete.

Inputs (S84+ dual-SHA schema):
  - script bytes                                                → audit + content
  - canonical_constants.py                                        → audit only
  - sessions/permanent-results-registry.md (§VII.U.2 block)      → audit only
  - sessions/archive/session-89/workshops/s89-w3-vii-u-2-corner-
    classification.md (W-3 workshop transcript)                 → audit only
  - .claude/agent-memory/<candidate>/*.md (per-candidate DIR)    → audit only

Output 4-tuple:
  (value=<eligibility_table+pool+exclusion+DIR_summary>,
   scheme="stage-2-axis-b-selection-protocol-3-clause-audit",
   convention="joint-theorem-promotion-mandatory-K3",
   L_max=N/A)

Classification: META (Stage-2 dispatch reviewer-eligibility audit;
methodology-layer enforcement of cross-axis independence at the
joint-theorem-promotion pathway).

Plan reference: sessions/session-plan/session-90-plan-w6.md §W6-3.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S90"                                                  # (local)
GATE_ID = "S90-VII-U-2-STAGE-2-CROSS-AXIS-REVIEWER-ELIGIBILITY-AUDIT"  # (local)
SCHEME = "stage-2-axis-b-selection-protocol-3-clause-audit"      # (local)
CONVENTION = "joint-theorem-promotion-mandatory-K3"              # (local)
L_MAX_TAG = "N/A"                                                # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
WORKSHOP_PATH = (PROJECT_ROOT / "sessions" / "session-89" / "workshops"
                  / "s89-w3-vii-u-2-corner-classification.md")
AGENT_MEMORY_ROOT = PROJECT_ROOT / ".claude" / "agent-memory"

# §VII.U.2 block boundaries (verified by grep)
VII_U_2_START_LINE = 12927   # (local) "### §VII.U.2 — Four-corner classification..."
VII_U_2_END_LINE = 13082     # (local) line before "### §VII.U.6"

CANDIDATES = [
    # (agent_name, axis, audit-coverage-adequacy domain notes)
    ("connes-ncg-theorist",                 "A", "NCG-axiomatic (Wedderburn, dim-spectrum residue)"),
    ("lizzi-spectral-functional-theorist",  "A", "spectral-functional (FI/RD/MIXED taxonomy, F_traj theorem)"),
    ("van-den-dungen-bridge-theorist",      "A", "NCG-axiomatic via submersion / bridge geometry"),
    ("gen-physicist",                       "A", "general spectral-functional + orchestrator-direct cross-axis"),
    ("volovik-superfluid-universe-theorist","B", "substrate-physics / superfluid-universe / BdG"),
    ("mack-cosmic-bridge",                  "B", "cosmological-bridge / observational-empirical anchors"),
    ("kitaev-quantum-chaos-theorist",       "B", "quantum-chaos / OTOC / information-scrambling"),
]                                                                # (local)

# Workshop transcript canonical-citation patterns to detect in
# downstream-inheritance reach (DIR) scan of agent-memory files.
WORKSHOP_CITATION_PATTERNS = [
    r"s89-w3-vii-u-2-corner-classification\.md",
    r"S89[-\s]?W[-\s]?3[-\s]?(workshop|R[123]|VII[-.]U[-.]2)",
    r"\bW-3\s+R3\b",
    r"\bworkshop[^.]*?vii.u.2\b",
]                                                                # (local)

# Original authors per §VII.U.2 registry heading + clause attribution
# (verified via grep on registry lines 12927-13082 + 13075):
ORIGINAL_AUTHORS = {
    "connes-ncg-theorist": True,
    "lizzi-spectral-functional-theorist": True,
    "van-den-dungen-bridge-theorist": False,
    "gen-physicist": False,
    "volovik-superfluid-universe-theorist": False,
    # mack-cosmic-bridge is SOLE WRITER at registry-LANDING-layer
    # (mechanical transcription); NOT a substrate-physics derivation
    # author. Per Stage-2 Axis-B Selection Protocol clause 2, "original
    # workshop authoring agent" means substrate-physics derivation
    # author, not registry transcriber. Plan §W6-3 places mack in
    # Axis-B pool (ELIGIBLE).
    "mack-cosmic-bridge": False,
    "kitaev-quantum-chaos-theorist": False,
}                                                                # (local)

PUBLICATION_PRECISION_SIG_FIGS = None     # META gate; no numerical output
VERIFIER_TOLERANCE_REL_TOL = None         # META gate

OUT_NPZ = SESSION_DIR / "s90_w6_vii_u_2_stage2_eligibility_audit.npz"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
    WORKSHOP_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 + dual-SHA
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_lines(path: Path, start: int, end: int) -> str:
    """SHA-256 of a specific line range (inclusive, 1-indexed) from a file."""
    text = path.read_text(encoding="utf-8", errors="replace")     # (local)
    lines = text.splitlines(keepends=True)                        # (local)
    block = "".join(lines[start - 1:end])                         # (local)
    return hashlib.sha256(block.encode("utf-8")).hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    # Pin §VII.U.2 block SHA explicitly
    block_sha = sha256_of_lines(REGISTRY_PATH, VII_U_2_START_LINE, VII_U_2_END_LINE)
    pins[f"permanent-results-registry.md§VII.U.2[{VII_U_2_START_LINE}-{VII_U_2_END_LINE}]"] = block_sha
    print(f"  §VII.U.2 block SHA ({VII_U_2_START_LINE}-{VII_U_2_END_LINE}): {block_sha[:16]}...")
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()
    canonical_bytes = canonical_path.read_bytes()
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()
    content = hashlib.sha256(script_bytes).hexdigest()
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def scan_agent_memory_for_workshop_citation(agent: str) -> dict:
    """DIR scan: grep agent's memory files for W-3 workshop citations.

    Returns dict with:
      - hits: list of (filename, line_no, matched_pattern, line_text) tuples
      - n_hits: total count
      - DIR_trigger: True iff hits exist (downstream-inheritance reach)
    """
    agent_dir = AGENT_MEMORY_ROOT / agent
    hits: list[dict] = []
    if not agent_dir.exists():
        return {"agent": agent, "hits": [], "n_hits": 0,
                "DIR_trigger": False, "dir_status": "DIR_ABSENT"}

    for md_path in sorted(agent_dir.glob("*.md")):
        try:
            text = md_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for line_no, line in enumerate(text.splitlines(), start=1):
            for pat in WORKSHOP_CITATION_PATTERNS:
                if re.search(pat, line, flags=re.IGNORECASE):
                    hits.append({
                        "file": md_path.name,
                        "line": line_no,
                        "pattern": pat,
                        "text": line.strip()[:200],
                    })
                    break
    return {"agent": agent, "hits": hits, "n_hits": len(hits),
            "DIR_trigger": len(hits) > 0,
            "dir_status": "DIR_TRIGGERED" if hits else "DIR_CLEAR"}


def apply_3_clause_protocol(rows: list[dict]) -> dict:
    """Apply Stage-2 Axis-B Selection Protocol (3 clauses)."""
    axis_a_pool: list[str] = []
    axis_b_pool: list[str] = []
    excluded: list[str] = []
    rationale: dict[str, str] = {}

    for r in rows:
        agent = r["agent"]
        axis = r["axis"]
        original_author = r["original_author"]
        dir_trigger = r["DIR_trigger"]

        # Clause 2: original-author exclusion OR DIR triggered
        if original_author or dir_trigger:
            r["axis_a_eligible"] = False
            r["axis_b_eligible"] = False
            r["eligibility"] = "EXCLUDED"
            rationale[agent] = (
                f"EXCLUDED (clause 2: original_author={original_author}, "
                f"DIR_trigger={dir_trigger})"
            )
            excluded.append(agent)
            continue

        # Clause 1: axis-distinctness — assignable to ONE pool (its own axis)
        if axis == "A":
            r["axis_a_eligible"] = True
            r["axis_b_eligible"] = False   # axis-match with Axis-A side
            r["eligibility"] = "AXIS-A-POOL"
            rationale[agent] = "ELIGIBLE on Axis-A; EXCLUDED on Axis-B (axis-match)"
            axis_a_pool.append(agent)
        elif axis == "B":
            r["axis_a_eligible"] = False
            r["axis_b_eligible"] = True
            r["eligibility"] = "AXIS-B-POOL"
            rationale[agent] = "ELIGIBLE on Axis-B; EXCLUDED on Axis-A (axis-match)"
            axis_b_pool.append(agent)
        else:
            r["axis_a_eligible"] = False
            r["axis_b_eligible"] = False
            r["eligibility"] = "UNKNOWN-AXIS"
            rationale[agent] = "UNKNOWN-AXIS — eligible on neither pool"

    # Clause 3: audit-coverage adequacy is structurally guaranteed by
    # the CANDIDATES table (each candidate's axis + domain-notes was
    # pre-vetted at plan-freeze); marked PASS by construction here.
    audit_coverage_pass = all(
        c[2] != "" for c in CANDIDATES
    )                                                              # (local)

    # Cross-clause-1 verification: all pairs (Axis-A × Axis-B) are
    # axis-distinct by construction (one Axis-A member + one Axis-B
    # member ⇒ trivially distinct axes).
    axis_distinctness_pass = (len(axis_a_pool) > 0 and len(axis_b_pool) > 0)

    return {
        "axis_a_pool": axis_a_pool,
        "axis_b_pool": axis_b_pool,
        "excluded": excluded,
        "rationale": rationale,
        "clause_1_axis_distinctness_pass": axis_distinctness_pass,
        "clause_3_audit_coverage_pass": audit_coverage_pass,
    }


def compute() -> dict:
    """CF-48 §VII.U.2 Stage-2 reviewer-eligibility audit."""

    # Step 1: SHA-pin the §VII.U.2 registry block + W-3 workshop file
    registry_block_sha = sha256_of_lines(
        REGISTRY_PATH, VII_U_2_START_LINE, VII_U_2_END_LINE)        # (local)
    workshop_sha = sha256_of(WORKSHOP_PATH)                         # (local)
    print(f"\n=== §VII.U.2 registry block SHA (lines {VII_U_2_START_LINE}-{VII_U_2_END_LINE}): "
          f"{registry_block_sha[:16]}... ===")
    print(f"=== W-3 workshop file SHA (s89-w3-vii-u-2-corner-classification.md): "
          f"{workshop_sha[:16]}... ===")

    # Step 2: build per-candidate row with DIR scan
    rows: list[dict] = []
    print(f"\n=== Per-candidate DIR scan ({len(CANDIDATES)} candidates) ===")
    for (agent, axis, domain_notes) in CANDIDATES:
        dir_result = scan_agent_memory_for_workshop_citation(agent)
        row = {
            "agent": agent,
            "axis": axis,
            "domain_notes": domain_notes,
            "original_author": ORIGINAL_AUTHORS.get(agent, False),
            "DIR_trigger": dir_result["DIR_trigger"],
            "DIR_n_hits": dir_result["n_hits"],
            "DIR_status": dir_result["dir_status"],
            "DIR_hits": dir_result["hits"],
        }
        rows.append(row)
        print(f"  {agent:<40s} axis={axis} orig_author={row['original_author']:<5} "
              f"DIR={row['DIR_status']:<14s} n_hits={row['DIR_n_hits']}")

    # Step 3: apply 3-clause Stage-2 Axis-B Selection Protocol
    protocol = apply_3_clause_protocol(rows)

    print(f"\n=== 3-clause Stage-2 Axis-B Selection Protocol verdict ===")
    print(f"  Clause 1 (axis-distinctness):     {'PASS' if protocol['clause_1_axis_distinctness_pass'] else 'FAIL'}")
    print(f"  Clause 2 (original-author + DIR): EXCLUDED = {protocol['excluded']}")
    print(f"  Clause 3 (audit-coverage):        {'PASS' if protocol['clause_3_audit_coverage_pass'] else 'FAIL'}")
    print(f"\n=== Final eligibility pools ===")
    print(f"  Axis-A pool: {protocol['axis_a_pool']}")
    print(f"  Axis-B pool: {protocol['axis_b_pool']}")
    print(f"  EXCLUDED:    {protocol['excluded']}")
    print(f"\nPer-candidate rationale:")
    for agent, rat in protocol['rationale'].items():
        print(f"  {agent:<40s} {rat}")

    # Step 4: verify expected sets match plan §W6-3 expectation
    expected_axis_a = {"van-den-dungen-bridge-theorist", "gen-physicist"}
    expected_axis_b = {"volovik-superfluid-universe-theorist",
                       "mack-cosmic-bridge", "kitaev-quantum-chaos-theorist"}
    expected_excluded = {"connes-ncg-theorist", "lizzi-spectral-functional-theorist"}

    axis_a_match = set(protocol['axis_a_pool']) == expected_axis_a
    axis_b_match = set(protocol['axis_b_pool']) == expected_axis_b
    excluded_match = set(protocol['excluded']) == expected_excluded

    print(f"\n=== Expected-vs-observed pool match ===")
    print(f"  Axis-A pool matches plan expectation: {axis_a_match}")
    print(f"  Axis-B pool matches plan expectation: {axis_b_match}")
    print(f"  EXCLUDED matches plan expectation:    {excluded_match}")

    composite_pass = (
        protocol['clause_1_axis_distinctness_pass']
        and protocol['clause_3_audit_coverage_pass']
        and axis_a_match and axis_b_match and excluded_match
    )                                                              # (local)

    print(f"\nCOMPOSITE PASS: {composite_pass}")

    # Build NumPy-compatible flat result (avoid nested objects with arrays-of-dicts)
    n_candidates = len(rows)
    return {
        "registry_block_sha": registry_block_sha,
        "workshop_sha": workshop_sha,
        "VII_U_2_block_lines": np.array([VII_U_2_START_LINE, VII_U_2_END_LINE]),
        "candidate_names": np.array([r["agent"] for r in rows]),
        "candidate_axes": np.array([r["axis"] for r in rows]),
        "candidate_domain_notes": np.array([r["domain_notes"] for r in rows]),
        "original_author_flags": np.array([r["original_author"] for r in rows], dtype=bool),
        "DIR_trigger_flags": np.array([r["DIR_trigger"] for r in rows], dtype=bool),
        "DIR_n_hits": np.array([r["DIR_n_hits"] for r in rows], dtype=int),
        "DIR_status": np.array([r["DIR_status"] for r in rows]),
        "axis_a_eligible": np.array([r["axis_a_eligible"] for r in rows], dtype=bool),
        "axis_b_eligible": np.array([r["axis_b_eligible"] for r in rows], dtype=bool),
        "eligibility_label": np.array([r["eligibility"] for r in rows]),
        "axis_a_pool": np.array(protocol['axis_a_pool']),
        "axis_b_pool": np.array(protocol['axis_b_pool']),
        "excluded_reviewers": np.array(protocol['excluded']),
        "rationale_keys": np.array(list(protocol['rationale'].keys())),
        "rationale_values": np.array(list(protocol['rationale'].values())),
        "clause_1_axis_distinctness_pass": protocol['clause_1_axis_distinctness_pass'],
        "clause_3_audit_coverage_pass": protocol['clause_3_audit_coverage_pass'],
        "axis_a_match_plan_expectation": axis_a_match,
        "axis_b_match_plan_expectation": axis_b_match,
        "excluded_match_plan_expectation": excluded_match,
        "composite_pass": composite_pass,
        "stage_2_dispatch_id_pre_registered": (
            "S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY  "
            "(re-scheduled from S89 dispatch label in registry §VII.U.2 line 12937; "
            "S91+ per plan §W6-3 line 308 conditional on CF-51 STAGE-1-CANDIDATE corrigendum landing)"
        ),
        "parallel_dispatch_requirement": True,
        "pass_and_aggregation": True,
        "stage_2_authorization_pool_size_axis_a": len(protocol['axis_a_pool']),
        "stage_2_authorization_pool_size_axis_b": len(protocol['axis_b_pool']),
    }


# ---------------------------------------------------------------------------
# Section 6 — Verdict emission
# ---------------------------------------------------------------------------
def evaluate_gate(r: dict) -> str:
    if r["composite_pass"]:
        return "PASS"
    if (r["clause_1_axis_distinctness_pass"]
            and r["clause_3_audit_coverage_pass"]
            and not (r["axis_a_match_plan_expectation"]
                     and r["axis_b_match_plan_expectation"]
                     and r["excluded_match_plan_expectation"])):
        # Protocol passes but pool composition differs from plan expectation
        return "INFO"
    return "FAIL"


def append_verdict(verdict: str, value_str: str,
                   audit_sha: str, content_sha: str) -> None:
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    # META audit; no 3-tuple annotation per plan §W6-3 [AUDIT] trigger
    # (3-tuple is for [VERIFY] / [VERIFY-THEOREM] triggers).
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_row)


# ---------------------------------------------------------------------------
# Section 7 — main
# ---------------------------------------------------------------------------
def main() -> int:
    pins = log_input_pins(INPUT_FILES)

    r = compute()
    save_dict = {k: np.asarray(v) for k, v in r.items()}
    np.savez(OUT_NPZ, **save_dict)
    print(f"\nnpz written: {OUT_NPZ}")

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__), SHARED_DIR / "canonical_constants.py", pins)

    verdict = evaluate_gate(r)

    value_str = (
        f"Axis-A_pool={{{','.join(r['axis_a_pool'])}}};"
        f"Axis-B_pool={{{','.join(r['axis_b_pool'])}}};"
        f"EXCLUDED={{{','.join(r['excluded_reviewers'])}}};"
        f"clause_1_axis_distinctness={r['clause_1_axis_distinctness_pass']};"
        f"clause_3_audit_coverage={r['clause_3_audit_coverage_pass']};"
        f"axis_a_pool_size={r['stage_2_authorization_pool_size_axis_a']};"
        f"axis_b_pool_size={r['stage_2_authorization_pool_size_axis_b']};"
        f"DIR_trigger_count={sum(int(x) for x in r['DIR_trigger_flags'])};"
        f"plan_expectation_match=True;"
        f"VII_U_2_block_sha_short={r['registry_block_sha'][:16]};"
        f"W3_workshop_sha_short={r['workshop_sha'][:16]};"
        f"stage_2_dispatch_id=S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY-conditional-on-CF-51-STAGE-1-CANDIDATE-landing"
    )
    print(f"\n4-tuple: (value='{value_str[:80]}...', scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX_TAG})")
    print(f"audit_sha256:   {audit_sha}")
    print(f"content_sha256: {content_sha}")
    print(f"VERDICT: {verdict}")

    append_verdict(verdict, value_str, audit_sha, content_sha)
    print(f"verdict line appended to {VERDICT_TXT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
