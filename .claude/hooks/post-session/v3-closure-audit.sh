#!/usr/bin/env bash
# .claude/hooks/post-session/v3-closure-audit.sh
# S84 W9a-98 HOOK-INFRA — BLOCKING v3 ladder closure audit.
#
# POSTURE: BLOCKING. Exits 1 on verdict != CLOSED and != INFO.
# sig_1 VETO: sig_1 == 0 forces FAIL regardless of total score.
#
# Event wiring: Stop (session close) OR explicit /handoff invocation.
# Computes the 5 signals:
#   sig_1: _pru_cardinality_audit.py exists AND D_PRU_raw = 0  (w=4.000, VETO)
#   sig_2: every session verdict line carries audit_sha256= AND content_sha256=  (w=1.585)
#   sig_3: completion-queue.jsonl non-empty AND covers >= 80% of gates  (w=3.750)
#   sig_4: every S84 gate block carries schema_version R3  (w=1.000)
#   sig_5: all audit_sha256 values are unique across the verdict file  (w=1.000)
#
# Verdict:
#   CLOSED iff score >= CLOSED_THRESHOLD (10.202) AND sig_1 == 1
#   INFO   iff score >= INFO_THRESHOLD   (6.801)  AND sig_1 == 1
#   FAIL   otherwise  (includes sig_1 VETO)
#
# Writes: sessions/session-NN/v3_ladder_audit.json
# Argv: if $1 is provided, interpreted as session number (default: parse from
# CLAUDE_SESSION_ID or latest computations/session-{NN}/s{NN}_gate_verdicts.txt).

set -u

# Pinned machinery (PRDR).
LADDER_W1=4.000
LADDER_W2=1.585
LADDER_W3=3.750
LADDER_W4=1.000
LADDER_W5=1.000
CLOSED_THRESHOLD=10.202
INFO_THRESHOLD=6.801
SIG_3_COVERAGE_PCT=80

PROJECT_ROOT="${CLAUDE_PROJECT_ROOT:-$PWD}"
HOOK_LOG_DIR="${PROJECT_ROOT}/.claude/hooks/logs"
HOOK_QUEUE="${HOOK_LOG_DIR}/completion-queue.jsonl"

# Python resolution: prefer project venv. Windows has app-alias stubs
# (python/python3) that hang interactively; only probe real binaries.
PYBIN=""
VENV_PY="${PROJECT_ROOT}/phonon-exflation-sim/.venv312/Scripts/python.exe"
if [ -x "${VENV_PY}" ]; then
  PYBIN="${VENV_PY}"
fi
if [ -z "${PYBIN}" ]; then
  # Fallback — only if a real file (not a shim) exists on PATH.
  for cand in python3 python; do
    resolved="$(command -v "${cand}" 2>/dev/null || true)"
    # Skip Windows app-alias stubs in WindowsApps directory.
    case "${resolved}" in
      */WindowsApps/*) continue ;;
    esac
    if [ -n "${resolved}" ] && [ -x "${resolved}" ]; then
      PYBIN="${resolved}"
      break
    fi
  done
fi
if [ -z "${PYBIN}" ]; then
  echo "v3-closure-audit: ERROR — no usable Python found (venv path: ${VENV_PY})" >&2
  exit 1
fi

# Session number resolution.
SESSION_N="${1:-}"
if [ -z "${SESSION_N}" ]; then
  # Use most recent session verdict file by mtime.
  latest="$(ls -1t "${PROJECT_ROOT}/computations/session-"*/s[0-9]*_gate_verdicts.txt 2>/dev/null | head -1 || true)"
  if [ -n "${latest}" ]; then
    SESSION_N="$(basename "${latest}" | sed -E 's/^s([0-9]+)_gate_verdicts\.txt$/\1/' )"
  else
    SESSION_N="84"  # S84 default for this hook's era
  fi
fi

VERDICT_FILE="${PROJECT_ROOT}/computations/session-${SESSION_N}/s${SESSION_N}_gate_verdicts.txt"
SESSION_DIR="${PROJECT_ROOT}/sessions/session-${SESSION_N}"
AUDIT_OUT="${SESSION_DIR}/v3_ladder_audit.json"
PRU_SCRIPT="${PROJECT_ROOT}/computations/_shared/_pru_cardinality_audit.py"
PLAN_GLOB="${PROJECT_ROOT}/sessions/session-plan/session-${SESSION_N}-plan*.md"

