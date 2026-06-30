#!/usr/bin/env python3
"""Minimal test."""
with open('computations/session-59/s59_quicktest_out.txt', 'w') as f:
    f.write("start\n")
    try:
        import numpy as np
        f.write("numpy ok\n")
        lp = np.load('computations/session-57/s57_leggett_partition.npz', allow_pickle=True)
        f.write(f"lp keys: {list(lp.keys())}\n")
        if 'F_BA' in lp.keys():
            f.write(f"F_BA = {float(lp['F_BA'])}\n")
        else:
            f.write("NO F_BA key!\n")
    except Exception as e:
        f.write(f"ERROR: {e}\n")
        import traceback
        f.write(traceback.format_exc())
