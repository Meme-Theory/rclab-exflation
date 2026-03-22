"""
Session 19a: Generate eigenvalue sweep data for spectral diagnostics S-1 through S-4.

Calls collect_spectrum() at 21 tau-values (0.0, 0.1, ..., 2.0) with max_pq_sum=6.
Stores all eigenvalues, sector labels (p,q), and multiplicities in a .npz file.

Environment: System Python (numpy + scipy only, no GPU).
Runtime: ~8.7s per tau-value at max_pq_sum=6 => ~3 minutes total.

Author: phonon-exflation-sim agent (Session 19a)
Date: 2026-02-15
"""

import sys
import os
import time
import numpy as np

# Add tier0-computation to path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    build_cliff8,
    collect_spectrum,
)


def generate_sweep_data(tau_values, max_pq_sum=6, verbose=True):
    """
    Generate eigenvalue data at each tau-value for all irreps up to max_pq_sum.

    For each tau, we store:
      - The absolute eigenvalues |lambda| (sorted, distinct within each sector)
      - The sector labels (p, q) for each eigenvalue
      - The Peter-Weyl multiplicity dim(p,q) for each eigenvalue

    The PW multiplicity dim(p,q) is the correct per-eigenvalue weight for all
    spectral sums (heat kernel, partition function, entropy). Each sector (p,q)
    contributes dim(p,q)*16 distinct eigenvalues from D_pi, and each appears
    dim(p,q) times in the full L^2(SU(3)) spectrum via Peter-Weyl.

    Returns:
        data: dict with keys:
            'tau_values': (N_tau,) array
            'eigenvalues': list of N_tau arrays, each (N_evals,) of |lambda|
            'sector_p': list of N_tau arrays, each (N_evals,) of int p-label
            'sector_q': list of N_tau arrays, each (N_evals,) of int q-label
            'multiplicities': list of N_tau arrays, each (N_evals,) of int PW mult dim(p,q)
    """
    # Initialize infrastructure (computed once, reused across all tau)
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    all_abs_evals = []
    all_sector_p = []
    all_sector_q = []
    all_pw_mult = []

    t_total_start = time.time()

    for i, tau in enumerate(tau_values):
        t_start = time.time()
        if verbose:
            print(f"\n=== tau = {tau:.2f}  ({i+1}/{len(tau_values)}) ===")

        # collect_spectrum returns:
        #   all_eigenvalues: list of (eigenvalue_complex, pw_multiplicity)
        #   eval_data: list of (p, q, eigenvalues_array) per sector
        all_evals_raw, eval_data = collect_spectrum(
            tau, gens, f_abc, gammas,
            max_pq_sum=max_pq_sum, verbose=False
        )

        # Extract per-eigenvalue data from eval_data (sector-labeled)
        abs_evals = []
        sector_p = []
        sector_q = []
        pw_mult = []

        for (p, q, evals_array) in eval_data:
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
            for ev in evals_array:
                abs_ev = np.abs(ev)
                abs_evals.append(abs_ev)
                sector_p.append(p)
                sector_q.append(q)
                pw_mult.append(dim_pq)

        abs_evals = np.array(abs_evals, dtype=np.float64)
        sector_p = np.array(sector_p, dtype=np.int32)
        sector_q = np.array(sector_q, dtype=np.int32)
        pw_mult = np.array(pw_mult, dtype=np.int32)

        all_abs_evals.append(abs_evals)
        all_sector_p.append(sector_p)
        all_sector_q.append(sector_q)
        all_pw_mult.append(pw_mult)

        dt = time.time() - t_start
        n_evals = len(abs_evals)
        n_sectors = len(eval_data)
        total_mult = np.sum(pw_mult)
        if verbose:
            print(f"  {n_evals} eigenvalues, {n_sectors} sectors, "
                  f"total PW mult = {total_mult}, time = {dt:.1f}s")

    total_time = time.time() - t_total_start
    if verbose:
        print(f"\n=== Total sweep time: {total_time:.1f}s ===")

    return {
        'tau_values': np.array(tau_values),
        'eigenvalues': all_abs_evals,
        'sector_p': all_sector_p,
        'sector_q': all_sector_q,
        'multiplicities': all_pw_mult,
    }


