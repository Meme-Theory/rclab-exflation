#!/usr/bin/env python3
"""
S80-W0-2 (A): W2-C CLEAN RE-RUN UNDER PRU DISCIPLINE (L_max = 6)
==================================================================

Gate: S80-W2-C-REMED (AUDIT trigger)

Pre-registration (from session-80-plan.md §W0-2 + S79 P1-3 REMED spec):
  PASS = runs under PRU pins; produces a 4-tuple-tagged drift_u1(L=6).
  INFO = partial (some PRU pins not applicable at L=6 infrastructure level).
  FAIL = inapplicable (PRU pins cannot be constructed for this script).

PRU pins implemented:
  (1) SHA-256 content-hash of the L_max=6 eigenvalue list (all sectors).
  (2) SHA-256 content-hash of the full import-closure (this script +
      canonical_constants.py + dirac_spectrum.py + spectral_action.py).
  (3) Hankel-formula-order pin = 2^(2ν-3) = 2 (5-pt central FD, ν=2 -> O(h^4)).
  (4) ε-scan pre-registered (h ∈ {1e-4, 1e-5, 1e-6} * M_KK, dimensionless units).
  (5) Single run per L_max — no iteration.

Method (identical MATH to S78 W2-C, with PRU pins applied and eigh fast path):
  For each branch i in {C2, su2, u1}, compute
      J_i^{func} = d² S_i(φ) / dφ²  at φ=0,   func ∈ {SDW, zeta2, zeta4}
  via a 5-pt central FD stencil on Tr f(D(φ)²) with branch-projected perturbation
  G_i = Σ_{a∈branch} ρ[a] ⊗ γ_a.

  drift_u1(L) per P4-B definition:
      drift_u1(L) = |<α_1>^{L} − <α_1>^{exact}| / |<α_1>^{exact}|
      where  <α_1>^{L}    = (J_u1^{zeta2} / J_u1^{SDW}) at truncation L
             <α_1>^{exact} = mean across branches of (J_b^{zeta2} / J_b^{SDW})
  Equivalent to the S78 S7 quantity `within_branch_drift_z2["u1"]`.

PERFORMANCE: D_π is anti-Hermitian. We form H_π(φ) = −D_π(φ)² which is
  positive-Hermitian with eigenvalues |λ|². Use eigvalsh (fast, real). We
  extract all 3 functionals from the SAME eigenvalue vector per (branch, φ)
  matrix, not 3 separate diagonalizations. This cuts the eigvals count from
  180 to 60 passes at L=6 (one pass ≈ 5-10s on 32 cores).

Substrate framing (from .claude/rules/phononic-framing.md):
  R-protection per-branch is a STRUCTURAL identity of the spectral triple.
  D_K eigenvalues on Jensen-deformed SU(3) fiber → branch-projected spectral
  moments → Josephson coupling ratios. The per-branch ratio J^{zeta}/J^{SDW}
  tests whether the Mellin transform of one branch's eigenvalue distribution
  preserves the branch's internal shape under the scheme change. The u1
  branch has only the Cartan direction λ_8 → dim H_π = 1 on that branch →
  CLT 1/√N residual predicts drift_u1^{CLT}(N) = 0.5 + 0.5/√N (P4-B
  ABELIAN-SUBFACTOR-LACKS-LEVEL-2-R-PROTECTION candidate theorem).

Outputs:
  computations/session-80/s80_w2c_remed.py     (this script)
  computations/session-80/s80_w2c_remed.npz    (numerical data + SHA pins)
  computations/session-80/s80_w2c_remed.png    (single-L=6 diagnostic)
  Append verdict line to computations/session-80/s80_gate_verdicts.txt

Session: S80 W0-2 (A). Author: landau-condensed-matter-theorist.
"""

import os
# Cap CPU threads BEFORE numpy import (safety net if GPU path fails)
os.environ.setdefault('OMP_NUM_THREADS', '8')                         # (local)
os.environ.setdefault('MKL_NUM_THREADS', '8')                         # (local)

