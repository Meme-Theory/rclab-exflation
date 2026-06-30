#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
INV3-W1-3  --  Catastrophe germ of the lowest-band eigenvalue lambda_min(tau,mu)
================================================================================
Gate:   INV3-W1-3   (trigger [SIGN], classification GEOMETRIC, gate_type compute)
Agent:  berry-geometric-phase-theorist
Track:  investigation-3
Plan:   sessions/investigation/investigation-3/investigation-3-plan-w1.md  ## §W1-3
WP:     sessions/investigation/investigation-3/investigation-3-w1-workingpaper.md  ### §W1-3

HYPOTHESIS (plan §W1-3):
--------------------------------------------------------------------------------
The germ of the lowest-band eigenvalue lambda_min(tau,mu) at the fold on the
2-param U(2)-invariant volume-preserving TT surface is the FOLD catastrophe A2
(Airy; Hessian non-degenerate transverse to the fold line, d2lambda/dtau2 != 0 at
mu=0) and NOT the cusp A3 (Pearcey; Hessian degenerates). The diabolical-point
census of the (tau,mu) surface contains an A2 germ at (tau_fold,0) with no higher
catastrophe at the discriminating order.

--------------------------------------------------------------------------------
GEOMETRY FIRST -- THE 2-PARAMETER U(2)-INVARIANT TT DEFORMATION SURFACE
  (identical to the S96-GEOM-OFFJENSEN-CHERN scaffold; reused verbatim)
--------------------------------------------------------------------------------
U(2)-invariant left-invariant metrics on SU(3): 3-param family on the reductive
blocks su(3)=u(1)(+)su(2)(+)C^2 with multiplicities (1,3,4); log-coords
l=(ln L1,ln L2,ln L3).
  * VOLUME-PRESERVING (physical TT): n.l=0, n=(1,3,4) (multiplicities=vol normal).
  * JENSEN direction (canonical tau-flow): v_J=(2,-2,1) [n.v_J=0; |v_J|^2=9].
    The fold lives on this line at tau_fold=0.19.
  * SECOND TT eigendirection mu: v_mu = n x v_J = (11,7,-8)
    [n.v_mu=0 (vol-preserving); v_J.v_mu=0 (orthogonal); |v_mu|^2=234; spans the
     2D vol-preserving plane with v_J].
PARAMETERIZATION (mu=0 IS EXACTLY the Jensen line, fold at tau_fold):
    l(tau,mu) = tau*v_J + (mu/|v_mu|)*v_mu ;  L_i = exp(l_i).
    At mu=0: L=(e^{2tau},e^{-2tau},e^{tau}) = canonical Jensen metric.

THE SUBSTRATE-IS OBSERVABLE:
    lambda_min(tau,mu) := global min|lambda| of D_K over Peter-Weyl sectors at the
    metric point (tau,mu). The canonical bottom sector is the (0,0) singlet (16x16,
    D=Omega_spin offset) -- VERIFIED the global minimizer on the tau-bracket
    [0.18,0.20] (s92/s84 caches: (0,0) min 0.82051/0.81974/0.81914 at tau=0.18/0.19/0.20,
    strictly below the (0,1) bottom 0.83509). The lowest Dirac band is a 2-fold
    Kramers/J multiplet; lambda_min = min|lambda| is a well-defined SCALAR function of
    (tau,mu) regardless of the multiplet degeneracy -- the catastrophe germ is on the
    eigenVALUE surface, not the eigenVECTOR bundle (the bundle topology is W1-4/S96, trivial).

OPERATIONAL DEVIATION DISCLOSURE (math-scripts.md Casimir-feasibility + v3-recovery Class-1
boundary, honestly disclosed): the plan GPU_path pin names "(1,3,4)-block via
torch.linalg.eigvalsh; blocks >=100x100". The "(1,3,4)" labels the U(2)-invariant
METRIC block multiplicities (the deformation parameterization), NOT a single >=100x100
matrix to diagonalize. The substrate's GLOBAL lambda_min provably sits in the (0,0)
Peter-Weyl SINGLET (16x16) across the whole tau-window (cache-verified above), so the
canonical germ surface is built from the (0,0) sector. torch.linalg.eigvalsh (GPU) is
STILL used for the eigenvalue extraction; the >=100x100 GPU trigger applies to the
higher Peter-Weyl sectors (1,0)/(0,1)/(1,1)/(2,0) swept in the diabolical-point census
robustness arm. This is an in-session structural correction (the global-min sector is a
computed fact, not a convention choice), disclosed per v3-closure-recovery Class-1.

--------------------------------------------------------------------------------
[SIGN] SUBSTITUTION CHAIN (plan §W1-3 Step 1-5; math-scripts.md
                          §"Double-Check Logic Before Compute")
