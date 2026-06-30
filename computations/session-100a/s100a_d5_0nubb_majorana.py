#!/usr/bin/env python3
"""
S100a W5-2 S100a-D5-0NUBB-MAJORANA -- KO-dim-6 Pfaffian Majorana texture -> m_bb vs 0nubb bounds
=================================================================================================

Gate: S100a-D5-0NUBB-MAJORANA ([VERIFY])

Pre-registered threshold (plan sessions/session-plan/session-100a-plan-w5.md, YAML block
"## SS W5-2. S100a-D5-0NUBB-MAJORANA", strict_PASS_boundary + operator):
  PASS: m_bb^{central} < m_betabeta_KamLANDZen (0.122 eV, loose-NME end)  AND
        m_bb^{central} in [1.5e-3, 4.5e-3] eV  (NO funnel, m_1 = 0)
  FAIL: m_bb^{central} > m_betabeta_KamLANDZen (substrate Majorana texture already excluded)
  INFO: DIRAC determination (m_bb = NULL, lepton number conserved -- definite structural
        result), or a material NEW qualification on the m_bb value half.

Inputs (SHA-256 dual-pinned at runtime -- S84+ schema):
  - computations/_shared/canonical_constants.py
  - computations/session-99/s99_w3_seesaw_summnu.npz       (Route-A hierarchical m_i, M_R, NO)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (L12 cache cross-check, (0,0) sector)
  - computations/session-96/s96_matter_0nubb.npz           (S96 KO-dim-6 determination cross-check)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<determination+m_bb+band+bounds>, scheme=KO-dim-6-Pfaffian-Majorana-on-H_K+_
   S99-oscillation-anchored-m_i-RouteA, convention=ABSOLUTE, L_max=12)

Classification: PARTICLE

METHODOLOGY
-----------
PART 1 RE-USES the S96-MATTER-0NUBB machinery (computations/session-96/s96_matter_0nubb.py;
FULL physical Cl(8)/KO-dim-6 build via dirac_spectrum, NOT a SCHEMATIC helper): canonical
Cl(8) gammas, corrected charge conjugation C2 = g1 g3 g5 g7, particle-hole C1 = g2 g4 g6 g8,
chirality g9, bare finite Dirac D_F = i*Omega on the (0,0) singlet at tau_fold; KO-dim-6
axioms on the conjugate-doubled C^32 (J^2=+1, JD=DJ, Jg=-gJ); (1,1,0) SM-singlet
identification via so(8) Cartan weights; Majorana-vs-Dirac DETERMINATION on representation
content (J-self-conjugate singlet within its chirality, zero opposite-chirality Dirac
partners, non-obstructed H_F+ Majorana block). Every PART-1 output is cross-checked against
the stored s96_matter_0nubb.npz values (the determination is DEFINITE either way).

PART 2 (the NEW content vs S96): m_bb = |sum_i U_ei^2 m_i| with the S99 OSCILLATION-ANCHORED
hierarchical masses m_i = [0, 0.0086776, 0.0495278] eV (normal ordering, m_1 = 0, from
s99_w3_seesaw_summnu.npz) -- NOT the S96 W4-2 raw quasi-degenerate M_KK-unit magnitudes and
NOT the W4-2 framework U_ei (whose angles do not fit NuFit; the W4-2 INFO caveat). This is
the clean Route-A: the PMNS electron-row U_ei are LABORATORY-IN inputs pinned from the plan's
NuFit-6.0 NO values sin^2(th12)=0.307, sin^2(th13)=0.0220 (ABSENT from canonical_constants
per the plan-freeze list_constants check -> pinned in-script as # (local) per the plan
Input-SHA-Ledger note). delta_CP in {0,pi} is substrate-forced ([J,D_K]=0 => M_R real);
both values give the IDENTICAL m_bb (e^{-2i*delta} = 1 at delta = 0 and pi) -- verified.
Majorana phases alpha_2, alpha_3 are scanned on the pre-registered 240 x 40 grid (step
2pi/240 x 2pi/40, diagnostic band bracket); the central no-phase value is the primary
deterministic observable (no-cancellation positive sum => funnel UPPER edge).

SCOPE PIN (load-bearing, from the plan): this gate supplies the OBSERVABLE leg of the D5
Majorana-vs-Dirac discriminator ONLY. Capstone 7.3 D5 STATUS stays `unreconciled` regardless
of this verdict; the "no-seesaw"-vs-Majorana-M_R prose adjudication is a workshop question;
the m_bb falsifier-master-inventory row routes to mack-cosmic-bridge as SOLE WRITER at
session close. Cross-gate caveat (W5-1 closed INFO): the m_i absolute scale is oscillation-
anchored with residual-Dirac-scale-normalization-IRREDUCIBLE (track_B 0.9) -- m_bb is a
prediction CONDITIONAL on the measured Delta-m^2 (+ substrate NO, m_1=0, Majorana texture),
NOT a zero-free-parameter substrate number.

DISCIPLINE
----------
- `from canonical_constants import *`; intermediates tagged `# (local)`
- 16x16/32x32 Clifford + 3-term contraction: numpy.linalg (sub-100x100; CPU correct),
  OMP capped at 8 BEFORE numpy import (plan machinery_pin_map GPU_path)
- SHA-256 of all input files logged in first 20 lines of stdout; dual-SHA (S84+)
- Verdict emitted via the `emit_verdict` knowledge-MCP tool: this script PRINTS the payload
  (print_verdict_payload) and does NOT write the verdict file (Windows open("a") race).
- [VERIFY] trigger: NO schema-v2 3-tuple row.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- thread caps BEFORE numpy import (machinery pin: OMP=8, CPU path)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
SESSION_DIR = os.path.dirname(os.path.abspath(__file__))
SHARED_DIR = os.path.join(os.path.dirname(SESSION_DIR), "_shared")
sys.path.insert(0, SHARED_DIR)

# Canonical constants (MANDATORY first project import)
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    tau_fold, M_KK,
    dm2_21_NuFit, dm2_31_NuFit,
    m_betabeta_KamLANDZen, m_betabeta_LEGEND200_reach, m_betabeta_nextgen_reach,
    Sigma_mnu_FW,
)

# ---------------------------------------------------------------------------
# Section 2 -- standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# S96-MATTER-0NUBB machinery (FULL physical Cl(8)/KO-dim-6 build; _shared/dirac_spectrum.py)
from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    build_cliff8, build_chirality,
)

# ---------------------------------------------------------------------------
# Section 3 -- paths + pre-registration (plan SS W5-2 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION_DIR_P = Path(SESSION_DIR)
COMPUTATIONS_DIR = SESSION_DIR_P.parent
SHARED_DIR_P = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "100a"                                                    # (local) letter-suffixed sub-session
GATE_ID = "S100a-D5-0NUBB-MAJORANA"                                 # (local)
SCHEME = "KO-dim-6-Pfaffian-Majorana-on-H_K+_S99-oscillation-anchored-m_i-RouteA"  # (local)
CONVENTION = "ABSOLUTE"                                             # (local)
L_MAX = 12                                                          # (local)
TOL_MAJ = 1.0e-12        # (local) tol_majorana_detect -- KO-dim-6 Pfaffian nonzero floor (S96 pin)
TAU = tau_fold           # (local) single-slice eval point (canonical tau_fold = 0.19)

# Pre-registered gate band (plan SS W5-2 strict_PASS_boundary; NO funnel at m_1 = 0)
FUNNEL_LO_EV = 1.5e-3    # (local) pre-registered NO funnel lower edge [eV]
FUNNEL_HI_EV = 4.5e-3    # (local) pre-registered NO funnel upper edge [eV]

# Laboratory-IN PMNS pins -- plan SS W5-2 machinery_pin_map + substitution chain values
# ("NuFit-6.0 NO best fit" per the plan). ABSENT from canonical_constants
# (plan-freeze MCP list_constants('sin2_theta') -> only sin2_thetaW_* entries), so pinned
# in-script per the plan Input-SHA-Ledger note: laboratory-IN observation pins with explicit
# provenance, Source-Reconciliation class (f) does NOT fire.
SIN2_TH12 = 0.307        # (local) sin^2(theta_12), plan pin "NuFit-6.0 NO" [lab-IN]
SIN2_TH13 = 0.0220       # (local) sin^2(theta_13), plan pin "NuFit-6.0 NO" [lab-IN]

# Diagnostic-only sensitivity pins (NON-GATING; PMNS global-fit version sensitivity check):
# NuFit-6.0 (Sept 2024) IC19-with-SK NO best fit quotes sin^2(th12)=0.303, sin^2(th13)=0.02225;
# the plan's 0.307/0.0220 match the NuFit-5.x/PDG-style values. The gate uses the PLAN pins
# (pre-registration discipline); this diagnostic quantifies the version sensitivity only.
SIN2_TH12_DIAG = 0.303   # (local) DIAGNOSTIC ONLY -- NuFit-6.0 IC19+SK NO
SIN2_TH13_DIAG = 0.02225 # (local) DIAGNOSTIC ONLY -- NuFit-6.0 IC19+SK NO

# Majorana-phase grid (plan: step 2pi/240 on alpha_2 x 2pi/40 on alpha_3; scan_role=diagnostic)
N_ALPHA2 = 240           # (local)
N_ALPHA3 = 40            # (local)

OUT_NPZ = SESSION_DIR_P / "s100a_d5_0nubb_majorana.npz"
OUT_PNG = SESSION_DIR_P / "s100a_d5_0nubb_majorana.png"

CANON = SHARED_DIR_P / "canonical_constants.py"
S99_NPZ = COMPUTATIONS_DIR / "session-99" / "s99_w3_seesaw_summnu.npz"
S84_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S96_NPZ = COMPUTATIONS_DIR / "session-96" / "s96_matter_0nubb.npz"

INPUT_FILES = [CANON, S99_NPZ, S84_CACHE, S96_NPZ]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 dual-pin block (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(Path(path).read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(Path(p).resolve().relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """audit_sha256 = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    try:
        script_bytes = Path(script_path).read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = Path(canonical_path).read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- PART 1: KO-dim-6 Pfaffian Majorana determination
