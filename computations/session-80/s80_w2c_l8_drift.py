#!/usr/bin/env python3
"""
S80-W0-2 (B): drift_u1(L=8) vs CLT 1/√N PREDICTION
======================================================

Gate: S80-W2C-L8-DRIFT (VERIFY trigger)

Pre-registered substitution chain (from session-80-plan.md §W0-2):
  Step 1 (def): drift_u1(L) = |<α_1>^{L} − <α_1>^{exact}| / |<α_1>^{exact}|
                with <α_1>^L = (J_u1^{zeta2}/J_u1^{SDW})(L)
                and <α_1>^{exact} = cross-branch mean at L (R-protection target).
  Step 2 (model): drift^{CLT}(N) = A + B/√N with (A,B)=(0.5, 0.5).
  Step 3 (subst): drift^{CLT}(8) = 0.5 + 0.5/√8 = 0.5 + 0.5/2.8284271... = 0.6768.
  Step 4 (band): pre-reg [0.56, 0.76] (≈ ±15% of 0.6768 rounded).
  Step 5 (verdict): Python computes actual drift_u1(L=8), classifies:
    PASS-CLT      : drift ∈ [0.56, 0.76]  → CLT confirmed, abelian-failure confirmed
                      → Kasparov uses dual-argument track (K-theory + CLT).
    FAIL Sc.1     : drift < 0.40          → R-protection HOLDS at dim H_π = 1
                      → Kasparov uses K-theory only.
    FAIL Sc.2     : drift > 0.80          → stronger-than-CLT residual
                      → need stronger integrability constraint.
    INFO          : drift ∈ [0.40, 0.56] ∪ [0.76, 0.80].

PRU pins:
  (1) SHA-256 content-hash of L=8 eigenvalue list (all sectors).
  (2) SHA-256 content-hash of full import-closure (this script + imports).
  (3) Hankel-formula-order pin = 2^(2ν-3) = 2 (5-pt central FD, ν=2).
  (4) ε-scan pre-registered (h ∈ {1e-4, 1e-5, 1e-6} * M_KK) AT L=8 ONLY.
  (5) Single run per L — no iteration.

PERFORMANCE: D_π is anti-Hermitian. We form H_π(φ) = −D_π(φ)² (positive
  Hermitian, eigenvalues = |λ|²). Use eigvalsh and extract all 3 functionals
  from the same eigenvalue vector. Only the 4 non-zero phi values need a
  re-diagonalization per (sector, branch); phi=0 is cached.

Also produces the L ∈ {4, 5, 6, 7, 8} drift_u1 curve (one run per L_max) for
the CLT-band overlay plot. ε-scan ONLY at headline L=8 to keep runtime tractable.

Substrate framing (from .claude/rules/phononic-framing.md):
  The u1 branch has dim H_π = 1 on the SU(3) fiber (only Cartan direction λ_8).
  R-protection is a Kasparov-class identity: per-branch spectral-moment ratios
  are scheme-invariant because the Mellin transform of a single representation
  block's eigenvalue distribution preserves the block's shape. For dim H_π = 1,
  the within-sector "averaging" across representation states is absent; only a
  per-sector fluctuation survives. The CLT hypothesis is that this leaves a
  residual O(1/√N) drift in the per-branch ratio as a function of the mode-count
  N ≈ N_sec(L_max). The test of the CLT prediction at L=8 (versus L=6) is a
  decisive measurement of abelian-subfactor-lacks-R-protection vs
  R-protection-holds.

Outputs:
  computations/session-80/s80_w2c_l8_drift.py      (this script)
  computations/session-80/s80_w2c_l8_drift.npz     (drift curve + L=8 headline)
  computations/session-80/s80_w2c_l8_drift.png     (curve with CLT-band overlay)
  Append verdict line to computations/session-80/s80_gate_verdicts.txt

Session: S80 W0-2 (B). Author: landau-condensed-matter-theorist.
"""

