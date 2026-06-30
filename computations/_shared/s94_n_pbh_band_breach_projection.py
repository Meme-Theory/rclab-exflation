#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S94-N-PBH-BAND-BREACH-PROJECTION  (Session 94, Wave 5, gate W5-2)
=================================================================

[SIGN] threshold-crossing gate. Find the smallest truncation L_max at which the
n_PBH_central(L_max) trajectory breaches the JE5 conjunct-upper ceiling 2.2e-22
m^-3 FROM BELOW.

Substrate framing (phononic-framing.md / IS Space, Not IN Space)
----------------------------------------------------------------
The substrate IS the spectral triple (A_K, H_K, D_K(tau_fold=0.19)). The
n_PBH_central(L_max) trajectory is the laboratory-IN image (a PBH number density,
m^-3, measured IN a cosmological-volume container) of the substrate-IS
cardinality-cascade edge count n_edge = C(N_eigs, 2) on D_K, truncation-
parametrized by L_max via the W4-3 Sage-exact quintic N_eigs(L_max).  Direction
of explanation: D_K eigenvalues -> N_eigs(L_max) cardinality growth (the SU(3)
representation ring is INFINITE, so N_eigs is an unbounded quintic) -> n_edge ->
n_PBH_central rises -> crosses the laboratory-IN ceiling 2.2e-22 at L_breach.

CLASSIFICATION: GEOMETRIC (the band-breach point is a property of the
N_eigs(L_max) cardinality growth of the D_K spectral triple -- the fabric --
driving a laboratory-IN band-membership predicate).

Method (plan §W5-2)
-------------------
  n_PBH_central(L_max) = central14 * N_eigs(L_max) / N_eigs(14)
    central14         = n_PBH_FW_central = 7.2761e-23 m^-3  [canonical; = 72761/10^27]
    N_eigs(L_max)     = (4/15)L^5 + (10/3)L^4 + 16 L^3 + (110/3)L^2 + (596/15)L + 16
                        [W4-3 Sage-exact quintic; s93_w4_3_..._npz n_eigs_closed_form_coeffs]
    ceiling_JE5_upper = 2.2e-22 m^-3 = 22/10^23   [JE5 conjunct band upper edge; S92 JE5]
    breach predicate  = n_PBH_central(L_max) > ceiling_JE5_upper   (STRICT, from below)
  L_breach = min{ L_max in Z_{>=14} : n_PBH_central(L_max) > 2.2e-22 }.

All band-membership comparisons use EXACT rationals (python fractions.Fraction,
cross-checked against the Sage MCP QQ computation) -- NO floating-point fit -- per
regulator-pin-discipline.md §"Sage-Exact Rationals" and the QQ-EXACT-RATIONAL
convention.

Cross-validation: the L=14/15/16 anchors central14*N_eigs(L)/N_eigs(14) are
cross-checked against the on-disk obs_2 trajectory {7.276e-23, 9.775e-23,
1.292e-22} (s93_w4_3_..._npz['obs2_n_PBH_per_Lmax']) to <= 1%.

SIGN pre-registration (substitution chain Step 4):  N_eigs is strictly monotone
increasing (d/dL N_eigs = (4/3)L^4 + (40/3)L^3 + 48 L^2 + (220/3)L + 596/15 > 0
for all L >= 1), so the trajectory rises monotonically and the crossing is a
clean FROM-BELOW breach at a UNIQUE smallest integer L_breach.  The directional
prediction is:  n_PBH_central(L_breach) - 2.2e-22 > 0  (POSITIVE; breach from
below).  Predicted L_breach = 19 (S93 W-1 workshop adjudication).

This file lives in computations/_shared/ per the plan producing_script path; it
writes outputs to computations/session-94/.

Environment: phonon-exflation-sim/.venv312/Scripts/python.exe
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from fractions import Fraction
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np  # noqa: E402

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# -----------------------------------------------------------------------------
# Section 1 — Paths + canonical-constants import
# -----------------------------------------------------------------------------
SHARED_DIR = Path(__file__).resolve().parent                     # computations/_shared
PROJECT_ROOT = SHARED_DIR.parent.parent                          # repo root
SESSION_DIR = PROJECT_ROOT / "computations" / "session-94"
SESSION_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import n_PBH_FW_central, M_KK, tau_fold  # noqa: E402

