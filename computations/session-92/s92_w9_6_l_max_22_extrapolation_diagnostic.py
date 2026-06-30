#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S92-W9-CF-S91-W6-2-L-MAX-22-EXTRAPOLATION-DIAGNOSTIC

Post-hoc root-cause decomposition of the K_csub_R Mellin/zeta = -245.69
intercept (from S91 W6-2) into:
  (a) analytic kappa_2-quadratic growth contribution
        analytic_quadratic_contribution(L) = 1 + kappa_2_substrate_FW * L^2 / (5*pi)^2
  (b) cache-truncated proxy
        cache_truncated_proxy(L) = sum_{i} 1/lambda_i^2   over the L_max=L truncation
        of the L_max=12 master cache, with N_cache HELD at the L_max=12 ceiling
        for L > 12 (cache-ceiling SCHEMATIC artifact).

Trigger:        [AUDIT]
Classification: PHONONIC
Agent:          gen-physicist

SUBSTRATE FRAMING (MANDATORY — direction of explanation):
  The substrate IS the L_max-truncated spectral triple (A_K, H_K, D_K) whose
  eigenvalue cache at L_max=12 IS the substrate's image. The K_csub_R Mellin/zeta
  intercept IS a substrate-IS regulator-class-dependent quantity at the
  substrate-distance-2 Mellin pole s=4, evaluated through the SCHEMATIC
  `M_Pl_eff_sq_with_regulator` proxy. The L_max=12 cache IS the substrate's
  image; the `sum 1/lambda_i^2` evaluated for L > 12 IS a cache-ceiling SCHEMATIC
  artifact, NOT a substrate truth at L > 12. We do NOT frame this as
  "the regulator extrapolates outside the cache" — INVERT: the diagnostic IS a
  substrate-physics attribution of the empirical intercept to (a) the substrate-IS
  analytic-quadratic kappa_2 contribution + (b) the SCHEMATIC cache-ceiling
  artifact. The substrate's TRUE alpha(s=4) at L > 12 is NOT in this gate's scope;
  this gate documents the SCHEMATIC-helper attribution structure that motivates the
  FULL-physical retry (CF-S91-W6-2-FULL-PHYSICAL-RETRY) at S92 W1.

SCHEMATIC LEVEL-PIN DISCLOSURE (K=4 MANDATORY per
`.claude/rules/substrate-first-canonical-sourcing.md §(iv)`):
  This gate analyzes the output of `_spectral_action_regulators.py`-class SCHEMATIC
  machinery via the S91 W6-2 producing function `M_Pl_eff_sq_with_regulator`
  (a deterministic SCHEMATIC analog, not a FULL physical regularization). The
  SCHEMATIC class is disclosed in the verdict-line `convention=` field
  (`-SCHEMATIC-helper-disclosed`) and the `# tier_pin=TIER-2` companion comment row.

Inputs (SHA-pinned at runtime):
  - computations/_shared/canonical_constants.py        (kappa_2_substrate_FW, tau_fold, M_KK)
  - computations/session-91/s91_w6_2_k_hk_k_csub_empirical_anchoring.npz
                                                       (ratio_per_L, L_grid, M_Pl_eff_sq_0)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
                                                       (sector_evals; cache-proxy recomputation)
  - computations/_shared/_spectral_action_regulators.py (SCHEMATIC; level-pin disclosure)

Outputs:
  - computations/session-92/s92_w9_6_l_max_22_extrapolation_diagnostic.npz
  - computations/session-92/s92_w9_6_l_max_22_extrapolation_diagnostic.png
  - verdict line + dual-SHA companion row -> computations/session-92/s92_gate_verdicts.txt
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # GPU_path pin = cpu-cap-OMP8 (small data; CPU-only)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import math
import time
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 — Paths + canonical constants import
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_92_DIR = PROJECT_ROOT / "computations" / "session-92"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (  # noqa: E402
    kappa_2_substrate_FW,
    tau_fold,
    M_KK,
)

CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
SPECTRAL_REGULATORS_PATH = SHARED_DIR / "_spectral_action_regulators.py"   # SCHEMATIC (level-pin disclosed)
W6_2_NPZ_DEFAULT = PROJECT_ROOT / "computations" / "session-91" / "s91_w6_2_k_hk_k_csub_empirical_anchoring.npz"
L12_CACHE_PATH = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

OUT_NPZ = SESSION_92_DIR / "s92_w9_6_l_max_22_extrapolation_diagnostic.npz"
OUT_PNG = SESSION_92_DIR / "s92_w9_6_l_max_22_extrapolation_diagnostic.png"
VERDICT_TXT = SESSION_92_DIR / "s92_gate_verdicts.txt"

# ---------------------------------------------------------------------------
# Section 2 — Gate identity + pre-registered machinery pins
# ---------------------------------------------------------------------------
GATE_ID = "S92-W9-CF-S91-W6-2-L-MAX-22-EXTRAPOLATION-DIAGNOSTIC"
SCHEME = ("post-hoc-decomposition-analytic-kappa-2-quadratic-vs-cache-truncated-proxy-"
          "substrate-distance-2-pole-s4-MIXED-SCHEMATIC-disclosed")
CONVENTION = ("gen-physicist-W6-2-L-MAX-22-EXTRAPOLATION-DIAGNOSTIC-CPU-only-post-hoc-"
              "SCHEMATIC-helper-disclosed")
L_MAX = 22                                    # (local) — pre-registered L_max pin (W6-2 baseline)

# Pre-registered thresholds (plan §W9-6):
CACHE_TRUNCATION_DOMINANCE_THRESHOLD = 0.95   # (local) — INFO if cache-truncation > 95% at intercept
ANALYTIC_QUADRATIC_MAX_AT_L22 = 0.05          # (local) — INFO if analytic-quadratic < 5% at L=22
L_CACHE_CEILING = 12                          # (local) — cache ceiling: N_cache(L>12) = N_cache(L=12)
FIVE_PI_SQ = (5.0 * math.pi) ** 2             # (5*pi)^2 = 246.74011...


