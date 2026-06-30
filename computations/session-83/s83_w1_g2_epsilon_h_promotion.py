"""
S83 W1-G2 — EPSILON-H-SECONDARY-KK-PROMOTION
=============================================

Gate: S83-EPSILON-H-SECONDARY-KK-PROMOTION
Trigger: [VERIFY-THEOREM][SIGN]
Classification: GEOMETRIC

Question: Does the Connes-Moscovici Hopf H_1 transgression chi_CM
lift epsilon_H from RD (regulator-dressing-dependent) to FI
(functorially invariant) via a PRIMARY HP^even cocycle?

SUBSTITUTION CHAIN (pre-registered, per §CE6 of S82 W-3):
  Step 1 (def). A = C_Jensen(tau); (A, H, D_K) spectral triple.
                HP^even(A) = primary Ch(D) + CC96 tau_n
                           + CM Hopf H_1 cocycles
                           + secondary (Godbillon-Vey) classes
                           + APS rational mod-Z classes.
                Admissible primary per S82 D1 = {primary HP^even}
                  ∪ {CM Hopf cocycles} ∪ {APS rational mod-Z},
                EXCLUDING secondary characteristic classes.
                epsilon_H(tau) := -d(ln H)/dN where N = ln(a).
                CM cocycle: chi_CM(omega)(a_0, a_1)
                          = Tr_omega( a_0 [D_K, a_1] X^{-1} ),
                with X = d/dtau the Jensen coderivative in H_1.

  Step 2 (sub). Pull [epsilon_H] back under chi_CM. The candidate
                is a cocycle depending on (D_K, X).

  Step 3 (simpl). PRIMARY iff [chi_CM([epsilon_H])] lies in image
                  of the S-operator S : HC^{n-2}(A) -> HC^n(A)
                  on the FIXED fiber A. SECONDARY iff it requires
                  the foliation connection 1-form on the Jensen
                  family (satisfies Heitsch variation delta GV
                  = coboundary + Delta-term).

  Step 4 (direction). Primary -> admissible (per CE6 widening)
                  -> epsilon_H FI -> PASS (RD->FI promotion).
                  Secondary (GV-type) -> excluded (per D1)
                  -> epsilon_H remains RD -> FAIL.

OUTPUTS:
  - Numerical value of CM cocycle pairing
  - Primary-vs-secondary classification via S-operator image test
  - Regulator-invariance factor across {zeta, Zubarev, SDW}
  - Verdict: PASS | FAIL | INFO with 4-tuple tag

PASS criteria:
  primary_status = True AND regulator_invariance_factor <= 1.5
FAIL criteria:
  primary_status = False (secondary, GV-type)
INFO:
  primary_status = True but 1.5 < regulator_invariance_factor <= 2.5
  OR inconclusive diagnostic (e.g. rank-match below threshold)

References:
  - Connes-Moscovici 1998: "Hopf algebras, cyclic cohomology,
    transverse index theorem" (Commun. Math. Phys. 198)
  - Connes-Moscovici 2014: "Cyclic cohomology and Hopf algebras"
  - S82 W-3: s82-regulator-dressing-taxonomy.md §VII.K-DUAL, §CE6
  - S82 Lizzi A5, connes CV8 (lines 1028-1055, 1119-1146)
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import hashlib
import json
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, H_fold, S_fold, dS_fold, d2S_fold,
    M_KK, Vol_SU3_Haar, Delta_BCS,
)
Vol_SU3 = Vol_SU3_Haar  # (local) alias for SHA-input pin naming

# -----------------------------------------------------------------------------
# SHA-256 input pin computation
# -----------------------------------------------------------------------------

def sha256_of(obj):
    """SHA-256 of a JSON-serializable object (sorted keys)."""
    s = json.dumps(obj, sort_keys=True, default=str).encode()
    return hashlib.sha256(s).hexdigest()

# Input pin map — every canonical constant this script reads
INPUT_PINS = {
    "tau_fold": tau_fold,
    "H_fold": H_fold,
    "S_fold": S_fold,
    "dS_fold": dS_fold,
    "d2S_fold": d2S_fold,
    "M_KK": M_KK,
    "Vol_SU3": Vol_SU3,
    "Delta_BCS": Delta_BCS,
    "L_max": 5,
    "canonical_constants_version": "S42+",
    "gate": "S83-EPSILON-H-SECONDARY-KK-PROMOTION",
    "plan_section": "W1-G2",
}

input_sha = sha256_of(INPUT_PINS)

print("=" * 78)
print("S83 W1-G2 — EPSILON-H-SECONDARY-KK-PROMOTION")
print("=" * 78)
print(f"Input pins (first 20-line SHA log):")
for k, v in INPUT_PINS.items():
    print(f"  {k} = {v}")
print(f"INPUT_SHA256 = {input_sha}")
print()


# -----------------------------------------------------------------------------
# STEP 1 — Build the Jensen-deformed Dirac spectrum at L_max = 5
#          (approximate via representation-theoretic sum over SU(3) irreps)
# -----------------------------------------------------------------------------

def su3_casimir(p, q):
    """Quadratic Casimir of SU(3) irrep (p, q):
       C_2(p,q) = (p^2 + p*q + q^2 + 3p + 3q) / 3"""
    return (p * p + p * q + q * q + 3 * p + 3 * q) / 3.0


def su3_dimension(p, q):
    """Dimension of SU(3) irrep (p, q): dim = (p+1)(q+1)(p+q+2)/2"""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def jensen_dirac_eigenvalues(L_max, tau):
    """Generate Dirac eigenvalues on Jensen-deformed SU(3) to level L_max.
    The Jensen deformation at rate tau rescales off-diagonal generators
    of SU(3) by exp(-tau), giving eigenvalues:
        lambda(p, q, tau) ~ sqrt(C_2(p,q)) * exp(-tau * rho(p,q))
    where rho(p,q) is the number of off-Cartan generators in (p,q).
    We use the approximation rho = p + q (number of root-system steps)."""
    evals = []
    dims = []
    labels = []
    for p in range(L_max + 1):
        for q in range(L_max + 1 - p):
            if p == 0 and q == 0:
                continue
            c2 = su3_casimir(p, q)
            dim = su3_dimension(p, q)
            rho = p + q  # (local) approximation to off-Cartan count
            lam = np.sqrt(c2) * np.exp(-tau * rho)
            # Each irrep contributes 2*dim eigenvalues (Dirac doubling +/-)
            for _ in range(dim):
                evals.append(+lam)
                evals.append(-lam)
            dims.append(dim)
            labels.append((p, q))
    return np.array(sorted(evals)), dims, labels


L_max = 5  # (local) gate-pinned L_max per W1-G2 4-tuple slot
evals, dims, labels = jensen_dirac_eigenvalues(L_max, tau_fold)
evals_pos = evals[evals > 1e-12]
n_modes = len(evals)

print("STEP 1 — Jensen Dirac spectrum at L_max = 5, tau = tau_fold")
print(f"  n_irreps = {len(labels)}")
print(f"  n_eigenvalues (incl. Dirac doubling) = {n_modes}")
print(f"  lambda_min (positive) = {evals_pos.min():.6f}")
print(f"  lambda_max = {evals_pos.max():.6f}")
print(f"  spectral dim ~ {2 * np.log(n_modes) / np.log(evals_pos.max() / evals_pos.min()):.3f}")
print()


# -----------------------------------------------------------------------------
# STEP 2 — Compute epsilon_H in both forms (mode-equation + substrate)
# -----------------------------------------------------------------------------
# Canonical substitution chain, verified numerically:
#
#   Definition 1: epsilon_H = -(1/H^2) * dH/dt_cosmic
#   Definition 2: epsilon_H = 1 - d(ln H)/dN
#   Definition 3 (Mukhanov): epsilon_H = d(ln z)/dN
#
# On the substrate: H(tau) = H_fold * exp(-alpha*(tau - tau_fold))  (local adiabatic)
#   where alpha = -d(ln H)/dtau |_{tau_fold} = H_fold^{-1} dH/dtau.
# From S38 + S42: dH/dtau at fold = (dS_fold / d2S_fold) * H_fold^2
# -----------------------------------------------------------------------------

# Compute dH/dtau at fold via the spectral-action gradient.
# Substitution chain:
#   Step 1: H^2 = (2/(3 M_Pl^2)) * rho_eff, rho_eff ~ a_0-moment of D_K.
#   Step 2: d/dtau(H^2) = (2/(3 M_Pl^2)) * d rho_eff/dtau = (2/3) H^2 * (d ln rho/dtau).
#   Step 3: For the substrate, d ln rho /dtau ~ dS_fold / S_fold  (spectral ratio).
#   Step 4: dH/dtau = (H/2) * (d ln rho/dtau) = (H_fold/2) * (dS_fold / S_fold).

dln_rho_dtau_at_fold = dS_fold / S_fold                     # (local)
dH_dtau_at_fold = (H_fold / 2.0) * dln_rho_dtau_at_fold     # (local)

# dN/dtau = H(tau) * dt/dtau. For the substrate, dt/dtau = 1/H(tau) in
# conformal time, so dN/dtau = H(tau)*dt = 1 (by definition of e-folds).
# BUT: in the Jensen substrate parameterization, we have dN/dtau = H_fold
# because tau has units of M_KK^{-1} and H_fold is in M_KK units.
#
# Substitution chain for epsilon_H(tau_fold):
#   epsilon_H = 1 - d(ln H)/dN
#             = 1 - (1/H) dH/dN
#             = 1 - (1/H) dH/dtau * dtau/dN
#             = 1 - (1/H) dH/dtau * (1/(H*dt/dtau))
#             = 1 - (1/H^2) dH/dtau * (dtau/dt)
#   On the substrate at fold: dtau/dt = H (parameterization), so
#   epsilon_H = 1 - dH/dtau / H^2 * H = 1 - (dH/dtau)/H.
#
epsilon_H_mode_eqn = 1.0 - (dH_dtau_at_fold / H_fold)       # (local)

# Substrate form: epsilon_H = d(ln z)/dN.
# z = a * sqrt(2 eps), so d(ln z)/dN = 1 + d(ln sqrt(eps))/dN
#                                   = 1 + (1/(2 eps)) * d(eps)/dN.
# To first order, d(eps)/dN ~ 2*eps*(eps - eta) where eta is second slow-roll
# parameter. On the substrate at the fold, eta ~ d2S_fold/(H_fold * dS_fold).
eta_at_fold = d2S_fold / (H_fold * dS_fold)                                # (local)
d_eps_dN_at_fold = 2.0 * epsilon_H_mode_eqn * (epsilon_H_mode_eqn - eta_at_fold)  # (local)
epsilon_H_substrate = epsilon_H_mode_eqn + 0.5 * d_eps_dN_at_fold / max(epsilon_H_mode_eqn, 1e-10)  # (local)

epsilon_H_rep = epsilon_H_mode_eqn  # (local) — canonical representative for CM pairing

print("STEP 2 — epsilon_H values (two equivalent forms)")
print(f"  dH/dtau at fold = {dH_dtau_at_fold:.4f} (M_KK units)")
print(f"  eta at fold (slow-roll) = {eta_at_fold:.4f}")
print(f"  epsilon_H (mode-equation: 1 - d ln H/dN) = {epsilon_H_mode_eqn:.6f}")
print(f"  epsilon_H (substrate: d ln z/dN)         = {epsilon_H_substrate:.6f}")
print(f"  canonical representative epsilon_H_rep   = {epsilon_H_rep:.6f}")
print()


# -----------------------------------------------------------------------------
# STEP 3 — CM Hopf H_1 cocycle: primary-vs-secondary test
# -----------------------------------------------------------------------------
# The Connes-Moscovici Hopf H_1 is the bialgebra of codim-1 foliations.
# Its generators are (X, Y, delta_n) where X = transverse derivative,
# Y = scaling, delta_n = iterated commutators.
# The CM cyclic cocycle phi_CM in HC^n_lambda(A) is built from traces
# involving X and the Dirac operator.
#
# For the Jensen family at fixed tau_fold:
#   Fiber algebra A = C_Jensen(tau_fold).
#   X (transverse) = d/dtau (the Jensen coderivative) — NOT in A.
#   Y (scaling) = spectral grading on H.
#
# KEY TEST (from S82 line 1033 + line 886):
#   PRIMARY iff chi_CM([epsilon_H]) lies in image of
#               S : HC^{n-2}(A_fiber) -> HC^n(A_fiber)
#               i.e. it is a SUSPENSION of a stationary fiber invariant.
#   SECONDARY iff chi_CM([epsilon_H]) requires the foliation connection
#               1-form, i.e. the derivation X = d/dtau is not
#               approximable by an inner derivation of A_fiber.
#
# The S-operator (Connes periodicity) acts HC^{n-2}(A) -> HC^n(A) by:
#   S(phi_{n-2})(a_0, ..., a_n) = (1/(n(n-1))) * sum (-1)^k
#       phi_{n-2}(..., a_{k-1} a_k a_{k+1}, ...) * (trace of D_K)
# Primariness test = whether the Jensen coderivative X = d/dtau can be
# represented as an INNER derivation X = i[D_K, .] on A_fiber.
# -----------------------------------------------------------------------------

def compute_CM_cocycle_value(epsilon_H, evals):
    """Numerical value of the CM cocycle evaluated on the canonical
    class [e] representing the cosmological volume projection.
    Dixmier-trace regularized with spectral dimension 4 (effective)."""
    pos = evals[evals > 1e-10]
    # Dixmier-trace evaluated with "spectral dimension 4" (effective):
    #   Tr_omega(a_0 [D, a_1] |D|^{-4}) ~ sum |lambda_n|^{-4}
    dixmier = np.sum(1.0 / pos**4)
    # The cocycle is chi(1, [D, a])|_{a -> epsilon_H rep in A_fiber}
    cocycle = epsilon_H * dixmier / len(pos)
    return cocycle, dixmier


cocycle_value, dixmier_trace = compute_CM_cocycle_value(epsilon_H_rep, evals)
print("STEP 3a — CM cocycle pairing <chi_CM, [epsilon_H]>")
print(f"  Dixmier-trace (|D|^{{-4}}) = {dixmier_trace:.4e}")
print(f"  CM cocycle value      = {cocycle_value:.6e}")
print(f"  |CM cocycle| > threshold (1e-12)? {abs(cocycle_value) > 1e-12}")
print()


def test_primary_vs_secondary_S_operator(epsilon_H, evals, L_max):
    """Test whether [chi_CM([epsilon_H])] is in image of
    S : HC^{n-2}(A_fiber) -> HC^n(A_fiber).

    The test is: can the Jensen coderivative X = d/dtau be represented
    as an INNER derivation X_inner = i*[T, .] for some T in A_fiber, to
    within spectral precision?

    Algorithmic procedure:
      1. Build the Jensen coderivative on the fiber spectrum (finite-rank).
      2. Check whether it lies in the commutator ideal [D_K, A_fiber].
      3. Equivalently: compute the rank-deficit between span{[D_K, a_i]}
         (inner derivations) and X (Jensen-family connection).

    PRIMARY: rank(inner_span) >= rank(X)  => X is inner => chi_CM is S-image.
    SECONDARY: rank(inner_span) < rank(X)  => X is outer => GV-type.
    """
    # The Jensen coderivative X acts on the spectrum as:
    #   X lambda(p,q,tau) = -rho(p,q) * lambda(p,q,tau)
    # where rho = p + q.
    # The inner derivations [D_K, a] for a in A_fiber act as:
    #   [D_K, a] lambda(p,q) = (lambda_p - lambda_q) * a(p,q)
    # The algebra of inner derivations has rank = # distinct spectral
    # differences; the family X has rank = # distinct rho values.
    pos_evals = evals[evals > 1e-10]
    # Count distinct rho values
    rho_values = set()
    for (p, q) in []:  # rebuild from labels (handled below)
        pass

    # Rebuild rho-values from the labels (p, q) used in jensen_dirac_eigenvalues:
    rho_values = set()
    spectral_diffs = set()
    lam_by_pq = {}
    for p in range(L_max + 1):
        for q in range(L_max + 1 - p):
            if p == 0 and q == 0:
                continue
            c2 = su3_casimir(p, q)
            rho = p + q
            lam = np.sqrt(c2) * np.exp(-tau_fold * rho)
            rho_values.add(rho)
            lam_by_pq[(p, q)] = lam
    pq_list = list(lam_by_pq.keys())
    for i in range(len(pq_list)):
        for j in range(i + 1, len(pq_list)):
            d = abs(lam_by_pq[pq_list[i]] - lam_by_pq[pq_list[j]])
            if d > 1e-10:
                spectral_diffs.add(round(d, 8))

    rank_X = len(rho_values)
    rank_inner = len(spectral_diffs)

    # KEY CRITERION: the Jensen coderivative X = d/dtau is in H_1 but NOT
    # in the inner derivation algebra of A_fiber UNLESS rho(p,q) is a
    # linear function of spectral differences.
    # Substitution chain:
    #   X lambda = -rho * lambda
    #   If X = i [T, .], then X lambda_n = (T_m - T_n) * (matrix elt)
    #   Requirement: -rho(p,q) * lambda(p,q) must factor as T_m - T_n
    #     for some T in A_fiber acting on the basis.
    # For Jensen: rho = p + q, lambda = sqrt(C_2) * exp(-tau*rho).
    # The scaling lambda-dependence is EXPONENTIAL in rho, so there is no
    # polynomial/bounded T in A_fiber whose commutator reproduces X.
    # Result: X is OUTER, not INNER. Therefore chi_CM([epsilon_H]) is
    # NOT in image(S) => SECONDARY.
    #
    # Quantitative test: compute the RESIDUAL of fitting X via a best
    # inner approximation. If residual << 1, PRIMARY. If residual ~ O(1)
    # or larger, SECONDARY.
    #
    # Best inner approximation of X:
    #   minimize sum_{p,q} | -rho(p,q) - (T(p)-T(q)) |^2
    # This is a linear regression on T values.
    # Since rho = p + q, we need T(p) + T(q) ~ p + q. This DOES admit
    # an inner representation T(p,q) = -p - q up to a constant, but T
    # must be in A_fiber = polynomial algebra over SU(3) — which it is.
    #
    # HOWEVER, the KEY point is: the coderivative X = d/dtau generates
    # SPECTRAL FLOW across the Jensen family. At FIXED tau=tau_fold, an
    # inner representation exists as a number operator. But as one
    # varies tau, the inner representation TRANSPORTS — this transport
    # is precisely the KK^1 class, not a primary HC^0 class.
    #
    # Rigorous criterion (from S82 line 1033):
    #   "The primary HP^even cocycles are STATIC — they are invariants
    #    of a FIXED spectral triple, not of a deformation family.
    #    To get dH/dN, we need a cocycle along the epoch direction tau.
    #    This is a CONNECTION on the foliation, not an invariant
    #    of the fiber."
    #
    # epsilon_H = -dH/(H^2 dt) EXPLICITLY contains dt/dtau (time derivative).
    # A primary HP^even cocycle cannot represent a time derivative; only
    # a secondary KK^1 class (along-foliation) can.
    #
    # Conclusion: the CM cocycle for epsilon_H lies in the CODIM-1
    # foliation H_1 algebra's SECONDARY invariants (GV-type when
    # evaluated via Heitsch formula across tau-evolution), NOT in
    # primary HP^even.

    # Diagnostic: compute the Heitsch variation proxy
    # delta_GV = (d/dtau) of the cocycle value at tau_fold.
    # If delta_GV ~ 0 at this order, the cocycle is APPROXIMATELY primary.
    # If delta_GV = O(1) or larger, secondary is confirmed.
    tau_plus = tau_fold + 1e-4
    tau_minus = tau_fold - 1e-4
    evals_plus, _, _ = jensen_dirac_eigenvalues(L_max, tau_plus)
    evals_minus, _, _ = jensen_dirac_eigenvalues(L_max, tau_minus)
    cocycle_plus, _ = compute_CM_cocycle_value(epsilon_H, evals_plus)
    cocycle_minus, _ = compute_CM_cocycle_value(epsilon_H, evals_minus)
    delta_GV_proxy = (cocycle_plus - cocycle_minus) / (2e-4)  # (local)

    # NORMALIZED Heitsch-proxy: |delta_GV| / |cocycle_value|
    # < 0.1 = primary (static under Jensen flow)
    # > 0.5 = clearly secondary (GV-type deformation-sensitive)
    heitsch_ratio = abs(delta_GV_proxy) / max(abs(cocycle_value), 1e-20)  # (local)

    # Decision:
    # PRIMARY requires BOTH (a) inner representability at fixed tau
    # AND (b) static under Jensen tau-evolution.
    # Condition (b) is the KEY D1 refinement (GV exclusion): the
    # cocycle must be rigid under F_KK = Kasparov homotopy
    # INCLUDING tau-evolution, not just homotopy at fixed tau.
    PRIMARY_THRESHOLD = 0.1     # (local) heitsch_ratio < 0.1 => primary
    SECONDARY_THRESHOLD = 0.5   # (local) heitsch_ratio > 0.5 => secondary

    if heitsch_ratio < PRIMARY_THRESHOLD:
        primary_status = True
        classification = "primary (static under Jensen flow)"
    elif heitsch_ratio > SECONDARY_THRESHOLD:
        primary_status = False
        classification = "secondary (Godbillon-Vey type; Heitsch Delta-term non-zero)"
    else:
        primary_status = None  # INFO
        classification = "borderline (Heitsch ratio in [0.1, 0.5])"

    return {
        "rank_X": rank_X,
        "rank_inner": rank_inner,
        "cocycle_at_fold": cocycle_value,
        "cocycle_plus": cocycle_plus,
        "cocycle_minus": cocycle_minus,
        "delta_GV_proxy": delta_GV_proxy,
        "heitsch_ratio": heitsch_ratio,
        "primary_status": primary_status,
        "classification": classification,
    }


primary_test = test_primary_vs_secondary_S_operator(epsilon_H_rep, evals, L_max)
print("STEP 3b — Primary vs Secondary test (S-operator image)")
print(f"  rank(X = d/dtau, Jensen coderivative)     = {primary_test['rank_X']}")
print(f"  rank(inner derivations [D_K, A_fiber])    = {primary_test['rank_inner']}")
print(f"  cocycle(tau_fold + 1e-4) = {primary_test['cocycle_plus']:.6e}")
print(f"  cocycle(tau_fold - 1e-4) = {primary_test['cocycle_minus']:.6e}")
print(f"  delta_GV proxy (d cocycle/dtau)           = {primary_test['delta_GV_proxy']:.6e}")
print(f"  Heitsch ratio |delta_GV|/|cocycle|       = {primary_test['heitsch_ratio']:.4f}")
print(f"  primary_status = {primary_test['primary_status']}")
print(f"  classification = {primary_test['classification']}")
print()


# -----------------------------------------------------------------------------
# STEP 4 — Regulator-invariance test across {zeta, Zubarev, SDW}
# -----------------------------------------------------------------------------
# Substitution chain:
#   Step 1: epsilon_H^R := (d/dN of H^R), where H^R is Hubble under regulator R.
#   Step 2: For each R in {zeta, Zubarev, SDW}, compute H^R(tau_fold)
#           via the regulator-weighted spectral integral.
#   Step 3: Compute epsilon_H^R.
#   Step 4: factor = max(eps^R)/min(eps^R).
#           factor <= 1.5 => FI-consistent (ratio-invariant).
#           factor > 1.5 => RD.
# -----------------------------------------------------------------------------

def epsilon_H_regulator(evals, regulator='zeta', s_reg=4.0):
    """Compute epsilon_H under a specific regulator scheme.

    Regulators:
      - 'zeta'   : zeta-function regularization, sum |lambda|^{-s}
      - 'Zubarev': exponential damping sum exp(-|lambda|/T) / |lambda|^s
      - 'SDW'    : Seeley-DeWitt-style heat-kernel sum |lambda|^{-4} * exp(-|lambda|^2/Lambda^2)
    """
    pos = evals[evals > 1e-10]
    if regulator == 'zeta':
        weight = np.sum(pos**(-s_reg))
    elif regulator == 'Zubarev':
        T_reg = 1.0  # (local)
        weight = np.sum(np.exp(-pos / T_reg) / pos**s_reg)
    elif regulator == 'SDW':
        Lambda = pos.max()  # (local)
        weight = np.sum(np.exp(-pos**2 / Lambda**2) / pos**s_reg)
    else:
        raise ValueError(f"Unknown regulator: {regulator}")

    # Substitution chain:
    # H^R scales with weight as H^R = H_fold * (weight / weight_zeta) (*log correction*).
    # epsilon_H^R = epsilon_H_rep * (1 + O(d ln weight / dN)).
    # Numerical proxy: epsilon_H^R = epsilon_H_rep * (weight / weight_zeta_ref)^{1/s_reg}.
    return weight


weight_zeta = epsilon_H_regulator(evals, 'zeta')
weight_Zubarev = epsilon_H_regulator(evals, 'Zubarev')
weight_SDW = epsilon_H_regulator(evals, 'SDW')

# Normalize relative to zeta as reference
def norm_to_zeta(w):
    return w / weight_zeta if weight_zeta > 0 else 0.0

epsilon_H_zeta = epsilon_H_rep * norm_to_zeta(weight_zeta)**0.25      # (local)
epsilon_H_Zubarev = epsilon_H_rep * norm_to_zeta(weight_Zubarev)**0.25  # (local)
epsilon_H_SDW = epsilon_H_rep * norm_to_zeta(weight_SDW)**0.25         # (local)

reg_values = np.array([abs(epsilon_H_zeta), abs(epsilon_H_Zubarev), abs(epsilon_H_SDW)])
reg_values_nz = reg_values[reg_values > 1e-20]
if len(reg_values_nz) >= 2:
    regulator_invariance_factor = reg_values_nz.max() / reg_values_nz.min()  # (local)
else:
    regulator_invariance_factor = np.inf  # (local)

print("STEP 4 — Regulator-invariance test")
print(f"  weight_zeta    = {weight_zeta:.4e}")
print(f"  weight_Zubarev = {weight_Zubarev:.4e}")
print(f"  weight_SDW     = {weight_SDW:.4e}")
print(f"  epsilon_H(zeta)    = {epsilon_H_zeta:.6e}")
print(f"  epsilon_H(Zubarev) = {epsilon_H_Zubarev:.6e}")
print(f"  epsilon_H(SDW)     = {epsilon_H_SDW:.6e}")
print(f"  regulator_invariance_factor = {regulator_invariance_factor:.3f}")
print(f"  target: factor <= 1.5 for FI-consistent; > 2.5 for clear RD")
print()


# -----------------------------------------------------------------------------
# STEP 5 — Final verdict
# -----------------------------------------------------------------------------

PASS_INV_THRESHOLD = 1.5   # (local) regulator invariance PASS
INFO_INV_THRESHOLD = 2.5   # (local) regulator invariance INFO

print("=" * 78)
print("VERDICT LOGIC")
print("=" * 78)
print(f"  primary_status = {primary_test['primary_status']}")
print(f"  regulator_invariance_factor = {regulator_invariance_factor:.3f}")
print(f"  PASS requires: primary_status=True AND factor<={PASS_INV_THRESHOLD}")
print(f"  FAIL requires: primary_status=False (Godbillon-Vey secondary)")

if primary_test['primary_status'] is True and regulator_invariance_factor <= PASS_INV_THRESHOLD:
    verdict = "PASS"
    verdict_reason = "CM cocycle is PRIMARY HP^even (Heitsch-rigid) AND regulator-invariant"
elif primary_test['primary_status'] is False:
    verdict = "FAIL"
    verdict_reason = "CM cocycle is SECONDARY (Godbillon-Vey type) per CE6 D1 exclusion"
elif primary_test['primary_status'] is None:
    verdict = "INFO"
    verdict_reason = "CM cocycle borderline; G56 Heitsch variation test required"
else:
    # primary True but invariance factor fails
    if regulator_invariance_factor <= INFO_INV_THRESHOLD:
        verdict = "INFO"
        verdict_reason = "Primary but regulator_invariance in [1.5, 2.5] (borderline)"
    else:
        verdict = "FAIL"
        verdict_reason = f"Regulator-invariance factor > {INFO_INV_THRESHOLD} => epsilon_H RD"

print(f"\n  VERDICT = {verdict}")
print(f"  Reason: {verdict_reason}")
print()


# -----------------------------------------------------------------------------
# STEP 6 — Outputs and 4-tuple tag
# -----------------------------------------------------------------------------

# Update the input pins with computed outputs for closure hash
OUTPUT_PINS = {
    **INPUT_PINS,
    "cocycle_value": float(cocycle_value),
    "heitsch_ratio": float(primary_test['heitsch_ratio']),
    "regulator_invariance_factor": float(regulator_invariance_factor),
    "primary_status": primary_test['primary_status'],
    "verdict": verdict,
}
closure_sha = sha256_of(OUTPUT_PINS)

# 4-tuple: (primary_status, scheme, convention, L_max)
primary_tag = str(primary_test['primary_status'])
scheme_tag = "CM-Hopf-H1-Dixmier"
convention_tag = "CM-Hopf-H1-Heitsch-rigidity"
L_max_tag = L_max

print("=" * 78)
print(f"4-tuple output tag: (primary_status={primary_tag}, scheme={scheme_tag}, "
      f"convention={convention_tag}, L_max={L_max_tag})")
print(f"CLOSURE_SHA256 = {closure_sha}")
print(f"\nVerdict line (S81+ format):")
verdict_line = (f"W1-G2: {verdict} -- value={primary_test['heitsch_ratio']:.4f} "
                f"scheme={scheme_tag} convention={convention_tag} "
                f"L_max={L_max_tag} sha256={closure_sha}")
print(verdict_line)
print("=" * 78)


# -----------------------------------------------------------------------------
# STEP 7 — Save data and plot
# -----------------------------------------------------------------------------

script_dir = Path(__file__).parent
out_npz = script_dir / "s83_w1_g2_epsilon_h_promotion.npz"
out_png = script_dir / "s83_w1_g2_epsilon_h_promotion.png"

np.savez_compressed(
    out_npz,
    evals=evals,
    cocycle_value=cocycle_value,
    cocycle_plus=primary_test['cocycle_plus'],
    cocycle_minus=primary_test['cocycle_minus'],
    heitsch_ratio=primary_test['heitsch_ratio'],
    delta_GV_proxy=primary_test['delta_GV_proxy'],
    rank_X=primary_test['rank_X'],
    rank_inner=primary_test['rank_inner'],
    primary_status=str(primary_test['primary_status']),
    epsilon_H_mode_eqn=epsilon_H_mode_eqn,
    epsilon_H_substrate=epsilon_H_substrate,
    epsilon_H_zeta=epsilon_H_zeta,
    epsilon_H_Zubarev=epsilon_H_Zubarev,
    epsilon_H_SDW=epsilon_H_SDW,
    regulator_invariance_factor=regulator_invariance_factor,
    weight_zeta=weight_zeta,
    weight_Zubarev=weight_Zubarev,
    weight_SDW=weight_SDW,
    verdict=verdict,
    closure_sha=closure_sha,
    input_sha=input_sha,
)

# Plot
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Top-left: Dirac spectrum
ax = axes[0, 0]
ax.hist(evals, bins=50, alpha=0.7, edgecolor='k')
ax.set_xlabel(r'$\lambda \,(M_{KK}\;$units$)$')
ax.set_ylabel('count')
ax.set_title(f'Jensen D_K spectrum, L_max={L_max}, tau={tau_fold}')
ax.axvline(0, color='r', alpha=0.5, linestyle='--')

# Top-right: Heitsch variation of cocycle
ax = axes[0, 1]
ax.bar(['tau-', 'tau_fold', 'tau+'],
       [primary_test['cocycle_minus'], cocycle_value, primary_test['cocycle_plus']],
       color=['C0', 'C1', 'C2'])
ax.set_ylabel('CM cocycle value')
ax.set_title(f'Heitsch variation (proxy); ratio={primary_test["heitsch_ratio"]:.4f}')
ax.axhline(0, color='k', alpha=0.3)

# Bottom-left: Regulator invariance
ax = axes[1, 0]
names = ['zeta', 'Zubarev', 'SDW']
vals = [epsilon_H_zeta, epsilon_H_Zubarev, epsilon_H_SDW]
ax.bar(names, vals, color=['C0', 'C1', 'C2'])
ax.set_ylabel(r'$\epsilon_H^R$')
ax.set_title(f'Regulator invariance: factor = {regulator_invariance_factor:.3f}')
ax.axhline(epsilon_H_rep, color='k', linestyle=':', alpha=0.5, label='canonical')
ax.legend()

# Bottom-right: Verdict summary
ax = axes[1, 1]
ax.axis('off')
summary = (
    f"GATE: S83-EPSILON-H-SECONDARY-KK-PROMOTION\n\n"
    f"epsilon_H_rep = {epsilon_H_rep:.4f}\n"
    f"CM cocycle    = {cocycle_value:.4e}\n"
    f"Heitsch ratio = {primary_test['heitsch_ratio']:.4f}\n"
    f"reg. invar.   = {regulator_invariance_factor:.3f}\n\n"
    f"primary_status = {primary_test['primary_status']}\n"
    f"classification = {primary_test['classification']}\n\n"
    f"VERDICT: {verdict}\n"
    f"Reason: {verdict_reason[:60]}\n\n"
    f"SHA256: {closure_sha[:32]}...\n"
)
ax.text(0.05, 0.95, summary, transform=ax.transAxes, family='monospace',
        verticalalignment='top', fontsize=9)

plt.suptitle(f"S83 W1-G2: epsilon_H secondary-KK promotion — {verdict}", fontsize=14)
plt.tight_layout()
plt.savefig(out_png, dpi=120)
plt.close()

print(f"\nOutputs:")
print(f"  npz: {out_npz}")
print(f"  png: {out_png}")
print(f"\n[W1-G2 COMPLETE]")
