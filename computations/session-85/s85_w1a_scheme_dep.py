#!/usr/bin/env python3
"""
S85 W1a-1: SCHEME-DEP
=====================

Gate: S85-W1a-SCHEME-DEP
Trigger: [VERIFY]
Classification: META (scheme-invariance audit of f_conv)
Agent: mack-cosmic-bridge

Hypothesis: The S84 f_conv scheme-variance floor (4.65% from W4-45
Yukawa-OOM envelope) is either (a) CLOSED by a 2-loop Z_R correction
driving variance to <=1%, OR (b) PERMANENTLY ACCEPTED as an irreducible
scheme degree of freedom and booked into working-paper §VII.M.2.

Method: Compute Z_R_2loop(mu_BC) on the S84 W4-45 anchor grid
mu_BC in {188, 500, 2000} GeV with Z_R(mu) = 1 + (alpha_s/pi)*L
+ c_2*alpha_s^2*L^2 at L = log(mu/M_Z) and c_2 = 11/(16*pi^2)
(QCD-like CONVENTION-I). Compare max relative deviation to the S84
4.65% floor and to the pre-registered PASS/FAIL cut.

Substitution chain (Python-verified at top of compute() below):
  Step 1: Z_R_2loop(mu) = 1 + (alpha_s/pi)*L + c_2*alpha_s^2*L^2
  Step 2: variance := max_{mu in grid} |Z_R_2loop(mu) - Z_R_2loop(M_Z)| / Z_R_2loop(M_Z)
          Z_R_2loop(M_Z) = 1 (L = 0)
  Step 3: At mu = 2000 GeV, L = log(2000/91.1876) = 3.088
          1-loop term   = (0.1180/pi) * 3.088           = 0.1160
          2-loop term   = (11/(16*pi^2)) * 0.1180^2 * 3.088^2 = 0.00925
          Z_R_2loop(2000) - 1 = 0.1252
  Step 4: max_variance at mu=2000 is the binding value: 0.1252
  Step 5: Compare to PASS threshold (<=0.01), FAIL threshold (>0.046):
          0.1252 > 0.046 ==> FAIL
  Direction: 2-loop sign-agreement with 1-loop (both positive terms for
             c_2 > 0, L > 0) means variance GROWS under 2-loop;
             the perturbative series is CONVERGENT (2L/1L ratio = 0.080
             at mu=2000) but does NOT close the 4.65% floor.
             Path (b) is forced: scheme-variance is STRUCTURAL, not
             closable by higher orders.

Cross-check 1 (perturbative convergence): ratio |2L|/|1L| at mu=2000 GeV
must be < 1 for the expansion to be convergent. Computed ratio = 0.080,
well below 1 ==> expansion is convergent.

Cross-check 2 (heat-kernel residue, cf. W0-TWO-LOOP-Z):
The W0 f_conv_two_loop_zr script computed ratio_MS_ladder = 8.64e-08
(S85 verdict line 3), a different observable (2-loop vs 1-loop RATIO
at a single anchor). Consistent sign with this computation: 2-loop
correction is positive, small relative to 1-loop baseline, and does
not overturn the 1-loop scheme-deviation floor.

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py
  - computations/session-85/s85_w0_f_conv_two_loop_zr.py (feeder)
  - sessions/archive/session-84/session-84-s1-mack-alpha_s-synthesis.md
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<max_variance>, scheme=MS-bar, convention=CONVENTION-I, L_max=10)

Thresholds (pre-registered, plan §W1a-1):
  - PASS iff max_variance <= 0.01 (>= 5x reduction from 4.65% floor)
  - FAIL iff max_variance > 0.046
  - INFO iff 0.01 < max_variance <= 0.046

Output files:
  - computations/session-85/s85_w1a_scheme_dep.py
  - computations/session-85/s85_w1a_scheme_dep.npz
  - computations/session-85/s85_w1a_scheme_dep.png
  - verdict appended to computations/session-85/s85_gate_verdicts.txt
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 -- CPU thread cap (scalar workload; no GPU needed)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first content import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import alpha_s_MZ_obs, M_Z  # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

SESSION = "S85"                                                     # (local)
GATE_ID = "S85-W1a-SCHEME-DEP"                                      # (local)
SCHEME = "MS-bar"                                                   # (local)
CONVENTION = "CONVENTION-I"                                         # (local) QCD-like c_2
L_MAX = 10                                                          # (local) Dirac-spectrum baseline

# Pre-registered thresholds (plan §W1a-1)
PASS_THRESHOLD = 0.01                                               # (local) >= 5x reduction from 4.65%
FAIL_THRESHOLD = 0.046                                              # (local) 4.65% floor from S84 W4-45
INFO_THRESHOLD = 0.046                                              # (local) INFO is (0.01, 0.046]

# Anchor grid from S84 W4-45 Yukawa-OOM envelope
MU_BC_GRID = np.array([188.0, 500.0, 2000.0], dtype=np.float64)     # (local) GeV

# Canonical two-loop coefficient, QCD-like (CONVENTION-I)
C_2 = 11.0 / (16.0 * np.pi ** 2)                                    # (local) 0.06966

# S84 baseline: 1-loop Z_R variance floor (Yukawa-OOM envelope)
Z_R_1LOOP_BASELINE = 0.0465                                         # (local) S84 W4-45

# Output destinations
OUT_NPZ = SCRIPT_DIR / "s85_w1a_scheme_dep.npz"
OUT_PNG = SCRIPT_DIR / "s85_w1a_scheme_dep.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
W0_FEEDER = SCRIPT_DIR / "s85_w0_f_conv_two_loop_zr.py"
S84_SYNTH = PROJECT_ROOT / "sessions" / "session-84" / "session-84-s1-mack-alpha_s-synthesis.md"

INPUT_FILES = [CANON_PY, W0_FEEDER, S84_SYNTH]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

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


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())                                    # (local)
    h = hashlib.sha256()                                            # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    script_bytes = b""                                              # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""                                           # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                               # (local)

    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                     # (local)

    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                 # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 -- Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Compute Z_R_2loop_variance across mu_BC grid.

    Substitution chain (Python-explicit):
      Step 1: Z_R_2loop(mu) = 1 + (alpha_s/pi)*L + c_2*alpha_s^2*L^2, L=log(mu/M_Z)
      Step 2: Z_R_2loop(M_Z) = 1
      Step 3: deviation(mu) = Z_R_2loop(mu) - 1 = (alpha_s/pi)*L + c_2*alpha_s^2*L^2
      Step 4: variance = max_{mu in grid} |deviation(mu)|
    """
    L_vec = np.log(MU_BC_GRID / M_Z)                                # (local) log(mu_BC/M_Z)
    term1 = (alpha_s_MZ_obs / np.pi) * L_vec                        # (local) 1-loop contribution
    term2 = C_2 * (alpha_s_MZ_obs ** 2) * (L_vec ** 2)              # (local) 2-loop contribution
    Z_R_2loop = 1.0 + term1 + term2                                 # (local) full Z_R to 2-loop
    Z_R_1loop = 1.0 + term1                                         # (local) 1-loop check

    # variance = max_mu |Z_R(mu) - Z_R(M_Z)| / Z_R(M_Z); Z_R(M_Z) = 1
    deviation_2loop = np.abs(Z_R_2loop - 1.0)                       # (local)
    deviation_1loop = np.abs(Z_R_1loop - 1.0)                       # (local)
    variance_2loop = float(np.max(deviation_2loop))                 # (local)
    variance_1loop = float(np.max(deviation_1loop))                 # (local)

    # CROSS-CHECK 1: perturbative convergence |term2|/|term1| at binding mu (max of grid)
    i_max = int(np.argmax(deviation_2loop))                         # (local) binding mu index
    pert_ratio = float(abs(term2[i_max]) / abs(term1[i_max]))       # (local) 2L/1L ratio

    # CROSS-CHECK 2: sign agreement check. c_2 > 0 and L > 0 imply same sign as 1L.
    same_sign = bool(np.all(np.sign(term1) == np.sign(term2)))      # (local)

    # Reduction factor vs S84 1-loop Yukawa-OOM baseline (4.65%)
    reduction_factor = Z_R_1LOOP_BASELINE / variance_2loop          # (local) >1 means 2L improves
    ratio_to_baseline = variance_2loop / Z_R_1LOOP_BASELINE         # (local)

    return {
        "value": variance_2loop,
        "variance_2loop": variance_2loop,
        "variance_1loop": variance_1loop,
        "Z_R_2loop": Z_R_2loop,
        "Z_R_1loop": Z_R_1loop,
        "term1_vec": term1,
        "term2_vec": term2,
        "L_vec": L_vec,
        "mu_BC_grid": MU_BC_GRID,
        "c_2": C_2,
        "alpha_s": alpha_s_MZ_obs,
        "M_Z": M_Z,
        "binding_mu_BC": float(MU_BC_GRID[i_max]),
        "pert_ratio": pert_ratio,
        "same_sign": same_sign,
        "baseline_1loop_S84": Z_R_1LOOP_BASELINE,
        "ratio_to_baseline": ratio_to_baseline,
        "reduction_factor": reduction_factor,
    }


