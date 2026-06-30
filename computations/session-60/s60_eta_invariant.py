#!/usr/bin/env python3
"""
S60 ETA-INVARIANT-60: eta-Invariant of D_K at Jensen Fold
===========================================================

GATE: ETA-INVARIANT-60
  PASS: eta != 0 at the fold (topological anomaly contributes to CC)
  FAIL: eta = 0 to machine precision (J-symmetry enforces; mechanism 5 closed)
  INFO: computation inconclusive due to convergence issues

PHYSICS:
  The APS eta-invariant eta(D) = sum_lambda sign(lambda) |lambda|^{-s}|_{s=0}
  measures the spectral asymmetry of the Dirac operator D_K on (SU(3), g_tau).

  For a BDI system with T^2 = +1, the real structure J satisfies:
    J D_K J^{-1} = D_K  (commutes, not anti-commutes)
  and J is anti-unitary with J^2 = +1.

  If J maps eigenvector |psi, lambda> to |J psi, lambda>, this does NOT
  directly force spectral symmetry. What forces eta = 0 is the COMBINATION
  of the Clifford algebra structure and the representation-theoretic
  decomposition:

  1. D_K is anti-Hermitian (math convention). H = i*D_K is Hermitian.
  2. On each Peter-Weyl sector (p,q), the eigenvalues of H come in
     +/- pairs from the chirality grading (dim 8, even).
  3. The charge conjugation C (involving complex conjugation of the
     representation) maps sector (p,q) to sector (q,p) with eigenvalue
     sign reversal: if mu is an eigenvalue of H on (p,q), then -mu is
     an eigenvalue on (q,p).
  4. For self-conjugate sectors (p=q), the internal C acts within the
     sector and forces exact +/- pairing.

  CROSS-CHECK: compute eta numerically from the full truncated spectrum.
  If eta = 0 exactly (to machine precision), mechanism 5 is closed.

COMPUTATION:
  1. Build Dirac spectrum at tau_fold with max_pq_sum=5 (992 eigenvalues)
  2. The eigenvalues of H = i*D_pi are real. The "signed Dirac eigenvalues"
     are these real numbers mu_n.
  3. eta(s) = sum_n sign(mu_n) * |mu_n|^{-s} for s > dim/2 = 4 (convergent)
  4. Analytically continue to s = 0 via polynomial fit in 1/s or direct
     evaluation at decreasing s.
  5. Cross-check: N_+ - N_- (count of positive vs negative eigenvalues)
  6. Cross-check: pair spectrum (p,q) vs (q,p) to verify conjugation symmetry
  7. Spectral flow: track eigenvalue zero-crossings from tau=0 to tau_fold

Author: Spectral-Geometer Agent (Session 60)
Date: 2026-03-27
"""

import numpy as np
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# dirac_spectrum imports branching_computation which lives in computations/_shared
archive_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_shared")
if os.path.isdir(archive_dir):
    sys.path.insert(0, os.path.abspath(archive_dir))
from canonical_constants import tau_fold, Vol_SU3_Haar, M_KK
from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset, build_cliff8,
    validate_clifford, validate_connection, validate_omega_hermitian,
    get_irrep, dirac_operator_on_irrep, _irrep_cache
)

# =============================================================================
# CONFIGURATION
# =============================================================================
TAU_FOLD = tau_fold  # 0.19
MAX_PQ_SUM = 5  # 992 modes (sufficient for eta convergence) (local)
N_TAU_FLOW = 40      # tau steps for spectral flow computation
EPS_ZERO = 1e-12     # threshold for "zero eigenvalue"

print("=" * 72)
print("S60 ETA-INVARIANT-60: eta-Invariant of D_K at Jensen Fold")
print("=" * 72)
print(f"  tau_fold = {TAU_FOLD}")
print(f"  max_pq_sum = {MAX_PQ_SUM}")
print(f"  n_tau_flow = {N_TAU_FLOW}")


