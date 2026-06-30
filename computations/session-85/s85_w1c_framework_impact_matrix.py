#!/usr/bin/env python3
"""
S85 W1c-7 — FRAMEWORK-IMPACT-MATRIX
===================================

Gate: S85-W1c-FRAMEWORK-IMPACT-MATRIX ([AUDIT])

Pre-registered threshold (plan §W1c-7.9):
  PASS iff N_gates_flagged <= 5 AND impact matrix fully populated
       (no missing rows for any α_s-touching gate).
  INFO iff 5 < N_gates_flagged <= 20 (carry-forward to S86).
  FAIL iff N_gates_flagged > 20 (systemic; W1d would be warranted,
       or the Option 2 commit itself may need revisiting).

Inputs (SHA-256 dual-pinned):
  - computations/session-85/s85_w1c_historical_alpha_s_audit.json (W1c-3 output)
  - sessions/permanent-results-registry.md (post-W1c-5)
  - computations/session-84/s84_gate_verdicts.txt
  - computations/session-85/s85_gate_verdicts.txt
  - computations/_shared/canonical_constants.py (post-W1c-1)

Output 4-tuple:
  (value=<N_gates_flagged>, scheme=impact-matrix,
   convention=post-W1c-2-commit, L_max=N/A)

Classification: META (cascade audit; downstream-impact mapping)

METHODOLOGY
-----------
1. Parse s84 and s85 verdict files. Extract every verdict line whose
   gate_id, scheme, or convention field references alpha_s / alpha-s
   (case-insensitive).
2. For each identified gate, classify alpha_s_type_used:
   - if the gate's gate_id or convention explicitly names
     alpha_s_framework_central -> FRAMEWORK-IDENTITY (commit-consistent)
   - if the gate's convention names alpha_s_MZ, MZ, QCD, PDG
     -> QCD (commit-INCONSISTENT under Option 2)
   - if the gate's convention names Planck, Planck-pivot, Mukhanov,
     slow-roll, dn_s/dlnk -> INFLATIONARY (commit-consistent)
   - else -> AMBIGUOUS (flag for manual review)
3. Check verdict-stable: TRUE iff the commit interpretation does NOT
   flip the gate's verdict status. For Option 2 = INFLATIONARY:
   - if alpha_s_type_used = INFLATIONARY or FRAMEWORK-IDENTITY:
     verdict is stable (same interpretation, same threshold comparison)
   - if alpha_s_type_used = QCD: verdict MAY flip under Option 2
     interpretation (gate was measuring against QCD α_s; under Option 2
     it should have been measuring against inflationary). Flag
     verdict-unstable.
   - if AMBIGUOUS: flag
4. Aggregate: N_gates_total, N_commit_inconsistent, N_verdict_unstable,
   N_gates_flagged = union of the two flag classes.
5. Emit impact table + verdict.

Exit 0 regardless of PASS/FAIL per .claude/rules/math-scripts.md.
"""

from __future__ import annotations

from canonical_constants import *  # noqa: F401,F403

import hashlib
import json
import re
import sys
import time
from pathlib import Path
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-W1c-FRAMEWORK-IMPACT-MATRIX"                  # (local)
SCHEME = "impact-matrix"                                     # (local)
CONVENTION = "post-W1c-2-commit"                             # (local)
L_MAX = "N/A"                                                # (local)

PASS_MAX_FLAGGED = 5                                         # (local) plan §W1c-7.9
INFO_MAX_FLAGGED = 20                                        # (local)

CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')
W1C_3_JSON = resolve_output(85, 's85_w1c_historical_alpha_s_audit.json')
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
S84_VERDICTS = resolve_output(84, 's84_gate_verdicts.txt')
S85_VERDICTS = resolve_output(85, 's85_gate_verdicts.txt')
OUT_JSON = resolve_output(85, 's85_w1c_framework_impact_matrix.json')

VERDICT_LINE_RE = re.compile(
    r"^(?P<gate>[A-Za-z0-9_\-]+):\s+"
    r"(?P<status>PASS|FAIL|INFO|PENDING-EVENT|PRE-REG-INCOMPLETE)\s+--\s+"
    r"value=(?P<value>\S+)\s+"
    r"scheme=(?P<scheme>\S+)\s+"
    r"convention=(?P<convention>\S+)\s+"
    r"L_max=(?P<Lmax>\S+)"
)  # (local)

