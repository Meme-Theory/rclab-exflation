"""
S84 W1b-4: S84-MU-BC-GEOMETRIC -- bi-criterion main gate
============================================================================

Geometric coupling-ratio identity on the spectral triple (A_F, H, D_K):

    F(tau) := 3 / (3 + exp(12*tau))                  (CUBIC L1 algebraic id)
    sin^2(theta_W)_cubic := F(tau_fold)              (L3b beta-conjecture)
    mu_BC_K3 := M_Z / sqrt(F(tau))
              = M_Z * sqrt(1 + exp(12*tau)/3)        (Layer-3b ball-volume)

Substrate framing
-----------------
mu_BC is a coupling-ratio identity on the internal geometry. The fiber
F = SU(3) (Jensen-deformed) IS the structure at each point; there is no
"internal vs external" -- the fiber is all there is. M_Z is not a mass "of"
something embedded in spacetime; it is a spectral moment of D_K at
tau = tau_fold. The chain runs:

    D_K eigenvalues -> Mellin-cone moments -> coupling-ratio constants

mu_BC is the boundary-condition scale at which the geometric cubic identity
sin^2(theta_W) = F(tau_fold) = 0.234803 holds; running it down to M_Z via
2-loop + Yukawa RGE recovers PDG 0.23122 to high precision (S83 G47).

Layered structure
-----------------
L1   Cubic algebraic identity F(tau) = 3/(3 + exp(12*tau))
       PROVEN to 2.78e-17 machine epsilon (re-verified here).
L2   tau_fold = 0.19 +/- 0.01 (3He-B inheritance pin, S42 freeze).
L3a  K_SUBSTRATE = A_F-SU(3) project-wide alpha-identification.
L3b  Ball-volume = coupling-ratio beta-conjecture
       Vol(B_alpha_1) / Vol(B_alpha_2) = exp(12*tau) / 3
       The cubic exponent 12 is L1; the denominator 3 from
       C^2 (+) M_3(C) decomposition with C^2 block OMITTED.

Bi-criterion
------------
(A) Numerical agreement vs S83 PRIMARY (188.34 GeV) at < 0.5%
(B) Wave-9 obligations dispatched (NOT discharged here):
     DERIV-I  cube-3 override:  d_spec(s) := Tr(|D_K|^{-s}) -> 3 at fiber-transition
     DERIV-II C^2-block omission: rep-theoretic decomposition placing
              C^2 block off-diagonal so it does not enter sin^2 expression

Composite verdict
-----------------
W1b-4 PASS  <==>  (A) PASS  AND  (B) DISPATCHED-TO-W9 (both gates)

M_H interpretation lockout (PERMANENTLY CLOSED)
-----------------------------------------------
The old "M_Z + M_H = 97 GeV" back-solve is closed on three channels
(2-loop + KK threshold m_H = 131.8 GeV is NOT tree-level; Coleman-Weinberg
shift too small by ~3x; LEP2 exclusion m_H > 114.4 GeV at 95% CL).
This script does NOT use 97 GeV as a coupling boundary anywhere.
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# -- canonical constants (S34+ MANDATORY import) ---------------------------
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    M_Z, tau_fold, sin2_thetaW_MSbar
)

_HERE = Path(__file__).parent

# -- plan-pinned constants (orchestrator override) -------------------------
# Per plan §W1b-4 explicit pins:
#   G47 PRIMARY = 188.34 GeV   (2-loop + Yukawa, S83 W3 G47)
#   G47 CHK1    = 188.44 GeV   (2-loop gauge only, S83 W3 G47)
mu_BC_PRIMARY_S83 = 188.34   # (local) plan §W1b-4 PRIMARY pin (G47 PRIMARY line)
mu_BC_CHK1_S83 = 188.44      # (local) plan §W1b-4 CHK1 pin    (G47 CHK1 line)

# -- gate parameters (PRDR machinery pin) ----------------------------------
A_THRESHOLD_PCT = 0.5            # (local) PASS criterion (A) threshold
INFO_BAND_LO_PCT = 0.3           # (local) INFO band lower
INFO_BAND_HI_PCT = 0.5           # (local) INFO band upper
EPS_L1_TOLERANCE = 1e-15         # (local) L1 identity machine-epsilon tolerance
TAU_SCAN_LO = 0.18               # (local) sensitivity bracket lower
TAU_SCAN_HI = 0.20               # (local) sensitivity bracket upper
TAU_SCAN_STEP = 0.001            # (local) sensitivity bracket step
TAU_UNCERTAINTY = 0.01           # (local) tau_fold +/- pin (3He-B)
CUBIC_EXPONENT_a = 12            # (local) CUBIC L1 algebraic exponent
BALL_VOL_DENOM = 3               # (local) C^2-omitted L3b beta denominator

# Expected pins (plan §6 PROCEDURE)
F_FOLD_EXPECTED = 0.234803       # (local) L1 expected at tau_fold (6 dp)
F_FOLD_EPSILON_BOUND = 2.78e-17  # (local) prior proof residual ceiling
MU_BC_K3_EXPECTED = 188.185      # (local) plan-stated expected output


# ==========================================================================
# Section 0 -- input pin map and SHA closure (S84+ dual-SHA schema)
# ==========================================================================
INPUT_PINS: dict[str, str] = {}


def _file_sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


# Static-file SHA pins (these enter the closure SHA).
_static_files = [
    _HERE / "canonical_constants.py",
    _HERE / "s83_w3_g47_sin2_thetaW_2loop_mu_BC.py",
    _HERE / "s83_gate_verdicts.txt",
]
for _p in _static_files:
    if _p.exists():
        INPUT_PINS[_p.name] = _file_sha(_p)
    else:
        INPUT_PINS[_p.name] = "MISSING"

# Pinned constants (literal-pin map; canonical_constants subset used)
INPUT_PINS["M_Z_PDG"] = f"{M_Z:.6f}"
INPUT_PINS["tau_fold"] = f"{tau_fold:.6f}"
INPUT_PINS["sin2_thetaW_MSbar_PDG"] = f"{sin2_thetaW_MSbar:.6f}"
INPUT_PINS["mu_BC_PRIMARY_S83"] = f"{mu_BC_PRIMARY_S83:.4f}"
INPUT_PINS["mu_BC_CHK1_S83"] = f"{mu_BC_CHK1_S83:.4f}"
INPUT_PINS["CUBIC_EXPONENT_a"] = f"{CUBIC_EXPONENT_a:d}"
INPUT_PINS["BALL_VOL_DENOM"] = f"{BALL_VOL_DENOM:d}"
INPUT_PINS["A_THRESHOLD_PCT"] = f"{A_THRESHOLD_PCT:.4f}"
INPUT_PINS["TAU_SCAN_LO"] = f"{TAU_SCAN_LO:.4f}"
INPUT_PINS["TAU_SCAN_HI"] = f"{TAU_SCAN_HI:.4f}"
INPUT_PINS["TAU_SCAN_STEP"] = f"{TAU_SCAN_STEP:.4f}"
INPUT_PINS["scheme"] = "CUBIC-OMITTED-C2"
INPUT_PINS["convention"] = "L3b-beta-BALL-VOL-RATIO"
INPUT_PINS["L_max"] = "N_A"

# content closure: input pin map only (script INPUTS, not OUTPUTS)
CLOSURE_INPUT = json.dumps(INPUT_PINS, sort_keys=True, separators=(",", ":"))
content_sha256 = hashlib.sha256(CLOSURE_INPUT.encode("utf-8")).hexdigest()


# ==========================================================================
# Section 1 -- banner + SHA log (per gate-verdicts.md, first 20 lines)
# ==========================================================================
print("=" * 78)
print("S84 W1b-4: MU-BC-GEOMETRIC (bi-criterion main gate)")
print("=" * 78)
print(f"content_sha256 (64 char) : {content_sha256}")
print(f"content_sha256 (16 head) : {content_sha256[:16]}")
print()
print("--- input pin map ---")
for k, v in INPUT_PINS.items():
    print(f"  {k:<32s}: {v}")
print()
print("--- canonical constants used ---")
print(f"  M_Z (PDG on-shell)         = {M_Z:.6f} GeV")
print(f"  tau_fold (S42 freeze)      = {tau_fold:.6f}")
print(f"  sin^2(theta_W)_PDG_MSbar   = {sin2_thetaW_MSbar:.6f}")
print(f"  mu_BC_PRIMARY_S83 (G47)    = {mu_BC_PRIMARY_S83:.4f} GeV")
print(f"  mu_BC_CHK1_S83 (G47)       = {mu_BC_CHK1_S83:.4f} GeV")
print()


# ==========================================================================
# Section 2 -- Layer-1 algebraic identity (CUBIC, machine epsilon)
# ==========================================================================
print("=" * 78)
print("Layer-1: CUBIC algebraic identity F(tau) = 3 / (3 + exp(12*tau))")
print("=" * 78)


def F_cubic(tau: float, a: int = CUBIC_EXPONENT_a, denom: int = BALL_VOL_DENOM) -> float:
    """L1 + L3b combined: F(tau) = denom / (denom + exp(a * tau))."""
    return denom / (denom + np.exp(a * tau))


def mu_BC_geometric(tau: float, m_z: float = M_Z) -> float:
    """L3b beta: mu_BC = M_Z / sqrt(F(tau)) = M_Z * sqrt(1 + exp(12*tau)/denom)."""
    return m_z / np.sqrt(F_cubic(tau))


# Sub-step 2.1: F_fold direct vs hand-computed reference
F_fold = F_cubic(tau_fold)                              # (local)
F_fold_ref = 3.0 / (3.0 + np.exp(2.28))                 # (local)
F_fold_residual = abs(F_fold - F_fold_ref)              # (local)
print(f"  F(tau_fold = {tau_fold:.4f}) = {F_fold:.16f}")
print(f"  Reference 3/(3+exp(2.28)) = {F_fold_ref:.16f}")
print(f"  |F_fold - reference|      = {F_fold_residual:.3e}")
print(f"  Tolerance (machine eps)   = {EPS_L1_TOLERANCE:.3e}")
L1_machine_eps_PASS = F_fold_residual < EPS_L1_TOLERANCE     # (local)
print(f"  L1 identity (machine eps) : {'PASS' if L1_machine_eps_PASS else 'FAIL'}")

# Sub-step 2.2: round-to-6-decimal pin check
F_fold_6dp_match = abs(F_fold - F_FOLD_EXPECTED) < 1e-6      # (local)
print(f"  F_fold matches expected {F_FOLD_EXPECTED:.6f} at 1e-6 : "
      f"{'PASS' if F_fold_6dp_match else 'FAIL'}")
print()


# ==========================================================================
# Section 3 -- Layer-2 tau_fold pin and sensitivity
# ==========================================================================
print("=" * 78)
print("Layer-2: tau_fold pin (3He-B inheritance) and dmu_BC/dtau sensitivity")
print("=" * 78)


def dmu_BC_dtau(tau: float, m_z: float = M_Z, a: int = CUBIC_EXPONENT_a,
                denom: int = BALL_VOL_DENOM) -> float:
    """
    Analytical derivative:
        mu_BC(tau) = M_Z * sqrt(1 + exp(a*tau)/denom)
        => dmu_BC/dtau = M_Z * (a * exp(a*tau) / denom)
                       / (2 * sqrt(1 + exp(a*tau)/denom))
    """
    e = np.exp(a * tau)
    num = a * e / denom
    den = 2.0 * np.sqrt(1.0 + e / denom)
    return m_z * num / den


# Analytic derivative at tau_fold
dmu_dtau_fold = dmu_BC_dtau(tau_fold)                          # (local)

# Numerical derivative (central difference) for cross-check
_h = 1e-6                                                       # (local)
dmu_num = (mu_BC_geometric(tau_fold + _h)
           - mu_BC_geometric(tau_fold - _h)) / (2.0 * _h)       # (local)
deriv_residual = abs(dmu_dtau_fold - dmu_num)                   # (local)

print(f"  dmu_BC/dtau at tau_fold (analytic) = {dmu_dtau_fold:.6f} GeV/unit-tau")
print(f"  dmu_BC/dtau at tau_fold (numeric ) = {dmu_num:.6f}")
print(f"  |analytic - numeric|               = {deriv_residual:.3e}")
print(f"  pin uncertainty (3He-B)            : tau = 0.19 +/- {TAU_UNCERTAINTY:.3f}")
mu_BC_uncertainty = dmu_dtau_fold * TAU_UNCERTAINTY              # (local)
print(f"  +/- mu_BC at tau_fold              : {mu_BC_uncertainty:.4f} GeV")
print()


# ==========================================================================
# Section 4 -- Layer-3b mu_BC_K3 evaluation at tau_fold
# ==========================================================================
print("=" * 78)
print("Layer-3b: mu_BC_K3 = M_Z * sqrt(1 + exp(12*tau_fold)/3)")
print("=" * 78)

# Step-by-step (substitution chain explicit)
exp_term = np.exp(CUBIC_EXPONENT_a * tau_fold)                  # (local)
ratio_term = exp_term / BALL_VOL_DENOM                          # (local)
sum_term = 1.0 + ratio_term                                     # (local)
sqrt_term = np.sqrt(sum_term)                                   # (local)
mu_BC_K3 = M_Z * sqrt_term                                      # (local)

# Cross-check via 1/sqrt(F)
mu_BC_K3_check = M_Z / np.sqrt(F_fold)                          # (local)
mu_BC_self_consistency = abs(mu_BC_K3 - mu_BC_K3_check)         # (local)

print(f"  Step 1: exp(12 * 0.19)        = {exp_term:.6f}")
print(f"  Step 2: exp(12*tau)/3         = {ratio_term:.6f}")
print(f"  Step 3: 1 + exp(12*tau)/3     = {sum_term:.6f}")
print(f"  Step 4: sqrt(...)             = {sqrt_term:.6f}")
print(f"  Step 5: M_Z * sqrt(...)       = {mu_BC_K3:.6f} GeV")
print(f"  cross: M_Z / sqrt(F_fold)     = {mu_BC_K3_check:.6f} GeV")
print(f"  |mu_BC - cross|               = {mu_BC_self_consistency:.3e}")
print()
mu_BC_K3_match_expected = abs(mu_BC_K3 - MU_BC_K3_EXPECTED) < 5e-3   # (local)
print(f"  mu_BC_K3 vs plan-expected ({MU_BC_K3_EXPECTED:.3f}) : "
      f"{'PASS' if mu_BC_K3_match_expected else 'FAIL'}")
print()


# ==========================================================================
# Section 5 -- bi-criterion (A) numerical agreement
# ==========================================================================
print("=" * 78)
print("Bi-criterion (A): residual vs S83 PRIMARY and CHK1")
print("=" * 78)

residual_A_PRIMARY = abs(mu_BC_K3 - mu_BC_PRIMARY_S83) / mu_BC_PRIMARY_S83 * 100.0   # (local)
residual_A_CHK1 = abs(mu_BC_K3 - mu_BC_CHK1_S83) / mu_BC_CHK1_S83 * 100.0            # (local)

print(f"  mu_BC_K3 (geometric L3b)      = {mu_BC_K3:.6f} GeV")
print(f"  S83 PRIMARY (G47 2L+Yukawa)   = {mu_BC_PRIMARY_S83:.4f} GeV")
print(f"  S83 CHK1    (G47 2L gauge)    = {mu_BC_CHK1_S83:.4f} GeV")
print(f"  residual_A vs PRIMARY         = {residual_A_PRIMARY:.4f} %")
print(f"  residual_A vs CHK1            = {residual_A_CHK1:.4f} %")
print(f"  PASS threshold                = {A_THRESHOLD_PCT:.4f} %")

A_PASS_PRIMARY = residual_A_PRIMARY < A_THRESHOLD_PCT                                # (local)
A_PASS_CHK1 = residual_A_CHK1 < A_THRESHOLD_PCT                                      # (local)
A_INFO_BAND = (INFO_BAND_LO_PCT <= residual_A_PRIMARY < INFO_BAND_HI_PCT)            # (local)

if A_INFO_BAND:
    A_VERDICT = "INFO"
elif A_PASS_PRIMARY:
    A_VERDICT = "PASS"
else:
    A_VERDICT = "FAIL"

print(f"  criterion (A) verdict         = {A_VERDICT}")
print()


# ==========================================================================
# Section 6 -- bi-criterion (B): DERIV-I + DERIV-II dispatch status
# ==========================================================================
print("=" * 78)
print("Bi-criterion (B): Wave-9 sub-obligation dispatch status")
print("=" * 78)

# Per orchestrator override: DERIV-I and DERIV-II are DISPATCHED-TO-W9.
# This script CITES dispatch status; it does NOT discharge them.
# Plan §1163 verdict-line + §0.10 PRDR pre-registration require explicit
# dispatch metadata for each sub-obligation.

DERIV_I_dispatch = {
    "id": "S84-W9-DERIV-I",
    "title": "cube-3 override via spectral dimension",
    "predicate": "d_spec(s) = Tr(|D_K|^{-s}) -> 3 at fiber-transition scale",
    "status": "DISPATCHED-TO-W9",
    "wave": 9,
    "agent_type": "connes-ncg-theorist + lizzi-spectral-functional-theorist",
    "gate_spec_present": True,
    "discharge_required": True,
    "carry_forward_id": "#105",
    "note": "Wave-9 sub-obligation; NOT discharged in W1b-4 per orchestrator override.",
}

DERIV_II_dispatch = {
    "id": "S84-W9-DERIV-II",
    "title": "C^2-block off-diagonal omission",
    "predicate": ("rep-theoretic decomposition of D_K eigenstates places "
                  "C^2 block off-diagonal (W+/-, Z + coset X/Y) so it does "
                  "NOT enter sin^2(theta_W) expression"),
    "status": "DISPATCHED-TO-W9",
    "wave": 9,
    "agent_type": "connes-ncg-theorist + van-den-dungen-bridge-theorist",
    "gate_spec_present": True,
    "discharge_required": True,
    "carry_forward_id": "#106",
    "note": "Wave-9 sub-obligation; NOT discharged in W1b-4 per orchestrator override.",
}

print(f"  DERIV-I  : id={DERIV_I_dispatch['id']}")
print(f"             status={DERIV_I_dispatch['status']}, wave={DERIV_I_dispatch['wave']}")
print(f"             predicate={DERIV_I_dispatch['predicate']}")
print(f"  DERIV-II : id={DERIV_II_dispatch['id']}")
print(f"             status={DERIV_II_dispatch['status']}, wave={DERIV_II_dispatch['wave']}")
print(f"             predicate={DERIV_II_dispatch['predicate']}")
print()

B_DISPATCHED = (
    DERIV_I_dispatch["status"] == "DISPATCHED-TO-W9"
    and DERIV_I_dispatch["gate_spec_present"]
    and DERIV_II_dispatch["status"] == "DISPATCHED-TO-W9"
    and DERIV_II_dispatch["gate_spec_present"]
)                                                                                    # (local)
print(f"  criterion (B) dispatched      = {B_DISPATCHED}")
print()


# ==========================================================================
# Section 7 -- composite verdict (W1b-4 PASS condition)
# ==========================================================================
print("=" * 78)
print("Composite verdict")
print("=" * 78)
# Composite rule (plan §7 trigger discipline):
#   W1b-4 PASS  iff  (A PASS) AND (B DISPATCHED)
#   W1b-4 FAIL  if   (A FAIL) OR  (B NOT-DISPATCHED)
#   W1b-4 INFO  if   (A INFO band) AND (B DISPATCHED)
if A_VERDICT == "PASS" and B_DISPATCHED:
    composite_verdict = "PASS"
elif A_VERDICT == "INFO" and B_DISPATCHED:
    composite_verdict = "INFO"
else:
    composite_verdict = "FAIL"

print(f"  (A) verdict     = {A_VERDICT}")
print(f"  (B) dispatched  = {B_DISPATCHED}")
print(f"  composite (W1b-4) = {composite_verdict}")
print()


# ==========================================================================
# Section 8 -- cross-checks CC1..CC4
# ==========================================================================
print("=" * 78)
print("Cross-checks CC1 .. CC4 (independent derivations)")
print("=" * 78)

# CC1 (analytic limits): F(0) = 0.75 ; F(infty) -> 0 ; monotone decreasing
F_0 = F_cubic(0.0)                                          # (local)
F_inf_approx = F_cubic(10.0)                                # (local) approximate infinity
CC1_F0 = abs(F_0 - 0.75) < 1e-12                            # (local)
CC1_Finf = F_inf_approx < 1e-50                             # (local)

# Monotonicity check: F'(tau) < 0 for tau > 0
def F_prime(tau: float, a: int = CUBIC_EXPONENT_a, denom: int = BALL_VOL_DENOM) -> float:
    """F'(tau) = -denom * a * exp(a*tau) / (denom + exp(a*tau))^2 < 0."""
    e = np.exp(a * tau)
    return -denom * a * e / (denom + e) ** 2

