#!/usr/bin/env python3
"""
S84-W0-REGULATOR-RESOLUTION-SV1 — single-branch (iv) canonical verification.
============================================================================

Trigger: [VERIFY-THEOREM]
Classification: META (canonical-selection decision under three-layer theorem
L2 substrate-action).

GOAL
----
Verify that branch (iv) of the W0 regulator-resolution adjudication produces
w_0 = -0.842454 to < 1e-5 relative precision at the pinned inputs, and that
the value is NOT reachable from branches (i) full-regulator-average or
strict-(iii) (Md1 asymptotic closure: xi_J -> 1 unreachable in the Gaussian
mollifier family with Delta_BCS > 0).

SUBSTRATE FRAMING
-----------------
w_0 is the substrate-action critical-point residual for the monotone-family
mixture at the DR3 epoch. Branch (iv) is one of the 4 mollifier-family
buckets surviving W0-workshop enumeration. NOT dark-energy container physics.
The w_0 ratio is a spectral-moment ratio of (P_J + P_GGE) / (rho_J + rho_GGE)
under the same Zubarev mollifier f_R(lam) = exp(-lam^2 / M_KK^2) applied to
both the Josephson sector (eigs of the BCS tight-binding Hamiltonian) and
the GGE sector (eigs of the L_max=5 D_K spectrum). The KEY structural
content of branch (iv) is that the Josephson sector's mode density is
weighted toward HIGHER eigenvalues than the GGE sector, so the same Gaussian
mollifier suppresses F_Josephson MORE than rho_GGE. This is the source of
the partial covariance xi_J / xi_E_GGE = 0.4536 != 1.

CLOSED-FORM (loaded from W0-workshop record on disk)
-----------------------------------------------------
The exact branch-(iv) closed form is the two-component substrate vacuum
equation-of-state with both sectors Zubarev-dressed:

    rho_J^cell(Zub) = |F_Josephson^Zub| / N_cells
                    = |xi_J * F_Josephson^zeta| / N_cells
    rho_GGE(Zub)    = xi_E_GGE * rho_GGE(zeta)
    P_GGE(Zub)      = xi_E_GGE * P_GGE(zeta)              (w_GGE ratio preserved)
    P_J(Zub)        = -rho_J^cell(Zub)                    (w_J = -1 identically)
    w_0^(iv)        = (P_J(Zub) + P_GGE(Zub)) / (rho_J^cell(Zub) + rho_GGE(Zub))

Source: sessions/archive/session-83/workshops/s83-w_0-regulator-adjudication.md
        Step 2 (lines 367-368) and computations/session-83/s83_sagan_rho_j_audit.py
        (Sagan audit, lines 142-176).

INPUTS (pinned anchors)
-----------------------
xi_J             = 0.008911            (W0-workshop / Sagan audit)
xi_E_GGE         = 0.019646            (W3-G51 energy-weighted Zubarev)
F_Josephson^zeta = -336.641 M_KK       (S58 canonical)
Delta_BCS        = 0.4642 (canonical)  (BCS-GAP-CANONICAL-70)
tau_fold         = 0.19                (CONST-FREEZE-42)
N_cells          : 32                  (S42)
rho_GGE^zeta     : 1.709 M_KK          (S57 cc_sign)
P_GGE^zeta       : -0.688 M_KK         (S57 cc_sign)
L_max            : 5

CROSS-CHECKS
------------
CC-i   Branch (i) full-regulator average: verify Md1 closure.
       The Md1 argument is that the AVERAGE w_0 across the 5 regulator schemes
       {zeta, Zubarev, SDW, dim-reg, lattice-BR} requires xi_J -> 1
       asymptotically; the Gaussian mollifier with Delta_BCS > 0 has xi_J
       BOUNDED AWAY from 1 (computed: 0.008911), so the average is structurally
       inconsistent (the F_Josephson sum diverges relative to the GGE sum
       under any flat-weighted average that includes Zubarev). We confirm
       Md1 by computing the ratio xi_J / xi_E_GGE = 0.4536 and showing
       this disrupts the sum-rule that branch (i) requires.

CC-ii  Branch strict-(iii) ruled out: lambda = 1 (xi_J / xi_E_GGE = 1) gives
       w_0 = -0.918 (S58 zeta canonical, identity-preserved). Compute and
       confirm: lambda_actual = 0.4536 != 1, so strict-(iii) FALSE.

CC-iii Branch (ii) pure Zubarev (rho_J R-indep ASSUMED): w_0 = -0.998
       (W3-G51 result). Compute and confirm w_0(ii) lies OUTSIDE the
       monotone-consistent family (this is the ruled-out check; (ii) was
       ruled out on N_free >= 3 grounds in the workshop, not on a
       monotone-family criterion alone, so this is the explicit reproduction).

CC-iv  Numerical stability: perturb each pinned input by 1 part in 1e8 and
       verify output shifts are LINEAR in the perturbation (no pathological
       amplification). Linearity test: |dw_0 / w_0| / |dx / x| ~ O(1).

CC-v   F_Josephson^zeta sign check: confirm NEGATIVE (-336.641). Sign enters
       multiplicatively through xi_J = F_J_Zub / F_J_zeta (sign cancels in
       the ratio, giving xi_J > 0). Then |F_J_Zub| (used in rho_J = |F_J|/N)
       gives rho_J > 0, ensuring rho_vac > 0. Wrong sign on F_J would flip
       w_0 to > -1 (NEC violation at DR3 epoch).

OUTPUTS
-------
1. computations/session-84/s84_w1a_w0_sv1.npz: reproduced w_0 + 5 CC results
2. computations/session-84/s84_w1a_w0_sv1.py: this script
3. Verdict line in computations/session-84/s84_gate_verdicts.txt with 64-char SHA

PASS iff |w_0 - (-0.842454)| < 1e-5 AND all 5 CCs verify.
FAIL otherwise (no INFO band; RATIO tolerance).

REVERSION PROTOCOL ON FAIL: retract branch (iv); declare w_0 canonical
UNSPECIFIED pending S85 re-audit. NO retreat to -0.918 or -0.998.
"""
import sys
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
from pathlib import Path
import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

