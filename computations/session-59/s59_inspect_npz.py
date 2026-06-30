#!/usr/bin/env python3
"""Inspect NPZ files for Q-VARIABLE-59."""
import numpy as np

out_lines = []

for fname in ['s58_sa_saddle.npz', 's58_ej_3d_landscape.npz']:
    d = np.load(f'computations/_shared/{fname}', allow_pickle=True)
    out_lines.append(f'\n=== {fname} ===')
    out_lines.append(f'Keys: {list(d.keys())}')
    for k in sorted(d.keys()):
        v = d[k]
        if v.ndim == 0:
            out_lines.append(f'  {k}: scalar = {v.item()}')
        elif v.size < 30:
            out_lines.append(f'  {k}: shape={v.shape}, dtype={v.dtype}')
            out_lines.append(f'    values = {v}')
        else:
            out_lines.append(f'  {k}: shape={v.shape}, dtype={v.dtype}')
            out_lines.append(f'    first 5 = {v[:5]}')
            out_lines.append(f'    last 5  = {v[-5:]}')
            out_lines.append(f'    min={v.min():.6e}, max={v.max():.6e}, mean={v.mean():.6e}')

with open('computations/session-59/s59_npz_inspect.txt', 'w') as f:
    f.write('\n'.join(out_lines))

print("Written to s59_npz_inspect.txt")