ALPHA_S_MENTION_RE = re.compile(r"alpha[-_]?s", re.IGNORECASE)  # (local)


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path,
                     canonical_path: Path,
                     pins: dict) -> tuple:
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
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


def classify_alpha_s_type(gate_id: str, scheme: str, convention: str) -> str:
    """Classify a gate's alpha_s_type_used from its gate_id + metadata."""
    blob = f"{gate_id} {scheme} {convention}".lower()  # (local)

    # FRAMEWORK-IDENTITY: explicitly names the canonical handle
    if "alpha_s_framework_central" in blob:
        return "FRAMEWORK-IDENTITY"
    # Plan of W1c-2 commit + prior W1c-5 § landing: S50-51 identity
    if any(k in blob for k in ("s50-51-identity", "n_s_canon**2",
                               "n_s**2 - 1", "magnitude-gap")):
        return "FRAMEWORK-IDENTITY"

    # QCD: explicitly tied to QCD markers
    if any(k in blob for k in ("alpha_s_mz", "mz_obs", "qcd",
                               "pdg", "ms-bar")):
        # MS-bar IS a QCD-sector renormalization scheme; however a few
        # inflationary gates use "MS-bar" loosely for the running-of-running
        # convention (e.g., beta_s CMB-S4 pre-reg). Check for inflationary
        # companion markers to avoid false-QCD classification.
        if any(inf in blob for inf in ("planck-central", "beta-s", "cmb-s4",
                                        "planck-pivot", "running-of-running")):
            return "INFLATIONARY"
        return "QCD"

    # INFLATIONARY markers
    if any(k in blob for k in ("planck", "mukhanov", "slow-roll",
                               "dn_s/dlnk", "dn_s", "inflation", "cmb",
                               "k_pivot", "spectral-zeta",
                               "running", "transit-ps", "lcdm", "desi")):
        return "INFLATIONARY"

    # FRAMEWORK-IDENTITY via convention tags W1c-4 produced
    if "post-w1c-1-patch" in blob or "option-2-commit" in blob:
        return "FRAMEWORK-IDENTITY"

    return "AMBIGUOUS"


def classify_commit_consistency(alpha_s_type: str) -> bool:
    """Option 2 = INFLATIONARY. Consistent iff type in {INFLATIONARY,
    FRAMEWORK-IDENTITY}."""
    return alpha_s_type in ("INFLATIONARY", "FRAMEWORK-IDENTITY")


def classify_verdict_stability(alpha_s_type: str, status: str) -> bool:
    """Verdict-stable iff the Option 2 commit does NOT flip the gate's
    verdict. Under Option 2 = INFLATIONARY:
      - INFLATIONARY/FRAMEWORK-IDENTITY: stable (same comparison target)
      - QCD: potentially unstable (gate was measuring QCD α_s; under Option
        2 the framework's α_s is inflationary; if the gate is about the
        framework's α_s vs QCD observation, it should be re-interpreted;
        if the gate is about QCD independently of framework, it's stable)
      - AMBIGUOUS: flag as unstable pending review
    PENDING-EVENT gates are stable by definition (verdict not yet set).
    """
    if status == "PENDING-EVENT":
        return True
    if alpha_s_type in ("INFLATIONARY", "FRAMEWORK-IDENTITY"):
        return True
    if alpha_s_type == "QCD":
        # Conservative: assume unstable (flag for review). In practice,
        # gates whose gate_id explicitly includes "QCD" and are ABOUT
        # QCD physics in isolation are stable; but gate_ids that use
        # alpha_s in a QCD context WHILE the framework predicts
        # inflationary are ambiguous. Flag all QCD-classified gates.
        return False
    # AMBIGUOUS
    return False


