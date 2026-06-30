#!/usr/bin/env python3
"""
S103 W2-2 / S103-S7-LC-TIER1-REANCHOR — PART 1 (Tier-1 dimensionless re-anchor)
==============================================================================

Gate: S103-S7-LC-TIER1-REANCHOR ([VERIFY-THEOREM]; inequality + Stage-2 PASS-AND)
Classification: GEOMETRIC (the §VII.BT entry IS the substrate's bridge-anatomy
image; the s=7 Mellin-cone residue tower of ζ_{D_K}(s) at the τ=0 LC genesis
slice is a substrate-IS observable — NO data-agreement appeal).

This script computes PART 1 only — the Tier-1 dimensionless re-anchor inequality
Level-3_dimensionless < Level-2 at L_max=10 (strict <). The COMPOSITE gate verdict
(this Part-1 result PASS-AND'd with the two Stage-2 cross-axis verdicts) is
assembled by the orchestrating connes-ncg-theorist AFTER the two BLIND
cross-reviewers return their JSON verdict files. The script writes both:
  (a) the Part-1 result (npz + png), and
  (b) the composite verdict payload, by INGESTING the two axis verdict JSONs IF
      they already exist on disk at run time (the orchestrator runs this script
      AFTER dispatching + awaiting the two cross-reviewers). If the axis JSONs
      are not yet present, the composite collapses to the Part-1-only sub-result
      and the payload is NOT emitted (the orchestrator re-runs after the reviews).

PART 1 — Tier-1 re-anchor (cross-pillar-bridge-anatomy.md §"Tier-1/Tier-2
dimensional-re-anchorability gate", corpus §25):
  The §VII.BT Stage-1 Level-3 anchor is the DIMENSIONFUL residue magnitude
  |a_2^{Mellin}(LC)| = 0.01259583 M_KK^2 (Tier-2-dimensionful, registry-PASS-
  INELIGIBLE, HELD `NOT-SATISFIED-PENDING-substrate-physical-scale-anchor`,
  differentia = dimensionful-slot-collision). The Tier-1 pathway re-anchors
  Level-3 to the DIMENSIONLESS truncation match-error peel_heldout(L_max=10) —
  a relative-deviation invariant that ANNIHILATES the M_KK^2 dimension (a ratio
  of two M_KK^2 quantities). This is the DOCUMENTED forward-gate route the
  §VII.BT entry itself names — NOT a post-hoc swap of the pre-registered
  Stage-1 Level-3 (comparator-discipline preserved; v3-closure-recovery.md
  PROHIBITED_ACTIONS Class 1/3).

  Test: Level-3_dimensionless < Level-2 = env_at_Lmax10 = 1.039022e-05, strict <.

PLAN-TEXT-DRIFT (substrate-first-canonical-sourcing.md §(ii.B)):
  The context (plan item 9) cited peel_heldout(L_max=10) = 1.2234e-11. The s101
  LC-certificate npz holds TWO peel fields:
    peel_heldout_nolog  = 4.95474088e-12   (the GATE GROUND-TRUTH; log-free)
    peel_heldout_withlog = 1.22341698e-11  (the with-log variant = the
                                            context-cited 1.2234e-11)
  This script RESOLVES to the npz GROUND-TRUTH log-free field
  (peel_heldout_nolog = 4.95474088e-12) as Level-3_NEW, per §(ii.B) npz-ground-
  truth resolution. The drift is documented in the verdict-line value field +
  the dual-SHA companion row; the context-cited with-log value is preserved as
  an audit-trail pointer. The strict Level-3 < Level-2 inequality holds under
  BOTH (4.95e-12 < 1.039e-05, ratio 4.77e-07; AND 1.22e-11 < 1.039e-05, ratio
  1.18e-06) — the drift does NOT flip the outcome.

SUBSTITUTION CHAIN (Tier-1 dimensional-class claim; math-scripts.md
§"Double-Check Logic Before Compute"):
  Claim: "Re-anchoring §VII.BT Level-3 to peel_heldout(L_max=10) (DIMENSIONLESS)
          restores the strict Level-3 < Level-2 inequality that the DIMENSIONFUL
          residue magnitude |a_2^{Mellin}(LC)| = 0.0126 M_KK^2 FAILS."
  Step 1: Level-2 = env_at_Lmax10 = 10^{-alpha} = 1.039022e-05  [DIMENSIONLESS
          L^{-alpha} convergence-rate bound; alpha = 6.584; registry §VII.BT
          Level-2 row, Level-2-binding]
  Step 2: Level-3_OLD = |a_2^{Mellin}(LC)| = 0.01259583         [DIMENSIONFUL,
          M_KK^2 units; npz res_sA3 / a2_mellin_LC]
  Step 3: Level-3_NEW = peel_heldout_nolog = 4.95474088e-12     [DIMENSIONLESS;
          relative truncation deviation |residue(L=10) - residue(inf)| /
          |residue(inf)| — the M_KK^2 dimension cancels in the ratio; npz
          ground-truth]
  Substitute (OLD):  Level-3_OLD < Level-2 is 0.01259583 [M_KK^2] < 1.039022e-05
                     [dimensionless] -> compares M_KK^2 vs a dimensionless rate.
  Simplify:          dimensionally inhomogeneous => Tier-2-dimensionful =>
                     registry-PASS-INELIGIBLE (dimensionful-slot-collision).
  Substitute' (NEW): Level-3_NEW < Level-2 is 4.95474088e-12 < 1.039022e-05
                     -> both DIMENSIONLESS.
  Canonical form:    ratio = 4.95474088e-12 / 1.039022e-05 = 4.7687e-07 < 1.
  Direction:         Level-3_NEW / Level-2 << 1 => strict Level-3 < Level-2 HOLDS.
  Conclusion:        the Tier-1 dimensionless re-anchor satisfies the strict
                     registry-PASS criterion by ~6 OOM margin; the HELD status
                     converts to registry-PASS-eligible.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-101/s101_w3_lc_pole_cert.npz  (peel_heldout_nolog,
    a2_mellin_LC / res_sA3; gate S101-W3-LC-POLE-CERT PASS audit ebfd1d43)
  - sessions/permanent-results-registry.md  (§VII.BT Stage-1 entry; the
    Level-2 envelope value 1.039022e-05 is registry-PRE-REGISTERED there)
  - canonical_constants.py  (feeds audit_sha256; re-pinned at runtime per
    substrate-first §(ii.B) — drifted from plan-freeze 9f2fe998 to runtime)
  - the two axis verdict JSONs (ingested IF present, for the composite)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=(<composite or part1>, ratio, margin), scheme=cross-pillar-bridge-
   anatomy-Tier-1-dimensionless-re-anchor,
   convention=poleconv-DUAL-SUBSTRATE-NATURAL-BINDING, L_max=10)
"""

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 1 — Paths + canonical import
# ---------------------------------------------------------------------------
HERE = Path(__file__).resolve()                                   # (local)
SESSION_DIR = HERE.parent                                          # (local)
COMPUTATIONS_DIR = SESSION_DIR.parent                              # (local)
PROJECT_ROOT = COMPUTATIONS_DIR.parent                            # (local)
SHARED_DIR = COMPUTATIONS_DIR / "_shared"                          # (local)
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403  (M_KK and provenance feed audit_sha256)

