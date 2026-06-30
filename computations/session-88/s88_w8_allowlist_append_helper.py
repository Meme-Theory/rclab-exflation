"""S88 W8-92 — atomic-append helper for methodology-wave-allowlist.md row.

Mirrors the canonical Python `with open("a")` POSIX O_APPEND pattern from
`_script_template.py append_verdict()` to avoid mtime-conditional Edit-tool
race conditions under parallel writers (per registry-landing.md
§"Bridge-Landing Script Architecture").
"""
from pathlib import Path

ALLOWLIST = Path(__file__).resolve().parent.parent.parent / ".claude" / "rules" / "methodology-wave-allowlist.md"

NEW_ROW = (
    "| W8-92 | S88     | S88-OPERATOR-PROJECTION-READING-A-RULE-PROMOTE "
    "(registry-landing.md §\"Operator-Projection Reading-A Naming Hygiene\" extension; "
    "K=3 calibration corpus K_promotion=3 → MANDATORY status promotion per "
    "`feedback_rules-compensate-missing-structure.md`; corpus = "
    "{S87 W4-2 §VII.AJ.W4-1 operator-projection on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) "
    "central-projection traces, S87 W6-1 §VII.AG.1 operator-projection on "
    "T7 ↔ S67 quotient-functor cyclic-fold V_4 modulo "
    "(CF-LZ-VV Cyclic-Fold Mellin Spectroscopy theorem candidate "
    "STAGE-1-CANDIDATE per joint-theorem-promotion.md), S87 W11-meta-2 "
    "operator-projection on cross-pillar bridge-anatomy K-count discipline "
    "(math-scripts.md §\"Machinery-Feasibility Audit\" D_K Block-Diagonality "
    "pre-check; W11-2 + W11-3 dual calibration with "
    "audit_sha256 = 9f6d9bcea1e798eccdf3dad43922dad94b07ac3977353b7e032db39494f62253)}; "
    "naming convention `§VII.X.OP-PROJ` (algebra-side) vs `§VII.X.STATE-PROJ` "
    "(state-side) MANDATORY at plan-freeze; `_registry_landing_audit.py` "
    "Class-(g) `OP-VS-STATE-PROJECTION-NAMING-DRIFT` flag; cross-link to "
    "`cross-pillar-bridge-anatomy.md §\"Algebra-axis orthogonality K-counter\"` "
    "MANDATORY clause as registry-naming-layer specialization at non-redundant "
    "operational layer; CO-AUTHOR `connes-ncg-theorist` registry-naming-consistency "
    "review embedded in WP §W8-92; M1-M4 conjunction satisfied "
    "[M1 artifact-existence on rule-file diff ≥15 substantive lines; "
    "M2 Edit on .claude/rules/registry-landing.md + Edit on .claude/rules/methodology-wave-allowlist.md; "
    "M3 verbatim corpus from S87 W4-2 §VII.AJ.W4-1 + S87 W6-1 §VII.AG.1 + S87 W11-meta-2; "
    "M4 allowlist append herewith]; orchestrator-direct-write per "
    "`wave-classification.md` §\"Dispatch consequences\"; "
    "gen-physicist PRIMARY + connes-ncg-theorist CO-AUTHOR) | pending |\n"
)


def main() -> int:
    # Idempotency check: skip append if W8-92 row already present
    text = ALLOWLIST.read_text(encoding="utf-8")
    if "| W8-92 | S88" in text:
        print("W8-92 row already present in allowlist; no-op")
        return 0
    with ALLOWLIST.open("a", encoding="utf-8") as f:
        f.write(NEW_ROW)
    print("W8-92 row appended to", ALLOWLIST)
    print("last line:", ALLOWLIST.read_text(encoding="utf-8").splitlines()[-1][:120], "...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
