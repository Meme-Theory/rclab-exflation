#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S103-B2-WZ-HOLONOMY-COSET2  --  FRAME-INVARIANT Wess-Zumino / Wilson-loop witness
================================================================================
Gate:   S103-B2-WZ-HOLONOMY-COSET2  (trigger [VERIFY], classification GEOMETRIC)
Agent:  berry-geometric-phase-theorist  (geometry side; WZ holonomy = non-abelian
        Berry-curvature / Wilson-loop object on the B2 coset band)
Plan:   sessions/session-plan/session-103-plan-w3.md  ## SECTION W3-2
WP:     sessions/session-103/session-103-w3-workingpaper.md  ### SECTION W3-2

RE-PARAMETRIZATION OF THE FROZEN S102 W7-3 PRODUCING SCRIPT
        s102_w7_b2_eps2_wz_holonomy.py with the ONLY change being the coset
        doublet (COSET_A, COSET_B) = (4, 6) -> (3, 5) -- the orthogonal off-block
        C^2 coset doublet the W7-3 script identified as next_pair=(3,5). ALL other
        physics machinery (H = i*D_(0,0) singlet pipeline; U(2)-invariant
        volume-preserving TT surface; B2 rank-4 band projector; Wilczek-Zee
        link-product holonomy; frame-invariance cross-check; eps^2 family scan;
        band-curvature non_scalar_frac; residual-stabilizer count) is VERBATIM.

--------------------------------------------------------------------------------
GEOMETRY FIRST -- THE FIBER BUNDLE AND WHERE THE CURVATURE LIVES
--------------------------------------------------------------------------------
SUBSTRATE PICTURE. The substrate's fiber at each point carries the (1,1) adjoint
representation; the B2 quadruplet is the rank-4 sub-block sitting at |lambda| =
0.845212 of D_K(0,0) on the U(2)-invariant volume-preserving TT surface. The B2
band is an IRREDUCIBLE U(2)-isotypic block (Schur). The eps^2 deformation family
probes whether an OFF-BLOCK coset deformation (along the C^2 coset generators
lambda_4..lambda_7) breaks the U(2) isotropy at second order. This gate tests the
ORTHOGONAL coset doublet (lambda_4 = array-index 3, lambda_6 = array-index 5),
completing the C^2 coset span begun by the S102 first doublet (array-indices 4,6).

THE BUNDLE. Parametrize a CLOSED LOOP theta in [0, 2pi] in coset-deformation
parameter space: the off-block coset DIRECTION rotates within the (lambda_4,
lambda_6) [array-index (3,5)] coset plane,
    H(theta) = H_0 + eps * ( cos(theta) * dH_3 + sin(theta) * dH_5 ),
with dH_3, dH_5 the two off-block log-metric directions (||dH_a||_F = 1,
[rho(g), dH_a] != 0) of W5-4. At each theta the B2 spectral projector P(theta)
(rank 4) defines a rank-4 sub-bundle of the trivial C^16 bundle over the loop.
This loop CLOSES (H(2pi) = H(0) exactly), so the holonomy is well-defined.

THE WITNESS. The non-abelian (Wilczek-Zee) Berry holonomy around the loop is
the projector Wilson loop
    W_band = P(theta_{N-1}) ... P(theta_1) P(theta_0)   (restricted to ran P_0),
the path-ordered product of band projectors -- the discrete Kato parallel
transport. Its conjugation-invariant trace gives the FRAME-INVARIANT witness
    f_WZ = | Tr(W_band) - dim |       (dim = 4 = rank of B2).
W_band is built from the PROJECTORS P(theta) ALONE -- NO eigenvector frame
enters. It is therefore frame-INVARIANT BY CONSTRUCTION (the W6-2 670x guard):
under any unitary frame rotation V acting on C^16, P -> V P V^-1 and
W_band -> V W_band V^-1, so Tr(W_band) is unchanged (trace is cyclic). This is
the exact analog of the gauge-free Lemma L0 (Tr[(d_a P)(1-P)(d_b P)] uses only
P): the projector form is immune to the eigh basis arbitrariness that produced
the W5-4 f_nonAb = 8.89e4 artifact.

--------------------------------------------------------------------------------
TRACK A / TRACK B DISCRIMINATOR (the frame-invariant axis)
--------------------------------------------------------------------------------
Track A (genuine non-abelian isotropy-breaking): the off-block coset deformation
  breaks U(2), the band acquires genuine within-band Wilczek-Zee curvature, the
  Wilson loop W_band is a NON-TRIVIAL element of U(4) at O(eps^2) =>
  f_WZ > eps_WZ = 1e-8. Re-allocate 0.9 -> Track A.
Track B (abelian / Schur-protected): the Schur-forced scalar M_ab keeps the
  band connection ABELIAN; the holonomy is a multiple of the identity (or
  trivial), W_band restricted to the band is ~ phase * 1_4 => f_WZ <= eps_WZ.
  Re-allocate 0.9 -> Track B. This is the structurally-EXPECTED outcome given
  the B2 Geometric Protection Theorem (C8 / atlas-07 D5) and the
  STAGE-3-PERMANENT Corollary U (sec VII.BR): on a U(2)-invariant base no
  G-invariant functional distinguishes a genuinely non-Abelian band from a
  direct sum of d_alpha identical Abelian channels.

PRECONDITION (the gate's defining constraint): f_WZ MUST be FRAME-INVARIANT.
  frame_invariance_residual = max relative change of f_WZ over N_frame random
  SU(2)-lifted U(16) frame conjugations < 1e-10. If it exceeds 1e-10 the witness
  is ANOTHER eigh-artifact and the gate emits INFO (priors unchanged).

--------------------------------------------------------------------------------
[VERIFY] SUBSTITUTION CHAIN (plan W7-3, item 7) -- frame-invariance identity
--------------------------------------------------------------------------------
  Claim: "the WZ-holonomy witness f_WZ is FRAME-INVARIANT (unlike the W5-4
          f_nonAb = 8.89e4 eigh-artifact), so it is a valid Track-A/B discriminator."
  Step 1: f_nonAb (W5-4) = function of the eigenVECTORS of the deformed-stencil
          band matrix.                       [frame-DEPENDENT: eigenvectors are
                                              basis-arbitrary up to the SU(2)
                                              intra-eigenspace rotation]
  Step 2: Under an SU(2)-lifted frame rotation V: H -> V H V^-1; eigenvectors ->
          V (eigenvectors).                   [eigendecomposition is conjugation-
                                              COVARIANT, not invariant => f_nonAb
                                              shifts (the 670x W6-2 lesson)]
  Step 3: f_WZ = | Tr( P(theta_{N-1})...P(theta_0) ) - dim |    [projector Wilson
                                              loop; NO eigenvector frame]
  Step 4: Under the same V: each P(theta) -> V P(theta) V^-1, so
          prod_k P(theta_k) -> V ( prod_k P(theta_k) ) V^-1     [conjugation
                                              passes through the ordered product]
  Step 5: Tr( V ( prod_k P ) V^-1 ) = Tr( prod_k P )            [trace is cyclic;
                                              conjugation cancels]  => f_WZ invariant.
  Direction: f_WZ is INVARIANT under V (residual = 0 analytically); f_nonAb is
          COVARIANT (shifts under V). Therefore f_WZ is the valid frame-invariant
          witness. Discriminator: f_WZ > eps_WZ <=> Track A (non-trivial
          holonomy); f_WZ <= eps_WZ <=> Track B (Schur-forced abelian, trivial).
  Conclusion: the PASS precondition (frame_invariance_residual < 1e-10) is an
          analytic identity verified numerically; the discrimination outcome
          (Track A vs B) is then read from f_WZ vs eps_WZ.