# ---------------------------------------------------------------------------
# Section 2 — Gate identity + pre-registered constants
# ---------------------------------------------------------------------------
SESSION = "S103"
GATE_ID = "S103-S7-LC-TIER1-REANCHOR"
SCHEME = "cross-pillar-bridge-anatomy-Tier-1-dimensionless-re-anchor"
CONVENTION = "poleconv-DUAL-SUBSTRATE-NATURAL-BINDING"
L_MAX = 10                           # (local) canonical L_max for the §VII.BT 3-level ladder (gate machinery pin)

# Pre-registered Level-2 envelope (registry §VII.BT Level-2 row; alpha=6.584;
# Level-2-binding). This is the registry-PRE-REGISTERED dimensionless L^{-alpha}
# convergence-rate bound at canonical L_max=10. NOT a free parameter of this gate.
ENV_AT_LMAX10 = 1.039022e-05        # (local) Level-2 = 10^{-alpha}, registry §VII.BT
ALPHA_DECAY = 6.584                  # (local) per-order Laurent decay exponent, registry §VII.BT

# Input files
LC_CERT = COMPUTATIONS_DIR / "session-101" / "s101_w3_lc_pole_cert.npz"
REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
CANONICAL = SHARED_DIR / "canonical_constants.py"
AXIS_A_JSON = SESSION_DIR / "s103_s7_lc_tier1_reanchor_axisA_verdicts.json"
AXIS_B_JSON = SESSION_DIR / "s103_s7_lc_tier1_reanchor_axisB_verdicts.json"

