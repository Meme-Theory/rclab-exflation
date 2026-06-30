"""
INV8-W2-4 — Running-Vacuum RG c1 vs Substrate q-Theory n=2 Tracking Coefficient
================================================================================
Investigation 8, Wave 2 (einstein-theorist; volovik co-option for q-theory
tracking-vacuum machinery).

TASK (plan §W2-4): two-part comparison.

  PART 1 (present-epoch coefficient match):
    Compare the substrate q-theory n=2 tracking coefficient (the dimensionless
    H^2-prefactor alpha_V of rho_vac/M_Pl^2) against the Running-Vacuum-Model
    (Sola Peracaula 2022/2024) RG coefficient c1 of Lambda(H)=c0+c1 H^2+...
      D_c1 = |log10(c1_RVM) - log10(c1_substrate)|
    D_c1 < 0.5 PASS (C10 RG-grounded); 0.5<=D_c1<=1.0 INFO; D_c1>1.0 FAIL.

  PART 2 (BBN relief check — SECONDARY axis):
    Extrapolate the RG Lambda(H) back to BBN (X=ln(H_BBN/H0)=40.2756) and compute
    (rho_vac/rho_rad)_BBN^RVM. Substrate lever-route gives 0.474049 > bound 0.227113
    (delta_N_eff=2.087, ~2.087x overshoot). Does the RVM route relieve (<0.227113)
    or reinforce (>=)?

SUBSTRATE FRAMING (phononic-framing.md — IS not IN):
  The cosmological-term tracking rho_vac ~ M_Pl^2 H^2 IS the substrate's
  effacement-residual / Volovik vacuum-partition departure from equilibrium
  (a_0 Seeley-DeWitt zeroth moment tracking the Hubble rate) — NOT a fundamental
  running-vacuum law imposed on a background. Direction of explanation:
    D_K eigenvalues -> q-theory vacuum (Volovik partition) -> n=2 H^2 coefficient
    (kcurv=+3586.53, S97/S101) -> emergent rho_vac(H). The Sola RVM RG-running is
    the SAME equation in QFT language (q-theory = F-theory, same variational
    principle). The RVM H^2 coefficient is the QFT-language IMAGE of the substrate's
    q-theory n=2 spectral coefficient — NOT the other way around.

SUBSTITUTION CHAIN (plan §W2-4 item 7; all numbers substituted below):
  Step 1: rho_vac^substrate = alpha_V M_Pl^2 H^{n_eff}, n_eff=2 (n2tracking=2.0001;
          S101-W1-QEQ-SELFCONS; kcurv=+3586.53 M_KK). Dimensionless H^2-coefficient:
          c1_substrate = alpha_V (the H^2-prefactor of rho_vac/M_Pl^2).
          DILUTION-CC normalization (S98 line 196): rho_vac(H0)=rho_vac_over_rho_obs
          * rho_crit. With rho_crit=3 M_Pl^2 H0^2 (reduced Planck), n_eff=2:
            alpha_V = rho_vac(H0)/(M_Pl^2 H0^2) = 3 * rho_vac_over_rho_obs.
  Step 2: Lambda(H)^RVM = c0 + c1 H^2 + c2 Hdot + ...   [Sola Eq.27/5.10]
            rho_vac^RVM = rho_vac^0 + (3 nu_eff/8pi G_N)(H^2 - H0^2)
          In reduced-Planck units 1/(8pi G_N)=M_Pl^2:
            rho_vac^RVM/M_Pl^2 = rho_vac^0/M_Pl^2 + 3 nu_eff (H^2 - H0^2)
            => c1_RVM = 3 nu_eff,  nu_eff ~ 1e-5..1e-3 (GUT-scale; Sola Eq.28)
  Step 3: BOTH are the H^2-coefficient of rho_vac/M_Pl^2:
            c1_substrate = alpha_V ~ O(1) (full-strength DILUTION-CC tracking)
            c1_RVM       = 3 nu_eff ~ O(nu) (loop-suppressed, |nu|<<1)
            D_c1 = |log10(c1_RVM) - log10(c1_substrate)|
  Step 4: The substrate fixes the H^2-POWER to be EXACTLY 2 (Gibbs-Duhem simple-fluid;
          n_eff=2+Sum(dp_k/dH)n_k/(Sum omega_k n_k), correction->0 at fold per S66) —
          the SAME H^2 power the RVM derives from RG-running. The coefficient MAGNITUDE
          match is the test. POWER agrees; MAGNITUDE is the discriminator.
  Step 5: BBN relief direction. (rho_vac/rho_rad)_BBN = (rho_vac/M_Pl^2) M_Pl^2/rho_rad
          at H_BBN. Substrate lever-route: 0.474049 (S98 from-below n_eff=1.978111),
          0.474049/0.227113 = 2.087x overshoot. RVM route: rho_vac^RVM/M_Pl^2 ~
          3 nu_eff H_BBN^2 (H_BBN>>H0). With rho_rad_BBN=3 M_Pl^2 H_BBN^2 (rad-dom):
            (rho_vac/rho_rad)_BBN^RVM = 3 nu_eff M_Pl^2 H_BBN^2 / rho_rad_BBN = nu_eff.
          IF c1_RVM=c1_substrate THEN same 0.474 overshoot (no relief). Relief requires
          c1_RVM < c1_substrate (a smaller coefficient) OR a different effective n_eff.
  Step 6: sign_verdict keys on D_c1 (do the coefficients agree?). Here c1_substrate~3.1
          (O(1)) vs c1_RVM~1e-5..1e-3 (O(nu)) => D_c1~3..5 >> 1 => DISAGREE. Part 2:
          BECAUSE c1_RVM<<c1_substrate, the RVM (rho_vac/rho_rad)_BBN^RVM=nu_eff~1e-5..1e-3
          << 0.227113 => RVM RELIEVES, but only BY the coefficient difference. The honest
          coupling: substrate-overshoot and RVM-relief are TWO DIFFERENT laws with the SAME
          power (n=2) but radically different coefficient magnitude. Grounding C10 in the
          RVM running FAILS: the substrate tracking is NOT the loop-suppressed RVM running.

The n_eff sign dispute (R-3, S66 G_eff-route n_eff=2.3 vs S98/S99 lever-route n_eff=
1.978111<2) is the upstream sign dispute — disclosed; the canonical n_eff=1.978111
from-below (S98 V.9 HARD) is used. The dispute was RECONCILED at S100b
(same-observable theorem) but is orthogonal to the Part-1 coefficient-magnitude
finding (the n_eff direction is a sub-percent correction to a POWER that is 2 on both
sides; the FAIL is in the O(1)-vs-O(nu) coefficient, not the n_eff direction).

ENV: phonon-exflation-sim/.venv312/Scripts/python.exe; OMP_NUM_THREADS=8; CPU.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np  # noqa: E402

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# -----------------------------------------------------------------------------
# Section 1 — Paths + canonical-constants import (NEVER hardcode framework values)
# -----------------------------------------------------------------------------
SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"   # computations/_shared
INV_DIR = Path(__file__).resolve().parent                         # computations/investigation-8
PROJECT_ROOT = INV_DIR.parent.parent                              # repo root
INV_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: E402,F401,F403  (per math-scripts.md MANDATORY)
# Explicit names used (all from canonical_constants; documented for the reader):
from canonical_constants import (  # noqa: E402
    M_Pl_reduced,
    H_0_GeV,
    rho_crit_GeV4,
    rho_vac_over_rho_obs,
    rho_vac_over_rho_rad_BBN_below,
    T_BBN_GeV,
    g_star_BBN,
    M_KK,
    tau_fold,
    a_0_FW_zeta,
)

GATE_ID = "INV8-W2-4"
SESSION = 8                        # (local) investigation-track unit number (NOT a framework value)
TRACK = "investigation"
SCHEME = "RVM-Sola"
CONVENTION = "RATIO"
L_MAX = "N/A"
SCHEMA_VERSION = "S84+"

NPZ_OUT = INV_DIR / "inv8_w2_4_running_vacuum_rg_vs_n2.npz"
PNG_OUT = INV_DIR / "inv8_w2_4_running_vacuum_rg_vs_n2.png"

CANONICAL_PY = SHARED_DIR / "canonical_constants.py"
S101_NPZ = PROJECT_ROOT / "computations" / "session-101" / "s101_w4_qeq_selfcons.npz"

# audit_sha256_inputs: ["script", "canonical", "pinmap", "s101_qeq_selfcons_npz"]
INPUT_FILES = [CANONICAL_PY, S101_NPZ]

# -----------------------------------------------------------------------------
# Section 2 — Pre-registered machinery pins (plan §W2-4 machinery_pin_map)
# -----------------------------------------------------------------------------
N_EVAL = 100                       # H-grid points across BBN->present extrapolation       # (local)
SCAN_RANGE = (0.0, 40.2756)        # X = ln(H/H_0) from present (X=0) to BBN (X=40.2756)    # (local)
STEP_SIZE = 0.40756                # uniform X-grid, 100 points                             # (local)
TOLERANCE = 0.5                    # D_c1 coefficient-match tolerance (half an OOM, PASS)   # (local)
INFO_BAND_HI = 1.0                 # 0.5<=D_c1<=1.0 -> INFO; D_c1>1.0 -> FAIL               # (local)
PUBLICATION_PRECISION = 4          # D_c1 and (rho_vac/rho_rad)_BBN published to 4 sig figs # (local)
# BBN bound (S66 canonical): delta_N_eff(vac)=(rho_vac/rho_rad)/(7/8*(4/11)^{4/3}) <= 1
# DERIVED substrate-first/observational (NOT a placeholder) => (local).
BBN_VACUUM_FRACTION_BOUND = 7.0 / 8.0 * (4.0 / 11.0) ** (4.0 / 3.0)   # 0.227107...          # (local)

# RVM running parameter nu_eff band (Sola Eq.28/5.12; GUT-scale particles):
# nu_eff ~ 1e-5..1e-3 (the paper's quoted range; |nu_eff|<<1, loop+log suppressed).
NU_EFF_LO = 1.0e-5                 # Sola lower bound (light-mass / weak deviation)          # (local)
NU_EFF_HI = 1.0e-3                 # Sola upper bound (GUT-scale)                            # (local)
NU_EFF_CENTRAL = 1.0e-3            # canonical RVM headline magnitude (|nu|~10^-3)           # (local)

# regulator_pin: a_0^{zeta} — rho_vac is the a_0-channel tracking vacuum (zeta-regulated
# zeroth Seeley-DeWitt moment, a_0_FW_zeta). CC=a_0, a DIFFERENT moment than gravity a_2.
REGULATOR_PIN = "a_0^{zeta}"       # (local)


# -----------------------------------------------------------------------------
# Section 3 — SHA machinery (canonical dual-SHA, S84+ schema)
# -----------------------------------------------------------------------------
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
    """audit = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""   # (local)
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


