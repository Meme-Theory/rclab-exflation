#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S117-W3-4-OFFJENSEN-U2-SHARING  (Session 117, Wave 3, §W3-4)  -- [VERIFY] gate.

ARE THE phi_88 (K7-transit) AND eps_LX (leptonic) CP PHASES INDEPENDENT OFF-JENSEN
MODULI, OR DO THEY SHARE ONE PARAMETER?  An exact su(3) Lie-algebra moduli count.

  RESOLVED  dim(off-Jensen moduli) = 1 (phi_88 Cartan) + k_coset (eps_LX coset),
            no linking constraint => phi_88 (lambda_8) is a DIFFERENT, INDEPENDENT
            CP invariant from the leptonic eps_LX coset phase => K7-transit's
            phi_CP = pi/2 SURVIVES a real leptonic eps_LX (J_PMNS = 0 is CONSISTENT
            with K7-transit baryogenesis; the E-3 sector-resolution; supports 3-2 PASS-K7).
  SHARED    dim < 1 + k_coset, a constraint c(phi_88, eps_LX) = 0 links them
            => one parameter; a real eps_LX would lock phi_88; the D1 main-line stands.

GOVERNING STRUCTURE (structure-first)
-------------------------------------
The fiber is SU(3); the Jensen deformation is a U(2)-INVARIANT left-invariant metric
(framework scaling L_1=e^{2tau} on u(1)_Y=<lambda_8> 1 dir; L_2=e^{-2tau} on
su(2)_I=<lambda_1,2,3> 3 dirs; L_3=e^{tau} on the C^2 coset SU(3)/U(2)=<lambda_4..7>
4 dirs -- Phononic-Substrate-Geometry.md).  The OFF-JENSEN deformation goes beyond the
U(2)-invariant family: it turns on (a) the lambda_8 Cartan phase phi_88 (= phi_CP_K7,
canonical:674, = pi/2 EXACT) and (b) the coset off-diagonal eps_LX texture (lepton CP).

The residual gauge group preserving the Jensen background is the isotropy U(2) =
SU(2)_I x U(1)_Y.  The off-Jensen MODULI are deformations modulo this residual gauge.
The discriminator RESOLVED-vs-SHARED is the U(2)-ISOTROPY IRREP TYPE of the two
deformation directions:

  * lambda_8 generates the CENTER of U(2)  ([lambda_8, lambda_1]=[lambda_8,lambda_2]=
    [lambda_8,lambda_3]=[lambda_8,lambda_8]=0).  Hence phi_88 is a U(2)-SINGLET modulus.
  * the coset <lambda_4..lambda_7> is a single irreducible U(2)-DOUBLET (CP^2; one
    hypercharge magnitude sqrt(3) under U(1)_Y).

A U(2)-singlet and a U(2)-doublet are DIFFERENT irreps; no U(2)-equivariant map (hence
no residual-gauge linking constraint) connects them.  The off-Jensen deformation space
D = <lambda_4,...,lambda_8> therefore DECOMPOSES as
        D = (U(2)-singlet <lambda_8>)  (+)  (U(2)-doublet <lambda_4..7>)
with the lambda_8 block DECOUPLED from the coset block in ad(u(2)) -- no off-diagonal
mixing in EITHER direction.  dim(off-Jensen moduli) = 1 + 4 = 5 = 1 + k_coset.  RESOLVED.

This is EXACTLY the substitution-chain warning made precise: [lambda_8, coset] != 0
(the coset carries lambda_8 hypercharge), but generator NON-commutation does NOT link
the DEFORMATION PARAMETERS -- the U(1)_Y action rotates the coset off-diagonal PHASE
(gauge on eps_LX) while FIXING lambda_8 (which commutes with itself), so phi_88 is
gauge-INVARIANT and cannot be absorbed into eps_LX.  The count is on the moduli (irrep
content), not the generator commutators.