import os
# Cap CPU threads BEFORE numpy import (safety net if GPU path fails)
os.environ.setdefault('OMP_NUM_THREADS', '8')                         # (local)
os.environ.setdefault('MKL_NUM_THREADS', '8')                         # (local)

import sys
import time
import hashlib
import math
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# GPU path via torch.linalg.eigvalsh on AMD RX 9070 XT (17.1 GB VRAM)
import torch
_USE_GPU = torch.cuda.is_available()                                  # (local)
_GPU_DEVICE = torch.device('cuda') if _USE_GPU else torch.device('cpu')   # (local)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

from canonical_constants import (
    M_KK, tau_fold, PI,
    J_C2, J_su2, J_u1,
    omega_L1, omega_L2,
)

from dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    build_cliff8,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    dirac_operator_on_irrep,
    get_irrep,
)

from spectral_action import dim_su3_irrep

# ===========================================================================
# PRU PINS: IMPORT-CLOSURE SHA-256 HASH
# ===========================================================================
IMPORT_CLOSURE_FILES = [                                              # (local)
    "s80_w2c_l8_drift.py",
    "canonical_constants.py",
    "dirac_spectrum.py",
    "spectral_action.py",
]

def sha256_of_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()

def sha256_of_array(arr):
    a = np.ascontiguousarray(np.asarray(arr, dtype=np.float64))
    return hashlib.sha256(a.tobytes()).hexdigest()

def eigvalsh_gpu(Hsq):
    """GPU-accelerated eigvalsh for Hermitian complex matrix, fallback to numpy on small sizes.
    Substitution chain:
      Step 1: Hsq built via 0.5*(H + H^H) -> Hermitian by construction.
      Step 2: torch.linalg.eigvalsh -> real eigenvalues, ascending.
      Step 3: .cpu().numpy() -> float64.
      Step 4: Validated vs np.linalg.eigvalsh: 5.684e-14 max abs err at N=100.
    """
    if not _USE_GPU or Hsq.shape[0] < 100:
        return np.linalg.eigvalsh(Hsq)                                # (local)
    t = torch.tensor(Hsq, device=_GPU_DEVICE, dtype=torch.complex128)
    ev = torch.linalg.eigvalsh(t).cpu().numpy()                       # (local)
    return ev

import_hashes = {f: sha256_of_file(os.path.join(SCRIPT_DIR, f)) for f in IMPORT_CLOSURE_FILES}    # (local)
closure_concat = "".join(sorted(import_hashes.values())).encode()                                  # (local)
IMPORT_CLOSURE_SHA = hashlib.sha256(closure_concat).hexdigest()                                    # (local)

# ===========================================================================
# CONFIGURATION — PRU pinned
# ===========================================================================
TAU = tau_fold                                                  # (local) 0.190
L_LIST = [4, 5, 6, 7, 8]                                        # (local) scan for CLT curve
HEADLINE_L = 8                                                  # (local) L for verdict
PHI_J_AMPLITUDE = 1.0e-4                                        # (local) dimensionless (M_KK units)
STENCIL_STEPS = np.array([1.0e-4, 1.0e-5, 1.0e-6])              # (local) ε-scan pre-reg
PRIMARY_STEP = 1.0e-5                                           # (local) pinned stencil step
HANKEL_ORDER_PIN = 2                                            # (local) 2^(2ν-3), ν=2

# Pre-registered CLT prediction (VERIFY trigger)
CLT_A = 0.5                                                     # (local) intercept from P4-B abelian-subfactor hypothesis
CLT_B = 0.5                                                     # (local) slope in 1/√N
CLT_AT_L8 = CLT_A + CLT_B / math.sqrt(HEADLINE_L)               # (local) 0.6767766952966369
BAND_LO = 0.56                                                  # (local) pre-reg lower
BAND_HI = 0.76                                                  # (local) pre-reg upper
FAIL_SC1_THRESHOLD = 0.40                                       # (local) below = R holds
FAIL_SC2_THRESHOLD = 0.80                                       # (local) above = stronger-than-CLT

