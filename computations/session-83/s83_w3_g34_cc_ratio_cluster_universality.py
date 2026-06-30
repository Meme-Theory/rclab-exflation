#!/usr/bin/env python3
"""
S83 W3-G34 — CC-RATIO-CLUSTER-UNIVERSALITY
=============================================

Gate: S83-CC-RATIO-CLUSTER-UNIVERSALITY  [VERIFY-THEOREM][CHAIN]
Classification: PHONONIC + GEOMETRIC (structural universality)
Owner: kaku-speculative-theorist

Pre-registration (sessions/session-plan/session-83-plan.md §W3-G34 L2144-L2186):
    HYPOTHESIS: The 5x3=15 CC-ratio-cluster table (5 regulators
    x 3 ratios {n_s/alpha_s, A_s/mu, f_NL/r}) demonstrates universality:
    cluster span < factor-1.5 in each column.
    PASS: all 3 ratio columns PASS factor-1.5
    INFO: all 3 spans < 2.5
    FAIL: any span > 2.5

4-tuple slot: (max_span=?, scheme=5-regulator-3-ratio,
               convention=CC-ratio-cluster, L_max=5)

CONTEXT — paradigmatic CC-ratio theorem test (S80 W1-4 substrate inheritance):
    S80 W1-4 CC-RATIOS-ONLY proved:
      * Weight-BALANCED ratios (same Mellin k): f_R CANCELS -> regulator
        independent to machine epsilon.
      * Weight-UNBALANCED ratios (different Mellin k): f_R RETAINS ->
        regulator-specific scheme dependence.
    This gate tests whether 3 paradigmatic CC-observable ratios sit at
    balanced OR unbalanced Mellin labels by directly propagating the
    5-regulator scheme through each ratio. The THEOREM predicts only
    balanced-label ratios PASS factor-1.5.

    Related prior gates this inherits from:
      * G14 PASS: c_s FI ratio 1.227 (zeta+Zubarev+SDW) — balanced k=2
      * G15 FAIL: k_a2 NOT-R-protected span 14.69 (5-regulators) — unbalanced
      * G16 PASS: A_s with 3PI substitution, 4/5 PASS
      * G28 FAIL: A_s cluster ratio span 14.69 linear-in-k_a2
      * G33: ratio-probe-lead-indicator (pair-predictor)

SUBSTITUTION CHAIN [VERIFY-THEOREM][CHAIN] (mandatory, math-scripts.md):

    Step 1 (Definition of the three observables and their regulator dependence).
        (i)  f_conv^R := pi^4 / (9216 * (M_0^R)^2)                 [framework]
             M_0^R    := 0.5 * sum_j d_j * w_R(lam_j)              [spectrum-level]
        (ii) n_s       := ns_framework (fold-canonical zero-loop)
                          [structurally scheme-invariant at BCS+1-loop]
        (iii) alpha_s  := d n_s / d ln k  carries (f_2^R / f_4^R) UNBALANCED
                          Mellin-moment ratio (dS/dln k involves a_4 slot).
                          Structural form:
                            alpha_s^R = alpha_s_fold * (f_2^R / f_4^R) /
                                        (f_2^{zeta} / f_4^{zeta})
                          (regulator-multiplier, normalized to zeta at 1).
        (iv) A_s       := prefactor * f_conv^R * (ledger factors)
                          [LINEAR in f_conv^R, other ledger factors R-invariant]
        (v)  mu        := bispectrum amplitude via N_pair. Framework result:
                          mu ~ 1/N_pair ~ 1/M_0^R ~ sqrt(f_conv^R) structurally.
                          (N_pair = 2*M_0 = multiplicity-weighted count.)
                          More precisely: N_pair^R = 2*M_0^R, so
                          mu^R = const_mu / N_pair^R = const_mu / (2*M_0^R).
                          In terms of f_conv: since f_conv = pi^4/(9216*M_0^2),
                          M_0 = sqrt(pi^4 / (9216*f_conv)) = C/sqrt(f_conv).
                          So mu = const_mu / (2*C/sqrt(f_conv)) = K * sqrt(f_conv)
                          where K = const_mu / (2*C). mu ~ sqrt(f_conv).
        (vi) f_NL      := f_NL^folded = N_pair^{-1/2}  (CLT diagonal GGE, S67)
                          So f_NL ~ 1/sqrt(M_0^R) ~ f_conv^{1/4} structurally.
                          More precisely: N_pair = 2*M_0 => f_NL = 1/sqrt(2*M_0).
        (vii) r        := r_FW (transit, tensor-to-scalar). In framework,
                          r = 16*eps_H is INAPPLICABLE (VdD-Hawking workshop
                          established 5 independent arguments); transit-derived
                          r_FW = 0.0242 is R-INVARIANT at leading order.

    Step 2 (Substitute — 5 regulators at L_max=5, Lambda_Z = M_KK = 1 Conv A).
        Canonical weights (matching S83 W2-G14, W2-G15, W3-G28):
          w_zeta(lam)      = 1                              (flat)
          w_Zubarev(lam)   = exp(-lam^2/Lambda_Z^2), LZ=M_KK=1 (Gaussian mollifier)
          w_SDW(lam)       = alpha*sqrt(x) + beta*exp(-x),
                             x = lam^2/lam_max^2,
                             (alpha, beta) = (0.912, 0.088)
          w_dim-reg(lam)   = 1 (MSbar, eps=0, pole-subtracted; flat after pole)
          w_lattice-BR(lam)= 1 (continuum limit of Brillouin regulator)

        Mellin-moment weights (for f_2^R / f_4^R in alpha_s correction):
          w_zeta-moment(u)      = 1
          w_Zubarev-moment(u)   = exp(-u) (Conv A, Lambda_Z=1)
          w_SDW-moment(u)       = alpha*sqrt(x_u) + beta*exp(-x_u),
                                  x_u = u/L2_max
          w_dim-reg-moment(u)   = 1
          w_lattice-moment(u)   = 1

        f_2^R = integral_0^L2 w_R^moment(u) du
        f_4^R = integral_0^L2 w_R^moment(u) * u du

    Step 3 (Simplify per ratio — theorem-predicted scheme behavior).

        Ratio 1: n_s / alpha_s
          n_s^R          = n_s_fold                (scheme-invariant zero-loop)
          alpha_s^R      = alpha_s_fold * g^R,
                           g^R = (f_2^R/f_4^R) / (f_2^{zeta}/f_4^{zeta})
          n_s/alpha_s^R  = (n_s_fold/alpha_s_fold) * (1/g^R)
          span_1         = max_R (1/g^R) / min_R (1/g^R) = span(f_4^R/f_2^R)
                           This is the UNBALANCED ratio (S80 theorem: f RETAINS).
                           => span_1 LARGE (similar to G15 k_a2 span 14.69).

        Ratio 2: A_s / mu
          A_s^R          = K_A * f_conv^R          (LINEAR in f_conv)
          mu^R           = K_mu * sqrt(f_conv^R)   (sqrt in f_conv)
          A_s/mu^R       = (K_A/K_mu) * sqrt(f_conv^R)
          span_2         = max_R sqrt(f_conv^R) / min_R sqrt(f_conv^R)
                         = sqrt(cluster_{f_conv}(R))
                           This is a PARTIAL UNBALANCE: the ratio carries
                           sqrt(f_conv) scheme dependence. So span_2 = sqrt(span_{f_conv}).

          CORRECTION — CLARIFY:
          The RATIO A_s/mu under this definition depends on
          sqrt(f_conv), because A_s is linear and mu is 1/M_0 = sqrt(f_conv)*const.
          If G28 found cluster_{f_conv} = span_k_a2 inheriting G15 = 14.69, then
          sqrt(14.69) ~ 3.83. But G28 computed f_conv-observable cluster using
          M_0 directly with each w_R weight function on spectrum, getting
          its own span. We compute fresh here.

        Ratio 3: f_NL / r
          f_NL^R         = 1/sqrt(2*M_0^R)          (CLT GGE diagonal)
          r^R            = r_FW                      (transit, R-invariant)
          f_NL/r^R       = 1/(r_FW * sqrt(2*M_0^R))
          span_3         = max_R (1/sqrt(M_0^R)) / min_R (1/sqrt(M_0^R))
                         = sqrt(max_R M_0^R / min_R M_0^R)
                           This also inherits M_0 span / f_conv span via sqrt.

    Step 4 (Direction — pre-registered thresholds).
        PASS if all 3 spans < 1.5 (universality validated)
        INFO if all 3 spans < 2.5 (moderate scheme sensitivity, NOT universal)
        FAIL if any span >= 2.5 (scheme dependence dominates structural content)

    Step 5 (Python verification — plan snippet).
        regulators = ['zeta','Zubarev','SDW','dim-reg','lattice-BR']
        ratios = ['ns_over_alphas', 'As_over_mu', 'fNL_over_r']
        values = {(reg, r): compute_ratio(reg, r) for reg in regulators for r in ratios}
        spans = {r: max(values[(reg,r)] for reg in regulators) /
                    min(values[(reg,r)] for reg in regulators) for r in ratios}
        all_pass = all(s < 1.5 for s in spans.values())

    STRUCTURAL EXPECTATION (pre-run, Kaku-Speculative-Theorist analysis):
        The three-column table is a paradigmatic constraint map, not a
        universality claim. Per S80 W1-4 theorem:
          * A_s/mu: PARTIAL BALANCE — both carry f_conv^R dependence but
            at DIFFERENT powers (1 vs 1/2). Ratio RETAINS sqrt(f_conv)
            dependence. Expected span = sqrt(f_conv cluster).
          * n_s/alpha_s: UNBALANCED (f_2/f_4 Mellin labels differ). span
            RETAINS f_2/f_4 ratio dependence. Expected LARGE span.
          * f_NL/r: transit-r is R-invariant by construction; f_NL ~
            1/sqrt(M_0). Span = sqrt(M_0 cluster).
        Prediction: all three spans likely > 1.5 (theorem-consistent).

L_max:  5 (task-pinned; matches W2-G14/G15/G16, W3-G28)
Cross-check at L_max in {3, 7, 9}.

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py
  - s74_spectrum_cache_L9_tau019.npz   (D_K spectrum at tau_fold)
  - this script

Output 4-tuple:
  (max_span=<v>, scheme=5-regulator-3-ratio,
   convention=CC-ratio-cluster, L_max=5)
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401, F403
from canonical_constants import PI, M_KK, tau_fold, ns_framework, planck_alpha_s

# ---------------------------------------------------------------------------
# Section 2 — Standard imports (CPU thread cap BEFORE numpy)
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
# Section 3 — Paths + pre-registration constants
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

SESSION = "S83"                                                    # (local)
GATE_ID = "S83-CC-RATIO-CLUSTER-UNIVERSALITY"                      # (local)
SCHEME = "5-regulator-3-ratio"                                     # (local)
CONVENTION = "CC-ratio-cluster"                                    # (local)
L_MAX = 5                                                          # (local) task-pinned

OUT_NPZ = SCRIPT_DIR / "s83_w3_g34_cc_ratio_cluster_universality.npz"
OUT_PNG = SCRIPT_DIR / "s83_w3_g34_cc_ratio_cluster_universality.png"
VERDICT_TXT = SCRIPT_DIR / "s83_gate_verdicts.txt"
SPECTRUM_CACHE = SCRIPT_DIR / "s74_spectrum_cache_L9_tau019.npz"   # (local)

INPUT_FILES = [
    SCRIPT_DIR / "canonical_constants.py",
    SPECTRUM_CACHE,
    SCRIPT_DIR / "s83_w3_g34_cc_ratio_cluster_universality.py",
]

# Pre-registered thresholds (plan L2155-L2156)
PASS_SPAN_THRESHOLD = 1.5                                          # (local)
INFO_SPAN_THRESHOLD = 2.5                                          # (local)
EVAL_CUTOFF = 0.01                                                 # (local) IR cutoff, matches W3-G28/W2-G15

# Regulator convention pins (matches W2-G14, W2-G15, W3-G28 Convention A)
LAMBDA_Z_A = 1.0                                                   # (local) M_KK units
ALPHA_STAR = 0.912                                                 # (local) SDW f_star sqrt weight
BETA_STAR  = 0.088                                                 # (local) SDW f_star exp weight

# Transit-derived r (r_FW from canonical_constants / S69 PVD07)
R_FW = 0.0242                                                      # (local) r_FW, S69 PVD07 / S77 domain_wall

# n_s, alpha_s central values at fold (framework canonical, scheme-invariant at zero-loop)
N_S_FOLD = ns_framework                                            # (local alias) = 0.9595
ALPHA_S_FOLD = -1.0e-3                                             # (local) framework alpha_s zero-loop central
                                                                    # (framework zero-loop alpha_s ~ 0; we seed 1e-3 for
                                                                    # ratio scaling without nullifying the test. The SCALED
                                                                    # g^R multiplier is what carries regulator structure.)


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
# Section 5 — Spectrum loader (L_max filter)
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
# Section 6 — Regulator weights (lam-level for M_0, u-level for Mellin moments)
# ---------------------------------------------------------------------------

# LAM-level weights (M_0 assembly)
def w_zeta_lam(lam):
    return np.ones_like(lam, dtype=np.float64)


def w_Zubarev_lam(lam, Lambda_Z=LAMBDA_Z_A):
    return np.exp(-(lam / Lambda_Z) ** 2)


def w_SDW_lam(lam, lam_max=None, alpha=ALPHA_STAR, beta=BETA_STAR):
    if lam_max is None:
        lam_max = float(np.max(lam))
    x = (lam / lam_max) ** 2          # (local)
    return alpha * np.sqrt(x) + beta * np.exp(-x)


def w_dimreg_lam(lam):
    return np.ones_like(lam, dtype=np.float64)


def w_latticeBR_lam(lam):
    return np.ones_like(lam, dtype=np.float64)


def M0_of(lam, mult, weight_fn, **kw):
    """M_0^R = 0.5 * sum_j d_j * w_R(lam_j), spectrum-level."""
    w = weight_fn(lam, **kw) if kw else weight_fn(lam)   # (local)
    return float(0.5 * np.sum(mult * w))


def f_conv_of(M0):
    """f_conv = pi^4 / (9216 * M_0^2)  (framework canonical, S77-B3 / S76)."""
    if M0 <= 0.0 or not np.isfinite(M0):
        return float('nan')
    return float(PI ** 4 / (9216.0 * M0 ** 2))


# ---------------------------------------------------------------------------
# Section 7 — Mellin-moment computations (for alpha_s regulator dependence)
# ---------------------------------------------------------------------------

def f_k_moment(regulator, k, L2, lam_max_local=None):
    """
    f_k^R(L2) = int_0^{L2} w_R^moment(u) * u^{k/2-1} du.

    For k=2: f_2 = int_0^L2 w_R(u) du
    For k=4: f_4 = int_0^L2 w_R(u) * u du

    w_R^moment(u) is the MELLIN-VARIABLE form (u = lam^2 in M_KK^2 units).
    """
    if regulator == 'zeta':
        wfunc = lambda u: 1.0
    elif regulator == 'Zubarev':
        # Conv A: Lambda_Z = 1 in M_KK units
        wfunc = lambda u: np.exp(-u)
    elif regulator == 'SDW':
        # w_SDW^moment(u) = alpha*sqrt(x_u) + beta*exp(-x_u), x_u = u/L2_primary
        L2_ref = L2 if lam_max_local is None else lam_max_local ** 2  # (local)
        wfunc = lambda u: ALPHA_STAR * np.sqrt(u / L2_ref) + BETA_STAR * np.exp(-u / L2_ref)
    elif regulator == 'dim-reg':
        wfunc = lambda u: 1.0
    elif regulator == 'lattice-BR':
        wfunc = lambda u: 1.0
    else:
        raise ValueError(f"Unknown regulator: {regulator}")

    integrand = lambda u: wfunc(u) * u ** (k / 2.0 - 1.0)  # (local)
    val, _ = integrate.quad(integrand, 0.0, L2, limit=500, epsabs=1e-14, epsrel=1e-12)
    return float(val)


# ---------------------------------------------------------------------------
# Section 8 — Compute the three ratio sets per regulator
# ---------------------------------------------------------------------------

def compute_five_regulators_ratios(lam, mult):
    """
    Compute the 5x3 table:
      regulators x {ns_over_alphas, As_over_mu, fNL_over_r}.

    Returns:
      data: dict with keys:
        M0           : dict{R: M_0^R}
        f_conv       : dict{R: f_conv^R}
        f_2          : dict{R: f_2^R}
        f_4          : dict{R: f_4^R}
        g            : dict{R: (f_2^R/f_4^R)/(f_2^{zeta}/f_4^{zeta})}
        n_s          : dict{R: n_s (scheme-invariant)}
        alpha_s      : dict{R: alpha_s_fold * g^R}
        A_s          : dict{R: K_A * f_conv^R} — K_A free (cancels in ratio)
        mu           : dict{R: K_mu * sqrt(f_conv^R)} — K_mu free (cancels in ratio)
        f_NL         : dict{R: 1/sqrt(2*M_0^R)}
        r            : dict{R: r_FW}
        ratio_ns_alphas : dict{R}
        ratio_As_mu     : dict{R}
        ratio_fNL_r     : dict{R}
    """
    lam_max = float(lam.max())   # (local)
    L2_primary = lam_max ** 2    # (local)

    # --- M_0 and f_conv per regulator ---
    M0 = {
        'zeta':       M0_of(lam, mult, w_zeta_lam),
        'Zubarev':    M0_of(lam, mult, w_Zubarev_lam, Lambda_Z=LAMBDA_Z_A),
        'SDW':        M0_of(lam, mult, w_SDW_lam, lam_max=lam_max),
        'dim-reg':    M0_of(lam, mult, w_dimreg_lam),
        'lattice-BR': M0_of(lam, mult, w_latticeBR_lam),
    }
    f_conv = {R: f_conv_of(v) for R, v in M0.items()}

    # --- Mellin moments f_2 and f_4 per regulator ---
    f_2 = {R: f_k_moment(R, 2, L2_primary, lam_max_local=lam_max)
           for R in M0.keys()}
    f_4 = {R: f_k_moment(R, 4, L2_primary, lam_max_local=lam_max)
           for R in M0.keys()}

    # --- g^R multiplier for alpha_s: normalized so g^{zeta}=1 ---
    ratio_24_zeta = f_2['zeta'] / f_4['zeta']       # (local) reference
    g = {R: (f_2[R] / f_4[R]) / ratio_24_zeta for R in M0.keys()}

    # --- n_s (scheme-invariant at fold zero-loop) ---
    n_s = {R: N_S_FOLD for R in M0.keys()}

    # --- alpha_s with regulator-driven correction via f_2/f_4 Mellin unbalance ---
    alpha_s = {R: ALPHA_S_FOLD * g[R] for R in M0.keys()}

    # --- A_s (linear in f_conv) and mu (sqrt in f_conv via 1/M_0) ---
    # We do NOT need absolute normalization — ratio cancels prefactors.
    # Use bare proportionals.
    A_s  = {R: f_conv[R] for R in M0.keys()}          # K_A absorbed
    mu   = {R: 1.0 / M0[R] for R in M0.keys()}        # K_mu absorbed; mu ~ 1/N_pair ~ 1/M_0

    # --- f_NL (CLT GGE diagonal) and r (transit, R-invariant) ---
    # N_pair = 2*M_0; f_NL = 1/sqrt(N_pair) = 1/sqrt(2*M_0)
    f_NL = {R: 1.0 / np.sqrt(2.0 * M0[R]) for R in M0.keys()}
    r    = {R: R_FW for R in M0.keys()}

    # --- Compute the three ratios ---
    ratio_ns_alphas = {R: n_s[R] / alpha_s[R] for R in M0.keys()}
    ratio_As_mu     = {R: A_s[R] / mu[R] for R in M0.keys()}
    ratio_fNL_r     = {R: f_NL[R] / r[R] for R in M0.keys()}

    return {
        'M0': M0,
        'f_conv': f_conv,
        'f_2': f_2,
        'f_4': f_4,
        'g': g,
        'n_s': n_s,
        'alpha_s': alpha_s,
        'A_s': A_s,
        'mu': mu,
        'f_NL': f_NL,
        'r': r,
        'ratio_ns_alphas': ratio_ns_alphas,
        'ratio_As_mu': ratio_As_mu,
        'ratio_fNL_r': ratio_fNL_r,
    }


def span_of(d):
    """Span = max/min across regulators, signed-magnitude-safe."""
    vals = np.array([abs(v) for v in d.values()])   # (local) magnitude
    if vals.min() <= 0:
        return float('inf')
    return float(vals.max() / vals.min())


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins + closure
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...")
    print(f"  full closure: {closure}")
    print()

    # 2. Load spectrum
    if not SPECTRUM_CACHE.exists():
        print(f"SPECTRUM CACHE MISSING: {SPECTRUM_CACHE}")
        print("INCOMPUTABLE — cannot run without D_K spectrum.")
        return 2
    cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
    sector_evals = cache['sector_evals'].item()
    cache.close()

    lam, mult = collect_spectrum(sector_evals, L_MAX, EVAL_CUTOFF)
    lam_max = float(lam.max())                 # (local)
    print(f"[L_max={L_MAX}] spectrum loaded:")
    print(f"  n_modes     = {len(lam)}")
    print(f"  lam_max     = {lam_max:.6f} M_KK")
    print(f"  Lambda^2    = {lam_max**2:.6f} M_KK^2")
    print(f"  sum(mult)   = {int(mult.sum())}")
    print(f"  tau_fold    = {tau_fold}")
    print()

    # 3. Compute the 5x3 table
    result = compute_five_regulators_ratios(lam, mult)
    regulators = ['zeta', 'Zubarev', 'SDW', 'dim-reg', 'lattice-BR']

    # --- Diagnostics: M_0, f_conv, f_2, f_4, g per regulator ---
    print("Intermediate quantities (Convention A, Lambda_Z=M_KK=1):")
    print(f"  {'R':>12s} | {'M_0':>12s} | {'f_conv':>12s} | {'f_2':>12s} | "
          f"{'f_4':>12s} | {'g^R':>10s}")
    for R in regulators:
        print(f"  {R:>12s} | {result['M0'][R]:>12.4e} | "
              f"{result['f_conv'][R]:>12.4e} | "
              f"{result['f_2'][R]:>12.4e} | {result['f_4'][R]:>12.4e} | "
              f"{result['g'][R]:>10.4f}")
    print()

    # --- The 5x3 observable-ratio table ---
    print("=" * 78)
    print("CC-RATIO-CLUSTER TABLE (5 regulators x 3 ratios)")
    print("=" * 78)
    print(f"  {'R':>12s} | {'n_s/alpha_s':>16s} | {'A_s/mu':>14s} | "
          f"{'f_NL/r':>14s}")
    for R in regulators:
        r1 = result['ratio_ns_alphas'][R]
        r2 = result['ratio_As_mu'][R]
        r3 = result['ratio_fNL_r'][R]
        print(f"  {R:>12s} | {r1:>16.6e} | {r2:>14.6e} | {r3:>14.6e}")
    print()

    # --- Per-column spans ---
    span_1 = span_of(result['ratio_ns_alphas'])
    span_2 = span_of(result['ratio_As_mu'])
    span_3 = span_of(result['ratio_fNL_r'])

    print("Per-column spans (max/min across 5 regulators):")
    print(f"  Column 1  n_s/alpha_s : span = {span_1:.6f}")
    print(f"  Column 2  A_s/mu      : span = {span_2:.6f}")
    print(f"  Column 3  f_NL/r      : span = {span_3:.6f}")
    print()

    max_span = max(span_1, span_2, span_3)  # (local)
    all_pass = span_1 < PASS_SPAN_THRESHOLD and \
               span_2 < PASS_SPAN_THRESHOLD and \
               span_3 < PASS_SPAN_THRESHOLD
    all_info = span_1 < INFO_SPAN_THRESHOLD and \
               span_2 < INFO_SPAN_THRESHOLD and \
               span_3 < INFO_SPAN_THRESHOLD

    # --- Pre-registered verdict ---
    if all_pass:
        verdict = "PASS"
    elif all_info:
        verdict = "INFO"
    else:
        verdict = "FAIL"

    print(f"PASS threshold : all 3 spans < {PASS_SPAN_THRESHOLD:.2f}")
    print(f"INFO threshold : all 3 spans < {INFO_SPAN_THRESHOLD:.2f}")
    print(f"FAIL trigger   : any span >= {INFO_SPAN_THRESHOLD:.2f}")
    print()
    print(f"=> Verdict: {verdict} (max_span = {max_span:.4f})")
    print()

    # --- Structural interpretation (S80 theorem prediction vs measurement) ---
    print("STRUCTURAL INTERPRETATION (S80 CC-RATIOS-ONLY theorem):")
    # Expected span_1 (unbalanced k=2 vs k=4)
    expected_span_1 = span_of(
        {R: result['f_4'][R] / result['f_2'][R] for R in regulators}
    )
    # Expected span_2 = sqrt(f_conv cluster)
    expected_span_2 = np.sqrt(span_of(result['f_conv']))
    # Expected span_3 = sqrt(M_0 cluster)
    expected_span_3 = np.sqrt(span_of(result['M0']))
    print(f"  Theorem-predicted span_1 (unbalanced f_4/f_2): {expected_span_1:.4f}")
    print(f"    -> measured span_1 = {span_1:.4f}  (agreement: {abs(span_1-expected_span_1)/max(span_1, 1e-12):.4%})")
    print(f"  Theorem-predicted span_2 (sqrt(f_conv cluster)): {expected_span_2:.4f}")
    print(f"    -> measured span_2 = {span_2:.4f}  (agreement: {abs(span_2-expected_span_2)/max(span_2, 1e-12):.4%})")
    print(f"  Theorem-predicted span_3 (sqrt(M_0 cluster)): {expected_span_3:.4f}")
    print(f"    -> measured span_3 = {span_3:.4f}  (agreement: {abs(span_3-expected_span_3)/max(span_3, 1e-12):.4%})")
    print()

    # --- L_max robustness scan (diagnostic) ---
    L_max_scan = [3, 5, 7, 9]                              # (local)
    span_scan = {}                                          # (local)
    for L in L_max_scan:
        lam_L, mult_L = collect_spectrum(sector_evals, L, EVAL_CUTOFF)
        if len(lam_L) == 0:
            continue
        res_L = compute_five_regulators_ratios(lam_L, mult_L)
        s1 = span_of(res_L['ratio_ns_alphas'])  # (local)
        s2 = span_of(res_L['ratio_As_mu'])      # (local)
        s3 = span_of(res_L['ratio_fNL_r'])      # (local)
        span_scan[L] = (s1, s2, s3)
    print("L_max robustness scan (diagnostic):")
    print(f"  {'L':>3s}  {'span_1':>10s}  {'span_2':>10s}  {'span_3':>10s}")
    for L in L_max_scan:
        if L in span_scan:
            s1, s2, s3 = span_scan[L]
            print(f"  {L:>3d}  {s1:>10.4f}  {s2:>10.4f}  {s3:>10.4f}")

    # --- Save artifacts ---
    np.savez(
        OUT_NPZ,
        L_max=L_MAX,
        n_modes=len(lam),
        lam_max=lam_max,
        Lambda_sq=lam_max ** 2,
        # Table 1: intermediate
        M0_zeta=result['M0']['zeta'],
        M0_Zubarev=result['M0']['Zubarev'],
        M0_SDW=result['M0']['SDW'],
        M0_dimreg=result['M0']['dim-reg'],
        M0_lattice_BR=result['M0']['lattice-BR'],
        f_conv_zeta=result['f_conv']['zeta'],
        f_conv_Zubarev=result['f_conv']['Zubarev'],
        f_conv_SDW=result['f_conv']['SDW'],
        f_conv_dimreg=result['f_conv']['dim-reg'],
        f_conv_lattice_BR=result['f_conv']['lattice-BR'],
        f_2_zeta=result['f_2']['zeta'],
        f_2_Zubarev=result['f_2']['Zubarev'],
        f_2_SDW=result['f_2']['SDW'],
        f_2_dimreg=result['f_2']['dim-reg'],
        f_2_lattice_BR=result['f_2']['lattice-BR'],
        f_4_zeta=result['f_4']['zeta'],
        f_4_Zubarev=result['f_4']['Zubarev'],
        f_4_SDW=result['f_4']['SDW'],
        f_4_dimreg=result['f_4']['dim-reg'],
        f_4_lattice_BR=result['f_4']['lattice-BR'],
        g_zeta=result['g']['zeta'],
        g_Zubarev=result['g']['Zubarev'],
        g_SDW=result['g']['SDW'],
        g_dimreg=result['g']['dim-reg'],
        g_lattice_BR=result['g']['lattice-BR'],
        # Ratios per regulator
        ns_over_alphas_zeta=result['ratio_ns_alphas']['zeta'],
        ns_over_alphas_Zubarev=result['ratio_ns_alphas']['Zubarev'],
        ns_over_alphas_SDW=result['ratio_ns_alphas']['SDW'],
        ns_over_alphas_dimreg=result['ratio_ns_alphas']['dim-reg'],
        ns_over_alphas_lattice_BR=result['ratio_ns_alphas']['lattice-BR'],
        As_over_mu_zeta=result['ratio_As_mu']['zeta'],
        As_over_mu_Zubarev=result['ratio_As_mu']['Zubarev'],
        As_over_mu_SDW=result['ratio_As_mu']['SDW'],
        As_over_mu_dimreg=result['ratio_As_mu']['dim-reg'],
        As_over_mu_lattice_BR=result['ratio_As_mu']['lattice-BR'],
        fNL_over_r_zeta=result['ratio_fNL_r']['zeta'],
        fNL_over_r_Zubarev=result['ratio_fNL_r']['Zubarev'],
        fNL_over_r_SDW=result['ratio_fNL_r']['SDW'],
        fNL_over_r_dimreg=result['ratio_fNL_r']['dim-reg'],
        fNL_over_r_lattice_BR=result['ratio_fNL_r']['lattice-BR'],
        # Spans
        span_1_ns_alphas=span_1,
        span_2_As_mu=span_2,
        span_3_fNL_r=span_3,
        max_span=max_span,
        # Theorem predictions
        expected_span_1=expected_span_1,
        expected_span_2=expected_span_2,
        expected_span_3=expected_span_3,
        # L_max scan
        L_max_scan=np.array(L_max_scan),
        span_scan_ns_alphas=np.array([span_scan.get(L, (np.nan,)*3)[0] for L in L_max_scan]),
        span_scan_As_mu=np.array([span_scan.get(L, (np.nan,)*3)[1] for L in L_max_scan]),
        span_scan_fNL_r=np.array([span_scan.get(L, (np.nan,)*3)[2] for L in L_max_scan]),
        # Gate pins
        PASS_SPAN_THRESHOLD=PASS_SPAN_THRESHOLD,
        INFO_SPAN_THRESHOLD=INFO_SPAN_THRESHOLD,
        verdict=verdict,
        closure=closure,
    )
    print(f"\nArtifacts: {OUT_NPZ.name}")

    # --- Plot: 2 panels — (a) 5x3 heatmap; (b) per-column spans vs thresholds ---
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    ax0, ax1 = axes

    # Panel (a): 5x3 heatmap of log10(ratio/reference)
    ratio_array = np.array([
        [result['ratio_ns_alphas'][R] for R in regulators],
        [result['ratio_As_mu'][R] for R in regulators],
        [result['ratio_fNL_r'][R] for R in regulators],
    ])
    # Normalize each row to its zeta reference for heatmap contrast
    norm_ratio = ratio_array / ratio_array[:, 0:1]
    im = ax0.imshow(np.log10(np.abs(norm_ratio)), aspect='auto', cmap='RdBu_r',
                    vmin=-1.5, vmax=1.5)
    ax0.set_xticks(range(5))
    ax0.set_xticklabels(regulators, rotation=20)
    ax0.set_yticks(range(3))
    ax0.set_yticklabels(['n_s/alpha_s', 'A_s/mu', 'f_NL/r'])
    for i in range(3):
        for j in range(5):
            ax0.text(j, i, f"{norm_ratio[i,j]:.3f}", ha='center', va='center',
                     fontsize=9, color='black' if abs(norm_ratio[i,j]-1) < 0.5 else 'white')
    plt.colorbar(im, ax=ax0, label='log10(ratio / zeta_ref)')
    ax0.set_title('5x3 CC-Ratio Cluster Table\n(normalized to zeta, per row)')

    # Panel (b): per-column spans with thresholds
    col_labels = ['n_s/alpha_s', 'A_s/mu', 'f_NL/r']
    col_spans = [span_1, span_2, span_3]
    col_colors = ['#2c7fb8', '#d95f0e', '#31a354']
    bars = ax1.bar(col_labels, col_spans, color=col_colors, alpha=0.85,
                   edgecolor='k', linewidth=0.5)
    ax1.axhline(PASS_SPAN_THRESHOLD, color='k', linestyle='--',
                label=f'PASS threshold ({PASS_SPAN_THRESHOLD})')
    ax1.axhline(INFO_SPAN_THRESHOLD, color='gray', linestyle=':',
                label=f'INFO threshold ({INFO_SPAN_THRESHOLD})')
    for b, v in zip(bars, col_spans):
        ax1.text(b.get_x() + b.get_width() / 2.,
                 v + max(col_spans) * 0.02,
                 f'{v:.3f}', ha='center', va='bottom', fontsize=10)
    ax1.set_ylabel('Span (max / min across 5 regulators)')
    ax1.set_yscale('log')
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_title(f'CC-Ratio Cluster Spans — {verdict}\n'
                  f'max_span = {max_span:.3f} (threshold {PASS_SPAN_THRESHOLD})')
    ax1.grid(alpha=0.3, which='both')

    fig.suptitle(f'S83 W3-G34 CC-RATIO-CLUSTER-UNIVERSALITY — '
                 f'{verdict} (5x3 regulator atlas)', fontsize=12)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110, bbox_inches='tight')
    plt.close(fig)
    print(f"Plot:      {OUT_PNG.name}")

    # --- 4-tuple + verdict line ---
    tag = (f"(max_span={max_span:.6f}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n4-tuple: {tag}")

    verdict_line = (
        f"{GATE_ID}: {verdict} -- value=max_span={max_span:.6f},"
        f"span_1={span_1:.6f},span_2={span_2:.6f},span_3={span_3:.6f} "
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
