"""Check keys in all .npz files for the 4-sector low-mode analysis."""
import numpy as np

for fname in ['kk1_bosonic_spectrum.npz', 'l20_TT_spectrum.npz',
              's19a_sweep_data.npz', 'l20_vtotal_minimum.npz']:
    print(f"\n--- {fname} ---")
    data = np.load(fname, allow_pickle=True)
    for key in sorted(data.keys()):
        arr = data[key]
        if hasattr(arr, 'shape'):
            print(f"  {key}: shape={arr.shape}, dtype={arr.dtype}")
            if arr.ndim == 1 and len(arr) <= 25:
                print(f"    values: {arr}")
        else:
            print(f"  {key}: {type(arr)} = {arr}")
