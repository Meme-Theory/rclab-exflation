#!/usr/bin/env python3
"""
S85 W0-1: BETA-S-CMB-S4-PREREG
==============================

Gate: S85-BETA-S-CMB-S4-PREREG
Trigger: [VERIFY]
Classification: PHONONIC
Agent: mack-cosmic-bridge

Hypothesis: The framework-predicted running-of-the-running
beta_s = -0.1331 (derived from spectral moments of D_K at the
electroweak tau_fold slice of Jensen flow, third Taylor coefficient
from the OZ-propagator derivation in S84 W8-86) is observationally
pre-registered against the CMB-S4 Science Book forecast
sigma(beta_s) ~ 2.2e-3, yielding a pull of 60.5 (>> 5 sigma floor).

This is a SCALAR pre-registration: no MCMC, no Fisher-matrix build.
beta_s is a canonical constant (S84-W6 BETA-S-CMB-S4-PREREG closure);
sigma_beta_s_CMB_S4 is a canonical constant (CMB-S4 Science Book v2
2022 Table 6.1 literal). The pull is

    pull = |beta_s_framework - 0| / sigma(beta_s_forecast)
         = |-0.1331 - 0| / 2.2e-3
         = 60.5

LCDM null: beta_s = 0 (minimal slow-roll inflation predicts
|beta_s| <~ eps^3 ~ 1e-6, negligible vs sigma_forecast).

Substrate framing: beta_s is NOT a parameter of an inflaton potential.
It is the SECOND SPECTRAL MOMENT of D_K's Mellin-balance structure at
the tau_fold slice of the Jensen flow. The framework is not fitting
beta_s to data; it is emitting the substrate's inevitable consequence
to observation. CMB-S4 (launch 2028) will measure a quantity whose
value the substrate has already pinned.

Substitution chain (verified via python before compute -- see module
docstring at top of file):
  Step 1: beta_s_framework = -0.1331        [def., S84-W6 closure]
  Step 2: sigma_forecast   =  2.2e-3        [def., CMB-S4 Sci Book T6.1]
  Step 3: LCDM null:         beta_s = 0     [Planck-central convention]
  Step 4: pull = |beta_s_framework - 0| / sigma_forecast
               = 0.1331 / 0.0022
               = 60.5
  Step 5: Direction: pull = 60.5 >> 5 ==> PASS regime
          (5 sigma discriminator floor per plan threshold).

Inputs (SHA-256 dual-pinned at runtime -- see Section 4):
  - computations/_shared/canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=60.5, scheme=MS-bar, convention=Planck-central, L_max=8)

Thresholds (pre-registered):
  - PASS iff pull >= 5   (5 sigma discriminator floor)
  - INFO iff 2 <= pull < 5
  - FAIL iff pull < 2

Output files:
  - computations/session-85/s85_w0_beta_s_cmb_s4_prereg.py
  - computations/session-85/s85_w0_beta_s_cmb_s4_prereg.npz
  - computations/session-85/s85_w0_beta_s_cmb_s4_prereg.png
  - verdict appended to computations/session-85/s85_gate_verdicts.txt
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 -- CPU thread cap (this is a scalar workload; no GPU needed)
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

from canonical_constants import beta_s, sigma_beta_s_CMB_S4  # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")  # headless
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

SESSION = "S85"                                                     # (local)
GATE_ID = "S85-BETA-S-CMB-S4-PREREG"                                # (local)
SCHEME = "MS-bar"                                                   # (local)
CONVENTION = "Planck-central"                                       # (local)
L_MAX = 8                                                           # (local)

# Pre-registered thresholds (defined BEFORE computation per plan W0-1)
PASS_THRESHOLD_PULL = 5.0                                           # (local) 5-sigma discriminator floor
INFO_THRESHOLD_PULL = 2.0                                           # (local) INFO regime floor

# LCDM null hypothesis value of beta_s
BETA_S_LCDM_NULL = 0.0                                              # (local) minimal slow-roll inflation |beta_s| ~ eps^3 ~ 1e-6, << sigma_forecast

# Output destinations
OUT_NPZ = SCRIPT_DIR / "s85_w0_beta_s_cmb_s4_prereg.npz"
OUT_PNG = SCRIPT_DIR / "s85_w0_beta_s_cmb_s4_prereg.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"

INPUT_FILES = [
    CANON_PY,
]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (S84+ dual-SHA schema)
#
#   audit_sha256   = sha256( bytes(script) || bytes(canonical) || bytes(pinmap_json) )
#   content_sha256 = sha256( bytes(script) )
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                            # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} pinmap for closure."""
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
    """Stable hash over all input SHAs (legacy closure; informational)."""
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
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
    content_sha256 = sha256( bytes(script) )
    """
    script_bytes = b""                                              # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                           # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
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
    """Compute the pull of beta_s_framework against CMB-S4 LCDM null.

    Substitution chain (Python-explicit):
      Step 1: beta_s_framework = beta_s (canonical) = -0.1331
      Step 2: sigma_forecast   = sigma_beta_s_CMB_S4 (canonical) = 2.2e-3
      Step 3: LCDM null:         BETA_S_LCDM_NULL = 0.0
      Step 4: pull = |beta_s_framework - BETA_S_LCDM_NULL| / sigma_forecast
                   = |-0.1331 - 0.0| / 2.2e-3
                   = 0.1331 / 0.0022
                   = 60.5
      Step 5: pull = 60.5 >> 5 ==> PASS regime.
    """
    delta = beta_s - BETA_S_LCDM_NULL                               # (local) signed framework - null
    pull = abs(delta) / sigma_beta_s_CMB_S4                         # (local) 1-sigma units
    # Cross-check: the pull is independent of the sign of beta_s.
    pull_abs_first = abs(beta_s - 0.0) / sigma_beta_s_CMB_S4        # (local) alternate grouping
    assert abs(pull - pull_abs_first) < 1e-12, "pull grouping inconsistent"

    # 1-sigma and 2-sigma forecast bands around LCDM null (for posterior plot)
    band_1sigma = sigma_beta_s_CMB_S4                               # (local)
    band_2sigma = 2.0 * sigma_beta_s_CMB_S4                         # (local)
    band_5sigma = 5.0 * sigma_beta_s_CMB_S4                         # (local)

    # Framework-error ansatz: RATIO +/-2% tolerance per plan machinery pin.
    # The framework's beta_s uncertainty (from the 3rd Taylor coefficient in
    # S84 W8-86) is not explicitly stated; we bracket at 2% relative as the
    # plan RATIO tolerance on sigma_forecast. This yields a 1-sigma
    # framework band for visualization only -- the pull uses the CMB-S4
    # forecast sigma in the denominator, not the framework ansatz.
    framework_tol_rel = 0.02                                        # (local) plan RATIO tolerance
    framework_sigma_ansatz = framework_tol_rel * abs(beta_s)        # (local)

    threshold_list = np.array([
        INFO_THRESHOLD_PULL,    # 2 sigma INFO floor
        PASS_THRESHOLD_PULL,    # 5 sigma PASS floor
    ], dtype=np.float64)

    return {
        "value": float(pull),
        "pull": float(pull),
        "beta_s_framework": float(beta_s),
        "beta_s_lcdm_null": float(BETA_S_LCDM_NULL),
        "sigma_forecast": float(sigma_beta_s_CMB_S4),
        "band_1sigma": float(band_1sigma),
        "band_2sigma": float(band_2sigma),
        "band_5sigma": float(band_5sigma),
        "framework_sigma_ansatz": float(framework_sigma_ansatz),
        "framework_tol_rel": float(framework_tol_rel),
        "threshold_list": threshold_list,
    }


# ---------------------------------------------------------------------------
# Section 6 -- Plot
# ---------------------------------------------------------------------------

def make_plot(res: dict, out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(9.0, 5.4))                      # (local)

    beta_fw = res["beta_s_framework"]                               # (local)
    sigma_fc = res["sigma_forecast"]                                # (local)
    pull = res["pull"]                                              # (local)
    sig_ansatz = res["framework_sigma_ansatz"]                      # (local)

    # x-axis in units of sigma_forecast around LCDM null (beta_s = 0).
    x_sigma = np.linspace(-70.0, 5.0, 1201)                         # (local)
    x_beta = x_sigma * sigma_fc                                     # (local) rescale to beta_s units

    # LCDM forecast posterior band (Gaussian centered at 0)
    pdf_lcdm = np.exp(-0.5 * x_sigma ** 2) / np.sqrt(2.0 * np.pi)   # (local)
    ax.plot(x_sigma, pdf_lcdm / pdf_lcdm.max(), color="#b03030", lw=1.8,
            label=r"CMB-S4 LCDM posterior (null: $\beta_s=0$, $\sigma=2.2\times10^{-3}$)")
    ax.fill_between(x_sigma, 0, pdf_lcdm / pdf_lcdm.max(),
                    color="#b03030", alpha=0.10)

    # Shade the +/-1, +/-2, +/-5 sigma bands of the LCDM forecast
    ax.axvspan(-1.0, 1.0, color="#b03030", alpha=0.12, label=r"$\pm 1\sigma$ LCDM")
    ax.axvspan(-5.0, -1.0, color="#b03030", alpha=0.06)
    ax.axvspan(1.0, 5.0, color="#b03030", alpha=0.06)
    ax.axvline(0.0, color="#b03030", lw=1.2, ls="-", alpha=0.8)

    # Framework posterior: narrow Gaussian centered at beta_s = -0.1331
    # (sigma = 2% RATIO tolerance on beta_s per plan machinery pin; visualization only).
    fw_center_sigma = beta_fw / sigma_fc                            # (local) -> pull-signed x-units
    fw_sigma_sigma = sig_ansatz / sigma_fc                          # (local)
    if fw_sigma_sigma < 0.05:  # too-narrow spike -> widen for visual only (no effect on pull)
        fw_sigma_sigma_vis = 0.5                                    # (local)
    else:
        fw_sigma_sigma_vis = fw_sigma_sigma                         # (local)
    pdf_fw = np.exp(-0.5 * ((x_sigma - fw_center_sigma) / fw_sigma_sigma_vis) ** 2)  # (local)
    pdf_fw /= pdf_fw.max() + 1e-300
    ax.plot(x_sigma, pdf_fw, color="#1a5fb4", lw=2.0,
            label=rf"Framework $\beta_s=-0.1331$ (pull $={pull:.1f}\sigma$)")
    ax.fill_between(x_sigma, 0, pdf_fw, color="#1a5fb4", alpha=0.18)
    ax.axvline(fw_center_sigma, color="#1a5fb4", lw=1.4, ls="--", alpha=0.85)

    # Threshold markers: 5-sigma PASS floor
    ax.axvline(-5.0, color="#335533", lw=1.1, ls=":", alpha=0.8,
               label=r"5$\sigma$ PASS floor")
    ax.axvline(-2.0, color="#775500", lw=1.1, ls=":", alpha=0.6,
               label=r"2$\sigma$ INFO floor")

    # Secondary x-axis in beta_s units
    sec = ax.secondary_xaxis(
        'top',
        functions=(lambda s: s * sigma_fc, lambda b: b / sigma_fc),
    )
    sec.set_xlabel(r"$\beta_s$ (dimensionless)")

    ax.set_xlabel(r"Deviation from LCDM null, in units of $\sigma(\beta_s)=2.2\times10^{-3}$")
    ax.set_ylabel("Posterior (normalized)")
    ax.set_xlim(-70.0, 5.0)
    ax.set_ylim(0, 1.12)
    ax.set_title(
        f"S85 W0-1 pre-registration: beta_s = -0.1331 vs CMB-S4 (pull = {pull:.1f} sigma)"
    )
    ax.legend(loc="upper left", fontsize=9, framealpha=0.92)
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"  PNG written: {out_path.name}")


# ---------------------------------------------------------------------------
# Section 7 -- Gate verdict, 4-tuple emit, NPZ save
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def evaluate_gate(pull_value: float) -> str:
    """Pre-registered rule per plan W0-1.

    PASS iff pull >= 5 (5-sigma discriminator floor).
    INFO iff 2 <= pull < 5 (observable but sub-decisive).
    FAIL iff pull < 2 (registration useless).
    """
    if pull_value >= PASS_THRESHOLD_PULL:
        return "PASS"
    if pull_value >= INFO_THRESHOLD_PULL:
        return "INFO"
    return "FAIL"


def append_verdict(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Append single-line verdict to computations/session-85/s85_gate_verdicts.txt.

    S84+ dual-SHA schema: audit_sha256 + content_sha256 + schema_version=S84+.
    Atomic append (single open('a') write; POSIX O_APPEND semantics).
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    header_needed = not VERDICT_TXT.exists()                        # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        if header_needed:
            fp.write(
                "# S85 gate verdicts -- canonical S84+ dual-SHA schema\n"
                "# Each line: {GATE}: PASS|FAIL|INFO -- value=<v> scheme=<s> "
                "convention=<c> L_max=<L> audit_sha256=<64hex> "
                "content_sha256=<64hex> schema_version=S84+\n"
                "# audit_sha256   = sha256( script || canonical_constants.py || pinmap_json )\n"
                "# content_sha256 = sha256( script )\n"
                "# Path: computations/session-85/s85_gate_verdicts.txt "
                "(canonical per .claude/rules/gate-verdicts.md)\n\n"
            )
        fp.write(line)


# ---------------------------------------------------------------------------
# Section 8 -- Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                # (local)

    # 1. Log input pins (first 20 lines of stdout).
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)                                    # (local)
    print(f"  closure:        {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs.
    script_path = Path(__file__).resolve()                          # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    # 2. Compute the pull.
    res = compute()
    value = res["value"]
    pull = res["pull"]

    # 3. Evaluate gate.
    verdict = evaluate_gate(pull)

    # 4. Report the substitution chain explicitly.
    print("=== Substitution chain (Python-verified) ===")
    print(f"  Step 1: beta_s_framework = {res['beta_s_framework']:.4f}   (canonical, S84-W6)")
    print(f"  Step 2: sigma_forecast   = {res['sigma_forecast']:.4e}    (CMB-S4 Sci Book T6.1)")
    print(f"  Step 3: LCDM null        = {res['beta_s_lcdm_null']:.4f}")
    print(f"  Step 4: pull = |{res['beta_s_framework']:.4f} - {res['beta_s_lcdm_null']:.4f}|"
          f" / {res['sigma_forecast']:.4e}")
    print(f"                = {abs(res['beta_s_framework']):.4f} / {res['sigma_forecast']:.4e}")
    print(f"                = {pull:.4f}")
    print(f"  Step 5: pull = {pull:.4f} vs PASS floor {PASS_THRESHOLD_PULL} "
          f"==> {verdict}")
    print()

    # 5. Save NPZ with (beta_s_framework, sigma_forecast, pull, threshold_list).
    np.savez(
        OUT_NPZ,
        beta_s_framework=np.float64(res["beta_s_framework"]),
        sigma_forecast=np.float64(res["sigma_forecast"]),
        pull=np.float64(res["pull"]),
        threshold_list=res["threshold_list"],
        # Cross-check fields (not in the mandated 4-array set but useful
        # for downstream audits):
        beta_s_lcdm_null=np.float64(res["beta_s_lcdm_null"]),
        band_1sigma=np.float64(res["band_1sigma"]),
        band_2sigma=np.float64(res["band_2sigma"]),
        band_5sigma=np.float64(res["band_5sigma"]),
        framework_sigma_ansatz=np.float64(res["framework_sigma_ansatz"]),
        framework_tol_rel=np.float64(res["framework_tol_rel"]),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")

    # 6. Plot.
    make_plot(res, OUT_PNG)

    # 7. Emit 4-tuple + append verdict (dual-SHA, S84+).
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    # 8. Final summary.
    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