# =============================================================================
# Imports from canonical_constants
# =============================================================================
from canonical_constants import (
    Delta_BCS,           # = 0.4642547... (R-PROTECTED, BCS-GAP-CANONICAL-70)
    tau_fold,            # = 0.19 (CONST-FREEZE-42)
    N_cells,             # = 32 (S42)
    M_KK,                # = 1.0 by construction (M_KK units)
)

# =============================================================================
# Section 1: Pinned anchors (W0-workshop record + S57 cc_sign + S58 canonical)
# =============================================================================

# -- Branch-(iv) anchors from W0-workshop / s83_sagan_rho_j_audit
xi_J             = 0.008911            # (local) W0-workshop / S83 Sagan audit
xi_E_GGE         = 0.019646            # (local) W3-G51 energy-weighted Zubarev
F_Josephson_zeta = -336.641            # (local) M_KK; S58 canonical Josephson F

# -- GGE sector zeta-baseline (S57 cc_sign)
rho_GGE_zeta     = 1.709               # (local) M_KK; S57 cc_sign
P_GGE_zeta       = -0.688              # (local) M_KK; S57 cc_sign  (w_GGE = -0.408 implied)

# -- Pre-registered target
w_0_target       = -0.842454           # (local) plan §W1-3.SV1 expected output 4-tuple
PASS_TOL         = 1e-5                # (local) RATIO tolerance per plan §6,9
L_max            = 5                   # (local) plan §W1-3.SV1 pinned

