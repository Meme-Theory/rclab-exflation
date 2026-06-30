#!/usr/bin/env python3
"""
S83 W3-G28 — F-CONV-CLUSTER-TEST (W2-8 REDIRECT, OBSERVABLE LEVEL)
====================================================================

Gate: S83-F-CONV-CLUSTER-TEST  [VERIFY][AUDIT]
Classification: PHONONIC
Owner: gen-physicist

Pre-registration (sessions/session-plan/session-83-plan.md §W3-G28 L1881-L1886):
    HYPOTHESIS: f_conv(pivot) computed at observable level (A_s prediction)
    clusters within factor-2 across 5 regulator conventions, even though
    f_conv-per-convention pointwise may differ more.
    PASS: observable-level A_s ratio across 5 conventions < 2
    INFO: ratio in [2, 3]
    FAIL: ratio >= 3

4-tuple slot: (cluster_ratio=?, scheme=f_conv-observable-level,
               convention=5-regulator-atlas, L_max=5)

CONTEXT (W2-8 redirect):
    S82 W2-8 tested a_n slot variance across 5 regulators at POINTWISE level
    and FAILed (var_a2=60.35%, FULL-5-SCHEME-CLUSTER). This gate REDIRECTS:
    does the OBSERVABLE A_s amplitude cluster within factor-2, even though
    pointwise f_conv drifts?

    WAVE 2 CARRY-FORWARD:
        G14 PASS: c_s FI ratio 1.227 (zeta+Zubarev+SDW)
        G15 FAIL: k_a2 NOT-R-protected span 14.69 (5-regulators, Lambda_Z=M_KK)
        G16 PASS: A_s with 3PI substitution, 4/5 PASS inheriting G15 span
                  (the A_s ledger under G16 is LINEAR in k_a2 so the cluster
                   ratio IS the k_a2 span in that case.)

    For this gate we compute 5-regulator f_conv directly via the framework's
    canonical formula (S77-B3 / S76 Scenario-B):
        f_conv = pi^4 / (9216 * M_0^2)
    where M_0 is the half-sum of multiplicity-weighted mode-count under the
    scheme's regulator kernel w_R(lam) evaluated on the D_K spectrum.

SUBSTITUTION CHAIN [VERIFY][AUDIT] (mandatory, math-scripts.md):

    Step 1 (Definition of f_conv and A_s).
        (i)  f_conv^R = pi^4 / (9216 * (M_0^R)^2)                    [frame def]
             M_0^R    = 0.5 * sum_j d_j * w_R(lam_j)                 [spectrum level]
        (ii) A_s     = prefactor * f_conv * (remaining ledger factors)
             with UNIFIED-AS-79 ledger:
                A_s = (H_tilde^2 / (8 pi^2)) * (1/eps_H) * F_amp * (1/c_sub) * f_conv
             (s80_unified_as_79_full.py L89-95; reproduced in G16 line 211).

    Step 2 (Substitute per regulator at pivot, L_max=5 spectrum).
        Weights (matching S83 W2-G14 and W2-G15 canonical conventions):
          w_zeta(lam)      = 1                              (flat count; zeta_D(0))
          w_Zubarev(lam)   = exp(-lam^2 / Lambda_Z^2)       (Gaussian mollifier)
              Conv A: Lambda_Z = M_KK = 1 (M_KK units)
              Conv B: Lambda_Z = lam_max (matched-scale)    [supplementary]
          w_SDW(lam)       = alpha*sqrt(x) + beta*exp(-x), x=lam^2/lam_max^2
                             with S72 (alpha, beta)=(0.912, 0.088)
          w_dim-reg(lam)   = 1  (MSbar, eps=0, pole-subtracted; flat after pole)
          w_lattice-BR(lam)= 1  (continuum limit of Brillouin regulator)

        Remaining A_s ledger factors FIXED (S80 W1-2 TD-framework baseline,
        headline branch; matches G16 PRIMARY):
          H_tilde_TD     = 5.9076e-03   (zeta-substrate, L_max=3)
          eps_H          = 0.02163      (S80 one-loop slow-roll)
          c_sub          = 2.238        (S78 zeta/Zubarev/SDW central)
          F_amp          = F_amp^{3PI} * k_a2_primary
                         = 1.0257840776 * 0.58297862385 = 0.5980
          (headline from G16, zeta-zeta under Conv A).

    Step 3 (Simplify; linearity identity).
        A_s_R = P * f_conv_R where P = prefactor*(1/eps_H)*F_amp*(1/c_sub) is
        R-INDEPENDENT (all other ledger factors fixed across regulators).
        Therefore:
          cluster_{A_s}(R) := max_R A_s_R / min_R A_s_R
                           = max_R (P * f_conv_R) / min_R (P * f_conv_R)
                           = max_R f_conv_R / min_R f_conv_R
                           = cluster_{f_conv}(R)
        The observable-level clustering ratio EQUALS the pointwise f_conv
        clustering ratio WHEN the ledger is linear in f_conv.

    Step 4 (Direction — pre-registered thresholds).
        PASS if cluster_{A_s} < 2
        INFO if cluster_{A_s} in [2, 3)
        FAIL if cluster_{A_s} >= 3

    Step 5 (Python verification — plan snippet, verbatim).
        conventions = ['zeta','Zubarev','SDW','dim-reg','lattice-BR']
        f_conv_vals = {c: compute_f_conv(c, 'pivot') for c in conventions}
        A_s_vals    = {c: compute_A_s_with_fconv(c, f_conv_vals[c]) for c in conventions}
        cluster     = max(A_s_vals.values()) / min(A_s_vals.values())

L_max:  5 (task-pinned, consistent with W2-G14/G15/G16 convention)
Cross-check at L_max in {3, 7, 9}.

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py
  - s74_spectrum_cache_L9_tau019.npz  (D_K spectrum at tau_fold)
  - this script

Output 4-tuple:
  (cluster_ratio=<v>, scheme=f_conv-observable-level,
   convention=5-regulator-atlas, L_max=5)
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401, F403
from canonical_constants import PI, M_KK, tau_fold

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
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration constants
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

SESSION = "S83"                                                    # (local)
GATE_ID = "S83-F-CONV-CLUSTER-TEST"                                # (local)
SCHEME = "f_conv-observable-level"                                 # (local)
CONVENTION = "5-regulator-atlas"                                   # (local)
L_MAX = 5                                                          # (local) task-pinned

OUT_NPZ = SCRIPT_DIR / "s83_w3_g28_f_conv_cluster_test.npz"
OUT_PNG = SCRIPT_DIR / "s83_w3_g28_f_conv_cluster_test.png"
VERDICT_TXT = SCRIPT_DIR / "s83_gate_verdicts.txt"
SPECTRUM_CACHE = SCRIPT_DIR / "s74_spectrum_cache_L9_tau019.npz"   # (local)

INPUT_FILES = [
    SCRIPT_DIR / "canonical_constants.py",
    SPECTRUM_CACHE,
    SCRIPT_DIR / "s83_w3_g28_f_conv_cluster_test.py",
]

# Pre-registered thresholds (plan line 1886)
PASS_CLUSTER_THRESHOLD = 2.0       # (local) observable-level factor-2 PASS
INFO_CLUSTER_THRESHOLD = 3.0       # (local) INFO upper / PASS boundary factor-3
EVAL_CUTOFF = 0.01                 # (local) IR cutoff matches W2-G14/G15

# SDW f_star parameters (S72; same literal as W2-G15)
ALPHA_STAR = 0.912                 # (local) f_star sqrt-weight
BETA_STAR  = 0.088                 # (local) f_star exp-weight

# Zubarev convention (headline = Conv A: Lambda_Z = M_KK = 1 in M_KK units)
LAMBDA_Z_A = 1.0                   # (local) Conv A: Lambda_Z = M_KK
# Conv B (supplementary): Lambda_Z = lam_max, computed per-L_max below

# A_s ledger fixed values (headline TD-framework zeta baseline; G16 primary)
H_TILDE_TD   = 5.90760e-03         # (local) S80 W1-1 TD-framework (zeta, L_max=3)
EPS_H        = 0.02163             # (local) S80 one-loop slow-roll
C_SUB        = 2.238               # (local) S78 W2-E central (zeta/Zub/SDW)
F_AMP_3PI    = 1.02578407761463    # (local) S83 G7 PASS F_amp^{3PI}(N_pivot) zeta
K_A2_PRIMARY = 0.58297862384968670 # (local) S83 G15 zeta slot, Conv A headline
F_AMP_HEAD   = F_AMP_3PI * K_A2_PRIMARY  # (local) composite F_amp (G16 PRIMARY)

# A_s canonical reference (S80 W1-2 PASS-F2 headline)
A_S_CANONICAL = 3.30e-9            # (local) S80 TD-framework zeta PASS-F2


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (per .claude/rules/gate-verdicts.md §4)
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
    """Assemble (|lam|, mult) arrays for modes at level <= L_max_cut."""
    abs_list = []  # (local)
    mult_list = []  # (local)
    for _key, data in sorted(sector_dict.items()):
        if data['level'] <= L_max_cut:
            dim = int(data['dim'])  # (local) SU(3) irrep dim
            for ev in data['abs_evals']:
                a = float(ev)  # (local)
                if a > cutoff:
                    abs_list.append(a)
                    mult_list.append(dim)
    return (np.array(abs_list, dtype=np.float64),
            np.array(mult_list, dtype=np.float64))


# ---------------------------------------------------------------------------
# Section 6 — Regulator kernels w_R(lam) (match W2-G14 / W2-G15 convention)
# ---------------------------------------------------------------------------

def w_zeta(lam):
    """zeta: flat weight = 1 (zeta_D(0) mode-counting)."""
    return np.ones_like(lam, dtype=np.float64)


def w_Zubarev(lam, Lambda_Z=LAMBDA_Z_A):
    """Zubarev Gaussian mollifier: exp(-lam^2 / Lambda_Z^2)."""
    return np.exp(-(lam / Lambda_Z) ** 2)


def w_SDW(lam, lam_max=None, alpha=ALPHA_STAR, beta=BETA_STAR):
    """SDW f_star: alpha*sqrt(x) + beta*exp(-x), x = lam^2 / lam_max^2."""
    if lam_max is None:
        lam_max = float(np.max(lam))
    x = (lam / lam_max) ** 2
    return alpha * np.sqrt(x) + beta * np.exp(-x)


def w_dimreg(lam):
    """dim-reg at eps=0 (MSbar pole-subtracted): flat weight = 1 after subtract."""
    return np.ones_like(lam, dtype=np.float64)


def w_latticeBR(lam):
    """lattice-BR (Brillouin) in continuum limit: flat weight = 1."""
    return np.ones_like(lam, dtype=np.float64)


# ---------------------------------------------------------------------------
# Section 7 — M_0 and f_conv computation per regulator
# ---------------------------------------------------------------------------

def M0_of(lam, mult, weight_fn, **kw):
    """M_0^R = 0.5 * sum_j d_j * w_R(lam_j), spectrum-level (s78_f_conv_anomaly M0 fn)."""
    w = weight_fn(lam, **kw) if kw else weight_fn(lam)   # (local)
    return float(0.5 * np.sum(mult * w))


def f_conv_of(M0):
    """f_conv = pi^4 / (9216 * M_0^2)  [framework canonical, S77-B3 / S76]."""
    if M0 <= 0.0 or not np.isfinite(M0):
        return float('nan')
    return float(PI ** 4 / (9216.0 * M0 ** 2))


def compute_f_conv_five_regulators(lam, mult, Lambda_Z=LAMBDA_Z_A):
    """Compute M_0 and f_conv for all 5 pre-registered regulators."""
    lam_max = float(lam.max())  # (local)

    M0 = {
        'zeta':       M0_of(lam, mult, w_zeta),
        'Zubarev':    M0_of(lam, mult, w_Zubarev, Lambda_Z=Lambda_Z),
        'SDW':        M0_of(lam, mult, w_SDW, lam_max=lam_max),
        'dim-reg':    M0_of(lam, mult, w_dimreg),
        'lattice-BR': M0_of(lam, mult, w_latticeBR),
    }
    f_conv = {k: f_conv_of(v) for k, v in M0.items()}
    return M0, f_conv


def A_s_with_fconv(f_conv_val):
    """A_s ledger: A_s = (H_tilde^2 / (8 pi^2)) * (1/eps_H) * F_amp * (1/c_sub) * f_conv."""
    prefactor = H_TILDE_TD ** 2 / (8.0 * PI ** 2)             # (local)
    return prefactor * (1.0 / EPS_H) * F_AMP_HEAD * (1.0 / C_SUB) * f_conv_val


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins + closure
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...")
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
    print(f"  sum(mult)   = {int(mult.sum())}")
    print(f"  tau_fold    = {tau_fold}")
    print()

    # 3. Compute f_conv for 5 regulators (headline: Zubarev Conv A, Lambda_Z=M_KK=1)
    M0_headline, f_conv_headline = compute_f_conv_five_regulators(
        lam, mult, Lambda_Z=LAMBDA_Z_A
    )
    print("HEADLINE (Convention A: Lambda_Z=M_KK=1 in M_KK units):")
    for R in ['zeta', 'Zubarev', 'SDW', 'dim-reg', 'lattice-BR']:
        print(f"  M_0[{R:>12s}] = {M0_headline[R]:.6e}")
    print()
    for R in ['zeta', 'Zubarev', 'SDW', 'dim-reg', 'lattice-BR']:
        print(f"  f_conv[{R:>12s}] = {f_conv_headline[R]:.6e}")
    print()

    # 4. Propagate to A_s (LINEAR in f_conv; observable-level)
    A_s_vals = {R: A_s_with_fconv(v) for R, v in f_conv_headline.items()}
    print("A_s per convention (TD-framework baseline F_amp_head="
          f"{F_AMP_HEAD:.4f}):")
    for R in ['zeta', 'Zubarev', 'SDW', 'dim-reg', 'lattice-BR']:
        print(f"  A_s[{R:>12s}] = {A_s_vals[R]:.6e}   "
              f"log10(/canon)={np.log10(A_s_vals[R]/A_S_CANONICAL):+.4f}")
    print()

    # 5. Cluster ratio (observable level)
    A_s_arr = np.array(list(A_s_vals.values()))        # (local)
    f_conv_arr = np.array(list(f_conv_headline.values()))  # (local)
    cluster_As = float(A_s_arr.max() / A_s_arr.min())  # (local) headline metric
    cluster_fconv = float(f_conv_arr.max() / f_conv_arr.min())  # (local) pointwise

    # Linearity identity check (Step 3 substitution chain)
    linearity_identity_ok = bool(
        abs(cluster_As - cluster_fconv) / cluster_fconv < 1e-10
    )
    print(f"cluster_{{A_s}}    = max(A_s)/min(A_s) = {cluster_As:.6f}")
    print(f"cluster_{{f_conv}} = max(f_conv)/min(f_conv) = {cluster_fconv:.6f}")
    print(f"LINEARITY IDENTITY (Step 3): cluster_{{A_s}} == cluster_{{f_conv}}")
    print(f"  verified: {linearity_identity_ok}")
    print()

    # 6. Substitution-chain direction step (Step 4)
    print(f"PRE-REGISTERED THRESHOLDS (plan L1886):")
    print(f"  PASS: cluster < {PASS_CLUSTER_THRESHOLD:.1f}")
    print(f"  INFO: cluster in [{PASS_CLUSTER_THRESHOLD:.1f}, "
          f"{INFO_CLUSTER_THRESHOLD:.1f})")
    print(f"  FAIL: cluster >= {INFO_CLUSTER_THRESHOLD:.1f}")
    print()

    if cluster_As < PASS_CLUSTER_THRESHOLD:
        verdict = "PASS"
    elif cluster_As < INFO_CLUSTER_THRESHOLD:
        verdict = "INFO"
    else:
        verdict = "FAIL"
    print(f"=> verdict: {verdict}")

    # 7. Plan-snippet verbatim (per prompt Step 5)
    print("\nPlan-snippet (verbatim):")
    conventions = ['zeta', 'Zubarev', 'SDW', 'dim-reg', 'lattice-BR']  # (local)
    f_conv_vals = {c: f_conv_headline[c] for c in conventions}          # (local)
    A_s_vals_snippet = {c: A_s_with_fconv(f_conv_vals[c])
                        for c in conventions}                           # (local)
    cluster_snippet = (max(A_s_vals_snippet.values())
                       / min(A_s_vals_snippet.values()))                # (local)
    print(f"  A_s observable clustering ratio = {cluster_snippet:.4f}")
    snippet_verdict = ('PASS' if cluster_snippet < 2
                       else 'INFO' if cluster_snippet < 3
                       else 'FAIL')                                     # (local)
    print(f"  Verdict: {snippet_verdict}")
    assert snippet_verdict == verdict, "snippet-verdict disagrees with main verdict"

    # 8. L_max robustness scan (diagnostic)
    L_max_scan = [3, 5, 7, 9]                                           # (local)
    cluster_by_L = {}                                                   # (local)
    for L_s in L_max_scan:
        lam_L, mult_L = collect_spectrum(sector_evals, L_s, EVAL_CUTOFF)
        _, fc_L = compute_f_conv_five_regulators(lam_L, mult_L,
                                                  Lambda_Z=LAMBDA_Z_A)
        v = np.array(list(fc_L.values()))                               # (local)
        cluster_by_L[L_s] = float(v.max() / v.min())
    print("\nL_max scan (cluster ratio at each L_max):")
    print(f"  {'L':>3s}  {'n_modes':>8s}  {'lam_max':>10s}  {'cluster':>12s}")
    for L_s in L_max_scan:
        lam_L, _ = collect_spectrum(sector_evals, L_s, EVAL_CUTOFF)
        print(f"  {L_s:>3d}  {len(lam_L):>8d}  {float(lam_L.max()):>10.4f}  "
              f"{cluster_by_L[L_s]:>12.4f}")

    # 9. Supplementary cross-check: Zubarev Convention B (Lambda_Z = lam_max)
    print("\nSupplementary: Zubarev Convention B (Lambda_Z = lam_max):")
    Lambda_Z_B = lam_max  # (local)
    _, f_conv_B = compute_f_conv_five_regulators(lam, mult, Lambda_Z=Lambda_Z_B)
    for R in ['zeta', 'Zubarev', 'SDW', 'dim-reg', 'lattice-BR']:
        print(f"  f_conv_B[{R:>12s}] = {f_conv_B[R]:.6e}")
    A_s_B = {R: A_s_with_fconv(v) for R, v in f_conv_B.items()}
    cluster_B = (max(A_s_B.values()) / min(A_s_B.values()))             # (local)
    print(f"  cluster_B = {cluster_B:.4f}  (supplementary; NOT verdict driver)")

    # 10. Cross-checks
    print("\nCross-checks:")
    # CC-1: all finite positive
    all_finite_ok = bool(np.all(np.isfinite(A_s_arr)) and np.all(A_s_arr > 0))
    # CC-2: zeta/dim-reg/lattice-BR give identical f_conv (flat weight)
    zeta_val = f_conv_headline['zeta']                                   # (local)
    dimreg_val = f_conv_headline['dim-reg']                              # (local)
    lattice_val = f_conv_headline['lattice-BR']                          # (local)
    flat_degenerate_ok = bool(
        abs(zeta_val - dimreg_val) / zeta_val < 1e-12 and
        abs(zeta_val - lattice_val) / zeta_val < 1e-12
    )
    # CC-3: cluster_As == cluster_fconv (Step 3 identity, re-verified)
    step3_identity_ok = linearity_identity_ok
    # CC-4: A_s prefactor chain gives specific value for zeta
    prefactor = H_TILDE_TD ** 2 / (8.0 * PI ** 2)                        # (local)
    A_s_zeta_by_hand = (prefactor * (1.0/EPS_H) * F_AMP_HEAD
                        * (1.0/C_SUB) * zeta_val)                        # (local)
    cc4_ok = bool(abs(A_s_zeta_by_hand - A_s_vals['zeta']) /
                  A_s_vals['zeta'] < 1e-12)
    # CC-5: Zubarev < zeta (Gaussian mollifier has smaller M_0 => LARGER f_conv)
    #   Substitution chain CC-5 [SIGN]:
    #     M_0^{zeta} = 0.5 * sum_j d_j * 1         (full count)
    #     M_0^{Zub}  = 0.5 * sum_j d_j * exp(-lam_j^2)  (suppressed)
    #     Since each term exp(-lam_j^2) <= 1, we have M_0^{Zub} <= M_0^{zeta}
    #     f_conv = pi^4 / (9216 * M_0^2) is MONOTONICALLY DECREASING in M_0.
    #     So f_conv^{Zub} >= f_conv^{zeta}. Direction: Zubarev HIGHER f_conv.
    zub_higher_than_zeta_ok = bool(
        f_conv_headline['Zubarev'] > f_conv_headline['zeta']
    )
    # CC-6: SDW f_conv relationship
    #   M_0^{SDW} = 0.5 * sum_j d_j * (alpha*sqrt(x_j) + beta*exp(-x_j))
    #   At x=1 (lam=lam_max) this is alpha + beta*exp(-1) ~ 0.944
    #   At x<1 the value is smaller than 1 but larger than exp(-lam^2/1^2) at large lam.
    sdw_between_ok = bool(
        f_conv_headline['SDW'] > f_conv_headline['zeta'] and
        f_conv_headline['SDW'] < f_conv_headline['Zubarev']
    )
    cc_all_ok = bool(
        all_finite_ok and flat_degenerate_ok and step3_identity_ok and
        cc4_ok and zub_higher_than_zeta_ok
    )
    print(f"  CC-1 all_finite_positive         : {all_finite_ok}")
    print(f"  CC-2 zeta=dim-reg=lattice-BR     : {flat_degenerate_ok}")
    print(f"  CC-3 Step-3 linearity identity   : {step3_identity_ok}")
    print(f"  CC-4 A_s prefactor chain         : {cc4_ok}")
    print(f"  CC-5 Zubarev f_conv > zeta       : {zub_higher_than_zeta_ok}")
    print(f"  CC-6 SDW between zeta and Zub    : {sdw_between_ok}  (diagnostic)")
    print(f"  ALL cross-checks (required)      : {cc_all_ok}")

    # 11. Save artifacts
    np.savez(
        OUT_NPZ,
        L_max=L_MAX,
        n_modes=len(lam),
        lam_max=lam_max,
        sum_mult=float(mult.sum()),
        # Headline (Conv A) — verdict driver
        M0_zeta=M0_headline['zeta'],
        M0_Zubarev=M0_headline['Zubarev'],
        M0_SDW=M0_headline['SDW'],
        M0_dimreg=M0_headline['dim-reg'],
        M0_latticeBR=M0_headline['lattice-BR'],
        f_conv_zeta=f_conv_headline['zeta'],
        f_conv_Zubarev=f_conv_headline['Zubarev'],
        f_conv_SDW=f_conv_headline['SDW'],
        f_conv_dimreg=f_conv_headline['dim-reg'],
        f_conv_latticeBR=f_conv_headline['lattice-BR'],
        A_s_zeta=A_s_vals['zeta'],
        A_s_Zubarev=A_s_vals['Zubarev'],
        A_s_SDW=A_s_vals['SDW'],
        A_s_dimreg=A_s_vals['dim-reg'],
        A_s_latticeBR=A_s_vals['lattice-BR'],
        cluster_As=cluster_As,
        cluster_fconv=cluster_fconv,
        # Supplementary (Conv B)
        f_conv_B_zeta=f_conv_B['zeta'],
        f_conv_B_Zubarev=f_conv_B['Zubarev'],
        f_conv_B_SDW=f_conv_B['SDW'],
        f_conv_B_dimreg=f_conv_B['dim-reg'],
        f_conv_B_latticeBR=f_conv_B['lattice-BR'],
        cluster_B=cluster_B,
        # L_max scan
        L_max_scan=np.array(L_max_scan),
        cluster_scan=np.array([cluster_by_L[L_s] for L_s in L_max_scan]),
        # Fixed ledger inputs
        H_TILDE_TD=H_TILDE_TD,
        EPS_H=EPS_H,
        C_SUB=C_SUB,
        F_AMP_HEAD=F_AMP_HEAD,
        F_AMP_3PI=F_AMP_3PI,
        K_A2_PRIMARY=K_A2_PRIMARY,
        A_S_CANONICAL=A_S_CANONICAL,
        # Thresholds
        PASS_CLUSTER_THRESHOLD=PASS_CLUSTER_THRESHOLD,
        INFO_CLUSTER_THRESHOLD=INFO_CLUSTER_THRESHOLD,
        EVAL_CUTOFF=EVAL_CUTOFF,
        # Cross-checks
        cc_all_ok=cc_all_ok,
        linearity_identity_ok=linearity_identity_ok,
        flat_degenerate_ok=flat_degenerate_ok,
        zub_higher_than_zeta_ok=zub_higher_than_zeta_ok,
        sdw_between_ok=sdw_between_ok,
        # Closure
        verdict=verdict,
        closure=closure,
    )
    print(f"\nArtifacts: {OUT_NPZ.name}")

    # 12. Plot — 2 panels: f_conv per R + A_s per R with PASS/INFO/FAIL bands
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    ax0, ax1 = axes

    R_names = ['zeta', 'Zubarev', 'SDW', 'dim-reg', 'lattice-BR']
    colors = ['#2c7fb8', '#d95f0e', '#31a354', '#c26dbc', '#7a7a7a']

    # Panel (a): f_conv per regulator (log scale)
    f_vals = [f_conv_headline[R] for R in R_names]
    bars0 = ax0.bar(R_names, f_vals, color=colors, alpha=0.85, edgecolor='k',
                    linewidth=0.5)
    for b, v in zip(bars0, f_vals):
        ax0.text(b.get_x() + b.get_width() / 2., v * 1.15,
                 f'{v:.2e}', ha='center', va='bottom', fontsize=8, rotation=45)
    ax0.set_yscale('log')
    ax0.set_ylabel(r'$f_{\rm conv}$ (log scale)')
    ax0.set_title(f'$f_{{\\rm conv}}$ across 5 regulators '
                  f'(pointwise span = {cluster_fconv:.2f})')
    ax0.grid(True, alpha=0.3, which='both', axis='y')

    # Panel (b): A_s per regulator (log scale) with PASS/INFO bands
    A_vals = [A_s_vals[R] for R in R_names]
    # Color-code by verdict per regulator: compare against canonical A_s = 3.30e-9
    A_s_PASS_LO = A_S_CANONICAL / PASS_CLUSTER_THRESHOLD
    A_s_PASS_HI = A_S_CANONICAL * PASS_CLUSTER_THRESHOLD
    A_s_INFO_LO = A_S_CANONICAL / INFO_CLUSTER_THRESHOLD
    A_s_INFO_HI = A_S_CANONICAL * INFO_CLUSTER_THRESHOLD

    bars1 = ax1.bar(R_names, A_vals, color=colors, alpha=0.85, edgecolor='k',
                    linewidth=0.5)
    ax1.axhline(A_S_CANONICAL, color='k', linestyle='--', linewidth=1.0,
                label=f'$A_s$ canon = {A_S_CANONICAL:.2e}')
    ax1.axhspan(A_s_PASS_LO, A_s_PASS_HI, color='g', alpha=0.12,
                label='PASS (factor-2)')
    ax1.axhspan(A_s_INFO_LO, A_s_INFO_HI, color='y', alpha=0.08,
                label='INFO (factor-3)')
    for b, v in zip(bars1, A_vals):
        ax1.text(b.get_x() + b.get_width() / 2., v * 1.15,
                 f'{v:.2e}', ha='center', va='bottom', fontsize=8, rotation=45)
    ax1.set_yscale('log')
    ax1.set_ylabel(r'$A_s$ (log scale)')
    ax1.set_title(f'G28 observable-level: cluster = {cluster_As:.2f} -> {verdict}')
    ax1.legend(loc='lower right', fontsize=8)
    ax1.grid(True, alpha=0.3, which='both', axis='y')

    fig.suptitle(f'S83 W3-G28 F-CONV-CLUSTER-TEST — {verdict} '
                 f'(obs-level cluster = {cluster_As:.2f})', fontsize=12)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110, bbox_inches='tight')
    plt.close(fig)
    print(f"Plot:      {OUT_PNG.name}")

    # 13. 4-tuple tag + verdict line
    tag = (f"(cluster_ratio={cluster_As:.6f}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n4-tuple: {tag}")

    verdict_line = (
        f"{GATE_ID}: {verdict} -- value={cluster_As:.6f} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"sha256={closure}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_line)
    print(f"Verdict line appended to: {VERDICT_TXT.name}")
    print(f"  {verdict_line.strip()}")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0 if verdict == "PASS" else (1 if verdict == "FAIL" else 3)


if __name__ == "__main__":
    sys.exit(main())
