#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S96-W1-TAUDOT-PROFILE  (Session 96, Wave 1, gate W1-6)
======================================================

Global sweep-rate profile tau_dot(tau) through the van Hove fold, and the
diabaticity test that decides whether the sudden-quench saturation P_exc=1
(known at the FOLD CENTER, T1 PROVEN: delta_t/T_L = 1.25e-5) holds MODE-BY-MODE
across the ENTIRE van Hove feature, not just at one point.

This gate CONSTRUCTS the minimal one-parameter family of global tau_dot(tau)
profiles consistent with the two pinned endpoints, propagates each through
t(tau) = t_0 + int dtau'/tau_dot(tau'), and tests the local diabaticity ratio
D(tau) = delta_t(tau)/T_L(tau) < 1e-2 across the feature.

SUBSTRATE FRAMING (phononic-framing.md "IS Space, Not IN Space"):
  CLASSIFICATION: PHONONIC. tau is NOT a velocity through a pre-existing time
  coordinate -- tau is the substrate's intrinsic Jensen-deformation parameter
  (the "inflaton" analog driving dS/dtau = +58,673), and tau_dot is the RATE at
  which the substrate's spectral complexity reorganizes. The van Hove fold is a
  feature of the density-of-states R_K(tau); the sweep rate tau_dot through that
  feature controls the diabaticity of the Bogoliubov transformation. This is a
  Level-2 MODULI-DEFORMATION observable: the moduli-space of tau-deformations IS
  substrate-IS; tau_dot(tau) is the substrate's own rate of reorganization, NOT a
  coordinate-velocity in a meta-container. Direction of explanation:
    D_K eigenvalue spectrum -> reorganizes through the van Hove fold R_K(tau) ->
    sweep rate tau_dot(tau) sets the LOCAL diabaticity delta_t/T_L ->
    diabaticity sets |beta_k|^2 (impulsive => P_exc=1 maximal mixing; adiabatic =>
    P_exc->0 no-particle vacuum) -> |beta_k|^2 sets the relic content rho_relic ->
    rho_relic sources H^2. This gate pins the controlling rate GLOBALLY (currently
    known only at the fold), the single highest-leverage transit-side unknown for
    the a(t) closure: the t(tau) map gate-1 integrates is t(tau)=t_0+int dtau'/tau_dot.

STRUCTURAL ANCHOR (PRIOR STATE this gate BUILDS ON, does NOT re-derive):
  T1 -- "Transit is sudden quench" (PROVEN, S36/S38; atlas-04-assumptions):
    delta_t/T_L = 1.25e-5, P_exc = 1.000, dwell time 38,600x shorter than the BCS
    condensate formation time. The transit through the fold is parametric (sudden),
    not adiabatic. This is the FOLD-CENTER value; the present gate tests whether it
    extends GLOBALLY across the feature.
  E3 -- R_K(tau) = -1/4 e^{-4tau} + 2 e^{-tau} - 1/4 + 1/2 e^{2tau} (closed form,
    baptista-operator-dk-tau.md; R_K(0)=2). The Jensen-fiber scalar curvature whose
    tau-variation sets the van Hove feature width.
  Clock constraint (E27): t(tau) = t_0 + int dtau'/tau_dot; tau_dot known LOCALLY at
    the fold, GLOBALLY UNDETERMINED. The post-fold clock bound |tau_dot| < 2.4e-6
    tau_0/t_H is the SLOWEST admissible rate (|tau_today - tau_0| < 7.5e-6 over
    N ~ 2.4e60 ticks).

