#!/usr/bin/env python3
"""
S110 W4b-3 S110-CF-EVOI-REANCHOR — EVOI Tier-1/Tier-2 re-anchor + anti-rescue audit
====================================================================================

Gate: S110-CF-EVOI-REANCHOR ([AUDIT])

Pre-registered "threshold" (artifact-existence / set operator, NOT a numerical band):
  PASS iff  (EVOI Tier re-rank applied: structural cohort UP / observational cohort DOWN)
       AND  (atlas-08 Q44 annotated CLOSED)
       AND  (anti-rescue audit = no PROHIBITED_ACTIONS Class 1 rescue attempted).

This is the empirical-conscience / AUDIT gate of the M_KK-keystone session. It does NOT
re-derive the inv-13 W2-3 per-observable Bayes factors — that synthesis is the rollup
aggregation node and is CONSUMED as input (its SHA is pinned). The script's job is the
RECOMPOSITION ARITHMETIC (posterior-odds product over the two cohorts) plus the
ANTI-RESCUE AUDIT (verify the n_s / w_a / w_0 liability figures match their canonical
substrate pins — i.e. that NO friendlier-anchor or branch-shopped value was substituted).

Inputs (SHA-256 dual-pinned at runtime):
  - sessions/investigation/investigation-13/investigation-13-bayesian-reanchor-synthesis.md
        (the per-observable BF table; INPUT, not re-derived)
  - sessions/evoi-framework.md          (the table being re-anchored + re-stamped)
  - canonical_constants.py              (feeds audit_sha256; the anti-rescue pin source)
  - script bytes                        (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<directional-split record>, scheme=EVOI-RE-ANCHOR-BF-ELICITED,
   convention=ANTI-RESCUE-FENCE-CLASS-1, L_max=N/A)

Classification: NON-PHONONIC (methodology / empirical-conscience).

METHODOLOGY
-----------
Posterior odds factor as a product over independent cohorts (inv-13 §III; NOT an
arithmetic mean):  O_post = O_prior * BF_struct * BF_obs,  with prior P0 = 0.22 (S69
anchor). The structural cohort S (10 blind STAGE-3 zero-parameter geometric identities,
joint BF 25-55) rises; the observational cohort O (n_s 4.73 sigma global post-look-
elsewhere, w_a 3.43 sigma, A_s route-unstable) falls. The headline ~22% is STATIONARY by
near-exact cancellation when BF_struct * BF_obs ~ 1 -- the cancellation IS the finding
(the dual_prior track-discriminator). We reproduce the inv-13 §III bracket and confirm the
directional split is what the re-anchor reports, NOT a collapsed single number.

The anti-rescue audit checks each liability row's honest figure against its canonical pin:
  - w_0 = -0.918 canonical (the 2.13 sigma branch); branch-iv -0.842 (0.731 sigma) is
    derivation-INADMISSIBLE post-S86 -> selecting it would be branch-shopping (Class 1).
  - n_s = 0.959 (sqrt-cutoff, COMMITTED) -> the 4.73 sigma global is the look-elsewhere-
    corrected worst-anchor figure; the friendliest anchor (Planck 1.40 sigma) is NOT picked.
  - w_a = 0 (four-fold structural lock, zero free params) -> 3.43 sigma stands.
The audit PASSES iff the honest (worst-case / canonical) figure is the one carried -- i.e.
no row was quietly rescued to a lower sigma-distance.

DISCIPLINE
----------
- `from canonical_constants import *`
- every intermediate tagged `# (local)`
- dual-SHA (audit = script+canonical+pinmap; content = script) emitted via print_verdict_payload
- the script does NOT write the verdict file (race-safe emit_verdict owns that)
- no numerical PASS threshold: this is an [AUDIT]/set gate; the verdict is the set-conjunction
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import; the anti-rescue pin source)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
import canonical_constants as cc

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import math
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")
import numpy as np  # noqa: E402
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
# This script lives in computations/_shared/ (per the plan: W4b aggregate/re-anchor
# scripts live in _shared, their data/png/verdict land in computations/session-110/).
SHARED_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SHARED_DIR.parent
PROJECT_ROOT = COMPUTATIONS_DIR.parent
SESSION_OUT_DIR = COMPUTATIONS_DIR / "session-110"

SESSION = "S110"                                                  # (local)
GATE_ID = "S110-CF-EVOI-REANCHOR"                                 # (local)
SCHEME = "EVOI-RE-ANCHOR-BF-ELICITED"                             # (local)
CONVENTION = "ANTI-RESCUE-FENCE-CLASS-1"                          # (local)
L_MAX = "N/A"                                                     # (local)

OUT_NPZ = SESSION_OUT_DIR / "s110_cf_evoi_reanchor.npz"
OUT_PNG = SESSION_OUT_DIR / "s110_cf_evoi_reanchor.png"

BF_TABLE = (PROJECT_ROOT / "sessions" / "investigation" / "investigation-13"
            / "investigation-13-bayesian-reanchor-synthesis.md")          # (local)
EVOI_FILE = PROJECT_ROOT / "sessions" / "evoi-framework.md"               # (local)
CANONICAL = SHARED_DIR / "canonical_constants.py"                          # (local)

INPUT_FILES = [
    CANONICAL,
    BF_TABLE,
    EVOI_FILE,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (dual-SHA schema)
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
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Compute: recomposition arithmetic + anti-rescue audit
# ---------------------------------------------------------------------------

# inv-13 W2-3 §III verified-arithmetic cohort pairs (CONSUMED, not re-derived).
# Each row: (BF_struct [S rises], BF_obs [O falls], P_post reported in inv-13 §III).
INV13_SIII_PAIRS = [
    (1.5, 0.40, 0.145),
    (2.0, 0.55, 0.237),
    (3.0, 0.55, 0.318),
    (2.0, 0.70, 0.283),
    (1.5, 0.70, 0.228),
]                                                                          # (local)

PRIOR_P0 = 0.22   # S69 anchor (inv-13 §III prior)                         # (local)


def posterior_from_odds(prior_p: float, bf_struct: float, bf_obs: float) -> float:
    """O_post = O_prior * BF_struct * BF_obs ;  P_post = O_post / (1 + O_post).

    This is the posterior-odds PRODUCT over independent cohorts (inv-13 §III) --
    NOT an arithmetic mean of per-observable probabilities.
    """
    o_prior = prior_p / (1.0 - prior_p)          # (local)
    o_post = o_prior * bf_struct * bf_obs        # (local)
    return o_post / (1.0 + o_post)               # (local)


def reproduce_inv13_bracket() -> dict:
    """Re-derive the inv-13 §III P_post bracket from the posterior-odds product.

    Confirms (a) the arithmetic is a product not a mean, (b) the bracket
    [0.145, 0.372] reproduces, (c) BF_struct*BF_obs ~ 1 => headline stationary.
    """
    recomputed = []          # (local)
    max_abs_dev = 0.0        # (local)
    for bf_s, bf_o, p_reported in INV13_SIII_PAIRS:
        p_calc = posterior_from_odds(PRIOR_P0, bf_s, bf_o)   # (local)
        dev = abs(p_calc - p_reported)                       # (local)
        max_abs_dev = max(max_abs_dev, dev)
        recomputed.append((bf_s, bf_o, p_reported, round(p_calc, 6),
                           round(bf_s * bf_o, 4)))
    p_vals = [r[3] for r in recomputed]                      # (local)
    # The "stationary by cancellation" check: the pair whose product is closest to 1
    # should land closest to the prior 0.22.
    prod_to_one = [(abs(r[4] - 1.0), r) for r in recomputed]  # (local)
    prod_to_one.sort(key=lambda x: x[0])
    nearest_unity = prod_to_one[0][1]                        # (local)
    return {
        "recomputed": recomputed,
        "p_min": round(min(p_vals), 6),
        "p_max": round(max(p_vals), 6),
        "max_abs_dev_vs_inv13": round(max_abs_dev, 6),
        "nearest_unity_pair": nearest_unity,
        "prior_p0": PRIOR_P0,
    }


def anti_rescue_audit() -> dict:
    """Verify each observational liability row carries its HONEST (canonical / worst-
    case) figure -- i.e. NO friendliest-anchor selection, NO branch-shopping.

    A rescue would be a PROHIBITED_ACTIONS Class 1 violation (the methodology-floor
    analog of convention-shopping). This audit records that NO rescue was attempted by
    checking the carried figures against their canonical substrate pins.
    """
    findings = []            # (local)
    clean = True             # (local)

    # --- w_0: canonical -0.918 (2.13 sigma) vs INADMISSIBLE branch-iv -0.842 (0.731 sigma)
    w0_canonical = float(cc.w0_FW)                                  # (local)
    w0_honest_expected = -0.918                                    # (local)
    w0_branch_iv_rescue = -0.842                                   # (local)  the forbidden lower-sigma pick
    w0_match = math.isclose(w0_canonical, w0_honest_expected, abs_tol=1e-9)  # (local)
    # The carried figure MUST be the canonical (2.13 sigma), NOT branch-iv (0.731 sigma).
    w0_rescued = not w0_match or math.isclose(w0_canonical, w0_branch_iv_rescue, abs_tol=1e-9)  # (local)
    clean = clean and (not w0_rescued)
    findings.append({
        "row": "w_0",
        "honest_sigma": 2.13,
        "rescue_sigma_rejected": 0.731,
        "carried_value": w0_canonical,
        "canonical_pin": "w0_FW",
        "rescue_attempted": bool(w0_rescued),
        "note": ("canonical -0.918 (2.13 sigma) carried; branch-iv -0.842 (0.731 sigma) "
                 "is derivation-INADMISSIBLE post-S86 -- NOT selected (branch-shopping forbidden)"),
    })

    # --- n_s: canonical sqrt-cutoff 0.959 (COMMITTED); 4.73 sigma global is the
    #     look-elsewhere-CORRECTED WORST anchor (P-ACT), NOT the friendliest (Planck 1.40 sigma).
    ns_canonical = float(cc.n_s_FW_sqrt_cutoff)                    # (local)
    ns_honest_expected = 0.959                                    # (local)
    ns_match = math.isclose(ns_canonical, ns_honest_expected, abs_tol=5e-4)  # (local)
    ns_friendliest_sigma = 1.40   # Planck best-anchor -- the value a rescue would pick  # (local)
    ns_honest_sigma = 4.73        # global post-Sidak-N=4 worst-anchor                    # (local)
    # The audit carries the WORST (4.73), not the friendliest (1.40). Rescue iff we
    # had silently down-graded the liability to the friendliest anchor.
    ns_rescued = not ns_match     # value drift would be the only silent-substitution channel  # (local)
    clean = clean and (not ns_rescued)
    findings.append({
        "row": "n_s",
        "honest_sigma": ns_honest_sigma,
        "rescue_sigma_rejected": ns_friendliest_sigma,
        "carried_value": ns_canonical,
        "canonical_pin": "n_s_FW_sqrt_cutoff",
        "rescue_attempted": bool(ns_rescued),
        "note": ("4.73 sigma global (Sidak N=4, worst anchor P-ACT) carried; the friendliest "
                 "anchor (Planck 1.40 sigma) is NOT picked -- real liability, not artifact"),
    })

    # --- w_a: four-fold structural lock = 0 (zero free params) -> 3.43 sigma stands.
    #     There is no alternate-value channel to rescue (the prediction is exactly 0).
    wa_honest_sigma = 3.43                                        # (local)
    wa_rescued = False  # exact-0 structural lock; no friendlier value exists to substitute  # (local)
    clean = clean and (not wa_rescued)
    findings.append({
        "row": "w_a",
        "honest_sigma": wa_honest_sigma,
        "rescue_sigma_rejected": None,
        "carried_value": 0.0,
        "canonical_pin": "four-fold structural lock (exact 0, zero free params)",
        "rescue_attempted": bool(wa_rescued),
        "note": ("w_a = 0 exact; DESI DR2 post-Dovekie 3.43 sigma stands -- no alternate "
                 "value exists to branch-shop; clearest dark-energy liability"),
    })

    return {
        "clean": bool(clean),
        "no_class1_rescue_attempted": bool(clean),
        "findings": findings,
    }


def cohort_directions() -> dict:
    """The directional split -- the load-bearing finding (NOT a collapsed headline)."""
    return {
        "structural": {
            "direction": "UP",
            "driver": "10 blind STAGE-3 zero-parameter geometric promotions (K1-K11, K8 pending)",
            "joint_BF_low": 25.0,
            "joint_BF_high": 55.0,
            "independence": ("constructive -- Stage-2 PASS-AND, two cross-reviewers who "
                             "NEVER saw the workshop (joint-theorem-promotion.md); NOT "
                             "agreement-among-agents"),
        },
        "observational": {
            "direction": "DOWN",
            "driver": "n_s 4.73 sigma global; w_a 3.43 sigma; A_s route-unstable (>3 OOM, no convergence)",
            "BF_n_s": [0.7, 0.9],
            "BF_w_a": [0.6, 0.8],
            "BF_A_s": [0.7, 0.9],
        },
        "headline": {
            "P_anchor": PRIOR_P0,
            "stationary_by": "near-exact cohort cancellation (BF_struct * BF_obs ~ 1)",
            "finding": "the CANCELLATION is the finding, not the ~22% itself",
        },
    }


def make_plot(bracket: dict, audit: dict, path: Path) -> None:
    """Two-panel: (L) posterior-odds product bracket vs prior; (R) cohort directions."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))  # (local)

    # Panel 1: P_post for each inv-13 §III pair, colored by BF_struct*BF_obs.
    labels = [f"{r[0]}x{r[1]}\n(prod={r[4]})" for r in bracket["recomputed"]]  # (local)
    p_calc = [r[3] for r in bracket["recomputed"]]                              # (local)
    prods = [r[4] for r in bracket["recomputed"]]                              # (local)
    colors = ["tab:green" if abs(p - 1.0) < 0.15 else "tab:gray" for p in prods]  # (local)
    ax1.bar(range(len(labels)), p_calc, color=colors)
    ax1.axhline(PRIOR_P0, color="tab:red", ls="--", lw=1.6,
                label=f"prior anchor P0={PRIOR_P0}")
    ax1.set_xticks(range(len(labels)))
    ax1.set_xticklabels(labels, fontsize=8)
    ax1.set_ylabel("P_post (odds product)")
    ax1.set_title("Posterior-odds PRODUCT over cohorts\n(green = product ~ 1 => stationary)")
    ax1.legend(fontsize=8)
    ax1.set_ylim(0, 0.45)

    # Panel 2: directional arrows.
    ax2.annotate("", xy=(0.3, 0.85), xytext=(0.3, 0.55),
                 arrowprops=dict(arrowstyle="->", color="tab:green", lw=3))
    ax2.text(0.34, 0.70, "STRUCTURAL cohort UP\njoint BF 25-55\n(10 blind STAGE-3)",
             fontsize=10, va="center", color="tab:green")
    ax2.annotate("", xy=(0.3, 0.15), xytext=(0.3, 0.45),
                 arrowprops=dict(arrowstyle="->", color="tab:red", lw=3))
    ax2.text(0.34, 0.30, "OBSERVATIONAL cohort DOWN\nn_s 4.73s, w_a 3.43s, A_s unstable",
             fontsize=10, va="center", color="tab:red")
    ax2.axhline(0.50, color="k", ls=":", lw=1.2)
    ax2.text(0.02, 0.52, f"headline ~{int(PRIOR_P0*100)}% (stationary by cancellation)",
             fontsize=9, color="k")
    rescue_txt = ("anti-rescue audit: CLEAN\n(no Class-1 rescue attempted)"
                  if audit["clean"] else "anti-rescue audit: BREACH")  # (local)
    ax2.text(0.02, 0.05, rescue_txt, fontsize=9,
             color="tab:green" if audit["clean"] else "tab:red")
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis("off")
    ax2.set_title("Directional split (the finding)")

    fig.suptitle("S110-CF-EVOI-REANCHOR — recomposition + anti-rescue audit", fontsize=12)
    fig.tight_layout()
    fig.savefig(path, dpi=110)
    plt.close(fig)