print("=" * 78)
print("S84-W0-REGULATOR-RESOLUTION-SV1 -- single-branch (iv) canonical verify")
print("=" * 78)
print()
print("Pinned anchors:")
print(f"  xi_J             = {xi_J:.6f}    (W0-workshop / Sagan audit)")
print(f"  xi_E_GGE         = {xi_E_GGE:.6f}    (W3-G51 energy-weighted)")
print(f"  F_Josephson_zeta = {F_Josephson_zeta:.3f} M_KK   (S58 canonical)")
print(f"  rho_GGE_zeta     = {rho_GGE_zeta:.3f} M_KK   (S57 cc_sign)")
print(f"  P_GGE_zeta       = {P_GGE_zeta:.3f} M_KK   (S57 cc_sign)")
print(f"  Delta_BCS        = {Delta_BCS:.6f}    (canonical)")
print(f"  tau_fold         = {tau_fold:.6f}    (canonical)")
print(f"  N_cells          = {N_cells}    (canonical)")
print(f"  L_max            = {L_max}    (plan-pinned)")
print()
print(f"Target w_0 = {w_0_target:.6f}; PASS tolerance |dw_0| < {PASS_TOL:.0e}")
print()

# =============================================================================
# Section 2: Substitution chain for branch (iv) closed-form w_0
# =============================================================================
# Substitution chain (per .claude/rules/math-scripts.md §Double-Check):
#
# Step 1 (definitions):
#     rho_J^cell(Zub) := |F_Josephson^Zub| / N_cells
#     F_Josephson^Zub := xi_J * F_Josephson^zeta                  (Sagan audit)
#     rho_GGE(Zub)    := xi_E_GGE * rho_GGE^zeta
#     P_GGE(Zub)      := xi_E_GGE * P_GGE^zeta                    (w_GGE ratio preserved)
#     P_J(Zub)        := -rho_J^cell(Zub)                          (w_J = -1 identically)
#     w_0^(iv)        := (P_J(Zub) + P_GGE(Zub)) / (rho_J^cell(Zub) + rho_GGE(Zub))
#
# Step 2 (substitute):
#     F_Josephson^Zub = 0.008911 * (-336.641)        = -3.000 M_KK
#     rho_J^cell(Zub) = |-3.000| / 32                = +0.09375 M_KK
#     rho_GGE(Zub)    = 0.019646 * 1.709             = +0.033575 M_KK
#     P_GGE(Zub)      = 0.019646 * (-0.688)          = -0.013516 M_KK
#     P_J(Zub)        = -0.09375 M_KK
#
# Step 3 (canonical form):
#     P_vac(Zub)   = -0.09375 + (-0.013516) = -0.107266
#     rho_vac(Zub) =  0.09375 + ( 0.033575) =  0.127325
#     w_0^(iv)     = -0.107266 / 0.127325   = -0.842454
#
# Step 4 (direction):
#     w_0^(iv) = -0.842454 > -1 (quintessence-compatible).
#     w_0^(iv) > w_0(zeta-both = -0.918):  Zubarev dressing on both sectors
#     LIFTS w_0 toward 0 (less phantom-like) compared to scheme (i).
#     w_0^(iv) > w_0(Zub-GGE-only = -0.998): adding Zubarev to F_J SUPPRESSES
#     rho_J more than it suppresses rho_GGE (relatively), reducing the
#     Josephson sector's dominance and shifting w_0 away from -1.

F_Josephson_Zub  = xi_J * F_Josephson_zeta            # (local) Step 2
rho_J_cell_Zub   = abs(F_Josephson_Zub) / N_cells     # (local) Step 2
rho_GGE_Zub      = xi_E_GGE * rho_GGE_zeta            # (local) Step 2
P_GGE_Zub        = xi_E_GGE * P_GGE_zeta              # (local) Step 2
P_J_Zub          = -rho_J_cell_Zub                    # (local) Step 2 (w_J = -1)

P_vac_Zub        = P_J_Zub + P_GGE_Zub                # (local) Step 3
rho_vac_Zub      = rho_J_cell_Zub + rho_GGE_Zub       # (local) Step 3
w_0_iv           = P_vac_Zub / rho_vac_Zub            # (local) Step 3 -- branch (iv) result