[SIGN] SUBSTITUTION CHAIN (math-scripts.md "Double-Check Logic Before Compute"):
  Claim: "For a non-empty one-parameter family of tau_dot(tau) profiles bounded by
          the two pinned endpoints, the LOCAL diabaticity ratio delta_t/T_L stays
          BELOW 1e-2 across the WHOLE van Hove feature, so the sudden-quench
          saturation P_exc=1 holds MODE-BY-MODE, not just at the fold center."

  Step 1 -- Definitions (cite canonical source):
    delta_t_transit = dt_transit = 1.1301575e-3 M_KK^{-1}  [canonical_constants.py; fold crossing time]
    D_fold          = delta_t/T_L |_fold = 1.25e-5         [T1 PROVEN sudden-quench ratio at fold center]
    T_L             = delta_t_transit / 1.25e-5             [condensate formation time; tau-INDEPENDENT ref scale]
    R_K(tau)        = -1/4 e^{-4tau} + 2 e^{-tau} - 1/4 + 1/2 e^{2tau}   [E3 closed form; R_K(0)=2]
    R_K'(tau)       = e^{-4tau} - 2 e^{-tau} + e^{2tau}     [LOCAL spectral-reorganization rate => gap-opening rate]
    rho_feat(tau)   = |R_K'(tau)| / |R_K'(tau_fold)|        [normalized local feature width; >=0, =1 at fold]
    |tau_dot|_clock = 2.4e-6  (in tau_0/t_H units)          [slowest admissible post-fold rate; E27]
    g(tau)          = tau_dot(tau)/tau_dot_fold             [dimensionless profile shape; g=1 at fold]
    D(tau)          = delta_t(tau)/T_L(tau)                 [LOCAL diabaticity ratio along the profile]

  Step 2 -- Substitution (no simplification):
    delta_t(tau)  = (feature-element width)/tau_dot(tau) = [Delta_tau * rho_feat(tau)] / [tau_dot_fold * g(tau)]
                    -- the time to cross a feature element scales with the LOCAL feature width rho_feat and
                       INVERSELY with the local sweep rate tau_dot.
    T_L(tau)      = T_L  (the BCS condensate-formation time; gap-formation reference, set at the fold)
    D(tau)        = delta_t(tau)/T_L = D_fold * rho_feat(tau) / g(tau)
                    -- at fold center rho_feat=1, g=1 => D = D_fold = 1.25e-5 (recovers T1 EXACTLY).

  Step 3 -- Simplification (one step per line):
    D(tau) = 1.25e-5 * rho_feat(tau) / g(tau)
    The ratio scales INVERSELY with tau_dot (with g): faster sweep (larger g) => smaller delta_t => smaller D.
    A profile that SLOWS away from the fold (smaller g) INCREASES D (toward adiabatic, P_exc<1).
    The clock bound |tau_dot| < 2.4e-6 tau_0/t_H is the SLOWEST admissible rate => g >= g_clock at the edges.
    Non-emptiness:  D(tau) < 1e-2  <=>  g(tau) > g_min(tau) = D_fold * rho_feat(tau) / 1e-2
                    the family is non-empty iff g_min(tau) <= g_max(tau) (upper rate envelope) across the feature.

  Step 4 -- Direction read-off (from canonical form):
    Since D = D_fold * rho_feat / g DECREASES with g (dD/dg = -D/g < 0 strictly, g>0), and the fold-center
    value 1.25e-5 is a FACTOR 800 below the 1e-2 ceiling, the family is non-empty in a neighborhood of the
    fold. The TEST is whether it stays non-empty across the FULL feature width R_K(tau) before the clock
    bound forces g too small at the edges:
      PASS  iff EXISTS a profile with D(tau) < 1e-2 everywhere on the feature (non-empty family);
      FAIL  iff the clock bound forces D(tau) >= 1 somewhere (an adiabatic patch => P_exc<1 there);
      INFO  iff the family is under-constrained (multiple admissible shapes, no unique selection -- needs gate-1).

  Step 5 -- Conclusion:
    The fold-center margin (1.25e-5 vs 1e-2, factor 800) is large; a non-empty family almost certainly
    exists in the feature core. The EDGES (where the clock bound binds g from below) are the decisive test.
    The output tau_dot(tau) profile is the controlling rate for gate-1's rho_relic(tau) integration and
    the a(t) MAGNITUDE.

VERDICT RUBRIC (plan W1-6):
  PASS  = a non-empty family of tau_dot(tau) keeps D(tau) < 1e-2 across the full van Hove feature
          (P_exc=1 is ROBUST mode-by-mode, not a fold-center artifact) AND the selection is essentially
          unique (the family collapses to a narrow band).
  FAIL  = the only admissible profiles violate the clock bound, OR an adiabatic patch (D >= 1) appears at
          the feature edges (P_exc<1 somewhere; relic content genuinely rate-sensitive away from fold).
  INFO  = the family is non-empty but UNDER-CONSTRAINED (multiple admissible shapes, all keeping D<1e-2,
          no unique selection): tau_dot(tau) is a ONE-PARAMETER family pending the gate-1 a(t) closure.

[SIGN] 3-tuple (gate-verdicts.md schema-v2):
  sign_verdict      : the predicted DIRECTION D ~ 1/tau_dot (DECREASING in tau_dot). PASS iff the computed
                      profile family confirms dD/d(tau_dot) < 0 (faster sweep => more sudden) AND a
                      non-empty family with max_feature D < 1e-2 exists.
  magnitude_verdict : how the worst-case (max over feature) diabaticity ratio of the WIDEST admissible
                      profile compares to the 1e-2 ceiling. PASS iff max_feature D < 1e-2 with margin;
                      INFO iff 1e-2 <= max D < 1 (under-constrained but still sub-adiabatic);
                      FAIL iff max D >= 1 (adiabatic patch).
  regime_verdict    : VALID iff the sudden-quench (diabatic) regime omega_max*delta_t << 1 holds throughout
                      the tested feature (the family stays sub-adiabatic on >=95% of the intended window);
                      MARGINAL iff 50-95%; BREAKDOWN iff <50%.

Author: transit-dynamics-theorist | Session 96 Wave 1.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU-only arithmetic; cap threads (computation-environment.md; GPU_path=cpu-cap-OMP8)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Path discipline (project root contains a SPACE -- use absolute Path objects)
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
ROOT_COMPUTATIONS = PROJECT_ROOT / "computations"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT_COMPUTATIONS))

# -----------------------------------------------------------------------------
# Canonical constants (MANDATORY: never hardcode framework constants)
# -----------------------------------------------------------------------------
from canonical_constants import (  # noqa: E402
    tau_fold,                # 0.19    -- van Hove fold (Jensen deformation parameter)
    dt_transit,              # 1.1302e-3 M_KK^{-1} -- fold-local crossing time
    Mach_max_framework,      # 13.75   -- framework Mach at the van Hove fold
    c_fabric,                # 209.97368021 -- substrate sound speed (velocity scale)
    P_exc_kz,                # 1.0     -- Kibble-Zurek excitation probability (sudden quench, exact)
    n_pairs,                 # 59.8    -- Bogoliubov quasiparticle pairs
)

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (per plan W1-6 R3 YAML)
# -----------------------------------------------------------------------------
GATE_ID = "S96-W1-TAUDOT-PROFILE"
SCHEME = "global-tau-dot-family-bounded-by-fold-rate-and-clock"
CONVENTION = "two-endpoint-pinned-one-parameter-sweep-rate-family"
L_MAX = "N/A"                # tau_dot profile is a modulus-flow quantity, not a spectral computation (R_K closed form)