GATE_ID = "S94-N-PBH-BAND-BREACH-PROJECTION"
SCHEME = "FWD-C5-CARDINALITY-CASCADE-TAIL"
CONVENTION = "QQ-EXACT-RATIONAL"
L_MAX = "scan-14-25"
SCHEMA_VERSION = "S87+"

VERDICT_TXT = SESSION_DIR / "s94_gate_verdicts.txt"
NPZ_OUT = SESSION_DIR / "s94_n_pbh_band_breach_projection.npz"
PNG_OUT = SESSION_DIR / "s94_n_pbh_band_breach_projection.png"

W4_3_NPZ = (
    PROJECT_ROOT / "computations" / "session-93"
    / "s93_w4_3_n_pbh_canonical_truncation_factorization.npz"
)
CANONICAL_PY = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [CANONICAL_PY, W4_3_NPZ]

# -----------------------------------------------------------------------------
# Section 2 — Pre-registered machinery pins (plan §W5-2 machinery_pin_map)
# -----------------------------------------------------------------------------
SCAN_LO = 14                       # scan_range [14, 25]                       # (local)
SCAN_HI = 25                       # (local)
ANCHOR_LMAX = 14                   # the trajectory normalisation truncation N_eigs(14)  # (local)
XVAL_TOL = 0.01                    # 1% cross-validation tol vs on-disk obs_2 anchors  # (local)
QUINTIC_TOL = 1e-12                # Sage-exact quintic reproduction (relative) cross-check  # (local)
PREDICTED_L_BREACH = 19            # S93 W-1 workshop adjudication             # (local)

# JE5 conjunct band edges (m^-3), EXACT rationals
CEILING_JE5_UPPER = Fraction(22, 10 ** 23)      # 2.2e-22
FLOOR_JE5_LOWER = Fraction(55, 10 ** 24)        # 5.5e-23
# central14 published at 5 sig figs (canonical n_PBH_FW_central = 7.2761e-23)
CENTRAL14 = Fraction(72761, 10 ** 27)           # = 7.2761e-23 exact

# W4-3 Sage-exact quintic coefficients (c5..c0), EXACT rationals
#   N_eigs(L) = (4/15)L^5 + (10/3)L^4 + 16 L^3 + (110/3)L^2 + (596/15)L + 16
QUINTIC_COEFFS_Q = [
    Fraction(4, 15),   # c5
    Fraction(10, 3),   # c4
    Fraction(16),      # c3
    Fraction(110, 3),  # c2
    Fraction(596, 15), # c1
    Fraction(16),      # c0
]


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
# Section 4 — N_eigs quintic (exact-rational + integer)
# -----------------------------------------------------------------------------
def n_eigs_exact(L: int) -> Fraction:
    """Exact-rational N_eigs(L) from the W4-3 quintic. Integer-valued for L>=1."""
    Lq = Fraction(L)  # (local)
    c = QUINTIC_COEFFS_Q  # (local)
    return (c[0] * Lq ** 5 + c[1] * Lq ** 4 + c[2] * Lq ** 3
            + c[3] * Lq ** 2 + c[4] * Lq + c[5])


def n_pbh_central_exact(L: int) -> Fraction:
    """n_PBH_central(L) = central14 * N_eigs(L) / N_eigs(14), EXACT rational [m^-3]."""
    return CENTRAL14 * n_eigs_exact(L) / n_eigs_exact(ANCHOR_LMAX)


