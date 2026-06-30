"""Axis-B Stage-2 Set_B inspection helper.

Inspects the substrate-input-orthogonality Set_B data file consumed exclusively
by Axis-B per joint-theorem-promotion.md §"Substrate-input-orthogonality clause"
MANDATORY-K=3. Computes SHA-256 and dumps array contents for the per-clause
single-axis verify.
"""
import hashlib
import os
import sys
import numpy as np

# (local) Working directory anchor — script may be invoked from anywhere
ROOT = r"C:\sandbox\Ainulindale Exflation"
os.chdir(ROOT)

set_b_path = os.path.join("computations", "session-91", "s91_w6_1_d4_envelope_extended_pathway_b.npz")

with open(set_b_path, "rb") as f:
    raw = f.read()
set_b_sha256 = hashlib.sha256(raw).hexdigest()  # (local) file SHA for Stage-2 audit pin
print(f"set_B_path = {set_b_path}")
print(f"set_B_sha256 = {set_b_sha256}")
print(f"set_B_bytes  = {len(raw)}")

d = np.load(set_b_path, allow_pickle=True)
print(f"\narrays in file: {list(d.keys())}")
for k in d.keys():
    arr = d[k]
    try:
        if hasattr(arr, "shape"):
            print(f"  {k}: shape={arr.shape}, dtype={arr.dtype}")
            if arr.size == 0:
                print(f"    (empty)")
            elif arr.size <= 40:
                print(f"    value={arr}")
            else:
                flat = arr.flatten()
                print(f"    first10={flat[:10]}")
                print(f"    last10 ={flat[-10:]}")
        else:
            print(f"  {k}: {repr(arr)}")
    except Exception as e:
        print(f"  {k}: <inspection failed: {e}>")

print("\n--- DONE ---")
