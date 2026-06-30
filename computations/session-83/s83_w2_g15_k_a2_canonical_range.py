#!/usr/bin/env python3
"""
S83 W2-G15 — K-A2-CANONICAL-RANGE
=================================

Gate: S83-K-A2-CANONICAL-RANGE ([VERIFY])

Pre-registered threshold (from sessions/session-plan/session-83-plan.md
§W2-G15 L1231-L1237):
  PASS: span = max(k_a2_R)/min(k_a2_R) < 1.5
  INFO: 1.5 <= span <= 2.5
  FAIL: span > 2.5

4-tuple slot: (span=?, scheme={5-regulators},
               convention=Lambda_Z-M_KK-headline, L_max=5)

Classification: GEOMETRIC (spectral moment k_a2).

CONTEXT
-------
k_a2 is the a_2-slot smoothed-kernel factor from F_pivot_smooth(N)
decomposition per S82 W-2 (inherited via S80 W1-A slot audit). It
governs how the scalar-curvature Mellin-moment slot rescales the A_s
ledger across regulator schemes. At S80 W1-A, k_a2 was canonically
defined as:

    k_a2 := f_2^{sharp} / f_2^{f*} = 18.456 / 48.293 = 0.3822

where f_n^{R}(Lambda^2) := int_0^{Lambda^2} w_R(u) du are the
Chamseddine-Connes Mellin weights for the a_n slot at cutoff
Lambda^2 = lam_max^2 (per P4-C workshop, session-79).

For the 5-regulator span test we generalize by ALSO using f* as the
canonical denominator (the reference anchor for slot factor definition):

    k_a2^R := f_2^R / f_2^{f*}

This preserves the S80 W1-A definition: at R=sharp (= anomaly/dim-reg/
lattice-BR per CC convention, all of which give f(u)=1 on [0,L2]),
k_a2^R matches the canonical 0.382.

REGULATOR CONVENTION PIN (PRU Class 8)
--------------------------------------
The plan §W2-G15 L1234 lists {zeta, Zubarev, SDW, dim-reg, lattice-BR}
but does NOT pin Lambda_Z for Zubarev. This is a Pre-Registration
Underspecification (PRU Class 8). To prevent iterate-until-PASS
convention-shopping, we HEADLINE Convention A (Lambda_Z=M_KK, the
pin also used in S83 W2-G14 which PASSED at 1.227) and report
Convention B (Lambda_Z=matched-scale) as a SUPPLEMENTARY cross-check.
The verdict uses span_A.

SUBSTITUTION CHAIN [VERIFY]
---------------------------
Step 1 (definition, Chamseddine-Connes a_2 slot Mellin moment):
    f_2^R(Lambda^2) := int_0^{Lambda^2} w_R(u) du
    k_a2^R := f_2^R / f_2^{f*}  (f* is canonical slot-factor anchor)

Step 2 (substitute per regulator at L_max=5, Lambda^2 = lam_max^2):
    w_zeta(u)        = 1                                (flat Mellin)
    w_Zubarev(u)     = exp(-u / Lambda_Z^2)             (Gaussian mollifier)
       Convention A: Lambda_Z = M_KK = 1 in M_KK units  -> w = exp(-u)
       Convention B: Lambda_Z = sqrt(lam_max^2)         -> w = exp(-u/L2)
    w_SDW(u)         = sqrt(u)                          (Andrianov-Lizzi)
    w_dim-reg(u)     = 1 (at eps=0, MSbar)              (pole-subtracted)
    w_lattice-BR(u)  = 1 (bare continuum limit)         (Brillouin reg)
    w_f*(u)          = alpha*sqrt(u) + beta*exp(-u)     (S72 f_star)

    Closed forms:
      f_2^zeta(L2)      = L2
      f_2^Zubarev_A(L2) = int_0^{L2} exp(-u) du = 1 - exp(-L2)
      f_2^Zubarev_B(L2) = int_0^{L2} exp(-u/L2) du = L2 * (1 - 1/e)
      f_2^SDW(L2)       = (2/3) * L2^{3/2}
      f_2^dim-reg(L2)   = L2 (at eps=0)
      f_2^lattice-BR(L2)= L2 (continuum)
      f_2^f*(L2)        = alpha*(2/3)*L2^{3/2} + beta*(1 - exp(-L2))

Step 3 (simplify):
    span_A = max_{R in 5} k_a2^R / min_{R in 5} k_a2^R at Convention A
    span_B analogously at Convention B (supplementary)

Step 4 (direction):
    PASS if span_A < 1.5 (FI claim validated)
    INFO if 1.5 <= span_A <= 2.5 (borderline scheme-sensitive)
    FAIL if span_A > 2.5 (regulator-dominated, k_a2 scheme-dressed)

Step 5 (Python verification):
    Verified offline BEFORE this script run (math-scripts.md discipline):
      span_A at L_max=5 = 14.68  -> FAIL headline
      span_B at L_max=5 = 2.96   -> FAIL cross-check

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py        (closure hash)
  - s74_spectrum_cache_L9_tau019.npz   (D_K spectrum for lam_max at L_max=5)

Output 4-tuple:
  (span=<v>, scheme={zeta,Zubarev,SDW,dim-reg,lattice-BR},
   convention=Lambda_Z-M_KK-headline, L_max=5)
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

SESSION = "S83"                                       # (local)
GATE_ID = "S83-K-A2-CANONICAL-RANGE"                  # (local)
SCHEME = "5-regulators"                               # (local)
CONVENTION = "Lambda_Z-M_KK-headline"                 # (local)
L_MAX = 5                                             # (local) task-pinned

OUT_NPZ = SCRIPT_DIR / "s83_w2_g15_k_a2_canonical_range.npz"
OUT_PNG = SCRIPT_DIR / "s83_w2_g15_k_a2_canonical_range.png"
VERDICT_TXT = SCRIPT_DIR / "s83_gate_verdicts.txt"
SPECTRUM_CACHE = SCRIPT_DIR / "s74_spectrum_cache_L9_tau019.npz"  # (local)

INPUT_FILES = [
    SCRIPT_DIR / "canonical_constants.py",
    SPECTRUM_CACHE,
    SCRIPT_DIR / "s83_w2_g15_k_a2_canonical_range.py",
]

# Gate thresholds (pre-registered, plan L1236)
PASS_SPAN_THRESHOLD = 1.5                             # (local) FI factor-1.5 band
INFO_SPAN_THRESHOLD = 2.5                             # (local) scheme-dependent upper
EVAL_CUTOFF = 0.01                                    # (local) IR cutoff (match W2-G14/W2-8)

# SDW f_star parameters (S72 canonical — literal in this script, pinned at the
# spectral-functional fit, matches W2-8 / W2-G14 canonical usage).
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
# Section 6 — Analytic Mellin moments f_2^R(Lambda^2)
# ---------------------------------------------------------------------------

def f2_zeta(L2):
    """f_2^{zeta}(L2) = int_0^{L2} 1 du = L2 (flat Mellin weight)."""
    return float(L2)


def f2_Zubarev_A(L2):
    """f_2^{Zubarev-A}: Lambda_Z = M_KK = 1 in M_KK units.
       int_0^{L2} exp(-u) du = 1 - exp(-L2)."""
    return float(1.0 - np.exp(-L2))


def f2_Zubarev_B(L2):
    """f_2^{Zubarev-B}: Lambda_Z = sqrt(L2) (matched-scale).
       int_0^{L2} exp(-u/L2) du = L2 * (1 - 1/e)."""
    return float(L2 * (1.0 - np.exp(-1.0)))


def f2_SDW(L2):
    """f_2^{SDW}(L2) = int_0^{L2} sqrt(u) du = (2/3) L2^{3/2}."""
    return float((2.0/3.0) * L2 ** 1.5)


def f2_dimreg(L2):
    """f_2^{dim-reg}(L2): at eps=0 (MSbar pole-subtracted) reduces to L2.
       In MSbar the finite part after pole subtraction carries w(u)=1."""
    return float(L2)


def f2_lattice_BR(L2):
    """f_2^{lattice-BR}(L2): Brillouin regulator in continuum limit reduces
       to bare L2 value (finite-lattice corrections are higher-order in
       a_lat/Lambda and vanish at the continuum limit)."""
    return float(L2)


def f2_fstar(L2, alpha=ALPHA_STAR, beta=BETA_STAR):
    """f_2^{f*}(L2) = alpha*(2/3)*L2^{3/2} + beta*(1 - exp(-L2))."""
    return float(alpha * (2.0/3.0) * L2 ** 1.5 + beta * (1.0 - np.exp(-L2)))


def f2_numeric_zubarev_A(L2):
    """Numerical cross-check for Zubarev-A."""
    val, _ = integrate.quad(lambda u: np.exp(-u), 0.0, L2,
                            limit=500, epsabs=1e-14, epsrel=1e-12)
    return float(val)


def f2_numeric_zubarev_B(L2):
    """Numerical cross-check for Zubarev-B."""
    val, _ = integrate.quad(lambda u: np.exp(-u / L2), 0.0, L2,
                            limit=500, epsabs=1e-14, epsrel=1e-12)
    return float(val)


# ---------------------------------------------------------------------------
# Section 7 — k_a2^R assembler
# ---------------------------------------------------------------------------

def k_a2_convention(L2, convention):
    """
    Compute k_a2^R per 5-regulator scheme.

    Returns dict: {regulator: k_a2^R = f_2^R / f_2^{f*}}.

    convention='A': Lambda_Z = M_KK = 1 (M_KK units) for Zubarev.
    convention='B': Lambda_Z = sqrt(L2) matched-scale for Zubarev.
    """
    f2_fs = f2_fstar(L2)                                  # (local) denominator anchor
    if convention == 'A':
        zub = f2_Zubarev_A(L2)                            # (local)
    elif convention == 'B':
        zub = f2_Zubarev_B(L2)                            # (local)
    else:
        raise ValueError(f"Unknown convention: {convention}")
    k = {                                                 # (local)
        'zeta':       f2_zeta(L2)       / f2_fs,
        'Zubarev':    zub               / f2_fs,
        'SDW':        f2_SDW(L2)        / f2_fs,
        'dim-reg':    f2_dimreg(L2)     / f2_fs,
        'lattice-BR': f2_lattice_BR(L2) / f2_fs,
    }
    return k


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
        print("INCOMPUTABLE — cannot run without D_K spectrum for lam_max.")
        return 2
    cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
    sector_evals = cache['sector_evals'].item()
    cache.close()

    lam, mult = collect_spectrum(sector_evals, L_MAX, EVAL_CUTOFF)
    lam_max = float(lam.max())                             # (local)
    L2_primary = lam_max ** 2                              # (local) Lambda^2
    print(f"[L_max={L_MAX}] spectrum loaded:")
    print(f"  n_modes        = {len(lam)}")
    print(f"  lam_max (M_KK) = {lam_max:.6f}")
    print(f"  Lambda^2       = lam_max^2 = {L2_primary:.6f}")
    print(f"  sum(mult)      = {int(mult.sum())}")
    print()

    # 3. Analytic vs numerical cross-check for Zubarev (sanity)
    zub_A_ana = f2_Zubarev_A(L2_primary)                   # (local)
    zub_A_num = f2_numeric_zubarev_A(L2_primary)           # (local)
    zub_B_ana = f2_Zubarev_B(L2_primary)                   # (local)
    zub_B_num = f2_numeric_zubarev_B(L2_primary)           # (local)
    print(f"Analytic-numerical cross-check (Zubarev):")
    print(f"  Zubarev-A: analytic={zub_A_ana:.10e}  numeric={zub_A_num:.10e}  "
          f"|diff|={abs(zub_A_ana-zub_A_num):.2e}")
    print(f"  Zubarev-B: analytic={zub_B_ana:.10e}  numeric={zub_B_num:.10e}  "
          f"|diff|={abs(zub_B_ana-zub_B_num):.2e}")
    assert abs(zub_A_ana - zub_A_num) < 1e-9, "Zubarev-A analytic/numeric mismatch"
    assert abs(zub_B_ana - zub_B_num) < 1e-9, "Zubarev-B analytic/numeric mismatch"
    print()

    # 4. Compute k_a2^R at both conventions
    k_a2_A = k_a2_convention(L2_primary, 'A')
    k_a2_B = k_a2_convention(L2_primary, 'B')

    print("Convention A (Lambda_Z=M_KK=1 in M_KK units) — HEADLINE:")
    for R, v in k_a2_A.items():
        print(f"  k_a2[{R:>10s}] = {v:.6f}")
    vals_A = np.array(list(k_a2_A.values()))               # (local)
    max_A = float(vals_A.max())                            # (local)
    min_A = float(vals_A.min())                            # (local)
    span_A = max_A / min_A                                 # (local) headline metric
    print(f"  max(k_a2)  = {max_A:.6f}")
    print(f"  min(k_a2)  = {min_A:.6f}")
    print(f"  span_A     = {span_A:.6f}")
    print()

    print("Convention B (Lambda_Z=sqrt(lam_max^2) matched-scale) — CROSS-CHECK:")
    for R, v in k_a2_B.items():
        print(f"  k_a2[{R:>10s}] = {v:.6f}")
    vals_B = np.array(list(k_a2_B.values()))               # (local)
    max_B = float(vals_B.max())                            # (local)
    min_B = float(vals_B.min())                            # (local)
    span_B = max_B / min_B                                 # (local)
    print(f"  max(k_a2)  = {max_B:.6f}")
    print(f"  min(k_a2)  = {min_B:.6f}")
    print(f"  span_B     = {span_B:.6f}")
    print()

    # 5. Gate decision (HEADLINE from Convention A)
    print(f"PASS threshold         = span < {PASS_SPAN_THRESHOLD:.2f}")
    print(f"INFO upper threshold   = span < {INFO_SPAN_THRESHOLD:.2f}")
    print(f"FAIL                   = span >= {INFO_SPAN_THRESHOLD:.2f}")

    if span_A < PASS_SPAN_THRESHOLD:
        verdict = "PASS"
    elif span_A < INFO_SPAN_THRESHOLD:
        verdict = "INFO"
    else:
        verdict = "FAIL"
    print(f"\n=> Headline verdict (Convention A): {verdict}")

    # 6. Cross-check consistency with S83 W2-G14 (c_s at Zubarev Lambda=M_KK
    # PASSed with span 1.227). W2-G14 computed <lam^2> first-moment ratio; this
    # gate computes f_2 slot Mellin-moment ratios. Different observables; their
    # directional behaviors need not agree. We REPORT the W2-G14 reference,
    # then evaluate whether this gate's Zubarev behavior is internally
    # consistent with W2-G14's at the Lambda=M_KK scale.
    w2_g14_ratio = 1.2269                                  # (local) W2-G14 PASS ratio
    w2_g14_convention = "Lambda_Z=M_KK=1 (same as Convention A here)"  # (local)
    internal_consistency_zub_suppressed = bool(
        k_a2_A['Zubarev'] < k_a2_A['zeta']
    )
    # Expected direction: Zubarev's exp(-u) weight suppresses the a_2
    # integral relative to the flat weight at L2 > 1. f_2^{Zub-A}(L2) = 1 -
    # exp(-L2) asymptotes to 1 as L2 -> infty, while f_2^{zeta}(L2) = L2
    # grows linearly. So k_a2^{Zub-A} < k_a2^{zeta} at large L2.
    print(f"\nS83 W2-G14 cross-check:")
    print(f"  W2-G14 ratio (c_s, Zubarev-A) = {w2_g14_ratio:.4f} (PASS)")
    print(f"  This gate k_a2 Convention-A Zubarev < zeta: "
          f"{internal_consistency_zub_suppressed}")
    print(f"  (expected: TRUE; Zubarev mollifier suppresses UV tail at L2>1)")

    # 7. PRU Class 8 flag: the plan left Lambda_Z unpinned.
    pru_class8_flag = True                                 # (local)
    pru_note = (
        "PRU Class 8: plan §W2-G15 L1234 lists 5 regulators but does not pin "
        "Lambda_Z for Zubarev. Orchestrator pre-pinned Convention A "
        "(Lambda_Z=M_KK) as HEADLINE to match S83 W2-G14 Zubarev convention. "
        "Convention B (Lambda_Z=matched-scale) reported as SUPPLEMENTARY."
    )
    print(f"\nPRU Class 8 flag: {pru_class8_flag}")
    print(f"  {pru_note}")

    # 8. L_max robustness scan (diagnostic)
    L_max_scan = [3, 5, 7, 9]                              # (local)
    span_A_by_L = {}                                        # (local)
    span_B_by_L = {}                                        # (local)
    for L in L_max_scan:
        lam_L, _ = collect_spectrum(sector_evals, L, EVAL_CUTOFF)
        L2_L = float(lam_L.max() ** 2)                      # (local)
        k_A_L = k_a2_convention(L2_L, 'A')                  # (local)
        k_B_L = k_a2_convention(L2_L, 'B')                  # (local)
        vA = np.array(list(k_A_L.values()))                 # (local)
        vB = np.array(list(k_B_L.values()))                 # (local)
        span_A_by_L[L] = float(vA.max() / vA.min())
        span_B_by_L[L] = float(vB.max() / vB.min())
    print("\nL_max robustness scan (diagnostic):")
    print(f"  {'L':>3s}  {'Lambda^2':>10s}  {'span_A':>10s}  {'span_B':>10s}")
    for L in L_max_scan:
        lam_L, _ = collect_spectrum(sector_evals, L, EVAL_CUTOFF)
        L2_L = float(lam_L.max() ** 2)
        print(f"  {L:>3d}  {L2_L:>10.4f}  {span_A_by_L[L]:>10.4f}  "
              f"{span_B_by_L[L]:>10.4f}")

    # 9. Save artifacts
    np.savez(
        OUT_NPZ,
        L_max=L_MAX,
        n_modes=len(lam),
        lam_max=lam_max,
        Lambda_sq=L2_primary,
        # Convention A (HEADLINE)
        k_a2_A_zeta=k_a2_A['zeta'],
        k_a2_A_Zubarev=k_a2_A['Zubarev'],
        k_a2_A_SDW=k_a2_A['SDW'],
        k_a2_A_dimreg=k_a2_A['dim-reg'],
        k_a2_A_lattice_BR=k_a2_A['lattice-BR'],
        max_A=max_A,
        min_A=min_A,
        span_A=span_A,
        # Convention B (CROSS-CHECK)
        k_a2_B_zeta=k_a2_B['zeta'],
        k_a2_B_Zubarev=k_a2_B['Zubarev'],
        k_a2_B_SDW=k_a2_B['SDW'],
        k_a2_B_dimreg=k_a2_B['dim-reg'],
        k_a2_B_lattice_BR=k_a2_B['lattice-BR'],
        max_B=max_B,
        min_B=min_B,
        span_B=span_B,
        # L_max scan
        L_max_scan=np.array(L_max_scan),
        span_A_scan=np.array([span_A_by_L[L] for L in L_max_scan]),
        span_B_scan=np.array([span_B_by_L[L] for L in L_max_scan]),
        # Diagnostics
        f2_fstar=f2_fstar(L2_primary),
        PASS_SPAN_THRESHOLD=PASS_SPAN_THRESHOLD,
        INFO_SPAN_THRESHOLD=INFO_SPAN_THRESHOLD,
        w2_g14_ratio_reference=w2_g14_ratio,
        pru_class8_flag=pru_class8_flag,
        pru_note=pru_note,
        verdict=verdict,
        closure=closure,
    )
    print(f"\nArtifacts: {OUT_NPZ.name}")

    # 10. Plot — 2 panels: Convention A and Convention B side-by-side
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    ax0, ax1 = axes

    R_names = list(k_a2_A.keys())                          # (local)
    colors = ['#2c7fb8', '#d95f0e', '#31a354',
              '#c26dbc', '#7a7a7a']                        # (local)

    # Panel (a): Convention A — HEADLINE
    vals_A_plot = [k_a2_A[R] for R in R_names]             # (local)
    bars = ax0.bar(R_names, vals_A_plot, color=colors, alpha=0.85,
                   edgecolor='k', linewidth=0.5)
    ax0.axhline(min_A * PASS_SPAN_THRESHOLD, color='k', linestyle='--',
                label=f'PASS band top (min*{PASS_SPAN_THRESHOLD})')
    ax0.axhline(min_A * INFO_SPAN_THRESHOLD, color='gray', linestyle=':',
                label=f'INFO band top (min*{INFO_SPAN_THRESHOLD})')
    for b, v in zip(bars, vals_A_plot):
        ax0.text(b.get_x() + b.get_width() / 2., v + max_A * 0.02,
                 f'{v:.4f}', ha='center', va='bottom', fontsize=9)
    ax0.set_ylabel(r'$k_{a_2}^R$')
    ax0.set_title(f'Convention A (Lambda_Z=M_KK, HEADLINE)\n'
                  f'span = {span_A:.4f} -> {verdict}')
    ax0.legend(loc='upper right', fontsize=8)
    ax0.set_ylim(0, max_A * 1.35)
    ax0.grid(alpha=0.3)
    ax0.tick_params(axis='x', rotation=20)

    # Panel (b): Convention B — CROSS-CHECK
    if span_B < PASS_SPAN_THRESHOLD:
        v_B_label = "PASS"  # (local)
    elif span_B < INFO_SPAN_THRESHOLD:
        v_B_label = "INFO"  # (local)
    else:
        v_B_label = "FAIL"  # (local)
    vals_B_plot = [k_a2_B[R] for R in R_names]             # (local)
    bars = ax1.bar(R_names, vals_B_plot, color=colors, alpha=0.85,
                   edgecolor='k', linewidth=0.5)
    ax1.axhline(min_B * PASS_SPAN_THRESHOLD, color='k', linestyle='--',
                label=f'PASS band top (min*{PASS_SPAN_THRESHOLD})')
    ax1.axhline(min_B * INFO_SPAN_THRESHOLD, color='gray', linestyle=':',
                label=f'INFO band top (min*{INFO_SPAN_THRESHOLD})')
    for b, v in zip(bars, vals_B_plot):
        ax1.text(b.get_x() + b.get_width() / 2., v + max_B * 0.02,
                 f'{v:.4f}', ha='center', va='bottom', fontsize=9)
    ax1.set_ylabel(r'$k_{a_2}^R$')
    ax1.set_title(f'Convention B (Lambda_Z=matched, CROSS-CHECK)\n'
                  f'span = {span_B:.4f} -> {v_B_label}')
    ax1.legend(loc='upper right', fontsize=8)
    ax1.set_ylim(0, max_B * 1.35)
    ax1.grid(alpha=0.3)
    ax1.tick_params(axis='x', rotation=20)

    fig.suptitle(f'S83 W2-G15 K-A2-CANONICAL-RANGE — '
                 f'Headline {verdict} (span_A={span_A:.4f})',
                 fontsize=12)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110, bbox_inches='tight')
    plt.close(fig)
    print(f"Plot:      {OUT_PNG.name}")

    # 11. 4-tuple + verdict line
    tag = (f"(span_A={span_A:.6f}, span_B={span_B:.6f}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n4-tuple: {tag}")

    verdict_line = (
        f"{GATE_ID}: {verdict} -- value=span_A={span_A:.6f},span_B={span_B:.6f} "
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
