#!/usr/bin/env python3
"""
S84 W3-32 — K-A4-CANONICAL-RANGE
================================

Gate: S84-K-A4-CANONICAL-RANGE ([VERIFY])

Pre-registered threshold (plan session-84-plan-w3.md §W3-32):
  PASS: span(k_a4) < 1.5  (R-protected — surprising)
  INFO: 1.5 <= span < 10  (NOT-R-protected, less severe than predicted)
  FAIL: span >= 10        (NOT-R-protected; prediction ~30.97 at L_max=5)

Prediction 30.97 from W3-30 scaling extrapolation (k=2 -> k=4).
10% prediction-accuracy tolerance applies to the prediction check,
separate from the PASS/INFO/FAIL classification.

4-tuple slot: (value=span_k_a4, scheme=5-regulators,
               convention=Lambda_Z-M_KK-headline, L_max=5)

Classification: GEOMETRIC (a_4 slot span — YM coefficient slot).

CONTEXT — Extends S83 W2-G15 from a_2 to a_4
---------------------------------------------
Per Chamseddine-Connes Mellin decomposition, a_n slot weight is
    f_n^R(Lambda^2) := int_0^{Lambda^2} u^{n/2 - 1} * w_R(u) du
For a_2: u^0 = 1 (as in G15).
For a_4: u^1 (extra |D|^2 factor from Seeley-DeWitt a_4 coefficient).
Setting k_a4^R := f_4^R / f_4^{f*} (f* anchor matching G15 convention).

SUBSTITUTION CHAIN [VERIFY]
---------------------------
Step 1 (definition):
    f_4^R(L2) := int_0^{L2} u * w_R(u) du
    k_a4^R   := f_4^R / f_4^{f*}

Step 2 (substitute per regulator):
    w_zeta(u)        = 1                   -> f_4 = L2^2 / 2
    w_Zubarev_A(u)   = exp(-u)             -> f_4 = 1 - (L2+1) e^{-L2}
    w_Zubarev_B(u)   = exp(-u/L2)          -> f_4 = L2^2 (1 - 2/e)
    w_SDW(u)         = sqrt(u)             -> f_4 = (2/5) L2^{5/2}
    w_dim-reg(u)     = 1                   -> f_4 = L2^2 / 2
    w_lattice-BR(u)  = 1                   -> f_4 = L2^2 / 2
    w_f*(u)          = a*sqrt(u)+b*exp(-u) -> f_4 = a*(2/5)L2^{5/2}+b*[1-(L2+1)e^{-L2}]

Step 3 (simplify):
    span_A = max_R k_a4^R / min_R k_a4^R  (Convention A: Lambda_Z=M_KK=1)
    span_B analogously (Convention B: Lambda_Z=sqrt(L2))

Step 4 (direction):
    span is ratio of positive quantities, so span >= 1 always.
    span >= 10 => FAIL R-protection (a_4 slot scheme-dressed).
    1.5 <= span < 10 => INFO (mild).
    span < 1.5 => PASS R-protection (surprising).

Step 5 (Python pre-verification — run before this script):
    At L_max=5, lam_max=2.802848, L2=7.855955:
      k_a4[zeta]=0.488329
      k_a4[Zub-A]=0.015771
      k_a4[SDW]=1.094969
      k_a4[dim-reg]=0.488329
      k_a4[lattice-BR]=0.488329
      span_A = 1.094969 / 0.015771 = 69.4305
      span_B = 4.2429
    -> FAIL headline. Prediction 30.97 MISSED (69.43 is 2.24x prediction,
       outside 10% tolerance). Classification (FAIL) still matches plan.
    Analytic-numerical f_4 cross-check: |diff| < 1.6e-10 for all regulators.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import M_KK, tau_fold, PI

# ---------------------------------------------------------------------------
# Section 2 — Standard imports (CPU thread cap before numpy)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import sys
import time
from pathlib import Path

import numpy as np
from scipy import integrate
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

SESSION = "S84"                                       # (local)
GATE_ID = "S84-K-A4-CANONICAL-RANGE"                  # (local)
SCHEME = "5-regulators"                               # (local)
CONVENTION = "Lambda_Z-M_KK-headline"                 # (local)
L_MAX = 5                                             # (local) task-pinned
L_MAX_CROSSCHECK = 7                                  # (local) plan cross-check

OUT_NPZ = SCRIPT_DIR / "s84_w3_k_a4_canonical_range.npz"
OUT_PNG = SCRIPT_DIR / "s84_w3_k_a4_canonical_range.png"
VERDICT_TXT = SCRIPT_DIR / "s84_gate_verdicts.txt"
SPECTRUM_CACHE = SCRIPT_DIR / "s74_spectrum_cache_L9_tau019.npz"  # (local)

INPUT_FILES = [
    SCRIPT_DIR / "canonical_constants.py",
    SPECTRUM_CACHE,
    SCRIPT_DIR / "s84_w3_k_a4_canonical_range.py",
]

# Gate thresholds (pre-registered per plan §W3-32)
PASS_SPAN_THRESHOLD = 1.5                             # (local) R-protected
INFO_SPAN_THRESHOLD = 10.0                            # (local) mild NOT-R-protected upper
PREDICTED_SPAN = 30.97                                # (local) plan §W3-32 prediction
PREDICTION_TOLERANCE = 0.10                           # (local) 10%
EVAL_CUTOFF = 0.01                                    # (local) IR cutoff (match G15)

# SDW f_star parameters (S72 canonical — matches G15)
ALPHA_STAR = 0.912                                    # (local) f_star sqrt-weight
BETA_STAR  = 0.088                                    # (local) f_star exp-weight


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    # S84 audit finding — include gate_id + script SHA as virtual entries
    pins["__gate_id__"] = hashlib.sha256(GATE_ID.encode("utf-8")).hexdigest()
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    print(f"  __gate_id__: {pins['__gate_id__'][:16]}...")
    return pins


def closure_hash(pins):
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()          # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Spectrum loader
# ---------------------------------------------------------------------------

def collect_spectrum(sector_dict, L_max_cut, cutoff):
    abs_list, mult_list = [], []  # (local)
    for _key, data in sorted(sector_dict.items()):
        if data['level'] <= L_max_cut:
            dim = int(data['dim'])  # (local)
            for ev in data['abs_evals']:
                a = float(ev)       # (local)
                if a > cutoff:
                    abs_list.append(a)
                    mult_list.append(dim)
    return (np.array(abs_list, dtype=np.float64),
            np.array(mult_list, dtype=np.float64))


# ---------------------------------------------------------------------------
# Section 6 — Analytic f_4^R(L2) = int_0^L2 u * w_R(u) du
# ---------------------------------------------------------------------------

def f4_zeta(L2):        return float(0.5 * L2**2)
def f4_Zubarev_A(L2):   return float(1.0 - (L2 + 1.0) * np.exp(-L2))
def f4_Zubarev_B(L2):   return float(L2**2 * (1.0 - 2.0 / np.e))
def f4_SDW(L2):         return float((2.0/5.0) * L2**2.5)
def f4_dimreg(L2):      return float(0.5 * L2**2)
def f4_lattice_BR(L2):  return float(0.5 * L2**2)
def f4_fstar(L2, a=ALPHA_STAR, b=BETA_STAR):
    return float(a * (2.0/5.0) * L2**2.5
                 + b * (1.0 - (L2 + 1.0) * np.exp(-L2)))


def f4_numeric(L2, wfun):
    val, _ = integrate.quad(lambda u: u * wfun(u), 0.0, L2,
                            limit=500, epsabs=1e-14, epsrel=1e-12)
    return float(val)


# ---------------------------------------------------------------------------
# Section 7 — k_a4^R assembler
# ---------------------------------------------------------------------------

def k_a4_convention(L2, convention):
    f4_fs = f4_fstar(L2)  # (local)
    if convention == 'A':
        zub = f4_Zubarev_A(L2)  # (local)
    elif convention == 'B':
        zub = f4_Zubarev_B(L2)  # (local)
    else:
        raise ValueError(f"Unknown convention: {convention}")
    k = {  # (local)
        'zeta':       f4_zeta(L2)       / f4_fs,
        'Zubarev':    zub               / f4_fs,
        'SDW':        f4_SDW(L2)        / f4_fs,
        'dim-reg':    f4_dimreg(L2)     / f4_fs,
        'lattice-BR': f4_lattice_BR(L2) / f4_fs,
    }
    return k


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...")
    print()

    if not SPECTRUM_CACHE.exists():
        print(f"SPECTRUM CACHE MISSING: {SPECTRUM_CACHE}")
        return 2
    cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
    sector_evals = cache['sector_evals'].item()
    cache.close()

    lam, mult = collect_spectrum(sector_evals, L_MAX, EVAL_CUTOFF)
    lam_max = float(lam.max())   # (local)
    L2_primary = lam_max ** 2    # (local)
    print(f"[L_max={L_MAX}] spectrum:")
    print(f"  n_modes        = {len(lam)}")
    print(f"  lam_max (M_KK) = {lam_max:.6f}")
    print(f"  Lambda^2       = {L2_primary:.6f}")
    print()

    # Analytic/numeric cross-check for all regulators
    ana_num = {  # (local)
        'zeta':       (f4_zeta(L2_primary),       f4_numeric(L2_primary, lambda u: 1.0)),
        'Zubarev-A':  (f4_Zubarev_A(L2_primary),  f4_numeric(L2_primary, lambda u: np.exp(-u))),
        'Zubarev-B':  (f4_Zubarev_B(L2_primary),  f4_numeric(L2_primary, lambda u: np.exp(-u/L2_primary))),
        'SDW':        (f4_SDW(L2_primary),        f4_numeric(L2_primary, lambda u: np.sqrt(u))),
        'f*':         (f4_fstar(L2_primary),      f4_numeric(L2_primary, lambda u: ALPHA_STAR*np.sqrt(u) + BETA_STAR*np.exp(-u))),
    }
    print("Analytic-numerical cross-check (f_4^R):")
    for name, (ana, num) in ana_num.items():
        diff = abs(ana - num)  # (local)
        print(f"  {name:10s}: ana={ana:.10e}  num={num:.10e}  |diff|={diff:.2e}")
        assert diff < 1e-8, f"f4 {name} analytic/numeric mismatch"
    print()

    # Compute k_a4 at both conventions
    k_a4_A = k_a4_convention(L2_primary, 'A')
    k_a4_B = k_a4_convention(L2_primary, 'B')

    print("Convention A (Lambda_Z=M_KK=1) — HEADLINE:")
    for R, v in k_a4_A.items():
        print(f"  k_a4[{R:>10s}] = {v:.6f}")
    vals_A = np.array(list(k_a4_A.values()))  # (local)
    max_A = float(vals_A.max())                # (local)
    min_A = float(vals_A.min())                # (local)
    span_A = max_A / min_A                     # (local)
    print(f"  max = {max_A:.6f}  min = {min_A:.6f}  span_A = {span_A:.6f}")
    print()

    print("Convention B (Lambda_Z=sqrt(L2)) — CROSS-CHECK:")
    for R, v in k_a4_B.items():
        print(f"  k_a4[{R:>10s}] = {v:.6f}")
    vals_B = np.array(list(k_a4_B.values()))  # (local)
    max_B = float(vals_B.max())                # (local)
    min_B = float(vals_B.min())                # (local)
    span_B = max_B / min_B                     # (local)
    print(f"  max = {max_B:.6f}  min = {min_B:.6f}  span_B = {span_B:.6f}")
    print()

    # Gate classification — HEADLINE from Convention A
    if span_A < PASS_SPAN_THRESHOLD:
        verdict = "PASS"
    elif span_A < INFO_SPAN_THRESHOLD:
        verdict = "INFO"
    else:
        verdict = "FAIL"

    # Prediction accuracy (secondary — not gate-deciding)
    pred_rel_err = abs(span_A - PREDICTED_SPAN) / PREDICTED_SPAN  # (local)
    pred_within_tol = pred_rel_err <= PREDICTION_TOLERANCE        # (local)
    print(f"Predicted span (plan): {PREDICTED_SPAN:.2f}")
    print(f"Measured span_A:       {span_A:.4f}")
    print(f"Prediction rel. err:   {pred_rel_err:.4f} "
          f"({'within' if pred_within_tol else 'OUTSIDE'} {PREDICTION_TOLERANCE*100:.0f}% tol)")
    print(f"Headline classification: {verdict}")
    print()

    # L_max=7 cross-check
    lam7, _ = collect_spectrum(sector_evals, L_MAX_CROSSCHECK, EVAL_CUTOFF)
    L2_7 = float(lam7.max() ** 2)  # (local)
    k_A_7 = k_a4_convention(L2_7, 'A')
    vA7 = np.array(list(k_A_7.values()))  # (local)
    span_A_7 = float(vA7.max() / vA7.min())  # (local)
    k_B_7 = k_a4_convention(L2_7, 'B')
    vB7 = np.array(list(k_B_7.values()))  # (local)
    span_B_7 = float(vB7.max() / vB7.min())  # (local)
    print(f"[L_max={L_MAX_CROSSCHECK}] cross-check: Lambda^2={L2_7:.6f}")
    print(f"  span_A={span_A_7:.4f}  span_B={span_B_7:.4f}")
    print()

    # Comparison to G15 a_2 slot (S83)
    print("Reference (S83 G15, a_2 slot): span_A=14.685 (FAIL)")
    print(f"This gate (a_4 slot):          span_A={span_A:.4f} ({verdict})")
    print(f"Ratio a_4-span / a_2-span:     {span_A / 14.685:.4f}")

    # Save artifacts
    np.savez(
        OUT_NPZ,
        L_max=L_MAX,
        lam_max=lam_max,
        Lambda_sq=L2_primary,
        k_a4_A_zeta=k_a4_A['zeta'],
        k_a4_A_Zubarev=k_a4_A['Zubarev'],
        k_a4_A_SDW=k_a4_A['SDW'],
        k_a4_A_dimreg=k_a4_A['dim-reg'],
        k_a4_A_lattice_BR=k_a4_A['lattice-BR'],
        max_A=max_A, min_A=min_A, span_A=span_A,
        k_a4_B_zeta=k_a4_B['zeta'],
        k_a4_B_Zubarev=k_a4_B['Zubarev'],
        k_a4_B_SDW=k_a4_B['SDW'],
        k_a4_B_dimreg=k_a4_B['dim-reg'],
        k_a4_B_lattice_BR=k_a4_B['lattice-BR'],
        max_B=max_B, min_B=min_B, span_B=span_B,
        span_A_Lmax7=span_A_7,
        span_B_Lmax7=span_B_7,
        predicted_span=PREDICTED_SPAN,
        prediction_rel_err=pred_rel_err,
        prediction_within_tol=pred_within_tol,
        g15_a2_span_reference=14.685,
        PASS_SPAN_THRESHOLD=PASS_SPAN_THRESHOLD,
        INFO_SPAN_THRESHOLD=INFO_SPAN_THRESHOLD,
        verdict=verdict,
        closure=closure,
    )
    print(f"Artifacts: {OUT_NPZ.name}")

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    ax0, ax1 = axes
    R_names = list(k_a4_A.keys())  # (local)
    colors = ['#2c7fb8', '#d95f0e', '#31a354', '#c26dbc', '#7a7a7a']  # (local)

    vals_A_plot = [k_a4_A[R] for R in R_names]  # (local)
    ax0.bar(R_names, vals_A_plot, color=colors, alpha=0.85, edgecolor='k', linewidth=0.5)
    ax0.axhline(min_A * PASS_SPAN_THRESHOLD, color='k', linestyle='--',
                label=f'PASS top (min*{PASS_SPAN_THRESHOLD})')
    ax0.axhline(min_A * INFO_SPAN_THRESHOLD, color='gray', linestyle=':',
                label=f'INFO top (min*{INFO_SPAN_THRESHOLD})')
    for i, v in enumerate(vals_A_plot):
        ax0.text(i, v + max_A * 0.02, f'{v:.4f}', ha='center', va='bottom', fontsize=9)
    ax0.set_ylabel(r'$k_{a_4}^R$')
    ax0.set_title(f'Conv A (Lambda_Z=M_KK) — HEADLINE\nspan={span_A:.4f} -> {verdict}')
    ax0.set_yscale('log')
    ax0.legend(loc='upper right', fontsize=8)
    ax0.grid(alpha=0.3, which='both')
    ax0.tick_params(axis='x', rotation=20)

    vals_B_plot = [k_a4_B[R] for R in R_names]  # (local)
    if span_B < PASS_SPAN_THRESHOLD:      v_B = "PASS"
    elif span_B < INFO_SPAN_THRESHOLD:    v_B = "INFO"
    else:                                 v_B = "FAIL"
    ax1.bar(R_names, vals_B_plot, color=colors, alpha=0.85, edgecolor='k', linewidth=0.5)
    ax1.axhline(min_B * PASS_SPAN_THRESHOLD, color='k', linestyle='--',
                label=f'PASS top (min*{PASS_SPAN_THRESHOLD})')
    ax1.axhline(min_B * INFO_SPAN_THRESHOLD, color='gray', linestyle=':',
                label=f'INFO top (min*{INFO_SPAN_THRESHOLD})')
    for i, v in enumerate(vals_B_plot):
        ax1.text(i, v + max_B * 0.02, f'{v:.4f}', ha='center', va='bottom', fontsize=9)
    ax1.set_ylabel(r'$k_{a_4}^R$')
    ax1.set_title(f'Conv B (Lambda_Z=matched) — CROSS-CHECK\nspan={span_B:.4f} -> {v_B}')
    ax1.legend(loc='upper right', fontsize=8)
    ax1.grid(alpha=0.3)
    ax1.tick_params(axis='x', rotation=20)

    fig.suptitle(f'S84 W3-32 K-A4-CANONICAL-RANGE — {verdict} (span_A={span_A:.4f}, '
                 f'pred={PREDICTED_SPAN})', fontsize=12)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110, bbox_inches='tight')
    plt.close(fig)
    print(f"Plot:      {OUT_PNG.name}")

    tag = (f"(value=span_A={span_A:.6f}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n4-tuple: {tag}")

    verdict_line = (
        f"{GATE_ID}: {verdict} -- value=span_A={span_A:.6f},span_B={span_B:.6f},"
        f"pred={PREDICTED_SPAN},pred_rel_err={pred_rel_err:.4f} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"sha256={closure}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_line)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0 if verdict == "PASS" else (1 if verdict == "FAIL" else 3)


if __name__ == "__main__":
    sys.exit(main())
