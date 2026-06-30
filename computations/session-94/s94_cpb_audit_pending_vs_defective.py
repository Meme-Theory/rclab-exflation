"""
s94_cpb_audit_pending_vs_defective.py

Producing script for gate S94-CPB-AUDIT-PENDING-VS-DEFECTIVE (S94 W6-17,
METHODOLOGY-class audit-script extension).

Runs the S94 W6-17 status-aware extension of `_cross_pillar_bridge_audit.run_audit()`
on the LIVE `permanent-results-registry.md`, runs the synthetic self-test, writes
the JSON audit report, and appends the dual-SHA verdict line.

Verdict semantics (pre-registered per session-94-plan-w6.md §W6-17):
  - The extended run_audit() classifies each non-PASS §VII bridge section into
    {legitimately-pending, genuinely-defective, self-non-bridge, superseded, PASS}
    and emits PASS / PASS-WITH-N-PENDING / FAIL.
  - On the LIVE (un-retrofitted) registry, genuinely_defective > 0 ⇒ verdict FAIL,
    with the genuinely-defective set NAMED (FAIL_meaning: "the defective entry is
    named and routed to mack-cosmic-bridge for the registry retrofit, and the
    audit correctly FAILs until that lands"). mack-cosmic-bridge is the sole
    registry writer per `feedback_mack-bridge-role.md`; this gate does NOT edit
    the registry — it writes the audit-script extension + the JSON report.
  - The self-test proves the classifier returns PASS-WITH-N-PENDING with
    genuinely_defective == 0 AFTER the OE-form/tier retrofit of the defective set
    (synthetic fixture), confirming the extension is implementable.

Dual-SHA closure (METHODOLOGY-class, per wave-classification.md §"Dual-SHA
closure for METHODOLOGY-class"):
  - content_sha256 = sha256( bytes(_cross_pillar_bridge_audit.py) )
    (the audit-script diff; the F-image of the numerical PASS-predicate eigenvalue).
  - audit_sha256   = sha256( bytes(_cross_pillar_bridge_audit.py)
                             || bytes(permanent-results-registry.md)
                             || pinmap_json )  (input-pin map closure).

Run:
    "phonon-exflation-sim/.venv312/Scripts/python.exe" \
        computations/session-94/s94_cpb_audit_pending_vs_defective.py
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

# Project root + shared dir on path.
ROOT = Path(__file__).resolve().parent.parent.parent           # (local) project root
SHARED = ROOT / "computations" / "_shared"                     # (local)
sys.path.insert(0, str(SHARED))

# Canonical constants per computations/_shared/CLAUDE.md (S34+). No framework
# constant is computed here (this is a methodology-floor audit-emission script),
# but the canonical namespace is imported for discipline compliance.
from canonical_constants import *  # noqa: E402,F401,F403

from _cross_pillar_bridge_audit import run_audit  # noqa: E402

# Import the self-test driver so its all-pass result is captured in the report.
sys.path.insert(0, str(SHARED))
import s94_w6_cpb_audit_pending_vs_defective_selftest as selftest  # noqa: E402


# ---------------------------------------------------------------------------
# Pinned paths + gate identity
# ---------------------------------------------------------------------------

GATE_ID = "S94-CPB-AUDIT-PENDING-VS-DEFECTIVE"                  # (local)
SCHEME = "METHODOLOGY-class-audit-script-extension"            # (local)
CONVENTION = (                                                  # (local)
    "PASS-WITH-N-PENDING-classifier;"
    "parent-sub-section-anatomy-inheritance-resolver"
)
L_MAX = "N/A"                                                  # (local) methodology-floor audit

AUDIT_SCRIPT_PATH = SHARED / "_cross_pillar_bridge_audit.py"   # (local)
SELFTEST_PATH = SHARED / "s94_w6_cpb_audit_pending_vs_defective_selftest.py"  # (local)
REGISTRY_PATH = ROOT / "sessions" / "permanent-results-registry.md"          # (local)
CORPUS_PATH = (                                                # (local)
    ROOT / "sessions" / "framework" / "registry"
    / "cross-pillar-bridge-corpus.md"
)
JSON_OUT = (                                                   # (local)
    ROOT / "computations" / "session-94"
    / "s94_cpb_audit_pending_vs_defective.json"
)
VERDICT_TXT = (                                                # (local)
    ROOT / "computations" / "session-94" / "s94_gate_verdicts.txt"
)


def _sha256_file(p: Path) -> str:
    """SHA-256 hexdigest of a file's bytes ('' if missing)."""
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return ""


