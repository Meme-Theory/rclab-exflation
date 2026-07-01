#!/bin/bash
# PreToolUse:TaskUpdate hook: retrospective verification at completion claim.
# Fires ONLY when tool_input.status=="completed". Other transitions pass silently.
# Also runs the §VII slot-allocation audit; the audit dump is hashed and emitted
# only on delta from the previous emission (identical findings → suppressed).

INPUT=$(cat)

PROJECT_ROOT="${CLAUDE_PROJECT_ROOT:-$(pwd)}"
PYBIN="${PROJECT_ROOT}/phonon-exflation-sim/.venv312/Scripts/python.exe"
if [ ! -x "$PYBIN" ]; then
  PYBIN="$(command -v python 2>/dev/null || command -v python3 2>/dev/null)"
fi
if [ -z "$PYBIN" ]; then exit 0; fi

NEW_STATUS=$(printf '%s' "$INPUT" | "$PYBIN" -c "
import json, sys
try:
    d = json.load(sys.stdin)
    print(d.get('tool_input', {}).get('status', ''))
except Exception:
    print('')
" 2>/dev/null)

if [ "$NEW_STATUS" != "completed" ]; then exit 0; fi

exec "$PYBIN" - <<'PYEOF'
import hashlib, json, os, subprocess, sys, tempfile

project_root = os.environ.get("CLAUDE_PROJECT_ROOT") or os.getcwd()
pybin = os.path.join(project_root, "phonon-exflation-sim", ".venv312", "Scripts", "python.exe")
if not os.path.isfile(pybin):
    pybin = sys.executable

audit_script = os.path.join(project_root, "computations", "_shared", "_vii_slot_allocation_audit.py")
audit_summary = ""

if os.path.isfile(audit_script):
    try:
        r = subprocess.run(
            [pybin, audit_script, "--json", "--quiet"],
            capture_output=True, text=True, timeout=30,
        )
        if r.returncode == 0 and r.stdout.strip():
            d = json.loads(r.stdout)
            verdict = d.get("verdict", "UNKNOWN")
            if verdict != "PASS":
                counts = d.get("counts", {})
                findings = d.get("findings", [])

                # Hash-cache: suppress repeat emission of identical findings.
                findings_blob = json.dumps(
                    {"verdict": verdict, "counts": counts, "findings": findings},
                    sort_keys=True,
                )
                findings_hash = hashlib.sha256(findings_blob.encode("utf-8")).hexdigest()[:16]
                hash_file = os.path.join(tempfile.gettempdir(), "vii-audit-last-hash.txt")

                last_hash = ""
                try:
                    if os.path.isfile(hash_file):
                        with open(hash_file, "r") as f:
                            last_hash = f.read().strip()
                except Exception:
                    pass

                if findings_hash == last_hash:
                    # Identical findings → emit a one-line note instead of full dump.
                    audit_summary = (
                        "\n\n[VII-AUDIT: {} findings unchanged from last emission; "
                        "full dump suppressed]".format(len(findings))
                    )
                else:
                    # Delta from last (or first emission) → full dump.
                    lines = [
                        "",
                        "==== VII-SLOT-AUDIT — verdict={} ====".format(verdict),
                        "Counts: B={} C={} D={} E={}".format(
                            counts.get("B_UNREGISTERED_RESERVATION", 0),
                            counts.get("C_COLLISION_DOUBLE_RESERVATION", 0),
                            counts.get("D_ORPHANED_TABLE_ENTRY", 0),
                            counts.get("E_REGISTRY_VS_TABLE_DRIFT", 0),
                        ),
                    ]
                    for f in findings[:10]:
                        lines.append("  [{}] {} — {}".format(
                            f.get("class", "?"), f.get("slot", "?"), f.get("detail", "")
                        ))
                    if len(findings) > 10:
                        lines.append("  ...and {} more.".format(len(findings) - 10))
                    if last_hash:
                        lines.append("(delta from previous emission)")
                    lines.append("Per CLAUDE.md No Technical Debt: fix in-session.")
                    audit_summary = "\n".join(lines)

                    try:
                        with open(hash_file, "w") as f:
                            f.write(findings_hash)
                    except Exception:
                        pass
    except Exception:
        pass

# Reminder brief removed 2026-05-28 (hook-relaxation per session-95-model-swap-meta-report.md §D):
# the COMPLETION-CLAIM nag + the >=15-line stub heuristic were Opus-4.7-era bandaids that
# contradict feedback_max-effort-full-fidelity.md ("verify by CONTENT, not line count"). This
# hook now emits ONLY the VII-slot-allocation audit (a real, delta-suppressed registry check),
# and only when that audit actually has findings.
if audit_summary.strip():
    result = {
        "suppressOutput": True,
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": audit_summary.lstrip("\n"),
        },
    }
    print(json.dumps(result))
PYEOF