#              (S96-MATTER-0NUBB machinery re-used verbatim; cross-checked vs stored npz)
# ---------------------------------------------------------------------------
def build_bare_singlet_DF(tau: float):
    """Bare finite Dirac operator D_F = i*Omega on the (0,0) singlet sector (16x16)."""
    gens = su3_generators()                       # (local)
    f_abc = compute_structure_constants(gens)     # (local)
    B_ab = compute_killing_form(f_abc)            # (local)
    g_s = jensen_metric(B_ab, tau)                # (local)
    E = orthonormal_frame(g_s)                    # (local)
    ft = frame_structure_constants(f_abc, E)      # (local)
    Gamma = connection_coefficients(ft)           # (local)
    Omega = spinor_connection_offset(Gamma, build_cliff8())  # (local)
    return 1j * Omega                             # (local) Hermitian D_F


def so8_cartan_weights(gammas):
    """so(8) Cartan weight 4-tuples H_k = i g_{2k-1} g_{2k} (diagonal +-1), shape (4,16)."""
    H = np.array([np.diag(1j * gammas[2 * k] @ gammas[2 * k + 1]).real for k in range(4)])  # (local)
    return H


def compute_part1() -> dict:
    """Re-run the S96 PART-1 determination (algebra-following; DEFINITE either way)."""
    p1 = {}  # (local)
    gammas = build_cliff8()
    g9 = build_chirality(gammas)
    C2 = gammas[0] @ gammas[2] @ gammas[4] @ gammas[6]   # corrected J factor (real symm; s34a)
    C1 = gammas[1] @ gammas[3] @ gammas[5] @ gammas[7]   # particle-hole factor
    I16 = np.eye(16)                                      # (local)
    D_F = build_bare_singlet_DF(TAU)

    # structural anchors
    herm_err = float(np.max(np.abs(D_F - D_F.conj().T)))                 # (local)
    anti_g9 = float(np.max(np.abs(g9 @ D_F + D_F @ g9)))                 # (local) {g9,D_F}=0
    C2sq_err = float(np.max(np.abs(C2 @ C2 - I16)))                      # (local)

    # antilinear T-symmetry (T1) vs linear-commutator pitfall contrast
    antilinear_Tsym = float(np.max(np.abs(C2 @ np.conj(D_F) @ C2 - D_F)))   # (local) = 0 (T1)
    linear_commutator = float(np.max(np.abs(C2 @ D_F - D_F @ C2)))          # (local) != 0 (PITFALL)

    # KO-dim-6 axioms on the canonical conjugate-DOUBLED C^32 (s66)
    Xi = np.block([[np.zeros((16, 16)), I16], [I16, np.zeros((16, 16))]])   # (local) swap
    D32 = np.block([[D_F, 0 * I16], [0 * I16, np.conj(D_F)]])               # (local)
    g32 = np.block([[g9, 0 * I16], [0 * I16, -g9]])                         # (local)
    ko_J2 = float(np.max(np.abs(Xi @ Xi - np.eye(32))))                     # (local) J^2=+1
    ko_JD = float(np.max(np.abs(Xi @ np.conj(D32) - D32 @ Xi)))             # (local) JD=DJ (eps'=+1)
    ko_Jg = float(np.max(np.abs(Xi @ np.conj(g32) + g32 @ Xi)))             # (local) Jg=-gJ (eps''=-1)
    ko_anti_g32 = float(np.max(np.abs(g32 @ D32 + D32 @ g32)))              # (local) {g32,D32}=0

    # (1,1,0) SM singlet identification via so(8) Cartan weights
    wp = np.diag(g9).real                                                  # (local)
    Hp = [i for i in range(16) if wp[i] > 0]                               # (local) H_K+
    Hm = [i for i in range(16) if wp[i] < 0]                               # (local) H_K-
    H = so8_cartan_weights(gammas)                                         # (local) (4,16)
    singlets_Hp = [i for i in Hp if np.all(H[:, i].astype(int) == H[:, i].astype(int)[0])]  # (local)
    singlets_Hm = [i for i in Hm if np.all(H[:, i].astype(int) == H[:, i].astype(int)[0])]  # (local)
    SINGLET = singlets_Hp[0] if singlets_Hp else 0                         # (local)

    # antilinear Majorana bilinear on the bare D_F (T4: bare/tree = 0; mass is seesaw-generated)
    xi = np.zeros(16, complex); xi[SINGLET] = 1.0                          # (local)
    Jxi = C2 @ np.conj(xi)                                                 # (local) antilinear J=C2*K
    m_M_bare = complex(Jxi.conj() @ (D_F @ xi))                            # (local)
    m_M_bare_abs = float(abs(m_M_bare))                                    # (local)

    # C1-conjugate of the singlet (same-chirality pairing = Majorana signature)
    cc_idx = int(np.argmax(np.abs(C1[:, SINGLET])))                        # (local)
    cc_same_chirality = bool(wp[cc_idx] == wp[SINGLET])                    # (local)

    # Dirac-partner count (opposite-chirality SM singlets)
    n_dirac_partner = len(singlets_Hm)                                     # (local)
    dirac_possible = (n_dirac_partner > 0)                                 # (local)

    # H_F+ Majorana block via the doubled antilinear form (admissibility measure)
    B32 = Xi @ D32                                                         # (local) Majorana form
    Hp32 = [i for i in range(32) if np.diag(g32).real[i] > 0]              # (local) H_F+ (16-dim)
    Bpp32 = B32[np.ix_(Hp32, Hp32)]                                        # (local)
    maj_block_frob = float(np.linalg.norm(Bpp32))                          # (local)
    maj_block_sv = np.linalg.svd(Bpp32, compute_uv=False)                  # (local)

    # DETERMINATION (representation content + J-pairing; identical rule to S96)
    majorana_admitted = (not dirac_possible) and cc_same_chirality and (maj_block_frob > TOL_MAJ)  # (local)
    determination = "MAJORANA" if majorana_admitted else "DIRAC"           # (local)

    # D_F spectrum (for the L12 cache (0,0)-sector cross-check)
    DF_abs_evals = np.sort(np.abs(np.linalg.eigvalsh(D_F)))                # (local) 16 values

    p1.update(dict(
        herm_err=herm_err, anti_g9=anti_g9, C2sq_err=C2sq_err,
        antilinear_Tsym=antilinear_Tsym, linear_commutator=linear_commutator,
        ko_J2=ko_J2, ko_JD=ko_JD, ko_Jg=ko_Jg, ko_anti_g32=ko_anti_g32,
        Hp=np.array(Hp), Hm=np.array(Hm),
        singlets_Hp=np.array(singlets_Hp), singlets_Hm=np.array(singlets_Hm),
        SINGLET=SINGLET, singlet_weight=H[:, SINGLET].astype(int),
        m_M_bare_abs=m_M_bare_abs, cc_idx=cc_idx, cc_same_chirality=cc_same_chirality,
        n_dirac_partner=n_dirac_partner, dirac_possible=dirac_possible,
        maj_block_frob=maj_block_frob,
        maj_block_minsv=float(maj_block_sv.min()), maj_block_maxsv=float(maj_block_sv.max()),
        determination=determination, majorana_admitted=majorana_admitted,
        DF_abs_evals=DF_abs_evals,
    ))
    return p1


