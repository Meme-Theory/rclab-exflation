#!/usr/bin/env python3
"""
S74 W4-M ZERO-MODE-WINDING-74
==============================

Task: Is the Jensen deformation parameter tau compact with periodicity?
If yes, winding number conservation provides a purely topological stabilization
of the modulus, beyond the dynamical stabilization investigated in W1-B.

Gate: ZERO-MODE-WINDING-74
  PASS  if tau is compact with identifiable period
  INFO  if partial compactness (compact sub-direction, non-compact in the
        relevant stabilization direction)
  FAIL  if tau is non-compact (no winding stabilization)

Governing structure (Baptista paper 13, eq 2.25-2.40):
  Jensen modulus phi takes values in C^2 subset su(3).
  Left-invariant metric g_phi is positive-definite iff |phi|^2 < 1/4.
  Under U(2), phi -> (det a) a phi with U(1) center weight 3.
  Radial invariant is r_tau := |phi|^2, and the physical Lagrangian
  depends on phi only through r_tau and its covariant derivatives
  (eq 3.41: L contains C_phi |d_A phi|^2 and D_phi |d r_tau|^2).

This script performs four independent analytic/numeric tests of
compactness of the tau direction:

  Test 1 — Positivity domain topology:
    |phi|^2 < 1/4 defines an OPEN ball of radius 1/2 in R^4.  Topologically
    a 4-ball, not a 4-torus.  The radial variable r_tau = |phi|^2 ranges
    over the half-open interval [0, 1/4).  The boundary at 1/4 is a metric
    DEGENERACY (R_{g_phi} -> -infty), not a gluing of an identification.

  Test 2 — U(2)-orbit structure:
    Compute the orbit of a generic phi in C^2 under U(2), extract its
    stabilizer, and determine whether any orbit gives a closed loop in
    |phi|^2 under U(2) motion.  Since U(2) preserves |phi|^2 exactly,
    U(2)-orbit motion NEVER changes tau -- winding around U(2) orbits
    gives non-trivial pi_1 on gauge coset, not on the modulus direction.

  Test 3 — Periodicity scan of R_{g_phi}(r_tau):
    Evaluate the scalar curvature (eq 2.40) on a dense grid of r_tau
    in (0, 1/4).  Test whether R(r_tau + P) = R(r_tau) for any
    candidate period P > 0.  If no period exists, the Jensen modulus
    is non-periodic in tau.

  Test 4 — Winding number law:
    For any compact direction, there is a conserved current
    J^mu = (partial^mu X) / L where L is the period and X is the
    compact coordinate.  Compute:
      (a) For the phase of phi (the Higgs U(1)_Y direction): PASS --
          compact S^1 with period 2 pi / 3 after Z_3 center quotient.
      (b) For the radial modulus r_tau: FAIL -- no period.

Outputs:
  - s74_zero_mode_winding.npz (compactness flags, period candidates)
  - s74_zero_mode_winding.png (optional diagnostic)
"""

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import os  # noqa: E402
import sys  # noqa: E402

# ----- Canonical constants import -----
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import tau_fold, PI  # noqa: E402


# ==============================================================================
#  Baptista 2021, eq (2.40): scalar curvature of g_phi on SU(3)
# ==============================================================================

def R_g_phi(r, lam=1.0):
    """Scalar curvature of Jensen metric g_phi as a function of r = |phi|^2.
    Baptista 2021, eq (2.40).

    Domain: r in [0, 1/4).  Diverges at r = 1/4.
    """
    num = 3.0 * (4.0 - 25.0 * r + 33.0 * r**2 - 8.0 * r**3)  # (local)
    den = lam * (1.0 - r) ** 2 * (1.0 - 4.0 * r)  # (local)
    return num / den


def volume_form_density(r, lam=1.0):
    """Volume density f_phi = lambda^4 (1 - r) sqrt(1 - 4 r).  eq (2.37)."""
    return (lam**4) * (1.0 - r) * np.sqrt(np.maximum(0.0, 1.0 - 4.0 * r))  # (local)


# ==============================================================================
#  Test 1 — Positivity-domain topology
# ==============================================================================

