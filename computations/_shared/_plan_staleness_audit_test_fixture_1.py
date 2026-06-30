#!/usr/bin/env python
"""
S89 W6-1 fixture 1 — pre-supersession pin detection
====================================================

Asserts that `_plan_staleness_audit.scan_plan_staleness` fires the
`pre_supersession_pin` signal on a synthetic plan-block citing a literal
`eta_threshold_literal` post-supersession-event canonical. The fixture
is fixture-by-construction (orchestrator-direct-without-cross-actor)
per `epistemic-discipline.md §"Layer-Decomposition"`.

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
    SYNTH_FIXTURE_1_PLAN,
    synthetic_fixture_1,
)


def main() -> int:
    result = synthetic_fixture_1()
    print(json.dumps(result, indent=2))
    # Cross-check: re-run scan_plan_staleness directly on the synthetic plan
    matches = scan_plan_staleness(SYNTH_FIXTURE_1_PLAN)
    expected_fired = bool(matches["pre_supersession_pin"])
    other_fired = (
        bool(matches["downstream_inheritance_reviewer"])
        or bool(matches["pre_W8_100_corrective_no_supersedes"])
    )
    fixture_passes = expected_fired and not other_fired
    return 0 if fixture_passes else 1


if __name__ == "__main__":
    sys.exit(main())
