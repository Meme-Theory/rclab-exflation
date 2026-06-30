#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S104-EULER-CLASS-J-DOUBLET
================================================================================
Gate:   S104-EULER-CLASS-J-DOUBLET   (trigger [VERIFY], classification GEOMETRIC)
Agent:  berry-geometric-phase-theorist
Plan:   sessions/session-plan/session-104-plan-w2.md  ## §W2-1
WP:     sessions/session-104/session-104-w2-workingpaper.md  ### §W2-1

================================================================================
GEOMETRY FIRST -- THE RIGHT CHARACTERISTIC CLASS FOR A REAL RANK-2 BUNDLE
================================================================================
S96-GEOM-OFFJENSEN-CHERN (PASS-TRIVIAL, C_FHS=9.78e-15, maxOmega=2.27e-23) closed
the CHERN corridor on the 2-parameter U(2)-invariant volume-preserving TT surface
(v_J=(2,-2,1), v_mu=n x v_J=(11,7,-8), |v_mu|=sqrt(234); mu=0 = Jensen line; fold at
tau=tau_fold). The substrate's lowest Dirac band is a 2-FOLD J/PH-DEGENERATE REAL
(BDI) doublet in every Peter-Weyl sector (band_deg=2). Reality (Kosmann K_a
anti-Hermitian => real eigenstates, S25/W5 PROVEN, Omega=0 at 1.12e-16) kills the
Abelian Berry curvature AND the arg-det Wilczek-Zee link identically -- that is what
S96 measured.

But the bundle is a REAL O(2)/BDI two-band bundle, NOT a complex U(1) line bundle.
Its characteristic class is the EULER class -- the Pfaffian of the so(2)-valued
curvature of the real frame -- NOT the first Chern class (the trace of the u(1)-valued
curvature). A real frame can ROTATE around a closed loop (an SO(2) element with nonzero
rotation angle) WITHOUT acquiring any complex phase. That rotation is the Euler holonomy.
arg det (Chern) sees |det|=1 (no U(1) winding); Pf sees the SO(2) rotation angle. S96
computed the WRONG characteristic class for a real bundle. This gate computes the RIGHT one.

THE EULER CLASS:
    e2 = (1/2pi) oint_S Pf(F^Euler)
For a 2x2 antisymmetric (so(2)) curvature [[0,f],[-f,0]]: Pf = f (Pf^2 = det = f^2).
e2 in Z (Chern-Weil / Gauss-Bonnet): the net number of 2pi rotations of the real
eigenframe of the lowest Dirac doublet as (tau,mu) sweep the closed loop around the fold.

  * PASS-TRIVIAL  (|e2|<1e-3 -> 0, max|F^Euler|<1e-12): trivial in Euler AS WELL AS
    Chern. Strengthens metric-without-curvature to its strongest form (g~982.5
    Provost-Vallee reservoir = SOLE topologically-active object); L0-L7 chain gains a
    12th independent zero invariant. The real frame is globally non-rotating.
  * PASS-NONTRIVIAL (|e2-n|<1e-3, n!=0, max|F^Euler|>1e-6): the substrate's FIRST
    nonzero topological invariant; re-opens topology-survives-dissolution; Kwon-Yang
    quantum-volume<->Euler bound ties g~982.5 to a nonzero topological charge.

--------------------------------------------------------------------------------
[VERIFY] SUBSTITUTION CHAIN (plan §W2-1 substitution_chain; math-scripts.md
                            §"Double-Check Logic Before Compute")
--------------------------------------------------------------------------------
Claim A: "Chern=0 does NOT imply Euler=0; e2 is genuinely uncomputed."
  Def 1: F^Euler = so(2)-valued (real antisymmetric 2x2) curvature of the real rank-2
         frame O(tau,mu); a 2x2 antisymmetric matrix is [[0,f],[-f,0]], single entry f.
  Def 2: Pf([[0,f],[-f,0]]) = f.
  Def 3: det([[0,f],[-f,0]]) = f^2 = (Pf)^2  (Pf(A)^2 = det(A) for antisymmetric A;
         smoke-tested at <1e-13 residual on a random 4x4 here).
  Def 4: e2 = (1/2pi) oint Pf(F^Euler); the U(1)/Chern c1 = (1/2pi) oint tr(i F^{u(1)})
         is a DIFFERENT trace of a DIFFERENT (arg-det) component. S96 measured c1-type = 0.
  Substitute: Pf is LINEAR in f (sign-sensitive); det = f^2 is QUADRATIC (sign-blind).
         arg det reads det(M)/|det(M)| of the COMPLEX overlap M; its phase IS the U(1)
         (Chern) part -- IDENTICALLY 1 when the eigenstates are real (M real => arg in
         {0,pi}; |lambda|-min reality forces the trivial branch).
  Simplify: a real frame can ROTATE around the loop (SO(2), nonzero angle) WITHOUT any
         complex phase. That rotation is the Euler holonomy; generator = off-diagonal f.
         arg det sees |det|=1 (no U(1) winding) but Pf sees the SO(2) rotation angle.
  Canonical form: e2 = (1/2pi) oint f(tau,mu) (SO(2) holonomy angle / 2pi over plaquettes).
  Direction: e2 is a SIGNED integer (orientation-dependent); PASS-TRIVIAL e2=0 (no net
         real-frame rotation), PASS-NONTRIVIAL e2=n!=0.
  Conclusion: Chern=0 does NOT imply Euler=0. S96 PASS-TRIVIAL (arg det=0) is SILENT on
         the Pfaffian of the real frame. e2 is genuinely uncomputed; the gate decides it.

Claim B: PASS-NONTRIVIAL inverts metric-without-curvature (the g~982.5 reservoir would
         be topologically active); PASS-TRIVIAL closes the LAST geometric-invariant
         escape route (g~982.5 the SOLE topologically-active object).

