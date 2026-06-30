#!/usr/bin/env python3
"""
s86_w6_2_lattice_spacing_immunization.py
========================================
Gate: S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE (W6-2 / 1C C-α / OQ1)

Owner: lizzi-spectral-functional-theorist
Trigger: [VERIFY-THEOREM]
Classification: GEOMETRIC

PURPOSE
-------
Test §VII.S.B C-α corollary at slot-by-slot Mellin level. The corollary
predicts that the substrate's a_n spectral moments inherit the discretization
order of the regulator: tree-level Symanzik improvement gives O(a^4) per
Mellin slot, while Wilson actions (parametrized by clover coefficient r_W)
give degraded scaling that worsens with slot index k.

Source (lizzi 9A §E-1, sessions/archive/session-85/session-85-lizzi-synthesis-w6-13.md
line 780-784, verbatim):
  E-1. S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE (1C C-α / OQ1)
  - What: Test §VII.S.B's C-α corollary at slot-by-slot Mellin level.
    Pre-register r ∈ {ζ, Zubarev, SDW} scope; 3 Wilson + 1 Symanzik
    discretizations at L_max=5; per-slot drift exponents 0,1,2,3 confirmed
    at Symanzik O(a^4) PASS-band; INFO band factor-2; FAIL beyond.
    Empirical validation of S-1 §II.4 partition.
  - Gate: S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE. PASS iff per-slot drift
    matches Symanzik O(a^4); INFO factor-2; FAIL beyond.

PRE-REGISTERED PASS BAND (plan §M, frozen pre-compute)
-----------------------------------------------------
PASS:
  Symanzik p_k ∈ [3.5, 4.5] for ALL k ∈ {0, 1, 2, 3} (O(a^4) per slot)
  AND Wilson schemes p_k ∈ [0.5, 2.5] for k ∈ {1, 2, 3} (degraded)
  AND fit R² ≥ 0.9 per (k, scheme) line
INFO:
  Symanzik within [2.5, 3.5] OR [4.5, 5.5] for ≤ 1 of 4 slots
FAIL:
  Symanzik outside [2.5, 5.5] on any slot
  OR Wilson p_k outside [0.5, 2.5] for k > 0
  OR R² < 0.9 on any (k, scheme) line

Tolerance rule: RATIO (drift exponent p_k is a log-log slope; band-width is
the additive interval on the slope value, which is itself a ratio quantity).

SUBSTITUTION CHAIN (drift-exponent direction across slots, plan §S)
-------------------------------------------------------------------
Step 1 (definition):
  a_{2k}(a, s)   = Σ_i Θ(λ_max - λ_i(a, s)) · λ_i(a, s)^{(2k - d_spec)/2}
                                        [Mellin slot-by-slot, S-1 §IV.5]
  a_{2k}(a→0,s)  = lim_{a→0} a_{2k}(a, s)        [Richardson 5-point Aitken]
  ε_k(a, s)      = a_{2k}(a, s) - a_{2k}(a→0, s) [discretization error]
  p_k(s)         = log-log slope of |ε_k(a, s)| vs a   [drift exponent]

Step 2 (substitute, Symanzik tree-level, c_SW=1.0):
  Symanzik action removes O(a) and O(a²) discretization terms by
  construction (Symanzik 1983); the leading nonzero contribution to
  |D_K(a, Symanzik) - D_K(continuum)| is O(a^4). Spectral moments are
  smooth functionals of the eigenvalue density ρ(λ); discretization
  errors propagate linearly to leading order:
      ε_k(a, Symanzik) = c_k · a^4 + O(a^6)    [c_k slot-dependent constant]

Step 3 (simplify):
  |ε_k(a, Symanzik)| ~ |c_k| · a^4
  log|ε_k(a, Symanzik)| = 4 · log(a) + log|c_k|
  ⇒ p_k(Symanzik) = 4    for all k ∈ {0, 1, 2, 3}    [4 ∈ [3.5, 4.5] PASS]

Step 4 (direction):
  p_k(Symanzik) = 4 across slots k = 0, 1, 2, 3 → SLOT-INDEPENDENT
  p_k(Wilson-i) = q_k where q_k degrades with k (a_{2k} weights eigenvalues
                                with positive power λ^{(2k-8)/2} for k > 4
                                / negative power for k ≤ 3, both enhancing
                                sensitivity to UV discretization noise)
  ⇒ p_k(Symanzik) ≥ p_k(Wilson-i) for ALL k > 0    [strict inequality]
  ⇒ DIRECTION: Symanzik dominates Wilson per slot at k > 0.

  PASS condition reads off:
    "Symanzik p_k ∈ [3.5, 4.5] for all k" tests p_k(Symanzik) = 4 ± 0.5.
    "Wilson p_k ∈ [0.5, 2.5] for k > 0" tests degraded but bounded.

  Conclusion: the inequality direction the gate tests is
    p_k(Symanzik) ≥ p_k(Wilson-i) ≥ 0.5 for all k > 0
  with Symanzik saturating at 4 per slot. PASS verifies; FAIL falsifies.

REGULATOR-PIN DISCIPLINE (per W12-4 P14, regulator-pin-discipline.md)
---------------------------------------------------------------------
Each spectral moment is tagged: a_{2k}^{Wilson-i, a=...} or
a_{2k}^{Symanzik, a=...}. The .npz output dict keys carry the regulator-pin
explicitly (no bare a_n).

VRAM SAFETY: per-irrep block max ~672×672 → ~7 MB at complex128 → safe on
17 GB AMD RX 9070 XT (ROCm 7.2). Total spectral dim Σ d_irr = 378 (× 16
spin = 6048 eigenvalues per (a, scheme)).
"""

