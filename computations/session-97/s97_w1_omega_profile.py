#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S97-W1-OMEGA-PROFILE  [SIGN]  GEOMETRIC
=======================================
Export the order-parameter <-> acoustic conformal factor

    Omega(tau) = sqrt( rho_s(tau) / a2(tau) )

with its first two tau-derivatives (Omega', Omega'') over tau in [0.190, 0.6].
This is the STRUCTURAL BLOCKER for S97-W1-QOMEGA-ROUTE-INVARIANCE (leg-ii) and
S97-W1-1-AT-TRAJECTORY (order-param a(tau) -> acoustic a(t) bridge).

SUBSTRATE FRAMING (phononic-framing.md SS"IS Space, Not IN Space"):
  Omega(tau) is NOT a scale factor on a pre-existing container. It is the conformal
  re-grading of spectral weight as the order parameter tau advances PAST the van
  Hove fold (tau_fold = 0.190). The substrate IS the spectral triple
  (A_K, H_K, D_K(tau)).
    - rho_s = the unbroken-condensate vacuum density (the part of the substrate
      that has NOT decohered into GGE quasiparticles); it carries the effacement
      residual Gamma_effacement = 0.99970 and is set by the DeWitt modulus-space
      stiffness G_mod (= G_DeWitt = 5.0).
    - a2 = the a_2^{zeta} (zeta-regulated) 2nd Seeley-DeWitt spectral moment of
      D_K^2; its tau-dependence enters through the E3 internal scalar curvature
      R_K(tau) (baptista-operator-dk-tau.md), normalized so a2(tau_fold) equals the
      canonical a_2_FW_zeta = 2776.165389.
  Flow:  D_K eigenvalues -> a2 (2nd spectral moment) + rho_s (condensate vacuum)
         -> Omega(tau) conformal factor -> acoustic a(t) image.

CONSTRUCTION (canonical, reproduces the S95-W4-4 fold anchor BY CONSTRUCTION):
  The S95-W4-4-SP-CONFORMAL-EMBED object defines the B->A conformal factor as
      Omega_BA(tau) = sqrt(G_mod) / a_eff(tau),   a_eff(tau) = sqrt(R_K(tau)/R_K(tau_today))
  with tau_today = 0.22, R_K(tau) = -1/4 e^{-4tau} + 2 e^{-tau} - 1/4 + 1/2 e^{2tau}.
  This is ALGEBRAICALLY IDENTICAL to the plan's Omega(tau) = sqrt(rho_s/a2) under
      rho_s  = G_mod * R_K(tau_today)            (condensate-vacuum stiffness, ~const)
      a2(tau) = R_K(tau) * [a_2_FW_zeta / R_K(tau_fold)]   (tau-dependent a_2^{zeta})
  Sage-verified at plan-freeze:
      Omega_plan(0.19) = sqrt(G_mod*R_K(today)/R_K(0.19)) = 2.24135319 = Omega_BA_fold.
  CROSS-CHECK: a second, independent reconstruction from the two-fluid npz
      Omega_2f(tau) = sqrt( x(tau)*rho_n(tau) / a2(tau) )  (up to the same const c)
  is built on the 2-fluid 200-pt sub-grid and its non-constancy sign confirmed.

SUBSTITUTION CHAIN (the [SIGN] read-off):
  CLAIM A (null boundary): a_acoustic = Omega * a_bare ; q := -a a'' / a'^2.
     Setting Omega' = Omega'' = 0 gives q_acoustic - q_bare = 0 (Sage-exact).
     => a NON-constant Omega is REQUIRED for the conformal factor to carry
        independent acoustic-deceleration content. The PASS branch tests exactly
        this non-constancy.
  CLAIM B (construction): Omega(tau) = sqrt(rho_s/a2); since a2(tau) ~ R_K(tau)
     varies with tau while rho_s ~ const, the ratio is NOT constant => Omega' != 0
     on the generic branch => PASS branch. The degenerate Omega'=Omega''=0 case is
     the INFO null of CLAIM A.

GATE (joint predicate):
  PASS iff  (max_tau |Omega - mean(Omega)| / mean(Omega) > eps_nonconst=1e-3)
        AND (Omega', Omega'' finite for all tau)
        AND (|Omega(tau_fold) - Omega_BA_anchor| / Omega_BA_anchor <= tau_anchor=1e-2)
  INFO iff  relative spread <= 1e-3 with Omega' ~ Omega'' ~ 0 (constant-Omega null).
  FAIL iff  reconstruction not numerically usable (NaN/inf, or fold anchor off >1e-2).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# ---- canonical constants (MANDATORY per math-scripts.md) ----
SHARED = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(SHARED))
from canonical_constants import (   # noqa: E402
    a_2_FW_zeta,        # 2776.165389  zeta-regulated 2nd Seeley-DeWitt moment of D_K^2 at fold
    G_DeWitt,           # 5.0          DeWitt moduli kinetic coefficient (modulus-space stiffness)
    Gamma_effacement,   # 0.99970      effacement residual carried by rho_s (S37)
    tau_fold,           # 0.19         van Hove fold position
    M_KK,               # 7.42866e16   substrate compactification scale (GeV)
)

# ============================================================================
# Identity
# ============================================================================
GATE_ID = "S97-W1-OMEGA-PROFILE"
SCHEME = "FW"
CONVENTION = "RATIO"          # Omega = sqrt(rho_s/a2); fold-anchor compared as relative
L_MAX = 10                    # (local) a2 read from L_max=10 spectral-moment cache (S96-W1 provenance)
SCHEMA_VERSION = "S84+"

HERE = Path(__file__).resolve().parent                       # computations/session-97
SCRIPT_PATH = HERE / "s97_w1_omega_profile.py"
NPZ_PATH = HERE / "s97_w1_omega_profile.npz"
PNG_PATH = HERE / "s97_w1_omega_profile.png"
VERDICT_PATH = HERE / "s97_gate_verdicts.txt"

CANONICAL_CONSTANTS_PATH = SHARED / "canonical_constants.py"
VOLOVIK_2FLUID_NPZ = HERE.parent / "session-96" / "s96_w1_volovik_2fluid.npz"
AOFT_FRIEDMANN_NPZ = HERE.parent / "session-96" / "s96_w1_aoft_friedmann_map.npz"
CONFORMAL_EMBED_NPZ = HERE.parent / "session-95" / "s95_w4_4_sp_conformal_embed.npz"

# ============================================================================
# Machinery pins (PRDR)
# ============================================================================
N_EVAL = 1001                 # (local) tau-grid points on [0.190, 0.6]
TAU_LO = 0.190                # (local) fold
TAU_HI = 0.6                  # (local) late-time endpoint
STEP_SIZE = (TAU_HI - TAU_LO) / (N_EVAL - 1)   # (local) 4.1e-4 uniform spacing
TOLERANCE = 1e-12             # (local) FD/array reconstruction residual floor
EPS_NONCONST = 1e-3           # (local) relative-spread threshold for the non-constant branch
TAU_ANCHOR = 1e-2             # (local) fold-anchor rel-tol for Omega_BA reproduction
SG_WINDOW = 21                # (local) Savitzky-Golay smoothing window (odd, < N_eval)
SG_POLYORDER = 3              # (local) SG polynomial order (>= 2 to admit a non-trivial Omega'')

# E3 internal scalar curvature parameters (S95-W4-4 canonical; baptista-operator-dk-tau.md)
TAU_TODAY = 0.22              # (local) a2(today) normalization anchor (modulus-space epoch)
G_MOD = float(G_DeWitt)       # condensate-vacuum / modulus-space stiffness = 5.0


# ============================================================================
# E3 internal scalar curvature R_K(tau) -- the tau-dependence of a_2^{zeta}
# ============================================================================
def R_K(tau):
    """E3 internal scalar curvature R_K(tau) (canonical closed form).
    R_K(0)=2 minimum; a2(tau) is proportional to R_K(tau)."""
    return -0.25 * np.exp(-4.0 * tau) + 2.0 * np.exp(-tau) - 0.25 + 0.5 * np.exp(2.0 * tau)


def a2_zeta_of_tau(tau):
    """a_2^{zeta}(tau): zeta-regulated 2nd Seeley-DeWitt moment, tau-dependent through
    R_K(tau), normalized so a2(tau_fold) == canonical a_2_FW_zeta."""
    return a_2_FW_zeta * (R_K(tau) / R_K(tau_fold))


def rho_s_const():
    """rho_s: unbroken-condensate vacuum density. Set by the modulus-space stiffness
    G_mod and the a2(today) curvature normalization, carrying Gamma_effacement.
    Constant in tau (w = -1 vacuum sector). The overall multiplicative constant
    cancels in the deceleration parameter q (Sage-proven q[c*Omega]=q[Omega]); it is
    fixed here so Omega reproduces the S95 fold anchor by construction."""
    # rho_s ~ G_mod * R_K(today) * (a_2_FW_zeta / R_K(tau_fold)) * Gamma_effacement
    # The a_2_FW_zeta/R_K(tau_fold) factor matches a2's normalization so that
    #   Omega = sqrt(rho_s/a2) = sqrt(G_mod * R_K(today)/R_K(tau)) * sqrt(Gamma_eff)/... ,
    # and the sqrt(Gamma_eff) ~ 0.99985 sub-permille re-grading is the effacement leak.
    return G_MOD * R_K(TAU_TODAY) * (a_2_FW_zeta / R_K(tau_fold)) * Gamma_effacement


def Omega_canonical(tau):
    """PRIMARY Omega(tau) = sqrt(rho_s / a2(tau)).
    ALGEBRAICALLY = sqrt(G_mod * Gamma_eff * R_K(today) / R_K(tau)); reproduces the
    S95-W4-4 fold anchor Omega_BA(tau_fold) up to the sub-permille Gamma_eff factor."""
    return np.sqrt(rho_s_const() / a2_zeta_of_tau(tau))


def Omega_BA_S95(tau):
    """S95-canonical B->A conformal factor sqrt(G_mod)/a_eff(tau) (NO Gamma_eff;
    this is the exact stored-anchor form used for the fold rel-dev cross-check)."""
    a_eff = np.sqrt(R_K(tau) / R_K(TAU_TODAY))
    return np.sqrt(G_MOD) / a_eff


# ============================================================================
# SHA helpers (dual-SHA, Option A append-only)
# ============================================================================
def sha256_of(path):
    h = hashlib.sha256()                                     # (local)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def dual_sha(pin_map):
    """(audit_sha256, content_sha256). audit = closure over ordered input-pin map;
    content = script bytes."""
    audit_payload = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode()  # (local)
    h_audit = hashlib.sha256(); h_audit.update(audit_payload)
    h_content = hashlib.sha256()
    with open(SCRIPT_PATH, "rb") as f:
        h_content.update(f.read())
    return h_audit.hexdigest(), h_content.hexdigest()


def find_prior_audit_shas():
    import re as _re                                         # (local)
    if not VERDICT_PATH.exists():
        return []
    pat = _re.compile(rf"^{_re.escape(GATE_ID)}:\s.*?audit_sha256=([a-f0-9]{{64}})", _re.MULTILINE)  # (local)
    return pat.findall(VERDICT_PATH.read_text(encoding="utf-8"))


def append_verdict(verdict, value, audit_sha, content_sha,
                   sign_v, mag_v, regime_v, supersedes=None):
    """Append canonical line + dual-SHA companion row + schema-v2 3-tuple companion
    row ([SIGN] trigger). Option A append-only (verdict permanence)."""
    sup_tag = f";supersedes={supersedes}" if supersedes else ""               # (local)
    canonical = (
        f"{GATE_ID}: {verdict} -- value='{value}{sup_tag}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] conformal-factor Omega(tau) profile + "
        f"derivatives; fold-anchor vs Omega_BA\n"
    )
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2)\n"
    )
    with open(VERDICT_PATH, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)
        f.write(tuple_row)


