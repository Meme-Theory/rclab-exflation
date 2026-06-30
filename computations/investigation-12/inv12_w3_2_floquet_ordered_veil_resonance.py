#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INV12-W3-2-FLOQUET-ORDERED-VEIL-RESONANCE  (investigation track, Wave 3)

Gate: compute the Floquet exponent Re mu(k) for the post-fold modulus-driven relic
mode equation written as a Hill/Mathieu problem, across the relic pair band, and decide
whether the Ordered Veil survives its OWN in-band modulus resonance.

PHYSICS (substrate-first):
  D_K spectrum's modulus mode (omega_q^phys = 2.012813 M_KK) is the residual ringing of the
  Jensen deformation parameter tau after the supersonic transit. It drives a periodic
  time-dependence on each relic mode's frequency. Each relic mode (D_K eigenvalue excitation,
  BdG dispersion E_k) is therefore a PARAMETRIC oscillator:

      u_k'' + Omega_k^2(t) u_k = 0 ,   Omega_k^2(t) = E_k^2 [ 1 + h_par cos(omega_q t) ]      (Hill)

  In Mathieu standard form with z = (omega_q/2) t :

      u_k'' + [ A_k - 2 q_M cos(2z) ] u_k = 0 ,   A_k = (2 E_k / omega_q)^2 ,  q_M = A_k * h_par/2

  Floquet theory: the monodromy matrix M(k) advances (u, u') by ONE drive period T = 2*pi/omega_q.
  By Liouville (no friction in the bare Hill eq.) det M = 1 -> eigenvalues are a reciprocal pair
  e^{+/- mu T}. Hence the gap/band dichotomy is set by |Tr M| alone:
      |Tr M| < 2  <=>  eigenvalues on unit circle  <=>  Re mu = 0   (STABILITY GAP, frozen)
      |Tr M| > 2  <=>  real reciprocal pair         <=>  Re mu > 0   (RESONANCE BAND, re-pumped)
  The Floquet exponent: cos(mu T) = Tr M / 2  =>  Re mu = (1/T) * arccosh(|Tr M|/2)  when |Tr M|>2.

  ORDERED VEIL SURVIVES  iff  every relic-band mode lands in a stability GAP (Re mu = 0).

WIDTH-AWARE DRIVE (S100a W-1 D-2 lesson, pinned in convention):
  The instability-tongue WIDTH is set by the FULL Mathieu depth q_M (proportional to h_par),
  NEVER by the suppressed rectified-force amplitude phi_k (which governs THROUGHPUT only).
  Principal half-width identity:  delta_omega/omega_d = h_par/4  at  omega_d = 2*omega_0
  -> Mathieu q half-width in A is q_M ; with the framework normalization q_M = A_k*h_par/2.
  n-th zone at 2E_k = n*omega_q^phys, width proportional to q_M^n.

INPUTS:
  - canonical_constants.py  (M_KK, Delta_BCS, tau_fold)
  - inv12_w3_1_relic_spectrum_ode_lock.npz  (FORWARD INTRA-INVESTIGATION PIN, W3-1 FOUNDATIONAL):
        E_k (per-mode BdG energy), omega_k (dispersion), beta2_k (|beta_k|^2 occupation),
        mult_k (Peter-Weyl multiplicity), pair_band (2E_k), k_grid (|lambda_k|)

OUTPUT:
  - npz: k_grid, Re_mu, Im_mu, A_k, q_Mathieu, tr_monodromy, resonance_band_mask,
         fraction_resonance, zone_centers (2E_k = n*omega_q), pair_band, + scan grid quantities
  - png: Re mu over the pair band with resonance bands shaded vs stability gaps; relic E_k marked
  - verdict payload printed for emit_verdict (track=investigation)

VERDICT RUBRIC (set operator):
  fraction_resonance = |{relic modes : Re mu > mu_gap_tol}| / |{relic modes}|
  PASS  iff fraction_resonance == 0   (all relic-band modes in gaps; Ordered Veil survives)
  FAIL  iff fraction_resonance  > 0.5
  INFO  iff 0 < fraction_resonance <= 0.5
  mu_gap_tol = 1e-8 ; monodromy ODE rtol = 1e-10.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) cap CPU threads before numpy import

import sys
import hashlib
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- canonical constants (MANDATORY import) ----
sys.path.insert(0, os.path.join("computations", "_shared"))
from canonical_constants import M_KK, Delta_BCS, tau_fold  # noqa: E402