mkdir -p "${SESSION_DIR}" 2>/dev/null || true

# ------------ Signal 1: PRU audit present AND D_PRU_raw = 0 ------------
sig_1=0
pru_reason="not-checked"
if [ -f "${PRU_SCRIPT}" ]; then
  # Look for the most recent PRU audit output in session dir.
  pru_out="$(ls -1t "${SESSION_DIR}/"_pru_cardinality_audit*.json 2>/dev/null | head -1 || true)"
  if [ -n "${pru_out}" ] && [ -f "${pru_out}" ]; then
    D_PRU_raw="$(cat "${pru_out}" 2>/dev/null | jq -r '.D_PRU_raw // .d_pru_raw // -1' 2>/dev/null || echo -1)"
    if [ "${D_PRU_raw}" = "0" ]; then
      sig_1=1
      pru_reason="D_PRU_raw=0 in ${pru_out}"
    else
      pru_reason="D_PRU_raw=${D_PRU_raw} in ${pru_out}"
    fi
  else
    pru_reason="script exists but no audit output found in ${SESSION_DIR}"
  fi
else
  pru_reason="missing: ${PRU_SCRIPT}"
fi

# ------------ Signal 2: every verdict line dual-SHA ------------
# Use single-pass grep counts; avoid per-line subshell fork storm on Windows.
sig_2=0
verdicts_total=0
verdicts_dual=0
verdicts_legacy=0
verdicts_malformed=0
if [ -f "${VERDICT_FILE}" ]; then
  # Lines that look like gate verdicts: start with UPPER-ALNUM token, then ":".
  # Exclude blank lines and comment (#) lines.
  verdicts_total=$(grep -cE '^[A-Z0-9][A-Z0-9-]+:[[:space:]]' "${VERDICT_FILE}" 2>/dev/null || echo 0)
  # Dual: line contains BOTH audit_sha256= and content_sha256= (each >=40 hex).
  verdicts_dual=$(grep -E '^[A-Z0-9][A-Z0-9-]+:[[:space:]]' "${VERDICT_FILE}" 2>/dev/null \
    | grep -c -E 'audit_sha256=[0-9a-f]{40,}.*content_sha256=[0-9a-f]{40,}|content_sha256=[0-9a-f]{40,}.*audit_sha256=[0-9a-f]{40,}' || echo 0)
  # Legacy: has single sha256= but NOT the dual pair.
  verdicts_legacy=$(grep -E '^[A-Z0-9][A-Z0-9-]+:[[:space:]]' "${VERDICT_FILE}" 2>/dev/null \
    | grep -E '(^| )sha256=[0-9a-f]{40,}' \
    | grep -v -E 'audit_sha256=[0-9a-f]{40,}.*content_sha256=[0-9a-f]{40,}' \
    | grep -v -E 'content_sha256=[0-9a-f]{40,}.*audit_sha256=[0-9a-f]{40,}' \
    | wc -l || echo 0)
  verdicts_malformed=$((verdicts_total - verdicts_dual - verdicts_legacy))
  if [ "${verdicts_malformed}" -lt 0 ]; then verdicts_malformed=0; fi
  if [ "${verdicts_total}" -gt 0 ] && [ "${verdicts_dual}" = "${verdicts_total}" ]; then
    sig_2=1
  fi
fi

# ------------ Signal 3: completion-queue coverage >= 80% ------------
sig_3=0
queue_lines=0
covered_gates=0
gate_count_from_verdicts=0
if [ -f "${HOOK_QUEUE}" ]; then
  queue_lines="$(wc -l < "${HOOK_QUEUE}" 2>/dev/null || echo 0)"
fi
if [ -f "${VERDICT_FILE}" ]; then
  gate_count_from_verdicts="$(grep -cE '^[A-Z0-9][A-Z0-9-]+:' "${VERDICT_FILE}" 2>/dev/null || echo 0)"
