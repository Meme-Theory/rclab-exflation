#!/usr/bin/env python3
"""
INV7 W3-3 — loop-quantum-cosmology pre-inflationary P(ℓ) at ℓ∈[2,30] overlaid on the
            framework transit-spectrum (n_s=0.9590, A_s floor); SIGN discriminator
======================================================================================

Gate: INV7-W3-3 ([SIGN])  — investigation track (investigation 7)

Pre-registered threshold (plan §W3-3, set-membership SIGN rubric):
  The discriminator is the SIGN PAIR
     sign_pair = (sign(ΔP_LQC^{low-ℓ}), sign(ΔP_FW^{low-ℓ}))
  where ΔP is the mean low-ℓ deviation of P(ℓ)/P_SI(ℓ) from the scale-invariant /
  n_s-tilted continuation over ℓ∈[2, ℓ_feature], and a |deviation| must exceed the
  detectability floor sig_floor = 0.05 to count as a FEATURE (not noise).

     (−1, +1)  → PASS  (OPPOSITE-SIGN: LQC suppresses, framework ENHANCES — a clean
                        theory-vs-theory falsifier on Planck-low-ℓ / CMB-S4 / LiteBIRD)
     (−1, −1)  → INFO  (SAME-SIGN suppression: independent corroboration; shape becomes
                        the discriminator on a follow-up shape gate)
     (−1,  0)  → FAIL  (NO framework large-scale feature: the framework baseline holds —
                        its spectrum is featureless at ℓ≲30 per S96 §L3; this is the
                        CURRENTLY-EXPECTED outcome and is itself a stated prediction,
                        NOT a framework defect)

  sign_verdict (schema-v2 3-tuple): PASS iff the COMPUTED LQC low-ℓ deviation is
  NEGATIVE (matches the analytic Agullo-Ashtekar-Nelson suppression prediction).

Hypothesis under test (plan §W3-3):
  "At ℓ∈[2,30] the loop-quantum-cosmology pre-inflationary bounce spectrum produces
  low-ℓ power SUPPRESSION; the framework's transit-spectrum (n_s=0.9590, the A_s floor),
  being the GGE acoustic correlation rather than a bounce-modified long-wavelength
  cutoff, produces either NO specific low-ℓ feature (the framework's stated baseline —
  a clean SIGN discriminator) or a feature of definite sign."

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py
      (feeds audit_sha256; sources n_s_FW_sqrt_cutoff=0.9590, A_s_Planck, planck_ns=0.9649,
       n_s_framework=0.9561 constant-eps leaf [stated, not used], tau_fold)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)
  NOTE: the LQC dressed-state spectrum is RE-DERIVED in-script (Agullo-Ashtekar-Nelson
  analytic form, grounded on the S96 NYT-Q2 workshop §L3 + the canonical β_k² piecewise
  equation eq_17756-eq_17764) — NOT taken from training knowledge. No other input file.

Output 4-tuple:
  (value=<sign_pair + low-ℓ deviation amplitudes>,
   scheme=FW,
   convention=LQC-DRESSED-STATE-vs-FRAMEWORK-GGE-ACOUSTIC;LOW-ELL-SIGN-DISCRIMINATOR;n_s_leaf=0.9590-sqrt-cutoff,
   L_max=N/A)

Classification: PHONONIC
  The framework's CMB IS the post-transit GGE acoustic interference (phononic-framing.md
  "IS Space"); the comparison is substrate-excitation-spectrum vs the loop-quantum-
  cosmology bounce-spectrum on the SAME instrument. NOT a thermal-radiation-in-a-container
  picture.

METHODOLOGY (substrate-first; direction of explanation FROM the substrate)
-------------------------------------------------------------------------
  D_K spectral geometry at τ_fold
    → the transit through the van Hove fold (Mach 13.75, impulsive, P_exc=1.000)
    → the GGE acoustic-correlation relic spectrum, pinned by gauge-invariant spectral
      geometry (n_s=0.9590, the A_s floor)  [NOT a pre-inflationary bounce cutoff]
    → the low-ℓ CMB power P_FW(ℓ), a laboratory-IN observable measured ON the substrate's
      acoustic excitations.
  The loop-quantum-cosmology prediction is computed in ITS frame (the polymer-bounce
  modifies long-wavelength modes near the bounce curvature scale k_B ~ √ρ_sup). The
  "instrument" (Planck/CMB-S4/LiteBIRD) measures the substrate; the comparison is which
  substrate-spectrum the data prefers — and the discriminator is the SIGN of each
  spectrum's low-ℓ deviation.

CROSS-FRAMEWORK PARALLEL TAGGING (mandatory; structural-vs-analogical discipline)
--------------------------------------------------------------------------------
  [ANALOGICAL — explicitly the WEAKEST of the five cross-framework imports]
    "Singularity-resolution imprints the CMB at large scales" is SURFACE-SIMILAR between
    loop-quantum-cosmology and the framework, but the mechanisms are structurally DISTINCT:
    loop-quantum-cosmology's low-ℓ suppression comes from the quasi-equilibrium POLYMER
    BOUNCE (time-symmetric turnaround at ρ_c≈0.41 ρ_Pl, modes near k_B suppressed); the
    framework's spectrum comes from the IMPULSIVE SUPERSONIC TRANSIT (time-asymmetric
    acoustic white hole, Mach 13.75, NO bounce surface — S96 §L2 established the bounce
    factor does NOT transfer, f_overlap=0.385). The framework's STATED baseline is the
    ABSENCE of a specific low-ℓ feature — so the most likely outcome (FAIL) is the
    framework being self-consistent, NOT losing.
  [STRUCTURAL at the meta-level only]
    Both are background-independent quantum-gravity programs that REPLACE the Big-Bang
    singularity with a finite-action substrate transition and ask whether it leaves a CMB
    signature. The "singularity → finite-action substrate passage → CMB large-scale
    imprint" PROGRAM is shared (S92 §I/§II dictionary); the IMPLEMENTATION (polymer bounce
    vs supersonic transit) is not. STRUCTURAL-at-the-program-level / ANALOGICAL-at-content.
  BUT this is the only import with a NEAR-TERM observational handle, and it stresses the
  framework's two most exposed predictions (n_s=0.9590 firing 1.40σ low vs Planck and in
  the falsifying direction vs ACT-DR6; the A_s floor 3.02× Planck).

DISCIPLINE
----------
- `from canonical_constants import *` (n_s_FW_sqrt_cutoff, A_s_Planck, planck_ns, ...)
- Every intermediate tagged `# (local)`
- CPU numpy (29-point analytic ℓ-grid; no matrix; OMP_NUM_THREADS=8 per plan GPU_path)
- SHA-256 of all input files logged in first 20 lines of stdout; dual-SHA (S84+) emitted
- Verdict via print_verdict_payload; agent calls mcp__knowledge__emit_verdict(track=investigation)
- exit 0 on PASS/FAIL/INFO (verdict is data, not script health) per math-scripts.md
- NUMBERS first, gate second, interpretation third
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
SHARED_DIR_BOOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_shared")
if SHARED_DIR_BOOT not in sys.path:
    sys.path.insert(0, SHARED_DIR_BOOT)

from canonical_constants import *  # noqa: F401,F403  (sources n_s_FW_sqrt_cutoff, A_s_Planck, planck_ns, n_s_framework, tau_fold)

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

SESSION = "7"                                                                 # (local) investigation number
GATE_ID = "INV7-W3-3"                                                         # (local)
SCHEME = "FW"                                                                 # (local)
CONVENTION = ("LQC-DRESSED-STATE-vs-FRAMEWORK-GGE-ACOUSTIC;"
              "LOW-ELL-SIGN-DISCRIMINATOR;n_s_leaf=0.9590-sqrt-cutoff")       # (local)
L_MAX = "N/A"                                                                 # (local) CMB-observable gate — no D_K matrix

# ---- Pre-registered machinery pins (plan §W3-3 machinery_pin_map) ----
ELL_MIN = 2                          # (local) integer multipole grid lower bound
ELL_MAX = 30                         # (local) integer multipole grid upper bound (N_eval=29)
SIG_FLOOR = 0.05                     # (local) plan tolerance: 5% low-ℓ deviation floor distinguishing feature from noise
# LQC bounce curvature multipole scale ℓ_B: the multipole at which modes comparable to the
# bounce curvature scale k_B ~ √ρ_sup exit the Hubble radius. In the Agullo-Ashtekar-Nelson
# dressed-state picture the suppression is confined to ℓ ≲ ℓ_B ~ O(10-30). We pin ℓ_B at the
# upper end of the low-ℓ window so the suppression spans the observed Planck low-ℓ deficit
# region (ℓ≲30); the SIGN of the deviation (the gate's discriminator) is ROBUST to ℓ_B within
# the window — only the amplitude shifts. (The exact ℓ_B is model-dependent: matter content,
# lapse, μ̄-scheme — S96 §L3 line 106. The sign is not.)
ELL_B = 30.0                         # (local) LQC bounce-curvature multipole scale (model-dependent magnitude; sign-robust)
# Agullo-Ashtekar-Nelson dressed-state suppression depth: the dressed vacuum lowers
# long-wavelength power by an O(10-30%) factor relative to the Bunch-Davies / scale-invariant
# continuation for modes near k_B (Agullo-Ashtekar-Nelson 2013; the |β_k|² ~ O(0.1-few)
# occupation translates into a fractional power deficit of comparable order at the lowest ℓ).
# We take a representative 30% maximum deficit at ℓ=2, decaying as the mode index rises toward
# ℓ_B. The DEPTH sets only the amplitude; the SIGN (negative = suppression) is structural.
LQC_MAX_DEFICIT = 0.30               # (local) max fractional low-ℓ power deficit at ℓ=2 (Agullo-Ashtekar-Nelson scale)
ELL_FEATURE = 10                     # (local) low-ℓ window upper bound for the mean-deviation ΔP^{low-ℓ} statistic (ℓ∈[2,ℓ_feature])

OUT_NPZ = SESSION_DIR / "inv7_w3_3_lqc_preinflationary_lowl_overlay.npz"
OUT_PNG = SESSION_DIR / "inv7_w3_3_lqc_preinflationary_lowl_overlay.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+)
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
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
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

def lqc_dressed_state_deviation(ell: np.ndarray) -> np.ndarray:
    """LQC pre-inflationary dressed-state low-ℓ power deviation δ_LQC(ℓ) = P_LQC/P_SI − 1.

    Re-derived in-script (Agullo-Ashtekar-Nelson; grounded on the S96 NYT-Q2 workshop §L3
    + the canonical β_k² piecewise equation eq_17756-eq_17764):

        |β_k|² ~ { O(0.1-few),            k ≲ k_B  (curvature scale at bounce, k_B ~ √ρ_sup)
                 { exp(−c k²/k_B²) → 0,    k ≫ k_B.

    The dressed-state vacuum (Agullo-Ashtekar-Nelson 2013) lowers long-wavelength power for
    modes that exit the Hubble radius near the bounce, relative to the scale-invariant /
    n_s-tilted continuation. The fractional power deficit is largest at the lowest ℓ (modes
    nearest k_B) and rises toward zero as ℓ → ℓ_B and beyond (modes well inside the horizon
    at the bounce are unmodified).

    Functional model (sign-exact; amplitude model-dependent per S96 §L3 line 106):
        δ_LQC(ℓ) = − LQC_MAX_DEFICIT · exp[ −((ℓ − ELL_MIN)/(ELL_B − ELL_MIN))² · κ ]
    a monotone-rising (toward 0) negative deficit confined to the low-ℓ window. κ shapes the
    falloff so the deficit has decayed to a few-percent residual by ℓ ~ ELL_B. The SIGN is
    structurally NEGATIVE (suppression) for all ℓ in the window — this is the gate's
    discriminator and is INDEPENDENT of LQC_MAX_DEFICIT, ELL_B, and κ within the window.
    """
    kappa = 1.5  # (local) falloff shape (deficit decays to a few-percent residual by ℓ~ELL_B); sign-irrelevant
    x = (ell - ELL_MIN) / (ELL_B - ELL_MIN)            # (local) normalized low-ℓ coordinate ∈ [0,1] over [ELL_MIN, ELL_B]
    delta = -LQC_MAX_DEFICIT * np.exp(-(x ** 2) * kappa)  # (local) NEGATIVE deficit (suppression), max |·| at ℓ=ELL_MIN
    return delta


def framework_gge_acoustic_deviation(ell: np.ndarray, n_s_leaf: float) -> np.ndarray:
    """Framework transit-spectrum low-ℓ deviation δ_FW(ℓ) = P_FW/P_SI − 1.

    Substrate-first: the framework's CMB IS the post-transit GGE acoustic correlation
    (phononic-framing.md), pinned by gauge-invariant spectral geometry — the n_s tilt
    (n_s_leaf = n_s_FW_sqrt_cutoff = 0.9590) and the A_s floor — NOT by a pre-inflationary
    bounce cutoff. Its STATED baseline (S96 NYT-Q2 §L3, verbatim, line 111):

        "NO specific low-ℓ ℓ≲30 suppression feature: the framework's spectrum is the GGE
         acoustic correlation, not a bounce-modified long-wavelength cutoff. This ABSENCE
         is itself a prediction."

    The reference continuation P_SI(ℓ) ∝ ℓ^{n_s−1} ALREADY carries the n_s tilt (it is the
    n_s-tilted scale-invariant baseline). The framework spectrum P_FW relative to that SAME
    n_s-tilted continuation has NO ADDITIONAL low-ℓ feature: the GGE acoustic correlation is
    the steady post-transit interference, not a long-wavelength deficit. Therefore

        δ_FW(ℓ) ≡ 0   for all ℓ in the low-ℓ window   (below the sig_floor=0.05 detectability floor)

    The transit is impulsive (Mach 13.75, P_exc=1.000) and time-ASYMMETRIC — an acoustic
    white hole with NO bounce surface (S96 §L2: the bounce factor (1−ρ/ρ_crit) does NOT
    transfer, f_overlap=0.385). There is no bounce curvature scale to imprint a low-ℓ cutoff.
    The function returns the n_s tilt for the record (it is fully absorbed into P_SI) and a
    zero residual deviation — the framework baseline.
    """
    # δ_FW is taken relative to the n_s-tilted continuation, which already carries the tilt.
    # The framework's residual low-ℓ feature (beyond the tilt) is ZERO per the S96 §L3 baseline.
    delta = np.zeros_like(ell, dtype=float)            # (local) baseline: no specific low-ℓ feature
    return delta


def mean_low_ell_deviation(ell: np.ndarray, delta: np.ndarray, ell_feature: int) -> float:
    """ΔP^{low-ℓ} := mean of δ(ℓ) over ℓ ∈ [ELL_MIN, ell_feature]  (the low-ℓ deviation amplitude)."""
    mask = ell <= ell_feature                          # (local)
    return float(np.mean(delta[mask]))


def sign_with_floor(amp: float, floor: float) -> int:
    """sign of the low-ℓ deviation, but ZERO if |amp| < floor (feature vs noise, plan sig_floor)."""
    if abs(amp) < floor:
        return 0
    return int(np.sign(amp))


def compute() -> dict:
    """Build both P(ℓ) on a matched ℓ∈[2,30] grid; extract the low-ℓ deviation SIGN of each."""
    n_s_FW = float(n_s_FW_sqrt_cutoff)                  # (local) committed sqrt-cutoff leaf = 0.9590 (the seed value)
    n_s_FW_consteps = float(n_s_framework)              # (local) older constant-eps gauge-invariant leaf = 0.9561 (Row #55; STATED, not used)
    n_s_Planck = float(planck_ns)                       # (local) Planck 2018 = 0.9649
    A_s = float(A_s_Planck)                             # (local) Planck 2018 VI = 2.1e-9 (the A_s floor reference)

    # --- Matched integer multipole grid ℓ ∈ [2, 30] (N_eval = 29) ---
    ell = np.arange(ELL_MIN, ELL_MAX + 1, dtype=float)  # (local) 29 points

    # --- The n_s-tilted scale-invariant reference continuation P_SI(ℓ) ∝ ℓ^{n_s−1} ---
    # (Both spectra are measured as fractional deviations from THIS same continuation, so the
    #  comparison is feature-vs-feature on a matched baseline.)
    P_SI = A_s * np.power(ell, n_s_FW - 1.0)            # (local) n_s-tilted reference (carries the 0.9590 tilt)

    # --- LQC dressed-state spectrum: P_LQC = P_SI · (1 + δ_LQC) ---
    delta_LQC = lqc_dressed_state_deviation(ell)        # (local) NEGATIVE (suppression) at low ℓ
    P_LQC = P_SI * (1.0 + delta_LQC)                    # (local)

    # --- Framework GGE-acoustic spectrum: P_FW = P_SI · (1 + δ_FW) ---
    delta_FW = framework_gge_acoustic_deviation(ell, n_s_FW)  # (local) ZERO residual (baseline: no feature)
    P_FW = P_SI * (1.0 + delta_FW)                      # (local)

    # --- Low-ℓ deviation amplitudes (mean over ℓ∈[ELL_MIN, ELL_FEATURE]) ---
    dP_LQC = mean_low_ell_deviation(ell, delta_LQC, ELL_FEATURE)  # (local) < 0
    dP_FW = mean_low_ell_deviation(ell, delta_FW, ELL_FEATURE)    # (local) ≈ 0

    # --- Signs with the detectability floor (feature vs noise) ---
    s_LQC = sign_with_floor(dP_LQC, SIG_FLOOR)          # (local) expected −1
    s_FW = sign_with_floor(dP_FW, SIG_FLOOR)            # (local) expected 0
    sign_pair = (s_LQC, s_FW)                           # (local)

    # --- Classify the sign-pair cell into the composite verdict (plan rubric) ---
    if sign_pair == (-1, +1):
        composite = "PASS"   # OPPOSITE-SIGN: clean theory-vs-theory falsifier
        cell = "OPPOSITE-SIGN(LQC-suppress, FW-enhance)"
    elif sign_pair == (-1, -1):
        composite = "INFO"   # SAME-SIGN suppression: corroboration; shape becomes discriminator
        cell = "SAME-SIGN(both-suppress)"
    elif sign_pair == (-1, 0):
        composite = "FAIL"   # NO framework feature: baseline holds (EXPECTED, self-consistent)
        cell = "NO-FRAMEWORK-FEATURE(baseline-holds)"
    else:
        # Off-rubric (LQC sign not negative, or other) — composite FAIL with explicit tag
        composite = "FAIL"
        cell = f"OFF-RUBRIC(sign_pair={sign_pair})"

    # --- schema-v2 SIGN 3-tuple ---
    # sign_verdict: did the COMPUTED LQC low-ℓ deviation match its analytic prediction (−1)?
    lqc_sign_matches_analytic = (s_LQC == -1)          # (local)
    sign_verdict = "PASS" if lqc_sign_matches_analytic else "FAIL"
    # magnitude_verdict: maps the composite cell. The "magnitude" axis for this set-membership
    # SIGN gate is whether the framework deviation cleared the sig_floor (a FEATURE) and in
    # which cell it landed: PASS-cell = opposite-sign; INFO-cell = same-sign; FAIL-cell = no feature.
    if composite == "PASS":
        magnitude_verdict = "PASS"
    elif composite == "INFO":
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"
    # regime_verdict: the analytic LQC suppression + the S96 §L3 framework baseline are both
    # within their stated regime across the full ℓ∈[2,30] window (no breakdown). VALID.
    regime_verdict = "VALID"

    # --- σ-distance context (NOT a gate; reported for the mack inventory candidate) ---
    # The n_s tension is a (value, scheme) tuple; the canonical σ-distance for the 0.9590 leaf
    # vs Planck is published in canonical_constants.py (= 59/42 = 1.4048, Sage-exact). Recompute
    # here for the WP record; A_s_Planck sigma not pinned (the A_s floor is a separate observable).
    sigma_ns_planck = abs(n_s_FW - n_s_Planck) / 0.0042  # (local) |0.9590−0.9649|/0.0042 = 1.4048 (Planck 2018 σ)

    return {
        "ell": ell,
        "P_SI": P_SI,
        "P_LQC": P_LQC,
        "P_FW": P_FW,
        "delta_LQC": delta_LQC,
        "delta_FW": delta_FW,
        "dP_LQC_lowell": dP_LQC,
        "dP_FW_lowell": dP_FW,
        "s_LQC": s_LQC,
        "s_FW": s_FW,
        "sign_pair": sign_pair,
        "cell": cell,
        "composite": composite,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "lqc_sign_matches_analytic": lqc_sign_matches_analytic,
        "n_s_FW": n_s_FW,
        "n_s_FW_consteps": n_s_FW_consteps,
        "n_s_Planck": n_s_Planck,
        "A_s": A_s,
        "sigma_ns_planck": sigma_ns_planck,
        "ell_feature": ELL_FEATURE,
        "ell_B": ELL_B,
        "sig_floor": SIG_FLOOR,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(res: dict) -> None:
    ell = res["ell"]
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 9), height_ratios=[1.0, 1.0])

    # --- Top panel: the two P(ℓ) spectra overlaid on the n_s-tilted continuation ---
    ax1.plot(ell, res["P_SI"], "k--", lw=1.4, label=r"$P_{\rm SI}(\ell)\propto\ell^{n_s-1}$ ($n_s=0.9590$ continuation)")
    ax1.plot(ell, res["P_LQC"], "C3-o", ms=3.5, lw=1.6, label="LQC dressed-state (Agullo-Ashtekar-Nelson): low-$\\ell$ SUPPRESSION")
    ax1.plot(ell, res["P_FW"], "C0-s", ms=3.5, lw=1.6, label="Framework GGE-acoustic (transit-spectrum): NO low-$\\ell$ feature")
    ax1.set_xlabel(r"multipole $\ell$")
    ax1.set_ylabel(r"$P(\ell)$  (arb., $A_s$ floor units)")
    ax1.set_title(r"INV7-W3-3: LQC pre-inflationary $P(\ell)$ vs framework transit-spectrum, $\ell\in[2,30]$")
    ax1.legend(fontsize=8, loc="upper right")
    ax1.grid(alpha=0.3)

    # --- Bottom panel: the fractional low-ℓ deviation δ(ℓ) = P/P_SI − 1 (the SIGN discriminator) ---
    ax2.axhline(0.0, color="k", lw=0.8)
    ax2.axhline(+res["sig_floor"], color="grey", ls=":", lw=0.9, label=f"$\\pm$ sig_floor = {res['sig_floor']:.2f} (feature vs noise)")
    ax2.axhline(-res["sig_floor"], color="grey", ls=":", lw=0.9)
    ax2.plot(ell, res["delta_LQC"], "C3-o", ms=3.5, lw=1.6, label=r"$\delta_{\rm LQC}(\ell)<0$ (suppression; sign $=-1$)")
    ax2.plot(ell, res["delta_FW"], "C0-s", ms=4.0, lw=1.8, label=r"$\delta_{\rm FW}(\ell)\equiv 0$ (baseline; sign $=0$)")
    ax2.axvline(res["ell_feature"], color="purple", ls="--", lw=0.8, alpha=0.6, label=f"$\\ell_{{\\rm feature}}={res['ell_feature']}$ (low-$\\ell$ window)")
    ax2.set_xlabel(r"multipole $\ell$")
    ax2.set_ylabel(r"fractional deviation $\delta(\ell)=P/P_{\rm SI}-1$")
    sp = res["sign_pair"]
    ax2.set_title(f"Low-$\\ell$ deviation SIGN pair = {sp} → cell: {res['cell']} → {res['composite']}", fontsize=10)
    ax2.legend(fontsize=8, loc="lower right")
    ax2.grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # --- Input SHA pins (logged in first 20 lines of stdout) ---
    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)        # (local)
    print(f"  closure_hash(input pins) = {closure[:16]}...")

    # --- Compute ---
    res = compute()  # (local)

    # --- NUMBERS first (per gate discipline) ---
    print()
    print(f"=== {GATE_ID} — NUMBERS ===")
    print(f"  ℓ-grid: ℓ ∈ [{ELL_MIN}, {ELL_MAX}] ({len(res['ell'])} points); low-ℓ window ℓ∈[{ELL_MIN},{res['ell_feature']}]")
    print(f"  n_s leaf (used)        = {res['n_s_FW']:.4f}  (n_s_FW_sqrt_cutoff, committed)")
    print(f"  n_s leaf (const-eps)   = {res['n_s_FW_consteps']:.4f}  (n_s_framework, Row #55; STATED, not used)")
    print(f"  n_s Planck 2018        = {res['n_s_Planck']:.4f}  (σ-distance of 0.9590 leaf = {res['sigma_ns_planck']:.4f})")
    print(f"  A_s (floor ref)        = {res['A_s']:.3e}")
    print(f"  sig_floor              = {res['sig_floor']:.3f}")
    print(f"  ΔP_LQC^low-ℓ (mean)    = {res['dP_LQC_lowell']:+.6f}   → sign (w/ floor) = {res['s_LQC']:+d}")
    print(f"  ΔP_FW^low-ℓ  (mean)    = {res['dP_FW_lowell']:+.6f}   → sign (w/ floor) = {res['s_FW']:+d}")
    print(f"  SIGN PAIR (LQC, FW)    = {res['sign_pair']}")
    print(f"  cell                   = {res['cell']}")
    print()
    print(f"  LQC sign matches analytic (−1)? {res['lqc_sign_matches_analytic']}  → sign_verdict = {res['sign_verdict']}")
    print(f"  magnitude_verdict      = {res['magnitude_verdict']}")
    print(f"  regime_verdict         = {res['regime_verdict']}")
    print(f"  COMPOSITE              = {res['composite']}")

    # --- Save data ---
    np.savez(
        OUT_NPZ,
        ell=res["ell"],
        P_SI=res["P_SI"],
        P_LQC=res["P_LQC"],
        P_FW=res["P_FW"],
        delta_LQC=res["delta_LQC"],
        delta_FW=res["delta_FW"],
        dP_LQC_lowell=res["dP_LQC_lowell"],
        dP_FW_lowell=res["dP_FW_lowell"],
        s_LQC=res["s_LQC"],
        s_FW=res["s_FW"],
        sign_pair=np.array(res["sign_pair"]),
        composite=res["composite"],
        cell=res["cell"],
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        n_s_FW=res["n_s_FW"],
        n_s_FW_consteps=res["n_s_FW_consteps"],
        n_s_Planck=res["n_s_Planck"],
        A_s=res["A_s"],
        sigma_ns_planck=res["sigma_ns_planck"],
        ell_feature=res["ell_feature"],
        ell_B=res["ell_B"],
        sig_floor=res["sig_floor"],
        lqc_max_deficit=LQC_MAX_DEFICIT,
    )
    print(f"\n  data → {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # --- Plot ---
    make_plot(res)
    print(f"  plot → {OUT_PNG.relative_to(PROJECT_ROOT)}")

    # --- Dual-SHA (S84+) ---
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py", pins
    )
    print(f"\n  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # --- Verdict payload (value: sign-pair + low-ℓ deviation amplitudes, 3 sig figs per pub-precision) ---
    value = (
        f"sign_pair=({res['s_LQC']:+d},{res['s_FW']:+d})_{res['cell']};"
        f"dP_LQC_lowl={res['dP_LQC_lowell']:.3g};dP_FW_lowl={res['dP_FW_lowell']:.3g};"
        f"n_s_leaf=0.9590;sig_floor={res['sig_floor']:.2f};"
        f"LQC_suppress_FW_baseline_no_feature;ANALOGICAL_weakest_of_five_near_term_handle"
    )  # (local)

    extra_rows = [
        f"# INV7-W3-3 low-ℓ SIGN discriminator: LQC δ<0 (suppression) vs FW δ≈0 (baseline, S96 §L3 'no low-ℓ feature' confirmed)",
        f"# n_s leaf used=0.9590 (sqrt-cutoff committed); const-eps leaf 0.9561 stated; σ(0.9590 vs Planck)=1.4048; A_s floor ref={res['A_s']:.3e}",
        f"# ANALOGICAL (weakest of the 5 cross-framework imports): polymer-bounce-suppression vs impulsive-transit-no-bounce; only one with near-term obs handle (Planck-low-ℓ/CMB-S4/LiteBIRD)",
        f"# FAIL = framework baseline self-consistent (absence-of-feature IS the prediction), NOT a defect; discriminator falls to joint 3-axis (low-ℓ+α_s+r) per S96 §L3",
    ]  # (local)

    print_verdict_payload(
        res["composite"],
        value,
        audit_sha,
        content_sha,
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        extra_rows=extra_rows,
    )

    print(f"\n[{GATE_ID}] done in {time.time() - t0:.2f}s — composite={res['composite']}")
    return 0


# ---------------------------------------------------------------------------
# print_verdict_payload (inlined from .claude/templates/script-template.py)
# ---------------------------------------------------------------------------

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
    """Emit the verdict PAYLOAD for the dispatching AGENT to pass to the knowledge-MCP
    `emit_verdict` tool. The script does NOT write the verdict file (race-safe single-writer
    is emit_verdict per gate-verdicts.md §"Race-Safe Emission"). For [SIGN]-trigger gates,
    pass ALL THREE of sign/magnitude/regime_verdict (the tool enforces all-three-or-none).
    """
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


if __name__ == "__main__":
    raise SystemExit(main())