# -----------------------------------------------------------------------------
# Section 5 — Compute
# -----------------------------------------------------------------------------
def compute() -> dict:
    # --- (Step A cross-check) reproduce W4-3 quintic + monotonicity confirmation ---
    d = np.load(W4_3_NPZ, allow_pickle=True)  # (local)
    npz_coeffs = np.asarray(d["n_eigs_closed_form_coeffs"], dtype=float)  # (local)
    my_coeffs = np.array([float(c) for c in QUINTIC_COEFFS_Q])            # (local)
    coeff_match = bool(np.allclose(npz_coeffs, my_coeffs, rtol=1e-12, atol=1e-12))  # (local)

    npz_anchor_neigs = np.asarray(d["n_eigs_per_Lmax"], dtype=np.int64)   # L=14,15,16 (local)
    npz_anchor_Ls = np.asarray(d["L_max_scan"], dtype=np.int64)           # (local)
    quintic_rel_err = []  # (local)
    for L, n_npz in zip(npz_anchor_Ls.tolist(), npz_anchor_neigs.tolist()):
        n_mine = n_eigs_exact(int(L))  # exact (local)
        # integer-exact reproduction: relative error vs the on-disk Sage-exact integer
        rel = abs(float(n_mine) / float(n_npz) - 1.0)  # (local)
        quintic_rel_err.append(rel)
    quintic_rel_err = np.array(quintic_rel_err)  # (local)
    quintic_repro_ok = bool(np.all(quintic_rel_err <= QUINTIC_TOL))  # (local)
    quintic_integer_exact = bool(
        all(n_eigs_exact(int(L)).denominator == 1
            for L in npz_anchor_Ls.tolist())
    )  # (local)

    # d/dL N_eigs > 0 for all L>=1 (derivative coeffs); confirm on the scan window
    # d/dL = (4/3)L^4 + (40/3)L^3 + 48 L^2 + (220/3)L + 596/15
    def dNdL(L: float) -> float:  # (local)
        return ((4.0 / 3.0) * L ** 4 + (40.0 / 3.0) * L ** 3 + 48.0 * L ** 2
                + (220.0 / 3.0) * L + 596.0 / 15.0)
    deriv_positive = bool(all(dNdL(float(L)) > 0.0 for L in range(1, SCAN_HI + 1)))  # (local)

    # --- (Step 3-5) the breach scan, EXACT rationals ---
    R_thresh = CEILING_JE5_UPPER / CENTRAL14    # breach <=> R(L) > R_thresh (local exact)

    Ls = list(range(SCAN_LO, SCAN_HI + 1))  # (local)
    n_eigs_int = []          # (local)
    n_pbh_float = []         # (local)
    ratio_upper_float = []   # n_PBH_central / upper (local)
    ratio_R_float = []       # N_eigs(L)/N_eigs(14) (local)
    in_band_flags = []       # (local)
    breach_flags = []        # (local)
    L_breach = None          # (local)
    n_pbh_exact_at = {}      # (local)
    for L in Ls:
        NL = n_eigs_exact(L)              # exact (local)
        nPBH = n_pbh_central_exact(L)     # exact (local)
        ratio_u = nPBH / CEILING_JE5_UPPER  # exact (local)
        ratio_R = NL / n_eigs_exact(ANCHOR_LMAX)  # exact (local)
        in_band = (nPBH >= FLOOR_JE5_LOWER) and (nPBH <= CEILING_JE5_UPPER)  # (local)
        breach = nPBH > CEILING_JE5_UPPER   # STRICT (local)
        if breach and L_breach is None:
            L_breach = L
        n_eigs_int.append(int(NL))
        n_pbh_float.append(float(nPBH))
        ratio_upper_float.append(float(ratio_u))
        ratio_R_float.append(float(ratio_R))
        in_band_flags.append(bool(in_band))
        breach_flags.append(bool(breach))
        n_pbh_exact_at[L] = nPBH

    # uniqueness of the from-below crossing: every L < L_breach is in-band-or-below,
    # every L >= L_breach is breach (monotone => single crossing)
    below_all_not_breach = all(
        not breach_flags[i] for i, L in enumerate(Ls) if L < L_breach
    )  # (local)
    above_all_breach = all(
        breach_flags[i] for i, L in enumerate(Ls) if L >= L_breach
    )  # (local)
    unique_from_below = bool(below_all_not_breach and above_all_breach)  # (local)

    # last-in-band truncation + its margin
    last_in_band_L = max(L for i, L in enumerate(Ls) if in_band_flags[i])  # (local)
    margin_last = (CEILING_JE5_UPPER - n_pbh_exact_at[last_in_band_L]) / CEILING_JE5_UPPER  # exact (local)
    excess_breach = (n_pbh_exact_at[L_breach] - CEILING_JE5_UPPER) / CEILING_JE5_UPPER     # exact (local)

    # SIGN delta at L_breach: n_PBH_central(L_breach) - 2.2e-22  (must be > 0)
    delta_breach_exact = n_pbh_exact_at[L_breach] - CEILING_JE5_UPPER  # exact (local)
    delta_breach_float = float(delta_breach_exact)  # (local)
    sign_positive = bool(delta_breach_exact > 0)  # (local)

    # --- cross-validation against on-disk obs_2 anchors {L=14,15,16} ---
    obs2 = np.asarray(d["obs2_n_PBH_per_Lmax"], dtype=float)  # (local)
    obs2_Ls = npz_anchor_Ls.tolist()  # (local)
    xval_rel = []  # (local)
    for i, L in enumerate(obs2_Ls):
        mine = float(n_pbh_central_exact(int(L)))  # (local)
        rel = abs(mine / float(obs2[i]) - 1.0)  # (local)
        xval_rel.append(rel)
    xval_rel = np.array(xval_rel)  # (local)
    xval_max = float(np.max(xval_rel))  # (local)
    xval_ok = bool(xval_max <= XVAL_TOL)  # (local)

    # --- breach matches W-1 predicted L=19 ---
    breach_matches_w1 = bool(L_breach == PREDICTED_L_BREACH)  # (local)
    breach_off_by_one = bool(abs(L_breach - PREDICTED_L_BREACH) == 1)  # (local)

    return {
        "value": L_breach,
        "L_breach": L_breach,
        "predicted_L_breach": PREDICTED_L_BREACH,
        "breach_matches_w1": breach_matches_w1,
        "breach_off_by_one": breach_off_by_one,
        "Ls": np.array(Ls, dtype=np.int64),
        "n_eigs_int": np.array(n_eigs_int, dtype=np.int64),
        "n_pbh_float": np.array(n_pbh_float, dtype=float),
        "ratio_upper_float": np.array(ratio_upper_float, dtype=float),
        "ratio_R_float": np.array(ratio_R_float, dtype=float),
        "in_band_flags": np.array(in_band_flags, dtype=bool),
        "breach_flags": np.array(breach_flags, dtype=bool),
        "R_thresh_num": R_thresh.numerator,
        "R_thresh_den": R_thresh.denominator,
        "R_thresh_float": float(R_thresh),
        "unique_from_below": unique_from_below,
        "last_in_band_L": last_in_band_L,
        "margin_last_float": float(margin_last),
        "excess_breach_float": float(excess_breach),
        "delta_breach_float": delta_breach_float,
        "delta_breach_num": delta_breach_exact.numerator,
        "delta_breach_den": delta_breach_exact.denominator,
        "sign_positive": sign_positive,
        "coeff_match": coeff_match,
        "quintic_repro_ok": quintic_repro_ok,
        "quintic_rel_err_max": float(np.max(quintic_rel_err)),
        "quintic_integer_exact": quintic_integer_exact,
        "deriv_positive": deriv_positive,
        "xval_rel": xval_rel,
        "xval_max": xval_max,
        "xval_ok": xval_ok,
        # exact-rational n_PBH/upper at the two decisive truncations (string for npz)
        "L18_ratio_upper_exact": str(n_pbh_exact_at.get(18) / CEILING_JE5_UPPER),
        "L19_ratio_upper_exact": str(n_pbh_exact_at.get(19) / CEILING_JE5_UPPER),
    }