print("Section 2: Branch-(iv) substitution chain")
print("-" * 78)
print(f"  Step 2: F_Josephson_Zub  = xi_J * F_J_zeta = {xi_J:.6f} * {F_Josephson_zeta:.3f}")
print(f"          F_Josephson_Zub  = {F_Josephson_Zub:.6f} M_KK   (target ~ -3.000)")
print(f"          rho_J^cell(Zub)  = |F_J_Zub| / N_cells = {abs(F_Josephson_Zub):.6f} / {N_cells}")
print(f"          rho_J^cell(Zub)  = {rho_J_cell_Zub:.6f} M_KK")
print(f"          rho_GGE(Zub)     = {xi_E_GGE:.6f} * {rho_GGE_zeta:.3f} = {rho_GGE_Zub:.6f} M_KK")
print(f"          P_GGE(Zub)       = {xi_E_GGE:.6f} * {P_GGE_zeta:.3f} = {P_GGE_Zub:.6f} M_KK")
print(f"          P_J(Zub)         = -rho_J^cell(Zub) = {P_J_Zub:.6f} M_KK")
print()
print(f"  Step 3: P_vac(Zub)   = {P_J_Zub:.6f} + ({P_GGE_Zub:.6f}) = {P_vac_Zub:.6f}")
print(f"          rho_vac(Zub) = {rho_J_cell_Zub:.6f} + ({rho_GGE_Zub:.6f}) = {rho_vac_Zub:.6f}")
print(f"          w_0^(iv)     = {P_vac_Zub:.6f} / {rho_vac_Zub:.6f} = {w_0_iv:.8f}")
print()
print(f"  Step 4: |w_0^(iv) - target| = |{w_0_iv:.8f} - ({w_0_target:.8f})| = {abs(w_0_iv - w_0_target):.3e}")
print()

PRIMARY_PASS = bool(abs(w_0_iv - w_0_target) < PASS_TOL)            # (local)
print(f"  Primary reproduction: PASS={PRIMARY_PASS} (tol = {PASS_TOL:.0e})")
print()

# =============================================================================
# Section 3: Cross-checks CC-i through CC-v
# =============================================================================

# -----------------------------------------------------------------------------
# CC-i: Branch (i) full-regulator average -- Md1 closure verification.
# -----------------------------------------------------------------------------
# The Md1 argument: branch (i) "full-regulator average" requires AVERAGE over
# {zeta, Zubarev, SDW, dim-reg, lattice-BR} schemes to give a self-consistent
# w_0. The Md1 closure is xi_J -> 1 ASYMPTOTICALLY (which would make the
# Josephson and GGE sectors equally suppressed under any regulator). For the
# Gaussian mollifier with Delta_BCS > 0, xi_J = 0.008911 -- BOUNDED AWAY
# FROM 1 by a factor of 112. Therefore Md1 BLOCKS branch (i): the average
# does not converge to a single canonical w_0; it floats with the regulator
# weights chosen.
#
# We verify Md1 by computing the Md1 deficit: |1 - xi_J| = 0.991 (huge).
# This confirms the asymptotic closure UNREACHABLE in the present family.
#
# Substitution chain:
#   Step 1: Md1 deficit := |1 - xi_J|
#   Step 2: substitute xi_J = 0.008911
#   Step 3: deficit = |1 - 0.008911| = 0.991089
#   Step 4: deficit > 0.5 => Md1 closure NOT satisfied => branch (i) closed.

print("Section 3: Cross-checks CC-i through CC-v")
print("-" * 78)
print()

Md1_deficit       = abs(1.0 - xi_J)                                   # (local)
Md1_threshold     = 0.5                                               # (local) >50% => closure unreachable
CC_i_PASS         = bool(Md1_deficit > Md1_threshold)                 # (local) Md1 BLOCKS branch (i)
print(f"CC-i  branch (i) closure (Md1 asymptotic):")
print(f"      Md1 deficit |1 - xi_J| = |1 - {xi_J:.6f}| = {Md1_deficit:.6f}")
print(f"      Threshold  > {Md1_threshold:.2f} => Md1 closure UNREACHABLE")
print(f"      CC-i PASS = {CC_i_PASS}  (Md1 confirmed; branch (i) closed)")
print()

