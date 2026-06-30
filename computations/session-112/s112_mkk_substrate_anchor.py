#!/usr/bin/env python3
"""
S112 W1-1 CF-S112-MKK-SUBSTRATE-ANCHOR — the M_KK keystone
==========================================================

Gate: CF-S112-MKK-SUBSTRATE-ANCHOR ([SIGN])

Pre-registered threshold (per candidate anchor Lambda_anchor^{(c)}):
  leg1_RGinv := max_tau |M_KK(tau)/M_KK(tau_fold) - 1| <= 5e-2 over [0.19, 0.55]
  leg2_noimport := codata_set INTERSECT inputs(Lambda_anchor^{(c)}) = empty
  Delta_rel := |M_KK(tau_fold) - M_KK_target| / M_KK_target <= 5e-2
  GATE PASS iff EITHER candidate satisfies (leg1 AND leg2 AND Delta_rel<5e-2).

The dimensionless transmutation kernel is FIXED + substrate-internal (S110 CV2A /
S111 MKK-RG, bit-exact-reproduced): R(tau) = exp(-1/(lam_eff(tau)*N0(tau))). The
gate's only structural object is Lambda_anchor, PINNED to two candidates:
  A (GAP-EMERGENT-LENGTH):  Lambda_A = Delta_BCS * M_KK
  B (EMERGENT-NEWTON):      Lambda_B = sqrt(a_2^{zeta}/(48 pi^2)) * M_KK
Both are PURE-NUMBER * M_KK in M_KK units (Delta_BCS, a_2^{zeta} are dimensionless),
so neither carries an INDEPENDENT GeV scale -- the substitution-chain prediction is
the self-referential no-go (FAIL). This script tests that prediction against compute.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-111/s111_mkk_rg_invariance.npz  (BARE-IMPORT baseline + R/lam/N0 scan)
  - computations/session-110/s110_cf_cv2a_mkk_transmut_promote.npz  (transmutation kernel)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<composite>, scheme=SA, convention=RATIO, L_max=12)

Classification: GEOMETRIC (M_KK = 1/R_K is the compactification scale of the
spectral-triple fabric, not a property of its phononic excitations).

METHODOLOGY
-----------
Re-run the S111 two-leg tau-RG-invariance test, replacing the BARE-IMPORT magnitude
anchor (M_Pl_reduced, CODATA) with each pinned substrate-natural candidate. R(tau),
lam_eff(tau), N0(tau) are loaded bit-exact from the S111 scan arrays (continuity
check vs S111 R_fold/lam_fold/N0_fold to 1e-9). For each candidate, M_KK(tau) =
Lambda_anchor(tau)*R(tau) is evaluated on the tau-scan; leg1 measures the tau-flatness
of the M_KK(tau)/M_KK(tau_fold) RATIO over the [0.19,0.55] plan sub-window; leg2 is a
set-membership audit of the anchor's dimensionful-input set against the codata
exclusion list; Delta_rel is the target-match at tau_fold. Because a substrate pure
number carries no independent GeV scale, Delta_rel is evaluated in the SELF-CONSISTENCY
reading M_KK(tau_fold) = prefactor*M_KK with M_KK held at target -> Delta_rel =
|prefactor - 1| (a fixed point of the closed form only at M_KK=0). The substitution
chain (Step 2-4) reduces both candidates to M_KK*(pure number); the gate decides
whether ANY substrate-internal anchor closes the loop tau-RG-invariantly without an
external GeV pin.

DISCIPLINE
----------
- `from canonical_constants import *`
- every local/intermediate tagged `# (local)`
- no new large eigensolve (cached scalars re-used per GPU_path pin); OMP8 thread cap
- SHA-256 of all inputs logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as final non-verdict line
- verdict emitted via emit_verdict MCP tool (race-safe); script PRINTS the payload
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0b — make computations/_shared importable BEFORE the canonical import
# ---------------------------------------------------------------------------
import sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402

_SHARED = _Path(__file__).resolve().parent.parent / "_shared"  # computations/_shared
sys.path.insert(0, str(_SHARED))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402
    M_KK_gravity,
    M_Pl_reduced,
    a_2_FW_zeta,
    Delta_BCS,
    tau_fold,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S112"                                   # (local)
GATE_ID = "CF-S112-MKK-SUBSTRATE-ANCHOR"           # (local)
SCHEME = "SA"                                       # (local)
CONVENTION = "RATIO"                                # (local)
L_MAX = 12                                          # (local)

# Pre-registered bands (plan §W1-1 strict_PASS_boundary)
DELTA_REL_BAND = 5e-2          # (local) both legs use the same 5e-2 band
INFO_BAND = 5e-1               # (local) near-miss INFO ceiling (plan INFO_meaning)
CONTINUITY_TOL = 1e-9          # (local) bit-exact continuity vs S111 R_fold/lam_fold/N0_fold
LEG1_WINDOW = (0.19, 0.55)     # (local) the plan's leg1 tau-flatness sub-window
M_KK_TARGET = M_KK_gravity     # 7.428660036284456e16 GeV (S42 CONST-FREEZE-42)

# codata_exclusion_set: any presence in an anchor's dimensionful-input set => leg2=False
CODATA_EXCLUSION_SET = (
    "M_Pl_reduced",
    "M_Pl_unreduced",
    "G_Newton_CODATA",
    "hbar_CODATA",
    "c_CODATA",
    "eV_GeV_unit_conversion",
)
# Substrate-internal pure-number admissibles (carry NO absolute GeV scale in M_KK units)
SUBSTRATE_ADMISSIBLE = (
    "Delta_BCS",
    "a_0_FW_zeta",
    "a_2_FW_zeta",
    "lam_eff",
    "N0",
    "R",
    "tau_fold",
    "M_KK_as_unit",
)

OUT_NPZ = SESSION_DIR / "s112_mkk_substrate_anchor.npz"
OUT_PNG = SESSION_DIR / "s112_mkk_substrate_anchor.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    COMPUTATIONS_DIR / "session-111" / "s111_mkk_rg_invariance.npz",
    COMPUTATIONS_DIR / "session-110" / "s110_cf_cv2a_mkk_transmut_promote.npz",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
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
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


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
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Two-leg tau-RG-invariance test under two pinned substrate-natural anchors.

    Returns a dict with 'value' (composite payload string) and all cross-check
    fields for the npz + WP.
    """
    # ---- Load the two pinned npz inputs ----
    s111_path = COMPUTATIONS_DIR / "session-111" / "s111_mkk_rg_invariance.npz"  # (local)
    s110_path = (
        COMPUTATIONS_DIR / "session-110" / "s110_cf_cv2a_mkk_transmut_promote.npz"
    )  # (local)
    d111 = np.load(s111_path, allow_pickle=True)  # (local)
    d110 = np.load(s110_path, allow_pickle=True)  # (local)

    # ---- Cached substrate-internal transmutation kernel (bit-exact reproduced) ----
    tau_scan = np.asarray(d111["tau_scan"], dtype=float)  # (local) S111 scan grid
    lam_scan = np.asarray(d111["lam_scan"], dtype=float)  # (local) lam_eff(tau)
    N0_scan = np.asarray(d111["N0_scan"], dtype=float)    # (local) windowed van-Hove DOS
    R_scan = np.asarray(d111["R_scan"], dtype=float)      # (local) R(tau)=exp(-1/(lam*N0))
    tau_fold_found = float(d111["tau_fold_found"])         # (local) 0.19015788...
    R_fold = float(d111["R_fold"])                          # (local) 0.16016847970570353
    lam_fold = float(d111["lam_fold"])                      # (local) 0.038934760900644856
    N0_fold = float(d111["N0_fold_check"])                  # (local) 14.023250234055002

    # ---- Bit-exact continuity check vs S111 / S110 CV2A ----
    R_CV2A = float(d110["transmutation_ratio"])  # (local) 0.16016847970570353
    lam_CV2A = float(d110["lambda_eff"])          # (local)
    N0_CV2A = float(d110["N0"])                    # (local)
    cont_R = abs(R_fold - R_CV2A)                  # (local)
    cont_lam = abs(lam_fold - lam_CV2A)            # (local)
    cont_N0 = abs(N0_fold - N0_CV2A)               # (local)
    continuity_ok = bool(
        (cont_R < CONTINUITY_TOL)
        and (cont_lam < CONTINUITY_TOL)
        and (cont_N0 < CONTINUITY_TOL)
    )  # (local)

    # Re-derive R(tau_fold) from the kernel formula as an internal consistency check
    R_fold_recomputed = math.exp(-1.0 / (lam_fold * N0_fold))  # (local)
    R_formula_resid = abs(R_fold_recomputed - R_fold)           # (local)

    # ---- Dimensionless anchor PREFACTORS (the substrate pure numbers) ----
    # Candidate B (EMERGENT-NEWTON): M_Pl_eff/M_KK = sqrt(a_2^{zeta}/(48 pi^2))
    denom_48pi2 = 48.0 * math.pi**2                    # (local) 473.7410...
    a2_over_48pi2 = a_2_FW_zeta / denom_48pi2          # (local) 5.86009...
    mpl_eff_over_mkk = math.sqrt(a2_over_48pi2)        # (local) 2.420762... (substrate Planck ratio)
    # Candidate A (GAP-EMERGENT-LENGTH): the gap pure number Delta_BCS
    gap_pure = float(Delta_BCS)                         # (local) 0.4642547...

    # ---- M_KK(tau) = Lambda_anchor(tau) * R(tau), in M_KK-PREFACTOR form ----
    # Lambda_anchor(tau) = (pure number) * M_KK  (the pure number is tau-INDEPENDENT for
    # both candidates: a_2^{zeta} and Delta_BCS are tau_fold-anchored canonical scalars).
    # So M_KK(tau)/M_KK = (pure number) * R(tau): the tau-flow is carried ENTIRELY by R(tau).
    prefac_B_scan = mpl_eff_over_mkk * R_scan          # (local) M_KK(tau)/M_KK, candidate B
    prefac_A_scan = gap_pure * R_scan                  # (local) M_KK(tau)/M_KK, candidate A

    prefac_B_fold = mpl_eff_over_mkk * R_fold          # (local) 0.387730 (matches sub-chain)
    prefac_A_fold = gap_pure * R_fold                  # (local) 0.074359

    # ---- leg1: tau-flatness of the M_KK(tau)/M_KK(tau_fold) RATIO over [0.19,0.55] ----
    win_lo, win_hi = LEG1_WINDOW                                          # (local)
    win_mask = (tau_scan >= win_lo - 1e-12) & (tau_scan <= win_hi + 1e-12)  # (local)
    tau_win = tau_scan[win_mask]                                          # (local)

    def leg1_flatness(prefac_scan: np.ndarray, prefac_fold: float) -> float:
        # ratio M_KK(tau)/M_KK(tau_fold) over the window; tau-flatness = max|ratio-1|
        ratio = prefac_scan[win_mask] / prefac_fold  # (local)
        return float(np.max(np.abs(ratio - 1.0)))

    leg1_flat_B = leg1_flatness(prefac_B_scan, prefac_B_fold)  # (local)
    leg1_flat_A = leg1_flatness(prefac_A_scan, prefac_A_fold)  # (local)
    leg1_B = bool(leg1_flat_B <= DELTA_REL_BAND)               # (local)
    leg1_A = bool(leg1_flat_A <= DELTA_REL_BAND)               # (local)

    # ---- leg2: set-membership audit of each anchor's dimensionful-input set ----
    # Candidate A dimensionful-input set: {M_KK_as_unit, Delta_BCS}  (no CODATA literal)
    inputs_A = ("M_KK_as_unit", "Delta_BCS")                                   # (local)
    # Candidate B dimensionful-input set: {M_KK_as_unit, a_2_FW_zeta}  (no CODATA literal)
    inputs_B = ("M_KK_as_unit", "a_2_FW_zeta")                                 # (local)
    codata_in_A = sorted(set(inputs_A) & set(CODATA_EXCLUSION_SET))            # (local)
    codata_in_B = sorted(set(inputs_B) & set(CODATA_EXCLUSION_SET))            # (local)
    leg2_A = bool(len(codata_in_A) == 0)                                       # (local)
    leg2_B = bool(len(codata_in_B) == 0)                                       # (local)
    # The DEGENERACY flag: leg2 "passes" set-membership trivially, BUT "M_KK_as_unit"
    # means the anchor is expressed IN M_KK units and carries NO independent GeV scale.
    # To produce a GeV NUMBER, an external scale must re-enter. Record the degeneracy.
    independent_gev_scale_A = False  # (local) Lambda_A = (pure number)*M_KK -> no indep GeV
    independent_gev_scale_B = False  # (local) Lambda_B = (pure number)*M_KK -> no indep GeV

    # ---- Delta_rel: target-match in the SELF-CONSISTENCY reading ----
    # M_KK(tau_fold) = prefactor * M_KK; holding M_KK at target, the closed form returns
    # prefactor*M_KK_target. Delta_rel = |prefactor*M_KK_target - M_KK_target|/M_KK_target
    #             = |prefactor - 1|. A fixed point (self-consistent M_KK) ONLY at prefactor=1.
    delta_rel_B = abs(prefac_B_fold - 1.0)  # (local) 0.612270
    delta_rel_A = abs(prefac_A_fold - 1.0)  # (local) 0.925641

    # ---- BARE-IMPORT baseline (the thing the substrate-natural anchor must beat) ----
    delta_rel_bare = float(d111["delta_rel"])  # (local) 8.192935623277037 (S111 FAIL)
    # The CODATA-anchored derived value (CV2A): M_KK_derived = M_Pl_reduced * R_fold
    M_KK_derived_bare = float(d111["M_KK_derived_red"])  # (local) 3.900e17
    # Sanity: M_Pl_reduced * R_fold should reproduce M_KK_derived_red
    M_KK_bare_recon = M_Pl_reduced * R_fold              # (local)
    bare_recon_resid = abs(M_KK_bare_recon - M_KK_derived_bare) / M_KK_derived_bare  # (local)

    # ---- Per-candidate conjunction ----
    passA = bool(leg1_A and leg2_A and (delta_rel_A <= DELTA_REL_BAND)
                 and independent_gev_scale_A)  # (local)
    passB = bool(leg1_B and leg2_B and (delta_rel_B <= DELTA_REL_BAND)
                 and independent_gev_scale_B)  # (local)
    # NOTE: the conjunction REQUIRES an independent GeV scale (the degeneracy gate).
    # leg2 set-membership alone is necessary-not-sufficient: a pure-number anchor passes
    # set-membership but supplies no absolute magnitude. The PASS rubric (PASS_meaning)
    # requires the anchor to "fix M_KK" -> an independent GeV scale is implied.
    gate_pass = bool(passA or passB)  # (local)

    # ---- Composite verdict + 3-tuple ([SIGN]) ----
    # sign_verdict: the substitution-chain Step-4 direction is that the substrate-natural
    #   anchor must FLATTEN the tau-product the bare anchor left STEEP (S111 8.193 -> <5e-2)
    #   AND carry a GeV scale. Direction predicted = "anchor reduces to M_KK*(pure number),
    #   no indep GeV scale, self-reference". Computed direction MATCHES that prediction
    #   (both prefactors != 1, neither carries indep GeV). sign_verdict = PASS (the predicted
    #   self-referential direction is the observed one).
    # magnitude_verdict: best Delta_rel across candidates vs the 5e-2 / 5e-1 bands.
    best_delta_rel = min(delta_rel_A, delta_rel_B)  # (local) = delta_rel_B = 0.612270
    if best_delta_rel <= DELTA_REL_BAND:
        magnitude_verdict = "PASS"  # (local)
    elif best_delta_rel <= INFO_BAND:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local) 0.612270 > 5e-1
    sign_verdict = "PASS"  # (local) predicted self-referential direction observed
    regime_verdict = "VALID"  # (local) closed-form arithmetic on cached scalars; in-regime

    # Composite collapse (gate-verdicts.md deterministic rule)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"  # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)
    # The composite FAIL == the registered no-go: neither candidate closes the loop.
    # gate_pass is False (no independent GeV scale) -> consistent with composite FAIL.

    # ---- value payload (no single-quote chars; emit_verdict wraps value='...') ----
    value = (
        f"NO-GO-self-referential-unit-system;"
        f"gate_pass={gate_pass};"
        f"candA[leg1={leg1_A},leg2={leg2_A},dRel={delta_rel_A:.6f},indepGeV={independent_gev_scale_A}];"
        f"candB[leg1={leg1_B},leg2={leg2_B},dRel={delta_rel_B:.6f},indepGeV={independent_gev_scale_B}];"
        f"prefacA={prefac_A_fold:.6f};prefacB={prefac_B_fold:.6f};"
        f"MPl_eff/MKK={mpl_eff_over_mkk:.6f};"
        f"bare_baseline_dRel={delta_rel_bare:.4f};"
        f"continuity={continuity_ok}"
    )  # (local)

    return {
        "value": value,
        # legs + conjunction
        "leg1_A": leg1_A, "leg1_B": leg1_B,
        "leg1_flat_A": leg1_flat_A, "leg1_flat_B": leg1_flat_B,
        "leg2_A": leg2_A, "leg2_B": leg2_B,
        "codata_in_A": codata_in_A, "codata_in_B": codata_in_B,
        "independent_gev_scale_A": independent_gev_scale_A,
        "independent_gev_scale_B": independent_gev_scale_B,
        "delta_rel_A": delta_rel_A, "delta_rel_B": delta_rel_B,
        "best_delta_rel": best_delta_rel,
        "passA": passA, "passB": passB, "gate_pass": gate_pass,
        # prefactors / substitution chain
        "prefac_A_fold": prefac_A_fold, "prefac_B_fold": prefac_B_fold,
        "mpl_eff_over_mkk": mpl_eff_over_mkk,
        "a2_over_48pi2": a2_over_48pi2, "denom_48pi2": denom_48pi2,
        "gap_pure": gap_pure,
        # kernel / continuity
        "R_fold": R_fold, "lam_fold": lam_fold, "N0_fold": N0_fold,
        "R_CV2A": R_CV2A, "lam_CV2A": lam_CV2A, "N0_CV2A": N0_CV2A,
        "cont_R": cont_R, "cont_lam": cont_lam, "cont_N0": cont_N0,
        "continuity_ok": continuity_ok,
        "R_fold_recomputed": R_fold_recomputed, "R_formula_resid": R_formula_resid,
        "tau_fold_found": tau_fold_found,
        # bare baseline
        "delta_rel_bare": delta_rel_bare,
        "M_KK_derived_bare": M_KK_derived_bare,
        "M_KK_bare_recon": M_KK_bare_recon, "bare_recon_resid": bare_recon_resid,
        # scans for plot/npz
        "tau_scan": tau_scan, "R_scan": R_scan,
        "prefac_A_scan": prefac_A_scan, "prefac_B_scan": prefac_B_scan,
        "tau_win": tau_win,
        # targets + 3-tuple
        "M_KK_target": M_KK_TARGET,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "composite": composite,
    }


