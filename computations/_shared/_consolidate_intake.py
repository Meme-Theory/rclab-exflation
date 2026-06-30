#!/usr/bin/env python3
"""
Consolidate intake verdicts into s81_gate_verdicts.txt.

Reads every `computations/_shared/t3-intake/t3_*_verdict.txt`, extracts the S81
canonical verdict line (and contiguous `#` comment lines immediately after
it), and appends to `computations/session-81/s81_gate_verdicts.txt` — skipping
gates already present.

Usage:
    python _consolidate_intake.py           # append new verdicts only
    python _consolidate_intake.py --dry     # preview what would be added
    python _consolidate_intake.py --force   # re-append even if present

NON-PHONONIC infrastructure; no substitution-chain trigger.
"""
from __future__ import annotations

# Canonical import per project rules (unused here; this script operates on
# plain text, but the audit rejects computation scripts missing this line).
from canonical_constants import *  # noqa: F401,F403

import argparse
import re
import sys
from pathlib import Path
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


PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'COMPUTATIONS_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
INTAKE_DIR = resolve_script(None, 't3-intake')
VERDICT_LOG = resolve_output(81, 's81_gate_verdicts.txt')

# S81 (legacy, single-SHA) canonical verdict regex — pre-S84 form.
# Line MUST match this to be harvested under the legacy schema.
RE_S81_LINE = re.compile(
    r"^(T3-[A-Z][A-Z0-9\-]+):\s+"
    r"(PASS|FAIL|INFO|PRE-REG|INCOMPUTABLE|CANCELLED|INTERMEDIATE)\s+"
    r"--\s+"
    # Value may be a simple token OR a parens-wrapped tuple (which may
    # contain spaces after commas, e.g. `(a_0=..., a_2=...)`). Non-greedy
    # up to " scheme=".
    r"value=(.+?)\s+"
    r"scheme=(\S+)\s+"
    r"convention=(\S+)\s+"
    r"L_max=(\S+)\s+"
    r"sha256=([0-9a-fA-F]{40,})\s*$",
    re.MULTILINE,
)

# Verdict-token alternation observed across S81+ verdict files.
# Keep this list in sync with `.claude/rules/gate-verdicts.md` §Verdict Format.
_VERDICT_TOKENS = (
    r"PASS|FAIL|INFO|PENDING-EVENT|PRE-REG-INCOMPLETE|PRE-REG|"
    r"INCOMPUTABLE|CANCELLED|INTERMEDIATE"
)

# S84+ dual-SHA canonical verdict regex. Accepts gate IDs that start
# with either `T3-` (re-run intake) or `S{NN}-` (session gates) — the
# dual-SHA schema is defined for all S84+ verdicts, not just intake.
#
# Line shape (the SCRIPT TEMPLATE canonical order):
#   {GATE}: VERDICT -- value=<v> scheme=<s> convention=<c> L_max=<L>
#     audit_sha256=<64> content_sha256=<64> schema_version=S84+
#
# Observed in the wild (S84 dual-SHA producers): `content_sha256`
# occasionally emitted BEFORE `audit_sha256`. Both orderings are
# accepted. content_sha256 may be the literal "LEGACY-PRE-S84" marker
# when the shim promotes a legacy single-SHA verdict in-memory.
#
# The value token is permissive (allows embedded `=`, `,`, `()`) — it is
# opaque to the consolidator. The field-boundary anchor is
# `scheme=` after the last value chunk.
RE_S84_DUAL_LINE = re.compile(
    r"^((?:T3|S\d+|W\d+)[-A-Za-z0-9_][A-Za-z0-9\-_/]*):\s+"
    r"(" + _VERDICT_TOKENS + r")\s+"
    r"--\s+"
    r"value=(.+?)\s+scheme=(.+?)\s+convention=(.+?)\s+L_max=(\S+)\s+"
    # Dual-SHA fields: either order accepted.
    r"(?:"
    r"audit_sha256=(?P<audit1>[0-9a-fA-F]{40,})\s+"
    r"content_sha256=(?P<content1>[0-9a-fA-F]{40,}|LEGACY-PRE-S84)"
    r"|"
    r"content_sha256=(?P<content2>[0-9a-fA-F]{40,}|LEGACY-PRE-S84)\s+"
    r"audit_sha256=(?P<audit2>[0-9a-fA-F]{40,})"
    r")"
    r"(?:\s+schema_version=(?P<schema>\S+))?"
    r"\s*$",
    re.MULTILINE,
)

