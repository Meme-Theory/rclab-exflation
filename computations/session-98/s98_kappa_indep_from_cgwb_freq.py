#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S98-KAPPA-INDEP-FROM-CGWB-FREQ  (agent: mack-cosmic-bridge)
===========================================================
Test whether the CGWB peak FREQUENCY axis (f_obs proportional to kappa-scaling)
supplies a SECOND, dimensionally-independent seconds-scale that would upgrade
kappa from "consistency-pinned" (the S97-COOLING-BUDGET-KAPPA-PIN status) to
"independently-pinned."

THE QUESTION (plan session-98-plan-w4.md §W4-2):
  kappa is the M_KK^-1 -> SI-seconds normalization knob. The S97 cooling-budget
  gate established kappa is CONSISTENCY-pinned (= kappa_nat = hbar/(M_KK*GeV_to_J))
  but the recovery there is an IDENTITY forced by M_KK-unit consistency, NOT an
  independent triangulation. An INDEPENDENT seconds-scale would require a SECOND,
  dimensionally-distinct observable that depends on kappa and is MEASURABLE.
  The CGWB peak frequency f_obs proportional to kappa is exactly such a candidate
  axis: if a real GW detector could measure f_obs in its band, that measured
  frequency -> a measured seconds-scale independent of the cooling-budget pin,
  triangulating kappa.

  This gate tests the candidate: does f_obs(kappa_nat) = 8.4835e+39 Hz land in
  ANY existing/proposed GW detector horizon band? Set-membership across the union
  of {PTA, LISA, LIGO/ET, optimistic resonant-HF ceiling}.

  INFO/FAIL gate (plan §V.7: NO PASS branch):
    INFO iff f_obs IN any detector band -> kappa would be INDEPENDENTLY-pinnable.
    FAIL iff f_obs OUTSIDE ALL horizons -> kappa stays CONSISTENCY-PINNED.

SUBSTRATE FRAMING (phononic-framing.md):
  The CGWB peak IS a substrate observable -- the ACOUSTIC signature of the GGE
  relic's post-fold spectral reorganization. Its frequency flows FROM the fold
  van-Hove DOS (M_KK/(2pi) emission) through the redshift chain (a_fold/a_now),
  NOT a thermal-equilibrium CMB-style spectrum IN an expanding container. The
  arrow is:
      D_K spectrum -> fold van-Hove acoustic emission M_KK/(2pi)
                   -> redshift a_fold/a_now -> f_obs ~ 10^40 Hz.
  kappa enters f_obs MULTIPLICATIVELY (f_obs proportional to kappa), which is
  precisely WHY an in-band frequency WOULD pin kappa. But the substrate puts the
  peak ~10^40 Hz, far above every horizon (>=28.9 decades above the optimistic
  resonant-HF ceiling, 42.5 decades above the LISA pivot). A laboratory detector
  probes the deeply IR-tail mHz-GHz channels; the detector=tail separation is set
  by the kappa-scaling transport factor. So no independent kappa-pin exists from
  this axis; kappa stays consistency-pinned because the only frequency axis that
  depends on it lies beyond all detectors.
  NON-PHONONIC caveat: the gate's OBJECT is the kappa-determinacy (epistemic
  status of an emergent transport knob) + detector-reach arithmetic -- a
  methodology/observational-falsifier question, not a substrate excitation.

  CROSS-LINK (project_s96_w3_cgwb_flagship_retirement): the GW-detector CGWB
  flagship has been RETIRED (GW -> LSS migration); the live acoustic falsifier is
  the first-sound BAO ring, NOT a GW-detector signal. This gate makes the
  detector-sterility of the CGWB FREQUENCY axis (for kappa-triangulation) explicit
  and final.

Verdict rubric (per plan §W4-2 / gate-verdicts.md schema-v2 3-tuple collapse):
  This is a [SIGN] INFO/FAIL gate (no PASS token).
  sign_verdict     = PASS iff the predicted direction holds: log10(f_obs) >
                     log10(hi_max) for the highest band (f_obs strictly ABOVE the
                     top horizon edge), matching the substitution-chain prediction.
                     FAIL on direction mismatch.
  magnitude_verdict= INFO iff f_obs is a MEMBER of any band (would license
                     independently-pinned); FAIL iff f_obs is OUTSIDE all bands
                     (the predicted detector-sterile outcome). [NOTE the inversion
                     from a recovery gate: here "in-band" is the surprising INFO
                     outcome and "out-of-band" is the predicted FAIL.]
  regime_verdict   = VALID iff the frequency-vs-band arithmetic is well-defined
                     (f_obs finite, cross-check vs S97 npz matches, all band edges
                     positive-ordered).