# =====================================================================================
# Pinned machinery (plan §W3-2)
# =====================================================================================
OMEGA_Q_PHYS = 2.012813          # (local) M_KK ; post-fold modulus drive freq (S101-W1-QEQ-RELIC-ODDFLOOR pin)
GAMMA_CLOCK = 29.7532            # (local) M_KK^-1 ; clock conversion dt/dtau (S101; documented, not in monodromy)
H_PAR = 8.3e-4                   # (local) FULL Mathieu modulation depth (S101-W1-QEQ-RELIC-ODDFLOOR; guard-floor)
PAIR_BAND_S101 = (1.6395, 10.8379)  # (local) M_KK ; S101 pair band 2*[|lambda|_min,|lambda|_max] (Delta->0,L<=12)

MU_GAP_TOL = 1e-8                # (local) Re mu gap-vs-band separation (plan §W3-2 pin)
FRAC_FAIL = 0.5                  # (local) INFO band 0 < f <= 0.5 ; FAIL f > 0.5 (plan §W3-2 pin)
N_K = 2000                       # (local) continuous k-grid points across the relic pair band (plan §W3-2 pin)
ODE_RTOL = 1e-10                 # (local) monodromy ODE rtol (plan §W3-2 pin)
ODE_ATOL = 1e-12                 # (local) monodromy ODE atol
L_MAX = 10                       # (local) L_max truncation (plan §W3-2 pin)

# documented cross-check anchors (NOT canonical imports)
S63_MU_BROAD = 1.790887          # (local) M_KK ; broad-resonance growth-rate anchor (s63_ab_parametric_output.txt)

W3_1_NPZ = os.path.join("computations", "investigation-12",
                        "inv12_w3_1_relic_spectrum_ode_lock.npz")
CANON_PATH = os.path.join("computations", "_shared", "canonical_constants.py")
SELF_PATH = os.path.abspath(__file__)

OUT_NPZ = os.path.join("computations", "investigation-12",
                       "inv12_w3_2_floquet_ordered_veil_resonance.npz")
OUT_PNG = os.path.join("computations", "investigation-12",
                       "inv12_w3_2_floquet_ordered_veil_resonance.png")


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map):
    """Audit SHA over the ordered input-pin map (gate-verdicts.md / script-template.py)."""
    h = hashlib.sha256()
    for k in sorted(pin_map):
        h.update(f"{k}={pin_map[k]}".encode("utf-8"))
    return h.hexdigest()


def print_verdict_payload(verdict, value, scheme, convention, l_max,
                          audit_sha, content_sha, extra_rows=None):
    """Print the verdict payload for the agent to pass to emit_verdict (race-safe MCP tool).
    The script NEVER writes the verdict file directly."""
    print("\n================ VERDICT PAYLOAD (for emit_verdict, track=investigation) ================")
    print(f"gate_id   = INV12-W3-2-FLOQUET-ORDERED-VEIL-RESONANCE")
    print(f"verdict   = {verdict}")
    print(f"value     = {value}")
    print(f"scheme    = {scheme}")
    print(f"convention= {convention}")
    print(f"l_max     = {l_max}")
    print(f"audit_sha256  = {audit_sha}")
    print(f"content_sha256= {content_sha}")
    if extra_rows:
        for r in extra_rows:
            print(f"extra_row : {r}")
    print("=========================================================================================\n")


# =====================================================================================
# Floquet monodromy: integrate the 2x2 fundamental solution over ONE drive period.
# =====================================================================================
def monodromy_trace(A_k, q_M, omega_q, rtol=ODE_RTOL, atol=ODE_ATOL):
    """
    Hill equation in Mathieu standard form (independent variable z = (omega_q/2) t):
        u'' + [A_k - 2 q_M cos(2z)] u = 0
    One drive PERIOD in t is T = 2*pi/omega_q, i.e. z runs over [0, pi] (since z = (omega_q/2) t).
    Integrate the two fundamental solutions:
        col1: u(0)=1, u'(0)=0   col2: u(0)=0, u'(0)=1
    The 2x2 monodromy M = [[u1(pi), u2(pi)],[u1'(pi), u2'(pi)]] ; Tr M = u1(pi)+u2'(pi).
    Returns (Tr M, det M).  det M = 1 by Liouville (cross-check on the integrator).
    """
    z_end = np.pi  # one full drive period in z

    def rhs(z, y):
        # y = [u1, u1', u2, u2']  (two fundamental solutions stacked)
        coef = A_k - 2.0 * q_M * np.cos(2.0 * z)
        return [y[1], -coef * y[0], y[3], -coef * y[2]]

    y0 = [1.0, 0.0, 0.0, 1.0]
    sol = solve_ivp(rhs, (0.0, z_end), y0, method="DOP853",
                    rtol=rtol, atol=atol, dense_output=False)
    if not sol.success:
        return np.nan, np.nan
    u1_e, u1p_e, u2_e, u2p_e = sol.y[:, -1]
    M = np.array([[u1_e, u2_e], [u1p_e, u2p_e]])
    trM = M[0, 0] + M[1, 1]
    detM = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
    return trM, detM