BRANCH_SU2 = [0, 1, 2]                                          # (local)
BRANCH_U1 = [7]                                                 # (local) λ_8 — abelian dim H_π = 1
BRANCH_C2 = [3, 4, 5, 6]                                        # (local)
BRANCHES = {"su2": BRANCH_SU2, "u1": BRANCH_U1, "C2": BRANCH_C2}

# 4-tuple tag components
SCHEME_TAG = "zeta2_over_SDW"                                   # (local)
CONVENTION_TAG = "Phi_J=1e-4*M_KK, 5pt central FD, step=1e-5*M_KK, Hankel-order=2^(2nu-3)=2"  # (local)

print("=" * 78, flush=True)
print(f"S80-W0-2 (B) drift_u1(L={HEADLINE_L}) vs CLT 1/√N", flush=True)
print("=" * 78, flush=True)
print(f"  Compute backend: {'GPU (torch.linalg.eigvalsh on ' + torch.cuda.get_device_name(0) + ')' if _USE_GPU else 'CPU (numpy.linalg.eigvalsh, 8 threads)'}", flush=True)
print(f"""
  Pre-registered substitution chain:
    Step 1: drift_u1(L) = |<α_1>^L − <α_1>^exact| / |<α_1>^exact|
    Step 2: drift^CLT(N) = {CLT_A} + {CLT_B}/√N
    Step 3: drift^CLT({HEADLINE_L}) = {CLT_A} + {CLT_B}/√{HEADLINE_L}
                          = {CLT_A} + {CLT_B/math.sqrt(HEADLINE_L):.16f}
                          = {CLT_AT_L8:.16f}
    Step 4: pre-reg band = [{BAND_LO}, {BAND_HI}]  (±15% of {CLT_AT_L8:.4f})
    Step 5: Python-computed drift_u1({HEADLINE_L}) below → classify.

  Verdict thresholds:
    PASS-CLT   : drift ∈ [{BAND_LO}, {BAND_HI}]
    FAIL Sc.1  : drift < {FAIL_SC1_THRESHOLD}
    FAIL Sc.2  : drift > {FAIL_SC2_THRESHOLD}
    INFO       : otherwise

  PRU pins:
    Import-closure SHA-256  = {IMPORT_CLOSURE_SHA}
    Hankel order pin        = 2^(2ν-3) = 2
    Single-run discipline   = True (one run per L_max)

  Scan range: L_max ∈ {L_LIST} (for CLT-curve overlay; ε-scan ONLY at L=8)
""", flush=True)

# ===========================================================================
# STEP 1: BUILD SHARED INFRASTRUCTURE (frame, connection, clifford)
# ===========================================================================
t0 = time.time()                                                  # (local)
gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()
B_ab = compute_killing_form(f_abc)
g_s = jensen_metric(B_ab, TAU)
E_frame = orthonormal_frame(g_s)
ft = frame_structure_constants(f_abc, E_frame)
Gamma_conn = connection_coefficients(ft)
Omega = spinor_connection_offset(Gamma_conn, gammas)
print(f"  Frame/connection built in {time.time()-t0:.2f}s", flush=True)

# ===========================================================================
# HELPERS
# ===========================================================================
def build_G_i(rho_list, branch):
    dim_rho = rho_list[0].shape[0]
    dim_spin = 16  # (local)
    G = np.zeros((dim_rho * dim_spin, dim_rho * dim_spin), dtype=complex)
    for a in branch:
        G += np.kron(rho_list[a], gammas[a])
    return G

def spectral_moments_from_eigsq(eigs_sq):
    eigs_sq = np.clip(eigs_sq, 0.0, None)
    mask = eigs_sq > 1e-24
    e2 = eigs_sq[mask]
    abs_lam = np.sqrt(e2)
    return {
        "SDW": float(np.sum(abs_lam)),
        "zeta2": float(np.sum(1.0 / e2)),
        "zeta4": float(np.sum(1.0 / (e2 * e2))),
    }

def eigsq_of(D_matrix):
    Hsq = -(D_matrix @ D_matrix)
    Hsq = 0.5 * (Hsq + Hsq.conj().T)
    return eigvalsh_gpu(Hsq)