# Looser legacy S81+ regex that also accepts session gate IDs
# (S{NN}-...) — needed by the dual-SHA shim to promote legacy S83
# verdicts. Not used by the intake consolidation path (which retains
# the strict T3-only regex above).
RE_LEGACY_ANY_LINE = re.compile(
    r"^((?:T3|S\d+|W\d+)[-A-Za-z0-9_][A-Za-z0-9\-_/]*):\s+"
    r"(" + _VERDICT_TOKENS + r")\s+"
    r"--\s+"
    r"value=(.+?)\s+scheme=(.+?)\s+convention=(.+?)\s+L_max=(\S+)\s+"
    r"sha256=([0-9a-fA-F]{40,})\s*$",
    re.MULTILINE,
)

LEGACY_CONTENT_MARKER = "LEGACY-PRE-S84"  # (local) per W9a-99 PRDR pin

# Hybrid verdict-line handler: some pre-W9a-99 S84 scripts emitted BOTH
# `sha256=<64>` (legacy) AND `audit_sha256=<64>`/`content_sha256=<64>`
# (new-schema) on the same line during the transition. The consolidator
# accepts these lines and promotes them to dual-SHA records, with a
# warning flag `hybrid_transition=True`. Strict form (no legacy
# `sha256=` when dual is present) is preferred for all S85+ emitters.
_HYBRID_AUDIT_KV = re.compile(r"audit_sha256=([0-9a-fA-F]{40,})")
_HYBRID_CONTENT_KV = re.compile(
    r"content_sha256=([0-9a-fA-F]{40,}|LEGACY-PRE-S84)"
)
_HYBRID_LEGACY_KV = re.compile(r"\bsha256=([0-9a-fA-F]{40,})")
_HYBRID_GATE_RE = re.compile(
    r"^((?:T3|S\d+|W\d+)[-A-Za-z0-9_][A-Za-z0-9\-_/]*):\s+"
    r"(" + _VERDICT_TOKENS + r")\s+--\s+"
)


def _existing_gate_ids() -> set[str]:
    """Gate IDs already appearing in the verdict log."""
    if not VERDICT_LOG.exists():
        return set()
    out: set[str] = set()
    text = VERDICT_LOG.read_text(encoding="utf-8")
    for m in RE_S81_LINE.finditer(text):
        out.add(m.group(1))
    return out


# ---------------------------------------------------------------------------
# S84+ dual-SHA shim (W9a-99)
#
# The shim provides a uniform record shape across the legacy single-SHA
# schema (S81–S83) and the dual-SHA schema (S84+). Any verdict-consuming
# audit tool should call `parse_verdict_line` rather than the raw regex
# so that upstream code is schema-version-agnostic.
#
# Record shape (dict):
#   {
#     "gate_id":        str,
#     "verdict":        PASS|FAIL|INFO|...,
#     "value":          str,  # raw token — per-gate casting is caller's job
#     "scheme":         str,
#     "convention":     str,
#     "L_max":          str,
#     "audit_sha256":   64-hex,
#     "content_sha256": 64-hex | "LEGACY-PRE-S84",
#     "schema_version": "S84+" | "LEGACY",
#   }
# ---------------------------------------------------------------------------

class MalformedVerdictLine(ValueError):
    """Raised when a line matches neither the S84+ dual-SHA schema nor
    any recognised legacy single-SHA form. Callers that need to reject
    malformed input should propagate this exception; audit tools that
    scan a mixed log should catch it and skip the offending line."""