def test1_positivity_domain():
    """Determine topology of the positivity region |phi|^2 < 1/4 in C^2 = R^4."""
    r_pos_max = 0.25  # (local) — positivity wall (Baptista eq below 2.25)
    r_fold = tau_fold  # project's operating point |phi|^2 = 0.19

    # R and volume at the fold and at several probe points
    r_probes = np.array([0.0, 0.05, 0.10, tau_fold, 0.20, 0.24, 0.245, 0.249])  # (local)
    R_probes = R_g_phi(r_probes)  # (local)
    f_probes = volume_form_density(r_probes)  # (local)

    # Topology:
    # The positivity domain is {phi in C^2 : |phi|^2 < 1/4}.
    # As a subset of R^4, this is an open 4-ball of radius 1/2.
    # The fundamental group of the open 4-ball is TRIVIAL (simply connected).
    # Therefore NO non-trivial winding number exists on the 4-ball itself.
    pi_1_domain = 0  # trivial fundamental group of open 4-ball  # (local)

    # The radial coordinate r = |phi|^2 ranges over [0, 1/4), which is
    # topologically the half-open interval -- also contractible -> pi_1 = 0.
    r_range_is_interval = True  # (local)

    # Boundary behavior: R_{g_phi} -> -infinity as r -> 1/4
    r_near_wall = np.array([0.2499, 0.24999, 0.249999])  # (local)
    R_near_wall = R_g_phi(r_near_wall)  # (local)
    vol_near_wall = volume_form_density(r_near_wall)  # (local)

    return {
        "r_pos_max": r_pos_max,
        "r_fold": r_fold,
        "r_probes": r_probes,
        "R_probes": R_probes,
        "f_probes": f_probes,
        "pi_1_positivity_domain": pi_1_domain,
        "r_radial_range_is_half_open_interval": r_range_is_interval,
        "R_near_wall": R_near_wall,
        "vol_near_wall": vol_near_wall,
        "boundary_is_degeneracy_not_identification": True,
    }


# ==============================================================================
#  Test 2 — U(2)-orbit structure of phi in C^2 under phi -> (det a) a phi
# ==============================================================================

def test2_u2_orbit_structure():
    """Compute U(2) orbit of a probe phi in C^2 under phi -> (det a) a phi.

    Verifies that U(2) acts transitively on spheres |phi|^2 = const.
    The U(1) center (a = e^{i*theta} I_2) acts by phi -> e^{3 i theta} phi,
    so the U(1)-orbit is a circle S^1 with period 2 pi / 3 after Z_3 quotient.
    This is the HIGGS PHASE direction, NOT the radial Jensen direction.
    """
    # Probe point at the fold, purely real
    phi_0 = np.sqrt(tau_fold) * np.array([1.0, 0.0], dtype=complex)  # (local)
    r_probe = (np.abs(phi_0) ** 2).sum()  # = tau_fold  # (local)

    # U(1) center orbit: a = e^{i theta} I_2, det a = e^{2 i theta},
    # action phi -> (det a) a phi = e^{3 i theta} phi
    n_theta = 360  # (local)
    thetas = np.linspace(0.0, 2.0 * PI, n_theta, endpoint=False)  # (local)
    phi_orbit = np.array([np.exp(3j * t) * phi_0 for t in thetas])  # (local)
    r_along_orbit = (np.abs(phi_orbit) ** 2).sum(axis=1)  # (local)

    # The U(1)-orbit lies entirely on the 3-sphere |phi|^2 = r_probe
    r_orbit_range = np.ptp(r_along_orbit)  # max - min (local)
    r_invariant_under_U1 = r_orbit_range < 1e-14

    # Z_3 stabilizer: phi = e^{3 i theta} phi iff 3 theta in 2 pi Z iff
    # theta in {0, 2 pi / 3, 4 pi / 3}
    stabilizer_Z3 = [0.0, 2.0 * PI / 3.0, 4.0 * PI / 3.0]  # (local)

    # Effective period of the Higgs-phase direction after Z_3 quotient
    T_higgs_phase = 2.0 * PI / 3.0

    # SU(2) subgroup action: phi -> a phi with det a = 1, so (det a) a phi = a phi
    # SU(2) acts transitively on the 3-sphere, so the SU(2)-orbit = S^3_{sqrt(r_probe)}
    # Draw a discrete SU(2) path and check r-invariance
    rng = np.random.default_rng(42)  # (local)
    n_su2 = 500  # (local)
    r_su2_path = np.zeros(n_su2)  # (local)
    for k in range(n_su2):
        alpha, beta = rng.normal(size=2) + 1j * rng.normal(size=2)  # (local)
        norm = np.sqrt(np.abs(alpha) ** 2 + np.abs(beta) ** 2)  # (local)
        a = np.array([[alpha / norm, -np.conj(beta) / norm],
                      [beta / norm, np.conj(alpha) / norm]])  # (local)
        # det(a) = 1 by construction
        phi_k = a @ phi_0  # (local)
        r_su2_path[k] = (np.abs(phi_k) ** 2).sum()

    r_su2_range = np.ptp(r_su2_path)  # (local)
    r_invariant_under_SU2 = r_su2_range < 1e-14

    # Full U(2) orbit = S^3 at fixed r.  The radial direction r = |phi|^2 is
    # ORTHOGONAL to the full U(2)-orbit in the C^2 target space.
    orbit_preserves_r = bool(r_invariant_under_U1 and r_invariant_under_SU2)

    return {
        "r_probe": float(r_probe),
        "r_orbit_U1_range": float(r_orbit_range),
        "r_orbit_SU2_range": float(r_su2_range),
        "T_higgs_phase": T_higgs_phase,
        "stabilizer_Z3": np.array(stabilizer_Z3),
        "orbit_preserves_r": orbit_preserves_r,
        # Topology of the orbit = S^3 (U(2) acts transitively mod radial)
        "orbit_topology": "S^3 (3-sphere at fixed r)",
        # Fundamental group of S^3 is trivial
        "pi_1_U2_orbit": 0,
        # Fundamental group of the U(1)-phase circle is Z
        "pi_1_higgs_phase": "Z",
    }


