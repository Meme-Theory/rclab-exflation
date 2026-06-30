"""Build harvester.py by wrapping each of 10 harvester scripts in a closure.

Strategy:
  - Strip imports + leading path setup from each harvester source.
  - Wrap the remaining body inside `def _<name>_harvester(): ...`, indented +4.
  - Append `main()` call at the end of each wrapper so invocation runs the
    original main pipeline.
  - All imports are hoisted into the shared header.
  - All module-level constants from harvesters become LOCAL to their wrapper
    (so HEADER_TEMPLATE-from-archive does not collide with HEADER_TEMPLATE-
    from-workingpaper, etc.).
  - The CLI dispatcher calls the appropriate _<name>_harvester().
"""
import re
import textwrap
from pathlib import Path

tools = Path(__file__).resolve().parent

# Mapping: subcommand name -> source filename
HARVESTERS = [
    ('archive',                'harvest_archive_edges.py'),
    ('provenance',             'harvest_provenance_edges.py'),
    ('theorem-closure',        'harvest_theorem_closure_edges.py'),
    ('equation',               'harvest_equation_edges.py'),
    ('attribution',            'harvest_attribution_edges.py'),
    ('chain-of-custody',       'harvest_chain_of_custody_edges.py'),
    ('plan-pin',               'harvest_plan_pin_edges.py'),
    ('workingpaper',           'harvest_workingpaper_edges.py'),
    ('script-import',          'harvest_script_import_edges.py'),
    ('archive-script-import',  'harvest_archive_script_import_edges.py'),
]


def strip_leading_header(src: str) -> str:
    """Remove docstring + imports + ROOT/PROJECT_ROOT definitions from the
    top of a harvester source. Returns the body starting at the first
    non-trivial constant or function definition.

    The body is what we wrap in a closure. We anchor on either:
      - The first `def ` at column 0
      - OR the first `[A-Z]` constant assignment that is NOT one of the
        shared names (PROJECT_ROOT, ROOT, COMPUTATIONS_DIR, CC_PATH,
        DB_PATH, HERE, ARCHIVE, CANONICAL — see SHARED_NAMES below).
    """
    lines = src.splitlines(keepends=True)
    out_idx = 0
    # Skip shebang + module docstring
    i = 0
    if lines and lines[0].startswith('#!'):
        i += 1
    # Skip blank lines
    while i < len(lines) and lines[i].strip() == '':
        i += 1
    # Skip module docstring. Handle r"""..."""/u"""/b"""/f""" string prefixes.
    if i < len(lines):
        stripped_line = lines[i].lstrip()
        m_prefix = re.match(r'^[rRuUbBfF]{0,2}("""|\'\'\')', stripped_line)
        if m_prefix:
            quote = m_prefix.group(1)
            if stripped_line.count(quote) >= 2 and len(stripped_line) > len(m_prefix.group(0)):
                i += 1  # single-line docstring
            else:
                i += 1
                while i < len(lines) and quote not in lines[i]:
                    i += 1
                i += 1  # past the closing line
    # Skip imports + path setup. Track open-paren depth so multi-line
    # `from X import (a, b, c)` blocks are skipped in their entirety.
    skip_prefixes = (
        'from __future__',
        'import ',
        'from ',
        'sys.path.insert',
        'sys.path.append',
    )
    shared_path_assigns = re.compile(
        r'^\s*(PROJECT_ROOT|ROOT|HERE|COMPUTATIONS_DIR|COMPUTATIONS|'
        r'CC_PATH|DB_PATH|SHARED_DIR|ARCHIVE|CANONICAL)\s*='
    )
    paren_depth = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        # If still inside an open paren from a prior import/assign, keep skipping
        if paren_depth > 0:
            paren_depth += line.count('(') - line.count(')')
            i += 1
            continue
        # Skip blank + comment
        if stripped == '' or stripped.startswith('#'):
            i += 1
            continue
        # Skip imports
        if any(stripped.startswith(p) for p in skip_prefixes):
            # Track opening paren on this line so we keep skipping the
            # continuation body of a multi-line `from X import (...)`.
            paren_depth += line.count('(') - line.count(')')
            i += 1
            continue
        # Skip path-shared assignments (may also span multiple lines via paren)
        if shared_path_assigns.match(line):
            paren_depth += line.count('(') - line.count(')')
            i += 1
            continue
        # Hit the first real body content
        break
    body = ''.join(lines[i:])

    # Strip trailing `if __name__ == "__main__":` block
    m = re.search(r'\nif __name__\s*==\s*["\']__main__["\']:', body)
    if m:
        body = body[:m.start()].rstrip() + '\n'
    # Some sources end with `sys.exit(main())` at module level — strip
    body = re.sub(r'\nsys\.exit\(main\(\)\)\s*$', '\n', body)
    return body


def wrap_in_closure(name: str, body: str) -> str:
    """Wrap a harvester body in a closure function, indent +4, add main() call at end."""
    # Indent every line by 4 spaces (preserving empty lines)
    indented = textwrap.indent(body, '    ', predicate=lambda line: line.strip() != '')
    return (
        f"def _{name.replace('-', '_')}_harvester() -> None:\n"
        f'    """Run the {name} harvester. Lifted from harvest_{name.replace("-", "_")}_edges.py."""\n'
        + indented
        + '    main()\n'
    )