def stencil_5pt(v_m2, v_m1, v_0, v_p1, v_p2, h):
    return (-v_m2 + 16.0 * v_m1 - 30.0 * v_0 + 16.0 * v_p1 - v_p2) / (12.0 * h ** 2)

def build_sectors(L_max):
    """Return list of sector dicts with D_pi, rho, G_i per branch, cached phi=0 eigs_sq."""
    irreps = [(0, 0)]
    for p in range(L_max + 1):
        for q in range(L_max + 1 - p):
            if p == 0 and q == 0:
                continue
            irreps.append((p, q))

    data = []                                                     # (local)
    all_evals = []                                                # (local)
    for (p, q) in irreps:
        d_pq = dim_su3_irrep(p, q)
        if p == 0 and q == 0:
            D_pi = Omega.copy()
            rho_list = [np.zeros((1, 1), dtype=complex) for _ in range(8)]
        else:
            rho_list, dc = get_irrep(p, q, gens, f_abc)
            assert dc == d_pq
            D_pi = dirac_operator_on_irrep(rho_list, E_frame, gammas, Omega)
        eigs_sq_0 = eigsq_of(D_pi)
        abs_lam = np.sqrt(np.clip(eigs_sq_0, 0.0, None))
        all_evals.extend(np.sort(abs_lam).tolist())
        G_map = {bn: build_G_i(rho_list, bd) for bn, bd in BRANCHES.items()}
        data.append({"pq": (p, q), "dim": d_pq, "D": D_pi, "G": G_map, "eigs_sq_0": eigs_sq_0})
    return data, np.sort(np.array(all_evals))

def compute_J_block(sectors, branch_name, h):
    """For one branch, one h: compute J^{SDW}, J^{zeta2}, J^{zeta4} by 5-pt FD stencil."""
    J_sums = {"SDW": 0.0, "zeta2": 0.0, "zeta4": 0.0}
    phi_vals = (-2 * h, -h, 0.0, h, 2 * h)

    for sec in sectors:
        D0 = sec["D"]
        G = sec["G"][branch_name]
        d_pq = sec["dim"]

        trf = {"SDW": np.zeros(5), "zeta2": np.zeros(5), "zeta4": np.zeros(5)}

        # phi=0 cached
        m_cached = spectral_moments_from_eigsq(sec["eigs_sq_0"])
        for fn in ("SDW", "zeta2", "zeta4"):
            trf[fn][2] = m_cached[fn]

        # phi != 0: diagonalize, extract all 3 functionals at once
        for k, phi in enumerate(phi_vals):
            if k == 2:
                continue
            D_phi = D0 + phi * G
            eigs_sq = eigsq_of(D_phi)
            m = spectral_moments_from_eigsq(eigs_sq)
            for fn in ("SDW", "zeta2", "zeta4"):
                trf[fn][k] = m[fn]

        for fn in ("SDW", "zeta2", "zeta4"):
            d2S = stencil_5pt(trf[fn][0], trf[fn][1], trf[fn][2], trf[fn][3], trf[fn][4], h)
            J_sums[fn] += d_pq * d2S

    return J_sums

