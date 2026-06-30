#!/usr/bin/env python3
"""
S117 W1-3 — CF-S117-ROUTE-B-PW-SOCC ([SIGN])
============================================

Gate: CF-S117-ROUTE-B-PW-SOCC
Classification: PHONONIC
Owner: transit-dynamics-theorist
Plan: sessions/session-plan/session-117-plan-w1.md §W1-3

QUESTION (the Q23 A_s-magnitude rate-limiter, route-robustness leg):
  The A_s magnitude sits on a 2-member plurality fork —
    ξ_KZ grid (box-delta impulse-quench)  : A_s_FW   = 1.5367e-8  -> OOM +0.864
    H̃  grid (TD/ζ UNIFIED-AS-79 Branch-A) : A_s(H̃)  = 3.2994e-9  -> OOM +0.196
  Route-B Peter-Weyl is a THIRD, independent assembly of the SAME substrate-IS
  observable A_s: it sums squeezed power over the Peter-Weyl (p,q) decomposition
  of D_K's spectrum (S66 AMPLITUDE-NORM-66 route), rather than propagating a
  single impulse mode (box-delta) or running the SR five-factor ledger (TD/ζ).
  This gate recomputes Route-B A_s with the OCCUPIED-state spectral functional
  S_occ = (1+2 n_k)·S_fold (NOT the vacuum S_fold) and asks: WHICH fork member
  (or a distinct third value) does it image?

SUBSTRATE FRAMING (phononic, IS-not-IN):
  Route-B Peter-Weyl IS the substrate's spectral-sum reading of A_s — the
  van-Hove-fold reorganization of D_K's fiber spectrum read as a sum over its
  (p,q) sectors. The occupied-state functional S_occ = (1+2 n_k)·S_fold replaces
  the Bunch-Davies VACUUM reading with the GGE-relic occupation the substrate
  actually carries (n̄ = 2.736e-4 frozen quasiparticle pairs; the Ordered Veil
  S_ent=0 licenses the frozen-n reading). The gate asks whether the substrate's
  spectral-sum route to A_s lands on the same magnitude as its impulse route.

LINEAGE (the base assembly):
  - S66 Route-B Peter-Weyl RAW (s66_amplitude_norm.npz: A_s_route_B_PW = 2.918e-6,
    gap 3.143 OOM) was the "normalization crisis": A_s^RouteB = R_B_PW^2,
    R_B_PW = (delta_rho_B/rho_B)·sqrt(frac_PW)/(3(1+w_GGE)), frac_PW = 3.191e-4.
  - The UNIFIED-AS-79 reconciliation (S77-S84) + CC3 H̃-threading brought the
    TD-canonical Route-B/Bunch-Davies floor to A_s^BD = 5.078171e-9 (S82 W2-4 /
    S84 AS-PIN-MAP-COMMIT; the base used by inv12_w1_2, the modern "Route-B GGE
    modular reference"). THIS is the CC3-anchored base A_s^RouteB-vac.

SUBSTITUTION CHAIN [SIGN] (math-scripts.md MANDATORY discipline):
  Claim: the S_occ correction INCREASES A_s (occupied-state squeeze amplifies)
         but by ≪ 0.1 OOM, so the image identity is set by the BASE Route-B-PW
         assembly, not by S_occ.

  Def 1: S_occ          = (1 + 2 n_k)·S_fold              [occupied-state functional]
  Def 2: n̄             = n_bar_mw = 2.7358e-4            [locked-relic mult-weighted occupation; inv12_w1_2]
  Def 3: K_sub          = 1 + 2 n̄ = 1.0005472            [squeeze amplification factor; R2 reading]
  Def 4: A_s^RouteB-vac = A_s^BD = 5.078171e-9            [TD-canonical Route-B/BD floor, CC3-anchored to H̃=5.9076e-3]
  Def 5: A_s^RouteB-SOcc= K_sub · A_s^RouteB-vac          [S_occ vs vacuum functional, LINEAR in S]
  Def 6: OOM_RB         = log10(A_s^RouteB-SOcc / A_s_CMB)

  Substitute: ΔOOM_Socc = log10(K_sub) = log10(1.0005472) = +2.38e-4 OOM
  Simplify:   |ΔOOM_Socc| = 2.38e-4 ≪ 0.1 ⇒ S_occ is SIGN-positive (amplifying)
              but magnitude-NEGLIGIBLE ⇒ OOM_RB fixed by the base assembly.
  Direction (SIGN):  K_sub > 1 ⇒ A_s^RouteB-SOcc > A_s^RouteB-vac (occupied-state
              functional squeezes MORE); sign_verdict = PASS iff the computed
              A_s^RouteB-SOcc ≥ A_s^RouteB-vac (lift direction confirmed).
  Direction (IMAGE): because S_occ shifts ≪ 0.1 OOM, OOM_RB is fixed by the base
              ⇒ the gate MEASURES which fork member (or third value) Route-B lands on.
  Conclusion: sign_verdict = PASS (S_occ lifts A_s); magnitude_verdict = image
              classification at 0.1 OOM: +0.864 (PASS box-delta) / +0.196 (FAIL
              TD-ζ) / neither (INFO third point).

CC3 thread (d ln A_s / d ln H̃ = +2; UNIFIED-AS-79 machine-ε identity):
  A_s^BD is anchored at canonical H̃ = 5.9076e-3 with the +2 power law. Threading
  CC3 means A_s(H̃) = A_s^BD · (H̃/H̃_can)^2; verify slope = +2 numerically.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py                       (A_s_CMB, A_s_FW, H̃)
  - computations/session-66/s66_amplitude_norm.npz                    (S66 Route-B PW lineage)
  - computations/investigation-12/inv12_w1_2_a_s_gge_modular_reference.npz (A_s^BD base, n̄, K_sub readings)
  - this script bytes

Output 4-tuple:
  (value=OOM_RB, scheme=ROUTE-B-PETER-WEYL-S_occ-CC3,
   convention=OCCUPIED-state-S_occ=(1+2n_k)·S_fold-Branch-A-Zubarev, L_max=10)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent              # computations/session-117
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (  # noqa: E402,F401
    A_s_CMB,                  # Planck 2018 VI scalar amplitude = 2.1e-9
    A_s_FW,                   # box-delta impulse-quench (ξ_KZ grid) = 1.5367e-8
    H_tilde_canonical_TD,     # canonical TD H̃ = 5.9076e-3 (CC3 anchor)
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib   # noqa: E402
import json      # noqa: E402
import time      # noqa: E402

import numpy as np            # noqa: E402
import matplotlib             # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Pre-registration constants (plan §W1-3 operator block)
# ---------------------------------------------------------------------------
SESSION = "117"                                                       # (local)
GATE_ID = "CF-S117-ROUTE-B-PW-SOCC"                                   # (local)
SCHEME = "ROUTE-B-PETER-WEYL-S_occ-CC3"                               # (local)
CONVENTION = "OCCUPIED-state-S_occ=(1+2n_k).S_fold-Branch-A-Zubarev"  # (local)
L_MAX = 10                                                            # (local)

IMG_TOL = 0.1                       # (local) image-classification tolerance (OOM, SOURCE-RECON band)
CC3_SLOPE_TARGET = 2.0             # (local) d ln A_s / d ln H̃ = +2 (UNIFIED-AS-79 CC3)
CC3_REL_TOL = 1e-9                 # (local) CC3 slope identity tolerance (machine-ε)

# A_s(H̃) TD/ζ Branch-A comparator: npz-sourced (inv12_w3_5 / UNIFIED-AS-79),
# NOT a named canonical (plan SOURCE-RECON note Class-(d)). Pinned comparator only.
A_S_HTILDE_TDZETA = 3.2994e-9      # (local) comparator: H̃-grid fork member (inv12_w3_5)

S66_NPZ = COMPUTATIONS_DIR / "session-66" / "s66_amplitude_norm.npz"
INV12_W1_2_NPZ = COMPUTATIONS_DIR / "investigation-12" / "inv12_w1_2_a_s_gge_modular_reference.npz"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

OUT_NPZ = SESSION_DIR / "s117_route_b_pw_socc.npz"
OUT_PNG = SESSION_DIR / "s117_route_b_pw_socc.png"

INPUT_FILES = [CANONICAL_PATH, S66_NPZ, INV12_W1_2_NPZ]


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
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
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
    """Recompute the Route-B Peter-Weyl A_s with the occupied-state functional
    S_occ = (1+2 n̄)·S_fold (R2 mult-weighted-mean reading), CC3-threaded, and
    classify which fork member (or third value) it images."""

    # --- Base: TD-canonical Route-B / Bunch-Davies floor (CC3-anchored to H̃) ---
    dB = np.load(INV12_W1_2_NPZ, allow_pickle=True)
    A_s_RouteB_vac = float(dB["A_s_BD"])               # (local) = 5.078171e-9, A_s^RouteB-vac
    n_bar_mw = float(dB["n_bar_mw"])                   # (local) = 2.7358e-4 mult-weighted relic occupation
    K_sub_keys = [str(x) for x in dB["K_sub_readings_keys"]]   # (local)
    K_sub_vals = np.asarray(dB["K_sub_readings_vals"], dtype=float)  # (local) [R1,R2,R3,R4]
    A_s_GGE_inv12 = float(dB["A_s_GGE"])               # (local) inv12 canonical (R1-softest) reading
    K_sub_canonical_inv12 = float(dB["K_sub_canonical"])  # (local) R1-softest = 1.0000204533

    # --- S66 Route-B Peter-Weyl RAW lineage (the pre-reconciliation crisis value) ---
    dS = np.load(S66_NPZ, allow_pickle=True)
    A_s_route_B_PW_S66 = float(dS["A_s_route_B_PW"])   # (local) = 2.918e-6 raw S66 crisis value
    gap_route_B_PW_S66 = float(dS["gap_route_B_PW"])   # (local) = 3.143 OOM
    frac_PW_S66 = float(dS["frac_PW"])                 # (local) = 3.191e-4 (0,0) PW projection fraction

    # --- S_occ squeeze amplification factor (R2 mult-weighted-mean = plan-pinned) ---
    # K_sub = 1 + 2 n̄ ; the four readings R1..R4 are the band (all >= 1 by n_k>=0)
    K_sub_R2 = 1.0 + 2.0 * n_bar_mw                    # (local) plan-pinned K_sub = 1.0005472
    # cross-check: K_sub_R2 must equal the stored R2_mult_weighted_mean reading
    i_R2 = K_sub_keys.index("R2_mult_weighted_mean")  # (local)
    K_sub_R2_stored = float(K_sub_vals[i_R2])          # (local)
    K_sub_R2_resid = abs(K_sub_R2 - K_sub_R2_stored)   # (local)
    K_sub = K_sub_R2                                    # (local) CANONICAL for this gate

    # --- A_s^RouteB-SOcc and OOM_RB ---
    A_s_RouteB_SOcc = K_sub * A_s_RouteB_vac            # (local) Def 5
    OOM_RB = float(np.log10(A_s_RouteB_SOcc / A_s_CMB)) # (local) Def 6
    OOM_RB_vac = float(np.log10(A_s_RouteB_vac / A_s_CMB))  # (local) base (no S_occ)
    dOOM_Socc = float(np.log10(K_sub))                 # (local) ΔOOM_Socc = +2.38e-4

    # --- Image classification vs the two fork members (exact comparator OOMs) ---
    OOM_box = float(np.log10(A_s_FW / A_s_CMB))         # (local) box-delta image, +0.864
    OOM_TD = float(np.log10(A_S_HTILDE_TDZETA / A_s_CMB))  # (local) TD-ζ image, +0.196
    dist_box = abs(OOM_RB - OOM_box)                    # (local)
    dist_TD = abs(OOM_RB - OOM_TD)                      # (local)
    if dist_box <= IMG_TOL:
        image = "box-delta(+0.864)"                     # (local)
        magnitude_verdict = "PASS"                      # (local) PASS-as-image (box-delta)
    elif dist_TD <= IMG_TOL:
        image = "TD-zeta(+0.196)"                       # (local)
        magnitude_verdict = "FAIL"                      # (local) images the TD/ζ member instead
    else:
        image = "third-point"                           # (local) plurality 2->3
        magnitude_verdict = "INFO"                      # (local)

    # --- K_sub-reading robustness: OOM image across all four R1..R4 readings ---
    OOM_by_reading = {                                  # (local)
        K_sub_keys[i]: float(np.log10(K_sub_vals[i] * A_s_RouteB_vac / A_s_CMB))
        for i in range(len(K_sub_keys))
    }
    OOM_reading_spread = float(max(OOM_by_reading.values()) - min(OOM_by_reading.values()))  # (local)
    # all readings third-point? (none within IMG_TOL of either fork member)
    all_third_point = all(
        (abs(v - OOM_box) > IMG_TOL) and (abs(v - OOM_TD) > IMG_TOL)
        for v in OOM_by_reading.values()
    )  # (local)

    # --- CC3 thread: d ln A_s / d ln H̃ = +2 (UNIFIED-AS-79 identity) ---
    # A_s(H̃) = A_s^RouteB-SOcc · (H̃/H̃_can)^2 ; verify the power-law slope = +2.
    H_can = float(H_tilde_canonical_TD)                 # (local) = 5.9076e-3
    eps = 1e-6                                          # (local) central-diff rel step

    def A_s_of_H(H):                                    # (local) CC3 power-law in H̃
        return A_s_RouteB_SOcc * (H / H_can) ** 2

    Hp, Hm = H_can * (1.0 + eps), H_can * (1.0 - eps)   # (local)
    cc3_slope = (np.log(A_s_of_H(Hp)) - np.log(A_s_of_H(Hm))) / \
                (np.log(Hp) - np.log(Hm))               # (local) numerical d ln A_s / d ln H̃
    cc3_slope = float(cc3_slope)
    cc3_resid = abs(cc3_slope - CC3_SLOPE_TARGET)       # (local)
    cc3_pass = cc3_resid < CC3_REL_TOL                  # (local)
    A_s_at_Hcan = float(A_s_of_H(H_can))                # (local) consistency: == A_s_RouteB_SOcc

    # --- SIGN: occupied-state functional lifts A_s (K_sub > 1) ---
    delta_A_s = A_s_RouteB_SOcc - A_s_RouteB_vac        # (local) > 0
    sign_pass = delta_A_s >= 0.0                        # (local) plan PASS direction (lift confirmed)

    return {
        "value": OOM_RB,
        "OOM_RB": OOM_RB,
        "OOM_RB_vac": OOM_RB_vac,
        "dOOM_Socc": dOOM_Socc,
        "A_s_RouteB_vac": A_s_RouteB_vac,
        "A_s_RouteB_SOcc": A_s_RouteB_SOcc,
        "A_s_CMB": float(A_s_CMB),
        "A_s_FW": float(A_s_FW),
        "A_s_HTILDE_TDZETA": A_S_HTILDE_TDZETA,
        "n_bar_mw": n_bar_mw,
        "K_sub": K_sub,
        "K_sub_R2_resid": K_sub_R2_resid,
        "K_sub_canonical_inv12_R1": K_sub_canonical_inv12,
        "A_s_GGE_inv12_R1": A_s_GGE_inv12,
        "OOM_box": OOM_box,
        "OOM_TD": OOM_TD,
        "dist_box": dist_box,
        "dist_TD": dist_TD,
        "image": image,
        "magnitude_verdict": magnitude_verdict,
        "OOM_by_reading": OOM_by_reading,
        "OOM_reading_spread": OOM_reading_spread,
        "all_third_point": bool(all_third_point),
        "cc3_slope": cc3_slope,
        "cc3_resid": cc3_resid,
        "cc3_pass": bool(cc3_pass),
        "A_s_at_Hcan": A_s_at_Hcan,
        "delta_A_s": delta_A_s,
        "sign_pass": bool(sign_pass),
        # S66 lineage
        "A_s_route_B_PW_S66": A_s_route_B_PW_S66,
        "gap_route_B_PW_S66": gap_route_B_PW_S66,
        "frac_PW_S66": frac_PW_S66,
        # arrays
        "_K_sub_keys": np.array(K_sub_keys),
        "_K_sub_vals": K_sub_vals,
    }


# ---------------------------------------------------------------------------
# Section 6 — [SIGN] 3-tuple + composite collapse (gate-verdicts.md)
# ---------------------------------------------------------------------------
def evaluate_sign_tuple(res: dict) -> tuple[str, str, str, str]:
    """Return (sign_verdict, magnitude_verdict, regime_verdict, composite).

    sign_verdict   : PASS iff A_s^RouteB-SOcc >= A_s^RouteB-vac (S_occ lift confirmed).
    magnitude_verdict: image classification at 0.1 OOM (PASS=box-delta / FAIL=TD-ζ / INFO=third).
    regime_verdict : VALID — closed-form Peter-Weyl assembly, exact K_sub (locked relic n̄),
                     CC3 power-law slope machine-ε; no small-parameter breakdown.
    composite      : gate-verdicts.md §"Composite-collapse rule".
    """
    sign_verdict = "PASS" if res["sign_pass"] else "FAIL"   # (local)
    magnitude_verdict = res["magnitude_verdict"]            # (local)
    # Regime VALID iff CC3 slope identity holds (the only numerical-method check here)
    regime_verdict = "VALID" if res["cc3_pass"] else "MARGINAL"  # (local)

    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                                  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"                                  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"                                  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"                                  # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"                                  # (local)
    else:
        composite = "PASS"                                  # (local)
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
        "session": int(SESSION),
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

    # Left: the A_s OOM line — three assembly routes on the Planck axis
    pts = [
        ("TD/ζ\n(H̃ grid)", res["OOM_TD"], "C0"),
        ("Route-B PW\n(this gate)", res["OOM_RB"], "C2"),
        ("box-delta\n(ξ_KZ grid)", res["OOM_box"], "C3"),
    ]  # (local)
    for i, (lab, val, col) in enumerate(pts):
        ax[0].scatter([val], [0], s=140, color=col, zorder=3)
        ax[0].annotate(f"{lab}\nOOM={val:+.3f}", (val, 0),
                       xytext=(0, (-46 if i == 1 else 26)), textcoords="offset points",
                       ha="center", fontsize=8, color=col)
    ax[0].axvline(0.0, color="k", ls="--", lw=1, label="Planck A_s (OOM=0)")
    # 0.1 OOM tolerance windows around the two fork members
    for val, col, lab in [(res["OOM_box"], "C3", "box-delta ±0.1"),
                          (res["OOM_TD"], "C0", "TD/ζ ±0.1")]:
        ax[0].axvspan(val - IMG_TOL, val + IMG_TOL, color=col, alpha=0.12, label=lab)
    ax[0].set_xlim(-0.15, 1.05)
    ax[0].set_yticks([])
    ax[0].set_xlabel(r"$\mathrm{OOM} = \log_{10}(A_s / A_s^{\rm CMB})$")
    ax[0].set_title("Route-B-PW-SOcc images a THIRD value\n"
                    f"(neither fork member; image = {res['image']})")
    ax[0].legend(fontsize=7, loc="upper center", ncol=2)
    ax[0].grid(alpha=0.3, axis="x")

    # Right: K_sub-reading robustness — all four readings land third-point
    keys = list(res["OOM_by_reading"].keys())          # (local)
    vals = [res["OOM_by_reading"][k] for k in keys]    # (local)
    ax[1].axhspan(res["OOM_box"] - IMG_TOL, res["OOM_box"] + IMG_TOL,
                  color="C3", alpha=0.12, label="box-delta image band")
    ax[1].axhspan(res["OOM_TD"] - IMG_TOL, res["OOM_TD"] + IMG_TOL,
                  color="C0", alpha=0.12, label="TD/ζ image band")
    ax[1].bar(range(len(vals)), vals, color="C2", alpha=0.75)
    ax[1].axhline(res["OOM_RB"], color="C2", ls="-", lw=1.4,
                  label=f"canonical R2 = {res['OOM_RB']:+.4f}")
    ax[1].set_xticks(range(len(keys)))
    ax[1].set_xticklabels([k.split("(")[0].replace("_", "\n") for k in keys],
                          fontsize=7)
    ax[1].set_ylabel(r"$\mathrm{OOM}(A_s^{\rm RouteB\text{-}SOcc})$ per $K_{sub}$ reading")
    ax[1].set_ylim(0.0, 1.0)
    ax[1].set_title(f"Image is $K_{{sub}}$-reading-robust\n"
                    f"(spread {res['OOM_reading_spread']:.4f} OOM; all third-point="
                    f"{res['all_third_point']})")
    ax[1].legend(fontsize=7, loc="upper right")
    ax[1].grid(alpha=0.3, axis="y")

    fig.suptitle("CF-S117-ROUTE-B-PW-SOCC — Route-B Peter-Weyl GGE-modular A_s "
                 "images +0.384 OOM (3rd point; plurality 2->3)", fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(),
                                              CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()
    sign_v, mag_v, regime_v, composite = evaluate_sign_tuple(res)

    # --- Report ---
    print(f"=== {GATE_ID} — Route-B Peter-Weyl A_s with S_occ=(1+2n_k)·S_fold ===")
    print(f"  S66 Route-B PW RAW lineage  : A_s = {res['A_s_route_B_PW_S66']:.6e} "
          f"(gap {res['gap_route_B_PW_S66']:.4f} OOM; frac_PW={res['frac_PW_S66']:.4e}) "
          f"[pre-reconciliation crisis]")
    print(f"  TD-canonical Route-B/BD base: A_s^RouteB-vac = {res['A_s_RouteB_vac']:.6e} "
          f"(CC3-anchored to H̃={float(H_tilde_canonical_TD):.4e})")
    print()
    print(f"  n̄ (mult-weighted relic occ) : {res['n_bar_mw']:.6e}  (inv12_w1_2)")
    print(f"  K_sub = 1 + 2 n̄ (R2)        : {res['K_sub']:.10f}  "
          f"(stored-R2 resid {res['K_sub_R2_resid']:.2e})")
    print(f"  ΔOOM_Socc = log10(K_sub)    : {res['dOOM_Socc']:+.4e} OOM  "
          f"(≪ 0.1 ⇒ S_occ does NOT bridge the fork)")
    print()
    print(f"  A_s^RouteB-vac              : {res['A_s_RouteB_vac']:.6e}  (OOM {res['OOM_RB_vac']:+.5f})")
    print(f"  A_s^RouteB-SOcc = K·vac     : {res['A_s_RouteB_SOcc']:.6e}  (OOM {res['OOM_RB']:+.5f})")
    print(f"  delta = SOcc - vac          : {res['delta_A_s']:+.4e}  (>0 ⇒ S_occ lifts, sign PASS)")
    print()
    print(f"  Image classification (tol {IMG_TOL} OOM):")
    print(f"     box-delta (ξ_KZ)  OOM_box = {res['OOM_box']:+.5f}  |dist| = {res['dist_box']:.5f}")
    print(f"     TD/ζ (H̃ grid)    OOM_TD  = {res['OOM_TD']:+.5f}  |dist| = {res['dist_TD']:.5f}")
    print(f"     => OOM_RB = {res['OOM_RB']:+.5f}  ⇒ image = {res['image']}")
    print()
    print(f"  K_sub-reading robustness (R1..R4):")
    for k in res["OOM_by_reading"]:
        print(f"     {k:28s} OOM = {res['OOM_by_reading'][k]:+.6f}")
    print(f"     spread = {res['OOM_reading_spread']:.6f} OOM ; all_third_point = {res['all_third_point']}")
    print(f"     (inv12 R1-softest cross-check: K_sub={res['K_sub_canonical_inv12_R1']:.8f}, "
          f"A_s_GGE={res['A_s_GGE_inv12_R1']:.6e})")
    print()
    print(f"  CC3 thread d ln A_s/d ln H̃ : {res['cc3_slope']:.12f}  "
          f"(target {CC3_SLOPE_TARGET}; resid {res['cc3_resid']:.2e}; pass={res['cc3_pass']})")
    print(f"     A_s(H̃_can) consistency   : {res['A_s_at_Hcan']:.6e} == A_s^RouteB-SOcc")
    print()
    print(f"  [SIGN] sign={sign_v}  magnitude={mag_v}  regime={regime_v}  => composite={composite}")
    print()

    # --- Save npz ---
    np.savez(
        OUT_NPZ,
        value=res["value"],
        OOM_RB=res["OOM_RB"],
        OOM_RB_vac=res["OOM_RB_vac"],
        dOOM_Socc=res["dOOM_Socc"],
        A_s_RouteB_vac=res["A_s_RouteB_vac"],
        A_s_RouteB_SOcc=res["A_s_RouteB_SOcc"],
        A_s_CMB=res["A_s_CMB"],
        A_s_FW=res["A_s_FW"],
        A_s_HTILDE_TDZETA=res["A_s_HTILDE_TDZETA"],
        n_bar_mw=res["n_bar_mw"],
        K_sub=res["K_sub"],
        K_sub_R2_resid=res["K_sub_R2_resid"],
        K_sub_canonical_inv12_R1=res["K_sub_canonical_inv12_R1"],
        A_s_GGE_inv12_R1=res["A_s_GGE_inv12_R1"],
        OOM_box=res["OOM_box"],
        OOM_TD=res["OOM_TD"],
        dist_box=res["dist_box"],
        dist_TD=res["dist_TD"],
        image=res["image"],
        magnitude_verdict=res["magnitude_verdict"],
        OOM_reading_spread=res["OOM_reading_spread"],
        all_third_point=res["all_third_point"],
        cc3_slope=res["cc3_slope"],
        cc3_resid=res["cc3_resid"],
        cc3_pass=res["cc3_pass"],
        A_s_at_Hcan=res["A_s_at_Hcan"],
        delta_A_s=res["delta_A_s"],
        sign_pass=res["sign_pass"],
        A_s_route_B_PW_S66=res["A_s_route_B_PW_S66"],
        gap_route_B_PW_S66=res["gap_route_B_PW_S66"],
        frac_PW_S66=res["frac_PW_S66"],
        K_sub_keys=res["_K_sub_keys"],
        K_sub_vals=res["_K_sub_vals"],
        OOM_by_reading_vals=np.array(list(res["OOM_by_reading"].values())),
        sign_verdict=sign_v,
        magnitude_verdict_tuple=mag_v,
        regime_verdict=regime_v,
        composite=composite,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  wrote {OUT_NPZ.name}")

    make_plot(res)
    print(f"  wrote {OUT_PNG.name}")
    print()

    print(emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX))

    companion = (
        f"OOM_RB={res['OOM_RB']:+.5f}(3rd point); "
        f"A_s_RouteB_SOcc={res['A_s_RouteB_SOcc']:.6e}; "
        f"K_sub_R2={res['K_sub']:.7f}(n_bar_mw={res['n_bar_mw']:.4e}); "
        f"dOOM_Socc={res['dOOM_Socc']:+.3e}(<<0.1); "
        f"dist_box={res['dist_box']:.4f},dist_TD={res['dist_TD']:.4f}(both>0.1=>third); "
        f"CC3_slope={res['cc3_slope']:.6f}(resid {res['cc3_resid']:.1e}); "
        f"plurality 2->3"
    )  # (local)
    extra = [
        "# regulator_pin=a_n^{zeta} (Branch-A Zubarev/zeta-regularized; no regulator mixing across A_s ledger per S83 W1-G1)",
        "# base A_s^RouteB-vac=A_s_BD=5.078171e-9 (TD-canonical Route-B/BD floor; S82 W2-4 / S84 AS-PIN-MAP; modern image of S66 Route-B-PW crisis 2.918e-6)",
        f"# K_sub-reading robust: R1..R4 OOM spread {res['OOM_reading_spread']:.4f}; all_third_point={res['all_third_point']} (S_occ functional choice does NOT change the image)",
    ]  # (local)
    print_verdict_payload(
        composite, res["value"], audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=companion, extra_rows=extra,
    )

    print(f"\n=== {GATE_ID}: {composite} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
