#!/usr/bin/env python3
"""Inspect input .npz files for PENROSE-ACCESS-59."""
import numpy as np
import os, sys

outlines = []

def inspect(path, label):
    outlines.append(f"\n=== {label}: {path} ===")
    if not os.path.exists(path):
        outlines.append(f"  FILE NOT FOUND")
        return None
    f = np.load(path, allow_pickle=True)
    outlines.append(f"  Arrays: {f.files}")
    for k in f.files:
        v = f[k]
        outlines.append(f"  {k}: shape={v.shape}, dtype={v.dtype}")
        if v.ndim == 0:
            outlines.append(f"    scalar value: {v.item()}")
        elif v.size <= 30:
            outlines.append(f"    values: {v}")
        else:
            outlines.append(f"    first 10: {v.flat[:10]}")
            outlines.append(f"    last 5:  {v.flat[-5:]}")
    return f

f1 = inspect("computations/session-59/s59_npair3_integ.npz", "N_pair=3 integrability")
f2 = inspect("computations/session-58/s58_sa_saddle.npz", "S58 SA saddle")
f3 = inspect("computations/session-58/s58_cc_cancellation_sweep.npz", "S58 CC cancellation sweep")

out = "\n".join(outlines)
with open("computations/session-59/s59_inspect_output.txt", "w") as fout:
    fout.write(out)
print("Inspection written to s59_inspect_output.txt")
