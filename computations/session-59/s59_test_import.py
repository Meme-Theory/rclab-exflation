#!/usr/bin/env python3
"""Test imports and npz loading."""
import os
import traceback

os.chdir("C:/sandbox/Ainulindale Exflation")

try:
    import sys
    sys.path.insert(0, "computations")
    import numpy as np
    with open("computations/session-59/s59_test_out.txt", "w") as f:
        f.write("numpy OK\n")

        # Test npz loading
        try:
            d1 = np.load("computations/session-59/s59_npair3_integ.npz", allow_pickle=True)
            f.write(f"s59_npair3_integ arrays: {sorted(d1.files)}\n")
            for k in sorted(d1.files):
                v = d1[k]
                if v.ndim == 0:
                    f.write(f"  {k} = {v.item()}\n")
                elif v.size <= 20:
                    f.write(f"  {k} = {v}\n")
                else:
                    f.write(f"  {k}: shape={v.shape}\n")
        except Exception as e:
            f.write(f"ERROR loading s59_npair3_integ: {e}\n")
            f.write(traceback.format_exc())

        try:
            d2 = np.load("computations/session-58/s58_sa_saddle.npz", allow_pickle=True)
            f.write(f"\ns58_sa_saddle arrays: {sorted(d2.files)}\n")
            for k in sorted(d2.files):
                v = d2[k]
                if v.ndim == 0:
                    f.write(f"  {k} = {v.item()}\n")
                elif v.size <= 20:
                    f.write(f"  {k} = {v}\n")
                else:
                    f.write(f"  {k}: shape={v.shape}\n")
        except Exception as e:
            f.write(f"ERROR loading s58_sa_saddle: {e}\n")
            f.write(traceback.format_exc())

        try:
            d3 = np.load("computations/session-58/s58_cc_cancellation_sweep.npz", allow_pickle=True)
            f.write(f"\ns58_cc_cancellation_sweep arrays: {sorted(d3.files)}\n")
            for k in sorted(d3.files):
                v = d3[k]
                if v.ndim == 0:
                    f.write(f"  {k} = {v.item()}\n")
                elif v.size <= 20:
                    f.write(f"  {k} = {v}\n")
                else:
                    f.write(f"  {k}: shape={v.shape}\n")
        except Exception as e:
            f.write(f"ERROR loading s58_cc_cancellation_sweep: {e}\n")
            f.write(traceback.format_exc())

        f.write("\nDONE\n")
except Exception as e:
    with open("computations/session-59/s59_test_err.txt", "w") as f:
        f.write(f"FATAL: {e}\n")
        f.write(traceback.format_exc())
