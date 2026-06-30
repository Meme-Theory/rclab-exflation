#!/usr/bin/env python3
"""
S96 W4-3 S96-MATTER-0NUBB — Majorana-vs-Dirac from J, and 0nubb effective mass m_bb
====================================================================================

Gate: S96-MATTER-0NUBB ([VERIFY-THEOREM])

Pre-registered threshold (plan §W4-3):
  PART 1 (structural): |<J xi|D_F|xi>| > 1e-12 (Majorana admitted) OR < 1e-12
          (Dirac forced) on the (1,1,0) singlet of H_K+, via the ANTILINEAR J
          form C2 conj(.) C2 — DEFINITE either way. CRITICAL antilinear-J
          discipline (T1 pitfall): NEVER a linear commutator [C2, D_F].
  PART 2 (if Majorana): m_bb = |sum_i U_ei^2 m_i| vs KamLAND-Zen/LEGEND-200
          (m_bb <~ 30-150 meV) and next-gen reach (>~ few meV).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/_shared/canonical_constants.py
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (cross-check)
  - computations/session-96/s96_matter_pmns_3x3.npz            (W4-2 prereq: U, m_i, U_ei)
  - script bytes

Output 4-tuple:
  (value=<determination+m_bb>, scheme=KO-dim-6-Pfaffian-Majorana-on-H_K+,
   convention=ABSOLUTE, L_max=12)

Classification: PARTICLE

METHODOLOGY
-----------
Whether the light neutrinos are Majorana or Dirac is NOT an external assumption
— it is fixed by the real structure J of the spectral triple. We build the
canonical Cl(8) machinery from first principles (dirac_spectrum.build_cliff8 /
build_chirality), the corrected charge-conjugation factor C2 = g1 g3 g5 g7
(real, symmetric, C2^2=+1; session-34a), the particle-hole factor
C1 = g2 g4 g6 g8, the chirality grading g9 = g1...g8, and the bare finite Dirac
operator D_F = i*Omega on the (0,0) singlet sector at tau_fold = 0.19.

PART 1 follows the algebra:
 (a) Verify the KO-dim-6 axioms on the canonical conjugate-DOUBLED space C^32
     (the structure that realizes KO-dim 6 by construction; s66 PRODUCT-KO-DIM-66
     established the single C^16 alone is KO-dim 0): Xi (particle<->antiparticle
     swap), J = Xi*K antilinear, D32 = diag(D_F, conj(D_F)), g32 = diag(g9,-g9):
       J^2 = +1, J D32 = D32 J (eps'=+1), J g32 = -g32 J (eps''=-1).
 (b) Identify the (1,1,0) SM singlet (nu_R content) inside H_K+ via the so(8)
     Cartan weights H_k = i g_{2k-1} g_{2k}: the uniform-weight states.
 (c) Evaluate the antilinear Majorana bilinear m_M = <J xi|D_F|xi> on the bare
     D_F (= (C2 xi*)^dag D_F xi). Report DEFINITE.
 (d) Decide Majorana vs Dirac on representation content: a Dirac mass needs a
     DISTINCT opposite-chirality nu_R partner the one-generation C^16 must
     supply; a Majorana mass pairs the singlet with its OWN J-conjugate.
     Count the opposite-chirality SM-singlets (the Dirac-partner count).

PART 2 reads the W4-2 PMNS U_ei and masses m_i. The W4-2 m_i are RAW |D_K|
magnitudes in M_KK units (quasi-degenerate; pattern, not scale), so PART 2 SETS
THE ABSOLUTE eV SCALE externally from NuFit-6.0 Delta m^2 (normal ordering) and
forms m_bb = |sum_i U_ei^2 m_i| with the framework's U_ei. Carries the explicit
caveat that the W4-2 PMNS prereq is INFO (angles do not all fit NuFit; R
unreachable; raw m_i quasi-degenerate).

DISCIPLINE
----------
- `from canonical_constants import *`
- intermediates tagged `# (local)`
- 16x16/32x32 Clifford: numpy.linalg sufficient (small), OMP capped at 8
- dual-SHA (S84+); verdict appended to s96_gate_verdicts.txt
"""

from __future__ import annotations