Composite collapse (gate-verdicts.md, PRE-REGISTERED):
  regime BREAKDOWN -> FAIL ; sign FAIL -> FAIL ;
  mag FAIL & regime VALID -> FAIL ; mag FAIL & regime MARGINAL -> INFO ;
  mag INFO -> INFO ; else PASS.
  This gate has no PASS branch (mag is only INFO|FAIL), so composite collapses to
  FAIL (predicted: out-of-band) or INFO (surprise: in-band).

Inputs:
  computations/_shared/canonical_constants.py
      (f_obs_CGWB_peak_kappa_nat=8.4835e+39, M_KK_inv_seconds=8.860439881925477e-42,
       Omega_GW_acoustic_peak, GeV_to_J, M_KK, hbar_SI)
  computations/session-97/s97_omegagw_peak_height.npz
      (cross-check: f_peak_Hz=8.4835e+39, f_LISA_Hz=0.003, kappa_grid(121),
       kappa_nat=8.860439881925477e-42, kappa_robust=True; amplitude robust under
       kappa, frequency kappa-DEPENDENT -- the axis this gate tests)

Outputs:
  computations/session-98/s98_kappa_indep_from_cgwb_freq.npz
  computations/session-98/s98_kappa_indep_from_cgwb_freq.png
  verdict line + dual-SHA companion row + schema-v2 3-tuple row appended to
  computations/session-98/s98_gate_verdicts.txt
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")     # scalar set-membership arithmetic; CPU thread cap (no matrices, no GPU)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- locate project root and canonical_constants ---
THIS = Path(__file__).resolve()
PROJECT_ROOT = THIS.parents[2]                                  # .../Ainulindale Exflation
SHARED = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED))

from canonical_constants import (                                # noqa: E402
    f_obs_CGWB_peak_kappa_nat,   # Hz; CGWB peak freq at substrate-natural kappa=hbar/M_KK (8.4835e+39)
    M_KK_inv_seconds,            # s; kappa_nat = hbar_SI/(M_KK*GeV_to_J) (8.860439881925477e-42)
    M_KK,                        # GeV; substrate compactification scale
    hbar_SI,                     # J*s
    GeV_to_J,                    # J/GeV
)

# ---------------------------------------------------------------------------
# Gate identity + machinery pins (PRDR; per plan §W4-2 machinery_pin_map)
# ---------------------------------------------------------------------------
GATE_ID    = "S98-KAPPA-INDEP-FROM-CGWB-FREQ"
SCHEME     = "FW"
CONVENTION = "ABSOLUTE"            # absolute frequencies in Hz
L_MAX      = "N/A"                 # no spectrum computation; arithmetic on a pinned frequency vs pinned bands

SESSION_98_DIR = PROJECT_ROOT / "computations" / "session-98"
VERDICT_TXT    = SESSION_98_DIR / "s98_gate_verdicts.txt"      # canonical path (gate-verdicts.md)
NPZ_OUT        = SESSION_98_DIR / "s98_kappa_indep_from_cgwb_freq.npz"
PNG_OUT        = SESSION_98_DIR / "s98_kappa_indep_from_cgwb_freq.png"

CANONICAL_PATH = SHARED / "canonical_constants.py"
S97_PEAK_NPZ   = PROJECT_ROOT / "computations" / "session-97" / "s97_omegagw_peak_height.npz"

