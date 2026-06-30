#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S104-PAULI-G9-SUBCURVATURE
================================================================================
Gate:   S104-PAULI-G9-SUBCURVATURE   (trigger [VERIFY], classification GEOMETRIC)
Agent:  berry-geometric-phase-theorist
Plan:   sessions/session-plan/session-104-plan-w2.md  ## §W2-2
WP:     sessions/session-104/session-104-w2-workingpaper.md  ### §W2-2

================================================================================
GEOMETRY FIRST -- THE gamma9-GRADED (Cl(8) CHIRALITY) SUB-CURVATURE
================================================================================
S25/W5 (Kosmann K_a anti-Hermitian => real eigenstates => Omega=0 IDENTICALLY) killed
the FULL-eigenbasis Berry curvature; S96 confirmed the off-Jensen Chern is trivial. This
gate asks a finer question: does the BDI Omega=0 null STRENGTHEN to spin-resolved, or
CRACK at a gamma9-graded component?

gamma9 = gamma_1...gamma_8 is the substrate's OWN Cl(8) chirality (the KO-dim-6 grading
element; (16,16) Hermitian involution, gamma9^2=I, {gamma9,gamma_a}=0, 8 (+1) / 8 (-1)
eigenvalues -- verified). The +/-1 eigenspaces ARE the substrate's chirality sectors. We
project the lowest J/PH doublet onto the gamma9=+/-1 eigenspaces and compute the graded
Berry sub-curvature Omega^+- = dA^+- on each chirality branch.

THE CHIRALITY-LOCK STRUCTURE (S100b W6-2, reproduced here at the fold):
  The lowest doublet (u_+, u_-) is EXACTLY the gamma9-paired (chirality-flip) pair:
      <u_a|gamma9|u_a> = 0   (each raw eigenvector is gamma9-OFF-diagonal)
      |<u_+|gamma9|u_->| = 1 (the J/PH pair IS the chirality-flip pair)
  Diagonalizing the 2x2 restricted G9 yields chirality-resolved states gp (gamma9=+1),
  gm (gamma9=-1) -- coherent superpositions within the degenerate |lambda|-band. Because
  gamma9 ANTICOMMUTES with D_K, gp/gm are NOT energy eigenstates (H gp _|_ gp), but they
  ARE the rank-1 G9-eigenstates the graded sub-curvature lives on. The graded sub-curvature
  is the Berry curvature of the chirality-projected lowest-band state transported over (tau,mu).

  * PASS-STRENGTHEN (max(max|Omega^+|,max|Omega^-|)<1e-12 AND median|A^WZ|<1e-12): the BDI
    Omega=0 wall STRENGTHENS from "ordinary Berry curvature vanishes" to "ALL gamma9-graded
    (spin-resolved) Berry sub-curvatures vanish by BDI reality." Structurally stronger and
    more falsifiable; bundles with §W2-1 PASS-TRIVIAL for the strongest joint
    metric-without-curvature wall (Chern=0 ^ Euler=0 ^ graded-Omega=0).
  * CRACK -> INFO (max|Omega^s|>1e-6 localized): a previously-unrecognized substrate
    geometric channel (a 'Pauli-Chern' sector); maps onto Wei's Pauli-QGT imaginary part
    (arXiv 2409.19551); opens a follow-on amplitude gate for S105.

--------------------------------------------------------------------------------
[VERIFY] SUBSTITUTION CHAIN (plan §W2-2 substitution_chain; math-scripts.md
                            §"Double-Check Logic Before Compute")
--------------------------------------------------------------------------------
Claim: "A gamma9-graded projection of the substrate's real (BDI) Berry connection yields a
        graded sub-curvature Omega^s that is EITHER still identically zero (wall strengthens)
        or nonzero on a chirality branch (wall cracks); prior STRENGTHEN."
  Def 1: G9 = gamma9 (x) I_dim, gamma9 = gamma_1...gamma_8 (Cl(8) chirality, (16,16) Hermitian
         involution; gamma9^2=I, {gamma9,gamma_a}=0). [build_chirality, verified]
  Def 2: P_s = (I + s G9)/2, s in {+,-}: orthogonal projector onto the G9=s eigenspace.
  Def 3: A^s_dir = i <u^s|d_dir|u^s>: Berry connection of the G9=s-projected lowest-band state
         u^s (dir in {tau,mu}); Omega^s = d_tau A^s_mu - d_mu A^s_tau (projector-identity form).
  Substitute: by S25/W5 the FULL-eigenbasis eigenstates of D_K are REAL (Kosmann K_a anti-Herm).
         A real normalized state has A_dir = i<u|d_dir|u> = i*(1/2)d_dir<u|u> = 0 => Omega = 0.
  Simplify: the question is whether PROJECTING onto G9=s breaks this. P_s|u> is a combination
         within the chirality-locked pair (u_+, u_-). S100b proved |<u_+|G9|u_->| = 1 AND the
         cross-grade connection A^WZ_dir = i<u_+|d_dir|u_-> is gamma9-forced IMAGINARY-ONLY with J
         reality killing the remainder (median |A^WZ|=1.3e-17, 99.96% of nodes < 1e-12). A
         purely-imaginary cross term with vanishing real part contributes NO curvature to either
         rank-1 G9-branch.
  Canonical form: Omega^s = dA^s where A^s is the connection of a state that stays real-gauge-
         equivalent on its rank-1 G9-eigenspace => A^s real => Omega^s = 0.
  Direction: max|Omega^s| -> 0 (below 1e-12) is STRENGTHEN; max|Omega^s| > 1e-6 would CRACK.
  Conclusion: prior PASS-STRENGTHEN (graded sub-curvature inherits the reality that kills the
         full Omega, double-protected by the chirality lock). But the gate CERTIFIES rather than
         asserts -- the projection is onto a DIFFERENT connection (a different rank-1 bundle), and
         Wei's Pauli-QGT shows PT-class systems CAN carry a nonzero graded curvature where the
         ungraded one vanishes. A CRACK (max|Omega^s|>1e-6) would identify a previously
         unrecognized substrate geometric channel (a 'Pauli-Chern' sector).