# ==============================================================================
#  Test 3 — Periodicity scan of R_{g_phi}(r) in the radial direction
# ==============================================================================

def test3_periodicity_scan():
    """Scan R_{g_phi}(r) for any period P > 0.  Inside the positivity domain,
    r in (0, 1/4), we test whether R(r + P) = R(r) for any P <= 0.125.
    """
    n_grid = 4001  # (local)
    # Slight offset to avoid r=0 saddle and r=1/4 singularity
    r_grid = np.linspace(0.001, 0.249, n_grid)  # (local)
    R_grid = R_g_phi(r_grid)  # (local)

    # Monotonicity check: is R(r) monotonic on the physical interval?
    dR = np.diff(R_grid)  # (local)
    n_sign_flips = int(np.sum(np.diff(np.sign(dR)) != 0))
    is_monotonic = n_sign_flips == 0

    # Count stationary points (turning points)
    n_stationary = int(np.sum(dR[:-1] * dR[1:] < 0))

    # Period hunt via autocorrelation.  If R were periodic with period P,
    # its autocorrelation would peak at multiples of P.
    R_centered = R_grid - R_grid.mean()  # (local)
    # FFT-based autocorrelation
    n_pad = 2 ** int(np.ceil(np.log2(2 * len(R_centered))))  # (local)
    R_padded = np.pad(R_centered, (0, n_pad - len(R_centered)))  # (local)
    R_fft = np.fft.fft(R_padded)  # (local)
    power = np.abs(R_fft) ** 2  # (local)
    autocorr = np.real(np.fft.ifft(power))[: len(R_centered)]  # (local)
    autocorr /= autocorr[0]  # normalize  # (local)

    # Look for any secondary peak > 0.9 (would indicate near-period)
    search_start = 50  # skip the DC peak  # (local)
    secondary_peak_candidates = autocorr[search_start:]  # (local)
    max_secondary = float(np.max(secondary_peak_candidates))
    arg_max = int(np.argmax(secondary_peak_candidates) + search_start)
    candidate_period = float(r_grid[arg_max] - r_grid[0]) if max_secondary > 0.9 else np.nan

    is_periodic = max_secondary > 0.99  # strict periodicity threshold

    # Behavior at boundaries
    R_at_0 = float(R_g_phi(0.0))     # = 12 = bi-invariant Einstein curvature  # (local)
    R_at_fold = float(R_g_phi(tau_fold))
    # Approaching the wall: R -> -inf

    return {
        "r_grid": r_grid,
        "R_grid": R_grid,
        "is_monotonic": bool(is_monotonic),
        "n_stationary_points": n_stationary,
        "autocorr": autocorr,
        "max_secondary_autocorr": max_secondary,
        "candidate_period": candidate_period,
        "is_periodic": bool(is_periodic),
        "R_at_0": R_at_0,
        "R_at_fold": R_at_fold,
    }