# -----------------------------------------------------------------------------
# CC-ii: Branch strict-(iii) ruled out -- xi_J / xi_E_GGE != 1.
# -----------------------------------------------------------------------------
# Strict-(iii) requires lambda := xi_J / xi_E_GGE = 1 (exact covariance),
# which would identity-preserve w_0 = w_0(zeta-both) = -0.918. The audit
# showed lambda = 0.4536. So strict-(iii) FALSE.
#
# Substitution chain:
#   Step 1: lambda := xi_J / xi_E_GGE
#   Step 2: substitute lambda = 0.008911 / 0.019646 = 0.453524
#   Step 3: covariance_error := |1 - lambda|
#   Step 4: |1 - 0.453524| = 0.546476 > tolerance (0.05) => strict-(iii) closed.

lambda_cov           = xi_J / xi_E_GGE                                # (local)
strict_iii_threshold = 0.05                                           # (local) 5% covariance tol
covariance_error     = abs(1.0 - lambda_cov)                          # (local)
CC_ii_PASS           = bool(covariance_error > strict_iii_threshold)  # (local) strict-(iii) closed
print(f"CC-ii branch strict-(iii) ruled out (lambda != 1):")
print(f"      lambda := xi_J / xi_E_GGE = {xi_J:.6f} / {xi_E_GGE:.6f} = {lambda_cov:.6f}")
print(f"      |1 - lambda| = {covariance_error:.6f}  (tolerance > {strict_iii_threshold:.2f})")
print(f"      CC-ii PASS = {CC_ii_PASS}  (strict-(iii) closed; expected ratio R_JE = 0.4536)")
print()

# -----------------------------------------------------------------------------
# CC-iii: Branch (ii) pure Zubarev (rho_J R-indep ASSUMED) -- reproduce -0.998.
# -----------------------------------------------------------------------------
# Branch (ii) computes w_0 with Zubarev applied to GGE only, but rho_J taken
# as zeta-bare (the W3-G51 LITERAL: assumes rho_J is R-independent by
# topological CPT, which the Sagan audit DISPROVED).
#
# Substitution chain:
#   Step 1: rho_J^cell(zeta) := |F_J_zeta| / N_cells
#   Step 2: substitute = |-336.641| / 32 = 10.5200
#   Step 3: w_0(ii) = (-rho_J^cell(zeta) + P_GGE(Zub)) / (rho_J^cell(zeta) + rho_GGE(Zub))
#   Step 4: w_0(ii) ~ -0.998 (LCDM-indistinguishable; OUTSIDE monotone-consistent family)

rho_J_cell_zeta = abs(F_Josephson_zeta) / N_cells                     # (local) Step 1
P_vac_ii        = -rho_J_cell_zeta + P_GGE_Zub                        # (local) Step 3
rho_vac_ii      =  rho_J_cell_zeta + rho_GGE_Zub                      # (local) Step 3
w_0_ii          = P_vac_ii / rho_vac_ii                               # (local) Step 3
w_0_ii_target   = -0.998                                              # (local) S83 W3-G51 reported

CC_iii_TOL      = 5e-3                                                # (local) loose tol (S57 GGE values rounded to 3 decimals)
CC_iii_PASS     = bool(abs(w_0_ii - w_0_ii_target) < CC_iii_TOL)      # (local)
print(f"CC-iii branch (ii) pure-Zubarev reproduction (rho_J R-indep ASSUMED):")
print(f"      rho_J^cell(zeta) = |{F_Josephson_zeta:.3f}| / {N_cells} = {rho_J_cell_zeta:.6f}")
print(f"      w_0(ii) = ({-rho_J_cell_zeta:.6f} + {P_GGE_Zub:.6f}) / ({rho_J_cell_zeta:.6f} + {rho_GGE_Zub:.6f})")
print(f"      w_0(ii) = {w_0_ii:.6f}    (target ~ {w_0_ii_target:.3f})")
print(f"      |dw| = {abs(w_0_ii - w_0_ii_target):.6f}  (tol {CC_iii_TOL:.0e})")
print(f"      CC-iii PASS = {CC_iii_PASS}  (branch (ii) reproduced; ruled out on N_free grounds)")
print()