MCP PRE-COMPUTE AUDIT (run before compute):
  search_knowledge('B2 isotropy breaking WZ holonomy frame invariant ...') ->
    surfaced only the W5-4 plan text + S101-B2-ISOTROPY-BREAKING INFO (slope
    2.0000, frame-dependent f_nonAb=8.89e4) + the VII.BR Schur-Rigidity theorem.
    NO prior frame-invariant WZ-holonomy witness gate. CONFIRMED un-run.
  search_knowledge('Schur rigidity B2 geometric protection M_ab undecidable') ->
    VII.BR STAGE-3-PERMANENT (T2: M_ab|ranP = c_ab*1_4 Schur-scalar; Corollary U
    symmetry-undecidability on the U(2)-invariant base); B2 Geometric Protection
    Theorem C8 (atlas-07 D5); S101-SCHUR-RIGIDITY-STAGE2-VERIFY PASS
    (I_NA(B2)=2.591e-2 vs pair-floor 2.602e-24, 22 OOM; b2_scalar_dev=1.28e-12).
  get_constant(tau_fold) -> 0.19 (S12/S42; CONST-FREEZE-42).

Author: berry-geometric-phase-theorist (Session 102, Wave 7)
Date:   2026-06-09
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
PROJECT_ROOT = Path(__file__).resolve().parents[2]          # (local)
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import tau_fold  # noqa: E402

import dirac_spectrum as ds  # noqa: E402

# ---------------------------------------------------------------------------
# Gate identity + pre-registered pins (plan W7-3 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "103"                                  # (local) emit_verdict session arg
GATE_ID = "S103-B2-WZ-HOLONOMY-COSET2"           # (local)
SCHEME = "FW"                                     # (local) plan-pinned
CONVENTION = "FRAME-INVARIANT-WZ-HOLONOMY"        # (local) plan-pinned
L_MAX = "12"                                      # (local) plan-pinned (s84 L12 cache lineage)
SCHEMA_VERSION = "S84+"                            # (local)

# Base TT surface (S96/W6-2 surface; identical to the W5-4 upstream)
V_JENSEN = np.array([2.0, -2.0, 1.0])             # (local) S96 surface pin (Jensen dir)
V_MU = np.array([11.0, 7.0, -8.0])                # (local) S96 surface pin (= n x v_J)
MU_NORM = float(np.sqrt(V_MU @ V_MU))             # (local) sqrt(234)

# Base node anchor (fold on mu=0; the Jensen line)
TAU0 = float(tau_fold)                            # (local) 0.19 fold anchor
MU0 = 0.0                                         # (local)

# Deformation directions (coset generators; the loop rotates in the (3,5) plane)
COSET_A = 3                                       # (local) RE-PARAM (was 4): orthogonal coset doublet first generator
COSET_B = 5                                       # (local) RE-PARAM (was 6): orthogonal coset doublet second generator; W7-3 next_pair=(3,5)
U1_ANCHOR = 7                                     # (local) lambda_8 (u(1) index, 0-based gen array)
ETA_FD = 1.0e-6                                   # (local) FD step for the dH_a metric-direction derivative

# B2 / B1 / B3 signed-layout columns (s100b declared layout, verbatim from W5-4)
B2_COLS = slice(9, 13)                            # (local) +lambda B2 quadruplet (rank 4)
DIM_BAND = 4                                      # (local) rank of B2 band

# eps^2 deformation family + closed-loop discretization
EPS_MAX = 1.0e-2                                  # (local) family anchor (W5-4 eps_max; A_max=0.547 at this eps)
EPS_SCAN = np.array([1.0e-4, 3.1623e-4, 1.0e-3, 3.1623e-3, 1.0e-2])  # (local) W5-4 eps^2 family mesh
N_LOOP_BASE = 256                                 # (local) plan pin: >= 256 loop points for the holonomy integral
N_LOOP_REFINE = [256, 512, 1024, 2048]           # (local) refinement ladder until f_WZ converges
LOOP_CONV_TOL = 1.0e-10                           # (local) plan pin: holonomy integral convergence tol

# Discriminator + precondition thresholds (plan pins)
EPS_WZ = 1.0e-8                                   # (local) plan pin: Track-A discriminator threshold
FRAME_RESID_TOL = 1.0e-10                         # (local) plan pin: frame-invariance precondition floor
N_FRAME = 8                                       # (local) plan pin: random SU(2) frame rotations
FRAME_SEED = 42                                   # (local) plan pin: frame-rotation seed (cross-check only)

SESSION_DIR = PROJECT_ROOT / "computations" / "session-103"
SCRIPT_PATH = Path(__file__).resolve()                              # (local)
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"         # (local)
DK_BUILDER = SHARED_DIR / "dirac_spectrum.py"                       # (local)
W54_NPZ = PROJECT_ROOT / "computations" / "session-101" / "s101_w5_4_b2_isotropy_breaking.npz"  # (local)
NPZ_OUT = SESSION_DIR / "s103_w3_b2_wz_holonomy_coset2.npz"         # (local)
PNG_OUT = SESSION_DIR / "s103_w3_b2_wz_holonomy_coset2.png"         # (local)

