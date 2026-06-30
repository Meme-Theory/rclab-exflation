"""Build format_generations.py by composing from the 4 source files.

One-shot consolidator. Run once, then delete this file.
"""
import re
from pathlib import Path

tools = Path(__file__).resolve().parent
archive = tools / 'archive'

regex_set = (tools / '_format_generation_regex_set.py').read_text(encoding='utf-8')
scan_src   = (tools / '_format_generation_scan.py').read_text(encoding='utf-8')
dryrun_src = (tools / '_format_generation_dry_run.py').read_text(encoding='utf-8')
zerocov_src = (archive / '_format_generation_zero_coverage.py').read_text(encoding='utf-8')

# --- regex_set body: strip trailing __main__ block ---
m = re.search(r'\nif __name__ == "__main__":', regex_set)
assert m, "regex_set: no __main__ block found"
regex_set_body = regex_set[:m.start()].rstrip() + '\n\n'

# --- scan body: anchor + main→run_scan + AGENT_NAMES→SCAN_AGENT_NAMES ---
m = re.search(r'\n# Agent identifiers seen in the project\.', scan_src)
assert m, "scan: anchor not found"
scan_body = scan_src[m.start():]
m2 = re.search(r'\nif __name__ == "__main__":', scan_body)
assert m2, "scan: __main__ not found"
scan_body = scan_body[:m2.start()].rstrip() + '\n'
scan_body = re.sub(r'\ndef main\(\)', '\ndef run_scan()', scan_body)
scan_body = re.sub(r'\bAGENT_NAMES\b', 'SCAN_AGENT_NAMES', scan_body)
scan_body = re.sub(r'\bAGENT_RE\b', 'SCAN_AGENT_RE', scan_body)
scan_body = re.sub(r'\bOUT_PATH\b', 'SCAN_OUT_PATH', scan_body)

# --- dryrun body ---
m = re.search(r'\nOUT_JSON = ROOT / "tools" / "_format_generation_dry_run\.json"', dryrun_src)
assert m, "dryrun: anchor not found"
dryrun_body = dryrun_src[m.start():]
m2 = re.search(r'\nif __name__ == "__main__":', dryrun_body)
assert m2, "dryrun: __main__ not found"
dryrun_body = dryrun_body[:m2.start()].rstrip() + '\n'
dryrun_body = re.sub(r'\ndef main\(\)', '\ndef run_dry_run()', dryrun_body)
dryrun_body = re.sub(r'\bOUT_JSON\b', 'DRYRUN_OUT_JSON', dryrun_body)
dryrun_body = re.sub(r'\bOUT_MD\b', 'DRYRUN_OUT_MD', dryrun_body)

# --- zerocov body ---
m = re.search(r'\nOUT_JSON = ROOT / "tools" / "_format_generation_zero_coverage\.json"', zerocov_src)
assert m, "zerocov: anchor not found"
zerocov_body = zerocov_src[m.start():]
m2 = re.search(r'\nif __name__ == "__main__":', zerocov_body)
assert m2, "zerocov: __main__ not found"
zerocov_body = zerocov_body[:m2.start()].rstrip() + '\n'
zerocov_body = re.sub(r'\ndef main\(\)', '\ndef run_zero_coverage()', zerocov_body)
zerocov_body = re.sub(r'\bOUT_JSON\b', 'ZEROCOV_OUT_JSON', zerocov_body)
zerocov_body = re.sub(r'\bOUT_MD\b', 'ZEROCOV_OUT_MD', zerocov_body)
# Drop the inline late-import of canonicalize_agent
zerocov_body = re.sub(r'\s+from _format_generation_regex_set import canonicalize_agent\n', '\n', zerocov_body)

# --- regex_set: strip leading imports (we replace with our own header) ---
m = re.search(r'\n# ---', regex_set_body)
assert m, "regex_set: section anchor not found"
regex_set_clean = regex_set_body[m.start():]

HEADER = '''#!/usr/bin/env python3
"""format_generations.py - consolidated format-generation pipeline.

Replaces the four legacy scripts:
  - _format_generation_regex_set.py     (now: library backbone + self-test subcmd)
  - _format_generation_scan.py          (now: scan subcommand)
  - _format_generation_dry_run.py       (now: dry-run subcommand)
  - _format_generation_zero_coverage.py (now: zero-coverage subcommand)

Library functions (canonicalize_agent, ROLE_VOCAB, AttributionEdge, the G1-G7
regex set, extract_g2..g7, extract_workshop_g7) are exposed for import by
harvester.py's attribution subcommand.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

'''

DISPATCHER = '''

# ---------------------------------------------------------------------------
# CLI dispatcher
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="format_generations.py",
        description="Format-generation pipeline (scan / dry-run / zero-coverage / self-test).",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("scan", help="Phase 0: fingerprint sessions for archetypes.")
    sub.add_parser("dry-run", help="Phase 0.5: aggregate per-generation edge counts.")
    sub.add_parser("zero-coverage", help="Phase 0.9: surface files with zero attribution edges.")
    sub.add_parser("self-test", help="Verify the G1-G7 regex set against frozen fixtures.")
    args = parser.parse_args()
    if args.cmd == "scan":
        run_scan()
    elif args.cmd == "dry-run":
        run_dry_run()
    elif args.cmd == "zero-coverage":
        run_zero_coverage()
    elif args.cmd == "self-test":
        sys.exit(run_self_test())


if __name__ == "__main__":
    main()
'''

out = (
    HEADER
    + regex_set_clean
    + '\n\n# ===========================================================================\n'
    + '# SCAN - lifted from _format_generation_scan.py (renamed AGENT_NAMES->SCAN_AGENT_NAMES)\n'
    + '# ===========================================================================\n'
    + scan_body
    + '\n\n# ===========================================================================\n'
    + '# DRY-RUN - lifted from _format_generation_dry_run.py (main -> run_dry_run)\n'
    + '# ===========================================================================\n'
    + dryrun_body
    + '\n\n# ===========================================================================\n'
    + '# ZERO-COVERAGE - lifted from _format_generation_zero_coverage.py (main -> run_zero_coverage)\n'
    + '# ===========================================================================\n'
    + zerocov_body
    + DISPATCHER
)

out_path = tools / 'format_generations.py'
out_path.write_text(out, encoding='utf-8')
print(f"Wrote {out_path}")
print(f"  Size: {out_path.stat().st_size:,} bytes")
print(f"  Lines: {out.count(chr(10))}")