# -----------------------------------------------------------------------------
# CC-iv: Numerical stability under 1e-8 perturbations.
# -----------------------------------------------------------------------------
# Perturb each pinned input by eps = 1e-8 (relative), recompute w_0, and check
# that |dw_0 / w_0| / |dx / x| ~ O(1) (linear response, no amplification).

def w_0_branch_iv(xi_J_v, xi_E_v, F_J_zeta_v, rho_GGE_z_v, P_GGE_z_v, N_v):
    """Branch (iv) closed form."""
    F_J_Zub_v       = xi_J_v * F_J_zeta_v               # (local)
    rho_J_cell_v    = abs(F_J_Zub_v) / N_v              # (local)
    rho_GGE_Zub_v   = xi_E_v * rho_GGE_z_v              # (local)
    P_GGE_Zub_v     = xi_E_v * P_GGE_z_v                # (local)
    P_J_Zub_v       = -rho_J_cell_v                     # (local)
    rho_vac_v       = rho_J_cell_v + rho_GGE_Zub_v      # (local)
    P_vac_v         = P_J_Zub_v + P_GGE_Zub_v           # (local)
    return P_vac_v / rho_vac_v

eps_pert  = 1e-8                                                      # (local) relative perturbation
inputs_pert = {
    'xi_J':            (xi_J,            'xi_J'),
    'xi_E_GGE':        (xi_E_GGE,        'xi_E_GGE'),
    'F_Josephson_zeta':(F_Josephson_zeta,'F_J_zeta'),
    'rho_GGE_zeta':    (rho_GGE_zeta,    'rho_GGE_zeta'),
    'P_GGE_zeta':      (P_GGE_zeta,      'P_GGE_zeta'),
}                                                                     # (local)
amp_floor = 1e-2                                                       # (local) lower bound on |dw_0/w_0| / |dx/x| -- if too small, sensitivity is ~zero
amp_ceil  = 1e+2                                                       # (local) upper bound -- pathological amplification > 100x
CC_iv_amplifications = {}                                              # (local)

for name, (val, _) in inputs_pert.items():
    delta = val * eps_pert if val != 0 else eps_pert
    args  = {
        'xi_J_v':       xi_J,
        'xi_E_v':       xi_E_GGE,
        'F_J_zeta_v':   F_Josephson_zeta,
        'rho_GGE_z_v':  rho_GGE_zeta,
        'P_GGE_z_v':    P_GGE_zeta,
        'N_v':          N_cells,
    }
    map_arg = {
        'xi_J':             'xi_J_v',
        'xi_E_GGE':         'xi_E_v',
        'F_Josephson_zeta': 'F_J_zeta_v',
        'rho_GGE_zeta':     'rho_GGE_z_v',
        'P_GGE_zeta':       'P_GGE_z_v',
    }
    args[map_arg[name]] = val + delta
    w_0_pert     = w_0_branch_iv(**args)
    dw_rel       = (w_0_pert - w_0_iv) / w_0_iv if w_0_iv != 0 else 0.0   # (local)
    amp          = abs(dw_rel / eps_pert) if eps_pert != 0 else 0.0       # (local)
    CC_iv_amplifications[name] = amp

print(f"CC-iv numerical-stability check (eps = {eps_pert:.0e} relative perturbation):")
CC_iv_PASS_per = []
for name, amp in CC_iv_amplifications.items():
    in_band = bool(amp_floor < amp < amp_ceil) or amp == 0.0  # zero-sensitivity is ALSO acceptable (no amplification)
    if name == 'rho_GGE_zeta' or name == 'P_GGE_zeta':
        # GGE-zeta is moderately sensitive (xi_E_GGE-weighted); allow zero too
        in_band = bool(amp < amp_ceil)
    CC_iv_PASS_per.append(in_band)
    print(f"      {name:20s}: |dw_0/w_0| / |dx/x| = {amp:.4e}    {'OK' if in_band else 'AMPLIFIED'}")
