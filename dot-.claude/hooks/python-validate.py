#!/usr/bin/env python3
"""
python-validate.py — PostToolUse validator for computations/**/*.py writes.

Paired with python-validate.sh. Reads a Claude Code PostToolUse tool-call
envelope on stdin, extracts the file_path, and runs four compliance checks:

  1. Canonical import present       (`from canonical_constants import ...`)
  2. No unlocal-tagged hardcodes    (assignments reusing a canonical name
                                     without a `# (local)` tag)
  3. Unregistered numeric literals  (untagged `name = <number>` style)
  4. Filename pattern               (`s{session}_*.py` session OR `inv{n}_*.py` investigation; warn if not matching)

Emits a single JSON object on stdout:
    { "hookSpecificOutput": { "hookEventName": "PostToolUse",
                              "additionalContext": "<WARN text or empty>" } }

Initial-rollout policy: WARN-only. See python-validate.sh §POLICY.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path("C:/sandbox/Ainulindale Exflation")
COMPUTATIONS_ROOT = PROJECT_ROOT / "computations"
CANON_PY = COMPUTATIONS_ROOT / "_shared" / "canonical_constants.py"

# Same regex as s80_pru_audit.py
ASSIGN_RE = re.compile(
    r"^\s*([A-Za-z_][A-Za-z_0-9]*)\s*=\s*"
    r"(-?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?)"
    r"\s*(?:#.*)?$"
)
LOCAL_TAG_RE = re.compile(r"#\s*\(?local\)?\b", re.IGNORECASE)
CANON_IMPORT_RE = re.compile(r"from\s+canonical_constants\s+import\s+")
FILENAME_RE = re.compile(r"^(?:s\d+[a-z]?|inv\d+)_[A-Za-z0-9_]+\.py$")

BUILTIN_EXCLUDE = frozenset({
    "i", "j", "k", "l", "m", "n",
    "x", "y", "z", "t",
    "pi", "e",
    "tau", "eps", "epsilon", "delta",
    "N", "M",
})

# Max warnings to list before truncating.
WARN_CAP = 12  # per-check cap, keep hook output short


def emit(additional_context: str) -> None:
    """Emit hook output. Empty additional_context → silent passthrough.

    When warnings exist, PostToolUse must emit `decision: "block"` + `reason`
    for Claude to actually see the additionalContext. `decision: "block"` on
    PostToolUse does NOT undo the tool call (that already completed); it just
    surfaces the reason + additionalContext back to Claude as a system reminder.
    Without it, the hook output is parsed and thrown away.
    """
    if not additional_context:
        # Silent passthrough: emit nothing. Hook system treats empty stdout
        # (with exit 0) as "no action".
        return

    # Take the first line as the inline `reason`; full text goes to additionalContext.
    first_line = additional_context.split("\n", 1)[0][:200]
    out = {
        "decision": "block",
        "reason": first_line,
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": additional_context,
        },
    }
    sys.stdout.write(json.dumps(out))
    sys.stdout.flush()


def load_canonical_names(path: Path) -> set[str]:
    if not path.exists():
        return set()
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return set()
    names: set[str] = set()
    for line in text.splitlines():
        # Skip indented lines (not top-level)
        if line.startswith((" ", "\t")):
            continue
        # Strip comment
        code = line.split("#", 1)[0].rstrip()
        if "=" not in code:
            continue
        lhs = code.split("=", 1)[0].strip()
        if re.match(r"^[A-Za-z_][A-Za-z_0-9]*$", lhs) and not lhs.startswith("_"):
            names.add(lhs)
    return names


def validate(target: Path) -> str:
    """Return the WARN text for a file; empty string if clean."""
    try:
        text = target.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return f"[python-validate] cannot read {target.name}: {e}"

    lines = text.splitlines()
    canon_names = load_canonical_names(CANON_PY)
    warns: list[str] = []

    # Check 1 — canonical import present
    has_canonical_import = any(CANON_IMPORT_RE.search(line) for line in lines)
    if not has_canonical_import:
        warns.append(
            f"  [1] Missing `from canonical_constants import ...` "
            f"(required by computations/_shared/CLAUDE.md)"
        )

    # Checks 2 + 3 — hardcodes and untagged literals
    hardcodes: list[str] = []
    untagged: list[str] = []
    for idx, line in enumerate(lines, start=1):
        m = ASSIGN_RE.match(line)
        if not m:
            continue
        name = m.group(1)
        literal = m.group(2)
        if name in BUILTIN_EXCLUDE:
            continue
        is_tagged = bool(LOCAL_TAG_RE.search(line))
        if name in canon_names:
            if not is_tagged:
                hardcodes.append(f"    L{idx}: `{name} = {literal}` "
                                 f"— canonical name reassigned (add `# (local)` or import)")
        else:
            if not is_tagged:
                untagged.append(f"    L{idx}: `{name} = {literal}` — tag `# (local)` or promote to canonical_constants.py")

    if hardcodes:
        warns.append(f"  [2] {len(hardcodes)} canonical-name reassignment(s):")
        warns.extend(hardcodes[:WARN_CAP])
        if len(hardcodes) > WARN_CAP:
            warns.append(f"    ...+{len(hardcodes) - WARN_CAP} more")

    if untagged:
        warns.append(f"  [3] {len(untagged)} untagged numeric literal(s):")
        warns.extend(untagged[:WARN_CAP])
        if len(untagged) > WARN_CAP:
            warns.append(f"    ...+{len(untagged) - WARN_CAP} more")

    # Check 4 — filename pattern
    if not FILENAME_RE.match(target.name) and not target.name.startswith("_"):
        warns.append(f"  [4] Filename `{target.name}` does not match "
                     f"`s{{session}}_*.py` (session) or `inv{{n}}_*.py` (investigation) "
                     f"(helpers should prefix `_`)")

    if not warns:
        return ""

    # Count actual issue categories ([1]..[4] headers), not list entries.
    n_categories = sum(1 for w in warns if re.match(r"^\s*\[\d+\]", w))
    header = (
        f"[python-validate] {target.name} — WARN ({n_categories} issue categor{'y' if n_categories == 1 else 'ies'}):"
    )
    return header + "\n" + "\n".join(warns) + (
        "\n  Policy: WARN-only during initial rollout. "
        "Fix when convenient or tag as local. See .claude/rules/math-scripts.md."
    )


def main() -> int:
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        emit("")
        return 0

    tool = payload.get("tool_name") or payload.get("toolName") or ""
    if tool not in {"Write", "Edit", "MultiEdit", "NotebookEdit"}:
        emit("")
        return 0

    tool_input = payload.get("tool_input") or payload.get("toolInput") or {}
    fp_str = tool_input.get("file_path") or tool_input.get("filePath") or ""
    if not fp_str:
        emit("")
        return 0

    target = Path(fp_str)
    try:
        target = target.resolve()
    except OSError:
        emit("")
        return 0

    # Gate on computations/**/*.py only
    try:
        target.relative_to(COMPUTATIONS_ROOT)
    except ValueError:
        emit("")
        return 0

    if target.suffix.lower() != ".py":
        emit("")
        return 0

    # Skip the validator itself, the audit tool, and other meta files
    if target.name in {"s80_pru_audit.py",
                       "python-validate.py", "canonical_constants.py"}:
        emit("")
        return 0

    msg = validate(target)
    emit(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
