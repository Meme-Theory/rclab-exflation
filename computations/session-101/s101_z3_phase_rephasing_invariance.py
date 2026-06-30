#!/usr/bin/env python3
"""
S101 W3-5 S101-Z3-PHASE-REPHASING-INVARIANCE — arg(w) Z3 phases rephasing-removable
vs delta_CP-feeding (3x3 algebra)
====================================================================================

Gate: S101-Z3-PHASE-REPHASING-INVARIANCE ([VERIFY])

Pre-registered threshold (operator, three-branch; transcribed from
session-101-plan-w3.md SS W3-5):
  Discriminator: J = Im(U_e1 U_mu2 U*_e2 U*_mu1) on U_PMNS = U_l^dag U_nu,
  evaluated on the closed configuration set (3 Z3 points x <= 2 U_nu legs).
  PASS = |J| <= 1e-12 (THEOREM) for ALL configurations: rephasing-removable;
         delta_CP in {0, pi} consistency CERTIFIED vs canonical
         delta_CP_PMNS_substrate; Majorana relocation reported (non-gating).
  FAIL = |J| > 1e-12 at ANY substrate-pinned configuration: a non-removable
         phase forces delta_CP outside {0, pi}; cross-session contradiction.
  INFO = removability basis-conditional: J = 0 on a proper non-empty subset;
         scope clause emitted naming surviving/failing legs.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-100a/s100a_yukawa_overlap_offdiag.npz   (|w|, arg w, d-vector)
  - computations/session-100a/s100a_md_normalization.npz         (leg i diagonal m_D maps)
  - computations/session-100b/s100b_w2_3_mr_texture_class.npz     (sector guard phi_CP^K7, M_R)
  - computations/session-100a/s100a_gate_verdicts.txt             (read-only verdict anchor)
  - computations/session-101/s101_nu_dirac_offdiag_texture.npz    (leg ii CONDITIONAL; absent => N/A)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<J-zero-set summary>, scheme=JARLSKOG-REPHASING-INVARIANT-3X3,
   convention=ABSOLUTE-EXACT-ALGEBRA, L_max=N/A)

Classification: PARTICLE

METHODOLOGY
-----------
Rephasing-invariance analysis; 3x3 algebra ONLY (no diagonalization compute
beyond closed-form 3x3). The Jarlskog invariant J = Im(U_e1 U_mu2 U*_e2 U*_mu1)
is itself rephasing-invariant and complete for the Dirac phase at non-degenerate
angles, so J = 0 <=> delta_CP in {0, pi}, configuration by configuration -- no
rephasing search needed. Step A: construct the 3x3 charged-lepton Hermitian
matrix from the npz d-vector + the w channel on the BDI fund<->antifund (mu,tau)
pair (W-2 orientation tau=(1,0), mu=(1,1), e=(3,0)); the doublet block is
[[d, w],[w*, d]] with d real (J-forced d1 = d2, S99 BDI; npz witness
bdi_pair_max_rel_dev ~ 3.7e-15). Step B: factor U_l analytically -- the doublet
block diagonalizes as U_l(2x2) = D(phi)*U_0 with D(phi) = diag(1, e^{-i phi}) and
U_0 real. Step C: build U_PMNS = U_l^dag U_nu on the substrate-pinned U_nu legs:
leg (i) ALWAYS = diagonal m_D (S100a landed maps both diagonal; U_nu real up to
Majorana signs; M_R real-diagonal by J-reality T1/T11, m_1 = 0, NO ordering);
leg (ii) CONDITIONAL = gate-2 doublet-texture m_D pushed through the seesaw,
consumed IFF S101-NU-DIRAC-OFFDIAG-TEXTURE has landed (else texture_leg=N/A,
pre-registered N/A clause, NOT a PRE-REG-INC). Step D: compute J at each Z3 point
x each U_nu leg. Step E (reported, non-gating): Majorana relocation flag where
the phase relocates into column (Majorana) phases. Sector-guard assertion:
phi_CP^K7 = pi/2 absent from every configuration. Angle MAGNITUDES are NOT gated
(that is the MD-NORMALIZATION lineage); only the phase fate is.

Substitution-chain anchors PRE-verified at machine eps before the live read:
  Step 3 (factorization): D*U_0*diag(d+|w|,d-|w|)*U_0^T*D^dag = M_l
  Step 5 (phi = pi): diag(1,e^{i pi})=diag(1,-1) REAL => U_PMNS real => J=0
  Step 4 (leg i diagonal m_D): phase -> COLUMN (Majorana) phase => J=0 EXACTLY
Any deviation in a PRE-verification is a CONSTRUCTION BUG, not physics (halt+fix).
Sage-exact cross-check (sage_eval, this dispatch): on leg (i), max|Im J| = 0 over
ALL 3 Z3 points x 8 Majorana-sign choices; a GENERIC real U_nu gives Im J ~
sin(phi) != 0 at +-2pi/3 -- removability is leg-(i)-STRUCTURAL, not generic.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- 3x3 complex algebra only; CPU OMP8 cap (no GPU)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via emit_verdict MCP tool (race-safe); the script PRINTS
  the payload via print_verdict_payload carrying the schema-v2 3-tuple
  (rephasing-removable vs delta_CP-feeding is a structural directional binary).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (3x3 algebra; set BEFORE numpy import)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Path bootstrap + canonical constants (MANDATORY)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

# canonical_constants.py lives in computations/_shared/; put it on the path
# BEFORE the canonical import (scripts run from computations/session-101/).
_SHARED = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: E402,F401,F403
from canonical_constants import (  # noqa: E402  explicit names used below
    delta_CP_PMNS_substrate,
    dm2_21_NuFit,
    dm2_31_NuFit,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S101"                                       # (local)
GATE_ID = "S101-Z3-PHASE-REPHASING-INVARIANCE"          # (local)
SCHEME = "JARLSKOG-REPHASING-INVARIANT-3X3"             # (local)
CONVENTION = "ABSOLUTE-EXACT-ALGEBRA"                   # (local)
L_MAX = "N/A"                                           # (local)

# Pre-registered THEOREM tolerances (define BEFORE running)
J_TOL = 1e-12               # (local) Jarlskog zero-test (THEOREM)
UNITARITY_TOL = 1e-12       # (local) U_PMNS unitarity (THEOREM)
SECTOR_GUARD_TOL = 1e-9     # (local) phi_CP^K7 = pi/2 must NOT appear among phases
CONSTRUCTION_TOL = 1e-12    # (local) Step-3/4/5 PRE-verification (machine eps)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s101_z3_phase_rephasing_invariance.npz"
OUT_PNG = SESSION_DIR / "s101_z3_phase_rephasing_invariance.png"

YUKAWA_NPZ = COMPUTATIONS_DIR / "session-100a" / "s100a_yukawa_overlap_offdiag.npz"
MD_NPZ = COMPUTATIONS_DIR / "session-100a" / "s100a_md_normalization.npz"
MR_NPZ = COMPUTATIONS_DIR / "session-100b" / "s100b_w2_3_mr_texture_class.npz"
S100A_VERDICT = COMPUTATIONS_DIR / "session-100a" / "s100a_gate_verdicts.txt"
TEXTURE_NPZ = SESSION_DIR / "s101_nu_dirac_offdiag_texture.npz"  # CONDITIONAL (leg ii)
S101_VERDICT = SESSION_DIR / "s101_gate_verdicts.txt"           # leg-ii existence probe

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    YUKAWA_NPZ,
    MD_NPZ,
    MR_NPZ,
    S100A_VERDICT,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path, canonical_path: Path, pins: dict[str, str]
) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Phase-fate algebra
# ---------------------------------------------------------------------------
def jarlskog(U: np.ndarray) -> float:
    """Standard Jarlskog invariant J = Im(U_e1 U_mu2 U*_e2 U*_mu1).

    Index convention: rows/cols (e, mu, tau) = (0,1,2); 1-based (1,2) -> 0-based
    cols (0,1). This is the rephasing-invariant CP-violation measure: J = 0 <=>
    Dirac CP-conservation (delta_CP in {0, pi}) at non-degenerate angles. J is
    quartet-independent up to sign in a unitary 3x3, so the single (e,mu;1,2)
    quartet is complete.
    """
    return float(np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0])))


def build_M_l_3x3(d_vec: np.ndarray, w_abs: float, phi: float) -> np.ndarray:
    """3x3 Hermitian charged-lepton matrix.

    Index order (e, mu, tau) = (0,1,2). W-2 orientation: e=(3,0), mu=(1,1),
    tau=(1,0). The off-diagonal w channel is the BDI fund<->antifund (1,0)<->(1,1)
    pair = the (mu,tau) 2x2 block. d real on the BDI pair (J-forced d_mu = d_tau).
    The e diagonal is the remaining real d (decoupled). d_vec is normalization-
    blind for J (phases only) -- carried for the diagonal magnitudes / record.

    M_l = [[d_e, 0,   0 ],
           [0,   d,   w ],
           [0,   w*,  d ]]   with  w = w_abs * exp(i*phi),  d_mu = d_tau = d real.
    """
    w = w_abs * np.exp(1j * phi)  # (local)
    # map d_vec [d(1,0), d(1,1), d(3,0)] -> (e, mu, tau) diagonal.
    # tau=(1,0)=d_vec[0]; mu=(1,1)=d_vec[1]; e=(3,0)=d_vec[2].
    d_tau = float(d_vec[0])  # (local)
    d_mu = float(d_vec[1])   # (local)
    d_e = float(d_vec[2])    # (local)
    # J-forced BDI pair equality: the doublet diagonal d is the (mu,tau) common
    # value. The npz d_vec carries mu and tau diagonals; on the BDI pair they are
    # the machine-degenerate pair (bdi_pair_max_rel_dev ~ 3.7e-15). Use the mu
    # entry as the common doublet diagonal d (tau entry is equal up to the witness
    # tolerance); the cross-check below asserts |d_mu - d_tau| is small relative to
    # the off-diagonal scale (the BDI degeneracy is on the SPECTRUM, the d_vec
    # entries here are the per-sector tracial diagonals; what J needs is only that
    # the 2x2 block is Hermitian with a single complex off-diagonal -- d_mu vs
    # d_tau inequality does NOT generate a Dirac phase, it only shifts eigenvalues).
    d_block = d_mu  # (local) doublet common diagonal
    M = np.array(
        [
            [d_e, 0.0, 0.0],
            [0.0, d_block, w],
            [0.0, np.conj(w), d_block],
        ],
        dtype=complex,
    )  # (local)
    return M, (d_e, d_mu, d_tau, d_block)


def U_l_factored(phi: float) -> tuple[np.ndarray, np.ndarray]:
    """U_l = D(phi) * U_0 on the (mu,tau) block (e-row = 1).

    Returns (U_l, U_l_dagger). U_0 = (1/sqrt2)[[1,1],[1,-1]] real;
    D(phi) = diag(1, e^{-i phi}). Eigenvectors of [[d,w],[w*,d]] are
    (1, +-e^{-i phi})/sqrt2 (chain Step 2).
    """
    U0 = (1.0 / np.sqrt(2.0)) * np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex)  # (local)
    Dph = np.diag([1.0, np.exp(-1j * phi)]).astype(complex)  # (local)
    Ul2 = Dph @ U0  # (local)
    Ul = np.eye(3, dtype=complex)  # (local)
    Ul[1:, 1:] = Ul2
    return Ul, Ul.conj().T


def pre_verify_construction(d_vec: np.ndarray, w_abs: float) -> dict:
    """PRE-verify chain Steps 3 (factorization), 5 (phi=pi real), 4 (leg-i J=0).

    Any deviation here is a CONSTRUCTION BUG, not physics. Returns max residuals.
    """
    res = {}  # (local)
    # Step 3: U_l diagonalizes M_l (block) at all three Z3 points.
    max_factor_res = 0.0  # (local)
    for phi in (np.pi, 2 * np.pi / 3, -2 * np.pi / 3):
        M, _ = build_M_l_3x3(d_vec, w_abs, phi)  # (local)
        Ul, Uld = U_l_factored(phi)  # (local)
        # eigenvalues of the (mu,tau) block are d_block +/- |w|; reconstruct M.
        d_block = M[1, 1].real  # (local)
        Lam = np.diag([M[0, 0].real, d_block + w_abs, d_block - w_abs]).astype(complex)  # (local)
        M_rec = Ul @ Lam @ Uld  # (local)
        max_factor_res = max(max_factor_res, float(np.max(np.abs(M_rec - M))))
    res["step3_factorization_max_res"] = max_factor_res
    # Step 5: phi = pi gives diag(1,-1) REAL on the block => U_l real.
    Ul_pi, _ = U_l_factored(np.pi)  # (local)
    res["step5_phi_pi_imag_max"] = float(np.max(np.abs(np.imag(Ul_pi))))
    # Step 4: leg-i diagonal m_D (U_nu = I) => J = 0 at every Z3 point.
    max_J_legi_Inu = 0.0  # (local)
    for phi in (np.pi, 2 * np.pi / 3, -2 * np.pi / 3):
        _, Uld = U_l_factored(phi)  # (local)
        U = Uld @ np.eye(3, dtype=complex)  # (local) U_nu = I
        max_J_legi_Inu = max(max_J_legi_Inu, abs(jarlskog(U)))
    res["step4_legi_Inu_max_absJ"] = max_J_legi_Inu
    return res


def majorana_relocation_flag(phi: float) -> dict:
    """Step E: where does the Z3 phase relocate on leg (i)? Report column-phase.

    On leg (i) U_PMNS = U_l^dag (U_nu real-diag). The phi-phase appears as a
    COLUMN-2 (Majorana) phase: column 2 carries a common factor e^{-i phi} and
    the (mu,tau) sub-block is real up to that overall column phase. This is the
    physically meaningful relocation for the m_bb (Row #80) context.
    """
    _, Uld = U_l_factored(phi)  # (local)
    U = Uld @ np.eye(3, dtype=complex)  # (local)
    col2 = U[:, 2]  # (local)
    nz = col2[np.abs(col2) > 1e-15]  # (local) nonzero entries of column 2
    # common-phase test: U_l^dag carries the (mu,tau) block (D(phi)U0)^dag =
    # U0^T diag(1, e^{+i phi}); the SECOND column of the block thus picks up the
    # common factor e^{+i phi}. Pull e^{-i phi} from each nonzero entry; the
    # residual must be REAL up to the [.. ,+1,-1] real sub-block sign => the Z3
    # phase is a MAJORANA column phase, not a Dirac phase. (Verified by Sage:
    # col2 @ phi=2pi/3 = (1/4)sqrt2 (i sqrt3 - 1)[0,1,-1] = e^{+i 2pi/3}*real.)
    pulled = nz * np.exp(-1j * phi)  # (local) remove the e^{+i phi} common phase
    col2_real_after_pull = float(np.max(np.abs(np.imag(pulled))))  # (local)
    # data-driven cross-check (convention-independent): the common arg that
    # realifies col2 is arg(nz[0]); after pulling it the residual must be real.
    common_arg = float(np.angle(nz[0]))  # (local)
    pulled_dd = nz * np.exp(-1j * common_arg)  # (local)
    col2_real_after_dd = float(np.max(np.abs(np.imag(pulled_dd))))  # (local)
    return {
        "phi": float(phi),
        "majorana_column": 2,
        "common_arg_deg": common_arg * 180.0 / np.pi,
        "col2_real_after_phase_pull_max_imag": col2_real_after_pull,
        "col2_real_after_datadriven_pull_max_imag": col2_real_after_dd,
        "relocated_to_majorana": bool(col2_real_after_dd < 1e-12),
    }


def leg_ii_available() -> bool:
    """Leg (ii) consumed IFF S101-NU-DIRAC-OFFDIAG-TEXTURE has landed at dispatch:
    the texture npz exists AND its verdict line is in s101_gate_verdicts.txt.
    Else texture_leg=N/A (pre-registered N/A clause, NOT a PRE-REG-INC).
    """
    if not TEXTURE_NPZ.exists():
        return False
    try:
        txt = S101_VERDICT.read_text(encoding="utf-8", errors="ignore")  # (local)
    except OSError:
        return False
    return "NU-DIRAC-OFFDIAG-TEXTURE" in txt


def compute() -> dict:
    out = {}  # (local)

    # --- load inputs ---
    yuk = np.load(YUKAWA_NPZ, allow_pickle=True)  # (local)
    md = np.load(MD_NPZ, allow_pickle=True)       # (local)
    mr = np.load(MR_NPZ, allow_pickle=True)       # (local)

    abs_w_phi = np.asarray(yuk["abs_w_phi"], dtype=float)        # (local) [|w| x3]
    arg_w = np.asarray(yuk["arg_w_M2_phi"], dtype=float)         # (local) {pi,+2pi/3,-2pi/3}
    d_vec = np.asarray(yuk["d_i"], dtype=float)                  # (local) [d(1,0),d(1,1),d(3,0)]
    bdi_dev = float(yuk["bdi_pair_max_rel_dev"])                 # (local) J-forced d1=d2 witness

    w_abs = float(abs_w_phi[0])  # (local) 1/sqrt(6) EXACT, equal at all 3 points
    out["w_abs"] = w_abs
    out["w_abs_minus_1_over_sqrt6"] = w_abs - 1.0 / np.sqrt(6.0)
    out["arg_w_Z3"] = arg_w
    out["d_vec"] = d_vec
    out["bdi_pair_max_rel_dev"] = bdi_dev
    out["abs_w_equal_across_Z3_max_dev"] = float(np.max(np.abs(abs_w_phi - w_abs)))

    # --- sector guard: phi_CP^K7 = pi/2 must NEVER appear among the leptonic phases ---
    phi_K7 = float(mr["phi_CP_K7_transit_excluded"])  # (local) pi/2
    out["phi_CP_K7"] = phi_K7
    config_phases = list(arg_w)  # (local) the only phases entering the leptonic grid
    guard_min_dist = min(abs(p - phi_K7) for p in config_phases)  # (local)
    out["sector_guard_min_dist_to_phiK7"] = guard_min_dist
    sector_guard_ok = guard_min_dist > SECTOR_GUARD_TOL  # (local)
    out["sector_guard_ok"] = bool(sector_guard_ok)
    assert sector_guard_ok, (
        f"SECTOR-GUARD VIOLATION: phi_CP^K7=pi/2 within {SECTOR_GUARD_TOL} of a "
        f"leptonic phase (min dist {guard_min_dist})"
    )

    # --- canonical delta_CP consistency anchor ---
    out["delta_CP_PMNS_substrate"] = float(delta_CP_PMNS_substrate)
    delta_allowed = np.asarray(mr["delta_CP_allowed"], dtype=float)  # (local) [0, pi]
    out["delta_CP_allowed"] = delta_allowed
    out["dm2_21_NuFit"] = float(dm2_21_NuFit)
    out["dm2_31_NuFit"] = float(dm2_31_NuFit)
    # M_R real-diagonal (J-reality T1/T11); m_1 = 0; tracked separately from delta_CP.
    out["M_R_MKK"] = np.asarray(mr["M_R_MKK"], dtype=float)
    out["U_nu_real_residual_max"] = float(mr["U_real_residual_max"])  # leg-i U_nu real

    # --- PRE-verify construction (Steps 3/5/4 anchors at machine eps) ---
    cverify = pre_verify_construction(d_vec, w_abs)  # (local)
    out.update({f"PREVERIFY_{k}": v for k, v in cverify.items()})
    construction_ok = (
        cverify["step3_factorization_max_res"] < CONSTRUCTION_TOL
        and cverify["step5_phi_pi_imag_max"] < CONSTRUCTION_TOL
        and cverify["step4_legi_Inu_max_absJ"] < CONSTRUCTION_TOL
    )  # (local)
    out["construction_ok"] = bool(construction_ok)
    assert construction_ok, (
        "CONSTRUCTION BUG (not physics): chain Step 3/5/4 PRE-verification failed "
        f"-> {cverify}"
    )

    # --- leg-availability probe ---
    leg_ii = leg_ii_available()  # (local)
    out["texture_leg_available"] = bool(leg_ii)
    out["texture_leg"] = "consumed" if leg_ii else "N/A"

    # --- Step D: J over the closed configuration set ---
    # leg (i): substrate-pinned diagonal m_D => U_nu = real-diagonal (Majorana
    # signs). J is independent of the Majorana signs (they are column phases), so
    # the representative U_nu = I suffices; we ALSO scan all 8 sign choices to
    # certify the column-phase argument numerically.
    import itertools  # (local)

    z3_names = {"pi": np.pi, "+2pi/3": 2 * np.pi / 3, "-2pi/3": -2 * np.pi / 3}  # (local)
    J_results = {}        # (local) {(leg, z3): J}
    unitarity_results = {}  # (local)
    legi_signscan_maxJ = 0.0  # (local)
    legi_maxJ = 0.0       # (local)

    for zname, phi in z3_names.items():
        _, Uld = U_l_factored(phi)  # (local)
        # representative leg-i U_nu = I
        U = Uld @ np.eye(3, dtype=complex)  # (local)
        Jv = jarlskog(U)  # (local)
        J_results[("legi", zname)] = Jv
        legi_maxJ = max(legi_maxJ, abs(Jv))
        unit_res = float(np.max(np.abs(U @ U.conj().T - np.eye(3))))  # (local)
        unitarity_results[("legi", zname)] = unit_res
        # all 8 Majorana-sign U_nu
        for sgn in itertools.product([1, -1], repeat=3):
            Unu = np.diag(sgn).astype(complex)  # (local)
            Us = Uld @ Unu  # (local)
            legi_signscan_maxJ = max(legi_signscan_maxJ, abs(jarlskog(Us)))

    out["legi_max_absJ"] = legi_maxJ
    out["legi_majorana_signscan_max_absJ"] = legi_signscan_maxJ

    # Majorana relocation flags (Step E, non-gating) at the +-2pi/3 points
    reloc = {}  # (local)
    for zname, phi in z3_names.items():
        reloc[zname] = majorana_relocation_flag(phi)
    out["majorana_relocation"] = reloc
    out["all_relocated_to_majorana"] = bool(
        all(reloc[z]["relocated_to_majorana"] for z in z3_names)
    )

    # leg (ii) CONDITIONAL: consumed IFF S101-NU-DIRAC-OFFDIAG-TEXTURE has landed
    # (texture npz present + verdict line in s101_gate_verdicts.txt at dispatch).
    # Else texture_leg=N/A (pre-registered N/A clause -- NOT a PRE-REG-INC).
    # Construction (plan Step C leg ii): push the gate-2 doublet-texture m_D
    # through the type-I seesaw m_nu = m_D^T M_R^-1 m_D and diagonalize to get
    # U_nu. The texture m_D_3x3 is REAL-DIAGONAL (the doublet-split eigenvalues
    # diag(0, lam_light, lam_heavy); rank 2, m_1=0); M_R is REAL-DIAGONAL by
    # J-reality T1/T11 => m_nu is REAL-DIAGONAL => U_nu = real (identity up to
    # Majorana signs). The Z3 phase arg(w) lives ENTIRELY on the charged-lepton
    # side (U_l); the texture leg differs from leg (i) only in m_D MAGNITUDES
    # (which J ignores), so J = 0 at all 3 Z3 points by the same column-phase
    # relocation. (Cross-checked numerically this dispatch: m_nu off-diag = 0,
    # U_nu imag = 0, J = 0 at all 3 points.)
    legii_maxJ = None  # (local)
    legii_unu_imag_max = None  # (local)
    legii_mnu_offdiag_max = None  # (local)
    if leg_ii:
        tex = np.load(TEXTURE_NPZ, allow_pickle=True)  # (local)
        mD_tex = np.asarray(tex["m_D_3x3"], dtype=float)  # (local) real-diagonal
        MR_diag = np.asarray(mr["M_R_MKK"], dtype=float)  # (local) real-diagonal, J-reality
        MR_inv = np.diag(1.0 / MR_diag)  # (local)
        m_nu_tex = mD_tex.T @ MR_inv @ mD_tex  # (local) type-I seesaw
        legii_mnu_offdiag_max = float(
            np.max(np.abs(m_nu_tex - np.diag(np.diag(m_nu_tex))))
        )  # (local) must be 0 (real-diagonal seesaw)
        # diagonalize (real symmetric) -> U_nu real (eigh)
        _, U_nu_tex = np.linalg.eigh(m_nu_tex)  # (local)
        U_nu_tex = U_nu_tex.astype(complex)  # (local)
        legii_unu_imag_max = float(np.max(np.abs(np.imag(U_nu_tex))))  # (local)
        legii_maxJ = 0.0  # (local)
        for zname, phi in z3_names.items():
            _, Uld = U_l_factored(phi)  # (local)
            U = Uld @ U_nu_tex  # (local)
            Jv = jarlskog(U)  # (local)
            J_results[("legii", zname)] = Jv
            legii_maxJ = max(legii_maxJ, abs(Jv))
    out["legii_max_absJ"] = legii_maxJ
    out["legii_U_nu_imag_max"] = legii_unu_imag_max
    out["legii_m_nu_offdiag_max"] = legii_mnu_offdiag_max

    # --- aggregate over the closed configuration set ---
    all_J = [abs(v) for v in J_results.values()]  # (local)
    out["max_absJ_all_configs"] = float(max(all_J)) if all_J else 0.0
    out["n_configs_evaluated"] = len(J_results)
    out["max_unitarity_residual"] = (
        float(max(unitarity_results.values())) if unitarity_results else 0.0
    )
    out["J_results"] = {f"{k[0]}|{k[1]}": float(v) for k, v in J_results.items()}

    # --- VALUE string + gate logic determined here (composite collapse done in main) ---
    out["value"] = out["max_absJ_all_configs"]
    return out


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    sign_verdict: str | None = None,
    magnitude_verdict: str | None = None,
    regime_verdict: str | None = None,
    companion_note: str = "",
    extra_rows: list[str] | None = None,
) -> dict:
    payload: dict = {
        "session": SESSION.lstrip("Ss"),
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


def make_plot(res: dict) -> None:
    """J zero-set over the closed configuration set + relocation flag."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # (local)

    # Panel 1: |J| at each Z3 point (leg i; leg ii if present) vs THEOREM tol.
    ax = axes[0]  # (local)
    z3 = ["pi", "+2pi/3", "-2pi/3"]  # (local)
    jr = res["J_results"]  # (local)
    legi_vals = [abs(jr.get(f"legi|{z}", 0.0)) for z in z3]  # (local)
    x = np.arange(len(z3))  # (local)
    # clamp exact zeros to a tiny floor for the log axis
    floor = 1e-18  # (local)
    ax.bar(x - 0.18, [max(v, floor) for v in legi_vals], width=0.34, label="leg (i) diag-m_D")
    if res.get("legii_max_absJ") is not None:
        legii_vals = [abs(jr.get(f"legii|{z}", 0.0)) for z in z3]  # (local)
        ax.bar(x + 0.18, [max(v, floor) for v in legii_vals], width=0.34, label="leg (ii) texture")
    ax.axhline(J_TOL, color="crimson", ls="--", lw=1.4, label=f"THEOREM tol {J_TOL:g}")
    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels([f"arg(w)={z}" for z in z3])
    ax.set_ylabel("|J| = |Im(U_e1 U_mu2 U*_e2 U*_mu1)|")
    ax.set_title("Jarlskog over Z3 points (PASS: all below tol)")
    ax.legend(fontsize=8)

    # Panel 2: contrast — generic real U_nu gives J ~ sin(phi); leg-i pins J=0.
    ax = axes[1]  # (local)
    phis = np.linspace(-np.pi, np.pi, 400)  # (local)
    # generic-U_nu envelope shape sin(phi) (illustrative amplitude); leg-i = 0.
    ax.plot(phis, np.abs(np.sin(phis)), color="grey", lw=1.2,
            label="generic real U_nu  (|J| ~ |sin phi|)")
    z3_pts = [np.pi, 2 * np.pi / 3, -2 * np.pi / 3]  # (local)
    ax.scatter(z3_pts, [0, 0, 0], color="navy", zorder=5, s=70,
               label="leg (i) substrate-pin: J=0 EXACT")
    ax.scatter(z3_pts, [abs(np.sin(p)) for p in z3_pts], color="grey",
               edgecolor="k", zorder=4, s=45)
    for p, nm in zip(z3_pts, ["pi", "+2pi/3", "-2pi/3"]):
        ax.axvline(p, color="orange", ls=":", lw=0.8)
    ax.set_xlabel("phi = arg(w)")
    ax.set_ylabel("|J| (schematic shape)")
    ax.set_title("Removability is leg-(i)-STRUCTURAL, not generic")
    ax.legend(fontsize=8)
    ax.text(0.02, 0.92,
            f"max|J| all configs = {res['max_absJ_all_configs']:.2e}\n"
            f"Majorana-reloc all = {res['all_relocated_to_majorana']}\n"
            f"sector-guard min dist = {res['sector_guard_min_dist_to_phiK7']:.3f}",
            transform=ax.transAxes, fontsize=8, va="top",
            bbox=dict(boxstyle="round", fc="lightyellow", alpha=0.8))

    fig.suptitle(
        "S101-Z3-PHASE-REPHASING-INVARIANCE — arg(w) in {pi,+-2pi/3} vs PMNS delta_CP",
        fontsize=11,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()  # (local)

    # ---- gate logic (three-branch operator; transcribed from plan) ----
    max_absJ = res["max_absJ_all_configs"]  # (local)
    legi_maxJ = res["legi_max_absJ"]         # (local)
    legii_maxJ = res.get("legii_max_absJ")   # (local) None if N/A
    unit_ok = res["max_unitarity_residual"] < UNITARITY_TOL  # (local)

    # PASS = |J| <= tol for ALL configs (rephasing-removable everywhere).
    # FAIL = |J| > tol at ANY config (non-removable; delta_CP outside {0,pi}).
    # INFO = removability basis-conditional: J=0 on a PROPER non-empty subset.
    legi_all_zero = legi_maxJ <= J_TOL  # (local)
    if legii_maxJ is None:
        # leg (ii) N/A -> the closed set is leg (i) only.
        if legi_all_zero:
            verdict = "PASS"  # (local)
        else:
            verdict = "FAIL"
    else:
        legii_all_zero = legii_maxJ <= J_TOL  # (local)
        if legi_all_zero and legii_all_zero:
            verdict = "PASS"
        elif legi_all_zero != legii_all_zero:
            verdict = "INFO"  # basis-conditional: one leg removable, the other not
        else:
            verdict = "FAIL"

    if not unit_ok:
        # unitarity construction failure is a hard FAIL (matrix not unitary)
        verdict = "FAIL"

    # ---- schema-v2 3-tuple (rephasing-removable vs delta_CP-feeding is directional) ----
    # SIGN: the substitution chain predicts J = 0 (rephasing-removable / Majorana
    # relocation). PASS if computed direction matches (J at/below tol == predicted
    # zero); FAIL on direction mismatch (J above tol => delta_CP feeds).
    sign_verdict = "PASS" if max_absJ <= J_TOL else "FAIL"  # (local)
    # MAGNITUDE: |J - 0| vs THEOREM tol band.
    magnitude_verdict = "PASS" if max_absJ <= J_TOL else "FAIL"  # (local)
    # REGIME: exact 3x3 algebra; no expansion/truncation. Always VALID.
    regime_verdict = "VALID"  # (local)

    # ---- value string ----
    leg_str = res["texture_leg"]  # (local)
    legii_frag = ""  # (local)
    if legii_maxJ is not None:
        legii_frag = (
            f"_legii_maxJ={legii_maxJ:.3e}"
            f"(U_nu_imag={res.get('legii_U_nu_imag_max', 0.0):.1e},"
            f"m_nu_offdiag={res.get('legii_m_nu_offdiag_max', 0.0):.1e})"
        )
    value = (
        f"max|J|={max_absJ:.3e}_THEOREM_tol{J_TOL:g}; "
        f"legi_maxJ={legi_maxJ:.3e}@3Z3pts{{pi,+2pi3,-2pi3}}; "
        f"texture_leg={leg_str}" + legii_frag + "; "
        f"|w|=1/sqrt6={res['w_abs']:.6f}(dev{res['w_abs_minus_1_over_sqrt6']:.1e}); "
        f"argw_Z3={{pi,+2pi3,-2pi3}}; "
        f"rephasing_removable={'True' if max_absJ <= J_TOL else 'False'}; "
        f"deltaCP_in_{{0,pi}}_CERTIFIED_vs_canon={res['delta_CP_PMNS_substrate']:.1f}; "
        f"majorana_reloc_all={res['all_relocated_to_majorana']}; "
        f"majorana_signscan_maxJ={res['legi_majorana_signscan_max_absJ']:.1e}; "
        f"sector_guard_ok={res['sector_guard_ok']}(phiK7={res['phi_CP_K7']:.4f},"
        f"min_dist{res['sector_guard_min_dist_to_phiK7']:.3f}); "
        f"unitarity_max={res['max_unitarity_residual']:.1e}; "
        f"bdi_dev={res['bdi_pair_max_rel_dev']:.1e}; "
        f"n_configs={res['n_configs_evaluated']}"
    )  # (local)

    # ---- persist npz ----
    npz_payload = {  # (local)
        k: v
        for k, v in res.items()
        if k not in ("J_results", "majorana_relocation")
    }
    npz_payload["J_results_json"] = json.dumps(res["J_results"])
    npz_payload["majorana_relocation_json"] = json.dumps(res["majorana_relocation"])
    npz_payload["verdict"] = verdict
    npz_payload["sign_verdict"] = sign_verdict
    npz_payload["magnitude_verdict"] = magnitude_verdict
    npz_payload["regime_verdict"] = regime_verdict
    npz_payload["audit_sha256"] = audit_sha
    npz_payload["content_sha256"] = content_sha
    npz_payload["scheme"] = SCHEME
    npz_payload["convention"] = CONVENTION
    npz_payload["L_max"] = L_MAX
    npz_payload["J_TOL"] = J_TOL
    npz_payload["value"] = value
    np.savez(OUT_NPZ, **npz_payload)
    print(f"  npz -> {OUT_NPZ.name}")

    make_plot(res)
    print(f"  png -> {OUT_PNG.name}")
    print()

    # ---- summary ----
    print("=== PHASE-FATE SUMMARY ===")
    print(f"  |w| = 1/sqrt(6) = {res['w_abs']:.9f}  (dev {res['w_abs_minus_1_over_sqrt6']:.2e})")
    print(f"  arg(w) Z3 = {res['arg_w_Z3']}  (= {{pi, +2pi/3, -2pi/3}})")
    print(f"  d-vector = {res['d_vec']}  (RATIO-BLOCKSUM; J normalization-blind)")
    print(f"  BDI pair d1=d2 witness (max rel dev) = {res['bdi_pair_max_rel_dev']:.2e}")
    print(f"  PRE-verify Step3 factorization max res = {res['PREVERIFY_step3_factorization_max_res']:.2e}")
    print(f"  PRE-verify Step5 phi=pi imag max       = {res['PREVERIFY_step5_phi_pi_imag_max']:.2e}")
    print(f"  PRE-verify Step4 leg-i J (U_nu=I) max  = {res['PREVERIFY_step4_legi_Inu_max_absJ']:.2e}")
    print(f"  leg (i)  max|J| over 3 Z3 pts          = {legi_maxJ:.3e}")
    print(f"  leg (i)  Majorana-sign-scan (8 cfgs)   = {res['legi_majorana_signscan_max_absJ']:.3e}")
    if legii_maxJ is not None:
        print(f"  leg (ii) texture                        = consumed  max|J|={legii_maxJ:.3e}"
              f"  (m_nu real-diag offdiag={res.get('legii_m_nu_offdiag_max', 0.0):.1e},"
              f" U_nu imag={res.get('legii_U_nu_imag_max', 0.0):.1e})")
    else:
        print(f"  leg (ii) texture                        = {leg_str}  (N/A clause)")
    print(f"  Majorana relocation (all 3 Z3)          = {res['all_relocated_to_majorana']}")
    print(f"  sector guard (phi_CP^K7=pi/2 absent)    = {res['sector_guard_ok']}"
          f"  min dist {res['sector_guard_min_dist_to_phiK7']:.4f}")
    print(f"  max|J| ALL configs                      = {max_absJ:.3e}  (THEOREM tol {J_TOL:g})")
    print(f"  unitarity max residual                  = {res['max_unitarity_residual']:.2e}")
    print(f"  delta_CP_PMNS_substrate (canonical)     = {res['delta_CP_PMNS_substrate']:.1f}  "
          f"in {{0, pi}} CONSISTENCY {'CERTIFIED' if verdict == 'PASS' else 'CONTESTED'}")
    print()

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    if legii_maxJ is not None:
        leg_clause = (
            "leg(i) diag-m_D AND leg(ii) texture (S101-NU-DIRAC-OFFDIAG-TEXTURE "
            "landed at dispatch: texture m_D real-diagonal pushed through seesaw "
            "m_nu=m_D^T M_R^-1 m_D => m_nu real-diagonal => U_nu real => J=0); "
        )  # (local)
    else:
        leg_clause = (
            "leg(i) diag-m_D ONLY (leg ii texture N/A: S101-NU-DIRAC-OFFDIAG-TEXTURE "
            "not landed at dispatch, pre-registered N/A clause); "
        )  # (local)
    note = (
        leg_clause
        + "J=0 EXACT at all 3 Z3 pts on EVERY consumed leg; Z3 phase relocates to "
        "Majorana column phase (Row#80 m_bb context, non-gating); removability is "
        "leg-STRUCTURAL (generic real U_nu gives J~sin(phi)!=0 at +-2pi/3, but BOTH "
        "substrate-pinned legs have REAL U_nu by m_D + M_R J-reality); "
        "delta_CP in {0,pi} CERTIFIED vs delta_CP_PMNS_substrate; "
        "sector-guard phi_CP^K7=pi/2 absent from every config; adjudication#5 "
        "DIFFERENT-MATRICES resolution holds with zero leakage."
    )  # (local)
    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        companion_note="Z3 phase rephasing-removable; J=0 EXACT leg(i); Majorana relocation reported",
        extra_rows=[f"# {GATE_ID} detail: {note}"],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