def crosscheck_part1_vs_s96(p1: dict) -> dict:
    """CC-P1: every re-run PART-1 output vs the stored s96_matter_0nubb.npz values."""
    cc = {}  # (local)
    s96 = np.load(S96_NPZ, allow_pickle=True)  # (local)
    det_s96 = str(s96["determination"])        # (local)
    cc["s96_determination"] = det_s96
    cc["determination_match"] = bool(p1["determination"] == det_s96)
    cc["frob_reldiff"] = float(abs(p1["maj_block_frob"] - float(s96["maj_block_frob"]))
                               / float(s96["maj_block_frob"]))
    cc["n_dirac_partner_match"] = bool(p1["n_dirac_partner"] == int(s96["n_dirac_partner"]))
    cc["cc_same_chirality_match"] = bool(p1["cc_same_chirality"] == bool(s96["cc_same_chirality"]))
    cc["singlet_match"] = bool(p1["SINGLET"] == int(s96["SINGLET"]))
    ko_keys = ["ko_J2", "ko_JD", "ko_Jg", "ko_anti_g32", "antilinear_Tsym"]  # (local)
    cc["ko_residual_max_rerun"] = float(max(p1[k] for k in ko_keys))
    cc["ko_residual_max_s96"] = float(max(float(s96[k]) for k in ko_keys))
    cc["ko_axioms_all_zero"] = bool(cc["ko_residual_max_rerun"] == 0.0
                                    and cc["ko_residual_max_s96"] == 0.0)
    cc["linear_commutator_s96"] = float(s96["linear_commutator"])
    cc["linear_commutator_reldiff"] = float(
        abs(p1["linear_commutator"] - cc["linear_commutator_s96"]) / cc["linear_commutator_s96"])
    cc["all_match"] = bool(
        cc["determination_match"] and cc["n_dirac_partner_match"]
        and cc["cc_same_chirality_match"] and cc["singlet_match"]
        and cc["frob_reldiff"] < 1e-12 and cc["ko_axioms_all_zero"])
    return cc