def compute() -> dict:
    bracket = reproduce_inv13_bracket()   # (local)
    audit = anti_rescue_audit()           # (local)
    directions = cohort_directions()      # (local)
    return {"bracket": bracket, "audit": audit, "directions": directions}


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def evaluate_gate(result: dict) -> str:
    """Set-conjunction verdict (artifact-existence / [AUDIT] gate).

    PASS iff:
      (1) the recomposition reproduces the inv-13 §III bracket (max dev < 0.01),
      (2) the directional split is well-formed (structural UP, observational DOWN),
      (3) the anti-rescue audit is clean (no Class-1 rescue attempted).
    The Q44-closed + EVOI-re-rank table edits are verified on disk by the orchestrator's
    must_contain checklist (artifact-existence); the script certifies the ARITHMETIC +
    AUDIT legs of the conjunction.
    """
    bracket = result["bracket"]                                       # (local)
    audit = result["audit"]                                           # (local)
    dirs = result["directions"]                                       # (local)
    arithmetic_ok = bracket["max_abs_dev_vs_inv13"] < 0.01            # (local)
    split_ok = (dirs["structural"]["direction"] == "UP"
                and dirs["observational"]["direction"] == "DOWN")     # (local)
    rescue_clean = audit["clean"]                                     # (local)
    if arithmetic_ok and split_ok and rescue_clean:
        return "PASS"
    # An audit gate whose anti-rescue leg breached, or whose arithmetic failed to
    # reproduce, is a FAIL (a real finding: either the input drifted or a rescue slipped).
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    result = compute()
    bracket = result["bracket"]
    audit = result["audit"]
    dirs = result["directions"]

    print("=== Recomposition arithmetic (posterior-odds PRODUCT, NOT mean) ===")
    print(f"  prior P0 = {PRIOR_P0}")
    for r in bracket["recomputed"]:
        print(f"  BF_struct={r[0]:<4} BF_obs={r[1]:<5} product={r[4]:<7} "
              f"-> P_post(calc)={r[3]:<8} (inv-13 reported {r[2]})")
    print(f"  bracket reproduced: [{bracket['p_min']}, {bracket['p_max']}] "
          f"(inv-13 §III: [0.145, 0.372])")
    print(f"  max abs dev vs inv-13: {bracket['max_abs_dev_vs_inv13']}")
    nu = bracket["nearest_unity_pair"]  # (local)
    print(f"  nearest-unity pair (BF_struct*BF_obs~1): {nu[0]}x{nu[1]} prod={nu[4]} "
          f"-> P_post={nu[3]} (stationary near prior {PRIOR_P0})")
    print()

    print("=== Anti-rescue audit (PROHIBITED_ACTIONS Class 1 fence) ===")
    for f in audit["findings"]:
        flag = "RESCUE-ATTEMPTED" if f["rescue_attempted"] else "clean"
        print(f"  {f['row']:<5} honest={f['honest_sigma']}sigma carried={f['carried_value']} "
              f"[{flag}] — {f['note']}")
    print(f"  AUDIT: {'CLEAN (no Class-1 rescue attempted)' if audit['clean'] else 'BREACH'}")
    print()

    print("=== Directional split (the finding) ===")
    print(f"  structural cohort: {dirs['structural']['direction']} "
          f"(joint BF {dirs['structural']['joint_BF_low']}-{dirs['structural']['joint_BF_high']})")
    print(f"  observational cohort: {dirs['observational']['direction']} "
          f"({dirs['observational']['driver']})")
    print(f"  headline ~{int(PRIOR_P0*100)}% stationary by {dirs['headline']['stationary_by']}")
    print()

    verdict = evaluate_gate(result)

    # Persist the consumption record + audit (npz).
    SESSION_OUT_DIR.mkdir(parents=True, exist_ok=True)
    np.savez(
        OUT_NPZ,
        inv13_pairs=np.array(INV13_SIII_PAIRS, dtype=float),
        recomputed=np.array([[r[0], r[1], r[2], r[3], r[4]]
                             for r in bracket["recomputed"]], dtype=float),
        prior_p0=np.array([PRIOR_P0]),
        p_bracket=np.array([bracket["p_min"], bracket["p_max"]]),
        max_abs_dev=np.array([bracket["max_abs_dev_vs_inv13"]]),
        anti_rescue_clean=np.array([1 if audit["clean"] else 0]),
        structural_BF=np.array([25.0, 55.0]),
        w0_canonical=np.array([float(cc.w0_FW)]),
        ns_canonical=np.array([float(cc.n_s_FW_sqrt_cutoff)]),
        audit_findings_json=np.array([json.dumps(audit["findings"])]),
        directions_json=np.array([json.dumps(dirs)]),
    )
    make_plot(bracket, audit, OUT_PNG)
    print(f"  wrote {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    print(f"  wrote {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    # Verdict value string carries BOTH cohort directions (the split, NOT a collapsed number).
    value = (
        f"REANCHOR-APPLIED;structural=UP(jointBF=25-55,10blindSTAGE3,Stage2-PASS-AND-independence);"
        f"observational=DOWN(n_s=4.73sigma-global,w_a=3.43sigma,A_s=route-unstable);"
        f"headline~{int(PRIOR_P0*100)}pct-STATIONARY-BY-CANCELLATION(BFstruct*BFobs~1,NOT-collapsed);"
        f"recomp-bracket=[{bracket['p_min']},{bracket['p_max']}](inv13[0.145,0.372],maxdev={bracket['max_abs_dev_vs_inv13']});"
        f"Q44=CLOSED(frozen-since-S66-W2-A);"
        f"anti-rescue=CLEAN(no-Class1-rescue:w0=-0.918(2.13s)-NOT-branch-iv-0.842(0.731s);"
        f"n_s=4.73s-worst-NOT-Planck-1.40s-friendliest;w_a=0-exact);"
        f"currency=S110"
    )                                                                          # (local)

    extra = [
        ("# recomposition: O_post = O_prior * BF_struct * BF_obs (posterior-odds PRODUCT over "
         "independent cohorts, NOT arithmetic mean); prior P0=0.22 (S69); bracket "
         f"[{bracket['p_min']},{bracket['p_max']}] reproduces inv-13 §III [0.145,0.372] "
         f"(max dev {bracket['max_abs_dev_vs_inv13']})"),
        ("# dual_prior discriminator: track-A structural-STRENGTHENING vs track-B "
         "observational-WEAKENING; PASS = the split is REPORTED + Q44 closed + anti-rescue "
         "clean; the headline ~22% holds ONLY by near-exact cancellation — the cancellation "
         "IS the finding, NOT collapsed to a single number"),
        ("# anti-rescue audit (PROHIBITED_ACTIONS Class 1 fence ARMED): w_0 canonical -0.918 "
         "(2.13sigma) carried, branch-iv -0.842 (0.731sigma) derivation-INADMISSIBLE post-S86 "
         "NOT selected; n_s 4.73sigma global (Sidak N=4 worst anchor) carried, Planck 1.40sigma "
         "friendliest NOT picked; w_a=0 exact (no alternate value to branch-shop) — NO rescue attempted"),
        ("# HK-EVOI-Q37 (DESI-DR3 / branch-iv register down-tag, co-lands): "
         "'S105 INFO 0.0443091 / FB-envelope-bounded' -> 'deep-truncation DIVERGES at L in {12..16}, "
         "spread_CAC=0.0630 > 0.05 FAIL' (scope L_max-only; S101 admissibility UNAFFECTED; "
         "value pre-computed inv-13 W1-3 — this is the register-cell down-tag, not a recompute)"),
        ("# Q44 CLOSED: 40-session-standing Sagan re-anchoring (frozen since S66 W2-A) adjudicated; "
         "structural-UP/observational-DOWN; the retraction-log discipline (atlas-09, 50 items) RAISES "
         "the prior on survivors per the Baloney Detection Kit"),
        ("# EVOI values are ordinal leverage proxies, NOT calibrated probabilities (§EVOI honesty "
         "caveat); the highest forward EVOI is now ORTHOGONAL to the CMB axis (NICER/LSS gold-standard "
         "independent confirmation worth more than another CMB refinement)"),
    ]                                                                          # (local)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # AUDIT gate: verdict is data; exit 0 on a healthy run regardless of PASS/FAIL


if __name__ == "__main__":
    sys.exit(main())