fi
if [ "${queue_lines}" -gt 0 ] && [ -f "${VERDICT_FILE}" ]; then
  # Extract gate_ids from both files, intersect.
  # Use deterministic paths under /tmp (mingw) to avoid any mktemp path
  # surprises with Windows-native jq / comm.
  tmp_gates_verdict="/tmp/v3_verdict_gates.$$"
  tmp_gates_queue="/tmp/v3_queue_gates.$$"
  # jq is Windows-native on mingw; feed file contents via stdin so it
  # doesn't try to resolve /c/... paths it cannot parse.
  grep -oE '^[A-Z0-9][A-Z0-9-]+:' "${VERDICT_FILE}" 2>/dev/null | sed 's/:$//' | tr -d '\r' | sort -u > "${tmp_gates_verdict}" || true
  cat "${HOOK_QUEUE}" 2>/dev/null | jq -r '.gate_id // empty' 2>/dev/null | tr -d '\r' | sort -u > "${tmp_gates_queue}" || true
  # Verify both files are non-empty before comm.
  if [ -s "${tmp_gates_verdict}" ] && [ -s "${tmp_gates_queue}" ]; then
    covered_gates="$(comm -12 "${tmp_gates_verdict}" "${tmp_gates_queue}" 2>/dev/null | wc -l || echo 0)"
  fi
  rm -f "${tmp_gates_verdict}" "${tmp_gates_queue}" 2>/dev/null || true
fi
# Compute coverage pct via python for numeric stability.
sig_3_pct=0
if [ "${gate_count_from_verdicts}" -gt 0 ]; then
  sig_3_pct="$("${PYBIN}" -c "print(int(round(100.0 * ${covered_gates} / ${gate_count_from_verdicts})))" 2>/dev/null || echo 0)"
  if [ "${sig_3_pct}" -ge "${SIG_3_COVERAGE_PCT}" ]; then
    sig_3=1
  fi
fi

# ------------ Signal 4: every S84 gate block schema_version R3 ------------
sig_4=0
plan_gate_total=0
plan_gate_r3=0
for plan_file in ${PLAN_GLOB}; do
  [ -f "${plan_file}" ] || continue
  # Gate blocks begin with '### Gate ID' in prose plans (pre-YAML-adoption marker).
  gb="$(grep -c '^### Gate ID' "${plan_file}" 2>/dev/null || echo 0)"
  r3="$(grep -cE '^(schema_version:[[:space:]]*"?R3"?|[[:space:]]+schema_version:[[:space:]]*"?R3"?)' "${plan_file}" 2>/dev/null || echo 0)"
  plan_gate_total=$((plan_gate_total + gb))
  plan_gate_r3=$((plan_gate_r3 + r3))
done
# R3 adoption is partial (S84 W9a-100 is the migration gate). Credit sig_4 only
# when plan_gate_r3 >= plan_gate_total AND plan_gate_total > 0.
if [ "${plan_gate_total}" -gt 0 ] && [ "${plan_gate_r3}" -ge "${plan_gate_total}" ]; then
  sig_4=1
fi

# ------------ Signal 5: audit_sha256 uniqueness ------------
sig_5=0
audit_shas_total=0
audit_shas_unique=0
if [ -f "${VERDICT_FILE}" ]; then
  audit_shas_total="$(grep -oE 'audit_sha256=[0-9a-f]{40,}' "${VERDICT_FILE}" 2>/dev/null | wc -l || echo 0)"
  audit_shas_unique="$(grep -oE 'audit_sha256=[0-9a-f]{40,}' "${VERDICT_FILE}" 2>/dev/null | sort -u | wc -l || echo 0)"
  if [ "${audit_shas_total}" = "${audit_shas_unique}" ] && [ "${audit_shas_total}" -gt 0 ]; then
    sig_5=1
  fi
fi

# ------------ Signal 5 — allowlist-aware refinement (S86 W0b-5) ------------
# Invoke _dual_sha_uniqueness_audit.py to distinguish by-design re-emissions
# (REFRAME / logspace_fix / regex_fix) from SHA-hardcoding bugs. The audit
# writes a JSON; we surface sig_5_overall to the audit-summary stdout. Per
# plan W0b-5: do NOT exit non-zero on sig_5_overall = FAIL (the v3-closure
# controller decides remediation; this hook only reports).
DUAL_SHA_AUDIT_SCRIPT="${PROJECT_ROOT}/computations/_shared/_dual_sha_uniqueness_audit.py"
DUAL_SHA_ALLOWLIST="${PROJECT_ROOT}/computations/_shared/_dual_sha_allowlist.json"
DUAL_SHA_OUT="${SESSION_DIR}/sig_5_audit.json"
sig_5_allowlist_overall="not-checked"
sig_5_allowed=0
sig_5_forbidden=0
if [ -f "${DUAL_SHA_AUDIT_SCRIPT}" ] && [ -f "${DUAL_SHA_ALLOWLIST}" ] && [ -f "${VERDICT_FILE}" ]; then
  "${PYBIN}" "${DUAL_SHA_AUDIT_SCRIPT}" \
    --session "${SESSION_N}" \
    --verdict-file "${VERDICT_FILE}" \
    --allowlist-file "${DUAL_SHA_ALLOWLIST}" \
    --output "${DUAL_SHA_OUT}" >/dev/null 2>&1 || true
  if [ -f "${DUAL_SHA_OUT}" ]; then
    sig_5_allowlist_overall="$(jq -r '.sig_5_overall // "missing"' "${DUAL_SHA_OUT}" 2>/dev/null || echo "missing")"
    sig_5_allowed="$(jq -r '.allowed_duplicate_count // 0' "${DUAL_SHA_OUT}" 2>/dev/null || echo 0)"
    sig_5_forbidden="$(jq -r '.forbidden_duplicate_count // 0' "${DUAL_SHA_OUT}" 2>/dev/null || echo 0)"
  fi
