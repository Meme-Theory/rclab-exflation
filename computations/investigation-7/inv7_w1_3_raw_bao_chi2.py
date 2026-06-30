#!/usr/bin/env python3
"""
INV7 W1-3 — Raw-DESI-DR2-BAO chi2/N against the CANONICAL w0 = -0.918
=====================================================================

Gate: INV7-W1-3 ([SIGN])

Pre-registered threshold (plan §W1-3, sessions/investigation/investigation-7/
investigation-7-plan-w1.md):
  operator:  chi2/N < 4
  PASS iff chi2/N < 4 (BAO-VIABLE)
  FAIL iff chi2/N >= 4 (BAO-EXCLUDED, like the superseded -0.509)
  INFO iff 2 <= chi2/N < 4 (marginal band)
  (the atlas-09 Item-25 / DESI-DR3-JOINT-50 FAIL-threshold: the SUPERSEDED
   w0 = -0.509 FAILED at chi2/N = 23.2, Delta chi2 = +241 vs LCDM)

CRITICAL pre-registration pins:
  - w0 = w0_FW = -0.918 (Volovik vacuum partition + effacement Gamma_eff=0.99970);
    CONSTANT w (NOT CPL w0-wa; NOT the superseded -0.509; NOT the CPL-plane param).
  - r_d held at the canonical sound horizon r_d = 147.0244278618993 Mpc
    (s64_desi_dv.npz r_d_Mpc; Planck-2018 fiducial), NOT marginalized as a nuisance.
    The framework does NOT modify r_d (BCS transition at ~1e-41 s is irrelevant to
    recombination at T ~ 0.26 eV).
  - tested against the RAW measured DESI DR2 BAO distances {D_M/r_d, D_H/r_d,
    D_V/r_d} + full covariance (arXiv:2503.14738), NOT the CPL-plane (w0,wa)
    projection the project itself flagged misleading, NOT vs a hypothetical
    DR3 reference.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py     (audit_sha256 only)
  - computations/investigation-7/_data/desi_dr2_bao_distances.txt   (FETCHED DESI DR2 means)
  - computations/investigation-7/_data/desi_dr2_bao_covariance.txt  (FETCHED DESI DR2 13x13 cov)
  - script bytes                                     (BOTH audit + content)

Output 4-tuple:
  (value=<chi2/N>, scheme=FW, convention=ABSOLUTE, L_max=N/A)

Classification: PHONONIC-with-cosmological-readout
  The DE EOS w0=-0.918 is the laboratory-IN image of the substrate effacement
  residual (0.03% leakage through Gamma_eff=0.99970 in the Volovik vacuum
  partition). The gate does not fit a w; it takes the substrate-derived w0 and
  asks whether the emergent-FRW distance ladder survives the raw BAO data.
  Flow: D_K spectral action -> a_0 vacuum-energy moment + Volovik partition ->
  effacement residual Gamma_eff=0.99970 -> effective w0=-0.918 -> distance
  ladder D(z) -> BAO chi2.

DISCIPLINE
----------
- `from canonical_constants import *` (w0_FW, Omega_m, Omega_r, Omega_Lambda,
  H_0_km_s_Mpc, c_light_km_s are framework-canonical; never hardcoded here).
- CPU-only (distance integrals + tiny 13x13 cov solve); OMP_NUM_THREADS=8.
- Dual-SHA emitted; agent calls mcp__knowledge__emit_verdict(**payload).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap BEFORE numpy import (no GPU benefit; tiny problem)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SHARED = os.path.join(SCRIPT_DIR, "..", "_shared")
sys.path.insert(0, os.path.abspath(SHARED))
from canonical_constants import *  # noqa: F401,F403
# Explicit names we consume (all canonical):
from canonical_constants import (
    w0_FW,            # -0.918  Framework DE w_0 (Volovik partition + effacement)
    Omega_m,          # 0.315   matter density (Planck 2018)
    Omega_r,          # 9.15e-5 radiation density (Planck 2018)
    Omega_Lambda,     # 0.685   DE density (Planck 2018)
    H_0_km_s_Mpc,     # 67.4    Hubble constant (Planck 2018)
    c_light_km_s,     # 2.99792458e5 km/s
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration pins
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
DATA_DIR = SESSION_DIR / "_data"

SESSION = "7"                                                       # (local) investigation number
GATE_ID = "INV7-W1-3"                                              # (local)
SCHEME = "FW"                                                       # (local)
CONVENTION = "ABSOLUTE"                                             # (local)
L_MAX = "N/A"                                                       # (local) distance-ladder integral

# Pre-registered thresholds (plan §W1-3) — define BEFORE running
PASS_THRESHOLD = 4.0          # chi2/N FAIL-threshold (atlas-09 Item-25)        # (local)
INFO_LOWER = 2.0              # 2 <= chi2/N < 4 is the marginal INFO band        # (local)
N_EVAL = 1000                 # Simpson base-grid nodes per distance integral    # (local)
SCAN_MIN = 0.0               # z integration lower bound                         # (local)
SCAN_MAX = 2.5               # DESI DR2 BAO effective-redshift span ceiling      # (local)
DIST_TOL = 1e-9              # distance-integral convergence tolerance           # (local)

# canonical sound horizon (NOT marginalized) — s64_desi_dv.npz r_d_Mpc, Planck-2018 fiducial
R_D_MPC = 147.0244278618993                                        # (local)

# Superseded reference (the value this gate must NOT use), for reporting only
W0_SUPERSEDED = -0.509        # S49 band-midpoint; FAILED at chi2/N=23.2          # (local)
CHI2_OVER_N_SUPERSEDED = 23.2 # atlas-09 Item-25 / DESI-DR3-JOINT-50 (S50)        # (local)

OUT_NPZ = SESSION_DIR / "inv7_w1_3_raw_bao_chi2.npz"
OUT_PNG = SESSION_DIR / "inv7_w1_3_raw_bao_chi2.png"

DATA_MEAN = DATA_DIR / "desi_dr2_bao_distances.txt"
DATA_COV = DATA_DIR / "desi_dr2_bao_covariance.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    DATA_MEAN,
    DATA_COV,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
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
# Section 5 — Data parsing
# ---------------------------------------------------------------------------

def parse_mean(path: Path):
    """Return (z[N], value[N], quantity[N], tracer[N]) in canonical likelihood order."""
    z_list, v_list, q_list, t_list = [], [], [], []  # (local)
    for line in path.read_text().splitlines():
        s = line.strip()  # (local)
        if not s or s.startswith("#"):
            continue
        parts = s.split()  # (local)
        # z value quantity tracer
        z_list.append(float(parts[0]))
        v_list.append(float(parts[1]))
        q_list.append(parts[2])
        t_list.append(parts[3] if len(parts) > 3 else "?")
    return (np.array(z_list), np.array(v_list),
            np.array(q_list, dtype=object), np.array(t_list, dtype=object))


def parse_cov(path: Path, n: int) -> np.ndarray:
    """Return the NxN covariance matrix (skips comment lines)."""
    rows = []  # (local)
    for line in path.read_text().splitlines():
        s = line.strip()  # (local)
        if not s or s.startswith("#"):
            continue
        rows.append([float(x) for x in s.split()])
    C = np.array(rows, dtype=float)  # (local)
    assert C.shape == (n, n), f"cov shape {C.shape} != ({n},{n})"
    return C


# ---------------------------------------------------------------------------
# Section 6 — Distance ladder (flat wCDM, CONSTANT w = w0)
# ---------------------------------------------------------------------------

def E_of_z(z: float, w0: float) -> float:
    """E(z) = H(z)/H0 for flat wCDM with CONSTANT w = w0.
    rho_DE(z)/rho_DE(0) = (1+z)^{3(1+w0)}   [constant w; NO CPL wa term].
    Omega_DE = 1 - Omega_m - Omega_r (flat).
    """
    zp1 = 1.0 + z  # (local)
    Omega_DE = 1.0 - Omega_m - Omega_r  # (local) flat closure
    return float(np.sqrt(Omega_r * zp1**4
                         + Omega_m * zp1**3
                         + Omega_DE * zp1**(3.0 * (1.0 + w0))))


def H_of_z(z: float, w0: float) -> float:
    """H(z) in km/s/Mpc."""
    return H_0_km_s_Mpc * E_of_z(z, w0)


def D_M(z: float, w0: float) -> float:
    """Comoving transverse distance D_M(z) [Mpc], flat geometry = comoving chi(z)."""
    val, _ = quad(lambda zp: c_light_km_s / H_of_z(zp, w0),
                  0.0, z, limit=N_EVAL, epsabs=DIST_TOL, epsrel=DIST_TOL)  # (local)
    return val


def D_H(z: float, w0: float) -> float:
    """Hubble distance D_H(z) = c/H(z) [Mpc]."""
    return c_light_km_s / H_of_z(z, w0)


def D_V(z: float, w0: float) -> float:
    """Volume-averaged distance D_V(z) = [z D_M^2 D_H]^{1/3} [Mpc]."""
    dm = D_M(z, w0)  # (local)
    dh = D_H(z, w0)  # (local)
    return float((z * dm * dm * dh) ** (1.0 / 3.0))


def predict_ratio(z: float, quantity: str, w0: float) -> float:
    """Predicted distance ratio (D_X / r_d) for the named quantity at z."""
    if quantity == "DM_over_rs":
        return D_M(z, w0) / R_D_MPC
    if quantity == "DH_over_rs":
        return D_H(z, w0) / R_D_MPC
    if quantity == "DV_over_rs":
        return D_V(z, w0) / R_D_MPC
    raise ValueError(f"unknown quantity {quantity!r}")


# ---------------------------------------------------------------------------
# Section 7 — Compute chi2
# ---------------------------------------------------------------------------

def chi2_for_w0(z, val, quant, C_inv, w0: float):
    """Return (chi2, residual_vector, pred_vector) for a CONSTANT-w model."""
    pred = np.array([predict_ratio(float(z[i]), str(quant[i]), w0)
                     for i in range(len(z))])  # (local)
    resid = pred - val  # (local)  Delta = d_pred - d_DESI
    chi2 = float(resid @ C_inv @ resid)  # (local)  Delta^T C^-1 Delta
    return chi2, resid, pred


def compute() -> dict:
    z, val, quant, tracer = parse_mean(DATA_MEAN)
    N = len(z)  # (local) number of BAO distance data points
    C = parse_cov(DATA_COV, N)
    C_inv = np.linalg.inv(C)  # (local) 13x13, tiny

    # --- Primary: CANONICAL constant-w = w0_FW = -0.918 ---
    chi2_FW, resid_FW, pred_FW = chi2_for_w0(z, val, quant, C_inv, w0_FW)
    chi2_over_N_FW = chi2_FW / N  # (local) THE gate statistic

    # --- Reference models (context only; NOT the gate) ---
    chi2_LCDM, resid_LCDM, pred_LCDM = chi2_for_w0(z, val, quant, C_inv, -1.0)
    chi2_over_N_LCDM = chi2_LCDM / N  # (local)
    chi2_SUP, resid_SUP, pred_SUP = chi2_for_w0(z, val, quant, C_inv, W0_SUPERSEDED)
    chi2_over_N_SUP = chi2_SUP / N  # (local) re-derive the -0.509 value on DR2 data

    # per-point standardized residuals (diagonal-normalized) for the plot/report
    sig = np.sqrt(np.diag(C))  # (local)
    nsig_FW = resid_FW / sig  # (local)
    nsig_LCDM = resid_LCDM / sig  # (local)

    delta_chi2_FW_vs_LCDM = chi2_FW - chi2_LCDM  # (local) >0 means LCDM preferred

    print("\n=== Distance-ladder predictions (CONSTANT w) ===")
    print(f"  w0_FW (canonical)   = {w0_FW}")
    print(f"  r_d (held, NOT marg)= {R_D_MPC} Mpc")
    print(f"  N (BAO data points) = {N}")
    print(f"\n  {'tracer':<11s} {'z':>6s} {'quant':<11s} {'data':>9s} "
          f"{'pred_FW':>9s} {'nsig_FW':>8s} {'pred_LCDM':>9s} {'nsig_LCDM':>9s}")
    for i in range(N):
        print(f"  {str(tracer[i]):<11s} {z[i]:6.3f} {str(quant[i]):<11s} "
              f"{val[i]:9.4f} {pred_FW[i]:9.4f} {nsig_FW[i]:+8.2f} "
              f"{pred_LCDM[i]:9.4f} {nsig_LCDM[i]:+9.2f}")

    print(f"\n  chi2_FW (w0=-0.918)       = {chi2_FW:.4f}  -> chi2/N = {chi2_over_N_FW:.4f}")
    print(f"  chi2_LCDM (w0=-1.0)       = {chi2_LCDM:.4f}  -> chi2/N = {chi2_over_N_LCDM:.4f}")
    print(f"  chi2_SUPERSEDED (w0=-0.509)= {chi2_SUP:.4f}  -> chi2/N = {chi2_over_N_SUP:.4f}")
    print(f"  Delta chi2 (FW - LCDM)    = {delta_chi2_FW_vs_LCDM:+.4f}")
    print(f"  [context] atlas-09 Item-25 superseded -0.509: chi2/N = {CHI2_OVER_N_SUPERSEDED} (S50, vs DR1)")

    # --- substitution-chain sign read-off (computed, not asserted) ---
    sign_delta = chi2_over_N_FW - PASS_THRESHOLD  # (local) < 0 => PASS direction
    print("\n=== Substitution-chain sign read-off ===")
    print(f"  chi2/N - threshold = {chi2_over_N_FW:.4f} - {PASS_THRESHOLD} = {sign_delta:+.4f}")
    print(f"  sign(chi2/N - 4)   = {'NEGATIVE (PASS direction)' if sign_delta < 0 else 'POSITIVE (FAIL direction)'}")

    # --- plot ---
    make_plot(z, val, quant, tracer, sig, pred_FW, pred_LCDM, pred_SUP,
              chi2_over_N_FW, chi2_over_N_LCDM, chi2_over_N_SUP)

    np.savez(
        OUT_NPZ,
        z=z, val=val, quant=np.array([str(q) for q in quant]),
        tracer=np.array([str(t) for t in tracer]),
        cov=C, cov_inv=C_inv, sig=sig,
        w0_FW=w0_FW, r_d_Mpc=R_D_MPC, N_data=N,
        Omega_m=Omega_m, Omega_r=Omega_r, Omega_Lambda=Omega_Lambda,
        H0_km_s_Mpc=H_0_km_s_Mpc, c_km_s=c_light_km_s,
        pred_FW=pred_FW, resid_FW=resid_FW, nsig_FW=nsig_FW,
        pred_LCDM=pred_LCDM, resid_LCDM=resid_LCDM, nsig_LCDM=nsig_LCDM,
        pred_SUPERSEDED=pred_SUP,
        chi2_FW=chi2_FW, chi2_over_N_FW=chi2_over_N_FW,
        chi2_LCDM=chi2_LCDM, chi2_over_N_LCDM=chi2_over_N_LCDM,
        chi2_SUPERSEDED=chi2_SUP, chi2_over_N_SUPERSEDED=chi2_over_N_SUP,
        delta_chi2_FW_vs_LCDM=delta_chi2_FW_vs_LCDM,
        pass_threshold=PASS_THRESHOLD, info_lower=INFO_LOWER,
        w0_superseded=W0_SUPERSEDED,
        chi2_over_N_superseded_S50=CHI2_OVER_N_SUPERSEDED,
        sign_delta=sign_delta,
    )
    print(f"\n  saved: {OUT_NPZ.name}, {OUT_PNG.name}")

    return {
        "value": chi2_over_N_FW,
        "N": N,
        "chi2_FW": chi2_FW,
        "chi2_over_N_LCDM": chi2_over_N_LCDM,
        "chi2_over_N_SUP": chi2_over_N_SUP,
        "delta_chi2_FW_vs_LCDM": delta_chi2_FW_vs_LCDM,
        "sign_delta": sign_delta,
    }


def make_plot(z, val, quant, tracer, sig, pred_FW, pred_LCDM, pred_SUP,
              c2n_FW, c2n_LCDM, c2n_SUP):
    """Hubble diagram of D_M/r_d, D_H/r_d, D_V/r_d: data vs models."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # (local)
    qmap = {"DM_over_rs": (0, r"$D_M/r_d$"),
            "DH_over_rs": (1, r"$D_H/r_d$"),
            "DV_over_rs": (2, r"$D_V/r_d$")}  # (local)
    for q, (ax_i, lab) in qmap.items():
        ax = axes[ax_i]  # (local)
        mask = np.array([str(quant[i]) == q for i in range(len(z))])  # (local)
        if mask.any():
            ax.errorbar(z[mask], val[mask], yerr=sig[mask], fmt="ko",
                        capsize=3, label="DESI DR2 (raw)", zorder=5)
            ax.plot(z[mask], pred_FW[mask], "C0s-",
                    label=fr"FW $w_0=-0.918$ ($\chi^2/N={c2n_FW:.2f}$)")
            ax.plot(z[mask], pred_LCDM[mask], "C2^--",
                    label=fr"$\Lambda$CDM ($\chi^2/N={c2n_LCDM:.2f}$)")
            ax.plot(z[mask], pred_SUP[mask], "C3x:",
                    label=fr"superseded $w_0=-0.509$ ($\chi^2/N={c2n_SUP:.2f}$)")
        ax.set_xlabel("z")
        ax.set_ylabel(lab)
        ax.set_title(lab)
        ax.legend(fontsize=8)
        ax.grid(alpha=0.3)
    fig.suptitle(f"INV7-W1-3: raw DESI DR2 BAO vs canonical $w_0=-0.918$ "
                 f"(threshold $\\chi^2/N<4$)", fontsize=12)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Gate verdict + 3-tuple ([SIGN])
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def evaluate_gate(value: float) -> str:
    """chi2/N < 4 -> PASS; 2 <= chi2/N < 4 -> INFO; chi2/N >= 4 -> FAIL."""
    if value < INFO_LOWER:
        return "PASS"
    if value < PASS_THRESHOLD:
        return "INFO"
    return "FAIL"