--------------------------------------------------------------------------------
METHOD (FHS-Pfaffian-Euler lattice + continuum so(2)-curvature cross-check; plan §W2-1)
--------------------------------------------------------------------------------
(A) LATTICE Pfaffian-Euler (primary, gauge-invariant). At each NODE rotate the 2-block
    to a real orthonormal frame O(i,j) (S25/W5 reality: fix a real gauge by deterministic
    Gram-Schmidt of real(u) per band). Form the SO(2) frame-overlap R_dir = O(i,j)^T
    O(i+1_dir,j) (real 2x2, ~orthogonal). The plaquette real-frame holonomy
        W = R_tau(i,j) R_mu(i+1,j) R_tau(i,j+1)^T R_mu(i,j)^T
    is a (near) SO(2) matrix; its log is antisymmetric [[0,f],[-f,0]]; F^Euler(i,j) = f =
    the SO(2) rotation angle of the plaquette. e2_lattice = (1/2pi) sum_{i,j} F^Euler(i,j).
    The real-frame det-sign is tracked so reflections (det=-1, O(2)\SO(2)) are handled.
(B) CONTINUUM Pfaffian-Euler (cross-check). From the SAME doublet eigendecomposition,
    form the real antisymmetric non-Abelian Berry curvature (the so(2) part of the WZ
    curvature F_{tau mu} = d_tau A_mu - d_mu A_tau + [A_tau, A_mu] in the 2-band index),
    in the REAL frame; e2_cont = (1/2pi) integral Pf(Omega^{ab}) dtau dmu.
Orientation pinned dtau ^ dmu (tau outer/y, mu inner/x); Pf([[0,f],[-f,0]])=+f, consistent
across (A) and (B).
Companion INFO: Kwon-Yang ideal-condition residual R_ideal = ||g - F12 omega|| / ||g|| at
the fold, g = Provost-Vallee quantum metric (Re QGT) computed on the SAME doublet (NOT
imported; atlas-07's reservoir ~982.5 is a methodological cross-check only).

SUBSTRATE ARROW (phononic-framing.md; never inverted):
    D_K eigenbundle over the substrate's OWN modulus surface -> real (BDI) two-band frame
    O(tau,mu) -> SO(2)-valued frame curvature F^Euler -> Euler class e2. e2 counts how many
    net 2pi rotations the REAL eigenframe of the lowest Dirac doublet undergoes as the
    substrate's intrinsic deformation parameters (tau,mu) sweep a closed loop around the
    fold. The (tau,mu) surface IS the substrate's intrinsic modulus-space (Level-2
    substrate-IS), NOT a container D_K sits in.

Author: berry-geometric-phase-theorist (Session 104, Wave 2)
Date:   2026-06-10
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import scipy.linalg as sla
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Paths + canonical imports (MANDATORY: from canonical_constants import *)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]          # (local) computations/session-104 => parents[2]=root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_96_DIR = PROJECT_ROOT / "computations" / "session-96"
SESSION_104_DIR = PROJECT_ROOT / "computations" / "session-104"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(SESSION_96_DIR))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import tau_fold  # noqa: E402

# Reuse the S96 off-Jensen-Chern scaffold (build_su3_infra / metric_scale_factors /
# build_dirac_sector / lowest_band_multiplet / band_degeneracy / dD_dparam / eigh_H).
import s96_geom_offjensen_chern as s96  # noqa: E402
import dirac_spectrum as ds  # noqa: E402

# ---------------------------------------------------------------------------
# Gate identity + pre-registered pins (plan §W2-1 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "S104"                          # (local) for print_verdict_payload
GATE_ID = "S104-EULER-CLASS-J-DOUBLET"    # (local)
SCHEME = "FHS-Pfaffian-Euler"             # (local) plan-pinned (real-frame SO(2)/Pfaffian variant of FHS)
CONVENTION = "ABSOLUTE"                   # (local) plan-pinned (Euler = orientation-dependent integer; dtau ^ dmu, Pf([[0,f],[-f,0]])=+f)
L_MAX = "10"                              # (local) plan-pinned Peter-Weyl restriction
SCHEMA_VERSION = "S84+"                   # (local)

# Plan scan_range identical to S96: tau in [0.10,0.30] x mu in [-0.10,0.10]; 50x50 plaquette mesh.
TAU_LO, TAU_HI = 0.10, 0.30               # (local) plan scan_range tau
MU_LO, MU_HI = -0.10, 0.10                # (local) plan scan_range mu (mu=0 = Jensen line)
N_PLAQ = 50                               # (local) 50x50 plaquette grid (N_eval=2500)
N_NODE = N_PLAQ + 1                       # (local) 51x51 NODE grid
DTAU = (TAU_HI - TAU_LO) / N_PLAQ         # (local) ~0.004
DMU = (MU_HI - MU_LO) / N_PLAQ            # (local) ~0.004
BAND_DEG = 2                              # (local) plan band_deg=2 (J/PH doublet; verified on the S96 npz)

# Tolerances (plan §W2-1 machinery_pin_map.tolerance)
EULER_INT_TOL = 1e-3                      # (local) integer-quantization |e2-round(e2)|
TRIVIAL_FEULER_FLOOR = 1e-12             # (local) trivial-branch max|F^Euler| floor
NONTRIVIAL_FEULER_THR = 1e-6             # (local) nontrivial-branch localized-Pfaffian threshold
PFAFFIAN_NUM_FLOOR = 1e-14               # (local) real-Schur Pfaffian numerics floor (= 10x float eps)
ESTIMATOR_AGREE_TOL = max(1e-3, 0.05)   # (local) |e2_lattice - e2_cont| agreement
FD_EPS = 1e-5                            # (local) central-FD step for dD/d{tau,mu} in continuum arm
GAP_FLOOR = 1e-9                         # (local) near-degenerate gap guard (cross-multiplet only)
DEG_TOL = 1e-7                           # (local) J/PH-pair identification (reused S96 band_degeneracy)