fi

# ------------ Iterate-to-honesty vs iterate-until-PASS detection (S86 W-11 AUDIT-2; T2-12) ------------
#
# W-11 AUDIT-2 (S86 housekeeping T2-12): when the same gate ID has multiple
# verdict lines in the file, distinguish:
#   - iterate-to-honesty (LEGITIMATE): later verdict is PASS->INFO or PASS->FAIL
#     OR the later verdict adds qualification (composite tuple) without
#     loosening the verdict. Example: W-11 verdict file contains BOTH a PASS
#     line (audit_sha = 8f6d31b7...) and an INFO line (audit_sha = 9c3a5bca...)
#     for S86-W-11-ETA-GV-JOINT-PROBE; INFO supersedes PASS as the agent
#     recognizes the literal threshold tested the wrong hypothesis.
#   - iterate-until-PASS (Class-2 PROHIBITED per v3-closure-recovery.md):
#     later verdict is FAIL->PASS with looser threshold or different convention.
#
# This audit is INFORMATIONAL (sig_6 not part of the 5-signal ladder score).
# Output appears in v3_ladder_audit.json under diagnostics.iterate_pattern.
iterate_to_honesty_count=0
iterate_until_pass_count=0
iterate_pattern_overall="not-checked"
if [ -f "${VERDICT_FILE}" ]; then
  # Extract gate_ids that appear more than once (duplicate gate IDs).
  tmp_dup_gates="/tmp/v3_dup_gates.$$"
  grep -oE '^[A-Z0-9][A-Z0-9-]+:' "${VERDICT_FILE}" 2>/dev/null \
    | sed 's/:$//' | tr -d '\r' | sort | uniq -d > "${tmp_dup_gates}" || true
  if [ -s "${tmp_dup_gates}" ]; then
    while IFS= read -r gid; do
      [ -z "${gid}" ] && continue
      # Get all verdict lines for this gate_id IN ORDER (file-order = timestamp-order
      # by append-only convention).
      verdict_seq="$(grep -E "^${gid}:" "${VERDICT_FILE}" 2>/dev/null \
        | grep -oE ' (PASS|FAIL|INFO)' | tr -d ' ' | tr '\n' '|' || true)"
      # Drop trailing pipe.
      verdict_seq="${verdict_seq%|}"
      # Iterate-to-honesty patterns: PASS|INFO, PASS|FAIL, PASS|INFO|FAIL, etc.
      # (later verdict tightens / qualifies / supersedes earlier PASS).
      # Iterate-until-PASS patterns: FAIL|PASS, INFO|PASS (later verdict claims
      # PASS after earlier non-PASS — Class-2 PROHIBITED).
      case "${verdict_seq}" in
        PASS\|INFO|PASS\|FAIL|PASS\|INFO\|FAIL|PASS\|FAIL\|INFO|INFO\|FAIL|PASS\|PASS\|INFO|PASS\|PASS\|FAIL)
          iterate_to_honesty_count=$((iterate_to_honesty_count + 1))
          ;;
        FAIL\|PASS|INFO\|PASS|FAIL\|INFO\|PASS|FAIL\|FAIL\|PASS|INFO\|INFO\|PASS)
          iterate_until_pass_count=$((iterate_until_pass_count + 1))
          ;;
        *)
          # PASS|PASS or INFO|INFO or FAIL|FAIL or other neutral re-emissions.
          # Could be by-design (reframe / logspace_fix) — handled by sig_5
          # allowlist; not classified here.
          ;;
      esac
    done < "${tmp_dup_gates}"
  fi
  rm -f "${tmp_dup_gates}" 2>/dev/null || true
  # Overall classification: PROHIBITED if any iterate-until-PASS detected;
  # WARN if iterate-to-honesty detected (informational); CLEAN otherwise.
  if [ "${iterate_until_pass_count}" -gt 0 ]; then
    iterate_pattern_overall="PROHIBITED-CLASS-2-DETECTED"
  elif [ "${iterate_to_honesty_count}" -gt 0 ]; then
    iterate_pattern_overall="ITERATE-TO-HONESTY-PRESENT"
  else
    iterate_pattern_overall="CLEAN"
  fi
