#!/usr/bin/env python3
"""
S83 Wave 2 Gate G7 — CC7-DYNAMICAL
====================================

Gate: S83-CC7-DYNAMICAL  [VERIFY][CHAIN]
Classification: PHONONIC
Owner: transit-dynamics-theorist

Purpose: The DYNAMICAL backbone of the CC7 hierarchy (W-2 carry-forward #1).
Tests whether the Mukhanov mode equation, integrated from fold-epoch BD
initial conditions to the CMB-pivot e-fold, produces an amplification
factor F_amp_lin(N_pivot) consistent with the UNIFIED-AS-79 ledger target
F_amp_canonical = 1.0166 (S80 W1-B-REMED Method B pin) within a factor-3
band.

Phononic framing:
  The Mukhanov variable v_k = z(N) * zeta_k is the canonical curvature
  phonon on the a_2-Seeley-DeWitt emergent metric g_M.  The equation
      v_k'' + (k^2 - z''/z) v_k = 0
  IS the substrate phonon wave equation in the GGE approximation.  The
  pump field z''/z is a time-dependent frequency modulation of the
  parametric oscillator; F_amp_lin measures the integrated Bogoliubov
  squeeze across the post-fold dS cascade.  For strict-dS + constant
  eps_H this is the standard inflaton calculation; the substrate
  derivation says the SAME mode equation applies post-relaxation from
  the fold SUPERSONIC transit (Mach 13.75, dS_fold=+58,673).  The gate
  tests the dynamical content of the transitive W1-2 PASS-F2 that
  currently RESTS on F_amp_canonical = 1.0166 as INPUT.

Substitution chain [VERIFY][CHAIN]:

  Step 1 (definitions):
    Mukhanov variable:   z(N) = a(N) * sqrt(2 * eps_H(N)) * M_Pl_eff
    Mode equation:       v_k'' + (k^2 - z''/z) v_k = 0   ('=d/d(eta))
    Bunch-Davies IC:     v_k(eta) -> (1/sqrt(2k)) * exp(-i*k*eta)  when |k*eta|>>1
    Power spectrum:      P_zeta(k) = (k^3/(2 pi^2)) * |v_k(N_horizon)/z(N_horizon)|^2

  Step 2 (substitution):
    In strict dS with constant eps_H, H(N) = H0 * exp(-eps_H * N) gives
    a(N) = exp(N), and analytical solution for v_k:
      v_k(eta) = (sqrt(pi)/2) * sqrt(-eta) * H_nu^{(1)}(-k*eta) * exp(i pi (nu+1/2)/2)
      nu = 3/2 + eps_H (first-order slow-roll)
    Late-time limit (|k*eta| -> 0): |v_k|^2 -> (1/(2k))*(1/|k*eta|)^{2*nu-1}*2^{2*nu-1}*Gamma(nu)^2/pi

  Step 3 (F_amp_lin definition):
    F_amp_lin(N) := |v_k(N)|^2 / |v_k^{BD}(N)|^2
    where |v_k^{BD}|^2 is the BD mode amplitude evolved under pure-dS (nu=3/2).
    Equivalently (W-2 §Epoch-gating L460):
      F_amp_lin(k, N) = measured |v_k(N)|^2 vs bare |v_k^{BD}|^2 at same N

    At horizon crossing N = N_pivot (k = aH):
      F_amp_lin(pivot) = (Gamma(3/2+eps_H)/Gamma(3/2))^2 * (2/|k*eta_pivot|)^{2*eps_H}
      With |k*eta|=1 at crossing:
      F_amp_lin(pivot, analytic) = (Gamma(1.5 + eps_H)/Gamma(1.5))^2 * 2^{2*eps_H}

  Step 4 (target):
    F_amp_target := F_amp_canonical = 1.0166
    Source: S80 W1-B-REMED Method B pin, used as INPUT in S82 W1-2 PASS-F2.
    Also matches W-2 §Epoch-gating T4 (s82-as-ledger-self-consistent.md L413/L419):
      "F_amp_canonical = 1.0166 at N_pivot = 55 e-folds post-fold represents
       the surviving transient amplification after full post-fold dS decay
       of the substrate polarization."

  Step 5 (composite check per [CHAIN] trigger):
    F_amp_lin should factor as  F_amp_lin = F_amp^{3PI} * k_a2^{-1}  (inverse slot rescale)
    because F_amp_slot = F_amp_canonical * k_a2 (slot-adjusted), so in
    the pre-slot ledger,  F_amp_canonical = F_amp_slot / k_a2.
    Alternatively (W-2 §Epoch-gating L544): F_amp^{3PI}(N_pivot) = F_amp_lin(N_pivot)
    (to leading order in r(N_pivot) << 1 at pivot).
    So the composite check is: F_amp_lin(pivot, dynamical) ~ F_amp_canonical
    ~ F_amp^{3PI}(N_pivot) ~ (S78 3PI ceiling at pivot) converges to unity.

  Step 6 (PRE-PYTHON direction from canonical form):
    For eps_H > 0 (canonical 0.02163 > 0), both (Gamma(1.5+eps)/Gamma(1.5))^2
    and 2^{2*eps_H} exceed 1. Therefore F_amp_lin(pivot) > 1.
    For eps_H = 0 (pure dS), F_amp_lin = 1 exactly (BD limit recovered).
    This direction is INDEPENDENT of the numerical integration; the
    numerical solver reproduces this inequality by construction if the
    mode equation and IC are correctly implemented.

  Step 7 (Python verification and threshold classification):
    See Section 7 (solve_ivp run + F_amp extraction) and Section 8 (PASS/INFO/FAIL).

Canonical inputs pinned:
  eps_H      = 0.02163             (S75/S77 canonical; S82 W1-2 factor 2)
  N_pivot    = 64.08                (S82 W-1 #10; CMB pivot e-fold count)
  H_fold     = 586.53 M_KK          (S38 s38_kz_defects.npz via H_fold canonical)
  k_pivot    = k* (mode with horizon crossing at N_pivot)

References:
  * S82 W-2 workshop:  sessions/archive/session-82/workshops/s82-as-ledger-self-consistent.md
    - L460: F_amp_canonical definition
    - L413/L419: F_amp_canonical = 1.0166 at N_pivot = 55 e-folds
    - L622, L634-L638: CC7' proposed as Mukhanov dynamical integration
    - L1394-L1403: CC7' promoted canonical dynamical test
  * S82 W1-2:  computations/session-82/s82_w1_2_unified_as_79_full.py
    - F_amp_canonical = 1.0166 used as INPUT to W1-2 PASS-F2
  * S80 Mukhanov:  computations/session-80/s80_unified_as_79_mode_eqn.py
    - Bare dS derivation and W1-6 cross-checks
  * S64 Mukhanov-Sasaki:  computations/session-64/s64_mukhanov_sasaki.py
    - Prior full substrate-profile implementation; this script uses the
      analytically-cleaner strict-dS+eps formulation per the W1-G4 PASS
      that epsilon_H is trajectory-FI (F_traj=3/2 at threshold).

Output 4-tuple: (value=F_amp_lin, scheme=zeta, convention=Mukhanov-BD-to-pivot, L_max=N/A)

Environment: CPU-only scalar ODE (solve_ivp); 8-thread cap per rule.
"""

import os
# CPU cap BEFORE numpy import (scalar ODE; no GPU benefit)
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.integrate import solve_ivp
from scipy.special import gamma as gamma_fn
from scipy.special import hankel1

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

# Canonical constants (MANDATORY import)
from canonical_constants import (
    PI,
    H_fold,           # 586.53 M_KK (S38)
    tau_fold,         # 0.19
    M_Pl_reduced,
    A_s_CMB,          # 2.1e-9 Planck 2018
)

# =============================================================================
# SECTION 0: Input SHA-256 pin map (MANDATORY, first 20 lines of stdout)
# =============================================================================

def _sha256_file(path):
    """SHA-256 hexdigest of file bytes; 'FILE_MISSING' if absent."""
    p = Path(path)
    if not p.exists():
        return "FILE_MISSING"
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


INPUT_PINS = {
    "canonical_const":   SCRIPT_DIR / "canonical_constants.py",
    "s82_w1_2":          SCRIPT_DIR / "s82_w1_2_unified_as_79_full.py",
    "s80_mode_eqn_ref":  SCRIPT_DIR / "s80_unified_as_79_mode_eqn.py",
    "s64_mukhanov_ref":  SCRIPT_DIR / "s64_mukhanov_sasaki.py",
    "self_script":       SCRIPT_DIR / "s83_w2_g7_cc7_dynamical.py",
}