def crosscheck_cache_L12(p1: dict) -> dict:
    """CC-CACHE: D_F re-run spectrum vs the L12 master cache (0,0) sector (D_K|_(0,0) = D_F)."""
    cc = {}  # (local)
    cache = np.load(S84_CACHE, allow_pickle=True)  # (local)
    sec = cache["sector_evals"].item()             # (local) dict {(p,q): {'dim','level','abs_evals'}}
    cc["n_sectors"] = int(len(sec))
    cc["sector00_present"] = bool((0, 0) in sec)
    if cc["sector00_present"]:
        abs00 = np.sort(np.asarray(sec[(0, 0)]["abs_evals"], dtype=float).ravel())  # (local)
        DF_abs = p1["DF_abs_evals"]  # (local) 16 sorted |evals|
        if abs00.size == DF_abs.size:
            cc["cache00_maxdiff"] = float(np.max(np.abs(abs00 - DF_abs)))
        else:
            # cache may store unique magnitudes; compare on the union of unique values
            uniq_c = np.unique(np.round(abs00, 9))   # (local)
            uniq_d = np.unique(np.round(DF_abs, 9))  # (local)
            n = min(uniq_c.size, uniq_d.size)        # (local)
            cc["cache00_maxdiff"] = float(np.max(np.abs(uniq_c[:n] - uniq_d[:n])))
        cc["cache00_min_abs"] = float(abs00.min())
        cc["DF_min_abs"] = float(DF_abs.min())
        cc["cache00_match"] = bool(cc["cache00_maxdiff"] < 1e-9)
    else:
        cc["cache00_match"] = False
    return cc