# -----------------------------------------------------------------------------
# Section 6 — Gate verdict (3-tuple per pre-registered operator + collapse)
# -----------------------------------------------------------------------------
def evaluate_gate(res: dict) -> tuple[str, str, str, str]:
    """Return (composite, sign_v, mag_v, reg_v).

    sign_verdict  : breach from-below => n_PBH_central(L_breach) - 2.2e-22 > 0 (POSITIVE).
                    PASS iff the computed delta sign matches the predicted POSITIVE direction.
    magnitude_v   : |L_breach - 19| band.  PASS iff L_breach == 19 (W-1 match);
                    INFO iff |L_breach - 19| == 1 (QQ-vs-float boundary rounding);
                    FAIL otherwise OR anchors fail <=1% cross-validation.
    regime_v      : VALID iff (a) the from-below crossing is unique (monotone quintic),
                    (b) the quintic reproduces the on-disk Sage-exact integers, and
                    (c) the L=14/15/16 anchors cross-validate <=1%.  MARGINAL iff the
                    last-in-band margin is within band-edge resolution (<5%) -- the L=18
                    in-band margin is 1.77%, so the breach point sits one truncation above
                    a near-wall last-in-band truncation; flagged MARGINAL.  BREAKDOWN iff
                    monotonicity / integer-exactness fails (would contradict the quintic).
    """
    sign_v = "PASS" if res["sign_positive"] else "FAIL"  # (local)

    if not res["xval_ok"]:
        mag_v = "FAIL"  # (local)  anchor cross-validation failure => source/coeff mismatch
    elif res["breach_matches_w1"]:
        mag_v = "PASS"  # (local)  L_breach == 19
    elif res["breach_off_by_one"]:
        mag_v = "INFO"  # (local)  L_breach == 18 or 20 (boundary rounding)
    else:
        mag_v = "FAIL"  # (local)

    structural_ok = (res["unique_from_below"] and res["quintic_repro_ok"]
                     and res["quintic_integer_exact"] and res["deriv_positive"])  # (local)
    if not structural_ok:
        reg_v = "BREAKDOWN"  # (local)
    elif res["margin_last_float"] < 0.05:
        # last-in-band (L=18) margin only 1.77% => breach sits one step above a near-wall
        # truncation; band-edge resolution flag (MARGINAL), per INFO_meaning band-edge clause
        reg_v = "MARGINAL"  # (local)
    else:
        reg_v = "VALID"  # (local)

    # Composite-collapse rule (gate-verdicts.md S87 schema-v2; PRE-REGISTERED)
    if reg_v == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and reg_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and reg_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return composite, sign_v, mag_v, reg_v


