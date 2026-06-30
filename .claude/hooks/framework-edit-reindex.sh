#!/usr/bin/env bash
# .claude/hooks/framework-edit-reindex.sh
#
# Phase 3 of the framework-ingestion fix: when a file under sessions/framework/
# is edited or written, trigger an incremental knowledge-index rebuild for THAT
# file, then emit a summary of how many entries the registry now contributes to
# each bucket. The framework folder is the capstone destination for knowledge;
# this hook closes the automation loop so edits flow straight into the index.
#
# Fires PostToolUse on Edit|Write|MultiEdit. Reads JSON tool_input from stdin.
# If tool_input.file_path is NOT under sessions/framework/*.md, exits silently.
# Otherwise runs `extract_entities.py --incremental --file <path>` and emits
# a blocking-style JSON with hookSpecificOutput.additionalContext summarizing
# the effect on the index.
#
# Exit 0 always: this is a visibility hook, not a gate.

set -u

PROJECT_ROOT="${CLAUDE_PROJECT_ROOT:-$PWD}"
VENV_PY="${PROJECT_ROOT}/phonon-exflation-sim/.venv312/Scripts/python.exe"

# Read tool_input JSON from stdin.
INPUT="$(cat || true)"

# Extract file_path using a python one-liner (jq is Windows-native and
# sometimes struggles with Windows paths in stdin).
FILE_PATH=""
if [ -x "${VENV_PY}" ]; then
  FILE_PATH="$(printf '%s' "${INPUT}" | "${VENV_PY}" -c \
    "import sys,json; print(json.loads(sys.stdin.read() or '{}').get('tool_input',{}).get('file_path',''))" \
    2>/dev/null || true)"
fi

# Normalize to forward slashes for path matching; strip trailing whitespace.
FILE_PATH_NORM="$(printf '%s' "${FILE_PATH}" | tr '\\' '/' | sed 's/[[:space:]]*$//')"

# Silent exit if not a framework .md file. Match both absolute paths
# (e.g. /c/sandbox/Ainulindale Exflation/sessions/framework/...) and
# project-relative paths (sessions/framework/...).
case "${FILE_PATH_NORM}" in
  */sessions/framework/*.md) : ;;
  sessions/framework/*.md) : ;;
  *) exit 0 ;;
esac

# Absolute path for the extractor (it expects relative-to-project-root or abs).
ABS_PATH="${FILE_PATH}"
if [ ! -f "${ABS_PATH}" ]; then
  # Try resolving relative to project root.
  ABS_PATH="${PROJECT_ROOT}/${FILE_PATH_NORM}"
fi
if [ ! -f "${ABS_PATH}" ]; then
  exit 0
fi

# Run incremental rebuild for just this file.
if [ ! -x "${VENV_PY}" ]; then
  printf '{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"[framework-reindex] venv Python missing; framework edit detected at %s but index not rebuilt."}}\n' "${FILE_PATH_NORM}"
  exit 0
fi

REINDEX_OUTPUT="$("${VENV_PY}" "${PROJECT_ROOT}/tools/extract_entities.py" \
                   --incremental --file "${ABS_PATH}" 2>&1 | tail -80 || true)"

# Pull the post-rebuild entry counts from the index for just this file.
SUMMARY="$("${VENV_PY}" - "${FILE_PATH_NORM}" <<'PY' 2>/dev/null || true
import json, sys, pathlib
# The index stores source_file project-relative (sessions/framework/...), but the
# hook may receive an ABSOLUTE file_path (the project's Write convention). Normalize
# both sides to the project-relative tail so the comparison is path-form-agnostic.
_marker = "sessions/framework/"
def _norm(p):
    p = (p or "").replace("\\", "/")
    return p[p.index(_marker):] if _marker in p else p
rel = _norm(sys.argv[1].strip())
idx_path = pathlib.Path("tools/knowledge-index.json")
if not idx_path.exists():
    print("index missing")
    sys.exit(0)
idx = json.loads(idx_path.read_text(encoding="utf-8"))
reg_hit = None
for r in idx.get("registries", []):
    if _norm(r.get("source_file")) == rel:
        reg_hit = r
        break
counts = {}
for bucket in ("theorems", "closed_mechanisms", "gates", "open_channels"):
    n = sum(
        1 for e in idx.get(bucket, [])
        if _norm(e.get("source_file")) == rel
    )
    if n:
        counts[bucket] = n
if reg_hit is None:
    print("registry meta-entry not found")
    sys.exit(0)
print(
    f"registry_id={reg_hit.get('registry_id')}  "
    f"title={(reg_hit.get('title') or '')[:60]}  "
    f"summary_rows={reg_hit.get('summary_row_count')}  "
    f"target_buckets={reg_hit.get('target_buckets')}  "
    f"entries_by_bucket={counts}  "
    f"consumer_gates={len(reg_hit.get('consumer_gates') or [])}"
)
PY
)"

# Emit the additionalContext JSON. PostToolUse uses hookSpecificOutput for
# narrative context; the `decision` field is omitted (exit 0, non-blocking).
CTX="[framework-reindex] ${FILE_PATH_NORM} re-indexed. ${SUMMARY}"
# Escape newlines/quotes for JSON embedding.
CTX_JSON="$(printf '%s' "${CTX}" | "${VENV_PY}" -c \
  "import sys,json; print(json.dumps(sys.stdin.read()))" 2>/dev/null || printf '"[framework-reindex] done"')"

printf '{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":%s}}\n' "${CTX_JSON}"
exit 0
