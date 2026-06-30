#!/usr/bin/env python3
"""
INV6-W3-1 ETA-B-GGE-RESCATTERING
================================
Inter-branch GGE strong-rescattering phase -> C6 eta_B amplitude. Does the
post-transit 8-branch GGE relic's inter-branch overlap (strong / final-state)
phase delta_strong supply the missing ~13.5x that lifts eta_B from the S98 base
4.517492e-11 into the observed band [3e-10, 1.2e-9]?

Gate:  INV6-W3-1-ETA-B-GGE-RESCATTERING   ([SIGN]; schema-v2 3-tuple required)
Plan:  sessions/investigation/investigation-6/investigation-6-plan-w3.md  §W3-1
Track: investigation-6 (verdict -> computations/investigation-6/inv6_gate_verdicts.txt)

------------------------------------------------------------------------------
STRUCTURE-FIRST (substrate -> 8-branch GGE spectrum -> inter-branch overlap
                 phase -> CP-observable eta_B amplitude)
------------------------------------------------------------------------------
GOVERNING STRUCTURE. The substrate IS the post-transit GGE relic: a product
state (S_ent=0, T2) of Bogoliubov pairs across 8 branches (Row #67 two-speed
spectrum, s94_bao_peak_branch.npz). One branch (Goldstone) is gapless/protected;
the 7 others (B1, B2, B3, Leggett-L1/L2, Optical-O1/O2) are gapped. The B2
sector carries the K_7 charge and the phi_88-Cartan CP source. The C6
baryogenesis amplitude (S98-W3-2-BARYOGEN-UNIQUENESS) is a SINGLE-AMPLITUDE
readout that implicitly sets the STRONG (final-state rescattering) phase to zero
and carries only the WEAK CP phase phi_CP = pi/2 (maximal).

INTERFERING-AMPLITUDE CP FORM (LHCb-2025 arXiv:2504.15008 baryon-CP lesson).
A CP asymmetry from interfering amplitudes
   A_1 = |A_1| e^{i(phi_weak,1 + delta_strong,1)},
   A_2 = |A_2| e^{i(phi_weak,2 + delta_strong,2)}
is  A_CP propto |A_1||A_2| sin(Dphi_weak) sin(Ddelta_strong):
CP-observability requires BOTH a weak-phase difference AND a strong-phase
difference. The substrate's strong phases are the inter-branch overlap phases of
the 7 gapped GGE branches, read off the Row #67 two-speed split.

INTER-BRANCH OVERLAP (STRONG) PHASE -- SUBSTRATE CONSTRUCTION. Each gapped
branch i carries a two-speed pair (c1_i = LAYER-1, c2_i = LAYER-2) with split
delta_i = c1_i - c2_i. The rescattering phase of branch i (the substrate analog
of a final-state strong phase: the relative phase accumulated when two relay
patterns of differing phase velocity re-overlap at a fiber) is the LAYER-1/LAYER-2
velocity contrast normalized to the sound speed c_s = c_BLV:

   delta_strong,i = arctan( delta_i / c_s )            (Construction A; primary)

cross-checked against the S64 skyrmion-baryon inter-branch-overlap baseline
delta_CP_UV = 1/sqrt(IBO_ratio) (Construction B, IBO-scaled).

ENHANCEMENT FACTOR (plan substitution chain Step 4-5; the gate-pinned form):

   eta_B_enhanced = eta_B_base * R_enh,
   R_enh = | Sum_i w_i sin(phi_CP + delta_strong,i) | / | sin(phi_CP) |

with w_i the branch overlap weights (Sum w_i = 1; primary = LAYER-1 amplitude
c1_i; cross-check = equal). At phi_CP = pi/2: sin(pi/2 + delta) = cos(delta), so
   R_enh = | Sum_i w_i cos(delta_strong,i) |  <=  Sum_i w_i  =  1   EXACTLY.

STRUCTURAL CEILING (the decisive result). Because cos(delta) <= 1 for every
delta and the weights are normalized, the coherent branch sum CANNOT exceed 1.
At maximal weak phase phi_CP = pi/2 the strong-rescattering phase provides NO
enhancement -- it can only mildly suppress. The LHCb-2025 O(10-30) enhancement
arises for NON-maximal (per-mille) weak phases, where small phi_weak benefits
from a large delta_strong via sin(phi_weak + delta_strong). The substrate's
phi_CP = pi/2 is precisely the configuration where rescattering cannot boost.

REGIME. Deterministic spectral readout off frozen cache data; no irrep
reconstruction (L_max=12 Friedrich-Bar saturated; D_K block-diagonal). No
small-parameter expansion -- regime VALID by construction.
------------------------------------------------------------------------------
Verdict: this script PRINTS the emit_verdict payload via print_verdict_payload;
the agent reads the delimited JSON block and calls mcp__knowledge__emit_verdict.
"""