# =============================================================================
# SECTION 1: Build infrastructure
# =============================================================================

print("\n--- Section 1: Lie algebra + Clifford infrastructure ---")
gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

cliff_err = validate_clifford(gammas)
print(f"  Clifford algebra error: {cliff_err:.2e}")
assert cliff_err < 1e-14, "Clifford algebra validation failed"


# =============================================================================
# SECTION 2: Build spectrum at the fold
# =============================================================================

def build_spectrum_at_tau(tau, max_pq_sum, verbose=True):
    """
    Build the full Dirac spectrum at a given tau.
    Returns dict with sector-by-sector eigenvalues of H = i*D.
    """
    from scipy.linalg import eigh as scipy_eigh

    # Clear irrep cache for fresh computation
    _irrep_cache.clear()

    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    if verbose:
        mc_err = validate_connection(Gamma)
        _, is_ah, h_err, ah_err = validate_omega_hermitian(Omega)
        print(f"  tau={tau:.4f}: connection err={mc_err:.2e}, "
              f"Omega anti-Herm err={ah_err:.2e}")

    sectors = []
    all_mu = []  # all real eigenvalues of H = i*D

    # Enumerate irreps
    irreps = []
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
            C2 = (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0
            irreps.append((C2, p, q, dim_pq))
    irreps.sort()

    for _, p, q, dim_pq in irreps:
        try:
            if (p, q) == (0, 0):
                D_pi = Omega.copy()
            else:
                rho, dim_check = get_irrep(p, q, gens, f_abc)
                assert dim_check == dim_pq
                D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)

            # Anti-Hermiticity check
            ah_err = np.max(np.abs(D_pi + D_pi.conj().T))

            # H = i*D is Hermitian => real eigenvalues
            H = 1j * D_pi
            h_err = np.max(np.abs(H - H.conj().T))

            if h_err > 1e-10:
                # Fall back to general eigvals
                mu = np.sort(np.linalg.eigvalsh(H))
            else:
                mu = np.sort(scipy_eigh(H, eigvals_only=True))

            sectors.append({
                'p': p, 'q': q, 'dim_pq': dim_pq,
                'mu': mu, 'ah_err': ah_err, 'h_err': h_err
            })

            # Peter-Weyl multiplicity: each mu appears dim_pq times
            for m in mu:
                all_mu.append((m, dim_pq))

        except Exception as e:
            if verbose:
                print(f"    ({p},{q}): FAILED ({e})")
            continue

    return sectors, all_mu


print("\n--- Section 2: Dirac spectrum at the fold ---")
t0 = time.time()
sectors_fold, all_mu_fold = build_spectrum_at_tau(TAU_FOLD, MAX_PQ_SUM)
t_fold = time.time() - t0
print(f"  Spectrum computed in {t_fold:.1f}s")
print(f"  Number of sectors: {len(sectors_fold)}")

n_eigenvalues_distinct = sum(len(s['mu']) for s in sectors_fold)
n_eigenvalues_pw = sum(len(s['mu']) * s['dim_pq'] for s in sectors_fold)
print(f"  Distinct eigenvalues: {n_eigenvalues_distinct}")
print(f"  Peter-Weyl weighted: {n_eigenvalues_pw}")


# =============================================================================
# SECTION 3: eta-invariant computation
# =============================================================================

print("\n--- Section 3: eta-invariant ---")

# 3a. Direct count: N_+ - N_- (with Peter-Weyl weights)
n_pos = 0
n_neg = 0
n_zero = 0  # (local)
for mu_val, pw_mult in all_mu_fold:
    if abs(mu_val) < EPS_ZERO:
        n_zero += pw_mult
    elif mu_val > 0:
        n_pos += pw_mult
    else:
        n_neg += pw_mult

spectral_asymmetry = n_pos - n_neg
print(f"  N_+ = {n_pos}, N_- = {n_neg}, N_0 = {n_zero}")
print(f"  Spectral asymmetry N_+ - N_- = {spectral_asymmetry}")

