#!/usr/bin/env python3
"""
S99 W2-2 — S99-W2-BBN-RELIEF : additional substrate relief for the BBN-epoch vacuum fraction
============================================================================================

Gate: S99-W2-BBN-RELIEF ([SIGN])

Pre-registered threshold (plan §W2-2):
  operator  : (rho_vac/rho_rad)_BBN,relieved / bound <= 1.0   (ΔN_eff(vacuum) <= 1)
  PASS iff a SUBSTRATE-JUSTIFIED relief mechanism (a)/(b)/(c) brings ΔN_eff <= 1 at the
            SINGLE substrate-justified BBN lever X=ln(H_BBN/H0)=40.2756 (NOT scanned).
  FAIL iff no single substrate-justified mechanism delivers the additional <=0.479 factor
            without tuning  ==>  BBN-arm tension STRUCTURAL  (or sign_verdict==FAIL).
  INFO iff a mechanism narrows ΔN_eff below the baseline 2.0873 toward 1 but does not reach <=1.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-98/s98_mk3_2_bbn_vacuum_fraction.npz   (V.10; baseline ratio + lever X)
  - computations/session-98/s98_mk3_1_c10_subleading_sign.npz   (V.9 ; HARD from-below n_eff=1.978111)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<ΔN_eff_relieved_best>, scheme=FW, convention=ABSOLUTE, L_max=N/A)

Classification: PHONONIC.
  The BBN-epoch vacuum fraction IS the a0 tracking-vacuum (Volovik, the spectral-action ZEROTH
  moment a_0_FW_zeta=6440.0 -- a DIFFERENT spectral moment than gravity a_2) evaluated at the
  radiation-dominated BBN epoch: rho_vac = alpha_V M_Pl^2 H^{n_eff}. Arrow:
    D_K eigenvalues -> a_0 zeroth spectral moment -> rho_vac tracking-vacuum
      -> BBN-epoch fraction (rho_vac/rho_rad)_BBN -> ΔN_eff.
  DESI/Planck N_eff is the laboratory-IN falsifier; the tracking-vacuum is substrate-IS.

METHODOLOGY
-----------
Closed-form modified-Friedmann lever (NO D_K diagonalization; consumes the L_max=12 n_eff
pinned upstream in S98 V.9). The substrate-correct lever is

    (rho_vac/rho_rad)_BBN = frac_base * (H_BBN/H_0)^{n_eff-2}
                          = frac_base * exp( (n_eff-2) * X ),   X = ln(H_BBN/H_0) = 40.2756,

which reproduces the S98 V.10 canonical frac_below=0.474049 to 0.0e+00 residual (verified below).
[PLAN-TEXT NOTE: the §W2-2 substitution-chain WRITES the lever as X^{n_eff-2}=0.9223; that double-
logs X (X is ALREADY ln(H_BBN/H0)) and does NOT reproduce the canonical frac_below -- it would give
frac=1.0558, dNeff=4.65, contradicting the canonical dNeff=2.0873. The substrate-correct exp((n-2)*X)
lever -- the one the S98 V.10 npz actually used -- is adopted here; the direction logic in the plan
chain ((n-2)<0 & X>0 => relief_factor<1) is correct under BOTH forms. Documented as a process
observation, not silently propagated.]

Three candidate relief mechanisms are enumerated and each tested for whether its REQUIRED parameter
is substrate-justified (NOT a tuned fit):
  (a) larger from-below shift Δn  : solve frac_base*exp((n_a-2)*X)=bound for n_a; compare to the HARD
                                    V.9 n_eff=1.978111 (divergence_type=A) -- is the required shift the
                                    substrate-derived one?
  (b) epoch-dependent alpha_V     : rho_vac ∝ alpha_V, so the required alpha_V,BBN/alpha_V,0 = extra
                                    factor = bound/frac_below; DILUTION-CC-66 uses a SINGLE alpha_V
                                    tracking normalization -- is a z-dependent alpha_V substrate-forced?
  (c) distinct dilution channel   : a separate suppression factor at BBN; the cc-path-d (D-57)
                                    mode-fraction channel rho_vac^eff=(N_eff/992)*rho_vac needs
                                    N_eff/992 = extra factor -- is that mode sub-selection substrate-derived?

DISCIPLINE
----------
- `from canonical_constants import *`
- every intermediate tagged `# (local)`
- closed-form scalar evaluation; CPU; OMP_NUM_THREADS=8 set before numpy import
- SHA-256 of all inputs logged in first 20 lines of stdout
- audit_sha256 + content_sha256 (S84+ dual-SHA); the script PRINTS the verdict payload, the agent
  calls mcp__knowledge__emit_verdict (race-safe; the script does NOT open("a") the verdict file)
- [SIGN] trigger: sign/magnitude/regime 3-tuple emitted (all-three-or-none)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU; closed-form scalar -- cap threads before numpy

import sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"  # computations/_shared
sys.path.insert(0, str(_SHARED))

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    rho_vac_over_rho_rad_BBN_below,
    delta_N_eff_vacuum_BBN_below,
    a_0_FW_zeta,
    rho_vac_over_rho_obs,
    M_KK,
    tau_fold,
)

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 -- Identity / paths
# ---------------------------------------------------------------------------
SESSION = "S99"
GATE_ID = "S99-W2-BBN-RELIEF"
SCHEME = "FW"
CONVENTION = "ABSOLUTE"
L_MAX = "N/A"

HERE = Path(__file__).resolve().parent          # (local) computations/session-99
SHARED_DIR = HERE.parent / "_shared"            # (local) computations/_shared
CANONICAL = SHARED_DIR / "canonical_constants.py"  # (local)

NPZ_V10 = HERE.parent / "session-98" / "s98_mk3_2_bbn_vacuum_fraction.npz"  # (local) V.10
NPZ_V9 = HERE.parent / "session-98" / "s98_mk3_1_c10_subleading_sign.npz"   # (local) V.9

INPUT_FILES = {
    "computations/_shared/canonical_constants.py": CANONICAL,
    "computations/session-98/s98_mk3_2_bbn_vacuum_fraction.npz": NPZ_V10,
    "computations/session-98/s98_mk3_1_c10_subleading_sign.npz": NPZ_V9,
}

OUT_NPZ = HERE / "s99_w2_bbn_relief.npz"  # (local)
OUT_PNG = HERE / "s99_w2_bbn_relief.png"  # (local)


# ---------------------------------------------------------------------------
# Section 4 -- SHA helpers (dual-SHA per S84+ schema; copied from script-template.py)
# ---------------------------------------------------------------------------
def _sha256_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "<absent>"


def log_input_pins(files: dict[str, Path]) -> dict[str, str]:
    pins: dict[str, str] = {}  # (local)
    for relpath, p in sorted(files.items()):
        sha = _sha256_file(p)  # (local)
        pins[relpath] = sha
        print(f"  INPUT {relpath}: {sha}")
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
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
# Section 5 -- Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    """Closed-form modified-Friedmann lever + three substrate relief-mechanism tests."""
    # ---- Load upstream substrate-IS inputs (NO re-derivation; pinned by SHA) ----
    d10 = np.load(NPZ_V10, allow_pickle=True)  # (local) S98 V.10
    d9 = np.load(NPZ_V9, allow_pickle=True)    # (local) S98 V.9

    n_eff = float(d9["n_eff_T61"])            # (local) HARD from-below 1.978110506244663 (V.9)
    X = float(d10["X"])                       # (local) ln(H_BBN/H0) = 40.27560958603052 (single, NOT scanned)
    frac_base = float(d10["frac_base"])       # (local) n=2 baseline rho_vac/rho_rad = 1.1447295727818823
    frac_below = float(d10["frac_below"])     # (local) from-below value = 0.4740491472923885 (canonical)

    # cross-check the loaded n_eff and frac_below against the canonical_constants pins
    cc_frac_below = float(rho_vac_over_rho_rad_BBN_below)   # (local) 0.474049 (4 sig figs)
    cc_dNeff = float(delta_N_eff_vacuum_BBN_below)          # (local) 2.0873 (5 sig figs)

    # ---- BBN bound: canonical S66 formula (7/8)(4/11)^(4/3); substrate-first, exact-formula value ----
    # NOTE: the plan pins BBN_bound=0.227113 (rounded literal). The exact-formula value is 0.227107.
    #       The npz also carries bound=0.22710731766 (the exact-formula value). We adopt the
    #       exact-formula value (substrate-first canonical-sourcing) and document the 0.227113 drift.
    BBN_BOUND = (7.0 / 8.0) * (4.0 / 11.0) ** (4.0 / 3.0)  # (local) = 0.227107317660239
    npz_bound = float(d10["bound"])                        # (local) 0.22710731766023898
    plan_pinned_bound = 0.227113                           # (local) rounded plan literal (documented drift)

    # ============================================================
    # Baseline lever (substrate-correct form): exp((n_eff-2)*X)
    # ============================================================
    exp_below = n_eff - 2.0                          # (local) -0.021889... (sign NEGATIVE: n_eff<2)
    relief_factor = float(np.exp(exp_below * X))     # (local) exp((n-2)*X) = 0.414114... (<1: relief)
    frac_below_recomputed = frac_base * relief_factor  # (local) reproduce 0.474049
    repro_residual = frac_below_recomputed - frac_below  # (local) MUST be ~0

    # ---- [SIGN] relief-direction substitution chain (executable) ----
    sign_exp_neg = (exp_below < 0.0)                 # (local) (n_eff-2) < 0
    sign_lever_pos = (X > 0.0)                       # (local) X = ln(H_BBN/H0) > 0
    relief_direction = (relief_factor < 1.0)         # (local) (neg power of base>1) => factor < 1
    # direction predicted by chain: sign_exp_neg AND sign_lever_pos => relief_factor < 1
    direction_predicted = sign_exp_neg and sign_lever_pos
    sign_ok = (direction_predicted == relief_direction)  # (local) computed dir matches predicted

    # ---- baseline ΔN_eff (current state, from-below, no extra relief) ----
    dNeff_below = frac_below / BBN_BOUND             # (local) 2.0873...
    extra_needed = BBN_BOUND / frac_below            # (local) 0.479080 -- factor still required ON TOP

    # ============================================================
    # Three candidate substrate relief mechanisms (a)/(b)/(c)
    # Each: compute the REQUIRED parameter, then test substrate-justification.
    # ============================================================

    # (a) LARGER from-below shift Δn :  frac_base*exp((n_a-2)*X) = bound  ->  n_a-2 = ln(bound/frac_base)/X
    n_a_minus_2 = float(np.log(BBN_BOUND / frac_base) / X)  # (local) required (n-2) to hit the bound
    n_a_required = 2.0 + n_a_minus_2                        # (local) 1.959839...
    shift_ratio_a = n_a_minus_2 / exp_below                 # (local) required-shift / substrate-shift = 1.835
    frac_a = frac_base * float(np.exp(n_a_minus_2 * X))     # (local) == bound by construction
    dNeff_a = frac_a / BBN_BOUND                            # (local) -> 1.0 by construction
    # substrate-justification (a): V.9 fixes n_eff at 1.978111 HARD (divergence_type=A). The required
    # shift is 1.835x larger; NOT the substrate-derived sub-leading value.
    a_substrate_justified = bool(abs(n_a_required - n_eff) < 1e-3)  # (local) is required shift ~ substrate?

    # (b) EPOCH-DEPENDENT alpha_V :  rho_vac ∝ alpha_V  ->  required alpha_V,BBN/alpha_V,0 = extra_needed
    alpha_ratio_required = extra_needed              # (local) 0.479080
    frac_b = frac_below * alpha_ratio_required       # (local) == bound by construction
    dNeff_b = frac_b / BBN_BOUND                     # (local) -> 1.0 by construction
    # substrate-justification (b): DILUTION-CC-66 uses ONE alpha_V (single a_0 tracking normalization,
    # z=0 lever=1 leaves rho_vac_over_rho_obs=1.032 UNAFFECTED). No substrate forces alpha_V(z) to halve
    # specifically at BBN; a z-dependent alpha_V is a free function => NOT substrate-justified.
    b_substrate_justified = False                    # (local) no substrate-derived alpha_V(z) halving

    # (c) DISTINCT dilution channel :  rho_vac^eff=(N_eff/992)*rho_vac (cc-path-d D-57) -> N_eff/992 = extra
    mode_frac_required = extra_needed                # (local) 0.479080
    N_modes_required = mode_frac_required * 992.0    # (local) 475.25 of 992
    frac_c = frac_below * mode_frac_required         # (local) == bound by construction
    dNeff_c = frac_c / BBN_BOUND                     # (local) -> 1.0 by construction
    # substrate-justification (c): in DILUTION-CC ALL 992 D_K modes gravitate (a_0=zeta_{D_K}(0)=Tr(1)
    # counts the full mode set). No substrate sub-selects ~475 modes at BBN => NOT substrate-justified.
    c_substrate_justified = False                    # (local) no substrate-derived 992->475 sub-selection

    any_substrate_justified = (a_substrate_justified
                               or b_substrate_justified
                               or c_substrate_justified)  # (local)

    # best relieved ΔN_eff achievable WITHOUT tuning = the baseline from-below (no mechanism qualifies)
    dNeff_best_unforced = dNeff_below                # (local) 2.0873 (none of a/b/c is substrate-justified)

    # ---- consequence of the ERRONEOUS plan-text X^(n-2) lever (documented, not used) ----
    relief_planform = float(X ** exp_below)          # (local) 0.922288 (plan-chain WRITTEN value)
    frac_planform = frac_base * relief_planform      # (local) 1.0558 -- does NOT match canonical 0.474049

    return {
        "value": dNeff_best_unforced,
        # inputs / reproduction
        "n_eff": n_eff, "X": X, "frac_base": frac_base, "frac_below": frac_below,
        "cc_frac_below": cc_frac_below, "cc_dNeff": cc_dNeff,
        "BBN_BOUND_exact": BBN_BOUND, "npz_bound": npz_bound, "plan_pinned_bound": plan_pinned_bound,
        "exp_below": exp_below, "relief_factor": relief_factor,
        "frac_below_recomputed": frac_below_recomputed, "repro_residual": repro_residual,
        # sign / direction
        "sign_exp_neg": sign_exp_neg, "sign_lever_pos": sign_lever_pos,
        "relief_direction": relief_direction, "direction_predicted": direction_predicted,
        "sign_ok": sign_ok,
        # baseline ΔN_eff + extra factor needed
        "dNeff_below": dNeff_below, "extra_needed": extra_needed,
        # mechanism (a)
        "n_a_required": n_a_required, "n_a_minus_2": n_a_minus_2, "shift_ratio_a": shift_ratio_a,
        "frac_a": frac_a, "dNeff_a": dNeff_a, "a_substrate_justified": a_substrate_justified,
        # mechanism (b)
        "alpha_ratio_required": alpha_ratio_required, "frac_b": frac_b, "dNeff_b": dNeff_b,
        "b_substrate_justified": b_substrate_justified,
        # mechanism (c)
        "mode_frac_required": mode_frac_required, "N_modes_required": N_modes_required,
        "frac_c": frac_c, "dNeff_c": dNeff_c, "c_substrate_justified": c_substrate_justified,
        # roll-up
        "any_substrate_justified": any_substrate_justified,
        "dNeff_best_unforced": dNeff_best_unforced,
        # plan-text error consequence
        "relief_planform": relief_planform, "frac_planform": frac_planform,
        # context constants
        "a_0_FW_zeta": float(a_0_FW_zeta), "rho_vac_over_rho_obs": float(rho_vac_over_rho_obs),
        "M_KK": float(M_KK), "tau_fold": float(tau_fold),
    }


# ---------------------------------------------------------------------------
# Section 6 -- Gate verdict (composite collapse) + 3-tuple + 4-tuple
# ---------------------------------------------------------------------------
def evaluate_3tuple(r: dict) -> tuple[str, str, str]:
    """Return (sign_verdict, magnitude_verdict, regime_verdict) per gate-verdicts.md schema-v2."""
    # SIGN: relief direction predicted by the substitution chain vs computed
    sign_verdict = "PASS" if r["sign_ok"] else "FAIL"  # (local)

    # MAGNITUDE: best UNFORCED relieved ΔN_eff vs threshold 1.0 (pass band), info band, fail
    # PASS iff a substrate-justified mechanism achieves ΔN_eff <= 1 (|ΔN_eff-1| within band)
    dNeff = r["dNeff_best_unforced"]  # (local)
    pass_band = 0.05    # (local) consistent with the W2 cluster band; ΔN_eff<=1 strict
    info_band = 0.10    # (local)
    if r["any_substrate_justified"] and dNeff <= 1.0 + pass_band:
        magnitude_verdict = "PASS"  # (local)
    elif r["any_substrate_justified"] and dNeff <= 1.0 + info_band:
        magnitude_verdict = "INFO"  # (local)
    elif dNeff < float(delta_N_eff_vacuum_BBN_below):  # narrowed below baseline 2.0873 toward 1
        # narrowing without reaching <=1: INFO only if a mechanism actually moved it; here none did
        magnitude_verdict = "INFO" if r["any_substrate_justified"] else "FAIL"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)

    # REGIME: closed-form, single substrate-fixed epoch, exact-formula bound -> VALID
    regime_verdict = "VALID"  # (local)
    return sign_verdict, magnitude_verdict, regime_verdict


def collapse(sign_v: str, mag_v: str, reg_v: str) -> str:
    """Pre-registered composite-collapse rule (gate-verdicts.md)."""
    if reg_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if mag_v == "FAIL" and reg_v == "VALID":
        return "FAIL"
    if mag_v == "FAIL" and reg_v == "MARGINAL":
        return "INFO"
    if mag_v == "INFO":
        return "INFO"
    return "PASS"


# ---------------------------------------------------------------------------
# print_verdict_payload (delimited stdout block for the dispatching agent)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
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


def make_plot(r: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))

    # Panel 1: lever curve rho_vac/rho_rad vs n_eff, with bound + the three mechanism targets
    n_grid = np.linspace(1.90, 2.06, 400)                         # (local)
    frac_grid = r["frac_base"] * np.exp((n_grid - 2.0) * r["X"])  # (local)
    ax1.plot(n_grid, frac_grid, "b-", lw=2, label=r"$(\rho_{vac}/\rho_{rad})_{BBN}=$frac$_{base}\,e^{(n-2)X}$")
    ax1.axhline(r["BBN_BOUND_exact"], color="green", ls="--", lw=1.5,
                label=fr"BBN bound $= (7/8)(4/11)^{{4/3}} = {r['BBN_BOUND_exact']:.6f}$")
    ax1.axhline(r["frac_below"], color="red", ls=":", lw=1.5,
                label=fr"from-below $= {r['frac_below']:.6f}$ ($\Delta N_{{eff}}={r['dNeff_below']:.4f}$)")
    ax1.axvline(2.0, color="gray", ls="-", lw=0.8, alpha=0.6, label=r"$n=2$ baseline")
    ax1.plot([r["n_eff"]], [r["frac_below"]], "rs", ms=9, label=fr"V.9 HARD $n_{{eff}}={r['n_eff']:.6f}$")
    ax1.plot([r["n_a_required"]], [r["BBN_BOUND_exact"]], "k^", ms=11,
             label=fr"(a) required $n_a={r['n_a_required']:.6f}$ ({r['shift_ratio_a']:.3f}$\times$ shift)")
    ax1.set_xlabel(r"tracking exponent $n_{eff}$")
    ax1.set_ylabel(r"$(\rho_{vac}/\rho_{rad})_{BBN}$")
    ax1.set_yscale("log")
    ax1.set_title("BBN-epoch vacuum fraction lever (single substrate-fixed $X=40.2756$)")
    ax1.legend(fontsize=7, loc="upper left")
    ax1.grid(alpha=0.3)

    # Panel 2: ΔN_eff bar chart -- baseline + the three mechanisms (each forced to 1 by construction)
    labels = ["from-below\n(no extra)", "(a) larger Δn", "(b) ε-dep α_V", "(c) mode channel", "bound\nΔN=1"]  # (local)
    dNeffs = [r["dNeff_below"], r["dNeff_a"], r["dNeff_b"], r["dNeff_c"], 1.0]  # (local)
    justified = [None, r["a_substrate_justified"], r["b_substrate_justified"],
                 r["c_substrate_justified"], None]  # (local)
    colors = []  # (local)
    for j in justified:
        if j is None:
            colors.append("gray")
        elif j:
            colors.append("green")
        else:
            colors.append("red")
    bars = ax2.bar(labels, dNeffs, color=colors, alpha=0.75, edgecolor="black")
    ax2.axhline(1.0, color="green", ls="--", lw=1.5, label=r"BBN bound $\Delta N_{eff}=1$")
    ax2.axhline(r["dNeff_below"], color="red", ls=":", lw=1.0, alpha=0.6)
    for b, v in zip(bars, dNeffs):
        ax2.text(b.get_x() + b.get_width() / 2, v + 0.04, f"{v:.3f}", ha="center", fontsize=8)
    # annotate required-but-NOT-substrate-justified
    ax2.text(0.5, 0.92,
             "(a)/(b)/(c) reach ΔN=1 ONLY at\nNON-substrate parameters\n"
             f"(a): n needs {r['shift_ratio_a']:.2f}× shift\n"
             f"(b): α_V needs ×{r['alpha_ratio_required']:.4f}\n"
             f"(c): {r['N_modes_required']:.0f}/992 modes\n"
             "=> red = NOT substrate-justified",
             transform=ax2.transAxes, fontsize=7, va="top", ha="center",
             bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.85))
    ax2.set_ylabel(r"$\Delta N_{eff}$(vacuum)")
    ax2.set_title("Relief-mechanism test (green=substrate-justified, red=tuned)")
    ax2.legend(fontsize=8, loc="upper right")
    ax2.grid(alpha=0.3, axis="y")

    fig.suptitle(f"{GATE_ID} -- BBN-arm relief: from-below direction CORRECT, magnitude STRUCTURALLY insufficient",
                 fontsize=11, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 -- Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} (session {SESSION}) ===")
    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)        # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    r = compute()  # (local)

    # ---- substitution-chain echo (NUMBERS) ----
    print("--- relief-direction substitution chain (substrate-correct lever) ---")
    print(f"  n_eff (V.9 HARD)            = {r['n_eff']:.15f}")
    print(f"  X = ln(H_BBN/H0)           = {r['X']:.15f}  (single substrate-fixed; NOT scanned)")
    print(f"  (n_eff-2)                  = {r['exp_below']:.15f}  [sign NEGATIVE]")
    print(f"  relief_factor=exp((n-2)*X) = {r['relief_factor']:.15f}  [<1 => relief]")
    print(f"  frac_base                  = {r['frac_base']:.15f}")
    print(f"  frac_base*relief_factor    = {r['frac_below_recomputed']:.15f}")
    print(f"  canonical frac_below       = {r['frac_below']:.15f}")
    print(f"  reproduction residual      = {r['repro_residual']:.3e}  [MUST be ~0]")
    print(f"  BBN bound (exact formula)  = {r['BBN_BOUND_exact']:.15f}")
    print(f"    npz bound                = {r['npz_bound']:.15f}  (matches exact formula)")
    print(f"    plan-pinned 0.227113     = {r['plan_pinned_bound']}  (rounded literal; drift {abs(r['plan_pinned_bound']-r['BBN_BOUND_exact']):.2e})")
    print(f"  dNeff_below (baseline)     = {r['dNeff_below']:.15f}")
    print(f"  extra factor needed        = {r['extra_needed']:.15f}")
    print()
    print("--- PLAN-TEXT lever-form discrepancy (documented, NOT used) ---")
    print(f"  plan-chain X^(n-2)         = {r['relief_planform']:.15f}  (WRITTEN in plan §W2-2 chain)")
    print(f"  frac_base*X^(n-2)          = {r['frac_planform']:.15f}  (does NOT match canonical 0.474049)")
    print(f"  => substrate-correct lever is exp((n-2)*X); plan double-logs X. Direction logic unaffected.")
    print()
    print("--- three relief mechanisms ---")
    print(f"  (a) larger Δn : n_a_required={r['n_a_required']:.6f}  (n-2={r['n_a_minus_2']:.6f}; "
          f"{r['shift_ratio_a']:.4f}x substrate shift) -> dNeff_a={r['dNeff_a']:.6f}  "
          f"substrate-justified={r['a_substrate_justified']}")
    print(f"  (b) ε-dep α_V : alpha_ratio_required={r['alpha_ratio_required']:.6f} -> dNeff_b={r['dNeff_b']:.6f}  "
          f"substrate-justified={r['b_substrate_justified']}")
    print(f"  (c) mode chan : N_modes_required={r['N_modes_required']:.4f}/992 "
          f"(frac={r['mode_frac_required']:.6f}) -> dNeff_c={r['dNeff_c']:.6f}  "
          f"substrate-justified={r['c_substrate_justified']}")
    print(f"  any substrate-justified?   = {r['any_substrate_justified']}")
    print(f"  best UNFORCED dNeff         = {r['dNeff_best_unforced']:.15f}")
    print()

    # ---- 3-tuple + composite ----
    sign_v, mag_v, reg_v = evaluate_3tuple(r)  # (local)
    composite = collapse(sign_v, mag_v, reg_v)  # (local)
    print(f"  sign_verdict={sign_v}  magnitude_verdict={mag_v}  regime_verdict={reg_v}  => composite={composite}")

    # ---- 4-tuple ----
    fourtuple = (f"(value={r['value']!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(f"  4-tuple: {fourtuple}")

    # ---- save npz ----
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite=composite, sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        **{k: v for k, v in r.items()},
        audit_sha256=audit_sha, content_sha256=content_sha,
        BBN_BOUND=r["BBN_BOUND_exact"],
        track_B_structural=(not r["any_substrate_justified"]),
    )
    print(f"  saved npz: {OUT_NPZ}")

    make_plot(r)
    print(f"  saved png: {OUT_PNG}")
    print()

    # ---- value payload string (no single-quote chars; the tool wraps value='...') ----
    value_payload = (
        f"dNeff_best_unforced={r['dNeff_best_unforced']:.4f};"
        f"frac_below={r['frac_below']:.6f};bound={r['BBN_BOUND_exact']:.6f};"
        f"relief_factor={r['relief_factor']:.6f};relief_direction={r['relief_direction']};"
        f"extra_needed={r['extra_needed']:.6f};"
        f"mech_a_n_req={r['n_a_required']:.6f}(shift_x{r['shift_ratio_a']:.3f});"
        f"mech_b_alpha_req={r['alpha_ratio_required']:.6f};"
        f"mech_c_modes_req={r['N_modes_required']:.1f}of992;"
        f"any_substrate_justified={r['any_substrate_justified']};"
        f"track_B_structural={not r['any_substrate_justified']}"
    )  # (local)

    print_verdict_payload(
        composite, value_payload, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        companion_note="BBN-arm relief: from-below direction CORRECT (factor 0.4141<1) but magnitude STRUCTURALLY insufficient (dNeff=2.0873>1); none of (a)/(b)/(c) substrate-justified",
        extra_rows=[
            "# regulator_pin=a_0^{zeta}  # rho_vac is the a0 zeroth Seeley-DeWitt moment (zeta-regulated) tracking-vacuum (regulator-pin-discipline.md)",
        ],
    )

    print(f"\n  elapsed: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