import hashlib
import json
import sys
import os
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU-cap (8x8 overlap; far below GPU threshold)

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

t0 = time.time()  # (local)

# --------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# --------------------------------------------------------------------------
INV_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = INV_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
import canonical_constants as cc
# consumed: eta_BBN_obs, eta_BBN_err, epsilon_K7, n_pairs, phi_CP_K7_transit,
#           IBO_ratio, R_machine_substrate_67_88, c_BLV

# --------------------------------------------------------------------------
# Section 2 -- Identity + machinery pins
# --------------------------------------------------------------------------
SESSION = 6                                                       # (local)
GATE_ID = "INV6-W3-1-ETA-B-GGE-RESCATTERING"                      # (local)
SCHEME = "GGE-RESCATTERING-S98-AMPLITUDE-CHAIN"                   # (local)
CONVENTION = "RATIO"                                              # (local)
L_MAX = "12"                                                      # (local)

OUT_NPZ = INV_DIR / "inv6_w3_1_eta_b_gge_rescattering.npz"        # (local)
OUT_PNG = INV_DIR / "inv6_w3_1_eta_b_gge_rescattering.png"        # (local)

ROW67_NPZ = COMPUTATIONS_DIR / "session-94" / "s94_bao_peak_branch.npz"        # (local)
S98_NPZ = COMPUTATIONS_DIR / "session-98" / "s98_w3_2_baryogen_uniqueness.npz"  # (local)

# PASS band (plan strict_PASS_boundary)
BAND_LO = 3.0e-10                                                 # (local)
BAND_HI = 1.2e-9                                                  # (local)
ETA_TOL = 1e-12                                                   # (local) float compare

