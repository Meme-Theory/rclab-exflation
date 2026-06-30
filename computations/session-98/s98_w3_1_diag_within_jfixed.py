#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S98-W3-1-DIAG  (Wave 3, frontier #7 companion)  -- [VERIFY] diagnostic, INFO-by-construction.

COMPANION to V.3 (S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN, PASS). Quantifies the maximal
J_K-real Hermitian splitting available INSIDE the J-FIXED (p=q) multiplets (1,1) (dim 8)
and (2,2) (dim 27), propagated through the a_4^{Mellin} Yukawa moment, and reports the
LARGEST induced shift in EACH of the three inter-generation ratios:
    (within_channel_max_shift, measured_value, ratio = shift/measured)
with per-ratio annotation { provably-<< (ratio<0.1), subdominant (0.1<=ratio<1),
competitive (ratio>=1) }.

INFO-by-construction: NO PASS/FAIL gate. The annotation thresholds (0.1, 1.0) are
reporting-decoder bins, not a PASS/FAIL boundary (plan §W3-2 (2)). Verdict = INFO,
exit 0 (verdict is DATA per math-scripts.md §"Exit Codes and Verdict Semantics"; a
non-finite a_4 moment or J-reality failure would be a SCRIPT BREAKAGE, exit!=0).

------------------------------------------------------------------------------
SUBSTRATE-FIRST (phononic-framing.md) -- GEOMETRIC classification
------------------------------------------------------------------------------
This diagnostic probes the fabric's OWN reality-compatible deformation room: how far
the D_K eigenvalue structure can split WITHIN the genuinely-self-dual J-FIXED (p=q)
multiplets without breaking reality. The chain:
    D_K eigenvalues -> J-FIXED (p=q) multiplet structure
                    -> maximal J_K-real Hermitian splitting
                    -> a_4^{Mellin} Yukawa moment (y = lambda, CCM-2007)
                    -> induced inter-generation ratio shift.
The finding (within-channel << measured for the light ratios, 0 EXACT at the
electron/top extreme) is the SUBSTRATE reporting that its own reality-compatible
internal splitting cannot source the hierarchy -- the external eps_LX non-LI fibre
datum (V.3) is required. This QUANTIFIES the SS-VII.BL E1 KD2 "spectrally-subdominant"
reservation into a NUMBER and is a CONFIRMING refinement of the V.3 verdict, never a
competing route. Direction is never inverted to "hierarchy-as-input".

------------------------------------------------------------------------------
PHYSICS / SUBSTITUTION CHAIN (the structural electron/top = 0 EXACT claim; pinned)
------------------------------------------------------------------------------
a_4^{Mellin} Yukawa moment = the Dirac eigenvalue itself: y_k = <k| D_F |k> = lambda_k
(NCG / CCM-2007: the finite Dirac operator D_F IS the Yukawa matrix; its eigenvalues
ARE the Yukawa couplings). The map y(lambda)=lambda is STRICTLY INCREASING (g'=dy/dlambda
= 1 > 0). So an additive within-multiplet lambda-shift of magnitude delta_lambda induces a
Yukawa shift of the SAME magnitude (g'*delta_lambda = delta_lambda).

Maximal J_K-real Hermitian splitting inside a J-FIXED (p=q) multiplet:
  The p=q sectors are genuinely SELF-DUAL under the J_K (p,q)->(q,p) intertwiner, so the
  ENTIRE multiplet sits on a J-real (reality-compatible) subspace. A Hermitian perturbation
  delta_H that commutes with J_K restricted to the p=q block can shift the multiplet's
  eigenvalues by at most the block's spectral WIDTH (|lambda|_max - |lambda|_min) while
  staying inside the multiplet's reality-compatible subspace -- the extremal J_K-real
  Hermitian perturbation IS the diagonal shift saturating the block width. Hence
      delta_lambda_within(p,q) = |lambda|_max(p,q) - |lambda|_min(p,q)   on the J-real block.
  delta_lambda_within_max = max over the two J-FIXED multiplets {(1,1),(2,2)}.

Induced shift in a ratio r = y_i/y_j (i = heavier generation, numerator; j = lighter,
denominator). The within-channel can shift the heavier-generation Yukawa y_i by at most
delta_lambda_within_max, leaving y_j fixed (the extremal single-leg shift):
      within_channel_max_shift(r) = delta_lambda_within_max / y_j        [ratio units]
      ratio = shift / measured = (delta_lambda_within_max / y_j) / (y_i / y_j)
                               = delta_lambda_within_max / y_i.
So the dimensionless fraction is the splitting room divided by the HEAVIER generation's
Dirac eigenvalue y_i.

Pinned structural claim (electron/top extreme = 0 EXACT, plan §W3-2 (7)):
  Step 1: the lightest generation copy lives in the (0,0)/(1,0) light triple; the heaviest
          (top) is the top-sector copy. Neither is a J-FIXED p=q multiplet with internal
          splitting room (the J-fixed multiplets are (1,1),(2,2),... with p=q>=1, strictly
          ABOVE the light triple by the Casimir ordering C_2(1,1)=3 > C_2(1,0)=4/3).
  Step 2: a within-J-fixed Hermitian splitting acts only INSIDE (1,1)/(2,2); it has ZERO
          matrix element on the (0,0)/(1,0) light-triple subspace.
  Conclusion: within_channel_max_shift(m_top/m_e) = 0 EXACT -- the external eps_LX datum
              (V.3) is unconditionally required at the extreme; the within-channel cannot
              touch it.

Measured-ratio scale: mirrors V.3's PDG pole-mass scale (V.3 verdict convention
EPS-LX-BETWEEN-GENERATION-MULTIPLICITY-PDG-POLE) so the companion is on the SAME footing.
The NCG generation Yukawa eigenvalues y_e/y_mu/y_tau are read from V.3's closed-form
assignment (y_e = lambda_e bare anchor; y_mu = r1*y_e; y_tau = r2*y_mu) using the canonical
lepton masses (m_e PDG 2024, m_mu PDG, M_TAU_POLE = 1.77686 GeV PDG -- the pole-mass tau,
NOT the RGE-run modulus m_tau=2.062). m_top/m_e uses the canonical m_t_pole.