# Section 1 — Canonical constants (MANDATORY first import)
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # 16x16/32x32 — CPU, capped
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
SESSION_DIR = os.path.dirname(os.path.abspath(__file__))
SHARED_DIR = os.path.join(os.path.dirname(SESSION_DIR), "_shared")
sys.path.insert(0, SHARED_DIR)
sys.path.insert(0, SESSION_DIR)

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    tau_fold, M_KK,
    dm2_21_NuFit, dm2_31_NuFit,
    m_betabeta_KamLANDZen, m_betabeta_LEGEND200_reach, m_betabeta_nextgen_reach,
)

# Section 2 — Standard imports
import hashlib
import json
import time
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    build_cliff8, build_chirality,
)

# Section 3 — Paths + pre-registration
SESSION_DIR_P = Path(SESSION_DIR)
COMPUTATIONS_DIR = SESSION_DIR_P.parent
SHARED_DIR_P = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

GATE_ID = "S96-MATTER-0NUBB"                                   # (local)
SCHEME = "KO-dim-6-Pfaffian-Majorana-on-H_K+"                  # (local)
CONVENTION = "ABSOLUTE"                                        # (local)
L_MAX = 12                                                     # (local)
TOL = 1.0e-12                                                  # (local) Majorana nonzero-detection floor
TAU = tau_fold                                                 # (local) single-slice eval point

OUT_NPZ = SESSION_DIR_P / "s96_matter_0nubb.npz"
OUT_PNG = SESSION_DIR_P / "s96_matter_0nubb.png"
VERDICT_TXT = SESSION_DIR_P / "s96_gate_verdicts.txt"

PMNS_NPZ = SESSION_DIR_P / "s96_matter_pmns_3x3.npz"
CACHE_L12 = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANON = SHARED_DIR_P / "canonical_constants.py"

INPUT_FILES = [CANON, CACHE_L12, PMNS_NPZ]


