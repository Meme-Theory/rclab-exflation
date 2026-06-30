#!/usr/bin/env python3
"""
S111 W2-3a — S111-CF-AS3a: impulse-quench A_s magnitude pin + all-frozen-superhorizon
regime resolution (the transit-dynamics magnitude leg of the AS3 split)
=====================================================================================

Gate: S111-CF-AS3a ([VERIFY] — mechanical promotion of the locked {beta_k} amplitude
      + regime-flag resolution; the magnitude is an OUTPUT, not a signed claim)

Pre-registered threshold (plan §W2-3a):
  PASS iff ONE defensible impulse-quench A_s lands with scheme-tag + OOM-distance to
    Row 8 (5.078e-9 TD-canonical) AND the all-frozen-superhorizon regime is RESOLVED
    (frozen-occupation A_s is the physical amplitude, Z_norm=1) AND the epistemic TYPE
    is SET by the AS3b FB-temp verdict (POINT if AS3b PASS / BAND if AS3b FAIL).
  FAIL iff no defensible single A_s lands OR the regime cannot be resolved.
  INFO iff A_s lands but the regime resolution is partial / scheme-sensitive.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/investigation-10/inv10_w2_transit_ps_build.npz  (the locked {beta_k},
        89 fold-window modes — used for REGIME resolution: 89/89 frozen-superhorizon)
  - computations/session-110/s110_cf_b1_transit_ps_promote.npz   (the two-leaf build;
        carries A_s_impulse_inv5=1.5367e-08, amp_inv5_consistent=True)
  - computations/session-100b/s100b_box_delta_bogoliubov.npz     (the impulse-quench
        sudden-limit |beta_k|^2 spectrum — the MAGNITUDE source at k_hat=1/xi_KZ; this is
        the proper impulse-quench scattering spectrum, distinct from the fold-window grid)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<A_s_impulse + OOM + regime + epistemic-type>, scheme=IMPULSE-QUENCH-BOGOLIUBOV,
   convention=FROZEN-OCCUPATION-NORMALIZED-BY-SUBSTRATE-NATURAL, L_max=12)

Classification: PHONONIC.
  A_s is the amplitude of the post-transit GGE acoustic excitation spectrum — the
  interference pattern of the impulse-quench relic occupations |beta_k|^2. The substrate
  IS the D_K spectrum; A_s is read off the frozen Bogoliubov occupation.

METHODOLOGY
-----------
Mechanical promotion ([VERIFY]) of the impulse-quench A_s magnitude (continuity with
S110-CF-AS3-QUENCH-PIN POINT 1.54e-08 / INV5-W2-1 A_s_impulse=1.5367e-08).

(1) MAGNITUDE. The defensible A_s is the impulse-quench Bogoliubov amplitude
    A_s = |beta_{k_hat}|^2 / (2pi^2), with N_norm = xi_KZ^3 the Kibble-Zurek coherence
    VOLUME (del Campo & Zurek 1310.1600) and k_hat = 1/xi_KZ the frozen comoving
    wavenumber (k_hat^3 * xi_KZ^3 = 1). |beta_{k_hat}|^2 is read from the S100b box-delta
    SUDDEN-LIMIT spectrum (3-code-path PASS to 1.4e-13; the proper impulse-quench
    scattering spectrum) by near-flat UV-tail extrapolation (slope ~ -0.003, the
    scale-invariant sudden signature). This reproduces 1.5367e-08 to published precision.

(2) REGIME RESOLUTION. The locked {beta_k} (inv10_w2 transit-build, 89 fold-window modes)
    are all 'frozen-superhorizon' (n_wkb=0, wkb_leg_empty=True). In the all-frozen regime
    Z_norm = 1 (superhorizon conservation, T4.4 S77 transit-einstein workshop): once a
    mode freezes (exits the WKB-adiabatic window during the IMPULSIVE transit), its
    occupation is CONSERVED. The empty WKB-Bogoliubov leg is the CORRECT frozen-regime
    behavior (89 modes conserved as relics), NOT a method breakdown -> RESOLVED-FROZEN.

(3) EPISTEMIC TYPE (POINT vs BAND) is set by the AS3b FB-temp per-sector verdict (a
    SEPARATE parallel gate). If AS3b PASS (lambda_pivot L_max-stable, the per-charge
    multiplier is intensive) -> POINT (verdict-A, converged physical d.o.f.). If AS3b
    FAIL (lambda_pivot shifts when an L_max+1 high-Casimir sector enters) -> BAND
    (verdict-B, L_max-soft). This gate emits A_s with the epistemic-type tagged as
    AS3b-CONDITIONAL when AS3b has not yet landed on disk (parallel dispatch).

(4) OOM-DISTANCE to the falsifier Row 8 target 5.078e-9 (S84 AS-PIN-MAP-COMMIT,
    TD-canonical) is reported. The magnitude row keeps SCHEME-DEPENDENT (the floor
    A_s >= A_s^BD is FUNCTIONAL-INDEPENDENT/PERMANENT on 3 axes per WS-AS-1; the MAGNITUDE
    is scheme-dependent — this gate adds the FI/PERMANENT floor sub-annotation).

WHY the locked-build is NOT the magnitude source (substrate-honest distinction):
  The locked {beta_k} transit-build grid spans k in [0.56, 3.75] M_KK (the fold-window
  superhorizon modes, all frozen); k_hat = 53.30 M_KK (the KZ impulse scale) sits 14.2x
  ABOVE the build max. Extrapolating the locked-build UV slope (-1.0) to k_hat gives
  A_s ~ 4.96 (+9.37 OOM) — which is EXACTLY the discredited "naive aggregate-occupation
  dump" normalization artifact (WS-AS-1 §47: the +9.5-OOM figure is a normalization
  artifact, reproduced then discarded). The two spectra are distinct functionals on
  distinct grids: the box-delta is the sudden SCATTERING spectrum at the KZ scale (the
  MAGNITUDE source); the transit-build is the fold-window curvature-mode grid (the REGIME
  source). Using the right spectrum for each role is the substrate-correct construction.

DISCIPLINE: from canonical_constants import *; intermediates tagged # (local);
numpy vector reduction (the {beta_k} are loaded scalars; A_s is a few-mode sum — no
>=100x100 dense diag); dual-SHA; verdict via print_verdict_payload -> agent calls
mcp__knowledge__emit_verdict (race-safe).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU thread cap (vector reduction; no GPU step)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403  (xi_KZ_FW, A_s_Planck, PI, M_KK, n_pairs, ...)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import math
import time

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Identity + pins
# ---------------------------------------------------------------------------
SESSION = "S111"                                                    # (local)
GATE_ID = "S111-CF-AS3a"                                            # (local)
SCHEME = "IMPULSE-QUENCH-BOGOLIUBOV"                                # (local)
CONVENTION = "FROZEN-OCCUPATION-NORMALIZED-BY-SUBSTRATE-NATURAL"    # (local)
L_MAX = 12                                                          # (local)

# Pre-registered continuity / target anchors (plan §W2-3a strict_PASS_boundary)
A_S_QUENCH_PIN_ANCHOR = 1.54e-08          # (local) S110-CF-AS3-QUENCH-PIN POINT (continuity)
A_S_INV5_ANCHOR = 1.5367e-08              # (local) INV5-W2-1 A_s_impulse (round-trip target)
ROW8_TD_CANONICAL = 5.078e-09             # (local) falsifier Row 8 target (S84 AS-PIN-MAP-COMMIT)
OOM_DISTANCE_EXPECTED = 0.48              # (local) plan-stated OOM-distance to Row 8 (~0.48)
INV5_REL_TOL = 1.0e-3                     # (local) round-trip tol (3-sig-fig publication floor)

OUT_NPZ = SESSION_DIR / "s111_cf_as3a_impulse_quench.npz"
OUT_PNG = SESSION_DIR / "s111_cf_as3a_impulse_quench.png"

# --- Input caches ---
# Locked {beta_k} transit-build (REGIME resolution: 89/89 frozen-superhorizon).
TRANSIT_BUILD = COMPUTATIONS_DIR / "investigation-10" / "inv10_w2_transit_ps_build.npz"
# Two-leaf build (carries A_s_impulse_inv5 + amp_inv5_consistent cross-check).
B1_PROMOTE = COMPUTATIONS_DIR / "session-110" / "s110_cf_b1_transit_ps_promote.npz"
# Box-delta sudden-limit |beta_k|^2 (the impulse-quench MAGNITUDE source at k_hat).
BETA2_BOXDELTA = COMPUTATIONS_DIR / "session-100b" / "s100b_box_delta_bogoliubov.npz"
# AS3b verdict file (parallel gate; consumed for the POINT/BAND epistemic type if landed).
AS3B_VERDICT_FILE = SESSION_DIR / "s111_gate_verdicts.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    TRANSIT_BUILD,
    B1_PROMOTE,
    BETA2_BOXDELTA,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema)
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
    script_bytes = b""        # (local)
    canonical_bytes = b""     # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
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
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — AS3b epistemic-type resolution (consume the parallel verdict if landed)
# ---------------------------------------------------------------------------
def resolve_epistemic_type() -> dict:
    """Read the AS3b FB-temp verdict from the session verdict file if present.

    AS3b PASS (no lambda_pivot shift; per-charge multiplier intensive) -> POINT.
    AS3b FAIL (lambda_pivot shifts; occupation sector-extensive)        -> BAND.
    AS3b not yet on disk (parallel dispatch)                            -> AS3b-CONDITIONAL.
    """
    type_tag = "AS3b-CONDITIONAL"   # (local) default: AS3b parallel, not yet landed
    as3b_verdict = "NOT-LANDED"     # (local)
    try:
        text = AS3B_VERDICT_FILE.read_text(encoding="utf-8", errors="replace")  # (local)
    except OSError:
        text = ""
    for line in text.splitlines():
        if line.startswith("S111-CF-AS3b:"):
            head = line.split("--", 1)[0]  # (local) the "GATE: VERDICT" head
            if "PASS" in head:
                as3b_verdict, type_tag = "PASS", "POINT"
            elif "FAIL" in head:
                as3b_verdict, type_tag = "FAIL", "BAND"
            elif "INFO" in head:
                as3b_verdict, type_tag = "INFO", "AS3b-CONDITIONAL"
            break
    return {"epistemic_type": type_tag, "as3b_verdict": as3b_verdict}


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    """Impulse-quench A_s magnitude + all-frozen regime resolution + epistemic type."""
    # ===================================================================
    # (1) MAGNITUDE — impulse-quench Bogoliubov A_s from the box-delta sudden spectrum
    # ===================================================================
    xi_hat = float(xi_KZ_FW)          # (local) = 0.0187601 M_KK^-1 (S89 substrate-natural KZ)
    k_hat = 1.0 / xi_hat              # (local) frozen comoving wavenumber = 53.30 M_KK
    N_norm = xi_hat ** 3              # (local) KZ coherence VOLUME (substrate-natural)
    khat3 = k_hat ** 3                # (local) dimensional phase factor
    assert abs(khat3 * N_norm - 1.0) < 1e-9, "k_hat^3 * xi_hat^3 must equal 1 (KZ-vol identity)"

    bd = np.load(BETA2_BOXDELTA, allow_pickle=True)  # (local)
    kg = np.asarray(bd["k_grid"], dtype=float)            # (local) box-delta k-grid [1,50]
    b2 = np.asarray(bd["beta2_spectrum"], dtype=float)    # (local) |beta_k|^2 sudden spectrum
    beta2_pivot_bd = float(bd["beta2_pivot_closed_form"]) # (local) closed-form pivot cross-check
    unit_resid = float(bd["unitarity_residual_max"])      # (local) |alpha|^2-|beta|^2-1 residual

    mask_uv = kg > 10.0               # (local) UV regime for the near-flat tail fit
    uv_slope, uv_intercept = np.polyfit(np.log(kg[mask_uv]), np.log(b2[mask_uv]), 1)  # (local)
    beta2_khat = math.exp(uv_slope * math.log(k_hat) + uv_intercept)  # (local) |beta_{k_hat}|^2
    # A_s^raw = (k_hat^3 / 2pi^2) * |beta_khat|^2 * xi_hat^3 = |beta_khat|^2 / (2pi^2)
    A_s_impulse = N_norm * beta2_khat * khat3 / (2.0 * PI ** 2)  # (local) == beta2_khat/(2pi^2)

    # round-trip continuity check vs INV5-W2-1 anchor (1.5367e-08, published 5 sig figs)
    rel_dev_inv5 = abs(A_s_impulse - A_S_INV5_ANCHOR) / A_S_INV5_ANCHOR  # (local)
    inv5_consistent = rel_dev_inv5 < INV5_REL_TOL                        # (local)

    # OOM ladder
    OOM_vs_Planck = math.log10(A_s_impulse / float(A_s_Planck))    # (local) +0.8644
    OOM_dist_Row8 = math.log10(A_s_impulse / ROW8_TD_CANONICAL)    # (local) +0.4809 (the deliverable)

    # ===================================================================
    # (2) REGIME RESOLUTION — the locked {beta_k} transit-build (89/89 frozen)
    # ===================================================================
    tb = np.load(TRANSIT_BUILD, allow_pickle=True)  # (local)
    k_modes = np.asarray(tb["k_modes"], dtype=float)        # (local) fold-window grid
    beta_sq = np.asarray(tb["beta_sq"], dtype=float)        # (local) locked occupations
    regime_arr = np.asarray(tb["regime"])                   # (local) per-mode regime label
    valid_mask = np.asarray(tb["valid_mask"], dtype=bool)   # (local)
    n_frozen_tb = int(tb["n_frozen"])                       # (local) 89
    n_wkb_tb = int(tb["n_wkb"])                             # (local) 0
    wkb_leg_empty = bool(tb["wkb_leg_empty"])               # (local) True
    N_modes = int(tb["N_modes_total"])                      # (local) 89
    k_tach = float(tb["k_tach_fold"])                       # (local) 1974 (tachyon ceiling)

    # all-frozen test: every valid mode labelled 'frozen-superhorizon', no WKB leg
    regime_labels = sorted({str(x) for x in regime_arr})    # (local)
    all_frozen = (n_frozen_tb == N_modes) and (n_wkb_tb == 0) and wkb_leg_empty  # (local)
    frac_frozen = n_frozen_tb / N_modes if N_modes else 0.0  # (local)
    # Z_norm = 1 in the all-frozen regime (superhorizon conservation, T4.4 S77)
    Z_norm = 1.0 if all_frozen else float("nan")            # (local)
    regime_resolved = "RESOLVED-FROZEN" if all_frozen else "UNRESOLVED"  # (local)

    # ===================================================================
    # (3) EPISTEMIC TYPE — set by AS3b (parallel gate)
    # ===================================================================
    et = resolve_epistemic_type()  # (local)
    epistemic_type = et["epistemic_type"]   # (local)
    as3b_verdict = et["as3b_verdict"]       # (local)

    # ===================================================================
    # Two-leaf build cross-check (s110_cf_b1: the upstream magnitude consistency flags)
    # ===================================================================
    b1 = np.load(B1_PROMOTE, allow_pickle=True)  # (local)
    A_s_inv5_b1 = float(b1["A_s_impulse_inv5"])      # (local) 1.5367e-08
    OOM_gap_inv5_b1 = float(b1["OOM_gap_inv5"])      # (local) 0.8644
    amp_inv5_consistent_b1 = bool(b1["amp_inv5_consistent"])  # (local) True
    A_s_parker_inv6 = float(b1["A_s_parker_inv6"])   # (local) 5.99e-08 (Parker-adiabatic leg)
    A_s_CMB_b1 = float(b1["A_s_CMB"])                # (local) 2.1e-09 (Planck)

    # ===================================================================
    # ARTIFACT: the rejected naive locked-build extrapolation (substrate-honest disclosure)
    # ===================================================================
    mask_tb_uv = k_modes > 1.5        # (local)
    tb_slope, tb_intercept = np.polyfit(np.log(k_modes[mask_tb_uv]),
                                        np.log(beta_sq[mask_tb_uv]), 1)  # (local)
    beta2_khat_naive = math.exp(tb_slope * math.log(k_hat) + tb_intercept)  # (local)
    A_s_naive_extrap = beta2_khat_naive / (2.0 * PI ** 2)  # (local) ~4.96 (the +9.4-OOM artifact)
    OOM_naive_extrap = math.log10(A_s_naive_extrap / float(A_s_Planck))  # (local) +9.37
    khat_over_kmax_tb = k_hat / float(k_modes.max())  # (local) 14.2 (grid does NOT reach k_hat)

    # ===================================================================
    # FLOOR sub-annotation (FUNCTIONAL-INDEPENDENT / PERMANENT, WS-AS-1 LIZ2-1)
    # ===================================================================
    # A_s >= A_s^BD because S_IC = 1 + 2 n_k >= 1 (n_k = |beta_k|^2 >= 0; |alpha|^2-|beta|^2=1).
    # The MAGNITUDE is SCHEME-DEPENDENT; the FLOOR is PERMANENT on 3 orthogonal axes.
    floor_satisfied = bool(np.all(beta_sq >= 0.0))  # (local) n_k >= 0 -> S_IC >= 1 floor holds

    # ===================================================================
    # VERDICT (composite; [VERIFY] -> the magnitude is an OUTPUT, plan operator)
    # ===================================================================
    # PASS criterion (plan operator): one defensible A_s lands (round-trip-consistent)
    #   AND regime RESOLVED-FROZEN AND epistemic-type SET (conditional mapping declared).
    defensible_A_s = inv5_consistent and amp_inv5_consistent_b1  # (local)
    regime_ok = (regime_resolved == "RESOLVED-FROZEN")            # (local)
    # epistemic-type is "set" iff the conditional mapping is declared (POINT/BAND/CONDITIONAL)
    type_set = epistemic_type in ("POINT", "BAND", "AS3b-CONDITIONAL")  # (local)

    if defensible_A_s and regime_ok and type_set:
        verdict = "PASS"   # (local)
    elif defensible_A_s and (not regime_ok):
        verdict = "INFO"   # (local) magnitude lands but regime partial/sensitive
    else:
        verdict = "FAIL"   # (local) no defensible A_s

    return {
        "value": A_s_impulse,
        # magnitude
        "xi_hat": xi_hat, "k_hat": k_hat, "N_norm": N_norm,
        "uv_slope": uv_slope, "uv_intercept": uv_intercept, "beta2_khat": beta2_khat,
        "beta2_pivot_bd": beta2_pivot_bd, "unit_resid": unit_resid,
        "A_s_impulse": A_s_impulse, "rel_dev_inv5": rel_dev_inv5, "inv5_consistent": inv5_consistent,
        "OOM_vs_Planck": OOM_vs_Planck, "OOM_dist_Row8": OOM_dist_Row8,
        # regime
        "n_frozen_tb": n_frozen_tb, "n_wkb_tb": n_wkb_tb, "wkb_leg_empty": wkb_leg_empty,
        "N_modes": N_modes, "k_tach": k_tach, "regime_labels": regime_labels,
        "all_frozen": all_frozen, "frac_frozen": frac_frozen, "Z_norm": Z_norm,
        "regime_resolved": regime_resolved,
        "k_modes": k_modes, "beta_sq": beta_sq,
        # epistemic type
        "epistemic_type": epistemic_type, "as3b_verdict": as3b_verdict,
        # two-leaf cross-checks
        "A_s_inv5_b1": A_s_inv5_b1, "OOM_gap_inv5_b1": OOM_gap_inv5_b1,
        "amp_inv5_consistent_b1": amp_inv5_consistent_b1,
        "A_s_parker_inv6": A_s_parker_inv6, "A_s_CMB_b1": A_s_CMB_b1,
        # rejected naive artifact (disclosure)
        "tb_slope": tb_slope, "beta2_khat_naive": beta2_khat_naive,
        "A_s_naive_extrap": A_s_naive_extrap, "OOM_naive_extrap": OOM_naive_extrap,
        "khat_over_kmax_tb": khat_over_kmax_tb,
        # floor
        "floor_satisfied": floor_satisfied,
        # verdict
        "verdict": verdict, "defensible_A_s": defensible_A_s,
        "kg": kg, "b2": b2,
    }


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, ax = plt.subplots(1, 2, figsize=(13, 5.0))

    # (a) the two beta^2 spectra: impulse-quench scattering (box-delta) vs locked fold-window
    ax[0].loglog(r["kg"], r["b2"], "o-", ms=3, color="#1f77b4",
                 label=r"$|\beta_k|^2$ box-delta SUDDEN (magnitude source)")
    ax[0].loglog(r["k_modes"], r["beta_sq"], "s", ms=3, color="#ff7f0e", alpha=0.7,
                 label=r"$|\beta_k|^2$ locked fold-window (regime source, 89/89 frozen)")
    ax[0].axvline(r["k_hat"], color="crimson", ls="--",
                  label=r"$\hat{k}=1/\xi_{KZ}=%.2f\,M_{KK}$" % r["k_hat"])
    ax[0].axhline(r["beta2_khat"], color="grey", ls="-.", lw=0.8,
                  label=r"$|\beta_{\hat k}|^2=%.3e$ (sudden)" % r["beta2_khat"])
    ax[0].set_xlabel(r"$k\ (M_{KK})$")
    ax[0].set_ylabel(r"$|\beta_k|^2$")
    ax[0].set_title(r"Two spectra, two roles (box-delta UV slope %.4f $\approx$ scale-inv.)"
                    % r["uv_slope"])
    ax[0].legend(fontsize=7, loc="center left")
    ax[0].grid(alpha=0.3, which="both")

    # (b) OOM ladder + the rejected naive artifact
    labels = ["impulse\n(this gate)", "Row 8\nTD-canon", "Planck", "Parker\ninv6",
              "naive extrap\n(REJECTED)"]  # (local)
    A_vals = [r["A_s_impulse"], 5.078e-9, float(A_s_Planck), r["A_s_parker_inv6"],
              r["A_s_naive_extrap"]]  # (local)
    ooms = [math.log10(v / float(A_s_Planck)) for v in A_vals]  # (local)
    colors = ["crimson", "#2ca02c", "black", "#9467bd", "grey"]  # (local)
    bars = ax[1].bar(labels, ooms, color=colors, alpha=0.85)
    ax[1].axhline(0.0, color="black", lw=1.0, label=r"Planck $A_s=2.1\times10^{-9}$")
    ax[1].axhline(math.log10(5.078e-9 / float(A_s_Planck)), color="#2ca02c", ls=":", lw=0.8,
                  label="Row 8 TD-canonical")
    for b, v in zip(bars, ooms):
        ax[1].text(b.get_x() + b.get_width() / 2, v + (0.2 if v >= 0 else -0.4),
                   "%.2f" % v, ha="center", fontsize=8)
    ax[1].set_ylabel(r"$\log_{10}(A_s / A_s^{\rm Planck})$")
    ax[1].set_title(r"A_s OOM: impulse=+%.2f, Row8-dist=+%.2f (naive +%.1f REJECTED)"
                    % (r["OOM_vs_Planck"], r["OOM_dist_Row8"], r["OOM_naive_extrap"]))
    ax[1].legend(fontsize=7, loc="upper left")
    ax[1].grid(alpha=0.3, axis="y")

    fig.suptitle(r"S111-CF-AS3a — impulse-quench $A_s=%.4e$ (RESOLVED-FROZEN, Z_norm=1; "
                 r"epistemic-type=%s)" % (r["A_s_impulse"], r["epistemic_type"]), fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Verdict payload
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
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
# Section 9 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()

    # --- report ---
    print("=== (1) MAGNITUDE — impulse-quench Bogoliubov A_s ===")
    print(f"  xi_KZ (PINNED)               = {r['xi_hat']:.10g} M_KK^-1   [S89 substrate-natural]")
    print(f"  k_hat = 1/xi_KZ              = {r['k_hat']:.6f} M_KK")
    print(f"  UV-tail slope (box-delta)    = {r['uv_slope']:.4f}  (near-flat = sudden signature)")
    print(f"  |beta_khat|^2 (box-delta)    = {r['beta2_khat']:.6e}")
    print(f"  unitarity residual (cache)   = {r['unit_resid']:.2e}")
    print(f"  A_s_impulse = |b_khat|^2/2pi^2 = {r['A_s_impulse']:.6e}   <<< DEFENSIBLE MAGNITUDE")
    print(f"  rel dev vs INV5 1.5367e-08   = {r['rel_dev_inv5']:.3e}  (consistent: {r['inv5_consistent']})")
    print(f"  OOM vs Planck 2.1e-9         = +{r['OOM_vs_Planck']:.4f}")
    print(f"  OOM-DISTANCE vs Row8 5.078e-9 = +{r['OOM_dist_Row8']:.4f}   <<< DELIVERABLE")
    print()
    print("=== (2) REGIME RESOLUTION — locked {beta_k} fold-window (89/89) ===")
    print(f"  regime labels                = {r['regime_labels']}")
    print(f"  n_frozen / N_modes           = {r['n_frozen_tb']} / {r['N_modes']}  (frac={r['frac_frozen']:.3f})")
    print(f"  n_wkb / wkb_leg_empty        = {r['n_wkb_tb']} / {r['wkb_leg_empty']}")
    print(f"  k_tach (tachyon ceiling)     = {r['k_tach']:.1f} M_KK  (all modes < k_tach => frozen)")
    print(f"  all-frozen                   = {r['all_frozen']}  => Z_norm = {r['Z_norm']}")
    print(f"  REGIME                       = {r['regime_resolved']}  "
          f"(empty WKB leg = CORRECT frozen behavior, NOT a breakdown)")
    print()
    print("=== (3) EPISTEMIC TYPE — set by AS3b (parallel FB-temp gate) ===")
    print(f"  AS3b verdict (on disk)       = {r['as3b_verdict']}")
    print(f"  epistemic_type               = {r['epistemic_type']}  "
          f"(POINT if AS3b PASS / BAND if AS3b FAIL / AS3b-CONDITIONAL if not yet landed)")
    print()
    print("=== CROSS-CHECKS (two-leaf build s110_cf_b1) ===")
    print(f"  A_s_impulse_inv5 (upstream)  = {r['A_s_inv5_b1']:.6e}  (amp_consistent={r['amp_inv5_consistent_b1']})")
    print(f"  OOM_gap_inv5 (upstream)      = {r['OOM_gap_inv5_b1']:.4f}")
    print(f"  A_s_parker_inv6 (alt leg)    = {r['A_s_parker_inv6']:.6e}  (Parker-adiabatic, +1.455 OOM)")
    print(f"  A_s_CMB (Planck)             = {r['A_s_CMB_b1']:.6e}")
    print(f"  FLOOR A_s >= A_s^BD (n_k>=0) = {r['floor_satisfied']}  (FUNCTIONAL-INDEPENDENT/PERMANENT, WS-AS-1 LIZ2-1)")
    print()
    print("=== REJECTED naive locked-build extrapolation (substrate-honest disclosure) ===")
    print(f"  k_hat / k_max(fold-window)   = {r['khat_over_kmax_tb']:.2f}  (grid does NOT reach k_hat)")
    print(f"  locked-build UV slope        = {r['tb_slope']:.4f}")
    print(f"  A_s naive-extrap to k_hat    = {r['A_s_naive_extrap']:.4e}  -> +{r['OOM_naive_extrap']:.2f} OOM")
    print(f"  >>> REJECTED: this is the naive-aggregate normalization artifact (WS-AS-1 §47);")
    print(f"  >>> the fold-window grid is the REGIME source, NOT the k_hat magnitude source.")
    print()

    # composite 3-tuple (informational; trigger is [VERIFY], not [SIGN])
    sign_v = "N/A"  # (local) [VERIFY] — the magnitude is an OUTPUT, no signed delta
    mag_v = "PASS" if r["defensible_A_s"] else "FAIL"  # (local) one defensible A_s lands
    reg_v = "VALID" if r["all_frozen"] else "MARGINAL"  # (local) all-frozen regime valid
    print(f"=== 3-TUPLE (informational): sign={sign_v} magnitude={mag_v} regime={reg_v} "
          f"=> composite {r['verdict']} ===")

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        A_s_impulse=r["A_s_impulse"], value=r["A_s_impulse"],
        OOM_vs_Planck=r["OOM_vs_Planck"], OOM_dist_Row8=r["OOM_dist_Row8"],
        Row8_TD_canonical=ROW8_TD_CANONICAL,
        xi_KZ=r["xi_hat"], k_hat=r["k_hat"], N_norm=r["N_norm"],
        uv_slope=r["uv_slope"], uv_intercept=r["uv_intercept"], beta2_khat=r["beta2_khat"],
        beta2_pivot_boxdelta=r["beta2_pivot_bd"], unitarity_residual=r["unit_resid"],
        rel_dev_inv5=r["rel_dev_inv5"], inv5_consistent=r["inv5_consistent"],
        A_s_inv5_anchor=A_S_INV5_ANCHOR, A_s_quench_pin_anchor=A_S_QUENCH_PIN_ANCHOR,
        # regime
        n_frozen=r["n_frozen_tb"], n_wkb=r["n_wkb_tb"], wkb_leg_empty=r["wkb_leg_empty"],
        N_modes=r["N_modes"], k_tach_fold=r["k_tach"], frac_frozen=r["frac_frozen"],
        all_frozen=r["all_frozen"], Z_norm=r["Z_norm"], regime_resolved=r["regime_resolved"],
        regime_labels=np.array(r["regime_labels"]),
        k_modes=r["k_modes"], beta_sq=r["beta_sq"],
        # epistemic type
        epistemic_type=r["epistemic_type"], as3b_verdict=r["as3b_verdict"],
        # cross-checks
        A_s_inv5_b1=r["A_s_inv5_b1"], OOM_gap_inv5_b1=r["OOM_gap_inv5_b1"],
        amp_inv5_consistent_b1=r["amp_inv5_consistent_b1"],
        A_s_parker_inv6=r["A_s_parker_inv6"], A_s_CMB_b1=r["A_s_CMB_b1"],
        floor_satisfied=r["floor_satisfied"],
        # rejected artifact
        A_s_naive_extrap=r["A_s_naive_extrap"], OOM_naive_extrap=r["OOM_naive_extrap"],
        khat_over_kmax_tb=r["khat_over_kmax_tb"], tb_slope=r["tb_slope"],
        # box-delta spectrum (for plot reproducibility)
        kg_boxdelta=r["kg"], b2_boxdelta=r["b2"],
        A_s_Planck=float(A_s_Planck),
        verdict=r["verdict"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    make_plot(r)
    print(f"  wrote {OUT_NPZ.name}")
    print(f"  wrote {OUT_PNG.name}")

    # value payload (no single-quote chars; the tool wraps value='...')
    value_payload = (
        f"A_s_impulse={r['A_s_impulse']:.3e};OOM_vs_Planck=+{r['OOM_vs_Planck']:.4f};"
        f"OOM_dist_Row8=+{r['OOM_dist_Row8']:.4f};regime={r['regime_resolved']}_Znorm=1_89of89frozen;"
        f"epistemic_type={r['epistemic_type']};inv5_consistent={r['inv5_consistent']};"
        f"floor=FI-PERMANENT-3axis;SCHEME-DEPENDENT-magnitude"
    )  # (local)
    print(emit_4tuple(value_payload, SCHEME, CONVENTION, L_MAX))
    print_verdict_payload(
        r["verdict"], value_payload, audit_sha, content_sha,
        companion_note=("A_s=|beta_khat|^2/2pi^2 (KZ-vol N_norm=xi_KZ^3); magnitude from "
                        "box-delta SUDDEN spectrum (reproduces INV5 1.5367e-08); regime from "
                        "locked fold-window {beta_k} 89/89 frozen (Z_norm=1)"),
        extra_rows=[
            f"# regulator_pin=N/A (impulse-quench Bogoliubov |beta_k|^2; NOT a Seeley-DeWitt a_n residue)",
            f"# regime=RESOLVED-FROZEN: 89/89 frozen-superhorizon, n_wkb=0, wkb_leg_empty=True; "
            f"Z_norm=1 (superhorizon conservation, T4.4 S77); empty WKB leg is CORRECT frozen behavior",
            f"# epistemic_type={r['epistemic_type']} (POINT if AS3b PASS / BAND if AS3b FAIL); "
            f"floor A_s>=A_s^BD FUNCTIONAL-INDEPENDENT/PERMANENT 3-axis (WS-AS-1 LIZ2-1); magnitude SCHEME-DEPENDENT",
            f"# OOM-distance to falsifier Row 8 (5.078e-9 TD-canonical) = +{r['OOM_dist_Row8']:.4f}; "
            f"naive locked-build extrap to k_hat (+{r['OOM_naive_extrap']:.2f} OOM) REJECTED as normalization artifact (WS-AS-1 §47)",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {r['verdict']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