CC1_monotone_check_taus = np.linspace(0.01, 1.0, 50)         # (local)
CC1_monotone = bool(np.all(np.array([F_prime(t) for t in CC1_monotone_check_taus]) < 0))   # (local)
CC1_PASS = CC1_F0 and CC1_Finf and CC1_monotone

print(f"  CC1: F(0) = {F_0:.6f} (expect 0.75)         : {'PASS' if CC1_F0 else 'FAIL'}")
print(f"  CC1: F(10) = {F_inf_approx:.3e} (expect ->0): {'PASS' if CC1_Finf else 'FAIL'}")
print(f"  CC1: F'(tau) < 0 on [0.01, 1.0]            : {'PASS' if CC1_monotone else 'FAIL'}")
print(f"  CC1 verdict                                : {'PASS' if CC1_PASS else 'FAIL'}")

# CC2 (tau sensitivity bracket): compute mu_BC at endpoints
#
# NOTE ON PLAN-NARRATIVE DISCREPANCY: the plan §W1b-4 CC2 text quotes
#   tau=0.18 -> F=0.2504, mu=182.2 GeV
#   tau=0.20 -> F=0.2196, mu=194.5 GeV
# These values are algebraically INCONSISTENT with the formula
#   F(tau) = 3/(3 + exp(12*tau))
# which yields F(0.18)=0.257044, F(0.20)=0.213932.
# (Reverse-check: mu=182.2 implies F=0.2505, mu=194.5 implies F=0.2198.)
# The plan's central pin (F_fold=0.234803 at tau_fold=0.19) IS consistent.
# CC2 therefore tests formula-consistent values. The plan-narrative values
# are recorded as an observation for Wave-9 audit (likely a linearization
# typo in the plan prose; the formula is canonical).
F_018 = F_cubic(0.18)                                       # (local)
F_020 = F_cubic(0.20)                                       # (local)
mu_BC_018 = mu_BC_geometric(0.18)                           # (local)
mu_BC_020 = mu_BC_geometric(0.20)                           # (local)

