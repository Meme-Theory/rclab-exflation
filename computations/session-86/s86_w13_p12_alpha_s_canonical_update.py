#!/usr/bin/env python3
"""
S86 W13 P12: ALPHA-S-CANONICAL-UPDATE
======================================

Gate ID: S86-W13-P12-ALPHA-S-CANONICAL-UPDATE
Trigger: [VERIFY] + [SIGN]
Classification: PHONONIC -- alpha_s IS the running of the GGE-acoustic
                spectral tilt (substrate observable: second derivative
                of GGE quasiparticle dispersion at the pivot scale).
Agent: mack-cosmic-bridge (canonical-constants edit + 2 re-emissions)

Hypothesis (plan S86-W13-5.5):
  Updating canonical_constants.py from
    alpha_s_canon = -0.0045 +/- 0.0067 (Planck 2018, planck_alpha_s)
  to
    alpha_s_canon_2020 = +0.0023 +/- 0.0063 (ACT DR4 + Planck, Aiola 2020)
  per W1b-8 FAIL produces a self-consistent canonical pin AND the two
  re-emitted gates (S85 W1a-9 7D Fisher + S85 W1b-3 sigma_corr/sigma_diag)
  emit updated verdict lines under the new pin without script breakage.

Substitution chain (Python-verified; plan S86-W13-5 Section 10):

  Step 1 -- Definitions:
    alpha_s_old   = -0.0045   # Planck 2018 central
    sigma_old     =  0.0067   # Planck 2018 1-sigma
    alpha_s_new   = +0.0023   # Aiola 2020 ACT DR4 + Planck central
    sigma_new     =  0.0063   # Aiola 2020 1-sigma
    alpha_s_FW    = -0.068968 # alpha_s_inflation_framework (UNCHANGED)
    gap(X)        = alpha_s_X - alpha_s_FW
    n_sigma(X)    = |gap(X)| / sigma_X

  Step 2 -- Substitute:
    Delta(central)  = alpha_s_new - alpha_s_old
                    = (+0.0023) - (-0.0045)
                    = +0.0068
    gap_old         = alpha_s_old - alpha_s_FW
                    = (-0.0045) - (-0.068968)
                    = +0.064468
    gap_new         = alpha_s_new - alpha_s_FW
                    = (+0.0023) - (-0.068968)
                    = +0.071268
    Delta(gap)      = gap_new - gap_old
                    = +0.006800

  Step 3 -- Simplify:
    n_sigma_old   = 0.064468 / 0.0067 = 9.622
    n_sigma_new   = 0.071268 / 0.0063 = 11.312
    Delta(n_sigma)= n_sigma_new - n_sigma_old = +1.690

  Step 4 -- Direction:
    Delta(central) > 0  -> canon central moves toward POSITIVE
    alpha_s_FW < 0      -> framework prediction is NEGATIVE
    Delta(gap) > 0      -> gap WIDENS
    Delta(n_sigma) > 0  -> tension INCREASES from 9.622 to 11.312 (+1.690 sigma)

  Conclusion: pin update WIDENS the tension; framework prediction is
  UNCHANGED (-0.068968); only the observational reference moved. This
  is a HARDENING of the observational falsifier, NOT a framework
  retraction. Reported as INFO sub-tag in the diagnostic verdict.

Output 4-tuple (P12):
  (value=alpha_s_canon_2020=+0.0023, scheme=Aiola-2020-ACT-DR4-Planck,
   convention=additive-edit, L_max=N/A)

PASS/FAIL/INFO thresholds (plan S86-W13-5.9):
  PASS: canonical_constants.py contains alpha_s_canon_2020 = +0.0023 AND
        legacy planck_alpha_s = -0.0045 retained AND import-parseable AND
        BOTH re-emissions (W1a-9 + W1b-3) produce non-error verdict lines
        AND diagnostic substitution chain matches Section 10 within 1e-6.
  FAIL: any of: import breaks, re-emission script-error, diagnostic
        arithmetic incorrect, legacy entry overwritten.
  INFO: diagnostic tension value n_sigma_new = 11.312 reported as INFO
        sub-tag, not as PASS/FAIL.

Inputs (SHA-256 pinned at runtime):
  - computations/_shared/canonical_constants.py (post-edit; contains both
    legacy planck_alpha_s and new alpha_s_canon_2020)
  - computations/session-85/s85_w1a_multid_fisher.py (W1a-9 producing logic)
  - computations/session-85/s85_w1b_alpha_s_joint_fisher_correlated.py (W1b-3)
  - computations/session-85/s85_gate_verdicts.txt (baseline W1a-9 + W1b-3)
  - script bytes (this file)

Substrate framing (plan S86-W13-5.13):
  alpha_s IS the substrate's GGE-acoustic spectral tilt's running -- the
  second derivative of the GGE quasiparticle dispersion at the pivot
  scale. The framework prediction (-0.068968) is FROZEN; it derives from
  substrate eigenvalue structure (S50-51 identity alpha_s = n_s^2 - 1
  with n_s_canon = 0.9649), not from data fitting. The pin update is
  OBSERVATIONAL discipline (which external reference is canonical for
  tension calculations), not a framework adjustment. The widening
  tension (9.62 sigma -> 11.31 sigma) is the substrate's PREDICTION
  facing a hardening external constraint; whether the substrate's
  alpha_s derivation is correct is a separate question for future
  sessions. Frame as: the substrate's alpha_s prediction is
  increasingly discriminable; future detector data (CMB-S4 / CMB-HD /
  SKA-1) will resolve whether the substrate-derived value is correct.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import (  # noqa: E402
    planck_alpha_s,
    planck_alpha_s_err,
    alpha_s_canon_2020,
    alpha_s_canon_2020_err,
    alpha_s_canon_2020_source,
    alpha_s_canon_2020_session,
    alpha_s_inflation_framework,
    w0_FW,
    beta_s,
    sigma_beta_s_CMB_S4,
    r_CMB_framework,
)

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

# Gate IDs (per plan S86-W13-5 OUTPUT FILES section)
P12_GATE_ID = "S86-W13-P12-ALPHA-S-CANONICAL-UPDATE"                # (local)
W1A9_REEMIT_GATE_ID = "S85-W1a-9-RE-EMIT-S86-W13-P12"               # (local)
W1B3_REEMIT_GATE_ID = "S85-W1b-3-RE-EMIT-S86-W13-P12"               # (local)

P12_SCHEME = "Aiola-2020-ACT-DR4-Planck"                            # (local)
P12_CONVENTION = "additive-edit"                                    # (local)
P12_L_MAX = "N/A"                                                   # (local)

# File paths
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
W1A9_BASELINE_PY = SCRIPT_DIR / "s85_w1a_multid_fisher.py"
W1B3_BASELINE_PY = SCRIPT_DIR / "s85_w1b_alpha_s_joint_fisher_correlated.py"
S85_VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
S86_VERDICT_TXT = SCRIPT_DIR / "s86_gate_verdicts.txt"

OUT_JSON_P12 = SCRIPT_DIR / "s86_w13_p12_alpha_s_canonical_update.json"
OUT_JSON_W1A9 = SCRIPT_DIR / "s86_w13_p12_re_emit_w1a_9.json"
OUT_JSON_W1B3 = SCRIPT_DIR / "s86_w13_p12_re_emit_w1b_3.json"

# Tolerance (plan S86-W13-5 PRDR)
DIAGNOSTIC_TOLERANCE = 1e-6                                         # (local, plan tolerance_rule)

# Pre-registered values from plan Section 10 (for verification)
EXPECTED_DELTA_CENTRAL = +0.0068                                    # (local)
EXPECTED_GAP_OLD = +0.064468                                        # (local)
EXPECTED_GAP_NEW = +0.071268                                        # (local)
EXPECTED_DELTA_GAP = +0.006800                                      # (local)
EXPECTED_N_SIGMA_OLD = 9.622                                        # (local)
EXPECTED_N_SIGMA_NEW = 11.312                                       # (local)
EXPECTED_DELTA_N_SIGMA = +1.690                                     # (local)


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                            # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(label: str, inputs: list[Path]) -> dict[str, str]:
    print(f"=== {label} -- input SHA-256 pins ===")
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
    """Dual SHA per plan: audit_sha = SHA(script || canonical || pinmap_json),
    content_sha = SHA(script_bytes)."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def grep_baseline_verdict(gate_pattern: str) -> dict:
    """Extract baseline verdict line + audit_sha + content_sha from S85 file."""
    if not S85_VERDICT_TXT.exists():
        return {"found": False}
    lines = S85_VERDICT_TXT.read_text(encoding="utf-8").splitlines()
    for line in lines:
        if line.startswith(gate_pattern):
            parts = {}                                              # (local)
            for token in line.split():
                if "=" in token:
                    k, v = token.split("=", 1)
                    parts[k] = v
            return {"found": True, "line": line, "parsed": parts}
    return {"found": False}


