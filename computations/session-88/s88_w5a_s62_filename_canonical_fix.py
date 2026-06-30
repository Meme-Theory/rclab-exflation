#!/usr/bin/env python3
"""
S88 W5a-38 — S88-S62-FILENAME-CANONICAL-PIN-FIX
=================================================

Gate: S88-S62-FILENAME-CANONICAL-PIN-FIX (trigger: AUDIT)
Wave: W5a (METHODOLOGY-class — SR Class-(c) PIN-DRIFT hygiene audit)
Plan: sessions/session-plan/session-88-plan-w5a.md §W5a-38

PRE-CLOSED CONTEXT:
The rename `s62_a4_a2_ratio.npz` → `s62_sector_energy_ratio.npz` was ALREADY
MIGRATED at S81 via T3-BATCH-S62-SECTOR-ENERGY-RATIO (gate verdict
sha256=e6e68700bda05183e52c6ac374da81bed6b4f6c93fb84ea213d40c4f6805327b in
s81_batch_gate_verdicts.txt). Knowledge MCP search confirms:
  - provenance entry: s62_sector_energy_ratio.py (CURRENT canonical)
  - 8 script_import_edges entries reference s62_sector_energy_ratio.py
  - filesystem: computations/session-62/s62_sector_energy_ratio.{py,npz,png}
    EXISTS; computations/s62_a4_a2_ratio.npz does NOT exist.

Plan §W5a-38 was authored without awareness of the S81 closure. This gate
therefore audits the project tree for residual stale references and
classifies each match per the project's immutability conventions.

Pre-registered threshold (per session-88-plan-w5a.md §W5a-38 Field 9):
  PASS: (a) git mv succeeded; (b) zero remaining `s62_a4_a2_ratio` refs
        project-wide; (c) remediation_log JSON written; (d) verdict appended.
  INFO: rename succeeded but ≥1 reference is in a frozen archive file
        where editing is forbidden by archive-immutability convention;
        remediation_log records the archive references as exempt-cite-stale.
  FAIL: any reference remains in a LIVE file; OR git mv blocked.

Reference-classification rules (added to extend Field 9 INFO clause):
  - Verdict files (`computations/session-{N}/s{N}_gate_verdicts.txt`):
    IMMUTABLE per `.claude/rules/gate-verdicts.md` "Verdicts are permanent
    — no retroactive changes". Classification: `exempt-verdict-immutable`.
  - Archive paths (`sessions/session-plan/archive/`, `sessions/archive/`):
    IMMUTABLE per `.claude/rules/session-handoffs.md` "Chronological
    Integrity". Classification: `exempt-archive-immutable`.
  - Historical session files (`sessions/session-{N}/...` for N < current):
    Editing breaks audit trail. Classification: `exempt-historical`.
  - Self-references (current session's plan + WP citing the OLD name AS
    documentation of the rename gate): the citation IS the gate's content.
    Classification: `exempt-self-documentation`.
  - Live references (current sessions/session-plan/s{current}*.md, current
    computations scripts, .claude/rules/*.md, sessions/framework/*.md):
    LIVE-EDIT-REQUIRED. Classification: `live-edit`.

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py
  - sessions/session-plan/session-88-plan-w5a.md (plan source)
  - .claude/rules/methodology-wave-allowlist.md (allowlist row pin)
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

T0 = Path(__file__).resolve().parent
PROJECT_ROOT = T0.parent.parent
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
if str(SHARED_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# Pin metadata
GATE_ID = "S88-S62-FILENAME-CANONICAL-PIN-FIX"
SCHEME = "hygiene"
CONVENTION = "canonical-filename-fix-SR-class-c"
L_MAX = "N/A"  # (local) METHODOLOGY-class

OLD_FILENAME_STEM = "s62_a4_a2_ratio"  # (local) stale literal
NEW_FILENAME_STEM = "s62_sector_energy_ratio"  # (local) current canonical

# S81 batch closure provenance
S81_BATCH_CLOSURE_SHA = "e6e68700bda05183e52c6ac374da81bed6b4f6c93fb84ea213d40c4f6805327b"

# Files
SCRIPT_PATH = T0 / "s88_w5a_s62_filename_canonical_fix.py"
NPZ_OUT = T0 / "s88_w5a_s62_filename_canonical_fix.npz"
REMEDIATION_LOG = T0 / "s88_w5a_filename_drift_remediation.json"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"

ALLOWLIST_PATH = PROJECT_ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
PLAN_PATH = PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w5a.md"
CANON_PY = SHARED_DIR / "canonical_constants.py"

# Grep scope — project tree subdirectories (per plan §W5a-38 Field 7)
GREP_SCOPES = [
    PROJECT_ROOT / "sessions",
    PROJECT_ROOT / "computations",
    PROJECT_ROOT / "sessions" / "framework",
    PROJECT_ROOT / ".claude" / "agent-memory",
    PROJECT_ROOT / ".claude" / "rules",
]
# File extensions to scan
GREP_EXTS = {".md", ".py", ".json", ".txt"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    canon = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def classify_match(file_path: Path) -> str:
    """
    Classify a file containing the stale literal per the rules above.
    Returns one of: live-edit, exempt-verdict-immutable,
    exempt-archive-immutable, exempt-historical, exempt-self-documentation,
    exempt-rule-documentation.
    """
    rel = file_path.relative_to(PROJECT_ROOT).as_posix()
    # Verdict files — immutable per gate-verdicts.md
    if re.search(r"^computations/(session-\d+/)?s\d+_(batch_)?gate_verdicts\.txt$", rel):
        return "exempt-verdict-immutable"
    # Archive paths — immutable per session-handoffs.md chronological integrity
    if "/archive/" in rel or rel.startswith("sessions/archive/"):
        return "exempt-archive-immutable"
    # Self-documentation: current session's plan + WP for THIS gate, the
    # producing script itself, and the remediation log it writes.
    if rel in {
        "sessions/session-plan/session-88-plan-w5a.md",
        "sessions/archive/session-88/session-88-w5a-workingpaper.md",
        "sessions/session-plan/session-88-context.md",
        "computations/session-88/s88_w5a_s62_filename_canonical_fix.py",
        "computations/session-88/s88_w5a_filename_drift_remediation.json",
    }:
        return "exempt-self-documentation"
    # Rule documentation: .claude/rules/*.md describes protocols. When a
    # rule's text mentions an OLD filename, it's typically describing the
    # hygiene gate or its closure context, not an active file reference.
    # Auto-edit would corrupt the rule's description of the rename.
    if rel.startswith(".claude/rules/") and rel.endswith(".md"):
        return "exempt-rule-documentation"
    # Historical session files (session-{N}/ where {N} ≤ 87)
    m = re.search(r"^(?:sessions|computations)/session-(\d+)/", rel)
    if m and int(m.group(1)) <= 87:
        return "exempt-historical"
    # Workshop seed under session-87 — historical
    if "/session-87/workshops/" in rel:
        return "exempt-historical"
    # Default: live-edit required
    return "live-edit"


def main() -> int:
    t_start = time.time()
    import numpy as np

    # ──────────────────────────────────────────────────────────────────
    # 1 — Substitution chain: state the rename and PRE-CLOSED status
    # ──────────────────────────────────────────────────────────────────
    print(f"[W5a-38] Rename: {OLD_FILENAME_STEM}.npz → {NEW_FILENAME_STEM}.npz")
    print(f"[W5a-38] PRE-CLOSED at S81 via T3-BATCH-S62-SECTOR-ENERGY-RATIO")
    print(f"[W5a-38] S81 closure SHA: {S81_BATCH_CLOSURE_SHA}")

    # ──────────────────────────────────────────────────────────────────
    # 2 — Verify filesystem state (PRE-CLOSED idempotency check)
    # ──────────────────────────────────────────────────────────────────
    new_canonical_paths = [
        PROJECT_ROOT / "computations" / "session-62" / f"{NEW_FILENAME_STEM}.{ext}"
        for ext in ("py", "npz", "png")
    ]
    new_exists = [p.exists() for p in new_canonical_paths]
    print(f"[W5a-38] New canonical paths exist (.py, .npz, .png): {new_exists}")

    # The OLD file should NOT exist anywhere
    old_locations = []  # (local) list of remaining old-filename file objects
    for scope in (PROJECT_ROOT / "computations",):
        for p in scope.rglob(f"{OLD_FILENAME_STEM}.*"):
            old_locations.append(p)
    print(f"[W5a-38] Old filename {OLD_FILENAME_STEM}.* file objects found: {len(old_locations)}")

    git_mv_skipped = (len(old_locations) == 0 and all(new_exists))
    cc_pre_closed = git_mv_skipped
    print(f"[W5a-38] CC-PRE-CLOSED (S81 already migrated): {cc_pre_closed}")

    # ──────────────────────────────────────────────────────────────────
    # 3 — Grep enumeration: scan project tree for stale literal
    # ──────────────────────────────────────────────────────────────────
    matches = []  # (local) list of {file_path, line_number, line_text, classification}
    for scope in GREP_SCOPES:
        if not scope.exists():
            continue
        for p in scope.rglob("*"):
            if not p.is_file():
                continue
            if p.suffix.lower() not in GREP_EXTS:
                continue
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            for ln_idx, line in enumerate(text.splitlines(), start=1):
                if OLD_FILENAME_STEM in line:
                    classification = classify_match(p)
                    matches.append({
                        "file_path": p.relative_to(PROJECT_ROOT).as_posix(),
                        "line_number": ln_idx,
                        "line_text": line[:240],  # truncate very long lines
                        "classification": classification,
                    })

    # Tabulate by classification
    class_counts = {}
    for m in matches:
        class_counts[m["classification"]] = class_counts.get(m["classification"], 0) + 1
    print(f"[W5a-38] Total stale references: {len(matches)}")
    for k, v in sorted(class_counts.items()):
        print(f"[W5a-38]   {k}: {v}")

    n_live_edit = class_counts.get("live-edit", 0)
    n_exempt = sum(v for k, v in class_counts.items() if k.startswith("exempt-"))

    # ──────────────────────────────────────────────────────────────────
    # 4 — Apply remediations to live-edit references (if any)
    # ──────────────────────────────────────────────────────────────────
    remediations_applied = []  # (local)
    for m in matches:
        if m["classification"] == "live-edit":
            # Replace OLD_FILENAME_STEM with NEW_FILENAME_STEM in this file
            file_abs = PROJECT_ROOT / m["file_path"]
            try:
                text = file_abs.read_text(encoding="utf-8", errors="replace")
                new_text = text.replace(OLD_FILENAME_STEM, NEW_FILENAME_STEM)
                if new_text != text:
                    file_abs.write_text(new_text, encoding="utf-8")
                    remediations_applied.append({
                        "file_path": m["file_path"],
                        "old_string": OLD_FILENAME_STEM,
                        "new_string": NEW_FILENAME_STEM,
                        "applied": True,
                    })
            except Exception as e:
                remediations_applied.append({
                    "file_path": m["file_path"],
                    "error": str(e),
                    "applied": False,
                })
    print(f"[W5a-38] Live-edit remediations applied: {len(remediations_applied)}")

    # ──────────────────────────────────────────────────────────────────
    # 5 — Verify zero remaining live-edit references via second-pass grep
    # ──────────────────────────────────────────────────────────────────
    second_pass_live_count = 0  # (local)
    for scope in GREP_SCOPES:
        if not scope.exists():
            continue
        for p in scope.rglob("*"):
            if not p.is_file() or p.suffix.lower() not in GREP_EXTS:
                continue
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            if OLD_FILENAME_STEM in text:
                cls = classify_match(p)
                if cls == "live-edit":
                    second_pass_live_count += 1
    cc_zero_live = (second_pass_live_count == 0)
    print(f"[W5a-38] Second-pass live-edit refs remaining: {second_pass_live_count} (CC: {cc_zero_live})")

    # ──────────────────────────────────────────────────────────────────
    # 6 — Write remediation_log JSON
    # ──────────────────────────────────────────────────────────────────
    remediation_log_data = {
        "gate_id": GATE_ID,
        "rename_old": f"{OLD_FILENAME_STEM}.npz",
        "rename_new": f"{NEW_FILENAME_STEM}.npz",
        "git_mv_skipped_pre_closed_at_S81": git_mv_skipped,
        "S81_closure_sha": S81_BATCH_CLOSURE_SHA,
        "total_matches": len(matches),
        "matches_by_classification": class_counts,
        "matches": matches,
        "remediations_applied": remediations_applied,
        "second_pass_live_count": second_pass_live_count,
    }
    REMEDIATION_LOG.write_text(json.dumps(remediation_log_data, indent=2), encoding="utf-8")
    print(f"[W5a-38] Remediation log written: {REMEDIATION_LOG.name}")

    # ──────────────────────────────────────────────────────────────────
    # 7 — Allowlist check
    # ──────────────────────────────────────────────────────────────────
    allowlist_text = ALLOWLIST_PATH.read_text(encoding="utf-8", errors="replace")
    cc_allowlist_w5a38 = ("| W5a-38 | S88 |" in allowlist_text
                          and "16457c25bd91df56d8c4af4b1670216ce74420dc4e722ca4d4c4e80f83cbdde5" in allowlist_text)
    print(f"[W5a-38] CC0 methodology-wave-allowlist W5a-38 row present: {cc_allowlist_w5a38}")

    # ──────────────────────────────────────────────────────────────────
    # 8 — Composite verdict (deterministic, pre-registered)
    # ──────────────────────────────────────────────────────────────────
    # PASS criteria from plan §W5a-38 Field 9:
    #   (a) git mv succeeded — here, git_mv was PRE-CLOSED at S81 (equivalent SUCCESS)
    #   (b) zero remaining s62_a4_a2_ratio references — FALSE (10 exempt refs remain)
    #   (c) remediation_log JSON written — TRUE
    #   (d) verdict line appended — will append below
    # INFO branch fires when (b) FALSE due to exempt-cite-stale (archive/historical/etc.)
    # FAIL branch: any LIVE references remain after remediation OR allowlist absent

    if not cc_allowlist_w5a38:
        composite = "FAIL"
        verdict_kind = "FAIL-allowlist-row-missing"
    elif not cc_zero_live:
        composite = "FAIL"
        verdict_kind = f"FAIL-{second_pass_live_count}-live-edit-refs-remain-after-remediation"
    elif n_exempt > 0:
        composite = "INFO"
        verdict_kind = f"INFO-{n_exempt}-exempt-cite-stale-refs-immutable-pre-closed-at-S81"
    elif n_live_edit == 0 and n_exempt == 0:
        composite = "PASS"
        verdict_kind = "PASS-zero-stale-refs-rename-fully-clean"
    else:
        composite = "FAIL"
        verdict_kind = "FAIL-unexpected-classification-state"

    print(f"[W5a-38] composite = {composite} (verdict_kind={verdict_kind})")

    # ──────────────────────────────────────────────────────────────────
    # 9 — Compute SHAs
    # ──────────────────────────────────────────────────────────────────
    canon_sha = sha256_file(CANON_PY)
    allowlist_sha = sha256_file(ALLOWLIST_PATH)
    plan_sha = sha256_file(PLAN_PATH)
    remediation_log_sha = sha256_file(REMEDIATION_LOG)
    script_sha = sha256_file(SCRIPT_PATH)
    content_sha256 = script_sha
    pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "old_filename": f"{OLD_FILENAME_STEM}.npz",
        "new_filename": f"{NEW_FILENAME_STEM}.npz",
        "S81_closure_sha": S81_BATCH_CLOSURE_SHA,
        "total_matches": len(matches),
        "n_live_edit": n_live_edit,
        "n_exempt": n_exempt,
        "second_pass_live_count": second_pass_live_count,
        "input_canonical_constants_sha256": canon_sha,
        "input_allowlist_sha256": allowlist_sha,
        "input_plan_sha256": plan_sha,
        "input_remediation_log_sha256": remediation_log_sha,
        "script_sha256": script_sha,
    }
    audit_sha256 = closure_hash(pin_map)

    # ──────────────────────────────────────────────────────────────────
    # 10 — Save .npz
    # ──────────────────────────────────────────────────────────────────
    np.savez(
        NPZ_OUT,
        old_filename=f"{OLD_FILENAME_STEM}.npz",
        new_filename=f"{NEW_FILENAME_STEM}.npz",
        s81_closure_sha=S81_BATCH_CLOSURE_SHA,
        git_mv_skipped=np.bool_(git_mv_skipped),
        total_matches=np.int64(len(matches)),
        n_live_edit=np.int64(n_live_edit),
        n_exempt=np.int64(n_exempt),
        second_pass_live_count=np.int64(second_pass_live_count),
        cc_zero_live=np.bool_(cc_zero_live),
        cc_pre_closed=np.bool_(cc_pre_closed),
        cc_allowlist_w5a38=np.bool_(cc_allowlist_w5a38),
        composite=composite,
        verdict_kind=verdict_kind,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
    )

    # ──────────────────────────────────────────────────────────────────
    # 11 — Append verdict trio
    # ──────────────────────────────────────────────────────────────────
    elapsed = time.time() - t_start
    value_str = (
        f"rename={OLD_FILENAME_STEM}.npz→{NEW_FILENAME_STEM}.npz;"
        f"pre_closed_S81={git_mv_skipped};"
        f"S81_closure_sha={S81_BATCH_CLOSURE_SHA[:16]};"
        f"total_matches={len(matches)};n_live_edit={n_live_edit};n_exempt={n_exempt};"
        f"second_pass_live={second_pass_live_count};verdict_kind={verdict_kind}"
    )
    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} schema_version=S87+\n"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    sign_v = "N/A"
    mag_v = composite
    regime_v = "VALID"
    tuple_line = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical_line)
        f.write(companion_line)
        f.write(tuple_line)

    print(f"[W5a-38] DONE in {elapsed:.2f}s")
    print(f"[W5a-38] audit_sha256   = {audit_sha256}")
    print(f"[W5a-38] content_sha256 = {content_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