def parse_verdict_line(line: str) -> dict:
    """Parse one verdict line; return a canonical record dict.

    Try S84+ dual-SHA schema FIRST (presence of BOTH `audit_sha256=` and
    `content_sha256=` keys). Fall back to the legacy single-SHA form and
    promote to dual-SHA-shaped record with content_sha256 set to the
    LEGACY_CONTENT_MARKER. Raise MalformedVerdictLine otherwise.
    """
    m = RE_S84_DUAL_LINE.match(line.strip() + "\n")
    if m is None:
        m = RE_S84_DUAL_LINE.match(line.strip())
    if m is not None:
        audit_val = m.group("audit1") or m.group("audit2")  # (local)
        content_val = m.group("content1") or m.group("content2")  # (local)
        schema_val = m.group("schema") or "S84+"  # (local)
        return {
            "gate_id":        m.group(1),
            "verdict":        m.group(2),
            "value":          m.group(3),
            "scheme":         m.group(4),
            "convention":     m.group(5),
            "L_max":          m.group(6),
            "audit_sha256":   audit_val,
            "content_sha256": content_val,
            "schema_version": schema_val,
        }

    # Legacy single-SHA: promote to dual-SHA-shaped record.
    m = RE_LEGACY_ANY_LINE.match(line.strip() + "\n")
    if m is None:
        m = RE_LEGACY_ANY_LINE.match(line.strip())
    if m is not None:
        return {
            "gate_id":        m.group(1),
            "verdict":        m.group(2),
            "value":          m.group(3),
            "scheme":         m.group(4),
            "convention":     m.group(5),
            "L_max":          m.group(6),
            "audit_sha256":   m.group(7),
            "content_sha256": LEGACY_CONTENT_MARKER,
            "schema_version": "LEGACY",
        }

    # Hybrid transitional: line has BOTH `sha256=<64>` (legacy) AND
    # at least one of `audit_sha256=<64>`/`content_sha256=<64>`. Observed
    # in S84 pre-W9a-99 emitters. Promote to dual-SHA; audit_sha256 wins
    # if both legacy and new audit keys appear (new wins); content_sha256
    # defaults to LEGACY_CONTENT_MARKER if absent.
    gate_m = _HYBRID_GATE_RE.match(line.strip())
    audit_m = _HYBRID_AUDIT_KV.search(line)
    content_m = _HYBRID_CONTENT_KV.search(line)
    legacy_m = _HYBRID_LEGACY_KV.search(line)
    has_any_sha = bool(audit_m or content_m or legacy_m)
    if gate_m is not None and has_any_sha:
        audit_sha = audit_m.group(1) if audit_m else (
            legacy_m.group(1) if legacy_m else None
        )  # (local)
        content_sha = (
            content_m.group(1) if content_m else LEGACY_CONTENT_MARKER
        )  # (local)
        if audit_sha is None:
            raise MalformedVerdictLine(
                f"hybrid line has no usable SHA: {line.strip()!r}"
            )
        return {
            "gate_id":        gate_m.group(1),
            "verdict":        gate_m.group(2),
            "value":          "<hybrid-transition>",
            "scheme":         "<hybrid-transition>",
            "convention":     "<hybrid-transition>",
            "L_max":          "<hybrid-transition>",
            "audit_sha256":   audit_sha,
            "content_sha256": content_sha,
            "schema_version": "HYBRID-TRANSITION",
        }

    raise MalformedVerdictLine(
        f"verdict line matches neither S84+ dual-SHA nor legacy single-SHA "
        f"schema: {line.strip()!r}"
    )


def scan_verdict_file(path: Path) -> dict:
    """Scan an s{N}_gate_verdicts.txt file; return counts + records.

    Returns:
        {
          "dual_sha":  [ record, ... ],   # S84+ canonical (schema_version=S84+)
          "legacy":    [ record, ... ],   # promoted-legacy (schema_version=LEGACY)
          "hybrid":    [ record, ... ],   # hybrid transition (schema_version=HYBRID-TRANSITION)
          "malformed": [ (line_no, text), ... ],
        }
    """
    dual: list[dict] = []
    legacy: list[dict] = []
    hybrid: list[dict] = []
    malformed: list[tuple[int, str]] = []
    if not path.exists():
        return {
            "dual_sha": dual,
            "legacy": legacy,
            "hybrid": hybrid,
            "malformed": malformed,
        }

    for idx, raw in enumerate(
        path.read_text(encoding="utf-8", errors="replace").splitlines(),
        start=1,
    ):
        s = raw.strip()
        # Skip blanks, comments, prose headers.
        if not s or s.startswith("#"):
            continue
        # Only attempt to parse lines that look like a verdict
        # ("GATE_ID: VERDICT -- ..."). Anything else is prose; skip silently.
        if " -- " not in s:
            continue
        # Must contain at least one SHA-bearing key (value=, sha256=, etc.)
        if (
            "value=" not in s
            and "sha256=" not in s
            and "audit_sha256=" not in s
        ):
            continue
        try:
            rec = parse_verdict_line(s)
        except MalformedVerdictLine:
            malformed.append((idx, s))
            continue
        schema = rec["schema_version"]  # (local)
        if schema == "HYBRID-TRANSITION":
            hybrid.append(rec)
        elif schema == "LEGACY":
            legacy.append(rec)
        else:
            dual.append(rec)
    return {
        "dual_sha": dual,
        "legacy": legacy,
        "hybrid": hybrid,
        "malformed": malformed,
    }