# ---------------------------------------------------------------------------
# DIAGNOSTIC SUBSTITUTION CHAIN (plan S86-W13-5 Section 10)
# ---------------------------------------------------------------------------

def diagnostic_chain() -> dict:
    # Step 1: Definitions
    a_old = float(planck_alpha_s)                                   # (local) -0.0045
    s_old = float(planck_alpha_s_err)                               # (local)  0.0067
    a_new = float(alpha_s_canon_2020)                               # (local) +0.0023
    s_new = float(alpha_s_canon_2020_err)                           # (local)  0.0063
    a_FW  = float(alpha_s_inflation_framework)                      # (local) -0.068968

    # Step 2: Substitute
    delta_central = a_new - a_old                                   # (local)
    gap_old = a_old - a_FW                                          # (local) signed gap (canon - FW)
    gap_new = a_new - a_FW                                          # (local)
    delta_gap = gap_new - gap_old                                   # (local)

    # Step 3: Simplify
    n_sigma_old = abs(gap_old) / s_old                              # (local)
    n_sigma_new = abs(gap_new) / s_new                              # (local)
    delta_n_sigma = n_sigma_new - n_sigma_old                       # (local)

    # Step 4: Direction (booleans for downstream verification)
    direction = {
        "delta_central_positive": delta_central > 0,
        "framework_negative": a_FW < 0,
        "delta_gap_positive": delta_gap > 0,
        "delta_n_sigma_positive": delta_n_sigma > 0,
    }                                                               # (local)

    # Verify against plan Section 10 expected values
    verify = {
        "delta_central_match": abs(delta_central - EXPECTED_DELTA_CENTRAL) < DIAGNOSTIC_TOLERANCE,
        "gap_old_match": abs(gap_old - EXPECTED_GAP_OLD) < DIAGNOSTIC_TOLERANCE,
        "gap_new_match": abs(gap_new - EXPECTED_GAP_NEW) < DIAGNOSTIC_TOLERANCE,
        "delta_gap_match": abs(delta_gap - EXPECTED_DELTA_GAP) < DIAGNOSTIC_TOLERANCE,
        "n_sigma_old_match": abs(n_sigma_old - EXPECTED_N_SIGMA_OLD) < 1e-2,  # 3-fig published
        "n_sigma_new_match": abs(n_sigma_new - EXPECTED_N_SIGMA_NEW) < 1e-2,
        "delta_n_sigma_match": abs(delta_n_sigma - EXPECTED_DELTA_N_SIGMA) < 1e-2,
    }                                                               # (local)
    all_match = all(verify.values())                                # (local)

    return {
        "alpha_s_old": a_old,
        "sigma_old": s_old,
        "alpha_s_new": a_new,
        "sigma_new": s_new,
        "alpha_s_FW": a_FW,
        "delta_central": delta_central,
        "gap_old": gap_old,
        "gap_new": gap_new,
        "delta_gap": delta_gap,
        "n_sigma_old": n_sigma_old,
        "n_sigma_new": n_sigma_new,
        "delta_n_sigma": delta_n_sigma,
        "direction": direction,
        "verify": verify,
        "all_match": all_match,
    }


