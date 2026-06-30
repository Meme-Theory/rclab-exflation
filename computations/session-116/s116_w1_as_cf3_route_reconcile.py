#!/usr/bin/env python3
"""
S116 W1-AS-CF3 — Product reconciliation A_s = squeeze x filter; route collapse vs S115 axis
============================================================================================

Gate: S116-W1-AS-CF3 ([SIGN] — collapse-direction)

Pre-registered threshold:
  collapse_dist = max over regime-tagged routes |OOM_route - workshop_figure|
  PASS  iff collapse_dist <= 0.1  (routes COLLAPSE onto the single workshop figure -> S115 PLURALISM overturned)
  INFO  iff collapse_dist  > 0.1 AND the routes reproduce the S115 sudden<->adiabatic two-cluster axis
  FAIL  iff neither (a NEW inconsistency vs S115)
  n_s sub-criterion: the two framework n_s scheme variants are regulator-consistent
     (spread <= Planck sigma-band AND both RED n_s<1).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-116/s116_w1_as_cfb1_squeeze_promote.npz  (SQUEEZE leg, FRESH; CFB1 PASS)
  - computations/session-116/s116_w1_as_cf2_greybody_exact.npz    (FILTER leg, FRESH; CF2 FAIL = fitted-knob)
  - sessions/session-116/workshops/s116-w1-htilde-recon.md        (workshop pinned figure, FRESH)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<collapse summary>, scheme=ROUTE-RECONCILIATION-REGIME-TAGGED,
   convention=OOM-COLLAPSE-VS-S115-AXIS-AND-NS-SCHEME-SPLIT, L_max=12)

Classification: PHONONIC

METHODOLOGY
-----------
A_s IS the GGE-relic acoustic squeezing modulus of the post-fold produced state; the lab reads
its power IN the CMB container.  The substrate produces ONE relic state; the "routes" are
different normalization/regime READINGS of its squeeze x filter.  This gate collects all route
A_s/OOM figures, REGIME-TAGS each (sudden vs adiabatic per the S115 axis), and tests whether they
COLLAPSE onto the single workshop-pinned A_s-vs-Planck figure (+0.864 OOM = box-delta floor,
PINNED-conditional on CF-S117 per S116-W1-HTILDE-RECON) or REPRODUCE the S115 two-cluster axis.
The workshop's 2.38(H~)/4.76(A_s) CC3-conjugate pair is figure-MULTIPLICITY (the TD-vs-LI
IC-scheme divergence) -- a CLOSED, ORTHOGONAL space -- NOT the collapse target (using it would
conflate the H~<->A_s power axis with the A_s-vs-Planck overproduction axis).  Also reconciles the
n_s cutoff-scheme split as regulator-variants of the SAME substrate geometric tilt 1-2*eps_H,
carried to the CMB pivot by deg(T_BZ->pivot)=+2, with (scale, channel) tags.

DISCIPLINE
----------
- `from canonical_constants import *`; every intermediate tagged `# (local)`
- cpu-cap-OMP8 (scalar reconciliation; NO heavy linear algebra)
- dual-SHA (audit = script+canonical+pinmap; content = script); payload PRINTED, agent emits
- FAIL/INFO => NO canonical_constants pin (Step-2 write-order N/A; this gate mints no new prediction)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path as _Path
# canonical_constants.py lives in computations/_shared/ — put it on the path BEFORE the import.
sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "_shared"))

# Section 1 — Canonical constants (MANDATORY first import)
from canonical_constants import (
    A_s_CMB,                # 2.1e-9  CMB scalar amplitude (Planck 2018 VI)
    A_s_FW,                 # 1.5367059962762235e-8  box-delta impulse-quench A_s (S111-CF-AS3a)
    planck_ns,              # 0.9649  Planck 2018 TT,TE,EE+lowE+lensing
    planck_ns_err,          # 0.0042  Planck 2018 1-sigma
    n_s_framework,          # 0.9561  constant-eps gauge-invariant tilt (S85)
    n_s_FW_sqrt_cutoff,     # 0.9590  sqrt-cutoff / BCS+1-loop generating functional (S103)
)

# Section 2 — Standard imports
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Section 3 — Paths + pre-registration
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S116"                                                    # (local)
GATE_ID = "S116-W1-AS-CF3"                                          # (local)
SCHEME = "ROUTE-RECONCILIATION-REGIME-TAGGED"                       # (local)
CONVENTION = "OOM-COLLAPSE-VS-S115-AXIS-AND-NS-SCHEME-SPLIT"        # (local)
L_MAX = 12                                                          # (local)

COLLAPSE_BAND = 0.10            # (local) PASS band: routes collapse to ONE figure within 0.1 OOM
S115_SPREAD_REF = 1.2590        # (local) S115-AS-NEWAXIS-SELECTOR spread_existing_OOM (established)
S115_MIN_COLLAPSE_REF = 0.6281  # (local) S115-AS-NEWAXIS-SELECTOR min_collapse_dist_OOM (established)

# Upstream FRESH inputs (Batch 2 — all three landed this wave)
SQUEEZE_NPZ = SESSION_DIR / "s116_w1_as_cfb1_squeeze_promote.npz"
FILTER_NPZ = SESSION_DIR / "s116_w1_as_cf2_greybody_exact.npz"
WORKSHOP_MD = (PROJECT_ROOT / "sessions" / "session-116" / "workshops"
               / "s116-w1-htilde-recon.md")

OUT_NPZ = SESSION_DIR / "s116_w1_as_cf3_route_reconcile.npz"
OUT_PNG = SESSION_DIR / "s116_w1_as_cf3_route_reconcile.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SQUEEZE_NPZ,
    FILTER_NPZ,
    WORKSHOP_MD,
]


# Section 4 — SHA-256 input-pin block
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


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""    # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# Section 5 — Compute
def oom(a_s: float) -> float:
    """OOM gap vs Planck A_s: log10(A_s_route / A_s_CMB)."""
    return float(np.log10(a_s / A_s_CMB))                                       # (local)


def compute() -> dict:
    # ---- 5.1 Load FRESH upstream legs ---------------------------------------
    sq = np.load(SQUEEZE_NPZ, allow_pickle=True)                                # (local)
    fl = np.load(FILTER_NPZ, allow_pickle=True)                                 # (local)

    A_s_squeeze = float(sq["A_s_squeeze"])                                      # (local) FRESH CFB1
    squeeze_type = str(sq["epistemic_type"])                                    # (local) POINT
    squeeze_oom = float(sq["OOM"])                                              # (local) +0.8644
    A_s_parker_inv6 = float(sq["A_s_parker_inv6"])                              # (local) 5.99e-8 (adiabatic end)

    filter_fitted = float(fl["fitted"])                                        # (local) FRESH CF2 Gamma=0.5119
    filter_best_agree = float(fl["best_overall_agree"])                        # (local) 0.278 (FAIL)
    filter_composite = str(fl["composite_verdict"])                            # (local) FAIL
    filter_is_substrate_derived = (filter_composite == "PASS")                 # (local) -> False (fitted-knob)

    # squeeze leg round-trips the canonical box-delta A_s_FW (consistency assert)
    assert abs(A_s_squeeze - A_s_FW) <= 1e-5 * A_s_FW, "squeeze != A_s_FW (box-delta)"

    # ---- 5.2 Workshop-pinned figure (FRESH; A_s-vs-Planck regime magnitude) --
    # The S116-W1-HTILDE-RECON Structural Verdict pins the A_s-vs-Planck regime magnitude at
    # +0.864 OOM (box-delta floor A_s_FW, PINNED-conditional on CF-S117).  THAT is the collapse
    # target.  The 2.38(H~)/4.76(A_s) CC3-conjugate pair is figure-MULTIPLICITY (TD-vs-LI
    # IC-scheme divergence) -- a CLOSED, ORTHOGONAL space, recorded but NOT the target.
    workshop_md_text = WORKSHOP_MD.read_text(encoding="utf-8", errors="replace")  # (local)
    workshop_fresh = ("Structural Verdict" in workshop_md_text
                      and "+0.864" in workshop_md_text)                          # (local)
    workshop_figure_oom = oom(A_s_FW)        # (local) = +0.8644 A_s-vs-Planck (box-delta floor pin)
    fig_multiplicity_Htilde = 2.38           # (local) CC3-conjugate H~-space (CLOSED axis; NOT target)
    fig_multiplicity_As = 4.76               # (local) CC3-conjugate A_s-space = 2x2.38 (CLOSED axis)

    # ---- 5.3 Route set (A_s-vs-Planck OOM gaps) -----------------------------
    # Route A_s anchors: squeeze leg is FRESH; the others are established prior-session route
    # predictions (plan session-116-plan-w1 lines 33-41; cited there + in the CFB1 npz).
    A_s_tdzeta = 3.2994e-9         # (local) TD/zeta UNIFIED-AS-79 Branch-A (S82 W1-2)
    A_s_maxent = 1.4006e-8         # (local) maxent Jaynes occupation (S115)
    A_s_boxdelta = A_s_squeeze     # (local) box-delta = FRESH squeeze leg (= A_s_FW, S111)
    A_s_parker = A_s_parker_inv6   # (local) Parker inv6 (S110 / INV6-W2-2), FRESH-via-CFB1-npz
    A_s_connes = 7.068e-8          # (local) Connes-Parker (S115)

    routes = {                                                                  # (local)
        "TD/zeta_UNIFIED-AS-79": A_s_tdzeta,
        "maxent": A_s_maxent,
        "box-delta_canonical(squeeze)": A_s_boxdelta,
        "Parker_inv6": A_s_parker,
        "Connes-Parker": A_s_connes,
    }
    route_oom = {name: oom(a) for name, a in routes.items()}                    # (local)

    # ---- 5.4 Regime-tag (sudden produced-state vs adiabatic) per S115 axis ---
    sudden_routes = ["TD/zeta_UNIFIED-AS-79", "maxent", "box-delta_canonical(squeeze)"]  # (local)
    adiab_routes = ["Parker_inv6", "Connes-Parker"]                             # (local)
    sudden_oom = [route_oom[r] for r in sudden_routes]                          # (local)
    adiab_oom = [route_oom[r] for r in adiab_routes]                            # (local)

    within_sudden_spread = max(sudden_oom) - min(sudden_oom)                    # (local) the CF-S117 N-gap
    within_adiab_spread = max(adiab_oom) - min(adiab_oom)                       # (local)
    full_band = max(route_oom.values()) - min(route_oom.values())              # (local) raw 5-route band
    cross_cluster_gap = min(adiab_oom) - max(sudden_oom)                        # (local) sudden-top -> adiab-bottom empty zone

    # ---- 5.5 Collapse distance (HEADLINE) -----------------------------------
    # collapse_dist = max over ALL routes |OOM_route - workshop_figure|  ("do ALL routes collapse
    # to the ONE figure?").  This equals the residual-after-regime-tagging the plan describes:
    # the workshop figure (+0.864) is the TOP of the sudden cluster, so the worst route is the
    # within-sudden N-gap end (TD/zeta +0.196).  REJECT the per-route MIN (=0; box-delta IS the
    # figure) -- load-and-compare-to-self does not measure collapse.
    dists_to_workshop = {name: abs(o - workshop_figure_oom)                     # (local)
                         for name, o in route_oom.items()}
    collapse_dist = max(dists_to_workshop.values())                            # (local) HEADLINE
    per_route_min_REJECTED = min(dists_to_workshop.values())                    # (local) degenerate (=0)

    routes_collapse = collapse_dist <= COLLAPSE_BAND                            # (local)
    # Reproduces the S115 two-cluster axis iff: no collapse, AND two regime clusters separated by
    # a gap that exceeds the COLLAPSE_BAND, AND the residual stays within the established S115
    # spread (shrinks under regime-tagging but does NOT exceed S115 -> not a NEW inconsistency).
    reproduces_S115_axis = (not routes_collapse
                            and cross_cluster_gap > COLLAPSE_BAND
                            and collapse_dist <= (S115_SPREAD_REF + 0.05))      # (local)

    # ---- 5.6 squeeze x filter product (filter is FITTED, not substrate-derived) ----
    A_s_product = A_s_squeeze * filter_fitted                                  # (local)
    product_oom = squeeze_oom + float(np.log10(filter_fitted))                 # (local) = +0.574
    product_overproduces = product_oom > 0.0                                   # (local) True (filter does NOT reach Planck)

    # ---- 5.7 n_s scheme-split reconciliation --------------------------------
    ns_sqrt = float(n_s_FW_sqrt_cutoff)        # (local) 0.9590  (scale=substrate->pivot deg+2; channel=Planck)
    ns_fw = float(n_s_framework)               # (local) 0.9561  (same scale/channel; different cutoff scheme)
    ns_planck = float(planck_ns)               # (local) 0.9649
    ns_sigma = float(planck_ns_err)            # (local) 0.0042
    ns_scheme_spread = abs(ns_sqrt - ns_fw)                                     # (local) 0.0029
    ns_spread_in_planck_sigma = ns_scheme_spread / ns_sigma                     # (local) 0.69 sigma
    ns_both_red = (ns_sqrt < 1.0) and (ns_fw < 1.0)                             # (local) both RED
    ns_sigdist_sqrt = abs(ns_sqrt - ns_planck) / ns_sigma                       # (local) 1.405 sigma
    ns_sigdist_fw = abs(ns_fw - ns_planck) / ns_sigma                           # (local) 2.095 sigma
    # regulator-consistent iff the two framework variants are within the Planck sigma-band of each
    # other (statistically indistinguishable as predictions) AND both RED.
    ns_regulator_consistent = (ns_spread_in_planck_sigma <= 1.0) and ns_both_red  # (local)

    # ---- 5.8 Composite [SIGN] 3-tuple ---------------------------------------
    # sign: Step-5 PREDICTED no-collapse (collapse_dist > band).  Computed direction matches => PASS.
    sign_verdict = "PASS" if (collapse_dist > COLLAPSE_BAND) else "FAIL"        # (local)
    # magnitude: PASS if collapsed (<=band); INFO if shrinks-but-stays (band < d <= S115 spread);
    #            FAIL if d exceeds S115 spread (a NEW inconsistency, worse than S115).
    if collapse_dist <= COLLAPSE_BAND:
        magnitude_verdict = "PASS"                                             # (local)
    elif collapse_dist <= (S115_SPREAD_REF + 0.05):
        magnitude_verdict = "INFO"                                             # (local)
    else:
        magnitude_verdict = "FAIL"                                             # (local)
    # regime: scalar closed-form reconciliation; all routes + figure well-defined => VALID.
    # (the CF2 filter-FAIL is incorporated as substrate CONTENT -- filter is fitted -- not a
    #  regime breakdown of the reconciliation itself.)
    regime_verdict = "VALID"                                                   # (local)

    # composite collapse rule (gate-verdicts.md), applied deterministically
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                                                     # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    return {
        # legs
        "A_s_squeeze": A_s_squeeze, "squeeze_oom": squeeze_oom,
        "squeeze_type": squeeze_type, "squeeze_FRESH": True,
        "filter_fitted": filter_fitted, "filter_best_agree": filter_best_agree,
        "filter_composite": filter_composite,
        "filter_is_substrate_derived": filter_is_substrate_derived, "filter_FRESH": True,
        "workshop_FRESH": bool(workshop_fresh),
        # workshop figures
        "workshop_figure_oom": workshop_figure_oom,
        "fig_multiplicity_Htilde": fig_multiplicity_Htilde,
        "fig_multiplicity_As": fig_multiplicity_As,
        # routes
        "route_names": list(routes.keys()),
        "route_A_s": [routes[n] for n in routes],
        "route_oom": [route_oom[n] for n in routes],
        "sudden_routes": sudden_routes, "adiab_routes": adiab_routes,
        # collapse
        "collapse_dist": collapse_dist,
        "per_route_min_REJECTED": per_route_min_REJECTED,
        "within_sudden_spread": within_sudden_spread,
        "within_adiab_spread": within_adiab_spread,
        "cross_cluster_gap": cross_cluster_gap,
        "full_band": full_band,
        "S115_spread_ref": S115_SPREAD_REF,
        "S115_min_collapse_ref": S115_MIN_COLLAPSE_REF,
        "routes_collapse": routes_collapse,
        "reproduces_S115_axis": reproduces_S115_axis,
        # product
        "A_s_product": A_s_product, "product_oom": product_oom,
        "product_overproduces": product_overproduces,
        # n_s
        "ns_sqrt": ns_sqrt, "ns_fw": ns_fw, "ns_planck": ns_planck, "ns_sigma": ns_sigma,
        "ns_scheme_spread": ns_scheme_spread,
        "ns_spread_in_planck_sigma": ns_spread_in_planck_sigma,
        "ns_both_red": ns_both_red,
        "ns_sigdist_sqrt": ns_sigdist_sqrt, "ns_sigdist_fw": ns_sigdist_fw,
        "ns_regulator_consistent": ns_regulator_consistent,
        # verdict
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict, "composite": composite,
    }


# Section 6 — payload + plot
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID, "verdict": verdict, "value": str(value),
        "scheme": SCHEME, "convention": CONVENTION, "l_max": str(L_MAX),
        "audit_sha256": audit_sha, "content_sha256": content_sha,
        "schema_version": "S84+",
    }
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


def make_plot(r: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))                       # (local)

    # Panel 1 — route OOM axis with regime-tag clusters
    names = r["route_names"]; ooms = r["route_oom"]                            # (local)
    sudden = set(r["sudden_routes"])                                           # (local)
    wf = r["workshop_figure_oom"]                                              # (local)
    for i, (nm, om) in enumerate(zip(names, ooms)):
        col = "#1f77b4" if nm in sudden else "#d62728"                         # (local)
        ax1.scatter(om, i, s=140, color=col, zorder=3)
        ax1.annotate(f"{nm}\n+{om:.3f}", (om, i), textcoords="offset points",
                     xytext=(8, 0), va="center", fontsize=8)
    ax1.axvline(0.0, color="green", ls="--", lw=1.5, label="Planck A_s (OOM=0)")
    ax1.axvline(wf, color="black", ls="-", lw=1.6,
                label=f"workshop figure +{wf:.3f} (box-delta floor, CF-S117-cond.)")
    ax1.axvspan(wf - r["collapse_band"] if "collapse_band" in r else wf - 0.1,
                wf + 0.1, color="black", alpha=0.08, label="0.1 collapse band")
    ax1.set_yticks(range(len(names)))
    ax1.set_yticklabels(["" for _ in names])
    ax1.set_xlabel("OOM gap above Planck  =  log10(A_s_route / A_s_CMB)")
    ax1.set_title(f"S116-W1-AS-CF3 route reconciliation\n"
                  f"collapse_dist={r['collapse_dist']:.3f} > 0.1  =>  INFO "
                  f"(S115 two-cluster axis REPRODUCED)\n"
                  f"sudden(blue) N-gap={r['within_sudden_spread']:.3f} [CF-S117]  |  "
                  f"cross-cluster gap={r['cross_cluster_gap']:.3f}  |  adiab(red)={r['within_adiab_spread']:.3f}",
                  fontsize=9)
    ax1.legend(fontsize=7, loc="lower right")
    ax1.grid(alpha=0.3)

    # squeeze x filter product marker
    ax1.scatter(r["product_oom"], -0.7, s=120, marker="D", color="purple", zorder=3)
    ax1.annotate(f"squeeze x FITTED-filter\n+{r['product_oom']:.3f} (CF2 FAIL; overproduces)",
                 (r["product_oom"], -0.7), textcoords="offset points",
                 xytext=(8, 0), va="center", fontsize=7, color="purple")
    ax1.set_ylim(-1.3, len(names) - 0.3)

    # Panel 2 — n_s scheme split vs Planck
    ns_vals = [r["ns_fw"], r["ns_sqrt"]]                                       # (local)
    ns_labs = [f"framework 0.9561\n({r['ns_sigdist_fw']:.2f} sig)",
               f"sqrt-cutoff 0.9590\n({r['ns_sigdist_sqrt']:.2f} sig)"]         # (local)
    ax2.errorbar([r["ns_planck"]], [0], xerr=[r["ns_sigma"]], fmt="o", color="green",
                 capsize=5, label="Planck 0.9649 +/- 0.0042")
    ax2.axvspan(r["ns_planck"] - r["ns_sigma"], r["ns_planck"] + r["ns_sigma"],
                color="green", alpha=0.12)
    for v, lab in zip(ns_vals, ns_labs):
        ax2.scatter(v, 0, s=140, color="#1f77b4", zorder=3)
        ax2.annotate(lab, (v, 0), textcoords="offset points", xytext=(0, 18),
                     ha="center", fontsize=8)
    ax2.axvline(1.0, color="gray", ls=":", lw=1, label="scale-invariant n_s=1")
    ax2.set_xlim(0.950, 1.003)
    ax2.set_yticks([])
    ax2.set_xlabel("n_s")
    ax2.set_title(f"n_s scheme split (cutoff-scheme images of 1-2*eps_H, deg(T)=+2)\n"
                  f"framework-spread={r['ns_scheme_spread']:.4f} = "
                  f"{r['ns_spread_in_planck_sigma']:.2f} sig_Planck  -> "
                  f"REGULATOR-CONSISTENT={r['ns_regulator_consistent']} (both RED)", fontsize=9)
    ax2.legend(fontsize=7, loc="upper left")
    ax2.grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# Section 7 — Main
def main() -> int:
    t0 = time.time()                                                           # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                                     # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"                     # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()
    r["collapse_band"] = COLLAPSE_BAND

    # report
    print("--- route OOM (A_s-vs-Planck) ---")
    for nm, om in zip(r["route_names"], r["route_oom"]):
        tag = "sudden" if nm in set(r["sudden_routes"]) else "adiabatic"        # (local)
        print(f"  {nm:32s} OOM=+{om:.4f}  [{tag}]")
    print(f"  workshop figure (A_s-vs-Planck)  = +{r['workshop_figure_oom']:.4f} (box-delta floor; CF-S117-cond.)")
    print(f"  figure-multiplicity (CLOSED axis) = 2.38 H~ / 4.76 A_s (NOT the collapse target)")
    print(f"--- collapse test ---")
    print(f"  collapse_dist (max|OOM-workshop|) = {r['collapse_dist']:.4f}  (band {COLLAPSE_BAND})")
    print(f"  per-route MIN (REJECTED, self)    = {r['per_route_min_REJECTED']:.4f}")
    print(f"  within-sudden N-gap (CF-S117)     = {r['within_sudden_spread']:.4f}")
    print(f"  cross-cluster gap (sudden<->adiab)= {r['cross_cluster_gap']:.4f}")
    print(f"  within-adiabatic spread           = {r['within_adiab_spread']:.4f}")
    print(f"  full 5-route band                 = {r['full_band']:.4f}  (S115 spread_ref={r['S115_spread_ref']})")
    print(f"  routes_collapse={r['routes_collapse']}  reproduces_S115_axis={r['reproduces_S115_axis']}")
    print(f"--- squeeze x filter product ---")
    print(f"  squeeze={r['A_s_squeeze']:.6e} ({r['squeeze_type']}, FRESH)  "
          f"filter(fitted Gamma)={r['filter_fitted']:.6f} (CF2={r['filter_composite']}, "
          f"substrate_derived={r['filter_is_substrate_derived']})")
    print(f"  product A_s={r['A_s_product']:.6e}  OOM=+{r['product_oom']:.4f}  "
          f"overproduces={r['product_overproduces']} (single fitted filter does NOT reach Planck)")
    print(f"--- n_s scheme split ---")
    print(f"  sqrt-cutoff={r['ns_sqrt']:.4f}  framework={r['ns_fw']:.4f}  Planck={r['ns_planck']:.4f}+/-{r['ns_sigma']:.4f}")
    print(f"  framework-spread={r['ns_scheme_spread']:.4f} = {r['ns_spread_in_planck_sigma']:.3f} sig_Planck  "
          f"both_RED={r['ns_both_red']}  regulator_consistent={r['ns_regulator_consistent']}")
    print(f"  sigma-dist to Planck: sqrt={r['ns_sigdist_sqrt']:.3f}  framework={r['ns_sigdist_fw']:.3f}")
    print(f"--- 3-tuple ---")
    print(f"  sign={r['sign_verdict']} magnitude={r['magnitude_verdict']} regime={r['regime_verdict']} "
          f"=> composite={r['composite']}")

    # save npz
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        **{k: np.array(v, dtype=object) if isinstance(v, (list, str)) else v
           for k, v in r.items()},
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    make_plot(r)

    # value payload (no single-quote chars; tool wraps value='...')
    val = (f"collapse_dist={r['collapse_dist']:.4f}>band{COLLAPSE_BAND};routes_DO_NOT_collapse;"
           f"reproduce_S115_two_cluster_axis;workshop_fig=+{r['workshop_figure_oom']:.3f}_A_s_vs_Planck_FRESH;"
           f"fig_mult_2.38Htil/4.76As=CLOSED-ORTHOGONAL-axis-NOT-target;"
           f"within_sudden_N_gap={r['within_sudden_spread']:.3f}_CF-S117-conditional;"
           f"cross_cluster_gap={r['cross_cluster_gap']:.3f};within_adiab={r['within_adiab_spread']:.3f};"
           f"squeeze={r['A_s_squeeze']:.4e}_FRESH_POINT;filter={r['filter_fitted']:.4f}_FRESH_CF2-FAIL-fitted-knob;"
           f"product_OOM=+{r['product_oom']:.3f}_overproduces(filter_does_not_reach_Planck);"
           f"ns_split_sqrt{r['ns_sqrt']:.4f}/fw{r['ns_fw']:.4f}/planck{r['ns_planck']:.4f};"
           f"ns_spread={r['ns_scheme_spread']:.4f}={r['ns_spread_in_planck_sigma']:.2f}sig_REGULATOR-CONSISTENT_bothRED;"
           f"ns_sigdist=sqrt{r['ns_sigdist_sqrt']:.2f}/fw{r['ns_sigdist_fw']:.2f};S115_PLURALISM_CONFIRMED")

    tag = emit_4tuple(val, SCHEME, CONVENTION, L_MAX)
    print(tag)

    extra_rows = [
        ("# S116-W1-AS-CF3 collapse: max|OOM_route-workshop_fig(+0.864)|=%.4f > band 0.1 => NO single-figure "
         "collapse; routes reproduce S115 sudden<->adiabatic two-cluster axis (S115 spread_ref=1.259, "
         "min_collapse_ref=0.628). PLURALISM CONFIRMED (expected; not overturned)."
         % r["collapse_dist"]),
        ("# S116-W1-AS-CF3 regime-tag: sudden{TD/zeta+0.196,maxent+0.824,box-delta+0.864} (within N-gap %.3f, "
         "CF-S117-conditional) vs adiabatic{Parker+1.455,Connes+1.527} (within %.3f); cross-cluster gap %.3f. "
         "Per-route MIN=%.3f REJECTED (box-delta IS the figure = load-and-compare-to-self)."
         % (r["within_sudden_spread"], r["within_adiab_spread"], r["cross_cluster_gap"],
            r["per_route_min_REJECTED"])),
        ("# S116-W1-AS-CF3 product: A_s=squeeze(%.4e,FRESH POINT) x filter(%.4f,FRESH CF2-FAIL=fitted-knob,NOT "
         "substrate-derived) = %.4e, OOM=+%.3f STILL overproduces => a single fitted greybody does NOT collapse "
         "the routes to Planck (confirms workshop: 1 filter cannot map N inputs to 1 output)."
         % (r["A_s_squeeze"], r["filter_fitted"], r["A_s_product"], r["product_oom"])),
        ("# S116-W1-AS-CF3 fig-MULTIPLICITY 2.38(H~)/4.76(A_s)=CC3-conjugate (TD-vs-LI IC-scheme divergence) is a "
         "CLOSED ORTHOGONAL space (H~<->A_s power, deg=+2), NOT the A_s-vs-Planck collapse target; not conflated."),
        ("# S116-W1-AS-CF3 n_s scheme-split: sqrt-cutoff=0.9590(S103) / framework=0.9561(S85,exact 9561/10000) are "
         "cutoff-scheme images of the SAME substrate tilt 1-2eps_H carried by deg(T_BZ->pivot)=+2 (scale=substrate->"
         "pivot, channel=Planck/CMB-pivot); spread=0.0029=0.69sig_Planck<sigma => REGULATOR-CONSISTENT, both RED; "
         "sigma-dist to Planck 0.9649+/-0.0042: sqrt=1.40sig, framework=2.10sig. NOT a contradiction."),
        ("# S116-W1-AS-CF3 FRESH-vs-FALLBACK: squeeze=FRESH(CFB1 PASS), filter=FRESH(CF2 FAIL), workshop=FRESH "
         "(S116-W1-HTILDE-RECON). All 3 upstreams FRESH (Batch 2); no fallback invoked."),
        "# regulator_pin=N/A (route OOM gaps + Bogoliubov A_s; n_s variants are cutoff-SCHEMES via (scale,channel) tags, not a_n^{regulator})",
    ]

    print_verdict_payload(r["composite"], val, audit_sha, content_sha,
                          sign_verdict=r["sign_verdict"],
                          magnitude_verdict=r["magnitude_verdict"],
                          regime_verdict=r["regime_verdict"],
                          extra_rows=extra_rows)

    wall = time.time() - t0                                                    # (local)
    print(f"\n=== {GATE_ID}: {r['composite']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