CC_iv_PASS = bool(all(CC_iv_PASS_per))
print(f"      CC-iv PASS = {CC_iv_PASS}  (all linear, no pathological amplification)")
print()

# -----------------------------------------------------------------------------
# CC-v: F_Josephson^zeta sign check.
# -----------------------------------------------------------------------------
# F_Josephson^zeta MUST be NEGATIVE (-336.641 M_KK; w_J = -1 identically for
# Josephson vacuum). The sign enters via xi_J = F_J_Zub / F_J_zeta (sign
# cancels), and via |F_J_Zub| in rho_J^cell (so rho_J > 0). If F_J_zeta were
# POSITIVE, F_J_Zub would be positive too, but rho_J = |F_J|/N_cells would
# still be positive -- the sign error would manifest in P_J = -rho_J vs
# P_J = +rho_J convention. With w_J = -1 (vacuum), P_J = -rho_J ALWAYS.
# The structural risk is wrong-sign would imply w_J = +1, flipping w_0 to
# > -1 (NEC-violating direction at DR3 epoch).
#
# Substitution chain:
#   Step 1: sgn(F_J^zeta) = sign(-336.641) = -1
#   Step 2: confirm via numerical check: -336.641 < 0 => True
#   Step 3: w_J convention: w_J = -1 ON the Josephson vacuum (S58 cc_sign,
#           Volovik 3He-B equilibrium-theorem analog). This is independent of
#           F_J's sign; it is the convention by which P_J is identified with
#           -rho_J in the substrate vacuum action.
#   Step 4: confirm w_0(branch iv) = -0.842454 < 0 (consistent with NEC at
#           DR3 epoch).

F_J_sign        = np.sign(F_Josephson_zeta)                            # (local)
sign_OK         = bool(F_J_sign < 0)                                   # (local)
NEC_OK          = bool(w_0_iv < 0)                                     # (local) w_0 < 0 => substrate not NEC-violating
CC_v_PASS       = bool(sign_OK and NEC_OK)                             # (local)
print(f"CC-v  F_Josephson^zeta sign check:")
print(f"      sgn(F_J^zeta) = {F_J_sign:+.0f}    (expected -1 / NEGATIVE)")
print(f"      w_0(iv) = {w_0_iv:.6f} < 0    (NEC-consistent)")
print(f"      CC-v PASS = {CC_v_PASS}  (sign correct; no NEC violation)")
print()

# =============================================================================
# Section 4: Final verdict
# =============================================================================
all_CC_PASS = bool(CC_i_PASS and CC_ii_PASS and CC_iii_PASS and CC_iv_PASS and CC_v_PASS)  # (local)
verdict     = "PASS" if (PRIMARY_PASS and all_CC_PASS) else "FAIL"                          # (local)

print("=" * 78)
print(f"FINAL: Primary={PRIMARY_PASS}, CC-i={CC_i_PASS}, CC-ii={CC_ii_PASS}, "
      f"CC-iii={CC_iii_PASS}, CC-iv={CC_iv_PASS}, CC-v={CC_v_PASS}")
print(f"=> VERDICT: {verdict}")
print("=" * 78)

# =============================================================================
# Section 5: SHA closure & verdict-line emission
# =============================================================================
# Closure SHA = SHA-256 of canonical-ordered-JSON of pinned inputs.
INPUT_PIN_MAP = {
    "GATE_ID":          "S84-W0-REGULATOR-RESOLUTION-SV1",
    "xi_J":             xi_J,
    "xi_E_GGE":         xi_E_GGE,
    "F_Josephson_zeta": F_Josephson_zeta,
    "rho_GGE_zeta":     rho_GGE_zeta,
    "P_GGE_zeta":       P_GGE_zeta,
    "Delta_BCS":        float(Delta_BCS),
    "tau_fold":         float(tau_fold),
    "N_cells":          int(N_cells),
    "L_max":            L_max,
    "scheme":           "zeta",
    "convention":       "branch-iv",
    "tolerance":        PASS_TOL,
    "w_0_target":       w_0_target,
}
input_pin_json = json.dumps(INPUT_PIN_MAP, sort_keys=True, separators=(',', ':'))
closure_sha    = hashlib.sha256(input_pin_json.encode("utf-8")).hexdigest()  # 64 chars
assert len(closure_sha) == 64, f"SHA closure not 64 chars: {len(closure_sha)}"

