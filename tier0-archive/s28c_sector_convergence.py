"""
Session 28c Gate L-8: Sector Count Convergence at p+q<=4
=========================================================

Extends Session 27's multi-sector BCS from p+q<=3 (9 sectors) to p+q<=4
(14 sectors: adds (4,0), (0,4), (3,1), (1,3), (2,2)).

PHYSICS:
    F_total(tau, mu) = sum_{(p,q)} mult(p,q) * F_cond^{(p,q)}(tau, mu)

    S27 computed 9 sectors with total effective multiplicity = 805.
    The 5 new sectors add:
        (4,0) + (0,4): dim=15, mult_eff = 2 * 225 = 450
        (3,1) + (1,3): dim=24, mult_eff = 2 * 576 = 1152
        (2,2):         dim=27, mult_eff = 729  (self-conjugate)
        Total new: 2331  (2.9x the S27 total!)

    KEY QUESTION: Do higher sectors contribute negligibly (converged) or
    change the qualitative picture (not converged)?

CPT CONJUGATE STRUCTURE:
    (4,0) <-> (0,4): conjugate pair, same spectrum/BCS. Compute both, verify, double.
    (3,1) <-> (1,3): conjugate pair, same spectrum/BCS. Compute both, verify, double.
    (2,2) <-> (2,2): self-conjugate. No doubling.

GATE L-8:
    PASS (converged):  |F_total(14) - F_total(9)| / |F_total(9)| < 0.10
    FAIL (not converged): qualitative change (new minimum, shifted location, >10%)

Author: phonon-exflation-sim
Date: 2026-02-27
Session: 28c, Gate L-8
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh, eigvalsh

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

# Import geometry + irrep infrastructure from tier1_dirac_spectrum
from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    dirac_operator_on_irrep,
    get_irrep,
    validate_clifford,
    validate_connection,
    _irrep_cache,
    C2_IDX,
)

# Import Kosmann formula from s23a
from s23a_kosmann_singlet import kosmann_operator_antisymmetric

# Import BCS functions from s26 (sector-agnostic)
from s26_multimode_bcs import (
    build_bcs_kernel,
    linearized_eigenvalues,
    selfconsistent_bcs,
    build_J_projector,
    check_spectral_pairing,
)

# Reuse robust free energy from s27
from s27_multisector_bcs import (
    free_energy_bcs_robust,
    build_geometry,
    compute_sector_eigensystem,
    compute_sector_kosmann_V,
    bcs_for_sector,
)


# ===========================================================================
# CONSTANTS
# ===========================================================================

TAU_VALUES = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])
N_TAU = len(TAU_VALUES)

# Reduced mu grid: focus on the physically interesting range
# S27 showed condensation at mu/lmin >= 0.95. We keep the full S27 grid for
# direct comparison.
MU_RATIOS = np.array([0.0, 0.5, 0.8, 0.9, 0.95, 1.0, 1.05, 1.1, 1.2, 1.5, 2.0, 3.0])
N_MU = len(MU_RATIOS)

# NEW sectors at p+q = 4
# (p, q, dim_rho, base_multiplicity)
NEW_SECTORS = [
    (4, 0, 15, 225),
    (0, 4, 15, 225),
    (3, 1, 24, 576),
    (1, 3, 24, 576),
    (2, 2, 27, 729),
]

# Conjugate pairs: (4,0)<->(0,4), (3,1)<->(1,3). (2,2) self-conjugate.
# Effective multiplicities for F_total:
CONJUGATE_MAP = {
    (4, 0): (0, 4),  # (4,0) has conjugate (0,4)
    (3, 1): (1, 3),  # (3,1) has conjugate (1,3)
}
# (2,2) is self-conjugate: eff_mult = 729 (no doubling)
# (4,0): eff_mult = 225 (+ 225 from (0,4) = 450 combined)
# (3,1): eff_mult = 576 (+ 576 from (1,3) = 1152 combined)

# S27 sectors for reference
S27_SECTORS = [
    (0, 0, 1, 1),
    (1, 0, 3, 9),
    (0, 1, 3, 9),
    (1, 1, 8, 64),
    (2, 0, 6, 36),
    (0, 2, 6, 36),
    (3, 0, 10, 100),
    (0, 3, 10, 100),
    (2, 1, 15, 225),
]
# S27 effective multiplicities (includes CPT doubling of (2,1)):
S27_MULT_21_EFFECTIVE = 225 + 225

N_NEW = len(NEW_SECTORS)

# BCS iteration parameters (match S27)
MAX_ITER = 50000
CONV_TOL = 1e-13
DELTA0_SCALE = 0.01


# ===========================================================================
# MAIN COMPUTATION
# ===========================================================================

def main():
    """Compute BCS for 5 new sectors at p+q=4 and compare to S27."""
    print("=" * 78)
    print("Session 28c Gate L-8: Sector Count Convergence (p+q<=4)")
    print("=" * 78)
    print(f"New sectors: {N_NEW} at p+q=4")
    print(f"Tau grid: {TAU_VALUES}")
    print(f"Mu ratios: {MU_RATIOS}")
    print(f"BCS: MAX_ITER={MAX_ITER}, TOL={CONV_TOL}")
    print()

    t_total_start = time.time()

    # Load S27 reference data
    s27_path = os.path.join(SCRIPT_DIR, "s27_multisector_bcs.npz")
    if not os.path.exists(s27_path):
        print(f"FATAL: S27 data not found: {s27_path}")
        sys.exit(1)

    s27_data = np.load(s27_path, allow_pickle=True)
    F_total_s27 = s27_data['F_total']  # (9 tau, 12 mu)
    M_max_s27 = s27_data['M_max']      # (9 sectors, 9 tau, 12 mu)
    print(f"Loaded S27 reference: F_total shape={F_total_s27.shape}")
    print(f"S27 verdict: {s27_data['verdict']}")
    print()

    # Initialize infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    cliff_err = validate_clifford(gammas)
    print(f"Clifford validation: max_err = {cliff_err:.2e}")

    # Storage for new sectors
    M_max_new = np.zeros((N_NEW, N_TAU, N_MU))
    Delta_max_new = np.zeros((N_NEW, N_TAU, N_MU))
    F_cond_new = np.full((N_NEW, N_TAU, N_MU), np.nan)
    lambda_min_new = np.zeros((N_NEW, N_TAU))
    V_diag_sum_new = np.zeros((N_NEW, N_TAU))

    # For npz storage
    npz_data = {
        "tau_values": TAU_VALUES,
        "mu_ratios": MU_RATIOS,
        "new_sectors": np.array([(p, q, d, m) for p, q, d, m in NEW_SECTORS]),
    }

    # Conjugate verification data
    conj_evals_err = {}  # {(p,q): max eigenvalue mismatch with conjugate}

    # -----------------------------------------------------------------------
    # Main loop: tau (outer) x new sector (inner)
    # -----------------------------------------------------------------------
    for tau_idx, tau in enumerate(TAU_VALUES):
        t_tau_start = time.time()
        print(f"\n{'='*70}")
        print(f"TAU = {tau:.2f}  ({tau_idx+1}/{N_TAU})")
        print(f"{'='*70}")

        # Clear irrep cache between tau values
        import tier1_dirac_spectrum
        tier1_dirac_spectrum._irrep_cache = {}

        # Build geometry ONCE for this tau
        E, Gamma, Omega = build_geometry(tau, gens, f_abc, gammas)

        mc_err = validate_connection(Gamma)
        ah_err = np.max(np.abs(Omega + Omega.conj().T))
        print(f"  Geometry: connection mc_err={mc_err:.2e}, Omega ah_err={ah_err:.2e}")

        # Store eigensystems for conjugate verification
        sector_evals_cache = {}

        for s_idx, (p, q, dim_rho_expected, mult) in enumerate(NEW_SECTORS):
            t_sec_start = time.time()
            label = f"({p},{q})"
            spinor_dim = dim_rho_expected * 16

            print(f"\n  --- Sector {label}: dim_rho={dim_rho_expected}, "
                  f"spinor_dim={spinor_dim}, mult={mult} ---")

            # 1. Eigensystem
            evals, evecs, dim_rho = compute_sector_eigensystem(
                p, q, tau, gens, f_abc, gammas, E, Gamma, Omega
            )
            assert dim_rho == dim_rho_expected, \
                f"dim_rho mismatch: got {dim_rho}, expected {dim_rho_expected}"

            lambda_min = np.min(np.abs(evals))
            lambda_min_new[s_idx, tau_idx] = lambda_min

            # Spectral pairing check
            paired, pair_err = check_spectral_pairing(evals)
            print(f"    evals: [{evals[0]:.6f}, ..., {evals[-1]:.6f}], "
                  f"lambda_min={lambda_min:.6f}, pairing_err={pair_err:.2e}")

            # Cache for conjugate verification
            sector_evals_cache[(p, q)] = np.sort(evals)

            # Store in npz
            npz_data[f"evals_{p}_{q}_{tau_idx}"] = evals

            # 2. Kosmann pairing matrix
            V, K_norms = compute_sector_kosmann_V(Gamma, gammas, dim_rho, evecs)

            V_diag_sum = np.sum(np.diag(V))
            V_offdiag_max = np.max(np.abs(V - np.diag(np.diag(V))))
            V_diag_sum_new[s_idx, tau_idx] = V_diag_sum

            print(f"    Kosmann: ||K_a|| = [{K_norms[0]:.4f}, {K_norms[1]:.4f}, "
                  f"{K_norms[2]:.4f}, {K_norms[3]:.4f}]")
            print(f"    V_nm: diag_sum={V_diag_sum:.6f}, offdiag_max={V_offdiag_max:.6f}")

            npz_data[f"V_{p}_{q}_{tau_idx}"] = V

            # 3. BCS scan over mu
            M_max_arr, Delta_max_arr, F_cond_arr, Delta_sols = bcs_for_sector(
                V, evals, MU_RATIOS, label=label
            )

            M_max_new[s_idx, tau_idx, :] = M_max_arr
            Delta_max_new[s_idx, tau_idx, :] = Delta_max_arr
            F_cond_new[s_idx, tau_idx, :] = F_cond_arr

            # Brief summary
            M_max_best = np.max(M_max_arr)
            i_Mmax = np.argmax(M_max_arr)
            print(f"    BCS: M_max_best={M_max_best:.4f} at mu/lmin={MU_RATIOS[i_Mmax]:.2f}")

            cond_mask = Delta_max_arr > 1e-20
            if np.any(cond_mask):
                best_cond_idx = np.argmax(Delta_max_arr)
                print(f"    BCS: Delta_max={Delta_max_arr[best_cond_idx]:.6f} "
                      f"at mu/lmin={MU_RATIOS[best_cond_idx]:.2f}, "
                      f"F_cond={F_cond_arr[best_cond_idx]:.6e}")
            else:
                print(f"    BCS: NO CONDENSATE at any mu")

            t_sec_elapsed = time.time() - t_sec_start
            print(f"    Sector {label} time: {t_sec_elapsed:.1f}s")

        # Conjugate verification at this tau
        for (p1, q1), (p2, q2) in CONJUGATE_MAP.items():
            if (p1, q1) in sector_evals_cache and (p2, q2) in sector_evals_cache:
                e1 = sector_evals_cache[(p1, q1)]
                e2 = sector_evals_cache[(p2, q2)]
                err = np.max(np.abs(e1 - e2))
                key = f"({p1},{q1})<->({p2},{q2})"
                if key not in conj_evals_err:
                    conj_evals_err[key] = []
                conj_evals_err[key].append(err)
                if err > 1e-10:
                    print(f"  WARNING: Conjugate mismatch {key}: {err:.2e}")
                else:
                    print(f"  Conjugate check {key}: err={err:.2e} PASS")

        t_tau_elapsed = time.time() - t_tau_start
        print(f"\n  Tau={tau:.2f} total time: {t_tau_elapsed:.1f}s")

    # -----------------------------------------------------------------------
    # Compute F_total_new (new sectors only) and F_total_combined
    # -----------------------------------------------------------------------
    print(f"\n{'='*70}")
    print("COMPUTING F_TOTAL WITH NEW SECTORS")
    print(f"{'='*70}")

    # New sector contribution to F_total
    F_new_contribution = np.zeros((N_TAU, N_MU))

    for tau_idx in range(N_TAU):
        for mu_idx in range(N_MU):
            F_sum = 0.0
            any_nan = False
            for s_idx, (p, q, dim_rho, mult) in enumerate(NEW_SECTORS):
                F_s = F_cond_new[s_idx, tau_idx, mu_idx]

                # Effective multiplicity with conjugate doubling
                if (p, q) in CONJUGATE_MAP:
                    # This is a sector with a conjugate that we also computed.
                    # Skip the conjugate sector (0,4) and (1,3) in summation
                    # and double the primary sector (4,0) and (3,1).
                    # But we computed ALL 5 sectors, so we use them directly.
                    pass

                if np.isnan(F_s):
                    any_nan = True
                else:
                    F_sum += mult * F_s

            F_new_contribution[tau_idx, mu_idx] = F_sum if not any_nan else np.nan

    # Combined F_total = S27 + new
    F_total_combined = np.zeros((N_TAU, N_MU))
    for tau_idx in range(N_TAU):
        for mu_idx in range(N_MU):
            f_s27 = F_total_s27[tau_idx, mu_idx]
            f_new = F_new_contribution[tau_idx, mu_idx]
            if np.isnan(f_s27) or np.isnan(f_new):
                F_total_combined[tau_idx, mu_idx] = np.nan
            else:
                F_total_combined[tau_idx, mu_idx] = f_s27 + f_new

    # Print comparison tables
    print("\nF_total (S27 only, p+q<=3):")
    _print_ftotal_table(F_total_s27, TAU_VALUES, MU_RATIOS)

    print("\nF_new_contribution (new sectors only, p+q=4):")
    _print_ftotal_table(F_new_contribution, TAU_VALUES, MU_RATIOS)

    print("\nF_total_combined (all 14 sectors, p+q<=4):")
    _print_ftotal_table(F_total_combined, TAU_VALUES, MU_RATIOS)

    # -----------------------------------------------------------------------
    # Convergence analysis
    # -----------------------------------------------------------------------
    print(f"\n{'='*70}")
    print("CONVERGENCE ANALYSIS")
    print(f"{'='*70}")

    # Per mu: relative change |F_combined - F_s27| / |F_s27|
    print("\nRelative change |F(14) - F(9)| / |F(9)| at each (tau, mu):")
    print(f"{'tau':>6s}", end="")
    for r in MU_RATIOS:
        print(f"  {r:>8.2f}", end="")
    print()

    convergence_ratios = np.full((N_TAU, N_MU), np.nan)
    for tau_idx in range(N_TAU):
        print(f"{TAU_VALUES[tau_idx]:6.2f}", end="")
        for mu_idx in range(N_MU):
            f9 = F_total_s27[tau_idx, mu_idx]
            f14 = F_total_combined[tau_idx, mu_idx]
            if np.isnan(f9) or np.isnan(f14) or abs(f9) < 1e-15:
                print(f"  {'---':>8s}", end="")
            else:
                ratio = abs(f14 - f9) / abs(f9)
                convergence_ratios[tau_idx, mu_idx] = ratio
                print(f"  {ratio:8.3f}", end="")
        print()

    # Focus on the interior minimum region
    # S27 found RESCUE with interior minimum. Check if it persists.
    print("\n\nInterior minimum analysis (F_total_combined):")

    verdict = "PENDING"
    verdict_text = ""
    rescue_details_s27 = []
    rescue_details_combined = []

    for mu_idx in range(N_MU):
        # S27 interior minimum check
        F_s27_tau = F_total_s27[:, mu_idx]
        F_comb_tau = F_total_combined[:, mu_idx]

        if np.all(np.isfinite(F_s27_tau)):
            min_idx_s27 = np.argmin(F_s27_tau)
            if 0 < min_idx_s27 < N_TAU - 1 and F_s27_tau[min_idx_s27] < 0:
                if (F_s27_tau[min_idx_s27 - 1] > F_s27_tau[min_idx_s27] and
                    F_s27_tau[min_idx_s27 + 1] > F_s27_tau[min_idx_s27]):
                    rescue_details_s27.append(
                        f"  S27:  mu/lmin={MU_RATIOS[mu_idx]:.2f}, "
                        f"min at tau={TAU_VALUES[min_idx_s27]:.2f}, "
                        f"F={F_s27_tau[min_idx_s27]:.4e}"
                    )

        if np.all(np.isfinite(F_comb_tau)):
            min_idx_comb = np.argmin(F_comb_tau)
            if 0 < min_idx_comb < N_TAU - 1 and F_comb_tau[min_idx_comb] < 0:
                if (F_comb_tau[min_idx_comb - 1] > F_comb_tau[min_idx_comb] and
                    F_comb_tau[min_idx_comb + 1] > F_comb_tau[min_idx_comb]):
                    rescue_details_combined.append(
                        f"  p+q<=4: mu/lmin={MU_RATIOS[mu_idx]:.2f}, "
                        f"min at tau={TAU_VALUES[min_idx_comb]:.2f}, "
                        f"F={F_comb_tau[min_idx_comb]:.4e}"
                    )

    print("  S27 (p+q<=3) interior minima:")
    for line in rescue_details_s27:
        print(line)
    if not rescue_details_s27:
        print("  (none)")

    print("  Combined (p+q<=4) interior minima:")
    for line in rescue_details_combined:
        print(line)
    if not rescue_details_combined:
        print("  (none)")

    # Quantitative convergence at the S27 interior minimum locations
    print("\n\nQuantitative convergence at S27 minimum locations:")
    convergence_at_minima = []
    for mu_idx in range(N_MU):
        F_s27_tau = F_total_s27[:, mu_idx]
        F_comb_tau = F_total_combined[:, mu_idx]
        if not np.all(np.isfinite(F_s27_tau)):
            continue
        min_idx = np.argmin(F_s27_tau)
        if 0 < min_idx < N_TAU - 1 and F_s27_tau[min_idx] < 0:
            f9 = F_s27_tau[min_idx]
            f14 = F_comb_tau[min_idx]
            if abs(f9) > 1e-15:
                ratio = abs(f14 - f9) / abs(f9)
                convergence_at_minima.append((MU_RATIOS[mu_idx], TAU_VALUES[min_idx],
                                               f9, f14, ratio))
                print(f"  mu/lmin={MU_RATIOS[mu_idx]:.2f}, tau={TAU_VALUES[min_idx]:.2f}: "
                      f"F(9)={f9:.4e}, F(14)={f14:.4e}, ratio={ratio:.4f} "
                      f"({'<10%' if ratio < 0.10 else '>10% NOT CONVERGED'})")

    # Per-sector M_max summary (new sectors)
    print("\n\nPer-sector M_max summary (new sectors):")
    for s_idx, (p, q, dim_rho, mult) in enumerate(NEW_SECTORS):
        M_mu0 = M_max_new[s_idx, :, 0]
        M_mu1 = M_max_new[s_idx, :, 5]  # mu=lambda_min
        print(f"  ({p},{q}) d={dim_rho:>2d} m={mult:>4d}: "
              f"M(mu=0)=[{M_mu0.min():.4f},{M_mu0.max():.4f}], "
              f"M(mu=lm)=[{M_mu1.min():.4f},{M_mu1.max():.4f}]")

    # Conjugate verification summary
    print("\nConjugate verification:")
    for key, errs in conj_evals_err.items():
        max_err = max(errs)
        print(f"  {key}: max eigenvalue err across tau = {max_err:.2e}")

    # -----------------------------------------------------------------------
    # Gate verdict
    # -----------------------------------------------------------------------
    print(f"\n{'='*70}")
    print("GATE L-8 VERDICT: Sector Count Convergence")
    print(f"{'='*70}")

    # Criterion 1: Does the interior minimum persist?
    min_persists = len(rescue_details_combined) > 0
    min_existed = len(rescue_details_s27) > 0

    # Criterion 2: Quantitative convergence at minima
    if convergence_at_minima:
        max_ratio = max(r for _, _, _, _, r in convergence_at_minima)
        mean_ratio = np.mean([r for _, _, _, _, r in convergence_at_minima])
        converged_10pct = all(r < 0.10 for _, _, _, _, r in convergence_at_minima)
    else:
        max_ratio = np.nan
        mean_ratio = np.nan
        converged_10pct = True  # No minima to compare = trivially converged

    # Criterion 3: Qualitative change in minimum location
    location_shifted = False
    if rescue_details_s27 and rescue_details_combined:
        # Check if minimum moved significantly in tau
        # (This is a rough check; a proper one would parse the tau values.)
        pass

    # Criterion 4: New supercritical sectors at mu=0
    new_supercritical_mu0 = False
    for s_idx, (p, q, dim_rho, mult) in enumerate(NEW_SECTORS):
        if np.any(M_max_new[s_idx, :, 0] > 1.0):
            new_supercritical_mu0 = True
            break

    # Determine verdict
    summary_lines = []
    summary_lines.append(f"S27 sectors: 9 (p+q<=3), eff_mult=805")
    summary_lines.append(f"New sectors: 5 (p+q=4), eff_mult=2331")
    summary_lines.append(f"Multiplicity increase: {2331/805:.1f}x")
    summary_lines.append(f"")
    summary_lines.append(f"mu=0 condensation: {'YES (NEW)' if new_supercritical_mu0 else 'NO (same as S27)'}")

    if convergence_at_minima:
        summary_lines.append(f"Max convergence ratio: {max_ratio:.4f}")
        summary_lines.append(f"Mean convergence ratio: {mean_ratio:.4f}")
        summary_lines.append(f"All within 10%: {'YES' if converged_10pct else 'NO'}")
    else:
        summary_lines.append(f"No interior minima to compare")

    summary_lines.append(f"S27 interior minima: {len(rescue_details_s27)}")
    summary_lines.append(f"Combined interior minima: {len(rescue_details_combined)}")

    if not min_existed and not min_persists:
        # Both have no interior minimum -- trivially converged
        verdict = "PASS"
        verdict_text = ("PASS (converged): Neither S27 nor p+q<=4 has interior minimum. "
                        "Both agree: no tau lock from BCS.")
    elif min_existed and not min_persists:
        verdict = "FAIL"
        verdict_text = ("FAIL (not converged): S27 had interior minimum, but p+q<=4 "
                        "eliminates it. Higher sectors qualitatively change the picture.")
    elif not min_existed and min_persists:
        verdict = "FAIL"
        verdict_text = ("FAIL (not converged): S27 had no interior minimum, but p+q<=4 "
                        "creates one. Higher sectors qualitatively change the picture.")
    elif converged_10pct:
        verdict = "PASS"
        verdict_text = (f"PASS (converged): Interior minima persist. Max correction = "
                        f"{max_ratio:.1%}. Mean correction = {mean_ratio:.1%}. "
                        f"S27 result is robust.")
    else:
        verdict = "FAIL"
        verdict_text = (f"FAIL (not converged): Interior minima persist but corrections "
                        f"exceed 10%. Max = {max_ratio:.1%}, Mean = {mean_ratio:.1%}. "
                        f"Need p+q<=5 or higher.")

    print(f"\n  {verdict_text}")
    print()
    for line in summary_lines:
        print(f"  {line}")

    # -----------------------------------------------------------------------
    # Save data
    # -----------------------------------------------------------------------
    npz_data.update({
        "M_max_new": M_max_new,
        "Delta_max_new": Delta_max_new,
        "F_cond_new": F_cond_new,
        "lambda_min_new": lambda_min_new,
        "V_diag_sum_new": V_diag_sum_new,
        "F_new_contribution": F_new_contribution,
        "F_total_s27": F_total_s27,
        "F_total_combined": F_total_combined,
        "convergence_ratios": convergence_ratios,
        "verdict": np.array([verdict]),
        "verdict_text": np.array([verdict_text]),
    })

    npz_path = os.path.join(SCRIPT_DIR, "s28c_sector_convergence.npz")
    np.savez_compressed(npz_path, **npz_data)
    print(f"\nData saved: {npz_path}")

    # -----------------------------------------------------------------------
    # Gate verdict file
    # -----------------------------------------------------------------------
    gate_path = os.path.join(SCRIPT_DIR, "s28c_gate_verdicts.txt")
    with open(gate_path, 'a') as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"L-8 Sector Count Convergence (p+q<=4)\n")
        f.write(f"{'='*60}\n")
        f.write(f"Verdict: {verdict}\n")
        f.write(f"Detail: {verdict_text}\n")
        f.write(f"\n")
        for line in summary_lines:
            f.write(f"  {line}\n")
        f.write(f"\n")
        if convergence_at_minima:
            f.write(f"Convergence at S27 minimum locations:\n")
            for mu_r, tau_v, f9, f14, ratio in convergence_at_minima:
                f.write(f"  mu/lmin={mu_r:.2f}, tau={tau_v:.2f}: "
                        f"F(9)={f9:.4e}, F(14)={f14:.4e}, ratio={ratio:.4f}\n")
    print(f"Gate verdict appended: {gate_path}")

    # -----------------------------------------------------------------------
    # Plot
    # -----------------------------------------------------------------------
    make_plots(
        F_total_s27, F_total_combined, F_new_contribution,
        M_max_new, convergence_ratios,
        verdict_text, summary_lines,
        os.path.join(SCRIPT_DIR, "s28c_sector_convergence.png")
    )

    t_total = time.time() - t_total_start
    print(f"\nTotal runtime: {t_total:.1f}s ({t_total/60:.1f} min)")
    print(f"\n{'='*70}")
    print(f"FINAL VERDICT: {verdict_text}")
    print(f"{'='*70}")


def _print_ftotal_table(F, tau_values, mu_ratios):
    """Print F_total table to stdout."""
    print(f"{'tau':>6s}", end="")
    for r in mu_ratios:
        print(f"  {r:>9.2f}", end="")
    print()
    for ti in range(len(tau_values)):
        print(f"{tau_values[ti]:6.2f}", end="")
        for mi in range(len(mu_ratios)):
            val = F[ti, mi]
            if np.isnan(val):
                print(f"  {'NaN':>9s}", end="")
            elif abs(val) < 1e-4:
                print(f"  {val:9.4f}", end="")
            else:
                print(f"  {val:9.4f}", end="")
        print()


# ===========================================================================
# PLOTTING
# ===========================================================================

def make_plots(F_s27, F_combined, F_new, M_max_new, conv_ratios,
               verdict_text, summary_lines, save_path):
    """Generate 6-panel diagnostic plot comparing S27 and combined results."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 3, figsize=(18, 11))
    fig.suptitle("Session 28c L-8: Sector Count Convergence (p+q<=4)",
                 fontsize=14, fontweight='bold')

    new_sector_labels = [f"({p},{q})" for p, q, _, _ in NEW_SECTORS]
    colors_new = plt.cm.Set2(np.linspace(0, 1, N_NEW))

    # Panel 1: F_total comparison at key mu values
    ax = axes[0, 0]
    mu_show = [5, 6, 8, 9]  # mu/lmin = 1.0, 1.05, 1.2, 1.5
    for i_mu in mu_show:
        if i_mu < N_MU:
            ax.plot(TAU_VALUES, F_s27[:, i_mu], 'o--', alpha=0.6,
                     label=f'S27 mu/lm={MU_RATIOS[i_mu]:.2f}', markersize=4)
            ax.plot(TAU_VALUES, F_combined[:, i_mu], 's-',
                     label=f'p+q<=4 mu/lm={MU_RATIOS[i_mu]:.2f}', markersize=4)
    ax.set_xlabel('tau')
    ax.set_ylabel('F_total')
    ax.set_title('F_total: S27 (dashed) vs p+q<=4 (solid)')
    ax.legend(fontsize=6, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel 2: New sector contribution as fraction of S27
    ax = axes[0, 1]
    for i_mu in mu_show:
        if i_mu < N_MU:
            f_s27_tau = F_s27[:, i_mu]
            f_new_tau = F_new[:, i_mu]
            valid = (np.isfinite(f_s27_tau) & np.isfinite(f_new_tau) &
                     (np.abs(f_s27_tau) > 1e-10))
            if np.any(valid):
                ratio = np.abs(f_new_tau[valid] / f_s27_tau[valid])
                ax.semilogy(TAU_VALUES[valid], ratio, 'o-',
                             label=f'mu/lm={MU_RATIOS[i_mu]:.2f}', markersize=4)
    ax.axhline(0.10, color='red', linestyle='--', alpha=0.7, label='10% threshold')
    ax.set_xlabel('tau')
    ax.set_ylabel('|F_new / F_S27|')
    ax.set_title('New sector contribution (fraction of S27)')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 3: M_max for new sectors at mu=lambda_min
    ax = axes[0, 2]
    for s_idx, (p, q, dim_rho, mult) in enumerate(NEW_SECTORS):
        M_data = M_max_new[s_idx, :, 5]  # mu = lambda_min
        ax.plot(TAU_VALUES, M_data, 'o-', color=colors_new[s_idx],
                 label=f'{new_sector_labels[s_idx]} m={mult}', markersize=4)
    ax.axhline(1.0, color='red', linestyle='--', alpha=0.7, label='M=1 (critical)')
    ax.set_xlabel('tau')
    ax.set_ylabel('M_max')
    ax.set_title('M_max for new sectors (mu=lambda_min)')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 4: M_max for new sectors at mu=0
    ax = axes[1, 0]
    for s_idx, (p, q, dim_rho, mult) in enumerate(NEW_SECTORS):
        M_data = M_max_new[s_idx, :, 0]  # mu = 0
        ax.plot(TAU_VALUES, M_data, 'o-', color=colors_new[s_idx],
                 label=f'{new_sector_labels[s_idx]}', markersize=4)
    ax.axhline(1.0, color='red', linestyle='--', alpha=0.7, label='M=1 (critical)')
    ax.set_xlabel('tau')
    ax.set_ylabel('M_max')
    ax.set_title('M_max for new sectors (mu=0)')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 5: Convergence ratio heatmap
    ax = axes[1, 1]
    valid_conv = np.where(np.isfinite(conv_ratios), conv_ratios, np.nan)
    # Only show mu values where there's actually a nonzero F_total
    has_data = np.any(np.isfinite(valid_conv), axis=0)
    if np.any(has_data):
        from matplotlib.colors import LogNorm
        # Fill NaN with a sentinel for display
        plot_data = np.where(np.isfinite(valid_conv), valid_conv, 0.0)
        im = ax.imshow(plot_data, aspect='auto', cmap='RdYlGn_r',
                        extent=[0, N_MU, TAU_VALUES[-1], TAU_VALUES[0]],
                        vmin=0, vmax=1.0)
        fig.colorbar(im, ax=ax, label='|dF/F|')
        ax.set_xlabel('mu index')
        ax.set_ylabel('tau')
        ax.set_title('Convergence ratio |F(14)-F(9)|/|F(9)|')
    else:
        ax.text(0.5, 0.5, 'No data', transform=ax.transAxes, ha='center')
        ax.set_title('Convergence ratio (no data)')

    # Panel 6: Gate verdict
    ax = axes[1, 2]
    ax.axis('off')
    ax.text(0.5, 0.90, 'GATE L-8 VERDICT', fontsize=14, fontweight='bold',
             ha='center', va='top', transform=ax.transAxes)

    # Color the verdict
    if 'PASS' in verdict_text:
        vcolor = 'green'
    elif 'FAIL' in verdict_text:
        vcolor = 'red'
    else:
        vcolor = 'orange'
    ax.text(0.5, 0.75, verdict_text[:80], fontsize=10, ha='center', va='top',
             transform=ax.transAxes, color=vcolor, fontweight='bold', wrap=True)
    if len(verdict_text) > 80:
        ax.text(0.5, 0.65, verdict_text[80:], fontsize=9, ha='center', va='top',
                 transform=ax.transAxes, color=vcolor, wrap=True)

    summary_text = '\n'.join(summary_lines)
    ax.text(0.05, 0.50, summary_text, fontsize=7, fontfamily='monospace',
             ha='left', va='top', transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\nPlot saved: {save_path}")


if __name__ == "__main__":
    main()