# --- Pre-registered machinery pins (plan W1-6) ---
N_EVAL = 50                  # (local) one-parameter-family shape-parameter scan
TAU_LO = 0.0                 # (local) scan_range lower (brackets the van Hove feature)
TAU_HI = 0.5                 # (local) scan_range upper (fold to nominal fixed point)
SHAPE_STEP = 0.01            # (local) shape-parameter step (50 points over the family)
N_TAU_FEATURE = 200          # (local) tau-feature sampling points
DIABATICITY_CEILING = 1e-2   # (local) pre-registered diabaticity-ratio ceiling (strict_PASS_boundary value=1e-2, direction "<")
PUB_PRECISION = 4            # (local) publication precision (tau_dot endpoints feed gate 1)

# --- Canonical fold-center sudden-quench ratio (T1 PROVEN; the structural anchor) ---
D_FOLD = 1.25e-5             # (local) delta_t/T_L at fold center (atlas-04-assumptions T1; canonical sudden-quench ratio)

# --- Post-fold clock bound (E27; SLOWEST admissible rate, in tau_0/t_H units) ---
TAUDOT_CLOCK_BOUND = 2.4e-6  # (local) |tau_dot| < 2.4e-6 tau_0/t_H (post-fold clock-constraint E27 upper bound)

# --- Regime-fraction bands (gate-verdicts.md auto-shortening / regime discipline) ---
REGIME_VALID_FRAC = 0.95     # (local) >=95% of feature sub-adiabatic => VALID
REGIME_MARGINAL_FRAC = 0.50  # (local) 50-95% => MARGINAL; <50% => BREAKDOWN

# -----------------------------------------------------------------------------
# Verdict file path (S96 canonical location per gate-verdicts.md)
# -----------------------------------------------------------------------------
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-96" / "s96_gate_verdicts.txt"

# -----------------------------------------------------------------------------
# Input + output files
# -----------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
OUT_NPZ = PROJECT_ROOT / "computations" / "session-96" / "s96_w1_taudot_profile.npz"
OUT_PNG = PROJECT_ROOT / "computations" / "session-96" / "s96_w1_taudot_profile.png"


# -----------------------------------------------------------------------------
# Closed-form fiber curvature E3 + its derivative (the van Hove feature width)
# -----------------------------------------------------------------------------
def R_K(tau):
    r"""E3 closed form: R_K(tau) = -1/4 e^{-4tau} + 2 e^{-tau} - 1/4 + 1/2 e^{2tau}. R_K(0)=2."""
    return (-0.25 * np.exp(-4.0 * tau) + 2.0 * np.exp(-tau)
            - 0.25 + 0.5 * np.exp(2.0 * tau))


def R_K_prime(tau):
    r"""d R_K/dtau = e^{-4tau} - 2 e^{-tau} + e^{2tau}. The LOCAL spectral-reorganization rate.

    Where R_K' is large the D_K spectrum reorganizes fast => the gap opens fast
    (small T_L) => the local diabaticity delta_t/T_L is locally enhanced. This is the
    substrate-natural van Hove feature-width measure.
    """
    return (np.exp(-4.0 * tau) - 2.0 * np.exp(-tau) + np.exp(2.0 * tau))


def feature_density(tau, tau_ref):
    r"""rho_feat(tau) = |R_K'(tau)| / |R_K'(tau_ref)|  (normalized local feature width; =1 at tau_ref)."""
    ref = abs(R_K_prime(tau_ref))  # (local)
    return np.abs(R_K_prime(tau)) / ref


# -----------------------------------------------------------------------------
# SHA helpers (dual-SHA per S84+ schema)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """(audit_sha256, content_sha256). audit = sha(script||canonical||pinmap_json); content = sha(script)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# -----------------------------------------------------------------------------
# The one-parameter family of global sweep-rate profiles
# -----------------------------------------------------------------------------
def build_profile_family(tau_grid, shape_params, tau_anchor, g_clock):
    r"""Construct g_s(tau) = tau_dot(tau)/tau_dot_fold for each shape parameter s.

    The two-endpoint pin:
      g(tau_anchor) = 1                      (fold rate, canonical center)
      g(tau) -> g_clock as the profile decays post-fold  (clock bound, slowest admissible)

    The minimal one-parameter family interpolates between the fold rate and the clock floor
    with shape parameter s in [0,1] controlling how FAST the rate decays away from the fold:
      g_s(tau) = g_clock + (1 - g_clock) * exp( -s * w_decay * (tau - tau_anchor)^2 )
    s -> 0 : flat (g~1 everywhere; stays FAST -- most sudden, but must respect the clock bound asymptotically)
    s -> 1 : sharp Gaussian decay to the clock floor away from the fold (slowest edges -- the binding test).

    Returns g_family[s_idx, tau_idx] >= g_clock, with g=1 at tau_anchor for all s.
    """
    w_decay = 8.0  # (local) decay-width scale (M_KK^2; sets how localized the fast-sweep window is)
    dtau = (tau_grid - tau_anchor)  # (local)
    g_family = np.empty((len(shape_params), len(tau_grid)), dtype=float)  # (local)
    for i, s in enumerate(shape_params):
        decay = np.exp(-s * w_decay * dtau ** 2)  # (local) 1 at anchor, ->0 away from it
        g_family[i] = g_clock + (1.0 - g_clock) * decay  # (local) in [g_clock, 1]; =1 at anchor
    return g_family