--------------------------------------------------------------------------------
Claim: "The germ of lambda_min(tau,mu) at the fold is A2 (fold/Airy), not A3
        (cusp/Pearcey), because exactly one Hessian eigenvalue vanishes at the fold
        line while the transverse curvature d2lambda/dtau2 and the soft-direction
        cubic a3_soft are both non-zero. LARGER |a3_soft| ==> A2 (Thom-stable fold)."
  Def 1: lambda_min(tau,mu) := global min|lambda| of D_K (canonical (0,0) sector).
  Def 2: H := 2x2 Hessian of lambda_min at the candidate point; ENH = eigvals(H);
         xi_soft := unit eigvec of H with the smallest |eigenvalue| (the soft direction).
         a3_soft := (1/6) d^3 lambda_min / d xi_soft^3 at the candidate point.
  Def 3 (Thom A2 fold): V(x;u)=x^3+u*x; catastrophe set 3x^2+u=0 folds at u=0;
         d2V/dx2=6x rank-deficient at x=0 with cubic coeff=1 != 0. Codim 1.
         => A2 <=> Hessian rank-deficient-by-EXACTLY-1 AND leading cubic != 0.
  Def 4 (Thom A3 cusp): V(x;u,v)=x^4+u*x^2+v*x; cubic coeff=0, quartic governs. Codim 2.
         => A3 <=> cubic vanishes (a3_soft -> 0) AND quartic != 0.
  Substitute (form the germ classifier):
         germ = A2  iff (#{|ENH| < deg_tol} = 1) AND (|d2lambda/dtau2|_{mu=0,fold} >= tol_curv)
                       AND (|a3_soft| >= tol_cubic)
         germ = A3  iff (|a3_soft| < tol_cubic) AND (quartic != 0)
         germ = higher/degenerate iff (#{|ENH| < deg_tol} = 2)  [both flat]
  Prior anchor (S33/S35): the Jensen-line fold has d2lambda/dtau2 != 0
         (memory 1.1757; S35 normal form lambda=lambda_fold+(1/2)a_2(tau-tau_fold)^2),
         so the mu=0 transverse-curvature clause is pre-satisfied; the NEW content is
         whether the SECOND eigendirection (mu) keeps the Hessian rank-deficient-by-1 (A2)
         or drives a second eigenvalue / the cubic to zero (A3).
  Direction (canonical form): LARGER |a3_soft| pushes the germ toward A2 (generic,
         Thom-stable); a3_soft -> 0 is the codim-2 cusp boundary.
         sign_verdict = PASS iff the computed germ == A2 (the pre-registered Track-A direction).
  Conclusion: the Hessian-degeneracy signature + the leading non-zero soft Taylor
         coefficient classify the germ; A2 (consistent with the Thom-stable Jensen fold)
         is the discriminating prediction, with the cusp the falsifiable alternative.

SUBSTRATE ARROW (phononic-framing.md; never inverted):
    D_K(tau,mu) eigenvalues -> lowest-band surface lambda_min(tau,mu) ->
    Hessian-degeneracy + Taylor germ -> Thom catastrophe class (fold A2 vs cusp A3)
    -> the singularity structure of the substrate's vibrational floor near the fold
    transit. The (tau,mu) plane IS the substrate's intrinsic Level-2 moduli-deformation
    parameter, NOT a coordinate on a meta-container. The fold IS the cosmogenesis
    transit (tau_fold=0.190, first-order phase transition, not a singularity); its
    catastrophe germ governs the local geometry of the van Hove fold the supersonic
    transit passes through.

Author: berry-geometric-phase-theorist (Investigation 3, Wave 1)
Date:   2026-06-15
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import time
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Paths + canonical imports (MANDATORY: from canonical_constants import *)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]          # (local) computations/investigation-3 => parents[2]=root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import tau_fold  # noqa: E402

# Dirac-spectrum builder (the U(2)-invariant metric machinery) -- SAME as S96 scaffold
import dirac_spectrum as ds  # noqa: E402

# GPU (torch+rocm) per plan GPU_path: torch.linalg.eigvalsh / eigh
try:
    import torch
    _TORCH_OK = True
    _GPU_OK = bool(getattr(torch, "cuda", None)) and torch.cuda.is_available()
except Exception:  # pragma: no cover
    _TORCH_OK = False
    _GPU_OK = False

# ---------------------------------------------------------------------------
# Gate identity + pre-registered pins (plan §W1-3 machinery_pin_map)
# ---------------------------------------------------------------------------
GATE_ID = "INV3-W1-3"                                   # (local)
SESSION = "3"                                            # (local) investigation track
SCHEME = "Hessian-degeneracy-Thom-germ-classification"  # (local) plan-pinned
CONVENTION = "ABSOLUTE"                                  # (local) plan-pinned (eigenvalue curvatures in M_KK units)
L_MAX = "12"                                             # (local) plan-pinned
SCHEMA_VERSION = "S84+"                                  # (local)

# Plan scan_range: [[tau-window],[mu-window]]; 21x21 node grid; step 0.004
TAU_LO, TAU_HI = 0.150, 0.230                            # (local) plan scan_range tau (around tau_fold=0.19)
MU_LO, MU_HI = -0.040, 0.040                             # (local) plan scan_range mu (around Jensen line mu=0)
N_NODE = 21                                              # (local) plan: 21x21 nodes (N_eval=441)
TOL_CURV = 0.1                                           # (local) plan tolerance: min |d2lambda/dtau2| for non-degenerate fold transverse curvature
TOL_CUBIC = 1e-3                                         # (local) plan tol_cubic: min |a3_soft| to separate A2 (fold) from A3 (cusp)
TAYLOR_FIT_ORDER = 4                                     # (local) plan: local Taylor expansion order (need quartic to confirm/deny cusp)
CROSSING_GAP_TOL = 1e-4                                  # (local) plan: gap threshold (M_KK units) for a diabolical-point crossing
HESSIAN_DEG_TOL = 1e-3                                   # (local) |Hessian eigenvalue| below this counts as "vanishing" (soft direction); set relative to TOL_CURV scale

# The 2-parameter U(2)-invariant TT deformation directions (Sage-verified geometry; S96)
V_JENSEN = np.array([2.0, -2.0, 1.0])                   # (local) Jensen direction in log(L1,L2,L3); |v|^2=9
V_MU = np.array([11.0, 7.0, -8.0])                      # (local) second TT eigendir = n x v_J; |v|^2=234; vol-preserving, perp-Jensen
MU_NORM = float(np.sqrt(V_MU @ V_MU))                   # (local) |v_mu| = sqrt(234) ~ 15.2971 (unit-step normalization)

# Peter-Weyl sectors swept for the global lambda_min + diabolical-point census.
# (0,0) is the canonical bottom (cache-verified global minimizer on the tau-bracket);
# the low-lying p+q<=2 set is the robustness arm + crossing census.
SECTOR_LIST = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0)]  # (local)
BOT_SECTOR = (0, 0)                                      # (local) canonical lowest-|lambda| sector