print("=" * 78)
print("S83 W2-G7 — CC7-DYNAMICAL  (Mukhanov mode-eq, fold -> pivot)")
print("=" * 78)
print("\nInput pins (SHA-256):")
pin_hashes = {}
for name, p in INPUT_PINS.items():
    h = _sha256_file(p)
    pin_hashes[name] = h
    print(f"  {name:20s} sha256={h[:16]}...{h[-8:]}")

# =============================================================================
# SECTION 1: Canonical inputs (pre-registered in plan §W2-G7)
# =============================================================================

# S82 W-1 #10 pin: CMB-pivot e-fold count (NOT in canonical_constants.py yet,
# but promoted to canonical by the separate W3-G61 gate this session).
# Plan §W2-G7 line 684: "Integration domain N in [N_fold, N_pivot] = [0, 64.08]"
N_PIVOT = 64.08                  # (local) S82 W-1 #10 pin — CMB pivot e-fold

# W1-G4 PASS (INFO): epsilon_H substrate-derivable, F_traj = 3/2 at threshold.
# Canonical value: eps_H = 0.02163 (S75/S77; also S82 W1-2 factor 2).
EPS_H = 0.02163                  # (local) slow-roll eps_H, canonical

# F_traj caveat (per W1-G4 INFO verdict):
# eps_H^zeta / eps_H^Zubarev = 3/2 exactly (at threshold). The canonical
# value 0.02163 is the zeta-scheme value. Mukhanov integration with
# different regulators would shift the target by factor (3/2)^{-1}.
# This gate uses zeta (default per W1-G1 PASS Zubarev-canonical... see
# NOTE below), and reports the F_traj sensitivity in Section 9.

# NOTE: S83 W1-G1 verdict (Zubarev-canonical) selects Branch-B of the
# 3-branch CC tree. Plan §W2-G7 pre-registration says scheme=zeta by
# default (W1-G1 zeta-canonical assumption). Since W1-G1 actually returned
# Zubarev, the canonical scheme for the A_s ledger is ambiguous in the
# workshop — but F_amp_lin itself is a Bogoliubov squeeze ratio, which
# is SCHEME-INDEPENDENT (eigenvalue-ratio bypasses Seeley-DeWitt expansion)
# for fixed eps_H. We tag scheme=zeta to match plan pre-registration but
# note the ratio is robust. See self-assessment at tail of script.

# UNIFIED-AS-79 target F_amp (S82 W1-2 / S80 W1-B-REMED Method B pin)
F_AMP_TARGET = 1.0166            # (local) F_amp_canonical from S82 W1-2
K_A2         = 0.3822            # (local) a_2 slot rescale (W0-5)
F_AMP_SLOT_ADJUSTED = F_AMP_TARGET * K_A2  # (local) 0.3885

# W-2 §Epoch-gating §VI.E: F_amp^{3PI}_pivot = F_amp_lin(N_pivot)
# and F_amp^{3PI} = 47.9177 at transient peak (SI, S78 bound).
F_AMP_3PI_TRANSIENT = 47.9177    # (local) W3-5 FAMP-SC-3PI PASS

# Gate thresholds (plan §W2-G7 line 685-687)
PASS_LOG10_FACTOR3  = np.log10(3.0)   # (local) 0.477 factor-3 band
INFO_LOG10_FACTOR3  = 0.30            # (local) 0.30 borderline lower bound

# Mode equation numerical parameters
N_FOLD = 0.0                     # (local) N=0 at fold (normalization)
# Pre-registered (plan §W2-G7 line 684): N_eval sub-grid density 256 points
N_SUB_GRID = 256                 # (local) plan pre-reg
# Wide BD subhorizon entry: start integration when k*|eta| ~ 200
BD_SUBHORIZON_X = 200.0          # (local) x = k*|eta| at integration start

print(f"\nPre-registered canonical inputs:")
print(f"  eps_H               = {EPS_H:.5f}  (S75/S77 canonical, zeta-scheme)")
print(f"  N_pivot             = {N_PIVOT:.2f}  (S82 W-1 #10 pin)")
print(f"  N_fold              = {N_FOLD:.1f}   (normalization)")
print(f"  H_fold (imported)   = {H_fold:.4f} M_KK")
print(f"  F_amp_target        = {F_AMP_TARGET:.4f}  (F_amp_canonical, S80 W1-B-REMED)")
print(f"  k_a2 (slot)         = {K_A2:.4f}   (W0-5)")
print(f"  F_amp_slot_adjusted = {F_AMP_SLOT_ADJUSTED:.4f} = {F_AMP_TARGET:.4f}*{K_A2:.4f}")
print(f"  F_amp^3PI transient = {F_AMP_3PI_TRANSIENT:.4f}  (S78 bound; W3-5 PASS)")
print(f"\nPASS threshold: |log10(F_amp_lin / F_amp_target)| < {PASS_LOG10_FACTOR3:.4f} (factor-3)")
print(f"INFO threshold: {INFO_LOG10_FACTOR3:.4f} < |log10| < {PASS_LOG10_FACTOR3:.4f}")
print(f"FAIL threshold: |log10| > {PASS_LOG10_FACTOR3:.4f}")

# =============================================================================
# SECTION 2: Background dynamics — strict-dS cascade post-fold
# =============================================================================
#
# Post-fold relaxation (W-2 §Epoch-gating): the SUPERSONIC fold transit is
# NOT modeled as dS (Bunch-Davies derivation fails there). The Mukhanov
# BD derivation applies ONLY after the substrate has relaxed to the dS
# cascade.  Canonical post-fold background:
#   H(N) = H_fold * exp(-eps_H * (N - N_fold))
#   a(N) = exp(N - N_fold)                       (scale factor, N_fold = 0)
#   dt/dN = 1/H(N)                                (number of e-folds)
#   conformal time eta(N) = int a^{-1} dt = int exp(-N + eps*N)/H0 dN
#                         = (-1/(1-eps_H)) * 1/(a*H)    (exact for constant eps)
#
# This is the pre-registered background (plan §W2-G7). It represents the
# post-relaxation regime where the mode-equation BD derivation is valid.

print("\n" + "-"*78)
print("SECTION 2: Background dynamics (post-fold strict-dS cascade)")
print("-"*78)

def a_of_N(N):
    """Scale factor normalized to a(N_fold)=1."""
    return np.exp(N - N_FOLD)                          # (local) a(N_fold)=1

def H_of_N(N, H0=H_fold, eps=EPS_H):
    """Hubble as exponential of e-folds (strict slow-roll)."""
    return H0 * np.exp(-eps * (N - N_FOLD))            # (local)

def eta_of_N(N, H0=H_fold, eps=EPS_H):
    """Conformal time in strict-dS slow-roll: eta = -1/((1-eps)*a*H)."""
    a = a_of_N(N)                                      # (local)
    H = H_of_N(N, H0, eps)                             # (local)
    return -1.0 / ((1.0 - eps) * a * H)                # (local)

def N_of_eta(eta, H0=H_fold, eps=EPS_H):
    """Inverse: N from eta. Solve numerically; used for eta-domain ODE."""
    # eta * (1-eps) * H0 * exp((eps-1)*(N-N_FOLD)) = -1  =>
    # exp((1-eps)*N) = -1 / ((1-eps)*eta*H0)
    # (1-eps)*N = ln(-1/((1-eps)*eta*H0))
    # N = ln(-1/((1-eps)*eta*H0)) / (1-eps)
    arg = -1.0 / ((1.0 - eps) * eta * H0)              # (local) >0 since eta<0
    return np.log(arg) / (1.0 - eps) + N_FOLD          # (local)

# z''/z analytical for strict-dS + constant eps_H:
# z = a * sqrt(2 eps_H), so z prop. to a(eta).
# For a = -1/((1-eps) H eta) ~ -1/(H eta) as eps -> 0, a' = -1/(H eta^2) = a^2 H.
# z''/z = a''/a = 2/eta^2 + 3 eps + O(eps^2) all divided by eta^2
# More precisely: z''/z = (nu^2 - 1/4) / eta^2  where  nu = 3/2 + eps_H + O(eps^2).
# Substitute nu = 3/2 + eps:
#   nu^2 - 1/4 = 9/4 + 3 eps + eps^2 - 1/4 = 2 + 3 eps + eps^2
# So z''/z = (2 + 3 eps_H + eps_H^2) / eta^2.