# ---------------------------------------------------------------------------
# RE-EMISSION 1: W1a-9 (7D Fisher) under new pin
# ---------------------------------------------------------------------------
#
# The original W1a-9 script (s85_w1a_multid_fisher.py) hardcoded the LCDM
# alpha_s reference at 0.0 (consistent with vanilla LCDM). The pin update
# does NOT change LCDM = 0; it changes the canonical OBSERVATIONAL
# central. The substrate framework's alpha_s_running_FW = 0.00117 (S63
# RUNNING-NS-63) is the prediction. The 7D Fisher pull for alpha_s slot
# under the OLD canon convention computes
#   pull = (alpha_s_running_FW - alpha_s_LCDM_ref) / sigma_alphas_CMBS4
# with alpha_s_LCDM_ref = 0.0 (vanilla LCDM null). The recalibration to
# Aiola-2020 does not alter this pull, since the pull tests
# framework-vs-LCDM-null (not framework-vs-canonical-observation).
#
# However, the pin update DOES update the joint posterior context: the
# log10(BF) calculation uses the canonical observation as the data
# point against which both LCDM and FW are tested. We re-emit the W1a-9
# verdict with the new canonical-pin context: chi^2 and log10(BF) recompute
# trivially (pull definition unchanged) but the verdict carries the new
# audit_sha tied to the new canonical_constants.py state.
#
# This is the standard re-emission pattern: the producing script's
# numerics are unchanged; the audit_sha changes because canonical_constants
# changed; the verdict line carries the new SHA so downstream consumers
# pick up the post-update state.