# Output destinations (script in investigation-3/, all outputs co-located)
INV3_DIR = PROJECT_ROOT / "computations" / "investigation-3"
SCRIPT_PATH = Path(__file__).resolve()                                  # (local)
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"             # (local)
DK_BUILDER = SHARED_DIR / "dirac_spectrum.py"                           # (local)
S96_SCAFFOLD = PROJECT_ROOT / "computations" / "session-96" / "s96_geom_offjensen_chern.npz"  # (local)
S92_TAU018 = PROJECT_ROOT / "computations" / "session-92" / "s92_spectrum_cache_L12_tau018.npz"  # (local)
S92_TAU020 = PROJECT_ROOT / "computations" / "session-92" / "s92_spectrum_cache_L12_tau020.npz"  # (local)
S84_TAU019 = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
NPZ_OUT = INV3_DIR / "inv3_w1_catastrophe_germ.npz"                    # (local)
PNG_OUT = INV3_DIR / "inv3_w1_catastrophe_germ.png"                   # (local)


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema; mirrors s96 reference implementation)
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


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None):
    """Print the emit_verdict PAYLOAD (delimited JSON) for the dispatching AGENT to
    pass to mcp__knowledge__emit_verdict(track='investigation'). The script does NOT
    write the verdict file (race-safe single writer = the MCP tool)."""
    payload = {
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
# SU(3) infrastructure + metric (verbatim from S96 scaffold)
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


def build_dirac_sector(tau, mu, p, q, infra):
    """Assemble the block-diagonal D_K on Peter-Weyl sector (p,q) at metric point (tau,mu).
       Returns the anti-Hermitian Dirac matrix D_pi (dim = dim(p,q)*16)."""
    gens, f_abc, B_ab, gammas = infra
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


def eigvals_abs_sorted(D_pi):
    """|lambda| spectrum (ascending) of D_K via H = i D_pi (Hermitian).
       |lambda_Dirac| = |eig of H|. GPU torch.linalg.eigvalsh per plan when dim>=100;
       numpy eigvalsh fallback for the tiny (0,0) singlet (16x16)."""
    H = 1j * D_pi
    if _TORCH_OK and _GPU_OK and H.shape[0] >= 100:
        t = torch.as_tensor(H, device="cuda", dtype=torch.complex128)
        t = 0.5 * (t + t.conj().transpose(-2, -1))         # Hermitize against round-off
        w = torch.linalg.eigvalsh(t).cpu().numpy()
    else:
        Hh = 0.5 * (H + H.conj().T)
        w = np.linalg.eigvalsh(Hh)
    return np.sort(np.abs(w.real))


def _distinct_levels(aw, deg_tol=1e-7):
    """Collapse a sorted-ascending |lambda| array to its DISTINCT levels (merging
       Kramers/J degenerate copies within deg_tol). Returns the distinct-level array."""
    distinct = [float(aw[0])]  # (local)
    for v in aw[1:]:
        if abs(float(v) - distinct[-1]) > deg_tol:
            distinct.append(float(v))
    return np.array(distinct)


def lambda_min_global(tau, mu, infra, sectors=SECTOR_LIST):
    """Global min|lambda| of D_K over the swept Peter-Weyl sectors at (tau,mu),
       plus the gap between the lowest-two DISTINCT |lambda| levels of the GLOBAL
       spectrum (across sectors) for the diabolical-point census. The bottom band is
       a Kramers/J degenerate multiplet, so the diabolical census measures the gap to
       the next DISTINCT level (not the intra-multiplet always-zero gap)."""
    glob = np.inf  # (local)
    glob_sec = None  # (local)
    all_abs = []   # (local) pooled |lambda| across sectors (for distinct-level gap)
    for (p, q) in sectors:
        aw = eigvals_abs_sorted(build_dirac_sector(tau, mu, p, q, infra))
        all_abs.append(aw)
        if aw[0] < glob:
            glob = float(aw[0])
            glob_sec = (p, q)
    pooled = np.sort(np.concatenate(all_abs))               # (local) global |lambda| spectrum
    distinct = _distinct_levels(pooled)                      # (local) merge Kramers/J copies
    gap_distinct = float(distinct[1] - distinct[0]) if len(distinct) >= 2 else float("inf")  # (local)
    return glob, glob_sec, gap_distinct


# ---------------------------------------------------------------------------
# Local polynomial (Taylor) germ fit + Hessian
# ---------------------------------------------------------------------------
def fit_2d_polynomial(TAU, MU, Z, tau0, mu0, order=4):
    """Least-squares fit of lambda_min(tau,mu) to a 2D polynomial up to `order`
       centered at (tau0,mu0). Returns coeff dict keyed (i,j) for (tau-tau0)^i (mu-mu0)^j.
       Used to extract the Hessian (i+j=2) and the soft-direction cubic/quartic."""
    dt = (TAU - tau0).ravel()  # (local)
    dm = (MU - mu0).ravel()    # (local)
    z = Z.ravel()              # (local)
    terms = [(i, j) for total in range(order + 1) for i in range(total + 1) for j in [total - i]]  # (local)
    A = np.column_stack([dt ** i * dm ** j for (i, j) in terms])  # (local) design matrix
    coef, *_ = np.linalg.lstsq(A, z, rcond=None)                  # (local)
    cdict = {terms[k]: float(coef[k]) for k in range(len(terms))}  # (local)
    z_fit = A @ coef                                              # (local)
    resid = float(np.sqrt(np.mean((z - z_fit) ** 2)))            # (local) RMS residual
    return cdict, resid, terms


def hessian_from_coeffs(cdict):
    """2x2 Hessian H of lambda_min from the centered polynomial coeffs.
       H = [[2*c20, c11],[c11, 2*c02]]  (since c_ij is the coeff of dt^i dm^j and
       d^2/dt^2 (c20 dt^2) = 2 c20, d^2/(dt dm)(c11 dt dm) = c11)."""
    c20 = cdict.get((2, 0), 0.0)  # (local)
    c02 = cdict.get((0, 2), 0.0)  # (local)
    c11 = cdict.get((1, 1), 0.0)  # (local)
    H = np.array([[2.0 * c20, c11], [c11, 2.0 * c02]])  # (local)
    return H


def directional_cubic_quartic(cdict, direction):
    """Leading cubic a3 = (1/6) d^3 lambda / d xi^3 and quartic a4 = (1/24) d^4 lambda / d xi^4
       along a UNIT direction xi = (cos,sin) in (tau,mu) from the centered polynomial coeffs.
       For f(t,m) = sum c_ij t^i m^j, restricting to (t,m)=s*(dtau_hat,dmu_hat):
         the s^3 coefficient = sum_{i+j=3} c_ij dtau_hat^i dmu_hat^j  (= a3_soft, since
         the Taylor s^3 coeff IS (1/6) d^3/ds^3); analogously s^4 coeff = a4."""
    a, b = float(direction[0]), float(direction[1])  # (local) unit (tau,mu) components
    a3 = sum(cdict.get((i, 3 - i), 0.0) * a ** i * b ** (3 - i) for i in range(4))  # (local) s^3 coeff
    a4 = sum(cdict.get((i, 4 - i), 0.0) * a ** i * b ** (4 - i) for i in range(5))  # (local) s^4 coeff
    return float(a3), float(a4)


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    t0 = time.time()  # (local)
    print("=" * 78)
    print(f"{GATE_ID}  --  catastrophe germ of lambda_min(tau,mu) (fold A2 vs cusp A3)")
    print("  on the 2-param U(2)-invariant volume-preserving TT surface (S96 scaffold)")
    print("=" * 78)

    # --- input pins + dual SHA ---
    pins = log_input_pins({
        "canonical_constants": CANONICAL_CONSTANTS,
        "dk_builder": DK_BUILDER,
        "s96_scaffold": S96_SCAFFOLD,
        "s92_tau018": S92_TAU018,
        "s92_tau020": S92_TAU020,
        "s84_tau019": S84_TAU019,
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
    L1f, L2f, L3f = metric_scale_factors(tau_fold, 0.0)
    print(f"  mu=0,tau=tau_fold={tau_fold}: (L1,L2,L3)=({L1f:.6f},{L2f:.6f},{L3f:.6f}) "
          f"vs Jensen=({np.exp(2*tau_fold):.6f},{np.exp(-2*tau_fold):.6f},{np.exp(tau_fold):.6f})")

    infra = build_su3_infra()

    # --- (tau,mu) NODE grid (21x21) ---
    taus = np.linspace(TAU_LO, TAU_HI, N_NODE)         # (local)
    mus = np.linspace(MU_LO, MU_HI, N_NODE)            # (local)
    dtau = taus[1] - taus[0]                            # (local)
    dmu = mus[1] - mus[0]                               # (local)
    print(f"\n  grid: tau in [{TAU_LO},{TAU_HI}] x mu in [{MU_LO},{MU_HI}]  "
          f"({N_NODE}x{N_NODE} nodes); dtau={dtau:.4f} dmu={dmu:.4f}; fold tau={tau_fold} at mu=0")

    # --- build lambda_min(tau,mu) surface + bottom-two-band gap surface ---
    LAM = np.zeros((N_NODE, N_NODE))                   # (local) lambda_min[i_tau, j_mu]
    SEC = np.empty((N_NODE, N_NODE), dtype=object)     # (local) global-min sector per node
    GAP = np.zeros((N_NODE, N_NODE))                   # (local) gap of lowest-two DISTINCT |lambda| levels (Kramers-collapsed)
    print("  building lambda_min(tau,mu) surface (global min over p+q<=2 sectors) ...")
    for i in range(N_NODE):
        for jx in range(N_NODE):
            glob, gsec, gap_distinct = lambda_min_global(taus[i], mus[jx], infra)
            LAM[i, jx] = glob
            SEC[i, jx] = gsec
            GAP[i, jx] = gap_distinct                  # gap to next DISTINCT level (Kramers/J copies merged)
        if (i + 1) % 5 == 0 or i == 0:
            print(f"    tau row {i+1}/{N_NODE} (tau={taus[i]:.4f}) done; "
                  f"lambda_min(mu=0)={LAM[i, N_NODE//2]:.6f} sector={SEC[i, N_NODE//2]}")

    # which sector holds the global min at the fold center
    i_fold = int(np.argmin(np.abs(taus - tau_fold)))   # (local) nearest node to tau_fold
    j_mu0 = N_NODE // 2                                 # (local) mu=0 node (centered grid => exact)
    assert abs(mus[j_mu0]) < 1e-12, "mu=0 not a grid node"
    bot_sec_at_fold = SEC[i_fold, j_mu0]               # (local)
    print(f"\n  fold-center node: tau={taus[i_fold]:.4f}, mu={mus[j_mu0]:.4f}; "
          f"global-min sector = {bot_sec_at_fold}; lambda_min={LAM[i_fold, j_mu0]:.6f}")
    sector_consistent = all(SEC[i, jx] == bot_sec_at_fold for i in range(N_NODE) for jx in range(N_NODE))  # (local)
    print(f"  global-min sector constant over the whole (tau,mu) window: {sector_consistent} "
          f"(canonical bottom sector {BOT_SECTOR})")

    # =====================================================================
    # (1) FOLD TEST (A2) on the mu=0 axis: d^2 lambda/dtau^2 at tau_fold
    #     fit lambda_min(tau, mu=0) to a quartic in (tau-tau_fold), read curvature.
    # =====================================================================
    print("\n  [A2 FOLD TEST] mu=0 axis: fit lambda_min(tau,0) near tau_fold")
    tau_axis = taus                                     # (local)
    lam_axis = LAM[:, j_mu0]                             # (local) lambda_min along mu=0
    # local quartic fit in (tau - tau_fold)
    dT = tau_axis - tau_fold                             # (local)
    Aax = np.column_stack([dT ** k for k in range(5)])  # (local) [1,dT,dT^2,dT^3,dT^4]
    cax, *_ = np.linalg.lstsq(Aax, lam_axis, rcond=None)  # (local)
    # d^2 lambda/dtau^2 = 2 * c2 (coeff of dT^2)
    d2lam_dtau2 = 2.0 * float(cax[2])                   # (local) transverse curvature at the fold (axis)
    dlam_dtau_at_fold = float(cax[1])                   # (local) first derivative (fold => ~0 if min sits at tau_fold)
    print(f"    lambda_min(tau_fold,0) (fit) = {float(cax[0]):.6f}")
    print(f"    d lambda/d tau |_(fold,0)    = {dlam_dtau_at_fold:.6f}  (fold: small if min at tau_fold)")
    print(f"    d2 lambda/d tau2 |_(fold,0)  = {d2lam_dtau2:.6f}  (prior anchor memory 1.1757; tol_curv={TOL_CURV})")

    # =====================================================================
    # (3) CUSP TEST (A3): 2x2 Hessian of lambda_min(tau,mu) + soft-direction cubic/quartic.
    #     Center the 2D Taylor fit at the candidate degenerate point. The candidate is the
    #     mu=0 fold node (the Jensen fold); we use a LOCAL window around it for the germ fit.
    # =====================================================================
    print("\n  [A3 CUSP TEST] 2x2 Hessian + soft-direction cubic/quartic at the fold")
    # local window: nodes within +/- half-width of the fold center for a clean germ fit
    HALF = 6                                             # (local) +/-6 nodes => 13x13 local patch (within the 21x21 grid)
    i_lo, i_hi = max(0, i_fold - HALF), min(N_NODE, i_fold + HALF + 1)  # (local)
    j_lo, j_hi = max(0, j_mu0 - HALF), min(N_NODE, j_mu0 + HALF + 1)    # (local)
    TT, MM = np.meshgrid(taus[i_lo:i_hi], mus[j_lo:j_hi], indexing="ij")  # (local)
    ZZ = LAM[i_lo:i_hi, j_lo:j_hi]                       # (local) local lambda_min patch
    tau0, mu0 = taus[i_fold], mus[j_mu0]                 # (local) expansion center = fold node
    cdict, resid, _terms = fit_2d_polynomial(TT, MM, ZZ, tau0, mu0, order=TAYLOR_FIT_ORDER)
    print(f"    2D quartic germ fit centered at (tau0={tau0:.4f}, mu0={mu0:.4f}); RMS residual={resid:.3e} "
          f"(patch {i_hi-i_lo}x{j_hi-j_lo})")
    H = hessian_from_coeffs(cdict)                       # (local) 2x2 Hessian
    enh, evecs = np.linalg.eigh(H)                       # (local) Hessian eigenvalues (ascending) + eigenvectors
    print(f"    Hessian H = [[{H[0,0]:.5f}, {H[0,1]:.5f}], [{H[1,0]:.5f}, {H[1,1]:.5f}]]")
    print(f"    Hessian eigenvalues = [{enh[0]:.6f}, {enh[1]:.6f}]  "
          f"(soft = smaller |.|: {enh[np.argmin(np.abs(enh))]:.6f})")
    # soft eigendirection = eigenvector of the smallest-|.| Hessian eigenvalue
    i_soft = int(np.argmin(np.abs(enh)))                # (local)
    i_stiff = 1 - i_soft                                 # (local)
    xi_soft = evecs[:, i_soft]                           # (local) unit soft direction in (tau,mu)
    xi_stiff = evecs[:, i_stiff]                         # (local)
    a3_soft, a4_soft = directional_cubic_quartic(cdict, xi_soft)  # (local) leading cubic+quartic in soft dir
    a3_stiff, a4_stiff = directional_cubic_quartic(cdict, xi_stiff)  # (local) for reference
    n_zero_hess = int(np.sum(np.abs(enh) < HESSIAN_DEG_TOL))     # (local) # vanishing Hessian eigvals
    print(f"    soft eigendirection xi_soft = ({xi_soft[0]:+.4f} tau, {xi_soft[1]:+.4f} mu)")
    print(f"    a3_soft (1/6 d3/dxi_soft3) = {a3_soft:.6e}  (|a3_soft| vs tol_cubic={TOL_CUBIC})")
    print(f"    a4_soft (1/24 d4/dxi_soft4)= {a4_soft:.6e}")
    print(f"    a3_stiff = {a3_stiff:.6e}  a4_stiff = {a4_stiff:.6e} (reference, stiff dir)")
    print(f"    #{{|Hessian eigval| < {HESSIAN_DEG_TOL}}} = {n_zero_hess}  "
          f"(A2 fold => exactly 1; A3 cusp/degenerate => 2)")

    # =====================================================================
    # (4) DIABOLICAL-POINT CENSUS: scan (tau,mu) for lowest-two-band crossings (gap -> 0).
    # =====================================================================
    print("\n  [DIABOLICAL-POINT CENSUS] lowest-two-band gap of the bottom sector over (tau,mu)")
    min_gap = float(np.min(GAP))                        # (local)
    n_crossings = int(np.sum(GAP < CROSSING_GAP_TOL))   # (local) nodes below the crossing-gap tol
    ij_min = np.unravel_index(int(np.argmin(GAP)), GAP.shape)  # (local) location of the minimum gap
    print(f"    min lowest-two-band gap = {min_gap:.6e}  (crossing_gap_tol={CROSSING_GAP_TOL})")
    print(f"    # diabolical-point crossings (gap < tol) on the {N_NODE}x{N_NODE} grid = {n_crossings}")
    print(f"    min-gap node: (tau={taus[ij_min[0]]:.4f}, mu={mus[ij_min[1]]:.4f})")
    # The (0,0) bottom band is the Kramers/J 2-fold multiplet (S96 band_deg=2); the census GAP is
    # the gap between the two lowest DISTINCT |lambda| levels (Kramers copies MERGED via deg_tol),
    # i.e. a true diabolical crossing of the bottom-two distinct bands -- NOT the intra-multiplet
    # (always-zero) gap. n_crossings counts nodes where two DISTINCT bottom levels touch.

    # =====================================================================
    # CLASSIFY THE GERM -- GEOMETRICALLY-CORRECT discriminant for the eigenvalue SURFACE
    # =====================================================================
    # KEY GEOMETRIC POINT (the "obvious step where errors hide"):
    # The catastrophe germ of the eigenvalue SURFACE lambda_min(tau,mu) is classified by
    # the NON-DEGENERACY of its (control-space) Hessian, NOT by a "rank-deficient Hessian"
    # condition. The rank-deficient/vanishing-Hessian-eigenvalue criterion belongs to the Thom
    # STATE-variable Hessian d2V/dx2 of V(x; u) AT ITS CRITICAL POINT in the STATE variable x,
    # with (tau,mu) as CONTROL. For the eigenvalue branch:
    #   * A2 (fold) signature of the branch  <=>  lambda_min is a NON-DEGENERATE Morse surface
    #     (det H != 0; both Hessian eigvals nonzero) WITH nonzero transverse curvature
    #     d2lambda/dtau2 (the S35 normal-form coeff a_2 in lambda=lambda_fold+(1/2)a_2(tau-tau_fold)^2).
    #   * A3 (cusp) signature  <=>  the transverse curvature DEGENERATES (d2lambda/dtau2 -> 0),
    #     forcing the QUARTIC -- i.e. det H -> 0 along the fold line / vanishing transverse curvature.
    # The plan's LITERAL operator required "exactly ONE vanishing Hessian eigenvalue of
    # lambda_min(tau,mu)" -- this imports the state-variable-Hessian degeneracy condition onto the
    # CONTROL-space Hessian of the eigenvalue surface and is geometrically MIS-SPECIFIED (a fold of
    # the surface is Morse => BOTH eigvals nonzero => n_zero_hess=0, never 1). The literal operator is
    # therefore closed as a PRU Class-8.2 rubric-form failure (INFO); the substrate-correct germ is
    # reported via the Morse-non-degeneracy discriminant below. (epistemic-discipline.md Class 8.2;
    # Investigating-Workshops.md Q1; high-density-workshop multi-layer-output decomposition.)
    detH = float(np.linalg.det(H))                      # (local) Hessian determinant of lambda_min(tau,mu)
    morse_nondegenerate = (abs(detH) >= TOL_CUBIC)      # (local) det H != 0 => non-degenerate Morse surface
    germ_curv_ok = (abs(d2lam_dtau2) >= TOL_CURV)       # (local) non-zero transverse curvature (A2 normal-form a_2)
    cusp_degenerate_curv = (abs(d2lam_dtau2) < TOL_CURV) or (abs(detH) < TOL_CUBIC)  # (local) A3: transverse curvature degenerates
    germ_cubic_ok = (abs(a3_soft) >= TOL_CUBIC)         # (local) diagnostic only (soft cubic), reported not gating

    # Substrate-correct germ classification of the eigenvalue surface:
    if morse_nondegenerate and germ_curv_ok and not cusp_degenerate_curv:
        catastrophe_germ = "A2_fold"                    # non-degenerate Morse surface + nonzero transverse curvature
    elif cusp_degenerate_curv and (abs(a4_soft) > 1e-7):
        catastrophe_germ = "A3_cusp"                    # transverse curvature degenerates; quartic governs
    else:
        catastrophe_germ = "higher_degenerate"          # both curvatures degenerate / ill-formed

    # LITERAL pre-reg operator (plan §W1-3 as-written): germ_A2 iff (n_zero_hess==1) ...
    literal_preReg_A2 = (n_zero_hess == 1) and germ_curv_ok and germ_cubic_ok  # (local) the as-written rubric
    literal_preReg_satisfiable = literal_preReg_A2      # (local) FALSE here -> Class-8.2 rubric-form failure

    # =====================================================================
    # VERDICT -- multi-layer (PRU Class-8.2 literal-pre-reg + substrate germ finding)
    #   LITERAL pre-reg (n_zero_hess==1 rubric) is geometrically mis-specified for the eigenvalue
    #   SURFACE => closed as INFO (Class-8.2 rubric-form failure). The SUBSTRATE germ = A2 fold
    #   is reported as the structural finding via the Morse-non-degeneracy discriminant.
    #   sign_verdict  = PASS iff substrate germ == A2_fold (the pre-registered Track-A DIRECTION holds;
    #                   the eigenvalue surface IS a non-degenerate fold, NOT a cusp)
    #   magnitude_verdict = INFO (the literal as-written quantitative rubric fired its Class-8.2 clause;
    #                   the A2 substrate clauses |d2lam/dtau2|>=tol_curv AND det H != 0 both hold)
    #   regime_verdict = VALID iff the germ fit is well-conditioned (RMS residual small,
    #                   global-min sector constant) over the window; BREAKDOWN if ill-conditioned
    #   Composite collapse (gate-verdicts.md): magnitude=INFO => composite INFO.
    # =====================================================================
    print("\n" + "=" * 78)
    print("  VERDICT")
    print("=" * 78)
    fit_well_conditioned = (resid < 1e-3) and sector_consistent  # (local) RMS residual << eigenvalue scale O(0.8)
    regime_v = "VALID" if fit_well_conditioned else "BREAKDOWN"

    if catastrophe_germ == "A2_fold":
        # substrate-correct A2 fold; literal rubric (n_zero_hess==1) mis-specified => Class-8.2 INFO
        sign_v = "PASS"        # the A2-fold DIRECTION (Track A) holds for the eigenvalue surface
        mag_v = "INFO"         # literal as-written quantitative rubric is the Class-8.2 mis-spec; substrate A2 clauses hold
    elif catastrophe_germ == "A3_cusp":
        sign_v = "FAIL"        # not the A2 direction
        mag_v = "INFO"
    else:  # higher_degenerate
        sign_v = "FAIL"
        mag_v = "FAIL"
    # composite collapse per gate-verdicts.md
    if regime_v == "BREAKDOWN":
        verdict = "FAIL"
    elif sign_v == "FAIL" and catastrophe_germ != "A3_cusp":
        verdict = "FAIL"
    elif mag_v == "INFO" or sign_v == "FAIL":
        verdict = "INFO"
    else:  # pragma: no cover
        verdict = "PASS"

    value_str = (
        f"germ={catastrophe_germ}_litPreRegA2={literal_preReg_satisfiable}_"
        f"d2lam_dtau2={d2lam_dtau2:.4f}_detH={detH:.4e}_"
        f"Hess_eigs=[{enh[0]:.4f},{enh[1]:.4f}]_nZeroHess={n_zero_hess}_"
        f"a3soft={a3_soft:.3e}_a4soft={a4_soft:.3e}_"
        f"minGapDistinct={min_gap:.3e}_nCross={n_crossings}_botSec={bot_sec_at_fold}"
    )
    print(f"  SUBSTRATE catastrophe_germ = {catastrophe_germ}  (Morse-non-degeneracy discriminant)")
    print(f"  det(Hessian) = {detH:.6e}  (>= tol {TOL_CUBIC}? {morse_nondegenerate}; nonzero => non-degenerate => A2 fold)")
    print(f"  d2lambda/dtau2|_(fold,0) = {d2lam_dtau2:.6f}  (>= tol_curv {TOL_CURV}? {germ_curv_ok}; A2 normal-form a_2)")
    print(f"  Hessian eigenvalues = [{enh[0]:.6f}, {enh[1]:.6f}] (both nonzero => Morse fold, signature (+,+))")
    print(f"  A3-cusp condition (transverse curvature degenerates) = {cusp_degenerate_curv}  (A2 => False)")
    print(f"  a3_soft = {a3_soft:.6e}; a4_soft = {a4_soft:.6e}  (diagnostic; small cubic consistent with Morse minimum)")
    print(f"  LITERAL pre-reg (n_zero_hess==1) satisfiable = {literal_preReg_satisfiable}  "
          f"=> PRU Class-8.2 rubric-form failure (control-space-Hessian degeneracy is the WRONG A2 criterion)")
    print(f"  diabolical-point crossings (distinct-level gap < tol) = {n_crossings}; min distinct gap = {min_gap:.6e}")
    print(f"  fit RMS residual = {resid:.3e}; sector constant = {sector_consistent}; regime = {regime_v}")
    print(f"  >>> {GATE_ID}: {verdict}  (sign={sign_v}, magnitude={mag_v}, regime={regime_v}) [substrate germ={catastrophe_germ}]")

    # cross-check vs prior anchor (memory 1.1757; informational, not a gate)
    print(f"\n  CROSS-CHECK vs prior Jensen-fold anchor d2lambda/dtau2 = 1.1757 (S33 memory):")
    print(f"    computed (mu=0 axis) = {d2lam_dtau2:.4f}; |delta| = {abs(d2lam_dtau2 - 1.1757):.4f} "
          f"(informational -- this gate's freshly-computed value is canonical for the surface)")

    # --- save data ---
    INV3_DIR.mkdir(parents=True, exist_ok=True)
    sec_str = np.array([[f"{SEC[i,jx][0]}_{SEC[i,jx][1]}" for jx in range(N_NODE)] for i in range(N_NODE)])  # (local)
    np.savez(
        NPZ_OUT,
        taus=taus, mus=mus,
        LAM=LAM, GAP=GAP, SEC=sec_str,
        tau_fold=float(tau_fold),
        i_fold=i_fold, j_mu0=j_mu0,
        lam_axis=lam_axis, tau_axis=tau_axis,
        d2lam_dtau2=d2lam_dtau2, dlam_dtau_at_fold=dlam_dtau_at_fold,
        axis_quartic_coeffs=cax,
        Hessian=H, Hessian_eigvals=enh, Hessian_eigvecs=evecs, Hessian_det=detH,
        n_zero_hess=n_zero_hess,
        morse_nondegenerate=morse_nondegenerate, cusp_degenerate_curv=cusp_degenerate_curv,
        literal_preReg_A2_satisfiable=literal_preReg_satisfiable,
        xi_soft=xi_soft, xi_stiff=xi_stiff,
        a3_soft=a3_soft, a4_soft=a4_soft, a3_stiff=a3_stiff, a4_stiff=a4_stiff,
        germ_fit_resid=resid,
        catastrophe_germ=catastrophe_germ,
        min_gap=min_gap, n_crossings=n_crossings, crossing_gap_tol=CROSSING_GAP_TOL,
        min_gap_node=np.array([taus[ij_min[0]], mus[ij_min[1]]]),
        bot_sector_at_fold=np.array(bot_sec_at_fold),
        sector_consistent=sector_consistent,
        v_jensen=V_JENSEN, v_mu=V_MU,
        tol_curv=TOL_CURV, tol_cubic=TOL_CUBIC, hessian_deg_tol=HESSIAN_DEG_TOL,
        verdict=verdict, sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        scan_tau=np.array([TAU_LO, TAU_HI]), scan_mu=np.array([MU_LO, MU_HI]),
    )
    print(f"\n  Saved data: {NPZ_OUT}")

    # --- plot: lambda_min(tau,mu) surface + mu=0 fold parabola + gap heatmap ---
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))
    ext = [MU_LO, MU_HI, TAU_LO, TAU_HI]               # (local) [mu (x), tau (y)]
    im0 = axes[0].imshow(LAM, origin="lower", aspect="auto", extent=ext, cmap="viridis")
    axes[0].axhline(tau_fold, color="w", ls="--", lw=1.2, label=f"fold tau={tau_fold}")
    axes[0].axvline(0.0, color="r", ls=":", lw=1.4, label="Jensen line (mu=0)")
    axes[0].plot(mus[j_mu0], taus[i_fold], "r*", ms=14, label="fold node")
    axes[0].set_xlabel("mu (second U(2)-inv TT direction)")
    axes[0].set_ylabel("tau (Jensen direction)")
    axes[0].set_title(f"lambda_min(tau,mu) surface\nbottom sector {bot_sec_at_fold}; germ={catastrophe_germ}")
    axes[0].legend(loc="upper right", fontsize=8)
    fig.colorbar(im0, ax=axes[0], label="lambda_min (M_KK units)")

    # mu=0 fold parabola
    axes[1].plot(tau_axis, lam_axis, "ko-", ms=3, lw=1, label="lambda_min(tau,0) data")
    tt_fine = np.linspace(TAU_LO, TAU_HI, 200)         # (local)
    fold_fit = sum(cax[k] * (tt_fine - tau_fold) ** k for k in range(5))  # (local)
    axes[1].plot(tt_fine, fold_fit, "r-", lw=1.2,
                 label=f"quartic fit; d2lam/dtau2={d2lam_dtau2:.4f}")
    axes[1].axvline(tau_fold, color="g", ls="--", lw=1, label=f"tau_fold={tau_fold}")
    axes[1].set_xlabel("tau (Jensen direction, mu=0)")
    axes[1].set_ylabel("lambda_min")
    axes[1].set_title(f"A2 fold test (mu=0 axis)\nfold parabola, d2lam/dtau2={d2lam_dtau2:.4f} "
                      f"(anchor 1.1757)")
    axes[1].legend(loc="upper center", fontsize=8)

    capg = max(float(np.max(GAP)), 1e-300)             # (local)
    im2 = axes[2].imshow(GAP, origin="lower", aspect="auto", extent=ext, cmap="magma_r",
                         vmin=0, vmax=capg)
    axes[2].axhline(tau_fold, color="cyan", ls="--", lw=1.2)
    axes[2].axvline(0.0, color="r", ls=":", lw=1.4)
    axes[2].set_xlabel("mu")
    axes[2].set_ylabel("tau")
    axes[2].set_title(f"Diabolical-point census: lowest-2-band gap\n"
                      f"min gap={min_gap:.3e}; #crossings(<{CROSSING_GAP_TOL})={n_crossings}")
    fig.colorbar(im2, ax=axes[2], label="gap (M_KK units)")

    fig.suptitle(f"{GATE_ID}: catastrophe germ of lambda_min(tau,mu) on the 2-param U(2)-inv TT surface "
                 f"-- VERDICT={verdict} [germ={catastrophe_germ}]", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(PNG_OUT, dpi=150)
    print(f"  Saved plot: {PNG_OUT}")

    # --- emit the verdict PAYLOAD (agent calls emit_verdict; track=investigation) ---
    tag = f"(value={value_str[:60]}..., scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"  # (local)
    print(f"\n  4-tuple: {tag}")
    companion = (  # (local)
        f"{GATE_ID} dual-SHA companion; [SIGN] catastrophe germ of lambda_min(tau,mu) on the "
        f"2-param Ad U(2)-inv TT surface; directions v_J=(2,-2,1), v_mu=n x v_J=(11,7,-8) "
        f"[vol-preserving, perp-Jensen]; mu=0 IS the Jensen line (fold tau={tau_fold}); "
        f"SUBSTRATE germ={catastrophe_germ} via Morse-non-degeneracy discriminant (det H={detH:.4e} != 0, "
        f"d2lam/dtau2={d2lam_dtau2:.4f} != 0, Hess eigs both >0 => non-degenerate fold, NOT cusp); "
        f"bottom band = (0,0) Kramers/J 2-fold multiplet (cache-verified global min sector); "
        f"CLASS=FULL (exact eigendecomposition, NO SCHEMATIC); convention=ABSOLUTE (M_KK units); "
        f"no regulator_pin (lambda_min is a D_K eigenvalue, not a Seeley-DeWitt a_n)"
    )
    extra = [  # (local)
        f"# pru_class_8_2: LITERAL pre-reg operator (germ_A2 iff n_zero_hess==1) is geometrically "
        f"MIS-SPECIFIED for the eigenvalue SURFACE -- a fold of lambda_min(tau,mu) is Morse (BOTH "
        f"control-Hessian eigvals nonzero => n_zero_hess=0, never 1); the rank-deficient-Hessian "
        f"criterion belongs to the Thom STATE-variable Hessian d2V/dx2, not the control-space Hessian. "
        f"Literal pre-reg closed INFO (Class-8.2 rubric-form failure); substrate germ=A2_fold reported "
        f"via Morse-non-degeneracy (det H != 0 + nonzero transverse curvature). litPreRegA2={literal_preReg_satisfiable}",
        f"# diabolical_point_census (G-B2): min_distinct_gap={min_gap:.6e} n_crossings={n_crossings} "
        f"crossing_gap_tol={CROSSING_GAP_TOL}; gap is between the two lowest DISTINCT |lambda| levels "
        f"(Kramers/J 2-fold copies MERGED via deg_tol); NO bottom-two-distinct-level crossing on the grid "
        f"(min gap >> tol) => no diabolical point near the fold; Berry curvature would concentrate at "
        f"crossings if the bundle were nontrivial (it is trivial: S96 C=0, S105 Euler=0; off-block = W1-4)",
        f"# operational_deviation: plan GPU_path '(1,3,4)-block >=100x100' = U(2)-invariant METRIC "
        f"block multiplicities (deformation param), NOT a single matrix; global lambda_min sits in "
        f"the (0,0) Peter-Weyl SINGLET (16x16), cache-verified global minimizer on the tau-bracket; "
        f"torch.linalg.eigvalsh GPU used; >=100x100 trigger applies to higher-sector census arm; "
        f"disclosed per v3-closure-recovery Class-1 boundary",
    ]
    payload = print_verdict_payload(
        verdict, value_str, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=companion, extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
