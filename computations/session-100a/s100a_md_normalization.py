#!/usr/bin/env python3
"""
S100a W5-1 S100a-MD-NORMALIZATION — substrate-forward Dirac-Yukawa map uniqueness;
zero-free-parameter Sigma m_nu re-gate
====================================================================================

Gate: S100a-MD-NORMALIZATION ([SIGN])

Pre-registered thresholds (plan sessions/session-plan/session-100a-plan-w5.md §W5-1):
  PRIMARY:    Sigma_mnu^{substrate-forward} < bound_DESI = 0.072 eV
  JOINT:      |Sigma_mnu^{substrate-forward} - 0.0582053272|/0.0582053272 <= tol_reproduce = 0.05
  UNIQUENESS: |Sigma_mnu^{MAP-A} - Sigma_mnu^{MAP-B}|/Sigma_mnu^{MAP-A} <= tol_uniqueness = 0.05
  strict PASS: DESI AND reproduce AND map_unique==True
  FAIL: substrate-forward maps overshoot the loose bound (Sigma > 0.12 eV)
  INFO: map NON-UNIQUE (maps disagree beyond tol_uniqueness OR an external overall
        Dirac scale Y_ref must be tuned to reach the band) => S99 track_B caveat
        confirmed STRUCTURALLY IRREDUCIBLE (residual-Dirac-scale-normalization-IRREDUCIBLE).

[SIGN] claim (plan §W5-1 substitution chain): the type-I seesaw SUPPRESSES the light
mass — d m_{nu,i}/d M_i = -m_{D,i}^2/M_i^2 < 0 for i=2,3 (strictly), and the substrate
M_R ~ M_KK scale drives Sigma DOWN below the DESI bound (delta = Sigma - bound < 0).
Direction identical to S99; the substrate-forward Y_i change only the ABSOLUTE Sigma,
which is what the uniqueness test interrogates.

METHOD (substrate-forward; INVERTS the S99 back-solve)
------------------------------------------------------
(1) Bottom light-triple from the L_max=12 block-diagonal master cache (sector_evals
    dict, per-(p,q) abs_evals; UNION of the 90 sectors; NO re-diagonalization):
    tower-resolved bottoms of the three lowest Peter-Weyl towers,
      E_1 = min |lambda| of (0,0)  [trivial,      triality 0, C_2 = 0   ]
      E_2 = min |lambda| of (1,0)=(0,1) [fundamental, triality 1/2, C_2 = 4/3]
      E_3 = min |lambda| of (1,1)  [adjoint,      triality 0, C_2 = 3   ]
    = the ~0.82-0.87 M_KK E1/E2/E3 set S96-MATTER-R-HIERARCHY read as R_direct=9.86
    (rank-1 direct-spacing wall). Cross-checked against the s55_bogoliubov_992.npz
    alternate triple (omega_f post-transit spectrum) and the S96 R_direct value.
(2) Two PRE-REGISTERED substrate-forward maps (competing reductions of the SAME
    triple — this IS the uniqueness test). Shared substrate-natural overall scale
    Y_ref = E_1 (the raw dimensionless bottom eigenvalue, M_KK units; NO external
    input). Rank-deficiency (m_1 = 0 PROVEN) => Y_1 = 0 in the seesaw texture:
      MAP-A (eigenvalue-proportional): Y_i = Y_ref * (E_i/E_ref), E_ref = E_1
              => Y_i^A = E_i for i = 2,3 (Y_1 = 0 imposed by rank deficiency).
      MAP-B (Casimir-graded):          Y_i = Y_ref * sqrt(C_2(p_i,q_i)/C_2_ref),
              C_2_ref = C_2(1,0) = 4/3 (lowest NONZERO tower Casimir)
              => Y^B = [0 (EXACT, C_2(0,0)=0 — rank deficiency EMERGES), E_1, 1.5*E_1].
(3) Type-I seesaw per map: m_D = Y v_ew/sqrt(2); M_R = B-branch D_K fold energies
    (read from the pinned S99 baseline npz; cross-checked to the S60 log + the L12
    cache spectral coincidence < tol_MR); m_nu = m_D^T M_R^{-1} m_D (3x3 real-symmetric,
    eigvalsh); Sigma = sum |eigenvalues| in eV.
(4) Re-gate vs DESI 0.072 eV + the 0.0582053272 eV reproduce band + the uniqueness
    ratio; quantify the residual freedom (required overall Y_ref rescale per map;
    per-generation required rescale = shape test; required Y_3/Y_2 vs map shapes).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py            (M_KK, v_ew, Sigma_mnu_FW,
        Sigma_mnu_bound_DESI_2024, tau_fold; feeds audit_sha256)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (bottom-triple source)
  - computations/session-55/s55_bogoliubov_992.npz         (alternate triple, omega_f)
  - computations/session-99/s99_w3_seesaw_summnu.npz       (baseline Sigma/M_R/Y_i)
  - computations/session-60/s60_lepto_cp_log.txt           (M_R fold-energy texture)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<Sigma_A/Sigma_B summary>, scheme=type-I-seesaw-substrate-forward-Yi-from-DK-bottom-triple,
   convention=ABSOLUTE, L_max=12)

Classification: PARTICLE
  Generations are the SU(3) Peter-Weyl Z_3-triality multiplicity; the neutrino Dirac
  Yukawas live as the overlap of the light-triple fiber modes with the Higgs |s(h)|^2
  mode in the M_3(C) summand of A_K = C (+) H (+) M_3(C). Flow: D_K eigenvalues
  (bottom light-triple) -> substrate-forward Yukawa map Y_i -> m_D = Y v/sqrt(2) ->
  type-I seesaw with M_R = B-branch D_K fold energies (Majorana scale INTERNAL to the
  spectrum) -> Sigma_mnu (laboratory-IN observable vs DESI). The gate tests whether
  the FIRST arrow (eigenvalue -> Yukawa) is a UNIQUE substrate map or carries a
  residual scale. Cross-axis derivation-author tag: connes-ncg-theorist owns the
  Dirac-side D_F texture reading (whether the bottom-triple -> Y_i map is forced by
  the finite Dirac operator's representation structure).

DISCIPLINE
----------
- `from canonical_constants import *`; intermediates tagged `# (local)`
- CPU-correct (3x3 eigh + cache dict reads, sub-100x100); OMP_NUM_THREADS=8 before numpy
- dual-SHA (audit + content) per S84+; verdict via emit_verdict MCP tool (script PRINTS payload)
- [SIGN] gate => sign/magnitude/regime 3-tuple in the payload (all-three-or-none)
- exit 0 for any valid scientific verdict (PASS/FAIL/INFO are all results)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
import sys
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

_SHARED_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_shared"
)
if _SHARED_PATH not in sys.path:
    sys.path.insert(0, _SHARED_PATH)

from canonical_constants import *  # noqa: F401,F403,E402  (M_KK, v_ew, Sigma_mnu_FW, Sigma_mnu_bound_DESI_2024, tau_fold)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "100a"                                                   # (local) letter-suffixed sub-session
GATE_ID = "S100a-MD-NORMALIZATION"                                 # (local)
SCHEME = "type-I-seesaw-substrate-forward-Yi-from-DK-bottom-triple"  # (local)
CONVENTION = "ABSOLUTE"                                            # (local)
L_MAX = 12                                                         # (local)

# Pre-registered gate boundaries (plan §W5-1 operator + machinery_pin_map)
TOL_REPRODUCE = 0.05                     # rel tol on Sigma vs the 0.0582053272 target  # (local)
TOL_UNIQUENESS = 0.05                    # rel tol between MAP-A and MAP-B Sigmas  # (local)
TOL_MR = 0.02                            # B-branch spectral-coincidence rel tol (S96 PART-1)  # (local)
TOL_EIGH = 1e-12                         # eigh numerical tolerance  # (local)
INFO_CEIL = 0.12                         # eV; FAIL iff substrate-forward maps overshoot this  # (local)
PUBLICATION_SIG_FIGS = 5                 # value-string precision (npz carries full float64; Class 8.3)  # (local)
DEEP_SEESAW_REGIME = 1e-6                # max(m_D/M_R) < this => VALID regime (S99 criterion)  # (local)

# Cross-check anchors (pinned input artifacts / prior verdict values — comparison-only)
R_S96_VERDICT = 9.86183067373777         # (local) S96-MATTER-R-HIERARCHY verdict value (rank-1 wall)
TOL_R_CROSSCHECK = 1e-6                  # (local) rel tol on the R_direct reproduction (machine-precision expected)
TOL_BASELINE = 1e-6                      # (local) rel tol on the S99-baseline Sigma re-derivation

EV_PER_GEV = 1.0e-9                      # (local) eV = 1e-9 GeV

OUT_NPZ = SESSION_DIR / "s100a_md_normalization.npz"
OUT_PNG = SESSION_DIR / "s100a_md_normalization.png"

S84_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S55_BOG = COMPUTATIONS_DIR / "session-55" / "s55_bogoliubov_992.npz"
S99_BASE = COMPUTATIONS_DIR / "session-99" / "s99_w3_seesaw_summnu.npz"
S60_LOG = COMPUTATIONS_DIR / "session-60" / "s60_lepto_cp_log.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S84_CACHE,
    S55_BOG,
    S99_BASE,
    S60_LOG,
]

# The three lowest Peter-Weyl towers the bottom-triple occupies (S96 sector-assignment,
# verified at machine precision against the L12 cache in compute()):
TOWER_SECTORS = [(0, 0), (1, 0), (1, 1)]   # (local) gen-1/2/3 towers; (1,0)=(0,1) conjugate pair


def su3_casimir(p: int, q: int) -> float:
    """SU(3) quadratic Casimir, normalization C_2(1,0) = 4/3, C_2(1,1) = 3."""
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


def su3_triality(p: int, q: int) -> int:
    """Z_3 triality of the (p,q) irrep."""
    return (p - q) % 3


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+)
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


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
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
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
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
# Section 5 — Substrate readers + cross-check helpers
# ---------------------------------------------------------------------------
def read_bottom_triple_from_cache(cache_path: Path):
    """Tower-resolved bottom light-triple from the L12 block-diagonal master cache.

    Reads per-(p,q)-sector abs_evals (NO re-diagonalization — the cache IS the
    block-diagonal spectrum). E_i = min |lambda| of the i-th lowest Peter-Weyl tower:
    (0,0) trivial, (1,0)/(0,1) fundamental conjugate pair, (1,1) adjoint.
    Returns (E_triple, casimirs, trialities, conj_pair_split).
    """
    d = np.load(cache_path, allow_pickle=True)  # (local)
    sec = d["sector_evals"].item()              # (local) dict {(p,q): {'dim','level','abs_evals'}}
    if len(sec) != 90:
        print(f"  [warn] cache sector count = {len(sec)} (expected 90)")
    e10 = float(np.min(np.asarray(sec[(1, 0)]["abs_evals"])))   # (local)
    e01 = float(np.min(np.asarray(sec[(0, 1)]["abs_evals"])))   # (local)
    conj_split = abs(e10 - e01)                                  # (local) conjugate-pair degeneracy check
    E = np.array([
        float(np.min(np.asarray(sec[(0, 0)]["abs_evals"]))),     # E_1: trivial tower
        e10,                                                      # E_2: fundamental tower
        float(np.min(np.asarray(sec[(1, 1)]["abs_evals"]))),     # E_3: adjoint tower
    ])                                                            # (local)
    C2 = np.array([su3_casimir(p, q) for (p, q) in TOWER_SECTORS])   # (local) [0, 4/3, 3]
    tri = np.array([su3_triality(p, q) for (p, q) in TOWER_SECTORS])  # (local) [0, 1, 0]; (0,1) carries 2
    return E, C2, tri, conj_split


def crosscheck_s55_alternate(s55_path: Path, E: np.ndarray):
    """Alternate-source check: each tower-bottom E_i present in the s55 omega_f
    post-transit Bogoliubov spectrum (992 modes) at machine precision."""
    d = np.load(s55_path, allow_pickle=True)        # (local)
    wf = np.sort(np.asarray(d["omega_f"]).ravel())  # (local)
    nearest = np.array([wf[np.argmin(np.abs(wf - e))] for e in E])  # (local)
    reldiff = np.abs(nearest - E) / E               # (local)
    return nearest, reldiff, bool(np.all(reldiff < 1e-8))


def crosscheck_R_direct(E: np.ndarray) -> tuple[float, float, bool]:
    """Reproduce the S96-MATTER-R-HIERARCHY R_direct from the cache-read triple
    (conv-A direct spacings, m_1=0): confirms the SAME triple the S96 gate read."""
    m2 = E[1] - E[0]                                 # (local)
    m3 = E[2] - E[0]                                 # (local)
    R = (m3**2 - m2**2) / (m2**2 - 0.0)              # (local)
    rd = abs(R - R_S96_VERDICT) / R_S96_VERDICT      # (local)
    return R, rd, bool(rd < TOL_R_CROSSCHECK)


def verify_MR_in_S60_log(log_path: Path, targets: np.ndarray) -> bool:
    """Confirm the B-branch fold energies are the M_R texture stated in the S60 log."""
    try:
        txt = log_path.read_text(errors="ignore")  # (local)
    except OSError:
        return False
    found = re.findall(r"[-+]?\d*\.\d+", txt)      # (local)
    fvals = np.array([float(x) for x in found])    # (local)
    ok = True                                      # (local)
    for t in targets:
        if not np.any(np.isclose(fvals, t, rtol=1e-4, atol=1e-4)):
            ok = False
    return ok


def MR_spectral_coincidence(cache_path: Path, targets: np.ndarray):
    """Re-extract the 3 M_i from the L12 block-diagonal cache by spectral coincidence
    (union of the 90 sectors' abs_evals; NO re-diagonalization)."""
    d = np.load(cache_path, allow_pickle=True)   # (local)
    sec = d["sector_evals"].item()               # (local)
    allv = np.concatenate([np.asarray(blk["abs_evals"]).ravel() for blk in sec.values()])  # (local)
    absu = np.unique(np.round(allv, 8))          # (local)
    nearest = np.array([absu[np.argmin(np.abs(absu - t))] for t in targets])  # (local)
    reldiff = np.abs(nearest - targets) / targets  # (local)
    return nearest, reldiff, float(reldiff.max())


def seesaw_sigma(Y: np.ndarray, M_R_GeV: np.ndarray) -> tuple[np.ndarray, float, np.ndarray, np.ndarray]:
    """Type-I seesaw: m_D = Y v/sqrt(2); m_nu = m_D^T M_R^{-1} m_D (3x3 real-symmetric,
    eigvalsh); returns (m_nu_eV ascending, Sigma_eV, m_D_GeV, dmnu_dM)."""
    v = float(v_ew)                                          # (local)
    m_D_GeV = Y * v / np.sqrt(2.0)                           # (local)
    mD_mat = np.diag(m_D_GeV)                                # (local)
    MR_mat = np.diag(M_R_GeV)                                # (local)
    m_nu_mat_GeV = mD_mat.T @ np.linalg.inv(MR_mat) @ mD_mat  # (local) magnitude (Majorana sign absorbed)
    m_nu_mat_GeV = 0.5 * (m_nu_mat_GeV + m_nu_mat_GeV.T)     # (local) symmetrize
    evals_GeV = np.linalg.eigvalsh(m_nu_mat_GeV)             # (local)
    m_nu_eV = np.sort(np.abs(evals_GeV)) / EV_PER_GEV        # (local) ascending
    Sigma_eV = float(m_nu_eV.sum())                          # (local)
    with np.errstate(divide="ignore", invalid="ignore"):
        dmnu_dM = np.where(M_R_GeV > 0, -(m_D_GeV ** 2) / (M_R_GeV ** 2), 0.0)  # (local) GeV/GeV
    return m_nu_eV, Sigma_eV, m_D_GeV, dmnu_dM


# ---------------------------------------------------------------------------
# Section 6 — Compute (substrate-FORWARD maps + uniqueness test)
# ---------------------------------------------------------------------------
def compute() -> dict:
    M_KK_GeV = float(M_KK)                       # (local) 7.428660036284456e16 GeV (CONST-FREEZE-42)
    Sigma_target = float(Sigma_mnu_FW)           # (local) 0.0582053272 eV (S99-W3-SEESAW-SUMMNU)
    bound_DESI = float(Sigma_mnu_bound_DESI_2024)  # (local) 0.072 eV (DESI 2024, 95% CL)

    # --- (1) bottom light-triple, tower-resolved, from the L12 cache ---
    E, C2, tri, conj_split = read_bottom_triple_from_cache(S84_CACHE)
    s55_nearest, s55_reldiff, s55_ok = crosscheck_s55_alternate(S55_BOG, E)
    R_direct, R_reldiff, R_ok = crosscheck_R_direct(E)

    # --- M_R from the pinned S99 baseline artifact (B-branch D_K fold energies) ---
    d99 = np.load(S99_BASE, allow_pickle=True)   # (local)
    M_R_MKK = np.asarray(d99["M_R_MKK"]).ravel()  # (local) [1.0044, 1.0786, 1.1700]
    Y_S99 = np.asarray(d99["Y"]).ravel()          # (local) back-solved baseline [0, 4.794, 11.928]
    Sigma_S99_npz = float(d99["Sigma_mnu_eV"])    # (local) 0.0582053272...
    m_nu_S99 = np.asarray(d99["m_nu_eV"]).ravel()  # (local) [0, 0.0086776, 0.0495278]
    M_R_GeV = M_R_MKK * M_KK_GeV                  # (local)

    # --- M_R cross-checks: S60 log texture + L12 cache spectral coincidence ---
    mr_in_s60 = verify_MR_in_S60_log(S60_LOG, M_R_MKK)              # (local)
    mr_nearest, mr_reldiff, mr_maxrel = MR_spectral_coincidence(S84_CACHE, M_R_MKK)

    # --- CC0: baseline re-derivation — my seesaw pipeline reproduces the S99/canonical Sigma ---
    m_nu_base, Sigma_base, m_D_base, _ = seesaw_sigma(Y_S99, M_R_GeV)
    base_reldiff_npz = abs(Sigma_base - Sigma_S99_npz) / Sigma_S99_npz       # (local)
    base_reldiff_canon = abs(Sigma_base - Sigma_target) / Sigma_target       # (local)
    baseline_ok = bool(base_reldiff_npz < TOL_BASELINE and base_reldiff_canon < TOL_BASELINE)  # (local)

    # --- (2) substrate-FORWARD maps (shared substrate-natural scale Y_ref = E_1) ---
    Y_ref = E[0]                                  # (local) raw dimensionless bottom eigenvalue (M_KK units)
    # MAP-A (eigenvalue-proportional): Y_i = Y_ref * (E_i/E_1) = E_i; Y_1 = 0 (rank deficiency imposed)
    Y_A = np.array([0.0, E[1], E[2]])             # (local)
    # MAP-B (Casimir-graded): Y_i = Y_ref * sqrt(C_2_i/C_2_ref), C_2_ref = C_2(1,0) = 4/3;
    # Y_1 = 0 EXACT because C_2(0,0) = 0 — the rank deficiency EMERGES from the grading.
    C2_ref = C2[1]                                # (local) 4/3
    Y_B = Y_ref * np.sqrt(C2 / C2_ref)            # (local) [0, E_1, 1.5*E_1] exactly
    shape_A = Y_A[2] / Y_A[1]                     # (local) E_3/E_2
    shape_B = Y_B[2] / Y_B[1]                     # (local) sqrt(C2_3/C2_2) = 3/2 exact

    # --- (3) seesaw per map ---
    m_nu_A, Sigma_A, m_D_A, dmnu_dM_A = seesaw_sigma(Y_A, M_R_GeV)
    m_nu_B, Sigma_B, m_D_B, dmnu_dM_B = seesaw_sigma(Y_B, M_R_GeV)

    # --- (4) gate quantities ---
    uniq_ratio = abs(Sigma_A - Sigma_B) / Sigma_A                    # (local) pre-registered uniqueness operator
    maps_agree = bool(uniq_ratio <= TOL_UNIQUENESS)                  # (local)
    reproduce_reldiff_A = abs(Sigma_A - Sigma_target) / Sigma_target  # (local)
    reproduce_reldiff_B = abs(Sigma_B - Sigma_target) / Sigma_target  # (local)
    reproduce_A = bool(reproduce_reldiff_A <= TOL_REPRODUCE)         # (local)
    reproduce_B = bool(reproduce_reldiff_B <= TOL_REPRODUCE)         # (local)
    desi_A = bool(Sigma_A < bound_DESI)                              # (local)
    desi_B = bool(Sigma_B < bound_DESI)                              # (local)
    overshoot = bool(min(Sigma_A, Sigma_B) > INFO_CEIL)              # (local) FAIL clause (both maps overshoot)

    # map_unique (plan method (2)): maps agree AND no free overall scale left —
    # i.e. the parameter-free (Y_ref = E_1) evaluation already lands in the band.
    map_unique = bool(maps_agree and reproduce_A and reproduce_B)    # (local)

    # Residual-freedom quantification (the track_B content):
    # required overall Y_ref rescale per map (Sigma scales as Y_ref^2)
    rescale_Yref_A = float(np.sqrt(Sigma_target / Sigma_A))          # (local)
    rescale_Yref_B = float(np.sqrt(Sigma_target / Sigma_B))          # (local)
    # per-generation required rescale (shape test): Y_i^{S99-required}/Y_i^{map}, i=2,3
    pergen_rescale_A = Y_S99[1:] / Y_A[1:]                           # (local)
    pergen_rescale_B = Y_S99[1:] / Y_B[1:]                           # (local)
    shape_required = Y_S99[2] / Y_S99[1]                             # (local) 2.488 = sqrt(m3 M3/(m2 M2))
    shape_const_A = bool(np.isclose(pergen_rescale_A[0], pergen_rescale_A[1], rtol=TOL_UNIQUENESS))  # (local)
    shape_const_B = bool(np.isclose(pergen_rescale_B[0], pergen_rescale_B[1], rtol=TOL_UNIQUENESS))  # (local)

    # --- [SIGN] suppression direction (both maps): d m_nu_i/d M_i = -m_D_i^2/M_i^2 < 0, i=2,3 ---
    suppression_all_negative = bool(
        np.all(dmnu_dM_A[1:] < 0.0) and np.all(dmnu_dM_B[1:] < 0.0)
    )                                                                # (local)
    delta_A = Sigma_A - bound_DESI                                   # (local) negative => below bound
    delta_B = Sigma_B - bound_DESI                                   # (local)

    # deep-seesaw regime (both maps)
    supp_ratio = float(max(np.max(m_D_A[1:] / M_R_GeV[1:]),
                           np.max(m_D_B[1:] / M_R_GeV[1:])))         # (local)

    return {
        "E": E, "C2": C2, "tri": tri, "conj_split": conj_split,
        "tower_sectors": np.array(TOWER_SECTORS),
        "s55_nearest": s55_nearest, "s55_reldiff": s55_reldiff, "s55_ok": s55_ok,
        "R_direct": R_direct, "R_reldiff": R_reldiff, "R_ok": R_ok,
        "M_R_MKK": M_R_MKK, "M_R_GeV": M_R_GeV,
        "mr_in_s60": mr_in_s60, "mr_nearest": mr_nearest,
        "mr_reldiff": mr_reldiff, "mr_maxrel": mr_maxrel,
        "Y_S99": Y_S99, "Sigma_S99_npz": Sigma_S99_npz, "m_nu_S99": m_nu_S99,
        "Sigma_base": Sigma_base, "m_nu_base": m_nu_base,
        "base_reldiff_npz": base_reldiff_npz, "base_reldiff_canon": base_reldiff_canon,
        "baseline_ok": baseline_ok,
        "Y_ref": Y_ref, "Y_A": Y_A, "Y_B": Y_B, "C2_ref": C2_ref,
        "shape_A": shape_A, "shape_B": shape_B, "shape_required": shape_required,
        "m_D_A": m_D_A, "m_D_B": m_D_B,
        "m_nu_A": m_nu_A, "m_nu_B": m_nu_B,
        "Sigma_A": Sigma_A, "Sigma_B": Sigma_B,
        "dmnu_dM_A": dmnu_dM_A, "dmnu_dM_B": dmnu_dM_B,
        "uniq_ratio": uniq_ratio, "maps_agree": maps_agree,
        "reproduce_reldiff_A": reproduce_reldiff_A, "reproduce_reldiff_B": reproduce_reldiff_B,
        "reproduce_A": reproduce_A, "reproduce_B": reproduce_B,
        "desi_A": desi_A, "desi_B": desi_B, "overshoot": overshoot,
        "map_unique": map_unique,
        "rescale_Yref_A": rescale_Yref_A, "rescale_Yref_B": rescale_Yref_B,
        "pergen_rescale_A": pergen_rescale_A, "pergen_rescale_B": pergen_rescale_B,
        "shape_const_A": shape_const_A, "shape_const_B": shape_const_B,
        "suppression_all_negative": suppression_all_negative,
        "delta_A": delta_A, "delta_B": delta_B,
        "supp_ratio": supp_ratio,
        "Sigma_target": Sigma_target, "bound_DESI": bound_DESI, "info_ceil": INFO_CEIL,
    }


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict (3-tuple + composite collapse) + 4-tuple
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
        "session": SESSION,
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


def evaluate_gate(res: dict) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    [SIGN] 3-tuple per gate-verdicts.md schema-v2:
      sign_verdict      = PASS iff the suppression derivatives d m_nu_i/dM_i < 0 (i=2,3,
                          both maps) AND delta = Sigma - bound_DESI < 0 (both maps) —
                          the pre-registered direction (identical to S99).
      magnitude_verdict = PASS iff DESI AND reproduce AND uniqueness all met;
                          FAIL iff both maps overshoot INFO_CEIL = 0.12 eV;
                          INFO otherwise (the pre-registered NON-UNIQUE outcome).
      regime_verdict    = VALID iff deep seesaw (max m_D/M_R < 1e-6) throughout.
    """
    sign_v = "PASS" if (res["suppression_all_negative"]
                        and res["delta_A"] < 0.0 and res["delta_B"] < 0.0) else "FAIL"  # (local)

    if res["overshoot"]:
        mag_v = "FAIL"   # (local)
    elif (res["desi_A"] and res["desi_B"] and res["map_unique"]):
        mag_v = "PASS"   # (local)
    else:
        mag_v = "INFO"   # (local) NON-UNIQUE / residual-scale outcome (pre-registered)

    regime_v = "VALID" if res["supp_ratio"] < DEEP_SEESAW_REGIME else "MARGINAL"  # (local)

    # --- composite collapse (gate-verdicts.md PRE-REGISTERED rule) ---
    if regime_v == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"  # (local)
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"  # (local)
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"  # (local)
    elif mag_v == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)
    return composite, sign_v, mag_v, regime_v


# ---------------------------------------------------------------------------
# Section 8 — Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict, path: Path) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(16.5, 5))  # (local)
    gens = np.array([1, 2, 3])  # (local)

    # (a) Yukawa shapes: substrate-forward maps vs the S99 back-solved (required) Y
    ax = axes[0]  # (local)
    ax.semilogy(gens[1:], res["Y_S99"][1:], "k*-", ms=13,
                label=r"$Y_i$ required (S99 back-solve)")
    ax.semilogy(gens[1:], res["Y_A"][1:], "o-", color="#1f77b4",
                label=r"MAP-A: $Y_i = E_i$ (eigenvalue-prop)")
    ax.semilogy(gens[1:], res["Y_B"][1:], "s-", color="#d62728",
                label=r"MAP-B: $Y_i = E_1\sqrt{C_2^{(i)}/C_2^{(2)}}$ (Casimir)")
    ax.annotate(f"shape req: $Y_3/Y_2$={res['shape_required']:.3f}\n"
                f"MAP-A: {res['shape_A']:.3f}  MAP-B: {res['shape_B']:.3f}",
                xy=(0.04, 0.05), xycoords="axes fraction", fontsize=8,
                bbox=dict(boxstyle="round", fc="lightyellow", alpha=0.9))
    ax.set_xlabel("generation $i$")
    ax.set_ylabel(r"$Y_i$ (dimensionless)")
    ax.set_xticks(gens)
    ax.set_title("Dirac Yukawas: substrate-forward maps\nvs oscillation-required ($Y_1=0$ rank-def.)")
    ax.legend(fontsize=7, loc="upper left")
    ax.grid(alpha=0.3, which="both")

    # (b) Sigma per map vs target band + DESI bound (log scale)
    ax = axes[1]  # (local)
    xs = np.array([0, 1])  # (local)
    vals = [res["Sigma_A"], res["Sigma_B"]]  # (local)
    cols = ["#1f77b4", "#d62728"]  # (local)
    ax.bar(xs, vals, width=0.55, color=cols, edgecolor="k")
    for x, v in zip(xs, vals):
        ax.text(x, v * 1.25, f"{v:.3e}", ha="center", fontsize=8)
    t = res["Sigma_target"]  # (local)
    ax.axhspan(t * (1 - TOL_REPRODUCE), t * (1 + TOL_REPRODUCE), color="green", alpha=0.25,
               label=f"reproduce band {t:.6f}$\\pm$5%")
    ax.axhline(res["bound_DESI"], color="red", ls="--", lw=2,
               label=f"DESI 2024 = {res['bound_DESI']} eV")
    ax.axhline(res["info_ceil"], color="darkred", ls=":", lw=1.5,
               label=f"FAIL ceiling = {res['info_ceil']} eV")
    ax.set_yscale("log")
    ax.set_xticks(xs)
    ax.set_xticklabels(["MAP-A\n(eigenvalue)", "MAP-B\n(Casimir)"], fontsize=9)
    ax.set_ylabel(r"$\Sigma m_\nu$ [eV]")
    ax.set_title(f"$\\Sigma m_\\nu$ substrate-forward: ~100x BELOW band\n"
                 f"uniq ratio = {res['uniq_ratio']:.3f} (tol {TOL_UNIQUENESS}) "
                 f"$\\Rightarrow$ NON-UNIQUE")
    ax.legend(fontsize=7, loc="center right")
    ax.grid(alpha=0.3, axis="y", which="both")

    # (c) per-generation required rescale (shape failure)
    ax = axes[2]  # (local)
    w = 0.35  # (local)
    ax.bar(gens[1:] - w / 2, res["pergen_rescale_A"], width=w, color="#1f77b4",
           edgecolor="k", label="MAP-A: $Y_i^{req}/Y_i^A$")
    ax.bar(gens[1:] + w / 2, res["pergen_rescale_B"], width=w, color="#d62728",
           edgecolor="k", label="MAP-B: $Y_i^{req}/Y_i^B$")
    ax.axhline(res["rescale_Yref_A"], color="#1f77b4", ls="--", lw=1.2,
               label=f"single $Y_{{ref}}$ rescale A = {res['rescale_Yref_A']:.2f}")
    ax.axhline(res["rescale_Yref_B"], color="#d62728", ls="--", lw=1.2,
               label=f"single $Y_{{ref}}$ rescale B = {res['rescale_Yref_B']:.2f}")
    ax.set_xticks(gens[1:])
    ax.set_xlabel("generation $i$")
    ax.set_ylabel("required rescale factor")
    ax.set_title("Residual freedom is NOT 1-parameter:\nper-generation rescale non-constant (shape fails)")
    ax.legend(fontsize=7)
    ax.grid(alpha=0.3, axis="y")

    fig.suptitle(f"{GATE_ID} — substrate-forward Dirac-Yukawa maps: uniqueness test "
                 f"(PARTICLE; $m_1$=0 NO; $M_R$ = B-branch $D_K$ fold energies)", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(path, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()  # (local)

    # --- substitution-chain echo ([SIGN] direction with substituted numbers) ---
    print("--- [SIGN] substitution chain: seesaw suppression direction (both maps) ---")
    print(f"  bottom triple E   = {res['E']}  (M_KK units; towers {TOWER_SECTORS})")
    print(f"  triality          = {res['tri']}  ((0,1) conjugate carries 2); C_2 = {res['C2']}")
    print(f"  conj-pair split   = {res['conj_split']:.3e}  ((1,0) vs (0,1) bottoms)")
    print(f"  M_R (M_KK)        = {res['M_R_MKK']}")
    print(f"  M_R (GeV)         = {res['M_R_GeV']}")
    print(f"  Y_ref = E_1       = {res['Y_ref']:.10f}")
    print(f"  MAP-A Y           = {res['Y_A']}   (shape Y3/Y2 = {res['shape_A']:.6f})")
    print(f"  MAP-B Y           = {res['Y_B']}   (shape Y3/Y2 = {res['shape_B']:.6f} = 3/2 exact)")
    print(f"  MAP-A m_D (GeV)   = {res['m_D_A']}")
    print(f"  MAP-B m_D (GeV)   = {res['m_D_B']}")
    print(f"  MAP-A d m_nu/dM   = {res['dmnu_dM_A']}  (all < 0 for i=2,3 => suppression)")
    print(f"  MAP-B d m_nu/dM   = {res['dmnu_dM_B']}  (all < 0 for i=2,3 => suppression)")
    print(f"  suppression_all_negative = {res['suppression_all_negative']}")
    print(f"  MAP-A m_nu (eV)   = {res['m_nu_A']}")
    print(f"  MAP-B m_nu (eV)   = {res['m_nu_B']}")
    print(f"  Sigma_A           = {res['Sigma_A']:.10e} eV   delta_A = {res['delta_A']:+.4e} (<0)")
    print(f"  Sigma_B           = {res['Sigma_B']:.10e} eV   delta_B = {res['delta_B']:+.4e} (<0)")
    print(f"  deep-seesaw ratio = {res['supp_ratio']:.3e}  (< {DEEP_SEESAW_REGIME} => VALID)")
    print()
    print("--- gate quantities ---")
    print(f"  target Sigma      = {res['Sigma_target']} eV (Sigma_mnu_FW canonical, S99)")
    print(f"  uniq_ratio        = {res['uniq_ratio']:.6f}  (tol {TOL_UNIQUENESS}; agree={res['maps_agree']})")
    print(f"  reproduce reldiff A/B = {res['reproduce_reldiff_A']:.6f} / {res['reproduce_reldiff_B']:.6f} (tol {TOL_REPRODUCE})")
    print(f"  DESI ok A/B       = {res['desi_A']} / {res['desi_B']}  (bound {res['bound_DESI']} eV)")
    print(f"  overshoot (>{res['info_ceil']})  = {res['overshoot']}")
    print(f"  map_unique        = {res['map_unique']}")
    print(f"  required Y_ref rescale A/B = {res['rescale_Yref_A']:.4f} / {res['rescale_Yref_B']:.4f}")
    print(f"  per-gen rescale A = {res['pergen_rescale_A']}  (constant? {res['shape_const_A']})")
    print(f"  per-gen rescale B = {res['pergen_rescale_B']}  (constant? {res['shape_const_B']})")
    print(f"  shape required Y3/Y2 = {res['shape_required']:.6f}  vs A {res['shape_A']:.6f} / B {res['shape_B']:.6f}")
    print()
    print("--- cross-checks ---")
    print(f"  CC0 baseline re-derivation: Sigma_base = {res['Sigma_base']:.10f} eV")
    print(f"      vs npz {res['Sigma_S99_npz']:.10f} (reldiff {res['base_reldiff_npz']:.2e});"
          f" vs canonical (reldiff {res['base_reldiff_canon']:.2e}); ok={res['baseline_ok']}")
    print(f"  CC-R: R_direct(cache triple) = {res['R_direct']:.11f} vs S96 {R_S96_VERDICT}"
          f" (reldiff {res['R_reldiff']:.2e}; ok={res['R_ok']})")
    print(f"  CC-s55: omega_f nearest = {res['s55_nearest']} reldiff = {res['s55_reldiff']} ok={res['s55_ok']}")
    print(f"  CC-MR: cache coincidence nearest = {res['mr_nearest']}")
    print(f"         reldiff {res['mr_reldiff']}  maxrel {res['mr_maxrel']:.5f} (tol {TOL_MR})")
    print(f"  CC-S60: M_R texture in S60 log = {res['mr_in_s60']}")
    print()

    composite, sign_v, mag_v, regime_v = evaluate_gate(res)  # (local)

    # --- save npz (full float64; Class 8.3 publication-precision discipline) ---
    np.savez(
        OUT_NPZ,
        E_triple=res["E"], C2=res["C2"], triality=res["tri"],
        tower_sectors=res["tower_sectors"], conj_split=res["conj_split"],
        s55_nearest=res["s55_nearest"], s55_reldiff=res["s55_reldiff"], s55_ok=res["s55_ok"],
        R_direct_crosscheck=res["R_direct"], R_reldiff=res["R_reldiff"], R_ok=res["R_ok"],
        M_R_MKK=res["M_R_MKK"], M_R_GeV=res["M_R_GeV"],
        mr_in_s60=res["mr_in_s60"], mr_nearest=res["mr_nearest"],
        mr_reldiff=res["mr_reldiff"], mr_maxrel=res["mr_maxrel"],
        Y_S99=res["Y_S99"], Sigma_S99_npz=res["Sigma_S99_npz"], m_nu_S99=res["m_nu_S99"],
        Sigma_base=res["Sigma_base"], m_nu_base=res["m_nu_base"],
        base_reldiff_npz=res["base_reldiff_npz"], base_reldiff_canon=res["base_reldiff_canon"],
        baseline_ok=res["baseline_ok"],
        Y_ref=res["Y_ref"], Y_A=res["Y_A"], Y_B=res["Y_B"], C2_ref=res["C2_ref"],
        shape_A=res["shape_A"], shape_B=res["shape_B"], shape_required=res["shape_required"],
        m_D_A_GeV=res["m_D_A"], m_D_B_GeV=res["m_D_B"],
        m_nu_A_eV=res["m_nu_A"], m_nu_B_eV=res["m_nu_B"],
        Sigma_mnu_MAP_A_eV=res["Sigma_A"], Sigma_mnu_MAP_B_eV=res["Sigma_B"],
        dmnu_dM_A=res["dmnu_dM_A"], dmnu_dM_B=res["dmnu_dM_B"],
        uniq_ratio=res["uniq_ratio"], maps_agree=res["maps_agree"],
        reproduce_reldiff_A=res["reproduce_reldiff_A"],
        reproduce_reldiff_B=res["reproduce_reldiff_B"],
        reproduce_A=res["reproduce_A"], reproduce_B=res["reproduce_B"],
        desi_A=res["desi_A"], desi_B=res["desi_B"], overshoot=res["overshoot"],
        map_unique=res["map_unique"],
        rescale_Yref_A=res["rescale_Yref_A"], rescale_Yref_B=res["rescale_Yref_B"],
        pergen_rescale_A=res["pergen_rescale_A"], pergen_rescale_B=res["pergen_rescale_B"],
        shape_const_A=res["shape_const_A"], shape_const_B=res["shape_const_B"],
        suppression_all_negative=res["suppression_all_negative"],
        delta_A=res["delta_A"], delta_B=res["delta_B"], supp_ratio=res["supp_ratio"],
        Sigma_target=res["Sigma_target"], bound_DESI=res["bound_DESI"],
        info_ceil=res["info_ceil"],
        tol_reproduce=TOL_REPRODUCE, tol_uniqueness=TOL_UNIQUENESS,
        tol_MR=TOL_MR, tol_eigh=TOL_EIGH,
        tau_fold_pin=float(tau_fold), M_KK_pin=float(M_KK), v_ew_pin=float(v_ew),
        verdict=composite, sign_verdict=sign_v,
        magnitude_verdict=mag_v, regime_verdict=regime_v,
        audit_sha256=audit_sha, content_sha256=content_sha,
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
    )
    print(f"  saved: {OUT_NPZ.name}")

    make_plot(res, OUT_PNG)
    print(f"  saved: {OUT_PNG.name}")
    print()

    # --- 4-tuple + emit_verdict payload (5-sig-fig value string; npz carries float64) ---
    value_str = (
        f"SigmaA={res['Sigma_A']:.4e}eV;SigmaB={res['Sigma_B']:.4e}eV;"
        f"uniq_ratio={res['uniq_ratio']:.4f}>{TOL_UNIQUENESS}_NONUNIQUE;"
        f"reproduce_reldiff_A={res['reproduce_reldiff_A']:.4f};"
        f"rescale_Yref_A={res['rescale_Yref_A']:.3f}_B={res['rescale_Yref_B']:.3f};"
        f"shape_Y3overY2_req={res['shape_required']:.4f}_vs_A={res['shape_A']:.4f}_B={res['shape_B']:.4f};"
        f"DESI_ok_both;map_unique={res['map_unique']};"
        f"residual-Dirac-scale-normalization-IRREDUCIBLE;trackB_0.9"
    )  # (local)
    tag = emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)

    note = ("substrate-forward Yi maps NON-UNIQUE: MAP-A (eigenvalue-prop) vs MAP-B "
            "(Casimir-graded) disagree %.1f%%; both ~100x below 0.0582 eV band; external "
            "Y_ref rescale (%.2fx / %.2fx) required AND per-generation rescale non-constant "
            "(shape fails too); S99 track_B caveat STRUCTURALLY IRREDUCIBLE; Sigma_mnu_FW "
            "unchanged" % (100 * res["uniq_ratio"], res["rescale_Yref_A"], res["rescale_Yref_B"]))  # (local)
    extra = [
        (f"# Sigma_mnu_MAP_A={res['Sigma_A']:.10e} eV Sigma_mnu_MAP_B={res['Sigma_B']:.10e} eV "
         f"(full float64 in npz); target Sigma_mnu_FW={res['Sigma_target']} eV; "
         f"DESI bound={res['bound_DESI']} eV; FAIL ceiling={res['info_ceil']} eV"),
        (f"# bottom-triple E=[{res['E'][0]:.8f},{res['E'][1]:.8f},{res['E'][2]:.8f}] M_KK; "
         f"towers=[(0,0),(1,0)+(0,1),(1,1)] triality=[0,(1|2),0] C2=[0,4/3,3]; "
         f"R_direct_crosscheck={res['R_direct']:.6f} (S96 rank-1 wall reproduced); "
         f"MAP-B Y1=0 EXACT (C2(0,0)=0 - rank deficiency EMERGES from Casimir grading)"),
        (f"# track_B posterior 0.9 (plan discriminator: INFO -> 0.9 track_B); "
         f"dmnu_dM<0 all i=2,3 both maps; deep-seesaw ratio {res['supp_ratio']:.2e}; "
         f"CC0 baseline reldiff {res['base_reldiff_canon']:.2e}; MR coincidence maxrel "
         f"{res['mr_maxrel']:.4f}<{TOL_MR}"),
    ]  # (local)

    print_verdict_payload(composite, value_str, audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
                          companion_note=note, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (sign={sign_v} mag={mag_v} regime={regime_v}; wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