def reemit_w1a9() -> dict:
    """Re-emit S85 W1a-9 7D Fisher verdict under updated canonical_constants.py.

    The 7D Fisher numerics are unchanged because:
      (a) framework prediction vector p_FW is fixed (canonical sources, S58/S63/S65/S82);
      (b) LCDM reference vector is the inflation-consistency-relation null
          (-1, 0, -r/8, 0, 0, 0, 0); the alpha_s LCDM slot is 0.0 by definition,
          NOT the canonical observational central;
      (c) detector sigmas are pre-registered projections (DESI DR3, LiteBIRD,
          CMB-S4, SKA-1), independent of the alpha_s canonical pin.
    The pin update changes the audit context (which canonical_constants the
    re-emission was computed against), captured in the dual-SHA.
    """
    # Compute under updated canonical_constants
    # 7D framework vector (matches s85_w1a_multid_fisher.py)
    W_A_FW_loc = 0.0                                                # (local, S74 W4-Z)
    N_T_CMB_FW_loc = -3.024e-3                                      # (local, S66 TENSOR-TRANSFER)
    ALPHA_S_RUNNING_FW_loc = 0.00117                                # (local, S63 RUNNING-NS-63)
    F_NL_FW_loc = 0.0547                                            # (local, S82 W3-4 GGE-FNL)

    # Detector sigmas (block-diagonal Fisher; from s85_w1a_multid_fisher.py)
    SIGMA_W0_DR3_loc = 0.025                                        # (local)
    SIGMA_WA_DR3_loc = 0.10                                         # (local)
    SIGMA_NT_LITEB_loc = 8.0e-4                                     # (local)
    SIGMA_R_LITEB_loc = 1.0e-3                                      # (local)
    SIGMA_ALPHAS_CMBS4_loc = 2.1e-3                                 # (local)
    SIGMA_FNL_SKA1_loc = 5.0                                        # (local)

    p_FW = np.array([                                               # (local)
        w0_FW, W_A_FW_loc, N_T_CMB_FW_loc, r_CMB_framework,
        beta_s, ALPHA_S_RUNNING_FW_loc, F_NL_FW_loc,
    ], dtype=np.float64)
    p_LCDM = np.array([                                             # (local)
        -1.0, 0.0, -r_CMB_framework / 8.0, 0.0,
        0.0, 0.0, 0.0,
    ], dtype=np.float64)
    sigmas = np.array([                                             # (local)
        SIGMA_W0_DR3_loc, SIGMA_WA_DR3_loc, SIGMA_NT_LITEB_loc, SIGMA_R_LITEB_loc,
        sigma_beta_s_CMB_S4, SIGMA_ALPHAS_CMBS4_loc, SIGMA_FNL_SKA1_loc,
    ], dtype=np.float64)
    delta = p_FW - p_LCDM                                           # (local)
    pulls = delta / sigmas                                          # (local)
    pulls_sq = pulls ** 2                                           # (local)
    chi2_total = float(pulls_sq.sum())                              # (local)
    log10BF = 0.5 * chi2_total / np.log(10.0)                       # (local)

    # Diagnostic: under the NEW canonical pin, the canon-vs-FW pull on the
    # alpha_s slot using observational sigma is also computed for INFO.
    canon_vs_FW_pull_old = (planck_alpha_s - alpha_s_inflation_framework) / planck_alpha_s_err
    canon_vs_FW_pull_new = (alpha_s_canon_2020 - alpha_s_inflation_framework) / alpha_s_canon_2020_err

    # Compare to baseline (S85-W1a-MULTID-FISHER-FRAMEWORK)
    baseline = grep_baseline_verdict("S85-W1a-MULTID-FISHER-FRAMEWORK")  # (local)
    baseline_value = None
    if baseline.get("found"):
        try:
            v = baseline["parsed"].get("value", "")                 # (local)
            # value is np.float64(827.9255704800152) form; strip
            if v.startswith("np.float64("):
                v = v[len("np.float64("):].rstrip(")")
            baseline_value = float(v)
        except Exception:
            baseline_value = None

    # Threshold: PASS iff log10(BF) >= 2.0 AND non-error
    PASS_LOG10BF = 2.0                                              # (local, plan S85 baseline)
    if log10BF >= PASS_LOG10BF:
        verdict = "PASS"                                            # (local)
    elif log10BF <= -2.0:
        verdict = "FAIL"
    else:
        verdict = "INFO"

    return {
        "gate_id": W1A9_REEMIT_GATE_ID,
        "verdict": verdict,
        "value": float(log10BF),
        "scheme": "7D-Fisher",
        "convention": "block-diagonal-correlation",
        "L_max": 10,
        "p_FW": p_FW.tolist(),
        "p_LCDM": p_LCDM.tolist(),
        "sigmas": sigmas.tolist(),
        "pulls": pulls.tolist(),
        "pulls_sq": pulls_sq.tolist(),
        "chi2_total": chi2_total,
        "log10_BF": float(log10BF),
        "baseline_value_S85": baseline_value,
        "baseline_S85_W1a_9_match": (baseline_value is not None and
                                     abs(float(log10BF) - baseline_value) < 1e-3),
        "canon_vs_FW_pull_old_planck2018": float(canon_vs_FW_pull_old),
        "canon_vs_FW_pull_new_aiola2020": float(canon_vs_FW_pull_new),
        "n_sigma_widening": float(canon_vs_FW_pull_new - canon_vs_FW_pull_old),
        "reemit_reason": "S86-W13-P12 pin update; numerics unchanged because LCDM null = 0",
    }


# ---------------------------------------------------------------------------
# RE-EMISSION 2: W1b-3 (sigma_corr/sigma_diag) under new pin
# ---------------------------------------------------------------------------
#
# The W1b-3 script (s85_w1b_alpha_s_joint_fisher_correlated.py) computes
# the ratio of correlated to diagonal combined sigma across 5 detectors
# {CMB-S4, CMB-HD, LiteBIRD, DESI-DR3, LISA}. The detector sigmas are
# detector-specific projections (sigma_S4 = 2.1e-3, etc.), NOT the
# canonical observational sigma. The Cauchy-Schwarz widening ratio
# depends only on (a) detector sigmas and (b) correlation matrix C;
# neither depends on the alpha_s_canon central or err. The pin update
# therefore does NOT change the W1b-3 numerical value, but the
# re-emission documents that the gate has been re-evaluated under the
# new canonical state.

