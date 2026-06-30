#!/usr/bin/env python3
"""
S80 W1-3: FOLD-INST-GRADIENT (path-integral consult, feynman-theorist)
======================================================================

Independent cross-check of kaku's primary (single-instanton spectral-action form).

METHOD (path-integral view):
    S_inst[Phi_inst, tau] = int d^4x L_E[Phi_inst(x), tau]         (Euclidean action)
    Z = int D[Phi] exp(-S_E[Phi, tau])                             (path integral)

    At a saddle, Feynman-Hellmann gives:
        dS_inst/dtau = int d^4x (partial L_E / partial tau)|_{Phi=Phi_inst}
                     + 0  (boundary terms vanish, Phi_inst -> vac at infinity)

    The explicit tau-derivative of L_E has two channels:
        (a) DIRECT: L_E inherits the full substrate spectral action S_total(tau)
            at each space-time point (substrate-first framing).  Then
                dS_inst/dtau = dS_total/dtau  (from S42 gradient_stiffness data).
        (b) SINGLE-INSTANTON: S_inst(tau) = (8*pi^2 / g_eff^2(tau)) * kappa(tau)
            where g_eff^2(tau) inherits Jensen coupling running g_1/g_2 = e^{-2tau}
            and kappa(tau) = sqrt(Z(tau)/Z_fold) captures the fluctuation prefactor.
            Then
                dS_inst/dtau = (8*pi^2 * kappa) * d(1/g_eff^2)/dtau
                             + (8*pi^2 / g_eff^2) * dkappa/dtau.

    Both prescriptions are Euclidean (convention: exp(-S_E) is the weight).
    Step function evaluated at tau in {0.15, 0.17, 0.19, 0.21, 0.25}.

SUBSTITUTION CHAIN (MANDATORY [VERIFY]):
    Step 1: S_inst(tau) := int d^4x L_E[Phi_inst, tau]
            S_total(tau) := S42 spectral action (S_full(tau) from s42_gradient_stiffness.npz)
            g_eff^2(tau) := g_base^2 * exp(+tau/4)
                            (from Jensen coupling weights 1/8 U(1) + 3/8 SU(2) + 4/8 C^2
                             with exponents -2, 0, +1; product gives exp(+tau/4))
            kappa(tau) := sqrt(Z(tau)/Z_fold) with Z(tau) = d^2 S_total / dtau^2
    Step 2: Substitute. Prescription A: dS_inst/dtau|_A = dS_total/dtau.
            Prescription B: dS_inst/dtau|_B = 8*pi^2 * [kappa * d(1/g_eff^2)/dtau
                                                    + (1/g_eff^2) * dkappa/dtau].
    Step 3: Numerical evaluation on tau_grid from s42.
    Step 4: Read tau_peak := argmax |dS_inst/dtau|.
            PASS iff |tau_peak - tau_fold| <= 0.02.

The gate PASSES iff kappa's tau-derivative generates a narrow peak at tau_fold
via Z(tau) = d^2 S_total/dtau^2.

NOTE: The Feynman-Hellmann theorem says (at a saddle) that only the EXPLICIT
tau-dependence contributes -- the implicit Phi_inst(tau) dependence drops out.

Output:
    computations/session-80/s80_fold_inst_gradient_feynman.npz
    computations/session-80/s80_fold_inst_gradient_feynman.png
    4-tuple (dS_inst_dtau_peak, scheme=path-integral, convention=Euclidean, L_max=5)

Author: feynman-theorist (S80 W1-3 consult)
Date: 2026-04-17
"""
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')                  # (local) CPU cap for 8-tau grid
os.environ.setdefault('MKL_NUM_THREADS', '8')                  # (local) CPU cap

import sys
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    tau_fold, dS_fold, d2S_fold, S_fold, Z_fold,
    c_fabric, g_SU2_fold, g_U1_fold, PI,
)

# =========================================================================
# CONFIGURATION
# =========================================================================

