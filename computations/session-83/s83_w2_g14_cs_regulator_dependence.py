#!/usr/bin/env python3
"""
S83 W2-G14 — CS-REGULATOR-DEPENDENCE
=====================================

Gate: S83-CS-REGULATOR-DEPENDENCE ([VERIFY])

Pre-registered threshold (from sessions/archive/session-83/session-83-results-workingpaper.md
line 1200):
  PASS: max_R1,R2 |c_s_R1 / c_s_R2| <= 1.5
  FAIL: ratio > 2.5
  INFO: ratio in [1.5, 2.5]

4-tuple slot: (c_s_ratio=?, scheme=zeta+Zubarev+SDW,
               convention=Bogoliubov-dispersion, L_max=5)

Classification: PHONONIC.

CONTEXT
-------
S82 W-1 carry-forward #5 pre-registered this test: if c_s is FI, the W-1
PASS-F2 verdict (A_s framework = 3.2994e-9, delta_OOM = +0.1962) becomes
unconditional on c_s across regulators.

Wave-1 G1 (IC-SCHEME-DERIVATION) established Branch-B Zubarev pathway.
Wave-1 G3 (REGULATOR-PRIORITY-PROOF) PASS zeta-axiom-unique at Dixmier
layer. If c_s is FI across 3 regulators, that is ORTHOGONAL evidence that
c_s is substrate-intrinsic and NOT regulator-picked; if RD, c_s-pinning
becomes scheme-contingent.

METHODOLOGY
-----------
Canonical Bogoliubov dispersion from the D_K eigenvalue spectrum:

  omega_R^2(k) = (c_s_R k)^2 + (k^2 / 2 m_R)^2

For k -> 0:  c_s_R^2 = dE/dk |_{k=0} = <lam^2>_R (first-moment ratio)
                     = [sum_n d_n w_R(lam_n) lam_n^2] / [sum_n d_n w_R(lam_n)]

Three regulators (identical to W1-G1/G3 convention):
  w_zeta(lam) = 1                                (zeta_D(0) counting)
  w_Zub(lam)  = exp(-lam^2 / Lambda_Z^2), Lambda_Z=1 in M_KK units
  w_SDW(lam)  = alpha_star sqrt(x) + beta_star exp(-x),  x = lam^2
                with S72 f_star: alpha_star=0.91168, beta_star=0.08832

Both numerator and denominator share the same regulator-dependent weight;
no external Lambda scale enters the RATIO beyond the spectrum itself.

SUBSTITUTION CHAIN [VERIFY]
---------------------------
Step 1. Definition.
    c_s^2 = lim_{k->0} dE^2/dk^2 where E = omega_R(k) = Bogoliubov phonon
    dispersion on the D_K eigenvalue spectrum. In the BLV (canonical-kinetic)
    convention, c_s^2 = first-weighted-moment ratio <lam^2>_R.

Step 2. Substitute per regulator:
    c_s_R^2 = sum_n d_n w_R(lam_n) lam_n^2 / sum_n d_n w_R(lam_n)
    with the three weights defined above.

Step 3. Simplify.
    FI criterion:  max_R1,R2 c_s_R1 / c_s_R2 <= 1.5
    The ratio is dimensionless; the sqrt of the moment ratio isolates the
    spectrum-level comparison (no Lambda enters).

Step 4. Direction.
    PASS if max/min <= 1.5
    INFO if 1.5 < max/min <= 2.5
    FAIL if max/min > 2.5

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py  (closure hash)
  - s74_spectrum_cache_L9_tau019.npz  (D_K spectrum at tau_fold)

Output 4-tuple:
  (c_s_ratio=<max/min>, scheme=zeta+Zubarev+SDW,
   convention=Bogoliubov-dispersion, L_max=5)
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
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

SESSION = "S83"                                    # (local)
GATE_ID = "S83-CS-REGULATOR-DEPENDENCE"            # (local)
SCHEME = "zeta+Zubarev+SDW"                        # (local)
CONVENTION = "Bogoliubov-dispersion"               # (local)
L_MAX = 5                                          # (local) task-pinned

OUT_NPZ = SCRIPT_DIR / "s83_w2_g14_cs_regulator_dependence.npz"
OUT_PNG = SCRIPT_DIR / "s83_w2_g14_cs_regulator_dependence.png"
VERDICT_TXT = SCRIPT_DIR / "s83_gate_verdicts.txt"
SPECTRUM_CACHE = SCRIPT_DIR / "s74_spectrum_cache_L9_tau019.npz"  # (local)

INPUT_FILES = [
    SCRIPT_DIR / "canonical_constants.py",
    SPECTRUM_CACHE,
    SCRIPT_DIR / "s83_w2_g14_cs_regulator_dependence.py",
]

# Gate thresholds (pre-registered)
PASS_RATIO_THRESHOLD = 1.5                         # (local) FI factor-1.5 band
INFO_RATIO_THRESHOLD = 2.5                         # (local) scheme-dependent band upper
EVAL_CUTOFF = 0.01                                 # (local) IR cutoff (matches W1-G1/G3)

# SDW f_star parameters (S72, canonical)
ALPHA_STAR = 0.9116771171053042                    # (local) S72 f_star sqrt-weight
BETA_STAR  = 0.08832288289469575                   # (local) S72 f_star exp-weight


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
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()          # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Spectrum loader (L_max=5 filter)
# ---------------------------------------------------------------------------

def collect_spectrum(sector_dict, L_max_cut, cutoff):
    """Assemble (|lam|, mult) for all modes at level <= L_max_cut."""
    abs_list = []    # (local)
    mult_list = []   # (local)
    for _key, data in sorted(sector_dict.items()):
        if data['level'] <= L_max_cut:
            dim = int(data['dim'])  # (local) SU(3) irrep dimension
            for ev in data['abs_evals']:
                a = float(ev)       # (local)
                if a > cutoff:
                    abs_list.append(a)
                    mult_list.append(dim)
    return (np.array(abs_list, dtype=np.float64),
            np.array(mult_list, dtype=np.float64))


# ---------------------------------------------------------------------------
# Section 6 — Regulator weights (canonical W1-G1/G3 convention)
# ---------------------------------------------------------------------------

def weight_zeta(lam):
    """Zeta regulator: zeta_D(0) counting, flat weight = 1."""
    return np.ones_like(lam, dtype=np.float64)


def weight_zubarev(lam, Lambda_Z=1.0):
    """Zubarev Gaussian mollifier: exp(-lam^2 / Lambda_Z^2)."""
    return np.exp(-(lam / Lambda_Z) ** 2)


def weight_sdw(lam, Lambda_S=1.0, alpha=ALPHA_STAR, beta=BETA_STAR):
    """SDW f_star (S72): alpha*sqrt(x) + beta*exp(-x), x=lam^2/Lambda_S^2."""
    x = (lam / Lambda_S) ** 2
    return alpha * np.sqrt(x) + beta * np.exp(-x)


# ---------------------------------------------------------------------------
# Section 7 — Bogoliubov c_s from first-moment ratio
# ---------------------------------------------------------------------------

def c_s_from_moment(lam, mult, weight_fn):
    """
    Bogoliubov phonon c_s^2 at k->0 limit.

    c_s^2 = dE^2/dk^2 at k=0 = <lam^2>_R
          = sum_n d_n w_R(lam_n) lam_n^2 / sum_n d_n w_R(lam_n)

    Returns c_s in M_KK units.
    """
    w = weight_fn(lam)                                    # (local)
    num = float((mult * w * lam ** 2).sum())              # (local) Z_R
    den = float((mult * w).sum())                         # (local) S_R normalization
    if den <= 0.0 or not np.isfinite(den):
        return float('nan')
    return float(np.sqrt(num / den))


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins + closure
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...")
    print()

    # 2. Load spectrum at L_max=5
    if not SPECTRUM_CACHE.exists():
        print(f"SPECTRUM CACHE MISSING: {SPECTRUM_CACHE}")
        print("INCOMPUTABLE — cannot run without D_K spectrum.")
        return 2
    cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
    sector_evals = cache['sector_evals'].item()
    cache.close()

    lam, mult = collect_spectrum(sector_evals, L_MAX, EVAL_CUTOFF)
    print(f"[L_max={L_MAX}] spectrum loaded:")
    print(f"  n_modes        = {len(lam)}")
    print(f"  lam_max (M_KK) = {lam.max():.6f}")
    print(f"  sum(mult)      = {int(mult.sum())}")
    print()

    # 3. Compute c_s per regulator
    c_s_zeta    = c_s_from_moment(lam, mult, weight_zeta)
    c_s_Zubarev = c_s_from_moment(lam, mult, weight_zubarev)
    c_s_SDW     = c_s_from_moment(lam, mult, weight_sdw)

    c_s_vals = {
        'zeta':    c_s_zeta,
        'Zubarev': c_s_Zubarev,
        'SDW':     c_s_SDW,
    }

    print("Bogoliubov phonon c_s per regulator (M_KK units):")
    for R, v in c_s_vals.items():
        print(f"  c_s[{R:>7s}] = {v:.6f}")

    # 4. max/min ratio (FI metric)
    vals = np.array([c_s_zeta, c_s_Zubarev, c_s_SDW])    # (local)
    max_val = float(vals.max())                           # (local)
    min_val = float(vals.min())                           # (local)
    max_ratio = max_val / min_val                         # (local) headline FI metric

    print()
    print(f"max_R c_s_R            = {max_val:.6f}")
    print(f"min_R c_s_R            = {min_val:.6f}")
    print(f"max/min ratio          = {max_ratio:.6f}")
    print(f"PASS threshold         = {PASS_RATIO_THRESHOLD:.2f}")
    print(f"INFO upper threshold   = {INFO_RATIO_THRESHOLD:.2f}")

    # 5. Gate decision
    if max_ratio <= PASS_RATIO_THRESHOLD:
        verdict = "PASS"
    elif max_ratio <= INFO_RATIO_THRESHOLD:
        verdict = "INFO"
    else:
        verdict = "FAIL"
    print(f"\n=> verdict: {verdict}")

    # 6. Cross-checks
    #   (a) Each c_s finite and positive
    #   (b) zeta c_s equals RMS(lam) weighted by multiplicity
    #   (c) Zubarev c_s < zeta c_s (Gaussian suppresses UV)
    #   (d) SDW c_s near zeta c_s (sqrt-UV dominant)
    rms_lam = float(np.sqrt((mult * lam ** 2).sum() / mult.sum()))  # (local)
    checks = {
        'all_finite_positive': bool(np.all(np.isfinite(vals)) and np.all(vals > 0)),
        'zeta_equals_rms': bool(abs(c_s_zeta - rms_lam) < 1e-10),
        'Zubarev_suppressed': bool(c_s_Zubarev < c_s_zeta),
        'SDW_near_zeta': bool(abs(c_s_SDW - c_s_zeta) / c_s_zeta < 0.10),
    }
    print("\nCross-checks:")
    for k, v in checks.items():
        print(f"  {k}: {v}")

    # 7. Per-mode dispersion diagnostic (Bogoliubov spectrum head/tail)
    #    omega_R(k=0..lam_max) sampled at 40 k-points per regulator
    k_grid = np.linspace(1e-3, lam.max(), 40)             # (local)
    def omega_at_k(c_s, m_eff, k):
        return np.sqrt((c_s * k) ** 2 + (k ** 2 / (2.0 * m_eff)) ** 2)

    # Effective phonon mass m_R^{-1} = <lam^{-2}>_R / <1>_R
    def m_eff_inv(weight_fn):
        w = weight_fn(lam)                                # (local)
        num = float((mult * w / lam ** 2).sum())          # (local)
        den = float((mult * w).sum())                     # (local)
        return num / den
    m_inv_zeta = m_eff_inv(weight_zeta)                   # (local)
    m_inv_Zub  = m_eff_inv(weight_zubarev)                # (local)
    m_inv_SDW  = m_eff_inv(weight_sdw)                    # (local)
    m_eff_zeta = 1.0 / m_inv_zeta if m_inv_zeta > 0 else np.inf  # (local)
    m_eff_Zub  = 1.0 / m_inv_Zub  if m_inv_Zub  > 0 else np.inf  # (local)
    m_eff_SDW  = 1.0 / m_inv_SDW  if m_inv_SDW  > 0 else np.inf  # (local)

    disp_zeta = omega_at_k(c_s_zeta,    m_eff_zeta, k_grid)  # (local)
    disp_Zub  = omega_at_k(c_s_Zubarev, m_eff_Zub,  k_grid)  # (local)
    disp_SDW  = omega_at_k(c_s_SDW,     m_eff_SDW,  k_grid)  # (local)

    # 8. Save artifacts
    np.savez(
        OUT_NPZ,
        L_max=L_MAX,
        n_modes=len(lam),
        lam_max=lam.max(),
        sum_mult=float(mult.sum()),
        c_s_zeta=c_s_zeta,
        c_s_Zubarev=c_s_Zubarev,
        c_s_SDW=c_s_SDW,
        max_val=max_val,
        min_val=min_val,
        max_ratio=max_ratio,
        PASS_RATIO_THRESHOLD=PASS_RATIO_THRESHOLD,
        INFO_RATIO_THRESHOLD=INFO_RATIO_THRESHOLD,
        rms_lam=rms_lam,
        m_eff_zeta=m_eff_zeta,
        m_eff_Zubarev=m_eff_Zub,
        m_eff_SDW=m_eff_SDW,
        k_grid=k_grid,
        disp_zeta=disp_zeta,
        disp_Zubarev=disp_Zub,
        disp_SDW=disp_SDW,
        verdict=verdict,
        closure=closure,
    )
    print(f"\nArtifacts: {OUT_NPZ.name}")

    # 9. Plot — 2 panels: (a) bar chart c_s per R, (b) dispersion curves
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    ax0, ax1 = axes

    # Panel (a): c_s bars with ratio annotation
    names = list(c_s_vals.keys())                         # (local)
    cs_arr = [c_s_vals[k] for k in names]                 # (local)
    colors = ['#2c7fb8', '#d95f0e', '#31a354']            # (local)
    bars = ax0.bar(names, cs_arr, color=colors, alpha=0.85)
    ax0.axhline(min_val * PASS_RATIO_THRESHOLD, color='k', linestyle='--',
                label=f'PASS band top (min*{PASS_RATIO_THRESHOLD})')
    ax0.axhline(min_val * INFO_RATIO_THRESHOLD, color='gray', linestyle=':',
                label=f'INFO band top (min*{INFO_RATIO_THRESHOLD})')
    for b, v in zip(bars, cs_arr):
        ax0.text(b.get_x() + b.get_width() / 2., v + 0.02,
                 f'{v:.4f}', ha='center', va='bottom', fontsize=9)
    ax0.set_ylabel(r'$c_s$ (M$_{KK}$ units)')
    ax0.set_title(f'c_s per regulator — max/min = {max_ratio:.4f} -> {verdict}')
    ax0.legend(loc='lower right', fontsize=8)
    ax0.set_ylim(0, max_val * 1.35)
    ax0.grid(alpha=0.3)

    # Panel (b): Bogoliubov dispersions
    ax1.plot(k_grid, disp_zeta, color=colors[0], label=f'zeta   (c_s={c_s_zeta:.3f})', lw=2)
    ax1.plot(k_grid, disp_Zub,  color=colors[1], label=f'Zubarev (c_s={c_s_Zubarev:.3f})', lw=2)
    ax1.plot(k_grid, disp_SDW,  color=colors[2], label=f'SDW     (c_s={c_s_SDW:.3f})', lw=2)
    ax1.set_xlabel('k (M_KK units)')
    ax1.set_ylabel(r'$\omega_R(k)$')
    ax1.set_title(r'Bogoliubov dispersion: $\omega^2 = (c_s k)^2 + (k^2/2m)^2$')
    ax1.legend(loc='upper left', fontsize=9)
    ax1.grid(alpha=0.3)

    fig.suptitle(f'S83 W2-G14 CS-REGULATOR-DEPENDENCE — {verdict} (ratio={max_ratio:.4f})',
                 fontsize=12)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110, bbox_inches='tight')
    plt.close(fig)
    print(f"Plot:      {OUT_PNG.name}")

    # 10. 4-tuple + verdict line
    tag = (f"(c_s_ratio={max_ratio:.6f}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n4-tuple: {tag}")

    verdict_line = (
        f"{GATE_ID}: {verdict} -- value={max_ratio:.6f} "
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