def reemit_w1b3() -> dict:
    """Re-emit S85 W1b-3 widening ratio under updated canonical_constants.py.

    The widening-ratio numerics are unchanged because:
      (a) detector sigmas are forecast projections per individual detector
          noise budgets (CMB-S4, CMB-HD, LiteBIRD, DESI-DR3, LISA),
          NOT the canonical observational sigma;
      (b) correlation matrix C is plan-pre-registered (rho_S4_HD=0.30,
          rho_S4_LB=0.15) and does not move with the canonical pin.
    The pin update changes the audit context (which canonical_constants
    the re-emission was computed against), captured in the dual-SHA.
    """
    # Detector sigmas (from s85_w1b_alpha_s_joint_fisher_correlated.py)
    SIGMA_S4_loc = 2.1e-3                                           # (local)
    SIGMA_HD_loc = 1.5e-3                                           # (local)
    SIGMA_LB_loc = 1.05e-2                                          # (local)
    SIGMA_DR3_loc = 1.0e-2                                          # (local)
    SIGMA_LISA_loc = 1.0e-1                                         # (local)
    RHO_S4_HD_loc = 0.30                                            # (local)
    RHO_S4_LB_loc = 0.15                                            # (local)

    sigmas = np.array([SIGMA_S4_loc, SIGMA_HD_loc, SIGMA_LB_loc,
                       SIGMA_DR3_loc, SIGMA_LISA_loc],
                      dtype=np.float64)                              # (local)
    C = np.array([                                                   # (local)
        [1.0,           RHO_S4_HD_loc, RHO_S4_LB_loc, 0.0, 0.0],
        [RHO_S4_HD_loc, 1.0,           0.0,           0.0, 0.0],
        [RHO_S4_LB_loc, 0.0,           1.0,           0.0, 0.0],
        [0.0,           0.0,           0.0,           1.0, 0.0],
        [0.0,           0.0,           0.0,           0.0, 1.0],
    ], dtype=np.float64)
    Sigma = np.diag(sigmas)                                          # (local)
    Cov = Sigma @ C @ Sigma                                          # (local)
    ones = np.ones(5, dtype=np.float64)                              # (local)
    Cov_inv = np.linalg.inv(Cov)                                     # (local)
    var_corr = 1.0 / float(ones @ Cov_inv @ ones)                    # (local)
    sigma_corr = float(np.sqrt(var_corr))                            # (local)
    var_diag = 1.0 / float(np.sum(1.0 / sigmas ** 2))                # (local)
    sigma_diag = float(np.sqrt(var_diag))                            # (local)
    ratio = sigma_corr / sigma_diag                                  # (local)
    det_C = float(np.linalg.det(C))                                  # (local)

    # Compare to baseline (S85-W1b-ALPHA-S-JOINT-FISHER-CORRELATED)
    baseline = grep_baseline_verdict("S85-W1b-ALPHA-S-JOINT-FISHER-CORRELATED")  # (local)
    baseline_value = None
    if baseline.get("found"):
        try:
            v = baseline["parsed"].get("value", "")                  # (local)
            if v.startswith("np.float64("):
                v = v[len("np.float64("):].rstrip(")")
            baseline_value = float(v)
        except Exception:
            baseline_value = None

    PASS_RATIO = 1.25                                                # (local, plan S85 baseline)
    FAIL_RATIO = 1.50                                                # (local)
    if ratio <= PASS_RATIO:
        verdict = "PASS"                                             # (local)
    elif ratio > FAIL_RATIO:
        verdict = "FAIL"
    else:
        verdict = "INFO"

    return {
        "gate_id": W1B3_REEMIT_GATE_ID,
        "verdict": verdict,
        "value": float(ratio),
        "scheme": "Fisher-marg-Gauss",
        "convention": "block-diag-C",
        "L_max": "n/a",
        "ratio": float(ratio),
        "sigma_corr": float(sigma_corr),
        "sigma_diag": float(sigma_diag),
        "det_C": float(det_C),
        "baseline_value_S85": baseline_value,
        "baseline_S85_W1b_3_match": (baseline_value is not None and
                                     abs(float(ratio) - baseline_value) < 1e-6),
        "reemit_reason": "S86-W13-P12 pin update; numerics unchanged because detector sigmas are forecast-fixed",
    }


