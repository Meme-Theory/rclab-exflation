#!/usr/bin/env bash
# .claude/hooks/post-agent/completion-verify.sh
# S84 W9a-98 HOOK-INFRA — ADVISORY post-Agent completion verifier.
#
# POSTURE: ADVISORY. Exits 0 regardless of findings. Writes one JSONL line
# to .claude/hooks/logs/completion-queue.jsonl per Agent completion so the
# post-session v3 closure audit (sig_3) has artifact-existence evidence.
#
# Event wiring: PostToolUse, matcher="Agent".
# Stdin (claude-code convention): JSON with tool_use info. ENV vars passed:
#   CLAUDE_SESSION_ID, CLAUDE_PROJECT_ROOT (if available).
#
# This hook intentionally avoids prompt-text regex when possible; instead it
# reads the Agent's output_file (JSONL transcript) and checks any
# "ARTIFACTS PROMISED" block for literal path tokens, then runs stat / wc -l.
#
# Fail-soft: every branch exits 0. Any internal error is swallowed into the
# advisory_status field of the JSONL line so the post-session auditor can
# still see that the hook fired.

# ADVISORY posture: be maximally lenient. Missing variables / failed subcommands
# must not raise exit>0. Do NOT set -e or -u here.
HOOK_LOG_DIR="${CLAUDE_PROJECT_ROOT:-$PWD}/.claude/hooks/logs"
HOOK_QUEUE="${HOOK_LOG_DIR}/completion-queue.jsonl"
mkdir -p "${HOOK_LOG_DIR}" 2>/dev/null || true

# Harvest input JSON. On mingw, jq is Windows-native and cannot read MSYS /tmp
# paths. Store stdin in a variable and pipe into jq via stdin instead.
if [ -t 0 ]; then
  STDIN_JSON='{}'
else
  STDIN_JSON="$(cat 2>/dev/null || echo '{}')"
  [ -z "${STDIN_JSON}" ] && STDIN_JSON='{}'
fi

# Best-effort extraction. Missing keys become ""; never fail.
AGENT_ID="$(printf '%s' "${STDIN_JSON}" | jq -r '.tool_use_id // .tool_call_id // "unknown"' 2>/dev/null)"
[ -z "${AGENT_ID}" ] && AGENT_ID="unknown"
OUTPUT_FILE="$(printf '%s' "${STDIN_JSON}" | jq -r '.tool_result.output_file // .output_file // ""' 2>/dev/null)"
PROMPT_TEXT="$(printf '%s' "${STDIN_JSON}" | jq -r '.tool_input.prompt // .tool_input.description // ""' 2>/dev/null)"
SESSION_ID="${CLAUDE_SESSION_ID:-unknown}"
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# Recover gate_id from prompt text (first regex match of S##-... token).
GATE_ID="$(printf '%s' "${PROMPT_TEXT}" | grep -oE 'S[0-9]+-[A-Z0-9][A-Z0-9-]+' | head -1 || true)"
[ -z "${GATE_ID:-}" ] && GATE_ID="unknown"

# Extract ARTIFACTS PROMISED block (if present) for path tokens.
ARTIFACTS_RAW="$(printf '%s' "${PROMPT_TEXT}" \
  | awk 'BEGIN{p=0} /ARTIFACTS PROMISED/{p=1; next} p && /^$/{exit} p{print}' 2>/dev/null || true)"