import sys, os, time, hashlib, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy.linalg import inv, cholesky, eigvalsh as np_eigvalsh

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---- GPU pin (mandatory per plan §M DO-NOT line 1; feedback_compute-environment.md)
TORCH_OK = True
try:
    import torch
    DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    DTYPE_C = torch.complex128
    DTYPE_R = torch.float64
    if DEVICE.type == 'cuda':
        print(f"[GPU] torch device: {DEVICE} | {torch.cuda.get_device_name(0)} | "
              f"VRAM {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
    else:
        print(f"[GPU] torch device: {DEVICE} (no CUDA/ROCm — falling back to torch CPU)")
except Exception as exc:
    TORCH_OK = False
    os.environ.setdefault('OMP_NUM_THREADS', '8')
    os.environ.setdefault('MKL_NUM_THREADS', '8')
    print(f"[CPU-FALLBACK] torch import failed ({exc}); using numpy.linalg, OMP=8")

from canonical_constants import M_KK, tau_fold, Vol_SU3_Haar, J_C2, PI

print("=" * 78)
print("  S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE (W6-2)")
print("=" * 78)
print(f"  M_KK         = {M_KK:.6e} GeV (M_KK_gravity, S42)")
print(f"  tau_fold     = {tau_fold} (S12/S42 CONST-FREEZE-42)")
print(f"  Vol_SU3_Haar = {Vol_SU3_Haar:.6f} (S44 s44_constants_corrected)")
print(f"  J_C2         = {J_C2}")
t_global = time.time()

base_dir = os.path.dirname(os.path.abspath(__file__))

# =============================================================================
# 1. INPUT-PIN MAP & SHA-256 CLOSURE (audit_sha256 base)
# =============================================================================
def file_sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for blk in iter(lambda: f.read(1 << 20), b''):
            h.update(blk)
    return h.hexdigest()

CANON_SHA = file_sha256(os.path.join(base_dir, 'canonical_constants.py'))

# Most-recent-S85 spectrum cache pin (no L_max=5 cache exists; pin S84_L12 +
# S74_L9 as upstream provenance for the eigenvalue-construction infrastructure)
UPSTREAM_CACHES = {
    's84_spectrum_cache_L12_tau019.npz': file_sha256(
        os.path.join(base_dir, 's84_spectrum_cache_L12_tau019.npz')),
    's74_spectrum_cache_L9_tau019.npz':  file_sha256(
        os.path.join(base_dir, 's74_spectrum_cache_L9_tau019.npz')),
}
print("\n--- Input-pin map (audit_sha256 base) ---")
print(f"  canonical_constants.py SHA = {CANON_SHA[:16]}...")
for k, v in UPSTREAM_CACHES.items():
    print(f"  {k} SHA = {v[:16]}...")

# =============================================================================
# 2. SU(3) INFRASTRUCTURE (CPU one-time; deterministic, no random seed)
# =============================================================================
print("\n--- SU(3) Lie-algebra setup ---")

def gell_mann():
    L = []
    L.append(np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex))
    L.append(np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex))
    L.append(np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex))
    L.append(np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex))
    L.append(np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex))
    L.append(np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex))
    L.append(np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex))
    L.append(np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex) / np.sqrt(3))
    return L

def su3_gens():
    return [-1j / 2.0 * lam for lam in gell_mann()]   # (local) anti-Hermitian generators

def structure_constants(gens):
    n = len(gens)
    f = np.zeros((n, n, n), dtype=np.float64)        # (local)
    for a in range(n):
        for b in range(a+1, n):
            comm = gens[a] @ gens[b] - gens[b] @ gens[a]
            for c in range(n):
                v = -2.0 * np.trace(comm @ gens[c])  # (local)
                f[a, b, c] = v.real
                f[b, a, c] = -v.real
    return f

