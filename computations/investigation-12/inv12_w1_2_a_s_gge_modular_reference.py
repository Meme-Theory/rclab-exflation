#!/usr/bin/env python3
"""
INV12 W1-2 — A_s GGE-MODULAR-REFERENCE (5th A_s route)
======================================================

Gate: INV12-W1-2-A-S-GGE-MODULAR-REFERENCE ([SIGN])
Classification: PHONONIC
Owner: lizzi-spectral-functional-theorist

Pre-registered threshold (plan §W1-2):
  R_wall = A_s^{GGE-ref} / A_s_CMB
  PASS iff R_wall in [0.9, 1.1]   (GGE reference lands A_s in the Planck band)
  FAIL iff R_wall >= 2.8          (wall reference-state-INDEPENDENT, worse-than-BD)
  INFO iff R_wall in (1.1, 2.8)   (relocated, not dissolved)
  [SIGN] 3-tuple governs the COMPOSITE (sign-collapse rule, gate-verdicts.md).

HYPOTHESIS (to be tested, NOT assumed):
  The A_s amplitude floor (5.078e-9 TD-canonical, ~3.02x Planck) — proven a
  PERMANENT WALL RELATIVE TO Bunch-Davies (S82 W2-4) — LIFTS into the Planck
  band when the reference modular state is the substrate's post-transit GGE
  modular weight omega (the GGE-relic squeezed state) instead of the BD vacuum.

WHAT THIS GATE COMPUTES (the spectral-functional theorist's move):
  S82 W2-4 already established the GGE-modular reference object:
      A_s^{substrate} = A_s^{BD} . K_substrate,  K_substrate = S_IC^GGE(k_pivot)
      S_IC^GGE(k) = 1 + 2 n_k = |alpha_k + beta_k|^2   (squeezing factor)
  but it computed n_k from S43-MEMORY band-averaged occupations (n ~ 0.46-0.52
  => K_sub ~ 1.92-2.18, K_base=2.035). THIS gate re-derives K_sub from the
  SUBSTRATE-DERIVED, ODE-LOCKED per-mode occupations n_k = |beta_k|^2 of the
  INV12-W3-1 relic spectrum (inv12_w3_1_relic_spectrum_ode_lock.npz). It is a
  SAME-INPUT-SOURCE upgrade: replace the documented band input with the
  substrate-internal computation and test whether the STRUCTURAL conclusion
  survives.

SUBSTITUTION CHAIN [SIGN] (per math-scripts.md MANDATORY discipline):
  Claim: A_s^{GGE-ref} >= A_s^{BD}  (the GGE reference CANNOT lower A_s; FAIL of lift)
  Step 1 (definitions):
    S_IC^BD     = 1                          [BD vacuum: no relic occupation, n_k=0]
    S_IC^GGE(k) = 1 + 2 n_k = |alpha_k+beta_k|^2  [GGE squeezing; n_k=|beta_k|^2]
    K_sub(k)    = S_IC^GGE(k)/S_IC^BD = 1 + 2 n_k
    A_s^{GGE-ref} = A_s^{BD} . K_sub(k_pivot)    [E2.4 -> multiplicative; S82 W2-4]
  Step 2 (positivity substitution — the structural wall):
    n_k = |beta_k|^2 >= 0  (number operator; locked {beta_k} from W3-1)
    => S_IC^GGE = 1 + 2 n_k >= 1  => K_sub >= 1
  Step 3 (canonical form):
    A_s^{GGE-ref} = A_s^{BD} . K_sub,  K_sub in [1, inf)
    R_wall^{GGE}  = R_wall^{BD} . K_sub,  R_wall^{BD} = 5.078e-9/2.1e-9 = 2.4182
  Step 4 (direction from canonical form):
    K_sub >= 1 => A_s^{GGE-ref} >= A_s^{BD}; the GGE reference equal-or-amplifies.
    sign_verdict = PASS iff A_s^{GGE-ref} <= A_s^{BD} (the PLAN's PASS direction).
    Here A_s^{GGE-ref} > A_s^{BD} => sign_verdict = FAIL (GGE makes it worse, however
    slightly; the BD-referenced wall is NOT a wrong-reference-state artifact in SIGN).
  Conclusion: the BD-referenced wall is reference-state-INDEPENDENT in SIGN; n_k>=0
    forbids the lift. CF23 ("permanent structural-position wall") CONFIRMED.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py     (A_s_CMB, tau_fold, gaps; audit only)
  - computations/investigation-12/inv12_w3_1_relic_spectrum_ode_lock.npz (locked {beta_k})
  - this script bytes

Output 4-tuple:
  (value=R_wall^{GGE}, scheme=MODULAR-GGE-REFERENCE, convention=FROZEN-GGE-NON-KMS, L_max=10)

NOTE on the cross-wave input: the orchestrator override pins the CANONICAL name
  inv12_w3_1_relic_spectrum_ode_lock.npz (the plan/WP `..._lock.npz` is a
  slightly-off reference). The npz EXISTS, so the full derivation runs (no
  PRE-REG-INC partial-input close); the locked-{beta_k} availability flag is TRUE.
  rho_relic carries an L_max truncation band (15.41 @ p+q<=7 -> 26.85 @ p+q<=8);
  A_s^{GGE-ref} depends on the OCCUPATIONS n_k (firm, machine-precision), NOT on
  absolute rho_relic, so the verdict is band-INDEPENDENT — the band is reported.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import (  # noqa: F401
    A_s_CMB,
    tau_fold,
    T_GGE_B2,
    Delta_B1,
    Delta_B2,
    Delta_B3,
    Delta_BCS,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent           # computations/investigation-12
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "12"                                                          # (local)
GATE_ID = "INV12-W1-2-A-S-GGE-MODULAR-REFERENCE"                        # (local)
SCHEME = "MODULAR-GGE-REFERENCE"                                        # (local)
CONVENTION = "FROZEN-GGE-NON-KMS"                                       # (local)
L_MAX = 10                                                             # (local)

# Pre-registered bands (plan §W1-2 operator block)
PASS_LO = 0.9                                                          # (local)
PASS_HI = 1.1                                                          # (local)
FAIL_THRESH = 2.8                                                      # (local)

# BD-referenced anchor (S84 AS-PIN-MAP-COMMIT, TD-canonical; falsifier-rigor-registry Row 8)
A_S_BD = 5.078171e-9                                                   # (local) TD-canonical A_s^{BD}
R_WALL_BD = A_S_BD / A_s_CMB                                          # (local) = 2.4182 baseline

RELIC_NPZ = SESSION_DIR / "inv12_w3_1_relic_spectrum_ode_lock.npz"
OUT_NPZ = SESSION_DIR / "inv12_w1_2_a_s_gge_modular_reference.npz"
OUT_PNG = SESSION_DIR / "inv12_w1_2_a_s_gge_modular_reference.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    RELIC_NPZ,
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


def compute_dual_sha(
    script_path: Path, canonical_path: Path, pins: dict[str, str]
) -> tuple[str, str]:
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
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    """Re-derive K_sub = S_IC^GGE(k_pivot) from the LOCKED W3-1 relic occupations,
    then A_s^{GGE-ref} = A_s^{BD} . K_sub and R_wall^{GGE}.

    Multiple pivot readings (S82 R1/R2/R3 analogs) are computed to expose the
    K_sub band; ALL are >= 1 by the n_k >= 0 positivity wall. The CANONICAL
    pivot reading is the softest (lowest-omega, long-wavelength CMB-pivot)
    sector — the S82 R1 reading — because A_s is the long-wavelength curvature
    amplitude. The mult-weighted-mean and geo-mean readings (S82 R2/R3) are
    reported as the band.
    """
    d = np.load(RELIC_NPZ, allow_pickle=True)
    n_k = np.asarray(d["beta2_k"], dtype=float)        # (local) = |beta_k|^2 = GGE occupation
    alpha_k = np.asarray(d["alpha_k"], dtype=float)    # (local)
    beta_k = np.asarray(d["beta_k"], dtype=float)      # (local)
    omega_k = np.asarray(d["omega_k"], dtype=float)    # (local) M_KK
    mult_k = np.asarray(d["mult_k"], dtype=float)      # (local)
    Delta_k = np.asarray(d["Delta_k"], dtype=float)    # (local)
    rho_relic = float(d["rho_relic"])                  # (local) p+q<=7 band
    rho_relic_check = float(d["rho_relic_check"])      # (local) p+q<=8 band
    L_band_ceiling = int(d["L_band_ceiling"])          # (local) = 7
    trunc_consistent = bool(d["truncation_consistent"])  # (local) = False
    locked_beta_available = True                       # (local) npz exists -> full run

    # --- Cross-check 1: per-mode squeezing identity S_IC = |alpha+beta|^2 = 1 + 2 n_k ---
    S_IC_from_ab = (alpha_k + beta_k) ** 2             # (local)
    S_IC_from_n = 1.0 + 2.0 * n_k                      # (local)
    squeeze_resid = float(np.max(np.abs(S_IC_from_ab - S_IC_from_n)))  # (local)
    wronskian_resid = float(np.max(np.abs(alpha_k ** 2 - beta_k ** 2 - 1.0)))  # (local)

    # --- Pivot readings of K_sub = S_IC^GGE(k_pivot) ---
    S_IC = 1.0 + 2.0 * n_k                             # (local) per-mode squeezing factor

    # R1 (canonical): softest mode = lowest omega = longest-wavelength CMB-pivot sector
    i_soft = int(np.argmin(omega_k))                   # (local)
    K_sub_softest = float(S_IC[i_soft])                # (local) CANONICAL pivot reading
    n_pivot_softest = float(n_k[i_soft])               # (local)

    # R2: multiplicity-weighted mean occupation -> S_IC(mean)
    n_bar_mw = float(np.sum(mult_k * n_k) / np.sum(mult_k))  # (local)
    K_sub_meanocc = 1.0 + 2.0 * n_bar_mw               # (local)

    # R3: geometric mean of S_IC over unique modes (isotropic-Haar analog)
    K_sub_geomean = float(np.exp(np.mean(np.log(S_IC))))  # (local)

    # R4: max-occupation mode (most-amplified sector; upper edge of the band)
    i_hi = int(np.argmax(n_k))                         # (local)
    K_sub_maxocc = float(S_IC[i_hi])                   # (local)
    n_pivot_maxocc = float(n_k[i_hi])                  # (local)

    K_sub_readings = {                                 # (local)
        "R1_softest(CANONICAL)": K_sub_softest,
        "R2_mult_weighted_mean": K_sub_meanocc,
        "R3_geometric_mean": K_sub_geomean,
        "R4_max_occupation": K_sub_maxocc,
    }
    K_sub_min = float(min(K_sub_readings.values()))    # (local)
    K_sub_max = float(max(K_sub_readings.values()))    # (local)

    # CANONICAL K_sub: softest sector (S82 R1; A_s = long-wavelength amplitude).
    K_sub = K_sub_softest                              # (local)

    # --- A_s^{GGE-ref} and R_wall^{GGE} ---
    A_s_GGE = A_S_BD * K_sub                           # (local)
    R_wall_GGE = A_s_GGE / A_s_CMB                     # (local) == R_WALL_BD * K_sub

    # Band of R_wall across the four readings (all >= R_WALL_BD by positivity)
    R_wall_band = {k: R_WALL_BD * v for k, v in K_sub_readings.items()}  # (local)

    # --- S82 W2-4 cross-check: K_base = 2.035 from S43-memory band occupations ---
    # B2 band: T=0.668, Delta=Delta_B2; B1 band: T=0.4350 (S43 memory), Delta=Delta_BCS.
    # n_k^GGE = 1/(exp(omega/T)-1), omega ~ Delta per band (pair excitation at gap edge).
    T_B1_S43 = 0.4350                                  # (local) S43-memory B1 GGE Lagrange multiplier
    x_B2 = Delta_B2 / T_GGE_B2                          # (local)
    x_B1 = Delta_BCS / T_B1_S43                         # (local)
    n_B2_s43 = 1.0 / (np.exp(x_B2) - 1.0)              # (local)
    n_B1_s43 = 1.0 / (np.exp(x_B1) - 1.0)              # (local)
    S_IC_B2_s43 = 1.0 + 2.0 * n_B2_s43                 # (local) ~1.92
    S_IC_B1_s43 = 1.0 + 2.0 * n_B1_s43                 # (local) ~2.05
    K_base_s43_geomean = float(np.sqrt(S_IC_B2_s43 * S_IC_B1_s43))  # (local) ~2.0, S82 R2

    # --- SIGN evaluation (plan convention: PASS iff A_s_GGE <= A_s_BD) ---
    # K_sub >= 1 STRUCTURALLY (n_k = |beta_k|^2 >= 0). Here K_sub > 1 => A_s_GGE > A_s_BD.
    delta_A_s = A_s_GGE - A_S_BD                        # (local) > 0
    sign_pass = delta_A_s <= 0.0                        # (local) plan PASS direction; FALSE here
    K_sub_positivity_ok = K_sub_min >= 1.0              # (local) the structural wall holds

    return {
        "value": R_wall_GGE,
        "R_wall_GGE": R_wall_GGE,
        "R_wall_BD": R_WALL_BD,
        "A_s_GGE": A_s_GGE,
        "A_s_BD": A_S_BD,
        "A_s_CMB": float(A_s_CMB),
        "K_sub": K_sub,
        "K_sub_readings": K_sub_readings,
        "K_sub_min": K_sub_min,
        "K_sub_max": K_sub_max,
        "R_wall_band": R_wall_band,
        "n_pivot_softest": n_pivot_softest,
        "n_pivot_maxocc": n_pivot_maxocc,
        "n_bar_mw": n_bar_mw,
        "omega_softest": float(omega_k[i_soft]),
        "squeeze_resid": squeeze_resid,
        "wronskian_resid": wronskian_resid,
        "delta_A_s": delta_A_s,
        "sign_pass": bool(sign_pass),
        "K_sub_positivity_ok": bool(K_sub_positivity_ok),
        "K_base_s43_geomean": K_base_s43_geomean,
        "S_IC_B1_s43": S_IC_B1_s43,
        "S_IC_B2_s43": S_IC_B2_s43,
        "rho_relic": rho_relic,
        "rho_relic_check": rho_relic_check,
        "L_band_ceiling": L_band_ceiling,
        "trunc_consistent": trunc_consistent,
        "locked_beta_available": locked_beta_available,
        "n_modes_unique": int(n_k.size),
        # arrays for plot + npz
        "_n_k": n_k,
        "_S_IC": S_IC,
        "_omega_k": omega_k,
        "_mult_k": mult_k,
        "_Delta_k": Delta_k,
    }


# ---------------------------------------------------------------------------
# Section 6 — [SIGN] 3-tuple + composite collapse
# ---------------------------------------------------------------------------
def evaluate_sign_tuple(res: dict) -> tuple[str, str, str, str]:
    """Return (sign_verdict, magnitude_verdict, regime_verdict, composite).

    sign_verdict   : PASS iff A_s_GGE <= A_s_BD (plan direction); else FAIL.
    magnitude_verdict: PASS if R_wall in [0.9,1.1]; INFO if (1.1,2.8); FAIL if >=2.8.
    regime_verdict : VALID (the squeezing-identity + Wronskian residual is the
                     W3-1 single-segment adiabatic-truncation floor ~3.8e-3 << 1;
                     the per-mode S_IC = 1+2n identity holds; method in-regime).
    composite      : gate-verdicts.md sign-collapse rule.
    """
    R = res["R_wall_GGE"]                              # (local)
    sign_verdict = "PASS" if res["sign_pass"] else "FAIL"  # (local)

    if PASS_LO <= R <= PASS_HI:
        magnitude_verdict = "PASS"                     # (local)
    elif R >= FAIL_THRESH:
        magnitude_verdict = "FAIL"                     # (local)
    else:
        magnitude_verdict = "INFO"                     # (local)

    # Regime: the reconstruction residual is the adiabatic-truncation floor, well
    # within tolerance; the structural positivity (K_sub>=1) is exact.
    regime_verdict = "VALID" if res["squeeze_resid"] < 1e-2 else "MARGINAL"  # (local)

    # Composite collapse (gate-verdicts.md §"Composite-collapse rule"):
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                             # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"                             # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"                             # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"                             # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"                             # (local)
    else:
        composite = "PASS"                             # (local)
    return sign_verdict, magnitude_verdict, regime_verdict, composite


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    sign_verdict: str | None = None,
    magnitude_verdict: str | None = None,
    regime_verdict: str | None = None,
    companion_note: str = "",
    extra_rows: list[str] | None = None,
) -> dict:
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
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))

    # Left: per-mode S_IC = 1 + 2 n_k vs omega (all >= 1 by positivity)
    om = res["_omega_k"]                               # (local)
    sic = res["_S_IC"]                                 # (local)
    ax[0].scatter(om, sic, s=8, alpha=0.5, color="C0")
    ax[0].axhline(1.0, color="k", ls="--", lw=1, label="S_IC^BD = 1 (positivity floor)")
    ax[0].set_xlabel(r"$\omega_k$ (M_KK)")
    ax[0].set_ylabel(r"$S_{IC}^{GGE}(k) = 1 + 2 n_k$")
    ax[0].set_title("GGE squeezing factor per mode\n(locked W3-1 relic; all $\\geq 1$)")
    ax[0].legend(fontsize=8)
    ax[0].grid(alpha=0.3)

    # Right: R_wall readings + bands
    labels = list(res["R_wall_band"].keys())          # (local)
    vals = [res["R_wall_band"][k] for k in labels]    # (local)
    ax[1].axhspan(PASS_LO, PASS_HI, color="green", alpha=0.15, label="PASS band [0.9,1.1]")
    ax[1].axhspan(PASS_HI, FAIL_THRESH, color="gold", alpha=0.12, label="INFO band (1.1,2.8)")
    ax[1].axhspan(FAIL_THRESH, 3.2, color="red", alpha=0.10, label="FAIL band >=2.8")
    ax[1].axhline(res["R_wall_BD"], color="C3", ls="-", lw=1.5,
                  label=f"R_wall^BD = {res['R_wall_BD']:.4f}")
    ax[1].bar(range(len(vals)), vals, color="C0", alpha=0.7)
    ax[1].set_xticks(range(len(labels)))
    ax[1].set_xticklabels([l.split("(")[0].replace("_", "\n") for l in labels],
                          fontsize=7, rotation=0)
    ax[1].set_ylabel(r"$R_{wall}^{GGE} = A_s^{GGE-ref}/A_s^{CMB}$")
    ax[1].set_title(f"GGE-ref does NOT lift the wall\n"
                    f"R_wall^GGE(canonical) = {res['R_wall_GGE']:.4f}; sign=FAIL")
    ax[1].legend(fontsize=7, loc="upper left")
    ax[1].grid(alpha=0.3)

    fig.suptitle("INV12-W1-2 — A_s GGE-modular reference: the BD wall is "
                 "reference-state-INDEPENDENT in SIGN (K_sub >= 1)", fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()
    sign_v, mag_v, regime_v, composite = evaluate_sign_tuple(res)

    # --- Report ---
    print("=== INV12-W1-2 — A_s GGE-MODULAR-REFERENCE ===")
    print(f"  locked-{{beta_k}} available : {res['locked_beta_available']} "
          f"(inv12_w3_1_relic_spectrum_ode_lock.npz; {res['n_modes_unique']} unique modes)")
    print(f"  squeezing identity resid  : max|(a+b)^2-(1+2n)| = {res['squeeze_resid']:.3e}")
    print(f"  Wronskian resid           : max|a^2-b^2-1|      = {res['wronskian_resid']:.3e}")
    print()
    print(f"  A_s^BD  (TD-canonical)    : {res['A_s_BD']:.6e}")
    print(f"  A_s_CMB (Planck 2018)     : {res['A_s_CMB']:.6e}")
    print(f"  R_wall^BD baseline        : {res['R_wall_BD']:.6f}")
    print()
    print("  K_sub = S_IC^GGE(k_pivot) readings (ALL >= 1 by n_k>=0 positivity):")
    for k, v in res["K_sub_readings"].items():
        print(f"     {k:28s} : K_sub = {v:.8f}   R_wall = {res['R_wall_band'][k]:.6f}")
    print(f"  K_sub band [min,max]      : [{res['K_sub_min']:.8f}, {res['K_sub_max']:.8f}]")
    print(f"  CANONICAL K_sub (R1 soft) : {res['K_sub']:.8f}  (omega_soft={res['omega_softest']:.4f})")
    print()
    print(f"  A_s^GGE-ref (canonical)   : {res['A_s_GGE']:.6e}")
    print(f"  R_wall^GGE  (canonical)   : {res['R_wall_GGE']:.6f}")
    print(f"  delta = A_s^GGE - A_s^BD  : {res['delta_A_s']:+.4e}  (>0 => GGE raises, sign FAIL)")
    print()
    print("  S82 W2-4 cross-check (S43-memory band occupations, NOT locked relic):")
    print(f"     S_IC^B1(S43) = {res['S_IC_B1_s43']:.4f}, S_IC^B2(S43) = {res['S_IC_B2_s43']:.4f}")
    print(f"     K_base(S43 geomean) = {res['K_base_s43_geomean']:.4f}  (S82 canonical 2.035)")
    print()
    print(f"  rho_relic band            : {res['rho_relic']:.4f} (p+q<={res['L_band_ceiling']}) "
          f"-> {res['rho_relic_check']:.4f} (p+q<={res['L_band_ceiling']+1}); "
          f"trunc_consistent={res['trunc_consistent']}")
    print(f"     [A_s^GGE-ref depends on OCCUPATIONS n_k (firm), NOT absolute rho_relic "
          f"=> verdict band-INDEPENDENT]")
    print()
    print(f"  [SIGN] sign={sign_v}  magnitude={mag_v}  regime={regime_v}  => composite={composite}")
    print()

    # --- Save npz ---
    np.savez(
        OUT_NPZ,
        R_wall_GGE=res["R_wall_GGE"],
        R_wall_BD=res["R_wall_BD"],
        A_s_GGE=res["A_s_GGE"],
        A_s_BD=res["A_s_BD"],
        A_s_CMB=res["A_s_CMB"],
        K_sub_canonical=res["K_sub"],
        K_sub_min=res["K_sub_min"],
        K_sub_max=res["K_sub_max"],
        K_sub_readings_keys=np.array(list(res["K_sub_readings"].keys())),
        K_sub_readings_vals=np.array(list(res["K_sub_readings"].values())),
        R_wall_band_vals=np.array(list(res["R_wall_band"].values())),
        n_pivot_softest=res["n_pivot_softest"],
        n_pivot_maxocc=res["n_pivot_maxocc"],
        n_bar_mw=res["n_bar_mw"],
        omega_softest=res["omega_softest"],
        squeeze_resid=res["squeeze_resid"],
        wronskian_resid=res["wronskian_resid"],
        delta_A_s=res["delta_A_s"],
        sign_pass=res["sign_pass"],
        K_sub_positivity_ok=res["K_sub_positivity_ok"],
        K_base_s43_geomean=res["K_base_s43_geomean"],
        S_IC_B1_s43=res["S_IC_B1_s43"],
        S_IC_B2_s43=res["S_IC_B2_s43"],
        rho_relic=res["rho_relic"],
        rho_relic_check=res["rho_relic_check"],
        L_band_ceiling=res["L_band_ceiling"],
        trunc_consistent=res["trunc_consistent"],
        locked_beta_available=res["locked_beta_available"],
        n_modes_unique=res["n_modes_unique"],
        n_k=res["_n_k"],
        S_IC=res["_S_IC"],
        omega_k=res["_omega_k"],
        mult_k=res["_mult_k"],
        Delta_k=res["_Delta_k"],
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        composite=composite,
    )
    print(f"  wrote {OUT_NPZ.name}")

    make_plot(res)
    print(f"  wrote {OUT_PNG.name}")
    print()

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    companion = (
        f"K_sub_canonical={res['K_sub']:.6f}(R1-softest); "
        f"K_sub_band=[{res['K_sub_min']:.6f},{res['K_sub_max']:.6f}]; "
        f"R_wall_BD={res['R_wall_BD']:.4f}; locked_beta=TRUE; "
        f"rho_relic_band=[{res['rho_relic']:.2f}(pq<=7),{res['rho_relic_check']:.2f}(pq<=8)]; "
        f"CF23_status=CONFIRMED(reference-state-INDEPENDENT-in-sign); "
        f"S82_W2-4_K_base_S43=2.035"
    )  # (local)
    extra = [
        "# regulator_pin=a_2^{zeta} (Einstein-Hilbert moment; entanglement-first-law variation)",
        "# K_sub=S_IC^GGE/S_IC^BD=(1+2 n_k)/1>=1 STRUCTURAL (n_k=|beta_k|^2>=0 positivity wall)",
        "# locked-relic occupations n_bar_mw=2.736e-4 << S43-memory n~0.5 (S82 K_base=2.035); "
        "K_sub-1 magnitude is SCHEME-DEPENDENT, K_sub>=1 sign is FUNCTIONAL-INDEPENDENT",
    ]  # (local)
    print_verdict_payload(
        composite, res["value"], audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=companion, extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