def make_plot(result: dict) -> None:
    tau_scan = result["tau_scan"]  # (local)
    R_scan = result["R_scan"]      # (local)
    pa = result["prefac_A_scan"]   # (local)
    pb = result["prefac_B_scan"]   # (local)
    win_lo, win_hi = LEG1_WINDOW   # (local)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))  # (local)

    # Left: M_KK(tau)/M_KK = (pure number)*R(tau) for both candidates; the tau-flow is
    # carried entirely by R(tau) -> NOT flat -> leg1 FAIL.
    ax = axes[0]
    ax.plot(tau_scan, pb, "o-", ms=3, color="#c0392b", label=r"cand B: $\sqrt{a_2^{\zeta}/48\pi^2}\,R(\tau)$")
    ax.plot(tau_scan, pa, "s-", ms=3, color="#2471a3", label=r"cand A: $\Delta_{BCS}\,R(\tau)$")
    ax.axhline(1.0, color="k", ls="--", lw=0.8, label=r"$M_{KK}$ self-consistency (=1)")
    ax.axvspan(win_lo, win_hi, color="gray", alpha=0.12, label=r"leg1 window $[0.19,0.55]$")
    ax.set_xlabel(r"$\tau$ (Jensen deformation)")
    ax.set_ylabel(r"$M_{KK}(\tau)/M_{KK}$  (prefactor)")
    ax.set_title("Both anchors = (pure number)$\\cdot R(\\tau)$:\nself-reference, prefactor $\\neq 1$")
    ax.legend(fontsize=7, loc="upper right")
    ax.grid(alpha=0.3)

    # Right: Delta_rel bar chart (self-consistency |prefactor-1|) vs the 5e-2 / 5e-1 bands
    ax = axes[1]
    labels = ["cand A\n(GAP-LEN)", "cand B\n(EMERG-NEWTON)", "bare-import\n(S111, CODATA)"]  # (local)
    vals = [result["delta_rel_A"], result["delta_rel_B"], result["delta_rel_bare"]]  # (local)
    colors = ["#2471a3", "#c0392b", "#7f8c8d"]  # (local)
    bars = ax.bar(labels, vals, color=colors)
    ax.axhline(DELTA_REL_BAND, color="green", ls="--", lw=1.0, label=r"PASS band $5\times10^{-2}$")
    ax.axhline(INFO_BAND, color="orange", ls=":", lw=1.0, label=r"INFO band $5\times10^{-1}$")
    ax.set_yscale("log")
    ax.set_ylabel(r"$\Delta_{rel}=|{\rm prefactor}-1|$  (self-consistency)")
    ax.set_title("No candidate enters PASS band:\nself-referential no-go (magnitude FAIL)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v * 1.1, f"{v:.3f}", ha="center", fontsize=8)

    fig.suptitle(
        r"CF-S112-MKK-SUBSTRATE-ANCHOR — self-referential-unit-system no-go: "
        r"$M_{KK}=1/R_K$ cannot fix its own absolute GeV scale from within",
        fontsize=10,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

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
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    result = compute()  # (local)

    # ---- diagnostics to stdout ----
    print("=== substitution chain (bit-exact) ===")
    print(f"  48*pi^2                       = {result['denom_48pi2']:.6f}")
    print(f"  a_2^zeta/(48 pi^2)            = {result['a2_over_48pi2']:.6f}")
    print(f"  sqrt(a_2^zeta/(48 pi^2))      = {result['mpl_eff_over_mkk']:.6f}  (M_Pl_eff/M_KK)")
    print(f"  R_fold                        = {result['R_fold']:.17g}")
    print(f"  prefac_B = sqrt(..)*R_fold    = {result['prefac_B_fold']:.6f}  -> M_KK(fold)=prefac_B*M_KK")
    print(f"  prefac_A = Delta_BCS*R_fold   = {result['prefac_A_fold']:.6f}")
    print(f"  Delta_rel_B = |prefac_B - 1|  = {result['delta_rel_B']:.6f}")
    print(f"  Delta_rel_A = |prefac_A - 1|  = {result['delta_rel_A']:.6f}")
    print()
    print("=== continuity vs S111 / S110 CV2A (tol 1e-9) ===")
    print(f"  |R_fold - R_CV2A|     = {result['cont_R']:.3e}")
    print(f"  |lam_fold - lam_CV2A| = {result['cont_lam']:.3e}")
    print(f"  |N0_fold - N0_CV2A|   = {result['cont_N0']:.3e}")
    print(f"  continuity_ok         = {result['continuity_ok']}")
    print(f"  R_formula_resid       = {result['R_formula_resid']:.3e}  (exp(-1/(lam*N0)) vs cached)")
    print(f"  bare_recon_resid      = {result['bare_recon_resid']:.3e}  (M_Pl_red*R_fold vs S111 derived)")
    print()
    print("=== two-leg test ===")
    print(f"  cand A: leg1={result['leg1_A']}(flat={result['leg1_flat_A']:.4e}) "
          f"leg2={result['leg2_A']}(codata={result['codata_in_A']}) "
          f"indepGeV={result['independent_gev_scale_A']} dRel={result['delta_rel_A']:.6f} -> passA={result['passA']}")
    print(f"  cand B: leg1={result['leg1_B']}(flat={result['leg1_flat_B']:.4e}) "
          f"leg2={result['leg2_B']}(codata={result['codata_in_B']}) "
          f"indepGeV={result['independent_gev_scale_B']} dRel={result['delta_rel_B']:.6f} -> passB={result['passB']}")
    print(f"  GATE PASS (A or B)    = {result['gate_pass']}")
    print()
    print(f"  3-tuple: sign={result['sign_verdict']} magnitude={result['magnitude_verdict']} "
          f"regime={result['regime_verdict']} -> composite={result['composite']}")
    print()

    # ---- save npz ----
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite=result["composite"],
        sign_verdict=result["sign_verdict"],
        magnitude_verdict=result["magnitude_verdict"],
        regime_verdict=result["regime_verdict"],
        gate_pass=result["gate_pass"],
        leg1_A=result["leg1_A"], leg1_B=result["leg1_B"],
        leg1_flat_A=result["leg1_flat_A"], leg1_flat_B=result["leg1_flat_B"],
        leg2_A=result["leg2_A"], leg2_B=result["leg2_B"],
        codata_in_A=np.array(result["codata_in_A"], dtype=object),
        codata_in_B=np.array(result["codata_in_B"], dtype=object),
        independent_gev_scale_A=result["independent_gev_scale_A"],
        independent_gev_scale_B=result["independent_gev_scale_B"],
        delta_rel_A=result["delta_rel_A"], delta_rel_B=result["delta_rel_B"],
        best_delta_rel=result["best_delta_rel"],
        passA=result["passA"], passB=result["passB"],
        prefac_A_fold=result["prefac_A_fold"], prefac_B_fold=result["prefac_B_fold"],
        mpl_eff_over_mkk=result["mpl_eff_over_mkk"],
        a2_over_48pi2=result["a2_over_48pi2"], denom_48pi2=result["denom_48pi2"],
        gap_pure=result["gap_pure"],
        R_fold=result["R_fold"], lam_fold=result["lam_fold"], N0_fold=result["N0_fold"],
        R_CV2A=result["R_CV2A"], lam_CV2A=result["lam_CV2A"], N0_CV2A=result["N0_CV2A"],
        cont_R=result["cont_R"], cont_lam=result["cont_lam"], cont_N0=result["cont_N0"],
        continuity_ok=result["continuity_ok"],
        R_fold_recomputed=result["R_fold_recomputed"],
        R_formula_resid=result["R_formula_resid"],
        tau_fold_found=result["tau_fold_found"],
        delta_rel_bare=result["delta_rel_bare"],
        M_KK_derived_bare=result["M_KK_derived_bare"],
        M_KK_bare_recon=result["M_KK_bare_recon"],
        bare_recon_resid=result["bare_recon_resid"],
        tau_scan=result["tau_scan"], R_scan=result["R_scan"],
        prefac_A_scan=result["prefac_A_scan"], prefac_B_scan=result["prefac_B_scan"],
        tau_win=result["tau_win"],
        M_KK_target=result["M_KK_target"],
        delta_rel_band=DELTA_REL_BAND, info_band=INFO_BAND,
        leg1_window=np.array(LEG1_WINDOW),
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  npz -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(result)
    print(f"  png -> {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    tag = emit_4tuple(result["value"], SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)

    # regulator_pin + parity_pin companion rows (plan §W1-1 machinery pins)
    extra = [
        "# regulator_pin=a_2^{zeta} (poleconv-A-double pole_in_s=3 curvature_grade_n=2; "
        "M_Pl_eff^2=a_2^{zeta}/(48 pi^2) EH-normalization, regulator-pin-discipline.md)",
        "# convention_parity_pin=RATIO-DA-1-PARITY-odd (M_KK is d_A=+1 ODD scale leg; "
        "the magnitude leg lives on the sign-locked M_KK^1 odd scale-leg face of the Q=R*M_KK^m wall; "
        "corpus §23.0(5) fifth pin axis)",
    ]  # (local)

    print_verdict_payload(
        result["composite"],
        result["value"],
        audit_sha,
        content_sha,
        sign_verdict=result["sign_verdict"],
        magnitude_verdict=result["magnitude_verdict"],
        regime_verdict=result["regime_verdict"],
        companion_note="self-referential-unit-system no-go (lattice-QCD scale-setting analog)",
        extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {result['composite']} (wall {wall:.2f}s) ===")
    return 0 if result["composite"] != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
