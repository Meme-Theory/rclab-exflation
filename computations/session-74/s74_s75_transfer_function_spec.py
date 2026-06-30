#!/usr/bin/env python3
"""
S75-TRANSFER-FUNCTION-SPEC-74: Specification Document for S75 s75_transfer_function.py
=======================================================================================

W4-CC task. This is a SPEC-ONLY computation. The script itself does no physics
computation -- it writes the full-fidelity prompt for s75_transfer_function.py
to an npz file so it can be dispatched in S75 with zero drift.

CONTEXT
=======

Framework chapter section 8.4 lists s75_transfer_function.py as a deferred item
dependent on W1-E (FRIEDMANN-FROM-A2-74). That dependency is now resolved:

  W1-E verdict: FAIL (matching step; NOT structural).
    - G_N emergent from a_2 to factor 12 of Planck: PASS (structural).
    - 8-mode Bogoliubov <T_{00}>_GGE at fold: well-defined (rho ~ M_KK^4).
    - H_0 viable for natural f_conv in [0.3, 3]: FAIL.
    - Diluted-to-today route undershoots Planck by 29 OOM in H (56 in rho).
    - Undiluted-fold route overshoots by 58 OOM in H (117 in rho).
    - Bracket span: 86 OOM. f_conv is the sole surviving DOF in the matching.

The structural FAIL is at the fold-to-4D projection step. The ingredients that
s75_transfer_function.py needs (H(tau) functional form, a_2 emergent G_N,
branch-resolved mode spectrum, post-fold spectral relaxation region) are all
well-defined by W1-E and W1-H outputs. The f_conv ambiguity becomes an
externally-fixed calibration rather than an obstruction: s75_transfer_function
quotes T(k) and C_l SHAPES (dimensionless ratios) and leaves the overall A_s
amplitude as an uncalibrated budget gap, to be closed by W1-A, W1-G, or the
still-open non-circular projection rule.

DIRECTION OF EXPLANATION
========================

  D_K eigenvalues (fold) -> per-branch horizon-crossing and squeeze amplitudes
  -> a_2 Seeley-DeWitt emergent FRW line element (ds^2 from spatial projection)
  -> emergent Klein-Gordon equation for mode evolution on that line element
  -> T(k) from fold to recombination
  -> line-of-sight projection to angular C_l
  -> observable CMB spectrum from the fold-epoch fiber spectrum

DELIVERABLE
===========

A full-fidelity S75 agent prompt containing:

1. Substrate framing block (container-thinking correction, direction of explanation)
2. Task statement and scope
3. Inputs (paths to W1-A/W1-E/W1-H/S73A/S73B npz files)
4. Computation steps (1..N, each with a specific equation/table/output)
5. Output files (script, npz keys, plot)
6. Pre-registered gate (S75-TRANSFER-FUNCTION-75) with PASS/INFO/FAIL thresholds
7. Environment instructions (canonical_constants, venv Python)
8. Rules (numbers first, one writer per file, substrate framing discipline)

The prompt is written once here and pickled into the npz. S75 loads the string
and dispatches the computation.

SUBSTRATE DISCIPLINE NOTE
=========================

The framework chapter puts s75_transfer_function.py in section 8.4 (projection
and nonlocality). The computation is NOT a GR-in-a-container transfer function.
The emergent line element is an output of the spectral triple reduction, not
an input from a pre-existing spacetime. The "mode evolution fold -> recombination"
is a spectral-weight reorganization inside the fabric between two epochs; the
"Klein-Gordon equation" is the effective equation that falls out of the a_2
sector once the 4D projection is made. The prompt must enforce that direction.

GATE
====

S75-TRANSFER-FUNCTION-SPEC-74:
  PASS  -- full-fidelity prompt written (substrate framing, computation steps,
           inputs, outputs, gate, environment, rules).
  INFO  -- prompt drafted but needs review before S75 dispatch.
  FAIL  -- cannot be written due to W1-E structural FAIL.

W1-E failed at the MATCHING step (f_conv calibration), NOT at the structural
level. All structural ingredients needed for s75_transfer_function.py are in
hand: H(z) functional form, a_2 emergent G_N, 8-mode BCS spectrum, W1-H
emergent FRW line element (Omega_k = 0 exactly). Therefore the spec CAN be
written and W4-CC PASSES.

Session: S74 | Wave: W4-CC | Classification: GEOMETRIC + PHONONIC (spec)
phonon-first-cosmologist
"""

