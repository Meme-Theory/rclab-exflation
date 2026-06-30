#!/usr/bin/env python3
"""
S84 W5-54 -- K-FLOOR-REGULATOR-INVARIANCE
==========================================

Gate: S84-K-FLOOR-REGULATOR-INVARIANCE   ([VERIFY] [AUDIT])
Agent: volovik-superfluid-universe-theorist
Classification: GEOMETRIC (regulator-layer independence of the K-family
  positivity floor; tests whether the S83 G38 K-matching basin K_R5=1.922
  is structural or a Zubarev-specific artifact).

Pre-registered threshold (plan L134-L140, verbatim):
  PASS: |K_R5(Zubarev) - K_R5(zeta)| / K_R5(Zubarev) <= 0.02
        AND both values >= 1 (positivity).
  FAIL: ratio >= 0.10 OR either value < 1 (WALL crossed in one regulator).
  INFO: 0.02 < ratio < 0.10 (weak regulator-dependence).

Scan: K in [0.5, 3.0], log-uniform, 26 points (plan L151; Delta ln K=0.0717).
  Note: plan writes "Delta ln K = 0.1 (26 points)" but 0.1 over [ln 0.5, ln 3]
  yields only 18 points. The faithful resolution is 26 LOG-UNIFORM points
  covering the full range; the effective Delta ln K = 0.07167, a minor
  cosmetic tightening documented here for audit trail.

SUBSTITUTION CHAIN [VERIFY] [AUDIT]
------------------------------------
Step 1 (definitions):
  f_zeta(lam)  := 1                            (zeta regulator, flat weight)
  f_Zub(lam)   := exp(-lam^2 / M_KK^2)          (Zubarev Gaussian mollifier)
  S_R_E        := sum_{k} d_k * f_R(lam_k) * lam_k   (energy-weighted first moment)
  xi(R)        := S_R_E / S_zeta_E
  A_s_base(R)  := A_s_W1_2 * xi(R)             [W1-2 TD baseline * regulator dressing]
  A_s(K; R)    := A_s_base(R) * K              [R5 linear-response map, S82 sec V.7]
  K_match(R)   := A_s_Planck / A_s_base(R)      [dial needed to hit Planck]
  K_R5(R)      := K-value under R5 convention such that A_s_base(R)*K = A_s_Planck
                  = K_match(R)
               (K_R5 interpretation: the 'floor' under R5 is the K that lands the
                linear-response curve on the Planck amplitude; the 'positivity floor'
                A_s >= 0 is automatically satisfied for all K > 0.)

Step 2 (substitution at L_max=5, SV1 anchor):
  xi(zeta)     = 1.000000 (flat; identity)
  xi(Zubarev)  = S_Zub_E / S_zeta_E  (Python-computed from L=5 spectrum cache)
                 From S84 W1a SV1: xi_E = 0.019646 (verified below).
  A_s_W1_2     = 3.299e-9  (S82 W1-2 TD-branch)
  A_s_Planck   = 2.10e-9   (canonical_constants.A_s_CMB)
  A_s_base(zeta)    = 3.299e-9 * 1.000000 = 3.299e-9
  A_s_base(Zubarev) = 3.299e-9 * 0.019646 = 6.482e-11
  K_match(zeta)     = 2.10e-9 / 3.299e-9   = 0.6366
  K_match(Zubarev)  = 2.10e-9 / 6.482e-11  = 32.39

Step 3 (simplification):
  |K_R5(Zubarev) - K_R5(zeta)| / K_R5(Zubarev)
    = |32.39 - 0.6366| / 32.39
    = 31.76 / 32.39
    = 0.9804

Step 4 (direction from canonical form):
  xi(Zubarev) < 1 (Gaussian mollifier strictly suppresses every lam > 0).
  => A_s_base(Zubarev) < A_s_base(zeta).
  => K_match(Zubarev) > K_match(zeta).
  => K_R5(Zubarev) differs from K_R5(zeta) by a factor 1/xi(Zubarev) ~ 50.
  => ratio >> 0.10 FAIL threshold.

  SECONDARY positivity check:
  K_match(zeta) = 0.6366 < 1   => K_R5(zeta) < 1, POSITIVITY WALL CROSSED.
  K_match(Zubarev) = 32.4 > 1  => K_R5(Zubarev) >> 1, POSITIVITY RESPECTED.
  Per plan FAIL clause: "either value < 1 (WALL crossed in one regulator)"
  => K_R5(zeta) = 0.6366 triggers the FAIL clause INDEPENDENTLY.

Predicted verdict: FAIL (TWO independent grounds).
Structural consequence: S83 G38 K_match = 0.6366 WALL is REGULATOR-SPECIFIC
  (zeta-only artifact). Under Zubarev the K-match shifts to 32.4, far above
  unity, so the "corridor K-cluster at K ~ 2 over-shoots Planck" statement
  is zeta-convention-specific.

Cross-checks (CC1-CC5):
  CC1 xi(zeta) == 1 exactly                       (flat-weight identity)
  CC2 xi(Zubarev) ~ 0.0196 matches SV1 anchor     (S84 W1a ref 0.019646)
  CC3 K_match(R) * A_s_base(R) = A_s_Planck       (machine epsilon)
  CC4 Torch vs numpy first-moment cross-check     (GPU path sanity)
  CC5 K-scan monotonicity: A_s(K;R) is linear in K, so PASS/FAIL is
      independent of where within [0.5, 3.0] we probe.

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py
  - s74_spectrum_cache_L9_tau019.npz (spectral cache, L=9 available; filter L<=5)
  - s83_w3_g38_k_matching_5_conventions.py (pre-registered K_R5=1.922 basin)
  - s82_w1_2_unified_as_79_full.npz (A_s_W1_2 TD baseline)
  - this script (self-pin)

Output:
  - s84_w5_54_data.npz
  - s84_w5_54_plot.png (K_R5 vs regulator with 0.02 RATIO band + K-scan curves)
  - verdict line appended to s84_gate_verdicts.txt
"""
from __future__ import annotations

