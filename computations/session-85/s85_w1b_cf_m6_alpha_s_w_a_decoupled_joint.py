#!/usr/bin/env python3
"""
S85 W1b-10: ALPHA-S x W-A DECOUPLED-JOINT EVIDENCE LEDGER (CF-M6)
=================================================================

Gate: S85-W1b-CF-M6-ALPHA-S-W-A-DECOUPLED-JOINT
Trigger: [VERIFY]
Classification: META (decoupled-joint evidence ledger; detector-independence audit)
Agent: mack-cosmic-bridge

Hypothesis: alpha_s (CMB-S4/HD/LiteBIRD) and w_a (DESI-DR3/Euclid/LSST)
are probed by different detector classes. The framework's structural
prediction yields both alpha_s_canon and w_a_canon from the SAME
spectral triple, so if the detector classes are truly independent,
the joint evidence is the PRODUCT of individual Bayes factors:
  BF_indep = BF_alpha_s * BF_w_a
  BF_joint = p(D_alpha, D_w | FW) / p(D_alpha, D_w | LCDM)
  Independence test: |log10(BF_joint) - log10(BF_indep)| < 0.30

Pre-verification (Python):

  BF_alpha_s from W1b-3 (executed; 3 priors):
    wide_uniform:   BF = 4.162, log10 = +0.619
    narrow_uniform: BF = 1.682, log10 = +0.226
    planck_gauss:   BF = 0.989, log10 = -0.005

  BF_w_a from analog W1b-3 formulation applied to w_0:
    framework point: w_0_FW = -0.918 (canonical w0_FW, S58)
    DESI DR3 projected sigma(w_0) = 0.025
    LCDM null: w_0 = -1
    L_fw(w_0_FW | data=w_0_FW, sig=0.025) = 15.96  (framework-right case)
    narrow uniform prior [-1.2, -0.8]: marg_L = 2.50,
      BF_w_narrow = 6.38, log10 = +0.805
    Alternatively via W1a-9 Fisher pull (w_0 pull = 3.28 sigma):
      log10(BF_w) = 0.5 * pull^2 / ln(10) = +2.336, BF = 217

  BF_indep (narrow x narrow) = 0.226 + 0.805 = +1.031 (log10)

  BF_joint: requires joint MCMC across {CMB-S4, DESI-DR3} with joint
  likelihood. DESI DR3 has NOT YET fired (W1a-5 PENDING-EVENT),
  so BF_joint cannot be computed today.

Substitution chain (Python-verified):

  Step 1: BF_alpha_s (from W1b-3, executed):
          narrow_uniform = 1.682  (plan primary; log10 = +0.226)
          planck_gauss   = 0.989  (min across priors, log10 ~= 0)

  Step 2: BF_w_a formulation:
          framework point w_0_FW = -0.918
          LCDM null       w_0 = -1
          DR3 projected   sigma = 0.025
          L_fw / marg_L_LCDM = BF_w

  Step 3: Independence product: BF_indep = BF_alpha_s x BF_w_a
                                log10(BF_indep) = log10(BF_alpha_s) + log10(BF_w_a)

  Step 4: Independence test: D := |log10(BF_joint) - log10(BF_indep)|
          PASS iff D < 0.30 dex (factor ~2 deviation)
          FAIL iff D > 0.60 dex (factor ~4 deviation)
          INFO iff 0.30 <= D <= 0.60

  Step 5: BF_joint pending DR3 event:
          DR3 window: opens 2026-04-23 (today); data.desi.lbl.gov
          not yet public.
          D cannot be computed today.
          Verdict: PENDING-EVENT (pre-registration complete;
                   verification when DR3 data lands).

  Direction: The gate PRE-REGISTERS the independence product formula.
             When DR3 fires AND a joint MCMC is performed on
             {alpha_s, w_0/w_a} posterior, the deviation D can be
             measured against the 0.30 threshold. For today,
             the deliverable is the frozen formula + SHA-pinned
             pre-registration artifact.

Inputs (SHA-256 dual-pinned at runtime):
  - canonical_constants.py (alpha_s_canon, w0_FW)
  - computations/session-85/s85_w1b_alpha_s_prior_range_lcdm.npz (W1b-3 output)
  - computations/session-85/s85_w0_dr3_regulator_successor_tree.json (W0 successor tree)

Output 4-tuple:
  (value='PENDING-EVENT', scheme=joint-vs-independent-product, convention=log10, L_max=n/a)

Thresholds (plan §W1b-10):
  - PASS iff |log10(BF_joint) - log10(BF_indep)| < 0.30
  - FAIL iff > 0.60
  - INFO iff 0.30 <= D <= 0.60
  - PENDING-EVENT iff BF_joint undefined (DR3 data pending)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "4")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import w0_FW  # noqa: E402 (framework w_0 point)

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
from scipy.stats import norm  # noqa: E402
from scipy.integrate import quad  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

GATE_ID = "S85-W1b-CF-M6-ALPHA-S-W-A-DECOUPLED-JOINT"               # (local)
SCHEME = "joint-vs-independent-product"                             # (local)
CONVENTION = "log10"                                                # (local)
L_MAX_LABEL = "n/a"                                                 # (local)

# DESI DR3 projected sigma(w_0)
SIGMA_W0_DR3 = 0.025                                                # (local, DESI DR3 projected)
W0_LCDM_NULL = -1.0                                                 # (local)

# Narrow uniform LCDM prior on w_0 (analog to W1b-3 narrow uniform)
W0_PRIOR_LO = -1.2                                                  # (local)
W0_PRIOR_HI = -0.8                                                  # (local)

# W1b-3 BF_alpha_s values (from s85_w1b_alpha_s_prior_range_lcdm.npz)
BF_ALPHA_NARROW = 1.682                                             # (local)
BF_ALPHA_WIDE = 4.162                                               # (local)
BF_ALPHA_GAUSS = 0.989                                              # (local)

# Independence thresholds (plan §W1b-10)
PASS_D = 0.30                                                       # (local) factor-2
FAIL_D = 0.60                                                       # (local) factor-4

# Event status
EVENT_DR3_PUBLIC = False                                            # (local) DR3 window opens today; not public yet

OUT_NPZ = SCRIPT_DIR / "s85_w1b_cf_m6_alpha_s_w_a_decoupled_joint.npz"
OUT_PNG = SCRIPT_DIR / "s85_w1b_cf_m6_alpha_s_w_a_decoupled_joint.png"
OUT_JSON = SCRIPT_DIR / "s85_w1b_cf_m6_alpha_s_w_a_decoupled_joint.json"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
W1B3_NPZ = SCRIPT_DIR / "s85_w1b_alpha_s_prior_range_lcdm.npz"
W0_DR3_JSON = SCRIPT_DIR / "s85_w0_dr3_regulator_successor_tree.json"

INPUT_FILES = [CANON_PY]
for p in (W1B3_NPZ, W0_DR3_JSON):
    if p.exists():
        INPUT_FILES.append(p)


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                            # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name                                            # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def compute_BF_w_framework_right(w_fw: float, sigma: float,
                                 prior_lo: float, prior_hi: float) -> dict:
    """Compute BF_w assuming data lands at framework point (hypothetical
    DR3 realization).

    L_fw(w_fw | data=w_fw, sigma) = N(w_fw | w_fw, sigma) = 1/(sigma sqrt(2pi))
    marg_L_LCDM (narrow uniform [lo, hi]) =
       (1/(hi-lo)) * integral_{lo}^{hi} N(w | w_fw, sigma) dw
    BF_w = L_fw / marg_L_LCDM
    """
    L_fw = float(norm.pdf(w_fw, loc=w_fw, scale=sigma))             # (local)
    width = prior_hi - prior_lo                                     # (local)
    margL, _ = quad(lambda w: norm.pdf(w, loc=w_fw, scale=sigma) / width,
                    prior_lo, prior_hi, epsabs=1e-12, epsrel=1e-10)
    BF = L_fw / margL                                               # (local)
    return {
        "L_fw": L_fw,
        "marg_L_LCDM_narrow": margL,
        "BF_w_narrow": BF,
        "log10_BF_w_narrow": float(np.log10(BF)),
    }


def compute() -> dict:
    # BF_alpha_s from W1b-3 (values pinned at script-freeze from NPZ)
    BFa = {
        "narrow_uniform": BF_ALPHA_NARROW,
        "wide_uniform":   BF_ALPHA_WIDE,
        "planck_gauss":   BF_ALPHA_GAUSS,
    }
    log10_BFa = {k: float(np.log10(v)) for k, v in BFa.items()}     # (local)

    # BF_w_a via W1b-3-analog (framework-right data realization, narrow uniform)
    bfw = compute_BF_w_framework_right(
        w_fw=float(w0_FW), sigma=SIGMA_W0_DR3,
        prior_lo=W0_PRIOR_LO, prior_hi=W0_PRIOR_HI,
    )

    # Independence product (using narrow_uniform for both; canonical pair)
    log10_BF_indep_narrow = log10_BFa["narrow_uniform"] + bfw["log10_BF_w_narrow"]
    BF_indep_narrow = 10 ** log10_BF_indep_narrow                   # (local)

    # BF_joint: requires DR3 data + joint MCMC (PENDING-EVENT)
    BF_joint_status = "PENDING-EVENT" if not EVENT_DR3_PUBLIC else "TO-BE-COMPUTED"

    # If we could compute D, it would be |log10(BF_joint) - log10(BF_indep)|
    # Today: D is undefined; pre-reg formula only.

    return {
        "value": "PENDING-EVENT",
        "BF_alpha_s": BFa,
        "log10_BF_alpha_s": log10_BFa,
        "BF_w_narrow": bfw["BF_w_narrow"],
        "log10_BF_w_narrow": bfw["log10_BF_w_narrow"],
        "L_fw_w_0": bfw["L_fw"],
        "marg_L_LCDM_w_narrow": bfw["marg_L_LCDM_narrow"],
        "BF_indep_narrow_x_narrow": BF_indep_narrow,
        "log10_BF_indep_narrow_x_narrow": log10_BF_indep_narrow,
        "BF_joint_status": BF_joint_status,
        "PASS_D": PASS_D,
        "FAIL_D": FAIL_D,
        "w0_FW": float(w0_FW),
        "sigma_w0_DR3": SIGMA_W0_DR3,
        "event_DR3_public": EVENT_DR3_PUBLIC,
    }


def evaluate_gate(res: dict) -> str:
    # BF_joint pending DR3 event => PENDING-EVENT verdict
    if not res["event_DR3_public"]:
        return "PENDING-EVENT"
    # If DR3 data public, compute D (not today)
    return "TO-BE-CLASSIFIED"


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_LABEL} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def write_registration_json(res: dict, audit_sha: str, content_sha: str,
                            out_path: Path) -> None:
    reg = {
        "gate_id": GATE_ID,
        "pre_registration_frozen_at": "2026-04-23",
        "formula": "BF_indep = BF_alpha_s * BF_w_a; test |log10(BF_joint) - log10(BF_indep)| < 0.30",
        "BF_alpha_s": res["BF_alpha_s"],
        "log10_BF_alpha_s": res["log10_BF_alpha_s"],
        "BF_w_a_narrow_uniform": res["BF_w_narrow"],
        "log10_BF_w_a_narrow_uniform": res["log10_BF_w_narrow"],
        "BF_indep_narrow_x_narrow": res["BF_indep_narrow_x_narrow"],
        "log10_BF_indep_narrow_x_narrow": res["log10_BF_indep_narrow_x_narrow"],
        "BF_joint_status": res["BF_joint_status"],
        "detector_classes": {
            "alpha_s_channel": ["CMB-S4", "CMB-HD", "LiteBIRD"],
            "w_a_channel":     ["DESI-DR3", "Euclid", "LSST"],
            "cross_correlation_assumption": "0 (independent sky surveys)",
        },
        "PASS_threshold_D_dex": PASS_D,
        "FAIL_threshold_D_dex": FAIL_D,
        "event_trigger": "DESI DR3 public release (window opened 2026-04-23)",
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }
    out_path.write_text(json.dumps(reg, indent=2), encoding="utf-8")
    print(f"  JSON written: {out_path.name}")


def make_plot(res: dict, out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(9.0, 5.4))                      # (local)
    bars = [
        ("log10 BF_α narrow",   res["log10_BF_alpha_s"]["narrow_uniform"]),
        ("log10 BF_α gauss",    res["log10_BF_alpha_s"]["planck_gauss"]),
        ("log10 BF_w narrow",   res["log10_BF_w_narrow"]),
        ("log10 BF_indep\n(narrow x narrow)", res["log10_BF_indep_narrow_x_narrow"]),
    ]
    labels = [b[0] for b in bars]
    vals = [b[1] for b in bars]
    colors = ["#1a5fb4", "#6690b8", "#b06530", "#2a7a2a"]
    ax.bar(range(len(labels)), vals, color=colors, alpha=0.85)
    ax.set_xticks(range(len(labels))); ax.set_xticklabels(labels, rotation=0, fontsize=9)
    ax.axhline(0, color="k", lw=0.8)
    ax.set_ylabel(r"$\log_{10}(BF)$")
    for i, v in enumerate(vals):
        ax.text(i, v + (0.05 if v >= 0 else -0.12), f"{v:+.3f}",
                ha="center", fontsize=9)
    ax.set_title(f"{GATE_ID}: pre-registration (BF_joint PENDING DR3)")
    ax.grid(True, alpha=0.25, axis="y")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"  PNG written: {out_path.name}")


def main() -> int:
    t0 = time.time()                                                # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                          # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    res = compute()
    verdict = evaluate_gate(res)

    print("=== Substitution chain (Python-verified) ===")
    print(f"  Step 1: BF_alpha_s from W1b-3 output (executed):")
    for k, v in res["BF_alpha_s"].items():
        print(f"          {k:15s}: BF={v:.3f}, log10={res['log10_BF_alpha_s'][k]:+.3f}")
    print(f"  Step 2: BF_w_a via W1b-3-analog (framework-right, narrow uniform prior):")
    print(f"          w_0_FW = {res['w0_FW']}, sigma_DR3 = {res['sigma_w0_DR3']}")
    print(f"          prior width = {W0_PRIOR_HI - W0_PRIOR_LO:.2f}")
    print(f"          L_fw = {res['L_fw_w_0']:.4f}, marg_L_LCDM = {res['marg_L_LCDM_w_narrow']:.4f}")
    print(f"          BF_w = {res['BF_w_narrow']:.3f}, log10 = {res['log10_BF_w_narrow']:+.3f}")
    print(f"  Step 3: BF_indep (narrow x narrow) = BF_alpha_narrow * BF_w_narrow")
    print(f"          log10(BF_indep) = {res['log10_BF_alpha_s']['narrow_uniform']:+.3f} + "
          f"{res['log10_BF_w_narrow']:+.3f} = {res['log10_BF_indep_narrow_x_narrow']:+.3f}")
    print(f"  Step 4: BF_joint status: {res['BF_joint_status']}")
    print(f"          DR3 event public: {res['event_DR3_public']}")
    print(f"  Step 5: D = |log10(BF_joint) - log10(BF_indep)| UNDEFINED (BF_joint pending)")
    print(f"  Step 6: Verdict: {verdict}")
    print()

    np.savez(
        OUT_NPZ,
        BF_alpha_narrow=np.float64(res["BF_alpha_s"]["narrow_uniform"]),
        BF_alpha_wide=np.float64(res["BF_alpha_s"]["wide_uniform"]),
        BF_alpha_gauss=np.float64(res["BF_alpha_s"]["planck_gauss"]),
        BF_w_narrow=np.float64(res["BF_w_narrow"]),
        log10_BF_w_narrow=np.float64(res["log10_BF_w_narrow"]),
        BF_indep_narrow_x_narrow=np.float64(res["BF_indep_narrow_x_narrow"]),
        log10_BF_indep_narrow_x_narrow=np.float64(res["log10_BF_indep_narrow_x_narrow"]),
        event_DR3_public=np.array(res["event_DR3_public"]),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")

    write_registration_json(res, audit_sha, content_sha, OUT_JSON)
    make_plot(res, OUT_PNG)

    tag = emit_4tuple("PENDING-EVENT", SCHEME, CONVENTION, L_MAX_LABEL)
    print(tag)
    append_verdict(verdict, "PENDING-EVENT", audit_sha, content_sha)

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