# -----------------------------------------------------------------------------
# Section 4 — Read S101 n=2 tracking coefficient (canonical pin cross-check)
# -----------------------------------------------------------------------------
def read_s101() -> dict:
    """Read the S101-W1-QEQ-SELFCONS n=2 tracking output (kcurv, n2tracking)."""
    if not S101_NPZ.exists():
        return {"present": False, "k_curv": None, "slope_selfcons": None}
    d = np.load(S101_NPZ, allow_pickle=True)  # (local)
    k_curv = float(d["k_curv"]) if "k_curv" in d.files else None        # 3586.53...  # (local)
    slope = float(d["slope_selfcons"]) if "slope_selfcons" in d.files else None  # ~1.000074 # (local)
    omega = float(d["omega_q"]) if "omega_q" in d.files else None       # 59.888      # (local)
    return {"present": True, "k_curv": k_curv, "slope_selfcons": slope, "omega_q": omega}


# -----------------------------------------------------------------------------
# Section 5 — Compute (substitution chain Steps 1-6; all numbers substituted)
# -----------------------------------------------------------------------------
def compute(s101: dict) -> dict:
    M_Pl = M_Pl_reduced                                   # reduced Planck 2.435e18 GeV
    H0 = H_0_GeV                                           # 1.438e-42 GeV
    n_eff_substrate = 2.0                                  # (local) n2tracking=2.0001 -> EXACTLY 2
    # S98 from-below tracking exponent (the n_eff sign-dispute canonical, R-3):
    n_eff_BBN_below = 1.978110506244663                   # (local) S98 V.9 HARD from-below

    # === Step 1: substrate c1 = alpha_V (the dimensionless H^2-prefactor) ===
    # DILUTION-CC normalization: rho_vac(H0) = rho_vac_over_rho_obs * rho_crit.
    # Reading A (reduced-Planck identity rho_crit = 3 M_Pl^2 H0^2):
    #   alpha_V = rho_vac(H0)/(M_Pl^2 H0^2) = 3 * rho_vac_over_rho_obs.
    c1_substrate_reduced = 3.0 * rho_vac_over_rho_obs     # (local) = 3 * 1.032 = 3.096
    # Reading B (S98-consistent: uses the canonical observational rho_crit_GeV4=4.08e-47,
    #   which is the value the actual BBN-fraction pin 0.474049 was computed against):
    rho_vac_0 = rho_vac_over_rho_obs * rho_crit_GeV4      # (local)
    c1_substrate_S98 = rho_vac_0 / (M_Pl ** 2 * H0 ** 2)  # (local) ~3.434 (rho_crit/3M_Pl^2H0^2=1.109)
    # The 0.04-dex spread between readings is the (h~0.7 observational rho_crit) vs
    # (reduced-Planck identity) mismatch; BOTH are O(1) and both give D_c1 >> 1.
    # PRIMARY = the S98-consistent reading (it is the alpha_V the BBN pin uses).
    c1_substrate = c1_substrate_S98                       # (local) primary
    c1_substrate_spread_dex = float(abs(np.log10(c1_substrate_S98)
                                        - np.log10(c1_substrate_reduced)))  # (local) ~0.044

    # === Step 2: RVM c1 = 3 nu_eff (Sola Eq.27/5.10, reduced-Planck units) ===
    c1_RVM_lo = 3.0 * NU_EFF_LO                            # (local) 3e-5
    c1_RVM_hi = 3.0 * NU_EFF_HI                            # (local) 3e-3
    c1_RVM_central = 3.0 * NU_EFF_CENTRAL                  # (local) 3e-3 (headline |nu|~1e-3)
    # Most-generous-to-PASS RVM value = the LARGEST c1_RVM (closest to the O(1) substrate):
    c1_RVM_best = c1_RVM_hi                                # (local) 3e-3 (best case for a match)

    # === Step 3: D_c1 coefficient match ===
    D_c1_central = float(abs(np.log10(c1_RVM_central) - np.log10(c1_substrate)))   # (local)
    D_c1_best = float(abs(np.log10(c1_RVM_best) - np.log10(c1_substrate)))         # (local) most generous
    D_c1_lo = float(abs(np.log10(c1_RVM_lo) - np.log10(c1_substrate)))             # (local) worst (smallest nu)
    # The binding (most-generous-to-PASS) discriminator is D_c1_best.
    D_c1 = D_c1_best                                       # (local) the reported D_c1 (best case)

    # === Step 4: H^2-power agreement (POWER vs MAGNITUDE) ===
    power_substrate = n_eff_substrate                     # (local) 2 exactly
    power_RVM = 2.0                                        # (local) RVM O(H^2) leading term
    power_match = bool(abs(power_substrate - power_RVM) < 1e-9)   # (local) True (both n=2)
    # cross-check: S101 n2tracking slope ~ 1.000074 confirms the integer power = 2
    s101_power_confirm = (s101["slope_selfcons"] is not None
                          and abs(s101["slope_selfcons"] - 1.0) < 0.05)  # (local)

    # === Step 5: BBN relief check (SECONDARY axis) ===
    # H-grid X = ln(H/H_0) in [0, 40.2756] (present -> BBN); 100 points.
    X_grid = np.linspace(SCAN_RANGE[0], SCAN_RANGE[1], N_EVAL)   # (local)
    H_over_H0_grid = np.exp(X_grid)                        # (local)
    X_BBN = SCAN_RANGE[1]                                  # (local) 40.2756
    H_ratio_BBN = float(np.exp(X_BBN))                     # (local) H_BBN/H_0

    # rad-dom Friedmann at BBN: rho_rad_BBN = 3 M_Pl^2 H_BBN^2; reproduce the S98 path
    # to confirm the substrate lever-route fraction == canonical 0.474049.
    rho_rad_BBN = (np.pi ** 2 / 30.0) * g_star_BBN * T_BBN_GeV ** 4   # (local)
    H_BBN = float(np.sqrt(rho_rad_BBN / (3.0 * M_Pl ** 2)))           # (local)
    H_ratio_BBN_direct = float(H_BBN / H0)                # (local) cross-check vs exp(40.2756)
    X_BBN_direct = float(np.log(H_ratio_BBN_direct))      # (local) ~40.2756 (lever cross-check)

    # substrate lever-route BBN fraction (reproduce S98 0.474049):
    frac_substrate_BBN = float(rho_vac_0 * (H_ratio_BBN_direct ** n_eff_BBN_below)
                               / rho_rad_BBN)             # (local) -> 0.474049
    frac_substrate_BBN_n2 = float(rho_vac_0 * (H_ratio_BBN_direct ** n_eff_substrate)
                                  / rho_rad_BBN)          # (local) n=2 baseline (1.1447)
    substrate_overshoot = float(frac_substrate_BBN / BBN_VACUUM_FRACTION_BOUND)   # (local) ~2.087

    # RVM BBN fraction: rho_vac^RVM/M_Pl^2 ~ 3 nu_eff H_BBN^2 (H_BBN>>H0, drop -H0^2).
    #   (rho_vac/rho_rad)_BBN^RVM = 3 nu_eff M_Pl^2 H_BBN^2 / rho_rad_BBN
    #   with rho_rad_BBN = 3 M_Pl^2 H_BBN^2 (rad-dom) => = nu_eff.
    rad_dom_factor = float(M_Pl ** 2 * H_BBN ** 2 / rho_rad_BBN)   # (local) = 1/3
    frac_RVM_BBN_lo = float(c1_RVM_lo * rad_dom_factor)       # (local) = nu_eff_lo
    frac_RVM_BBN_hi = float(c1_RVM_hi * rad_dom_factor)       # (local) = nu_eff_hi
    frac_RVM_BBN_central = float(c1_RVM_central * rad_dom_factor)  # (local) = nu_eff_central
    # Relief if (rho_vac/rho_rad)_BBN^RVM < bound:
    rvm_relief = bool(frac_RVM_BBN_hi < BBN_VACUUM_FRACTION_BOUND)   # (local) True (1e-3<<0.227)
    rvm_relief_factor = float(frac_RVM_BBN_central / frac_substrate_BBN)  # (local) how much smaller

    # === Step 6: directional read-off ===
    # sign_verdict keys on D_c1 (do the coefficients AGREE in magnitude?).
    #   The substrate c1 is O(1); the RVM c1 is O(nu)<<1. They DISAGREE => the
    #   "C10 is the RVM running" claim is NOT supported => sign = FAIL.
    coefficients_agree = bool(D_c1 < TOLERANCE)           # (local) D_c1~2.5..5 -> False
    sign_verdict = "PASS" if coefficients_agree else "FAIL"   # (local)
    # magnitude_verdict: D_c1 band. PASS iff D_c1<0.5; INFO iff 0.5<=D_c1<=1.0; FAIL iff >1.0.
    if D_c1 < TOLERANCE:
        magnitude_verdict = "PASS"                        # (local)
    elif D_c1 <= INFO_BAND_HI:
        magnitude_verdict = "INFO"                        # (local)
    else:
        magnitude_verdict = "FAIL"                        # (local)
    # regime_verdict: closed-form coefficient comparison + BBN extrapolation; the
    # H-grid extrapolation is exact (no small-parameter expansion to breach) => VALID.
    # (cross-check: X_BBN_direct must reproduce the 40.2756 lever to <1%.)
    lever_consistent = bool(abs(X_BBN_direct - X_BBN) / X_BBN < 0.01)   # (local)
    bbn_repro_ok = bool(abs(frac_substrate_BBN - rho_vac_over_rho_rad_BBN_below)
                        / rho_vac_over_rho_rad_BBN_below < 1e-3)  # (local) reproduce 0.474049
    regime_verdict = "VALID" if (lever_consistent and bbn_repro_ok) else "MARGINAL"  # (local)

    # === composite collapse rule (gate-verdicts.md, applied at compute time) ===
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                                # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"                                # (local) coefficients disagree => Part-1 FAIL
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"                                # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"                                # (local)
    else:
        composite = "PASS"                                # (local)

    return {
        "M_Pl": M_Pl, "H0": H0,
        "n_eff_substrate": n_eff_substrate, "n_eff_BBN_below": n_eff_BBN_below,
        # --- substrate c1 ---
        "c1_substrate": c1_substrate,
        "c1_substrate_reduced": c1_substrate_reduced,
        "c1_substrate_S98": c1_substrate_S98,
        "c1_substrate_spread_dex": c1_substrate_spread_dex,
        "rho_vac_over_rho_obs": float(rho_vac_over_rho_obs),
        # --- RVM c1 ---
        "nu_eff_lo": NU_EFF_LO, "nu_eff_hi": NU_EFF_HI, "nu_eff_central": NU_EFF_CENTRAL,
        "c1_RVM_lo": c1_RVM_lo, "c1_RVM_hi": c1_RVM_hi, "c1_RVM_central": c1_RVM_central,
        "c1_RVM_best": c1_RVM_best,
        # --- D_c1 ---
        "D_c1": D_c1, "D_c1_best": D_c1_best, "D_c1_central": D_c1_central, "D_c1_lo": D_c1_lo,
        "coefficients_agree": coefficients_agree,
        # --- power ---
        "power_substrate": power_substrate, "power_RVM": power_RVM,
        "power_match": power_match, "s101_power_confirm": s101_power_confirm,
        "s101_k_curv": s101["k_curv"], "s101_slope_selfcons": s101["slope_selfcons"],
        "s101_omega_q": s101.get("omega_q"),
        # --- BBN ---
        "X_BBN": X_BBN, "H_ratio_BBN": H_ratio_BBN,
        "H_BBN": H_BBN, "H_ratio_BBN_direct": H_ratio_BBN_direct, "X_BBN_direct": X_BBN_direct,
        "rho_rad_BBN": rho_rad_BBN, "rho_vac_0": rho_vac_0,
        "rad_dom_factor": rad_dom_factor,
        "frac_substrate_BBN": frac_substrate_BBN, "frac_substrate_BBN_n2": frac_substrate_BBN_n2,
        "substrate_overshoot": substrate_overshoot,
        "frac_RVM_BBN_lo": frac_RVM_BBN_lo, "frac_RVM_BBN_hi": frac_RVM_BBN_hi,
        "frac_RVM_BBN_central": frac_RVM_BBN_central,
        "rvm_relief": rvm_relief, "rvm_relief_factor": rvm_relief_factor,
        "bound": BBN_VACUUM_FRACTION_BOUND,
        "lever_consistent": lever_consistent, "bbn_repro_ok": bbn_repro_ok,
        # --- grids for plotting ---
        "X_grid": X_grid, "H_over_H0_grid": H_over_H0_grid,
        # --- verdicts ---
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict, "composite": composite,
    }


