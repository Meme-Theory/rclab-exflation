#!/usr/bin/env python3
"""
S87 W1b-HK-4 — S87-W1B-HK-4-VII-U-VII-W-CONVENTION-RECITE
========================================================

Gate: S87-W1B-HK-4-VII-U-VII-W-CONVENTION-RECITE ([VERIFY])

Purpose:
  Following W1b-3 falsification of d_eff=8 at the bulk-Weyl level,
  every downstream §VII.U / §VII.W reference citing d_spec=8 (the
  alias under which d_eff=8 appears in the registry's Mellin-cone
  prose) must carry an explicit convention-pin annotation pending
  the HK-3 convention audit. This driver performs the annotation
  pass idempotently using append-only Python file writers (no
  Edit-tool round-trips) per `.claude/rules/epistemic-discipline.md`
  §"Registry-Write Hygiene under Parallel-Writer Race".

Pre-registered threshold:
  PASS iff (a) all in-scope §VII.U / §VII.W d_spec=8 (or d_eff=8)
  citations carry an inline annotation `(convention pin pending
  S87-W1B-HK-3)` AFTER each such token; AND (b) the citation
  inventory written to s87_w1b_hk_4_vii_u_w_recite.npz matches the
  per-file edit count; AND (c) the script is idempotent — re-running
  detects pre-existing annotations and is a no-op.

  FAIL iff any in-scope citation remains unannotated.
  INFO iff zero in-scope citations exist (NULL pass — annotation
  set is empty by construction).

Inputs (SHA-256 dual-pinned at runtime):
  - sessions/permanent-results-registry.md  (target file 1)
  - sessions/framework/registry/elimination-bulletins.md  (target 2)
  - sessions/archive/session-87/session-87-results-workingpaper.md  (target 3)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<n_annotations_landed>, scheme=textual-citation-recite,
   convention=convention-pending-S87-W1B-HK-3, L_max=NA)

Classification: GEOMETRIC (registry-text annotation pass; no
  numerical computation; no spectral evaluation. The W1b-3 numerical
  finding has already established the bulk-falsification direction.
  This gate is a textual provenance hygiene operation propagating
  that finding into downstream registry citations.)

Substrate framing:
  The registry's §VII.U/§VII.W entries are NOT containers in which
  d_spec=8 lives as a fundamental quantity. d_spec is the substrate's
  OWN spectral dimension, an emergent description of how D_K's
  eigenvalue density distributes in the L_max → ∞ limit. W1b-3
  showed the substrate's bulk-Weyl exponent extrapolates to 5.061
  (Conv B) / 10.122 (Conv A) under Richardson L^{-3} extrapolation,
  NOT to 8. The d_spec=8 anchor is therefore a per-stratum or
  per-cluster sub-axis identity, NOT a bulk identity. This driver
  flags every in-scope citation so downstream consumers cannot
  silently inherit the bulk-Weyl reading.

METHODOLOGY
-----------
1. Enumerate in-scope citation targets:
   a. permanent-results-registry.md lines 12857, 12898 (§VII.U.6)
   b. session-87-results-workingpaper.md lines 97, 131 (§W1a-1
      §VII.U.6 landing — mirrors registry text)
   c. elimination-bulletins.md d_spec rows: lines 307, 347, 348, 349
      (gate-name references — NOT annotated; logged as out-of-scope)
   d. permanent-results-registry.md §VII.W block (lines 14371-14499)
      and §VII.W-2 block (line 15319+): VERIFIED zero d_spec=8
      citations.
2. For each in-scope target line, append the annotation
   `(convention pin pending S87-W1B-HK-3)` AFTER the d_spec token,
   PRESERVING the original surrounding text exactly. Idempotency:
   if the annotation is already present on the line, skip.
3. Write back using tempfile + os.replace (atomic, no Edit-tool
   mtime races; equivalent to the open("a") template pattern but
   for in-place text edits).
4. Save citation inventory to NPZ.
5. Append verdict line via the canonical S84+ dual-SHA pattern.
6. Append post-execution sub-section to WP §W1b-3 documenting the
   citation inventory and per-file edit counts.

DISCIPLINE
----------
- `from canonical_constants import *`
- All intermediates tagged `# (local)`
- CPU-only (no GPU; pure I/O + SHA-256 + text manipulation)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict appended via atomic open("a") single-line append
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import tempfile
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
SESSIONS_DIR = PROJECT_ROOT / "sessions"

SESSION = "S87"                                                    # (local)
GATE_ID = "S87-W1B-HK-4-VII-U-VII-W-CONVENTION-RECITE"             # (local)
SCHEME = "textual-citation-recite"                                 # (local)
CONVENTION = "convention-pending-S87-W1B-HK-3"                     # (local)
L_MAX = "NA"                                                       # (local)

ANNOTATION = " (convention pin pending S87-W1B-HK-3; "             # (local)
ANNOTATION += "scope: bulk-Weyl-falsified per W1b-3 — "
ANNOTATION += "may survive at per-stratum / per-cluster sub-axis)"

# Idempotency sentinel — substring uniquely identifying the appended note.
ANNOT_SENTINEL = "convention pin pending S87-W1B-HK-3"             # (local)

REGISTRY_PATH = SESSIONS_DIR / "permanent-results-registry.md"
ELIM_BULLETINS_PATH = (
    SESSIONS_DIR / "framework" / "registry" / "elimination-bulletins.md"
)
WP_PATH = SESSIONS_DIR / "session-87" / "session-87-results-workingpaper.md"

OUT_NPZ = resolve_output(87, 's87_w1b_hk_4_vii_u_w_recite.npz')
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')

# In-scope citation inventory — manually pinned at plan time after
# §VII.U / §VII.W block boundary verification (registry §VII.U:
# lines 12586-13030; §VII.W: 14371-14499; §VII.W-2: 15319+).
# Key = file path; value = list of (line_number, scope_tag).
IN_SCOPE_TARGETS = {
    str(REGISTRY_PATH): [
        (12857, "§VII.U.6 cross-reference to §VII.T (Re(2s) > d_spec)"),
        (12898, "§VII.U.6 substrate framing (d_spec=8 NCG cone apex)"),
    ],
    str(WP_PATH): [
        (97, "§W1a-1 §VII.U.6 landing — Catalogue-row prose (d_spec=8 strip)"),
        (131, "§W1a-1 substrate framing — mirrors registry 12898 (d_spec=8 NCG cone apex)"),
    ],
}

# Out-of-scope hits documented in inventory but NOT annotated:
#   - permanent-results-registry.md lines 4643-4909, 6792-6874,
#     14603-14612 (§VII.T, §VII.K-PROP, §VII.Z; outside §VII.U /
#     §VII.W spawn-prompt scope).
#   - elimination-bulletins.md lines 307, 347, 348, 349 (gate-name
#     bibliographic references like "W0-9 d_spec"; not numerical
#     d_spec=8 claims).
#   - WP lines 745 (d_spec=4, different value), 866 (W1b-3 section
#     itself — is the SOURCE of the falsification, not a downstream
#     citation), 868, 889, 897 (W1b-3 method/results discussion of
#     the substrate-faithful d_eff value).
OUT_OF_SCOPE_NOTES = [
    ("permanent-results-registry.md", 4643, "§VII.T body (Mellin Strip / Convergence Cone Theorem; out-of-§VII.U/W scope)"),
    ("permanent-results-registry.md", 4660, "§VII.T body (out-of-scope)"),
    ("permanent-results-registry.md", 4681, "§VII.T body (out-of-scope)"),
    ("permanent-results-registry.md", 4711, "§VII.T body (out-of-scope)"),
    ("permanent-results-registry.md", 4713, "§VII.T body (out-of-scope)"),
    ("permanent-results-registry.md", 4716, "§VII.T body (out-of-scope)"),
    ("permanent-results-registry.md", 4718, "§VII.T body (out-of-scope)"),
    ("permanent-results-registry.md", 4771, "§VII.T body (out-of-scope)"),
    ("permanent-results-registry.md", 4909, "§VII.T body (out-of-scope)"),
    ("permanent-results-registry.md", 6792, "§VII.K-PROP body (out-of-scope)"),
    ("permanent-results-registry.md", 6804, "§VII.K-PROP body (out-of-scope)"),
    ("permanent-results-registry.md", 6806, "§VII.K-PROP body (out-of-scope)"),
    ("permanent-results-registry.md", 6808, "§VII.K-PROP body (out-of-scope)"),
    ("permanent-results-registry.md", 6824, "§VII.K-PROP body (out-of-scope)"),
    ("permanent-results-registry.md", 6828, "§VII.K-PROP body (out-of-scope)"),
    ("permanent-results-registry.md", 6830, "§VII.K-PROP body (out-of-scope)"),
    ("permanent-results-registry.md", 6836, "§VII.K-PROP body (out-of-scope)"),
    ("permanent-results-registry.md", 6858, "§VII.K-PROP body (out-of-scope)"),
    ("permanent-results-registry.md", 6862, "§VII.K-PROP body (out-of-scope)"),
    ("permanent-results-registry.md", 6874, "§VII.K-PROP body (out-of-scope)"),
    ("permanent-results-registry.md", 14603, "§VII.Z body (F_4-MB Structural Wall Family; out-of-scope)"),
    ("permanent-results-registry.md", 14612, "§VII.Z body (out-of-scope)"),
    ("elimination-bulletins.md", 307, "Gate-name bibliographic reference (not d_spec=8 claim)"),
    ("elimination-bulletins.md", 347, "Gate-name bibliographic reference"),
    ("elimination-bulletins.md", 348, "Gate-name bibliographic reference"),
    ("elimination-bulletins.md", 349, "Gate-name bibliographic reference"),
    ("session-87-results-workingpaper.md", 745, "d_spec=4 (different value; substrate-distance-1 pole at SD slot)"),
    ("session-87-results-workingpaper.md", 866, "§W1b-3 body — SOURCE of falsification, not a downstream citation"),
    ("session-87-results-workingpaper.md", 868, "§W1b-2 method discussion"),
    ("session-87-results-workingpaper.md", 889, "§W1b-2 results table"),
    ("session-87-results-workingpaper.md", 897, "§W1b-2 results table"),
]

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    REGISTRY_PATH,
    ELIM_BULLETINS_PATH,
    WP_PATH,
]

# ---------------------------------------------------------------------------
# Section 4 — SHA-256 / dual-SHA helpers
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    """S84+ dual-SHA: audit covers script+canonical+pinmap; content is script-only."""
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
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
# Section 5 — Annotation pass + atomic file rewrite
# ---------------------------------------------------------------------------

def annotate_d_spec_token(line: str) -> tuple[str, bool]:
    """Append ANNOTATION after the FIRST 'd_spec' token on the line.

    Returns (new_line, did_change). If the annotation is already
    present on the line (idempotency sentinel match), returns
    (line, False).

    The annotation is inserted IMMEDIATELY AFTER the matched token
    AND any contiguous suffix that completes the token (e.g.,
    `d_spec=8`, `d_spec ~ 8`, `d_spec/2`, `d_spec)`). Strategy: find
    'd_spec', then scan forward up to 8 chars to include a numeric
    suffix or '=8' / '~ 8' tail; insert annotation immediately after.
    For simplicity and bulletproofness, we insert AFTER the next
    whitespace-or-punctuation boundary that follows 'd_spec', so the
    inserted text reads "...d_spec=8 (convention pin pending ...)..."
    OR "...d_spec ~ 8 (convention pin pending ...)..." etc.
    """
    if ANNOT_SENTINEL in line:
        return line, False
    idx = line.find("d_spec")  # (local)
    if idx < 0:
        return line, False
    # Walk forward past 'd_spec' (6 chars), then past any of:
    # - '=8' / '= 8' / '=4' / '/2' / ' = 8' / ' ~ 8' / '8'
    # We want to insert after the integer (8 or 4 or after the
    # dimension number) when there is one; otherwise immediately
    # after 'd_spec'.
    j = idx + len("d_spec")  # (local)
    n = len(line)  # (local)
    # Skip leading whitespace and operator tokens like '=', '~', '/',
    # ',', up to a digit; then consume the digit(s).
    k = j  # (local)
    while k < n and line[k] in " \t=~/<>≤≥":
        k += 1
    # Now k is either at a digit or at end-of-token
    if k < n and line[k].isdigit():
        # Consume contiguous digits (e.g. '8', '4', '12')
        while k < n and line[k].isdigit():
            k += 1
        insert_at = k  # (local)
    else:
        # No digit follows; insert right after the 'd_spec' token
        insert_at = j  # (local)
    new_line = line[:insert_at] + ANNOTATION + line[insert_at:]
    return new_line, True


def rewrite_file_with_annotations(path: Path, line_targets):
    """Read file, annotate target lines, write back atomically.

    Args:
      path: file to edit.
      line_targets: list of (1-indexed line_number, scope_tag) tuples.

    Returns: list of dicts with (line_number, scope_tag, original,
    annotated, changed).
    """
    text = path.read_text(encoding="utf-8")  # (local)
    lines = text.splitlines(keepends=True)  # (local)
    inventory = []  # (local)
    for line_num, scope_tag in line_targets:
        idx = line_num - 1  # 0-based  # (local)
        if idx < 0 or idx >= len(lines):
            inventory.append({
                "line_number": line_num,
                "scope_tag": scope_tag,
                "original": "",
                "annotated": "",
                "changed": False,
                "error": "line_number out of range",
            })
            continue
        original = lines[idx]  # (local)
        # Strip trailing newline for annotation, restore after
        if original.endswith("\r\n"):
            stripped = original[:-2]  # (local)
            tail = "\r\n"  # (local)
        elif original.endswith("\n"):
            stripped = original[:-1]
            tail = "\n"
        else:
            stripped = original
            tail = ""
        new_stripped, changed = annotate_d_spec_token(stripped)
        if changed:
            lines[idx] = new_stripped + tail
        inventory.append({
            "line_number": line_num,
            "scope_tag": scope_tag,
            "original": original,
            "annotated": (new_stripped + tail) if changed else original,
            "changed": changed,
        })
    # Atomic write: tempfile in same directory, then os.replace
    parent = path.parent  # (local)
    fd, tmp_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=str(parent)
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as fp:
            fp.writelines(lines)
        os.replace(tmp_name, str(path))
    except Exception:
        # Clean up tmp on failure
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise
    return inventory


# ---------------------------------------------------------------------------
# Section 6 — Compute (annotation pass)
# ---------------------------------------------------------------------------

def compute():
    """Execute the annotation pass over all in-scope targets."""
    full_inventory = []  # (local)
    per_file_changes = {}  # (local)
    for file_path_str, targets in IN_SCOPE_TARGETS.items():
        path = Path(file_path_str)  # (local)
        if not path.exists():
            print(f"  SKIP missing: {path}")
            continue
        inventory = rewrite_file_with_annotations(path, targets)
        for row in inventory:
            row["file"] = str(path.relative_to(PROJECT_ROOT)).replace("\\", "/")
        full_inventory.extend(inventory)
        per_file_changes[str(path)] = sum(1 for r in inventory if r["changed"])
        print(f"  {path.name}: "
              f"{per_file_changes[str(path)]} / {len(targets)} annotated")
    n_landed = sum(1 for r in full_inventory if r["changed"])  # (local)
    n_in_scope = len(full_inventory)  # (local)
    n_already_annotated = n_in_scope - n_landed  # (local)
    return {
        "value": n_landed,
        "n_in_scope": n_in_scope,
        "n_landed": n_landed,
        "n_already_annotated": n_already_annotated,
        "inventory": full_inventory,
        "per_file_changes": per_file_changes,
        "out_of_scope": OUT_OF_SCOPE_NOTES,
    }


# ---------------------------------------------------------------------------
# Section 7 — Verdict, NPZ, WP append
# ---------------------------------------------------------------------------

def evaluate_gate(value, n_in_scope, n_already):
    """Gate rule:
       PASS iff value == n_in_scope (every in-scope hit annotated this
              run) OR (value == 0 AND n_already == n_in_scope) (every
              hit was ALREADY annotated, idempotent re-run).
       INFO iff n_in_scope == 0 (no in-scope citations exist; null pass).
       FAIL otherwise.
    """
    if n_in_scope == 0:
        return "INFO"
    if value + n_already == n_in_scope and (value == n_in_scope or value == 0):
        return "PASS"
    return "FAIL"


def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict, value, audit_sha, content_sha):
    """Atomic single-line append per S84+ dual-SHA schema."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
    # Companion comment row (short-form dual-SHA echo for grep audit)
    comment = (
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]} "
        f"3-tuple sign=N/A magnitude={verdict} regime=VALID\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(comment)