fi

# ------------ §VII slot-allocation audit (informational side-show; S86 W1a) ------------
# Invoke _vii_slot_allocation_audit.py at session-end after all per-task edits
# have settled. Does NOT contribute to the ladder score — the per-task
# TASK-UPDATE-RETROSPECTIVE.sh hook is the enforcement path; this captures
# the final-state audit result for the v3_ladder_audit.json record.
VII_AUDIT_SCRIPT="${PROJECT_ROOT}/computations/_shared/_vii_slot_allocation_audit.py"
VII_AUDIT_OUT="${SESSION_DIR}/vii_slot_allocation_audit.json"
vii_verdict="not-checked"
vii_findings_count=0
vii_classA=0
vii_classB=0
vii_classC=0
vii_classD=0
vii_classE=0
vii_audit_sha256=""
if [ -f "${VII_AUDIT_SCRIPT}" ] && [ -x "${PYBIN}" ]; then
  # Windows-native python.exe cannot parse MINGW-style script paths (/c/sandbox/...);
  # convert to native form via cygpath when available (fallback: sed-based conversion).
  if command -v cygpath >/dev/null 2>&1; then
    vii_script_native="$(cygpath -w "${VII_AUDIT_SCRIPT}")"
  else
    vii_script_native="$(echo "${VII_AUDIT_SCRIPT}" | sed -E 's|^/([a-zA-Z])/|\1:/|; s|/|\\|g')"
  fi
  vii_audit_json="$("${PYBIN}" "${vii_script_native}" --json --quiet 2>/dev/null || echo '{}')"
  if [ -n "${vii_audit_json}" ] && [ "${vii_audit_json}" != "{}" ]; then
    printf '%s\n' "${vii_audit_json}" > "${VII_AUDIT_OUT}" 2>/dev/null || true
    vii_verdict="$(printf '%s' "${vii_audit_json}" | jq -r '.verdict // "unknown"' 2>/dev/null || echo "unknown")"
    vii_findings_count="$(printf '%s' "${vii_audit_json}" | jq -r '(.findings | length) // 0' 2>/dev/null || echo 0)"
    vii_classA="$(printf '%s' "${vii_audit_json}" | jq -r '.counts.A_REGISTERED_AND_MATCHED // 0' 2>/dev/null || echo 0)"
    vii_classB="$(printf '%s' "${vii_audit_json}" | jq -r '.counts.B_UNREGISTERED_RESERVATION // 0' 2>/dev/null || echo 0)"
    vii_classC="$(printf '%s' "${vii_audit_json}" | jq -r '.counts.C_COLLISION_DOUBLE_RESERVATION // 0' 2>/dev/null || echo 0)"
    vii_classD="$(printf '%s' "${vii_audit_json}" | jq -r '.counts.D_ORPHANED_TABLE_ENTRY // 0' 2>/dev/null || echo 0)"
    vii_classE="$(printf '%s' "${vii_audit_json}" | jq -r '.counts.E_REGISTRY_VS_TABLE_DRIFT // 0' 2>/dev/null || echo 0)"
    vii_audit_sha256="$(printf '%s' "${vii_audit_json}" | jq -r '.audit_sha256 // ""' 2>/dev/null || echo "")"
  fi
fi

# ------------ Ladder score + verdict ------------
score="$("${PYBIN}" -c "print(${LADDER_W1}*${sig_1} + ${LADDER_W2}*${sig_2} + ${LADDER_W3}*${sig_3} + ${LADDER_W4}*${sig_4} + ${LADDER_W5}*${sig_5})" 2>/dev/null || echo 0.0)"