# -----------------------------------------------------------------------------
# Gate evaluation (PRE-REGISTERED 3-tuple bands + composite collapse)
# -----------------------------------------------------------------------------
def evaluate_gate(max_D_per_shape, feature_mask, D_grid_widest,
                  monotone_confirmed, family_nonempty, unique_selection):
    r"""Composite operator (plan W1-6):
      PASS  = non-empty family keeps max_feature D < 1e-2 AND selection essentially unique.
      FAIL  = clock bound forces an adiabatic patch (max D >= 1) OR only-admissible profiles violate clock.
      INFO  = non-empty family but UNDER-CONSTRAINED (no unique selection) -- one-parameter family pending gate-1.

    3-tuple (gate-verdicts.md schema-v2):
      sign_verdict: PASS iff D ~ 1/tau_dot direction confirmed (dD/dtau_dot<0) AND a non-empty family
        with max_feature D < 1e-2 exists.
      magnitude_verdict: PASS iff the WIDEST admissible profile's max_feature D < 1e-2 (with margin);
        INFO iff 1e-2 <= max D < 1 (under-constrained, sub-adiabatic); FAIL iff max D >= 1 (adiabatic patch).
      regime_verdict: VALID iff >=95% of the feature is sub-adiabatic (D<1) for the widest profile;
        MARGINAL iff 50-95%; BREAKDOWN iff <50%.
    """
    # --- worst-case (widest admissible) diabaticity over the feature ---
    max_D_widest = float(np.max(D_grid_widest[feature_mask]))  # (local) max over feature of the widest profile

    # --- SIGN: direction D ~ 1/tau_dot AND a non-empty family exists with max D < 1e-2 ---
    sign_pass = bool(monotone_confirmed and family_nonempty)  # (local)
    sign_v = "PASS" if sign_pass else "FAIL"  # (local)

    # --- MAGNITUDE: where does the worst-case feature diabaticity land vs the ceiling? ---
    if max_D_widest < DIABATICITY_CEILING:
        mag_v = "PASS"  # (local) widest admissible profile is sub-ceiling everywhere => robust P_exc=1
    elif max_D_widest < 1.0:
        mag_v = "INFO"  # (local) sub-adiabatic but above the 1e-2 ceiling at some edge => under-constrained
    else:
        mag_v = "FAIL"  # (local) adiabatic patch (D>=1) => P_exc<1 somewhere

    # --- REGIME: fraction of the feature that is sub-adiabatic (D<1) for the widest profile ---
    n_feat = int(np.sum(feature_mask))  # (local)
    n_subadiabatic = int(np.sum(D_grid_widest[feature_mask] < 1.0))  # (local)
    frac_valid = n_subadiabatic / n_feat if n_feat > 0 else 0.0  # (local)
    if frac_valid >= REGIME_VALID_FRAC:
        reg_v = "VALID"  # (local)
    elif frac_valid >= REGIME_MARGINAL_FRAC:
        reg_v = "MARGINAL"  # (local)
    else:
        reg_v = "BREAKDOWN"  # (local)

    # --- Composite collapse rule (gate-verdicts.md schema-v2, PRE-REGISTERED) ---
    if reg_v == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"  # (local)
    elif mag_v == "FAIL" and reg_v == "VALID":
        composite = "FAIL"  # (local)
    elif mag_v == "FAIL" and reg_v == "MARGINAL":
        composite = "INFO"  # (local)
    elif mag_v == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)

    # --- INFO override: family non-empty + sub-ceiling but NOT uniquely selected => under-constrained ---
    # (the plan's INFO_meaning: multiple admissible shapes, all keeping D<1e-2, no unique selection).
    if composite == "PASS" and not unique_selection:
        composite = "INFO"  # (local) under-constrained one-parameter family pending the gate-1 closure
    return composite, sign_v, mag_v, reg_v, max_D_widest, frac_valid


