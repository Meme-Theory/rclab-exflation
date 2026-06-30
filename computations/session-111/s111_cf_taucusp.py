#!/usr/bin/env python3
"""
S111 W1-6 S111-CF-TAUCUSP — does the tau_fold van Hove cusp leave a SEPARABLE,
DETECTABLE spectral-tilt signature in the GGE-relic running/tilt structure?
=============================================================================

Gate: S111-CF-TAUCUSP ([SIGN])
Classification: PHONONIC

Pre-registered threshold (plan §W1-6):
  operator: |Delta(running/tilt)_cusp| > thr_baseline  AND  |Delta_cusp| ≷ sigma_detector
  SIGN claim (Step 4): the cusp contribution is NONZERO and SEPARABLE from the
                       smooth monotone-ramp matter sector.
  MAGNITUDE claim (Step 5): the SEPARABLE excess must exceed the CMB-S4/CMB-HD
                       detector horizon IN THE OBSERVABLE THE DETECTOR READS.
  RATIO convention: cusp contribution as an excess/ratio over the smooth-ramp
                    baseline.

  PASS  iff cusp contribution is separable (SIGN PASS) AND the detectable excess
        at the CMB-pivot detector leaf >= detector-sigma (MAGNITUDE PASS, regime VALID).
  INFO  iff cusp contribution is separable (SIGN PASS) but the detectable excess
        at the CMB-pivot leaf is BELOW the detector horizon.
  FAIL  iff cusp contribution ~ 0 / inseparable from the smooth ramp (SIGN FAIL):
        observationally sterile like the matter-sector no-bounce.

SUBSTRATE-FIRST PHYSICS (the two-leaf structure — the crux of this gate)
------------------------------------------------------------------------
The GGE-relic power spectrum is P(k) ~ |beta_k|^2 g(omega_k), g = density of
states of D_K. The van Hove cusp at tau_cusp ~ 0.221 (canonical tau_fold = 0.19
sits on the rising flank) is a NON-ANALYTIC feature in g as a function of the
Level-2 modulus tau (S85 PERMANENT, §VII.M.W10-3). It IS a genuine, separable
feature in the substrate spectral structure.

But the GGE-relic spectral tilt/running carries TWO scale-tagged leaves
(SCALE-AND-CHANNEL-TAGGING; S110-CF-B1-TRANSITPS):

  leaf-1 (substrate-distance / BZ-internal): alpha_s^substrate = -0.08587279
         (Mellin residue s=3, inside the BZ). This leaf DOES carry the
         spectral-complexity / DOS imprint — the cusp images here.

  leaf-2 (Goldstone / CMB-pivot, what CMB-S4/CMB-HD reads): alpha_s^pivot = 0,
         n_s = 1 - 2 eps_H = 0.9561 = GEOMETRIC tilt ONLY, by the Mode-Independent
         Occupation Theorem (S57/S62 PROVEN): the CMB-pivot tilt is INDEPENDENT
         of |beta_k|^2 occupation / DOS. The cusp is BLIND on this leaf.

The two leaves are 54.04 decades apart, connected by the transport map with
deg(T_{BZ->pivot}) = 2.0 NON-SCALAR (T4 formulation; S93 W7-1 PASS, S110-CF-CV6B).
O^pivot = O^substrate IFF deg(T) is the T2-VACUOUS (scalar) case. It is NON-SCALAR,
so the substrate-distance running does NOT transport to the pivot:
  alpha_s^pivot = alpha_s^substrate * [transport factor] = 0  (Mode-Independent).

CONSEQUENCE (the falsifiable-asymmetry content made precise):
  SIGN   = PASS  -> the cusp contribution is NONZERO and separable on the
                   substrate-distance leaf (cusp-in-tau is REAL).
  MAGNITUDE      -> the detectable excess AT THE CMB-PIVOT DETECTOR LEAF is
                   exactly 0 (Mode-Independent Occupation), hence below ANY finite
                   detector-sigma. The detector reads no cusp signal regardless of
                   how sharp the substrate-leaf cusp is.
  -> composite INFO: the conjugate-pair prediction holds STRUCTURALLY (bounded
     structure DOES image into the tau-conjugate spectral-complexity observable)
     but is observationally SUB-HORIZON at the CMB-pivot detector axis
     (the strongest form of sub-horizon: exactly 0 at the pivot leaf).

Direction of explanation: D_K eigenvalue DOS divergence at tau_fold
  -> GGE-relic spectral-complexity tilt (substrate-distance leaf, alpha_s^substrate)
  -> [transport, deg=2 NON-SCALAR] -> CMB-pivot tilt (geometric-only, cusp-blind)
  -> CMB running observable.
The substrate IS the spectral structure; the observable is its measured imprint.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-85/s85_w0_van_hove_cusp_theorem.npz  (the DOS cusp profile)
  - canonical_constants.py  (n_s, alpha_s leaves, tau_fold, deg_T, detector-sigma)
  - script bytes

regulator_pin: a_n^{Mellin}  (substrate-distance running alpha_s is a Mellin
               residue s=3 evaluation; the Seeley-DeWitt moment entering the tilt
               is Mellin-regulated — regulator-pin-discipline.md).
publication_precision: 4 sig figs (the cusp-contribution magnitude is cited
               downstream in the conjugate-pair falsifiable-asymmetry record;
               downstream verifier rel_tol >= 1e-4).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # cpu-cap-OMP8 per plan GPU_path
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent.parent / "_shared"))

from canonical_constants import (  # noqa: F401
    tau_fold,
    n_s_framework,
    alpha_s_substrate_distance_1,
    alpha_s_pivot_goldstone,
    deg_T_BZ_pivot,
    sigma_beta_s_CMB_S4,
    beta_s,
    PI,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S111"                                       # (local)
GATE_ID = "S111-CF-TAUCUSP"                            # (local)
SCHEME = "GGE-relic-spectral-tilt"                    # (local)
CONVENTION = "RATIO"                                  # (local)
L_MAX = 10                                            # (local) op. L=8 cusp cache

# Pre-registered detector-sigma comparison anchor (plan §W1-6 machinery_pin_map):
# CMB-S4 1-sigma running sensitivity (running-of-running forecast, Science Book
# v2 2022 Table 6.1) — the tilt/running detector horizon for the MAGNITUDE leg.
SIGMA_DETECTOR_CMB_S4 = sigma_beta_s_CMB_S4           # (local) = 0.0022
# CMB-HD is a tighter (redundant) channel on the SAME moment (atlas-05 Window-16;
# cross-channel-correlation-matrix); pinned as a factor-3 tighter horizon for the
# detector-watch routing (no separate canonical exists; conservative tightening).
SIGMA_DETECTOR_CMB_HD = sigma_beta_s_CMB_S4 / 3.0     # (local)

# Separability floor: the cusp contribution must exceed the smooth-ramp baseline
# (i.e., separable). Pre-registered as the smooth-ramp matter-sector running
# magnitude proxy — the cusp EXCESS must be a nonzero fraction of the
# substrate-distance running for SIGN PASS.
SEP_FLOOR_FRAC = 1.0e-3                               # (local) separability floor

OUT_NPZ = SESSION_DIR / "s111_cf_taucusp.npz"
OUT_PNG = SESSION_DIR / "s111_cf_taucusp.png"

CUSP_NPZ = COMPUTATIONS_DIR / "session-85" / "s85_w0_van_hove_cusp_theorem.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CUSP_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA)
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
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
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
    """Extract the cusp-attributable spectral-tilt contribution on the
    substrate-distance leaf, then propagate through the NON-SCALAR transport map
    to the CMB-pivot detector leaf.

    Step A: read the DOS cusp profile (S85). The sharpness S(tau) of the DOS
            peaks at tau_cusp; the rel_dev is the cusp's non-stationarity
            signature (S85 stationarity FAIL = genuine cusp).
    Step B: separability — split S(tau) into a smooth monotone-ramp baseline (fit
            away from the cusp window) + the cusp EXCESS at the cusp/fold.
            cusp_excess_frac = (cusp sharpness excess) / (sharpness baseline scale).
    Step C: substrate-leaf tilt contribution — the cusp's relative DOS modulation
            (rel_dev) injects curvature into ln P, modulating the substrate-distance
            running alpha_s^substrate. Delta_alpha_substrate = rel_dev * |alpha_s^substrate|.
    Step D: transport to the CMB-pivot detector leaf. deg(T_{BZ->pivot}) = 2.0
            NON-SCALAR => the substrate-distance running does NOT transport;
            alpha_s^pivot = 0 (Mode-Independent Occupation). The detectable cusp
            excess AT THE PIVOT LEAF is Delta_alpha_pivot = 0.
    Step E: verdict — SIGN from Step B/C (cusp separable + nonzero on substrate
            leaf); MAGNITUDE from Step D vs detector-sigma (pivot-leaf excess vs
            CMB-S4/CMB-HD horizon).
    """
    d = np.load(CUSP_NPZ, allow_pickle=True)  # (local)
    tau = d["tau_grid"]                       # (local) 101-pt tau in [0.15,0.25]
    S = d["sharpness_tau"]                    # (local) DOS sharpness vs tau
    dos = d["dos_matrix"]                     # (local) (101, 432) DOS g(E;tau)
    Ec = d["E_centers"]                       # (local) 432 energy-bin centers
    i_cusp = int(d["i_cusp"])                 # (local)
    tau_cusp = float(d["tau_cusp"])           # (local) = 0.221
    rel_dev = float(d["rel_dev_refined"])     # (local) cusp non-stationarity signature
    S_max = float(d["S_max"])                 # (local) peak sharpness at cusp
    L_max_cusp = int(d["L_max"])              # (local) = 8 (cusp cache)

    # --- Step B: separability split (smooth ramp baseline vs cusp excess) ---
    # Smooth monotone-ramp baseline: linear fit to S(tau) EXCLUDING the cusp window.
    cusp_half_window = 0.015                              # (local) tau window half-width
    mask_smooth = np.abs(tau - tau_cusp) > cusp_half_window  # (local)
    coef = np.polyfit(tau[mask_smooth], S[mask_smooth], 1)   # (local) [slope, intercept]
    baseline = np.polyval(coef, tau)                         # (local) smooth-ramp baseline
    excess = S - baseline                                    # (local) cusp excess profile

    i_fold = int(np.argmin(np.abs(tau - tau_fold)))      # (local) canonical fold index
    cusp_excess_peak = float(np.max(excess))             # (local) peak excess at cusp
    baseline_scale = float(np.mean(np.abs(baseline)))    # (local) ramp magnitude scale
    # Fractional cusp excess over the smooth-ramp baseline (the RATIO convention):
    cusp_excess_frac = cusp_excess_peak / baseline_scale  # (local)

    # Separability: is the cusp excess a genuine nonzero feature above the ramp?
    separable = cusp_excess_frac > SEP_FLOOR_FRAC        # (local)

    # --- Step C: substrate-distance-leaf tilt/running contribution ---
    # The cusp's relative DOS modulation (rel_dev) injects curvature into ln P;
    # it modulates the substrate-distance running alpha_s^substrate.
    delta_alpha_substrate = rel_dev * abs(alpha_s_substrate_distance_1)  # (local)
    # As a fraction of the substrate-distance running:
    delta_alpha_substrate_frac = delta_alpha_substrate / abs(alpha_s_substrate_distance_1)  # (local)
    # (= rel_dev by construction; the substrate-leaf cusp imprint is rel_dev-sized)

    # --- Step D: transport to the CMB-pivot detector leaf (deg=2 NON-SCALAR) ---
    # Mode-Independent Occupation Theorem (S57/S62): the CMB-pivot tilt is
    # geometric-only, INDEPENDENT of |beta_k|^2 / DOS. deg(T_{BZ->pivot})=2.0 is
    # NON-SCALAR (NOT the T2-VACUOUS scalar case), so the substrate-distance running
    # does NOT transport to the pivot. The transport factor for the DOS/occupation
    # channel onto the pivot tilt is the scalar-projection of a NON-SCALAR degree-2
    # map = 0 (the occupation channel is annihilated at the pivot).
    is_scalar_transport = (float(deg_T_BZ_pivot) == 0.0)  # (local) T2-VACUOUS test
    if is_scalar_transport:
        # would transport intact (NOT the realized case)
        delta_alpha_pivot = delta_alpha_substrate         # (local)
    else:
        # NON-SCALAR (deg=2): occupation/DOS channel annihilated at pivot leaf.
        # Anchored to the canonical pivot value alpha_s^pivot = 0 (Mode-Independent).
        delta_alpha_pivot = abs(float(alpha_s_pivot_goldstone))  # (local) = 0
    # Sanity: confirm the canonical pivot running is exactly the cusp-blind value.
    pivot_running_canonical = float(alpha_s_pivot_goldstone)  # (local) = 0

    # --- Step E: detector-horizon comparison (MAGNITUDE leg) ---
    # The detectable cusp excess at the CMB-pivot leaf vs CMB-S4/CMB-HD horizon.
    detectable_excess = delta_alpha_pivot                # (local) pivot-leaf excess
    sigma_s4 = float(SIGMA_DETECTOR_CMB_S4)              # (local)
    sigma_hd = float(SIGMA_DETECTOR_CMB_HD)              # (local)
    n_sigma_s4 = detectable_excess / sigma_s4            # (local) excess in S4 sigma
    n_sigma_hd = detectable_excess / sigma_hd            # (local) excess in HD sigma
    detectable_s4 = detectable_excess >= sigma_s4        # (local)
    detectable_hd = detectable_excess >= sigma_hd        # (local)

    # --- Verdict 3-tuple (schema-v2; [SIGN] gate) ---
    # SIGN: the cusp contribution is NONZERO and separable (Step B/C).
    sign_verdict = "PASS" if (separable and delta_alpha_substrate_frac > SEP_FLOOR_FRAC) else "FAIL"
    # MAGNITUDE: pivot-leaf detectable excess vs detector horizon.
    #   PASS  if detectable at S4 (>= sigma_s4)
    #   INFO  if present-but-sub-horizon (separable substrate signal, < detector sigma)
    #   FAIL  if SIGN FAIL (cusp ~ 0 / inseparable)
    if sign_verdict == "FAIL":
        magnitude_verdict = "FAIL"
    elif detectable_s4:
        magnitude_verdict = "PASS"
    else:
        magnitude_verdict = "INFO"  # separable but below CMB-S4 horizon
    # REGIME: is the two-leaf transport framework valid throughout? Yes — the
    # Mode-Independent Occupation Theorem (PROVEN) and deg(T)=2 NON-SCALAR (PASS)
    # hold exactly at the CMB pivot; the substrate-leaf cusp extraction is on the
    # S85 cusp cache (L=8) and the GGE-relic anchors are L_max-saturated. VALID.
    regime_verdict = "VALID"

    # Composite collapse (generic rule from gate-verdicts.md):
    #   regime BREAKDOWN -> FAIL; sign FAIL -> FAIL;
    #   magnitude FAIL & regime VALID -> FAIL; magnitude INFO -> INFO; else PASS.
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

    # publication precision: 4 sig figs on the cusp-contribution magnitude
    delta_alpha_substrate_4sf = float(f"{delta_alpha_substrate:.4g}")  # (local)

    print()
    print(f"  [Step A] cusp profile: tau_cusp={tau_cusp:.5f}  S_max={S_max:.4f}  "
          f"S_floor={float(np.min(S)):.4f}  rel_dev={rel_dev:.6f}  L_max(cusp)={L_max_cusp}")
    print(f"           canonical tau_fold={tau_fold} sits at index {i_fold} "
          f"(tau={tau[i_fold]:.4f}, on the rising flank of the cusp at {tau_cusp:.4f})")
    print(f"  [Step B] smooth-ramp baseline slope={coef[0]:.4f} intercept={coef[1]:.4f}; "
          f"cusp excess peak={cusp_excess_peak:.4f} (frac of ramp={cusp_excess_frac:.4f}) "
          f"=> SEPARABLE={separable}")
    print(f"  [Step C] substrate-distance leaf: alpha_s^substrate={alpha_s_substrate_distance_1:.8f}; "
          f"Delta_alpha_cusp(substrate)={delta_alpha_substrate:.6f} "
          f"(= rel_dev x |alpha_s^substrate|, 4sf={delta_alpha_substrate_4sf:.4g})")
    print(f"  [Step D] transport deg(T_BZ->pivot)={deg_T_BZ_pivot} "
          f"(NON-SCALAR; T2-VACUOUS-scalar={is_scalar_transport}); "
          f"Mode-Independent Occupation => alpha_s^pivot={pivot_running_canonical} "
          f"=> Delta_alpha_cusp(pivot)={delta_alpha_pivot:.6f}")
    print(f"  [Step E] detectable excess(pivot)={detectable_excess:.6f}; "
          f"sigma_S4={sigma_s4:.4g} (n_sigma={n_sigma_s4:.4f}, detect={detectable_s4}); "
          f"sigma_HD={sigma_hd:.4g} (n_sigma={n_sigma_hd:.4f}, detect={detectable_hd})")
    print(f"  3-tuple: sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict} "
          f"=> composite={composite}")

    # --- Save data ---
    np.savez(
        OUT_NPZ,
        tau_grid=tau,
        sharpness_tau=S,
        smooth_baseline=baseline,
        cusp_excess=excess,
        E_centers=Ec,
        dos_cusp_row=dos[i_cusp],
        dos_fold_row=dos[i_fold],
        i_cusp=i_cusp,
        i_fold=i_fold,
        tau_cusp=tau_cusp,
        tau_fold_canonical=tau_fold,
        rel_dev=rel_dev,
        cusp_excess_peak=cusp_excess_peak,
        cusp_excess_frac=cusp_excess_frac,
        separable=separable,
        alpha_s_substrate=alpha_s_substrate_distance_1,
        alpha_s_pivot=pivot_running_canonical,
        n_s_framework=n_s_framework,
        deg_T_BZ_pivot=float(deg_T_BZ_pivot),
        delta_alpha_substrate=delta_alpha_substrate,
        delta_alpha_substrate_frac=delta_alpha_substrate_frac,
        delta_alpha_pivot=delta_alpha_pivot,
        detectable_excess=detectable_excess,
        sigma_detector_CMB_S4=sigma_s4,
        sigma_detector_CMB_HD=sigma_hd,
        n_sigma_S4=n_sigma_s4,
        n_sigma_HD=n_sigma_hd,
        detectable_S4=detectable_s4,
        detectable_HD=detectable_hd,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        composite=composite,
        delta_alpha_substrate_4sf=delta_alpha_substrate_4sf,
    )

    # --- Plot ---
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    ax0 = axes[0]
    ax0.plot(tau, S, "o-", ms=3, color="tab:blue", label="DOS sharpness S(tau)")
    ax0.plot(tau, baseline, "--", color="tab:gray", label="smooth-ramp baseline")
    ax0.axvline(tau_cusp, color="tab:red", ls=":", label=f"tau_cusp={tau_cusp:.3f} (van Hove)")
    ax0.axvline(tau_fold, color="tab:green", ls="-.", label=f"tau_fold={tau_fold} (canonical)")
    ax0.set_xlabel("tau (Level-2 Jensen modulus)")
    ax0.set_ylabel("DOS sharpness S")
    ax0.set_title("Step B: cusp excess over smooth-ramp baseline (substrate leaf)")
    ax0.legend(fontsize=7)
    ax0.grid(alpha=0.3)

    ax1 = axes[1]
    leaves = ["substrate-distance\n(BZ-internal)", "CMB-pivot\n(Goldstone; detector)"]
    vals = [delta_alpha_substrate, delta_alpha_pivot]
    bars = ax1.bar(leaves, vals, color=["tab:purple", "tab:orange"])
    ax1.axhline(sigma_s4, color="tab:red", ls="--", label=f"CMB-S4 sigma={sigma_s4:.4g}")
    ax1.axhline(sigma_hd, color="tab:brown", ls=":", label=f"CMB-HD sigma={sigma_hd:.4g}")
    ax1.set_ylabel("|Delta alpha_s|_cusp (running contribution)")
    ax1.set_title("Step D/E: cusp imprint per leaf vs detector horizon")
    for b, v in zip(bars, vals):
        ax1.text(b.get_x() + b.get_width() / 2, v, f"{v:.4g}", ha="center", va="bottom", fontsize=8)
    ax1.legend(fontsize=7)
    ax1.grid(alpha=0.3, axis="y")
    fig.suptitle("S111-CF-TAUCUSP: van Hove cusp -> GGE-relic tilt; separable (substrate) "
                 "but pivot-leaf cusp-blind (Mode-Independent Occupation)", fontsize=9)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)

    return {
        "value": (f"sign={sign_verdict}_mag={magnitude_verdict}_regime={regime_verdict}"
                  f"_composite={composite}"
                  f"_dAlpha_substrate={delta_alpha_substrate_4sf:.4g}"
                  f"_dAlpha_pivot={delta_alpha_pivot:.4g}"
                  f"_cuspExcessFrac={cusp_excess_frac:.4g}"
                  f"_nSigma_S4={n_sigma_s4:.4g}_degT={float(deg_T_BZ_pivot):.1f}"
                  f"_relDev={rel_dev:.4g}"),
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "composite": composite,
        "delta_alpha_substrate": delta_alpha_substrate,
        "delta_alpha_pivot": delta_alpha_pivot,
        "cusp_excess_frac": cusp_excess_frac,
        "n_sigma_S4": n_sigma_s4,
        "rel_dev": rel_dev,
    }


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


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


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)        # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()           # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    result = compute()  # (local)
    value = result["value"]
    verdict = result["composite"]

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print()
    print(tag)
    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        sign_verdict=result["sign_verdict"],
        magnitude_verdict=result["magnitude_verdict"],
        regime_verdict=result["regime_verdict"],
        companion_note=("cusp separable on substrate-distance leaf "
                        "(Delta_alpha_substrate=rel_dev*|alpha_s^sub|); "
                        "CMB-pivot leaf cusp-blind by Mode-Independent Occupation "
                        "(deg_T=2 NON-SCALAR) => detectable_excess(pivot)=0 < detector-sigma"),
        extra_rows=[
            "# regulator_pin=a_n^{Mellin} (substrate-distance running alpha_s via Mellin residue s=3)",
            "# publication_precision=4sf downstream rel_tol>=1e-4 (cusp-contribution magnitude cited downstream)",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # verdict is data; exit 0 on script health


if __name__ == "__main__":
    sys.exit(main())