# ---------------------------------------------------------------------------
# S91 W0 R6 — Supersedes-chain consumer adoption (Option-A protocol)
#
# Per `.claude/rules/gate-verdicts.md §"Option A — sig_5 remediation pathway
# under absolute verdict permanence"` item 3 (S88 W8-100 user adjudication):
#
#   "Downstream consumers cite the LATEST NON-SUPERSEDED line as canonical.
#    Orchestrators, audit scripts, /weave --update, _consolidate_intake.py,
#    and any other tool that resolves a gate's canonical verdict MUST follow
#    the supersession chain: scan all canonical lines for the gate-ID,
#    identify each line that is named in another line's supersedes= token,
#    exclude those superseded lines from the canonical reading, and treat
#    the latest non-superseded line as authoritative."
#
# `supersedes=<full-64-char-old-audit-sha>` tags appear in EITHER:
#   (a) the value field of the corrective canonical line, OR
#   (b) the dual-SHA companion comment row immediately following.
# Both forms are scanned by the discipline below.
#
# Calibration corpus (N=3 from S88 Wave 8 per gate-verdicts.md §"Calibration
# corpus (N=3 from S88 Wave 8)"):
#   - S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE
#     (line 270 FAIL + line 286 FAIL superseded by line 290 PASS)
#   - S88-W8-89-STAGE-2-AXIS-A-CONNES-VERIFY
#     (line 296 FAIL superseded by line 300 PASS)
#   - S88-CF-28-ORPHAN-FNL-PATHWAY-REGISTRY-UPDATE
#     (line 277 FAIL superseded by line 284 PASS)
#
# Additional S90 corpus instances surfaced via grep during S91 W0 R2:
#   - S90-VII-NEXT-SUBSTRATE-CLOCK-UNIQUENESS-THEOREM-STAGE-1-CANDIDATE-LANDING
#     (W2-2 corrective; supersedes da4f9f261a801680c3c01e1389d6e9c66df027e44520704335ed97ac350293ae)
#   - S90-W6A-PLAN-FILE-OR-DOWNSTREAM-ANCHOR-RECONCILIATION
#     (W2-7 corrective; supersedes c0fa4b0d80142d27480013c031b5d2fa9d5660468faf8d06cc9e0f73b79f90e2)
# ---------------------------------------------------------------------------

# Regex for `supersedes=<full-64-char-old-audit-sha>` tokens in either the
# value field (canonical line) or the companion comment row.
SUPERSEDES_TOKEN_RE = re.compile(r"supersedes=([0-9a-fA-F]{40,64})")