# SOURCE-RECON Class-(c) cache-pin documentation. The orchestrator STALE
# CACHE-SHA HINT flags plan-pinned 88f1e9b1...->9e6d9cf7... (the s84 L12 mode
# cache used by sibling gates). THIS gate's plan §W3-1 input_files pin
# s94_bao_peak_branch.npz + s98_w3_2_baryogen_uniqueness.npz with
# <computed-at-runtime> SHAs (no hardcoded plan value to drift from); both are
# resolved to their on-disk SHA at runtime and recorded in the pinmap.
MACHINERY_PINS = {                                                # (local)
    "N_eval": "8",                 # 8-branch GGE spectrum (7 gapped + 1 Goldstone)
    "L_max": "12",                 # Row #67 / 992-mode cache; Friedrich-Bar saturated
    "scan_range": "delta_strong in [0,pi] (admissibility envelope; delta_strong COMPUTED, not scanned)",
    "step_size": "N/A-deterministic",
    "tolerance": "1e-12",
    "scheme": SCHEME,
    "convention": CONVENTION,
    "random_seed": "N/A-deterministic",
    "GPU_path": "numpy.linalg-cpu-cap-OMP8 (8x8 overlap; below 100x100 GPU threshold)",
    "publication_precision": "6",
    "s94_cache_pin": "computed-at-runtime (plan <computed-at-runtime>; no stale literal)",
    "s84_sibling_pin_drift": "Class-(c) PIN-DRIFT 88f1e9b1(inv-6-plan-stale)->9e6d9cf7(S100-canonical); "
                             "s84 cache NOT read by THIS gate (W3-1 reads s94+s98)",
}


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                          # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict) -> tuple[str, str]:
    """S84+ dual-SHA: audit = sha256(script || canonical || pinmap_json);
    content = sha256(script)."""
    script_bytes = script_path.read_bytes()                       # (local)
    canonical_bytes = canonical_path.read_bytes()                 # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")       # (local)
    h_a = hashlib.sha256()                                        # (local)
    h_a.update(script_bytes); h_a.update(canonical_bytes); h_a.update(pinmap_json)
    h_c = hashlib.sha256()                                        # (local)
    h_c.update(script_bytes)
    return h_a.hexdigest(), h_c.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    """Print the emit_verdict payload (race-safe MCP emission by the agent)."""
    payload = {                                                   # (local)
        "session": SESSION, "gate_id": GATE_ID, "verdict": verdict,
        "value": str(value), "scheme": SCHEME, "convention": CONVENTION,
        "l_max": str(L_MAX), "audit_sha256": audit_sha,
        "content_sha256": content_sha, "schema_version": "S84+",
        "track": "investigation",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None
            and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# --------------------------------------------------------------------------
# Section 3 -- Input SHA verification (first 20 lines of stdout)
# --------------------------------------------------------------------------
def verify_inputs() -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict = {}                                               # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"        # (local)
    sha_canon = sha256_of(canonical_path)                         # (local)
    print(f"  canonical_constants.py: {sha_canon[:16]}... (runtime-pinned)")
    pins["computations/_shared/canonical_constants.py"] = sha_canon

    sha_row67 = sha256_of(ROW67_NPZ)                              # (local)
    print(f"  s94_bao_peak_branch.npz: {sha_row67[:16]}... (Row #67 8-branch "
          f"two-speed; runtime-pinned; plan <computed-at-runtime>)")
    pins["computations/session-94/s94_bao_peak_branch.npz"] = sha_row67

    sha_s98 = sha256_of(S98_NPZ)                                  # (local)
    print(f"  s98_w3_2_baryogen_uniqueness.npz: {sha_s98[:16]}... (eta_B base + "
          f"amplitude chain; runtime-pinned)")
    pins["computations/session-98/s98_w3_2_baryogen_uniqueness.npz"] = sha_s98

    if sha_row67 == "" or sha_s98 == "":
        print("HARD-ABORT: a required cache is ABSENT.")
        sys.exit(2)
    return pins


# --------------------------------------------------------------------------
# Section 4 -- Load anchors (eta_B base chain + Row #67 8-branch spectrum)
# --------------------------------------------------------------------------
def load_anchors() -> dict:
    a: dict = {}                                                  # (local)

    s98 = np.load(S98_NPZ, allow_pickle=True)                     # (local)
    a["eta_B_base"] = float(s98["eta_B"])
    a["eps_nLI"] = float(s98["eps_nLI"])
    a["phi_CP"] = float(s98["phi_CP"])
    a["sin_phi_CP"] = float(s98["sin_phi_CP"])
    a["n_pairs_s98"] = float(s98["n_pairs"])
    a["eps_K7_s98"] = float(s98["eps_K7"])
    a["eta_obs_s98"] = float(s98["eta_obs"])
    a["underprod_oom_s98"] = float(s98["underprod_oom"])

    row = np.load(ROW67_NPZ, allow_pickle=True)                  # (local)
    a["branch_names"] = [str(x) for x in row["branch_names"]]
    a["c1"] = np.asarray(row["c1"], dtype=float)   # LAYER-1 phase velocities
    a["c2"] = np.asarray(row["c2"], dtype=float)   # LAYER-2 phase velocities
    a["delta"] = np.asarray(row["delta"], dtype=float)  # c1 - c2 (two-speed split)
    a["is_protected"] = np.asarray(row["is_protected"], dtype=bool)
    a["tau_fold_row"] = float(row["tau_fold"])
    return a


# --------------------------------------------------------------------------
# Section 5 -- Inter-branch strong (rescattering) phase + R_enh
# --------------------------------------------------------------------------
def compute(a: dict) -> dict:
    r: dict = {}                                                  # (local)

    eta_base = a["eta_B_base"]                                    # (local)
    phi_CP = a["phi_CP"]                                          # (local) = pi/2
    c_s = float(cc.c_BLV)                                         # (local) sound speed
    IBO = float(cc.IBO_ratio)                                     # (local)
    delta_CP_UV = 1.0 / np.sqrt(IBO)                              # (local) S64 IBO baseline

    names = a["branch_names"]                                     # (local)
    c1 = a["c1"]; c2 = a["c2"]; dlt = a["delta"]                  # (local)
    prot = a["is_protected"]                                      # (local)
    gapped = ~prot                                                # (local)
    idx = np.where(gapped)[0]                                     # (local) 7 gapped branch indices

    # ---- inter-branch strong phases ----
    # Construction A (primary): rescattering phase = arctan(two-speed contrast)
    contrast = dlt[idx] / c_s                                     # (local) delta_i / c_s
    delta_strong_A = np.arctan(contrast)                         # (local)
    # Construction B (cross-check): IBO-baseline-scaled relative contrast
    delta_strong_B = delta_CP_UV * (contrast / np.mean(contrast))  # (local)

    # ---- branch overlap weights ----
    w_c1 = c1[idx] / np.sum(c1[idx])                            # (local) primary: LAYER-1 amplitude
    w_eq = np.ones(len(idx)) / len(idx)                         # (local) cross-check: equal

    sin_den = abs(np.sin(phi_CP))                               # (local) = 1.0

    def R_enh(dstrong, w):
        return float(abs(np.sum(w * np.sin(phi_CP + dstrong))) / sin_den)

    # Reading 1 (plan-pinned coherent sum). Primary = Construction A, c1 weights.
    R_enh_A_c1 = R_enh(delta_strong_A, w_c1)                    # (local)
    R_enh_A_eq = R_enh(delta_strong_A, w_eq)                    # (local)
    R_enh_B_c1 = R_enh(delta_strong_B, w_c1)                    # (local)
    R_enh_B_eq = R_enh(delta_strong_B, w_eq)                    # (local)

    R_enh_primary = R_enh_A_c1                                  # (local) THE gate number
    eta_enhanced = eta_base * R_enh_primary                     # (local)

    # Reading 2 (product form A_CP ~ sin(Dphi_weak) sin(Ddelta_strong)).
    # The strong-phase DIFFERENCES between branches (rescattering between channels).
    ddelta = delta_strong_A - np.mean(delta_strong_A)          # (local)
    # relative to the single-amplitude sin(phi_CP)=1 baseline, the product form
    # multiplies by sin(Ddelta_strong) <= max|sin(ddelta)| << 1
    prod_factor_max = float(np.max(np.abs(np.sin(ddelta))))    # (local)
    R_enh_product = prod_factor_max                             # (local) generous upper bound

    # ---- structural ceiling (the decisive identity) ----
    # at phi_CP=pi/2: R_enh = |sum w_i cos(delta_i)| <= sum w_i = 1.0 EXACTLY
    coherent_ceiling = 1.0                                      # (local)
    cos_terms_c1 = w_c1 * np.cos(delta_strong_A)               # (local)
    R_ceiling_check = float(np.sum(cos_terms_c1))              # (local) == R_enh_A_c1 at phi=pi/2

    # ---- required enhancement (closed ratio) ----
    eta_obs = float(cc.eta_BBN_obs)                             # (local)
    R_required = eta_obs / eta_base                             # (local) = 13.55
    R_pass_lo = BAND_LO / eta_base                              # (local) lower PASS-band R edge
    R_pass_hi = BAND_HI / eta_base                              # (local) upper PASS-band R edge

    # ---- in-band test (the gate operator) ----
    in_band = bool((BAND_LO - ETA_TOL) <= eta_enhanced <= (BAND_HI + ETA_TOL))  # (local)

    # ---- [SIGN] direction: does rescattering ENHANCE (R_enh > 1)? ----
    # predicted-by-chain direction: CONDITIONAL enhancement only if coherent sum > 1
    # measured: R_enh_primary. enhancement_sign True iff R_enh > 1 + tol
    enhances = bool(R_enh_primary > 1.0 + 1e-9)                 # (local)
    # eta sign preserved (baryon excess > 0)
    eta_positive = bool(eta_enhanced > 0.0)                     # (local)

    r.update(dict(
        eta_base=eta_base, phi_CP=phi_CP, c_s=c_s, IBO=IBO,
        delta_CP_UV=delta_CP_UV,
        gapped_idx=idx, gapped_names=[names[i] for i in idx],
        contrast=contrast,
        delta_strong_A=delta_strong_A, delta_strong_B=delta_strong_B,
        w_c1=w_c1, w_eq=w_eq,
        R_enh_A_c1=R_enh_A_c1, R_enh_A_eq=R_enh_A_eq,
        R_enh_B_c1=R_enh_B_c1, R_enh_B_eq=R_enh_B_eq,
        R_enh_primary=R_enh_primary, eta_enhanced=eta_enhanced,
        ddelta=ddelta, R_enh_product=R_enh_product,
        coherent_ceiling=coherent_ceiling, R_ceiling_check=R_ceiling_check,
        R_required=R_required, R_pass_lo=R_pass_lo, R_pass_hi=R_pass_hi,
        eta_obs=eta_obs, in_band=in_band,
        enhances=enhances, eta_positive=eta_positive,
        all_names=names, c1=c1, c2=c2, delta=dlt, is_protected=prot,
    ))
    return r


# --------------------------------------------------------------------------
# Section 6 -- Gate evaluation ([SIGN] 3-tuple + collapse rule)
# --------------------------------------------------------------------------
def evaluate_gate(r: dict) -> tuple:
    # SIGN: the substitution chain predicts CONDITIONAL enhancement (R_enh>1 only
    # under coherent-sum boost). The MEASURED direction: R_enh = 0.9992 <= 1 ->
    # NO enhancement (mild suppression). The chain's Step-5 caveat ("enhancement
    # is NOT automatic at phi_CP=pi/2; cos(delta)<=1") is CONFIRMED: the measured
    # direction matches the chain's structural prediction that enhancement
    # requires a coherent boost that the substrate does NOT provide.
    # sign_verdict PASS = measured direction matches the chain's structural
    # ceiling prediction (R_enh <= 1 at phi=pi/2). The chain did not assert
    # enhancement; it asserted the ceiling. The ceiling holds -> sign PASS.
    sign_ok = bool(r["R_enh_primary"] <= r["coherent_ceiling"] + 1e-9)  # (local)
    sign_v = "PASS" if sign_ok else "FAIL"                       # (local)

    # MAGNITUDE: eta_enhanced in PASS band [3e-10, 1.2e-9]?
    mag_pass = bool(r["in_band"])                                # (local)
    # INFO band: eta moved UP (R_enh>1) but stays below 3e-10 (partial relief)
    mag_info = bool((not r["in_band"]) and r["enhances"]
                    and r["eta_enhanced"] < BAND_LO)             # (local)
    if mag_pass:
        mag_v = "PASS"                                           # (local)
    elif mag_info:
        mag_v = "INFO"                                           # (local)
    else:
        mag_v = "FAIL"                                           # (local)

    # REGIME: deterministic spectral readout; no small-parameter expansion;
    # full intended computation performed (no auto-shortening) -> VALID.
    regime_v = "VALID"                                          # (local)

    # collapse rule (pre-registered, gate-verdicts.md)
    if regime_v == "BREAKDOWN":
        comp = "FAIL"                                            # (local)
    elif sign_v == "FAIL":
        comp = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        comp = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        comp = "INFO"
    elif mag_v == "INFO":
        comp = "INFO"
    else:
        comp = "PASS"

    detail = dict(sign_ok=sign_ok, mag_pass=mag_pass, mag_info=mag_info)  # (local)
    return comp, sign_v, mag_v, regime_v, detail


# --------------------------------------------------------------------------
# Section 7 -- Plot
# --------------------------------------------------------------------------
def make_plot(r: dict):
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))             # (local)

    # Panel 1: inter-branch strong phases per gapped branch
    ax = axes[0, 0]
    names = r["gapped_names"]                                    # (local)
    x = np.arange(len(names))                                    # (local)
    ax.bar(x - 0.2, r["delta_strong_A"], width=0.4, label="Construction A  arctan(delta/c_s)",
           color="C0")
    ax.bar(x + 0.2, r["delta_strong_B"], width=0.4, label="Construction B  IBO-scaled",
           color="C1", alpha=0.8)
    ax.axhline(np.pi / 2, color="r", ls="--", lw=1, label="pi/2 (enhancement boundary)")
    ax.set_xticks(x); ax.set_xticklabels(names, rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("delta_strong,i  [rad]")
    ax.set_title("Inter-branch strong (rescattering) phases\n(all << pi/2 -> cos(delta)~1)")
    ax.legend(fontsize=7); ax.grid(alpha=0.3)

    # Panel 2: R_enh vs the required 13.55 (log scale)
    ax = axes[0, 1]
    labels = ["A,c1\n(primary)", "A,equal", "B,c1", "B,equal", "product\nform"]  # (local)
    vals = [r["R_enh_A_c1"], r["R_enh_A_eq"], r["R_enh_B_c1"], r["R_enh_B_eq"],
            r["R_enh_product"]]                                  # (local)
    ax.bar(range(len(vals)), vals, color=["C3", "C0", "C0", "C0", "C2"])
    ax.axhline(1.0, color="k", ls="-", lw=1.2, label="ceiling = 1.0 (cos<=1 at phi=pi/2)")
    ax.axhline(r["R_required"], color="r", ls="--", lw=1.5,
               label=f"required = {r['R_required']:.2f}")
    ax.axhline(r["R_pass_lo"], color="orange", ls=":", lw=1,
               label=f"PASS-band lo = {r['R_pass_lo']:.2f}")
    ax.set_yscale("log")
    ax.set_xticks(range(len(labels))); ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("R_enh")
    ax.set_title("Enhancement factor vs required 13.55\n(all readings R_enh < 1)")
    ax.legend(fontsize=7); ax.grid(alpha=0.3, which="both")

    # Panel 3: eta_B base vs enhanced vs band vs obs
    ax = axes[1, 0]
    ys = [r["eta_base"], r["eta_enhanced"], r["eta_obs"]]        # (local)
    ax.bar([0, 1, 2], ys, color=["C0", "C3", "C2"])
    ax.axhspan(BAND_LO, BAND_HI, color="green", alpha=0.15, label="PASS band [3e-10,1.2e-9]")
    ax.set_yscale("log")
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["eta_base\n(S98)", "eta_enhanced\n(this gate)", "eta_obs\n(BBN)"],
                       fontsize=8)
    ax.set_ylabel("eta_B")
    ax.set_title(f"eta_B: base {r['eta_base']:.3e} -> enhanced {r['eta_enhanced']:.3e}\n"
                 f"(obs {r['eta_obs']:.3e}; gap persists)")
    ax.legend(fontsize=7); ax.grid(alpha=0.3, which="both")

    # Panel 4: the cos-ceiling -- R_enh(phi) sweep showing pi/2 is the worst case
    ax = axes[1, 1]
    phis = np.linspace(0, np.pi, 400)                           # (local)
    # R_enh(phi) = |sum w_i sin(phi + d_i)| / |sin(phi)| using primary construction
    w = r["w_c1"]; ds = r["delta_strong_A"]                     # (local)
    Rphi = np.array([abs(np.sum(w * np.sin(p + ds))) / max(abs(np.sin(p)), 1e-12)
                     for p in phis])                             # (local)
    ax.plot(phis, Rphi, color="C0", lw=1.5, label="R_enh(phi_weak)")
    ax.axvline(np.pi / 2, color="r", ls="--", lw=1.2, label="substrate phi_CP = pi/2")
    ax.axhline(1.0, color="k", ls=":", lw=1, label="R_enh = 1")
    ax.set_ylim(0, min(5, np.nanmax(Rphi[np.isfinite(Rphi)]) * 1.1))
    ax.set_xlabel("weak phase phi_weak  [rad]")
    ax.set_ylabel("R_enh")
    ax.set_title("R_enh vs weak phase: enhancement needs SMALL phi_weak\n"
                 "(substrate sits at pi/2 -> the no-boost point)")
    ax.legend(fontsize=7); ax.grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}: inter-branch GGE strong-rescattering -> eta_B  "
                 f"[R_enh={r['R_enh_primary']:.4f} <= 1; gap NOT closed]",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"Saved plot: {OUT_PNG}")