# Formula-consistent expectation: CC2 checks the monotone sensitivity
# direction and the bracket width scale (NOT the plan narrative numbers).
CC2_F_decreasing = (F_018 > F_fold > F_020)                 # (local) monotonicity PASS
CC2_mu_increasing = (mu_BC_018 < mu_BC_K3 < mu_BC_020)      # (local) mu increasing in tau
# bracket half-width should be within a factor ~2 of the analytical
# dmu/dtau * 0.01 uncertainty (analytical = 8.6399 GeV)
mu_BC_bracket_half_width = (mu_BC_020 - mu_BC_018) / 2.0    # (local)
CC2_bracket_matches_analytic = abs(mu_BC_bracket_half_width - mu_BC_uncertainty) \
                               / mu_BC_uncertainty < 0.10   # (local) within 10%
CC2_PASS = CC2_F_decreasing and CC2_mu_increasing and CC2_bracket_matches_analytic

# Plan-narrative values (recorded for Wave-9 audit, NOT enforced)
_plan_F_018 = 0.2504                                         # (local) plan prose
_plan_F_020 = 0.2196                                         # (local) plan prose
_plan_mu_018 = 182.2                                         # (local) plan prose
_plan_mu_020 = 194.5                                         # (local) plan prose

print(f"  CC2: F(0.18) = {F_018:.6f}    (plan-prose 0.2504; formula-computed)")
print(f"  CC2: F(0.20) = {F_020:.6f}    (plan-prose 0.2196; formula-computed)")
print(f"  CC2: mu_BC(0.18) = {mu_BC_018:.4f} GeV (plan-prose 182.2; formula-computed)")
print(f"  CC2: mu_BC(0.20) = {mu_BC_020:.4f} GeV (plan-prose 194.5; formula-computed)")
print(f"  CC2: half-width  = +/- {mu_BC_bracket_half_width:.4f} GeV (analytic {mu_BC_uncertainty:.4f})")
print(f"  CC2: F decreasing in tau (0.18 > fold > 0.20)    : {'PASS' if CC2_F_decreasing else 'FAIL'}")
print(f"  CC2: mu increasing in tau (0.18 < fold < 0.20)   : {'PASS' if CC2_mu_increasing else 'FAIL'}")
print(f"  CC2: bracket half-width matches analytic dmu/dtau: {'PASS' if CC2_bracket_matches_analytic else 'FAIL'}")
print(f"  CC2 verdict (formula-consistent monotonicity)   : {'PASS' if CC2_PASS else 'FAIL'}")
print(f"  CC2 NOTE: plan §W1b-4 CC2 prose values (0.2504, 182.2 ; 0.2196, 194.5)")
print(f"            are algebraically inconsistent with F(tau) = 3/(3+exp(12*tau)).")
print(f"            Recording for Wave-9 plan-text audit.")

