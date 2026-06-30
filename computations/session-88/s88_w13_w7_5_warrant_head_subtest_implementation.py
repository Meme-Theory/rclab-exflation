"""
s88_w13_w7_5_warrant_head_subtest_implementation.py
====================================================

Gate: S88-W7-5-WARRANT-HEAD-SUBTEST-IMPLEMENTATION ([VERIFY])

Pre-registered threshold (plan §W13-165 lines 558-561):
  PASS  iff subtest_a ∧ subtest_b ∧ subtest_c ALL-PASS; SECONDARY composite operational.
  FAIL  iff ≥1 subtest FAILs.
  INFO  iff ≥1 subtest INFO (e.g., scheme-invariance margins close to threshold).

Inputs (SHA-256 dual-pinned per S84+ schema; W9a-99 split):
  - sessions/session-plan/session-88-plan-w13.md     (gate-block authority)
  - sessions/permanent-results-registry.md          (§VII-B.HP1-NEAR-INVARIANCE Step 1)
  - .claude/rules/regulator-convention-lockdown.md  (CAC convention)
  - computations/_shared/canonical_constants.py     (eps_H_HP1_norm, L_envelope_d4_Lmax10)
  - computations/session-88/s88_w7_warrant_check_eps_h_hp1_norm_v2.py
                                                    (HEAD; subtest_a/b/c implementation)

Output 4-tuple:
  (value=<composite verdict string>,
   scheme=warrant-check-3-subtest-substrate-first,
   convention=lizzi-CV-LZ-4-template-v2-fork,
   L_max=10)

Classification: GEOMETRIC (HP^1-cohomology-class structural identity at the
                methodology layer)

METHODOLOGY
-----------
Imports `s88_w7_warrant_check_eps_h_hp1_norm_v2.run_warrant_check`
(canonical sole executor for the subtests), captures the 3 subtest
verdicts and a substrate-first canonical-table summary, emits .npz + .png +
verdict line per gate-verdicts.md S84+ schema, then writes the WP §W13-165
section last.

DISCIPLINE
----------
- `from canonical_constants import *` (via subordinate module).
- All intermediates tagged `# (local)`.
- SHA-256 of all input files logged in first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- 4-tuple printed as the final non-verdict line.
- Verdict appended to `computations/session-88/s88_gate_verdicts.txt`
  (CANONICAL path per .claude/rules/gate-verdicts.md §"Canonical Verdict-File Path").
- Atomic single open("a") write per the canonical append_verdict pattern.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

# ---------------------------------------------------------------------------
# Section 1 — Paths
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent                                  # (local)
COMPUTATIONS_DIR = SESSION_DIR.parent                                          # (local)
SHARED_DIR = COMPUTATIONS_DIR / "_shared"                                      # (local)
PROJECT_ROOT = COMPUTATIONS_DIR.parent                                         # (local)

sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(SESSION_DIR))

from canonical_constants import eps_H_HP1_norm, L_envelope_d4_Lmax10           # noqa: E402
import numpy as np                                                              # noqa: E402
import matplotlib                                                                # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                                                 # noqa: E402

# Subtest executor (S88 W13-165 fork)
from s88_w7_warrant_check_eps_h_hp1_norm_v2 import (                          # noqa: E402
    run_warrant_check,
    EPS_H_HP1_CLAIM,
    F_4_ATLAS,
    ATLAS_5,
    F_4_STRICT_MAX_RATIO,
    ATLAS_5_LOOSE_MAX_RATIO,
    PLAN_REGULATOR_SCAN,
    L_MAX_SCAN,
)

# ---------------------------------------------------------------------------
# Section 2 — Pre-registration
# ---------------------------------------------------------------------------
SESSION = "S88"                                                                # (local)
GATE_ID = "S88-W7-5-WARRANT-HEAD-SUBTEST-IMPLEMENTATION"                       # (local)
SCHEME = "warrant-check-3-subtest-substrate-first"                             # (local)
CONVENTION = "lizzi-CV-LZ-4-template-v2-fork"                                  # (local)
L_MAX = 10                                                                     # (local) plan §W13-165 anchor

OUT_NPZ = SESSION_DIR / "s88_w13_w7_5_warrant_head_subtest_implementation.npz"
OUT_JSON = SESSION_DIR / "s88_w13_w7_5_warrant_head_subtest_implementation.json"
OUT_PNG = SESSION_DIR / "s88_w13_w7_5_warrant_head_subtest_implementation.png"

# Per .claude/rules/gate-verdicts.md §"Canonical Verdict-File Path (MANDATORY)":
# the ONE canonical location is computations/session-{N}/s{N}_gate_verdicts.txt.
VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"                            # (local)

# Input pin map — files whose SHA is included in the audit_sha256 closure.
PLAN_W13_PATH = (PROJECT_ROOT / "sessions" / "session-plan"                    # (local)
                 / "session-88-plan-w13.md")
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"    # (local)
REG_CONV_LOCKDOWN_PATH = (PROJECT_ROOT / ".claude" / "rules"                   # (local)
                          / "regulator-convention-lockdown.md")
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"                         # (local)
SUBTEST_MODULE_PATH = (SESSION_DIR                                             # (local)
                       / "s88_w7_warrant_check_eps_h_hp1_norm_v2.py")

INPUT_FILES = [                                                                # (local)
    PLAN_W13_PATH,
    REGISTRY_PATH,
    REG_CONV_LOCKDOWN_PATH,
    CANONICAL_PATH,
    SUBTEST_MODULE_PATH,
]


# ---------------------------------------------------------------------------
# Section 3 — SHA helpers
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                                       # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}                                                  # (local)
    for p in inputs:
        sha = sha256_of(p)                                                     # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")              # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())                                               # (local)
    h = hashlib.sha256()                                                       # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path,
                     canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""                                                         # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                                      # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(                                                  # (local)
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")

    h_audit = hashlib.sha256()                                                 # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                                # (local)

    h_content = hashlib.sha256()                                               # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                            # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 4 — Compute (delegates to v2 module)
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Execute SECONDARY composite via v2 module."""
    return run_warrant_check()


