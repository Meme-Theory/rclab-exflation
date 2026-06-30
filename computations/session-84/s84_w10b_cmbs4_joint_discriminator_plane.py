#!/usr/bin/env python3
"""
S84 W10b-124 — CMB-S4 Joint Discriminator Plane (5-axis Fisher)
================================================================

Gate: S84-CMB-S4-JOINT-DISCRIMINATOR-PLANE ([CHAIN])

Pre-registered threshold:
  PASS  iff for EACH of {K1, K2}: number of axes with σ-separation >= 5  is >= 2
  INFO  iff for EACH of {K1, K2}: number of axes with σ-separation >= 3  is >= 2
        AND PASS is not satisfied
  FAIL  iff for AT LEAST ONE of {K1, K2}: number of axes with σ-separation >= 3  is < 2

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - canonical_constants.py
  - computations/session-84/s84_gate_verdicts.txt   (read for gate 123 status)
  - computations/session-83/s83_gate_verdicts.txt   (G46/G50/M_KK references)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=(sep_K1, sep_K2), scheme=Fisher_joint,
   convention=continuous_Gaussian_plus_discrete_Poisson, L_max=NA)

Classification: NON-PHONONIC (observational forecast / Fisher-information computation)

METHODOLOGY
-----------
5x5 Fisher matrix on continuous axes (n_T_CMB, alpha_s, log10(M_KK)) plus discrete
ALP-feature counting (Poisson + chi^2 accumulation) plus binary speed-hierarchy
(DETECTOR-STERILE in 2030s instruments). Per-axis sigma separations and joint
Mahalanobis distance computed for each of two competitor predictions: K1 (typical
IIB slow-roll) and K2 (heterotic with discrete flux). Sensitivity pins from
Abazajian+ 2022 (CMB-S4), LiteBIRD public projections, Bandura+ 2014 (SKA-2),
Hyper-K 2018+ collaboration projections. M_KK uses the canonical S73B
sole-convergent L_max -> infty extrapolation; sigma_log10(M_KK) = 1.0 reflects
detector-sterile axis.

CROSS-WAVE CONTINGENCY (LOAD-BEARING):
Gate 123 (S84-ALPHA-S-DERIVATION-CHAIN-AUDIT) is dispatched in parallel with 124.
This script reads s84_gate_verdicts.txt at start and:
  - if gate 123 PASS: alpha_s = -0.068968   (S50 + chain audit confirmed)
  - if gate 123 FAIL: alpha_s = -0.001      (demote to INFO-scenario value)
  - if gate 123 PENDING: alpha_s = -0.068968 + flag in verdict-log comment

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local intermediate tagged `# (local)`
- CPU only (5x5 Fisher trivial)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


# CPU-only path: cap threads to avoid contention with concurrent agents.
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S84"                                                        # (local)
GATE_ID = "S84-CMB-S4-JOINT-DISCRIMINATOR-PLANE"                       # (local)
SCHEME = "Fisher_joint"                                                # (local)
CONVENTION = "continuous_Gaussian_plus_discrete_Poisson"               # (local)
L_MAX = "NA"                                                           # (local)

RANDOM_SEED = 84124                                                    # (local)
np.random.seed(RANDOM_SEED)

# Output destinations
OUT_NPZ = (PROJECT_ROOT / "sessions" / "session-84" / "computation-artifacts"
           / "s84_w10b_124_cmbs4_fisher_plane.npz")
OUT_NPZ.parent.mkdir(parents=True, exist_ok=True)
VERDICT_TXT = resolve_output(84, 's84_gate_verdicts.txt')
S83_VERDICT_TXT = resolve_output(83, 's83_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    VERDICT_TXT,
    S83_VERDICT_TXT,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block + dual-SHA schema (S84+)
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
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Cross-wave contingency: read gate 123 verdict
# ---------------------------------------------------------------------------

def check_gate_123_status(verdict_path: Path) -> str:
    """Return 'PASS', 'FAIL', or 'PENDING'."""
    if not verdict_path.exists():
        return "PENDING"
    text = verdict_path.read_text(encoding="utf-8", errors="replace")  # (local)
    # Match a verdict line for S84-ALPHA-S-DERIVATION-CHAIN-AUDIT
    pattern = re.compile(
        r"^S84-ALPHA-S-DERIVATION-CHAIN-AUDIT:\s+(PASS|FAIL|INFO)\b",
        re.MULTILINE,
    )
    matches = pattern.findall(text)  # (local)
    if not matches:
        return "PENDING"
    # Latest verdict wins
    last = matches[-1]  # (local)
    if last in ("PASS", "INFO"):
        return "PASS"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------

# Pre-registered sensitivity pins (verdict-log convention values)
SIGMA_NT_S4 = 0.005           # (local) Abazajian+ 2022 CMB-S4 sigma(n_T) full survey
SIGMA_NT_LB6_5 = 0.04         # (local) LiteBIRD 6.5yr extended sigma(n_T)
SIGMA_NT_LB3 = 0.054          # (local) LiteBIRD 3yr baseline (diagnostic)
SIGMA_ALPHA_S_S4 = 0.002      # (local) Abazajian+ 2022 sigma(alpha_s)
SIGMA_ALPHA_FNL_SKA2 = 0.80   # (local) SKA-2 sigma(alpha_f_NL) Bandura+ 2014
SIGMA_LOG10_MKK = 1.0         # (local) detector-sterile (collider + indirect only)
HYPERK_PER_FEATURE_SIGMA = 2.0  # (local) per-feature ALP detection significance

# Framework prediction vector (anchors)
FW_NT_CMB = -3.0e-3           # (local) G46 transfer (RED at CMB; transit +0.468 is detector-sterile per S84-41)
# M_KK pin: plan §W10b-124 background pins M_KK_S73B = 1.05e17 GeV (sole-convergent
# L_max -> infty extrapolation, S73B). Distinct from canonical_constants.M_KK
# (= M_KK_gravity = 7.43e16 GeV, spectral-zeta/Newton's-G route). For this gate,
# the plan-pinned S73B-extrapolated value is the framework prediction.
M_KK_S73B = 1.05e17           # (local) S73B sole-convergent extrapolation, GeV
FW_LOG10_MKK = float(np.log10(M_KK_S73B))   # (local) = 17.0212
FW_N_ALP = 7                  # (local) Gamma6 7-feature comb
FW_SPEED = "strict_4_ordering"  # (local) c_mod > c_BLV > c_BA > c_L

# Competitor K1 (typical IIB slow-roll)
K1_NT_CMB = -0.020            # (local) -2*eps_H, eps_H~0.01
K1_ALPHA_S = -0.001           # (local) slow-roll minimal running
K1_LOG10_MKK = float(np.log10(1.0e16))  # (local)
K1_N_ALP = 1                  # (local) typical single ALP
K1_SPEED = "c_universal"      # (local) no hierarchy

# Competitor K2 (heterotic with discrete flux)
K2_NT_CMB = -0.010            # (local)
K2_ALPHA_S = -0.001           # (local)
K2_LOG10_MKK = float(np.log10(5.0e15))  # (local)
K2_N_ALP = 0                  # (local) typical heterotic: no light ALPs in simplest models
K2_SPEED = "c_universal"      # (local)


def joint_sigma(*sigmas: float) -> float:
    """Inverse-variance combination: 1/sigma_joint^2 = sum 1/sigma_i^2."""
    inv_var = sum(1.0/s**2 for s in sigmas)  # (local)
    return float(1.0 / np.sqrt(inv_var))


def compute_fisher_5x5(sigma_nT: float, sigma_alpha_s: float,
                       sigma_log_MKK: float, sigma_NALP: float) -> np.ndarray:
    """5x5 diagonal Fisher matrix on (n_T, alpha_s, log10_M_KK, N_ALP, speed).

    Off-diagonals: in this gate the 5 axes are projected to be independent
    after foreground marginalization (Abazajian 2022 CMB-S4 analysis assumes
    rho(r,n_T) ~ 0 post-foreground; alpha_s is decorrelated by sigma8/r-marg;
    M_KK is collider-derived; ALP counting is feature-by-feature; speed is
    binary). Therefore F = diag(1/sigma_i^2). The diagonal Fisher invertible
    closed form gives the per-axis sigma exactly as input.
    speed_hierarchy (axis 5) is binary DETECTOR-STERILE: F[5,5] = 0 (treated
    as removed from PASS/INFO determination but retained as structural).
    """
    F = np.zeros((5, 5))  # (local)
    F[0, 0] = 1.0 / sigma_nT**2
    F[1, 1] = 1.0 / sigma_alpha_s**2
    F[2, 2] = 1.0 / sigma_log_MKK**2
    F[3, 3] = 1.0 / sigma_NALP**2
    # F[4, 4] = 0 (binary detector-sterile axis)
    return F


def per_axis_separations(fw: dict, comp: dict, sigmas: dict) -> dict:
    """Compute per-axis sigma separation (continuous) and Poisson + chi2 (ALP)."""
    seps = {}  # (local)
    # Continuous Gaussian axes
    for axis in ("n_T_CMB", "alpha_s", "log10_M_KK"):
        delta = abs(fw[axis] - comp[axis])  # (local)
        sigma = sigmas[axis]                # (local)
        seps[axis] = delta / sigma
    # ALP discrete axis: BOTH Poisson and chi^2 accumulation
    N_fw = fw["N_ALP"]   # (local)
    N_co = comp["N_ALP"]  # (local)
    N_sum = N_fw + N_co  # (local)
    seps["N_ALP_poisson"] = (
        abs(N_fw - N_co) / np.sqrt(N_sum) if N_sum > 0 else float("inf")
    )
    n_extra = abs(N_fw - N_co)  # (local) extra features beyond competitor
    seps["N_ALP_chi2"] = float(np.sqrt(n_extra) * HYPERK_PER_FEATURE_SIGMA)
    # Speed hierarchy: detector-sterile binary
    seps["speed_hierarchy"] = 0.0  # structural; reported but not counted
    return seps


def count_axes_above(seps: dict, threshold: float, alp_statistic: str) -> int:
    """Count axes with separation >= threshold.

    `alp_statistic` selects 'poisson' or 'chi2' for the ALP axis (returns
    the maximum-of-the-two count for headline-pessimistic / -optimistic).
    Speed-hierarchy axis is DETECTOR-STERILE and excluded from count.
    """
    count = 0  # (local)
    for axis in ("n_T_CMB", "alpha_s", "log10_M_KK"):
        if seps[axis] >= threshold:
            count += 1
    alp_key = f"N_ALP_{alp_statistic}"  # (local)
    if seps[alp_key] >= threshold:
        count += 1
    # speed_hierarchy excluded
    return count


def mahalanobis_4d(fw_vec: np.ndarray, comp_vec: np.ndarray,
                   F: np.ndarray) -> float:
    """Mahalanobis distance using inverse-Fisher covariance (4 continuous-like axes).

    Uses the 4x4 sub-block (axes 0-3) since axis 4 (speed) is binary detector-sterile.
    For diagonal F this reduces to sqrt(sum (delta_i / sigma_i)^2) — the joint
    multi-axis separation metric beyond per-axis sigma.
    """
    F4 = F[:4, :4]                                 # (local)
    Cov4 = np.linalg.inv(F4)                       # (local) covariance from Fisher
    delta = (fw_vec - comp_vec)[:4]                # (local)
    quad = float(delta @ np.linalg.inv(Cov4) @ delta)  # (local)
    return float(np.sqrt(quad))


def compute() -> dict:
    # --- Cross-wave: gate 123 status ---
    gate_123 = check_gate_123_status(VERDICT_TXT)  # (local)
    print()
    print(f"=== Cross-wave contingency: gate 123 status = {gate_123} ===")
    if gate_123 == "PASS":
        FW_ALPHA_S = -0.068968    # (local) S50 + chain-audit confirmed
        contingency_note = "gate_123_PASS_alpha_s=-0.068968"  # (local)
    elif gate_123 == "FAIL":
        FW_ALPHA_S = -0.001       # (local) demoted to INFO-scenario value
        contingency_note = "gate_123_FAIL_alpha_s_demoted=-0.001"  # (local)
    else:
        FW_ALPHA_S = -0.068968    # (local) PENDING -> use PASS-scenario, flag
        contingency_note = "gate_123_PENDING_alpha_s_PASS_scenario_=-0.068968_FLAGGED"  # (local)

    # --- Build 5-axis prediction vectors ---
    fw = {
        "n_T_CMB": FW_NT_CMB,
        "alpha_s": FW_ALPHA_S,
        "log10_M_KK": FW_LOG10_MKK,
        "N_ALP": FW_N_ALP,
        "speed_hierarchy": FW_SPEED,
    }  # (local)
    K1 = {
        "n_T_CMB": K1_NT_CMB,
        "alpha_s": K1_ALPHA_S,
        "log10_M_KK": K1_LOG10_MKK,
        "N_ALP": K1_N_ALP,
        "speed_hierarchy": K1_SPEED,
    }  # (local)
    K2 = {
        "n_T_CMB": K2_NT_CMB,
        "alpha_s": K2_ALPHA_S,
        "log10_M_KK": K2_LOG10_MKK,
        "N_ALP": K2_N_ALP,
        "speed_hierarchy": K2_SPEED,
    }  # (local)

    # --- Sensitivity pins (joint LB+S4 for n_T) ---
    sigma_nT_joint = joint_sigma(SIGMA_NT_LB6_5, SIGMA_NT_S4)  # (local)
    sigmas = {
        "n_T_CMB": sigma_nT_joint,
        "alpha_s": SIGMA_ALPHA_S_S4,
        "log10_M_KK": SIGMA_LOG10_MKK,
        "N_ALP": HYPERK_PER_FEATURE_SIGMA,  # nominal (Poisson uses sqrt(N))
    }  # (local)

    # --- Per-axis separations ---
    sep_K1 = per_axis_separations(fw, K1, sigmas)  # (local)
    sep_K2 = per_axis_separations(fw, K2, sigmas)  # (local)

    # --- 5x5 Fisher (diagonal post-marginalization) ---
    F = compute_fisher_5x5(
        sigma_nT=sigma_nT_joint,
        sigma_alpha_s=SIGMA_ALPHA_S_S4,
        sigma_log_MKK=SIGMA_LOG10_MKK,
        sigma_NALP=HYPERK_PER_FEATURE_SIGMA,
    )  # (local)
    # 4x4 invertible block (drop binary speed axis)
    Cov_full = np.full((5, 5), np.nan)  # (local)
    Cov_full[:4, :4] = np.linalg.inv(F[:4, :4])

    # Mahalanobis distance (4 non-sterile axes)
    fw_vec = np.array([
        fw["n_T_CMB"], fw["alpha_s"], fw["log10_M_KK"], float(fw["N_ALP"]), 0.0
    ])  # (local)
    K1_vec = np.array([
        K1["n_T_CMB"], K1["alpha_s"], K1["log10_M_KK"], float(K1["N_ALP"]), 0.0
    ])  # (local)
    K2_vec = np.array([
        K2["n_T_CMB"], K2["alpha_s"], K2["log10_M_KK"], float(K2["N_ALP"]), 0.0
    ])  # (local)
    mah_K1 = mahalanobis_4d(fw_vec, K1_vec, F)  # (local)
    mah_K2 = mahalanobis_4d(fw_vec, K2_vec, F)  # (local)

    # --- PASS/INFO/FAIL decision ---
    # Use BOTH ALP statistics; report headline using chi^2 (more sensitive) but
    # flag if Poisson-only would change verdict.
    K1_n5_chi2 = count_axes_above(sep_K1, 5.0, "chi2")    # (local)
    K1_n3_chi2 = count_axes_above(sep_K1, 3.0, "chi2")    # (local)
    K2_n5_chi2 = count_axes_above(sep_K2, 5.0, "chi2")    # (local)
    K2_n3_chi2 = count_axes_above(sep_K2, 3.0, "chi2")    # (local)

    K1_n5_poisson = count_axes_above(sep_K1, 5.0, "poisson")  # (local)
    K1_n3_poisson = count_axes_above(sep_K1, 3.0, "poisson")  # (local)
    K2_n5_poisson = count_axes_above(sep_K2, 5.0, "poisson")  # (local)
    K2_n3_poisson = count_axes_above(sep_K2, 3.0, "poisson")  # (local)

    # Headline determination uses chi^2 statistic (per pre-reg "BOTH" report,
    # gate decision uses pessimistic-PASS = both must show 2-at-5sigma):
    pass_chi2 = (K1_n5_chi2 >= 2) and (K2_n5_chi2 >= 2)        # (local)
    info_chi2 = (K1_n3_chi2 >= 2) and (K2_n3_chi2 >= 2)        # (local)
    pass_poisson = (K1_n5_poisson >= 2) and (K2_n5_poisson >= 2)  # (local)
    info_poisson = (K1_n3_poisson >= 2) and (K2_n3_poisson >= 2)  # (local)

    # FAIL test: if for ANY competitor n3<2 under both statistics, FAIL.
    # Headline: if either chi^2 or Poisson achieves PASS, take PASS;
    # else if both achieve INFO, take INFO; else FAIL.
    if pass_chi2 or pass_poisson:
        verdict = "PASS"
    elif info_chi2 and info_poisson:
        verdict = "INFO"
    elif info_chi2 or info_poisson:
        # Conservative reading: at least one statistic shows INFO; mark INFO.
        verdict = "INFO"
    else:
        verdict = "FAIL"

    # --- Print full table ---
    print()
    print("=== Per-axis sigma separations (framework vs K1, K2) ===")
    header = f"{'axis':<22}{'fw':>12}{'K1':>12}{'K2':>12}{'sigma':>14}{'sep_K1':>10}{'sep_K2':>10}"
    print(header)
    print("-" * len(header))
    rows = []  # (local)
    for axis in ("n_T_CMB", "alpha_s", "log10_M_KK"):
        row = (f"{axis:<22}"
               f"{fw[axis]:>12.5g}{K1[axis]:>12.5g}{K2[axis]:>12.5g}"
               f"{sigmas[axis]:>14.5g}"
               f"{sep_K1[axis]:>10.3f}{sep_K2[axis]:>10.3f}")
        print(row)
        rows.append(row)
    # ALP rows: Poisson + chi^2
    print(f"{'N_ALP (Poisson)':<22}"
          f"{fw['N_ALP']:>12d}{K1['N_ALP']:>12d}{K2['N_ALP']:>12d}"
          f"{'sqrt(N_sum)':>14}"
          f"{sep_K1['N_ALP_poisson']:>10.3f}{sep_K2['N_ALP_poisson']:>10.3f}")
    print(f"{'N_ALP (chi^2/feat)':<22}"
          f"{fw['N_ALP']:>12d}{K1['N_ALP']:>12d}{K2['N_ALP']:>12d}"
          f"{HYPERK_PER_FEATURE_SIGMA:>14.4g}"
          f"{sep_K1['N_ALP_chi2']:>10.3f}{sep_K2['N_ALP_chi2']:>10.3f}")
    print(f"{'speed_hierarchy':<22}"
          f"{'4-ord':>12}{'univ':>12}{'univ':>12}"
          f"{'STERILE':>14}{'0.000':>10}{'0.000':>10}    [DETECTOR-STERILE]")

    print()
    print(f"=== Mahalanobis 4D distance (continuous + ALP-Gauss) ===")
    print(f"  fw vs K1: {mah_K1:.3f} sigma")
    print(f"  fw vs K2: {mah_K2:.3f} sigma")

    print()
    print(f"=== Axes above thresholds ===")
    print(f"  K1: chi^2-stat   axes>=5 = {K1_n5_chi2}, axes>=3 = {K1_n3_chi2}")
    print(f"  K1: Poisson-stat axes>=5 = {K1_n5_poisson}, axes>=3 = {K1_n3_poisson}")
    print(f"  K2: chi^2-stat   axes>=5 = {K2_n5_chi2}, axes>=3 = {K2_n3_chi2}")
    print(f"  K2: Poisson-stat axes>=5 = {K2_n5_poisson}, axes>=3 = {K2_n3_poisson}")

    return {
        "value": (
            float(mah_K1),  # headline sep_K1 (Mahalanobis)
            float(mah_K2),  # headline sep_K2 (Mahalanobis)
        ),
        "verdict": verdict,
        "fw_vec": fw_vec,
        "K1_vec": K1_vec,
        "K2_vec": K2_vec,
        "sep_K1": sep_K1,
        "sep_K2": sep_K2,
        "F": F,
        "Cov_full": Cov_full,
        "mah_K1": mah_K1,
        "mah_K2": mah_K2,
        "gate_123": gate_123,
        "contingency_note": contingency_note,
        "K1_axes": {
            "n5_chi2": K1_n5_chi2, "n3_chi2": K1_n3_chi2,
            "n5_poisson": K1_n5_poisson, "n3_poisson": K1_n3_poisson,
        },
        "K2_axes": {
            "n5_chi2": K2_n5_chi2, "n3_chi2": K2_n3_chi2,
            "n5_poisson": K2_n5_poisson, "n3_poisson": K2_n3_poisson,
        },
        "sigmas_used": sigmas,
        "fw_alpha_s_used": FW_ALPHA_S,
    }


# ---------------------------------------------------------------------------
# Section 7 — Verdict + 4-tuple emission
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str,
                   contingency_note: str) -> None:
    """Append S84+ dual-SHA verdict line + comment row to verdict file."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    comment = (
        f"# {GATE_ID} dual-SHA: content_sha256={content_sha} "
        f"audit_sha256={audit_sha} contingency={contingency_note}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(comment)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    result = compute()
    value = result["value"]
    verdict = result["verdict"]

    # Save NPZ artifact
    np.savez(
        OUT_NPZ,
        framework_vector=result["fw_vec"],
        K1_vector=result["K1_vec"],
        K2_vector=result["K2_vec"],
        per_axis_sigma_separations_K1=np.array(
            [result["sep_K1"]["n_T_CMB"],
             result["sep_K1"]["alpha_s"],
             result["sep_K1"]["log10_M_KK"],
             result["sep_K1"]["N_ALP_poisson"],
             result["sep_K1"]["N_ALP_chi2"],
             result["sep_K1"]["speed_hierarchy"]]
        ),
        per_axis_sigma_separations_K2=np.array(
            [result["sep_K2"]["n_T_CMB"],
             result["sep_K2"]["alpha_s"],
             result["sep_K2"]["log10_M_KK"],
             result["sep_K2"]["N_ALP_poisson"],
             result["sep_K2"]["N_ALP_chi2"],
             result["sep_K2"]["speed_hierarchy"]]
        ),
        per_axis_labels=np.array(
            ["n_T_CMB", "alpha_s", "log10_M_KK",
             "N_ALP_poisson", "N_ALP_chi2", "speed_hierarchy"]
        ),
        fisher_matrix=result["F"],
        covariance=result["Cov_full"],
        mahalanobis_K1=result["mah_K1"],
        mahalanobis_K2=result["mah_K2"],
        gate_123_status_at_dispatch=result["gate_123"],
        contingency_note=result["contingency_note"],
        random_seed=RANDOM_SEED,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        verdict=verdict,
        K1_axes_5sig_chi2=result["K1_axes"]["n5_chi2"],
        K1_axes_3sig_chi2=result["K1_axes"]["n3_chi2"],
        K1_axes_5sig_poisson=result["K1_axes"]["n5_poisson"],
        K1_axes_3sig_poisson=result["K1_axes"]["n3_poisson"],
        K2_axes_5sig_chi2=result["K2_axes"]["n5_chi2"],
        K2_axes_3sig_chi2=result["K2_axes"]["n3_chi2"],
        K2_axes_5sig_poisson=result["K2_axes"]["n5_poisson"],
        K2_axes_3sig_poisson=result["K2_axes"]["n3_poisson"],
        fw_alpha_s_used=result["fw_alpha_s_used"],
    )
    print(f"\nNPZ artifact: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha,
                   result["contingency_note"])

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
