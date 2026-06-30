#!/usr/bin/env python3
"""Probe NPZ files for Q-VARIABLE-59."""
import numpy as np

lines = []

for fname in ['s58_sa_saddle.npz', 's58_ej_3d_landscape.npz']:
    d = np.load(f'computations/_shared/{fname}', allow_pickle=True)
    lines.append(f'\n=== {fname} ===')
    lines.append(f'Keys: {sorted(d.keys())}')
    for k in sorted(d.keys()):
        v = d[k]
        if v.ndim == 0:
            lines.append(f'  {k}: scalar = {v.item()}')
        elif v.size < 30:
            lines.append(f'  {k}: shape={v.shape}, dtype={v.dtype}, values={v}')
        else:
            lines.append(f'  {k}: shape={v.shape}, dtype={v.dtype}, min={v.min():.6e}, max={v.max():.6e}')

with open('computations/session-59/s59_npz_probe.txt', 'w') as f:
    f.write('\n'.join(lines))