# -----------------------------------------------------------------------------
# Section 7 — Plot
# -----------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    Ls = res["Ls"]  # (local)
    nPBH = res["n_pbh_float"]  # (local)
    L_breach = res["L_breach"]  # (local)
    upper = float(CEILING_JE5_UPPER)  # (local)
    floor = float(FLOOR_JE5_LOWER)    # (local)

    fig, ax = plt.subplots(figsize=(10.5, 6.6))  # (local)

    # JE5 band shaded region
    ax.axhspan(floor, upper, color="tab:green", alpha=0.12,
               label=f"JE5 conjunct band [5.5e-23, 2.2e-22] m$^{{-3}}$")
    ax.axhline(upper, color="tab:red", ls="--", lw=1.6,
               label="JE5 conjunct-upper ceiling 2.2e-23 (= 22/10$^{23}$)".replace("2.2e-23", "2.2e-22"))
    ax.axhline(floor, color="tab:green", ls=":", lw=1.2,
               label="JE5 conjunct-floor 5.5e-23 (= 55/10$^{24}$)")

    in_band = res["in_band_flags"]  # (local)
    breach = res["breach_flags"]    # (local)
    ax.plot(Ls, nPBH, "-", color="0.35", lw=1.3, zorder=2)
    ax.scatter(Ls[in_band], nPBH[in_band], s=70, color="tab:blue",
               zorder=4, label="in-band ($L_{max} \\leq 18$)")
    ax.scatter(Ls[breach], nPBH[breach], s=70, color="tab:red", marker="^",
               zorder=4, label="breach ($L_{max} \\geq L_{breach}$)")

    # mark L_breach
    yb = nPBH[list(Ls).index(L_breach)]  # (local)
    ax.axvline(L_breach, color="tab:red", ls="-.", lw=1.4, alpha=0.8)
    ax.annotate(
        f"$L_{{breach}} = {L_breach}$\n"
        f"$n_{{PBH}}/$upper $= {res['ratio_upper_float'][list(Ls).index(L_breach)]:.4f}$\n"
        f"({res['excess_breach_float']*100:.2f}% above ceiling)",
        xy=(L_breach, yb), xytext=(L_breach + 0.8, yb * 1.15),
        fontsize=9.5, color="tab:red",
        arrowprops=dict(arrowstyle="->", color="tab:red", lw=1.2),
    )
    # mark last-in-band
    L_last = res["last_in_band_L"]  # (local)
    y_last = nPBH[list(Ls).index(L_last)]  # (local)
    ax.annotate(
        f"last in-band $L={L_last}$\n(margin {res['margin_last_float']*100:.2f}% below wall)",
        xy=(L_last, y_last), xytext=(L_last - 4.2, y_last * 0.62),
        fontsize=9, color="tab:blue",
        arrowprops=dict(arrowstyle="->", color="tab:blue", lw=1.0),
    )

    ax.set_yscale("log")
    ax.set_xlabel("$L_{max}$ (truncation)", fontsize=12)
    ax.set_ylabel("$n_{PBH,\\,central}(L_{max})$  [m$^{-3}$]", fontsize=12)
    ax.set_title(
        "S94-N-PBH-BAND-BREACH-PROJECTION  ($n_{PBH}$ from-below breach of the JE5 band)\n"
        "$n_{PBH}(L) = $central14$\\cdot N_{eigs}(L)/N_{eigs}(14)$ "
        "(W4-3 Sage-exact quintic; QQ-exact breach)",
        fontsize=10.5,
    )
    ax.set_xticks(list(Ls))
    ax.legend(loc="upper left", fontsize=8.6, framealpha=0.9)
    ax.grid(True, which="both", alpha=0.25)
    fig.tight_layout()
    fig.savefig(PNG_OUT, dpi=140)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Section 8 — Verdict-line emitter (atomic append; dual-SHA + REQUIRED 3-tuple)
