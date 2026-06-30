"""
_quotient_functor_pre_registration_audit.py

Minimal scaffold per S88 W9-103 orchestrator override (volovik PRIMARY +
connes-ncg CO).  W-6 RULE-1 (T1-6, S86 W-6, anchor at
`.claude/rules/epistemic-discipline.md` §"Quotient-functor pre-registration"
lines 174-184) mandates 3 fields per incarnation pre-registration:

  (a) Quotient-equivalence specification
  (b) Rank-match check at the quotient level: rank(ker) and rank(coker)
      at the quotient = finite-rank Pillar-V observable
  (c) Explicit declaration of residual cokernel content killed by the
      quotient

This audit verifies that for a list of incarnation dictionaries with keys
matching {a_quotient_eq_spec, b_rank_match, c_residual_cokernel,
parallelogram_max_dev, w11_1_anchor_max_dev}, all 3 fields are present and
non-empty for each incarnation.

Usage:
    from _quotient_functor_pre_registration_audit import audit_incarnations
    audit_result = audit_incarnations(incarnations, w11_1_anchor=1.163869)

Returns: dict
    {"per_incarnation": [...], "all_pass": bool, "n_pass": int, "n_fail": int}

S88 W9-103 (this file) is the FIRST authorship of this audit; future
extension queued under S89-QUOTIENT-FUNCTOR-AUDIT-EXPANSION.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

# Canonical constants per .claude/rules/math-scripts.md (S34+ MANDATORY).
# This audit is a non-numerical infrastructure module but the canonical
# import is required for computations/_shared/ compliance.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: F401,F403


REQUIRED_FIELDS = (
    "a_quotient_eq_spec",
    "b_rank_match",
    "c_residual_cokernel",
)


def _field_pass(value: Any) -> bool:
    """A field PASSES iff present, non-None, non-empty, and not a falsy stub.

    For dict / list values: must be non-empty container.
    For string values: must contain at least one non-whitespace character
        AND must not equal a literal stub marker.
    For numeric values: any finite numeric value PASSES (zero counts as
        empty residual cokernel — a positive structural finding, not a stub).
    """
    if value is None:
        return False
    if isinstance(value, (list, tuple, dict, set)):
        return len(value) > 0
    if isinstance(value, str):
        s = value.strip()
        if not s:
            return False
        STUB_MARKERS = ("TBD", "PENDING", "PLACEHOLDER", "?", "N/A")
        if s.upper() in STUB_MARKERS:
            return False
        return True
    # numeric / bool / other: pass-through if not None
    return True


def audit_incarnation(incarnation: dict, w11_1_anchor: float = 1.163869) -> dict:
    """Audit a single V_4 incarnation against W-6 RULE-1 (a)+(b)+(c).

    Parameters
    ----------
    incarnation : dict
        Must contain keys:
          - a_quotient_eq_spec : str (quotient-equivalence spec)
          - b_rank_match       : dict with {rank_ker, rank_coker} keys
          - c_residual_cokernel: str | dict (declaration of residual content)
        Optional:
          - parallelogram_max_dev : float (W11-1 PARALLELOGRAM IDENTITY test)
          - incarnation_id        : str
          - prior_verdict         : str  (S87/S88 verdict tag)

    Returns
    -------
    dict with per-field PASS/FAIL plus aggregate verdict.
    """
    per_field = {}
    for field in REQUIRED_FIELDS:
        per_field[field] = _field_pass(incarnation.get(field))
    all_three_pass = all(per_field.values())

    # Cross-check parallelogram identity max_dev against W11-1 anchor
    p_max_dev = incarnation.get("parallelogram_max_dev")
    parallelogram_pass = None
    if p_max_dev is not None:
        # Threshold: PASS iff max_dev <= 1e-12 (machine precision)
        # FAIL iff > 1e-9; INFO between (per W11-1 plan §W11-1.5)
        if p_max_dev <= 1e-12:
            parallelogram_pass = "PASS"
        elif p_max_dev <= 1e-9:
            parallelogram_pass = "INFO"
        else:
            parallelogram_pass = "FAIL"

    # Critical: per W-6 RULE-1, "Explicit declaration of residual cokernel
    # content KILLED BY the quotient" — if residual cokernel is non-empty
    # the quotient is NOT a clean isomorphism. Declaration of non-empty
    # residual content is HONEST but means field (c) PASSes the
    # declaration-discipline yet the incarnation FAILs the structural
    # quotient-isomorphism criterion.
    c_residual = incarnation.get("c_residual_cokernel")
    residual_is_nonempty_killed = incarnation.get(
        "c_residual_killed_by_quotient", None
    )

    return {
        "incarnation_id": incarnation.get("incarnation_id", "<unnamed>"),
        "per_field_pass": per_field,
        "all_three_present": all_three_pass,
        "parallelogram_max_dev": p_max_dev,
        "parallelogram_verdict": parallelogram_pass,
        "w11_1_anchor": w11_1_anchor,
        "c_residual_killed_by_quotient": residual_is_nonempty_killed,
        "prior_verdict": incarnation.get("prior_verdict"),
    }


def audit_incarnations(
    incarnations: list, w11_1_anchor: float = 1.163869
) -> dict:
    """Audit a list of V_4 incarnations.

    Returns the per-incarnation audit results plus an aggregate verdict:
    PASS iff every incarnation has all 3 fields AND the residual cokernel
    field declares the content is structurally killed by the quotient.
    """
    results = [
        audit_incarnation(inc, w11_1_anchor=w11_1_anchor)
        for inc in incarnations
    ]
    n_pass_3field = sum(1 for r in results if r["all_three_present"])
    n_pass_killed = sum(
        1 for r in results
        if r["all_three_present"]
        and r.get("c_residual_killed_by_quotient") is True
    )
    return {
        "per_incarnation": results,
        "n_total": len(incarnations),
        "n_3field_present": n_pass_3field,
        "n_residual_killed": n_pass_killed,
        "all_pass": n_pass_killed == len(incarnations),
    }


if __name__ == "__main__":
    # Self-test smoke
    test_incarnations = [
        {
            "incarnation_id": "test_pass",
            "a_quotient_eq_spec": "V_4 = Z_2 x Z_2",
            "b_rank_match": {"rank_ker": 2, "rank_coker": 0},
            "c_residual_cokernel": "empty",
            "c_residual_killed_by_quotient": True,
            "parallelogram_max_dev": 1e-15,
        },
        {
            "incarnation_id": "test_fail",
            "a_quotient_eq_spec": "V_4 = Z_2 x Z_2",
            "b_rank_match": {"rank_ker": 1, "rank_coker": 5},
            "c_residual_cokernel": "non-trivial 5-dim residual",
            "c_residual_killed_by_quotient": False,
            "parallelogram_max_dev": 1.16,
        },
    ]
    result = audit_incarnations(test_incarnations)
    import json
    print(json.dumps(result, indent=2))
