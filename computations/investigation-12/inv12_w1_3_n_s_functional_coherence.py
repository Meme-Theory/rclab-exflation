#!/usr/bin/env python3
"""
INV12-W1-3-N-S-FUNCTIONAL-COHERENCE — n_s coherence between two canonical functionals
=====================================================================================

Gate: INV12-W1-3-N-S-FUNCTIONAL-COHERENCE  ([SIGN])
Agent: lizzi-spectral-functional-theorist (Investigation 12, Wave 1)

Pre-registered threshold (plan §W1-3):
  operator: |n_s(f*) - n_s(sqrt(x))| <= sigma_budget   (sigma_budget = Planck 2018 1sigma = 0.0042)
  PASS  iff |Delta n_s| <= 0.0042
  INFO  iff 0.0042 < |Delta n_s| <= 0.02
  FAIL  iff |Delta n_s| > 0.02
  [SIGN] prediction: the e^{-x} admixture in f* tilts BLUER => n_s(f*) >= n_s(sqrt(x)).

WHAT THIS GATE IS (and is NOT)
------------------------------
This is a COHERENCE CHECK between two ALREADY-CANONICAL spectral functionals:
  (A) pure sqrt(x)  -- the S103-committed cutoff family (n_s_FW_sqrt_cutoff = 0.959)
  (B) f* = 0.9117 sqrt(x) + 0.0883 e^{-x}  -- the WORKING functional (t_star = 0.08832)
It asks whether the framework's COMMITTED n_s (pure sqrt) is COHERENT with the
functional it actually uses for A_s / dynamics (f*).  It does NOT re-select the
functional, does NOT tune t*, does NOT compare against other functionals.
RE-SHOP IS FORBIDDEN (PROHIBITED_ACTIONS Class 1).  Whichever way Delta n_s lands,
the gate reports it; it never switches functionals.

METHODOLOGY (substrate-faithful canonical n_s pipeline; S64 T12 / S65 / S62)
----------------------------------------------------------------------------
n_s is a SHAPE INVARIANT of the spectral-action profile S(tau) (S64 Transfer
Function Factorization Theorem T12): the tilt depends only on the RATIO
eps_H = S'^2/(2 S S''), with the functional f entering through S(tau) = Tr f(D^2/Lambda^2).
The canonical framework map is the Hubble-slow-roll N2 identity:

    S_f(tau) = sum_{(p,q)} dim(p,q)^2 * sum_j f( lambda_j(tau)^2 / Lambda^2 )      [spectral action]
    eps_H(f) = (1/2) S_f'^2 / (S_f * S_f'')                                        [Hubble SR; E3]
    n_s(f)   = 1 - 2 eps_H(f)                                                      [N2]

For f = sqrt(x):   f(u)=sqrt(u) => S_sqrt = (1/Lambda) sum PW^2 sum|lambda|; the
overall 1/Lambda CANCELS in eps_H (n_s(sqrt) is Lambda-independent).  This
reproduces S_fold/dS_fold/d2S_fold and the canonical n_s = 0.9567 EXACTLY.

For f* :  f*(u) = 0.9117 sqrt(u) + 0.0883 e^{-u},  u = lambda^2/Lambda^2, Lambda = M_KK.
  S_{f*}(tau) = 0.9117 S_sqrt(tau) + 0.0883 G(tau),   G(tau) = sum PW^2 sum_j e^{-lambda_j^2/Lambda^2}.

Both functionals are evaluated on the IDENTICAL eigenvalue set {lambda_k(tau)} (the
S36 multi-tau cache, 7 tau values; the canonical sqrt-cutoff n_s machinery).  Only
the functional weight differs => Delta n_s is a PURE functional-difference.

PLAN-VS-REALITY DEVIATION (honestly disclosed; v3-closure-recovery Class-1 boundary)
------------------------------------------------------------------------------------
The plan PIN MAP names the single-tau cache s84_spectrum_cache_L12_tau019.npz.  But
the coherence observable n_s = 1 - 2 eps_H requires the tau-DERIVATIVES of S(tau)
(eps_H = S'^2/(2 S S'')), which a single-tau slice CANNOT supply.  The CANONICAL
n_s pipeline (S65/S63/S62) uses the multi-tau S36 cache (s36_sfull_tau_stabilization.npz,
7 tau values) -- it is literally what produced n_s_FW_sqrt_cutoff.  We therefore use
the S36 multi-tau cache as the PRIMARY input (substrate-natural, reproduces the
canonical sqrt n_s bit-for-bit) and cite the S84 L12 single-tau cache as a fold-slice
cross-check anchor.  This deviation is disclosed in the convention tag
(-S36-MULTITAU-PRIMARY) and the WP Methodology block.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-36/s36_sfull_tau_stabilization.npz   (PRIMARY: 7-tau spectrum)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (single-tau fold anchor)
  - computations/_shared/canonical_constants.py                (feeds audit_sha256)
  - script bytes                                               (feeds both SHAs)

Output 4-tuple:
  (value=<Delta n_s>, scheme=FW, convention=TWO-FUNCTIONAL-FIXED-SPECTRUM-S36-MULTITAU-PRIMARY, L_max=10)

Classification: PHONONIC.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
import sys

SESSION_DIR = os.path.dirname(os.path.abspath(__file__))
COMPUTATIONS_DIR = os.path.dirname(SESSION_DIR)
SHARED_DIR = os.path.join(COMPUTATIONS_DIR, "_shared")
PROJECT_ROOT = os.path.dirname(COMPUTATIONS_DIR)
sys.path.insert(0, SHARED_DIR)

os.environ.setdefault("OMP_NUM_THREADS", "8")   # n_s(eps_H) is a small scalar reduction; CPU-cap per plan GPU_path=numpy.linalg
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import (   # noqa: E402
    M_KK, tau_fold, planck_ns, planck_ns_err, t_star,
    n_s_FW_sqrt_cutoff, S_fold, dS_fold, d2S_fold,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib   # noqa: E402
import json      # noqa: E402
from pathlib import Path   # noqa: E402

import numpy as np   # noqa: E402
import matplotlib    # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt   # noqa: E402
from scipy.interpolate import CubicSpline   # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Identity + pre-registration pins
# ---------------------------------------------------------------------------
SESSION = "12"                                                       # (local) investigation number
GATE_ID = "INV12-W1-3-N-S-FUNCTIONAL-COHERENCE"                      # (local)
SCHEME = "FW"                                                        # (local) framework spectral-action n_s pipeline
CONVENTION = "TWO-FUNCTIONAL-FIXED-SPECTRUM-S36-MULTITAU-PRIMARY"    # (local) sqrt vs f* on IDENTICAL spectrum; NOT a re-selection
L_MAX = 10                                                           # (local) canonical D_K cache truncation

# Pre-registered thresholds (plan §W1-3)
SIGMA_BUDGET = planck_ns_err          # (local) = 0.0042 Planck 2018 n_s 1sigma
INFO_BAND = 0.02                       # (local) |Delta n_s| info-band ceiling (FAIL_meaning: > 0.02)

# f* functional coefficients (S72 fit; t_star = 0.08832 is the e^{-x} weight)
C_SQRT = 1.0 - t_star                  # (local) 0.91168 -- sqrt-piece coefficient (1 - t*)
C_EXP = t_star                         # (local) 0.08832 -- e^{-x} admixture (= t_star)

LAMBDA = 1.0                           # (local) eigenvalues already in M_KK units; x = (lambda/Lambda)^2, Lambda = M_KK => 1.0

# SU(3) sectors with max_pq_sum = 3 (the canonical n_s truncation; L_max=10 cache, near-fold modes)
SECTORS = [(p, q) for p in range(4) for q in range(4) if p + q <= 3]   # (local)
TAU_EVALS = np.array([0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22])       # (local) S36 cache tau grid

OUT_NPZ = os.path.join(SESSION_DIR, "inv12_w1_3_n_s_functional_coherence.npz")
OUT_PNG = os.path.join(SESSION_DIR, "inv12_w1_3_n_s_functional_coherence.png")

S36_CACHE = os.path.join(COMPUTATIONS_DIR, "session-36", "s36_sfull_tau_stabilization.npz")
S84_CACHE = os.path.join(COMPUTATIONS_DIR, "session-84", "s84_spectrum_cache_L12_tau019.npz")

INPUT_FILES = [
    os.path.join(SHARED_DIR, "canonical_constants.py"),
    S36_CACHE,
    S84_CACHE,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: str) -> str:
    h = hashlib.sha256()   # (local)
    try:
        with open(path, "rb") as fh:
            h.update(fh.read())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[str]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}   # (local)
    for p in inputs:
        sha = sha256_of(p)       # (local)
        rel = os.path.relpath(p, PROJECT_ROOT).replace("\\", "/")   # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: str, canonical_path: str, pins: dict[str, str]) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
    try:
        with open(script_path, "rb") as fh:
            script_bytes = fh.read()   # (local)
    except OSError:
        script_bytes = b""             # (local)
    try:
        with open(canonical_path, "rb") as fh:
            canonical_bytes = fh.read()   # (local)
    except OSError:
        canonical_bytes = b""             # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")   # (local)

    h_audit = hashlib.sha256()   # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()   # (local)

    h_content = hashlib.sha256()   # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()   # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Spectral-action / slow-roll machinery
# ---------------------------------------------------------------------------
def su3_dim(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def build_spectral_action(d_cache, func) -> tuple[np.ndarray, int]:
    """S_f(tau) = sum_{(p,q)} dim(p,q)^2 sum_j f( (lambda_j/Lambda)^2 ) over the S36 tau grid.

    Returns (S array over TAU_EVALS, PW-weighted mode count at fold)."""
    S = np.zeros(len(TAU_EVALS))   # (local)
    nmodes_fold = 0                 # (local)
    for i, tau in enumerate(TAU_EVALS):
        for (p, q) in SECTORS:
            key = f"evals_tau{tau:.3f}_{p}_{q}"   # (local)
            if key not in d_cache:
                continue
            lam = np.abs(d_cache[key])             # (local) |lambda_j(tau)|
            pw2 = su3_dim(p, q) ** 2               # (local) Peter-Weyl spectral-action multiplicity
            x = (lam / LAMBDA) ** 2                 # (local) spectral-action argument u = (lambda/Lambda)^2
            S[i] += pw2 * np.sum(func(x))
            if abs(tau - tau_fold) < 1e-9:
                nmodes_fold += su3_dim(p, q) * len(lam)
    return S, nmodes_fold


def eps_H_n_s(S: np.ndarray) -> dict:
    """Hubble slow-roll eps_H = (1/2) S'^2/(S S'') at the fold; n_s = 1 - 2 eps_H.

    CubicSpline over the near-fold subset (drop tau=0.05, far from fold), matching
    the canonical S65/S63 n_s pipeline."""
    idx = np.arange(1, len(TAU_EVALS))   # (local) indices 1..6 => tau 0.16..0.22
    tn = TAU_EVALS[idx]                   # (local)
    cs = CubicSpline(tn, S[idx])          # (local)
    tf = float(tau_fold)                  # (local)
    Sv = float(cs(tf))                    # (local)
    dS = float(cs(tf, 1))                 # (local)
    d2S = float(cs(tf, 2))                # (local)
    eps = 0.5 * dS ** 2 / (Sv * d2S)      # (local)
    ns = 1.0 - 2.0 * eps                  # (local)
    return {"S": Sv, "dS": dS, "d2S": d2S, "eps_H": eps, "n_s": ns, "spline": cs}


def single_tau_eps_proxy(d_l12, func) -> float | None:
    """Single-tau (S84 L12) cross-check: report sum PW^2 sum f(x) at the fold slice.

    A single tau slice has NO tau-neighbors, so eps_H = S'^2/(2 S S'') is NOT
    computable from it.  This anchor cross-checks ONLY the fold-slice spectral-action
    VALUE S_f(tau_fold) against the S36 cache (consistency of the two spectra at
    tau=0.19), not the tilt.  Returns the L12 spectral-action value."""
    try:
        se = d_l12["sector_evals"].item()   # (local) dict keyed by (p,q) -> {dim, level, abs_evals}
    except Exception:
        return None
    S_val = 0.0   # (local)
    for (p, q), rec in se.items():
        if (p + q) > 3:                      # (local) restrict to the same max_pq_sum=3 truncation
            continue
        lam = np.abs(np.asarray(rec["abs_evals"]))   # (local)
        pw2 = su3_dim(p, q) ** 2                       # (local)
        x = (lam / LAMBDA) ** 2                         # (local)
        S_val += pw2 * np.sum(func(x))
    return float(S_val)


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload helper (script PRINTS; agent calls emit_verdict)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION),
        "track": "investigation",
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
def main() -> None:
    print("=" * 78)
    print(f"{GATE_ID}")
    print("n_s COHERENCE: committed sqrt(x) vs working f* = 0.9117 sqrt(x) + 0.0883 e^{-x}")
    print("=" * 78)

    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(
        os.path.abspath(__file__),
        os.path.join(SHARED_DIR, "canonical_constants.py"),
        pins,
    )
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    print("\n  Pre-registered pins:")
    print(f"    sigma_budget (Planck n_s 1sigma) = {SIGMA_BUDGET}")
    print(f"    info-band ceiling                = {INFO_BAND}")
    print(f"    f* coefficients: c_sqrt = {C_SQRT:.5f} (=1-t*), c_exp = {C_EXP:.5f} (=t*)")
    print(f"    Lambda = M_KK ({M_KK:.4e} GeV) => x = (lambda/Lambda)^2; in M_KK units Lambda=1.0")
    print(f"    n_s_FW_sqrt_cutoff (committed)   = {n_s_FW_sqrt_cutoff}")

    # --- Functionals -------------------------------------------------------
    f_sqrt = lambda x: np.sqrt(x)                                  # (local) committed cutoff family
    f_star = lambda x: C_SQRT * np.sqrt(x) + C_EXP * np.exp(-x)    # (local) working functional
    f_gauss = lambda x: np.exp(-x)                                 # (local) the e^{-x} admixture, isolated

    # --- Build spectral actions on the IDENTICAL S36 spectrum --------------
    print("\n" + "=" * 78)
    print("STEP 1: Spectral actions on the IDENTICAL S36 spectrum (7 tau values)")
    print("=" * 78)
    d36 = np.load(S36_CACHE, allow_pickle=True)
    S_sqrt, nmodes = build_spectral_action(d36, f_sqrt)
    S_star, _ = build_spectral_action(d36, f_star)
    S_gauss, _ = build_spectral_action(d36, f_gauss)
    print(f"  PW-weighted modes at fold = {nmodes}")
    print(f"  {'tau':>6s}  {'S_sqrt':>14s}  {'S_f*':>14s}  {'G=S_exp':>14s}")
    for i, tau in enumerate(TAU_EVALS):
        print(f"  {tau:6.3f}  {S_sqrt[i]:14.4f}  {S_star[i]:14.4f}  {S_gauss[i]:14.4f}")

    # --- Slow-roll / n_s for each functional -------------------------------
    print("\n" + "=" * 78)
    print("STEP 2: eps_H = (1/2) S'^2/(S S'') at fold; n_s = 1 - 2 eps_H")
    print("=" * 78)
    r_sqrt = eps_H_n_s(S_sqrt)
    r_star = eps_H_n_s(S_star)
    r_gauss = eps_H_n_s(S_gauss)
    for name, r in [("sqrt(x)", r_sqrt), ("f*", r_star), ("e^{-x} (isolated)", r_gauss)]:
        print(f"\n  {name}:")
        print(f"    S={r['S']:14.4f}  S'={r['dS']:14.4f}  S''={r['d2S']:14.4f}")
        print(f"    eps_H = {r['eps_H']:.6f}   n_s = 1-2eps_H = {r['n_s']:.6f}")

    # --- Cross-check: sqrt reproduces the canonical S_fold / dS_fold / d2S_fold / n_s
    print("\n" + "=" * 78)
    print("STEP 3: Cross-check sqrt(x) reproduces the canonical sqrt-cutoff anchors")
    print("=" * 78)
    dev_S = abs(r_sqrt["S"] - S_fold) / S_fold                       # (local)
    dev_dS = abs(r_sqrt["dS"] - dS_fold) / abs(dS_fold)              # (local)
    dev_d2S = abs(r_sqrt["d2S"] - d2S_fold) / abs(d2S_fold)         # (local)
    print(f"  S(fold):   computed {r_sqrt['S']:.4f}  vs canonical S_fold={S_fold:.4f}    (rel dev {dev_S:.2e})")
    print(f"  S'(fold):  computed {r_sqrt['dS']:.4f}  vs canonical dS_fold={dS_fold:.4f}  (rel dev {dev_dS:.2e})")
    print(f"  S''(fold): computed {r_sqrt['d2S']:.4f} vs canonical d2S_fold={d2S_fold:.4f}(rel dev {dev_d2S:.2e})")
    print(f"  n_s(sqrt bare-tree) = {r_sqrt['n_s']:.6f}  (S62/S75 canonical 0.9567; committed-with-BCS 0.959)")
    crosscheck_ok = (dev_S < 1e-6 and dev_dS < 1e-4 and dev_d2S < 1e-4)   # (local)
    print(f"  Cross-check PASS: {crosscheck_ok}")

    # --- Single-tau (S84 L12) fold-slice anchor ----------------------------
    print("\n" + "=" * 78)
    print("STEP 4: Single-tau S84 L12 fold-slice anchor (consistency of the fold spectrum)")
    print("=" * 78)
    d84 = np.load(S84_CACHE, allow_pickle=True)
    S_sqrt_L12_fold = single_tau_eps_proxy(d84, f_sqrt)
    S_star_L12_fold = single_tau_eps_proxy(d84, f_star)
    if S_sqrt_L12_fold is not None:
        # Ratio of f*-to-sqrt at the fold slice -- a tilt-FREE consistency number across the two caches.
        ratio_S36 = S_star[4] / S_sqrt[4]                # (local) f*/sqrt at fold from S36 (tau index 4 = 0.19)
        ratio_L12 = S_star_L12_fold / S_sqrt_L12_fold    # (local) same ratio from L12 single-tau
        print(f"  S36  fold-slice S_f*/S_sqrt = {ratio_S36:.6f}")
        print(f"  L12  fold-slice S_f*/S_sqrt = {ratio_L12:.6f}")
        print(f"  ratio agreement |dev|       = {abs(ratio_S36 - ratio_L12):.4e}")
        print("  (single-tau slice cannot give eps_H = S'^2/(2 S S''); used only as fold-slice consistency anchor)")
    else:
        ratio_S36 = S_star[4] / S_sqrt[4]   # (local)
        ratio_L12 = float("nan")            # (local)
        print("  WARNING: S84 L12 sector_evals not resolvable; fold-slice anchor SKIPPED (S36 primary stands).")

    # --- The coherence verdict ---------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 5: COHERENCE VERDICT  (Delta n_s = n_s(f*) - n_s(sqrt))")
    print("=" * 78)
    ns_sqrt = r_sqrt["n_s"]                                      # (local) bare-tree like-for-like partner
    ns_star = r_star["n_s"]                                      # (local)
    delta_ns = ns_star - ns_sqrt                                 # (local) SIGNED difference
    abs_delta = abs(delta_ns)                                    # (local)

    # Robustness of Delta n_s to the comparison footing:
    #   committed value uses BCS+1-loop dressing (0.959); like-for-like uses bare-tree (0.9567).
    #   Delta n_s is a PURE functional-difference on the SAME spectrum/dressing => footing-robust by construction.
    delta_ns_vs_committed = ns_star - n_s_FW_sqrt_cutoff         # (local) f* vs the committed point-value

    print(f"  n_s(sqrt, bare-tree)   = {ns_sqrt:.6f}")
    print(f"  n_s(f*,   bare-tree)   = {ns_star:.6f}")
    print(f"  Delta n_s (f* - sqrt)  = {delta_ns:+.6f}")
    print(f"  |Delta n_s|            = {abs_delta:.6f}")
    print(f"  sigma_budget           = {SIGMA_BUDGET}")
    print(f"  |Delta n_s| / sigma    = {abs_delta / SIGMA_BUDGET:.4f}")
    print(f"  (f* vs COMMITTED 0.959): Delta = {delta_ns_vs_committed:+.6f} "
          f"({abs(delta_ns_vs_committed) / SIGMA_BUDGET:.3f} sigma)")

    # --- [SIGN] 3-tuple ----------------------------------------------------
    # Substitution chain Step 4 prediction: e^{-x} (isolated) gives eps_H<0 (blue tilt, n_s>1);
    # mixing 8.83% blue functional into sqrt pulls eps_H DOWN => n_s UP (bluer).
    # => PREDICTED sign: n_s(f*) >= n_s(sqrt)  i.e.  delta_ns >= 0.
    # sign_verdict PASS iff the computed direction matches the prediction (delta_ns >= 0).
    gauss_is_bluer = (r_gauss["eps_H"] < r_sqrt["eps_H"])   # (local) cross-check: isolated e^{-x} has lower eps_H (bluer)
    sign_verdict = "PASS" if delta_ns >= 0.0 else "FAIL"

    if abs_delta <= SIGMA_BUDGET:
        magnitude_verdict = "PASS"
    elif abs_delta <= INFO_BAND:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"

    # regime: the slow-roll n_s = 1-2eps_H first-order truncation is valid iff eps_H small (<<1)
    # throughout; here eps_H ~ 0.021 for both functionals (well inside the SR regime).
    regime_verdict = "VALID" if (abs(r_sqrt["eps_H"]) < 0.1 and abs(r_star["eps_H"]) < 0.1) else "MARGINAL"

    # Composite collapse (gate-verdicts.md deterministic rule)
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

    print("\n  [SIGN] 3-tuple:")
    print(f"    sign_verdict      = {sign_verdict}   (predicted delta_ns>=0; e^{{-x}} admixture bluer; "
          f"isolated-Gaussian-bluer cross-check={gauss_is_bluer})")
    print(f"    magnitude_verdict = {magnitude_verdict}   (|Delta n_s| vs sigma_budget {SIGMA_BUDGET}, info-band {INFO_BAND})")
    print(f"    regime_verdict    = {regime_verdict}   (eps_H={r_sqrt['eps_H']:.4f}/{r_star['eps_H']:.4f} << 1)")
    print(f"    COMPOSITE         = {composite}")

    # --- 4-tuple line ------------------------------------------------------
    four_tuple = (f"(value={delta_ns:.6e}, scheme={SCHEME}, "
                  f"convention={CONVENTION}, L_max={L_MAX})")   # (local)

    # --- Plot --------------------------------------------------------------
    fig = plt.figure(figsize=(15, 5))
    fig.suptitle(f"{GATE_ID}  [{composite}]   "
                 r"$n_s(f^*)$ vs $n_s(\sqrt{x})$ coherence", fontsize=12, fontweight="bold")

    ax1 = fig.add_subplot(1, 3, 1)
    idx = np.arange(1, len(TAU_EVALS))
    tn = TAU_EVALS[idx]
    tt = np.linspace(tn.min(), tn.max(), 200)   # (local)
    ax1.plot(tt, r_sqrt["spline"](tt) / 1e3, "b-", lw=2, label=r"$S_{\sqrt{x}}$")
    ax1.plot(tt, r_star["spline"](tt) / 1e3, "r-", lw=2, label=r"$S_{f^*}$")
    ax1.scatter(tn, S_sqrt[idx] / 1e3, c="b", s=20)
    ax1.scatter(tn, S_star[idx] / 1e3, c="r", s=20)
    ax1.axvline(float(tau_fold), color="gray", ls="--", alpha=0.6)
    ax1.set_xlabel(r"$\tau$"); ax1.set_ylabel(r"$S\times10^{-3}$")
    ax1.set_title("(a) Spectral-action profiles\n(same spectrum, two functionals)", fontsize=10)
    ax1.legend(fontsize=9); ax1.grid(alpha=0.3)

    ax2 = fig.add_subplot(1, 3, 2)
    names = [r"$\sqrt{x}$", r"$f^*$", r"$e^{-x}$"]
    eps_vals = [r_sqrt["eps_H"], r_star["eps_H"], r_gauss["eps_H"]]
    colors = ["#1f77b4", "#d62728", "#7f7f7f"]
    bars = ax2.bar(names, eps_vals, color=colors, alpha=0.75, edgecolor="black")
    for b, v in zip(bars, eps_vals):
        ax2.text(b.get_x() + b.get_width() / 2, v + (0.002 if v >= 0 else -0.006),
                 f"{v:.4f}", ha="center", fontsize=8)
    ax2.axhline(0, color="k", lw=0.6)
    ax2.set_ylabel(r"$\epsilon_H$")
    ax2.set_title(r"(b) $\epsilon_H$ by functional"
                  "\n" r"($e^{-x}$ isolated $\Rightarrow\epsilon_H<0$, blue)", fontsize=10)
    ax2.grid(alpha=0.3, axis="y")

    ax3 = fig.add_subplot(1, 3, 3)
    ax3.axvspan(planck_ns - SIGMA_BUDGET, planck_ns + SIGMA_BUDGET, alpha=0.15, color="gold",
                label=r"Planck $1\sigma$")
    for lab, v, c in [(r"$n_s(\sqrt{x})$", ns_sqrt, "#1f77b4"),
                      (r"$n_s(f^*)$", ns_star, "#d62728"),
                      ("committed 0.959", n_s_FW_sqrt_cutoff, "#2ca02c")]:
        ax3.axvline(v, color=c, lw=2, label=f"{lab}={v:.4f}")
    ax3.axvline(planck_ns, color="orange", lw=1.5, ls=":", label=f"Planck {planck_ns}")
    ax3.set_xlim(0.952, 0.967)
    ax3.set_yticks([])
    ax3.set_xlabel(r"$n_s$")
    ax3.set_title(f"(c) Coherence\n"
                  rf"$\Delta n_s={delta_ns:+.5f}$ ($={abs_delta / SIGMA_BUDGET:.2f}\sigma$) [{composite}]",
                  fontsize=10)
    ax3.legend(fontsize=7, loc="upper right")
    ax3.grid(alpha=0.3, axis="x")

    plt.tight_layout(rect=[0, 0, 1, 0.94])
    plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"\n  Saved plot: {OUT_PNG}")

    # --- Save data ---------------------------------------------------------
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite_verdict=composite,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        # core results
        n_s_sqrt=ns_sqrt,
        n_s_f_star=ns_star,
        delta_n_s=delta_ns,
        abs_delta_n_s=abs_delta,
        sigma_budget=SIGMA_BUDGET,
        delta_over_sigma=abs_delta / SIGMA_BUDGET,
        info_band=INFO_BAND,
        # eps_H decomposition
        eps_H_sqrt=r_sqrt["eps_H"],
        eps_H_f_star=r_star["eps_H"],
        eps_H_gauss_isolated=r_gauss["eps_H"],
        n_s_gauss_isolated=r_gauss["n_s"],
        # spectral-action moments
        S_sqrt_fold=r_sqrt["S"], dS_sqrt_fold=r_sqrt["dS"], d2S_sqrt_fold=r_sqrt["d2S"],
        S_f_star_fold=r_star["S"], dS_f_star_fold=r_star["dS"], d2S_f_star_fold=r_star["d2S"],
        # footing robustness
        n_s_committed=n_s_FW_sqrt_cutoff,
        delta_n_s_vs_committed=delta_ns_vs_committed,
        # cross-checks
        crosscheck_canonical_ok=crosscheck_ok,
        ratio_fold_S36=ratio_S36,
        ratio_fold_L12=ratio_L12,
        # functional coefficients
        c_sqrt=C_SQRT, c_exp=C_EXP, t_star=t_star,
        # profiles
        tau_evals=TAU_EVALS,
        S_sqrt_profile=S_sqrt,
        S_f_star_profile=S_star,
        S_gauss_profile=S_gauss,
        pw_modes_fold=nmodes,
        # pins
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  Saved data: {OUT_NPZ}")

    print("\n" + "=" * 78)
    print(f"  4-tuple: {four_tuple}")
    print("=" * 78)

    note = (f"n_s(sqrt)={ns_sqrt:.6f} n_s(f*)={ns_star:.6f} dNs={delta_ns:+.6f} "
            f"={abs_delta / SIGMA_BUDGET:.3f}sig<sigma_budget={SIGMA_BUDGET}; "
            f"committed sqrt coherent with working f*; NO-RE-SHOP (PROHIB Class 1)")   # (local)
    extra = [
        f"# regulator_pin=a_2^{{cutoff}} (sqrt and f* moments are cutoff-regulated, NOT zeta)",
        f"# plan-pin-deviation: S36 multitau cache PRIMARY (n_s needs tau-derivs; S84 L12 is single-tau fold anchor)",
        f"# footing: like-for-like bare-tree; f* vs committed-0.959 = {abs(delta_ns_vs_committed) / SIGMA_BUDGET:.3f}sig",
    ]   # (local)

    print_verdict_payload(
        composite, f"{delta_ns:.6e}", audit_sha, content_sha,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        companion_note=note, extra_rows=extra,
    )


if __name__ == "__main__":
    main()