# Pre-registered tau scan (from session-80-plan.md lines 960, 990-1008).
TAU_SCAN = np.array([0.15, 0.17, 0.19, 0.21, 0.25])    # (local) pre-registered gate grid
TAU_FOLD_ABS_WINDOW_PASS = 0.02                          # (local) PASS window
TAU_FOLD_ABS_WINDOW_INFO = 0.05                          # (local) INFO window

# S42 gradient-stiffness full grid (source of truth for S_total(tau)).
S42_DATA_PATH = os.path.join(                                  # (local) npz path
    os.path.dirname(SCRIPT_DIR), 'computations/_shared', 's42_gradient_stiffness.npz')


# =========================================================================
# FEYNMAN-HELLMANN DERIVATIVES (PRESCRIPTION A: DIRECT SPECTRAL ACTION)
# =========================================================================

def load_s42_spectral_action():
    """Load the full spectral-action field S_total(tau) from S42."""
    d = np.load(S42_DATA_PATH, allow_pickle=True)
    return {
        'tau_grid': d['tau_grid'],         # 10-point grid
        'S_total':  d['S_total'],          # S_full(tau)
        'dS_dtau':  d['dS_dtau'],          # dS_full / dtau (finite-diff, S42)
        'd2S_dtau2':d['d2S_dtau2'],        # d^2 S_full / dtau^2
        'Z_spec':   d['Z_spectral'],       # Z(tau) = gradient stiffness
    }


def prescription_A_direct(s42, tau_scan):
    """
    PRESCRIPTION A -- DIRECT spectral-action inheritance.

    Path-integral reading: L_E at each x contains the substrate's full
    spectral functional, so S_inst(tau) = S_total(tau) (one-fiber action).
    Then dS_inst/dtau = dS_total/dtau at the pre-registered tau values.
    """
    # Cubic spline interpolant on the full s42 grid for smooth evaluation.
    tau_g = s42['tau_grid']
    S_tot = s42['S_total']
    cs_S = CubicSpline(tau_g, S_tot)                          # (local)
    dS_num = cs_S(tau_scan, 1)                                # (local) 1st deriv
    d2S_num = cs_S(tau_scan, 2)                                # (local) 2nd deriv

    # Central differences as independent cross-check (step size = s42 native).
    cs_dS = CubicSpline(tau_g, s42['dS_dtau'])                # (local)
    dS_native = cs_dS(tau_scan)                               # (local)

    return {
        'dS_inst_dtau_splineA': dS_num,
        'd2S_inst_dtau2_splineA': d2S_num,
        'dS_inst_dtau_nativeA': dS_native,
    }


# =========================================================================
# SINGLE-INSTANTON FORM (PRESCRIPTION B: 8 pi^2 / g_eff^2 * kappa)
# =========================================================================

def g_eff_sq(tau, g_base_sq):
    """
    Effective gauge coupling squared under Jensen deformation.

    Derivation: Jensen metric stretches fiber directions with exponents
        U(1):  exp(+2 tau)   (1 direction, weight 1/8)
        SU(2): exp(-2 tau)   (3 directions, weight 3/8)
        C^2:   exp(+1 tau)   (4 directions, weight 4/8)
    Geometric mean (arithmetic in log) of 1/g^2 weighted by direction count:
        log(g_base^2 / g_eff^2) = (1/8)*(-2 tau) + (3/8)*0 + (4/8)*(+1 tau)
                               = -tau/4 + tau/2 = +tau/4
        => g_eff^2(tau) = g_base^2 * exp(+tau/4).
    """
    return g_base_sq * np.exp(tau / 4.0)


def dg_eff_sq_dtau(tau, g_base_sq):
    """d g_eff^2 / d tau = (g_base^2 / 4) * exp(+tau/4) = g_eff^2 / 4."""
    return g_eff_sq(tau, g_base_sq) / 4.0