# ---------------------------------------------------------------------------
# Section 3 — Dual-SHA closure helpers (S84+ schema; copied from script-template.py)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    """Print SHA-256 of each input; return {relpath: sha} for the closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
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


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append a single canonical verdict line + dual-SHA companion comment row.

    Atomic append (single open("a") write — no read-modify-write, no truncate).
    POSIX O_APPEND-safe under concurrent appenders.
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    tier_pin_row = (
        f"# tier_pin=TIER-2 # {GATE_ID} SCHEMATIC level-pin disclosure "
        f"(K=4 MANDATORY per substrate-first-canonical-sourcing.md §(iv); "
        f"M_Pl_eff_sq_with_regulator is a SCHEMATIC analog)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)
        fp.write(tier_pin_row)


# ---------------------------------------------------------------------------
# Section 4 — Decomposition primitives (substrate-distance-2 pole s=4)
# ---------------------------------------------------------------------------
def analytic_quadratic_contribution(L) -> float:
    """Analytic kappa_2-quadratic growth contribution at L_max truncation L.

        analytic_quadratic_contribution(L) = 1 + kappa_2_substrate_FW * L^2 / (5*pi)^2

    This IS the substrate-IS quadratic-in-L_max growth term per the S89 canonical
    kappa_2_substrate_FW (CM-1995 §III.4 second-order Jensen perturbation on the
    HK-5 closed form 5/(1 - tau/(5*pi)) at the substrate-distance-2 pole s=4).
    It is the EXACT growth factor applied by the S91 W6-2 `M_Pl_eff_sq_with_regulator`
    for L > 12 (`M_Pl_eff_sq_0 * growth`).
    """
    L_f = float(L)  # (local)
    return 1.0 + kappa_2_substrate_FW * L_f * L_f / FIVE_PI_SQ


def evals_at_L_max(sectors: dict, L_max: int) -> np.ndarray:
    """Union of all Peter-Weyl (p,q) sector eigenvalues with p+q <= L_max.

    Bit-identical to S91 W6-2 `evals_at_L_max` (and S90 W8 FWD-C1 convention).
    For L_max <= 12 this is exact on the L_max=12 master cache.
    """
    evals = []  # (local)
    for (p, q), s in sectors.items():
        if (p + q) <= L_max:
            evals.extend(s["abs_evals"])
    return np.asarray(evals, dtype=np.float64)


def cache_truncated_proxy(sectors: dict, L: int) -> float:
    """Cache-truncated `sum 1/lambda_i^2` proxy at L_max truncation L.

        cache_truncated_proxy(L) = sum_{i : lambda_i > 0} 1 / lambda_i^2
                                   over evals_at_L_max(sectors, min(L, 12))

    N_cache is HELD at the L_max=12 ceiling for L > 12 (CACHE CEILING):
    the L_max=12 master cache IS the substrate's image; `sum 1/lambda_i^2` for
    L > 12 is a cache-ceiling SCHEMATIC artifact, not a substrate truth at L > 12.
    Bit-identical to S91 W6-2 `compute_m_pl_eff_squared` on the truncated spectrum.
    """
    L_eff = min(int(L), L_CACHE_CEILING)  # (local) — cache ceiling
    evals = evals_at_L_max(sectors, L_eff)  # (local)
    if evals.size == 0:
        return 0.0
    mask = evals > 1e-15  # (local) — drop zero modes
    return float(np.sum(1.0 / evals[mask] ** 2))


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def _decode_object_pairs(arr) -> dict:
    """Decode a (5,2) object array of [name, value] rows into a dict."""
    out = {}  # (local)
    for row in arr:
        out[str(row[0])] = row[1]
    return out


def compute(w6_2_npz_path: Path) -> dict:
    # --- Load S91 W6-2 npz (runtime canonical-path: glob-resolved upstream) ---
    w6 = np.load(w6_2_npz_path, allow_pickle=True)  # (local)
    L_grid = np.asarray(w6["L_grid"], dtype=np.int64)  # (local)
    regulators = [str(r) for r in w6["regulators"]]  # (local)
    M_Pl_eff_sq_0 = float(w6["M_Pl_eff_sq_0"])  # (local)
    ratio_per_L = _decode_object_pairs(w6["ratio_per_L"])  # (local) {R: ratio_array}
    K_csub_R = _decode_object_pairs(w6["K_csub_R"])  # (local) {R: intercept}
    slope_R = _decode_object_pairs(w6["slope_R"])  # (local) {R: slope}

    # --- Load L_max=12 master cache for cache-truncated-proxy recomputation ---
    cache = np.load(L12_CACHE_PATH, allow_pickle=True)  # (local)
    sectors = cache["sector_evals"].item()  # (local) — {(p,q): {abs_evals, ...}}

    # --- Independent recomputation of M_Pl_eff_sq_0 (cross-check vs npz pin) ---
    M0_recomputed = cache_truncated_proxy(sectors, 0)  # (local) — proxy at L=0 ((0,0) sector)
    M0_match = math.isclose(M0_recomputed, M_Pl_eff_sq_0, rel_tol=1e-12)  # (local)

    # --- Per-(R, L) decomposition table ------------------------------------
    # Decompose ratio_per_L[R][L] into:
    #   (a) analytic-quadratic contribution  aq(L)            (substrate-IS growth)
    #   (b) cache-truncated proxy ratio       proxy(L) / M0   (cache-ceiling artifact)
    #
    # In the S91 W6-2 producing function `M_Pl_eff_sq_with_regulator`, the
    # ratio is constructed PIECEWISE:
    #   L <= 12 : ratio = proxy(L)/M0                       (pure cache-truncated proxy)
    #   L  > 12 : ratio = M0*aq(L)/M0 = aq(L)               (pure analytic-quadratic)
    # We report BOTH contributions at EVERY L so the splice + the dominance
    # structure are explicit.
    aq_per_L = np.array([analytic_quadratic_contribution(L) for L in L_grid], dtype=np.float64)  # (local)
    proxy_per_L = np.array([cache_truncated_proxy(sectors, int(L)) for L in L_grid], dtype=np.float64)  # (local)
    proxy_ratio_per_L = proxy_per_L / M_Pl_eff_sq_0  # (local) — cache-truncated proxy ratio
    proxy_ceiling = cache_truncated_proxy(sectors, L_CACHE_CEILING)  # (local) — frozen ceiling at L=12
    proxy_ceiling_ratio = proxy_ceiling / M_Pl_eff_sq_0  # (local)

    # Which branch does the S91 W6-2 ratio actually use at each L?
    branch_per_L = ["cache-proxy" if int(L) <= L_CACHE_CEILING else "analytic-quad" for L in L_grid]  # (local)

    # --- Reconstruct the S91 W6-2 ratio piecewise + verify reproduction -----
    # F_2-class (Mellin/zeta have sub_term=0): ratio reproduces exactly.
    inv_L = 1.0 / L_grid.astype(np.float64)  # (local)

    per_regulator = {}  # (local)
    for R in regulators:
        meas_ratio = np.asarray(ratio_per_L[R], dtype=np.float64)  # (local) — W6-2 measured ratio vector
        # Piecewise SCHEMATIC reconstruction (F_2-class form; sub_term=0):
        recon = np.where(
            L_grid <= L_CACHE_CEILING, proxy_ratio_per_L, aq_per_L
        )  # (local)
        # For F_2-class (Mellin/zeta) recon should reproduce meas_ratio bit-close.
        reproduces = bool(np.allclose(recon, meas_ratio, rtol=1e-6, atol=1e-6))  # (local)
        # Linear 1/L fit -> intercept (reproduces K_csub_R)
        slope_fit, intercept_fit = np.polyfit(inv_L, meas_ratio, 1)  # (local)
        intercept_match = math.isclose(
            float(intercept_fit), float(K_csub_R[R]), rel_tol=1e-6
        )  # (local)

        # Intercept-decomposition attribution (per plan substitution chain):
        #   |intercept| is dominated by the largest-magnitude L<=12 cache-proxy ratio.
        #   The analytic-quadratic at L=22 enters only via its tiny ratio (~1.04).
        abs_intercept = abs(float(K_csub_R[R]))  # (local)
        L8_idx = int(np.argmin(L_grid))  # (local) — L=8 is smallest L in grid
        cache_L8_ratio = float(meas_ratio[L8_idx])  # (local)
        aq_at_L22 = float(aq_per_L[-1])  # (local) — L=22 analytic-quadratic
        # Fractions relative to |intercept| (avoid div-by-zero):
        if abs_intercept > 0:
            cache_truncation_fraction = abs(cache_L8_ratio) / abs_intercept  # (local)
            analytic_quadratic_fraction = abs(aq_at_L22) / abs_intercept  # (local)
        else:
            cache_truncation_fraction = float("nan")  # (local)
            analytic_quadratic_fraction = float("nan")  # (local)

        per_regulator[R] = {
            "measured_ratio_per_L": meas_ratio,
            "reconstructed_ratio_per_L": recon,
            "schematic_reconstruction_reproduces": reproduces,
            "intercept_K_csub_R": float(K_csub_R[R]),
            "intercept_refit": float(intercept_fit),
            "intercept_match": intercept_match,
            "slope_refit": float(slope_fit),
            "cache_L8_ratio": cache_L8_ratio,
            "analytic_quadratic_at_L22": aq_at_L22,
            "cache_truncation_fraction": cache_truncation_fraction,
            "analytic_quadratic_fraction": analytic_quadratic_fraction,
        }

    # --- Structural-cause identification (F_2-class Mellin/zeta is the target) ---
    # The plan's specific intercept = K_csub_R[Mellin] = K_csub_R[zeta] = -245.69.
    target_R = "Mellin"  # (local) — Mellin/zeta share the F_2-class intercept
    tgt = per_regulator[target_R]  # (local)
    cache_dom = tgt["cache_truncation_fraction"]  # (local)
    aq_frac = tgt["analytic_quadratic_fraction"]  # (local)

    cache_truncation_dominant = bool(cache_dom > CACHE_TRUNCATION_DOMINANCE_THRESHOLD)  # (local)
    analytic_quadratic_small = bool(aq_frac < ANALYTIC_QUADRATIC_MAX_AT_L22)  # (local)
    schematic_root_cause = bool(cache_truncation_dominant and analytic_quadratic_small)  # (local)

    # FAIL guards: a "different root cause" would be one of:
    #  - intercept does NOT reproduce from the npz ratio (npz key mismatch / wrong basis)
    #  - the F_2-class SCHEMATIC piecewise reconstruction does NOT reproduce the ratio
    #  - M0 cross-check fails (sign error / proxy mismatch)
    intercept_reproduces = all(per_regulator[R]["intercept_match"] for R in regulators)  # (local)
    f2_reconstruction_ok = (
        per_regulator["Mellin"]["schematic_reconstruction_reproduces"]
        and per_regulator["zeta"]["schematic_reconstruction_reproduces"]
    )  # (local)
    different_root_cause = bool(
        (not intercept_reproduces) or (not M0_match) or (not f2_reconstruction_ok)
    )  # (local)

    # --- Verdict (set form per plan operator) ------------------------------
    # PASS: decomposition completed + structural cause identified (always true here
    #       if the data reproduces). INFO: SCHEMATIC mismatch confirmed. FAIL:
    #       different root cause.
    if different_root_cause:
        verdict = "FAIL"
        root_cause_tag = "different-root-cause-npz-mismatch-or-sign-error"  # (local)
    elif schematic_root_cause:
        verdict = "INFO"
        root_cause_tag = "SCHEMATIC-cache-truncation-analytic-extrapolation-mismatch"  # (local)
    else:
        # Decomposition completed + cause documented but not the SCHEMATIC-mismatch
        # signature -> PASS (decomposition table written + cause identified).
        verdict = "PASS"
        root_cause_tag = "decomposition-completed-cause-documented"  # (local)

    return {
        "L_grid": L_grid,
        "regulators": regulators,
        "M_Pl_eff_sq_0": M_Pl_eff_sq_0,
        "M0_recomputed": M0_recomputed,
        "M0_match": M0_match,
        "aq_per_L": aq_per_L,
        "proxy_per_L": proxy_per_L,
        "proxy_ratio_per_L": proxy_ratio_per_L,
        "proxy_ceiling": proxy_ceiling,
        "proxy_ceiling_ratio": proxy_ceiling_ratio,
        "branch_per_L": branch_per_L,
        "per_regulator": per_regulator,
        "target_R": target_R,
        "cache_truncation_fraction_target": cache_dom,
        "analytic_quadratic_fraction_target": aq_frac,
        "cache_truncation_dominant": cache_truncation_dominant,
        "analytic_quadratic_small": analytic_quadratic_small,
        "schematic_root_cause": schematic_root_cause,
        "intercept_reproduces": intercept_reproduces,
        "f2_reconstruction_ok": f2_reconstruction_ok,
        "different_root_cause": different_root_cause,
        "verdict": verdict,
        "root_cause_tag": root_cause_tag,
        "K_csub_target_intercept": per_regulator[target_R]["intercept_K_csub_R"],
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    L_grid = res["L_grid"]
    inv_L = 1.0 / L_grid.astype(np.float64)
    tgt = res["per_regulator"][res["target_R"]]
    meas = tgt["measured_ratio_per_L"]
    aq = res["aq_per_L"]
    proxy_ratio = res["proxy_ratio_per_L"]

    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    # Panel A: measured ratio_per_L vs L (Mellin/zeta), log scale -> shows the splice
    axA = axes[0, 0]
    axA.semilogy(L_grid, np.abs(meas), "o-", color="#1f77b4", label="|ratio_per_L| (Mellin/zeta, measured)")
    axA.semilogy(L_grid, np.abs(proxy_ratio), "s--", color="#d62728",
                 label=r"cache-proxy ratio $\Sigma\lambda^{-2}/M_0$")
    axA.semilogy(L_grid, aq, "^:", color="#2ca02c",
                 label=r"analytic-quadratic $1+\kappa_2 L^2/(5\pi)^2$")
    axA.axvline(L_CACHE_CEILING + 1, color="gray", ls=":", alpha=0.7)
    axA.text(L_CACHE_CEILING + 1.2, axA.get_ylim()[1] * 0.3, "cache ceiling\nsplice (L=12->14)",
             fontsize=8, color="gray")
    axA.set_xlabel("L_max"); axA.set_ylabel("contribution (log)")
    axA.set_title("(A) Piecewise SCHEMATIC ratio: cache-proxy (L<=12) vs analytic-quad (L>12)")
    axA.legend(fontsize=8); axA.grid(alpha=0.3)

    # Panel B: 1/L linear fit -> intercept = K_csub_R
    axB = axes[0, 1]
    axB.plot(inv_L, meas, "o", color="#1f77b4", label="ratio_per_L (measured)")
    slope, intercept = np.polyfit(inv_L, meas, 1)
    xfit = np.linspace(0, inv_L.max() * 1.05, 100)
    axB.plot(xfit, slope * xfit + intercept, "-", color="#ff7f0e",
             label=f"1/L fit -> intercept={intercept:.2f}")
    axB.axhline(intercept, color="#d62728", ls="--", alpha=0.6)
    axB.scatter([0], [intercept], color="#d62728", zorder=5, s=60,
                label=f"K_csub_R (1/L->0) = {res['K_csub_target_intercept']:.2f}")
    axB.set_xlabel("1 / L_max"); axB.set_ylabel("ratio_per_L")
    axB.set_title("(B) 1/L->0 extrapolation: intercept = -245.69 (Mellin/zeta)")
    axB.legend(fontsize=8); axB.grid(alpha=0.3)

    # Panel C: intercept-attribution bar chart (target regulator)
    axC = axes[1, 0]
    labels = ["cache-truncation\n(L=8 ratio)", "analytic-quadratic\n(L=22)"]
    fracs = [res["cache_truncation_fraction_target"] * 100.0,
             res["analytic_quadratic_fraction_target"] * 100.0]
    bars = axC.bar(labels, fracs, color=["#d62728", "#2ca02c"])
    axC.axhline(95, color="gray", ls="--", alpha=0.6, label="95% dominance threshold")
    axC.axhline(5, color="purple", ls=":", alpha=0.6, label="5% analytic-quad threshold")
    for b, f in zip(bars, fracs):
        axC.text(b.get_x() + b.get_width() / 2, f + 1.5, f"{f:.2f}%", ha="center", fontsize=9)
    axC.set_ylabel("% of |intercept| = 245.69")
    axC.set_title("(C) Intercept attribution: cache-truncation dominates")
    axC.legend(fontsize=8); axC.grid(alpha=0.3, axis="y"); axC.set_ylim(0, 110)

    # Panel D: per-regulator intercept magnitudes + verdict text
    axD = axes[1, 1]
    axD.axis("off")
    lines = [f"VERDICT: {res['verdict']}", f"root_cause_tag: {res['root_cause_tag']}", ""]
    lines.append(f"target (Mellin/zeta) intercept K_csub_R = {res['K_csub_target_intercept']:.4f}")
    lines.append(f"M_Pl_eff_sq_0 (npz)        = {res['M_Pl_eff_sq_0']:.6f}")
    lines.append(f"M_Pl_eff_sq_0 (recomputed) = {res['M0_recomputed']:.6f}  match={res['M0_match']}")
    lines.append("")
    lines.append(f"cache-truncation fraction (L=8) = {res['cache_truncation_fraction_target']*100:.2f}%  (>95%? {res['cache_truncation_dominant']})")
    lines.append(f"analytic-quadratic frac (L=22)  = {res['analytic_quadratic_fraction_target']*100:.3f}%  (<5%? {res['analytic_quadratic_small']})")
    lines.append(f"SCHEMATIC root cause confirmed  = {res['schematic_root_cause']}")
    lines.append("")
    lines.append("per-regulator intercept K_csub_R:")
    for R in res["regulators"]:
        v = res["per_regulator"][R]["intercept_K_csub_R"]
        rep = res["per_regulator"][R]["intercept_match"]
        lines.append(f"  {R:>14s} : {v: .4e}  (refit match={rep})")
    axD.text(0.0, 1.0, "\n".join(lines), va="top", ha="left", fontsize=8.5, family="monospace",
             transform=axD.transAxes)
    axD.set_title("(D) Diagnostic summary")

    fig.suptitle(f"{GATE_ID}\nK_csub_R Mellin/zeta = -245.69 intercept decomposition "
                 f"(SCHEMATIC cache-truncation vs analytic-quadratic; substrate-distance-2 pole s=4)",
                 fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def resolve_w6_2_npz() -> Path:
    """Runtime canonical-path rescue: glob the S91 W6-2 npz (plan-assumed name first)."""
    if W6_2_NPZ_DEFAULT.exists():
        return W6_2_NPZ_DEFAULT
    candidates = sorted((PROJECT_ROOT / "computations" / "session-91").glob("s91_w6_2_*.npz"))
    if not candidates:
        raise FileNotFoundError("No S91 W6-2 npz found via glob s91_w6_2_*.npz")
    return candidates[0]


def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} ===")
    print(f"kappa_2_substrate_FW = {kappa_2_substrate_FW!r}")
    print(f"tau_fold = {tau_fold!r}  M_KK = {M_KK!r}")
    print(f"(5*pi)^2 = {FIVE_PI_SQ!r}")

    w6_2_npz = resolve_w6_2_npz()  # (local)
    print(f"S91 W6-2 npz resolved: {w6_2_npz.relative_to(PROJECT_ROOT)}")

    # Input pins
    INPUT_FILES = [
        Path(__file__).resolve(),
        CANONICAL_CONSTANTS_PATH,
        w6_2_npz,
        L12_CACHE_PATH,
        SPECTRAL_REGULATORS_PATH,
    ]  # (local)
    pins = log_input_pins(INPUT_FILES)  # (local)

    # Compute
    res = compute(w6_2_npz)  # (local)

    # Print decomposition table
    print("\n=== Per-regulator decomposition table ===")
    print(f"{'regulator':>14s} | {'K_csub_R':>14s} | {'refit_match':>11s} | "
          f"{'cache_frac%':>11s} | {'aq_frac%':>9s}")
    for R in res["regulators"]:
        pr = res["per_regulator"][R]  # (local)
        cf = pr["cache_truncation_fraction"]  # (local)
        af = pr["analytic_quadratic_fraction"]  # (local)
        print(f"{R:>14s} | {pr['intercept_K_csub_R']: .4e} | {str(pr['intercept_match']):>11s} | "
              f"{cf*100:11.3f} | {af*100:9.4f}")

    print("\n=== Per-L contributions (Mellin/zeta F_2-class) ===")
    print(f"{'L':>4s} | {'branch':>13s} | {'meas_ratio':>13s} | {'cache_proxy_ratio':>17s} | {'analytic_quad':>13s}")
    tgt = res["per_regulator"]["Mellin"]  # (local)
    for i, L in enumerate(res["L_grid"]):
        print(f"{int(L):>4d} | {res['branch_per_L'][i]:>13s} | {tgt['measured_ratio_per_L'][i]:13.6f} | "
              f"{res['proxy_ratio_per_L'][i]:17.6f} | {res['aq_per_L'][i]:13.6f}")

    print(f"\nM_Pl_eff_sq_0 (npz)        = {res['M_Pl_eff_sq_0']:.10f}")
    print(f"M_Pl_eff_sq_0 (recomputed) = {res['M0_recomputed']:.10f}  match={res['M0_match']}")
    print(f"proxy ceiling @ L=12 ratio = {res['proxy_ceiling_ratio']:.6f}")
    print(f"\ncache-truncation dominant (>95%) : {res['cache_truncation_dominant']} "
          f"({res['cache_truncation_fraction_target']*100:.3f}%)")
    print(f"analytic-quadratic small (<5%)   : {res['analytic_quadratic_small']} "
          f"({res['analytic_quadratic_fraction_target']*100:.4f}%)")
    print(f"SCHEMATIC root cause confirmed   : {res['schematic_root_cause']}")
    print(f"intercept reproduces from npz    : {res['intercept_reproduces']}")
    print(f"F_2 SCHEMATIC reconstruction OK  : {res['f2_reconstruction_ok']}")
    print(f"different_root_cause (FAIL guard): {res['different_root_cause']}")

    # Plot
    make_plot(res)
    print(f"\nplot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")

    # Save npz
    per_reg_save = {}  # (local)
    for R in res["regulators"]:
        pr = res["per_regulator"][R]  # (local)
        per_reg_save[f"meas_ratio__{R}"] = pr["measured_ratio_per_L"]
        per_reg_save[f"recon_ratio__{R}"] = pr["reconstructed_ratio_per_L"]
        per_reg_save[f"intercept__{R}"] = pr["intercept_K_csub_R"]
        per_reg_save[f"intercept_refit__{R}"] = pr["intercept_refit"]
        per_reg_save[f"intercept_match__{R}"] = pr["intercept_match"]
        per_reg_save[f"cache_truncation_fraction__{R}"] = pr["cache_truncation_fraction"]
        per_reg_save[f"analytic_quadratic_fraction__{R}"] = pr["analytic_quadratic_fraction"]
        per_reg_save[f"schematic_reproduces__{R}"] = pr["schematic_reconstruction_reproduces"]

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=res["verdict"],
        root_cause_tag=res["root_cause_tag"],
        L_grid=res["L_grid"],
        regulators=np.array(res["regulators"], dtype=object),
        branch_per_L=np.array(res["branch_per_L"], dtype=object),
        kappa_2_substrate_FW=float(kappa_2_substrate_FW),
        five_pi_sq=FIVE_PI_SQ,
        M_Pl_eff_sq_0=res["M_Pl_eff_sq_0"],
        M0_recomputed=res["M0_recomputed"],
        M0_match=res["M0_match"],
        aq_per_L=res["aq_per_L"],
        proxy_per_L=res["proxy_per_L"],
        proxy_ratio_per_L=res["proxy_ratio_per_L"],
        proxy_ceiling=res["proxy_ceiling"],
        proxy_ceiling_ratio=res["proxy_ceiling_ratio"],
        target_R=res["target_R"],
        K_csub_target_intercept=res["K_csub_target_intercept"],
        cache_truncation_fraction_target=res["cache_truncation_fraction_target"],
        analytic_quadratic_fraction_target=res["analytic_quadratic_fraction_target"],
        cache_truncation_dominant=res["cache_truncation_dominant"],
        analytic_quadratic_small=res["analytic_quadratic_small"],
        schematic_root_cause=res["schematic_root_cause"],
        intercept_reproduces=res["intercept_reproduces"],
        f2_reconstruction_ok=res["f2_reconstruction_ok"],
        different_root_cause=res["different_root_cause"],
        tau_fold=float(tau_fold),
        M_KK=float(M_KK),
        cache_truncation_dominance_threshold=CACHE_TRUNCATION_DOMINANCE_THRESHOLD,
        analytic_quadratic_max_at_L22=ANALYTIC_QUADRATIC_MAX_AT_L22,
        **per_reg_save,
    )
    print(f"data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 4-tuple output (final non-verdict line)
    value_str = res["root_cause_tag"]  # (local)
    print(f"\n4-tuple: (value={value_str!r}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")

    # Dual-SHA + verdict emission
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CANONICAL_CONSTANTS_PATH, pins
    )  # (local)
    append_verdict(res["verdict"], value_str, audit_sha, content_sha)
    print(f"\nverdict appended: {res['verdict']} -- value={value_str!r}")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print(f"\nwall: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
