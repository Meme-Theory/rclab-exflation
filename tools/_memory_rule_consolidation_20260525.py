#!/usr/bin/env python3
"""Memory-rule consolidation reference migration (2026-05-25).

Orchestrator memory's 49 feedback_*.md operating rules were consolidated to 12
canonical rules. This script repoints the LIVE rule-API references from the 46
absorbed names to their 12 survivors.

SCOPE: GLOBAL over the project root. The SHAs (audit_sha256 = closure_hash of an
input-pin-map; content_sha256 over gate content) are recorded hex literals checked
only for uniqueness (v3 sig_5), never recomputed-and-diffed against a file; renaming
a cited rule in a comment/provenance string changes no verdict, and nobody re-derives
a frozen script's SHA. So find/replace runs over ALL text files for full reference
consistency.

EXCLUDED: .git/; binaries (.db/.npz/.png/.jpg/.pyc/.pdf/.zip/.ico/.svg/.parquet);
*.bak rollback snapshots; tools/archive/ true backups; and this migration script
itself (it holds the old names as dict keys). The memory dir + its backup are outside
the project root and are not walked.
"""
from pathlib import Path

ROOT = Path(r"C:\sandbox\Ainulindale Exflation")

# old feedback stem (no .md) -> survivor stem (no .md). Matching the bare stem
# also catches the .md form and [[wikilink]] form.
MAP = {
    # -> dispatch-discipline
    "feedback_max-8-subagents": "feedback_dispatch-discipline",
    "feedback_batch-size-discrete": "feedback_dispatch-discipline",
    "feedback_autonomous-batch-dispatch": "feedback_dispatch-discipline",
    "feedback_workshop-autonomous-rolling": "feedback_dispatch-discipline",
    "feedback_dispatch-not-halt": "feedback_dispatch-discipline",
    "feedback_dispatch-duplicates": "feedback_dispatch-discipline",
    "feedback_resume-completed-agent-via-sendmessage": "feedback_dispatch-discipline",
    "feedback_agent-spawning": "feedback_dispatch-discipline",
    # -> no-asking-just-execute
    "feedback_autonomous-fix-no-asking": "feedback_no-asking-just-execute",
    "feedback_no-asking-housekeeping-fixes": "feedback_no-asking-just-execute",
    "feedback_wave-synthesis-no-asking": "feedback_no-asking-just-execute",
    "feedback_dont-relitigate-confirmed-decisions": "feedback_no-asking-just-execute",
    "feedback_trust-user-verify": "feedback_no-asking-just-execute",
    # -> fix-in-session-never-defer (kept; absorbs carry-forward-mandatory)
    "feedback_carry-forward-mandatory": "feedback_fix-in-session-never-defer",
    # -> max-effort-full-fidelity
    "feedback_never-limit-thinking": "feedback_max-effort-full-fidelity",
    "feedback_no-weak-models-for-complex-tasks": "feedback_max-effort-full-fidelity",
    "feedback_never-haiku-for-math": "feedback_max-effort-full-fidelity",
    "feedback_full-fidelity-prompts": "feedback_max-effort-full-fidelity",
    "feedback_no-line-count-requirements": "feedback_max-effort-full-fidelity",
    "feedback_execution-discipline": "feedback_max-effort-full-fidelity",
    # -> session-process
    "feedback_working-paper-shells-first": "feedback_session-process",
    "feedback_parallel-wp-write-token-bleed": "feedback_session-process",
    "feedback_large-wp-partition-by-size": "feedback_session-process",
    "feedback_wave-partition-respect-run-order": "feedback_session-process",
    "feedback_workshop-not-carry-forward-listing": "feedback_session-process",
    "feedback_compact-breaks-goals": "feedback_session-process",
    # -> reporting-framing
    "feedback_lcdm-matches": "feedback_reporting-framing",
    "feedback_inflation-flexibility": "feedback_reporting-framing",
    "feedback_pass-fail-ratio-not-metric": "feedback_reporting-framing",
    "feedback_plan-size-superlatives": "feedback_reporting-framing",
    "feedback_substrate-framing-corrections": "feedback_reporting-framing",
    "feedback_fabric-not-crystal": "feedback_reporting-framing",
    # -> agent-roster
    "feedback_agent-behavior": "feedback_agent-roster",
    "feedback_agent-memory-not-authoritative": "feedback_agent-roster",
    "feedback_adjudication-prompt-pattern": "feedback_agent-roster",
    "feedback_volovik-sharpest-reviewer": "feedback_agent-roster",
    "feedback_landau-undervalued": "feedback_agent-roster",
    # -> framework-hygiene
    "feedback_framework-folder-curated": "feedback_framework-hygiene",
    "feedback_evoi-table-maintenance": "feedback_framework-hygiene",
    "feedback_no-user-priority-elevation": "feedback_framework-hygiene",
    "feedback_preserve-anchor-keyed-audits": "feedback_framework-hygiene",
    # -> compute-environment
    "feedback_agents-never-use-gpu": "feedback_compute-environment",
    "feedback_no-cd-out-of-project-root": "feedback_compute-environment",
    "feedback_read-code-not-benchmark": "feedback_compute-environment",
    # -> research-corpus
    "feedback_no-training-knowledge-papers": "feedback_research-corpus",
    "feedback_collab-section6-table": "feedback_research-corpus",
}

# longest-first so no stem is rewritten by a shorter substring of another
ORDERED = sorted(MAP.items(), key=lambda kv: -len(kv[0]))

EXCLUDE_DIR_FRAGMENTS = ("/.git/", "/tools/archive/", "/memory-backup-")
EXCLUDE_SUFFIX = (".bak", ".db", ".npz", ".png", ".jpg", ".jpeg", ".gif",
                  ".pyc", ".pdf", ".zip", ".ico", ".svg", ".parquet", ".lock")
INCLUDE_SUFFIX = (".md", ".py", ".txt", ".sh", ".yaml", ".yml", ".json",
                  ".js", ".cfg", ".ini", ".toml", ".csv", ".jsonl")
SELF = Path(__file__).resolve()

def targets():
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if p.resolve() == SELF:
            continue  # this script holds the old names as dict keys
        sp = p.as_posix()
        if any(frag in sp for frag in EXCLUDE_DIR_FRAGMENTS):
            continue
        suf = p.suffix.lower()
        if suf in EXCLUDE_SUFFIX or suf not in INCLUDE_SUFFIX:
            continue
        yield p

def main():
    total_files, total_repl = 0, 0
    per_old = {k: 0 for k in MAP}
    changed = []
    for p in targets():
        try:
            text = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue
        new = text
        file_repl = 0
        for old, sub in ORDERED:
            c = new.count(old)
            if c:
                new = new.replace(old, sub)
                per_old[old] += c
                file_repl += c
        if new != text:
            p.write_text(new, encoding="utf-8")
            changed.append((str(p.relative_to(ROOT)), file_repl))
            total_files += 1
            total_repl += file_repl
    print(f"Files changed: {total_files}")
    print(f"Total replacements: {total_repl}")
    print("\nPer-old-name replacement counts (nonzero):")
    for old in sorted(per_old, key=lambda k: -per_old[k]):
        if per_old[old]:
            print(f"  {per_old[old]:5d}  {old} -> {MAP[old]}")
    print("\nChanged files:")
    for relp, c in sorted(changed, key=lambda x: -x[1]):
        print(f"  {c:4d}  {relp}")

if __name__ == "__main__":
    main()