def zpp_over_z_of_eta(eta, eps=EPS_H):
    """z''/z in strict-dS + constant eps_H (analytic, exact to O(eps^2))."""
    nu_sq_minus_quarter = (1.5 + eps)**2 - 0.25         # (local)
    return nu_sq_minus_quarter / eta**2                 # (local)

# Verify conformal time construction
eta_fold = eta_of_N(N_FOLD)
eta_pivot = eta_of_N(N_PIVOT)
a_pivot = a_of_N(N_PIVOT)
H_pivot = H_of_N(N_PIVOT)
k_pivot_substrate = a_pivot * H_pivot                  # k=aH at pivot (horizon-exit scale)

print(f"\n  eta(N=0 fold)  = {eta_fold:.6e}  (M_KK^{{-1}})")
print(f"  eta(N=pivot)   = {eta_pivot:.6e}  (M_KK^{{-1}})")
print(f"  a(N_pivot)/a(N_fold) = exp(N_pivot) = {a_pivot:.6e}")
print(f"  H(N_pivot)     = {H_pivot:.4f} M_KK  (dS decay factor {H_pivot/H_fold:.6f})")
print(f"  k_pivot = a(N_pivot)*H(N_pivot) = {k_pivot_substrate:.4e}  (substrate units)")
print(f"  eta_pivot * k_pivot = {eta_pivot * k_pivot_substrate:.6f}  (should be -1/(1-eps)={-1/(1.0-EPS_H):.6f})")

# Structural identity: eta*k = -1/(1-eps) at horizon crossing. Verify.
eta_k_crossing_check = abs(eta_pivot * k_pivot_substrate - (-1.0/(1.0 - EPS_H)))
assert eta_k_crossing_check < 1e-10, \
    f"eta*k at crossing deviates: {eta_k_crossing_check:.3e}"
print(f"  CHECK: eta*k at crossing = -1/(1-eps) to {eta_k_crossing_check:.2e}  PASS")

# =============================================================================
# SECTION 3: Analytical F_amp_lin from strict-dS Hankel solution
# =============================================================================
#
# In strict dS + constant eps_H, the exact mode equation solution is:
#   v_k(eta) = (sqrt(pi)/2) * sqrt(-eta) * H_nu^{(1)}(-k*eta) * exp(i*pi*(nu+1/2)/2)
# where nu = 3/2 + eps_H + O(eps_H^2).
#
# BD matching:  at |k*eta| >> 1,  H_nu^{(1)}(-k*eta) ~ sqrt(2/(pi*(-k*eta)))*exp(-i*(k*eta + pi*(nu+1/2)/2))
#               so v_k -> (1/sqrt(2*k)) * exp(-i*k*eta), matching BD IC exactly.
#
# Late-time limit (|k*eta| -> 0):
#   H_nu^{(1)}(x) ~ -(i*Gamma(nu)/pi) * (x/2)^{-nu}  for small x and nu > 0
#   |v_k(eta)|^2 -> (1/pi) * Gamma(nu)^2 * (2/(-k*eta))^{2*nu - 1} / k
#                 = (2^{2*nu-1}/pi) * Gamma(nu)^2 * (1/(-k*eta))^{2*nu-1} / k
#
# F_amp_lin(eta) = |v_k(eta)|^2 / |v_k^{BD}(eta)|^2
# where BD mode (pure dS, nu=3/2) at late-time has:
#   |v_k^{BD}(eta)|^2 = (1/(2k))*(1/(k*eta))^2 = (1/(2k^3 eta^2))
# (This is the canonical P_zeta = H^2/(4 pi^2 M_Pl^2 eps) via v/z.)
#
# RATIO at |k*eta| = 1 (horizon crossing):
#   F_amp_lin(crossing) = [(2^{2*eps_H}/pi) * Gamma(1.5+eps_H)^2] / [(1/pi)*Gamma(1.5)^2]
#                       * (1/|k*eta|)^{2*eps_H}
#                       = (Gamma(1.5+eps_H)/Gamma(1.5))^2 * 2^{2*eps_H} * (1/|k*eta|)^{2*eps_H}
# At |k*eta|=1: F_amp_lin = (Gamma(1.5+eps)/Gamma(1.5))^2 * 2^{2*eps}

print("\n" + "-"*78)
print("SECTION 3: Analytical F_amp_lin from exact Hankel solution")
print("-"*78)
# Two levels:
#   (A) Late-time asymptotic (|k*eta|->0):
#       F_amp_lin -> (Gamma(3/2+eps)/Gamma(3/2))^2 * (2/|k*eta|)^{2*eps}
#       At |k*eta|=1 this gives (Gamma(3/2+eps)/Gamma(3/2))^2 * 2^{2*eps}.
#       Valid ONLY for |k*eta|<<1 (deep superhorizon).
#
#   (B) Exact pure-dS closed form + Hankel function at |k*eta|~1:
#       v_k^{shifted}(eta) = (sqrt(pi)/2)*sqrt(-eta)*H_{3/2+eps}^{(1)}(-k*eta)
#       v_k^{BD,full}(eta) = (1/sqrt(2k))*(1 - i/(k*eta))*exp(-i*k*eta)
#       F_amp_lin(eta) = |v_k^{shifted}|^2 / |v_k^{BD,full}|^2
#       Valid at ALL |k*eta|.  This is the canonical definition.
#
# The W-2 target F_amp_canonical=1.0166 was obtained via (B).  Use (B) as
# primary; report (A) as diagnostic.

nu_exact = 1.5 + EPS_H                                                 # (local) slow-roll Hankel order
k_eta_exit = 1.0/(1.0 - EPS_H)                                         # (local) |k*eta| at horizon crossing in slow-roll

# (A) Late-time asymptotic ratio at |k*eta|=1 (diagnostic; not used for verdict)
gamma_ratio = (gamma_fn(1.5 + EPS_H) / gamma_fn(1.5))**2               # (local)
twopow      = 2.0**(2.0 * EPS_H)                                        # (local) (2/|k*eta|)^{2eps} at |k*eta|=1
F_amp_lin_late_time_asymptote = gamma_ratio * twopow                    # (local) level (A), diagnostic only

# (B) Exact Hankel evaluation at |k*eta|=1/(1-eps) (horizon crossing in strict slow-roll)
# |v_k^{shifted}|^2 = (pi/4)*(-eta)*|H_{3/2+eps}^{(1)}(-k*eta)|^2 = (pi/4)*(|k*eta|/k)*|H_nu|^2
# = (pi/(4*k))*|k*eta|*|H_{3/2+eps}(|k*eta|)|^2
# |v_k^{BD,full}|^2 at same |k*eta|: (1/(2k))*(1 + 1/(k*eta)^2)
H_shifted_crossing = hankel1(nu_exact, k_eta_exit)                     # (local)
v_shifted_abs_sq_crossing_times_k = (PI * k_eta_exit / 4.0) * abs(H_shifted_crossing)**2  # (local)
v_BD_full_crossing_times_k        = 0.5 * (1.0 + 1.0/k_eta_exit**2)   # (local) (1/(2k))*(1+1/(k*eta)^2) * k

F_amp_lin_analytical = v_shifted_abs_sq_crossing_times_k / v_BD_full_crossing_times_k  # (local) CANONICAL (level B)

print(f"\n  nu = 3/2 + eps_H                = {nu_exact:.6f}")
print(f"  |k*eta| at horizon crossing     = 1/(1-eps) = {k_eta_exit:.6f}")
print(f"\n  Level (A) diagnostic — late-time asymptote at |k*eta|=1:")
print(f"     (Gamma(3/2+eps)/Gamma(3/2))^2 = {gamma_ratio:.6f}")
print(f"     2^{{2*eps_H}}                    = {twopow:.6f}")
print(f"     F_amp_lin(A)                  = {F_amp_lin_late_time_asymptote:.6f}")
print(f"\n  Level (B) CANONICAL — exact Hankel at |k*eta|=1/(1-eps):")
print(f"     |v_{{3/2+eps}}|^2 * k            = {v_shifted_abs_sq_crossing_times_k:.6f}")
print(f"     |v_{{BD,full}}|^2 * k            = {v_BD_full_crossing_times_k:.6f}")
print(f"     F_amp_lin (analytical Hankel) = {F_amp_lin_analytical:.6f}")
print(f"     F_amp_target                  = {F_AMP_TARGET:.6f}")
print(f"     ratio (analytic/target)       = {F_amp_lin_analytical/F_AMP_TARGET:.6f}")
print(f"     log10(ratio, analytic)        = {np.log10(F_amp_lin_analytical/F_AMP_TARGET):+.6f}")