# ---------------------------------------------------------------------------
# Section 6 -- PART 2: m_bb = |sum_i U_ei^2 m_i| (Route-A, S99 masses + plan PMNS pins)
# ---------------------------------------------------------------------------
def compute_part2() -> dict:
    p2 = {}  # (local)
    s99 = np.load(S99_NPZ, allow_pickle=True)  # (local)
    m_i = np.asarray(s99["m_nu_eV"], dtype=float)  # (local) [0, 0.0086776, 0.0495278] eV
    p2["m_i_eV"] = m_i
    p2["s99_verdict"] = str(s99["verdict"])
    p2["M_R_MKK"] = np.asarray(s99["M_R_MKK"], dtype=float)
    p2["delta_CP_allowed"] = np.asarray(s99["delta_CP_allowed"], dtype=float)

    # plan-quoted triple cross-check (the spawn/plan pin [0, 0.0086776, 0.0495278] eV)
    m_i_plan = np.array([0.0, 0.0086776, 0.0495278])                       # (local) plan SS W5-2 pin
    p2["plan_triple_maxdiff"] = float(np.max(np.abs(m_i - m_i_plan)))

    # normal-ordering check (m_1 = 0 rank-deficient lightest; m_2 < m_3)
    p2["ordering_NO"] = bool(m_i[0] == 0.0 and m_i[1] > 0.0 and m_i[2] > m_i[1])

    # implied Delta-m^2 vs canonical NuFit-6.0 pins (cross-check on the S99 m_i anchoring)
    dm2_21_implied = float(m_i[1] ** 2 - m_i[0] ** 2)                      # (local)
    dm2_31_implied = float(m_i[2] ** 2 - m_i[0] ** 2)                      # (local)
    p2["dm2_21_implied"] = dm2_21_implied
    p2["dm2_31_implied"] = dm2_31_implied
    p2["dm2_21_reldiff_vs_NuFit"] = float(abs(dm2_21_implied - dm2_21_NuFit) / dm2_21_NuFit)
    p2["dm2_31_reldiff_vs_NuFit"] = float(abs(dm2_31_implied - dm2_31_NuFit) / dm2_31_NuFit)

    # PMNS electron-row magnitudes (plan pins; lab-IN)
    c13sq = 1.0 - SIN2_TH13                                                # (local)
    U_e1sq = (1.0 - SIN2_TH12) * c13sq                                     # (local) c12^2 c13^2
    U_e2sq = SIN2_TH12 * c13sq                                             # (local) s12^2 c13^2
    U_e3sq = SIN2_TH13                                                     # (local) s13^2
    U_eisq = np.array([U_e1sq, U_e2sq, U_e3sq])                            # (local)
    p2["U_eisq"] = U_eisq
    # electron-row closure (algebraic identity c12^2c13^2 + s12^2c13^2 + s13^2 = 1)
    p2["unitarity_resid"] = float(abs(U_eisq.sum() - 1.0))

    # term decomposition at zero phase (substitution-chain values)
    terms = U_eisq * m_i                                                    # (local) [0, t2, t3] eV
    p2["terms_eV"] = terms
    mbb_central = float(abs(terms.sum()))                                   # (local) eV
    p2["mbb_central_eV"] = mbb_central
    p2["mbb_central_meV"] = mbb_central * 1e3

    # delta_CP in {0, pi} substrate-forced degeneracy check: U_e3^2 -> s13^2 e^{-2i delta}
    mbb_d0 = float(abs(terms[0] + terms[1] + U_e3sq * np.exp(-2j * 0.0) * m_i[2]))      # (local)
    mbb_dpi = float(abs(terms[0] + terms[1] + U_e3sq * np.exp(-2j * np.pi) * m_i[2]))   # (local)
    p2["mbb_delta0_eV"] = mbb_d0
    p2["mbb_deltapi_eV"] = mbb_dpi
    p2["deltaCP_degeneracy_absdiff"] = float(abs(mbb_d0 - mbb_dpi))

    # Majorana-phase band (pre-registered diagnostic grid 240 x 40, step 2pi/240 x 2pi/40)
    a2 = np.linspace(0.0, 2.0 * np.pi, N_ALPHA2, endpoint=False)            # (local)
    a3 = np.linspace(0.0, 2.0 * np.pi, N_ALPHA3, endpoint=False)            # (local)
    A2, A3 = np.meshgrid(a2, a3, indexing="ij")                             # (local)
    Z = terms[0] + terms[1] * np.exp(1j * A2) + terms[2] * np.exp(1j * A3)  # (local)
    G = np.abs(Z)                                                           # (local) (240,40) eV
    p2["alpha2_grid"] = a2
    p2["alpha3_grid"] = a3
    p2["mbb_grid_eV"] = G
    p2["mbb_band_lo_eV"] = float(G.min())
    p2["mbb_band_hi_eV"] = float(G.max())
    # analytic band cross-check (m_1 = 0 => band = [|t2 - t3|, t2 + t3]; pi and 0 are on-grid)
    p2["band_lo_analytic_eV"] = float(abs(terms[1] - terms[2]))
    p2["band_hi_analytic_eV"] = float(terms[1] + terms[2])
    p2["band_lo_absdiff"] = float(abs(p2["mbb_band_lo_eV"] - p2["band_lo_analytic_eV"]))
    p2["band_hi_absdiff"] = float(abs(p2["mbb_band_hi_eV"] - p2["band_hi_analytic_eV"]))
    p2["central_is_band_max"] = bool(abs(mbb_central - p2["mbb_band_hi_eV"]) < 1e-15)

    # plan-freeze hand-substitution cross-check (plan chain Step 3: 3.69e-3 eV, 3 sig figs)
    p2["plan_handsub_eV"] = 3.69e-3                                         # (local) plan Step-3 value
    p2["plan_handsub_reldiff"] = float(abs(mbb_central - 3.69e-3) / 3.69e-3)

    # bound placement (canonical falsifier pins)
    p2["below_KamLANDZen"] = bool(mbb_central < m_betabeta_KamLANDZen)
    p2["below_LEGEND200"] = bool(mbb_central < m_betabeta_LEGEND200_reach)
    p2["below_nextgen"] = bool(mbb_central < m_betabeta_nextgen_reach)
    p2["margin_KamLANDZen"] = float(m_betabeta_KamLANDZen / mbb_central)
    p2["margin_LEGEND200"] = float(m_betabeta_LEGEND200_reach / mbb_central)
    p2["margin_nextgen"] = float(m_betabeta_nextgen_reach / mbb_central)
    p2["in_NO_funnel"] = bool(FUNNEL_LO_EV <= mbb_central <= FUNNEL_HI_EV)
    p2["band_inside_funnel"] = bool(p2["mbb_band_lo_eV"] >= FUNNEL_LO_EV
                                    and p2["mbb_band_hi_eV"] <= FUNNEL_HI_EV)

    # ---- DIAGNOSTIC sensitivity rows (NON-GATING; specialist robustness checks) ----
    # (d1) NuFit-6.0 dm2-implied masses (m2 = sqrt(dm2_21), m3 = sqrt(dm2_31)) with plan angles
    m2_nf = float(np.sqrt(dm2_21_NuFit))                                    # (local) diagnostic
    m3_nf = float(np.sqrt(dm2_31_NuFit))                                    # (local) diagnostic
    p2["diag_mbb_NuFit_dm2_eV"] = float(U_e2sq * m2_nf + U_e3sq * m3_nf)
    # (d2) NuFit-6.0 IC19+SK best-fit angles with the S99 masses
    c13sq_d = 1.0 - SIN2_TH13_DIAG                                          # (local) diagnostic
    p2["diag_mbb_NuFit60_angles_eV"] = float(
        SIN2_TH12_DIAG * c13sq_d * m_i[1] + SIN2_TH13_DIAG * m_i[2])
    p2["diag_angle_sensitivity_rel"] = float(
        abs(p2["diag_mbb_NuFit60_angles_eV"] - mbb_central) / mbb_central)
    # (d3) S96 PART-2 comparison (framework W4-2 U_ei route; the INFO-caveat route this
    #      gate replaces): stored primary 8.273 meV -- difference is the U_ei source.
    s96 = np.load(S96_NPZ, allow_pickle=True)                               # (local)
    p2["diag_s96_mbb_primary_meV"] = float(s96["part2_mbb_primary_meV"])
    p2["diag_s96_U_eisq"] = np.asarray(s96["part2_U_ei"], dtype=float) ** 2

    return p2