# CC3 (sin^2 theta_W PDG comparison)
F_fold_minus_PDG_pct = (F_fold - sin2_thetaW_MSbar) / sin2_thetaW_MSbar * 100.0   # (local)
# Plan §6 CC3: residual ~1.40%, expected to close to <1% under DERIV-II + 2-loop + Yukawa
CC3_pos_pct_present = (F_fold_minus_PDG_pct > 0.0)          # (local) F_fold > PDG before run-down
CC3_residual_in_band = (1.0 < F_fold_minus_PDG_pct < 2.0)   # (local) 1-2% structural position
CC3_PASS = CC3_pos_pct_present and CC3_residual_in_band

print(f"  CC3: F_fold = {F_fold:.6f} vs sin^2_PDG_MSbar = {sin2_thetaW_MSbar:.6f}")
print(f"  CC3: residual = {F_fold_minus_PDG_pct:.4f}% (positive sign expected pre-RGE-rundown)")
print(f"  CC3 (1-2% structural position pre-DERIV-II): {'PASS' if CC3_PASS else 'FAIL'}")

# CC4 (bi-directional identity): mu_BC * sqrt(F_fold) =?= M_Z
CC4_product = mu_BC_K3 * np.sqrt(F_fold)                    # (local)
CC4_residual = abs(CC4_product - M_Z)                       # (local)
CC4_PASS = CC4_residual < 1e-10
print(f"  CC4: mu_BC_K3 * sqrt(F_fold) = {CC4_product:.10f} GeV")
print(f"  CC4: |product - M_Z|         = {CC4_residual:.3e} (expect < 1e-10)")
print(f"  CC4 verdict                                : {'PASS' if CC4_PASS else 'FAIL'}")