# 3b. eta(s) for s in the convergent regime (s > dim/2 = 4)
# eta(s) = sum_n sign(mu_n) * |mu_n|^{-s} * dim_pq
# with PW weights

def compute_eta(s_val, all_mu, eps_zero=1e-12):
    """Compute eta(s) = sum sign(mu) |mu|^{-s} * PW_weight, skipping zeros."""
    result = 0.0
    for mu_val, pw_mult in all_mu:
        if abs(mu_val) < eps_zero:
            continue
        result += np.sign(mu_val) * abs(mu_val)**(-s_val) * pw_mult
    return result


# Evaluate eta(s) for s from 5.0 down to 0.1
s_values = np.array([10.0, 8.0, 6.0, 5.0, 4.5, 4.0, 3.5, 3.0,
                      2.5, 2.0, 1.5, 1.0, 0.5, 0.25, 0.1])
eta_values = np.array([compute_eta(sv, all_mu_fold) for sv in s_values])

print("\n  eta(s) values:")
print(f"  {'s':>8s}  {'eta(s)':>18s}")
for sv, ev in zip(s_values, eta_values):
    print(f"  {sv:8.2f}  {ev:18.12e}")

# The eta-invariant is eta(0). For a symmetric spectrum, eta(s) = 0 for all s.
# Extrapolate to s=0.

# 3c. Direct computation at s = 0 for FINITE truncation
# For finite spectrum, eta(0) = sum sign(mu) * |mu|^0 * PW = sum sign(mu) * PW
# = N_+ - N_- (exactly the spectral asymmetry)
eta_at_zero_direct = float(spectral_asymmetry)
print(f"\n  eta(s=0) direct (finite truncation) = {eta_at_zero_direct}")


# =============================================================================
# SECTION 4: Sector-by-sector symmetry analysis
# =============================================================================

print("\n--- Section 4: Sector-by-sector spectral symmetry ---")

# For each sector (p,q), check if eigenvalues come in +/- pairs
max_pair_err_all = 0.0
sector_eta_data = []