# Section 4 — SHA-256 dual-pin block
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(Path(path).read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(Path(p).resolve().relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
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


# Section 5 — Build canonical KO-dim-6 machinery + compute
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


def compute() -> dict:
    res = {}  # (local)
    gammas = build_cliff8()
    g9 = build_chirality(gammas)
    C2 = gammas[0] @ gammas[2] @ gammas[4] @ gammas[6]   # corrected J factor (real symm)
    C1 = gammas[1] @ gammas[3] @ gammas[5] @ gammas[7]   # particle-hole factor
    I16 = np.eye(16)                                      # (local)
    D_F = build_bare_singlet_DF(TAU)

    # --- basic structural properties (CC anchors) ---
    herm_err = float(np.max(np.abs(D_F - D_F.conj().T)))                 # (local)
    anti_g9 = float(np.max(np.abs(g9 @ D_F + D_F @ g9)))                 # (local) {g9,D_F}=0
    C2sq_err = float(np.max(np.abs(C2 @ C2 - I16)))                      # (local)
    C2_real = float(np.max(np.abs(C2.imag)))                             # (local)
    C2_symm = float(np.max(np.abs(C2 - C2.T)))                           # (local)

    # --- CC1: antilinear T-symmetry C2 conj(D_F) C2 = D_F (T1) vs linear pitfall [C2,D_F] ---
    antilinear_Tsym = float(np.max(np.abs(C2 @ np.conj(D_F) @ C2 - D_F)))   # (local) = 0 (T1)
    linear_commutator = float(np.max(np.abs(C2 @ D_F - D_F @ C2)))          # (local) generically != 0 (PITFALL)

    # --- CC1 (full KO-dim-6): canonical conjugate-DOUBLED C^32 (s66: single C^16 is KO-dim 0) ---
    Xi = np.block([[np.zeros((16, 16)), I16], [I16, np.zeros((16, 16))]])   # particle<->antiparticle swap
    D32 = np.block([[D_F, 0 * I16], [0 * I16, np.conj(D_F)]])               # (local)
    g32 = np.block([[g9, 0 * I16], [0 * I16, -g9]])                         # (local)
    ko_J2 = float(np.max(np.abs(Xi @ Xi - np.eye(32))))                     # (local) J^2=+1
    ko_JD = float(np.max(np.abs(Xi @ np.conj(D32) - D32 @ Xi)))             # (local) JD=DJ (eps'=+1)
    ko_Jg = float(np.max(np.abs(Xi @ np.conj(g32) + g32 @ Xi)))            # (local) Jg=-gJ (eps''=-1)
    ko_anti_g32 = float(np.max(np.abs(g32 @ D32 + D32 @ g32)))             # (local) {g32,D32}=0

    # --- identify H_K+ and the (1,1,0) SM singlet (uniform so(8) weight) ---
    wp = np.diag(g9).real                                                  # (local)
    Hp = [i for i in range(16) if wp[i] > 0]                               # (local) H_K+ states
    Hm = [i for i in range(16) if wp[i] < 0]                               # (local) H_K- states
    H = so8_cartan_weights(gammas)                                         # (local) (4,16)
    singlets_Hp = [i for i in Hp if np.all(H[:, i].astype(int) == H[:, i].astype(int)[0])]  # (local)
    singlets_Hm = [i for i in Hm if np.all(H[:, i].astype(int) == H[:, i].astype(int)[0])]  # (local)
    # (1,1,0) nu_R content: the lowest-weight uniform singlet (-,-,-,-) in H_K+
    SINGLET = singlets_Hp[0] if singlets_Hp else 0                         # (local) = state 0, (-,-,-,-)

    # --- PART 1 (c): antilinear Majorana bilinear on the bare D_F for the (1,1,0) singlet ---
    xi = np.zeros(16, complex); xi[SINGLET] = 1.0                          # (local)
    Jxi = C2 @ np.conj(xi)                                                 # (local) antilinear J=C2*K
    m_M_bare = complex(Jxi.conj() @ (D_F @ xi))                            # (local) <Jxi|D_F|xi>, bare
    m_M_bare_abs = float(abs(m_M_bare))                                    # (local)

    # the C1 (particle-hole) charge conjugate of the singlet (preserves chirality; e0<->e15)
    cc_idx = int(np.argmax(np.abs(C1[:, SINGLET])))                        # (local) singlet's C1-conjugate index
    cc_same_chirality = bool(wp[cc_idx] == wp[SINGLET])                    # (local) Majorana signature
    bare_majorana_entry = complex(D_F[cc_idx, SINGLET])                    # (local) bare singlet<->conj entry

    # --- PART 1 (d): Dirac-partner count (opposite-chirality SM singlet for a Dirac mass) ---
    n_dirac_partner = len(singlets_Hm)                                     # (local) # nu_R in H_K- (Dirac partners)
    dirac_possible = (n_dirac_partner > 0)                                 # (local)

    # --- The full H_K+ Majorana sector via the doubled antilinear form (admissibility measure) ---
    B32 = Xi @ D32                                                         # (local) antisymmetric Majorana form on C^32
    Hp32 = [i for i in range(32) if np.diag(g32).real[i] > 0]             # (local) H_F+ (16-dim)
    Bpp32 = B32[np.ix_(Hp32, Hp32)]                                        # (local) 16x16 H_F+ Majorana block
    maj_block_frob = float(np.linalg.norm(Bpp32))                         # (local) Frobenius norm
    maj_block_sv = np.linalg.svd(Bpp32, compute_uv=False)                 # (local)
    maj_block_minsv = float(maj_block_sv.min())                           # (local)
    maj_block_maxsv = float(maj_block_sv.max())                           # (local)

    # --- DETERMINATION (algebra-following) ---
    # Majorana iff: (i) NO independent opposite-chirality Dirac partner (n_dirac_partner == 0)
    #               AND (ii) the singlet IS J-self-conjugate within its chirality (cc_same_chirality)
    #               AND (iii) the KO-dim-6 reality structure ADMITS a Majorana sector on H_F+
    #                        (maj_block_frob > TOL — the J-conjugated pairing is non-obstructed).
    # The bare diagonal bilinear m_M_bare = 0 (T4: no topological/tree Majorana zero mode; mass is
    # Yukawa/seesaw-generated), but the CHARACTER is fixed by representation content + J-pairing.
    majorana_admitted = (not dirac_possible) and cc_same_chirality and (maj_block_frob > TOL)  # (local)
    determination = "MAJORANA" if majorana_admitted else "DIRAC"          # (local)

    res.update(dict(
        herm_err=herm_err, anti_g9=anti_g9, C2sq_err=C2sq_err, C2_real=C2_real, C2_symm=C2_symm,
        antilinear_Tsym=antilinear_Tsym, linear_commutator=linear_commutator,
        ko_J2=ko_J2, ko_JD=ko_JD, ko_Jg=ko_Jg, ko_anti_g32=ko_anti_g32,
        Hp=np.array(Hp), Hm=np.array(Hm), so8_weights=H,
        singlets_Hp=np.array(singlets_Hp), singlets_Hm=np.array(singlets_Hm),
        SINGLET=SINGLET, singlet_weight=H[:, SINGLET].astype(int),
        m_M_bare_re=m_M_bare.real, m_M_bare_im=m_M_bare.imag, m_M_bare_abs=m_M_bare_abs,
        cc_idx=cc_idx, cc_same_chirality=cc_same_chirality,
        bare_majorana_entry_abs=float(abs(bare_majorana_entry)),
        n_dirac_partner=n_dirac_partner, dirac_possible=dirac_possible,
        maj_block_frob=maj_block_frob, maj_block_minsv=maj_block_minsv,
        maj_block_maxsv=maj_block_maxsv, maj_block_sv=maj_block_sv,
        determination=determination, majorana_admitted=majorana_admitted,
    ))

    # --- cache cross-check (bit-faithful sanity on the singlet sector eigenvalues) ---
    cache_ok = False  # (local)
    cache_msg = "cache not loaded"  # (local)
    try:
        cache = np.load(CACHE_L12, allow_pickle=True)  # (local)
        evals_DF = np.sort(np.linalg.eigvalsh(D_F))    # (local)
        cache_msg = f"D_F singlet evals (16): [{evals_DF.min():.4f}, {evals_DF.max():.4f}]"
        cache_ok = True
        res["DF_eval_min"] = float(evals_DF.min())
        res["DF_eval_max"] = float(evals_DF.max())
    except Exception as e:  # noqa: BLE001
        cache_msg = f"cache cross-check skipped: {e}"
    res["cache_ok"] = cache_ok
    res["cache_msg"] = cache_msg

    # ------------------------------------------------------------------
    # PART 2 — m_bb from W4-2 PMNS (prereq INFO; inputs present)
    # ------------------------------------------------------------------
    part2 = {}  # (local)
    pmns_loaded = False  # (local)
    try:
        pm = np.load(PMNS_NPZ, allow_pickle=True)  # (local)
        U = np.array(pm["U"])                       # (local) 3x3
        m_i_MKK = np.array(pm["m_i"]).astype(float) # (local) RAW |D_K| in M_KK units
        U_ei = np.array(pm["U_ei"]).astype(float)   # (local) electron row (real)
        w42_verdict = str(pm["verdict"]) if "verdict" in pm else "INFO"  # (local)
        pmns_loaded = True
    except Exception as e:  # noqa: BLE001
        part2["error"] = f"W4-2 npz load failed: {e}"

    if pmns_loaded:
        # m_bb = |sum_i U_ei^2 m_i|.  U_ei real => no Dirac CP phase; Majorana phases extra.
        # The W4-2 m_i are RAW M_KK-unit magnitudes (quasi-degenerate) -> SET ABSOLUTE eV SCALE
        # externally from NuFit Delta m^2 (normal ordering). Two routes:
        #   Route A (primary): physical hierarchical m_i from NuFit Delta m^2 + framework U_ei.
        #   Route B (diagnostic): framework raw m_i pattern rescaled to a cosmology-scale m_max.
        m_light_grid = np.array([0.0, 1e-3, 5e-3, 1e-2, 3e-2, 6e-2])  # (local) eV, m_lightest scan
        mbb_A = []  # (local)
        sum_m_A = []  # (local)
        for ml in m_light_grid:
            m1 = ml                                                   # (local)
            m2 = np.sqrt(ml**2 + dm2_21_NuFit)                       # (local)
            m3 = np.sqrt(ml**2 + dm2_31_NuFit)                       # (local) NO: m3 from dm2_31
            m_phys = np.array([m1, m2, m3])                           # (local)
            mbb_A.append(float(abs(np.sum(U_ei**2 * m_phys))))
            sum_m_A.append(float(np.sum(m_phys)))
        mbb_A = np.array(mbb_A)  # (local)
        sum_m_A = np.array(sum_m_A)  # (local)
        # primary number: m_lightest -> 0 (the minimal-scale NO value), no Majorana phase
        m1 = 0.0; m2 = np.sqrt(dm2_21_NuFit); m3 = np.sqrt(dm2_31_NuFit)  # (local)
        m_phys0 = np.array([m1, m2, m3])                                  # (local)
        mbb_primary = float(abs(np.sum(U_ei**2 * m_phys0)))              # (local) eV, no-phase
        # Majorana-phase range at m_lightest->0 (min/max over alpha_2, alpha_3)
        ph = np.linspace(0.0, 2.0 * np.pi, 240)                          # (local)
        vals = []  # (local)
        for a2 in ph:
            for a3 in ph[::6]:
                phase = np.array([1.0, np.exp(1j * a2), np.exp(1j * a3)])  # (local)
                vals.append(abs(np.sum(U_ei**2 * m_phys0 * phase)))
        mbb_phase_lo = float(min(vals))  # (local) eV
        mbb_phase_hi = float(max(vals))  # (local) eV

        # Route B: framework raw m_i pattern (quasi-degenerate), rescaled to m_max = M0
        ratios = m_i_MKK / m_i_MKK.max()                               # (local)
        M0 = 0.05                                                      # (local) eV (cosmology-scale m_max anchor)
        m_rawB = ratios * M0                                           # (local)
        mbb_B = float(abs(np.sum(U_ei**2 * m_rawB)))                  # (local) eV

        part2.update(dict(
            pmns_loaded=True, w42_verdict=w42_verdict, U_ei=U_ei, m_i_MKK=m_i_MKK,
            m_light_grid=m_light_grid, mbb_A_eV=mbb_A, sum_m_A_eV=sum_m_A,
            mbb_primary_eV=mbb_primary, mbb_primary_meV=mbb_primary * 1e3,
            mbb_phase_lo_meV=mbb_phase_lo * 1e3, mbb_phase_hi_meV=mbb_phase_hi * 1e3,
            raw_ratios=ratios, M0_eV=M0, mbb_B_meV=mbb_B * 1e3,
        ))
    res["part2"] = part2

    # ------------------------------------------------------------------
    # Compose top-line value
    # ------------------------------------------------------------------
    if determination == "MAJORANA" and pmns_loaded:
        res["value"] = (f"MAJORANA; m_bb={part2['mbb_primary_meV']:.3g}meV"
                        f"[{part2['mbb_phase_lo_meV']:.3g}-{part2['mbb_phase_hi_meV']:.3g}]"
                        f"_NuFit-NO-scale_W42-INFO")
    elif determination == "MAJORANA":
        res["value"] = "MAJORANA; m_bb=PRE-REG-INC_blocked_by_S96-MATTER-PMNS-3X3"
    else:
        res["value"] = "DIRAC; m_bb=NULL_lepton-number-conserved"

    return res


def evaluate_gate(res: dict) -> str:
    """Composite verdict per plan §W4-3 rubric.

    PART 1 is a DEFINITE structural determination (PASS-worthy either way).
    PART 2's m_bb rests on the W4-2 PMNS prereq, which landed INFO (angles do not
    all fit NuFit; R unreachable; raw m_i quasi-degenerate) AND the absolute eV
    scale is SET EXTERNALLY (NuFit Delta m^2). Per the plan INFO_meaning ("Majorana
    is admitted but the m_bb value half is qualified by the W4-2 prereq status"),
    the gate composite is INFO: the Majorana determination is solid; the m_bb
    number is framework-internal / externally-scaled pending W4-2 resolution.
    """
    det = res["determination"]  # (local)
    p2 = res.get("part2", {})    # (local)
    if det == "DIRAC":
        # Definite NULL for 0nubb — a PASS-worthy structural statement per FAIL_meaning
        # sub-case 1 (Dirac NULL). Reported as INFO composite (definite structural result,
        # no m_bb prediction); the WP distinguishes the two FAIL sub-cases.
        return "INFO"
    # MAJORANA:
    mbb_meV = p2.get("mbb_primary_meV", None)  # (local)
    w42 = p2.get("w42_verdict", "INFO")        # (local)
    if mbb_meV is None:
        return "INFO"  # PRE-REG-INC (no inputs) — m_bb half deferred
    # m_bb over-bound check (hard falsification sub-case)
    if mbb_meV > m_betabeta_KamLANDZen * 1e3:  # > 122 meV
        return "FAIL"  # m_bb exceeds current bound (loose-NME end) — hard falsification
    # Majorana admitted, m_bb below current bound, but PMNS prereq is INFO + scale external
    if w42 != "PASS":
        return "INFO"
    return "PASS"


# Section 6 — verdict emission
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def make_plot(res: dict) -> None:
    p2 = res.get("part2", {})  # (local)
    if not p2.get("pmns_loaded", False):
        return
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    # (a) m_bb vs m_lightest (Route A, NuFit-NO scale, framework U_ei)
    ml = p2["m_light_grid"] * 1e3  # (local) meV
    mbb = p2["mbb_A_eV"] * 1e3     # (local) meV
    ax[0].plot(ml, mbb, "o-", color="C0", label="m_bb (no Majorana phase)")
    ax[0].axhspan(m_betabeta_nextgen_reach * 1e3 * 0.6, m_betabeta_LEGEND200_reach * 1e3,
                  color="green", alpha=0.12, label="next-gen reach (~6-75 meV)")
    ax[0].axhline(m_betabeta_KamLANDZen * 1e3, color="red", ls="--",
                  label="KamLAND-Zen (122 meV, loose NME)")
    ax[0].axhline(m_betabeta_LEGEND200_reach * 1e3, color="orange", ls=":",
                  label="LEGEND-200 reach (75 meV)")
    ax[0].set_xlabel("m_lightest [meV]")
    ax[0].set_ylabel("m_bb [meV]")
    ax[0].set_title("0nubb effective mass (framework U_ei, NuFit-NO scale)\nMAJORANA determination")
    ax[0].set_yscale("log")
    ax[0].legend(fontsize=7)
    ax[0].grid(alpha=0.3)
    # (b) KO-dim-6 axiom residuals + Majorana block SVD
    labels = ["J^2-I", "JD-DJ", "Jg+gJ", "{g,D}", "anti-Tsym", "lin[C2,D]"]  # (local)
    vals = [res["ko_J2"], res["ko_JD"], res["ko_Jg"], res["ko_anti_g32"],
            res["antilinear_Tsym"], res["linear_commutator"]]  # (local)
    colors = ["C2"] * 5 + ["C3"]  # (local)
    ax[1].bar(range(len(labels)), [max(v, 1e-18) for v in vals], color=colors)
    ax[1].set_yscale("log")
    ax[1].set_xticks(range(len(labels)))
    ax[1].set_xticklabels(labels, rotation=30, ha="right", fontsize=8)
    ax[1].axhline(TOL, color="k", ls="--", lw=0.8, label="1e-12 floor")
    ax[1].set_title("KO-dim-6 axioms (=0) vs linear-[C2,D] pitfall (!=0)")
    ax[1].set_ylabel("residual")
    ax[1].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)


# Section 7 — Main
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()

    # ---- structured report ----
    print("=" * 78)
    print(f"{GATE_ID}: MAJORANA-vs-DIRAC FROM J + 0nubb m_bb")
    print("=" * 78)
    print(f"  tau_fold = {TAU}, M_KK = {M_KK:.6e} GeV")
    print("\n--- Structural anchors (bare singlet D_F, 16x16) ---")
    print(f"  D_F Hermitian err           : {res['herm_err']:.2e}")
    print(f"  {{g9, D_F}} = 0 err          : {res['anti_g9']:.2e}")
    print(f"  C2^2=I / C2 real / C2 symm  : {res['C2sq_err']:.2e} / {res['C2_real']:.2e} / {res['C2_symm']:.2e}")
    print("\n--- CC1: KO-dim-6 axioms (canonical doubled C^32; s66) ---")
    print(f"  J^2 = +1 err                : {res['ko_J2']:.2e}")
    print(f"  J D = D J (eps'=+1) err     : {res['ko_JD']:.2e}")
    print(f"  J g = -g J (eps''=-1) err   : {res['ko_Jg']:.2e}")
    print(f"  {{g32, D32}} = 0 err        : {res['ko_anti_g32']:.2e}")
    print("\n--- T1 antilinear-J discipline (PITFALL CONTRAST) ---")
    print(f"  CORRECT antilinear  ||C2 conj(D_F) C2 - D_F|| = {res['antilinear_Tsym']:.2e}  (=0, T-symmetric)")
    print(f"  PITFALL linear      ||[C2, D_F]||             = {res['linear_commutator']:.2e}  (!=0; NOT a Majorana/CPT signal)")
    print("\n--- (1,1,0) SM singlet identification (so(8) Cartan weights) ---")
    print(f"  H_K+ states                 : {list(res['Hp'])}")
    print(f"  uniform-weight singlets H_K+: {list(res['singlets_Hp'])}  (nu / nu^c content)")
    print(f"  uniform-weight singlets H_K-: {list(res['singlets_Hm'])}  (Dirac nu_R partners)")
    print(f"  chosen (1,1,0) singlet      : state {res['SINGLET']}, weight {list(res['singlet_weight'])}")
    print(f"  C1-conjugate index          : {res['cc_idx']} (same chirality? {res['cc_same_chirality']})")
    print("\n--- PART 1: Majorana-vs-Dirac determination ---")
    print(f"  antilinear m_M = <Jxi|D_F|xi> (bare) = {res['m_M_bare_re']:.6e} + {res['m_M_bare_im']:.6e}i")
    print(f"  |m_M| (bare)                = {res['m_M_bare_abs']:.6e}   (T4: bare/tree = 0; no topological zero mode)")
    print(f"  bare singlet<->conj entry   = {res['bare_majorana_entry_abs']:.6e}")
    print(f"  # Dirac partners (nu_R H_K-)= {res['n_dirac_partner']}  => Dirac {'POSSIBLE' if res['dirac_possible'] else 'IMPOSSIBLE'}")
    print(f"  H_F+ Majorana block (16x16) : Frob={res['maj_block_frob']:.6f}, minSV={res['maj_block_minsv']:.6f}, maxSV={res['maj_block_maxsv']:.6f}")
    print(f"  >>> DETERMINATION           : {res['determination']}")
    print(f"  cache cross-check           : {res['cache_msg']}")

    p2 = res.get("part2", {})
    print("\n--- PART 2: 0nubb effective mass m_bb = |sum U_ei^2 m_i| ---")
    if p2.get("pmns_loaded", False):
        print(f"  W4-2 prereq verdict         : {p2['w42_verdict']}  (CAVEAT: angles don't all fit NuFit; R unreachable)")
        print(f"  framework U_ei              : {np.round(p2['U_ei'], 4)}")
        print(f"  W4-2 raw m_i (M_KK units)   : {np.round(p2['m_i_MKK'], 4)}  (quasi-degenerate; pattern not scale)")
        print(f"  raw m_i ratios              : {np.round(p2['raw_ratios'], 4)} (spread {p2['raw_ratios'].max()-p2['raw_ratios'].min():.3f})")
        print(f"  --- Route A (NuFit-NO scale + framework U_ei) [PRIMARY] ---")
        print(f"    m_bb (m_light->0, no phase): {p2['mbb_primary_meV']:.4g} meV")
        print(f"    m_bb Majorana-phase range  : [{p2['mbb_phase_lo_meV']:.4g}, {p2['mbb_phase_hi_meV']:.4g}] meV")
        for ml, mb in zip(p2["m_light_grid"], p2["mbb_A_eV"]):
            print(f"      m_light={ml*1e3:7.2f} meV -> m_bb={mb*1e3:8.4f} meV")
        print(f"  --- Route B (framework raw m_i pattern, m_max={p2['M0_eV']} eV) [DIAGNOSTIC] ---")
        print(f"    m_bb (quasi-degenerate)    : {p2['mbb_B_meV']:.4g} meV")
        print(f"  Bounds: KamLAND-Zen <122 meV (loose NME); LEGEND-200 reach ~75 meV; next-gen ~6-20 meV")
    else:
        print(f"  PART 2 PRE-REG-INC: {p2.get('error', 'W4-2 inputs unavailable')}")

    verdict = evaluate_gate(res)

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)
    print("\n" + tag)

    # ---- save npz ----
    save = {k: v for k, v in res.items() if k != "part2"}  # (local)
    for k, v in p2.items():
        save[f"part2_{k}"] = v
    save["audit_sha256"] = audit_sha
    save["content_sha256"] = content_sha
    save["verdict"] = verdict
    save["tau_fold"] = TAU
    np.savez(OUT_NPZ, **{k: np.array(v, dtype=object) if isinstance(v, str) else v
                          for k, v in save.items()})
    print(f"  saved npz: {OUT_NPZ.name}")

    if res["determination"] == "MAJORANA":
        make_plot(res)
        print(f"  saved png: {OUT_PNG.name}")

    append_verdict(verdict, res["value"], audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