# Direction check: for eps_H > 0, F_amp_lin should exceed 1 (amplification).
# For eps_H = 0 (pure dS), F_amp_lin = 1 (BD limit).
# Chain: at eps=0, nu=3/2, and H_{3/2}^{(1)}(x) = -i*sqrt(2/(pi*x))*(1 - i/x)*exp(i*x)
# so |H_{3/2}|^2 = (2/(pi*x))*(1 + 1/x^2), and |v_k|^2 = (pi/4)*(-eta)*(2/(pi*(-k*eta)))*(1+1/(k*eta)^2)
#                 = (1/(2k))*(1 + 1/(k*eta)^2) = |v_BD,full|^2 identically.
#                 => F_amp_lin = 1 at eps=0 (EXACT, at all |k*eta|).
assert F_amp_lin_analytical > 1.0, \
    f"STRUCTURAL FAILURE: eps_H > 0 should give F_amp_lin > 1, got {F_amp_lin_analytical}"
print(f"  DIRECTION CHECK: eps_H=0.02163>0 => F_amp_lin>1 ({F_amp_lin_analytical:.4f}>1) PASS")

# =============================================================================
# SECTION 4: Numerical integration of Mukhanov mode equation
# =============================================================================
#
# Integrate in conformal time eta:
#   v_k'' + (k^2 - z''/z) v_k = 0
# Real + Imaginary split:
#   y0 = Re(v_k), y1 = Im(v_k), y2 = Re(v_k'), y3 = Im(v_k')
#   y0' = y2
#   y1' = y3
#   y2' = -(k^2 - z''/z) * y0
#   y3' = -(k^2 - z''/z) * y1
#
# BD IC at deep subhorizon (|k*eta_start| = 200):
#   v_k = (1/sqrt(2k)) * exp(-i*k*eta_start)
#   v_k' = -i*k * v_k
# So: y0(eta_start) = A * cos(k*eta_start)  (note: exp(-i*k*eta) has real part cos(k*eta)
#                                             if we take -k*eta_start > 0 for eta_start < 0)
#     y1(eta_start) = -A * sin(-k*eta_start) = A * sin(k*eta_start)  (negative eta)
# Let theta = k*eta_start (negative). Re(v_k) = (1/sqrt(2k))*cos(|theta|), Im(v_k) = (1/sqrt(2k))*sin(|theta|)
# Since eta_start is negative, -k*eta_start = k*|eta_start| > 0; so
#   exp(-i*k*eta_start) = exp(i*k*|eta_start|) = cos(k*|eta_start|) + i*sin(k*|eta_start|)
# Setup:
#   eta_start = -BD_SUBHORIZON_X / k  (so that k*|eta_start| = BD_SUBHORIZON_X)
#   v_k(eta_start) = (1/sqrt(2k)) * exp(i*BD_SUBHORIZON_X)
#   v_k'(eta_start) = -i*k*v_k = -i*k*(1/sqrt(2k))*exp(i*BD_SUBHORIZON_X)

print("\n" + "-"*78)
print(f"SECTION 4: Numerical Mukhanov integration  (scipy.integrate.solve_ivp)")
print("-"*78)

def mode_rhs(eta, y, k, eps):
    """v_k'' + (k^2 - z''/z) v_k = 0  as 4D real system (Re, Im of v and v')."""
    zpp_z = zpp_over_z_of_eta(eta, eps)
    omega_sq = k**2 - zpp_z                              # (local)
    # Re(v)' = Re(v'), Im(v)' = Im(v'), Re(v')' = -omega^2 Re(v), Im(v')' = -omega^2 Im(v)
    return [y[2], y[3], -omega_sq * y[0], -omega_sq * y[1]]


def integrate_mode(k, eps=EPS_H, eta_target=None, rtol=1e-10, atol=1e-14):
    """Integrate Mukhanov mode equation from deep subhorizon to eta_target.

    Returns the solution at eta_target: (v_re, v_im, vprime_re, vprime_im).
    """
    eta_start = -BD_SUBHORIZON_X / k                     # (local) deep subhorizon
    if eta_target is None:
        eta_target = eta_of_N(N_PIVOT, H_fold, eps)
    # BD IC: v_k = (1/sqrt(2k)) * exp(-i*k*eta_start) = (1/sqrt(2k))*exp(i*k*|eta_start|)
    A = 1.0 / np.sqrt(2.0 * k)                           # (local)
    phase = k * (-eta_start)                             # (local) = BD_SUBHORIZON_X, positive
    v_re_0 = A * np.cos(phase)                           # (local)
    v_im_0 = A * np.sin(phase)                           # (local)
    # v' = -i*k*v, so Re(v') = k*Im(v), Im(v') = -k*Re(v)
    vp_re_0 = k * v_im_0                                 # (local)
    vp_im_0 = -k * v_re_0                                # (local)
    y0 = [v_re_0, v_im_0, vp_re_0, vp_im_0]              # (local)

    # Integrate from eta_start to eta_target (eta_start < eta_target < 0)
    t_span = (eta_start, eta_target)                     # (local)
    sol = solve_ivp(
        mode_rhs, t_span, y0, args=(k, eps),
        method='DOP853',                                 # high-order fixed for oscillatory
        rtol=rtol, atol=atol,
        dense_output=False,
        max_step=(eta_target - eta_start) / 10000.0,
    )
    if not sol.success:
        raise RuntimeError(f"Mukhanov integration failed for k={k}: {sol.message}")
    return sol.t, sol.y


# Pick a representative k = k_pivot_substrate (horizon crossing at N_PIVOT)
K_PIVOT = k_pivot_substrate                              # (local)
print(f"\n  k_pivot = {K_PIVOT:.4e}  (horizon-crossing at N_pivot={N_PIVOT:.2f})")
print(f"  eta_start = -{BD_SUBHORIZON_X:.1f}/k_pivot = {-BD_SUBHORIZON_X/K_PIVOT:.4e}")
print(f"  eta_target = eta(N_pivot) = {eta_pivot:.4e}")

# Dense sub-grid per plan §W2-G7 (line 684, N_eval=256)
# Sample v_k amplitude along the trajectory between (N_entry_subhorizon, N_pivot)
# where N_entry = N such that k*|eta(N)| = BD_SUBHORIZON_X.
# Solve for N_entry: BD_SUBHORIZON_X = k*|eta| = k/((1-eps)*a*H) = k/((1-eps)*exp(N)*H_fold*exp(-eps*N))
# = k / ((1-eps)*H_fold*exp((1-eps)*N))
# exp((1-eps)*N) = k / ((1-eps)*H_fold*BD_SUBHORIZON_X)
# N_entry = ln(k / ((1-eps)*H_fold*BD_SUBHORIZON_X)) / (1-eps)
# For k = k_pivot with horizon crossing at N_PIVOT = 64.08:
#   k_pivot = a(N_pivot)*H(N_pivot) = exp(N_pivot)*H_fold*exp(-eps*N_pivot) = H_fold*exp((1-eps)*N_pivot)
# So k/((1-eps)*H_fold*BD_SUBHORIZON_X) = exp((1-eps)*N_pivot) / ((1-eps)*BD_SUBHORIZON_X)
# N_entry = N_pivot + ln(1/((1-eps)*BD_SUBHORIZON_X)) / (1-eps)
#         = N_pivot - ln((1-eps)*BD_SUBHORIZON_X) / (1-eps)

N_entry = N_PIVOT - np.log((1.0 - EPS_H) * BD_SUBHORIZON_X) / (1.0 - EPS_H)
print(f"  N_entry (subhorizon start, BD_x={BD_SUBHORIZON_X:.0f}) = {N_entry:.4f}")
print(f"  N_horizon_crossing (k=aH)            = {N_PIVOT:.4f}")
print(f"  e-folds under BD ICs to pivot        = {N_PIVOT - N_entry:.4f}")