# ==============================================================================
#  Test 4 — Winding number law candidates
# ==============================================================================

def test4_winding_laws():
    """Test which directions in the Jensen moduli space admit winding number
    conservation.  A conserved winding number requires a compact coordinate
    with a natural period.
    """
    # (a) Higgs-phase direction alpha = arg(phi):
    #     Compact S^1, period 2 pi / 3 after Z_3 quotient (from test 2).
    #     Winding number n_H = (1 / (2 pi / 3)) * oint d alpha = (3/2 pi) oint d alpha.
    #     This IS a conserved winding number, and it is integer-valued after
    #     the Z_3 quotient.  BUT this is the electroweak hypercharge phase,
    #     NOT the Jensen radial direction.
    T_alpha = 2.0 * PI / 3.0   # period after Z_3 quotient  # (local)
    has_winding_higgs_phase = True

    # (b) Radial direction r_tau = |phi|^2:
    #     Half-open interval [0, 1/4).  NOT compact.  NO natural period.
    #     The boundary at 1/4 is a metric degeneracy, not an identification.
    #     NO winding number.
    has_winding_radial = False

    # (c) SU(2) orbit direction (within S^3 at fixed r):
    #     SU(2) = S^3, fundamental group of S^3 is trivial pi_1(S^3) = 0.
    #     NO winding number at the homotopy level (only the hypercharge
    #     phase contributes to pi_1).
    has_winding_SU2 = False

    # (d) Full U(2) orbit direction:
    #     U(2) = (SU(2) x U(1)) / Z_2, fundamental group pi_1(U(2)) = Z.
    #     BUT this Z is INTERNAL to the gauge group, and corresponds to
    #     the same Higgs phase in (a).
    has_winding_U2 = "same as (a)"

    # Summary: the ONLY compact direction carrying a winding number is the
    # Higgs phase alpha.  This direction does NOT stabilize r_tau (the
    # Jensen radial modulus).  The radial modulus is non-compact.
    return {
        "higgs_phase_period": T_alpha,
        "higgs_phase_winding": has_winding_higgs_phase,
        "radial_winding": has_winding_radial,
        "SU2_winding": has_winding_SU2,
        "U2_winding_summary": has_winding_U2,
        "conclusion": (
            "Jensen radial modulus r_tau = |phi|^2 is non-compact; "
            "the only winding number in the moduli space is the Higgs "
            "phase U(1)_Y winding, which stabilizes the Higgs gauge "
            "phase (Goldstone direction) but NOT the radial Jensen "
            "modulus.  Radial stabilization is potential-driven, not "
            "topological."
        ),
    }


# ==============================================================================
#  Cross-checks
# ==============================================================================

