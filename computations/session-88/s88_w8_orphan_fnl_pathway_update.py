#!/usr/bin/env python3
"""
S88 W8-97 — S88-CF-28-ORPHAN-FNL-PATHWAY-REGISTRY-UPDATE
========================================================

Gate: S88-CF-28-ORPHAN-FNL-PATHWAY-REGISTRY-UPDATE ([AUDIT] / METHODOLOGY)

Pre-registered threshold (plan §W8-97 line 396):
  PASS iff (a) all "Row #9" instances renamed to "Row #9a" in
  `sessions/framework/registry/f-nl-folded-pathway-registry.md`
  AND (b) cross-reference note present
  "Row #9a indicates orphan-pathway sub-row landing per S88 W8-97 (S87 W14-4 follow-up)"
  AND (c) allowlist row appended to `.claude/rules/methodology-wave-allowlist.md`.
  FAIL otherwise. METHODOLOGY-class artifact-existence verdict.

Inputs (SHA-256 dual-pinned at runtime):
  - sessions/framework/registry/f-nl-folded-pathway-registry.md (PRE-EDIT state captured)
  - sessions/framework/registry/falsifier-master-inventory.md (cross-reference target)
  - .claude/rules/methodology-wave-allowlist.md (allowlist target)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<PASS/FAIL composite>, scheme=METHODOLOGY-registry-row-rename,
   convention=Row-9-to-Row-9a-orphan-pathway, L_max=N/A)

Classification: NON-PHONONIC (METHODOLOGY-class registry hygiene; the
substrate-physics observable f_NL_folded itself is PHONONIC, but this gate's
output is artifact-existence over a markdown registry file).

METHODOLOGY
-----------
The f-nl-folded-pathway-registry.md was created at S86 W13 P10 with
references to "Row #9" as the bundled master-inventory row label. At
S87 W4-* the master inventory split Row #9 into Row #9a (laboratory-IN
side: 3-pathway projection of CMB / 21-cm bispectrum) + Row #9b
(substrate-IS side: phi_3 cocycle in HC^3(A_K)). The pathway registry
projects the LAB-IN side only (Row #9a). This script renames the
remaining "Row #9" → "Row #9a" verbatim, adds a cross-reference note
clarifying the orphan-pathway sub-row landing per S88 W8-97 (S87 W14-4
follow-up), and updates the falsifier-master-inventory cross-link
target on the pathway-registry side.

Cross-link to falsifier-master-inventory.md: per the spawn-prompt
"small/obvious" criterion — the cross-link is one-directional from
pathway-registry → master-inventory ("this registry projects Row #9a
in falsifier-master-inventory.md"). The master-inventory side is
ALREADY consistent (rows #9a, #9b, #9a-S, #9b-F all landed at S86
W-4 + S87 W4 sequence). No edit to the master-inventory file is
required; the gen-physicist sole-write boundary on this gate is
preserved per `feedback_mack-bridge-role.md`.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local intermediate tagged `# (local)`
- SHA-256 of all input files logged
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Verdict appended atomic-only via `with open("a")` per agent-standards.md
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path

_SCRIPT_PATH = _Path(__file__).resolve()
_SHARED = _SCRIPT_PATH.parent.parent / "_shared"
_sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = _SCRIPT_PATH.parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S88"  # (local)
GATE_ID = "S88-CF-28-ORPHAN-FNL-PATHWAY-REGISTRY-UPDATE"  # (local)
SCHEME = "METHODOLOGY-registry-row-rename"  # (local)
CONVENTION = "Row-9-to-Row-9a-orphan-pathway"  # (local)
L_MAX = "N/A"  # (local)

# Targets
PATHWAY_REGISTRY = (
    PROJECT_ROOT / "sessions" / "framework" / "registry" / "f-nl-folded-pathway-registry.md"
)  # (local)
MASTER_INVENTORY = (
    PROJECT_ROOT / "sessions" / "framework" / "registry" / "falsifier-master-inventory.md"
)  # (local)
ALLOWLIST = (
    PROJECT_ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
)  # (local)

OUT_JSON = SESSION_DIR / "s88_w8_orphan_fnl_pathway_update.json"
VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    PATHWAY_REGISTRY,
    MASTER_INVENTORY,
    ALLOWLIST,
]

CROSS_REF_NOTE = (
    "Row #9a indicates orphan-pathway sub-row landing per S88 W8-97 "
    "(S87 W14-4 follow-up)"
)  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA helpers (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of_bytes(b: bytes) -> str:
    h = hashlib.sha256()  # (local)
    h.update(b)
    return h.hexdigest()


def sha256_of(path: _Path) -> str:
    try:
        return sha256_of_bytes(path.read_bytes())
    except OSError:
        return ""


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: _Path, canonical_path: _Path, pins: dict):
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute (the registry edit + verification)
# ---------------------------------------------------------------------------

def edit_pathway_registry(pre_text: str) -> tuple[str, dict]:
    """Apply the rename + cross-reference-note insertion.

    Returns (post_text, edit_log) where edit_log records every change.
    """
    edit_log = {  # (local)
        "row9_count_pre": pre_text.count("Row #9"),
        "row9a_count_pre": pre_text.count("Row #9a"),
        "rename_locations": [],
        "cross_ref_inserted": False,
    }

    # Identify each line with bare "Row #9" (not already #9a / #9b / #9a-S / #9b-F)
    # The two known instances at lines 5 and 66 both write the bare "Row #9"
    # form; the rename is verbatim "Row #9" -> "Row #9a".  Note that "Row #9a"
    # already contains "Row #9", so a naive replace_all would also replace the
    # "Row #9a" prefix sub-string and break the file.  Use a regex with a
    # negative lookahead to match "Row #9" NOT followed by [a-zA-Z0-9].
    import re as _re  # (local)
    pattern = _re.compile(r"Row #9(?![a-zA-Z0-9])")  # (local)

    # Record the line indices for the JSON log
    for i, line in enumerate(pre_text.splitlines(), start=1):
        if pattern.search(line):
            edit_log["rename_locations"].append({"line": i, "text_pre": line})

    post_text = pattern.sub("Row #9a", pre_text)  # (local)

    # Verify: every previously-bare "Row #9" is now "Row #9a"
    bare_remaining = pattern.findall(post_text)  # (local)
    edit_log["bare_row9_remaining_post"] = len(bare_remaining)

    # Cross-reference note insertion: append a new sub-section at the bottom
    # before the trailing "End of registry." line.  The note explains the
    # orphan-pathway sub-row landing per S88 W8-97 (S87 W14-4 follow-up).
    cross_ref_block = (
        "\n## Orphan-Pathway Sub-Row Landing (S88 W8-97)\n\n"
        f"{CROSS_REF_NOTE}.\n\n"
        "Context: at S87 W4-* the master falsifier inventory split the "
        "previously-bundled Row #9-pre ('1 observable, 3 pathway projections') "
        "into laboratory-IN Row #9a (3-pathway projection of the CMB / 21-cm "
        "bispectrum, projected from substrate-IS phi_3 cocycle under the HKR "
        "boundary map) AND substrate-IS Row #9b (phi_3 in HC^3(A_K), "
        "rank-3 Hochschild cocycle / 3-pt-connected vertex; CF-25 STAGE-1-CANDIDATE "
        "Channel-3 anchor). This pathway registry projects the LAB-IN side "
        "ONLY (Row #9a). For substrate-IS Row #9b provenance, consult "
        "`falsifier-master-inventory.md` Row #9b cell + Row #9b-F sub-row + "
        "Row #9b.audit. Per `cross-pillar-bridge-anatomy.md` 5-anatomy + "
        "3-level ladder, this registry's three pathway entries (S82-GGE-equilateral, "
        "S67-GGE-folded, W9-3-analytic-template-folded) are the laboratory-IN "
        "Element 2 OE-form components ∫ d k Tr(...) projected from the "
        "substrate-IS phi_3 cocycle Element 1 Hochschild pairing.\n\n"
        "Cross-link to `falsifier-master-inventory.md`: this registry "
        "projects Row #9a (laboratory-IN side); see also Row #9a-S sub-row "
        "(co-coordinates of pathways B + C on the shared N_pair_eff=59.8 "
        "1-D sub-manifold) and Row #9a.audit (full-64-hex per-pathway pins "
        "preserved verbatim from W14-4).\n\n"
        "Provenance: S88 W8-97 (`S88-CF-28-ORPHAN-FNL-PATHWAY-REGISTRY-UPDATE`); "
        "method per plan `sessions/session-plan/session-88-plan-w8.md` §W8-97; "
        "executor gen-physicist sole writer per `feedback_mack-bridge-role.md` "
        "(falsifier-master-inventory.md untouched on this gate; mack-cosmic-bridge "
        "remains sole writer of that file).\n"
    )

    if "Orphan-Pathway Sub-Row Landing" not in post_text:
        # Insert before the trailing "End of registry." marker if present;
        # else append.
        anchor = "---\n\nEnd of registry."  # (local)
        if anchor in post_text:
            post_text = post_text.replace(
                anchor, cross_ref_block + "\n---\n\nEnd of registry."
            )
        else:
            post_text = post_text.rstrip() + "\n" + cross_ref_block
        edit_log["cross_ref_inserted"] = True

    edit_log["row9_count_post_bare"] = len(
        pattern.findall(post_text)
    )
    edit_log["row9a_count_post"] = post_text.count("Row #9a")
    edit_log["cross_ref_note_present"] = CROSS_REF_NOTE in post_text

    return post_text, edit_log


def append_allowlist_row(
    pre_text: str, gate_id_short: str, gate_id_full: str, audit_sha: str
) -> tuple[str, dict]:
    """Append the W8-97 row to the methodology-wave-allowlist.md table.

    The allowlist is append-only (per the rule's edit discipline). The row
    schema is `gate_id | session | rationale | sha256_of_plan_block`.
    """
    log = {"already_present": False, "appended": False}  # (local)
    if gate_id_full in pre_text:
        log["already_present"] = True
        return pre_text, log

    rationale = (
        f"{gate_id_full} (rename 'Row #9' → 'Row #9a' verbatim across "
        "f-nl-folded-pathway-registry.md citations + cross-reference note "
        "insertion per S87 W14-4 follow-up; orphan-pathway sub-row landing; "
        "M1-M4 conjunction satisfied [M1 artifact-existence on registry "
        "rename + note insertion; M2 Edit-only on registry markdown + "
        "allowlist markdown; M3 verbatim from S87 W4 master-inventory split + "
        "S87 W14-4 follow-up; M4 allowlist append herewith]; gen-physicist "
        "sole writer per `feedback_mack-bridge-role.md` (falsifier-master-inventory.md "
        "untouched); orchestrator-direct-write per `wave-classification.md` "
        "§\"Dispatch consequences\")"
    )  # (local)

    new_row = (
        f"| {gate_id_short} | S88 | {rationale} | {audit_sha} |\n"
    )  # (local)

    # Append at end (the file's tail is just a series of pipe-rows; new
    # MANDATORY rows go at the bottom of the table per its append-only rule).
    post_text = pre_text.rstrip() + "\n" + new_row  # (local)
    log["appended"] = True
    log["row_text"] = new_row
    return post_text, log


def atomic_write(path: _Path, text: str) -> None:
    """Write atomically via temp + replace; preserves Windows compatibility."""
    tmp = path.with_suffix(path.suffix + ".tmp")  # (local)
    with tmp.open("w", encoding="utf-8", newline="") as fp:
        fp.write(text)
    tmp.replace(path)


def evaluate_gate(edit_log: dict, allowlist_log: dict) -> str:
    """PASS iff (a) all bare 'Row #9' renamed AND (b) cross-ref note present
    AND (c) allowlist row appended (or already present).
    """
    cond_a = edit_log["row9_count_post_bare"] == 0  # (local)
    cond_b = edit_log["cross_ref_note_present"]  # (local)
    cond_c = allowlist_log["appended"] or allowlist_log["already_present"]  # (local)
    if cond_a and cond_b and cond_c:
        return "PASS"
    return "FAIL"


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (
        f"(value={value!r}, scheme={scheme}, "
        f"convention={convention}, L_max={L_max})"
    )


def append_verdict(
    verdict: str,
    value: str,
    audit_sha: str,
    content_sha: str,
) -> tuple[str, str]:
    """Atomic append of canonical line + dual-SHA companion row.

    METHODOLOGY-class wave per wave-classification.md §"Dual-SHA closure":
    audit_sha256 over input-pin map (registry-file SHAs + canonical_constants);
    content_sha256 over script bytes only.
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+_v2\n"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"METHODOLOGY-class wave-classification.md §M4; "
        f"allowlist row at .claude/rules/methodology-wave-allowlist.md\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_line)
    return canonical_line, companion_line


# ---------------------------------------------------------------------------
# Section 6 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Load inputs (PRE-EDIT capture)
    pathway_pre = PATHWAY_REGISTRY.read_text(encoding="utf-8")  # (local)
    allowlist_pre = ALLOWLIST.read_text(encoding="utf-8")  # (local)

    pathway_pre_sha = sha256_of_bytes(pathway_pre.encode("utf-8"))  # (local)
    allowlist_pre_sha = sha256_of_bytes(allowlist_pre.encode("utf-8"))  # (local)

    # 2. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 3. Compute dual SHAs
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(_SCRIPT_PATH, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 4. Apply pathway-registry edit (rename + cross-ref note)
    pathway_post, edit_log = edit_pathway_registry(pathway_pre)
    pathway_post_sha = sha256_of_bytes(pathway_post.encode("utf-8"))  # (local)

    print(f"=== pathway-registry edit ===")
    print(f"  bare 'Row #9' instances pre  : {edit_log['row9_count_pre']}")
    print(f"  'Row #9a' instances pre      : {edit_log['row9a_count_pre']}")
    print(f"  rename locations             : {len(edit_log['rename_locations'])}")
    for loc in edit_log["rename_locations"]:
        print(f"    line {loc['line']}: {loc['text_pre'][:80]}...")
    print(f"  bare 'Row #9' remaining post : {edit_log['row9_count_post_bare']}")
    print(f"  'Row #9a' instances post     : {edit_log['row9a_count_post']}")
    print(f"  cross-ref note inserted      : {edit_log['cross_ref_inserted']}")
    print(f"  cross-ref note present       : {edit_log['cross_ref_note_present']}")
    print()

    # Write the pathway-registry edit
    atomic_write(PATHWAY_REGISTRY, pathway_post)

    # 5. Append allowlist row (append-only per rule's edit discipline)
    allowlist_post, allowlist_log = append_allowlist_row(
        allowlist_pre, "W8-97", GATE_ID, audit_sha
    )
    allowlist_post_sha = sha256_of_bytes(allowlist_post.encode("utf-8"))  # (local)
    print(f"=== allowlist edit ===")
    print(f"  already present : {allowlist_log['already_present']}")
    print(f"  appended        : {allowlist_log['appended']}")
    print()
    if allowlist_log["appended"]:
        atomic_write(ALLOWLIST, allowlist_post)

    # 6. Evaluate gate
    verdict = evaluate_gate(edit_log, allowlist_log)

    # Compose the verdict-line value field
    value_field = (
        f"row9_renamed={edit_log['row9_count_pre']}"
        f"_row9a_post={edit_log['row9a_count_post']}"
        f"_crossref={edit_log['cross_ref_note_present']}"
        f"_allowlist={'appended' if allowlist_log['appended'] else 'already_present' if allowlist_log['already_present'] else 'MISSING'}"
    )  # (local)

    # 7. Emit 4-tuple
    tag = emit_4tuple(value_field, SCHEME, CONVENTION, L_MAX)
    print(tag)

    # 8. Append verdict (atomic, dual-SHA)
    canonical_line, companion_line = append_verdict(
        verdict, value_field, audit_sha, content_sha
    )
    print()
    print("=== verdict appended ===")
    print(canonical_line.rstrip())
    print(companion_line.rstrip())

    # 9. Write JSON sidecar (before/after SHAs of registry file +
    #    audit log of edits)
    sidecar = {
        "gate_id": GATE_ID,
        "wp_id": "W8-97",
        "session": SESSION,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "verdict": verdict,
        "value": value_field,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "input_pins": pins,
        "closure_hash": closure,
        "pathway_registry": {
            "path": str(PATHWAY_REGISTRY.relative_to(PROJECT_ROOT)).replace("\\", "/"),
            "pre_sha256": pathway_pre_sha,
            "post_sha256": pathway_post_sha,
            "edit_log": edit_log,
        },
        "allowlist": {
            "path": str(ALLOWLIST.relative_to(PROJECT_ROOT)).replace("\\", "/"),
            "pre_sha256": allowlist_pre_sha,
            "post_sha256": allowlist_post_sha,
            "log": allowlist_log,
        },
        "falsifier_master_inventory_crosslink_disposition": {
            "edit_required": False,
            "rationale": (
                "master-inventory ALREADY contains the post-CF-28 split "
                "(Row #9a, #9b, #9a-S, #9b-F at lines 261, 424-455). "
                "gen-physicist sole writer on f-nl-folded-pathway-registry.md "
                "(this gate); mack-cosmic-bridge sole writer on "
                "falsifier-master-inventory.md per feedback_mack-bridge-role.md. "
                "The cross-link is one-directional from pathway-registry → "
                "master-inventory ('this registry projects Row #9a'); "
                "the cross-ref note inserted at the pathway-registry tail "
                "carries this directional pointer without requiring a "
                "master-inventory edit."
            ),
            "carry_forward_flag": False,
        },
        "wall_seconds": time.time() - t0,
    }
    OUT_JSON.write_text(json.dumps(sidecar, indent=2), encoding="utf-8")
    print(f"\n=== sidecar written: {OUT_JSON.name} ===")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # exit 0 regardless of verdict per math-scripts.md §"Exit Codes"


if __name__ == "__main__":
    _sys.exit(main())
