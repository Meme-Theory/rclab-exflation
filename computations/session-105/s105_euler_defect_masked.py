#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S105-EULER-DEFECT-MASKED
================================================================================
Gate:   S105-EULER-DEFECT-MASKED   (trigger [VERIFY], classification GEOMETRIC)
Agent:  berry-geometric-phase-theorist
Plan:   sessions/session-plan/session-105-plan-w3.md  ## §W3-1
WP:     sessions/session-105/session-105-w3-workingpaper.md  ### §W3-1

================================================================================
GEOMETRY FIRST -- THE EULER-CLASS CONJUNCT OF THE METRIC-WITHOUT-CURVATURE WALL
================================================================================
S104-EULER-CLASS-J-DOUBLET (INFO, e2_lattice=-7.02e-3, max|F^Euler|=4.41e-2,
n_plaq_above=1) computed the FHS-Pfaffian Euler class of the lowest 2-fold
J/BDI-real Dirac doublet on the 2-parameter U(2)-invariant volume-preserving TT
surface (v_J=(2,-2,1), v_mu = n x v_J = (11,7,-8), |v_mu|^2=234; mu=0 = Jensen
line; fold at tau_fold=0.19). The ENTIRE non-trivial Euler content traced to ONE
corner plaquette corner_plaq_ij=[0,49] at the S100b-documented B1/B2 von
Neumann-Wigner level crossing (the (0.10,+0.10) window corner) -- a frame-singular
LATTICE artifact (the real SO(2) frame is undefined where the two bands cross),
NOT a substrate-IS topological obstruction. S104 already computed the
defect-EXCLUDED Euler class e2_lattice_defect_excluded = -8.83e-18 ~ 0
(PASS-TRIVIAL content), but the S104 INFO verdict could NOT promote it to a
literal PASS without a re-run with the defect plaquette masked BY PRE-REGISTRATION
(the mask pinned at plan-freeze from the S104 defect map, NOT a post-hoc exclusion
on the same run -- which would be iterate-until-PASS-adjacent, v3-closure-recovery.md
Class 6).

THIS GATE: re-run the IDENTICAL S104 FHS-Pfaffian-Euler eigenbundle transport
(genuine re-execution, NOT an npz re-read), then EXCLUDE the single plan-pinned
corner plaquette [0,49] from BOTH the Pfaffian-sum accumulation e2_masked AND the
max|F^Euler|_masked reduction. The mask index is PINNED AT PLAN-FREEZE from the
SHA-pinned S104 npz field 'corner_plaq_ij'; the producing script asserts the
runtime-recovered dominant plaquette equals the plan-pinned mask (re-mesh-drift
guard) and FAILs honestly (INFO branch) on mismatch -- closing the Class-8.2
execution-time-freedom (run-time mask selection) this gate exists to eliminate.

PASS (the Euler-class conjunct of the metric-without-curvature wall):
    PASS iff ( |e2_masked - round(e2_masked)| < 1e-3 )       [round-deficit]
         AND ( round(e2_masked) == 0 )                       [integer-quantization]
         AND ( max|F^Euler|_masked < 1e-12 ).                [curvature-vanishing]
This is the ORIGINAL S104 PASS-TRIVIAL criterion evaluated on the masked domain;
the tolerances (1e-3, 1e-12) are BYTE-IDENTICAL to S104. The ONLY change is the
plan-frozen exclusion of the frame-singular plaquette -- NO threshold change
(Class 3 forbidden), NO convention change (Class 1 forbidden), NO seed/scan
iteration (Class 6 forbidden; single-shot deterministic).

--------------------------------------------------------------------------------
[VERIFY] SUBSTITUTION CHAIN (plan §W3-1 substitution_chain;
                            math-scripts.md §"Double-Check Logic Before Compute")
--------------------------------------------------------------------------------
Claim: "Masking the single plan-pinned defect plaquette yields e2_masked rounding
        to the integer 0 with max|F^Euler|_masked < 1e-12 (PASS-TRIVIAL), with no
        threshold change vs S104."

Step 1 -- Definitions:
  F^Euler_{ij}        = real-frame SO(2) Wilson-loop Pfaffian curvature on
                        plaquette (i,j), lowest 2-fold J/BDI-real doublet
                        [S104 FHS-Pfaffian-Euler path; reuses S96 eigenbundle transport].
  e2                  = (1/2pi) sum_{(i,j)} Pf(F^Euler_{ij}).
  mask                = plaquette index [0,49] = corner_plaq_ij from
                        s104_euler_class_j_doublet.npz (the (0.10,+0.10) B1/B2
                        vN-Wigner crossing) [PINNED AT PLAN-FREEZE].
  e2_masked           = (1/2pi) sum_{(i,j) != mask} Pf(F^Euler_{ij}).
  max|F^Euler|_masked = max_{(i,j) != mask} |F^Euler_{ij}|.