def drift_u1_at_L(L_max, primary_step, compute_eps_scan=False):
    """Return dict with drift_u1 + per-branch J at given L_max. Single primary run."""
    t_local = time.time()                                         # (local)
    sectors, sorted_abs_evals = build_sectors(L_max)
    N_sec_count = len(sectors)                                    # (local)
    N_eig_total = len(sorted_abs_evals)                           # (local)

    eig_sha = sha256_of_array(sorted_abs_evals)                   # (local)

    J = {bn: compute_J_block(sectors, bn, primary_step) for bn in BRANCHES}      # (local)

    alpha1 = {b: J[b]["zeta2"] / J[b]["SDW"] for b in BRANCHES}   # (local)
    alpha1_exact = float(np.mean(list(alpha1.values())))          # (local)
    drift_all = {b: abs(alpha1[b] - alpha1_exact) / abs(alpha1_exact) for b in BRANCHES}  # (local)

    eps_scan = None                                               # (local)
    if compute_eps_scan:
        eps_scan = {}
        for bn in BRANCHES:
            eps_scan[bn] = {fn: np.zeros(len(STENCIL_STEPS)) for fn in ("SDW", "zeta2", "zeta4")}
            for k, h in enumerate(STENCIL_STEPS):
                if abs(h - primary_step) < 1e-20:
                    for fn in ("SDW", "zeta2", "zeta4"):
                        eps_scan[bn][fn][k] = J[bn][fn]
                else:
                    Jh = compute_J_block(sectors, bn, h)
                    for fn in ("SDW", "zeta2", "zeta4"):
                        eps_scan[bn][fn][k] = Jh[fn]

    dt = time.time() - t_local                                    # (local)
    print(f"    L={L_max}: N_sec={N_sec_count}, N_eig={N_eig_total}, "
          f"drift_u1={drift_all['u1']:.4%}  [{dt:.1f}s]  eig_sha={eig_sha[:16]}", flush=True)

    return {
        "L": L_max,
        "N_sec": N_sec_count,
        "N_eig_total": N_eig_total,
        "J": J,
        "alpha1": alpha1,
        "alpha1_exact": alpha1_exact,
        "drift": drift_all,
        "drift_u1": drift_all["u1"],
        "eig_sha": eig_sha,
        "eps_scan": eps_scan,
    }

# ===========================================================================
# STEP 2: SCAN L_max ∈ {4, 5, 6, 7, 8}, HEADLINE AT L=8 WITH ε-SCAN
# ===========================================================================
print("\n" + "=" * 78, flush=True)
print("STEP 2: Per-L drift_u1 scan (single run per L_max)", flush=True)
print("=" * 78, flush=True)

results_by_L = {}                                                 # (local)
for L in L_LIST:
    is_headline = (L == HEADLINE_L)
    print(f"\n  Building L={L} infrastructure and computing J...", flush=True)
    results_by_L[L] = drift_u1_at_L(L, PRIMARY_STEP, compute_eps_scan=is_headline)

headline = results_by_L[HEADLINE_L]                               # (local)
drift_u1_L8 = headline["drift_u1"]                                # (local) headline VERIFY quantity
EIGENVALUE_LIST_SHA_L8 = headline["eig_sha"]                      # (local)

# ===========================================================================
# STEP 3: CLT PREDICTION CURVE + ε-SCAN AT L=8
# ===========================================================================
print("\n" + "=" * 78, flush=True)
print("STEP 3: CLT prediction curve and ε-scan diagnostic at L=8", flush=True)
print("=" * 78, flush=True)

clt_curve = {L: CLT_A + CLT_B / math.sqrt(L) for L in L_LIST}     # (local)
print("\n  CLT model drift^CLT(N) = 0.5 + 0.5/√N:", flush=True)
for L in L_LIST:
    obs = results_by_L[L]['drift_u1']
    print(f"    L={L}: CLT={clt_curve[L]:.4f}, observed drift_u1={obs:.4%}, "
          f"obs/CLT={obs/clt_curve[L]:.3f}", flush=True)

# ε-scan diagnostic at L=8
eps_L8 = headline["eps_scan"]                                     # (local)
stencil_converged = True                                          # (local)
print(f"\n  ε-scan at L=8 (h ∈ {STENCIL_STEPS.tolist()} dimensionless M_KK units):", flush=True)
print(f"  {'Branch':<6} {'Func':<6} {'J(1e-4)':>14} {'J(1e-5)':>14} {'J(1e-6)':>14} {'rel spread':>12}", flush=True)
for bn in BRANCHES:
    for fn in ("SDW", "zeta2", "zeta4"):
        vals = eps_L8[bn][fn]
        mean_abs = np.mean(np.abs(vals))
        spread = (np.max(vals) - np.min(vals)) / mean_abs if mean_abs > 0 else 0.0        # (local)
        if abs(spread) > 0.10:
            stencil_converged = False
        flag = "" if abs(spread) < 0.05 else "!"                                           # (local)
        print(f"  {bn:<6} {fn:<6} {vals[0]:>14.4e} {vals[1]:>14.4e} {vals[2]:>14.4e} {spread:>11.2%}{flag}", flush=True)