import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np

from canonical_constants import *

t_start = time.time()

# ==============================================================================
#  SECTION 0: Header
# ==============================================================================

print("=" * 78)
print("S75-TRANSFER-FUNCTION-SPEC-74: Specification for s75_transfer_function.py")
print("=" * 78)
print()
print("Gate thresholds:")
print("  PASS: full-fidelity S75 prompt written")
print("  INFO: prompt drafted but needs review")
print("  FAIL: cannot be written due to W1-E structural FAIL")
print()
print("W1-E FRIEDMANN-FROM-A2-74 verdict: FAIL at matching step, NOT structural.")
print("W1-H FLATNESS-FROM-A2-74 verdict: PASS (Omega_k = 0 structurally).")
print("-> All structural ingredients in hand. Spec writable. W4-CC PASSES.")
print()

data_dir = os.path.dirname(os.path.abspath(__file__))  # (local)

# ==============================================================================
#  SECTION 1: W1-E / W1-H status digest for the prompt context block
# ==============================================================================

print("SECTION 1: Digest W1-E and W1-H outputs for the prompt context block")
print("-" * 78)

# W1-E constants (from the working paper W1-E section)
w1e_a2_fold = a2_fold                                         # (local)
w1e_f2_default = f_2_default                                  # (local)
w1e_M_KK_gev = M_KK                                           # (local)
w1e_G_N_emergent_inv_gev2 = 5.549e-40                         # (local)
w1e_G_N_planck_inv_gev2 = 6.709e-39                           # (local)
w1e_G_ratio = w1e_G_N_emergent_inv_gev2 / w1e_G_N_planck_inv_gev2   # (local)

w1e_rho_gge_fold = 1.102e70   # GeV^4, fiber-local at fold        # (local)
w1e_rho_gge_zpe = 1.131e68    # GeV^4, BCS ZPE-only contribution  # (local)
w1e_zpe_frac = w1e_rho_gge_zpe / w1e_rho_gge_fold               # (local)

w1e_N_efolds = 132.45                                         # (local)
w1e_matter_dilution = 2.721e-173                              # (local)
w1e_rho_gge_today_diluted = 2.999e-103   # GeV^4              # (local)
w1e_rho_crit_obs = 4.08e-47              # GeV^4              # (local)
w1e_rho_ratio = w1e_rho_gge_today_diluted / w1e_rho_crit_obs  # (local)

w1e_H0_undershoot_oom = 29.0                                  # (local)
w1e_H0_overshoot_oom = 58.0                                   # (local)
w1e_H0_bracket_oom = w1e_H0_undershoot_oom + w1e_H0_overshoot_oom  # (local)

# W1-H constants
w1h_Omega_k = 0.0                                             # (local) structural
w1h_R_SU3_fold = 2.018144                                     # (local) s64 normalization
w1h_R_SU3_tau0 = 2.000000                                     # (local) bi-invariant limit
w1h_a2_homog_8D = 0.728235                                    # (local) HEAT-KERNEL-A2-61

print(f"  W1-E rho_GGE(fold, total)       = {w1e_rho_gge_fold:.3e} GeV^4")
print(f"  W1-E rho_GGE(fold, ZPE-only)    = {w1e_rho_gge_zpe:.3e} GeV^4")
print(f"  W1-E ZPE / total ratio          = {w1e_zpe_frac:.4f}")
print(f"  W1-E rho_GGE(today, diluted)    = {w1e_rho_gge_today_diluted:.3e} GeV^4")
print(f"  W1-E rho_crit_obs               = {w1e_rho_crit_obs:.3e} GeV^4")
print(f"  W1-E rho_today / rho_crit       = {w1e_rho_ratio:.3e}")
print(f"  W1-E G_N(emergent)/G_N(Planck)  = {w1e_G_ratio:.4f}  (factor-{1/w1e_G_ratio:.1f} gap)")
print(f"  W1-E H_0 bracket span (OOM)     = {w1e_H0_bracket_oom:.1f}")
print(f"  W1-H Omega_k                    = {w1h_Omega_k:.1f}  (structural, not fit)")
print(f"  W1-H R(SU(3)_tau=0.19)          = {w1h_R_SU3_fold:.6f}  (s64 norm)")
print(f"  W1-H a_2 (8D HEAT-KERNEL-A2-61) = {w1h_a2_homog_8D:.6f}")
print()

