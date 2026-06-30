#!/usr/bin/env bash
# Diagnostic: timing for each audit stage.
set -u
PROJECT_ROOT="${CLAUDE_PROJECT_ROOT:-$PWD}"
VERDICT_FILE="${PROJECT_ROOT}/computations/session-84/s84_gate_verdicts.txt"
VENV_PY="${PROJECT_ROOT}/phonon-exflation-sim/.venv312/Scripts/python.exe"

echo "STAGE_0 start $(date +%s)"
[ -x "${VENV_PY}" ] && echo "  venv python: OK"
echo "STAGE_1 python probe $(date +%s)"
"${VENV_PY}" -c "print('ok')"
echo "STAGE_2 done probe $(date +%s)"

echo "STAGE_3 grep count $(date +%s)"
total=$(grep -cE '^[A-Z0-9][A-Z0-9-]+:[[:space:]]' "${VERDICT_FILE}" 2>/dev/null || echo 0)
echo "  total=${total} at $(date +%s)"

echo "STAGE_4 dual pattern $(date +%s)"
dual=$(grep -E '^[A-Z0-9][A-Z0-9-]+:[[:space:]]' "${VERDICT_FILE}" 2>/dev/null \
  | grep -c -E 'audit_sha256=[0-9a-f]{40,}.*content_sha256=[0-9a-f]{40,}|content_sha256=[0-9a-f]{40,}.*audit_sha256=[0-9a-f]{40,}' || echo 0)
echo "  dual=${dual} at $(date +%s)"

echo "STAGE_5 done $(date +%s)"