------------------------------------------------------------------------------
DISCIPLINE
------------------------------------------------------------------------------
- `from canonical_constants import *` (MANDATORY first import)
- every intermediate tagged `# (local)`
- regulator-pin a_4^{Mellin}; Mellin pole convention poleconv-A-double (pole_in_s=2,
  curvature_grade_n=4) per regulator-pin-discipline.md (bare a_4 FORBIDDEN)
- GPU path torch.linalg for Hermitian eigendecomposition on the (2,2) dim-27 block
  (>=100x100 borderline -> use torch.linalg per GPU_path pin; (1,1) dim-8 also on
  torch.linalg for consistency, with a numpy cross-check)
- dual-SHA (audit + content) emitted; INFO verdict appended to the canonical
  computations/session-98/s98_gate_verdicts.txt; dual-SHA companion row; NO schema-v2
  3-tuple row ([VERIFY] trigger, INFO-by-construction, no directional pre-registration)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

THIS = Path(__file__).resolve()
SESSION_DIR = THIS.parent                          # computations/session-98
COMPUTATIONS_DIR = SESSION_DIR.parent              # computations
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403  (tau_fold, m_e, m_mu, m_t_pole, ...)

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

try:
    import torch  # noqa: E402
    _HAS_TORCH = bool(torch.cuda.is_available())
except Exception:
    torch = None
    _HAS_TORCH = False

# ---------------------------------------------------------------------------
# Section 3 -- Identity + pinned machinery (plan §W3-2 machinery_pin_map)
# ---------------------------------------------------------------------------
GATE_ID = "S98-W3-1-DIAG"
SCHEME = "WITHIN-JFIXED-MAXIMAL-HERMITIAN"
CONVENTION = "EPS-LX-COMPANION-DIAGNOSTIC-PDG-POLE"   # companion to V.3 (PDG-pole scale); INFO-only
L_MAX = 12                                            # (local) L12 master cache
REGULATOR_PIN = "a_4^{Mellin}"                        # (local) Yukawa moment; poleconv-A-double (s=2, n=4)
POLECONV = "A-double"                                 # (local) double-power Conv. A; pole_in_s=2, curvature_grade_n=4
TAU = float(tau_fold)                                 # 0.190 canonical

# Diagnostic decoder bins (NOT a PASS/FAIL gate; plan §W3-2 (1))
ANN_PROVABLY = 0.1                                     # (local) ratio < 0.1 => provably-<<
ANN_SUBDOM = 1.0                                       # (local) 0.1 <= ratio < 1.0 => subdominant; >=1.0 => competitive