def sign_magnitude_regime(value: float, verdict: str):
    """[SIGN] 3-tuple per .claude/rules/gate-verdicts.md.

    sign_verdict: PASS iff the substitution-chain Step-4 predicted direction
      (chi2/N below threshold; sign(chi2/N - 4) < 0) matches the computed sign.
    magnitude_verdict: how far chi2/N sits from the threshold band.
    regime_verdict: VALID — flat-wCDM distance integrals are exact on [0, z_eff];
      no small-parameter expansion, no regime boundary crossed in the window.
    """
    sign_delta = value - PASS_THRESHOLD  # (local)
    sign_verdict = "PASS" if sign_delta < 0 else "FAIL"  # (local)
    # magnitude: PASS if cleanly below the INFO band; INFO if in marginal band;
    # FAIL if at/above threshold.
    if value < INFO_LOWER:
        magnitude_verdict = "PASS"  # (local)
    elif value < PASS_THRESHOLD:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)
    regime_verdict = "VALID"  # (local) exact distance integrals, no expansion
    return sign_verdict, magnitude_verdict, regime_verdict


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION),
        "track": "investigation",
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
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    result = compute()
    value = result["value"]
    verdict = evaluate_gate(value)
    sgn, mag, reg = sign_magnitude_regime(value, verdict)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    note = (f"chi2/N={value:.4f} vs threshold 4 over N={result['N']} raw DESI DR2 "
            f"BAO distances; constant-w=-0.918 (NOT CPL, NOT superseded -0.509); "
            f"r_d=147.0244 Mpc held (NOT marginalized)")  # (local)
    extra = [
        f"# INV7-W1-3 context: chi2/N_FW={value:.4f} chi2/N_LCDM={result['chi2_over_N_LCDM']:.4f} "
        f"chi2/N_superseded(-0.509,on-DR2)={result['chi2_over_N_SUP']:.4f} "
        f"Delta_chi2(FW-LCDM)={result['delta_chi2_FW_vs_LCDM']:+.4f}; "
        f"atlas-09 Item-25 superseded -0.509 was chi2/N=23.2 vs DR1 (S50). "
        f"DESI DR2 means+cov: arXiv:2503.14738 (Cobaya bao_data desi_bao_dr2)."
    ]  # (local)

    payload = print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        sign_verdict=sgn, magnitude_verdict=mag, regime_verdict=reg,
        companion_note=note, extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (chi2/N={value:.4f}, "
          f"sign={sgn}/mag={mag}/regime={reg}, wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