def kappa_of_tau(tau, s42_cs_Z):
    """
    Jensen instanton-density correction. The path-integral fluctuation
    determinant around the instanton gives det'(-D^2 + V''(Phi_inst))^{-1/2}.
    For a single modulus tau, the 1-loop prefactor scales as
        kappa(tau) = sqrt( Z(tau) / Z_fold )
    where Z(tau) = d^2 S_total / dtau^2 is the gradient stiffness.
    This ensures kappa(tau_fold) = 1 (normalization at the fold).
    """
    Z_tau = s42_cs_Z(tau)                                      # (local)
    return np.sqrt(Z_tau / Z_fold)


def dkappa_dtau(tau, s42_cs_Z):
    """dkappa/dtau = (1/(2 kappa)) * (1/Z_fold) * dZ/dtau."""
    Z_tau = s42_cs_Z(tau)                                      # (local)
    dZ_dtau_val = s42_cs_Z(tau, 1)                             # (local) 1st deriv of Z
    kappa = np.sqrt(Z_tau / Z_fold)                            # (local)
    return 0.5 * (dZ_dtau_val / Z_fold) / kappa


def prescription_B_single_instanton(s42, tau_scan):
    """
    PRESCRIPTION B -- single-instanton form, S_inst = (8 pi^2 / g_eff^2) * kappa.

    dS_inst/dtau = 8 pi^2 * [kappa * d(1/g_eff^2)/dtau + (1/g_eff^2) * dkappa/dtau]
                = 8 pi^2 * [-kappa * (dg_eff^2/dtau)/g_eff^4 + dkappa/dtau / g_eff^2].

    We use g_base_sq = 1 (coupling independent of absolute normalization for
    the argmax test; overall scale cancels in tau_peak location).
    """
    g_base_sq = 1.0                                            # (local) normalization scale
    # Cubic spline for Z(tau) and dZ/dtau on s42 grid.
    cs_Z = CubicSpline(s42['tau_grid'], s42['Z_spec'])         # (local)

    geff2 = g_eff_sq(tau_scan, g_base_sq)                      # (local) g_eff^2(tau)
    dgeff2 = dg_eff_sq_dtau(tau_scan, g_base_sq)                # (local)
    kappa = kappa_of_tau(tau_scan, cs_Z)                        # (local)
    dkappa = dkappa_dtau(tau_scan, cs_Z)                        # (local)

    # d(1/g^2)/dtau = -dg^2/dtau / g^4
    d_inv_geff2 = -dgeff2 / geff2**2                           # (local)

    term1 = 8.0 * PI**2 * kappa * d_inv_geff2                  # (local) coupling-running piece
    term2 = 8.0 * PI**2 * (1.0 / geff2) * dkappa                # (local) fluctuation piece
    dS_inst_dtau = term1 + term2                               # (local)

    S_inst = 8.0 * PI**2 * kappa / geff2                       # (local) total action

    return {
        'tau_scan':         tau_scan,
        'g_eff_sq':         geff2,
        'kappa':            kappa,
        'dkappa_dtau':      dkappa,
        'term1_running':    term1,
        'term2_fluctuation': term2,
        'dS_inst_dtau_B':   dS_inst_dtau,
        'S_inst_B':         S_inst,
    }


# =========================================================================
# GATE EVALUATION
# =========================================================================