def save_sweep_data(data, output_path):
    """
    Save sweep data to a .npz file.

    Uses variable-length arrays stored as separate keys per tau-value.
    """
    save_dict = {
        'tau_values': data['tau_values'],
        'n_tau': np.array([len(data['tau_values'])]),
    }

    for i in range(len(data['tau_values'])):
        save_dict[f'eigenvalues_{i}'] = data['eigenvalues'][i]
        save_dict[f'sector_p_{i}'] = data['sector_p'][i]
        save_dict[f'sector_q_{i}'] = data['sector_q'][i]
        save_dict[f'multiplicities_{i}'] = data['multiplicities'][i]

    np.savez_compressed(output_path, **save_dict)
    print(f"Saved sweep data to {output_path}")


def load_sweep_data(input_path):
    """
    Load sweep data from a .npz file.

    Returns:
        data: dict with same structure as generate_sweep_data output
    """
    npz = np.load(input_path, allow_pickle=False)
    tau_values = npz['tau_values']
    n_tau = int(npz['n_tau'][0])

    data = {
        'tau_values': tau_values,
        'eigenvalues': [],
        'sector_p': [],
        'sector_q': [],
        'multiplicities': [],
    }

    for i in range(n_tau):
        data['eigenvalues'].append(npz[f'eigenvalues_{i}'])
        data['sector_p'].append(npz[f'sector_p_{i}'])
        data['sector_q'].append(npz[f'sector_q_{i}'])
        data['multiplicities'].append(npz[f'multiplicities_{i}'])

    return data


def print_sweep_summary(data):
    """Print summary statistics of the sweep data."""
    tau_values = data['tau_values']
    print(f"\nSweep data summary:")
    print(f"  tau range: [{tau_values[0]:.2f}, {tau_values[-1]:.2f}], "
          f"{len(tau_values)} points")

    for i, tau in enumerate(tau_values):
        evals = data['eigenvalues'][i]
        mults = data['multiplicities'][i]
        p_labels = data['sector_p'][i]
        q_labels = data['sector_q'][i]

        n_evals = len(evals)
        total_mult = np.sum(mults)
        n_sectors = len(set(zip(p_labels.tolist(), q_labels.tolist())))
        min_ev = np.min(evals) if n_evals > 0 else 0
        max_ev = np.max(evals) if n_evals > 0 else 0
        min_nonzero = np.min(evals[evals > 1e-10]) if np.any(evals > 1e-10) else 0

        print(f"  tau={tau:.2f}: {n_evals} evals, {n_sectors} sectors, "
              f"mult_sum={total_mult}, |lambda| in [{min_ev:.4f}, {max_ev:.4f}], "
              f"min_nonzero={min_nonzero:.4f}")


if __name__ == '__main__':
    # Configuration
    TAU_VALUES = np.arange(0.0, 2.01, 0.1)  # 21 values: 0.0, 0.1, ..., 2.0
    MAX_PQ_SUM = 6
    OUTPUT_PATH = os.path.join(SCRIPT_DIR, 's19a_sweep_data.npz')

    print("Session 19a: Eigenvalue Sweep Data Generation")
    print(f"  tau values: {len(TAU_VALUES)} points, [{TAU_VALUES[0]:.1f}, {TAU_VALUES[-1]:.1f}]")
    print(f"  max_pq_sum: {MAX_PQ_SUM} (28 irreps)")
    print(f"  Output: {OUTPUT_PATH}")

    # Generate the data
    data = generate_sweep_data(TAU_VALUES, max_pq_sum=MAX_PQ_SUM, verbose=True)

    # Save to disk
    save_sweep_data(data, OUTPUT_PATH)

    # Print summary
    print_sweep_summary(data)

    print("\nDone. Data ready for S-1 through S-4 diagnostics.")