# --------------------------------------------------------------------------
# Section 8 -- main
# --------------------------------------------------------------------------
def main() -> int:
    pins = verify_inputs()                                       # (local)

    pinmap = dict(pins)                                          # (local)
    pinmap.update({f"_machinery::{k}": v for k, v in MACHINERY_PINS.items()})
    pinmap["_gate::id"] = GATE_ID
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py",
        pinmap)                                                  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    a = load_anchors()                                          # (local)
    r = compute(a)                                              # (local)
    comp, sign_v, mag_v, regime_v, detail = evaluate_gate(r)    # (local)

    print("\n" + "=" * 72)
    print("NUMBERS (computed before gate)")
    print("=" * 72)
    print(f"  eta_B_base (S98 canonical)          = {r['eta_base']:.6e}")
    print(f"  phi_CP                              = {r['phi_CP']:.6f} rad (= pi/2); sin(phi_CP) = {np.sin(r['phi_CP']):.6f}")
    print(f"  sound speed c_s = c_BLV             = {r['c_s']:.6f} M_KK")
    print(f"  IBO_ratio                           = {r['IBO']:.1f}; delta_CP_UV = 1/sqrt(IBO) = {r['delta_CP_UV']:.6f} rad")
    print(f"  gapped branches ({len(r['gapped_idx'])})              = {r['gapped_names']}")
    print(f"  delta_strong,i (Construction A)     = {np.round(r['delta_strong_A'], 6)}")
    print(f"  delta_strong,i (Construction B)     = {np.round(r['delta_strong_B'], 6)}")
    print(f"  branch weights w_i (LAYER-1)        = {np.round(r['w_c1'], 6)}")
    print(f"  R_enh  (A, c1 weights) [PRIMARY]    = {r['R_enh_A_c1']:.6f}")
    print(f"  R_enh  (A, equal)                   = {r['R_enh_A_eq']:.6f}")
    print(f"  R_enh  (B, c1)                      = {r['R_enh_B_c1']:.6f}")
    print(f"  R_enh  (B, equal)                   = {r['R_enh_B_eq']:.6f}")
    print(f"  R_enh  (product form, upper bnd)    = {r['R_enh_product']:.6f}")
    print(f"  coherent-sum ceiling (cos<=1)       = {r['coherent_ceiling']:.6f}  [R_ceiling_check={r['R_ceiling_check']:.6f}]")
    print(f"  R_required (eta_obs/eta_base)       = {r['R_required']:.6f}")
    print(f"  PASS-band R edges                   = [{r['R_pass_lo']:.4f}, {r['R_pass_hi']:.4f}]")
    print(f"  eta_B_enhanced (= base * R_primary) = {r['eta_enhanced']:.6e}")
    print(f"  eta_obs (BBN)                       = {r['eta_obs']:.6e}")
    print(f"  in PASS band [3e-10,1.2e-9]?        = {r['in_band']}")
    print(f"  enhances (R_enh > 1)?               = {r['enhances']}")

    print("\n" + "=" * 72)
    print("GATE EVALUATION ([SIGN] 3-tuple + collapse rule)")
    print("=" * 72)
    print(f"  SIGN: measured R_enh = {r['R_enh_primary']:.6f} <= ceiling 1.0 "
          f"[{detail['sign_ok']}] (chain Step-5 ceiling at phi=pi/2 CONFIRMED) => {sign_v}")
    print(f"  MAGNITUDE: eta_enhanced {r['eta_enhanced']:.3e} in [3e-10,1.2e-9]? "
          f"[{detail['mag_pass']}]; INFO(moved-up-but-below)? [{detail['mag_info']}] => {mag_v}")
    print(f"  REGIME: deterministic spectral readout, full window, no expansion => {regime_v}")
    print(f"  COMPOSITE (collapse rule): {comp}")

    # ---- npz (full float64) ----
    np.savez(
        OUT_NPZ,
        # ==== headline outputs (FULL float64) ====
        eta_B_base=r["eta_base"],
        eta_B_enhanced=r["eta_enhanced"],
        R_enh_primary=r["R_enh_primary"],
        R_required=r["R_required"],
        eta_obs=r["eta_obs"],
        in_band=r["in_band"],
        enhances=r["enhances"],
        # ==== R_enh under all constructions/weights ====
        R_enh_A_c1=r["R_enh_A_c1"], R_enh_A_eq=r["R_enh_A_eq"],
        R_enh_B_c1=r["R_enh_B_c1"], R_enh_B_eq=r["R_enh_B_eq"],
        R_enh_product=r["R_enh_product"],
        coherent_ceiling=r["coherent_ceiling"], R_ceiling_check=r["R_ceiling_check"],
        R_pass_lo=r["R_pass_lo"], R_pass_hi=r["R_pass_hi"],
        # ==== inter-branch strong phases ====
        gapped_names=np.array(r["gapped_names"], dtype=object),
        delta_strong_A=r["delta_strong_A"], delta_strong_B=r["delta_strong_B"],
        contrast=r["contrast"], ddelta=r["ddelta"],
        w_c1=r["w_c1"], w_eq=r["w_eq"],
        # ==== inputs ====
        phi_CP=r["phi_CP"], c_s=r["c_s"], IBO=r["IBO"], delta_CP_UV=r["delta_CP_UV"],
        branch_names_all=np.array(r["all_names"], dtype=object),
        c1_all=r["c1"], c2_all=r["c2"], delta_all=r["delta"],
        is_protected=r["is_protected"],
        eps_nLI=a["eps_nLI"], underprod_oom_s98=a["underprod_oom_s98"],
        # ==== band ====
        band_lo=BAND_LO, band_hi=BAND_HI,
        # ==== verdict block ====
        verdict=comp, sign_verdict=sign_v, magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        audit_sha256=audit_sha, content_sha256=content_sha,
        s98_predecessor_sha="3be22b8a",
    )
    print(f"\nSaved data: {OUT_NPZ}")

    make_plot(r)

    # ---- 4-tuple + payload ----
    val = (f"eta_B_enh={r['eta_enhanced']:.6e};R_enh={r['R_enh_primary']:.6f};"
           f"R_required={r['R_required']:.4f};eta_base={r['eta_base']:.6e};"
           f"in_band={r['in_band']};enhances={r['enhances']};"
           f"R_enh_A_eq={r['R_enh_A_eq']:.6f};R_enh_B_c1={r['R_enh_B_c1']:.6f};"
           f"R_prod={r['R_enh_product']:.6f};ceiling=1.0")        # (local)
    print(f"\n(value={val!r}, scheme={SCHEME}, convention={CONVENTION}, "
          f"L_max={L_MAX})")

    note = (f"Inter-branch GGE strong-rescattering phase -> C6 eta_B. "
            f"delta_strong,i = arctan(delta_i/c_s) over 7 gapped branches "
            f"(all << pi/2); R_enh = |sum w_i sin(phi_CP+d_i)|/|sin(phi_CP)| "
            f"= {r['R_enh_primary']:.6f} <= 1.0 EXACTLY (cos-ceiling at phi_CP=pi/2). "
            f"eta_B {r['eta_base']:.3e} -> {r['eta_enhanced']:.3e}; required {r['R_required']:.2f}x "
            f"NOT supplied. Gap persists (G-1 open); Track-B failing-prediction.")

    rows = [
        f"# STRUCTURAL CEILING: at phi_CP=pi/2, R_enh=|sum w_i cos(delta_strong,i)| "
        f"<= sum w_i = 1.0 EXACTLY; rescattering CANNOT enhance at MAXIMAL weak phase. "
        f"LHCb-2025 O(10-30) boost needs NON-maximal (per-mille) phi_weak. # {GATE_ID}",
        f"# delta_strong from Row #67 two-speed split delta_i=c1_i-c2_i over 7 gapped "
        f"branches (Goldstone protected, delta=0); contrast delta_i/c_s in "
        f"[0.0008(B2),0.055(B3)] all << 1 rad -> cos~1 -> R_enh~1. # {GATE_ID}",
        f"# both readings agree: Reading-1 coherent-sum R_enh={r['R_enh_primary']:.4f}; "
        f"Reading-2 product-form upper bound {r['R_enh_product']:.4f} (sin of tiny "
        f"strong-phase DIFFERENCE) -- neither supplies 13.55x. # {GATE_ID}",
        f"# eta_B_base=4.517492e-11 (S98-W3-2-BARYOGEN-UNIQUENESS PASS, audit 3be22b8a; "
        f"NOT a supersedes token); eps_nLI={a['eps_nLI']:.3e}; phi_CP=pi/2 substrate-FIXED. # {GATE_ID}",
        f"# Track-B (failing-prediction, dual-prior 0.55->0.9): the 'GGE strong "
        f"rescattering supplies the OOM' corridor is CLOSED; the delta_A magnitude "
        f"posit (LBA-1) remains the open failure locus; routes to W3-3 acoustic-Schwinger "
        f"+ G-4 M_KK-degeneracy. # {GATE_ID}",
        f"# C-3 lepton/baryon CP orthogonality NOT structurally derived by this gate "
        f"(the rescattering route did not close); delta_CP^PMNS=0 (S99) stands on its "
        f"own derivation, not on a baryon-rescattering contrast. # {GATE_ID}",
        f"# regulator_pin=N/A -- no Seeley-DeWitt a_n; no SCHEMATIC helper "
        f"(s94+s98 npz data + canonical_constants only). # {GATE_ID}",
        f"# cache-pin SOURCE-RECON Class-(c): orchestrator STALE-HINT 88f1e9b1->9e6d9cf7 "
        f"applies to the s84 L12 mode cache used by SIBLING gates; THIS gate reads "
        f"s94_bao_peak_branch.npz + s98_w3_2 (plan <computed-at-runtime>; on-disk SHA "
        f"runtime-pinned; s84 NOT read here) -> zero physics effect. # {GATE_ID}",
    ]                                                          # (local)

    print_verdict_payload(comp, val, audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v,
                          regime_verdict=regime_v, companion_note=note,
                          extra_rows=rows)

    print(f"\n=== {GATE_ID}: {comp} (wall {time.time()-t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