# --- pre-registered detector-horizon bands (plan §W4-2 machinery_pin_map: band_edges_Hz) ---
# Pinned at plan-freeze. resonant_HF upper edge 1e11 is the OPTIMISTIC ceiling
# (memory: <~10^11 Hz HF-detector ceiling -- the highest band any proposed detector
# reaches). These are session-specific PRE-REGISTERED gate pins (detector horizons),
# NOT framework-wide canonicals; tagged local per math-scripts.md.
DETECTOR_BANDS = {                                # (local) {name: (lo_Hz, hi_Hz)}
    "PTA":         (1e-9, 1e-7),                  # (local) pulsar-timing-array nHz band
    "LISA":        (1e-4, 1e-1),                  # (local) space-laser mHz band
    "LIGO_ET":     (1e1,  1e4),                   # (local) ground-based audio band (LIGO/Virgo/ET)
    "resonant_HF": (1e9,  1e11),                  # (local) optimistic resonant high-frequency ceiling
}
F_LISA_PIVOT_HZ = 0.003                           # (local) LISA pivot for the headline decade-gap (s97 npz f_LISA_Hz=0.003)
TOL             = 1e-9                             # (local) float floor for decade-gap arithmetic (irrelevant to ~28.9-dec margin; pinned for completeness)


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema; mirrors s97_cooling_budget_kappa_pin sibling)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins (first 20 lines of stdout) ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""          # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
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


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Atomic single-write canonical line + dual-SHA companion row.

    Canonical path computations/session-98/s98_gate_verdicts.txt per
    gate-verdicts.md (NOT _shared/).
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] set-membership: f_obs(kappa_nat)="
        f"8.4835e+39 Hz vs union of detector horizons {{PTA,LISA,LIGO/ET,resonant-HF<=1e11}}; "
        f"f_obs OUTSIDE all bands (>=28.9 dec above optimistic HF ceiling) => CGWB frequency "
        f"axis supplies NO independent seconds-scale => kappa stays CONSISTENCY-PINNED; "
        f"NON-PHONONIC kappa-determinacy of an emergent transport knob over a substrate "
        f"(GGE-relic acoustic) CGWB peak\n"
    )
    SESSION_98_DIR.mkdir(parents=True, exist_ok=True)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def append_3tuple_row(sign_v: str, mag_v: str, regime_v: str, detail: str) -> None:
    """schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row (REQUIRED for [SIGN])."""
    row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; [SIGN]: f_obs strictly ABOVE highest "
        f"horizon edge => out-of-band => kappa consistency-pinned -> {detail})\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(row)


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main() -> int:
    # ---- input pins + dual-SHA ----
    inputs = [CANONICAL_PATH, S97_PEAK_NPZ]
    pins = log_input_pins(inputs)

    # =====================================================================
    # Def 1: f_obs(kappa_nat) = the CGWB peak frequency at the cooling-budget kappa-pin
    # =====================================================================
    f_obs = float(f_obs_CGWB_peak_kappa_nat)                    # 8.4835e+39 Hz (canonical, NOT superseded)
    kappa_nat = float(M_KK_inv_seconds)                         # 8.860439881925477e-42 s/tick
    log10_f_obs = float(np.log10(f_obs))                        # (local) = 39.9286

    print(f"\n=== {GATE_ID} -- NUMBERS FIRST ===")
    print(f"  f_obs(kappa_nat) [canonical f_obs_CGWB_peak_kappa_nat] = {f_obs:.6e} Hz")
    print(f"  log10(f_obs)                                          = {log10_f_obs:.4f}")
    print(f"  kappa_nat [M_KK_inv_seconds]                          = {kappa_nat:.12e} s/tick")

    # --- cross-check f_obs against the S97 npz f_peak_Hz ---
    s97 = np.load(S97_PEAK_NPZ, allow_pickle=True)
    f_peak_npz = float(s97["f_peak_Hz"])                       # (local) 8.4835e+39
    f_LISA_npz = float(s97["f_LISA_Hz"])                      # (local) 0.003
    kappa_nat_npz = float(s97["kappa_nat"])                   # (local) 8.860439881925477e-42
    kappa_robust_npz = bool(s97["kappa_robust"])             # (local) True (amplitude kappa-indep; freq kappa-DEP)
    kappa_grid_npz = np.asarray(s97["kappa_grid"], dtype=float)  # (local) 121-pt sweep [1e-20,1e-10]
    f_obs_xcheck_resid = abs(f_peak_npz - f_obs) / f_obs      # (local)
    kappa_xcheck_resid = abs(kappa_nat_npz - kappa_nat) / kappa_nat  # (local)
    f_LISA_resid = abs(f_LISA_npz - F_LISA_PIVOT_HZ) / F_LISA_PIVOT_HZ  # (local)
    print(f"\n  --- cross-check vs s97_omegagw_peak_height.npz ---")
    print(f"  npz f_peak_Hz   = {f_peak_npz:.6e}  (rel to canonical {f_obs_xcheck_resid:.3e})")
    print(f"  npz kappa_nat   = {kappa_nat_npz:.12e}  (rel {kappa_xcheck_resid:.3e})")
    print(f"  npz f_LISA_Hz   = {f_LISA_npz:.6e}  (pinned pivot {F_LISA_PIVOT_HZ}; rel {f_LISA_resid:.3e})")
    print(f"  npz kappa_robust= {kappa_robust_npz}  (amplitude kappa-indep; FREQUENCY kappa-DEP -- the axis tested)")
    print(f"  npz kappa_grid  = {kappa_grid_npz.size} pts, [{kappa_grid_npz.min():.0e},{kappa_grid_npz.max():.0e}]"
          f"  (the kappa-sweep grid -- carried fwd from S96, NOT s96_w6_5 which is ABSENT)")

    # =====================================================================
    # Def 2 + Def 3: set-membership test across the union of detector horizon bands
    # =====================================================================
    print(f"\n=== {GATE_ID} -- SET-MEMBERSHIP (f_obs in union of detector horizons?) ===")
    band_names = list(DETECTOR_BANDS.keys())                  # (local)
    band_results = {}                                          # (local) name -> dict
    any_member = False                                         # (local)
    member_band = None                                         # (local)
    decade_gaps_above_hi = {}                                  # (local) name -> log10(f_obs/hi) (>0 means above band)

    for name in band_names:
        lo, hi = DETECTOR_BANDS[name]                          # (local)
        is_member = bool(lo <= f_obs <= hi)                   # (local) set-membership
        # decade gap above the band's upper edge (POSITIVE => f_obs sits above this band):
        gap_above_hi = float(np.log10(f_obs / hi))            # (local)
        # decade gap below the band's lower edge (POSITIVE => f_obs sits below this band):
        gap_below_lo = float(np.log10(lo / f_obs))            # (local)
        band_results[name] = dict(lo=lo, hi=hi, is_member=is_member,
                                  gap_above_hi=gap_above_hi, gap_below_lo=gap_below_lo)
        decade_gaps_above_hi[name] = gap_above_hi
        if is_member:
            any_member = True
            member_band = name
        print(f"  {name:12s} band [{lo:.0e},{hi:.0e}]: f_obs in-band = {is_member}; "
              f"f_obs/hi = 10^{gap_above_hi:+.3f}")

    # Highest detector upper edge (the substitution-chain hi_max):
    hi_max_name = max(DETECTOR_BANDS, key=lambda n: DETECTOR_BANDS[n][1])   # (local) resonant_HF
    hi_max = DETECTOR_BANDS[hi_max_name][1]                                 # (local) 1e11
    log10_hi_max = float(np.log10(hi_max))                                 # (local) 11

    # Nearest horizon = the channel with the SMALLEST positive decade-gap above its upper edge
    # (i.e. the band whose ceiling is closest below f_obs). Since f_obs is above ALL bands,
    # all gaps_above_hi are positive; the nearest is the minimum.
    nearest_gap = float(min(decade_gaps_above_hi.values()))               # (local) = gap above resonant_HF ceiling
    nearest_band = min(decade_gaps_above_hi, key=lambda n: decade_gaps_above_hi[n])  # (local) resonant_HF
    decades_above_LISA_pivot = float(np.log10(f_obs / F_LISA_PIVOT_HZ))   # (local) headline 42.45

    print(f"\n  highest detector edge: {hi_max_name} hi_max = {hi_max:.0e} Hz (log10={log10_hi_max:.1f})")
    print(f"  nearest horizon = {nearest_band} ceiling; nearest decade-gap = +{nearest_gap:.3f} decades")
    print(f"  decades above LISA pivot (3 mHz) = +{decades_above_LISA_pivot:.3f}")
    print(f"  f_obs member of ANY band = {any_member}  (member_band={member_band})")

    # =====================================================================
    # SUBSTITUTION CHAIN read-off (the [SIGN] direction claim)
    # =====================================================================
    # Step 4: sign of (log10 f_obs - log10 hi_max). POSITIVE => f_obs strictly above the
    #         highest edge => out-of-band on the top channel => (a fortiori) out-of-band
    #         on all lower channels.
    sign_top_gap = float(log10_f_obs - log10_hi_max)                       # (local) = +28.929
    sign_is_positive = bool(sign_top_gap > 0.0)                            # (local) predicted: True
    print(f"\n  SUBSTITUTION CHAIN read-off:")
    print(f"    Step 4: log10(f_obs) - log10(hi_max) = {log10_f_obs:.4f} - {log10_hi_max:.1f} "
          f"= {sign_top_gap:+.3f}")
    print(f"    sign(top gap) = {'+' if sign_is_positive else '-'}  "
          f"(POSITIVE => f_obs ABOVE highest horizon => out-of-band)")

    # =====================================================================
    # REPORT-ONLY: how tight an EXTERNAL frequency anchor would need to be to triangulate kappa
    # =====================================================================
    # Since f_obs proportional to kappa: an external anchor at f_anchor in a real band would
    # pin kappa = kappa_nat * (f_anchor / f_obs(kappa_nat)). The required FRACTIONAL precision
    # on kappa is set by the band WIDTH: delta_kappa/kappa ~ (hi-lo)/f_center mapped through
    # the linear f_obs proportional to kappa relation -> the band's log-width in decades is the
    # achievable log-precision on kappa IF f_obs were in that band. (It is not; report-only.)
    print(f"\n  --- REPORT-ONLY: hypothetical kappa-triangulation precision per band ---")
    band_triangulation = {}                                                # (local)
    for name in band_names:
        lo, hi = DETECTOR_BANDS[name]                                      # (local)
        log_width_dec = float(np.log10(hi / lo))                          # (local) band log-width in decades
        # kappa that an in-band anchor at the band CENTER would imply (proportional scaling):
        f_center = float(np.sqrt(lo * hi))                                # (local) geometric center
        kappa_if_anchored = kappa_nat * (f_center / f_obs)               # (local) hypothetical
        band_triangulation[name] = dict(log_width_dec=log_width_dec,
                                        f_center=f_center,
                                        kappa_if_anchored=kappa_if_anchored)
        print(f"    {name:12s}: band log-width = {log_width_dec:.1f} dec; "
              f"IF anchored at center {f_center:.2e} Hz => kappa_implied = {kappa_if_anchored:.3e} s "
              f"(!= kappa_nat by 10^{np.log10(kappa_if_anchored/kappa_nat):+.1f}; NOT realized -- f_obs out-of-band)")

    # =====================================================================
    # 3-tuple (schema-v2) + composite collapse
    # =====================================================================
    # SIGN: predicted direction = f_obs strictly ABOVE the highest horizon edge (top gap > 0).
    #   PASS iff sign_is_positive (matches the substitution-chain Step-4 prediction). FAIL on mismatch.
    sign_v = "PASS" if sign_is_positive else "FAIL"                        # (local)

    # MAGNITUDE (INVERTED relative to a recovery gate -- see docstring rubric):
    #   INFO iff f_obs IS a member of some band (the SURPRISE outcome: kappa independently-pinnable);
    #   FAIL iff f_obs is OUTSIDE all bands (the PREDICTED detector-sterile outcome).
    if any_member:
        mag_v = "INFO"    # f_obs landed in a detector band -> kappa would be independently-pinnable
    else:
        mag_v = "FAIL"    # f_obs outside ALL horizons -> kappa stays consistency-pinned (predicted)

    # REGIME: VALID iff the arithmetic is well-defined: f_obs finite & positive, cross-check vs
    #   S97 npz matches (<1e-6 rel), kappa cross-check matches, all band edges positive & ordered.
    bands_well_ordered = all(DETECTOR_BANDS[n][0] < DETECTOR_BANDS[n][1] for n in band_names)  # (local)
    regime_ok = bool(
        np.isfinite(f_obs) and f_obs > 0.0
        and f_obs_xcheck_resid < 1e-6
        and kappa_xcheck_resid < 1e-6
        and bands_well_ordered
    )  # (local)
    regime_v = "VALID" if regime_ok else "MARGINAL"                        # (local)

    # Composite collapse (PRE-REGISTERED, gate-verdicts.md). This gate has no PASS branch
    # (mag is only INFO|FAIL), so the collapse yields FAIL (predicted out-of-band) or INFO
    # (surprise in-band):
    if regime_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"   # structurally unreachable for this gate (no PASS branch in rubric)

    print(f"\n  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print(f"  COMPOSITE = {composite}")
    print(f"  DISPOSITION: kappa is "
          f"{'INDEPENDENTLY-PINNABLE (f_obs in a detector band)' if any_member else 'CONSISTENCY-PINNED (f_obs outside all horizons)'}")

    # =====================================================================
    # PLOT
    # =====================================================================
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    # left: log10-frequency number line with detector bands + f_obs
    ax = axes[0]
    band_colors = {"PTA": "C0", "LISA": "C1", "LIGO_ET": "C2", "resonant_HF": "C3"}  # (local)
    for i, name in enumerate(band_names):
        lo, hi = DETECTOR_BANDS[name]
        ax.axvspan(np.log10(lo), np.log10(hi), color=band_colors[name], alpha=0.35,
                   label=f"{name} [{lo:.0e},{hi:.0e}]")
    ax.axvline(log10_f_obs, color="k", ls="--", lw=2.2,
               label=fr"$f_{{\rm obs}}(\kappa_{{\rm nat}})=8.4835\times10^{{39}}$ Hz")
    ax.axvline(np.log10(F_LISA_PIVOT_HZ), color="C1", ls=":", lw=1.4,
               label=r"LISA pivot 3 mHz")
    # annotate nearest gap
    ax.annotate("", xy=(log10_f_obs, 0.55), xytext=(log10_hi_max, 0.55),
                arrowprops=dict(arrowstyle="<->", color="firebrick", lw=1.6))
    ax.text((log10_f_obs + log10_hi_max) / 2, 0.60,
            f"+{nearest_gap:.1f} dec\nabove HF ceiling", ha="center", va="bottom",
            fontsize=8, color="firebrick")
    ax.set_xlim(-12, 42)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_xlabel(r"$\log_{10}(f\,/\,{\rm Hz})$")
    ax.set_title("CGWB peak vs detector horizons (frequency number line)\n"
                 f"$f_{{\\rm obs}}$ is +{nearest_gap:.1f} dec above the optimistic HF ceiling "
                 f"(OUT of every band)")
    ax.legend(fontsize=7, loc="upper left")
    ax.grid(alpha=0.3, axis="x")

    # right: decade-gap bar chart (f_obs above each band's upper edge)
    ax = axes[1]
    gaps = [decade_gaps_above_hi[n] for n in band_names]      # (local)
    bars = ax.bar(band_names, gaps, color=[band_colors[n] for n in band_names], alpha=0.75)
    for b, g in zip(bars, gaps):
        ax.text(b.get_x() + b.get_width() / 2, g + 0.5, f"+{g:.1f}", ha="center", va="bottom", fontsize=9)
    ax.axhline(0, color="k", lw=0.8)
    ax.set_ylabel(r"$\log_{10}(f_{\rm obs}/f_{\rm hi,band})$  [decades above band ceiling]")
    ax.set_title("Decades $f_{\\rm obs}$ sits ABOVE each detector band ceiling\n"
                 "(all POSITIVE $\\Rightarrow$ detector-sterile for $\\kappa$-triangulation)")
    ax.grid(alpha=0.3, axis="y")

    fig.suptitle(f"{GATE_ID}  --  composite={composite}  "
                 f"(sign={sign_v}, mag={mag_v}, regime={regime_v})  "
                 f"=> kappa {'INDEP-PINNABLE' if any_member else 'CONSISTENCY-PINNED'}",
                 fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    SESSION_98_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(PNG_OUT, dpi=130)
    plt.close(fig)
    print(f"\n  plot -> {PNG_OUT.relative_to(PROJECT_ROOT)}")

    # =====================================================================
    # NPZ
    # =====================================================================
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        composite=composite,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        # --- core observable ---
        f_obs=f_obs,
        log10_f_obs=log10_f_obs,
        kappa_nat=kappa_nat,
        # --- cross-check vs S97 npz ---
        f_peak_npz=f_peak_npz,
        f_obs_xcheck_resid=f_obs_xcheck_resid,
        kappa_nat_npz=kappa_nat_npz,
        kappa_xcheck_resid=kappa_xcheck_resid,
        f_LISA_npz=f_LISA_npz,
        f_LISA_pivot_pinned=F_LISA_PIVOT_HZ,
        f_LISA_resid=f_LISA_resid,
        kappa_robust_npz=kappa_robust_npz,
        kappa_grid_npz=kappa_grid_npz,
        # --- set-membership results ---
        band_names=np.array(band_names),
        band_lo=np.array([DETECTOR_BANDS[n][0] for n in band_names]),
        band_hi=np.array([DETECTOR_BANDS[n][1] for n in band_names]),
        band_is_member=np.array([band_results[n]["is_member"] for n in band_names]),
        gap_above_hi=np.array([decade_gaps_above_hi[n] for n in band_names]),
        any_member=any_member,
        member_band=str(member_band),
        # --- nearest horizon + headline gaps ---
        hi_max_name=str(hi_max_name),
        hi_max=hi_max,
        log10_hi_max=log10_hi_max,
        nearest_band=str(nearest_band),
        nearest_gap=nearest_gap,
        decades_above_LISA_pivot=decades_above_LISA_pivot,
        sign_top_gap=sign_top_gap,
        sign_is_positive=sign_is_positive,
        # --- report-only triangulation precision ---
        band_log_width_dec=np.array([band_triangulation[n]["log_width_dec"] for n in band_names]),
        band_f_center=np.array([band_triangulation[n]["f_center"] for n in band_names]),
        band_kappa_if_anchored=np.array([band_triangulation[n]["kappa_if_anchored"] for n in band_names]),
        # --- machinery pins ---
        N_detector_bands=len(band_names),
        tolerance=TOL,
        publication_precision=4,
        # --- constants ---
        M_KK=float(M_KK),
        hbar_SI=float(hbar_SI),
        GeV_to_J=float(GeV_to_J),
    )
    print(f"  data -> {NPZ_OUT.relative_to(PROJECT_ROOT)}")

    # =====================================================================
    # 4-tuple output tag (final non-verdict line) + verdict emission
    # =====================================================================
    value_str = (
        f"f_obs={f_obs:.4e}Hz(log10={log10_f_obs:.4f});"
        f"member_of_any_band={any_member};"
        f"nearest_horizon={nearest_band}_ceiling_{hi_max:.0e};"
        f"nearest_gap=+{nearest_gap:.3f}dec_ABOVE;"
        f"decades_above_LISA_pivot=+{decades_above_LISA_pivot:.3f};"
        f"kappa_status={'INDEPENDENTLY-PINNABLE' if any_member else 'CONSISTENCY-PINNED'};"
        f"CGWB_freq_axis_supplies_independent_seconds_scale={any_member}"
    )  # (local)
    print(f"\n  4-tuple: value={value_str!r} scheme={SCHEME} convention={CONVENTION} L_max={L_MAX}")

    audit_sha, content_sha = compute_dual_sha(THIS, CANONICAL_PATH, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    append_verdict(composite, value_str, audit_sha, content_sha)
    tuple_detail = (
        f"f_obs={f_obs:.3e}Hz is +{nearest_gap:.1f} dec ABOVE the optimistic HF ceiling "
        f"({hi_max:.0e} Hz) and +{decades_above_LISA_pivot:.1f} dec above the LISA pivot; "
        f"member of NO detector band (PTA/LISA/LIGO-ET/resonant-HF); CGWB FREQUENCY axis "
        f"(f_obs prop kappa) supplies NO independent seconds-scale; kappa stays "
        f"CONSISTENCY-PINNED (consistent with S96-OBS-CGWB-PEAK-FREQ FAIL GHz+; CGWB GW "
        f"flagship retired, GW->LSS BAO-ring migration)"
    )  # (local)
    append_3tuple_row(sign_v, mag_v, regime_v, tuple_detail)
    print(f"  verdict appended -> {VERDICT_TXT.relative_to(PROJECT_ROOT)}")
    print(f"\n=== {GATE_ID} COMPLETE: composite={composite} ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