def extract_supersedes_pointers(verdict_file_text: str) -> dict[str, list[dict]]:
    """Extract all `supersedes=` pointers from a verdict-file text body.

    Scans BOTH canonical lines AND companion comment rows for the
    `supersedes=<64-hex>` token. Each pointer records:
      - successor_audit_sha: the audit_sha256 of the line carrying the
        supersedes= token (i.e., the corrective successor)
      - superseded_audit_sha: the audit_sha256 the successor names as
        superseded (i.e., the old line being retired from canonical
        reading but RETAINED on disk per absolute verdict permanence)
      - line_no: 1-indexed line number of the line carrying the token
      - context: "canonical" or "companion_row"

    Returns:
      dict mapping superseded_audit_sha (64-hex) → list of pointer dicts.
      A single superseded SHA may receive multiple supersedes pointers
      across the lifetime of the verdict file; the latest non-superseded
      successor (per canonical-line ordering) IS the authoritative entry.
    """
    pointers: dict[str, list[dict]] = {}
    # Walk lines; for each line that contains a supersedes= token, look
    # backward up to 5 lines to find the parent canonical line and
    # extract its audit_sha256 (the successor's audit_sha).
    lines = verdict_file_text.splitlines()
    for idx, line in enumerate(lines, start=1):
        m_super = SUPERSEDES_TOKEN_RE.search(line)
        if m_super is None:
            continue
        superseded_sha = m_super.group(1).lower()  # (local) canonical lowercase
        # Identify the successor's audit_sha:
        #   (a) If THIS line is the canonical line, parse its audit_sha256 directly
        #   (b) If THIS line is the companion comment row, walk backward to the
        #       canonical line and parse its audit_sha256
        successor_sha = None  # (local)
        context_kind = None  # (local)
        # Try (a): is this line itself a canonical verdict line?
        try:
            rec = parse_verdict_line(line)
            successor_sha = rec["audit_sha256"].lower()
            context_kind = "canonical"
        except MalformedVerdictLine:
            # Try (b): walk backward up to 5 lines for the canonical parent
            for back in range(1, 6):
                if idx - back - 1 < 0:
                    break
                parent_line = lines[idx - back - 1]
                try:
                    parent_rec = parse_verdict_line(parent_line)
                    successor_sha = parent_rec["audit_sha256"].lower()
                    context_kind = "companion_row"
                    break
                except MalformedVerdictLine:
                    continue
        if successor_sha is None:
            # Couldn't bind the supersedes token to a parent canonical line
            # (unusual; may indicate a malformed comment row). Skip silently.
            continue
        ptr_record = {  # (local)
            "successor_audit_sha": successor_sha,
            "superseded_audit_sha": superseded_sha,
            "line_no": idx,
            "context": context_kind,
        }
        pointers.setdefault(superseded_sha, []).append(ptr_record)
    return pointers


def resolve_supersession_chains(
    records: list[dict],
    verdict_file_text: str,
) -> dict:
    """Apply Option-A supersession-chain filtering to verdict records.

    Per `gate-verdicts.md §"Option A"` item 3, downstream consumers MUST
    treat the LATEST NON-SUPERSEDED line per gate-ID as canonical. This
    function:
      1. Extracts all `supersedes=` pointers from `verdict_file_text`.
      2. Builds the set of SUPERSEDED audit_sha256 values.
      3. Partitions `records` into:
           - `canonical`: records whose audit_sha256 is NOT in the
             superseded set (the latest non-superseded line per gate-ID)
           - `superseded`: records whose audit_sha256 IS in the superseded
             set (retained on disk per absolute verdict permanence, but
             excluded from canonical reading)
      4. For each gate-ID, if multiple canonical records exist (e.g., the
         gate has no supersedes chain at all, just multiple emissions),
         the LATEST by line order is returned in `canonical_latest_per_gate`.

    Args:
      records: list of record dicts from scan_verdict_file()['dual_sha'] +
               ['legacy'] (or any flat list of records).
      verdict_file_text: the raw verdict-file text body (for scanning
                          supersedes pointers in companion rows + value fields).

    Returns:
      dict with keys:
        - 'pointers':              dict[superseded_sha, list[pointer_record]]
        - 'superseded_shas':       set[str] of audit_sha256 values that
                                     are superseded by some successor
        - 'all_records':           records (input pass-through)
        - 'canonical_records':     records minus those whose audit_sha256
                                     is in superseded_shas
        - 'superseded_records':    records whose audit_sha256 IS in
                                     superseded_shas (RETAINED ON DISK
                                     per absolute verdict permanence, but
                                     EXCLUDED from canonical reading)
        - 'canonical_latest_per_gate': dict[gate_id, canonical_record]
                                       — the latest canonical record per
                                         gate-ID (for downstream consumers
                                         that resolve a single canonical
                                         verdict per gate)
    """
    pointers = extract_supersedes_pointers(verdict_file_text)
    superseded_shas: set[str] = set(pointers.keys())  # (local)

    canonical_records: list[dict] = []
    superseded_records: list[dict] = []
    for rec in records:
        rec_sha = rec.get("audit_sha256", "").lower()
        if rec_sha in superseded_shas:
            superseded_records.append(rec)
        else:
            canonical_records.append(rec)

    # Build canonical_latest_per_gate (last canonical record per gate_id by
    # input order; assumes records iterated in canonical line-order from the
    # verdict file, which is the natural order from scan_verdict_file()).
    canonical_latest_per_gate: dict[str, dict] = {}
    for rec in canonical_records:
        canonical_latest_per_gate[rec["gate_id"]] = rec  # (local) overwrite preserves latest

    return {
        "pointers": pointers,
        "superseded_shas": superseded_shas,
        "all_records": records,
        "canonical_records": canonical_records,
        "superseded_records": superseded_records,
        "canonical_latest_per_gate": canonical_latest_per_gate,
    }