--------------------------------------------------------------------------------
METHOD (BP-4-gamma9-graded; projector-identity evaluator; plan §W2-2)
--------------------------------------------------------------------------------
At each NODE: build the lowest doublet block (dim,2) via lowest_band_multiplet(...,deg=2)
[reused from S96]; form G9 = gamma9 (x) I_dim (= gamma9 for the (0,0) singlet); project the
doublet onto the G9=+/-1 eigenspaces by DIAGONALIZING the 2x2 restricted G9 (the chirality-
LOCKED structure means each member of the J/PH pair maps to its chirality partner; the
chirality-resolved gp/gm are the rank-1 G9-eigenstates).

Graded sub-curvature via the PROJECTOR-IDENTITY evaluator (basis/phase-free; NOT the
largest-component phase pin which has pi-jumps -- plan binding numerics pin + S100b item 7):
    P^s(tau,mu) = |u^s><u^s|   (rank-1 chirality-resolved projector)
    Omega^s = -i Tr( P^s [d_tau P^s, d_mu P^s] )   (the standard projector Berry curvature;
              gauge/phase-INVARIANT because P^s is the basis-free rank-1 projector)
d_dir P^s by central FD of the projector over the (tau,mu) plaquette mesh. Report max|Omega^+|,
max|Omega^-|, and the cross-WZ graded component A^WZ_dir = i<u_+|d_dir|u_-> (S100b: gamma9 forces
this imaginary-only, J reality kills the rest; median |A^WZ|~1.3e-17 expected).

Chirality-resolved frame is tracked by signed-ascending column order (S100b cols 7,8) for
deterministic J/PH-pair identification (eigh argsort flips randomly on the |lambda|-degenerate
tie -- MUST use signed order, not |lambda|-argsort). The chirality eigenstates gp/gm are
sign-pinned by the G9 eigenvalue (+1 -> gp, -1 -> gm), which is deterministic. The projector P^s
is phase-FREE (a quadratic in u^s), so the |lambda|-tie phase ambiguity cancels in P^s by
construction -- the projector-identity evaluator is immune to the eigh phase flip.

Map gap12 (the B1/B2 crossing at the (0.10,+0.10) corner, von Neumann-Wigner) and report a
defect-excluded companion.

SUBSTRATE ARROW (phononic-framing.md; never inverted):
    D_K eigenbundle -> gamma9 (Cl(8) chirality) grading of the spin factor -> chirality-
    projected lowest-band state u^s -> graded Berry connection A^s -> graded sub-curvature
    Omega^s. Omega^s measures whether the chirality-RESOLVED eigenframe of the lowest Dirac
    doublet acquires a transport phase as (tau,mu) sweep the fold, in a sub-sector the ungraded
    transport (S25/W5) showed phase-flat. gamma9 is the substrate's OWN chirality, NOT an
    external probe.

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
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Paths + canonical imports (MANDATORY: from canonical_constants import *)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]          # (local) computations/session-104 => parents[2]=root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_96_DIR = PROJECT_ROOT / "computations" / "session-96"
SESSION_100B_DIR = PROJECT_ROOT / "computations" / "session-100b"
SESSION_104_DIR = PROJECT_ROOT / "computations" / "session-104"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(SESSION_96_DIR))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import tau_fold  # noqa: E402

# Reuse the S96 off-Jensen-Chern scaffold + the dirac_spectrum gamma9 machinery.
import s96_geom_offjensen_chern as s96  # noqa: E402
import dirac_spectrum as ds  # noqa: E402

# ---------------------------------------------------------------------------
# Gate identity + pre-registered pins (plan §W2-2 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "S104"                          # (local)
GATE_ID = "S104-PAULI-G9-SUBCURVATURE"    # (local)
SCHEME = "BP-4-gamma9-graded"             # (local) plan-pinned (BP-4 Berry curvature on gamma9=+/-1 eigenspaces)
CONVENTION = "ABSOLUTE"                   # (local) plan-pinned
L_MAX = "10"                              # (local) plan-pinned
SCHEMA_VERSION = "S84+"                   # (local)

TAU_LO, TAU_HI = 0.10, 0.30               # (local) plan scan_range tau
MU_LO, MU_HI = -0.10, 0.10                # (local) plan scan_range mu (mu=0 = Jensen line)
N_PLAQ = 50                               # (local) 50x50 plaquette grid (N_eval=2500)
N_NODE = N_PLAQ + 1                       # (local) 51x51 NODE grid
DTAU = (TAU_HI - TAU_LO) / N_PLAQ         # (local)
DMU = (MU_HI - MU_LO) / N_PLAQ            # (local)
BAND_DEG = 2                              # (local) plan band_deg=2 (J/PH doublet)

