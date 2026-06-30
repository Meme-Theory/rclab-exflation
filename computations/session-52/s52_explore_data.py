#!/usr/bin/env python3
"""Explore input data for N-PAIR-FULL-52."""
import sys
sys.path.insert(0, '.')
import numpy as np

print("="*60)
print("s44_dos_tau.npz")
print("="*60)
d = np.load('computations/session-44/s44_dos_tau.npz', allow_pickle=True)
print("Keys:", list(d.keys()))
for k in sorted(d.keys()):
    v = d[k]
    if hasattr(v, 'shape'):
        print(f"  {k}: shape={v.shape}, dtype={v.dtype}")
        if v.ndim == 0:
            print(f"    scalar value: {v.item()}")
        elif v.ndim == 1 and v.size <= 30:
            print(f"    values: {v}")
        elif v.ndim == 1:
            print(f"    first 10: {v[:10]}")
            print(f"    size={v.size}, min={v.min():.6f}, max={v.max():.6f}")
        elif v.ndim == 2:
            print(f"    shape={v.shape}")
            if v.size <= 50:
                print(f"    {v}")
    else:
        print(f"  {k}: type={type(v)}")

print()
print("="*60)
print("s36_multisector_ed.npz")
print("="*60)
d2 = np.load('computations/session-36/s36_multisector_ed.npz', allow_pickle=True)
print("Keys:", list(d2.keys()))
for k in sorted(d2.keys()):
    v = d2[k]
    if hasattr(v, 'shape'):
        print(f"  {k}: shape={v.shape}, dtype={v.dtype}")
        if v.ndim == 0:
            print(f"    scalar value: {v.item()}")
        elif v.ndim == 1 and v.size <= 20:
            print(f"    values: {v}")
        elif v.ndim == 1:
            print(f"    first 5: {v[:5]}, size={v.size}")
    else:
        print(f"  {k}: type={type(v)}")

print()
print("="*60)
print("s34a_dphys_kosmann.npz")
print("="*60)
d3 = np.load('computations/session-34/s34a_dphys_kosmann.npz', allow_pickle=True)
print("Keys:", list(d3.keys()))
for k in sorted(d3.keys()):
    v = d3[k]
    if hasattr(v, 'shape'):
        print(f"  {k}: shape={v.shape}, dtype={v.dtype}")
        if v.ndim == 0:
            print(f"    scalar value: {v.item()}")
        elif v.ndim == 1 and v.size <= 20:
            print(f"    values: {v}")
        elif v.ndim == 1:
            print(f"    first 5: {v[:5]}, size={v.size}")
        elif v.ndim == 2:
            r, c = v.shape
            print(f"    [{r}x{c}], corner: {v[:min(3,r),:min(3,c)]}")
    else:
        print(f"  {k}: type={type(v)}")

print("\nDONE")