# The 2-parameter U(2)-invariant TT directions (reused via s96.V_JENSEN / s96.V_MU)
V_JENSEN = s96.V_JENSEN                   # (local) (2,-2,1); |v|^2=9
V_MU = s96.V_MU                           # (local) (11,7,-8) = n x v_J; |v|^2=234; vol-preserving, perp-Jensen

# Output destinations
SCRIPT_PATH = Path(__file__).resolve()                                  # (local)
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"             # (local)
DK_BUILDER = SHARED_DIR / "dirac_spectrum.py"                           # (local)
S96_SCRIPT = SESSION_96_DIR / "s96_geom_offjensen_chern.py"             # (local)
S96_NPZ = SESSION_96_DIR / "s96_geom_offjensen_chern.npz"              # (local)
NPZ_OUT = SESSION_104_DIR / "s104_euler_class_j_doublet.npz"          # (local)
PNG_OUT = SESSION_104_DIR / "s104_euler_class_j_doublet.png"         # (local)


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema; mirrors S96 reference implementation)
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        try:
            rel = str(Path(p).resolve().relative_to(PROJECT_ROOT))  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  INPUT-PIN  {name}: {rel}  sha256={sha[:16]}...")
        pins[name] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit_sha256 = sha256(script_bytes + canonical_bytes + pinmap_json);
       content_sha256 = sha256(script_bytes).  (S84+ dual-SHA schema; plan
       audit_sha256_inputs=[script,canonical,pinmap], content_sha256_inputs=[script].)"""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()    # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=None):
    """Emit the verdict PAYLOAD for the dispatching AGENT to pass to the knowledge-MCP
    `emit_verdict` tool (race-safe; .claude/rules/gate-verdicts.md §"Race-Safe Emission").
    The script does NOT write the verdict file. [VERIFY] integer-quantization: no 3-tuple."""
    payload = {  # (local)
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": SCHEMA_VERSION,
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Pfaffian helper (real Schur; verified Pf^2 = det)
# ---------------------------------------------------------------------------
def pfaffian_2x2(A2):
    """Pfaffian of a 2x2 antisymmetric matrix [[0,f],[-f,0]] = f (the (0,1) entry)."""
    return 0.5 * (A2[0, 1] - A2[1, 0])   # robust to tiny symmetric round-off; = f for exact antisymmetric


def pfaffian_real_schur(A):
    """Pfaffian of an EVEN-dim real antisymmetric matrix via real Schur (scipy.linalg.schur).
       Real Schur block-diagonalizes A into 2x2 antisymmetric-like blocks; Pf = +/- prod of
       block (0,1) entries with the orthogonal-transform sign. We use it ONLY for the 2x2 case
       here (band_deg=2), so this reduces to pfaffian_2x2; retained for the Pf^2=det smoke test."""
    n = A.shape[0]
    A_anti = 0.5 * (A - A.T)              # (local) antisymmetrize against round-off
    T, Z = sla.schur(A_anti, output="real")
    pf = 1.0                              # (local)
    for k in range(0, n, 2):
        pf *= T[k, k + 1]
    pf *= np.linalg.det(Z)               # orthogonal-transform sign (det Z = +-1)
    return pf


def pf2_det_smoke():
    """Smoke test: Pf(A)^2 = det(A) for a random 4x4 antisymmetric. Returns residual."""
    rng = np.random.default_rng(0)
    A = rng.standard_normal((4, 4))
    A = A - A.T
    pf = pfaffian_real_schur(A)          # (local)
    return abs(pf * pf - np.linalg.det(A))


# ---------------------------------------------------------------------------
# Real-frame construction (S25/W5 reality: real gauge by Gram-Schmidt of real(u))
# ---------------------------------------------------------------------------
def real_frame_block(block):
    """Rotate the complex (dim, deg) lowest doublet to a REAL orthonormal frame.

    S25/W5: the eigenstates are REAL up to a global U(1) phase (Kosmann K_a anti-Hermitian).
    Construct a real (dim, deg) frame spanning the SAME degenerate subspace by deterministic
    Gram-Schmidt of {Re(col_k), Im(col_k)} -- the real and imaginary parts of the complex
    eigenvectors together span the real 2-plane; Gram-Schmidt extracts an orthonormal real
    basis. This is the unique-up-to-O(deg) real gauge; the Euler class is the O(deg) holonomy.

    Returns (R, ok): R = (dim, deg) real orthonormal frame (R^T R = I_deg); ok = reality flag
    (the real-imag span has rank deg). Phase-free and deterministic (NO random U(1) enters)."""
    dim, deg = block.shape
    # Candidate real vectors: real and imaginary parts of each complex eigenvector.
    cands = []  # (local)
    for k in range(deg):
        cands.append(block[:, k].real.astype(float))
        cands.append(block[:, k].imag.astype(float))
    # Deterministic Gram-Schmidt; keep the first `deg` vectors with norm above tol.
    Q = []  # (local) orthonormal real vectors
    for c in cands:
        v = c.copy()                                  # (local)
        for q in Q:
            v = v - (q @ v) * q
        nv = float(np.linalg.norm(v))                 # (local)
        if nv > 1e-9:
            Q.append(v / nv)
        if len(Q) == deg:
            break
    if len(Q) < deg:
        # Fallback: span did not reach rank deg from real/imag parts -> use real(block) GS only.
        Q = []
        for k in range(deg):
            v = block[:, k].real.astype(float).copy()  # (local)
            for q in Q:
                v = v - (q @ v) * q
            nv = float(np.linalg.norm(v))              # (local)
            if nv > 1e-12:
                Q.append(v / nv)
        ok = (len(Q) == deg)
    else:
        ok = True
    R = np.stack(Q[:deg], axis=1) if len(Q) >= deg else np.zeros((dim, deg))  # (local)
    return R, ok


def so2_log_angle(R):
    """Rotation angle f of a (near) 2x2 orthogonal frame-overlap matrix R.
       For a proper rotation [[c,-s],[s,c]] the antisymmetric log is [[0,-theta],[theta,0]]
       => the so(2) generator entry f = (R[1,0]-R[0,1])/2 normalized to the rotation angle.
       Uses atan2 on the rotation part; for a reflection (det<0) returns the rotation of the
       SO(2) part after stripping the reflection (det-sign tracked separately)."""
    detR = np.linalg.det(R)              # (local)
    if detR < 0:
        # O(2)\SO(2): split off a reflection; rotation angle of R . diag(1,-1)
        Rs = R @ np.diag([1.0, -1.0])    # (local) now det>0 (proper rotation)
    else:
        Rs = R
    # proper-rotation angle via atan2(sin, cos), cos=(tr)/2, sin=(Rs[1,0]-Rs[0,1])/2
    cth = 0.5 * (Rs[0, 0] + Rs[1, 1])    # (local)
    sth = 0.5 * (Rs[1, 0] - Rs[0, 1])    # (local)
    return float(np.arctan2(sth, cth)), float(detR)


# ---------------------------------------------------------------------------
# (A) LATTICE Pfaffian-Euler: real-frame SO(2) holonomy per plaquette
# ---------------------------------------------------------------------------
def fhs_pfaffian_euler(p, q, infra, taus, mus, deg):
    """Lattice Euler class of the lowest DEGENERATE band (deg) of D_K(sector (p,q)) over the
       (tau,mu) NODE grid via the real-frame SO(2) Wilson-loop holonomy (Pfaffian variant of FHS).

       Per plaquette, with real frames O(i,j)=(dim,deg):
         R_dir(i,j) = O(i,j)^T O(i+1_dir,j)        (real 2x2 frame overlap, ~orthogonal)
         W          = R_tau(i,j) R_mu(i+1,j) R_tau(i,j+1)^T R_mu(i,j)^T   (plaquette holonomy)
         F^Euler(i,j) = so2_log_angle(W)           (= Pf of the so(2) curvature = SO(2) angle)
         e2_lattice = (1/2pi) sum_{i,j} F^Euler(i,j).

       The real-gauge fix (deterministic Gram-Schmidt of real(u)) makes the frame O(2)-defined;
       the holonomy is the O(2) Wilson loop. Reflections (det<0 frame-overlaps) are det-tracked.
       Returns (e2_lattice, F_plaq, det_track, frame_ok_frac)."""
    n_tau = len(taus)
    n_mu = len(mus)
    frames = np.empty((n_tau, n_mu), dtype=object)     # (local) real frames (dim,deg)
    ok_count = 0                                        # (local)
    for i in range(n_tau):
        for jx in range(n_mu):
            blk, _, _, _ = s96.lowest_band_multiplet(taus[i], mus[jx], p, q, infra, deg, deg_tol=DEG_TOL)
            R, ok = real_frame_block(blk)
            frames[i, jx] = R
            ok_count += int(ok)
        if (i + 1) % 10 == 0:
            print(f"    [Pf-Euler] tau row {i+1}/{n_tau} (tau={taus[i]:.4f}) real frames built (deg={deg})")

    F_plaq = np.zeros((n_tau - 1, n_mu - 1))           # (local) plaquette Pfaffian (SO(2) angle)
    det_track = np.zeros((n_tau - 1, n_mu - 1))        # (local) plaquette holonomy det (reflection witness)
    for i in range(n_tau - 1):
        for jx in range(n_mu - 1):
            O00 = frames[i, jx]
            O10 = frames[i + 1, jx]
            O01 = frames[i, jx + 1]
            O11 = frames[i + 1, jx + 1]
            R_tau_00 = O00.T @ O10                     # link +tau at (i,j)
            R_mu_10 = O10.T @ O11                      # link +mu  at (i+1,j)
            R_tau_01 = O01.T @ O11                     # link +tau at (i,j+1)
            R_mu_00 = O00.T @ O01                      # link +mu  at (i,j)
            W = R_tau_00 @ R_mu_10 @ R_tau_01.T @ R_mu_00.T   # real-frame plaquette holonomy
            angle, detW = so2_log_angle(W)
            F_plaq[i, jx] = angle
            det_track[i, jx] = detW
    e2_lattice = float(np.sum(F_plaq) / (2.0 * np.pi))  # (local)
    return e2_lattice, F_plaq, det_track, ok_count / float(n_tau * n_mu)


# ---------------------------------------------------------------------------
# (B) CONTINUUM Pfaffian-Euler: so(2) part of the real-frame WZ curvature
# ---------------------------------------------------------------------------
def real_frame_at(tau, mu, p, q, infra, deg):
    """Real (dim,deg) frame O(tau,mu) of the lowest doublet at a continuum point."""
    blk, _, _, _ = s96.lowest_band_multiplet(tau, mu, p, q, infra, deg, deg_tol=DEG_TOL)
    R, _ = real_frame_block(blk)
    return R


def continuum_pfaffian_euler(p, q, infra, tau_c, mu_c, deg, h_loop):
    """Continuum Euler density Pf(Omega) on the plaquette-center grid via a GAUGE-INVARIANT local
       real-frame Wilson-loop holonomy (the SO(2) angle of a small closed loop of side h_loop,
       divided by the enclosed area), the same construction as the lattice estimator (A) but
       evaluated at the plaquette CENTERS on an independent fine-scale loop.

       WHY NOT the naive nested-FD of A_dir = O^T d_dir O: the real-gauge fix (Gram-Schmidt of
       real/imag parts of complex eigenvectors) is NOT smooth node-to-node -- the real/imag split
       flips discontinuously as the eigenvector's global U(1) phase rotates, so the nested central
       difference of A_dir is ill-conditioned (it blows up uniformly, NOT at the band crossing).
       The closed-loop Wilson holonomy is INVARIANT under that gauge-phase discontinuity (the
       arbitrary frame rotation at each corner cancels around the loop), so it is the correct
       gauge-invariant continuum cross-check -- this is precisely why FHS-type lattice methods
       exist. The local curvature is
         Pf(Omega)(t0,m0) = so2_angle( W_loop(t0,m0; h_loop) ) / h_loop^2
       with W_loop the side-h_loop real-frame plaquette holonomy centered at (t0,m0). Returns
       (Omega (N x N), max|Omega|, e2_cont)."""
    n = len(tau_c)
    m = len(mu_c)
    Omega = np.zeros((n, m))                            # (local) gauge-invariant local Pf curvature
    hl = h_loop                                         # (local) Wilson-loop side
    area = hl * hl                                      # (local) enclosed area
    for i in range(n):
        for jx in range(m):
            t0, m0 = tau_c[i], mu_c[jx]
            # four corners of a side-hl loop centered at (t0,m0): (-,-),(+,-),(+,+),(-,+)
            O00 = real_frame_at(t0 - 0.5 * hl, m0 - 0.5 * hl, p, q, infra, deg)
            O10 = real_frame_at(t0 + 0.5 * hl, m0 - 0.5 * hl, p, q, infra, deg)
            O11 = real_frame_at(t0 + 0.5 * hl, m0 + 0.5 * hl, p, q, infra, deg)
            O01 = real_frame_at(t0 - 0.5 * hl, m0 + 0.5 * hl, p, q, infra, deg)
            R_tau_00 = O00.T @ O10                     # link +tau (bottom edge)
            R_mu_10 = O10.T @ O11                      # link +mu  (right edge)
            R_tau_01 = O01.T @ O11                     # link +tau (top edge)
            R_mu_00 = O00.T @ O01                      # link +mu  (left edge)
            W = R_tau_00 @ R_mu_10 @ R_tau_01.T @ R_mu_00.T   # closed real-frame holonomy
            angle, _ = so2_log_angle(W)
            Omega[i, jx] = angle / area                # local so(2) curvature (Pf density)
        if (i + 1) % 10 == 0:
            print(f"    [cont-Euler] tau-center row {i+1}/{n} done")
    max_absOmega = float(np.max(np.abs(Omega)))        # (local)
    e2_cont = float(np.sum(Omega) * DTAU * DMU / (2.0 * np.pi))  # (local) midpoint rule
    return Omega, max_absOmega, e2_cont


# ---------------------------------------------------------------------------
# Kwon-Yang INFO companion: Provost-Vallee quantum metric (Re QGT) + R_ideal
# ---------------------------------------------------------------------------
def provost_vallee_metric(tau, mu, p, q, infra, deg):
    """Provost-Vallee quantum metric g_{ab} = Re QGT (a,b in {tau,mu}) of the lowest band-group
       (non-Abelian trace), from the SAME doublet eigendecomposition (NOT imported). The QGT is
         Q_{ab} = sum_{n in lowest} sum_{m not in lowest} <n|dH_a|m><m|dH_b|n>/(mu_n-mu_m)^2 ;
       g = Re Q, Omega = -2 Im Q. Returns g_2x2 (real symmetric)."""
    _, w, v, _ = s96.lowest_band_multiplet(tau, mu, p, q, infra, deg, deg_tol=DEG_TOL)
    aw = np.abs(w)
    order = np.argsort(aw)
    low_idx = list(order[:deg])                        # (local)
    low_set = set(low_idx)                             # (local)
    dH = {}                                            # (local)
    for ax in ("tau", "mu"):
        dH[ax] = 1j * s96.dD_dparam(tau, mu, p, q, infra, ax)
    Amat = {ax: v.conj().T @ dH[ax] @ v for ax in ("tau", "mu")}  # (local)
    n_dim = len(w)
    Q = np.zeros((2, 2), dtype=complex)                # (local) (tau,mu) QGT
    axes = ["tau", "mu"]
    for a in range(2):
        for b in range(2):
            qab = 0.0 + 0.0j                           # (local)
            for n_idx in low_idx:
                for mm in range(n_dim):
                    if mm in low_set:
                        continue
                    denom = (w[n_idx] - w[mm]) ** 2
                    if denom < GAP_FLOOR:
                        continue
                    qab += Amat[axes[a]][n_idx, mm] * Amat[axes[b]][mm, n_idx] / denom
            Q[a, b] = qab
    g = Q.real                                         # (local) Provost-Vallee metric
    return 0.5 * (g + g.T)                             # symmetrize


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    print("=" * 78)
    print(f"{GATE_ID}  --  Euler class of the lowest J/BDI-real Dirac doublet")
    print("  the characteristic class a REAL rank-2 bundle carries (Pf of the so(2) curvature)")
    print("  S96 measured Chern (U(1)/arg-det) = 0; this gate measures Euler (SO(2)/Pfaffian)")
    print("=" * 78)

    # --- input pins + dual SHA ---
    pins = log_input_pins({
        "canonical_constants": CANONICAL_CONSTANTS,
        "s96_chern_script": S96_SCRIPT,
        "s96_chern_npz": S96_NPZ,
        "dirac_spectrum": DK_BUILDER,
    })
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # --- Pfaffian smoke test (Pf^2 = det) ---
    pf_resid = pf2_det_smoke()                          # (local)
    print(f"  Pf^2=det smoke test (random 4x4 antisym): residual = {pf_resid:.3e} "
          f"(floor {PFAFFIAN_NUM_FLOOR:.0e}) {'OK' if pf_resid < 1e-12 else 'WARN'}")

    # --- geometry self-check (Sage-verified relations) ---
    n_vol = np.array([1.0, 3.0, 4.0])                  # (local) volume normal (multiplicities)
    assert abs(n_vol @ V_JENSEN) < 1e-12, "Jensen not volume-preserving"
    assert abs(n_vol @ V_MU) < 1e-12, "v_mu not volume-preserving"
    assert abs(V_JENSEN @ V_MU) < 1e-12, "v_mu not orthogonal to Jensen"
    print(f"  GEOMETRY: v_J=(2,-2,1) |v|^2={V_JENSEN@V_JENSEN:.0f}; "
          f"v_mu=(11,7,-8)=n x v_J |v|^2={V_MU@V_MU:.0f}; vol-preserving & perp-Jensen OK")

    infra = s96.build_su3_infra()

    # --- confirm band_deg=2 at the fold (S96 baseline) ---
    deg_bot, lam_bot = s96.band_degeneracy(tau_fold, 0.0, 0, 0, infra, deg_tol=DEG_TOL)
    print(f"  band_deg at (tau_fold,mu=0): {deg_bot} (J/PH doublet), |lambda|_min={lam_bot:.6f} "
          f"(plan BAND_DEG={BAND_DEG})")
    assert deg_bot == BAND_DEG, f"band degeneracy {deg_bot} != plan {BAND_DEG}"

    # --- NODE grid ---
    taus = np.linspace(TAU_LO, TAU_HI, N_NODE)         # (local)
    mus = np.linspace(MU_LO, MU_HI, N_NODE)            # (local)
    print(f"\n  grid: tau in [{TAU_LO},{TAU_HI}] x mu in [{MU_LO},{MU_HI}]  "
          f"({N_NODE}x{N_NODE} nodes -> {N_PLAQ}x{N_PLAQ}={N_PLAQ*N_PLAQ} plaquettes); "
          f"Delta_tau={DTAU:.4f} Delta_mu={DMU:.4f}; fold tau={tau_fold} enclosed at mu=0")

    # =====================================================================
    # (A) LATTICE Pfaffian-Euler on the canonical bottom band (0,0)
    # =====================================================================
    print("\n  [A LATTICE] FHS-Pfaffian-Euler: real-frame SO(2) Wilson-loop holonomy")
    e2_lattice, F_plaq, det_track, frame_ok_frac = fhs_pfaffian_euler(0, 0, infra, taus, mus, deg_bot)
    max_absF = float(np.max(np.abs(F_plaq)))           # (local)
    n_reflections = int(np.sum(det_track < 0))         # (local) plaquettes whose holonomy is a reflection
    print(f"    e2_lattice = {e2_lattice:.6e}; round={round(e2_lattice)}; "
          f"|e2-round|={abs(e2_lattice-round(e2_lattice)):.3e}; max|F^Euler|={max_absF:.3e}")
    print(f"    real-frame rank-ok fraction = {frame_ok_frac:.4f}; "
          f"reflection plaquettes (detW<0) = {n_reflections}/{F_plaq.size}")

    # --- map gap12 (B1/B2 von Neumann-Wigner crossing at the (0.10,+0.10) corner per S100b) ---
    # The corner-crossing defect manifests as an isolated large-|F^Euler| plaquette. Locate it and
    # report a defect-excluded companion (the dominant single plaquette removed).
    flat = np.abs(F_plaq).ravel()                      # (local)
    imax = int(np.argmax(flat))                        # (local)
    ci, cj = np.unravel_index(imax, F_plaq.shape)      # (local) dominant plaquette index
    tau_corner = 0.5 * (taus[ci] + taus[ci + 1])       # (local)
    mu_corner = 0.5 * (mus[cj] + mus[cj + 1])          # (local)
    e2_lattice_defect_excluded = float((np.sum(F_plaq) - F_plaq[ci, cj]) / (2.0 * np.pi))  # (local)
    print(f"    gap12 map: dominant |F^Euler| plaquette at (tau,mu)=({tau_corner:.4f},{mu_corner:.4f}) "
          f"value={F_plaq[ci,cj]:.3e}; defect-excluded e2={e2_lattice_defect_excluded:.6e}")

    # =====================================================================
    # (B) CONTINUUM Pfaffian-Euler cross-check (so(2) part of real-frame WZ curvature)
    # =====================================================================
    print("\n  [B CONTINUUM] gauge-invariant local Wilson-loop Pf curvature (plaquette centers)")
    tau_c = 0.5 * (taus[:-1] + taus[1:])               # (local)
    mu_c = 0.5 * (mus[:-1] + mus[1:])                  # (local)
    H_LOOP = DTAU                                       # (local) continuum center-loop side (= one plaquette scale; independent of node grid)
    Omega_cont, max_absOmega, e2_cont = continuum_pfaffian_euler(0, 0, infra, tau_c, mu_c, deg_bot, H_LOOP)
    print(f"    max|Omega_cont(Pf)| = {max_absOmega:.3e} (gauge-invariant; immune to gauge-phase "
          f"discontinuity); e2_cont = (1/2pi) int Pf(Omega) dtau dmu = {e2_cont:.6e}")

    # =====================================================================
    # Kwon-Yang INFO companion: R_ideal = ||g - F12 omega|| / ||g|| at the fold
    # =====================================================================
    print("\n  [INFO] Kwon-Yang ideal-condition residual at the fold (g = Provost-Vallee, computed)")
    g_fold = provost_vallee_metric(tau_fold, 0.0, 0, 0, infra, deg_bot)  # (local)
    # Berry curvature (so(2) Pf) at the fold continuum point (closest center to mu=0).
    j_mid = int(np.argmin(np.abs(mu_c)))               # (local) nearest center to mu=0
    i_fold = int(np.argmin(np.abs(tau_c - tau_fold)))  # (local)
    F12_fold = Omega_cont[i_fold, j_mid]               # (local) so(2) Pf curvature at the fold
    g_norm = float(np.linalg.norm(g_fold))             # (local)
    omega_munu = np.array([[0.0, 1.0], [-1.0, 0.0]])   # (local) symplectic form on (tau,mu)
    R_ideal = float(np.linalg.norm(g_fold - F12_fold * omega_munu) / max(g_norm, 1e-300))  # (local)
    g_trace = float(np.trace(g_fold))                  # (local) ~ quantum-metric reservoir cross-check
    print(f"    g_fold (Provost-Vallee, computed) = [[{g_fold[0,0]:.4e},{g_fold[0,1]:.4e}],"
          f"[{g_fold[1,0]:.4e},{g_fold[1,1]:.4e}]]; tr(g)={g_trace:.4e}")
    print(f"    F12(Pf) at fold = {F12_fold:.4e}; R_ideal = ||g - F12 omega||/||g|| = {R_ideal:.4e}")
    print(f"    (atlas-07 reservoir g~982.5 is a methodological cross-check ONLY; NOT imported)")

    # =====================================================================
    # VERDICT (plan §W2-1 operator.form)
    # =====================================================================
    print("\n" + "=" * 78)
    print("  VERDICT")
    print("=" * 78)
    e2 = e2_lattice                                                       # (local) primary estimator
    is_integer = abs(e2 - round(e2)) <= EULER_INT_TOL                     # (local)
    n_round = round(e2)                                                   # (local)
    estimators_agree = abs(e2_lattice - e2_cont) <= ESTIMATOR_AGREE_TOL  # (local)
    # n_plaq_above = number of plaquettes carrying nontrivial-threshold curvature (the gap12
    # B1/B2 von Neumann-Wigner corner-crossing defect manifests as EXACTLY ONE dominant plaquette).
    n_plaq_above = int(np.sum(np.abs(F_plaq) > NONTRIVIAL_FEULER_THR))    # (local)
    # corner-crossing defect dominates (pre-registered INFO branch iii, plan §W2-1 INFO_meaning):
    # a single plaquette accounts for the entire raw-e2 non-quantization, AND removing it the
    # defect-excluded e2 quantizes cleanly to 0 (the S100b spurious class). This is INDEPENDENT
    # of whether round(raw e2) happens to land on 0 (here it does) or on n (the predicate must
    # catch both -- the prior bug required n_round!=0 and missed the round-lands-on-0 case).
    defect_excl_quantized_0 = (
        abs(e2_lattice_defect_excluded - round(e2_lattice_defect_excluded)) <= EULER_INT_TOL
        and round(e2_lattice_defect_excluded) == 0
        and abs(e2_lattice_defect_excluded) < TRIVIAL_FEULER_FLOOR
    )                                                                     # (local)
    corner_defect_dominates = (n_plaq_above == 1) and defect_excl_quantized_0  # (local)
    # clean trivial branch: NO plaquette above the nontrivial threshold AND quantized to 0
    trivial_branch = (n_round == 0) and (max_absF < TRIVIAL_FEULER_FLOOR)      # (local)
    nontrivial_branch = (n_round != 0) and (max_absF > NONTRIVIAL_FEULER_THR) \
        and (n_plaq_above > 1)                                                 # (local) genuine extended nonzero field

    if corner_defect_dominates:
        # pre-registered INFO branch (iii): single corner-crossing plaquette dominates; the
        # gauge-invariant lattice defect-excluded Euler class is 0 (PASS-TRIVIAL content), but
        # the raw estimator is non-quantized by the documented S100b B1/B2 vN-Wigner gap-closure.
        verdict = "INFO"
        branch = "corner-crossing-defect-dominates"
    elif not is_integer:
        verdict = "FAIL"
        branch = "non-integer-e2"
    elif trivial_branch and estimators_agree:
        verdict = "PASS"
        branch = "PASS-TRIVIAL"
    elif nontrivial_branch and estimators_agree:
        verdict = "PASS"
        branch = "PASS-NONTRIVIAL"
    else:
        verdict = "INFO"
        branch = "marginal-or-estimator-disagreement"

    value_str = (
        f"e2={e2:.6e}_round={n_round}_branch={branch}_"
        f"maxFEuler={max_absF:.3e}_e2_cont={e2_cont:.6e}_"
        f"e2_defectExcl={e2_lattice_defect_excluded:.6e}_nPlaqAbove={n_plaq_above}_"
        f"R_ideal={R_ideal:.4e}_estAgree={estimators_agree}_pf2detResid={pf_resid:.2e}"
    )
    print(f"  e2_lattice = {e2:.6e}  (round={n_round}, |e2-round|={abs(e2-n_round):.3e} vs tol {EULER_INT_TOL})")
    print(f"  e2_cont (so(2) Pf) = {e2_cont:.6e}   lattice/cont agree: {estimators_agree} "
          f"(|diff|={abs(e2_lattice-e2_cont):.3e} vs {ESTIMATOR_AGREE_TOL})")
    print(f"  max|F^Euler| = {max_absF:.3e}  (trivial floor {TRIVIAL_FEULER_FLOOR:.0e}, "
          f"nontrivial thr {NONTRIVIAL_FEULER_THR:.0e})")
    print(f"  R_ideal (Kwon-Yang) = {R_ideal:.4e}  tr(g_PV)={g_trace:.4e}")
    print(f"  >>> {GATE_ID}: {verdict}  [{branch}]")

    # --- save data ---
    SESSION_104_DIR.mkdir(parents=True, exist_ok=True)
    np.savez(
        NPZ_OUT,
        taus=taus, mus=mus, tau_centers=tau_c, mu_centers=mu_c,
        F_plaq=F_plaq, det_track=det_track, Omega_cont=Omega_cont,
        e2_lattice=e2_lattice, e2_cont=e2_cont,
        e2_lattice_defect_excluded=e2_lattice_defect_excluded,
        max_absF=max_absF, max_absOmega=max_absOmega,
        n_round=n_round, frame_ok_frac=frame_ok_frac, n_reflections=n_reflections,
        n_plaq_above=n_plaq_above, corner_defect_dominates=corner_defect_dominates,
        corner_plaq_ij=np.array([ci, cj]),
        corner_tau_mu=np.array([tau_corner, mu_corner]),
        g_fold=g_fold, F12_fold=F12_fold, R_ideal=R_ideal, g_trace=g_trace,
        pf2det_residual=pf_resid,
        estimators_agree=estimators_agree, is_integer=is_integer,
        band_deg=int(deg_bot), v_jensen=V_JENSEN, v_mu=V_MU,
        verdict=verdict, branch=branch, tau_fold=float(tau_fold),
        scan_tau=np.array([TAU_LO, TAU_HI]), scan_mu=np.array([MU_LO, MU_HI]),
        c_fhs_s96_chern=9.777563e-15,
    )
    print(f"\n  Saved data: {NPZ_OUT}")

    # --- plot: F^Euler(tau,mu) heatmap + continuum so(2) Pf curvature ---
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    ext = [MU_LO, MU_HI, TAU_LO, TAU_HI]               # (local) [mu (x), tau (y)]
    capF = max(max_absF, 1e-300)                       # (local)
    im0 = axes[0].imshow(F_plaq, origin="lower", aspect="auto", extent=ext,
                         cmap="RdBu_r", vmin=-capF, vmax=capF)
    axes[0].axhline(tau_fold, color="k", ls="--", lw=1.2, label=f"fold tau={tau_fold}")
    axes[0].axvline(0.0, color="green", ls=":", lw=1.4, label="Jensen line (mu=0)")
    axes[0].plot(mu_corner, tau_corner, "x", color="magenta", ms=10, mew=2,
                 label="gap12 dominant plaq")
    axes[0].set_xlabel("mu (second U(2)-inv TT direction)")
    axes[0].set_ylabel("tau (Jensen direction)")
    axes[0].set_title(f"FHS-Pfaffian-Euler field strength F^Euler (SO(2) angle)\n"
                      f"e2_lattice={e2_lattice:.3e} (round={n_round}); max|F^Euler|={max_absF:.2e}")
    axes[0].legend(loc="upper right", fontsize=8)
    fig.colorbar(im0, ax=axes[0], label="F^Euler (rad)")

    capO = max(max_absOmega, 1e-300)                   # (local)
    im1 = axes[1].imshow(Omega_cont, origin="lower", aspect="auto", extent=ext,
                         cmap="RdBu_r", vmin=-capO, vmax=capO)
    axes[1].axhline(tau_fold, color="k", ls="--", lw=1.2)
    axes[1].axvline(0.0, color="green", ls=":", lw=1.4)
    axes[1].set_xlabel("mu")
    axes[1].set_ylabel("tau")
    axes[1].set_title(f"Continuum so(2) Pf Berry curvature Omega\n"
                      f"e2_cont={e2_cont:.3e}; VERDICT={verdict} [{branch}]")
    fig.colorbar(im1, ax=axes[1], label="Pf(Omega)")

    fig.suptitle(f"{GATE_ID}: Euler class of the lowest BDI-real Dirac doublet on the "
                 f"2-param U(2)-inv TT surface\n(S96 Chern=0 was the WRONG class for a real "
                 f"bundle; the Pfaffian/SO(2) Euler class is the right one)", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(PNG_OUT, dpi=150)
    print(f"  Saved plot: {PNG_OUT}")

    # --- emit verdict payload (agent calls emit_verdict; race-safe) ---
    euler_companion = (
        f"# {GATE_ID} dual-SHA companion row; [VERIFY] Euler class e2=(1/2pi)oint Pf(F^Euler) of the "
        f"lowest 2-fold J/BDI-real Dirac doublet on the 2-param U(2)-inv TT surface (v_J=(2,-2,1), "
        f"v_mu=n x v_J=(11,7,-8)); FHS-Pfaffian-Euler real-frame SO(2) Wilson-loop lattice cross-checked "
        f"vs continuum so(2)-curvature Pf; S96 measured Chern (arg-det)=0 (C_FHS=9.78e-15) -- this gate "
        f"measures the SO(2)/Pfaffian Euler class a REAL rank-2 bundle carries; Pf^2=det residual "
        f"{pf_resid:.1e}; R_ideal(Kwon-Yang)={R_ideal:.3e}; CLASS=FULL (exact eigendecomposition, NO "
        f"SCHEMATIC); no regulator_pin (Euler class is a property of the D_K eigenbundle, not a "
        f"Seeley-DeWitt a_n)"
    )
    print_verdict_payload(verdict, value_str, audit_sha, content_sha, extra_rows=[euler_companion])
    print(f"\n  4-tuple: (value={value_str[:60]}..., scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