# Pull out candidate file paths. Accept lines in common bullet forms:
#   - path/to/file.ext
#   * path/to/file.ext
#   `path/to/file.ext`
#   "path/to/file.ext"
# And absolute: /path/..., C:\path\...
declare -a TARGETS
TARGETS=()
while IFS= read -r line; do
  [ -z "${line}" ] && continue
  # Strip leading bullet / whitespace / backtick / quote.
  cleaned="$(printf '%s' "${line}" | sed -E 's/^[[:space:]]*[-*][[:space:]]*//; s/^[[:space:]]*//' 2>/dev/null)"
  # Split on whitespace; first non-empty token is the candidate path.
  for tok in ${cleaned}; do
    # Strip wrapping backticks/quotes.
    tok="${tok//\`/}"
    tok="${tok//\"/}"
    tok="${tok//\'/}"
    # Strip trailing punctuation.
    tok="${tok%%[,;:]}"
    # Must contain a slash OR a backslash (is a path), have a dot (has ext), no scheme.
    case "${tok}" in
      http*|*://*|''|.|..) continue ;;
    esac
    case "${tok}" in
      */*|*\\*)
        case "${tok}" in
          *.*) TARGETS+=("${tok}"); break ;;
        esac
        ;;
    esac
  done
done <<< "${ARTIFACTS_RAW}"

# Existence + length checks.
EXISTENCE_JSON='[]'
LENGTH_JSON='[]'
RED_COUNT=0
YELLOW_COUNT=0
GREEN_COUNT=0
TOTAL="${#TARGETS[@]}"
[ -z "${TOTAL}" ] && TOTAL=0

if [ "${TOTAL}" -gt 0 ]; then
  for t in "${TARGETS[@]}"; do
    # Normalize: strip trailing punctuation.
    tn="${t%%[,;:]}"
    # Path resolution: relative to project root if not absolute.
    case "${tn}" in
      /*|[A-Za-z]:*) full="${tn}" ;;
      *) full="${CLAUDE_PROJECT_ROOT:-$PWD}/${tn}" ;;
    esac
    if [ -f "${full}" ]; then
      sz="$(wc -c < "${full}" 2>/dev/null || echo 0)"
      ln="$(wc -l < "${full}" 2>/dev/null || echo 0)"
      if [ "${sz}" -gt 0 ] && [ "${ln}" -ge 15 ]; then
        GREEN_COUNT=$((GREEN_COUNT+1))
      elif [ "${sz}" -gt 0 ]; then
        YELLOW_COUNT=$((YELLOW_COUNT+1))
      else
        RED_COUNT=$((RED_COUNT+1))
      fi
      EXISTENCE_JSON="$(printf '%s' "${EXISTENCE_JSON}" | jq --arg p "${tn}" '. + [{path: $p, exists: true}]' 2>/dev/null || echo "${EXISTENCE_JSON}")"
      LENGTH_JSON="$(printf '%s' "${LENGTH_JSON}" | jq --arg p "${tn}" --argjson s "${sz}" --argjson l "${ln}" '. + [{path: $p, bytes: $s, lines: $l}]' 2>/dev/null || echo "${LENGTH_JSON}")"
    else
      RED_COUNT=$((RED_COUNT+1))
      EXISTENCE_JSON="$(printf '%s' "${EXISTENCE_JSON}" | jq --arg p "${tn}" '. + [{path: $p, exists: false}]' 2>/dev/null || echo "${EXISTENCE_JSON}")"
    fi
  done
fi

# Advisory status rule (ADVISORY posture only; exit code always 0).
if [ "${TOTAL}" -eq 0 ]; then
  STATUS="YELLOW"  # no ARTIFACTS PROMISED block parsed
elif [ "${RED_COUNT}" -gt 0 ]; then
  STATUS="RED"
elif [ "${YELLOW_COUNT}" -gt 0 ]; then
  STATUS="YELLOW"
else
  STATUS="GREEN"
fi

# Emit one JSONL line (atomic single append; no truncate-rewrite).
LINE="$(jq -nc \
  --arg agent_id "${AGENT_ID}" \
  --arg session_id "${SESSION_ID}" \
  --arg gate_id "${GATE_ID}" \
  --arg ts "${TS}" \
  --arg status "${STATUS}" \
  --arg output_file "${OUTPUT_FILE}" \
  --argjson existence "${EXISTENCE_JSON}" \
  --argjson length "${LENGTH_JSON}" \
  --argjson total "${TOTAL}" \
  --argjson green "${GREEN_COUNT}" \
  --argjson yellow "${YELLOW_COUNT}" \
  --argjson red "${RED_COUNT}" \
  '{agent_id: $agent_id, session_id: $session_id, gate_id: $gate_id, ts: $ts,
    write_targets_total: $total, existence_checks: $existence, length_checks: $length,
    green: $green, yellow: $yellow, red: $red,
    advisory_status: $status, output_file: $output_file}' 2>/dev/null || \
  printf '{"agent_id":"%s","gate_id":"%s","ts":"%s","advisory_status":"ERROR"}' \
    "${AGENT_ID}" "${GATE_ID}" "${TS}")"

# Atomic append. Single open("a") write. No read-modify-truncate.
printf '%s\n' "${LINE}" >> "${HOOK_QUEUE}" 2>/dev/null || true

exit 0
