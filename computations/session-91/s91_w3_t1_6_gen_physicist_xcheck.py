"""Gen-physicist numerical-integration cross-check for T1.6 S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED.

Read-only on mack's NPZ + producing-script kernels. Independent re-evaluation of:
1. Kernel normalization at m/T=0 (Fermi-Dirac → 7/8; Bose-Einstein → 1)
2. Threshold-band spot (m_W/T=0.804 at T=100 GeV)
3. Deep-Boltzmann tail (m_top/T=1.7269 at T=100 GeV)
4. Heavy-tail at QCD-crossover anchor (m_top/T=172.69 at T=1 GeV)
5. Sub-MeV anchor (m_e/T=0.511 at T=1 MeV)
6. Aggregate scipy abserr scan over mack's kolb_turner_kernel_evaluations object array

Does NOT emit verdict line. Per plan §W3-1 §4: gen-physicist authors cross-check
sub-section in working paper; verdict-emission remains mack's role.
"""

import math
import os
import warnings

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np
import scipy.integrate

# Canonical-constants import (per .claude/rules/math-scripts.md; we re-use no
# framework constants directly — the SM masses are pinned in mack's producing
# script via SM_SPECIES, not as canonical constants — but the import contract
# is mandatory).
import sys
sys.path.insert(0, "computations/_shared")
from canonical_constants import g_star_SM, g_star_BBN  # noqa: F401 (referenced in comments)

# Configure scipy to RAISE on IntegrationWarning so we can detect non-convergence
warnings.filterwarnings("error", category=scipy.integrate.IntegrationWarning)


PREF = 15.0 / math.pi**4  # (local; canonical Kolb-Turner prefactor)
QUAD_LIMIT = 200  # (local; plan §7 row 1 pin)
QUAD_EPSABS = 1e-10  # (local; plan §7 row 1 pin)
QUAD_EPSREL = 1e-8  # (local; plan §7 row 1 pin)


def integrand_fermion(u: float, x: float) -> float:
    e = math.sqrt(u * u + x * x)
    if e > 700.0:
        return 0.0
    return (u * u) * e / (math.exp(e) + 1.0)


def integrand_boson(u: float, x: float) -> float:
    e = math.sqrt(u * u + x * x)
    if e > 700.0:
        return 0.0
    d = math.exp(e) - 1.0
    if d <= 0.0:
        return (u * u) * e / max(e + 0.5 * e * e, 1e-300)
    return (u * u) * e / d


def k_fermion(x: float) -> tuple[float, float]:
    val, err = scipy.integrate.quad(
        integrand_fermion, 0.0, np.inf, args=(x,),
        limit=QUAD_LIMIT, epsabs=QUAD_EPSABS, epsrel=QUAD_EPSREL,
    )
    return PREF * val, PREF * err


def k_boson(x: float) -> tuple[float, float]:
    val, err = scipy.integrate.quad(
        integrand_boson, 0.0, np.inf, args=(x,),
        limit=QUAD_LIMIT, epsabs=QUAD_EPSABS, epsrel=QUAD_EPSREL,
    )
    return PREF * val, PREF * err