def evaluate_gate(tau_scan, dS_inst_dtau, label):
    """
    Gate S80-FOLD-INST-GRADIENT:
        PASS iff argmax(|dS_inst/dtau|) is within 0.02 of tau_fold=0.190
        INFO iff within 0.05 but outside 0.02
        FAIL iff beyond 0.05 OR flat profile
    """
    idx_peak = int(np.argmax(np.abs(dS_inst_dtau)))            # (local)
    tau_peak = float(tau_scan[idx_peak])                        # (local)
    dtau_from_fold = abs(tau_peak - tau_fold)                   # (local)

    # Flatness check -- coefficient of variation.
    cv = np.std(dS_inst_dtau) / (abs(np.mean(dS_inst_dtau)) + 1e-30)  # (local)
    flat = cv < 0.05                                            # (local) <5% variation == flat

    if flat:
        verdict = 'FAIL'                                        # (local)
        reason = f'flat profile (CV={cv:.3%})'                  # (local)
    elif dtau_from_fold <= TAU_FOLD_ABS_WINDOW_PASS:
        verdict = 'PASS'                                        # (local)
        reason = f'tau_peak={tau_peak:.3f} within ±0.02 of fold'  # (local)
    elif dtau_from_fold <= TAU_FOLD_ABS_WINDOW_INFO:
        verdict = 'INFO'                                        # (local)
        reason = f'tau_peak={tau_peak:.3f} at 0.02-0.05 from fold'  # (local)
    else:
        verdict = 'FAIL'                                        # (local)
        reason = f'tau_peak={tau_peak:.3f} displaced >0.05 from fold'  # (local)

    print(f"\n=== GATE S80-FOLD-INST-GRADIENT ({label}) ===")
    print(f"  tau_scan:         {tau_scan}")
    print(f"  dS_inst/dtau:     {dS_inst_dtau}")
    print(f"  |dS_inst/dtau|:   {np.abs(dS_inst_dtau)}")
    print(f"  tau_peak:         {tau_peak:.4f}")
    print(f"  |delta tau|:      {dtau_from_fold:.4f}")
    print(f"  Coeff of var:     {cv:.4f}")
    print(f"  VERDICT:          {verdict} ({reason})")

    return {
        'tau_peak':       tau_peak,
        'dtau_from_fold': dtau_from_fold,
        'coeff_var':      cv,
        'verdict':        verdict,
        'reason':         reason,
    }


# =========================================================================
# MAIN
# =========================================================================