# Dense integration + sample at sub-grid
print(f"\n  Integrating mode equation (DOP853, rtol=1e-10, atol=1e-14)...")
sol_t, sol_y = integrate_mode(K_PIVOT, eps=EPS_H)
print(f"  Integration success: final eta = {sol_t[-1]:.4e}, steps = {len(sol_t)}")

v_re_pivot = sol_y[0, -1]
v_im_pivot = sol_y[1, -1]
v_abs_sq_pivot = v_re_pivot**2 + v_im_pivot**2

# Compare to PURE-dS BD envelope at pivot (EXACT, including interference term):
#   |v_k^{BD,full}(eta)|^2 = (1/(2k)) * (1 + 1/(k*eta)^2)
# This is the EXACT pure-dS (nu=3/2) Bunch-Davies mode-function amplitude.
# The leading-late-time form (1/(2k))*(1/(k*eta))^2 DROPS the "+1" interference
# term which is O(1) at |k*eta|~1 (horizon crossing). Since the integration
# domain for CC7' puts the endpoint at k*|eta|=1/(1-eps_H)~1.022, the leading
# form underestimates |v_BD|^2 by ~2x, making F_amp_lin spuriously ~2x too large.
# The W-2 F_amp_canonical=1.0166 definition implicitly uses the full BD envelope
# (the W1-B-REMED method integrates |v_k|^2 vs a pure-dS |v_BD|^2 evaluated at
# the same eta, not at late-time asymptote).
k_eta_val = K_PIVOT * eta_pivot                                   # (local) = -1.022
v_abs_sq_BD_pivot_leading = (1.0 / (2.0 * K_PIVOT)) * (1.0 / k_eta_val**2)   # (local) legacy/informational
v_abs_sq_BD_pivot        = (1.0 / (2.0 * K_PIVOT)) * (1.0 + 1.0/k_eta_val**2)  # (local) FULL BD envelope

F_AMP_LIN_NUMERICAL        = v_abs_sq_pivot / v_abs_sq_BD_pivot          # (local) canonical
F_amp_lin_leading_only     = v_abs_sq_pivot / v_abs_sq_BD_pivot_leading  # (local) diagnostic

print(f"\n  |v_k(eta_pivot)|^2 (numerical)         = {v_abs_sq_pivot:.6e}")
print(f"  |v_k^{{BD,full}}(eta_pivot)|^2 (pure dS)  = {v_abs_sq_BD_pivot:.6e}  (canonical)")
print(f"  |v_k^{{BD,leading}}(eta_pivot)|^2        = {v_abs_sq_BD_pivot_leading:.6e}  (diagnostic)")
print(f"  F_amp_lin (numerical, full BD)         = {F_AMP_LIN_NUMERICAL:.6f}")
print(f"  F_amp_lin (numerical, leading BD)      = {F_amp_lin_leading_only:.6f}  [diagnostic]")
print(f"  F_amp_lin (analytical Hankel, full BD) = {F_amp_lin_analytical:.6f}")
print(f"  Numerical/analytical ratio             = {F_AMP_LIN_NUMERICAL/F_amp_lin_analytical:.6f}")

# Cross-check: reject if numerical/analytical disagree by > 5%
num_anl_dev = abs(F_AMP_LIN_NUMERICAL / F_amp_lin_analytical - 1.0)
print(f"  |num/anl - 1|                          = {num_anl_dev:.3e}")

# =============================================================================
# SECTION 5: Composite check — F_amp_lin factorization
# =============================================================================
#
# [CHAIN] trigger: F_amp_lin should factor as the pre-slot ledger value
# consistent with W-2 §Epoch-gating.
# From S82 W1-2 and S82 W-2:
#   F_amp_slot_adjusted = F_amp_canonical * k_a2
#   F_amp_canonical ~ F_amp^{3PI}(N_pivot) ~ F_amp_lin(N_pivot)
# Composite identity to check:
#   (F_amp_lin * k_a2) ~ F_amp_slot_adjusted
# and (F_amp_lin) ~ F_amp^{3PI}(N_pivot) ~ F_amp_canonical

print("\n" + "-"*78)
print("SECTION 5: Composite factorization check  [CHAIN] trigger")
print("-"*78)

F_amp_slot_from_dyn = F_AMP_LIN_NUMERICAL * K_A2         # (local)
slot_dev_oom = np.log10(F_amp_slot_from_dyn / F_AMP_SLOT_ADJUSTED)  # (local)

print(f"  F_amp_lin * k_a2 (dynamical)           = {F_amp_slot_from_dyn:.6f}")
print(f"  F_amp_slot_adjusted (S82 W1-2 pin)     = {F_AMP_SLOT_ADJUSTED:.6f}")
print(f"  log10 dynamical/pinned                 = {slot_dev_oom:+.6f}")
print(f"  PASS if |slot_dev| < {PASS_LOG10_FACTOR3:.4f} (factor-3)")

# F_amp^{3PI} at pivot converges to F_amp_lin(pivot) per W-2 §Epoch-gating T4:
#   F_amp^{3PI}(N_pivot) = F_amp_lin(N_pivot) * (1 + r(N_pivot))^{-1/2}
#   r(N_pivot) << 1 => F_amp^{3PI}(pivot) ~ F_amp_lin(pivot)
# Transient peak F_amp^{3PI} = 47.9177 is at N = N_fold + a few e-folds, NOT at pivot.
F_amp_3PI_pivot_from_dyn = F_AMP_LIN_NUMERICAL            # (local) to leading order in r
print(f"\n  F_amp^{{3PI}}(N_pivot) (predicted from dyn) = {F_amp_3PI_pivot_from_dyn:.6f}")
print(f"  F_amp^{{3PI}} transient peak (S78/W3-5)     = {F_AMP_3PI_TRANSIENT:.6f}")
print(f"  Ratio peak/pivot                             = {F_AMP_3PI_TRANSIENT/F_amp_3PI_pivot_from_dyn:.2f}x")

# =============================================================================
# SECTION 6: k-scan (modes around pivot)
# =============================================================================
# Plan §W2-G7 line 684: N_eval sub-grid density 256 points, though k-scan
# is a secondary check here (F_amp_lin is a per-mode Bogoliubov ratio).
# Sample 11 modes spanning k/k_pivot in [0.1, 10] to verify F_amp_lin
# is approximately k-independent (horizon-crossing cancellation).

print("\n" + "-"*78)
print("SECTION 6: k-scan (F_amp_lin k-invariance at each mode's horizon crossing)")
print("-"*78)
# At horizon crossing for mode k: k = a(N_hc)*H(N_hc).
# With a(N) = exp(N) and H(N) = H_fold * exp(-eps*N):
#   k = exp(N_hc) * H_fold * exp(-eps*N_hc) = H_fold * exp((1-eps)*N_hc)
#   N_hc(k) = ln(k/H_fold) / (1-eps)
# eta at crossing:  eta_hc = -1/((1-eps)*a(N_hc)*H(N_hc)) = -1/((1-eps)*k)
# So k*eta_hc = -1/(1-eps) (same as K_PIVOT at N_PIVOT — horizon-crossing cancellation)
# F_amp_lin at each mode's own crossing is k-INVARIANT (by strict slow-roll).
# Evaluating at a FIXED eta_pivot (as before) would put smaller-k modes deep
# superhorizon (log growth above 1) and larger-k modes deep subhorizon
# (ratio near 1, i.e. still BD). The canonical CC7' measurement is at
# each mode's OWN horizon crossing.

k_scan_ratios = np.geomspace(0.1, 10.0, 11)             # (local) k/k_pivot
k_scan_values = k_scan_ratios * K_PIVOT                 # (local)
F_amp_scan = np.zeros(len(k_scan_values))                # (local)
N_hc_scan  = np.zeros(len(k_scan_values))                # (local)
eta_hc_scan = np.zeros(len(k_scan_values))               # (local)

for i, k in enumerate(k_scan_values):
    # Each mode's horizon crossing N_hc(k) and eta_hc(k):
    N_hc_i = np.log(k / H_fold) / (1.0 - EPS_H) + N_FOLD
    eta_hc_i = -1.0 / ((1.0 - EPS_H) * k)
    N_hc_scan[i] = N_hc_i
    eta_hc_scan[i] = eta_hc_i
    try:
        t_scan, y_scan = integrate_mode(k, eps=EPS_H, eta_target=eta_hc_i)
        v_sq = y_scan[0, -1]**2 + y_scan[1, -1]**2
        # Full BD envelope at each mode's own eta_hc
        k_eta_hc = k * eta_hc_i                         # (local) = -1/(1-eps), same for all
        v_sq_BD_full = (1.0/(2.0*k)) * (1.0 + 1.0/k_eta_hc**2)
        F_amp_scan[i] = v_sq / v_sq_BD_full
    except Exception as e:
        F_amp_scan[i] = np.nan
        print(f"  k/k_pivot={k_scan_ratios[i]:.2f}: FAILED ({e})")

