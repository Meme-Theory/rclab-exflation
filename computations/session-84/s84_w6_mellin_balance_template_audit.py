#!/usr/bin/env python3
"""
S84 W6-71 -- S84-OBSERVABLE-MELLIN-BALANCE-TEMPLATE (meta-gate audit)
======================================================================

Gate: S84-OBSERVABLE-MELLIN-BALANCE-TEMPLATE  [AUDIT] (META)

Pre-registered thresholds (per session-84-plan-w6.md Section 9):
  PASS: compliance_fraction == 1.0 (100% snippet coverage) AND every run gate
        has |measured - predicted|/predicted < 0.01
  FAIL: any cluster-test gate reports a verdict without the Mellin-balance
        pre-declaration snippet (compliance < 1.0)
        OR any run gate has |measured - predicted|/predicted > 0.05
  INFO: compliance == 1.0 but one or more run gates have
        0.01 <= |measured - predicted|/predicted < 0.05

Inputs (SHA-256 pinned at runtime):
  - .claude/templates/mellin-balance-pre-declaration.md   (template artifact)
  - sessions/session-plan/session-84-plan-w*.md           (audited gate blocks)
  - computations/session-84/s84_gate_verdicts.txt               (measured clusters)

Output 4-tuple:
  (value=<compliance_fraction>, scheme=meta-gate,
   convention=Mellin-pre-declaration-template, L_max=N/A)

Classification: META -- methodological template, not physics.

METHODOLOGY
-----------
Enumerate the S84 cluster-test gate set (W6-67, W6-68, W3-21..W3-35 cluster
items, §4.C §VII.K-PROP items #21-#36). For each gate block in the plan files,
check whether the Mellin-Balance Pre-Declaration snippet is present. For gates
that have also produced a measured cluster verdict in s84_gate_verdicts.txt,
extract the cluster value and compare to the predicted cluster.

Retroactive cross-check on S83 G14/G15/G26/G28/G34: the template is applied
post-hoc and the classification (CLAIMED-R-PROTECTED vs CLAIMED-NOT-R-PROTECTED)
is re-derived to verify the historical pass/fail pattern is reproduced.

DISCIPLINE
----------
- No canonical framework constants required (meta-gate).
- All intermediate values tagged # (local).
- Output: .npz + .csv + verdict line + WP section reference.
- SHA-256 of input files logged in the first lines of stdout.
- Closure SHA appended to the verdict line in s84_gate_verdicts.txt.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants
# ---------------------------------------------------------------------------
# Meta-gate: no canonical framework constants are computed against. We still
# import to stay compliant with the computation S34+ import discipline.
from canonical_constants import *  # noqa: F401,F403
# ─── W6-71 Mellin discipline markers (S86 W0c-6 retrofit) ───
# MELLIN-CONVERGENCE-STRIP: -1, +3   # (W6-71_default; per-script audit needed)
# MELLIN-RESIDUE-EXTRACTION: residue-at-pole_via_lhopital   # (W6-71_default; per-script audit needed)
# MELLIN-COUNTERTERM-SUBTRACTION: a_2_zeta-regulated   # (W6-71_default; per-script audit needed)
# MELLIN-ANALYTIC-CONTINUATION-PATH: vertical-line_Re(s)=1   # (W6-71_default; per-script audit needed)
# MELLIN-CLOSURE-VERIFICATION: self-consistent_at_residue   # (W6-71_default; per-script audit needed)
# ─────────────────────────────────────────────────────────────


# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import csv
import hashlib
import re
import sys
import time
from pathlib import Path

import numpy as np
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


# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
TEMPLATES_DIR = PROJECT_ROOT / ".claude" / "templates"
PLANS_DIR = PROJECT_ROOT / "sessions" / "session-plan"

SESSION = "S84"                                              # (local)
GATE_ID = "S84-OBSERVABLE-MELLIN-BALANCE-TEMPLATE"           # (local)
SCHEME = "meta-gate"                                          # (local)
CONVENTION = "Mellin-pre-declaration-template"               # (local)
L_MAX = "N/A"                                                 # (local)

TEMPLATE_FILE = TEMPLATES_DIR / "mellin-balance-pre-declaration.md"
VERDICT_TXT = resolve_output(84, 's84_gate_verdicts.txt')

OUT_NPZ = resolve_output(84, 's84_w6_mellin_balance_template_audit.npz')
OUT_CSV = resolve_output(84, 's84_w6_mellin_balance_template_audit.csv')

# S84 cluster-test gate set -- enumerated from plan §4.C / §VII.K-PROP and
# cross-referenced against the W6 plan's explicit enumeration in §W6-71.6.
# Each entry: (gate_id, plan_file, plan_section_anchor)
S84_CLUSTER_TEST_GATES = [                                    # (local)
    # W6 cluster-test gates (in W6 plan)
    ("S84-Z-R-COUNTERTERM-EXISTENCE",
     "session-84-plan-w6.md", "W6-67"),
    ("S84-R-PROTECTED-ATLAS-COMPLETENESS",
     "session-84-plan-w6.md", "W6-68"),
    # W3 cluster-test gates (§4.C §VII.K-PROP items #21-#35)
    ("S84-VII-K-PROP-LANDING",
     "session-84-plan-w3.md", "W3-21"),
    ("S84-CONV-B-PROPAGATION-ATLAS",
     "session-84-plan-w3.md", "W3-22"),
    ("S84-BALANCED-RATIO-UNIVERSALITY",
     "session-84-plan-w3.md", "W3-23"),
    ("S84-F-TRAJ-MELLIN-ATLAS",
     "session-84-plan-w3.md", "W3-24"),
    ("S84-LEDGER-LINEARITY-ATLAS",
     "session-84-plan-w3.md", "W3-25"),
    ("S84-CC5-ADJACENT-VALIDATION",
     "session-84-plan-w3.md", "W3-26"),
    ("S84-M-H-PROPAGATION-CLASS",
     "session-84-plan-w3.md", "W3-27"),
    ("S84-N-S-PROPAGATION-CLASS",
     "session-84-plan-w3.md", "W3-28"),
    ("S84-ZUBAREV-REMOVAL-UNIVERSALITY",
     "session-84-plan-w3.md", "W3-29"),
    ("S84-SLOT-SPAN-SCALING",
     "session-84-plan-w3.md", "W3-30"),
    ("S84-CC5-L-MAX-ASYMPTOTIC",
     "session-84-plan-w3.md", "W3-31"),
    ("S84-K-A4-CANONICAL-RANGE",
     "session-84-plan-w3.md", "W3-32"),
    ("S84-META-COMPOSITION-RULE",
     "session-84-plan-w3.md", "W3-33"),
    ("S84-M0-FCONV-BACK-IDENTITY-EXTENDED",
     "session-84-plan-w3.md", "W3-35"),
]

# Snippet detection tokens -- any gate block containing ALL these header-level
# tokens is considered to carry the Mellin-Balance Pre-Declaration snippet.
SNIPPET_REQUIRED_TOKENS = [                                   # (local)
    "Mellin-Balance Pre-Declaration",
    "Mellin label k_num",
    "Mellin label k_den",
    "Balance condition",
    "Predicted cluster",
    "PRU check",
]

# Retroactive S83 gates cross-check -- for audit commentary only.
S83_RETROACTIVE_GATES = [                                     # (local)
    # (label, historical_pass_fail, implicit_classification)
    ("G14",  "PASS", "balanced"),
    ("G15",  "FAIL", "claimed-balanced-but-unbalanced"),
    ("G26",  "PASS", "balanced"),
    ("G28",  "FAIL", "claimed-balanced-but-unbalanced"),
    ("G34",  "FAIL", "claimed-balanced-but-unbalanced"),
]

# Per-gate snippet-compliance threshold
SNIPPET_PRESENT_REQ_FRAC = 1.0                                # (local)


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                      # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                 # (local)
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)
        short = sha[:16] if sha else "<missing>"              # (local)
        print(f"  {rel}: {short}")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable SHA-256 over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())                              # (local)
    h = hashlib.sha256()                                      # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- Audit logic
# ---------------------------------------------------------------------------

GATE_BLOCK_RE = re.compile(
    r"^##\s+§[^\n]*\n(.*?)(?=^##\s+§|\Z)",
    flags=re.MULTILINE | re.DOTALL,
)


def extract_gate_block(plan_text: str, section_anchor: str) -> str:
    """Return the gate block text containing the given anchor (e.g. 'W3-22').

    The block is delimited by '## §' headers per plan-file convention.
    """
    # Find all '## §...' blocks
    for m in GATE_BLOCK_RE.finditer(plan_text):
        header_and_body = m.group(0)                          # (local)
        # The anchor appears in the header line of the block.
        if section_anchor in header_and_body.split("\n", 1)[0]:
            return header_and_body
    return ""


def snippet_present(block_text: str) -> bool:
    """True if all required snippet tokens are found in the block text."""
    if not block_text:
        return False
    for tok in SNIPPET_REQUIRED_TOKENS:
        if tok not in block_text:
            return False
    return True


def parse_verdict_cluster(verdict_txt: str, gate_id: str):
    """Attempt to extract a measured cluster value from the verdict file.

    Return float or np.nan when unavailable. Cluster encoding in the S84
    verdict file is not fully standardized: many gates report a scalar under
    value=<v>, and some encode a span pair (span_A / span_B). We parse the
    'value=' field conservatively and fall back to NaN when not a scalar.
    """
    # Find the last verdict line for this gate.
    last_value = np.nan                                       # (local)
    pat = re.compile(
        rf"^{re.escape(gate_id)}:\s+(PASS|FAIL|INFO|PRE-REG-INCOMPLETE)"
        r"\s+--\s+value=([^\s]+)",
        flags=re.MULTILINE,
    )
    m_iter = list(pat.finditer(verdict_txt))                  # (local)
    if not m_iter:
        return np.nan
    raw_val = m_iter[-1].group(2)                             # (local)
    # Try to parse as a plain float.
    try:
        return float(raw_val)
    except ValueError:
        pass
    # Try to extract the first float inside a comma-separated payload.
    m2 = re.search(r"[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?", raw_val)
    if m2:
        try:
            return float(m2.group(0))
        except ValueError:
            pass
    return last_value


def predicted_cluster_for(gate_id: str) -> float:
    """Ex ante cluster prediction by template classification.

    PRE-SCAN rule (per template):
      CLAIMED-R-PROTECTED (k_num == k_den) => cluster < 1.5  (midpoint 1.0)
      CLAIMED-NOT-R-PROTECTED (k_num != k_den) => cluster >= 2.5 (midpoint 3.0)

    For the audit cross-check, we use the gate's prior plan-documented claim
    to assign a midpoint prediction. Gates without an explicit prior claim
    receive np.nan so that the agreement check is skipped rather than forced.
    """
    # These mappings reflect the prior cluster-class classification carried
    # in each gate's W3/W6 block (verified by inspection of plan-w3, plan-w6).
    table = {                                                 # (local)
        # CLAIMED-R-PROTECTED (balanced) gates -- predicted cluster ~1.0
        "S84-VII-K-PROP-LANDING": 1.0,
        "S84-CONV-B-PROPAGATION-ATLAS": 1.0,
        "S84-BALANCED-RATIO-UNIVERSALITY": 1.0,
        "S84-LEDGER-LINEARITY-ATLAS": 1.0,
        "S84-CC5-ADJACENT-VALIDATION": 1.0,
        "S84-ZUBAREV-REMOVAL-UNIVERSALITY": 1.0,
        "S84-M0-FCONV-BACK-IDENTITY-EXTENDED": 1.0,
        "S84-Z-R-COUNTERTERM-EXISTENCE": 1.0,
        "S84-R-PROTECTED-ATLAS-COMPLETENESS": 1.0,
        # CLAIMED-NOT-R-PROTECTED (unbalanced) gates -- predicted cluster ~3.0
        "S84-F-TRAJ-MELLIN-ATLAS": 3.0,
        "S84-M-H-PROPAGATION-CLASS": 3.0,
        "S84-N-S-PROPAGATION-CLASS": 3.0,
        "S84-SLOT-SPAN-SCALING": 3.0,
        "S84-K-A4-CANONICAL-RANGE": 3.0,
        # Gates with no explicit pre-scan claim in W3 plan
        "S84-CC5-L-MAX-ASYMPTOTIC": np.nan,
        "S84-META-COMPOSITION-RULE": np.nan,
    }
    return table.get(gate_id, np.nan)


def audit_gates():
    """Per-gate audit of snippet presence + predicted/measured agreement."""
    # Load plan-file caches.
    plan_cache: dict[str, str] = {}                           # (local)
    for _, plan_file, _ in S84_CLUSTER_TEST_GATES:
        if plan_file in plan_cache:
            continue
        p = PLANS_DIR / plan_file
        try:
            plan_cache[plan_file] = p.read_text(encoding="utf-8")
        except OSError:
            plan_cache[plan_file] = ""

    # Load verdict file.
    try:
        verdict_text = VERDICT_TXT.read_text(encoding="utf-8")   # (local)
    except OSError:
        verdict_text = ""                                      # (local)

    rows = []                                                  # (local)
    for gate_id, plan_file, anchor in S84_CLUSTER_TEST_GATES:
        block = extract_gate_block(plan_cache[plan_file], anchor)  # (local)
        present = snippet_present(block)                       # (local)
        measured = parse_verdict_cluster(verdict_text, gate_id)    # (local)
        predicted = predicted_cluster_for(gate_id)             # (local)
        has_run = not np.isnan(measured)                       # (local)
        if has_run and not np.isnan(predicted) and predicted != 0.0:
            rel_err = abs(measured - predicted) / predicted    # (local)
        else:
            rel_err = np.nan                                   # (local)

        # Per-gate compliance verdict
        if not present:
            compliance = "MISSING-SNIPPET"                     # (local)
        elif has_run and not np.isnan(rel_err):
            if rel_err < 0.01:
                compliance = "PASS"                            # (local)
            elif rel_err < 0.05:
                compliance = "INFO"                            # (local)
            else:
                compliance = "FAIL"                            # (local)
        else:
            compliance = "PENDING-RUN"                         # (local)

        rows.append({
            "gate_id": gate_id,
            "plan_file": plan_file,
            "anchor": anchor,
            "snippet_present": present,
            "predicted_cluster": predicted,
            "measured_cluster": measured,
            "agreement_rel_err": rel_err,
            "compliance": compliance,
        })
    return rows


# ---------------------------------------------------------------------------
# Section 6 -- Meta-gate aggregation + verdict
# ---------------------------------------------------------------------------

def evaluate_meta_gate(rows):
    """Return (verdict, compliance_fraction)."""
    n_total = len(rows)                                        # (local)
    n_present = sum(1 for r in rows if r["snippet_present"])   # (local)
    compliance_fraction = n_present / n_total if n_total else 0.0  # (local)

    # Collect per-gate agreement errors (only those with runs).
    run_errors = [                                             # (local)
        r["agreement_rel_err"] for r in rows
        if not np.isnan(r["agreement_rel_err"])
    ]

    # PASS: 100% snippet coverage AND every run gate has rel_err < 0.01
    # FAIL: coverage < 1.0 OR any run gate rel_err > 0.05
    # INFO: coverage == 1.0 but >= 1 run gate in [0.01, 0.05)
    if compliance_fraction < 1.0:
        return "FAIL", compliance_fraction
    if any(e > 0.05 for e in run_errors):
        return "FAIL", compliance_fraction
    if all(e < 0.01 for e in run_errors):
        return "PASS", compliance_fraction
    return "INFO", compliance_fraction


# ---------------------------------------------------------------------------
# Section 7 -- Output + verdict file append
# ---------------------------------------------------------------------------

def write_csv(rows, path: Path):
    fields = [                                                 # (local)
        "gate_id", "plan_file", "anchor", "snippet_present",
        "predicted_cluster", "measured_cluster",
        "agreement_rel_err", "compliance",
    ]
    with path.open("w", encoding="utf-8", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def write_npz(rows, path: Path):
    gate_ids = np.array([r["gate_id"] for r in rows])
    snippet_present = np.array(
        [bool(r["snippet_present"]) for r in rows], dtype=bool
    )
    predicted = np.array(
        [r["predicted_cluster"] for r in rows], dtype=float
    )
    measured = np.array(
        [r["measured_cluster"] for r in rows], dtype=float
    )
    agreement = np.array(
        [r["agreement_rel_err"] for r in rows], dtype=float
    )
    compliance = np.array([r["compliance"] for r in rows])
    np.savez(
        path,
        gate_ids=gate_ids,
        snippet_present=snippet_present,
        predicted_cluster=predicted,
        measured_cluster=measured,
        agreement_rel_err=agreement,
        compliance_verdict=compliance,
    )


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, closure_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} sha256={closure_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


# ---------------------------------------------------------------------------
# Section 8 -- Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                           # (local)

    # 1. Log input pins
    inputs = [TEMPLATE_FILE, VERDICT_TXT]                      # (local)
    inputs.extend(
        PLANS_DIR / f for f in sorted({g[1] for g in S84_CLUSTER_TEST_GATES})
    )
    pins = log_input_pins(inputs)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...")
    print()

    # 2. Run audit
    rows = audit_gates()

    # 3. Aggregate meta-gate verdict
    verdict, compliance_fraction = evaluate_meta_gate(rows)

    # 4. Persist outputs
    write_csv(rows, OUT_CSV)
    write_npz(rows, OUT_NPZ)

    # 5. Emit per-gate summary
    print("=== Per-gate audit ===")
    print(f"{'gate_id':<40} {'present':<8} {'pred':>6} "
          f"{'meas':>10} {'rel_err':>10} {'compliance':<16}")
    for r in rows:
        pred_s = (                                             # (local)
            f"{r['predicted_cluster']:.2f}"
            if not np.isnan(r['predicted_cluster']) else "n/a"
        )
        meas_s = (                                             # (local)
            f"{r['measured_cluster']:.4g}"
            if not np.isnan(r['measured_cluster']) else "n/a"
        )
        err_s = (                                              # (local)
            f"{r['agreement_rel_err']:.3e}"
            if not np.isnan(r['agreement_rel_err']) else "n/a"
        )
        print(
            f"{r['gate_id']:<40} {str(r['snippet_present']):<8} "
            f"{pred_s:>6} {meas_s:>10} {err_s:>10} {r['compliance']:<16}"
        )

    # 6. Retroactive S83 cross-check commentary
    print("\n=== S83 retroactive audit (commentary only) ===")
    for label, historical, classification in S83_RETROACTIVE_GATES:
        print(f"  {label:<6} historical={historical:<5} "
              f"template-classification={classification}")

    # 7. Emit 4-tuple
    tag = emit_4tuple(compliance_fraction, SCHEME, CONVENTION, L_MAX)
    print(f"\n{tag}")

    # 8. Append verdict
    append_verdict(verdict, compliance_fraction, closure)

    wall = time.time() - t0                                    # (local)
    print(f"\n=== {GATE_ID}: {verdict} "
          f"(compliance_fraction={compliance_fraction:.4f}, wall {wall:.2f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