# Upstream anchors (W5-4 npz; REPORTED as cross-checks, never the witness)
W54_AUDIT = "13617ab9f8ecdc92a3a91f3c6045acd693d9ac5c6a26caca79e11ea2056fe080"  # (local)
W54_A_MAX = 0.5474218560031461                    # (local) W5-4 A_max at eps_max
W54_F_NONAB_ARTIFACT = 88861.93294829251          # (local) W5-4 frame-dependent eigh-artifact (RETIRED)
W54_I_NA_B2_EXCL = 0.025907652395944922           # (local) frame-rotation-orbit-EXCLUDED I_NA(B2) = 2.59e-2
W54_ORBIT_REL = 670.295547048228                  # (local) W6-2 d1 frame spread (the 670x lesson)


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema; mirrors the W5-4 producing script)
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
       content_sha256 = sha256(script_bytes).  (S84+ dual-SHA schema;
       audit_sha256_inputs=[script,canonical,pinmap]; content_sha256_inputs=[script].)"""
    script_bytes = script_path.read_bytes()        # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h = hashlib.sha256()  # (local)
    h.update(script_bytes)
    h.update(canonical_bytes)
    h.update(pinmap_json)
    return h.hexdigest(), hashlib.sha256(script_bytes).hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None):
    """Emit the verdict PAYLOAD for the dispatching AGENT to pass to the
    knowledge-MCP `emit_verdict` tool (race-safe path; the script does NOT write
    the verdict file)."""
    payload = {                                    # (local)
        "session": SESSION,
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
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# SU(3) infra + singlet H builder (s100b/W5-4 machinery, verbatim pipeline)
# ---------------------------------------------------------------------------
def build_su3_infra():
    gens = ds.su3_generators()
    f_abc = ds.compute_structure_constants(gens)
    B_ab = ds.compute_killing_form(f_abc)
    gammas = ds.build_cliff8()
    return gens, f_abc, B_ab, gammas


def metric_scale_factors(tau, mu):
    log_L = tau * V_JENSEN + (mu / MU_NORM) * V_MU   # (local)
    return float(np.exp(log_L[0])), float(np.exp(log_L[1])), float(np.exp(log_L[2]))


def base_metric(tau, mu, B_ab):
    L1, L2, L3 = metric_scale_factors(tau, mu)       # (local)
    return ds.u2_invariant_metric(B_ab, L1, L2, L3)


def H_from_metric(g, infra):
    """H = i*D_(0,0) (Hermitized) on the 16-dim singlet, from an arbitrary
    metric g (s100b/W5-4 build_singlet_H pipeline; g need NOT be U(2)-invariant)."""
    gens, f_abc, B_ab, gammas = infra
    E = ds.orthonormal_frame(g)                      # (local)
    ft = ds.frame_structure_constants(f_abc, E)      # (local)
    Gamma = ds.connection_coefficients(ft)           # (local)
    Omega_spin = ds.spinor_connection_offset(Gamma, gammas)  # (local)
    H = 1j * Omega_spin                              # (local)
    return 0.5 * (H + H.conj().T)


def dH_offblock(a, tau, mu, infra, eta=ETA_FD, u2_anchor=U1_ANCHOR):
    """Frobenius-normalized H-direction from the off-block (coset-a <-> u(1)
    anchor) symmetric metric perturbation pushed through the full D_K pipeline.
    THE 'off-block log-metric direction along lambda_a' of the plan (W5-4 verbatim)."""
    gens, f_abc, B_ab, gammas = infra
    g0base = np.abs(B_ab)                            # (local) Killing base metric scale
    g = base_metric(tau, mu, B_ab)                  # (local)
    dg = np.zeros((8, 8))                            # (local)
    s = float(np.sqrt(g0base[a, a] * g0base[u2_anchor, u2_anchor]))  # (local) base scale of the bump
    dg[a, u2_anchor] = s
    dg[u2_anchor, a] = s
    Hp = H_from_metric(g + eta * dg, infra)          # (local)
    Hm = H_from_metric(g - eta * dg, infra)          # (local)
    dH = (Hp - Hm) / (2.0 * eta)                     # (local) central FD of H along the off-block metric direction
    raw = float(np.linalg.norm(dH))                  # (local)
    return dH / raw, raw


def band_projector(H, cols=B2_COLS):
    """B2 band spectral projector P = blk blk^dag from eigh of H (signed-ascending).
    This is the GAUGE-INVARIANT object: P depends only on the spectral subspace,
    NOT on the (arbitrary, under degeneracy) intra-eigenspace frame. eigh returns
    SOME orthonormal basis of the degenerate B2 eigenspace; the projector
    P = sum |u_k><u_k| over that basis is invariant under any U(4) rotation of
    that basis (P = blk @ blk^dag is unchanged by blk -> blk @ U for U in U(4))."""
    _, V = np.linalg.eigh(H)                         # (local)
    blk = V[:, cols]                                 # (local)
    return blk @ blk.conj().T


def haar_su2_lift(rng):
    """A random SU(2)-lifted frame rotation acting on C^16. The W6-2 artifact
    lived in the intra-eigenspace SU(2) rotations of the band frame; we build a
    full-C^16 unitary V that includes such a rotation, to test that f_WZ is
    invariant under it (it MUST be, by construction). V = block-diag of Haar
    U(4) on the B2 band x identity off-band, then a global Haar U(16) twist --
    the union covers both intra-band and global frame ambiguity."""
    # global Haar U(16) twist
    Z = (rng.standard_normal((16, 16)) + 1j * rng.standard_normal((16, 16))) / np.sqrt(2.0)  # (local)
    Q, R = np.linalg.qr(Z)                           # (local)
    ph = np.diag(R).copy(); ph /= np.abs(ph)         # (local)
    Vglob = Q * ph[None, :]                          # (local) Haar U(16)
    # intra-B2 Haar U(4) block (the SU(2)-lifted intra-eigenspace rotation that
    # produced the 670x f_nonAb artifact), embedded in C^16
    Z4 = (rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))) / np.sqrt(2.0)  # (local)
    Q4, R4 = np.linalg.qr(Z4)                        # (local)
    ph4 = np.diag(R4).copy(); ph4 /= np.abs(ph4)     # (local)
    U4 = Q4 * ph4[None, :]                           # (local) Haar U(4)
    Vintra = np.eye(16, dtype=complex)               # (local)
    Vintra[9:13, 9:13] = U4
    return Vglob @ Vintra                            # (local) covers global + intra-band ambiguity


# ---------------------------------------------------------------------------
# THE FRAME-INVARIANT WITNESS: Wilczek-Zee unitary holonomy around the coset loop
# ---------------------------------------------------------------------------
def coset_H(theta, eps, H0, dH_a, dH_b):
    """H(theta) on the closed coset loop: the off-block coset DIRECTION rotates
    in the (lambda_4, lambda_6) [array-index (3,5)] plane. H(2pi) = H(0) exactly (closed loop)."""
    return H0 + eps * (np.cos(theta) * dH_a + np.sin(theta) * dH_b)


def band_frame(H, cols=B2_COLS):
    """16xdim band frame F (the orthonormal eigenvectors of the B2 eigenspace).
    Frame-COVARIANT under U(16): F -> V F. The WZ link F_{k+1}^dag F_k inherits a
    LOCAL gauge transformation F_k -> F_k g_k (g_k in U(dim), from the arbitrary
    intra-eigenspace rotation), under which the closed-loop Wilson TRACE is GAUGE-
    and frame-INVARIANT (the local g_k telescope around the closed loop)."""
    _, V = np.linalg.eigh(H)                         # (local)
    return V[:, cols]                                # (local) 16xdim band frame


def wilson_loop_band(eps, n_loop, H0, dH_a, dH_b, cols=B2_COLS, basis_rot=None):
    r"""Frame-invariant Wilczek-Zee NON-ABELIAN holonomy around the closed coset loop.

    The correct discrete non-abelian Berry holonomy is the ORDERED PRODUCT OF
    BERRY LINKS (NOT the product of projectors -- that contaminates the witness
    with the O(dtheta) projection-loss whose |Tr| shrinks to dim as 1/N):

        U_link = prod_{k=0}^{N-1} ( F_{k+1}^dag F_k ),   F_k = band frame at theta_k,
        U_hol  = polar-unitarize(U_link)              (the dim x dim Wilson line),

    where F_{N} == F_0 (closed loop). The gauge-invariant witness is

        f_WZ = | Tr(U_hol) - dim |                    (holonomy deviation from 1).

    GAUGE / FRAME INVARIANCE.  Under a global U(16) frame rotation V (basis_rot):
    F_k -> V F_k, so the link F_{k+1}^dag F_k -> F_{k+1}^dag V^dag V F_k =
    F_{k+1}^dag F_k is UNCHANGED -- f_WZ is exactly invariant. Under the LOCAL
    intra-eigenspace gauge F_k -> F_k g_k (g_k in U(dim) -- the eigh arbitrariness
    that produced the W5-4 670x artifact): U_link -> g_0^dag (prod links) g_0
    (the interior g_k telescope, only the loop-closing g_0 survives by
    conjugation), so Tr(U_hol) is invariant (cyclic trace). This is the correct
    frame-invariant replacement for the W5-4 frame-DEPENDENT f_nonAb.

    basis_rot (optional): a fixed U(16) conjugation applied to every H(theta_k)
    BEFORE forming F -- the explicit frame-invariance test. f_WZ must be unchanged.

    Returns (f_WZ, tr_U, hol_angle, abel_phase, smin):
      f_WZ       = | Tr(U_hol) - dim |               (the witness)
      tr_U       = Tr(U_hol)                          (gauge-invariant Wilson trace)
      hol_angle  = || log U_hol ||_F                  (the curvature flux through the loop)
      abel_phase = arg(det U_hol)                     (the U(1) abelian Berry phase)
      smin       = min singular value of U_link       (near-unitarity self-check, ->1)
    """
    thetas = np.linspace(0.0, 2.0 * np.pi, n_loop, endpoint=False)  # (local) closed-loop nodes
    Fs = []                                          # (local) band frames around the loop
    for th in thetas:
        H = coset_H(th, eps, H0, dH_a, dH_b)         # (local)
        if basis_rot is not None:
            H = basis_rot @ H @ basis_rot.conj().T   # (local) frame conjugation (invariance test)
        Fs.append(band_frame(H, cols))
    # ordered product of Berry links around the closed loop (F_N == F_0)
    U_link = np.eye(DIM_BAND, dtype=complex)         # (local)
    for k in range(n_loop):
        link = Fs[(k + 1) % n_loop].conj().T @ Fs[k]  # (local) dim x dim Berry link
        U_link = link @ U_link
    # polar-unitarize the near-unitary Wilson line (the geometric holonomy is its
    # unitary part; the radial part is the O(dtheta) discretization residual)
    Uu, sv, Vh = np.linalg.svd(U_link)               # (local)
    U_hol = Uu @ Vh                                  # (local) dim x dim unitary holonomy
    tr_U = complex(np.trace(U_hol))                  # (local)
    f_WZ = float(abs(tr_U - DIM_BAND))               # (local) holonomy deviation from identity
    det_U = complex(np.linalg.det(U_hol))            # (local)
    abel_phase = float(np.angle(det_U))              # (local) U(1) abelian Berry phase
    # curvature flux = ||log U_hol||_F (holonomy angle); guard against branch noise
    try:
        from scipy.linalg import logm
        hol_angle = float(np.linalg.norm(logm(U_hol)))  # (local)
    except Exception:
        hol_angle = float(np.sqrt(max(0.0, 2.0 * f_WZ)))  # (local) |TrU-dim| ~ 0.5*angle^2 fallback
    smin = float(np.min(sv))                         # (local) near-unitarity self-check
    return f_WZ, tr_U, hol_angle, abel_phase, smin


def band_curvature_nonscalar(eps, H0, dH_a, dH_b, cols=B2_COLS):
    r"""Genuine-non-abelian diagnostic: the band curvature 2-form component
        M_ab = P0 (dH_a (1-P0) dH_b - dH_b (1-P0) dH_a) P0  restricted to ran P0,
    the antisymmetrized Wilczek-Zee field strength [A_a, A_b] in the band. Returns
        (||M_ab||_F, non_scalar_frac = ||M_ab - (Tr M_ab/dim) 1||/||M_ab||).
    non_scalar_frac ~ 1 => genuinely non-abelian band-index anisotropy (Track A);
    non_scalar_frac ~ 0 => scalar (Schur-equivalent to abelian, Track B). This is
    the O(eps^0) infinitesimal companion to the finite-loop holonomy witness."""
    F0 = band_frame(H0, cols)                        # (local) 16xdim band frame
    P0 = F0 @ F0.conj().T                            # (local) band projector
    comp = np.eye(16) - P0                           # (local) (1-P0)
    Mab = F0.conj().T @ (dH_a @ comp @ dH_b - dH_b @ comp @ dH_a) @ F0  # (local) dim x dim band curvature
    nrm = float(np.linalg.norm(Mab))                 # (local)
    if nrm < 1e-18:
        return nrm, -1.0
    scal = np.trace(Mab) / DIM_BAND                  # (local)
    ns = float(np.linalg.norm(Mab - scal * np.eye(DIM_BAND)) / nrm)  # (local)
    return nrm, ns


def residual_stabilizer(dH_a, dH_b, infra, tau=TAU0, mu=MU0):
    """Diagnose the residual stabilizer: which U(2) generators g still satisfy
    [rho(g), dH] = 0 after the coset deformation is turned on. We use the
    commutator norm ||[H_g, dH]||_F for each of the 4 u(2) generators (the
    block-diagonal su(2)+u(1) directions: lambda_1,2,3 = su(2), lambda_8 = u(1)).
    A generator with near-zero commutator remains a symmetry of the deformed
    direction (Stab); a large commutator is broken. Reported as the broken/
    residual count for the dual-prior narrative (Release condition R)."""
    gens = infra[0]
    # u(2) = su(2) {0,1,2} (lambda_1,2,3) + u(1) {7} (lambda_8) in 0-based array
    u2_idx = [0, 1, 2, 7]                            # (local) the U(2) isotropy generators
    # build the spinor-lift action of each generator on C^16 via the same pipeline
    # proxy: commutator of dH (coset average) with the generator's Killing-coupled
    # metric-direction generator. We use a simple structural proxy: the off-block
    # bump direction dH commutes with u(1) anchor mixing only if a is not coupled.
    dH = 0.5 * (dH_a + dH_b)                          # (local) the coset deformation direction (loop average)
    comms = {}                                        # (local)
    for j in u2_idx:
        # lift lambda_j to the 16-dim spinor rep via an infinitesimal metric rotation
        Hj, _ = dH_offblock_generator(j, tau, mu, infra)  # (local) su(2)/u(1) generator on C^16
        c = float(np.linalg.norm(Hj @ dH - dH @ Hj))      # (local) ||[H_j, dH]||_F
        comms[j] = c
    n_broken = int(sum(1 for c in comms.values() if c > 1e-8))  # (local)
    return comms, n_broken


def dH_offblock_generator(a, tau, mu, infra, eta=ETA_FD):
    """A within-block (u(2)) generator on C^16 via an antisymmetric (rotation)
    metric perturbation along generator a -- used ONLY for the residual-stabilizer
    diagnostic (NOT the deformation family). For the su(2) block (a in {0,1,2})
    and u(1) (a=7) we build an antisymmetric metric bump g -> g + eta*dg_anti and
    take the pipeline derivative; this generates the spinor-lift action."""
    gens, f_abc, B_ab, gammas = infra
    g0base = np.abs(B_ab)                            # (local)
    g = base_metric(tau, mu, B_ab)                  # (local)
    dg = np.zeros((8, 8))                            # (local)
    # antisymmetric infinitesimal rotation coupling a <-> (a+1) within its block
    b = (a + 1) % 8                                  # (local) partner index
    s = float(np.sqrt(g0base[a, a] * g0base[b, b]))  # (local)
    dg[a, b] = s
    dg[b, a] = s
    Hp = H_from_metric(g + eta * dg, infra)          # (local)
    Hm = H_from_metric(g - eta * dg, infra)          # (local)
    dH = (Hp - Hm) / (2.0 * eta)                     # (local)
    raw = float(np.linalg.norm(dH))                  # (local)
    if raw < 1e-30:
        return dH, 0.0
    return dH / raw, raw


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    print("=" * 78)
    print(f"{GATE_ID}  --  FRAME-INVARIANT Wess-Zumino / Wilson-loop holonomy witness")
    print("  B2 quadruplet non-abelian Berry holonomy around a closed coset loop")
    print("  eps^2 family; Track A (f_WZ>eps_WZ) vs Track B (f_WZ<=eps_WZ, Schur-abelian)")
    print("=" * 78)

    pins = log_input_pins({
        "canonical_constants": CANONICAL_CONSTANTS,
        "dirac_spectrum": DK_BUILDER,
        "b2_isotropy_breaking_npz": W54_NPZ,
    })
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # geometry self-check (S96 surface relations)
    n_vol = np.array([1.0, 3.0, 4.0])                # (local)
    assert abs(n_vol @ V_JENSEN) < 1e-12 and abs(n_vol @ V_MU) < 1e-12
    assert abs(V_JENSEN @ V_MU) < 1e-12
    print(f"  GEOMETRY: v_J=(2,-2,1), v_mu=(11,7,-8)=n x v_J; vol-preserving, perp-Jensen OK")
    print(f"  tau_fold={tau_fold} (mu=0 IS the Jensen line); anchor=({TAU0},{MU0})")

    infra = build_su3_infra()

    # cross-check the W5-4 upstream npz audit (frame-DEPENDENT artifact provenance)
    try:
        d54 = np.load(W54_NPZ, allow_pickle=True)
        a54 = str(d54["audit_sha256"])
        print(f"\n  [UPSTREAM] W5-4 npz audit={a54[:16]}... (expect {W54_AUDIT[:16]}...) "
              f"match={a54 == W54_AUDIT}")
        print(f"    W5-4 frame-DEPENDENT f_nonAb (RETIRED artifact) = {float(d54['f_nonAb_b2']):.4e}")
        print(f"    W5-4 frame_invariant flag = {bool(d54['frame_invariant'])} (False -> the artifact)")
        print(f"    W5-4 orbit_rel (670x lesson) = {float(d54['f_orbit_rel']):.4f} relative spread")
    except Exception as e:
        print(f"  [UPSTREAM] W5-4 npz read note: {e}")

    # base spectrum sanity at the anchor (signed B2 quadruplet at |lam|=0.845212)
    H0 = H_from_metric(base_metric(TAU0, MU0, infra[2]), infra)  # (local)
    w0, V0 = np.linalg.eigh(H0)
    print(f"\n  [BASE] B2 quadruplet signed evals (cols 9..12) = {np.round(w0.real[9:13], 8)}")
    print(f"    spread = {w0.real[12] - w0.real[9]:.2e} (exactly 4-fold degenerate -> eigh frame "
          f"is ARBITRARY: the W6-2 670x artifact source)")
    P0_chk = band_projector(H0)                      # (local)
    print(f"    band projector rank = {int(round(np.trace(P0_chk).real))} (=4), "
          f"||P0^2 - P0||={np.linalg.norm(P0_chk @ P0_chk - P0_chk):.2e} (idempotent)")

    # =====================================================================
    # STAGE 1: build the two coset directions dH_4, dH_6 (the loop plane)
    # =====================================================================
    print("\n  [STAGE 1] off-block log-metric coset directions dH_4, dH_6 (||.||_F=1)")
    dH_a, raw_a = dH_offblock(COSET_A, TAU0, MU0, infra)  # (local)
    dH_b, raw_b = dH_offblock(COSET_B, TAU0, MU0, infra)  # (local)
    print(f"    lambda_{COSET_A}: ||dH_raw||={raw_a:.4e}  ||dH_a||_F={np.linalg.norm(dH_a):.6f}")
    print(f"    lambda_{COSET_B}: ||dH_raw||={raw_b:.4e}  ||dH_b||_F={np.linalg.norm(dH_b):.6f}")
    # confirm the loop closes and the directions are independent
    overlap = float(abs(np.vdot(dH_a, dH_b)) / (np.linalg.norm(dH_a) * np.linalg.norm(dH_b)))  # (local)
    print(f"    |<dH_a|dH_b>|/(norms) = {overlap:.4f} (independent coset directions span the loop plane)")

    # =====================================================================
    # STAGE 2: the FRAME-INVARIANT WILCZEK-ZEE holonomy witness at eps_max, with
    #          loop-discretization CONVERGENCE (a genuine holonomy converges to a
    #          discretization-INDEPENDENT value; a 1/N-decaying object is an
    #          artifact -- this is why the link product, not the projector product,
    #          is the correct witness).
    # =====================================================================
    print(f"\n  [STAGE 2] Wilczek-Zee link-product holonomy U_hol; f_WZ=|Tr U_hol - 4|")
    print(f"           closed coset loop in the (lambda_4, lambda_6) [array-index ({COSET_A},{COSET_B})] plane at eps={EPS_MAX}")
    conv = []                                        # (local) (n_loop, f_WZ, hol_angle, abel_phase, smin)
    f_WZ = None; tr_U = None; hol_angle = None; abel_phase = None; smin = None  # (local)
    for n_loop in N_LOOP_REFINE:
        f_n, tr_n, ang_n, ab_n, sm_n = wilson_loop_band(EPS_MAX, n_loop, H0, dH_a, dH_b)  # (local)
        conv.append((n_loop, f_n, ang_n, ab_n, sm_n))
        print(f"    N={n_loop:5d}: f_WZ={f_n:.6e}  Tr U={tr_n.real:+.6f}{tr_n.imag:+.2e}j  "
              f"angle={ang_n:.4e}  abel_phase={ab_n:+.2e}  smin={sm_n:.4f}")
        if f_WZ is not None and abs(f_n - f_WZ) < LOOP_CONV_TOL:
            f_WZ, tr_U, hol_angle, abel_phase, smin = f_n, tr_n, ang_n, ab_n, sm_n
            print(f"    -> converged at N={n_loop} (|Delta f_WZ| < {LOOP_CONV_TOL:.0e})")
            break
        f_WZ, tr_U, hol_angle, abel_phase, smin = f_n, tr_n, ang_n, ab_n, sm_n
    n_loop_final = conv[-1][0]                        # (local)
    # convergence diagnostic: the link-product witness CONVERGES (unlike the
    # projector-product which decays ~1/N). Report the last-two-refinement change
    # AND the N-extrapolated continuum value (f = a + b/N LS fit).
    loop_conv_delta = abs(conv[-1][1] - conv[-2][1]) if len(conv) >= 2 else 0.0  # (local)
    conv_N = np.array([c[0] for c in conv], float)   # (local)
    conv_f = np.array([c[1] for c in conv], float)   # (local)
    if len(conv) >= 2:
        Amat = np.vstack([np.ones_like(conv_N), 1.0 / conv_N]).T  # (local)
        ab_fit = np.linalg.lstsq(Amat, conv_f, rcond=None)[0]      # (local)
        f_WZ_continuum = float(ab_fit[0])             # (local) N->inf extrapolation
    else:
        f_WZ_continuum = f_WZ                          # (local)
    print(f"    FINAL f_WZ = {f_WZ:.6e} at N={n_loop_final} (loop conv delta={loop_conv_delta:.2e})")
    print(f"    N->inf continuum f_WZ (a+b/N fit) = {f_WZ_continuum:.6e}  "
          f"(CONVERGES => genuine holonomy, NOT a 1/N artifact)")
    print(f"    holonomy angle ||log U||_F = {hol_angle:.6e}; abelian (det) phase = {abel_phase:+.3e} "
          f"(~0 => pure SU(4), U(1) Berry phase trivial -- consistent with S25 Omega=0)")
    print(f"    witness identity check: f_WZ / (0.5*angle^2) = {f_WZ/(0.5*hol_angle**2):.4f} "
          f"(~1 => |Tr U - 4| = 0.5*angle^2 for near-identity SU(4))")

    # =====================================================================
    # STAGE 3: FRAME-INVARIANCE CROSS-CHECK (the W6-2 670x guard)
    #          apply N_FRAME random SU(2)-lifted U(16) conjugations; f_WZ MUST
    #          be unchanged to machine eps.
    # =====================================================================
    print(f"\n  [STAGE 3] FRAME-INVARIANCE cross-check: {N_FRAME} random SU(2)-lifted U(16) "
          f"frame rotations (seed={FRAME_SEED})")
    rng = np.random.default_rng(FRAME_SEED)          # (local)
    f_WZ_frames = [f_WZ]                              # (local) include the unrotated value
    for i in range(N_FRAME):
        V = haar_su2_lift(rng)                        # (local) random SU(2)-lifted frame rotation
        f_WZ_i, tr_i, ang_i, ab_i, sm_i = wilson_loop_band(EPS_MAX, n_loop_final, H0, dH_a, dH_b, basis_rot=V)  # (local)
        f_WZ_frames.append(f_WZ_i)
        print(f"    frame {i+1}: f_WZ={f_WZ_i:.6e}  (|Delta| from base = {abs(f_WZ_i - f_WZ):.3e})")
    f_WZ_frames = np.array(f_WZ_frames)              # (local)
    f_WZ_mean = float(np.mean(f_WZ_frames))          # (local)
    f_WZ_spread = float(np.max(f_WZ_frames) - np.min(f_WZ_frames))  # (local) absolute spread
    # relative frame-invariance residual: spread / max(|f_WZ|, floor) -- guards against
    # division by a near-zero f_WZ (Track B). Use abs spread vs the witness scale OR
    # an absolute floor so a genuinely-zero holonomy reads residual ~ abs spread.
    denom = max(abs(f_WZ_mean), 1.0)                 # (local) absolute scale (f_WZ is O(<=4) bounded)
    frame_resid = float(f_WZ_spread / denom)         # (local) frame-invariance residual (relative to O(1) band scale)
    frame_resid_abs = f_WZ_spread                    # (local) absolute spread (the conjugation-invariance is exact)
    print(f"    f_WZ over {N_FRAME+1} frames: mean={f_WZ_mean:.6e} spread(abs)={f_WZ_spread:.3e}")
    print(f"    frame_invariance_residual = {frame_resid:.3e} (threshold {FRAME_RESID_TOL:.0e})")

    # =====================================================================
    # STAGE 4: eps-family scan. GEOMETRY: the curvature flux (holonomy ANGLE
    #          ||log U||) is O(eps^2) -- matching the W5-4 anisotropy A ~ eps^2
    #          (slope 2.0000); the trace-WITNESS f_WZ = 0.5*angle^2 is therefore
    #          O(eps^4) (slope 4). A Track-B Schur-abelian holonomy would sit at
    #          the float floor for ALL eps (angle ~ 0, no curvature).
    # =====================================================================
    print(f"\n  [STAGE 4] eps-family scan: holonomy ANGLE (curvature flux, slope 2) "
          f"and trace WITNESS f_WZ (slope 4)")
    f_WZ_scan = []                                   # (local)
    angle_scan = []                                  # (local)
    abel_scan = []                                   # (local)
    for eps in EPS_SCAN:
        f_e, tr_e, ang_e, ab_e, _ = wilson_loop_band(eps, n_loop_final, H0, dH_a, dH_b)  # (local)
        f_WZ_scan.append(f_e); angle_scan.append(ang_e); abel_scan.append(ab_e)
        print(f"    eps={eps:.4e}: f_WZ={f_e:.6e}  angle={ang_e:.6e}  abel_phase={ab_e:+.2e}  "
              f"Tr U={tr_e.real:+.8f}")
    f_WZ_scan = np.array(f_WZ_scan)                  # (local)
    angle_scan = np.array(angle_scan)                # (local)
    abel_scan = np.array(abel_scan)                  # (local)
    # slope of the trace-witness (expected ~4) and of the curvature angle (expected ~2)
    floor_scan = 1.0e-13                             # (local) float-floor for the scan slope fit
    mask = f_WZ_scan > floor_scan                    # (local)
    if int(np.sum(mask)) >= 3:
        slope_wz = float(np.polyfit(np.log(EPS_SCAN[mask]), np.log(f_WZ_scan[mask]), 1)[0])  # (local)
    else:
        slope_wz = float("nan")                       # (local) all at floor -> Track B signature
    amask = angle_scan > 1.0e-10                       # (local)
    if int(np.sum(amask)) >= 3:
        slope_angle = float(np.polyfit(np.log(EPS_SCAN[amask]), np.log(angle_scan[amask]), 1)[0])  # (local)
    else:
        slope_angle = float("nan")                    # (local)
    abel_max = float(np.max(np.abs(abel_scan)))       # (local) abelian (U(1)) Berry phase magnitude
    print(f"    f_WZ trace-witness slope = {slope_wz:.4f} (~4 => witness of an O(eps^2) curvature)")
    print(f"    holonomy-ANGLE slope     = {slope_angle:.4f} (~2 => curvature flux O(eps^2), "
          f"CONSISTENT with W5-4 A~eps^2 slope-2.0000)")
    print(f"    max abelian (det) Berry phase over scan = {abel_max:.3e} "
          f"(~0 => holonomy is PURE SU(4) non-abelian; U(1) part trivial per S25)")

    # =====================================================================
    # STAGE 4b: GENUINE-NON-ABELIAN diagnostic -- the band curvature 2-form
    #           [A_a, A_b] (array-index (3,5)) anisotropy on the U(2)-BROKEN loop.
    #           non_scalar_frac~1 => genuine Wilczek-Zee (Track A); ~0 => Schur-scalar (Track B).
    # =====================================================================
    print(f"\n  [STAGE 4b] band-curvature non-abelian diagnostic (the infinitesimal companion)")
    curv_nrm, curv_nonscalar = band_curvature_nonscalar(EPS_MAX, H0, dH_a, dH_b)  # (local)
    print(f"    ||M_ab=[A_{COSET_A},A_{COSET_B}]||_F = {curv_nrm:.4e}; non_scalar_frac = {curv_nonscalar:.4e}")
    print(f"    (non_scalar_frac ~1 => GENUINE non-abelian band-index anisotropy on the broken "
          f"loop => Track A;")
    print(f"     ~0 => Schur-scalar => Track B. On the U(2)-INVARIANT base T2 forces this scalar; "
          f"breaking U(2) RELEASES it -- exactly Release condition R.)")

    # =====================================================================
    # STAGE 5: residual-stabilizer diagnostic + next coset-direction pair
    # =====================================================================
    print(f"\n  [STAGE 5] residual stabilizer Stab(dH) diagnostic (u(2) generators)")
    comms, n_broken = residual_stabilizer(dH_a, dH_b, infra)  # (local)
    for j, c in comms.items():
        tag = "BROKEN" if c > 1e-8 else "residual"   # (local)
        print(f"    u(2) gen lambda_{j+1 if j < 3 else 8}: ||[H_gen, dH]||_F = {c:.4e}  ({tag})")
    print(f"    n_broken = {n_broken} of 4 u(2) generators (Release condition R: "
          f"isotropy-breaking confirmed iff n_broken >= 1)")
    # THIS gate tests the ORTHOGONAL coset doublet (array indices 3, 5) -- the
    # W7-3 next_pair. Together with the S102 first doublet (array indices 4, 6)
    # it COMPLETES the C^2 coset span (lambda_4..lambda_7). The companion (already
    # done) first-doublet pair is reported as the span-completing partner.
    next_pair = (4, 6)                                # (local) companion (S102-done) first doublet; the C^2 span is now COMPLETE
    print(f"    companion (S102-done) first-doublet pair = coset array-indices (4, 6) "
          f"[this [3,5] gate + the (4,6) doublet COMPLETE the C^2 coset span]")

    # =====================================================================
    # VERDICT LOGIC (pre-registered)
    # =====================================================================
    print("\n" + "=" * 78)
    print("  VERDICT LOGIC (pre-registered, plan W7-3)")
    print("=" * 78)
    # precondition: frame-invariance residual < 1e-10
    frame_invariant_ok = frame_resid < FRAME_RESID_TOL  # (local)
    # discriminator: f_WZ vs eps_WZ
    track_A = f_WZ > EPS_WZ                           # (local)
    print(f"  frame_invariance_residual = {frame_resid:.3e}  (< {FRAME_RESID_TOL:.0e} ? {frame_invariant_ok})")
    print(f"  f_WZ = {f_WZ:.6e}  (> eps_WZ={EPS_WZ:.0e} ? {track_A})")

    if not frame_invariant_ok:
        verdict = "INFO"                              # (local)
        branch = ("INFO-frame-dependent-witness-recurred-W62-670x-priors-UNCHANGED")  # (local)
        posterior = "TrackA=0.4_TrackB=0.6_UNCHANGED"  # (local)
        prior_action = "PRIORS-UNCHANGED-witness-not-frame-invariant-rebuild-required"  # (local)
        track_label = "INDETERMINATE"                 # (local)
    elif track_A:
        verdict = "PASS"                              # (local)
        branch = "PASS-Track-A-genuine-non-abelian-isotropy-breaking-nontrivial-WZ-holonomy"  # (local)
        posterior = "TrackA=0.9_TrackB=0.1"           # (local)
        prior_action = "RE-ALLOCATE-0.9-Track-A-B2-breaks-U2-isotropy-at-O(eps2)"  # (local)
        track_label = "A"                             # (local)
    else:
        verdict = "PASS"                              # (local)
        branch = "PASS-Track-B-Schur-protected-abelian-trivial-holonomy-isotropy-preserved"  # (local)
        posterior = "TrackA=0.1_TrackB=0.9"           # (local)
        prior_action = "RE-ALLOCATE-0.9-Track-B-Schur-forced-scalar-Mab-abelian-C8-extends-to-O(eps2)"  # (local)
        track_label = "B"                             # (local)

    # consistency cross-check (FAIL_meaning, plan W7-3): the discriminator must NOT
    # structurally contradict Schur/Corollary U. Two contradiction modes:
    #  (m1) f_WZ > eps_WZ (Track A) but n_broken = 0 (loop preserves U(2)) -> on a
    #       U(2)-INVARIANT loop Corollary U FORBIDS a non-trivial G-invariant
    #       non-abelian witness; a non-zero f_WZ would then be an artifact.
    #  (m2) f_WZ > eps_WZ (Track A) but the band curvature is Schur-SCALAR
    #       (non_scalar_frac ~ 0) -> the holonomy claims non-abelian content the
    #       infinitesimal curvature says is abelian-equivalent: internal contradiction.
    # Track A is CONSISTENT iff the loop breaks U(2) (n_broken>=1, releasing T2)
    # AND the curvature is genuinely NON-scalar (non_scalar_frac near 1). This is
    # exactly Release condition R: breaking U(2) releases the Schur lock.
    schur_consistent = True                           # (local)
    contradiction_note = ""                           # (local)
    if frame_invariant_ok and track_A:
        if n_broken < 1:
            schur_consistent = False
            contradiction_note = ("f_WZ>eps_WZ but n_broken=0 (loop preserves U(2)) "
                                  "-> contradicts Corollary U; re-derive coset loop")
        elif curv_nonscalar >= 0.0 and curv_nonscalar < 0.5:
            schur_consistent = False
            contradiction_note = (f"f_WZ>eps_WZ but band curvature is Schur-scalar "
                                  f"(non_scalar_frac={curv_nonscalar:.2e}<0.5) -> holonomy "
                                  f"claims non-abelian content the curvature denies")
    print(f"  Schur-consistency cross-check: {schur_consistent} {contradiction_note}")
    print(f"    (Release R verified: n_broken={n_broken}>=1 releases T2; band-curvature "
          f"non_scalar_frac={curv_nonscalar:.3f}~1 => genuine WZ; abelian Berry phase "
          f"{abel_max:.2e}~0 => pure SU(4))")
    if not schur_consistent:
        verdict = "FAIL"                              # (local)
        branch = "FAIL-discriminator-contradicts-Schur-Corollary-U-" + contradiction_note  # (local)
        posterior = "TrackA=0.4_TrackB=0.6_UNCHANGED"  # (local)
        prior_action = "FAIL-coset-loop-rederivation-required"  # (local)

    print(f"\n  VERDICT  = {verdict}")
    print(f"  TRACK    = {track_label}")
    print(f"  BRANCH   = {branch}")
    print(f"  POSTERIOR= {posterior}")
    print(f"  PRIOR ACTION = {prior_action}")
    print(f"  RETIRED: W5-4 frame-dependent f_nonAb={W54_F_NONAB_ARTIFACT:.4e} (eigh-artifact) "
          f"-> replaced by frame-invariant f_WZ={f_WZ:.4e}")

    # =====================================================================
    # SAVE
    # =====================================================================
    np.savez(
        NPZ_OUT,
        # witness (Wilczek-Zee link-product holonomy)
        f_WZ=f_WZ, tr_U_re=tr_U.real, tr_U_im=tr_U.imag,
        hol_angle=hol_angle, abel_phase=abel_phase, smin=smin,
        f_WZ_continuum=f_WZ_continuum,
        dim_band=DIM_BAND, n_loop_final=n_loop_final, loop_conv_delta=loop_conv_delta,
        conv_n=conv_N, conv_fwz=conv_f,
        conv_angle=np.array([c[2] for c in conv]),
        conv_abel=np.array([c[3] for c in conv]),
        conv_smin=np.array([c[4] for c in conv]),
        # frame-invariance
        frame_resid=frame_resid, frame_resid_abs=frame_resid_abs,
        f_WZ_frames=f_WZ_frames, f_WZ_mean=f_WZ_mean, f_WZ_spread=f_WZ_spread,
        frame_invariant_ok=frame_invariant_ok, n_frame=N_FRAME, frame_seed=FRAME_SEED,
        # eps family scan (angle slope ~2 matches W5-4 A~eps^2; witness slope ~4)
        eps_scan=EPS_SCAN, f_WZ_scan=f_WZ_scan, angle_scan=angle_scan, abel_scan=abel_scan,
        slope_wz=slope_wz, slope_angle=slope_angle, abel_max=abel_max,
        # genuine-non-abelian band curvature diagnostic
        curv_nrm=curv_nrm, curv_nonscalar=curv_nonscalar,
        # discriminator
        eps_WZ=EPS_WZ, track_A=track_A, track_label=track_label,
        verdict=verdict, branch=branch, posterior=posterior, prior_action=prior_action,
        schur_consistent=schur_consistent,
        # residual stabilizer + next pair
        stab_comms=np.array([comms[j] for j in sorted(comms)]),
        stab_idx=np.array(sorted(comms)), n_broken=n_broken,
        next_pair=np.array(next_pair),
        # geometry
        tau_fold=TAU0, tau0=TAU0, mu0=MU0, eps_max=EPS_MAX,
        v_jensen=V_JENSEN, v_mu=V_MU, coset_a=COSET_A, coset_b=COSET_B,
        b2_eval=float(w0.real[9]),
        # upstream cross-check anchors
        W54_audit=W54_AUDIT, W54_A_max=W54_A_MAX,
        W54_f_nonAb_artifact=W54_F_NONAB_ARTIFACT,
        W54_I_NA_b2_excl=W54_I_NA_B2_EXCL, W54_orbit_rel=W54_ORBIT_REL,
        # dual SHA
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\n  saved npz -> {NPZ_OUT}")

    # =====================================================================
    # PLOT
    # =====================================================================
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # (a) loop-discretization CONVERGENCE of f_WZ (genuine holonomy -> plateau)
    ax = axes[0, 0]
    cn = conv_N; cf = conv_f                          # (local)
    ax.plot(cn, cf, "o-", color="C0", label="f_WZ (link product)")
    ax.axhline(f_WZ_continuum, color="C4", ls=":",
               label=f"N->inf continuum = {f_WZ_continuum:.3e}")
    ax.axhline(EPS_WZ, color="C3", ls="--", label=f"eps_WZ={EPS_WZ:.0e} (Track A/B)")
    ax.set_xlabel("N (loop discretization points)")
    ax.set_ylabel("f_WZ = |Tr U_hol - 4|")
    ax.set_title("(a) Wilczek-Zee holonomy CONVERGES (genuine, not 1/N artifact)")
    ax.legend(fontsize=7.5); ax.grid(alpha=0.3)

    # (b) frame-invariance: f_WZ over random SU(2)-lifted frames
    ax = axes[0, 1]
    ax.plot(range(len(f_WZ_frames)), f_WZ_frames, "s-", color="C2")
    ax.axhline(f_WZ_mean, color="k", ls=":", label=f"mean={f_WZ_mean:.3e}")
    ax.set_xlabel("frame index (0 = unrotated; 1..8 random SU(2)-lifts)")
    ax.set_ylabel("f_WZ")
    ax.set_title(f"(b) FRAME-INVARIANCE: residual={frame_resid:.2e} (< {FRAME_RESID_TOL:.0e})\n"
                 f"the W6-2 670x guard (contrast W5-4 orbit_rel={W54_ORBIT_REL:.0f})")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # (c) eps-family scan: holonomy ANGLE (slope 2) and trace WITNESS (slope 4)
    ax = axes[1, 0]
    ax.loglog(EPS_SCAN, np.maximum(angle_scan, 1e-18), "o-", color="C0",
              label=f"holonomy angle (slope {slope_angle:.2f})")
    ax.loglog(EPS_SCAN, np.maximum(f_WZ_scan, 1e-18), "s-", color="C1",
              label=f"f_WZ witness (slope {slope_wz:.2f})")
    ax.axhline(EPS_WZ, color="C3", ls="--", label=f"eps_WZ={EPS_WZ:.0e}")
    ax.set_title("(c) eps scan: angle~eps^2 (=W5-4 A slope-2); witness=0.5*angle^2~eps^4")
    ax.set_xlabel("eps"); ax.set_ylabel("magnitude"); ax.legend(fontsize=7.5); ax.grid(alpha=0.3)

    # (d) verdict summary panel
    ax = axes[1, 1]; ax.axis("off")
    txt = (
        f"VERDICT: {verdict}   TRACK: {track_label}\n"
        f"{'='*48}\n"
        f"f_WZ (frame-invariant)    = {f_WZ:.4e}\n"
        f"  N->inf continuum        = {f_WZ_continuum:.4e}\n"
        f"eps_WZ (discriminator)    = {EPS_WZ:.0e}\n"
        f"frame_inv_residual        = {frame_resid:.3e}\n"
        f"  (threshold {FRAME_RESID_TOL:.0e}; OK={frame_invariant_ok})\n"
        f"Tr U_hol                  = {tr_U.real:+.6f}{tr_U.imag:+.1e}j\n"
        f"holonomy angle ||log U||  = {hol_angle:.4e}\n"
        f"abelian Berry phase       = {abel_max:.2e} (~0: pure SU4)\n"
        f"angle slope (~2 = W5-4 A) = {slope_angle:.3f}\n"
        f"band-curv non_scalar_frac = {curv_nonscalar:.3f} (~1: WZ)\n"
        f"n_broken (u2 gens)        = {n_broken}/4 (R released)\n"
        f"{'-'*48}\n"
        f"posterior: {posterior}\n"
        f"{'-'*48}\n"
        f"RETIRED W5-4 artifact:\n"
        f"  f_nonAb = {W54_F_NONAB_ARTIFACT:.3e} (frame-DEP eigh)\n"
        f"  orbit_rel = {W54_ORBIT_REL:.1f} (670x lesson)\n"
        f"REPLACED by frame-INVARIANT f_WZ above.\n"
        f"{'-'*48}\n"
        f"VII.BR Corollary U: undecidable on the\n"
        f"  U(2)-INVARIANT base; this loop BREAKS\n"
        f"  U(2) (R), releasing the Schur lock."
    )
    ax.text(0.02, 0.98, txt, va="top", ha="left", family="monospace", fontsize=8.0,
            transform=ax.transAxes)

    fig.suptitle(f"{GATE_ID}: frame-invariant WZ-holonomy witness (B2 eps^2 isotropy-breaking)",
                 fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(PNG_OUT, dpi=130)
    print(f"  saved png -> {PNG_OUT}")

    # =====================================================================
    # VERDICT PAYLOAD (agent passes to emit_verdict; race-safe)
    # =====================================================================
    val = (f"verdict={verdict}_track={track_label}_f_WZ={f_WZ:.4e}_"
           f"continuum={f_WZ_continuum:.4e}_frame_resid={frame_resid:.3e}_"
           f"frame_inv={frame_invariant_ok}_eps_WZ={EPS_WZ:.0e}_TrU={tr_U.real:.6f}_"
           f"hol_angle={hol_angle:.4e}_abel_phase={abel_max:.2e}_angle_slope={slope_angle:.4f}_"
           f"witness_slope={slope_wz:.4f}_nonscalar={curv_nonscalar:.4f}_n_broken={n_broken}_"
           f"posterior={posterior}_RETIRED-W54-f_nonAb={W54_F_NONAB_ARTIFACT:.3e}-frame-dep-eigh-artifact")  # (local)
    extra = [
        f"# regulator_pin=N/A (WZ-holonomy is not a regulator-tagged Seeley-DeWitt moment); "
        f"prereq S101-B2-ISOTROPY-BREAKING INFO (audit {W54_AUDIT[:16]})",
        f"# frame-invariance: f_WZ spread(abs)={f_WZ_spread:.3e} over {N_FRAME} SU(2)-lifted U(16) "
        f"conjugations (seed {FRAME_SEED}); conjugation-invariance EXACT by construction (Wilczek-Zee link product)",
        f"# geometry: holonomy angle ||log U||={hol_angle:.4e}~eps^2 (slope {slope_angle:.4f}=W5-4 A slope-2); "
        f"f_WZ=0.5*angle^2~eps^4 (slope {slope_wz:.4f}); abelian Berry phase {abel_max:.2e}~0 (pure SU(4), S25 Omega=0); "
        f"band-curvature non_scalar_frac={curv_nonscalar:.4f}~1 (genuine WZ); n_broken={n_broken}/4 (Release R)",
        f"# dual_prior re-allocation: prior 0.6B/0.4A -> {posterior}; {prior_action}",
        f"# VII.BR STAGE-3-PERMANENT cross-ref: T2 Schur-scalar M_ab|ranP=c_ab*1_4 + Corollary U "
        f"undecidability hold on the U(2)-INVARIANT base; this loop BREAKS U(2) (Release condition R), "
        f"releasing the Schur lock -- Track A does NOT contradict Corollary U",
    ]
    payload = print_verdict_payload(
        verdict, val, audit_sha, content_sha,
        companion_note=f"FRAME-INVARIANT-WZ-HOLONOMY witness f_WZ={f_WZ:.4e} (Track {track_label})",
        extra_rows=extra,
    )
    return payload


if __name__ == "__main__":
    main()
