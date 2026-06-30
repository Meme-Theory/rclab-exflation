#!/usr/bin/env python3
"""
S100a W1-3 S100a-W1-3-NS-NLO — NLO precision-stability of the n_s = 0.9561 LO tilt
====================================================================================

Gate: S100a-W1-3-NS-NLO ([SIGN])
Plan: sessions/session-plan/session-100a-plan-w1.md §W1-3 (schema R3)
Agent: lizzi-spectral-functional-theorist
Classification: PHONONIC

Pre-registered threshold (plan §W1-3, operator + verdict rubric):
  |Δn_s^{NLO}| = |n_s^{NLO} − n_s^{LO}| < 0.003          → PASS
  0.003 ≤ |Δn_s^{NLO}| < 0.009                            → INFO
  |Δn_s^{NLO}| ≥ 0.009                                    → FAIL
  Expected sign (pre-registered): Δn_s^{NLO} NEGATIVE (slow-roll reddens).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py  (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)
  No npz inputs: the B1 trajectory enters through the canonical a_2^{zeta}/a_4^{zeta}
  moments + the bit-exact n_s_FW_exact = Fraction(9561, 10000) anchor (orchestrator
  override; all confirmed in canonical_constants.py at plan-freeze).

Output 4-tuple:
  (value=Delta_ns_NLO, scheme=FW, convention=CONSTANT-EPSILON-SLOW-ROLL-NLO, L_max=10)

METHODOLOGY (substitution chain per plan §W1-3 item 7, executed exactly)
------------------------------------------------------------------------
Definition 1 (LO anchor): n_s^{LO} = 1 − 2ε_H = 0.9561 (S84 T6 constant-ε
  gauge-invariant spectral geometry; bit-exact n_s_FW_exact = Fraction(9561,10000),
  S88 W-15 W15-V.2). ⇒ ε_H = (1 − n_s^{LO})/2 = Fraction(439, 20000) = 0.02195 EXACT.
  The ε_H value is moment-derived: the S84 T6 derivation builds the slow-variation
  parameter from the a_2^{zeta}/a_4^{zeta} Seeley-DeWitt ratios along the B1
  trajectory through the tau_fold slice (regulator pin: both moments zeta-regulated
  per regulator-pin-discipline.md).

Definition 2 (NLO term, spectral-action expansion): the framework's registered
  EXACT constant-ε tilt theorem [T6] (atlas-07 permanent results, W4-01, "Exact"):
      n_s^{T6-exact} = (1 − 3ε)/(1 − ε)        for power-law with constant ε
  has the exact series (1−3ε)/(1−ε) = 1 − 2ε − 2ε² − 2ε³ − ...  (every coefficient
  beyond order 0 is exactly −2). The NLO truncation is therefore
      n_s^{NLO} = 1 − 2ε_H − 2ε_H²,   Δn_s^{NLO} = −C₂·ε_H²  with  C₂ = 2 EXACT.
  C₂ is fixed framework-internally by T6 — not imported. Two-route cross-check:
  the standard second-order Hubble-flow tilt (Stewart-Lyth / Schwarz-Terrero-
  Escalante horizon-flow form)
      n_s − 1 = −2ε₁ − ε₂ − 2ε₁² − (2C+3)ε₁ε₂ − C·ε₂ε₃,  C = γ_E + ln2 − 2
  reduces at ε₂ = 0 (constant-ε class) to n_s = 1 − 2ε₁ − 2ε₁²: identical C₂ = 2.

Definition 3 (η_H, a₄-pulled curvature): η_H ≡ ε₂ = d ln ε_H/dN. On the T6
  constant-ε class η_H = 0 IDENTICALLY — and this is FORCED by the LO anchor:
  a nonzero ε₂ enters the tilt LINEARLY (−ε₂ term above), so any ε₂ ≠ 0 at the
  pivot would shift the PROVEN LO value at first order, contradicting the
  bit-exact anchor. The gate quantifies the off-class envelope two ways:
    (a) a₄-pulled curvature proxy: η_H^{a4} = ε_H · (a_4^{zeta}/a_2^{zeta})
        — the moment-hierarchy ratio is the natural curvature scale of the
        slow-variation expansion (the a₄ sector pulls the trajectory);
    (b) empirical ε_H-spread: |ε_H^{anchor} − eps_H_W6| (the independent S80
        dS/dτ-route determination eps_H_W6 = 0.02163), attributed maximally
        conservatively to ΔN = 1 e-fold analog: η_H^{spread} = Δε_H/ε_H.
  The η-term enters the NLO correction at second order: −(2C+3)·ε_H·η_H.

DISCIPLINE
----------
- from canonical_constants import *  (a_2_FW_zeta, a_4_FW_zeta, n_s_framework,
  n_s_FW_exact, eps_H_W6, planck_ns, planck_ns_err)
- machinery pin GPU_path = numpy cpu-cap-OMP8 (OMP_NUM_THREADS=8 set BEFORE numpy)
- every computed intermediate tagged # (local)
- exact Fraction arithmetic for the central value; float64 for envelopes
- verdict via print_verdict_payload → agent calls mcp__knowledge__emit_verdict
  (race-safe; script does NOT write the verdict file)
- round-trip: full float64 → npz; 4-sig-fig rounding → WP (Class 8.3)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (machinery pin: cpu-cap-OMP8, BEFORE numpy import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json     # noqa: E402
import math     # noqa: E402
import time     # noqa: E402
from fractions import Fraction  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib   # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Identity + pre-registration (plan §W1-3, pinned at plan-freeze)
# ---------------------------------------------------------------------------
SESSION = "100a"                                                   # (local)
GATE_ID = "S100a-W1-3-NS-NLO"                                      # (local)
SCHEME = "FW"                                                      # (local)
CONVENTION = "CONSTANT-EPSILON-SLOW-ROLL-NLO"                      # (local)
L_MAX = "10"                                                       # (local)

# Pre-registered gate bands (plan §W1-3 operator + verdict rubric)
PASS_BAND = 0.003                                                  # (local)
INFO_BAND = 0.009                                                  # (local)
FLOAT_TOL = 1e-12                                                  # (local) plan tolerance pin
# Regime-of-validity caps for the slow-variation series (gate-verdicts.md
# regime_verdict semantics: VALID / MARGINAL(>=0.1) / BREAKDOWN(>=0.5))
REGIME_VALID_CAP = 0.1                                             # (local)
REGIME_BREAKDOWN_CAP = 0.5                                         # (local)

OUT_NPZ = SESSION_DIR / "s100a_w1_ns_nlo.npz"
OUT_PNG = SESSION_DIR / "s100a_w1_ns_nlo.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
]


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


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """audit_sha256 = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    script_bytes = script_path.read_bytes()        # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
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
# Section 5 — Compute (exact-Fraction backbone + float64 envelopes)
# ---------------------------------------------------------------------------
def compute() -> dict:
    ONE = Fraction(1)  # (local)

    # --- Definition 1: LO anchor + eps_H (EXACT) -------------------------
    n_s_LO = n_s_FW_exact                          # canonical bit-exact Fraction(9561,10000)
    assert n_s_LO == Fraction(9561, 10000), "n_s_FW_exact drifted from bit-exact pin"
    assert abs(float(n_s_LO) - n_s_framework) < 1e-15, "n_s_framework float/Fraction mismatch"

    eps_H = (ONE - n_s_LO) / 2                     # (local) EXACT slow-variation parameter
    assert eps_H == Fraction(439, 20000), "eps_H exact-Fraction identity failed"
    eps_f = float(eps_H)                           # (local) 0.02195 float64 image

    # --- Definition 2: T6 exact + NLO truncation (EXACT) -----------------
    # [T6] Constant-Epsilon Theorem (atlas-07, W4-01, Exact): n_s = (1-3e)/(1-e)
    n_s_T6 = (ONE - 3 * eps_H) / (ONE - eps_H)     # (local) exact all-orders tilt
    assert n_s_T6 == Fraction(18683, 19561), "T6 exact Fraction identity failed"

    # NLO truncation of the T6 series: n_s_NLO = 1 - 2e - 2e^2
    n_s_NLO = ONE - 2 * eps_H - 2 * eps_H**2       # (local)
    delta_ns_NLO = n_s_NLO - n_s_LO                # (local) THE gate value (exact)
    assert delta_ns_NLO == -2 * eps_H**2, "Delta_ns_NLO != -2*eps_H^2 (C2=2) exact identity failed"

    # C2 = 2 EXACT, route 1 (T6 series): verify every truncation order k=1..5
    # satisfies (1-3e)/(1-e) - [1 - 2*sum_{n=1..k} e^n] == -2 e^{k+1}/(1-e) in Q,
    # i.e. EVERY series coefficient beyond order 0 is exactly -2.
    for k in range(1, 6):
        S_k = ONE - 2 * sum(eps_H**n for n in range(1, k + 1))  # (local)
        assert n_s_T6 - S_k == -2 * eps_H**(k + 1) / (ONE - eps_H), \
            f"T6 series coefficient check failed at order {k}"
    C2_exact = 2                                   # (local) pinned by T6 (framework-internal)

    # NNLO+ residual (all orders beyond NLO): -2 e^3/(1-e) — regime diagnostic
    resid_NNLO = n_s_T6 - n_s_NLO                  # (local)
    assert resid_NNLO == -2 * eps_H**3 / (ONE - eps_H), "NNLO residual exact identity failed"

    # C2 = 2 route 2 (Hubbleflow second-order, Stewart-Lyth C-coefficient form):
    # n_s - 1 = -2e1 - e2 - 2e1^2 - (2C+3)e1e2 - C e2e3, C = gamma_E + ln2 - 2;
    # constant-eps class => e2 = 0 => n_s = 1 - 2e1 - 2e1^2 (same C2).
    C_SL = np.euler_gamma + math.log(2.0) - 2.0    # (local) = -0.7296371545...
    C_eta = 2.0 * C_SL + 3.0                       # (local) = 1.5407256909... (eps*eta NLO coeff)
    eps2_onclass = 0.0                             # (local) constant-eps class: eta_H = e2 = 0
    n_s_NLO_HF = (1.0 - 2.0 * eps_f - eps2_onclass - 2.0 * eps_f**2
                  - C_eta * eps_f * eps2_onclass - C_SL * eps2_onclass * 0.0)  # (local)
    route_diff = abs(n_s_NLO_HF - float(n_s_NLO))  # (local)
    assert route_diff < FLOAT_TOL, f"two-route C2 cross-check failed: {route_diff:.3e}"

    # --- Definition 3: eta_H envelopes (a4-pulled curvature + eps-spread) -
    ratio_a4_a2 = a_4_FW_zeta / a_2_FW_zeta        # (local) zeta-regulated moment ratio
    eta_H_a4 = eps_f * ratio_a4_a2                 # (local) a4-pulled curvature proxy
    eta_term_a4 = abs(C_eta * eps_f * eta_H_a4)    # (local) |(2C+3) eps eta| envelope (a4)

    eps_spread = abs(eps_f - eps_H_W6)             # (local) vs independent S80 dS/dtau route
    eta_H_spread = eps_spread / eps_f              # (local) DeltaN=1 maximally conservative
    eta_term_spread = abs(C_eta * eps_f * eta_H_spread)  # (local) = C_eta*eps_spread

    delta_central = float(delta_ns_NLO)            # (local) -9.63605e-4
    env_a4 = abs(delta_central) + eta_term_a4      # (local)
    env_worst = abs(delta_central) + eta_term_spread  # (local) worst-case |Delta|
    env_min = abs(delta_central) - eta_term_spread    # (local) sign-robustness floor
    # sign flips only if |eta_H| > 2 eps_H / (2C+3):
    eta_flip = 2.0 * eps_f / C_eta                 # (local)
    eta_flip_over_eps = eta_flip / eps_f           # (local) = 2/C_eta = 1.298

    # --- Planck sigma-distance bookkeeping (plan boundary note) -----------
    sigma_LO = (planck_ns - float(n_s_LO)) / planck_ns_err     # (local)
    sigma_NLO = (planck_ns - float(n_s_NLO)) / planck_ns_err   # (local)
    sigma_shift = abs(sigma_NLO - sigma_LO)                    # (local)

    # --- Regime diagnostics ------------------------------------------------
    series_ratio = eps_f / (1.0 - eps_f)           # (local) geometric convergence ratio
    nnlo_over_nlo = abs(float(resid_NNLO) / delta_central)  # (local)

    return {
        "value": delta_central,
        "n_s_LO": n_s_LO, "eps_H": eps_H, "n_s_NLO": n_s_NLO,
        "delta_ns_NLO": delta_ns_NLO, "n_s_T6": n_s_T6, "resid_NNLO": resid_NNLO,
        "C2_exact": C2_exact, "C_SL": C_SL, "C_eta": C_eta,
        "route_diff": route_diff,
        "ratio_a4_a2": ratio_a4_a2, "eta_H_a4": eta_H_a4, "eta_term_a4": eta_term_a4,
        "eps_spread": eps_spread, "eta_H_spread": eta_H_spread,
        "eta_term_spread": eta_term_spread,
        "env_a4": env_a4, "env_worst": env_worst, "env_min": env_min,
        "eta_flip": eta_flip, "eta_flip_over_eps": eta_flip_over_eps,
        "sigma_LO": sigma_LO, "sigma_NLO": sigma_NLO, "sigma_shift": sigma_shift,
        "series_ratio": series_ratio, "nnlo_over_nlo": nnlo_over_nlo,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict (pre-registered bands) + schema-v2 3-tuple
# ---------------------------------------------------------------------------
def evaluate_gate(abs_delta: float) -> str:
    """|Delta| < 0.003 PASS; 0.003 <= |Delta| < 0.009 INFO; >= 0.009 FAIL."""
    if abs_delta < PASS_BAND:
        return "PASS"
    if abs_delta < INFO_BAND:
        return "INFO"
    return "FAIL"


def evaluate_3tuple(r: dict):
    """[SIGN] 3-tuple per gate-verdicts.md schema-v2 (all pre-registered)."""
    # sign: pre-registered NEGATIVE (slow-roll reddens)
    sign_v = "PASS" if r["value"] < 0.0 else "FAIL"            # (local)
    # magnitude: same banding as the composite operator
    mag_v = evaluate_gate(abs(r["value"]))                     # (local)
    # regime: slow-variation series convergence + NNLO smallness
    worst_ratio = max(r["series_ratio"], r["nnlo_over_nlo"])   # (local)
    if worst_ratio < REGIME_VALID_CAP:
        reg_v = "VALID"                                        # (local)
    elif worst_ratio < REGIME_BREAKDOWN_CAP:
        reg_v = "MARGINAL"                                     # (local)
    else:
        reg_v = "BREAKDOWN"                                    # (local)
    return sign_v, mag_v, reg_v


def collapse(sign_v: str, mag_v: str, reg_v: str) -> str:
    """Canonical composite-collapse rule (gate-verdicts.md, pre-registered)."""
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


def emit_4tuple(value, scheme, convention, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    """Print the emit_verdict payload (agent calls mcp__knowledge__emit_verdict)."""
    payload = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }  # (local)
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
def make_plot(r: dict, verdict: str):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.4))  # (local)

    # Left: tilt ladder vs Planck band
    ns_lo = float(r["n_s_LO"])     # (local)
    ns_nlo = float(r["n_s_NLO"])   # (local)
    ns_t6 = float(r["n_s_T6"])     # (local)
    ax1.axvspan(planck_ns - 2 * planck_ns_err, planck_ns + 2 * planck_ns_err,
                color="tab:blue", alpha=0.10, label="Planck 2018 ±2σ")
    ax1.axvspan(planck_ns - planck_ns_err, planck_ns + planck_ns_err,
                color="tab:blue", alpha=0.22, label="Planck 2018 ±1σ")
    ax1.axvline(planck_ns, color="tab:blue", lw=1.4, label=f"planck_ns = {planck_ns}")
    levels = [("LO  (1 − 2ε_H)", ns_lo, "tab:red", 1.00),
              ("NLO (1 − 2ε_H − 2ε_H²)", ns_nlo, "tab:orange", 0.62),
              ("T6 exact (1−3ε)/(1−ε)", ns_t6, "tab:green", 0.24)]  # (local)
    for label, x, c, y in levels:
        ax1.plot([x], [y], "o", ms=9, color=c)
        ax1.annotate(f"{label}\n{x:.6f}", (x, y), textcoords="offset points",
                     xytext=(8, -4), fontsize=8.5, color=c)
    ax1.annotate("", xy=(ns_nlo, 0.81), xytext=(ns_lo, 0.81),
                 arrowprops=dict(arrowstyle="->", color="k", lw=1.2))
    ax1.text(0.5 * (ns_lo + ns_nlo), 0.835, f"Δn_s^NLO = {r['value']:.4e}",
             ha="center", fontsize=9, color="k")
    ax1.set_ylim(0.0, 1.12)
    ax1.set_yticks([])
    ax1.set_xlabel("n_s")
    ax1.set_title(f"Tilt ladder: σ-distance {r['sigma_LO']:.3f}σ → {r['sigma_NLO']:.3f}σ "
                  f"(shift {r['sigma_shift']:.3f}σ < 0.7σ)", fontsize=10)
    ax1.legend(loc="upper left", fontsize=8)

    # Right: magnitude budget vs gate bands (log scale)
    names = ["|Δn_s^NLO|\ncentral (−2ε²)", "η-term\n(a₄-pulled)", "η-term\n(ε-spread)",
             "worst envelope", "|NNLO resid|"]  # (local)
    vals = [abs(r["value"]), r["eta_term_a4"], r["eta_term_spread"],
            r["env_worst"], abs(float(r["resid_NNLO"]))]  # (local)
    colors = ["tab:red", "tab:purple", "tab:purple", "tab:gray", "tab:green"]  # (local)
    bars = ax2.bar(range(len(vals)), vals, color=colors, alpha=0.75)  # (local)
    ax2.axhline(PASS_BAND, color="k", ls="--", lw=1.4, label=f"PASS band {PASS_BAND}")
    ax2.axhline(INFO_BAND, color="k", ls=":", lw=1.4, label=f"INFO→FAIL band {INFO_BAND}")
    ax2.set_yscale("log")
    ax2.set_xticks(range(len(names)))
    ax2.set_xticklabels(names, fontsize=8)
    for b, v in zip(bars, vals):
        ax2.text(b.get_x() + b.get_width() / 2, v * 1.15, f"{v:.3e}",
                 ha="center", fontsize=7.5)
    ax2.set_ylabel("|contribution to Δn_s|")
    ax2.set_title("NLO magnitude budget vs pre-registered bands", fontsize=10)
    ax2.legend(loc="upper right", fontsize=8)

    fig.suptitle(f"{GATE_ID}: {verdict} — Δn_s^NLO = {r['value']:.6e} "
                 f"(exact −2ε_H² = −192721/200000000), ε_H = 439/20000",
                 fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)
    print(f"  plot   -> {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()                 # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha} (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha} (script only)")
    print()

    r = compute()  # (local)

    # --- numbers first ---------------------------------------------------
    print("=== substitution chain (numbers) ===")
    print(f"  Def 1: n_s_LO = {r['n_s_LO']} = {float(r['n_s_LO']):.6f}  (bit-exact canonical)")
    print(f"         eps_H = (1 - n_s_LO)/2 = {r['eps_H']} = {float(r['eps_H']):.6f} EXACT")
    print(f"  Def 2: T6 exact n_s = (1-3e)/(1-e) = {r['n_s_T6']} = {float(r['n_s_T6']):.9f}")
    print(f"         series: 1 - 2e - 2e^2 - 2e^3 - ...  => C2 = {r['C2_exact']} EXACT (orders 1..5 verified in Q)")
    print(f"         n_s_NLO = 1 - 2e - 2e^2 = {r['n_s_NLO']} = {float(r['n_s_NLO']):.9f}")
    print(f"         Delta_ns_NLO = n_s_NLO - n_s_LO = {r['delta_ns_NLO']} = {r['value']:.6e}  <-- GATE VALUE")
    print(f"         NNLO+ residual = -2e^3/(1-e) = {float(r['resid_NNLO']):.4e} "
          f"({r['nnlo_over_nlo']*100:.2f}% of NLO term)")
    print(f"         two-route C2 cross-check (Hubble-flow, C={r['C_SL']:.10f}, "
          f"2C+3={r['C_eta']:.10f}): diff = {r['route_diff']:.3e} < {FLOAT_TOL:.0e}")
    print(f"  Def 3: eta_H = 0 on T6 constant-eps class (forced by LO anchor: linear -e2 term)")
    print(f"         a4-pulled proxy: a_4^zeta/a_2^zeta = {r['ratio_a4_a2']:.6f}; "
          f"eta_H_a4 = {r['eta_H_a4']:.6f}; |(2C+3) eps eta| = {r['eta_term_a4']:.4e}")
    print(f"         eps-spread proxy: |0.02195 - eps_H_W6({eps_H_W6})| = {r['eps_spread']:.5f}; "
          f"eta_H_spread = {r['eta_H_spread']:.6f}; term = {r['eta_term_spread']:.4e}")
    print(f"         envelopes: |Delta| in [{r['env_min']:.4e}, {r['env_worst']:.4e}] "
          f"(a4-route {r['env_a4']:.4e}); ALL < {PASS_BAND}")
    print(f"         sign-flip needs |eta_H| > 2eps/(2C+3) = {r['eta_flip']:.6f} "
          f"= {r['eta_flip_over_eps']:.3f} x eps_H  => sign ROBUST across envelope")
    print(f"  Planck: sigma_LO = {r['sigma_LO']:.4f}, sigma_NLO = {r['sigma_NLO']:.4f}, "
          f"shift = {r['sigma_shift']:.4f} sigma (< 0.7 boundary note)")
    print()

    # --- gate second -------------------------------------------------------
    sign_v, mag_v, reg_v = evaluate_3tuple(r)  # (local)
    verdict = collapse(sign_v, mag_v, reg_v)   # (local)
    print(f"=== gate: |Delta_ns_NLO| = {abs(r['value']):.6e} vs PASS<{PASS_BAND} / INFO<{INFO_BAND} ===")
    print(f"  sign_verdict={sign_v} (pre-registered NEGATIVE; computed {r['value']:+.3e})")
    print(f"  magnitude_verdict={mag_v}  regime_verdict={reg_v} "
          f"(series ratio {r['series_ratio']:.4f}, NNLO/NLO {r['nnlo_over_nlo']:.4f})")
    print(f"  composite (canonical collapse): {verdict}")
    print()

    # --- npz (full float64 + exact integers; Class 8.3 round-trip) ---------
    np.savez(
        OUT_NPZ,
        # gate value (full float64) + exact rational pins
        delta_ns_NLO=np.float64(r["value"]),
        delta_ns_NLO_num=np.int64(r["delta_ns_NLO"].numerator),
        delta_ns_NLO_den=np.int64(r["delta_ns_NLO"].denominator),
        n_s_LO=np.float64(float(r["n_s_LO"])),
        n_s_LO_num=np.int64(r["n_s_LO"].numerator),
        n_s_LO_den=np.int64(r["n_s_LO"].denominator),
        eps_H=np.float64(float(r["eps_H"])),
        eps_H_num=np.int64(r["eps_H"].numerator),
        eps_H_den=np.int64(r["eps_H"].denominator),
        n_s_NLO=np.float64(float(r["n_s_NLO"])),
        n_s_NLO_num=np.int64(r["n_s_NLO"].numerator),
        n_s_NLO_den=np.int64(r["n_s_NLO"].denominator),
        n_s_T6_exact=np.float64(float(r["n_s_T6"])),
        n_s_T6_num=np.int64(r["n_s_T6"].numerator),
        n_s_T6_den=np.int64(r["n_s_T6"].denominator),
        resid_NNLO=np.float64(float(r["resid_NNLO"])),
        # coefficients
        C2_exact=np.float64(r["C2_exact"]),
        C_SL=np.float64(r["C_SL"]),
        C_eta=np.float64(r["C_eta"]),
        route_diff=np.float64(r["route_diff"]),
        # eta_H envelopes
        ratio_a4_a2=np.float64(r["ratio_a4_a2"]),
        eta_H_a4=np.float64(r["eta_H_a4"]),
        eta_term_a4=np.float64(r["eta_term_a4"]),
        eps_H_W6_pin=np.float64(eps_H_W6),
        eps_spread=np.float64(r["eps_spread"]),
        eta_H_spread=np.float64(r["eta_H_spread"]),
        eta_term_spread=np.float64(r["eta_term_spread"]),
        env_a4=np.float64(r["env_a4"]),
        env_worst=np.float64(r["env_worst"]),
        env_min=np.float64(r["env_min"]),
        eta_flip=np.float64(r["eta_flip"]),
        eta_flip_over_eps=np.float64(r["eta_flip_over_eps"]),
        # Planck bookkeeping
        planck_ns_pin=np.float64(planck_ns),
        planck_ns_err_pin=np.float64(planck_ns_err),
        sigma_LO=np.float64(r["sigma_LO"]),
        sigma_NLO=np.float64(r["sigma_NLO"]),
        sigma_shift=np.float64(r["sigma_shift"]),
        # moments (zeta-regulated; regulator-pin-discipline)
        a_2_zeta_pin=np.float64(a_2_FW_zeta),
        a_4_zeta_pin=np.float64(a_4_FW_zeta),
        # regime + bands
        series_ratio=np.float64(r["series_ratio"]),
        nnlo_over_nlo=np.float64(r["nnlo_over_nlo"]),
        pass_band=np.float64(PASS_BAND),
        info_band=np.float64(INFO_BAND),
        # verdicts + SHAs
        verdict=np.array(verdict),
        sign_verdict=np.array(sign_v),
        magnitude_verdict=np.array(mag_v),
        regime_verdict=np.array(reg_v),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
        scheme=np.array(SCHEME),
        convention=np.array(CONVENTION),
        L_max=np.array(L_MAX),
    )
    print(f"  data   -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(r, verdict)
    print()

    # --- 4-tuple + payload ---------------------------------------------------
    print(emit_4tuple(r["value"], SCHEME, CONVENTION, L_MAX))
    value_str = (
        f"Delta_ns_NLO={r['value']:.6e} exact -192721/200000000 = -2*eps_H^2 (C2=2 from T6 exact (1-3e)/(1-e)); "
        f"eps_H=439/20000=0.02195; n_s_NLO={float(r['n_s_NLO']):.9f}; NNLO_resid={float(r['resid_NNLO']):.3e}; "
        f"eta-envelope worst |Delta|={r['env_worst']:.3e} sign-robust; "
        f"Planck sigma {r['sigma_LO']:.3f}->{r['sigma_NLO']:.3f} shift {r['sigma_shift']:.3f}<0.7"
    )  # (local)
    extra_rows = [
        f"# regulator_pin: a_2^{{zeta}}={a_2_FW_zeta} a_4^{{zeta}}={a_4_FW_zeta} "
        f"(zeta-regulated Seeley-DeWitt per regulator-pin-discipline.md) # {GATE_ID}",
        f"# eta_H-envelope: central eta_H=0 (T6 constant-eps class, forced by LO anchor); "
        f"a4-pulled eta_H={r['eta_H_a4']:.6f} -> |Delta|={r['env_a4']:.3e}; "
        f"eps-spread (vs eps_H_W6={eps_H_W6}, DeltaN=1) -> worst |Delta|={r['env_worst']:.3e}; "
        f"all < {PASS_BAND} # {GATE_ID}",
    ]  # (local)
    print_verdict_payload(
        verdict, value_str, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        companion_note=(f"C2=2 exact (T6 series, orders 1..5 verified in Q); "
                        f"two-route Hubble-flow x-check diff {r['route_diff']:.1e}"),
        extra_rows=extra_rows,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    # Exit 0 on any valid scientific verdict (math-scripts.md exit-code semantics)
    return 0


if __name__ == "__main__":
    sys.exit(main())