print(f"\n  Stencil-converged at L=8: {stencil_converged}", flush=True)

# ===========================================================================
# STEP 4: VERDICT CLASSIFICATION (pre-registered thresholds)
# ===========================================================================
print("\n" + "=" * 78, flush=True)
print("STEP 4: Gate verdict — S80-W2C-L8-DRIFT", flush=True)
print("=" * 78, flush=True)

print(f"\n  Substitution chain re-verified:", flush=True)
print(f"    drift^CLT({HEADLINE_L}) = {CLT_A} + {CLT_B}/√{HEADLINE_L} = {CLT_AT_L8:.10f}", flush=True)
print(f"    Pre-reg band           = [{BAND_LO}, {BAND_HI}]", flush=True)
print(f"    Computed drift_u1(L=8) = {drift_u1_L8:.6f} = {drift_u1_L8:.4%}", flush=True)

if BAND_LO <= drift_u1_L8 <= BAND_HI:
    verdict = "PASS-CLT"                                          # (local)
    reason = (f"drift_u1(L=8)={drift_u1_L8:.4%} ∈ [{BAND_LO:.2%}, {BAND_HI:.2%}]  "
              f"→ CLT 1/√N confirmed; abelian-subfactor-lacks-Level-2-R-protection "
              f"CONFIRMED; Kasparov proof uses dual-argument track.")       # (local)
elif drift_u1_L8 < FAIL_SC1_THRESHOLD:
    verdict = "FAIL-Sc1"                                          # (local)
    reason = (f"drift_u1(L=8)={drift_u1_L8:.4%} < {FAIL_SC1_THRESHOLD:.2%}  "
              f"→ R-protection HOLDS at dim H_π=1 contrary to P4-B; "
              f"Kasparov proof must use pure K-theory track.")             # (local)
elif drift_u1_L8 > FAIL_SC2_THRESHOLD:
    verdict = "FAIL-Sc2"                                          # (local)
    reason = (f"drift_u1(L=8)={drift_u1_L8:.4%} > {FAIL_SC2_THRESHOLD:.2%}  "
              f"→ stronger-than-CLT abelian-failure; "
              f"Kasparov proof needs stronger integrability constraint.")  # (local)
else:
    verdict = "INFO"                                              # (local)
    reason = (f"drift_u1(L=8)={drift_u1_L8:.4%} ∈ borderline band "
              f"[{FAIL_SC1_THRESHOLD:.2%}, {BAND_LO:.2%}] ∪ "
              f"[{BAND_HI:.2%}, {FAIL_SC2_THRESHOLD:.2%}]; inconclusive.")  # (local)

print(f"\n  VERDICT: {verdict}", flush=True)
print(f"  reason : {reason}", flush=True)

# ===========================================================================
# STEP 5: PLOT — drift_u1 vs L with CLT band overlay
# ===========================================================================
print("\n" + "=" * 78, flush=True)
print("STEP 5: Plot drift_u1 vs L with CLT band", flush=True)
print("=" * 78, flush=True)

fig, axs = plt.subplots(1, 2, figsize=(14, 5.5))
fig.suptitle("S80-W2C-L8-DRIFT: drift_u1 vs L with CLT 1/√N overlay", fontsize=13)

ax = axs[0]
Ls_arr = np.array(L_LIST)
drifts_u1 = np.array([results_by_L[L]["drift_u1"] for L in L_LIST])
drifts_c2 = np.array([results_by_L[L]["drift"]["C2"] for L in L_LIST])
drifts_su2 = np.array([results_by_L[L]["drift"]["su2"] for L in L_LIST])
clt_vals = np.array([clt_curve[L] for L in L_LIST])