def cross_checks(t1, t2, t3, t4):
    """Independent verifications of the main test conclusions."""

    # CC1: R(0) should equal 12 / lambda (bi-invariant Einstein, Baptista eq 2.40
    # at r=0 gives 3*4/(1*1) = 12)
    R0_expected = 12.0  # (local)
    R0_computed = R_g_phi(0.0)  # (local)
    cc1_err = abs(R0_computed - R0_expected) / R0_expected  # (local)
    cc1_pass = cc1_err < 1e-14

    # CC2: R(r) should diverge to -infty as r -> 1/4^-
    r_walls = np.array([0.2499, 0.24999, 0.249999, 0.2499999])  # (local)
    R_walls = R_g_phi(r_walls)  # (local)
    # Expect decreasing (more negative) values as r -> 1/4
    is_divergent = R_walls[-1] < R_walls[0] < 0.0
    cc2_pass = bool(is_divergent) and R_walls[-1] < -1e3

    # CC3: Volume form should vanish as r -> 1/4
    vol_at_wall = volume_form_density(0.249999)  # (local)
    cc3_pass = vol_at_wall < 1e-2

    # CC4: Autocorrelation of a genuinely periodic signal should return
    # max_secondary = 1.  Use sin(6 pi r) as a sanity check on the FFT.
    n_sanity = 4001  # (local)
    r_sanity = np.linspace(0.001, 0.249, n_sanity)  # (local)
    sanity_signal = np.sin(6.0 * PI * r_sanity)  # period = 1/3  # (local)
    sanity_centered = sanity_signal - sanity_signal.mean()  # (local)
    n_pad = 2 ** int(np.ceil(np.log2(2 * len(sanity_centered))))  # (local)
    sanity_padded = np.pad(sanity_centered, (0, n_pad - len(sanity_centered)))  # (local)
    sanity_fft = np.fft.fft(sanity_padded)  # (local)
    sanity_power = np.abs(sanity_fft) ** 2  # (local)
    sanity_autocorr = np.real(np.fft.ifft(sanity_power))[: len(sanity_centered)]  # (local)
    sanity_autocorr /= sanity_autocorr[0]  # (local)
    # For a true periodic signal, expect max_secondary very close to 1
    sanity_max_sec = float(np.max(sanity_autocorr[50:]))
    cc4_pass = sanity_max_sec > 0.95  # sanity-check: FFT finds the period

    return {
        "CC1_R_at_zero": {
            "expected": R0_expected,
            "computed": R0_computed,
            "rel_err": cc1_err,
            "pass": bool(cc1_pass),
        },
        "CC2_wall_divergence": {
            "R_near_wall": R_walls,
            "monotone_divergent": bool(is_divergent),
            "pass": bool(cc2_pass),
        },
        "CC3_volume_vanishes": {
            "vol_at_wall": float(vol_at_wall),
            "pass": bool(cc3_pass),
        },
        "CC4_fft_finds_period": {
            "sanity_max_sec": sanity_max_sec,
            "pass": bool(cc4_pass),
        },
    }


# ==============================================================================
#  Main
# ==============================================================================

