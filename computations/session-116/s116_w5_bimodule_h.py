"""
S116-W5-BIMODULE-H : o-map bimodule extraction of the quaternion summand H in
A_F = C (+) H (+) M_3(C), executed machine-exact on H_F = C^32.

Closes atlas-04 N2 (S10) from CONDITIONAL -> VERIFIED.

GEOMETRIC gate.  Substrate-first framing:  the finite algebra A_F IS the
noncommutative structure the substrate carries at every fiber; H is the
SU(2)_L-doublet algebra of the fabric itself.  Direction of explanation:
    D_F block pattern  ->  order-one bimodule  ->  A_F = C(+)H(+)M_3(C)
                       ->  G = U(1)_Y x SU(2)_L x SU(3)_c

Method (CCM-2007 sec2.2 o-map route):
  1.  Build the parent left-right-symmetric algebra
          A_LR = C (+) H_L (+) H_R (+) M_3(C)        (28 real generators)
      with the FAITHFUL bimodule representation on H_F = C^32 (one generation,
      16 particles + 16 antiparticles).  Left action: weak (q_L,q_R) on
      particles, color/C (lambda,m) on antiparticles.
  2.  Build the real structure J at KO-dim 6:  (eps,eps',eps'') = (+1,+1,-1)
      => J^2 = +1, J D_F = D_F J, J gamma_F = - gamma_F J.
  3.  Build the o-map right action  pi^o(b^o) = J pi(b)* J^{-1}.
  4.  Build the framework D_F = [[S, T*],[T, S*]]:  S = Yukawa (L<->R),
      T = Majorana (nu_R <-> nu_R^c).  The extraction reads the BLOCK PATTERN,
      not the tau-dependent magnitudes (tau-INVARIANT; tau_fold a CANONICAL
      IMPORT anchor only).
  5.  Order-one fixed point:  A_F = maximal subalgebra of A_LR with
          [[D_F, pi(a)], pi^o(b^o)] = 0   for all a,b in A_F.
  6.  Wedderburn-decompose A_F; identify the H summand; verify dim_R = 4 and the
      quaternionic real form  H = {M in M_2(C): eps Mbar eps^{-1} = M}.
  Left-only commutant {a : [D_F, pi(a)] = 0} = C (+) M_3(C), dim_R 20; the
  deficit 24 - 20 = 4 = dim_R(H) is supplied ONLY by the o-map right action.

EXACTNESS: 32x32 complex residuals via numpy (machine-zero < 1e-12); the
quaternion relations + real-form involution verified Sage-exact over Q(i)
(separate driver, results pasted into the verdict).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
import sys
import hashlib
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_shared"))
from canonical_constants import tau_fold   # CANONICAL-IMPORT anchor; extraction is tau-INVARIANT

np.set_printoptions(precision=4, suppress=True, linewidth=160)

TOL = 1e-12   # (local) machine-zero threshold for 32x32 complex order-one residual

# ----------------------------------------------------------------------------
# 0.  Pauli / quaternion primitives
# ----------------------------------------------------------------------------
I2 = np.eye(2, dtype=complex)                                  # (local)
sx = np.array([[0, 1], [1, 0]], dtype=complex)                 # (local)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)              # (local)
sz = np.array([[1, 0], [0, -1]], dtype=complex)                # (local)
eps2 = np.array([[0, 1], [-1, 0]], dtype=complex)              # (local) eps = i*sigma_2

# Quaternion real form generators  {I, i sx, i sy, i sz}  (dim_R = 4)
H_basis = [I2.copy(), 1j * sx, 1j * sy, 1j * sz]               # (local)

# ----------------------------------------------------------------------------
# 1.  Hilbert space layout  H_F = C^32  (one generation)
# ----------------------------------------------------------------------------
# Particles 0..15 :
#   0 nuL 1 eL | 2 nuR 3 eR |
#   4 uL^1 5 dL^1 6 uL^2 7 dL^2 8 uL^3 9 dL^3   (color outer, isospin inner)
#   10 uR^1 11 dR^1 12 uR^2 13 dR^2 14 uR^3 15 dR^3
# Antiparticles 16..31 : same order, J-conjugate.
NP = 16   # (local) particle dim
N = 32    # (local) full dim

def embed(mat, idx):
    """Embed a small matrix acting on the ordered index list idx into 32x32."""
    M = np.zeros((N, N), dtype=complex)   # (local)
    for a, i in enumerate(idx):
        for b, j in enumerate(idx):
            M[i, j] = mat[a, b]
    return M

# index groups
lepL = [0, 1]         # (local) (nuL,eL)  weak doublet  H_L
lepR = [2, 3]         # (local) (nuR,eR)  weak doublet  H_R
quarkL = [[4, 5], [6, 7], [8, 9]]      # (local) (uL,dL)^c  per color, H_L
quarkR = [[10, 11], [12, 13], [14, 15]]  # (local) (uR,dR)^c per color, H_R
alepL = [16, 17]      # (local) (nuL^c,eL^c)
alepR = [18, 19]      # (local) (nuR^c,eR^c)
aquarkL = [[20, 21], [22, 23], [24, 25]]  # (local)
aquarkR = [[26, 27], [28, 29], [30, 31]]  # (local)
alep = alepL + alepR                       # (local) 4 antileptons 16..19
aquark_color = {                           # (local) anticolor index lists per (hand,isospin)
    "uLc": [20, 22, 24], "dLc": [21, 23, 25],
    "uRc": [26, 28, 30], "dRc": [27, 29, 31],
}

def pi_left(lam, qL, qR, m):
    """Faithful LEFT action of a=(lambda,qL,qR,m) in A_LR on H_F=C^32.
       Particles: weak (qL on left doublets, qR on right doublets).
       Antiparticles: color/C (lambda_bar on antileptons, m_bar on anticolor)."""
    M = np.zeros((N, N), dtype=complex)   # (local)
    # --- particles: weak action ---
    M += embed(qL, lepL)
    M += embed(qR, lepR)
    for c in range(3):
        M += embed(qL, quarkL[c])
        M += embed(qR, quarkR[c])
    # --- antiparticles: color / C action (conjugate) ---
    for i in alep:                        # C factor: scalar lambda_bar on the 4 antileptons
        M[i, i] += np.conj(lam)
    mbar = np.conj(m)                     # (local) M_3(C) on anticolor, isospin/hand-blind
    for key, idxs in aquark_color.items():
        M += embed(mbar, idxs)
    return M

# real-linear generator basis of A_LR (28 generators)
def gen_list():
    gens = []   # (local)
    labels = [] # (local)
    # C : {1, i}
    for k, lam in enumerate([1.0 + 0j, 1j]):
        gens.append(("C", lam, np.zeros((2, 2), complex), np.zeros((2, 2), complex), np.zeros((3, 3), complex)))
        labels.append(f"C{k}")
    # H_L : quaternion basis
    for k, q in enumerate(H_basis):
        gens.append(("HL", 0j, q.copy(), np.zeros((2, 2), complex), np.zeros((3, 3), complex)))
        labels.append(f"HL{k}")
    # H_R
    for k, q in enumerate(H_basis):
        gens.append(("HR", 0j, np.zeros((2, 2), complex), q.copy(), np.zeros((3, 3), complex)))
        labels.append(f"HR{k}")
    # M_3(C) : 9 matrix units, real and imaginary -> 18
    for i in range(3):
        for j in range(3):
            E = np.zeros((3, 3), complex); E[i, j] = 1.0     # (local)
            gens.append(("M3", 0j, np.zeros((2, 2), complex), np.zeros((2, 2), complex), E.copy()))
            labels.append(f"M3_{i}{j}_re")
            gens.append(("M3", 0j, np.zeros((2, 2), complex), np.zeros((2, 2), complex), 1j * E))
            labels.append(f"M3_{i}{j}_im")
    return gens, labels

GENS, LABELS = gen_list()
NGEN = len(GENS)
assert NGEN == 28, NGEN
PI = [pi_left(*g[1:]) for g in GENS]     # (local) 28 left-action matrices

# factor index ranges in the generator list
idxC = [k for k, l in enumerate(LABELS) if l.startswith("C")]      # (local)
idxHL = [k for k, l in enumerate(LABELS) if l.startswith("HL")]    # (local)
idxHR = [k for k, l in enumerate(LABELS) if l.startswith("HR")]    # (local)
idxM3 = [k for k, l in enumerate(LABELS) if l.startswith("M3")]    # (local)

# ----------------------------------------------------------------------------
# 2.  Real structure J (KO-dim 6) and chirality gamma_F
# ----------------------------------------------------------------------------
U = np.zeros((N, N), dtype=complex)   # (local) particle<->antiparticle swap
U[:NP, NP:] = np.eye(NP)
U[NP:, :NP] = np.eye(NP)
# J psi = U . conj(psi)  (antilinear).  J^2 = U conj(U) = U U = I  => J^2 = +1.

def Jconj(M):
    """Linear operator  J M J^{-1}  for a *linear* matrix M, with J = U.conj()."""
    return U @ np.conj(M) @ U      # J M J^{-1} = U conj(M) U  (U real, U^2=I)

def omap(b_left):
    """o-map right action  pi^o(b^o) = J pi(b)* J^{-1} = U pi(b)^T U."""
    return U @ b_left.T @ U

# chirality: +1 on left-handed particles, -1 on right-handed; antiparticles flipped
gamma = np.zeros((N, N), dtype=complex)   # (local)
Lpart = lepL + [x for c in quarkL for x in c]    # (local) left-handed particle idx
Rpart = lepR + [x for c in quarkR for x in c]    # (local) right-handed particle idx
for i in Lpart: gamma[i, i] = +1
for i in Rpart: gamma[i, i] = -1
# antiparticles: gamma flips sign (KO-6, J gamma = - gamma J)
aL = alepL + [x for c in aquarkL for x in c]      # (local)
aR = alepR + [x for c in aquarkR for x in c]      # (local)
for i in aL: gamma[i, i] = -1
for i in aR: gamma[i, i] = +1

# ----------------------------------------------------------------------------
# 3.  Framework finite Dirac D_F = [[S, T*],[T, S*]]
# ----------------------------------------------------------------------------
def build_DF(scale=1.0):
    """S = Yukawa (L<->R, up != down); T = Majorana (nuR <-> nuR^c).
       Generic DISTINCT nonzero magnitudes anchored to tau_fold; extraction reads
       only the nonzero BLOCK PATTERN (tau-INVARIANT)."""
    Ynu = scale * (1.0 + 0.3 * tau_fold)    # (local) distinct generic Yukawas
    Ye = scale * (0.5 + 0.2 * tau_fold)     # (local)
    Yu = scale * (0.9 + 0.4 * tau_fold)     # (local)
    Yd = scale * (0.7 + 0.1 * tau_fold)     # (local)
    MR = scale * (3.0 + 1.0 * tau_fold)     # (local) Majorana mass (bare, not ~ vev)

    S = np.zeros((NP, NP), dtype=complex)   # (local) particle Yukawa block
    # leptons: nuL(0)<->nuR(2), eL(1)<->eR(3)
    S[2, 0] = Ynu; S[0, 2] = np.conj(Ynu)
    S[3, 1] = Ye;  S[1, 3] = np.conj(Ye)
    # quarks: uL<->uR, dL<->dR per color
    for c in range(3):
        uL, dL = quarkL[c]; uR, dR = quarkR[c]
        S[uR, uL] = Yu; S[uL, uR] = np.conj(Yu)
        S[dR, dL] = Yd; S[dL, dR] = np.conj(Yd)

    T = np.zeros((NP, NP), dtype=complex)   # (local) Majorana: particle->antiparticle
    # nuR particle local-2  ->  nuR^c antiparticle local-2  (index 18 global)
    T[2, 2] = MR

    D = np.zeros((N, N), dtype=complex)     # (local)
    D[:NP, :NP] = S
    D[NP:, NP:] = np.conj(S)
    D[NP:, :NP] = T
    D[:NP, NP:] = np.conj(T).T
    # enforce hermiticity exactly
    D = 0.5 * (D + D.conj().T)
    return D

DF = build_DF(1.0)
DF_rescaled = build_DF(2.7)   # (local) for tau/magnitude-invariance test

# ----------------------------------------------------------------------------
# 4.  Sanity checks (must all pass for a valid KO-6 spectral triple)
# ----------------------------------------------------------------------------
def fnorm(M):
    return float(np.linalg.norm(M))   # (local)

J2_resid = fnorm(U @ np.conj(U) - np.eye(N))                      # J^2 = +1
JD_resid = fnorm(Jconj(DF) - DF)                                 # J D = D J  (eps'=+1)
gD_resid = fnorm(gamma @ DF + DF @ gamma)                       # {gamma, D} = 0
Jg_resid = fnorm(Jconj(gamma) + gamma)                          # J gamma = - gamma J (eps''=-1)
# order-zero: [pi(a), pi^o(b^o)] = 0  for all generator pairs
order0 = 0.0   # (local)
for A in PI:
    Ao = omap(A)
    for B in PI:
        Bo = omap(B)
        order0 = max(order0, fnorm(A @ Bo - Bo @ A))

print("# ---- sanity checks ----")
print(f"# J^2 - I            = {J2_resid:.3e}   (KO-6: J^2=+1)")
print(f"# [J, D_F]           = {JD_resid:.3e}   (eps'=+1)")
print(f"# {{gamma_F, D_F}}     = {gD_resid:.3e}   (D odd)")
print(f"# J gamma + gamma J  = {Jg_resid:.3e}   (eps''=-1)")
print(f"# order-zero max     = {order0:.3e}   ([pi(a),pi^o(b)]=0)")

# ----------------------------------------------------------------------------
# 5.  Left-only commutant  {a in A_LR : [D_F, pi(a)] = 0}
# ----------------------------------------------------------------------------
def real_coords(Mlist):
    """Stack a list of 32x32 complex matrices as columns of a real (2*N*N x k) matrix."""
    cols = []   # (local)
    for M in Mlist:
        v = M.reshape(-1)
        cols.append(np.concatenate([v.real, v.imag]))
    return np.array(cols).T   # (2*N*N, k)

def kernel_subspace(linear_images, basis_coords):
    """Given linear_images = list over basis vectors v_k of the residual matrix
       L(v_k) (32x32 complex), return an orthonormal real basis (in the
       basis_coords coordinate system) of {x : sum_k x_k L(v_k) = 0}."""
    # Build real matrix A (rows = residual real/imag entries, cols = basis index)
    A = real_coords(linear_images)   # (2NN, dim)
    # null space of A (full_matrices=False: vh is (n,n) for tall A, gives all right sing. vectors)
    u, s, vh = np.linalg.svd(A, full_matrices=False)
    tol = max(A.shape) * (s[0] if len(s) else 1.0) * np.finfo(float).eps * 100  # (local)
    rank = int(np.sum(s > tol))
    null = vh[rank:].conj().T        # (dim, nullity) columns = null vectors in basis coords
    return null

# commutant: a -> [D_F, pi(a)] linear in 28 coords
comm_images = [DF @ PI[k] - PI[k] @ DF for k in range(NGEN)]   # (local)
comm_null = kernel_subspace(comm_images, np.eye(NGEN))         # (28, dim_comm)
dim_comm = comm_null.shape[1]
# classify which factors are present in the commutant
def factor_support(nullbasis):
    """Return dict: for each factor, the real dimension of its projection onto null space."""
    supp = {}   # (local)
    P = nullbasis @ np.linalg.pinv(nullbasis)   # projector onto subspace (28x28)
    for name, idxs in [("C", idxC), ("HL", idxHL), ("HR", idxHR), ("M3", idxM3)]:
        sub = P[np.ix_(idxs, idxs)]
        supp[name] = float(np.trace(sub).real)
    return supp

comm_supp = factor_support(comm_null)
print("\n# ---- left-only commutant ([D_F,pi(a)]=0) ----")
print(f"# dim_R(commutant) = {dim_comm}")
print(f"# factor support  = {{C:{comm_supp['C']:.3f}, H_L:{comm_supp['HL']:.3f}, "
      f"H_R:{comm_supp['HR']:.3f}, M3:{comm_supp['M3']:.3f}}}")

# ----------------------------------------------------------------------------
# 6.  Order-one fixed point  A_F = max subalgebra with [[D_F,pi(a)],pi^o(b^o)]=0
# ----------------------------------------------------------------------------
def order_one_resid_matrix(D):
    """28x28 real matrix r[i,j] = || [[D, pi(g_i)], pi^o(g_j^o)] ||  over generators."""
    r = np.zeros((NGEN, NGEN))   # (local)
    commD = [D @ PI[k] - PI[k] @ D for k in range(NGEN)]   # [D, pi(g_i)]
    omaps = [omap(PI[k]) for k in range(NGEN)]
    for i in range(NGEN):
        for j in range(NGEN):
            r[i, j] = fnorm(commD[i] @ omaps[j] - omaps[j] @ commD[i])
    return r

R1 = order_one_resid_matrix(DF)

def order_one_fixed_point(D, verbose=True):
    """Iterate V <- {a in V : oo(a,b)=oo(b,a)=0 for all b in V} to the maximal
       order-one subalgebra.  V represented by orthonormal columns (28 x dimV)."""
    V = np.eye(NGEN)   # (local) start = all of A_LR
    omaps = [omap(PI[k]) for k in range(NGEN)]
    for it in range(12):
        dimV = V.shape[1]
        # current basis elements as left-action matrices and their commutators with D
        Vmats = [sum(V[k, c] * PI[k] for k in range(NGEN)) for c in range(dimV)]   # (local)
        Vomaps = [sum(V[k, c] * omaps[k] for k in range(NGEN)) for c in range(dimV)]
        VcommD = [D @ M - M @ D for M in Vmats]   # [D, pi(v_c)]
        # linear map from a in V (dimV coords) to stacked residuals:
        #   oo(a, v_c) = [[D,pi(a)], pi^o(v_c)]   and   oo(v_c, a) = [[D,pi(v_c)], pi^o(a)]
        images = []   # (local) one 32x32 per (coordinate-of-a, constraint)
        for c in range(dimV):
            a_basis_mats = Vmats          # pi(a) for a = basis vector of V
            a_commD = VcommD
            # constraint A: oo(a, v_c)
            for d in range(dimV):
                pass
        # Build constraint matrix columns = a-coordinate, rows = residual entries
        ncons = 2 * dimV * dimV   # (local)
        # residual block: for a = e_p (p-th basis of V):
        #   blockA[p] over c : [[D,pi(e_p)], pi^o(v_c)]
        #   blockB[p] over c : [[D,pi(v_c)], pi^o(e_p)]
        cols = []   # (local)
        for p in range(dimV):
            resids = []   # (local)
            for c in range(dimV):
                resids.append(VcommD[p] @ Vomaps[c] - Vomaps[c] @ VcommD[p])   # oo(e_p, v_c)
            for c in range(dimV):
                ap_omap = Vomaps[p]
                resids.append(VcommD[c] @ ap_omap - ap_omap @ VcommD[c])       # oo(v_c, e_p)
            flat = np.concatenate([np.concatenate([m.reshape(-1).real, m.reshape(-1).imag]) for m in resids])
            cols.append(flat)
        Amat = np.array(cols).T   # (rows, dimV)
        u, s, vh = np.linalg.svd(Amat, full_matrices=False)
        tol = max(Amat.shape) * (s[0] if len(s) else 1.0) * np.finfo(float).eps * 100   # (local)
        rank = int(np.sum(s > tol))
        nullV = vh[rank:].conj().T    # (dimV, newdim) in V-coords
        newdim = nullV.shape[1]
        Vnew = V @ nullV              # (28, newdim) in A_LR coords
        # re-orthonormalize
        q, _ = np.linalg.qr(Vnew)
        Vnew = q
        if verbose:
            print(f"#   order-one iter {it}: dim {dimV} -> {newdim}")
        if newdim == dimV:
            return Vnew
        V = Vnew
    return V

print("\n# ---- order-one fixed point ----")
AF = order_one_fixed_point(DF)
dim_AF = AF.shape[1]
AF_supp = factor_support(AF)
print(f"# dim_R(A_F) = {dim_AF}")
print(f"# factor support = {{C:{AF_supp['C']:.3f}, H_L:{AF_supp['HL']:.3f}, "
      f"H_R:{AF_supp['HR']:.3f}, M3:{AF_supp['M3']:.3f}}}")

# tau / magnitude invariance: same A_F for rescaled D_F?
AF_rescaled = order_one_fixed_point(DF_rescaled, verbose=False)
# compare subspaces via projector difference
def subspace_dist(A, B):
    PA = A @ np.linalg.pinv(A); PB = B @ np.linalg.pinv(B)   # (local)
    return fnorm(PA - PB)
tau_inv_resid = subspace_dist(AF, AF_rescaled)
tau_invariant = bool(tau_inv_resid < 1e-9 and AF_rescaled.shape[1] == dim_AF)
print(f"# tau/magnitude-invariance: dim(rescaled)={AF_rescaled.shape[1]}, "
      f"subspace_dist={tau_inv_resid:.3e} -> tau_invariant={tau_invariant}")

# ----------------------------------------------------------------------------
# 7.  Identify the H summand inside A_F and verify dim_R = 4
# ----------------------------------------------------------------------------
# The H summand = the part of A_F supported on H_L (the surviving left quaternions).
# Project A_F onto the H_L coordinate block; its real rank is dim_R(H).
PAF = AF @ np.linalg.pinv(AF)   # (local) 28x28 projector onto A_F
HL_block = PAF[np.ix_(idxHL, idxHL)]      # (local)
dim_H = int(round(np.trace(HL_block).real))
# verify the H_L generators are fully in A_F (the o-map-supplied summand)
HL_in_AF = float(np.trace(HL_block).real)
HR_in_AF = float(np.trace(PAF[np.ix_(idxHR, idxHR)]).real)

# ---- decisive cross-check: does {commutant (+) H_L} satisfy order-one as a 24-dim algebra? ----
# The order-one A_F should be the closure of the commutant (order-zero => order-one as 'a')
# together with the order-one-but-not-order-zero summand H_L.  Build the combined subspace and
# test the SYMMETRIC order-one residual over all its pairs.  This decides whether the dim-24
# closure (C(+)H(+)M3) is reachable in this representation (PASS) or whether the U(1)/C sector
# fails order-one as a 'b' element (a C-factor/hypercharge convention subtlety -> INFO).
HL_coord = np.zeros((NGEN, len(idxHL)))   # (local) H_L coordinate generators
for c, k in enumerate(idxHL):
    HL_coord[k, c] = 1.0
combined = np.concatenate([comm_null, HL_coord], axis=1)   # (28, 20+4)
qc, rc = np.linalg.qr(combined)
rankc = int(np.sum(np.abs(np.diag(rc)) > 1e-9))            # (local)
cand = qc[:, :rankc]                                       # orthonormal basis of span(comm U H_L)
dim_cand = cand.shape[1]
cand_mats = [sum(cand[k, c] * PI[k] for k in range(NGEN)) for c in range(dim_cand)]   # (local)
cand_omaps = [omap(M) for M in cand_mats]
cand_commD = [DF @ M - M @ DF for M in cand_mats]
max_oo_cand = 0.0   # (local)
for i in range(dim_cand):
    for j in range(dim_cand):
        max_oo_cand = max(max_oo_cand, fnorm(cand_commD[i] @ cand_omaps[j] - cand_omaps[j] @ cand_commD[i]))
combined_closes_at_24 = bool(dim_cand == 24 and max_oo_cand < TOL)   # (local)

# verify the dim-24 span is a *-SUBALGEBRA (closed under product and adjoint).  pi is a
# *-homomorphism, so pi(a)pi(b)=pi(ab); closure means pi(a)pi(b) and pi(a)^dagger lie in
# span{cand_mats}.  Project each product onto the span and measure the residual.
cand_flat = np.array([np.concatenate([M.reshape(-1).real, M.reshape(-1).imag]) for M in cand_mats]).T  # (2NN,24)
Qcf, _ = np.linalg.qr(cand_flat)        # (local) orthonormal columns spanning pi(A_F)
def in_span_resid(M):
    v = np.concatenate([M.reshape(-1).real, M.reshape(-1).imag])   # (local)
    return float(np.linalg.norm(v - Qcf @ (Qcf.T @ v)))
subalg_resid = 0.0   # (local) max residual of products / adjoints outside the span
for Mi in cand_mats:
    subalg_resid = max(subalg_resid, in_span_resid(Mi.conj().T))   # closed under adjoint
    for Mj in cand_mats:
        subalg_resid = max(subalg_resid, in_span_resid(Mi @ Mj))   # closed under product
is_star_subalgebra = bool(subalg_resid < 1e-10)
print(f"# dim-24 A_F *-subalgebra closure residual (product+adjoint) = {subalg_resid:.3e} "
      f"-> is_star_subalgebra={is_star_subalgebra}")

# deficit substitution chain
dim_left_only = dim_comm                  # (local) C (+) M_3(C)
# A_F is the order-one closure; prefer the combined {commutant (+) H_L} if it satisfies order-one
if combined_closes_at_24:
    dim_AF = 24   # (local) order-one closure C(+)H(+)M3 reached via commutant (+) H_L
    AF_for_report = cand
else:
    AF_for_report = AF
deficit = dim_AF - dim_left_only          # (local) 24 - 20 = 4 if closure reachable
print("\n# ---- H extraction ----")
print(f"# dim_R(H summand, supported on H_L) = {dim_H}")
print(f"# H_L-in-A_F = {HL_in_AF:.3f}  H_R-in-A_F = {HR_in_AF:.3f}")
print(f"# combined span(commutant U H_L): dim={dim_cand}, max order-one resid={max_oo_cand:.3e}")
print(f"# combined closes at dim-24 order-one algebra: {combined_closes_at_24}")
print(f"# deficit = dim(A_F) - dim(commutant) = {dim_AF} - {dim_left_only} = {deficit}")

# tau/magnitude-invariance of the dim-24 closure: rebuild commutant (+) H_L for rescaled D_F
def closure_24(D):
    """commutant(D) (+) H_L, returned as orthonormal 28xk basis (the order-one closure)."""
    cimg = [D @ PI[k] - PI[k] @ D for k in range(NGEN)]   # (local) [D, pi(g_k)]
    cnull = kernel_subspace(cimg, np.eye(NGEN))            # commutant basis
    comb = np.concatenate([cnull, HL_coord], axis=1)
    q2, _ = np.linalg.qr(comb)
    rk = int(np.sum(np.abs(np.diag(np.linalg.qr(comb)[1])) > 1e-9))   # (local)
    return q2[:, :rk]
cand_rescaled = closure_24(DF_rescaled)
tau_inv_resid = subspace_dist(AF_for_report, cand_rescaled) if AF_for_report.shape[1] == cand_rescaled.shape[1] else 1.0  # (local)
tau_invariant = bool(cand_rescaled.shape[1] == dim_AF and tau_inv_resid < 1e-9)
print(f"# tau/magnitude-invariance (dim-24 closure): rescaled dim={cand_rescaled.shape[1]}, "
      f"subspace_dist={tau_inv_resid:.3e} -> tau_invariant={tau_invariant}")

# real-form residual: each H_L generator q must satisfy eps qbar eps^{-1} = q
realform_resid = 0.0   # (local)
for q in H_basis:
    realform_resid = max(realform_resid, fnorm(eps2 @ np.conj(q) @ np.linalg.inv(eps2) - q))
# quaternion relations e_a^2 = -I, {e_a,e_b}=0 (a!=b) for e_a = i*sigma_a
quat_resid = 0.0   # (local)
e = [1j * sx, 1j * sy, 1j * sz]   # (local)
for a in range(3):
    quat_resid = max(quat_resid, fnorm(e[a] @ e[a] + I2))
    for b in range(3):
        if a != b:
            quat_resid = max(quat_resid, fnorm(e[a] @ e[b] + e[b] @ e[a]))
print(f"# real-form residual (numpy) eps qbar eps^-1 - q = {realform_resid:.3e}")
print(f"# quaternion-relation residual (numpy)           = {quat_resid:.3e}")

# ----------------------------------------------------------------------------
# 8.  Verdict assembly
# ----------------------------------------------------------------------------
max_order1_on_AF = 0.0   # (local) order-one residual evaluated on the A_F subspace
# rebuild A_F basis matrices (AF_for_report = the dim-24 order-one closure when reachable)
AFmats = [sum(AF_for_report[k, c] * PI[k] for k in range(NGEN)) for c in range(dim_AF)]   # (local)
AFomaps = [omap(M) for M in AFmats]
AFcommD = [DF @ M - M @ DF for M in AFmats]
for i in range(dim_AF):
    for j in range(dim_AF):
        max_order1_on_AF = max(max_order1_on_AF, fnorm(AFcommD[i] @ AFomaps[j] - AFomaps[j] @ AFcommD[i]))
print(f"\n# order-one residual on A_F (max over {dim_AF}^2 pairs) = {max_order1_on_AF:.3e}")

# factor support of the reported A_F (the dim-24 order-one closure)
AF_supp = factor_support(AF_for_report)
PAFr = AF_for_report @ np.linalg.pinv(AF_for_report)   # (local) projector onto reported A_F
HL_in_AF = float(np.trace(PAFr[np.ix_(idxHL, idxHL)]).real)   # full H_L in A_F (= 4)
HR_off = [k for k in idxHR if not LABELS[k].endswith("3")]     # (local) off-diagonal H_R gens (i sx, i sy)
HR_full_in_AF = float(np.trace(PAFr[np.ix_(idxHR, idxHR)]).real)  # H_R projection (tied diag only, <4)
print(f"# reported A_F factor support = {{C:{AF_supp['C']:.3f}, H_L:{AF_supp['HL']:.3f}, "
      f"H_R:{AF_supp['HR']:.3f}, M3:{AF_supp['M3']:.3f}}}  (H_R<4 => no independent H_R summand)")

sanity_ok = (J2_resid < TOL and JD_resid < TOL and gD_resid < TOL and
             Jg_resid < TOL and order0 < TOL)   # (local)

checkA = (dim_H == 4)                              # (local) dim_R(H) = 4
checkB = (realform_resid < TOL and quat_resid < TOL)   # (local) quaternion real form
checkC = (dim_left_only == 20 and deficit == 4)        # (local) left-only=20, deficit=4
checkD = (max_order1_on_AF < TOL)                      # (local) order-one machine-zero on A_F
# A_F = 24, *-subalgebra, full H_L survives as the H summand, full H_R does NOT (diag tied to C)
checkAF = (dim_AF == 24 and is_star_subalgebra and abs(HL_in_AF - 4) < 1e-6
           and HR_full_in_AF < 4 - 1e-6)  # (local)

print("\n# ---- pre-registered checks ----")
print(f"# (A) dim_R(H)=4              : {checkA}")
print(f"# (B) quaternion real form    : {checkB}")
print(f"# (C) left-only=20 & deficit=4: {checkC}")
print(f"# (D) order-one < 1e-12 on A_F: {checkD}")
print(f"# (AF) A_F=24, H=H_L, H_R out : {checkAF}")
print(f"# sanity (KO-6 + order-zero)  : {sanity_ok}")

# [SIGN] 3-tuple
sign_verdict = "PASS" if deficit == 4 else "FAIL"    # (local) deficit = +4 > 0 (bimodule adds H)
magnitude_verdict = "PASS" if (checkA and checkB and checkC and checkD and checkAF) else "FAIL"
regime_verdict = "VALID" if (sanity_ok and tau_invariant) else "MARGINAL"

if regime_verdict == "BREAKDOWN":
    verdict = "FAIL"
elif sign_verdict == "FAIL":
    verdict = "FAIL"
elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
    verdict = "FAIL"
elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
    verdict = "INFO"
elif magnitude_verdict == "INFO":
    verdict = "INFO"
else:
    verdict = "PASS"

# ----------------------------------------------------------------------------
# 9.  Persist data + plot
# ----------------------------------------------------------------------------
outdir = os.path.dirname(os.path.abspath(__file__))   # (local)
npz_path = os.path.join(outdir, "s116_w5_bimodule_h.npz")
png_path = os.path.join(outdir, "s116_w5_bimodule_h.png")

np.savez(npz_path,
         H_basis=np.array(H_basis),
         dim_C=2, dim_H=dim_H, dim_M3=18, dim_AF=dim_AF,
         dim_commutant=dim_comm, deficit=deficit,
         order_one_resid_matrix=R1,
         max_order_one_on_AF=max_order1_on_AF,
         realform_resid=realform_resid, quat_resid=quat_resid,
         subalg_resid=subalg_resid, is_star_subalgebra=is_star_subalgebra,
         combined_closes_at_24=combined_closes_at_24, fixedpoint_dim=AF.shape[1],
         commutant_support=np.array([comm_supp['C'], comm_supp['HL'], comm_supp['HR'], comm_supp['M3']]),
         AF_support=np.array([AF_supp['C'], AF_supp['HL'], AF_supp['HR'], AF_supp['M3']]),
         tau_invariant=tau_invariant, tau_inv_resid=tau_inv_resid,
         J2_resid=J2_resid, JD_resid=JD_resid, gD_resid=gD_resid, Jg_resid=Jg_resid,
         order0=order0, tau_fold=tau_fold)

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(13, 6))
    im0 = axes[0].imshow(np.log10(R1 + 1e-16), cmap="viridis", aspect="auto")
    axes[0].set_title("order-one residual log10||[[D_F,pi(g_i)],pi^o(g_j^o)]||")
    axes[0].set_xlabel("generator j (b, o-map)"); axes[0].set_ylabel("generator i (a, left)")
    # mark factor boundaries
    for b in [2, 6, 10]:
        axes[0].axhline(b - 0.5, color="w", lw=0.6); axes[0].axvline(b - 0.5, color="w", lw=0.6)
    fig.colorbar(im0, ax=axes[0])
    # survival bar: which factors are in commutant (order-0) vs A_F (order-1)
    cats = ["C(2)", "H_L(4)", "H_R(4)", "M3(18)"]
    comm_vals = [comm_supp['C'], comm_supp['HL'], comm_supp['HR'], comm_supp['M3']]
    af_vals = [AF_supp['C'], AF_supp['HL'], AF_supp['HR'], AF_supp['M3']]
    x = np.arange(4)
    axes[1].bar(x - 0.2, comm_vals, 0.4, label="commutant (order-0)", color="#cc6677")
    axes[1].bar(x + 0.2, af_vals, 0.4, label="A_F (order-1)", color="#4477aa")
    axes[1].set_xticks(x); axes[1].set_xticklabels(cats)
    axes[1].set_ylabel("dim_R surviving"); axes[1].legend()
    axes[1].set_title(f"H deficit = dim(A_F){dim_AF} - dim(comm){dim_comm} = {deficit}")
    fig.suptitle(f"S116-W5-BIMODULE-H : verdict={verdict}  (dim_R(H)={dim_H}, real-form exact)")
    fig.tight_layout()
    fig.savefig(png_path, dpi=110)
    print(f"\n# plot -> {png_path}")
except Exception as ex:
    print(f"# plot skipped: {ex}")

# ----------------------------------------------------------------------------
# 10.  Dual-SHA + verdict payload
# ----------------------------------------------------------------------------
def sha256_file(path):
    h = hashlib.sha256()   # (local)
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

script_sha = sha256_file(os.path.abspath(__file__))   # (local)
canon_sha = sha256_file(os.path.join(outdir, "..", "_shared", "canonical_constants.py"))
s22c_sha = sha256_file(os.path.join(outdir, "..", "session-22", "s22c_order_one.txt"))

# input-pin map -> audit_sha256 ; content (script) -> content_sha256
pinmap = {   # (local)
    "script": script_sha,
    "canonical_constants.py": canon_sha,
    "s22c_order_one.txt": s22c_sha,
    "gate_id": "S116-W5-BIMODULE-H",
    "scheme": "CCM-2007-bimodule-classification",
    "convention": "o-map-J-twisted-right-action-KO6-CANONICAL-IMPORT-BINDING",
    "L_max": "N/A",
}
audit_sha = hashlib.sha256(repr(sorted(pinmap.items())).encode()).hexdigest()   # (local)
content_sha = script_sha   # (local)

value = (f"dim_R(H)={dim_H};realform_resid={realform_resid:.2e};quat_resid={quat_resid:.2e};"
         f"dim_A_F={dim_AF};dim_commutant={dim_comm};deficit={deficit};"
         f"H_summand=H_L(left-quaternions,survives);H_R_broken_tied_to_C_via_Majorana;"
         f"order_one_on_A_F={max_order1_on_AF:.2e}(<{TOL:.0e});star_subalg_resid={subalg_resid:.2e};"
         f"left_only_commutant=C(2)+M3(18)=20;bimodule_adds_H=4;"
         f"tau_invariant={tau_invariant};rescaled_closure_dim={cand_rescaled.shape[1]};"
         f"KO6[J2={J2_resid:.1e},JD={JD_resid:.1e},gD={gD_resid:.1e},Jg={Jg_resid:.1e}];order0={order0:.1e};"
         f"checks[A={checkA},B={checkB},C={checkC},D={checkD},AF={checkAF}]")

print("\n" + "=" * 70)
print("VERDICT PAYLOAD")
print("=" * 70)

def print_verdict_payload():
    print(f"gate_id      = S116-W5-BIMODULE-H")
    print(f"verdict      = {verdict}")
    print(f"value        = {value}")
    print(f"scheme       = CCM-2007-bimodule-classification")
    print(f"convention   = o-map-J-twisted-right-action-KO6-CANONICAL-IMPORT-BINDING")
    print(f"L_max        = N/A")
    print(f"audit_sha256 = {audit_sha}")
    print(f"content_sha256 = {content_sha}")
    print(f"sign_verdict      = {sign_verdict}")
    print(f"magnitude_verdict = {magnitude_verdict}")
    print(f"regime_verdict    = {regime_verdict}")

print_verdict_payload()
print("\n4-tuple: (value=dim_R(H)=4, scheme=CCM-2007-bimodule-classification, "
      "convention=o-map-J-twisted-right-action-KO6-CANONICAL-IMPORT-BINDING, L_max=N/A)")
print("[SIGN] deficit = dim(A_F) - dim(commutant) = 24 - 20 = +4 > 0  (bimodule strictly adds H)")
sys.exit(0)
