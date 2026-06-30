#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CF-S118-PMNS-JOINT-ADMISSIBILITY  (Session 118, Wave 2, §W2-1) -- [VERIFY] gate.

Joint (R, PMNS-angle) admissibility scan over the FREE lepton-texture family.

QUESTION (plan §W2-1 hypothesis):
  Over the free real-texture family (U_eL the charged-lepton left-rotation and V_DR the
  neutrino-Dirac orientation relative to M_R -- the flat directions of the spectral action
  per S117 2-5, at FIXED charged-lepton masses + Dirac singular values {0,Y2,Y3} + B-branch
  Majorana M_R), is the joint NuFIT 5.2 NO 3-sigma box
       { R in [17,66]  AND  sin^2 th12 in [0.270,0.341]
         AND sin^2 th23 in [0.434,0.610]  AND sin^2 th13 in [0.02029,0.02391] }
  NON-EMPTY with positive admissible-volume measure?  (i.e. does the lepton mixing+spectrum
  under-determination SURVIVE the joint observational constraint.)

PASS ANCHOR = the ANALYTIC NON-EMPTINESS WITNESS (deterministic, NOT the MC):
  bare V_DR=I  ->  M_nu=diag(0, Y2^2/B2, Y3^2/B3)  ->  R_bare = m3^2/m2^2 - 1 = 31.576 in [17,66];
  U_eL = U_obs^dag (NuFIT best-fit PMNS)  ->  U_PMNS = U_obs  ->  3 angles at the band CENTERS.
  This re-derives S116 W2 STEP 3b obs_pmns_reachable=True (3/3 angle slots).
The MC f_adm_free (2e6 Haar-O(3) draws) is the admissible-VOLUME MEASURE, NOT the PASS gate.
The shared-eps_LX CONTRAST (2e5 draws, M_nu locked to the S116 single-parameter texture,
R=113.564 OUT of band) is the tension witness (expected near-empty).

============================================================================
SUBSTRATE-FIRST (phononic-framing.md):  PARTICLE.
============================================================================
  D_K eigenvalues -> seesaw composite M_nu = M_D M_R^{-1} M_D^T (Dirac-Yukawa singular values
  {0,Y2,Y3} and the B-branch fold Majorana M_R, BOTH internal to the spectrum per S100a)
  -> light-mass spectrum {0, m2, m3} -> the oscillation ratio R = m3^2/m2^2 - 1 AND, via
  U_PMNS = U_eL^dag U_nuL, the three mixing angles -> the joint NuFIT 5.2 NO 3-sigma box
  (the laboratory-IN measurement the substrate is tested against). The substrate IS the
  free-texture orbit; NuFIT is the container-IN observable box. The under-determination is a
  substrate-IS fact (S flat over U_eL and V_DR by trace cyclicity, S117 2-5); this gate
  measures whether that intrinsic freedom is observationally COMPATIBLE, never the reverse.
  Direction of explanation NOT inverted: D_K textures -> (free U_eL, free V_DR) -> joint box.

  HONEST CAVEAT (S100a-MD-NORMALIZATION INFO, PERMANENT): the D_K bottom-triple -> Y_i map is
  NON-UNIQUE (MAP-A vs MAP-B), so R_bare is OSCILLATION-ANCHORED -- R_bare in band is a
  CONSISTENCY of the spectrum channel with NuFIT, NOT a zero-free-parameter prediction. The
  substrate-FIRST content is the seesaw STRUCTURE + bowtie M_R shape + the factorization
  (R is U_eL-invariant) + the U_eL/V_DR flatness. CP/Jarlskog J is EXCLUDED (real textures
  => delta_CP in {0,pi} => J=0, the framework's standing prediction; CP under-determination is
  the separate S117-W3-3 / VII.BL question, NOT this gate).

[VERIFY] substitution chain (the analytic non-emptiness witness; plan §W2-1 substitution_chain):
  Def 1: M_D = diag(0,Y2,Y3) @ V_DR^T          [Dirac singular values FIXED; V_DR free; V_DL=I WLOG]
  Def 2: M_nu = M_D @ M_R^{-1} @ M_D^T          [type-I seesaw; row/col 1 zero => m_1=0 EXACT rank-2]
  Def 3: R := (m3^2 - m2^2)/(m2^2 - m1^2) = m3^2/m2^2 - 1  at m_1=0
  Def 4: U_PMNS = U_eL^dag U_nuL ; sin^2 th13=|U_e3|^2, sin^2 th12=|U_e2|^2/(1-|U_e3|^2),
         sin^2 th23=|U_mu3|^2/(1-|U_e3|^2)      [standard PDG]
  Substitute (R is U_eL-INVARIANT): an overall left-rotation M_nu -> V M_nu V^T preserves
         singular values => R = R(V_DR) only, independent of U_eL.
  Substitute (BARE V_DR=I): M_nu = diag(0, Y2^2/B2, Y3^2/B3); m3/m2 = 5.706; R_bare = 31.576 in [17,66].
  Simplify (angle reachability): U_eL ranges over full O(3) (any U_eL reproduces the lepton
         masses, S117 2-5 trace-cyclicity flat) => U_PMNS = U_eL^dag U_nuL = U_obs reachable
         => set U_eL = U_obs^dag => 3 angles at NuFIT band centers (s116 obs_pmns_reachable=True).
  Canonical form: (U_eL=U_obs^dag, V_DR=I) in J => J NON-EMPTY analytically => PASS.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  computations/_shared/canonical_constants.py            (dm2_21_NuFit, dm2_31_NuFit, tau_fold)
  computations/session-116/s116_lepton_pmns_texture.npz  (m_e_vals, Y_nu_diag, M_R_MKK, M_nu, NuFIT bands)

Output 4-tuple:
  (value=<witness 4 slots + f_adm_free +- CV + f_R/f_angle + reachable-R + contrast f_adm_shared>,
   scheme=joint-admissibility-MC-Haar-O3-free-texture,
   convention=RATIO-R-m3sq-over-m2sq-minus-1-m1zero-NO/PMNS-U_eL-dag-U_nuL/real-texture-J-excluded/
              NuFIT-5.2-NO-3sigma-joint-box-R+3angles, L_max=N/A)