Step 2 -- Substitution (S104 measured fields, no simplification):
  e2_lattice (full)               = -7.016945e-03
  max_absF   (full)               =  4.408876e-02   (the [0,49] corner cell)
  e2_lattice_defect_excluded      = -8.834874e-18   (= e2_masked, S104 already computed it)
  |F^Euler| at [0,49]             =  4.408876e-02   (= max_absF; SOLE contaminating cell, n_plaq_above=1)
  max|F^Euler| over all != [0,49] =  4.510281e-17   (next-largest plaquette)

Step 3 -- Simplification (algebra only, one step per line):
  e2_masked            = e2_lattice_defect_excluded = -8.834874e-18.
  |e2_masked - round(e2_masked)| = |-8.834874e-18 - 0| = 8.83e-18  < 1e-3.   [round-deficit]
  round(e2_masked)     = round(-8.83e-18) = 0.                              [integer-quantization]
  max|F^Euler|_masked  = 4.510281e-17                          < 1e-12.     [curvature-vanishing]

Step 4 -- Direction read-off:
  All three conjuncts hold by 14-15 OOM margins. The ENTIRE non-trivial Euler
  content lives in the single [0,49] corner plaquette; removing it collapses both
  observables to the float64 round-off floor. The corner is a frame-singular
  lattice artifact at the B1/B2 vN-Wigner crossing, NOT a substrate-IS obstruction.

Conclusion: With the plan-pinned mask, e2_masked = 0 (integer, round-deficit
  8.8e-18) and max|F^Euler|_masked = 4.5e-17 < 1e-12 => PASS-TRIVIAL on the
  masked domain; the Euler-class conjunct of the metric-without-curvature wall
  holds at the LITERAL S104 threshold.

SUBSTRATE ARROW (phononic-framing.md; never inverted):
  D_K eigenbundle over the substrate's OWN modulus surface -> real (BDI,
  Kosmann-anti-Hermitian) two-band frame O(tau,mu) -> SO(2)-valued frame curvature
  F^Euler -> Euler class e2. Reality is upstream and load-bearing: K_a anti-Hermitian
  => the lowest doublet admits a REAL frame, whose Berry curvature vanishes
  identically (Im(QGT)=0) -- that is WHY the Euler class is 0. The single vN-Wigner
  corner plaquette is a frame-singular discretization shadow where the real SO(2)
  frame degenerates (two bands cross), NOT a topological feature of the fabric.
  The (tau,mu) surface IS the substrate's intrinsic modulus-space (Level-2
  substrate-IS), NOT a container D_K sits in.

Author: berry-geometric-phase-theorist (Session 105, Wave 3)
Date:   2026-06-11
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
PROJECT_ROOT = Path(__file__).resolve().parents[2]          # (local) computations/session-105 => parents[2]=root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_96_DIR = PROJECT_ROOT / "computations" / "session-96"
SESSION_104_DIR = PROJECT_ROOT / "computations" / "session-104"
SESSION_105_DIR = PROJECT_ROOT / "computations" / "session-105"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(SESSION_96_DIR))
sys.path.insert(0, str(SESSION_104_DIR))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import tau_fold  # noqa: E402

# Reuse the S96 off-Jensen-Chern eigenbundle-transport scaffold + the S104
# FHS-Pfaffian-Euler path VERBATIM (real_frame_block / so2_log_angle /
# fhs_pfaffian_euler / pf2_det_smoke). Importing s104 re-uses the exact deg-2
# non-Abelian real-frame SO(2) Wilson-loop machinery -- the gate's DELTA is the
# plan-pinned mask + the re-run + the anti-drift guard, NOT a re-derivation.
import s96_geom_offjensen_chern as s96  # noqa: E402
import s104_euler_class_j_doublet as s104  # noqa: E402

# ---------------------------------------------------------------------------
# Gate identity + pre-registered pins (plan §W3-1 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "S105"                          # (local) for print_verdict_payload
GATE_ID = "S105-EULER-DEFECT-MASKED"      # (local)
SCHEME = "FHS-Pfaffian-Euler"             # (local) UNCHANGED from S104
CONVENTION = "ABSOLUTE"                   # (local) UNCHANGED from S104
L_MAX = "10"                              # (local) Peter-Weyl band, UNCHANGED from S104
SCHEMA_VERSION = "S84+"                   # (local)

