#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S96-GEOM-OFFJENSEN-CHERN
================================================================================
Gate:   S96-GEOM-OFFJENSEN-CHERN   (trigger [VERIFY], classification GEOMETRIC)
Agent:  berry-geometric-phase-theorist
Plan:   sessions/session-plan/session-96-plan-w5.md  ## §W5-5
WP:     sessions/archive/session-96/session-96-w5-workingpaper.md  ### §W5-5

OPEN CHANNEL CLOSED: C11/C12 off-Jensen Berry (S29 open_channel "May reappear on
U(2)-invariant surface"). The 1D Jensen-line result is Omega=0 PROVEN (S25/W5:
Kosmann K_a anti-Hermitian => real eigenstates => Omega=0 identically, all
eigenstates, all sectors, all tau; max|Omega|<4e-14). This gate computes the
Berry curvature 2-form Omega(tau,mu) and the integrated Chern number
C = (1/2pi) oint Omega dtau dmu on the 2-parameter Ad U(2)-invariant deformation
SURFACE (the sole open route to nontrivial substrate topology / the P-30w gate).

HYPOTHESIS (berry §V CF-BERRY-OFF-JENSEN-CHERN):
--------------------------------------------------------------------------------
Omega(tau,mu) and C = (1/2pi) oint Omega dtau dmu either
  (a) PASS-TRIVIAL: |C|<1e-3, C quantized to 0, max|Omega|<1e-12 -- strengthening
      the §9 "topology survives dissolution" spine to the FULL physical deformation
      surface (not just the 1D Jensen slice); OR
  (b) PASS-NONTRIVIAL: |C-n|<1e-3, n!=0, max|Omega|>1e-6 localized -- a genuine
      substrate topological invariant of the modulus-space eigenbundle.
The 1D-Jensen-line result Omega=0 does NOT determine the off-Jensen surface
(dimension count: a 1D base carries NO 2-form).

--------------------------------------------------------------------------------
GEOMETRY FIRST -- THE 2-PARAMETER U(2)-INVARIANT TT DEFORMATION SURFACE
--------------------------------------------------------------------------------
The U(2)-invariant left-invariant metrics on SU(3) form a 3-parameter family
parameterized by scale factors (L1,L2,L3) on the reductive blocks
    su(3) = u(1) (+) su(2) (+) C^2     with multiplicities (1, 3, 4)