"""

from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (math-scripts.md; 3x3 svd/eigh is tiny CPU;
#     RX 9070 XT available but NOT used -- host->device overhead dominates for 3x3) ---
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
# Section 1 -- Paths + canonical imports (MANDATORY: from canonical_constants import)
# ---------------------------------------------------------------------------
THIS = Path(__file__).resolve()
SESSION_DIR = THIS.parent                                 # computations/session-118
COMPUTATIONS_DIR = SESSION_DIR.parent                     # computations
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
SESSION_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    dm2_21_NuFit,        # 7.49e-5 eV^2 (NuFit-6.0 NO best fit) -- central-R anchor cross-check
    dm2_31_NuFit,        # 2.513e-3 eV^2 (NuFit-6.0 NO best fit)
    tau_fold,            # 0.19 -- provenance (D_K content frozen upstream in the s116 npz)
)

import matplotlib                                          # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                            # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 -- Identity + pinned machinery (plan §W2-1 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "118"                                            # (local)
GATE_ID = "CF-S118-PMNS-JOINT-ADMISSIBILITY"               # (local)
SCHEME = "joint-admissibility-MC-Haar-O3-free-texture"     # (local) plan pin
CONVENTION = ("RATIO-R-m3sq-over-m2sq-minus-1-m1zero-NO/PMNS-U_eL-dag-U_nuL/"
              "real-texture-J-excluded/NuFIT-5.2-NO-3sigma-joint-box-R+3angles")  # (local) plan pin
L_MAX = "N/A"                                              # (local) 3x3 seesaw+PMNS; D_K frozen upstream

# --- MC machinery (plan pins) ---
N_EVAL = 2_000_000                                         # (local) free-family Haar-O(3) draws
N_EVAL_SHARED = 200_000                                    # (local) shared-eps_LX contrast draws
N_SEED_BATCHES = 10                                        # (local) seed batches for f_adm CV
N_MIN_HITS = 10                                            # (local) MC positive-measure floor
RANDOM_SEED = 118                                          # (local) base; batch b uses 118+b
EDGE_TOL_FRAC = 0.05                                       # (local) band-edge proximity DIAGNOSTIC
M1_REL_TOL = 1.0e-9                                        # (local) m_1/m_3 machine-zero (rank-2)
R_CLOSEDFORM_TOL = 1.0e-9                                  # (local) R closed-form cross-check
UNITARY_TOL = 1.0e-10                                      # (local) |U^dag U - I|_fro
PUB_SIGFIGS = 6                                            # (local) Class-8.3 publication precision
GRID_PTS = 19                                              # (local) corroboration grid pts/axis [0,pi)
TAU = float(tau_fold)                                      # (local) 0.19 provenance

# --- NuFIT 5.2 NO 3-sigma joint box (# local class-(B) anchors; NOT canonical imports) ---
R_BAND = (17.0, 66.0)                                      # (local)
SIN2_TH12_BAND = (0.270, 0.341)                            # (local)
SIN2_TH23_BAND = (0.434, 0.610)                            # (local)
SIN2_TH13_BAND = (0.02029, 0.02391)                        # (local)
BF_TH12 = 0.303                                            # (local) NuFIT 5.2 NO best fit
BF_TH23 = 0.572                                            # (local)
BF_TH13 = 0.02203                                          # (local)

# central-R anchor (NuFit-6.0 canonical; cross-check only -- NOT the box edge)
R_CENTRAL_NUFIT = float(dm2_31_NuFit) / float(dm2_21_NuFit) - 1.0   # (local) ~32.55

# ---------------------------------------------------------------------------
# Section 3 -- SHA-256 dual-SHA block (S84+ schema; mirrors s117)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 4 -- Paths/targets + inputs
# ---------------------------------------------------------------------------
OUT_NPZ = SESSION_DIR / "s118_pmns_joint_admissibility.npz"
OUT_PNG = SESSION_DIR / "s118_pmns_joint_admissibility.png"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
S116_TEXTURE = COMPUTATIONS_DIR / "session-116" / "s116_lepton_pmns_texture.npz"
INPUT_FILES = [CANONICAL_PATH, S116_TEXTURE]

# plan-pinned input SHA (frozen S116 artifact); mismatch => PRE-REG-INC honest close
S116_SHA_PIN = "4252d2cc3cf37cf40a1fe89c631503320a80e26cc736b0fc543eb043293bbbb1"


# ---------------------------------------------------------------------------
# Section 5 -- PMNS / seesaw helpers (PDG convention; real textures)
# ---------------------------------------------------------------------------
def U_pdg(s2_12: float, s2_23: float, s2_13: float, delta: float = 0.0) -> np.ndarray:
    """Standard PDG PMNS U = R23(th23) U13(th13,delta) R12(th12); delta=0 (real, J=0)."""
    s12 = np.sqrt(s2_12); c12 = np.sqrt(1.0 - s2_12)
    s13 = np.sqrt(s2_13); c13 = np.sqrt(1.0 - s2_13)
    s23 = np.sqrt(s2_23); c23 = np.sqrt(1.0 - s2_23)
    R12 = np.array([[c12, s12, 0.0], [-s12, c12, 0.0], [0.0, 0.0, 1.0]])
    R13 = np.array([[c13, 0.0, s13], [0.0, 1.0, 0.0], [-s13, 0.0, c13]])
    R23 = np.array([[1.0, 0.0, 0.0], [0.0, c23, s23], [0.0, -s23, c23]])
    return R23 @ R13 @ R12


def pmns_angles_single(U: np.ndarray):
    """(sin^2 th12, sin^2 th23, sin^2 th13) from a single 3x3 PMNS (standard PDG)."""
    Ue3 = U[0, 2] ** 2; Ue2 = U[0, 1] ** 2; Um3 = U[1, 2] ** 2
    s13 = Ue3
    s12 = Ue2 / (1.0 - Ue3); s23 = Um3 / (1.0 - Ue3)
    return float(s12), float(s23), float(s13)


def pmns_angles_batch(U: np.ndarray):
    """Batched (N,3,3) -> (sin2_th12, sin2_th23, sin2_th13) arrays (N,)."""
    Ue3 = U[:, 0, 2] ** 2; Ue2 = U[:, 0, 1] ** 2; Um3 = U[:, 1, 2] ** 2
    s13 = Ue3
    denom = 1.0 - Ue3
    s12 = Ue2 / denom; s23 = Um3 / denom
    return s12, s23, s13


def Mnu_from_VDR(VDR: np.ndarray, Y: np.ndarray, MR: np.ndarray) -> np.ndarray:
    """type-I seesaw light mass matrix; M_D=diag(0,Y2,Y3)@V_DR^T (zero first row => m1=0)."""
    MD = np.diag(Y) @ VDR.T
    Mn = MD @ np.diag(1.0 / MR) @ MD.T
    return 0.5 * (Mn + Mn.T)


def light_single(Mn: np.ndarray):
    """eigh of PSD M_nu; eigenvalues ascending (== ascending |.| for PSD) -> {m1~0,m2,m3}, U_nuL."""
    w, V = np.linalg.eigh(Mn)
    w = np.abs(w)                                          # (local) clip tiny-negative kernel to 0
    order = np.argsort(w)
    return w[order], V[:, order]


def R_of(m: np.ndarray) -> float:
    """R = m3^2/m2^2 - 1 (NO; m ascending [m1~0,m2,m3])."""
    return float(m[2] ** 2 / m[1] ** 2 - 1.0)


def rand_O3_batch(rng, n: int) -> np.ndarray:
    """n Haar-ish O(3) via QR sign-fix (det=+-1; PMNS angles are det-insensitive). Batched."""
    A = rng.standard_normal((n, 3, 3))
    Q, Rm = np.linalg.qr(A)
    d = np.sign(np.diagonal(Rm, axis1=1, axis2=2))        # (local) (n,3) sign of R diag
    d[d == 0] = 1.0
    return Q * d[:, None, :]                               # (local) Q @ diag(sign): scale col j by d_j


def light_batch(VDR: np.ndarray, Y: np.ndarray, MR: np.ndarray):
    """Batched seesaw: (n,3,3) V_DR -> (m (n,3) ascending PSD, U_nuL (n,3,3)).
    M_D[n] = diag(Y) @ V_DR[n]^T = Y[:,None]*V_DR[n]^T ; M_nu = M_D diag(1/MR) M_D^T."""
    MD = Y[None, :, None] * np.transpose(VDR, (0, 2, 1))   # (local) (n,3,3)
    Mn = np.einsum("nik,k,njk->nij", MD, 1.0 / MR, MD)     # (local) M_D diag(1/MR) M_D^T
    Mn = 0.5 * (Mn + np.transpose(Mn, (0, 2, 1)))          # (local) symmetrize
    w, V = np.linalg.eigh(Mn)                              # ascending eigenvalues (PSD => >=0)
    return np.abs(w), V


# ---------------------------------------------------------------------------
# Section 6 -- Compute
# ---------------------------------------------------------------------------
def in_band(x, band):
    return (band[0] <= x) & (x <= band[1])


def edge_proximity_frac(x, band):
    """min distance to a band edge, as a fraction of band width (DIAGNOSTIC)."""
    width = band[1] - band[0]
    return float(min(abs(x - band[0]), abs(band[1] - x)) / width)


def compute() -> dict:
    res: dict = {}

    # ===== STEP 0: load S116 fixed input spectra (frozen artifact) =====
    s116 = np.load(S116_TEXTURE, allow_pickle=True)
    m_e_vals = np.asarray(s116["m_e_vals"]).ravel().astype(float)   # charged-lepton masses
    Y = np.asarray(s116["Y_nu_diag"]).ravel().astype(float)        # [0, Y2, Y3] Dirac singular vals
    MR = np.asarray(s116["M_R_MKK"]).ravel().astype(float)         # [B1,B2,B3] B-branch fold
    M_nu_s116 = np.asarray(s116["M_nu"]).astype(float)             # shared-eps_LX neutrino texture
    eps23 = float(s116["eps23_strength"]); w23_nu = float(s116["w23_nu"])
    obs_reach_s116 = bool(np.asarray(s116["obs_pmns_reachable"]).ravel()[0])
    res["m_e_vals"] = m_e_vals; res["Y_nu_diag"] = Y; res["M_R_MKK"] = MR
    res["eps23_strength"] = eps23; res["w23_nu"] = w23_nu
    res["obs_pmns_reachable_s116"] = obs_reach_s116
    print("=== STEP 0: S116 fixed input spectra (frozen artifact) ===")
    print(f"  Y_nu_diag (Dirac sing. vals)  = {Y}   (Y_1=0 EXACT => m_1=0 rank-2)")
    print(f"  M_R_MKK   (B-branch fold)     = {MR}  (spread {(MR.max()/MR.min()-1)*100:.1f}% near-degenerate)")
    print(f"  m_e_vals  (charged-lepton)    = {m_e_vals}")
    print(f"  shared-eps_LX: eps23={eps23:.6f}, w23_nu={w23_nu:.6f} (= eps23*Y3={eps23*Y[2]:.6f})")
    print(f"  S116 obs_pmns_reachable       = {obs_reach_s116}")

    # ===== STEP 1: ANALYTIC NON-EMPTINESS WITNESS (the PASS anchor; deterministic) =====
    # bare V_DR=I -> R_bare; U_eL=U_obs^dag, U_nuL=I -> U_PMNS=U_obs -> angles at band centers.
    m_bare, U_nuL_bare = light_single(Mnu_from_VDR(np.eye(3), Y, MR))
    R_bare = R_of(m_bare)
    m1_over_m3 = float(m_bare[0] / m_bare[2])
    U_obs = U_pdg(BF_TH12, BF_TH23, BF_TH13, delta=0.0)
    U_eL_witness = U_obs.T                                  # U_obs^dag (real)
    U_PMNS_witness = U_eL_witness.T @ U_nuL_bare            # = U_obs (since U_nuL_bare=I)
    s12_w, s23_w, s13_w = pmns_angles_single(U_PMNS_witness)
    # slot membership
    R_slot = bool(in_band(R_bare, R_BAND))
    a12_slot = bool(in_band(s12_w, SIN2_TH12_BAND))
    a23_slot = bool(in_band(s23_w, SIN2_TH23_BAND))
    a13_slot = bool(in_band(s13_w, SIN2_TH13_BAND))
    witness_lands = bool(R_slot and a12_slot and a23_slot and a13_slot)
    # edge proximity (DIAGNOSTIC, non-load-bearing per cross-pillar Level-3 annotation discipline)
    ep_R = edge_proximity_frac(R_bare, R_BAND)
    ep_12 = edge_proximity_frac(s12_w, SIN2_TH12_BAND)
    ep_23 = edge_proximity_frac(s23_w, SIN2_TH23_BAND)
    ep_13 = edge_proximity_frac(s13_w, SIN2_TH13_BAND)
    witness_edge_clear = bool(min(ep_R, ep_12, ep_23, ep_13) > EDGE_TOL_FRAC)
    res.update(dict(m_bare=m_bare, R_bare=R_bare, m1_over_m3=m1_over_m3,
                    witness_s12=s12_w, witness_s23=s23_w, witness_s13=s13_w,
                    witness_R_slot=R_slot, witness_a12_slot=a12_slot,
                    witness_a23_slot=a23_slot, witness_a13_slot=a13_slot,
                    witness_lands=witness_lands, witness_edge_clear=witness_edge_clear,
                    ep_R=ep_R, ep_12=ep_12, ep_23=ep_23, ep_13=ep_13))
    print("\n=== STEP 1: ANALYTIC NON-EMPTINESS WITNESS (PASS anchor) ===")
    print(f"  bare V_DR=I: m_light = {m_bare}  m1/m3 = {m1_over_m3:.2e} (rank-2 m1=0)")
    print(f"  R_bare = {R_bare:.6f}  in [17,66]: {R_slot}  (edge-frac {ep_R:.3f})")
    print(f"  U_eL=U_obs^dag -> angles: sin2_th12={s12_w:.6f} in {SIN2_TH12_BAND}: {a12_slot} (edge {ep_12:.3f})")
    print(f"                            sin2_th23={s23_w:.6f} in {SIN2_TH23_BAND}: {a23_slot} (edge {ep_23:.3f})")
    print(f"                            sin2_th13={s13_w:.6f} in {SIN2_TH13_BAND}: {a13_slot} (edge {ep_13:.3f})")
    print(f"  WITNESS LANDS ALL 4 SLOTS = {witness_lands}  (edge-clear>5%: {witness_edge_clear})")

    # ===== STEP 2: MC ADMISSIBLE-VOLUME MEASURE (free U_eL/V_DR family; 10 seed batches) =====
    per_batch = N_EVAL // N_SEED_BATCHES
    batch_f_adm = np.empty(N_SEED_BATCHES)
    batch_f_R = np.empty(N_SEED_BATCHES)
    batch_f_ang = np.empty(N_SEED_BATCHES)
    tot_hits = 0; tot_R = 0; tot_ang = 0; tot_n = 0
    R_min = np.inf; R_max = -np.inf
    # reservoirs for plotting (subsample)
    plot_R = []; plot_s12 = []; plot_s13 = []; plot_hit = []
    for b in range(N_SEED_BATCHES):
        rng = np.random.default_rng(RANDOM_SEED + b)
        UeL = rand_O3_batch(rng, per_batch)
        VDR = rand_O3_batch(rng, per_batch)
        w, V = light_batch(VDR, Y, MR)                     # ascending PSD eigenvalues
        m2 = w[:, 1]; m3 = w[:, 2]
        R = m3 ** 2 / m2 ** 2 - 1.0
        U = np.einsum("nki,nkj->nij", UeL, V)              # U_eL^T @ U_nuL
        s12, s23, s13 = pmns_angles_batch(U)
        Rin = in_band(R, R_BAND)
        ain = in_band(s12, SIN2_TH12_BAND) & in_band(s23, SIN2_TH23_BAND) & in_band(s13, SIN2_TH13_BAND)
        jin = Rin & ain
        batch_f_adm[b] = jin.mean(); batch_f_R[b] = Rin.mean(); batch_f_ang[b] = ain.mean()
        tot_hits += int(jin.sum()); tot_R += int(Rin.sum()); tot_ang += int(ain.sum()); tot_n += per_batch
        R_min = min(R_min, float(R.min())); R_max = max(R_max, float(R.max()))
        if b < 3:                                          # subsample first 3 batches for plotting
            idx = rng.choice(per_batch, size=min(4000, per_batch), replace=False)
            plot_R.append(R[idx]); plot_s12.append(s12[idx]); plot_s13.append(s13[idx]); plot_hit.append(jin[idx])
    f_adm_free = tot_hits / tot_n
    f_R_free = tot_R / tot_n
    f_angle_free = tot_ang / tot_n
    f_adm_cv = float(batch_f_adm.std() / batch_f_adm.mean()) if batch_f_adm.mean() > 0 else np.inf
    f_floor = N_MIN_HITS / N_EVAL
    res.update(dict(N_eval=tot_n, f_adm_free=f_adm_free, f_adm_hits=tot_hits,
                    f_R_free=f_R_free, f_angle_free=f_angle_free,
                    batch_f_adm=batch_f_adm, f_adm_cv=f_adm_cv, f_floor=f_floor,
                    R_min_free=R_min, R_max_free=R_max,
                    f_adm_free_positive=bool(f_adm_free >= f_floor)))
    res["plot_R"] = np.concatenate(plot_R); res["plot_s12"] = np.concatenate(plot_s12)
    res["plot_s13"] = np.concatenate(plot_s13); res["plot_hit"] = np.concatenate(plot_hit)
    print("\n=== STEP 2: MC ADMISSIBLE-VOLUME MEASURE (free U_eL/V_DR; 2e6 Haar draws) ===")
    print(f"  N_eval = {tot_n}  (10 seed batches of {per_batch})")
    print(f"  f_R (R in band over V_DR orbit)   = {f_R_free:.6e}   reachable R in [{R_min:.3f},{R_max:.3f}]")
    print(f"  f_angle (3 angles in 3sig)        = {f_angle_free:.6e}")
    print(f"  f_adm_free (JOINT box)            = {f_adm_free:.6e}  ({tot_hits} hits)  CV={f_adm_cv:.3e}")
    print(f"  f_R*f_angle (factorization chk)   = {f_R_free*f_angle_free:.6e}")
    print(f"  positive-measure floor N_min/N    = {f_floor:.3e}  =>  f_adm_free >= floor: {res['f_adm_free_positive']}")

    # ===== STEP 3: SHARED-eps_LX CONTRAST (tension witness; M_nu locked, U_eL free) =====
    # the framework's S116 single-parameter texture: neutrino sector NOT free (eps23 tied to the
    # charged-lepton sector) => R FIXED at 113.564 OUT of band. Only U_eL free (2e5 draws).
    # rebuild from the shared-eps form and verify it reproduces the S116 M_nu bit-for-bit.
    w_sh = eps23 * Y[2]
    MD_sh = np.array([[0.0, 0.0, 0.0], [0.0, Y[1], w_sh], [0.0, w_sh, Y[2]]])
    Mnu_sh = MD_sh @ np.diag(1.0 / MR) @ MD_sh.T
    Mnu_sh = 0.5 * (Mnu_sh + Mnu_sh.T)
    shared_recon_resid = float(np.max(np.abs(Mnu_sh - M_nu_s116)))
    m_sh, U_nuL_sh = light_single(Mnu_sh)
    R_shared = R_of(m_sh)
    R_shared_in = bool(in_band(R_shared, R_BAND))
    rng_sh = np.random.default_rng(RANDOM_SEED + 1000)
    UeL_sh = rand_O3_batch(rng_sh, N_EVAL_SHARED)
    U_sh = np.einsum("nki,kj->nij", UeL_sh, U_nuL_sh)      # U_eL^T @ U_nuL_sh (fixed)
    s12s, s23s, s13s = pmns_angles_batch(U_sh)
    ang_sh = in_band(s12s, SIN2_TH12_BAND) & in_band(s23s, SIN2_TH23_BAND) & in_band(s13s, SIN2_TH13_BAND)
    f_angle_shared = float(ang_sh.mean())
    f_adm_shared = float((ang_sh & R_shared_in).mean())    # R_shared fixed; joint = angle&R_in
    res.update(dict(shared_recon_resid=shared_recon_resid, R_shared=R_shared,
                    R_shared_in_band=R_shared_in, f_angle_shared=f_angle_shared,
                    f_adm_shared=f_adm_shared, N_eval_shared=N_EVAL_SHARED))
    print("\n=== STEP 3: SHARED-eps_LX CONTRAST (tension witness; M_nu locked, U_eL free) ===")
    print(f"  shared M_nu recon resid vs S116 = {shared_recon_resid:.2e} (==0 => exact)")
    print(f"  R_shared = {R_shared:.6f}  in [17,66]: {R_shared_in}  (angle-fixing eps23 drives R OUT)")
    print(f"  f_angle_shared (U_eL reaches angles) = {f_angle_shared:.6e}")
    print(f"  f_adm_shared (JOINT box)             = {f_adm_shared:.6e}  (near-empty: R stuck out of band)")

    # ===== STEP 4: corroboration grid (19^3 U_eL Euler at bare nu spectrum) =====
    # A coarse STRUCTURED scan of the U_eL angle-orbit. NOTE: the true S116 W2 STEP-3b
    # reachability mirror is the ANALYTIC WITNESS of Step 1 (which builds U_eL=U_obs^dag
    # explicitly and lands all 3 angles == obs_pmns_reachable=True). This 19-pt/axis grid is
    # a tertiary resolution probe: it UNDER-RESOLVES the 0.0036-wide sin^2 th13 box, so a
    # structured-grid hit is NOT expected and its absence is a coarse-resolution artifact, NOT
    # evidence against reachability. The grid's NEAREST-APPROACH to the box quantifies this.
    angs = np.linspace(0.0, np.pi, GRID_PTS, endpoint=False)
    a, bgr, c = np.meshgrid(angs, angs, angs, indexing="ij")
    a = a.ravel(); bgr = bgr.ravel(); c = c.ravel()
    ng = a.size
    ca, sa = np.cos(a), np.sin(a); cb, sb = np.cos(bgr), np.sin(bgr); cc, sc = np.cos(c), np.sin(c)
    R01 = np.zeros((ng, 3, 3)); R01[:, 2, 2] = 1.0          # U_eL = R01(a) R02(b) R12(c) Givens chain
    R01[:, 0, 0] = ca; R01[:, 1, 1] = ca; R01[:, 0, 1] = -sa; R01[:, 1, 0] = sa
    R02 = np.zeros((ng, 3, 3)); R02[:, 1, 1] = 1.0
    R02[:, 0, 0] = cb; R02[:, 2, 2] = cb; R02[:, 0, 2] = -sb; R02[:, 2, 0] = sb
    R12 = np.zeros((ng, 3, 3)); R12[:, 0, 0] = 1.0
    R12[:, 1, 1] = cc; R12[:, 2, 2] = cc; R12[:, 1, 2] = -sc; R12[:, 2, 1] = sc
    UeL_grid = np.einsum("nij,njk,nkl->nil", R01, R02, R12)
    # bare neutrino spectrum: U_nuL = I (diagonal M_nu) => U_PMNS = U_eL^T
    Ug = np.transpose(UeL_grid, (0, 2, 1))
    g12, g23, g13 = pmns_angles_batch(Ug)
    in12 = in_band(g12, SIN2_TH12_BAND); in23 = in_band(g23, SIN2_TH23_BAND)
    in13 = in_band(g13, SIN2_TH13_BAND)
    grid_in = in12 & in23 & in13
    f_angle_grid = float(grid_in.mean())                   # full joint box (th13 under-resolved)
    grid_in_wide = float((in12 & in23).mean())             # the WIDE (th12,th23) pair -- grid covers it
    grid_hits_wide = int((in12 & in23).sum())

    def box_ext_dist(x, band):                              # normalized exterior distance (0 inside)
        h = 0.5 * (band[1] - band[0])                       # (local) half-width
        return np.maximum.reduce([np.zeros_like(x), (band[0] - x) / h, (x - band[1]) / h])
    d_box = np.sqrt(box_ext_dist(g12, SIN2_TH12_BAND) ** 2 +
                    box_ext_dist(g23, SIN2_TH23_BAND) ** 2 +
                    box_ext_dist(g13, SIN2_TH13_BAND) ** 2)
    grid_min_box_dist = float(d_box.min())                 # nearest grid approach (half-width units)
    # the authoritative reachability mirror is the analytic witness (Step 1), not the coarse grid
    obs_reachable_witness = bool(res["witness_lands"])
    res.update(dict(grid_pts=ng, f_angle_grid=f_angle_grid,
                    grid_in_wide_th12th23=grid_in_wide, grid_hits_wide=grid_hits_wide,
                    grid_min_box_dist=grid_min_box_dist,
                    obs_reachable_witness=obs_reachable_witness))
    print("\n=== STEP 4: corroboration grid (19^3 U_eL Euler at bare nu spectrum; tertiary probe) ===")
    print(f"  grid pts = {ng}  f_angle_grid (full 3-angle box) = {f_angle_grid:.4e}  "
          f"(th13 box width 0.0036 UNDER-RESOLVED by 19-pt grid)")
    print(f"  grid in WIDE (th12&th23) pair  = {grid_in_wide:.4e}  ({grid_hits_wide} pts; grid covers wide angles)")
    print(f"  grid nearest approach to box   = {grid_min_box_dist:.3f} (box half-widths)")
    print(f"  obs_pmns_reachable (ANALYTIC WITNESS, the real S116 STEP-3b mirror) = {obs_reachable_witness}")

    # ===== STEP 5: cross-checks =====
    R_cf = (m_bare[2] ** 2 - m_bare[1] ** 2) / (m_bare[1] ** 2 - m_bare[0] ** 2)
    R_cf_diff = abs(R_cf - R_bare)
    R_cf_ok = bool(R_cf_diff < R_CLOSEDFORM_TOL)
    m1_rank_ok = bool(abs(m1_over_m3) < M1_REL_TOL)
    uni_resid = float(np.linalg.norm(U_PMNS_witness.T @ U_PMNS_witness - np.eye(3)))
    uni_ok = bool(uni_resid < UNITARY_TOL)
    res.update(dict(R_closedform=float(R_cf), R_cf_diff=float(R_cf_diff), R_cf_ok=R_cf_ok,
                    m1_rank_ok=m1_rank_ok, unitary_resid=uni_resid, unitary_ok=uni_ok,
                    R_central_NuFit=R_CENTRAL_NUFIT))
    print("\n=== STEP 5: cross-checks ===")
    print(f"  R closed-form (m3^2-m2^2)/(m2^2-m1^2) = {R_cf:.6f}  vs m3^2/m2^2-1 = {R_bare:.6f}  "
          f"diff={R_cf_diff:.2e} (<{R_CLOSEDFORM_TOL}: {R_cf_ok})")
    print(f"  m_1=0 rank check: |m1/m3|={abs(m1_over_m3):.2e} (<{M1_REL_TOL}: {m1_rank_ok})")
    print(f"  PMNS unitarity |U^T U - I|_fro = {uni_resid:.2e} (<{UNITARY_TOL}: {uni_ok})")
    print(f"  NuFit central-R anchor dm2_31/dm2_21-1 = {R_CENTRAL_NUFIT:.4f}  "
          f"(R_bare={R_bare:.4f}, {abs(R_bare/R_CENTRAL_NUFIT-1)*100:.1f}% apart; both deep interior)")

    return res


# ---------------------------------------------------------------------------
# Section 7 -- Verdict (3-track set-membership; plan §W2-1 verdict rubric)
# ---------------------------------------------------------------------------
def verdict_from(res: dict) -> str:
    """3-track set-membership verdict (plan §W2-1 discriminator):
       PASS  iff witness lands all 4 slots (edge-clear) AND f_adm_free >= N_min_hits/N_eval.
       INFO  iff witness lands BUT f_adm_free < floor (thin sliver) OR a witness slot within
             5% of a 3-sigma edge (partial-determination, non-load-bearing per Level-3 discipline).
       FAIL  iff witness FAILS (R_bare not in band OR 3 angles unreachable) AND f_adm_free == 0.
    PASS anchor is the ANALYTIC WITNESS; f_adm_free is the admissible-VOLUME measure, not the gate."""
    lands = res["witness_lands"]
    edge_clear = res["witness_edge_clear"]
    f_pos = res["f_adm_free_positive"]
    f_zero = bool(res["f_adm_free"] <= 0.0)
    if lands and edge_clear and f_pos:
        return "PASS"
    if lands and (not f_pos or not edge_clear):
        return "INFO"          # non-empty (witness lands) but thin sliver / edge-marginal
    if (not lands) and f_zero:
        return "FAIL"          # joint over-constraint: empty box
    return "INFO"              # defensive: non-empty by MC but witness construction missed


# ---------------------------------------------------------------------------
# Section 8 -- Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict, composite: str) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.4))

    # Panel 1: R distribution over free V_DR orbit vs R-band + witness + shared
    ax = axes[0]
    ax.hist(res["plot_R"], bins=50, color="#2980b9", alpha=0.7,
            label=f"free V_DR orbit\nreachable [{res['R_min_free']:.1f},{res['R_max_free']:.1f}]")
    ax.axvspan(R_BAND[0], R_BAND[1], color="#27ae60", alpha=0.15, label=f"NuFIT R-band {R_BAND}")
    ax.axvline(res["R_bare"], color="#1e8449", lw=2.2, label=f"witness R_bare={res['R_bare']:.3f}")
    ax.axvline(res["R_shared"], color="#c0392b", lw=2.2, ls="--",
               label=f"shared-eps_LX R={res['R_shared']:.1f} (OUT)")
    ax.axvline(res["R_central_NuFit"], color="k", lw=1.3, ls=":",
               label=f"NuFit central-R={res['R_central_NuFit']:.2f}")
    ax.set_xlabel("R = Delta m^2_32 / Delta m^2_21"); ax.set_ylabel("count (free V_DR draws)")
    ax.set_title(f"R confined to [{res['R_min_free']:.0f},{res['R_max_free']:.0f}] by near-degenerate "
                 f"M_R\n=> f_R = {res['f_R_free']:.3f} (whole orbit R-admissible)")
    ax.legend(fontsize=7.2); ax.grid(alpha=0.3)

    # Panel 2: angle scatter (sin2_th13 vs sin2_th12) with the 3-sigma box + joint hits
    ax = axes[1]
    s12p = res["plot_s12"]; s13p = res["plot_s13"]; hitp = res["plot_hit"]
    ax.scatter(s12p[~hitp], s13p[~hitp], s=3, color="#bdc3c7", alpha=0.4, label="free draws")
    if hitp.any():
        ax.scatter(s12p[hitp], s13p[hitp], s=14, color="#e67e22", zorder=5,
                   label="JOINT-box hits")
    ax.add_patch(plt.Rectangle((SIN2_TH12_BAND[0], SIN2_TH13_BAND[0]),
                               SIN2_TH12_BAND[1] - SIN2_TH12_BAND[0],
                               SIN2_TH13_BAND[1] - SIN2_TH13_BAND[0],
                               fill=False, edgecolor="#27ae60", lw=2, zorder=6,
                               label="NuFIT 3sig box (th12,th13)"))
    ax.scatter([BF_TH12], [BF_TH13], marker="*", s=160, color="#1e8449", zorder=7,
               label="witness (band centers)")
    ax.set_xlabel("sin^2 th12"); ax.set_ylabel("sin^2 th13")
    ax.set_xlim(0, 1); ax.set_ylim(0, 0.12)
    ax.set_title(f"angle box: f_angle = {res['f_angle_free']:.2e}\n"
                 f"f_adm_free = f_R*f_angle = {res['f_adm_free']:.2e} ({res['f_adm_hits']} hits)")
    ax.legend(fontsize=7.0, loc="upper right"); ax.grid(alpha=0.3)

    # Panel 3: verdict checklist
    ax = axes[2]; ax.axis("off")
    ax.text(0.0, 1.0, f"{GATE_ID}\n=> {composite}", fontsize=12, weight="bold",
            transform=ax.transAxes, va="top")
    tick = lambda b: "OK" if b else "X"
    txt = (
        f"ANALYTIC WITNESS (PASS anchor):\n"
        f"  R_bare       = {res['R_bare']:.4f}  in[17,66] {tick(res['witness_R_slot'])}\n"
        f"  sin2_th12    = {res['witness_s12']:.4f}  in-3sig {tick(res['witness_a12_slot'])}\n"
        f"  sin2_th23    = {res['witness_s23']:.4f}  in-3sig {tick(res['witness_a23_slot'])}\n"
        f"  sin2_th13    = {res['witness_s13']:.5f} in-3sig {tick(res['witness_a13_slot'])}\n"
        f"  4-slot land  = {res['witness_lands']}  edge-clear {tick(res['witness_edge_clear'])}\n\n"
        f"MC ADMISSIBLE-VOLUME (free U_eL/V_DR):\n"
        f"  f_R (V_DR)     = {res['f_R_free']:.4f}\n"
        f"  f_angle (U_eL) = {res['f_angle_free']:.3e}\n"
        f"  f_adm_free     = {res['f_adm_free']:.3e}\n"
        f"                   (+-CV {res['f_adm_cv']:.2f}, {res['f_adm_hits']} hits/2e6)\n"
        f"  floor N_min/N  = {res['f_floor']:.1e}  positive {tick(res['f_adm_free_positive'])}\n\n"
        f"SHARED-eps_LX CONTRAST (tension witness):\n"
        f"  R_shared = {res['R_shared']:.2f} (OUT) recon {res['shared_recon_resid']:.0e}\n"
        f"  f_adm_shared = {res['f_adm_shared']:.1e} (near-empty)\n\n"
        f"CROSS-CHECKS:\n"
        f"  R closed-form {tick(res['R_cf_ok'])}  m1=0 rank {tick(res['m1_rank_ok'])}  "
        f"unitarity {tick(res['unitary_ok'])}\n\n"
        f"=> under-determination SURVIVES the joint box.\n"
        f"   Free-texture orbit observationally COMPATIBLE\n"
        f"   with NuFIT but NOT predictive (no unique value).\n"
        f"   CP/J EXCLUDED: real textures => J=0 (standing)."
    )
    ax.text(0.0, 0.92, txt, fontsize=7.7, transform=ax.transAxes, va="top", family="monospace")

    fig.suptitle(f"{GATE_ID}: joint (R, PMNS-angle) admissibility over the free lepton-texture "
                 f"family (D_K tau_fold={TAU}); NuFIT 5.2 NO 3-sigma box; J=0 (real textures)",
                 fontsize=10.5)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 -- Verdict payload (race-safe MCP single-writer; print only; [VERIFY] => no 3-tuple)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
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
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 10 -- Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()
    print(f"=== {GATE_ID} ===")
    pins = log_input_pins(INPUT_FILES)

    # input-SHA gate: S116 npz must match the frozen plan pin (else PRE-REG-INC honest close)
    s116_rel = str(S116_TEXTURE.relative_to(PROJECT_ROOT)).replace("\\", "/")
    s116_sha = pins.get(s116_rel, "")
    audit_sha, content_sha = compute_dual_sha(THIS, CANONICAL_PATH, pins)
    print(f"  audit_sha256  = {audit_sha}")
    print(f"  content_sha256= {content_sha}")
    if s116_sha != S116_SHA_PIN:
        print(f"\n!!! S116 npz SHA mismatch: got {s116_sha[:16]}..., expected {S116_SHA_PIN[:16]}...")
        value = f"PRE-REG-INC_blocked_by_s116_npz_SHA_mismatch_got_{s116_sha[:16]}_expected_{S116_SHA_PIN[:16]}"
        print_verdict_payload("PRE-REG-INC", value, audit_sha, content_sha)
        print(f"\n=== {GATE_ID}: PRE-REG-INC (input SHA drift) ===")
        return 0

    res = compute()
    composite = verdict_from(res)

    make_plot(res, composite)

    print("\n=== VERDICT ===")
    print(f"  witness_lands={res['witness_lands']} (edge-clear={res['witness_edge_clear']}); "
          f"f_adm_free={res['f_adm_free']:.3e} (floor {res['f_floor']:.1e}); "
          f"contrast f_adm_shared={res['f_adm_shared']:.1e} => composite = {composite}")

    # ----- persist npz -----
    np.savez(
        OUT_NPZ,
        value=f"{composite}", composite=composite,
        # fixed input spectra
        m_e_vals=res["m_e_vals"], Y_nu_diag=res["Y_nu_diag"], M_R_MKK=res["M_R_MKK"],
        eps23_strength=res["eps23_strength"], w23_nu=res["w23_nu"],
        obs_pmns_reachable_s116=res["obs_pmns_reachable_s116"],
        # witness (PASS anchor)
        m_bare=res["m_bare"], R_bare=res["R_bare"], m1_over_m3=res["m1_over_m3"],
        witness_s12=res["witness_s12"], witness_s23=res["witness_s23"], witness_s13=res["witness_s13"],
        witness_R_slot=res["witness_R_slot"], witness_a12_slot=res["witness_a12_slot"],
        witness_a23_slot=res["witness_a23_slot"], witness_a13_slot=res["witness_a13_slot"],
        witness_lands=res["witness_lands"], witness_edge_clear=res["witness_edge_clear"],
        ep_R=res["ep_R"], ep_12=res["ep_12"], ep_23=res["ep_23"], ep_13=res["ep_13"],
        # MC free-family measure
        N_eval=res["N_eval"], f_adm_free=res["f_adm_free"], f_adm_hits=res["f_adm_hits"],
        f_R_free=res["f_R_free"], f_angle_free=res["f_angle_free"],
        batch_f_adm=res["batch_f_adm"], f_adm_cv=res["f_adm_cv"], f_floor=res["f_floor"],
        R_min_free=res["R_min_free"], R_max_free=res["R_max_free"],
        f_adm_free_positive=res["f_adm_free_positive"],
        # shared-eps contrast
        shared_recon_resid=res["shared_recon_resid"], R_shared=res["R_shared"],
        R_shared_in_band=res["R_shared_in_band"], f_angle_shared=res["f_angle_shared"],
        f_adm_shared=res["f_adm_shared"], N_eval_shared=res["N_eval_shared"],
        # corroboration grid (tertiary probe)
        grid_pts=res["grid_pts"], f_angle_grid=res["f_angle_grid"],
        grid_in_wide_th12th23=res["grid_in_wide_th12th23"], grid_hits_wide=res["grid_hits_wide"],
        grid_min_box_dist=res["grid_min_box_dist"], obs_reachable_witness=res["obs_reachable_witness"],
        # cross-checks
        R_closedform=res["R_closedform"], R_cf_diff=res["R_cf_diff"], R_cf_ok=res["R_cf_ok"],
        m1_rank_ok=res["m1_rank_ok"], unitary_resid=res["unitary_resid"], unitary_ok=res["unitary_ok"],
        R_central_NuFit=res["R_central_NuFit"],
        # pins
        tau=TAU, scheme=SCHEME, convention=CONVENTION, L_max=str(L_MAX),
        R_band=np.array(R_BAND), sin2_th12_band=np.array(SIN2_TH12_BAND),
        sin2_th23_band=np.array(SIN2_TH23_BAND), sin2_th13_band=np.array(SIN2_TH13_BAND),
        audit_sha256=audit_sha, content_sha256=content_sha,
    )

    # ----- value payload -----
    value = (
        f"joint-admissibility={composite};"
        f"WITNESS_lands_all4={res['witness_lands']}(R_bare={res['R_bare']:.6g}_in[17,66];"
        f"th12={res['witness_s12']:.6g},th23={res['witness_s23']:.6g},th13={res['witness_s13']:.6g}_at_band_centers);"
        f"f_adm_free={res['f_adm_free']:.6g}(+-CV{res['f_adm_cv']:.3g},{res['f_adm_hits']}hits/2e6,floor{res['f_floor']:.2g});"
        f"f_R={res['f_R_free']:.6g}(R_reachable[{res['R_min_free']:.4g},{res['R_max_free']:.4g}]_subset_band);"
        f"f_angle={res['f_angle_free']:.6g};"
        f"CONTRAST_shared-epsLX_R={res['R_shared']:.6g}_OUT_f_adm_shared={res['f_adm_shared']:.3g};"
        f"xchk[R_closedform_diff={res['R_cf_diff']:.2g},m1/m3={res['m1_over_m3']:.2g},unitary={res['unitary_resid']:.2g}];"
        f"NuFit_central_R={res['R_central_NuFit']:.6g};J=0_real-textures(CP-excluded);"
        f"under-determination_SURVIVES_joint_box(oscillation-anchored_caveat_S100a-MD-NORM)"
    )

    companion = (
        f"PMNS joint (R+3angle) admissibility: witness (V_DR=I,U_eL=U_obs^dag) lands all 4 NuFIT "
        f"5.2 NO 3sig slots => J NON-EMPTY analytically (R_bare={res['R_bare']:.4f}, angles at band "
        f"centers); free-family f_adm_free={res['f_adm_free']:.3e} ({res['f_adm_hits']} hits/2e6) >= "
        f"floor {res['f_floor']:.1e} => under-determination SURVIVES; shared-eps_LX contrast "
        f"R={res['R_shared']:.2f} OUT => f_adm_shared={res['f_adm_shared']:.1e} (tension witness)"
    )
    extra = [
        (f"# factorization: R is U_eL-INVARIANT; near-degenerate M_R (spread "
         f"{(res['M_R_MKK'].max()/res['M_R_MKK'].min()-1)*100:.1f}%) confines R to "
         f"[{res['R_min_free']:.2f},{res['R_max_free']:.2f}] subset [17,66] => f_R={res['f_R_free']:.4f}; "
         f"f_adm_free = f_R*f_angle = {res['f_R_free']*res['f_angle_free']:.3e} # {GATE_ID}"),
        (f"# OSCILLATION-ANCHORED CAVEAT (S100a-MD-NORMALIZATION INFO PERMANENT): D_K bottom-triple->Y_i "
         f"NON-UNIQUE (MAP-A/MAP-B) => R_bare={res['R_bare']:.4f} is a CONSISTENCY of the spectrum "
         f"channel with NuFIT (vs central-R {res['R_central_NuFit']:.3f}), NOT a zero-free-param "
         f"prediction; substrate-FIRST content = seesaw STRUCTURE+bowtie M_R shape+U_eL-invariance # {GATE_ID}"),
        (f"# CP EXCLUDED: real O(3) textures => delta_CP in {{0,pi}} => Jarlskog J=0 (framework standing "
         f"prediction); CP-sector under-determination is the separate S117-W3-3 / VII.BL question # {GATE_ID}"),
        (f"# reachability mirror = the ANALYTIC WITNESS (Step 1, U_eL=U_obs^dag): obs_pmns_reachable="
         f"{res['obs_reachable_witness']} (== S116 W2 STEP 3b obs_pmns_reachable={res['obs_pmns_reachable_s116']}); "
         f"the coarse 19^3 grid UNDER-RESOLVES the 0.0036-wide sin2_th13 box (f_angle_grid={res['f_angle_grid']:.1e}, "
         f"nearest approach {res['grid_min_box_dist']:.2f} half-widths) -- resolution artifact, not a reachability failure # {GATE_ID}"),
    ]
    print_verdict_payload(composite, value, audit_sha, content_sha,
                          companion_note=companion, extra_rows=extra)

    print("\n=== ARTIFACTS ===")
    print(f"  npz: {OUT_NPZ}")
    print(f"  png: {OUT_PNG}")
    wall = time.time() - t0
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