# -----------------------------------------------------------------------------
# Section 6 — Plot
# -----------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(17.0, 5.2))

    # Panel 1: c1 comparison (substrate O(1) vs RVM O(nu)) on a log axis
    ax = axes[0]
    cats = ["substrate\nalpha_V\n(n=2 track)", "RVM\n3nu_eff\n(nu~1e-3)",
            "RVM\n3nu_eff\n(nu~1e-5)"]
    vals = [res["c1_substrate"], res["c1_RVM_hi"], res["c1_RVM_lo"]]
    colors = ["C0", "C3", "C1"]
    bars = ax.bar(cats, vals, color=colors, alpha=0.85, log=True)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v * 1.4, f"{v:.2e}",
                ha="center", va="bottom", fontsize=8.5)
    ax.set_ylabel(r"dimensionless $H^2$-coefficient $c_1$ of $\rho_{vac}/M_{Pl}^2$")
    ax.set_title(f"PART 1: c1 match\n"
                 f"D_c1=|log10(c1_RVM_best)-log10(c1_sub)|={res['D_c1']:.4f} "
                 f"=> {res['magnitude_verdict']} (>1.0 => FAIL)")
    ax.set_ylim(min(vals) * 0.2, max(vals) * 5)
    ax.grid(True, which="both", axis="y", alpha=0.25)

    # Panel 2: rho_vac/M_Pl^2 vs H/H0 (both n=2 power, different coefficient)
    ax = axes[1]
    Hr = res["H_over_H0_grid"]                             # (local)
    sub_curve = res["c1_substrate"] * Hr ** 2             # (local) substrate O(1) coeff
    rvm_curve_hi = res["c1_RVM_hi"] * Hr ** 2             # (local) RVM nu=1e-3
    rvm_curve_lo = res["c1_RVM_lo"] * Hr ** 2             # (local) RVM nu=1e-5
    ax.loglog(Hr, sub_curve, "-", color="C0", lw=2.0,
              label=rf"substrate $\alpha_V H^2$ ($c_1$={res['c1_substrate']:.2f})")
    ax.loglog(Hr, rvm_curve_hi, "--", color="C3", lw=1.8,
              label=rf"RVM $3\nu H^2$ ($\nu$=1e-3, $c_1$={res['c1_RVM_hi']:.1e})")
    ax.loglog(Hr, rvm_curve_lo, ":", color="C1", lw=1.6,
              label=rf"RVM $3\nu H^2$ ($\nu$=1e-5, $c_1$={res['c1_RVM_lo']:.1e})")
    ax.axvline(res["H_ratio_BBN"], color="gray", ls="-", lw=0.8,
               label=rf"$H_{{BBN}}/H_0=e^{{40.28}}$")
    ax.set_xlabel(r"$H/H_0$ (epoch lever, $X=\ln(H/H_0)\in[0,40.28]$)")
    ax.set_ylabel(r"$\rho_{vac}/M_{Pl}^2$")
    ax.set_title(f"SAME power n=2, DIFFERENT coefficient\n"
                 f"power_match={res['power_match']} (both H^2); "
                 f"coeff O(1) vs O(nu)")
    ax.legend(fontsize=7.0, loc="upper left")
    ax.grid(True, which="both", alpha=0.2)

    # Panel 3: BBN relief — (rho_vac/rho_rad)_BBN substrate vs RVM vs bound
    ax = axes[2]
    labels = ["substrate\nn=1.978\n(lever)", "RVM\nnu=1e-3", "RVM\nnu=1e-5",
              "bound\n0.227"]
    vals3 = [res["frac_substrate_BBN"], res["frac_RVM_BBN_central"],
             res["frac_RVM_BBN_lo"], res["bound"]]
    colors3 = ["C0", "C3", "C1", "k"]
    bars3 = ax.bar(labels, vals3, color=colors3, alpha=0.85, log=True)
    for b, v in zip(bars3, vals3):
        ax.text(b.get_x() + b.get_width() / 2, v * 1.4, f"{v:.3e}",
                ha="center", va="bottom", fontsize=8.0)
    ax.axhline(res["bound"], color="k", ls="--", lw=1.0)
    ax.set_ylabel(r"$(\rho_{vac}/\rho_{rad})_{BBN}$")
    ax.set_title(f"PART 2: BBN relief (secondary)\n"
                 f"substrate {res['frac_substrate_BBN']:.3f} (2.087x over) | "
                 f"RVM<<bound => RVM relieves (by coeff diff)")
    ax.grid(True, which="both", axis="y", alpha=0.25)

    fig.suptitle(
        f"{GATE_ID}  —  Running-vacuum RVM c1 vs substrate q-theory n=2 coefficient  "
        f"|  c1_sub={res['c1_substrate']:.2f} (O(1)) vs c1_RVM={res['c1_RVM_hi']:.1e} (O(nu)) "
        f"=> D_c1={res['D_c1']:.2f} => COMPOSITE {res['composite']}",
        fontsize=10.5)
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(PNG_OUT, dpi=140)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Section 7 — Verdict payload (NO open-coded append; agent calls emit_verdict)
# -----------------------------------------------------------------------------
def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict: str, magnitude_verdict: str, regime_verdict: str,
                          extra_rows: list[str]) -> dict:
    """Emit the [SIGN] verdict PAYLOAD for the dispatching AGENT to pass to the
    knowledge-MCP emit_verdict tool (race-safe, single lock-serialized writer).
    Investigation track => session=8, track='investigation'."""
    payload: dict = {
        "session": SESSION,
        "track": TRACK,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": SCHEMA_VERSION,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "extra_rows": list(extra_rows),
    }
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# -----------------------------------------------------------------------------
# Section 8 — Main
# -----------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PY, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  M_KK={M_KK:.6e}  tau_fold={tau_fold}  a_0_FW_zeta={a_0_FW_zeta}")
    print()

    s101 = read_s101()  # (local)
    print("=== S101-W1-QEQ-SELFCONS n=2 tracking coefficient (canonical cross-check) ===")
    print(f"  present={s101['present']}  k_curv={s101['k_curv']}  "
          f"slope_selfcons={s101['slope_selfcons']}  omega_q={s101.get('omega_q')}")
    print()

    res = compute(s101)  # (local)

    print("=== Step 1: substrate c1 = alpha_V (dimensionless H^2-prefactor) ===")
    print(f"  rho_vac_over_rho_obs (DILUTION-CC) = {res['rho_vac_over_rho_obs']}")
    print(f"  c1_substrate (S98-consistent, rho_crit=4.08e-47) = {res['c1_substrate_S98']:.6f}  PRIMARY")
    print(f"  c1_substrate (reduced, =3*1.032)                 = {res['c1_substrate_reduced']:.6f}")
    print(f"  reading-spread = {res['c1_substrate_spread_dex']:.4f} dex (h~0.7 rho_crit vs reduced identity)")
    print()
    print("=== Step 2: RVM c1 = 3 nu_eff (Sola Eq.27/5.10, reduced-Planck units) ===")
    print(f"  nu_eff band (Sola Eq.28) = [{res['nu_eff_lo']:.0e}, {res['nu_eff_hi']:.0e}]")
    print(f"  c1_RVM = 3 nu_eff: lo={res['c1_RVM_lo']:.3e}  hi={res['c1_RVM_hi']:.3e}  "
          f"(best-case-for-match = hi = {res['c1_RVM_best']:.3e})")
    print()
    print("=== Step 3: D_c1 coefficient match (PART 1) ===")
    print(f"  D_c1 (best, nu=1e-3)   = |log10({res['c1_RVM_best']:.2e})-log10({res['c1_substrate']:.2f})| "
          f"= {res['D_c1_best']:.4f}")
    print(f"  D_c1 (worst, nu=1e-5)  = {res['D_c1_lo']:.4f}")
    print(f"  REPORTED D_c1 (most generous) = {res['D_c1']:.4f}  vs tol {TOLERANCE} (PASS<) / "
          f"{INFO_BAND_HI} (INFO<=) => magnitude={res['magnitude_verdict']}")
    print(f"  coefficients_agree (D_c1<0.5) = {res['coefficients_agree']}")
    print()
    print("=== Step 4: H^2-power agreement (POWER vs MAGNITUDE) ===")
    print(f"  power_substrate = {res['power_substrate']}  power_RVM = {res['power_RVM']}  "
          f"power_match = {res['power_match']} (both n=2)")
    print(f"  S101 slope_selfcons={res['s101_slope_selfcons']} confirms integer power=2: "
          f"{res['s101_power_confirm']}")
    print()
    print("=== Step 5: BBN relief check (PART 2 — secondary axis) ===")
    print(f"  X_BBN (plan pin) = {res['X_BBN']:.4f}  X_BBN (direct rad-dom) = {res['X_BBN_direct']:.4f}  "
          f"lever_consistent = {res['lever_consistent']}")
    print(f"  substrate lever-route frac_BBN(n=1.978) = {res['frac_substrate_BBN']:.6f} "
          f"(canonical 0.474049; repro_ok={res['bbn_repro_ok']})")
    print(f"  substrate overshoot = {res['frac_substrate_BBN']:.4f}/{res['bound']:.4f} = "
          f"{res['substrate_overshoot']:.4f}x")
    print(f"  RVM (rho_vac/rho_rad)_BBN = nu_eff: lo={res['frac_RVM_BBN_lo']:.3e}  "
          f"central={res['frac_RVM_BBN_central']:.3e}  hi={res['frac_RVM_BBN_hi']:.3e}")
    print(f"  RVM relief (frac_RVM_hi < bound {res['bound']:.4f})? {res['rvm_relief']} "
          f"(BUT only because c1_RVM<<c1_substrate)")
    print()
    print("=== Step 6: directional read-off + composite ===")
    print(f"  sign_verdict     = {res['sign_verdict']}  (coefficients_agree={res['coefficients_agree']})")
    print(f"  magnitude_verdict= {res['magnitude_verdict']}  (D_c1={res['D_c1']:.4f})")
    print(f"  regime_verdict   = {res['regime_verdict']}  (lever_consistent={res['lever_consistent']}, "
          f"bbn_repro_ok={res['bbn_repro_ok']})")
    print(f"  => COMPOSITE = {res['composite']}")
    print()

    # --- value string (compact, downstream-citable; 4 sig figs per pub precision) ---
    value_str = (
        f"composite={res['composite']};"
        f"D_c1={res['D_c1']:.4f};D_c1_worst={res['D_c1_lo']:.4f};"
        f"c1_substrate={res['c1_substrate']:.4f};c1_substrate_reduced={res['c1_substrate_reduced']:.4f};"
        f"c1_RVM_best={res['c1_RVM_best']:.3e};c1_RVM_lo={res['c1_RVM_lo']:.3e};"
        f"nu_eff_band=[{res['nu_eff_lo']:.0e},{res['nu_eff_hi']:.0e}];"
        f"power_substrate={res['power_substrate']:.0f};power_RVM={res['power_RVM']:.0f};power_match={res['power_match']};"
        f"s101_kcurv={res['s101_k_curv']:.4f};s101_slope={res['s101_slope_selfcons']:.6f};"
        f"frac_substrate_BBN={res['frac_substrate_BBN']:.4f};substrate_overshoot={res['substrate_overshoot']:.4f};"
        f"bound={res['bound']:.4f};"
        f"frac_RVM_BBN_central={res['frac_RVM_BBN_central']:.3e};frac_RVM_BBN_hi={res['frac_RVM_BBN_hi']:.3e};"
        f"rvm_relief={res['rvm_relief']};rvm_relief_factor={res['rvm_relief_factor']:.3e};"
        f"coefficients_agree={res['coefficients_agree']};"
        f"sign={res['sign_verdict']};magnitude={res['magnitude_verdict']};regime={res['regime_verdict']};"
        f"reading=C10_NOT_RG-grounded_by_RVM;coupling=substrate_O(1)_vs_RVM_O(nu)_SAME_power_DIFF_magnitude"
    )

    # --- save npz ---
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        composite=res["composite"],
        sign_verdict=res["sign_verdict"], magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        # substrate c1
        c1_substrate=res["c1_substrate"], c1_substrate_reduced=res["c1_substrate_reduced"],
        c1_substrate_S98=res["c1_substrate_S98"],
        c1_substrate_spread_dex=res["c1_substrate_spread_dex"],
        rho_vac_over_rho_obs=res["rho_vac_over_rho_obs"],
        n_eff_substrate=res["n_eff_substrate"], n_eff_BBN_below=res["n_eff_BBN_below"],
        # RVM c1
        nu_eff_lo=res["nu_eff_lo"], nu_eff_hi=res["nu_eff_hi"], nu_eff_central=res["nu_eff_central"],
        c1_RVM_lo=res["c1_RVM_lo"], c1_RVM_hi=res["c1_RVM_hi"], c1_RVM_central=res["c1_RVM_central"],
        c1_RVM_best=res["c1_RVM_best"],
        # D_c1
        D_c1=res["D_c1"], D_c1_best=res["D_c1_best"], D_c1_central=res["D_c1_central"],
        D_c1_lo=res["D_c1_lo"], coefficients_agree=res["coefficients_agree"],
        # power
        power_substrate=res["power_substrate"], power_RVM=res["power_RVM"],
        power_match=res["power_match"], s101_power_confirm=res["s101_power_confirm"],
        s101_k_curv=res["s101_k_curv"] if res["s101_k_curv"] is not None else np.nan,
        s101_slope_selfcons=res["s101_slope_selfcons"] if res["s101_slope_selfcons"] is not None else np.nan,
        s101_omega_q=res["s101_omega_q"] if res["s101_omega_q"] is not None else np.nan,
        # BBN
        X_BBN=res["X_BBN"], H_ratio_BBN=res["H_ratio_BBN"],
        H_BBN=res["H_BBN"], H_ratio_BBN_direct=res["H_ratio_BBN_direct"], X_BBN_direct=res["X_BBN_direct"],
        rho_rad_BBN=res["rho_rad_BBN"], rho_vac_0=res["rho_vac_0"], rad_dom_factor=res["rad_dom_factor"],
        frac_substrate_BBN=res["frac_substrate_BBN"], frac_substrate_BBN_n2=res["frac_substrate_BBN_n2"],
        substrate_overshoot=res["substrate_overshoot"],
        frac_RVM_BBN_lo=res["frac_RVM_BBN_lo"], frac_RVM_BBN_hi=res["frac_RVM_BBN_hi"],
        frac_RVM_BBN_central=res["frac_RVM_BBN_central"],
        rvm_relief=res["rvm_relief"], rvm_relief_factor=res["rvm_relief_factor"],
        bound=res["bound"], rho_vac_over_rho_rad_BBN_below=rho_vac_over_rho_rad_BBN_below,
        lever_consistent=res["lever_consistent"], bbn_repro_ok=res["bbn_repro_ok"],
        # grids
        X_grid=res["X_grid"], H_over_H0_grid=res["H_over_H0_grid"],
        # machinery + provenance
        N_eval=N_EVAL, tolerance=TOLERANCE, info_band_hi=INFO_BAND_HI,
        publication_precision=PUBLICATION_PRECISION, regulator_pin=REGULATOR_PIN,
        M_KK=M_KK, tau_fold=tau_fold, a_0_FW_zeta=a_0_FW_zeta, M_Pl=res["M_Pl"], H0=res["H0"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  npz  -> {NPZ_OUT.relative_to(PROJECT_ROOT)}")

    make_plot(res)
    print(f"  plot -> {PNG_OUT.relative_to(PROJECT_ROOT)}")

    # --- companion rows (dual-SHA + schema-v2 3-tuple + detail + regulator pin) ---
    extra_rows = [
        (f"# {GATE_ID} substitution-chain: c1_substrate=alpha_V="
         f"{res['c1_substrate']:.4f} (O(1), full-strength DILUTION-CC tracking: "
         f"alpha_V=rho_vac(H0)/(M_Pl^2 H0^2)=3*rho_vac_over_rho_obs="
         f"3*{res['rho_vac_over_rho_obs']:.3f}); c1_RVM=3 nu_eff="
         f"{res['c1_RVM_best']:.2e} (O(nu), nu_eff~1e-5..1e-3 loop+log suppressed, "
         f"Sola Eq.27/28); D_c1=|log10(c1_RVM_best)-log10(c1_sub)|={res['D_c1']:.4f}>1.0 "
         f"=> coefficients DISAGREE => C10 NOT RG-grounded by RVM running"),
        (f"# {GATE_ID} POWER vs MAGNITUDE: both n_eff=2 EXACTLY (power_match="
         f"{res['power_match']}; S101 slope_selfcons={res['s101_slope_selfcons']:.6f}~1, "
         f"kcurv={res['s101_k_curv']:.2f}) -- SAME H^2 power, RADICALLY DIFFERENT coefficient "
         f"magnitude (substrate O(1) vs RVM O(nu)); the FAIL is in the coefficient, NOT the power"),
        (f"# {GATE_ID} BBN(Part-2 secondary): substrate lever-route frac_BBN="
         f"{res['frac_substrate_BBN']:.4f}={res['substrate_overshoot']:.4f}x bound "
         f"{res['bound']:.4f} (overshoot, n_eff=1.978 from-below); RVM frac_BBN=nu_eff~"
         f"{res['frac_RVM_BBN_central']:.2e}<<bound => RVM RELIEVES, but ONLY because "
         f"c1_RVM<<c1_substrate (the relief is BOUGHT by the coefficient difference; "
         f"two DIFFERENT laws, not the same mechanism)"),
        (f"# {GATE_ID} n_eff sign-dispute (R-3) disclosure: S66 G_eff-route n_eff=2.3 vs "
         f"S98/S99 lever-route n_eff=1.978111<2 (from-below, V.9 HARD); RECONCILED S100b "
         f"(same-observable theorem); ORTHOGONAL to this finding (the dispute is a sub-percent "
         f"correction to a POWER=2 on BOTH sides; the D_c1 FAIL is in the O(1)-vs-O(nu) coefficient)"),
        (f"# {GATE_ID} regulator_pin=a_0^{{zeta}} LEVEL_CLASS_PIN=FULL # rho_vac is the "
         f"a_0-channel tracking vacuum (zeta-regulated zeroth Seeley-DeWitt moment, "
         f"a_0_FW_zeta={a_0_FW_zeta}); CC=a_0 a DIFFERENT moment than gravity a_2; "
         f"substrate-first: alpha_V derived from rho_vac_over_rho_obs (DILUTION-CC-66) + "
         f"M_Pl/H0 canonical; RVM c1 from Sola Peracaula 2022/2024 (methodological cross-check, "
         f"NOT a substrate replacement); reading=C10_q-theory_DISTINCT_from_RVM_RG-running"),
    ]

    payload = print_verdict_payload(
        res["composite"], value_str, audit_sha, content_sha,
        res["sign_verdict"], res["magnitude_verdict"], res["regime_verdict"],
        extra_rows,
    )

    print()
    print(f"OUTPUT_4TUPLE: (value={res['D_c1']:.6f}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"VERDICT: {GATE_ID}: {res['composite']}  "
          f"[sign={res['sign_verdict']}, magnitude={res['magnitude_verdict']}, "
          f"regime={res['regime_verdict']}]")
    print(f"  elapsed {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