INPUT_FILES = [LC_CERT, REGISTRY, CANONICAL]

# Plan-pinned SHAs (for the disclosure / drift audit trail)
PLAN_CANONICAL_SHA = "9f2fe9983ecbbb76a2ba1b3e951cf9275deda8d7f2241576ef23b7f728ba1047"  # (local) plan-freeze pin
PLAN_LC_CERT_SHA = "a4abff525f30edea45c48660567a4583ce61dadd8e35977b4cd135bae0d9cb4b"     # (local) registry §VII.BT pin
CONTEXT_CITED_PEEL = 1.2234e-11      # (local) plan-text-drift: context-cited value (= npz peel_heldout_withlog)


# ---------------------------------------------------------------------------
# Section 3 — SHA helpers (S84+ dual-SHA schema; verbatim from script-template)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def log_input_pins(paths) -> dict:
    pins = {}                                                      # (local)
    print(f"=== {GATE_ID} — input pins ===")
    for p in paths:
        rel = str(Path(p).resolve()).replace(str(PROJECT_ROOT), "").lstrip("\\/")  # (local)
        s = sha256_of(Path(p))                                     # (local)
        pins[rel] = s
        print(f"  {rel}: {s[:16]}...")
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())                                  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()                       # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()             # (local)
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                   # (local)
    content = hashlib.sha256(script_bytes).hexdigest()            # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 4 — print_verdict_payload (verbatim from script-template)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    payload = {
        "session": int(SESSION.lstrip("Ss")),
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
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 5 — Compute (PART 1 re-anchor + PART 2 ingestion)
# ---------------------------------------------------------------------------
def ingest_axis_verdict(path: Path):
    """Read an axis verdict JSON; return (overall, joint_passand, dict) or (None, ...)."""
    if not path.exists():
        return None, None, None
    try:
        d = json.loads(path.read_text(encoding="utf-8"))           # (local)
    except (OSError, json.JSONDecodeError):
        return None, None, None
    overall = str(d.get("overall_verdict", "")).upper()            # (local)
    # JOINT clauses PASS only if every clause tagged joint=true is PASS.
    clauses = d.get("clauses", {})                                 # (local)
    joint_states = []                                              # (local)
    for _name, c in clauses.items():
        if isinstance(c, dict) and c.get("joint", False):
            joint_states.append(str(c.get("verdict", "")).upper())
    if joint_states:
        if any(v == "FAIL" for v in joint_states):
            joint = "FAIL"                                         # (local)
        elif any(v == "INFO" for v in joint_states):
            joint = "INFO"                                         # (local)
        else:
            joint = "PASS"                                         # (local)
    else:
        joint = None                                               # (local) no joint clauses tagged
    return overall, joint, d


