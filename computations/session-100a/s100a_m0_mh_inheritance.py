#!/usr/bin/env python3
"""
S100a W4-13 S100a-M0-MH-INHERITANCE — M0 absolute-normalization m_H-residual provenance trace
=============================================================================================

Gate: S100a-M0-MH-INHERITANCE ([AUDIT])
Classification: GEOMETRIC (traces a scale anchor on the spectral triple, not an excitation)

Pre-registered outcome class:
  INFO-class report-only provenance trace — NO PASS/FAIL token. The SOLE outcome
  is a documented answer to: does the per-sector absolute mass normalization
  M0^{sector} inherit the framework's m_H over-prediction?
    branch (a): |s(h)|^2-anchored  -> LINEAR inheritance, dM0/M0 in [r_KK, r_tree]
    branch (b): independently anchored -> dM0/M0 = 0

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - canonical_constants.py (feeds audit_sha256; supplies m_H_obs, v_ew)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<trace payload>, scheme=KK-threshold-131.8-plus-tree-A10-134,
   convention=ABSOLUTE-NORMALIZATION-PROVENANCE-TRACE, L_max=N/A)

METHODOLOGY
-----------
(1) Establish the two m_H residuals EXACTLY (rational arithmetic, cross-checked
    against Sage QQ): r_KK = m_H^{KK}/m_H_obs - 1 = 1318/1251 - 1 = 67/1251;
    r_tree = m_H^{tree}/m_H_obs - 1 = 1340/1251 - 1 = 89/1251.
(2) Identify the anchor of M0^{sector}: per Item 6 (S100a-YUKAWA-OVERLAP-OFFDIAG,
    landed INFO — Jensen-fiber overlap kernel sets the per-sector Yukawa
    normalization envelope) and KK-THRESHOLD-64 (S64 W4-B, INFO — m_H = 131.8 GeV
    from KK threshold corrections to the |S|^2 mode of the fiber embedding;
    framework prediction lineage S28c), M0 is set by the SAME |s(h)|^2
    fiber-embedding |S|^2 transverse-oscillation mode that sets m_H.
(3) Linear propagation: m_H = v*sqrt(2*lambda_h) with lambda_h = (4/3) g_3^2(M_KK)
    * (a_4/a_2) (theorem A10, S62 Filter-Independence) => m_H ~ (scale)^1;
    M0 ~ (scale)^1. So dM0/M0 = dm_H/m_H to LEADING ORDER (first power, NOT
    squared — the residual rides the mass scale linearly).
(4) Propagated band: dM0/M0 in [+67/1251, +89/1251] = [+5.356%, +7.114%] IF
    |s(h)|^2-anchored (branch (a), the identified branch); 0 IF independently
    anchored (branch (b), e.g. direct M_KK anchoring downstream of |s(h)|^2).
(5) Honest-scope ledger feed: the fermion-mass RATIOS are clean substrate
    predictions; the absolute SCALE carries the documented Higgs-sector residual.
    The BCS threshold correction (~-7%, S62 THRESHOLD-62 / HIGGS-BCS-THRESHOLD-62,
    applied to g_3(M_KK) in the m_H chain, bringing 134 -> ~125) has been applied
    in the m_H discussion ONLY — it has NOT been applied to M0^{sector}.

SUBSTITUTION CHAIN (direction claim per plan §W4-13 item 7; MANDATORY)
----------------------------------------------------------------------
  Claim: "m_H is OVER-predicted by the framework (+5.36% KK-threshold / +7.11%
          tree); IF M0^{sector} is |s(h)|^2-anchored to the same mode that sets
          m_H, M0 inherits this residual LINEARLY."
  Def 1: m_H_obs   = 125.1 GeV   [canonical_constants.py m_H_obs, PDG 2024]
  Def 2: m_H^{KK}  = 131.8 GeV   [KK-THRESHOLD-64 gate value; |S|^2 fiber-embedding
                                  mode + KK threshold; S28c lineage]
  Def 3: m_H^{tree}= 134.0 GeV   [theorem A10 Filter-Independence; tree-level,
                                  cutoff-shape-independent]
  Def 4: M0^{sector} = overall per-sector scale set by the |s(h)|^2 fiber-embedding
         mode (Item 6). m_H is the |S|^2 transverse-oscillation of the SAME fiber
         embedding => shared anchor.
  Def 5 (propagation): m_H^2 = (4/3) g_3^2(M_KK) (a_4/a_2) v^2-structure =>
         m_H ~ (scale)^1; M0 ~ (scale)^1. So dM0/M0 = dm_H/m_H to leading order
         (LINEAR, first power — NOT squared).
  Substitute: r_KK   = 131.8/125.1 - 1 = 1318/1251 - 1 = 67/1251
  Simplify:   r_KK   = +0.0535572     = +5.356%   (4 s.f.)
  Substitute: r_tree = 134.0/125.1 - 1 = 1340/1251 - 1 = 89/1251
  Simplify:   r_tree = +0.0711431     = +7.114%   (4 s.f.)
  Canonical form: both residuals POSITIVE (m_H^{framework} > m_H_obs) => the
         framework OVER-predicts m_H; the BCS threshold correction (~-7%, S62)
         is the documented physical mechanism that would bring 134 -> ~125.
  Direction: r_KK, r_tree > 0 => if |s(h)|^2-anchored, dM0/M0 = +5.36%..+7.11%
         (M0 OVER-normalized by the same fraction). If independently anchored
         (e.g., to M_KK directly), dM0/M0 = 0.
  Conclusion: ledger records the band [+5.356%, +7.114%] CONDITIONAL on
         |s(h)|^2-anchoring (the identified branch (a)), vs 0 under independent
         anchoring. Report-only; no PASS/FAIL.

DISCIPLINE
----------
- `from canonical_constants import *`; framework m_H predictions pinned below as
  documented # (local) framework-prediction literals (NOT yet canonical at
  script-write time; canonical write-order promotes them via update_constant
  AFTER verdict emission, BEFORE any inventory row — math-scripts.md
  §"Canonical Write-Order").
- Exact rational arithmetic via fractions.Fraction, cross-checked against the
  Sage QQ MCP evaluation (67/1251, 89/1251; band width 22/1251).
- GPU path: N/A — scalar arithmetic, CPU (machinery pin GPU_path=CPU); thread
  cap set before numpy import.
- Verdict emitted via the emit_verdict knowledge-MCP tool (race-safe); this
  script only PRINTS the payload via print_verdict_payload. NO schema-v2
  3-tuple (report-only [AUDIT] INFO — sign/magnitude/regime omitted entirely).
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU path; cap before numpy import
os.environ.setdefault("MKL_NUM_THREADS", "8")

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

from canonical_constants import *  # noqa: F401,F403  (m_H_obs, v_ew, M_KK)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from fractions import Fraction

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Identity + pre-registration pins
# ---------------------------------------------------------------------------
SESSION = "100a"                                                    # (local)
GATE_ID = "S100a-M0-MH-INHERITANCE"                                 # (local)
SCHEME = "KK-threshold-131.8-plus-tree-A10-134"                     # (local)
CONVENTION = "ABSOLUTE-NORMALIZATION-PROVENANCE-TRACE"              # (local)
L_MAX = "N/A"                                                       # (local) no fresh diagonalization

# Framework m_H predictions — # (local) documented framework-prediction literals.
# NOT yet in canonical_constants.py at script-write time. Canonical write-order
# obligation (math-scripts.md §"Canonical Write-Order"): after verdict emission
# these are promoted via update_constant as m_H_FW_KK_threshold / m_H_FW_tree
# WITH PROVENANCE, BEFORE any falsifier-inventory row.
M_H_FW_KK_LOCAL = 131.8    # (local) GeV — KK-THRESHOLD-64 (S64 W4-B, INFO); S28c framework prediction; KK threshold corrections to the |S|^2 fiber-embedding mode
M_H_FW_TREE_LOCAL = 134.0  # (local) GeV — theorem A10 (S62 Filter-Independence; atlas-07): lambda_h=(4/3)g_3^2(M_KK)*(a_4/a_2), cutoff-shape-independent tree level

# Sage QQ cross-check pins (mcp__sage__sage_eval, this gate, exact rationals)
SAGE_R_KK_NUM, SAGE_R_KK_DEN = 67, 1251      # (local) r_KK exact = 67/1251
SAGE_R_TREE_NUM, SAGE_R_TREE_DEN = 89, 1251  # (local) r_tree exact = 89/1251
SAGE_BAND_NUM, SAGE_BAND_DEN = 22, 1251      # (local) band width exact = 22/1251

# Plan-quoted decimal cross-check values (plan §W4-13 substitution chain)
PLAN_RATIO_KK = 1.053557     # (local) plan-quoted 131.8/125.1 (6 d.p.)
PLAN_RATIO_TREE = 1.071143   # (local) plan-quoted 134.0/125.1 (6 d.p.)

OUT_NPZ = SESSION_DIR / "s100a_m0_mh_inheritance.npz"
OUT_PNG = SESSION_DIR / "s100a_m0_mh_inheritance.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema)
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
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()        # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Compute (report-only provenance trace)
# ---------------------------------------------------------------------------
def compute() -> dict:
    # --- (1) Exact residuals (Fraction == exact rational arithmetic) ---
    f_obs = Fraction(str(m_H_obs))            # (local) 1251/10 exact, from canonical m_H_obs
    f_kk = Fraction(str(M_H_FW_KK_LOCAL))     # (local) 1318/10 exact
    f_tree = Fraction(str(M_H_FW_TREE_LOCAL)) # (local) 1340/10 exact

    r_kk_exact = f_kk / f_obs - 1             # (local) exact rational residual
    r_tree_exact = f_tree / f_obs - 1         # (local)
    band_exact = r_tree_exact - r_kk_exact    # (local)

    # --- Cross-check 1: Sage QQ exact rationals (MCP, this gate) ---
    assert r_kk_exact == Fraction(SAGE_R_KK_NUM, SAGE_R_KK_DEN), \
        f"r_KK exact mismatch vs Sage QQ: {r_kk_exact} != 67/1251"
    assert r_tree_exact == Fraction(SAGE_R_TREE_NUM, SAGE_R_TREE_DEN), \
        f"r_tree exact mismatch vs Sage QQ: {r_tree_exact} != 89/1251"
    assert band_exact == Fraction(SAGE_BAND_NUM, SAGE_BAND_DEN), \
        f"band exact mismatch vs Sage QQ: {band_exact} != 22/1251"

    # --- Cross-check 2: plan-quoted 6-d.p. ratios ---
    ratio_kk = float(f_kk / f_obs)            # (local)
    ratio_tree = float(f_tree / f_obs)        # (local)
    assert abs(ratio_kk - PLAN_RATIO_KK) < 5e-7, ratio_kk
    assert abs(ratio_tree - PLAN_RATIO_TREE) < 5e-7, ratio_tree

    # --- Cross-check 3: both residuals POSITIVE (over-prediction direction) ---
    assert r_kk_exact > 0 and r_tree_exact > 0, "direction claim violated"

    r_kk = float(r_kk_exact)                  # (local) full float64
    r_tree = float(r_tree_exact)              # (local)

    # --- (2) Anchor identification (the provenance-trace content) ---
    # Branch (a) of the pre-registered hypothesis is the identified branch:
    # M0^{sector} IS |s(h)|^2-anchored. Evidence chain (substrate-first):
    anchor_evidence = [
        # (i) m_H IS the |S|^2 transverse-oscillation of the fiber embedding:
        "canonical_classes.py 'Higgs and EW cluster': framework prediction "
        "m_H = 131.8 GeV (KK threshold corrections to the |S|^2 mode of the "
        "fiber embedding)",
        # (ii) the 131.8 lineage: S28c prediction evaluated at KK-THRESHOLD-64
        "KK-THRESHOLD-64 (S64 W4-B, INFO): delta=2.35, m_H = 131.8 GeV at the "
        "Jensen-deformed fiber (KK-mode threshold correction structure; S28c)",
        # (iii) the per-sector Yukawa/mass normalization envelope is the SAME
        # fiber-embedding overlap object (Item 6, landed this session):
        "S100a-YUKAWA-OVERLAP-OFFDIAG (Item 6, INFO): per-sector Yukawa "
        "normalization from the Jensen-fiber |s(h)|^2 overlap kernel "
        "(JENSEN-FIBER-OVERLAP-SU3-HAAR); M0^{sector} rides the same "
        "fiber-embedding envelope whose transverse |S|^2 oscillation is m_H",
        # (iv) tree anchor: A10 filter-independence fixes the 134.0 endpoint
        "theorem A10 (S62, atlas-07 permanent): lambda_h = (4/3) g_3^2(M_KK) "
        "* (a_4/a_2), cutoff-shape-INDEPENDENT; m_H(tree) = v*sqrt(2*lambda) "
        "= 134.0 GeV",
    ]
    anchored = True  # (local) branch (a): |s(h)|^2-anchored — shared anchor with m_H

    # --- (3) Linear propagation (Def 5: first power, NOT squared) ---
    dM0_low = r_kk if anchored else 0.0       # (local) inherited band, low edge
    dM0_high = r_tree if anchored else 0.0    # (local) inherited band, high edge
    dM0_independent = 0.0                     # (local) branch (b) reference value

    # --- (5) BCS threshold correction bookkeeping (honest-scope note) ---
    bcs_note = (
        "BCS threshold correction (~-7%, S62 THRESHOLD-62 / "
        "HIGGS-BCS-THRESHOLD-62, anomalous self-energy correction to "
        "g_3(M_KK)) is the documented mechanism closing 134 -> ~125 in the "
        "m_H chain. It has been applied to m_H ONLY — NOT to M0^{sector}. "
        "If the same screening were applied to M0, the inherited residual "
        "would shrink toward ~0 in step with m_H -> 125."
    )  # (local)

    value_payload = (
        f"r_KK=+{100*r_kk:.3f}pct_exact_67/1251;"
        f"r_tree=+{100*r_tree:.3f}pct_exact_89/1251;"
        f"anchor=s(h)sq-fiber-embedding-SHARED-with-m_H_branch(a);"
        f"inheritance=LINEAR-first-power;"
        f"band_conditional=[+{100*r_kk:.3f}pct,+{100*r_tree:.3f}pct];"
        f"band_if_independent=0;"
        f"BCS_minus7pct_applied_to_m_H_only_NOT_M0"
    )  # (local)

    return {
        "value": value_payload,
        "r_kk": r_kk, "r_tree": r_tree,
        "r_kk_exact": r_kk_exact, "r_tree_exact": r_tree_exact,
        "band_exact": band_exact,
        "dM0_low": dM0_low, "dM0_high": dM0_high,
        "dM0_independent": dM0_independent,
        "anchored": anchored,
        "anchor_evidence": anchor_evidence,
        "bcs_note": bcs_note,
        "ratio_kk": ratio_kk, "ratio_tree": ratio_tree,
    }


def save_npz(res: dict) -> None:
    np.savez(
        OUT_NPZ,
        # full float64 (Class 8.3 round-trip: npz carries full precision)
        r_kk=np.float64(res["r_kk"]),
        r_tree=np.float64(res["r_tree"]),
        dM0_over_M0_low=np.float64(res["dM0_low"]),
        dM0_over_M0_high=np.float64(res["dM0_high"]),
        dM0_over_M0_independent_branch=np.float64(res["dM0_independent"]),
        # exact rational pins (numerator/denominator integers)
        r_kk_exact_num=np.int64(res["r_kk_exact"].numerator),
        r_kk_exact_den=np.int64(res["r_kk_exact"].denominator),
        r_tree_exact_num=np.int64(res["r_tree_exact"].numerator),
        r_tree_exact_den=np.int64(res["r_tree_exact"].denominator),
        band_exact_num=np.int64(res["band_exact"].numerator),
        band_exact_den=np.int64(res["band_exact"].denominator),
        # mass inputs
        m_H_obs=np.float64(m_H_obs),
        m_H_FW_KK_threshold=np.float64(M_H_FW_KK_LOCAL),
        m_H_FW_tree=np.float64(M_H_FW_TREE_LOCAL),
        # anchor verdict (branch (a) = 1; branch (b) = 0)
        anchored_to_sh_sq_mode=np.int64(1 if res["anchored"] else 0),
        # documentation strings
        anchor_evidence=np.array(res["anchor_evidence"], dtype=object),
        bcs_note=np.array(res["bcs_note"], dtype=object),
        allow_pickle=True,
    )
    print(f"  npz written: {OUT_NPZ.name}")


def save_png(res: dict) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(7.2, 4.6))  # (local)
    labels = ["r_KK\n(131.8 vs 125.1)", "r_tree\n(134.0 vs 125.1)",
              "dM0/M0 if independently\nanchored (branch b)"]  # (local)
    vals = [100 * res["r_kk"], 100 * res["r_tree"], 0.0]  # (local)
    colors = ["#c0504d", "#8064a2", "#9bbb59"]  # (local)
    bars = ax.bar(labels, vals, color=colors, width=0.55)  # (local)
    ax.axhspan(100 * res["r_kk"], 100 * res["r_tree"], alpha=0.15,
               color="orange",
               label="inherited band [+5.356%, +7.114%] (branch a: |s(h)|^2-anchored)")
    for b, v in zip(bars, vals):  # (local)
        ax.text(b.get_x() + b.get_width() / 2, v + 0.12, f"+{v:.3f}%",
                ha="center", fontsize=10)
    ax.set_ylabel("residual vs m_H_obs = 125.1 GeV  [%]")
    ax.set_title("S100a-M0-MH-INHERITANCE — M0 absolute-normalization residual band\n"
                 "(report-only provenance trace; anchor identified: |s(h)|^2 fiber-embedding mode)")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_ylim(-0.5, 8.5)
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  png written: {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload (printed; agent calls emit_verdict MCP tool)
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str,
                          content_sha: str, companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    """Print the emit_verdict payload. Report-only [AUDIT] gate: NO schema-v2
    3-tuple (sign/magnitude/regime omitted entirely per plan + orchestrator)."""
    payload: dict = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()                 # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py" # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha} (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha} (script only)")
    print()

    res = compute()  # (local)

    print("=== residuals (exact rational | full float64 | published 4 s.f.) ===")
    print(f"  r_KK   = {res['r_kk_exact']} = {res['r_kk']:.12f} = +{100*res['r_kk']:.3f}%")
    print(f"  r_tree = {res['r_tree_exact']} = {res['r_tree']:.12f} = +{100*res['r_tree']:.3f}%")
    print(f"  band width = {res['band_exact']} = {float(res['band_exact']):.12f}")
    print(f"  anchored (branch a, |s(h)|^2): {res['anchored']}")
    print(f"  dM0/M0 inherited band: [+{100*res['dM0_low']:.3f}%, +{100*res['dM0_high']:.3f}%]")
    print(f"  dM0/M0 branch (b) independent-anchor reference: {res['dM0_independent']:.1f}")
    print()
    print("=== anchor evidence chain (substrate-first) ===")
    for i, ev in enumerate(res["anchor_evidence"], 1):  # (local)
        print(f"  [{i}] {ev}")
    print()
    print(f"=== BCS bookkeeping ===\n  {res['bcs_note']}")
    print()

    save_npz(res)
    try:
        save_png(res)
    except Exception as exc:  # png optional per plan
        print(f"  png skipped (optional): {exc}")

    verdict = "INFO"  # (local) SOLE pre-registered outcome — report-only trace
    print()
    print(emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX))
    print_verdict_payload(
        verdict, res["value"], audit_sha, content_sha,
        companion_note=("M0 anchor identified: |s(h)|^2 fiber-embedding mode "
                        "SHARED with m_H (branch a) => LINEAR inheritance; "
                        "honest-scope ledger: mass RATIOS clean, absolute "
                        "SCALE carries the m_H residual band; BCS -7% (S62) "
                        "applied to m_H only, NOT to M0"),
        extra_rows=[
            "# r_KK=67/1251 exact (+5.355715%) r_tree=89/1251 exact (+7.114309%) "
            "band=22/1251 exact; Sage QQ cross-checked; full float64 in npz "
            f"# {GATE_ID}",
            "# canonical write-order: m_H_FW_KK_threshold=131.8 (S28c/KK-THRESHOLD-64) "
            "+ m_H_FW_tree=134.0 (theorem A10/S62) promoted to canonical_constants "
            f"via update_constant AFTER this line, BEFORE inventory row # {GATE_ID}",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # INFO is the valid pre-registered outcome; exit 0 = script health


if __name__ == "__main__":
    sys.exit(main())