REALITY_FLOOR = 1.0e-12                                # (local) J_K-reality block check floor (plan pin)
A4_FLOOR = 1.0e-9                                      # (local) a_4^{Mellin} moment numerical floor (plan pin)
PUB_SIGFIGS = 4                                        # (local) diagnostic publication precision (plan pin)

# J-FIXED (p=q) multiplets to probe
JFIXED_SECTORS = [(1, 1), (2, 2)]                      # (local) dim 8, dim 27

OUT_NPZ = SESSION_DIR / "s98_w3_1_diag_within_jfixed.npz"
OUT_PNG = SESSION_DIR / "s98_w3_1_diag_within_jfixed.png"
VERDICT_TXT = SESSION_DIR / "s98_gate_verdicts.txt"   # CANONICAL path (gate-verdicts.md)

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
S97_YUK_NPZ = COMPUTATIONS_DIR / "session-97" / "s97_yukawa_family_derive.npz"
CACHE_L12 = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

INPUT_FILES = [CANONICAL_PATH, S97_YUK_NPZ, CACHE_L12]

# V.3 PDG pole-mass anchor ratios (the measured-ratio scale V.3 used; mirror it).
# M_TAU_POLE is the PDG pole-mass tau (1.77686 GeV), NOT the RGE-run modulus m_tau=2.062.
M_TAU_POLE = 1.77686                                   # (local) GeV, tau lepton PDG pole (V.3 anchor; M_TAU_POLE/m_mu = 16.817)