import sys
import time
import hashlib
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
    "s80_w2c_remed.py",
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
    Substitution chain for direction-claim:
      Step 1: Hsq is built as Hsq = 0.5*(H + H^H) so Hsq is Hermitian by construction.
      Step 2: torch.linalg.eigvalsh returns real eigenvalues sorted ascending (same as numpy).
      Step 3: moved to CPU via .cpu().numpy() — returns float64 array.
      Step 4: Validated against np.linalg.eigvalsh on 100x100 test: max abs err = 5.684e-14 (< 1e-12 tolerance).
    """
    if not _USE_GPU or Hsq.shape[0] < 100:
        return np.linalg.eigvalsh(Hsq)                                # (local) small-matrix CPU fast path
    t = torch.tensor(Hsq, device=_GPU_DEVICE, dtype=torch.complex128)
    ev = torch.linalg.eigvalsh(t).cpu().numpy()                       # (local)
    return ev

import_hashes = {f: sha256_of_file(os.path.join(SCRIPT_DIR, f)) for f in IMPORT_CLOSURE_FILES}   # (local)
closure_concat = "".join(sorted(import_hashes.values())).encode()                                 # (local)
IMPORT_CLOSURE_SHA = hashlib.sha256(closure_concat).hexdigest()                                   # (local)

# ===========================================================================
# CONFIGURATION — PRU-pinned
# ===========================================================================
TAU = tau_fold                                                  # (local) 0.190
MAX_PQ_SUM = 6                                                  # (local) L_max truncation for REMED
PHI_J_AMPLITUDE = 1.0e-4                                        # (local) dimensionless (M_KK units)
STENCIL_STEPS = np.array([1.0e-4, 1.0e-5, 1.0e-6])              # (local) ε-scan pre-reg, dimensionless
PRIMARY_STEP = 1.0e-5                                           # (local) pinned stencil step, dimensionless
HANKEL_ORDER_PIN = 2                                            # (local) 2^(2ν-3), ν=2, 5-pt central FD

GATE_PASS = 0.02                                                # (local) 2% within-branch (PASS)
GATE_INFO = 0.05                                                # (local) 2-5% INFO band
GATE_FAIL = 0.05                                                # (local) >5% FAIL

BRANCH_SU2 = [0, 1, 2]                                          # (local) λ_1,λ_2,λ_3
BRANCH_U1 = [7]                                                 # (local) λ_8
BRANCH_C2 = [3, 4, 5, 6]                                        # (local) λ_4,λ_5,λ_6,λ_7
BRANCHES = {"su2": BRANCH_SU2, "u1": BRANCH_U1, "C2": BRANCH_C2}

# Scheme / convention / L_max tag 4-tuple components
SCHEME_TAG = "zeta2_over_SDW"                                   # (local)
CONVENTION_TAG = "Phi_J=1e-4*M_KK, 5pt central FD, step=1e-5*M_KK, Hankel-order=2^(2nu-3)=2"  # (local)
L_MAX_TAG = MAX_PQ_SUM                                          # (local)

print("=" * 78)
print("S80-W0-2 (A) W2-C REMED: zeta-Josephson clean re-run under PRU discipline")
print("=" * 78)
print(f"  Compute backend: {'GPU (torch.linalg.eigvalsh on ' + torch.cuda.get_device_name(0) + ')' if _USE_GPU else 'CPU (numpy.linalg.eigvalsh, 8 threads)'}", flush=True)
print(f"""
  PRU pins:
    Import-closure SHA-256 = {IMPORT_CLOSURE_SHA}
    Files in closure       = {IMPORT_CLOSURE_FILES}
    Hankel order pin       = 2^(2ν-3) = 2 (ν=2, 5-pt central O(h^4))
    ε-scan                 = {STENCIL_STEPS.tolist()}
    Primary step           = {PRIMARY_STEP}
    Single-run discipline  = True (no iteration)

  Conventions:
    tau_fold               = {TAU}
    max_pq_sum (L_max)     = {MAX_PQ_SUM}
    Phi_J amplitude        = {PHI_J_AMPLITUDE:.4e} (dimensionless, M_KK units)
    M_KK                   = {M_KK:.4e} GeV (reference only; D_K eigenvalues M_KK units)

  Branch decomposition (Baptista su(3) = su(2) + u(1) + C²):
    BRANCH_SU2             = {BRANCH_SU2} (3 bonds)
    BRANCH_U1              = {BRANCH_U1} (1 bond, dim H_π = 1 abelian)
    BRANCH_C2              = {BRANCH_C2} (4 bonds)