ax.plot(Ls_arr, drifts_u1, "o-", color="tab:green", label="u1 (observed)", lw=2, ms=8)
ax.plot(Ls_arr, drifts_c2, "s-", color="tab:blue", label="C2 (observed)", ms=6, alpha=0.7)
ax.plot(Ls_arr, drifts_su2, "^-", color="tab:orange", label="su2 (observed)", ms=6, alpha=0.7)
ax.plot(Ls_arr, clt_vals, "k--", label="CLT: 0.5 + 0.5/√N", lw=1.5)
ax.fill_between([HEADLINE_L - 0.2, HEADLINE_L + 0.2], BAND_LO, BAND_HI,
                alpha=0.3, color="green", label=f"L=8 pre-reg band [{BAND_LO}, {BAND_HI}]")  # (local)
ax.scatter([HEADLINE_L], [drift_u1_L8], color="red", s=120, zorder=10, marker="*",
           label=f"headline drift_u1(8) = {drift_u1_L8:.3f}")
ax.set_xlabel("L_max")
ax.set_ylabel("drift_b = |<α_1>^L − <α_1>^exact| / |<α_1>^exact|")
ax.set_title("Per-branch drift vs L with CLT model")
ax.legend(fontsize=8, loc="best")
ax.grid(alpha=0.3)

ax = axs[1]
ax.axhspan(0, FAIL_SC1_THRESHOLD, alpha=0.15, color="red", label=f"FAIL Sc.1 (<{FAIL_SC1_THRESHOLD})")
ax.axhspan(FAIL_SC1_THRESHOLD, BAND_LO, alpha=0.15, color="yellow", label="INFO")
ax.axhspan(BAND_LO, BAND_HI, alpha=0.20, color="green", label=f"PASS-CLT [{BAND_LO}, {BAND_HI}]")
ax.axhspan(BAND_HI, FAIL_SC2_THRESHOLD, alpha=0.15, color="yellow")
ax.axhspan(FAIL_SC2_THRESHOLD, 1.0, alpha=0.15, color="red", label=f"FAIL Sc.2 (>{FAIL_SC2_THRESHOLD})")
ax.plot(Ls_arr, drifts_u1, "o-", color="tab:green", label="u1 observed", lw=2, ms=8)
ax.plot(Ls_arr, clt_vals, "k--", label="CLT model", lw=1.5)
ax.scatter([6], [0.8375], marker="x", color="gray", s=80, label="S78 ref drift_u1(6) = 0.8375")
ax.scatter([HEADLINE_L], [drift_u1_L8], color="red", s=150, zorder=10, marker="*",
           label=f"drift_u1(8)={drift_u1_L8:.3f}  [{verdict}]")
ax.set_xlabel("L_max")
ax.set_ylabel("drift_u1")
ax.set_title(f"drift_u1 vs L with verdict bands — VERDICT: {verdict}")
ax.set_ylim(0, 1.0)
ax.legend(fontsize=7, loc="upper right")
ax.grid(alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, "s80_w2c_l8_drift.png")
plt.savefig(plot_path, dpi=120)
print(f"  Plot saved: {plot_path}", flush=True)