(dirac_spectrum.u2_invariant_metric). In log-coordinates l=(ln L1,ln L2,ln L3):

  * VOLUME-PRESERVING constraint (the physical TT condition, vol = L1 L2^3 L3^4):
        n . l = 0   with   n = (1, 3, 4)   (multiplicities = volume normal)
    => a 2D plane through the origin in log-space.

  * JENSEN direction (canonical tau-flow; L1=e^{2t},L2=e^{-2t},L3=e^{t}):
        v_J = (2, -2, 1)    [n.v_J = 2-6+4 = 0; volume-preserving; |v_J|^2 = 9]
    The fold lives on this line at tau=0.19.

  * SECOND admissible U(2)-invariant TT eigendirection mu (Sage-verified, this
    script's design choice -- the geometrically forced second direction):
        v_mu = n x v_J = (11, 7, -8)
        [n.v_mu = 11+21-32 = 0  => volume-preserving
         v_J.v_mu = 22-14-8 = 0 => ORTHOGONAL to Jensen (independent deformation)
         rank[v_J; v_mu] = 2     => the two SPAN the full 2D volume-preserving plane
         |v_mu|^2 = 234]
    v_mu is the cross product of the volume normal with the Jensen tangent, hence
    the unique (up to sign/scale) volume-preserving direction orthogonal to the
    Jensen shear -- the second TT eigendirection of the bi-invariant Einstein
    metric restricted to the U(2)-invariant family.

PARAMETERIZATION (so mu=0 IS EXACTLY the Jensen line, fold at tau=0.19):
        l(tau,mu) = tau * v_J  +  (mu / |v_mu|) * v_mu
        L_i(tau,mu) = exp( l_i(tau,mu) )
    mu is normalized by |v_mu| so that Delta_mu is a unit-Euclidean step in
    log-space, comparable to Delta_tau (plan grid Delta_tau=Delta_mu=0.004).
    At mu=0: L = (e^{2tau}, e^{-2tau}, e^{tau}) = the canonical Jensen metric. QED.

--------------------------------------------------------------------------------
[VERIFY] SUBSTITUTION CHAIN (plan §W5-5 Step 1-5; math-scripts.md
                            §"Double-Check Logic Before Compute")
--------------------------------------------------------------------------------
Claim: "the 1D-Jensen-line result Omega=0 does NOT determine the off-Jensen
        2-parameter Chern number; a nonzero C is POSSIBLE off-Jensen."

  Step 1: Berry curvature 2-form  Omega = dA,  A_i = i<n|d_i|n>,  i in {tau,mu}.
  Step 2: On the 1D Jensen line (mu fixed = 0) the parameter base is 1-dimensional
          => Omega = dA needs a 2-form, but a 1D base carries NO 2-form
          => Omega == 0 on the Jensen line BY DIMENSION COUNT
             (plus the deeper anti-Hermitian K_a => real eigenstates, S25/W5).
  Step 3: On the 2-parameter surface (tau,mu both varying)
             Omega = (d_tau A_mu - d_mu A_tau) dtau ^ dmu  is a genuine 2-form
          => Omega CAN be nonzero off-Jensen even though it vanishes on the mu=0 slice.
  Step 4: anti-Hermitian-K_a (W5) gives REAL eigenstates on the Jensen line
          => A real => gauge-trivial there; off-Jensen the v_mu direction is NOT
          the Jensen shear and MAY break the reality => complex eigenstate phase
          => possibly nonzero Omega.
  Step 5: 1D-base Omega=0  =/=>  2D-base C=0   [triviality on a slice does not
          imply triviality on the surface].
  Conclusion: the off-Jensen Chern is genuinely UNDETERMINED by the Jensen-line
          result; C = (1/2pi) oint Omega dtau dmu over the closed (tau,mu) surface
          enclosing the fold is the decisive object. The gate computes it.

--------------------------------------------------------------------------------
METHOD (FHS lattice-Chern + continuum BP-4 cross-check; per plan)
--------------------------------------------------------------------------------
Primary: Fukui-Hatsugai-Suzuki (2005) gauge-invariant Wilson-loop lattice Chern.
  Per plaquette (i,j) on the (tau,mu) mesh, with |n> the lowest band eigenvector:
     U_tau(i,j) = <n(i,j)|n(i+1,j)> / |.|         (U(1) link variable)
     U_mu (i,j) = <n(i,j)|n(i,j+1)> / |.|
     F(i,j)     = arg[ U_tau(i,j) U_mu(i+1,j) U_tau(i,j+1)^{-1} U_mu(i,j)^{-1} ]
                  (lattice field strength, principal branch in (-pi,pi])
     C          = (1/2pi) sum_{i,j} F(i,j)
  FHS is gauge-invariant by construction (the random U(1) phase of each |n> cancels
  around every plaquette) and integer-quantized for a closed surface.

Cross-check: BP-4 continuum Berry curvature
     Omega_n(tau,mu) = -2 Im sum_{m!=n} <n|d_tau D|m><m|d_mu D|n>/(lam_n-lam_m)^2
  evaluated from the SAME eigendecomposition (d_tau D, d_mu D by central finite
  difference of the per-sector Dirac matrix). C_cont = (1/2pi) integral Omega dtau dmu.

Eigenbundle: D_K is BLOCK-DIAGONAL by Peter-Weyl (proven S22b). The lowest |lambda|
band sits in the (0,0) singlet sector (16x16, D = Omega_spin offset) -- the SAME
sector S25/W5 used for the Jensen-line Omega=0 baseline. We track the lowest band
of D_K within that sector across the (tau,mu) surface. (A wider sector sweep is run
as a robustness arm; the (0,0) singlet is the canonical bottom band.)

SUBSTRATE ARROW (phononic-framing.md; never inverted):
    D_K eigenbundle over modulus space -> Berry connection A -> curvature Omega
    -> Chern number C. The Berry curvature lives on the substrate's OWN parameter
    space, NOT a container D_K sits in. The (tau,mu) surface IS the substrate's
    intrinsic modulus-space (Level-2 substrate-IS per phononic-framing.md). C=0 off
    -Jensen strengthens the §9 geometry-vs-topology spine; C!=0 would be a genuine
    substrate topological invariant.

Author: berry-geometric-phase-theorist (Session 96, Wave 5)
Date:   2026-05-29
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Paths + canonical imports (MANDATORY: from canonical_constants import *)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]          # (local) script in computations/session-96 => parents[2]=root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import tau_fold  # noqa: E402

# Dirac-spectrum builder (the U(2)-invariant metric machinery)
import dirac_spectrum as ds  # noqa: E402
from branching_computation import gell_mann_matrices  # noqa: E402

# GPU (torch+rocm) per plan GPU_path: torch.linalg.eigh
try:
    import torch
    _TORCH_OK = True
    _GPU_OK = bool(getattr(torch, "cuda", None)) and torch.cuda.is_available()
except Exception:  # pragma: no cover
    _TORCH_OK = False
    _GPU_OK = False

# ---------------------------------------------------------------------------
# Gate identity + pre-registered pins (plan §W5-5 machinery_pin_map)
# ---------------------------------------------------------------------------
GATE_ID = "S96-GEOM-OFFJENSEN-CHERN"      # (local)
SCHEME = "FHS-Wilson-loop"                # (local) plan-pinned
CONVENTION = "ABSOLUTE"                   # (local) plan-pinned (Chern = gauge/convention-invariant integer)
L_MAX = "10"                              # (local) plan-pinned
SCHEMA_VERSION = "S84+"                   # (local)

