import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
print("Starting...")
import numpy as np
print("numpy OK")
from canonical_constants import tau_fold, G_DeWitt, M_KK_gravity, M_Pl_unreduced
print(f"tau_fold={tau_fold}, G_DeWitt={G_DeWitt}")
print(f"M_KK={M_KK_gravity:.4e}, M_P={M_Pl_unreduced:.4e}")

# Check S44 data
s44 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's44_dos_tau.npz')
print(f"S44 path: {s44}")
print(f"S44 exists: {os.path.exists(s44)}")

if os.path.exists(s44):
    d = np.load(s44, allow_pickle=True)
    print(f"S44 keys: {list(d.keys())[:5]}...")
    tv = d['tau_values']
    omegas = d[f'tau{tv[0]:.2f}_all_omega']
    dims = d[f'tau{tv[0]:.2f}_all_dim2']
    a2_0 = np.sum(dims * omegas)
    print(f"a2(tau=0) = {a2_0:.2f}")

# Quick test: compute the key number
MKK_MP = M_KK_gravity / M_Pl_unreduced
print(f"M_KK/M_P = {MKK_MP:.6e}")
print(f"(M_KK/M_P)^4 = {MKK_MP**4:.6e}")

# Write a test file to confirm script execution completes
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 's52_test_marker.txt'), 'w') as f:
    f.write("Script completed successfully\n")
    f.write(f"M_KK/M_P = {MKK_MP:.6e}\n")
print("Test marker written. DONE.")