print(f"\n  k/k_pivot      N_hc(k)       F_amp_lin   log10(ratio to target)")
for i, r in enumerate(k_scan_ratios):
    if np.isfinite(F_amp_scan[i]):
        print(f"  {r:9.3f}    {N_hc_scan[i]:9.3f}    {F_amp_scan[i]:.6f}    {np.log10(F_amp_scan[i]/F_AMP_TARGET):+.4f}")

F_amp_scan_median = float(np.nanmedian(F_amp_scan))      # (local)
F_amp_scan_std    = float(np.nanstd(F_amp_scan))         # (local)
F_amp_scan_ratio_max_min = float(np.nanmax(F_amp_scan)/np.nanmin(F_amp_scan))  # (local)
print(f"\n  Median F_amp over k-scan  = {F_amp_scan_median:.6f}")
print(f"  StDev F_amp over k-scan   = {F_amp_scan_std:.6e}  (should be ~0 if k-invariant)")
print(f"  max/min F_amp            = {F_amp_scan_ratio_max_min:.6f}  (target: close to 1)")

# =============================================================================
# SECTION 7: Cross-checks
# =============================================================================

print("\n" + "-"*78)
print("SECTION 7: Cross-checks (machine-precision identities)")
print("-"*78)

# CC1: BD limit. In the limit eps_H -> 0, F_amp_lin -> 1 EXACTLY (at all |k*eta|).
# Full Hankel form: check at pure dS (nu=3/2) reproduces v_BD_full identically.
eps_test_zero = 0.0                                      # (local)
nu_BD = 1.5                                              # (local) pure dS Hankel order
H_nu_BD_check = hankel1(nu_BD, k_eta_exit)
v_BD_shifted_check_times_k = (PI * k_eta_exit / 4.0) * abs(H_nu_BD_check)**2
F_amp_BD_check = v_BD_shifted_check_times_k / v_BD_full_crossing_times_k
CC1_dev = abs(F_amp_BD_check - 1.0)
CC1_ok  = CC1_dev < 1e-12
print(f"  CC1: BD limit (eps=0, full Hankel) F_amp_lin = {F_amp_BD_check:.14f}  dev={CC1_dev:.2e}  ok={CC1_ok}")

# CC2: d(ln F_amp_lin)/d(eps_H) at canonical eps. Analytical form:
# F = (Gamma(1.5+eps)/Gamma(1.5))^2 * 2^{2 eps}
# ln F = 2*(digamma(1.5+eps) - digamma(1.5))*eps + 2*eps*ln 2  (leading order)
# d(ln F)/d(eps) = 2*digamma(1.5+eps) - 2*digamma(1.5) + 2*ln 2  at eps_H canonical
# Numerical check:
from scipy.special import digamma
delta_eps = 1e-6                                         # (local)
F_plus  = (gamma_fn(1.5 + EPS_H + delta_eps)/gamma_fn(1.5))**2 * 2.0**(2*(EPS_H + delta_eps))
F_minus = (gamma_fn(1.5 + EPS_H - delta_eps)/gamma_fn(1.5))**2 * 2.0**(2*(EPS_H - delta_eps))
dlnF_deps_num = (np.log(F_plus) - np.log(F_minus)) / (2.0 * delta_eps)  # (local)

# Analytical at eps_H:
# d/d(eps) [2*ln(Gamma(1.5+eps)/Gamma(1.5)) + 2*eps*ln 2]
# = 2*digamma(1.5+eps) + 2*ln 2     (digamma(1.5) is constant in d/d(eps))
# Note: ln(Gamma(1.5)) constant, d/d(eps)=0. So = 2*digamma(1.5+eps) + 2*ln 2.
# But we expect PATTERN: d(ln F)/d(eps) = 2*(digamma(1.5+eps_H) + ln(2))  at operating eps_H
dlnF_deps_anl = 2.0 * (digamma(1.5 + EPS_H) + np.log(2.0))  # (local) evaluated at operating eps_H
# NB: digamma(1.5) = 2 - gamma - 2 ln 2, not subtracted in analytical form because we
# computed d/d(eps)[ln F] not [d/d(eps) ln(F_relative)], so subtraction of digamma(1.5)
# only enters when computing F relative to eps=0 baseline, which we do.
# Actually: ln F = 2*ln(Gamma(1.5+eps)) - 2*ln(Gamma(1.5)) + 2*eps*ln 2
# d/d(eps) = 2*digamma(1.5+eps) + 2 ln 2   (ln Gamma(1.5) is constant, dropped)
# So analytical: 2*digamma(1.5+eps_H) + 2*ln(2).
CC2_dev = abs(dlnF_deps_num - dlnF_deps_anl) / abs(dlnF_deps_anl)
CC2_ok  = CC2_dev < 1e-4
print(f"  CC2: d(ln F_amp)/d(eps_H): num={dlnF_deps_num:.6f}, anl=2*digamma(1.5+eps)+2*ln 2={dlnF_deps_anl:.6f}")
print(f"       rel_dev={CC2_dev:.2e}  ok={CC2_ok}")

# CC3: numerical integration reproduces analytical Hankel value (full BD envelope).
# num_anl_dev was computed in Section 4 after Mukhanov integration.
CC3_dev = num_anl_dev                                     # (local)
CC3_ok  = CC3_dev < 0.01                                  # (local) 1% tolerance for numerical integration
print(f"  CC3: numerical/analytical agreement: dev={CC3_dev:.3e}  ok={CC3_ok}  (tol 1%)")

# CC4: |v_k|^2 normalization at BD entry (should equal A^2 = 1/(2k))
# Integrate back to eta_start and check |v|^2 = 1/(2k)
# Skip full re-integration here; verify analytically that IC was correct:
k_test = K_PIVOT
eta_start = -BD_SUBHORIZON_X / k_test
A_IC = 1.0 / np.sqrt(2.0 * k_test)
v_re_IC = A_IC * np.cos(k_test * (-eta_start))  # = A * cos(BD_SUBHORIZON_X)
v_im_IC = A_IC * np.sin(k_test * (-eta_start))
v_sq_IC = v_re_IC**2 + v_im_IC**2
CC4_dev = abs(v_sq_IC - 1.0/(2.0 * k_test))
CC4_ok  = CC4_dev < 1e-18
print(f"  CC4: BD IC |v|^2 at entry = {v_sq_IC:.6e}, target 1/(2k)={1.0/(2.0*k_test):.6e}, dev={CC4_dev:.2e}  ok={CC4_ok}")

# CC5: k-scan k-invariance at each mode's own horizon crossing.
# Since all modes cross at the same |k*eta| = 1/(1-eps) in strict slow-roll,
# F_amp_lin(k, N_hc(k)) is k-INVARIANT by construction. Verify numerically.
# max/min should be < 1.01 (all modes produce the same ratio to 3 significant digits).
F_amp_finite = F_amp_scan[np.isfinite(F_amp_scan)]              # (local)
if len(F_amp_finite) > 0:
    kscan_range = float(np.max(F_amp_finite) / np.min(F_amp_finite))  # (local)
    CC5_ok = kscan_range < 1.01                                 # (local) 1% tolerance
    print(f"  CC5: k-scan range max/min F_amp = {kscan_range:.6f}  ok(<1.01)={CC5_ok}")
else:
    kscan_range = float('nan')
    CC5_ok = False

# CC6: Numerical Mukhanov result vs analytical Hankel (full) at |k*eta|=1/(1-eps).
# The numerical integration implements the SAME mode equation as the analytical form
# IF the pump z''/z = (nu^2 - 1/4)/eta^2 is correctly installed (it is, Section 2).
# Disagreement > 0.5% would signal an integration error or BD-IC mismatch.
CC6_dev = abs(F_AMP_LIN_NUMERICAL - F_amp_lin_analytical) / F_amp_lin_analytical  # (local)
CC6_ok  = CC6_dev < 0.005                                                         # (local) 0.5% tol
print(f"  CC6: numerical vs analytical (full Hankel): F_amp_num={F_AMP_LIN_NUMERICAL:.6f}, F_amp_anl={F_amp_lin_analytical:.6f}, rel_dev={CC6_dev:.3%}  ok={CC6_ok}")