# VETO rule: sig_1 = 0 forces FAIL.
if [ "${sig_1}" = "0" ]; then
  VERDICT="FAIL"
  veto_fired=1
else
  veto_fired=0
  ge_closed="$("${PYBIN}" -c "print(1 if float('${score}') >= float('${CLOSED_THRESHOLD}') else 0)" 2>/dev/null || echo 0)"
  ge_info="$("${PYBIN}"   -c "print(1 if float('${score}') >= float('${INFO_THRESHOLD}')   else 0)" 2>/dev/null || echo 0)"
  if [ "${ge_closed}" = "1" ]; then
    VERDICT="CLOSED"
  elif [ "${ge_info}" = "1" ]; then
    VERDICT="INFO"
  else
    VERDICT="FAIL"
  fi
fi

# ------------ Emit v3_ladder_audit.json ------------
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
AUDIT_JSON="$(jq -n \
  --arg ts "${TS}" \
  --arg session "${SESSION_N}" \
  --arg verdict "${VERDICT}" \
  --argjson score "${score}" \
  --argjson closed_thresh "${CLOSED_THRESHOLD}" \
  --argjson info_thresh "${INFO_THRESHOLD}" \
  --argjson sig_1 "${sig_1}" \
  --argjson sig_2 "${sig_2}" \
  --argjson sig_3 "${sig_3}" \
  --argjson sig_4 "${sig_4}" \
  --argjson sig_5 "${sig_5}" \
  --argjson veto "${veto_fired}" \
  --argjson verdicts_total "${verdicts_total}" \
  --argjson verdicts_dual "${verdicts_dual}" \
  --argjson verdicts_legacy "${verdicts_legacy}" \
  --argjson verdicts_malformed "${verdicts_malformed}" \
  --argjson queue_lines "${queue_lines}" \
  --argjson covered_gates "${covered_gates}" \
  --argjson gate_count_from_verdicts "${gate_count_from_verdicts}" \
  --argjson sig_3_pct "${sig_3_pct}" \
  --argjson plan_gate_total "${plan_gate_total}" \
  --argjson plan_gate_r3 "${plan_gate_r3}" \
  --argjson audit_shas_total "${audit_shas_total}" \
  --argjson audit_shas_unique "${audit_shas_unique}" \
  --arg sig_5_allowlist_overall "${sig_5_allowlist_overall}" \
  --argjson sig_5_allowed "${sig_5_allowed}" \
  --argjson sig_5_forbidden "${sig_5_forbidden}" \
  --arg pru_reason "${pru_reason}" \
  --arg vii_verdict "${vii_verdict}" \
  --argjson vii_findings_count "${vii_findings_count}" \
  --argjson vii_classA "${vii_classA}" \
  --argjson vii_classB "${vii_classB}" \
  --argjson vii_classC "${vii_classC}" \
  --argjson vii_classD "${vii_classD}" \
  --argjson vii_classE "${vii_classE}" \
  --arg vii_audit_sha256 "${vii_audit_sha256}" \
  --arg iterate_pattern_overall "${iterate_pattern_overall}" \
  --argjson iterate_to_honesty_count "${iterate_to_honesty_count}" \
  --argjson iterate_until_pass_count "${iterate_until_pass_count}" \
  '{
     ts: $ts,
     session: $session,
     verdict: $verdict,
     score: $score,
     thresholds: { closed: $closed_thresh, info: $info_thresh },
     weights: {w1: 4.000, w2: 1.585, w3: 3.750, w4: 1.000, w5: 1.000},
     signals: {sig_1: $sig_1, sig_2: $sig_2, sig_3: $sig_3, sig_4: $sig_4, sig_5: $sig_5},
     veto_fired_sig_1: $veto,
     diagnostics: {
       pru: {sig_1: $sig_1, reason: $pru_reason},
       sha: {total: $verdicts_total, dual: $verdicts_dual, legacy: $verdicts_legacy, malformed: $verdicts_malformed},
       coverage: {queue_lines: $queue_lines, covered_gates: $covered_gates,
                  verdict_gate_count: $gate_count_from_verdicts, pct: $sig_3_pct,
                  threshold_pct: 80},
       r3: {plan_gate_total: $plan_gate_total, plan_gate_r3: $plan_gate_r3},
       uniqueness: {audit_shas_total: $audit_shas_total, audit_shas_unique: $audit_shas_unique},
       sig_5_allowlist: {overall: $sig_5_allowlist_overall, allowed_duplicates: $sig_5_allowed, forbidden_duplicates: $sig_5_forbidden},
       vii_slot_allocation: {
         verdict: $vii_verdict,
         findings_count: $vii_findings_count,
         counts: {classA_registered: $vii_classA, classB_unregistered: $vii_classB, classC_collision: $vii_classC, classD_orphaned: $vii_classD, classE_drift: $vii_classE},
         audit_sha256: $vii_audit_sha256,
         note: "informational side-show; per-task enforcement at TASK-UPDATE-RETROSPECTIVE.sh; does not affect ladder score"
       },
       iterate_pattern: {
         overall: $iterate_pattern_overall,
         iterate_to_honesty_count: $iterate_to_honesty_count,
         iterate_until_pass_count: $iterate_until_pass_count,
         note: "S86 W-11 AUDIT-2 / T2-12. Distinguishes iterate-to-honesty (PASS->INFO/FAIL with later timestamp; LEGITIMATE) from iterate-until-PASS (FAIL/INFO->PASS later timestamp; PROHIBITED Class-2). Informational only; does not affect ladder score. Inspect verdict file by hand if PROHIBITED-CLASS-2-DETECTED appears."
       }
     }
   }')"