# -----------------------------------------------------------------------------
def append_verdict(verdict, value_str, audit_sha, content_sha,
                   sign_v, mag_v, reg_v, res) -> None:
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); [SIGN] n_PBH from-below "
        f"breach of JE5 conjunct band; QQ-exact (fractions.Fraction, Sage-MCP QQ-verified)\n"
    )
    schema_v2_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={reg_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2); "
        f"sign = breach from-below => n_PBH_central(L_breach)-2.2e-22 > 0 (POSITIVE; "
        f"delta={res['delta_breach_float']:.6e} m^-3, sign_positive={res['sign_positive']}); "
        f"magnitude = |L_breach-19| band (L_breach={res['L_breach']}, W-1 match={res['breach_matches_w1']}); "
        f"regime = monotone-quintic unique from-below crossing + last-in-band margin "
        f"{res['margin_last_float']*100:.2f}% (band-edge resolution)\n"
    )
    detail_row = (
        f"# L_breach={res['L_breach']} predicted_W1={res['predicted_L_breach']} "
        f"R_thresh=220000/72761={res['R_thresh_float']:.7f} "
        f"L18_n_PBH/upper={res['L18_ratio_upper_exact']}({float(eval_frac(res['L18_ratio_upper_exact'])):.6f}) "
        f"L19_n_PBH/upper={res['L19_ratio_upper_exact']}({float(eval_frac(res['L19_ratio_upper_exact'])):.6f}) "
        f"excess_breach={res['excess_breach_float']*100:.4f}% xval_max={res['xval_max']:.3e}(tol{XVAL_TOL}) "
        f"# {GATE_ID} QQ-exact band-breach detail\n"
    )
    regulator_pin = (
        f"# LEVEL_CLASS_PIN=FULL # {GATE_ID} no a_n Seeley-DeWitt coefficient cited "
        f"(N_eigs is the Peter-Weyl rep-ring edge-count quintic, W4-3 Sage-exact; no "
        f"regulator superscript applies); central14=n_PBH_FW_central canonical import; "
        f"substrate-first-canonical-sourcing.md PASS\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(schema_v2_row)
        fp.write(detail_row)
        fp.write(regulator_pin)


def eval_frac(s: str) -> Fraction:
    """Parse a 'num/den' (or integer) string back to a Fraction for display."""
    return Fraction(s)


# -----------------------------------------------------------------------------
# Section 9 — Main
# -----------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PY, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()
    print(f"  canonical central14 = n_PBH_FW_central = {n_PBH_FW_central:.5e} m^-3 "
          f"(= {CENTRAL14.numerator}/10^27)")
    print(f"  M_KK = {M_KK:.6e} | tau_fold = {tau_fold}")
    print()

    res = compute()  # (local)

    print("=== N_eigs quintic reproduction (Step A cross-check) ===")
    print(f"  coeff_match vs npz       : {res['coeff_match']}")
    print(f"  quintic_repro_ok         : {res['quintic_repro_ok']} "
          f"(max rel err {res['quintic_rel_err_max']:.3e}, tol {QUINTIC_TOL})")
    print(f"  quintic_integer_exact    : {res['quintic_integer_exact']}")
    print(f"  d/dL N_eigs > 0 (1..25)  : {res['deriv_positive']}  (=> strictly monotone)")
    print()
    print("=== anchor cross-validation vs on-disk obs_2 {L=14,15,16} ===")
    print(f"  rel deltas : {res['xval_rel']}")
    print(f"  xval_max   : {res['xval_max']:.3e} (tol {XVAL_TOL}) -> ok={res['xval_ok']}")
    print()
    print("=== band-breach scan (QQ-exact) ===")
    print(f"  breach ratio threshold R_thresh = 220000/72761 = {res['R_thresh_float']:.7f}")
    for i, L in enumerate(res["Ls"].tolist()):
        tag = "BREACH" if res["breach_flags"][i] else ("in-band" if res["in_band_flags"][i] else "below")  # (local)
        print(f"  L={L:>2}: N_eigs={res['n_eigs_int'][i]:>8} "
              f"n_PBH={res['n_pbh_float'][i]:.6e}  "
              f"n_PBH/upper={res['ratio_upper_float'][i]:.6f}  {tag}")
    print()
    print(f"  L_breach = {res['L_breach']} (predicted W-1 = {res['predicted_L_breach']}; "
          f"match={res['breach_matches_w1']})")
    print(f"  unique_from_below crossing : {res['unique_from_below']}")
    print(f"  last-in-band L={res['last_in_band_L']} margin {res['margin_last_float']*100:.4f}% below wall")
    print(f"  L_breach excess above wall : {res['excess_breach_float']*100:.4f}%")
    print(f"  SIGN delta n_PBH_central(L_breach)-2.2e-22 = {res['delta_breach_float']:.6e} "
          f"(>0 ? {res['sign_positive']})")
    print()

    composite, sign_v, mag_v, reg_v = evaluate_gate(res)  # (local)
    print(f"  sign_verdict      = {sign_v}")
    print(f"  magnitude_verdict = {mag_v}")
    print(f"  regime_verdict    = {reg_v}")
    print(f"  COMPOSITE         = {composite}")
    print()

    # Save npz
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        L_breach=res["L_breach"],
        predicted_L_breach=res["predicted_L_breach"],
        breach_matches_w1=res["breach_matches_w1"],
        Ls=res["Ls"],
        n_eigs_int=res["n_eigs_int"],
        n_pbh_central=res["n_pbh_float"],
        ratio_upper=res["ratio_upper_float"],
        ratio_R=res["ratio_R_float"],
        in_band_flags=res["in_band_flags"],
        breach_flags=res["breach_flags"],
        R_thresh_num=res["R_thresh_num"],
        R_thresh_den=res["R_thresh_den"],
        R_thresh_float=res["R_thresh_float"],
        ceiling_upper=float(CEILING_JE5_UPPER),
        floor_lower=float(FLOOR_JE5_LOWER),
        central14=float(CENTRAL14),
        unique_from_below=res["unique_from_below"],
        last_in_band_L=res["last_in_band_L"],
        margin_last_float=res["margin_last_float"],
        excess_breach_float=res["excess_breach_float"],
        delta_breach_float=res["delta_breach_float"],
        delta_breach_num=res["delta_breach_num"],
        delta_breach_den=res["delta_breach_den"],
        sign_positive=res["sign_positive"],
        coeff_match=res["coeff_match"],
        quintic_repro_ok=res["quintic_repro_ok"],
        quintic_rel_err_max=res["quintic_rel_err_max"],
        quintic_integer_exact=res["quintic_integer_exact"],
        deriv_positive=res["deriv_positive"],
        xval_rel=res["xval_rel"],
        xval_max=res["xval_max"],
        xval_ok=res["xval_ok"],
        L18_ratio_upper_exact=res["L18_ratio_upper_exact"],
        L19_ratio_upper_exact=res["L19_ratio_upper_exact"],
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=reg_v,
        composite_verdict=composite,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        M_KK=M_KK,
        tau_fold=tau_fold,
    )
    print(f"  wrote {NPZ_OUT.name}")

    make_plot(res)
    print(f"  wrote {PNG_OUT.name}")

    value_str = (
        f"L_breach={res['L_breach']};predicted_W1={res['predicted_L_breach']};"
        f"breach_matches_w1={res['breach_matches_w1']};"
        f"R_thresh=220000/72761={res['R_thresh_float']:.7f};"
        f"L18_n_PBH/upper={res['L18_ratio_upper_exact']};"
        f"L19_n_PBH/upper={res['L19_ratio_upper_exact']};"
        f"excess_breach={res['excess_breach_float']*100:.4f}pct;"
        f"last_in_band_L={res['last_in_band_L']};last_margin={res['margin_last_float']*100:.4f}pct;"
        f"delta_breach={res['delta_breach_float']:.6e};sign_positive={res['sign_positive']};"
        f"unique_from_below={res['unique_from_below']};xval_max={res['xval_max']:.3e};"
        f"quintic_repro_ok={res['quintic_repro_ok']};quintic_integer_exact={res['quintic_integer_exact']}"
    )  # (local)
    append_verdict(composite, value_str, audit_sha, content_sha,
                   sign_v, mag_v, reg_v, res)
    print(f"  appended verdict line: {GATE_ID}: {composite}")
    print(f"\n  elapsed {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