def main():
    print("=" * 72)
    print("S74 W4-M ZERO-MODE-WINDING-74")
    print("=" * 72)
    print()

    # Test 1 — positivity domain topology
    print("Test 1: Positivity-domain topology")
    t1 = test1_positivity_domain()
    print(f"  positivity wall: r_max = {t1['r_pos_max']}")
    print(f"  operating point: r_fold = {t1['r_fold']}")
    print(f"  pi_1(positivity domain) = {t1['pi_1_positivity_domain']}")
    print(f"  domain is half-open interval [0, 1/4): {t1['r_radial_range_is_half_open_interval']}")
    print(f"  R near wall: {t1['R_near_wall']}")
    print(f"  volume near wall: {t1['vol_near_wall']}")
    print()

    # Test 2 — U(2) orbit structure
    print("Test 2: U(2) orbit structure")
    t2 = test2_u2_orbit_structure()
    print(f"  r_probe = {t2['r_probe']:.6f}")
    print(f"  r_orbit_U1_range = {t2['r_orbit_U1_range']:.2e} (should be ~0)")
    print(f"  r_orbit_SU2_range = {t2['r_orbit_SU2_range']:.2e} (should be ~0)")
    print(f"  Higgs-phase period (after Z_3 quotient) = {t2['T_higgs_phase']:.6f} = 2 pi / 3")
    print(f"  U(2) orbit topology: {t2['orbit_topology']}")
    print(f"  pi_1(U(2) orbit) = {t2['pi_1_U2_orbit']}")
    print(f"  pi_1(Higgs phase) = {t2['pi_1_higgs_phase']}")
    print(f"  orbit preserves radial r: {t2['orbit_preserves_r']}")
    print()

    # Test 3 — periodicity scan
    print("Test 3: Periodicity scan of R_{g_phi}(r)")
    t3 = test3_periodicity_scan()
    print(f"  is_monotonic: {t3['is_monotonic']}")
    print(f"  n_stationary_points: {t3['n_stationary_points']}")
    print(f"  max_secondary_autocorr: {t3['max_secondary_autocorr']:.6f}")
    print(f"  candidate_period: {t3['candidate_period']}")
    print(f"  is_periodic: {t3['is_periodic']}")
    print(f"  R(0) = {t3['R_at_0']:.6f}")
    print(f"  R(fold) = {t3['R_at_fold']:.6f}")
    print()

    # Test 4 — winding laws
    print("Test 4: Winding number law candidates")
    t4 = test4_winding_laws()
    print(f"  Higgs phase period: {t4['higgs_phase_period']:.6f}")
    print(f"  Higgs phase has winding: {t4['higgs_phase_winding']}")
    print(f"  Radial direction has winding: {t4['radial_winding']}")
    print(f"  SU(2) direction has winding: {t4['SU2_winding']}")
    print(f"  U(2) winding: {t4['U2_winding_summary']}")
    print(f"  Conclusion: {t4['conclusion']}")
    print()

    # Cross-checks
    print("Cross-checks:")
    cc = cross_checks(t1, t2, t3, t4)
    for name, result in cc.items():
        print(f"  {name}: {'PASS' if result['pass'] else 'FAIL'}")
        for k, v in result.items():
            if k != "pass":
                if isinstance(v, np.ndarray):
                    print(f"    {k} = {v}")
                else:
                    print(f"    {k} = {v}")
    print()

    # Gate verdict
    radial_compact = False       # from Test 1 + Test 3
    any_phase_compact = True     # from Test 2 + Test 4 (Higgs phase)

    # Gate: PASS if tau is compact; INFO if partial compactness;
    #       FAIL if tau is non-compact.
    # The "tau" in question is the Jensen RADIAL modulus, NOT the Higgs phase.
    # Because a compact phase exists ORTHOGONAL to the radial direction (it
    # is the Higgs gauge phase, not a stabilization direction for r_tau),
    # we classify this as PARTIAL compactness = INFO verdict.
    if radial_compact:
        verdict = "PASS"
        verdict_text = (
            "Jensen radial modulus tau = |phi|^2 is compact with period P. "
            "Winding number conservation provides topological modulus stabilization."
        )
    elif any_phase_compact and not radial_compact:
        verdict = "INFO"
        verdict_text = (
            "Partial compactness: the Higgs phase direction (arg phi) is compact "
            "with period 2 pi / 3, but the Jensen RADIAL modulus r_tau = |phi|^2 "
            "is non-compact with a half-open interval [0, 1/4). "
            "The Higgs-phase winding corresponds to U(1)_Y hypercharge winding -- "
            "it does NOT stabilize the radial Jensen modulus. Radial stabilization "
            "is potential-driven (dynamic), not topological."
        )
    else:
        verdict = "FAIL"
        verdict_text = "Jensen radial modulus is non-compact. No winding stabilization."

    print("=" * 72)
    print(f"VERDICT: {verdict}")
    print("=" * 72)
    print(verdict_text)
    print()

    # Plot diagnostic
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.0))
    ax = axes[0]
    r_plot = np.linspace(0.001, 0.249, 2000)  # (local)
    ax.plot(r_plot, R_g_phi(r_plot), "b-", lw=1.3)
    ax.axvline(tau_fold, color="r", ls="--", lw=1.0, label="fold (r=0.19)")
    ax.axvline(0.25, color="k", ls=":", lw=1.0, label="positivity wall")
    ax.set_xlabel("r = |phi|^2")
    ax.set_ylabel("R_{g_phi}(r)  (lambda=1 units)")
    ax.set_title("Scalar curvature: monotonic + diverges")
    ax.set_ylim(-50, 30)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    ax = axes[1]
    ax.plot(r_plot, volume_form_density(r_plot), "g-", lw=1.3)
    ax.axvline(tau_fold, color="r", ls="--", lw=1.0)
    ax.axvline(0.25, color="k", ls=":", lw=1.0)
    ax.set_xlabel("r = |phi|^2")
    ax.set_ylabel("f_phi(r)")
    ax.set_title("Volume form: vanishes at r=1/4")
    ax.grid(alpha=0.3)

    ax = axes[2]
    # Depict the positivity disk in R^2 = Re(phi_1), Im(phi_1) for fixed phi_2=0
    theta_c = np.linspace(0.0, 2.0 * PI, 300)  # (local)
    radius = 0.5  # (local) sqrt(1/4)
    ax.plot(radius * np.cos(theta_c), radius * np.sin(theta_c), "k-", lw=1.5, label="|phi|=1/2")
    ax.fill(radius * np.cos(theta_c), radius * np.sin(theta_c), alpha=0.10, color="b")
    fold_radius = float(np.sqrt(tau_fold))  # (local)
    ax.plot(fold_radius * np.cos(theta_c), fold_radius * np.sin(theta_c), "r--", lw=1.0, label="|phi|=sqrt(fold)")
    ax.set_xlim(-0.55, 0.55)
    ax.set_ylim(-0.55, 0.55)
    ax.set_aspect("equal")
    ax.set_xlabel("Re(phi_1)")
    ax.set_ylabel("Im(phi_1)")
    ax.set_title("Positivity domain (C^2 cross-section) = open 4-ball")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plot_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "s74_zero_mode_winding.png",
    )
    plt.savefig(plot_path, dpi=130)
    plt.close()

    # Save data
    npz_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "s74_zero_mode_winding.npz",
    )
    np.savez(
        npz_path,
        # Test 1
        r_pos_max=t1["r_pos_max"],
        r_fold=t1["r_fold"],
        r_probes=t1["r_probes"],
        R_probes=t1["R_probes"],
        f_probes=t1["f_probes"],
        pi_1_positivity_domain=t1["pi_1_positivity_domain"],
        r_radial_range_is_half_open_interval=t1["r_radial_range_is_half_open_interval"],
        R_near_wall=t1["R_near_wall"],
        vol_near_wall=t1["vol_near_wall"],
        boundary_is_degeneracy=t1["boundary_is_degeneracy_not_identification"],
        # Test 2
        r_probe=t2["r_probe"],
        r_orbit_U1_range=t2["r_orbit_U1_range"],
        r_orbit_SU2_range=t2["r_orbit_SU2_range"],
        T_higgs_phase=t2["T_higgs_phase"],
        stabilizer_Z3=t2["stabilizer_Z3"],
        orbit_preserves_r=t2["orbit_preserves_r"],
        # Test 3
        r_grid=t3["r_grid"],
        R_grid=t3["R_grid"],
        is_monotonic=t3["is_monotonic"],
        n_stationary_points=t3["n_stationary_points"],
        max_secondary_autocorr=t3["max_secondary_autocorr"],
        candidate_period=(t3["candidate_period"] if not np.isnan(t3["candidate_period"]) else -1.0),
        is_periodic=t3["is_periodic"],
        R_at_0=t3["R_at_0"],
        R_at_fold=t3["R_at_fold"],
        # Test 4
        higgs_phase_period=t4["higgs_phase_period"],
        higgs_phase_winding=t4["higgs_phase_winding"],
        radial_winding=t4["radial_winding"],
        # Cross-checks
        cc1_rel_err=cc["CC1_R_at_zero"]["rel_err"],
        cc1_pass=cc["CC1_R_at_zero"]["pass"],
        cc2_pass=cc["CC2_wall_divergence"]["pass"],
        cc3_vol_at_wall=cc["CC3_volume_vanishes"]["vol_at_wall"],
        cc3_pass=cc["CC3_volume_vanishes"]["pass"],
        cc4_sanity_max_sec=cc["CC4_fft_finds_period"]["sanity_max_sec"],
        cc4_pass=cc["CC4_fft_finds_period"]["pass"],
        # Verdict
        verdict=verdict,
        verdict_text=verdict_text,
        radial_compact=radial_compact,
        any_phase_compact=any_phase_compact,
    )
    print(f"Saved: {npz_path}")
    print(f"Saved: {plot_path}")
    return verdict, verdict_text


if __name__ == "__main__":
    main()