# ===========================================================================
# STEP 6: SAVE NPZ
# ===========================================================================
npz_path = os.path.join(SCRIPT_DIR, "s80_w2c_l8_drift.npz")
save_dict = dict(
    L_list=np.array(L_LIST, dtype=np.int64),
    drift_u1_vs_L=np.array([results_by_L[L]["drift_u1"] for L in L_LIST]),
    drift_C2_vs_L=np.array([results_by_L[L]["drift"]["C2"] for L in L_LIST]),
    drift_su2_vs_L=np.array([results_by_L[L]["drift"]["su2"] for L in L_LIST]),
    alpha1_u1_vs_L=np.array([results_by_L[L]["alpha1"]["u1"] for L in L_LIST]),
    alpha1_C2_vs_L=np.array([results_by_L[L]["alpha1"]["C2"] for L in L_LIST]),
    alpha1_su2_vs_L=np.array([results_by_L[L]["alpha1"]["su2"] for L in L_LIST]),
    alpha1_exact_vs_L=np.array([results_by_L[L]["alpha1_exact"] for L in L_LIST]),
    N_sec_vs_L=np.array([results_by_L[L]["N_sec"] for L in L_LIST]),
    N_eig_vs_L=np.array([results_by_L[L]["N_eig_total"] for L in L_LIST]),
    eig_sha_vs_L=np.array([results_by_L[L]["eig_sha"] for L in L_LIST]),
    clt_A=np.float64(CLT_A),
    clt_B=np.float64(CLT_B),
    clt_curve=np.array([clt_curve[L] for L in L_LIST]),
    headline_L=np.int64(HEADLINE_L),
    drift_u1_L8=np.float64(drift_u1_L8),
    clt_at_L8=np.float64(CLT_AT_L8),
    band_lo=np.float64(BAND_LO),
    band_hi=np.float64(BAND_HI),
    fail_sc1_threshold=np.float64(FAIL_SC1_THRESHOLD),
    fail_sc2_threshold=np.float64(FAIL_SC2_THRESHOLD),
    verdict=np.array(verdict),
    reason=np.array(reason),
    import_closure_sha256=np.array(IMPORT_CLOSURE_SHA),
    eigenvalue_list_sha256_L8=np.array(EIGENVALUE_LIST_SHA_L8),
    hankel_order_pin=np.int64(HANKEL_ORDER_PIN),
    tau_fold_used=np.float64(TAU),
    phi_J_amp=np.float64(PHI_J_AMPLITUDE),
    primary_step=np.float64(PRIMARY_STEP),
    stencil_steps=STENCIL_STEPS,
    J_scan_u1_zeta2_L8=eps_L8["u1"]["zeta2"],
    J_scan_u1_SDW_L8=eps_L8["u1"]["SDW"],
    J_scan_C2_zeta2_L8=eps_L8["C2"]["zeta2"],
    J_scan_C2_SDW_L8=eps_L8["C2"]["SDW"],
    J_scan_su2_zeta2_L8=eps_L8["su2"]["zeta2"],
    J_scan_su2_SDW_L8=eps_L8["su2"]["SDW"],
    stencil_converged_L8=np.bool_(stencil_converged),
    scheme_tag=np.array(SCHEME_TAG),
    convention_tag=np.array(CONVENTION_TAG),
    L_max_tag=np.int64(HEADLINE_L),
    s78_drift_u1_reference=np.float64(0.8375),
)
np.savez(npz_path, **save_dict)
print(f"\n  NPZ saved: {npz_path}", flush=True)

# ===========================================================================
# STEP 7: APPEND VERDICT LINE
# ===========================================================================
verdict_path = os.path.join(SCRIPT_DIR, "s80_gate_verdicts.txt")
drift_str = ",".join(f"L{L}:{results_by_L[L]['drift_u1']:.4f}" for L in L_LIST)
verdict_line = (
    f"S80-W2C-L8-DRIFT: {verdict} -- "
    f"drift_u1(L=8)={drift_u1_L8:.4%} vs CLT({CLT_AT_L8:.4f}) band [{BAND_LO},{BAND_HI}], "
    f"scan=[{drift_str}], "
    f"(value={drift_u1_L8:.6f},scheme={SCHEME_TAG},conv={CONVENTION_TAG!r},L_max={HEADLINE_L}), "
    f"import_closure_sha256={IMPORT_CLOSURE_SHA[:16]}, "
    f"eigenvalue_sha256_L8={EIGENVALUE_LIST_SHA_L8[:16]}, "
    f"hankel_order=2^(2nu-3)=2"
)
with open(verdict_path, "a") as fh:
    fh.write(verdict_line + "\n")
print(f"  Verdict appended: {verdict_path}", flush=True)
print(f"    {verdict_line}", flush=True)

print("\n" + "=" * 78, flush=True)
print(f"DONE. Verdict: {verdict}  |  drift_u1(L=8) = {drift_u1_L8:.4%}", flush=True)
print("=" * 78, flush=True)