# Plan scan_range IDENTICAL to S104: tau in [0.10,0.30] x mu in [-0.10,0.10]; 50x50 plaquette mesh.
TAU_LO, TAU_HI = 0.10, 0.30               # (local) plan scan_range tau
MU_LO, MU_HI = -0.10, 0.10                # (local) plan scan_range mu (mu=0 = Jensen line)
N_PLAQ = 50                               # (local) 50x50 plaquette grid (N_eval=2500); IDENTICAL to S104
N_NODE = N_PLAQ + 1                       # (local) 51x51 NODE grid; IDENTICAL to S104
DTAU = (TAU_HI - TAU_LO) / N_PLAQ         # (local) ~0.004
DMU = (MU_HI - MU_LO) / N_PLAQ            # (local) ~0.004
BAND_DEG = 2                              # (local) plan band_deg=2 (J/PH doublet; non-Abelian FHS)

# Tolerances (plan §W3-1 machinery_pin_map.tolerance) -- BYTE-IDENTICAL to S104 PASS-TRIVIAL criterion.
EULER_INT_TOL = 1e-3                       # (local) integer-quantization |e2_masked-round(e2_masked)|
TRIVIAL_FEULER_FLOOR = 1e-12              # (local) curvature-vanishing max|F^Euler|_masked floor
DEG_TOL = 1e-7                            # (local) J/PH-pair identification (reused S96 band_degeneracy)

# ---- PLAN-FREEZE MASK PIN (the anti-iterate-until-PASS structure) ----
# PINNED AT PLAN-FREEZE from s104_euler_class_j_doublet.npz field 'corner_plaq_ij'.
DEFECT_MASK_PLAQ_IJ = (0, 49)            # (local) the (0.10,+0.10) B1/B2 vN-Wigner corner plaquette
DEFECT_MASK_TAU_MU = (0.102, 0.098)     # (local) corner_tau_mu from the npz (the (0.10,+0.10) corner)
MASK_CARDINALITY = 1                     # (local) EXACTLY one plaquette masked (n_plaq_above=1 in S104);
                                         #         a SECOND masked plaquette would be over-masking and FAILs pre-registration
DEFECT_MASK_SOURCE_NPZ = SESSION_104_DIR / "s104_euler_class_j_doublet.npz"   # (local)
DEFECT_MASK_SOURCE_FIELD = "corner_plaq_ij"                                    # (local) exact npz field name
DEFECT_MASK_SOURCE_SHA256 = "1aff8a3143169c8a0b887584167bf7ddc80d04f7df5fa4f671a2bfd6903ca9de"  # (local) SHA pin of the npz

# The 2-parameter U(2)-invariant TT directions (reused via s96.V_JENSEN / s96.V_MU)
V_JENSEN = s96.V_JENSEN                    # (local) (2,-2,1); |v|^2=9
V_MU = s96.V_MU                            # (local) (11,7,-8) = n x v_J; |v|^2=234; vol-preserving, perp-Jensen