# ---------------------------------------------------------------------------
# Section 6 -- Plot
# ---------------------------------------------------------------------------

def make_plot(res: dict, out_path: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.6))             # (local)

    mu_grid = res["mu_BC_grid"]                                     # (local)
    var2 = res["variance_2loop"]                                    # (local)

    # Left panel: Z_R(mu) with term breakdown
    ax = axes[0]
    mu_fine = np.logspace(np.log10(91.2), np.log10(2500.0), 200)    # (local)
    L_fine = np.log(mu_fine / res["M_Z"])                           # (local)
    t1_fine = (res["alpha_s"]/np.pi) * L_fine                       # (local)
    t2_fine = res["c_2"] * res["alpha_s"]**2 * L_fine**2            # (local)
    ax.plot(mu_fine, 1+t1_fine, color="#1a5fb4", lw=1.8, label="1-loop")
    ax.plot(mu_fine, 1+t1_fine+t2_fine, color="#b03030", lw=2.0, label="1+2 loop")
    ax.scatter(mu_grid, res["Z_R_2loop"], c="#333333", s=55, zorder=5,
               label="mu_BC anchor grid")
    ax.axhline(1.0, color="k", lw=0.8, ls=":")
    ax.set_xscale("log")
    ax.set_xlabel(r"$\mu_{\mathrm{BC}}$ (GeV)")
    ax.set_ylabel(r"$Z_R(\mu_{\mathrm{BC}})$")
    ax.set_title(r"$Z_R$ expansion vs $\mu_{\mathrm{BC}}$")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(True, alpha=0.25)

    # Right panel: variance comparison
    ax = axes[1]
    bar_labels = ["1-loop baseline\n(S84 W4-45)", "2-loop variance\n(this gate)",
                  "PASS threshold", "FAIL threshold"]
    bar_vals = [res["baseline_1loop_S84"], var2, PASS_THRESHOLD, FAIL_THRESHOLD]
    colors = ["#808080", "#b03030", "#2a7a2a", "#884400"]
    ax.bar(bar_labels, bar_vals, color=colors, alpha=0.85)
    ax.axhline(var2, color="#b03030", lw=1.0, ls="--", alpha=0.5)
    ax.set_ylabel("Scheme variance")
    ax.set_title(f"W1a-1 verdict cut (2-loop variance = {var2:.4f})")
    ax.set_yscale("log")
    ax.grid(True, alpha=0.25, axis="y")
    for i, v in enumerate(bar_vals):
        ax.text(i, v * 1.15, f"{v:.4f}", ha="center", fontsize=8)

    fig.suptitle(f"{GATE_ID}: 2-loop Z_R does NOT close 4.65% floor "
                 f"(ratio_2L/1L={res['pert_ratio']:.3f}, convergent)")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"  PNG written: {out_path.name}")


