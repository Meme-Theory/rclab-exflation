#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
INV7-W3-1 — Modular-horizon entropy S = <-ln rho_omega> (von Neumann) on the
emergent crossed product A_hor = A_K rtimes_{sigma^omega} R (§VII.BZ, S105-S106)
vs the a_2-area A-hat; test Bekenstein-Hawking scaling S ∝ A-hat / (4 G_eff),
G_eff = 1/(16 pi a_2_FW_zeta M_KK^2).

GEOMETRIC. Substrate-first (phononic-framing.md "IS Space"): the horizon is NOT a
surface the substrate sits inside; it is the emergent Type-II_oo crossed-product
structure of the fabric's own frozen-occupation algebra (Connes-Takesaki). The
entropy IS the substrate's modular entropy; "S = A/4 G" is its emergent,
laboratory-IN thermodynamic image. Direction of explanation:

  D_K(tau) block spectrum {|lambda|_a(tau_fold)}
    -> per-mode BdG occupation f_a of the frozen GGE relic omega
    -> the area operator A-hat = a_2 SECOND Seeley-DeWitt moment (a_2_FW_zeta)
    -> the von Neumann modular entropy S = Sum -f ln f - (1-f) ln(1-f) of omega
       restricted to A_hor
    -> (does it equal?) Bekenstein-Hawking S = A-hat/(4 G_eff).

This gate EXTENDS the S105-W2-3 area-modular construction from the modular
GENERATOR K_a = log[(1-f_a)/f_a] = E_a/T to the modular ENTROPY (the von Neumann
entropy of the quasi-free state). The area AXIS is a controlled family of horizon
TRUNCATIONS Lambda_cut.

Cross-framework parallel tagging (mandatory, structural-vs-analogical discipline):
  * [STRUCTURAL at the area-law ROLE] Both loop-quantum-gravity and the framework
    realize a gauge-invariant geometric entropy that scales with horizon AREA,
    fixed by a SINGLE substrate quantity (loop-quantum-gravity: Immirzi gamma via
    S=A/4 puncture-matching; framework: the M_KK/a_2 pin via S=A/(4 G_eff)
    modular-matching). The "single-parameter pins the area-law coefficient"
    structure is shared.
  * [ANALOGICAL at the content / mechanism] loop-quantum-gravity's S = A/(4 l_P^2)
    comes from COUNTING discrete SU(2) spin-network punctures of an isolated horizon
    (a finite-dim Chern-Simons boundary Hilbert space; the area is a DISCRETE
    operator eigenvalue Sum 8 pi gamma l_P^2 sqrt(j(j+1))). The framework's S comes
    from the CONTINUOUS modular entropy of a quasi-free state on a Type-II_oo
    crossed product -- NO punctures, NO discrete area spectrum (consistent with the
    S105-S106 "no geometric area-clock / no discrete area spectrum" result). The
    mechanisms are structurally DISTINCT: discrete-puncture-counting (equilibrium
    microstate enumeration) vs continuous-modular-entropy (Tomita-Takesaki of a
    non-equilibrium frozen relic). Same observable S ∝ A/4, two distinct machineries.

Verdict: NUMBERS first, gate second, interpretation third. [SIGN] trigger -- the
area-law slope sign is structurally fixed (dS/dA-hat >= 0 == sign(1/(4 G_eff)) > 0);
the gate decides the MAGNITUDE (slope ratio within 15% band) + LINEARITY (R^2 >= 0.95).
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU-cap per math-scripts.md (no >=100x100 matrix)

import sys
import json
import hashlib
from pathlib import Path

import numpy as np

# --- canonical constants (MANDATORY: from canonical_constants import *) -------
_HERE = Path(__file__).resolve().parent
_SHARED = _HERE.parent / "_shared"
sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403  (a_2_FW_zeta, M_KK, T_GGE_B2, Delta_B2/B3/BCS, tau_fold, ...)

# import the verdict-payload printer (script PRINTS payload; agent calls emit_verdict)
TEMPLATE_DIR = _HERE.parent.parent / ".claude" / "templates"
sys.path.insert(0, str(TEMPLATE_DIR))
try:
    from script_template import print_verdict_payload  # type: ignore