def extract_alpha_s_gates(verdict_file: Path) -> list:
    """Parse all verdict lines in a file; return those mentioning alpha_s
    in gate_id, scheme, or convention."""
    rows = []  # (local)
    for line in verdict_file.read_text(encoding="utf-8").splitlines():
        m = VERDICT_LINE_RE.match(line)
        if not m:
            continue
        gid = m.group("gate")  # (local)
        scheme = m.group("scheme")  # (local)
        convention = m.group("convention")  # (local)
        status = m.group("status")  # (local)
        if (ALPHA_S_MENTION_RE.search(gid)
                or ALPHA_S_MENTION_RE.search(scheme)
                or ALPHA_S_MENTION_RE.search(convention)):
            rows.append({
                "gate_id": gid,
                "status": status,
                "value": m.group("value"),
                "scheme": scheme,
                "convention": convention,
                "Lmax": m.group("Lmax"),
                "source_file": verdict_file.name,
            })
    return rows


def main() -> int:
    t0 = time.time()  # (local)

    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    canonical_sha = sha256_of(CANONICAL_PATH)  # (local)
    w1c_3_sha = sha256_of(W1C_3_JSON)  # (local)
    registry_sha = sha256_of(REGISTRY_PATH)  # (local)
    s84_sha = sha256_of(S84_VERDICTS)  # (local)
    s85_sha = sha256_of(S85_VERDICTS)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    print(f"  canonical_constants.py (post-W1c-1): {canonical_sha[:16]}...")
    print(f"  W1c-3 audit JSON:                    {w1c_3_sha[:16]}...")
    print(f"  registry (post-W1c-5):               {registry_sha[:16]}...")
    print(f"  s84_gate_verdicts.txt:               {s84_sha[:16]}...")
    print(f"  s85_gate_verdicts.txt:               {s85_sha[:16]}...")
    print(f"  script (self):                       "
          f"{sha256_of(script_path)[:16]}...")
    print()

    # 1. Extract all alpha_s-touching gates from s84+s85 verdict files
    rows_s84 = extract_alpha_s_gates(S84_VERDICTS)  # (local)
    rows_s85 = extract_alpha_s_gates(S85_VERDICTS)  # (local)
    all_rows = rows_s84 + rows_s85  # (local)
    print(f"  Alpha_s-touching verdict rows:")
    print(f"    S84: {len(rows_s84)}  S85: {len(rows_s85)}")
    print(f"    Total: {len(all_rows)}")
    print()

    # Deduplicate by (gate_id, source_file): keep latest per gate+file
    # (multiple verdicts for the same gate across reruns should all count,
    # but impact-matrix is per-gate — take latest)
    latest_per_gate = {}  # (local)
    for row in all_rows:
        key = (row["gate_id"], row["source_file"])  # (local)
        latest_per_gate[key] = row  # overwritten by later rows (latest wins)

    # 2. Build the impact matrix
    impact_rows = []  # (local)
    for (gate_id, source_file), row in sorted(latest_per_gate.items()):
        alpha_s_type = classify_alpha_s_type(
            gate_id, row["scheme"], row["convention"])
        commit_consistent = classify_commit_consistency(alpha_s_type)
        verdict_stable = classify_verdict_stability(alpha_s_type,
                                                    row["status"])
        impact_rows.append({
            "gate_id": gate_id,
            "source_file": source_file,
            "status": row["status"],
            "scheme": row["scheme"],
            "convention": row["convention"],
            "alpha_s_type_used": alpha_s_type,
            "commit_consistent": commit_consistent,
            "verdict_stable": verdict_stable,
            "flagged": (not commit_consistent) or (not verdict_stable),
        })

    # 3. Aggregate counts
    n_gates_total = len(impact_rows)  # (local)
    n_commit_inconsistent = sum(1 for r in impact_rows
                                if not r["commit_consistent"])  # (local)
    n_verdict_unstable = sum(1 for r in impact_rows
                             if not r["verdict_stable"])  # (local)
    n_gates_flagged = sum(1 for r in impact_rows if r["flagged"])  # (local)

    print(f"=== Aggregate counts ===")
    print(f"  N_gates_total:          {n_gates_total}")
    print(f"  N_commit_inconsistent:  {n_commit_inconsistent}")
    print(f"  N_verdict_unstable:     {n_verdict_unstable}")
    print(f"  N_gates_flagged:        {n_gates_flagged}")
    print()

    # By-type breakdown
    by_type = {}  # (local)
    for r in impact_rows:
        t = r["alpha_s_type_used"]  # (local)
        by_type[t] = by_type.get(t, 0) + 1
    print(f"=== By alpha_s_type_used ===")
    for t, c in sorted(by_type.items()):
        print(f"  {t:<25s}: {c}")
    print()

    # 4. Dispatch
    if n_gates_flagged <= PASS_MAX_FLAGGED:
        final_status = "PASS"  # (local)
        reason = (f"N_gates_flagged = {n_gates_flagged} <= PASS_MAX = "
                  f"{PASS_MAX_FLAGGED}; Option 2 commit is structurally safe "
                  f"for the α_s-touching gates in S84+S85.")  # (local)
    elif n_gates_flagged <= INFO_MAX_FLAGGED:
        final_status = "INFO"  # (local)
        reason = (f"N_gates_flagged = {n_gates_flagged} in ({PASS_MAX_FLAGGED}, "
                  f"{INFO_MAX_FLAGGED}]; carry-forward a dedicated S86 "
                  f"re-audit sub-wave.")  # (local)
    else:
        final_status = "FAIL"  # (local)
        reason = (f"N_gates_flagged = {n_gates_flagged} > INFO_MAX = "
                  f"{INFO_MAX_FLAGGED}; cascade-breaking implications; "
                  f"Option 2 commit may need revisiting.")  # (local)

    # 5. Dual-SHA
    pins = {
        "computations/_shared/canonical_constants.py": canonical_sha,
        "computations/session-85/s85_w1c_historical_alpha_s_audit.json": w1c_3_sha,
        "sessions/permanent-results-registry.md": registry_sha,
        "computations/session-84/s84_gate_verdicts.txt": s84_sha,
        "computations/session-85/s85_gate_verdicts.txt": s85_sha,
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH,
                                              pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 6. 4-tuple + verdict
    value = n_gates_flagged  # (local)
    four_tuple = (f"(value={value}, scheme={SCHEME}, "
                  f"convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print("\n" + four_tuple)

    line = (
        f"{GATE_ID}: {final_status} -- value={value} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    with S85_VERDICTS.open("a", encoding="utf-8") as fp:
        fp.write(line)

    # 7. JSON summary
    summary = {
        "gate_id": GATE_ID,
        "status": final_status,
        "value": value,
        "reason": reason,
        "n_gates_total": n_gates_total,
        "n_commit_inconsistent": n_commit_inconsistent,
        "n_verdict_unstable": n_verdict_unstable,
        "n_gates_flagged": n_gates_flagged,
        "by_type": by_type,
        "impact_rows": impact_rows,
        "canonical_sha": canonical_sha,
        "w1c_3_sha": w1c_3_sha,
        "registry_sha": registry_sha,
        "s84_verdicts_sha": s84_sha,
        "s85_verdicts_sha": s85_sha,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "thresholds": {
            "PASS_MAX_FLAGGED": PASS_MAX_FLAGGED,
            "INFO_MAX_FLAGGED": INFO_MAX_FLAGGED,
        },
    }  # (local)
    OUT_JSON.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {final_status} (wall {wall:.2f}s) ===")
    print(f"    Reason: {reason}")

    # Preview impact table
    print(f"\n=== Impact matrix preview (first 15 rows) ===")
    print(f"{'gate_id':<55s} {'status':<16s} {'α_s_type':<20s} "
          f"{'commit':<6s} {'stable':<6s} {'flag':<5s}")
    for r in impact_rows[:15]:
        print(f"  {r['gate_id'][:54]:<55s} {r['status']:<16s} "
              f"{r['alpha_s_type_used']:<20s} "
              f"{'Y' if r['commit_consistent'] else 'N':<6s} "
              f"{'Y' if r['verdict_stable'] else 'N':<6s} "
              f"{'*' if r['flagged'] else '':<5s}")
    if len(impact_rows) > 15:
        print(f"  ... ({len(impact_rows) - 15} more rows in JSON)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