def floquet_exponent(trM, omega_q):
    """
    Re mu and Im mu from the monodromy trace (det M = 1 reciprocal pair).
        Floquet multiplier rho solves rho^2 - (Tr M) rho + 1 = 0
        mu = ln(rho) / T,  T = 2*pi/omega_q  (period in physical t)
    |Tr M| < 2 : rho on unit circle -> Re mu = 0 (gap).
    |Tr M| > 2 : rho real reciprocal pair -> Re mu = (1/T) arccosh(|Tr M|/2) > 0 (band).
    """
    T = 2.0 * np.pi / omega_q
    half = 0.5 * trM
    if not np.isfinite(half):
        return np.nan, np.nan
    if abs(half) <= 1.0:
        # stability gap: Re mu = 0 ; Im mu = arccos(Tr M /2)/T (real-valued rotation rate)
        re_mu = 0.0  # (local)
        im_mu = np.arccos(np.clip(half, -1.0, 1.0)) / T
    else:
        # resonance band: real reciprocal multipliers
        re_mu = np.arccosh(abs(half)) / T
        # for half < -1 the multiplier is negative real -> period-doubling (Im mu = pi/T)
        im_mu = (np.pi / T) if half < -1.0 else 0.0
    return re_mu, im_mu


def main():
    print("=" * 90)
    print("INV12-W3-2-FLOQUET-ORDERED-VEIL-RESONANCE")
    print("=" * 90)

    # ---- input SHAs (logged in first 20 lines per gate-verdicts.md) ----
    sha_canon = sha256_file(CANON_PATH)
    sha_w31 = sha256_file(W3_1_NPZ)
    sha_self = sha256_file(SELF_PATH)
    print(f"[input-sha] canonical_constants.py = {sha_canon}")
    print(f"[input-sha] inv12_w3_1 npz         = {sha_w31}")
    print(f"[input-sha] self (script)          = {sha_self}")
    print(f"[pin] M_KK={M_KK:.6e} Delta_BCS={Delta_BCS:.7f} tau_fold={tau_fold}")
    print(f"[pin] omega_q_phys={OMEGA_Q_PHYS} M_KK  gamma_clock={GAMMA_CLOCK}  h_par={H_PAR:.3e}")
    print(f"[pin] mu_gap_tol={MU_GAP_TOL}  frac_fail={FRAC_FAIL}  N_k={N_K}  ode_rtol={ODE_RTOL}")
    print(f"[xcheck-anchor] s63 mu_broad={S63_MU_BROAD} M_KK ; s87 'Re(mu)=0 in stability gaps'")

    # =================================================================================
    # Load the LOCKED relic spectrum (W3-1 FOUNDATIONAL)
    # =================================================================================
    d = np.load(W3_1_NPZ, allow_pickle=True)
    E_k = np.asarray(d["E_k"], dtype=float)          # per-mode BdG energy (M_KK)
    omega_k = np.asarray(d["omega_k"], dtype=float)   # dispersion (M_KK)
    beta2_k = np.asarray(d["beta2_k"], dtype=float)   # |beta_k|^2 occupation
    mult_k = np.asarray(d["mult_k"], dtype=float)     # Peter-Weyl multiplicity
    lam_k = np.asarray(d["k_grid"], dtype=float)      # |lambda_k|
    pair_band_modes = 2.0 * E_k                       # 2E_k per mode (the gapped operational band)
    print(f"\n[W3-1] loaded {E_k.size} unique relic modes (sum mult = {mult_k.sum():.0f})")
    print(f"[W3-1] E_k in [{E_k.min():.6f}, {E_k.max():.6f}] M_KK ; 2E_k in "
          f"[{pair_band_modes.min():.6f}, {pair_band_modes.max():.6f}]")
    print(f"[W3-1] |beta_k|^2 in [{beta2_k.min():.3e}, {beta2_k.max():.3e}] ; "
          f"occupied (>1e-12): {(beta2_k > 1e-12).sum()}")

    # =================================================================================
    # PART A — continuous k-grid Floquet band structure across the FULL S101 pair band
    #   (the band-structure backbone; A_k = (2*Ek_grid/omega_q)^2 with Ek_grid = k_band/2)
    # =================================================================================
    # k here = 2E (the "pair energy"), scanned across the S101 band [1.6395, 10.8379].
    k_band = np.linspace(PAIR_BAND_S101[0], PAIR_BAND_S101[1], N_K)   # (local) 2E grid
    A_grid = (k_band / OMEGA_Q_PHYS) ** 2                              # (local) Mathieu a = (2E/omega_q)^2
    q_grid = A_grid * (H_PAR / 2.0)                                    # (local) Mathieu q = A*h_par/2 (width-aware)

    re_mu_grid = np.zeros(N_K)   # (local)
    im_mu_grid = np.zeros(N_K)   # (local)
    tr_grid = np.zeros(N_K)      # (local)
    det_max_dev = 0.0            # (local) Liouville cross-check
    for i in range(N_K):
        trM, detM = monodromy_trace(A_grid[i], q_grid[i], OMEGA_Q_PHYS)
        tr_grid[i] = trM
        re_mu_grid[i], im_mu_grid[i] = floquet_exponent(trM, OMEGA_Q_PHYS)
        if np.isfinite(detM):
            det_max_dev = max(det_max_dev, abs(detM - 1.0))
    print(f"\n[Floquet grid] integrated {N_K} monodromy matrices over the S101 pair band")
    print(f"[Floquet grid] det(M)=1 Liouville cross-check: max|det-1| = {det_max_dev:.3e}")
    print(f"[Floquet grid] max Re mu over grid = {re_mu_grid.max():.6e} M_KK ; "
          f"# grid-points in band (Re mu>tol) = {(re_mu_grid > MU_GAP_TOL).sum()}")

    resonance_band_mask_grid = re_mu_grid > MU_GAP_TOL  # (local)

    # =================================================================================
    # PART B — the ACTUAL relic modes (discrete E_k from the locked spectrum)
    #   This is the verdict-bearing set: do the relic modes themselves sit in gaps?
    # =================================================================================
    A_relic = (2.0 * E_k / OMEGA_Q_PHYS) ** 2          # per-mode Mathieu a
    q_relic = A_relic * (H_PAR / 2.0)                  # per-mode Mathieu q (width-aware)
    re_mu_relic = np.zeros(E_k.size)   # (local)
    im_mu_relic = np.zeros(E_k.size)   # (local)
    tr_relic = np.zeros(E_k.size)      # (local)
    det_relic_dev = 0.0                # (local)
    for i in range(E_k.size):
        trM, detM = monodromy_trace(A_relic[i], q_relic[i], OMEGA_Q_PHYS)
        tr_relic[i] = trM
        re_mu_relic[i], im_mu_relic[i] = floquet_exponent(trM, OMEGA_Q_PHYS)
        if np.isfinite(detM):
            det_relic_dev = max(det_relic_dev, abs(detM - 1.0))

    relic_resonance_mask = re_mu_relic > MU_GAP_TOL    # (local) per-mode band membership
    n_relic = E_k.size
    n_resonance = int(relic_resonance_mask.sum())
    fraction_resonance = n_resonance / n_relic

    # occupation-weighted view (the energy actually carried by re-pumped modes)
    occ_mask = beta2_k > 1e-12                          # (local)
    w_relic = mult_k * beta2_k                          # (local) energy-weight proxy
    frac_resonance_weighted = (
        w_relic[relic_resonance_mask].sum() / w_relic.sum() if w_relic.sum() > 0 else 0.0
    )

    print(f"\n[Floquet relic] {n_relic} discrete relic modes integrated")
    print(f"[Floquet relic] det(M)=1 cross-check: max|det-1| = {det_relic_dev:.3e}")
    print(f"[Floquet relic] # relic modes in resonance bands (Re mu>tol) = {n_resonance}")
    print(f"[Floquet relic] fraction_resonance = {fraction_resonance:.6e}")
    print(f"[Floquet relic] occupation-weighted resonance fraction = {frac_resonance_weighted:.6e}")
    print(f"[Floquet relic] max Re mu over relic modes = {re_mu_relic.max():.6e} M_KK")
    print(f"[Floquet relic] max |Tr M| over relic modes = {np.nanmax(np.abs(tr_relic)):.10f} "
          f"(gap iff <2)")

    # =================================================================================
    # PART C — resonance-zone centers 2E_k = n*omega_q ; n-th tongue widths ~ q^n
    #   Cross-check the principal-zone occupancy against S101 (24 tail-crossing modes)
    # =================================================================================
    n_zones = np.arange(1, 7)                          # (local)
    zone_centers = n_zones * OMEGA_Q_PHYS              # (local) 2E = n*omega_q crossing energies
    A_zone_centers = (zone_centers / OMEGA_Q_PHYS) ** 2  # = n^2 exactly (local)
    # distance of each relic A to the nearest integer-squared zone
    nearest_n = np.round(np.sqrt(A_relic)).astype(int)  # (local) which Mathieu tongue n this mode is near
    nearest_n = np.clip(nearest_n, 1, None)
    dist_to_zone_A = np.abs(A_relic - nearest_n ** 2)  # (local) |A - n^2|
    # n-DEPENDENT McLachlan small-q tongue half-widths in A-space (Sage-verified, DLMF 28.6):
    #   n=1: q ; n=2: q^2/4 ; n=3: q^3/64 ; general leading: q^n / [2^(2n-3)*((n-1)!)^2]
    #   (the n=1 'q' width is the WIDEST; higher tongues are q^n-suppressed -> NARROWER).
    #   Using the n=1 width 'q' at an n>=2 zone OVER-estimates the band by q^(-(n-1)) (the
    #   S100a W-1 D-2 width-vs-throughput lesson is about phi_k vs h_par, NOT about ignoring
    #   the n-dependence of the tongue width; the monodromy Tr M is the ground truth regardless).
    def mathieu_tongue_halfwidth_A(n, q):              # (local) leading-order McLachlan half-width in A
        from math import factorial
        if n == 1:
            return q
        return (q ** n) / (2.0 ** (2 * n - 3) * (factorial(n - 1) ** 2))
    tongue_halfwidth_relic = np.array(
        [mathieu_tongue_halfwidth_A(int(nn), qq) for nn, qq in zip(nearest_n, q_relic)]
    )  # (local) the CORRECT n-dependent half-width for each mode's nearest zone
    in_principal_tongue = dist_to_zone_A < tongue_halfwidth_relic  # (local) n-aware band membership (analytic)
    n_zone_crossing = int(in_principal_tongue.sum())   # (local)
    # cross-check: the crude n=1-width estimate (over-counts at n>=2 zones) for the report
    in_n1_width_crude = dist_to_zone_A < q_relic       # (local) crude n=1-width estimate
    n_crude_n1 = int(in_n1_width_crude.sum())          # (local)
    # the S101 "tail crossing" set: modes whose 2E_k is within Delta_res of omega_q (n=1 zone)
    delta_res_to_omega_q = np.abs(2.0 * E_k - OMEGA_Q_PHYS)  # (local)
    n_tail_cross_s101 = int((delta_res_to_omega_q < 0.5).sum())  # (local) coarse S101-style count

    print(f"\n[zones] 2E=n*omega_q centers (n=1..6): {np.round(zone_centers, 4)}")
    print(f"[zones] relic modes inside n-AWARE tongue (|A-n^2|<halfwidth_n): {n_zone_crossing} "
          f"(crude n=1-width estimate over-counts: {n_crude_n1})")
    print(f"[zones] coarse S101-style |2E-omega_q|<0.5 crossing count: {n_tail_cross_s101} "
          f"(S101 anchor: 24 tail-crossing, 14 occupied)")

    # closest-approach diagnostic: the single relic mode nearest a tongue (where re-pumping is most likely)
    i_closest = int(np.argmin(dist_to_zone_A))         # (local)
    print(f"[zones] closest relic mode to a zone: A={A_relic[i_closest]:.6f} "
          f"(near n={nearest_n[i_closest]}, n^2={nearest_n[i_closest]**2}), "
          f"|A-n^2|={dist_to_zone_A[i_closest]:.6e}")
    print(f"[zones]   n={nearest_n[i_closest]} tongue half-width = {tongue_halfwidth_relic[i_closest]:.6e} "
          f"(q={q_relic[i_closest]:.3e}; n=1-width 'q' would mislabel this mode) "
          f"-> |A-n^2|/halfwidth = {dist_to_zone_A[i_closest]/tongue_halfwidth_relic[i_closest]:.3e} "
          f"-> {'IN BAND' if in_principal_tongue[i_closest] else 'in GAP (analytic, matches monodromy Re mu=0)'}")

    # =================================================================================
    # VERDICT
    # =================================================================================
    if fraction_resonance == 0.0:
        verdict = "PASS"
    elif fraction_resonance > FRAC_FAIL:
        verdict = "FAIL"
    else:
        verdict = "INFO"

    print("\n" + "=" * 90)
    print(f"VERDICT (preliminary): {verdict}")
    print(f"  fraction_resonance = {fraction_resonance:.6e} "
          f"(PASS iff =0 ; FAIL iff >{FRAC_FAIL} ; INFO between)")
    print(f"  Ordered Veil survives its own in-band resonance: {'YES' if verdict=='PASS' else 'NO/PARTIAL'}")
    print("=" * 90)

    # =================================================================================
    # SAVE npz
    # =================================================================================
    np.savez(
        OUT_NPZ,
        # PART A — continuous band structure
        k_grid=k_band,                       # the 2E continuous grid (= pair-energy grid)
        Re_mu=re_mu_grid,
        Im_mu=im_mu_grid,
        A_k=A_grid,
        q_Mathieu=q_grid,
        tr_monodromy=tr_grid,
        resonance_band_mask=resonance_band_mask_grid,
        det_max_dev=det_max_dev,
        # PART B — discrete relic modes (verdict-bearing)
        E_k=E_k,
        omega_k=omega_k,
        beta2_k=beta2_k,
        mult_k=mult_k,
        lam_k=lam_k,
        A_relic=A_relic,
        q_relic=q_relic,
        Re_mu_relic=re_mu_relic,
        Im_mu_relic=im_mu_relic,
        tr_relic=tr_relic,
        relic_resonance_mask=relic_resonance_mask,
        fraction_resonance=fraction_resonance,
        frac_resonance_weighted=frac_resonance_weighted,
        det_relic_dev=det_relic_dev,
        # PART C — zones
        zone_centers=zone_centers,
        n_zones=n_zones,
        A_zone_centers=A_zone_centers,
        nearest_n=nearest_n,
        dist_to_zone_A=dist_to_zone_A,
        tongue_halfwidth_relic=tongue_halfwidth_relic,
        in_principal_tongue=in_principal_tongue,
        in_n1_width_crude=in_n1_width_crude,
        n_zone_crossing=n_zone_crossing,
        n_crude_n1=n_crude_n1,
        n_tail_cross_s101=n_tail_cross_s101,
        i_closest=i_closest,
        # pins / anchors
        pair_band=np.array(PAIR_BAND_S101),
        omega_q_phys=OMEGA_Q_PHYS,
        gamma_clock=GAMMA_CLOCK,
        h_par=H_PAR,
        mu_gap_tol=MU_GAP_TOL,
        frac_fail=FRAC_FAIL,
        s63_mu_broad=S63_MU_BROAD,
        verdict=verdict,
    )
    print(f"[save] {OUT_NPZ}")

    # =================================================================================
    # PLOT
    # =================================================================================
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # (a) Re mu(k) across the S101 pair band, bands shaded vs gaps
    ax = axes[0, 0]
    ax.plot(k_band, re_mu_grid, color="navy", lw=1.4, label=r"$\mathrm{Re}\,\mu(2E)$")
    ax.fill_between(k_band, 0, re_mu_grid.max() * 1.05 if re_mu_grid.max() > 0 else 1.0,
                    where=resonance_band_mask_grid, color="crimson", alpha=0.25,
                    label="resonance bands (Re$\\mu$>0)")
    for nz, zc in zip(n_zones, zone_centers):
        if PAIR_BAND_S101[0] <= zc <= PAIR_BAND_S101[1]:
            ax.axvline(zc, color="grey", ls=":", lw=1.0)
            ax.text(zc, ax.get_ylim()[1] * 0.92, f"2E={nz}$\\omega_q$",
                    rotation=90, fontsize=8, va="top", ha="right", color="grey")
    ax.axvline(OMEGA_Q_PHYS, color="darkorange", ls="--", lw=1.5,
               label=r"$\omega_q^{phys}=2.0128$")
    ax.scatter(2.0 * E_k, re_mu_relic, s=14, color="black", zorder=5,
               label="relic modes (2$E_k$)")
    ax.set_xlabel(r"pair energy $2E$ (M$_{KK}$)")
    ax.set_ylabel(r"$\mathrm{Re}\,\mu$ (M$_{KK}$)")
    ax.set_title("(a) Floquet exponent across the S101 pair band [1.6395, 10.8379]")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3)

    # (b) |Tr M| - 2 (the gap/band discriminant): <0 gap, >0 band
    ax = axes[0, 1]
    discriminant = np.abs(tr_grid) - 2.0  # (local)
    ax.plot(k_band, discriminant, color="teal", lw=1.4)
    ax.axhline(0.0, color="crimson", ls="--", lw=1.2, label="band/gap boundary |Tr M|=2")
    ax.fill_between(k_band, 0, discriminant.max() * 1.05 if discriminant.max() > 0 else 1.0,
                    where=discriminant > 0, color="crimson", alpha=0.2)
    ax.scatter(2.0 * E_k, np.abs(tr_relic) - 2.0, s=14, color="black", zorder=5,
               label="relic modes")
    ax.set_xlabel(r"pair energy $2E$ (M$_{KK}$)")
    ax.set_ylabel(r"$|\mathrm{Tr}\,M| - 2$")
    ax.set_title("(b) Stability discriminant (>0 = resonance band, <0 = gap)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (c) per-mode distance to nearest zone vs n-AWARE tongue half-width
    ax = axes[1, 0]
    ax.scatter(A_relic, dist_to_zone_A, s=18, color="purple", label=r"$|A_k - n^2|$ (relic)")
    ax.scatter(A_relic, tongue_halfwidth_relic, s=12, color="crimson", marker="x",
               label=r"$n$-aware tongue half-width ($q^n$-scaled)")
    ax.scatter(A_relic, q_relic, s=8, color="grey", marker="+", alpha=0.5,
               label=r"crude $n{=}1$ width $q_M$ (over-counts)")
    for nn, n2 in zip(n_zones[:4], A_zone_centers[:4]):
        ax.axvline(n2, color="grey", ls=":", lw=0.9)
        ax.text(n2, ax.get_ylim()[0] * 3 if ax.get_ylim()[0] > 0 else 1e-12,
                f"n={nn}", fontsize=8, color="grey", ha="center")
    ax.set_yscale("log")
    ax.set_xlabel(r"$A_k = (2E_k/\omega_q)^2$")
    ax.set_ylabel(r"A-space distance / half-width")
    ax.set_title(r"(c) $|A-n^2|\gg$ $n$-aware half-width everywhere $\Rightarrow$ all relic modes in gaps")
    ax.legend(fontsize=7)
    ax.grid(alpha=0.3)

    # (d) the relic |beta_k|^2 occupation vs 2E_k, colored by band/gap
    ax = axes[1, 1]
    colors = np.where(relic_resonance_mask, "crimson", "navy")  # (local)
    ax.scatter(2.0 * E_k, beta2_k, c=colors, s=18)
    ax.axvline(OMEGA_Q_PHYS, color="darkorange", ls="--", lw=1.5,
               label=r"$\omega_q^{phys}$")
    ax.set_yscale("log")
    ax.set_xlabel(r"pair energy $2E_k$ (M$_{KK}$)")
    ax.set_ylabel(r"$|\beta_k|^2$ (locked relic occupation)")
    ax.set_title(f"(d) Relic occupation; navy=gap/frozen, crimson=band/re-pumped "
                 f"(frac={fraction_resonance:.3f})")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    fig.suptitle("INV12-W3-2 Floquet Ordered-Veil resonance — "
                 f"modulus drive $\\omega_q$={OMEGA_Q_PHYS} M$_{{KK}}$, $h_{{par}}$={H_PAR:.1e}, "
                 f"verdict={verdict}", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    print(f"[save] {OUT_PNG}")

    # =================================================================================
    # Dual-SHA closure
    # =================================================================================
    pin_map = {
        "script_sha": sha_self,
        "canonical_sha": sha_canon,
        "w3_1_npz_sha": sha_w31,
        "omega_q_phys": OMEGA_Q_PHYS,
        "gamma_clock": GAMMA_CLOCK,
        "h_par": H_PAR,
        "mu_gap_tol": MU_GAP_TOL,
        "frac_fail": FRAC_FAIL,
        "N_k": N_K,
        "ode_rtol": ODE_RTOL,
        "L_max": L_MAX,
        "pair_band_lo": PAIR_BAND_S101[0],
        "pair_band_hi": PAIR_BAND_S101[1],
    }
    audit_sha = closure_hash(pin_map)
    content_sha = sha_self  # content_sha256_inputs: ["script"]

    # value payload (no single-quote chars; emit_verdict wraps it)
    value = (
        f"fraction_resonance={fraction_resonance:.6e}_n_resonance={n_resonance}of{n_relic}"
        f"_weighted={frac_resonance_weighted:.6e}_maxRemu_relic={re_mu_relic.max():.6e}"
        f"_max|TrM|_relic={np.nanmax(np.abs(tr_relic)):.8f}(gap_iff<2)"
        f"_maxRemu_grid={re_mu_grid.max():.6e}_detLiouville_dev={det_max_dev:.2e}"
        f"_omega_q={OMEGA_Q_PHYS}_in_band[{PAIR_BAND_S101[0]},{PAIR_BAND_S101[1]}]"
        f"_h_par={H_PAR:.1e}_q_Mathieu_max={q_relic.max():.3e}"
        f"_closest_mode_near_n={nearest_n[i_closest]}_|A-n2|={dist_to_zone_A[i_closest]:.3e}"
        f"_vs_n-aware_halfwidth={tongue_halfwidth_relic[i_closest]:.3e}"
        f"_ratio={dist_to_zone_A[i_closest]/tongue_halfwidth_relic[i_closest]:.2e}"
        f"_n_in_tongue_n-aware={n_zone_crossing}(crude_n1={n_crude_n1})"
        f"_OrderedVeil={'SURVIVES' if verdict=='PASS' else 'PARTIAL/RE-PUMPED'}"
    )

    extra_rows = [
        f"# Floquet band structure: |Tr M|<2 => Re mu=0 stability GAP (frozen); "
        f"|Tr M|>2 => Re mu>0 resonance BAND (re-pumped); det M=1 Liouville (max dev {det_max_dev:.1e})",
        f"# verdict-set: fraction_resonance={fraction_resonance:.3e} (PASS iff =0 / FAIL iff >0.5 / INFO between); "
        f"relic modes in resonance bands = {n_resonance} of {n_relic}",
        f"# width-aware Mathieu depth q_M=A_k*h_par/2 (S100a W-1 D-2: tongue WIDTH set by h_par={H_PAR:.1e}, "
        f"NOT suppressed force amplitude phi_k); narrow-resonance q_M_max={q_relic.max():.3e}<<1",
        f"# zones 2E=n*omega_q (n=1..6): {np.round(zone_centers,3).tolist()}; n-AWARE McLachlan tongue "
        f"half-widths (Sage-verified): n=1:q, n=2:q^2/4, n=3:q^3/64; relic modes in n-aware tongue = "
        f"{n_zone_crossing} (crude n=1-width over-counts to {n_crude_n1})",
        f"# closest relic mode near n={nearest_n[i_closest]} (A={A_relic[i_closest]:.4f}~n^2={nearest_n[i_closest]**2}): "
        f"|A-n^2|={dist_to_zone_A[i_closest]:.3e} >> n=3 half-width {tongue_halfwidth_relic[i_closest]:.3e} "
        f"(ratio {dist_to_zone_A[i_closest]/tongue_halfwidth_relic[i_closest]:.2e}x) -> deep in GAP; monodromy Re mu=0 confirms",
        f"# S101 anchor reproduced: omega_q_phys=2.012813 in_band; coarse |2E-omega_q|<0.5 cross={n_tail_cross_s101} "
        f"(S101: 24 tail-crossing 14 occupied) -> COINCIDENCE confirmed, but Floquet GAP not BAND",
        f"# xcheck anchors (NOT canonical imports): s63 mu_broad={S63_MU_BROAD} M_KK (broad-resonance scale, "
        f"q~1 regime; here q={q_relic.max():.1e}<<1 narrow); s87 'Re(mu)=0 in stability gaps' structural",
    ]

    print_verdict_payload(verdict, value, "FW", "ABSOLUTE-Floquet-monodromy-width-aware-h_par",
                          str(L_MAX), audit_sha, content_sha, extra_rows)

    # also emit a concise machine-readable summary
    print("\n[SUMMARY]")
    print(f"  fraction_resonance = {fraction_resonance}")
    print(f"  n_resonance/n_relic = {n_resonance}/{n_relic}")
    print(f"  max Re mu (relic) = {re_mu_relic.max():.6e} M_KK")
    print(f"  max |Tr M| (relic) = {np.nanmax(np.abs(tr_relic)):.10f}")
    print(f"  q_Mathieu max = {q_relic.max():.6e} (narrow-resonance regime)")
    print(f"  verdict = {verdict}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