def main() -> None:
    npz_path = "computations/session-91/s91_w3_cf40_kolb_turner_fd_be_integrated.npz"
    data = np.load(npz_path, allow_pickle=True)

    print("=== NPZ machinery-pin keys ===")
    for k in ("quad_limit", "quad_epsabs", "quad_epsrel"):
        if k in data.keys():
            print(f"  {k} = {data[k]}")

    spot_checks = []  # (anchor, species, x, k_KT, k_KT_expected, scipy_abserr, warning_seen)

    # --- Spot check 1: kernel normalization at m/T = 0 (fermion) ---
    try:
        k_f0, err_f0 = k_fermion(0.0)
        spot_checks.append(("m/T=0", "fermion-norm", 0.0, k_f0, 7.0 / 8.0, err_f0, False))
    except scipy.integrate.IntegrationWarning as w:
        spot_checks.append(("m/T=0", "fermion-norm", 0.0, None, 7.0 / 8.0, None, True))
        print(f"  WARN fermion m/T=0: {w}")

    # --- Spot check 1b: kernel normalization at m/T = 0 (boson) ---
    try:
        k_b0, err_b0 = k_boson(0.0)
        spot_checks.append(("m/T=0", "boson-norm", 0.0, k_b0, 1.0, err_b0, False))
    except scipy.integrate.IntegrationWarning as w:
        spot_checks.append(("m/T=0", "boson-norm", 0.0, None, 1.0, None, True))
        print(f"  WARN boson m/T=0: {w}")

    # --- Spot check 2: threshold-band m_W/T at T=100 GeV ---
    x = 80.379 / 100.0
    try:
        k_W, err_W = k_boson(x)
        spot_checks.append(("T=100 GeV", "W (boson)", x, k_W, 0.92, err_W, False))
    except scipy.integrate.IntegrationWarning as w:
        spot_checks.append(("T=100 GeV", "W (boson)", x, None, 0.92, None, True))
        print(f"  WARN W m_W/T=0.804: {w}")

    # --- Spot check 3: deep-Boltzmann m_top/T at T=100 GeV ---
    x = 172.69 / 100.0
    try:
        k_t, err_t = k_fermion(x)
        # plan Step 5 predicted ~0.13-0.16 — use midpoint 0.145
        spot_checks.append(("T=100 GeV", "top (fermion)", x, k_t, 0.145, err_t, False))
    except scipy.integrate.IntegrationWarning as w:
        spot_checks.append(("T=100 GeV", "top (fermion)", x, None, 0.145, None, True))
        print(f"  WARN top m/T=1.73: {w}")

    # --- Spot check 4: heavy-tail m_top/T at T=1 GeV (deeply non-relativistic) ---
    x = 172.69 / 1.0
    try:
        k_t1, err_t1 = k_fermion(x)
        spot_checks.append(("T=1 GeV", "top (fermion)", x, k_t1, 0.0, err_t1, False))
    except scipy.integrate.IntegrationWarning as w:
        spot_checks.append(("T=1 GeV", "top (fermion)", x, None, 0.0, None, True))
        print(f"  WARN top m_t/T=172.69: {w}")

    # --- Spot check 5: sub-MeV m_e/T at T=1 MeV ---
    x = 0.000511 / 0.001
    try:
        k_e, err_e = k_fermion(x)
        spot_checks.append(("T=1 MeV", "e (fermion)", x, k_e, None, err_e, False))
    except scipy.integrate.IntegrationWarning as w:
        spot_checks.append(("T=1 MeV", "e (fermion)", x, None, None, None, True))
        print(f"  WARN e m_e/T=0.511: {w}")

    print()
    print("=== Spot-check table (independent scipy re-evaluation) ===")
    print(f"{'anchor':<10} {'species':<18} {'m/T':>8} {'k_KT':>14} {'expected':>10} {'scipy abserr':>14} {'warning':>8}")
    for anchor, species, x, k, expected, err, warning_seen in spot_checks:
        k_str = f"{k:.10f}" if k is not None else "(IntegrationWarning)"
        err_str = f"{err:.3e}" if err is not None else "n/a"
        exp_str = f"{expected:.6f}" if expected is not None else "n/a"
        print(f"{anchor:<10} {species:<18} {x:>8.4f} {k_str:>14} {exp_str:>10} {err_str:>14} {str(warning_seen):>8}")

    # --- Aggregate scan over mack's kolb_turner_kernel_evaluations object ---
    print()
    print("=== Aggregate scipy convergence diagnostic from mack NPZ ===")
    ke = data["kolb_turner_kernel_evaluations"].item()
    max_err = 0.0  # (local)
    max_err_species = None
    max_err_anchor = None
    total_evals = 0  # (local)
    for anchor_label, species_list in ke.items():
        for entry in species_list:
            total_evals += 1
            e_val = float(entry.get("k_KT_abs_err", 0.0))
            if e_val > max_err:
                max_err = e_val
                max_err_species = entry.get("name", "?")
                max_err_anchor = anchor_label
    n_above_10x = sum(
        1 for sl in ke.values() for e in sl if float(e.get("k_KT_abs_err", 0.0)) > 10 * QUAD_EPSABS
    )
    n_above_100x = sum(
        1 for sl in ke.values() for e in sl if float(e.get("k_KT_abs_err", 0.0)) > 100 * QUAD_EPSABS
    )
    print(f"  Total kernel evaluations: {total_evals}")
    print(f"  Max scipy abserr reported: {max_err:.3e}  (species={max_err_species}, anchor={max_err_anchor})")
    print(f"  epsabs pin = {QUAD_EPSABS:.0e}; max_err / epsabs = {max_err / QUAD_EPSABS:.2f}x")
    print(f"  Pre-PREFACTOR (15/pi^4 = {PREF:.4f}): true integrand-side abserr ceiling = {QUAD_EPSABS * PREF:.3e}")
    print(f"  Evaluations exceeding 10x epsabs (1e-9): {n_above_10x}")
    print(f"  Evaluations exceeding 100x epsabs (1e-8): {n_above_100x}")
    print(f"  Domain handling: [0, +inf) with scipy automatic substitution (plan §7 row 2); no upper-bound divergence at heaviest species top@T=1 GeV (top kernel value ~ {spot_checks[4][3]:.3e})")


if __name__ == "__main__":
    main()