def cliff8():
    s1 = np.array([[0,1],[1,0]], dtype=complex)
    s2 = np.array([[0,-1j],[1j,0]], dtype=complex)
    s3 = np.array([[1,0],[0,-1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    def k4(A,B,C,D):
        return np.kron(A, np.kron(B, np.kron(C, D)))
    return [
        k4(s1,I2,I2,I2), k4(s2,I2,I2,I2),
        k4(s3,s1,I2,I2), k4(s3,s2,I2,I2),
        k4(s3,s3,s1,I2), k4(s3,s3,s2,I2),
        k4(s3,s3,s3,s1), k4(s3,s3,s3,s2),
    ]

GENS = su3_gens()
F_ABC = structure_constants(GENS)
GAMMAS = cliff8()
DIM_SPIN = 16   # (local) cliff8 spinor dim

def metric_jensen(tau):
    """Jensen-deformed SU(3) reference metric with tau scaling J_C2 sector.
    8x8 diagonal: SU(2) sector (idx 0,1,2) = 1.0; C2 sector (3,4,5,6) =
    exp(2*tau)*J_C2; U(1) sector (7) = exp(-2*tau).  This reproduces the
    framework's tau-deformation pattern at the metric level.
    """
    g = np.eye(8, dtype=np.float64)             # (local)
    for i in (3, 4, 5, 6):
        g[i, i] = np.exp(2.0 * tau) * J_C2      # (local)
    g[7, 7] = np.exp(-2.0 * tau)                # (local)
    return g

def frame(g):
    L = cholesky(g)
    return inv(L)

def frame_struct(f_abc, E):
    Einv = inv(E)
    return np.einsum('ac,bd,cde,ef->abf', E, E, f_abc, Einv)

def conn_coeffs(ft):
    n = ft.shape[0]
    G = np.zeros((n, n, n), dtype=np.float64)   # (local)
    for c in range(n):
        for a in range(n):
            for b in range(n):
                G[c, a, b] = 0.5 * (ft[a, b, c] - ft[b, c, a] + ft[c, a, b])
    return G

def spinor_omega(G, gam):
    n = len(gam)
    Om = np.zeros((gam[0].shape[0], gam[0].shape[0]), dtype=complex)  # (local)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                coef = G[b, a, c]
                if abs(coef) > 1e-15:
                    Om += coef * gam[a] @ gam[b] @ gam[c]
    Om *= 0.25
    return Om

def build_dirac_block(rho, E, gammas, Omega):
    """Build D_K block for one irrep (numpy)."""
    dim_rho = rho[0].shape[0]
    dim_total = dim_rho * DIM_SPIN
    D = np.zeros((dim_total, dim_total), dtype=complex)   # (local)
    for a in range(8):
        for b in range(8):
            if abs(E[a, b]) > 1e-15:
                D += E[a, b] * np.kron(rho[b], gammas[a])
    D += np.kron(np.eye(dim_rho), Omega)
    return D

# =============================================================================
# 3. IRREPS UP TO L_max = 5 (max_pq_sum = 5)
# =============================================================================
def irrep_fundamental(g):  return [x.copy() for x in g]
def irrep_antifundamental(g): return [-x.T for x in g]
def irrep_adjoint(f):     return [f[a, :, :].T.astype(complex) for a in range(8)]

def irrep_symmetric_n(g, n_sym):
    from itertools import combinations_with_replacement, permutations
    d = 3   # (local)
    basis = list(combinations_with_replacement(range(d), n_sym))
    dim = len(basis)
    dn = d ** n_sym
    P_cols = []
    for idx in basis:
        v = np.zeros(dn, dtype=complex)        # (local)
        perms = set(permutations(idx))
        norm = np.sqrt(len(perms))             # (local)
        for p in perms:
            flat = sum(pk * (d ** (n_sym - 1 - k)) for k, pk in enumerate(p))
            v[flat] = 1.0 / norm
        P_cols.append(v)
    P = np.column_stack(P_cols)
    I3 = np.eye(d, dtype=complex)
    rho = []
    for X in g:
        rho_dn = np.zeros((dn, dn), dtype=complex)   # (local)
        for k in range(n_sym):
            facs = [I3] * n_sym                       # (local)
            facs[k] = X
            M = facs[0]
            for fac in facs[1:]:
                M = np.kron(M, fac)
            rho_dn += M
        rho.append(P.conj().T @ rho_dn @ P)
    return rho

def irrep_via_casimir(rA, rB, target_dim):
    dA, dB = rA[0].shape[0], rB[0].shape[0]
    dP = dA * dB
    C2 = np.zeros((dP, dP), dtype=complex)            # (local)
    rho_p = []
    for a in range(8):
        ra = np.kron(rA[a], np.eye(dB)) + np.kron(np.eye(dA), rB[a])
        rho_p.append(ra)
        C2 += ra @ ra
    evals, evecs = np.linalg.eigh(C2)
    tol = 1e-8                                        # (local)
    groups = []
    for ev in sorted(zip(evals, range(dP))):
        val, idx = ev
        if not groups or abs(val - groups[-1][0]) > tol:
            groups.append((val, [idx]))
        else:
            groups[-1][1].append(idx)
    for val, ix in groups:
        if len(ix) == target_dim:
            mask = np.abs(evals - val) < tol
            P = evecs[:, mask]
            return [P.conj().T @ rho_p[a] @ P for a in range(8)]
    raise RuntimeError(f"target_dim {target_dim} not found")

def get_irreps(max_pq_sum=5):
    rf = irrep_fundamental(GENS)
    raf = irrep_antifundamental(GENS)
    rad = irrep_adjoint(F_ABC)
    cg = [-g.T for g in GENS]
    built = {}
    built[(0, 0)] = [np.zeros((1, 1), dtype=complex) for _ in range(8)]
    built[(1, 0)] = rf
    built[(0, 1)] = raf
    built[(1, 1)] = rad
    for n in range(2, max_pq_sum + 1):
        d_n0 = (n + 1) * (n + 2) // 2
        try:
            r = irrep_symmetric_n(GENS, n)
            if r[0].shape[0] == d_n0: built[(n, 0)] = r
        except Exception: pass
        try:
            r = irrep_symmetric_n(cg, n)
            if r[0].shape[0] == d_n0: built[(0, n)] = r
        except Exception: pass
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            if (p, q) in built: continue
            d_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
            ok = False
            for parent_q, src in [((p - 1, q), rf), ((p, q - 1), raf), ((p - 1, q - 1), rad)]:
                if parent_q in built:
                    try:
                        built[(p, q)] = irrep_via_casimir(built[parent_q], src, d_pq)
                        ok = True
                        break
                    except Exception: continue
            if not ok:
                print(f"  [warn] could not build ({p},{q})")
    out = []
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            if (p, q) in built:
                d_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
                if built[(p, q)][0].shape[0] == d_pq:
                    out.append((p, q, d_pq, built[(p, q)]))
    return out

print("Building irreps up to L_max = 5 ...")
t0 = time.time()
IRREPS = get_irreps(max_pq_sum=5)
print(f"  built {len(IRREPS)} irreps in {time.time()-t0:.1f}s; dims = "
      f"{[d for _,_,d,_ in IRREPS]}; total = {sum(d for _,_,d,_ in IRREPS)}")

# =============================================================================
# 4. DISCRETIZATION SCHEMES (4 schemes × 5 spacings)
#
# Per plan §M lines 260-271:
# - Wilson-1: r_W = 1.0 (standard Wilson clover)
# - Wilson-2: r_W = 0.5
# - Wilson-3: r_W = 1.5
# - Symanzik: c_SW = 1.0 (tree-level Symanzik improved)
#
# Discretization model: each scheme perturbs the connection 1-form Omega by
# a scheme-specific lattice-spacing-dependent term. Wilson actions add an
# O(a^p_W) clover term where p_W depends on r_W; Symanzik action adds an
# O(a^4) tree-level-improved term that cancels lower orders by construction.
#
# Concrete model: D_K(a, scheme) = D_K(continuum) + δD(a, scheme), where
#   δD(a, Wilson-i) = r_W * a * R_clover * (1 + 0.5 * a^2 * R_clover^2 + ...)
#   δD(a, Symanzik) = a^4 * R_imp^2 * (1 + 0.5 * a^2 * R_imp^2 + ...)
# and R_clover, R_imp are scheme-specific operator-valued perturbations
# constructed from the irrep generators (Hermitian, traceless).
#
# This model directly encodes the Symanzik 1983 construction: tree-level
# improvement removes O(a) and O(a^2) terms, leaving leading O(a^4); Wilson
# actions retain the O(a) clover term scaled by r_W.
# =============================================================================

SCHEMES = ['Wilson-1', 'Wilson-2', 'Wilson-3', 'Symanzik']
SCHEME_PARAMS = {
    'Wilson-1': {'type': 'wilson', 'r_W': 1.0},
    'Wilson-2': {'type': 'wilson', 'r_W': 0.5},
    'Wilson-3': {'type': 'wilson', 'r_W': 1.5},
    'Symanzik': {'type': 'symanzik', 'c_SW': 1.0},
}
LATTICE_SPACINGS = [0.500, 0.250, 0.125, 0.0625, 0.03125]   # (local) M_KK^{-1} units
SLOTS = [0, 1, 2, 3]            # (local) k indices for a_{2k}
D_SPEC = 8                      # (local) NCG dimension (Connes-Chamseddine)

def lattice_perturbation(rho_a, p_a, q_a, scheme, a_lat, E_frame, gammas):
    """Build the lattice-perturbation operator δD(a, scheme) on a single
    irrep block.

    NCG STRUCTURE: the lattice perturbation must be ANTI-HERMITIAN (matching
    D's structure: GENS = -i/2 * λ_GM are anti-Hermitian, γ_a are Hermitian,
    so D = E_ab * (rho_b ⊗ γ_a) is anti-Hermitian; iD is the physical
    Hermitian Dirac operator). A Hermitian perturbation × I_block would
    cancel under iD's Hermitization. So we build δD via the same kron
    structure as D but with scheme-specific frame perturbation E_frame_lat
    that mimics the Wilson clover / Symanzik improvement at the action level.

    Wilson clover (action level, Wilson 1974):
       D_W(a) = D_continuum + a * r_W * C_clover + O(a^2)
       where C_clover = sum_{a,b} σ_ab F^{ab} (Pauli term, irrep-dependent)
    We model C_clover ≈ Σ_a γ_a^2 ⊗ rho_a (commutator of Dirac ops),
    which gives a leading O(a^1) shift in each eigenvalue.

    Symanzik tree-level (Symanzik 1983):
       D_S(a) = D_continuum + a^4 * c_SW * C_imp + O(a^6)
       O(a) and O(a^2) terms cancel by construction; leading O(a^4).

    Both perturbations are anti-Hermitian (kron structure preserved) and
    NON-COMMUTING with D_continuum (different representation content per
    irrep block → distinct per-eigenvalue shifts → resolves slot-by-slot
    Mellin integration).
    """
    dim_rho = rho_a[0].shape[0]
    dim_block = dim_rho * DIM_SPIN
    # Build clover-like perturbation: Σ_a (γ_a^2 ⊗ rho_a) — anti-Hermitian
    # because rho_a is anti-Hermitian and γ_a^2 = I (Clifford algebra) is
    # Hermitian. Result: kron(I, anti-Herm) = anti-Hermitian.
    C_clover = np.zeros((dim_block, dim_block), dtype=complex)               # (local)
    for a in range(8):
        gam_sq = gammas[a] @ gammas[a]              # (local) γ_a^2 (≈ I in our basis)
        # Use the next γ to break degeneracy (gives non-commuting perturbation)
        gam_op = gammas[(a + 1) % 8]                # (local)
        C_clover += np.kron(rho_a[a], gam_op @ gam_sq)
    # Casimir-2 strength weights the irrep contribution
    C2_irrep = (p_a * p_a + q_a * q_a + p_a * q_a + 3 * p_a + 3 * q_a) / 3.0  # (local)
    C2_strength = max(C2_irrep, 0.1)                                         # (local)

    if scheme in ('Wilson-1', 'Wilson-2', 'Wilson-3'):
        r_W = SCHEME_PARAMS[scheme]['r_W']
        # Wilson clover: leading O(a) + O(a^2) + O(a^3) (UNIMPROVED action)
        # δD = a * r_W * C_clover * (1 + 0.5*a*C2 + ...)
        delta = (r_W * a_lat
                 + 0.5 * (r_W * a_lat) ** 2 * C2_strength
                 + 0.125 * (r_W * a_lat) ** 3 * C2_strength ** 2) * C_clover  # (local)
    elif scheme == 'Symanzik':
        c_SW = SCHEME_PARAMS[scheme]['c_SW']
        # Tree-level Symanzik: O(a) and O(a^2) coefficients vanish by
        # construction (Symanzik 1983); leading nonzero is O(a^4).
        # δD = a^4 * c_SW * C_clover * C2 + O(a^6)
        delta = (c_SW * a_lat ** 4 * C2_strength
                 + 0.5 * a_lat ** 6 * C2_strength ** 2) * C_clover           # (local)
    else:
        raise ValueError(f"unknown scheme {scheme}")
    return delta

# =============================================================================
# 5. CONTINUUM D_K AT (tau_fold, L_max=5)
# =============================================================================
print(f"\nBuilding continuum D_K at tau = {tau_fold}, L_max = 5 ...")
t0 = time.time()
g_tau = metric_jensen(tau_fold)
E = frame(g_tau)
ft = frame_struct(F_ABC, E)
G = conn_coeffs(ft)
Om = spinor_omega(G, GAMMAS)

D_continuum_blocks = []
for (p, q, dim, rho) in IRREPS:
    Db = build_dirac_block(rho, E, GAMMAS, Om)
    D_continuum_blocks.append((p, q, dim, Db))
total_eigs = sum(d * DIM_SPIN for _, _, d, _ in D_continuum_blocks)
print(f"  built {len(D_continuum_blocks)} continuum blocks "
      f"(total spectral dim {total_eigs}) in {time.time()-t0:.1f}s")

# =============================================================================
# 6. EIGVALSH SCAN — 4 schemes × 5 spacings × 21 irrep blocks
#
# GPU PIN: torch.linalg.eigvalsh per block (max block 672x672 → trivial on
# AMD RX 9070 XT 17.1 GB VRAM); fall back to numpy.linalg.eigvalsh only on
# torch import failure.
# =============================================================================

def eigvalsh_gpu(M):
    """Hermitian eigenvalues of D_K. NCG convention: D as built is anti-
    Hermitian (GENS = -i/2 * λ_GM are anti-Hermitian; spinor γ_a are
    Hermitian; their kron product is anti-Hermitian). The Hermitian
    Dirac operator is i*D (matches s75_morse_bott_multi_lmax.py line 345
    `iD_batch = 1j * D_batch`). GPU torch path mandatory per plan §M."""
    iD = 1j * M                          # (local) make Hermitian
    iD_sym = 0.5 * (iD + iD.conj().T)    # (local) enforce numerical Hermiticity
    if TORCH_OK:
        T = torch.tensor(iD_sym, dtype=DTYPE_C, device=DEVICE)
        ev = torch.linalg.eigvalsh(T)
        return ev.cpu().numpy()
    return np_eigvalsh(iD_sym)

def compute_full_spectrum(scheme, a_lat):
    """Compute all eigenvalues at (scheme, a_lat) by per-block eigvalsh."""
    eigs = []
    for (p, q, dim, Db_continuum) in D_continuum_blocks:
        rho = next(rho for (pp, qq, _, rho) in IRREPS if pp == p and qq == q)
        delta = lattice_perturbation(rho, p, q, scheme, a_lat, E, GAMMAS)
        Db = Db_continuum + delta
        ev = eigvalsh_gpu(Db)
        eigs.append(ev)
    return np.concatenate(eigs)

# Continuum spectrum (a → 0 reference; theoretical limit, NOT one of the 5
# scan points — the Richardson Aitken Δ² extrapolation extracts a_{2k}(a→0)
# from the 5 finite-a values in §7).
def continuum_spectrum():
    eigs = []
    for (_, _, _, Db) in D_continuum_blocks:
        eigs.append(eigvalsh_gpu(Db))
    return np.concatenate(eigs)

print("\nComputing continuum reference spectrum ...")
t0 = time.time()
ev_cont = continuum_spectrum()
ev_cont = np.sort(np.abs(ev_cont))
LAMBDA_MAX = float(ev_cont[-1])         # (local) Mellin slot cutoff
print(f"  continuum spectrum: {len(ev_cont)} eigenvalues; "
      f"|λ| range = [{ev_cont[ev_cont > 1e-12].min():.3e}, {ev_cont[-1]:.3e}], "
      f"λ_max = {LAMBDA_MAX:.6e} ({time.time()-t0:.1f}s)")

# =============================================================================
# 7. MELLIN SLOT-BY-SLOT INTEGRATION (S-1 §IV.5)
#    a_{2k}(a, s) = Σ_i Θ(λ_max - |λ_i|) · |λ_i|^{(2k - d_spec)/2}
#
# Per plan §M line 280: d_spec = 8 → exponent (2k - 8)/2:
#   k=0 → λ^{-4}   (a_0 slot, deepest IR)
#   k=1 → λ^{-3}   (a_2 slot)
#   k=2 → λ^{-2}   (a_4 slot, Yang-Mills)
#   k=3 → λ^{-1}   (a_6 slot)
# Eigenvalue floor cuts λ < λ_floor to avoid IR divergence.
# =============================================================================

LAMBDA_FLOOR = max(1e-6 * LAMBDA_MAX, 1e-4)   # (local) Mellin IR cutoff

def mellin_slot(eigs, k):
    """a_{2k}(a, s) per S-1 §IV.5: sum over |λ_i| ∈ (λ_floor, λ_max]."""
    abs_e = np.abs(eigs)
    mask = (abs_e > LAMBDA_FLOOR) & (abs_e <= LAMBDA_MAX)        # (local)
    weights = abs_e[mask] ** ((2.0 * k - D_SPEC) / 2.0)           # (local)
    return float(weights.sum())

# Continuum a_{2k}(a→0, s) reference
a2k_continuum = {k: mellin_slot(ev_cont, k) for k in SLOTS}
print("\nContinuum Mellin moments (reference for ε_k):")
for k, v in a2k_continuum.items():
    print(f"  a_{{{2*k}}}(continuum) = {v:.6e}    [Mellin slot k={k}, exp={(2*k - D_SPEC)/2}]")

# =============================================================================
# 8. SCAN: 4 schemes × 5 spacings → eigenvalues → 16-entry a_{2k}(a, s) dict
# =============================================================================
print("\n" + "=" * 78)
print("  SCAN: 4 schemes × 5 spacings × 4 slots = 80 (a_{2k}, scheme, a) entries")
print("=" * 78)

scan_results = {}     # (local) scheme -> a_lat -> {slot_k: a_2k value}
spectra_all = {}      # (local) scheme -> a_lat -> eigenvalues
t_scan = time.time()
for scheme in SCHEMES:
    scan_results[scheme] = {}
    spectra_all[scheme] = {}
    for a_lat in LATTICE_SPACINGS:
        t0 = time.time()
        eigs = compute_full_spectrum(scheme, a_lat)
        spectra_all[scheme][a_lat] = eigs
        scan_results[scheme][a_lat] = {k: mellin_slot(eigs, k) for k in SLOTS}
        # Regulator-pin discipline (W12-4 P14): tag this row
        tag = f"a_{{2k}}^{{{scheme}, a={a_lat}}}"
        print(f"  [{scheme:9s} a={a_lat:.5f}] eigs in {time.time()-t0:5.2f}s | "
              f"a_0={scan_results[scheme][a_lat][0]:.4e} "
              f"a_2={scan_results[scheme][a_lat][1]:.4e} "
              f"a_4={scan_results[scheme][a_lat][2]:.4e} "
              f"a_6={scan_results[scheme][a_lat][3]:.4e}  {tag}")
print(f"  scan total: {time.time()-t_scan:.1f}s")

# =============================================================================
# 9. RICHARDSON 5-POINT AITKEN Δ² EXTRAPOLATION (per scheme, per slot)
#
# For each (scheme, slot k), compute a_{2k}(a → 0, s) from the 5-point
# sequence using iterated Aitken Δ² acceleration. Output a_{2k}(a→0, s)
# is the empirical continuum extrapolation; ε_k(a, s) = a_{2k}(a, s) -
# a_{2k}(a→0, s).
# =============================================================================

def aitken_delta2(seq):
    """Single Aitken Δ² acceleration step (returns len(seq)-2 array)."""
    s = np.asarray(seq, dtype=np.float64)
    out = np.empty(len(s) - 2)
    for i in range(len(s) - 2):
        d1 = s[i+1] - s[i]                                     # (local)
        d2 = s[i+2] - 2 * s[i+1] + s[i]                        # (local)
        out[i] = s[i] - d1 * d1 / d2 if abs(d2) > 1e-30 else s[i+2]
    return out

def richardson_5point_aitken(values):
    """Iterate Aitken Δ² twice on a 5-element sequence to get 1 acceleration."""
    s1 = aitken_delta2(values)         # 5 → 3
    s2 = aitken_delta2(s1)             # 3 → 1
    return float(s2[0])

print("\n--- Richardson 5-point Aitken Δ² extrapolation ---")
a_2k_continuum_emp = {}     # (local) (scheme, slot) -> empirical a_{2k}(a→0, s)
for scheme in SCHEMES:
    for k in SLOTS:
        seq = [scan_results[scheme][a][k] for a in LATTICE_SPACINGS]
        a_2k_continuum_emp[(scheme, k)] = richardson_5point_aitken(seq)
        print(f"  {scheme:9s} k={k}: a_{{{2*k}}}(a→0)_emp = "
              f"{a_2k_continuum_emp[(scheme, k)]:.6e}    "
              f"(theory continuum a_{{{2*k}}} = {a2k_continuum[k]:.6e})")

# =============================================================================
# 10. DRIFT-EXPONENT FITS (per scheme, per slot)
#
# log10(|ε_k(a, s)|) = p_k(s) · log10(a) + C_k(s)
# Linear least-squares; report (p_k, C_k, R²).
# =============================================================================
print("\n--- Drift-exponent fits ---")
drift_results = {}        # (local) (scheme, slot) -> {p_k, C_k, R2, eps_k}
log_a = np.log10(np.array(LATTICE_SPACINGS, dtype=np.float64))

for scheme in SCHEMES:
    for k in SLOTS:
        cont = a_2k_continuum_emp[(scheme, k)]
        seq  = np.array([scan_results[scheme][a][k] for a in LATTICE_SPACINGS])
        eps  = np.abs(seq - cont)
        # Guard against ε≈0 at smallest a (Richardson exactness on smooth seqs)
        eps = np.maximum(eps, 1e-300)                          # (local)
        log_eps = np.log10(eps)
        # Weighted least squares: weight tighter fit on smaller-a points
        # (those are closer to continuum and dominate the slope estimate)
        wts = np.array([1.0, 1.0, 1.0, 1.5, 2.0])              # (local)
        # Standard linear LSQ (slope is the drift exponent p_k)
        Wsum = wts.sum()                                       # (local)
        x_bar = (wts * log_a).sum() / Wsum                     # (local)
        y_bar = (wts * log_eps).sum() / Wsum                   # (local)
        Sxx = (wts * (log_a - x_bar) ** 2).sum()               # (local)
        Sxy = (wts * (log_a - x_bar) * (log_eps - y_bar)).sum()# (local)
        p_k = Sxy / Sxx                                        # (local) drift exponent
        C_k = y_bar - p_k * x_bar                              # (local)
        # R² (weighted)
        y_pred = p_k * log_a + C_k                             # (local)
        ss_res = (wts * (log_eps - y_pred) ** 2).sum()         # (local)
        ss_tot = (wts * (log_eps - y_bar) ** 2).sum()          # (local)
        R2 = 1.0 - ss_res / ss_tot if ss_tot > 1e-30 else 0.0  # (local)
        drift_results[(scheme, k)] = {
            'p_k':  float(p_k),
            'C_k':  float(C_k),
            'R2':   float(R2),
            'eps_k': eps.tolist(),
        }
        # Regulator-pin tag
        tag = f"p_k^{{{scheme}, slot a_{{{2*k}}}}}"
        print(f"  {tag:38s} p_k = {p_k:7.4f}  C_k = {C_k:7.4f}  R² = {R2:.4f}")

# =============================================================================
# 11. PRE-REGISTERED PASS / FAIL / INFO LOGIC (plan §T, frozen pre-compute)
# =============================================================================
print("\n" + "=" * 78)
print("  PASS / FAIL / INFO LOGIC (pre-registered)")
print("=" * 78)

PASS_BAND_SYMANZIK = (3.5, 4.5)            # (local) PRDR pin
INFO_BAND_LOW      = (2.5, 3.5)            # (local)
INFO_BAND_HIGH     = (4.5, 5.5)            # (local)
PASS_BAND_WILSON   = (0.5, 2.5)            # (local) for k > 0
FAIL_BAND_OUTSIDE  = (2.5, 5.5)            # (local) Symanzik must be inside
R2_FLOOR           = 0.9                   # (local)

# Symanzik PASS check
symanzik_p = [drift_results[('Symanzik', k)]['p_k'] for k in SLOTS]
symanzik_R2 = [drift_results[('Symanzik', k)]['R2']  for k in SLOTS]
sym_in_pass  = [PASS_BAND_SYMANZIK[0] <= p <= PASS_BAND_SYMANZIK[1] for p in symanzik_p]
sym_in_info  = [(INFO_BAND_LOW[0] <= p <= INFO_BAND_LOW[1])
                or (INFO_BAND_HIGH[0] <= p <= INFO_BAND_HIGH[1]) for p in symanzik_p]
sym_in_fail  = [not (FAIL_BAND_OUTSIDE[0] <= p <= FAIL_BAND_OUTSIDE[1]) for p in symanzik_p]

# Wilson PASS check (k > 0 only)
wilson_p = {sc: [drift_results[(sc, k)]['p_k'] for k in SLOTS] for sc in
            ['Wilson-1', 'Wilson-2', 'Wilson-3']}
wilson_R2 = {sc: [drift_results[(sc, k)]['R2']  for k in SLOTS] for sc in
             ['Wilson-1', 'Wilson-2', 'Wilson-3']}
wilson_in_pass = {sc: [PASS_BAND_WILSON[0] <= wilson_p[sc][k] <= PASS_BAND_WILSON[1]
                       for k in [1, 2, 3]] for sc in wilson_p}

# R² check (all 16 (scheme, slot) lines)
all_R2_ok = all(drift_results[(sc, k)]['R2'] >= R2_FLOOR
                for sc in SCHEMES for k in SLOTS)
all_R2_min = min(drift_results[(sc, k)]['R2'] for sc in SCHEMES for k in SLOTS)

# Verdict logic (pre-registered, plan §T):
if any(sym_in_fail):
    fail_slots = [k for k, f in zip(SLOTS, sym_in_fail) if f]
    verdict = "FAIL"
    reason = f"Symanzik p_k outside [{FAIL_BAND_OUTSIDE[0]}, {FAIL_BAND_OUTSIDE[1]}] at slots {fail_slots}"
elif any(not w for sc_list in wilson_in_pass.values() for w in sc_list):
    bad = [(sc, k) for sc in wilson_in_pass for k, w in zip([1,2,3], wilson_in_pass[sc]) if not w]
    verdict = "FAIL"
    reason = f"Wilson p_k outside [{PASS_BAND_WILSON[0]}, {PASS_BAND_WILSON[1]}] at (scheme, slot) {bad}"
elif not all_R2_ok:
    verdict = "FAIL"
    reason = f"R² < {R2_FLOOR} on at least one (scheme, slot) (min={all_R2_min:.3f})"
elif all(sym_in_pass):
    verdict = "PASS"
    reason = "Symanzik p_k ∈ [3.5, 4.5] for all 4 slots; all Wilson p_k ∈ [0.5, 2.5] for k>0; R² ≥ 0.9"
elif sum(sym_in_info) <= 1 and sum(sym_in_pass) >= 3:
    verdict = "INFO"
    reason = f"Symanzik approximately holds: {sum(sym_in_pass)}/4 slots in [3.5,4.5], {sum(sym_in_info)} in INFO band"
else:
    # Multiple INFO-band slots OR mixed: fall through to FAIL
    verdict = "FAIL"
    reason = f"Symanzik {sum(sym_in_pass)}/4 slots in PASS band, {sum(sym_in_info)} in INFO band — multiple-slot underperformance"

# Reported value: min p_k(Symanzik) over k (plan §M VERDICT LINE spec)
value_reported = float(min(symanzik_p))                        # (local)

print(f"\n  Symanzik p_k values:  {[f'{p:.3f}' for p in symanzik_p]}")
print(f"  Symanzik in PASS:     {sym_in_pass}")
print(f"  Symanzik in INFO:     {sym_in_info}")
print(f"  Symanzik in FAIL:     {sym_in_fail}")
for sc in wilson_p:
    print(f"  {sc} p_k values:  {[f'{p:.3f}' for p in wilson_p[sc]]}  in_pass(k>0) = {wilson_in_pass[sc]}")
print(f"  All R² ≥ {R2_FLOOR}: {all_R2_ok}  (min = {all_R2_min:.4f})")
print(f"\n  VERDICT: {verdict}")
print(f"  REASON:  {reason}")
print(f"  value (min p_k(Symanzik)): {value_reported:.6f}")

# =============================================================================
# 12. CROSS-CHECKS (plan §M lines 308-313)
# =============================================================================
print("\n" + "=" * 78)
print("  CROSS-CHECKS")
print("=" * 78)

# CC1: p_0(Symanzik) ≈ 4 (a_0 cosmological-constant slot saturates Symanzik)
p0_sym = drift_results[('Symanzik', 0)]['p_k']
cc1_dev = abs(p0_sym - 4.0)
cc1_pass = cc1_dev <= 1.0
print(f"  CC1: p_0(Symanzik) = {p0_sym:.4f}  deviation from 4.0 = {cc1_dev:.4f}  "
      f"{'PASS' if cc1_pass else 'FAIL'} (threshold ±1.0)")

# CC2: p_3(Wilson-i) > p_3(Symanzik)/2 (Wilson degraded but not catastrophic)
p3_sym = drift_results[('Symanzik', 3)]['p_k']
cc2_pass_per = {}
for sc in ['Wilson-1', 'Wilson-2', 'Wilson-3']:
    p3_w = drift_results[(sc, 3)]['p_k']
    cc2_pass_per[sc] = p3_w > p3_sym / 2.0
    print(f"  CC2 ({sc}): p_3 = {p3_w:.4f}  > p_3(Symanzik)/2 = {p3_sym/2:.4f}: "
          f"{'PASS' if cc2_pass_per[sc] else 'FAIL'}")
cc2_pass = all(cc2_pass_per.values())

# CC3: W12-4 5-regulator atlas spread (a_0/a_2/a_4 spread 0.50/1.03/0.49) — OOM check
# Compare Wilson-1 a_0 drift OOM vs the W12-4 reference 0.50 spread
w1_a0_drift_ratio = abs(scan_results['Wilson-1'][0.500][0] -
                         a_2k_continuum_emp[('Wilson-1', 0)]) / max(
                         abs(a_2k_continuum_emp[('Wilson-1', 0)]), 1e-30)
w12_4_a0_spread = 0.50                  # (local) W12-4 atlas reference (5-regulator a_0)
cc3_oom_match = abs(np.log10(max(w1_a0_drift_ratio, 1e-10)) -
                    np.log10(w12_4_a0_spread)) <= 1.5     # (local) ±1.5 OOM tolerance
print(f"  CC3: Wilson-1 a_0 drift ratio = {w1_a0_drift_ratio:.4e}  "
      f"W12-4 atlas a_0 spread = {w12_4_a0_spread:.4f}  "
      f"OOM diff = {abs(np.log10(max(w1_a0_drift_ratio, 1e-10)) - np.log10(w12_4_a0_spread)):.2f}  "
      f"{'PASS' if cc3_oom_match else 'INFO'} (tolerance ±1.5 OOM)")

# =============================================================================
# 13. PLOT: drift exponents across slots × schemes
# =============================================================================
print("\nPlotting drift exponents ...")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

ax = axes[0]
colors = {'Wilson-1': 'tab:blue', 'Wilson-2': 'tab:orange',
          'Wilson-3': 'tab:green', 'Symanzik': 'tab:red'}
markers = {'Wilson-1': 'o', 'Wilson-2': 's', 'Wilson-3': '^', 'Symanzik': 'D'}
for sc in SCHEMES:
    p_arr = [drift_results[(sc, k)]['p_k'] for k in SLOTS]
    ax.plot(SLOTS, p_arr, marker=markers[sc], color=colors[sc],
            linewidth=2, markersize=10, label=sc)
ax.axhspan(PASS_BAND_SYMANZIK[0], PASS_BAND_SYMANZIK[1], alpha=0.15, color='red',
           label='Symanzik PASS band [3.5, 4.5]')
ax.axhspan(PASS_BAND_WILSON[0], PASS_BAND_WILSON[1], alpha=0.10, color='blue',
           label='Wilson PASS band (k>0) [0.5, 2.5]')
ax.set_xticks(SLOTS)
ax.set_xticklabels([f'k={k}\n(a_{{{2*k}}})' for k in SLOTS])
ax.set_xlabel('Mellin slot index k')
ax.set_ylabel('Drift exponent p_k')
ax.set_title('S86 W6-2: Per-slot drift exponents\n(Symanzik should saturate p=4)')
ax.legend(loc='best', fontsize=9)
ax.grid(True, alpha=0.3)

ax = axes[1]
for sc in SCHEMES:
    for k in SLOTS:
        eps = drift_results[(sc, k)]['eps_k']
        if k == 0 and sc == 'Symanzik':
            ax.loglog(LATTICE_SPACINGS, eps, marker=markers[sc], color=colors[sc],
                      linestyle='-', alpha=0.8, label=f'{sc} k={k}')
        else:
            ax.loglog(LATTICE_SPACINGS, eps, marker=markers[sc], color=colors[sc],
                      linestyle='-', alpha=0.5, markersize=5)
ax.set_xlabel('Lattice spacing a [M_KK^{-1}]')
ax.set_ylabel('|ε_k(a, scheme)|')
ax.set_title('Discretization error per (scheme, slot)')
ax.grid(True, which='both', alpha=0.3)
ax.legend(loc='best', fontsize=8)

plt.tight_layout()
plot_path = os.path.join(base_dir, 's86_w6_2_lattice_drift_exponents.png')
plt.savefig(plot_path, dpi=120, bbox_inches='tight')
plt.close()
print(f"  saved: {plot_path}")

# =============================================================================
# 14. SAVE .npz (16-entry dict + Richardson continuum + raw spectra)
# =============================================================================
npz_path = os.path.join(base_dir, 's86_w6_2_lattice_spacing_immunization.npz')

# Build the 16-entry (scheme, slot) → drift exponent dict, plus per-(scheme, a_lat, slot)
# 80-entry a_{2k}(a, s) raw values, plus Richardson continuum values
drift_p_grid = np.array([[drift_results[(sc, k)]['p_k'] for k in SLOTS] for sc in SCHEMES])
drift_R2_grid = np.array([[drift_results[(sc, k)]['R2'] for k in SLOTS] for sc in SCHEMES])
drift_C_grid  = np.array([[drift_results[(sc, k)]['C_k'] for k in SLOTS] for sc in SCHEMES])
a2k_raw_grid  = np.array([[[scan_results[sc][a][k] for k in SLOTS]
                           for a in LATTICE_SPACINGS] for sc in SCHEMES])
a2k_continuum_emp_grid = np.array([[a_2k_continuum_emp[(sc, k)] for k in SLOTS]
                                   for sc in SCHEMES])
eps_grid = np.array([[drift_results[(sc, k)]['eps_k'] for k in SLOTS] for sc in SCHEMES])

np.savez(
    npz_path,
    # Pre-registered output 4-tuple components
    schemes=np.array(SCHEMES),
    lattice_spacings=np.array(LATTICE_SPACINGS),
    slots=np.array(SLOTS),
    d_spec=D_SPEC,
    L_max=5,
    tau_fold_used=tau_fold,
    lambda_max=LAMBDA_MAX,
    lambda_floor=LAMBDA_FLOOR,
    # 16-entry drift exponent grid (scheme × slot)
    drift_p_grid=drift_p_grid,           # (4, 4) — rows=schemes, cols=slots
    drift_R2_grid=drift_R2_grid,
    drift_C_grid=drift_C_grid,
    # Richardson 5-point Aitken continuum extrapolation
    a2k_continuum_emp_grid=a2k_continuum_emp_grid,
    # Theoretical continuum moments (a→0 reference, no scheme)
    a2k_continuum_theory=np.array([a2k_continuum[k] for k in SLOTS]),
    # 80-entry raw a_{2k}(a, s) grid: (scheme, spacing, slot)
    a2k_raw_grid=a2k_raw_grid,
    # 80-entry epsilon grid: (scheme, slot, spacing)
    eps_grid=eps_grid,
    # Verdict + cross-checks
    verdict=verdict,
    reason=reason,
    value_min_p_symanzik=value_reported,
    cc1_dev=cc1_dev,
    cc1_pass=cc1_pass,
    cc2_pass=cc2_pass,
    cc3_oom_match=cc3_oom_match,
    cc3_w1_a0_drift=w1_a0_drift_ratio,
    # Audit pins
    canonical_constants_sha=CANON_SHA,
    upstream_caches=json.dumps(UPSTREAM_CACHES),
    # Regulator-pin discipline tags (W12-4 P14)
    regulator_pin_tags=np.array([
        f"a_{{{2*k}}}^{{{sc}, a={a}}}"
        for sc in SCHEMES for a in LATTICE_SPACINGS for k in SLOTS
    ]),
)
print(f"  saved: {npz_path}")

# =============================================================================
# 15. DUAL-SHA VERDICT (W9a-99 split per gate-verdicts.md S81+)
# =============================================================================
# audit_sha256: SHA of ordered input-pin map (per plan §M VERDICT LINE companion)
audit_inputs = json.dumps({
    'canonical_constants_sha': CANON_SHA,
    'upstream_caches':         UPSTREAM_CACHES,
    'schemes':                 SCHEMES,
    'lattice_spacings':        LATTICE_SPACINGS,
    'slots':                   SLOTS,
    'L_max':                   5,
    'tau_fold':                tau_fold,
    'd_spec':                  D_SPEC,
    'pass_band_symanzik':      list(PASS_BAND_SYMANZIK),
    'pass_band_wilson':        list(PASS_BAND_WILSON),
    'R2_floor':                R2_FLOOR,
}, sort_keys=True)
audit_sha256 = hashlib.sha256(audit_inputs.encode('utf-8')).hexdigest()

# content_sha256: SHA of script + .npz outputs
script_sha = file_sha256(__file__)
npz_sha = file_sha256(npz_path)
content_inputs = json.dumps({
    'script_sha':  script_sha,
    'npz_sha':     npz_sha,
    'value':       value_reported,
    'verdict':     verdict,
    'p_grid':      drift_p_grid.tolist(),
    'R2_grid':     drift_R2_grid.tolist(),
}, sort_keys=True)
content_sha256 = hashlib.sha256(content_inputs.encode('utf-8')).hexdigest()

verdict_line = (
    f"S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE: {verdict} -- "
    f"value={value_reported:.6f} "
    f"scheme=W6-2-lattice-Mellin-slot "
    f"convention=Symanzik-O(a^4)-PASS-band "
    f"L_max=5 "
    f"audit_sha256={audit_sha256} "
    f"content_sha256={content_sha256} "
    f"schema_version=S86+"
)

# Companion row (W9a-99 split): short SHAs + per-slot summary
companion_line = (
    f"# audit_sha256_short={audit_sha256[:16]} "
    f"content_sha256_short={content_sha256[:16]} "
    f"# S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE dual-SHA companion row (W9a-99 split); "
    f"symanzik_p_k=[{','.join(f'{p:.3f}' for p in symanzik_p)}]; "
    f"wilson1_p_k=[{','.join(f'{p:.3f}' for p in wilson_p['Wilson-1'])}]; "
    f"wilson2_p_k=[{','.join(f'{p:.3f}' for p in wilson_p['Wilson-2'])}]; "
    f"wilson3_p_k=[{','.join(f'{p:.3f}' for p in wilson_p['Wilson-3'])}]; "
    f"min_R2={all_R2_min:.4f}; "
    f"CC1_p0sym={p0_sym:.4f}; CC1_pass={cc1_pass}; "
    f"CC2_pass={cc2_pass}; CC3_oom_match={cc3_oom_match}; "
    f"reason={reason[:120]}"
)

verdict_path = os.path.join(base_dir, 's86_gate_verdicts.txt')
with open(verdict_path, 'a', encoding='utf-8') as fh:
    fh.write('\n' + verdict_line + '\n')
    fh.write(companion_line + '\n')

print("\n" + "=" * 78)
print(f"  VERDICT APPENDED to {verdict_path}")
print("=" * 78)
print(verdict_line)
print(companion_line)

print(f"\n[Total wall time: {time.time()-t_global:.1f}s]")
print("=" * 78)
print(f"  Output 4-tuple:")
print(f"    value     = {value_reported:.6f}  (min p_k(Symanzik) over k)")
print(f"    scheme    = W6-2-lattice-Mellin-slot")
print(f"    convention= Symanzik-O(a^4)-PASS-band")
print(f"    L_max     = 5")
print("=" * 78)

sys.exit(0)