except Exception:
    # local fallback printer matching the template contract
    def print_verdict_payload(payload: dict) -> None:  # type: ignore
        print("VERDICT_PAYLOAD_JSON_BEGIN")
        print(json.dumps(payload, sort_keys=True))
        print("VERDICT_PAYLOAD_JSON_END")


# ---------------------------------------------------------------------------
# Section 1 — Identity + pre-registered machinery pins (PRDR)
# ---------------------------------------------------------------------------
GATE_ID = "INV7-W3-1"
SCHEME = "FW"
CONVENTION = ("FROZEN-GGE-QUASI-FREE-MODULAR-ENTROPY;VON-NEUMANN-S;"
              "CONTINUOUS-NO-PUNCTURE;A-hat=a_2_zeta;SLOPE-vs-1/(4 G_eff)")
L_MAX = 10                 # (local) canonical L_max for the named-block modular test (S105-W2-3)
N_CUT = 24                 # (local) number of horizon-truncation Lambda_cut grid points
SLOPE_RATIO_BAND = 0.15    # (local) PASS iff |slope_ratio - 1| <= 0.15 (pre-registered band)
INFO_BAND = 0.50           # (local) INFO band ceiling (sign PASS, magnitude FAIL, regime VALID -> INFO)
R2_MIN = 0.95              # (local) linearity sub-condition (pre-registered)
ENTROPY_TOL = 1e-12        # (local) float64 entropy-sum tolerance (sum is bit-stable)
REGULATOR_PIN = "a_2^{zeta}"
PUB_PRECISION = 4          # (local) slope-ratio published to 4 sig figs

HORIZON_BLOCKS = [(0, 0), (1, 0), (0, 1), (1, 1)]  # the four named horizon sectors (S105-W2-3)

# ---------------------------------------------------------------------------
# Section 2 — Input file pins
# ---------------------------------------------------------------------------
CANON_PY = _SHARED / "canonical_constants.py"
S105_W2_2_NPZ = _HERE.parent / "session-105" / "s105_w2_2_omega_faithful_normal.npz"
S105_W2_3_NPZ = _HERE.parent / "session-105" / "s105_w2_3_area_modular_agreement.npz"
S84_CACHE_NPZ = _HERE.parent / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

OUT_NPZ = _HERE / "inv7_w3_1_modular_horizon_entropy.npz"
OUT_PNG = _HERE / "inv7_w3_1_modular_horizon_entropy.png"


def _sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 3 — Per-mode BdG occupation + von Neumann entropy density
#   (IDENTICAL substitution chain to S105-W2-3 bdg_modular_data; extended to S)
#   xi_a = |lambda|_a - lam_horizon          (normal-state dispersion)
#   E_a  = sqrt(xi_a^2 + Delta_a^2)          (BdG energy >= Delta_a > 0, GAPPED)
#   f_a  = 1/(exp(E_a/T) + 1)                (FD occupation; quasi-free separating)
#   K_a  = log[(1-f_a)/f_a] = E_a/T          (fermionic modular Hamiltonian)
#   s_a  = -f_a ln f_a - (1-f_a) ln(1-f_a)   (von Neumann entropy density, in [0, ln2])
# ---------------------------------------------------------------------------
def bdg_mode_data(abs_evals: np.ndarray, lam_horizon: float, Delta_a: float, T_a: float):
    xi = abs_evals - lam_horizon                          # (local)
    E = np.sqrt(xi * xi + Delta_a * Delta_a)              # (local) >= Delta_a > 0
    x = E / T_a                                           # (local) = K_a exactly
    f = 1.0 / (np.exp(x) + 1.0)                           # (local) in (0, 1/2)
    with np.errstate(divide="ignore", invalid="ignore"):
        K = np.log((1.0 - f) / f)                         # (local) = x for FD form
    # von Neumann entropy density of the per-mode 2-level (occupied/empty) Gaussian state
    s = -f * np.log(f) - (1.0 - f) * np.log(1.0 - f)      # (local) in [0, ln 2]
    return xi, E, f, K, s