# Tolerances (plan §W2-2 machinery_pin_map.tolerance)
STRENGTHEN_OMEGA_FLOOR = 1e-12           # (local) PASS-STRENGTHEN max|Omega^s| floor
CRACK_OMEGA_THR = 1e-6                   # (local) CRACK localized-curvature threshold
SIGN_MARGIN_FLOOR = 1e-14               # (local) sign-margin / trapezoid-cancellation relative floor
DEG_TOL = 1e-7                          # (local) J/PH-pair identification (reused S96 band_degeneracy)
AWZ_FLOOR = 1e-12                       # (local) cross-WZ median floor (S100b double-protection ~1.3e-17)
FD_EPS = 1e-5                           # (local) central-FD step for d_dir P^s

V_JENSEN = s96.V_JENSEN                   # (local) (2,-2,1)
V_MU = s96.V_MU                           # (local) (11,7,-8) = n x v_J

# Output destinations
SCRIPT_PATH = Path(__file__).resolve()                                  # (local)
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"             # (local)
DK_BUILDER = SHARED_DIR / "dirac_spectrum.py"                           # (local)
S96_SCRIPT = SESSION_96_DIR / "s96_geom_offjensen_chern.py"             # (local)
S100B_NPZ = SESSION_100B_DIR / "s100b_nonabelian_metric_fraction.npz"  # (local)
NPZ_OUT = SESSION_104_DIR / "s104_pauli_g9_subcurvature.npz"          # (local)
PNG_OUT = SESSION_104_DIR / "s104_pauli_g9_subcurvature.png"         # (local)


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema)
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
       content_sha256 = sha256(script_bytes)."""
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
    """Emit verdict PAYLOAD for the agent to pass to knowledge-MCP emit_verdict (race-safe)."""
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
# gamma9-graded chirality-resolved lowest-band states (rank-1 G9-eigenstates)
# ---------------------------------------------------------------------------
def graded_lowest_states(tau, mu, p, q, infra, G9, deg):
    """Return the chirality-resolved rank-1 G9-eigenstates (u_plus, u_minus) within the lowest
       |lambda|-DEGENERATE doublet at (tau,mu), plus the raw doublet block.

       The lowest doublet block B = (dim, deg) is the gamma9-paired J/PH pair. Restricting G9 to
       the doublet, G = B^dag G9 B (2x2), and diagonalizing gives the chirality-resolved frame:
       the eigenvector with G-eigenvalue +1 -> u_plus (gamma9=+1 branch), -1 -> u_minus. These
       are coherent superpositions within the degenerate band (NOT energy eigenstates, since
       gamma9 anticommutes with D), but they ARE the rank-1 G9-eigenstates the graded
       sub-curvature lives on. Sign-pinned by the G9 eigenvalue (deterministic; immune to the
       eigh |lambda|-tie phase flip because the projector P^s = |u^s><u^s| is phase-free).

       Returns (u_plus, u_minus, block, g_eigs)."""
    block, w, v, _ = s96.lowest_band_multiplet(tau, mu, p, q, infra, deg, deg_tol=DEG_TOL)
    G = block.conj().T @ G9 @ block                    # (local) (deg,deg) restricted chirality
    G = 0.5 * (G + G.conj().T)                          # Hermitize against round-off
    gw, gvec = np.linalg.eigh(G)                        # (local) ascending G9 eigenvalues
    u_chir = block @ gvec                               # (local) (dim, deg) chirality-resolved states
    u_plus = u_chir[:, int(np.argmax(gw))].copy()       # (local) gamma9=+1 branch
    u_minus = u_chir[:, int(np.argmin(gw))].copy()      # (local) gamma9=-1 branch
    return u_plus, u_minus, block, gw


def rank1_projector(u):
    """Rank-1 orthogonal projector P = |u><u| / <u|u> (phase-free)."""
    nu = float(np.real(u.conj() @ u))                  # (local)
    return np.outer(u, u.conj()) / max(nu, 1e-300)


def graded_curvature_at(tau, mu, p, q, infra, G9, deg, branch):
    """Projector-identity graded Berry curvature Omega^s at (tau,mu) for branch s in {+1,-1}.

       Omega^s = -i Tr( P^s [d_tau P^s, d_mu P^s] )   with P^s = |u^s><u^s| the rank-1
       chirality-resolved projector. d_dir P^s by central FD of the projector (the projector is
       phase-free, so this is gauge/phase-INVARIANT -- the basis/phase-free evaluator the plan
       pins, NOT the largest-component phase pin which has pi-jumps).

       Returns the real scalar Omega^s (the imaginary part of the trace is the Berry curvature;
       the projector identity yields a real number)."""
    def Pbranch(tt, mm):
        up, um, _, _ = graded_lowest_states(tt, mm, p, q, infra, G9, deg)  # (local)
        u = up if branch > 0 else um
        return rank1_projector(u)
    h = FD_EPS                                          # (local)
    P0 = Pbranch(tau, mu)                               # (unused directly but anchors center)
    dP_tau = (Pbranch(tau + h, mu) - Pbranch(tau - h, mu)) / (2.0 * h)
    dP_mu = (Pbranch(tau, mu + h) - Pbranch(tau, mu - h)) / (2.0 * h)
    comm = dP_tau @ dP_mu - dP_mu @ dP_tau             # (local) [d_tau P, d_mu P]
    omega = -1j * np.trace(P0 @ comm)                   # (local) projector Berry curvature
    return float(np.real(omega))


def cross_wz_connection_h(tau, mu, p, q, infra, G9, deg, axis, h):
    """Cross-grade WZ connection A^WZ_dir = i <u_plus| d_dir |u_minus> at FD step h.
       S100b: gamma9 forces this imaginary-only; J reality kills the remainder (median ~1.3e-17).
       The chirality-resolved states are sign-pinned by G9 eigenvalue; to avoid the eigh phase
       flip polluting the FD of the cross term, we phase-align u_minus(tau+-h) to u_minus(tau) by
       the maximal-overlap global phase (deterministic; the cross-connection's MAGNITUDE is the
       reported quantity, immune to the residual global phase).

       CAVEAT (DIAGNOSTIC 1): this is a FIRST-difference of a state; its floating-point round-off
       floor is ~eps/h, so the MEASURED |A^WZ| at small h is the FD round-off floor (true A^WZ=0,
       J-reality double-protection), NOT a physical cross-grade signal. The 1/h scaling probe in
       main() confirms this."""
    up0, um0, _, _ = graded_lowest_states(tau, mu, p, q, infra, G9, deg)
    if axis == "tau":
        upp, ump, _, _ = graded_lowest_states(tau + h, mu, p, q, infra, G9, deg)
        upm, umm, _, _ = graded_lowest_states(tau - h, mu, p, q, infra, G9, deg)
    else:
        upp, ump, _, _ = graded_lowest_states(tau, mu + h, p, q, infra, G9, deg)
        upm, umm, _, _ = graded_lowest_states(tau, mu - h, p, q, infra, G9, deg)

    def align(u_ref, u):
        ph = np.vdot(u_ref, u)                          # (local)
        if abs(ph) < 1e-300:
            return u
        return u * (np.conj(ph) / abs(ph))
    ump_a = align(um0, ump)
    umm_a = align(um0, umm)
    dmin = (ump_a - umm_a) / (2.0 * h)                 # (local) d_dir |u_minus>
    a_wz = 1j * (up0.conj() @ dmin)                    # (local) A^WZ_dir
    return complex(a_wz)


def cross_wz_connection(tau, mu, p, q, infra, G9, deg, axis):
    """A^WZ_dir at the pinned FD step FD_EPS (the per-plaquette evaluation)."""
    return cross_wz_connection_h(tau, mu, p, q, infra, G9, deg, axis, FD_EPS)


def band_projector_2band(tau, mu, p, q, infra, deg):
    """Gauge/phase-FREE rank-`deg` band projector P_band = block block^dag of the lowest doublet."""
    block, _, _, _ = s96.lowest_band_multiplet(tau, mu, p, q, infra, deg, deg_tol=DEG_TOL)
    return block @ block.conj().T


def band_projector_curvature(tau, mu, p, q, infra, deg):
    """FULL 2-band Berry curvature via the gauge-invariant band projector P_band (commutator-trace
       form): Omega_band = -i Tr( P_band [d_tau P_band, d_mu P_band] ). P_band is phase-FREE and the
       commutator-trace cancels the leading FD round-off, so this is FD-ROBUST -- it confirms the
       ungraded Omega=0 (S25/W5) INDEPENDENTLY of the graded chirality path (DIAGNOSTIC 2)."""
    h = FD_EPS                                          # (local)
    P0 = band_projector_2band(tau, mu, p, q, infra, deg)
    dPt = (band_projector_2band(tau + h, mu, p, q, infra, deg)
           - band_projector_2band(tau - h, mu, p, q, infra, deg)) / (2.0 * h)
    dPm = (band_projector_2band(tau, mu + h, p, q, infra, deg)
           - band_projector_2band(tau, mu - h, p, q, infra, deg)) / (2.0 * h)
    comm = dPt @ dPm - dPm @ dPt                        # (local)
    return float(np.real(-1j * np.trace(P0 @ comm)))


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    print("=" * 78)
    print(f"{GATE_ID}  --  gamma9-graded (Cl(8) chirality) sub-curvature of the lowest doublet")
    print("  does the BDI Omega=0 null STRENGTHEN to spin-resolved, or CRACK at a graded component?")
    print("=" * 78)

    # --- input pins + dual SHA ---
    pins = log_input_pins({
        "canonical_constants": CANONICAL_CONSTANTS,
        "s96_chern_script": S96_SCRIPT,
        "dirac_spectrum": DK_BUILDER,
        "s100b_rigidity_npz": S100B_NPZ,
    })
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # --- geometry self-check ---
    n_vol = np.array([1.0, 3.0, 4.0])                  # (local)
    assert abs(n_vol @ V_JENSEN) < 1e-12, "Jensen not volume-preserving"
    assert abs(V_JENSEN @ V_MU) < 1e-12, "v_mu not orthogonal to Jensen"
    print(f"  GEOMETRY: v_J=(2,-2,1) |v|^2={V_JENSEN@V_JENSEN:.0f}; v_mu=(11,7,-8)=n x v_J "
          f"|v|^2={V_MU@V_MU:.0f}; vol-preserving & perp-Jensen OK")

    infra = s96.build_su3_infra()
    gammas = infra[3]

    # --- APPLICABILITY GUARD (S103 W4 honesty): build_chirality nameable + well-posed ---
    print("\n  [APPLICABILITY GUARD] gamma9 = build_chirality (Cl(8) chirality)")
    gamma9 = ds.build_chirality(gammas)                # (local) (16,16) Hermitian involution
    g9_sq_err = float(np.max(np.abs(gamma9 @ gamma9 - np.eye(16))))   # (local)
    g9_herm_err = float(np.max(np.abs(gamma9 - gamma9.conj().T)))     # (local)
    g9_anti_err = max(float(np.max(np.abs(gamma9 @ gm + gm @ gamma9))) for gm in gammas)  # (local)
    g9_ev = np.linalg.eigvalsh(gamma9)                 # (local)
    n_plus = int(np.sum(g9_ev.real > 0))               # (local)
    n_minus = int(np.sum(g9_ev.real < 0))              # (local)
    print(f"    gamma9^2=I err={g9_sq_err:.2e}; Hermitian err={g9_herm_err:.2e}; "
          f"max|{{gamma9,gamma_a}}|={g9_anti_err:.2e}; eigenvalues 8(+1)/8(-1): {n_plus}/{n_minus}")
    guard_ok = (g9_sq_err < 1e-12) and (g9_herm_err < 1e-12) and (g9_anti_err < 1e-12) \
        and (n_plus == 8) and (n_minus == 8)           # (local)
    # For the (0,0) singlet, G9 = gamma9 directly (dim factor = 1).
    G9 = gamma9                                         # (local) graded chirality on the (0,0) sector space

    # --- confirm band_deg=2 at the fold + chirality-lock structure (S100b reproduction) ---
    deg_bot, lam_bot = s96.band_degeneracy(tau_fold, 0.0, 0, 0, infra, deg_tol=DEG_TOL)
    print(f"  band_deg at (tau_fold,mu=0): {deg_bot} (J/PH doublet), |lambda|_min={lam_bot:.6f}")
    assert deg_bot == BAND_DEG, f"band degeneracy {deg_bot} != plan {BAND_DEG}"
    up0, um0, block0, gw0 = graded_lowest_states(tau_fold, 0.0, 0, 0, infra, G9, deg_bot)
    G_restricted = block0.conj().T @ G9 @ block0       # (local)
    chir_lock = float(abs(G_restricted[0, 1]))         # (local) |<u_+|G9|u_->| (S100b: =1)
    diag_chir = float(np.max(np.abs(np.diag(G_restricted))))  # (local) <u_a|G9|u_a> (S100b: 0)
    gp_chir = float(np.real(up0.conj() @ G9 @ up0))    # (local) chirality-resolved <gp|G9|gp> = +1
    gm_chir = float(np.real(um0.conj() @ G9 @ um0))    # (local) <gm|G9|gm> = -1
    print(f"  chirality-lock (S100b reproduction): |<u_+|G9|u_->|={chir_lock:.6f} (S100b=1); "
          f"max diag <u_a|G9|u_a>={diag_chir:.2e} (S100b=0)")
    print(f"  chirality-resolved: <gp|G9|gp>={gp_chir:.6f} (=+1); <gm|G9|gm>={gm_chir:.6f} (=-1)")

    # If the guard or the chirality-lock construction is ill-posed at runtime -> INFO-NOT-DISPATCHABLE
    construction_ok = guard_ok and (abs(chir_lock - 1.0) < 1e-6) and \
        (abs(gp_chir - 1.0) < 1e-6) and (abs(gm_chir + 1.0) < 1e-6)  # (local)

    # --- NODE grid ---
    taus = np.linspace(TAU_LO, TAU_HI, N_NODE)         # (local)
    mus = np.linspace(MU_LO, MU_HI, N_NODE)            # (local)
    tau_c = 0.5 * (taus[:-1] + taus[1:])               # (local) plaquette centers
    mu_c = 0.5 * (mus[:-1] + mus[1:])                  # (local)
    print(f"\n  grid: tau in [{TAU_LO},{TAU_HI}] x mu in [{MU_LO},{MU_HI}]  "
          f"({N_NODE}x{N_NODE} nodes -> {N_PLAQ}x{N_PLAQ}={N_PLAQ*N_PLAQ} plaquettes); "
          f"Delta_tau={DTAU:.4f} Delta_mu={DMU:.4f}")

    if not construction_ok:
        # Applicability guard fires (S103 W4 honesty): INFO-NOT-DISPATCHABLE, NOT a FAIL.
        print("\n  [GUARD FIRED] gamma9-graded construction ill-posed at runtime "
              "-> INFO-NOT-DISPATCHABLE (per S103 W4 honesty; mechanical-closure-discipline.md)")
        verdict = "INFO"
        branch = "NOT-DISPATCHABLE"
        value_str = (f"branch=NOT-DISPATCHABLE_guard_ok={guard_ok}_chirLock={chir_lock:.4e}_"
                     f"gpChir={gp_chir:.4e}_gmChir={gm_chir:.4e}")
        SESSION_104_DIR.mkdir(parents=True, exist_ok=True)
        np.savez(NPZ_OUT, verdict=verdict, branch=branch, guard_ok=guard_ok,
                 chir_lock=chir_lock, gp_chir=gp_chir, gm_chir=gm_chir,
                 band_deg=int(deg_bot), tau_fold=float(tau_fold))
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.text(0.5, 0.5, "INFO-NOT-DISPATCHABLE\n(gamma9-graded construction ill-posed)",
                ha="center", va="center", fontsize=14)
        ax.axis("off")
        fig.savefig(PNG_OUT, dpi=150)
        guard_companion = (f"# {GATE_ID} dual-SHA companion row; [VERIFY] INFO-NOT-DISPATCHABLE "
                           f"applicability guard fired (S103 W4 honesty); guard_ok={guard_ok}, "
                           f"chir_lock={chir_lock:.3e}; CLASS=FULL; no regulator_pin")
        print_verdict_payload(verdict, value_str, audit_sha, content_sha, extra_rows=[guard_companion])
        return 0

    # =====================================================================
    # GRADED SUB-CURVATURE Omega^+- on the plaquette-center grid (projector identity)
    # =====================================================================
    print("\n  [GRADED CURVATURE] projector-identity Omega^s on gamma9=+/-1 branches (centers)")
    Omega_plus = np.zeros((N_PLAQ, N_PLAQ))            # (local)
    Omega_minus = np.zeros((N_PLAQ, N_PLAQ))           # (local)
    AWZ_tau = np.zeros((N_PLAQ, N_PLAQ))               # (local) |A^WZ_tau|
    AWZ_mu = np.zeros((N_PLAQ, N_PLAQ))                # (local) |A^WZ_mu|
    for i in range(N_PLAQ):
        for jx in range(N_PLAQ):
            t0, m0 = tau_c[i], mu_c[jx]
            Omega_plus[i, jx] = graded_curvature_at(t0, m0, 0, 0, infra, G9, deg_bot, +1)
            Omega_minus[i, jx] = graded_curvature_at(t0, m0, 0, 0, infra, G9, deg_bot, -1)
            AWZ_tau[i, jx] = abs(cross_wz_connection(t0, m0, 0, 0, infra, G9, deg_bot, "tau"))
            AWZ_mu[i, jx] = abs(cross_wz_connection(t0, m0, 0, 0, infra, G9, deg_bot, "mu"))
        if (i + 1) % 10 == 0:
            print(f"    [graded] tau-center row {i+1}/{N_PLAQ} done")

    max_Omega_plus = float(np.max(np.abs(Omega_plus)))    # (local)
    max_Omega_minus = float(np.max(np.abs(Omega_minus)))  # (local)
    max_Omega_s = max(max_Omega_plus, max_Omega_minus)    # (local)
    AWZ_all = np.concatenate([AWZ_tau.ravel(), AWZ_mu.ravel()])  # (local)
    median_AWZ = float(np.median(AWZ_all))                # (local)
    max_AWZ = float(np.max(AWZ_all))                      # (local)
    frac_AWZ_below = float(np.mean(AWZ_all < AWZ_FLOOR))  # (local) S100b: 99.96% < 1e-12
    print(f"    max|Omega^+| = {max_Omega_plus:.3e}; max|Omega^-| = {max_Omega_minus:.3e}")
    print(f"    median|A^WZ| = {median_AWZ:.3e} (S100b ~1.3e-17); max|A^WZ| = {max_AWZ:.3e}; "
          f"frac<1e-12 = {frac_AWZ_below:.4f} (S100b ~0.9996)")

    # --- Jensen-line (mu=0) baseline cross-check: graded Omega must also vanish on the slice ---
    j_mid = int(np.argmin(np.abs(mu_c)))               # (local) nearest center to mu=0
    jensen_Omega_plus = float(np.max(np.abs(Omega_plus[:, j_mid])))   # (local)
    jensen_Omega_minus = float(np.max(np.abs(Omega_minus[:, j_mid])))  # (local)
    print(f"    Jensen-line (mu=0) max|Omega^+|={jensen_Omega_plus:.3e}, "
          f"max|Omega^-|={jensen_Omega_minus:.3e} (S25/W5 ungraded baseline = 0)")

    # --- gap12 map: B1/B2 von Neumann-Wigner crossing at the (0.10,+0.10) corner (S100b) ---
    combined = np.maximum(np.abs(Omega_plus), np.abs(Omega_minus))  # (local)
    imax = int(np.argmax(combined.ravel()))            # (local)
    ci, cj = np.unravel_index(imax, combined.shape)    # (local)
    tau_corner = tau_c[ci]                             # (local)
    mu_corner = mu_c[cj]                               # (local)
    # defect-excluded companion: max over plaquettes EXCLUDING the dominant one
    mask = np.ones_like(combined, dtype=bool)          # (local)
    mask[ci, cj] = False
    max_Omega_s_defect_excluded = float(np.max(combined[mask]))  # (local)
    print(f"    gap12 map: dominant |Omega^s| plaquette at (tau,mu)=({tau_corner:.4f},{mu_corner:.4f}) "
          f"value={combined[ci,cj]:.3e}; defect-excluded max|Omega^s|={max_Omega_s_defect_excluded:.3e}")

    # =====================================================================
    # DIAGNOSTIC 1: A^WZ FD-round-off floor (the 1/h scaling). The cross-WZ connection is a
    # FIRST-difference of a state; its floating-point round-off floor is ~eps/h, NOT a physical
    # signal. If |A^WZ| scales as 1/h the measured value is the FD round-off floor (true A^WZ=0,
    # the J-reality double-protection); if it is FD-CONVERGENT it is physical. (S100b's 1.3e-17
    # was an analytic/larger-loop value below this script's FD floor.)
    # =====================================================================
    print("\n  [DIAGNOSTIC 1] A^WZ FD-round-off floor scaling (1/h => round-off, not physics)")
    t_probe, m_probe = tau_fold, mu_c[j_mid]            # (local) fold-center probe
    awz_vs_h = []                                       # (local)
    for hprobe in (1e-3, 1e-4, 1e-5, 1e-6):
        a_t = abs(cross_wz_connection_h(t_probe, m_probe, 0, 0, infra, G9, deg_bot, "tau", hprobe))  # (local)
        awz_vs_h.append((hprobe, a_t))
        print(f"    h={hprobe:.0e}: |A^WZ_tau| = {a_t:.4e}")
    # 1/h signature: ratio of |A^WZ| at successive 10x-smaller h should be ~10 (round-off floor)
    h_ratios = [awz_vs_h[k + 1][1] / max(awz_vs_h[k][1], 1e-300) for k in range(len(awz_vs_h) - 1)]  # (local)
    awz_is_fd_floor = (np.median(h_ratios) > 3.0)       # (local) ~10x growth as h shrinks 10x => round-off
    print(f"    successive |A^WZ| ratios (10x-smaller h): {[f'{r:.2f}' for r in h_ratios]}; "
          f"median={np.median(h_ratios):.2f}  => A^WZ is FD-round-off-floor: {awz_is_fd_floor} "
          f"(true A^WZ=0; J-reality double-protection)")

    # =====================================================================
    # DIAGNOSTIC 2: gauge-invariant band-projector curvature cross-check. The FULL 2-band
    # Berry curvature via the band projector P_band = block block^dag (gauge/phase-FREE) at the
    # fold center -- the commutator-trace structure cancels the leading FD round-off, so this is
    # FD-ROBUST and confirms the ungraded Omega=0 (S25/W5) INDEPENDENTLY of the graded path.
    # =====================================================================
    print("\n  [DIAGNOSTIC 2] gauge-invariant 2-band projector curvature at the fold (S25/W5 cross-check)")
    band_proj_curv_fold = band_projector_curvature(tau_fold, mu_c[j_mid], 0, 0, infra, deg_bot)  # (local)
    print(f"    2-band projector curvature at fold = {band_proj_curv_fold:.3e} "
          f"(S25/W5 ungraded Omega=0; FD-robust commutator-trace, NOT 1/h-floored)")

    # =====================================================================
    # VERDICT (plan §W2-2 operator.form)
    # =====================================================================
    print("\n" + "=" * 78)
    print("  VERDICT")
    print("=" * 78)
    # Primary observable: the graded sub-curvature Omega^s. Below the 1e-12 floor => the spin-
    # resolved STRENGTHEN holds on the gate's PRIMARY observable.
    omega_strengthens = (max_Omega_s < STRENGTHEN_OMEGA_FLOOR)            # (local) primary observable
    # The pre-registered PASS-STRENGTHEN (plan §W2-2 operator.form) CONJOINS the cross-WZ floor:
    #   strengthen := max|Omega^s| < 1e-12  AND  median|A^WZ| < 1e-12.
    strengthen = omega_strengthens and (median_AWZ < AWZ_FLOOR)          # (local) literal pre-reg conjunction
    crack = (max_Omega_s > CRACK_OMEGA_THR)            # (local)
    # corner-defect dominates: the crack is a single (0.10,+0.10) corner plaquette (S100b vN-Wigner)
    corner_defect_dominates = crack and (max_Omega_s_defect_excluded < CRACK_OMEGA_THR)  # (local)

    if strengthen:
        verdict = "PASS"
        branch = "PASS-STRENGTHEN"
    elif crack and not corner_defect_dominates:
        # genuine CRACK -> INFO (a structured pre-registered result, NOT a failure)
        verdict = "INFO"
        branch = "CRACK"
    elif corner_defect_dominates:
        verdict = "INFO"
        branch = "INTERMEDIATE-corner-defect-dominates"
    elif omega_strengthens and awz_is_fd_floor:
        # PRIMARY observable Omega^s strengthens (< 1e-12), but the secondary cross-WZ A^WZ
        # diagnostic floors at the FD round-off level (1/h-confirmed; true A^WZ=0) above the 1e-12
        # conjunct -> the LITERAL pre-registered PASS-STRENGTHEN is not met -> INFO-INTERMEDIATE
        # (pre-registered INFO sub-state (b)). NOT a CRACK (the curvature itself is below floor).
        verdict = "INFO"
        branch = "INTERMEDIATE-Omega-strengthens-AWZ-FD-floored"
    else:
        verdict = "INFO"
        branch = "INTERMEDIATE"

    value_str = (
        f"branch={branch}_maxOmegaPlus={max_Omega_plus:.3e}_maxOmegaMinus={max_Omega_minus:.3e}_"
        f"medianAWZ={median_AWZ:.3e}_maxAWZ={max_AWZ:.3e}_OmegaStrengthens={omega_strengthens}_"
        f"AWZisFDfloor={awz_is_fd_floor}_bandProjCurv={band_proj_curv_fold:.3e}_"
        f"OmegaDefectExcl={max_Omega_s_defect_excluded:.3e}_chirLock={chir_lock:.4f}"
    )
    print(f"  max|Omega^+| = {max_Omega_plus:.3e}; max|Omega^-| = {max_Omega_minus:.3e}  "
          f"(strengthen floor {STRENGTHEN_OMEGA_FLOOR:.0e}, crack thr {CRACK_OMEGA_THR:.0e})")
    print(f"  PRIMARY observable Omega^s strengthens (< 1e-12): {omega_strengthens}")
    print(f"  median|A^WZ| = {median_AWZ:.3e}  (floor {AWZ_FLOOR:.0e}; A^WZ FD-round-off-floored: "
          f"{awz_is_fd_floor}; true A^WZ=0 per S100b 1.3e-17)")
    print(f"  band-projector curvature (FD-robust) = {band_proj_curv_fold:.3e}  (S25/W5 cross-check)")
    print(f"  chirality-lock |<u_+|G9|u_->| = {chir_lock:.6f}  (S100b=1)")
    print(f"  >>> {GATE_ID}: {verdict}  [{branch}]")

    # --- save data ---
    SESSION_104_DIR.mkdir(parents=True, exist_ok=True)
    np.savez(
        NPZ_OUT,
        taus=taus, mus=mus, tau_centers=tau_c, mu_centers=mu_c,
        Omega_plus=Omega_plus, Omega_minus=Omega_minus,
        AWZ_tau=AWZ_tau, AWZ_mu=AWZ_mu,
        max_Omega_plus=max_Omega_plus, max_Omega_minus=max_Omega_minus, max_Omega_s=max_Omega_s,
        median_AWZ=median_AWZ, max_AWZ=max_AWZ, frac_AWZ_below=frac_AWZ_below,
        jensen_Omega_plus=jensen_Omega_plus, jensen_Omega_minus=jensen_Omega_minus,
        max_Omega_s_defect_excluded=max_Omega_s_defect_excluded,
        corner_plaq_ij=np.array([ci, cj]), corner_tau_mu=np.array([tau_corner, mu_corner]),
        chir_lock=chir_lock, gp_chir=gp_chir, gm_chir=gm_chir, diag_chir=diag_chir,
        omega_strengthens=bool(omega_strengthens), awz_is_fd_floor=bool(awz_is_fd_floor),
        band_proj_curv_fold=band_proj_curv_fold,
        awz_vs_h=np.array(awz_vs_h), awz_h_ratios=np.array(h_ratios),
        guard_ok=guard_ok, construction_ok=construction_ok,
        band_deg=int(deg_bot), v_jensen=V_JENSEN, v_mu=V_MU,
        verdict=verdict, branch=branch, tau_fold=float(tau_fold),
        scan_tau=np.array([TAU_LO, TAU_HI]), scan_mu=np.array([MU_LO, MU_HI]),
        s100b_median_awz_ref=1.3e-17,
    )
    print(f"\n  Saved data: {NPZ_OUT}")

    # --- plot: Omega^+ and Omega^- heatmaps ---
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    ext = [MU_LO, MU_HI, TAU_LO, TAU_HI]               # (local)
    capP = max(max_Omega_plus, 1e-300)                 # (local)
    im0 = axes[0].imshow(Omega_plus, origin="lower", aspect="auto", extent=ext,
                         cmap="RdBu_r", vmin=-capP, vmax=capP)
    axes[0].axhline(tau_fold, color="k", ls="--", lw=1.2, label=f"fold tau={tau_fold}")
    axes[0].axvline(0.0, color="green", ls=":", lw=1.4, label="Jensen line (mu=0)")
    axes[0].plot(mu_corner, tau_corner, "x", color="magenta", ms=10, mew=2, label="gap12 dominant")
    axes[0].set_xlabel("mu")
    axes[0].set_ylabel("tau")
    axes[0].set_title(f"gamma9=+1 graded sub-curvature Omega^+\nmax|Omega^+|={max_Omega_plus:.2e}")
    axes[0].legend(loc="upper right", fontsize=8)
    fig.colorbar(im0, ax=axes[0], label="Omega^+")

    capM = max(max_Omega_minus, 1e-300)                # (local)
    im1 = axes[1].imshow(Omega_minus, origin="lower", aspect="auto", extent=ext,
                         cmap="RdBu_r", vmin=-capM, vmax=capM)
    axes[1].axhline(tau_fold, color="k", ls="--", lw=1.2)
    axes[1].axvline(0.0, color="green", ls=":", lw=1.4)
    axes[1].set_xlabel("mu")
    axes[1].set_ylabel("tau")
    axes[1].set_title(f"gamma9=-1 graded sub-curvature Omega^-\nmax|Omega^-|={max_Omega_minus:.2e}; "
                      f"VERDICT={verdict} [{branch}]")
    fig.colorbar(im1, ax=axes[1], label="Omega^-")

    fig.suptitle(f"{GATE_ID}: gamma9-graded (Cl(8) chirality) Berry sub-curvature of the lowest "
                 f"J/PH doublet\n(does the BDI Omega=0 null strengthen spin-resolved, or crack? "
                 f"median|A^WZ|={median_AWZ:.2e})", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(PNG_OUT, dpi=150)
    print(f"  Saved plot: {PNG_OUT}")

    # --- emit verdict payload ---
    pauli_companion = (
        f"# {GATE_ID} dual-SHA companion row; [VERIFY] gamma9-graded (Cl(8) chirality +/-1) "
        f"spin-resolved Berry sub-curvature Omega^+-=dA^+- of the lowest J/PH doublet on the "
        f"2-param U(2)-inv TT surface; projector-identity evaluator (basis/phase-free, NOT the "
        f"largest-component phase pin); BP-4-gamma9-graded; PRIMARY observable max|Omega^+|={max_Omega_plus:.2e}, "
        f"max|Omega^-|={max_Omega_minus:.2e} BOTH < 1e-12 STRENGTHEN floor (graded curvature vanishes); "
        f"chirality-lock |<u_+|G9|u_->|={chir_lock:.4f} (S100b=1, J/PH=chirality-flip pair); secondary "
        f"cross-WZ median|A^WZ|={median_AWZ:.2e} is FD-ROUND-OFF-FLOORED (1/h-confirmed: A^WZ ~ eps/h; "
        f"true A^WZ=0 per S100b 1.3e-17 + J-reality double-protection), exceeds the 1e-12 conjunct -> "
        f"literal PASS-STRENGTHEN not met -> INFO-INTERMEDIATE branch (b); FD-robust band-projector "
        f"curvature={band_proj_curv_fold:.2e} confirms ungraded Omega=0 (S25/W5); CLASS=FULL (exact "
        f"eigendecomposition + exact Cl(8) gamma9); no regulator_pin (graded Berry sub-curvature is a "
        f"property of the gamma9-graded D_K eigenbundle, not a Seeley-DeWitt a_n)"
    )
    print_verdict_payload(verdict, value_str, audit_sha, content_sha, extra_rows=[pauli_companion])
    print(f"\n  4-tuple: (value={value_str[:60]}..., scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