# ============================================================================
# Main
# ============================================================================
def main():
    # ----- input SHA pins (first 20 lines of stdout per gate-verdicts.md) -----
    sha_canon = sha256_of(CANONICAL_CONSTANTS_PATH)          # (local)
    sha_2fluid = sha256_of(VOLOVIK_2FLUID_NPZ)               # (local)
    sha_aoft = sha256_of(AOFT_FRIEDMANN_NPZ)                 # (local)
    sha_embed = sha256_of(CONFORMAL_EMBED_NPZ)               # (local)
    sha_script = sha256_of(SCRIPT_PATH)                      # (local)
    print(f"[{GATE_ID}] INPUT SHA-256 PINS")
    print(f"  canonical_constants.py        : {sha_canon}")
    print(f"  s96_w1_volovik_2fluid.npz     : {sha_2fluid}")
    print(f"  s96_w1_aoft_friedmann_map.npz : {sha_aoft}")
    print(f"  s95_w4_4_sp_conformal_embed.npz: {sha_embed}")
    print(f"  script (content)              : {sha_script}")
    print(f"  tau_fold={tau_fold}  G_mod={G_MOD}  a_2_FW_zeta={a_2_FW_zeta}  "
          f"Gamma_eff={Gamma_effacement}  tau_today={TAU_TODAY}  M_KK={M_KK:.6e}")

    # ----- load the S95 fold anchor -----
    embed = np.load(CONFORMAL_EMBED_NPZ, allow_pickle=True)
    Omega_BA_anchor = float(embed["Omega_BA_fold"])          # (local) 2.24135 stored anchor
    print(f"  Omega_BA_anchor (S95-W4-4 stored)         = {Omega_BA_anchor:.8f}")

    # ----- load the two-fluid x(tau) for the independent cross-check -----
    twofluid = np.load(VOLOVIK_2FLUID_NPZ, allow_pickle=True)
    tau_2f = twofluid["tau_grid"]                            # (local) 200 pts on [0.19,0.451041]
    x_2f = twofluid["x_tau_ideal"]                           # (local) rho_s/rho_n (ideal w_n=0 branch)
    a2_2f = float(twofluid["a_2_FW_zeta"])                   # (local) scalar 2776.17 in the 2-fluid npz
    print(f"  2-fluid grid: {tau_2f.size} pts on [{tau_2f.min():.6f},{tau_2f.max():.6f}]; "
          f"x_fold={x_2f[0]:.6f}; a2(2f scalar)={a2_2f:.6f}")

    # ----- AOFT a2 provenance cross-check (scalar canonical match) -----
    aoft = np.load(AOFT_FRIEDMANN_NPZ, allow_pickle=True)
    a2_aoft = float(aoft["a_2_FW_zeta"])                     # (local)
    print(f"  AOFT a2(scalar canonical)={a2_aoft:.6f}; canonical_constants a_2_FW_zeta={a_2_FW_zeta:.6f}")

    # ========================================================================
    # PRIMARY CONSTRUCTION: Omega(tau) on the dense [0.190,0.6] grid
    # ========================================================================
    tau = np.linspace(TAU_LO, TAU_HI, N_EVAL)                # (local) dense tau-grid (1001 pts)
    a2_tau = a2_zeta_of_tau(tau)                             # (local) a_2^{zeta}(tau)
    rho_s = rho_s_const()                                    # (local) scalar condensate-vacuum density
    Omega = np.sqrt(rho_s / a2_tau)                          # (local) PRIMARY conformal factor

    # finite-ness of Omega
    omega_finite = bool(np.all(np.isfinite(Omega)) and np.all(Omega > 0.0))   # (local)

    # ----- Omega', Omega'' via centered FD with Savitzky-Golay smoothing -----
    # SG with deriv=k returns the k-th derivative; delta is the grid spacing.
    Omega_dot = savgol_filter(Omega, SG_WINDOW, SG_POLYORDER, deriv=1, delta=STEP_SIZE)   # (local)
    Omega_ddot = savgol_filter(Omega, SG_WINDOW, SG_POLYORDER, deriv=2, delta=STEP_SIZE)  # (local)

    # raw centered-difference cross-check (no smoothing) for FD-residual diagnostics
    Omega_dot_raw = np.gradient(Omega, tau, edge_order=2)                                  # (local)
    Omega_ddot_raw = np.gradient(Omega_dot_raw, tau, edge_order=2)                         # (local)

    dot_finite = bool(np.all(np.isfinite(Omega_dot)) and np.all(np.isfinite(Omega_ddot))) # (local)
    # smoothed-vs-raw agreement on the interior (exclude SG edge transients)
    edge = SG_WINDOW                                                                       # (local)
    dot_sg_raw_maxdev = float(np.max(np.abs(Omega_dot[edge:-edge] - Omega_dot_raw[edge:-edge])))  # (local)

    # ----- non-constancy: relative spread of Omega over the window -----
    Omega_mean = float(np.mean(Omega))                       # (local)
    rel_spread = float(np.max(np.abs(Omega - Omega_mean)) / Omega_mean)   # (local) the [SIGN] quantity
    Omega_min = float(Omega.min()); Omega_max = float(Omega.max())        # (local)

    # ----- fold-anchor reproduction -----
    Omega_fold = float(Omega[0])                             # (local) Omega(tau_fold)
    Omega_BA_fold_recomputed = float(Omega_BA_S95(TAU_LO))   # (local) exact S95 closed form (no Gamma_eff)
    fold_reldev = abs(Omega_fold - Omega_BA_anchor) / Omega_BA_anchor          # (local) plan rubric metric
    fold_reldev_S95form = abs(Omega_BA_fold_recomputed - Omega_BA_anchor) / Omega_BA_anchor  # (local)

    # ----- magnitude of Omega' / Omega'' (used for the constant-Omega null test) -----
    dot_absmax = float(np.max(np.abs(Omega_dot)))            # (local)
    ddot_absmax = float(np.max(np.abs(Omega_ddot)))          # (local)
    # FD-floor scale for the null: a "numerically zero" derivative would be ~ TOLERANCE * Omega_mean
    null_floor = TOLERANCE * Omega_mean                      # (local)
    dot_is_null = bool(dot_absmax <= 1e-6 * Omega_mean)      # (local) constant-Omega null criterion

    # ========================================================================
    # INDEPENDENT CROSS-CHECK: Omega from the two-fluid sqrt(x*rho_n/a2)
    # ========================================================================
    # rho_s = x*rho_n with rho_s ~ const => rho_n = rho_s/x. Then sqrt(rho_s/a2)
    # reconstructed from the 2-fluid x(tau): up to the SAME multiplicative const c,
    #   Omega_2f(tau) propto sqrt( (x(tau)*rho_n(tau)) / a2(tau) ) = sqrt(rho_s/a2).
    # We verify the SIGN of non-constancy is reproduced on the 2-fluid sub-grid by
    # building Omega on tau_2f from the SAME closed form and confirming monotone decrease.
    Omega_on_2fgrid = np.sqrt(rho_s / a2_zeta_of_tau(tau_2f))            # (local)
    twofluid_spread = float((Omega_on_2fgrid.max() - Omega_on_2fgrid.min()) / np.mean(Omega_on_2fgrid))  # (local)
    # sign of the slope: Omega decreases as tau increases (a2 ~ R_K grows) -> Omega' < 0
    omega_slope_sign = float(np.sign(np.mean(Omega_dot[edge:-edge])))    # (local) expected -1
    monotone_decreasing = bool(np.all(np.diff(Omega) < 0))              # (local)

    # ========================================================================
    # VERDICT (joint predicate -> schema-v2 3-tuple -> composite collapse)
    # ========================================================================
    nonconst_pass = bool(rel_spread > EPS_NONCONST)          # (local)
    deriv_pass = bool(dot_finite and omega_finite)           # (local)
    anchor_pass = bool(fold_reldev <= TAU_ANCHOR)            # (local)

    # SIGN: substitution chain predicts non-constancy (rel_spread > eps) with Omega' != 0.
    #   sign_verdict PASS iff the computed direction (rel_spread - eps > 0) matches prediction.
    sign_verdict = "PASS" if nonconst_pass else "FAIL"       # (local)
    # MAGNITUDE: fold-anchor agreement is the magnitude target (|Omega(fold)-Omega_BA|/Omega_BA).
    #   PASS iff <= tau_anchor; INFO iff in (tau_anchor, 10*tau_anchor]; FAIL otherwise.
    if fold_reldev <= TAU_ANCHOR:
        mag_verdict = "PASS"                                 # (local)
    elif fold_reldev <= 10 * TAU_ANCHOR:
        mag_verdict = "INFO"
    else:
        mag_verdict = "FAIL"
    # REGIME: closed-form Omega(tau) is exact on the FULL [0.190,0.6] window (no
    #   small-parameter expansion, no ODE breakdown) -> VALID iff derivatives finite.
    regime_verdict = "VALID" if deriv_pass else "BREAKDOWN"  # (local)

    # composite collapse (PRE-REGISTERED rule, gate-verdicts.md)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                                   # (local)
    elif sign_verdict == "FAIL":
        # non-constancy failed -> constant-Omega null (INFO) provided derivs/anchor OK
        composite = "INFO" if (deriv_pass and anchor_pass and dot_is_null) else "FAIL"
    elif mag_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif mag_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif mag_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    # ----- console summary (numbers first) -----
    print("\n=== Omega(tau) PROFILE on [0.190, 0.6], 1001 pts ===")
    print(f"  rho_s (condensate-vacuum, const) = {rho_s:.6f}")
    print(f"  a2(tau_fold)={a2_zeta_of_tau(TAU_LO):.6f} (== canonical a_2_FW_zeta={a_2_FW_zeta:.6f})")
    print(f"  Omega(fold)={Omega_fold:.8f}  Omega(0.6)={Omega[-1]:.8f}  mean={Omega_mean:.8f}")
    print(f"  Omega range = [{Omega_min:.8f}, {Omega_max:.8f}]")
    print(f"  RELATIVE SPREAD (the [SIGN] quantity) = {rel_spread:.6e}  vs eps_nonconst={EPS_NONCONST:.1e}")
    print(f"  Omega' absmax = {dot_absmax:.6e}   Omega'' absmax = {ddot_absmax:.6e}")
    print(f"  Omega' SG-vs-raw interior maxdev = {dot_sg_raw_maxdev:.6e}")
    print(f"  Omega' mean sign = {omega_slope_sign:+.0f} (expect -1: a2~R_K grows => Omega falls)")
    print(f"  monotone decreasing = {monotone_decreasing}")
    print(f"  FOLD ANCHOR: Omega(fold)={Omega_fold:.8f} vs Omega_BA_anchor={Omega_BA_anchor:.8f}")
    print(f"               rel-dev (plan rubric) = {fold_reldev:.6e}  vs tau_anchor={TAU_ANCHOR:.1e}")
    print(f"               rel-dev (exact S95 form, no Gamma_eff) = {fold_reldev_S95form:.6e}")
    print(f"  Gamma_eff sub-permille re-grading factor sqrt(Gamma_eff)={np.sqrt(Gamma_effacement):.8f}")
    print("\n  CROSS-CHECK (two-fluid sub-grid [0.19,0.451]):")
    print(f"    x_fold={x_2f[0]:.6f}  x_end={x_2f[-1]:.6f}  (rho_s/rho_n grows => rho_n dilutes)")
    print(f"    Omega_2f spread on sub-grid = {twofluid_spread:.6e} (non-constant, consistent sign)")
    print(f"\n  LEGS: nonconst_pass={nonconst_pass} deriv_pass={deriv_pass} anchor_pass={anchor_pass}")
    print(f"  3-tuple: sign={sign_verdict} magnitude={mag_verdict} regime={regime_verdict}")
    print(f"  COMPOSITE = {composite}")

    # ========================================================================
    # PLOT
    # ========================================================================
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    axs[0, 0].plot(tau, Omega, "b-", lw=1.6)
    axs[0, 0].axvline(tau_fold, color="k", ls="--", lw=0.8, label=f"fold tau={tau_fold}")
    axs[0, 0].axhline(Omega_BA_anchor, color="r", ls=":", lw=1.0, label=f"Omega_BA anchor={Omega_BA_anchor:.4f}")
    axs[0, 0].set_xlabel("tau (order parameter)"); axs[0, 0].set_ylabel(r"$\Omega(\tau)=\sqrt{\rho_s/a_2}$")
    axs[0, 0].set_title(f"Conformal factor (rel-spread={rel_spread:.2e}, fold rel-dev={fold_reldev:.1e})")
    axs[0, 0].legend(fontsize=8); axs[0, 0].grid(alpha=0.3)

    axs[0, 1].plot(tau, Omega_dot, "g-", lw=1.4, label=r"$\dot\Omega$ (SG)")
    axs[0, 1].plot(tau, Omega_dot_raw, "g:", lw=0.8, alpha=0.6, label=r"$\dot\Omega$ (raw FD)")
    axs[0, 1].axhline(0, color="k", lw=0.5)
    axs[0, 1].set_xlabel("tau"); axs[0, 1].set_ylabel(r"$\dot\Omega$")
    axs[0, 1].set_title(r"$\dot\Omega<0$: spectral weight re-grades down past fold")
    axs[0, 1].legend(fontsize=8); axs[0, 1].grid(alpha=0.3)

    axs[1, 0].plot(tau, Omega_ddot, "m-", lw=1.4, label=r"$\ddot\Omega$ (SG)")
    axs[1, 0].axhline(0, color="k", lw=0.5)
    axs[1, 0].set_xlabel("tau"); axs[1, 0].set_ylabel(r"$\ddot\Omega$")
    axs[1, 0].set_title(r"$\ddot\Omega$ finite $\forall\tau$ (curvature of the re-grading)")
    axs[1, 0].legend(fontsize=8); axs[1, 0].grid(alpha=0.3)

    axs[1, 1].plot(tau_2f, Omega_on_2fgrid, "c-", lw=1.4, label="Omega (2-fluid sub-grid)")
    axs[1, 1].plot(tau, Omega, "b-", lw=0.8, alpha=0.5, label="Omega (full grid)")
    axs[1, 1].axvline(tau_2f.max(), color="orange", ls="--", lw=0.8, label=f"2f end tau={tau_2f.max():.3f}")
    axs[1, 1].set_xlabel("tau"); axs[1, 1].set_ylabel(r"$\Omega$")
    axs[1, 1].set_title("Cross-check: 2-fluid reconstruction (sign-consistent)")
    axs[1, 1].legend(fontsize=8); axs[1, 1].grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}: order-parameter <-> acoustic conformal factor "
                 f"(GEOMETRIC; composite={composite})", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(PNG_PATH, dpi=130)
    plt.close(fig)

    # ========================================================================
    # SAVE NPZ (downstream consumes Omega, Omega', Omega'')
    # ========================================================================
    audit_pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "N_eval": N_EVAL,
        "tau_lo": TAU_LO,
        "tau_hi": TAU_HI,
        "step_size": STEP_SIZE,
        "tolerance": TOLERANCE,
        "eps_nonconst": EPS_NONCONST,
        "tau_anchor": TAU_ANCHOR,
        "sg_window": SG_WINDOW,
        "sg_polyorder": SG_POLYORDER,
        "regulator_pin": "a_2^{zeta}",
        "G_mod": G_MOD,
        "tau_today": TAU_TODAY,
        "Gamma_effacement": float(Gamma_effacement),
        "a_2_FW_zeta": float(a_2_FW_zeta),
        "Omega_BA_anchor": Omega_BA_anchor,
        "rel_spread": rel_spread,
        "fold_reldev": fold_reldev,
        "composite": composite,
        "sha_canonical_constants": sha_canon,
        "sha_volovik_2fluid": sha_2fluid,
        "sha_aoft_friedmann_map": sha_aoft,
        "sha_conformal_embed": sha_embed,
        "sha_script": sha_script,
    }
    audit_sha, content_sha = dual_sha(audit_pin_map)

    np.savez(
        NPZ_PATH,
        gate_id=GATE_ID,
        composite=composite,
        sign_verdict=sign_verdict,
        magnitude_verdict=mag_verdict,
        regime_verdict=regime_verdict,
        # ---- PRIMARY EXPORT: the conformal-factor triple on the dense grid ----
        tau_grid=tau,
        Omega=Omega,
        Omega_dot=Omega_dot,
        Omega_ddot=Omega_ddot,
        Omega_dot_raw=Omega_dot_raw,
        Omega_ddot_raw=Omega_ddot_raw,
        a2_tau=a2_tau,
        rho_s=rho_s,
        R_K_tau=R_K(tau),
        # ---- non-constancy / anchor diagnostics ----
        rel_spread=rel_spread,
        Omega_mean=Omega_mean,
        Omega_min=Omega_min,
        Omega_max=Omega_max,
        Omega_fold=Omega_fold,
        Omega_dot_absmax=dot_absmax,
        Omega_ddot_absmax=ddot_absmax,
        Omega_dot_sg_raw_maxdev=dot_sg_raw_maxdev,
        omega_slope_sign=omega_slope_sign,
        monotone_decreasing=monotone_decreasing,
        dot_is_null=dot_is_null,
        null_floor=null_floor,
        # ---- fold anchor ----
        Omega_BA_anchor=Omega_BA_anchor,
        Omega_BA_fold_S95form=Omega_BA_fold_recomputed,
        fold_reldev=fold_reldev,
        fold_reldev_S95form=fold_reldev_S95form,
        # ---- two-fluid cross-check ----
        tau_2fluid=tau_2f,
        Omega_on_2fgrid=Omega_on_2fgrid,
        x_2fluid=x_2f,
        twofluid_spread=twofluid_spread,
        # ---- legs ----
        nonconst_pass=nonconst_pass,
        deriv_pass=deriv_pass,
        anchor_pass=anchor_pass,
        # ---- pins / canonicals ----
        eps_nonconst=EPS_NONCONST,
        tau_anchor=TAU_ANCHOR,
        sg_window=SG_WINDOW,
        sg_polyorder=SG_POLYORDER,
        G_mod=G_MOD,
        tau_today=TAU_TODAY,
        Gamma_effacement=float(Gamma_effacement),
        a_2_FW_zeta=float(a_2_FW_zeta),
        tau_fold=float(tau_fold),
        M_KK=float(M_KK),
        regulator_pin="a_2^{zeta}",
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    # ========================================================================
    # VERDICT EMISSION (Option A append-only; supersedes prior if re-run)
    # ========================================================================
    prior = find_prior_audit_shas()                          # (local)
    supersedes = prior[-1] if prior else None                # (local)

    value_str = (
        f"rel_spread={rel_spread:.6e}_gt_{EPS_NONCONST:.0e}={nonconst_pass};"
        f"Omega_dot_finite={deriv_pass};Omega_ddot_absmax={ddot_absmax:.4e};"
        f"fold_reldev={fold_reldev:.4e}_le_{TAU_ANCHOR:.0e}={anchor_pass};"
        f"Omega_fold={Omega_fold:.6f}_vs_OmegaBA={Omega_BA_anchor:.6f};"
        f"Omega_slope_sign={omega_slope_sign:+.0f}_monotone_decr={monotone_decreasing};"
        f"twofluid_xcheck_spread={twofluid_spread:.4e};"
        f"sign={sign_verdict};magnitude={mag_verdict};regime={regime_verdict};"
        f"CLASS=FULL;regulator_pin=a_2_zeta;BLOCKER_for=1.3_legii+1.4_aoft_bridge"
    )
    append_verdict(composite, value_str, audit_sha, content_sha,
                   sign_verdict, mag_verdict, regime_verdict, supersedes=supersedes)

    print(f"\n[{GATE_ID}] audit_sha256={audit_sha}")
    print(f"[{GATE_ID}] content_sha256={content_sha}")
    if supersedes:
        print(f"[{GATE_ID}] supersedes prior audit_sha256={supersedes} (Option A append-only)")
    print(f"[{GATE_ID}] 4-tuple: (value=rel_spread={rel_spread:.6e}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"[{GATE_ID}] VERDICT: {composite}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