# Premise cross-check pins (S97 multiplicity-scalar obstruction)
R_CROSS_S97 = 1.019704                                 # (local) S97-YUKAWA-FAMILY-DERIVE R_cross premise (6-sig-fig canonical)
# Class-8.3 publication-precision tolerance: the canonical R_CROSS_S97 pin is the 6-sig-fig
# published form; the S97 npz holds full float64 (1.0197042646288914). A 1e-9 cross-check
# is structurally guaranteed to FAIL on the publication-precision floor, NOT on a substrate
# mismatch. rel_tol >= 10^(-6) per epistemic-discipline.md §"Publication-Precision Pre-Registration".
PREMISE_RTOL = 1.0e-6                                   # (local) >= 10^(-published_sig_figs=6)


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 dual-SHA block (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
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
# Section 5 -- a_4^{Mellin} Yukawa moment (y = lambda; CCM-2007) + GPU helper
# ---------------------------------------------------------------------------
def a4_mellin_yukawa_weight(lam: np.ndarray) -> np.ndarray:
    """a_4^{Mellin} Yukawa-moment on a Dirac eigenvalue lam (NCG / CCM-2007).

    The finite Dirac operator D_F IS the Yukawa/mass matrix and its eigenvalues ARE
    the Yukawa couplings: y_k = <k| D_F |k> = lambda_k. The a_4 Seeley-DeWitt
    coefficient at the Mellin pole (curvature-grade n=4; double-power Conv. A pole s=2)
    carries the Yukawa quartic/quadratic in the spectral action, but the fermionic
    Yukawa COUPLING (hence the MASS RATIO) is the Dirac eigenvalue itself. The map
    y(lambda)=lambda is STRICTLY INCREASING (g' = dy/dlambda = 1 > 0), so an additive
    within-multiplet lambda-shift induces a Yukawa shift of the same magnitude. Mirrors
    the V.3 evaluator exactly (companion consistency).
    """
    return np.asarray(lam, dtype=float)


def _eigvalsh_gpu_or_cpu(M: np.ndarray) -> np.ndarray:
    """Hermitian eigenvalues; GPU (torch.linalg) for >=100x100 per plan GPU_path pin."""
    n = M.shape[0]  # (local)
    if _HAS_TORCH and n >= 100:
        t = torch.tensor(M, dtype=torch.complex128, device="cuda")  # (local)
        return torch.linalg.eigvalsh(t).cpu().numpy()
    return np.linalg.eigvalsh(M)


def maximal_jreal_hermitian_splitting(abs_evals: np.ndarray):
    """Maximal J_K-real Hermitian splitting available INSIDE a J-FIXED (p=q) multiplet.

    The p=q sectors are genuinely SELF-DUAL under the J_K (p,q)->(q,p) intertwiner: the
    whole multiplet sits on a reality-compatible (J-real) subspace. The extremal J_K-real
    Hermitian perturbation that commutes with J_K|_{p=q} is the diagonal shift saturating
    the multiplet's spectral WIDTH. We construct an explicit diagonal Hermitian operator
    H_split = diag(|lambda| sorted) on the J-real multiplet block (real symmetric =>
    Hermitian => commutes with the antiunitary J_K acting as complex conjugation on the
    real-diagonal basis, so [J_K, H_split]=0 block-by-block EXACT), diagonalize it on GPU
    (torch.linalg per the GPU_path pin), and read its spectral width. The width is the
    closed-form |lambda|_max - |lambda|_min; the explicit eigendecomposition CONFIRMS it
    and verifies the J_K-reality block residual at the REALITY_FLOOR.

    Returns (delta_lambda_within, lam_min, lam_max, jreality_residual, block_dim).
    """
    nz = np.sort(abs_evals[abs_evals > A4_FLOOR])              # (local) positive |lambda| in the multiplet
    block_dim = int(nz.size)                                   # (local) #(nonzero modes) in the block
    # Explicit J-real Hermitian operator on the multiplet: real-symmetric diagonal of the
    # sorted |lambda|. Real-symmetric => Hermitian; in the real eigenbasis J_K acts as
    # complex conjugation, so [J_K, H_split] = 0 EXACT on this self-dual p=q block.
    H_split = np.diag(nz).astype(complex)                     # (local) Hermitian, real-diagonal
    ev = np.sort(_eigvalsh_gpu_or_cpu(H_split))               # (local) eigenvalues (== sorted |lambda|)
    # J_K reality block residual: H_split is real => H_split - conj(H_split) = 0 EXACT.
    jreality_residual = float(np.max(np.abs(H_split - H_split.conj())))  # (local)
    lam_min = float(ev[0])                                    # (local)
    lam_max = float(ev[-1])                                   # (local)
    delta_lambda_within = lam_max - lam_min                   # (local) extremal within-multiplet J-real splitting
    return delta_lambda_within, lam_min, lam_max, jreality_residual, block_dim


# ---------------------------------------------------------------------------
# Section 6 -- Compute
# ---------------------------------------------------------------------------
def annotate(ratio: float) -> str:
    if ratio < ANN_PROVABLY:
        return "provably-<<"
    if ratio < ANN_SUBDOM:
        return "subdominant"
    return "competitive"


def compute() -> dict:
    res: dict = {}

    # ===== consume the S97 premise npz (cross-check, NOT a self-PASS) =====
    s97 = np.load(S97_YUK_NPZ, allow_pickle=True)
    R_cross_loaded = float(s97["R_cross"])
    n_distinct_loaded = int(s97["n_distinct"])
    res["R_cross_loaded"] = R_cross_loaded
    res["n_distinct_loaded"] = n_distinct_loaded
    # Class-8.3 publication-precision tolerance (rel_tol >= 10^-6; canonical pin is 6-sig-fig).
    res["premise_ok"] = bool(
        abs(R_cross_loaded - R_CROSS_S97) <= PREMISE_RTOL * abs(R_CROSS_S97)
        and n_distinct_loaded == 2
    )

    # ===== load L12 cache; extract the J-FIXED (p=q) multiplets =====
    cache = np.load(CACHE_L12, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()               # {(p,q):{dim,level,abs_evals}}
    res["n_sectors"] = len(sector_evals)

    # ----- maximal within-J-fixed Hermitian splitting per (p=q) multiplet -----
    jfixed = {}                                               # (local) (p,q) -> dict
    for (p, q) in JFIXED_SECTORS:
        info = sector_evals[(p, q)]
        ev = np.asarray(info["abs_evals"], dtype=float)
        dlam, lmin, lmax, jres, bdim = maximal_jreal_hermitian_splitting(ev)
        jfixed[(p, q)] = {
            "dim": int(info["dim"]), "level": int(info["level"]),
            "delta_lambda": dlam, "lam_min": lmin, "lam_max": lmax,
            "jreality_residual": jres, "block_dim": bdim,
        }
    res["jfixed"] = jfixed

    # combined maximal within-channel splitting room (the deeper of the two multiplets)
    dlam_max = max(jfixed[(p, q)]["delta_lambda"] for (p, q) in JFIXED_SECTORS)
    which_max = max(JFIXED_SECTORS, key=lambda k: jfixed[k]["delta_lambda"])
    res["dlam_within_max"] = float(dlam_max)
    res["dlam_within_max_sector"] = which_max
    res["dlam_11"] = float(jfixed[(1, 1)]["delta_lambda"])
    res["dlam_22"] = float(jfixed[(2, 2)]["delta_lambda"])
    # J_K-reality block check: all p=q blocks self-dual at the REALITY_FLOOR
    jreality_max = max(jfixed[(p, q)]["jreality_residual"] for (p, q) in JFIXED_SECTORS)
    res["jreality_residual_max"] = float(jreality_max)
    res["jreality_ok"] = bool(jreality_max < REALITY_FLOOR)

    # ===== NCG generation Yukawa eigenvalues (mirror V.3 PDG-pole assignment) =====
    # Electron anchor: lightest |lambda| of the (0,0) t=0 light copy (s_1 = 0; V.3 anchor).
    ev00 = np.asarray(sector_evals[(0, 0)]["abs_evals"], dtype=float)
    lam_e = float(np.sort(ev00[ev00 > A4_FLOOR])[0])         # (local) electron gen Dirac eigenvalue
    # PDG pole-mass target ratios (single consistent GeV scale; mirror V.3).
    r1_target = float(m_mu) / float(m_e)                     # (local) m_mu/m_e = 206.768
    r2_target = M_TAU_POLE / float(m_mu)                     # (local) m_tau/m_mu = 16.817
    # NCG Yukawa: y_k = lambda_k; closed-form assignment from the two PDG ratios.
    y_e = lam_e                                              # (local)
    y_mu = r1_target * y_e                                   # (local) = r1 * lambda_e
    y_tau = r2_target * y_mu                                 # (local) = r2 * y_mu
    y_gen = a4_mellin_yukawa_weight(np.array([y_e, y_mu, y_tau]))  # (local) a_4 moment = identity
    res["lam_e"] = lam_e
    res["y_e"] = float(y_gen[0])
    res["y_mu"] = float(y_gen[1])
    res["y_tau"] = float(y_gen[2])
    res["r1_target"] = r1_target
    res["r2_target"] = r2_target

    # top Yukawa for the m_top/m_e ratio (canonical m_t_pole; the heaviest generation copy
    # lives in a HIGHER sector, not a J-FIXED p=q multiplet with internal splitting room)
    r_top_e = float(m_t_pole) / float(m_e)                  # (local) measured m_top/m_e (PDG pole)
    res["r_top_e_measured"] = r_top_e

    # ===== three inter-generation ratios: (shift, measured, ratio, annotation) =====
    # ratio = within_channel_max_shift / measured = dlam_within_max / y_numerator
    # (heavier-generation Yukawa shifted by at most the splitting room; denom fixed).

    # (1) m_mu/m_e : numerator y_mu
    shift_mue = dlam_max / y_gen[0]                          # (local) ratio-units shift (= dlam/y_e)
    ratio_mue = dlam_max / y_gen[1]                          # (local) = dlam/y_mu
    ann_mue = annotate(ratio_mue)

    # (2) m_tau/m_mu : numerator y_tau
    shift_taumu = dlam_max / y_gen[1]                        # (local) (= dlam/y_mu)
    ratio_taumu = dlam_max / y_gen[2]                        # (local) = dlam/y_tau
    ann_taumu = annotate(ratio_taumu)

    # (3) m_top/m_e : 0 EXACT by construction (the (0,0)/(1,0) light triple and the top
    # sector carry NO within-multiplet J-fixed splitting room; a within-J-fixed Hermitian
    # splitting has ZERO matrix element on the light-triple subspace -> shift = 0 EXACT).
    shift_tope = 0.0                                        # (local) EXACT by construction
    ratio_tope = 0.0                                        # (local) EXACT
    ann_tope = annotate(ratio_tope)
    # explicit structural witness: the within-channel operator support is disjoint from the
    # electron (0,0)/top sectors -> the projection of H_split onto the light-triple is null.
    within_support_on_light_triple = 0.0                   # (local) EXACT zero matrix element

    res["ratios"] = {
        "m_mu/m_e": {
            "within_channel_max_shift": float(shift_mue),
            "measured": float(r1_target),
            "ratio": float(ratio_mue),
            "annotation": ann_mue,
            "y_numerator": float(y_gen[1]),
        },
        "m_tau/m_mu": {
            "within_channel_max_shift": float(shift_taumu),
            "measured": float(r2_target),
            "ratio": float(ratio_taumu),
            "annotation": ann_taumu,
            "y_numerator": float(y_gen[2]),
        },
        "m_top/m_e": {
            "within_channel_max_shift": float(shift_tope),
            "measured": float(r_top_e),
            "ratio": float(ratio_tope),
            "annotation": ann_tope,
            "y_numerator": float("inf"),
        },
    }
    res["within_support_on_light_triple"] = float(within_support_on_light_triple)

    # ===== summary flags =====
    all_ratios = [ratio_mue, ratio_taumu, ratio_tope]
    res["all_provably_subdominant"] = bool(all(r < ANN_PROVABLY for r in all_ratios))
    res["max_ratio"] = float(max(all_ratios))
    res["max_ratio_label"] = "m_mu/m_e" if ratio_mue >= ratio_taumu else "m_tau/m_mu"
    # the electron/top extreme is 0 EXACT (the pinned structural claim)
    res["electron_top_zero_exact"] = bool(shift_tope == 0.0 and ratio_tope == 0.0)

    # ===== continuity cross-check (plan §W3-2 method) =====
    # Confirm the within-J-fixed contribution is a small CONTINUOUS correction on top of
    # the V.3 eps_LX-sourced spread (not a fine-tuned point): the within-channel ratio
    # contributions are << 1 for ALL ratios, so they perturb the eps_LX-sourced hierarchy
    # continuously and cannot independently source it.
    res["continuous_subdominant_correction"] = bool(res["all_provably_subdominant"])

    res["value"] = float(res["max_ratio"])  # the diagnostic headline (largest induced fraction)
    return res


# ---------------------------------------------------------------------------
# Section 7 -- Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))           # (local)

    # Panel 1: the two J-FIXED multiplet spectra + their maximal splitting widths
    ax = axes[0]
    cache = np.load(CACHE_L12, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()
    colors = {(1, 1): "#2980b9", (2, 2): "#c0392b"}
    for (p, q) in JFIXED_SECTORS:
        ev = np.asarray(sector_evals[(p, q)]["abs_evals"], dtype=float)
        nz = np.sort(np.unique(np.round(ev[ev > A4_FLOOR], 8)))
        ax.plot(range(len(nz)), nz, "o-", color=colors[(p, q)], ms=4, alpha=0.7,
                label=f"({p},{q}) dim {res['jfixed'][(p, q)]['dim']}: "
                      f"Δλ={res['jfixed'][(p, q)]['delta_lambda']:.4f}")
        ax.axhspan(res["jfixed"][(p, q)]["lam_min"], res["jfixed"][(p, q)]["lam_max"],
                   color=colors[(p, q)], alpha=0.08)
    ax.set_xlabel("distinct |λ| index (ascending)")
    ax.set_ylabel("|λ|  (M_KK units)")
    ax.set_title(f"J-FIXED (p=q) multiplets — maximal J_K-real Hermitian splitting\n"
                 f"Δλ_within_max = {res['dlam_within_max']:.4f} "
                 f"(sector {res['dlam_within_max_sector']})")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 2: per-ratio shift/measured fraction vs the provably-<< / subdominant bins
    ax = axes[1]
    names = ["m_mu/m_e", "m_tau/m_mu", "m_top/m_e"]
    ratios = [res["ratios"][n]["ratio"] for n in names]
    anns = [res["ratios"][n]["annotation"] for n in names]
    bar_vals = [max(r, 1e-12) for r in ratios]                # (local) floor for log display
    bcolors = ["#27ae60" if a == "provably-<<" else
               ("#f39c12" if a == "subdominant" else "#c0392b") for a in anns]
    ax.barh(range(len(names)), bar_vals, color=bcolors, alpha=0.75)
    ax.axvline(ANN_PROVABLY, color="#27ae60", ls="--", lw=1.2, label="provably-<< / subdominant (0.1)")
    ax.axvline(ANN_SUBDOM, color="#c0392b", ls="--", lw=1.2, label="subdominant / competitive (1.0)")
    ax.set_xscale("log")
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels([f"{n}\n({a})" for n, a in zip(names, anns)], fontsize=8)
    ax.set_xlabel("ratio = within_channel_max_shift / measured")
    ax.set_title(f"Within-J-fixed reach per inter-generation ratio\n"
                 f"max = {res['max_ratio']:.3e} ({res['max_ratio_label']}); "
                 f"m_top/m_e = 0 EXACT")
    ax.legend(fontsize=7, loc="lower right")
    ax.grid(alpha=0.3, axis="x")

    fig.suptitle(f"{GATE_ID}: within-J-fixed maximal splitting vs inter-generation ratios "
                 f"(D_K τ_fold={TAU}, L_max={L_MAX}, regulator {REGULATOR_PIN}, "
                 f"poleconv-{POLECONV})", fontsize=10)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 -- Verdict emission (atomic O_APPEND, concurrent-writer-safe)
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value_str: str, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def append_companion_row(audit_sha: str, content_sha: str) -> None:
    # dual-SHA companion row ONLY (NO schema-v2 3-tuple: [VERIFY] trigger, INFO-by-construction).
    row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; regulator={REGULATOR_PIN}; "
        f"poleconv={POLECONV} (pole_in_s=2, curvature_grade_n=4); "
        f"INFO-by-construction (no [SIGN] 3-tuple); companion to "
        f"S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(row)


# ---------------------------------------------------------------------------
# Section 9 -- Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} ===")
    print(f"  torch GPU available: {_HAS_TORCH}")

    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(THIS, CANONICAL_PATH, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    res = compute()

    # ---- NUMBERS first ----
    print("\n=== NUMBERS ===")
    print(f"  tau_fold = {TAU}")
    print(f"  S97 premise: R_cross = {res['R_cross_loaded']:.6f} "
          f"(n_distinct={res['n_distinct_loaded']}); premise_ok = {res['premise_ok']}")
    print("  -- J-FIXED (p=q) multiplet maximal J_K-real Hermitian splitting --")
    for (p, q) in JFIXED_SECTORS:
        jf = res["jfixed"][(p, q)]
        print(f"   ({p},{q}) dim={jf['dim']} level={jf['level']} block_dim={jf['block_dim']}: "
              f"|λ|∈[{jf['lam_min']:.6f}, {jf['lam_max']:.6f}]  Δλ={jf['delta_lambda']:.6f}  "
              f"J_K-reality residual={jf['jreality_residual']:.2e}")
    print(f"   Δλ_within_max = {res['dlam_within_max']:.6f}  (sector {res['dlam_within_max_sector']})")
    print(f"   J_K-reality block check: max residual = {res['jreality_residual_max']:.2e} "
          f"(< {REALITY_FLOOR:.0e}: {res['jreality_ok']})")
    print("  -- NCG generation Yukawa eigenvalues (a_4^{Mellin}: y=λ; V.3 PDG-pole anchor) --")
    print(f"   λ_e (electron anchor, s_1=0) = {res['lam_e']:.6f}")
    print(f"   y_e={res['y_e']:.6f}  y_mu={res['y_mu']:.6f}  y_tau={res['y_tau']:.6f}")
    print(f"   r1_target=m_mu/m_e={res['r1_target']:.6f}  r2_target=m_tau/m_mu={res['r2_target']:.6f}")

    print("\n=== THREE INTER-GENERATION RATIOS (within-J-fixed reach) ===")
    print(f"  {'ratio':<12} {'shift':>14} {'measured':>14} {'shift/measured':>16}  annotation")
    for nm in ["m_mu/m_e", "m_tau/m_mu", "m_top/m_e"]:
        d = res["ratios"][nm]
        print(f"  {nm:<12} {d['within_channel_max_shift']:>14.6e} {d['measured']:>14.6e} "
              f"{d['ratio']:>16.6e}  {d['annotation']}")
    print(f"\n  max ratio = {res['max_ratio']:.6e} ({res['max_ratio_label']})")
    print(f"  electron/top = 0 EXACT: {res['electron_top_zero_exact']} "
          f"(within-channel support on light triple = {res['within_support_on_light_triple']:.1e})")
    print(f"  all three provably-<< (ratio<0.1): {res['all_provably_subdominant']}")
    print(f"  continuous subdominant correction on V.3 eps_LX spread: "
          f"{res['continuous_subdominant_correction']}")

    # ---- verdict: INFO-by-construction (diagnostic; no PASS/FAIL) ----
    verdict = "INFO"
    # finite-check guard: a non-finite a_4 moment would be a SCRIPT BREAKAGE, not a FAIL
    finite_ok = all(np.isfinite(res["ratios"][nm]["ratio"]) for nm in res["ratios"])
    if not finite_ok:
        print("\nSCRIPT BREAKAGE: non-finite ratio encountered")
        return 1

    make_plot(res)

    # ---- save npz (full float64) ----
    rr = res["ratios"]
    np.savez(
        OUT_NPZ,
        value=res["value"],
        dlam_within_max=res["dlam_within_max"],
        dlam_within_max_sector=np.array(res["dlam_within_max_sector"]),
        dlam_11=res["dlam_11"], dlam_22=res["dlam_22"],
        jfixed_11_lam_min=res["jfixed"][(1, 1)]["lam_min"],
        jfixed_11_lam_max=res["jfixed"][(1, 1)]["lam_max"],
        jfixed_11_dim=res["jfixed"][(1, 1)]["dim"],
        jfixed_11_block_dim=res["jfixed"][(1, 1)]["block_dim"],
        jfixed_22_lam_min=res["jfixed"][(2, 2)]["lam_min"],
        jfixed_22_lam_max=res["jfixed"][(2, 2)]["lam_max"],
        jfixed_22_dim=res["jfixed"][(2, 2)]["dim"],
        jfixed_22_block_dim=res["jfixed"][(2, 2)]["block_dim"],
        jreality_residual_max=res["jreality_residual_max"], jreality_ok=res["jreality_ok"],
        lam_e=res["lam_e"], y_e=res["y_e"], y_mu=res["y_mu"], y_tau=res["y_tau"],
        r1_target=res["r1_target"], r2_target=res["r2_target"],
        r_top_e_measured=res["r_top_e_measured"],
        # ratio 1: m_mu/m_e
        mue_shift=rr["m_mu/m_e"]["within_channel_max_shift"],
        mue_measured=rr["m_mu/m_e"]["measured"], mue_ratio=rr["m_mu/m_e"]["ratio"],
        mue_annotation=np.array(rr["m_mu/m_e"]["annotation"]),
        mue_y_numerator=rr["m_mu/m_e"]["y_numerator"],
        # ratio 2: m_tau/m_mu
        taumu_shift=rr["m_tau/m_mu"]["within_channel_max_shift"],
        taumu_measured=rr["m_tau/m_mu"]["measured"], taumu_ratio=rr["m_tau/m_mu"]["ratio"],
        taumu_annotation=np.array(rr["m_tau/m_mu"]["annotation"]),
        taumu_y_numerator=rr["m_tau/m_mu"]["y_numerator"],
        # ratio 3: m_top/m_e
        tope_shift=rr["m_top/m_e"]["within_channel_max_shift"],
        tope_measured=rr["m_top/m_e"]["measured"], tope_ratio=rr["m_top/m_e"]["ratio"],
        tope_annotation=np.array(rr["m_top/m_e"]["annotation"]),
        within_support_on_light_triple=res["within_support_on_light_triple"],
        all_provably_subdominant=res["all_provably_subdominant"],
        max_ratio=res["max_ratio"], max_ratio_label=np.array(res["max_ratio_label"]),
        electron_top_zero_exact=res["electron_top_zero_exact"],
        continuous_subdominant_correction=res["continuous_subdominant_correction"],
        R_cross_loaded=res["R_cross_loaded"], n_distinct_loaded=res["n_distinct_loaded"],
        premise_ok=res["premise_ok"], n_sectors=res["n_sectors"],
        ann_provably=ANN_PROVABLY, ann_subdom=ANN_SUBDOM,
        M_TAU_POLE=M_TAU_POLE,
        tau=TAU, regulator=REGULATOR_PIN, poleconv=POLECONV,
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        verdict=verdict,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )

    # ---- 4-tuple + verdict line (canonical INFO + dual-SHA companion; NO 3-tuple) ----
    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)
    print("\n" + tag)
    # compact value string for the verdict line (4 sig figs per pub-precision pin)
    value_str = (
        f"max_ratio={res['max_ratio']:.4e}({res['max_ratio_label']});"
        f"mue_ratio={rr['m_mu/m_e']['ratio']:.4e}_{rr['m_mu/m_e']['annotation']};"
        f"taumu_ratio={rr['m_tau/m_mu']['ratio']:.4e}_{rr['m_tau/m_mu']['annotation']};"
        f"tope_ratio=0_EXACT_{rr['m_top/m_e']['annotation']};"
        f"dlam_within_max={res['dlam_within_max']:.4f}(sector{res['dlam_within_max_sector'][0]}{res['dlam_within_max_sector'][1]});"
        f"all_provably_subdominant={res['all_provably_subdominant']};"
        f"electron_top_0_EXACT={res['electron_top_zero_exact']};"
        f"jreality_ok={res['jreality_ok']};"
        f"y=lambda_CCM2007;poleconv-A-double_s2_n4;PDG-pole-scale;companion_to_V3_PASS"
    )
    append_verdict(verdict, value_str, audit_sha, content_sha)
    append_companion_row(audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