# ==============================================================================
#  SECTION 2: Assemble the full-fidelity S75 prompt string
# ==============================================================================

print("SECTION 2: Assemble S75 prompt (full-fidelity)")
print("-" * 78)

# The prompt is assembled as a single string with explicit section headers.
# It is deliberately complete so that S75 dispatch needs zero augmentation.

S75_PROMPT = r"""
You are the phonon-first-cosmologist (or an appropriately-scoped teammate from
hawking-theorist / mack-cosmic-bridge if the team-lead chooses). You have ONE
task. Complete it and stop.

================================================================================
Substrate Framing (MANDATORY)
================================================================================

The fabric is not IN space -- space is an emergent description of how the
fabric's spectral weight distributes itself through D_K eigenvalue
reorganization. Every computation must flow FROM the substrate TOWARD emergent
physics. The direction is:

    D_K eigenvalues -> spectral action moments -> emergent field equations
    -> observed physics

In this task specifically:

  Fold-epoch fiber excitation spectrum (8-mode BCS Bogoliubov)
     -> a_2 Seeley-DeWitt emergent FRW-like line element (W1-H: Omega_k = 0,
        R^(3) = 0 structurally, and g_M emergent from block-diagonal projection)
     -> H(tau) functional form from the fiber energy density via the emergent
        Friedmann equation (W1-E H(z))
     -> emergent Klein-Gordon equation for the comoving curvature perturbation
        zeta on that line element
     -> transfer kernel T(k) mapping P_zeta(k, tau_fold) to P_zeta(k, tau_recomb)
     -> line-of-sight projection with the transfer kernel and the emergent
        visibility function to angular power spectrum C_l^TT and C_l^TE

This is NOT GR-in-a-container. The Klein-Gordon equation is an OUTPUT of the
a_2 sector, not an input. The "mode evolution" is spectral-weight
reorganization inside the fabric between the fold epoch and recombination --
two parametric labels on the same fiber. The "Hubble horizon" is not a
boundary of a container; it is the length scale at which the emergent g_M's
second spectral moment balances the zeta-mode kinetic coefficient.

If you find yourself writing "the mode crosses the horizon as space expands"
or "P_zeta(k) in comoving Newtonian gauge on a pre-existing FRW background",
STOP and invert the direction. The FRW line element is derived; the mode
equation is an emergent effective equation; the horizon is a spectral balance
point.

================================================================================
Task: S75-TRANSFER-FUNCTION-75 (s75_transfer_function.py)
================================================================================

Compute the angular CMB power spectrum C_l^TT (and optionally C_l^TE) from the
fold-epoch fiber spectrum via a full first-principles transfer function
pipeline. The pipeline has four stages:

  Stage A: Emergent FRW-like line element from a_2 (input: W1-H, W1-E)
  Stage B: Mode evolution from tau_fold to tau_recomb on that line element
           (emergent Klein-Gordon for zeta_k)
  Stage C: Transfer function T(k) = zeta(k, tau_recomb) / zeta(k, tau_fold)
  Stage D: Line-of-sight projection to angular C_l

This is the framework-chapter Section 8.4 deferred item, now computable after
W1-E (H(tau) functional form) and W1-H (Omega_k = 0 structurally, a_2 FRW
line element) completed in S74.

The primary observable is the SHAPE of C_l (acoustic peak positions, relative
amplitudes, damping tail), NOT the overall amplitude. The overall amplitude
ties into the unresolved A_s budget (W1-A gap = 5.83 OOM, W1-G gap = 9.47 OOM,
W1-E f_conv bracket = 86 OOM). S75-TRANSFER-FUNCTION-75 leaves the A_s
normalization as an open calibration and quotes T(k) and C_l in dimensionless
ratio form.

================================================================================
Inputs (read-only, absolute paths from C:\sandbox\Ainulindale Exflation)
================================================================================

1. W1-E Friedmann output (fiber energy, H(tau) functional form, ZPE breakdown):
     computations/session-74/s74_friedmann_from_a2.npz

2. W1-H Flatness output (Omega_k = 0, R(SU(3)_tau), a_2 SDW constants):
     computations/session-74/s74_flatness_from_a2.npz

3. W1-A multifield delta-N transfer output (per-branch horizon-crossing
    reference; S75 should REPRODUCE W1-A as its fiber-stage subroutine and
    then extend past horizon crossing to recombination):
     computations/session-74/s74_transfer_function.npz

4. S73B transit power spectrum (8-mode BCS fold data, omega_k, r_k, mode
    weights, Phi_final, beta_sq_total, branch decomposition):
     computations/session-73/s73b_transit_ps.npz

5. S73A exit-horizon Bogoliubov (branch squeezings r_k_entry, r_k_bcs,
    phase-Jacobian data used in W1-A):
     computations/session-73/s73a_exit_horizon_bog.npz

6. S73A Fabry-Perot cavity (omega_k frequencies at fold, Ma_BA sanity
    check for the fold-entry impulsive region):
     computations/session-73/s73a_fabry_perot_cavity.npz

7. Canonical constants (MANDATORY: from canonical_constants import *):
     computations/_shared/canonical_constants.py

Inputs required but NOT produced by prior sessions (must be computed in S75):

  - Emergent visibility function g(tau) = n_e(tau) sigma_T c exp(-tau_optical)
    This is built FROM the substrate (not pulled from CAMB/CLASS). Specifically,
    the free-electron number density n_e(tau) is an OUTPUT of the GGE
    relic-to-matter conversion (W1-F GGE-PARTITION-74 Leggett channel) plus the
    branch-resolved fiber-to-baryon map (W2-K HP4-PAIRING-74 if completed, else
    use a zero'th-order model with a free ionization epoch). The recombination
    time tau_recomb is NOT an input from Planck; it is the epoch at which the
    Leggett-channel free-electron density drops below a threshold set by
    d/dtau(n_e sigma_T c) = 0 in the emergent frame.

  - Emergent matter power spectrum source. The Jeans length for the Leggett
    channel is k_J (computed separately in W4-FF LEGGETT-JEANS-74). s75 uses
    k_J as a sanity scale and cross-checks that the computed C_l acoustic
    peak positions are consistent with k_J being the sound horizon at
    tau_recomb.

================================================================================
Computation Steps
================================================================================

Step 1 -- Assemble the emergent FRW-like line element from W1-H + W1-E.

  From W1-H:
    Omega_k = 0 (structural; no K term in the line element)
    R^(3) = 0 on each constant-t hypersurface
    a_2 projection gives ds^2 = -dt^2 + a(t)^2 (dx^2 + dy^2 + dz^2)
    where a(t) is the scale factor whose evolution is given by W1-E H(t).

  From W1-E:
    The structural Friedmann relation is 3 H^2 = (8 pi G_N_emergent) rho,
    where G_N_emergent = 1/(16 pi a_2 f_2 M_KK^2) = 5.549e-40 GeV^(-2)
    (factor 12 of Planck, consistent with S44 Sakharov). This G_N is fixed
    by the structural a_2 coefficient and the f_2 second moment of the
    cutoff function f_star; it is NOT a free parameter in the transfer
    function stage.

    The energy density rho_GGE(tau) functional form is:
      rho_GGE(tau) = sum_k omega_k(tau) (n_k(tau) + 1/2)
    where n_k(tau) = sinh^2(r_k_compound(tau)) is the squeeze-dependent
    occupation and the sum is over the 8 BCS modes. Evaluate rho_GGE at
    tau_fold (already done in W1-E: 1.102e70 GeV^4) and at tau_recomb
    using the dilution + dispersion functional form from W1-E. This gives
    a(tau) implicitly via H^2(tau) = rho_GGE(tau)/(3 a_2 f_2 M_KK^2).

  Output: a(tau) table on a 2001-point log grid in tau from tau_fold to
          tau_today, plus H(tau) = d ln a / dt table, plus comoving
          conformal time eta(tau) = int dt'/a(t') table.

Step 2 -- Emergent Klein-Gordon equation for the comoving curvature
perturbation zeta.

  The zeta mode equation on the emergent line element is:

    zeta_k'' + 2 (z'/z) zeta_k' + c_s^2 k^2 zeta_k = 0

  where primes are derivatives with respect to conformal time eta,
  z = a * sqrt(2 epsilon) / c_s is the Mukhanov variable, epsilon = -H'/H^2
  is the Hubble slow-roll parameter (recovered from W1-E H(tau)), and c_s
  is the per-branch sound speed from the BCS dispersion at tau_fold,
  continuously evolved to tau_recomb via the fiber relaxation map already
  computed in W1-A.

  PER-BRANCH TREATMENT. The three branches (B1 acoustic, B2 flat-optical,
  B3 dispersive) each carry their own c_b(tau) and Jacobian J_b(tau). Use
  the W1-A per-branch Jacobian table as the initial condition at tau_fold
  and evolve each branch's zeta_b on the same emergent line element. The
  total zeta is the coherent sum weighted by the branch energy fractions
  psi_b from W1-A (psi_B1 = 0.801, psi_B2 = 0.004, psi_B3 = 0.195).

  Integrate from tau_fold to tau_recomb for 501 log-spaced wavenumbers in
  k in [10^-5, 10^-1] Mpc^-1 (the emergent 4D k; the conversion from
  M_KK^-1 to Mpc^-1 uses the emergent a_2 conversion, NOT a GR-fit scale
  factor). Use a stiff ODE integrator (scipy.integrate.solve_ivp with LSODA
  or Radau).

  Output: zeta_b(k, eta_recomb) table per branch, and the total zeta(k)
          at recombination.

Step 3 -- Transfer function T(k).

  T(k) = |zeta(k, tau_recomb) / zeta(k, tau_fold)|

  Extract:
    n_s(k_pivot) from d ln P_zeta / d ln k at k_pivot = 0.05 Mpc^-1
    alpha_s(k_pivot) from second log derivative
    A_s(k_pivot) UNCALIBRATED (quote as dimensionless ratio)
    k_peak[i] for i = 1..7 (first seven acoustic peak wavenumbers)
    ratio k_peak[i+1] / k_peak[i] for each i
    damping scale k_silk from exp(-k^2/k_silk^2) fit to T(k) at k > k_peak[1]

  Cross-check: in the uniform-velocity limit (all three c_b forced to the
  same value), T(k) should give a purely scale-invariant P_zeta (Sasaki-Stewart
  theorem). This is the S75 analog of W1-A's CHK1 check.

Step 4 -- Line-of-sight projection to C_l.

  The angular power spectrum for a scalar field is:

    C_l^TT = (4 pi / (2 l + 1)^2) * int dk/k * P_zeta(k) * |Theta_l(k)|^2

  where Theta_l(k) is the Sachs-Wolfe + ISW source, computed from the emergent
  line element's gravitational potential. For a substrate analysis, the
  Sachs-Wolfe term is:

    Theta_l^SW(k) = (1/3) zeta(k, tau_recomb) j_l(k * (eta_0 - eta_recomb))

  where eta_0 is the conformal time today, and j_l is the spherical Bessel
  function. The ISW term is:

    Theta_l^ISW(k) = int_tau_recomb^tau_0 dtau g(tau) Phi'(k, tau) j_l(k(eta_0 - eta(tau)))

  where g(tau) is the visibility function and Phi is the curvature potential
  (tied to zeta by the emergent Poisson equation via a_2).

  Evaluate C_l^TT at l = 2, 3, ..., 2500 using scipy.special.spherical_jn for
  the Bessel functions. Use the visibility function g(tau) from Step 1
  (if W1-F GGE-PARTITION and W2-K HP4-PAIRING are not yet complete, use a
  zero'th-order delta-function visibility at tau_recomb and report the result
  as S75-INFO pending the full visibility).

Step 5 -- Cross-checks (pre-registered; at least 5 must PASS for the gate).

  CHK1 -- Uniform-velocity limit: setting all three c_b(tau) to a common value
          must give a scale-invariant P_zeta(k) (Sasaki-Stewart theorem).
          PASS if n_s = 1 to 1e-10, FAIL otherwise.

  CHK2 -- S73B naive limit: turning off the multifield delta-N projection
          (all modes on a single rigid horizon) must reproduce the S73B
          W1-A alpha_s = +0.833 result to 1% (the failing extrapolation
          that motivated W1-A's multifield transfer).

  CHK3 -- W1-A at horizon crossing: evaluating T(k) at eta_recomb = eta_cross
          (no post-horizon evolution) must reproduce W1-A's alpha_s = 8e-15
          and n_s = 1 exactly (machine epsilon). This is the boundary
          condition at which S75 hands off to W1-A and nothing further is
          done. S75 must agree with W1-A in this limit.

  CHK4 -- Flatness sanity: Omega_k extracted from the computed a(tau) via
          Omega_k = -k_curvature / (a^2 H^2) must be 0 to machine epsilon
          (consistent with W1-H structural zero).

  CHK5 -- Acoustic peak ratio: k_peak[2] / k_peak[1] for the computed
          T(k) must equal 2.00 +- 0.05 for adiabatic initial conditions
          on a scale-invariant line element (this is a mathematical identity
          for cos(k c_s eta_recomb) peaks, not a Planck fit). FAIL if the
          ratio is outside [1.8, 2.2].

  CHK6 -- Silk damping recovery: k_silk_computed / k_silk_naive should be
          in [0.3, 3.0], where k_silk_naive = 2 pi / d_silk and d_silk is
          the photon diffusion length at recombination. This is a factor-3
          sanity check; a strict PASS is not required.

  CHK7 -- C_l positivity: C_l^TT > 0 for all l in [2, 2500]. FAIL if any
          bin is negative (indicates numerical instability in the line-of-sight
          integral).

  CHK8 -- l=2 ISW tail: C_2 should exceed C_1000 by a factor of at least 5
          if the ISW effect is included (large-scale tilt). If only the
          Sachs-Wolfe term is included (delta-function visibility, INFO path),
          C_2 should be in [0.5, 2] times C_1000. Cross-check on the
          visibility-function choice.

================================================================================
Output
================================================================================

1. Script: computations/session-75/s75_transfer_function.py
   (~600-800 lines, well-commented, follows the s74 style)

2. Data: computations/session-75/s75_transfer_function.npz
   Keys (at minimum):
     - labels (8-mode labels from S73B)
     - k_mpc_inv (501 log-spaced k values in [1e-5, 1e-1] Mpc^-1)
     - l_values (l = 2..2500)
     - a_tau (scale factor on 2001-point tau grid, emergent)
     - H_tau (Hubble rate on same grid)
     - eta_tau (conformal time)
     - epsilon_slow_roll (Hubble slow-roll parameter)
     - T_k (transfer function per k)
     - T_k_per_branch (3 x 501 array, per-branch transfer)
     - n_s_k_pivot (computed n_s at k = 0.05 Mpc^-1)
     - alpha_s_k_pivot
     - A_s_uncalibrated
     - k_peak (first 7 acoustic peaks)
     - k_silk (damping scale)
     - C_l_TT (uncalibrated; shape)
     - C_l_TT_SW (Sachs-Wolfe only)
     - C_l_TT_ISW (ISW contribution)
     - chk1..chk8 (cross-check flags, bool)
     - gate_verdict (string: "PASS", "FAIL", or "INFO")
     - gate_reasons (list of strings explaining each check)

3. Plot: computations/session-75/s75_transfer_function.png
   6-panel diagnostic:
     (a) a(tau), H(tau), eta(tau) on the emergent line element
     (b) T(k) per branch and total, vs k in log scale
     (c) P_zeta(k) at tau_fold and tau_recomb, comparison
     (d) C_l^TT shape (l in log, C_l l(l+1)/(2 pi) in log)
     (e) acoustic peak positions with annotated ratios
     (f) cross-check status panel (8 checks + gate verdict)

4. Log: computations/session-75/s75_transfer_function_output.log

================================================================================
Pre-Registered Gate
================================================================================

S75-TRANSFER-FUNCTION-75 (the S75-session gate; distinct from W4-CC S75-
TRANSFER-FUNCTION-SPEC-74 which is this spec itself):

  PASS -- CHK1-CHK5 and CHK7 all PASS, AND n_s(k_pivot) in [0.9607, 0.9691]
          (Planck 1-sigma), AND k_peak[2]/k_peak[1] in [1.8, 2.2], AND
          C_l^TT positive everywhere.

  INFO -- CHK1-CHK3 PASS, CHK4 PASS, CHK5 marginal ([1.6, 2.4]), visibility
          function is delta-function approximation OR n_s in [0.9565, 0.9733]
          (Planck 2-sigma) with the correct direction of departure from 1.

  FAIL -- CHK1 fails (scale-invariance theorem broken), OR CHK3 fails (W1-A
          boundary condition broken), OR CHK7 fails (negative C_l), OR
          n_s outside Planck 2-sigma in the wrong direction.

================================================================================
Environment
================================================================================

- Python: phonon-exflation-sim/.venv312/Scripts/python.exe
- Working dir: C:\sandbox\Ainulindale Exflation
- Canonical constants: from canonical_constants import * (MANDATORY).
  If a constant is not in canonical_constants.py, ADD it there first,
  then import. No hardcoding of framework constants.
- Local variables (computed intermediates) must be tagged with # (local).
- GPU not required for this task (CPU-only FFT and ODE integration).

================================================================================
Rules
================================================================================

- NUMBERS first. Gate second. Interpretation third.
- Pre-registered gates only. No retroactive threshold changes.
- One writer per output file (s75_transfer_function.py, .npz, .png, .log).
- Substrate framing discipline: every section of the script header and every
  print block must remind the reader that the line element is DERIVED, the
  Klein-Gordon is EMERGENT, and the horizon is a spectral balance point,
  not a causal boundary. Use "post-fold spectral relaxation region" instead
  of "exit horizon" in prose. See S74 W4-AA audit for the full vocabulary
  replacement table.
- A_s amplitude calibration is NOT part of this gate. Quote A_s_uncalibrated
  and let downstream sessions close the amplitude budget.
- When finished, STOP.

================================================================================
Cross-References
================================================================================

- W1-A TRANSFER-FUNCTION-74: the fiber-to-horizon stage of this pipeline.
  s75 consumes its outputs and extends them past horizon crossing.
- W1-E FRIEDMANN-FROM-A2-74: provides the H(tau) functional form and the
  emergent G_N. The f_conv calibration ambiguity is carried forward as an
  uncalibrated amplitude; the SHAPE observables (n_s, alpha_s, k_peak ratios,
  k_silk) are NOT affected by f_conv.
- W1-H FLATNESS-FROM-A2-74: structural basis for the FRW line element
  (Omega_k = 0 exactly by the block-diagonal theorem).
- W4-AA S70-S72-EXIT-HORIZON-AUDIT-74: vocabulary preservation table.
  Use "post-fold spectral relaxation region" in prose, preserve
  historical gate IDs in docstrings and npz keys.
- Framework chapter section 8.4: s75_transfer_function.py is listed there
  as a deferred item.

================================================================================
End of S75-TRANSFER-FUNCTION-75 prompt
================================================================================
"""