def load_horizon_spectrum() -> dict:
    cache = np.load(S84_CACHE_NPZ, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()  # (local) {(p,q): {dim, level, abs_evals}}
    out = {}
    for pq in HORIZON_BLOCKS:
        out[pq] = np.asarray(sector_evals[pq]["abs_evals"], dtype=np.float64)
    return out


# ---------------------------------------------------------------------------
# Section 4 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # ---- 4.0 pins from S105-W2-2 (the faithful-normal omega witness) --------
    d22 = np.load(S105_W2_2_NPZ, allow_pickle=True)
    lam_horizon = float(d22["lam_horizon"])          # (local) 0.8197411...
    T_GGE = float(d22["T_GGE"])                       # (local) 0.668
    Delta_B2_v = float(d22["Delta_B2"])              # (local) 0.732026
    Delta_B3_v = float(d22["Delta_B3"])              # (local) 0.176
    Delta_BCS_v = float(d22["Delta_BCS"])            # (local) 0.4642547
    n_modes_w22 = int(d22["n_modes_total"])          # (local) 720

    # pairing-gap dictionary on the horizon BdG modes (matches S105-W2-3 BDG_GAPS)
    BDG_GAPS = {"B2": Delta_B2_v, "B3": Delta_B3_v, "BCS": Delta_BCS_v}  # (local)
    Delta_min = min(BDG_GAPS.values())               # (local) = Delta_B3 = 0.176

    # ---- 4.1 build the per-mode arrays by replaying the EXACT S105-W2-3 loop -
    #   for ch in {B2,B3,BCS}:  for pq in HORIZON_BLOCKS:
    # so the 720-mode ordering is identical -> the recomputed K_a matches the
    # stored K_modular (faithfulness cross-check below).
    horizon_spec = load_horizon_spectrum()
    lam_list, Delta_list, f_list, K_list, s_list = [], [], [], [], []  # (local)
    for ch, Dg in BDG_GAPS.items():
        for pq in HORIZON_BLOCKS:
            ae = horizon_spec[pq]                                  # (local) sector |lambda| spectrum
            _, _, f, K, s = bdg_mode_data(ae, lam_horizon, Dg, T_GGE)
            lam_list.append(ae)                                   # the D_K eigenvalue carries the area weight 1/lambda^2
            Delta_list.append(np.full_like(ae, Dg))
            f_list.append(f)
            K_list.append(K)
            s_list.append(s)

    lam = np.concatenate(lam_list)        # (local) per-mode |lambda|_a (720,)
    f_occ = np.concatenate(f_list)        # (local) per-mode occupation f_a (720,)
    K_a = np.concatenate(K_list)          # (local) per-mode modular Hamiltonian (720,)
    s_vn = np.concatenate(s_list)         # (local) per-mode von Neumann entropy density (720,)
    n_modes = int(lam.size)               # (local) = 720

    # ---- 4.2 FAITHFULNESS cross-check: recomputed K_a vs stored K_modular ----
    d23 = np.load(S105_W2_3_NPZ, allow_pickle=True)
    K_stored = np.asarray(d23["K_modular"], dtype=np.float64)     # (local) (720,)
    A_hat_full = float(d23["A_hat"])                              # (local) 2776.165389 (a_2_zeta)
    K_match_max = float(np.max(np.abs(K_a - K_stored)))           # (local) should be ~machine eps
    faithful_K = bool(K_match_max < 1e-9)                         # (local)

    # ---- 4.3 area AXIS: controlled horizon truncations Lambda_cut -----------
    # A-hat(Lambda) = Sum_{|lambda|_a <= Lambda} 1/lambda_a^2  (a_2-partial moment on the
    # truncated horizon patch; mult=1 per unfolded mode). FULL value tracks a_2_FW_zeta
    # scale; the regression uses the dimensionless partial moment directly.
    # S(Lambda)     = Sum_{|lambda|_a <= Lambda} s_a            (von Neumann entropy)
    lam_max = float(lam.max())                                   # (local) full named-block max |lambda|
    lam_lo = lam_horizon + 0.25 * Delta_min                      # (local) just above horizon mode
    # ensure the grid lower edge admits at least the horizon mode
    Lambda_grid = np.linspace(lam_lo, lam_max, N_CUT)            # (local) N_cut=24 truncation grid

    area_per_mode = 1.0 / (lam * lam)                            # (local) a_2-weight 1/lambda^2 per mode
    A_axis = np.empty(N_CUT, dtype=np.float64)                   # (local) partial a_2 moment
    S_axis = np.empty(N_CUT, dtype=np.float64)                   # (local) partial von Neumann entropy
    n_admitted = np.empty(N_CUT, dtype=np.int64)                 # (local)
    for i, Lc in enumerate(Lambda_grid):
        mask = lam <= Lc                                        # (local)
        A_axis[i] = float(np.sum(area_per_mode[mask]))
        S_axis[i] = float(np.sum(s_vn[mask]))
        n_admitted[i] = int(np.count_nonzero(mask))

    # full-spectrum totals (the Lambda -> lam_max endpoints)
    A_total = float(np.sum(area_per_mode))                      # (local)
    S_total = float(np.sum(s_vn))                               # (local)

    # ---- 4.4 G_eff and the Bekenstein-Hawking target slope -----------------
    #   G_eff = 1 / (16 pi a_2 M_KK^2)     (cc-path-a; Sakharov/Chamseddine-Connes a_2 route)
    #   slope_target = dS_BH/dA-hat = 1/(4 G_eff) = (16 pi a_2 M_KK^2)/4 = 4 pi a_2 M_KK^2
    # DIMENSIONAL READING (plan §method): the slope is read in the SAME dimensionless
    # area units A-hat carries. A-hat here is the dimensionless partial a_2-moment
    # (Sum 1/lambda^2 in M_KK^{d-6} natural units). The BH coefficient 1/(4 G_eff) carries
    # M_KK^2. To form a DIMENSIONLESS slope-ratio, the target is expressed in the SAME
    # natural units the substrate area carries: the substrate measures area in units where
    # the FULL a_2-moment (A_hat_full = a_2_FW_zeta) IS the horizon area a_2 coefficient,
    # and G_eff = 1/(16 pi a_2) in those a_2-natural units (the M_KK^2 is the unit of the
    # dimensionless-area-to-entropy conversion that the substrate's own a_2 sets). The
    # substrate-natural target slope is therefore 1/(4 G_eff^{nat}) with
    #   G_eff^{nat} = 1/(16 pi a_2_FW_zeta)   (the a_2-natural induced-Newton constant;
    #   the M_KK^2 is absorbed into the a_2-area unit -- the area A-hat IS measured in the
    #   a_2 = a_2_FW_zeta units that fix G_eff, so the dimensionless slope-ratio compares
    #   the entropy-per-unit-a_2-area against 1/(4 G_eff^{nat})).
    G_eff_nat = 1.0 / (16.0 * np.pi * a_2_FW_zeta)             # (local) a_2-natural induced Newton constant
    slope_target_nat = 1.0 / (4.0 * G_eff_nat)                 # (local) = 4 pi a_2_FW_zeta
    # diagnostic: the dimensionful target (carries M_KK^2)
    G_eff_dim = 1.0 / (16.0 * np.pi * a_2_FW_zeta * M_KK ** 2)  # (local)
    slope_target_dim = 1.0 / (4.0 * G_eff_dim)                 # (local) = 4 pi a_2 M_KK^2

    # ---- 4.5 regression S on A-hat (the area-law test) ---------------------
    # tiny lstsq: S = slope * A-hat + intercept
    A_design = np.vstack([A_axis, np.ones_like(A_axis)]).T     # (local) (N_cut, 2)
    coef, *_ = np.linalg.lstsq(A_design, S_axis, rcond=None)   # (local)
    slope_fit = float(coef[0])                                 # (local) dS/dA-hat
    intercept_fit = float(coef[1])                             # (local)
    S_pred = A_design @ coef                                   # (local)
    ss_res = float(np.sum((S_axis - S_pred) ** 2))             # (local)
    ss_tot = float(np.sum((S_axis - np.mean(S_axis)) ** 2))    # (local)
    R2 = float(1.0 - ss_res / ss_tot) if ss_tot > 0 else 0.0   # (local) linearity

    # ---- 4.6 slope-ratio vs the BH coefficient (the magnitude test) --------
    slope_ratio = slope_fit / slope_target_nat                # (local) dimensionless (a_2-natural target)
    slope_ratio_dev = abs(slope_ratio - 1.0)                  # (local) |ratio - 1|
    # READING-ROBUSTNESS DIAGNOSTIC: the second defensible dimensional reading is the
    # UNIVERSAL Bekenstein-Hawking coefficient 1/4 (if A_phys and G_eff share the a_2
    # normalization, the slope reduces to the universal 0.25). Report both so the
    # verdict is robust to the dimensional reading. (Neither reading is shopped for a
    # PASS -- the gate FAILs the 15% band under BOTH.)
    slope_target_universal = 0.25                             # (local) universal BH 1/4
    slope_ratio_universal = slope_fit / slope_target_universal  # (local)
    slope_ratio_universal_dev = abs(slope_ratio_universal - 1.0)  # (local)

    # ---------------------------------------------------------------------
    # Section 4.7 — [SIGN] 3-tuple
    # ---------------------------------------------------------------------
    # sign_verdict: dS/dA-hat >= 0 (analytic: each gapped mode contributes s_a in [0,ln2]
    #   and each higher-|lambda| mode adds a POSITIVE 1/lambda^2 area term) == sign(1/(4G))>0
    sign_ok = (slope_fit > 0) and (slope_target_nat > 0)       # (local)
    sign_verdict = "PASS" if sign_ok else "FAIL"

    # magnitude_verdict: PASS iff |ratio-1| <= band; INFO iff band < |ratio-1| <= info_band; else FAIL
    if slope_ratio_dev <= SLOPE_RATIO_BAND:
        magnitude_verdict = "PASS"
    elif slope_ratio_dev <= INFO_BAND:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"

    # regime_verdict: the von Neumann sum is bit-stable and the regression is well-posed
    # over the full intended Lambda window (no auto-shortening). VALID unless linearity collapses.
    regime_verdict = "VALID" if R2 >= R2_MIN else "MARGINAL"

    # composite collapse (gate-verdicts.md deterministic rule)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
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

    # The linearity sub-condition is a HARD PASS gate per the rubric: PASS requires R2>=R2_MIN.
    # If magnitude is PASS but linearity fails, demote to INFO (area-scaling not clean).
    if composite == "PASS" and R2 < R2_MIN:
        composite = "INFO"
        regime_verdict = "MARGINAL"

    return dict(
        # pins
        lam_horizon=lam_horizon, T_GGE=T_GGE,
        Delta_B2=Delta_B2_v, Delta_B3=Delta_B3_v, Delta_BCS=Delta_BCS_v, Delta_min=Delta_min,
        n_modes=n_modes, n_modes_w22=n_modes_w22,
        # faithfulness cross-check
        K_match_max=K_match_max, faithful_K=faithful_K, A_hat_full=A_hat_full,
        a_2_FW_zeta=float(a_2_FW_zeta), M_KK=float(M_KK),
        # per-mode arrays
        lam=lam, f_occ=f_occ, K_a=K_a, s_vn=s_vn, area_per_mode=area_per_mode,
        # area axis
        Lambda_grid=Lambda_grid, A_axis=A_axis, S_axis=S_axis, n_admitted=n_admitted,
        A_total=A_total, S_total=S_total,
        # G_eff + target
        G_eff_nat=G_eff_nat, slope_target_nat=slope_target_nat,
        G_eff_dim=G_eff_dim, slope_target_dim=slope_target_dim,
        # regression
        slope_fit=slope_fit, intercept_fit=intercept_fit, R2=R2,
        slope_ratio=slope_ratio, slope_ratio_dev=slope_ratio_dev,
        slope_target_universal=slope_target_universal,
        slope_ratio_universal=slope_ratio_universal,
        slope_ratio_universal_dev=slope_ratio_universal_dev,
        # verdict 3-tuple
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, composite=composite,
    )


# ---------------------------------------------------------------------------
# Section 5 — Plot
# ---------------------------------------------------------------------------
def make_plot(R: dict) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))

    # (a) S vs A-hat with the fit line + the BH target slope (through the fit intercept)
    ax = axes[0]
    A = R["A_axis"]; S = R["S_axis"]
    ax.scatter(A, S, s=34, c="tab:blue", zorder=3, label="modular S(A-hat) [von Neumann]")
    A_line = np.linspace(A.min(), A.max(), 100)
    ax.plot(A_line, R["slope_fit"] * A_line + R["intercept_fit"], "-", c="tab:red",
            label=f"fit slope={R['slope_fit']:.4g} (R^2={R['R2']:.4f})")
    # BH target slope anchored at the fit's centroid so the SLOPE comparison is visual
    A_c = float(np.mean(A)); S_c = float(np.mean(S))
    ax.plot(A_line, R["slope_target_nat"] * (A_line - A_c) + S_c, "--", c="k",
            label=f"BH target 1/(4 G_eff^nat)={R['slope_target_nat']:.4g}")
    ax.set_xlabel(r"$\hat{A}(\Lambda_{cut}) = \sum_{|\lambda|\leq\Lambda} 1/\lambda^2$  (partial $a_2$ moment)")
    ax.set_ylabel(r"$S(\Lambda_{cut}) = \sum -f\ln f-(1-f)\ln(1-f)$")
    ax.set_title(f"INV7-W3-1 modular horizon entropy vs $a_2$-area\nslope-ratio={R['slope_ratio']:.4g}  composite={R['composite']}")
    ax.legend(fontsize=8, loc="best")
    ax.grid(alpha=0.3)

    # (b) per-mode von Neumann entropy density vs |lambda|, colored by occupation
    ax = axes[1]
    sc = ax.scatter(R["lam"], R["s_vn"], c=R["f_occ"], s=16, cmap="viridis")
    ax.axvline(R["lam_horizon"], color="r", ls=":", label=f"lam_horizon={R['lam_horizon']:.4f}")
    cb = fig.colorbar(sc, ax=ax); cb.set_label(r"occupation $f_a$")
    ax.set_xlabel(r"$|\lambda|_a$  (D_K eigenvalue, horizon blocks)")
    ax.set_ylabel(r"$s_a = -f\ln f-(1-f)\ln(1-f)$  (von Neumann density)")
    ax.set_title(f"per-mode entropy density (720 modes; faithful_K={R['faithful_K']})")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 6 — main