HEADER = '''#!/usr/bin/env python3
"""harvester.py - consolidated edge harvester for the knowledge index.

Replaces the ten legacy harvest_*.py scripts with a single CLI entry point
exposing each as a subcommand. The original logic from each script is wrapped
in a private closure function (_archive_harvester, _provenance_harvester, ...)
so HEADER_TEMPLATE / main() / ROOT / OUT_PATH definitions stay local to each
implementation and don't collide.

Subcommands:
  archive                - Phase 1: edges from session-archive synthesis files.
  provenance             - Phase 1: script -> data -> gate lineage.
  theorem-closure        - Optional Phase 2 pass: theorem-closure edges from DB.
  equation               - Optional Phase 2 pass: equation-citation edges.
  attribution            - Phase 1 / G1-G7: authored_by / co_authored_by / reviewed_by.
  chain-of-custody       - Phase 1.1: carries_forward / anchored_in / succ_of.
  plan-pin               - Edges from session-plan PIN MAPs.
  workingpaper           - Edges from session-N workingpaper gate sections.
  script-import          - Edges from `from canonical_constants import X` patterns.
  archive-script-import  - Same, against the computations archive.

Each subcommand executes the original harvester's main() pipeline unchanged.
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sqlite3
import sys
import types
from collections import Counter, defaultdict, OrderedDict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

# Shared path setup. Each harvester closure inherits these via Python's
# function-scope lookup (locals -> enclosing -> module -> builtins).
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ROOT = PROJECT_ROOT                       # alias used by some harvesters
HERE = Path(__file__).resolve().parent    # alias used by some harvesters
COMPUTATIONS_DIR = PROJECT_ROOT / "computations"
COMPUTATIONS = COMPUTATIONS_DIR           # alias used by script-import
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
CC_PATH = SHARED_DIR / "canonical_constants.py"
DB_PATH = PROJECT_ROOT / "tools" / "knowledge.db"
ARCHIVE = PROJECT_ROOT / "computation-archive"   # used by archive-script-import
CANONICAL = CC_PATH                              # alias used by archive-script-import

# Make canonical_constants importable for harvesters that rely on
# `import canonical_constants as CC` (script-import edges build VOCAB via
# dir(CC)). Insert tools/../computations/_shared at front of sys.path.
if str(SHARED_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_DIR))

# Make format_generations symbols available to the attribution closure
# (was: from _format_generation_regex_set import ...). format_generations.py
# lives in the same tools/ directory.
from format_generations import (   # noqa: E402
    AttributionEdge,
    G1_AGENT_RE,
    canonicalize_agent,
    extract_g1,
    extract_g2,
    extract_g3,
    extract_g5_per_gate,
    extract_g6,
    extract_g7,
    extract_workshop_g7,
    session_to_generation,
)

import importlib.util   # noqa: E402  - used by plan-pin + archive-script-import closures

# Chain-of-custody extractor library, inlined here so the chain-of-custody
# closure has access without depending on the standalone module.
# ---- BEGIN INLINED _chain_of_custody_extractors.py ----
__CHAIN_OF_CUSTODY_PLACEHOLDER__
# ---- END INLINED _chain_of_custody_extractors.py ----

'''


def build():
    # Inline _chain_of_custody_extractors.py body at module level.
    coc_src = (tools / '_chain_of_custody_extractors.py').read_text(encoding='utf-8')
    coc_body = strip_leading_header(coc_src)
    header = HEADER.replace('__CHAIN_OF_CUSTODY_PLACEHOLDER__', coc_body.rstrip())

    sections = []
    for name, fname in HARVESTERS:
        src = (tools / fname).read_text(encoding='utf-8')
        body = strip_leading_header(src)
        wrapper = wrap_in_closure(name, body)
        sections.append(
            f'# ==========================================================================\n'
            f'# {name.upper()} -- lifted from {fname}\n'
            f'# ==========================================================================\n\n'
            + wrapper
        )

    DISPATCHER = '''
# ---------------------------------------------------------------------------
# CLI dispatcher
# ---------------------------------------------------------------------------

SUBCMDS = {
    "archive":               _archive_harvester,
    "provenance":            _provenance_harvester,
    "theorem-closure":       _theorem_closure_harvester,
    "equation":              _equation_harvester,
    "attribution":           _attribution_harvester,
    "chain-of-custody":      _chain_of_custody_harvester,
    "plan-pin":              _plan_pin_harvester,
    "workingpaper":          _workingpaper_harvester,
    "script-import":         _script_import_harvester,
    "archive-script-import": _archive_script_import_harvester,
}


def main_dispatch() -> None:
    parser = argparse.ArgumentParser(
        prog="harvester.py",
        description="Edge harvesters for the knowledge index.",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)
    for name in SUBCMDS:
        sub.add_parser(name)
    args, _extra = parser.parse_known_args()
    # Each closure invokes its own argparse on sys.argv, so reset sys.argv to
    # only what the inner main() expects (drop the harvester.py + subcommand
    # tokens, keep any pass-through flags).
    inner_argv = [f"harvester.py {args.cmd}"] + _extra
    saved_argv = sys.argv
    sys.argv = inner_argv
    try:
        SUBCMDS[args.cmd]()
    finally:
        sys.argv = saved_argv


if __name__ == "__main__":
    main_dispatch()
'''

    out = header + '\n\n'.join(sections) + DISPATCHER
    out_path = tools / 'harvester.py'
    out_path.write_text(out, encoding='utf-8')
    print(f"Wrote {out_path}")
    print(f"  Size: {out_path.stat().st_size:,} bytes")
    print(f"  Lines: {out.count(chr(10))}")
    # Syntax check
    try:
        ast.parse(out)
        print("  SYNTAX OK")
    except SyntaxError as e:
        print(f"  SYNTAX ERROR: line {e.lineno}: {e.msg}")
        # Show context
        lines = out.splitlines()
        for i in range(max(0, e.lineno-3), min(len(lines), e.lineno+3)):
            marker = " >> " if (i+1) == e.lineno else "    "
            print(f"  {marker}{i+1:5d}: {lines[i]}")


if __name__ == "__main__":
    import ast
    build()