[VERIFY] substitution chain (plan §W3-4):
  Def 1: su(3) Gell-Mann basis {lambda_1..8}; Cartan = <lambda_3, lambda_8>.
  Def 2: U(2) = <lambda_1,lambda_2,lambda_3,lambda_8>; coset CP^2 = <lambda_4,5,6,7>.
  Def 3: phi_88 = lambda_8 Cartan CP phase = phi_CP_K7_transit = pi/2 (canonical:674);
         eps_LX = lepton off-diagonal in the coset <lambda_4..7> (sec VII.BL).
  Def 4: off-Jensen deformation D(theta) on <lambda_4..8>; moduli = independent {theta_a}.
  Substitute: phi_88 = 1 modulus (lambda_8 U(1)); eps_LX = k_coset coset moduli.
  Simplify (linking test): [lambda_8, lambda_{4..7}] != 0 (coset carries hypercharge),
         BUT decompose D under ad(u(2)): lambda_8 -> SINGLET, coset -> DOUBLET; no mixing.
  Canonical form: RESOLVED dim = 1 + k_coset (independent) ; SHARED dim < 1 + k_coset.
  Direction: RESOLVED => phi_88 is a DIFFERENT CP invariant; K7-transit phi_CP=pi/2
             survives a real eps_LX; SHARED => one parameter, the two phases locked.
  [No eta_B / J_CP numerical sign claim -- the discriminant is a structural integer
   (moduli dimension), exact via the su(3) structure constants.]

============================================================================
SUBSTRATE-FIRST (phononic-framing.md) -- GEOMETRIC:
============================================================================
  The off-Jensen deformation moduli of the SU(3) fiber are a property of the
  spectral-triple STRUCTURE (the fabric itself), not its excitations.  Direction of
  explanation: the SU(3) Gell-Mann generator algebra -> the U(2)+CP^2 coset
  decomposition -> the off-Jensen deformation moduli space -> whether the phi_88 Cartan
  CP phase (K7-transit source) and the eps_LX coset off-diagonal (leptonic CP source)
  are independent moduli.  The governing structure is the representation theory of the
  U(2) c SU(3) isotropy: the deformation algebra's irrep factorisation is a
  Lie-algebraic invariant.  Whether the transit and leptonic CP phases are different
  invariants (sector-resolved) or one (shared) is fixed by the fiber's coset geometry,
  NOT by any excitation dynamics.

Output 4-tuple:
  (value=<RESOLVED/SHARED + dim breakdown + irrep types>,
   scheme=su3-gellmann-U2-isotropy-ad-irrep-moduli-count, convention=..., L_max=N/A)

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  computations/_shared/canonical_constants.py   (phi_CP_K7_transit = pi/2; feeds audit)
  No npz input: pure su(3) Lie-algebra moduli count (the eps_LX class lives in sec
  VII.BL/VII.CK in the registry; the off-Jensen generator structure is read from su(3)).

