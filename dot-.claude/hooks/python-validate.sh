#!/bin/bash
# ----------------------------------------------------------------------------
# Computation-Script Python Validation Hook
# ----------------------------------------------------------------------------
# Fires PostToolUse on Write|Edit|MultiEdit. If the tool_input.file_path lands
# inside computations/**/*.py, runs four checks and — only when warnings
# exist — emits `{decision:"block", reason:..., hookSpecificOutput.additionalContext:...}`.
# `decision:"block"` on PostToolUse does NOT undo the tool call (already done);
# it surfaces the reason + additionalContext to Claude as a system reminder.
# Without `decision:"block"`, PostToolUse additionalContext is parsed and
# discarded — the hook would be silent. Clean files produce silent passthrough.
#
#   1. Canonical import present       (`from canonical_constants import`)
#   2. No unlocal-tagged hardcodes    (regex-matches canonical symbol list)
#   3. Unregistered numeric literals  (untagged `name = <number>` lines)
#   4. Filename pattern               (`s{session}_*.py` or `inv{n}_*.py`)
#
# Wired in .claude/settings.local.json PostToolUse[matcher:Edit|Write|MultiEdit].
# ----------------------------------------------------------------------------

set -e

# Read the tool-call envelope from stdin.
PAYLOAD=$(cat)

# Delegate all parsing + checks to Python (the project venv is the canonical
# runtime, avoiding jq / sed dependencies that drift on Windows).
VENV_PY="C:/sandbox/Ainulindale Exflation/phonon-exflation-sim/.venv312/Scripts/python.exe"

if [[ ! -x "$VENV_PY" ]]; then
    # Venv unavailable — silent passthrough (empty stdout + exit 0).
    exit 0
fi

# Run the validator. stdout is the JSON hook envelope; stderr is diagnostic.
# On error inside the Python script, we still emit a passthrough envelope.
RESULT=$("$VENV_PY" "C:/sandbox/Ainulindale Exflation/.claude/hooks/python-validate.py" <<< "$PAYLOAD") || {
    # Silent passthrough: empty stdout + exit 0 = hook fired, no action.
    exit 0
}

printf '%s' "$RESULT"
exit 0

# ----------------------------------------------------------------------------
# §POLICY — Upgrading from WARN to BLOCK
# ----------------------------------------------------------------------------
# To make the hook blocking once the corpus is compliant, edit
# python-validate.py and change the `emit_warn()` function to emit a
# `"permissionDecision": "deny"` field (see Claude Code hooks docs). Until
# the live review set is fully canonical-compliant, blocking would wedge
# any edit touching a legacy script.
