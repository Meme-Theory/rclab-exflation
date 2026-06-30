#!/usr/bin/env python
"""
S89 W6-1 fixture 2 — downstream-inheritance reviewer detection
==============================================================

Asserts that `_plan_staleness_audit.scan_plan_staleness` fires the
`downstream_inheritance_reviewer` signal on a synthetic plan-block
naming `lizzi-spectral-functional-theorist` as Stage-2 Axis-A on a
§VII.W-3.LAB cross-review with the workshop's R3 transcript path
mentioned. Fixture-by-construction.

Exit: 0 on PASS; 1 on FAIL.
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: E402,F401,F403  (mandatory per computations/_shared/CLAUDE.md)
from _plan_staleness_audit import (  # noqa: E402
    scan_plan_staleness,
    SYNTH_FIXTURE_2_PLAN,
    synthetic_fixture_2,
)


def main() -> int:
    result = synthetic_fixture_2()
    print(json.dumps(result, indent=2))
    matches = scan_plan_staleness(SYNTH_FIXTURE_2_PLAN)
    expected_fired = bool(matches["downstream_inheritance_reviewer"])
    other_fired = (
        bool(matches["pre_supersession_pin"])
        or bool(matches["pre_W8_100_corrective_no_supersedes"])
    )
    fixture_passes = expected_fired and not other_fired
    return 0 if fixture_passes else 1


if __name__ == "__main__":
    sys.exit(main())