# ---------------------------------------------------------------------------
# Section 7 -- gate verdict (pre-registered operator, plan SS W5-2)
# ---------------------------------------------------------------------------
def evaluate_gate(p1: dict, p2: dict) -> str:
    """PASS: MAJORANA and m_bb_central < KamLAND-Zen and in NO funnel.
    FAIL: m_bb_central > KamLAND-Zen.
    INFO: DIRAC determination (m_bb NULL) or other pre-registered qualification."""
    if p1["determination"] != "MAJORANA":
        return "INFO"  # DIRAC-m_bb-NULL: definite structural result, no 0nubb signal
    if p2["mbb_central_eV"] > m_betabeta_KamLANDZen:
        return "FAIL"
    if p2["below_KamLANDZen"] and p2["in_NO_funnel"]:
        return "PASS"
    return "INFO"


def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str) -> dict:
    """PRINT the emit_verdict payload (the agent calls mcp__knowledge__emit_verdict).
    [VERIFY] trigger: NO sign/magnitude/regime 3-tuple fields."""
    payload = {
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
    }  # (local)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 8 -- plot
# ---------------------------------------------------------------------------
def make_plot(p1: dict, p2: dict, cc1: dict) -> None:
    fig, ax = plt.subplots(1, 2, figsize=(12.5, 5.2))

    # (a) Majorana-phase band + bound ladder
    a2_deg = p2["alpha2_grid"] * 180.0 / np.pi            # (local)
    G_meV = p2["mbb_grid_eV"] * 1e3                       # (local)
    lo_a3 = G_meV.min(axis=1)                             # (local) min over alpha_3
    hi_a3 = G_meV.max(axis=1)                             # (local) max over alpha_3
    ax[0].fill_between(a2_deg, lo_a3, hi_a3, color="C0", alpha=0.30,
                       label="Majorana-phase band (alpha_2 x alpha_3 scan)")
    ax[0].plot(a2_deg, hi_a3, color="C0", lw=1.0)
    ax[0].plot(a2_deg, lo_a3, color="C0", lw=1.0)
    ax[0].axhspan(FUNNEL_LO_EV * 1e3, FUNNEL_HI_EV * 1e3, color="blue", alpha=0.10,
                  label="pre-registered NO funnel [1.5, 4.5] meV")
    ax[0].axhline(m_betabeta_KamLANDZen * 1e3, color="red", ls="--",
                  label=f"KamLAND-Zen bound ({m_betabeta_KamLANDZen*1e3:.0f} meV, loose NME)")
    ax[0].axhline(m_betabeta_LEGEND200_reach * 1e3, color="orange", ls=":",
                  label=f"LEGEND-200 reach ({m_betabeta_LEGEND200_reach*1e3:.0f} meV)")
    ax[0].axhline(m_betabeta_nextgen_reach * 1e3, color="green", ls="-.",
                  label=f"next-gen reach floor ({m_betabeta_nextgen_reach*1e3:.0f} meV)")
    ax[0].plot([0.0], [p2["mbb_central_meV"]], "k*", ms=13,
               label=f"central (no phase) = {p2['mbb_central_meV']:.4g} meV")
    ax[0].set_yscale("log")
    ax[0].set_xlabel("Majorana phase alpha_2 [deg]")
    ax[0].set_ylabel("m_bb [meV]")
    ax[0].set_title(f"0nubb effective mass -- {p1['determination']} texture\n"
                    "S99 NO masses (m_1=0) x plan NuFit U_ei; delta_CP in {0,pi} degenerate")
    ax[0].legend(fontsize=7, loc="upper right")
    ax[0].grid(alpha=0.3)

    # (b) PART-1 machinery cross-check: re-run vs S96 stored
    labels = ["J^2-I", "JD-DJ", "Jg+gJ", "{g,D}", "anti-Tsym", "lin[C2,D]\n(pitfall)"]  # (local)
    keys = ["ko_J2", "ko_JD", "ko_Jg", "ko_anti_g32", "antilinear_Tsym", "linear_commutator"]  # (local)
    s96 = np.load(S96_NPZ, allow_pickle=True)  # (local)
    v_rerun = [max(p1[k], 1e-18) for k in keys]            # (local)
    v_s96 = [max(float(s96[k]), 1e-18) for k in keys]      # (local)
    x = np.arange(len(labels))                              # (local)
    ax[1].bar(x - 0.18, v_rerun, width=0.36, color="C2", label="this gate (re-run)")
    ax[1].bar(x + 0.18, v_s96, width=0.36, color="C4", label="S96 stored npz")
    ax[1].axhline(TOL_MAJ, color="k", ls="--", lw=0.8, label="1e-12 floor")
    ax[1].set_yscale("log")
    ax[1].set_xticks(x)
    ax[1].set_xticklabels(labels, rotation=30, ha="right", fontsize=8)
    ax[1].set_ylabel("residual")
    ax[1].set_title(f"KO-dim-6 axioms: re-run vs S96 (match={cc1['all_match']})\n"
                    f"determination={p1['determination']} (S96: {cc1['s96_determination']}); "
                    f"frob reldiff={cc1['frob_reldiff']:.1e}")
    ax[1].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 -- main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    p1 = compute_part1()
    cc1 = crosscheck_part1_vs_s96(p1)
    ccc = crosscheck_cache_L12(p1)
    p2 = compute_part2()

    # ---- structured report ----
    print("=" * 78)
    print(f"{GATE_ID}: KO-dim-6 Pfaffian Majorana texture -> m_bb vs 0nubb bounds")
    print("=" * 78)
    print(f"  tau_fold = {TAU}, M_KK = {M_KK:.6e} GeV, L_max = {L_MAX}")

    print("\n--- PART 1: Majorana-vs-Dirac determination (S96 machinery re-run) ---")
    print(f"  KO-dim-6 axioms (J^2/JD/Jg/{{g,D}}/anti-Tsym) max residual: {cc1['ko_residual_max_rerun']:.2e}")
    print(f"  linear-[C2,D_F] pitfall contrast : {p1['linear_commutator']:.6f} (!=0, NOT a signal; S96 {cc1['linear_commutator_s96']:.6f})")
    print(f"  (1,1,0) singlet                  : state {p1['SINGLET']}, weight {list(p1['singlet_weight'])}")
    print(f"  C1-conjugate idx / same chirality: {p1['cc_idx']} / {p1['cc_same_chirality']}")
    print(f"  Dirac partners in H_K-           : {p1['n_dirac_partner']} => Dirac {'POSSIBLE' if p1['dirac_possible'] else 'IMPOSSIBLE'}")
    print(f"  H_F+ Majorana block Frobenius    : {p1['maj_block_frob']:.10f} > tol {TOL_MAJ:.0e}")
    print(f"  bare bilinear |<Jxi|D_F|xi>|     : {p1['m_M_bare_abs']:.2e} (T4: tree=0; mass seesaw-generated)")
    print(f"  >>> DETERMINATION                : {p1['determination']}")
    print(f"  CC-P1 vs S96 stored npz          : determination_match={cc1['determination_match']}, "
          f"frob_reldiff={cc1['frob_reldiff']:.2e}, all_match={cc1['all_match']}")
    print(f"  CC-CACHE L12 (0,0) sector        : n_sectors={ccc['n_sectors']}, "
          f"maxdiff={ccc.get('cache00_maxdiff', float('nan')):.2e}, match={ccc['cache00_match']} "
          f"(min|eval| cache {ccc.get('cache00_min_abs', float('nan')):.8f} vs D_F {ccc.get('DF_min_abs', float('nan')):.8f})")

    print("\n--- PART 2: m_bb = |sum U_ei^2 m_i| (Route-A) ---")
    print(f"  m_i [eV] (S99 osc-anchored, NO)  : {list(np.round(p2['m_i_eV'], 7))} "
          f"(plan-triple maxdiff {p2['plan_triple_maxdiff']:.1e}; ordering_NO={p2['ordering_NO']})")
    print(f"  implied dm2_21 / dm2_31 [eV^2]   : {p2['dm2_21_implied']:.4e} / {p2['dm2_31_implied']:.4e}")
    print(f"    vs NuFit-6.0 canonical pins    : reldiff {p2['dm2_21_reldiff_vs_NuFit']:.4f} / "
          f"{p2['dm2_31_reldiff_vs_NuFit']:.4f} (S99 anchored to PDG-style dm2; <2.5%)")
    print(f"  PMNS pins (plan)                 : sin2_th12={SIN2_TH12}, sin2_th13={SIN2_TH13}")
    print(f"  U_ei^2 = [c12c13, s12c13, s13]^2 : {list(np.round(p2['U_eisq'], 6))}")
    print(f"  electron-row closure |sum-1|     : {p2['unitarity_resid']:.2e}")
    print(f"  terms U_ei^2 m_i [eV]            : {list(np.round(p2['terms_eV'], 8))}")
    print(f"  m_bb CENTRAL (no phase)          : {p2['mbb_central_eV']:.6e} eV = {p2['mbb_central_meV']:.4f} meV")
    print(f"  delta_CP {{0,pi}} degeneracy     : |m_bb(0)-m_bb(pi)| = {p2['deltaCP_degeneracy_absdiff']:.2e} (exact)")
    print(f"  Majorana-phase band (240x40)     : [{p2['mbb_band_lo_eV']*1e3:.4f}, {p2['mbb_band_hi_eV']*1e3:.4f}] meV")
    print(f"    analytic band cross-check      : lo absdiff {p2['band_lo_absdiff']:.2e}, hi absdiff {p2['band_hi_absdiff']:.2e}")
    print(f"    central == band max (no-cancel): {p2['central_is_band_max']}")
    print(f"  plan hand-substitution 3.69e-3   : reldiff {p2['plan_handsub_reldiff']:.4f}")
    print(f"  KamLAND-Zen {m_betabeta_KamLANDZen*1e3:.0f} meV       : below={p2['below_KamLANDZen']} (x{p2['margin_KamLANDZen']:.1f} margin)")
    print(f"  LEGEND-200 reach {m_betabeta_LEGEND200_reach*1e3:.0f} meV    : below={p2['below_LEGEND200']} (x{p2['margin_LEGEND200']:.1f})")
    print(f"  next-gen floor {m_betabeta_nextgen_reach*1e3:.0f} meV      : below={p2['below_nextgen']} (x{p2['margin_nextgen']:.1f}; "
          f"detection above funnel falsifies)")
    print(f"  NO funnel [{FUNNEL_LO_EV*1e3:.1f}, {FUNNEL_HI_EV*1e3:.1f}] meV     : central in-funnel={p2['in_NO_funnel']}, "
          f"full band inside={p2['band_inside_funnel']}")
    print("\n  --- diagnostics (NON-GATING) ---")
    print(f"  (d1) NuFit-6.0 dm2-implied masses: m_bb = {p2['diag_mbb_NuFit_dm2_eV']*1e3:.4f} meV")
    print(f"  (d2) NuFit-6.0 IC19+SK angles    : m_bb = {p2['diag_mbb_NuFit60_angles_eV']*1e3:.4f} meV "
          f"(version sensitivity {p2['diag_angle_sensitivity_rel']*100:.2f}%)")
    print(f"  (d3) S96 W4-2 framework-U_ei route: {p2['diag_s96_mbb_primary_meV']:.3f} meV "
          f"(U_ei source difference; W4-2 angles were the INFO caveat)")

    verdict = evaluate_gate(p1, p2)

    # ---- value string (publication_precision=4 on m_bb; meV) ----
    if p1["determination"] == "MAJORANA":
        state = "MAJORANA-admitted-m_bb-funnel" if p2["in_NO_funnel"] else "MAJORANA-admitted"  # (local)
        val = (
            f"{state};m_bb_central={p2['mbb_central_meV']:.4g}meV;"
            f"band=[{p2['mbb_band_lo_eV']*1e3:.4g},{p2['mbb_band_hi_eV']*1e3:.4g}]meV;"
            f"KamLAND-Zen={m_betabeta_KamLANDZen*1e3:.0f}meV(x{p2['margin_KamLANDZen']:.1f}-below);"
            f"LEGEND200={m_betabeta_LEGEND200_reach*1e3:.0f}meV(x{p2['margin_LEGEND200']:.1f}-below);"
            f"nextgen-floor={m_betabeta_nextgen_reach*1e3:.0f}meV(x{p2['margin_nextgen']:.1f}-below;"
            f"detection-above-funnel-falsifies);"
            f"in-NO-funnel[1.5,4.5]meV={p2['in_NO_funnel']};"
            f"deltaCP{{0,pi}}-degenerate;"
            f"m_i=S99-osc-anchored-trackB-residual-Dirac-scale-caveat(W5-1-INFO);"
            f"scope=observable-leg-only-D5-prose-workshop-deferred"
        )  # (local)
    else:
        val = "DIRAC-m_bb-NULL;lepton-number-conserved;scope=observable-leg-only"  # (local)

    tag = emit_4tuple(val, SCHEME, CONVENTION, L_MAX)
    print("\n" + tag)

    # ---- save npz (full float64) ----
    save = {}  # (local)
    for k, v in p1.items():
        save[f"p1_{k}"] = v
    for k, v in cc1.items():
        save[f"cc1_{k}"] = v
    for k, v in ccc.items():
        save[f"ccache_{k}"] = v
    for k, v in p2.items():
        save[f"p2_{k}"] = v
    save["value"] = val
    save["verdict"] = verdict
    save["audit_sha256"] = audit_sha
    save["content_sha256"] = content_sha
    save["tau_fold"] = TAU
    save["L_max"] = L_MAX
    save["sin2_th12_pin"] = SIN2_TH12
    save["sin2_th13_pin"] = SIN2_TH13
    save["funnel_lo_eV"] = FUNNEL_LO_EV
    save["funnel_hi_eV"] = FUNNEL_HI_EV
    save["bound_KamLANDZen_eV"] = m_betabeta_KamLANDZen
    save["bound_LEGEND200_eV"] = m_betabeta_LEGEND200_reach
    save["bound_nextgen_eV"] = m_betabeta_nextgen_reach
    np.savez(OUT_NPZ, **{k: (np.array(v, dtype=object) if isinstance(v, str) else v)
                         for k, v in save.items()})
    print(f"  saved npz: {OUT_NPZ.name}")

    make_plot(p1, p2, cc1)
    print(f"  saved png: {OUT_PNG.name}")

    print_verdict_payload(verdict, val, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # exit 0 regardless of scientific verdict (math-scripts.md exit-code rule)


if __name__ == "__main__":
    sys.exit(main())