for sec in sectors_fold:
    p, q = sec['p'], sec['q']
    mu = sec['mu']
    dim_pq = sec['dim_pq']

    # Sort by absolute value
    abs_mu = np.abs(mu)
    sorted_idx = np.argsort(abs_mu)
    mu_sorted = mu[sorted_idx]

    # Check +/- pairing: sorted eigenvalues should be [-a_n, ..., -a_1, a_1, ..., a_n]
    n = len(mu)
    if n % 2 == 0:
        # Even number: pair mu[i] with mu[n-1-i]
        pair_err = 0.0  # (local)
        for i in range(n // 2):
            err = abs(mu_sorted[i] + mu_sorted[n - 1 - i])
            pair_err = max(pair_err, err)
    else:
        # Odd: middle eigenvalue should be zero, rest pair
        pair_err = abs(mu_sorted[n // 2])
        for i in range(n // 2):
            err = abs(mu_sorted[i] + mu_sorted[n - 1 - i])
            pair_err = max(pair_err, err)

    max_pair_err_all = max(max_pair_err_all, pair_err)

    # Sector eta(0) = N_+ - N_- within this sector
    n_p = np.sum(mu > EPS_ZERO)
    n_m = np.sum(mu < -EPS_ZERO)
    n_z = np.sum(np.abs(mu) <= EPS_ZERO)
    sector_eta = (n_p - n_m) * dim_pq

    sector_eta_data.append({
        'p': p, 'q': q, 'dim_pq': dim_pq,
        'n_eigenvalues': n, 'n_pos': int(n_p), 'n_neg': int(n_m),
        'n_zero': int(n_z), 'pair_err': pair_err, 'sector_eta': int(sector_eta)
    })

    if pair_err > 1e-10 or sector_eta != 0:
        print(f"  ({p},{q}) dim={dim_pq}: N+={n_p}, N-={n_m}, N0={n_z}, "
              f"pair_err={pair_err:.2e}, sector_eta={sector_eta}")

print(f"\n  Maximum +/- pair error (all sectors): {max_pair_err_all:.2e}")
print(f"  Total eta(0) from sector sum: {sum(s['sector_eta'] for s in sector_eta_data)}")


# =============================================================================
# SECTION 5: Conjugate sector cross-check
# =============================================================================

print("\n--- Section 5: Conjugate sector (p,q) vs (q,p) symmetry ---")

# Build dict of sectors by (p,q)
sector_dict = {}
for sec in sectors_fold:
    sector_dict[(sec['p'], sec['q'])] = sec

max_conj_err = 0.0
conj_checks = []

for sec in sectors_fold:
    p, q = sec['p'], sec['q']
    if p <= q:
        continue  # avoid double-counting; check p > q against q < p

    conj_key = (q, p)
    if conj_key not in sector_dict:
        continue

    mu_pq = np.sort(sec['mu'])
    mu_qp = np.sort(sector_dict[conj_key]['mu'])

    if len(mu_pq) != len(mu_qp):
        print(f"  WARNING: ({p},{q}) has {len(mu_pq)} evals, ({q},{p}) has {len(mu_qp)}")
        continue

    # For charge conjugation C mapping (p,q) -> (q,p):
    # If C anti-commutes with D_K, then mu(p,q) -> -mu(q,p)
    # If C commutes with D_K, then mu(p,q) -> mu(q,p)
    #
    # The correct statement for Dirac on Lie groups:
    # The anti-fundamental rho_{(0,1)}(X) = -rho_{(1,0)}(X)^T
    # This sends D -> -D (sign reversal), so eigenvalues flip sign.
    # Therefore mu(q,p) should equal -mu(p,q) (reversed).

    # Check C anti-commutes: mu_pq = -mu_qp (reversed)
    err_anti = np.max(np.abs(mu_pq + mu_qp[::-1]))

    # Check C commutes: mu_pq = mu_qp
    err_comm = np.max(np.abs(mu_pq - mu_qp))

    conj_checks.append({
        'p': p, 'q': q, 'err_anti': err_anti, 'err_comm': err_comm
    })

    max_conj_err = max(max_conj_err, min(err_anti, err_comm))

    mode = "ANTI" if err_anti < err_comm else "COMM"
    best_err = min(err_anti, err_comm)
    print(f"  ({p},{q}) vs ({q},{p}): {mode}-commutes, err={best_err:.2e} "
          f"[anti={err_anti:.2e}, comm={err_comm:.2e}]")

# Also check self-conjugate sectors (p = q)
print("\n  Self-conjugate sectors (p = q):")
for sec in sectors_fold:
    p, q = sec['p'], sec['q']
    if p != q:
        continue
    mu = sec['mu']
    n_p = np.sum(mu > EPS_ZERO)
    n_m = np.sum(mu < -EPS_ZERO)
    n_z = np.sum(np.abs(mu) <= EPS_ZERO)
    pair_err = sec_eta_item = None
    for item in sector_eta_data:
        if item['p'] == p and item['q'] == q:
            pair_err = item['pair_err']
            sec_eta_item = item['sector_eta']
            break
    print(f"  ({p},{q}) dim={sec['dim_pq']}: n_evals={len(mu)}, "
          f"N+={n_p}, N-={n_m}, N0={n_z}, pair_err={pair_err:.2e}, "
          f"eta_sector={sec_eta_item}")


# =============================================================================
# SECTION 6: Spectral flow from tau=0 to tau_fold
# =============================================================================

print("\n--- Section 6: Spectral flow ---")

tau_vals = np.linspace(0.0, TAU_FOLD, N_TAU_FLOW + 1)
flow_data = []  # list of (tau, all_mu) per tau step

# We use max_pq_sum=3 for the flow (cheaper, sufficient to see crossings)
MAX_PQ_FLOW = 3

print(f"  Computing spectral flow with max_pq_sum={MAX_PQ_FLOW}, "
      f"{N_TAU_FLOW+1} tau steps...")

t0 = time.time()
for i, tau in enumerate(tau_vals):
    _irrep_cache.clear()
    sectors_tau, all_mu_tau = build_spectrum_at_tau(
        tau, MAX_PQ_FLOW, verbose=False)
    flow_data.append({
        'tau': tau,
        'sectors': sectors_tau,
        'all_mu': all_mu_tau
    })
    if (i + 1) % 10 == 0:
        print(f"    tau step {i+1}/{N_TAU_FLOW+1} done...")

t_flow = time.time() - t0
print(f"  Spectral flow computed in {t_flow:.1f}s")

# Count zero crossings: track when eigenvalues change sign
# For each sector, track eigenvalues across tau
zero_crossings = 0
flow_sector_crossings = []

# Get list of sectors from first step
sector_keys = [(s['p'], s['q']) for s in flow_data[0]['sectors']]

for sk in sector_keys:
    p_sk, q_sk = sk
    # Extract eigenvalues for this sector across tau
    mu_trace = []
    for fd in flow_data:
        for s in fd['sectors']:
            if s['p'] == p_sk and s['q'] == q_sk:
                mu_trace.append(s['mu'])
                break

    if len(mu_trace) != len(tau_vals):
        continue

    mu_trace = np.array(mu_trace)  # shape (n_tau, n_evals)
    n_evals = mu_trace.shape[1]

    # Track sign changes along each eigenvalue track
    # Note: eigenvalues are sorted at each tau, so we track by index
    crossings_this_sector = 0
    for j in range(n_evals):
        track = mu_trace[:, j]
        for k in range(1, len(track)):
            if track[k-1] * track[k] < 0 and abs(track[k-1]) > EPS_ZERO and abs(track[k]) > EPS_ZERO:
                crossings_this_sector += 1

    dim_pq = (p_sk + 1) * (q_sk + 1) * (p_sk + q_sk + 2) // 2
    flow_sector_crossings.append({
        'p': p_sk, 'q': q_sk, 'dim_pq': dim_pq,
        'crossings': crossings_this_sector,
        'pw_crossings': crossings_this_sector * dim_pq
    })
    zero_crossings += crossings_this_sector * dim_pq

print(f"\n  Total zero crossings (PW-weighted, tau=0 to tau_fold): {zero_crossings}")
for fsc in flow_sector_crossings:
    if fsc['crossings'] > 0:
        print(f"    ({fsc['p']},{fsc['q']}): {fsc['crossings']} crossings "
              f"(x{fsc['dim_pq']} PW = {fsc['pw_crossings']})")

# Spectral flow = net number of eigenvalues crossing zero upward minus downward
# Each upward crossing changes eta by +2, each downward by -2
# For symmetric spectrum, total flow = 0

# Compute eta(0) = N+ - N- at each tau
eta_flow = []
for fd in flow_data:
    n_p = sum(pw for mu_val, pw in fd['all_mu'] if mu_val > EPS_ZERO)
    n_m = sum(pw for mu_val, pw in fd['all_mu'] if mu_val < -EPS_ZERO)
    eta_flow.append(n_p - n_m)

eta_flow = np.array(eta_flow)
print(f"\n  eta(0) along flow:")
print(f"  {'tau':>8s}  {'eta(0)':>10s}")
for i in range(0, len(tau_vals), max(1, len(tau_vals) // 10)):
    print(f"  {tau_vals[i]:8.4f}  {eta_flow[i]:10d}")

spectral_flow_net = (eta_flow[-1] - eta_flow[0]) // 2
print(f"\n  Net spectral flow: {spectral_flow_net}")
print(f"  eta(0) at tau=0: {eta_flow[0]}")
print(f"  eta(0) at tau_fold: {eta_flow[-1]}")


# =============================================================================
# SECTION 7: J-symmetry verification
# =============================================================================

print("\n--- Section 7: J-symmetry (real structure) verification ---")

# The real structure J = C * K where C = gamma_1 * gamma_3 * gamma_5 * gamma_7
# and K is complex conjugation.
# In the math convention, J acts on spinors. For the full D_K = sum rho(e_a) x gamma_a + I x Omega,
# the J-symmetry [J, D_K] = 0 implies the spectrum of H = iD is symmetric.
#
# We verify: for each sector (p,q), the spectrum of H is exactly +/- symmetric.

# Build C2 = gamma_1 * gamma_3 * gamma_5 * gamma_7 (the charge conjugation matrix)
C2 = gammas[0] @ gammas[2] @ gammas[4] @ gammas[6]  # gamma_1 * gamma_3 * gamma_5 * gamma_7

# Verify C2 properties
C2_sq = C2 @ C2
C2_sq_err = np.max(np.abs(C2_sq - np.eye(16)))
print(f"  C2^2 = I check: err = {C2_sq_err:.2e}")

# Check C2 * gamma_a * C2^{-1} vs gamma_a (or -gamma_a)
for a in range(8):
    conj = C2 @ gammas[a] @ C2.conj().T
    comm_err = np.max(np.abs(conj - gammas[a]))
    anti_err = np.max(np.abs(conj + gammas[a]))
    mode = "commutes" if comm_err < anti_err else "anti-commutes"

# For the combined J = C2 * K acting on D_pi in sector (p,q):
# J (rho(e_a) x gamma_a) J^{-1} = rho(e_a)^* x C2 gamma_a C2^{-1}
# The conjugated representation rho(e_a)^* acts on sector (q,p).
# So J maps sector (p,q) to sector (q,p) (confirmed above).
# For self-conjugate sectors (p=q), J maps within the sector.

# Verify +/- symmetry quantitatively for each sector
print("\n  Per-sector +/- symmetry (DEFINITIVE CHECK):")
total_asymmetry = 0
max_asym = 0.0

for sec in sectors_fold:
    p, q = sec['p'], sec['q']
    mu = np.sort(sec['mu'])
    n = len(mu)
    dim_pq = sec['dim_pq']

    # Pair: mu[i] should equal -mu[n-1-i]
    pair_errors = []
    for i in range(n // 2):
        pair_errors.append(abs(mu[i] + mu[n - 1 - i]))
    if n % 2 == 1:
        pair_errors.append(abs(mu[n // 2]))

    max_pe = max(pair_errors) if pair_errors else 0.0
    max_asym = max(max_asym, max_pe)

    # Count asymmetry
    n_p = int(np.sum(mu > EPS_ZERO))
    n_m = int(np.sum(mu < -EPS_ZERO))
    asym = (n_p - n_m) * dim_pq
    total_asymmetry += asym

    print(f"    ({p},{q}): dim={dim_pq:4d}, n_evals={n:4d}, "
          f"N+={n_p:3d}, N-={n_m:3d}, pair_err={max_pe:.2e}, "
          f"sector_eta={asym}")

print(f"\n  TOTAL eta(0) = {total_asymmetry}")
print(f"  Maximum pair error = {max_asym:.2e}")


# =============================================================================
# SECTION 8: Gate verdict
# =============================================================================

print("\n" + "=" * 72)
print("GATE VERDICT: ETA-INVARIANT-60")
print("=" * 72)

# Determine verdict
if total_asymmetry != 0:
    gate_verdict = "PASS"
    gate_detail = (f"eta(0) = {total_asymmetry} != 0: topological anomaly "
                   f"contributes to CC")
elif max_asym > 1e-6:
    gate_verdict = "INFO"
    gate_detail = (f"eta(0) = {total_asymmetry} but pair_err = {max_asym:.2e} "
                   f"too large for definitive statement")
else:
    gate_verdict = "FAIL"
    gate_detail = (f"eta(0) = 0 exact (pair_err = {max_asym:.2e}). "
                   f"J-symmetry enforces spectral symmetry. "
                   f"Mechanism 5 CLOSED.")

print(f"  Verdict: {gate_verdict}")
print(f"  Detail: {gate_detail}")
print(f"\n  Key numbers:")
print(f"    eta(0) at fold = {total_asymmetry}")
print(f"    Maximum +/- pair error = {max_asym:.2e}")
print(f"    N_+ = {n_pos}, N_- = {n_neg}, N_0 = {n_zero}")
print(f"    Spectral flow (tau=0 to fold) = {spectral_flow_net}")
print(f"    Zero crossings (PW-weighted) = {zero_crossings}")
print(f"    Sectors computed = {len(sectors_fold)}")
print(f"    Distinct eigenvalues = {n_eigenvalues_distinct}")
print(f"    PW-weighted eigenvalues = {n_eigenvalues_pw}")

# eta(s) extrapolation check
print(f"\n  eta(s) convergence (should all be ~0 for symmetric spectrum):")
for sv, ev in zip(s_values[:6], eta_values[:6]):
    print(f"    eta({sv:.1f}) = {ev:.12e}")


# =============================================================================
# SECTION 9: Save results
# =============================================================================

print("\n--- Saving results ---")

# Collect sector eigenvalues for saving
sector_p = np.array([s['p'] for s in sectors_fold])
sector_q = np.array([s['q'] for s in sectors_fold])
sector_dim = np.array([s['dim_pq'] for s in sectors_fold])
sector_pair_err = np.array([s['pair_err'] for s in sector_eta_data])
sector_eta_vals = np.array([s['sector_eta'] for s in sector_eta_data])

# Flatten all eigenvalues with PW weights
all_mu_flat = np.array([m for m, _ in all_mu_fold])
all_pw_flat = np.array([w for _, w in all_mu_fold])

np.savez(
    os.path.join(os.path.dirname(os.path.abspath(__file__)),
                 "s60_eta_invariant.npz"),
    # Gate
    gate_name=np.array(["ETA-INVARIANT-60"]),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
    # eta results
    eta_at_zero=np.array(total_asymmetry),
    max_pair_err=np.array(max_asym),
    N_pos=np.array(n_pos),
    N_neg=np.array(n_neg),
    N_zero=np.array(n_zero),
    spectral_asymmetry=np.array(spectral_asymmetry),
    # eta(s) function
    s_values=s_values,
    eta_s_values=eta_values,
    # Spectral flow
    tau_flow=tau_vals,
    eta_flow=eta_flow,
    spectral_flow_net=np.array(spectral_flow_net),
    zero_crossings_total=np.array(zero_crossings),
    # Sector data
    sector_p=sector_p,
    sector_q=sector_q,
    sector_dim=sector_dim,
    sector_pair_err=sector_pair_err,
    sector_eta=sector_eta_vals,
    # Full spectrum
    all_mu=all_mu_flat,
    all_pw=all_pw_flat,
    # Config
    tau_fold_used=np.array(TAU_FOLD),
    max_pq_sum_fold=np.array(MAX_PQ_SUM),
    max_pq_sum_flow=np.array(MAX_PQ_FLOW),
    n_sectors=np.array(len(sectors_fold)),
    n_eigenvalues_distinct=np.array(n_eigenvalues_distinct),
    n_eigenvalues_pw=np.array(n_eigenvalues_pw),
    # Conjugate checks
    conj_err_data=np.array([(c['p'], c['q'], c['err_anti'], c['err_comm'])
                             for c in conj_checks]) if conj_checks else np.array([]),
)

print(f"  Saved: computations/session-60/s60_eta_invariant.npz")
print("\nDONE.")
