#!/usr/bin/env python3
"""
S101 W3-2 — S101-NU-DIRAC-OFFDIAG-TEXTURE
=========================================

Gate: S101-NU-DIRAC-OFFDIAG-TEXTURE ([VERIFY])
Classification: PARTICLE
Agent: dirac-antimatter-theorist

Pre-registered three-clause AND threshold (plan §W3-2, lines 318-327):
  Clause 1 (shape): |S - 2.4882512| / 2.4882512 <= 0.01
                    S = (d + |w|)/(d - |w|), the unit-pinned doublet split ratio.
  Clause 2 (scale): |Y2_texture / Y2_S99 - 1| <= 0.05 at substrate-natural norm.
  Clause 3 (rank):  |s|^2-channel (0,0)<->(1,1) element = 0 at 1e-12 THEOREM tol.
  PASS  = 1 AND 2 AND 3
  INFO  = 1 AND 3, NOT 2
  FAIL  = unit-pinned x = |w|/d outside [0.405, 0.449]  OR  clause 3 violated.

  Composite collapse (gate-verdicts.md schema-v2) is applied to the 3-tuple
  (sign / magnitude / regime) when the literal PASS/INFO/FAIL triggers leave a
  gap (x inside window but shape band missed): magnitude_verdict==FAIL with
  regime_verdict==VALID collapses to composite FAIL.

GOVERNING STRUCTURE (Dirac / NCG, substrate-first)
--------------------------------------------------
The doublet-split off-diagonal texture on the (1,0)+(0,1) fund<->antifund
doublet is

      m_D  ∝  [[ d ,  w  ],
               [ w*,  d  ]]           (the 2x2 BDI block)

The diagonal equality d1 = d2 = d is NOT an ansatz: it is J-reality.  The real
structure J = charge conjugation acts on the (1,0)/(0,1) conjugate pair; the
S99 BDI reality adjudication forces [J, m_D] = 0 on this pair, which equalizes
the doublet diagonals (W2-2 npz machine witness bdi_pair_max_rel_dev ~ 3.7e-15,
bdi_pair_O_rel_dev ~ 1.08e-15).  This is the SAME J whose compatibility with
D_K (JD_K = D_K J, KO-dim 6) enforces m(particle) = m(antiparticle): here it
enforces the doublet symmetry.  w is unconstrained including its phase
(arg w = second-Z3 ∈ {π, ±2π/3}); the 2x2 eigenvalue split depends on |w| only.

  eigenvalues  =  d ± |w|     (2x2 exact; phase of w absorbable in the 2x2;
                              full 3x3 phase fate is gate 5's question, NOT here)
  gen 3 (heavy) =  d + |w|
  gen 2 (light) =  d - |w|
  gen 1         =  (0,0) decoupled, m1 = 0  CG-protected at s-linear order
                  [(2,0) x (0,0) = (2,0) != (0,1)]

  |w| = 1/sqrt(6)  is Weingarten-exact Haar geometry on the Jensen fiber
       (counting-INDEPENDENT per the W-2 unit ruling B6(iii)).

STEP A — the ONLY new computation: unit pin of the diagonal d
-------------------------------------------------------------
The as-computed system tags the diagonal d-entries RATIO-BLOCKSUM (extensive:
a block SUM over the sector modes, eps_lx_block_phi0 diagonal = O_g[0] = 8.2065)
while the off-diagonal |w| = 1/sqrt(6) is per-mode (intensive).  These are
DIFFERENT unit systems — the W-2 issue.  To form the seesaw split both must sit
in ONE system.

Per the Counting-axis discipline (regulator-pin-discipline.md §"Counting"):
RATIO-NORMALIZED-TRACE-MEAN = blocksum / multiplicity n_g (intensive, per-mode).
The off-diagonal is ALREADY per-mode, so it is INVARIANT under the retag (this
IS its "counting-INDEPENDENT" property).  The diagonal retags to its per-mode
trace mean = the kernel mean per mode.  The W-2 npz pins this number exactly:
kernel_mean_unit = 1.0 — the kernel is normalized so the per-mode (trace-mean)
diagonal amplitude is exactly 1.0 in the units where |w| = 1/sqrt(6).  Hence

      d_trace_mean = kernel_mean_unit = 1.0
      |w|          = 1/sqrt(6)                 (unchanged)
      x = |w| / d  = 1/sqrt(6) / 1 = 0.4082483

(Cross-check: the MIXED reading x = |w| / O_g[0] = 0.0497 is unphysical —
it couples an intensive numerator to an extensive denominator.  The plan
substitution-chain Step 5 names x_raw = 0.408248 at the AS-COMPUTED d = 1,
which is exactly kernel_mean_unit.)

STEP B/C — seesaw split and scale
---------------------------------
S(x) = (1+x)/(1-x), monotone increasing on (0,1), heavy = +|w| branch.
The seesaw m_nu = m_D^T M_R^{-1} m_D with diagonal M_R does NOT alter the
DIAGONAL-d-vs-OFF-DIAGONAL-w split STRUCTURE on the doublet (M_R diagonal acts
as a per-gen scalar; the Yukawa split ratio is the m_D eigenvalue ratio).  The
scale clause compares Y2_texture (= light doublet eigenvalue d - |w| in
substrate-natural normalization, lifted to the S99 Yukawa scale) against
Y2_S99 = 4.793566 (md_normalization npz).

STEP D — rank-deficiency sub-criterion
--------------------------------------
The (0,0)<->(1,1) |s|^2-channel is CG-ADMISSIBLE [(0,2) x (2,0) ⊇ (1,1)], so
its ABSENCE is a CONSTRAINT to verify, not an automatic property.  The W-2 npz
proves the channel vanishes (w_chain_zero_proof; M12_inner = 0; center-Z3 Haar
invariance + triality-0 kernel cannot connect t=1 to t=0).  Any nonzero value
there lifts m1 = 0 and FAILS clause 3.

Inputs (SHA-256 dual-pinned at runtime):
  - computations/session-100a/s100a_yukawa_overlap_offdiag.npz  (|w|, arg w, d, BDI witness)
  - computations/session-100a/s100a_md_normalization.npz        (M_R, Y_S99, shapes)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH SHAs)

Output 4-tuple:
  (value=<S_pinned>, scheme=TYPE-I-SEESAW-DOUBLET-SPLIT-OFFDIAG-W22-TEXTURE,
   convention=RATIO-NORMALIZED-TRACE-MEAN-UNITPIN-OFFDIAG-INVARIANT-DIAG-RETAGGED,
   L_max=N/A)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
import sys
from pathlib import Path as _Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# _shared (holding canonical_constants.py) added to sys.path before the import.
_SHARED = _Path(__file__).resolve().parents[1] / "_shared"
sys.path.insert(0, str(_SHARED))
from canonical_constants import M_KK, v_ew  # noqa: F401,E402  (substrate scales; documented use)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
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

SESSION = "S101"                                                       # (local)
GATE_ID = "S101-NU-DIRAC-OFFDIAG-TEXTURE"                              # (local)
SCHEME = "TYPE-I-SEESAW-DOUBLET-SPLIT-OFFDIAG-W22-TEXTURE"             # (local)
CONVENTION = (
    "RATIO-NORMALIZED-TRACE-MEAN-UNITPIN-OFFDIAG-INVARIANT-DIAG-RETAGGED"
)                                                                     # (local)
L_MAX = "N/A"                                                         # (local)

# Pre-registered thresholds (plan §W3-2)
S_REQUIRED = 2.4882511868262607          # required gen3/gen2 split ratio   # (local)
SHAPE_TOL = 0.01                         # clause-1 RATIO tolerance         # (local)
SCALE_TOL = 0.05                         # clause-2 RATIO tolerance         # (local)
RANK_TOL = 1e-12                         # clause-3 THEOREM tolerance       # (local)
X_WINDOW = (0.405, 0.449)                # binding |w|/d window (FAIL trigger)  # (local)

# Input npz (session-100a) — pinned SHAs from plan §W3-2 input_files
YUKAWA_NPZ = COMPUTATIONS_DIR / "session-100a" / "s100a_yukawa_overlap_offdiag.npz"  # (local)
MD_NPZ = COMPUTATIONS_DIR / "session-100a" / "s100a_md_normalization.npz"            # (local)
PIN_YUKAWA_SHA = "23d386dfa7e6d54d11006bd6d631fa860c156ea223e9c36b9b21eb6f3217dba2"  # (local)
PIN_MD_SHA = "0b3245b643a127bffac6274b5dad03cd9addd6efa1a5c73ad932142fe9794154"      # (local)

OUT_NPZ = SESSION_DIR / "s101_nu_dirac_offdiag_texture.npz"
OUT_PNG = SESSION_DIR / "s101_nu_dirac_offdiag_texture.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    YUKAWA_NPZ,
    MD_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
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
    # Extra pinmap entropy: the unit-pin procedure + window + tolerances
    # (plan audit_sha256_inputs lists "pinmap (unit-pin procedure, window, tolerances)").
    pinmap_extra = {  # (local)
        "unit_pin": "diag=RATIO-BLOCKSUM->RATIO-NORMALIZED-TRACE-MEAN(kernel_mean_unit); offdiag=counting-INDEPENDENT(1/sqrt6)",
        "x_window": list(X_WINDOW),
        "shape_tol": SHAPE_TOL,
        "scale_tol": SCALE_TOL,
        "rank_tol": RANK_TOL,
        "S_required": S_REQUIRED,
    }
    pins_full = dict(pins)  # (local)
    pins_full["__pinmap_extra__"] = json.dumps(pinmap_extra, sort_keys=True)
    pinmap_json = json.dumps(
        dict(sorted(pins_full.items())), separators=(",", ":"), sort_keys=True
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
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # ---- Load W-2 npz scalars (ground truth) ----
    yk = np.load(YUKAWA_NPZ, allow_pickle=True)  # (local)
    md = np.load(MD_NPZ, allow_pickle=True)      # (local)

    # SHA reconciliation against plan pins (drift guard)
    yk_sha = sha256_of(YUKAWA_NPZ)               # (local)
    md_sha = sha256_of(MD_NPZ)                   # (local)
    sha_ok = (yk_sha == PIN_YUKAWA_SHA) and (md_sha == PIN_MD_SHA)  # (local)
    print(f"  npz SHA reconciliation: yukawa={'OK' if yk_sha==PIN_YUKAWA_SHA else 'DRIFT'}, "
          f"md={'OK' if md_sha==PIN_MD_SHA else 'DRIFT'}")

    # ---- STEP A: unit pin (the ONLY new computation) ----
    # Off-diagonal: counting-INDEPENDENT, substrate-exact 1/sqrt(6).
    abs_w_phi = np.asarray(yk["abs_w_phi"], dtype=float)  # (local) [1/sqrt6 x3]
    abs_w = float(abs_w_phi[0])                            # (local)
    abs_w_exact = 1.0 / np.sqrt(6.0)                       # (local)
    w_matches_exact = abs(abs_w - abs_w_exact) < 1e-14     # (local)
    arg_w = np.asarray(yk["arg_w_M2_phi"], dtype=float)    # (local) [pi, +2pi/3, -2pi/3]

    # Diagonal as-computed (RATIO-BLOCKSUM class): d-vector & block sums.
    d_blocksum_ratio = np.asarray(yk["d_i"], dtype=float)  # (local) RATIO-BLOCKSUM
    O_g = np.asarray(yk["O_g"], dtype=float)               # (local) raw block SUMS
    kernel_mean_unit = float(yk["kernel_mean_unit"])       # (local) per-mode trace mean = 1.0

    # The trace-mean (intensive, per-mode) diagonal amplitude in the SAME units
    # as |w| is the kernel mean per mode, pinned by the W-2 npz to 1.0.
    # SUBSTITUTION CHAIN (Step A):
    #   d_blocksum (extensive) = O_g[0] = 8.2065   [eps_lx diagonal, RATIO-BLOCKSUM]
    #   d_trace_mean (intensive) = blocksum / n_modes = kernel_mean_unit = 1.0
    #   |w| (intensive, per-mode) UNCHANGED = 1/sqrt(6)        [counting-INDEPENDENT]
    #   => x = |w| / d_trace_mean = (1/sqrt6) / 1
    d_trace_mean = kernel_mean_unit                         # (local) == 1.0
    # MIXED (wrong) reading retained as an explicit cross-check witness:
    x_mixed = abs_w / float(O_g[0])                         # (local) couples intensive/extensive
    # Pinned (correct) reading:
    x_pinned = abs_w / d_trace_mean                         # (local) = 1/sqrt6

    # ---- STEP B: seesaw split ratio ----
    # eigenvalues = d +/- |w|; heavy = d+|w| (gen3); light = d-|w| (gen2).
    lam_heavy = d_trace_mean + abs_w                        # (local) gen3
    lam_light = d_trace_mean - abs_w                        # (local) gen2
    S_pinned = lam_heavy / lam_light                        # (local) = (1+x)/(1-x)
    # closed-form check: S = (sqrt6+1)^2 / 5 when d=1, w=1/sqrt6
    S_closed = (np.sqrt(6.0) + 1.0) ** 2 / 5.0              # (local)
    # required x from required S
    x_required = (S_REQUIRED - 1.0) / (S_REQUIRED + 1.0)    # (local) = 0.4266468...

    shape_dev = (S_pinned - S_REQUIRED) / S_REQUIRED        # (local) signed
    shape_abs = abs(shape_dev)                              # (local)
    clause1_shape = shape_abs <= SHAPE_TOL                  # (local)

    # ---- STEP C: scale clause (substrate-natural normalization) ----
    # Y_S99 from md npz: [0, 4.793566, 11.927596]. The texture's light/heavy
    # Yukawa in substrate-natural norm: normalize the doublet eigenvalues so the
    # HEAVY gen3 equals Y3_S99 (substrate-natural pin = gen3 anchor), then read
    # Y2_texture = (d-|w|)/(d+|w|) * Y3_S99 and compare to Y2_S99.
    Y_S99 = np.asarray(md["Y_S99"], dtype=float)            # (local) [0, Y2, Y3]
    Y2_S99 = float(Y_S99[1])                                # (local) 4.793566
    Y3_S99 = float(Y_S99[2])                                # (local) 11.927596
    # substrate-natural: pin the heavy texture eigenvalue to Y3_S99
    scale_pin = Y3_S99 / lam_heavy                          # (local) lift factor
    Y2_texture = lam_light * scale_pin                      # (local) = S99-lifted light eig
    Y3_texture = lam_heavy * scale_pin                      # (local) = Y3_S99 by construction
    scale_dev = abs(Y2_texture / Y2_S99 - 1.0)              # (local)
    clause2_scale = scale_dev <= SCALE_TOL                  # (local)
    # NOTE: the texture's Y2/Y3 = 1/S_pinned, while S99's Y2/Y3 = Y2_S99/Y3_S99.
    # When shape is off (S != S_required), Y2_texture necessarily misses Y2_S99 —
    # the scale clause is downstream of the shape clause for this texture.

    # ---- STEP D: rank-deficiency sub-criterion ----
    # The (0,0)<->(1,1) |s|^2-channel must be exactly zero. The W-2 npz proves
    # this two ways: M12_inner (inner product of the M1, M2 channels) and the
    # w_chain_literal_t0 (center-Z3 chain value). Both must be 0 at THEOREM tol.
    M12_inner = float(yk["M12_inner"])                      # (local) channel overlap
    w_chain_literal_t0 = float(yk["w_chain_literal_t0"])    # (local) center-Z3 chain
    conj_split = float(md["conj_split"])                    # (local) m1=0 conj cleanliness
    rank_channel = max(abs(M12_inner), abs(w_chain_literal_t0))  # (local) the |s|^2 element
    clause3_rank = rank_channel <= RANK_TOL                 # (local)

    # ---- explicit 3x3 m_D embedding for the rank check ----
    # Row/col order: gen1 = (0,0); gen2,gen3 = doublet (1,0)/(0,1) split states.
    # We build the m_D in the DOUBLET-EIGENBASIS (already diagonalized 2x2) so
    # gen2 = lam_light, gen3 = lam_heavy on the diagonal; the (0,0)<->(1,1)
    # off-diagonal element is the |s|^2-channel value (must be 0).
    m_D_3x3 = np.zeros((3, 3), dtype=float)                 # (local)
    m_D_3x3[0, 0] = 0.0                                     # (local) m1 = 0 (CG-protected)
    m_D_3x3[1, 1] = lam_light                               # (local) gen2 = d-|w|
    m_D_3x3[2, 2] = lam_heavy                               # (local) gen3 = d+|w|
    # The CG-admissible-but-must-vanish (0,0)<->(1,1) channel:
    m_D_3x3[0, 1] = rank_channel                            # (local) = 0 by W-2 proof
    m_D_3x3[1, 0] = rank_channel                            # (local) symmetric
    # rank of m_D: m1=0 => rank 2 (rank-deficient by 1) iff the (0,1) element is 0.
    svals = np.linalg.svd(m_D_3x3, compute_uv=False)        # (local) 3x3, tiny
    n_zero_sv = int(np.sum(svals <= RANK_TOL))              # (local)
    rank_mD = int(np.sum(svals > RANK_TOL))                 # (local)
    rank_deficient_ok = (rank_mD == 2) and (n_zero_sv >= 1) and clause3_rank  # (local)

    # ---- BDI reality witness (J-compatibility) ----
    bdi_max_rel_dev = float(yk["bdi_pair_max_rel_dev"])     # (local) ~3.7e-15
    bdi_O_rel_dev = float(yk["bdi_pair_O_rel_dev"])         # (local) ~1.08e-15
    d1_eq_d2_witness = bdi_max_rel_dev < 1e-12              # (local)

    # ---- direction read-off (substitution chain Step 4) ----
    # dS/dx = 2/(1-x)^2 > 0 => monotone increasing, heavy = +|w| branch, S > 1.
    dS_dx = 2.0 / (1.0 - x_pinned) ** 2                     # (local) > 0
    sign_ok = (S_pinned > 1.0) and (lam_heavy > lam_light) and (dS_dx > 0.0)  # (local)

    return {
        "value": float(S_pinned),
        # Step A
        "abs_w": abs_w,
        "abs_w_exact": float(abs_w_exact),
        "w_matches_exact": bool(w_matches_exact),
        "arg_w": arg_w.tolist(),
        "d_blocksum_ratio": d_blocksum_ratio.tolist(),
        "O_g": O_g.tolist(),
        "kernel_mean_unit": kernel_mean_unit,
        "d_trace_mean": float(d_trace_mean),
        "x_mixed_wrong": float(x_mixed),
        "x_pinned": float(x_pinned),
        # Step B
        "lam_heavy": float(lam_heavy),
        "lam_light": float(lam_light),
        "S_pinned": float(S_pinned),
        "S_closed": float(S_closed),
        "x_required": float(x_required),
        "shape_dev": float(shape_dev),
        "shape_abs": float(shape_abs),
        "clause1_shape": bool(clause1_shape),
        # Step C
        "Y2_S99": Y2_S99,
        "Y3_S99": Y3_S99,
        "Y2_texture": float(Y2_texture),
        "Y3_texture": float(Y3_texture),
        "scale_dev": float(scale_dev),
        "clause2_scale": bool(clause2_scale),
        # Step D
        "M12_inner": M12_inner,
        "w_chain_literal_t0": w_chain_literal_t0,
        "conj_split": conj_split,
        "rank_channel": float(rank_channel),
        "clause3_rank": bool(clause3_rank),
        "m_D_3x3": m_D_3x3.tolist(),
        "svals": svals.tolist(),
        "rank_mD": rank_mD,
        "n_zero_sv": n_zero_sv,
        "rank_deficient_ok": bool(rank_deficient_ok),
        # BDI / direction
        "bdi_max_rel_dev": bdi_max_rel_dev,
        "bdi_O_rel_dev": bdi_O_rel_dev,
        "d1_eq_d2_witness": bool(d1_eq_d2_witness),
        "dS_dx": float(dS_dx),
        "sign_ok": bool(sign_ok),
        # window
        "x_in_window": bool(X_WINDOW[0] <= x_pinned <= X_WINDOW[1]),
        "sha_ok": bool(sha_ok),
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict (three-clause AND + schema-v2 collapse) + 4-tuple
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def evaluate_gate(r: dict) -> dict:
    """Apply the pre-registered three-clause AND, then the schema-v2 3-tuple
    composite collapse. Returns dict with composite + sign/magnitude/regime."""
    c1 = r["clause1_shape"]   # shape  (local)
    c2 = r["clause2_scale"]   # scale  (local)
    c3 = r["clause3_rank"] and r["rank_deficient_ok"]   # rank  (local)
    x_in = r["x_in_window"]   # (local)

    # ---- Literal pre-registered triggers (plan lines 324-327) ----
    literal_PASS = c1 and c2 and c3                          # (local)
    literal_INFO = c1 and c3 and (not c2)                   # (local)
    literal_FAIL = (not x_in) or (not c3)                   # (local)

    # ---- schema-v2 3-tuple (the canonical tiebreaker; gate-verdicts.md) ----
    # sign_verdict: predicted direction (S>1, heavy=+|w|, dS/dx>0) — structurally forced.
    sign_verdict = "PASS" if r["sign_ok"] else "FAIL"       # (local)
    # magnitude_verdict: clause-1 shape band IS the magnitude test.
    #   PASS iff shape within band; (no separate info_band on shape) FAIL otherwise.
    magnitude_verdict = "PASS" if c1 else "FAIL"            # (local)
    # regime_verdict: VALID iff the unit-pin conversion is single-valued under W-2.
    #   The W-2 ruling fixes BOTH legs unambiguously (offdiag counting-INDEPENDENT;
    #   diagonal trace-mean = kernel_mean_unit = 1.0). No second admissible reading
    #   for d. Rank sub-criterion holding confirms no smuggled channel. => VALID.
    regime_ok = r["d1_eq_d2_witness"] and c3 and r["w_matches_exact"] and r["sha_ok"]  # (local)
    regime_verdict = "VALID" if regime_ok else "MARGINAL"  # (local)

    # ---- composite collapse rule (gate-verdicts.md; PRE-REGISTERED) ----
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    # Consistency: literal triggers must agree in DIRECTION with the collapse.
    # literal_PASS would require c1 (shape) which is the magnitude test; if c1
    # fails, literal_PASS/INFO are both excluded, and the collapse routes via
    # magnitude. If x is inside window (literal_FAIL not fired by window) the
    # collapse is the binding verdict on the tighter +/-1% shape band.
    return {
        "composite": composite,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "c1_shape": bool(c1),
        "c2_scale": bool(c2),
        "c3_rank": bool(c3),
        "x_in_window": bool(x_in),
        "literal_PASS": bool(literal_PASS),
        "literal_INFO": bool(literal_INFO),
        "literal_FAIL_window_or_rank": bool(literal_FAIL),
    }


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None) -> dict:
    payload = {  # (local)
        "session": 101,
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


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict, gate: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))

    # Left: S(x) = (1+x)/(1-x) with the pinned and required points.
    xs = np.linspace(0.30, 0.50, 400)                       # (local)
    Ss = (1.0 + xs) / (1.0 - xs)                            # (local)
    ax1.plot(xs, Ss, "b-", lw=2, label=r"$S(x)=(1+x)/(1-x)$")
    ax1.axhline(S_REQUIRED, color="green", ls="--", lw=1.4,
                label=f"required $S$ = {S_REQUIRED:.5f}")
    ax1.axhline(S_REQUIRED * (1 - SHAPE_TOL), color="green", ls=":", lw=0.8, alpha=0.6)
    ax1.axhline(S_REQUIRED * (1 + SHAPE_TOL), color="green", ls=":", lw=0.8, alpha=0.6,
                label=r"$\pm1\%$ shape band")
    ax1.axvspan(X_WINDOW[0], X_WINDOW[1], color="orange", alpha=0.12,
                label=f"FAIL window [{X_WINDOW[0]},{X_WINDOW[1]}]")
    ax1.plot([r["x_pinned"]], [r["S_pinned"]], "ro", ms=10,
             label=f"pinned $x$=1/√6={r['x_pinned']:.5f}, $S$={r['S_pinned']:.5f}")
    ax1.plot([r["x_required"]], [S_REQUIRED], "g^", ms=10,
             label=f"required $x$={r['x_required']:.5f}")
    ax1.annotate("", xy=(r["x_required"], S_REQUIRED),
                 xytext=(r["x_pinned"], r["S_pinned"]),
                 arrowprops=dict(arrowstyle="->", color="red", lw=1.2))
    ax1.set_xlabel(r"$x = |w|/d$  (trace-mean unit pin)")
    ax1.set_ylabel(r"split ratio $S = \lambda_{heavy}/\lambda_{light}$")
    ax1.set_title(f"Doublet split: shape dev = {r['shape_dev']*100:+.3f}%  "
                  f"(clause1 {'PASS' if gate['c1_shape'] else 'FAIL'})")
    ax1.legend(fontsize=7.5, loc="upper left")
    ax1.grid(alpha=0.3)

    # Right: the 2x2 / 3x3 texture + clause table.
    ax2.axis("off")
    txt = []  # (local)
    txt.append("m_D (doublet block) = [[d, w], [w*, d]]   "
               f"d (trace-mean) = {r['d_trace_mean']:.4f}")
    txt.append(f"|w| = 1/√6 = {r['abs_w']:.7f}  (counting-INDEPENDENT)")
    txt.append(f"arg w = {[round(a,4) for a in r['arg_w']]}  (second-Z3)")
    txt.append("")
    txt.append("STEP A unit pin (RATIO-BLOCKSUM → RATIO-NORM-TRACE-MEAN):")
    txt.append(f"   d_blocksum = O_g[0] = {r['O_g'][0]:.4f}  (extensive)")
    txt.append(f"   d_trace_mean = kernel_mean_unit = {r['d_trace_mean']:.4f}  (intensive)")
    txt.append(f"   x_pinned = |w|/d = {r['x_pinned']:.6f}   "
               f"(MIXED-wrong x = {r['x_mixed_wrong']:.5f})")
    txt.append("")
    txt.append(f"S_pinned = (√6+1)²/5 = {r['S_closed']:.6f}")
    txt.append(f"required x = {r['x_required']:.6f}  (x sits "
               f"{(r['x_required']-r['x_pinned'])/r['x_required']*100:.2f}% below)")
    txt.append("")
    txt.append("CLAUSES:")
    txt.append(f"  1 shape  |S−2.4883|/2.4883 = {r['shape_abs']:.5f} ≤ 0.01  "
               f"→ {'PASS' if gate['c1_shape'] else 'FAIL'}")
    txt.append(f"  2 scale  |Y2_tex/Y2_S99−1| = {r['scale_dev']:.5f} ≤ 0.05  "
               f"→ {'PASS' if gate['c2_scale'] else 'FAIL'}")
    txt.append(f"  3 rank   |s|²(0,0)↔(1,1) = {r['rank_channel']:.2e} ≤ 1e-12  "
               f"→ {'PASS' if gate['c3_rank'] else 'FAIL'}")
    txt.append(f"     rank(m_D)={r['rank_mD']} (m1=0; svals min={min(r['svals']):.2e})")
    txt.append("")
    txt.append(f"BDI J-reality d1=d2: max_rel_dev = {r['bdi_max_rel_dev']:.2e}")
    txt.append("")
    txt.append(f"3-tuple: sign={gate['sign_verdict']}  "
               f"mag={gate['magnitude_verdict']}  regime={gate['regime_verdict']}")
    txt.append(f"COMPOSITE = {gate['composite']}")
    ax2.text(0.02, 0.98, "\n".join(txt), va="top", ha="left",
             fontsize=9.0, family="monospace", transform=ax2.transAxes)
    ax2.set_title("S101-NU-DIRAC-OFFDIAG-TEXTURE")

    fig.suptitle("Doublet-split off-diagonal seesaw texture "
                 "(W-2 unit pin discharged)", fontsize=12, y=1.00)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()
    gate = evaluate_gate(r)

    # ---- structured stdout (NUMBERS first) ----
    print("=== STEP A — unit pin (the only new computation) ===")
    print(f"  |w| (npz)            = {r['abs_w']:.10f}")
    print(f"  |w| exact (1/sqrt6)  = {r['abs_w_exact']:.10f}  match={r['w_matches_exact']}")
    print(f"  d blocksum O_g[0]    = {r['O_g'][0]:.6f}   (RATIO-BLOCKSUM, extensive)")
    print(f"  kernel_mean_unit     = {r['kernel_mean_unit']:.6f}")
    print(f"  d_trace_mean         = {r['d_trace_mean']:.6f}   (RATIO-NORM-TRACE-MEAN, intensive)")
    print(f"  x_pinned = |w|/d     = {r['x_pinned']:.10f}")
    print(f"  x_mixed (wrong)      = {r['x_mixed_wrong']:.10f}  (couples intensive/extensive)")
    print(f"  x in window {X_WINDOW}? {r['x_in_window']}")
    print("=== STEP B — seesaw split ===")
    print(f"  lam_heavy = d+|w|    = {r['lam_heavy']:.10f}  (gen3)")
    print(f"  lam_light = d-|w|    = {r['lam_light']:.10f}  (gen2)")
    print(f"  S_pinned             = {r['S_pinned']:.10f}")
    print(f"  S_closed (√6+1)²/5   = {r['S_closed']:.10f}")
    print(f"  S_required           = {S_REQUIRED:.10f}")
    print(f"  x_required           = {r['x_required']:.10f}")
    print(f"  shape_dev            = {r['shape_dev']:+.6f}  ({r['shape_dev']*100:+.4f}%)")
    print(f"  clause1 shape PASS?  = {gate['c1_shape']}  (|dev|<= {SHAPE_TOL})")
    print("=== STEP C — scale (substrate-natural) ===")
    print(f"  Y2_S99               = {r['Y2_S99']:.6f}")
    print(f"  Y3_S99               = {r['Y3_S99']:.6f}")
    print(f"  Y2_texture           = {r['Y2_texture']:.6f}")
    print(f"  scale_dev            = {r['scale_dev']:.6f}")
    print(f"  clause2 scale PASS?  = {gate['c2_scale']}  (|dev|<= {SCALE_TOL})")
    print("=== STEP D — rank-deficiency sub-criterion ===")
    print(f"  M12_inner            = {r['M12_inner']:.2e}")
    print(f"  w_chain_literal_t0   = {r['w_chain_literal_t0']:.2e}")
    print(f"  rank_channel |s|^2   = {r['rank_channel']:.2e}  (<= {RANK_TOL})")
    print(f"  rank(m_D)            = {r['rank_mD']}  (m1=0 => rank-deficient by 1)")
    print(f"  svals                = {[f'{s:.4f}' for s in r['svals']]}")
    print(f"  clause3 rank PASS?   = {gate['c3_rank']}")
    print("=== BDI J-reality witness ===")
    print(f"  bdi_pair_max_rel_dev = {r['bdi_max_rel_dev']:.2e}  (d1=d2 forced by [J,m_D]=0)")
    print(f"  dS/dx                = {r['dS_dx']:.4f}  (>0 => S monotone increasing, heavy=+|w|)")
    print()
    print(f"  3-tuple: sign={gate['sign_verdict']} "
          f"magnitude={gate['magnitude_verdict']} regime={gate['regime_verdict']}")
    print(f"  literal: PASS={gate['literal_PASS']} INFO={gate['literal_INFO']} "
          f"FAIL(window/rank)={gate['literal_FAIL_window_or_rank']}")
    print(f"  COMPOSITE = {gate['composite']}")
    print()

    # ---- save npz ----
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        scheme=SCHEME,
        convention=CONVENTION,
        l_max=L_MAX,
        value=r["S_pinned"],
        verdict=gate["composite"],
        sign_verdict=gate["sign_verdict"],
        magnitude_verdict=gate["magnitude_verdict"],
        regime_verdict=gate["regime_verdict"],
        # Step A
        abs_w=r["abs_w"], abs_w_exact=r["abs_w_exact"], arg_w=np.asarray(r["arg_w"]),
        O_g=np.asarray(r["O_g"]), d_blocksum_ratio=np.asarray(r["d_blocksum_ratio"]),
        kernel_mean_unit=r["kernel_mean_unit"], d_trace_mean=r["d_trace_mean"],
        x_pinned=r["x_pinned"], x_mixed_wrong=r["x_mixed_wrong"], x_in_window=r["x_in_window"],
        # Step B
        lam_heavy=r["lam_heavy"], lam_light=r["lam_light"], S_pinned=r["S_pinned"],
        S_closed=r["S_closed"], S_required=S_REQUIRED, x_required=r["x_required"],
        shape_dev=r["shape_dev"], shape_abs=r["shape_abs"], clause1_shape=gate["c1_shape"],
        # Step C
        Y2_S99=r["Y2_S99"], Y3_S99=r["Y3_S99"], Y2_texture=r["Y2_texture"],
        Y3_texture=r["Y3_texture"], scale_dev=r["scale_dev"], clause2_scale=gate["c2_scale"],
        # Step D
        M12_inner=r["M12_inner"], w_chain_literal_t0=r["w_chain_literal_t0"],
        conj_split=r["conj_split"], rank_channel=r["rank_channel"], clause3_rank=gate["c3_rank"],
        m_D_3x3=np.asarray(r["m_D_3x3"]), svals=np.asarray(r["svals"]),
        rank_mD=r["rank_mD"], n_zero_sv=r["n_zero_sv"], rank_deficient_ok=r["rank_deficient_ok"],
        # BDI / direction
        bdi_max_rel_dev=r["bdi_max_rel_dev"], bdi_O_rel_dev=r["bdi_O_rel_dev"],
        d1_eq_d2_witness=r["d1_eq_d2_witness"], dS_dx=r["dS_dx"], sign_ok=r["sign_ok"],
        # thresholds
        shape_tol=SHAPE_TOL, scale_tol=SCALE_TOL, rank_tol=RANK_TOL,
        x_window=np.asarray(X_WINDOW),
        sha_ok=r["sha_ok"],
        # provenance
        M_KK_pin=M_KK, v_ew_pin=v_ew,
        yukawa_npz_sha=PIN_YUKAWA_SHA, md_npz_sha=PIN_MD_SHA,
        audit_sha256=audit_sha, content_sha256=content_sha,
        schema_version="S84+",
    )
    print(f"  saved npz -> {OUT_NPZ.name}")

    make_plot(r, gate)
    print(f"  saved png -> {OUT_PNG.name}")
    print()

    # ---- 4-tuple + verdict payload ----
    tag = emit_4tuple(r["S_pinned"], SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)

    value_payload = (
        f"S_split={r['S_pinned']:.7f}_xpin={r['x_pinned']:.7f}_"
        f"shapedev={r['shape_dev']*100:+.3f}pct_xreq={r['x_required']:.7f}_"
        f"clauses[shape={int(gate['c1_shape'])},scale={int(gate['c2_scale'])},"
        f"rank={int(gate['c3_rank'])}]_xinwindow={int(r['x_in_window'])}_"
        f"diag=tracemean(kernel_mean_unit=1.0)_offdiag=countingINDEP(1/sqrt6)"
    )  # (local)
    note = (
        "doublet split S=(sqrt6+1)^2/5=2.37980 vs req 2.48825; "
        "shape -4.36% out of +/-1% band; x=0.40825 in window [0.405,0.449] but "
        "below req 0.42665; magnitude FAIL in VALID regime => composite FAIL; "
        "rank-deficiency m1=0 preserved (|s|^2 channel=0); CLASS-2 at exact 1/sqrt6 excluded"
    )  # (local)
    extra = [
        f"# regulator_pin: a_2^{{cutoff}}/a_4^{{cutoff}} structural; "
        f"convention=RATIO-NORMALIZED-TRACE-MEAN (W-2 counting ruling, diag retag)",
    ]  # (local)
    print_verdict_payload(
        gate["composite"], value_payload, audit_sha, content_sha,
        sign_verdict=gate["sign_verdict"],
        magnitude_verdict=gate["magnitude_verdict"],
        regime_verdict=gate["regime_verdict"],
        companion_note=note, extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {gate['composite']} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
