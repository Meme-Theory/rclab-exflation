#!/usr/bin/env python3
"""Quick inspection of data files for Liouvillian computation."""
import os, sys, numpy as np

ARCHIVE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_shared")

d37 = np.load(os.path.join(ARCHIVE, 's37_pair_susceptibility.npz'), allow_pickle=True)
print("=== s37_pair_susceptibility.npz keys ===")
for k in sorted(d37.files):
    v = d37[k]
    if isinstance(v, np.ndarray):
        print(f"  {k}: shape={v.shape}, dtype={v.dtype}")
    else:
        print(f"  {k}: {v}")

print()
d38 = np.load(os.path.join(ARCHIVE, 's38_otoc_bcs.npz'), allow_pickle=True)
print("=== s38_otoc_bcs.npz keys ===")
for k in sorted(d38.files):
    v = d38[k]
    if isinstance(v, np.ndarray):
        print(f"  {k}: shape={v.shape}, dtype={v.dtype}")
    else:
        print(f"  {k}: {v}")

print("\n=== Key data ===")
E_8 = d37['E_8']
V_8x8 = d37['V_8x8']
rho_8 = d37['rho']
mu = float(d37['mu'])
branch_labels = d37['branch_labels']

print(f"E_8 = {E_8}")
print(f"mu = {mu}")
print(f"branch_labels = {branch_labels}")
print(f"rho_8 = {rho_8}")
print(f"V_8x8 =")
print(V_8x8)
print(f"\nV_phys (DOS-weighted) =")
V_phys = V_8x8 * np.sqrt(np.outer(rho_8, rho_8))
print(V_phys)
print(f"\nV_phys max = {np.max(np.abs(V_phys)):.8f}")
print(f"V_phys diagonal = {np.diag(V_phys)}")

# Check if s38 has V_phys directly
if 'V_phys' in d38.files:
    V_phys_s38 = d38['V_phys']
    print(f"\nV_phys from s38: shape={V_phys_s38.shape}")
    print(f"  max diff from recomputed = {np.max(np.abs(V_phys - V_phys_s38)):.2e}")
