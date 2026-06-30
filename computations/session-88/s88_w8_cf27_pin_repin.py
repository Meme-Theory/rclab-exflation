#!/usr/bin/env python3
"""
S88 W8-96 — S88-CF-27-PIN-RE-PIN-AT-PLAN-FREEZE
================================================

Gate: S88-CF-27-PIN-RE-PIN-AT-PLAN-FREEZE ([AUDIT])

Pre-registered threshold (session-88-plan-w8.md §W8-96 lines 372-374):
  PASS  iff all 3 f_NL pathway-keyed provenance SHAs match source SHAs at S88
        plan-freeze.
  FAIL with diagnostic + re-pin iff drift detected (provenance SHA != source
        SHA at S88 plan-freeze).
  INFO  iff pathway-keyed entry is MISSING entirely from canonical_constants.py
        (route to canonical_constants.py promotion via
        math-scripts.md §"Canonical write-order").

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - canonical_constants.py
    (queried for provenance entries f_NL_FW_S82_equilateral,
     f_NL_FW_S67_folded, f_NL_FW_S85_W9_3_analytic_template)
  - computations/session-82/s82_w3_4_gge_fnl_channel.py
    (S82 equilateral-template pathway source; emits f_NL = 0.0547)
  - computations/session-67/s67_gge_bispectrum.py
    (S67 folded-pathway source; emits f_NL = 0.129)
  - computations/session-85/s85_w9_folded_triangle_21cm_shape.py
    (S85 W9-3 analytic-template-folded source; emits f_NL = 0.7685)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<status_dict>, scheme=SHA-comparison-canonical-vs-source,
   convention=re-pin-on-drift-via-update_constant, L_max=N/A)

Classification: NON-PHONONIC (audit; canonical-sourcing-discipline gate)

METHODOLOGY
-----------
This is a SOURCE-RECON Class-(c) PIN-DRIFT-FROM-STALE-SOURCE pre-flight audit
for the 3 f_NL pathway-keyed canonical pins specified in plan §W8-96. The
plan threshold has three branches:

  (1) PASS — all 3 entries present in canonical_constants.py and provenance
      SHAs match source SHAs at S88 plan-freeze.
  (2) FAIL with diagnostic — at least one pin present but drift detected;
      re-pin via update_constant (orchestrator-side via Knowledge MCP).
  (3) INFO — pathway-keyed entry MISSING entirely; route to
      canonical_constants.py promotion via math-scripts.md
      §"Canonical write-order" (steps 1-3: verdict-line → canonical promotion
      → inventory landing).

Substitution chain for the verdict (cf. math-scripts.md §"Double-Check Logic"):

  Definitions:
    N_present(c) = 1 if mcp_get_constant(c) returns a value, else 0
    Σ_present   = Σ over c ∈ {f_NL_FW_S82_equilateral, f_NL_FW_S67_folded,
                              f_NL_FW_S85_W9_3_analytic_template} N_present(c)
    drift(c)    = (canonical_provenance_SHA(c) != current_source_SHA(c))
                  iff N_present(c) = 1; undefined otherwise

  Cases (mutually exclusive, exhaustive):
    Σ_present < 3                           ⇒ INFO
    Σ_present = 3 AND ¬∃c: drift(c)         ⇒ PASS
    Σ_present = 3 AND ∃c: drift(c)          ⇒ FAIL with diagnostic + re-pin

DISCIPLINE
----------
- `from canonical_constants import *` (Section 1).
- All MCP queries done by orchestrator BEFORE script run; results pre-cached
  in MCP_QUERY_RESULTS dict at top of Section 5. Script does NOT call MCP
  directly (separation-of-concerns; MCP is the orchestrator's authority
  lookup, the script is the on-disk evaluator).
- Source-file SHAs computed at runtime; emitted to .npz + verdict line.
- 4-tuple printed as final non-verdict line.
- Verdict appended to s88_gate_verdicts.txt with audit_sha256 +
  content_sha256 + schema_version=S84+.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
import numpy as np


# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S88"                                                         # (local)
GATE_ID = "S88-CF-27-PIN-RE-PIN-AT-PLAN-FREEZE"                         # (local)
SCHEME = "SHA-comparison-canonical-vs-source"                           # (local)
CONVENTION = "re-pin-on-drift-via-update_constant"                      # (local)
L_MAX = "N/A"                                                           # (local)

OUT_NPZ = SESSION_DIR / "s88_w8_cf27_pin_repin.npz"                     # (local)
VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"                     # (local)

# Three pathway-keyed constants per plan §W8-96 line 364
PATHWAY_KEYED_CONSTANTS = [                                             # (local)
    {
        "name": "f_NL_FW_S82_equilateral",
        "expected_value": 0.0547,
        "source_path": COMPUTATIONS_DIR / "session-82" / "s82_w3_4_gge_fnl_channel.py",
        "pathway_label": "S82 equilateral-template pathway (GGE-FNL channel projection)",
    },
    {
        "name": "f_NL_FW_S67_folded",
        "expected_value": 0.129,
        "source_path": COMPUTATIONS_DIR / "session-67" / "s67_gge_bispectrum.py",
        "pathway_label": "S67 folded-pathway (GGE-BISPECTRUM-67 in-in formalism)",
    },
    {
        "name": "f_NL_FW_S85_W9_3_analytic_template",
        "expected_value": 0.7685,
        "source_path": COMPUTATIONS_DIR / "session-85" / "s85_w9_folded_triangle_21cm_shape.py",
        "pathway_label": "S85 W9-3 analytic-template-folded pathway (folded-triangle 21cm shape)",
    },
]

INPUT_FILES = [SHARED_DIR / "canonical_constants.py"] + [
    p["source_path"] for p in PATHWAY_KEYED_CONSTANTS
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute (pin presence + drift detection)
# ---------------------------------------------------------------------------

# MCP knowledge query results pre-cached by orchestrator BEFORE script run.
# Per CLAUDE.md "Knowledge MCP — MANDATORY for Computation Agents" + plan §W8-96
# directive "query mcp__knowledge__.get_constant(...) BEFORE script (canonical
# authority lookup)".
#
# Orchestrator queried 2026-05-05 (current date per env block):
#   mcp__knowledge__.get_constant("f_NL_FW_S82_equilateral")
#       -> "Constant 'f_NL_FW_S82_equilateral' not found"
#   mcp__knowledge__.get_constant("f_NL_FW_S67_folded")
#       -> "Constant 'f_NL_FW_S67_folded' not found"
#   mcp__knowledge__.get_constant("f_NL_FW_S85_W9_3_analytic_template")
#       -> "Constant 'f_NL_FW_S85_W9_3_analytic_template' not found"
#
# Cross-check: list_constants(pattern="f_NL") returned only f_NL_total_SKA1
# (S86 W-4 CANON-EXTRACT). The 3 pathway-keyed entries are MISSING from
# canonical_constants.py.
#
# Cross-validated by `grep -n "f_NL_FW" computations/_shared/canonical_constants.py`
# at runtime (returned no matches).
MCP_QUERY_RESULTS = {                                                   # (local)
    "f_NL_FW_S82_equilateral": {
        "found": False,
        "raw_response": "Constant 'f_NL_FW_S82_equilateral' not found",
        "value": None,
        "session": None,
        "source": None,
        "gate": None,
        "provenance_sha": None,
    },
    "f_NL_FW_S67_folded": {
        "found": False,
        "raw_response": "Constant 'f_NL_FW_S67_folded' not found",
        "value": None,
        "session": None,
        "source": None,
        "gate": None,
        "provenance_sha": None,
    },
    "f_NL_FW_S85_W9_3_analytic_template": {
        "found": False,
        "raw_response": "Constant 'f_NL_FW_S85_W9_3_analytic_template' not found",
        "value": None,
        "session": None,
        "source": None,
        "gate": None,
        "provenance_sha": None,
    },
}


def crosscheck_canonical_constants_grep(canonical_path: Path) -> bool:
    """Cross-validate MCP results: grep canonical_constants.py for f_NL_FW.

    Returns True iff zero hits (consistent with MCP "not found" results).
    """
    txt = canonical_path.read_text(encoding="utf-8", errors="replace")  # (local)
    hits = [                                                             # (local)
        line for line in txt.splitlines()
        if "f_NL_FW" in line
    ]
    print(f"  cross-check grep 'f_NL_FW' in canonical_constants.py: {len(hits)} hits")
    return len(hits) == 0


def compute() -> dict:
    """Pin-presence + drift detection across the 3 pathway-keyed constants."""
    canonical_path = SHARED_DIR / "canonical_constants.py"               # (local)

    # Cross-check MCP results against on-disk grep
    grep_consistent = crosscheck_canonical_constants_grep(canonical_path)  # (local)

    diagnostics = []                                                     # (local)
    n_present = 0                                                        # (local)
    n_drift = 0                                                          # (local)
    n_missing = 0                                                        # (local)

    pathway_results = {}                                                 # (local)

    for entry in PATHWAY_KEYED_CONSTANTS:
        name = entry["name"]
        src_path = entry["source_path"]
        src_sha = sha256_of(src_path)                                    # (local)
        src_exists = src_path.exists()                                   # (local)

        mcp_record = MCP_QUERY_RESULTS[name]                             # (local)
        present = mcp_record["found"]                                    # (local)

        if present:
            canonical_sha = mcp_record["provenance_sha"]                 # (local)
            drift = (canonical_sha != src_sha)                           # (local)
            if drift:
                n_drift += 1
                diagnostics.append({
                    "name": name,
                    "status": "DRIFT-DETECTED",
                    "canonical_sha": canonical_sha,
                    "current_source_sha": src_sha,
                    "remediation": (
                        f"re-pin via update_constant({name!r}, value="
                        f"{entry['expected_value']}, session='S88', "
                        f"source='S88-W8-96', "
                        f"comment='re-pinned at S88 plan-freeze; prior SHA "
                        f"{canonical_sha}; new SHA {src_sha}')"
                    ),
                })
            else:
                diagnostics.append({
                    "name": name,
                    "status": "MATCH",
                    "canonical_sha": canonical_sha,
                    "current_source_sha": src_sha,
                })
            n_present += 1
        else:
            n_missing += 1
            diagnostics.append({
                "name": name,
                "status": "MISSING-FROM-CANONICAL",
                "canonical_sha": None,
                "current_source_sha": src_sha,
                "remediation": (
                    f"INFO: route to canonical_constants.py promotion via "
                    f"math-scripts.md §'Canonical write-order' "
                    f"(Step 2: update_constant({name!r}, value="
                    f"{entry['expected_value']}, session='S88', "
                    f"source='S88-W8-96', comment='S88-CF-27 pin-promotion; "
                    f"3-pathway f_NL projection per §W13-2 P10 registry; "
                    f"source_sha={src_sha}'))"
                ),
            })

        pathway_results[name] = {
            "expected_value": entry["expected_value"],
            "source_path": str(src_path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
            "source_exists": src_exists,
            "current_source_sha": src_sha,
            "present_in_canonical": present,
            "canonical_provenance_sha": mcp_record["provenance_sha"],
            "pathway_label": entry["pathway_label"],
            "mcp_raw_response": mcp_record["raw_response"],
        }

    # Verdict logic per plan §W8-96 (substitution chain in module docstring)
    if n_missing > 0:
        verdict = "INFO"                                                 # (local)
        verdict_reason = (
            f"PRE-REG-INC_route_to_canonical_promotion_"
            f"missing={n_missing}_present={n_present}_drift={n_drift}"
        )
    elif n_drift > 0:
        verdict = "FAIL"                                                 # (local)
        verdict_reason = (
            f"DRIFT_DETECTED_re-pin_required_"
            f"drift={n_drift}_present={n_present}"
        )
    else:
        verdict = "PASS"                                                 # (local)
        verdict_reason = (
            f"all_3_pathway_keyed_pins_match_source_SHAs_at_S88_plan_freeze"
        )

    return {
        "value": {
            "verdict": verdict,
            "verdict_reason": verdict_reason,
            "n_present": n_present,
            "n_missing": n_missing,
            "n_drift": n_drift,
            "grep_consistent_with_mcp": grep_consistent,
        },
        "pathway_results": pathway_results,
        "diagnostics": diagnostics,
        "verdict_top": verdict,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (
        f"(value={value!r}, scheme={scheme}, "
        f"convention={convention}, L_max={L_max})"
    )


def append_verdict(
    verdict: str,
    value_str: str,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Atomic single-line append per .claude/rules/gate-verdicts.md."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def append_companion_row(audit_sha: str, content_sha: str) -> None:
    """Dual-SHA companion comment row per gate-verdicts.md §S87+ schema-v2."""
    line = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute
    print(f"=== {GATE_ID} — pin-presence + drift detection ===")
    result = compute()
    value_dict = result["value"]
    pathway_results = result["pathway_results"]
    diagnostics = result["diagnostics"]
    verdict = result["verdict_top"]

    # 3. Print per-pathway diagnostics
    print()
    for diag in diagnostics:
        print(f"  {diag['name']}: {diag['status']}")
        print(f"    current_source_sha: {diag['current_source_sha']}")
        if diag.get('canonical_sha'):
            print(f"    canonical_sha:      {diag['canonical_sha']}")
        if diag.get('remediation'):
            print(f"    remediation: {diag['remediation'][:120]}...")

    # 4. Save .npz with full diagnostics
    npz_payload = {
        "verdict": verdict,
        "verdict_reason": value_dict["verdict_reason"],
        "n_present": value_dict["n_present"],
        "n_missing": value_dict["n_missing"],
        "n_drift": value_dict["n_drift"],
        "grep_consistent_with_mcp": value_dict["grep_consistent_with_mcp"],
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "closure_legacy": closure,
        "pathway_results_json": json.dumps(pathway_results, indent=2),
        "diagnostics_json": json.dumps(diagnostics, indent=2),
        "mcp_query_results_json": json.dumps(MCP_QUERY_RESULTS, indent=2),
    }
    # Per-pathway flat keys for ease of inspection
    for name, rec in pathway_results.items():
        npz_payload[f"{name}__source_sha"] = rec["current_source_sha"]
        npz_payload[f"{name}__source_path"] = rec["source_path"]
        npz_payload[f"{name}__present"] = rec["present_in_canonical"]
        npz_payload[f"{name}__expected_value"] = rec["expected_value"]
    np.savez(OUT_NPZ, **{k: np.asarray(v) for k, v in npz_payload.items()})
    print(f"\n  .npz saved: {OUT_NPZ.name}")

    # 5. Build summary value string for verdict line
    value_str = (
        f"verdict={verdict};"
        f"n_present={value_dict['n_present']};"
        f"n_missing={value_dict['n_missing']};"
        f"n_drift={value_dict['n_drift']};"
        f"reason={value_dict['verdict_reason']}"
    )

    # 6. 4-tuple
    tag = emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX)
    print(tag)

    # 7. Append verdict + companion row
    append_verdict(verdict, value_str, audit_sha, content_sha)
    append_companion_row(audit_sha, content_sha)

    # 8. Summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0  # exit 0 regardless of verdict per math-scripts.md §"Exit Codes"


if __name__ == "__main__":
    sys.exit(main())