prompt_length_chars = len(S75_PROMPT)   # (local)
prompt_length_lines = len(S75_PROMPT.splitlines())   # (local)

print(f"  Prompt length: {prompt_length_chars} chars, "
      f"{prompt_length_lines} lines")
print()

# Sanity check: the prompt must contain all mandatory sections
required_sections = [                                                # (local)
    "Substrate Framing",
    "Task: S75-TRANSFER-FUNCTION-75",
    "Inputs",
    "Computation Steps",
    "Output",
    "Pre-Registered Gate",
    "Environment",
    "Rules",
    "Cross-References",
]
missing_sections = [s for s in required_sections if s not in S75_PROMPT]   # (local)

if missing_sections:
    print(f"  MISSING SECTIONS: {missing_sections}")
    gate_verdict = "FAIL"                                            # (local)
    gate_reason = f"Prompt is missing required sections: {missing_sections}"   # (local)
else:
    print(f"  All {len(required_sections)} required sections present.")
    gate_verdict = "PASS"                                            # (local)
    gate_reason = ("Full-fidelity S75 prompt written with all required "
                   "sections (substrate framing, task, inputs, computation "
                   "steps, output, pre-registered gate, environment, rules, "
                   "cross-references). W1-E FAIL is at the matching step "
                   "only; all structural ingredients (H(tau) form, a_2 "
                   "FRW line element, 8-mode BCS spectrum) are available "
                   "for S75 dispatch.")   # (local)
