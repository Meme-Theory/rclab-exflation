import numpy as np

d = np.load(r"computations/investigation-12/inv12_w3_2_floquet_ordered_veil_resonance.npz",
            allow_pickle=True)
print("=== KEYS ===")
for k in d.files:
    arr = np.asarray(d[k])
    print(f"{k:30s} shape={str(arr.shape):15s} dtype={arr.dtype}")

def scalar(k):
    return float(np.asarray(d[k]).flat[0])

print("\n=== SCALARS / SMALL FIELDS ===")
for k in d.files:
    arr = np.asarray(d[k])
    if arr.size <= 4:
        print(f"{k:30s} = {arr.ravel()}")