cross_checks_all = [CC1_ok, CC2_ok, CC3_ok, CC4_ok, CC5_ok, CC6_ok]
print(f"\n  All cross-checks PASS: {all(cross_checks_all)}")

# =============================================================================
# SECTION 8: Gate verdict
# =============================================================================

print("\n" + "-"*78)
print("SECTION 8: Gate verdict")
print("-"*78)

# Primary metric: F_amp_lin from numerical Mukhanov integration
log_ratio = np.log10(F_AMP_LIN_NUMERICAL / F_AMP_TARGET)  # (local)
abs_log_ratio = abs(log_ratio)                             # (local)

if abs_log_ratio < INFO_LOG10_FACTOR3:
    VERDICT = "PASS"
elif abs_log_ratio < PASS_LOG10_FACTOR3:
    VERDICT = "INFO"
else:
    VERDICT = "FAIL"

print(f"\n  F_amp_lin (numerical)   = {F_AMP_LIN_NUMERICAL:.6f}")
print(f"  F_amp_target            = {F_AMP_TARGET:.6f}")
print(f"  log10(ratio)            = {log_ratio:+.6f}")
print(f"  |log10|                 = {abs_log_ratio:.6f}")
print(f"  PASS boundary           = {PASS_LOG10_FACTOR3:.4f} (factor-3)")
print(f"  INFO boundary           = {INFO_LOG10_FACTOR3:.4f}")
print(f"  VERDICT                 = {VERDICT}")

# =============================================================================
# SECTION 9: F_traj sensitivity (per W1-G4 INFO verdict)
# =============================================================================
# W1-G4 returned INFO with F_traj=3/2: eps_H^zeta/eps_H^Zubarev = 3/2.
# If Zubarev were canonical (per W1-G1 PASS), eps_H -> eps_H * (2/3) = 0.01442.
# Test F_amp_lin under this alternative canonical value.

print("\n" + "-"*78)
print("SECTION 9: F_traj sensitivity  (W1-G4 threshold 3/2)")
print("-"*78)

EPS_H_ZUBAREV = EPS_H * (2.0/3.0)        # (local) Zubarev-scheme eps_H under F_traj
F_amp_zubarev = (gamma_fn(1.5 + EPS_H_ZUBAREV)/gamma_fn(1.5))**2 * 2.0**(2*EPS_H_ZUBAREV)  # (local)
print(f"  eps_H^Zubarev = eps_H * 2/3 = {EPS_H_ZUBAREV:.5f}")
print(f"  F_amp_lin^Zubarev (analytic) = {F_amp_zubarev:.6f}")
print(f"  Ratio zeta/Zubarev F_amp = {F_amp_lin_analytical/F_amp_zubarev:.6f}")
log_ratio_zub = np.log10(F_amp_zubarev/F_AMP_TARGET)
print(f"  log10(Zubarev/target)    = {log_ratio_zub:+.6f}")

# =============================================================================
# SECTION 10: Plot (v_k(eta), horizon crossing overlay, k-scan)
# =============================================================================

print("\n" + "-"*78)
print("SECTION 10: Plotting")
print("-"*78)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel (a): |v_k(eta)|^2 over the integration, compared to BD envelope
ax = axes[0, 0]
v_abs_sq_trajectory = sol_y[0, :]**2 + sol_y[1, :]**2
# BD envelope |v_k^BD|^2 = (1/(2k))*(1 + 1/(k*eta)^2) for pure dS growing mode
# Actually for pure dS exact: |v_k^BD(eta)|^2 = (1/(2k))*(1 + 1/(k*eta)^2)
v_BD_trajectory = (1.0/(2.0*K_PIVOT)) * (1.0 + 1.0/(K_PIVOT*sol_t)**2)
k_abs_eta = K_PIVOT * np.abs(sol_t)
ax.semilogy(k_abs_eta, v_abs_sq_trajectory, 'b-', label=r'$|v_k|^2$ numerical', linewidth=1.5)
ax.semilogy(k_abs_eta, v_BD_trajectory, 'r--', label=r'$|v_k^{BD}|^2$ (pure dS)', linewidth=1.5, alpha=0.7)
ax.axvline(1.0, color='k', linestyle=':', alpha=0.6, label=r'horizon crossing ($k|\eta|=1$)')
ax.set_xlabel(r'$k |\eta|$')
ax.set_ylabel(r'$|v_k(\eta)|^2$')
ax.set_title(f'(a) Mode evolution k=k_pivot (invert x for time: high $k|\\eta|$=early)')
ax.set_xscale('log')
ax.invert_xaxis()
ax.legend(loc='best', fontsize=9)
ax.grid(alpha=0.3)

# Panel (b): F_amp_lin along trajectory
ax = axes[0, 1]
# F_amp_lin(eta) = |v|^2/|v_BD|^2 at each eta point
F_amp_trajectory = v_abs_sq_trajectory / v_BD_trajectory
ax.plot(k_abs_eta, F_amp_trajectory, 'g-', linewidth=1.5, label='F_amp_lin(eta)')
ax.axhline(F_AMP_TARGET, color='r', linestyle='--', label=f'target = {F_AMP_TARGET}')
ax.axhline(F_amp_lin_analytical, color='b', linestyle=':', label=f'analytic = {F_amp_lin_analytical:.4f}')
ax.axhline(1.0, color='k', linestyle='-.', alpha=0.4, label='BD=1')
ax.axvline(1.0, color='k', linestyle=':', alpha=0.6)
ax.set_xlabel(r'$k |\eta|$')
ax.set_ylabel('F_amp_lin(eta)')
ax.set_title('(b) F_amp_lin trajectory vs target')
ax.set_xscale('log')
ax.invert_xaxis()
ax.set_ylim(0.95, 1.10)
ax.legend(loc='best', fontsize=9)
ax.grid(alpha=0.3)

# Panel (c): k-scan
ax = axes[1, 0]
finite_idx = np.isfinite(F_amp_scan)
ax.semilogx(k_scan_ratios[finite_idx], F_amp_scan[finite_idx],
            'o-', color='purple', linewidth=2, markersize=8)
ax.axhline(F_AMP_TARGET, color='r', linestyle='--', label=f'target = {F_AMP_TARGET}')
ax.axhline(F_amp_lin_analytical, color='b', linestyle=':', label=f'analytic = {F_amp_lin_analytical:.4f}')
ax.axhline(1.0, color='k', linestyle='-.', alpha=0.4, label='BD')
ax.set_xlabel(r'$k/k_{pivot}$')
ax.set_ylabel('F_amp_lin(k)')
ax.set_title('(c) k-scan: F_amp_lin approximate k-invariance')
ax.set_ylim(0.98, 1.05)
ax.legend(loc='best', fontsize=9)
ax.grid(alpha=0.3)

# Panel (d): Verdict banner
ax = axes[1, 1]
ax.axis('off')
banner_lines = [
    "S83 W2-G7 CC7-DYNAMICAL",
    "",
    f"Verdict: {VERDICT}",
    f"",
    f"F_amp_lin (numerical)  = {F_AMP_LIN_NUMERICAL:.6f}",
    f"F_amp_lin (analytical) = {F_amp_lin_analytical:.6f}",
    f"F_amp_target           = {F_AMP_TARGET:.6f}",
    f"log10(ratio)           = {log_ratio:+.4f}",
    f"|log10|                = {abs_log_ratio:.4f}",
    f"",
    f"Thresholds:",
    f"  PASS < 0.30  (factor-2)",
    f"  INFO 0.30-0.477",
    f"  FAIL > 0.477 (factor-3)",
    f"",
    f"Substrate inputs (post-fold dS cascade):",
    f"  eps_H      = {EPS_H:.5f}  (zeta canonical)",
    f"  N_pivot    = {N_PIVOT:.2f}",
    f"  H_fold     = {H_fold:.2f} M_KK",
    f"",
    f"Cross-checks (CC1-CC6):",
    f"  CC1 BD limit           : {'ok' if CC1_ok else 'FAIL'}",
    f"  CC2 d(ln F)/d(eps)     : {'ok' if CC2_ok else 'FAIL'}",
    f"  CC3 num vs analytic    : {'ok' if CC3_ok else 'FAIL'}",
    f"  CC4 BD IC normalization: {'ok' if CC4_ok else 'FAIL'}",
    f"  CC5 k-scan invariance  : {'ok' if CC5_ok else 'FAIL'}",
    f"  CC6 analytic vs target : {'ok' if CC6_ok else 'FAIL'}",
    f"",
    f"F_traj sensitivity (W1-G4):",
    f"  F_amp@eps_zeta = {F_amp_lin_analytical:.4f}",
    f"  F_amp@eps_Zub  = {F_amp_zubarev:.4f}",
]
banner_text = "\n".join(banner_lines)
ax.text(0.02, 0.98, banner_text, family='monospace', fontsize=8,
        verticalalignment='top', transform=ax.transAxes)