# -----------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# -----------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import hashlib
import json
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import (
    A_s_CMB,        # 2.1e-9 (Planck 2018 scalar amplitude)
    M_KK,           # mass scale, 1.0 in M_KK units
    tau_fold,       # 0.19
)

# -----------------------------------------------------------------------------
# Section 2 -- Pre-registered parameters
# -----------------------------------------------------------------------------
SESSION     = "S84"                                                  # (local)
GATE_ID     = "S84-K-FLOOR-REGULATOR-INVARIANCE"                     # (local)
SCHEME_OUT  = "Zubarev-vs-zeta"                                      # (local)
CONVENTION  = "R5"                                                   # (local) Bogoliubov-primary B2
L_MAX       = 5                                                      # (local) plan pin
RANDOM_SEED = 42                                                     # (local) plan pin

PASS_TOL    = 0.02                                                   # (local) plan PASS threshold
FAIL_TOL    = 0.10                                                   # (local) plan FAIL threshold

A_s_W1_2_TD = 3.299e-9                                               # (local) S82 W1-2 TD-branch anchor
A_s_PLANCK  = A_s_CMB                                                # canonical
K_R5_PREREG = 1.922                                                  # (local) Landau V.1 / S83 G38 anchor
SV1_XI_E_REF = 0.019646                                              # (local) S84 W1a SV1 anchor

# Scan K in [0.5, 3.0], log-uniform 26 points (plan L151).
# Plan literal also says Delta ln K = 0.1; reconciled as 26-pt log-uniform
# over [0.5, 3.0] with effective d(ln K) = 0.07167. Full-range > step-fidelity.
K_SCAN_LO   = 0.5                                                    # (local) plan pin
K_SCAN_HI   = 3.0                                                    # (local) plan pin
N_SCAN      = 26                                                     # (local) plan pin

# -----------------------------------------------------------------------------
# Section 3 -- Paths
# -----------------------------------------------------------------------------
OUT_NPZ       = SCRIPT_DIR / "s84_w5_54_data.npz"
OUT_PNG       = SCRIPT_DIR / "s84_w5_54_plot.png"
VERDICT_TXT   = SCRIPT_DIR / "s84_gate_verdicts.txt"

SPECTRUM_CACHE = SCRIPT_DIR / "s74_spectrum_cache_L9_tau019.npz"
S83_G38_SCRIPT = SCRIPT_DIR / "s83_w3_g38_k_matching_5_conventions.py"
S83_G38_NPZ    = SCRIPT_DIR / "s83_w3_g38_k_matching_5_conventions.npz"
S82_W12_NPZ    = SCRIPT_DIR / "s82_w1_2_unified_as_79_full.npz"
CANONICAL_PY   = SCRIPT_DIR / "canonical_constants.py"
SELF_PATH      = SCRIPT_DIR / "s84_w5_k_floor_regulator_invariance.py"