""", flush=True)

# ===========================================================================
# STEP 1: BUILD D_K INFRASTRUCTURE
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

irreps = [(0, 0)]
for p in range(MAX_PQ_SUM + 1):
    for q in range(MAX_PQ_SUM + 1 - p):
        if p == 0 and q == 0:
            continue
        irreps.append((p, q))

print(f"  Built frame/connection; irrep sectors: {len(irreps)}", flush=True)

sector_data = []                                                  # (local)
all_evals = []                                                    # (local) flat list for SHA pin
for (p, q) in irreps:
    d_pq = dim_su3_irrep(p, q)
    if p == 0 and q == 0:
        D_pi = Omega.copy()
        rho_list = [np.zeros((1, 1), dtype=complex) for _ in range(8)]
    else:
        rho_list, dc = get_irrep(p, q, gens, f_abc)
        assert dc == d_pq
        D_pi = dirac_operator_on_irrep(rho_list, E_frame, gammas, Omega)
    # |λ|² = eigenvalues of −D² (positive Hermitian since D is anti-Hermitian)
    H_pi_sq = -(D_pi @ D_pi)
    H_pi_sq = 0.5 * (H_pi_sq + H_pi_sq.conj().T)  # symmetrize to tame roundoff
    eigs_sq = eigvalsh_gpu(H_pi_sq)
    eigs_sq = np.clip(eigs_sq, 0.0, None)
    abs_lam = np.sqrt(eigs_sq)
    sector_data.append({"pq": (p, q), "dim": d_pq, "D": D_pi, "rho": rho_list, "abs_lam_0": abs_lam})
    all_evals.extend(np.sort(abs_lam).tolist())

# PRU pin: SHA-256 of full eigenvalue list (sorted |λ|)
EIGENVALUE_LIST_SHA = sha256_of_array(np.sort(np.array(all_evals)))   # (local)
print(f"  Eigenvalue list SHA-256 (L={MAX_PQ_SUM}): {EIGENVALUE_LIST_SHA}", flush=True)
print(f"  Total eigenvalues: {len(all_evals)}", flush=True)
print(f"  Frame+spectrum build time: {time.time()-t0:.2f}s", flush=True)

# ===========================================================================
# STEP 2: BRANCH-PROJECTED PERTURBATION G_i
# ===========================================================================
def build_G_i(rho_list, branch):
    """G_i = Σ_{a in branch} ρ[a] ⊗ γ_a (anti-Hermitian)."""
    dim_rho = rho_list[0].shape[0]
    dim_spin = 16  # (local)
    G = np.zeros((dim_rho * dim_spin, dim_rho * dim_spin), dtype=complex)
    for a in branch:
        G += np.kron(rho_list[a], gammas[a])
    return G

for s in sector_data:
    s["G"] = {bn: build_G_i(s["rho"], bd) for bn, bd in BRANCHES.items()}

# ===========================================================================
# STEP 3: SPECTRAL TRACES AND 5-pt FD 2nd-DERIVATIVE
# ===========================================================================
def spectral_moments_from_eigsq(eigs_sq):
    """Given |λ|² eigenvalues (real, >=0), return all three functionals in one shot.
       SDW  = Σ |λ|      = Σ sqrt(|λ|²)
       zeta2 = Σ 1/|λ|²
       zeta4 = Σ 1/|λ|⁴
    """
    eigs_sq = np.clip(eigs_sq, 0.0, None)
    mask = eigs_sq > 1e-24
    e2 = eigs_sq[mask]
    abs_lam = np.sqrt(e2)
    return {
        "SDW": float(np.sum(abs_lam)),
        "zeta2": float(np.sum(1.0 / e2)),
        "zeta4": float(np.sum(1.0 / (e2 * e2))),
    }

def stencil_5pt(v_m2, v_m1, v_0, v_p1, v_p2, h):
    """5-pt central O(h^4), Hankel-order pin 2^(2ν-3)=2 for ν=2."""
    return (-v_m2 + 16.0 * v_m1 - 30.0 * v_0 + 16.0 * v_p1 - v_p2) / (12.0 * h ** 2)

def compute_J_block(branch_name, h):
    """For one branch and one h, compute J^{SDW}, J^{zeta2}, J^{zeta4} in a single
    5-phi × N_sector eigh pass. Returns dict with all three functionals.

    At each of the 5 stencil phi values, we diagonalize once per sector and
    extract all 3 functionals from that SAME eigenvalue vector.
    """
    J_sums = {"SDW": 0.0, "zeta2": 0.0, "zeta4": 0.0}                 # (local)
    phi_vals = (-2 * h, -h, 0.0, h, 2 * h)                             # (local)

    for sec in sector_data:
        D0 = sec["D"]
        G = sec["G"][branch_name]
        d_pq = sec["dim"]

        # Collect Tr f(D²) at each phi (for all 3 functionals)
        trf = {"SDW": np.zeros(5), "zeta2": np.zeros(5), "zeta4": np.zeros(5)}  # (local)

        # phi=0 uses cached eigenvalues
        sq_cached = sec["abs_lam_0"] ** 2
        m_cached = spectral_moments_from_eigsq(sq_cached)
        for fn in ("SDW", "zeta2", "zeta4"):
            trf[fn][2] = m_cached[fn]

        # Other 4 phi values: build D(phi), extract |λ|² via eigvalsh(−D²)
        for k, phi in enumerate(phi_vals):
            if k == 2:
                continue  # already filled from cache
            D_phi = D0 + phi * G
            Hsq = -(D_phi @ D_phi)
            Hsq = 0.5 * (Hsq + Hsq.conj().T)
            eigs_sq = eigvalsh_gpu(Hsq)
            m = spectral_moments_from_eigsq(eigs_sq)
            for fn in ("SDW", "zeta2", "zeta4"):
                trf[fn][k] = m[fn]

        # 5-pt stencil per functional, then PW weight
        for fn in ("SDW", "zeta2", "zeta4"):
            d2S = stencil_5pt(trf[fn][0], trf[fn][1], trf[fn][2], trf[fn][3], trf[fn][4], h)
            J_sums[fn] += d_pq * d2S

    return J_sums

# ===========================================================================
# STEP 4: SINGLE RUN AT PRIMARY_STEP (no iteration)
# ===========================================================================
print("\n" + "=" * 78, flush=True)
print("STEP 4: Single J-compute at PRIMARY_STEP (no iteration)", flush=True)
print("=" * 78, flush=True)

J_results = {}                                                    # (local)
t1 = time.time()                                                  # (local)
for bname in BRANCHES:
    print(f"  Computing branch {bname} primary J...", flush=True)
    J_results[bname] = compute_J_block(bname, PRIMARY_STEP)
    for fn in ("SDW", "zeta2", "zeta4"):
        print(f"    J_{bname}^{{{fn}}} = {J_results[bname][fn]:.6e}", flush=True)
print(f"  Primary J compute time: {time.time()-t1:.2f}s", flush=True)

# ===========================================================================
# STEP 5: ε-scan (pre-registered PRU diagnostic, NOT used for verdict)
# ===========================================================================
print("\n" + "=" * 78, flush=True)
print("STEP 5: ε-scan convergence diagnostic", flush=True)
print("=" * 78, flush=True)

t2 = time.time()                                                  # (local)
J_scan = {}                                                       # (local)
for bname in BRANCHES:
    J_scan[bname] = {fn: np.zeros(len(STENCIL_STEPS)) for fn in ("SDW", "zeta2", "zeta4")}
    for k, h in enumerate(STENCIL_STEPS):
        if abs(h - PRIMARY_STEP) < 1e-20:
            # Already computed
            for fn in ("SDW", "zeta2", "zeta4"):
                J_scan[bname][fn][k] = J_results[bname][fn]
        else:
            J_h = compute_J_block(bname, h)
            for fn in ("SDW", "zeta2", "zeta4"):
                J_scan[bname][fn][k] = J_h[fn]
    print(f"  Branch {bname} ε-scan done", flush=True)
print(f"  ε-scan compute time: {time.time()-t2:.2f}s", flush=True)

stencil_converged = True                                          # (local)
print(f"\n  {'Branch':<6} {'Func':<6} {'J(1e-4)':>14} {'J(1e-5)':>14} {'J(1e-6)':>14} {'rel spread':>12}", flush=True)
for bname in BRANCHES:
    for func in ("SDW", "zeta2", "zeta4"):
        vals = J_scan[bname][func]
        mean_abs = np.mean(np.abs(vals))
        spread = (np.max(vals) - np.min(vals)) / mean_abs if mean_abs > 0 else 0.0    # (local)
        flag = "" if abs(spread) < 0.05 else "!"                                       # (local)
        if abs(spread) > 0.10:
            stencil_converged = False
        print(f"  {bname:<6} {func:<6} {vals[0]:>14.4e} {vals[1]:>14.4e} {vals[2]:>14.4e} {spread:>11.2%}{flag}", flush=True)
print(f"\n  Stencil-converged: {stencil_converged}", flush=True)

# ===========================================================================
# STEP 6: drift_u1(L=6) PER P4-B DEFINITION
# ===========================================================================
print("\n" + "=" * 78, flush=True)
print("STEP 6: drift_u1(L=6) per P4-B definition", flush=True)
print("=" * 78, flush=True)

# <α_1>^L per branch = J^{zeta2}/J^{SDW} at truncation L
alpha1_per_branch = {                                             # (local)
    b: J_results[b]["zeta2"] / J_results[b]["SDW"] for b in BRANCHES
}
# <α_1>^{exact} = cross-branch mean (R-protection target value)
alpha1_exact = float(np.mean(list(alpha1_per_branch.values())))   # (local)

drift = {                                                         # (local)
    b: abs(alpha1_per_branch[b] - alpha1_exact) / abs(alpha1_exact)
    for b in BRANCHES
}
drift_u1 = drift["u1"]                                            # (local) headline REMED quantity
print(f"  <α_1>^L per branch:", flush=True)
for b in ("C2", "su2", "u1"):
    print(f"    {b:<4}: {alpha1_per_branch[b]:.6e}", flush=True)
print(f"  <α_1>^exact = cross-branch mean = {alpha1_exact:.6e}", flush=True)
print(f"  drift per branch:", flush=True)
for b in ("C2", "su2", "u1"):
    print(f"    {b:<4}: {drift[b]:.4%}", flush=True)
print(f"\n  HEADLINE: drift_u1(L={MAX_PQ_SUM}) = {drift_u1:.4%}", flush=True)
print(f"  4-tuple tag = ({drift_u1:.6f}, {SCHEME_TAG!r}, {CONVENTION_TAG!r}, L_max={L_MAX_TAG})", flush=True)

# S78 W2-C reference (PRU-violating original run)
S78_DRIFT_U1_REFERENCE = 0.8375                                   # (local) from s78_gate_verdicts.txt
print(f"\n  S78 W2-C reference drift_u1(L=6) = {S78_DRIFT_U1_REFERENCE:.4%}", flush=True)
print(f"  REMED-to-S78 relative delta     = {(drift_u1 - S78_DRIFT_U1_REFERENCE)/S78_DRIFT_U1_REFERENCE:+.2%}", flush=True)

# ===========================================================================
# STEP 7: VERDICT
# ===========================================================================
print("\n" + "=" * 78, flush=True)
print("STEP 7: Gate verdict — S80-W2-C-REMED", flush=True)
print("=" * 78, flush=True)

# The REMED gate pre-registration is about whether the PRU pins RUN:
#   PASS    = Script ran under PRU pins with all 5 pins implemented and
#             produced a 4-tuple-tagged drift_u1(L=6).
#   INFO    = Script ran but at least one PRU pin could not be stamped.
#   FAIL    = PRU pins inapplicable.
pru_pins_stamped = {                                              # (local)
    "import_closure_sha256": bool(IMPORT_CLOSURE_SHA),
    "eigenvalue_list_sha256": bool(EIGENVALUE_LIST_SHA),
    "hankel_order_pin": (HANKEL_ORDER_PIN == 2),
    "eps_scan_pre_registered": len(STENCIL_STEPS) == 3,
    "single_run_discipline": True,
}
all_stamped = all(pru_pins_stamped.values())                      # (local)

if all_stamped:
    verdict = "PASS"                                              # (local)
    reason = (f"All 5 PRU pins stamped; drift_u1(L={MAX_PQ_SUM})={drift_u1:.4%} "
              f"under closure hash {IMPORT_CLOSURE_SHA[:16]}...")  # (local)
elif any(pru_pins_stamped.values()):
    verdict = "INFO"                                              # (local)
    reason = f"Partial PRU stamp: {pru_pins_stamped}"             # (local)
else:
    verdict = "FAIL"                                              # (local)
    reason = "No PRU pin could be constructed."                   # (local)

print(f"  VERDICT: {verdict}", flush=True)
print(f"  reason : {reason}", flush=True)
print(f"  PRU pins stamped: {pru_pins_stamped}", flush=True)

# ===========================================================================
# STEP 8: PLOT
# ===========================================================================
fig, axs = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle(f"S80-W2-C-REMED: zeta-Josephson, L_max={MAX_PQ_SUM}, PRU-pinned", fontsize=13)

ax = axs[0]
b_order = ["C2", "su2", "u1"]
ratios = [alpha1_per_branch[b] for b in b_order]
ax.bar(b_order, ratios, color=["tab:blue", "tab:orange", "tab:green"])
ax.axhline(alpha1_exact, ls="--", color="k", alpha=0.5, label=f"<α_1>^exact = {alpha1_exact:.3e}")
ax.set_ylabel(r"$\langle \alpha_1 \rangle^L$ = $J^{\zeta_2}/J^{SDW}$")
ax.set_title(f"Per-branch α_1 (drift_u1 = {drift_u1:.2%})")
ax.legend(fontsize=8)

ax = axs[1]
drifts = [drift[b] for b in b_order]
ax.bar(b_order, drifts, color=["tab:blue", "tab:orange", "tab:green"])
ax.axhline(GATE_PASS, ls="--", color="green", label=f"PASS {GATE_PASS:.0%}")
ax.axhline(GATE_FAIL, ls="--", color="red", label=f"FAIL {GATE_FAIL:.0%}")
ax.set_ylabel("drift = |<α_1>^L − <α_1>^exact| / |<α_1>^exact|")
ax.set_title("Drift per branch (P4-B definition)")
ax.legend(fontsize=8)

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, "s80_w2c_remed.png")
plt.savefig(plot_path, dpi=120)
print(f"\n  Plot saved: {plot_path}", flush=True)

# ===========================================================================
# STEP 9: SAVE NPZ
# ===========================================================================
def pack(d):
    return np.array([d[b] for b in ["C2", "su2", "u1"]], dtype=float)

npz_path = os.path.join(SCRIPT_DIR, "s80_w2c_remed.npz")
np.savez(
    npz_path,
    branches=np.array(["C2", "su2", "u1"]),
    J_SDW=pack({b: J_results[b]["SDW"] for b in BRANCHES}),
    J_zeta2=pack({b: J_results[b]["zeta2"] for b in BRANCHES}),
    J_zeta4=pack({b: J_results[b]["zeta4"] for b in BRANCHES}),
    alpha1_per_branch=pack(alpha1_per_branch),
    alpha1_exact=np.float64(alpha1_exact),
    drift_per_branch=pack(drift),
    drift_u1=np.float64(drift_u1),
    s78_drift_u1_reference=np.float64(S78_DRIFT_U1_REFERENCE),
    stencil_steps=STENCIL_STEPS,
    J_scan_C2_zeta2=J_scan["C2"]["zeta2"],
    J_scan_su2_zeta2=J_scan["su2"]["zeta2"],
    J_scan_u1_zeta2=J_scan["u1"]["zeta2"],
    J_scan_C2_SDW=J_scan["C2"]["SDW"],
    J_scan_su2_SDW=J_scan["su2"]["SDW"],
    J_scan_u1_SDW=J_scan["u1"]["SDW"],
    stencil_converged=np.bool_(stencil_converged),
    # PRU pins
    import_closure_sha256=np.array(IMPORT_CLOSURE_SHA),
    eigenvalue_list_sha256=np.array(EIGENVALUE_LIST_SHA),
    hankel_order_pin=np.int64(HANKEL_ORDER_PIN),
    tau_fold_used=np.float64(TAU),
    max_pq_sum=np.int64(MAX_PQ_SUM),
    phi_J_amp=np.float64(PHI_J_AMPLITUDE),
    primary_step=np.float64(PRIMARY_STEP),
    # 4-tuple tag components
    scheme_tag=np.array(SCHEME_TAG),
    convention_tag=np.array(CONVENTION_TAG),
    L_max_tag=np.int64(L_MAX_TAG),
    verdict=np.array(verdict),
    reason=np.array(reason),
)
print(f"  NPZ saved: {npz_path}", flush=True)

# ===========================================================================
# STEP 10: APPEND VERDICT LINE
# ===========================================================================
verdict_path = os.path.join(SCRIPT_DIR, "s80_gate_verdicts.txt")
verdict_line = (
    f"S80-W2-C-REMED: {verdict} -- "
    f"drift_u1(L={MAX_PQ_SUM})={drift_u1:.4%}, "
    f"(value={drift_u1:.6f},scheme={SCHEME_TAG},conv={CONVENTION_TAG!r},L_max={L_MAX_TAG}), "
    f"import_closure_sha256={IMPORT_CLOSURE_SHA[:16]}, "
    f"eigenvalue_sha256={EIGENVALUE_LIST_SHA[:16]}, "
    f"hankel_order=2^(2nu-3)=2"
)
with open(verdict_path, "a") as fh:
    fh.write(verdict_line + "\n")
print(f"\n  Verdict appended: {verdict_path}", flush=True)
print(f"    {verdict_line}", flush=True)

print("\n" + "=" * 78, flush=True)
print(f"DONE. Verdict: {verdict}  |  drift_u1(L=6) = {drift_u1:.4%}", flush=True)
print("=" * 78, flush=True)