def _harvest_one(path: Path) -> tuple[str, str] | None:
    """Return (gate_id, block) for the first S81 line in the file.

    The block includes the canonical verdict line + all contiguous `#`
    comment lines immediately following it, cut off at the next blank
    or non-indented non-comment line.
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    m = RE_S81_LINE.search(text)
    if not m:
        return None
    gate_id = m.group(1)
    lines = text.split("\n")
    # Locate the line-index of the canonical line
    canon_line_idx = -1  # (local) sentinel before scan
    for i, ln in enumerate(lines):
        if ln.startswith(f"{gate_id}:"):
            canon_line_idx = i
            break
    if canon_line_idx < 0:
        return None
    # Collect the canonical line + contiguous comment lines below
    block_lines = [lines[canon_line_idx]]
    for ln in lines[canon_line_idx + 1:]:
        if not ln.strip():
            break
        stripped = ln.lstrip()
        if stripped.startswith("#"):
            block_lines.append(ln)
            continue
        # Stop at first non-comment non-blank line (prose/header/new block)
        break
    block = "\n".join(block_lines).rstrip()
    return gate_id, block


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry", action="store_true",
                    help="Preview appends without writing")
    ap.add_argument("--force", action="store_true",
                    help="Re-append even if gate ID already present")
    args = ap.parse_args()

    if not INTAKE_DIR.is_dir():
        print(f"ERROR: intake dir missing: {INTAKE_DIR}")
        return 2

    existing = set() if args.force else _existing_gate_ids()
    intake_files = sorted(INTAKE_DIR.glob("t3_*_verdict.txt"))
    if not intake_files:
        print("No t3_*_verdict.txt files in intake. Nothing to consolidate.")
        return 0

    new_blocks: list[tuple[Path, str, str]] = []
    skipped_present: list[tuple[Path, str]] = []
    unparseable: list[Path] = []

    for f in intake_files:
        harvested = _harvest_one(f)
        if harvested is None:
            unparseable.append(f)
            continue
        gate_id, block = harvested
        if gate_id in existing:
            skipped_present.append((f, gate_id))
            continue
        new_blocks.append((f, gate_id, block))

    print(f"Intake files scanned: {len(intake_files)}")
    print(f"  new (will append):  {len(new_blocks)}")
    print(f"  already in log:     {len(skipped_present)}")
    print(f"  unparseable:        {len(unparseable)}")

    for f in unparseable:
        print(f"    [UNPARSEABLE] {f.name}")
    for f, gid in skipped_present:
        print(f"    [SKIP]        {gid}  ({f.name})")
    for f, gid, _ in new_blocks:
        print(f"    [APPEND]      {gid}  ({f.name})")

    if args.dry:
        print("\n--- dry-run preview (blocks to append) ---")
        for _, gid, block in new_blocks:
            print(f"\n>>> {gid}")
            print(block)
        return 0

    if not new_blocks:
        print("\nNothing new to append.")
        return 0

    # Append atomically (single write append)
    append = ["\n## Level 3 intake consolidation\n"]
    for _, _, block in new_blocks:
        append.append("\n" + block + "\n")
    with VERDICT_LOG.open("a", encoding="utf-8") as out:
        out.write("".join(append))

    print(f"\nAppended {len(new_blocks)} verdict block(s) to {VERDICT_LOG}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