def main():
    print("="*70)
    print("S80 W1-3  FOLD-INST-GRADIENT  (path-integral consult, feynman-theorist)")
    print("="*70)
    print(f"tau_fold  = {tau_fold}")
    print(f"dS_fold   = {dS_fold}   (S42 canonical)")
    print(f"d2S_fold  = {d2S_fold}")
    print(f"Z_fold    = {Z_fold}")
    print(f"S_fold    = {S_fold}")
    print()

    # Load S42 spectral-action data.
    s42 = load_s42_spectral_action()
    print(f"S42 tau_grid: {s42['tau_grid']}")
    print(f"S42 S_total:  {s42['S_total']}")
    print(f"S42 Z_spec:   {s42['Z_spec']}")
    print()

    # --- PRESCRIPTION A: direct spectral action ---
    print("--- PRESCRIPTION A: dS_inst/dtau = dS_total/dtau (direct Feynman-Hellmann) ---")
    A = prescription_A_direct(s42, TAU_SCAN)
    print(f"  tau:               {TAU_SCAN}")
    print(f"  dS_inst/dtau|A:    {A['dS_inst_dtau_splineA']}")
    print(f"  d^2 S/dtau^2|A:    {A['d2S_inst_dtau2_splineA']}")
    gate_A = evaluate_gate(TAU_SCAN, A['dS_inst_dtau_splineA'], 'A:direct')
    print()

    # --- PRESCRIPTION B: single-instanton 8pi^2/g_eff^2 * kappa ---
    print("--- PRESCRIPTION B: single-instanton form 8 pi^2 / g_eff^2(tau) * kappa(tau) ---")
    B = prescription_B_single_instanton(s42, TAU_SCAN)
    print(f"  g_eff^2:           {B['g_eff_sq']}")
    print(f"  kappa:             {B['kappa']}")
    print(f"  dkappa/dtau:       {B['dkappa_dtau']}")
    print(f"  term1 (running):   {B['term1_running']}")
    print(f"  term2 (fluctn):    {B['term2_fluctuation']}")
    print(f"  dS_inst/dtau|B:    {B['dS_inst_dtau_B']}")
    print(f"  S_inst|B:          {B['S_inst_B']}")
    gate_B = evaluate_gate(TAU_SCAN, B['dS_inst_dtau_B'], 'B:1-instanton')
    print()

    # --- Cross-check: agreement between A and B ---
    # The two prescriptions should produce the SAME tau_peak if the path-integral
    # picture is consistent.  A genuine PASS requires convergence.
    agree = gate_A['tau_peak'] == gate_B['tau_peak']            # (local)
    print(f"--- CROSS-CHECK A vs B ---")
    print(f"  A tau_peak: {gate_A['tau_peak']:.4f}   verdict {gate_A['verdict']}")
    print(f"  B tau_peak: {gate_B['tau_peak']:.4f}   verdict {gate_B['verdict']}")
    print(f"  A/B tau_peak agreement: {'YES' if agree else 'NO'}")
    print()

    # --- Plots ---
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))

    # Panel 1: prescription A
    ax = axes[0, 0]
    ax.plot(TAU_SCAN, A['dS_inst_dtau_splineA'], 'o-', label='dS_total/dtau (A)')
    ax.axvline(tau_fold, color='r', ls='--', label=f'tau_fold={tau_fold}')
    ax.set_xlabel('tau')
    ax.set_ylabel('dS_inst/dtau (A)')
    ax.set_title('A: direct spectral-action Feynman-Hellmann')
    ax.grid(True); ax.legend()

    # Panel 2: prescription B
    ax = axes[0, 1]
    ax.plot(TAU_SCAN, B['dS_inst_dtau_B'], 's-', color='C2', label='single-inst (B)')
    ax.plot(TAU_SCAN, B['term1_running'], '--', color='C3', alpha=0.6, label='term1 running')
    ax.plot(TAU_SCAN, B['term2_fluctuation'], ':', color='C4', alpha=0.6, label='term2 fluctn')
    ax.axvline(tau_fold, color='r', ls='--')
    ax.set_xlabel('tau')
    ax.set_ylabel('dS_inst/dtau (B)')
    ax.set_title('B: single-instanton 8pi^2/g_eff^2 * kappa')
    ax.grid(True); ax.legend()

    # Panel 3: |dS/dtau| normalized, both
    ax = axes[1, 0]
    absA = np.abs(A['dS_inst_dtau_splineA']); absA /= absA.max()   # (local) normalized
    absB = np.abs(B['dS_inst_dtau_B']); absB /= absB.max()         # (local) normalized
    ax.plot(TAU_SCAN, absA, 'o-', label='|A| normalized')
    ax.plot(TAU_SCAN, absB, 's-', label='|B| normalized')
    ax.axvline(tau_fold, color='r', ls='--', label=f'tau_fold')
    ax.axvspan(tau_fold - 0.02, tau_fold + 0.02, alpha=0.15, color='green', label='PASS window ±0.02')
    ax.set_xlabel('tau')
    ax.set_ylabel('|dS_inst/dtau| / max')
    ax.set_title('Normalized |dS_inst/dtau|')
    ax.grid(True); ax.legend()

    # Panel 4: underlying S_total and Z on broader grid (context)
    ax = axes[1, 1]
    tau_plot = np.linspace(0.05, 0.30, 200)                    # (local) context plot grid
    cs_S = CubicSpline(s42['tau_grid'], s42['S_total'])        # (local)
    cs_Z = CubicSpline(s42['tau_grid'], s42['Z_spec'])         # (local)
    ax.plot(tau_plot, cs_S(tau_plot)/1e5, 'b-', label='S_total/1e5')
    ax.plot(tau_plot, cs_Z(tau_plot)/1e5, 'g--', label='Z=d^2S/dtau^2 /1e5')
    ax.plot(tau_plot, cs_S(tau_plot, 1)/1e5, 'm-.', label='dS_total/dtau /1e5')
    ax.axvline(tau_fold, color='r', ls='--')
    for tv in TAU_SCAN:                                        # (local) scan ticks
        ax.axvline(tv, color='k', alpha=0.2, lw=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('S, Z (scaled)')
    ax.set_title('Context: S_total(tau), Z(tau), dS/dtau')
    ax.grid(True); ax.legend()

    plt.tight_layout()
    plot_path = os.path.join(SCRIPT_DIR, 's80_fold_inst_gradient_feynman.png')  # (local)
    plt.savefig(plot_path, dpi=110)
    plt.close()

    # --- Print tau_peak before verdict (mandated by substitution chain) ---
    print("="*70)
    print(f"  tau_peak(A)    = {gate_A['tau_peak']}")
    print(f"  tau_peak(B)    = {gate_B['tau_peak']}")
    print(f"  tau_fold       = {tau_fold}")
    print("="*70)

    # --- 4-tuple required by plan ---
    # (dS_inst_dtau_peak_value, scheme=path-integral, convention=Euclidean, L_max=5)
    idx_A = int(np.argmax(np.abs(A['dS_inst_dtau_splineA'])))   # (local)
    dS_peak_A = float(A['dS_inst_dtau_splineA'][idx_A])         # (local) peak value (A)
    idx_B = int(np.argmax(np.abs(B['dS_inst_dtau_B'])))         # (local)
    dS_peak_B = float(B['dS_inst_dtau_B'][idx_B])                # (local) peak value (B)

    tuple_A = (dS_peak_A, 'path-integral-A', 'Euclidean', 5)    # (local) 4-tuple A
    tuple_B = (dS_peak_B, 'path-integral-B', 'Euclidean', 5)    # (local) 4-tuple B
    print(f"4-tuple A: {tuple_A}")
    print(f"4-tuple B: {tuple_B}")

    # --- Save ---
    out_path = os.path.join(SCRIPT_DIR, 's80_fold_inst_gradient_feynman.npz')  # (local)
    np.savez(
        out_path,
        # Pre-registered inputs
        tau_scan=TAU_SCAN,
        tau_fold=tau_fold,
        dS_fold=dS_fold, d2S_fold=d2S_fold, Z_fold=Z_fold,
        # S42 source data
        s42_tau_grid=s42['tau_grid'],
        s42_S_total=s42['S_total'],
        s42_dS_dtau=s42['dS_dtau'],
        s42_d2S_dtau2=s42['d2S_dtau2'],
        s42_Z_spec=s42['Z_spec'],
        # Prescription A outputs
        A_dS_inst_dtau=A['dS_inst_dtau_splineA'],
        A_d2S_inst_dtau2=A['d2S_inst_dtau2_splineA'],
        A_dS_inst_dtau_native=A['dS_inst_dtau_nativeA'],
        A_tau_peak=gate_A['tau_peak'],
        A_verdict=gate_A['verdict'],
        A_reason=gate_A['reason'],
        # Prescription B outputs
        B_tau_scan=B['tau_scan'],
        B_g_eff_sq=B['g_eff_sq'],
        B_kappa=B['kappa'],
        B_dkappa_dtau=B['dkappa_dtau'],
        B_term1_running=B['term1_running'],
        B_term2_fluctn=B['term2_fluctuation'],
        B_dS_inst_dtau=B['dS_inst_dtau_B'],
        B_S_inst=B['S_inst_B'],
        B_tau_peak=gate_B['tau_peak'],
        B_verdict=gate_B['verdict'],
        B_reason=gate_B['reason'],
        # Cross-check
        AB_agree_tau_peak=agree,
        # 4-tuples
        tuple_A_peak=dS_peak_A,
        tuple_B_peak=dS_peak_B,
    )
    print(f"\nSaved: {out_path}")
    print(f"Saved: {plot_path}")

    return gate_A, gate_B


if __name__ == '__main__':
    main()