CC_ALL_PASS = CC1_PASS and CC2_PASS and CC3_PASS and CC4_PASS
print(f"  CC ALL PASS                                : {'PASS' if CC_ALL_PASS else 'FAIL'}")
print()


# ==========================================================================
# Section 9 -- sensitivity bracket scan
# ==========================================================================
print("=" * 78)
print("Sensitivity bracket scan (tau in [0.18, 0.20], step 0.001)")
print("=" * 78)

tau_scan = np.arange(TAU_SCAN_LO, TAU_SCAN_HI + TAU_SCAN_STEP / 2.0, TAU_SCAN_STEP)   # (local)
F_scan = np.array([F_cubic(t) for t in tau_scan])                                      # (local)
mu_scan = np.array([mu_BC_geometric(t) for t in tau_scan])                             # (local)
print(f"  scan length    = {len(tau_scan)} points")
print(f"  tau range      = [{tau_scan[0]:.4f}, {tau_scan[-1]:.4f}]")
print(f"  F range        = [{F_scan.min():.6f}, {F_scan.max():.6f}]")
print(f"  mu_BC range    = [{mu_scan.min():.4f}, {mu_scan.max():.4f}] GeV")
# Substitution chain for monotonicity direction:
#   F'(tau) = -denom*a*exp(a*tau) / (denom + exp(a*tau))^2 < 0 (proven CC1)
#   mu_BC = M_Z / sqrt(F)  =>  d(mu_BC)/dtau = -M_Z * F'/(2 F^{3/2}) > 0
#   F' < 0 and F > 0  =>  -F' > 0  =>  d(mu_BC)/dtau > 0 (strictly increasing)
mu_strictly_increasing = bool(np.all(np.diff(mu_scan) > 0))                            # (local)
print(f"  mu_BC strictly increasing in tau           : {mu_strictly_increasing}")
print()


