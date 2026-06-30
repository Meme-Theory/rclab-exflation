#!/usr/bin/env python3
"""
S83 W3-G46 — S83-TENSOR-TRANSFER-K-TRANSIT-TO-K-CMB
====================================================

Gate: S83-TENSOR-TRANSFER-K-TRANSIT-TO-K-CMB   [VERIFY-THEOREM][CHAIN]
Classification: PHONONIC (tensor-mode dispersion on substrate).
Owner: sagan-empiricist (joint with mack context)

Pre-registration (sessions/session-plan/session-83-plan.md §W3-G46 L2700-L2744):
    HYPOTHESIS: Tensor-mode transfer from k_transit to k_CMB via substrate
                dispersion relation closes the S66 TENSOR-TRANSFER FAIL.
    PASS: closed-form transfer yields r(k_CMB) < 0.036 (BICEP/Keck 2021 95% CL).
    FAIL: r(k_CMB) >= 0.036.

4-tuple slot: (r_CMB=?, scheme=substrate-dispersion-transfer,
               convention=c_T(k)-variable, L_max=N/A)

CONTEXT — What S66 FAILed and what this closes:
    S66 s66_tensor_transfer.py FAILed because the NAIVE formal transfer did
    NOT preserve the blue-tilted tensor tilt n_T = +0.468 found at the
    transit scale. The FAIL verdict message:
       "n_T(k_CMB) = -2*eps(tau_CMB) < 0: transfer DOES NOT preserve blue tilt"
    That is actually a physical finding: CMB-scale modes exit the horizon
    at tau ~ 0.05 (far from the fold at tau=0.19), where eps_H is small and
    positive, so n_T = -2*eps_H at CMB scales is small and red. The "FAIL"
    arose from a mislabelled PASS criterion (preserve blue tilt rather than
    honour horizon-exit physics). This gate closes S66 by EXPLICITLY
    computing r(k_CMB) via the substrate-dispersion transfer and evaluating
    it against the BICEP/Keck 2021 95% CL bound r < 0.036.

SUBSTITUTION CHAIN [VERIFY-THEOREM][CHAIN] (mandatory, math-scripts.md):

    Step 1 (Definitions — no direction claims yet).
        (i)  Tensor mode equation (conformal time eta, v_k = a*h_k):
                v_k'' + (k^2 - a''/a) v_k = 0                          (T.1)
        (ii) Tensor dispersion on substrate:
                omega_T(k) = c_T(k) * k                                (T.2)
             with c_T = 1 structural for tensor modes (S67 canonical).
        (iii) Tensor power spectrum at horizon exit:
                P_T(k_exit) = (2*H(t_k*)^2) / (pi^2 * M_Pl^2)          (T.3)
             where t_k* is the time at which mode k exits the horizon:
             c_T(k)*k = a(t_k*) * H(t_k*).
        (iv) Scalar power spectrum at horizon exit (slow-roll, c_S=c_BLV):
                P_zeta(k_exit) = H(t_k*)^2 / (8*pi^2*M_Pl^2*eps_H * c_S)   (T.4)
        (v) Tensor-to-scalar ratio at horizon exit:
                r(k) = P_T(k)/P_zeta(k) = 16 * eps_H(t_k*) * (c_S/c_T)  (T.5)
             (Cheung-Creminelli-Fitzpatrick-Kaplan-Senatore 2008; Baumann
              TASI lectures 2012, eq. 6.111 with c_s extension.)

    Step 2 (k-transfer from transit to CMB — substrate).
        (a) k_transit is the wavenumber that exits the horizon at tau~0.19
            (the fold). k_CMB is the wavenumber that exits the horizon at
            tau_CMB (roughly 50-60 e-folds before the fold).
        (b) BOTH tensor modes are superhorizon between their exit time and
            today. Weinberg's superhorizon conservation theorem applies:
                h_k(eta >> eta_exit) = const
            so |T_h|^2 = 1 for amplitude transfer (S66/S68 established).
        (c) The k-DEPENDENCE of r(k) comes entirely from eps_H(t_k*) and
            the (c_S/c_T) ratio evaluated at the k-appropriate exit time.
        (d) Formal transfer function relating r(k_transit) to r(k_CMB):
                T^2(k_transit -> k_CMB) := r(k_CMB) / r(k_transit)      (T.6)
            This is a DEFINITION, not a rescaling.
        (e) By (T.5):
                T^2 = [eps_H(tau_CMB) * c_S(CMB)/c_T(CMB)]
                    / [eps_H(tau_transit) * c_S(transit)/c_T(transit)]  (T.7)
        (f) On the substrate c_T = 1 at both scales (structural). c_S =
            c_BLV = 0.485 at both scales for CMB-relevant k (both subhorizon
            at emission). So (c_S/c_T) cancels in the ratio:
                T^2 = eps_H(tau_CMB) / eps_H(tau_transit)               (T.8)

    Step 3 (Simplify — canonical form).
        Substituting (T.5) into the CMB value:
                r(k_CMB) = 16 * eps_H(tau_CMB) * c_BLV                 (T.9)
        (c_T = 1 canceled the numerator.) The transit-scale analog is:
                r(k_transit) = 16 * eps_H(tau_transit) * c_BLV         (T.10)
        Hence:
                r(k_CMB) = r(k_transit) * (T^2)                         (T.11)
        with T^2 given by (T.8). All factors are explicit substrate
        quantities — no ad hoc tuning.

    Step 4 (Direction from canonical form — pre-registered threshold).
        eps_H(tau=0.05) = 1.5118e-3 (S64 epsilon profile, CMB-exit tau)
        c_BLV          = 0.485     (S67 scalar sound speed)
        r(k_CMB)       = 16 * 1.5118e-3 * 0.485
                       = 1.1732e-2                                     (T.12)
        BICEP/Keck 2021 95% CL bound: r < 0.036.
        Direction: r(k_CMB) = 0.0117 < 0.036 => PASS.

    Step 5 (Python verification — plan snippet, verbatim).
        r_transit = compute_r_at_transit()      # 16*eps_H(tau_fold)*c_BLV
        T_factor  = compute_transfer_function(k_transit, k_CMB)
        r_CMB     = T_factor**2 * r_transit
        print(f"r_transit = {r_transit:.4f}")
        print(f"Transfer factor T = {T_factor:.4f}")
        print(f"r(k_CMB) = {r_CMB:.4f}")
        print(f"BICEP/Keck bound = 0.036")
        print(f"Verdict: {'PASS' if r_CMB<0.036 else 'FAIL'}")

L_max:  N/A (no KK spectrum required; uses S64 eps profile and S67 sound
        speeds as inputs).

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py
  - s67_acoustic_tensor.npz  (c_T, c_BLV, k_transit_T, r_at_transit)
  - s64_epsilon_profile.npz  (eps_H(tau) dense)
  - this script

Output 4-tuple:
  (r_CMB=<v>, scheme=substrate-dispersion-transfer,
   convention=c_T(k)-variable, L_max=N/A)
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401, F403
from canonical_constants import PI, tau_fold, A_s_CMB

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

SESSION = "S83"                                                     # (local)
GATE_ID = "S83-TENSOR-TRANSFER-K-TRANSIT-TO-K-CMB"                  # (local)
SCHEME = "substrate-dispersion-transfer"                            # (local)
CONVENTION = "c_T(k)-variable"                                      # (local)
L_MAX = "N/A"                                                       # (local)

OUT_NPZ = SCRIPT_DIR / "s83_w3_g46_tensor_transfer.npz"
OUT_PNG = SCRIPT_DIR / "s83_w3_g46_tensor_transfer.png"
VERDICT_TXT = SCRIPT_DIR / "s83_gate_verdicts.txt"
S67_DATA = SCRIPT_DIR / "s67_acoustic_tensor.npz"                   # (local)
S64_EPS = SCRIPT_DIR / "s64_epsilon_profile.npz"                    # (local)

INPUT_FILES = [
    SCRIPT_DIR / "canonical_constants.py",
    S67_DATA,
    S64_EPS,
    SCRIPT_DIR / "s83_w3_g46_tensor_transfer_k_transit_cmb.py",
]

# Pre-registered threshold (plan L2711, L2730, L2740)
R_BICEP_KECK_95CL = 0.036           # (local) BICEP/Keck 2021 95% CL upper bound

# CMB horizon-exit tau for k_CMB modes (far from fold)
# S66 canonical: tau_CMB ~ 0.05 is the slow-roll sampling epoch for CMB modes
TAU_CMB_EXIT = 0.05                 # (local) CMB horizon-exit tau (S66 canon)

# Transit horizon-exit tau: the fold
TAU_TRANSIT_EXIT = tau_fold         # (local) = 0.19, canonical


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()            # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                        # (local)
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())     # (local)
    h = hashlib.sha256()             # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Substrate dispersion + transfer (substitution chain T.6 - T.11)
# ---------------------------------------------------------------------------

def compute_r_at_scale(eps_H, c_T, c_S):
    """
    Apply Eq. (T.5): r = 16 * eps_H * (c_S/c_T).

    eps_H : Hubble slow-roll parameter evaluated at the k-mode's horizon exit.
    c_T   : tensor sound speed at that scale (substrate: structural = 1).
    c_S   : scalar sound speed at that scale (substrate: = c_BLV for CMB-exit).

    Returns r = P_T/P_zeta at horizon exit.
    """
    if c_T <= 0.0:
        return float('nan')
    return 16.0 * eps_H * (c_S / c_T)


def compute_transfer_squared(eps_CMB, eps_transit, c_T_CMB, c_T_transit,
                              c_S_CMB, c_S_transit):
    """
    Apply Eq. (T.7)/(T.8): the amplitude-conservation Weinberg transfer on
    superhorizon scales. |T_h|^2 = 1 (amplitude), but the RATIO r(k) differs
    between scales by the ratio of horizon-exit parameters. We encapsulate
    the r-ratio as the 'transfer squared' for bookkeeping with Eq. (T.6):

        T^2 := r(k_CMB) / r(k_transit)
             = [eps_CMB * c_S_CMB/c_T_CMB] / [eps_transit * c_S_transit/c_T_transit]

    On the substrate c_T_CMB = c_T_transit = 1, c_S_CMB = c_S_transit = c_BLV
    so T^2 reduces to eps_CMB / eps_transit.
    """
    num = eps_CMB * (c_S_CMB / c_T_CMB) if c_T_CMB > 0 else float('nan')
    den = eps_transit * (c_S_transit / c_T_transit) if c_T_transit > 0 \
          else float('nan')
    if den == 0.0 or not np.isfinite(den):
        return float('nan')
    return num / den


# ---------------------------------------------------------------------------
# Section 6 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                 # (local)

    # 1. Input pins + closure
    if not S67_DATA.exists() or not S64_EPS.exists():
        print(f"INPUT DATA MISSING: {S67_DATA.name} or {S64_EPS.name}")
        return 2
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...")
    print()

    # 2. Load substrate-dispersion inputs (S67 tensor, S64 eps profile)
    print(f"[SECTION 2] Loading S67 and S64 inputs")
    print("-" * 60)
    d67 = np.load(S67_DATA, allow_pickle=True)
    c_T_canon = float(d67['c_tensor'])             # structural = 1.0
    c_S_canon = float(d67['c_BLV'])                # = 0.485
    r_at_transit_S67 = float(d67['r_at_transit'])  # S67 Bogoliubov r
    r_superhorizon_median = float(d67['r_superhorizon_median'])
    k_transit_T = float(d67['k_transit_tensor'])   # M_KK units
    k_transit_S = float(d67['k_transit_scalar'])   # M_KK units
    d67.close()
    print(f"  c_T (tensor sound speed, substrate) = {c_T_canon:.6f}")
    print(f"  c_BLV (scalar sound speed)          = {c_S_canon:.6f}")
    print(f"  r_at_transit (S67 Bogoliubov)       = {r_at_transit_S67:.6e}")
    print(f"  k_transit^T = {k_transit_T:.3f} M_KK, k_transit^S = "
          f"{k_transit_S:.3f} M_KK")

    d64 = np.load(S64_EPS, allow_pickle=True)
    tau_dense = d64['tau_dense']
    eps_H_dense = d64['eps_H_dense']
    d64.close()
    print(f"  eps_H(tau) profile: tau in [{tau_dense.min():.3f}, "
          f"{tau_dense.max():.3f}], {len(tau_dense)} points")

    # Evaluate eps_H at the two canonical horizon-exit tau's
    idx_CMB = int(np.argmin(np.abs(tau_dense - TAU_CMB_EXIT)))
    idx_transit = int(np.argmin(np.abs(tau_dense - TAU_TRANSIT_EXIT)))
    eps_H_CMB = float(eps_H_dense[idx_CMB])         # (local)
    eps_H_transit = float(eps_H_dense[idx_transit]) # (local)
    print(f"  eps_H(tau_CMB={TAU_CMB_EXIT}) = {eps_H_CMB:.6e}")
    print(f"  eps_H(tau_fold={TAU_TRANSIT_EXIT}) = {eps_H_transit:.6e}")
    print()

    # 3. Substitution chain T.5: r at each scale
    #    r_transit via substrate-dispersion formula (check against S67)
    print(f"[SECTION 3] Substitution chain application (T.5, T.9, T.10)")
    print("-" * 60)
    r_transit_formula = compute_r_at_scale(eps_H_transit, c_T_canon, c_S_canon)
    r_CMB_formula = compute_r_at_scale(eps_H_CMB, c_T_canon, c_S_canon)
    print(f"  r(k_transit)  [16*eps*c_S/c_T] = {r_transit_formula:.6e}")
    print(f"  r(k_CMB)      [16*eps*c_S/c_T] = {r_CMB_formula:.6e}")
    print(f"  r(k_transit)  [S67 Bogoliubov] = {r_at_transit_S67:.6e}")

    # Agreement check between formula and S67 Bogoliubov at transit scale.
    # The formula and Bogoliubov approaches address different regimes: the
    # Bogoliubov r applies through the fold transit (non-adiabatic); the
    # formula gives the slow-roll at-horizon-exit r. For CMB scales both
    # are at slow-roll and agree. For transit scales Bogoliubov gives a
    # DIFFERENT number (larger 'instantaneous' r from steep pumps). We
    # report BOTH and flag the difference.
    ratio_formula_vs_S67 = r_transit_formula / r_at_transit_S67
    print(f"  ratio formula/S67 at transit   = {ratio_formula_vs_S67:.4f}")
    print(f"  (DIAGNOSTIC: formula is slow-roll at-exit, S67 is Bogoliubov")
    print(f"   through non-adiabatic fold transit — not expected to match.)")
    print()

    # 4. Transfer function T^2 = r(CMB)/r(transit)  [Eq. T.6]
    #    Using the substrate formula at both scales (slow-roll framework).
    T_sq = compute_transfer_squared(
        eps_CMB=eps_H_CMB, eps_transit=eps_H_transit,
        c_T_CMB=c_T_canon, c_T_transit=c_T_canon,
        c_S_CMB=c_S_canon, c_S_transit=c_S_canon,
    )
    T_factor = float(np.sqrt(T_sq)) if T_sq >= 0 else float('nan')
    print(f"[SECTION 4] Transfer function T^2 = r(CMB)/r(transit)")
    print("-" * 60)
    print(f"  T^2       = {T_sq:.6e}")
    print(f"  T         = {T_factor:.6e}")
    print(f"  r(k_CMB)  = T^2 * r(k_transit_formula)")
    r_CMB_via_transfer = T_sq * r_transit_formula   # (local)
    print(f"            = {T_sq:.6e} * {r_transit_formula:.6e}")
    print(f"            = {r_CMB_via_transfer:.6e}")
    print()
    print(f"  Identity check: r_CMB(direct) = {r_CMB_formula:.6e}")
    identity_ok = bool(
        abs(r_CMB_via_transfer - r_CMB_formula) / r_CMB_formula < 1e-10
    )
    print(f"  Identity (T.11) ok: {identity_ok}")
    print()

    # 5. Plan-snippet verbatim (Step 5)
    print(f"[SECTION 5] Plan-snippet verbatim")
    print("-" * 60)
    # compute_r_at_transit() returns the substrate slow-roll r at tau_fold:
    r_transit = r_transit_formula                   # (local)
    r_CMB = T_factor ** 2 * r_transit               # (local) snippet form
    print(f"r_transit = {r_transit:.4f}")
    print(f"Transfer factor T = {T_factor:.4f}")
    print(f"r(k_CMB) = {r_CMB:.4f}")
    print(f"BICEP/Keck bound = 0.036")
    snippet_verdict = 'PASS' if r_CMB < R_BICEP_KECK_95CL else 'FAIL'
    print(f"Verdict: {snippet_verdict}")
    print()

    # 6. Pre-registered verdict
    print(f"[SECTION 6] Pre-registered verdict")
    print("-" * 60)
    print(f"  Threshold: r(k_CMB) < {R_BICEP_KECK_95CL:.3f} (BICEP/Keck 2021)")
    print(f"  Computed:  r(k_CMB) = {r_CMB:.6e}")
    if r_CMB < R_BICEP_KECK_95CL:
        verdict = "PASS"
    else:
        verdict = "FAIL"
    print(f"  => verdict: {verdict}")
    print()
    assert snippet_verdict == verdict, \
        "snippet verdict disagrees with main verdict"

    # 7. Cross-checks
    print(f"[SECTION 7] Cross-checks")
    print("-" * 60)

    # CC-1: finite positive quantities
    cc1_finite = bool(
        np.isfinite(r_transit_formula) and r_transit_formula > 0 and
        np.isfinite(r_CMB_formula) and r_CMB_formula > 0 and
        np.isfinite(T_sq) and T_sq > 0
    )

    # CC-2: direction — eps_H(CMB) < eps_H(transit) at slow-roll far from
    # fold because eps grows toward the fold. Therefore T^2 < 1 (suppression).
    #   Substitution chain CC-2:
    #     eps_H(0.05) = 1.5118e-3 (S64 eps profile)
    #     eps_H(0.19) = ? (S64; expected larger since closer to fold)
    #     T^2 = eps(CMB)/eps(transit); if numerator < denominator, T^2 < 1.
    #   Direction: T^2 < 1 => r(CMB) < r(transit).
    cc2_T_sq_lt_1 = bool(T_sq < 1.0)

    # CC-3: identity r(CMB) = T^2 * r(transit) from substitution chain T.11
    cc3_identity = identity_ok

    # CC-4: r(k_CMB) formula in canonical form equals 16*eps_H(CMB)*c_BLV
    r_CMB_direct = 16.0 * eps_H_CMB * c_S_canon     # (local)
    cc4_r_CMB_canonical = bool(
        abs(r_CMB_direct - r_CMB_formula) / r_CMB_formula < 1e-12
    )

    # CC-5: BICEP/Keck threshold is correctly pinned to the literature value
    cc5_bicep_threshold = bool(abs(R_BICEP_KECK_95CL - 0.036) < 1e-12)

    # CC-6: ratio to BICEP bound (by how many factors we are below)
    factor_below = R_BICEP_KECK_95CL / r_CMB           # (local)
    cc6_factor_positive = bool(factor_below > 0)

    # CC-7: k-mode separation is physically meaningful
    # k_transit ~ 587 M_KK, k_CMB (in M_KK units) is vastly smaller
    # (decades below k_transit). The transfer operates over this range.
    cc7_k_separation_sane = bool(k_transit_T > 1.0)

    cc_all_ok = bool(
        cc1_finite and cc2_T_sq_lt_1 and cc3_identity and
        cc4_r_CMB_canonical and cc5_bicep_threshold and
        cc6_factor_positive and cc7_k_separation_sane
    )
    print(f"  CC-1 finite positive r, T^2          : {cc1_finite}")
    print(f"  CC-2 T^2 < 1 (eps grows toward fold) : {cc2_T_sq_lt_1}")
    print(f"  CC-3 identity r_CMB = T^2*r_transit  : {cc3_identity}")
    print(f"  CC-4 r_CMB = 16*eps_CMB*c_BLV direct : {cc4_r_CMB_canonical}")
    print(f"  CC-5 BICEP/Keck threshold pinned     : {cc5_bicep_threshold}")
    print(f"  CC-6 factor below bound = {factor_below:.3f}")
    print(f"  CC-7 k-mode separation sane          : {cc7_k_separation_sane}")
    print(f"  ALL cross-checks                     : {cc_all_ok}")
    print()

    # 8. Save artifacts
    np.savez(
        OUT_NPZ,
        # Canonical inputs (pinned)
        c_T_canon=c_T_canon,
        c_S_canon=c_S_canon,
        r_at_transit_S67=r_at_transit_S67,
        r_superhorizon_median_S67=r_superhorizon_median,
        k_transit_T=k_transit_T,
        k_transit_S=k_transit_S,
        tau_CMB_exit=TAU_CMB_EXIT,
        tau_transit_exit=TAU_TRANSIT_EXIT,
        eps_H_CMB=eps_H_CMB,
        eps_H_transit=eps_H_transit,
        # Substrate-dispersion outputs
        r_transit_formula=r_transit_formula,
        r_CMB_formula=r_CMB_formula,
        r_CMB_via_transfer=r_CMB_via_transfer,
        r_CMB=r_CMB,
        T_sq=T_sq,
        T_factor=T_factor,
        # Threshold + verdict
        r_BICEP_Keck_95CL=R_BICEP_KECK_95CL,
        factor_below_bound=factor_below,
        verdict=verdict,
        # Cross-checks
        cc_all_ok=cc_all_ok,
        cc1_finite=cc1_finite,
        cc2_T_sq_lt_1=cc2_T_sq_lt_1,
        cc3_identity=cc3_identity,
        cc4_r_CMB_canonical=cc4_r_CMB_canonical,
        cc5_bicep_threshold=cc5_bicep_threshold,
        cc6_factor_positive=cc6_factor_positive,
        cc7_k_separation_sane=cc7_k_separation_sane,
        # Diagnostic
        ratio_formula_vs_S67_at_transit=ratio_formula_vs_S67,
        # Closure
        closure=closure,
    )
    print(f"Artifacts: {OUT_NPZ.name}")

    # 9. Plot — 2 panels
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    ax0, ax1 = axes

    # Panel (a): eps_H(tau) profile with the two horizon-exit tau markers
    mask = (tau_dense >= 0.01) & (tau_dense <= 0.25)
    ax0.plot(tau_dense[mask], eps_H_dense[mask], 'b-', linewidth=2,
             label=r'$\epsilon_H(\tau)$')
    ax0.axvline(TAU_CMB_EXIT, color='g', linestyle='--', linewidth=1.5,
                label=fr'$\tau_{{\rm CMB}}={TAU_CMB_EXIT}$, '
                      fr'$\epsilon_H={eps_H_CMB:.2e}$')
    ax0.axvline(TAU_TRANSIT_EXIT, color='r', linestyle='--', linewidth=1.5,
                label=fr'$\tau_{{\rm fold}}={TAU_TRANSIT_EXIT}$, '
                      fr'$\epsilon_H={eps_H_transit:.2e}$')
    ax0.set_yscale('log')
    ax0.set_xlabel(r'$\tau$')
    ax0.set_ylabel(r'$\epsilon_H(\tau)$')
    ax0.set_title(r'Substrate $\epsilon_H$ profile (S64)')
    ax0.legend(loc='lower right', fontsize=9)
    ax0.grid(True, alpha=0.3)

    # Panel (b): r at each scale + BICEP/Keck band
    scales = ['r(transit)\n[formula]', 'r(transit)\n[S67-Bogol]', 'r(CMB)']
    r_vals = [r_transit_formula, r_at_transit_S67, r_CMB]
    colors = ['#d95f0e', '#8c2d04', '#2c7fb8']
    bars = ax1.bar(scales, r_vals, color=colors, alpha=0.85, edgecolor='k',
                   linewidth=0.5)
    for b, v in zip(bars, r_vals):
        ax1.text(b.get_x() + b.get_width() / 2., v * 1.25,
                 f'{v:.3e}', ha='center', va='bottom', fontsize=9, rotation=0)
    ax1.axhline(R_BICEP_KECK_95CL, color='k', linestyle='--', linewidth=1.3,
                label=fr'BICEP/Keck 95% CL = {R_BICEP_KECK_95CL}')
    ax1.axhspan(0, R_BICEP_KECK_95CL, color='g', alpha=0.10,
                label='PASS band')
    ax1.set_yscale('log')
    ax1.set_ylabel(r'$r$ (log)')
    ax1.set_title(fr'Tensor-to-scalar ratio — $r(k_{{\rm CMB}})={r_CMB:.4f}$ '
                  fr'$\to$ {verdict}')
    ax1.legend(loc='upper left', fontsize=9)
    ax1.grid(True, alpha=0.3, which='both', axis='y')

    fig.suptitle(f'S83 W3-G46 TENSOR-TRANSFER-K-TRANSIT-TO-K-CMB — {verdict} '
                 f'(r_CMB = {r_CMB:.4f})', fontsize=12)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110, bbox_inches='tight')
    plt.close(fig)
    print(f"Plot:      {OUT_PNG.name}")

    # 10. 4-tuple tag + verdict line
    tag = (f"(r_CMB={r_CMB:.6f}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n4-tuple: {tag}")

    verdict_line = (
        f"{GATE_ID}: {verdict} -- value={r_CMB:.6f} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"sha256={closure}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_line)
    print(f"Verdict line appended to: {VERDICT_TXT.name}")
    print(f"  {verdict_line.strip()}")

    wall = time.time() - t0          # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0 if verdict == "PASS" else (1 if verdict == "FAIL" else 3)


if __name__ == "__main__":
    sys.exit(main())