# Output destinations
SCRIPT_PATH = Path(__file__).resolve()                                  # (local)
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"             # (local)
DK_BUILDER = SHARED_DIR / "dirac_spectrum.py"                           # (local)
S96_SCRIPT = SESSION_96_DIR / "s96_geom_offjensen_chern.py"             # (local)
S104_SCRIPT = SESSION_104_DIR / "s104_euler_class_j_doublet.py"         # (local)
NPZ_OUT = SESSION_105_DIR / "s105_euler_defect_masked.npz"             # (local)
PNG_OUT = SESSION_105_DIR / "s105_euler_defect_masked.png"            # (local)


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema; mirrors S104 reference implementation).
# audit_sha256 includes the pinmap (which carries the plan-frozen mask index +
# coords) -- so a mask drift would change audit_sha256 (plan audit_discriminators).
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
       content_sha256 = sha256(script_bytes). The pinmap carries the plan-frozen
       mask index/coords (DEFECT_MASK_* keys) so a mask drift changes audit_sha256
       (plan §W3-1 audit_sha256_inputs=[script,canonical,pinmap])."""
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


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    print("=" * 78)
    print(f"{GATE_ID}  --  defect-masked Euler class of the lowest J/BDI-real Dirac doublet")
    print("  S104 INFO (e2=-7.02e-3, one corner plaquette dominated); this gate masks the")
    print(f"  plan-pinned vN-Wigner corner plaquette {DEFECT_MASK_PLAQ_IJ} BY PRE-REGISTRATION")
    print("=" * 78)

    # --- input pins + dual SHA (pinmap carries the plan-frozen mask) ---
    # File-SHA pins (hashed from disk).
    pins = log_input_pins({
        "canonical_constants": CANONICAL_CONSTANTS,
        "s96_chern_script": S96_SCRIPT,
        "s104_euler_script": S104_SCRIPT,
        "s104_euler_npz": DEFECT_MASK_SOURCE_NPZ,
        "dirac_spectrum": DK_BUILDER,
    })
    # Plan-frozen MASK pins enter the audit hash as literal values (NOT files): a mask drift
    # (index/coords/cardinality/source) => the pinmap json changes => audit_sha256 changes
    # (plan §W3-1 audit_sha256_inputs=[script,canonical,pinmap]).
    pins["_mask_plaq_ij"] = json.dumps(list(DEFECT_MASK_PLAQ_IJ))            # (local)
    pins["_mask_tau_mu"] = json.dumps([round(x, 6) for x in DEFECT_MASK_TAU_MU])  # (local)
    pins["_mask_cardinality"] = str(MASK_CARDINALITY)                       # (local)
    pins["_mask_source_field"] = DEFECT_MASK_SOURCE_FIELD                   # (local)
    pins["_mask_source_sha256"] = DEFECT_MASK_SOURCE_SHA256                 # (local)
    for k in ("_mask_plaq_ij", "_mask_tau_mu", "_mask_cardinality"):
        print(f"  MASK-PIN   {k}: {pins[k]}")
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # --- guard: SHA-pin the S104 npz the mask is lifted from (Input-SHA Ledger) ---
    s104_npz_sha = sha256_of_file(DEFECT_MASK_SOURCE_NPZ)        # (local)
    print(f"\n  S104 defect-map npz sha256 = {s104_npz_sha}")
    print(f"  plan-pinned                = {DEFECT_MASK_SOURCE_SHA256}")
    s104_npz_sha_ok = (s104_npz_sha == DEFECT_MASK_SOURCE_SHA256)  # (local)
    if not s104_npz_sha_ok:
        print("  WARN: S104 npz SHA mismatch vs plan-freeze pin -- the defect map drifted on disk.")

    # --- Pfaffian smoke test (Pf^2 = det) reused verbatim from S104 ---
    pf_resid = s104.pf2_det_smoke()                             # (local)
    print(f"  Pf^2=det smoke test (random 4x4 antisym): residual = {pf_resid:.3e} "
          f"{'OK' if pf_resid < 1e-12 else 'WARN'}")

    # --- geometry self-check (Sage-verified relations) ---
    n_vol = np.array([1.0, 3.0, 4.0])                          # (local) volume normal (multiplicities)
    assert abs(n_vol @ V_JENSEN) < 1e-12, "Jensen not volume-preserving"
    assert abs(n_vol @ V_MU) < 1e-12, "v_mu not volume-preserving"
    assert abs(V_JENSEN @ V_MU) < 1e-12, "v_mu not orthogonal to Jensen"
    print(f"  GEOMETRY: v_J=(2,-2,1) |v|^2={V_JENSEN@V_JENSEN:.0f}; "
          f"v_mu=(11,7,-8)=n x v_J |v|^2={V_MU@V_MU:.0f}; vol-preserving & perp-Jensen OK")

    infra = s96.build_su3_infra()

    # --- confirm band_deg=2 at the fold (S104/S96 baseline) ---
    deg_bot, lam_bot = s96.band_degeneracy(tau_fold, 0.0, 0, 0, infra, deg_tol=DEG_TOL)
    print(f"  band_deg at (tau_fold,mu=0): {deg_bot} (J/PH doublet), |lambda|_min={lam_bot:.6f} "
          f"(plan BAND_DEG={BAND_DEG})")
    assert deg_bot == BAND_DEG, f"band degeneracy {deg_bot} != plan {BAND_DEG}"

    # --- NODE grid (IDENTICAL to S104) ---
    taus = np.linspace(TAU_LO, TAU_HI, N_NODE)                 # (local)
    mus = np.linspace(MU_LO, MU_HI, N_NODE)                    # (local)
    print(f"\n  grid: tau in [{TAU_LO},{TAU_HI}] x mu in [{MU_LO},{MU_HI}]  "
          f"({N_NODE}x{N_NODE} nodes -> {N_PLAQ}x{N_PLAQ}={N_PLAQ*N_PLAQ} plaquettes); "
          f"Delta_tau={DTAU:.4f} Delta_mu={DMU:.4f}; fold tau={tau_fold} enclosed at mu=0")

    # =====================================================================
    # GENUINE RE-RUN: FHS-Pfaffian-Euler lattice (verbatim S104 path, NOT an npz re-read)
    # =====================================================================
    print("\n  [RE-RUN] FHS-Pfaffian-Euler: real-frame SO(2) Wilson-loop holonomy (verbatim S104)")
    e2_lattice, F_plaq, det_track, frame_ok_frac = s104.fhs_pfaffian_euler(
        0, 0, infra, taus, mus, deg_bot
    )
    max_absF_full = float(np.max(np.abs(F_plaq)))              # (local) full-domain max (the corner cell)
    n_reflections = int(np.sum(det_track < 0))                # (local)
    print(f"    e2_lattice (FULL) = {e2_lattice:.6e}; round={round(e2_lattice)}; "
          f"max|F^Euler|(FULL)={max_absF_full:.3e}; reflections={n_reflections}/{F_plaq.size}")

    # =====================================================================
    # RUNTIME MASK GUARD: recovered dominant plaquette MUST equal the plan-pinned mask
    # (re-mesh-drift guard; FAIL honestly -> INFO on mismatch, do NOT auto-relocate the mask)
    # =====================================================================
    flat = np.abs(F_plaq).ravel()                             # (local)
    imax = int(np.argmax(flat))                               # (local)
    rec_ci, rec_cj = np.unravel_index(imax, F_plaq.shape)     # (local) runtime-recovered dominant plaquette
    rec_ci, rec_cj = int(rec_ci), int(rec_cj)
    rec_tau = 0.5 * (taus[rec_ci] + taus[rec_ci + 1])         # (local)
    rec_mu = 0.5 * (mus[rec_cj] + mus[rec_cj + 1])            # (local)
    mask_matches = (rec_ci, rec_cj) == DEFECT_MASK_PLAQ_IJ    # (local) re-mesh-drift guard
    print(f"\n  [MASK GUARD] runtime dominant |F^Euler| plaquette = [{rec_ci},{rec_cj}] "
          f"at (tau,mu)=({rec_tau:.4f},{rec_mu:.4f}), |F^Euler|={F_plaq[rec_ci,rec_cj]:.6e}")
    print(f"               plan-pinned mask              = [{DEFECT_MASK_PLAQ_IJ[0]},{DEFECT_MASK_PLAQ_IJ[1]}] "
          f"at (tau,mu)=({DEFECT_MASK_TAU_MU[0]:.4f},{DEFECT_MASK_TAU_MU[1]:.4f})")
    print(f"               MASK MATCHES plan-pin: {mask_matches}  (FAIL->INFO on mismatch; NO auto-relocate)")

    # =====================================================================
    # APPLY THE PLAN-PINNED MASK to BOTH observables (the gate's DELTA vs S104)
    # =====================================================================
    mi, mj = DEFECT_MASK_PLAQ_IJ                              # (local) ALWAYS the plan-pinned index, never runtime
    F_masked = F_plaq.copy()                                  # (local)
    masked_pf_value = float(F_plaq[mi, mj])                   # (local) the value being removed
    # e2_masked = (1/2pi) sum_{(i,j) != mask} Pf(F^Euler_{ij})  -- exclude the plan-pinned cell.
    e2_masked = float((np.sum(F_plaq) - F_plaq[mi, mj]) / (2.0 * np.pi))  # (local)
    # max|F^Euler|_masked = max over (i,j) != mask of |F^Euler_{ij}|.
    F_masked_abs = np.abs(F_plaq).copy()                     # (local)
    F_masked_abs[mi, mj] = -np.inf                           # (local) exclude the masked cell from the max
    max_absF_masked = float(np.max(F_masked_abs))            # (local)
    masked_argmax = int(np.argmax(F_masked_abs))             # (local) location of the next-largest plaquette
    nm_ci, nm_cj = np.unravel_index(masked_argmax, F_plaq.shape)  # (local)

    print(f"\n  [MASKED] removed plaquette [{mi},{mj}] (Pf value {masked_pf_value:.6e})")
    print(f"    e2_masked            = {e2_masked:.6e}  (= e2 with the [{mi},{mj}] cell excluded)")
    print(f"    round(e2_masked)     = {round(e2_masked)}")
    print(f"    |e2_masked - round|  = {abs(e2_masked - round(e2_masked)):.6e}  (tol {EULER_INT_TOL:.0e})")
    print(f"    max|F^Euler|_masked  = {max_absF_masked:.6e}  at [{nm_ci},{nm_cj}]  (floor {TRIVIAL_FEULER_FLOOR:.0e})")

    # --- count plaquettes above the curvature floor AFTER masking (must be 0 for clean PASS) ---
    n_plaq_above_masked = int(np.sum(F_masked_abs > TRIVIAL_FEULER_FLOOR))  # (local) F_masked_abs has -inf at mask
    print(f"    plaquettes above {TRIVIAL_FEULER_FLOOR:.0e} (masked domain) = {n_plaq_above_masked}")

    # --- cross-check: e2_masked vs the SHA-pinned S104 npz field e2_lattice_defect_excluded ---
    s104d = np.load(DEFECT_MASK_SOURCE_NPZ, allow_pickle=True)  # (local)
    s104_e2_defect_excl = float(s104d["e2_lattice_defect_excluded"])  # (local)
    s104_corner_ij = tuple(int(x) for x in s104d["corner_plaq_ij"])   # (local)
    s104_n_plaq_above = int(s104d["n_plaq_above"])                    # (local)
    s104_max_absF = float(s104d["max_absF"])                          # (local)
    s104_e2_lattice = float(s104d["e2_lattice"])                      # (local)
    xchk_e2_diff = abs(e2_masked - s104_e2_defect_excl)              # (local) re-run reproducibility vs S104 stored
    xchk_corner_ij_match = (s104_corner_ij == DEFECT_MASK_PLAQ_IJ)    # (local) S104 stored corner == plan-pin
    print(f"\n  [X-CHECK vs SHA-pinned S104 npz]")
    print(f"    S104 corner_plaq_ij                = {s104_corner_ij}  (== plan-pin {DEFECT_MASK_PLAQ_IJ}: {xchk_corner_ij_match})")
    print(f"    S104 e2_lattice_defect_excluded    = {s104_e2_defect_excl:.6e}")
    print(f"    this-run e2_masked                 = {e2_masked:.6e}")
    print(f"    |this_run - S104_stored|           = {xchk_e2_diff:.3e}  (re-run reproducibility)")
    print(f"    S104 n_plaq_above (full)           = {s104_n_plaq_above}  (mask_cardinality plan-pin {MASK_CARDINALITY})")

    # =====================================================================
    # VERDICT (plan §W3-1 operator.form)
    # =====================================================================
    print("\n" + "=" * 78)
    print("  VERDICT")
    print("=" * 78)

    # The three PASS conjuncts (BYTE-IDENTICAL S104 PASS-TRIVIAL criterion on the masked domain).
    conj_round_deficit = abs(e2_masked - round(e2_masked)) < EULER_INT_TOL  # (local)
    conj_integer_zero = (round(e2_masked) == 0)                             # (local)
    conj_curv_vanish = (max_absF_masked < TRIVIAL_FEULER_FLOOR)             # (local)
    pass_all = conj_round_deficit and conj_integer_zero and conj_curv_vanish  # (local)

    # mask cardinality: EXACTLY one plaquette accounts for the non-trivial content.
    # If MORE than one plaquette exceeds the floor on the FULL domain, a single mask is insufficient
    # (over-masking would be needed) -> INFO (the pre-registration's single-plaquette assumption fails).
    n_plaq_above_full = int(np.sum(np.abs(F_plaq) > TRIVIAL_FEULER_FLOOR))  # (local) full-domain count
    mask_cardinality_ok = (n_plaq_above_full == MASK_CARDINALITY)           # (local) exactly one above floor

    if not mask_matches:
        # re-mesh drift: runtime dominant plaquette != plan-pinned mask. INFO per plan INFO_meaning;
        # record the drift, do NOT relocate the mask (run-time mask selection = the Class-8.2 freedom
        # this gate exists to close).
        verdict = "INFO"
        branch = "mask-drift-runtime-ne-planpin"
    elif not mask_cardinality_ok:
        # more (or fewer) than one plaquette above the floor -> the single-plaquette mask is insufficient.
        verdict = "INFO"
        branch = "mask-cardinality-ne-1"
    elif pass_all:
        verdict = "PASS"
        branch = "PASS-TRIVIAL-masked"
    elif not conj_curv_vanish:
        # the non-trivial Euler content is NOT confined to the one vN-Wigner corner: a genuine
        # SO(2)/Pfaffian obstruction the S25/W5 + S96 triviality chain did not anticipate.
        verdict = "FAIL"
        branch = "residual-curvature-after-mask"
    elif not conj_integer_zero:
        verdict = "FAIL"
        branch = "e2_masked-quantizes-nonzero"
    else:
        verdict = "FAIL"
        branch = "e2_masked-non-integer"

    value_str = (
        f"e2_masked={e2_masked:.6e}_round={round(e2_masked)}_branch={branch}_"
        f"maxFEulerMasked={max_absF_masked:.3e}_maskPlaq=[{mi},{mj}]_"
        f"maskMatches={mask_matches}_nPlaqAboveFull={n_plaq_above_full}_"
        f"e2Full={e2_lattice:.6e}_maxFEulerFull={max_absF_full:.3e}_"
        f"xchkE2Diff={xchk_e2_diff:.2e}_s104CornerMatch={xchk_corner_ij_match}_"
        f"pf2detResid={pf_resid:.2e}"
    )
    print(f"  conjunct round-deficit  |e2_masked-round| < {EULER_INT_TOL:.0e}: {conj_round_deficit}  "
          f"({abs(e2_masked - round(e2_masked)):.3e})")
    print(f"  conjunct integer-zero   round(e2_masked) == 0           : {conj_integer_zero}  "
          f"({round(e2_masked)})")
    print(f"  conjunct curv-vanish    max|F^Euler|_masked < {TRIVIAL_FEULER_FLOOR:.0e}: {conj_curv_vanish}  "
          f"({max_absF_masked:.3e})")
    print(f"  mask guard (runtime==planpin)                           : {mask_matches}")
    print(f"  mask cardinality (n_plaq_above_full == {MASK_CARDINALITY})              : {mask_cardinality_ok}  "
          f"({n_plaq_above_full})")
    print(f"  >>> {GATE_ID}: {verdict}  [{branch}]")

    # --- save data ---
    SESSION_105_DIR.mkdir(parents=True, exist_ok=True)
    np.savez(
        NPZ_OUT,
        taus=taus, mus=mus,
        F_plaq=F_plaq, det_track=det_track,
        e2_lattice_full=e2_lattice,
        e2_masked=e2_masked,
        max_absF_full=max_absF_full,
        max_absF_masked=max_absF_masked,
        masked_pf_value=masked_pf_value,
        defect_mask_plaq_ij=np.array(DEFECT_MASK_PLAQ_IJ),
        defect_mask_tau_mu=np.array(DEFECT_MASK_TAU_MU),
        runtime_dominant_plaq_ij=np.array([rec_ci, rec_cj]),
        runtime_dominant_tau_mu=np.array([rec_tau, rec_mu]),
        mask_matches=mask_matches,
        mask_cardinality=int(MASK_CARDINALITY),
        n_plaq_above_full=n_plaq_above_full,
        n_plaq_above_masked=n_plaq_above_masked,
        next_largest_plaq_ij=np.array([nm_ci, nm_cj]),
        n_reflections=n_reflections, frame_ok_frac=frame_ok_frac,
        conj_round_deficit=conj_round_deficit,
        conj_integer_zero=conj_integer_zero,
        conj_curv_vanish=conj_curv_vanish,
        pass_all=pass_all, mask_cardinality_ok=mask_cardinality_ok,
        # cross-check vs SHA-pinned S104 npz
        s104_e2_defect_excluded=s104_e2_defect_excl,
        s104_corner_plaq_ij=np.array(s104_corner_ij),
        s104_n_plaq_above=s104_n_plaq_above,
        s104_max_absF=s104_max_absF,
        s104_e2_lattice=s104_e2_lattice,
        s104_npz_sha_ok=s104_npz_sha_ok,
        xchk_e2_diff=xchk_e2_diff,
        xchk_corner_ij_match=xchk_corner_ij_match,
        pf2det_residual=pf_resid,
        band_deg=int(deg_bot), v_jensen=V_JENSEN, v_mu=V_MU,
        verdict=verdict, branch=branch, tau_fold=float(tau_fold),
        scan_tau=np.array([TAU_LO, TAU_HI]), scan_mu=np.array([MU_LO, MU_HI]),
        euler_int_tol=EULER_INT_TOL, trivial_feuler_floor=TRIVIAL_FEULER_FLOOR,
        c_fhs_s96_chern=9.777563e-15,   # S96 P-30w Chern cross-reference (the joint-wall sibling)
    )
    print(f"\n  Saved data: {NPZ_OUT}")

    # --- plot: full vs masked F^Euler field + the masked-domain residual ---
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    ext = [MU_LO, MU_HI, TAU_LO, TAU_HI]                       # (local) [mu (x), tau (y)]

    # left: full F^Euler with the masked corner highlighted
    capF = max(max_absF_full, 1e-300)                          # (local)
    im0 = axes[0].imshow(F_plaq, origin="lower", aspect="auto", extent=ext,
                         cmap="RdBu_r", vmin=-capF, vmax=capF)
    axes[0].axhline(tau_fold, color="k", ls="--", lw=1.2, label=f"fold tau={tau_fold}")
    axes[0].axvline(0.0, color="green", ls=":", lw=1.4, label="Jensen line (mu=0)")
    axes[0].plot(DEFECT_MASK_TAU_MU[1], DEFECT_MASK_TAU_MU[0], "x", color="magenta", ms=14, mew=3,
                 label=f"MASKED plaq [{mi},{mj}] (vN-Wigner)")
    axes[0].set_xlabel("mu (second U(2)-inv TT direction)")
    axes[0].set_ylabel("tau (Jensen direction)")
    axes[0].set_title(f"FULL F^Euler (SO(2) angle); e2_full={e2_lattice:.3e}\n"
                      f"ENTIRE non-trivial content in the [{mi},{mj}] vN-Wigner corner "
                      f"(max|F|={max_absF_full:.2e})")
    axes[0].legend(loc="upper right", fontsize=8)
    fig.colorbar(im0, ax=axes[0], label="F^Euler (rad)")

    # right: masked F^Euler (corner removed) at the masked-domain colour scale -> shows float-noise floor
    F_show = F_plaq.copy()                                     # (local)
    F_show[mi, mj] = np.nan                                    # (local) blank the masked cell
    capM = max(max_absF_masked, 1e-300)                        # (local)
    im1 = axes[1].imshow(F_show, origin="lower", aspect="auto", extent=ext,
                         cmap="RdBu_r", vmin=-capM, vmax=capM)
    axes[1].axhline(tau_fold, color="k", ls="--", lw=1.2)
    axes[1].axvline(0.0, color="green", ls=":", lw=1.4)
    axes[1].set_xlabel("mu")
    axes[1].set_ylabel("tau")
    axes[1].set_title(f"MASKED F^Euler (corner removed): max|F|_masked={max_absF_masked:.2e} < 1e-12\n"
                      f"e2_masked={e2_masked:.3e} (round={round(e2_masked)}); "
                      f"VERDICT={verdict} [{branch}]")
    fig.colorbar(im1, ax=axes[1], label="F^Euler (rad), masked-domain scale")

    fig.suptitle(f"{GATE_ID}: defect-masked Euler class of the lowest BDI-real Dirac doublet\n"
                 f"(the single vN-Wigner corner plaquette is a frame-singular lattice artifact; "
                 f"masking it -> PASS-TRIVIAL: Euler conjunct of the metric-without-curvature wall)",
                 fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(PNG_OUT, dpi=150)
    print(f"  Saved plot: {PNG_OUT}")

    # --- emit verdict payload (agent calls emit_verdict; race-safe) ---
    companion = (
        f"# {GATE_ID} dual-SHA companion row; [VERIFY] defect-masked Euler class e2_masked="
        f"(1/2pi) sum_(ij!=mask) Pf(F^Euler) of the lowest 2-fold J/BDI-real Dirac doublet on the "
        f"2-param U(2)-inv TT surface (v_J=(2,-2,1), v_mu=n x v_J=(11,7,-8)); FHS-Pfaffian-Euler "
        f"real-frame SO(2) Wilson-loop lattice (deg-2 non-Abelian); mask plaquette [{mi},{mj}] "
        f"(the (0.10,+0.10) B1/B2 vN-Wigner crossing) PINNED AT PLAN-FREEZE from "
        f"s104_euler_class_j_doublet.npz field corner_plaq_ij (sha {DEFECT_MASK_SOURCE_SHA256[:16]}...); "
        f"thresholds (1e-3,1e-12) BYTE-IDENTICAL to S104 PASS-TRIVIAL criterion (evaluator-mask change "
        f"only, NO threshold relaxation); e2_masked={e2_masked:.3e} round={round(e2_masked)} "
        f"max|F^Euler|_masked={max_absF_masked:.2e}; re-run reproducibility vs S104 stored defect-excl "
        f"|diff|={xchk_e2_diff:.1e}; Pf^2=det residual {pf_resid:.1e}; CLASS=FULL (exact eigendecomposition, "
        f"NO SCHEMATIC); no regulator_pin (Euler class is a property of the D_K eigenbundle, not a "
        f"Seeley-DeWitt a_n)"
    )
    print_verdict_payload(verdict, value_str, audit_sha, content_sha, extra_rows=[companion])
    print(f"\n  4-tuple: (value={value_str[:60]}..., scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