# ==========================================================================
# Section 10 -- M_H interpretation lockout (PERMANENTLY CLOSED)
# ==========================================================================
print("=" * 78)
print("M_H interpretation lockout (97 GeV back-solve PERMANENTLY CLOSED)")
print("=" * 78)
print("  Channel 1: framework m_H = 131.8 GeV is 2-loop + KK threshold,")
print("             NOT tree-level.")
print("  Channel 2: Coleman-Weinberg shift too small by factor ~3 to recover 97 GeV.")
print("  Channel 3: LEP2 direct-search exclusion m_H > 114.4 GeV at 95% CL.")
print("  Status   : LOCKED. No 97-GeV pin replayed. mu_BC_K3 = 188.185 GeV is the")
print("             coupling-ratio scale, NOT a Higgs-pin auxiliary.")
print()


# ==========================================================================
# Section 11 -- bi-criterion JSON payload
# ==========================================================================
print("=" * 78)
print("Bi-criterion JSON payload")
print("=" * 78)
payload = {
    "gate_id": "S84-MU-BC-GEOMETRIC",
    "session": 84,
    "wave": "W1b-4",
    "trigger": "[CHAIN]",
    "classification": "GEOMETRIC",
    "agents": ["connes-ncg-theorist", "kaluza-klein-theorist"],
    "scheme": "CUBIC-OMITTED-C2",
    "convention": "L3b-beta-BALL-VOL-RATIO",
    "L_max": "N/A",
    "expected_4tuple": {
        "value": "188.185_GeV",
        "scheme": "CUBIC-OMITTED-C2",
        "convention": "L3b-beta-BALL-VOL-RATIO",
        "L_max": "N/A",
    },
    "layered_structure": {
        "L1_cubic_identity": {
            "expression": "F(tau) = 3 / (3 + exp(12*tau))",
            "F_fold_value": float(F_fold),
            "F_fold_residual": float(F_fold_residual),
            "tolerance": float(EPS_L1_TOLERANCE),
            "machine_eps_PASS": bool(L1_machine_eps_PASS),
        },
        "L2_tau_fold_pin": {
            "tau_fold": float(tau_fold),
            "uncertainty": float(TAU_UNCERTAINTY),
            "dmu_BC_dtau_analytic": float(dmu_dtau_fold),
            "dmu_BC_dtau_numeric": float(dmu_num),
            "deriv_residual": float(deriv_residual),
            "mu_BC_uncertainty": float(mu_BC_uncertainty),
        },
        "L3a_K_substrate": "K_SUBSTRATE = A_F-SU(3) (project-wide alpha-id)",
        "L3b_beta_conjecture": {
            "expression": "mu_BC = M_Z * sqrt(1 + exp(12*tau)/3)",
            "mu_BC_K3_value": float(mu_BC_K3),
            "self_consistency_residual": float(mu_BC_self_consistency),
        },
    },
    "bi_criterion_A": {
        "mu_BC_K3": float(mu_BC_K3),
        "mu_BC_PRIMARY_S83": float(mu_BC_PRIMARY_S83),
        "mu_BC_CHK1_S83": float(mu_BC_CHK1_S83),
        "residual_PRIMARY_pct": float(residual_A_PRIMARY),
        "residual_CHK1_pct": float(residual_A_CHK1),
        "threshold_pct": float(A_THRESHOLD_PCT),
        "INFO_band": [INFO_BAND_LO_PCT, INFO_BAND_HI_PCT],
        "A_PASS": bool(A_PASS_PRIMARY),
        "A_INFO_band": bool(A_INFO_BAND),
        "A_verdict": A_VERDICT,
    },
    "bi_criterion_B": {
        "DERIV_I": DERIV_I_dispatch,
        "DERIV_II": DERIV_II_dispatch,
        "B_dispatched": bool(B_DISPATCHED),
    },
    "composite_verdict": composite_verdict,
    "cross_checks": {
        "CC1_analytic_limits_PASS": bool(CC1_PASS),
        "CC1_F_0": float(F_0),
        "CC1_F_inf_approx": float(F_inf_approx),
        "CC1_monotone": bool(CC1_monotone),
        "CC2_tau_sensitivity_PASS": bool(CC2_PASS),
        "CC2_F_018_formula": float(F_018),
        "CC2_F_020_formula": float(F_020),
        "CC2_mu_BC_018_GeV_formula": float(mu_BC_018),
        "CC2_mu_BC_020_GeV_formula": float(mu_BC_020),
        "CC2_bracket_half_width_GeV": float(mu_BC_bracket_half_width),
        "CC2_F_decreasing": bool(CC2_F_decreasing),
        "CC2_mu_increasing": bool(CC2_mu_increasing),
        "CC2_bracket_matches_analytic": bool(CC2_bracket_matches_analytic),
        "CC2_plan_narrative_F_018": _plan_F_018,
        "CC2_plan_narrative_F_020": _plan_F_020,
        "CC2_plan_narrative_mu_018": _plan_mu_018,
        "CC2_plan_narrative_mu_020": _plan_mu_020,
        "CC2_plan_narrative_discrepancy_note": (
            "Plan §W1b-4 CC2 prose values (F(0.18)=0.2504, mu=182.2; "
            "F(0.20)=0.2196, mu=194.5) are algebraically inconsistent with "
            "F(tau) = 3/(3+exp(12*tau)). Formula yields F(0.18)=0.257044 and "
            "F(0.20)=0.213932. Central pin (F_fold=0.234803, mu_BC=188.185) "
            "IS consistent. Recorded for Wave-9 plan-text audit."
        ),
        "CC3_PDG_comparison_PASS": bool(CC3_PASS),
        "CC3_residual_pct": float(F_fold_minus_PDG_pct),
        "CC4_bidirectional_identity_PASS": bool(CC4_PASS),
        "CC4_residual": float(CC4_residual),
        "CC_all_pass": bool(CC_ALL_PASS),
    },
    "sensitivity_scan": {
        "tau_lo": float(TAU_SCAN_LO),
        "tau_hi": float(TAU_SCAN_HI),
        "tau_step": float(TAU_SCAN_STEP),
        "n_points": int(len(tau_scan)),
        "F_min": float(F_scan.min()),
        "F_max": float(F_scan.max()),
        "mu_BC_min_GeV": float(mu_scan.min()),
        "mu_BC_max_GeV": float(mu_scan.max()),
        "mu_BC_strictly_increasing": bool(mu_strictly_increasing),
    },
    "M_H_interpretation_lockout": {
        "status": "PERMANENTLY-CLOSED",
        "channels": [
            "framework m_H = 131.8 GeV (2-loop + KK threshold, NOT tree-level)",
            "Coleman-Weinberg shift insufficient by ~3x for 97 GeV recovery",
            "LEP2 direct-search exclusion m_H > 114.4 GeV at 95% CL",
        ],
        "back_solve_replayable": False,
    },
    "input_pins": INPUT_PINS,
    "content_sha256": content_sha256,
}

