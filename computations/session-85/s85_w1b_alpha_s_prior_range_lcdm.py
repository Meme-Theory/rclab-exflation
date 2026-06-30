#!/usr/bin/env python3
"""
S85 W1b-3: ALPHA-S-PRIOR-RANGE-LCDM
====================================

Gate: S85-W1b-ALPHA-S-PRIOR-RANGE-LCDM
Trigger: [AUDIT]
Classification: META (Bayes-factor prior-range formalization)
Agent: mack-cosmic-bridge

Hypothesis: The framework's α_s "BF ≈ 1000 for zero-free-parameter"
claim depends on the LCDM prior range. Gate pre-registers 3 prior
choices (wide uniform, narrow uniform, Planck-2018 Gaussian) and
checks prior-robustness.

Substitution chain (Python-verified):
  Step 1: Framework alpha_s_canon = 0.00117 (S63 RUNNING-NS-63
          inflationary running; zero-parameter prediction).
  Step 2: Planck 2018 TT,TE,EE+lowE+lensing:
            alpha_s_obs = -0.0045, sigma_obs = 0.0067.
  Step 3: L_framework = N(alpha_canon | alpha_obs, sigma_obs)
          = 4.162e+01
  Step 4: Priors (pre-registered at plan-write, FROZEN):
            wide_uniform: U[-0.05, +0.05]
            narrow_uniform: U[-0.02, +0.02]
            planck_gauss: N(mu=-0.0045, sig=0.0067)
  Step 5: marg_L_LCDM(pi) = Integral[ N(alpha | obs, sig_obs) * pi(alpha) ] dalpha
          Uniform:  marg_L = (1/(H-L)) * Integral_{L}^{H} N(...) dalpha
          Gaussian: marg_L = N(alpha_obs | mu_prior, sqrt(sig_prior^2 + sig_obs^2))
  Step 6: BF(pi) = L_fw / marg_L_LCDM(pi)
  Step 7: Computed (Python quad, 1e-14 tolerance):
            wide_uniform  : marg_L=1.000e+01, BF=4.162,  log10BF=+0.619
            narrow_uniform: marg_L=2.474e+01, BF=1.682,  log10BF=+0.226
            planck_gauss  : marg_L=4.210e+01, BF=0.989,  log10BF=-0.005
  Step 8: Compare to plan thresholds (§W1b-3):
            PASS iff BF > 30 for ALL 3 priors (decisive evidence)
            FAIL iff BF < 3 for at least 1 of 3 priors
            INFO iff 3 <= BF <= 30 for any, NOT <3 for any
          Applied: narrow_uniform BF=1.68 < 3 AND planck_gauss BF=0.99 < 3
          ==> FAIL on 2 priors.
  Direction: Wider prior yields LARGER BF (LCDM's marg_L is diluted by
             wider integration window). The framework's "1000:1
             advertisement" requires a WIDE prior window; under tight
             Planck-posterior prior the advantage vanishes. Magnitude
             is monotonic in prior width. The FAIL verdict is an
             honest reflection that zero-parameter framework +
             Planck-centered point sit in the same region of alpha_s
             as a Planck-driven LCDM posterior; BF is small because
             both hypotheses predict the observed region equally well.

Inputs (SHA-256 dual-pinned at runtime):
  - canonical_constants.py (provenance)
  - Planck 2018 alpha_s tuple: inline (-0.0045 +/- 0.0067)

Output 4-tuple:
  (value=<min_BF_across_3_priors>, scheme=marg-L-ratio, convention=flat-model-prior, L_max=n/a)

Thresholds (plan §W1b-3):
  - PASS iff BF > 30 for ALL 3 priors
  - FAIL iff BF < 3 for any prior
  - INFO iff 3 <= BF <= 30 (substantial but sub-decisive)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import *  # noqa: E402, F401, F403

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
from scipy.integrate import quad  # noqa: E402
from scipy.stats import norm  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

GATE_ID = "S85-W1b-ALPHA-S-PRIOR-RANGE-LCDM"                        # (local)
SCHEME = "marg-L-ratio"                                             # (local)
CONVENTION = "flat-model-prior"                                     # (local)
L_MAX_LABEL = "n/a"                                                 # (local)

# Framework prediction (S63 RUNNING-NS-63; zero-free-parameter point)
ALPHA_CANON_FW = 0.00117                                            # (local, S63 canonical inflationary running)

# Planck 2018 TT,TE,EE+lowE+lensing
ALPHA_OBS_PLANCK = -0.0045                                          # (local, Planck 2018)
SIGMA_OBS_PLANCK = 0.0067                                           # (local, Planck 2018 1-sigma)

# 3 pre-registered priors (FROZEN at plan-write)
PRIOR_WIDE_UNIFORM_LO = -0.05                                       # (local)
PRIOR_WIDE_UNIFORM_HI = +0.05                                       # (local)
PRIOR_NARROW_UNIFORM_LO = -0.02                                     # (local)
PRIOR_NARROW_UNIFORM_HI = +0.02                                     # (local)
PRIOR_PLANCK_MU = -0.0045                                           # (local, Planck central)
PRIOR_PLANCK_SIG = 0.0067                                           # (local, Planck 1-sigma)

# Thresholds (plan §W1b-3)
PASS_BF = 30.0                                                      # (local)
FAIL_BF = 3.0                                                       # (local)

OUT_NPZ = SCRIPT_DIR / "s85_w1b_alpha_s_prior_range_lcdm.npz"
OUT_PNG = SCRIPT_DIR / "s85_w1b_alpha_s_prior_range_lcdm.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"

INPUT_FILES = [CANON_PY]


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


def L_framework(alpha_canon: float) -> float:
    """Framework likelihood at its point prediction."""
    return float(norm.pdf(alpha_canon,
                          loc=ALPHA_OBS_PLANCK, scale=SIGMA_OBS_PLANCK))


def marg_L_uniform(L_lo: float, L_hi: float) -> float:
    """Marginal likelihood for LCDM under uniform prior on [L_lo, L_hi]."""
    def integrand(a):                                               # (local)
        return (norm.pdf(a, loc=ALPHA_OBS_PLANCK, scale=SIGMA_OBS_PLANCK)
                / (L_hi - L_lo))
    val, _ = quad(integrand, L_lo, L_hi, epsabs=1e-14, epsrel=1e-12)
    return float(val)


def marg_L_gauss(mu: float, sig: float) -> float:
    """Marginal likelihood for LCDM under Gaussian prior N(mu, sig).

    Convolution of two Gaussians: N(alpha_obs | mu, sqrt(sig_prior^2 + sig_obs^2)).
    """
    sig_eff = float(np.sqrt(sig ** 2 + SIGMA_OBS_PLANCK ** 2))      # (local)
    return float(norm.pdf(ALPHA_OBS_PLANCK, loc=mu, scale=sig_eff))


def compute() -> dict:
    L_fw = L_framework(ALPHA_CANON_FW)                              # (local)

    priors = {
        "wide_uniform":   ("uniform", (PRIOR_WIDE_UNIFORM_LO, PRIOR_WIDE_UNIFORM_HI)),
        "narrow_uniform": ("uniform", (PRIOR_NARROW_UNIFORM_LO, PRIOR_NARROW_UNIFORM_HI)),
        "planck_gauss":   ("gauss",   (PRIOR_PLANCK_MU, PRIOR_PLANCK_SIG)),
    }

    BF_table = {}                                                   # (local)
    for name, (ptype, p) in priors.items():
        if ptype == "uniform":
            margL = marg_L_uniform(*p)
        else:
            margL = marg_L_gauss(*p)
        BF = L_fw / margL                                           # (local)
        BF_table[name] = {
            "marg_L": margL,
            "BF": BF,
            "log10_BF": float(np.log10(BF)) if BF > 0 else float("-inf"),
            "prior_type": ptype,
            "prior_params": p,
        }

    min_BF = min(v["BF"] for v in BF_table.values())                # (local)
    max_BF = max(v["BF"] for v in BF_table.values())                # (local)
    all_pass = all(v["BF"] > PASS_BF for v in BF_table.values())    # (local)
    any_fail = any(v["BF"] < FAIL_BF for v in BF_table.values())    # (local)

    return {
        "value": min_BF,
        "alpha_canon_FW": ALPHA_CANON_FW,
        "alpha_obs_Planck": ALPHA_OBS_PLANCK,
        "sigma_obs_Planck": SIGMA_OBS_PLANCK,
        "L_framework": L_fw,
        "BF_table": BF_table,
        "min_BF": min_BF,
        "max_BF": max_BF,
        "all_pass_threshold": all_pass,
        "any_fail_threshold": any_fail,
    }


def evaluate_gate(res: dict) -> str:
    if res["any_fail_threshold"]:
        return "FAIL"
    if res["all_pass_threshold"]:
        return "PASS"
    return "INFO"


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


def make_plot(res: dict, out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(9.0, 5.4))                      # (local)
    names = list(res["BF_table"].keys())
    BFs = [res["BF_table"][n]["BF"] for n in names]
    colors = ["#1a5fb4", "#b06530", "#b03030"]
    ax.bar(names, BFs, color=colors, alpha=0.85)
    ax.axhline(PASS_BF, color="#2a7a2a", lw=1.4, ls="--",
               label=f"PASS floor (BF > {PASS_BF})")
    ax.axhline(FAIL_BF, color="#b03030", lw=1.4, ls="--",
               label=f"FAIL floor (BF < {FAIL_BF})")
    ax.set_yscale("log")
    ax.set_ylabel(r"$BF_{\rm FW/LCDM}$")
    ax.set_title(f"{GATE_ID}: min(BF)={res['min_BF']:.2f}, max(BF)={res['max_BF']:.2f}")
    for i, v in enumerate(BFs):
        ax.text(i, v * 1.15, f"{v:.2f}", ha="center", fontsize=9)
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(True, alpha=0.25, axis="y", which="both")
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
    print(f"  Step 1: alpha_canon_FW = {res['alpha_canon_FW']} (S63 running)")
    print(f"  Step 2: Planck 2018: alpha_obs = {res['alpha_obs_Planck']} "
          f"+/- {res['sigma_obs_Planck']}")
    print(f"  Step 3: L_framework = {res['L_framework']:.4e}")
    print(f"  Step 4-6: Per-prior BF:")
    for name, row in res["BF_table"].items():
        print(f"          {name:15s}: marg_L={row['marg_L']:.4e}, "
              f"BF={row['BF']:.3f}, log10BF={row['log10_BF']:+.3f}")
    print(f"  Step 7: min(BF) = {res['min_BF']:.3f}, max(BF) = {res['max_BF']:.3f}")
    print(f"  Step 8: Thresholds: PASS if all BF>{PASS_BF}, FAIL if any BF<{FAIL_BF}")
    print(f"          all_pass={res['all_pass_threshold']}, "
          f"any_fail={res['any_fail_threshold']} ==> {verdict}")
    print()

    np.savez(
        OUT_NPZ,
        alpha_canon_FW=np.float64(res["alpha_canon_FW"]),
        alpha_obs_Planck=np.float64(res["alpha_obs_Planck"]),
        sigma_obs_Planck=np.float64(res["sigma_obs_Planck"]),
        L_framework=np.float64(res["L_framework"]),
        BF_wide_uniform=np.float64(res["BF_table"]["wide_uniform"]["BF"]),
        BF_narrow_uniform=np.float64(res["BF_table"]["narrow_uniform"]["BF"]),
        BF_planck_gauss=np.float64(res["BF_table"]["planck_gauss"]["BF"]),
        min_BF=np.float64(res["min_BF"]),
        max_BF=np.float64(res["max_BF"]),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")

    make_plot(res, OUT_PNG)

    tag = emit_4tuple(res["min_BF"], SCHEME, CONVENTION, L_MAX_LABEL)
    print(tag)
    append_verdict(verdict, res["min_BF"], audit_sha, content_sha)

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