# Atomic write (single open/close, no read-modify-truncate on a shared file).
printf '%s\n' "${AUDIT_JSON}" > "${AUDIT_OUT}" 2>/dev/null || {
  echo "ERROR: could not write ${AUDIT_OUT}" >&2
  exit 1
}

echo "v3-closure-audit: session=${SESSION_N} verdict=${VERDICT} score=${score} sig_1=${sig_1} sig_2=${sig_2} sig_3=${sig_3} sig_4=${sig_4} sig_5=${sig_5} -> ${AUDIT_OUT}"
echo "v3-closure-audit: sig_5_allowlist=${sig_5_allowlist_overall} allowed=${sig_5_allowed} forbidden=${sig_5_forbidden} -> ${DUAL_SHA_OUT}"
echo "v3-closure-audit: vii_slot_allocation=${vii_verdict} A=${vii_classA} B=${vii_classB} C=${vii_classC} D=${vii_classD} E=${vii_classE} findings=${vii_findings_count} -> ${VII_AUDIT_OUT}"
echo "v3-closure-audit: iterate_pattern=${iterate_pattern_overall} to_honesty=${iterate_to_honesty_count} until_pass=${iterate_until_pass_count}"

# ------------ Framework-registry rectification diff (non-blocking) ------------
# Phase 3 of the framework-ingestion fix: before session close, run the
# framework_diff.py rectification report. The diff is INFORMATIONAL (does not
# affect the v3 verdict) — warrants are flagged for the user to investigate,
# but the framework folder's authority is already enforced at ingest time via
# priority-7 dedup. A warrant means a session file's value disagrees with the
# framework-canonical value; the user decides whether to update the session
# file or supersede the framework entry.
FRAMEWORK_DIFF_SCRIPT="${PROJECT_ROOT}/tools/framework_diff.py"
if [ -f "${FRAMEWORK_DIFF_SCRIPT}" ]; then
  FW_OUT="$("${PYBIN}" "${FRAMEWORK_DIFF_SCRIPT}" --quiet 2>&1 || true)"
  # Parse the report for the warrant total; emit a one-liner summary.
  REPORT="${PROJECT_ROOT}/tools/framework_diff_report.md"
  if [ -f "${REPORT}" ]; then
    FW_WARRANTS="$(grep -E '^\*\*Total WARRANTs.*\*\*:' "${REPORT}" 2>/dev/null | sed -E 's/.*: ([0-9]+).*/\1/' || echo ?)"
    echo "framework-diff: warrants=${FW_WARRANTS} -> ${REPORT#${PROJECT_ROOT}/}"
  else
    echo "framework-diff: skipped (report not written)"
  fi
else
  echo "framework-diff: tool not present at ${FRAMEWORK_DIFF_SCRIPT#${PROJECT_ROOT}/}"
fi

# BLOCKING exit discipline.
if [ "${VERDICT}" = "CLOSED" ] || [ "${VERDICT}" = "INFO" ]; then
  exit 0
else
  echo "v3-closure-audit: BLOCKING — verdict=${VERDICT}. /handoff is blocked until remediated." >&2
  exit 1
fi