# ---------------------------------------------------------------------------
# Section 5 — Plot
# ---------------------------------------------------------------------------

def make_plot(result: dict, out_png: Path) -> None:
    """3-panel summary: subtest_a scheme-invariance bar; subtest_b L_max-stability;
    subtest_c witness predicate."""
    a = result["sub_results"]["a"]                                             # (local)
    b = result["sub_results"]["b"]                                             # (local)
    c = result["sub_results"]["c"]                                             # (local)

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))                          # (local)

    # Panel 1: subtest_a scheme-invariance (SURVEYED rel-dev vs threshold).
    ax1 = axes[0]
    schemes = list(a["per_scheme"].keys())                                     # (local)
    rel_devs = []                                                              # (local)
    colors = []                                                                # (local)
    for s in schemes:
        rd = a["per_scheme"][s]["rel_dev_vs_anchor"]                           # (local)
        if rd is None:
            rel_devs.append(0.0)
            colors.append("#cccccc")  # un-surveyed, grey
        else:
            rel_devs.append(rd)
            colors.append("#1f77b4")  # surveyed, blue
    bars = ax1.bar(schemes, rel_devs, color=colors)                            # (local)
    ax1.axhline(a["threshold"], color="r", linestyle="--",
                label=f"threshold={a['threshold']}")
    ax1.set_ylabel("rel-dev vs anchor")
    ax1.set_title(f"subtest_a scheme-invariance: {a['verdict']}")
    ax1.legend(loc="upper left", fontsize=8)
    ax1.tick_params(axis='x', rotation=20)
    # Annotate un-surveyed bars
    for bar, s in zip(bars, schemes):
        rd = a["per_scheme"][s]["rel_dev_vs_anchor"]                           # (local)
        if rd is None:
            ax1.annotate("not surveyed",
                         (bar.get_x() + bar.get_width() / 2, 0.001),
                         ha="center", va="bottom", fontsize=7, rotation=90)

    # Panel 2: subtest_b L_max-stability (envelope vs threshold).
    ax2 = axes[1]
    Ls = [int(k) for k in b["per_L"].keys()]                                   # (local)
    Ls.sort()
    envs = [b["per_L"][str(L)]["envelope"] for L in Ls]                        # (local)
    ax2.plot(Ls, envs, marker="o", color="#2ca02c", label="L^{-3} envelope")
    ax2.axhline(b["threshold"], color="r", linestyle="--",
                label=f"threshold={b['threshold']}")
    ax2.set_xlabel("L_max")
    ax2.set_ylabel("rel-dev envelope")
    ax2.set_title(f"subtest_b L_max-stability: {b['verdict']}")
    ax2.legend(fontsize=8)
    ax2.set_yscale("log")

    # Panel 3: subtest_c witness predicate (text panel).
    ax3 = axes[2]
    ax3.axis("off")
    rg_w = "Y" if c["registry_witness_present"] else "N"                       # (local)
    cn_w = "Y" if c["canonical_witness_present"] else "N"                      # (local)
    pv_dict = "Y" if c["machine_provenance_dict_present"] else "N"             # (local)
    txt = (
        f"subtest_c HP^1-membership: {c['verdict']}\n"
        f"\n"
        f"is_member_HP1_A_F : {c['is_member_HP1_A_F']}\n"
        f"registry_witness  : {rg_w} (§VII-B Step 1)\n"
        f"canonical_witness : {cn_w} (cc.py:155)\n"
        f"\n"
        f"PROVENANCE-dict gap (orthogonal):\n"
        f"machine_prov_dict : {pv_dict} (cc.py PROVENANCE has 126 keys;\n"
        f"                     eps_H_HP1_norm absent — carry-forward)\n"
    )
    ax3.text(0.0, 1.0, txt, va="top", ha="left", fontsize=9,
             family="monospace", transform=ax3.transAxes)
    ax3.set_title("subtest_c witness predicate")

    plt.suptitle(
        f"{GATE_ID}: composite={result['verdict']} "
        f"(anchor eps_H_HP1_norm = {eps_H_HP1_norm})",
        fontsize=10,
    )
    plt.tight_layout()
    plt.savefig(out_png, dpi=120, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 6 — Verdict + 4-tuple
# ---------------------------------------------------------------------------

def emit_4tuple(value: str) -> str:
    return (f"(value={value!r}, scheme={SCHEME}, "
            f"convention={CONVENTION}, L_max={L_MAX})")


def append_verdict(verdict: str, value: str,
                   audit_sha: str, content_sha: str) -> None:
    """Atomic single-shot append per S84+ dual-SHA schema (W9a-99 split).

    Per .claude/rules/gate-verdicts.md §"Canonical Verdict-File Path", target:
      computations/session-88/s88_gate_verdicts.txt
    """
    canonical_line = (                                                         # (local)
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion_line = (                                                         # (local)
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_line)


def evaluate_gate(result: dict) -> str:
    """Composite verdict from the v2 module.

    Pre-registered collapse rule (plan §W13-165 lines 558-561):
      PASS iff all 3 subtests PASS.
      FAIL iff ≥1 subtest FAILs.
      INFO iff ≥1 subtest INFO.
    """
    return result["verdict"]


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                           # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)                                         # (local)
    closure = closure_hash(pins)                                               # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Dual SHAs (S84+ schema)
    script_path = Path(__file__).resolve()                                     # (local)
    audit_sha, content_sha = compute_dual_sha(                                 # (local)
        script_path, CANONICAL_PATH, pins,
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute SECONDARY composite
    result = compute()                                                         # (local)

    # 3. Evaluate gate
    verdict = evaluate_gate(result)                                            # (local)

    # 4. Emit 4-tuple + append verdict
    value_str = (                                                              # (local)
        f"composite={verdict}|"
        f"a={result['sub_results']['a']['verdict']},"
        f"b={result['sub_results']['b']['verdict']},"
        f"c={result['sub_results']['c']['verdict']}"
    )
    tag = emit_4tuple(value_str)                                               # (local)
    print(tag)

    # 5. Persist artifacts
    np.savez(OUT_NPZ,
             audit_id=GATE_ID,
             composite_verdict=verdict,
             anchor_eps_H_HP1_norm=float(eps_H_HP1_norm),
             plan_regulator_scan=np.array(PLAN_REGULATOR_SCAN, dtype=object),
             F_4_atlas=np.array(F_4_ATLAS, dtype=object),
             Atlas_5=np.array(ATLAS_5, dtype=object),
             F_4_strict_max_ratio=F_4_STRICT_MAX_RATIO,
             Atlas_5_loose_max_ratio=ATLAS_5_LOOSE_MAX_RATIO,
             L_max_scan=np.array(L_MAX_SCAN),
             L_envelope_d4_Lmax10=float(L_envelope_d4_Lmax10),
             gate_threshold=float(EPS_H_HP1_CLAIM.gate_threshold),
             subtest_a_verdict=result["sub_results"]["a"]["verdict"],
             subtest_b_verdict=result["sub_results"]["b"]["verdict"],
             subtest_c_verdict=result["sub_results"]["c"]["verdict"],
             subtest_a_max_rel_dev=result["sub_results"]["a"]["surveyed_max_rel_dev"],
             subtest_b_max_envelope=result["sub_results"]["b"]["max_envelope"],
             subtest_c_membership=result["sub_results"]["c"]["is_member_HP1_A_F"],
             audit_sha256=audit_sha,
             content_sha256=content_sha,
             scheme=SCHEME,
             convention=CONVENTION,
             L_max=L_MAX,
             )
    with OUT_JSON.open("w", encoding="utf-8") as fp:
        json.dump({
            "audit_id": GATE_ID,
            "composite_verdict": verdict,
            "anchor": float(eps_H_HP1_norm),
            "scheme": SCHEME,
            "convention": CONVENTION,
            "L_max": L_MAX,
            "audit_sha256": audit_sha,
            "content_sha256": content_sha,
            "input_pins": pins,
            "result": result,
        }, fp, indent=2, default=str)

    make_plot(result, OUT_PNG)

    # 6. Append verdict line (canonical path; atomic single-shot)
    append_verdict(verdict, value_str, audit_sha, content_sha)

    # 7. Final summary
    wall = time.time() - t0                                                    # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    print(f"  subtest_a verdict: {result['sub_results']['a']['verdict']} "
          f"(surveyed_max_rel_dev={result['sub_results']['a']['surveyed_max_rel_dev']:.4f}, "
          f"threshold={result['sub_results']['a']['threshold']:.4f})")
    print(f"  subtest_b verdict: {result['sub_results']['b']['verdict']} "
          f"(max_envelope={result['sub_results']['b']['max_envelope']:.6f}, "
          f"threshold={result['sub_results']['b']['threshold']:.4f})")
    print(f"  subtest_c verdict: {result['sub_results']['c']['verdict']} "
          f"(is_member_HP1_A_F={result['sub_results']['c']['is_member_HP1_A_F']})")
    return 0  # All composites are valid scientific results; never fail-on-FAIL.


if __name__ == "__main__":
    sys.exit(main())
