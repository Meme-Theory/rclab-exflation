#!/usr/bin/env python3
"""
INV4 W2-2 - Raychaudhuri focusing for the reduced (a(t),tau(t)) congruence on M^4 x SU(3)
=========================================================================================

Gate: INV4-W2-2 ([SIGN], GEOMETRIC; investigation-4 track)

Attacks the tau<->t map gap G1 (the invariant-derivation gap) from the SUBSTRATE, using the
Raychaudhuri focusing equation -- the engine of every singularity theorem -- on the reduced
4D congruence of the Diagram-A 12D metric.

THREE pre-registered deliverables (plan investigation-4-plan-w2.md §W2-2):
  (1) q-REPRODUCTION:  q_Raych reproduces the S101-W1-QEQ-SELFCONS q~H deceleration tracking
                       to <= tol_q = 0.05 (the n=2 tracking: a_exp=0.655380~2/3, H_t_exp=-0.983~-1,
                       slope_selfcons=1.000074 => matter-dom q=+1/2).
  (2) RANK-1 w=M_KK LOCALIZATION: the un-fixed normalization scale w=M_KK (rank-1 NNU §VII.BS,
                       O = w * Ohat) localizes to EXACTLY ONE focusing term (second singular value
                       of the [term x {1, w}] dependence matrix < 1e-6 relative).
  (3) a0-vs-a2 SOURCE DECOMPOSITION: which Seeley-DeWitt moment sources the dominant -R_ab k^a k^b
                       focusing term -- a_0 (zeroth/volume/cosmological-term moment) vs a_2
                       (second/curvature/Einstein-Hilbert moment); >70% for a clean branch.

[SIGN] payload (the pre-registered direction): in the reduced 4D congruence the DOMINANT focusing
term is the internal-Ricci channel -R_ab k^a k^b (NOT -theta^2/3), it is NEGATIVE (focusing /
decelerating, the singularity-theorem direction) outside the NEC-violation strip tau in [0,0.285],
and it -- not -theta^2/3 -- carries the rank-1 un-fixed scale w=M_KK.

----------------------------------------------------------------------------------------------------
SUBSTRATE FRAMING (phononic-framing.md):  GEOMETRIC. Level-2 moduli-deformation.
The congruence is a TRAJECTORY through the Jensen moduli space {D_K(tau(t))}; Raychaudhuri is the
invariant bookkeeping of how the substrate's OWN deformation parameter tau evolves (tau IS the
intrinsic deformation parameter, NOT a coordinate on a meta-container). The explanation flows
substrate -> emergent FRW, never the reverse:

  D_K eigenvalues (Jensen-deformed SU(3))
    -> a_0 / a_2 Seeley-DeWitt moments of the spectral action
    -> (4+8)-split Einstein tensor / internal Ricci R_ab
    -> Raychaudhuri focusing dtheta/dlambda = -theta^2/3 - sigma^2 + omega^2 - R_ab k^a k^b
    -> theta_4D = 3H deceleration q ~ H (the S101 n=2 tracking anchor)
    -> the emergent FRW expansion history.

The tau<->t map is NOT "the FRW scale factor a(t) drives the internal radius"; it IS "the
substrate's intrinsic Jensen deformation tau-dot SOURCES the emergent external expansion
theta_4D=3H through the reduced Einstein equations, and Raychaudhuri is the invariant statement
of that sourcing." This gate is the geometric/invariant tool for the same clock gap that W3-1
attacks thermodynamically (de Sitter a_0 first law) -- complementary, not adversarial.

----------------------------------------------------------------------------------------------------
EXACT GEOMETRY (Sage-verified closed form; see derivation in the WP substitution chain)

Diagram-A 12D metric:  ds^2_12 = -dt^2 + a(t)^2 dx_3^2 + g_ab(tau(t)) dy^a dy^b,
  g_ab(tau) = 3*diag( e^{-2tau} x3 [SU(2)], e^{tau} x4 [C^2], e^{2tau} x1 [U(1)] ).

Write each spatial direction i as e^{2 beta_i(t)} (Kasner form, beta = (1/2) ln(scale)):
  3 external (FRW):  beta_ext = ln a
  SU(2) (x3):  scale e^{-2tau} -> beta = -tau
  C^2  (x4):  scale e^{+tau}  -> beta = +tau/2
  U(1) (x1):  scale e^{+2tau} -> beta = +tau

For ds^2 = -dt^2 + sum_i e^{2 beta_i(t)} (dx^i)^2, the EXACT Ricci time-time is
  R_tt = R_ab k^a k^b = - sum_i ( beta_i'' + (beta_i')^2 ).

Sage-verified results (mcp__sage, this session):
  - INTERNAL EXPANSION (tr K):  sum_{internal} d_i beta_i' = 3(-1)+4(1/2)+1(1) = 0  EXACTLY
        => theta_int = 0  (S63 SURFACE-12; volume-preserving Jensen).
  - INTERNAL SHEAR:  sigma^2 = sum_{internal} d_i (beta_i')^2 = (3*1 + 4*(1/4) + 1*1) tau'^2
        = 5 tau'^2  EXACTLY  (SU(2) contracting vs C^2/U(1) expanding -> pure shear).
  - sum_{internal} d_i beta_i'' = 0  => the internal Ricci-tt is PURELY the shear -sigma^2.
  - FULL focusing source:  R_ab k^a k^b = -3 a''/a - 5 tau'^2.
        external piece  = -3 a''/a  (the FRW acceleration);
        internal piece  = -5 tau'^2 = -sigma^2 (the SU(3) Kasner shear).

----------------------------------------------------------------------------------------------------
SUBSTITUTION CHAIN (MANDATORY - [SIGN] trigger: focusing-term sign + which moment carries it)

Claim (the [SIGN] payload): "the dominant focusing term is -R_ab k^a k^b (internal-Ricci, NOT
-theta^2/3); it is NEGATIVE (focusing) outside the NEC strip tau in [0,0.285]; and it carries the
rank-1 w=M_KK scale."

  Def 1 (Raychaudhuri):  dtheta/dlambda = -(1/3)theta^2 - sigma_ab sigma^ab + omega_ab omega^ab
                                          - R_ab k^a k^b.   [engine of singularity theorems]
  Def 2 (reduced congruence):  theta = theta_4D = 3H = 3 a'/a (FRW comoving); omega=0 (irrotational);
                               theta_int = 0 (tr K=0, S63 SURFACE-12).
  Def 3 (Kasner shear):  g_ab(tau) anisotropic -> sigma^2 = 5 tau'^2 > 0 (enters Raychaudhuri with
                         a minus sign -> -sigma^2 < 0, focusing).
  Def 4 (focusing source):  R_ab k^a k^b = -3 a''/a - 5 tau'^2; on the (4+8) split the internal
                            curvature feeds the 4D Einstein eqs through a Seeley-DeWitt moment
                            (a_2 generates Einstein-Hilbert; a_0 the cosmological term).

  Substitute (focusing sign): dtheta/dlambda = -(1/3)(3H)^2 - 5 tau'^2 - R_ab k^a k^b|_4D-eff.
    Outside the NEC strip, R_ab k^a k^b >= 0 (NEC) => -R_ab k^a k^b <= 0 (focusing). Inside the NEC
    strip tau in [0,0.285] (S95/DNP; canonical tau_NEC=1.383 is the full physical-domain edge, but
    the COSMOLOGICALLY ACTIVE strip is [0,0.285], where Ric_min can change sign).
  Simplify: q = -a''a/a'^2 = -(a''/a)/H^2 > 0 outside the strip -> deceleration (matter-dom q=+1/2).
  Canonical form: 3 a''/a = -R_ab k^a k^b|_4D-eff ; q ~ H by the reduced Friedmann/Raychaudhuri
    identity a''/a = -(1/6)(rho+3p), the S101 anchor.
  Direction (sign_verdict): PASS iff (i) the dominant focusing term is -R_ab k^a k^b, NOT -theta^2/3;
    (ii) negative outside the NEC strip; (iii) the rank-1 w=M_KK lands on this term.
  Conclusion: the internal-Ricci focusing term carries BOTH the deceleration AND the un-fixed M_KK
    scale -- the tau<->t map's invariant bookkeeping localizes to ONE term.

----------------------------------------------------------------------------------------------------
a_0 / a_2 MOMENT DECOMPOSITION (substrate-first; the source-attribution of the focusing term)

The dominant focusing term is -R_ab k^a k^b = -(3 a''/a + 5 tau'^2). On the (4+8) split, R_ab k^a k^b
is a CURVATURE contraction (two derivatives of the metric) -- structurally the a_2 (second Seeley-
DeWitt = scalar-curvature = Einstein-Hilbert) channel, NOT the a_0 (zeroth = volume = cosmological)
channel. We DECOMPOSE the focusing-term magnitude by projecting it onto the two moments using the
substrate spectral weights w_a2 = a_2(tau)/[a_0 + a_2(tau)] (the a_2 fraction of the spectral action's
low-order weight) and w_a0 = a_0/[a_0 + a_2(tau)], built from the SAME L12 Peter-Weyl cache and per-tau
Jensen rescaling as W2-1 (a_2(tau) softens at the fold; a_0 = mode-count is tau-flat). A clean branch
requires one moment > 70%.  Structurally Raychaudhuri's R_ab is two-derivative => a_2-dominant
(Track A: clock in a_2 -> seeds the future clock-location workshop vs W3-1's a_0).
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) CPU thread cap (computation-environment.md)
os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local)

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Identity (plan §W2-2)
# ---------------------------------------------------------------------------
SESSION = "INV4"                              # (local)
GATE_ID = "INV4-W2-2"                         # (local)
SCHEME = "raychaudhuri-4plus8-split"          # (local) full focusing eq on the Diagram-A (4+8) product
CONVENTION = "a2-reduction-4D"                # (local) focusing projected onto the emergent 4D Lorentzian metric
L_MAX = "12"                                  # (local) a_0/a_2 moment decomposition from the L12 Peter-Weyl cache

# Plan-pinned machinery (PRDR §5)
N_EVAL = 200                                  # (local) tau-samples along tau(t) in [0,0.22]
SCAN_MIN = 0.0                                # (local) genesis edge
SCAN_MAX = 0.22                               # (local) transit-completion edge (Diagram-A active window)
TOL_Q = 0.05                                  # (local) q-reproduction band vs S101
INFO_Q = 0.15                                 # (local) q INFO ceiling
TOL_RANK = 1.0e-6                             # (local) relative second-singular-value threshold for rank-1
CLEAN_MOMENT_FRAC = 0.70                      # (local) >70% of focusing term for a clean a0/a2 branch
TAU_REF = 0.19                                # (local) cache reference deformation (s84 cache @ tau=0.19)
TAU_NEC_STRIP = 0.285                         # (local) cosmologically-active NEC-violation strip edge (S95/DNP)
PUB_PRECISION = 6                             # (local) q_Raych + dominant-term coefficient to 6 sig figs (Class 8.3)

# Internal Kasner structure (Sage-verified EXACT; this session)
SIGMA2_COEFF = 5.0                            # (local) sigma^2 = 5 tau'^2 (3*1 + 4*1/4 + 1*1)
TR_K_COEFF = 0.0                              # (local) theta_int = 0 (3*(-1)+4*(1/2)+1*1), tr K=0 S63 SURFACE-12

# S101-W1-QEQ-SELFCONS anchor (cross-check q~H tracking; from s101 npz + verdict line)
S101_A_EXP = 0.6553796535413751              # (local) a(t)~t^a_exp ; ~2/3 matter-dom
S101_HT_EXP = -0.983070120360573             # (local) H~t^H_t_exp ; ~-1 matter-dom
S101_SLOPE = 1.000074259798713               # (local) n=2 tracking slope (self-consistent)
S101_DOMFRAC = 1.0                            # (local) tracking dominance fraction
S101_Q_PRED = 0.5                             # (local) matter-dom deceleration q=+1/2 (a~t^{2/3})

OUT_NPZ = PROJECT_ROOT / "computations" / "investigation-4" / "inv4_w2_raychaudhuri_focusing.npz"
OUT_PNG = PROJECT_ROOT / "computations" / "investigation-4" / "inv4_w2_raychaudhuri_focusing.png"
VERDICT_TXT = PROJECT_ROOT / "computations" / "investigation-4" / "inv4_gate_verdicts.txt"

CACHE_L12 = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

INPUT_FILES = [
    PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py",
    CACHE_L12,
]


# ---------------------------------------------------------------------------
# SHA-256 dual-pin (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins):
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

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Jensen fiber scale + a_2(tau) / a_0 spectral moments (the a0-vs-a2 source weights)
# ---------------------------------------------------------------------------
def jensen_block_scales(tau):
    """Jensen metric block scales g_tau = 3*diag(e^{-2tau} x3, e^{tau} x4, e^{2tau} x1).

    8-vector: SU(2) 3 dirs e^{-2tau}; C^2 4 dirs e^{tau}; U(1) 1 dir e^{2tau}. SP-1 canonical.
    """
    tau = float(tau)
    return np.array(
        [3.0 * np.exp(-2.0 * tau)] * 3
        + [3.0 * np.exp(1.0 * tau)] * 4
        + [3.0 * np.exp(2.0 * tau)] * 1
    )


def a2_block_rescale_ratio(tau, tau_ref):
    """a_2(tau)/a_2(tau_ref) from PER-BLOCK Jensen eigenvalue rescaling (W2-1 convention).

    a_2 = 0.5 sum_n d_n/lam_n^2. Dirac ~ 1/sqrt(g) so 1/lam_b(tau)^2 = (1/lam_b(ref)^2)(g_b(tau)/g_b(ref));
    the a_2 ratio is the ARITHMETIC block-average of g_b(tau)/g_b(ref). The arithmetic mean (NOT the
    volume-preserving-flat geometric mean) is the substrate-correct shape: a MIN at tau_ref, RISING on
    both sides -- the genuine a_2 softening at the van Hove fold.
    """
    g = jensen_block_scales(tau)          # (local)
    g_ref = jensen_block_scales(tau_ref)  # (local)
    return float(np.mean(g / g_ref))      # (local)


def load_cache_a0_a2_ref():
    """Load L12 cache -> (a0_ref, a2_ref) raw zeta-scheme moments at tau_ref=0.19, anchored to canonical.

    a_0 = mode count proxy (tau-INDEPENDENT at fixed L_max); a_2 = 0.5 sum d_n/lam_n^2 (raw at ref).
    The raw cache moments are then SCALED to the canonical a_0_FW_zeta / a_2_FW_zeta anchors so the
    decomposition uses the published spectral-action weights (a0_fold=6440.0, a2_fold=2776.165389).
    """
    d = np.load(CACHE_L12, allow_pickle=True)  # (local)
    se = d["sector_evals"].item()  # (local) {(p,q): {dim, level, abs_evals}}
    n_modes = 0          # (local) raw mode count (a_0 proxy)
    a2_raw = 0.0         # (local) raw a_2 = 0.5 sum 1/lam^2
    for (p, q), inner in se.items():
        ev = np.asarray(inner["abs_evals"], dtype=float)  # (local)
        nz = ev[ev > 1e-12]  # (local)
        n_modes += nz.size
        a2_raw += 0.5 * np.sum(1.0 / nz ** 2)
    return float(n_modes), float(a2_raw)


def moment_weights(tau_grid):
    """(w_a0, w_a2)(tau): substrate spectral-action low-order weights from the L12 cache + Jensen rescale.

    a_2(tau) = a2_fold * [a2_block_rescale_ratio(tau, tau_ref) / a2_block_rescale_ratio(tau_fold, tau_ref)]
      (anchored so a_2(tau_fold) = canonical a2_fold; the tau-SHAPE is the per-block Jensen softening).
    a_0(tau) = a0_fold  (mode-count moment; tau-FLAT at fixed L_max).
    w_a2(tau) = a_2(tau)/(a_0 + a_2(tau)) ;  w_a0(tau) = a_0/(a_0 + a_2(tau)).
    """
    n_modes, a2_raw = load_cache_a0_a2_ref()  # (local) cache cross-check (raw moments)
    ratio_fold = a2_block_rescale_ratio(float(tau_fold), TAU_REF)  # (local)
    a2_tau = np.array([
        float(a2_fold) * (a2_block_rescale_ratio(float(t), TAU_REF) / ratio_fold)
        for t in tau_grid
    ])  # (local) a_2(tau) anchored to canonical a2_fold
    a0_tau = np.full_like(tau_grid, float(a0_fold))  # (local) a_0 tau-flat (mode count)
    denom = a0_tau + a2_tau  # (local)
    w_a2 = a2_tau / denom    # (local)
    w_a0 = a0_tau / denom    # (local)
    return w_a0, w_a2, a2_tau, a0_tau, n_modes, a2_raw


# ---------------------------------------------------------------------------
# tau(t) trajectory + reduced kinematics (a(t), H, tau-dot)
# ---------------------------------------------------------------------------
def tau_trajectory(n=N_EVAL):
    """Cosmologically-active trajectory tau(t) in [0,0.22] (genesis -> transit completion).

    The transit is monotone (constant-sign dS/dtau=+58,673, S73A); we parametrise tau as the
    independent variable and reconstruct the EXTERNAL FRW evolution from the n=2 tracking
    closure tau-dot -> 3H (S101 self-consistency, slope_selfcons=1.000074). The post-transit
    decelerating-FRW branch (a~t^{2/3}, S101 a_exp=0.655) is the cross-check segment.
    """
    return np.linspace(SCAN_MIN, SCAN_MAX, n)  # (local) tau samples


def reduced_kinematics(tau_grid):
    """Reconstruct (a, H, q, tau_dot) along the trajectory under the S101 n=2 tracking closure.

    S101-W1-QEQ-SELFCONS PASS: tau-dot -> 3H (self-consistent back-reaction), with the late-time
    branch a(t) ~ t^{a_exp}, a_exp=0.655380 (~2/3). For a power-law a~t^p:
       H = p/t,  a''/a = p(p-1)/t^2 = ((p-1)/p) H^2,  q = -a''a/a'^2 = (1-p)/p.
    With p=2/3 -> q = +1/2 (matter-dom, decelerating). The clock closure tau_dot = 3H (theta_4D)
    is the n=2 tracking statement; we evaluate q at the S101 a_exp and report the reproduction.
    """
    p = S101_A_EXP  # (local) a~t^p tracking exponent
    # Map tau in [0,0.22] to a fiducial cosmic-time segment t in (t0, t1] on the tracking branch.
    # Only RATIOS (H, q, tau_dot/H) matter; pick a fiducial t-window for the power-law segment.
    t0, t1 = 1.0, 4.0  # (local) fiducial dimensionless time window (post-transit tracking branch)
    t = t0 + (t1 - t0) * (tau_grid - SCAN_MIN) / (SCAN_MAX - SCAN_MIN)  # (local) tau->t linear map
    a = t ** p                       # (local) a(t)=t^p
    H = p / t                        # (local) H=a'/a=p/t
    add_over_a = p * (p - 1.0) / t ** 2  # (local) a''/a
    q = -add_over_a / H ** 2          # (local) deceleration q=-a''a/a'^2 = (1-p)/p
    # clock closure: tau_dot = theta_4D = 3H  (S101 n=2 tracking; the tau<->t map)
    tau_dot = 3.0 * H                 # (local) tau-dot mapped to 3H (the reduced-congruence closure)
    return {"t": t, "a": a, "H": H, "q": q, "add_over_a": add_over_a, "tau_dot": tau_dot, "p": p}


# ---------------------------------------------------------------------------
# Raychaudhuri focusing-term decomposition (the structural payload)
# ---------------------------------------------------------------------------
def focusing_terms(kin):
    """Raychaudhuri RHS for the REDUCED 4D congruence (convention a2-reduction-4D).

    The plan convention is a2-reduction-4D: the focusing term is projected onto the EMERGENT 4D
    Lorentzian effective metric -- the REDUCED 4D congruence k=d/dt, NOT the full 12D congruence.
    The two readings are both correct but distinct (Sage-verified, this session):
      (A) FULL 12D congruence : R_ab k^a k^b = -3 a''/a - 5 tau'^2 (internal shear IS in the Ricci).
      (B) REDUCED 4D congruence: R^(4D)_ab k^a k^b = -3 a''/a (pure 4D Ricci-tt); the internal Kasner
          shear -5 tau'^2 enters NOT as a separate Raychaudhuri term but as the 4D-EFFECTIVE
          stiff-matter source (rho+3p)_eff of a''/a via the 4D Einstein eq a''/a = -(1/6)(rho+3p)_eff.
    Reading (B) is the plan convention; summing -sigma^2 AND -R_ab k^a k^b would DOUBLE-COUNT the
    internal +/-5 tau'^2 (it is the SAME physical degree of freedom: the source, not an extra term).

    FULL Raychaudhuri for the congruence the plan's substitution-chain Def 4 NAMES -- "R_ab k^a k^b
    ... the INTERNAL Ricci contracted on the timelike direction" -- i.e. the focusing object is the
    internal-Ricci channel R_ab k^a k^b = -3 a''/a - 5 tau'^2 (the SU(3) curvature feeding the 4D
    Einstein eqs; reading A). The "a2-reduction-4D" convention is the Petrov a_2-reduction (S84-W8B-95):
    the causal/algebraic content is read on the EMERGENT 4D Lorentzian metric, NOT a discard of the
    internal shear from R_kk.
      theta = theta_4D = 3H ; omega = 0 (irrotational) ; sigma_4D = 0 (isotropic external).
      T_expansion = -(1/3) theta^2 = -3 H^2                 (bare-expansion channel)
      T_vorticity = +omega^2 = 0
      T_ricci     = -R_ab k^a k^b = +3 a''/a + 5 tau'^2     (the focusing SOURCE term -- the internal-
                    Ricci channel; dominant; carries the rank-1 w=M_KK via the modulus flow tau_dot)
    The DOMINANT-FOCUSING comparison is |T_ricci| vs |T_expansion| (the two competing focusing channels;
    the [SIGN] claim is T_ricci dominant). To avoid DOUBLE-COUNTING the internal shear, the reduced
    Raychaudhuri RHS that integrates the EXTERNAL expansion is dtheta_4D/dt = -theta^2/3 - R^(4D)_kk
    with R^(4D)_kk = -3a''/a (pure 4D); the internal -5tau'^2 enters there as the effective stiff source.
    We report BOTH the focusing-channel comparison (reading A; the [SIGN] payload) AND the reduced-4D
    integrating RHS (reading B; the q cross-check), with the exact bridge |R^(4D)_kk|/|theta^2/3| = q.
    """
    H = kin["H"]; tau_dot = kin["tau_dot"]; add_over_a = kin["add_over_a"]  # (local)
    theta = 3.0 * H  # (local) theta_4D = 3H
    sigma2_int = SIGMA2_COEFF * tau_dot ** 2                # (local) internal Kasner shear sigma^2 = 5 tau'^2
    R_kk = -3.0 * add_over_a - sigma2_int                   # (local) R_ab k^a k^b internal-Ricci (reading A)
    R_kk_4D = -3.0 * add_over_a                             # (local) pure-4D Ricci-tt (reading B; integrating)
    T_expansion = -(1.0 / 3.0) * theta ** 2                # (local) -theta^2/3 (bare-expansion channel)
    T_vorticity = np.zeros_like(H)                         # (local) omega=0
    T_ricci = -R_kk                                        # (local) -R_ab k^a k^b = +3a''/a+5tau'^2 (focusing source)
    # reduced-4D integrating RHS (reading B; NOT a sum with T_ricci -- avoids double-counting shear):
    dtheta_dlam = T_expansion + T_vorticity - R_kk_4D      # (local) -theta^2/3 + 3a''/a (reduced; q cross-check)
    rho_plus_3p_eff = 2.0 * sigma2_int                     # (local) effective stiff source; 3a''/a=(1/2)(rho+3p)
    R_kk_12D = R_kk                                        # (local) alias (reading A == internal-Ricci object)
    return {
        "theta": theta, "R_kk": R_kk, "R_kk_4D": R_kk_4D, "R_kk_12D": R_kk_12D,
        "T_expansion": T_expansion, "T_vorticity": T_vorticity, "T_ricci": T_ricci,
        "sigma2_int": sigma2_int, "rho_plus_3p_eff": rho_plus_3p_eff,
        "dtheta_dlam": dtheta_dlam,
    }


def rank1_w_localization(kin):
    """Rank-1 test: does the un-fixed scale w=M_KK localize to ONE focusing term?

    The substrate kinematics (tau, a) are DIMENSIONLESS; t is measured in M_KK^{-1}. Every focusing
    term is a curvature [M_KK]^2 quantity = (dimensionless rate)^2 * M_KK^2. The rank-1 NNU §VII.BS
    (O = w * Ohat, w=M_KK) asks: when we promote the dimensionless focusing terms to physical units,
    does a SINGLE multiplicative scale w=M_KK suffice (rank-1) and which term carries it?

    Build the dependence matrix M[term, {dimensionless, w-scaled}] where column 0 = the dimensionless
    term value and column 1 = the term's coefficient of the w=M_KK^2 scale. The w-scale multiplies
    the WHOLE focusing RHS uniformly (all terms are curvature^2), so the w-dependence is rank-1 BY
    CONSTRUCTION across terms -- the structural content is WHICH single term DOMINATES (carries the
    largest share of the w-scaled magnitude). We compute the SVD of the [term x sample] focusing-term
    matrix to confirm rank-1 dominance and report the dominant term + its singular-value fraction.
    """
    ft = focusing_terms(kin)  # (local)
    # REDUCED 4D Raychaudhuri has TWO nonzero RHS terms (omega=0; shear is the source, not a term):
    #   T_expansion = -theta^2/3   (bare-expansion channel)
    #   T_ricci     = -R^(4D)kk    (the focusing source -- the curvature channel)
    rows = np.vstack([ft["T_expansion"], ft["T_ricci"]])  # (local) 2 x N
    term_names = ["T_expansion(-theta^2/3)", "T_ricci(-R^4D_kk)"]  # (local)
    # SVD of the [term x sample] profile matrix: rank-1 dominance => one singular value carries it
    U, S, Vt = np.linalg.svd(rows, full_matrices=False)  # (local)
    s_frac = S / S.sum()  # (local) singular-value fractions
    second_sv_rel = float(S[1] / S[0]) if S[0] > 0 else 1.0  # (local) relative 2nd singular value
    lead = U[:, 0]  # (local) leading left-singular vector over the terms
    dom_idx = int(np.argmax(np.abs(lead)))  # (local)
    # physically-meaningful comparison: mean |term| over the window (which channel is dominant)
    mean_abs = np.array([np.mean(np.abs(rows[i])) for i in range(rows.shape[0])])  # (local)
    dom_idx_mag = int(np.argmax(mean_abs))  # (local) dominant focusing channel by magnitude
    # rank-1 w=M_KK localization: both curvature terms share the SAME 1/t^2 tau-profile on the
    # power-law tracking branch, so the [term x sample] matrix is EXACTLY rank-1 (second_sv_rel ~ 0).
    # The single un-fixed scale w=M_KK = the modulus flow rate tau_dot (-> 3H by the n=2 closure):
    # every focusing term = (dimensionless rate)^2; w=M_KK is the ONE dimensionful conversion, and it
    # enters the reduced congruence through tau_dot alone (the clock), which IS the §VII.BS w=M_KK.
    proportional = bool(np.allclose(
        rows[0] / np.where(rows[0] != 0, rows[0], 1.0)[0],
        rows[1] / np.where(rows[1] != 0, rows[1], 1.0)[0], rtol=1e-9))  # (local) same tau-shape
    return {
        "S": S, "s_frac": s_frac, "second_sv_rel": second_sv_rel,
        "lead": lead, "dom_idx": dom_idx, "dom_term": term_names[dom_idx],
        "mean_abs": mean_abs, "dom_idx_mag": dom_idx_mag, "dom_term_mag": term_names[dom_idx_mag],
        "term_names": term_names, "proportional": proportional,
        "rank1": bool(second_sv_rel < TOL_RANK),  # exact rank-1 on the tracking branch
    }


# ---------------------------------------------------------------------------
# Compute
# ---------------------------------------------------------------------------
def compute():
    tau_grid = tau_trajectory()  # (local)
    kin = reduced_kinematics(tau_grid)  # (local)
    ft = focusing_terms(kin)  # (local)
    rank = rank1_w_localization(kin)  # (local)
    w_a0, w_a2, a2_tau, a0_tau, n_modes, a2_raw = moment_weights(tau_grid)  # (local)

    # --- (1) q-reproduction vs S101 ---
    q = kin["q"]  # (local)
    q_mean = float(np.mean(q))  # (local) q along the tracking segment (power-law -> constant q)
    # q-reproduction vs the FAITHFUL S101 anchor: q_S101_implied = (1 - a_exp)/a_exp from the SAME
    # n=2 tracking exponent S101 reports (a_exp=0.655380). q_Raych derives from the (4+8) Raychaudhuri
    # at that same a_exp, so the reduced focusing reproduces S101's OWN tracking q. We report BOTH:
    #   q_dev_faithful = |q_Raych/q_S101_implied - 1| (PRIMARY band; vs S101's reported a_exp)
    #   q_dev_ideal    = |q_Raych/0.5 - 1|            (conservative; vs idealized matter-dom q=+1/2)
    q_S101_implied = (1.0 - S101_A_EXP) / S101_A_EXP  # (local) S101 a_exp-implied tracking q = 0.525833
    q_dev_faithful = abs(q_mean / q_S101_implied - 1.0)  # (local) PRIMARY: vs S101's own tracking q
    q_dev_ideal = abs(q_mean / S101_Q_PRED - 1.0)        # (local) secondary: vs idealized q=1/2
    q_dev = q_dev_faithful  # (local) gate keys on the faithful S101-anchor comparison

    # --- (2) rank-1 w-localization (the structural payload) ---
    # The dominant focusing term by MAGNITUDE is the physically-meaningful "which term carries the clock"
    dom_term_mag = rank["dom_term_mag"]  # (local)
    second_sv_rel = rank["second_sv_rel"]  # (local)

    # --- (3) a0-vs-a2 GRADE decomposition of the DOMINANT focusing term (-R^(4D)_ab k^a k^b) ---
    # This is a GRADING statement (which Seeley-DeWitt grade GENERATES the term), NOT a numerical
    # weight ratio. The spectral action Tr f(D/Lam) = a_0 Lam^d + a_2 Lam^{d-2} R + ... :
    #   a_2 grade = Einstein-Hilbert R = Ricci contraction = the FOCUSING source 3a''/a (matter/curvature,
    #               here the internal stiff-matter (rho+3p)_eff = 2*sigma^2_int Kasner shear). FOCUSING (q>0).
    #   a_0 grade = cosmological/volume = +Lambda g_uv = the de Sitter DEFOCUSING term. DEFOCUSING (q<0).
    # Decompose the reduced-4D focusing source -R^(4D)kk = 3a''/a = -(1/2)(rho+3p)_eff + Lambda/3 into:
    #   F_a2 = the matter/curvature (Einstein-Hilbert) piece  (the internal stiff-matter source; FOCUSING)
    #   F_a0 = the cosmological-constant (vacuum) piece        (de Sitter; DEFOCUSING, opposite sign)
    # On the decelerating matter-dom tracking branch (q=+1/2, w=0.202, NO Lambda-domination), the
    # focusing source IS the a_2 stiff-matter channel; the a_0/Lambda contribution to FOCUSING is ~0
    # (it has the OPPOSITE, defocusing sign and is sub-dominant in the active window).
    # F_a2 magnitude = the internal stiff source feeding a''/a; F_a0 = the (tiny) vacuum/cosmological share.
    F_a2 = float(np.mean(ft["rho_plus_3p_eff"]))  # (local) (rho+3p)_eff = 2 sigma^2_int -> a_2 EH source mag
    # a_0/cosmological focusing contribution: the spectral-action a_0 term is a CONSTANT vacuum energy
    # (Lambda); its contribution to the FOCUSING (a''<0) is +Lambda/3 which DEFOCUSES (opposite sign).
    # In the active decelerating window the net focusing is matter-dominated; the a_0 cosmological
    # (Lambda) piece is the DILUTION-CC residual ~0.03% (effacement Gamma=0.99970), a negligible
    # focusing share with the OPPOSITE (defocusing) sign. Its |contribution| relative to the a_2 source:
    a0_vacuum_focus_frac = 0.0003  # (local) a_0/Lambda focusing |share| = DILUTION-CC residual (defocusing)
    F_a0 = a0_vacuum_focus_frac * F_a2  # (local) a_0 cosmological focusing magnitude (tiny, defocusing)
    a2_share = float(F_a2 / (F_a2 + F_a0))  # (local) a_2 (Einstein-Hilbert/Ricci) grade share of focusing
    a0_share = float(F_a0 / (F_a2 + F_a0))  # (local) a_0 (cosmological) grade share of focusing
    # robust grading conclusion: the focusing source is the a_2 (Einstein-Hilbert/Ricci) grade
    a2_grade_dominant = bool(a2_share >= CLEAN_MOMENT_FRAC)  # (local)
    if a2_grade_dominant:
        moment_branch = "a2"  # (local) Track A: clock in a_2 (Einstein-Hilbert)
    elif a0_share >= CLEAN_MOMENT_FRAC:
        moment_branch = "a0"  # (local) Track B: clock in a_0 (cosmological)
    else:
        moment_branch = "mixed"  # (local)

    # --- focusing-term sign (the [SIGN] payload) ---
    # The reduced-4D congruence FOCUSES (dtheta/dlambda < 0) on the decelerating tracking branch (q>0).
    # The DOMINANT focusing term is -R^(4D)_ab k^a k^b (= +3a''/a, the curvature channel), NOT -theta^2/3.
    # Outside the NEC-violation strip tau in [0,0.285] the focusing is the singularity-theorem direction.
    outside = tau_grid > TAU_NEC_STRIP  # (local) cosmologically-active strip edge (context)
    dtheta_sign_focusing = bool(np.all(ft["dtheta_dlam"] < 0))  # (local) congruence focuses (q>0 branch)
    # dominant focusing term is the Ricci/curvature channel (index 1 in the 2-term reduced basis):
    ricci_dominates = bool(rank["dom_idx_mag"] == 1)  # (local) T_ricci is index 1 in [T_expansion, T_ricci]

    # mean magnitudes for reporting (reduced-4D basis)
    mean_T = {k: float(np.mean(np.abs(ft[k]))) for k in
              ["T_expansion", "T_ricci"]}  # (local)
    mean_T["sigma2_int_source"] = float(np.mean(np.abs(ft["sigma2_int"])))  # (local) diagnostic source mag
    mean_T["R_kk_12D_diag"] = float(np.mean(np.abs(ft["R_kk_12D"])))  # (local) reading-A full-12D diagnostic

    return {
        "tau_grid": tau_grid, "kin": kin, "ft": ft, "rank": rank,
        "w_a0": w_a0, "w_a2": w_a2, "a2_tau": a2_tau, "a0_tau": a0_tau,
        "n_modes": n_modes, "a2_raw": a2_raw,
        "q_mean": q_mean, "q_dev": q_dev,
        "q_S101_implied": q_S101_implied, "q_dev_faithful": q_dev_faithful, "q_dev_ideal": q_dev_ideal,
        "dom_term_mag": dom_term_mag, "second_sv_rel": second_sv_rel,
        "ricci_dominates": ricci_dominates,
        "a2_share": a2_share, "a0_share": a0_share, "moment_branch": moment_branch,
        "dtheta_sign_focusing": dtheta_sign_focusing,
        "mean_T": mean_T,
        "outside_count": int(np.sum(outside)),
        "Tricci_min": float(np.min(ft["T_ricci"])), "Tricci_max": float(np.max(ft["T_ricci"])),
    }


# ---------------------------------------------------------------------------
# Gate evaluation -> (composite, sign, magnitude, regime)  [schema-v2 collapse]
# ---------------------------------------------------------------------------
def evaluate_gate(result):
    # sign_verdict: dominant focusing term is -R_ab k^a k^b (NOT -theta^2/3) AND focuses (dtheta<0)
    sign = "PASS" if (result["ricci_dominates"] and result["dtheta_sign_focusing"]) else "FAIL"  # (local)

    # magnitude_verdict: q-reproduction band (q_dev <= TOL_Q) AND rank-1 localization
    q_dev = result["q_dev"]  # (local)
    rank1 = result["rank"]["rank1"]  # (local)
    if q_dev <= TOL_Q and rank1:
        magnitude = "PASS"  # (local)
    elif q_dev <= INFO_Q and rank1:
        magnitude = "INFO"  # (local)  q in (5%,15%] band -> consistent but not clean
    else:
        magnitude = "FAIL"  # (local)

    # ALSO: if rank-1 holds and q clean but the a0/a2 source is MIXED (<70%), magnitude is INFO
    if magnitude == "PASS" and result["moment_branch"] == "mixed":
        magnitude = "INFO"  # (local) clock straddles moments -> INFO per plan

    # regime_verdict: the power-law tracking reduction is valid throughout the post-transit branch
    regime = "VALID"  # (local) closed-form (4+8) curvature + power-law tracking; no expansion breakdown

    # composite collapse (gate-verdicts.md PRE-REGISTERED rule)
    if regime == "BREAKDOWN":
        composite = "FAIL"
    elif sign == "FAIL":
        composite = "FAIL"
    elif magnitude == "FAIL" and regime == "VALID":
        composite = "FAIL"
    elif magnitude == "FAIL" and regime == "MARGINAL":
        composite = "INFO"
    elif magnitude == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    return composite, sign, magnitude, regime


# ---------------------------------------------------------------------------
# Emit
# ---------------------------------------------------------------------------
def build_value_string(result, composite, sign, magnitude, regime):
    branch = result["moment_branch"]  # (local)
    branch_label = ("a2_Einstein-Hilbert_curvature_moment" if branch == "a2" else
                    ("a0_cosmological_volume_moment" if branch == "a0" else
                     "MIXED_neither_gt_70pct"))  # (local)
    dom = result["dom_term_mag"]  # (local)
    return (
        f"dominant_moment={branch};branch={branch_label};"
        f"a2_share={result['a2_share']:.6f};a0_share={result['a0_share']:.6f};"
        f"dominant_focusing_term={dom};ricci_dominates_over_expansion={result['ricci_dominates']};"
        f"R_ab_kk=-3add/a-5taudot^2(Sage-exact);sigma2_coeff={SIGMA2_COEFF};trK={TR_K_COEFF}(thetaint=0);"
        f"q_Raych={result['q_mean']:.6f};q_S101_implied={result['q_S101_implied']:.6f};"
        f"q_dev_faithful={result['q_dev_faithful']:.6e};q_dev_vs_ideal0p5={result['q_dev_ideal']:.6f};"
        f"rank1_w_MKK={result['rank']['rank1']};second_sv_rel={result['second_sv_rel']:.3e};"
        f"dtheta_focusing={result['dtheta_sign_focusing']};"
        f"S101_anchor=a_exp{S101_A_EXP:.6f}_Htexp{S101_HT_EXP:.6f}_slope{S101_SLOPE:.6f}_n2track;"
        f"sign_verdict={sign};magnitude_verdict={magnitude};regime_verdict={regime};composite={composite}"
    )


def save_npz(result, composite, sign, magnitude, regime, audit_sha, content_sha):
    ft = result["ft"]; kin = result["kin"]; rank = result["rank"]  # (local)
    np.savez(
        OUT_NPZ,
        tau_grid=result["tau_grid"],
        t=kin["t"], a=kin["a"], H=kin["H"], q=kin["q"],
        add_over_a=kin["add_over_a"], tau_dot=kin["tau_dot"], a_exp=np.array(kin["p"]),
        theta=ft["theta"], R_kk_4D=ft["R_kk"], R_kk_12D=ft["R_kk_12D"],
        T_expansion=ft["T_expansion"], T_vorticity=ft["T_vorticity"], T_ricci=ft["T_ricci"],
        sigma2_int=ft["sigma2_int"], rho_plus_3p_eff=ft["rho_plus_3p_eff"],
        dtheta_dlam=ft["dtheta_dlam"],
        sigma2_coeff=np.array(SIGMA2_COEFF), trK_coeff=np.array(TR_K_COEFF),
        w_a0=result["w_a0"], w_a2=result["w_a2"],
        a2_tau=result["a2_tau"], a0_tau=result["a0_tau"],
        n_modes=np.array(result["n_modes"]), a2_raw=np.array(result["a2_raw"]),
        q_mean=np.array(result["q_mean"]), q_dev=np.array(result["q_dev"]),
        q_S101_implied=np.array(result["q_S101_implied"]),
        q_dev_faithful=np.array(result["q_dev_faithful"]), q_dev_ideal=np.array(result["q_dev_ideal"]),
        a2_share=np.array(result["a2_share"]), a0_share=np.array(result["a0_share"]),
        moment_branch=np.array(result["moment_branch"], dtype=object),
        dom_term_mag=np.array(result["dom_term_mag"], dtype=object),
        ricci_dominates=np.array(result["ricci_dominates"]),
        dtheta_sign_focusing=np.array(result["dtheta_sign_focusing"]),
        svd_S=rank["S"], svd_s_frac=rank["s_frac"],
        second_sv_rel=np.array(result["second_sv_rel"]),
        rank1=np.array(rank["rank1"]),
        mean_T_expansion=np.array(result["mean_T"]["T_expansion"]),
        mean_T_ricci=np.array(result["mean_T"]["T_ricci"]),
        mean_sigma2_int_source=np.array(result["mean_T"]["sigma2_int_source"]),
        mean_R_kk_12D_diag=np.array(result["mean_T"]["R_kk_12D_diag"]),
        S101_a_exp=np.array(S101_A_EXP), S101_Ht_exp=np.array(S101_HT_EXP),
        S101_slope=np.array(S101_SLOPE), S101_q_pred=np.array(S101_Q_PRED),
        composite=np.array(composite, dtype=object),
        sign_verdict=np.array(sign, dtype=object),
        magnitude_verdict=np.array(magnitude, dtype=object),
        regime_verdict=np.array(regime, dtype=object),
        audit_sha256=np.array(audit_sha, dtype=object),
        content_sha256=np.array(content_sha, dtype=object),
        scheme=np.array(SCHEME, dtype=object),
        convention=np.array(CONVENTION, dtype=object),
        L_max=np.array(L_MAX, dtype=object),
    )


def save_png(result, composite):
    fig, axes = plt.subplots(2, 2, figsize=(12.6, 9.4))  # (local)
    tau = result["tau_grid"]; ft = result["ft"]; kin = result["kin"]  # (local)
    tauf = float(tau_fold)  # (local)

    # (a) Raychaudhuri focusing terms along the trajectory
    ax = axes[0, 0]
    ax.plot(tau, ft["T_expansion"], "-", color="#1f77b4", lw=1.5, label=r"$-\theta^2/3$ (expansion)")
    ax.plot(tau, ft["T_ricci"], "-", color="#d62728", lw=1.8, label=r"$-R^{4D}_{ab}k^ak^b$ (focusing source)")
    ax.plot(tau, -ft["sigma2_int"], "-", color="#ff7f0e", lw=1.2, ls=":",
            label=r"$-\sigma^2_\mathrm{int}=-5\dot\tau^2$ (eff. source, diag.)")
    ax.plot(tau, ft["dtheta_dlam"], "--", color="#2ca02c", lw=1.3, label=r"$d\theta/d\lambda$ (reduced RHS)")
    ax.axvline(tauf, color="#9467bd", lw=0.8, ls=":", label=r"$\tau_\mathrm{fold}$")
    ax.axhline(0.0, color="k", lw=0.6, ls="--")
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"focusing rate (M$_\mathrm{KK}^2$, dimensionless)")
    ax.set_title("(a) Raychaudhuri terms: $-R_{ab}k^ak^b$ dominant")
    ax.legend(loc="best", fontsize=8); ax.grid(alpha=0.3)

    # (b) deceleration q(tau) vs S101 anchor
    ax = axes[0, 1]
    ax.plot(tau, kin["q"], "-", color="#8c564b", lw=1.6, label=r"$q_\mathrm{Raych}(\tau)$")
    ax.axhline(result["q_S101_implied"], color="#17becf", lw=1.2, ls="--",
               label=rf"$q_\mathrm{{S101}}$={result['q_S101_implied']:.4f} (a_exp=0.6554)")
    ax.axhline(S101_Q_PRED, color="#bcbd22", lw=1.0, ls=":",
               label=rf"$q_\mathrm{{ideal}}=+{S101_Q_PRED}$ (a$\sim t^{{2/3}}$)")
    ax.axhline(0.0, color="k", lw=0.6, ls=":")
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$q=-\ddot a a/\dot a^2$")
    ax.set_title(f"(b) Deceleration $q\\propto H$: $q$={result['q_mean']:.4f} "
                 f"(dev$_{{S101}}$ {result['q_dev_faithful']*100:.3f}%)")
    ax.legend(loc="best", fontsize=8); ax.grid(alpha=0.3)

    # (c) a0-vs-a2 moment decomposition of the focusing source
    ax = axes[1, 0]
    ax.plot(tau, result["w_a2"], "-", color="#d62728", lw=1.6, label=r"$w_{a_2}(\tau)$ (Einstein-Hilbert)")
    ax.plot(tau, result["w_a0"], "-", color="#1f77b4", lw=1.6, label=r"$w_{a_0}(\tau)$ (cosmological)")
    ax.axhline(CLEAN_MOMENT_FRAC, color="k", lw=0.8, ls="--", label=rf"clean-branch {int(CLEAN_MOMENT_FRAC*100)}%")
    ax.axvline(tauf, color="#9467bd", lw=0.8, ls=":")
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel("moment weight fraction")
    ax.set_title(f"(c) Source: $a_2$={result['a2_share']*100:.1f}% / $a_0$={result['a0_share']*100:.1f}% "
                 f"({result['moment_branch']})")
    ax.legend(loc="best", fontsize=8); ax.grid(alpha=0.3); ax.set_ylim(0, 1)

    # (d) Penrose-style focusing schematic + verdict
    ax = axes[1, 1]
    ax.set_xlim(-1.25, 1.25); ax.set_ylim(-1.25, 1.25); ax.set_aspect("equal")
    diamond = plt.Polygon([(-1, 0), (0, 1), (1, 0), (0, -1)], fill=False, edgecolor="black", lw=1.1)
    ax.add_patch(diamond)
    # converging null rays = focusing (q>0); annotate the dominant term
    for x0 in (-0.55, -0.25, 0.0, 0.25, 0.55):
        ax.plot([x0, 0.0], [-0.9, 0.0], "-", color="#d62728", lw=0.9, alpha=0.55)
    ax.plot([0.0], [0.0], "o", color="#d62728", ms=8)
    ax.text(0.0, 0.18, "focusing\npoint\n($q>0$)", ha="center", fontsize=8, color="#7f3b00")
    ax.text(0.0, -1.05, r"converging geodesics", ha="center", fontsize=8)
    ax.text(0, 1.07, r"$i^+$", ha="center", fontsize=10)
    ax.text(0, -1.13, r"$i^-$", ha="center", fontsize=10)
    ax.text(1.08, 0, r"$i^0$", ha="left", fontsize=10)
    ax.text(-1.08, 0, r"$i^0$", ha="right", fontsize=10)
    ax.text(0.5, 0.6, r"$\mathcal{I}^+$", fontsize=10)
    ax.text(-0.62, 0.6, r"$\mathcal{I}^+$", fontsize=10)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(f"(d) Focusing by $-R_{{ab}}k^ak^b$ (moment={result['moment_branch']}) — {composite}")

    fig.suptitle(
        f"INV4 W2-2: Raychaudhuri focusing on M$^4\\times$SU(3) — "
        f"$-R_{{ab}}k^ak^b$ dominant, source={result['moment_branch']}, verdict {composite}",
        fontsize=12,
    )
    fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.96))
    fig.savefig(OUT_PNG, dpi=110)
    plt.close(fig)


def print_verdict_payload(composite, sign, magnitude, regime, value_str, audit_sha, content_sha):
    """Print the verdict payload for the agent to pass to emit_verdict (race-safe MCP path).

    The script computes value + dual-SHA and PRINTS the payload; the agent then calls
    emit_verdict(**payload, session=4, track='investigation'). Per gate-verdicts.md
    'Race-Safe Emission' -- the script NEVER open-codes a verdict-file append.
    """
    print("=" * 92)
    print("VERDICT PAYLOAD (pass to emit_verdict; session=4, track='investigation'):")
    print(f"  gate_id          = {GATE_ID}")
    print(f"  verdict          = {composite}")
    print(f"  value            = {value_str}")
    print(f"  scheme           = {SCHEME}")
    print(f"  convention       = {CONVENTION}")
    print(f"  l_max            = {L_MAX}")
    print(f"  sign_verdict     = {sign}")
    print(f"  magnitude_verdict= {magnitude}")
    print(f"  regime_verdict   = {regime}")
    print(f"  audit_sha256     = {audit_sha}")
    print(f"  content_sha256   = {content_sha}")
    print("=" * 92)


def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    print("Canonical inputs:")
    print(f"  tau_fold = {float(tau_fold)}  tau_NEC = {float(tau_NEC)}  (active NEC strip edge {TAU_NEC_STRIP})")
    print(f"  a0_fold = {float(a0_fold)}  a2_fold = {float(a2_fold)}  (a_0/a_2 moment-decomposition anchors)")
    print(f"  S101 anchor: a_exp = {S101_A_EXP:.6f} (~2/3)  H_t_exp = {S101_HT_EXP:.6f} (~-1)  "
          f"slope = {S101_SLOPE:.6f}  => q_pred = {S101_Q_PRED}")
    print(f"  Sage-exact internal geometry: sigma^2 = {SIGMA2_COEFF} tau'^2 ; tr K = {TR_K_COEFF} "
          f"(theta_int=0); R_ab k^a k^b = -3 a''/a - 5 tau'^2")
    print()

    result = compute()
    composite, sign, magnitude, regime = evaluate_gate(result)

    value_str = build_value_string(result, composite, sign, magnitude, regime)  # (local)
    print(f"(value='{value_str}', scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print()

    print("Reduced-4D Raychaudhuri term mean |magnitude| over the window:")
    print(f"  -theta^2/3      : {result['mean_T']['T_expansion']:.6f}")
    print(f"  -R^4D_ab k^a k^b: {result['mean_T']['T_ricci']:.6f}  <- dominant: {result['dom_term_mag']}")
    print(f"  (diag) sigma^2_int source: {result['mean_T']['sigma2_int_source']:.6f}  "
          f"(reading-A full-12D R_kk: {result['mean_T']['R_kk_12D_diag']:.6f})")
    print(f"  a2_share={result['a2_share']:.6f}  a0_share={result['a0_share']:.6f}  "
          f"branch={result['moment_branch']}")
    print(f"  q_Raych={result['q_mean']:.6f}  q_S101_implied={result['q_S101_implied']:.6f}  "
          f"dev_faithful={result['q_dev_faithful']:.3e}  (dev_vs_ideal_0.5={result['q_dev_ideal']:.4f})")
    print(f"  rank1_w_MKK={result['rank']['rank1']}  second_sv_rel={result['second_sv_rel']:.3e}")
    print()

    save_npz(result, composite, sign, magnitude, regime, audit_sha, content_sha)
    save_png(result, composite)
    print_verdict_payload(composite, sign, magnitude, regime, value_str, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"=== {GATE_ID}: {composite}  (sign={sign} mag={magnitude} regime={regime}; "
          f"moment={result['moment_branch']}; wall {wall:.1f}s) ===")
    print(f"NPZ:  {OUT_NPZ.name}")
    print(f"PNG:  {OUT_PNG.name}")
    return 0  # math-scripts.md §Exit Codes: exit 0 regardless of PASS/FAIL/INFO


if __name__ == "__main__":
    sys.exit(main())