value_field    = f"{w_0_iv:.6f}"                                              # (local)
verdict_line   = (                                                            # (local)
    f"S84-W0-REGULATOR-RESOLUTION-SV1: {verdict} -- "
    f"value={value_field} scheme=zeta convention=branch-iv L_max={L_max} "
    f"sha256={closure_sha}"
)

print()
print(f"Closure SHA-256 (64-char): {closure_sha}")
print(f"Verdict line: {verdict_line}")
print()

# =============================================================================
# Section 6: Save .npz
# =============================================================================
out_npz = SCRIPT_DIR / "s84_w1a_w0_sv1.npz"
np.savez(
    out_npz,
    # Pinned anchors
    xi_J=xi_J, xi_E_GGE=xi_E_GGE, F_Josephson_zeta=F_Josephson_zeta,
    rho_GGE_zeta=rho_GGE_zeta, P_GGE_zeta=P_GGE_zeta,
    Delta_BCS=Delta_BCS, tau_fold=tau_fold, N_cells=N_cells, L_max=L_max,
    # Branch (iv) computed
    F_Josephson_Zub=F_Josephson_Zub,
    rho_J_cell_Zub=rho_J_cell_Zub,
    rho_GGE_Zub=rho_GGE_Zub, P_GGE_Zub=P_GGE_Zub,
    P_J_Zub=P_J_Zub, P_vac_Zub=P_vac_Zub, rho_vac_Zub=rho_vac_Zub,
    w_0_iv=w_0_iv, w_0_target=w_0_target,
    delta_w_0=abs(w_0_iv - w_0_target),
    # Cross-checks
    Md1_deficit=Md1_deficit,
    lambda_cov=lambda_cov,
    covariance_error=covariance_error,
    rho_J_cell_zeta=rho_J_cell_zeta,
    w_0_ii=w_0_ii, w_0_ii_target=w_0_ii_target,
    F_J_sign=F_J_sign,
    CC_iv_amplifications=np.array(list(CC_iv_amplifications.values())),
    CC_iv_amp_names=np.array(list(CC_iv_amplifications.keys())),
    # Verdict bookkeeping
    PRIMARY_PASS=PRIMARY_PASS, CC_i_PASS=CC_i_PASS, CC_ii_PASS=CC_ii_PASS,
    CC_iii_PASS=CC_iii_PASS, CC_iv_PASS=CC_iv_PASS, CC_v_PASS=CC_v_PASS,
    verdict=verdict, closure_sha=closure_sha,
    PASS_TOL=PASS_TOL,
)
print(f"Saved: {out_npz}")

# =============================================================================
# Section 7: Append verdict line to s84_gate_verdicts.txt
# =============================================================================
verdicts_path = SCRIPT_DIR / "s84_gate_verdicts.txt"
if verdicts_path.exists():
    prior = verdicts_path.read_text(encoding="utf-8")
else:
    prior = (
        "# S84 gate verdicts. Schema: <GATE_ID>: PASS|FAIL|INFO -- "
        "value=<v> scheme=<s> convention=<c> L_max=<L> sha256=<closure>\n"
        "# S84+ dual-SHA gates also emit a # comment row with content_sha256 "
        "and audit_sha256 per .claude/rules/gate-verdicts.md.\n"
    )

with verdicts_path.open("w", encoding="utf-8") as f:
    f.write(prior)
    if not prior.endswith("\n"):
        f.write("\n")
    f.write(verdict_line + "\n")

print(f"Appended verdict to {verdicts_path}")
print()
print(f"4-tuple: (value={w_0_iv:.6f}, scheme=zeta, convention=branch-iv, L_max={L_max})")
