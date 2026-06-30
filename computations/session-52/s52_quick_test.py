#!/usr/bin/env python3
"""Minimal test — no imports from tier1."""
import numpy as np
import os

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's52_quick_out.txt')

try:
    lines = ["START"]

    # Gell-Mann matrices
    lam = []
    lam.append(np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex))
    lam.append(np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex))
    lam.append(np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex))
    lam.append(np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex))
    lam.append(np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex))
    lam.append(np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex))
    lam.append(np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex))
    lam.append(np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex) / np.sqrt(3))

    su3_basis = [-1j/2.0 * l for l in lam]
    lines.append(f"su3 basis: {len(su3_basis)} generators")

    # Borel basis
    basis = []
    h1 = np.zeros((3,3), dtype=complex); h1[0,0]=1; h1[1,1]=-1
    h2 = np.zeros((3,3), dtype=complex); h2[1,1]=1; h2[2,2]=-1
    basis.append(h1); basis.append(h2)

    E12R = np.zeros((3,3), dtype=complex); E12R[0,1]=1
    E12I = np.zeros((3,3), dtype=complex); E12I[0,1]=1j
    E23R = np.zeros((3,3), dtype=complex); E23R[1,2]=1
    E23I = np.zeros((3,3), dtype=complex); E23I[1,2]=1j
    E13R = np.zeros((3,3), dtype=complex); E13R[0,2]=1
    E13I = np.zeros((3,3), dtype=complex); E13I[0,2]=1j
    basis.extend([E12R, E12I, E23R, E23I, E13R, E13I])
    lines.append(f"gstar basis: {len(basis)} generators")

    # Cross pairing: Im Tr(e_a T^b)
    P = np.zeros((8,8))
    for a in range(8):
        for b in range(8):
            P[a,b] = np.imag(np.trace(su3_basis[a] @ basis[b]))

    lines.append(f"Cross pairing rank: {np.linalg.matrix_rank(P, tol=1e-10)}")
    lines.append(f"Cross pairing det: {np.linalg.det(P):.6f}")
    lines.append(f"Cross pairing:\n{P}")

    # su(3) isotropy
    su3_pair = np.zeros((8,8))
    for a in range(8):
        for b in range(8):
            su3_pair[a,b] = np.imag(np.trace(su3_basis[a] @ su3_basis[b]))
    lines.append(f"su3 isotropy max: {np.max(np.abs(su3_pair)):.2e}")

    # g* isotropy
    gs_pair = np.zeros((8,8))
    for a in range(8):
        for b in range(8):
            gs_pair[a,b] = np.imag(np.trace(basis[a] @ basis[b]))
    lines.append(f"gstar isotropy max: {np.max(np.abs(gs_pair)):.2e}")

    lines.append("DONE")

    with open(out, 'w') as f:
        f.write('\n'.join(lines))

except Exception as e:
    import traceback
    with open(out, 'w') as f:
        f.write(f"ERROR: {e}\n{traceback.format_exc()}")
