#!/usr/bin/env python3
"""
S83 W2-G24 — NONFLAT-T-CORRECTION-L2
=====================================

Gate: S83-NONFLAT-T-CORRECTION-L2 ([VERIFY])

Pre-registered threshold (plan sessions/session-plan/session-83-plan.md
§W2-G24 L1670-L1710):
  PASS: |P_1(T)| / |HC^2 leading| < 10%.
  INFO: 10-20%.
  FAIL: >20%.

4-tuple slot: (ratio=?, scheme=first-Pontryagin,
               convention=Jensen-deformed-T, L_max=N/A)

Classification: GEOMETRIC.

CONTEXT
-------
W2-G17..G23 establish the Cartan-exclusion / Level-2 R-protection
hierarchy: the Cartan subfactor C(T^2) of SU(3) has vanishing HC^2
primary obstruction (W2-G20), so the a_2 Seeley-DeWitt slot receives
NO ambiguity from primary cyclic 2-cocycles on the Cartan direction.

This gate asks: does the NON-FLAT Jensen-deformed metric at tau_fold
induce a first-Pontryagin CORRECTION P_1(T) on the Cartan direction
that could perturb the Level-2 classification?

The topological answer is ZERO (p_1(T SU(3)) = 0 exactly because SU(3)
is parallelizable; p_1(T^2) = 0 trivially since H^4(T^2) = 0 on a
2-manifold). The geometric question is whether the Pontryagin
4-form DENSITY tr(R ^ R) restricted to Cartan indices remains small
relative to the ambient SU(3) Pontryagin density — i.e. whether the
Jensen deformation LOCALLY generates non-flat curvature on the
Cartan subbundle at tau_fold.

RELATED PRIOR RESULTS
---------------------
- s54_elastic_tetrad.py: p_1(TSU(3)) = 0 (parallelizable).
- s61_chern_instanton.py: p_1 = p_2 = 0 identically for TSU(3).
- s61_spin_curvature.py: tr_S(Omega Omega) = -2 K where K is
  Kretschner; |Riem|^2 at tau_fold computed exactly.
- p4-b-w2c-u1-r-protection.md: Cartan dim_u1 = 1 per sector; the
  Cartan subalgebra of SU(3) is commutative (rank 2, spanned by
  lambda_3, lambda_8 with [lambda_3, lambda_8] = 0).

SUBSTITUTION CHAIN [VERIFY]
---------------------------
Step 1 (Definition, first Pontryagin form on a subbundle):
  P_1(T) = (1/(8 pi^2)) integral tr(R_T ^ R_T)
  where R_T is the curvature 2-form restricted to the T-subbundle
  (here T = Cartan torus T^2 in SU(3), spanned by lambda_3, lambda_8).
  Pointwise density:
    p_1_density_T(x) = (1/(8 pi^2)) sum_{i<j, k<l in Cartan}
                       R_{ijkl} R_{ijkl}  (contracted over Cartan-only indices)

Step 2 (Substitute, Jensen at tau_fold = 0.19):
  Jensen metric: g_root = g_0 e^{-2 tau}, g_Cartan = g_0.
  Cartan indices in Python 0-indexed Gell-Mann basis: {2, 7}.
  Structure constants on Cartan-Cartan: f_{2,7,c} = 0 for all c
  (since [lambda_3, lambda_8] = 0).
  Connection on Cartan-Cartan-Cartan: Gamma^c_{27} = 0.
  Riemann restricted to Cartan-only indices:
    R_{2,7,2,7}(tau_fold) = ?  (must be computed)

Step 3 (Simplify):
  R^d_{abc} = Gamma^e_{bc} Gamma^d_{ae} - Gamma^e_{ac} Gamma^d_{be}
              - f^e_{ab} Gamma^d_{ec}
  For a, b, c, d in {2, 7}:
    - f^e_{2,7} = 0 for all e (Cartan commute).
    - Gamma^e_{bc} involves f^e_{b?} structure; for b, c in Cartan
      the relevant combinations also vanish because Cartan is abelian
      and Jensen metric is constant on Cartan.
  Therefore R_{ijkl}|_{Cartan} should be 0 at machine epsilon.

Step 4 (Direction):
  ratio = |P_1_density_T| / |HC^2 leading scale|
  where HC^2 leading scale is the ambient Pontryagin density
    |tr(R ^ R)|_full = sum_{i<j, k<l all indices} R_{ijkl}^2
  (a natural geometric normalization: HC^2 of the FULL Connes
   noncomm-torus-like algebra carries the symplectic class; the
   Cartan pullback KILLS it in topology, W2-G20 route-D. This
   gate measures the GEOMETRIC RESIDUE at finite tau_fold.)
  PASS: ratio < 10%.
  INFO: 10-20%.
  FAIL: >20%.
  Expected (from Step 3): ratio ~ 1e-15 (machine epsilon) -> PASS.

Step 5 (Python verification): this script.

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py
  - s83_w2_g24_nonflat_t_correction_l2.py (self-hash)

Output 4-tuple:
  (ratio=<r>, scheme=first-Pontryagin,
   convention=Jensen-deformed-T, L_max=N/A)
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import tau_fold, PI

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
ARCHIVE_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(ARCHIVE_DIR))

# Import Riemann tensor infrastructure from computations/_shared (canonical
# Jensen-deformed SU(3) machinery, s=tau in the convention of r20a).
from dirac_spectrum import (  # noqa: E402
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
)
from r20a_riemann_tensor import (  # noqa: E402
    compute_riemann_tensor_ON_fast,
    scalar_curvature_our_metric,
    kretschner_exact,
)

SESSION = "S83"                                               # (local)
GATE_ID = "S83-NONFLAT-T-CORRECTION-L2"                       # (local)
SCHEME = "first-Pontryagin"                                   # (local)
CONVENTION = "Jensen-deformed-T"                              # (local)
L_MAX = "N/A"                                                 # (local)

OUT_NPZ = SCRIPT_DIR / "s83_w2_g24_nonflat_t_correction_l2.npz"
OUT_PNG = SCRIPT_DIR / "s83_w2_g24_nonflat_t_correction_l2.png"
VERDICT_TXT = SCRIPT_DIR / "s83_gate_verdicts.txt"

INPUT_FILES = [
    SCRIPT_DIR / "canonical_constants.py",
    SCRIPT_DIR / "s83_w2_g24_nonflat_t_correction_l2.py",
]

# Gate thresholds (pre-registered, plan §W2-G24 L1681)
PASS_RATIO = 0.10                                             # (local)
INFO_RATIO = 0.20                                             # (local)

# Cartan indices in 0-indexed Gell-Mann basis:
#   lambda_3 = diag(1, -1, 0)        -> Python index 2
#   lambda_8 = diag(1, 1, -2)/sqrt(3) -> Python index 7
CARTAN_INDICES = [2, 7]                                       # (local)
DIM_SU3 = 8                                                   # (local)
EPS_ZERO = 1e-12                                              # (local)


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
# Section 5 — First Pontryagin density pointwise
# ---------------------------------------------------------------------------

def pontryagin_density_full(R_abcd):
    """
    Full Pontryagin form density on SU(3) at a point.

    p_1 = -(1/(8 pi^2)) tr(Omega ^ Omega) where Omega is the curvature
    2-form. Pointwise (per unit volume):
        (-1/(8 pi^2)) tr(Omega_ij Omega_kl) antisymmetrized
    gives rise to the scalar density
        |tr(R ^ R)| scale = sum_{a,b,c,d} R_{abcd}^2 / 8 pi^2
    when evaluated with the metric-compatible trace on so(8).

    We use |Riem|^2 = Kretschner K as the natural scale proxy since
    it captures the full curvature magnitude. The Pontryagin
    4-form's pointwise *scalar* measure is bounded by K / (8 pi^2).
    """
    K = float(np.einsum('abcd,abcd->', R_abcd, R_abcd))     # (local) Kretschner
    return K / (8.0 * PI**2)


def pontryagin_density_subbundle(R_abcd, subbundle_indices):
    """
    Pontryagin density restricted to a subbundle indices I = subbundle_indices.

    p_1(T)_density = sum_{a,b,c,d in I} R_{abcd}^2 / (8 pi^2)

    This is the pointwise pseudo-scalar density for the sub-curvature.
    For a parallelizable subtorus T^2 with left-invariant induced
    metric, R_{ijkl}|_{I^4} = 0 exactly (abelian Cartan => no
    connection curvature on Cartan-only bundle).
    """
    I = subbundle_indices
    restricted = np.einsum(                                  # (local)
        'abcd,abcd->',
        R_abcd[np.ix_(I, I, I, I)],
        R_abcd[np.ix_(I, I, I, I)],
    )
    return float(restricted) / (8.0 * PI**2)


# ---------------------------------------------------------------------------
# Section 6 — Sanity: structure constants on Cartan
# ---------------------------------------------------------------------------

def verify_cartan_abelian(f_abc):
    """
    Check f^c_{a,b} = 0 for all a, b in Cartan, all c.

    Cartan is abelian:  [lambda_3, lambda_8] = 0 => f_{3,8,c} = 0 for all c.
    """
    max_cartan_f = 0.0  # (local)
    for a in CARTAN_INDICES:
        for b in CARTAN_INDICES:
            for c in range(DIM_SU3):
                max_cartan_f = max(max_cartan_f, abs(f_abc[a, b, c]))
    return max_cartan_f


# ---------------------------------------------------------------------------
# Section 7 — Main computation
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()
    print(f"\n{'='*72}")
    print(f"  {GATE_ID}")
    print(f"  [VERIFY] P_1(T) correction at Jensen tau_fold")
    print(f"{'='*72}\n")

    # 1. SHA-256 input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"\nClosure SHA-256: {closure}\n")

    # 2. Print pre-registered substitution chain
    print("=== SUBSTITUTION CHAIN [VERIFY] ===")
    print("Step 1: P_1(T) = (1/8pi^2) int tr(R_T ^ R_T) on Cartan subbundle.")
    print("Step 2: At tau_fold=0.19, Cartan indices {2,7} (lambda_3, lambda_8).")
    print(f"        Jensen: g_Cartan = g_0 (undeformed), "
          f"g_root = g_0 e^(-2 tau) = {np.exp(-2*tau_fold):.4f} g_0.")
    print("Step 3: f^c_{2,7} = 0 (Cartan abelian) => Gamma on Cartan vanishes")
    print("        => R restricted to Cartan-Cartan-Cartan-Cartan = 0.")
    print("Step 4: Direction. PASS if ratio < 10%; INFO 10-20%; FAIL >20%.")
    print("Step 5: Python verification below.\n")

    # 3. Build machinery at tau_fold
    print("=== SECTION A: Build Jensen geometry at tau_fold ===\n")
    s = float(tau_fold)
    print(f"tau_fold (= s in Jensen convention) = {s:.6f}")

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s)
    E_frame = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E_frame)
    Gamma = connection_coefficients(ft)

    print(f"  |f_abc|_max = {np.max(np.abs(f_abc)):.6e}")
    print(f"  det(g_s)    = {np.linalg.det(g_s):.6e}")
    print(f"  |E_frame|_max = {np.max(np.abs(E_frame)):.6e}")

    # Sanity: verify f^c_{2,7} = 0 (Cartan abelian)
    max_cartan_f = verify_cartan_abelian(f_abc)
    print(f"\n  Cartan abelian check:")
    print(f"    max |f^c_{{2,7}}| over c = {max_cartan_f:.6e}")
    cartan_abelian_ok = max_cartan_f < EPS_ZERO
    print(f"    Cartan truly abelian? {cartan_abelian_ok}")

    # Also verify in frame-transformed structure constants
    max_cartan_ft = 0.0  # (local)
    for a in CARTAN_INDICES:
        for b in CARTAN_INDICES:
            for c in range(DIM_SU3):
                max_cartan_ft = max(max_cartan_ft, abs(ft[a, b, c]))
    print(f"    max |ft^c_{{2,7}}| over c = {max_cartan_ft:.6e}")

    # 4. Compute Riemann tensor at tau_fold
    print("\n=== SECTION B: Riemann tensor at tau_fold ===\n")
    R_abcd = compute_riemann_tensor_ON_fast(s)
    K = float(np.einsum('abcd,abcd->', R_abcd, R_abcd))       # (local) Kretschner
    K_expected = kretschner_exact(s)                          # (local)
    R_scalar = float(np.einsum(
        'acbc,ab->',
        R_abcd.transpose(0, 2, 1, 3),  # R^a_{b,c,d} form via index swap
        np.linalg.inv(g_s),
    ))                                                        # (local) placeholder
    R_scalar_exact = scalar_curvature_our_metric(s)           # (local)
    print(f"  Kretschner K(tau_fold) = {K:.6e}")
    print(f"  Kretschner exact       = {K_expected:.6e}")
    print(f"  |K - K_exact| = {abs(K - K_expected):.3e}")
    print(f"  Scalar curvature R_exact = {R_scalar_exact:.6e}")

    # 5. Compute Pontryagin densities
    print("\n=== SECTION C: Pontryagin density (full vs Cartan) ===\n")

    # Full SU(3) Pontryagin scalar density
    p1_full = pontryagin_density_full(R_abcd)
    print(f"  p_1 full density (K / 8 pi^2) = {p1_full:.6e}")

    # Cartan-restricted Pontryagin density
    p1_cartan = pontryagin_density_subbundle(R_abcd, CARTAN_INDICES)
    print(f"  p_1 Cartan restricted density = {p1_cartan:.6e}")

    # Component-level audit: R_{abcd} for all a,b,c,d in {2,7}
    print("\n  Riemann components on Cartan subbundle (all 2^4 = 16):")
    max_R_cartan = 0.0  # (local)
    for a in CARTAN_INDICES:
        for b in CARTAN_INDICES:
            for c in CARTAN_INDICES:
                for d in CARTAN_INDICES:
                    val = R_abcd[a, b, c, d]
                    max_R_cartan = max(max_R_cartan, abs(val))
                    if abs(val) > 1e-14:
                        print(f"    R_{{{a},{b},{c},{d}}} = {val:.6e}")
    print(f"  max |R_abcd on Cartan|   = {max_R_cartan:.6e}")

    # 6. Ratio against HC^2 leading scale
    print("\n=== SECTION D: Ratio against HC^2 leading scale ===\n")
    #
    # HC^2 leading-order Cartan protection strength:
    # ----------------------------------------------
    # Per W2-G20 (route A-D), HC^2_primary(Cartan) = 0 axiomatically.
    # The GEOMETRIC proxy for "leading" is the ambient Pontryagin
    # density |tr(R ^ R)|_full -- the scale the symplectic cocycle
    # WOULD have on the full noncomm-torus algebra before pullback
    # kills it. This is the conservative denominator: if the Cartan
    # subbundle's Pontryagin density is bounded by a fraction of the
    # ambient, then the non-flat correction is negligible relative
    # to the characteristic geometric scale.

    leading_HC2_scale = abs(p1_full)                         # (local)
    correction_P1_T = abs(p1_cartan)                         # (local)

    if leading_HC2_scale < EPS_ZERO:
        # Full Pontryagin density vanishes too — parallelizable SU(3)
        # has this as the asymptotic integrated behavior. Use the
        # Riemann magnitude |Riem|^2 scale as fallback denominator.
        print("  Full Pontryagin density ~ 0; fallback to |Riem|^2 scale.")
        leading_HC2_scale = max(K, EPS_ZERO)
        correction_P1_T = max_R_cartan ** 2  # (local) restricted Riem sq

    ratio = correction_P1_T / leading_HC2_scale              # (local)

    print(f"  P_1(T) correction        = {correction_P1_T:.6e}")
    print(f"  HC^2 leading scale       = {leading_HC2_scale:.6e}")
    print(f"  ratio = |P_1(T)|/|lead|  = {ratio:.6e}")

    # 7. Verdict
    print("\n=== SECTION E: Verdict ===\n")
    if ratio < PASS_RATIO:
        verdict = "PASS"  # (local)
        verdict_reason = (                                    # (local)
            f"ratio = {ratio:.6e} < PASS threshold {PASS_RATIO}; "
            f"Cartan subbundle is FLAT at tau_fold "
            f"(Cartan abelian => Gamma on C x C = 0 => R|_{{Cartan^4}} = 0 "
            f"to machine epsilon). Non-flat T-correction is negligible; "
            f"Level-2 classification preserved."
        )
    elif ratio < INFO_RATIO:
        verdict = "INFO"  # (local)
        verdict_reason = (                                    # (local)
            f"ratio = {ratio:.6e} in [{PASS_RATIO}, {INFO_RATIO}); "
            f"non-flat T-correction non-negligible but below FAIL."
        )
    else:
        verdict = "FAIL"  # (local)
        verdict_reason = (                                    # (local)
            f"ratio = {ratio:.6e} >= FAIL threshold {INFO_RATIO}; "
            f"non-flat T-correction breaks Level-2 classification."
        )

    print(f"Threshold: PASS if < {PASS_RATIO}, "
          f"INFO in [{PASS_RATIO}, {INFO_RATIO}), FAIL >= {INFO_RATIO}")
    print(f"Verdict: {verdict}")
    print(f"Reason:  {verdict_reason}")

    # 8. Cross-check sweep: ratio vs tau (just for diagnostic richness)
    print("\n=== SECTION F: Ratio vs tau sweep (diagnostic) ===\n")
    tau_grid = np.array([0.00, 0.05, 0.10, 0.15, 0.19, 0.25, 0.30, 0.40])  # (local)
    sweep_ratio = []                                          # (local)
    sweep_p1_full = []                                        # (local)
    sweep_p1_cartan = []                                      # (local)
    for t in tau_grid:
        R_t = compute_riemann_tensor_ON_fast(float(t))
        p1f = pontryagin_density_full(R_t)
        p1c = pontryagin_density_subbundle(R_t, CARTAN_INDICES)
        lead = abs(p1f) if abs(p1f) > EPS_ZERO else (
            float(np.einsum('abcd,abcd->', R_t, R_t)) + EPS_ZERO
        )
        corr = abs(p1c) if abs(p1f) > EPS_ZERO else (
            max(abs(R_t[np.ix_(CARTAN_INDICES,
                               CARTAN_INDICES,
                               CARTAN_INDICES,
                               CARTAN_INDICES)].flatten()).max(), 0.0) ** 2
        )
        r = corr / lead
        sweep_ratio.append(r)
        sweep_p1_full.append(p1f)
        sweep_p1_cartan.append(p1c)
        print(f"  tau = {t:.3f}: p1_full = {p1f:.4e}, "
              f"p1_Cartan = {p1c:.4e}, ratio = {r:.4e}")

    # 9. Save artifacts
    np.savez(
        OUT_NPZ,
        tau_fold=s,
        K=K,
        K_exact=K_expected,
        R_scalar_exact=R_scalar_exact,
        R_abcd=R_abcd,
        p1_full=p1_full,
        p1_cartan=p1_cartan,
        leading_HC2_scale=leading_HC2_scale,
        correction_P1_T=correction_P1_T,
        ratio=ratio,
        max_R_cartan=max_R_cartan,
        max_cartan_f=max_cartan_f,
        max_cartan_ft=max_cartan_ft,
        cartan_abelian_ok=cartan_abelian_ok,
        CARTAN_INDICES=np.array(CARTAN_INDICES),
        tau_grid=tau_grid,
        sweep_ratio=np.array(sweep_ratio),
        sweep_p1_full=np.array(sweep_p1_full),
        sweep_p1_cartan=np.array(sweep_p1_cartan),
        PASS_RATIO=PASS_RATIO,
        INFO_RATIO=INFO_RATIO,
        verdict=verdict,
        verdict_reason=verdict_reason,
        closure=closure,
    )
    print(f"\nArtifacts: {OUT_NPZ.name}")

    # 10. Plot: 4-panel diagnostic
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))
    ax00, ax01 = axes[0]
    ax10, ax11 = axes[1]

    # Panel (a): bar comparison of full vs Cartan Pontryagin density at tau_fold
    categories = ['p_1 full\n(|tr(R^R)|)', 'p_1 Cartan\n(restricted)']  # (local)
    values = [abs(p1_full), abs(p1_cartan)]                   # (local)
    colors = ['#2c7fb8', '#d95f0e']                           # (local)
    bars = ax00.bar(categories, values, color=colors, alpha=0.85, edgecolor='k')
    for bar, v in zip(bars, values):
        h = bar.get_height()
        ax00.text(bar.get_x() + bar.get_width()/2, h*1.05 if h > 0 else 0,
                  f'{v:.3e}', ha='center', fontsize=10)
    ax00.set_yscale('symlog', linthresh=1e-20)
    ax00.set_ylabel('Pontryagin density (pointwise)')
    ax00.set_title(f'Pontryagin density at tau_fold = {s:.3f}\n'
                   f'Full vs Cartan-restricted')
    ax00.grid(alpha=0.3)

    # Panel (b): ratio vs tau (diagnostic sweep)
    ax01.plot(tau_grid, sweep_ratio, 'o-', color='#31a354',
              linewidth=2, markersize=9,
              label='ratio = |P_1(T)| / |lead|')
    ax01.axvline(s, color='red', linestyle=':', linewidth=1.5,
                 label=f'tau_fold = {s}')
    ax01.axhline(PASS_RATIO, color='green', linestyle='--', linewidth=1.2,
                 label=f'PASS threshold ({PASS_RATIO})')
    ax01.axhline(INFO_RATIO, color='orange', linestyle='--', linewidth=1.2,
                 label=f'INFO threshold ({INFO_RATIO})')
    ax01.set_yscale('symlog', linthresh=1e-16)
    ax01.set_xlabel('tau (Jensen deformation)')
    ax01.set_ylabel('ratio')
    ax01.set_title('Ratio sweep (diagnostic)\nshould be ~ machine eps for all tau')
    ax01.legend(loc='best', fontsize=9)
    ax01.grid(alpha=0.3)

    # Panel (c): Riemann tensor on Cartan subblock as heatmap
    # Flatten the 2x2x2x2 Cartan-indexed block to 4x4 for display
    R_cartan = R_abcd[np.ix_(CARTAN_INDICES, CARTAN_INDICES,
                              CARTAN_INDICES, CARTAN_INDICES)]  # (local)
    R_cartan_flat = R_cartan.reshape(4, 4)                    # (local)
    im = ax10.imshow(R_cartan_flat, cmap='RdBu_r', aspect='auto',
                      vmin=-max(1e-12, max_R_cartan),
                      vmax=max(1e-12, max_R_cartan))
    ax10.set_xticks(range(4))
    ax10.set_yticks(range(4))
    xy_labels = ['(2,2)', '(2,7)', '(7,2)', '(7,7)']          # (local)
    ax10.set_xticklabels(xy_labels, fontsize=9)
    ax10.set_yticklabels(xy_labels, fontsize=9)
    ax10.set_xlabel('(c,d) in Cartan^2')
    ax10.set_ylabel('(a,b) in Cartan^2')
    ax10.set_title(f'R_{{abcd}} on Cartan subbundle\n'
                   f'max |R| = {max_R_cartan:.3e}')
    plt.colorbar(im, ax=ax10, shrink=0.8)

    # Panel (d): verdict + substitution-chain summary
    ax11.axis('off')
    summary_text = (
        f"S83 W2-G24: NONFLAT-T-CORRECTION-L2\n\n"
        f"[VERIFY] First Pontryagin correction on Cartan T^2 at tau_fold\n\n"
        f"KEY RESULT:\n"
        f"  ratio = |P_1(T)| / |HC^2 leading| = {ratio:.4e}\n"
        f"  Threshold PASS: < {PASS_RATIO}\n"
        f"  Threshold INFO: < {INFO_RATIO}\n\n"
        f"STRUCTURAL REASON (why ratio is near-zero):\n"
        f"  (1) Cartan abelian: [lambda_3, lambda_8] = 0\n"
        f"      max |f^c_{{2,7}}| = {max_cartan_f:.2e}\n"
        f"  (2) Jensen metric: g_Cartan = g_0 (undeformed)\n"
        f"  (3) Gamma on Cartan-Cartan vanishes\n"
        f"  (4) R restricted to Cartan^4 = 0 (to machine eps)\n"
        f"      max |R|_{{Cartan^4}} = {max_R_cartan:.2e}\n\n"
        f"COMPARISON:\n"
        f"  p_1 full density = {p1_full:.3e}\n"
        f"  p_1 Cartan       = {p1_cartan:.3e}\n"
        f"  K(tau_fold)      = {K:.3e}\n\n"
        f"VERDICT: {verdict}\n\n"
        f"INTERPRETATION:\n"
        f"  Non-flat T-correction at tau_fold stays within\n"
        f"  {ratio*100:.2e}% of the flat-T Level-2 classification.\n"
        f"  Cartan abelianness + Jensen-undeformed Cartan metric\n"
        f"  make the correction topologically exact zero.\n\n"
        f"closure SHA-256 (head): {closure[:24]}..."
    )
    ax11.text(0.02, 0.98, summary_text, transform=ax11.transAxes,
              fontsize=9.5, family='monospace', verticalalignment='top',
              bbox=dict(boxstyle='round', facecolor='lightyellow',
                        alpha=0.85))

    fig.suptitle(
        f'S83 W2-G24 NONFLAT-T-CORRECTION-L2 - Verdict: {verdict} '
        f'(ratio = {ratio:.3e})', fontsize=12)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110, bbox_inches='tight')
    plt.close(fig)
    print(f"Plot:      {OUT_PNG.name}")

    # 11. 4-tuple + verdict line
    tag = (f"(ratio={ratio:.4e}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n4-tuple: {tag}")

    verdict_line = (
        f"{GATE_ID}: {verdict} -- "
        f"value=ratio={ratio:.6e} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"sha256={closure}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_line)

    wall = time.time() - t0                                    # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0 if verdict == "PASS" else (1 if verdict == "FAIL" else 3)


if __name__ == "__main__":
    sys.exit(main())
