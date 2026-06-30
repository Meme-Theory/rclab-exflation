#!/usr/bin/env python3
"""Quick test script to debug s59_neff_ba.py imports."""
import sys
import traceback

sys.path.insert(0, 'computations')

outfile = 'computations/session-59/s59_neff_test_output.txt'

try:
    with open(outfile, 'w') as f:
        f.write("Starting import test...\n")

        from canonical_constants import (
            M_KK, T_BBN_GeV, PI, rho_crit_GeV4,
            Omega_r, H_0_km_s_Mpc, T_CMB, k_B,
            M_Pl_reduced, G_N,
        )
        f.write(f"Basic imports OK. M_KK = {M_KK}\n")

        from canonical_constants import Vol_SU3_Haar
        f.write(f"Vol_SU3_Haar = {Vol_SU3_Haar}\n")

        import numpy as np
        f.write("numpy OK\n")

        # Test loading npz files
        vp = np.load('computations/session-58/s58_volovik_partition.npz', allow_pickle=True)
        f.write(f"s58_volovik_partition loaded, keys: {list(vp.keys())[:5]}...\n")

        gge = np.load('computations/session-58/s58_sq_omega_gge.npz', allow_pickle=True)
        f.write(f"s58_sq_omega_gge loaded, keys: {list(gge.keys())[:5]}...\n")

        lp = np.load('computations/session-57/s57_leggett_partition.npz', allow_pickle=True)
        f.write(f"s57_leggett_partition loaded\n")
        f.write(f"F_BA = {float(lp['F_BA'])}\n")

        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        f.write("matplotlib OK\n")

        f.write("\nALL IMPORTS AND LOADS SUCCESSFUL\n")

except Exception as e:
    with open(outfile, 'a') as f:
        f.write(f"\nERROR: {e}\n")
        f.write(traceback.format_exc())