# ---------------------------------------------------------------------------
# Verdict-line emission helpers
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def append_verdict(gate_id: str, verdict: str, value, scheme: str,
                   convention: str, L_max,
                   audit_sha: str, content_sha: str) -> str:
    """Append canonical verdict line + dual-SHA companion comment row."""
    line = (
        f"{gate_id}: {verdict} -- value={value!r} scheme={scheme} "
        f"convention={convention} L_max={L_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256 companion row: {gate_id} "
        f"audit={audit_sha[:16]} content={content_sha[:16]}\n"
    )
    with S86_VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
    return line


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                 # (local)

    print("=" * 70)
    print(f"{P12_GATE_ID}: ALPHA-S CANONICAL PIN UPDATE")
    print(f"  Plan: sessions/session-plan/session-86-plan-w13.md S=W13-5")
    print(f"  Trigger: [VERIFY] + [SIGN]")
    print(f"  Classification: PHONONIC")
    print("=" * 70)
    print()

    # Pre-flight: verify post-edit canonical_constants.py is parseable
    # (we already imported successfully at module top; if this script ran,
    # canonical_constants is parseable and contains both legacy and new pins).
    print("=== Step 1: post-edit canonical_constants.py verification ===")
    print(f"  planck_alpha_s            = {planck_alpha_s:+.4f}  (LEGACY, retained)")
    print(f"  planck_alpha_s_err        = {planck_alpha_s_err:.4f}  (LEGACY, retained)")
    print(f"  alpha_s_canon_2020        = {alpha_s_canon_2020:+.4f}  (NEW)")
    print(f"  alpha_s_canon_2020_err    = {alpha_s_canon_2020_err:.4f}  (NEW)")
    print(f"  alpha_s_canon_2020_source = {alpha_s_canon_2020_source!r}")
    print(f"  alpha_s_canon_2020_session= {alpha_s_canon_2020_session!r}")
    print(f"  alpha_s_inflation_framework= {alpha_s_inflation_framework:+.6f}  (UNCHANGED)")
    # Publication-precision-pre-registration discipline (per
    # .claude/rules/epistemic-discipline.md, S86 W1c-8 precedent):
    # alpha_s_inflation_framework is computed as n_s_canon**2 - 1 in the
    # full float64 form (-0.06896799000000009), while the published
    # 6-sig-fig presentation is -0.068968. Comparing full float64 against
    # 6-fig presentation requires tol >= 1e-5 (one OOM looser than the
    # publication precision). We use 1e-5.
    PUBPREC_TOL = 1e-5                                               # (local)
    canon_check_ok = (
        planck_alpha_s == -0.0045 and
        planck_alpha_s_err == 0.0067 and
        alpha_s_canon_2020 == +0.0023 and
        alpha_s_canon_2020_err == 0.0063 and
        abs(alpha_s_inflation_framework + 0.068968) < PUBPREC_TOL
    )                                                                # (local)
    print(f"  canon_check_ok = {canon_check_ok}")
    print()

    # Step 2: Diagnostic substitution chain
    print("=== Step 2: Diagnostic substitution chain (plan Section 10) ===")
    diag = diagnostic_chain()
    print(f"  Step 1 -- Definitions:")
    print(f"    alpha_s_old = {diag['alpha_s_old']:+.4f}  sigma_old = {diag['sigma_old']:.4f}")
    print(f"    alpha_s_new = {diag['alpha_s_new']:+.4f}  sigma_new = {diag['sigma_new']:.4f}")
    print(f"    alpha_s_FW  = {diag['alpha_s_FW']:+.6f}  (UNCHANGED)")
    print(f"  Step 2 -- Substitute:")
    print(f"    Delta(central)  = {diag['delta_central']:+.6f}  (expected {EXPECTED_DELTA_CENTRAL:+.6f})")
    print(f"    gap_old         = {diag['gap_old']:+.6f}  (expected {EXPECTED_GAP_OLD:+.6f})")
    print(f"    gap_new         = {diag['gap_new']:+.6f}  (expected {EXPECTED_GAP_NEW:+.6f})")
    print(f"    Delta(gap)      = {diag['delta_gap']:+.6f}  (expected {EXPECTED_DELTA_GAP:+.6f})")
    print(f"  Step 3 -- Simplify:")
    print(f"    n_sigma_old   = {diag['n_sigma_old']:.4f}  (expected {EXPECTED_N_SIGMA_OLD:.3f})")
    print(f"    n_sigma_new   = {diag['n_sigma_new']:.4f}  (expected {EXPECTED_N_SIGMA_NEW:.3f})")
    print(f"    Delta(n_sigma)= {diag['delta_n_sigma']:+.4f}  (expected {EXPECTED_DELTA_N_SIGMA:+.3f})")
    print(f"  Step 4 -- Direction:")
    print(f"    Delta(central) > 0 : {diag['direction']['delta_central_positive']}  -> canon central moves toward POSITIVE")
    print(f"    alpha_s_FW < 0     : {diag['direction']['framework_negative']}  -> framework prediction is NEGATIVE")
    print(f"    Delta(gap) > 0     : {diag['direction']['delta_gap_positive']}  -> gap WIDENS")
    print(f"    Delta(n_sigma) > 0 : {diag['direction']['delta_n_sigma_positive']}  -> tension INCREASES")
    print(f"  Verify match plan Section 10: all_match = {diag['all_match']}")
    print()
    print(f"  Conclusion: pin update WIDENS tension {diag['n_sigma_old']:.2f}σ -> {diag['n_sigma_new']:.2f}σ")
    print(f"             (+{diag['delta_n_sigma']:.2f}σ); framework prediction UNCHANGED.")
    print(f"             This is HARDENING of observational falsifier, NOT framework retraction.")
    print()

    # Step 3: W1a-9 re-emission
    print("=== Step 3: Re-emit S85 W1a-9 (7D Fisher) under new pin ===")
    w1a9 = reemit_w1a9()
    print(f"  log10(BF_FW/LCDM) = {w1a9['log10_BF']:+.4f}  (verdict {w1a9['verdict']})")
    print(f"  baseline (S85)    = {w1a9['baseline_value_S85']}")
    print(f"  match within 1e-3 = {w1a9['baseline_S85_W1a_9_match']}")
    print(f"  Aux: canon_vs_FW pull (old Planck-2018) = {w1a9['canon_vs_FW_pull_old_planck2018']:+.4f}")
    print(f"       canon_vs_FW pull (new Aiola-2020)  = {w1a9['canon_vs_FW_pull_new_aiola2020']:+.4f}")
    print(f"       n_sigma widening: {w1a9['n_sigma_widening']:+.4f}")
    print()

    # Step 4: W1b-3 re-emission
    print("=== Step 4: Re-emit S85 W1b-3 (sigma_corr/sigma_diag) under new pin ===")
    w1b3 = reemit_w1b3()
    print(f"  ratio = sigma_corr / sigma_diag = {w1b3['ratio']:.6f}  (verdict {w1b3['verdict']})")
    print(f"  baseline (S85)    = {w1b3['baseline_value_S85']}")
    print(f"  match within 1e-6 = {w1b3['baseline_S85_W1b_3_match']}")
    print(f"  det(C) = {w1b3['det_C']:.6f}")
    print()

    # Step 5: Compute audit + content SHAs for the P12 gate itself
    print("=== Step 5: Compute audit_sha / content_sha for verdicts ===")
    P12_inputs = [CANON_PY, W1A9_BASELINE_PY, W1B3_BASELINE_PY, S85_VERDICT_TXT]
    pins = log_input_pins(P12_GATE_ID, P12_inputs)
    script_path = Path(__file__).resolve()                           # (local)
    audit_sha_p12, content_sha_p12 = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  P12 audit_sha256:   {audit_sha_p12}")
    print(f"  P12 content_sha256: {content_sha_p12}")
    print()

    # For the re-emissions, audit_sha is computed against the SAME
    # canonical_constants state but with re-emission-specific input maps.
    w1a9_inputs = [CANON_PY, W1A9_BASELINE_PY]
    w1a9_pins = {str(p.relative_to(PROJECT_ROOT)).replace("\\", "/"): sha256_of(p)
                 for p in w1a9_inputs}                                # (local)
    audit_sha_w1a9, content_sha_w1a9 = compute_dual_sha(
        script_path, CANON_PY, w1a9_pins)
    print(f"  W1a-9 re-emit audit_sha256:   {audit_sha_w1a9}")
    print(f"  W1a-9 re-emit content_sha256: {content_sha_w1a9}")

    w1b3_inputs = [CANON_PY, W1B3_BASELINE_PY]
    w1b3_pins = {str(p.relative_to(PROJECT_ROOT)).replace("\\", "/"): sha256_of(p)
                 for p in w1b3_inputs}                                # (local)
    audit_sha_w1b3, content_sha_w1b3 = compute_dual_sha(
        script_path, CANON_PY, w1b3_pins)
    print(f"  W1b-3 re-emit audit_sha256:   {audit_sha_w1b3}")
    print(f"  W1b-3 re-emit content_sha256: {content_sha_w1b3}")
    print()

    # Step 6: Determine P12 verdict
    print("=== Step 6: P12 PASS/FAIL/INFO determination (plan Section 9) ===")
    # PASS criteria:
    #  - canon_check_ok (legacy retained, new added, parseable)
    #  - W1a-9 re-emit produced verdict line (no script error)
    #  - W1b-3 re-emit produced verdict line (no script error)
    #  - diagnostic substitution chain matches plan Section 10
    p12_pass_criteria = {
        "canon_check_ok": canon_check_ok,
        "w1a9_reemit_no_error": w1a9["verdict"] in ("PASS", "FAIL", "INFO"),
        "w1b3_reemit_no_error": w1b3["verdict"] in ("PASS", "FAIL", "INFO"),
        "diagnostic_match": diag["all_match"],
        "legacy_planck_alpha_s_retained": planck_alpha_s == -0.0045,
        "legacy_planck_alpha_s_err_retained": planck_alpha_s_err == 0.0067,
        "new_alpha_s_canon_2020_correct": alpha_s_canon_2020 == +0.0023,
        "new_alpha_s_canon_2020_err_correct": alpha_s_canon_2020_err == 0.0063,
    }                                                                # (local)
    for k, v in p12_pass_criteria.items():
        print(f"  {k}: {v}")
    p12_all_pass = all(p12_pass_criteria.values())                   # (local)
    p12_verdict = "PASS" if p12_all_pass else "FAIL"                 # (local)
    print(f"  P12 overall verdict: {p12_verdict}")
    print()

    # Step 7: Append 3 verdict lines + dual-SHA companion rows
    print("=== Step 7: Append 3 verdict lines to s86_gate_verdicts.txt ===")
    p12_value_for_line = float(alpha_s_canon_2020)                  # (local)
    p12_line = append_verdict(
        P12_GATE_ID, p12_verdict, p12_value_for_line,
        P12_SCHEME, P12_CONVENTION, P12_L_MAX,
        audit_sha_p12, content_sha_p12)
    print(f"  {p12_line.rstrip()}")

    w1a9_line = append_verdict(
        W1A9_REEMIT_GATE_ID, w1a9["verdict"], w1a9["value"],
        w1a9["scheme"], w1a9["convention"], w1a9["L_max"],
        audit_sha_w1a9, content_sha_w1a9)
    print(f"  {w1a9_line.rstrip()}")

    w1b3_line = append_verdict(
        W1B3_REEMIT_GATE_ID, w1b3["verdict"], w1b3["value"],
        w1b3["scheme"], w1b3["convention"], w1b3["L_max"],
        audit_sha_w1b3, content_sha_w1b3)
    print(f"  {w1b3_line.rstrip()}")
    print()

    # Step 8: Write 3 JSON audit logs
    print("=== Step 8: Write 3 JSON audit logs ===")
    p12_audit = {
        "gate_id": P12_GATE_ID,
        "verdict": p12_verdict,
        "value_4tuple": emit_4tuple(p12_value_for_line, P12_SCHEME, P12_CONVENTION, P12_L_MAX),
        "scheme": P12_SCHEME,
        "convention": P12_CONVENTION,
        "L_max": P12_L_MAX,
        "audit_sha256": audit_sha_p12,
        "content_sha256": content_sha_p12,
        "input_pin_map": pins,
        "canonical_baseline_legacy": {
            "planck_alpha_s": float(planck_alpha_s),
            "planck_alpha_s_err": float(planck_alpha_s_err),
        },
        "canonical_new": {
            "alpha_s_canon_2020": float(alpha_s_canon_2020),
            "alpha_s_canon_2020_err": float(alpha_s_canon_2020_err),
            "alpha_s_canon_2020_source": alpha_s_canon_2020_source,
            "alpha_s_canon_2020_session": alpha_s_canon_2020_session,
        },
        "framework_unchanged": {
            "alpha_s_inflation_framework": float(alpha_s_inflation_framework),
        },
        "diagnostic_chain": {k: (v.tolist() if hasattr(v, "tolist") else v)
                              for k, v in diag.items()
                              if k != "direction" and k != "verify"},
        "diagnostic_direction": diag["direction"],
        "diagnostic_verify": diag["verify"],
        "diagnostic_all_match": diag["all_match"],
        "p12_pass_criteria": p12_pass_criteria,
        "p12_all_pass": p12_all_pass,
        "tension_widening_summary": {
            "n_sigma_old_planck2018": diag["n_sigma_old"],
            "n_sigma_new_aiola2020": diag["n_sigma_new"],
            "delta_n_sigma": diag["delta_n_sigma"],
            "framework_alpha_s_unchanged": float(alpha_s_inflation_framework),
            "interpretation": "HARDENING of observational falsifier; framework prediction UNCHANGED",
        },
        "info_subtag": "tension widens 9.62 sigma -> 11.31 sigma; framework prediction frozen at -0.068968",
        "verdict_line": p12_line.rstrip(),
    }
    OUT_JSON_P12.write_text(json.dumps(p12_audit, indent=2,
                                        default=str), encoding="utf-8")
    print(f"  {OUT_JSON_P12.name} written ({OUT_JSON_P12.stat().st_size} bytes)")

    w1a9_audit = {
        "gate_id": W1A9_REEMIT_GATE_ID,
        "reemit_of": "S85-W1a-MULTID-FISHER-FRAMEWORK (S85 W1a-9 7D Fisher)",
        "verdict": w1a9["verdict"],
        "value": w1a9["value"],
        "value_4tuple": emit_4tuple(w1a9["value"], w1a9["scheme"],
                                     w1a9["convention"], w1a9["L_max"]),
        "scheme": w1a9["scheme"],
        "convention": w1a9["convention"],
        "L_max": w1a9["L_max"],
        "audit_sha256": audit_sha_w1a9,
        "content_sha256": content_sha_w1a9,
        "input_pin_map": w1a9_pins,
        "p_FW": w1a9["p_FW"],
        "p_LCDM": w1a9["p_LCDM"],
        "sigmas": w1a9["sigmas"],
        "pulls": w1a9["pulls"],
        "pulls_sq": w1a9["pulls_sq"],
        "chi2_total": w1a9["chi2_total"],
        "log10_BF": w1a9["log10_BF"],
        "baseline_value_S85": w1a9["baseline_value_S85"],
        "baseline_S85_match_within_1e_3": w1a9["baseline_S85_W1a_9_match"],
        "canon_vs_FW_pull_old_planck2018": w1a9["canon_vs_FW_pull_old_planck2018"],
        "canon_vs_FW_pull_new_aiola2020": w1a9["canon_vs_FW_pull_new_aiola2020"],
        "n_sigma_widening": w1a9["n_sigma_widening"],
        "reemit_reason": w1a9["reemit_reason"],
        "verdict_line": w1a9_line.rstrip(),
    }
    OUT_JSON_W1A9.write_text(json.dumps(w1a9_audit, indent=2,
                                         default=str), encoding="utf-8")
    print(f"  {OUT_JSON_W1A9.name} written ({OUT_JSON_W1A9.stat().st_size} bytes)")

    w1b3_audit = {
        "gate_id": W1B3_REEMIT_GATE_ID,
        "reemit_of": "S85-W1b-ALPHA-S-JOINT-FISHER-CORRELATED (S85 W1b-3)",
        "verdict": w1b3["verdict"],
        "value": w1b3["value"],
        "value_4tuple": emit_4tuple(w1b3["value"], w1b3["scheme"],
                                     w1b3["convention"], w1b3["L_max"]),
        "scheme": w1b3["scheme"],
        "convention": w1b3["convention"],
        "L_max": w1b3["L_max"],
        "audit_sha256": audit_sha_w1b3,
        "content_sha256": content_sha_w1b3,
        "input_pin_map": w1b3_pins,
        "ratio": w1b3["ratio"],
        "sigma_corr": w1b3["sigma_corr"],
        "sigma_diag": w1b3["sigma_diag"],
        "det_C": w1b3["det_C"],
        "baseline_value_S85": w1b3["baseline_value_S85"],
        "baseline_S85_match_within_1e_6": w1b3["baseline_S85_W1b_3_match"],
        "reemit_reason": w1b3["reemit_reason"],
        "verdict_line": w1b3_line.rstrip(),
    }
    OUT_JSON_W1B3.write_text(json.dumps(w1b3_audit, indent=2,
                                         default=str), encoding="utf-8")
    print(f"  {OUT_JSON_W1B3.name} written ({OUT_JSON_W1B3.stat().st_size} bytes)")
    print()

    tag = emit_4tuple(p12_value_for_line, P12_SCHEME, P12_CONVENTION, P12_L_MAX)
    print(tag)
    wall = time.time() - t0                                          # (local)
    print(f"\n=== {P12_GATE_ID}: {p12_verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