# audit_sha256: closure over (input pins) + (output payload values) + (verdict)
audit_input = json.dumps(
    {
        "content_sha256": content_sha256,
        "composite_verdict": composite_verdict,
        "A_verdict": A_VERDICT,
        "B_dispatched": bool(B_DISPATCHED),
        "F_fold": float(F_fold),
        "mu_BC_K3": float(mu_BC_K3),
        "residual_A_PRIMARY_pct": float(residual_A_PRIMARY),
        "residual_A_CHK1_pct": float(residual_A_CHK1),
        "CC1_PASS": bool(CC1_PASS),
        "CC2_PASS": bool(CC2_PASS),
        "CC3_PASS": bool(CC3_PASS),
        "CC4_PASS": bool(CC4_PASS),
    },
    sort_keys=True,
    separators=(",", ":"),
)
audit_sha256 = hashlib.sha256(audit_input.encode("utf-8")).hexdigest()
payload["audit_sha256"] = audit_sha256

print(f"  content_sha256 (64 char) : {content_sha256}")
print(f"  audit_sha256   (64 char) : {audit_sha256}")
print()


# ==========================================================================
# Section 12 -- write artifacts (.npz, .json, .png)
# ==========================================================================
print("=" * 78)
print("Writing artifacts")
print("=" * 78)

# .npz
npz_path = _HERE / "s84_w1b_mu_bc_geometric.npz"
np.savez(
    str(npz_path),
    F_fold=F_fold,
    F_fold_residual=F_fold_residual,
    mu_BC_K3=mu_BC_K3,
    mu_BC_PRIMARY_S83=mu_BC_PRIMARY_S83,
    mu_BC_CHK1_S83=mu_BC_CHK1_S83,
    residual_A_PRIMARY_pct=residual_A_PRIMARY,
    residual_A_CHK1_pct=residual_A_CHK1,
    tau_scan=tau_scan,
    F_scan=F_scan,
    mu_scan=mu_scan,
    mu_BC_bracket_half_width=mu_BC_bracket_half_width,
    dmu_dtau_fold=dmu_dtau_fold,
    mu_BC_uncertainty=mu_BC_uncertainty,
    F_018=F_018,
    F_020=F_020,
    mu_BC_018=mu_BC_018,
    mu_BC_020=mu_BC_020,
    A_threshold_pct=A_THRESHOLD_PCT,
    composite_verdict=composite_verdict,
    A_verdict=A_VERDICT,
    B_dispatched=B_DISPATCHED,
    content_sha256=content_sha256,
    audit_sha256=audit_sha256,
)
print(f"  wrote {npz_path}")