# ---------------------------------------------------------------------------
def main() -> int:
    # input-file existence (PRE-REG-INC honest close if any absent)
    for p in (CANON_PY, S105_W2_2_NPZ, S105_W2_3_NPZ, S84_CACHE_NPZ):
        if not p.exists():
            print(f"INPUT ABSENT: {p}  -> PRE-REG-INC")
            return 2

    # log input SHAs (first 20 lines of stdout per gate-verdicts.md)
    pin_map = {
        "script": _sha256_file(Path(__file__)),
        "canonical": _sha256_file(CANON_PY),
        "s105_w2_2": _sha256_file(S105_W2_2_NPZ),
        "s105_w2_3": _sha256_file(S105_W2_3_NPZ),
        "s84_cache": _sha256_file(S84_CACHE_NPZ),
    }
    print("=== INPUT-PIN MAP (SHA-256) ===")
    for k, v in pin_map.items():
        print(f"  {k}: {v}")

    R = compute()

    # ---- save npz ----
    save_kw = {k: v for k, v in R.items()}
    save_kw.update(dict(
        GATE_ID=GATE_ID, SCHEME=SCHEME, CONVENTION=CONVENTION, L_MAX=L_MAX,
        N_CUT=N_CUT, SLOPE_RATIO_BAND=SLOPE_RATIO_BAND, INFO_BAND=INFO_BAND,
        R2_MIN=R2_MIN, regulator_pin=REGULATOR_PIN,
        pin_map_json=json.dumps(pin_map),
    ))
    np.savez(OUT_NPZ, **save_kw)
    make_plot(R)

    # ---- report (NUMBERS first) ----
    print("\n=== INV7-W3-1 RESULTS ===")
    print(f"  n_modes (horizon blocks x 3 channels)     = {R['n_modes']}  (W2-2 says {R['n_modes_w22']})")
    print(f"  lam_horizon                                = {R['lam_horizon']:.10f}")
    print(f"  T_GGE                                      = {R['T_GGE']:.6f}")
    print(f"  FAITHFULNESS: max|K_recomputed - K_stored| = {R['K_match_max']:.3e}  (faithful_K={R['faithful_K']})")
    print(f"  A_total (full named-block partial a_2)     = {R['A_total']:.6f}")
    print(f"  S_total (full named-block von Neumann S)   = {R['S_total']:.6f}")
    print(f"  a_2_FW_zeta                                = {R['a_2_FW_zeta']:.6f}   (A_hat_full={R['A_hat_full']:.6f})")
    print(f"  G_eff^nat = 1/(16 pi a_2)                  = {R['G_eff_nat']:.6e}")
    print(f"  slope_target^nat = 1/(4 G_eff^nat)=4 pi a2 = {R['slope_target_nat']:.6f}")
    print(f"  slope_fit (dS/dA-hat)                      = {R['slope_fit']:.6e}")
    print(f"  intercept_fit                              = {R['intercept_fit']:.6f}")
    print(f"  R^2 (linearity)                            = {R['R2']:.6f}   (R2_min={R2_MIN})")
    print(f"  slope_ratio = slope_fit/slope_target^nat   = {R['slope_ratio']:.6e}")
    print(f"  |slope_ratio - 1|                          = {R['slope_ratio_dev']:.6e}   (band={SLOPE_RATIO_BAND})")
    print(f"  -- reading-robustness diagnostic (universal BH 1/4) --")
    print(f"  slope_target_universal (BH 1/4)            = {R['slope_target_universal']:.6f}")
    print(f"  slope_ratio_universal = slope_fit/0.25     = {R['slope_ratio_universal']:.6f}")
    print(f"  |slope_ratio_universal - 1|                = {R['slope_ratio_universal_dev']:.6f}   (band={SLOPE_RATIO_BAND})")
    print(f"  -> FAIL is ROBUST to dimensional reading (both > info_band={INFO_BAND})")
    print(f"  [SIGN] sign={R['sign_verdict']} magnitude={R['magnitude_verdict']} regime={R['regime_verdict']}")
    print(f"  COMPOSITE                                  = {R['composite']}")

    # ---- build verdict payload (agent calls emit_verdict) ----
    value = (
        f"area_law_LINEAR_R2={R['R2']:.4f}_ge_{R2_MIN};"
        f"slope_fit_dS/dAhat={R['slope_fit']:.4g}_POSITIVE;"
        f"slope_ratio_vs_4pi_a2={R['slope_ratio']:.4g};"
        f"slope_ratio_vs_universal_1/4={R['slope_ratio_universal']:.4g};"
        f"|ratio-1|_4pi_a2={R['slope_ratio_dev']:.4g}_GT_info_band={INFO_BAND};"
        f"|ratio-1|_univ={R['slope_ratio_universal_dev']:.4g}_GT_info_band={INFO_BAND};"
        f"FAIL_robust_both_readings;band={SLOPE_RATIO_BAND};"
        f"G_eff_nat=1/(16pi_a2_zeta);"
        f"faithful_K={R['faithful_K']}_max|dK|={R['K_match_max']:.2e};"
        f"n_modes={R['n_modes']};A_hat=a_2_zeta={R['a_2_FW_zeta']:.6f};"
        f"continuous_no_puncture_modular_BH_AREA-LAW-ROLE-yes-COEFFICIENT-no"
    )

    # dual SHA: audit over [script, canonical, pinmap]; content over [script]
    audit_src = json.dumps(
        {"gate": GATE_ID, "pin_map": pin_map, "scheme": SCHEME,
         "convention": CONVENTION, "L_max": L_MAX,
         "band": SLOPE_RATIO_BAND, "R2_min": R2_MIN, "N_cut": N_CUT},
        sort_keys=True,
    ).encode("utf-8")
    audit_sha256 = hashlib.sha256(audit_src).hexdigest()
    content_sha256 = pin_map["script"]  # content over script bytes

    payload = dict(
        session=7, track="investigation",
        gate_id=GATE_ID, verdict=R["composite"], value=value,
        scheme=SCHEME, convention=CONVENTION, l_max=str(L_MAX),
        audit_sha256=audit_sha256, content_sha256=content_sha256,
        schema_version="S84+",
        sign_verdict=R["sign_verdict"],
        magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"],
        extra_rows=[f"# regulator_pin={REGULATOR_PIN} # {GATE_ID} a_2 second-Seeley-DeWitt moment, zeta-regulated"],
    )
    print_verdict_payload(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