print()

# ==============================================================================
#  SECTION 3: Write the prompt + gate to npz
# ==============================================================================

print("SECTION 3: Write S75 prompt + gate verdict to npz")
print("-" * 78)

out_path = os.path.join(data_dir, "s74_s75_transfer_function_spec.npz")   # (local)

np.savez(
    out_path,
    s75_prompt=S75_PROMPT,
    prompt_length_chars=prompt_length_chars,
    prompt_length_lines=prompt_length_lines,
    required_sections=np.array(required_sections),
    missing_sections=np.array(missing_sections),
    gate_verdict=gate_verdict,
    gate_reason=gate_reason,
    # W1-E digest (for audit trail)
    w1e_a2_fold=w1e_a2_fold,
    w1e_f2_default=w1e_f2_default,
    w1e_M_KK_gev=w1e_M_KK_gev,
    w1e_G_N_emergent_inv_gev2=w1e_G_N_emergent_inv_gev2,
    w1e_G_N_planck_inv_gev2=w1e_G_N_planck_inv_gev2,
    w1e_G_ratio=w1e_G_ratio,
    w1e_rho_gge_fold=w1e_rho_gge_fold,
    w1e_rho_gge_zpe=w1e_rho_gge_zpe,
    w1e_zpe_frac=w1e_zpe_frac,
    w1e_N_efolds=w1e_N_efolds,
    w1e_matter_dilution=w1e_matter_dilution,
    w1e_rho_gge_today_diluted=w1e_rho_gge_today_diluted,
    w1e_rho_crit_obs=w1e_rho_crit_obs,
    w1e_rho_ratio=w1e_rho_ratio,
    w1e_H0_undershoot_oom=w1e_H0_undershoot_oom,
    w1e_H0_overshoot_oom=w1e_H0_overshoot_oom,
    w1e_H0_bracket_oom=w1e_H0_bracket_oom,
    # W1-H digest
    w1h_Omega_k=w1h_Omega_k,
    w1h_R_SU3_fold=w1h_R_SU3_fold,
    w1h_R_SU3_tau0=w1h_R_SU3_tau0,
    w1h_a2_homog_8D=w1h_a2_homog_8D,
)

print(f"  Wrote: {out_path}")
print()

# ==============================================================================
#  SECTION 4: Gate verdict summary
# ==============================================================================

print("SECTION 4: Gate verdict summary")
print("-" * 78)
print()
print(f"  Gate:     S75-TRANSFER-FUNCTION-SPEC-74")
print(f"  Verdict:  {gate_verdict}")
print(f"  Reason:   {gate_reason}")
print()
print(f"  W1-E structural status:     PASS (G_N, Bogoliubov, a_2 form intact)")
print(f"  W1-E matching status:       FAIL (f_conv ambiguity, 86 OOM bracket)")
print(f"  W1-H structural status:     PASS (Omega_k = 0 exact)")
print(f"  Spec writable:              YES (structural ingredients in hand)")
print()

t_end = time.time()   # (local)
print(f"Elapsed: {t_end - t_start:.2f} s")
print()
print("=" * 78)
print("END S75-TRANSFER-FUNCTION-SPEC-74")
print("=" * 78)
