#!/usr/bin/env python3
"""Append W1-2 allowlist row + instances rationale (mechanical PRE-REG-INC closure)."""
import hashlib
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]  # (local) — repo-root resolver

# Compute plan-block SHA for §W1-2
text = (REPO_ROOT / 'sessions' / 'session-plan' / 'session-90-plan-w1.md').read_text(encoding='utf-8')
m = re.search(r'(## §W1-2\.[\s\S]*?)(?=\n## §W1-3\.)', text)
block = m.group(1) if m else ''
sha = hashlib.sha256(block.encode('utf-8')).hexdigest()
print('w1_2_plan_block_sha:', sha)

# Append allowlist row
allowlist = REPO_ROOT / '.claude' / 'rules' / 'methodology-wave-allowlist.md'
with allowlist.open('a', encoding='utf-8') as f:
    f.write(f'| W1-2 | S90 | {sha} |\n')

# Append instances rationale — concise, mechanical-closure pattern
rationale = (
    "\n\n### W1-2 (S90) — " + sha + "\n\n"
    "**Provenance**: gen-physicist orchestrator-direct-write under /rclab-solo on "
    "session-90-plan-w1.md §W1-2.\n"
    "**Gate**: `S90-CORNER-CLASSIFICATION-AUDIT-VII-U-2-EXTENSION` — mechanical "
    "PRE-REG-INC closure per `mechanical-closure-discipline.md`. Cross-wave prerequisite "
    "W2 CF-25 `S90-VII-U-2-CORNER-RECONCILIATION-READING-B-LOCK-IN` has NOT landed PASS at "
    "W1 dispatch time (user invoked /rclab-solo on W1 only; W2 is a separate dispatch). "
    "Plan §W1-2 #9 pre-registered INFO outcome for this scenario; emitted accordingly "
    "with full audit-trail value string naming the blocking prereq.\n\n"
    "**M1∧M2∧M3∧M4 conjunction**:\n"
    "- M1: artifact-existence-with-substantive-content per plan §9 — closure script "
    "`_s90_w1_2_mechanical_closure.py` exists (84 lines, non-stub) emitting honest PRE-REG-INC verdict.\n"
    "- M2: orchestrator-direct mechanical closure script under `computations/_shared/` (no numerical "
    "comparison threshold; INFO is the pre-registered outcome).\n"
    "- M3: source-of-truth = plan §W1-2 pre-registered threshold #9 (INFO iff W2 CF-25 NOT PASS).\n"
    f"- M4: this row appends gate-ID `W1-2` to `methodology-wave-allowlist.md` with sha={sha}.\n\n"
    "**Closure conditions** (per mechanical-closure-discipline.md §\"When mechanical closure IS "
    "acceptable\"): (1) upstream-block topology IS the cause; (2) verdict honesty INFO (not PASS); "
    "(3) per-gate-distinct audit_sha256 = "
    "`526a38d0baca18998d37aff5bd7512616efda575dabf8adb6d7d4854a99541a8` over W1-2-specific "
    "input-pin map; (4) audit-trail signature names blocking prereq verbatim; (5) WP update on "
    "next step.\n\n"
    "**Carry-forward**: deferred to S91 after W2 CF-25 "
    "`S90-VII-U-2-CORNER-RECONCILIATION-READING-B-LOCK-IN` lands PASS (or to a parallel W2 "
    "dispatch in current session). Audit-script extension cannot proceed without §VII.U.2 "
    "Reading-B-locked-in baseline.\n\n"
    "**Cross-link**: `sessions/session-plan/session-90-plan-w1.md` §W1-2 #5+#9 threshold; "
    "W2 CF-25 plan-block; `.claude/rules/mechanical-closure-discipline.md` §\"When mechanical "
    "closure IS acceptable\".\n"
)

instances = REPO_ROOT / 'sessions' / 'framework' / 'registry' / 'methodology-wave-instances.md'
with instances.open('a', encoding='utf-8') as f:
    f.write(rationale)
print('allowlist + instances appended for W1-2')