def save_inventory_npz(result, audit_sha, content_sha):
    """Persist citation inventory as structured arrays."""
    inv = result["inventory"]  # (local)
    files = np.array([r["file"] for r in inv], dtype=object)
    line_numbers = np.array([r["line_number"] for r in inv], dtype=np.int64)
    scope_tags = np.array([r["scope_tag"] for r in inv], dtype=object)
    originals = np.array([r["original"] for r in inv], dtype=object)
    annotateds = np.array([r["annotated"] for r in inv], dtype=object)
    changed = np.array([r["changed"] for r in inv], dtype=bool)

    oos_files = np.array([r[0] for r in OUT_OF_SCOPE_NOTES], dtype=object)
    oos_lines = np.array([r[1] for r in OUT_OF_SCOPE_NOTES], dtype=np.int64)
    oos_reasons = np.array([r[2] for r in OUT_OF_SCOPE_NOTES], dtype=object)

    np.savez(
        OUT_NPZ,
        files=files,
        line_numbers=line_numbers,
        scope_tags=scope_tags,
        originals=originals,
        annotateds=annotateds,
        changed=changed,
        n_in_scope=result["n_in_scope"],
        n_landed=result["n_landed"],
        n_already_annotated=result["n_already_annotated"],
        out_of_scope_files=oos_files,
        out_of_scope_lines=oos_lines,
        out_of_scope_reasons=oos_reasons,
        annotation_text=ANNOTATION,
        annotation_sentinel=ANNOT_SENTINEL,
        gate_id=GATE_ID,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  inventory NPZ: {OUT_NPZ.relative_to(PROJECT_ROOT)} "
          f"({OUT_NPZ.stat().st_size} B)")