INPUT_FILES = [
    CANONICAL_PY,
    SPECTRUM_CACHE,
    S83_G38_SCRIPT,
    S83_G38_NPZ,
    S82_W12_NPZ,
    SELF_PATH,
]


# -----------------------------------------------------------------------------
# Section 4 -- SHA-256 input pinning
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print("=" * 78)
    print(f"{GATE_ID} -- input SHA-256 pins")
    print("=" * 78)
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)
        short = sha[:16] if sha else "MISSING"                     # (local)
        print(f"  {rel}: {short}")
        pins[rel] = sha
    return pins


def closure_hash(pins_and_params: dict) -> str:
    items = sorted(pins_and_params.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# -----------------------------------------------------------------------------
# Section 5 -- Regulator weight functions (S83 canonical)
# -----------------------------------------------------------------------------
def weight_zeta(lam: np.ndarray) -> np.ndarray:
    """zeta regulator: flat weight = 1 (S83 G3 axiomatic / S83 W1-G1)."""
    return np.ones_like(lam, dtype=np.float64)


def weight_zubarev(lam: np.ndarray, Lambda_Z: float = 1.0) -> np.ndarray:
    """Zubarev Gaussian mollifier exp(-lam^2/Lambda_Z^2) (S83 W1-G1, M_KK units)."""
    return np.exp(-(lam / Lambda_Z) ** 2)


def spectral_moment_E(flat_lambdas: np.ndarray,
                       flat_mults: np.ndarray,
                       weight_fn) -> float:
    """Energy-weighted spectral first moment: sum_k d_k * f(lam_k) * lam_k.

    This is the canonical S_R_E from S83 W3-G51 and S84 W1a SV1/SV2.
    """
    return float((flat_mults * weight_fn(flat_lambdas) * flat_lambdas).sum())


# -----------------------------------------------------------------------------
# Section 6 -- Spectrum loading (filter L_max = 5)
# -----------------------------------------------------------------------------
def build_flat_spectrum(L_max_target: int):
    cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
    sector_evals = cache['sector_evals'].item()
    cache.close()
    flat_lambdas, flat_mults = [], []
    for (p, q), info in sector_evals.items():
        if info['level'] > L_max_target:
            continue
        dim = int(info['dim'])
        for lam in info['abs_evals']:
            flat_lambdas.append(float(lam))
            flat_mults.append(dim)
    return (np.asarray(flat_lambdas, dtype=np.float64),
            np.asarray(flat_mults,   dtype=np.float64))


# -----------------------------------------------------------------------------
# Section 7 -- Main
# -----------------------------------------------------------------------------
def main() -> int:
    np.random.seed(RANDOM_SEED)

    pins = log_input_pins(INPUT_FILES)
    print()

    # --- Section 7.1: Load spectrum, build regulator-dressed baselines ---
    print("-" * 78)
    print("Section 7.1: Spectrum load + regulator baselines")
    print("-" * 78)
    lam, mult = build_flat_spectrum(L_MAX)
    print(f"  L_max             = {L_MAX}")
    print(f"  n_modes (flat)    = {len(lam)}")
    print(f"  sum(d_k)          = {int(mult.sum())}")
    print(f"  lam range         = [{lam.min():.4e}, {lam.max():.4e}] M_KK")
    print()

    # Energy-weighted first moments
    S_zeta_E = spectral_moment_E(lam, mult, weight_zeta)             # (local)
    S_Zub_E  = spectral_moment_E(lam, mult, weight_zubarev)          # (local)
    xi_zeta    = 1.0                                                 # (local) identity
    xi_Zubarev = S_Zub_E / S_zeta_E                                  # (local)

    # CC4: torch vs numpy cross-check on first moment (GPU path sanity)
    try:
        import torch
        device = 'cuda' if torch.cuda.is_available() else 'cpu'      # (local)
        lam_t  = torch.tensor(lam, dtype=torch.float64, device=device)
        mult_t = torch.tensor(mult, dtype=torch.float64, device=device)
        w_zub_t = torch.exp(-(lam_t / 1.0) ** 2)
        S_Zub_E_t = float(((mult_t * w_zub_t) * lam_t).sum().cpu().item())
        cc4_abs = abs(S_Zub_E - S_Zub_E_t)                            # (local)
        cc4_rel = cc4_abs / abs(S_Zub_E) if S_Zub_E != 0 else float('inf')  # (local)
        cc4_ok  = cc4_rel < 1e-10                                     # (local)
        print(f"  [CC4 torch-vs-numpy first-moment check, device={device}]")
        print(f"    numpy   S_Zub_E = {S_Zub_E:.10e}")
        print(f"    torch   S_Zub_E = {S_Zub_E_t:.10e}")
        print(f"    |diff|  = {cc4_abs:.3e}, rel = {cc4_rel:.3e}, ok = {cc4_ok}")
    except Exception as e:
        cc4_ok = None                                                 # (local)
        cc4_rel = None                                                # (local)
        print(f"  [CC4] torch unavailable or failed ({e}); numpy-only path.")
    print()

    print(f"  S_zeta_E       = {S_zeta_E:.6f}")
    print(f"  S_Zubarev_E    = {S_Zub_E:.6f}")
    print(f"  xi(zeta)       = {xi_zeta:.6f}   (identity)")
    print(f"  xi(Zubarev)    = {xi_Zubarev:.6e}   (ref SV1: {SV1_XI_E_REF:.6e})")
    # CC2: SV1 anchor agreement
    cc2_diff = abs(xi_Zubarev - SV1_XI_E_REF)                        # (local)
    cc2_ok   = cc2_diff < 1e-4                                       # (local)
    print(f"  [CC2] SV1 xi_E anchor check: |diff| = {cc2_diff:.3e}, ok = {cc2_ok}")
    print()

    # --- Section 7.2: A_s_base(R) and K_match(R) ---
    print("-" * 78)
    print("Section 7.2: A_s_base and K_match per regulator")
    print("-" * 78)
    A_s_base_zeta    = A_s_W1_2_TD * xi_zeta                         # (local)
    A_s_base_Zubarev = A_s_W1_2_TD * xi_Zubarev                      # (local)
    K_match_zeta     = A_s_PLANCK / A_s_base_zeta                    # (local)
    K_match_Zubarev  = A_s_PLANCK / A_s_base_Zubarev                 # (local)

    # Under the R5 convention the "K-floor" under regulator R is the K that
    # lands the linear-response A_s on Planck: K_R5(R) = K_match(R).
    K_R5_zeta    = K_match_zeta                                      # (local)
    K_R5_Zubarev = K_match_Zubarev                                   # (local)

    print(f"  A_s_W1_2_TD    = {A_s_W1_2_TD:.4e}  (S82 TD-branch)")
    print(f"  A_s_Planck     = {A_s_PLANCK:.4e}   (canonical)")
    print(f"  A_s_base(zeta)    = {A_s_base_zeta:.4e}")
    print(f"  A_s_base(Zubarev) = {A_s_base_Zubarev:.4e}")
    print(f"  K_match(zeta)     = {K_match_zeta:.6f}")
    print(f"  K_match(Zubarev)  = {K_match_Zubarev:.6f}")
    print()

    # CC3: K_match(R) * A_s_base(R) == A_s_Planck  (identity)
    cc3_zeta = abs(K_match_zeta * A_s_base_zeta - A_s_PLANCK)        # (local)
    cc3_Zub  = abs(K_match_Zubarev * A_s_base_Zubarev - A_s_PLANCK)  # (local)
    cc3_ok   = (cc3_zeta < 1e-20) and (cc3_Zub < 1e-20)              # (local)
    print(f"  [CC3] identity check: max|K*A_base - Planck| = "
          f"{max(cc3_zeta, cc3_Zub):.3e}, ok = {cc3_ok}")
    print()

    # --- Section 7.3: The K-scan over [0.5, 3.0] ---
    print("-" * 78)
    print("Section 7.3: K-scan (log-uniform 26 points in [0.5, 3.0])")
    print("-" * 78)
    K_scan = np.exp(np.linspace(np.log(K_SCAN_LO),
                                 np.log(K_SCAN_HI),
                                 N_SCAN))                              # (local)
    dlnK = np.log(K_scan[1]) - np.log(K_scan[0])                      # (local)
    print(f"  n_points      = {len(K_scan)}")
    print(f"  K range       = [{K_scan[0]:.4f}, {K_scan[-1]:.4f}]")
    print(f"  d(ln K) eff   = {dlnK:.5f}  (plan text '0.1' -> log-uniform over full range yields {dlnK:.5f})")
    A_s_scan_zeta    = A_s_base_zeta    * K_scan                     # (local)
    A_s_scan_Zubarev = A_s_base_Zubarev * K_scan                     # (local)
    # Planck-match K under each regulator within the scan
    def interp_K_for_Planck(K_arr, A_s_arr):
        logK = np.log(K_arr); logA = np.log(A_s_arr)
        tgt = np.log(A_s_PLANCK)
        if tgt < logA.min() or tgt > logA.max():
            return None
        return float(np.exp(np.interp(tgt, logA, logK)))
    K_match_zeta_scan    = interp_K_for_Planck(K_scan, A_s_scan_zeta)     # (local)
    K_match_Zubarev_scan = interp_K_for_Planck(K_scan, A_s_scan_Zubarev)  # (local)
    print(f"  K_match(zeta)    within scan: {K_match_zeta_scan}")
    print(f"  K_match(Zubarev) within scan: {K_match_Zubarev_scan}")
    # CC5: linearity -> A_s(K)/A_s(K') = K/K' exactly
    cc5_ratio_zeta = (A_s_scan_zeta[-1] / A_s_scan_zeta[0]) / (K_scan[-1]/K_scan[0])  # (local)
    cc5_ratio_Zub  = (A_s_scan_Zubarev[-1] / A_s_scan_Zubarev[0]) / (K_scan[-1]/K_scan[0])  # (local)
    cc5_ok = (abs(cc5_ratio_zeta - 1) < 1e-12) and (abs(cc5_ratio_Zub - 1) < 1e-12)   # (local)
    print(f"  [CC5] linearity: zeta ratio deviation = {cc5_ratio_zeta - 1:.2e}, "
          f"Zub = {cc5_ratio_Zub - 1:.2e}, ok = {cc5_ok}")
    print()

    # --- Section 7.4: Verdict computation ---
    print("-" * 78)
    print("Section 7.4: Verdict")
    print("-" * 78)
    abs_diff      = abs(K_R5_Zubarev - K_R5_zeta)                    # (local)
    max_rel_span  = abs_diff / max(abs(K_R5_Zubarev), 1e-30)         # (local)
    max_rel_span_sym = abs_diff / max(abs(K_R5_zeta), abs(K_R5_Zubarev))  # (local) sym check

    positivity_zeta    = K_R5_zeta    >= 1.0                         # (local)
    positivity_Zubarev = K_R5_Zubarev >= 1.0                         # (local)
    positivity_all     = positivity_zeta and positivity_Zubarev      # (local)

    # Plan verdict logic (verbatim):
    # PASS: ratio <= 0.02 AND both values >= 1
    # FAIL: ratio >= 0.10 OR either value < 1
    # INFO: 0.02 < ratio < 0.10
    if (max_rel_span <= PASS_TOL) and positivity_all:
        verdict = "PASS"
    elif (max_rel_span >= FAIL_TOL) or (not positivity_all):
        verdict = "FAIL"
    else:
        verdict = "INFO"

    print(f"  |K_R5(Zub) - K_R5(zeta)|  = {abs_diff:.6f}")
    print(f"  / K_R5(Zub)               = {max_rel_span:.6f}")
    print(f"  K_R5(zeta)    >= 1 ?       = {positivity_zeta}   ({K_R5_zeta:.4f})")
    print(f"  K_R5(Zubarev) >= 1 ?       = {positivity_Zubarev}   ({K_R5_Zubarev:.4f})")
    print(f"  PASS threshold (rel<=0.02) = {PASS_TOL}")
    print(f"  FAIL threshold (rel>=0.10) = {FAIL_TOL}")
    print(f"  -> verdict = {verdict}")
    print()

    # --- Section 7.5: Comparison to S83 G38 K_match WALL ---
    g38_K_match = A_s_PLANCK / A_s_W1_2_TD                           # (local) 0.6366
    print(f"  [CF-G38] S83 G38 K_match_WALL = {g38_K_match:.4f}")
    print(f"          K_match(zeta)   = {K_match_zeta:.4f}  "
          f"(diff from G38: {K_match_zeta - g38_K_match:.3e})")
    print(f"          K_match(Zubarev) = {K_match_Zubarev:.4f}  "
          f"(dressed by 1/xi_Zub = {1.0/xi_Zubarev:.2f}x)")
    print(f"  S83 G38 WALL (0.6366) corresponds to zeta-regulator. Under Zubarev,")
    print(f"  the wall moves to {K_match_Zubarev:.2f} M_KK units -- regulator-dependent.")
    print()

    # --- Section 7.6: Closure SHA ---
    print("-" * 78)
    print("Section 7.6: Closure SHA-256")
    print("-" * 78)
    closure_map = dict(pins)                                         # (local)
    closure_map.update({
        "L_max":              L_MAX,
        "scheme":             SCHEME_OUT,
        "convention":         CONVENTION,
        "K_scan_lo":          K_SCAN_LO,
        "K_scan_hi":          K_SCAN_HI,
        "n_scan":             N_SCAN,
        "A_s_W1_2_TD":        f"{A_s_W1_2_TD:.10e}",
        "A_s_Planck":         f"{A_s_PLANCK:.10e}",
        "S_zeta_E":           f"{S_zeta_E:.10e}",
        "S_Zub_E":            f"{S_Zub_E:.10e}",
        "xi_zeta":            f"{xi_zeta:.10e}",
        "xi_Zubarev":         f"{xi_Zubarev:.10e}",
        "K_R5_zeta":          f"{K_R5_zeta:.10e}",
        "K_R5_Zubarev":       f"{K_R5_Zubarev:.10e}",
        "max_rel_span":       f"{max_rel_span:.10e}",
        "positivity_zeta":    int(positivity_zeta),
        "positivity_Zubarev": int(positivity_Zubarev),
        "verdict":            verdict,
        "PASS_TOL":           PASS_TOL,
        "FAIL_TOL":           FAIL_TOL,
        "random_seed":        RANDOM_SEED,
    })
    closure_sha = closure_hash(closure_map)
    print(f"  closure_sha = {closure_sha}")
    print()

    # --- Section 7.7: Save NPZ ---
    print("-" * 78)
    print("Section 7.7: Save artifacts")
    print("-" * 78)
    np.savez(OUT_NPZ,
             L_max=L_MAX,
             lam=lam,
             mult=mult,
             S_zeta_E=S_zeta_E,
             S_Zub_E=S_Zub_E,
             xi_zeta=xi_zeta,
             xi_Zubarev=xi_Zubarev,
             A_s_W1_2_TD=A_s_W1_2_TD,
             A_s_Planck=A_s_PLANCK,
             A_s_base_zeta=A_s_base_zeta,
             A_s_base_Zubarev=A_s_base_Zubarev,
             K_match_zeta=K_match_zeta,
             K_match_Zubarev=K_match_Zubarev,
             K_R5_zeta=K_R5_zeta,
             K_R5_Zubarev=K_R5_Zubarev,
             K_scan=K_scan,
             A_s_scan_zeta=A_s_scan_zeta,
             A_s_scan_Zubarev=A_s_scan_Zubarev,
             abs_diff=abs_diff,
             max_rel_span=max_rel_span,
             max_rel_span_sym=max_rel_span_sym,
             positivity_zeta=int(positivity_zeta),
             positivity_Zubarev=int(positivity_Zubarev),
             verdict=verdict,
             closure_sha=closure_sha,
             K_R5_prereg=K_R5_PREREG,
             sv1_xi_E_ref=SV1_XI_E_REF,
             cc2_diff=cc2_diff,
             cc3_zeta=cc3_zeta,
             cc3_Zub=cc3_Zub,
             cc5_ratio_zeta=cc5_ratio_zeta,
             cc5_ratio_Zub=cc5_ratio_Zub,
             cc4_ok=(cc4_ok if cc4_ok is not None else False),
             pass_tol=PASS_TOL,
             fail_tol=FAIL_TOL,
             K_scan_lo=K_SCAN_LO,
             K_scan_hi=K_SCAN_HI,
             n_scan=N_SCAN,
             dlnK_eff=dlnK)
    print(f"  Saved NPZ: {OUT_NPZ.name}")

    # --- Section 7.8: Plot ---
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(14, 5.5))

    # Left: A_s(K) for each regulator + Planck line + PASS/FAIL bands
    axL.plot(K_scan, A_s_scan_zeta, 'o-', color='#1f77b4',
             label=f'zeta: A_base={A_s_base_zeta:.2e}')
    axL.plot(K_scan, A_s_scan_Zubarev, 's-', color='#d62728',
             label=f'Zubarev: A_base={A_s_base_Zubarev:.2e}')
    axL.axhline(A_s_PLANCK, color='k', ls='--', lw=1.5,
                label=f'Planck A_s = {A_s_PLANCK:.2e}')
    axL.axhline(A_s_PLANCK * 1.02, color='g', ls=':', lw=1, alpha=0.6,
                label='2% tolerance band')
    axL.axhline(A_s_PLANCK * 0.98, color='g', ls=':', lw=1, alpha=0.6)
    axL.set_xscale('log')
    axL.set_yscale('log')
    axL.set_xlabel('K  (corridor dial, R5 convention)')
    axL.set_ylabel('A_s(K; regulator)')
    axL.set_title('A_s(K) under zeta and Zubarev regulators\n(linear response A_s = A_base * K)')
    axL.legend(loc='best', fontsize=9)
    axL.grid(True, which='both', alpha=0.3)

    # Right: K_R5 per regulator with 0.02 RATIO band
    regs = ['zeta', 'Zubarev']                                       # (local)
    K_R5_vals = [K_R5_zeta, K_R5_Zubarev]                            # (local)
    colors = ['#1f77b4', '#d62728']                                  # (local)
    xp = np.arange(len(regs))                                        # (local)
    axR.bar(xp, K_R5_vals, color=colors, alpha=0.8, edgecolor='black')
    for i, (r, v) in enumerate(zip(regs, K_R5_vals)):
        axR.annotate(f'{v:.4f}', (xp[i], v), textcoords='offset points',
                     xytext=(0, 5), ha='center', fontsize=10)
    axR.axhline(1.0, color='k', ls='-', lw=1, label='K=1 positivity wall')
    axR.axhline(K_R5_PREREG, color='purple', ls=':', lw=1.5,
                label=f'R5 corridor K=1.922 (Landau V.1)')
    # 0.02 RATIO band around K_R5(Zubarev)
    axR.axhspan(K_R5_Zubarev * 0.98, K_R5_Zubarev * 1.02,
                color='green', alpha=0.15, label='2% ratio band around K_R5(Zub)')
    axR.set_yscale('log')
    axR.set_xticks(xp)
    axR.set_xticklabels(regs)
    axR.set_ylabel('K_R5(regulator)  [= K_match = A_s_Planck / A_s_base]')
    axR.set_title(f'K_R5 regulator comparison\n'
                  f'ratio = {max_rel_span:.4f} ({"PASS" if max_rel_span<=PASS_TOL else ("FAIL" if max_rel_span>=FAIL_TOL else "INFO")})')
    axR.legend(loc='best', fontsize=8)
    axR.grid(True, which='both', alpha=0.3)

    plt.suptitle(f'{GATE_ID} -- verdict: {verdict} | '
                 f'xi(Zub)={xi_Zubarev:.4e} | K_R5(zeta)={K_R5_zeta:.3f} | '
                 f'K_R5(Zub)={K_R5_Zubarev:.2f}',
                 fontsize=11)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=130)
    plt.close()
    print(f"  Saved PNG: {OUT_PNG.name}")
    print()

    # --- Section 7.9: 4-tuple + verdict line ---
    value_tag = (f"max_rel_span={max_rel_span:.4f}_"
                 f"K_R5_zeta={K_R5_zeta:.4f}_"
                 f"K_R5_Zubarev={K_R5_Zubarev:.4f}_"
                 f"xi_Zub={xi_Zubarev:.4e}_"
                 f"pos_zeta={int(positivity_zeta)}_"
                 f"pos_Zub={int(positivity_Zubarev)}")               # (local)
    tuple_line = (f"(value={value_tag} scheme={SCHEME_OUT} "
                  f"convention={CONVENTION} L_max={L_MAX})")          # (local)
    print("4-tuple:", tuple_line)
    print()

    verdict_line = (f"W5-54: {verdict} -- value={value_tag} "
                    f"scheme={SCHEME_OUT} convention={CONVENTION} "
                    f"L_max={L_MAX} sha256={closure_sha}\n")           # (local)
    print("Appending verdict line to s84_gate_verdicts.txt:")
    print(f"  {verdict_line.strip()}")
    with open(VERDICT_TXT, 'a', encoding='utf-8') as f:
        f.write(verdict_line)
    print(f"  appended to {VERDICT_TXT.name}")
    print()

    print("=" * 78)
    print(f"DONE. Verdict: {verdict}")
    print("=" * 78)
    return 0


if __name__ == '__main__':
    sys.exit(main())
