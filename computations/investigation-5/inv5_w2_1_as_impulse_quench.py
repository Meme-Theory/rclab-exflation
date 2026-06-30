#!/usr/bin/env python3
"""
INV5 W2-1 — A_s in the impulse-quench (sudden) limit: frozen Bogoliubov |beta_k|^2
normalized by the substrate-natural Kibble-Zurek correlation length xi_hat
=================================================================================

Gate: INV5-W2-1-AS-IMPULSE-QUENCH-BOGOLIUBOV ([SIGN])

Pre-registered hypothesis (plan §W2-1):
  In the impulse (sudden-quench) limit the scalar power A_s is set by the frozen
  Bogoliubov occupation |beta_k|^2 normalized by the saturated KZ correlation
  length xi_hat = xi_KZ_FW = 0.0187601 M_KK^-1 (NOT the slow-roll 1/eps_H prefactor
  times an additive decoherence budget), yielding ONE canonical amplitude OOM
  (replacing the 3.02/3.15/4.56/9.5-OOM self-disagreement) plus the frozen
  wavenumber k_hat = 1/xi_hat as the characteristic comoving scale.

Verdict (INFO-by-construction on magnitude; [SIGN] 3-tuple carries the verdict):
  - sign_verdict:      PASS iff A_s^impulse < A_s^slow-roll (the impulse normalization
                       REDUCES A_s vs the 1/eps_H slow-roll assembly).
  - magnitude_verdict: INFO-by-construction (the canonical OOM is the DELIVERABLE,
                       not a pre-set target; the OOM gap is the OUTPUT).
  - regime_verdict:    VALID iff the sudden/impulse limit holds (dt/T_L << 1) and the
                       frozen-occupation expansion is inside its window.

Substrate-natural construction (substitution chain, dimensional, NOT fit):
  Standard dimensionless power:    P_zeta(k) = (k^3 / 2pi^2) |zeta_k|^2,  [|zeta_k|^2] = k^-3.
  Impulse-quench source (del Campo & Zurek 1310.1600): the frozen field has a
  correlation length xi_hat; the curvature mode's spectral weight at the
  characteristic scale is the frozen occupation |beta_k|^2 spread over the KZ
  coherence VOLUME xi_hat^3:        |zeta_k|^2 = |beta_k|^2 * xi_hat^3   (N_norm = xi_hat^3).
  Therefore at the frozen mode k_hat = 1/xi_hat:
       A_s^raw = (k_hat^3 / 2pi^2) |beta_{k_hat}|^2 xi_hat^3 = |beta_{k_hat}|^2 / (2pi^2),
  since k_hat^3 xi_hat^3 = 1. N_norm = xi_hat^3 is a SUBSTRATE-NATURAL quantity
  (the KZ coherence volume), NOT a tuned normalization.

|beta_k|^2 source: the S100b box-delta sudden-limit Bogoliubov spectrum
  (s100b_box_delta_bogoliubov.npz; scheme BOX-DELTA-SUDDEN; 3-code-path PASS to 1.4e-13;
  unitarity residual 1.9e-14). beta2_spectrum(k) over k_grid in [1,50]; evaluated at
  k_hat = 53.30 by power-law UV-tail extrapolation (the UV tail is near-flat:
  log-log slope ~ -0.003 => |beta_k|^2 nearly scale-invariant in the impulse regime,
  the substrate signature of the sudden limit).

SOURCE-RECON (MANDATORY for this gate, plan machinery_pin_map):
  xi_hat = canonical_constants.xi_KZ_FW = 0.0187601 M_KK^-1 (S89, substrate-natural
  impulse-regime). The survey/seed "0.808 M_KK^-1 saturated sudden-quench floor" is the
  S53 xi_BCS-ANALOG (an INPUT to the xi_KZ_FW derivation), NOT the impulse xi_hat;
  consuming 0.808 as xi_hat is the Class-(f) PIN-PLACEHOLDER pathology
  (D_max = |log10(0.808) - log10(0.0187601)| = 1.634 => SOURCE-RECON HARD-HALT band).
  This script PINS xi_KZ_FW and reports 0.808346 (xi_BCS) ONLY as a cross-check anchor.
  A_s_Planck = canonical_constants.A_s_Planck = 2.1e-9 (observational OOM-gap denominator).

Classification: PHONONIC (A_s IS the spectral-weight content of the frozen Bogoliubov
occupation -- the GGE relic of the supersonic transit, read off the cached |beta_k|^2).

DISCIPLINE: from canonical_constants import *; intermediates tagged # (local);
numpy.linalg vector reduction (no >=100x100 dense diag -- |beta_k|^2 read from cache);
dual-SHA (audit over [script,canonical,pinmap], content over [script]); verdict via
print_verdict_payload -> agent calls mcp__knowledge__emit_verdict (race-safe).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU-fallback thread cap (vector reduction)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403  (xi_KZ_FW, A_s_Planck, n_pairs, P_exc_kz, M_KK, PI, xi_BCS, ...)

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
SESSION = "5"                                                       # (local) investigation number
GATE_ID = "INV5-W2-1-AS-IMPULSE-QUENCH-BOGOLIUBOV"                 # (local)
SCHEME = "IMPULSE-QUENCH-BOGOLIUBOV"                                # (local)
CONVENTION = "FROZEN-OCCUPATION-NORMALIZED-BY-SUBSTRATE-NATURAL-XI-KZ"  # (local)
L_MAX = 10                                                         # (local)

OUT_NPZ = SESSION_DIR / "inv5_w2_1_as_impulse_quench.npz"
OUT_PNG = SESSION_DIR / "inv5_w2_1_as_impulse_quench.png"

# Substrate |beta_k|^2 cache (S100b box-delta sudden-limit Bogoliubov spectrum; PASS).
BETA2_CACHE = COMPUTATIONS_DIR / "session-100b" / "s100b_box_delta_bogoliubov.npz"
# Sector-resolved n_pairs aggregate cross-check (atlas T4 branch structure B1/B2/B3).
NPAIR_CACHE = COMPUTATIONS_DIR / "session-48" / "s48_npair_full.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    BETA2_CACHE,
    NPAIR_CACHE,
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
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    """Frozen-occupation A_s in the impulse-quench limit + frozen wavenumber k_hat."""
    # --- Substrate-natural KZ scale (PINNED; SOURCE-RECON: NOT the 0.808 xi_BCS-analog) ---
    xi_hat = float(xi_KZ_FW)               # (local) = 0.0187601 M_KK^-1 (S89 substrate-natural)
    k_hat = 1.0 / xi_hat                   # (local) frozen comoving wavenumber (M_KK)
    xi_bcs_anchor = float(xi_BCS)          # (local) 0.808346 M_KK^-1 — CROSS-CHECK ANCHOR ONLY
    D_max_xi = abs(math.log10(xi_bcs_anchor) - math.log10(xi_hat))  # (local) = 1.634 (HARD-HALT band)

    # --- Frozen Bogoliubov |beta_k|^2 spectrum (S100b box-delta sudden limit; PASS) ---
    bd = np.load(BETA2_CACHE, allow_pickle=True)  # (local)
    k_grid = np.asarray(bd["k_grid"], dtype=float)          # (local)
    beta2_spectrum = np.asarray(bd["beta2_spectrum"], dtype=float)  # (local)
    k_pivot = float(bd["k_pivot"])          # (local) = 14.311 M_KK (CMB pivot, fold norm)
    beta2_pivot = float(bd["beta2_pivot_closed_form"])      # (local) |beta_pivot|^2 cross-check

    # --- |beta_{k_hat}|^2 at the frozen scale (UV-tail power-law extrapolation) ---
    # The box-delta cache covers k in [1, 50]; k_hat = 53.30 sits just past the edge
    # (k_hat/kmax = 1.066). The UV tail is near-FLAT (log-log slope ~ -0.003 => the
    # impulse-limit occupation is nearly scale-invariant), so the extrapolation to k_hat
    # is essentially the plateau value and is insensitive to the exact eval point.
    mask_uv = k_grid > 10.0                 # (local) UV regime for the tail fit
    log_k = np.log(k_grid[mask_uv])         # (local)
    log_b2 = np.log(beta2_spectrum[mask_uv])  # (local)
    uv_slope, uv_intercept = np.polyfit(log_k, log_b2, 1)  # (local) log-log linear fit
    beta2_khat = math.exp(uv_slope * math.log(k_hat) + uv_intercept)  # (local) |beta_{k_hat}|^2

    # --- Substrate-natural A_s construction ---
    # A_s^raw = (k_hat^3 / 2pi^2) * |beta_{k_hat}|^2 * N_norm,  N_norm = xi_hat^3 (KZ vol)
    #         = |beta_{k_hat}|^2 / (2pi^2)   since k_hat^3 * xi_hat^3 = 1.
    N_norm = xi_hat ** 3                     # (local) KZ coherence VOLUME (substrate-natural)
    khat3 = k_hat ** 3                       # (local) dimensional phase factor
    assert abs(khat3 * N_norm - 1.0) < 1e-9, "k_hat^3 * xi_hat^3 must equal 1"
    A_s_raw = N_norm * beta2_khat * khat3 / (2.0 * PI ** 2)  # (local) == beta2_khat/(2pi^2)
    OOM_gap = math.log10(A_s_raw / float(A_s_Planck))        # (local) canonical OOM (deliverable)

    # --- Frozen scale vs CMB pivot (deg(T_{BZ->pivot}) target ratio, G-3) ---
    khat_over_kpivot = k_hat / k_pivot       # (local) = 3.725 (frozen scale ABOVE the pivot)

    # --- SIGN sub-test: A_s^impulse vs A_s^slow-roll (the object being REPLACED) ---
    # Slow-roll UNIFIED-AS-79 five-factor assembly (Branch-A; MEMORY canonical pins):
    #   A_s^slow-roll = P_pref * (1/eps_H) * F_amp * (1/c_sub) * f_conv.
    H_tilde_sr = 5.9076e-3                   # (local) Branch-A microscopic TD anchor (S82)
    eps_H_sr = 0.02163                       # (local) slow-roll parameter (<< 1)
    F_amp_sr = 47.92                         # (local) 3PI backreaction amplification (S82)
    c_sub_sr = 2.238                         # (local) Mellin-weight kinematic divisor (S79)
    f_conv_sr = 9.30e-4                      # (local) single KK hierarchy conversion
    P_pref_sr = H_tilde_sr ** 2 / (8.0 * PI ** 2)  # (local) slow-roll prefactor
    A_s_slowroll = P_pref_sr * (1.0 / eps_H_sr) * F_amp_sr * (1.0 / c_sub_sr) * f_conv_sr  # (local)
    A_s_slowroll_raw = P_pref_sr * (1.0 / eps_H_sr)  # (local) UNTAMED slow-roll (P_pref/eps_H)
    ratio_imp_sr = A_s_raw / A_s_slowroll    # (local) SIGN-test ratio
    ratio_imp_sr_raw = A_s_raw / A_s_slowroll_raw  # (local) vs untamed
    inv_eps_H = 1.0 / eps_H_sr               # (local) the slow-roll-specific LARGE factor

    # --- aggregate cross-checks (atlas T4 sector structure) ---
    sum_beta2 = float(beta2_spectrum.sum())  # (local) bare 64-mode box-delta sum
    np48 = np.load(NPAIR_CACHE, allow_pickle=True)  # (local)
    branch_labels = [str(x) for x in np48["branch_labels"]]  # (local)
    rho_8 = np.asarray(np48["rho_8"], dtype=float)           # (local) per-mode DOS (B2 van Hove)
    n_pairs_aggregate = float(n_pairs)       # (local) canonical 59.8 aggregate
    P_exc = float(P_exc_kz)                  # (local) 1.000 (KZ saturation)
    # Alternative-construction OOM probes (reported for transparency; NOT the deliverable):
    OOM_npairs = math.log10((n_pairs_aggregate / (2.0 * PI ** 2)) / float(A_s_Planck))  # (local)
    OOM_sumbeta2 = math.log10((sum_beta2 / (2.0 * PI ** 2)) / float(A_s_Planck))        # (local)

    # --- regime check: impulse/sudden validity (atlas T1) ---
    dt_over_TL = 1.25e-5                      # (local) sudden-quench diabaticity (atlas T1 PROVEN)
    regime_valid = (dt_over_TL < 1.0) and (abs(uv_slope) < 0.5)  # (local) impulse + tail-flatness

    # --- verdicts ---
    sign_verdict = "PASS" if A_s_raw < A_s_slowroll else "FAIL"   # (local)
    magnitude_verdict = "INFO"   # (local) INFO-by-construction: the OOM is the DELIVERABLE
    regime_verdict = "VALID" if regime_valid else "BREAKDOWN"     # (local)
    # composite collapse (gate-verdicts.md): regime VALID, sign PASS, magnitude INFO -> INFO
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"       # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"       # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"       # (local)
    else:
        composite = "PASS"       # (local)

    return {
        "value": A_s_raw,
        "xi_hat": xi_hat, "k_hat": k_hat, "xi_bcs_anchor": xi_bcs_anchor, "D_max_xi": D_max_xi,
        "beta2_khat": beta2_khat, "beta2_pivot": beta2_pivot, "uv_slope": uv_slope,
        "uv_intercept": uv_intercept, "N_norm": N_norm, "A_s_raw": A_s_raw, "OOM_gap": OOM_gap,
        "k_pivot": k_pivot, "khat_over_kpivot": khat_over_kpivot,
        "A_s_slowroll": A_s_slowroll, "A_s_slowroll_raw": A_s_slowroll_raw,
        "ratio_imp_sr": ratio_imp_sr, "ratio_imp_sr_raw": ratio_imp_sr_raw, "inv_eps_H": inv_eps_H,
        "sum_beta2": sum_beta2, "n_pairs_aggregate": n_pairs_aggregate, "P_exc": P_exc,
        "OOM_npairs": OOM_npairs, "OOM_sumbeta2": OOM_sumbeta2, "dt_over_TL": dt_over_TL,
        "k_grid": k_grid, "beta2_spectrum": beta2_spectrum, "branch_labels": branch_labels,
        "rho_8": rho_8,
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict, "composite": composite,
    }


def make_plot(r: dict) -> None:
    fig, ax = plt.subplots(1, 2, figsize=(13, 5.0))
    # (a) frozen Bogoliubov spectrum |beta_k|^2 with k_hat, k_pivot marked
    ax[0].loglog(r["k_grid"], r["beta2_spectrum"], "o-", ms=3, color="#1f77b4",
                 label=r"$|\beta_k|^2$ (S100b box-delta, sudden)")
    ax[0].axvline(r["k_hat"], color="crimson", ls="--",
                  label=r"$\hat{k}=1/\hat{\xi}=%.2f\,M_{KK}$" % r["k_hat"])
    ax[0].axvline(r["k_pivot"], color="green", ls=":",
                  label=r"$k_{\rm pivot}=%.2f\,M_{KK}$" % r["k_pivot"])
    ax[0].axhline(r["beta2_khat"], color="grey", ls="-.", lw=0.8,
                  label=r"$|\beta_{\hat k}|^2=%.3e$" % r["beta2_khat"])
    ax[0].set_xlabel(r"$k\ (M_{KK})$")
    ax[0].set_ylabel(r"$|\beta_k|^2$")
    ax[0].set_title("Frozen Bogoliubov occupation (UV near-flat: slope %.4f)" % r["uv_slope"])
    ax[0].legend(fontsize=7, loc="lower left")
    ax[0].grid(alpha=0.3, which="both")

    # (b) OOM ladder: impulse vs slow-roll routes vs Planck
    labels = ["impulse\n(this gate)", "slow-roll\nledger\n(AS-79)", "slow-roll\nRAW\n(P/eps_H)",
              "n_pairs\nnaive", "sum|b|^2\nnaive"]  # (local)
    ooms = [r["OOM_gap"], math.log10(r["A_s_slowroll"] / float(A_s_Planck)),
            math.log10(r["A_s_slowroll_raw"] / float(A_s_Planck)),
            r["OOM_npairs"], r["OOM_sumbeta2"]]  # (local)
    colors = ["crimson", "#ff7f0e", "#d62728", "grey", "grey"]  # (local)
    bars = ax[1].bar(labels, ooms, color=colors, alpha=0.85)
    ax[1].axhline(0.0, color="black", lw=1.0, label=r"Planck $A_s=2.1\times10^{-9}$")
    ax[1].axhline(1.0, color="green", ls=":", lw=0.8, label="+1 OOM band")
    for b, v in zip(bars, ooms):
        ax[1].text(b.get_x() + b.get_width() / 2, v + (0.15 if v >= 0 else -0.3),
                   "%.2f" % v, ha="center", fontsize=8)
    ax[1].set_ylabel(r"$\log_{10}(A_s / A_s^{\rm Planck})$ (OOM gap)")
    ax[1].set_title("A_s OOM: impulse normalization collapses the 9.5-OOM wall to +%.2f" % r["OOM_gap"])
    ax[1].legend(fontsize=7)
    ax[1].grid(alpha=0.3, axis="y")
    fig.suptitle("INV5-W2-1 — A_s impulse-quench Bogoliubov |beta_k|^2 / xi_hat  "
                 r"(SIGN: impulse/slow-roll = %.4f < 1)" % r["ratio_imp_sr"], fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
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
        "track": "investigation",
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
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()           # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()

    # --- report ---
    print("=== SUBSTRATE-NATURAL CONSTRUCTION ===")
    print(f"  xi_hat (xi_KZ_FW, PINNED)     = {r['xi_hat']:.10g} M_KK^-1   [S89 substrate-natural]")
    print(f"  xi_BCS anchor (CROSS-CHECK)   = {r['xi_bcs_anchor']:.10g} M_KK^-1  "
          f"[D_max={r['D_max_xi']:.4f} => HARD-HALT band if used as xi_hat; NOT used]")
    print(f"  k_hat = 1/xi_hat              = {r['k_hat']:.6f} M_KK")
    print(f"  |beta_{{k_hat}}|^2 (UV-tail)    = {r['beta2_khat']:.6e}  (slope={r['uv_slope']:.4f}, near-flat)")
    print(f"  N_norm = xi_hat^3 (KZ vol)    = {r['N_norm']:.6e}")
    print(f"  A_s^raw = |beta_khat|^2/2pi^2 = {r['A_s_raw']:.6e}")
    print(f"  OOM_gap = log10(A_s/A_s_Pl)   = {r['OOM_gap']:.4f}   <<< CANONICAL DELIVERABLE")
    print(f"  k_hat / k_pivot               = {r['khat_over_kpivot']:.4f}  (deg(T_BZ->pivot) target ratio)")
    print()
    print("=== SIGN SUB-TEST (impulse vs slow-roll) ===")
    print(f"  A_s^slow-roll (AS-79 ledger)  = {r['A_s_slowroll']:.6e}  (carries 1/eps_H={r['inv_eps_H']:.3f})")
    print(f"  A_s^slow-roll RAW (P/eps_H)   = {r['A_s_slowroll_raw']:.6e}")
    print(f"  ratio impulse/slow-roll       = {r['ratio_imp_sr']:.6f}  => impulse<slow-roll: {r['A_s_raw']<r['A_s_slowroll']}")
    print(f"  ratio impulse/RAW-slow-roll   = {r['ratio_imp_sr_raw']:.4e}")
    print()
    print("=== CROSS-CHECK / ALTERNATIVE CONSTRUCTIONS (NOT the deliverable) ===")
    print(f"  Sum|beta_k|^2 (64-mode bare)  = {r['sum_beta2']:.6e}  -> OOM {r['OOM_sumbeta2']:.4f}")
    print(f"  n_pairs aggregate (atlas T4)  = {r['n_pairs_aggregate']:.4g}  -> OOM {r['OOM_npairs']:.4f} (matches 9.5-OOM wall)")
    print(f"  P_exc (KZ saturation)         = {r['P_exc']:.4g}")
    print(f"  branch sectors                = {r['branch_labels']}")
    print(f"  regime: dt/T_L={r['dt_over_TL']:.2e} (sudden), tail-flat -> regime_valid={r['regime_verdict']}")
    print()
    print(f"=== 3-TUPLE: sign={r['sign_verdict']} magnitude={r['magnitude_verdict']} "
          f"regime={r['regime_verdict']} => composite {r['composite']} ===")

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        A_s_raw=r["A_s_raw"], OOM_gap=r["OOM_gap"],
        xi_hat=r["xi_hat"], k_hat=r["k_hat"], N_norm=r["N_norm"],
        xi_BCS_cross_check_anchor=r["xi_bcs_anchor"], D_max_xi_bcs_vs_xi_kz=r["D_max_xi"],
        beta2_khat=r["beta2_khat"], beta2_pivot=r["beta2_pivot"],
        uv_slope=r["uv_slope"], uv_intercept=r["uv_intercept"],
        k_pivot=r["k_pivot"], khat_over_kpivot=r["khat_over_kpivot"],
        A_s_slowroll_ledger=r["A_s_slowroll"], A_s_slowroll_raw=r["A_s_slowroll_raw"],
        ratio_impulse_over_slowroll=r["ratio_imp_sr"],
        ratio_impulse_over_slowroll_raw=r["ratio_imp_sr_raw"], inv_eps_H=r["inv_eps_H"],
        sum_beta2_bare=r["sum_beta2"], n_pairs_aggregate=r["n_pairs_aggregate"], P_exc=r["P_exc"],
        OOM_npairs_naive=r["OOM_npairs"], OOM_sumbeta2_naive=r["OOM_sumbeta2"],
        dt_over_TL=r["dt_over_TL"], A_s_Planck=float(A_s_Planck),
        k_grid=r["k_grid"], beta2_spectrum=r["beta2_spectrum"],
        branch_labels=np.array(r["branch_labels"]), rho_8=r["rho_8"],
        sign_verdict=r["sign_verdict"], magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"], composite=r["composite"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    make_plot(r)
    print(f"  wrote {OUT_NPZ.name}")
    print(f"  wrote {OUT_PNG.name}")

    value_payload = (f"A_s_impulse={r['A_s_raw']:.4e};OOM_gap={r['OOM_gap']:.4f};"
                     f"k_hat={r['k_hat']:.4f}_M_KK;khat/kpivot={r['khat_over_kpivot']:.4f};"
                     f"ratio_imp/SR={r['ratio_imp_sr']:.4f}")  # (local) no single-quote chars
    print(emit_4tuple(value_payload, SCHEME, CONVENTION, L_MAX))
    print_verdict_payload(
        r["composite"], value_payload, audit_sha, content_sha,
        sign_verdict=r["sign_verdict"], magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"],
        companion_note="A_s=|beta_khat|^2/2pi^2, N_norm=xi_KZ_FW^3 (KZ coh.vol); xi_BCS=0.808 cross-check only (D_max=1.63)",
        extra_rows=[
            f"# regulator_pin=IMPULSE-QUENCH-BOGOLIUBOV xi_KZ_FW=0.018760 (S89 substrate-natural); "
            f"OOM_gap=+{r['OOM_gap']:.4f} replaces 3.02/3.15/4.56/9.5-OOM self-disagreement; "
            f"k_hat=1/xi_hat={r['k_hat']:.4f} M_KK (G-3 deg(T_BZ->pivot) scale)",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {r['composite']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