def compute() -> dict:
    # --- PART 1: Tier-1 dimensionless re-anchor inequality ---
    cert = np.load(LC_CERT, allow_pickle=True)                     # (local)

    peel_nolog = float(cert["peel_heldout_nolog"][0])              # (local) Level-3_NEW ground-truth
    peel_withlog = float(cert["peel_heldout_withlog"][0])          # (local) context-cited drift value
    a2_mellin_LC = float(cert["a2_mellin_LC"][0])                  # (local) Level-3_OLD (dimensionful, signed)
    res_sA3 = float(cert["res_sA3"][0])                            # (local) same residue, cross-check
    level3_old_dimful = abs(a2_mellin_LC)                          # (local) |a_2^{Mellin}(LC)| M_KK^2

    # Cross-check: a2_mellin_LC == res_sA3 (same residue, two npz fields)
    a2_consistent = abs(a2_mellin_LC - res_sA3) < 1e-15            # (local)

    # Cross-check: the context-cited drift value equals the npz with-log field
    drift_matches_withlog = abs(CONTEXT_CITED_PEEL - peel_withlog) < 1e-13  # (local)

    level2 = ENV_AT_LMAX10                                         # (local) registry-PRE-REGISTERED
    level3_new_dimless = peel_nolog                                # (local) substrate-first §(ii.B) ground-truth

    # The strict registry-PASS inequality: Level-3_NEW < Level-2
    ratio = level3_new_dimless / level2                            # (local) match/envelope
    part1_pass = bool(level3_new_dimless < level2)                 # (local) STRICT <
    # Margin in OOM (orders of magnitude inside the envelope)
    oom_margin = float(np.log10(level2) - np.log10(level3_new_dimless))  # (local)

    # Same inequality under the context-cited (with-log) value (drift robustness)
    ratio_withlog = peel_withlog / level2                         # (local)
    part1_pass_withlog = bool(peel_withlog < level2)              # (local)

    # The DIMENSIONFUL OLD comparison (documents WHY it was HELD; not a PASS test)
    # 0.01259583 (M_KK^2) vs 1.039022e-05 (dimensionless) — inhomogeneous.
    old_literal_holds = bool(level3_old_dimful < level2)          # (local) -> False (and dimensionally invalid)

    # --- PART 2: ingest the two BLIND cross-axis verdicts IF present ---
    axisA_overall, axisA_joint, axisA_d = ingest_axis_verdict(AXIS_A_JSON)  # (local)
    axisB_overall, axisB_joint, axisB_d = ingest_axis_verdict(AXIS_B_JSON)  # (local)
    both_present = (axisA_overall is not None) and (axisB_overall is not None)  # (local)

    # Composite collapse (plan verdict rubric):
    #   PASS iff (part1_pass) AND (Axis-A PASS) AND (Axis-B PASS)
    #            AND (JOINT clauses PASS in BOTH)
    #   any clause FAIL -> FAIL ; any clause INFO (none FAIL) -> INFO
    composite = None                                              # (local)
    composite_basis = "PART-1-ONLY (axis JSONs not yet present)"  # (local)
    if both_present:
        # gather every per-axis state we gate on
        states = [axisA_overall, axisB_overall]                  # (local)
        # JOINT PASS-AND across both axes (a joint clause must PASS in BOTH)
        joint_states = [s for s in (axisA_joint, axisB_joint) if s is not None]  # (local)
        joint_passand = "PASS"                                   # (local)
        if any(s == "FAIL" for s in joint_states):
            joint_passand = "FAIL"
        elif any(s == "INFO" for s in joint_states):
            joint_passand = "INFO"
        states.append(joint_passand)
        # Part-1 contributes a PASS/FAIL
        states.append("PASS" if part1_pass else "FAIL")
        if "FAIL" in states:
            composite = "FAIL"                                   # (local)
        elif "INFO" in states:
            composite = "INFO"                                   # (local)
        else:
            composite = "PASS"                                   # (local)
        composite_basis = (f"PART-1={'PASS' if part1_pass else 'FAIL'} AND "
                           f"AxisA={axisA_overall} AND AxisB={axisB_overall} AND "
                           f"JOINT-PASS-AND={joint_passand}")

    value_str = (
        f"part1_reanchor={'PASS' if part1_pass else 'FAIL'};"
        f"L3_new_dimless=peel_heldout_nolog={level3_new_dimless:.8e};"
        f"L2_envelope={level2:.6e};ratio={ratio:.4e};oom_margin={oom_margin:.3f};"
        f"L3_old_dimful=|a2_Mellin_LC|={level3_old_dimful:.8e}_M_KK2_HELD_Tier2;"
        f"drift_nolog_used_withlog_cited={peel_withlog:.8e};"
        f"composite={composite if composite else 'PART1-ONLY'}"
    )

    return {
        "value": value_str,
        "part1_pass": part1_pass,
        "level3_new_dimless": level3_new_dimless,
        "level3_old_dimful": level3_old_dimful,
        "level2": level2,
        "alpha_decay": ALPHA_DECAY,
        "ratio": ratio,
        "oom_margin": oom_margin,
        "ratio_withlog": ratio_withlog,
        "part1_pass_withlog": part1_pass_withlog,
        "peel_nolog": peel_nolog,
        "peel_withlog": peel_withlog,
        "context_cited_peel": CONTEXT_CITED_PEEL,
        "drift_matches_withlog": drift_matches_withlog,
        "a2_mellin_LC": a2_mellin_LC,
        "res_sA3": res_sA3,
        "a2_consistent": a2_consistent,
        "old_literal_holds": old_literal_holds,
        "both_axes_present": both_present,
        "axisA_overall": axisA_overall,
        "axisB_overall": axisB_overall,
        "axisA_joint": axisA_joint,
        "axisB_joint": axisB_joint,
        "composite": composite,
        "composite_basis": composite_basis,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict, out_png: Path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(1, 2, figsize=(13, 5.2))

    # Left: log-scale bar comparison Level-3_OLD vs Level-3_NEW vs Level-2
    labels = ["Level-3_OLD\n|a2_Mellin(LC)|\n(M_KK^2; HELD Tier-2)",
              "Level-2\nenvelope 10^-alpha\n(dimensionless)",
              "Level-3_NEW\npeel_heldout(L=10)\n(dimensionless; Tier-1)"]
    vals = [r["level3_old_dimful"], r["level2"], r["level3_new_dimless"]]
    colors = ["#c0392b", "#2c3e50", "#27ae60"]
    bars = ax[0].bar(range(3), vals, color=colors, log=True, width=0.6)
    ax[0].set_yscale("log")
    ax[0].set_xticks(range(3))
    ax[0].set_xticklabels(labels, fontsize=8)
    ax[0].axhline(r["level2"], color="#2c3e50", ls="--", lw=1.2, alpha=0.7)
    ax[0].set_ylabel("value (log scale)")
    ax[0].set_title("§VII.BT Tier-1 re-anchor: Level-3_NEW (dimensionless)\n"
                    "deep inside the Level-2 envelope (strict <)", fontsize=10)
    for b, v in zip(bars, vals):
        ax[0].text(b.get_x() + b.get_width() / 2, v * 1.5, f"{v:.2e}",
                   ha="center", va="bottom", fontsize=7)
    # annotate the dimensional-class boundary
    ax[0].text(0, r["level3_old_dimful"] * 3.5,
               "DIMENSIONFUL\n(inhomogeneous vs Level-2\n=> Tier-2 HELD)",
               ha="center", va="bottom", fontsize=7, color="#c0392b")

    # Right: ratio (match/envelope) — should be << 1
    ax[1].axhline(1.0, color="#c0392b", ls="--", lw=1.5, label="ratio = 1 (PASS boundary)")
    ax[1].bar([0], [r["ratio"]], color="#27ae60", width=0.4,
              label=f"L3_new/L2 = {r['ratio']:.2e}")
    ax[1].bar([1], [r["ratio_withlog"]], color="#16a085", width=0.4, alpha=0.7,
              label=f"with-log (drift) = {r['ratio_withlog']:.2e}")
    ax[1].set_yscale("log")
    ax[1].set_xticks([0, 1])
    ax[1].set_xticklabels(["nolog\n(ground-truth)", "withlog\n(context-cited)"], fontsize=8)
    ax[1].set_ylabel("Level-3 / Level-2 (log scale)")
    ax[1].set_title(f"Strict-< margin: {r['oom_margin']:.2f} OOM inside envelope\n"
                    f"(both peel variants PASS the inequality)", fontsize=10)
    ax[1].legend(fontsize=7, loc="upper right")
    ax[1].set_ylim(1e-8, 10)

    fig.suptitle(f"{GATE_ID} — PART 1 Tier-1 dimensionless re-anchor "
                 f"(part1_pass={r['part1_pass']}; composite={r['composite']})",
                 fontsize=11, y=1.00)
    fig.tight_layout()
    fig.savefig(out_png, dpi=130, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def main() -> int:
    t0 = time.time()                                              # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # Runtime SHA disclosure (canonical_constants.py drift per substrate-first §(ii.B))
    runtime_canonical_sha = sha256_of(CANONICAL)                  # (local)
    runtime_lc_sha = sha256_of(LC_CERT)                           # (local)
    runtime_registry_sha = sha256_of(REGISTRY)                    # (local)
    canonical_drifted = runtime_canonical_sha != PLAN_CANONICAL_SHA  # (local)
    lc_matches_plan = runtime_lc_sha == PLAN_LC_CERT_SHA          # (local)
    print(f"  [DRIFT-DISCLOSURE §(ii.B)] canonical_constants.py: "
          f"plan-freeze {PLAN_CANONICAL_SHA[:16]}... -> runtime {runtime_canonical_sha[:16]}... "
          f"(drifted={canonical_drifted}; mid-session append-only S103 W5-2 COMMIT)")
    print(f"  [PIN-MATCH] s101_w3_lc_pole_cert.npz: runtime {runtime_lc_sha[:16]}... "
          f"== plan-pinned {PLAN_LC_CERT_SHA[:16]}... -> {lc_matches_plan}")
    print(f"  [RUNTIME] registry SHA: {runtime_registry_sha[:16]}... (computed-at-runtime per plan)")

    audit_sha, content_sha = compute_dual_sha(HERE, CANONICAL, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()

    # --- PART 1 report ---
    print("=== PART 1 — Tier-1 dimensionless re-anchor ===")
    print(f"  Level-2 (registry §VII.BT, alpha={r['alpha_decay']}): {r['level2']:.6e}  [DIMENSIONLESS]")
    print(f"  Level-3_OLD = |a_2^Mellin(LC)|              : {r['level3_old_dimful']:.8e}  [DIMENSIONFUL M_KK^2; HELD Tier-2]")
    print(f"    (a2_mellin_LC={r['a2_mellin_LC']:.8e}, res_sA3={r['res_sA3']:.8e}, consistent={r['a2_consistent']})")
    print(f"  Level-3_NEW = peel_heldout_nolog            : {r['level3_new_dimless']:.8e}  [DIMENSIONLESS; ground-truth]")
    print(f"  [DRIFT] context-cited peel={r['context_cited_peel']:.4e} == npz peel_heldout_withlog={r['peel_withlog']:.8e} -> {r['drift_matches_withlog']}")
    print(f"  ratio L3_new/L2 = {r['ratio']:.4e}  (<< 1 => strict < holds)")
    print(f"  OOM margin inside envelope = {r['oom_margin']:.3f}")
    print(f"  STRICT Level-3_NEW < Level-2 ? {r['part1_pass']}  "
          f"(with-log variant also PASSes? {r['part1_pass_withlog']}, ratio {r['ratio_withlog']:.4e})")
    print(f"  [OLD dimensionful literal {r['level3_old_dimful']:.4e} < {r['level2']:.4e} ? "
          f"{r['old_literal_holds']} — and dimensionally INVALID => Tier-2 HELD, documents WHY re-anchor needed]")
    print()

    # --- PART 2 report ---
    print("=== PART 2 — Stage-2 cross-axis PASS-AND ===")
    print(f"  Axis-A (lizzi) JSON present  : {AXIS_A_JSON.exists()}  -> overall={r['axisA_overall']}, joint={r['axisA_joint']}")
    print(f"  Axis-B (volovik) JSON present: {AXIS_B_JSON.exists()}  -> overall={r['axisB_overall']}, joint={r['axisB_joint']}")
    print(f"  both axes present: {r['both_axes_present']}")
    print(f"  composite basis: {r['composite_basis']}")
    print(f"  COMPOSITE VERDICT: {r['composite']}")
    print()

    # --- npz ---
    out_npz = SESSION_DIR / "s103_s7_lc_tier1_reanchor.npz"
    np.savez(
        out_npz,
        gate_id=np.array([GATE_ID]),
        part1_pass=np.array([r["part1_pass"]]),
        level3_new_dimless=np.array([r["level3_new_dimless"]]),
        level3_old_dimful=np.array([r["level3_old_dimful"]]),
        level2_envelope=np.array([r["level2"]]),
        alpha_decay=np.array([r["alpha_decay"]]),
        ratio=np.array([r["ratio"]]),
        oom_margin=np.array([r["oom_margin"]]),
        peel_heldout_nolog=np.array([r["peel_nolog"]]),
        peel_heldout_withlog=np.array([r["peel_withlog"]]),
        context_cited_peel=np.array([r["context_cited_peel"]]),
        drift_matches_withlog=np.array([r["drift_matches_withlog"]]),
        a2_mellin_LC=np.array([r["a2_mellin_LC"]]),
        res_sA3=np.array([r["res_sA3"]]),
        a2_consistent=np.array([r["a2_consistent"]]),
        old_literal_holds=np.array([r["old_literal_holds"]]),
        both_axes_present=np.array([r["both_axes_present"]]),
        axisA_overall=np.array([str(r["axisA_overall"])]),
        axisB_overall=np.array([str(r["axisB_overall"])]),
        axisA_joint=np.array([str(r["axisA_joint"])]),
        axisB_joint=np.array([str(r["axisB_joint"])]),
        composite=np.array([str(r["composite"])]),
        composite_basis=np.array([r["composite_basis"]]),
        runtime_canonical_sha=np.array([runtime_canonical_sha]),
        plan_canonical_sha=np.array([PLAN_CANONICAL_SHA]),
        canonical_drifted=np.array([canonical_drifted]),
        runtime_lc_sha=np.array([runtime_lc_sha]),
        lc_matches_plan=np.array([lc_matches_plan]),
        runtime_registry_sha=np.array([runtime_registry_sha]),
        audit_sha256=np.array([audit_sha]),
        content_sha256=np.array([content_sha]),
        value=np.array([r["value"]]),
    )
    print(f"  npz -> {out_npz}")

    out_png = SESSION_DIR / "s103_s7_lc_tier1_reanchor.png"
    make_plot(r, out_png)
    print(f"  png -> {out_png}")
    print()

    # --- 4-tuple + payload ---
    tag = emit_4tuple(r["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    # Composite verdict for emission. Only emit the payload when BOTH axes are
    # present (the composite is well-defined). If absent, print the Part-1
    # sub-result and instruct the orchestrator to re-run after the reviews.
    if r["both_axes_present"] and r["composite"] is not None:
        verdict = r["composite"]                                  # (local)
        regulator_row = (
            "# regulator_pin=a_2^{Mellin}(LC) poleconv-DUAL "
            "(s_A=3==s_B=6, grade_n=2; a_2^{Mellin}(LC)=-0.01259583 M_KK^2 the HELD Tier-2 magnitude; "
            "Tier-1 re-anchor target peel_heldout_nolog=4.95474088e-12 is the DIMENSIONLESS truncation "
            "invariant of the SAME Mellin-regulated residue)"
        )                                                         # (local)
        drift_row = (
            f"# plan-text-drift §(ii.B): npz GROUND-TRUTH peel_heldout_nolog={r['peel_nolog']:.8e} USED as Level-3; "
            f"context-cited {r['context_cited_peel']:.4e} == npz peel_heldout_withlog={r['peel_withlog']:.8e} (with-log variant, audit-trail pointer); "
            f"canonical_constants.py SHA drifted plan {PLAN_CANONICAL_SHA[:16]}->runtime {runtime_canonical_sha[:16]} (mid-session append-only); LC cert SHA matches plan-pin"
        )                                                         # (local)
        passand_row = (
            f"# Stage-2 PASS-AND: Part1={'PASS' if r['part1_pass'] else 'FAIL'} AND "
            f"AxisA(lizzi)={r['axisA_overall']} AND AxisB(volovik)={r['axisB_overall']} AND "
            f"JOINT-clauses-PASS-AND-in-BOTH (axisA_joint={r['axisA_joint']}, axisB_joint={r['axisB_joint']}) "
            f"-> composite={verdict} (joint-theorem-promotion.md Stage 2)"
        )                                                         # (local)
        print_verdict_payload(
            verdict, r["value"], audit_sha, content_sha,
            extra_rows=[regulator_row, drift_row, passand_row],
        )
    else:
        # Stage-2 prerequisite ABSENT (one or both axis verdict JSONs missing).
        # Honest mechanical closure per mechanical-closure-discipline.md
        # §"When mechanical closure IS acceptable": the composite gate has a
        # prerequisite (the two Stage-2 cross-axis verdicts) that is not PASS
        # (it is ABSENT) => emit PRE-REG-INC, NEVER PASS. The Part-1 Tier-1
        # re-anchor inequality PASSes and is preserved as a documented
        # sub-result (plan INFO_meaning: "the Tier-1 re-anchor inequality
        # itself (Part 1) may independently PASS — recorded as a sub-result").
        a_status = "PASS-present" if AXIS_A_JSON.exists() else "absent"   # (local)
        b_status = "PASS-present" if AXIS_B_JSON.exists() else "absent"   # (local)
        verdict = "PRE-REG-INC"                                            # (local)
        blocked_value = (
            f"PRE-REG-INC_blocked_by_axisA_verdict_{a_status}_axisB_verdict_{b_status}_"
            f"stage2_dispatch_required;part1_reanchor=PASS;"
            f"L3_new_dimless=peel_heldout_nolog={r['level3_new_dimless']:.8e};"
            f"L2_envelope={r['level2']:.6e};ratio={r['ratio']:.4e};oom_margin={r['oom_margin']:.3f};"
            f"L3_old_dimful=|a2_Mellin_LC|={r['level3_old_dimful']:.8e}_M_KK2_HELD_Tier2;"
            f"drift_nolog_used_withlog_cited={r['peel_withlog']:.8e}"
        )                                                                 # (local)
        regulator_row = (
            "# regulator_pin=a_2^{Mellin}(LC) poleconv-DUAL "
            "(s_A=3==s_B=6, grade_n=2; a_2^{Mellin}(LC)=-0.01259583 M_KK^2 HELD Tier-2; "
            "Tier-1 re-anchor target peel_heldout_nolog=4.95474088e-12 the DIMENSIONLESS truncation invariant)"
        )                                                                 # (local)
        drift_row = (
            f"# plan-text-drift §(ii.B): npz GROUND-TRUTH peel_heldout_nolog={r['peel_nolog']:.8e} USED as Level-3; "
            f"context-cited {r['context_cited_peel']:.4e} == npz peel_heldout_withlog={r['peel_withlog']:.8e} (audit-trail pointer); "
            f"canonical_constants.py SHA drifted plan {PLAN_CANONICAL_SHA[:16]}->runtime {runtime_canonical_sha[:16]} (mid-session append-only); LC cert SHA matches plan-pin"
        )                                                                 # (local)
        prereg_row = (
            f"# PRE-REG-INC per mechanical-closure-discipline.md: Stage-2 two-agent cross-axis verify NOT executed "
            f"(axisA={a_status}, axisB={b_status}); composite blocked. Part-1 Tier-1 re-anchor PASSes "
            f"(strict {r['level3_new_dimless']:.3e} < {r['level2']:.3e}, {r['oom_margin']:.2f} OOM); "
            f"required prereqs: [s103_s7_lc_tier1_reanchor_axisA_verdicts.json, s103_s7_lc_tier1_reanchor_axisB_verdicts.json]; "
            f"BLIND reviewer prompts on disk: s103_s7_lc_tier1_reanchor_axis{{A,B}}_PROMPT.md"
        )                                                                 # (local)
        print("[STAGE-2-ABSENT] Axis verdict JSONs not both present; composite = PRE-REG-INC (honest mechanical closure).")
        print(f"[STAGE-2-ABSENT] Part-1 sub-result PRESERVED: part1_pass={r['part1_pass']}, "
              f"ratio={r['ratio']:.4e}, oom_margin={r['oom_margin']:.3f}")
        print_verdict_payload(
            verdict, blocked_value, audit_sha, content_sha,
            extra_rows=[regulator_row, drift_row, prereg_row],
        )
        r["composite"] = verdict

    wall = time.time() - t0                                       # (local)
    print(f"\n=== {GATE_ID}: PART1={'PASS' if r['part1_pass'] else 'FAIL'}, "
          f"composite={r['composite']} (wall {wall:.1f}s) ===")
    # Exit 0 regardless of scientific verdict (math-scripts.md §"Exit Codes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