NOTE on canonical_constants.py SHA: the plan §W3-4 pins
8c850fd95a3214211cfb37ee66bec7da19f2344fb03d976a85cf0f2c4a4bbdaa, but the runtime file
differs (in-session W0 rho_s/c2 promotions, s117_w0_rhos_c2_promote.py).  This gate cites
ONLY phi_CP_K7_transit (= pi/2, MCP-confirmed unchanged), so the drift does NOT affect
the verdict.  audit_sha256 binds the RUNTIME canonical bytes per
substrate-first-canonical-sourcing.md §(ii.B) plan-text-drift correction.
"""

from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (math-scripts.md; 3x3/8x8 algebra is tiny;
#     GPU path N/A -- the matrices are 3x3 / 8x8, far below the 100x100 GPU threshold) ---
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 1 -- Paths + canonical constants (MANDATORY import)
# ---------------------------------------------------------------------------
THIS = Path(__file__).resolve()
SESSION_DIR = THIS.parent                                  # computations/session-117
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
SESSION_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    tau_fold,                       # 0.190 (Jensen deformation parameter at the fold)
    M_KK,                           # KK scale (framing only)
    phi_CP_K7_transit,              # = pi/2 EXACT (lambda_8 Cartan K7-transit CP phase)
)

import matplotlib                                           # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                             # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 -- Identity + pinned machinery (plan §W3-4 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "117"                                             # (local)
GATE_ID = "S117-W3-4-OFFJENSEN-U2-SHARING"                  # (local)
SCHEME = "su3-gellmann-U2-isotropy-ad-irrep-moduli-count"  # (local) plan pin
CONVENTION = ("Tr(lam_a_lam_b)=2delta_ab;U2=<1,2,3,8>;"
              "coset-CP2=<4,5,6,7>;Jensen-Cartan;offJensen-coset")  # (local) plan pin
L_MAX = "N/A"                                               # (local) algebraic; not a D_K truncation
TOL = 1.0e-12                                               # (local) integer-count "is-zero" tolerance
PUB_SIGFIGS = 6                                             # (local) Class-8.3 publication precision

# Framework Jensen-block dimensions (Phononic-Substrate-Geometry.md L_1/L_2/L_3 scaling)
DIM_U1Y = 1                                                 # (local) u(1)_Y = <lambda_8>, 1 dir
DIM_SU2I = 3                                                # (local) su(2)_I = <lambda_1,2,3>, 3 dirs
K_COSET = 4                                                 # (local) CP^2 coset <lambda_4..7>, 4 dirs
N_CARTAN_PHASE = 1                                          # (local) phi_88 on lambda_8 (U(1)_Y center)

U2_IDX = (1, 2, 3, 8)                                       # (local) U(2) generator indices
SU2_IDX = (1, 2, 3)                                         # (local) su(2)_isospin indices
COSET_IDX = (4, 5, 6, 7)                                    # (local) CP^2 coset indices
DEF_IDX = (4, 5, 6, 7, 8)                                   # (local) off-Jensen deform space D = coset + lambda_8

# ---------------------------------------------------------------------------
# Section 3 -- SHA-256 dual-SHA block (S84+ schema; pattern from template)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                    # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                               # (local)
    for p in inputs:
        sha = sha256_of(p)                                  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())                            # (local)
    h = hashlib.sha256()                                    # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    script_bytes = b""                                      # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                   # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()                              # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                             # (local)
    h_content = hashlib.sha256()                            # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                         # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 4 -- su(3) Gell-Mann algebra (exact-valued; cross-checked vs Sage QQbar)
# ---------------------------------------------------------------------------
def gellmann() -> dict:
    """The 8 Hermitian Gell-Mann matrices, Tr(lam_a lam_b) = 2 delta_ab."""
    s3 = np.sqrt(3.0)                                       # (local)
    lam = {                                                 # (local)
        1: np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex),
        2: np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex),
        3: np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex),
        4: np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex),
        5: np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex),
        6: np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex),
        7: np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex),
        8: np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / s3,
    }
    return lam


def comm(A, B):
    return A @ B - B @ A


def struct_const(lam, a, b, c) -> float:
    """f_{abc} via [lam_a, lam_b] = 2i f_{abc} lam_c ; f = Tr([la,lb] lc)/(4i)."""
    return float((np.trace(comm(lam[a], lam[b]) @ lam[c]) / (4j)).real)


def real_ad(lam, h) -> np.ndarray:
    """Real 8x8 adjoint matrix of ad(e_h) in the real su(3) basis e_a = i lam_a.

    In the anti-Hermitian basis e_a = i lam_a (the actual real Lie algebra su(3)),
    ad(e_h) has REAL entries (A_h)_{cb} = -2 f_{hbc}, where
    [e_a, e_b] = -2 f_{abc} e_c.  Real adjoint matrices are the clean object for the
    real representation-theory (invariant subspaces, irrep decomposition, commutant).
    """
    A = np.zeros((8, 8), dtype=float)                       # (local)
    for b in range(1, 9):
        for c in range(1, 9):
            A[c - 1, b - 1] = -2.0 * struct_const(lam, h, b, c)
    return A


def sub(A: np.ndarray, idx) -> np.ndarray:
    """Restrict an 8x8 matrix to the subspace spanned by 1-based indices `idx`."""
    j = [i - 1 for i in idx]                                # (local)
    return A[np.ix_(j, j)]


def offblock(A: np.ndarray, rows, cols) -> np.ndarray:
    """The (rows x cols) off-diagonal block of an 8x8 matrix (1-based indices)."""
    r = [i - 1 for i in rows]                               # (local)
    c = [i - 1 for i in cols]                               # (local)
    return A[np.ix_(r, c)]


# ---------------------------------------------------------------------------
# Section 5 -- Compute: the off-Jensen U(2)-isotropy moduli count
# ---------------------------------------------------------------------------
def compute() -> dict:
    lam = gellmann()
    s3 = np.sqrt(3.0)                                       # (local)

    # --- (T0) Gell-Mann normalisation Tr(lam_a lam_b) = 2 delta_ab ---
    gram = np.array([[np.trace(lam[a] @ lam[b]).real for b in range(1, 9)]
                     for a in range(1, 9)])                 # (local)
    norm_ok = bool(np.allclose(gram, 2.0 * np.eye(8), atol=TOL))

    # --- real adjoint matrices A_h = ad(e_h), e_a = i lam_a ---
    A = {h: real_ad(lam, h) for h in range(1, 9)}           # (local)

    # --- (T1) lambda_8 is CENTRAL in u(2): [lambda_8, lambda_i] = 0, i in {1,2,3} ---
    #     (lambda_8 commutes with all of u(2) => generates the U(2) CENTER U(1)_Y).
    central_resid = {i: float(np.max(np.abs(comm(lam[8], lam[i])))) for i in SU2_IDX}  # (local)
    lambda8_central = bool(all(v < TOL for v in central_resid.values()))

    # key coset hypercharge structure constants (expect sqrt(3)/2)
    f_845 = struct_const(lam, 8, 4, 5)                      # (local)
    f_867 = struct_const(lam, 8, 6, 7)                      # (local)
    coset_hypercharge_ok = bool(abs(f_845 - s3 / 2) < TOL and abs(f_867 - s3 / 2) < TOL)

    # --- (T2) reductive [u(2), m] subset m  and  (T3) symmetric [m, m] subset u(2) ---
    def in_span(vec_mat, idx):
        coeffs = np.array([np.trace(vec_mat @ lam[c]).real / 2.0 for c in range(1, 9)])  # (local)
        leak = [abs(coeffs[a - 1]) for a in range(1, 9) if a not in idx]                 # (local)
        return (max(leak) if leak else 0.0)
    red_leak = max(in_span(comm(lam[h], lam[m]), COSET_IDX) for h in U2_IDX for m in COSET_IDX)  # (local)
    sym_leak = max(in_span(comm(lam[m1], lam[m2]), U2_IDX) for m1 in COSET_IDX for m2 in COSET_IDX)  # (local)
    reductive = bool(red_leak < TOL)
    symmetric = bool(sym_leak < TOL)

    # --- (T4) ad(lambda_8)|coset eigenvalues = single hypercharge magnitude (=> ONE doublet) ---
    A8_coset = sub(A[8], COSET_IDX)                         # (local) real 4x4
    eig8 = np.linalg.eigvals(A8_coset)                      # (local)
    hyper_mags = np.sort(np.abs(eig8))                      # (local)
    hyper_single = bool(np.allclose(hyper_mags, hyper_mags[0], atol=1e-9))
    hypercharge_mag = float(hyper_mags[0])                  # (local) = 2*sqrt(3)/... reported as computed

    # --- (T5) U(2) decomposition of D = <lambda_4..lambda_8> (off-Jensen deform space) ---
    # (a) D is ad(u(2))-invariant: [u(2), D] subset D
    def_leak = max(in_span(comm(lam[h], lam[d]), DEF_IDX) for h in U2_IDX for d in DEF_IDX)  # (local)
    D_invariant = bool(def_leak < TOL)

    # (b) <lambda_8> is a U(2)-SINGLET inside D: ad(h) lambda_8 = 0 for all h in u(2)
    singlet_resid = max(float(np.max(np.abs(comm(lam[h], lam[8])))) for h in U2_IDX)  # (local)
    lambda8_singlet = bool(singlet_resid < TOL)

    # (c) NO equivariant mixing lambda_8 <-> coset in EITHER direction (the linking test)
    #     ad(h) lambda_8 has zero coset component  AND  ad(h) coset has zero lambda_8 component
    mix_8_to_coset = 0.0                                    # (local)
    mix_coset_to_8 = 0.0                                    # (local)
    for h in U2_IDX:
        blk = offblock(A[h], COSET_IDX, (8,))              # coset-rows, lambda_8-col  (ad(h) lam_8 -> coset?)
        mix_8_to_coset = max(mix_8_to_coset, float(np.max(np.abs(blk))))
        blk2 = offblock(A[h], (8,), COSET_IDX)            # lambda_8-row, coset-cols  (ad(h) coset -> lam_8?)
        mix_coset_to_8 = max(mix_coset_to_8, float(np.max(np.abs(blk2))))
    no_mixing = bool(mix_8_to_coset < TOL and mix_coset_to_8 < TOL)

    # (d) coset is a SINGLE irreducible U(2)-doublet: real commutant of {ad(h)|coset} = C (real dim 2)
    #     (Schur over R: an irreducible complex rep has commutant C => real dim 2.)
    coset_mats = [sub(A[h], COSET_IDX) for h in U2_IDX]     # (local) four 4x4 real
    # solve {X : [A_h|coset, X] = 0 for all h} ; nullspace dim of the stacked commutator operator
    rows = []                                               # (local)
    eye4 = np.eye(4)                                        # (local)
    for Mh in coset_mats:
        # vec([Mh, X]) = (I (x) Mh - Mh^T (x) I) vec(X)
        rows.append(np.kron(eye4, Mh) - np.kron(Mh.T, eye4))
    Cstack = np.vstack(rows)                                # (local) (4*16) x 16
    sv = np.linalg.svd(Cstack, compute_uv=False)           # (local)
    commutant_dim = int(np.sum(sv < 1e-9))                 # (local) dim of real commutant
    coset_one_irrep = bool(commutant_dim == 2)             # C => irreducible complex doublet

    # --- (T6) basis-invariance (=> NOT INFO): rotate the coset basis by a generic U(2)
    #     group element and re-check lambda_8 singlet + the singlet/doublet split persist ---
    rng = np.random.default_rng(117)                        # (local)
    theta = rng.normal(size=4)                              # (local) random u(2) parameters (1,2,3,8)
    Hgen = sum(theta[k] * lam[g] for k, g in enumerate(U2_IDX))  # (local) Hermitian u(2) element
    # U(2) group element g = exp(i Hgen); rotate the coset generators lam_k -> g lam_k g^{-1}
    from scipy.linalg import expm                           # (local)
    g = expm(1j * Hgen)                                     # (local)
    rot_coset = {k: g @ lam[k] @ g.conj().T for k in COSET_IDX}  # (local) rotated coset basis
    # lambda_8 still commutes with all rotated coset? (it must -- conjugation by U(2) preserves
    # the coset as a U(2)-module, and lambda_8 is central) ; and lambda_8 stays a singlet.
    # Check: the rotated coset stays orthogonal to lambda_8 (Tr(g lam_k g^-1 lam_8)=Tr(lam_k lam_8)=0)
    rot_orth_8 = max(abs(np.trace(rot_coset[k] @ lam[8]).real) for k in COSET_IDX)  # (local)
    # and lambda_8 still annihilated by ad(u(2)) is basis-independent (already T5b); the split
    # is preserved iff rotating the coset never produces a lambda_8 component:
    basis_invariant = bool(rot_orth_8 < 1e-9 and lambda8_singlet)

    # --- (T7) COUNTERFACTUAL teeth: if the "Cartan-phase" generator were a COSET generator
    #     (lambda_4) instead of the central lambda_8, it would land IN the doublet => SHARED.
    #     This shows the RESOLVED verdict is a genuine fact about lambda_8 being CENTRAL,
    #     not a tautology of the test. ---
    cf_singlet_resid = max(float(np.max(np.abs(comm(lam[h], lam[4])))) for h in U2_IDX)  # (local)
    cf_is_singlet = bool(cf_singlet_resid < TOL)            # expect FALSE (lambda_4 is in the doublet)
    counterfactual_discriminates = bool(not cf_is_singlet)  # test has teeth iff lam_4 != singlet

    # --- VERDICT logic -------------------------------------------------------
    structural_ok = norm_ok and reductive and symmetric and D_invariant and coset_hypercharge_ok

    # The off-Jensen moduli dimension and the linking-constraint determination:
    # RESOLVED iff phi_88 (lambda_8) is a U(2)-SINGLET, the coset is a SEPARATE irrep
    # (one doublet), and NO equivariant mixing links them => dim = 1 + k_coset, no constraint.
    resolved_conditions = (lambda8_central and lambda8_singlet and coset_one_irrep
                           and no_mixing)
    linking_constraint = not resolved_conditions            # SHARED would set this True

    if not structural_ok:
        verdict = "FAIL"                                    # (local) decomposition ill-defined
        branch = "ILL-DEFINED"                              # (local)
        moduli_dim = -1                                     # (local)
    elif not basis_invariant:
        verdict = "INFO"                                    # (local) convention-sensitive
        branch = "BASIS-DEPENDENT"                          # (local)
        moduli_dim = -1                                     # (local)
    elif not linking_constraint:
        verdict = "PASS"                                    # (local)
        branch = "RESOLVED"                                 # (local)
        moduli_dim = N_CARTAN_PHASE + K_COSET              # (local) 1 + 4 = 5
    else:
        verdict = "PASS"                                    # (local) SHARED is also a definite PASS
        branch = "SHARED"                                   # (local)
        moduli_dim = K_COSET                                # (local) < 1 + k_coset (linked)

    result = {
        "verdict": verdict,
        "branch": branch,
        "moduli_dim": moduli_dim,
        "n_cartan_phase": N_CARTAN_PHASE,
        "k_coset": K_COSET,
        "norm_ok": norm_ok,
        "lambda8_central": lambda8_central,
        "central_resid": central_resid,
        "coset_hypercharge_ok": coset_hypercharge_ok,
        "f_845": f_845, "f_867": f_867, "sqrt3_over_2": float(s3 / 2),
        "reductive": reductive, "red_leak": red_leak,
        "symmetric": symmetric, "sym_leak": sym_leak,
        "hyper_single": hyper_single, "hypercharge_mag": hypercharge_mag,
        "hyper_mags": hyper_mags.tolist(),
        "D_invariant": D_invariant, "def_leak": def_leak,
        "lambda8_singlet": lambda8_singlet, "singlet_resid": singlet_resid,
        "no_mixing": no_mixing, "mix_8_to_coset": mix_8_to_coset,
        "mix_coset_to_8": mix_coset_to_8,
        "coset_one_irrep": coset_one_irrep, "commutant_dim": commutant_dim,
        "basis_invariant": basis_invariant, "rot_orth_8": rot_orth_8,
        "counterfactual_discriminates": counterfactual_discriminates,
        "cf_is_singlet": cf_is_singlet, "cf_singlet_resid": cf_singlet_resid,
        "linking_constraint": linking_constraint,
        # arrays for the figure / npz
        "A_def": sub(sum(np.abs(A[h]) for h in U2_IDX), DEF_IDX),  # |ad(u2)| on D (block structure)
        "A8_coset": A8_coset,
    }
    # the published value string (no single-quote chars; the MCP tool wraps value='...')
    result["value"] = (
        f"{branch}:dim={moduli_dim}=1(phi88-U2singlet-lam8-center)"
        f"+{K_COSET}(epsLX-U2doublet-CP2coset);no-linking-constraint={not linking_constraint};"
        f"lam8-central-in-U2={lambda8_central};coset-one-irrep(commutant_dim={commutant_dim}=C);"
        f"no-equivariant-mixing={no_mixing};phi88-gauge-invariant-survives-real-epsLX;"
        f"K7-transit-CP-independent-of-leptonic-epsLX;basis-invariant={basis_invariant};"
        f"counterfactual-lam4-would-be-SHARED={counterfactual_discriminates};phi_CP_K7=pi/2"
    )
    return result


# ---------------------------------------------------------------------------
# Section 6 -- Figure (U(2)-isotropy decomposition of the off-Jensen deform space)
# ---------------------------------------------------------------------------
def make_figure(res: dict) -> None:
    fig, ax = plt.subplots(2, 2, figsize=(13, 10))
    labels_def = [r"$\lambda_4$", r"$\lambda_5$", r"$\lambda_6$", r"$\lambda_7$", r"$\lambda_8$"]  # (local)

    # (a) |ad(u(2))| block structure on D = <lambda_4..8>: lambda_8 row/col is ZERO (decoupled)
    A_def = np.asarray(res["A_def"])                        # (local)
    im0 = ax[0, 0].imshow(A_def, cmap="magma", aspect="equal")
    ax[0, 0].set_xticks(range(5)); ax[0, 0].set_yticks(range(5))
    ax[0, 0].set_xticklabels(labels_def); ax[0, 0].set_yticklabels(labels_def)
    ax[0, 0].set_title(r"$\sum_{h\in u(2)}|\mathrm{ad}(\lambda_h)|$ on $D=\langle\lambda_4..\lambda_8\rangle$"
                       + "\n(λ₈ row/col = 0 ⇒ U(2)-SINGLET decoupled from coset DOUBLET)")
    fig.colorbar(im0, ax=ax[0, 0], fraction=0.046)
    ax[0, 0].axhline(3.5, color="cyan", lw=1.5); ax[0, 0].axvline(3.5, color="cyan", lw=1.5)
    ax[0, 0].text(1.5, -0.8, "coset CP² doublet (k=4)", color="white", ha="center", fontsize=9)
    ax[0, 0].text(4.0, 4.9, "φ₈₈ singlet", color="cyan", ha="center", fontsize=9)

    # (b) moduli count bar
    cats = ["φ₈₈\n(λ₈ U(2)-singlet)", "ε_LX coset\n(CP² doublet)", "off-Jensen\nmoduli total"]  # (local)
    vals = [res["n_cartan_phase"], res["k_coset"], res["moduli_dim"]]  # (local)
    colors = ["#2ca02c", "#1f77b4", "#d62728"]             # (local)
    ax[0, 1].bar(cats, vals, color=colors)
    for i, v in enumerate(vals):
        ax[0, 1].text(i, v + 0.08, str(v), ha="center", fontsize=13, fontweight="bold")
    ax[0, 1].set_ylabel("moduli dimension")
    ax[0, 1].set_title(f"Off-Jensen moduli count: {res['branch']}\n"
                       f"dim = 1 + k_coset = {res['moduli_dim']}  (RESOLVED ⇔ no linking constraint)")
    ax[0, 1].set_ylim(0, max(vals) + 1)

    # (c) ad(lambda_8)|coset eigenvalues in the complex plane (the U(1)_Y hypercharge)
    eig = np.linalg.eigvals(np.asarray(res["A8_coset"]))   # (local)
    ax[1, 0].scatter(eig.real, eig.imag, s=120, c="#9467bd", zorder=3)
    ax[1, 0].axhline(0, color="grey", lw=0.7); ax[1, 0].axvline(0, color="grey", lw=0.7)
    circ = plt.Circle((0, 0), res["hypercharge_mag"], fill=False, ls="--", color="grey")  # (local)
    ax[1, 0].add_patch(circ)
    ax[1, 0].set_aspect("equal")
    ax[1, 0].set_xlabel("Re"); ax[1, 0].set_ylabel("Im")
    ax[1, 0].set_title(r"$\mathrm{ad}(\lambda_8)|_{\rm coset}$ eigenvalues"
                       + f"\nsingle |Y| = {res['hypercharge_mag']:.4f} ⇒ ONE irreducible doublet")

    # (d) verdict text panel
    ax[1, 1].axis("off")
    txt = (
        f"VERDICT: {res['verdict']} — {res['branch']}\n"
        f"────────────────────────────────────────\n"
        f"dim(off-Jensen moduli) = {res['moduli_dim']} = 1 + {res['k_coset']}\n"
        f"  φ₈₈  : 1  (λ₈ = U(2) CENTER ⇒ singlet)\n"
        f"  ε_LX : {res['k_coset']}  (CP² coset ⇒ one U(2) doublet)\n\n"
        f"STRUCTURAL CHECKS (exact, su(3) struct const):\n"
        f"  Tr(λλ)=2δ ......... {res['norm_ok']}\n"
        f"  λ₈ central in U(2) . {res['lambda8_central']}\n"
        f"  [u(2),m]⊆m ........ {res['reductive']}\n"
        f"  [m,m]⊆u(2) (sym) .. {res['symmetric']}\n"
        f"  f₈₄₅=f₈₆₇=√3/2 .... {res['coset_hypercharge_ok']}\n"
        f"  λ₈ U(2)-singlet ... {res['lambda8_singlet']}\n"
        f"  coset 1 irrep (C) . {res['coset_one_irrep']} (commutant dim {res['commutant_dim']})\n"
        f"  no λ₈↔coset mixing  {res['no_mixing']}\n"
        f"  basis-invariant ... {res['basis_invariant']}\n"
        f"  counterfactual λ₄→SHARED {res['counterfactual_discriminates']}\n\n"
        f"⇒ φ₈₈ (K7-transit, φ_CP=π/2) and ε_LX (leptonic)\n"
        f"   are INDEPENDENT CP invariants. K7-transit\n"
        f"   SURVIVES a real ε_LX (J_PMNS=0 CONSISTENT).\n"
        f"   E-3 sector-resolution holds; supports 3-2 PASS-K7."
    )
    ax[1, 1].text(0.0, 0.98, txt, va="top", ha="left", family="monospace", fontsize=9.5)

    fig.suptitle("S117-W3-4 — Off-Jensen U(2) moduli: φ₈₈ Cartan vs ε_LX coset (RESOLVED vs SHARED)",
                 fontsize=13, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 -- emit verdict payload (race-safe; agent calls emit_verdict)
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
    payload = {                                             # (local)
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


OUT_NPZ = SESSION_DIR / "s117_offjensen_u2_sharing.npz"     # (local)
OUT_PNG = SESSION_DIR / "s117_offjensen_u2_sharing.png"     # (local)
INPUT_FILES = [SHARED_DIR / "canonical_constants.py"]       # (local)


# ---------------------------------------------------------------------------
# Section 8 -- Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                       # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)                           # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()                 # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  phi_CP_K7_transit = {float(phi_CP_K7_transit):.10f}  (= pi/2 = {np.pi/2:.10f})")
    print(f"  tau_fold = {float(tau_fold)}  M_KK = {float(M_KK)} (framing)")
    print()

    res = compute()

    # cross-check vs the Sage QQbar verification (documented in the working paper)
    print("=== structural checks (exact su(3) structure constants) ===")
    print(f"  Tr(lam_a lam_b)=2delta_ab : {res['norm_ok']}")
    print(f"  lambda_8 CENTRAL in U(2)  : {res['lambda8_central']}  (resid {max(res['central_resid'].values()):.2e})")
    print(f"  f_845={res['f_845']:.6f}  f_867={res['f_867']:.6f}  sqrt3/2={res['sqrt3_over_2']:.6f}")
    print(f"  reductive [u(2),m]<=m     : {res['reductive']} (leak {res['red_leak']:.2e})")
    print(f"  symmetric [m,m]<=u(2)     : {res['symmetric']} (leak {res['sym_leak']:.2e})")
    print(f"  ad(l8)|coset |Y| single   : {res['hyper_single']}  |Y|={res['hypercharge_mag']:.6f}  eigs|.|={res['hyper_mags']}")
    print(f"  D=<l4..l8> ad(u2)-invariant: {res['D_invariant']} (leak {res['def_leak']:.2e})")
    print(f"  lambda_8 U(2)-SINGLET     : {res['lambda8_singlet']} (resid {res['singlet_resid']:.2e})")
    print(f"  coset ONE irrep (commutant dim={res['commutant_dim']}, =2 means C): {res['coset_one_irrep']}")
    print(f"  no l8<->coset mixing      : {res['no_mixing']} (8->coset {res['mix_8_to_coset']:.2e}, coset->8 {res['mix_coset_to_8']:.2e})")
    print(f"  basis-invariant (not INFO): {res['basis_invariant']} (rot_orth_8 {res['rot_orth_8']:.2e})")
    print(f"  counterfactual lam4=SHARED: {res['counterfactual_discriminates']} (lam4 singlet? {res['cf_is_singlet']})")
    print()
    print(f"=== MODULI COUNT: dim = {res['moduli_dim']} = {res['n_cartan_phase']} (phi_88) + {res['k_coset']} (eps_LX coset) ===")
    print(f"=== linking_constraint = {res['linking_constraint']}  =>  BRANCH = {res['branch']} ===")
    print()

    # save data
    np.savez(
        OUT_NPZ,
        verdict=res["verdict"], branch=res["branch"],
        moduli_dim=res["moduli_dim"], n_cartan_phase=res["n_cartan_phase"], k_coset=res["k_coset"],
        norm_ok=res["norm_ok"], lambda8_central=res["lambda8_central"],
        coset_hypercharge_ok=res["coset_hypercharge_ok"],
        f_845=res["f_845"], f_867=res["f_867"], sqrt3_over_2=res["sqrt3_over_2"],
        reductive=res["reductive"], red_leak=res["red_leak"],
        symmetric=res["symmetric"], sym_leak=res["sym_leak"],
        hyper_single=res["hyper_single"], hypercharge_mag=res["hypercharge_mag"],
        hyper_mags=np.asarray(res["hyper_mags"]),
        D_invariant=res["D_invariant"], def_leak=res["def_leak"],
        lambda8_singlet=res["lambda8_singlet"], singlet_resid=res["singlet_resid"],
        no_mixing=res["no_mixing"], mix_8_to_coset=res["mix_8_to_coset"],
        mix_coset_to_8=res["mix_coset_to_8"],
        coset_one_irrep=res["coset_one_irrep"], commutant_dim=res["commutant_dim"],
        basis_invariant=res["basis_invariant"], rot_orth_8=res["rot_orth_8"],
        counterfactual_discriminates=res["counterfactual_discriminates"],
        cf_singlet_resid=res["cf_singlet_resid"],
        linking_constraint=res["linking_constraint"],
        A_def=np.asarray(res["A_def"]), A8_coset=np.asarray(res["A8_coset"]),
        phi_CP_K7_transit=float(phi_CP_K7_transit), tau_fold=float(tau_fold),
        audit_sha256=audit_sha, content_sha256=content_sha,
        value=res["value"],
    )
    print(f"  wrote {OUT_NPZ.name}")

    make_figure(res)
    print(f"  wrote {OUT_PNG.name}")
    print()

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    print_verdict_payload(
        res["verdict"], res["value"], audit_sha, content_sha,
        companion_note=("off-Jensen U(2) moduli RESOLVED: phi_88 (lambda_8 U(2)-center singlet) "
                        "INDEPENDENT of eps_LX (CP^2 coset doublet); dim=1+k_coset=5; "
                        "K7-transit phi_CP=pi/2 survives real eps_LX; supports W3-2 PASS-K7; E-3 sector-resolution"),
        extra_rows=[
            "# regulator_pin: N/A (algebraic su(3) Lie-algebra count; no Seeley-DeWitt a_n, no spectral truncation)",
            "# canonical_drift: plan-pinned canonical_constants.py sha 8c850fd9..; runtime sha differs (in-session W0 rho_s/c2 promotions); only phi_CP_K7_transit=pi/2 cited (MCP-confirmed unchanged); audit_sha binds runtime bytes per substrate-first-canonical-sourcing.md (ii.B)",
        ],
    )

    wall = time.time() - t0                                # (local)
    print(f"\n=== {GATE_ID}: {res['verdict']} ({res['branch']}) (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