def compute_dual_sha() -> tuple[str, str, dict]:
    """Compute (audit_sha256, content_sha256, pinmap).

    content_sha256 = sha256( bytes(audit-script) )  — the script diff only.
    audit_sha256   = sha256( bytes(audit-script) || bytes(registry) || pinmap_json ).

    The pinmap is the {relpath: sha256} map of every input file the gate reads,
    matching the plan §W6-17 (8) input_files block + the producing artifacts.
    """
    pinmap = {                                                 # (local)
        "computations/_shared/_cross_pillar_bridge_audit.py":
            _sha256_file(AUDIT_SCRIPT_PATH),
        "computations/_shared/s94_w6_cpb_audit_pending_vs_defective_selftest.py":
            _sha256_file(SELFTEST_PATH),
        "sessions/permanent-results-registry.md":
            _sha256_file(REGISTRY_PATH),
        "sessions/framework/registry/cross-pillar-bridge-corpus.md":
            _sha256_file(CORPUS_PATH),
    }
    pinmap_json = json.dumps(                                  # (local)
        dict(sorted(pinmap.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")

    script_bytes = AUDIT_SCRIPT_PATH.read_bytes()             # (local)
    registry_bytes = REGISTRY_PATH.read_bytes()               # (local)

    h_audit = hashlib.sha256()                                # (local)
    h_audit.update(script_bytes)
    h_audit.update(registry_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                               # (local)

    content = hashlib.sha256(script_bytes).hexdigest()        # (local)
    return audit, content, pinmap


def append_verdict(verdict: str, value: str, audit_sha: str,
                   content_sha: str) -> None:
    """Atomic single-line verdict append + dual-SHA companion comment row.

    [AUDIT] trigger ⇒ NO 3-tuple [SIGN] companion row (per plan §W6-17
    schema_v2_3tuple_required: false). Atomic O_APPEND single open('a') write
    per the canonical append_verdict() helper (no read-modify-write / truncate).
    """
    line = (                                                   # (local)
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (                                              # (local)
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [AUDIT] pending-vs-defective "
        f"classifier extension; no [SIGN] 3-tuple\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def main() -> int:
    # --- 1. Run the status-aware audit on the LIVE registry ---
    audit_result = run_audit()                                 # (local)

    # --- 2. Run the synthetic self-test, capture all-pass ---
    st = selftest.run_self_test()                              # (local)

    # --- 3. Compute dual-SHA over the input-pin map ---
    audit_sha, content_sha, pinmap = compute_dual_sha()        # (local)

    # --- 4. Assemble + write the JSON audit report ---
    report = {                                                 # (local)
        "gate_id": GATE_ID,
        "trigger": "[AUDIT]",
        "classification": "NON-PHONONIC (methodology-floor F-image)",
        "live_audit": audit_result,
        "self_test": {
            "all_pass": st["all_pass"],
            "n_assertions": len(st["assertions"]),
            "assertions": st["assertions"],
        },
        "dual_sha": {
            "audit_sha256": audit_sha,
            "content_sha256": content_sha,
            "input_pin_map": pinmap,
        },
        "verdict_semantics": {
            "live_verdict": audit_result["verdict"],
            "live_verdict_class": audit_result.get("verdict_class"),
            "genuinely_defective_count": audit_result.get("genuinely_defective_count"),
            "legitimately_pending_count": audit_result.get("legitimately_pending_count"),
            "self_non_bridge_count": audit_result.get("self_non_bridge_count"),
            "superseded_count": audit_result.get("superseded_count"),
            "n_pass": audit_result.get("n_pass"),
            "note": (
                "Live registry FAIL because genuinely_defective > 0; the "
                "genuinely-defective set is NAMED for mack-cosmic-bridge "
                "OE-form/tier retrofit (sole registry writer per "
                "feedback_mack-bridge-role.md). Self-test proves the classifier "
                "emits PASS-WITH-N-PENDING with genuinely_defective == 0 after "
                "the retrofit (synthetic fixture)."
            ),
        },
    }
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(json.dumps(report, indent=2, default=str),
                        encoding="utf-8")

    # --- 5. Verdict value string (compact, audit-greppable) ---
    gd_anchors = [                                              # (local)
        gd["section_anchor"].split("—")[0].strip().lstrip("# ").strip()
        for gd in audit_result.get("genuinely_defective", [])
    ]
    value = (                                                  # (local)
        f"live_verdict={audit_result['verdict']};"
        f"n_bridge={audit_result.get('n_bridge_sections')};"
        f"PASS={audit_result.get('n_pass')};"
        f"legitimately_pending={audit_result.get('legitimately_pending_count')};"
        f"genuinely_defective={audit_result.get('genuinely_defective_count')};"
        f"self_non_bridge={audit_result.get('self_non_bridge_count')};"
        f"superseded={audit_result.get('superseded_count')};"
        f"defective_set={gd_anchors};"
        f"selftest_all_pass={st['all_pass']}({len(st['assertions'])}_assertions);"
        f"verdict_strings_supported=PASS|PASS-WITH-N-PENDING|FAIL"
    )

    # The script HEALTH is independent of the scientific verdict: FAIL is a valid
    # pre-registered outcome (genuinely_defective > 0 on the live registry).
    # Compose the gate verdict: the gate PASSES iff the classifier extension is
    # in place AND the self-test all-passes (the EXTENSION is the deliverable);
    # the LIVE-registry FAIL is reported in the value string + JSON and routed to
    # mack. Per FAIL_meaning, the audit's live verdict is FAIL until the retrofit
    # lands; we emit the gate verdict = the live audit verdict (FAIL), which is
    # the honest pre-registered outcome.
    if not st["all_pass"]:
        gate_verdict = "FAIL"                                  # (local) extension itself broken
    else:
        gate_verdict = audit_result["verdict"]                 # (local) live audit verdict
        if gate_verdict.startswith("PASS-WITH-"):
            gate_verdict = "PASS"                              # canonical top-line for non-FAIL

    append_verdict(gate_verdict, value, audit_sha, content_sha)

    # Console summary (stdout; verdict is DATA in the file, not the exit code).
    print(f"GATE {GATE_ID}")
    print(f"  live audit verdict: {audit_result['verdict']}")
    print(f"  n_bridge={audit_result.get('n_bridge_sections')} "
          f"PASS={audit_result.get('n_pass')} "
          f"pending={audit_result.get('legitimately_pending_count')} "
          f"defective={audit_result.get('genuinely_defective_count')} "
          f"self_non_bridge={audit_result.get('self_non_bridge_count')} "
          f"superseded={audit_result.get('superseded_count')}")
    print(f"  self-test all_pass: {st['all_pass']} "
          f"({len(st['assertions'])} assertions)")
    print(f"  gate verdict emitted: {gate_verdict}")
    print(f"  audit_sha256={audit_sha}")
    print(f"  content_sha256={content_sha}")
    print(f"  JSON report: {JSON_OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