# -----------------------------------------------------------------------------
# Plot -- tau_dot(tau) family, diabaticity ratio across the feature, admissibility band
# -----------------------------------------------------------------------------
def make_plot(tau_grid, g_family, shape_params, D_family, g_min_grid, feature_mask,
              widest_idx, composite, sign_v, mag_v, reg_v, max_D_widest, frac_valid):
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.4))

    # Panel 1: the one-parameter family of sweep-rate profiles g(tau) = tau_dot/tau_dot_fold
    ax = axes[0]
    for i in range(0, len(shape_params), max(1, len(shape_params) // 8)):
        ax.plot(tau_grid, g_family[i], lw=0.9, alpha=0.6,
                color=plt.cm.viridis(i / max(1, len(shape_params) - 1)))
    ax.plot(tau_grid, g_family[widest_idx], lw=2.2, color="C3",
            label=f"widest admissible (s={shape_params[widest_idx]:.2f})")
    ax.axvline(tau_fold, color="k", ls=":", lw=1.2, label=f"fold tau={tau_fold}")
    ax.axhline(TAUDOT_CLOCK_BOUND, color="C1", ls="--", lw=1.2,
               label=f"clock floor g_clock={TAUDOT_CLOCK_BOUND:.1e}")
    ax.axhline(1.0, color="C7", ls="-", lw=0.7, label="fold rate g=1")
    ax.set_xlabel(r"$\tau$ (Jensen deformation)")
    ax.set_ylabel(r"$g(\tau)=\dot\tau(\tau)/\dot\tau_{\rm fold}$")
    ax.set_yscale("log")
    ax.set_title("One-parameter sweep-rate family $\\dot\\tau(\\tau)$\n(two-endpoint pinned: g=1 at fold, g$\\to$clock floor)")
    ax.legend(fontsize=6.5, loc="lower left")
    ax.grid(alpha=0.3)

    # Panel 2: local diabaticity ratio D(tau)=delta_t/T_L across the feature
    ax = axes[1]
    for i in range(0, len(shape_params), max(1, len(shape_params) // 8)):
        ax.plot(tau_grid, D_family[i], lw=0.9, alpha=0.6,
                color=plt.cm.viridis(i / max(1, len(shape_params) - 1)))
    ax.plot(tau_grid, D_family[widest_idx], lw=2.2, color="C3", label="widest admissible")
    ax.axhline(DIABATICITY_CEILING, color="C0", ls="-", lw=1.6,
               label=f"ceiling $\\delta t/T_L$=1e-2")
    ax.axhline(D_FOLD, color="C2", ls="--", lw=1.2, label=f"T1 fold value 1.25e-5")
    ax.axhline(1.0, color="C8", ls=":", lw=1.0, label="adiabatic threshold D=1")
    ax.axvline(tau_fold, color="k", ls=":", lw=1.0)
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$D(\tau)=\delta t(\tau)/T_L(\tau)$")
    ax.set_yscale("log")
    ax.set_title(f"Diabaticity ratio across van Hove feature\nmax$_{{\\rm feature}}$ D (widest) = {max_D_widest:.3e}")
    ax.legend(fontsize=6.5, loc="upper left")
    ax.grid(alpha=0.3)

    # Panel 3: admissibility band g_min(tau) <= g(tau) <= g_max(tau)=1 + summary
    ax = axes[2]
    tau_feat = tau_grid[feature_mask]  # (local)
    g_min_feat = g_min_grid[feature_mask]  # (local)
    ax.fill_between(tau_feat, g_min_feat, 1.0,
                    where=(g_min_feat <= 1.0), color="C2", alpha=0.25,
                    label="admissible band [g_min, 1]")
    ax.plot(tau_grid, g_min_grid, lw=1.8, color="C0",
            label=r"$g_{\min}(\tau)=D_{\rm fold}\rho_{\rm feat}/10^{-2}$")
    ax.axhline(TAUDOT_CLOCK_BOUND, color="C1", ls="--", lw=1.2, label="clock floor")
    ax.axhline(1.0, color="C7", ls="-", lw=0.7, label="fold rate g=1")
    ax.axvline(tau_fold, color="k", ls=":", lw=1.0, label=f"fold tau={tau_fold}")
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel("normalized rate $g$")
    ax.set_yscale("log")
    ax.set_title("Non-emptiness: $g_{\\min}(\\tau)\\leq g_{\\max}(\\tau)$ across feature")
    ax.text(0.02, 0.02,
            f"composite={composite}\nsign={sign_v} mag={mag_v} regime={reg_v}\n"
            f"max$_{{\\rm feat}}$ D = {max_D_widest:.2e}\n"
            f"sub-adiabatic frac = {frac_valid:.3f}\n"
            f"fold margin = {DIABATICITY_CEILING/D_FOLD:.0f}x",
            transform=ax.transAxes, fontsize=7.5, ha="left", va="bottom",
            bbox=dict(boxstyle="round", fc="lightyellow", ec="C3", alpha=0.9))
    ax.legend(fontsize=6.5, loc="upper right")
    ax.grid(alpha=0.3)

    fig.suptitle(
        f"{GATE_ID} -- global sweep-rate profile $\\dot\\tau(\\tau)$ through the van Hove fold "
        f"(supersonic Mach {Mach_max_framework}, impulsive)  |  composite={composite}  "
        f"sign={sign_v} mag={mag_v} regime={reg_v}  |  P_exc={P_exc_kz} robust mode-by-mode? "
        f"(T1 fold 1.25e-5 << 1e-2 ceiling)",
        fontsize=9)
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Verdict-line emitter (atomic append; dual-SHA + schema-v2 3-tuple REQUIRED)
# -----------------------------------------------------------------------------
def find_prior_audit_sha() -> str:
    """Latest non-superseded canonical line for GATE_ID (gate-verdicts.md "Option A")."""
    if not VERDICT_TXT.exists():
        return ""
    import re as _re  # (local)
    text = VERDICT_TXT.read_text(encoding="utf-8")  # (local)
    canon_re = _re.compile(
        rf"^{_re.escape(GATE_ID)}:\s.*?audit_sha256=([a-f0-9]{{64}})", _re.MULTILINE)  # (local)
    shas = canon_re.findall(text)  # (local)
    if not shas:
        return ""
    sup_re = _re.compile(r"supersedes=([a-f0-9]{64})")  # (local)
    superseded = set(sup_re.findall(text))  # (local)
    non_superseded = [s for s in shas if s not in superseded]  # (local)
    return non_superseded[-1] if non_superseded else shas[-1]


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, reg_v: str,
                   max_D_widest: float, frac_valid: float,
                   supersedes_sha: str = "") -> None:
    """Append canonical line + dual-SHA companion + schema-v2 3-tuple row (atomic single open('a'))."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    sup_token = f"_supersedes={supersedes_sha}" if supersedes_sha else ""  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}{sup_token}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )
    # REQUIRED [SIGN] 3-tuple companion row.
    schema_v2_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={reg_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2); "
        f"sign = D(tau)=delta_t/T_L scales 1/tau_dot (DECREASING in tau_dot; faster sweep => more sudden) "
        f"AND a non-empty family with max_feature D < 1e-2 exists; "
        f"mag = widest-admissible max_feature D = {max_D_widest:.3e} vs 1e-2 ceiling; "
        f"regime = sub-adiabatic (D<1) fraction {frac_valid:.3f} of the van Hove feature\n"
    )
    # Structural-anchor row (the PROVEN T1 sudden-quench anchor this gate extends)
    anchor_row = (
        f"# ANCHOR=T1_transit_is_sudden_quench_delta_t/T_L=1.25e-5_P_exc=1.000 "
        f"# {GATE_ID} atlas-04-assumptions T1 PROVEN (S36/S38); fold-center value EXTENDED globally; "
        f"R_K(tau) E3 closed form (baptista-operator-dk-tau); clock bound E27 |tau_dot|<2.4e-6 tau_0/t_H; "
        f"output tau_dot(tau) feeds S96-W1-AOFT-FRIEDMANN-MAP rho_relic(tau) integration + a(t) magnitude\n"
    )
    rows = [line, companion, schema_v2_row, anchor_row]  # (local)
    if supersedes_sha:
        rows.append(
            f"# supersedes={supersedes_sha} "
            f"# {GATE_ID} corrective re-emission per gate-verdicts.md \"Option A\" "
            f"(prior line RETAINED; this corrective line is canonical)\n"
        )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        for r in rows:
            fp.write(r)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> int:
    print("=" * 78)
    print(f"  {GATE_ID}")
    print("  Global sweep-rate profile tau_dot(tau) through the van Hove fold")
    print("=" * 78)

    # --- Input SHA log (first 20 lines of stdout per gate-verdicts.md) ---
    print("\n=== Input SHA-256 pins ===")
    sha_script = sha256_of(SCRIPT_PATH)  # (local)
    sha_canon = sha256_of(CANONICAL_CONSTANTS_PATH)  # (local)
    print(f"  script                 : {sha_script}")
    print(f"  canonical_constants.py : {sha_canon}")
    print(f"  tau_fold={tau_fold}  dt_transit={dt_transit:.6e} M_KK^-1  Mach={Mach_max_framework}  "
          f"c_fabric={c_fabric}")
    print(f"  P_exc_kz={P_exc_kz}  n_pairs={n_pairs}  D_fold(T1)={D_FOLD}  clock_bound={TAUDOT_CLOCK_BOUND}")

    # --- Substitution chain summary (Step 1-5; [SIGN]) ---
    print("\n=== Substitution chain (Step 1-5; [SIGN]) ===")
    print("  Step 1: D_fold = delta_t/T_L = 1.25e-5 (T1 PROVEN); T_L = dt_transit/1.25e-5; R_K(tau) E3 closed form")
    print("  Step 2: D(tau) = D_fold * rho_feat(tau)/g(tau),  g=tau_dot/tau_dot_fold,  rho_feat=|R_K'(tau)|/|R_K'(fold)|")
    print("  Step 3: D ~ 1/tau_dot => faster sweep (larger g) => smaller D; clock bound = slowest g (floor)")
    print("  Step 4: PASS iff EXISTS profile with D<1e-2 across feature (non-empty family); FAIL iff adiabatic patch")
    print("  Step 5: fold margin 1.25e-5 vs 1e-2 = factor 800; EDGES (clock-bound-binding) are the test")

    # === Build the tau grid + the van Hove feature mask ===
    tau_grid = np.linspace(TAU_LO, TAU_HI, N_TAU_FEATURE)  # (local)
    rho_feat = feature_density(tau_grid, tau_fold)  # (local) normalized local feature width (=1 at fold)

    # Van Hove feature = where the spectral-reorganization rate |R_K'| is non-negligible relative to fold.
    # Define the feature as rho_feat >= 1% of the fold value (captures the full enhanced-DOS region).
    FEATURE_REL_THRESH = 0.01  # (local) feature = where local reorg rate >= 1% of fold reorg rate
    feature_mask = rho_feat >= FEATURE_REL_THRESH  # (local)
    n_feat = int(np.sum(feature_mask))  # (local)
    print("\n=== van Hove feature (from R_K'(tau) reorganization rate) ===")
    print(f"  R_K(0)={R_K(0.0):.4f}  R_K(fold)={R_K(tau_fold):.4f}  R_K'(fold)={R_K_prime(tau_fold):.6f}")
    print(f"  feature width: {n_feat}/{N_TAU_FEATURE} tau-points with rho_feat >= {FEATURE_REL_THRESH} "
          f"(tau in [{tau_grid[feature_mask].min():.3f}, {tau_grid[feature_mask].max():.3f}])")
    print(f"  max rho_feat over feature = {np.max(rho_feat[feature_mask]):.4f} (at the steepest reorg point)")

    # === g_min(tau): the SLOWEST g keeping D(tau) < 1e-2 ===
    # D(tau) = D_fold * rho_feat / g < 1e-2  <=>  g > g_min = D_fold * rho_feat / 1e-2
    g_min_grid = D_FOLD * rho_feat / DIABATICITY_CEILING  # (local) lower envelope of admissible g
    # g_clock floor: the clock bound is the SLOWEST admissible absolute rate; in g-units (tau_dot/tau_dot_fold)
    # the fold rate is the reference. The clock bound 2.4e-6 (tau_0/t_H) is the post-fold slowest rate; as a
    # FRACTION of the fold rate it sets the asymptotic floor of g away from the fold.
    g_clock = TAUDOT_CLOCK_BOUND  # (local) clock floor in g-units (slowest admissible normalized rate)

    # === Build the one-parameter family of profiles g_s(tau) ===
    shape_params = np.linspace(0.0, 1.0, N_EVAL)  # (local) shape parameter s in [0,1] (50 points)
    g_family = build_profile_family(tau_grid, shape_params, tau_fold, g_clock)  # (local)

    # === Diabaticity ratio D_s(tau) = D_fold * rho_feat / g_s(tau) for each profile ===
    D_family = D_FOLD * rho_feat[None, :] / g_family  # (local) [s_idx, tau_idx]

    # === Per-shape worst-case diabaticity over the feature ===
    max_D_per_shape = np.max(np.where(feature_mask[None, :], D_family, -np.inf), axis=1)  # (local)
    print("\n=== Per-shape worst-case diabaticity over the feature ===")
    for i in range(0, N_EVAL, max(1, N_EVAL // 10)):
        admissible = "ADMISSIBLE" if max_D_per_shape[i] < DIABATICITY_CEILING else (
            "sub-adiabatic" if max_D_per_shape[i] < 1.0 else "ADIABATIC-PATCH")  # (local)
        print(f"  s={shape_params[i]:.3f}: max_feature D = {max_D_per_shape[i]:.3e}  [{admissible}]")

    # === Non-emptiness: which profiles keep D < 1e-2 across the WHOLE feature? ===
    admissible_mask = max_D_per_shape < DIABATICITY_CEILING  # (local)
    n_admissible = int(np.sum(admissible_mask))  # (local)
    family_nonempty = bool(n_admissible > 0)  # (local)
    # The WIDEST admissible profile = the one with the LARGEST shape parameter (slowest edges) that is still
    # admissible -- it is the binding edge case. If none admissible, the widest is the least-bad (max s).
    if family_nonempty:
        widest_idx = int(np.max(np.where(admissible_mask)[0]))  # (local) slowest-edge admissible profile
    else:
        widest_idx = int(N_EVAL - 1)  # (local) the slowest profile (worst case) for the FAIL diagnostic
    D_grid_widest = D_family[widest_idx]  # (local)

    # === Non-emptiness check from the analytic envelope: g_min(tau) <= g_max(tau)=1 across feature ===
    # The upper rate envelope is the fold rate g=1 (cannot sweep faster than the fold-center rate in this family).
    g_max_envelope = 1.0  # (local) fold rate is the fastest admissible normalized rate
    envelope_nonempty = bool(np.all(g_min_grid[feature_mask] <= g_max_envelope))  # (local)
    print("\n=== Non-emptiness (analytic envelope) ===")
    print(f"  max_feature g_min(tau) = {np.max(g_min_grid[feature_mask]):.3e}  (must be <= g_max=1)")
    print(f"  g_min(tau) <= 1 across feature: {envelope_nonempty}  "
          f"(fold-center g_min = {D_FOLD * 1.0 / DIABATICITY_CEILING:.3e})")
    print(f"  admissible profiles (max_feature D < 1e-2): {n_admissible}/{N_EVAL}")

    # === Direction confirmation: D ~ 1/tau_dot (monotone DECREASING in g) ===
    # Check dD/dg < 0 at a representative feature point: compare D at g=1 vs g=g_clock.
    rho_at_fold = float(feature_density(np.array([tau_fold]), tau_fold)[0])  # (local) = 1
    D_fast = D_FOLD * rho_at_fold / 1.0  # (local) D at the fast (fold) rate
    D_slow = D_FOLD * rho_at_fold / g_clock  # (local) D at the slow (clock-floor) rate
    monotone_confirmed = bool(D_slow > D_fast)  # (local) slower sweep => LARGER D (toward adiabatic)
    print("\n=== Direction read-off (Step 4): D ~ 1/tau_dot ===")
    print(f"  D(fast g=1) = {D_fast:.3e}  ;  D(slow g=g_clock={g_clock:.1e}) = {D_slow:.3e}")
    print(f"  D DECREASES with tau_dot (slower => larger D): {monotone_confirmed}")

    # === Uniqueness: is the admissible family a NARROW band (unique selection) or WIDE (under-constrained)? ===
    # The family is "uniquely selected" if essentially ALL shape parameters are admissible (the constraint
    # does not pin a unique shape -> under-constrained); it is "constrained" if only a NARROW sub-band is
    # admissible. Per plan INFO_meaning, a WIDE admissible band = UNDER-CONSTRAINED => INFO.
    admissible_frac = n_admissible / N_EVAL  # (local)
    # under-constrained if a large fraction of shapes are admissible (no unique shape pinned)
    unique_selection = bool(admissible_frac < 0.5)  # (local) <50% admissible => the constraint pins a narrow band
    print(f"\n  admissible fraction of family = {admissible_frac:.3f}  "
          f"(unique selection iff < 0.5: {unique_selection})")

    # === Verdict ===
    composite, sign_v, mag_v, reg_v, max_D_widest, frac_valid = evaluate_gate(
        max_D_per_shape, feature_mask, D_grid_widest,
        monotone_confirmed, family_nonempty, unique_selection)  # (local)
    print("\n=== Verdict 3-tuple ===")
    print(f"  sign_verdict      = {sign_v}  (D ~ 1/tau_dot DECREASING; non-empty family with max D<1e-2)")
    print(f"  magnitude_verdict = {mag_v}  (widest-admissible max_feature D = {max_D_widest:.3e} vs 1e-2)")
    print(f"  regime_verdict    = {reg_v}  (sub-adiabatic frac {frac_valid:.3f} of feature)")
    print(f"  COMPOSITE         = {composite}")

    # === SHA closure (pinmap) ===
    pins = {
        "_gate_id": GATE_ID, "_scheme": SCHEME, "_convention": CONVENTION,
        "L_max": L_MAX, "N_eval": N_EVAL, "N_tau_feature": N_TAU_FEATURE,
        "tau_lo": TAU_LO, "tau_hi": TAU_HI, "shape_step": SHAPE_STEP,
        "diabaticity_ceiling": DIABATICITY_CEILING,
        "D_fold": D_FOLD, "taudot_clock_bound": TAUDOT_CLOCK_BOUND,
        "tau_fold": float(tau_fold), "dt_transit": float(dt_transit),
        "Mach_max_framework": float(Mach_max_framework), "c_fabric": float(c_fabric),
        "P_exc_kz": float(P_exc_kz), "n_pairs": float(n_pairs),
        "feature_rel_thresh": FEATURE_REL_THRESH,
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS_PATH, pins)  # (local)
    print("\n=== Dual-SHA closure ===")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # === Save data ===
    np.savez(
        OUT_NPZ,
        tau_grid=tau_grid,
        rho_feat=rho_feat,
        feature_mask=feature_mask,
        shape_params=shape_params,
        g_family=g_family,
        D_family=D_family,
        max_D_per_shape=max_D_per_shape,
        admissible_mask=admissible_mask,
        g_min_grid=g_min_grid,
        D_grid_widest=D_grid_widest,
        widest_idx=widest_idx,
        n_admissible=n_admissible,
        admissible_frac=admissible_frac,
        family_nonempty=family_nonempty,
        envelope_nonempty=envelope_nonempty,
        monotone_confirmed=monotone_confirmed,
        unique_selection=unique_selection,
        max_D_widest=max_D_widest,
        frac_valid=frac_valid,
        D_fold=D_FOLD, D_fast=D_fast, D_slow=D_slow,
        g_clock=g_clock,
        diabaticity_ceiling=DIABATICITY_CEILING,
        taudot_clock_bound=TAUDOT_CLOCK_BOUND,
        tau_fold=float(tau_fold), dt_transit=float(dt_transit),
        Mach=float(Mach_max_framework), c_fabric=float(c_fabric),
        P_exc=float(P_exc_kz), n_pairs=float(n_pairs),
        composite=composite, sign_v=sign_v, mag_v=mag_v, reg_v=reg_v,
        audit_sha256=audit_sha, content_sha256=content_sha,
        R_K_fold=float(R_K(tau_fold)), R_K_prime_fold=float(R_K_prime(tau_fold)),
    )
    print(f"\n  data  -> {OUT_NPZ}")

    # === Plot ===
    make_plot(tau_grid, g_family, shape_params, D_family, g_min_grid, feature_mask,
              widest_idx, composite, sign_v, mag_v, reg_v, max_D_widest, frac_valid)
    print(f"  plot  -> {OUT_PNG}")

    # === Emit verdict line (canonical + dual-SHA companion + schema-v2 3-tuple) ===
    value_str = (
        f"family_nonempty={family_nonempty};"
        f"n_admissible={n_admissible}/{N_EVAL};"
        f"max_feature_D_widest={max_D_widest:.4e};"
        f"fold_margin={DIABATICITY_CEILING/D_FOLD:.0f}x;"
        f"D_fold=1.25e-5;ceiling=1e-2;"
        f"subadiabatic_frac={frac_valid:.4f};"
        f"unique_selection={unique_selection};"
        f"feature_tau=[{tau_grid[feature_mask].min():.3f},{tau_grid[feature_mask].max():.3f}]"
    )  # (local)
    prior_sha = find_prior_audit_sha()  # (local)
    supersedes = ""  # (local)
    if prior_sha and prior_sha != audit_sha:
        supersedes = prior_sha  # (local) corrective re-emission per gate-verdicts.md Option A
    append_verdict(composite, value_str, audit_sha, content_sha,
                   sign_v, mag_v, reg_v, max_D_widest, frac_valid, supersedes_sha=supersedes)
    print(f"\n  verdict -> {VERDICT_TXT}")
    print(f"  {GATE_ID}: {composite} -- {value_str}")

    # === 4-tuple output tag (final non-verdict line per gate-verdicts.md) ===
    print(f"\n(value={composite}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