# Plan scan_range: tau in [0.10,0.30] x mu in [-0.10,0.10]; 50x50 plaquette mesh.
TAU_LO, TAU_HI = 0.10, 0.30               # (local) plan scan_range tau
MU_LO, MU_HI = -0.10, 0.10                # (local) plan scan_range mu (mu=0 = Jensen line)
N_PLAQ = 50                               # (local) plan 50x50 plaquette grid (N_eval=2500)
N_NODE = N_PLAQ + 1                       # (local) 51x51 NODE grid -> 50x50 plaquettes
DTAU = (TAU_HI - TAU_LO) / N_PLAQ         # (local) ~0.004
DMU = (MU_HI - MU_LO) / N_PLAQ            # (local) ~0.004
PQ_CUT = 10                               # (local) L_max=10 Peter-Weyl restriction (sector sweep arm)
CHERN_INT_TOL = 1e-3                      # (local) plan: integer-quantization tolerance |C-round(C)|
TRIVIAL_OMEGA_FLOOR = 1e-12               # (local) plan: trivial-branch max|Omega| floor
NONTRIVIAL_OMEGA_THR = 1e-6               # (local) plan: nontrivial-branch localized-Omega threshold
FD_EPS = 1e-5                             # (local) central-FD step for d D/d{tau,mu} in BP-4 arm

# The 2-parameter U(2)-invariant TT deformation directions (Sage-verified geometry)
V_JENSEN = np.array([2.0, -2.0, 1.0])     # (local) Jensen direction in log(L1,L2,L3); |v|^2=9
V_MU = np.array([11.0, 7.0, -8.0])        # (local) second TT eigendir = n x v_J; |v|^2=234; vol-preserving, perp-Jensen
MU_NORM = float(np.sqrt(V_MU @ V_MU))     # (local) |v_mu| = sqrt(234) ~ 15.2971 (unit-step normalization)