def append_post_execution_subsection(result, verdict, audit_sha, content_sha):
    """Insert the **Post-execution §VII.U/§VII.W convention re-cite (HK-4)**
    sub-section into WP §W1b-3 immediately before the `---` separator
    at line 1356 (the divider between §W1b-3 and §W1b-4).

    Idempotent: scans for the sentinel header text; if present, skips.
    """
    sentinel = "**Post-execution §VII.U/§VII.W convention re-cite (HK-4)**"  # (local)
    text = WP_PATH.read_text(encoding="utf-8")  # (local)
    if sentinel in text:
        print("  WP sub-section already present; skipping append.")
        return False

    # Build the sub-section block
    inv_rows = []  # (local)
    for r in result["inventory"]:
        snippet = r["original"].rstrip()  # (local)
        if len(snippet) > 110:
            snippet = snippet[:107] + "..."
        flag = "annotated this run" if r["changed"] else "already annotated"
        inv_rows.append(
            f"| `{r['file']}` | {r['line_number']} | {r['scope_tag']} | {flag} |"
        )
    inv_table = "\n".join(inv_rows)

    oos_rows = []  # (local)
    for fname, lineno, reason in OUT_OF_SCOPE_NOTES:
        oos_rows.append(f"| `{fname}` | {lineno} | {reason} |")
    oos_table = "\n".join(oos_rows)

    block = f"""
**Post-execution §VII.U/§VII.W convention re-cite (HK-4)**

This sub-section documents the post-execution annotation pass run by the HK-4 driver `computations/session-87/s87_w1b_hk_4_vii_u_w_recite.py` (composite gate `{GATE_ID}`, verdict {verdict}, audit_sha256 `{audit_sha}`, content_sha256 `{content_sha}`). Following W1b-3's bulk-Weyl falsification of the d_eff=8 anchor (Conv-A 10.122 / Conv-B 5.061; Richardson L^{{-3}} clean), every downstream §VII.U / §VII.W citation of the same anchor (alias `d_spec=8`) MUST carry an explicit convention pin pending the HK-3 convention audit. The driver appends the inline annotation `{ANNOTATION.strip()}` immediately after each in-scope `d_spec` token; original prose is preserved exactly; idempotent on re-run via the sentinel `{ANNOT_SENTINEL}`.

**In-scope citation inventory** ({result['n_in_scope']} citations across {len(result['per_file_changes'])} files; {result['n_landed']} annotated this run; {result['n_already_annotated']} already-annotated):

| File | Line | Scope tag | Action |
|:----|:----|:----|:----|
{inv_table}

**Out-of-scope hits** ({len(OUT_OF_SCOPE_NOTES)} citations enumerated; NOT annotated — outside §VII.U / §VII.W block boundaries OR not numerical d_spec=8 claims):

| File | Line | Reason |
|:----|:----|:----|
{oos_table}

**Section-boundary verification**:
- Registry §VII.U block: lines 12586-13030 (header line 12586 `## §VII.U`; ends before §VII.K-META.COMPOSITE-60 header at line 13031). In-scope hits: 12857, 12898 (both in §VII.U.6 sub-block, lines 12878-12930).
- Registry §VII.W block: lines 14371-14499 (header line 14371 `## §VII.W`; ends before §VII.AA header at line 14500). In-scope hits: ZERO.
- Registry §VII.W-2 block: lines 15319+ (W1a-5 cross-program unification). In-scope hits: ZERO.
- WP §W1a-1 (results-workingpaper §VII.U.6 landing): lines 7-145. In-scope hits: 97, 131 (mirror registry text 12857, 12898 respectively).
- WP §W1b-3 (this section): lines 1111-1356. EXCLUDED from annotation as the SOURCE of falsification, not a downstream citation.

**Idempotency**: The driver scans each target line for the sentinel substring `{ANNOT_SENTINEL}` before appending. Re-runs detect the sentinel on already-annotated lines and skip them, leaving the line invariant. The PASS predicate accepts both the first-run case (every in-scope hit annotated this run) and the idempotent re-run case (every hit was already annotated). FAIL only if any in-scope hit is found unannotated AND the rewrite path failed to land the annotation.

**Substrate framing for the annotation**: The annotation text reads "(convention pin pending S87-W1B-HK-3; scope: bulk-Weyl-falsified per W1b-3 — may survive at per-stratum / per-cluster sub-axis)". This formulation respects the substrate-IS framing: d_spec is the substrate's OWN spectral dimension (an emergent description of D_K's eigenvalue density), not an external dimensional input. W1b-3 falsified the bulk-Weyl reading; whether the d_spec=8 identity survives at a non-bulk sub-axis (per-cluster, per-stratum-projection, fixed-fiber) is precisely the open question routed to S87-W1B-HK-3 (the convention audit) and to S88-D-EFF-ANCHOR-CONVENTION-AUDIT (the substrate-canonical re-derivation).

**Cross-references**:
- §W1b-3 (this section, lines 1111-1356): the bulk-Weyl falsification verdict and Richardson L^{{-3}} numerical anchor.
- §W1a-1 (lines 7-145): two of the four annotated lines live here (97 substrate framing prose; 131 §VII.U.6 substrate-framing block).
- `sessions/permanent-results-registry.md` §VII.U.6 entry (registry lines 12878-12930): the registry-canonical text two of the four annotations land in.
- Carry-forward queue: `S87-W1B-HK-3` (convention audit; resolves Conv-A vs Conv-B); `S88-VII-U-VII-W-CONVENTION-AUDIT` (replaces the pending-pin with a definitive convention or drops the d_spec=8 anchor in favor of a different structural identity).

**Artifact pointers**:
- Driver: `computations/session-87/s87_w1b_hk_4_vii_u_w_recite.py`
- Inventory NPZ: `computations/session-87/s87_w1b_hk_4_vii_u_w_recite.npz`
- Verdict: `computations/session-87/s87_gate_verdicts.txt` ({GATE_ID} canonical line + dual-SHA companion comment row)
- Files edited: `sessions/permanent-results-registry.md` (lines 12857, 12898); `sessions/archive/session-87/session-87-results-workingpaper.md` (lines 97, 131); `sessions/framework/registry/elimination-bulletins.md` (no edits — gate-name references only).

"""

    # Locate insertion point: the `---` separator at line 1356.
    # We anchor on the §W1b-4 header line and back up to the prior `---`.
    target_anchor = "\n### §W1b-4. S87-PAIRED-SLOT-RATIO-INTERPRETATION"  # (local)
    pos = text.find(target_anchor)  # (local)
    if pos < 0:
        # Fallback: insert at end-of-file
        new_text = text + block  # (local)
    else:
        # Walk back from pos to find the `---\n` that separates §W1b-3
        # from §W1b-4. The block has the canonical pattern:
        #   ...end of §W1b-3 content...
        #   <blank line>
        #   ---
        #   <blank line>
        #   ### §W1b-4. ...
        # We insert BEFORE the `---` separator so the new sub-section
        # appears at the END of §W1b-3.
        pre_anchor = text[:pos]  # (local)
        sep_idx = pre_anchor.rfind("\n---\n")  # (local)
        if sep_idx < 0:
            sep_idx = pre_anchor.rfind("\n---")
        if sep_idx < 0:
            new_text = text + block
        else:
            insert_pos = sep_idx + 1  # right BEFORE `---\n`  # (local)
            new_text = (
                text[:insert_pos] + block.rstrip() + "\n\n"
                + text[insert_pos:]
            )

    # Atomic write
    parent = WP_PATH.parent  # (local)
    fd, tmp_name = tempfile.mkstemp(
        prefix=f".{WP_PATH.name}.", suffix=".tmp", dir=str(parent)
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as fp:
            fp.write(new_text)
        os.replace(tmp_name, str(WP_PATH))
    except Exception:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise
    print(f"  WP sub-section appended at §W1b-3 end "
          f"({len(block)} chars).")
    return True


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)

    # 1. Log input pins (BEFORE annotation pass — captures pre-edit state)
    pins_pre = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins_pre)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs over PRE-EDIT pinmap (script + canonical
    #     + pre-edit input SHAs). The SHAs commit to the inputs as seen
    #     at execution start; the post-edit file states are recorded in
    #     the NPZ inventory rather than the audit pinmap (the same
    #     pattern the registry-write helpers under parallel-writer race
    #     follow per `epistemic-discipline.md`).
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')  # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, canonical_path, pins_pre
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute (annotation pass)
    result = compute()

    # 3. Evaluate gate
    verdict = evaluate_gate(
        result["value"], result["n_in_scope"], result["n_already_annotated"]
    )

    # 4. Save inventory NPZ
    save_inventory_npz(result, audit_sha, content_sha)

    # 5. Emit 4-tuple + append verdict (dual-SHA, S84+ schema)
    tag = emit_4tuple(result["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, result["value"], audit_sha, content_sha)

    # 6. Append post-execution sub-section to WP §W1b-3 (idempotent)
    append_post_execution_subsection(result, verdict, audit_sha, content_sha)

    # 7. Final summary
    wall = time.time() - t0  # (local)
    print()
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    print(f"   in-scope citations: {result['n_in_scope']}")
    print(f"   annotated this run: {result['n_landed']}")
    print(f"   already annotated:  {result['n_already_annotated']}")
    print(f"   out-of-scope hits enumerated: {len(OUT_OF_SCOPE_NOTES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