# .json
json_path = _HERE / "s84_w1b_mu_bc_geometric.json"
with json_path.open("w", encoding="utf-8") as fh:
    json.dump(payload, fh, indent=2, sort_keys=True)
print(f"  wrote {json_path}")

# .png
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

ax_F = axes[0]
ax_F.plot(tau_scan, F_scan, "b-", lw=2, label=r"$F(\tau) = 3 / (3 + e^{12\tau})$")
ax_F.axvline(tau_fold, color="r", ls="--", lw=1.2, label=fr"$\tau_{{\rm fold}}={tau_fold}$")
ax_F.axhline(F_fold, color="r", ls=":", lw=1.0, alpha=0.7,
             label=fr"$F_{{\rm fold}}={F_fold:.6f}$")
ax_F.axhline(sin2_thetaW_MSbar, color="g", ls=":", lw=1.0, alpha=0.7,
             label=fr"$\sin^2\theta_W^{{\rm PDG}}={sin2_thetaW_MSbar:.5f}$")
ax_F.set_xlabel(r"Jensen deformation $\tau$")
ax_F.set_ylabel(r"$F(\tau) = \sin^2\theta_W^{\rm cubic}$")
ax_F.set_title(r"L1 cubic identity (CC3 1.40% structural position)")
ax_F.legend(loc="best", fontsize=8)
ax_F.grid(True, alpha=0.3)

ax_mu = axes[1]
ax_mu.plot(tau_scan, mu_scan, "k-", lw=2,
           label=r"$\mu_{\rm BC} = M_Z\sqrt{1 + e^{12\tau}/3}$")
ax_mu.axvline(tau_fold, color="r", ls="--", lw=1.2,
              label=fr"$\tau_{{\rm fold}}={tau_fold}$")
ax_mu.axhline(mu_BC_K3, color="r", ls=":", lw=1.0, alpha=0.7,
              label=fr"$\mu_{{\rm BC}}^{{\rm K3}}={mu_BC_K3:.3f}$ GeV")
ax_mu.axhline(mu_BC_PRIMARY_S83, color="b", ls="-.", lw=1.2,
              label=fr"S83 PRIMARY $={mu_BC_PRIMARY_S83}$ GeV")
ax_mu.axhline(mu_BC_CHK1_S83, color="m", ls="-.", lw=1.0, alpha=0.7,
              label=fr"S83 CHK1 $={mu_BC_CHK1_S83}$ GeV")
# half-width band around mu_BC_K3 for the +/- 0.5% threshold (visualization)
band = A_THRESHOLD_PCT / 100.0 * mu_BC_PRIMARY_S83          # (local)
ax_mu.fill_between(tau_scan,
                   mu_BC_PRIMARY_S83 - band,
                   mu_BC_PRIMARY_S83 + band,
                   color="lightblue", alpha=0.3,
                   label=fr"$\pm{A_THRESHOLD_PCT}\%$ around S83 PRIMARY")
ax_mu.set_xlabel(r"Jensen deformation $\tau$")
ax_mu.set_ylabel(r"$\mu_{\rm BC}$ [GeV]")
ax_mu.set_title("Layer-3b geometric mu_BC (CC2 sensitivity bracket)")
ax_mu.legend(loc="best", fontsize=8)
ax_mu.grid(True, alpha=0.3)

plt.suptitle(
    f"S84 W1b-4: MU-BC-GEOMETRIC -- composite {composite_verdict} "
    f"(A {A_VERDICT}, residual {residual_A_PRIMARY:.4f}%; B DISPATCHED-TO-W9)",
    fontsize=11,
)
plt.tight_layout()
png_path = _HERE / "s84_w1b_mu_bc_geometric.png"
plt.savefig(str(png_path), dpi=120, bbox_inches="tight")
plt.close(fig)
print(f"  wrote {png_path}")
print()


# ==========================================================================
# Section 13 -- verdict line append (S84+ dual-SHA schema)
# ==========================================================================
print("=" * 78)
print("Appending verdict line to s84_gate_verdicts.txt")
print("=" * 78)

verdict_line = (
    f"S84-MU-BC-GEOMETRIC: {composite_verdict} -- "
    f"value=188.185_GeV scheme=CUBIC-OMITTED-C2 "
    f"convention=L3b-beta-BALL-VOL-RATIO L_max=N/A "
    f"content_sha256={content_sha256} "
    f"audit_sha256={audit_sha256}"
)
verdict_path = _HERE / "s84_gate_verdicts.txt"
with verdict_path.open("a", encoding="utf-8") as fh:
    fh.write(verdict_line + "\n")
print(f"  appended to {verdict_path}")
print()
print("verdict line:")
print(f"  {verdict_line}")
print()

# Final 4-tuple (last non-verdict line per template).
print(f"4-TUPLE: (value=188.185_GeV, scheme=CUBIC-OMITTED-C2, "
      f"convention=L3b-beta-BALL-VOL-RATIO, L_max=N/A)")
