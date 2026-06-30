#!/usr/bin/env python3
"""Verify s59_neff_ba.npz output."""
import numpy as np

d = np.load('computations/session-59/s59_neff_ba.npz', allow_pickle=True)
with open('computations/session-59/s59_neff_verify.txt', 'w') as f:
    f.write("=== s59_neff_ba.npz verification ===\n\n")
    for k in sorted(d.keys()):
        v = d[k]
        if v.ndim == 0:
            f.write(f"{k}: {v.item()}\n")
        elif v.size < 20:
            f.write(f"{k}: {v}\n")
        else:
            f.write(f"{k}: shape={v.shape}, first 5: {v.flat[:5]}\n")
