# -*- coding: utf-8 -*-
"""(local probe — NOT a deliverable) §W6-2 pre-flight: (0,0)-block band structure,
eigh gauge smoothness across the (tau,mu) mesh, s84 cache keys."""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")
import sys
from pathlib import Path
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import tau_fold  # noqa: E402
import dirac_spectrum as ds  # noqa: E402

V_JENSEN = np.array([2.0, -2.0, 1.0])
V_MU = np.array([11.0, 7.0, -8.0])
MU_NORM = float(np.sqrt(V_MU @ V_MU))


def build_su3_infra():
    gens = ds.su3_generators()
    f_abc = ds.compute_structure_constants(gens)
    B_ab = ds.compute_killing_form(f_abc)
    gammas = ds.build_cliff8()
    return gens, f_abc, B_ab, gammas


def metric_scale_factors(tau, mu):
    log_L = tau * V_JENSEN + (mu / MU_NORM) * V_MU
    return float(np.exp(log_L[0])), float(np.exp(log_L[1])), float(np.exp(log_L[2]))


def build_singlet(tau, mu, infra):
    gens, f_abc, B_ab, gammas = infra
    L1, L2, L3 = metric_scale_factors(tau, mu)
    g = ds.u2_invariant_metric(B_ab, L1, L2, L3)
    E = ds.orthonormal_frame(g)
    ft = ds.frame_structure_constants(f_abc, E)
    Gamma = ds.connection_coefficients(ft)
    Omega_spin = ds.spinor_connection_offset(Gamma, gammas)
    return Omega_spin.copy()


def eigh_H(D_pi):
    H = 1j * D_pi
    Hh = 0.5 * (H + H.conj().T)
    w, v = np.linalg.eigh(Hh)
    return w.real, v


infra = build_su3_infra()

print("=" * 70)
print("PROBE 1: (0,0)-block spectrum at (tau,mu)=(0.19, 0) [fold, Jensen line]")
D = build_singlet(0.19, 0.0, infra)
print(f"  D shape={D.shape}, max|Re D|={np.max(np.abs(D.real)):.3e}, max|Im D|={np.max(np.abs(D.imag)):.3e}")
w, v = eigh_H(D)
aw = np.abs(w)
order = np.argsort(aw)
print("  |lambda| sorted (16 values):")
for k, idx in enumerate(order):
    print(f"    band {k:2d}: |lam|={aw[idx]:.12f}  (signed mu={w[idx]:+.12f})")

# degenerate-group structure
sw = aw[order]
groups = []
start = 0  # (local)
for k in range(1, 16):
    if sw[k] - sw[k - 1] > 1e-7:
        groups.append((start, k, sw[start]))
        start = k
groups.append((start, 16, sw[start]))
print("  degenerate groups (deg_tol=1e-7 on |lambda|):")
for (a, b, val) in groups:
    print(f"    indices [{a}:{b}] deg={b-a}  |lam|={val:.10f}")

print()
print("PROBE 1b: spectrum at off-Jensen corners")
for (tt, mm) in [(0.10, -0.10), (0.10, 0.10), (0.30, -0.10), (0.30, 0.10), (0.19, 0.05)]:
    D2 = build_singlet(tt, mm, infra)
    w2, _ = eigh_H(D2)
    aw2 = np.sort(np.abs(w2))
    g01 = aw2[1] - aw2[0]
    g12 = aw2[2] - aw2[1]
    g23 = aw2[3] - aw2[2]
    print(f"  (tau={tt:.2f},mu={mm:+.2f}): low4 |lam| = {aw2[0]:.8f},{aw2[1]:.8f},{aw2[2]:.8f},{aw2[3]:.8f}"
          f"  gap(0,1)={g01:.2e} gap(1,2)={g12:.4f} gap(2,3)={g23:.2e}")
    print(f"      maxImD={np.max(np.abs(D2.imag)):.3e} maxReD={np.max(np.abs(D2.real)):.3e}")

print()
print("PROBE 2: eigh gauge smoothness of the lowest-2 multiplet along the mesh")


def lowest_block(tau, mu, deg=2):
    D3 = build_singlet(tau, mu, infra)
    w3, v3 = eigh_H(D3)
    o3 = np.argsort(np.abs(w3))
    return v3[:, o3[:deg]]


for mu_test in (0.0, 0.052):
    taus = np.arange(0.10, 0.10 + 12 * 0.004, 0.004)
    prev = lowest_block(taus[0], mu_test)
    mins, dets = [], []
    for t in taus[1:]:
        cur = lowest_block(t, mu_test)
        M = prev.conj().T @ cur
        mins.append(float(np.min(np.abs(np.diag(M)))))
        dets.append(float(np.abs(np.linalg.det(M))))
        prev = cur
    print(f"  mu={mu_test}: min diag|M_nn| over 11 steps = {min(mins):.6f}; "
          f"min |det M| = {min(dets):.6f}; mean diag = {np.mean(mins):.6f}")

print()
print("PROBE 3: s84 cache keys")
cache = np.load(PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz",
                allow_pickle=True)
print("  keys:", sorted(cache.files))
for k in sorted(cache.files):
    arr = cache[k]
    print(f"    {k}: shape={getattr(arr, 'shape', None)} dtype={getattr(arr, 'dtype', None)}")
    if arr.size <= 8:
        print(f"        value={arr}")

print()
print("PROBE 4: timing — one full node eval (16x16 eigh)")
import time
t0 = time.perf_counter()
for _ in range(50):
    D4 = build_singlet(0.2, 0.03, infra)
    w4, v4 = eigh_H(D4)
t1 = time.perf_counter()
print(f"  50 node evals in {t1-t0:.3f}s -> {(t1-t0)/50*1000:.2f} ms/node; 2601 nodes ~ {(t1-t0)/50*2601:.1f}s")
print("PROBE DONE")
