# -*- coding: utf-8 -*-
"""(local probe 2 — NOT a deliverable) §W6-2: crossing-curve map, intra-pair
coupling magnitude, signed-spectrum layout, phase-pin smoothness."""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")
import sys
from pathlib import Path
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
import dirac_spectrum as ds  # noqa: E402

V_JENSEN = np.array([2.0, -2.0, 1.0])
V_MU = np.array([11.0, 7.0, -8.0])
MU_NORM = float(np.sqrt(V_MU @ V_MU))

gens = ds.su3_generators()
f_abc = ds.compute_structure_constants(gens)
B_ab = ds.compute_killing_form(f_abc)
gammas = ds.build_cliff8()


def build_singlet(tau, mu):
    log_L = tau * V_JENSEN + (mu / MU_NORM) * V_MU
    L1, L2, L3 = (float(np.exp(x)) for x in log_L)
    g = ds.u2_invariant_metric(B_ab, L1, L2, L3)
    E = ds.orthonormal_frame(g)
    ft = ds.frame_structure_constants(f_abc, E)
    Gamma = ds.connection_coefficients(ft)
    return ds.spinor_connection_offset(Gamma, gammas).copy()


def eigh_signed(tau, mu):
    H = 1j * build_singlet(tau, mu)
    Hh = 0.5 * (H + H.conj().T)
    w, v = np.linalg.eigh(Hh)   # ascending SIGNED order
    return w.real, v


print("PROBE A: full signed spectrum at corner (0.10,+0.10) and neighbors")
for (tt, mm) in [(0.10, 0.10), (0.104, 0.096), (0.12, 0.10), (0.10, 0.08), (0.14, 0.10), (0.19, 0.0)]:
    w, _ = eigh_signed(tt, mm)
    print(f"  ({tt:.3f},{mm:+.3f}): signed w = {np.array2string(w, precision=6, max_line_width=200)}")

print()
print("PROBE B: B1/B2 |lambda| gap map on 21x21 coarse mesh (window [0.10,0.30]x[-0.10,0.10])")
taus = np.linspace(0.10, 0.30, 21)
mus = np.linspace(-0.10, 0.10, 21)
gapmap = np.zeros((21, 21))
for i, t in enumerate(taus):
    for j, m in enumerate(mus):
        w, _ = eigh_signed(t, m)
        aw = np.sort(np.abs(w))
        gapmap[i, j] = aw[2] - aw[1]
print(f"  min gap12 = {gapmap.min():.6f} at idx {np.unravel_index(gapmap.argmin(), gapmap.shape)}")
print(f"  (tau,mu) of min = ({taus[np.unravel_index(gapmap.argmin(), gapmap.shape)[0]]:.3f},"
      f"{mus[np.unravel_index(gapmap.argmin(), gapmap.shape)[1]]:+.3f})")
nodes_small = int(np.sum(gapmap < 0.005))  # (local)
print(f"  nodes with gap12 < 0.005: {nodes_small}/441 = {nodes_small/441*100:.1f}%")
nodes_small2 = int(np.sum(gapmap < 0.002))  # (local)
print(f"  nodes with gap12 < 0.002: {nodes_small2}/441 = {nodes_small2/441*100:.1f}%")
# print the gap map row by row (tau ascending), coarse
for i in range(0, 21, 4):
    print(f"  tau={taus[i]:.2f}: " + " ".join(f"{gapmap[i,j]*1000:5.1f}" for j in range(0, 21, 2)) + "  [x1e-3]")

print()
print("PROBE C: intra-pair WZ coupling |<u_+|dH_a|u_-)>| / (lam_+ - lam_-) at sample nodes")
H_EPS = 0.004  # (local) mesh step used as FD step


def pair_states(tau, mu):
    w, v = eigh_signed(tau, mu)
    # signed layout: idx 7 = -|lam|min member, idx 8 = +|lam|min member (16-dim, symmetric)
    return w, v[:, 7], v[:, 8]


for (tt, mm) in [(0.19, 0.0), (0.19, 0.05), (0.25, -0.05), (0.12, 0.08), (0.30, 0.10)]:
    w0, um, up = pair_states(tt, mm)
    Hp_t = 1j * build_singlet(tt + H_EPS, mm)
    Hm_t = 1j * build_singlet(tt - H_EPS, mm)
    dH_t = 0.5 * ((Hp_t + Hp_t.conj().T) - (Hm_t + Hm_t.conj().T)) / (2 * H_EPS)
    Hp_m = 1j * build_singlet(tt, mm + H_EPS)
    Hm_m = 1j * build_singlet(tt, mm - H_EPS)
    dH_m = 0.5 * ((Hp_m + Hp_m.conj().T) - (Hm_m + Hm_m.conj().T)) / (2 * H_EPS)
    lam_m, lam_p = w0[7], w0[8]
    c_t = up.conj() @ (dH_t @ um) / (lam_m - lam_p)
    c_m = up.conj() @ (dH_m @ um) / (lam_m - lam_p)
    print(f"  ({tt:.2f},{mm:+.2f}): lam_pair=({lam_m:+.6f},{lam_p:+.6f}); "
          f"|A_tau,+-|={abs(c_t):.6e} |A_mu,+-|={abs(c_m):.6e}")

print()
print("PROBE D: phase-pin smoothness (largest-|comp| real-positive) along tau line at mu=0.052")


def pin_phase(vec):
    k = int(np.argmax(np.abs(vec)))
    ph = vec[k] / abs(vec[k])
    return vec / ph


prev_m, prev_p = None, None
maxdef_m, maxdef_p = 0.0, 0.0
for t in np.arange(0.10, 0.30001, 0.004):
    _, um, up = pair_states(t, 0.052)
    um, up = pin_phase(um), pin_phase(up)
    if prev_m is not None:
        dm = abs(np.angle(prev_m.conj() @ um))
        dp = abs(np.angle(prev_p.conj() @ up))
        maxdef_m = max(maxdef_m, dm)
        maxdef_p = max(maxdef_p, dp)
    prev_m, prev_p = um, up
print(f"  max |arg<u(x)|u(x+h)>| over 50 steps: minus-member={maxdef_m:.3e}, plus-member={maxdef_p:.3e}")
print("  (small ~O(h) => pinned frame smooth; O(1) => phase jumps present)")

print()
print("PROBE E: J/PH structure — is u_+ related to u_- by an antiunitary? overlap pattern")
w0, um, up = pair_states(0.19, 0.0)
print(f"  |<u_+|u_->| = {abs(up.conj() @ um):.3e} (orthogonal, trivially)")
print(f"  |<u_+*|u_->| = {abs(up @ um):.3e}  (complex-conjugate overlap — K-type pairing if ~1)")
print("PROBE2 DONE")