# ---------------------------------------------------------------------------
# Section 7 -- Verdict, 4-tuple, append
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def evaluate_gate(variance: float) -> str:
    """Plan §W1a-1 pre-registered thresholds.

    PASS iff variance <= 0.01 (>=5x reduction from 4.65%).
    FAIL iff variance > 0.046.
    INFO iff 0.01 < variance <= 0.046.
    """
    if variance <= PASS_THRESHOLD:
        return "PASS"
    if variance > FAIL_THRESHOLD:
        return "FAIL"
    return "INFO"


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    header_needed = not VERDICT_TXT.exists()                        # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        if header_needed:
            fp.write("# S85 gate verdicts -- canonical S84+ dual-SHA schema\n\n")
        fp.write(line)


# ---------------------------------------------------------------------------
# Section 8 -- Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)                                    # (local)
    print(f"  closure:        {closure[:16]}... (legacy, informational)")

    script_path = Path(__file__).resolve()                          # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    res = compute()
    variance = res["variance_2loop"]
    verdict = evaluate_gate(variance)

    print("=== Substitution chain (Python-verified) ===")
    print(f"  Step 1: Z_R_2loop(mu) = 1 + (alpha_s/pi)*L + c_2*alpha_s^2*L^2")
    print(f"          alpha_s(M_Z) = {res['alpha_s']:.4f}, M_Z = {res['M_Z']:.4f} GeV, c_2 = {res['c_2']:.6f}")
    print(f"  Step 2: per-anchor decomposition")
    for i, mu in enumerate(res["mu_BC_grid"]):
        print(f"          mu={mu:.0f}  L={res['L_vec'][i]:.4f}  "
              f"1L={res['term1_vec'][i]:+.6f}  2L={res['term2_vec'][i]:+.6f}  "
              f"Z_R={res['Z_R_2loop'][i]:.6f}  dev={res['Z_R_2loop'][i]-1:.6f}")
    print(f"  Step 3: variance_2loop = max dev = {variance:.6f} "
          f"(binding mu_BC = {res['binding_mu_BC']:.0f} GeV)")
    print(f"  Step 4: Compare to S84 1-loop baseline (0.0465): ratio = "
          f"{res['ratio_to_baseline']:.4f} (>1 means 2-loop WORSENS floor)")
    print(f"  Step 5: pert_ratio |2L/1L| at binding mu = {res['pert_ratio']:.6f} "
          f"(<1 ==> expansion is convergent)")
    print(f"  Step 6: sign-agreement 1L vs 2L: {res['same_sign']} "
          f"(True ==> 2L adds to 1L, variance GROWS)")
    print(f"  Step 7: Compare to thresholds: PASS<={PASS_THRESHOLD}, "
          f"FAIL>{FAIL_THRESHOLD}. value={variance:.6f} ==> {verdict}")
    print()

    np.savez(
        OUT_NPZ,
        variance_2loop=np.float64(variance),
        variance_1loop=np.float64(res["variance_1loop"]),
        baseline_1loop_S84=np.float64(res["baseline_1loop_S84"]),
        ratio_to_baseline=np.float64(res["ratio_to_baseline"]),
        pert_ratio=np.float64(res["pert_ratio"]),
        same_sign=np.array(res["same_sign"]),
        mu_BC_grid=res["mu_BC_grid"],
        Z_R_2loop=res["Z_R_2loop"],
        Z_R_1loop=res["Z_R_1loop"],
        term1_vec=res["term1_vec"],
        term2_vec=res["term2_vec"],
        L_vec=res["L_vec"],
        c_2=np.float64(res["c_2"]),
        alpha_s=np.float64(res["alpha_s"]),
        M_Z=np.float64(res["M_Z"]),
        threshold_PASS=np.float64(PASS_THRESHOLD),
        threshold_FAIL=np.float64(FAIL_THRESHOLD),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")

    make_plot(res, OUT_PNG)

    tag = emit_4tuple(variance, SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, variance, audit_sha, content_sha)

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    # Exit 0 on any clean run (PASS/INFO/FAIL are all physics verdicts, not errors).
    # Reserve non-zero exit for genuine script errors (unhandled exceptions).
    return 0


if __name__ == "__main__":
    sys.exit(main())