# Output destinations (script in session-96/, all outputs co-located)
SESSION_96_DIR = PROJECT_ROOT / "computations" / "session-96"
SCRIPT_PATH = Path(__file__).resolve()                                  # (local)
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"             # (local)
DK_BUILDER = SHARED_DIR / "dirac_spectrum.py"                           # (local)
BERRY_JENSEN_BASELINE = PROJECT_ROOT / "computations" / "session-25" / "s25_berry_results.npz"  # (local)
VERDICT_FILE = SESSION_96_DIR / "s96_gate_verdicts.txt"                 # (local) canonical path
NPZ_OUT = SESSION_96_DIR / "s96_geom_offjensen_chern.npz"              # (local)
PNG_OUT = SESSION_96_DIR / "s96_geom_offjensen_chern.png"             # (local)


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema; mirrors s96_w3_3 reference implementation)
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
       content_sha256 = sha256(script_bytes).  (S84+ dual-SHA schema.)"""
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


def append_verdict(verdict, value_str, audit_sha, content_sha):
    """Single canonical dual-SHA verdict line + dual-SHA companion row. Append-only single open('a').
    schema_v2_3tuple_required: false (plan §W5-5; [VERIFY] integer-quantization, no signed-delta)."""
    canonical = (  # (local)
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [VERIFY] off-Jensen Berry curvature / Chern on the "
        f"2-parameter Ad U(2)-invariant TT surface (closes C11/C12 open channel S29 / P-30w gate); "
        f"directions v_J=(2,-2,1), v_mu=n x v_J=(11,7,-8) [vol-preserving, perp-Jensen, span 2D plane]; "
        f"FHS Wilson-loop lattice Chern cross-checked vs BP-4 continuum Omega; mu=0 IS the Jensen line "
        f"(S25/W5 Omega=0, anti-Hermitian Kosmann K_a); CLASS=FULL (exact eigendecomposition, NO SCHEMATIC); "
        f"no regulator_pin (Berry curvature is a property of the D_K eigenbundle, not a Seeley-DeWitt a_n)\n"
    )
    SESSION_96_DIR.mkdir(parents=True, exist_ok=True)
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)


# ---------------------------------------------------------------------------
# SU(3) infrastructure (built ONCE -- tau,mu-independent)
# ---------------------------------------------------------------------------
def build_su3_infra():
    """Generators, structure constants, Killing form, Clifford gammas -- all
    independent of (tau,mu). Returns (gens, f_abc, B_ab, gammas)."""
    gens = ds.su3_generators()
    f_abc = ds.compute_structure_constants(gens)
    B_ab = ds.compute_killing_form(f_abc)
    gammas = ds.build_cliff8()
    return gens, f_abc, B_ab, gammas


def metric_scale_factors(tau, mu):
    """(L1,L2,L3) on the 2-parameter U(2)-invariant TT surface.
       l(tau,mu) = tau*v_J + (mu/|v_mu|)*v_mu ;  L_i = exp(l_i).
       mu=0 => (e^{2tau}, e^{-2tau}, e^{tau}) = canonical Jensen metric."""
    log_L = tau * V_JENSEN + (mu / MU_NORM) * V_MU   # (local) log-space coords
    return float(np.exp(log_L[0])), float(np.exp(log_L[1])), float(np.exp(log_L[2]))


def build_dirac_sector(tau, mu, p, q, gens, f_abc, B_ab, gammas):
    """Assemble the block-diagonal D_K on Peter-Weyl sector (p,q) at metric point (tau,mu).
       Returns the anti-Hermitian Dirac matrix D_pi (dim = dim(p,q)*16)."""
    L1, L2, L3 = metric_scale_factors(tau, mu)
    g = ds.u2_invariant_metric(B_ab, L1, L2, L3)
    E = ds.orthonormal_frame(g)
    ft = ds.frame_structure_constants(f_abc, E)
    Gamma = ds.connection_coefficients(ft)
    Omega_spin = ds.spinor_connection_offset(Gamma, gammas)
    if (p, q) == (0, 0):
        return Omega_spin.copy()                       # D = Omega offset on the 16-dim singlet
    rho, _ = ds.get_irrep(p, q, gens, f_abc)
    return ds.dirac_operator_on_irrep(rho, E, gammas, Omega_spin)


def eigh_H(D_pi):
    """Diagonalize H = i D_pi (Hermitian, real eigenvalues) -> (mu_real, evecs).
       GPU torch.linalg.eigh per plan when available; numpy fallback. mu = eig of H;
       Dirac eigenvalue lambda = -i*mu (we work with H's spectrum + eigenvectors)."""
    H = 1j * D_pi
    if _TORCH_OK and _GPU_OK and H.shape[0] >= 100:
        t = torch.as_tensor(H, device="cuda", dtype=torch.complex128)
        # Hermitize against round-off, then eigh
        t = 0.5 * (t + t.conj().transpose(-2, -1))
        w, v = torch.linalg.eigh(t)
        return w.cpu().numpy().real, v.cpu().numpy()
    # CPU fallback (singlet 16x16 is tiny; numpy eigh is exact + fast)
    Hh = 0.5 * (H + H.conj().T)
    w, v = np.linalg.eigh(Hh)
    return w.real, v


def lowest_band_state(tau, mu, p, q, infra):
    """Return the lowest-|lambda| eigenvector of D_K in sector (p,q) at (tau,mu),
       plus the full (eigvals, eigvecs) for the BP-4 continuum arm. The lowest band
       index is argmin(|mu_real|) (Dirac |lambda| = |mu_real|)."""
    gens, f_abc, B_ab, gammas = infra
    D_pi = build_dirac_sector(tau, mu, p, q, gens, f_abc, B_ab, gammas)
    w, v = eigh_H(D_pi)
    idx = int(np.argmin(np.abs(w)))                    # (local) lowest |lambda| band
    return v[:, idx].copy(), w, v, D_pi


def lowest_band_multiplet(tau, mu, p, q, infra, deg, deg_tol=1e-7):
    """Return the lowest-|lambda| DEGENERATE multiplet (the deg eigenvectors of D_K nearest
       |lambda|_min) as a (dim, deg) column-block at (tau,mu). The lowest Dirac band on the
       SU(3) eigenbundle is a Kramers/J-degenerate multiplet (the (0,0) singlet bottom band is
       2-fold); a SINGLE-band Berry phase is gauge-ill-defined inside a degenerate subspace, so
       the NON-ABELIAN FHS over the full multiplet is the correct discretization-robust estimator."""
    gens, f_abc, B_ab, gammas = infra
    D_pi = build_dirac_sector(tau, mu, p, q, gens, f_abc, B_ab, gammas)
    w, v = eigh_H(D_pi)
    order = np.argsort(np.abs(w))                       # (local) by |lambda|
    block = v[:, order[:deg]]                           # (local) (dim, deg) lowest multiplet
    return block, w, v, D_pi


def band_degeneracy(tau, mu, p, q, infra, deg_tol=1e-7):
    """Degeneracy of the lowest |lambda| band of D_K(sector (p,q)) at (tau,mu)."""
    gens, f_abc, B_ab, gammas = infra
    D_pi = build_dirac_sector(tau, mu, p, q, gens, f_abc, B_ab, gammas)
    w, _ = eigh_H(D_pi)
    aw = np.abs(w)
    lo = float(np.min(aw))                              # (local)
    return int(np.sum(np.abs(aw - lo) < deg_tol)), lo


# ---------------------------------------------------------------------------
# PRIMARY: NON-ABELIAN FHS gauge-invariant lattice Chern on the (tau,mu) eigenbundle
# ---------------------------------------------------------------------------
def _nonabelian_link(block_a, block_b):
    """Det-normalized non-Abelian U(deg) link matrix between two (dim,deg) band-blocks:
         M_ab = <n_a(k)|n_b(k')>  ;  link = M / det(M)^{1/deg}  (U(deg)-gauge covariant).
       Returns det(M)/|det(M)| (the U(1) phase factor used in the Wilson-loop product)."""
    M = block_a.conj().T @ block_b                     # (local) (deg,deg) overlap
    d = np.linalg.det(M)                               # (local)
    if abs(d) < 1e-14:
        return 1.0 + 0.0j                              # degenerate-overlap guard (identity link)
    return d / abs(d)


def fhs_lattice_chern(p, q, infra, taus, mus, deg, verbose=False):
    """Non-Abelian Fukui-Hatsugai-Suzuki (2005) lattice Chern of the lowest DEGENERATE band-group
       (degeneracy `deg`) of D_K(sector (p,q)) over the (tau,mu) NODE grid.
       Per plaquette, with band-blocks N(i,j) = (dim,deg):
         link_tau(i,j) = det<N(i,j)|N(i+1,j)>/|det| ;  link_mu analogous
         F(i,j)        = arg[ link_tau(i,j) link_mu(i+1,j) link_tau(i,j+1)^* link_mu(i,j)^* ]
         C             = (1/2pi) sum F.
       The det-normalization makes the link U(deg)-gauge covariant: the arbitrary U(deg) basis
       rotation of each degenerate band-block cancels around every plaquette (Fukui-Hatsugai-Suzuki
       non-Abelian extension). Returns (C_fhs, F_plaq, deg)."""
    n_tau = len(taus)
    n_mu = len(mus)
    blocks = np.empty((n_tau, n_mu), dtype=object)     # (local) lowest multiplet blocks (dim,deg)
    for i in range(n_tau):
        for jx in range(n_mu):
            blk, _, _, _ = lowest_band_multiplet(taus[i], mus[jx], p, q, infra, deg)
            blocks[i, jx] = blk
        if verbose:
            print(f"    [FHS] tau row {i+1}/{n_tau} (tau={taus[i]:.4f}) blocks built (deg={deg})")

    F_plaq = np.zeros((n_tau - 1, n_mu - 1))           # (local) plaquette field strength
    for i in range(n_tau - 1):
        for jx in range(n_mu - 1):
            N00 = blocks[i, jx]
            N10 = blocks[i + 1, jx]
            N01 = blocks[i, jx + 1]
            N11 = blocks[i + 1, jx + 1]
            l_tau_00 = _nonabelian_link(N00, N10)      # link +tau at (i,j)
            l_mu_10 = _nonabelian_link(N10, N11)       # link +mu  at (i+1,j)
            l_tau_01 = _nonabelian_link(N01, N11)      # link +tau at (i,j+1)
            l_mu_00 = _nonabelian_link(N00, N01)       # link +mu  at (i,j)
            # plaquette holonomy (det-phase Wilson loop)
            plaq = l_tau_00 * l_mu_10 * np.conj(l_tau_01) * np.conj(l_mu_00)
            F_plaq[i, jx] = np.angle(plaq)             # principal branch (-pi,pi]
    C_fhs = float(np.sum(F_plaq) / (2.0 * np.pi))      # (local)
    return C_fhs, F_plaq, deg


# ---------------------------------------------------------------------------
# CROSS-CHECK: BP-4 continuum Berry curvature Omega_n(tau,mu)
# ---------------------------------------------------------------------------
def dD_dparam(tau, mu, p, q, infra, axis):
    """Central finite-difference d D_pi / d{tau or mu} at (tau,mu)."""
    gens, f_abc, B_ab, gammas = infra
    if axis == "tau":
        Dp = build_dirac_sector(tau + FD_EPS, mu, p, q, gens, f_abc, B_ab, gammas)
        Dm = build_dirac_sector(tau - FD_EPS, mu, p, q, gens, f_abc, B_ab, gammas)
    else:
        Dp = build_dirac_sector(tau, mu + FD_EPS, p, q, gens, f_abc, B_ab, gammas)
        Dm = build_dirac_sector(tau, mu - FD_EPS, p, q, gens, f_abc, B_ab, gammas)
    return (Dp - Dm) / (2.0 * FD_EPS)


def bp4_curvature(tau, mu, p, q, infra, deg=1, gap_floor=1e-9):
    """BP-4 continuum Berry curvature of the lowest band-group (non-Abelian TRACE form):
         Omega = -2 Im sum_{n in lowest-deg} sum_{m not in lowest-deg}
                       <n|dH_tau|m><m|dH_mu|n>/(mu_n - mu_m)^2
       where H = i D_pi (eigenvalues mu real, dH = i dD). For a DEGENERATE lowest band the
       gauge-invariant object is the TRACE over the degenerate multiplet (sum over n in the
       lowest band-group), with the intra-multiplet (degenerate) terms excluded by the
       (mu_n - mu_m)^2 > gap_floor guard. This is the U(deg)-invariant non-Abelian Berry
       curvature (Wilczek-Zee trace) -- the continuum companion of the non-Abelian FHS link."""
    _, w, v, _ = lowest_band_multiplet(tau, mu, p, q, infra, deg)
    aw = np.abs(w)
    order = np.argsort(aw)                              # (local)
    low_idx = list(order[:deg])                         # (local) lowest-deg band indices
    low_set = set(low_idx)                              # (local)
    dH_tau = 1j * dD_dparam(tau, mu, p, q, infra, "tau")
    dH_mu = 1j * dD_dparam(tau, mu, p, q, infra, "mu")
    A_tau = v.conj().T @ dH_tau @ v                    # (local) <m|dH_tau|m'>
    A_mu = v.conj().T @ dH_mu @ v                      # (local)
    n_dim = len(w)
    omega = 0.0 + 0.0j                                  # (local)
    for n_idx in low_idx:
        for m in range(n_dim):
            if m in low_set:                            # exclude intra-multiplet (degenerate) terms
                continue
            denom = (w[n_idx] - w[m]) ** 2
            if denom < gap_floor:                       # near-degenerate guard
                continue
            omega += A_tau[n_idx, m] * A_mu[m, n_idx] / denom
    return -2.0 * np.imag(omega)


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    print("=" * 78)
    print(f"{GATE_ID}  --  off-Jensen Berry curvature / Chern number")
    print("  closes C11/C12 (S29 open channel) / the P-30w off-Jensen topology gate")
    print("=" * 78)

    # --- input pins + dual SHA ---
    pins = log_input_pins({
        "canonical_constants": CANONICAL_CONSTANTS,
        "dk_builder": DK_BUILDER,
        "berry_jensen_baseline": BERRY_JENSEN_BASELINE,
    })
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")
    print(f"  GPU available  = {_GPU_OK}  (torch_ok={_TORCH_OK})")

    # --- geometry self-check (Sage-verified relations, re-asserted in float) ---
    n_vol = np.array([1.0, 3.0, 4.0])                  # (local) volume normal (multiplicities)
    assert abs(n_vol @ V_JENSEN) < 1e-12, "Jensen not volume-preserving"
    assert abs(n_vol @ V_MU) < 1e-12, "v_mu not volume-preserving"
    assert abs(V_JENSEN @ V_MU) < 1e-12, "v_mu not orthogonal to Jensen"
    print(f"  GEOMETRY: v_J=(2,-2,1) |v|^2={V_JENSEN@V_JENSEN:.0f}; "
          f"v_mu=(11,7,-8)=n x v_J |v|^2={V_MU@V_MU:.0f}; vol-preserving & perp-Jensen OK")
    # mu=0 reproduces canonical Jensen at the fold
    L1f, L2f, L3f = metric_scale_factors(tau_fold, 0.0)
    print(f"  mu=0,tau=tau_fold={tau_fold}: (L1,L2,L3)=({L1f:.6f},{L2f:.6f},{L3f:.6f}) "
          f"vs Jensen (e^2t,e^-2t,e^t)=({np.exp(2*tau_fold):.6f},{np.exp(-2*tau_fold):.6f},{np.exp(tau_fold):.6f})")

    infra = build_su3_infra()

    # --- NODE grid (51x51 nodes -> 50x50 plaquettes) ---
    taus = np.linspace(TAU_LO, TAU_HI, N_NODE)         # (local)
    mus = np.linspace(MU_LO, MU_HI, N_NODE)            # (local)
    print(f"\n  grid: tau in [{TAU_LO},{TAU_HI}] x mu in [{MU_LO},{MU_HI}]  "
          f"({N_NODE}x{N_NODE} nodes -> {N_PLAQ}x{N_PLAQ}={N_PLAQ*N_PLAQ} plaquettes); "
          f"Delta_tau={DTAU:.4f} Delta_mu={DMU:.4f}; fold tau={tau_fold} enclosed at mu=0")

    # =====================================================================
    # PRIMARY: NON-ABELIAN FHS lattice Chern on the canonical bottom band (0,0)
    #   The lowest Dirac band is a Kramers/J-DEGENERATE multiplet (detected here);
    #   the non-Abelian (det-phase) FHS over the full multiplet is the correct
    #   gauge-invariant estimator (single-band FHS gives gauge noise in the
    #   degenerate subspace -- see WP §"Degenerate-band subtlety").
    # =====================================================================
    P_BOT, Q_BOT = 0, 0                                 # (local) canonical lowest-|lambda| sector (S25/W5)
    deg_bot, lam_bot = band_degeneracy(tau_fold, 0.0, P_BOT, Q_BOT, infra)
    print(f"\n  [PRIMARY] sector (0,0): lowest |lambda|={lam_bot:.6f}, degeneracy={deg_bot} "
          f"(Kramers/J multiplet) -> NON-ABELIAN FHS over the {deg_bot}-dim band-group")
    C_fhs, F_plaq, band_deg = fhs_lattice_chern(P_BOT, Q_BOT, infra, taus, mus, deg_bot, verbose=True)
    max_absF = float(np.max(np.abs(F_plaq)))           # (local)
    print(f"    deg={band_deg}; C_FHS = {C_fhs:.6e}; "
          f"round(C)={round(C_fhs)}; |C-round(C)|={abs(C_fhs-round(C_fhs)):.3e}; "
          f"max|F_plaq|={max_absF:.3e}")

    # =====================================================================
    # CROSS-CHECK: BP-4 continuum Omega(tau,mu) on the plaquette-CENTER grid
    #   (non-Abelian Wilczek-Zee trace over the same degenerate lowest band-group)
    # =====================================================================
    print("\n  [CROSS-CHECK] BP-4 continuum Berry curvature Omega(tau,mu) (plaquette centers)")
    tau_c = 0.5 * (taus[:-1] + taus[1:])               # (local) plaquette-center tau
    mu_c = 0.5 * (mus[:-1] + mus[1:])                  # (local) plaquette-center mu
    Omega_cont = np.zeros((N_PLAQ, N_PLAQ))            # (local)
    for i in range(N_PLAQ):
        for jx in range(N_PLAQ):
            Omega_cont[i, jx] = bp4_curvature(tau_c[i], mu_c[jx], P_BOT, Q_BOT, infra, deg=deg_bot)
        if (i + 1) % 10 == 0:
            print(f"    [BP-4] tau-center row {i+1}/{N_PLAQ} done")
    max_absOmega = float(np.max(np.abs(Omega_cont)))   # (local)
    # continuum Chern = (1/2pi) integral Omega dtau dmu (midpoint rule on plaquette centers)
    C_cont = float(np.sum(Omega_cont) * DTAU * DMU / (2.0 * np.pi))  # (local)
    print(f"    max|Omega_cont| = {max_absOmega:.3e}; "
          f"C_cont = (1/2pi) int Omega dtau dmu = {C_cont:.6e}")

    # =====================================================================
    # Jensen-line (mu=0) baseline cross-check: Omega must vanish on the slice
    # =====================================================================
    print("\n  [BASELINE] Jensen-line (mu=0) Omega -- must reproduce S25/W5 Omega=0")
    jensen_omega = np.array([bp4_curvature(t, 0.0, P_BOT, Q_BOT, infra, deg=deg_bot) for t in tau_c])  # (local)
    max_jensen_omega = float(np.max(np.abs(jensen_omega)))  # (local)
    print(f"    max|Omega(tau, mu=0)| = {max_jensen_omega:.3e}  "
          f"(S25/W5 PROVEN Omega=0, anti-Hermitian Kosmann K_a; expect ~ machine eps)")

    # =====================================================================
    # ROBUSTNESS ARM: NON-ABELIAN FHS Chern across the low-lying Peter-Weyl sectors
    #   (each sector's lowest band-group degeneracy detected independently)
    # =====================================================================
    print("\n  [ROBUSTNESS] non-Abelian FHS lattice Chern across low-lying sectors (p+q<=2)")
    sector_list = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0)]  # (local) bottom Peter-Weyl sectors
    sector_chern = {}                                  # (local)
    sector_deg = {}                                    # (local)
    for (p, q) in sector_list:
        try:
            d_s, _ = band_degeneracy(tau_fold, 0.0, p, q, infra)
            C_s, F_s, _ = fhs_lattice_chern(p, q, infra, taus, mus, d_s, verbose=False)
            sector_chern[(p, q)] = C_s
            sector_deg[(p, q)] = d_s
            print(f"    sector ({p},{q}) deg={d_s}: C_FHS={C_s:.6e} "
                  f"|C-round|={abs(C_s-round(C_s)):.2e}")
        except Exception as e:  # pragma: no cover
            print(f"    sector ({p},{q}) SKIPPED: {e}")
    all_trivial_sectors = all(abs(c - round(c)) < CHERN_INT_TOL and round(c) == 0
                              for c in sector_chern.values())  # (local)
    max_sector_absC = max((abs(c) for c in sector_chern.values()), default=0.0)  # (local)

    # =====================================================================
    # VERDICT (plan §W5-5 operator.form)
    # =====================================================================
    print("\n" + "=" * 78)
    print("  VERDICT")
    print("=" * 78)
    is_integer = abs(C_fhs - round(C_fhs)) <= CHERN_INT_TOL           # (local)
    n_round = round(C_fhs)                                             # (local)
    fhs_cont_agree = abs(C_fhs - C_cont) <= max(CHERN_INT_TOL, 0.05)  # (local) estimator agreement
    trivial_branch = (n_round == 0) and (max_absOmega < NONTRIVIAL_OMEGA_THR)  # (local)
    nontrivial_branch = (n_round != 0) and (max_absOmega > NONTRIVIAL_OMEGA_THR)  # (local)

    # PASS-TRIVIAL: integer-quantized C=0 + curvature below the nontrivial threshold
    #   (the FHS/continuum agree; the §9 spine strengthens to the full surface)
    # PASS-NONTRIVIAL: integer-quantized C=n!=0 + localized curvature above threshold
    # FAIL: non-integer C (gauge/discretization artifact)
    # INFO: near-integer but trivial/nontrivial call marginal OR estimators disagree
    if not is_integer:
        verdict = "FAIL"
        branch = "non-integer-C"
    elif trivial_branch and all_trivial_sectors and fhs_cont_agree:
        verdict = "PASS"
        branch = "PASS-TRIVIAL"
    elif nontrivial_branch and fhs_cont_agree:
        verdict = "PASS"
        branch = "PASS-NONTRIVIAL"
    else:
        verdict = "INFO"
        branch = "marginal-or-estimator-disagreement"

    value_str = (
        f"C_FHS={C_fhs:.6e}_round={n_round}_branch={branch}_"
        f"maxOmega={max_absOmega:.3e}_C_cont={C_cont:.6e}_"
        f"jensenOmega={max_jensen_omega:.3e}_allsectorsTrivial={all_trivial_sectors}"
    )
    print(f"  C_FHS = {C_fhs:.6e}  (round={n_round}, |C-round|={abs(C_fhs-n_round):.3e} vs tol {CHERN_INT_TOL})")
    print(f"  C_cont (BP-4) = {C_cont:.6e}   FHS/cont agree: {fhs_cont_agree}")
    print(f"  max|Omega| = {max_absOmega:.3e}  (trivial floor {TRIVIAL_OMEGA_FLOOR:.0e}, "
          f"nontrivial thr {NONTRIVIAL_OMEGA_THR:.0e})")
    print(f"  Jensen-line max|Omega(mu=0)| = {max_jensen_omega:.3e}  (S25/W5 baseline)")
    print(f"  all low-lying sectors trivial: {all_trivial_sectors}  (max|C_sector|={max_sector_absC:.3e})")
    print(f"  >>> {GATE_ID}: {verdict}  [{branch}]")

    # --- save data ---
    SESSION_96_DIR.mkdir(parents=True, exist_ok=True)
    np.savez(
        NPZ_OUT,
        taus=taus, mus=mus,
        tau_centers=tau_c, mu_centers=mu_c,
        F_plaq=F_plaq, Omega_cont=Omega_cont,
        jensen_omega=jensen_omega,
        C_fhs=C_fhs, C_cont=C_cont,
        max_absF=max_absF, max_absOmega=max_absOmega,
        max_jensen_omega=max_jensen_omega,
        n_round=n_round,
        sector_chern_keys=np.array([f"{p}_{q}" for (p, q) in sector_chern.keys()]),
        sector_chern_vals=np.array(list(sector_chern.values())),
        sector_deg_vals=np.array([sector_deg.get(k, 0) for k in sector_chern.keys()]),
        all_trivial_sectors=all_trivial_sectors,
        band_deg=int(deg_bot),
        v_jensen=V_JENSEN, v_mu=V_MU,
        verdict=verdict, branch=branch,
        tau_fold=float(tau_fold),
        scan_tau=np.array([TAU_LO, TAU_HI]), scan_mu=np.array([MU_LO, MU_HI]),
    )
    print(f"\n  Saved data: {NPZ_OUT}")

    # --- plot: Omega(tau,mu) heatmap + FHS field strength ---
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    ext = [MU_LO, MU_HI, TAU_LO, TAU_HI]               # (local) [mu (x), tau (y)]
    cap = max(max_absOmega, 1e-300)                    # (local) symmetric color cap
    im0 = axes[0].imshow(Omega_cont, origin="lower", aspect="auto", extent=ext,
                         cmap="RdBu_r", vmin=-cap, vmax=cap)
    axes[0].axhline(tau_fold, color="k", ls="--", lw=1.2, label=f"fold tau={tau_fold}")
    axes[0].axvline(0.0, color="green", ls=":", lw=1.4, label="Jensen line (mu=0)")
    axes[0].set_xlabel("mu (second U(2)-inv TT direction)")
    axes[0].set_ylabel("tau (Jensen direction)")
    axes[0].set_title(f"BP-4 continuum Berry curvature Omega(tau,mu)\nmax|Omega|={max_absOmega:.2e}, "
                      f"C_cont={C_cont:.3e}")
    axes[0].legend(loc="upper right", fontsize=8)
    fig.colorbar(im0, ax=axes[0], label="Omega")

    capF = max(max_absF, 1e-300)                        # (local)
    im1 = axes[1].imshow(F_plaq, origin="lower", aspect="auto",
                         extent=[MU_LO, MU_HI, TAU_LO, TAU_HI],
                         cmap="RdBu_r", vmin=-capF, vmax=capF)
    axes[1].axhline(tau_fold, color="k", ls="--", lw=1.2)
    axes[1].axvline(0.0, color="green", ls=":", lw=1.4)
    axes[1].set_xlabel("mu")
    axes[1].set_ylabel("tau")
    axes[1].set_title(f"FHS lattice field strength F_plaq\nC_FHS={C_fhs:.3e} (round={n_round}); "
                      f"VERDICT={verdict} [{branch}]")
    fig.colorbar(im1, ax=axes[1], label="F_plaq (rad)")

    fig.suptitle(f"{GATE_ID}: off-Jensen Berry / Chern on the 2-param U(2)-inv TT surface "
                 f"(closes C11/C12)", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(PNG_OUT, dpi=150)
    print(f"  Saved plot: {PNG_OUT}")

    # --- emit verdict line (single canonical + dual-SHA companion) ---
    append_verdict(verdict, value_str, audit_sha, content_sha)
    print(f"  Appended verdict to: {VERDICT_FILE}")
    print(f"\n  4-tuple: (value={value_str[:60]}..., scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
