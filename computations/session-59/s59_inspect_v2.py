#!/usr/bin/env python3
"""Inspect input .npz files for PENROSE-ACCESS-59 - v2."""
import numpy as np
import os

outlines = []

def inspect(path, label):
    outlines.append(f"\n=== {label}: {path} ===")
    if not os.path.exists(path):
        outlines.append(f"  FILE NOT FOUND")
        return None
    outlines.append(f"  FILE EXISTS, size={os.path.getsize(path)} bytes")
    f = np.load(path, allow_pickle=True)
    outlines.append(f"  Arrays: {f.files}")
    for k in sorted(f.files):
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

os.chdir("C:/sandbox/Ainulindale Exflation")

inspect("computations/session-59/s59_npair3_integ.npz", "N_pair=3 integrability (W0-2)")
inspect("computations/session-58/s58_sa_saddle.npz", "S58 SA saddle")
inspect("computations/session-58/s58_cc_cancellation_sweep.npz", "S58 CC cancellation sweep")

out = "\n".join(outlines)
outpath = "computations/session-59/s59_penrose_inspect.txt"
with open(outpath, "w") as fout:
    fout.write(out)
print(f"Written to {outpath}, {len(out)} chars")