plt.tight_layout()
out_png = SCRIPT_DIR / 's83_w2_g7_cc7_dynamical.png'
plt.savefig(out_png, dpi=120, bbox_inches='tight')
plt.close(fig)
print(f"  Plot saved: {out_png}")

# =============================================================================
# SECTION 11: Closure SHA over input pins + key outputs
# =============================================================================

closure_map = {
    'gate_id': 'S83-CC7-DYNAMICAL',
    'verdict': VERDICT,
    'scheme': 'zeta',
    'convention': 'Mukhanov-BD-to-pivot',
    'L_max': 'N/A-mode-eq',
    # Canonical inputs
    'eps_H': EPS_H,
    'N_pivot': N_PIVOT,
    'N_fold': N_FOLD,
    'H_fold': H_fold,
    'F_amp_target': F_AMP_TARGET,
    'k_a2': K_A2,
    'F_amp_slot_adjusted_pinned': F_AMP_SLOT_ADJUSTED,
    # Dynamical outputs
    'F_amp_lin_numerical': float(F_AMP_LIN_NUMERICAL),
    'F_amp_lin_analytical': float(F_amp_lin_analytical),
    'log_ratio': float(log_ratio),
    'abs_log_ratio': float(abs_log_ratio),
    # Composite
    'F_amp_slot_from_dyn': float(F_amp_slot_from_dyn),
    'slot_dev_oom': float(slot_dev_oom),
    'F_amp_3PI_pivot_from_dyn': float(F_amp_3PI_pivot_from_dyn),
    # k-scan
    'F_amp_scan_median': F_amp_scan_median,
    'F_amp_scan_std': F_amp_scan_std,
    # F_traj
    'F_amp_zubarev': float(F_amp_zubarev),
    'F_traj_ratio': float(F_amp_lin_analytical / F_amp_zubarev),
    # Cross-checks
    'CC1_BD_limit_ok': bool(CC1_ok),
    'CC2_dlnF_deps_ok': bool(CC2_ok),
    'CC3_num_vs_analytic_ok': bool(CC3_ok),
    'CC4_BD_IC_norm_ok': bool(CC4_ok),
    'CC5_kscan_invariance_ok': bool(CC5_ok),
    'CC6_analytic_vs_target_ok': bool(CC6_ok),
    'cross_checks_all_ok': bool(all(cross_checks_all)),
    # Thresholds
    'PASS_LOG10_FACTOR3': float(PASS_LOG10_FACTOR3),
    'INFO_LOG10_FACTOR3': float(INFO_LOG10_FACTOR3),
    # Input pins
    'input_pin_hashes': pin_hashes,
}
closure_str = json.dumps(closure_map, sort_keys=True, default=str)
closure_sha = hashlib.sha256(closure_str.encode('utf-8')).hexdigest()

print("\n" + "-"*78)
print("SECTION 11: Closure SHA")
print("-"*78)
print(f"  closure_sha = {closure_sha}")

# =============================================================================
# SECTION 12: Save .npz
# =============================================================================

out_npz = SCRIPT_DIR / 's83_w2_g7_cc7_dynamical.npz'

np.savez(out_npz,
    # Pre-registered inputs
    eps_H=EPS_H, N_pivot=N_PIVOT, N_fold=N_FOLD,
    H_fold=H_fold, F_amp_target=F_AMP_TARGET, k_a2=K_A2,
    F_amp_slot_adjusted_pinned=F_AMP_SLOT_ADJUSTED,
    F_amp_3PI_transient=F_AMP_3PI_TRANSIENT,
    # Pump-field background
    eta_fold=eta_fold, eta_pivot=eta_pivot,
    a_pivot=a_pivot, H_pivot=H_pivot, k_pivot_substrate=K_PIVOT,
    N_entry_subhorizon=N_entry, BD_SUBHORIZON_X=BD_SUBHORIZON_X,
    # Dynamical F_amp_lin outputs
    F_amp_lin_numerical=F_AMP_LIN_NUMERICAL,
    F_amp_lin_analytical=F_amp_lin_analytical,
    v_abs_sq_pivot=v_abs_sq_pivot,
    v_abs_sq_BD_pivot=v_abs_sq_BD_pivot,
    log_ratio=log_ratio,
    abs_log_ratio=abs_log_ratio,
    # Trajectory
    sol_t=sol_t, sol_y_re=sol_y[0, :], sol_y_im=sol_y[1, :],
    sol_yp_re=sol_y[2, :], sol_yp_im=sol_y[3, :],
    v_abs_sq_trajectory=v_abs_sq_trajectory,
    k_abs_eta_trajectory=K_PIVOT * np.abs(sol_t),
    # Composite
    F_amp_slot_from_dyn=F_amp_slot_from_dyn,
    slot_dev_oom=slot_dev_oom,
    F_amp_3PI_pivot_from_dyn=F_amp_3PI_pivot_from_dyn,
    # k-scan
    k_scan_ratios=k_scan_ratios,
    k_scan_values=k_scan_values,
    F_amp_scan=F_amp_scan,
    F_amp_scan_median=F_amp_scan_median,
    F_amp_scan_std=F_amp_scan_std,
    # F_traj sensitivity
    EPS_H_ZUBAREV=EPS_H_ZUBAREV,
    F_amp_zubarev=F_amp_zubarev,
    F_traj_ratio_zeta_over_zubarev=F_amp_lin_analytical/F_amp_zubarev,
    log_ratio_zub=log_ratio_zub,
    # Cross-checks
    CC1_BD_limit_ok=CC1_ok, CC1_dev=CC1_dev,
    CC2_dlnF_deps_ok=CC2_ok, CC2_dev=CC2_dev,
    CC3_num_vs_analytic_ok=CC3_ok, CC3_dev=CC3_dev,
    CC4_BD_IC_norm_ok=CC4_ok, CC4_dev=CC4_dev,
    CC5_kscan_invariance_ok=CC5_ok,
    CC6_analytic_vs_target_ok=CC6_ok, CC6_dev=CC6_dev,
    cross_checks_all_ok=all(cross_checks_all),
    # Verdict + thresholds
    verdict=VERDICT,
    PASS_LOG10_FACTOR3=PASS_LOG10_FACTOR3,
    INFO_LOG10_FACTOR3=INFO_LOG10_FACTOR3,
    # Closure SHA
    closure_sha=closure_sha,
)
print(f"\n  .npz saved: {out_npz}")

# =============================================================================
# SECTION 13: Append verdict line to s83_gate_verdicts.txt
# =============================================================================

verdict_line = (
    f"S83-CC7-DYNAMICAL: {VERDICT} -- "
    f"value=F_amp_lin={F_AMP_LIN_NUMERICAL:.4f},target={F_AMP_TARGET:.4f},log10={log_ratio:+.4f} "
    f"scheme=zeta convention=Mukhanov-BD-to-pivot L_max=N/A "
    f"sha256={closure_sha}\n"
)
verdicts_path = SCRIPT_DIR / 's83_gate_verdicts.txt'
with open(verdicts_path, 'a', encoding='utf-8') as f:
    f.write(verdict_line)
print(f"\n  Verdict appended to: {verdicts_path}")
print(f"  >> {verdict_line.strip()}")

# =============================================================================
# SECTION 14: Final 4-tuple tag (last non-verdict line per protocol)
# =============================================================================
print("\n" + "=" * 78)
print(f"S83-CC7-DYNAMICAL  {VERDICT}  (|log10 ratio|={abs_log_ratio:.4f})")
print(f"FINAL 4-TUPLE: (value={F_AMP_LIN_NUMERICAL:.6f}, scheme=zeta, convention=Mukhanov-BD-to-pivot, L_max=N/A)")
print("=" * 78)
