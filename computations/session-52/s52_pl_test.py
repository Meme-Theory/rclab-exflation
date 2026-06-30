#!/usr/bin/env python3
"""Quick test of PL-Tduality components."""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's52_test_out.txt')

try:
    from s52_pl_tduality import (su3_antihermitian_basis, borel_basis,
                                  verify_manin_triple, compute_structure_constants_general)
    lines = []
    lines.append("=== TEST 1: Bases ===")
    su3b = su3_antihermitian_basis()
    lines.append(f"su3 basis count: {len(su3b)}")

    gb = borel_basis()
    lines.append(f"gstar basis count: {len(gb)}")

    lines.append("\n=== TEST 2: Manin triple ===")
    mt = verify_manin_triple()
    for k, v in mt.items():
        if isinstance(v, np.ndarray) and v.ndim > 1:
            lines.append(f"{k}: shape={v.shape}, max={np.max(np.abs(v)):.6f}")
        else:
            lines.append(f"{k}: {v}")

    lines.append("\n=== TEST 3: g* structure constants ===")
    f_abc = compute_structure_constants_general(gb)
    lines.append(f"f_abc shape: {f_abc.shape}")
    lines.append(f"f_abc max: {np.max(np.abs(f_abc)):.6f}")
    # Check antisymmetry
    antisym_err = np.max(np.abs(f_abc + np.transpose(f_abc, (1,0,2))))
    lines.append(f"Antisymmetry error: {antisym_err:.2e}")

    lines.append("\n=== TEST 4: Dual metric at tau=0 ===")
    from s52_pl_tduality import iwasawa_metric_from_jensen
    M, P, G = iwasawa_metric_from_jensen(0.0)
    lines.append(f"M_dual shape: {M.shape}")
    evals = np.linalg.eigvalsh(M)
    lines.append(f"M_dual eigenvalues: {np.sort(evals)}")
    lines.append(f"All positive: {np.all(evals > 0)}")

    lines.append("\nDONE")

    with open(out, 'w') as f:
        f.write('\n'.join(lines))

except Exception as e:
    import traceback
    with open(out, 'w') as f:
        f.write(f"ERROR: {e}\n")
        f.write(traceback.format_exc())
